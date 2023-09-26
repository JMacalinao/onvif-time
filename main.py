import datetime
import os
import time
from onvif import ONVIFCamera

def set_time(tz: str, host: str, port: int, username: str, password: str):
    camera = ONVIFCamera(host, port, username, password)
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
username = os.getenv('USER')
password = os.getenv('PASS')
camera_hosts = os.getenv('HOSTS').split(',') if 'HOSTS' in os.environ else None
tz = os.getenv('POSIX_TZ') if 'POSIX_TZ' in os.environ else 'GMT'
interval = float(os.getenv('INTERVAL')) if 'INTERVAL' in os.environ else 60

# Main loop
while True:
    try:
        for str_host in camera_hosts:
            host = str_host
            port = 80
            if ':' in str_host:
                host = str_host.split(':')[0]
                port = int(str_host.split(':')[1])
            set_time(tz, host, port, username, password)
    except Exception as error:
        print('You dun goofed: ', error)
    time.sleep(interval)