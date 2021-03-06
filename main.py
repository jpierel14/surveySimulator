import surveySim,sys,os
import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt
from astropy.io import ascii
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

slacs=surveySim.survey(name='SLACS',snTypes=['Ia','Ib','Ic','IIP'])
slacs.cadence=3*u.day
slacs.magLimits=[24.7]
slacs.filters=['sdss::r']
slacs.surveyLength=1*u.year
slacs.galaxies=surveySim.load_example_data()
slacs.targetedSurvey(zpsys='ab')
print(slacs)
slacs.plotHist('sdss::r','Ia',savePlot=True,showPlot=False)

snls=surveySim.survey(name='SNLS',snTypes=['Ia','Ib','Ic','IIP'],zmin=.1,zmax=1.1,dz=.05)
snls.area=4*u.deg**2
snls.cadence=4*u.day
snls.magLimits=[24]
snls.filters=['sdss::i']
snls.surveyLength=2.08*u.year
snls.unTargetedSurvey(zpsys='vega')
print(snls)
snls.plotHist('sdss::i','Ia',savePlot=True,showPlot=False)#,showPlot=False,savePlot=True)
#surveySim.plotHist(snYield['sdss::i'])
'''


'''
for snClass in snYield.keys():
    surveySim.plotHist(snYield,snClass,magLimit,mu,zmin,zmax,dz,bound='lower')
    surveySim.plotHist(snYield,snClass,magLimit,mu,zmin,zmax,dz,bound='upper')


liverpool=surveySim.survey(name='Liverpool',snTypes=['Ia','Ib','Ic','IIP','IIn','IIL','IIb'])
liverpool.magLimits=[23.5]
liverpool.cadence=10*u.day
liverpool.filters=['sdss::r']
liverpool.surveyLength=1*u.year
liverpool.mu=5
liverpool.galaxies=ascii.read(os.path.join('surveySim','data','examples','liverpool.dat'))
liverpool.targetedSurvey(zpsys='ab',Ia_av=.3,CC_av=.49)
liverpool.verbose=True
print(liverpool)

from scipy.stats import poisson
from scipy.integrate import quad
maglim = 26.5
if True:
    glsnst = surveySim.survey(name='GLSNST',snTypes=['Ia','Ib','Ic','IIP','IIn','IIb','IIL'])
    glsnst.cadence= 20 * u.day
    glsnst.filters=['F160W']
    glsnst.surveyLength= 0.33 * u.year # not used, b/c tobs is defined in the input data file
    glsnst.galaxies = ascii.read('../glsnst/glsnst_sample_2018B+2019A.dat',format='commented_header', header_start=-1, data_start=0)
    glsnst.magLimits=[maglim]
    glsnst.targetedSurvey(zpsys='ab',Ia_av=.3,CC_av=.49,lc_sampling=200)
    glsnst.verbose = True
    print(glsnst)
    #integral of poisson distribution mean .7 integral from 1 upwards
'''   

maglims = [21.9,22.2,22.5]
for maglim in maglims:
    lco = surveySim.survey(name='LCO',snTypes=['Ia','Ib','Ic','IIP','IIn','IIb','IIL'])
    lco.zp=21.
    lco.cadence= 14. * u.day
    lco.mu=20.
    lco.filters=['sdss::r']
    lco.surveyLength= 1 * u.year # not used, b/c tobs is defined in the input data file
    lco.galaxies = ascii.read('../lco/detectability_sdssr_219_15.txt',format='commented_header', header_start=-1, data_start=0)
    lco.galaxies['nia_err']=0
    lco.galaxies['ncc_err']=0
    lco.galaxies['tobs']=.5
    lco.galaxies.sort('z')
    #lco.galaxies=lco.galaxies[:100]
    lco.magLimits=[maglim]
    lco.targetedSurvey(zpsys='ab',Ia_av=.3286,CC_av=.3286,lc_sampling=50)
    lco.verbose = True
    print(lco)
    #integral of poisson distribution mean .7 integral from 1 upwards




