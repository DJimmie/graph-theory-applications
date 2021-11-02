import datetime as dt
from datetime import timedelta



try:
    import tkinter.ttk
    from tkinter import *
#     from tkinter.ttk import *
except:
    from tkinter import *

from tkinter import font as tkFont

from tkinter import messagebox
from tkinter import filedialog

class UI(Tk):
    """WIndow and its attributes."""

    now=dt.date.today().strftime('%B %d, %Y')
    time_of_day=dt.datetime.today().strftime('%I:%M:%S %p')

    w=None
    banner_label=None

    def __init__(self,parent,*args,**kwargs):
        """Create the UI Window"""
        Tk.__init__(self,parent)
        self.parent=UI.w=parent

        # self.banner_text=f'{kwargs["banner"]} - {UI.now}   {UI.time_of_day}'
        self.banner_text=f'{kwargs["banner"]}'
        self.title(kwargs["title"])

        if 'win_color' in kwargs:
            self.window_colors=kwargs['win_color']
        else:
            self.window_colors='#0000CC'
        
        if 'fg' in kwargs:
            self.fg=kwargs['fg']
        else:
            self.fg='#FFFFFF'
        
        if 'window_width' in kwargs:
            self.window_width=kwargs['window_width']
        else:
            self.window_width=self.winfo_screenwidth()

        if 'window_height' in kwargs:
            self.window_height=kwargs['window_height']
        else:
            self.window_height=self.winfo_screenheight()

        if 'image' in kwargs:
            self.image=kwargs['image']
        else:
            self.image=None

        self.initialize()

        
    def initialize(self):
        """Set-up and configure the UI window"""

        self.geometry(f'{self.window_width}x{self.window_height}+0+0')
        self['borderwidth']=4
        self['bg']=self.window_colors

        fg='white'
        self.banner=UI.banner_label=Label(self,text=self.banner_text,fg=self.fg,bg=self.window_colors,font='Ariel 30 bold',image=self.image)
        self.banner.grid(row=0,column=0,columnspan=4,sticky=None)
        
        self.menubar=Menu(self)
        self.menubar.add_command(label="Exit",font='ariel',command=self.bye_bye)
        self.menubar.add_command(label="Instructions",font='ariel',command=None)
        self.config(menu=self.menubar)

        Tk.update(self)

   
    # self.gui_build()

    def bye_bye(self):
        """Close the UI Window on menu Exit"""
        self.destroy()


class Frames(Tk):
    """Frames amd their attributes"""
    def __init__(self,row,col,host=UI.w,*args,**kwargs):
        """Create the UI Window"""

        kwargs=widget_options(**kwargs)
        

        self.F=Frame(host)
        self.F['background']=the_frame_color=kwargs['bg']
        self.F['relief']=kwargs['relief']
        self.F['borderwidth']=5
        self.F.grid(row=row,column=col,pady=kwargs['pady'],padx=kwargs['padx'],sticky=kwargs['sticky'],rowspan=kwargs['rowspan'],columnspan=kwargs['columnspan'])
        banner_text=kwargs['banner_text']

        
        self.frame_banner=Label(self.F,text=banner_text,fg=kwargs['fg'],bg=the_frame_color,font=kwargs['font'],image=kwargs['image'])
        if kwargs['image']!=None:
            self.frame_banner.image=kwargs['image']
        self.frame_banner.grid(row=0,column=0,columnspan=5,pady=15)

class List_box(Tk):
    """Generate List Box"""
    def __init__(self,the_frame,name,row,col,*args,**kwargs):
        """Create the UI List Box with accompaning labels"""
        
        if 'list_items' in kwargs:
            self.list_box_items=kwargs['list_items']
        else:
            self.list_box_items=['TBD']

        kwargs=widget_options(**kwargs)

        font=kwargs['font']
        bg=kwargs['bg']
        fg=kwargs['fg']
        relief=kwargs['relief']

        # if 'font' in kwargs:
            
        # else:
        #     font='Ariel 12 bold'

        if 'fw' in kwargs:
            fw=kwargs['fw']
        else:
            fw=10

        if 'height' in kwargs:
            height=kwargs['height']
        else:
            height=int(.25*fw)

        if 'selectmode' in kwargs:
            selectmode=kwargs['selectmode']
        else:
            selectmode=SINGLE

        self.txt=name
        self.list_label=Label(the_frame,text=self.txt,bg='blue',fg='yellow',font='Ariel 12 bold',relief=relief)
        self.list_box=Listbox(the_frame,font=font, bg=bg,borderwidth=2,height=height,width=fw,selectmode=selectmode)
        
        self.list_label.grid(row=row,column=col,columnspan=kwargs['columnspan'],pady=kwargs['pady'],sticky=kwargs['sticky'])
        self.list_box.grid(row=(row+1),column=col,columnspan=kwargs['columnspan'],pady=kwargs['pady'],sticky=kwargs['sticky'])

        self.populate_list()

    def populate_list(self):

        for i,k in enumerate(self.list_box_items,start=1):
            self.list_box.insert(i,k)
            
