from tkinter import *
from tkinter import ttk
from poke_api import search_for_pokemon
from tkinter import messagebox


root = Tk()
root.title("Pokèmon Information Viewer")
root.resizable(False, False)

# Add Frames to window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, pady=(20.10))

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, padx=(20, 10,), pady=(10, 20), sticky=N)


frm_btm_right = ttk.LabelFrame(root, text='Pokèmon Stats')
frm_btm_right.grid(row=1, column=1, padx=(10, 20,), pady=(10, 20))


#Add widgets to frames
lbl_name = ttk.Label(frm_top, text='Pokèmon name:')
lbl_name.grid(row=0, column=0, padx=(10,5), pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

# populate widgets in the info box.
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, padx=(10,5), pady=10)
lbl_height_value = ttk.Label(frm_btm_left, text='TBD:')
lbl_height_value.grid(row=0, column=1, padx=(5,5), pady=10)

lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, padx=(10,5), pady=10)
lbl_weight_value = ttk.Label(frm_btm_left, text='TBD:')
lbl_weight_value.grid(row=1, column=1, padx=(5,5), pady=10)

lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, padx=(10,5), pady=10)
lbl_type_value = ttk.Label(frm_btm_left, text='TBD:')
lbl_type_value.grid(row=2, column=1, padx=(5,5), pady=10)

# Populate widgets in the stats frame. 
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, sticky=E, padx=(10,5), pady=(10,5))
bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0,column=1, padx=(0,10), pady=5)

lbl_attack = ttk.Label(frm_btm_right, text='Attack:' )
lbl_attack.grid(row=1, column=0, sticky=E)
bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_attack.grid(row=1,column=1, padx=(0,10), pady=5)

lbl_defense = ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0, sticky=E)
bar_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_defense.grid(row=2,column=1, padx=(0,10), pady=5)

lbl_spec_atk = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_spec_atk.grid(row=3, column=0, sticky=E, padx=(10,5), pady=(10,5))
bar_spec_atk = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_spec_atk.grid(row=3,column=1, padx=(0,10), pady=5)

lbl_spec_def = ttk.Label(frm_btm_right, text='Special Defense:')
lbl_spec_def.grid(row=4, column=0, sticky=E, padx=(10,5), pady=(10,5))
bar_spec_def = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_spec_def.grid(row=4,column=1, padx=(0,10), pady=5)

lbl_speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0, sticky=E, padx=(10,5), pady=(10,5))
bar_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_speed.grid(row=5,column=1, padx=(0,10), pady=5)

def handle_get_info():
    # Get Pokemon name entered by the user
    poke_name = ent_name.get().strip()
    if len(poke_name) == 0:
        return

    # get poke info from poke api
    poke_info = search_for_pokemon(poke_name)
    if poke_info is None:
        err_msg = f'unable to fetch information for {poke_name.capitalize()} from the PokeAPI.'
        messagebox.showinfo(title='Error', message=err_msg, icon='error')
    if poke_info is not None:
        type_list = [t['type']['name'] for t in poke_info['types']]
        poke_type = ', '.join(type_list).title()
        # Populate the info frame
        lbl_height_value['text'] = f"{poke_info['height']} dm "
        lbl_weight_value['text'] = f"{poke_info['weight']} hg"
        lbl_type_value['text'] = poke_type

        # Populate the stats frame
        bar_hp['value'] = poke_info['stats'][0]['base_stat']
        bar_attack['value'] = poke_info['stats'][1]['base_stat']
        bar_defense['value'] = poke_info['stats'][2]['base_stat']
        bar_spec_atk['value'] = poke_info['stats'][3]['base_stat']
        bar_spec_def['value'] = poke_info['stats'][4]['base_stat']
        bar_speed['value'] = poke_info['stats'][5]['base_stat']

# Create event handle for get info button
btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_get_info.grid(row=0, column=2, padx=10, pady=10)

#loop until window is closed
root.mainloop()