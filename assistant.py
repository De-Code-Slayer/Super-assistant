# class for assistant
from datetime import date
from .helpers.data_types import Voice, Lang
from typing import Optional


class Assistant:

    def __init__(self, voice: Voice):
        self.voice = voice


    def speak(self, words: str, lang: Optional[Lang] = Lang.english):
        # call speak enginge to speak the passed word
        pass
        
        
    def make(self):
            """
                make a call,
                reservation,
                task,
                prediction
                etc
            """
            pass


class House:

    # characteristics of a simple/basic House
     def __init__(self, room: list, temperature: int, time_of_day: date, devices: list, ):
          pass


