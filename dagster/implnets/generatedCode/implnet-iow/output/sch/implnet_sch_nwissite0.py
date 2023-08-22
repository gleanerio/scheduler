from dagster import schedule

from jobs.implnet_jobs_nwissite0 import implnet_job_nwissite0

@schedule(cron_schedule="0 4 6 * *", job=implnet_job_nwissite0, execution_timezone="US/Central")
def implnet_sch_nwissite0(_context):
    run_config = {}
    return run_config
