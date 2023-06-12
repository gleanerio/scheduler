from dagster import schedule

from jobs.implnet_jobs_nwissite3 import implnet_job_nwissite3

@schedule(cron_schedule="0 18 * * 3", job=implnet_job_nwissite3, execution_timezone="US/Central")
def implnet_sch_nwissite3(_context):
    run_config = {}
    return run_config
