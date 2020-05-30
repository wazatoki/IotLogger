from datetime import datetime
from infrastructure.flaskSetup import db
from util import util

class AsynchronousLog(db.Model):

    __tablename__ = 'asynchronous_logs'

    id = db.Column(db.String, primary_key=True, default=util.createUUID)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    event_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    event_code = db.Column(db.String, nullable=False, default='0000')
    event_category = db.Column(db.String, nullable=False, default='0000')
    event_name = db.Column(db.String, nullable=False, default='0000')

def add():
    log = AsynchronousLog()
    db.session.add(log)
    db.session.commit()
    db.session.close()