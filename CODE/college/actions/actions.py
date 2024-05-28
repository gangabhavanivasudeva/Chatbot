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
from typing import Any, Text, Dict, List
import webbrowser
import requests
# import wikipedia
# import nltk
# from nltk.corpus import stopwords
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import requests
from rasa_sdk.events import AllSlotsReset


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        
        txt = tracker.latest_message['text']
        webbrowser.open_new("http://google.com/search?q="+ txt)
        dispatcher.utter_message(text="I am sending you to Google...")
        return [AllSlotsReset(), UserUtteranceReverted()]

class rem(Action):
    def name(self) -> Text:
        return "action_rem"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user = tracker.get_slot('user')
        event = tracker.get_slot("event")
        dates = tracker.get_slot('dates')
        say = requests.get("http://localhost:8000/setReminder?user="+user+"&date="+dates+"&event="+event)
        say = say.json()
        dispatcher.utter_message(text=say)
        return [AllSlotsReset()]


class admission(Action):
    def name(self) -> Text:
        return "action_admission"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'http://localhost:8000/admission'
        say = requests.get(url)
        say = say.json()
        print(say)
        if len(say) == 0:
            dispatcher.utter_message(text="Sorry We don't have the information you are looking for")
            return [AllSlotsReset()]
        else:
            txt = ""
            # txt = txt + "<li>Branch -- Price </li>"
            for x in say:
                txt = txt + "<ul>"
                txt = txt + "<li>Branch:&nbsp" + str(x['branch']) + "</li>" + \
                      "<li>Description:&nbsp" + x['desc'] + "</li>" + \
                      "<li>Specializations:&nbsp" + str(x['special']) + "</li>" + \
                      "<li>Professors:&nbsp" + str(x['professors']) + "</li>" + \
                      "<li>Fees:&nbsp" + str(x['fees']) + "</li>" + \
                      "<li>Duration:&nbsp" + str(x['duration']) + "</li>" + \
                      "<li>Seats:&nbsp" + str(x['seats']) + "</li>"
                txt = txt + "</ul>"
            dispatcher.utter_message(text=txt)
        return [AllSlotsReset()]


class placements(Action):
    def name(self) -> Text:
        return "action_placements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'http://localhost:8000/placements'
        say = requests.get(url)
        say = say.json()
        if len(say) == 0:
            dispatcher.utter_message(text="Sorry We don't have the information you are looking for")
            return [AllSlotsReset()]
        else:
            txt = ""
            # txt = txt + "<li>Branch -- Price </li>"
            for x in say:
                txt = txt+ "<ul>"
                txt = txt + "<li>Company:&nbsp" + x['company'] + "</li>" + \
                      "<li>Package:&nbsp" + str(x['package']) + "</li>" + \
                      "<li>Full Time:&nbsp" + str(x['full_time']) + "</li>"
                txt = txt + "</ul>"
            dispatcher.utter_message(text=txt)
        return [AllSlotsReset()]


class infra(Action):
    def name(self) -> Text:
        return "action_infra"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'http://localhost:8000/infra'
        say = requests.get(url)
        say = say.json()
        if len(say) == 0:
            dispatcher.utter_message(text="Sorry We don't have the information you are looking for")
            return [AllSlotsReset()]
        else:
            dispatcher.utter_message(text=say)
        return [AllSlotsReset()]


class hostelfees(Action):
    def name(self) -> Text:
        return "action_hostelfees"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'http://localhost:8000/hostel'
        say = requests.get(url)
        say = say.json()
        if say == 0:
            dispatcher.utter_message(text="Sorry We don't have the information you are looking for")
            return [AllSlotsReset()]
        else:
            dispatcher.utter_message(text="RS "+str(say))
        return [AllSlotsReset()]


class environment(Action):
    def name(self) -> Text:
        return "action_environment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'http://localhost:8000/env'
        say = requests.get(url)
        say = say.json()
        if len(say) == 0:
            dispatcher.utter_message(text="Sorry We don't have the information you are looking for")
            return [AllSlotsReset()]
        else:
            dispatcher.utter_message(text=say)
        return [AllSlotsReset()]


class achievements(Action):
    def name(self) -> Text:
        return "action_achievements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'http://localhost:8000/achievements'
        say = requests.get(url)
        say = say.json()
        if len(say) == 0:
            dispatcher.utter_message(text="Sorry We don't have the information you are looking for")
            return [AllSlotsReset()]
        else:
            dispatcher.utter_message(text=say)
        return [AllSlotsReset()]


class naac(Action):
    def name(self) -> Text:
        return "action_naac"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'http://localhost:8000/naac'
        say = requests.get(url)
        say = say.json()
        if say == -1:
            dispatcher.utter_message(text="Sorry We don't have the information you are looking for")
            return [AllSlotsReset()]
        else:
            dispatcher.utter_message(text=str(say))
        return [AllSlotsReset()]


class nirf(Action):
    def name(self) -> Text:
        return "action_nirf"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'http://localhost:8000/nirf'
        say = requests.get(url)
        say = say.json()
        if say == -1:
            dispatcher.utter_message(text="Sorry We don't have the information you are looking for")
            return [AllSlotsReset()]
        else:
            dispatcher.utter_message(text=str(say))
        return [AllSlotsReset()]