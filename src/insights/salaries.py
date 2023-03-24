from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salaries_value = set()
    for salary_value in read(path):
        if salary_value['max_salary'].isdigit():
            salaries_value.add(int(salary_value['max_salary']))
    return max(salaries_value)


def get_min_salary(path: str) -> int:
    salaries_value = set()
    for salary_value in read(path):
        if salary_value['min_salary'].isdigit():
            salaries_value.add(int(salary_value['min_salary']))
    return min(salaries_value)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        not isinstance(salary, (int, str))
        or 'min_salary' not in job
        or 'max_salary' not in job
        or not str(job['min_salary']).isdigit()
        or not str(job['max_salary']).isdigit()
        or not int(job["min_salary"]) and int(job['min_salary']) != 0
        or not int(job["max_salary"])
        or int(job["min_salary"]) > int(job["max_salary"])
        or not salary and int(salary) != 0
    ):
        raise ValueError(
            "Error in max-salary or min-salary or salary, "
            "incorrect values or ranges"
        )
    if int(job['min_salary']) <= int(salary) <= int(job['max_salary']):
        return True
    else:
        return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
