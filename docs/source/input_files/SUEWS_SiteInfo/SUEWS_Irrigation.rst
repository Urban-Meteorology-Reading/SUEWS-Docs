.. _SUEWS_Irrigation.txt:

SUEWS_Irrigation.txt
~~~~~~~~~~~~~~~~~~~~

SUEWS includes a simple model for external water use if observed data
are not available. The model calculates daily water use from the mean
daily air temperature, number of days since rain and fraction of
irrigated area using automatic/manual irrigation. The sub-daily pattern
of water use is modelled according to the daily cycles specified in
`SUEWS_Profiles.txt`.

Alternatively, if available, the external water use can be provided in
the met forcing file (and set `WaterUseMethod` = 1 in
`RunControl.nml`), in which case all columns here
except Code should be set to :code:`-999`.



.. csv-table::
  :file: csv-table/SUEWS_Irrigation.csv
  :header-rows: 1
  :widths: 5 25 5 65


An example `SUEWS_Irrigation.txt` can be found below:

.. literalinclude:: sample-table/SUEWS_Irrigation.txt