class Textbox(Tk):

    def __init__(self,the_frame,name,row,col,*args,**kwargs):
        """Create the UI List Box with accompaning labels"""

        if 'font' in kwargs:
            font=kwargs['font']
        else:
            font='Ariel 12 bold'

        if 'width' in kwargs:
            width=kwargs['width']
        else:
            width=10

        if 'height' in kwargs:
            height=kwargs['height']
        else:
            height=10

        if 'state' in kwargs:
            state=kwargs['state']
        else:
            state=NORMAL

        if 'sticky' in kwargs:
            sticky=kwargs['sticky']
        else:
            sticky=W

        if 'pady' in kwargs:
            pady=kwargs['pady']
        else:
            pady=1

        if 'padx' in kwargs:
            padx=kwargs['padx']
        else:
            padx=1

        if 'columnspan' in kwargs:
            columnspan=kwargs['columnspan']
        else:
            columnspan=1

        

        self.text_box_label=Label(the_frame,text=name,bg='blue',fg='yellow',font='Ariel 12 bold')
        
        self.text_box=Text(the_frame,
        borderwidth=1,
        height=height,
        width=width,
        font=font,
        wrap=WORD,
        state=state)

        # self.yscroll = Scrollbar(the_frame,orient="vertical",command=self.text_box.yview).grid(row=(row+1),column=col,sticky=N+S+E)

        self.text_box_label.grid(row=row,column=col,columnspan=columnspan,pady=1,sticky=sticky)
        self.text_box.grid(row=(row+1),column=col,columnspan=columnspan,pady=pady,sticky=sticky)
        # self.text_box['yscrollcommand']=self.yscroll.set


class CheckBoxes(Tk):
    
    def __init__(self,the_frame,name,check_label,row,col,command,*args,**kwargs):
        """Create the UI Checkbox Box with accompaning labels"""
        
        self.check_box_label=Label(the_frame,text=name,bg='blue',fg='yellow',font='Ariel 12 bold')

        self.var=IntVar()
        self.check_box=Checkbutton(master=the_frame,
        text=check_label,
        highlightcolor='red',
        selectcolor='black',
        bg=the_frame['background'],
        fg='white',
        font='Ariel 15 bold',
        variable=self.var,
        command=command)

        self.check_box_label.grid(row=row,column=col,columnspan=1,pady=1,sticky=W)
        self.check_box.grid(row=(row+1),column=col,pady=1,sticky=W)

class Labels(Tk):
    def __init__(self,the_frame,name,row,col,*args,**kwargs):
        """Create the UI Labels"""

        if 'pady' in kwargs:
            pady=kwargs['pady']
        else:
            pady=None

        if 'padx' in kwargs:
            padx=kwargs['padx']
        else:
            padx=None

        if 'font' in kwargs:
            font=kwargs['font']
        else:
            font='Ariel 12 bold'
        
        if 'bg' in kwargs:
            bg=kwargs['bg']
        else:
            bg='blue'

        if 'fg' in kwargs:
            fg=kwargs['fg']
        else:
            fg='yellow'
        
        self.label=Label(the_frame,text=name,bg=bg,fg=fg,font=font)
        self.label.grid(row=row,column=col,columnspan=1,pady=pady,padx=padx,sticky=W)

class Buttons(Tk):
    def __init__(self,the_frame,name,row,col,width,command,*args,**kwargs):
        """Create the UI Buttons with accompaning labels"""

        if 'pady' in kwargs:
            pady=kwargs['pady']
        else:
            pady=None

        if 'padx' in kwargs:
            padx=kwargs['padx']
        else:
            padx=None

        if 'font' in kwargs:
            font=kwargs['font']
        else:
            font='Ariel 12 bold'
        
        if 'bg' in kwargs:
            bg=kwargs['bg']
        else:
            bg='black'

        if 'fg' in kwargs:
            fg=kwargs['fg']
        else:
            fg='yellow'

        if 'sticky' in kwargs:
            sticky=kwargs['sticky']
        else:
            sticky=None


        self.button = Button(the_frame, 
        text=name,
        width=width,
        fg=fg,
        bg=bg,
        font=font,
        command=command)

        self.button.grid(row=row,column=col,pady=pady,padx=padx,sticky=sticky)

