from dotenv import load_dotenv
from modules.db import initialize_db
from modules.transactions import add_transaction, get_transactions
from modules.reports import generate_report

def main():
    #Load the environment variables
    load_dotenv()
    db = initialize_db()

    # Add a sample transaction
    objective = input("Would you like to add, update, or delete a transaction? (add/update/delete): ").strip().lower()
    if objective == 'add':
        user = input("Enter the user ID: ")
        amount = float(input("Enter the amount: "))
        category = input("Enter the category (income/expense): ").strip().lower()
        description = input("Enter a description: ")
        add_transaction(db, user , amount, category, description)
    elif objective == 'update':
        transaction_id = input("Enter the transaction ID to update: ")
        new_amount = float(input("Enter the new amount: "))
        # Update logic would go here
    elif objective == 'delete':
        transaction_id = input("Enter the transaction ID to delete: ")
        # Delete logic would go here

    # Retrieve and print transactions
    transactions = get_transactions(db, 'sample_user')
    print("Transactions:", transactions)

    # Generate a report
    report = generate_report(db, 'sample_user')
    print("Financial Report:", report)



if __name__ == "__main__":
    main()