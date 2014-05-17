# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#


PROJECT = syllabus
PACKAGE = syllabus
PROJ_TIDY = *~ .*~ *.pyc
PROJ_CLEAN += $(EXPORT_MODULEDIR)

RECURSE_DIRS = \
    academia \
    classroom \
    core \
    messages \
    wishlist \
    settings \
    socialservice \


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
    middlewares.py \
    urls.py \
    __init__.py

export:: __init__.py export-python-modules export-resources
	BLD_ACTION="export" $(MM) recurse
	@$(RM) __init__.py

export-resources:
	$(CP_R) resources templates $(EXPORT_ROOT)

# construct my {__init__.py}
__init__.py: __init__py
	@sed -e "s:BZR_REVNO:$$(bzr revno):g" __init__py > __init__.py


# end of file 