class Combos(Tk):
    def __init__(self,the_frame,name,row,col,drop_down_list,*args,**kwargs):
        """Create the UI Entry fields with accompaning labels"""
        
        self.txt=name
        self.combo_label=Label(the_frame,text=self.txt,bg='blue',fg='yellow',font='Ariel 12 bold')
        
        if 'type' in kwargs:
            if (kwargs['type']=='IntVar'):
                self.combo_var=IntVar()
            elif (kwargs['type']=='DoubleVar'):
                self.combo_var=DoubleVar()
        else:
            self.combo_var=StringVar()

        if 'pady' in kwargs:
            pady=kwargs['pady']
        else:
            pady=1

        if 'fw' in kwargs:
            fw=kwargs['fw']
        else:
            fw=30

        if 'state' in kwargs:
            state=kwargs['state']
        else:
            state=NORMAL
        

        self.combo_box_list=drop_down_list
        self.combo=ttk.Combobox(the_frame,font='Ariel 15 bold',width=fw,
                                   background='yellow',textvariable=self.combo_var,
                                   values=self.combo_box_list,
                                   state=state)

        if 'direction' in kwargs:
            if kwargs['direction']=='HORZ':
                self.combo_label.grid(row=row,column=col,columnspan=1,pady=1,sticky=W)
                self.combo.grid(row=row,column=(col+1),columnspan=1,pady=1,sticky=W)
        else:
            # self.combo_label.grid(row=row,column=col,columnspan=1,pady=pady,sticky=W)
            # self.combo.grid(row=(row+1),column=col,columnspan=1,pady=pady,sticky=W)

            self.combo_label.grid(row=row,column=col,columnspan=1,pady=(0,self.combo_label.winfo_reqheight()),sticky=NW)
            self.combo.grid(row=row,column=col,columnspan=1,pady=(self.combo_label.winfo_reqheight(),0),sticky=NW)

            print(f'winfo height---->{self.combo_label.winfo_reqheight()}')


        


class Entries(Tk):
    def __init__(self,the_frame,name,row,col,fw=30,*args,**kwargs):
        """Create the UI Entry fields with accompaning labels"""
        field_widths=fw
        self.txt=name
        self.entry_label=Label(the_frame,text=self.txt,bg='blue',fg='yellow',font='Ariel 12 bold')

        kwargs=widget_options(**kwargs)

        if 'type' in kwargs:
            if (kwargs['type']=='IntVar'):
                self.entry_var=IntVar()
            elif (kwargs['type']=='DoubleVar'):
                self.entry_var=DoubleVar()
        else:
            self.entry_var=StringVar()
        
        
        self.entry=Entry(the_frame,font='Ariel 15 bold',width=field_widths,
                                   background='yellow',textvariable=self.entry_var,highlightbackground='pink',highlightthickness=5,state=kwargs['state'])

        if 'direction' in kwargs:
            if kwargs['direction']=='HORZ':
                self.entry_label.grid(row=row,column=col,columnspan=1,pady=kwargs['pady'],sticky=W)
                self.entry.grid(row=row,column=(col+1),columnspan=1,pady=1,sticky=W)
        else:
            self.entry_label.grid(row=row,column=col,columnspan=1,pady=kwargs['pady'],sticky=W)
            self.entry.grid(row=(row+1),column=col,columnspan=1,pady=1,sticky=W)


class RadioButtons(Tk):
    def __init__(self,the_frame,name,row,col,command,radio_dict,*args,**kwargs):
        """Create the UI radiobuttons with accompaning labels"""
        # field_widths=fw

        if 'bg' in kwargs:
            bg=kwargs['bg']
        else:
            bg='blue'

        if 'fg' in kwargs:
            fg=kwargs['fg']
        else:
            fg='yellow'

        if 'font' in kwargs:
            font=kwargs['fg']
        else:
            font='Ariel 12 bold'

        if 'padx' in kwargs:
            padx=kwargs['padx']
        else:
            padx=None

        self.var = IntVar()

        if 'type' in kwargs:
            if (kwargs['type']=='StringVar'):
                self.var=StringVar()
        else:
            self.var=IntVar()

        self.txt=name
        self.radio_label=Label(the_frame,text=self.txt,bg=bg,fg=fg,font='Ariel 12 bold')
        self.radio_label.grid(row=row,column=col,columnspan=1,pady=1,padx=padx,sticky=W)
        row+=1
        for key, val in radio_dict.items():
                self.radio=Radiobutton(the_frame, 
                        text=key,
                        padx = padx, 
                        variable=self.var, 
                        command=command,
                        value=val,
                        bg=bg,fg=fg,
                        selectcolor='navy',
                        font=font)
                    
                # print(row)
                self.radio.grid(row=(row),column=col,columnspan=1,pady=1,padx=None,sticky=W)
                row+=1

