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
- [Scrolled Text](tkinter_scrolled_text.py)
- [Drag and Drop (DnD)](tkinter_drag_and_drop.py) <sub>TODO: Complete this section</sub>
- Binds and Events <sub>TODO: Complete this section</sub>
  - [Mouse Key Events](tkinter_bindings.py)
  - [Mouse Move Events](tkinter_mouse_motion.py)
  - [Keyboard Events](tkinter_keyboard_events.py)
  - [General Events](tkinter_general_events.py)
- Layouts
- Widget
  - <details><summary><strong>List of Widgets</strong></summary>
  
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
  
    <details>
  - <details><summary><strong>Geometry Managers</strong></summary>

      - [Pack](tkinter_geometry_manager_pack.py)
        - <details><summary><strong>Options</strong></summary>
    
          - `anchor="center", "n", "e", "ne", "nw", "s", "se", "sw", "w"`
          - `side="top", "bottom", "left", "right"`
          - Internal Padding
            - `ipadx=N`, `ipady=N`
          - External Padding
            - `padx=N`, `pady=N`
          - `expand=True, False`
          - `fill="none", "both", "x", "y"`

          </details>
        - ![](tkinter_geometry_manager_pack.png)
      - [Grid](tkinter_geometry_manager_grid.py)
        - <details><summary><strong>Options</strong></summary>
    
          - `row=N`, `rowspan=N`
          - `column=N`, `columnspan=N`
          - Internal Padding
            - `ipadx=N`, `ipady=N`
          - External Padding
            - `padx=N`, `pady=N`
          - `sticky="n", "e", "ne", "nw", "s", "se", "sw", "w"` and `"ns", "ew"`

          </details>
        - ![](tkinter_geometry_manager_grid.png)
      - [Place](tkinter_geometry_manager_place.py)
        - <details><summary><strong>Options</strong></summary>
    
          - `anchor="center", "n", "e", "ne", "nw", "s", "se", "sw", "w"`
          - `bordermode="outside", "inside"`
          - `x=N`, `y=N`
          - `relx=0-1`, `rely=0-1`
          - `width=N`, `height=N`
          - `relwidth=0-1`, `relheight=0-1`

          </details>
        - ![](tkinter_geometry_manager_place.png)
    </details>

  - [Find config of a widget](tkinter_widget_find_config.py)
  - Tk Options  <sub>TODO: Complete this section</sub>
    - `color`, `cursor`, `distance`, `font`, `geometry`, `justify`, `region`, `relif`, `scrollcommand`, `wrap`


## Note:
- [ ] TODO: Continue reading the [Official Link](https://docs.python.org/3/library/tkinter.html) 
- [ ] TODO: Read more about [TTK](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk)
- [ ] TODO: Read more about [Winfo](https://www.tcl.tk/man/tcl8.6/TkCmd/winfo.html)