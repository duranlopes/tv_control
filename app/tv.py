import json
import samsungctl
import os

try:
    CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))+'/config.json'
    with open(CONFIG_PATH) as data:
        config_data = json.load(data)
except:
    config_data = {
        "name": "python-app",
        "description": "python",
        "id": os.environ['TV_MAC_ADDRESS'],
        "host": os.environ['TV_IP'],
        "port": 55000,
        "method": "legacy",
        "timeout": 0
    }

class Tv:
    def __init__(self):
        try:
            self.remote = samsungctl.Remote(config_data)
        except:
            print("Please verify you tv ip address")

    def up_volume(self):
        try:
            self.remote.control('KEY_VOLUP')
        except:
            return {'error volume up'}

    def down_volume(self):
        try:
            self.remote.control('KEY_VOLDOWN')
        except:
            return {'error volume down'}

    def channel_up(self):
        try:
            self.remote.control('KEY_CHUP')
        except:
            return {'error channel up'}

    def channel_down(self):
        try:
            self.remote.control('KEY_CHDOWN')
        except:
            return {'error channel down'}

    def poweroff(self):
        try:
            self.remote.control('KEY_POWEROFF')
        except:
            return {'error off'}

    def mute(self):
        try:
            self.remote.control('KEY_MUTE')
        except:
            return {'error mute'}


if __name__ == "__main__":
    tv = Tv()
    tv.up_volume()
