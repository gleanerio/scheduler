from dagster import schedule

from jobs.implnet_jobs_cuahsihisumbcgwids0 import implnet_job_cuahsihisumbcgwids0

@schedule(cron_schedule="0 18 * * 1", job=implnet_job_cuahsihisumbcgwids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisumbcgwids0(_context):
    run_config = {}
    return run_config
