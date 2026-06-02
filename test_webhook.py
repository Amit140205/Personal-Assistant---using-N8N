import requests

user_message="Can you tell me about balck holes in 3-4 lines?"

request_message={
    "message": user_message
}

url="http://localhost:5678/webhook-test/6fe814e1-ff1f-42b5-869e-b378f1cf3497"

response=requests.post(url, json=request_message)

print(response.status_code)
# print(response.json())
print(response.json()[0]["output"])