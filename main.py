from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.result = TextInput(text='', font_size=32, readonly=True, halign='right', size_hint_y=None, height=80)
        layout.add_widget(self.result)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, font_size=32)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
            
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        text = instance.text
        if text == 'C':
            self.result.text = ''
        elif text == '=':
            try:
                self.result.text = str(eval(current))
            except Exception:
                self.result.text = 'خطأ'
        else:
            self.result.text = current + text

if __name__ == '__main__':
    CalculatorApp().run()

