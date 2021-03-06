# Examples of Python3 code inspired by
# HMRC VAT(MTD) API documentation
# https://developer.service.hmrc.gov.uk

#These examples use the GET API resources
scope="read:vat"


# Usage:
# save this file as Test4i.py
# in terminal use $ python3
# use >>> from Test4i import *
# then use the functions in a good sequence

import json
from datetime import datetime
from urllib.request import pathname2url
from requests_oauthlib import OAuth2Session

# obtain these from your HMRC developer account on registration
CLIENT_ID = "mSBWD9mCAKOx8tfa873AZYaoegwa"
CLIENT_SECRET = "7c645e38-8d55-5529-8e40-a72297730483"

def Authorise(scope):
    """"obtains authorisation from the user"""
    # use >>> (hmrc,token) = Authorise(scope)
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
    with open("/home/pi/HMRC/token4.json", "r") as f:
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
    with open("/home/pi/HMRC/token4.json", "w") as f:
        json.dump(token, f)

def getObligations(hmrc,fromDate,toDate):
    """ get data from the hmrc sandbox endpoint with /organisations/vat/666582124/obligations path"""
    # use >>> g = getObligations(hmrc,"2017-01-01","2017-12-30")
    g = hmrc.get("https://test-api.service.hmrc.gov.uk/organisations/vat/666582124/obligations", headers={"Accept": "application/vnd.hmrc.1.0+json","Content-Type":"application/json"}, params={"from":fromDate,"to":toDate})
    print(g.status_code)
    print(json.dumps(g.json(), indent=4))
    return g

def getReturns(hmrc,periodKey):
    """ get data from the hmrc sandbox endpoint with /organisations/vat/666582124/returns/{periodKey} path"""
    # use >>> g = getReturns(hmrc,"#001")
    g = hmrc.get("https://test-api.service.hmrc.gov.uk/organisations/vat/666582124/returns/" + pathname2url(periodKey), headers={"Accept": "application/vnd.hmrc.1.0+json","Content-Type":"application/json"})
    print(g.status_code)
    if len(g.content)==0:
        print(g.content)
    else:
        print(json.dumps(g.json(), indent=4))
    return g

def getSingleLiability(hmrc):
    """ get data from the hmrc sandbox endpoint with /organisations/vat/666582124/liabilities path"""
    # use >>> g = getSingleLiability(hmrc)
    g = hmrc.get("https://test-api.service.hmrc.gov.uk/organisations/vat/666582124/liabilities", headers={"Accept": "application/vnd.hmrc.1.0+json","Content-Type":"application/json","Gov-Test-Scenario":"SINGLE_LIABILITY"}, params={"from":"2017-01-02","to":"2017-02-02"})
    print(g.status_code)
    print(json.dumps(g.json(), indent=4))
    return g

def getMultipleLiabilities(hmrc):
    """ get data from the hmrc sandbox endpoint with /organisations/vat/666582124/liabilities path"""
    # use >>> g = getMultipleLiabilities(hmrc)
    g = hmrc.get("https://test-api.service.hmrc.gov.uk/organisations/vat/666582124/liabilities", headers={"Accept": "application/vnd.hmrc.1.0+json","Content-Type":"application/json","Gov-Test-Scenario":"MULTIPLE_LIABILITIES"}, params={"from":"2017-04-05","to":"2017-12-21"})
    print(g.status_code)
    print(json.dumps(g.json(), indent=4))
    return g

def getSinglePayment(hmrc):
    """ get data from the hmrc sandbox endpoint with /organisations/vat/666582124/payments path"""
    # use >>> g = getSinglePayment(hmrc)
    g = hmrc.get("https://test-api.service.hmrc.gov.uk/organisations/vat/666582124/payments", headers={"Accept": "application/vnd.hmrc.1.0+json","Content-Type":"application/json","Gov-Test-Scenario":"SINGLE_PAYMENT"}, params={"from":"2017-01-02","to":"2017-02-02"})
    print(g.status_code)
    print(json.dumps(g.json(), indent=4))
    return g

def getMultiplePayments(hmrc):
    """ get data from the hmrc sandbox endpoint with /organisations/vat/666582124/payments path"""
    # use >>> g = getMultiplePayments(hmrc)
    g = hmrc.get("https://test-api.service.hmrc.gov.uk/organisations/vat/666582124/payments", headers={"Accept": "application/vnd.hmrc.1.0+json","Content-Type":"application/json","Gov-Test-Scenario":"MULTIPLE_PAYMENTS"}, params={"from":"2017-02-27","to":"2017-12-21"})
    print(g.status_code)
    print(json.dumps(g.json(), indent=4))
    return g



