# -*- coding: utf-8 -*-

{
    "name"      : "Comprobante Electronico para Traslados (CE)",
    "version"   : "1.0",
    "author"    : "German Ponce Dominguez",
    "website"   : "https://www.argil.mx",
    "license"   : "OEEL-1",
    "category"  : "Localization/Mexico",
    "description": """

Comprobante Traslado
====================

Este modulo permite incorporar el CFDI de Traslado para la Facturación Electronica 3.3

""",
    
    "depends": [
        "l10n_mx_einvoice",
        ],
    "data"    : [
                 "account_invoice_view.xml",
                 "report_invoice_facturae.xml",
    ],
    "installable": True,
}
