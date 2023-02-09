from dagster import schedule

from jobs.implnet_jobs_cuahsi173 import implnet_job_cuahsi173

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi173, execution_timezone="US/Central")
def implnet_sch_cuahsi173(_context):
    run_config = {}
    return run_config
