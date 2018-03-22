**********************
Simulating a Survey
**********************

Untargeted Survey
=================

For an untargeted survey search, use the following example:

		
.. code-block:: python     
	
     from __future__ import print_function
     import surveySim
     from astropy import units as u
     

Out::
  
   Survey Name:SNLS
		Length: 2.08 Years
		Cadence: 4.0 Days
		Area: 4.0 Square Degrees
		Redshift Range: 0.1-->1.1
		-------------------
   Filter=sdss::i, Limiting Magnitude=24
		Upper Bound Ia:1530.13
		Lower Bound Ia:765.06
		Upper Bound Ic:464.07
		Lower Bound Ic:232.03
		Upper Bound Ib:464.07
		Lower Bound Ib:232.03
		Upper Bound IIP:16.51
		Lower Bound IIP:8.25

		Total Ia Upper Bound:1530.13
		Total Ia Lower Bound:765.06
		Total CC Upper Bound:944.64
		Total CC Lower Bound:472.32

		Total Lower Bound:1237.39
		Total Upper Bound:2474.77
		-------------------






Plot the Results in a Histogram
===============================
You can directly plot a specific band from the result Dictionary::
  
  snls.plotHist('sdss::i','Ia')
  

Out:

.. image:: examples/example_plot_untar.png
    :width: 600px
    :align: center
    :height: 400px
    :alt: alternate text
