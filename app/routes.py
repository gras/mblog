from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm
from app.models import Worklog, User, Ticket
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/load')
def data_load():
    
    u = User(userid='grasmed',fullname='Jon Gras')
    db.session.add(u)
    
    t = Ticket(ticket='REQ-1234',sponsor='OAA',status='In Process',
               title='Do this work for me')
    db.session.add(t)

    w = Worklog(workdate=datetime.now(), hours= 2.5, message='did work',
                u_log=u, t_log=t)
    db.session.add(w)

    db.session.commit()
    return 'Loaded'

@app.route('/view')
def data_view():
    result = ''
    
    users = User.query.all()
    for u in users:
        result += str(u.id) +' '+ u.userid +' '
        
    tickets = Ticket.query.all()
    for t in tickets:
        result += t.sponsor +' '+ t.ticket +' '
        
    worklogs = Worklog.query.all()
    for w in worklogs:
        result += w.message +' '+ str(w.hours ) +' '+ w.u_log.userid +" "+ w.t_log.sponsor
    
    return result

@app.route('/delete')
def data_delete():
    users = User.query.all()
    for u in users:
        db.session.delete(u)
        
    tickets = Ticket.query.all()
    for t in tickets:
        db.session.delete(t)
        
    worklogs = Worklog.query.all()
    for w in worklogs:
        db.session.delete(w)
        
    db.session.commit()
    
    return 'Deleted'
