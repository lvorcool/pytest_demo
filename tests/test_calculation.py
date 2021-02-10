import pytest
import yaml

from scripts.calculation import Calculation

'''
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
'''


def loads_test_calculation_datas():
    with open('../datas/calculation.yaml') as f:
        return yaml.safe_load(f)


class TestCalculation:

    def setup_class(self):
        self.cal = Calculation()

    def teardown_class(self):
        pass

    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,result", [(1, 2, 3), (2, 3, 4), (1.0, 3, 4.0), ('a', 3, "相加只能整数型和浮点数形哦")])
    def test_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,result", loads_test_calculation_datas()['test_divide'])
    def test_divide(self, a, b, result):
        assert result == self.cal.divide(a, b)
