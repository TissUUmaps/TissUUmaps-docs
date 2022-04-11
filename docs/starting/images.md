# Images

## Supported image formats

TissUUmaps can read whole slide images in any format recognized by the <a href="https://openslide.org/api/python/#openslide-python" target="_blank">OpenSlide library</a>:
 * Aperio (.svs, .tif)
 * Hamamatsu (.ndpi, .vms, .vmu)
 * Leica (.scn)
 * MIRAX (.mrxs)
 * Philips (.tiff)
 * Sakura (.svslide)
 * Trestle (.tif)
 * Ventana (.bif, .tif)
 * Generic tiled TIFF (.tif)

TissUUmaps will automatically convert any other format into a pyramidal tiff (in a temporary `.tissuumaps` folder created in the original image folder) using <a href="https://github.com/libvips/libvips" target="_blank">vips</a>.

If your image fails to open, try converting it to `tif` format using an external tool.


## Load images

<!-- 
You can show how to open image by drag and dropping from File Explorer to TissUUmaps, or through the image menu
-->

## Apply filters

