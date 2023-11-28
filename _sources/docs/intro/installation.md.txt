# Installation

[TissUUmaps](https://tissuumaps.github.io/) is a browser-based tool for fast visualization and exploration of millions of data points overlaying a tissue sample. TissUUmaps can be used as a web service or locally in your computer, and allows users to share regions of interest and local statistics.

## Windows installation

1. Download the Windows Installer (`.exe`) from <a href="https://github.com/TissUUmaps/TissUUmaps/releases/latest" target="_blank">the last release</a> and install it. Note that the installer is not signed yet and may trigger warnings from the browser and from the firewall. You can safely pass these warnings.

## MacOS installation

1. Install vips with `brew install vips` (needs homebrew installed https://brew.sh/).
1. Download the macOS installer (`.dmg`) from <a href="https://github.com/TissUUmaps/TissUUmaps/releases/latest" target="_blank">the last release</a> and install it. Download the `x86_64` file if you have an Intel CPU, or download the `arm64` file if you have an Apple Silicon (M1/M2) CPU.
1. In the installer, drag-and-drop the TissUUmaps bundle to the Applications directory.
1. When the copy is finished, double-click the Applications icon in the installer and right-click + open TissUUmaps from the Applications menu.
        - A warning should be prompted "macOS cannot verify the developer of TissUUmaps (...)", click open and the program should launch.

## Debian / Ubuntu installation

1. Download the Ubuntu installer (`.deb`) from <a href="https://github.com/TissUUmaps/TissUUmaps/releases/latest" target="_blank">the last release</a> .deb file (20.04 or 22.04 depending on your Ubuntu version)

## PIP installation

If you want specific Python packages to be installed with TissUUmaps, or if your no installer is available for your operating system, you will need to install TissUUmaps using `pip`:

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
