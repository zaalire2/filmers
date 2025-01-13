from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    image = models.ImageField(upload_to='films/', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_average_rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return None
        return sum(review.rating for review in reviews) / reviews.count()

class Review(models.Model):
    film = models.ForeignKey(Film, related_name="reviews", on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user}: {self.comment} ({self.rating}/5)"
