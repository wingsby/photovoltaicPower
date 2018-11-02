import datetime
import time


# 归一化处理


def getData(batch_size,fileid=1):
    filename = '/dpdata/photovoltaic_power/data/train_%d.csv' % fileid
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
                    mstime = data[0].split('.')
                    ctime = time.strptime(mstime[0], "%Y-%m-%d %H:%M:%S")
                    if mstime.__len__() > 1:
                        ctime = time.localtime(time.mktime(ctime) + round(float(mstime[1]) / 1000))
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


def getValData(fileid=1):
    filename = "/dpdata/photovoltaic_power/data/train_%d.csv" % fileid
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
                mstime = data[0].split('.')
                ctime = time.strptime(mstime[0], "%Y-%m-%d %H:%M:%S")
                if mstime.__len__() > 1:
                    ctime = time.localtime(time.mktime(ctime) + round(float(mstime[1]) / 1000))
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


def getPredictData(fileid=1):
    filename = "/dpdata/photovoltaic_power/data/test_%d.csv" % fileid
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
                mstime = data[1].split('.')
                ctime = time.strptime(mstime[0], "%Y-%m-%d %H:%M:%S")
                if mstime.__len__()>1:
                    ctime = time.localtime(time.mktime(ctime) + round(float(mstime[1]) / 1000))
                ndata = []
                # ndata.append(cnt)
                ndata.append(ctime[1])
                ndata.append(ctime[2])
                ndata.append(ctime[3])
                ndata.append(ctime[4])
                ndata.append(ctime[5])
                ndata.append(float(data[2]))
                ndata.append(float(data[3]))
                ndata.append(float(data[4]))
                ndata.append(float(data[5]))
                ndata.append(float(data[6]))
                ndata.append(float(data[7]))
                # label = float(data[8])
                # labels.append(label)
                datalist.append(ndata)
            cnt += 1
    return datalist


def writePredictData(output,fileid=1):
    filename = "/dpdata/photovoltaic_power/data/out_%d.csv" % fileid
    file = open(filename, 'w', encoding='utf-8')
    for i in range(output.__len__()):
        str = ('%d,%f') % (i + 1, output[0][i])
        file.write(str)
    file.close()


def composeData(output,fileid=1):
    filename = "/dpdata/photovoltaic_power/data/out_%d.csv" % fileid
    file = open(filename, 'w', encoding='utf-8')
    for i in range(output.__len__()):
        str = ('%d,%f') % (i + 1, output[0][i])
        file.write(str)
    file.close()


# getData()
# getValData()
# d=getPredictData()
# print('hi')
# writePredictData([1,2])