from tkinter import *


def login_verify():
	print("Ok")

def register_user():
	username_info = username.get()
	password_info = password.get()

	file = open(username_info, "w")
	file.write(username_info+"\n")
	file.write(password_info+"\n")
	file.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)

	Label(screen1, text = "Registro concluido", fg = "green", font = ("Calibri", 12)).pack()

def register():
	global screen1
	screen1 = Toplevel(screen)
	screen1.title("Register")
	screen1.geometry("600x350")

	global username
	global password
	global username_entry
	global password_entry

	username = StringVar()
	password = StringVar()

	Label(screen1, text = "Preencha os dados abaixo:").pack()
	Label(screen1, text = "").pack()

	Label(screen1, text = "Username * ").pack()
	username_entry = Entry(screen1, textvariable = username)
	username_entry.pack()
	Label(screen1, text = "Password * ").pack()
	password_entry = Entry(screen1, textvariable = password, show = "*")
	password_entry.pack()
	Label(screen1, text = "").pack()
	Button(screen1, text = "Register", height = 1, command = register_user).pack()


def login():
	global screen2
	global username_verify
	global password_verify

	username_verify = StringVar()
	password_verify = StringVar()

	screen2 = Toplevel(screen)
	screen2.title("Login")
	screen2.geometry("600x350")

	Label(screen2, text = "Faca login com seus dados:").pack()
	Label(screen2, text = "").pack()

	Label(screen2, text = "Username * ").pack()
	username_entry1 = Entry(screen2, textvariable = username_verify)
	username_entry1.pack()
	Label(screen2, text = "Password * ").pack()
	password_entry1 = Entry(screen2, textvariable = password_verify, show = "*")
	password_entry1.pack()
	Label(screen2, text = "").pack()
	Button(screen2, text = "Login", command = login_verify).pack()

	username_entry.delete(0, END)
	password_entry.delete(0, END)


def main_screen():
  global screen
  screen = Tk()
  screen.geometry("600x350")
  screen.title("Luta Luta")
  Label(text = "Luta Luta", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()


main_screen()