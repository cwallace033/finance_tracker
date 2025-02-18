from datetime import datetime

def add_transaction(db, user_id, amount, category, description):
    #Add a transaction for a user
    transaction = {
        'amount': amount,
        'category': category,
        'description': description,
        'timestamp': datetime.now().isoformat()
    }
    db.collection('users').document(user_id).collection('transactions').add(transaction)

    user_ref = db.collection('users').document(user_id)
    user_doc = user_ref.get()

    if user_doc.exists:
        current_balance = user_doc.to_dict().get('balance', 0)
        if category == 'income':
            new_balance = current_balance + amount  
        elif category == 'expense':
            new_balance = current_balance - amount  
        else:
            new_balance = current_balance
        user_ref.update({'balance': new_balance})
        print(f"Transaction added for {user_id}: {description} - ${amount}")
        print(f"New balance: ${new_balance}")
    else:
        print(f"User {user_id} does not exist. Transaction not recorded.")

def update_transaction(db, user_id, transaction_id, new_amount, new_category, new_description):
    # Updating a transaction
    transaction_ref = db.collection('users').document(user_id).collection('transactions').document(transaction_id)
    transaction_doc = transaction_ref.get()
    if transaction_doc.exists:
        transaction_data = transaction_doc.to_dict()
        old_amount = transaction_data['amount']
        old_category = transaction_data['category']
        old_description = transaction_data['description']
        transaction_ref.update({
            'amount': new_amount,
            'category': new_category,
            'description': new_description,
            'timestamp': datetime.now().isoformat()
        })
        user_ref = db.collection('users').document(user_id)
        user_doc = user_ref.get()
        if user_doc.exists:
            current_balance = user_doc.to_dict().get('balance', 0)
            if new_category == 'income':
                current_balance += new_amount
            elif new_category == 'expense':
                current_balance -= new_amount
            else:
                current_balance

            if old_category == 'income':
                current_balance -= old_amount
            elif old_category == 'expense':
                current_balance += old_amount

            user_ref.update({'balance': current_balance})
            print(f"Transaction {transaction_id} updated.")
            print(f"New balance: ${current_balance}")
        else:
            print(f"User {user_id} not found.")


def delete_transaction(db, user_id, transaction_id):
    #Delete a transaction
    transaction_ref = db.collection('users').document(user_id).collection('transactions').document(transaction_id)
    transaction_doc = transaction_ref.get()
    if transaction_doc.exists:
        transaction_data = transaction_doc.to_dict()
        amount = transaction_data['amount']
        category = transaction_data['category']

        # Update the balance
        user_ref = db.collection('users').document(user_id)
        user_doc = user_ref.get()
        if user_doc.exists:
            current_balance = user_doc.to_dict().get('balance', 0)
            new_balance = current_balance - amount if category == 'income' else current_balance + amount
            user_ref.update({'balance': new_balance})
            transaction_ref.delete()
            print(f"Transaction {transaction_id} deleted for {user_id}.")
            print(f"New balance: ${new_balance}")
        else:
            print(f"User {user_id} not found.")




def get_transactions(db, user_id):
    #Retrieve all transactions for a user
    transactions_ref = db.collection('users').document(user_id).collection('transactions')
    docs = transactions_ref.stream()
    return [{doc.id: doc.to_dict()} for doc in docs]

def pretty_print_transactions(transactions):
    print("\nTransaction History:")
    print("=" * 40)
    for transaction in transactions:
        for transaction_id, details in transaction.items():
            print(f"Transaction ID: {transaction_id}")
            print(f"  Amount: ${details.get('amount', 0):.2f}")
            print(f"  Category: {details.get('category', 'N/A').title()}")
            print(f"  Description: {details.get('description', 'No description')}")
            print(f"  Timestamp: {details.get('timestamp', 'Unknown')}")
            print("-" * 40)

def get_transaction_id(db, user_id):
    #Get the most recent transaction ID for a user
    transactions_ref = db.collection('users').document(user_id).collection('transactions')
    docs = transactions_ref.stream()
    transaction_ids = [doc.id for doc in docs]
    if transaction_ids:
        return transaction_ids[-1]
    else:
        return None