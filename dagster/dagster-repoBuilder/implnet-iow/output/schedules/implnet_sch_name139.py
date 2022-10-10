from dagster import schedule

from jobs.implnet_jobs_name139 import implnet_job_name139

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_name139, execution_timezone="US/Central")
def implnet_sch_name139(_context):
    run_config = {}
    return run_config
