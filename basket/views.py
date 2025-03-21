from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic


class CreateTaskView(generic.CreateView):
    template_name = 'basket/create_task.html'
    form_class = forms.TaskForm
    success_url = '/task_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTaskView, self).form_valid(form=form)


class TaskListView(generic.ListView):
    template_name = 'basket/task_list.html'
    context_object_name = 'task'
    model = models.TodoList

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class TaskDetailView(generic.DetailView):
    template_name = 'basket/task_detail.html'
    context_object_name = 'task_id'

    def get_object(self, *args, **kwargs):
        task_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoList, id=task_id)


class UpdateTaskView(generic.UpdateView):
    template_name = 'basket/update_task.html'
    form_class = forms.TaskForm
    success_url = '/task_list/'

    def get_object(self, *args, **kwargs):
        task_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoList, id=task_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTaskView, self).form_valid(form=form)


class DeleteTaskView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/task_list/'

    def get_object(self, *args, **kwargs):
        task_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoList, id=task_id)
