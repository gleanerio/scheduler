from dagster import schedule

from jobs.implnet_jobs_ipc import implnet_job_ipc

@schedule(cron_schedule="0 15 * * 4", job=implnet_job_ipc, execution_timezone="US/Central")
def implnet_sch_ipc(_context):
    run_config = {}
    return run_config
