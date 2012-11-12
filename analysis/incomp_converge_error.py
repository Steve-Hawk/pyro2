#!/usr/bin/env python

import numpy
import mesh.patch as patch
import getopt
import sys
import advection.problems.smooth as smooth
import math

usage = """
      compare the output in file from the incompressible converge problem to
      the analytic solution.

      usage: ./incomp_converge_error.py file
"""

def error(imin, imax, dx, jmin, jmax, dy, r):

    # L2 norm of elements in r, multiplied by dx*dy to                          
    # normalize                                                                 
    return numpy.sqrt(dx*dy*numpy.sum((r[imin:imax+1,jmin:jmax+1]**2).flat))



def abort(string):
    print string
    sys.exit(2)


if not len(sys.argv) == 2:
    print usage
    sys.exit(2)


try: file1 = sys.argv[1]
except:
    print usage
    sys.exit(2)

myg, myd = patch.read(file1)


# numerical solution
u = myd.getVarPtr("x-velocity")
v = myd.getVarPtr("y-velocity")

t = myd.t

# analytic solution
u_exact = 1.0 - 2.0*numpy.cos(2.0*math.pi*(myg.x2d-t))*numpy.sin(2.0*math.pi*(myg.y2d-t))
v_exact = 1.0 + 2.0*numpy.sin(2.0*math.pi*(myg.x2d-t))*numpy.cos(2.0*math.pi*(myg.y2d-t))

# error
udiff = u_exact - u
vdiff = v_exact - v

print "errors: ", \
    error(myg.ilo, myg.ihi, myg.dx, myg.jlo, myg.jhi, myg.dy, udiff), \
    error(myg.ilo, myg.ihi, myg.dx, myg.jlo, myg.jhi, myg.dy, vdiff),








