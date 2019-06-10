#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from hermes_python.hermes import Hermes
import hermes_python.ontology.dialogue as dialogue
import io
from fußball import get_football_result

USERNAME_INTENTS = "olzeug"

def user_intent(intentname):
    return USERNAME_INTENTS + ":" + intentname

def read_configuration_file(configuration_file):
    try:
        cp = configparser.ConfigParser()
        with io.open(configuration_file, encoding="utf-8") as f:
            cp.read_file(f)
        return {section: {option_name: option for option_name, option in cp.items(section)}
                for section in cp.sections()}
    except (IOError, configparser.Error):
        return dict()

def intent_callback(hermes, intent_message):
    intentMessage = intent_message
    conf = read_configuration_file("config.ini")
    intentname = intent_message.intent.intent_name
    if intentname == user_intent("lastGame"):
        try:
            hermes.publish_end_session(intentMessage.session_id, str(get_football_result(str(intentMessage.slots.footballTeam.first().value),0,str(conf['secret']['api_key']))))
        except:
            hermes.publish_end_session(intentMessage.session_id,"Es konnten keine Daten abgerufen werden")

    elif intentname == user_intent("nextGame"):
        try:
            hermes.publish_end_session(intentMessage.session_id, str(get_football_result(str(intentMessage.slots.footballTeam.first().value),1,str(conf['secret']['api_key']))))
        except:
            hermes.publish_end_session(intentMessage.session_id,"Es konnten keine Daten abgerufen werden")
    elif intentname == user_intent("getTrainer"):
        try:
            hermes.publish_end_session(intentMessage.session_id, str(get_football_result(str(intentMessage.slots.footballTeam.first().value),2,str(conf['secret']['api_key']))))
        except:
            hermes.publish_end_session(intentMessage.session_id,"Es konnten keine Daten abgerufen werden")

if __name__ == "__main__":
    #config = read_configuration_file("config.ini")
    with Hermes("localhost:1883") as h:
        h.subscribe_intents(intent_callback)
        h.start()

