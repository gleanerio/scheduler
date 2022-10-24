from dagster import schedule

from jobs.implnet_jobs_ssdb.iodp import implnet_job_ssdb.iodp

@schedule(cron_schedule="0 17 * * 0", job=implnet_job_ssdb.iodp, execution_timezone="US/Central")
def implnet_sch_ssdb.iodp(_context):
    run_config = {}
    return run_config
