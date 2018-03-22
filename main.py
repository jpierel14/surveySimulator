import surveySim,sys
import numpy as np
from astropy import units as u

'''
sn=dict([])

with open('test.txt') as f:
    next(f)
    for line in f:
        line=line.split()
        for x in line:
            if x[:2]=='SN' and len(x)==4 and x[2]=='I':
                if x in sn.keys():
                    sn[x]+=1
                else:
                    sn[x]=1

print('SDSS')
print(sn)

magLimit=21.9
mu=1
dz=.01
zmin=.09
zmax=.5
snYield=surveySim.unTargetedSurvey(300,5,['sdss::i'],[magLimit],t_obs=1.1,mu=mu,dz=dz,zmin=zmin,zmax=zmax)
allSne_lower=[]
allSne_upper=[]
allCC_lower=[]
allCC_upper=[]
for key in snYield.keys():
    print('Upper Bound '+key+':'+str(np.sum(snYield[key]['upper'])))
    print('Lower Bound '+key+':'+str(np.sum(snYield[key]['lower'])))
    allSne_lower.append(np.sum(snYield[key]['lower']))
    allSne_upper.append(np.sum(snYield[key]['upper']))
    if key!='Ia':
        allCC_upper.append(np.sum(snYield[key]['upper']))
        allCC_lower.append(np.sum(snYield[key]['lower']))
print
print('Total Ia Upper Bound:'+str(np.sum(snYield['Ia']['upper'])))
print('Total Ia Lower Bound:'+str(np.sum(snYield['Ia']['lower'])))
print('Total CC Upper Bound:'+str(np.sum(allCC_upper)))
print('Total CC Lower Bound:'+str(np.sum(allCC_lower)))
print
print('Total Lower Bound:',str(np.sum(allSne_lower)))
print('Total Upper Bound:',str(np.sum(allSne_upper)))

print('Rodney Test:')
magLimit=24.7
mu=1
dz=.02
zmin=.01
zmax=1.61
snYield=surveySim.unTargetedSurvey(2.29*u.deg**2,5,['sdss::i'],[magLimit],zpsys='vega',t_obs=1,mu=mu,dz=dz,zmin=zmin,zmax=zmax)
allSne_lower=[]
allSne_upper=[]
allCC_lower=[]
allCC_upper=[]
for key in snYield.keys():
    print('Upper Bound '+key+':'+str(np.sum(snYield[key]['upper'])))
    print('Lower Bound '+key+':'+str(np.sum(snYield[key]['lower'])))
    allSne_lower.append(np.sum(snYield[key]['lower']))
    allSne_upper.append(np.sum(snYield[key]['upper']))
    if key!='Ia':
        allCC_upper.append(np.sum(snYield[key]['upper']))
        allCC_lower.append(np.sum(snYield[key]['lower']))
print
print('Total Ia Upper Bound:'+str(np.sum(snYield['Ia']['upper'])))
print('Total Ia Lower Bound:'+str(np.sum(snYield['Ia']['lower'])))
print('Total CC Upper Bound:'+str(np.sum(allCC_upper)))
print('Total CC Lower Bound:'+str(np.sum(allCC_lower)))
print
print('Total Lower Bound:',str(np.sum(allSne_lower)))
print('Total Upper Bound:',str(np.sum(allSne_upper)))
'''
print('SNLS:')
magLimit=24
mu=1
dz=.02
zmin=.05
zmax=1.1
snYield=surveySim.unTargetedSurvey(4*u.deg**2,4,['sdss::i'],[magLimit],zpsys='vega',t_obs=2.08,mu=mu,dz=dz,zmin=zmin,zmax=zmax)
allSne_lower=[]
allSne_upper=[]
allCC_lower=[]
allCC_upper=[]
for key in snYield.keys():
    print('Upper Bound '+key+':'+str(np.sum(snYield[key]['upper'])))
    print('Lower Bound '+key+':'+str(np.sum(snYield[key]['lower'])))
    allSne_lower.append(np.sum(snYield[key]['lower']))
    allSne_upper.append(np.sum(snYield[key]['upper']))
    if key!='Ia':
        allCC_upper.append(np.sum(snYield[key]['upper']))
        allCC_lower.append(np.sum(snYield[key]['lower']))
print
print('Total Ia Upper Bound:'+str(np.sum(snYield['Ia']['upper'])))
print('Total Ia Lower Bound:'+str(np.sum(snYield['Ia']['lower'])))
print('Total CC Upper Bound:'+str(np.sum(allCC_upper)))
print('Total CC Lower Bound:'+str(np.sum(allCC_lower)))
print
print('Total Lower Bound:',str(np.sum(allSne_lower)))
print('Total Upper Bound:',str(np.sum(allSne_upper)))




'''
for snClass in snYield.keys():
    surveySim.plotHist(snYield,snClass,magLimit,mu,zmin,zmax,dz,bound='lower')
    surveySim.plotHist(snYield,snClass,magLimit,mu,zmin,zmax,dz,bound='upper')
'''
