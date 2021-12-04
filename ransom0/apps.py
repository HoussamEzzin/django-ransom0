from django.apps import AppConfig
import sys
from urllib.parse import urlparse
from django.conf import settings



class Ransom0Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ransom0'
    
    def ready(self):
        if settings.DEV_SERVER and settings.USE_NGROK:
            from pyngrok import ngrok
            
            addrport = urlparse("http://{}".format(sys.argv[-1]))
            port = addrport.port if addrport.netloc and addrport.port else 8000
            
            public_url = ngrok.connect(port).public_url
            
            print("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))
            settings.ALLOWED_HOSTS.append(public_url)

            # Update any base URLs or webhooks to use the public ngrok URL
            settings.BASE_URL = public_url
            Ransom0Config.init_webhooks(public_url)
    
    
    @staticmethod
    def init_webhooks(base_url):
        # Update inbound traffic via APIs to use the public-facing ngrok URL
        pass
        