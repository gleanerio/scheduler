from dagster import repository, Definitions
import os
from .jobs.implnet_jobs_ecrr_submitted import job_ecrr_submitted
from .sch.implnet_sch_ecrr_submitted  import implnet_sch_ecrr_submitted
from .jobs.implnet_jobs_ecrr_examples import job_ecrr_examples
from .sch.implnet_sch_ecrr_examples  import implnet_sch_ecrr_examples

from dagster_slack import SlackResource, make_slack_on_run_failure_sensor
slack_on_run_failure = make_slack_on_run_failure_sensor(
     os.getenv("SLACK_CHANNEL"),
    os.getenv("SLACK_TOKEN")
)
jobs = [ job_ecrr_submitted, job_ecrr_examples]
schedules = [ implnet_sch_ecrr_submitted, implnet_sch_ecrr_examples]

defs = Definitions(
	jobs=jobs,
	schedules=schedules,
	sensors=[slack_on_run_failure]
)
