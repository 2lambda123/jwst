#!/usr/bin/env python

# Copyright (C) 2011-2012 Association of Universities for Research in Astronomy (AURA)

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

#     1. Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.

#     2. Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.

#     3. The name of AURA and its representatives may not be used to
#       endorse or promote products derived from this software without
#       specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY AURA ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL AURA BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
# TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.

# STDLIB
import argparse
import sys

# LOCAL
from jwst import ipc


def main():
    if '--version' in sys.argv:
        sys.stdout.write('%s\n' % ipc.__version__)
        sys.exit(0)

    parser = argparse.ArgumentParser("""Do IPC correction on Level 1b FITS files""")

    parser.add_argument(
        'infile', metavar='infile', nargs=1, help="""Input Level 1b FITS file."""
    )

    parser.add_argument(
        'outfile', metavar='outfile', nargs=1, help="""Output IPC corrected file"""
    )

    args = parser.parse_args()

    ipc_a = ipc.ipc_corr.DataSet(args.infile[0], args.outfile[0])
    ipc_a.do_all()


if __name__ == '__main__':
    main()
