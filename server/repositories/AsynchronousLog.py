from datetime import datetime
from infrastructure.dbSetup import db
from util import util

class AsynchronousLog(db.Model):

    __tablename__ = 'asynchronous_logs'

    id = db.Column(db.Integer, primary_key=True, default=util.createUUID)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

def add():
    log = AsynchronousLog()
    db.session.add(log)
    db.session.commit()
    db.session.close()