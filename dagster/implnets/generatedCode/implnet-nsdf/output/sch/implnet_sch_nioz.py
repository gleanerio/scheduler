from dagster import schedule

from jobs.implnet_jobs_nioz import implnet_job_nioz

@schedule(cron_schedule="0 15 * * 5", job=implnet_job_nioz, execution_timezone="US/Central")
def implnet_sch_nioz(_context):
    run_config = {}
    return run_config
