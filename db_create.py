from double_par import db
from double_par.models import Account

db.create_all()

account1 = Account('Checking', 'checking account')
account2 = Account('Savings', 'savings account')
account3 = Account('Credit Card', 'credit card account')
db.session.add(account1)
db.session.add(account2)
db.session.add(account3)

db.session.commit()


