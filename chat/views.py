from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView
from django.contrib import messages

# Create your views here.
from .models import ChatMessage


def chatMessageView(request):
	queryset = ChatMessage.objects.all()
	if request.method == 'POST':
		message = request.POST.get('message')
		ChatMessage.objects.create(message=message, author=request.user, author_id=request.user.id)
		messages.success(request, f'Сообщение успешно добавлено!')
		return redirect('chat')
	
	context = {'object_list': queryset}
	return render(request, 'chat/chat.html', context)
