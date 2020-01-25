# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:32:28 2019

@author: oyewunmi oluwaseyi
"""
import tkinter as tk
from tkinter import messagebox as msg , LabelFrame
from typing import Tuple


class Gpa ( tk.Tk ):
    """Class for the Gpa calculator"""

    def __init__(self , *args , **kwargs):
        tk.Tk.__init__ ( self , *args , **kwargs )
        photo = tk.Image ( 'photo' , file = 'calculator64.png' )
        self.iconphoto ( True , photo )
        self.tk.call ( 'wm' , 'iconphoto' , self._w , photo )
        self.gpa ()

    def gpa(self):
        'Creation of first dialoge asking for no of courses'
        self.Pass = tk.IntVar ()
        self.Length = tk.IntVar ()
        self.resizable ( 0 , 0 )
        Frame: LabelFrame = tk.LabelFrame ( self , text = 'Gpa Calculator' )
        Frame.pack ( expand = 'yes' )
        Frame['padx'] = 10
        Frame['pady'] = 10
        #        balloon_help = Pmw.Balloon(Frame)
        tk.Label ( Frame , text = "No of Courses" ).pack ()
        vcmd = (self.register ( self.validator ) , '%P' , '%d')
        self.D = tk.Entry ( Frame , validate = 'key' , validatecommand = vcmd )
        self.D.pack ()
        self.D.focus ()
        self.D.bind ( '<Return>' , self.entry )
        But = tk.Button ( Frame , text = 'Enter' , relief = 'raised' , bd = 2 ,
                          command = lambda: But.bind ( '<Button-1>' , self.entry ) )
        But.pack ()

    def entry(self , event):
        'Takes the no of courses to the PanelMaker class'
        try:
            Var = int ( self.D.get () )
            if (Var > 0 and Var < 15):
                PanelMaker ( x = Var )
            else:
                self.bell ()
                self.Pass.set ( "" )
        except ValueError:
            self.bell ()

    def validator(self , e , Type):
        'Validator function for entry box'
        "Validates the entry box to only accept numerals except zero"
        if Type == '1':
            if not e.isdigit ():
                self.bell ()
                return False
            if e == '0':
                self.bell ()
                return False
        return True


class PanelMaker ( tk.Tk ):
    """class for the calculation dialogue"""

    def __init__(self , x , *args , **kwargs):
        tk.Tk.__init__ ( self , *args , **kwargs )
        self._Hold = {}
        self._Hold1 = {}
        self._Hold2 = {}
        self.x = x
        self.resizable ( 0 , 0 )
        self.Panel ()

    def Panel(self):
        'Function creating the whole widgets'
        Frame = tk.LabelFrame ( self , text = 'Dialog' )
        Frame.grid ()
        tk.Label ( Frame , text = 'Courses' , width = 10 ).grid ( row = 0 , column = 0 )
        tk.Label ( Frame , text = 'Units' , width = 10 ).grid ( row = 0 , column = 1 )
        tk.Label ( Frame , text = 'Score' , width = 10 ).grid ( row = 0 , column = 2 )
        Frame2 = tk.LabelFrame ( self )
        Frame2.grid ()
        tk.Label ( Frame2 , text = 'GPA' ).grid ( row = 1 )
        self.L = tk.Label ( Frame2 , text = '' , width = 20 )
        self.L.grid ( row = 1 , column = 1 )
        tk.Label ( Frame2 , text = 'Status' ).grid ( row = 2 )
        self.S = tk.Label ( Frame2 , width = 28 )
        self.S.grid ( row = 2 , column = 1 )

        for rows in range ( self.x ):
            for cols in range ( 1 ):
                Indexer = (rows , cols)
                Course = tk.Entry ( Frame , width = 15 )
                Course.grid ( row = rows + 1 , column = 0 )
                self._Hold[Indexer] = Course
                Course.focus ()
        for rows in range ( self.x ):
            for cols in range ( 1 , 2 ):
                Indexer1 = (rows , cols)
                Units = tk.Spinbox ( Frame , from_ = 0 , to = 6 , width = 15 )
                Units.grid ( row = rows + 1 , column = 1 )
                self._Hold1[Indexer1] = Units
        for rows in range ( self.x ):
            for cols in range ( 2 , 3 ):
                Indexer2: Tuple[int , int] = (rows , cols)
                Score = tk.Spinbox ( Frame , from_ = 0 , to = 100 , width = 15 )
                Score.grid ( row = rows + 1 , column = 2 )
                self._Hold2[Indexer2] = Score
        button = tk.Button ( Frame , text = 'Calculate' , command = lambda: [f () for f in [self.SubmitCallback ,
                                                                                            self.SubmitCallback1 ,
                                                                                            self.SubmitCallback2 ,
                                                                                            self.Get]] )
        button.grid ( row = self.x + 1 , column = 1 )

    def SubmitCallback(self):
        CourseResult = []
        for rows in range ( self.x ):
            currentRow = []
            for cols in range ( 1 ):
                currentRow = []
                Index = (rows , cols)
                currentRow.append ( self._Hold[Index].get () )
            CourseResult.append ( currentRow )
        return CourseResult

    def SubmitCallback1(self):
        Unitresult = []
        for rows in range ( self.x ):
            currentRow = []
            for cols in range ( 1 , 2 ):
                currentRow = []
                Index = (rows , cols)
                currentRow.append ( self._Hold1[Index].get () )
            Unitresult.append ( currentRow )
        return Unitresult

    def SubmitCallback2(self):
        Scoreresult = []
        for rows in range ( self.x ):
            currentRow = []
            for cols in range ( 2 , 3 ):
                currentRow = []
                Index = (rows , cols)
                currentRow.append ( self._Hold2[Index].get () )
            Scoreresult.append ( currentRow )
        return Scoreresult

    @property
    def Get(self):
        try:
            u = []
            s = []
            d = []
            Units = self.SubmitCallback1 ()
            Score = self.SubmitCallback2 ()
            for i in range ( self.x ):
                u.append ( Units[i][0] )
                s.append ( Score[i][0] )
            grdepntslst = []
            for value in u:
                d.append ( int ( value ) )
            for values in s:
                Values = int ( values )
                if Values >= 70:
                    grdepnts = 5
                elif Values >= 60 and Values < 70:
                    grdepnts = 4
                elif Values >= 50 and Values < 60:
                    grdepnts = 3
                elif Values >= 40 and Values < 50:
                    grdepnts = 2
                else:
                    grdepnts = 0
                grdepntslst.append ( grdepnts )
            Total = []
            for unit in range ( self.x ):
                Cumpnts = d[unit] * grdepntslst[unit]
                Total.append ( Cumpnts )
            GrdeTotal = sum ( Total )
            UnitTotal = sum ( d )
            result = GrdeTotal / UnitTotal
            Result = str ( result )
            self.status ( Result )
            return Result
        except ZeroDivisionError:
            msg.showerror ( 'Error' , 'No Course Unit is not provided' )

    def status(self , x):
        """Displays the status of the calculated grade point"""
        self.L.configure ( text = x )
        if (float ( x ) >= 4.5):
            self.S.configure ( text = 'First class' )
            self.S.configure ( fg = 'blue' )
        elif (float ( x ) >= 3.5 and float ( x ) < 4.5):
            self.S.configure ( text = 'Second class upper' )
        elif (float ( x ) >= 2.5 and float ( x ) < 3.5):
            self.S.configure ( text = 'Second class lower' )
        elif (float ( x ) >= 1.5 and float ( x ) < 2.5):
            self.S.configure ( text = 'Third class' )
        else:
            self.S.configure ( text = 'VERY BAD' )
            self.S.configure ( fg = 'red' )


def Test():
    Gpa().mainloop()

if __name__ == '__main__':
    Test ()
