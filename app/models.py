from datetime import datetime
from app import db

class Worklog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workdate = db.Column(db.DateTime, index=True)
    hours = db.Column(db.Float)
    message = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))

    def __repr__(self):
        return '<Worklog {} {}>'.format(self.message, self.hours)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(64), index=True, unique=True)
    fullname = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    u_worklogs = db.relationship('Worklog', backref='u_log', lazy='dynamic')

    def __repr__(self):
        return '<User {} {}>'.format(self.id, self.userid)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.String(10), index=True, unique=True)
    sponsor = db.Column(db.String(10))
    status = db.Column(db.String(15))
    title = db.Column(db.String(100))
    t_worklogs = db.relationship('Worklog', backref='t_log', lazy='dynamic')

    def __repr__(self):
        return '<Ticket {} {}>'.format(self.sponsor, self.ticket)