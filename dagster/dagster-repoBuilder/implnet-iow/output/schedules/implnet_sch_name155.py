from dagster import schedule

from jobs.implnet_jobs_name155 import implnet_job_name155

@schedule(cron_schedule="0 16 * * 0", job=implnet_job_name155, execution_timezone="US/Central")
def implnet_sch_name155(_context):
    run_config = {}
    return run_config
