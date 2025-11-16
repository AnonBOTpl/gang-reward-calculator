#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class GangRewardCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🏆 Gang Reward Split Calculator")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#2c3e50', foreground='#ecf0f1')
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), background='#2c3e50', foreground='#3498db')
        style.configure('Custom.TFrame', background='#2c3e50')
        
        self.players_entries = []
        self.create_widgets()
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, style='Custom.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = ttk.Label(main_frame, text="🏆 GANG REWARD SPLIT CALCULATOR 🏆", 
                               style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Settings frame
        settings_frame = ttk.LabelFrame(main_frame, text="⚙️ Settings", padding=10)
        settings_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Number of players
        ttk.Label(settings_frame, text="Number of players:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.players_spinbox = tk.Spinbox(settings_frame, from_=2, to=20, width=10, 
                                        command=self.update_players_fields, value=8)
        self.players_spinbox.grid(row=0, column=1, sticky=tk.W)
        
        # Reward pool
        ttk.Label(settings_frame, text="Reward pool (credits):").grid(row=0, column=2, sticky=tk.W, padx=(20, 10))
        self.pool_entry = ttk.Entry(settings_frame, width=15)
        self.pool_entry.insert(0, "15000")
        self.pool_entry.grid(row=0, column=3, sticky=tk.W)
        
        # Equalization checkbox
        self.equalize_var = tk.BooleanVar()
        equalize_check = ttk.Checkbutton(settings_frame, variable=self.equalize_var, 
                                           text="⚖️ Equalization (50% equally + 50% by contribution)")
        equalize_check.grid(row=1, column=0, columnspan=4, sticky=tk.W, pady=(10, 0))
        
        # Players frame
        self.players_frame = ttk.LabelFrame(main_frame, text="👥 Players and their mined blocks", padding=10)
        self.players_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Scroll for players
        canvas = tk.Canvas(self.players_frame, bg='#ecf0f1')
        scrollbar = ttk.Scrollbar(self.players_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons
        buttons_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        calc_button = tk.Button(buttons_frame, text="🔢 CALCULATE", command=self.calculate_rewards,
                               bg='#27ae60', fg='white', font=('Arial', 12, 'bold'), 
                               relief=tk.RAISED, bd=3, cursor='hand2')
        calc_button.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_button = tk.Button(buttons_frame, text="🔄 CLEAR", command=self.clear_all,
                                bg='#e74c3c', fg='white', font=('Arial', 10), 
                                relief=tk.RAISED, bd=2, cursor='hand2')
        clear_button.pack(side=tk.LEFT, padx=(0, 10))
        
        save_button = tk.Button(buttons_frame, text="💾 SAVE", command=self.save_results,
                               bg='#3498db', fg='white', font=('Arial', 10), 
                               relief=tk.RAISED, bd=2, cursor='hand2')
        save_button.pack(side=tk.LEFT)
        
        # Initial fields for 8 players
        self.update_players_fields()

    def update_players_fields(self):
        # Clear old fields
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.players_entries = []
        
        # Headers
        ttk.Label(self.scrollable_frame, text="Player name", font=('Arial', 10, 'bold')).grid(
            row=0, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Label(self.scrollable_frame, text="Mined blocks", font=('Arial', 10, 'bold')).grid(
            row=0, column=1, padx=10, pady=5, sticky=tk.W)
        ttk.Label(self.scrollable_frame, text="Bonus % for support", font=('Arial', 10, 'bold')).grid(
            row=0, column=2, padx=10, pady=5, sticky=tk.W)
        
        # Create new fields
        count = int(self.players_spinbox.get())
        default_names = ["AnonBOT", "JavaBasti", "O924", "ErrorCodeNova", 
                        "xReaperr3", "Veskko", "Rapukker", "Refqyz"]
        
        for i in range(count):
            # Player name
            name_entry = ttk.Entry(self.scrollable_frame, width=20)
            if i < len(default_names):
                name_entry.insert(0, default_names[i])
            else:
                name_entry.insert(0, f"Player_{i+1}")
            name_entry.grid(row=i+1, column=0, padx=10, pady=2, sticky=tk.W)
            
            # Blocks
            blocks_entry = ttk.Entry(self.scrollable_frame, width=15)
            blocks_entry.insert(0, "0")
            blocks_entry.grid(row=i+1, column=1, padx=10, pady=2, sticky=tk.W)
            
            # Bonus checkbox and % field
            bonus_var = tk.BooleanVar()
            bonus_check = ttk.Checkbutton(self.scrollable_frame, variable=bonus_var, text="")
            bonus_check.grid(row=i+1, column=2, padx=(10, 5), pady=2, sticky=tk.W)
            
            bonus_entry = ttk.Entry(self.scrollable_frame, width=8)
            bonus_entry.insert(0, "3")  # default 3%
            bonus_entry.grid(row=i+1, column=3, padx=(0, 10), pady=2, sticky=tk.W)
            ttk.Label(self.scrollable_frame, text="%").grid(row=i+1, column=4, pady=2, sticky=tk.W)
            
            self.players_entries.append((name_entry, blocks_entry, bonus_var, bonus_entry))

    def calculate_rewards(self):
        try:
            pool = int(self.pool_entry.get())
            if pool <= 0:
                raise ValueError("Pool must be greater than 0")
            
            players_data = []
            total_blocks = 0
            
            for name_entry, blocks_entry, bonus_var, bonus_entry in self.players_entries:
                name = name_entry.get().strip()
                if not name:
                    name = "Unknown"
                
                try:
                    blocks = int(blocks_entry.get())
                    if blocks < 0:
                        raise ValueError()
                except:
                    blocks = 0
                
                has_bonus = bonus_var.get()
                bonus_percent = 0
                if has_bonus:
                    try:
                        bonus_percent = float(bonus_entry.get())
                        if bonus_percent < 0 or bonus_percent > 100:
                            raise ValueError()
                    except:
                        bonus_percent = 3
                
                players_data.append({
                    "name": name,
                    "blocks": blocks,
                    "bonus": has_bonus,
                    "bonus_percent": bonus_percent
                })
                total_blocks += blocks
            
            if total_blocks == 0:
                messagebox.showwarning("No data", "No player mined any blocks!")
                return
            
            for player in players_data:
                base_percent = (player["blocks"] / total_blocks) * 100 if total_blocks > 0 else 0
                base_credits = (player["blocks"] / total_blocks) * pool if total_blocks > 0 else 0
                
                if player["bonus"]:
                    bonus_credits = base_credits * (player["bonus_percent"] / 100)
                    final_credits = base_credits + bonus_credits
                else:
                    final_credits = base_credits
                
                player["percent"] = base_percent
                player["base_credits"] = base_credits
                player["credits"] = final_credits
            
            total_before = sum(player["credits"] for player in players_data)
            remaining = pool - int(total_before)
            
            for player in players_data:
                player["credits"] = int(player["credits"])
            
            if remaining > 0:
                fractions = []
                for i, player in enumerate(players_data):
                    fraction = (player["base_credits"] + (player["base_credits"] * (player["bonus_percent"] / 100) if player["bonus"] else 0)) % 1
                    fractions.append((fraction, i))
                
                fractions.sort(reverse=True)
                for j in range(min(remaining, len(fractions))):
                    players_data[fractions[j][1]]["credits"] += 1
            
            players_data.sort(key=lambda x: x["credits"], reverse=True)
            self.show_results(players_data, total_blocks, pool)
            
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid data: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_results(self, players_data, total_blocks, pool):
        results_window = tk.Toplevel(self.root)
        results_window.title("🏆 Reward Split Results")
        results_window.geometry("700x500")
        results_window.configure(bg='#2c3e50')
        
        results_frame = ttk.Frame(results_window)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(results_frame, text="🏆 REWARD SPLIT RESULTS 🏆", 
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=(0, 10))
        
        total_credits = sum(p["credits"] for p in players_data)
        summary_text = f"📊 Total blocks: {total_blocks:,} | 💰 Pool: {pool:,} | ✅ Distributed: {total_credits:,} credits"
        ttk.Label(results_frame, text=summary_text, font=('Arial', 12)).pack(pady=(0, 10))
        
        columns = ("Rank", "Player", "Blocks", "Bonus", "Share", "Credits")
        tree = ttk.Treeview(results_frame, columns=columns, show="headings", height=15)
        
        tree.heading("Rank", text="🏅 Rank")
        tree.heading("Player", text="👤 Player")
        tree.heading("Blocks", text="⛏️ Blocks")
        tree.heading("Bonus", text="⭐ Bonus")
        tree.heading("Share", text="📈 Share")
        tree.heading("Credits", text="💰 Credits")
        
        tree.column("Rank", width=80)
        tree.column("Player", width=130)
        tree.column("Blocks", width=80)
        tree.column("Bonus", width=80)
        tree.column("Share", width=70)
        tree.column("Credits", width=90)
        
        medals = ["🥇", "🥈", "🥉"]
        total = 0
        for i, player in enumerate(players_data):
            medal = medals[i] if i < 3 else "  "
            rank = f"{medal} #{i+1}"
            bonus_text = f"+{player['bonus_percent']:.0f}%" if player["bonus"] else "-"
            
            tree.insert("", "end", values=(
                rank,
                player["name"],
                f"{player['blocks']:,}",
                bonus_text,
                f"{player['percent']:.1f}%",
                f"{player['credits']:,}"
            ))
            total += player["credits"]
        
        tree.pack(fill=tk.BOTH, expand=True)
        scrollbar_tree = ttk.Scrollbar(results_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar_tree.set)
        scrollbar_tree.pack(side="right", fill="y")
        
        summary_label = ttk.Label(results_frame, 
                                 text=f"✅ Total payouts: {total:,} credits", 
                                 font=('Arial', 12, 'bold'))
        summary_label.pack(pady=(10, 0))
        
        self.last_results = {
            'players_data': players_data,
            'total_blocks': total_blocks,
            'pool': pool,
            'total_credits': total
        }

    def clear_all(self):
        self.pool_entry.delete(0, tk.END)
        self.pool_entry.insert(0, "15000")
        
        for name_entry, blocks_entry, bonus_var, bonus_entry in self.players_entries:
            blocks_entry.delete(0, tk.END)
            blocks_entry.insert(0, "0")
            bonus_var.set(False)
            bonus_entry.delete(0, tk.END)
            bonus_entry.insert(0, "3")
        
        messagebox.showinfo("Cleared", "All fields have been reset!")

    def save_results(self):
        if not hasattr(self, 'last_results'):
            messagebox.showwarning("No results", "Calculate rewards first!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialfile=f"reward_split_{self.last_results['total_blocks']}_blocks.txt"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("GANG REWARD SPLIT\n")
                    f.write("=" * 50 + "\n\n")
                    f.write(f"Total blocks: {self.last_results['total_blocks']:,}\n")
                    f.write(f"Reward pool: {self.last_results['pool']:,} credits\n")
                    f.write(f"Distributed: {self.last_results['total_credits']:,} credits\n\n")
                    f.write("RANKING:\n")
                    f.write("-" * 50 + "\n")
                    
                    for i, player in enumerate(self.last_results['players_data']):
                        f.write(f"#{i+1}. {player['name']}\n")
                        f.write(f"    Blocks: {player['blocks']:,}\n")
                        f.write(f"    Base share: {player['percent']:.1f}%\n")
                        if player['bonus']:
                            bonus_credits = player['credits'] - int(player.get('base_credits', 0))
                            f.write(f"    Bonus: +{player['bonus_percent']:.0f}% (+{bonus_credits} credits)\n")
                        f.write(f"    TOTAL Credits: {player['credits']:,}\n\n")
                    
                    f.write(f"TOTAL PAYOUTS: {self.last_results['total_credits']:,} credits\n")
                
                messagebox.showinfo("Saved", f"Results saved to:\n{filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")

def main():
    root = tk.Tk()
    app = GangRewardCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
