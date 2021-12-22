from tkinter import Tk, Label

window = Tk()
window.title("Bechosen Digital Clock")
window.geometry("600x300")
window.configure(bg="steelblue")

Label = Label(window, text="Welcome!", font=("Arial Black", 78, "bold"), bg="steelblue", fg="White")
Label.pack(pady=100)

window.mainloop()
