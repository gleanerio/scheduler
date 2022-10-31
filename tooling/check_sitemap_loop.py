import advertools as adv
import requests, sys, os
import yaml
from urllib.request import urlopen
import logging

# this script has an annoying stderr from advertools
# run with

#   python check_sitemap_loop.py  2> /dev/null

# to route stderr to dev/null

# Fun commands: grep " name:" gleanerconfig.yaml | awk '{print "\"" $2 "\""}' | tr '\n' ','
# to get a list you can loop on if doing a manual test of many resources

# smurl = 'https://www.oceanexpert.org/assets/sitemaps/sitemapExperts.xml'
# sources = "https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev-df/config/sources.yaml"
sources = "/home/fils/src/Projects/gleaner.io/scheduler/dagster/dagster-docker/src/implnet-eco/gleanerconfig.yaml"

def check_sitemap(target: str) -> int:

    # 'NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    logging.getLogger('requests').setLevel(logging.ERROR)
    logging.getLogger('advertools').setLevel(logging.ERROR)

    # f = urlopen(sources)
    f = open(sources)
    fr = f.read()
    try:
        cfg = yaml.safe_load(fr)
        # cfg = yaml.load(file, Loader=yaml.FullLoader)
        # print(cfg)
        for s in cfg["sources"]:
            if s["name"] == target:
                smurl = s["url"]
                stype = s["sourcetype"]
                # print(stype, " : ", smurl)
                if stype == "sitegraph":
                    x = requests.head(smurl)
                    # print(x.headers)
                    if x.status_code == 404:  # could check for 200 or 303?
                        print("ERROR {} : {} Sitegrap URL is 404".format(s["name"],smurl))
                        return 1 # sys.exit(os.EX_SOFTWARE)
                    else:
                        print("VALID {} : {} Sitegraph URL code is {} ".format(s["name"], smurl, x.status_code))
                        return 0 # sys.exit(os.EX_OK)
                else:
                    r = requests.get(smurl)
                    if r.status_code == 404:
                        print("ERROR {} : {} Sitemap URL is 404".format(s["name"],smurl))
                        return 1 # sys.exit(os.EX_SOFTWARE)
                    else:
                        try:
                            # adv.logs_to_df(log_file='data/sample_log.log',
                                                          # output_file='data/adv_logs.parquet',
                                                          # errors_file='data/adv_errors.txt',
                                                          # log_format='combined')
                            iow_sitemap = adv.sitemap_to_df(smurl)
                            usm = iow_sitemap.sitemap.unique()
                            uloc = iow_sitemap["loc"].unique()
                            print("VALID {} : {} has {} unique resources in {} sitemap URLs".format(s["name"],smurl, len(uloc), len(usm)))
                            return 0 # sys.exit(os.EX_OK)
                        except:
                            print("ERROR {} : {} reading sitemap XML".format(s["name"],smurl))
                            return 1
        # looped and didn't find target
        print("ERROR {} : target not found: returning 1".format(s["name"]))
        return 1
    except yaml.YAMLError as exc:
        print(exc)
        return 1 #  sys.exit(os.EX_SOFTWARE)

#
# r = check_sitemap("r2r")
# print(r)

# to test:  xdomes

names = ["balto","neotomadb","resourceregistry",
         "unidata","aquadocs","iris","edi","bcodmo","hydroshare","iedadata","opentopography",
         "unavco","ssdbiodp","linkedearth","lipdverse","ucar","opencoredata","magic","earthchem",
         "neon","designsafe","r2r","geocodes_demo_datasets","usapdc","cchdo","amgeo"]

for n in names:
    r = check_sitemap(n)
    # print(r)

