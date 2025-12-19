#!/usr/bin/env python3
"""
Database File Scanner

This script scans a directory and its subdirectories for SQLite database files
(.db extension) and checks if they contain a table named 'menu_items'.
"""

import os
import sqlite3
import sys


def scan_for_databases(directory):
    """
    Scan directory and subdirectories for .db files.
    
    Args:
        directory (str): Path to the directory to scan
        
    Returns:
        list: List of paths to .db files found
    """
    db_files = []
    
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.db'):
                    db_path = os.path.join(root, file)
                    db_files.append(db_path)
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Error scanning directory: {e}")
    
    return db_files


def check_menu_items_table(db_path):
    """
    Check if a database contains a 'menu_items' table.
    
    Args:
        db_path (str): Path to the database file
        
    Returns:
        bool: True if 'menu_items' table exists, False otherwise
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Query to check if table exists
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='menu_items'
        """)
        
        result = cursor.fetchone()
        return result is not None
        
    except sqlite3.Error as e:
        print(f"  Error reading database {db_path}: {e}")
        return False
    except Exception as e:
        print(f"  Unexpected error with {db_path}: {e}")
        return False
    finally:
        if conn:
            conn.close()


def main():
    """Main function to scan for databases and check for menu_items table."""
    # Get directory from command line argument or use current directory
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()
    
    # Validate directory exists
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory")
        sys.exit(1)
    
    print(f"Scanning directory: {directory}")
    print("-" * 60)
    
    # Find all database files
    db_files = scan_for_databases(directory)
    
    if not db_files:
        print("No database files (.db) found.")
        return
    
    print(f"Found {len(db_files)} database file(s):\n")
    
    # Check each database for menu_items table
    found_menu_items = []
    
    for db_path in db_files:
        print(f"Checking: {db_path}")
        has_menu_items = check_menu_items_table(db_path)
        
        if has_menu_items:
            print("  ✓ Contains 'menu_items' table")
            found_menu_items.append(db_path)
        else:
            print("  ✗ Does not contain 'menu_items' table")
    
    print("\n" + "=" * 60)
    print("Summary:")
    print(f"Total databases scanned: {len(db_files)}")
    print(f"Databases with 'menu_items' table: {len(found_menu_items)}")
    
    if found_menu_items:
        print("\nDatabases containing 'menu_items' table:")
        for db in found_menu_items:
            print(f"  - {db}")


if __name__ == "__main__":
    main()
