from dagster import schedule

from jobs.implnet_jobs_opentopography import implnet_job_opentopography

@schedule(cron_schedule="0 0 6 * *", job=implnet_job_opentopography, execution_timezone="US/Central")
def implnet_sch_opentopography(_context):
    run_config = {}
    return run_config
