from dagster import Definitions, load_assets_from_modules

from . import assets
from .sch import weekly_sch


all_assets = load_assets_from_modules([assets])
weekly_data_schedule=[ weekly_sch.loadstats_schedule, weekly_sch.all_graph_stats_schedule]

defs = Definitions(
    assets=all_assets,
    schedules=weekly_data_schedule,
)
