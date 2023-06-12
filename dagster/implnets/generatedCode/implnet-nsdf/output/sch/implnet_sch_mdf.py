from dagster import schedule

from jobs.implnet_jobs_mdf import implnet_job_mdf

@schedule(cron_schedule="0 18 * * 0", job=implnet_job_mdf, execution_timezone="US/Central")
def implnet_sch_mdf(_context):
    run_config = {}
    return run_config
