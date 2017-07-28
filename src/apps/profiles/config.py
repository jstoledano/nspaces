from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.profiles'
    verbose_name = 'Usuarios y Perfiles'

    def ready(self):
        """Sobrepone en:
            Users system checks
            Users signal registration
        """
        pass
