from tkinter import *
window = Tk()
window.title('LYFDROPS')
canvas = Canvas(window,width=900,height=700,bg='steelblue')
canvas.pack()
my_image =PhotoImage(file = 'C:\\Users\\Akash\\Desktop\\lyfdrop.png' )
canvas.create_image(300,170,image = my_image,anchor = NW)

window.mainloop()
