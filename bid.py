import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
#s.bind((host,port))
s.bind(("103.72.177.22",port))

s.listen(5)
while True:
	c, addr = s.accept()
	print("Got connection from " + str(addr))
	c.send('Thank you for connecting'.encode(encoding='utf_8'))
	c.close()
	
class Player(object):
	
	def __init__(self,name,id):
		self.coins = 100
		self.turn = 0
		self.name = name
		self.move = 0
		self.bid = 0
		self.id = id
		if(self.id == 1):
			self.player_space = ""
		else:
			self.player_space = "                                  "
		
	def BidTurn(self):
		print(self.player_space + "Move for player " + self.name)
		print(self.player_space + "You have " + str(self.coins) + " coins")
		self.bid = int(input (self.player_space + "Enter the bid amount "))
		if self.bid > self.coins:
			print(self.player_space + "Not enough coins")
			self.BidTurn()
		else:
			#self.coins = self.coins - self.bid
			print("")
			
	def MoveTurn(self):
		print(self.player_space + "Player " + self.name + "'s turn")
		self.move = int(input(self.player_space + "Enter the move"))
		if self.move < 0 or self.move > 8:
			print(self.player_space + "Invalid move. Enter between 1 and 9")
			self.MoveTurn()
		else:
			board[int(self.move/3)][int(self.move%3)] = self.id
			if ThreeInARow(self.id) == 1:
				print(self.player_space + self.name + " has won!")
				exit()
			
		
		
def DisplayBoard():
	for i in range(3):
		for j in range(3):
			print(board[i][j], end=" ")
		print("")
		
def ThreeInARow(id):
	#check horizontals
	for i in range(3):
		if board[i][0]==id and board[i][1]==id and board[i][2]==id:
			return 1
	
	#check verticals
	for i in range(3):
		if board[0][i]==id and board[1][i]==id and board[2][i]==id:
			return 1
	
	
	#check diagonals
		if board[0][0]==id and board[1][1]==id and board[2][2]==id:
			return 1
		else:
			if board[0][2]==id and board[1][1]==id and board[2][0]==id:
				return 1
		
	return 0
		
			

board = [[0,0,0], [0,0,0], [0,0,0]]			
		
p1 = Player("Jill",1)
p2 = Player("Bob",2)

while (1):
	DisplayBoard()
	p1.BidTurn()
	p2.BidTurn()
	
	if p1.bid > p2.bid:
		p1.coins -= p1.bid
		p2.coins += p1.bid
		p1.MoveTurn()
	else:
		if p2.bid > p1.bid:
			p2.coins -= p2.bid
			p1.coins += p2.bid
			p2.MoveTurn()
		else:
			print("Equal bids")
		
	
		
		