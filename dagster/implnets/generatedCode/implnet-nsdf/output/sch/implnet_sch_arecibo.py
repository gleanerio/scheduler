from dagster import schedule

from jobs.implnet_jobs_arecibo import implnet_job_arecibo

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_arecibo, execution_timezone="US/Central")
def implnet_sch_arecibo(_context):
    run_config = {}
    return run_config
