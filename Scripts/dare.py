import random

Tricks = {
    
#----------------------------Ken Grip------------------------------------

    "BIG_CUP":{"points": 100,"onGrip": 0,  "toGrip": 0, "canFlip": 0}, 
    "SMALL_CUP":{"points": 125, "onGrip": 0, "toGrip": 0, "canFlip": 0},  
    "BASE_CUP":{"points": 150, "onGrip": 0, "toGrip": 0, "canFlip": 0},
    "SPIKE":{"points": 500, "onGrip": 0, "toGrip": 0, "canFlip": 1},
    "DOWNSPIKE":{"points": 500, "onGrip": 0, "toGrip": 1, "canFlip": 0},
    
    "JUGGLE":{"points": 1000, "onGrip": 0, "toGrip": 0, "canFlip": 2},
    "TOSS":{"points": 1000, "onGrip": 0, "toGrip": 1, "canFlip": 2},
    "SWAP":{"points": 0, "onGrip": 0, "toGrip": 1, "canFlip": 0},
    
    "BIRD":{"points": 250, "onGrip": 0, "toGrip": 0, "canFlip": 1},
    "NIGHT_INGALE":{"points": 375, "onGrip": 0, "toGrip": 0, "canFlip": 1}, 
    "UNDER_BIRD":{"points": 500, "onGrip": 0, "toGrip": 0, "canFlip": 1},
    "HANDLESTALL":{"points": 750, "onGrip": 0, "toGrip": 0, "canFlip": 1}, 
    "RING":{"points": 1000, "onGrip": 0, "toGrip": 0, "canFlip": 1}, 
    "WING":{"points": 1000, "onGrip": 0, "toGrip": 0, "canFlip": 1}, 
    "OUTTER_WING":{"points": 1500, "onGrip": 0, "toGrip": 0, "canFlip": 1}, 
    
    
#----------------------------Tama Grip-----------------------------------
 
    "IN":{"points": 1000, "onGrip": 1, "toGrip": 1, "canFlip": 2},
    "LIGHT_HOUSE":{"points": 1250, "onGrip": 1, "toGrip": 1, "canFlip": 2},
    "LUNAR":{"points": 1500, "onGrip": 1, "toGrip": 1, "canFlip": 2},
    "INWARD_LUNAR":{"points": 1875, "onGrip": 1, "toGrip": 1, "canFlip": 2},
       
    "STILT":{"points": 2000, "onGrip": 1, "toGrip": 1, "canFlip": 2},
    "INWARD_STILT":{"points": 2000, "onGrip": 1, "toGrip": 1, "canFlip": 2},
    
    "SWAP":{"points": 0, "onGrip": 1, "toGrip": 0, "canFlip": 0},
    "TOSS":{"points": 1000, "onGrip": 1, "toGrip": 0, "canFlip": 2},
    }

#Difficulty

difficulty = input("difficulty: ").lower()


if difficulty == "easy":
    total_points = 1000
    before_onGrip = 0
elif difficulty == "medium":
    total_points = 5000
    before_onGrip = random.randint(0, 1)
elif difficulty == "hard":
    total_points = 10000
    before_onGrip = before_onGrip = random.randint(0, 1)
else:
    print("Unknown difficulty")
    
dare = []
darePoints = []
before_trick = "None"

    
while total_points > 250:
    trick = random.choice(list(Tricks.items()))[0]

    Trick = Tricks.get(trick)
    points = Trick.get("points")
    onGrip = Trick.get("onGrip")
    toGrip = Trick.get("toGrip")
    canFlip = Trick.get("canFlip")

    if onGrip == before_onGrip and (trick != before_trick and canFlip != 0):
        if points < total_points:
            print(Tricks.get(trick))
            print("-----------------------------------------------------\n")
            if trick == before_trick and canFlip == 1:
                dare.append((str(random.randint(1, 3))+ "T ")+ trick)
            elif canFlip == 1:
                if random.randint(1, 3) == 3:
                    dare.append((str(random.randint(1, 3))+ "T ")+ trick)
                else:
                    dare.append(trick)
            elif canFlip == 2:
                dare.append((str(random.randint(0, 3))+ "T ")+ trick)
            else:
                dare.append(trick)
                
            darePoints.append(points)
            total_points = total_points - points
            before_onGrip = toGrip
            before_trick = trick

            if total_points <= 250:
                break


#--------------- OUTPUT --------------------------
if dare[0][1] != "T":
    print("PULL_UP", end=" ")

if dare[-1].endswith("SPIKE") == False and dare[-1].endswith("IN") == False:
    if before_onGrip == 0:
        dare.append("SPIKE")
        darePoints.append(500)
    else:
        dare.append("IN")
        darePoints.append(500)
    
for x in dare:
    if x == dare[-1]:
        print(x)
    else:
        print(x, "+", end=" ")

for x in darePoints:
    
    print(x, "+", end=" ")

print("Total:", sum(darePoints))
    
    

