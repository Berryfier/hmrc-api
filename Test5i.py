# An example of Python3 code inspired by:
# HMRC VAT(MTD) API

# scope=write:vat

# Usage:
# save this file as Test5i.py
# in terminal use $ python3
# use >>> from Test5i import *
# then use the functions in a good sequence

import json
from datetime import datetime
from requests_oauthlib import OAuth2Session

# obtain these from your HMRC developer account on registration
CLIENT_ID = "mSBWD9mCAKOx8tfa873AZYaoegwa"
CLIENT_SECRET = "7c645e38-8d55-5529-8e40-a72297730483"

request = {
    "periodKey": "#001",
    "vatDueSales": 100.00,
    "vatDueAcquisitions": 100.00,
    "totalVatDue": 200.00,
    "vatReclaimedCurrPeriod": 100.00,
    "netVatDue": 100.00,
    "totalValueSalesExVAT": 500,
    "totalValuePurchasesExVAT": 500,
    "totalValueGoodsSuppliedExVAT": 500,
    "totalAcquisitionsExVAT": 500,
    "finalised": True
    }

def Authorise(scope):
    """"obtains authorisation from the user"""
    # use >>> (hmrc,token) = Authorise("write:vat")
    # subsequent authorisation can be by token
    # construct OAuth2 Authorise Request
    hmrc = OAuth2Session(CLIENT_ID, scope=scope, redirect_uri="https://example.com/redirect")
    # at this stage hmrc.authorized is False
    authorization_url, state = hmrc.authorization_url("https://test-api.service.hmrc.gov.uk/oauth/authorize")
    # the above state parameter is used to bind request and redirect
    print("Please go here and authorize: {}".format(authorization_url))
    # capture authorisation code (as querystring parameter)
    redirect_response = input('Paste the full redirect URL here: ')
    # construct OAuth2 Access Token Request (using querystring parameter)
    token = hmrc.fetch_token("https://test-api.service.hmrc.gov.uk/oauth/token",
                             client_secret=CLIENT_SECRET,
                             authorization_response=redirect_response)
    return (hmrc, token)


def loadToken():
    """load token previously obtained"""
    # use >>> token=loadToken()
    with open("/home/pi/HMRC/token5.json", "r") as f:
        token=json.load(f)
    return token

def checkToken(token):
    """checks for token expiry"""
    # use >>> checkToken(token)
    print("The token expires at {}".format(datetime.utcfromtimestamp(token['expires_at'])))
    print("The date and time is {}".format(datetime.utcnow()))

def startSession(token):
    """set up a new OAuth2 Session"""
    # use >>> hmrc=startSession(token)
    hmrc=OAuth2Session(CLIENT_ID, token=token)
    return hmrc

def renewToken(hmrc):
    # use >>> token=renewToken(hmrc)
    token = hmrc.refresh_token("https://test-api.service.hmrc.gov.uk/oauth/token", client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    return token

def saveToken(token):
    """save the token allready obtained"""
    # use >>> saveToken(token)
    with open("/home/pi/HMRC/token5.json", "w") as f:
        json.dump(token, f)

def postReturns(hmrc):
    """ post data to the hmrc sandbox endpoint with /organisations/vat/666582124/returns path"""
    # use >>> p = postReturns(hmrc)
    p = hmrc.post("https://test-api.service.hmrc.gov.uk/organisations/vat/666582124/returns",
                  headers={"Accept": "application/vnd.hmrc.1.0+json","Content-Type":"application/json"},
                  json=request)
    print(p.status_code)
    print(json.dumps(p.json(), indent=4))
    return p


