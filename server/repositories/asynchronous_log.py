from datetime import datetime
import typing as tp

from sqlalchemy import and_

from infrastructure.flaskSetup import db
from util import util
from domain import asynchronous

class AsynchronousLog(db.Model):

    __tablename__ = 'asynchronous_logs'

    id = db.Column(db.String, primary_key=True, default=util.createUUID)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    event_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    event_code = db.Column(db.String, nullable=False, default='0000')
    event_category = db.Column(db.String, nullable=False, default='0000')
    event_name = db.Column(db.String, nullable=False, default='0000')

def map_to_entity(a: tp.Type[asynchronous.Log_data]):
    log = AsynchronousLog()
    log.event_date = a.dt
    log.event_code = a.code
    log.event_category = a.category
    log.event_name = a.name
    return log

def map_to_object(a: tp.Type[AsynchronousLog]):
    data = asynchronous.Log_data()
    data.dt = a.event_date
    data.code = a.event_code
    data.category = a.event_category
    data.name = a.event_name

def add(a: tp.Type[asynchronous.Log_data]):
    log = map_to_entity(a)
    
    db.session.add(log)
    db.session.commit()
    db.session.close()

def find_all():
    objects = []
    items = AsynchronousLog.query.all()
    
    for item in items:
        o = map_to_object(item)
        objects.append(o)
    
    return objects

def find_by_event_date(f, t):
    objects = []
    items = AsynchronousLog.query.filter(and_(AsynchronousLog.event_date >= f, AsynchronousLog.event_date <= t )).all()

    for item in items:
        o = map_to_object(item)
        objects.append(o)
    
    return objects
