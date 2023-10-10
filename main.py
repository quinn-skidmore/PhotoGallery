from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("PhotoGallery.kv")

class PhotoGalleryApp(App):
    pass

class Display(Screen):
    global index
    global images
    def display_image(self):
        return images[index]
    def advance(self):
        if index < len(images):
            index += 1
        else:
            index = 0

images = ["monkey1.jpg","monkey2.jpg","monkey3.jpg"]
index = 0

PhotoGalleryApp().run()