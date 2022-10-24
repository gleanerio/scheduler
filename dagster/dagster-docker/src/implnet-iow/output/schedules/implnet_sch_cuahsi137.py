from dagster import schedule

from jobs.implnet_jobs_cuahsi137 import implnet_job_cuahsi137

@schedule(cron_schedule="0 21 * * 0", job=implnet_job_cuahsi137, execution_timezone="US/Central")
def implnet_sch_cuahsi137(_context):
    run_config = {}
    return run_config
