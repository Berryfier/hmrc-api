#!/usr/bin/env python3

# This is example code for using the
# 'HMRC Developer Hub' 'Create Test User' Test Support API.
# The example code uses this interface to generate credentials for a user
# which is an organisation, and enrolls the user for 'Making Tax Digital' VAT

# Usage:
# save this file as test2userAPI.py
# in terminal use $ python3 test2userAPI.py


import requests

# Use the token in the developer credentials allocated to you by HMRC
SERVER_TOKEN = "05eca4b94eecc5123b4679bd0e07f0"

p = requests.post("https://test-api.service.hmrc.gov.uk/create-test-user/organisations",
                  headers={
			  "accept": "application/vnd.hmrc.1.0+json",
			  "authorization": "Bearer {}".format(SERVER_TOKEN)
			  },
		  json={
			  "serviceNames":["mtd-vat"]
			  }
		  )

print(p.status_code)
print(p.content)
