from dagster import schedule

from jobs.implnet_jobs_name178 import implnet_job_name178

@schedule(cron_schedule="0 16 * * 0", job=implnet_job_name178, execution_timezone="US/Central")
def implnet_sch_name178(_context):
    run_config = {}
    return run_config
