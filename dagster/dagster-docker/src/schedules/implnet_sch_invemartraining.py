from dagster import schedule

from jobs.implnet_jobs_invemartraining import implnet_job_invemartraining

@schedule(cron_schedule="0 7 * * 0", job=implnet_job_invemartraining, execution_timezone="US/Central")
def implnet_sch_invemartraining(_context):
    run_config = {}
    return run_config
