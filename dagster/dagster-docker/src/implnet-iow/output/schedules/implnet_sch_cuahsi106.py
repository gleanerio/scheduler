from dagster import schedule

from jobs.implnet_jobs_cuahsi106 import implnet_job_cuahsi106

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi106, execution_timezone="US/Central")
def implnet_sch_cuahsi106(_context):
    run_config = {}
    return run_config
