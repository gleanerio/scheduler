# How to use this repository

1. Create a new .venv
2. Source the .venv
3. Install `requirements.txt`
4. Use the functions in main.py to build your jobs and config before spinning up the docker containers
    1. Run `python3 main.py generate-config`
    2. Run `python3 main.py generate-jobs`
    3. After these two, your `build/` directory should be populated with the jobs

