from app import app, db
from app.models import Worklog, User, Ticket 

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Worklog' : Worklog, 'User': User, 'Ticket': Ticket}