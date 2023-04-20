from dagster import schedule

from jobs.implnet_jobs_sceincespo import implnet_job_sceincespo

@schedule(cron_schedule="0 18 * * 2", job=implnet_job_sceincespo, execution_timezone="US/Central")
def implnet_sch_sceincespo(_context):
    run_config = {}
    return run_config
