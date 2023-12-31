from pieces.Queen import Queen
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Blank import Blank
from playsound import playsound
import views
import data 

from tkinter import *
import theme
from utils.paths import get_full_path


def is_in_danger(x, y, color, game_data):
    not_in_danger = True
    data = [[], [], [], [], [], [], [], []]

    for i in range(8):
        for j in range(8):
            data[i].append(game_data[i][j])

    data[x][y] = Blank(x, y)

    # Vertical Movement
    for k in range(1, 8):
        if 0 <= x + k <= 7:
            if (
                isinstance(data[x + k][y], Queen) or isinstance(data[x + k][y], Rook)
            ) and color != data[x + k][y].color:
                not_in_danger = False
                break
            elif not isinstance(data[x + k][y], Blank):
                break

    if not_in_danger == True:
        for k in range(1, 8):
            if 0 <= x - k <= 7:
                if (
                    isinstance(data[x - k][y], Queen)
                    or isinstance(data[x - k][y], Rook)
                ) and color != data[x - k][y].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x - k][y], Blank):
                    break

    # Horizontal Movement
    if not_in_danger == True:
        for k in range(1, 8):
            if 0 <= y + k <= 7:
                if (
                    isinstance(data[x][y + k], Queen)
                    or isinstance(data[x][y + k], Rook)
                ) and color != data[x][y + k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x][y + k], Blank):
                    break

    if not_in_danger == True:
        for k in range(1, 8):
            if 0 <= y - k <= 7:
                if (
                    isinstance(data[x][y - k], Queen)
                    or isinstance(data[x][y - k], Rook)
                ) and color != data[x][y - k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x][y - k], Blank):
                    break

    # Diagonal
    if not_in_danger == True:
        for k in range(1, 8):
            if 0 <= y + k <= 7 and 0 <= x + k <= 7:
                if (
                    isinstance(data[x + k][y + k], Queen)
                    or isinstance(data[x + k][y + k], Bishop)
                ) and color != data[x + k][y + k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x + k][y + k], Blank):
                    break

    if not_in_danger == True:
        for k in range(1, 8):
            if 0 <= y - k <= 7 and 0 <= x + k <= 7:
                if (
                    isinstance(data[x + k][y - k], Queen)
                    or isinstance(data[x + k][y - k], Bishop)
                ) and color != data[x + k][y - k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x + k][y - k], Blank):
                    break

    if not_in_danger == True:
        for k in range(1, 8):
            if 0 <= y - k <= 7 and 0 <= x - k <= 7:
                if (
                    isinstance(data[x - k][y - k], Queen)
                    or isinstance(data[x - k][y - k], Bishop)
                ) and color != data[x - k][y - k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x - k][y - k], Blank):
                    break

    if not_in_danger == True:
        for k in range(1, 8):
            if 0 <= y + k <= 7 and 0 <= x - k <= 7:
                if (
                    isinstance(data[x - k][y + k], Queen)
                    or isinstance(data[x - k][y + k], Bishop)
                ) and color != data[x - k][y + k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x - k][y + k], Blank):
                    break

    # Knight movement
    if not_in_danger == True:
        for dx in [1, -1, 2, -2]:
            break_outer = False
            for dy in [1, -1, 2, -2]:
                if abs(dx) != abs(dy):
                    if 0 <= x + dx <= 7 and 0 <= y + dy <= 7:
                        if (isinstance(data[x + dx][y + dy], Knight)) and color != data[
                            x + dx
                        ][y + dy].color:
                            not_in_danger = False
                            break_outer = True
                            break
            if break_outer:
                break

    if not_in_danger == True:
        if color == "W":
            if 0 <= x + 1 <= 7 and 0 <= y + 1 <= 7 and 0 <= y - 1 <= 7:
                if (
                    isinstance(data[x + 1][y + 1], Pawn)
                    or isinstance(data[x + 1][y - 1], Pawn)
                ) and (
                    data[x + 1][y + 1].color == "B" or data[x + 1][y - 1].color == "B"
                ):
                    not_in_danger = False
            else:
                if 0 <= x - 1 <= 7 and 0 <= y + 1 <= 7 and 0 <= y - 1 <= 7:
                    if (
                        isinstance(data[x - 1][y + 1], Pawn)
                        or isinstance(data[x - 1][y - 1], Pawn)
                    ) and (
                        data[x - 1][y + 1].color == "W"
                        or data[x - 1][y - 1].color == "W"
                    ):
                        not_in_danger = False

    return not not_in_danger

