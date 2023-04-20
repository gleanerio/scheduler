from dagster import schedule

from jobs.implnet_jobs_chile import implnet_job_chile

@schedule(cron_schedule="0 9 * * 6", job=implnet_job_chile, execution_timezone="US/Central")
def implnet_sch_chile(_context):
    run_config = {}
    return run_config
