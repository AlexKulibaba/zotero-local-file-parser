import sqlite3
import os
import shutil
import csv

# --- CONFIGURATION ---
# Standard path for macOS. 
# If you are on Windows, change to: os.path.expanduser("~/Zotero/zotero.sqlite")
db_path = os.path.expanduser("~/Zotero/zotero.sqlite")
temp_path = "zotero_temp_debug.sqlite"
output_csv_path = "zotero_attachments.csv"

def run_simple_query():
    # 1. SAFETY: Copy the DB to a temp file to avoid "Database Locked" errors
    # This happens because Zotero locks the file while the app is running.
    if not os.path.exists(db_path):
        print(f"Error: Could not find database at {db_path}")
        return

    try:
        shutil.copyfile(db_path, temp_path)
    except IOError as e:
        print(f"Error copying database: {e}")
        return

    try:
        # 2. CONNECT to the temporary copy
        con = sqlite3.connect(temp_path)
        cursor = con.cursor()

        # 3. YOUR QUERY
        query = """
        SELECT path, contentType 
        FROM itemAttachments 
        WHERE path IS NOT NULL 
        LIMIT 50
        """
        
        print(f"Running query on: {db_path} (via temp copy)\n")
        cursor.execute(query)
        rows = cursor.fetchall()

        # 4. WRITE RESULTS TO CSV
        if not rows:
            print("No attachments found with that query.")
        else:
            with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Name', 'Type', 'Path']) # Write header

                for path, content_type in rows:
                    name = path.split(':')[-1]
                    csv_writer.writerow([name, content_type, path])
            print(f"Successfully saved {len(rows)} attachments to {output_csv_path}")

        con.close()

    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        # 5. CLEANUP: Delete the temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    run_simple_query()