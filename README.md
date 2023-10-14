# onvif-time

Synchronize time for your stubborn ONVIF cameras.

_Story time!_ I have a couple of cameras that are almost perfect for my needs. However, there's a catch: Since I use my own NVR software, some of the features of those cameras depend on some settings that are set by their first-party NVR hardware, and that includes the date and time. Setting them per camera is fine, but once they reboot or there's a power outage, the date/time resets. Which is weird, because other settings are being persisted, like the video resolution.

So I made this simple script that makes sure the date/time is set correctly on those cameras. Time used to synchronize is based on current system time, so make sure your time is accurate to begin with!

## Prerequisites

You need to configure the script with `config.json` and `secrets.json` files. I have included sample files to get you started.

## Usage

### Through the command line

`python3 main.py` -- simple as that.

### Docker Compose

TODO

## Environment variables

| Variable | Default | Remark |
|---|---|---|
| `CONFIG_FILE` | config.json | Path to the main config file. Use the sample JSON file for reference. |
| `SECRETS_FILE` | secrets.json | Path to the secrets config file. Use the sample JSON file for reference. |
| `INTERVAL` | 60 | The number of seconds to wait in between resetting the date/time. |
| `POSIX_TZ` | GMT | The timezone in POSIX 1003.1 format. |