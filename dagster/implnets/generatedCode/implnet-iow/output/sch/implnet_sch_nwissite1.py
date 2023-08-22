from dagster import schedule

from jobs.implnet_jobs_nwissite1 import implnet_job_nwissite1

@schedule(cron_schedule="0 20 5 * *", job=implnet_job_nwissite1, execution_timezone="US/Central")
def implnet_sch_nwissite1(_context):
    run_config = {}
    return run_config
