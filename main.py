from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
import KGBerryKrunch

class MainScreen(Screen):
	def run_button(self, in_option, in_phrase, in_key):
		kgb = KGBerryKrunch.KGBerryKrunch(in_option, in_phrase, in_key)
		self.ids.result_text.text = kgb.get_result()
	def copy_result(self):
		Clipboard.put(self.ids.result_text.text, 'UTF8_STRING')


Builder.load_string("""
#:kivy 1.8.0
<MainScreen>:
	canvas:
		Rectangle:
			source: 'BgRed.png'
			size: self.size
		Rectangle:
			source: 'KGPieces.png'
			size: 800,self.size[1]
	BoxLayout:
		orientation: 'vertical'
		Image:
			size_hint_y: 0.15
			source: 'KGTitleNoMilk.png'
		BoxLayout:
			padding: 20
			spacing: 20
			orientation: 'vertical'
			BoxLayout:
				ToggleButton:
					id: encode_opt
					text: 'Encode'
					group: 'code'
					state: 'down'
					on_press: 
						if self.state == 'down': input_text.text = ''; pass_text.text = ''; result_text.text = ''
						self.state = 'down'
					on_state: 
						if self.state == 'down': run_button.text = 'Encode';input_text.hint_text = 'Message to Encode'
				ToggleButton:
					id: decode_opt
					text: 'Decode'
					group: 'code'
					on_press: 
						if self.state == 'down': input_text.text = ''; pass_text.text = ''; result_text.text = ''
						self.state = 'down'
					on_state: 
						if self.state == 'down': run_button.text = 'Decode';input_text.hint_text = 'Message to Decode'
			TextInput:
				id: input_text
				hint_text: 'Message to Encode'
			TextInput: 
				id: pass_text
				hint_text: 'Password'
				password: True
			BoxLayout:
				Label:
				Button:
					id: run_button
					text: 'Encode'
					on_press: 
						if decode_opt.state == 'down' and input_text.text != '' and pass_text.text != '': root.run_button('D', input_text.text, pass_text.text)
						elif encode_opt.state == 'down' and input_text.text != '' and pass_text.text != '': root.run_button('E', input_text.text, pass_text.text)
						else: pass
				Label:
			TextInput:
				size_hint_y: 3
				id: result_text
				hint_text: 'Result'
				multiline: True
				readonly: True
			BoxLayout:
				Button:
					text: 'Copy'	
					on_press: root.copy_result()
				Button:
					text: 'Clear'
					on_press: input_text.text = ''; pass_text.text = ''; result_text.text = ''
""")

class KGBerryKrunchApp(App):
	def build(self):
		Window.size = (480,700)
		return MainScreen()
	
if __name__ == '__main__':
	KGBerryKrunchApp().run()