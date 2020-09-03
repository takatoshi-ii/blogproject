from django.db import models


# Create your models here.
class SampleModel(models.Model):
	title = models.CharField(max_length=100)
	number = models.IntegerField()
	
CATEGOLY = (('busuness','ビジネス'),('life','生活'),('other','その他'))

class BlogModel(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	postdata = models.DateField(auto_now_add = True)
	category = models.CharField(
		max_length = 50,
		choices = CATEGOLY
	)