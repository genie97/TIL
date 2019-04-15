from django.db import models

class Task(models.Model): # Our database model is called Task
    TODO = 0
    DONE = 1

    STATUS_CHOICES = ( # We create a tuple of status choices
        (TODO, 'To do'),
        (DONE, 'Done')
    )

    description = models.CharField(max_length=255) # The tasks description is limited to 255 characters
    status = models.IntegerField(choices=STATUS_CHOICES, default=TODO) # The task's status, default status = TODO

