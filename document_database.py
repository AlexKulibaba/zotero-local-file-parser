import sqlite3
import os
import shutil

# --- CONFIGURATION ---
db_path = os.path.expanduser("~/Zotero/zotero.sqlite")
temp_path = "zotero_temp_docs.sqlite"
output_md_path = "database_schema.md"

def document_database():
    if not os.path.exists(db_path):
        print(f"Error: Could not find database at {db_path}")
        return

    try:
        shutil.copyfile(db_path, temp_path)
    except IOError as e:
        print(f"Error copying database: {e}")
        return

    try:
        con = sqlite3.connect(temp_path)
        cursor = con.cursor()

        # Get list of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        with open(output_md_path, 'w', encoding='utf-8') as md_file:
            md_file.write("# Zotero Database Schema\n\n")

            for table in tables:
                table_name = table[0]
                md_file.write(f"## Table: `{table_name}`\n\n")

                # Get table schema
                md_file.write("### Schema\n\n")
                md_file.write("| Column Name | Data Type | Not Null | Default Value | Primary Key |\n")
                md_file.write("|-------------|-----------|----------|---------------|-------------|\n")
                cursor.execute(f"PRAGMA table_info({table_name});")
                schema = cursor.fetchall()
                for column in schema:
                    md_file.write(f"| {column[1]} | {column[2]} | {bool(column[3])} | {column[4]} | {bool(column[5])} |\n")
                md_file.write("\n")

                # Get sample data
                md_file.write("### Sample Data (first 5 rows)\n\n")
                try:
                    cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
                    sample_data = cursor.fetchall()
                    if sample_data:
                        # Get column names for the header
                        column_names = [description[0] for description in cursor.description]
                        md_file.write(f"| {' | '.join(column_names)} |\n")
                        md_file.write(f"|{'|'.join(['---'] * len(column_names))}|")
                        for row in sample_data:
                            sanitized_row = []
                            for item in row:
                                if isinstance(item, (str, bytes)) and len(item) > 100:
                                    item = str(item[:100]) + '... [truncated]'
                                sanitized_row.append(str(item).replace('|', '\\|'))
                            md_file.write(f"| {' | '.join(sanitized_row)} |\n")
                    else:
                        md_file.write("No data in this table.\n")
                except sqlite3.OperationalError as e:
                    md_file.write(f"Could not retrieve sample data: {e}\n")

                md_file.write("\n")

        con.close()
        print(f"Successfully documented database schema to {output_md_path}")

    except (sqlite3.Error, IOError) as e:
        print(f"An error occurred: {e}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    document_database()