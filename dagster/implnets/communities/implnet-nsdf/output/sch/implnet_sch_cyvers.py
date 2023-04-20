from dagster import schedule

from jobs.implnet_jobs_cyvers import implnet_job_cyvers

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_cyvers, execution_timezone="US/Central")
def implnet_sch_cyvers(_context):
    run_config = {}
    return run_config
