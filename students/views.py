from django.shortcuts import render, redirect
from .models import Student, Party, Movie
from .forms import StudentForm, PartyForm
from .services import QueryMovie

def create_student(request):
    if request.method == 'POST': 
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_dashboard(request, user_id):
    ind_student = Student.objects.get(pk=user_id)
    return render(request, 'students/student_dashboard.html', {'info': ind_student, 'student_parties': ind_student.parties.all()})

def create_party(request, user_id):
    if request.method == 'POST':
        form = PartyForm(request.POST)
        if form.is_valid():
            party = form.save(commit=False)  
            student = Student.objects.get(pk=user_id)
            party.save()  
            party.attendees.add(student)  
            party.save() 
            breakpoint()
            return redirect(f"/students/{user_id}/")
    return render(request, 'students/create_party.html', {'info': Student.objects.get(pk=user_id)})

def view_party(request, user_id, party_id):
    all_movies = Party.objects.get(pk=party_id).movies.all()
    return render(request, 'students/view_party.html', {'party_id': party_id, 'user_id': user_id, 'movies': all_movies, 'name': Party.objects.get(pk=party_id).name})

def search_movies(request):
    x = QueryMovie(request.GET['q'])
    movie_array = []
    for movie in x['results']:
        new = Movie.objects.create(name=movie['original_title'])
        movie_array.append(new)
    return render(request, 'students/search_movie.html', {'info': movie_array, 'party_id': request.GET['party_id'], 'user_id': request.GET['user_id']})    

def add_movie_to_party(request, user_id, party_id):
    party = Party.objects.get(pk=party_id)
    movie_to_add = Movie.objects.get(pk=request.GET['movie_id'])
    party.movies.add(movie_to_add)
    party.save()
    return redirect(f'/students/{user_id}/parties/{party_id}/')
