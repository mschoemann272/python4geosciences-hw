import example1_addmath
import numpy as np

def test_ex1_addmath():
    assert example1_addmath.add_math() == np.sum(59)
