# expense tracker project
expences = [] # list to store expenses in form of dict
print("Welcome to Expense Tracker")
while True:
    print("=====MENU=====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3.view total kharcha")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

# Add Expense
    if choice == 1:
        date = input("Enter date : ")
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Transport): ")
        description = input("Enter description: ")
        expense = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        expences.append(expense)
        print("\n WELL DONE!!Expense added successfully!")
# View Expenses
    elif choice == 2:
        if (len(expences) == 0):
            print("\nNo expenses recorded.Jao phele kharcha kro.")
        else:
            print("\nAll Expenses:")
            count = 1
            for each_expense in expences:
                print(f"{count}. Date: {each_expense['date']}, Amount: {each_expense['amount']}, Category: {each_expense['category']}, Description: {each_expense['description']}")
                count += 1
# View Total Expense
    elif choice == 3:
        if (len(expences) == 0):
          print("\nNo expenses recorded.Jao phele kharcha kro.")
        else:
             total_expense= sum(item['amount'] for item in expences)
             print(f"\nTotal Expense: ₹{total_expense}")
#exit
    elif choice == 4:
        print("THANKU FOR USING EXPENSE TRACKER 🫶. Goodbye!")
        break
             

            
        

            