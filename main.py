from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import filechooser
import os

class NotePad(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.current_file = None
        
        # Text Input Area
        self.text_input = TextInput(
            hint_text='Start typing your note...',
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            font_size='18sp',
            padding=10
        )
        self.add_widget(self.text_input)
        
        # Button Layout
        button_layout = BoxLayout(size_hint=(1, 0.1), spacing=10, padding=10)
        
        # Action Buttons
        buttons = [
            ('Save', self.save_file),
            ('Load', self.load_file),
            ('New', self.new_file),
            ('Clear', self.clear_text)
        ]
        
        for text, callback in buttons:
            btn = Button(
                text=text,
                background_color=(0.2, 0.6, 1, 1),
                color=(1, 1, 1, 1),
                bold=True
            )
            btn.bind(on_press=callback)
            button_layout.add_widget(btn)
        
        self.add_widget(button_layout)

    def save_file(self, instance):
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import filechooser
import os

class NotePad(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.current_file = None
        
        # Text Input Area
        self.text_input = TextInput(
            hint_text='Start typing your note...',
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            font_size='18sp',
            padding=10
        )
        self.add_widget(self.text_input)
        
        # Button Layout
        button_layout = BoxLayout(size_hint=(1, 0.1), spacing=10, padding=10)
        
        # Action Buttons
        buttons = [
            ('Save', self.save_file),
            ('Load', self.load_file),
            ('New', self.new_file),
            ('Clear', self.clear_text)
        ]
        
        for text, callback in buttons:
            btn = Button(
                text=text,
                background_color=(0.2, 0.6, 1, 1),
                color=(1, 1, 1, 1),
                bold=True
            )
            btn.bind(on_press=callback)
            button_layout.add_widget(btn)
        
        self.add_widget(button_layout)

    def save_file(self, instance):
        if self.current_file:
            self._save_file(self.current_file)
        else:
            try:
                filechooser.save_file(
                    callback=self._save_callback,
                    filters=['*.txt'],
                    title='Save Note',
                    multiple=False
                )
            except NotImplementedError:
                self.show_popup('Error', 'File chooser not supported on this platform')

    def _save_callback(self, path):
        if path:
            if not path.endswith('.txt'):
                path += '.txt'
            self.current_file = path
            self._save_file(path)

    def _save_file(self, path):
        try:
            with open(path, 'w') as f:
                f.write(self.text_input.text)
            self.show_popup('Success', f'Saved successfully to:\n{os.path.basename(path)}')
        except Exception as e:
            self.show_popup('Error', f'Save failed: {str(e)}')

    def load_file(self, instance):
        try:
            filechooser.open_file(
                callback=self._load_callback,
                filters=['*.txt'],
                title='Open Note',
                multiple=False
            )
        except NotImplementedError:
            self.show_popup('Error', 'File chooser not supported on this platform')

    def _load_callback(self, selection):
        if selection:
            self.current_file = selection[0]
            Clock.schedule_once(lambda dt: self._load_file(self.current_file))

    def _load_file(self, path):
        try:
            with open(path, 'r') as f:
                self.text_input.text = f.read()
            self.show_popup('Success', f'Loaded:\n{os.path.basename(path)}')
        except Exception as e:
            self.show_popup('Error', f'Load failed: {str(e)}')

    def new_file(self, instance):
        self.clear_text()
        self.current_file = None
        self.show_popup('Info', 'New file created')

    def clear_text(self, instance=None):
        self.text_input.text = ''

    def show_popup(self, title, message):
        content = Label(text=message, halign='center', valign='middle')
        popup = Popup(
            title=title,
            content=content,
            size_hint=(None, None),
            size=(400, 200),
            separator_color=(0.2, 0.6, 1, 1)
        )
        content.bind(size=content.setter('text_size'))
        popup.open()

class NotePadApp(App):
    def build(self):
        self.title = 'NotePy - Mobile Notepad'
        return NotePad()

if __name__ == '__main__':
    NotePadApp().run()￼Enter        if self.current_file:
            self._save_file(self.current_file)
        else:
            try:
                filechooser.save_file(
                    callback=self._save_callback,
                    filters=['*.txt'],
                    title='Save Note',
                    multiple=False
                )
            except NotImplementedError:
                self.show_popup('Error', 'File chooser not supported on this platform')

    def _save_callback(self, path):
        if path:
            if not path.endswith('.txt'):
                path += '.txt'
            self.current_file = path
            self._save_file(path)

    def _save_file(self, path):
        try:
            with open(path, 'w') as f:
                f.write(self.text_input.text)
            self.show_popup('Success', f'Saved successfully to:\n{os.path.basename(path)}')
        except Exception as e:
      self.show_popup('Error', f'Save failed: {str(e)}')

    def load_file(self, instance):
        try:
            filechooser.open_file(
                callback=self._load_callback,
                filters=['*.txt'],
                title='Open Note',
                multiple=False
            )
        except NotImplementedError:
            self.show_popup('Error', 'File chooser not supported on this platform')

    def _load_callback(self, selection):
        if selection:
            self.current_file = selection[0]
            Clock.schedule_once(lambda dt: self._load_file(self.current_file))

    def _load_file(self, path):
        try:
            with open(path, 'r') as f:
                self.text_input.text = f.read()
            self.show_popup('Success', f'Loaded:\n{os.path.basename(path)}')
        except Exception as e:
            self.show_popup('Error', f'Load failed: {str(e)}')

