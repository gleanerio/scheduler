from dagster import schedule

from jobs.implnet_jobs_datadiscoverystudio import implnet_job_datadiscoverystudio

@schedule(cron_schedule="0 6 * * 1", job=implnet_job_datadiscoverystudio, execution_timezone="US/Central")
def implnet_sch_datadiscoverystudio(_context):
    run_config = {}
    return run_config
