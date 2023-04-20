from dagster import schedule

from jobs.implnet_jobs_peking import implnet_job_peking

@schedule(cron_schedule="0 0 * * 6", job=implnet_job_peking, execution_timezone="US/Central")
def implnet_sch_peking(_context):
    run_config = {}
    return run_config
