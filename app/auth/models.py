import ldap
from app import db, app
from _datetime import datetime
from flask_login import UserMixin


def get_ldap_connection():
    return ldap.initialize(app.config['LDAP_PROVIDER_URL'])


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def try_login(username, password):
        conn = get_ldap_connection()
        conn.simple_bind_s(username + app.config['DOMAIN'], password)
        base_dn = app.config['BASE_DN']
        searchfilter = "(&(objectClass=person)(sAMAccountName={}))".format(username)
        request_enable_members = conn.search_s(base_dn, ldap.SCOPE_SUBTREE, searchfilter, None)
        if bytes(app.config['FILTER_GROUP'], encoding='utf-8') in \
                request_enable_members[0][1]['memberOf']:
            return True
        else:
            raise ldap.INVALID_CREDENTIALS

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class Recipient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('recipients_group.id'))
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return self.email


class RecipientsGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
