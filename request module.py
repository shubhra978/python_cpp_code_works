import requests #requets library fetch request from web

response = requests.get("https://www.codechef.com/ide") # get function helps in fetching the content of the url 

format = response.json() #json converts the response into a json format

print(format)
