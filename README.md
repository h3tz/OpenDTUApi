# OpenDTUApi



## Description

This project is offering a wrapper to access the OpenDTUApi as definied from the OpenDTU project [Web-API.md
](https://github.com/tbnobody/OpenDTU/blob/master/docs/Web-API.md)

## Getting Started

### Bugs and feature requests

Have a bug or a feature request? Please open an issue.

### Covered API
| GET/POST | Auth required | URL |Implemented
| -------- | --- | -- |--|
| Get      | yes | /api/config/get | -
| Post     | yes | /api/config/delete |-
| Get      | yes | /api/config/list |-
| Post     | yes | /api/config/upload |-
| Get+Post | yes | /api/device/config |-
| Get      | no  | /api/devinfo/status |-
| Get+Post | yes | /api/dtu/config |-
| Get      | no  | /api/eventlog/status?inv=inverter-serialnumber |-
| Post     | yes | /api/firmware/update |-
| Get      | yes | /api/inverter/list |-
| Post     | yes | /api/inverter/add |-
| Post     | yes | /api/inverter/del |-
| Post     | yes | /api/inverter/edit |-
| Post     | yes | /api/limit/config |Yes
| Get      | no  | /api/limit/status |-
| Get      | no  | /api/livedata/status |Yes
| Post     | yes | /api/maintenance/reboot |-
| Get+Post | yes | /api/mqtt/config |-
| Get      | no  | /api/mqtt/status |-
| Get+Post | yes | /api/network/config |-
| Get      | no  | /api/network/status |-
| Get+Post | yes | /api/ntp/config |-
| Get      | no  | /api/ntp/status |-
| Get+Post | yes | /api/ntp/time |-
| Get      | no  | /api/power/status |-
| Post     | yes | /api/power/config |-
| Get      | no  | /api/prometheus/metrics |-
| Get+Post | yes | /api/security/config |-
| Get      | yes | /api/security/authenticate |-
| Get      | no  | /api/system/status |-

### Examples 
``` js
from opendtuapi import *
mydtu = opendtuapi("ip","admin","password","serial")
```
#/api/livedata/status
``` js
mystatus = mydtu.getlivestatus()

# hoymiles solarmodul connected at string 1
mydcWatt = mydtu.getDCPower(1) 
mydcWatt = mydtu.getDCVoltage(1)
myacPower = mydtu.getACPower()
```
#/api/limit/config
``` js
# set the hoymiles absolut limit in watt
passed = mydtu.setLimit(200)
```


## Authors
Andreas Hetz|Discord: ch3fh3tz#0964

## Version History
* 0.1
    * Initial Release 

## License

See the LICENSE.md file for details

## Other

* [OpenDTU](https://github.com/tbnobody/OpenDTU)
