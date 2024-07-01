from dagster import (
    op, job, Config,asset,
    In, Nothing,
    sensor, RunRequest, RunConfig,
    SensorEvaluationContext, asset_sensor, EventLogEntry,
    SkipReason,
    AssetKey,
    static_partitioned_config, dynamic_partitioned_config, DynamicPartitionsDefinition,
    define_asset_job, AssetSelection,graph_asset,
    get_dagster_logger
)

from dagster_aws.s3.sensor import get_s3_keys
from typing import List, Dict
from pydantic import Field
import pydash

#from pydash.collections import find
#from pydash.predicates import is_match
from ec.graph.manageGraph import ManageBlazegraph
from ..assets import gleanerio_tenants, tenant_partitions_def, sources_partitions_def
from .gleaner_summon_assets import RELEASE_PATH, SUMMARY_PATH

class TenantConfig(Config):
    source_name: str
    name: str
    source_list: List[str]
    TENANT_GRAPH_NAMESPACE: str
    TENANT_GRAPH_SUMMARY_NAMESPACE: str
    SUMMARY_PATH: str =  Field(
         description="GLEANERIO_GRAPH_SUMMARY_PATH.", default='graphs/summary')
    RELEASE_PATH : str =  Field(
         description="GLEANERIO_GRAPH_RELEASE_PATH.", default='graphs/latest')


class TenantOpConfig(Config):
    source_name: str

def find_tenants_with_source(source_name, tenats_all):
    get_dagster_logger().info(f" find tenant  {source_name} with {tenats_all}")
    tenants =[]
    # tenants = pydash.collections.find(tenats_all,
    #            lambda t: p    ydash.predicates.is_match(t["sources"], source_name) or pydash.predicates.is_match(t["sources"], 'all')
    #                                   )
    #tenants = pydash.collections.find(tenats_all,  lambda t: pydash.predicates.is_match(t["sources"], "all") )
    for tenant in tenats_all:
        get_dagster_logger().info(f"  tenant sources {tenant['sources']}")
        if source_name in tenant["sources"]:
            get_dagster_logger().info(f" found source  {source_name} in {tenant['community']}")
            tenants.append(tenant)
        if 'all' in tenant["sources"]:
            get_dagster_logger().info(f" found source  all in {tenant['community']}")
            tenants.append(tenant)
    return tenants
@asset(
    group_name="tenant_load",key_prefix="ingest",
    deps=[AssetKey(["ingest","tenant_names"]), AssetKey(["ingest","tenant_all"])],
    required_resource_keys={"gleanerio",},partitions_def=sources_partitions_def)
#def upload_release(context, config:TennantOpConfig  ):
def upload_release(context ):
    #context.log.info(config.source_name)
    tenants_all = context.repository_def.load_asset_value(AssetKey(["ingest","tenant_all"]))['tenant']
    source_name = context.asset_partition_key_for_output()

    context.log.info(f"source_name {source_name}")
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
    tenants = find_tenants_with_source(source_name, tenants_all)
    for tenant in tenants:
        #tenant["graph"]['main_namespace']
        #bg = ManageBlazegraph(triplestore.GLEANERIO_GRAPH_URL, tenant["graph"]['main_namespace'])
        try:
            #bg.upload_nq_file()
            namespace = tenant['graph']['main_namespace']
            endpoint =  triplestore.GraphEndpoint(namespace)
            triplestore.post_to_graph(source_name, path=RELEASE_PATH, extension="nq", graphendpoint=endpoint)
            context.log.info(f"load  release for {source_name} to tennant  {tenant['community']}  {triplestore.GLEANERIO_GRAPH_URL} ")
        except Exception as ex:
            context.log.info(f"load to tennant {source_name} failed {ex}")
            raise Exception(f"load to tennant {source_name} failed {ex}")
        return

#@asset(required_resource_keys={"gleanerio",},ins={"start": In(Nothing)})
@asset(group_name="tenant_load",key_prefix="ingest",
       deps=[AssetKey(["ingest","tenant_names"]), AssetKey(["ingest","tenant_all"])],
       required_resource_keys={"gleanerio",},partitions_def=sources_partitions_def)
