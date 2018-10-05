
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # age = models.PositiveIntegerField(default=0)
    pass  # Per default setting, No added fields required

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
        # return self.first_name
