#!/bin/bash
# https://dockerswarm.rocks/traefik/

docker compose -p dagster -f compose_local.yaml down

echo dagster stopped.