import tkinter as tk
import subprocess
import tkinter.filedialog as filedialog
import sys
import os.path
import datetime


class Interface:

    def __init__(self, master):
        self.master = master
        master.title("Conversion interface")
        
        # Variables for storing paths and file names
        self.file_path = tk.StringVar()
        self.file_name = tk.StringVar()
        self.name=tk.StringVar()
        self.file_new_file_name = tk.StringVar()
        self.new_file_name = tk.StringVar()

        # Interface elements
        self.radio_frame = tk.Frame(self.master, bd=2, relief="solid")
        self.radio_frame.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
        self.radio_frame2 = tk.Frame(self.master, bd=2, relief="solid")
        self.radio_frame2.grid(row=5, column=1, columnspan=2, padx=10, pady=10)


        tk.Label(master, text="Browse of the file :", font=("Arial", 12)).grid(row=0, column=0)
        self.path_entry = tk.Entry(master, textvariable=self.file_path, width=40)
        self.path_entry.grid(row=0, column=1, sticky="W", padx=5)

        tk.Label(master, text="Name of the new file :", font=("Arial", 12)).grid(row=1, column=0)
        self.name_entry = tk.Entry(master, textvariable=self.file_new_file_name, width=40)
        self.name_entry.grid(row=1, column=1)

        self.radio_var = tk.IntVar()
        tk.Radiobutton(master, text="ALL EVENTS", variable=self.radio_var, value=1, font=("Arial", 12)).grid(row=4, column=0, sticky="W", padx=20)
        tk.Radiobutton(master, text="COINCIDENCE", variable=self.radio_var, value=2, font=("Arial", 12)).grid(row=5, column=0, sticky="W",padx=20)


        self.search_button = tk.Button(master, text="Search", command=self.browse_file, font=("Arial", 12), width=10)
        self.search_button.grid(row=0, column=2)
        self.convert_button = tk.Button(master, text="Refresh", command=self.update_new_file_name, font=("Arial", 12), height=2, width=40)
        self.convert_button.grid(row=7, column=0, columnspan=4, pady=50)
        self.convert_button = tk.Button(master, text="Convert", command=self.convert_file, font=("Arial", 12), height=2, width=40)
        self.convert_button.grid(row=9, column=0, columnspan=4, pady=50)

        # Ajouter le label ici
        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.grid(row=6, column=0, columnspan=3)

        self.var1 = tk.StringVar(value="None")
        self.var2 = tk.StringVar(value="None")
        
        self.var3 = tk.StringVar(value="None")
        self.var4 = tk.StringVar(value="None")
        self.var5 = tk.StringVar(value="None")
        self.var6 = tk.StringVar(value="None")

    
 
        self.r3 = tk.Radiobutton(self.radio_frame, text="ENERGY", variable=self.var3, value="Radio 3", command=lambda: self.toggle_radio(3), font=("Arial", 12)).grid(row=0, column=1, sticky="W", padx=20)
        tk.Label(self.radio_frame, text="ADC0", font=("Arial", 12)).grid(row=0, column=0,padx=10, pady=10, sticky="NS")  
        self.r4 = tk.Radiobutton(self.radio_frame, text="TIME", variable=self.var4, value="Radio 4", command=lambda: self.toggle_radio(4), font=("Arial", 12)).grid(row=1, column=1, sticky="W", padx=20)
     
        self.r5 = tk.Radiobutton(self.radio_frame2, text="ENERGY", variable=self.var5, value="Radio 5", command=lambda: self.toggle_radio(5), font=("Arial", 12)).grid(row=0, column=1, sticky="W", padx=20)
        tk.Label(self.radio_frame2, text="ADC1", font=("Arial", 12)).grid(row=0, column=0,padx=10, pady=10, sticky="NS")      
        self.r6 = tk.Radiobutton(self.radio_frame2, text="TIME", variable=self.var6, value="Radio 6", command=lambda: self.toggle_radio(6), font=("Arial", 12)).grid(row=1, column=1, sticky="W", padx=20)
     

    def toggle_radio(self, radio_num):
        if radio_num == 3:
            self.var6.set("Radio 6")
            self.var5.set("None")
            self.var4.set("None")
            
        elif radio_num == 4:
            self.var5.set("Radio 5")
            self.var6.set("None")
            self.var3.set("None")
        elif radio_num == 5:
            self.var4.set("Radio 4")
            self.var6.set("None")
            self.var3.set("None")
        elif radio_num == 6:
            self.var3.set("Radio 3")
            self.var4.set("None")
            self.var5.set("None")
                

    def update_new_file_name(self):
        name = self.file_name.get()
        bouton1 = self.radio_var.get()
        bouton2 = self.var3.get()
        print(self.var3.get())
        print(self.radio_var.get())
        if bouton2 == "Radio 3":
            print("test")
            bouton2 = 1
        elif bouton2 == "None":
            bouton2 = 2
        file_path = self.file_path.get()
        file_name = os.path.basename(file_path)
        self.file_name.set(file_name)
        if bouton1 == 1:
            new_file_name = self.file_name.get()[:-4] + "_" + "ALL_EVENTS" + "_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
        elif bouton1 == 2 and bouton2 == 1:
            new_file_name = self.file_name.get()[:-4] + "_" + "COINCIDENCE_ADC0_ENERGY" + "_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
        elif bouton1 == 2 and bouton2 == 2:
            new_file_name = self.file_name.get()[:-4] + "_" + "COINCIDENCE_ADC0_TIME" + "_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
        else:
            new_file_name = self.file_name.get()[:-4] + "_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
        self.file_new_file_name.set(new_file_name)
        print(self.new_file_name.get())

    
    def browse_file(self):
        # Opens a window to browse files
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)
            file_name = os.path.basename(file_path)
            self.file_name.set(file_name)
            new_file_name = self.file_name.get()[:-4] + ".txt"
            self.file_new_file_name.set(new_file_name)
            print(self.file_new_file_name.get())
            self.update_new_file_name



    def convert_file(self):
        name = self.file_name.get()
        sortie = self.file_new_file_name.get()
        bouton1 = self.radio_var.get()
        bouton2 = self.var3.get()   
        
        if bouton2 == "Radio 3":
            bouton2 = 1
        elif bouton2 == "None":
            bouton2=2
 
        bouton1=str(bouton1)
        bouton2=str(bouton2)
        print(f"bouton 1 : {bouton1}")
        print(f"bouton 2 : {bouton2}")
        # Call the C program
        print(f"argv 0 : {name}")
        commande = ['./ToolTOFv1.exe', name, sortie, bouton1, bouton2]
        result = subprocess.run(commande, capture_output=True)
        print("-----------------------------------------------------")
        if result.returncode == 0:
             self.result_label.configure(text="Conversion successful!")
        else:
             self.result_label.configure(text="Conversion failed.")
        print(f"Return code: {result.returncode}")
        print(f"stdout: {result.stdout.decode()}")
        print(f"stderr: {result.stderr.decode()}")

root = tk.Tk()
interface = Interface(root)
root.mainloop()