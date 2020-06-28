from datetime import datetime
import typing as tp

from infrastructure.flaskSetup import db
from domain import device_item
from util import util

class Device_Item(db.Model):

    __tablename__ = 'device_items'

    id = db.Column(db.String, primary_key=True, default=util.createUUID)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    column_id = db.Column(db.String, nullable=False)
    device_id = db.Column(db.String, nullable=False)
    device_item_id = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    unit = db.Column(db.String, nullable=False)

def map_to_entity(o: tp.Type[device_item.Device_item]):
    e = Device_Item()
    e.column_id = o.column_id
    e.device_id = o.device_id
    e.device_item_id = o.device_item_id
    e.name = o.name
    e.unit = o.unit
    return e

def map_to_object(e: tp.Type[Device_Item]):
    o = device_item.Device_item()
    o.column_id = e.column_id
    o.device_id = e.device_id
    o.device_item_id = e.device_item_id
    o.name = e.name
    o.unit = e.unit
    return o

def add(o: tp.Type[device_item.Device_item]):
    d = map_to_entity(o)
    db.session.add(d)
    db.session.commit()

def delete_by_deviceID(deviceID):
    items = Device_Item.query.filter(Device_Item.device_id == deviceID).all()
    for item in items:
        db.session.delete(item)
    db.session.commit()

def find_by_deviceID(deviceID):
    objects = []
    items = Device_Item.query.filter(Device_Item.device_id == deviceID).all()
    
    for item in items:
        objects.append(map_to_object(item))
    return objects