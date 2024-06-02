class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category):
        self.expenses.append({'amount': amount, 'description': description, 'category': category})

    def categorize_expenses(self):
        categories = {}
        for expense in self.expenses:
            if expense['category'] not in categories:
                categories[expense['category']] = []
            categories[expense['category']].append(expense)
        return categories

    def monthly_summary(self):
        monthly_total = sum(expense['amount'] for expense in self.expenses)
        return monthly_total

    def category_summary(self, category):
        category_total = sum(expense['amount'] for expense in self.expenses if expense['category'] == category)
        return category_total

# User Input
def get_user_input():
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")
    return amount, description, category

# User Interface
def main():
    tracker = ExpenseTracker()
    for _ in range(3):  # Allowing 3 expenses for demonstration purposes
        amount, description, category = get_user_input()
        tracker.add_expense(amount, description, category)

    print("Monthly Summary:", tracker.monthly_summary())
    print("Category-wise Expenditure:", tracker.categorize_expenses())