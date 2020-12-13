from datetime import datetime
import typing as tp

from sqlalchemy import and_, desc

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
    device_id = db.Column(db.String, nullable=False, default='0000')
    item0 = db.Column(db.REAL, nullable=False, default=-32000)
    item1 = db.Column(db.REAL, nullable=False, default=-32000)
    item2 = db.Column(db.REAL, nullable=False, default=-32000)
    item3 = db.Column(db.REAL, nullable=False, default=-32000)
    item4 = db.Column(db.REAL, nullable=False, default=-32000)
    item5 = db.Column(db.REAL, nullable=False, default=-32000)
    item6 = db.Column(db.REAL, nullable=False, default=-32000)
    item7 = db.Column(db.REAL, nullable=False, default=-32000)
    item8 = db.Column(db.REAL, nullable=False, default=-32000)
    item9 = db.Column(db.REAL, nullable=False, default=-32000)
    


def map_to_entity(o: tp.Type[cyclic_data.Log_data]):
    e = CyclicLog()
    e.event_date = o.dt
    e.device_id = o.device_id
    e.item0 = o.item0
    e.item1 = o.item1
    e.item2 = o.item2
    e.item3 = o.item3
    e.item4 = o.item4
    e.item5 = o.item5
    e.item6 = o.item6
    e.item7 = o.item7
    e.item8 = o.item8
    e.item9 = o.item9
    
    return e

def map_to_object(e: tp.Type[CyclicLog]):
    o = cyclic_data.Log_data()
    o.dt = e.event_date
    o.device_id = e.device_id
    o.item0 = e.item0
    o.item1 = e.item1
    o.item2 = e.item2
    o.item3 = e.item3
    o.item4 = e.item4
    o.item5 = e.item5
    o.item6 = e.item6
    o.item7 = e.item7
    o.item8 = e.item8
    o.item9 = e.item9
    return o

def add(o: tp.Type[cyclic_data.Log_data]):
    e = map_to_entity(o)
    db.session.add(e)
    db.session.commit()

def find_current_state(f, t, device_id):
    items = CyclicLog.query.filter(and_(CyclicLog.event_date >= f, CyclicLog.event_date <= t, CyclicLog.device_id == device_id ))\
        .order_by(desc(CyclicLog.event_date))\
        .limit(1)\
        .all()

    if len(items) == 0 :
        return None
    else:
        o = map_to_object(items[0])
        return o

def mark_parsed_logs(f, t, device_id):
    items = CyclicLog.query.filter(and_(CyclicLog.event_date >= f, CyclicLog.event_date <= t, CyclicLog.is_parsed == False, CyclicLog.device_id == device_id )).all()
    
    for item in items:
        item.is_parsed = True
        db.session.commit()

def find_first_not_Parsed(device_id):
    items = CyclicLog.query.filter(and_(CyclicLog.is_parsed == False, CyclicLog.device_id == device_id))\
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

def find_by_event_date(f, t, device_id):
    objects = []
    items = CyclicLog.query.filter(and_(CyclicLog.event_date >= f, CyclicLog.event_date <= t, CyclicLog.device_id == device_id )).all()

    for item in items:
        o = map_to_object(item)
        objects.append(o)
    
    return objects

def delete_by_event_date(f, t, device_id):
    CyclicLog.query.filter(and_(CyclicLog.event_date >= f, CyclicLog.event_date <= t, CyclicLog.device_id == device_id )).delete()