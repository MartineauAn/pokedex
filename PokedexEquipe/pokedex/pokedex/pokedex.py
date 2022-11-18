from curses import window
from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO
import pokebase as pb

window = Tk()
window.title("Pokedex")
window.geometry("600x700")

img = ImageTk.PhotoImage(Image.open("pokemon.png"))
banner = Label(window, image=img)
banner.image = img
banner.pack() 

label1 = Label(window, text="Enter Pokemon Name: ", fg="red", pady=20, font=('Ubuntu', 20))
label1.pack()

pokemon_input = Entry(window,font=('Ubuntu', 18))
pokemon_input.pack(pady=20)

def search():
    details.delete(1.0, END)
    pokemon = pb.pokemon(pokemon_input.get())
    try:
        response = requests.get(pokemon.sprites.front_default)
        image = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        pokemon_image.config(image=image)
        pokemon_image.image = image
        abilities = ''
        types = ''
        for ability in pokemon.abilities:
            abilities += ability.ability.name + ', '
        for type in pokemon.types:
            types += type.type.name + ', '
        data = f"""{pokemon_input.get().capitalize()}
        \nHeight: {pokemon.height}
        \nWeight: {pokemon.weight}
        \nAbilities: {abilities}
        \nTypes: {types}
        """
        details.insert(END, data)

    except AttributeError:
        details.insert(END, "Pokemon not found")
        pokemon_image.config(image='')
     
btn= Button(window, bd='4', text="Submit", fg="red", bg="white", command=search)
btn.pack()

pokemon_image = Label(window)
pokemon_image.pack(pady = 30)

details= Text(window, font=('Ubuntu', 12), bg='light yellow')
details.pack()
window.mainloop()

