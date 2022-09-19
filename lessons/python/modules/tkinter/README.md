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
  - Frame
  - Entry
  - Label
  - Button
  - ---
  - Geometry Managers
    - [Pack](tkinter_geometry_manager_pack.py)
      - Options
        - `anchor="center"|"n"|"e"|"ne"|"nw"|"s"|"se"|"sw"|"w"`
        - `side="top"|"bottom"|"left"|"right"`
        - Internal Padding
          - `ipadx=value`, `ipady=value`
        - External Padding
          - `padx=value`, `pady=value`
        - `expand=True|False`
        - `fill="none"|"both"|"x"|"y"`
    - [Grid](tkinter_geometry_manager_grid.py)
      - Options
        - `row=value`, `rowspan=value`
        - `column=value`, `columnspan=value`
        - Internal Padding
          - `ipadx=value`, `ipady=value`
        - External Padding
          - `padx=value`, `pady=value`
        - `sticky="n"|"e"|"ne"|"nw"|"s"|"se"|"sw"|"w"` more useful-> `"ns"|"ew"`
    - [Place](tkinter_geometry_manager_place.py)
      - Options
        - `anchor="center"|"n"|"e"|"ne"|"nw"|"s"|"se"|"sw"|"w"`
        - `bordermode="outside"|"inside"`
        - `x=value`, `y=value`
        - `relx=0 to 1`, `rely=0 to 1`
        - `width=value`, `height=value`
        - `relwidth=0 to 1`, `relheight=0 to 1`
  - Find config of a widget
    - [`set(btn.configure().keys())`](tkinter_widget_find_config.py)


## Note:
- [ ] TODO: Continue reading the [Official Link](https://docs.python.org/3/library/tkinter.html) 
- [ ] TODO: Read more about [TTK](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk)
- [ ] TODO: Read more about [Winfo](https://www.tcl.tk/man/tcl8.6/TkCmd/winfo.html)