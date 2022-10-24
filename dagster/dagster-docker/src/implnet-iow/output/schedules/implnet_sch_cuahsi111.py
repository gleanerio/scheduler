from dagster import schedule

from jobs.implnet_jobs_cuahsi111 import implnet_job_cuahsi111

@schedule(cron_schedule="0 18 * * 0", job=implnet_job_cuahsi111, execution_timezone="US/Central")
def implnet_sch_cuahsi111(_context):
    run_config = {}
    return run_config
