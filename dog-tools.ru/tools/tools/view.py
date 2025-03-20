from django_filters.views import View
from django.shortcuts import render, redirect


class Test(View):
    def get(self, request, *args, **kwargs):
        test = request.get_host()
        print(test)
        data = {"test": test}
        return render(request, "tools/test.html", context=data)


class Robots(View):
    def get(self, request, *args, **kwargs):
        host = request.get_host()
        return render(request, "tools/robots.txt", context={"host": host})


class GeneralRedirect(View):
    def get(self, request, *args, **kwargs):
        host = request.get_host()
        return redirect("/", permanent=True)
