# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the base views for syllabus

# django imports
from django.views.generic import TemplateView
# python-react: https://github.com/markfinger/python-react
from react.render import render_component

class Home(TemplateView):
    """
    render the index template
    """
    template_name = 'index.jade'


# end of file
