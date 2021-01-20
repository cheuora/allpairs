# this is test code
import pytest
import itertools
from pairwise import Coverage, pairCovArray

parameters = [ [ "Brand X", "Brand Y","Brand A","Brand B","Brand C","Brand D" ]
             , [ "98", "NT", "2000", "XP"]
             , [ "Internal", "Modem" ],
             [56,45,22,34],
             ]

sample_combinations = [('Brand X', 'XP', 'Modem', 98), ('Brand D', 'XP', 'Modem', 45)]

@pytest.fixture
def ttt():
    ttt = Coverage(pairCovArray)
    return ttt

# def test_searchCoverageItem(ttt):
#     # ('Brand X', '2000')의 위치 반환
#     assert ttt.searchCoverageItem(('Brand X', '2000')) == (0,2)



# def test_updateCoverage(ttt):
#     ttt.updateCoverage((0,2)) #(0,2)에 해당하는 ('Brand X', '2000') 의 삭제 
#     assert ttt.searchCoverageItem(('Brand X', '2000')) == False

    
def test_checkCoverage(ttt):
    assert ttt.checkCoverage(sample_combinations[0]) == False