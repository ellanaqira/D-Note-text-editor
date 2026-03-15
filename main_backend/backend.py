from tkinter import *
from tkinter import messagebox, filedialog as fd
from tkinter.colorchooser import askcolor
from datetime import *
import os

class Backend:
    def realtime_label(self, event, textbox_name, textbox_content, file_label, file_name):
        realtype_typing = (textbox_name.get('1.0', 'end-1c') + event.char)
        if realtype_typing == textbox_content:
            file_label.config(text=file_name)
        else:
            file_label.config(text=f"*{file_name}")

# =====(FILE MENU)=====
    # NEW FILE BUTTON COMMAND
    def new_file_btn(self, textbox_name, file_label, status_bar):
        textbox_content = textbox_name.get('1.0', 'end-1c')

        if textbox_content:
                option_win = Toplevel()
                option_win.geometry('430x150')
                option_win.title("Create a New File")
                option_win.resizable(False,False)

                frame_all = Frame(option_win, bg="#FFFFFF")
                frame_all.pack(expand=True, fill='both')

                frame1 = Frame(frame_all, bg="#FFFFFF")
                frame1.pack()

                frame2 = Frame(frame_all, bg="#E4E4E4")
                frame2.pack(expand=True, fill='both')

                info_opsion = Label(frame1,text="""Do you want to save change to File?""",
                                font=('calibri', 14),
                                bg="#FFFFFF",
                                pady=30)
                info_opsion.grid(row=0, column=1)
                # NEW FILE SAVE BUTTON
                def save_newfile():
                    option_win.destroy()
                    newfile_save = fd.asksaveasfile(initialdir="/",
                                                    title="Save new file",
                                                    filetypes=[('text file', '*.txt'),
                                                               ('all file', '*.*')])
                    newfile_save.close()
                    file_label.config(text="Untitled")
                    textbox_name.delete("1.0", "end")
                save_btn = Button(frame2,
                                text='Save',
                                bg="#DDDDDD",
                                font=('calibri', 11),
                                bd=1,
                                width=12,
                                command=save_newfile)
                save_btn.grid(row=0, column=0, pady=(15), padx=(15,0))
                # NEW FILE DONT SAVE BUTTON
                def dontsave_newfile():
                    file_label.config(text="Untitled")
                    textbox_name.delete("1.0", "end")
                    option_win.destroy()
                dontsave_btn = Button(frame2,
                                    text="Don't Save",
                                    bg="#DDDDDD",
                                    font=('calibri', 11),
                                    bd=1,
                                    width=12,
                                    command=dontsave_newfile)
                dontsave_btn.grid(row=0, column=1, pady=(15), padx=10)
                self.textbox_changes_command(textbox_name, file_label, "Untitled", status_bar)
                # CANCEL BUTTON
                cancel_btn = Button(frame2,
                                    text="Cancel",
                                    bg="#DDDDDD",
                                    font=('calibri', 11),
                                    bd=1,
                                    width=12,
                                    command=lambda: option_win.destroy())
                cancel_btn.grid(row=0, column=2, pady=(15), padx=(0,15))

        else:
            return None

    # OPEN FILE BUTTON COMMAND
    def open_file_btn(self, textbox_name, file_label, status_bar, main_window, quetion_mark_icon):
        textbox_content = textbox_name.get("1.0", "end-1c")
        open_raw_file = fd.askopenfilename(filetypes=[("text file", "*.txt"),
                                                      ("all file", "*.*")],
                                                      initialdir="/")
        if open_raw_file:
            if textbox_content:
                option_window = Toplevel(main_window)
                option_window.attributes('-topmost', bool(True))
                option_window.geometry('385x200')
                option_window.title("Option")
                option_window.resizable(False,False)

                frame_all = Frame(option_window, bg="#FFFFFF")
                frame_all.pack(expand=True, fill='both')

                frame1 = Frame(frame_all, bg="#FFFFFF")
                frame1.pack()

                frame2 = Frame(frame_all, bg="#DDDDDD")
                frame2.pack(expand=True, fill='both')


                img_label = Label(frame1,
                                image=quetion_mark_icon,
                                bg="#FFFFFF")
                img_label.grid(row=0, column=0, padx=(0,25))

                info_opsion = Label(frame1,text="""Are you want to merge the
previous file with the opened file?,
or
Delete the previous file and
replace with the opened file?""",
                                font=('calibri', 11),
                                bg="#FFFFFF",
                                pady=20)
                info_opsion.grid(row=0, column=1)
                # MERGE FILE BUTTON
                def merge_command():
                    merged_file = open(open_raw_file, "r")
                    try:
                        textbox_name.insert("1.0", merged_file.read())
                    except UnicodeDecodeError:
                        option_window.destroy()
                        file_label.config(text="Untitled")
                        messagebox.showerror("error", "File format not suported")
                    merged_file_name = os.path.basename(open_raw_file)
                    file_label.config(text="Untitled")
                    option_window.destroy()
                    self.textbox_changes_command(textbox_name, file_label, "Untitled", status_bar)
                merge_btn = Button(frame2,
                                text='Merge',
                                bg="#DDDDDD",
                                bd=1,
                                width=10, 
                                command=merge_command)
                merge_btn.grid(row=0, column=0, padx=(10), pady=(10,0))
                # REPLACE FILE BUTTON
                def replace_command():
                    textbox_name.delete("1.0", "end-1c")
                    replaced_file = open(open_raw_file, "r")
                    try:
                        textbox_name.insert("1.0", replaced_file.read())
                    except UnicodeDecodeError:
                        option_window.destroy()
                        replaced_file_name = os.path.basename(open_raw_file)
                        file_label.config(text=replaced_file_name)
                        messagebox.showerror("error", "File format not suported")
                    replaced_file_name = os.path.basename(open_raw_file)
                    file_label.config(text=replaced_file_name)
                    option_window.destroy()
                    self.textbox_changes_command(textbox_name, file_label, replaced_file_name, status_bar)
                replace_btn = Button(frame2,
                                    text='Replace',
                                    bg="#DDDDDD",
                                    bd=1,
                                    width=10,
                                    command=replace_command)
                replace_btn.grid(row=0, column=1, padx=(10), pady=(10,0))
                # CANCEL BUTTON
                cancel_btn = Button(frame2,
                                    text='Cancel',
                                    bg="#DDDDDD",
                                    bd=1,
                                    width=10,
                                    command=lambda:option_window.destroy())
                cancel_btn.grid(row=0, column=2, padx=(10), pady=(10,0))
            else:
                textbox_name.delete("1.0", "end-1c")
                opened_file_name = os.path.basename(open_raw_file)
                file_label.config(text=opened_file_name)
                opened_file = open(open_raw_file, "r")
                try:
                    textbox_name.insert("1.0", opened_file.read())
                except UnicodeDecodeError:
                    messagebox.showerror("error", "File format not suported")
                opened_file.close()
                self.textbox_changes_command(textbox_name, file_label, opened_file_name, status_bar)
        else:
            print('no file choosen')

    # SAVE FILE BUTTON COMMAND
    def save_file_btn(self, textbox_name, file_label, status_bar):
        saved_file = fd.asksaveasfilename(filetypes=[("text file", "*.txt"),
                                                     ("all file", "*.*")],
                                          initialdir="/")
        if saved_file:
            saved_file_name = os.path.basename(saved_file)
            file_label.config(text=saved_file_name)
            saved_file = open(saved_file, "w")
            saved_file.write(textbox_name.get("1.0", "end-1c"))
            saved_file.close()
            self.textbox_changes_command(textbox_name, file_label, saved_file_name, status_bar)
        else:
            print("no file saved")

    # EXIT BUTTON COMMAND
    def exit_command_btn(self, main_window):
        main_window.destroy()

