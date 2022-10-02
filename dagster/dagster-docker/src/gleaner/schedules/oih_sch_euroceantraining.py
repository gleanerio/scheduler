from dagster import schedule

from gleaner.jobs.oih_jobs_euroceantraining import oih_job_euroceantraining

@schedule(cron_schedule="0 23 * * *", job=oih_job_euroceantraining, execution_timezone="US/Central")
def oih_sch_euroceantraining(_context):
    run_config = {}
    return run_config
