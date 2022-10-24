from dagster import schedule

from jobs.implnet_jobs_renci import implnet_job_renci

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_renci, execution_timezone="US/Central")
def implnet_sch_renci(_context):
    run_config = {}
    return run_config
