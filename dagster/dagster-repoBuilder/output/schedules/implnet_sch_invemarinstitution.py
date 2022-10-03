from dagster import schedule

from gleaner.jobs.implnet_jobs_invemarinstitution import implnet_job_invemarinstitution

@schedule(cron_schedule="0 5 * * 0", job=implnet_job_invemarinstitution, execution_timezone="US/Central")
def implnet_sch_invemarinstitution(_context):
    run_config = {}
    return run_config
