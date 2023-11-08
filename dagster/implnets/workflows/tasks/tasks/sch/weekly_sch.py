from dagster import schedule, RunRequest,  ScheduleEvaluationContext, define_asset_job, AssetSelection



load_analytics_job= define_asset_job("load_analytics_job", selection=AssetSelection.groups("load"))
graph_analytics_job= define_asset_job("graph_analytics_job", selection=AssetSelection.groups("graph"))
@schedule(job=load_analytics_job, cron_schedule="@weekly")
def loadstats_schedule(context:  ScheduleEvaluationContext):

    return RunRequest(
        run_key=None,
        run_config={}

    )

@schedule(job=graph_analytics_job, cron_schedule="@weekly")
def all_graph_stats_schedule(context:  ScheduleEvaluationContext):

    return RunRequest(
        run_key=None,
        run_config={}

    )
