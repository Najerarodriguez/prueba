from odoo import models, fields, api
from datetime import datetime, timedelta


class SitesTelyman(models.Model):
    _name = 'sites.telyman'