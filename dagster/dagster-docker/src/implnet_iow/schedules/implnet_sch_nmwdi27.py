from dagster import schedule

from jobs.implnet_jobs_nmwdi27 import implnet_job_nmwdi27

@schedule(cron_schedule="0 3 * * 0", job=implnet_job_nmwdi27, execution_timezone="US/Central")
def implnet_sch_nmwdi27(_context):
    run_config = {}
    return run_config
