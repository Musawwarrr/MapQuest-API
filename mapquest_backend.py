#Finds the directions from the json and outputs it
class steps():
    def fetch(self, text):
        print("DIRECTIONS:")
        
        try:
            for m in range(len(text['route']['legs'])):
                for x in range(len(text['route']['legs'][m]['maneuvers'])):
                    print (text['route']['legs'][m]['maneuvers'][x]['narrative'])
        except:
            print()
            print('NO ROUTE FOUND')
            exit()

#Calculates the total distance from the JSON
class totaldistance():
    def fetch(self, text):
        try:
            rounded = round(text['route']['distance'])
            print("TOTAL DISTANCE:", rounded, "miles.")
        except:
            print()
            print("NO ROUTE FOUND")
            exit()

#Calculates the total time from the JSON
class totaltime():
    def fetch(self, text):
        try:
            minutes = round((text['route']['time'])/60) 
            print("TOTAL TIME:", minutes, "minutes.")
        except:
            print()
            print("NO ROUTE FOUND")
            exit()

#Latitude and Longitude used for the elevation
class e_latlong():
    def fetch(self, text):
        latlng = []

        try:
            for m in range(len(text['route']['locations'])):
                for x in range(len(text['route']['locations'][m]['latLng']) - 1):
                    latlng.append(str(text['route']['locations'][m]['latLng']['lat']))
                    latlng.append(str(text['route']['locations'][m]['latLng']['lng']))

        except:
            print()
            print('NO ROUTE FOUND')
        
        return latlng

#Latitude and Longitude from JSON outputted
class latlong():
    def fetch(self, text):
        lat = []
        lng = []
        try:
            print("LATLONGS:")

            for m in range(len(text['route']['locations'])):
                for x in range(len(text['route']['locations'][m]['latLng']) - 1):
                    latitude(text, m, lat)
                    longitude(text, m, lng)
                
            for x in range(len(lat)):
                print (lat[x], lng[x])
        except:
            print()
            print("NO ROUTE FOUND")
            exit()

#Rounds the latitude to 2 decimal places and figures out which direction it is
def latitude(text, m, lat):
        if text['route']['locations'][m]['latLng']['lat'] < 0:
            lat.append(str('%0.2f' % (text['route']['locations'][m]['latLng']['lat'] * -1)) + 'S')
        elif text['route']['locations'][m]['latLng']['lat'] > 0:
            lat.append(str('%0.2f' % (text['route']['locations'][m]['latLng']['lat'])) + 'N')

#Rounds up the longitude to 2 decimal places and figures out which direction it is 
def longitude(text, m, lng):
        if text['route']['locations'][m]['latLng']['lng'] < 0:
            lng.append(str('%0.2f' % (text['route']['locations'][m]['latLng']['lng'] * -1)) + 'W')
        elif text['route']['locations'][m]['latLng']['lng'] > 0:
            lng.append(str('%0.2f' % (text['route']['locations'][m]['latLng']['lng'])) + 'E')

#Finds the elevation of a specific place from JSON
class elevation():
    def fetch(self, text):
        try:
            print('ELEVATION:')

            for m in range(len(text['elevationProfile'])):
                for x in range(len(text['elevationProfile'][m]) -1):
                    print (text['elevationProfile'][m]['height'])
        except:
            print()
            print("NO ROUTE FOUND")
            exit()

#Carries out most of the class actions
def fetch_data(output, text):
    for data in output:
        data.fetch(text)
        print()

#Carries out the elevation class because it requires the return 
def e_fetch_data(output, text):
    for data in output:
        return data.fetch(text)


         


