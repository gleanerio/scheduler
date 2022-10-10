from dagster import schedule

from jobs.implnet_jobs_name161 import implnet_job_name161

@schedule(cron_schedule="0 22 * * 0", job=implnet_job_name161, execution_timezone="US/Central")
def implnet_sch_name161(_context):
    run_config = {}
    return run_config
