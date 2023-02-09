from dagster import schedule

from jobs.implnet_jobs_cuahsi117 import implnet_job_cuahsi117

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi117, execution_timezone="US/Central")
def implnet_sch_cuahsi117(_context):
    run_config = {}
    return run_config
