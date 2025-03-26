

class AplikacioniLibrarise:
    def __init__(self, root):
        self.root = root
        self.root.title("Menaxhimi i Inventarit të Librarisë")
        self.library_inventory = []

        # Krijimi i fushave për të dhënat e librit
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="Titulli:").grid(row=0, column=0)
        self.title_entry = tk.Entry(self.frame)
        self.title_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Autori:").grid(row=1, column=0)
        self.author_entry = tk.Entry(self.frame)
        self.author_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Viti:").grid(row=2, column=0)
        self.year_entry = tk.Entry(self.frame)
        self.year_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Kopje:").grid(row=3, column=0)
        self.copies_entry = tk.Entry(self.frame)
        self.copies_entry.grid(row=3, column=1)

        # Butonat për veprimet kryesore
        tk.Button(self.frame, text="Regjistro", command=self.regjistro_liber).grid(row=4, columnspan=2, pady=5)
        tk.Button(self.root, text="Shfaq Librat", command=self.shfaq_librat).pack(pady=5)
        tk.Button(self.root, text="Kërko Libër", command=self.kerko_liber).pack(pady=5)

        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=5)

    def regjistro_liber(self):
        titulli = self.title_entry.get()
        autori = self.author_entry.get()
        viti = self.year_entry.get()
        kopje = self.copies_entry.get()
        
        if titulli and autori and viti and kopje.isdigit():
            self.library_inventory.append({"Titulli": titulli, "Autori": autori, "Viti": viti, "Kopje": int(kopje)})
            messagebox.showinfo("Sukses", "Libri u regjistrua me sukses!")
            self.pastro_fushat()
        else:
            messagebox.showerror("Gabim", "Ju lutemi plotësoni të gjitha fushat siç duhet!")

    def shfaq_librat(self):
        self.result_text.delete(1.0, tk.END)
        for libri in self.library_inventory:
            if libri["Kopje"] > 0:
                self.result_text.insert(tk.END, f"Titulli: {libri['Titulli']}, Autori: {libri['Autori']}, Viti: {libri['Viti']}, Kopje: {libri['Kopje']}\n")

    def kerko_liber(self):
        kerkimi = simpledialog.askstring("Kërko Libër", "Shkruani titullin ose autorin:")
        if kerkimi:
            self.result_text.delete(1.0, tk.END)
            gjetur = False
            for libri in self.library_inventory:
                if kerkimi.lower() in libri['Titulli'].lower() or kerkimi.lower() in libri['Autori'].lower():
                    if libri["Kopje"] > 0:
                        self.result_text.insert(tk.END, f"Titulli: {libri['Titulli']}, Autori: {libri['Autori']}, Viti: {libri['Viti']}, Kopje: {libri['Kopje']}\n")
                        gjetur = True
            if not gjetur:
                self.result_text.insert(tk.END, "Nuk u gjet asnjë libër me këtë kërkim.\n")

    def pastro_fushat(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.copies_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikacioniLibrarise(root)
    root.mainloop()

































































































