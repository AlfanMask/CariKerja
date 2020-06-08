from django.shortcuts import render
from django.http import HttpResponse


posts = [
	{
		'title' : 'Web Developer',
		'author' : 'PT Citra Nusantara',
		'date' : '8 Juni 2020',
		'content' : 'Dibutuhkan seorang web developer yang berkompeten,Dibutuhkan seorang web developer yang berkompeten,Dibutuhkan seorang web developer yang berkompeten,'
	} for i in range(20)
]


def home(request):
	context = {
		'posts' : posts
	}
	return render(request,'blog/home.html',context)

def login(request):
	return render(request,'blog/login.html',{'title':'Login'})

def signup(request):
	return render(request,'blog/signup.html',{'title':'Sign Up'})