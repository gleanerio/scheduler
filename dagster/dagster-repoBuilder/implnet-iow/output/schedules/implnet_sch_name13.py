from dagster import schedule

from jobs.implnet_jobs_name13 import implnet_job_name13

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_name13, execution_timezone="US/Central")
def implnet_sch_name13(_context):
    run_config = {}
    return run_config
