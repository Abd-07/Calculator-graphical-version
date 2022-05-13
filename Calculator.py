import tkinter
window=tkinter.Tk()

window.title("Calculator")
window.geometry("300x300")
window.configure(bg='#000080')


##Function to get info from text_1
def text_1_info():
    num_1=int(text_1.get())
    return num_1


##Function to get info from text_2
def text_2_info():
    num_2=int(text_2.get())
    return num_2


##Function of deleting info from text_3
def text_3_delete(answer):
    text_3.delete(0,"end")
    text_3.insert(0,answer)


##Function of sum
def summ():
    num_1=text_1_info()
    num_2=text_2_info()
    result=num_1 + num_2
    text_3_delete(result)
    

##Function of minus
def minus():
    num_1=text_1_info()
    num_2=text_2_info()
    result=num_1 - num_2
    text_3_delete(result)



##Function of mult
def mult():
    num_1=text_1_info()
    num_2=text_2_info()
    result=num_1 * num_2
    text_3_delete(result)

##Function of div
def div():
    num_1=text_1_info()
    num_2=text_2_info()
    result=num_1 / num_2
    text_3_delete(result)


##Function of eraser
def eraser():
    text_3.delete(0,"end")


##Function of erase_all
def eraser_a():
    text_1.delete(0,"end")
    text_2.delete(0,"end")
    text_3.delete(0,"end")
    
##creation of buttons
button_sum=tkinter.Button(window,text="+",command=summ,height=3,width=7,fg='green')
button_sum.place(x=130,y=135)
button_minus=tkinter.Button(window,text="-",command=minus,height=3,width=7,fg='green')
button_minus.place(x=195,y=135)
button_mult=tkinter.Button(window,text="x",command=mult,height=3,width=7,fg='green')
button_mult.place(x=130,y=185)
button_div=tkinter.Button(window,text="÷",command=div,height=3,width=7,fg='green')
button_div.place(x=195,y=185)
button_erase=tkinter.Button(window,text="Erase result",command=eraser,fg='red')
button_erase.place(x=11,y=37)
button_erase_all=tkinter.Button(window,text="Erase all",command=eraser_a,fg='red')
button_erase_all.place(x=18,y=97)

##Creation of text
text_1=tkinter.Entry(window,width=20)
text_1.place(x=95,y=35)
text_2=tkinter.Entry(window,width=20)
text_2.place(x=95,y=95)
text_3=tkinter.Entry(window,width=20)
text_3.place(x=95,y=267)


##Creation of labels
label_1=tkinter.Label(window,text="Enter the first number:",bg='#000080',fg='white')
label_1.place(x=95,y=5)
label_2=tkinter.Label(window,text="Enter the second number:",bg='#000080',fg='white')
label_2.place(x=95,y=65)
label_3=tkinter.Label(window,text="Result:",bg='#000080',fg='white')
label_3.place(x=95,y=237)



window.mainloop()
