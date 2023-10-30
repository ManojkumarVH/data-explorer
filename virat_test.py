import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
virat_test = pd.read_csv(r'C:\Users\manoj\PycharmProjects\data\kohli-centuries-test.csv')
print(virat_test.head())
virat_test = virat_test.drop(columns=['Unnamed: 7'])
print(virat_test.isnull().sum())
virat_test['Year'] = pd.DatetimeIndex(virat_test['Start Date']).year
print(virat_test.columns)
# PREPROCESSING
virat_test['Opposition'] = virat_test['Opposition'].str.replace('v ', ' ')
virat_test['Bat1'] = virat_test['Bat1'].str.replace('DNB', '0')
virat_test['Bat1'] = virat_test['Bat1'].str.replace('TDNB', '0')
virat_test['Bat1'] = virat_test['Bat1'].str.replace('T0', '0')
virat_test['Bat1'] = virat_test['Bat1'].str.replace('*', ' ')
virat_test['Bat2'] = virat_test['Bat2'].str.replace('DNB', '0')
virat_test['Bat2'] = virat_test['Bat2'].str.replace('TDNB', '0')
virat_test['Bat2'] = virat_test['Bat2'].str.replace('*', ' ')
virat_test['Bat2'] = virat_test['Bat2'].str.replace('-', '0')
virat_test['Bat1'] = pd.to_numeric(virat_test['Bat1'])
virat_test['Bat2'] = pd.to_numeric(virat_test['Bat2'])
virat_test['Runs'] = virat_test['Runs'].str.replace('-', '0')
virat_test['Runs'] = pd.to_numeric(virat_test['Runs'])
virat_test['Wkts'] = virat_test['Wkts'].str.replace('-', '0')
virat_test['Wkts'] = pd.to_numeric(virat_test['Wkts'])
virat_test['Conc'] = virat_test['Conc'].str.replace('-', '0')
virat_test['Conc'] = pd.to_numeric(virat_test['Conc'])


# NO OF DUCKS IN TEST CAREER
duck = ((virat_test['Bat1'] == 0) | (virat_test['Bat2'] == 0)).sum()
print('no of ducks is ', duck)
inn1 = virat_test['Bat1'].sum()
inn2 = virat_test['Bat2'].sum()
run = virat_test['Runs'].sum()
totalruns = inn2 + inn1
print(totalruns)
if run == totalruns:
    print(True)
# VISUALISATION
slices = [(virat_test['Bat1'] == 0).sum(), (virat_test['Bat2'] == 0).sum()]
labels = ['2nd innings', '1st innings']
plt.pie(slices, labels=labels, autopct='%1.0f%%', pctdistance=5, labeldistance=1.2, shadow=True)
fig = plt.get
plt.title('total runs percentage scored in 1st inn and 2nd inn ', pad=5)
sns.set(style='whitegrid')
sns.countplot(y=virat_test['Opposition'])
sns.countplot(y=virat_test['Year'])
plt.title('No of times played with other teams')
plt.figure(figsize=(20,16))
plt.grid(True, linestyle='--')
# Runs scored in diff venue
fig1 = plt.figure(figsize=(16, 8))
fig1.add_subplot(221)
virat_test.groupby('Ground')['Runs'].sum().plot(kind='bar', title='runs scored in different venue')
virat_test.groupby('Opposition')['Runs'].sum().plot(kind='bar', title='runs scored against each teams')
# double century scored against each team
# century scored against each team
inn4 = virat_test['Bat1'] >= 100
# double century scored against each team
inn3 = virat_test['Bat1'] >= 200
data1 = virat_test[inn4]
data2 = virat_test[inn3]
fig2 = plt.figure(figsize=(16, 8))
fig2.add_subplot(221)
data1.groupby('Opposition')['Bat1'].count().plot(kind='bar', title='hundred')
data2.groupby('Opposition')['Bat1'].count().plot(kind='bar', title='hundred')


plt.show()
