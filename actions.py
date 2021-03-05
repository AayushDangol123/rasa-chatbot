# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv

class actionfindengr(Action):
    def name(self) -> Text:
        return "action_findengr"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:
        # get the location slot
        location = tracker.get_slot('location')
        # read the CSV file
        with open('data/Engineering colllege.csv','r',encoding = "utf-8") as file:
            reader = csv.DictReader(file)
            # get a list of universities in the desired location
            output = [row for row in reader if row['location'] == location]
        if output: 
            reply  = f"This is a list of universities in {location}:"
            reply += "\n- " + "\n- ".join([item['College'] for item in output])
            # utter the message
            dispatcher.utter_message(reply)
        else: # the list is empty
            dispatcher.utter_message(f"I could not find universities in {location}")
