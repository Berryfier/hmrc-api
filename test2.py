#!/usr/bin/env python3

# Tutorials: Accessing an application-restricted endpoint.

# Usage:
# save this file as test2.py
# in terminal use $ python3 test2.py


# Provide Authentication Credentials
SERVER_TOKEN = "05eca4b94eecc5123b4679bd0e07f0"

import requests

g = requests.get("https://test-api.service.hmrc.gov.uk/hello/application",
                 headers={
                          "accept": "application/vnd.hmrc.1.0+json",
                          "authorization": "Bearer {}".format(SERVER_TOKEN)
                         }
                )
print(g.url)
print(g.status_code)
print(g.content)


