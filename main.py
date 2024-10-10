import requests
import hashlib
import sys

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

# checks if pwned and returns the pwn count, else returns 0
def check_if_pwned(password):
    hashed_password = hash_password(password)
    head, tail = hashed_password[:5], hashed_password[5:]
    response = request_api_data(head)

    list_of_lines = response.text.splitlines()
    for (line, count) in [ line.split(':') for line in list_of_lines]:
        if(line == tail):
            return count
    return 0

#to get the list of passwords from the command line
list_of_passwords = sys.argv[1:]
for password in list_of_passwords:
    res = check_if_pwned(password)
    if (res == 0):
        print(f"{password} - is secure and not even breached once!!!")
    else:
        print(f"{password} - is breached {res} times! - CHANGE IT NOW")
