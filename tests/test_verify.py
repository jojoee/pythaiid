import unittest
from pythaiid import verify


class TestVerify(unittest.TestCase):

    def test_input_must_be_number(self):
        self.assertEqual(verify(None), False)
        self.assertEqual(verify(True), False)
        self.assertEqual(verify(False), False)
        self.assertEqual(verify([]), False)
        self.assertEqual(verify([1, 2, 3]), False)
        self.assertEqual(verify({}), False)
        self.assertEqual(verify(''), False)
        self.assertEqual(verify(), False)
        self.assertEqual(verify('this-is-not-number'), False)
        self.assertEqual(verify('it-must-be-number-only'), False)

    def test_input_length_does_not_equal_13(self):
        self.assertEqual(verify('0'), False)
        self.assertEqual(verify('1'), False)
        self.assertEqual(verify('0123456'), False)
        self.assertEqual(verify('01234567890123456789'), False)

    def test_valid_checksum(self):
        self.assertEqual(verify('3648905117162'), True)
        self.assertEqual(verify('1234567891020'), True)
        self.assertEqual(verify('3648905117090'), True)
        self.assertEqual(verify('1234567891011'), True)
        self.assertEqual(verify('3648905117031'), True)
        self.assertEqual(verify('1234567891062'), True)
        self.assertEqual(verify('3648905117022'), True)
        self.assertEqual(verify('1234567891003'), True)
        self.assertEqual(verify('3648905117073'), True)
        self.assertEqual(verify('1234567891054'), True)
        self.assertEqual(verify('3648905117014'), True)
        self.assertEqual(verify('1234567891305'), True)
        self.assertEqual(verify('3648905117065'), True)
        self.assertEqual(verify('1234567891046'), True)
        self.assertEqual(verify('3648905117006'), True)
        self.assertEqual(verify('1234567891097'), True)
        self.assertEqual(verify('3648905117707'), True)
        self.assertEqual(verify('1234567891038'), True)
        self.assertEqual(verify('3648905117308'), True)
        self.assertEqual(verify('1234567891089'), True)
        self.assertEqual(verify('3648905117049'), True)

    def test_invalid_checksum(self):
        self.assertEqual(verify('1234567891021'), False)
        self.assertEqual(verify('3648905117092'), False)
        self.assertEqual(verify('1234567891012'), False)
        self.assertEqual(verify('3648905117033'), False)
        self.assertEqual(verify('1234567891063'), False)
        self.assertEqual(verify('3648905117024'), False)
        self.assertEqual(verify('1234567891004'), False)
        self.assertEqual(verify('3648905117075'), False)
        self.assertEqual(verify('1234567891055'), False)
        self.assertEqual(verify('3648905117016'), False)
        self.assertEqual(verify('1234567891306'), False)
        self.assertEqual(verify('3648905117067'), False)
        self.assertEqual(verify('1234567891047'), False)
        self.assertEqual(verify('3648905117008'), False)
        self.assertEqual(verify('1234567891098'), False)
        self.assertEqual(verify('3648905117709'), False)
        self.assertEqual(verify('1234567891039'), False)
        self.assertEqual(verify('3648905117300'), False)
        self.assertEqual(verify('1234567891080'), False)
        self.assertEqual(verify('3648905117041'), False)
