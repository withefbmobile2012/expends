from main.models.base import *


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "categories"
        ordering = ("name",)