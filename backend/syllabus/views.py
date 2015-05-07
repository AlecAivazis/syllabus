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


class ComponentView(TemplateView):
    """
    render the index template
    """
    template_name = 'component.jade'

    def get_context_data(self, **kwargs):
        # grab the parent context
        context = super().get_context_data()
        # add the rendered component to the context
        context['component'] = render_component(self.component_path, translate=True)
        # return the modified context
        return context


# end of file
