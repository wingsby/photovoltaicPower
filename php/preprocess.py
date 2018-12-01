import datetime
import time


# 归一化处理


def getData1(batch_size,fileid=1):
    # filename = '/dpdata/photovoltaic_power/data/train_%d.csv' % fileid
    filename = 'e:/tcdata/photovoltaic_power/train_%d.csv' % fileid
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
                    ndata.append(ctime[0])
                    ndata.append(ctime[1])
                    ndata.append(ctime[2])
                    ndata.append(ctime[3])
                    ndata.append(ctime[4])
                    ndata.append(float(data[1]))
                    ndata.append(float(data[2]))
                    ndata.append(float(data[3]))
                    ndata.append(float(data[4]))
                    ndata.append(float(data[5]))
                    ndata.append(float(data[6]))
                    ndata.append(pow(float(data[1]), 2))
                    ndata.append(pow(float(data[2]), 2))
                    ndata.append(pow(float(data[3]), 2))
                    ndata.append(pow(float(data[4]), 2))
                    ndata.append(pow(float(data[5]), 2))
                    ndata.append(pow(float(data[6]), 2))
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

# 17 特征
def getValData1(fileid=1):
    # filename = "/dpdata/photovoltaic_power/data/train_%d.csv" % fileid
    filename = "e:/tcdata/photovoltaic_power/train_%d.csv" % fileid
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
                ndata.append(ctime[0])
                ndata.append(ctime[1])
                ndata.append(ctime[2])
                ndata.append(ctime[3])
                ndata.append(ctime[4])
                ndata.append(float(data[1]))
                ndata.append(float(data[2]))
                ndata.append(float(data[3]))
                ndata.append(float(data[4]))
                ndata.append(float(data[5]))
                ndata.append(float(data[6]))
                ndata.append(pow(float(data[1]),2))
                ndata.append(pow(float(data[2]),2))
                ndata.append(pow(float(data[3]),2))
                ndata.append(pow(float(data[4]),2))
                ndata.append(pow(float(data[5]),2))
                ndata.append(pow(float(data[6]),2))
                label = float(data[8])
                labels.append(label)
                datalist.append(ndata)
    return datalist, labels


def getValData1(fileid=1):
    # filename = "/dpdata/photovoltaic_power/data/train_%d.csv" % fileid
    filename = "e:/tcdata/photovoltaic_power/train_%d.csv" % fileid
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
                ndata.append(ctime[0])
                ndata.append(ctime[1])
                ndata.append(ctime[2])
                ndata.append(ctime[3])
                ndata.append(ctime[4])
                ndata.append(float(data[1]))
                ndata.append(float(data[2]))
                ndata.append(float(data[3]))
                ndata.append(float(data[4]))
                ndata.append(float(data[5]))
                ndata.append(float(data[6]))
                ndata.append(pow(float(data[1]),2))
                ndata.append(pow(float(data[2]),2))
                ndata.append(pow(float(data[3]),2))
                ndata.append(pow(float(data[4]),2))
                ndata.append(pow(float(data[5]),2))
                ndata.append(pow(float(data[6]),2))
                label = float(data[8])
                labels.append(label)
                datalist.append(ndata)
    return datalist, labels






def getData(batch_size,fileid=1):
    # filename = '/dpdata/photovoltaic_power/data/train_%d.csv' % fileid
    filename = 'e:/tcdata/photovoltaic_power/train_%d.csv' % fileid
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
    # filename = "/dpdata/photovoltaic_power/data/train_%d.csv" % fileid
    filename = "e:/tcdata/photovoltaic_power/train_%d.csv" % fileid
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
                ndata.append(ctime[0])
                ndata.append(ctime[1])
                ndata.append(ctime[2])
                ndata.append(ctime[3])
                ndata.append(ctime[4])
                ndata.append(float(data[1]))
                ndata.append(float(data[2]))
                ndata.append(float(data[3]))
                ndata.append(float(data[4]))
                ndata.append(float(data[5]))
                ndata.append(float(data[6]))
                ndata.append(pow(float(data[1]),2))
                ndata.append(pow(float(data[2]),2))
                ndata.append(pow(float(data[3]),2))
                ndata.append(pow(float(data[4]),2))
                ndata.append(pow(float(data[5]),2))
                ndata.append(pow(float(data[6]),2))
                label = float(data[8])
                labels.append(label)
                datalist.append(ndata)

    return datalist, labels


def getPredictData(fileid=1):
    filename = "e:/tcdata/photovoltaic_power/test_%d.csv" % fileid
    # filename = "/dpdata/photovoltaic_power/data/test_%d.csv" % fileid
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
                ndata.append(ctime[0])
                ndata.append(ctime[1])
                ndata.append(ctime[2])
                ndata.append(ctime[3])
                ndata.append(ctime[4])
                # ndata.append(ctime[5])
                ndata.append(float(data[2]))
                ndata.append(float(data[3]))
                ndata.append(float(data[4]))
                ndata.append(float(data[5]))
                ndata.append(float(data[6]))
                ndata.append(float(data[7]))


                ndata.append(pow(float(data[2]), 2))
                ndata.append(pow(float(data[3]), 2))
                ndata.append(pow(float(data[4]), 2))
                ndata.append(pow(float(data[5]), 2))
                ndata.append(pow(float(data[6]), 2))
                ndata.append(pow(float(data[7]), 2))
                # label = float(data[8])
                # labels.append(label)
                datalist.append(ndata)
            cnt += 1
    return datalist


def writePredictData(output,fileid=1):
    # filename = "/dpdata/photovoltaic_power/data/out_%d.csv" % fileid
    filename = "E:/tcdata/photovoltaic_power/data/out_%d.csv" % fileid
    file = open(filename, 'w', encoding='utf-8')
    for i in range(output[0].__len__()):
        str = ('%d,%f\n') % (i + 1, output[0][i])
        file.write(str)
    file.close()


def composeData():
    cnt=0;
    outfile =open('e:/tcdata/photovoltaic_power/out.csv','w',encoding='utf-8')
    outfile.write('id,predicition\n')
    for i in range(4):
        filename = "e:/tcdata/photovoltaic_power/data/out_%d.csv" % (i+1)
        with open(filename,encoding='utf-8') as file:
            for line in file:
                cnt+=1
                strs=line.split(',')
                outstr=('%d,%s') % (cnt,strs[1])
                outfile.write(outstr)

    outfile.close()

def composeData2():
    cnt=0;
    outfile =open('e:/tcdata/photovoltaic_power/out.csv','w',encoding='utf-8')
    k=0
    for i in range(4):
        filename = "e:/tcdata/photovoltaic_power/out_%d.csv" % (i+1)
        with open(filename,encoding='utf-8') as file:
            for line in file:
                strs=line.split(',')
                for j in range(strs.__len__()):
                    if j==0 :
                        continue
                    outstr='%d,%s\n' % (j,strs[j])
                    outfile.write(outstr)
                    k += 1


    outfile.close()


# def runtrain():



composeData()
# getData()
# getValData()
# d=getPredictData()
# print('hi')
# writePredictData([1,2])