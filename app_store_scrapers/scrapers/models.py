from django.db import models
from django.contrib.postgres.fields import ArrayField
 
class Keyword(models.Model):
    text = models.CharField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class IOSKeywordObservation(models.Model):
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    popularity = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class IOSCategory(models.Model):
    name = models.CharField(max_length=30)
    app_store_id = models.IntegerField(unique=True)
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)


class IOSDeveloper(models.Model):
    app_store_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=250)
    store_url = models.CharField(max_length=250)
    site_url = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @staticmethod
    def api_mapping():
        return {
            'app_store_id': 'artistId',
            'name': 'sellerName',
            'store_url': 'artistViewUrl',
            'site_url': 'sellerUrl'
        }

class IOSApp(models.Model):

    name = models.CharField(max_length=56)
    platform = models.CharField(max_length=10)
    minimum_os_version = models.CharField(max_length=4)
    developer_id = models.ForeignKey(IOSDeveloper, on_delete=models.CASCADE)

    store_id = models.IntegerField(unique=True)

    currency = models.CharField(max_length=4)
    content_advistory_rating = models.CharField(max_length=4)

    category_ids = ArrayField(models.IntegerField())
    category_names = ArrayField(models.CharField(max_length=24))

    supported_devices = ArrayField(models.CharField(max_length=36))
    language_codes = ArrayField(models.CharField(max_length=4))

    icon_100 = models.ImageField(height_field=100, width_field=100)
    icon_512 = models.ImageField(height_field=512, width_field=512)
    bundle_id = models.CharField(max_length=120)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @staticmethod
    def api_mapping():
        return {
            'name': 'sellerName',
            'minimum_os_version': 'minimumOsVersion',
            'store_id': 'trackId',
            'currency': 'currency',
            'content_advistory_rating': 'contentAdvisoryRating',
            'category_names': 'genres',
            'supported_devices': 'supportedDevices',
            'language_codes': 'languageCodesISO2A',
            'icon_100': 'artworkUrl100',
            'icon_512': 'artworkUrl512',
            'bundle_id': 'bundleId'
        }

class IOSAppObservation(models.Model):

    description = models.TextField()
    release_date = models.DateField()
    overall_average_rating = models.FloatField()

    current_version_average_rating = models.FloatField()
    current_version_release_date = models.DateField()
    release_notes = models.TextField()

    results = models.IntegerField()
    ranking = models.IntegerField()


    ios_app_id = models.ForeignKey(IOSApp, on_delete=models.CASCADE)
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    screenshot_urls = ArrayField(models.CharField(max_length=256))
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('created', 'ios_app_id')

    @staticmethod
    def api_mapping():
        return {
            'description' : 'description',
            'release_date': 'releaseDate',
            'overall_average_rating': 'averageUserRating',
            'current_version_average_rating': 'averageUserRatingForCurrentVersion',
            'current_version_release_date': 'currentVersionReleaseDate',
            'release_notes': 'releaseNotes',
            'screenshot_urls': 'screenshotUrls'
        }