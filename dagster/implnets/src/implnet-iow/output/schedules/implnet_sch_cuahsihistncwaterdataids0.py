from dagster import schedule

from jobs.implnet_jobs_cuahsihistncwaterdataids0 import implnet_job_cuahsihistncwaterdataids0

@schedule(cron_schedule="0 3 * * 5", job=implnet_job_cuahsihistncwaterdataids0, execution_timezone="US/Central")
def implnet_sch_cuahsihistncwaterdataids0(_context):
    run_config = {}
    return run_config
