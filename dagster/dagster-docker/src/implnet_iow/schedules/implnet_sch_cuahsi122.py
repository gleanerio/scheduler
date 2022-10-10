from dagster import schedule

from jobs.implnet_jobs_cuahsi122 import implnet_job_cuahsi122

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_cuahsi122, execution_timezone="US/Central")
def implnet_sch_cuahsi122(_context):
    run_config = {}
    return run_config
