class Budget:

    def __init__(self):
        self.income = []
        self.expenses = []

    def main(self):
        while True:
            print("\n Budget Program")
            print("1. Enter Income")
            print("2. Enter Expenses")
            print("3. Show Balance")
            print("4. Show Report")
            print("5. Quit Finance manager")
            pick = input("Choose Your Action 1-5: ")

            if pick == "1":
                money = float(input("Enter income amount: "))
                self.get_income(money)
            elif pick == "2":
                money = float(input("Enter Expenses amount: "))
                self.get_expenses(money)
            elif pick == "3":
                print(f"Your Balance Is: {self.get_balance()}")
            elif pick == "4":
                print("Budget Summary: ")
                print(self.get_report())
            elif pick == "5":
                self.leave_program()
            else:
                print("Invalid choice. Please try again.")

    def get_income(self, money):
        self.income.append(money)

    def get_expenses(self, money):
        self.expenses.append(money)

    def get_balance(self):
        return sum(self.income) - sum(self.expenses)

    def get_report(self):
        report = "Your income:\n"
        for i, money in enumerate(self.income, 1):
            report += f"{i}: {money} \n"
        for i, money in enumerate(self.expenses, 1):
            report += f"{i}: -{money} \n"
        return report

    def leave_program(self):
        print("Thank you! ")
        quit()


if __name__ == "__main__":
    budget = Budget()
    budget.main()