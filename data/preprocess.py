import time

def getData(batch_size):
    filename='/dpdata/photovoltaic_power/data/train_1.csv'
    while (1):
        with open(filename, encoding='utf-8') as file:
            cnt = 0
            titles = []
            datalist = []
            labels = []
            for line in file:
                if cnt < 1:
                    titles = line.split(',')
                else:
                    data = line.split(',')
                    ctime = time.strptime(data[0], "%Y-%m-%d %H:%M:%S")
                    ndata = []
                    # ndata.append(cnt)
                    ndata.append(ctime[1])
                    ndata.append(ctime[2])
                    ndata.append(ctime[3])
                    ndata.append(ctime[4])
                    ndata.append(ctime[5])
                    ndata.append(float(data[1]))
                    ndata.append(float(data[2]))
                    ndata.append(float(data[3]))
                    ndata.append(float(data[4]))
                    ndata.append(float(data[5]))
                    ndata.append(float(data[6]))
                    label = float(data[8])
                    labels.append(label)
                    datalist.append(ndata)
                    if (datalist.__len__() >= batch_size):
                        yield (datalist, labels)
                        datalist = []
                        labels = []
                cnt += 1
                # return datalist,labels
                # print(datalist.__len__())


def getValData():
    filename = "/dpdata/photovoltaic_power/data/train_1.csv"
    with open(filename, encoding='utf-8') as file:
        cnt = 0
        titles = []
        datalist = []
        labels = []
        for line in file:
            cnt += 1
            if cnt < 60000:
                continue
            if cnt < 1:
                titles = line.split(',')
            else:
                data = line.split(',')
                ctime = time.strptime(data[0], "%Y-%m-%d %H:%M:%S")
                ndata = []
                # ndata.append(cnt)
                ndata.append(ctime[1])
                ndata.append(ctime[2])
                ndata.append(ctime[3])
                ndata.append(ctime[4])
                ndata.append(ctime[5])
                ndata.append(float(data[1]))
                ndata.append(float(data[2]))
                ndata.append(float(data[3]))
                ndata.append(float(data[4]))
                ndata.append(float(data[5]))
                ndata.append(float(data[6]))
                label = float(data[8])
                labels.append(label)
                datalist.append(ndata)

    return datalist, labels

def getPredictData():
    filename = "/dpdata/photovoltaic_power/data/test_1.csv"
    with open(filename, encoding='utf-8') as file:
        cnt = 0
        titles = []
        datalist = []
        labels = []
        for line in file:
            cnt += 1
            if cnt < 60000:
                continue
            if cnt < 1:
                titles = line.split(',')
            else:
                data = line.split(',')
                ctime = time.strptime(data[0], "%Y-%m-%d %H:%M:%S")
                ndata = []
                # ndata.append(cnt)
                ndata.append(ctime[1])
                ndata.append(ctime[2])
                ndata.append(ctime[3])
                ndata.append(ctime[4])
                ndata.append(ctime[5])
                ndata.append(float(data[1]))
                ndata.append(float(data[2]))
                ndata.append(float(data[3]))
                ndata.append(float(data[4]))
                ndata.append(float(data[5]))
                ndata.append(float(data[6]))
                label = float(data[8])
                labels.append(label)
                datalist.append(ndata)
# getData()
# getValData()
