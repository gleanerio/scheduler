from dagster import schedule

from jobs.implnet_jobs_cuahsihisodmkentstateids0 import implnet_job_cuahsihisodmkentstateids0

@schedule(cron_schedule="0 4 10 * *", job=implnet_job_cuahsihisodmkentstateids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisodmkentstateids0(_context):
    run_config = {}
    return run_config
