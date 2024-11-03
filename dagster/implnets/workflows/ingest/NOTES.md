
# Schedules

It's hard to a set of dynamic Schedules, with varying crons
https://github.com/dagster-io/dagster/discussions/22121

Right now, all sources will run weekly

while not ideal, I think we could setup three schedules: daily, weekly, monthly and quarterly.
Then if a the cron in the source matched, a run would occur.

more complex would be having something that ran (hourly), 
and go through the list of sources, and last runs, and if it was time to run, then run that source.
Basically put an evaluation function in before seeing if a run should occur,
if it should do add run request to list of run requests for time, then return that list.


How do I write a sensor or schedule that requests a run for every partition on every tick?
https://github.com/dagster-io/dagster/discussions/15532

partiton metadata about last run: https://github.com/dagster-io/dagster/discussions/14338
How to ensure the previous partition of a job has succeeded before running the next partition https://github.com/dagster-io/dagster/discussions/10264

dynamic partitions
https://docs.dagster.io/concepts/partitions-schedules-sensors/partitioning-assets#dynamically-partitioned-assets

