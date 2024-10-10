import requests
import hashlib

#api call
def request_api_data(str):
    url = 'https://api.pwnedpasswords.com/range/' + str
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError('please check the API call and try again')
    return response

#sha1 hashing
def hash_password(password):
    encd_pwd = password.encode('utf-8')
    hashed_pwd = hashlib.sha1(encd_pwd)
    hashed_hex_pwd = hashed_pwd.hexdigest()
    return hashed_hex_pwd.upper()


print(hash_password('Ajay'))