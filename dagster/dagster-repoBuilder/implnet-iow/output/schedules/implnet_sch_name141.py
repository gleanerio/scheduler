from dagster import schedule

from jobs.implnet_jobs_name141 import implnet_job_name141

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_name141, execution_timezone="US/Central")
def implnet_sch_name141(_context):
    run_config = {}
    return run_config
