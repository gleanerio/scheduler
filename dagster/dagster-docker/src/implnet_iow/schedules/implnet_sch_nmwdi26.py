from dagster import schedule

from jobs.implnet_jobs_nmwdi26 import implnet_job_nmwdi26

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_nmwdi26, execution_timezone="US/Central")
def implnet_sch_nmwdi26(_context):
    run_config = {}
    return run_config
