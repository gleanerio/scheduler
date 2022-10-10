from dagster import schedule

from jobs.implnet_jobs_name117 import implnet_job_name117

@schedule(cron_schedule="0 1 * * 0", job=implnet_job_name117, execution_timezone="US/Central")
def implnet_sch_name117(_context):
    run_config = {}
    return run_config
