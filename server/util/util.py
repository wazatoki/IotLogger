from uuid import uuid4
from datetime import datetime

def createUUID():
    return str(uuid4())+datetime.now().strftime('%Y%m%d%H%M%S%f')
    