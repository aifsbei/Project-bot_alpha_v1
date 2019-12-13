import tkinter
from tkinter import ttk


pad = 5
bullet = '\u2022'
forecolor = 'white smoke'
#backgroundcolor = 'LightSkyBlue4'
backgroundcolor = 'gray24'
inner_background = 'gray30'


def set_style():
    style = ttk.Style()
    settings = {"TNotebook": {"configure": {"background": "gray24"}},
        "TNotebook.Tab": {"configure": {"padding": [12, 4],
                                                "background": backgroundcolor
                                               },
                                  "map": {"background": [("selected", inner_background),
                                                         ("active", "gray10")],
                                          "foreground": [("selected", "#ffffff"),
                                                         ("active", "#ffffff")]

                                         }
                                  }
               }


    style.theme_create("new_theme", parent="default", settings=settings)
    style.theme_use("new_theme")

    ttk.Style().configure('Treeview', fieldbackground=backgroundcolor, background=backgroundcolor, foreground=forecolor)