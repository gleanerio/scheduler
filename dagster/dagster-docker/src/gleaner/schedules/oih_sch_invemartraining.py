from dagster import schedule

from gleaner.jobs.oih_jobs_invemartraining import oih_job_invemartraining

@schedule(cron_schedule="30 19 * * *", job=oih_job_invemartraining, execution_timezone="US/Central")
def oih_sch_invemartraining(_context):
    run_config = {}
    return run_config
