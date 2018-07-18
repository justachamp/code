import pytest
from datetime import datetime
from ui.fields import QuarterDateTimeField


@pytest.mark.parametrize('passed, expected', (
    (datetime(2013, 02, 25, 11, 53, 14, 6), datetime(2013, 02, 25, 11, 45)),
    (datetime(2013, 02, 25, 11, 45, 0, 0), datetime(2013, 02, 25, 11, 45)),
    (datetime(2013, 02, 25, 11, 59, 59), datetime(2013, 02, 25, 11, 45)),
))
@pytest.mark.unit
def test_quarter_rounding(passed, expected):
    field = QuarterDateTimeField()
    assert field.to_python(passed) == expected
