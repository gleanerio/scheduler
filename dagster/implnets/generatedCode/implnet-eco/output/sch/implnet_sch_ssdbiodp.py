from dagster import schedule

from jobs.implnet_jobs_ssdbiodp import implnet_job_ssdbiodp

@schedule(cron_schedule="0 18 6 * *", job=implnet_job_ssdbiodp, execution_timezone="US/Central")
def implnet_sch_ssdbiodp(_context):
    run_config = {}
    return run_config
