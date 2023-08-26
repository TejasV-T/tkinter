from tkinter import *
from tkinter import ttk 
from  time  import sleep
from PIL import *
root=Tk()
#Feed back window
def open_win(a):
    new1= Toplevel(root)
    new1.geometry("400x650")
    new1.title("Screen 2")
    #Create a Label in New window
    f=Frame(new1,width=400,height=700)
    f.pack()
    new=f
    Label(new, text=f"Thank you for providing {a} rating , in which aspect you liked/disliked the restaurant",
              font=('Helvetica 17 bold'),wraplength=300,fg="Blue").pack(pady=30)
    Food_quantity=Checkbutton(new,text="Food Quantity",font=("Ariel",10))
    Food_quantity.pack(padx=10,pady=10)
    Food_quality=Checkbutton(new,text="Food Quality",font=("Ariel",10))
    Food_quality.pack(padx=10,pady=10)
    Service=Checkbutton(new,text="Service",font=("Ariel",10))
    Service.pack(padx=10,pady=10)
    Pricing=Checkbutton(new,text="Prices",font=("Ariel",10))
    Pricing.pack(padx=10,pady=10)
    Label(new,text="Feedback :",font=('Helvetica 14 bold')).pack(pady=10)
    text= Text(new, height= 10,width= 40)
    text.pack(padx=10,pady=10)
    #here for this submit button please include th 
    submit_button=Button(new,text="Submit",command=new1.destroy)
    submit_button.pack(padx=10,pady=10)
    new1.resizable(False,False)
#................................
#g=frames_action()
good_label=Label(text="Good",)
good_label.config( font=("Ariel",25),fg="red")
good_label.grid(row=1,column=1,padx=20,pady=20)
#good_label.pack()
good_img=PhotoImage(file="Good.png")
good_button=Button(root,text="clickme",border=0,height=160,width=160,command=lambda:open_win("Good"))
good_button.config(image=good_img)
good_button.grid(row=2,column=1,padx=20,pady=20)
#............................
very_good_label=Label(text="Very good")
very_good_label.config( font=("Ariel",25),fg="red")
very_good_label.grid(row=1,column=0,padx=20,pady=20)
#very_good_label.pack()
very_good_img=PhotoImage(file="very_good.png")
very_good_button=Button(root,text="clickme",border=0,height=185,width=185,command=lambda:open_win("Very Good"))
very_good_button.config(image=very_good_img)
very_good_button.grid(row=2,column=0,padx=20,pady=20)
#.............................
not_good_label=Label(text="Not good")
not_good_label.config(font=("Ariel",25),fg="red")
not_good_label.grid(row=1,column=3,padx=20,pady=20)
#not_good_label.pack()
not_good_img=PhotoImage(file="not_good.png")
not_good_button=Button(root,text="clickme",border=0,height=180,width=180,command=lambda:open_win("Not Good"))
not_good_button.config(image=not_good_img)
not_good_button.grid(row=2,column=3,padx=20,pady=20)
#...................
ok_label=Label(text="Ok")
ok_label.config( font=("Ariel",25),fg="red")
ok_label.grid(row=1,column=2,padx=20,pady=20)
#good_label.pack()
ok_img=PhotoImage(file="ok.png")
ok_button=Button(root,text="clickme",border=0,height=180,width=180,command=lambda:open_win("OK"))
ok_button.config(image=ok_img)
ok_button.grid(row=2,column=2,padx=20,pady=20)
#...................................................
root.geometry("900x300")
root.resizable(False,False)
root.title("Screen1")
root.mainloop()