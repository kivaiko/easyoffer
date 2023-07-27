from django.shortcuts import render, redirect


def mentors(request):
    return render(request, 'mentors.html')


def mentor(request, username):
    return render(request, 'mentor.html')