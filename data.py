import requests

resp = requests.get("https://data.melbourne.vic.gov.au/resource/6cxw-5y4y.json")
data= resp.json()

spots = {}

for i in data:
    nm= i.get("common_name")
    if nm not in spots:
        spots[nm]=0
    spots[nm]+=1


myfile = open("birds.txt", "w")

for bird in spots:
    myfile.write(bird + "\t" + str(spots.get(bird)) + "\n")

myfile.close()