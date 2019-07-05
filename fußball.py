#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.client
import json
from datetime import date
import re
import time
import importlib
from random import choice
from CompareList import CompareList
from snipskit.apps import SnipsAppMixin
i18n = importlib.import_module("translation."+SnipsAppMixin().assistant["language"])
teams = []
for y in i18n.ligen:
    with open('/var/lib/snips/skills/Snips-Football-Skill/ligen/'+y.lower()+'.json') as f:
        response = json.loads(f.read())
    for t in response["teams"]:
        teams += [t["name"]+"|"+str(t["id"])]
c = CompareList(teams)

def tag_diff(second_date):
    datumB = date(int(re.split('[^\d]', second_date)[0]), int(re.split('[^\d]', second_date)[1]), int(re.split('[^\d]', second_date)[2])) 
    datumA = date(int(re.split('[^\d]', time.strftime("%Y-%m-%d"))[0]), int(re.split('[^\d]', time.strftime("%Y-%m-%d"))[1]), int(re.split('[^\d]', time.strftime("%Y-%m-%d"))[2]))
    return((datumB-datumA).days)
def get_data(pfad,key):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': str(key)}
    connection.request('GET', pfad, None, headers )
    response = json.loads(connection.getresponse().read().decode())
    return(response)
def get_team_id(search):
    result = c.liste(search)
    return(str(result[0]).split("|"))
def get_football_result(search,ask,key):
    team_name,team_id = get_team_id(search)
    if(ask == 0):
        response = get_data('/v2/teams/'+team_id+'/matches?status=FINISHED',key)
        i=-1
        if response["count"] == 0:
            return(choice(i18n.NO_GAMES_EXIST).format(team=team_name))
        home_score = str(response['matches'][i]['score']['fullTime']['homeTeam'])
        away_score = str(response['matches'][i]['score']['fullTime']['awayTeam'])
        home_team = str(response['matches'][i]['homeTeam']['name'])
        away_team = str(response['matches'][i]['awayTeam']['name'])
        if(home_score-3 > away_score or home_score < away_score-3):
            status = choice(i18n.HIGH_DEFEATED)
        else:
            status = choice(i18n.DEFEATED)
        if (home_score > away_score):
            return(choice(i18n.TEAM_1_WON).format(team1=home_team,team2=away_team,liga=str(response['matches'][i]['competition']['name']),count1=home_score,count2=away_score,verb=status))
        elif (home_score < away_score):
            return(choice(i18n.TEAM_2_WON).format(team1=home_team,team2=away_team,liga=str(response['matches'][i]['competition']['name']),count1=home_score,count2=away_score,verb=status))
        elif (home_score == away_score):
            return(choice(i18n.DRAW).format(team1=home_team,team2=away_team,liga=str(response['matches'][i]['competition']['name']),count1=home_score,count2=away_score))
    elif(ask == 1):
        response = get_data('/v2/teams/'+team_id+'/matches?status=SCHEDULED&limit=1',key)
        if response["count"] == 0:
            return(choice(i18n.NO_LATER_GAMES).format(team=team_name))
        if (tag_diff(str(response['matches'][0]['utcDate'])) == 0):
            datum = str(response['matches'][0]['utcDate'])
            datum = choice(i18n.TIME).format(hour=str(int(re.split('[^\d]', datum)[3])+1),minute=str(re.split('[^\d]', datum)[4]))
        else:
            datum = str(response['matches'][0]['utcDate'])
            datum = choice(i18n.TIME_AND_DAY).format(day=str(re.split('[^\d]', datum)[2]),month=str(i18n.months[int(re.split('[^\d]', datum)[1])-1]),year=str(re.split('[^\d]', datum)[0]),hour=str(int(re.split('[^\d]', datum)[3])+1),minute=str(re.split('[^\d]', datum)[4]))
            
        if (team_id == str(response['matches'][0]['homeTeam']['id'])):
            return(choice(i18n.NEXT_GAME).format(team1=str(response['matches'][0]['homeTeam']['name']),team2=str(response['matches'][0]['awayTeam']['name']),date=datum))
        else:
            return(choice(i18n.NEXT_GAME).format(team1=str(response['matches'][0]['awayTeam']['name']),team2=str(response['matches'][0]['homeTeam']['name']),date=datum))
    elif(ask == 2):
        response = get_data("/v2/teams/"+str(team_id),key)
        for i in response["squad"]:
            if i["role"] == "COACH":
                trainer = i["name"]
                break
        try:
            return(choice(i18n.TRAINER_NAME).format(team=team_name,trainer=trainer))
        except:
            return(choice(i18n.NO_TRAINER).format(team=team_name))
