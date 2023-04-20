from dagster import schedule

from jobs.implnet_jobs_ifsttar import implnet_job_ifsttar

@schedule(cron_schedule="0 6 * * 4", job=implnet_job_ifsttar, execution_timezone="US/Central")
def implnet_sch_ifsttar(_context):
    run_config = {}
    return run_config
