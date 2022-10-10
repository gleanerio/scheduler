from dagster import schedule

from jobs.implnet_jobs_cuahsi146 import implnet_job_cuahsi146

@schedule(cron_schedule="0 7 * * 0", job=implnet_job_cuahsi146, execution_timezone="US/Central")
def implnet_sch_cuahsi146(_context):
    run_config = {}
    return run_config
