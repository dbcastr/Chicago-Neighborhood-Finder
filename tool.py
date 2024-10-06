import googlemaps
import csv

gmaps = googlemaps.Client(key='ADD GOOGLE API KEY HERE')

with open('data.csv', mode = 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        address = row['Address']
        city = row['City']

        formattedAddress = address
        formattedAddress += ', '
        formattedAddress += city
        formattedAddress += ', IL'

        if city == 'Chicago':
            result = gmaps.geocode(formattedAddress)
            neighborhood = result[0].get("address_components")[2].get('long_name')
            print(neighborhood)
        else:
            print('N/A')
        
        

