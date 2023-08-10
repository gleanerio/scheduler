from dagster import schedule

from jobs.implnet_jobs_lipdverse import implnet_job_lipdverse

@schedule(cron_schedule="0 12 4 * *", job=implnet_job_lipdverse, execution_timezone="US/Central")
def implnet_sch_lipdverse(_context):
    run_config = {}
    return run_config
