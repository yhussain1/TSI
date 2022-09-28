

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

class House: # Contains all user inputs as attributes
    def __init__(self, walls, wall, exclusions, coats, paint):
        self.walls = walls
        self.wall = wall
        self.exclusions = exclusions
        self.coats = coats
        self.paint = paint

    def coverArea(self): # calculate area that needs to be painted
        total_area = self.wall - self.exclusions
        print("You need to paint "+str(round(total_area, 2))+"m2 of area.")

    def paintuse(self): # amount of paint to use for designated cover area
        paintneed = (self.wall - self.exclusions)*self.coats*1.1/10  # 1litre covers 10m2 including a 10% wastage https://www.diy.com/ideas-advice/calculators/wall-painting-calculator
        print("With 1 litre of paint covering 10m2 having 10% wastage and using "+str(self.coats)+" coats of paint \nyou will need "+str(round(paintneed, 2))+" litres of paint.")

    def totalCost(self): # total cost for area covered
        totalcost = self.paint * (self.wall - self.exclusions)*self.coats/10 # paint cost per litre multiplied by area to cover multiplied by coat of paint to apply divided by area coverage by litre of paint
        print("This will cost you £"+str(round(totalcost, 2))+" exactly.")

def paintchoice(paints): # The options of paint the user can use, basic but can be expanded in further iterations
    if paints == 1:
        print("This calculation will use the Elite Paint")
        paintscost = 4
    elif paints == 2:
        print("This calculation will use the Premium Paint")
        paintscost = 3
    else:
        print("This calculation will use the Standard Paint")
        paintscost = 2
    return paintscost

def exclusionsArea(windowno): # the area of the exclusions
    exclusionA = 0
    exclusion = []
    exclusion1 = []

    for k in range(windowno):
        wl = get_num(f"Please input the length in metres of Exclusion {k + 1}: ")
        ww = get_num(f"Please input the width in metres of Exclusion {k + 1}: ")
        dimension = [ww, wl]
        dimension1 = [ww + "m", wl + "m"]
        exclusion.append(dimension)
        exclusion1.append(dimension1)
        print(f"Adding Exclusion {dimension1}")
        print(f"The current Exclusion inputs are {exclusion1}")
        exclusionA += (float(ww) * float(wl))
    return exclusionA

def wallsArea(rooms): # area of the walls
    wallA = 0
    walls = []
    walls1 = []

    for i in range(r):
        l = get_num(f"Please input the length in metres of Wall {i + 1}: ")
        w = get_num(f"Please input the width in metres of Wall {i + 1}: ")
        dimension = [w, l]
        dimension1 = [w + "m", l + "m"]
        walls.append(dimension)
        walls1.append(dimension1)
        print(f"Adding wall {dimension1}")
        print(f"The current wall inputs are {walls1}")

    for d in walls:
        l = int(d[0])
        w = int(d[1])
        a = l * w
        wallA += a
    return wallA

# the user inputs
r = int(get_num("How many walls do you need to paint? "))
excl = int(get_num("What are the total number of exlusions on the walls you will paint over? "))
paintoption = float(get_coats("You have three options of paint cans to use. Please input the number corresponding to the paint can you would like to use.\n1) Elite Paint £4 per litre\n2) Premium Paint £3 per litre\n3) Standard Paint £2 per litre\n"))
coats = int(get_coats("Between 1, 2, and 3 coats how many coats of paint do you intend to apply? "))


exclusionsA = exclusionsArea(excl)
wallA = wallsArea(r)
paint = paintchoice(paintoption)

house = House(r, wallA, exclusionsA, coats, paint)

house.coverArea()
house.paintuse()
house.totalCost()
