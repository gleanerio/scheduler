from dagster import schedule

from jobs.implnet_jobs_pogo import implnet_job_pogo

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_pogo, execution_timezone="US/Central")
def implnet_sch_pogo(_context):
    run_config = {}
    return run_config
