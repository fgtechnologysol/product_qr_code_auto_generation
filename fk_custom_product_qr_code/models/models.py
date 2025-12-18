# # -*- coding: utf-8 -*-
#
# from odoo import models, fields, api
# import qrcode
# import base64
# from io import BytesIO
#
#
# def generate_qr_code(url):
#     """Generate QR code from URL and return as base64 encoded image"""
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(url)
#     qr.make(fit=True)
#
#     img = qr.make_image(fill_color="black", back_color="white")
#     buffer = BytesIO()
#     img.save(buffer, format='PNG')
#     buffer.seek(0)
#     img_base64 = base64.b64encode(buffer.read())
#     return img_base64
#
#
# class ProductTemplateInherit(models.Model):
#     _inherit = 'product.template'
#
#     qr_image = fields.Binary(string='Website QR Code', store=True, readonly=True)
#     image_name = fields.Char(string='Product Qr Code', compute='generate_image_name')
#     qr_url = fields.Char(string='Qr Url', compute='_compute_qr_url', store=True)
#
#     @api.depends('name', 'default_code')
#     def generate_image_name(self):
#         for record in self:
#             if record.name or record.default_code:
#                 record.image_name = str(record.default_code or '') + ' download ' + (record.name or '')
#             else:
#                 record.image_name = ''
#
#     @api.depends('website_url')
#     def _compute_qr_url(self):
#         for rec in self:
#             if rec.website_url:
#                 base_url = 'https://www.uzstore.com'
#                 base_url += rec.website_url
#                 rec.qr_url = base_url
#             else:
#                 rec.qr_url = False
#
#     @api.model_create_multi
#     def create(self, vals_list):
#         """Override create to generate QR code when product is created"""
#         records = super(ProductTemplateInherit, self).create(vals_list)
#         for record in records:
#             record._generate_qr_code_on_create()
#         return records
#
#     def write(self, vals):
#         """Override write to regenerate QR code when website_url changes"""
#         res = super(ProductTemplateInherit, self).write(vals)
#         if 'website_url' in vals:
#             for record in self:
#                 record._generate_qr_code_on_create()
#         return res
#
#     def _generate_qr_code_on_create(self):
#         """Generate QR code for the product"""
#         for record in self:
#             if record.website_url:
#                 base_url = 'https://www.uzstore.com' + record.website_url
#                 record.qr_image = generate_qr_code(base_url)
#             else:
#                 record.qr_image = False
#
#     def action_regenerate_qr_code(self):
#         """Manual action to regenerate QR code"""
#         self._generate_qr_code_on_create()
#
#     def download_image_field_prod_temp(self):
#         """Download QR code image"""
#         return {
#             'name': self.default_code or self.name,
#             'type': 'ir.actions.act_url',
#             'url': '/web/image?model=product.template&id={}&field=qr_image&download=true&filename={}'.format(
#                 self.id,
#                 self.image_name or 'qr_code.png'
#             ),
#             'target': 'self',
#         }
#
#
# class ProductProdInherit(models.Model):
#     _inherit = 'product.product'
#
#     qr_image = fields.Binary(string='Website QR Code', store=True, readonly=True)
#     qr_url = fields.Char(string='Qr Url', compute='_compute_qr_url', store=True)
#
#     @api.depends('website_url')
#     def _compute_qr_url(self):
#         for rec in self:
#             if rec.website_url:
#                 base_url = 'https://www.uzstore.com'
#                 base_url += rec.website_url
#                 rec.qr_url = base_url
#             else:
#                 rec.qr_url = False
#
#     @api.model_create_multi
#     def create(self, vals_list):
#         """Override create to generate QR code when product variant is created"""
#         records = super(ProductProdInherit, self).create(vals_list)
#         for record in records:
#             record._generate_qr_code_on_create()
#         return records
#
#     def write(self, vals):
#         """Override write to regenerate QR code when website_url changes"""
#         res = super(ProductProdInherit, self).write(vals)
#         if 'website_url' in vals:
#             for record in self:
#                 record._generate_qr_code_on_create()
#         return res
#
#     def _generate_qr_code_on_create(self):
#         """Generate QR code for the product variant"""
#         for record in self:
#             if record.website_url:
#                 base_url = 'https://www.uzstore.com' + record.website_url
#                 record.qr_image = generate_qr_code(base_url)
#             else:
#                 record.qr_image = False
#
#     def action_regenerate_qr_code(self):
#         """Manual action to regenerate QR code"""
#         self._generate_qr_code_on_create()
#
#     def download_image_field_prod_temp(self):
#         """Download QR code image"""
#         return {
#             'name': self.default_code or self.name,
#             'type': 'ir.actions.act_url',
#             'url': '/web/image?model=product.product&id={}&field=qr_image&download=true&filename={}'.format(
#                 self.id,
#                 self.image_name or 'qr_code.png'
#             ),
#             'target': 'self',
#         }


