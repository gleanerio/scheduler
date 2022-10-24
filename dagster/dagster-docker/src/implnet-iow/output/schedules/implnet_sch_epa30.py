from dagster import schedule

from jobs.implnet_jobs_epa30 import implnet_job_epa30

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_epa30, execution_timezone="US/Central")
def implnet_sch_epa30(_context):
    run_config = {}
    return run_config
