import datetime
import time
import requests
# from pprint import pprint
import json


def get_timestamp():
    timetuple = datetime.datetime.now().timetuple()
    ftimestamp = time.mktime(timetuple)
    timestamp = str(int(ftimestamp))
    return timestamp


def get_url(token='testing-0123456'):
    base_url = 'https://dropmail.me/api/graphql'
    # token = get_timestamp()
    # token = 'testing-0123456'
    url = f'{base_url}/{token}'
    print(url)
    return url


def query(querydict, url=None, token=None):
    if not url:
        if token:
            url = get_url(token=token)
        else:
            url = get_url()

    print(f'querying: {url}')
    print(f'with {querydict}')
    response = requests.post(url, json=querydict)
    response.raise_for_status()
    print(response.status_code)
    return response.json()


introduce_session = {
    "query":
        "mutation {introduceSession {id, expiresAt, addresses {address}}}"
}
list_sessions = {
    "query":
        "query {sessions {id, expiresAt, mails {rawSize, fromAddr, toAddr, downloadUrl, text, headerSubject}}}"
}
query_session = {
    "query":
        "query ($id: ID!) {session(id:$id) { addresses {address, restoreKey}, mails{rawSize, fromAddr, toAddr, downloadUrl, text, headerSubject}} }",
    "variables":
        {
            "id":
                "U2Vzc2lvbjqQstvqeWZCc75Qj9yBazz6"
        }
}
# print(query(introduce_session))
sessions = query(list_sessions)
print(json.dumps(sessions, indent=4))
session_id = sessions['data']['sessions'][0]['id']
print(f'session_id: {session_id}')
# exit()
query_session['variables']['id'] = session_id
print(query(querydict=query_session))




