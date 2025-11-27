from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
import sqlite3
import os
import shutil
import mimetypes

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# --- CONFIGURATION ---
# Use environment variable for the database path, with a fallback to the default.
DB_PATH = os.environ.get('ZOTERO_SQLITE_PATH', os.path.expanduser("~/Zotero/zotero.sqlite"))
TEMP_DB_PATH = "zotero_temp_backend.sqlite"

# Define the base directory for Zotero storage (usually the parent of the sqlite file)
# This might need adjustment based on user's Zotero setup
ZOTERO_STORAGE_BASE_DIR = os.path.join(os.path.dirname(DB_PATH), "storage")


@app.route('/api/attachments', methods=['GET'])
def get_attachments():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 50, type=int)
    offset = (page - 1) * per_page

    attachments = []
    total = 0
    
    # SAFETY: Copy the DB to a temp file to avoid "Database Locked" errors
    if not os.path.exists(DB_PATH):
        return jsonify({"error": f"Error: Could not find database at {DB_PATH}"}), 500

    try:
        shutil.copyfile(DB_PATH, TEMP_DB_PATH)
    except IOError as e:
        return jsonify({"error": f"Error copying database: {e}"}), 500

    con = None
    try:
        con = sqlite3.connect(TEMP_DB_PATH)
        cursor = con.cursor()

        # Get total count
        cursor.execute("SELECT COUNT(*) FROM itemAttachments WHERE path IS NOT NULL")
        total = cursor.fetchone()[0]

        query = """
        SELECT
            ia.itemID,
            ia.path,
            ia.contentType,
            i.key
        FROM itemAttachments ia
        JOIN items i ON ia.parentItemID = i.itemID
        WHERE ia.path IS NOT NULL
        LIMIT ? OFFSET ?
        """
        
        cursor.execute(query, (per_page, offset))
        rows = cursor.fetchall()

        for item_id, path, content_type, parent_item_key in rows:
            name = path.split(':')[-1]
            attachments.append({
                "id": item_id,
                "name": name,
                "type": content_type,
                "path": path,
                "is_local_file": path.startswith("storage:"),
                "parentItemKey": parent_item_key
            })

    except sqlite3.Error as e:
        return jsonify({"error": f"SQL Error: {e}"}), 500
    finally:
        if con:
            con.close()
        if os.path.exists(TEMP_DB_PATH):
            os.remove(TEMP_DB_PATH)

    return jsonify({
        "attachments": attachments,
        "total": total,
        "page": page,
        "per_page": per_page
    })

@app.route('/api/attachments/<int:item_id>/file', methods=['GET'])
def get_attachment_file(item_id):
    file_path = None
    content_type = None

    # SAFETY: Copy the DB to a temp file to avoid "Database Locked" errors
    if not os.path.exists(DB_PATH):
        return jsonify({"error": f"Error: Could not find database at {DB_PATH}"}), 500

    try:
        shutil.copyfile(DB_PATH, TEMP_DB_PATH)
    except IOError as e:
        return jsonify({"error": f"Error copying database: {e}"}), 500

    con = None
    try:
        con = sqlite3.connect(TEMP_DB_PATH)
        cursor = con.cursor()

        query = "SELECT path, contentType FROM itemAttachments WHERE itemID = ?"
        cursor.execute(query, (item_id,))
        result = cursor.fetchone()

        if result:
            db_path_raw, content_type = result
            if db_path_raw.startswith("storage:"):
                # Extract the actual file path from the Zotero storage structure
                # Zotero storage paths are usually like "storage:KEY/filename.pdf"
                # We need to find the actual directory based on the itemID or parentItemID
                # For simplicity, let's assume the filename is directly in a folder named after its key,
                # which is a common pattern for direct storage.
                # A more robust solution might involve querying `items` table for the key.
                
                # To get the storage key for an attachment itemID, we need to query the `items` table.
                key_query = "SELECT key FROM items WHERE itemID = ?"
                cursor.execute(key_query, (item_id,))
                item_key = cursor.fetchone()
                
                if item_key:
                    storage_key = item_key[0]
                    filename_in_db = db_path_raw.split(':')[-1]
                    potential_file_dir = os.path.join(ZOTERO_STORAGE_BASE_DIR, storage_key)
                    
                    # Search for the file in the potential directory
                    for root, _, files in os.walk(potential_file_dir):
                        if filename_in_db in files:
                            file_path = os.path.join(root, filename_in_db)
                            break
                    
                    if not file_path:
                        # Fallback: sometimes the path in DB is just "storage:file.pdf" without a key dir.
                        # This happens for old imports or specific attachment types.
                        # We try to find it directly under storage_key if it's a direct file
                        # or directly under ZOTERO_STORAGE_BASE_DIR if it's a linked file not in a specific folder.
                        # This part might need further refinement for edge cases.
                        file_path_guess = os.path.join(ZOTERO_STORAGE_BASE_DIR, filename_in_db)
                        if os.path.exists(file_path_guess):
                            file_path = file_path_guess
                        
                        if not file_path:
                            # Try finding it in the parent item's storage folder
                            parent_item_id_query = "SELECT parentItemID FROM itemAttachments WHERE itemID = ?"
                            cursor.execute(parent_item_id_query, (item_id,))
                            parent_item_id_result = cursor.fetchone()
                            if parent_item_id_result and parent_item_id_result[0]:
                                parent_key_query = "SELECT key FROM items WHERE itemID = ?"
                                cursor.execute(parent_key_query, (parent_item_id_result[0],))
                                parent_key = cursor.fetchone()
                                if parent_key:
                                    parent_storage_dir = os.path.join(ZOTERO_STORAGE_BASE_DIR, parent_key[0])
                                    for root, _, files in os.walk(parent_storage_dir):
                                        if filename_in_db in files:
                                            file_path = os.path.join(root, filename_in_db)
                                            break

                if not file_path or not os.path.exists(file_path):
                    return jsonify({"error": f"File not found on disk for itemID {item_id}. DB path: {db_path_raw}"}), 404
            else:
                # This is a linked file, the path is absolute or relative to the Zotero data directory
                # For security and simplicity, we will only serve files from within the Zotero storage directory
                # and prevent serving arbitrary files from the system.
                # A more robust solution might handle linked files based on a whitelist of allowed directories.
                return jsonify({"error": f"Serving linked files directly is not supported for itemID {item_id}. Path: {db_path_raw}"}), 400
        else:
            return jsonify({"error": f"Attachment with itemID {item_id} not found in database."}), 404

    except sqlite3.Error as e:
        return jsonify({"error": f"SQL Error: {e}"}), 500
    finally:
        if con:
            con.close()
        if os.path.exists(TEMP_DB_PATH):
            os.remove(TEMP_DB_PATH)

    if file_path and os.path.exists(file_path):
        # Infer mimetype if not provided by DB or if we want to ensure it's correct
        if not content_type:
            content_type, _ = mimetypes.guess_type(file_path)
        
        if content_type:
            return send_file(file_path, mimetype=content_type)
        else:
            return send_file(file_path) # Let Flask guess mimetype
    else:
        return jsonify({"error": f"File path could not be resolved or file does not exist: {file_path}"}), 500

if __name__ == '__main__':
    # It's better to run Flask with 'flask run' in production,
    # but for development, this is fine.
    # Ensure debug is off in production
    app.run(debug=True, port=5000)
