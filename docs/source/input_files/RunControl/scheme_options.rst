.. _scheme_options:

Scheme options
~~~~~~~~~~~~~~~~~

.. option:: CBLuse

		.. warning:: |NotAvail|

	:Requirement:
		Required
	:Description:
		Determines whether a CBL slab model is used to calculate temperature and humidity.
	:Configuration:
		.. csv-table::
			:file: csv-table/CBLuse.csv
			:header-rows: 1
			:widths: 10 80


.. option:: SnowUse

	:Requirement:
		Required
	:Description:
		Determines whether the snow part of the model runs.
	:Configuration:
		.. csv-table::
			:file: csv-table/SnowUse.csv
			:header-rows: 1
			:widths: 10 80


.. option:: SOLWEIGUse

		.. warning::
			#. |NotAvail|
			#. This option will considerably slow down the model since SOLWEIG is a 2D model.

	:Requirement:
		Required
	:Description:
		Determines whether a high resolution radiation model to calculate mean radiant temperate should be used (SOLWEIG).


	:Configuration:
		.. csv-table::
			:file: csv-table/SOLWEIGUse.csv
			:header-rows: 1
			:widths: 10 80


.. option:: NetRadiationMethod

	:Requirement:
		Required
	:Description:
		Determines method for calculation of radiation fluxes.
	:Configuration:
		.. csv-table::
			:file: csv-table/NetRadiationMethod.csv
			:header-rows: 1
			:widths: 10 80


.. option:: EmissionsMethod

	:Requirement:
		Required
	:Description:
		Determines method for QF calculation.
	:Configuration:
		.. csv-table::
			:file: csv-table/EmissionsMethod.csv
			:header-rows: 1
			:widths: 10 80


.. option:: StorageHeatMethod

	:Requirement:
		Required
	:Description:
		Determines method for calculating storage heat flux ΔQS.
	:Configuration:
		.. csv-table::
			:file: csv-table/StorageHeatMethod.csv
			:header-rows: 1
			:widths: 10 80


.. option:: OHMIncQF

	:Requirement:
		Required
	:Description:
		Determines whether the storage heat flux calculation uses |Qstar| or ( |Qstar| +QF).
	:Configuration:
		.. csv-table::
			:file: csv-table/OHMIncQF.csv
			:header-rows: 1
			:widths: 10 80


.. option:: StabilityMethod

	:Requirement:
		Required
	:Description:
		Defines which atmospheric stability functions are used.
	:Configuration:
		.. csv-table::
			:file: csv-table/StabilityMethod.csv
			:header-rows: 1
			:widths: 10 80


.. option:: RoughLenHeatMethod

	:Requirement:
		Required
	:Description:
		Determines method for calculating roughness length for heat.
	:Configuration:
		.. csv-table::
			:file: csv-table/RoughLenHeatMethod.csv
			:header-rows: 1
			:widths: 10 80



.. option:: RoughLenMomMethod

	:Requirement:
		Required
	:Description:
		Determines how aerodynamic roughness length (z0m) and zero displacement height (zdm) are calculated.
	:Configuration:
		.. csv-table::
			:file: csv-table/RoughLenMomMethod.csv
			:header-rows: 1
			:widths: 10 80


.. option:: SMDMethod

	:Requirement:
		Required
	:Description:
		Determines method for calculating soil moisture deficit (SMD).
	:Configuration:
		.. csv-table::
			:file: csv-table/SMDMethod.csv
			:header-rows: 1
			:widths: 10 80


.. option:: WaterUseMethod

	:Requirement:
		Required
	:Description:
		Defines how external water use is calculated.
	:Configuration:
		.. csv-table::
			:file: csv-table/WaterUseMethod.csv
			:header-rows: 1
			:widths: 10 80
