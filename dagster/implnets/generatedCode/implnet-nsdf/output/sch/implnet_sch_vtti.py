from dagster import schedule

from jobs.implnet_jobs_vtti import implnet_job_vtti

@schedule(cron_schedule="0 18 * * 0", job=implnet_job_vtti, execution_timezone="US/Central")
def implnet_sch_vtti(_context):
    run_config = {}
    return run_config
