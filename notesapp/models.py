from djongo import models as djongo_models # type: ignore
from django.db import models # type: ignore
import uuid

# User model
class User(djongo_models.Model):
    user_id = djongo_models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


# Notes model
class Notes(djongo_models.Model):
    note_id = djongo_models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note_title = models.CharField(max_length=200)
    note_content = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    user = djongo_models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.note_title
