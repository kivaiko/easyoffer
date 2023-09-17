


class AbstractQuestion(models.Model):
    class Meta:
        db_table = 'questions'
        abstract = True

    title = models.CharField(max_length=255)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    grade = models.CharField(max_length=100, choices=settings.GRADES, default='Не указан')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('question', args=[self.id])


class Rating(models.Model):
    class Meta:
        db_table = 'ratings'

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(default=1)
    position = models.IntegerField(default=1000)
    public = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.profession}, {self.question}"