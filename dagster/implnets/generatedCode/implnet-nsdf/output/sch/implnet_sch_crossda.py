from dagster import schedule

from jobs.implnet_jobs_crossda import implnet_job_crossda

@schedule(cron_schedule="0 3 * * 2", job=implnet_job_crossda, execution_timezone="US/Central")
def implnet_sch_crossda(_context):
    run_config = {}
    return run_config
