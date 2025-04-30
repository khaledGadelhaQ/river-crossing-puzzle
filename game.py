import tkinter as tk
from tkinter import messagebox
from collections import deque

class WolfGoatCabbageGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐺🐐🥬 River Crossing Puzzle")
        self.root.geometry("800x600")
        self.root.configure(bg="#F0F8FF")
        self.root.resizable(False, False)

        self.left_bank = {"wolf", "goat", "cabbage", "farmer"}
        self.right_bank = set()
        self.boat_position = "left"
        self.selected_item = None
        self.moves_count = 0
        self.auto_solving = False

        self.bg_color = "#B2E2F2"
        self.water_color = "#3AA1D9"
        self.bank_color = "#8D5524"
        self.boat_color = "#DEB887"

        self.emoji = {"wolf": "🐺", "goat": "🐐", "cabbage": "🥬", "farmer": "👨‍🌾"}

        self.canvas = tk.Canvas(root, width=800, height=500, bg=self.bg_color, highlightthickness=0)
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.handle_click)

        frame = tk.Frame(root, bg="#F0F8FF")
        frame.pack(fill=tk.X, pady=5)

        btn_style = {"font": ("Arial", 12, "bold"), "borderwidth": 2, "relief": tk.RAISED, "padx": 10, "pady": 5}
        tk.Button(frame, text="🔄 Reset Game", command=self.reset_game, bg="#FF6B6B", fg="white", **btn_style).pack(side=tk.LEFT, padx=15)
        tk.Button(frame, text="🤖 Auto Solve", command=self.auto_solve, bg="#4ECDC4", fg="white", **btn_style).pack(side=tk.LEFT, padx=15)

        self.move_label = tk.Label(frame, text="🚶 Moves: 0", font=("Arial", 14, "bold"), bg="#F0F8FF", fg="#333333")
        self.move_label.pack(side=tk.RIGHT, padx=15)

        self.status_label = tk.Label(root, text="Select an item then click the boat.", font=("Arial", 12), bg="#F0F8FF", fg="#333333", wraplength=780)
        self.status_label.pack(pady=10)

        self.draw_game()

    def draw_game(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 800, 500, fill=self.bg_color, outline="")
        self.canvas.create_oval(650, 30, 700, 80, fill="#FFDD33", outline="#FFB90F")
        for x, y in [(100,50),(250,70),(450,40),(600,60)]:
            for dx, dy in [(0,0),(15,10),(30,0),(45,10),(60,0)]:
                self.canvas.create_oval(x+dx-20, y+dy-20, x+dx+20, y+dy+20, fill="white", outline="")
        for y in range(200,300,10):
            self.canvas.create_rectangle(0, y, 800, y+10, fill=self.water_color, outline="")
        for bx, w in [(0,300),(500,300)]:
            self.canvas.create_rectangle(bx,100,bx+w,400, fill=self.bank_color, outline="")
            for x in range(bx, bx+w, 20):
                self.canvas.create_rectangle(x,100,x+20,110, fill="#567d46", outline="")
        boat_x = 250 if self.boat_position=="left" else 450
        self.canvas.create_oval(boat_x+10,275,boat_x+90,285, fill="#2C7AAF", outline="")
        self.canvas.create_polygon(boat_x,250,boat_x+20,270,boat_x+80,270,boat_x+100,250, fill=self.boat_color, outline="black", width=2)

        def draw_bank(bank, x0):
            x = x0
            for it in bank:
                y = {"wolf":150,"goat":200,"cabbage":250,"farmer":300}[it]
                bg = {"wolf":"#DDDDDD","goat":"#FFFFFF","cabbage":"#AAFFAA","farmer":"#FFE4C4"}[it]
                self.canvas.create_oval(x-25,y-25,x+25,y+25, fill=bg, outline="#333333", width=2, tags=it)
                self.canvas.create_text(x,y, text=self.emoji[it], font=("Arial",30), tags=it)
                x += 80
        draw_bank(self.left_bank, 50)
        draw_bank(self.right_bank, 550)

        # draw farmer on boat if present
        if "farmer" in (self.left_bank if self.boat_position=="left" else self.right_bank):
            self.canvas.create_text(boat_x+30,250, text=self.emoji["farmer"], font=("Arial",25))
        if self.selected_item and self.selected_item!="farmer":
            self.canvas.create_text(boat_x+80,250, text=self.emoji[self.selected_item], font=("Arial",25))

        if self.selected_item:
            self.canvas.create_text(400,50, text=f"Selected: {self.emoji[self.selected_item]} {self.selected_item}", font=("Arial",16,"bold"), fill="#FF5733")

    def handle_click(self, event):
        if self.auto_solving:
            return
        # check item click
        clicked = self.canvas.find_withtag("current")
        if clicked:
            tags = self.canvas.gettags(clicked[0])
            for t in tags:
                if t in ["wolf","goat","cabbage","farmer"]:
                    self.select_item(t)
                    return
        # check boat click
        bx = 250 if self.boat_position=="left" else 450
        if bx <= event.x <= bx+100 and 230 <= event.y <=270:
            self.move_boat()

    def select_item(self, item):
        bank = self.left_bank if self.boat_position=="left" else self.right_bank
        if item in bank:
            if self.selected_item==item:
                self.selected_item=None
                self.status_label.config(text="Item deselected.")
            else:
                self.selected_item=item
                self.status_label.config(text=f"Selected {item}. Now click the boat.")
            self.draw_game()

    def move_boat(self):
        src = self.left_bank if self.boat_position=="left" else self.right_bank
        dst = self.right_bank if self.boat_position=="left" else self.left_bank
        # move farmer
        src.remove("farmer"); dst.add("farmer")
        # maybe move cargo
        if self.selected_item and self.selected_item!="farmer":
            src.remove(self.selected_item); dst.add(self.selected_item)
        self.boat_position = "right" if self.boat_position=="left" else "left"
        self.moves_count += 1
        self.move_label.config(text=f"🚶 Moves: {self.moves_count}")
        self.selected_item = None
        self.status_label.config(text="Moved to other bank.")
        self.draw_game()
        self.check_game_state()

    def check_game_state(self):
        if len(self.right_bank)==4:
            messagebox.showinfo("🎉","You won in %d moves!"%self.moves_count)
            return
        for b in (self.left_bank, self.right_bank):
            if "farmer" not in b:
                if {"wolf","goat"}.issubset(b):
                    messagebox.showinfo("🐺","Wolf ate goat!"); self.reset_game(); return
                if {"goat","cabbage"}.issubset(b):
                    messagebox.showinfo("🐐","Goat ate cabbage!"); self.reset_game(); return

    def reset_game(self):
        self.left_bank={"wolf","goat","cabbage","farmer"}; self.right_bank=set(); self.boat_position="left"
        self.selected_item=None; self.moves_count=0; self.auto_solving=False
        self.move_label.config(text="🚶 Moves: 0"); self.status_label.config(text="Game reset. Select an item.")
        self.draw_game()

    def auto_solve(self):
        self.reset_game(); self.auto_solving=True; self.status_label.config(text="🤖 Solving...")
        steps = self.solve_bfs()
        if not steps:
            self.status_label.config(text="No solution."); return
        self.execute_solution(steps,0)

    def execute_solution(self, steps, idx):
        if idx>=len(steps):
            self.auto_solving=False; self.status_label.config(text="Solved!"); return
        l,r,boat,item = steps[idx]
        self.left_bank=set(l); self.right_bank=set(r); self.boat_position=boat
        self.moves_count+=1; self.move_label.config(text=f"🚶 Moves: {self.moves_count}")
        self.status_label.config(text=f"Moving {item or 'farmer'}...")
        self.draw_game()
        self.root.after(800, lambda: self.execute_solution(steps,idx+1))

    def solve_bfs(self):
        start=(frozenset(self.left_bank),frozenset(self.right_bank),self.boat_position)
        goal=(frozenset(),frozenset({"wolf","goat","cabbage","farmer"}),"right")
        queue=deque([(start,[])])
        seen={start}
        while queue:
            (l,r,boat),path=queue.popleft()
            if (l,r,boat)==goal: return path
            banks=(l,r) if boat=="left" else (r,l)
            for itm in [None]+[i for i in banks[0] if i!="farmer"]:
                s=set(banks[0]); d=set(banks[1])
                s.remove("farmer"); d.add("farmer")
                if itm: s.remove(itm); d.add(itm)
                if self.is_valid_state(s) and self.is_valid_state(d):
                    nboat="right" if boat=="left" else "left"
                    nl,nr=(s,d) if boat=="left" else (d,s)
                    st=(frozenset(nl),frozenset(nr),nboat)
                    if st not in seen:
                        seen.add(st); queue.append((st,path+[(nl,nr,nboat,itm)]))
        return None

    def is_valid_state(self, bank):
        if "farmer" in bank: return True
        if {"wolf","goat"}.issubset(bank): return False
        if {"goat","cabbage"}.issubset(bank): return False
        return True

if __name__ == "__main__":
    root=tk.Tk()
    WolfGoatCabbageGame(root)
    root.mainloop()
