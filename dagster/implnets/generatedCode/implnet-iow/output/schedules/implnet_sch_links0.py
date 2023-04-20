from dagster import schedule

from jobs.implnet_jobs_links0 import implnet_job_links0

@schedule(cron_schedule="0 18 * * 5", job=implnet_job_links0, execution_timezone="US/Central")
def implnet_sch_links0(_context):
    run_config = {}
    return run_config
