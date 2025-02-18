from dotenv import load_dotenv
from modules.db import initialize_db
from modules.transactions import add_transaction, get_transactions, delete_transaction, update_transaction, get_transaction_id, pretty_print_transactions
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

    # View balance, transactions, or generate a report
    select_action = input("Would you like to modify transaction, view transactions, or generate a report? (modify/view/report/end): ").strip().lower()
    while select_action != 'end':
        if select_action == 'modify':
            # modify transactions
            objective = input("Would you like to add, update, or delete a transaction? (add/update/delete/pass): ").strip().lower()
            while objective == 'add' or objective == 'update' or objective == 'delete':
                if objective == 'add':
                    amount = float(input("Enter the amount: "))
                    category = input("Enter the category (income/expense): ").strip().lower()
                    description = input("Enter a description: ")
                    add_transaction(db, user , amount, category, description)
                    print (f"Your transaction ID is: {get_transaction_id(db, user)}")

                elif objective == 'update':
                    transaction_id = input("Enter the transaction ID to update: ")
                    new_amount = float(input("Enter the new amount: "))
                    new_category = input("Enter the new category (income/expense): ").strip().lower()
                    new_description = input("Enter the new description: ")
                    update_transaction(db, user, transaction_id, new_amount, new_category, new_description)
                elif objective == 'delete':
                    transaction_id = input("Enter the transaction ID to delete: ")
                    delete_transaction(db, user, transaction_id)
                objective = input("Would you like to add, update, or delete a transaction? (add/update/delete/pass): ").strip().lower()
        
        # Retrieve and print transactions
        elif select_action == 'view':
            transactions = get_transactions(db, user)
            pretty_print_transactions(transactions)

        # Generate a report
        elif select_action == 'report':
            report = generate_report(db, user)
            print("Financial report generated.")
            display_financial_report(report)

        select_action = input("Would you like to modify transaction, view transactions, or generate a report? (modify/view/report/end): ").strip().lower()



if __name__ == "__main__":
    main()