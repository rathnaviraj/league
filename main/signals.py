from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """
    Function to listen login signal and trigger the record login stats for any user
    """
    user.record_login()


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    """
    Function to listen logout signal and trigger the record logout stats for any user
    """
    user.record_logout()
