# Expense Tracker (CLI)

A command-line expense tracker built with Python and SQLite. It needs no external libraries, only Python 3.

## Features
- Add expenses with an amount, category, optional note and date
- List all expenses in a table with a total
- Delete an expense by its id
- See total spending per category
- Input validation for amounts and dates

## Setup
```bash
git clone https://github.com/mayurcodes117/-expense-tracker..git
cd -expense-tracker.
python main.py --help
```

## Usage
```bash
python main.py add 250 food -n "Lunch"
python main.py add 1200 transport -d 2026-10-01
python main.py list
python main.py summary
python main.py delete 3
```

## Example output
```
ID   Date        Category        Amount  Note
-------------------------------------------------------
2    2026-10-04  transport      1200.00
1    2026-10-04  food            250.00  Lunch
-------------------------------------------------------
Total                           1450.00
```

## Project structure
- `main.py`: command-line interface (argparse) and output formatting
- `db.py`: database functions (SQLite)

## What I learned
- Working with SQLite using Python's `sqlite3` module
- Building a command-line interface with `argparse`
- Basic SQL: `INSERT`, `SELECT`, `DELETE`, `GROUP BY`
- Validating user input
- Using Git and GitHub

## Future improvements
- Filter expenses by month and category
- Monthly budgets with alerts
- Export to CSV
- Flask web version
