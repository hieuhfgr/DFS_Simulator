import tkinter as tk 
from tkinter import Button
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
		self.InitCanvas()
		self.MAXN = MAXN
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

		self.InitButtons()

	def gen(self, MAXN):
		self.MAXN = MAXN+1
		with open(f"{self.file}.INP", "w") as f:
			for i in range(1, MAXN):
				f.write(f"{max(randint(i-5, i-1), 1)} {i+1}\n")
		print("Generated a Tree")
		# self.readFile()

	def readFile(self):
		self.MAXN=500+1
		self.updateAdj()
		self.MAXN=1
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
		self.height[u] = self.height[par]+1
		self.parent[u] = par
		self.MAXN = max(self.MAXN, u+1)
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
		nodeSZ = 20
		node_radius = nodeSZ
		self.cntheight[self.height[node]] += 1
		x, y = self.cntheight[self.height[node]]*50, self.height[node]*50
		self.pos[node] = [x, y]
		self.nodes[node] = self.canvas.create_oval(x - node_radius, y - node_radius, x + node_radius, y + node_radius, fill=self.colorOff, outline='#2c3e50')
		self.canvas.create_text(x, y, text=f"{node}", fill='#000000', font=('Helvetica', nodeSZ))

		if self.parent[node] != 0:
			parent_x, parent_y = self.pos[self.parent[node]] 
			self.canvas.create_line(x, y, parent_x, parent_y, fill='#ecf0f1', width=2)

	def change_node_color(self, node_index, color):
		node_id = self.nodes[node_index]
		x, y = self.pos[node_index]
		self.canvas.itemconfig(node_id, fill=color)
		
	def startSimulate(self, root):
		self.canvas.itemconfig(self.DFSText, text="Start DFS")
		sleep(1)
		self.dfs(root, 0)
		self.canvas.itemconfig(self.DFSText, text="Done DFS")

	def handleRunDFS(self):
		dfs_thread_instance = threading.Thread(target=self.startSimulate, args=(1,))
		dfs_thread_instance.start()
	
	def handleGenTree(self):
		self.gen(25)

	def handleDrawTree(self):
		self.canvas.delete("all")
		self.InitCanvas()
		self.readFile()
	
	def handleGenAndDraw(self):
		self.handleGenTree()
		self.handleDrawTree()

	def InitButtons(self):
		_1 = Button(self.master, text ="Generate Tree", command=self.handleGenTree)
		_1.place(x=900,y=200)
		_2 = Button(self.master, text ="Draw Tree", command=self.handleDrawTree)
		_2.place(x=900,y=200+50)
		_3 = Button(self.master, text= "Start DFS", command=self.handleRunDFS) 
		_3.place(x=900,y=200+100)
		_4 = Button(self.master, text ="Generate And Draw Tree", command=self.handleGenAndDraw)
		_4.place(x=1000,y=200)

	def InitCanvas(self):
		self.canvas.create_text(900, 50, text=f"DFS Simulator - Created by @hieuhfgr", fill='#ffffff', font=('Helvetica', 20))
		self.DFSText = self.canvas.create_text(900, 200+150, text=f"", fill='#ffffff', font=('Helvetica', 15))

def main():
	root = tk.Tk()
	meh = DFS_Simulator(root, 25)
	root.mainloop()

if __name__ == "__main__":
	main()
