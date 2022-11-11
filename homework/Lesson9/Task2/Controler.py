import UI
import Function as Fun
import Read_input as Input

def run_programm():
    filename = UI.input_filename()
    choice = 0
    while choice != 6:
        choice = UI.show_menu()
        if choice == 1:
            Fun.fun_1_write_all(Input.read_txt(filename))
        if choice == 2:
            Fun.fun_2_find_sec_name(Input.read_txt(filename),UI.find_data())
        if choice == 3:
            Fun.fun_3_find_phone(Input.read_txt(filename),UI.find_data())
        if choice == 4:
            Fun.fun_4_add_data(filename,UI.add_data())
        if choice == 5:
            Fun.fun_5_output(UI.add_file(),Input.read_txt(filename))
        if choice == 6:
            exit