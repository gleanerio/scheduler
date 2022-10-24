from dagster import schedule

from jobs.implnet_jobs_bco-dmo import implnet_job_bco-dmo

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_bco-dmo, execution_timezone="US/Central")
def implnet_sch_bco-dmo(_context):
    run_config = {}
    return run_config
