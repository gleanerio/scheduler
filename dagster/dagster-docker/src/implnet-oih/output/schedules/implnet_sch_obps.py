from dagster import schedule

from jobs.implnet_jobs_obps import implnet_job_obps

@schedule(cron_schedule="0 18 * * 5", job=implnet_job_obps, execution_timezone="US/Central")
def implnet_sch_obps(_context):
    run_config = {}
    return run_config
