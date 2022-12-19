from django.db import models

class EmailSubscription(models.Model):
    email = models.EmailField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.email)

class Newsletter(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class FAQ(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class TermsCondition(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1500, blank=False)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
