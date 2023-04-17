from mypack.mymodule import myfunc
import numpy.testing as npt


class TestMyModule:
    """Test mymodule module."""

    value1 = 6.0
    value2_good = 3.0
    value2_bad = 0.0
    expected = 1.0

    def test_myfunc(self):
        """Test myfunc."""
        npt.assert_equal(myfunc(self.value1, self.value2_good), self.expected)

        npt.assert_raises(ValueError, myfunc, self.value1, self.value2_bad)
