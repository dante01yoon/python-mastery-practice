grid = [[1, 2, 3], [4, 5, 6]]
print(grid[0])
print(grid[1][2])
grid[0][0] = 10
print(grid)
print(len(grid), len(grid[0]))

students = [
    {"name": "민지", "score": 90},
    {"name": "준호", "score": 75},
]
print(students[0]["name"])
students.append({"name": "서연", "score": 88})
print(len(students), students[-1]["score"])

menu = {"커피": ["아메리카노", "라떼"], "차": ["녹차"]}
menu["차"].append("홍차")
print(menu["차"])
print(menu["커피"][1])
