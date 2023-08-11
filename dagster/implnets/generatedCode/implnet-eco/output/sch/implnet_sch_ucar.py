from dagster import schedule

from jobs.implnet_jobs_ucar import implnet_job_ucar

@schedule(cron_schedule="0 13 4 * *", job=implnet_job_ucar, execution_timezone="US/Central")
def implnet_sch_ucar(_context):
    run_config = {}
    return run_config
