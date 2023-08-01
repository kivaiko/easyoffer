from django.shortcuts import render


def mentors(request):
    return render(request, 'mentors.html')


def mentor(request, username):
    return render(request, 'mentor.html')