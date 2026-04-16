{
    'name': 'Project Management Custom',
    'version': '1.0.0',
    'summary': 'Module for managing employee projects',
    'description': """This module allows you to manage employee projects""",
    'depends': ['hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/hr_employee_view.xml'
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}