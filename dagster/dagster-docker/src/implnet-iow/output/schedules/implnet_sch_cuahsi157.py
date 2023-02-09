from dagster import schedule

from jobs.implnet_jobs_cuahsi157 import implnet_job_cuahsi157

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi157, execution_timezone="US/Central")
def implnet_sch_cuahsi157(_context):
    run_config = {}
    return run_config
