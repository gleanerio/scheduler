from dagster import schedule

from jobs.implnet_jobs_darus import implnet_job_darus

@schedule(cron_schedule="0 12 * * 2", job=implnet_job_darus, execution_timezone="US/Central")
def implnet_sch_darus(_context):
    run_config = {}
    return run_config
