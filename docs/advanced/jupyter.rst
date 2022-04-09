******************
Jupyter notebooks
******************

TissUUmaps can easily be used inside a Jupyter Notebook or Jupyter Lab.

Simple example to load an image in TissUUmaps::

   import tissuumaps.jupyter as tj
   viewer = tj.loaddata(["image.png"])

   viewer.screenshot()

.. automodule:: tissuumaps.jupyter
   :members: