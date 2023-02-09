from dagster import schedule

from jobs.implnet_jobs_cuahsi163 import implnet_job_cuahsi163

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi163, execution_timezone="US/Central")
def implnet_sch_cuahsi163(_context):
    run_config = {}
    return run_config
