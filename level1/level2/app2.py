print('& [root/level1/level2] app2.py')

import sys

sys.path.append('C:\\Users\\1800097.SYSTEX\\Dlevel2ktop\\systex\\exercise\\python-tlevel2t\\level1')

print('[1] __name__:', __name__)
print('[1] __package__:', __package__)

# import app2_2
# import .app2_2
# from . import app2_2

from ..utils import tool