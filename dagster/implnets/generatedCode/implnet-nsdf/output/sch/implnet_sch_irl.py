from dagster import schedule

from jobs.implnet_jobs_irl import implnet_job_irl

@schedule(cron_schedule="0 12 * * 4", job=implnet_job_irl, execution_timezone="US/Central")
def implnet_sch_irl(_context):
    run_config = {}
    return run_config
