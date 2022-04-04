from datetime import datetime, timedelta

import wrapt
from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform

from schedule_utils import schedule_task

SERVICE_NAME = u'{packagename}.Service{servicename}'.format(
    packagename=u'org.atq.atq',
    servicename=u'Notifier'
)

KV = '''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: '30sp'
        Button:
            text: 'start service'
            on_press: app.start_service()
        Button:
            text: 'stop service'
            on_press: app.stop_service()
    ScrollView:
        Label:
            id: label
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.size[0], None
'''


@wrapt.decorator
def android_only(wrapped, instance, args, kwargs):
    if platform == 'android':
        return wrapped(*args, **kwargs)
    else:
        raise NotImplementedError(f"not implemented for this platform: {platform}")


class ATQApp(App):
    def build(self):
        self.service = None

        self.root = Builder.load_string(KV)
        return self.root

    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })

    @android_only
    def start_service(self):
        schedule_task(datetime.now())

    @android_only
    def stop_service(self):
        pass


if __name__ == '__main__':
    ATQApp().run()
