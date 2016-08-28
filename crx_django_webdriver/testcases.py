from __future__ import unicode_literals

from django.test import LiveServerTestCase
from datetime import datetime
import os
from crx_django_webdriver import settings


class DjangoWebdriverTestCaseMixin(object):

    def setUp(self):
        self.driver = settings.DJANGO_WEBDRIVER_CLASS(**settings.DJANGO_WEBDRIVER_KWARGS)
        self.driver.implicitly_wait(settings.DJANGO_WEBDRIVER_IMPLICITLY_WAIT)

    def tearDown(self):
        self.driver.quit()

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def navigate_to(self, path=None):
        path = path or '/'
        self.driver.get('{}{}'.format(self.live_server_url, path))

    def page(self, page_class):
        return page_class(self)

    def screenshot(self, file_name=None, path=None):
        path = path or settings.DJANGO_WEBDRIVER_SCREENSHOT_PATH
        filename = file_name or 'screenshot-{}.png'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        self.driver.get_screenshot_as_file(os.path.join(path, filename))


class DjangoWebdriverLiveServerTestCase(DjangoWebdriverTestCaseMixin,
                                        LiveServerTestCase):
    pass
