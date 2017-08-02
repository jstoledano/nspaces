from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'apps.blog'
    verbose_name = 'Blog'
    icon = '<i class="material-icons">art_track</i>'

    def ready(self):
        """Sobrepone en:
            Users system checks
            Users signal registration
        """
        pass
