class ExpenseSplitter:
    def __init__(self):
        self.balances = {}

    def add_user(self, name):
        if name not in self.balances:
            self.balances[name] = 0

    def add_expense(self, payer, amount, participants):
        # Ek person ne pay kiya, sab mein divide hoga
        share = amount / len(participants)
        self.balances[payer] += amount
        
        for p in participants:
            self.balances[p] -= share

    def show_balances(self):
        print("\n--- Current Status ---")
        for user, bal in self.balances.items():
            if bal > 0:
                print(f"{user} ko {round(bal, 2)} milne chahiye.")
            elif bal < 0:
                print(f"{user} ko {round(abs(bal), 2)} dene hain.")
            else:
                print(f"{user} ka hisaab barabar hai.")

# Usage
app = ExpenseSplitter()
app.add_user("Amit")
app.add_user("Rahul")
app.add_user("Sana")

# Amit ne 300 diye dinner ke liye, jo teeno mein batenge
app.add_expense("Amit", 300, ["Amit", "Rahul", "Sana"])
app.show_balances()