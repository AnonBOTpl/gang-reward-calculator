#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class GangRewardCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🏆 Kalkulator Podziału Nagród w Gangu")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#2c3e50', foreground='#ecf0f1')
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), background='#2c3e50', foreground='#3498db')
        style.configure('Custom.TFrame', background='#2c3e50')
        
        self.gracze_entries = []
        self.create_widgets()
    
    def create_widgets(self):
        # Główny frame
        main_frame = ttk.Frame(self.root, style='Custom.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Tytuł
        title_label = ttk.Label(main_frame, text="🏆 KALKULATOR PODZIAŁU NAGRÓD W GANGU 🏆", 
                               style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Frame dla ustawień
        settings_frame = ttk.LabelFrame(main_frame, text="⚙️ Ustawienia", padding=10)
        settings_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Liczba graczy
        ttk.Label(settings_frame, text="Liczba graczy:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.gracze_spinbox = tk.Spinbox(settings_frame, from_=2, to=20, width=10, 
                                        command=self.update_gracze_fields, value=8)
        self.gracze_spinbox.grid(row=0, column=1, sticky=tk.W)
        
        # Pula nagród
        ttk.Label(settings_frame, text="Pula nagród (kredyty):").grid(row=0, column=2, sticky=tk.W, padx=(20, 10))
        self.pula_entry = ttk.Entry(settings_frame, width=15)
        self.pula_entry.insert(0, "15000")
        self.pula_entry.grid(row=0, column=3, sticky=tk.W)
        
        # Checkbox dla wyrównywania
        self.wyrownywanie_var = tk.BooleanVar()
        wyrownywanie_check = ttk.Checkbutton(settings_frame, variable=self.wyrownywanie_var, 
                                           text="⚖️ Wyrównywanie (50% równo + 50% za zasługi)")
        wyrownywanie_check.grid(row=1, column=0, columnspan=4, sticky=tk.W, pady=(10, 0))
        
        # Frame dla graczy
        self.gracze_frame = ttk.LabelFrame(main_frame, text="👥 Gracze i ich wykopane bloki", padding=10)
        self.gracze_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Scroll dla graczy
        canvas = tk.Canvas(self.gracze_frame, bg='#ecf0f1')
        scrollbar = ttk.Scrollbar(self.gracze_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Przyciski
        buttons_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        calc_button = tk.Button(buttons_frame, text="🔢 OBLICZ PODZIAŁ", command=self.calculate_rewards,
                               bg='#27ae60', fg='white', font=('Arial', 12, 'bold'), 
                               relief=tk.RAISED, bd=3, cursor='hand2')
        calc_button.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_button = tk.Button(buttons_frame, text="🔄 WYCZYŚĆ", command=self.clear_all,
                                bg='#e74c3c', fg='white', font=('Arial', 10), 
                                relief=tk.RAISED, bd=2, cursor='hand2')
        clear_button.pack(side=tk.LEFT, padx=(0, 10))
        
        save_button = tk.Button(buttons_frame, text="💾 ZAPISZ", command=self.save_results,
                               bg='#3498db', fg='white', font=('Arial', 10), 
                               relief=tk.RAISED, bd=2, cursor='hand2')
        save_button.pack(side=tk.LEFT)
        
        # Wstępnie utwórz pola dla 8 graczy
        self.update_gracze_fields()
    
    def update_gracze_fields(self):
        # Usuń stare pola
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.gracze_entries = []
        
        # Nagłówki
        ttk.Label(self.scrollable_frame, text="Nazwa gracza", font=('Arial', 10, 'bold')).grid(
            row=0, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Label(self.scrollable_frame, text="Wykopane bloki", font=('Arial', 10, 'bold')).grid(
            row=0, column=1, padx=10, pady=5, sticky=tk.W)
        ttk.Label(self.scrollable_frame, text="Bonus % za wsparcie", font=('Arial', 10, 'bold')).grid(
            row=0, column=2, padx=10, pady=5, sticky=tk.W)
        
        # Stwórz nowe pola
        liczba = int(self.gracze_spinbox.get())
        default_names = ["AnonBOT", "JavaBasti", "O924", "ErrorCodeNova", 
                        "xReaperr3", "Veskko", "Rapukker", "Refqyz"]
        
        for i in range(liczba):
            # Nazwa gracza
            name_entry = ttk.Entry(self.scrollable_frame, width=20)
            if i < len(default_names):
                name_entry.insert(0, default_names[i])
            else:
                name_entry.insert(0, f"Gracz_{i+1}")
            name_entry.grid(row=i+1, column=0, padx=10, pady=2, sticky=tk.W)
            
            # Bloki
            blocks_entry = ttk.Entry(self.scrollable_frame, width=15)
            blocks_entry.insert(0, "0")
            blocks_entry.grid(row=i+1, column=1, padx=10, pady=2, sticky=tk.W)
            
            # Bonus checkbox i pole %
            bonus_var = tk.BooleanVar()
            bonus_check = ttk.Checkbutton(self.scrollable_frame, variable=bonus_var, text="")
            bonus_check.grid(row=i+1, column=2, padx=(10, 5), pady=2, sticky=tk.W)
            
            bonus_entry = ttk.Entry(self.scrollable_frame, width=8)
            bonus_entry.insert(0, "3")  # domyślnie 3%
            bonus_entry.grid(row=i+1, column=3, padx=(0, 10), pady=2, sticky=tk.W)
            ttk.Label(self.scrollable_frame, text="%").grid(row=i+1, column=4, pady=2, sticky=tk.W)
            
            self.gracze_entries.append((name_entry, blocks_entry, bonus_var, bonus_entry))
    
    def calculate_rewards(self):
        try:
            # Pobierz pulę
            pula = int(self.pula_entry.get())
            if pula <= 0:
                raise ValueError("Pula musi być większa od 0")
            
            # Pobierz dane graczy
            gracze_data = []
            suma_blokow = 0
            
            for name_entry, blocks_entry, bonus_var, bonus_entry in self.gracze_entries:
                nazwa = name_entry.get().strip()
                if not nazwa:
                    nazwa = "Nieznany"
                
                try:
                    bloki = int(blocks_entry.get())
                    if bloki < 0:
                        raise ValueError()
                except:
                    bloki = 0
                
                # Sprawdź bonus
                ma_bonus = bonus_var.get()
                bonus_procent = 0
                if ma_bonus:
                    try:
                        bonus_procent = float(bonus_entry.get())
                        if bonus_procent < 0 or bonus_procent > 100:
                            raise ValueError()
                    except:
                        bonus_procent = 3  # domyślnie 3%
                
                gracze_data.append({
                    "nazwa": nazwa, 
                    "bloki": bloki,
                    "bonus": ma_bonus,
                    "bonus_procent": bonus_procent
                })
                suma_blokow += bloki
            
            if suma_blokow == 0:
                messagebox.showwarning("Brak danych", "Żaden gracz nie wykopał bloków!")
                return
            
            # Oblicz nagrody - najpierw bazowe na podstawie bloków
            for gracz in gracze_data:
                procent_bazowy = (gracz["bloki"] / suma_blokow) * 100 if suma_blokow > 0 else 0
                kredyty_bazowe = (gracz["bloki"] / suma_blokow) * pula if suma_blokow > 0 else 0
                
                # Dodaj bonus do kredytów
                if gracz["bonus"]:
                    bonus_kredyty = kredyty_bazowe * (gracz["bonus_procent"] / 100)
                    kredyty_finalne = kredyty_bazowe + bonus_kredyty
                else:
                    kredyty_finalne = kredyty_bazowe
                
                gracz["procent"] = procent_bazowy
                gracz["kredyty_bazowe"] = kredyty_bazowe
                gracz["kredyty"] = kredyty_finalne
            
            # Popraw zaokrąglenia - rozdziel resztę proporcjonalnie
            suma_kredytow_przed = sum(gracz["kredyty"] for gracz in gracze_data)
            pozostalo = pula - int(suma_kredytow_przed)
            
            # Zaokrąglij wszystkich w dół
            for gracz in gracze_data:
                gracz["kredyty"] = int(gracz["kredyty"])
            
            # Rozdaj resztę tym z największymi ułamkami
            if pozostalo > 0:
                reszty = []
                for i, gracz in enumerate(gracze_data):
                    ulamek = (gracz["kredyty_bazowe"] + (gracz["kredyty_bazowe"] * (gracz["bonus_procent"] / 100) if gracz["bonus"] else 0)) % 1
                    reszty.append((ulamek, i))
                
                reszty.sort(reverse=True)
                for j in range(min(pozostalo, len(reszty))):
                    gracze_data[reszty[j][1]]["kredyty"] += 1
            
            # Sortuj od największej liczby kredytów
            gracze_data.sort(key=lambda x: x["kredyty"], reverse=True)
            
            # Pokaż wyniki
            self.show_results(gracze_data, suma_blokow, pula)
            
        except ValueError as e:
            messagebox.showerror("Błąd", f"Niepoprawne dane: {e}")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")
    
    def show_results(self, gracze_data, suma_blokow, pula):
        # Nowe okno z wynikami
        results_window = tk.Toplevel(self.root)
        results_window.title("🏆 Wyniki Podziału Nagród")
        results_window.geometry("700x500")
        results_window.configure(bg='#2c3e50')
        
        # Frame z wynikami
        results_frame = ttk.Frame(results_window)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Tytuł
        title_label = ttk.Label(results_frame, text="🏆 WYNIKI PODZIAŁU NAGRÓD 🏆", 
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=(0, 10))
        
        # Podsumowanie
        suma_kredytow_final = sum(g["kredyty"] for g in gracze_data)
        summary_text = f"📊 Łącznie bloków: {suma_blokow:,} | 💰 Pula: {pula:,} | ✅ Rozdano: {suma_kredytow_final:,} kredytów"
        ttk.Label(results_frame, text=summary_text, font=('Arial', 12)).pack(pady=(0, 10))
        
        # Treeview dla wyników
        columns = ("Miejsce", "Gracz", "Bloki", "Bonus", "Udział", "Kredyty")
        tree = ttk.Treeview(results_frame, columns=columns, show="headings", height=15)
        
        # Nagłówki
        tree.heading("Miejsce", text="🏅 Miejsce")
        tree.heading("Gracz", text="👤 Gracz")
        tree.heading("Bloki", text="⛏️ Bloki")
        tree.heading("Bonus", text="⭐ Bonus")
        tree.heading("Udział", text="📈 Udział")
        tree.heading("Kredyty", text="💰 Kredyty")
        
        # Szerokości kolumn
        tree.column("Miejsce", width=80)
        tree.column("Gracz", width=130)
        tree.column("Bloki", width=80)
        tree.column("Bonus", width=80)
        tree.column("Udział", width=70)
        tree.column("Kredyty", width=90)
        
        # Dodaj dane
        suma_kredytow = 0
        medals = ["🥇", "🥈", "🥉"]
        
        for i, gracz in enumerate(gracze_data):
            medal = medals[i] if i < 3 else "  "
            miejsce = f"{medal} #{i+1}"
            
            # Formatuj bonus
            if gracz["bonus"]:
                bonus_text = f"+{gracz['bonus_procent']:.0f}%"
                bonus_kredyty = gracz["kredyty"] - gracz["kredyty_bazowe"]
            else:
                bonus_text = "-"
            
            tree.insert("", "end", values=(
                miejsce,
                gracz["nazwa"],
                f"{gracz['bloki']:,}",
                bonus_text,
                f"{gracz['procent']:.1f}%",
                f"{gracz['kredyty']:,}"
            ))
            suma_kredytow += gracz["kredyty"]
        
        tree.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar dla treeview
        scrollbar_tree = ttk.Scrollbar(results_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar_tree.set)
        scrollbar_tree.pack(side="right", fill="y")
        
        # Podsumowanie na dole
        summary_label = ttk.Label(results_frame, 
                                 text=f"✅ Suma wypłat: {suma_kredytow:,} kredytów", 
                                 font=('Arial', 12, 'bold'))
        summary_label.pack(pady=(10, 0))
        
        # Zapisz dane do użycia w save_results
        self.last_results = {
            'gracze_data': gracze_data,
            'suma_blokow': suma_blokow,
            'pula': pula,
            'suma_kredytow': suma_kredytow
        }
    
    def clear_all(self):
        # Wyczyść pulę
        self.pula_entry.delete(0, tk.END)
        self.pula_entry.insert(0, "15000")
        
        # Wyczyść pola graczy
        for name_entry, blocks_entry, bonus_var, bonus_entry in self.gracze_entries:
            blocks_entry.delete(0, tk.END)
            blocks_entry.insert(0, "0")
            bonus_var.set(False)
            bonus_entry.delete(0, tk.END)
            bonus_entry.insert(0, "3")
        
        messagebox.showinfo("Wyczyszczono", "Wszystkie pola zostały wyczyszczone!")
    
    def save_results(self):
        if not hasattr(self, 'last_results'):
            messagebox.showwarning("Brak wyników", "Najpierw oblicz podział nagród!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialname=f"podział_nagród_{self.last_results['suma_blokow']}_bloków.txt"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("PODZIAŁ NAGRÓD W GANGU\n")
                    f.write("=" * 50 + "\n\n")
                    f.write(f"Łącznie bloków: {self.last_results['suma_blokow']:,}\n")
                    f.write(f"Pula nagród: {self.last_results['pula']:,} kredytów\n")
                    f.write(f"Rozdano: {self.last_results['suma_kredytow']:,} kredytów\n\n")
                    f.write("RANKING:\n")
                    f.write("-" * 50 + "\n")
                    
                    for i, gracz in enumerate(self.last_results['gracze_data']):
                        f.write(f"#{i+1}. {gracz['nazwa']}\n")
                        f.write(f"    Bloki: {gracz['bloki']:,}\n")
                        f.write(f"    Udział bazowy: {gracz['procent']:.1f}%\n")
                        if gracz['bonus']:
                            bonus_kredyty = gracz['kredyty'] - int(gracz.get('kredyty_bazowe', 0))
                            f.write(f"    Bonus: +{gracz['bonus_procent']:.0f}% (+{bonus_kredyty} kredytów)\n")
                        f.write(f"    Kredyty RAZEM: {gracz['kredyty']:,}\n\n")
                    
                    f.write(f"SUMA WYPŁAT: {self.last_results['suma_kredytow']:,} kredytów\n")
                
                messagebox.showinfo("Zapisano", f"Wyniki zapisane do:\n{filename}")
                
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{e}")

def main():
    root = tk.Tk()
    app = GangRewardCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()