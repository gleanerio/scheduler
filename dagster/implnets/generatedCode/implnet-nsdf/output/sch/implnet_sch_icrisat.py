from dagster import schedule

from jobs.implnet_jobs_icrisat import implnet_job_icrisat

@schedule(cron_schedule="0 0 * * 4", job=implnet_job_icrisat, execution_timezone="US/Central")
def implnet_sch_icrisat(_context):
    run_config = {}
    return run_config
