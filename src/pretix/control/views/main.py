from django.shortcuts import render
from django.views.generic import ListView

from pretix.base.models import Event


class EventList(ListView):
    model = Event
    context_object_name = 'events'
    paginate_by = 30
    template_name = 'pretixcontrol/events/index.html'

    def get_queryset(self):
        return Event.objects.current.filter(
            permitted__id__exact=self.request.user.pk
        ).prefetch_related(
            "organizer",
        )


def index(request):
    return render(request, 'pretixcontrol/base.html', {})
