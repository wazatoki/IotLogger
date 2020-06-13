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
    speed_max = db.Column(db.Integer, nullable=False, default=-32000)
    speed_min = db.Column(db.Integer, nullable=False, default=-32000)
    flow_max = db.Column(db.REAL, nullable=False, default=-32000)
    flow_min = db.Column(db.REAL, nullable=False, default=-32000)
    pven_max = db.Column(db.Integer, nullable=False, default=-32000)
    pven_min = db.Column(db.Integer, nullable=False, default=-32000)
    pint_max = db.Column(db.Integer, nullable=False, default=-32000)
    pint_min = db.Column(db.Integer, nullable=False, default=-32000)
    deltap_max = db.Column(db.Integer, nullable=False, default=-32000)
    deltap_min = db.Column(db.Integer, nullable=False, default=-32000)
    part_max = db.Column(db.Integer, nullable=False, default=-32000)
    part_min = db.Column(db.Integer, nullable=False, default=-32000)
    tven_max = db.Column(db.REAL, nullable=False, default=-32000)
    tven_min = db.Column(db.REAL, nullable=False, default=-32000)
    tart_max = db.Column(db.REAL, nullable=False, default=-32000)
    tart_min = db.Column(db.REAL, nullable=False, default=-32000)
    svo2_max = db.Column(db.REAL, nullable=False, default=-32000)
    svo2_min = db.Column(db.REAL, nullable=False, default=-32000)
    hct_max = db.Column(db.REAL, nullable=False, default=-32000)
    hct_min = db.Column(db.REAL, nullable=False, default=-32000)

def map_to_entity(p: tp.Type[parsed_data.Log_data]):
    log = ParcedLog()
    log.event_date = p.dt
    log.speed_max = p.speed_max
    log.speed_min = p.speed_min
    log.flow_max = p.flow_max
    log.flow_min = p.flow_min
    log.pven_max = p.pven_max
    log.pven_min = p.pven_min
    log.pint_max = p.pint_max
    log.pint_min = p.pint_min
    log.deltap_max = p.deltap_max
    log.deltap_min = p.deltap_min
    log.part_max = p.part_max
    log.part_min = p.part_min
    log.tven_max = p.tven_max
    log.tven_min = p.tven_min
    log.tart_max = p.tart_max
    log.tart_min = p.tart_min
    log.svo2_max = p.svo2_max
    log.svo2_min = p.svo2_min
    log.hct_max = p.hct_max
    log.hct_min = p.hct_min
    return log

def map_to_object(p: tp.Type[ParcedLog]):
    data = parsed_data.Log_data()
    data.dt = p.event_date
    data.speed_max = p.speed_max
    data.speed_min = p.speed_min
    data.flow_max = p.flow_max
    data.flow_min = p.flow_min
    data.pven_max = p.pven_max
    data.pven_min = p.pven_min
    data.pint_max = p.pint_max
    data.pint_min = p.pint_min
    data.deltap_max = p.deltap_max
    data.deltap_min = p.deltap_min
    data.part_max = p.part_max
    data.part_min = p.part_min
    data.tven_max = p.tven_max
    data.tven_min = p.tven_min
    data.tart_max = p.tart_max
    data.tart_min = p.tart_min
    data.svo2_max = p.svo2_max
    data.svo2_min = p.svo2_min
    data.hct_max = p.hct_max
    data.hct_min = p.hct_min
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

def find_by_event_date(f, t):
    objects = []
    items = ParcedLog.query.filter(and_(ParcedLog.event_date >= f, ParcedLog.event_date <= t )).all()

    for item in items:
        o = map_to_object(item)
        objects.append(o)
    
    return objects
