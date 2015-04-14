# this file contains common imports among all of the views

from django.shortcuts import HttpResponseRedirect, HttpResponse, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from compressor.contrib.jinja2ext import CompressorExtension

import re

from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from django.core.servers.basehttp import FileWrapper
import calendar, os, mimetypes, zipfile, tempfile
from collections import defaultdict
import datetime, collections, time

from re import escape
from collections import defaultdict, OrderedDict

from datetime import date

def nl2br(value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') for p in _paragraph_re.split(escape(value)))
    return result

#env.filters['linebreaks'] = nl2br

dayDict = {
    '1':'M',
    '2':'T',
    '3':'W',
    '4':'Th',
    '5':'F',
    '6':'Sat',
    '7':'Sun'
}


#def render_to_response(filename, context={}):
#    template = env.get_template(filename)
#    rendered = template.render(**context)
#
#    return HttpResponse(rendered)

syllabus_version = (0, 8, 287)
