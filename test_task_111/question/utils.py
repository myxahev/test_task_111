
import requests


def get_requests_question(number):
    """ Get API request, return json https://jservice.io/api/random?count=1"""

    response = requests.get("https://jservice.io/api/random?count=%s" % number)

    return response.json()

