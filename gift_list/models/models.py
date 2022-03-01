# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    list_ids = fields.Many2many('gift_list.list',string="Lists")
    products_ids = fields.Many2many('gift_list.product',string="Products")
    comment_ids = fields.One2many('gift_list.comment',string="Comments", inverse_name='partner_id')
    # partner_ids = fields.Many2many('res.partner',string="Friends")

class List(models.Model):
    _name = 'gift_list.list'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    end_date = fields.Date(string="End date")
    partner_ids = fields.Many2many('res.partner',string="Partner")

    event_type = fields.Selection([
    	('1','Birthday'),
    	('2', 'St Valentines'),
    	('3', 'Christmas')], string="Event")

    product_ids = fields.Many2many('gift_list.product',string="Products")

class Product(models.Model):
    _name = 'gift_list.product'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    link = fields.Char(string="Link")
    reserved = fields.Boolean(string="Reserved")
    bought = fields.Boolean(string="Bought")
    list_id = fields.Many2one('gift_list.list',string="Lists")
    comment_ids = fields.Many2many('gift_list.comment',string="Comments")
    partner_ids = fields.Many2many('res.partner', string="Partner", related="list_id.partner_ids")

class Comment(models.Model):
    _name = 'gift_list.comment'

    partner_id = fields.Many2one('res.partner',string="Partner")
    product_id = fields.Many2one('gift_list.product',string="Product")
    comment = fields.Char(string="Comment")
