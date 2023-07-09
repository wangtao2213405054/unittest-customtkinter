# _author: Coke
# _date: 2023/7/9 21:25

from typing import Any
import tkinter.messagebox

YES = "yes"
NO = "no"


class CTkMessageBox(tkinter.messagebox.Message):
    """ tkinter.messagebox encapsulates a messagebox component for customtkinter style """

    def __init__(self, master=None, **options):
        super(CTkMessageBox, self).__init__(master, **options)

    def show(self, title=None, message=None, _icon=None, _type=None, **options) -> Any:
        if _icon and "icon" not in options:
            options["icon"] = _icon
        if _type and "type" not in options:
            options["type"] = _type
        if title:
            options["title"] = title
        if message:
            options["message"] = message

        res = super(CTkMessageBox, self).show()
        # In some Tcl installations, yes/no is converted into a boolean.
        if isinstance(res, bool):
            if res:
                return YES
            return NO
        # In others we get a Tcl_Obj.
        return str(res)
