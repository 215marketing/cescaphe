# -*- coding: utf-8 -*-

# Created on 2019-01-04
# author: 广州尚鹏，https://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Hr Department Chart Hierarchy, 员工部门多层级结构图',
    'version': '12.19.04.19',
    'author': 'Sunpop.cn',
    'category': 'Account',
    'website': 'https://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Chart Hierarchy Widget. Hierarchy Chart, Hierarchy Tree for multi level Parent Children relation tree.
    Free for category Hierarchy chart, stock Hierarchy chart. account chart.
    """,
    'description': """
This module extend to show a Hierarchy chart.
(N+1, N+2, direct subordinates)
image: image_field,
desc: descript_field,
direct_sub: children_field, must be one2many,
child_all_count: child_all_count field, count of direct and indirect children.
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'hr_org_chart',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/hr_department_views.xml',
        'views/contacts_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
