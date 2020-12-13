from datetime import datetime
import typing as tp

from sqlalchemy import and_

from infrastructure.flaskSetup import db
from util import util
from domain import parsed_data

class ParcedLog(db.Model):

    __tablename__ = 'parsed_logs'

    id = db.Column(db.String, primary_key=True, default=util.createUUID)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    event_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    device_id = db.Column(db.String, nullable=False, default='0000')
    item0_max = db.Column(db.REAL, nullable=False, default=-32000)
    item0_min = db.Column(db.REAL, nullable=False, default=-32000)
    item1_max = db.Column(db.REAL, nullable=False, default=-32000)
    item1_min = db.Column(db.REAL, nullable=False, default=-32000)
    item2_max = db.Column(db.REAL, nullable=False, default=-32000)
    item2_min = db.Column(db.REAL, nullable=False, default=-32000)
    item3_max = db.Column(db.REAL, nullable=False, default=-32000)
    item3_min = db.Column(db.REAL, nullable=False, default=-32000)
    item4_max = db.Column(db.REAL, nullable=False, default=-32000)
    item4_min = db.Column(db.REAL, nullable=False, default=-32000)
    item5_max = db.Column(db.REAL, nullable=False, default=-32000)
    item5_min = db.Column(db.REAL, nullable=False, default=-32000)
    item6_max = db.Column(db.REAL, nullable=False, default=-32000)
    item6_min = db.Column(db.REAL, nullable=False, default=-32000)
    item7_max = db.Column(db.REAL, nullable=False, default=-32000)
    item7_min = db.Column(db.REAL, nullable=False, default=-32000)
    item8_max = db.Column(db.REAL, nullable=False, default=-32000)
    item8_min = db.Column(db.REAL, nullable=False, default=-32000)
    item9_max = db.Column(db.REAL, nullable=False, default=-32000)
    item9_min = db.Column(db.REAL, nullable=False, default=-32000)

def map_to_entity(o: tp.Type[parsed_data.Log_data]):
    log = ParcedLog()
    log.event_date = o.dt
    log.device_id = o.device_id
    log.item0_max = o.item0_max
    log.item0_min = o.item0_min
    log.item1_max = o.item1_max
    log.item1_min = o.item1_min
    log.item2_max = o.item2_max
    log.item2_min = o.item2_min
    log.item3_max = o.item3_max
    log.item3_min = o.item3_min
    log.item4_max = o.item4_max
    log.item4_min = o.item4_min
    log.item5_max = o.item5_max
    log.item5_min = o.item5_min
    log.item6_max = o.item6_max
    log.item6_min = o.item6_min
    log.item7_max = o.item7_max
    log.item7_min = o.item7_min
    log.item8_max = o.item8_max
    log.item8_min = o.item8_min
    log.item9_max = o.item9_max
    log.item9_min = o.item9_min
    return log

def map_to_object(e: tp.Type[ParcedLog]):
    data = parsed_data.Log_data()
    data.dt = e.event_date
    data.device_id = e.device_id
    data.item0_max = e.item0_max
    data.item0_min = e.item0_min
    data.item1_max = e.item1_max
    data.item1_min = e.item1_min
    data.item2_max = e.item2_max
    data.item2_min = e.item2_min
    data.item3_max = e.item3_max
    data.item3_min = e.item3_min
    data.item4_max = e.item4_max
    data.item4_min = e.item4_min
    data.item5_max = e.item5_max
    data.item5_min = e.item5_min
    data.item6_max = e.item6_max
    data.item6_min = e.item6_min
    data.item7_max = e.item7_max
    data.item7_min = e.item7_min
    data.item8_max = e.item8_max
    data.item8_min = e.item8_min
    data.item9_max = e.item9_max
    data.item9_min = e.item9_min
    
    return data

def add(p: tp.Type[parsed_data.Log_data]):
    log = map_to_entity(p)

    db.session.add(log)
    db.session.commit()

def find_all():
    objects = []
    items = ParcedLog.query.all()
    
    for item in items:
        o = map_to_object(item)
        objects.append(o)
    
    return objects

def find_by_event_date(f, t, device_id):
    objects = []
    items = ParcedLog.query.filter(and_(ParcedLog.event_date >= f, ParcedLog.event_date <= t, ParcedLog.device_id == device_id )).all()

    for item in items:
        o = map_to_object(item)
        objects.append(o)
    
    return objects

def delete_by_event_date(f, t, device_id):
    ParcedLog.query.filter(and_(ParcedLog.event_date >= f, ParcedLog.event_date <= t, ParcedLog.device_id == device_id )).delete()
