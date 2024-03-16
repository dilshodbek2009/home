from tkinter import Tk, Label, Frame, LabelFrame, Button, Spinbox, PhotoImage
from PIL import ImageTk
from basa import Database

window = Tk()
window.geometry("1000x1000")
window.configure(bg="grey")

image_icon = PhotoImage(file="photo_2024-03-11_23-09-42-remove (1).png")
window.iconphoto(False, image_icon)

frame = Frame(window)
frame.grid(padx=80, pady=100)
db = Database()

label_frame = LabelFrame(frame, bg="light grey")
label_frame.grid()
# ======================================================
odam = ImageTk.PhotoImage(file="photo_2024-03-11_23-41-02-removebg-preview.png")
odam_label = Label(window, image=odam)
odam_label.grid(row=0, column=5)
# YOZUV ================================================
e_label = Label(window, text="RAYHON MILLIY TAOMLAR",
                fg="white", bg="#656464",
                font=("Arial", 30))
e_label.place(x=250, y=10)

# BURGER =================================================
burger_photo = ImageTk.PhotoImage(file="photo_6_2024-03-11_13-13-05 (1).jpg")
burger_label = Label(label_frame, image=burger_photo)
burger_label.grid(row=1, column=0)

burger_label = Label(label_frame, text="go'sht",
                     font=("Verdana", 20),
                     fg="white", bg="#656464")
burger_label.grid(row=2, column=0)

burger_label2 = Label(label_frame, text="25,000 so'm",
                      font=("Verdana", 20),
                      fg="white", bg="#656464")
burger_label2.grid(row=3, column=0)

burger_spinbox = Spinbox(label_frame, from_=1, to=100)
burger_spinbox.grid(row=4, column=0)
# LAVASH ==================================================
lavash_photo = ImageTk.PhotoImage(file="photo_5_2024-03-11_13-13-05 (1).jpg")
lavsh_label = Label(label_frame, image=lavash_photo)
lavsh_label.grid(row=1, column=1)

lavsh_label = Label(label_frame, text="salat",
                    font=("Verdana", 20),
                    fg="white", bg="#656464")
lavsh_label.grid(row=2, column=1)

lavsh_label2 = Label(label_frame, text="28,000 so'm",
                     font=("Verdana", 20),
                     fg="white", bg="#656464")
lavsh_label2.grid(row=3, column=1)

lavash_spinbox = Spinbox(label_frame, from_=1, to=100)
lavash_spinbox.grid(row=4, column=1)
# Shaurma ===================================================

shaurma_photo = ImageTk.PhotoImage(file="photo_4_2024-03-11_13-13-05 (1).jpg")
shaurma_label = Label(label_frame, image=shaurma_photo)
shaurma_label.grid(row=1, column=2)

shaurma_label = Label(label_frame, text="shashlik",
                      font=("Verdana", 20),
                      fg="white", bg="#656464")
shaurma_label.grid(row=2, column=2)

shaurma_label2 = Label(label_frame, text="25,000 so'm",
                       font=("Verdana", 20),
                       fg="white", bg="#656464")
shaurma_label2.grid(row=3, column=2)

shaurma_spinbox = Spinbox(label_frame, from_=1, to=100)
shaurma_spinbox.grid(row=4, column=2)
# HOT DOG ===============================================
Hot_dog_photo = ImageTk.PhotoImage(file="photo_3_2024-03-11_13-13-05 (2).jpg")
Hot_dog_label = Label(label_frame, image=Hot_dog_photo)
Hot_dog_label.grid(row=1, column=3)

Hot_dog_label = Label(label_frame, text="asorti",
                      font=("Verdana", 20),
                      fg="white", bg="#656464")
Hot_dog_label.grid(row=2, column=3)

Hot_dog_label2 = Label(label_frame, text="15,000 so'm",
                       font=("Verdana", 20),
                       fg="white", bg="#656464")
Hot_dog_label2.grid(row=3, column=3)

hotdog_spinbox = Spinbox(label_frame, from_=1, to=100)
hotdog_spinbox.grid(row=4, column=3)
# FRIES====================================================
fries_photo = ImageTk.PhotoImage(file="photo_2_2024-03-11_13-13-05 (2).jpg")
fries_label = Label(label_frame, image=fries_photo)
fries_label.grid(row=5, column=0)

fries_label = Label(label_frame, text="shula",
                    font=("Verdana", 20),
                    fg="white", bg="#656464")
