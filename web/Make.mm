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

.PHONY: resources

export:: resources

resources: 
	$(CP_R) resources templates $(EXPORT_ROOT)


# end of file 
