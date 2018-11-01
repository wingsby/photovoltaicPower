with open("/dpdata/photovoltaic_power/data/train_1.csv") as file:
    cnt = 0
    titles = []
    datalist = []
    for line in file:
        if cnt < 1:
            titles = line.split(',')
        else:
            data = line.split(',')
            datalist.append(data)
        cnt += 1
print(datalist.__len__())