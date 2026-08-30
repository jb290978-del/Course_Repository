motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("bmw")
print(motorcycles)

motorcycles[1] = "kawasaki"
print(motorcycles)

motorcycles.insert(1, "lambretta")
print(motorcycles)

del motorcycles[1]
print(motorcycles)

last_owned = motorcycles[-1]
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles.remove("ducati")
print(motorcycles)
print(f"I won't buy a {motorcycles[-2].title()} because they're too expensive for me.")

print(len(motorcycles))