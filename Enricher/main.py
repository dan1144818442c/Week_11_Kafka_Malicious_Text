import json
import re
import datetime

class Blacklist:

    def __init__(self,messages:json):
        self.messages = messages

    def weapons_detected(self,weapon_path:str):
        weapon_list = self._weapon_list(weapon_path)
        for message in self.messages:
            weapons = []
            for word in message.clean_text.splet():
                if word in weapon_list:
                    weapons.append(word)
            self.messages[message]["weapons_detected"] = weapons
        return self.messages

    def _weapon_list(self,weapon_path):
        with open(weapon_path, "r") as weapons:
            return weapons.read().splitlines()

    def relevant_timestamp(self):
        pass