from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MiAplicacion(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="¡Hola! Bienvenido a la aplicación de Erick."))
        self.boton_saludar = Button(text="Saludar")
        self.boton_salir = Button(text="Salir")
        self.boton_saludar.bind(on_press=self.saludar)
        self.boton_salir.bind(on_press=self.salir)
        self.add_widget(self.boton_saludar)
        self.add_widget(self.boton_salir)
        self.label_resultado = Label(text="")
        self.add_widget(self.label_resultado)

    def saludar(self, instance):
        self.clear_widgets()
        self.add_widget(Label(text="¿Cómo te llamas?"))
        self.entrada_nombre = TextInput(multiline=False)
        self.add_widget(self.entrada_nombre)
        self.boton_confirmar = Button(text="Confirmar")
        self.boton_confirmar.bind(on_press=self.mostrar_saludo)
        self.add_widget(self.boton_confirmar)

    def mostrar_saludo(self, instance):
        nombre = self.entrada_nombre.text
        self.clear_widgets()
        self.add_widget(Label(text=f"¡Hola, {nombre}! Encantado de conocerte."))

    def salir(self, instance):
        self.clear_widgets()
        self.add_widget(Label(text="Has salido de la aplicación. ¡Hasta luego!"))

class MiApp(App):
    def build(self):
        return MiAplicacion()

if __name__ == '__main__':
    MiApp().run()
