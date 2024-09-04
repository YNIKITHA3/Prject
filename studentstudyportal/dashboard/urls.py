from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('notes',views.notes,name="notes"),
    path('delete-note/<int:id>/', views.delete_note, name='delete_note'),
    path('homework',views.homework,name="homework"),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(),name="notes-detail"),
    path('todo',views.todo,name="todo"),
    path('update_todo/<int:pk>',views.update_todo,name="update-todo"),
    path('delete_todo/<int:pk>',views.delete_todo,name="delete-todo"),
    
]

#path('update_homework/<int:pk>',views.update_homework,name="update-homework"),