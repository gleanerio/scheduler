from dagster import schedule

from jobs.implnet_jobs_name51 import implnet_job_name51

@schedule(cron_schedule="0 4 * * 0", job=implnet_job_name51, execution_timezone="US/Central")
def implnet_sch_name51(_context):
    run_config = {}
    return run_config