# =====(EDIT MENU)=====
    # SELECT ALL BUTTON COMMAND
    def select_all_btn(self, textbox_name):
        textbox_name.tag_add(SEL, '1.0', 'end-1c')
        return 'break'
    # COPY BUTTON COMMAND
    def copy_command(self, textbox_name):
        textbox_name.event_generate("<<Copy>>")
    # CUT BUTTON COMMAND
    def cut_command(self, textbox_name):
        textbox_name.event_generate("<<Cut>>")
    # PASTE BUTTON COMMAND
    def paste_command(self, textbox_name):
        textbox_name.event_generate("<<Paste>>")

# =====(TOOLS MENU)=====
    # DOCUMENTS INFORMATION
    def doctinfo_command(self, main_window, textbox_name, file_label):
        doct_info = Toplevel(main_window)
        doct_info.attributes('-topmost', bool(TRUE))
        doct_info.title("Document Information")
        doct_info.configure(background="#FFFFFF")
        doct_info.geometry("300x190")
        doct_info.resizable(False, False)

        info_frame = Frame(doct_info, bg="#ffffff")
        info_frame.pack(padx=(10,0))

        button_frame = Frame(doct_info, bg="#ffffff")
        button_frame.pack(pady=(30,0))

        # GET CONTENT INSIDE TEXTBOX
        text_content = textbox_name.get('1.0', 'end-1c')
        # FILE NAME
        file_name = Label(info_frame,
                          bg="#FFFFFF",
                          text=(file_label.cget("text")))
        file_name.grid(row=0, column=0, pady=(10,0), sticky='w')
        SPACE = " "
        # LINES
        lines_label = Label(info_frame,
                           text=f"Lines{SPACE*19}:{SPACE*2}",
                           bg='#ffffff',
                           font=('consolas', 10))
        lines_label.grid(row=1, column=0, sticky='w')
        lines_val = Label(info_frame,
                          text=len(text_content.splitlines()),
                          font=('consolas', 10),
                          bg='#ffffff')
        lines_val.grid(row=1, column=1, sticky='e')
        print(len(text_content.splitlines()))
        # WORD 
        word_label = Label(info_frame,
                           text=f'Words{SPACE*19}:{SPACE*2}',
                           bg='#ffffff',
                           font=('consolas', 10))
        word_label.grid(row=2, column=0, sticky='w')
        text_all_space = text_content.replace('.', ' ').replace(',', ' ')
        word_val = Label(info_frame,
                         text=len(text_all_space.split()),
                         bg='#ffffff',
                         font=('consolas', 10))
        word_val.grid(row=2, column=1, sticky='e')
        # CAHARCTER WITH SPACE
        char_SPACE = Label(info_frame,
                           text=f'Character (with spaces){SPACE}:{SPACE*2}',
                           bg="#FFFFFF",
                           font=('consolas', 10))
        char_SPACE.grid(row=3, column=0, sticky='w')
        char_SPACE_val = Label(info_frame,
                               bg='#ffffff',
                               font=('consolas', 10),
                               text=len(textbox_name.get('1.0', 'end-1c')))
        char_SPACE_val.grid(row=3, column=1, sticky='e')
        # CAHARCTER WITHOUT SPACE
        char_without_SPACE = Label(info_frame,
                                   text=f'Character (no spaces){SPACE*3}:{SPACE*2}',
                                   bg='#ffffff',
                                   font=('consolas', 10))
        char_without_SPACE.grid(row=4, column=0, sticky='w')
        text_content_list = text_content.replace(' ', '').replace('\n', '').replace('\t', '')
        char_without_SPACE_val = Label(info_frame,
                                       bg='#ffffff',
                                       font=('consolas', 10),
                                       text=len(list(text_content_list)))
        char_without_SPACE_val.grid(row=4, column=1, sticky='e')
        # UDPDATE BUTTON
        def update_command():
             doct_info.destroy()
             self.doctinfo_command(main_window, textbox_name, file_label)
        update_btn = Button(button_frame,
                            text='Update',
                            font=('consolas', 10),
                            bg="#F3F3F3",
                            width=10,
                            command=update_command)
        update_btn.grid(row=0, column=0, padx=(0,10))
        # CLOSE BUTTON
        close_btn = Button(button_frame,
                           text='Close',
                           font=('consolas', 10),
                           bg="#F3F3F3",
                           width=10,
                           command=lambda: doct_info.destroy())
        close_btn.grid(row=0, column=1, padx=(10,0))
    
    # TIME COMMAND
    def print_out_time(self, textbox_name):
         time = datetime.now()
         curent_time = time.strftime("%H:%M:%S")
         textbox_name.insert('1.0', curent_time)

    # DATE COMMAND
    def print_out_date(self, textbox_name):
         current_date = date.today()
         current_date_format = f"{current_date.day}/{current_date.month}/{current_date.year}"
         textbox_name.insert('1.0', current_date_format)

    # ASCII ART LIBRARY WINDOW
    def open_ascii_window(self, master):
        ascii_win = Toplevel(master)
        ascii_win.attributes('-topmost', bool(True))
        ascii_win.geometry("600x700")
        ascii_win.resizable(False, False)
        ascii_win.title("Ascii Art Library")

        scrollbar_y = Scrollbar(ascii_win)
        scrollbar_y.pack(side="right", fill='y')

        text_area = Text(ascii_win,
                        yscrollcommand=scrollbar_y.set)
        text_area.pack(expand=True, fill="both")
        scrollbar_y.config(command=text_area.yview)

        ascii_art = open("aset/Ascii.txt")
        text_area.insert("1.0", ascii_art.read())

