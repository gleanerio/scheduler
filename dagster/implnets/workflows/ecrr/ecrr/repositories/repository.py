from dagster import repository

from jobs.implnet_jobs_ecrr_submitted import implnet_job_ecrr_submitted
from sch.implnet_sch_ecrr_submitted  import implnet_sch_ecrr_submitted
from jobs.implnet_jobs_ecrr_examples import implnet_job_ecrr_examples
from sch.implnet_sch_ecrr_examples  import implnet_sch_ecrr_examples

@repository
def ecrr():
	jobs = [ implnet_job_ecrr_submitted, implnet_job_ecrr_examples]
	schedules = [ implnet_sch_ecrr_submitted, implnet_sch_ecrr_examples]


	return jobs + schedules
