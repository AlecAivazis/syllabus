# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#

PROJECT = syllabus
PACKAGE = settings
PROJ_CLEAN += $(EXPORT_MODULEDIR)/$(PACKAGE)


#--------------------------------------------------------------------------
#

EXPORT_DBDIR = $(EXPORT_ROOT)/db
EXPORT_DB = $(EXPORT_DBDIR)/db.sqlite3

all: export 

$(EXPORT_DB):
	$(MKDIR) $(MKPARENTS) $(EXPORT_DBDIR)
	$(CHMOD) ugo+rwx $(EXPORT_DBDIR)
	echo "" > $(EXPORT_DBDIR)/db.sqlite3
	$(CHMOD) ugo+rw $(EXPORT_DBDIR)/db.sqlite3

migrate:
	manage.py migrate

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    base.py \
    local.py \
    production.py \
    syllabus.py \
    __init__.py


export:: export-package-python-modules $(EXPORT_DB) migrate

# end of file 
