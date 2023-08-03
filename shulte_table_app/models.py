from django.db import models

class ShulteTable(models.Model):
    size = models.PositiveIntegerField()
    table_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shulte Table ({self.size}x{self.size})"
