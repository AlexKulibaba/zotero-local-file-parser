import sqlite3
import os

# --- CONFIG ---
# Ensure this matches the path printed in your error message
db_path = os.path.expanduser("~/Zotero/zotero.sqlite")

def run_diagnostic():
    if not os.path.exists(db_path):
        print(f"❌ CRITICAL: No database found at {db_path}")
        print("   Please open Zotero -> Edit -> Settings -> Advanced -> Files and Folders")
        print("   to check your actual Data Directory location.")
        return

    print(f"✅ Database found at: {db_path}")
    
    try:
        con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        cursor = con.cursor()
        
        # 1. Check if table exists and get total count of ALL items
        cursor.execute("SELECT count(*) FROM items")
        total_items = cursor.fetchone()[0]
        print(f"📊 Total items in DB (folders, notes, papers, everything): {total_items}")

        # 2. Check specifically for Attachments (files)
        # We query the 'itemAttachments' table directly without joining titles
        query = """
        SELECT itemID, path, contentType 
        FROM itemAttachments 
        WHERE path IS NOT NULL 
        LIMIT 10
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        print(f"\n🔎 Sampling first 10 file attachments directly from DB:")
        print("-" * 60)
        if not rows:
            print("❌ No attachments found in 'itemAttachments' table.")
        
        for item_id, path, content_type in rows:
            print(f"ID: {item_id} | Type: {content_type} | Path: {path}")
            
        print("-" * 60)
        print("\n🤔 DIAGNOSIS:")
        if not rows:
            print("   The DB is empty of files. Are you using the right profile?")
        elif "storage:" not in rows[0][1]:
            print("   ⚠️ You are likely using LINKED files (not stored).")
            print("   The previous script filtered for 'storage:'. We need to adjust it.")
        else:
            print("   Files look standard. The previous script failed on the 'Title' Join.")
            
        con.close()

    except Exception as e:
        print(f"❌ SQL Error: {e}")

if __name__ == "__main__":
    run_diagnostic()