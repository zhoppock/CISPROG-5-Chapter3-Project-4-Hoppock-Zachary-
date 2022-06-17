#enter a height from which a ball is dropped from
index = 0.6
height = float(input("Enter the intitial height of the ball from the ground in feet: "))
bounces = int(input("Enter the number of times the ball may bounce: "))
bounceHeight = height * index
totalDistance = height + bounceHeight
count = 1
while count < bounces:
  count += 1
  height = bounceHeight
  bounceHeight = height * index
  totalDistance = totalDistance + height + bounceHeight

print("The ball travelled total distance of", totalDistance, "feet.")