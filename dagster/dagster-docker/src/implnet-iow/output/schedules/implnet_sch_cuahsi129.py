from dagster import schedule

from jobs.implnet_jobs_cuahsi129 import implnet_job_cuahsi129

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi129, execution_timezone="US/Central")
def implnet_sch_cuahsi129(_context):
    run_config = {}
    return run_config
