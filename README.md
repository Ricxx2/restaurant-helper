# restaurant-helper
Utility to scan files and identify menu database

## Overview

This tool scans a directory and its subdirectories for SQLite database files (`.db` extension) and checks if they contain a table named `menu_items`.

## Requirements

- Python 3.x (no additional dependencies required - uses standard library)

## Usage

### Basic Usage

Scan the current directory:
```bash
python3 db_scanner.py
```

### Scan a Specific Directory

Provide a directory path as an argument:
```bash
python3 db_scanner.py /path/to/directory
```

### Example Output

```
Scanning directory: test_data
------------------------------------------------------------
Found 3 database file(s):

Checking: test_data/other.db
  ✗ Does not contain 'menu_items' table
Checking: test_data/restaurant.db
  ✓ Contains 'menu_items' table
Checking: test_data/subdir/menu.db
  ✓ Contains 'menu_items' table

============================================================
Summary:
Total databases scanned: 3
Databases with 'menu_items' table: 2

Databases containing 'menu_items' table:
  - test_data/restaurant.db
  - test_data/subdir/menu.db
```

## Features

- **Recursive Scanning**: Automatically scans all subdirectories
- **SQLite Support**: Specifically designed for SQLite database files
- **Error Handling**: Gracefully handles permission errors and corrupted databases
- **Clear Output**: Provides detailed results with visual indicators (✓/✗)
- **Summary Report**: Shows total counts and lists databases containing the target table

## How It Works

1. The script walks through the specified directory and all subdirectories
2. Identifies files with `.db` extension
3. For each database file found:
   - Attempts to connect to the database
   - Queries the `sqlite_master` table to check for a table named `menu_items`
   - Reports whether the table exists
4. Provides a summary of all findings

## Error Handling

The scanner handles common errors gracefully:
- Permission denied errors when accessing directories
- Invalid or corrupted database files
- Non-existent directory paths
