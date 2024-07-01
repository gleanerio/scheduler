import distutils
import json
import os
from typing import List, Any
import pandas as pd
from dagster import asset, get_dagster_logger, define_asset_job
from ec.datastore import s3
from pydash import pick
from distutils import util

GLEANER_MINIO_ADDRESS = os.environ.get('GLEANERIO_MINIO_ADDRESS')
GLEANER_MINIO_PORT = os.environ.get('GLEANERIO_MINIO_PORT')
GLEANER_MINIO_USE_SSL = bool(util.strtobool(os.environ.get('GLEANERIO_MINIO_USE_SSL', 'true')))
GLEANER_MINIO_SECRET_KEY = os.environ.get('GLEANERIO_MINIO_SECRET_KEY')
GLEANER_MINIO_ACCESS_KEY = os.environ.get('GLEANERIO_MINIO_ACCESS_KEY')
GLEANER_MINIO_BUCKET = os.environ.get('GLEANERIO_MINIO_BUCKET')
# set for the earhtcube utiltiies
MINIO_OPTIONS={"secure":GLEANER_MINIO_USE_SSL

              ,"access_key": GLEANER_MINIO_ACCESS_KEY
              ,"secret_key": GLEANER_MINIO_SECRET_KEY
               }
REPORT_PATH = "reports/"
TASKS_PATH="tasks/"
ORG_PATH = "orgs/"
STAT_FILE_NAME = "missing_report_graph.json"
def _pythonMinioUrl(url):

    if (url.endswith(".amazonaws.com")):
        PYTHON_MINIO_URL = "s3.amazonaws.com"
    else:
        PYTHON_MINIO_URL = url
    return PYTHON_MINIO_URL

def getName(name):
    return name.replace("orgs/","").replace(".nq","")
@asset(group_name="load",key_prefix="task",)
def source_list() -> List[Any]:
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), MINIO_OPTIONS)
    orglist = s3Minio.listPath(GLEANER_MINIO_BUCKET, ORG_PATH,recursive=False)
    sources = map( lambda f: { "name": getName(f.object_name)}, orglist )
    sources=list(sources)
    source_json = json.dumps(sources)
    os.makedirs("data", exist_ok=True)

    s3Minio.putReportFile(GLEANER_MINIO_BUCKET, "all", f"source_list.json", source_json )
    # with open("data/source_list.json", "w") as f:
    #     json.dump(list(sources), f)
    return sources
#@asset(deps=[source_list])

# set a prefix so we can have some named stats file

#@asset( group_name="load",key_prefix="task",)
@asset(group_name="load",key_prefix="task",)
def loadstatsHistory(context,source_list) -> str:
    prefix="history"
    logger = get_dagster_logger()
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS),MINIO_OPTIONS)
 #   sourcelist = list(s3Minio.listPath(GLEANER_MINIO_BUCKET, ORG_PATH,recursive=False))

    # with open("data/source_list.json","r" ) as f:
    #     sourcelist = json.load(f)
    sourcelist=source_list
    stats = []
    for source in sourcelist:
        try:
           # stat = s3Minio.getReportFile(GLEANER_MINIO_BUCKET,source.get("name"), STAT_FILE_NAME )
           repo = source.get("name")
           dirs = s3Minio.listPath( GLEANER_MINIO_BUCKET,f"{REPORT_PATH}{repo}/",recursive=False )
           for d in dirs:
               latestpath = f"{REPORT_PATH}{repo}/latest/"
               if (d.object_name.casefold() == latestpath.casefold()) or (d.is_dir == False):
                   continue
               path = f"/{d.object_name}{STAT_FILE_NAME}"
               s3ObjectInfo = {"bucket_name": GLEANER_MINIO_BUCKET, "object_name": path}
               try:
                   resp = s3Minio.getFileFromStore(s3ObjectInfo)
                   stat = json.loads(resp)
                   stat = pick(stat, 'source', 'sitemap', 'date', 'sitemap_count', 'summoned_count',
                               'missing_sitemap_summon_count',
                               'graph_urn_count', 'missing_summon_graph_count')
                   stats.append(stat)
               except Exception as ex:
                   logger.info(f"no missing graph report {source.get('name')}  {ex}")
        except Exception as ex:
            logger.info(f"Failed to get { source.get('name')}  {ex}")
    df = pd.DataFrame(stats)
    df.to_csv(f"data/all_stats.csv")
    df_csv = df.to_csv()
    s3Minio.putReportFile(GLEANER_MINIO_BUCKET, "all", f"all_stats.csv", df_csv)
    get_dagster_logger().info(f"all_stats.csv uploaded ")
    #return df_csv
    return df_csv


