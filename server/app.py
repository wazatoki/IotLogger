from apscheduler.schedulers.background import BackgroundScheduler

from infrastructure import flaskSetup
import repositories
import gateway
from services import parseCyclicData
from config import config

app = flaskSetup.app
scheduler = BackgroundScheduler()

def job(app):
    with app.app_context():
        parseCyclicData.add_parsd_data()

scheduler.add_job(job, 'interval', args=[app], seconds=10)


if __name__ == '__main__':
    scheduler.start()
    app.run(host='0.0.0.0', port=config.http_port)
    
    