from dagster import schedule

from jobs.implnet_jobs_cuahsihisbrazilucbids0 import implnet_job_cuahsihisbrazilucbids0

@schedule(cron_schedule="0 21 * * 6", job=implnet_job_cuahsihisbrazilucbids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisbrazilucbids0(_context):
    run_config = {}
    return run_config
