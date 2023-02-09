from dagster import schedule

from jobs.implnet_jobs_cuahsi123 import implnet_job_cuahsi123

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi123, execution_timezone="US/Central")
def implnet_sch_cuahsi123(_context):
    run_config = {}
    return run_config
