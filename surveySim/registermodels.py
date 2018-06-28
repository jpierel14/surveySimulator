"""
Load trimmed JWST bandpasses and extrapolated SNANA CCSN models into sncosmo,
using registry.register_loader to make them accessible for on-the-fly loading.
"""
__author__ = 'rodney'

import os
from astropy import units as u
from astropy.utils.data import get_pkg_data_filename
from sncosmo.models import _SOURCES
from sncosmo import registry
from sncosmo import Source, TimeSeriesSource, SALT2Source
from sncosmo import io
from sncosmo.bandpasses import Bandpass, read_bandpass

__dir__=os.path.abspath(os.path.dirname(__file__))

def load_timeseries_ascii_local(pkg_data_name, name=None, version=None):
    # fname = get_pkg_data_filename(pkg_data_name)
    fname = os.path.join(__dir__, pkg_data_name)
    phase, wave, flux = io.read_griddata_ascii(fname)
    return TimeSeriesSource(phase, wave, flux, name=name, version=version)

def load_salt2model_local(pkg_data_name, name=None, version=None):
    # fname = get_pkg_data_filename(pkg_data_name)
    fname = os.path.join(__dir__, pkg_data_name)
    dirname = os.path.dirname(fname)
    return SALT2Source(modeldir=dirname, name=name, version=version)

def load_bandpass(pkg_data_name, name=None):
    # fname = get_pkg_data_filename(pkg_data_name)
    fname = os.path.join(__dir__, pkg_data_name)
    return read_bandpass(fname, wave_unit=u.micron, name=name)


# --------------------------------------------------------------------------
# JWST NIRCam, total throughput, mean across A+B modules.
jwst_meta = {'filterset': 'jwst-nircam',
            'dataurl': (
                'https://jwst-docs.stsci.edu/display/JTI/NIRCam+Filters'
                'nircam'),
            'retrieved': 'Jun 2018',
            'description': 'JWST NIRCam filters, trimmed.'}
registry.register_loader(
    Bandpass, 'f070w', load_bandpass, force=True,
    args=['data/bands/jwst/jwst_nircam_f070w.dat'], meta=jwst_meta)
registry.register_loader(
    Bandpass, 'f090w', load_bandpass, force=True,
    args=['data/bands/jwst/jwst_nircam_f090w.dat'], meta=jwst_meta)
registry.register_loader(
    Bandpass, 'f115w', load_bandpass, force=True,
    args=['data/bands/jwst/jwst_nircam_f115w.dat'], meta=jwst_meta)
registry.register_loader(
    Bandpass, 'f150w', load_bandpass, force=True,
    args=['data/bands/jwst/jwst_nircam_f150w.dat'], meta=jwst_meta)
registry.register_loader(
    Bandpass, 'f200w', load_bandpass, force=True,
    args=['data/bands/jwst/jwst_nircam_f200w.dat'], meta=jwst_meta)
registry.register_loader(
    Bandpass, 'f277w', load_bandpass, force=True,
    args=['data/bands/jwst/jwst_nircam_f277w.dat'], meta=jwst_meta)
registry.register_loader(
    Bandpass, 'f356w', load_bandpass, force=True,
    args=['data/bands/jwst/jwst_nircam_f356w.dat'], meta=jwst_meta)
registry.register_loader(
    Bandpass, 'f444w', load_bandpass, force=True,
    args=['data/bands/jwst/jwst_nircam_f444w.dat'], meta=jwst_meta)

del jwst_meta


# -----------------------------------------------------------------------
#  SALT2 UV2IR
meta = {'type': 'SN Ia',
        'subclass': '`~sncosmo.SALT2Source`',
        'url': 'https://github.com/jpierel14/SNSED_Repository',
        'note': "SALT2 extrapolation from Pierel+ 2018."}
_SOURCES.register_loader(
    'salt2-uv2ir', load_salt2model_local,
    args=('data/SEDs.P18-UV2IR/salt2-extended/SALT2.INFO',),
    version='1.0', meta=meta)