class Notebooks(Tk):
    def __init__(self,the_frame,row,col,*args,**kwargs):
        """Create the UI radiobuttons with accompaning labels"""
        # field_widths=fw

        kwargs=widget_options(**kwargs)
        
        noteStyle = ttk.Style()
        noteStyle.theme_use('default')
        noteStyle.configure("TNotebook", background='black', borderwidth=10)
        noteStyle.configure("TNotebook.Tab", background="blue", borderwidth=0,font='Ariel 12 bold')

        noteStyle.map("TNotebook.Tab", background=[("selected", 'green')])

        self.nb=ttk.Notebook(master=the_frame,style='TNotebook')

        self.nb.grid(row=row,column=col)


class MenuButtons(Tk):
    def __init__(self,the_frame,text,row,col,check_buttons,*args,**kwargs):
        """Create Menubuttons"""

        kwargs=widget_options(**kwargs)

        self.menubutton=Menubutton(
                                    the_frame,
                                    text=text,
                                    font=kwargs['font'],
                                    bg=kwargs['bg'],
                                    fg=kwargs['fg'],
                                    image=kwargs['image'],
                                    relief=kwargs['relief'],
                                    state=kwargs['state']
                                    )

        if kwargs['image']!=None:
            self.menubutton.image=kwargs['image']
        
        self.menubutton.grid(row=row,column=col,columnspan=1,pady=kwargs['pady'],sticky=kwargs['sticky'])

        self.menubutton.menu =  Menu ( self.menubutton, tearoff = 0 )
        self.menubutton["menu"] =  self.menubutton.menu


        num_checkbuttons=len(check_buttons['label'])
        c=0
        for i in range(num_checkbuttons):
            
           
            self.menubutton.menu.add_checkbutton (label=check_buttons['label'][c],
                                    variable=check_buttons['variable'][c],
                                    activebackground=check_buttons['activebackground'][c],
                                    font=check_buttons['font'][c],
                                    command=check_buttons['command'][c]
                                    )

            c+=1


class Tree(Tk):
    """Create the UI Entry fields with accompaning labels"""
    def __init__(self,the_frame,row,col,columns,style,*args,**kwargs):

        if 'height' in kwargs:
            height=kwargs['height']
        else:
            height=20

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure(style, highlightthickness=10, bd=0, rowheight=120, font=('Calibri', 10))
        self.style.configure("my.Treeview.Heading", font=('Calibri', 10,'bold'),foreground='white',background='black') 

        
        self.tree=ttk.Treeview(the_frame,columns=columns,style=style,height=height)

        yscrollbar = ttk.Scrollbar(the_frame,orient='vertical', command=self.tree.yview)
        xscrollbar = ttk.Scrollbar(the_frame,orient='horizontal', command=self.tree.xview)

        self.tree.configure(yscrollcommand = yscrollbar.set, xscrollcommand = xscrollbar.set, selectmode="browse")

        self.tree.grid(row=row,column=col,columnspan=2,pady=1,sticky=W)

        yscrollbar.config(command=self.tree.yview)
        xscrollbar.config(command=self.tree.xview)

        yscrollbar.grid(row=row, column=col+2, sticky='ns')
        xscrollbar.grid(row=row+1, column=col, columnspan=2,sticky='we')


def widget_options(**kwargs):
    """The various and most used widget options."""
    
    if 'pady' in kwargs:
        pady=kwargs['pady']
    else:
        kwargs['pady']=1

    if 'padx' in kwargs:
        padx=kwargs['padx']
    else:
        kwargs['padx']=1

    if 'font' in kwargs:
        font=kwargs['font']
    else:
        kwargs['font']='Ariel 12 bold'
    
    if 'bg' in kwargs:
        bg=kwargs['bg']
    else:
        kwargs['bg']='white'

    if 'fg' in kwargs:
        fg=kwargs['fg']
    else:
        kwargs['fg']='black'

    if 'sticky' in kwargs:
        sticky=kwargs['sticky']
    else:
        kwargs['sticky']=None

    if 'image' in kwargs:
        image=kwargs['image']
    else:
        kwargs['image']=None

    if 'state' in kwargs:
        state=kwargs['state']
    else:
        kwargs['state']='normal'

    if 'relief' in kwargs:
        relief=kwargs['relief']
    else:
        kwargs['relief']=RAISED

    if 'rowspan' in kwargs:
        rowspan=kwargs['rowspan']
    else:
        kwargs['rowspan']=1
    
    if 'columnspan' in kwargs:
        columnspan=kwargs['columnspan']
    else:
        kwargs['columnspan']=1

    if 'banner_text' in kwargs:
        banner_text=kwargs['banner_text']
    else:
        kwargs['banner_text']='TBD'


    print(kwargs)


    return kwargs