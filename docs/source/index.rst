.. _index_page:

SUEWS: Surface Urban Energy and Water Balance Scheme
----------------------------------------------------

.. image:: http://readthedocs.org/projects/suews-docs/badge/?version=latest
    :target: https://suews-docs.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. note::

  This documentation is being migrated from our previous wiki site to this new system.
  Also, some statements here may NOT be up to date as the model/software is under rapid development.
  Please report issues on the `GitHub page`_.

- **How to get SUEWS?**

.. epigraph::

  The software can be downloaded via `our GitHub page`_.
  The **latest formal** release of SUEWS is `new_2018a`.


- **How to use SUEWS?**

  - **For existing users:**

  .. epigraph::

    For notable changes in this version, see :ref:`new_latest`.
    If such changes have impacts on your existing simulation, please read parts related to your simulation files under influence and make necessary changes to adapt them for the new version.

    .. tip::

        A helper python script, `SUEWS table converter <input_converter>`, is provided to help facilitate the conversion of input files between different SUEWS versions.

    Additionally, the manuals for previous versions can be accessed in respective sections under `version_history`.


  - **For new users:**

  .. epigraph::

    Before starting to perform SUEWS simulations, new users are suggested to first get an overview from :ref:`introduction`, then follow the steps in `Preparing_to_run_the_model` to prepare `input files <input_files>` for SUEWS.

    Besides, it is a good starting point to learn running SUEWS via :ref:`the tutorial. <tutorials_suews>`


- **How has SUEWS been used?**

.. epigraph::

  The scientific details and application cases of SUEWS can be found in related papers under `Recent_publications`.

.. _cite_suews:

- **How to cite SUEWS?**

  Please cite `this version <new_latest>` as follows:

  .. epigraph::

    Sun T, L Järvi, M Havu, HC Ward, S Onomura, F Lindberg, F Olofson, A Gabey, CSB Grimmond (2018). SUEWS Manual V2018a. Department of Meteorology, University of Reading, Reading, UK


- **How to support SUEWS?**

  #. `Cite SUEWS <cite_suews>` appropriately in your work.
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

   introduction
   parameterisations-and-sub-models
   prepare-to-run-the-model
   input_files/input_files
   output_files/output_files
   troubleshooting
   recent-publications
   suews_related_softwares
   sub-tutorials/tutorials
   development
   version-history
   acknowledgement
   notation
   references


