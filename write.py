import http.client
import json
import configparser
import io
pfad = "/var/lib/snips/skills/Snips-Football-Skill/ligen/"
class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}
def read_configuration_file(configuration_file):
        with io.open(configuration_file, encoding="utf-8") as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
conf = read_configuration_file('/var/lib/snips/skills/Snips-Football-Skill/config.ini')
def get_data(pfad,key):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': str(key) }
    connection.request('GET', pfad, None, headers )
    response = connection.getresponse().read().decode()
    return(response)
ligen = ['BL1', 'PD', 'PL', 'SA', 'FL1','DED']
for i in ligen:
    response = get_data('/v2/competitions/'+i+'/teams',str(conf['secret']['api_key']))
    try:
        json.loads(response)["errorCode"]
        print(json.loads(response)["message"])
        break
    except:
        file = open(pfad+i.lower()+'.json','w')
        file.write(str(response))
        file.close()