# -----------------------------------------------------------------------
# Extrapolated SNANA CC SN models

ref = ('SNSEDextend', 'Pierel et al. 2018',
       '(submitted)')
website = 'https://github.com/jpierel14/SNSED_Repository'
subclass = '`~sncosmo.TimeSeriesSource`'
note = "Extrapolations of the SNANA CC SN models."
sedroot = 'data/SEDs.P18-UV2IR/'


registry.register_loader(Source,'Ic.01',load_timeseries_ascii_local,
                         args=[sedroot+'CSP-2004fe.SED'],version='1.0',
                         meta={'url':website,'snid':'CSP-2004fe','type':'Ic',
                               'subclass':subclass,'reference':ref,
                               'note':note})
registry.register_loader(Source,'Ic.02',load_timeseries_ascii_local,
                                args=[sedroot+'CSP-2004gq.SED'],version='1.0',
                                meta={'url':website,'snid':'CSP-2004gq','type':'Ic',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ic.03',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-004012.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-004012','type':'Ic',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ic.04',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-013195.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-013195','type':'Ic',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ic.05',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-014475.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-014475','type':'Ic',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ic.06',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-015475.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-015475','type':'Ic',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ic.07',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-017548.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-017548','type':'Ic',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ic.08',load_timeseries_ascii_local,
                                args=[sedroot+'SNLS-04D1la.SED'],version='1.0',
                                meta={'url':website,'snid':'SNLS-04D1la','type':'Ic',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ic.09',load_timeseries_ascii_local,
                                args=[sedroot+'SNLS-04D4jv.SED'],version='1.0',
                                meta={'url':website,'snid':'SNLS-04D4jv','type':'Ic',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})

registry.register_loader(Source,'Ib.01',load_timeseries_ascii_local,
                                args=[sedroot+'CSP-2004gv.SED'],version='1.0',
                                meta={'url':website,'snid':'CSP-2004gv','type':'Ib',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ib.02',load_timeseries_ascii_local,
                                args=[sedroot+'CSP-2006ep.SED'],version='1.0',
                                meta={'url':website,'snid':'CSP-2006ep','type':'Ib',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ib.03',load_timeseries_ascii_local,
                                args=[sedroot+'CSP-2007Y.SED'],version='1.0',
                                meta={'url':website,'snid':'CSP-2007Y','type':'Ib',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ib.04',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-000020.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-000020','type':'Ib',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ib.05',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-002744.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-002744','type':'Ib',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ib.06',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-014492.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-014492','type':'Ib',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'Ib.07',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-019323.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-019323','type':'Ib',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})


registry.register_loader(Source,'IIP.01',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-000018.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-000018','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.02',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-003818.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-003818','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.03',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-013376.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-013376','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.04',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-014450.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-014450','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.05',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-014599.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-014599','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.06',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-015031.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-015031','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.07',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-015320.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-015320','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.08',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-015339.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-015339','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.09',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-017564.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-017564','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.10',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-017862.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-017862','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.11',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018109.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018109','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.12',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018297.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018297','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.13',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018408.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018408','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.14',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018441.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018441','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.15',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018457.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018457','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.16',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018590.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018590','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.17',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018596.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018596','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.18',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018700.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018700','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.19',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018713.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018713','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.20',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018734.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018734','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.21',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018793.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018793','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.22',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018834.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018834','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIP.23',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-018892.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-018892','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})

registry.register_loader(Source,'IIL.01',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-020038.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-020038','type':'IIP',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})

registry.register_loader(Source,'IIn.01',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-012842.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-012842','type':'IIN',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})
registry.register_loader(Source,'IIn.02',load_timeseries_ascii_local,
                                args=[sedroot+'SDSS-013449.SED'],version='1.0',
                                meta={'url':website,'snid':'SDSS-013449','type':'IIN',
                                        'subclass':subclass,'reference':ref,
                                        'note':note})

