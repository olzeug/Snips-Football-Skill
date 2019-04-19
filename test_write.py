import http.client
import json
pfad = "/var/lib/snips/dateien/Datenbanken/ligen/"
def get_data(pfad):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': '{your API-KEY}' }
    connection.request('GET', pfad, None, headers )
    response = connection.getresponse().read().decode()
    return(response)
ligen = ['BL1', 'PD', 'PL', 'SA', 'FL1']
for i in ligen:
    response = get_data('/v2/competitions/'+i+'/teams')
    file = open(pfad+i.lower()+'.json','w')
    file.write(str(response))
    file.close()
