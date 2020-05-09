
import os
import sys
import json
import samsungctl

DIR_NAME = os.path.dirname(os.path.realpath(sys.argv[0]))
CONFIG_PATH = os.path.join(DIR_NAME, 'config.json')

with open(CONFIG_PATH) as data:
    config_data = json.load(data)


class Tv:
    def __init__(self):
        self.remote = samsungctl.Remote(config_data)
 
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
            return {'error'}

    def channel_down(self):
        try:
            self.remote.control('KEY_CHDOWN')
        except:
            return {'error'}

    def poweroff(self):
        try:
            self.remote.control('KEY_POWEROFF')
        except:
            return {'error_off'}

    def mute(self):
        try:
            self.remote.control('KEY_MUTE')
        except:
            return {'error_mute'}




