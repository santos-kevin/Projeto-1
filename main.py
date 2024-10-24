import customtkinter as ctk

janela = ctk.CTk()
tela_largura = janela.winfo_screenwidth()
tela_altura = janela.winfo_screenheight()
barra_tarefas = 40
janela.geometry(f"{tela_largura}x{tela_altura - barra_tarefas}+0+0+0+0+0+0")
janela._set_appearance_mode("light")
ctk.set_appearance_mode("light")

switch_var = ctk.StringVar(value="on")

def destroy():
    btn.destroy()
    switch.destroy()


def event():
    if switch_var.get() == "Ativado":
        ctk.set_appearance_mode("dark")
    elif switch_var.get() == "Desativado":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("System")


switch = ctk.CTkSwitch(master=janela, 
                       text="Modo escuro",
                       command=event,
                       variable=switch_var,
                       onvalue="Ativado",
                       offvalue="Desativado")

switch.pack(pady=30)

def tela_1():
    destroy()
    
    #frame = ctk.CTkFrame(janela_1, widtgh= )

btn = ctk.CTkButton(master=janela, text="iniciar", command=tela_1)
btn.pack(pady=50, padx= 50)


janela.mainloop()