from datetime import datetime
import typing as tp

from sqlalchemy import and_

from infrastructure.flaskSetup import db
from util import util
from domain import cyclic_data

class CyclicLog(db.Model):

    __tablename__ = 'cyclic_logs'

    id = db.Column(db.String, primary_key=True, default=util.createUUID)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    is_parsed = db.Column(db.Boolean, nullable=False, default=False)
    event_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
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


def map_to_entity(c: tp.Type[cyclic_data.Log_data]):
    log = CyclicLog()
    log.event_date = c.dt
    log.speed = c.speed
    log.flow = c.flow
    log.pven = c.pven
    log.pint = c.pint
    log.deltap = c.deltap
    log.part = c.part
    log.tven = c.tven
    log.tart = c.tart
    log.svo2 = c.svo2
    log.hct = c.hct
    return log

def map_to_object(c: tp.Type[CyclicLog]):
    data = cyclic_data.Log_data()
    data.dt = c.event_date
    data.speed = c.speed
    data.flow = c.flow
    data.pven = c.pven
    data.pint = c.pint
    data.deltap = c.deltap
    data.part = c.part
    data.tven = c.tven
    data.tart = c.tart
    data.svo2 = c.svo2
    data.hct = c.hct
    return data

def add(c: tp.Type[cyclic_data.Log_data]):
    log = CyclicLog()
    log.event_date = c.dt
    log.speed = c.speed
    log.flow = c.flow
    log.pven = c.pven
    log.pint = c.pint
    log.deltap = c.deltap
    log.part = c.part
    log.tven = c.tven
    log.tart = c.tart
    log.svo2 = c.svo2
    log.hct = c.hct

    db.session.add(log)
    db.session.commit()

def mark_parsed_logs(f, t):
    items = CyclicLog.query.filter(and_(CyclicLog.event_date >= f, CyclicLog.event_date <= t, CyclicLog.is_parsed == False )).all()
    
    for item in items:
        item.is_parsed = True
        db.session.commit()

def find_first_not_Parsed():
    items = CyclicLog.query.filter(CyclicLog.is_parsed == False)\
        .order_by(CyclicLog.event_date)\
        .limit(1)\
        .all()

    if len(items) == 0 :
        return None
    else:
        o = map_to_object(items[0])
        return o

def find_all():
    objects = []
    items = CyclicLog.query.all()
    
    for item in items:
        o = map_to_object(item)
        objects.append(o)
    
    return objects

def find_by_event_date(f, t):
    objects = []
    items = CyclicLog.query.filter(and_(CyclicLog.event_date >= f, CyclicLog.event_date <= t )).all()

    for item in items:
        o = map_to_object(item)
        objects.append(o)
    
    return objects
