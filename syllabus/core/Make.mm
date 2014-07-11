# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#


PROJECT = syllabus
PACKAGE = core
PROJ_CLEAN += $(EXPORT_MODULEDIR)

RECURSE_DIRS = \
    urls \
    views \


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
    jinja2_for_django.py \
    forms.py \
    middlewares.py \
    models.py \
    tests.py \
    __init__.py

export:: export-package-python-modules
	BLD_ACTION="export" $(MM) recurse

# end of file 
