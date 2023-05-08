import json
import yaml
import csv
import codecs
import ruamel.yaml, sys
from ruamel.yaml.comments import CommentedMap
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import argparse

# Notes
# https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html
# Google doc is at: https://docs.google.com/spreadsheets/d/1G7Wylo9dLlq3tmXe8E8lZDFNKFDuoIEeEZd3epS0ggQ/edit#gid=1340502269
# Take https://docs.google.com/spreadsheets/d/1G7Wylo9dLlq3tmXe8E8lZDFNKFDuoIEeEZd3epS0ggQ/gviz/tq\?tqx\=out:csv\&sheet\=sources
# Generate the gleaner config template


# converts single url file
def urlCSV(url, output=None):
    csvFile = urlopen(url)
    output = output if output else root+'/'+(url.split('/')[-1].replace('.csv','.yml'))
    csvToYaml(csvFile, output) 

# takes a csvFile name and output file name/path
def csvToYaml(csvFile, output):
    stream = open(output, 'w',encoding="utf-8")
    csvOpen = csv.reader(codecs.iterdecode(csvFile, 'utf-8'))
    keys = next(csvOpen)
    for row in csvOpen:
        if row[2] == "TRUE":
            row[2] = True  # we are only dealing with active TRUE, so convert to a real boolean
            if row[6] == "TRUE":
                row[6] = True
            else:
                row[6] = False
            del row[11]  # remove some ECO columns we don't use
            del row[10]  
            # del row[0]  # what even is the "hack" column

            yaml.dump([dict(zip(keys, row))], stream, default_flow_style=False, allow_unicode=True)

# Initialize args  parser
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--SiteIndex", help = "URL to OIH sources yaml file")
args = parser.parse_args()

urlCSV(args.SiteIndex, "sources.yaml")

