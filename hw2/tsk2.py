boys = ["Александр","Иннокентий","Добрыня","Алиджон"]
girls = ["Петруша","Любовь","Зинаида","Роза",]
g = sorted(girls)
b = sorted(boys)
if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары")
else:
    for idx in range(len(b)):
        print(b[idx],g[idx])