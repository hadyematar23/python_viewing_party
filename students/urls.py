from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_student),
    path('<int:user_id>/', views.student_dashboard), 
    path('<int:user_id>/parties/create/', views.create_party),
    path('<int:user_id>/parties/<int:party_id>/', views.view_party), 
    path('<int:user_id>/parties/<int:party_id>/add_movie/', views.add_movie_to_party)
]
# <a href="/students/{{user_id}}/parties/{{party_id}}/{{movie}}"><button>Add {{movie.original_title}} to this viewing party! </button></a>