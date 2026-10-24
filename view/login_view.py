import tkinter as tk
from tkinter import messagebox
from controller.login_controller import LoginController

class LoginVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema - Papelería")
        self.root.geometry("340x360")
        self.root.configure(bg="#212124")
        
        self.controller = LoginController()
        self._crear_interfaz()

    def _crear_interfaz(self):
        tk.Label(self.root, text="Iniciar Sesión", font=("Helvetica", 15, "bold"), fg="#ffffff", bg="#212124").pack(pady=(30, 20))

        tk.Label(self.root, text="Usuario:", font=("Helvetica", 10), fg="#cfcfcf", bg="#212124").pack(anchor="w", padx=35, pady=(5, 2))
        self.entry_usuario = tk.Entry(self.root, font=("Helvetica", 10), bg="#141416", fg="#ffffff", insertbackground="white")
        self.entry_usuario.pack(fill="x", padx=35, ipady=3)

        tk.Label(self.root, text="Contraseña (RFC):", font=("Helvetica", 10), fg="#cfcfcf", bg="#212124").pack(anchor="w", padx=35, pady=(12, 2))
        self.entry_pass = tk.Entry(self.root, show="*", font=("Helvetica", 10), bg="#141416", fg="#ffffff", insertbackground="white")
        self.entry_pass.pack(fill="x", padx=35, ipady=3)

        tk.Button(self.root, text="Entrar", font=("Helvetica", 10, "bold"), bg="#ffffff", fg="#000000", 
                  relief="flat", cursor="hand2", command=self._iniciar_sesion).pack(fill="x", padx=35, pady=(25, 0), ipady=4)

    def _iniciar_sesion(self):
        usuario = self.entry_usuario.get().strip()
        contrasena = self.entry_pass.get().strip()

        # LLAMADA AL CONTROLADOR
        user_obj, mensaje = self.controller.autenticar(usuario, contrasena)

        if user_obj:
            messagebox.showinfo("Bienvenido", f"Acceso concedido a {user_obj.nombre_completo}")
            self.root.destroy()
            
            # Abrir Dashboard
            dashboard_root = tk.Tk()
            from view.home_view import DashboardVentana
            DashboardVentana(dashboard_root, usuario=user_obj)
            dashboard_root.mainloop()
        else:
            # PREVENCIÓN DE ERRORES
            messagebox.showerror("Error de Acceso", mensaje, parent=self.root)