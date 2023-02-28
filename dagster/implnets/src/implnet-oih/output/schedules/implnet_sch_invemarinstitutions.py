from dagster import schedule

from jobs.implnet_jobs_invemarinstitutions import implnet_job_invemarinstitutions

@schedule(cron_schedule="0 12 * * 4", job=implnet_job_invemarinstitutions, execution_timezone="US/Central")
def implnet_sch_invemarinstitutions(_context):
    run_config = {}
    return run_config
