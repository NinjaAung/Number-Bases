from bases import convert
import unittest

class BasesConvertTest(unittest.TestCase):

    def test_convert_from_binary(self):
        assert convert('1101', 2, 3) == '111'
        assert convert('1101', 2, 4) == '31'
        assert convert('1101', 2, 8) == '15'
        assert convert('1101', 2, 10) == '13'
        assert convert('101010', 2, 3) == '1120'
        assert convert('101010', 2, 4) == '222'
        assert convert('101010', 2, 8) == '52'
        assert convert('101010', 2, 10) == '42'
        assert convert('101010', 2, 16) == '2a'
        assert convert('101010', 2, 25) == '1h'
        assert convert('101010', 2, 32) == '1a'
        assert convert('101010', 2, 36) == '16'

    def test_convert_to_binary(self):
        assert convert('111', 3, 2) == '1101'
        assert convert('31', 4, 2) == '1101'
        assert convert('15', 8, 2) == '1101'
        assert convert('13', 10, 2) == '1101'
        assert convert('101', 3, 2) == '1010'
        assert convert('101', 4, 2) == '10001'
        assert convert('101', 8, 2) == '1000001'
        assert convert('101', 10, 2) == '1100101'
        assert convert('101', 16, 2) == '100000001'
        assert convert('101', 25, 2) == '1001110010'
        assert convert('101', 32, 2) == '10000000001'
        assert convert('101', 36, 2) == '10100010001'

    def test_convert_hexadecimal_to_decimal(self):
        assert convert('a', 16, 10) == '10'
        assert convert('f', 16, 10) == '15'
        assert convert('99', 16, 10) == '153'
        assert convert('ff', 16, 10) == '255'
        assert convert('ace', 16, 10) == '2766'
        assert convert('cab', 16, 10) == '3243'
        assert convert('bead', 16, 10) == '48813'
        assert convert('face', 16, 10) == '64206'
        assert convert('c0ffee', 16, 10) == '12648430'
        assert convert('facade', 16, 10) == '16435934'
        assert convert('deadbeef', 16, 10) == '3735928559'
        assert convert('f007ba11', 16, 10) == '4027038225'

    def test_convert_decimal_to_hexadecimal(self):
        assert convert('10', 10, 16) == 'a'
        assert convert('15', 10, 16) == 'f'
        assert convert('153', 10, 16) == '99'
        assert convert('255', 10, 16) == 'ff'
        assert convert('2766', 10, 16) == 'ace'
        assert convert('3243', 10, 16) == 'cab'
        assert convert('48813', 10, 16) == 'bead'
        assert convert('64206', 10, 16) == 'face'
        assert convert('12648430', 10, 16) == 'c0ffee'
        assert convert('16435934', 10, 16) == 'facade'
        assert convert('3735928559', 10, 16) == 'deadbeef'
        assert convert('4027038225', 10, 16) == 'f007ba11'

    def test_convert_hexadecimal_to_binary(self):
        assert convert('a', 16, 2) == '1010'
        assert convert('b', 16, 2) == '1011'
        assert convert('c', 16, 2) == '1100'
        assert convert('d', 16, 2) == '1101'
        assert convert('e', 16, 2) == '1110'
        assert convert('f', 16, 2) == '1111'
        assert convert('c840', 16, 2) == '1100100001000000'
        assert convert('d951', 16, 2) == '1101100101010001'
        assert convert('ea62', 16, 2) == '1110101001100010'
        assert convert('fb73', 16, 2) == '1111101101110011'

    def test_convert_binary_to_hexadecimal(self):
        assert convert('1010', 2, 16) == 'a'
        assert convert('1011', 2, 16) == 'b'
        assert convert('1100', 2, 16) == 'c'
        assert convert('1101', 2, 16) == 'd'
        assert convert('1110', 2, 16) == 'e'
        assert convert('1111', 2, 16) == 'f'
        assert convert('1100100001000000', 2, 16) == 'c840'
        assert convert('1101100101010001', 2, 16) == 'd951'
        assert convert('1110101001100010', 2, 16) == 'ea62'
        assert convert('1111101101110011', 2, 16) == 'fb73'


if __name__ == '__main__':
    unittest.main()