from dagster import schedule

from jobs.implnet_jobs_cuahsihisredbuttecreekgamutids0 import implnet_job_cuahsihisredbuttecreekgamutids0

@schedule(cron_schedule="0 4 18 * *", job=implnet_job_cuahsihisredbuttecreekgamutids0, execution_timezone="US/Central")
def implnet_sch_cuahsihisredbuttecreekgamutids0(_context):
    run_config = {}
    return run_config
