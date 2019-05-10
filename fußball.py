import http.client
import json
from datetime import date,datetime
import re
import time
from random import choice
monate = ['Januar', 'Februar', 'März','April','Mai','Juni','Juli','August','September','November','Dezember']
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
def wörter_trennen(t):
        text =[]
        wort_teil = ''
        for i in str(t):
            if(i == ' '):
                text += [wort_teil]
                wort_teil = ''
            else:
                wort_teil = wort_teil+str(i)
        text += [wort_teil]
        return(text)
def compare(a,b):
        found_count = 0
        text_a = wörter_trennen(a.lower())
        text_b = wörter_trennen(b.lower())
        if (a == b):
            found_count = len(text_a)
        else:
            for a in text_a:
                for t in text_b:
                    if a == t:
                        found_count += 1
                if(len(a) > 3):
                    for y in text_b:
                        if(a in y or y in a):
                            found_count += 1
                else:
                    for y in text_b:
                        if(a == y == y in a):
                            found_count += 1
        return(found_count)
def end_stand(a, team_id, response):
    if (response['matches'][a]['score']['winner'] == "HOME_TEAM"):
        if (str(response['matches'][a]['homeTeam']['id']) == str(team_id)):
            last_game = "win"
        elif(str(response['matches'][a]['awayTeam']['id']) == str(team_id)):
            last_game = "lose"
    elif (str(response['matches'][a]['score']['winner']) == "AWAY_TEAM"):
        if (str(response['matches'][a]['awayTeam']['id']) == str(team_id)):
            last_game = "win"
        elif(str(response['matches'][a]['homeTeam']['id']) == str(team_id)):
            last_game = "lose"
    elif (str(response['matches'][a]['score']['winner']) == "DRAW"):
        last_game = "draw"
    return(last_game)
def get_team_id(search):
    ligen = ['BL1', 'PD', 'PL', 'SA', 'FL1']
    team_id = []
    team_name = []
    count = []
    for y in ligen:
        with open('/var/lib/snips/dateien/Datenbanken/ligen/'+y.lower()+'.json') as f:
            response = json.load(f)
        i = 0
        while True:
            try:
                name = compare(search, str(response['teams'][i]['name']))
                shortName = compare(search, str(response['teams'][i]['shortName']))
                tla = compare(search, str(response['teams'][i]['tla']))
                if(name>0 or shortName>0 or tla>0):
                    count += [str(int(name)+int(shortName)+int(tla))]
                    team_id += [str(response['teams'][i]['id'])]
                    team_name += [str(response['teams'][i]['name'])]
                i += 1
            except:
                break
    ta = 0
    team = 0
    for t in count:
        if (int(count[ta]) == int(max(count))):
            team = int(ta)
            break
        ta += 1
    return([str(team_id[team]),str(team_name[team])])
def get_football_result(search,ask,key):
    team_id,team_name = get_team_id(search)
    if(ask == 0):
        response = get_data('/v2/teams/'+team_id+'/matches?status=FINISHED',key)
        i=-1
        home_score = response['matches'][i]['score']['fullTime']['homeTeam']
        away_score = response['matches'][i]['score']['fullTime']['awayTeam']
        if (response['matches'][i]['score']['fullTime']['homeTeam'] > response['matches'][i]['score']['fullTime']['awayTeam']):
            if(home_score-3 > away_score or home_score < away_score-3):
                return(response['matches'][i]['homeTeam']['name']+' hat die Mannschaft '+response['matches'][i]['awayTeam']['name']+' im Fußball-'+str(response['matches'][i]['competition']['name'])+'-Match '+str(response['matches'][i]['score']['fullTime']['homeTeam'])+' zu '+str(response['matches'][i]['score']['fullTime']['awayTeam'])+' '+choice(['vom Platz gefegt.','abserviert.','vernichtet.','besiegt.','bezwungen.','geschlagen.']))
            else:
                return(response['matches'][i]['homeTeam']['name']+' hat die Mannschaft '+response['matches'][i]['awayTeam']['name']+' im Fußball-'+str(response['matches'][i]['competition']['name'])+'-Match '+str(response['matches'][i]['score']['fullTime']['homeTeam'])+' zu '+str(response['matches'][i]['score']['fullTime']['awayTeam'])+' '+choice(['besiegt.','bezwungen.','geschlagen.']))
        elif (response['matches'][i]['score']['fullTime']['homeTeam'] < response['matches'][i]['score']['fullTime']['awayTeam']):
            if(home_score-3 > away_score or home_score < away_score-3):
                return(response['matches'][i]['homeTeam']['name']+' wurde von der Mannschaft '+response['matches'][i]['awayTeam']['name']+' im Fußball-'+str(response['matches'][i]['competition']['name'])+'-Match '+str(response['matches'][i]['score']['fullTime']['homeTeam'])+' zu '+str(response['matches'][i]['score']['fullTime']['awayTeam'])+' '+choice(['vom Platz gefegt.','abserviert.','vernichtet.','besiegt.','bezwungen.','geschlagen.']))
            else:
                return(response['matches'][i]['homeTeam']['name']+' wurde von der Mannschaft '+response['matches'][i]['awayTeam']['name']+' im Fußball-'+str(response['matches'][i]['competition']['name'])+'-Match '+str(response['matches'][i]['score']['fullTime']['homeTeam'])+' zu '+str(response['matches'][i]['score']['fullTime']['awayTeam'])+' '+choice(['besiegt.','bezwungen.','geschlagen.']))
        elif (response['matches'][i]['score']['fullTime']['homeTeam'] == response['matches'][i]['score']['fullTime']['awayTeam']):
            return(response['matches'][i]['homeTeam']['name']+' hat die Mannschaft '+response['matches'][i]['awayTeam']['name']+' im Fußball-'+str(response['matches'][i]['competition']['name'])+'-Match nicht besiegen können, wegen einem '+str(response['matches'][i]['score']['fullTime']['homeTeam'])+' zu '+str(response['matches'][i]['score']['fullTime']['awayTeam']))
    elif(ask == 1):
        response = get_data('/v2/teams/'+team_id+'/matches?status=SCHEDULED&limit=1',key)
        if (tag_diff(str(response['matches'][0]['utcDate'])) == 0):
            datum = str(response['matches'][0]['utcDate'])
            datum = "um "+str(int(re.split('[^\d]', datum)[3])+1)+' Uhr  '+str(re.split('[^\d]', datum)[4])
        else:
            datum = str(response['matches'][0]['utcDate'])
            datum = "am "+str(re.split('[^\d]', datum)[2])+'. '+str(monate[int(re.split('[^\d]', datum)[1])-1])+' '+str(re.split('[^\d]', datum)[0])+' um '+str(int(re.split('[^\d]', datum)[3])+1)+' Uhr  '+str(re.split('[^\d]', datum)[4])
        if (team_id == str(response['matches'][0]['homeTeam']['id'])):
            return('Das Team "'+str(response['matches'][0]['homeTeam']['name'])+'" trifft auf das Team "'+str(response['matches'][0]['awayTeam']['name'])+'" '+datum)
        else:
            return('Das Team "'+str(response['matches'][0]['awayTeam']['name'])+'" trifft auf das Team "'+str(response['matches'][0]['homeTeam']['name'])+'" '+datum)
