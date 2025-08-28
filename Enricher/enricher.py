import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime
nltk.download('/usr/local/share/nltk_data')
nltk.download('vader_lexicon')


class Enricher_C:

    def __init__(self,dic_:dict):
        self.dict_ = dic_

    def weapons_detected(self,weapon_path:str,data:str):
        weapon_list = self._weapon_list(weapon_path)
        clean_weapon_list = []
        for weapon in weapon_list:
            clean_weapon_list.append(weapon.lower())
        weapons = []
        for word in data.split():
            if word in clean_weapon_list:
                weapons.append(word)

        return weapons

    def detect_weapons_in_messages(self,weapon_path:str):
        weapons = self.weapons_detected(weapon_path,self.dict_["clean_text"])
        if len(weapons) > 0:
            self.dict_["weapons_detected"] = weapons
        else:
            self.dict_["weapons_detected"] = ""
        return self.dict_

    def _weapon_list(self,weapon_path:str):
        try:
            with open(weapon_path, "r") as weapons:
                return weapons.read().splitlines()
        except:
            print("didn't find this file")
            return []

    def relevant_timestamp(self,text:str):
        date_time_pattern = r"\d{4}-\d{2}-\d{2}"
        times = re.findall(date_time_pattern,text)
        last_time = []
        format_string = "%Y-%m-%d"
        for time in times:
            time = datetime.strptime(time,format_string)
            last_time.append(time)
        return last_time

    def add_relevant_timestamps(self):
        last_time = self.relevant_timestamp(self.dict_["text"])
        if len(last_time) > 0:
            max_time = max(last_time)
            self.dict_["relevant_timestamp"] = str(max_time)
        else:
            self.dict_["relevant_timestamp"] = ""
        return self.dict_

    def find_emotion_of_text(self,text:str):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        emotion = score['compound']
        if 1 > emotion > 0.5:
            return "positive"
        elif 0.5 > emotion > -0.5:
            return  "neutral"
        elif -0.5 > emotion > -1:
            return  "negative"
        else:
            return  "?"

    def add_sentiment_to_dict(self):
        emotion = self.find_emotion_of_text(self.dict_["text"])
        self.dict_["sentiment"] = emotion
        return self.dict_

    def activate_all_func(self, path_weapon_list):
        self.add_sentiment_to_dict()
        self.detect_weapons_in_messages(path_weapon_list)
        self.add_relevant_timestamps()

        return self.dict_