from django.db import models

import main.models as model


class Dashboard(model.BaseModel):
    filter_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.filter_name

    class Meta:
        db_table = "dashboard"
        ordering = ("filter_name",)