from django.views.generic import TemplateView
import os
import requests


class IndexView(TemplateView):
    """
    simple template view to define proxy_test page
    """
    template_name = "proxy_test/index.html"
    pegel_url = "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/KÖLN/W.json?includeCurrentMeasurement=true"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fetch pegel
        try:
            resp = requests.get(self.pegel_url)
            rhein_pegel = resp.json()['currentMeasurement']['value']
            context['status'] = 'success'
        except requests.exceptions.SSLError as e:
            rhein_pegel = 'n/a'
            context['status'] = f'SSL Proxy Zertifikat wurde nicht akzeptiert {e}'
        except requests.exceptions.RequestException as e:
            rhein_pegel = 'n/a'
            context['status'] = f'Anderer Fehler ist aufgetreten: {e}'
        context['proxy_url'] = os.environ.get('HTTPS_PROXY', 'none')
        context['requests_ca_bundle'] = os.environ.get('REQUESTS_CA_BUNDLE', 'none')
        context['pegelstand'] = rhein_pegel
        return context
