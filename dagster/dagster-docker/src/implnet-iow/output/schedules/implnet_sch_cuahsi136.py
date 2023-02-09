from dagster import schedule

from jobs.implnet_jobs_cuahsi136 import implnet_job_cuahsi136

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi136, execution_timezone="US/Central")
def implnet_sch_cuahsi136(_context):
    run_config = {}
    return run_config
