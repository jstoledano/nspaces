from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'
    verbose_name = "Users"

    def ready(self):
        """Sobrepone en:
            Users system checks
            Users signal registration
        """
        pass