from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    variName = "Gazi Shah Al-Helaly"
    variAdds = "15/J, Mymensingh" 
    variAbout = { 'name':variName, 'adds':variAdds}
    return render(request, 'tmp-courses/about.html', variAbout)

def skill(request):
    variDesign = "Graphics Design"
    variMarketing = "Email Marketing"
    variOptimization = "Facebook, Instagram, Linkedin"
    variSkills = {'design':variDesign, 'marketing':variMarketing, 'optimization':variOptimization }
    return render(request, 'tmp-courses/skill.html',variSkills)