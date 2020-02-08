from wlmapi import WlmApi

from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

# read values from a section
API_KEY = config.get('Settings', 'API_KEY')
HOST = config.get('Settings', 'HOST')

api = WlmApi(HOST, API_KEY)
# print(api.get("levels"))
# print(api.get("levels/1561627012"))
#  1581181426
# print(api.post("levels", {"name": "testtttt"}))
print(api.get("levels/1581181426"))
print(api.put("levels/1581181426", {"name": "foo"}))
print(api.get("levels/1581181426"))
print(api.delete("levels/1581181426"))
print(api.get("levels/1581181426"))