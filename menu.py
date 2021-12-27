from kivy.uix.relativelayout import RelativeLayout


class MenuWidget(RelativeLayout):
    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        # managing menu clicks , (in the super i put RelativeLayout to avoid circular imports)
        return super(RelativeLayout, self).on_touch_down(touch)
