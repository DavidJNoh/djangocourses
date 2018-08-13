from django.db import models

class Manager(models.Manager):
    def validator(self, postData):
        x = {}
        if len(postData['course_name']) < 6 :
            x['course_name']= "Course name must be more than 5 characters"
        if len(postData['course_name']) > 255 :
            x['course_name']= "Course name can not be more than 255 characters"
            
        if len(postData['desc']) < 16 :
            x['desc']= "Description must be more than 15 characters"
        if len(postData['desc']) > 255 :
            x['desc']= "Description can not be more than 255 characters"
        return x

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = Manager()
