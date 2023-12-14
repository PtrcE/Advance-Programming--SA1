import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def woof(self):
        messagebox.showinfo('Woof', f'{self.name} woofs!')

    @classmethod
    def find_oldest(cls, dogs):
        oldest_dog = None
        max_age = 0

        for dog in dogs:
            if dog.age > max_age:
                max_age = dog.age
                oldest_dog = dog

        return oldest_dog

dog1 = Dog('Buddy', 3, 'Golden Retriever')
dog2 = Dog('Max', 5, 'Labrador')

root = tk.Tk()
root.title('Dog Information')

def display_data():
    data = [f'Name: {dog.name}', f'Age: {dog.age}', f'Breed: {dog.breed}']
    data_str = '\n'.join(data)

    oldest_dog = Dog.find_oldest([dog1, dog2])

    messagebox.showinfo('Dog Data', data_str)

    if oldest_dog:
        oldest_dog.woof()

button = tk.Button(root, text='Display Dog Data', command=display_data)
button.pack()

root.mainloop()