from dagster import schedule

from jobs.implnet_jobs_cuahsi109 import implnet_job_cuahsi109

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi109, execution_timezone="US/Central")
def implnet_sch_cuahsi109(_context):
    run_config = {}
    return run_config
