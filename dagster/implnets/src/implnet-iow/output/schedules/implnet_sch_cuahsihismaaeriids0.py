from dagster import schedule

from jobs.implnet_jobs_cuahsihismaaeriids0 import implnet_job_cuahsihismaaeriids0

@schedule(cron_schedule="0 18 * * 2", job=implnet_job_cuahsihismaaeriids0, execution_timezone="US/Central")
def implnet_sch_cuahsihismaaeriids0(_context):
    run_config = {}
    return run_config
