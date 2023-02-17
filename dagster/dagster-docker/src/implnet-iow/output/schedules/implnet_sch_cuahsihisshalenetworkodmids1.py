from dagster import schedule

from jobs.implnet_jobs_cuahsihisshalenetworkodmids1 import implnet_job_cuahsihisshalenetworkodmids1

@schedule(cron_schedule="0 3 * * 5", job=implnet_job_cuahsihisshalenetworkodmids1, execution_timezone="US/Central")
def implnet_sch_cuahsihisshalenetworkodmids1(_context):
    run_config = {}
    return run_config
