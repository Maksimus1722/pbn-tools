from django_filters.views import View
from django.shortcuts import render

class Test(View):
    def get(self, request, *args, **kwargs):
        test=request.get_host()
        print(test)
        data={"test":test}
        return render(request, "tools/test.html", context=data)