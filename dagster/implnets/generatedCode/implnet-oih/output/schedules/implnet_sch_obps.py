from dagster import schedule

from jobs.implnet_jobs_obps import implnet_job_obps

@schedule(cron_schedule="0 0 * * 6", job=implnet_job_obps, execution_timezone="US/Central")
def implnet_sch_obps(_context):
    run_config = {}
    return run_config
