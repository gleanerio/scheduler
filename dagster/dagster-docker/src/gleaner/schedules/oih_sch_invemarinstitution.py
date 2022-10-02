from dagster import schedule

from gleaner.jobs.oih_jobs_invemarinstitution import oih_job_invemarinstitution

@schedule(cron_schedule="30 18 * * *", job=oih_job_invemarinstitution, execution_timezone="US/Central")
def oih_sch_invemarinstitution(_context):
    run_config = {}
    return run_config
