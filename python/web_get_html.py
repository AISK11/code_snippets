#!/usr/bin/env python3

###############################################
# Author: AISK11                              #
# Description: this snippet returns html code #
# as a string when provided with a valid URL. #
###############################################

## Library for handling web requests:
import urllib.request, urllib.error
## Library for handling output to stderr and exit code:
import sys
## Library for returning exit codes as defined in POSIX:
## https://docs.python.org/2/library/os.html#process-management
import os

def web_get_html(url):
    ## Try to open requested URL:
    try:
        ## HTTPResponse object:
        req = urllib.request.urlopen(url)
    ## Exception: HTTP status code (e.g. 404, 502, ...):
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code}", file=sys.stderr)
        sys.exit(os.EX_UNAVAILABLE)
    ## Exception: most likely wrong URL:
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason}", file=sys.stderr)
        sys.exit(os.EX_NOHOST)

    ## Read bytes from HTTPResponse and then decode from bytes to string:
    html = req.read().decode("utf8")

    ## Return HTML code:
    return html


html = web_get_html("http://www.python3.com") ## CHANGE THIS
print(f"{html}")

