from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from datetime import date

all_posts = [
    {
        "slug":"AI-Techs",
        "image":"AI.png",
        "author":"Darshil Patel",
        "date": date(2025,6,24),
        "title": "AI-awarness",
        "excerpt": "AI is rapidly advancing and becoming a core part of everyday life. Today, Generative AI tools like ChatGPT, Midjourney, and Sora are helping people write, design, and create content with ease. In tech and business, Large Language Models (LLMs) and machine learning platforms are automating customer service, fraud detection, and data analysis.Computer vision is powering self-driving cars and facial recognition, while AI in healthcare is improving disease detection and drug development. Meanwhile, AI in education is growing through personalized learning apps and smart tutors. With continuous breakthroughs, AI is not just the future — it’s actively transforming industries right now",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem fuga nam voluptate tempore reiciendis ut sit quia ipsum repellat, nobis quae aut ducimus amet, natus nemo maiores temporibus. Neque, labore?
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit."""
    },
    {
        "slug":"Morden-AI-Science",
        "image":"mountains.jpg",
        "author":"Darshil Patel",
        "date": date(2025,6,21),
        "title": "Tech-AI-One",
        "excerpt": "Modern AI science is a blend of serious innovation and surprising fun. Today’s AI can write songs, drive cars, diagnose diseases, and even paint like Picasso—yet it might still call a dog a “fluffy potato.” Behind the advanced algorithms and deep learning models is a field constantly evolving, where machines learn from data, improve over time, and sometimes create unexpected results. It’s a fascinating mix of logic, creativity, and the occasional comedy of errors—proving that the journey to artificial intelligence is as entertaining as it is groundbreaking.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem fuga nam voluptate tempore reiciendis ut sit quia ipsum repellat, nobis quae aut ducimus amet, natus nemo maiores temporibus. Neque, labore?"""
    },
    {
        "slug":"Funny-thing-of-ai",
        "image":"funny.png",
        "author":"Darshil Patel",
        "date": date(2025,6,21),
        "title": "Funny - AI",
        "excerpt": "AI can be incredibly smart—but sometimes, it's hilariously offbeat. From chatbots that argue with you over whether you're a sandwich, to voice assistants playing heavy metal when you ask for meditation music, AI has its funny bone moments. One bot even tried to flirt with a toaster during a simulation (no sparks, thankfully). Whether it's writing weird poems about broccoli or mistaking your cat for a loaf of bread, AI keeps proving that while it’s clever, it’s still learning... one awkward moment at a time!",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem fuga nam voluptate tempore reiciendis ut sit quia ipsum repellat, nobis quae aut ducimus amet, natus nemo maiores temporibus. Neque, labore?"""
    }
]

def get_date(all_posts):
    return all_posts['date']

def home(request):
    sorted_post = sorted(all_posts,key=get_date)
    latest_post = sorted_post[-3:]
    temp = loader.get_template('home.html')
    return HttpResponse(temp.render({
        "posts": latest_post
    }))

def posts(request):
    temp = loader.get_template('all-post.html')
    return HttpResponse(temp.render({
        "all_posts": all_posts
    }))

def post_details(request,slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    temp = loader.get_template('post-details.html')
    return HttpResponse(temp.render({
        "post": identified_post
    }))

