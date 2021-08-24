from django.db import models


class Snippet(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('snippets:detail', kwargs={'pk': self.pk})


class Beat(models.Model):
    snippet = models.ForeignKey(Snippet, models.CASCADE, related_name='beats')


class Hihat(models.Model):
    beat = models.OneToOneField(Beat, models.CASCADE)


class Snare(models.Model):
    beat = models.OneToOneField(Beat, models.CASCADE)


class Kick(models.Model):
    beat = models.OneToOneField(Beat, models.CASCADE)


class Pattern(models.Model):
    hihat = models.OneToOneField(Hihat, models.CASCADE, blank=True, null=True)
    snare = models.OneToOneField(Snare, models.CASCADE, blank=True, null=True)
    kick = models.OneToOneField(Kick, models.CASCADE, blank=True, null=True)

    one = models.BooleanField()
    two = models.BooleanField()
    three = models.BooleanField()
    four = models.BooleanField()
    five = models.BooleanField()
    six = models.BooleanField()
    seven = models.BooleanField()
    eight = models.BooleanField()
