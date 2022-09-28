
def get_num(userinput):  # function to handle exception to a non integer value or negative
    while True:
        num = input(userinput)
        try:
            if float(num) > 0:
                return num
            else:
                print("Please enter a valid value")
        except:
            print("Please enter a valid value")


def get_coats(userinput):  # function to handle exception to number input outside range
    while True:
        num1 = input(userinput)
        try:
            if float(num1) == 1:
                return num1
            elif float(num1) == 2:
                return num1
            elif float(num1) == 3:
                return num1
            else:
                print("Please enter a valid value")
        except:
            print("Please enter a valid value")

class House:
    def __init__(self, rooms, wall, doors, windows, amount, cost, coats):
        self.rooms = rooms
        self.wall = wall
        self.doors = doors
        self.windows = windows
        self.amount = amount
        self.cost = cost
        self.coats = coats

    def coverArea(self):
        total_area = self.wall - self.doors - self.windows
        print("You need to paint "+str(round(total_area, 2))+"m2.")

    def paintcosts(self):
        paintneed = (self.wall - self.doors - self.windows)/(10*self.coats)  # 1litre covers 10m2 https://www.diy.com/ideas-advice/calculators/wall-painting-calculator
        print("With 1 litre of paint covering 10m2 and using "+str(self.coats)+" coats of paint you will need "+str(round(paintneed, 2))+" litres of paint.")

    def costeffect(self):
        costperlitre = self.cost/self.amount
        print("This paint will cost "+str(round(costperlitre, 2))+" £/litre")

    def totalCost(self):
        totalcost = (self.wall - self.doors - self.windows)/(10*self.coats) * self.cost/self.amount # paint needed (litres) multiplied by paint cost per litre
        print("This will cost you £"+str(round(totalcost, 2))+".")

amt = float(get_num("How many litres of paint in the paint can? "))
cst = float(get_num("What is the cost of the paint can you will buy (£)? "))
coats = int(get_coats("Between 1, 2, and 3 coats how many coats of paint do you intend to apply? "))
r = int(get_num("How many rooms do you need to paint? "))
drs = int(get_num("What are the total number of doors in the rooms you will paint (double doors should be inputted as two doors)? ")) * 1.98 * 0.8 # Average door dimensions UK https://www.everest.co.uk/doors/standard-door-sizes/
wdws = int(get_num("What are the total number of windows in the rooms you will paint? "))
wallA = 0
walls = []
walls1 = []
windowsA = 0
windows = []
windows1 = []

for k in range(wdws):
    wl = get_num(f"Please input the length in metres of Window {k + 1}: ")
    ww = get_num(f"Please input the width in metres of Window {k + 1}: ")
    dimension = [ww, wl]
    dimension1 = [ww + "m", wl + "m"]
    windows.append(dimension)
    windows1.append(dimension1)
    print(f"Adding Window {dimension1}")
    print(f"The current Window inputs are {windows1}")
    windowsA += (float(ww)*float(wl))

for i in range(r):
    for j in range(2):
        l = get_num(f"Please input the length in metres of Wall {j + 1} for Room {i + 1}: ")
        w = get_num(f"Please input the width in metres of Wall {j + 1} for Room {i + 1}: ")
        dimension = [w, l]
        dimension1 = [w + "m", l + "m"]
        walls.append(dimension)
        walls1.append(dimension1)
        print(f"Adding wall {dimension1}")
        print(f"The current wall inputs are {walls1}")

for d in walls:
    l = int(d[0])
    w = int(d[1])
    a = l * w * 2
    wallA += a

house = House(r, wallA, drs, windowsA, amt, cst, coats)

house.coverArea()
house.costeffect()
house.paintcosts()
house.totalCost()
