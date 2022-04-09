# Images

## Supported image formats

TissUUmaps can read whole slide images in any format recognized by the [OpenSlide library](https://openslide.org/api/python/#openslide-python):
 * Aperio (.svs, .tif)
 * Hamamatsu (.ndpi, .vms, .vmu)
 * Leica (.scn)
 * MIRAX (.mrxs)
 * Philips (.tiff)
 * Sakura (.svslide)
 * Trestle (.tif)
 * Ventana (.bif, .tif)
 * Generic tiled TIFF (.tif)

TissUUmaps will automatically convert any other format into a pyramidal tiff (in a temporary `.tissuumaps` folder created in the original image folder) using [vips](https://github.com/libvips/libvips).

If your image fails to open, try converting it to `tif` format using an external tool.


## Load images

