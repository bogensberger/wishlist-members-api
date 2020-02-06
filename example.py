from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

# read values from a section
API_KEY = config.get('Settings', 'API_KEY')