from dagster import schedule

from jobs.implnet_jobs_caribbeanmarineatlas import implnet_job_caribbeanmarineatlas

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_caribbeanmarineatlas, execution_timezone="US/Central")
def implnet_sch_caribbeanmarineatlas(_context):
    run_config = {}
    return run_config
