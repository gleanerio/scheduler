from dagster import schedule

from jobs.implnet_jobs_benguelacc import implnet_job_benguelacc

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_benguelacc, execution_timezone="US/Central")
def implnet_sch_benguelacc(_context):
    run_config = {}
    return run_config
