from django.views.generic import TemplateView
from django.shortcuts import render
from starships.search import all_starships

class HomeView(TemplateView):
    """
    This class defines the behavior for the Home Screen.
    """

    TEMPLATE_NAME = "home.html"

    def get(self, request, *args, **kwargs):
        context = locals()

        mglt = request.GET.get('mglt', False)
        mglt = int(mglt) if mglt else 0
        context['mglt'] = mglt

        startships = []
        for startship in all_starships():
            try:
                startship['xjumps'] = mglt / int(startship.get('MGLT'))
            except ValueError:
                if startship.get('MGLT') == 'unknown':
                    startship['xjumps'] = 'unknown'
            startships.append(startship)

        context['starships'] = startships

        return render(template_name=self.TEMPLATE_NAME,
                      context=context,
                      request=request)
