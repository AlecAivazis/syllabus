# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the for auth

# django imports
from django.views.generic import TemplateView

# index view
class Home(TemplateView):
    # return the rendered template
    """
    The index view
    """
    template_name =  "index.jade"


# end of file
