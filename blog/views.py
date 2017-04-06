from django.shortcuts import render
from .models import BlogPost, Topic
# Create your views here.



# first page of the webseite
def home_view(request, *args, **kwargs):


	if kwargs:				# if topic in kwargs {'topic' : 'topic-of-ML'}
		topic = Topic.objects.get(title=kwargs['topic'])
		if topic.pk == 1:		# if someone comes at first page by pressing prev. button
			next_topic = Topic.objects.get(pk=topic.pk+1)
			prev_topic = None			
		else:
			try:		# for normal case
				next_topic = Topic.objects.get(pk=topic.pk+1)
				prev_topic = Topic.objects.get(pk=topic.pk-1)
			except:		# if the topic is the last one
				next_topic = None
				prev_topic = Topic.objects.get(pk=topic.pk-1)

	else:	# opening the first page of the website
		topic = Topic.objects.get(pk=1)
		next_topic = Topic.objects.get(pk=topic.pk+1)
		prev_topic = None

	posts = BlogPost.objects.filter(topic=topic)
	context = {

			'next_topic' : next_topic,
			'prev_topic' : prev_topic,
			'posts' 	 : posts,
			'topic' 	 : topic,
	}



	return render(request, 'blog/index.html', context)

def	google_seach_verify(request):
	return render(request, 'blog/google55865d30d084df3d.html')