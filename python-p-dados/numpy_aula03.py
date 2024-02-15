import sys
sys.path.append(r'c:\users\user\appdata\local\programs\python\python310\lib\site-packages')

import numpy as np

print(np.array([5.4,6.7,2.1]).dtype) #float64
print(np.array([5,6,2]).dtype) #int32
print(np.array(["Hello", "oi", "womakerscode"]).dtype) #<U12
print(np.array([True, 3, False]).dtype) #int32

x = np.array([3,4,2.1])
print(x.astype(np.int32)) #ele exclui o decimal

vf = np.array([True, 3, False])
print(vf.astype(np.bool_))