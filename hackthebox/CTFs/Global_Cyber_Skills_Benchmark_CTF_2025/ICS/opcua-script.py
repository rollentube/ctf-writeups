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
