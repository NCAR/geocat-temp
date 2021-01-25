#!/bin/sh

cd src/geocat/f2py/fortran
f2py -c --fcompiler=gnu95 linint2.pyf linint2.f
f2py -c --fcompiler=gnu95 rcm2rgrid.pyf rcm2rgrid.f linmsg_dp.f linint2.f
f2py -c -llapack --fcompiler=gnu95 eof_scripps.pyf eof_scripps.f90
f2py -c -llapack --fcompiler=gnu95 prneofts_dp.pyf prneofts_dp.f statx_dp.f
f2py -c -llapack --fcompiler=gnu95 prneof_dp.pyf prneof_dp.f statx_dp.f
f2py -c -llapack --fcompiler=gnu95 prneofTranspose.pyf prneofTranspose.f
f2py -c --fcompiler=gnu95 moc_loops.pyf moc_loops.f
f2py -c --fcompiler=gnu95 dpres_plevel_dp.pyf dpres_plevel_dp.f
cd ../../../..

python -m pip install . --no-deps -vv
