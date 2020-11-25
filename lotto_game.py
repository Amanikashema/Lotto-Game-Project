# Amani Kashema class3
from tkinter import *
import random
from tkinter import messagebox as mb
import datetime as dt
root = Tk()
root.title("Age Validation")
root.geometry("500x350")
root.configure(bg="brown")


class Lotto:
    def __init__(self):
        # function to validate login
        def login():
            try:
                if int(self.age.entry.get()) < 18:
                    mb.showwarning("Sorry","You do not qualify to play lotto")

                elif int(self.age.entry.get()) >= 18:
                    mb.showinfo("You qualify to play Lotto","Welcome to the Ithuba National Lottery of South Africa")
                    root.destroy()
                    root1 = Tk()
                    root1.title("Lotto App")
                    root1.geometry("500x350")
                    root1.configure(bg="brown")

                    def random_lotto():
                        try:
                            input_list.append(int(a1.get()))
                            input_list.append(int(a2.get()))
                            input_list.append(int(a3.get()))
                            input_list.append(int(a4.get()))
                            input_list.append(int(a5.get()))
                            input_list.append(int(a6.get()))
                        except ValueError:
                            print("enter valid literals")
                            mb.showerror("Error","Please Enter valid literals for lotto numbers")

                        lotto_numbers = sorted(random.sample(range(1,49),6))
                        filename = "text_file.txt"

                        # statement for decision
                        if len(lotto_numbers) == len(input_list):
                            duplicates = set(lotto_numbers).intersection(set(input_list))
                            if len(duplicates) == 0:
                                answer.configure(text="You failed !!! " + str(self.var1.get()) + ' ' + str(self.var2.get()) + "\n Lucky Lotto Numbers are: " + str(lotto_numbers) + "\nPrize: R0 \n" + "Date: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))
                            elif len(duplicates) == 1:
                                answer.configure(text="Congratulations " + str(self.var1.get()) + ' ' + str(self.var2.get()) + "\n You got 1 number correct \n" + "Lucky Lotto Numbers are: " + str(lotto_numbers) + "\nPrize: R0\n" + "Date: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))
                            elif len(duplicates) == 2:
                                answer.configure(text="Congratulations " + str(self.var1.get()) + ' ' + str(self.var2.get()) + "\n You got 2 numbers correct \n" + "Lucky Lotto Numbers are: " + str(lotto_numbers) + "\nPrize: R20\n" + "Date: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))
                            elif len(duplicates) == 3:
                                answer.configure(text="Congratulations " + str(self.var1.get()) + ' ' + str(self.var2.get()) + "\n You got 3 numbers correct \n" + "Lucky Lotto Numbers are: " + str(lotto_numbers) + "\nPrize: R110\n" + "Date: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))
                            elif len(duplicates) == 4:
                                answer.configure(text="Congratulations " + str(self.var1.get()) + ' ' + str(self.var2.get()) + "\n You got 4 numbers correct \n" + "Lucky Lotto Numbers are: " + str(lotto_numbers) + "\nPrize: R2384\n" + "Date: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))
                            elif len(duplicates) == 5:
                                answer.configure(text="Congratulations " + str(self.var1.get()) + ' ' + str(self.var2.get()) + "\n You got 5 numbers correct \n" + "Lucky Lotto Numbers are: " + str(lotto_numbers) + "\nPrize: R8584\n" + "Date: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))
                            elif len(duplicates) == 6:
                                answer.configure(text="Congratulations " + str(self.var1.get()) + ' ' + str(self.var2.get()) + "\n You got 6 numbers correct \n" + "Lucky Lotto Numbers are: " + str(lotto_numbers) + "\nPrice: R10 000 000\n" + "Date: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))
                            file = open(filename, "w+")
                            file.close()
                            file = open(filename, "a")
                            answers = answer.cget("text")
                            file.write(answers)
                            file.close()

                    # lotto numbers
                    answer = Label(root1,bg="brown")
                    answer.place(x=100,y=200)
                    input_list = []

                    label_text = Label(root1, text="Enter lucky Lotto Numbers")
                    label_text.place(x=10,y=20)

                    def exit_b():
                        root1.destroy()
                    exit_button = Button(root1, text="Exit",bg="blue", command=exit_b)
                    exit_button.place(x=150, y=130)

                    # lotto entries
                    a1 = Entry(root1,bg="grey", width=4)
                    a1.place(x=200,y=20)

                    a2 = Entry(root1,bg="grey", width=4)
                    a2.place(x=250,y=20)

                    a3 = Entry(root1,bg="grey", width=4)
                    a3.place(x=300,y=20)

                    a4 = Entry(root1,bg="grey", width=4)
                    a4.place(x=350,y=20)

                    a5 = Entry(root1,bg="grey", width=4)
                    a5.place(x=400,y=20)

                    a6 = Entry(root1,bg="grey", width=4)
                    a6.place(x=450,y=20)

                    # Button to submit both list
                    button = Button(root1,text="Play Lotto",bg="green", command=random_lotto)
                    button.place(x=220,y=130)

                    # function to clear
                    def clear_a():
                        a1.delete("0", END)
                        a2.delete("0", END)
                        a3.delete("0", END)
                        a4.delete("0", END)
                        a5.delete("0", END)
                        a6.delete("0", END)
                    # clear button
                    clear_but = Button(root1,text="Clear",bg="yellow",command=clear_a)
                    clear_but.place(x=330, y=130)

            except ValueError:
                mb.showerror("Error","Enter Valid Literals for age")
                print("Please Enter valid literals for age")
                root.destroy()

            finally:
                pass
        # label
        self.user_name = Label(root,text="Please enter your name")
        self.user_surname = Label(root,text="Please enter your Surname")
        self.age = Label(root,text="Please enter your age")
        self.submit = Button(root,text="Check validation", bg="green", command=login).place(x=250, y=230)

        # time label
        now = dt.datetime.now()
        self.time = Label(root,bg="yellow")
        self.time.place(x=180, y=280)
        self.time.config(text="Date: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))

        # entry
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.user_name_entry = Entry(root,textvariable=self.var1)
        self.user_name_entry.place(x=290, y=50)
        self.user_surname_entry = Entry(root,textvariable=self.var2)
        self.user_surname_entry.place(x=290, y=100)
        self.age.entry = Entry(root)
        self.age.entry.place(x=290, y=150)

        # function to clear
        def clear():
            self.user_name_entry.delete("0", END)
            self.user_surname_entry.delete("0", END)
            self.age.entry.delete("0", END)

        # button to clear
        self.c_button = Button(root,text="Clear",bg="blue", command=clear)
        self.c_button.place(x=180,y=230)

        # positioning
        self.user_name.place(x=50, y=50)
        self.user_surname.place(x=50, y=100)
        self.age.place(x=50, y=150)

        # function to exit
        def exit_a():
            root.destroy()
        # exit button
        self.exit_button = Button(root, text="Exit",bg="red", command=exit_a)
        self.exit_button.place(x=120, y=230)


Lotto()
root.mainloop()
