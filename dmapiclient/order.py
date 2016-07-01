from __future__ import unicode_literals
from .audit import AuditTypes
from .base import BaseAPIClient, logger, make_iter_method
from .errors import HTTPError


class OrderAPIClient(BaseAPIClient):
    def init_app(self, app):
        self.base_url = app.config['DM_DATA_API_URL']
        self.auth_token = app.config['DM_DATA_API_AUTH_TOKEN']

    # Orders

    def create_order(self, order):
        return self._post("/orders", data=order)
