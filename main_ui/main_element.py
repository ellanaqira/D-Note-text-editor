from tkinter import *
from tkinter import ttk
from main_ui.main_frame import Main_frame
from main_backend.backend import Backend
from aset.aset_img import Aset_img

class Main_element:
    def __init__(self, root):
        self.root = root
        self.main_frame  = Main_frame()
        self.main_backend = Backend()
        self.aset_img = Aset_img()

# =====(TEXT TOOLS BAR)=====
    # SEPARATOR LINE CLASS
    class Separator:
        def __init__(self, line_img, frame_name, row, column):
            self.line_img = line_img
            self.frame_name = frame_name
            self.row = row
            self.column = column
        def separator_line(self):
            line = Label(self.frame_name,
                         image=self.line_img,)
            line.grid(row=self.row, column=self.column, padx=8, pady=5)

    def menu_display(self):
        # UNDO BUTTON
        def undo_command_btn():
            try:
                textbox.edit_undo()
            except TclError:
                pass  # No undo available
        undo_btn = Button(self.main_frame.frame_top,
                          bd=0,
                          image=self.aset_img.undo_icon,
                          command=undo_command_btn)
        undo_btn.grid(row=0, column=0, padx=(8,5))

        # REDO BUTTON
        def redo_command_btn():
            try:
                textbox.edit_redo()
            except TclError:
                pass  # No redo available
        redo_btn = Button(self.main_frame.frame_top,
                          bd=0,
                          image=self.aset_img.redo_icon,
                          command=redo_command_btn)
        redo_btn.grid(row=0, column=1, padx=(5,0))

        # SEPARATOR LINE
        separator_line = self.Separator(self.aset_img.vertical_line,
                                         self.main_frame.frame_top, 0, 2)
        separator_line.separator_line()

        # FONT FAMILY
        font_family = ["Consolas", "Calibri", "System Ui", "Times New Roman", "Noto Mono",
                       "Monospace", "Roboto", "Nimbus Mono", "Sans Serif", "Dejavu Serif",
                       "Arial", "Arial Narrow", "Impact", "Magneto", "Lucida sans", "Papyrus",
                       "Comic Sans", "Cambria"]
        font_family.sort()
        drop_font_family = ttk.Combobox(self.main_frame.frame_top,
                                        values=font_family,
                                        width=15)
        drop_font_family.grid(row=0, column=3, padx=(0,5))
        drop_font_family.set("Consolas")
        def change_font_style(event):
            self.main_backend.change_font(textbox, drop_font_family, font_size_menu)
        drop_font_family.bind("<<ComboboxSelected>>", change_font_style)

        # FONT SIZE
        size_list = []
        for i in range (1,65):
            size_list.append(i)
        font_size_menu = ttk.Combobox(self.main_frame.frame_top,
                                      width=4,
                                      font=('system ui', 10),
                                      values=size_list)
        font_size_menu.grid(row=0, column=4, padx=(5,5))
        font_size_menu.set(13)
        def change_font_size_bind(event):
            self.main_backend.change_font_size(font_size_menu, textbox)
        font_size_menu.bind("<<ComboboxSelected>>", change_font_size_bind)

        # FONT COLOR BUTTON
        label_color = Label(self.main_frame.frame_top,
                            bg="#ffffff",
                            relief='raised',
                            bd=1,
                            text=" ",
                            pady=2)
        label_color.grid(row=0, column=5, padx=(5,0))
        font_color_btn = Button(self.main_frame.frame_top,
                            text="A",
                            relief='raised',
                            font=('Times New Roman', 12, 'bold'),
                            bd=1,
                            padx=4,
                            pady=1,
                            command=lambda: self.main_backend.change_font_color(textbox, file_name_label, label_color))
        font_color_btn.grid(row=0, column=6)

        # SEPARATOR LINE
        separator_line = self.Separator(self.aset_img.vertical_line,
                                         self.main_frame.frame_top, 0, 7)
        separator_line.separator_line()
        # SEARCH FOR WORD
        search_btn = Button(self.main_frame.frame_top,
                            image=self.aset_img.search_icon,
                            bd=0,
                            command=lambda: self.main_backend.open_search_win(self.root, textbox))
        search_btn.grid(row=0, column=10)

        # SEPARATOR LINE
        separator_line = self.Separator(self.aset_img.vertical_line,
                                         self.main_frame.frame_top, 0, 11)
        separator_line.separator_line()

