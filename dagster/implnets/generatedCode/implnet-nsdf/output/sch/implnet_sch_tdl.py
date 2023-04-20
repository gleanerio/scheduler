from dagster import schedule

from jobs.implnet_jobs_tdl import implnet_job_tdl

@schedule(cron_schedule="0 21 * * 6", job=implnet_job_tdl, execution_timezone="US/Central")
def implnet_sch_tdl(_context):
    run_config = {}
    return run_config
