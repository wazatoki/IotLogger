from infrastructure.flaskSetup import db

class Device(db.Model):

    __tablename__ = 'device'

    id = db.Column(db.String, primary_key=True)

def add(device_id):
    d = Device()
    d.id = device_id

    db.session.add(d)
    db.session.commit()

def find_all_IDs():
    objects = []
    items = Device.query.all()
    
    for item in items:
        objects.append(item.id)
    
    return objects