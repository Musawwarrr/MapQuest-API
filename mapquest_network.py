import json
import urllib.parse
import urllib.request

API = '9J70Dc7iOM0awGlhrpzMoq3N6vEoxGQA'

base_url = 'https://open.mapquestapi.com/'

#Makes the URL 
def url_maker(f, t):
    parameters = [('key', API), ('from', f)]

    for x in t:
        p = ('to', x)
        parameters.append(p)

    return base_url + 'directions/v2/route?' + urllib.parse.urlencode(parameters)

#Makes the URl for the elevation
def e_url_maker(latlnglist):
    parameters = [('key', API), ('latLngCollection', "")]

    c = ','.join(latlnglist)

    p = str(c)

    return base_url + 'elevation/v1/profile?' + urllib.parse.urlencode(parameters) + p

#Converts thr url to JSON form
def conversion(url):
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    except:
        print()
        print('MAPQUEST ERROR')
        exit()

    finally: 
        if response != None: 
            response.close()