# =====(TEXT AREA/TEXT BOX)=====
        # TRIANGLE LEFT
        triangle_l = Label(self.main_frame.frame_midle,
                         image=self.aset_img.left_triangle_img,
                         anchor='w',
                         bd=0,
                         bg="#ffffff")
        triangle_l.grid(row=0, column=0, padx=(4,0))

        # FILE NAME LABEL
        file_name_label = Label(self.main_frame.frame_midle,
                           text='Untitled',
                           font=('calibri', 11),
                           fg="#242424",
                           bg="#FFFFFF",
                           anchor='w',
                           padx=50,
                           pady=3)
        file_name_label.grid(row=0, column=1, padx=(0,0), pady=(1,0))

        # TRIANGLE RIGHT
        triangle_r = Label(self.main_frame.frame_midle,
                         image=self.aset_img.right_triangle_img,
                         anchor='w',
                         bd=0,
                         bg="#ffffff")
        triangle_r.grid(row=0, column=2)

        # SCROLLBAR
        scrollbar_x = Scrollbar(self.main_frame.frame_textbox,
                                orient='horizontal',
                                bg="#FFFFFF")
        scrollbar_x.pack(side='bottom', fill='x')
                            
        scrollbar_y = Scrollbar(self.main_frame.frame_textbox,
                                bg="#FFFFFF")
        scrollbar_y.pack(side="right", fill="y")

        # TEXT BOX
        textbox = Text(self.main_frame.frame_textbox,
                       font=('consolas', 13),
                       fg="#242424",
                       bd=1,
                       undo=True,
                       wrap=NONE,
                       xscrollcommand= scrollbar_x.set,
                       yscrollcommand= scrollbar_y.set)
        textbox.pack(expand=True, fill='both', padx=(3,0))
        scrollbar_x.config(command=textbox.xview)
        scrollbar_y.config(command=textbox.yview)

        # STATUS BAR
        status_bar = Label(self.main_frame.frame_bottom,
                            text="Line 1, Column 1",
                            height=1,
                            pady=3,
                            bg="#DBDBDB")
        status_bar.pack(fill='x')

# =====(FILE MENU)=====
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File',
                            menu=file_menu)
        # NEW FILE BUTTON
        file_menu.add_command(label="New",
                              image=self.aset_img.newfile_icon,
                              compound='left',
                              accelerator="| Ctrl+N ",
                              command=lambda: self.main_backend.new_file_btn(textbox, file_name_label, status_bar))
        #NEW FILE COMMNAD FOR KEYBOARD
        def new_file_keyboard(event):
            self.main_backend.new_file_btn(textbox, file_name_label, status_bar)
        textbox.bind("<Control-Key-n>", new_file_keyboard)
        textbox.bind("<Control-Key-N>", new_file_keyboard)
        # OPEN FILE BUTTON
        file_menu.add_command(label="Open",
                              image=self.aset_img.openfile_icon,
                              compound='left',
                              accelerator="| Ctrl+O ",
                              command=lambda: self.main_backend.open_file_btn(textbox,
                                                                              file_name_label,
                                                                              status_bar,
                                                                              self.root,
                                                                              self.aset_img.question_mark))
        # OPEN FILE COMMAND FOR KEYBOARD
        def open_file_keyboard(event):
            self.main_backend.open_file_btn(textbox,
                                            file_name_label,
                                            status_bar,
                                            self.root,
                                            self.aset_img.question_mark)
        textbox.bind("<Control-Key-o>", open_file_keyboard)
        textbox.bind("<Control-Key-O>", open_file_keyboard)

        # SAVE FILE BUTTON
        file_menu.add_command(label="Save",
                              image=self.aset_img.save_icon,
                              compound='left',
                              accelerator="| Ctrl+S ",
                              command=lambda: self.main_backend.save_file_btn(textbox, file_name_label, status_bar))
        
        # SAVE FILE COMMAND FOR KEYBOARD
        def save_file_keyboard(event):
             self.main_backend.save_file_btn(textbox, file_name_label, status_bar)
        textbox.bind("<Control-Key-s>", save_file_keyboard)
        textbox.bind("<Control-Key-S>", save_file_keyboard)
        file_menu.add_separator()

        # EXIT BUTTON
        file_menu.add_command(label="Exit",
                              image=self.aset_img.exit_icon,
                              compound='left',
                              command=lambda:self.main_backend.exit_command_btn(self.root))
        separator_line.separator_line()

