from typing import List, Tuple
from .env import GLEANERIO_GLEANER_IMAGE, GLEANERIO_GLEANER_CONFIG_PATH, GLEANERIO_NABU_IMAGE, GLEANERIO_NABU_CONFIG_PATH
from .types import cli_modes

def get_cli_args(
    mode: cli_modes,
    source: str,
) -> Tuple[str, List[str], str, str]:
    """Given a mode and source return the cli args that are needed to run either gleaner or nabu"""
    if mode == "gleaner":
        IMAGE = GLEANERIO_GLEANER_IMAGE
        ARGS = ["--cfg", GLEANERIO_GLEANER_CONFIG_PATH, "-source", source, "--rude"]
        NAME = f"sch_{source}_{str(mode)}"
        WorkingDir = "/gleaner/"
    else:
        # Handle all nabu modes
        IMAGE = GLEANERIO_NABU_IMAGE
        WorkingDir = "/nabu/"
        NAME = f"sch_{source}_{str(mode)}"
        match mode:
            case "release":
                ARGS = [
                    "--cfg",
                    GLEANERIO_NABU_CONFIG_PATH,
                    "release",
                    "--prefix",
                    "summoned/" + source,
                ]
            case "object":
                ARGS = [
                    "--cfg",
                    GLEANERIO_NABU_CONFIG_PATH,
                    "object",
                    f"/graphs/latest/{source}_release.nq",
                    "--endpoint",
                    GLEANERIO_DATAGRAPH_ENDPOINT,
                ]
            case "prune":
                ARGS = [
                    "--cfg",
                    GLEANERIO_NABU_CONFIG_PATH,
                    "prune",
                    "--prefix",
                    "summoned/" + source,
                    "--endpoint",
                    GLEANERIO_DATAGRAPH_ENDPOINT,
                ]
            case "prov-release":
                ARGS = [
                    "--cfg",
                    GLEANERIO_NABU_CONFIG_PATH,
                    "release",
                    "--prefix",
                    "prov/" + source,
                ]

            case "prov-clear":
                ARGS = [
                    "--cfg",
                    GLEANERIO_NABU_CONFIG_PATH,
                    "clear",
                    "--endpoint",
                    "--endpoint",
                    GLEANERIO_PROVGRAPH_ENDPOINT,
                ]
            case "prov-object":
                ARGS = [
                    "--cfg",
                    GLEANERIO_NABU_CONFIG_PATH,
                    "object",
                    f"/graphs/latest/{source}_prov.nq",
                    "--endpoint",
                    GLEANERIO_PROVGRAPH_ENDPOINT,
                ]
            case "prov-drain":
                ARGS = [
                    "--cfg",
                    GLEANERIO_NABU_CONFIG_PATH,
                    "drain",
                    "--prefix",
                    "prov/" + source,
                ]
            case "orgs-release":
                ARGS = [
                    "--cfg",
                    GLEANERIO_NABU_CONFIG_PATH,
                    "release",
                    "--prefix",
                    "orgs",
                    "--endpoint",
                    GLEANERIO_DATAGRAPH_ENDPOINT,
                ]
            case "orgs":
                ARGS = [
                    "--cfg",
                    GLEANERIO_NABU_CONFIG_PATH,
                    "prefix",
                    "--prefix",
                    "orgs",
                    "--endpoint",
                    GLEANERIO_DATAGRAPH_ENDPOINT,
                ]
            case _:
                get_dagster_logger().error(f"Called gleaner with invalid mode: {mode}")
                return 1
    return IMAGE, ARGS, NAME, WorkingDir
