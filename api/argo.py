import os
import requests
from pprint import pprint


class Application(object):

    def __init__(self, name, revision, podName):
        self.name     = name
        self.revision = revision
        self.podName  = podName

    def __repr__(self):
        print(self.name)
        return "%s(%s, %s, %s)" % (
                    self.__class__.__name__,
                    self.name,
                    self.revision,
                    self.podName
                )

def apiCall(endpoint):
    headers={"Authorization": "Bearer %s" % (os.getenv("TOKEN"))}
    req = requests.get(endpoint, verify=False, headers=headers)
    return req.json()

c = Application("goSite", "0.0.7", "sean-goSite")

pprint(apiCall("https://127.0.0.1:8099/api/v1/applications/gosite"))
