from django.shortcuts import render

# Create your views here.
def css_files(request):
    return render(request,'template_html_files/basic.html')
