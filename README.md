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

## Configuration properties

### `config.json`

| Property | Default | Remark |
|---|---|---|
| `cameras` | [] | _Required._ List of cameras. |
| `cameras[0].name` |  | _Required, Unique._ Name of the camera. |
| `cameras[0].host` |  | _Required._ Hostname or IP. |
| `cameras[0].port` | 80 | Port number. |

### `secrets.json`

| Property | Default | Remark |
|---|---|---|
| `defaults` | [] | _Optional._ Default credentials. |
| `defaults.username` |  | Username that applies to all cameras (unless overridden by camera username below). |
| `defaults.username` |  | Password that applies to all cameras (unless overridden by camera password below). |
| `cameras` | [] | _Optional._ List of credentials specific to cameras. |
| `cameras[0].name` |  | _Required, Unique._ Name of the camera. Should match the name of the camera in the main config file. |
| `cameras[0].username` |  | Username of the camera. |
| `cameras[0].password` |  | Password of the camera. |