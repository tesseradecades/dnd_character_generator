from typing import List

from gene_model.convergence_tests import hamming_distance

class Test_hamming_distance:
    @staticmethod
    def test_empty_lists():
        # arrange
        list1: List[int] = []
        list2: List[int] = []

        # act
        actual:int = hamming_distance(list1,list2)

        # assert
        assert actual == 0
    
    @staticmethod
    def test_one_empty_list():
        # arrange
        empty_list: List[int] = []
        nonempty_list: List[int] = [0]

        # act
        actual:int = hamming_distance(empty_list,nonempty_list)

        # assert
        assert actual == len(nonempty_list)
    
    @staticmethod
    def test_equal_lists():
        # arrange
        some_list: List[int] = [0]

        # act
        actual:int = hamming_distance(some_list,some_list)

        # assert
        assert actual == 0
    
    @staticmethod
    def test_different_lists():
        # arrange
        one_list: List[int]=[1]
        zero_list: List[int] = [0]

        # act
        actual:int = hamming_distance(one_list,zero_list)

        # assert
        assert actual == 1
    
    @staticmethod
    def test_different_lists_of_different_length():
        # arrange
        one_list: List[int]=[1,0]
        zero_list: List[int] = [0]

        # act
        actual:int = hamming_distance(one_list,zero_list)

        # assert
        assert actual == 2