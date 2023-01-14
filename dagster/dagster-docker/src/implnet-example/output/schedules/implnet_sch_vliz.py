from dagster import schedule

from jobs.implnet_jobs_vliz import implnet_job_vliz

@schedule(cron_schedule="0 18 * * 6", job=implnet_job_vliz, execution_timezone="US/Central")
def implnet_sch_vliz(_context):
    run_config = {}
    return run_config