def restart(root):
    
    data.rooms_window = views.rooms.Rooms(data.room_window.parent)
    data.room_window.destroy()
    del data.room_window
    data.room_window = None
    root.destroy()


def check_for_end(i, j, data, won):
    if len(data[i][j].get_moves(data)) == 0:
        root = Tk()
        root.geometry("960x540")
        root.resizable(False, False)

        frame = Frame(root, background=theme.background_primary)
        frame.pack(fill=BOTH, expand=True)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(2, weight=1)

        if won == False:
            lb = Label(
                frame,
                text="You Lost",
                font=("Arial", 60),
                background=theme.background_primary,
                foreground="red",
            )
            try:
                playsound(get_full_path("assets/lose.wav"))
            except Exception as e:
                print("Error playing lose sound ", e)
        else:
            lb = Label(
                frame,
                text="You Won",
                font=("Arial", 60),
                background=theme.background_primary,
                foreground="#0e0ed4",
            )
            try:
                playsound(get_full_path("assets/win.mp3"))
            except Exception as e:
                print("Error playing win sound", e)
        lb2 = Label(
            frame,
            text="Game Over",
            font=("Arial", 30),
            background=theme.background_primary,
            foreground=theme.text_primary,
        )
        lb.grid(row=1, column=1)
        lb2.grid(row=2, column=1)

        bt = Button(frame,
            text="Play Again",
            background=theme.color_primary,
            foreground=theme.text_primary,
            border="1",
            width=10,
            height=2, 
            font=('Arial',12),
            activebackground=theme.color_secondary,
            activeforeground=theme.text_primary, 
            command=lambda root=root : restart(root))
        bt.grid(row=3 , column=1)

        root.mainloop()


def promote_pawn(parent, color, set_choice):
    frame = Frame(parent, background=theme.background_primary)
    frame.grid(row=0, column=1)

    global queen_image
    global knight_image
    global bishop_image
    global rook_image

    if color == "W":
        queen_image = PhotoImage(file=get_full_path("assets/w_q.png"))
        knight_image = PhotoImage(file=get_full_path("assets/w_n.png"))
        bishop_image = PhotoImage(file=get_full_path("assets/w_b.png"))
        rook_image = PhotoImage(file=get_full_path("assets/w_r.png"))

    else:
        queen_image = PhotoImage(file=get_full_path("assets/b_q.png"))
        knight_image = PhotoImage(file=get_full_path("assets/b_n.png"))
        bishop_image = PhotoImage(file=get_full_path("assets/b_b.png"))
        rook_image = PhotoImage(file=get_full_path("assets/b_r.png"))

    buttn1 = Button(
        frame,
        image=queen_image,
        width=60,
        height=60,
        border=0,
        background=theme.text_primary,
        command=lambda: set_choice("Q", frame),
    )
    buttn2 = Button(
        frame,
        image=knight_image,
        width=60,
        height=60,
        border=0,
        background=theme.text_primary,
        command=lambda: set_choice("N", frame),
    )
    buttn3 = Button(
        frame,
        image=bishop_image,
        width=60,
        height=60,
        border=0,
        background=theme.text_primary,
        command=lambda: set_choice("B", frame),
    )
    buttn4 = Button(
        frame,
        image=rook_image,
        width=60,
        height=60,
        border=0,
        background=theme.text_primary,
        command=lambda: set_choice("R", frame),
    )

    buttn1.grid(row=0, column=0, padx=5)
    buttn2.grid(row=0, column=1, padx=5)
    buttn3.grid(row=0, column=2, padx=5)
    buttn4.grid(row=0, column=3, padx=5)
