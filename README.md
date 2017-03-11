# HackerOne-Notifier

HackerOne-Notifier is a simple application which sends out a notification to your favorite device whenever a new program is available on HackerOne. Notifications are send out using Pushbullet. Currently the application supports the following functions: 

- Use HackerOne's filters to filter out uninteresting programs.
- Initial notification when the app launches. 
- Change the interval rate on which the app checks for new programs.

## Usage

1. Clone the repository.
2. Create a new config file `config.py` similar to `config-example.py` with the preferred settings and yout Pushbullet API key.
3. Install the requirements: `pip install -r requirements.txt`.
4. Make the python script executable: `chmod +x hackerone-notifier.py`.
5. Use no hangup to run the program in background: `nohup /path/to/hackerone-notifier.py &`.
6. Preferably, put this in `/etc/rc.local` to launch the app at startup.
