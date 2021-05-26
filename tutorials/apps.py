from django.apps import AppConfig


class TutorialsConfig(AppConfig):
    name = 'tutorials'

class CorsMiddleware(object):
    def process_response(self, req, resp):
        response["Access-Control-Allow-Origin"] = "*"
        return response