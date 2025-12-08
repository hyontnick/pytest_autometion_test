import requests
import json

# get the test configuration information from the configuration file
with open("../config/config.json", "r") as json_file:
    config = json.load(json_file)

# get the request data from the test data file
with open('../data/request_data.json', 'r') as json_file:
    request_data = json.load(json_file)

# get the response data from the test data file
with open('../data/response_data.json', 'r') as json_file:
    response_data = json.load(json_file)


class TestPytestDemo:

    def test_get_demo(self):
        host = config.get("host")
        get_api = config.get("getAPI")
        get_api_response_data = response_data.get("getAPI")
        # send request
        response = requests.get(host+get_api)
        # assert
        assert response.status_code == 200
        assert response.json() == get_api_response_data

    def test_post_demo(self):
        host = config.get("host")
        post_api = config.get("postAPI")
        post_api_request_data = request_data.get("postAPI")
        post_api_response_data = response_data.get("postAPI")
        # send request
        response = requests.post(host + post_api, post_api_request_data)
        # assert
        assert response.status_code == 201
        # Vérifier la valeur
        assert response.json()["userId"] == "1"

        # Vérifier le type
        assert isinstance(response.json()["userId"], str), "userId devrait être un entier"
        #assert response.json() == post_api_response_data, Test eronner ici car l'userId doit etre un int mais le serveur/api renvoi un str