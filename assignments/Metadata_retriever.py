def normalizer(): 
    request = input("What are we looking for today? Enter a name: ")
    request = request.strip()
    request = request.lower()
    request = request.replace(" ","+")
    return request


def searcher(request):
    url = "https://www.europeana.eu/api/entities/suggest?wskey=apidemo&text={}&type=agent".format(request)
    response = urllib.request.urlopen(url).read() #open the URL 
    json_obj = str(response, "utf-8") #make the URL response into a json object
    data = json.loads(json_obj) #load the json data
    try:
        for item in data["items"]: #check if the input of the user is in data[items] and print the result
            print(item)
    except:
        print("Item not available") #if the input is not available: print the error
        normalizer() #start over

request = normalizer()
searcher(request)