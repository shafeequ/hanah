TestMyOAuthProvide = False
import requests
import json

if not TestMyOAuthProvide:
    HOST = 'https://api-sandbox.bookingkit.de'
    BASE_HOST_URL = HOST+ '/v3/'
    TOKEN_URL = HOST+ '/oauth/token'
    VENDORS_LIST = HOST+ '/v3/vendors/'
    EVENTS_LIST = HOST+ 'v3/events/'
    client_id, client_secret, grant_type = ("GLS1KEik", "4SSju8wtbdqxBYsd5fFnE1DBJj1Xxz4s", "client_credentials")
    data = {"grant_type": grant_type}
    try:
        response = requests.post(TOKEN_URL, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

        print(f"response.text={response.text}")
        tokens = json.loads(response.text)
        print(f"tokens={tokens}")

        api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
        api_call_response = requests.get(VENDORS_LIST, headers=api_call_headers, verify=False)

        print(api_call_response.text)
    except Exception as e:
        print("Exception as {}".format(e))
else:
    HOST = 'http://127.0.0.1:8011'
    TOKEN_URL = HOST+ '/o/token/'
    VENDORS_LIST = HOST+ '/profile/'
    client_id, client_secret, grant_type = ("WsvpY7YK8gFKoU6RxGV7iRvoVe7KyGwTNrGhfj5c", "9hlz8CSltXyJVq6Di3TXAPxOyoaHfim5uV726T3IjuQTVlfMfFQ7Kn8LitDB9O0cRrWDwPB1nja7FpTGeb3eW0BqHGCCRoSXvZSqCIXIiwGZXmRUgaSNl84L8NY5QSXF", "client_credentials")
    data = {"grant_type": grant_type}
    try:
        response = requests.post(TOKEN_URL, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

        # print(f"response.text={response.text}")
        tokens = json.loads(response.text)
        api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
        api_call_response = requests.get(VENDORS_LIST, headers=api_call_headers, verify=False)
        print(api_call_response.text)
    except Exception as e:
        print("Exception as {}".format(e))
