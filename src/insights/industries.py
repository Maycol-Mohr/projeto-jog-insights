from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    get_unique = set()
    for job in read(path):
        if job['industry'] != '':
            get_unique.add(job['industry'])
    return list(get_unique)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filter_job = [job for job in jobs if job['industry'] == industry]
    return list(filter_job)
