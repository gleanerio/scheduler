#!/bin/bash
# https://dockerswarm.rocks/traefik/
if [ -f compose_local_${PROJECT}_override.yaml ]
  then
    override_file="-f compose_local_${PROJECT}_override.yaml"
  else
    override_file=""
fi

docker compose -p dagster -f compose_local.yaml $override_file down

echo dagster stopped.
