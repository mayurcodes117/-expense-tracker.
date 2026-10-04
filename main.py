import argparse
from datetime import date, datetime
import db

def positive_amount(value):
    try:
        amount = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Amount must be a number")
    if amount <= 0:
        raise argparse.ArgumentTypeError("Amount must be greater than 0")
    return amount


def valid_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be in YYYY-MM-DD format")

def build_parser():
    parser = argparse.ArgumentParser(description="Simple expense tracker")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="Add a new expense")
    add.add_argument("amount", type=positive_amount)
    add.add_argument("category")
    add.add_argument("-n", "--note", default="")
    add.add_argument("-d", "--date", type=valid_date, default=date.today().isoformat()) 
    sub.add_parser("list", help="Show all expenses")

    rm = sub.add_parser("delete", help="Delete an expense by id")
    rm.add_argument("id", type=int)
    sub.add_parser("summary", help="Total spent per category")
    return parser


def print_table(rows):
    if not rows:
        print("No expenses found.")
        return

    print(f"{'ID':<4} {'Date':<11} {'Category':<12} {'Amount':>10}  Note")
    print("-" * 55)
    total = 0
    for row in rows:
        print(f"{row['id']:<4} {row['date']:<11} {row['category']:<12} {row['amount']:>10.2f}  {row['note']}")
        total += row["amount"]
    print("-" * 55)
    print(f"{'Total':<28} {total:>10.2f}")


def main():
    db.init_db()
    args = build_parser().parse_args()

    if args.command == "add":
        new_id = db.add_expense(args.amount, args.category, args.note, args.date)
        print(f"Added expense #{new_id}: {args.amount} on {args.category}")

    elif args.command == "list":
        print_table(db.list_expenses())

    elif args.command == "delete":
        if db.delete_expense(args.id):
            print(f"Deleted expense #{args.id}")
        else:
            print(f"No expense with id {args.id}")
    elif args.command == "summary":
        rows = db.summary_by_category()
        if not rows:
            print("No expenses found.")
        for row in rows:
            print(f"{row['category']:<12} {row['total']:>10.2f}")    

if __name__ == "__main__":
    main()