# =====(THEME MENU)=====
    # CHANGE THEME CLASS
    class change_theme:
        def __init__(self, element):
            self.textbox = element.get("textbox name", 0)
            self.file_label = element.get("file label", 0)
            self.triangle_l = element.get("triangle left", 0)
            self.triangle_r = element.get("triangle right", 0)
            self.scrollbarx = element.get("scrollbar x", 0)
            self.scrollbary = element.get("scrollbar y", 0)
            self.statusbar = element.get("statusbar", 0)
            self.bg_color = element.get("background color", "")
            self.fg_color = element.get("foreground color", "")
            self.statusbar_bg = element.get("statusbar bg color", "")
        
        def theme_options(self):
            self.textbox.config(bg=self.bg_color,
                                fg=self.fg_color)
            self.file_label.config(bg=self.bg_color,
                                    fg=self.fg_color)
            self.triangle_l.config(bg=self.bg_color)
            self.triangle_r.config(bg=self.bg_color)
            self.statusbar.config(bg=self.statusbar_bg, fg=self.fg_color)
            self.scrollbarx.config(bg=self.bg_color)
            self.scrollbary.config(bg=self.bg_color)

    # LIGHT THEME COMMAND
    def light_theme_command(self, textbox_name, file_label, triangle_l, triangle_r, scrollbarx, scrollbary, status_bar):
        light_theme_setings = {"bg": "#ffffff",
                               "fg": "#242424",
                               "statusbar bg": "#DBDBDB"}

        self.element = {"textbox name" : textbox_name,
                        "file label" : file_label,
                        "triangle left" : triangle_l,
                        "triangle right" : triangle_r,
                        "scrollbar x" : scrollbarx,
                        "scrollbar y" : scrollbary,
                        "statusbar" : status_bar,
                        "background color" : light_theme_setings["bg"],
                        "foreground color" : light_theme_setings["fg"],
                        "statusbar bg color" : light_theme_setings["statusbar bg"]}
        light_theme = self.change_theme(self.element)
        light_theme.theme_options()

    # PAPER THEME COMMAND
    def paper_theme_command(self, textbox_name, file_label, triangle_l, triangle_r, scrollbarx, scrollbary, status_bar):
        paper_theme_setings = {"bg": "#f0e9d6",
                               "fg": "#242424",
                               "statusbar bg": "#d8d2c1"}

        self.element = {"textbox name" : textbox_name,
                        "file label" : file_label,
                        "triangle left" : triangle_l,
                        "triangle right" : triangle_r,
                        "scrollbar x" : scrollbarx,
                        "scrollbar y" : scrollbary,
                        "statusbar" : status_bar,
                        "background color" : paper_theme_setings["bg"],
                        "foreground color" : paper_theme_setings["fg"],
                        "statusbar bg color" : paper_theme_setings["statusbar bg"]}
        paper_theme = self.change_theme(self.element)
        paper_theme.theme_options()

    # DARK THEME COMMAND
    def dark_theme_command(self, textbox_name, file_label, triangle_l, triangle_r, scrollbarx, scrollbary, status_bar):
        dark_theme_setings = {"bg": "#383838",
                               "fg": "#FFFFFF",
                               "statusbar bg": "#4d4d4d"}

        self.element = {"textbox name" : textbox_name,
                        "file label" : file_label,
                        "triangle left" : triangle_l,
                        "triangle right" : triangle_r,
                        "scrollbar x" : scrollbarx,
                        "scrollbar y" : scrollbary,
                        "statusbar" : status_bar,
                        "background color" : dark_theme_setings["bg"],
                        "foreground color" : dark_theme_setings["fg"],
                        "statusbar bg color" : dark_theme_setings["statusbar bg"]}
        dark_theme = self.change_theme(self.element)
        dark_theme.theme_options()

    # CLASIC THEME COMMNAD
    def clasic_theme_command(self, textbox_name, file_label, triangle_l, triangle_r, scrollbarx, scrollbary, status_bar):
        clasic_theme_setings = {"bg": "#BBBA85",
                               "fg": "#000000",
                               "statusbar bg": "#ADA571"}

        self.element = {"textbox name" : textbox_name,
                        "file label" : file_label,
                        "triangle left" : triangle_l,
                        "triangle right" : triangle_r,
                        "scrollbar x" : scrollbarx,
                        "scrollbar y" : scrollbary,
                        "statusbar" : status_bar,
                        "background color" : clasic_theme_setings["bg"],
                        "foreground color" : clasic_theme_setings["fg"],
                        "statusbar bg color" : clasic_theme_setings["statusbar bg"]}
        clasic_theme = self.change_theme(self.element)
        clasic_theme.theme_options()

    # DEEP OCEAN THEME COMMNAD
    def deepocean_theme_command(self, textbox_name, file_label, triangle_l, triangle_r, scrollbarx, scrollbary, status_bar):
        deepocean_theme_setings = {"bg": "#042646",
                               "fg": "#FFFFFF",
                               "statusbar bg": "#041D35"}

        self.element = {"textbox name" : textbox_name,
                        "file label" : file_label,
                        "triangle left" : triangle_l,
                        "triangle right" : triangle_r,
                        "scrollbar x" : scrollbarx,
                        "scrollbar y" : scrollbary,
                        "statusbar" : status_bar,
                        "background color" : deepocean_theme_setings["bg"],
                        "foreground color" : deepocean_theme_setings["fg"],
                        "statusbar bg color" : deepocean_theme_setings["statusbar bg"]}
        deepocean_theme = self.change_theme(self.element)
        deepocean_theme.theme_options()

    # CUSTOM THEME COMMAND
    def custom_theme_command(self, textbox_name, file_label, triangle_l, triangle_r, scrollbarx, scrollbary, status_bar):
         theme_color = askcolor(title="Choose a theme color")
         if theme_color[1] == None:
              return
         else:
            custom_theme_setings = {"bg": theme_color[1],
                               "fg": "#FFFFFF",
                               "statusbar bg": theme_color[1]}

            self.element = {"textbox name" : textbox_name,
                            "file label" : file_label,
                            "triangle left" : triangle_l,
                            "triangle right" : triangle_r,
                            "scrollbar x" : scrollbarx,
                            "scrollbar y" : scrollbary,
                            "statusbar" : status_bar,
                            "background color" : custom_theme_setings["bg"],
                            "foreground color" : custom_theme_setings["fg"],
                            "statusbar bg color" : custom_theme_setings["statusbar bg"]}
            custom_theme = self.change_theme(self.element)
            custom_theme.theme_options()

