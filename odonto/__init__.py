"""
odonto - Our Opal Application
"""
from opal.core import application, menus

class Application(application.OpalApplication):
    javascripts   = [
        'js/openodonto/routes.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/openodonto/flow.js',
    ]

    @classmethod
    def get_menu_items(cls, user=None):
        menu_items = [
            menus.MenuItem(
                href="/pathway/#/add_patient",
                display="Add Patient",
                icon="fa fa-user",
            ),
            menus.MenuItem(
                href="/pathway/#/fp17",
                display="File FP17 Claim",
                icon="fa fa-money",
            )
        ]
        return menu_items