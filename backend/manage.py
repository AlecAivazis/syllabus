#!/usr/bin/env python3
#
# alec aivazis
# 
 
# when run from the command line
if __name__ == "__main__":

    import os
    import sys
    from django.core.management import execute_from_command_line

    # load the correct django settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "syllabus.settings.local")

    # if they asked for a live reaload server
    if 'livereload' in sys.argv:
        
        from django.core.wsgi import get_wsgi_application
        from livereload import Server

        # grab the wsgi app from django
        application = get_wsgi_application()
        # make a live reload wrapper around the wsgi app
        server = Server(application)

        # if the user specified a port
        if len(sys.argv) == 3:
            # start the server at the port designated by the last argument
            server.serve(port=sys.argv[2])
        # otherwise the user only provided one argument
        else:
            # start the server at the default port
            server.serve()

    # otherwise they didn't ask for a live reload server
    else:
        # perform the default action
        execute_from_command_line(sys.argv)


# end of file
