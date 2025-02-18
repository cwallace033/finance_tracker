

def create_user(db):
    # Create a user
    creation = input("Would you like to create a user? (yes/no): ").strip().lower()
    if creation == 'no':
        quit()
    user_id = input("Enter the user ID: ")
    user_email = input("Enter a user email: ")
    user_balance = float(input("Enter your balance: "))
    doc_ref = db.collection('users').document(user_id)
    doc_ref.set({
        'name': user_id,
        'email': user_email,
        'balance': user_balance
    })

    print("User create successfully.")

