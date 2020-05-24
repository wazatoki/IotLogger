from datetime import datetime
from infrastructure.dbSetup import db
from util import util

class CycleLog(db.Model):

    __tablename__ = 'cycle_logs'

    id = db.Column(db.Integer, primary_key=True, default=util.createUUID)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)