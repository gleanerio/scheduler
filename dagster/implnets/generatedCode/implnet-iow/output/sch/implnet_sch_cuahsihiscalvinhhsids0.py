from dagster import schedule

from jobs.implnet_jobs_cuahsihiscalvinhhsids0 import implnet_job_cuahsihiscalvinhhsids0

@schedule(cron_schedule="0 20 18 * *", job=implnet_job_cuahsihiscalvinhhsids0, execution_timezone="US/Central")
def implnet_sch_cuahsihiscalvinhhsids0(_context):
    run_config = {}
    return run_config
