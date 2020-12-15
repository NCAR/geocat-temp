import numpy as np
import xarray as xr
from dask.array.core import map_blocks
import time

from geocat.f2py.fortran import (deofts7)
from geocat.f2py import (eof11)
from .missing_values import (fort2py_msg, py2fort_msg)


# Dask Wrappers _<funcname>()
# These Wrapper are executed within dask processes, and should do anything that
# can benefit from parallel excution.
def _eofts7(x, evec, nobs, msta, msg_py, jopt):
    # evects = deofts7(x,evec,[nobs,msta,xmsg,jopt])

    # missing value handling
    x, msg_py, msg_fort = py2fort_msg(x, msg_py=msg_py)

    # fortran call
    evects = deofts7(x, evec, nobs, msta, xmsg=msg_py, jopt=jopt)

    # missing value handling
    x, msg_fort, msg_py = fort2py_msg(x, msg_fort=msg_fort, msg_py=msg_py)
    return evects

def eofts7(x, evec, nobs = None, msta = None, msg_py = None, jopt = None):
    # this is effectivly a stub, since this is not a parallelizable task.
    return _eofts7(x, evec, nobs, msta, msg_py, jopt)