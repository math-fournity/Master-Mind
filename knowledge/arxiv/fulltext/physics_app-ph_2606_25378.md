# Wide-field NV magnetometry under simultaneous high-pressure and high-temperature conditions

**arXiv ID**: 2606.25378v2
**Authors**: Masahiro Ohkuma, Eikichi Kimura, Shumpei Ohyama, Miu Tezuka, Ryo Matsumoto, Shinobu Onoda, Yoshihiko Takano, Shintaro Azuma, Kenji Ohta, Keigo Arai
**Published**: 2026-06-24
**Categories**: physics.app-ph, cond-mat.mtrl-sci, quant-ph
**HTML URL**: https://arxiv.org/html/2606.25378v2

## Abstract

We demonstrate wide-field optically detected magnetic resonance (ODMR) under simultaneous high-pressure and high-temperature conditions using nitrogen-vacancy (NV) centers. Although NV-center magnetometry has been widely used for spatially resolved magnetic-field imaging, its application to extreme environments combining pressure and temperature remains challenging. In this work, we show that ODMR can be observed at 5 GPa and 500 K, demonstrating the feasibility of NV spin readout under such combined extreme conditions. We further perform wide-field ODMR of iron at 7 GPa and 500 K, where the stray magnetic field from the sample is spatially visualized through the pressure cell. These results establish NV-center magnetometry as a promising platform for imaging magnetic phenomena in materials under high-pressure and high-temperature environments.

## Full Text

Wide-field NV magnetometry under simultaneous high-pressure and high-temperature conditions

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- 
- License: CC BY 4.0arXiv:2606.25378v2 [physics.app-ph] 30 Jun 2026

## Wide-field NV magnetometry under simultaneous high-pressure and high-temperature conditionsMasahiro Ohkuma1okuma.m.408d@m.isct.ac.jpEikichi Kimura1Shumpei Ohyama1Miu Tezuka2Ryo Matsumoto3Shinobu Onoda4Yoshihiko Takano3Shintaro Azuma2Kenji Ohta2k-ohta@eps.sci.isct.ac.jpKeigo Arai1arai.k.835f@m.isct.ac.jp1School of Engineering, Institute of Science Tokyo, Yokohama 226-8501, Kanagawa, Japan2Department of Earth and Planetary Sciences, Institute of Science Tokyo, Meguro 152-8551, Tokyo, Japan3Research Center for Materials Nanoarchitectonics (MANA), National Institute for Materials Science, Tsukuba 305-0047, Ibaraki, Japan4National Institutes for Quantum Science and Technology (QST), Takasaki 370-1292, Gunma, Japan

## Abstract

We demonstrate wide-field optically detected magnetic resonance (ODMR) under simultaneous high-pressure and high-temperature conditions using nitrogen-vacancy (NV) centers.
Although NV-center magnetometry has been widely used for spatially resolved magnetic-field imaging, its application to extreme environments combining pressure and temperature remains challenging.
In this work, we show that ODMR can be observed at 5 GPa and 500 K, demonstrating the feasibility of NV spin readout under such combined extreme conditions.
We further perform wide-field ODMR of iron at 7 GPa and 500 K, where the stray magnetic field from the sample is spatially visualized through the pressure cell.
These results establish NV-center magnetometry as a promising platform for imaging magnetic phenomena in materials under high-pressure and high-temperature environments.

## IIntroduction

High pressure and high temperature are fundamental thermodynamic variables for controlling the structural, electronic, and magnetic states of materials and have also been widely used to synthesize functional materials that are inaccessible under ambient conditions[1,2,3,4].
In high-pressure experiments using diamond anvil cell (DAC), simultaneous high-pressure and high-temperature conditions are commonly achieved by combining the DAC with heating techniques such as external resistive heating, internal resistive heating, or laser heating[5,6,7].
These developments have enabled a wide range of in situ structural, spectroscopic, and electrical transport measurements under high-pressure and high-temperature conditions[8,9,10,11,12].
Such measurements provide essential information for understanding phase transitions, magnetic ordering, and functional properties in condensed-matter physics, materials science, and geoscience.

Magnetic measurements under simultaneous high-pressure and high-temperature conditions are still challenging.
Mössbauer spectroscopy and X-ray magnetic circular dichroism (XMCD) have been used to investigate the magnetic properties under high pressure and high temperature[13,14,15,16,17].
These techniques provide information on hyperfine interactions and element-specific magnetic moments.
However, Mössbauer spectroscopy is restricted to suitable Mössbauer-active nuclei, whereas XMCD can be constrained in high-pressure experiments by the accessible X-ray absorption edges and X-ray transmission through the diamond anvils[18,19,20].
In contrast, magnetometry using commercial magnetometor based superconducting quantum interference device (SQUID) systems is a standard and versatile approach for magnetic characterization, however, widely used systems in their standard configuration typically operate only up to approximately 400 K[21].
Moreover, magnetic measurements under high pressure are further constrained by the small sample volume in the pressure chamber and the background signals from the pressure cell[21].
Therefore, a broadly applicable technique for probing local magnetic fields under simultaneous high-pressure and high-temperature conditions is desirable.Figure 1:Experimental configurations for ODMR measurements under high pressure.
(a) Energy-level diagram of NV center.
(b) Optical image of the diamond anvil with boron-doped diamond antenna.
(c) Schematic of the DAC setup for ODMR measurements using (100)-oriented diamond anvil.
(d) Schematic of the DAC setup for wide-field ODMR measurements using (111)-oriented diamond anvil.

