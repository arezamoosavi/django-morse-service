import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "http://127.0.0.1:8000/api/v1/morse"
  
# data to be sent to api 
data = {'sentence':"Hello from Iran"} 
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
pastebin_url = r.json()['morse_code']
print(pastebin_url) 



API_ENDPOINT = "http://127.0.0.1:8000/api/v1/queue"
data = {'messege':r.json()['morse_code']} 
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 
