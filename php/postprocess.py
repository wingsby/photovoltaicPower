

def postProcess(fileid):
    filename = 'e:/tcdata/photovoltaic_power/test_%d.csv' % fileid
    outfilename='e:/tcdata/photovoltaic_power/out_%d.csv' % fileid
    noutfilename = 'e:/tcdata/photovoltaic_power/nout_%d.csv' % fileid
    noutfile=open(noutfilename, 'w',encoding='utf-8')
    with open(filename,encoding='utf-8') as file,open(outfilename,encoding='utf-8') as outfile:
        tmp=file.readline()
        cnt=0
        for line,outline in zip(file,outfile):
            cnt+=1
            strs=line.split(",")
            if(float(strs[2])==-1):
                outstr='%d,%s\n' % (cnt,-0.022)
                noutfile.write(outstr)
            else:
                noutfile.write(outline)

    noutfile.close()

postProcess(1)
