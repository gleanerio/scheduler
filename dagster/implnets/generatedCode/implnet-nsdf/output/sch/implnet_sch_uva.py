from dagster import schedule

from jobs.implnet_jobs_uva import implnet_job_uva

@schedule(cron_schedule="0 3 * * 5", job=implnet_job_uva, execution_timezone="US/Central")
def implnet_sch_uva(_context):
    run_config = {}
    return run_config
