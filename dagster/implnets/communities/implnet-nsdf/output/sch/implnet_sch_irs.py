from dagster import schedule

from jobs.implnet_jobs_irs import implnet_job_irs

@schedule(cron_schedule="0 15 * * 2", job=implnet_job_irs, execution_timezone="US/Central")
def implnet_sch_irs(_context):
    run_config = {}
    return run_config
