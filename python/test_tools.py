#
# python -m pytest -s -v 
#

import pytest
from huff_tools import MAXBITS, invertBits, setBits, getBitMask, getNBits, huffDecode

@pytest.mark.tc001
def test_invert_bits():
    assert invertBits(0b00000000) == -1

@pytest.mark.tc002
def test_invert_bits2():
    assert invertBits(0b11111111) == -256

@pytest.mark.tc003
def test_invert_bits3():
    assert invertBits(0b10101010) == -171

@pytest.mark.tc010
def test_setBits1():
    assert setBits(1) == 0b00000001


@pytest.mark.tc011
def test_setBits0():
    assert setBits(0) == 0b00000000

@pytest.mark.tc012
def test_setBits5():
    assert setBits(5) == 0b00011111

@pytest.mark.tc013
def test_setBits12():
    assert setBits(12) == 0b111111111111


@pytest.mark.tc020
def test_getBitMask20():
    assert getBitMask([0, 0,]) == (2, 0)

@pytest.mark.tc021
def test_getBitMask45():
    assert getBitMask([0, 1, 0, 1]) == (4, 5)

@pytest.mark.tc022
def test_getBitMask54():
    assert getBitMask([0, 0, 1, 0, 0]) == (5, 4)


@pytest.mark.tc030
def test_getNBits440():
    assert getNBits(4, 4, ['\xf0', '\xff', '\xff', '\xff', '\xff']) == 0b0000

@pytest.mark.tc031
def test_getNBits12_4_F():
    assert getNBits(12, 4, ['\x00', '\x0f', '\x00', '\x00', '\x00']) == 0b1111

@pytest.mark.tc032
def test_getNBits12_8_FF():
    assert getNBits(12, 8, ['\x00', '\x0f', '\xf0', '\x00', '\x00']) == 0b11111111

@pytest.mark.tc033
def test_getNBits12_12_FFF():
    assert getNBits(12, 12, ['\x00', '\x0f', '\xff', '\x00', '\x00']) == 0b111111111111

@pytest.mark.tc034
def test_getNBits_last():
    assert getNBits(36, 4, ['\x00', '\x00', '\x00', '\x00', '\x0f']) == 0b1111

@pytest.mark.tc035
def test_getNBits_12_16_FFFF():
    assert getNBits(12, 16, ['\x00', '\x0f', '\xff', '\xf0', '\x00']) == 0b1111111111111111


@pytest.mark.tc040
def test_huffDecodeLn():
    codes = {'\n': (4, 5), '\r': (4, 6), ' ': (4, 15), '"': (9, 385), "'": (6, 28), 'm': (6, 36), 'q': (10, 40) }
    assert huffDecode(4, 5, codes) == '\n'

@pytest.mark.tc041
def test_huffDecodeSp():
    codes = {'\n': (4, 5), '\r': (4, 6), ' ': (4, 15), '"': (9, 385), "'": (6, 28), 'm': (6, 36), 'q': (10, 40) }
    assert huffDecode(4, 15, codes) == ' '

@pytest.mark.tc042
def test_huffDecodeSpNoneGt():
    codes = {'\n': (4, 5), '\r': (4, 6), ' ': (4, 15), '"': (9, 385), "'": (6, 28), 'm': (6, 36), 'q': (10, 40) }
    assert huffDecode(5, 15, codes) is None

@pytest.mark.tc043
def test_huffDecodeSpNoneLt():
    codes = {'\n': (4, 5), '\r': (4, 6), ' ': (4, 15), '"': (9, 385), "'": (6, 28), 'm': (6, 36), 'q': (10, 40) }
    assert huffDecode(3, 15, codes) is None

@pytest.mark.tc044
def test_huffDecodeQNoneLt():
    codes = {'\n': (4, 5), '\r': (4, 6), ' ': (4, 15), '"': (9, 385), "'": (6, 28), 'm': (6, 36), 'q': (10, 40) }
    assert huffDecode(9, 40, codes) is None

@pytest.mark.tc045
def test_huffDecodeQNoneGt():
    codes = {'\n': (4, 5), '\r': (4, 6), ' ': (4, 15), '"': (9, 385), "'": (6, 28), 'm': (6, 36), 'q': (10, 40) }
    assert huffDecode(11, 40, codes) is None

@pytest.mark.tc046
def test_huffDecodeQ():
    codes = {'\n': (4, 5), '\r': (4, 6), ' ': (4, 15), '"': (9, 385), "'": (6, 28), 'm': (6, 36), 'q': (10, 40) }
    assert huffDecode(10, 40, codes) == 'q'


# TODO decode_read