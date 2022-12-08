from dagster import schedule

from jobs.implnet_jobs_invemarvessels import implnet_job_invemarvessels

@schedule(cron_schedule="0 18 * * 4", job=implnet_job_invemarvessels, execution_timezone="US/Central")
def implnet_sch_invemarvessels(_context):
    run_config = {}
    return run_config
