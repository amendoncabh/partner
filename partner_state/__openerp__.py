# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Partner State',
    'version': '9.0.1.0.0',
    'category': 'Base',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'base'
    ],
    'data': [
        'views/res_partner_state_field_view.xml',
        'views/menu.xml',
        'views/company_view.xml',
        'views/partner_view.xml',
        'security/partner_state_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/company_demo.xml',
        'demo/res.partner.state.field.csv'
    ],
    'installable': True,
}