# -*- coding: utf-8 -*-

from odoo import models, fields, api
import qrcode
import base64
from io import BytesIO


def generate_qr_code(url):
    """Generate QR code from URL and return as base64 encoded image"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read())
    return img_base64


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    qr_image = fields.Binary(string='Website QR Code', store=True, readonly=True)
    image_name = fields.Char(string='Product Qr Code', compute='generate_image_name')
    qr_url = fields.Char(string='Qr Url', compute='_compute_qr_url', store=True)

    @api.depends('name', 'default_code')
    def generate_image_name(self):
        for record in self:
            if record.name or record.default_code:
                record.image_name = str(record.default_code or '') + ' ' + (record.name or '') + '_qr_code'
            else:
                record.image_name = 'product_qr_code'

    @api.depends('website_url')
    def _compute_qr_url(self):
        """Get dynamic base URL from system parameters"""
        for rec in self:
            if rec.website_url:
                # Get base URL from system parameter or website settings
                base_url = rec.env['ir.config_parameter'].sudo().get_param('web.base.url')
                rec.qr_url = base_url + rec.website_url
            else:
                rec.qr_url = False

    @api.model_create_multi
    def create(self, vals_list):
        """Override create to generate QR code when product is created"""
        records = super(ProductTemplateInherit, self).create(vals_list)
        for record in records:
            record._generate_qr_code_on_create()
        return records

    def write(self, vals):
        """Override write to regenerate QR code when website_url changes"""
        res = super(ProductTemplateInherit, self).write(vals)
        if 'website_url' in vals:
            for record in self:
                record._generate_qr_code_on_create()
        return res

    def _generate_qr_code_on_create(self):
        """Generate QR code for the product"""
        for record in self:
            if record.website_url:
                # Get dynamic base URL from system parameters
                base_url = record.env['ir.config_parameter'].sudo().get_param('web.base.url')
                full_url = base_url + record.website_url
                record.qr_image = generate_qr_code(full_url)
            else:
                record.qr_image = False

    def action_regenerate_qr_code(self):
        """Manual action to regenerate QR code"""
        self._generate_qr_code_on_create()

    def download_image_field_prod_temp(self):
        """Download QR code image"""
        return {
            'name': self.default_code or self.name,
            'type': 'ir.actions.act_url',
            'url': '/web/image?model=product.template&id={}&field=qr_image&download=true&filename={}'.format(
                self.id,
                self.image_name or 'qr_code.png'
            ),
            'target': 'self',
        }


class ProductProdInherit(models.Model):
    _inherit = 'product.product'

    qr_image = fields.Binary(string='Website QR Code', store=True, readonly=True)
    qr_url = fields.Char(string='Qr Url', compute='_compute_qr_url', store=True)

    @api.depends('website_url')
    def _compute_qr_url(self):
        """Get dynamic base URL from system parameters"""
        for rec in self:
            if rec.website_url:
                # Get base URL from system parameter or website settings
                base_url = rec.env['ir.config_parameter'].sudo().get_param('web.base.url')
                rec.qr_url = base_url + rec.website_url
            else:
                rec.qr_url = False

    @api.model_create_multi
    def create(self, vals_list):
        """Override create to generate QR code when product variant is created"""
        records = super(ProductProdInherit, self).create(vals_list)
        for record in records:
            record._generate_qr_code_on_create()
        return records

    def write(self, vals):
        """Override write to regenerate QR code when website_url changes"""
        res = super(ProductProdInherit, self).write(vals)
        if 'website_url' in vals:
            for record in self:
                record._generate_qr_code_on_create()
        return res

    def _generate_qr_code_on_create(self):
        """Generate QR code for the product variant"""
        for record in self:
            if record.website_url:
                # Get dynamic base URL from system parameters
                base_url = record.env['ir.config_parameter'].sudo().get_param('web.base.url')
                full_url = base_url + record.website_url
                record.qr_image = generate_qr_code(full_url)
            else:
                record.qr_image = False

    def action_regenerate_qr_code(self):
        """Manual action to regenerate QR code"""
        self._generate_qr_code_on_create()

    def download_image_field_prod_temp(self):
        """Download QR code image"""
        return {
            'name': self.default_code or self.name,
            'type': 'ir.actions.act_url',
            'url': '/web/image?model=product.product&id={}&field=qr_image&download=true&filename={}'.format(
                self.id,
                self.image_name or 'qr_code.png'
            ),
            'target': 'self',
        }