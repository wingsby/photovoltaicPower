import time

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score


def getData(fileid=1):
    # filename = '/dpdata/photovoltaic_power/data/train_%d.csv' % fileid
    filename = 'e:/tcdata/photovoltaic_power/train_%d.csv' % fileid
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
            cnt+=1
        return datalist, labels


n_folds=10
X,y=getData(1)
model_gbr = GradientBoostingRegressor(learning_rate=0.01,n_estimators=50,criterion='mae')
scores = cross_val_score(model_gbr, X, y, cv=n_folds)
pre_y=model_gbr.fit(X, y).predict(X)
tmp_score=mean_absolute_error((y, pre_y))
print(tmp_score)


