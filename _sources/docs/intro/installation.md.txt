# Installation

[TissUUmaps](https://tissuumaps.github.io/) is a browser-based tool for fast visualization and exploration of millions of data points overlaying a tissue sample. TissUUmaps can be used as a web service or locally in your computer, and allows users to share regions of interest and local statistics.

## Windows installation

1. Download the Windows Installer from <a href="https://github.com/TissUUmaps/TissUUmaps/releases/latest" target="_blank">the last release</a> and install it. Note that the installer is not signed yet and may trigger warnings from the browser and from the firewall. You can safely pass these warnings.

## PIP installation (for Linux and Mac)

1. Install `libvips` for your system: <a href="https://www.libvips.org/install.html" target="_blank">https://www.libvips.org/install.html</a>:

    An easy way to install `libvips` is to use an <a href="https://docs.anaconda.com/anaconda/install/index.html" target="_blank">Anaconda</a> environment with `libvips`:
    ```bash
    conda create -y -n tissuumaps_env -c conda-forge python=3.9
    conda activate tissuumaps_env
    ```

1. Install dependencies using `conda`:
    ```bash
    conda install -c conda-forge libvips pyvips openslide-python
    ```

1. Install the TissUUmaps library using `pip`:
    ```bash
    pip install "TissUUmaps[full]"
    ```
    ```{note}
    If the installation fails with PyQt6, you can remove `[full]` from the previous command and run step 5 to start TissUUmaps server.
    ```

1. Start the TissUUmaps user interface:
    ```bash
    tissuumaps
    ```

1. Or start TissUUmaps as a local server:
    ```bash
    tissuumaps_server path_to_your_images
    ```
    And open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your favorite browser.
