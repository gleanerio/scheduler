from dagster import schedule

from jobs.implnet_jobs_c4rsois import implnet_job_c4rsois

@schedule(cron_schedule="0 4 * * 0", job=implnet_job_c4rsois, execution_timezone="US/Central")
def implnet_sch_c4rsois(_context):
    run_config = {}
    return run_config
