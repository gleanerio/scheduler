from dagster import schedule

from jobs.implnet_jobs_cchdo import implnet_job_cchdo

@schedule(cron_schedule="0 10 6 * *", job=implnet_job_cchdo, execution_timezone="US/Central")
def implnet_sch_cchdo(_context):
    run_config = {}
    return run_config
