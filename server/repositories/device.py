from infrastructure.flaskSetup import db

class Device(db.Model):

    __tablename__ = 'devices'

    id = db.Column(db.String, primary_key=True)
    message = db.Column(db.String, default="")

def delete_all():
    items = Device.query.all()
    for item in items:
        db.session.delete(item)
        db.session.commit()

def add(device_id):
    d = Device()
    d.id = device_id
    db.session.add(d)
    db.session.commit()
        

def update_message(deviceID, message):
    d = Device.query.filter(Device.id == deviceID).first()
    d.message = message
    db.session.commit()

def find_message_by_deviceID(deviceID):
    d = Device.query.filter(Device.id == deviceID).first()
    return d.message

def find_all_IDs():
    objects = []
    items = Device.query.all()
    
    for item in items:
        objects.append(item.id)
    
    return objects