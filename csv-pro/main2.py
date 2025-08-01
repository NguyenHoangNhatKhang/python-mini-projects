import pandas 
data = pandas.read_csv("2018_Central_Park.csv")
data_color = data["Primary Fur Color"]

def count_color(color):
        result = data[data["Primary Fur Color"]==color.title()].shape[0]
        return {"Color":color,"Count":result}

results = [
    count_color("black"),
    count_color("gray"),
    count_color("cinamon")    
]

new_data = pandas.DataFrame(results)
new_data.to_csv("squirrel_count.csv")