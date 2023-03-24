from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        read_jobs = []
        jobs_file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for jobs in jobs_file_reader:
            read_jobs.append(jobs)
        return read_jobs


def get_unique_job_types(path: str) -> List[str]:
    unique_jobs_type = set()
    for job in read(path):
        unique_jobs_type.add(job["job_type"])
    return list(unique_jobs_type)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
