from django.db import models

class SearchCache(models.Model):
    search_type = models.CharField(max_length=100)
    search_text = models.CharField(max_length=255)
    cached_data = models.JSONField()
    cached_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.search_type} - {self.search_text}'