fries_label.grid(row=6, column=0)

fries_label2 = Label(label_frame, text="14,000 so'm",
                     font=("Verdana", 20),
                     fg="white", bg="#656464")
fries_label2.grid(row=7, column=0)

fries_spinbox = Spinbox(label_frame, from_=1, to=100)
fries_spinbox.grid(row=8, column=0)
# SNACKS ================================================
snacks_photo = ImageTk.PhotoImage(file="photo_1_2024-03-11_13-13-05 (2).jpg")
snacks_label = Label(label_frame, image=snacks_photo)
snacks_label.grid(row=5, column=1)

snacks_label = Label(label_frame, text="sho'rva",
                     font=("Verdana", 20),
                     fg="white", bg="#656464")
snacks_label.grid(row=6, column=1)

snacks_label2 = Label(label_frame, text="9,000 so'm",
                      font=("Verdana", 20),
                      fg="white", bg="#656464")
snacks_label2.grid(row=7, column=1)

snack_spinbox = Spinbox(label_frame, from_=1, to=100)
snack_spinbox.grid(row=8, column=1)
# HOT DOG ===============================================
combo_photo = ImageTk.PhotoImage(file="photo_2024-03-11_13-57-52 (2).jpg")
combo_label = Label(label_frame, image=combo_photo)
combo_label.grid(row=5, column=2)

combo_label = Label(label_frame, text="manti",
                    font=("Verdana", 20),
                    fg="white", bg="#656464")
combo_label.grid(row=6, column=2)

combo_label2 = Label(label_frame, text="30,000 so'm",
                     font=("Verdana", 20),
                     fg="white", bg="#656464")
combo_label2.grid(row=7, column=2)

combo_spinbox = Spinbox(label_frame, from_=1, to=100)
combo_spinbox.grid(row=8, column=2)
# COFFEE ===========================================
coffee_photo = ImageTk.PhotoImage(file="photo_2024-03-11_13-57-45 (2).jpg")
coffee_label = Label(label_frame, image=coffee_photo)
coffee_label.grid(row=5, column=3)

coffee_label = Label(label_frame, text="disert",
                     font=("Verdana", 20),
                     fg="white", bg="#656464")
coffee_label.grid(row=6, column=3)

coffee_label2 = Label(label_frame, text="12,000 so'm",
                      font=("Verdana", 20),
                      fg="white", bg="#656464")
coffee_label2.grid(row=7, column=3)

coffee_spinbox = Spinbox(label_frame, from_=1, to=100)
coffee_spinbox.grid(row=8, column=3)


# KNOPKA=================================================
def button_count():
    burger_total = int(burger_spinbox.get()) * 55_000
    lavash_total = int(lavash_spinbox.get()) * 28_000
    shaurma_total = int(shaurma_spinbox.get()) * 15_000
    hot_dog_total = int(hotdog_spinbox.get()) * 95_000
    fries_total = int(fries_spinbox.get()) * 26_000
    snack_total = int(snack_spinbox.get()) * 30_000
    combo_total = int(combo_spinbox.get()) * 10_000
    coffee_total = int(coffee_spinbox.get()) * 52_000
    total_bills = sum([burger_total, lavash_total, shaurma_total, hot_dog_total,
                       fries_total, snack_total, combo_total, coffee_total])
    bills = Label(text=f"Sizning hisobingiz {total_bills} so'm bo'ldi",
                  bg="#279340", fg="white", font=("Arial", 20, "bold"))
    bills.place(x=140, y=685)


buyur_button = Button(window, text="Buyurtma berish",
                      font=("Verdana", 25),
                      fg="#656464", bg="white", command=button_count)
buyur_button.place(x=310, y=680)

# =====================================================

for widget in label_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
from tkinter import Tk, Frame, Button, Menu, filedialog

my_menu = Menu(window)
window.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)


def open_file():
    filedialog.askopenfilename()


file_menu.add_command(label="javascript", command=window)
file_menu.add_separator()
file_menu.add_command(label="python", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
file_menu.add_separator()

sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label="Plugins")
sub_menu.add_command(label="copy")
file_menu.add_cascade(label="Settings", menu=sub_menu)

sub_menu2 = Menu(file_menu, tearoff=0)
sub_menu2.add_command(label="plugin1")
sub_menu2.add_command(label="plugin2")
sub_menu.add_cascade(label="Settings", menu=sub_menu2)

window.mainloop()
window.mainloop()
