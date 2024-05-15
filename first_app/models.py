from django.db import models

# Create your models here.
class Musician(models.Model):
    #id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    instrument  = models.CharField(max_length = 100)

    def _str_(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    #id = models.AutoField(primary_key = True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()

    rating = (
        (1, "Worst"),
        (1, "Bad"),
        (1, "Not Bad"),
        (1, "Good"),
        (1, "Excellent"),
    )

    num_starts = models.IntegerField(choices = rating)

    #mysql table name change for the model 
    # class Meta:
    #     db_table = "album"

    def _str_(self):
        return self.name + ", Rating: " + str(self.num_starts)