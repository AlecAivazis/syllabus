# -*- Makefile -*-
#
# alec aivazis
# orthologue
# (c) 1998-2014 all rights reserved
#


PROJECT = syllabus

RECURSE_DIRS = \
    bin \
    people \
    syllabus \
    util \
    apache \

#--------------------------------------------------------------------------
#
run: all server 

server:
	manage.py runserver_plus

all:
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse


#--------------------------------------------------------------------------
#  shortcuts to building in my subdirectories
.PHONY: bin people src 

bin:
	(cd bin; $(MM))

people:
	(cd people; $(MM))

syllabus:
	(cd syllabus; $(MM))

build: 

test: 


# end of file 
