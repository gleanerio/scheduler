from dagster import schedule

from jobs.implnet_jobs_cuahsi177 import implnet_job_cuahsi177

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi177, execution_timezone="US/Central")
def implnet_sch_cuahsi177(_context):
    run_config = {}
    return run_config
