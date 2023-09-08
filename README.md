# UniPlotter
A dashboard containing most of the usefull python scripts i have coded during my time in SBiNLAB.
Works utilizing DASH for the GUI and Heroku as the server host.

## CD Plotter
Allows the user to upload files from the JASCO CD spectrometer. 
Will allow either the overlaying of multiple far-UV spectras or fitting of thermodynamic parameters of a single thermo or chemical denaturanation spectrum.
Is capable of normalization to mean residue ellipticity and filtering out saturations over 600.

## ÄKTA PLOTTER
Allows for plotting of data from HPLC systems from Cytiva. 
Capable of overlaying multiple chromatograms and allows the user to filter out which data to display, such as conductivity, %B or fractions.
If multiple chromatograms are uploaded, only 280 nm will be shown.

## Flourescence plotter
Allows the PerkinElmer fluorescence Spectroscopy instruments.
Allows the fitting of one or multiple spectras.
If multiple are uploaded the user can select to display all curves at once. Additionally, the user can plot either the intensity at specific wavelength, selectable by a slider, or the wavelength with maximum intensity for all spectras.
Also allows for fitting of thermodynamic parameters.

## Mass spec plotter 
Very simple plotter which plots data from agilent mass spectrometers. Does absolutely nothing fancy, and was only developed when our mass spec computer was acting up.

## Bootstrapper
simulates error propagation of two or more biological or techinical replicates by bootstrapping to estimate an average value with takes the indiviual errors into account.

## Buffer Calculator
Work in progress :)

## Files
A dipository for the files type which the above scripts were based on. Allows user to see which formats the Uniplotter will accept


