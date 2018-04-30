# Python
import os
# Lib
from appium import webdriver
import selenium.webdriver.common.keys as keys
from celery import Celery
from celery.schedules import crontab
from django.apps import apps, AppConfig
from django.conf import settings

if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # pragma: no cover


app = Celery('app_store_scrapers')


class CeleryConfig(AppConfig):
    name = 'app_store_scrapers.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        # Using a string here means the worker will not have to
        # pickle the object when using Windows.
        app.config_from_object('django.conf:settings')
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)

        if hasattr(settings, 'RAVEN_CONFIG'):
            # Celery signal registration

            from raven import Client as RavenClient
            from raven.contrib.celery import register_signal as raven_register_signal
            from raven.contrib.celery import register_logger_signal as raven_register_logger_signal


            raven_client = RavenClient(dsn=settings.RAVEN_CONFIG['dsn'])
            raven_register_logger_signal(raven_client)
            raven_register_signal(raven_client)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')  # pragma: no cover

@app.task
def test(arg):
    print(arg)

@app.task
def appium_scrape_trending_keywords():
    '''
    xpaths:
    https://trello.com/c/wXtZ4tZT/1-app-store-xpath-selectors
    '''
    desired_capabilities={
        'bundleId': 'com.apple.AppStore',
        'platformName': 'iOS',
        'platformVersion': '11.3',
        'deviceName': 'iPhone 6',
        'udid': settings.SCRAPER_DEVICE_UDID,
        'xcodeOrgId': settings.SCRAPER_DEVELOPER_TEAM_ID,
        'xcodeSigningId': 'iPhone Developer',
        'updatedWDABundleId': settings.SCRAPER_DEVELOPER_TEAM
    }
    driver = webdriver.Remote(
        f'{settings.APPIUM_SERVER}/wd/hub',
        desired_capabilities)

    search_button = driver.find_element_by_id('Search').click();

    search_bar = driver.find_element_by_class_name('XCUIElementTypeSearchField').sendKeys(keys.ENTER);

    Keyword = apps.get_model('scrapers', 'Keyword')

    keywords = []
    for idx in range (2, 7):
        xpath = f'//XCUIElementTypeApplication[@name="App Store"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[{idx}]'
        el = driver.find_element_by_xpath(xpath)
        keyword_str = el.get_attribute('name')

        keyword, created = Keyword.objects.get_or_create(text='text')
        keywords.append(keyword)

    print(keywords)




@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    #sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    #sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )
    pass