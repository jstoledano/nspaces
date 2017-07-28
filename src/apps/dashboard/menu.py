from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.menu import items, Menu


class CustomMenu(Menu):
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Panel de Control'), reverse('admin:index')),
            items.Bookmarks(),
            items.AppList(
                _('Aplicaciones'),
                exclude=('django.contrib.*', 'apps.profiles.models.User')
            ),
            items.AppList(
                _('Gestión del sitio'),
                models=('django.contrib.*', 'apps.profiles.models.User')
            )
        ]

    def init_with_context(self, context):
        return super(CustomMenu, self).init_with_context(context)
