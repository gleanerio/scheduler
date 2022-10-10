from dagster import schedule

from jobs.implnet_jobs_nmwdi23 import implnet_job_nmwdi23

@schedule(cron_schedule="0 22 * * 0", job=implnet_job_nmwdi23, execution_timezone="US/Central")
def implnet_sch_nmwdi23(_context):
    run_config = {}
    return run_config
