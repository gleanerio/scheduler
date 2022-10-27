from dagster import schedule

from jobs.implnet_jobs_linkedearth import implnet_job_linkedearth

@schedule(cron_schedule="0 13 * * 3", job=implnet_job_linkedearth, execution_timezone="US/Central")
def implnet_sch_linkedearth(_context):
    run_config = {}
    return run_config