The negatively charged nitrogen-vacancy (NV) center in diamond offers a promising route to local magnetic sensing under extreme conditions.
It is a point defect that has enabled versatile applications in quantum information processing and sensing[22,23,24,25,26,27,28,29,30,31,32,33,34].
The NV center has a spin-triplet ground state that can be initialized and read out optically through spin-dependent fluorescence and exhibits magnetic resonance transitions at a zero-field splitting (DD) of approximately 2.87 GHz under ambient conditions, as shown in Fig.1a[35].
Detection of these magnetic resonance through changes in the fluorescence intensity is known as optically detected magnetic resonance (ODMR).
The energy levels of the state are highly sensitive to external perturbations, such as temperature, magnetic fields, and pressure, thereby enabling nanoscale sensing of these physical quantities[27,28,29,30,31,32,33,34,36,37].
The zero-field splittingDDincreases under hydrostatic pressure with a pressure coefficient of approximately 14 MHz/GPa, whereas it decreases with increasing temperature at a rate of approximately−74-74kHz/K near room temperature[31,36,38].
In contrast, a magnetic fieldBBapplied along the NV axis lifts the degeneracy of thems=±1m_{s}=\pm 1states through the Zeeman effect, shifting the resonance frequencies by approximately±γe​B∥\pm\gamma_{\mathrm{e}}B_{\parallel}, where gyromagnetic ratioγe≈28\gamma_{\mathrm{e}}\approx 28MHz/mT.
Therefore, the frequency separation between the two ODMR resonances is approximately2​γe​B∥2\gamma_{\mathrm{e}}B_{\parallel}.
The NV center retains its spin coherence even under temperatures up to 1400 K[39,40,41]or pressure above 100 GPa[42,43,44,45,46].
Although high-pressure or high-temperature NV-magnetometry have been demonstrated separately, NV-based magnetic imaging under simultaneous high-pressure and high-temperature conditions remains largely unexplored.

In this study, we demonstrate wide-field ODMR simultaneous high-pressure and high-temperature conditions.
Using local resistive heating with a patterned boron-doped diamond heater, we observe ODMR signals from NV centers at 5 GPa and 500 K, confirming that NV spin readout can be maintained in this environment.
We further perform magnetic imaging of iron under 7 GPa and 500 K, and visualize the stray magnetic field from the sample.
These results extend NV-magnetometry to spatially resolved magnetic imaging across pressure–temperature phase space.

## IIMethods

Pressure was applied using a CuBe diamond anvil cell.
We used type-Ib single-crystal diamond anvils with (100)- and (111)-oriented culet surfaces (Syntek Co., Ltd.).
The (100)-oriented diamond anvil was used for ODMR measurements, whereas the (111)-oriented diamond anvil was used for wide-field ODMR of iron.
The culet diameter of both diamond anvils was 300μ\mum.
For the creation of NV centers, vacancies were introduced byC+12{}^{12}\mathrm{C}^{+}ion implantation at an energy of 30 keV with a fluence of5×10125\times 10^{12}cm-2.
The diamond anvils were then annealed under vacuum at1000°C1000\text{\,}\mathrm{\SIUnitSymbolCelsius}for 2 h.
Stopping and Range of Ions in Matter simulations indicate that the implanted vacancies are distributed within approximately 50 nm from the diamond surface[47].

To heat the sample space, we employed a boron-doped diamond (BDD) heater[48,49,50,51].
For the (100)-oriented diamond-anvil experiment, the BDD heater was fabricated on the NV-containing diamond anvil.
For the (111)-oriented diamond-anvil experiment, the BDD heater was fabricated on the opposing type-IIa diamond anvil.
Microwave excitation was delivered using a BDD antenna patterned on the culet surface for the (100)-oriented diamond-anvil experiment, whereas a Pt foil was used for microwave delivery in the (111)-oriented diamond-anvil experiment.
BDD circuits were fabricated after the formation of NV centers.
An optical image of the (100)-oriented diamond anvil is shown in Fig.1b.

A rhenium gasket was pre-indented and drilled to form a hole with a diameter of 100 or 250μ\mum.
For the (100)-oriented diamond-anvil experiment, MgO was used to electrically insulate the BDD antenna from the metallic gasket.
For the (111)-oriented diamond-anvil experiment, a cBN–epoxy insulating layer was compressed, and a 100-μ\mum-diameter hole was subsequently drilled.
KCl was used as the pressure-transmitting medium.
In the wide-dield ODMR experiment using the (111)-oriented diamond anvil, an iron foil was loaded into the sample chamber.
The temperature was monitored using a K-type thermocouple attached to the slope of the NV-containing diamond anvil with cement.
The diamond anvil was mounted on a zirconia seat and fixed with cement.
For the (100)-oriented diamond-anvil experiment, the pressure was estimated from ruby fluorescence[52].
For the (111)-oriented diamond-anvil experiment, the pressure was estimated from resonance frequency of [111]-oriented NV center[53].
An overview of the experimental setups is illustrated in Figs.1c and1d, where Fig.1c shows the setup for ODMR measurements and Fig.1d shows the setup for wide-field ODMR.

Continuous-wave (CW) ODMR measurements were performed using a custom-built microscope.
A 532-nm green laser (MLL-S-532B, CNI laser or Verdi 2G, Coherent) was used to excite the NV centers through an objective lens (M-PLAN APO SL 20X, Mitutoyo).
The red fluorescence from the NV centers was collected through the same objective lens and passed through a long-pass filter.
For point-detection ODMR measurements, the fluorescence was detected by an avalanche photodiode (APD130A2, Thorlabs) coupled to a data acquisition device (USB-6363, National Instruments).
For wide-field ODMR imaging, the fluorescence was detected by an EMCCD camera (iXon Ultra 897, Andor).
Microwaves were generated using a signal generator (N5171B, Keysight, or SynthHD, Windfreak) and amplified using a power amplifier (ZHL-50W-63++or ZHL-16W-43++, Mini-Circuits).
A point-detection ODMR spectrum was acquired within 2 min, whereas a wide-field ODMR spectrum was acquired within 15 min.

## IIIResults

