from dagster import schedule

from jobs.implnet_jobs_name97 import implnet_job_name97

@schedule(cron_schedule="0 4 * * 0", job=implnet_job_name97, execution_timezone="US/Central")
def implnet_sch_name97(_context):
    run_config = {}
    return run_config
