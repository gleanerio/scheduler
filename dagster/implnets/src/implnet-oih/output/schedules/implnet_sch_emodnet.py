from dagster import schedule

from jobs.implnet_jobs_emodnet import implnet_job_emodnet

@schedule(cron_schedule="0 12 * * 3", job=implnet_job_emodnet, execution_timezone="US/Central")
def implnet_sch_emodnet(_context):
    run_config = {}
    return run_config