To verify the reliability of the temperature measured using the thermocouple attached to the slope of the diamond anvil, we measured the temperature dependence of the ODMR spectra and the ruby fluorescence spectra at ambient pressure.
Figures2a and2b show the ODMR spectra measured at different temperature and the corresponding temperature dependence of the zero-field splittingDD, respectively.
Here,DDis plotted as a function of temperatureTTrelative to its value at 300 K,Δ​D=D​(T)−D​(300​K)\Delta D=D(T)-D(300~\mathrm{K}).
The relatively low apparent ODMR contrast in this measurement may be due to the non-optimized optical collection conditions, which allowed part of the ruby fluorescence to be collected together with the NV fluorescence.
The measured temperature dependence ofΔ​D\Delta Dis in reasonable agreement with the previous report[39].
Figures2c and2d show the ruby fluorescence spectra measured at different temperatures and the corresponding temperature dependence of the R1 fluorescence line wavelength, respectively.
The R1 line shift is plotted relative to its value at 300 K,Δ​λ=λ​(T)−λ​(300​K)\Delta\lambda=\lambda(T)-\lambda(300~\mathrm{K}).
The observed temperature dependence is also consistent with previous study.
These results confirm that the thermocouple attached to the diamond anvil provides a reliable measure of the temperature in the sample chamber.Figure 2:(a) CW-ODMR spectra of NV centers measured at different temperatures.
The ODMR spectra are vertically offset by 0.04 for clarity.
(b) Temperature dependence of the zero-field splitting shift,Δ​D=D​(T)−D​(300​K)\Delta D=D(T)-D(300~\mathrm{K}).
The solid line represents the reported temperature dependence of zero-field splitting shift from Ref.[39].
The measured shift is in reasonable agreement with the reported temperature dependence.
(c) Ruby fluorescence spectra measured at different temperatures.
(d) Temperature dependence of the R1-line wavelength shift,Δ​λ=λ​(T)−λ​(300​K)\Delta\lambda=\lambda(T)-\lambda(300~\mathrm{K}).
The solid line represents the reported temperature dependence of R1-line wavelength shift from Ref.[52].
The agreement of both the NV and ruby temperature dependences confirms that the thermocouple attached to the diamond anvil provides a reliable measure of the temperature in the present experimental configuration.

The results obtained under applied pressure are summarized in Fig.3.
Figure3a shows the ODMR spectra measured at an initial ruby pressure of 5.3 GPa before heating.
Clear magnetic resonance signals were observed even above 500 K, demonstrating that ODMR readout is possible under simultaneous high-pressure and high-temperature conditions.
Figure3b shows the temperature dependence ofDD.
The dashed line represents a temperature-only reference curve calculated from the polynomial temperature dependence reported by Toylie​t​a​l.et~al.[39], with the curve offset to match the measured value ofDDat 300 K.
The temperature dependence ofDDunder pressure qualitatively follows the trend expected from the thermal shift.
However, the measuredDDvalues remain higher than those expected from the temperature-induced shift alone.
This deviation suggests that change in pressure also contributes to the observed resonance shift during heating.
Ruby fluorescence measurements performed after the temperature-dependent ODMR measurements indicated that the pressure had increased from 5.3 to 6.1 GPa.
After cooling back to room temperature, however,DDreturned to nearly the same value as that before heating, whereas ruby fluorescence indicated an increase in pressure after the heating cycle.
This discrepancy is likely due to the difference in the local pressure and stress environments probed by the NV centers and the ruby particle.
The NV centers are located within approximately 50 nm of the diamond anvil surface, whereas the ruby particle is placed in the sample chamber.

Figure3c shows the ODMR spectra measured at an initial ruby pressure of 12.0 GPa before heating.
Magnetic resonance signals were observed up to 426 K, confirming that ODMR readout remains possible even at higher pressure.
Figure3d shows the temperature dependence ofDD.
Up to approximately 400 K, the temperature dependence ofDDfollows the trend expected from the thermal shift.
At 426 K, however,DDdecreases abruptly.
This abrupt decrease is consistent with a pressure decrease during heating, as supported by ruby fluorescence measurements after the temperature-dependent ODMR measurements, which showed that the pressure had decreased from 12.0 to 10.4 GPa.
These results demonstrate that ODMR can be observed under simultaneous high-pressure and high-temperature conditions.
At the same time, they indicate that accurate in situ pressure calibration at elevated temperature is required to quantitatively determine the pressure–temperature dependence of theDD.Figure 3:ODMR measurements under simultaneous high-pressure and high-temperature conditions.
(a) CW-ODMR spectra of NV centers measured at different temperatures at an initial pressure of 5.3 GPa before heating.
Magnetic resonance signals were observed even above 500 K.
(b) Temperature dependence of the zero-field splitting parameterDDfor the data shown in (a).
The dashed line represents a temperature-only reference curve calculated from the polynomial temperature dependence ofDDreported by Toyli et al.[39], after shifting the curve to match the experimentally measured value ofDDat 300 K.
(c) CW-ODMR spectra of NV centers measured at different temperatures at an initial pressure of 12.0 GPa before heating.
Magnetic resonance signals were observed up to 426 K.
(d) Temperature dependence ofDDfor the data shown in (c).
The dashed line represents the temperature-only reference curve obtained in the same manner as in (b).
The ODMR spectra are vertically offset by 0.05 for clarity.

Next, we performed wide-field ODMR measurements under simultaneous high-pressure and high-temperature conditions.
Before discussing the wide-field ODMR results, we describe how the pressure was estimated in the wide-field ODMR experiment.
The pressure was estimated from the temperature-corrected shift ofDDin the (111)-oriented diamond anvil[53].
For simplicity, we assumed that the temperature- and pressure-induced shifts ofDDcan be treated independently.
The temperature-induced shift from 300 K, denoted asΔ​DT​(T)=Dref​(T)−Dref​(300​K)\Delta D_{T}(T)=D_{\mathrm{ref}}(T)-D_{\mathrm{ref}}(300~\mathrm{K}), was calculated from the reported temperature dependence ofDDat ambient pressure[39].
The pressure was then estimated asPODMR​(T)=Dmeas−Δ​DT​(T)−D0κ,P_{\mathrm{ODMR}}(T)=\frac{D_{\mathrm{meas}}-\Delta D_{T}(T)-D_{0}}{\kappa},(1)

