import sqlite3
import random


class BankingSystem:

    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
#         self.cur.execute('DROP TABLE card')
        self.cur.execute('CREATE TABLE card (id INTEGER PRIMARY KEY AUTOINCREMENT, '
                         'number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')

    @staticmethod
    def luhn(card):
        # list numbers of card
        n = list(map(int, list(card)))
        for i in range(len(n) - 1):
            if i % 2 == 0:
                if n[i] * 2 <= 9:
                    n[i] *= 2
                else:
                    n[i] = (n[i] * 2) // 10 + (n[i] * 2) % 10
            control_sum = sum(n[:-1])

        check = ((control_sum // 10) + 1) * 10 - control_sum
        return check == n[-1]

    def create_card(self):
        i = True
        while i:
            card = random.randint(4000000000000000, 4000009999999999)
            if self.luhn(str(card)):
                i = False
        return card

    def menu_acc(self, card):
        while True:
            print('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit''')
            query = input()
            if query == '1':
                self.cur.execute(f'SELECT balance FROM card WHERE number = {card}')
                print('Balance:', self.cur.fetchone()[0])
            elif query == '2':
                print('Enter income:')
                self.cur.execute(f'UPDATE card SET balance = balance + {int(input())} WHERE number = {card}')
                self.conn.commit()
                print('Income was added!')
            elif query == '3':
                print('''Transfer
Enter card number:''')
                trans_card = input()
                self.cur.execute(f'SELECT number FROM card WHERE number = {trans_card}')
                if trans_card == card:
                    print("You can't transfer money to the same account!")
                elif not self.luhn(trans_card):
                    print('Probably you made a mistake in the card number. Please try again!')
                elif not self.cur.fetchone():
                    print('Such a card does not exist.')
                else:
                    print('Enter how much money you want to transfer:')
                    money = int(input())
                    self.cur.execute(f'SELECT balance FROM card WHERE number = {card}')
                    if money > self.cur.fetchone()[0]:
                        print('Not enough money!')
                    else:
                        self.cur.execute(
                            f'UPDATE card SET balance = balance + {money} WHERE number = {trans_card}')
                        self.conn.commit()
                        self.cur.execute(
                            f'UPDATE card SET balance = balance - {money} WHERE number = {card}')
                        self.conn.commit()
                        print('Success!')
            elif query == '4':
                self.cur.execute(f'DELETE FROM card WHERE number = {card}')
                self.conn.commit()
                print('The account has been closed!')
                return True
            elif query == '5':
                print('You have successfully logged out!')
                return True
            elif query == '0':
                return False

    def main_menu(self):
        query = True
        while query:
            print('''1. Create an account
2. Log into account
0. Exit''')
            query = input()
            if query == '0':
                query = False
            elif query == '1':

                self.cur.execute(f'INSERT INTO card(number, pin) VALUES ({self.create_card()},'
                                 f' {str(random.randint(1000, 9999))})')
                self.conn.commit()
                print('''Your card has been created
Your card number:''')
                self.cur.execute(f'SELECT number FROM card WHERE id = (SELECT MAX(id) FROM card)')
                print(self.cur.fetchone()[0])
                print('Your card PIN:')
                self.cur.execute(f'SELECT pin FROM card WHERE id = (SELECT MAX(id) FROM card)')
                print(self.cur.fetchone()[0])
            elif query == '2':
                print('Enter your card number:')
                card = input()
                print('Enter your PIN:')
                pin = input()
                self.cur.execute(f'SELECT number FROM card WHERE number={card}')
                cards = self.cur.fetchone()
                self.cur.execute(f'SELECT pin FROM card WHERE number = {card}')
                pin_card = self.cur.fetchone()
                if cards is not None and card in cards and pin in pin_card:
                    print('You have successfully logged in!')
                    query = self.menu_acc(card)
                else:
                    print('Wrong card number or PIN!')
        print('Bye!')


acc = BankingSystem()
acc.main_menu()
