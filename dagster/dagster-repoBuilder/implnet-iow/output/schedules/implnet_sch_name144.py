from dagster import schedule

from jobs.implnet_jobs_name144 import implnet_job_name144

@schedule(cron_schedule="0 5 * * 0", job=implnet_job_name144, execution_timezone="US/Central")
def implnet_sch_name144(_context):
    run_config = {}
    return run_config
