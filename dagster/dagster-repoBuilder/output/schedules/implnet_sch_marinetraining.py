from dagster import schedule

from gleaner.jobs.implnet_jobs_marinetraining import implnet_job_marinetraining

@schedule(cron_schedule="0 9 * * 0", job=implnet_job_marinetraining, execution_timezone="US/Central")
def implnet_sch_marinetraining(_context):
    run_config = {}
    return run_config
