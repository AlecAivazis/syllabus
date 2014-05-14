# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#

PROJECT = syllabus
PACKAGE = classroom/urls
PROJ_CLEAN += $(EXPORT_MODULEDIR)/$(PACKAGE)


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    calendar.py \
    gradebook.py \
    massageboard.py \
    myClasses.py \
    spaces.py \
    __init__.py


export:: export-package-python-modules

# end of file 
