from dagster import schedule

from jobs.implnet_jobs_cuahsihismudlakeids0 import implnet_job_cuahsihismudlakeids0

@schedule(cron_schedule="0 18 * * 3", job=implnet_job_cuahsihismudlakeids0, execution_timezone="US/Central")
def implnet_sch_cuahsihismudlakeids0(_context):
    run_config = {}
    return run_config
