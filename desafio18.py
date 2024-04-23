import requests

url = "https://reqres.in/api/users"

payload = {}
headers = {}

# 1
users_data = requests.request("GET", url, headers=headers, data=payload)
print(users_data.text)

# 2
payload = '''{"first_name": "Ignacio",
"job": "Profesor"}'''

headers = {
    'Content-Type': 'application/json'
}

created_user = requests.request("POST", url, headers=headers, data=payload)
print(created_user.text)

# 3
payload = '''{"first_name": "morpheus",
"residence": "zion"}'''

headers = {
    'Content-Type': 'application/json'
}

updated_user = requests.request("PUT", url, headers=headers, data=payload)
print(updated_user.text)

# 4
delete_url = "https://reqres.in/api/users/6"

headers = {}

response = requests.delete(delete_url, headers=headers)

print(response.text)