# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#


PROJECT = syllabus
PACKAGE = core/urls
PROJ_CLEAN += $(EXPORT_MODULEDIR)

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    core.py \
    myHomework.py \
    myProfile.py \
    __init__.py

export:: export-package-python-modules

# end of file 
