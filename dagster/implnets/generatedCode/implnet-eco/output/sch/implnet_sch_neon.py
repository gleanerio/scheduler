from dagster import schedule

from jobs.implnet_jobs_neon import implnet_job_neon

@schedule(cron_schedule="0 0 6 * *", job=implnet_job_neon, execution_timezone="US/Central")
def implnet_sch_neon(_context):
    run_config = {}
    return run_config
