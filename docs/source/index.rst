.. _index_page:

SUEWS: Surface Urban Energy and Water Balance Scheme
----------------------------------------------------

.. note::

  This documentation is being migrated from our previous wiki site to this new system.
  Also, some statement here may NOT be up to date as the model/software is under rapid development.
  Please report issues on the `GitHub page`_.

- **How to get SUEWS?**

.. epigraph::

  The software can be downloaded via `our GitHub page`_.
  The **latest formal** release of SUEWS is `v2018a <new_2018a>` (released 1 August 2017).


- **How to use SUEWS?**

  - **For existing users:**

  .. epigraph::

    For notable changes in this version, see :ref:`new_latest`.
    If such changes have impacts on your exisitng simulation, please read parts related to your simulation files under influence and make necessary changes to adapt them for the new version.

    .. tip::

        A helper python script, `SUEWS table converter <input_converter>`, is provided to help facilitate the conversions of input files between different versions.

    Besides, the manuals for previous versions can be accessed in respective sections under `version_history`.


  - **For new users:**

  .. epigraph::

    Before starting to perform SUEWS simulations, new users are suggested to first get an overview from :ref:`introduction`, then follow the steps in `Preparing_to_run_the_model` to prepare `input files <input_files>` for SUEWS.

    Besides, it is a good starting point to learn running SUEWS via `the tutorial. <http://umep-docs.readthedocs.io/en/latest/Tutorials/IntroductionToSuews.html#urban-energy-balance-suews-introduction>`_


- **How to understand SUEWS?**

.. epigraph::

  The scientific details and application cases of SUEWS can be found in model description papers under `Recent_publications`.


- **How to cite SUEWS?**

  Please cite `this version <new_latest>` as follows:

  .. epigraph::

    Sun T, L Järvi, M Havu, HC Ward, S Onomura, F Lindberg, F Olofson, A Gabey, CSB Grimmond (2018). SUEWS Manual V2018a. Department of Meteorology, University of Reading, Reading, UK


- **How to support SUEWS?**

  #. Contribute to the `development <Development_Suggestions_Support>`.
  #. Report issues via the `GitHub page`_.
  #. Provide `suggestions and feedbacks <Development_Suggestions_Support>`.


.. _our GitHub page: https://urban-meteorology-reading.github.io/SUEWS
.. _this form: `dowload form`_
.. _dowload form: http://micromet.reading.ac.uk/software/
.. _GitHub page: https://github.com/Urban-Meteorology-Reading/SUEWS-Docs/issues



.. toctree::
   :maxdepth: 2
   :numbered:
   :hidden:

   recent-publications
   introduction
   suews-and-umep
   parameterisations-and-sub-models
   prepare-to-run-the-model
   input_files/input_files
   output_files/output_files
   troubleshooting
   acknowledgement
   notation
   development
   version-history
   differences-suews-lumps-fraise
   references
