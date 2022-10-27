from dagster import schedule

from jobs.implnet_jobs_decade import implnet_job_decade

@schedule(cron_schedule="0 10 * * 0", job=implnet_job_decade, execution_timezone="US/Central")
def implnet_sch_decade(_context):
    run_config = {}
    return run_config
