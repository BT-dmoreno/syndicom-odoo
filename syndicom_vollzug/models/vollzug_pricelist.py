# -*- coding: utf-8 -*-
from odoo import models, fields

class SyndicomVollzugPricelist(models.Model):
    _name = 'syndicom.vollzug.pricelist'
    _description = 'Vollzug Preisliste'

    # TODO: compute aktiv aufgrund von date_from und date_to
    active = fields.Boolean(string='Aktiv')

    gav_id = fields.Many2one(comodel_name='res.partner', string='GAV Partner')
    category = fields.Selection(string='Beitrag für', selection=[('verband', 'Verbandsmitglieder'), ('ev', 'Einzelverbandsmitglieder'), ('nicht', 'Nicht-Verband')])
    logic = fields.Selection(string='Berechnungslogik', selection=[('absolut', 'Absolute Beträge'), ('prozent', 'Prozentual'),])
    
    amount_tz = fields.Float(string='Teilzeit')
    amount_vz = fields.Float(string='Vollzeit')
    amount_lernend = fields.Float(string='Lernende')
    
    amount_ag_tz = fields.Float(string='AG-Beitrag Teilzeit')
    amount_ag_vz = fields.Float(string='AG-Beitrag Vollzeit')
    amount_ag_lernend = fields.Float(string='AG-Beitrag Lernende')
    
    
    discount_max = fields.Float(string='Rabatt Max.')
    discount = fields.Float(string='Rabatt in %')
    
    date_from = fields.Date(string='Gültig ab')
    date_to = fields.Date(string='Gültig bis')


    


    
    
    




    """


    GAV         category
    CC          * Verbands
    CC          * EV
    CC          * Lernende


    """