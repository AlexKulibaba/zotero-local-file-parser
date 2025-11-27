# Project Overview

This project consists of a collection of Python scripts designed to interact with the Zotero SQLite database. The primary purpose is to parse and extract information about Zotero attachments and to document the database schema.

**Main Technologies:**
*   Python 3
*   SQLite

**Architecture:**
The project is composed of standalone Python scripts that connect to the local Zotero database file. The scripts copy the database to a temporary location to avoid conflicts with a running Zotero application.

# Building and Running

There is no build process for this project. The scripts can be run directly using Python.

**Running the Scripts:**

*   **List Zotero Attachments:**
    ```bash
    python3 list_zotero_pdfs.py
    ```
    This script extracts information about attachments from your Zotero library and saves it to `zotero_attachments.csv`.

*   **Debug Zotero Database:**
    ```bash
    python3 debug_zotero.py
    ```
    This script runs diagnostics on your Zotero database to ensure it's accessible and contains the expected data.

*   **Document Database Schema:**
    ```bash
    python3 document_database.py
    ```
    This script generates a Markdown file named `database_schema.md` that documents the schema of your Zotero database.

# Development Conventions

*   **Style:** The code follows standard Python conventions (PEP 8).
*   **Database Interaction:** All scripts that interact with the Zotero database first copy it to a temporary file to prevent locking issues. The temporary file is cleaned up after the script finishes.
*   **Modularity:** Each script is self-contained and serves a specific purpose.
