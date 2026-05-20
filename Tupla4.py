month = ("enero","febrero","marzo","abril",'mayo',"mayo",'junio',"julio","agosto","septiembre","octubre","noviembre","diciembre")

profits = (20000, 45000, 70000, 970000, 12000,456000,65000,54000,
           10000,30000,70000,90000)

max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)