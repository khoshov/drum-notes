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

    one = models.BooleanField(default=False)
    two = models.BooleanField(default=False)
    three = models.BooleanField(default=False)
    four = models.BooleanField(default=False)
    five = models.BooleanField(default=False)
    six = models.BooleanField(default=False)
    seven = models.BooleanField(default=False)
    eight = models.BooleanField(default=False)
