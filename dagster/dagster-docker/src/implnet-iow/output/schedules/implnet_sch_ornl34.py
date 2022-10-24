from dagster import schedule

from jobs.implnet_jobs_ornl34 import implnet_job_ornl34

@schedule(cron_schedule="0 10 * * 0", job=implnet_job_ornl34, execution_timezone="US/Central")
def implnet_sch_ornl34(_context):
    run_config = {}
    return run_config
