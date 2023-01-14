from dagster import schedule

from jobs.implnet_jobs_obis import implnet_job_obis

@schedule(cron_schedule="0 12 * * 5", job=implnet_job_obis, execution_timezone="US/Central")
def implnet_sch_obis(_context):
    run_config = {}
    return run_config
