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
        new_balance = current_balance + amount if category == 'income' else current_balance - amount
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
            current_balance += (new_amount - old_amount) if new_category == 'income' else current_balance - (new_amount - old_amount)
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