#2.1
import pandas as pd

s=pd.Series([18,20,15,6,10,20,19,17,13,16,7,14,1,20,4,12,17,19,18])
print(s)

#2.2
import pandas as pd

df=pd.DataFrame([[1,'a'],[2,'b'],[3,'c']])
print(df)

#2.1.3
import pandas as pd

stdData=pd.read_csv('studentData.csv',delimiter=',')
print(stdData)

#2.1.3
import pandas as pd

stdData=pd.read_csv('studentData-noHeader.csv',delimiter=',',
                    names=['ID','Gender','CsScore','Height'])
print(stdData)

#2.3
import pandas as pd

stdData=pd.read_csv('studentData-noHeader.csv',delimiter=',',
                    names=['ID','Gender','CsScore','Height'])
print(stdData.count())

#2.4
import pandas as pd

stdData=pd.read_csv('studentData-noHeader.csv',delimiter=',',
                    names=['ID','Gender','CsScore','Height'])
print(stdData.CsScore.mean())

#2.5
import pandas as pd

stdData=pd.read_csv('studentData-noHeader.csv',delimiter=',',
                    names=['ID','Gender','CsScore','Height'])
print(stdData.groupby('Gender').mean())

#2.7
import pandas as pd

stdData=pd.read_csv('studentData.csv',delimiter=',')
sciData=pd.read_csv('sciScore.csv',delimiter=',')

newData=stdData.merge(sciData)
print(newData)

#2.8
import pandas as pd

stdData=pd.read_csv('studentData-noHeader.csv',delimiter=',',
                    names=['ID','Gender','CsScore','Height'])
sciData=pd.read_csv('sciScore.csv',delimiter=',')

newData=stdData.merge(sciData,left_on='ID',right_on='เลขประจำตัว')
print(newData)

#2.9
import pandas as pd
import matplotlib.pyplot as plt

stdData=pd.read_csv('studentData-noHeader.csv',delimiter=',',
                    names=['ID','Gender','CsScore','Height'])
sciData=pd.read_csv('sciScore.csv',delimiter=',')

newData=stdData.merge(sciData,left_on='ID',right_on='เลขประจำตัว',
                      how='inner')
print(newData)
newData.CsScore.hist(range=[0,20],bins=21)
plt.title('Computing Science Test Score Frequency')
plt.xlabel('CsScore')
plt.ylabel('Frequency')
plt.axis([0,20,0,5])
plt.xticks(range(0,21,2))
plt.show()

#2.10
import pandas as pd
import matplotlib.pyplot as plt

stdData=pd.read_csv('studentData-noHeader.csv',delimiter=','
                    ,names=['ID','Gender','CsScore','Height'])
sciData=pd.read_csv('sciScore.csv',delimiter=',')

newData=stdData.merge(sciData,left_on='ID',right_on='เลขประจำตัว',how='inner')
print(newData)

plt.scatter(newData.CsScore,newData.Science1)
plt.xlabel('Computing Science score')
plt.ylabel('Science score')
for i in range(0,20):
    plt.text(newData.CsScore[i],newData.Science1[i],newData.ID[i])
plt.title('Computing Science score & Science score relationship')
plt.show()

#กิจกรรม2.1
import pandas as pd
import matplotlib.pyplot as plt

bmidata = pd.read_csv('bmi.csv', encoding='utf-8')

bmidata['BMI'] = bmidata.apply(lambda row: round(row['น้ำหนัก'] / (row['ส่วนสูง']/100)**2), axis=1)

print(bmidata)

plt.scatter(bmidata['น้ำหนัก'], bmidata['ส่วนสูง'])
plt.xlabel('น้ำหนัก')
plt.ylabel('ส่วนสูง')
for i in range(min(180, len(bmidata))):
    plt.text(bmidata['น้ำหนัก'][i], bmidata['ส่วนสูง'][i], bmidata['BMI'][i])

plt.show()

##END##