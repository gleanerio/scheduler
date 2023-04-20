from dagster import schedule

from jobs.implnet_jobs_tdi import implnet_job_tdi

@schedule(cron_schedule="0 9 * * 2", job=implnet_job_tdi, execution_timezone="US/Central")
def implnet_sch_tdi(_context):
    run_config = {}
    return run_config