whereDmeasD_{\mathrm{meas}}is the measured zero-field splitting,D0=2.87​GHzD_{0}=2.87~\mathrm{GHz}is the zero-field splitting at 300 K and ambient pressure, andκ=7.94​MHz/GPa\kappa=7.94~\mathrm{MHz/GPa}is the pressure coefficient for the (111)-oriented diamond anvil[53].
Because the pressure was estimated using the temperature correction reported at ambient pressure, the obtained value should be regarded as an approximate pressure near the NV layer.

Figure4a and b show a optical scope image and a wide-field fluorescence image acquired atPODMR=11.8P_{\mathrm{ODMR}}=11.8GPa and 300 K.
At the pressure–temperature conditions studied here, iron is expected to remain in the ferromagnetic region according to the reported magnetic phase diagram, althoughα\alpha-Fe transforms to nonferromagneticϵ\epsilon-Fe at around 13–15 GPa under hydrostatic compression at room temperature[17].
The position of the sample chamber was identified from an optical image taken from the opposite side of the NV-containing diamond anvil.
Only part of the iron foil was directly visible; therefore, the overall foil position was inferred from the visible portion, the known foil geometry, and the ODMR-derived magnetic-field map.
The region of interest used for ODMR analysis was defined to encompass the KCl-filled sample chamber region.
A bias magnetic field of approximately 5.7 mT was applied using a permanent magnet, with the field direction approximately aligned along the [111] direction of the diamond anvil.
We define the ODMR splitting as the frequency separation between the two resonance dips assigned to the (111)-oriented NV centers.

Figure4b shows the spatial map of ODMR splitting obtained from the wide-field ODMR spectra.
The observed splitting map contains both enhanced and reduced regions relative to the background splitting far from the sample.
This behavior can be understood as the spatial variation of the stray magnetic field from the iron foil projected along the [111] NV axis.
Where the stray-field component is parallel to the applied bias field, the total field along the NV axis increases and the ODMR splitting becomes larger.
In contrast, where the stray-field component is antiparallel to the bias field, the total field is partially cancelled and the ODMR splitting becomes smaller.
To illustrate the spectral origin of the contrast in the splitting map, representative ODMR spectra obtained from regions with enhanced splitting, reduced splitting, and far from the iron foil are shown in Fig.4c.Figure 4:Wide-field ODMR atPODMR=11.8P_{\mathrm{ODMR}}=11.8GPa and 300 K.
(a) Optical scope image inside diamond anvil cell. The scale bar indicates 50μ\mum.
(b) Wide-field fluorescence image in the region of interest (ROI) shown in (a).
The sample chamber position was identified from an optical image taken from the opposite side of the NV-containing diamond anvil.
The black dotted line shows the estimated outline of the iron foil, the red solid square indicates the ROI used for ODMR analysis, and the blue dotted circle indicates the KCl-filled sample chamber region.
(c) ODMR splitting map obtained from pixel-by-pixel fitting of the wide-field ODMR spectra in the ROI shown in (b).
The ODMR splitting is defined as the frequency separation between the two resonance dips assigned to the [111]-oriented NV centers under an applied bias magnetic field of approximately 5.7 mT.
Enhanced and reduced splitting regions correspond to stray-field components from the iron foil that are parallel and antiparallel to the applied bias field along the [111] NV axis, respectively.
The colored circles indicate the positions at which the representative ODMR spectra in (c) were extracted.
(d) Representative ODMR spectra obtained from regions with enhanced splitting, reduced splitting, and far from the iron foil.
The ODMR spectra are vertically offset by 0.015 for clarity.
The scale bars in (b) and (c) represent 10μ\mum.

Next, we increased the temperature from the condition shown in Fig.4and performed wide-field ODMR measurements under simultaneous high-pressure and high-temperature conditions.
Figure5a shows the ODMR splitting map measured at 430 K andPODMR=11.2P_{\mathrm{ODMR}}=11.2GPa.
A spatial variation of the ODMR splitting is still observed near the iron foil, indicating that the stray magnetic field from the sample can be imaged under high-pressure and high-temperature conditions.
Representative ODMR spectra obtained from regions with enhanced splitting, reduced splitting, and far from the iron foil are shown in Fig.5b.

Figures5c and5d show the corresponding results measured at 500 K andPODMR=7.2P_{\mathrm{ODMR}}=7.2GPa.
In this measurement, camera binning was employed to improve the signal-to-noise ratio within the limited acquisition time, resulting in a coarser spatial sampling than in the lower-temperature measurements.
The pressure estimated from the ODMR shift decreased during heating, possibly caused by deformation of the sample chamber.
Indeed, the sample chamber had been deformed after the heating experiment.
A clear spatial variation of the ODMR splitting remains visible at higher temperature.
These results demonstrate that NV-based wide-field magnetic imaging can be performed at temperatures above 500 K under applied pressure.Figure 5:Wide-field ODMR under simultaneous high-pressure and high-temperature conditions.
(a) ODMR splitting map measured at 430 K andPODMR=11.2P_{\mathrm{ODMR}}=11.2GPa.
(b) Representative ODMR spectra obtained from regions with enhanced splitting, reduced splitting, and far from the iron foil for the data shown in (a).
(c) ODMR splitting map measured at 500 K andPODMR=7.2P_{\mathrm{ODMR}}=7.2GPa.
Camera binning was employed in this measurement to improve the signal-to-noise ratio within the limited acquisition time, resulting in coarser spatial sampling.
(d) Representative ODMR spectra obtained from regions with enhanced splitting, reduced splitting, and far from the iron foil for the data shown in (c).
The ODMR spectra are vertically offset by 0.015 for clarity.
The scale bars in (a) and (c) represent 10μ\mum.

