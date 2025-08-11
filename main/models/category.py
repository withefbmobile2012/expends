from main.models.base import *


class Category(BaseModel):
    name = models.CharField(max_length=100)
    order_num = models.PositiveIntegerField(default=0)
    used_times = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.name} {self.order_num}"

    class Meta:
        db_table = "categories"
        ordering = ("order_num",)