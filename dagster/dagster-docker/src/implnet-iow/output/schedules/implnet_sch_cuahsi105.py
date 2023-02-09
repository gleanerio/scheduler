from dagster import schedule

from jobs.implnet_jobs_cuahsi105 import implnet_job_cuahsi105

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi105, execution_timezone="US/Central")
def implnet_sch_cuahsi105(_context):
    run_config = {}
    return run_config
