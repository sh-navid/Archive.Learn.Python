# Python
## Tkinter 
### Installation on Ubuntu
`sudo apt-get install python3-tk`

## Headings
- [Color Chooser](tkinter_color_chooser.py)
- [Message Box](tkinter_Message_box.py)
- [Open File Dialog](tkinter_open_file_dialog.py)
- [Ask Question](tkinter_ask_from_user.py)
- [Ask Question with Input](tkinter_ask_with_input.py)
- [Ask Question with Custom Input](tkinter_ask_with_custom_input.py)
- Fonts
- [Scrolled Text](tkinter_scrolled_text.py)
- [Drag and Drop (DnD)](tkinter_drag_and_drop.py)
  - [ ] TODO: Complete this section
- Binds and Events
  - `<Button-1>`, `<Button-2>`, `<Button-3>`, `<Button-4>`, `<Button-5>`
  - [ ] TODO: Complete this section
- Layouts
- Widgets
  - [Frame](tkinter_frame.py)
    - ![](tkinter_frame.png)
  - [Entry](tkinter_entry.py)
    - ![](tkinter_entry.png)
  - [Label](tkinter_label.py)
    - ![](tkinter_label.png)
  - [Button](tkinter_button.py)
    - ![](tkinter_button.png)
  - [Image](tkinter_image.py)
    - ![](tkinter_image.png)
  - ---
  - Geometry Managers
    - [Pack](tkinter_geometry_manager_pack.py)
      - Options
        - `anchor="center", "n", "e", "ne", "nw", "s", "se", "sw", "w"`
        - `side="top", "bottom", "left", "right"`
        - Internal Padding
          - `ipadx=N`, `ipady=N`
        - External Padding
          - `padx=N`, `pady=N`
        - `expand=True, False`
        - `fill="none", "both", "x", "y"`
      - ![](tkinter_geometry_manager_pack.png)
    - [Grid](tkinter_geometry_manager_grid.py)
      - Options
        - `row=N`, `rowspan=N`
        - `column=N`, `columnspan=N`
        - Internal Padding
          - `ipadx=N`, `ipady=N`
        - External Padding
          - `padx=N`, `pady=N`
        - `sticky="n", "e", "ne", "nw", "s", "se", "sw", "w"` and `"ns", "ew"`
      - ![](tkinter_geometry_manager_grid.png)
    - [Place](tkinter_geometry_manager_place.py)
      - Options
        - `anchor="center", "n", "e", "ne", "nw", "s", "se", "sw", "w"`
        - `bordermode="outside", "inside"`
        - `x=N`, `y=N`
        - `relx=0-1`, `rely=0-1`
        - `width=N`, `height=N`
        - `relwidth=0-1`, `relheight=0-1`
      - ![](tkinter_geometry_manager_place.png)
  - Find config of a widget
    - [`set(btn.configure().keys())`](tkinter_widget_find_config.py)


## Note:
- [ ] TODO: Continue reading the [Official Link](https://docs.python.org/3/library/tkinter.html) 
- [ ] TODO: Read more about [TTK](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk)
- [ ] TODO: Read more about [Winfo](https://www.tcl.tk/man/tcl8.6/TkCmd/winfo.html)