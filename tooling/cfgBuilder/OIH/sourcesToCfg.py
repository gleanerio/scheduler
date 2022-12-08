import json
import yaml
import ruamel.yaml, sys
from ruamel.yaml.comments import CommentedMap
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import argparse

# Usage
# python sourcesToCfg.py -o ../../../configs/oih/gleanerconfig.yaml -s https://raw.githubusercontent.com/iodepo/odis-arch/master/config/sources.yaml


# Notes
# https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html

# Initialize args  parser
parser = argparse.ArgumentParser()

parser.add_argument("-s", "--SiteIndex", help = "URL to OIH sources yaml file")
parser.add_argument("-o", "--Output", help = "Locate to save the output file")

args = parser.parse_args()

r = requests.get(args.SiteIndex)
sd = r.text

sdp = ruamel.yaml.round_trip_load(sd)

sdptext = ruamel.yaml.round_trip_dump(sdp, block_seq_indent=0)

# read the PREFIX file# Reading data from file1
with open('gleanerconfigPREFIX.yaml') as fp:
    data = fp.read()

with open(args.Output, 'w') as outfile:
    outfile.write(data)
    outfile.write(sdptext)
