#dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
#multi dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# For item print
x=car.items()

print(x)

#for add new property
car["color"]="red"

print(car)

#for property check
if "model" in car:
    print("yes, model present in car")
if "name" in car:
    print("yes, name present in car")

#for add new property
car.update({"age":"45"})

print(car)

#for property drop
car.pop("brand")
print(car)

#multi dictionary access
print(myfamily["child3"]["name"])