Figures6a and6b summarize the linewidth and ODMR contrast, respectively, as a function of temperature.
These values were extracted from the lower-frequency ODMR resonance assigned to the [111]-oriented NV centers in spectra acquired far from the iron foil, as indicated by the green regions in the corresponding splitting maps.
The linewidth shows only a weak temperature dependence over the measured temperature range.
In contrast, the ODMR contrast decreases with increasing temperature, as previously reported[39].Figure 6:Temperature dependence of ODMR spectral parameters under high-pressure and high-temperature conditions.
(a) Linewidth of the lower-frequency resonance assigned to the [111]-oriented NV centers, extracted from ODMR spectra acquired far from the iron foil.
(b) ODMR contrast extracted from the same resonance.
The extraction regions are indicated by the green regions in the corresponding splitting maps.
The linewidth shows only a weak temperature dependence, whereas the ODMR contrast decreases with increasing temperature.

## IVDiscussion

The present results demonstrate that NV-magnetometry can serve as local magnetic probes under simultaneous high-pressure and high-temperature conditions.
Compared with conventional bulk magnetometry, the present approach provides spatially resolved information from a sample inside a DAC.
This capability is complementary to element- or isotope-selective probes such as XMCD and Mössbauer spectroscopy, because NV magnetometry detects the local magnetic field generated by the sample.
Thus, NV-based magnetic imaging may provide a new route for investigating magnetic properties under pressure and temperature.

The temperature dependence ofDDis known to originate from phonon-mediated effects, and recent analytical models describeD​(T)D(T)in terms of the thermal occupation of representative phonon modes[54,55,56,57].
Under applied pressure, phonon energies generally increase, and therefore the temperature dependence ofDDmay also be modified by pressure.
However, this effect is expected to be small in diamond at the pressure range studied here because of its lattice stiffness.
This expectation is supported by high-pressure Raman studies showing only a moderate pressure dependence of the diamond phonon modes[58].
Assuming that the relevant phonon modes contributing toD​(T)D(T)have a comparable pressure dependence, the change in the calculated thermal shift ofDDbetween 300 and 500 K is expected to be only marginal at around 10 GPa.

There is still considerable scope to extend the experimental range in both temperature and pressure.
For temperature, CW ODMR is applicable up to approximately 700 K, while pulsed-ODMR with laser heating allows measurements up to 1400 K[39,40,41].
In practice, however, repeated short-timescale pressure variations during heating cycles in pulsed-ODMR are expected to limit the experimental feasibility.
Accordingly, the practical temperature limit is likely around 700 K.
Reaching higher pressures will also require experiments under hydrostatic conditions using fluid pressure-transmitting media, because non-hydrostatic pressure reduces the ODMR contrast[38,59].

## VConclusion

In conclusion, we demonstrated NV-based magnetic imaging under simultaneous high-pressure and high-temperature conditions.
ODMR signals from NV centers were observed up to 500 K under applied pressure, and wide-field ODMR measurements visualized the stray magnetic field from an iron foil under the same combined extreme conditions.
These results show that NV-center magnetometry can be extended to spatially resolved magnetic imaging under concurrent high-pressure and high-temperature conditions.
Further studies on the pressure and temperature dependence of the zero-field splitting under in situ pressure and temperature calibration will be essential for quantitative NV magnetometry in high-pressure and high-temperature environments.

## Acknowledgements.This work was supported by JSPS KAKENHI Grant numbers JP24KJ1035, JP23K26528, JP23KK0267.
This work was also supported by JST ASPIRE Grant number JPMJAP24C1.
M.O. receives funding from JSPS Grant-in-Aid for JSPS Fellows Grant number JP24KJ1035.
E.K. receives funding from JST SPRING, Japan Grant Number JPMJSP2180.

## DATA AVAILABILITY

The data that support the findings of this article are openly available[60].

