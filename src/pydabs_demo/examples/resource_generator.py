import os

from databricks.bundles.jobs import notebook_task, job, resource_generator


def create_notebook_job(filename: str):
    resource_name = filename.replace(" ", "_").rstrip(".ipynb").lower()

    @notebook_task(notebook_path=f"notebooks/{filename}")
    def my_notebook():
        pass

    @job(name=filename, resource_name=resource_name)
    def my_job():
        my_notebook()

    return my_job


@resource_generator
def my_notebook_jobs():
    """
    Automatically create jobs with notebook tasks for each notebook in "notebooks" directory.
    """

    for filename in os.listdir("notebooks"):
        if not filename.endswith(".ipynb"):
            continue

        yield create_notebook_job(filename)
