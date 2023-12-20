import tkinter as tk
from random import randint
from time import sleep
import threading

class DFS_Simulator:
	def __init__(self, master, MAXN):
		self.master = master
		self.master.title("DFS Simulator - Coded by @hieuhfgr")
		self.master.configure(bg='#1E1E1E') 
		self.canvas = tk.Canvas(self.master, width=1200, height=700, bg='#1E1E1E', highlightthickness=0)
		self.canvas.pack()
		self.canvas.create_text(900, 50, text=f"DFS Simulator - Created by @hieuhfgr", fill='#ffffff', font=('Helvetica', 20))
		self.MAXN = MAXN + 5
		self.file = "DFS"
		self.adj = []
		self.height = []
		self.cntheight = []
		self.parent = []
		self.pos = []
		self.nodes = []
		self.updateAdj()
		self.colorOn = "#ff5c5c"
		self.colorOff ='#3498db'
		self.sleepTime = 0.1

	def gen(self, MAXN):
		self.MAXN = MAXN
		with open(f"{self.file}.INP", "w") as f:
			for i in range(1, MAXN):
				f.write(f"{max(randint(i-3, i-1), 1)} {i+1}\n")
		print("Done Gen")
		self.readFile()

	def readFile(self):
		self.updateAdj()
		self.DFSInit(1, 0)
		for node in range(1, self.MAXN):
			self.draw_node(node)

	def updateAdj(self):
		self.adj = [[] for _ in range(self.MAXN+5) ]
		self.height = [0 for _ in range(self.MAXN+5)]
		self.parent = [0 for _ in range(self.MAXN+5)]
		self.pos = [[0, 0] for _ in range(self.MAXN+5)]
		self.nodes = [0 for _ in range(self.MAXN+5)]
		self.cntheight = [0 for _ in range(self.MAXN+5)]
		with open(f"{self.file}.INP", "r") as f:
			line = f.readline()
			while line:
				line = line.strip()
				u = int(line.split()[0])
				v = int(line.split()[1])
				self.adj[u].append(v)
				self.adj[v].append(u)
				line = f.readline()
	
	def DFSInit(self, u, par):
		self.height[u] = self.height[par]+1;
		self.parent[u] = par;
		for v in self.adj[u]:
			if (v == par): continue
			self.DFSInit(v, u)

	def check(self):
		for i in range(self.MAXN):
			if(len(self.adj[i]) > 0):
				print(i, end=": ")
				for v in self.adj[i]:
					print(v, end=" ")
				print()

	def dfs(self, u, par):
		self.change_node_color(u, self.colorOn)
		sleep(self.sleepTime)
		flag = True
		for v in self.adj[u]:
			if (v == par): continue
			self.dfs(v, u)
			flag = False
		if (flag): sleep(1)
		sleep(self.sleepTime)
		self.change_node_color(u, self.colorOff)

	def draw_node(self, node):
		sz = 15
		node_radius = sz
		self.cntheight[self.height[node]] += 1
		x, y = self.cntheight[self.height[node]]*100, self.height[node]*50
		self.pos[node] = [x, y]
		self.nodes[node] = self.canvas.create_oval(x - node_radius, y - node_radius, x + node_radius, y + node_radius, fill=self.colorOff, outline='#2c3e50')
		self.canvas.create_text(x, y, text=f"{node}", fill='#000000', font=('Helvetica', sz))

		if self.parent[node] != 0:
			parent_x, parent_y = self.pos[self.parent[node]] 
			self.canvas.create_line(x, y, parent_x, parent_y, fill='#ecf0f1', width=2)

	def change_node_color(self, node_index, color):
		node_id = self.nodes[node_index]
		x, y = self.pos[node_index]
		self.canvas.itemconfig(node_id, fill=color)
		
	def startSimulate(self, root):
		sleep(1)
		meh = self.canvas.create_text(900, 100, text=f"Start DFS", fill='#ffffff', font=('Helvetica', 20))
		self.dfs(root, 0)
		self.canvas.itemconfig(meh, text="Done DFS")

def main():
	root = tk.Tk()
	meh = DFS_Simulator(root, 50)
	meh.gen(30)
	# meh.check()
	dfs_thread_instance = threading.Thread(target=meh.startSimulate, args=(1,))
	dfs_thread_instance.start()
	root.mainloop()

if __name__ == "__main__":
	main()