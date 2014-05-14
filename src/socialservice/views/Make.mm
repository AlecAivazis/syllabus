# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#

PROJECT = syllabus
PACKAGE = socialservice/views
PROJ_CLEAN += $(EXPORT_MODULEDIR)/$(PACKAGE)


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    meetings.py \
    __init__.py


export:: export-package-python-modules

# end of file 
