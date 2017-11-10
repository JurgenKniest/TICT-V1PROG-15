import requests
import xmltodict

auth_details = ('jurgen.kniest@student.hu.nl', 'ORa2N0Sz6xVGmmFO4Uh3eb8mw6ujmCw-eBU0J-SGaF9xf6gn0JrBxQ')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'

response = requests.get(api_url, auth=auth_details)

vertrekXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen:')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    #pakt de vetrektijd
    vertrektijd = vertrek['VertrekTijd']
    #pakt de huidige tijd:
    vertrektijd = vertrektijd[11:16]

    print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)

