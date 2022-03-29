# 1- create a new django project using our containing folder (blog)
# 2- create and install 2 apps: pages & post
# 3- create a home page and an about page and set them up so they are accessible at:
#     3.1- http://127.0.0.1:8000/ -> home
#     3.2- http://127.0.0.1800/about -> about
# 4- add a posts app with a model that supports:
#     4.1- title, author, body and created_on
# 5- make any neccessary migrations
# 6- run those migrations
# 7 register the new model on the admin panel
# 8 create 3 blog posts

from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)