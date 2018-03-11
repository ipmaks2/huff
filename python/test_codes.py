#
# python -m pytest -s -v 
#

import pytest
from huff_codes import getCodes

@pytest.mark.tc001
def test_getCodes1():
    tups = [('1', 100), ('2', 90), ('4', 85), ('8', 50), ('7', 20), ('3', 10), ('5', 10), ('6', 10), ('9', 9), ('0', 9)]        
    codes = getCodes(tups)
    for c, bits in codes.items():
        print c, bits

# TODO decode_read