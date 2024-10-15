from django.db import models


class CardData(models.Model):
    article = models.CharField(primary_key=True)
    card_data = models.JSONField()
    price_history_data = models.JSONField()
    info_data = models.JSONField()
