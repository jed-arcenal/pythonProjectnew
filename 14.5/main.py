red = int(input())
green = int(input())
blue = int(input())
if green <= red and green <= blue:
    red -= green
    blue -= green
    green -= green
if red <= green and red <= blue:
    green -= red
    blue -= red
    red -= red
if blue <= green and blue <= red:
    green -= blue
    red -= blue
    blue -= blue
    
#alternate way to solve
#smallest = red
#if smallest > green:
#smallest = green
#if smallest > blue:
#smallest = blue

#updating list for multiple elements
#a = [1,2,3,4,7,12,8,9,13]
#smallest = a[0]
#for element in a"
#if element < smallest:
#smallest = element

print(red, green, blue)
