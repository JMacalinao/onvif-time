import datetime
import json
import os
import time
from onvif import ONVIFCamera
from zeep.transports import Transport

def set_time(tz: str, host: str, port: int, username: str, password: str):
    camera = ONVIFCamera(host, port, username, password, transport=Transport(operation_timeout=5))
    now = datetime.datetime.utcnow()

    params = camera.devicemgmt.create_type('SetSystemDateAndTime')
    params.DateTimeType = 'Manual'
    params.DaylightSavings = True
    params.TimeZone = {
        'TZ': tz
    }
    params.UTCDateTime = {
        'Date': {
            'Year': now.year,
            'Month': now.month,
            'Day': now.day
        },
        'Time': {
           'Hour': now.hour,
           'Minute': now.minute,
           'Second': now.second
        }
    }
    print(params)
    camera.devicemgmt.SetSystemDateAndTime(params)

# Prep vars
config = json.load(open(os.getenv('CONFIG_FILE') if 'CONFIG_FILE' in os.environ else 'config.json'))
secrets = json.load(open(os.getenv('SECRETS_FILE') if 'SECRETS_FILE' in os.environ else 'secrets.json'))
tz = os.getenv('POSIX_TZ') if 'POSIX_TZ' in os.environ else 'GMT'
interval = float(os.getenv('INTERVAL')) if 'INTERVAL' in os.environ else 60

# Main loop
while True:
    try:
        for camera in config['cameras']:
            host = camera['host']
            port = int(camera['port']) if 'port' in camera else None
            username = secrets['defaults']['username']
            password = secrets['defaults']['password']
            camera_secret = next(filter(lambda x: x['name'] == camera['name'], secrets['cameras'])) if 'cameras' in secrets else None
            if camera_secret:
                username = camera_secret['username']
                password = camera_secret['password']
            set_time(tz, host, port, username, password)
    except Exception as error:
        print('You dun goofed: ', error)
    time.sleep(interval)