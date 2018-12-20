from app import app, db
from app.auth.models import User, Event, RecipientsGroup, Recipient


@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db, 'User': User, 'Event': Event, 'Recipient': Recipient,
            'RecipientGroup': RecipientsGroup}


if __name__ == '__main__':
    app.run()
