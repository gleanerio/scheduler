from dagster import schedule

from jobs.implnet_jobs_unb import implnet_job_unb

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_unb, execution_timezone="US/Central")
def implnet_sch_unb(_context):
    run_config = {}
    return run_config