# =====(HELP MENU)=====
    # ABOUT WINDOW
    def about_window(self, main_window, dnote_icon):
        about_win = Toplevel(main_window)
        about_win.geometry('350x360')
        about_win.resizable(False, False)
        about_win.attributes('-topmost', bool(True))
        about_win.configure(background="#f1f1f1")
        about_win.title('About D-Note')

        icon = Label(about_win,
                    text=' D-Note',
                    fg="#414141",
                    font=('system ui', 15),
                    image=dnote_icon,
                    bg="#f1f1f1",
                    compound='top')
        icon.pack(pady=(10,0))

        separator_line = Label(about_win,
                            text="_"*43,
                            bg='#f1f1f1')
        separator_line.pack(pady=(0,0))

        INFO = "D-Note is a simple text editor application created in Python.\n\nJust for information, all image assets in this project were created by myself."
        info = Label(about_win,
                    font=('system ui', 10),
                    justify='left',
                    bg='#f1f1f1',
                    wraplength=250,
                    text=INFO)
        info.pack()

        close_button = Button(about_win,
                            text='Close',
                            bg="#ffffff",
                            width=8,
                            relief='raised',
                            bd=1,
                            font=('system ui', 11),
                            command=lambda: about_win.destroy())
        close_button.pack(pady=(20,0), padx=(0,10), side='right')

