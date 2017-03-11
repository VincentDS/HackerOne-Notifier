# API key of your pushbullet account
PUSHBULLET_API_KEY = ''

# Refresh rate of the program in seconds
REFRESH_RATE = 300

# Hackerone filter type (select a key of the filters dict)
HACKERONE_FILTER = 'type'

# Different filter settings
filters = dict (
  type = 'hackerone',
  domain = 'example.com',
  bounties = 'yes',
  ibb = 'yes'
)