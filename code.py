#Dynamics of COVID-19

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

sb.set(rc = {'figure.figsize' : (9, 5)})

dataE = r'C:\Users\admin\Documents\dataCOVID-19\dataE.xlsx'
dataWPR = r'C:\Users\admin\Documents\dataCOVID-19\dataWPR.xlsx'
dataChina = r'C:\Users\admin\Documents\dataCOVID-19\dataChina.xlsx'
dataSEAR = r'C:\Users\admin\Documents\dataCOVID-19\dataS-EAR.xlsx'
dataEMR = r'C:\Users\admin\Documents\dataCOVID-19\dataEMR.xlsx'
dataAm = r'C:\Users\admin\Documents\dataCOVID-19\dataAm.xlsx'
dataAf = r'C:\Users\admin\Documents\dataCOVID-19\dataAf.xlsx'

dfE = pd.read_excel(dataE)
dfWPR = pd.read_excel(dataWPR)
dfChina = pd.read_excel(dataChina)
dfSEAR = pd.read_excel(dataSEAR)
dfEMR = pd.read_excel(dataEMR)
dfAm = pd.read_excel(dataAm)
dfAf = pd.read_excel(dataAf)

#COVID-19 European Region
plt.title('COVID-19 European Region');
plt.xticks(rotation = 45, ha = "right")

ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfE,
                 marker = 'D',
                 color = 'r')

ax.set(xlabel = 'Date', ylabel = 'Amount of infected persons for all time')
ax.set(xticks = dfE['Date'].values);
plt.show()

#COVID-19 Western Pacific Region
plt.title('COVID-19 Western Pacific Region');
plt.xticks(rotation = 45, ha = "right")

ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfWPR,
                 marker = 'D',
                 color = 'r')

ax.set(xlabel = 'Date', ylabel = 'Amount of infected persons for all time')
ax.set(xticks = dfWPR['Date'].values);
plt.show()

#COVID-19 China
plt.title('COVID-19 China');
plt.xticks(rotation = 45, ha = "right")

ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfChina,
                 marker = 'D',
                 color = 'r')

ax.set(xlabel = 'Date', ylabel = 'Amount of infected persons for all time')
ax.set(xticks = dfChina['Date'].values);
plt.show()

#COVID-19 South-East Asia Region
plt.title('COVID-19 South-East Asia Region')
plt.xticks(rotation = 45, ha = "right")

ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfSEAR,
                 marker = 'D',
                 color = 'r')

ax.set(xlabel = 'Date', ylabel = 'Amount of infected persons for all time')
ax.set(xticks = dfSEAR['Date'].values);
plt.show()

#COVID-19 Eastern Mediterranean Region
plt.title('COVID-19 Eastern Mediterranean Region')
plt.xticks(rotation = 45, ha = "right")

ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfEMR,
                 marker = 'D',
                 color = 'r')

ax.set(xlabel = 'Date', ylabel = 'Amount of infected persons for all time')
ax.set(xticks = dfEMR['Date'].values);
plt.show()

#COVID-19 Region of the Americas
plt.title('COVID-19 Region of the Americas')
plt.xticks(rotation = 45, ha = "right")

ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfAm,
                 marker = 'D',
                 color = 'r')

ax.set(xlabel = 'Date', ylabel = 'Amount of infected persons for all time')
ax.set(xticks = dfAm['Date'].values);
plt.show()

#COVID-19 African Region
plt.title('COVID-19 African Region')
plt.xticks(rotation = 45, ha = "right")

ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfAf,
                 marker = 'D',
                 color = 'r')

ax.set(xlabel = 'Date', ylabel = 'Amount of infected persons for all time')
ax.set(xticks = dfAf['Date'].values);
plt.show()

#COVID-19 Region(Confirmed)
plt.title('COVID-19 Region(Confirmed)')

plt.xticks(rotation = 45, ha = "right")

#European Region
ax = sb.lineplot(x = 'Date', y = 'Confirmed',
                 data = dfE,
                 marker = 'D',
                 color = 'r',
                 label = 'European Region')

#Western Pacific Region
ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfWPR,
                 marker = 'D',
                 color = 'b',
                 label = 'Western Pacific Region')

#South-East Asia Region
ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfSEAR,
                 marker = 'D',
                 color = 'g',
                 label = 'South-East Asia Region')

#Eastern Mediterranean Region
ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfEMR,
                 marker = 'D',
                 color = 'y',
                 label = 'Eastern Mediterranean Region')

#Region of the Americas
ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfAm,
                 marker = 'D',
                 color = 'k',
                 label = 'Region of the Americas')

#African Region
ax = sb.lineplot(x = 'Date',
                 y = 'Confirmed',
                 data = dfAf,
                 marker = 'D',
                 color = 'm',
                 label = 'African Region')

ax.set(xticks = dfE['Date'].values);
ax.set(xticks = dfWPR['Date'].values);

ax.set(xlabel = 'Date', ylabel = 'Amount of infected persons for all time')

plt.show()

#COVID-19 Region(Dead)
plt.title('COVID-19 Region(Dead)')

plt.xticks(rotation = 45, ha = "right")

#European Region
ax = sb.lineplot(x = 'Date', y = 'Dead',
                 data = dfE,
                 marker = 'D',
                 color = 'r',
                 label = 'European Region')

#Western Pacific Region
ax = sb.lineplot(x = 'Date',
                 y = 'Dead',
                 data = dfWPR,
                 marker = 'D',
                 color = 'b',
                 label = 'Western Pacific Region')

#South-East Asia Region
ax = sb.lineplot(x = 'Date',
                 y = 'Dead',
                 data = dfSEAR,
                 marker = 'D',
                 color = 'g',
                 label = 'South-East Asia Region')

#Eastern Mediterranean Region
ax = sb.lineplot(x = 'Date',
                 y = 'Dead',
                 data = dfEMR,
                 marker = 'D',
                 color = 'y',
                 label = 'Eastern Mediterranean Region')

#Region of the Americas
ax = sb.lineplot(x = 'Date',
                 y = 'Dead',
                 data = dfAm,
                 marker = 'D',
                 color = 'k',
                 label = 'Region of the Americas')

#African Region
ax = sb.lineplot(x = 'Date',
                 y = 'Dead',
                 data = dfAf,
                 marker = 'D',
                 color = 'm',
                 label = 'African Region')

ax.set(xticks = dfE['Date'].values);
ax.set(xticks = dfWPR['Date'].values);

ax.set(xlabel = 'Date', ylabel = 'Amount of infected persons for all time')

plt.show()