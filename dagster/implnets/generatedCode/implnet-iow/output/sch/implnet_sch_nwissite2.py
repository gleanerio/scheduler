from dagster import schedule

from jobs.implnet_jobs_nwissite2 import implnet_job_nwissite2

@schedule(cron_schedule="0 8 6 * *", job=implnet_job_nwissite2, execution_timezone="US/Central")
def implnet_sch_nwissite2(_context):
    run_config = {}
    return run_config
