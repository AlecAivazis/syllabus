# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#


PROJECT = syllabus
PACKAGE = wishlist
PROJ_CLEAN += $(EXPORT_MODULEDIR)

RECURSE_DIRS = \


#--------------------------------------------------------------------------
#

all: export

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse


#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    admin.py \
    models.py \
    tests.py \
    __init__.py \

export:: export-package-python-modules
	BLD_ACTION="export" $(MM) recurse

# end of file 
