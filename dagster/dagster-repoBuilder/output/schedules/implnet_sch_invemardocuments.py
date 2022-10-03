from dagster import schedule

from gleaner.jobs.implnet_jobs_invemardocuments import implnet_job_invemardocuments

@schedule(cron_schedule="0 4 * * 0", job=implnet_job_invemardocuments, execution_timezone="US/Central")
def implnet_sch_invemardocuments(_context):
    run_config = {}
    return run_config
