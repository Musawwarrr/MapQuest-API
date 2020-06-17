import mapquest_backend
import mapquest_network


#The main workshop of the whole program
def main_frame(d, o):
    user_inp(d, o)
    url = mapquest_network.url_maker(d[0], d[1])

    converted_text = mapquest_network.conversion(url)

    output_list = []
    e_list = []
    
    for x in o:
        if x == 'STEPS':
            output_list.append(mapquest_backend.steps())
        elif x == 'TOTALDISTANCE':
            output_list.append(mapquest_backend.totaldistance())
        elif x == 'TOTALTIME':
            output_list.append(mapquest_backend.totaltime())
        elif x == 'LATLONG':
            output_list.append(mapquest_backend.latlong())
        elif x == 'ELEVATION':
            e_list.append(mapquest_backend.elevation())

    p = mapquest_backend.fetch_data(output_list, converted_text)
    
    #Part for the elevation
    s = []
    s.append(mapquest_backend.e_latlong())
    q = mapquest_backend.e_fetch_data(s, converted_text)
    
    e_url = mapquest_network.e_url_maker(q)
    e_converted_text = mapquest_network.conversion(e_url)

    m = mapquest_backend.fetch_data(e_list, e_converted_text)

    print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.')
    print()

#All the user input is processed here
def user_inp(d, o): 
    destinations = 0
    outputs = 0
    t = []
    
    while destinations <= 1: 
        destinations = int(input())

        if destinations <= 1:
            print("You need to provide at least 2 destinations.")
            print()
        else: 
            fr = input()
            d.append(fr)

            for x in range(destinations - 1): 
                des = input()
                t.append(des)
            d.append(t)
    
    while outputs < 1:
        outputs = int(input())

        if outputs < 1:
            print("You need to provide at least 1 output.")
            print()
        else:
            for x in range(outputs):
                a = input().upper().strip()
                o.append(a)
    
    print()

#Runs the whole function
def main(): 
    d =[]
    o = []
    main_frame(d, o)

if __name__ == '__main__':
    main()
