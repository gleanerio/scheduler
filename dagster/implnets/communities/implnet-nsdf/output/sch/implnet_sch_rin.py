from dagster import schedule

from jobs.implnet_jobs_rin import implnet_job_rin

@schedule(cron_schedule="0 6 * * 5", job=implnet_job_rin, execution_timezone="US/Central")
def implnet_sch_rin(_context):
    run_config = {}
    return run_config
