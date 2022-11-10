from django.db import models


def default_urls():
    return {
        "work": "",
        "dou": "",
        "djinni": ""
    }


class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Назва міста',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Назва міста'
        verbose_name_plural = 'Назва міст'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Мова програмування',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Мова програмування'
        verbose_name_plural = 'Мова програмування'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250,
                             verbose_name='Заголовок вакансії')
    company = models.CharField(max_length=250,
                               verbose_name='Компанія')
    description = models.TextField(verbose_name='Опис вакансії')
    city = models.ForeignKey('City',
                             on_delete=models.CASCADE,
                             verbose_name='Місто')
    language = models.ForeignKey('Language',
                                 on_delete=models.CASCADE,
                                 verbose_name='Мова програмування')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'
        ordering = ['-timestamp']


    def __str__(self):
        return self.title


class Error(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()


class Url(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name='Місто')
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='Мова програмування')
    url_data = models.JSONField(default=default_urls)

    class Meta:
        unique_together = ("city", "language")

    def __str__(self):
        return f"{self.city} - {self.language}"
