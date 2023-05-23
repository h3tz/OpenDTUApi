from opendtuapi import *


mydtu = opendtuapi("ip","admin","password","serial")
mystatus = mydtu.getlivestatus()
mydcWatt = mydtu.getDCPower(1)
mydcWatt = mydtu.getDCVoltage(1)
myNewSetPoint = mydtu.setLimit(200)
myacPower = mydtu.getACPower()
pass
