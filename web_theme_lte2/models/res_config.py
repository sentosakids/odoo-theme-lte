# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.tools.translate import _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    lte2_skin = fields.Selection([
        ('blue', 'On invitation (blue) <span style="background:blue"> TAG </span>'),
        ('red', 'Free sign up (red)'),
    ], string="Skin")


    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        # xml_o = self.env['ir.model.data'].sudo().xmlid_to_object
        # ACTIVE SKIN
        skin_id = self.env['ir.ui.view'].sudo().search([('name','=','AdminLTE2 Skin')]).id
        skin_name = self.env['ir.model.data'].sudo().search([('res_id','=',skin_id),('model','=','ir.ui.view')]).name        
        skin = skin_name[10:]
        
        
        res.update(
            lte2_skin= skin,
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        # set_param('auth_signup.template_user_id', repr(self.auth_signup_template_user_id.id))
        # ACTIVE SKIN
        skin = self.lte2_skin
        
        xml_o = self.env['ir.model.data'].sudo().xmlid_to_object
        xml_o('web_theme_lte2.lte2_skin_blue', True).active = skin == 'blue'
        xml_o('web_theme_lte2.lte2_skin_red', True).active = skin == 'red'
        

