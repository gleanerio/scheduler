# Notes

## Development

At the top level (dagster/implents) you can run 

`dagster dev`

You need to set the environment based on dagster/implnets/deployment/envFile.env

It should run workflows/tasks/tasks

defined in the pyproject.toml

```
[tool.dagster]
module_name = "workflows.tasks.tasks"
```

### testing tasks

cd dagster/implnets/workflows/tasks
You need to set the environment based on dagster/implnets/deployment/envFile.env

`dagster dev`
will run just the task, and in editable form, i think.

## Some articles to review

[Medium on Dagster with configurable API and asset examples](https://medium.com/@alexandreguitton_12701/notes-1-2-dagster-data-orchestrator-hands-on-2af6772b13d9)
