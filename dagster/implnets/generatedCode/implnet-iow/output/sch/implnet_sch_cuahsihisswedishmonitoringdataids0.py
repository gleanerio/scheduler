from dagster import schedule

from jobs.implnet_jobs_cuahsihisswedishmonitoringdataids0 import implnet_job_cuahsihisswedishmonitoringdataids0

@schedule(cron_schedule="0 4 20 * *", job=implnet_job_cuahsihisswedishmonitoringdataids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisswedishmonitoringdataids0(_context):
    run_config = {}
    return run_config
