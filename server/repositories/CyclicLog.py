from datetime import datetime
from infrastructure.flaskSetup import db
from util import util

class CyclicLog(db.Model):

    __tablename__ = 'cyclic_logs'

    id = db.Column(db.String, primary_key=True, default=util.createUUID)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    speed = db.Column(db.Integer, nullable=False, default=-32000)
    flow = db.Column(db.REAL, nullable=False, default=-32000)
    pven = db.Column(db.Integer, nullable=False, default=-32000)
    pint = db.Column(db.Integer, nullable=False, default=-32000)
    deltap = db.Column(db.Integer, nullable=False, default=-32000)
    part = db.Column(db.Integer, nullable=False, default=-32000)
    tven = db.Column(db.REAL, nullable=False, default=-32000)
    tart = db.Column(db.REAL, nullable=False, default=-32000)
    svo2 = db.Column(db.REAL, nullable=False, default=-32000)
    hct = db.Column(db.REAL, nullable=False, default=-32000)