# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.tools.translate import _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    lte2_fixed = fields.Boolean('Fixed Layout')
    lte2_collapse = fields.Boolean('Sidebar Collapse', help="Default sidebar is collapsed")
    lte2_skin = fields.Selection([
        ('blue', 'Blue'),
        ('black', 'Black'),
        ('purple', 'Purple'),
        ('green', 'Green'),
        ('red', 'Red'),
        ('yellow', 'Yellow'),
        
        ('blue-light', 'Blue Light'),
        ('black-light', 'Black Light'),
        ('purple-light', 'Purple Light'),
        ('green-light', 'Green Light'),
        ('red-light', 'Red Light'),
        ('yellow-light', 'Yellow Light'),
    ], string="Skin")


    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        xml_o = self.env['ir.model.data'].sudo().xmlid_to_object
        # ACTIVE SKIN
        # skin_id = self.env['ir.ui.view'].sudo().search([('name','=','AdminLTE2 Skin')]).id
        # skin_name = self.env['ir.model.data'].sudo().search([('res_id','=',skin_id),('model','=','ir.ui.view')]).name        
        # skin = skin_name[10:] if skin_name else 'blue'
        skins = []
        skin = ''
        skin_ids = self.env['ir.ui.view'].sudo().search([('name','=','AdminLTE2 Skin')]).ids
        for o_skin in self.env['ir.model.data'].sudo().search([('res_id','in',skin_ids),('model','=','ir.ui.view')]):
            # skin += o_skin.name[10:]
            skins.append( o_skin.name[10:] )
        
        print 'SKINS-'*100, skins
        if skins[0] == 'light': 
            skins= skins[1:] + ['light']
        skin = '-'.join(skins)
        
        res.update(
            lte2_skin= skin,
            lte2_fixed = xml_o('web_theme_lte2.lte2_fixed', True).active,
            lte2_collapse = xml_o('web_theme_lte2.lte2_collapse', True).active,
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        xml_o = self.env['ir.model.data'].sudo().xmlid_to_object
        
        # set_param('auth_signup.template_user_id', repr(self.auth_signup_template_user_id.id))
        # ACTIVE SKIN
        skin = self.lte2_skin
        
        
        xml_o('web_theme_lte2.lte2_fixed', True).active = self.lte2_fixed
        xml_o('web_theme_lte2.lte2_collapse', True).active = self.lte2_collapse
        # xml_o('web_theme_lte2.lte2_skin_blue', True).active = skin == 'blue'
        # xml_o('web_theme_lte2.lte2_skin_black', True).active = skin == 'black'
        # xml_o('web_theme_lte2.lte2_skin_purple', True).active = skin == 'purple'
        # xml_o('web_theme_lte2.lte2_skin_green', True).active = skin == 'green'
        # xml_o('web_theme_lte2.lte2_skin_yellow', True).active = skin == 'yellow'
        # xml_o('web_theme_lte2.lte2_skin_red', True).active = skin == 'red'
        for color in 'blue black purple green yellow red light'.split(' '):
            xml_o('web_theme_lte2.lte2_skin_'+color, True).active = color in skin # 'red' in 'red-light'
        

