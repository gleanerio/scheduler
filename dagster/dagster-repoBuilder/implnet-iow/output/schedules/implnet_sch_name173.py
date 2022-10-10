from dagster import schedule

from jobs.implnet_jobs_name173 import implnet_job_name173

@schedule(cron_schedule="0 11 * * 0", job=implnet_job_name173, execution_timezone="US/Central")
def implnet_sch_name173(_context):
    run_config = {}
    return run_config
