from dagster import schedule

from jobs.implnet_jobs_maspawio import implnet_job_maspawio

@schedule(cron_schedule="0 6 * * 5", job=implnet_job_maspawio, execution_timezone="US/Central")
def implnet_sch_maspawio(_context):
    run_config = {}
    return run_config
