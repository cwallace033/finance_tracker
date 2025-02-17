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

def get_transactions(db, user_id):
    #Retrieve all transactions for a user
    transactions_ref = db.collection('users').document(user_id).collection('transactions')
    docs = transactions_ref.stream()
    return [{doc.id: doc.to_dict()} for doc in docs]