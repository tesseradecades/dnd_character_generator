from pytest import mark

class Test_example_method:
    @staticmethod
    @mark.skip
    def test_case_one():
        assert False

    @staticmethod
    def test_case_two():
        assert True

    @staticmethod
    def test_case_three():
        assert True
