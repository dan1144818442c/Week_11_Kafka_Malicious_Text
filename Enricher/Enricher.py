import json
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime

nltk.download('/usr/local/share/nltk_data')

class Enricher:

    def __init__(self,messages:json):
        self.messages = messages

    def weapons_detected(self,weapon_path:str,data:str):
        weapon_list = self._weapon_list(weapon_path)
        weapons = []
        for word in data.split():
            if word in weapon_list:
                weapons.append(word)
        return weapons

    def detect_weapons_in_messages(self,weapon_path:str):
        for message in self.messages:
            weapons = self.weapons_detected(weapon_path,message.value["clean_text"])
            self.messages[message].value["weapons_detected"] = weapons
        return self.messages

    def _weapon_list(self,weapon_path:str):
        try:
            with open(weapon_path, "r",encoding='utf-8') as weapons:
                return weapons.read().split()
        except:
            return ["file weapons not find..."]

    def relevant_timestamp(self,text:str):
        date_time_pattern = r"\d{2}/\d{2}/\d{4}"
        times = re.findall(date_time_pattern,text)
        last_time = []
        format_string = "%d/%m/%Y"
        for time in times:
            time = datetime.strptime(time,format_string)
            last_time.append(time)
        return last_time

    def add_relevant_timestamps(self):
        for message in self.messages:
            last_time = self.relevant_timestamp(message.value["original_text"])
            self.messages[message].value["relevant_timestamp"] = max(last_time)
        return self.messages

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

    def add_sentiment_to_messages(self):
        for message in self.messages:
            emotion = self.find_emotion_of_text(message.value["original_text"])
            self.messages[message].value["sentiment"] = emotion
        return self.messages