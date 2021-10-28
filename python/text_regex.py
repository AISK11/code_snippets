#!/usr/bin/env python3

###############################################
# Author: AISK11                              #
# Description: this snippet returns matching  #
# regex result from a string                  #
###############################################

## Library for regex:
import re


def text_regex(string = "", regex = ".*"):
    ## Perform regex search in string:
    result = re.search(str(regex), str(string))

    ## If there is match: type(result) == <class 're.Match'>    
    ## otherwise: type(result) == <class 'NoneType'>

    ## If object 'result' is NOT type 're.Match',
    ## return empty string:
    if not isinstance(result, re.Match):
        return ""
    ## Return only (first item in) string matching regex:
    return result.group(0)


matching_string = text_regex('<output id="res1" for="ta">1 DKK = 0.155852 USD</output>', '[0-9]{1,}\.[0-9]{1,}') ## CHANGE THIS
print(f"{matching_string}")
