import requests as req

def send_a_request(data):
     q = f"https://www.google.com/search?q={data}"
     print(f"The URL is: {q}")
     x = req.get(q)
     print(f"{x.status_code}")