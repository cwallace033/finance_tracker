def generate_report(db, user_id):
    # Generate a financial report for a user
    transactions_ref = db.collection('users').document(user_id).collection('transactions')
    transactions = transactions_ref.stream()

    income = 0
    expenses = 0
    details = []

    for doc in transactions:
        data = doc.to_dict()
        details.append(data)
        if data['category'] == 'income':
            income += data['amount']
        else:
            expenses += data['amount']
    
    balance = income - expenses
    return {
        'income': income,
        'expenses': expenses,
        'balance': balance,
        'transactions': details
    }

def display_financial_report(report):
    # Prints the financial report all pretty 
    print("\n=== Financial Report ===")
    print(f"Total Income: ${report['income']:.2f}")
    print(f"Total Expenses: ${report['expenses']:.2f}")
    print(f"Balance: ${report['balance']:.2f}")
    print(f"Number of Transactions: {len(report['transactions'])}")
    print("========================\n")
