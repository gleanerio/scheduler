from dagster import schedule

from jobs.implnet_jobs_cuahsihisparalanaturalezaids0 import implnet_job_cuahsihisparalanaturalezaids0

@schedule(cron_schedule="0 20 14 * *", job=implnet_job_cuahsihisparalanaturalezaids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisparalanaturalezaids0(_context):
    run_config = {}
    return run_config
