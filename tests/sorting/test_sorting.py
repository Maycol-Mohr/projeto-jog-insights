from src.pre_built.sorting import sort_by

jobs_list = [
    {"min_salary": 5000, "max_salary": 45000, "date_posted": "2000-05-30"},
    {"min_salary": 8000, "max_salary": 35000, "date_posted": "2020-05-30"},
    {"min_salary": 6000, "max_salary": 25000, "date_posted": "2010-05-30"},
]

jobs_min_salary = [
    {"min_salary": 5000, "max_salary": 45000, "date_posted": "2000-05-30"},
    {"min_salary": 6000, "max_salary": 25000, "date_posted": "2010-05-30"},
    {"min_salary": 8000, "max_salary": 35000, "date_posted": "2020-05-30"},
]

jobs_max_salary = [
    {"min_salary": 5000, "max_salary": 45000, "date_posted": "2000-05-30"},
    {"min_salary": 8000, "max_salary": 35000, "date_posted": "2020-05-30"},
    {"min_salary": 6000, "max_salary": 25000, "date_posted": "2010-05-30"},
]


jobs_date = [
   {"min_salary": 8000, "max_salary": 35000, "date_posted": "2020-05-30"},
   {"min_salary": 6000, "max_salary": 25000, "date_posted": "2010-05-30"},
   {"min_salary": 5000, "max_salary": 45000, "date_posted": "2000-05-30"},
]


def test_sort_by_criteria():
    sort_by(jobs_list, 'min_salary')
    assert jobs_list == jobs_min_salary

    sort_by(jobs_list, 'max_salary')
    assert jobs_list == jobs_max_salary

    sort_by(jobs_list, 'date_posted')
    assert jobs_list == jobs_date
