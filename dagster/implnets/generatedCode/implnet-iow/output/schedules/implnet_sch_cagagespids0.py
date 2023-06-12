from dagster import schedule

from jobs.implnet_jobs_cagagespids0 import implnet_job_cagagespids0

@schedule(cron_schedule="0 3 * * 1", job=implnet_job_cagagespids0, execution_timezone="US/Central")
def implnet_sch_cagagespids0(_context):
    run_config = {}
    return run_config
