from copyreg import dispatch_table

from django.db.models.signals import post_save
from django.dispatch import receiver

from movies.models import SearchTerm
from movies.tasks import notify_of_new_search_term


@receiver(post_save, sender=SearchTerm, dispatch_uid='search_term_saved')
def search_term_saved(sender, instance, created, **kwargs):
    notify_of_new_search_term.delay(instance.term)
    # if created:
    #     print(f'A new SearchTerm was created: "{instance.term}"')