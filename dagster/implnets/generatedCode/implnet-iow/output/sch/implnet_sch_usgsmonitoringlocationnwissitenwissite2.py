from dagster import schedule, DefaultScheduleStatus

from jobs.implnet_jobs_usgsmonitoringlocationnwissitenwissite2 import implnet_job_usgsmonitoringlocationnwissitenwissite2

@schedule(cron_schedule="0 10 13 * *", job=implnet_job_usgsmonitoringlocationnwissitenwissite2, default_status=DefaultScheduleStatus.RUNNING, execution_timezone="US/Central")
def implnet_sch_usgsmonitoringlocationnwissitenwissite2(_context):
    run_config = {}
    return run_config
