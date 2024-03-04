from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class PianoLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(PianoLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.sounds = {}

        grid_layout = GridLayout(cols=7, spacing=5, padding=5, size_hint_y=0.8)
        self.add_widget(grid_layout)
        for i in range(1, 8):
        	for note in ["C", "D", "E", "F", "G", "A", "B"]:
        		button = Button(text=note + str(i), on_press=self.play_note, background_color=(1, 1, 1, 5))
        		grid_layout.add_widget(button)

        		sound = SoundLoader.load(f'notes/{button.text}.wav')
        		if sound: self.sounds[button.text] = sound


    def play_note(self, instance):
        try:
        	note_text = instance.text  # Obtém o texto do botão
        	sound = self.sounds.get(note_text)

        	if sound: sound.play()
        except Exception as e:
            print(f"Erro ao carregar ou reproduzir a nota {note}: {e}")
        
class PianoApp(App):
    def build(self):
        return PianoLayout()

if __name__ == '__main__':
    PianoApp().run()

"""C: Dó
D: Ré
E: Mi
F: Fá
G: Sol
A: Lá
B: Si"""