# =====(TEXT TOOLS BAR)=====
    # CHANGE FONT STYLE
    def change_font(self, textbox_name, font_menu, size_menu):
        font = font_menu.get()
        size = size_menu.get()
        textbox_name.config(font=(font, size))

    # CHANGE FONT SIZE
    def change_font_size(self, Combobox_size, textbox_name):
         font_size = Combobox_size.get()
         textbox_name.config(font=('consolas', font_size))

    # CHANGE FONT COLOR
    def change_font_color(self, textbox_name, file_label, color_label):
         font_color = askcolor(title='Choose font color')
         if font_color == None:
              return
         else:
              textbox_name.config(fg=font_color[1])
              file_label.config(fg=font_color[1])
              color_label.config(bg=font_color[1])

    # OPEN SEARCH WINDOW
    def open_search_win(self, master, textbox_name):
        # SEARCH WINDOW
        search_win = Toplevel(master)
        search_win.title("Search for Text")
        search_win.geometry("505x100")
        search_win.resizable(False, False)
        search_win.attributes('-topmost', bool(True))
        # SEARCH ENTRY FRAME
        frame_entry = Frame(search_win)
        frame_entry.pack()
        # SEACH BUTTON FRAME
        frame_btn = Frame(search_win)
        frame_btn.pack(anchor='e')
        # SEARCH ENTRY
        search_entry = Entry(frame_entry,
                            width=60)
        search_entry.grid(row=0, column=0, pady=(10,20))
        search_entry.focus_set()

        # CANCEL SEARCH COMMAND
        def clear_search():
            textbox_name.tag_remove('found', '1.0', 'end')
            search_entry.delete('0', 'end')
            search_win.destroy()
            # CANCEL BUTTON
        cancel_button = Button(frame_btn,
                            text='Cancel',
                            width=10,
                            command=clear_search)
        cancel_button.grid(row=0, column=0, padx=5)

        # CLEAR SEARCH COMMAND
        def clear_search():
            textbox_name.tag_remove('found', '1.0', 'end')
            search_entry.delete('0', 'end')
        # CLEAR BUTTON
        clear_button = Button(frame_btn,
                            text='Clear',
                            width=10, 
                            command=clear_search)
        clear_button.grid(row=0, column=1, padx=5)

        # SEARCH FOR TEXT COMMNAD
        def search_text():
            textbox_name.tag_remove('found', '1.0', 'end')
            searched_val = search_entry.get()
            if searched_val:
                idx = '1.0'
                while True:
                    idx = textbox_name.search(searched_val, idx, nocase=True, stopindex='end')
                    if not idx:
                        break
                    last_idx = (f"{idx}+{len(searched_val)}c")

                    textbox_name.tag_add('found', idx, last_idx)
                    idx = last_idx
                textbox_name.tag_config('found', background="#5b73c4", foreground="#ffffff")
        # SEARCH BUTTON
        search_button = Button(frame_btn,
                            text='Search',
                            width=10,
                            command=search_text)
        search_button.grid(row=0, column=2, padx=(5,10))

# =====(REALTIME CHANGES LOGIC)=====
    def textbox_changes_command(self, textbox_name, file_label, file_name, statusbar_label):
        textbox_content = textbox_name.get('1.0', 'end-1c')
        def textbox_changes(event):
        # TEXT BOX CHANGES FOR UNTITLED FILE NAME
            realtype_typing = (textbox_name.get('1.0', 'end-1c') + event.char)
            if realtype_typing == textbox_content:
                file_label.config(text="Untitled")
            else:
                file_label.config(text=f"*Untitled")
        # TEXT BOX CHANGES FOR FILE NAME
            realtype_typing = (textbox_name.get('1.0', 'end-1c') + event.char)
            if realtype_typing == textbox_content:
                file_label.config(text=file_name)
            else:
                file_label.config(text=f"*{file_name}")
        # TEXT BOX CHANGES FOR STATUS BAR
            index = textbox_name.index(INSERT)
            row = index.split(".")[0]
            get_col = textbox_name.get(f"{row}.0", index)
            statusbar_label.config(text=f"Line {row}, Column {(len(get_col))+1}")

        textbox_name.bind("<KeyRelease>", textbox_changes)