{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "c8e32a8e-ab32-4789-bb2c-0ec84542be8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "class ExpenseSharing:\n",
    "    def __init__(self, friends):\n",
    "        self.friends = friends\n",
    "        self.balances = {friends: 0 for friends in friends}\n",
    "\n",
    "    def add_expense(self, payer, amount, participants):\n",
    "        split_amount = amount / len(participants)\n",
    "        \n",
    "        for participant in participants:\n",
    "            self.balances[participant] -= split_amount\n",
    "            \n",
    "        self.balances[payer] += amount\n",
    "\n",
    "    def calculate_settlement(self):\n",
    "        creditors = []\n",
    "        debtors = []\n",
    "        \n",
    "        for friend, balance in self.balances.items():\n",
    "            if balance > 0:\n",
    "                creditors.append([friend, balance])\n",
    "            elif balance < 0:\n",
    "                debtors.append([friend, -balance])\n",
    "\n",
    "            while debtors and creditors:\n",
    "                \n",
    "                debtor, debt_amount = debtors.pop()\n",
    "                creditor, credit_amount = creditors.pop()\n",
    "\n",
    "                payment = min(debt_amount, credit_amount)\n",
    "\n",
    "                print(f\"{debtor} owes {creditor}: Rs. {payment:.2f}\")\n",
    "\n",
    "                if debt_amount > payment:\n",
    "                    debtors.append((debtor, debt_amount - payment))\n",
    "                if credit_amount > payment:\n",
    "                    creditors.append((creditor, credit_amount - payment))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "265e3d71-576e-4059-bbc4-e0fd6dc901d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Final Settlement:\n",
      "Dass owes Vasi: Rs. 216.67\n",
      "Gokul owes Vasi: Rs. 1066.67\n",
      "Gokul owes Ajay: Rs. 1733.33\n",
      "God frey owen owes Ajay: Rs. 550.00\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    friends = [\"Ajay\", \"Vasi\", \"Dass\", \"Gokul\", \"God frey owen\"]\n",
    "    expense_sharing = ExpenseSharing(friends)\n",
    "\n",
    "\n",
    "    # sample expenses\n",
    "    expense_sharing.add_expense(\"Ajay\", 5000, [\"Ajay\", \"Vasi\", \"Gokul\", \"Dass\", \"God frey owen\"])          # Paid for Train Tickets\n",
    "    expense_sharing.add_expense(\"Vasi\", 5000, [\"Vasi\", \"Ajay\", \"Dass\", \"God frey owen\"])                   # Paid for Hotel\n",
    "    expense_sharing.add_expense(\"Gokul\", 1000, [\"Ajay\", \"Vasi\", \"Dass\", \"Gokul\", \"God frey owen\"])         # Paid for Local Transport\n",
    "    expense_sharing.add_expense(\"Dass\", 6000, [\"Ajay\", \"Dass\", \"Vasi\", \"Gokul\"])                           # Paid for Event\n",
    "    expense_sharing.add_expense(\"God frey owen\", 3000, [\"Ajay\", \"Vasi\", \"Gokul\", \"Dass\", \"God frey owen\"]) # Paid for Lunch\n",
    "    expense_sharing.add_expense(\"Ajay\", 3500, [\"Vasi\", \"Ajay\", \"Dass\"])                                    # Paid for Party\n",
    "    expense_sharing.add_expense(\"Vasi\", 2500, [\"Ajay\", \"Vasi\", \"Gokul\", \"Dass\", \"God frey owen\"])          # Paid for Dinner\n",
    "    \n",
    "\n",
    "\n",
    "    # calculate settlement\n",
    "    print(\"\\nFinal Settlement:\")\n",
    "    expense_sharing.calculate_settlement()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5108f62f-c690-4018-ad41-caf0c05394ac",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca4f0771-79a9-4a55-be14-3ebde8520f9a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1430f1c-5d44-42bf-b653-41fb59d98eed",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