#def upload_summary(context, config:TennantOpConfig):
def upload_summary(context):
    #context.log.info(config.source_name)
    source_name = context.asset_partition_key_for_output()
    context.log.info(f"tennant_name {source_name} ")
    tenants_all = context.repository_def.load_asset_value(AssetKey(["ingest","tenant_all"]))['tenant']

    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
    tenants = find_tenants_with_source(source_name, tenants_all)
    for tenant in tenants:
       # bg = ManageBlazegraph(triplestore.GLEANERIO_GRAPH_URL,  tenant["graph"]['summary_namespace'])
        try:
           # bg.upload_nq_file()
            namespace = tenant['graph']['summary_namespace']
            endpoint = triplestore.GraphEndpoint(namespace)
            triplestore.post_to_graph(source_name, path=SUMMARY_PATH,extension="ttl", graphendpoint=endpoint)
            context.log.info(f"load summary for {source_name} to tennant  {tenant['community']}   {triplestore.GLEANERIO_GRAPH_URL}")
        except Exception as ex:
            context.log.error(f"load to tennant failed {source_name}  {triplestore.GLEANERIO_GRAPH_URL} {ex}")
            raise Exception(f"load to tennant failed {source_name}  {triplestore.GLEANERIO_GRAPH_URL}  {ex}")
        return
#
# @asset(group_name="tenant_create",required_resource_keys={"gleanerio",},partitions_def=tenant_partitions_def)
# def create_graph_namespaces(context):
#     #context.log.info(config.source_name)
#     source_name = context.asset_partition_key_for_output()
#     context.log.info(f"tennant_name {source_name}")
#     gleaner_resource = context.resources.gleanerio
#     s3_resource = context.resources.gleanerio.gs3.s3
#     gleaner_s3 = context.resources.gleanerio.gs3
#     triplestore = context.resources.gleanerio.triplestore
#     pass
@asset(group_name="tenant_create",key_prefix="ingest",
       deps=[AssetKey(["ingest","tenant_all"])],
       required_resource_keys={"gleanerio",},partitions_def=tenant_partitions_def)
def create_graph_namespaces(context):
    #context.log.info(config.source_name)
    tenant_name = context.asset_partition_key_for_output()
    context.log.info(f"tennant_name {tenant_name}")
    tenants = context.repository_def.load_asset_value(AssetKey(["ingest","tenant_all"]))
    # from https://stackoverflow.com/questions/2361426/get-the-first-item-from-an-iterable-that-matches-a-condition
    tenant = next((t for t in tenants["tenant"] if t['community'] == tenant_name ),None)
    if tenant is None:
        raise Exception("Tenant with name {} does not exist".format(tenant_name))
    context.log.info(f"tennant {tenant}")
    # should we put a default.
    main_namespace = tenant["graph"]["main_namespace"]
    summary_namespace = tenant["graph"]["summary_namespace"]
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
    bg = ManageBlazegraph(triplestore.GLEANERIO_GRAPH_URL, main_namespace )
    bg_summary = ManageBlazegraph(triplestore.GLEANERIO_GRAPH_URL, summary_namespace)
    try:
        msg = bg.createNamespace(quads=True)
        context.log.info(f"graph creation  {tenant_name} {triplestore.GLEANERIO_GRAPH_URL} {msg}")
        msg = bg_summary.createNamespace(quads=False)
        context.log.info(f"graph creation  {tenant_name} {triplestore.GLEANERIO_GRAPH_URL} {msg}")
    except Exception as ex :
        context.log.error(f"graph creation failed {tenant_name} {triplestore.GLEANERIO_GRAPH_URL} {ex}")
        raise Exception(f"graph creation failed {tenant_name} {triplestore.GLEANERIO_GRAPH_URL} {ex}")
    return

@asset(group_name="tenant_create",key_prefix="ingest",
       deps=[AssetKey(["ingest","tenant_all"]), AssetKey(["ingest","create_graph_namespaces"])],
       required_resource_keys={"gleanerio",},partitions_def=tenant_partitions_def)
def create_tenant_containers(context):
    #context.log.info(config.source_name)
    tenant_name = context.asset_partition_key_for_output()
    tenants = context.repository_def.load_asset_value(AssetKey(["ingest","tenant_all"]))
    context.log.info(f"tennant_name {tenant_name}")
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
    pass
#@static_partitioned_config(partition_keys=TENNANT_NAMES)

    #return {"ops": {"continent_op": {"config": {"continent_name": partition_key}}}}
#@job(config=tennant_config, partitions_def=tenant_partitions_def)
# @job( partitions_def=tenant_partitions_def)
# def build_community():
#     source_name = context.asset_partition_key_for_output()
#     context.log.info(f"tennant_name {source_name}")
#     upload_summary(upload_release())
