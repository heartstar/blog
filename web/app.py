#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import uuid
import base64

STATIC_PATH = os.path.join(sys.path[0], 'static')
URLS = [
    (r'(localhost',
        (r'/', 'handler.web.IndexHandler'),
    )
]
TPL_PATH = os.path.join(sys.path[0], 'tpl')


class Application(web.Application):

    def __init__(self):
        settings = {
            'login_url': '/login',
            'xsrf_cookies': False,
            'debug': options.debug,
            'static_path': STATIC_PATH,
            'template_path': TPL_PATH,
        }
        web.Application.__init__(self, **settings)

        for spec in URLS:
            host = '.*$'
            handlers = spec[1:]
            self.add_handlers(host, handlers)


def run():
    application = Application()
    http_server = HTTPServer(application, xheaders=True)
    http_server.listen(options.port)
    print('Running on port %d' % options.port)
