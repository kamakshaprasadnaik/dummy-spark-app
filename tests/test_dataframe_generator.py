import pytest
from DataframeGenerator import DataGenerator

@pytest.fixture()
def data_generator():
    return DataGenerator(1)

def test_get_id(data_generator):
    assert str((data_generator.get_id())).isdigit()
        
def test_get_names(data_generator):
    assert str(data_generator.get_names())
def test_get_city(data_generator):
    assert data_generator.get_city()
    
def test_get_salary(data_generator):
    assert 100000 <= data_generator.get_salary() < 1000000
    
def test_string_representation(data_generator):
    assert str(data_generator)=="Data generator with 1 rows"