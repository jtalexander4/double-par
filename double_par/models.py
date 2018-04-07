from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from double_par import db, login_manager


class User(UserMixin, db.Model):
    """
    Create a User table
    """

    # __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class AccountGroup(db.Model):
    """
    Create an Account Group table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    # __tablename__ = 'account_groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    first_number = db.Column(db.Integer)
    last_number = db.Column(db.Integer)
    accounts = db.relationship('AccountChart', backref='account_group',
                               lazy='dynamic')

    def __repr__(self):
        return '<Account Group: {}>'.format(self.name)


class AccountChart(db.Model):
    """
    Create a Chart of Accounts table
    """

    # __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    number = db.Column(db.Integer)
    account_group_id = db.Column(db.Integer, db.ForeignKey(
                                 'account_group.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('account_chart.id'))
    parent = db.relationship("AccountChart", remote_side=[id])
