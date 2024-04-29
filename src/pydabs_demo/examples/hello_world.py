from databricks.bundles.jobs import task, job


@task
def print_hello_world():
    print("Hello, World!")


@job
def hello_world():
    print_hello_world()
