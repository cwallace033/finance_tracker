from dotenv import load_dotenv
from modules.db import initialize_db
from modules.transactions import add_transaction, get_transactions, delete_transaction, update_transaction, get_transaction_id
from modules.reports import generate_report, display_financial_report
from modules.users import create_user

def main():
    #Load the environment variables
    load_dotenv()
    db = initialize_db()
    validate_user = input("Do you have a user ID? (yes/no): ").strip().lower()
    if validate_user == 'no':
        create_user(db)
    user = input("Enter the user ID: ")
    objective = input("Would you like to add, update, or delete a transaction? (add/update/delete/pass): ").strip().lower()

    # Add a sample transaction
    while objective == 'add' or objective == 'update' or objective == 'delete':
        if objective == 'add':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category (income/expense): ").strip().lower()
            description = input("Enter a description: ")
            add_transaction(db, user , amount, category, description)
        elif objective == 'update':
            transaction_id = input("Enter the transaction ID to update: ")
            new_amount = float(input("Enter the new amount: "))
            new_category = input("Enter the new category (income/expense): ").strip().lower()
            new_description = input("Enter the new description: ")
            update_transaction(db, user, transaction_id, new_amount, new_category, new_description)
        elif objective == 'delete':
            transaction_id = input("Enter the transaction ID to delete: ")
            delete_transaction(db, user, transaction_id)
        print (f"Your transaction ID is: {get_transaction_id(db, user)}")
        objective = input("Would you like to add, update, or delete a transaction? (add/update/delete/pass): ").strip().lower()


    # Retrieve and print transactions
    view_transaction = input("Would you like to view transactions? (yes/no): ").strip().lower()
    if view_transaction == 'yes':
        transactions = get_transactions(db, user)
        print("\nTransactions:", transactions)

    # Generate a report
    view_report = input("\nWould you like to generate a financial report? (yes/no): ").strip().lower()
    report = generate_report(db, user)
    if view_report == 'yes':
        generate_report(db, user)
        print("Financial report generated.")
        display_financial_report(report)



if __name__ == "__main__":
    main()