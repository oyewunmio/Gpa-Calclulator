try:
 import Tkinter
except:
 import tkinter as Tkinter

import time

class Message(Tkinter.Toplevel): #class for message display
 def __init__(self,width=250,height=50,text="course is too small or too large \n Try again later",bg="white",font=('arial 10 bold italic')):#self is the class initializer
  Tkinter.Toplevel.__init__(self)
  self.font=font
  self.text=text
  self.bg=bg
  self.width=width
  self.height=height
  self.focus_force()
  self.overrideredirect(True)
  self.coordinate_position()
  self.creating_label()
  self.timer_is_starting()

 def creating_label(self):
  Tkinter.Label(self,text=self.text,bg=self.bg,font=self.font).pack(expand='yes',fill='both')
  return

 def coordinate_position(self):
  self.geometry("%dx%d+%d+%d" % (self.width,self.height,\
   self.winfo_screenwidth()/2-(self.width/2),\
   self.winfo_screenheight()/2-(self.height/2),\
   ))
  return

 def timer_is_starting(self):
  x=1.0
  for i in range(110):
   time.sleep(0.02)
   self.update_idletasks()
   self.update()
   self.attributes('-alpha',x)
   x=x-0.01
  return

def main():
 #root=Tkinter.Tk()
 Message() #calling the Message function
 #Tkinter.Button(root,text="Test",command=Message).pack()

 return

# Main Trigger
if __name__ == '__main__':
 main()
