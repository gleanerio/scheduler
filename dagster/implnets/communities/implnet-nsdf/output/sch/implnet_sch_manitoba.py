from dagster import schedule

from jobs.implnet_jobs_manitoba import implnet_job_manitoba

@schedule(cron_schedule="0 9 * * 0", job=implnet_job_manitoba, execution_timezone="US/Central")
def implnet_sch_manitoba(_context):
    run_config = {}
    return run_config
