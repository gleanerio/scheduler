from dagster import schedule

from jobs.implnet_jobs_bcodmo import implnet_job_bcodmo

@schedule(cron_schedule="0 18 * * 1", job=implnet_job_bcodmo, execution_timezone="US/Central")
def implnet_sch_bcodmo(_context):
    run_config = {}
    return run_config
