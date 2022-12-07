import json
import yaml
import ruamel.yaml, sys
from ruamel.yaml.comments import CommentedMap
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import argparse

# Notes
# https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html
#
# Take https://raw.githubusercontent.com/iodepo/odis-arch/master/config/sources.yaml
# Generate the gleaner config template

# Initialize args  parser
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--SiteIndex", help = "URL to OIH sources yaml file")
args = parser.parse_args()

r = requests.get(args.SiteIndex)
sd = r.text

sdp = ruamel.yaml.round_trip_load(sd)
# del sdp['sources'][0]

# # sdpv = sdp.items()
# print(sdp)

# assert isinstance(sdp, CommentedMap)

# for value in sdp:
#     print(value)

sdptext = ruamel.yaml.round_trip_dump(sdp, block_seq_indent=0)

# read the PREFIX file# Reading data from file1
with open('gleanerconfigPREFIX.yaml') as fp:
    data = fp.read()

with open('gleanerconfig.yaml', 'w') as outfile:
    outfile.write(data)
    outfile.write(sdptext)
