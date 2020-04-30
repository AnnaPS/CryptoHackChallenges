#!/usr/bin/env python3

import base64
import sys
import codecs

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()

print(b64)