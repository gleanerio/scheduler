from dagster import schedule

from jobs.implnet_jobs_edmo import implnet_job_edmo

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_edmo, execution_timezone="US/Central")
def implnet_sch_edmo(_context):
    run_config = {}
    return run_config
