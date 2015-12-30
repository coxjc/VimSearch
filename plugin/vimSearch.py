try:
    import requests
    import vim
    import json
except Exception:
    print("Error occurred while importing dependencies.")

URL = ["http://api.duckduckgo.com/?q=", "&format=json&t=VimSearch"]

def setUrl(query):
    URL.insert(1, query) 
    return ''.join(URL)#Return a string of the final URL (list to str)

def searchToData(url):
    searchReq = requests.get(url)
    return searchReq#return a finalized get request from the url 

def resultsToJson(data):
    data = data.content.decode("utf-8") #Byte >> string/utf-8
    jsonData = json.loads(data)#load to a json object)
    return jsonData

def verifyLength(data):
    if len(data["RelatedTopics"]) > 2:
        parseTo = 3
    else: 
        parseTo = len(data["RelatedTopics"])
    return parseTo #Set up to 3 results, but if there are less than three,
#then set to such.

def setResults(data, max):
    results = []
    try:
        for x in range(max):
            results.append(data["RelatedTopics"][x]["Text"])
    except Exception:
        results[0] = "Sorry, no results for this search query."
    return results#Makes a list of strings of the results.

def search(query):
    #url = setUrl(vim.eval("a:arg")) 
    url = setUrl(query)
    req = searchToData(url)
    jsonD = resultsToJson(req)
    results = setResults(jsonD, verifyLength(jsonD))
    for result in results:
         print(result)
    return
if __name__ == "__main__":
    search(vim.eval("a:arg")) 
