import json
import samsungctl

CONFIG_PATH = './app/config.json'

with open(CONFIG_PATH) as data:
    config_data = json.load(data)


class Tv:
    def __init__(self):
        self.remote = samsungctl.Remote(config_data)
 
    async def up_volume(self):
        try:
            self.remote.control('KEY_VOLUP')
        except:
            return {'error volume up'}

    async def down_volume(self):
        try:
            self.remote.control('KEY_VOLDOWN')
        except:
            return {'error volume down'}

    async def channel_up(self):
        try:
            self.remote.control('KEY_CHUP')
        except:
            return {'error channel up'}

    async def channel_down(self):
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




