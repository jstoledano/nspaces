from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'apps.blog'
    verbose_name = 'Blog'

    def ready(self):
        """Sobrepone en:
            Users system checks
            Users signal registration
        """
        pass
