# -*- coding: utf-8 -*-

# Import the application framework
import webapp2

from tools.common import is_testenv

# Import our application settings/configuration
from settings import config

# And of course import our application routes
import routes

application = webapp2.WSGIApplication(routes.urls, config=config, debug=is_testenv())
    
