# -*- coding: utf-8 -*-

"""Top-level package for FacturArk."""

from .api import (build_invoice, build_credit_note, send_invoice,
                  verify_document, query_document, generate_qrcode)

__author__ = """Nubark"""
__email__ = 'info@nubark.com'
__version__ = '0.3.0'
