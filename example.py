from opendtuapi import *

mydtu = opendtuapi("ip","admin","password","serial")
mynetworkstatus = mydtu.getNetzworkStatus()
mystatus = mydtu.getlivestatus()
mydcPower = mydtu.getDCPower(1)
mydcVoltage = mydtu.getDCVoltage(1)
myNewSetPoint = mydtu.setLimit(200)
myacPower = mydtu.getACPower()
pass
