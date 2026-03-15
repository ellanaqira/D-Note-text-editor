from aset.load_img import load_image

class Aset_img:
    def __init__(self):
        # FILE MENU IMAGE
        self.newfile_icon = load_image('aset/image/file_plus.png',(17,17))
        self.openfile_icon = load_image('aset/image/file_import.png',(17,17))
        self.save_icon = load_image('aset/image/save.png',(17,17))
        self.saveas_icon = load_image('aset/image/save_as.png',(17,17))
        self.exit_icon = load_image('aset/image/exit.png',(17,17))

        # EDIT MENU IMAGE
        self.copy_icon = load_image('aset/image/copy.png', (20,20))
        self.cut_icon = load_image('aset/image/cut.png', (20,20))
        self.paste_icon = load_image('aset/image/paste.png', (20,20))
        self.sel_all_icon = load_image('aset/image/sel_all.png', (20,20))

        # TOOL MENU IMAGE
        self.pacman_emote = load_image('aset/image/pacman.png', (15,15))

        # THEME MENU IMAGE
        self.white_ball = load_image('aset/image/white_ball.png',(20,20))
        self.paper_ball = load_image('aset/image/paper_ball.png',(20,20))
        self.black_ball = load_image('aset/image/black_ball.png',(20,20))
        self.clasic_ball = load_image('aset/image/clasic_ball.png',(20,20))
        self.blue_ball = load_image('aset/image/blue_ball.png',(20,20))
        self.color_ball = load_image('aset/image/color_ball.png',(20,20))

        # HELP MENU IMAGE
        self.exclamation_mark = load_image('aset/image/exclamation_mark.png', (17,17))
        self.Dnote_icon = load_image('aset/image/dnote_icon.png', (120,120))

        # OTHER  TOOLS
        self.undo_icon = load_image('aset/image/undo.png', (17,15))
        self.redo_icon = load_image('aset/image/redo.png', (17,15))
        self.vertical_line = load_image('aset/image/line.png', (2,30))
        self.question_mark = load_image('aset/image/question_mark.png', (70,70))
        self.right_triangle_img = load_image('aset/image/right_triangle.png', (18,30))
        self.left_triangle_img = load_image('aset/image/left_triangle.png', (18,30))
        self.search_icon = load_image('aset/image/search_icon.png', (21,21))   