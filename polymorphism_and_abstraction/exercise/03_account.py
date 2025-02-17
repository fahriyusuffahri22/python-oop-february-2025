from __future__ import annotations
from typing import List, Any


class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    @property
    def balance(self) -> int:
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount: int) -> str:
        if 0 > self.balance + transaction_amount:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount: Any) -> str:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        return self.handle_transaction(amount)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, item: int):
        return self._transactions[item]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other: Account):
        return self.balance > other.balance

    def __lt__(self, other: Account):
        return self.balance < other.balance

    def __ge__(self, other: Account):
        return self.balance >= other.balance

    def __le__(self, other: Account):
        return self.balance < other.balance

    def __eq__ (self, other: Account):
        return self.balance == other.balance

    def __ne__ (self, other: Account):
        return self.balance != other.balance

    def __add__(self, other: Account):
        account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        account._transactions += self._transactions + other._transactions
        return account