# =====(EDIT MENU)=====
        edit_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit',
                            menu=edit_menu)
        #SELECT ALL BUTTON
        edit_menu.add_command(label='Select all',
                              accelerator="| Ctrl+A ",
                              image=self.aset_img.sel_all_icon,
                              compound='left',
                              command=lambda:self.main_backend.select_all_btn(textbox))
        #SELECT ALL COMMAND FOR KEYBOARD
        def select_all_keyboard(event):
            textbox.tag_add(SEL, '1.0', 'end-1c')
            return 'break'
        textbox.bind("<Control-Key-a>", select_all_keyboard)
        textbox.bind("<Control-Key-A>", select_all_keyboard)
        # COPY BUTTON
        edit_menu.add_command(label='Copy', 
                              accelerator="| Ctrl+C ", 
                              image=self.aset_img.copy_icon,
                              compound='left',
                              command=lambda:self.main_backend.copy_command(textbox))
        # CUT BUTTON
        edit_menu.add_command(label='Cut', 
                              accelerator="| Ctrl+X ", 
                              image=self.aset_img.cut_icon,
                              compound='left',
                              command=lambda:self.main_backend.cut_command(textbox))
        # PASTE BUTTON
        edit_menu.add_command(label='Paste',
                              accelerator="| Ctrl+V ",
                              image=self.aset_img.paste_icon,
                              compound='left',
                              command=lambda:self.main_backend.paste_command(textbox))

# =====(TOOLS MENU)=====
        tool_menubar = Menu(menubar, tearoff=False)
        menubar.add_cascade(label='Tools', menu=tool_menubar)
        # DOCUMENT INFO
        tool_menubar.add_command(label='Document info',
                                 command=lambda: self.main_backend.doctinfo_command(self.root, textbox, file_name_label))
        # TIME BUTTON
        tool_menubar.add_command(label='Time',
                              command=lambda: self.main_backend.print_out_time(textbox))
        # DATE BUTTON
        tool_menubar.add_command(label='Date',
                              command=lambda: self.main_backend.print_out_date(textbox))
        tool_menubar.add_separator()
        # ASCII ART LIBRARY BUTTON
        tool_menubar.add_command(label="Ascii art",
                              image=self.aset_img.pacman_emote,
                              command=lambda: self.main_backend.open_ascii_window(self.root),
                              compound='left')

# =====(THEME MENU)=====
        theme_menu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Theme",
                            menu=theme_menu)
        theme_menu.add_command(label="Light",
                               image=self.aset_img.white_ball,
                               compound='left',
                               background="#FFFFFF",
                               command=lambda: self.main_backend.light_theme_command(textbox, file_name_label, triangle_l, triangle_r,
                                                                                     scrollbar_x, scrollbar_y, status_bar))
        theme_menu.add_command(label="Paper",
                               image=self.aset_img.paper_ball,
                               compound='left',
                               background="#dad3c2",
                               command=lambda: self.main_backend.paper_theme_command(textbox, file_name_label, triangle_l, triangle_r,
                                                                                     scrollbar_x, scrollbar_y, status_bar))
        theme_menu.add_command(label="Clasic",
                               image=self.aset_img.clasic_ball,
                               compound='left',
                               background="#8B8656",
                               foreground="#FFFFFF",
                               command=lambda: self.main_backend.clasic_theme_command(textbox, file_name_label, triangle_l, triangle_r,
                                                                                    scrollbar_x, scrollbar_y, status_bar))
        theme_menu.add_command(label="Dark",
                               image=self.aset_img.black_ball,
                               compound='left',
                               background="#5C5C5C",
                               foreground="#FFFFFF",
                               command=lambda: self.main_backend.dark_theme_command(textbox, file_name_label, triangle_l, triangle_r,
                                                                                    scrollbar_x, scrollbar_y, status_bar))
        theme_menu.add_command(label="Deep Ocean",
                               image=self.aset_img.blue_ball,
                               compound='left',
                               background="#34435A",
                               foreground="#FFFFFF",
                               command=lambda: self.main_backend.deepocean_theme_command(textbox, file_name_label, triangle_l, triangle_r,
                                                                                    scrollbar_x, scrollbar_y, status_bar))
        theme_menu.add_command(label="Custom",
                               image=self.aset_img.color_ball,
                               compound='left',
                               command=lambda: self.main_backend.custom_theme_command(textbox, file_name_label, triangle_l, triangle_r,
                                                                                      scrollbar_x, scrollbar_y, status_bar))

# =====(HELP MENU)=====
        help_menu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Help",
                            menu=help_menu)
        # ABOUT DNOTE
        help_menu.add_command(label="About",
                              image=self.aset_img.exclamation_mark,
                              compound='left',
                              command=lambda: self.main_backend.about_window(self.root,
                                                                     self.aset_img.Dnote_icon))

# =====(CALL REALTIME CHANGES LOGIC)=====
        self.main_backend.textbox_changes_command(textbox, file_name_label, "Untitled", status_bar)