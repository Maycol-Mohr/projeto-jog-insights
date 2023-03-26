# from src.pre_built.brazilian_jobs import read_brazilian_file
# from src.insights.jobs import read
# from unittest.mock import mock_open, patch
# import pytest


# @pytest.fixture
# def english_type():
#     return {"title": "Maquinista", "salary": "2000", "type": "trainee"}


# # @pytest.fixture
# # def portuguese_type():
# #     return {"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}


# def test_brazilian_jobs():
#     with patch("builtins.open",
# mock_open(read_data='tests/mocks/brazilians_jobs.csv')):
#         read_file = read(patch)
#         # file_path =  read_brazilian_file('tests/mocks/brazilians_jobs.csv')

#     dict_jobs = read_file
#     for job in dict_jobs:
#         job["title"] = job.pop("titulo")
#         job["salary"] = job.pop("salario")
#         job["type"] = job.pop("tipo")

#     assert read_brazilian_file(dict_jobs) == english_type