## References
- Shen and Mao [2016]G. Shen and H. K. Mao, High-pressure studies with x-rays
using diamond anvil cells,Rep. Prog. Phys.80, 016101 (2016).
- Maoet al.[2018]H.-K. Mao, X.-J. Chen,
Y. Ding, B. Li, and L. Wang, Solids, liquids, and gases under high pressure,Rev. Mod. Phys.90, 015007 (2018).
- Yamanaka [2010]S. Yamanaka, Silicon clathrates and
carbon analogs: High pressure synthesis, structure, and superconductivity,Dalton Trans.39, 1901 (2010).
- Azumaet al.[2021]M. Azuma, H. Hojo,
K. Oka, H. Yamamoto, K. Shimizu, K. Shigematsu, and Y. Sakai, Functional Transition Metal Perovskite Oxides with 6s2 Lone Pair
Activity Stabilized by High-Pressure Synthesis,Annual Review of Materials Research51, 329 (2021).
- Hazen and Finger [1981]R. M. Hazen and L. W. Finger, High-temperature
diamond-anvil pressure cell for single-crystal studies,Rev. Sci. Instrum.52, 75 (1981).
- Liu and Bassett [1975]L.-G. Liu and W. A. Bassett, The melting of iron up to
200 kbar,Journal of Geophysical Research (1896-1977)80, 3777 (1975).
- Ming and Bassett [1974]L.-c. Ming and W. A. Bassett, Laser heating in the
diamond anvil press up to 2000∘C sustained and
3000∘C pulsed at pressures up to 260 kilobars,Rev. Sci. Instrum.45, 1115 (1974).
- Salamatet al.[2014]A. Salamat, R. A. Fischer, R. Briggs,
M. I. McMahon, and S. Petitgirard,In Situsynchrotron
X-ray diffraction in the laser-heated diamond anvil cell: Melting
phenomena and synthesis of new materials,Coordination Chemistry Reviews Following
Chemical Structures Using Synchrotron Radiation,277–278, 15 (2014).
- Linet al.[2004]J.-F. Lin, M. Santoro,
V. V. Struzhkin, H.-k. Mao, and R. J. Hemley, In situ high pressure-temperature Raman spectroscopy
technique with laser-heated diamond anvil cells,Rev. Sci. Instrum.75, 3302 (2004).
- Kantoret al.[2018]I. Kantor, C. Marini,
O. Mathon, and S. Pascarelli, A laser heating facility for energy-dispersive X-ray
absorption spectroscopy,Rev. Sci. Instrum.89, 013111 (2018).
- Yousufet al.[1986]M. Yousuf, P. Ch. Sahu, and K. G. Rajan, High-pressure and
high-temperature electrical resistivity of ferromagnetic transition metals:
Nickel and iron,Phys. Rev. B34, 8086 (1986).
- Ohtaet al.[2023]K. Ohta, S. Suehiro,
S. I. Kawaguchi, Y. Okuda, T. Wakamatsu, K. Hirose, Y. Ohishi, M. Kodama, S. Hirai, and S. Azuma, Measuring
the Electrical Resistivity of Liquid Iron to 1.4 Mbar,Phys. Rev. Lett.130, 266301 (2023).
- Pipkornet al.[1964]D. N. Pipkorn, C. K. Edge,
P. Debrunner, G. De Pasquali, H. G. Drickamer, and H. Frauenfelder, Mössbauer Effect in Iron under Very High
Pressure,Phys. Rev.135, A1604 (1964).
- Kantoret al.[2004]A. P. Kantor, S. D. Jacobsen, I. Y. Kantor, L. S. Dubrovinsky, C. A. McCammon, H. J. Reichmann, and I. N. Goncharenko, Pressure-Induced
Magnetization in FeO: Evidence from Elasticity and
M\”ossbauer Spectroscopy,Phys. Rev. Lett.93, 215502 (2004).
- Liet al.[2024]X. Li, E. Bykova, D. Vasiukov, G. Aprilis, S. Chariton, V. Cerantola, M. Bykov, S. Müller, A. Pakhomova, F. I. Akbar, E. Mukhina, I. Kantor,
K. Glazyrin, D. Comboni, A. I. Chumakov, C. McCammon, L. Dubrovinsky, C. Sanchez-Valle, and I. Kupenko, Monoclinic distortion and magnetic transitions in FeO under
pressure and temperature,Commun Phys7, 305 (2024).
- Mathonet al.[2004a]O. Mathon, F. Baudelet,
J. P. Iti’e, A. Polian, M. d’Astuto, J. C. Chervin, and S. Pascarelli, Dynamics of the magnetic and structuralα\alpha–ϵ\epsilonphase transition in iron,Phys. Rev. Lett.93, 255503 (2004a).
- Dewaele and Nataf [2022]A. Dewaele and L. Nataf, Magnetic phase diagram of
iron at high pressure and temperature,Phys. Rev. B106, 014104 (2022).
- Cranshaw [1974]T. E. Cranshaw, Mössbauer
spectroscopy,J. Phys. E: Sci. Instrum.7, 497 (1974).
- Mathonet al.[2004b]O. Mathon, F. Baudelet,
J.-P. Itié, S. Pasternak, A. Polian, and S. Pascarelli, XMCD under pressure at the Fe K edge on the
energy-dispersive beamline of the ESRF,J Synchrotron Rad11, 423 (2004b).
- Haskelet al.[2007]D. Haskel, Y. C. Tseng,
J. C. Lang, and S. Sinogeikin, Instrument for x-ray magnetic circular dichroism
measurements at high pressures,Rev. Sci. Instrum.78, 083904 (2007).
- Mito and Hamada [2025]M. Mito and M. Hamada, Magnetization measurements using
SQUID with diamond anvil cells under extremely high pressure,Appl. Phys. Rev.12, 031310 (2025).
- Jelezkoet al.[2004a]F. Jelezko, T. Gaebel,
I. Popa, A. Gruber, and J. Wrachtrup, Observation of Coherent Oscillations in a Single Electron
Spin,Phys. Rev. Lett.92, 076401 (2004a).
- Gaebelet al.[2006]T. Gaebel, M. Domhan,
I. Popa, C. Wittmann, P. Neumann, F. Jelezko, J. R. Rabeau, N. Stavrias, A. D. Greentree, S. Prawer,
J. Meijer, J. Twamley, P. R. Hemmer, and J. Wrachtrup, Room-temperature coherent coupling of single spins in diamond,Nature Phys2, 408 (2006).
- Jelezkoet al.[2004b]F. Jelezko, T. Gaebel,
I. Popa, M. Domhan, A. Gruber, and J. Wrachtrup, Observation of Coherent Oscillation of a Single Nuclear Spin and
Realization of a Two-Qubit Conditional Quantum Gate,Phys. Rev. Lett.93, 130501 (2004b).
- Hansonet al.[2006]R. Hanson, F. M. Mendoza,
R. J. Epstein, and D. D. Awschalom, Polarization and Readout of
Coupled Single Spins in Diamond,Phys. Rev. Lett.97, 087601 (2006).
- Duttet al.[2007]M. V. G. Dutt, L. Childress, L. Jiang,
E. Togan, J. Maze, F. Jelezko, A. S. Zibrov, P. R. Hemmer, and M. D. Lukin, Quantum
Register Based on Individual Electronic and Nuclear Spin Qubits
in Diamond,Science316, 1312 (2007).
- Tayloret al.[2008]J. M. Taylor, P. Cappellaro,
L. Childress, L. Jiang, D. Budker, P. R. Hemmer, A. Yacoby, R. Walsworth, and M. D. Lukin, High-sensitivity diamond magnetometer with nanoscale resolution,Nature Phys.4, 810 (2008).
- Degen [2008]C. L. Degen, Scanning magnetic field
microscope with a diamond single-spin sensor,Applied Physics Letters92, 243111 (2008).
- Balasubramanianet al.[2008]G. Balasubramanian, I. Y. Chan, R. Kolesov,
M. Al-Hmoud, J. Tisler, C. Shin, C. Kim, A. Wojcik, P. R. Hemmer,
A. Krueger, T. Hanke, A. Leitenstorfer, R. Bratschitsch, F. Jelezko, and J. Wrachtrup, Nanoscale imaging magnetometry with diamond spins under ambient
conditions,Nature455, 648 (2008).
- Mazeet al.[2008]J. R. Maze, P. L. Stanwix,
J. S. Hodges, S. Hong, J. M. Taylor, P. Cappellaro, L. Jiang, M. V. G. Dutt, E. Togan, A. S. Zibrov, A. Yacoby, R. L. Walsworth, and M. D. Lukin, Nanoscale magnetic sensing
with an individual electronic spin in diamond,Nature455, 644 (2008).
- Acostaet al.[2010]V. M. Acosta, E. Bauch,
M. P. Ledbetter, A. Waxman, L.-S. Bouchard, and D. Budker, Temperature Dependence of the Nitrogen-Vacancy Magnetic
Resonance in Diamond,Phys. Rev. Lett.104, 070801 (2010).
- Doldeet al.[2011]F. Dolde, H. Fedder,
M. W. Doherty, T. Nöbauer, F. Rempp, G. Balasubramanian, T. Wolf, F. Reinhard, L. C. L. Hollenberg, F. Jelezko, and J. Wrachtrup, Electric-field sensing
using single diamond spins,Nature Phys7, 459 (2011).
- Kucskoet al.[2013]G. Kucsko, P. C. Maurer,
N. Y. Yao, M. Kubo, H. J. Noh, P. K. Lo, H. Park, and M. D. Lukin, Nanometre-scale thermometry in a living cell,Nature500, 54 (2013).
- Le Sageet al.[2013]D. Le Sage, K. Arai,
D. R. Glenn, S. J. DeVience, L. M. Pham, L. Rahn-Lee, M. D. Lukin, A. Yacoby, A. Komeili, and R. L. Walsworth, Optical
magnetic imaging of living cells,Nature496, 486 (2013).
- Dohertyet al.[2013]M. W. Doherty, N. B. Manson,
P. Delaney, F. Jelezko, J. Wrachtrup, and L. C. L. Hollenberg, The nitrogen-vacancy colour centre in diamond,Physics Reports The
Nitrogen-Vacancy Colour Centre in Diamond,528, 1 (2013).
- Dohertyet al.[2014a]M. W. Doherty, V. V. Struzhkin, D. A. Simpson, L. P. McGuinness, Y. Meng,
A. Stacey, T. J. Karle, R. J. Hemley, N. B. Manson, L. C. L. Hollenberg, and S. Prawer, Electronic properties and metrology applications of the
diamondNV−\mathrm{NV}^{-}center under pressure,Phys. Rev. Lett.112, 047601 (2014a).
- Broadwayet al.[2019]D. A. Broadway, B. C. Johnson, M. S. J. Barson, S. E. Lillie,
N. Dontschuk, D. J. McCloskey, A. Tsai, T. Teraji, D. A. Simpson, A. Stacey, J. C. McCallum, J. E. Bradby, M. W. Doherty,
L. C. L. Hollenberg, and J.-P. Tetienne, Microscopic Imaging of the
Stress Tensor in Diamond Using in Situ Quantum Sensors,Nano Lett.19, 4543 (2019).
- Hoet al.[2023]K. O. Ho, M. Y. Leung,
W. Wang, J. Xie, K. Y. Yip, J. Wu, S. K. Goh, A. Denisenko, J. Wrachtrup, and S. Yang, Spectroscopic Study of
N-$V$ Sensors in Diamond-Based High-Pressure Devices,Phys. Rev. Appl.19, 044091 (2023).
- Toyliet al.[2012]D. M. Toyli, D. J. Christle,
A. Alkauskas, B. B. Buckley, C. G. Van de Walle, and D. D. Awschalom, Measurement and Control of Single
Nitrogen-Vacancy Center Spins above 600 K,Phys. Rev. X2, 031001 (2012).
- Liuet al.[2019]G.-Q. Liu, X. Feng, N. Wang, Q. Li, and R.-B. Liu, Coherent quantum control of nitrogen-vacancy center spins near 1000
Kelvin,Nat. Commun.10, 1344 (2019).
- Fanet al.[2024]J.-W. Fan, S.-W. Guo,
C. Lin, N. Wang, G.-Q. Liu, Q. Li, and R.-B. Liu, Quantum
coherence control at temperatures up to 1400 K,Nano Lett.24, 14806 (2024).
- Hsiehet al.[2019]S. Hsieh, P. Bhattacharyya, C. Zu,
T. Mittiga, T. J. Smart, F. Machado, B. Kobrin, T. O. Höhn, N. Z. Rui, M. Kamrani, S. Chatterjee,
S. Choi, M. Zaletel, V. V. Struzhkin, J. E. Moore, V. I. Levitas, R. Jeanloz, and N. Y. Yao, Imaging stress and magnetism at high
pressures using a nanoscale quantum sensor,Science366, 1349 (2019).
- Lesiket al.[2019]M. Lesik, T. Plisson,
L. Toraille, J. Renaud, F. Occelli, M. Schmidt, O. Salord, A. Delobbe, T. Debuisschert, L. Rondin, P. Loubeyre, and J.-F. Roch, Magnetic measurements on micrometer-sized samples under high pressure using
designed NV centers,Science366, 1359 (2019).
- Yipet al.[2019]K. Y. Yip, K. O. Ho,
K. Y. Yu, Y. Chen, W. Zhang, S. Kasahara, Y. Mizukami, T. Shibauchi, Y. Matsuda, S. K. Goh, and S. Yang, Measuring magnetic field
texture in correlated electron systems under extreme conditions,Science366, 1355 (2019).
- Bhattacharyyaet al.[2024]P. Bhattacharyya, W. Chen,
X. Huang, S. Chatterjee, B. Huang, B. Kobrin, Y. Lyu, T. J. Smart, M. Block, E. Wang,
Z. Wang, W. Wu, S. Hsieh, H. Ma, S. Mandyam, B. Chen,
E. Davis, Z. M. Geballe, C. Zu, V. Struzhkin, R. Jeanloz, J. E. Moore, T. Cui, G. Galli, B. I. Halperin, C. R. Laumann, and N. Y. Yao, Imaging the Meissner effect in hydride superconductors using
quantum sensors,Nature627, 73 (2024).
- Wanget al.[2024]M. Wang, Y. Wang, Z. Liu, G. Xu, B. Yang, P. Yu, H. Sun, X. Ye, J. Zhou, A. F. Goncharov, Y. Wang, and J. Du, Imaging
magnetic transition of magnetite to megabar pressures using quantum sensors
in diamond anvil cell,Nat. Commun.15, 8843 (2024).
- Ziegleret al.[2010]J. F. Ziegler, M. D. Ziegler, and J. P. Biersack, SRIM – the stopping
and range of ions in matter (2010),Nuclear Instruments and Methods in Physics Research Section B:
Beam Interactions with Materials and Atoms268, 1818 (2010).
- Takanoet al.[2004]Y. Takano, M. Nagao,
I. Sakaguchi, M. Tachiki, T. Hatano, K. Kobayashi, H. Umezawa, and H. Kawarada, Superconductivity in diamond thin films well above liquid helium
temperature,Applied Physics Letters85, 2851 (2004).
- Matsumotoet al.[2016]R. Matsumoto, Y. Sasama,
M. Fujioka, T. Irifune, M. Tanaka, T. Yamaguchi, H. Takeya, and Y. Takano, Note:
Novel diamond anvil cell for electrical measurements using boron-doped
metallic diamond electrodes,Review of Scientific
Instruments87, 076103
(2016).
- Matsumotoet al.[2021]R. Matsumoto, S. Yamamoto,
S. Adachi, T. Sakai, T. Irifune, and Y. Takano, Diamond anvil cell with boron-doped diamond heater for high-pressure
synthesis and in situ transport measurements,Applied Physics Letters119, 053502 (2021).
- Ohkumaet al.[2024]M. Ohkuma, E. Kimura,
R. Matsumoto, S. Ohyama, S. Tsuchiya, H. Lim, Y. S. Lee, J. Lee, Y. Takano, and K. Arai,Coherent control of solid-state defect spins via patterned boron-doped
diamond circuit(2024),arXiv:2412.15586 [physics].
- Weiet al.[2024]Y. Wei, Q. Zhou, C. Zhang, L. Li, X. Li, and F. Li, Fluorescence
pressure sensors: Calibration of ruby, Sm2+: SrB4O7, and
Sm3+: YAG to 55 GPa and 850 K,Journal of Applied Physics135, 105902 (2024).
- Maiet al.[2025]D. Mai, C. Zhong, Z. Wang, H. Wang, X. Sun, R. Dai, Z. Wang, and Z. Zhang, Megabar pressure sensing and magnetic phase
imaging by [111]-oriented nitrogen-vacancy centers in diamond,J. Appl. Phys.138, 045901 (2025).
- Dohertyet al.[2014b]M. W. Doherty, V. M. Acosta,
A. Jarmola, M. S. J. Barson, N. B. Manson, D. Budker, and L. C. L. Hollenberg, Temperature shifts of the resonances of the NV-center in diamond,Phys. Rev. B90, 041201 (2014b).
- Ivádyet al.[2014]V. Ivády, T. Simon,
J. R. Maze, I. A. Abrikosov, and A. Gali, Pressure and temperature dependence of the zero-field
splitting in the ground state of NV centers in diamond: A
first-principles study,Phys. Rev. B90, 235205 (2014).
- Tanget al.[2023]H. Tang, A. R. Barr,
G. Wang, P. Cappellaro, and J. Li, First-Principles Calculation of the Temperature-Dependent
Transition Energies in Spin Defects,J. Phys. Chem. Lett.14, 3266 (2023).
- Cambriaet al.[2023]M. C. Cambria, G. Thiering,
A. Norambuena, H. T. Dinani, A. Gardill, I. Kemeny, V. Lordi, Á. Gali, J. R. Maze, and S. Kolkowitz, Physically motivated analytical expression for the temperature dependence of
the zero-field splitting of the nitrogen-vacancy center in diamond,Phys. Rev. B108, L180102 (2023).
- Akahama and Kawamura [2004]Y. Akahama and H. Kawamura, High-pressure Raman
spectroscopy of diamond anvils to 250GPa: Method for pressure
determination in the multimegabar pressure range,Journal of Applied Physics96, 3748 (2004).
- Huanget al.[2026]B. Huang, S. V. Mandyam,
W. Wu, B. Kobrin, P. Bhattacharyya, Y. Jin, B. Chen, M. Block,
E. Wang, Z. Wang, S. Hsieh, C. Zu, C. R. Laumann, N. Y. Yao, and G. Galli,Elucidating the Inter-system Crossing of the Nitrogen-Vacancy
Center up to Megabar Pressures(2026),arXiv:2511.20750 [quant-ph].
- Ohkumaet al.[2026]M. Ohkuma, E. Kimura,
S. Ohyama, M. Tezuka, R. Matsumoto, S. Onoda, Y. Takano, S. Azuma, K. Ohta, and K. Arai, Replication Data for: Wide-field NV magnetometry under simultaneous
high-pressure and high-temperature conditions, Zenodo10.5281/zenodo.19255015(2026).

## 


- 


Major funding support from
