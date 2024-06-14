import requests

url = "https://cloud.seatable.io/dtable-server/api/v1/dtables/c695d59d-5db8-49e8-878e-fef29d8a5077/rows/?table_name=Table2&view_name=Default%20View"

headers_BaseToken = {
    "accept": "application/json",
    "authorization": "Bearer d0ff0da1a3866c4a33210bbfb4a68a7ea7d35cfb"
}

def getBaseToken():
    url_BaseToken = "https://cloud.seatable.io/api/v2.1/dtable/app-access-token/"

    headers_BaseToken = {
        "accept": "application/json",
        "authorization": "Bearer d0ff0da1a3866c4a33210bbfb4a68a7ea7d35cfb"
    }
    response = requests.get(url_BaseToken, headers=headers_BaseToken)
    BaseToken = response.json()['access_token']

    return BaseToken    #return BaseToken in str type

headers = {
    "accept": "application/json",
    "authorization": "Bearer " + getBaseToken()
}

TOKEN = '6815329478:AAHYcixEDoxXbqMDSDuppTjrqtapAS4zWAk'

id_channel = "@FurinaOnee"
id_main_Admin = "@clkkrs"
id_channel_test = "@fur1inatest"
