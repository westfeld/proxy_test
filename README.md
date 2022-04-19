# Proxy Test App

Minimal demo app which querys an external API via HTTPS.

## Installation

* Clone the repo to your local disc. 
* create a virtualenvironment
* add requirements: Django, requests and mitmproxy, just run `pip install -r requirements.txt`

## Prepare Certificates

Start mitmproxy for the first time (no root user is required). At `$HOME/.mitmproxy` the CA certificates of the proxy are stored.

## Prepare Environment

The following environment variables have to be set:

`HTTPS_PROXY=http://localhost:8080`
This tells requests to use the proxy

`REQUESTS_CA_BUNDLE=$HOME/.mitmproxy/mitmproxy-ca.pem`
This tells requests where the CA of the proxy server is, that the TLS handshake can be completed successfully.


## Start Development Server

`./manage.py runserver`

Open a browser and navigate the adress, typically `http://localhost:8000`.
