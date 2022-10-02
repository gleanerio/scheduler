from dagster import schedule

from gleaner.jobs.implnet_jobs_edmerp import implnet_job_edmerp

@schedule(cron_schedule="0 14 * * *", job=implnet_job_edmerp, execution_timezone="US/Central")
def implnet_sch_edmerp(_context):
    run_config = {}
    return run_config
