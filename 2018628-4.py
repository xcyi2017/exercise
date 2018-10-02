from sympy import plot_implicit as pt, Eq
from sympy.abc import x, y
import numpy as np

p1 = pt(Eq(x**3+y**4,1))