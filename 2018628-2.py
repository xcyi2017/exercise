from sympy.parsing.sympy_parser import parse_expr  
from sympy import plot_implicit  

ezplot = lambda exper: plot_implicit(parse_expr(exper))#用了匿名函数  
expression='x*sin(10*pi*x)-y'#隐函数是x**2+y**2-1=0，其实就是圆的方程  
ezplot(expression)#能描绘大致的图像  
