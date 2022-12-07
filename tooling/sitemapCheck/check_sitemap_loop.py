import advertools as adv
import requests, sys, os
import yaml, yaql
from urllib.request import urlopen
import urllib.request
import logging

# Usage:
# python check_sitemap_loop.py ~/src/Projects/gleaner.io/scheduler/dagster/dagster-docker/src/implnet-oih/gleanerconfig.yaml

#  Shout out to OpenAI and ChatGPT (https://chat.openai.com/chat) for some fun pair programming :)
#  I for one welcome our new AI overlords and can be useful idiot in your plans for world conquest....

# this script has an annoying stderr from advertools, run with
# python check_sitemap_loop.py  2> /dev/null
# to route stderr to dev/null if that works better for you

# sources = "https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev-df/config/sources.yaml"
# sources = "/home/fils/src/Projects/gleaner.io/scheduler/dagster/dagster-docker/src/implnet-eco/gleanerconfig.yaml"
#sources = "/home/fils/src/Projects/gleaner.io/scheduler/dagster/dagster-docker/src/implnet-oih/gleanerconfig.yaml"

def check_sitemap(sources, target: str) -> int:

    # 'NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    logging.getLogger('requests').setLevel(logging.ERROR)
    logging.getLogger('advertools').setLevel(logging.ERROR)

    if "://" in sources:
        f = urlopen(sources)
    else:
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
                    try:
                        r = requests.get(smurl)
                    except:
                        print("ERROR making request, no further help at this time")
                        return 1
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


def main():
    # Read the command line arguments
    args = sys.argv[1:]
    sources = args[0]
    data_source = None

    if "://" in sources:
        # If the input is a URL, open it using urllib
        f = urlopen(sources)
        data_source = yaml.safe_load(f.read())
    else:
        # If the input is a file, open it
        data_source = yaml.safe_load(open(sources, 'r'))


    engine = yaql.factory.YaqlFactory().create()
    expression = engine( '$.sources.name')
    order = expression.evaluate(data=data_source)

    print(order)

    for n in order:
        r = check_sitemap(sources, n)
        print(r)

if __name__ == '__main__':
    main()

