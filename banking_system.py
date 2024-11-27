# Function to deposit money into an account
def deposit(account: dict, amount: float) -> None:
    current = account["balance"]
    account["balance"] = current + amount


# Function to withdraw money from an account
def withdraw(account: dict, amount: float) -> None:
    # current = account["balance"]
    # if current > amount:
    if account["balance"] >= amount:
        account["balance"] -= amount


# Function to transfer money between two accounts
def transfer(from_account: dict, to_account: dict, amount: float) -> None:
    fr_balance = from_account["balance"]
    if fr_balance >= amount:
        from_account["balance"] -= amount
        to_account["balance"] += amount


# Function to add a new account to the system
def add_account(accounts: dict, owner: str, initial_balance: float) -> None:
    if owner not in accounts:
        accounts[owner] = {'balance':initial_balance}


# Function to find an account by owner's name
def find_account(accounts: dict, owner: str) -> dict:
    return accounts.get(owner)


# Function to display all accounts in the system
def display_all_accounts(accounts: dict) -> str:
    return "\n".join(
        [f"{owner}: {account['balance']}" for owner, account in accounts.items()]
    )


if __name__ == "__main__":
    ...
    # accounts = {"John": {"balance": 1200}, "Jane": {"balance": 500}}
    # transfer(accounts['John'], accounts["Jane"], 1200)
    # print(accounts)
