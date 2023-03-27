from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        jobs_file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        read_jobs = []
        for jobs in jobs_file_reader:
            read_jobs.append(jobs)
        return list(read_jobs)


def get_unique_job_types(path: str) -> List[str]:
    unique_jobs_type = set()
    for job in read(path):
        unique_jobs_type.add(job["job_type"])
    return list(unique_jobs_type)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_job = [job for job in jobs if job['job_type'] == job_type]
    return list(filter_job)
