#!/usr/bin/env python3
#
# HMRC Making Tax Digital
# https://developer.service.hmrc.gov.uk/api-documentation
# Tutorials: Accessing an Open Endpoint
# A code translatation from the Java snippet.

# Usage:
# save this file as test0.py
# in terminal use $ python3 test0.py


print("Importing ...  ")
import requests
print("done \n")
# construct and execute the GET request for our Hello World endpoint
g = requests.get("https://test-api.service.hmrc.gov.uk/hello/world", headers={"accept": "application/vnd.hmrc.1.0+json"})
# extract the HTTP status code and response body
print(g.status_code)
print(g.content)

