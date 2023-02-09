from dagster import schedule

from jobs.implnet_jobs_cuahsi166 import implnet_job_cuahsi166

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi166, execution_timezone="US/Central")
def implnet_sch_cuahsi166(_context):
    run_config = {}
    return run_config
