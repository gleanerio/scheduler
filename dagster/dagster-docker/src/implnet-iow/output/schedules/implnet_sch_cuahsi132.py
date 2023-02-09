from dagster import schedule

from jobs.implnet_jobs_cuahsi132 import implnet_job_cuahsi132

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi132, execution_timezone="US/Central")
def implnet_sch_cuahsi132(_context):
    run_config = {}
    return run_config
