# Enhanced Temperature Sensitivity in Ensemble NV Centers through Improved Optically Detected Magnetic Resonance Spectral Modeling

**arXiv ID**: 2605.18863v1
**Authors**: Yuki S. Kato, Shingo Sotoma, Keisuke Fujita, Masanori Fujiwara, Izuru Ohki, Yuichiro Matsuzaki, Norikazu Mizuochi, Yoshie Harada
**Published**: 2026-05-15
**Categories**: physics.ins-det, quant-ph
**HTML URL**: https://arxiv.org/html/2605.18863v1

## Abstract

Nitrogen-vacancy (NV) center ensembles provide a powerful platform for high-precision temperature sensing, with ongoing efforts to further enhance their measurement performance. In ensemble NV optically detected magnetic resonance (ODMR) spectra, commonly used Lorentzian and Voigt fitting models fail to accurately describe the spectral shape near the resonance frequency, leading to degraded precision in resonance-frequency determination and, consequently, temperature estimation. In this work, we analytically establish a new fitting method, termed dip-peak fitting, for extracting the resonance frequency from ensemble cw-ODMR spectra. Starting from a physical model that describes ensemble cw-ODMR spectra as a convolution of single-NV responses with distributed zero-field splitting and strain, we show that the spectral feature near resonance can be accurately approximated by a single Lorentzian function with a background term. The proposed fitting model reproduces the cw-ODMR spectrum around resonance more faithfully than conventional approaches, enabling faster and more accurate resonance-frequency determination under weaker microwave excitation. Experiments using fluorescent nanodiamond ensembles confirm the robustness and applicability of this method for high-precision temperature sensing.

## Full Text

Enhanced Temperature Sensitivity in Ensemble NV Centers through Improved Optically Detected Magnetic Resonance Spectral Modeling

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- License: arXiv.org perpetual non-exclusive licensearXiv:2605.18863v1 [physics.ins-det] 15 May 2026

## Enhanced Temperature Sensitivity in Ensemble NV Centers through
Improved Optically Detected Magnetic Resonance Spectral ModelingYuki S. Katoyuki.s.kato@gmail.comDepartment of Earth and Space Science, Graduate School of Science, The University of Osaka, Osaka 560-0043, JapanShingo SotomaFaculty of Molecular Chemistry and Engineering, Kyoto Institute of Technology, Sakyo-ku, Kyoto 606-8585, JapanKeisuke FujitaPremium Research Institute for Human Metaverse Medicine, The University of Osaka, Osaka 565-0871, JapanMasanori FujiwaraInstitute for Chemical Research, Kyoto University, Uji, Kyoto 611-0011, Japan
Izuru OhkiInstitute for Chemical Research, Kyoto University, Uji, Kyoto 611-0011, JapanYuichiro MatsuzakiDepartment of Electrical, Electronic, and Communication Engineering, Faculty of Science and Engineering, Chuo University, Tokyo, JapanNorikazu MizuochiInstitute for Chemical Research, Kyoto University, Uji, Kyoto 611-0011, JapanYoshie Haradayharada@protein.osaka-u.ac.jpPremium Research Institute for Human Metaverse Medicine, The University of Osaka, Osaka 565-0871, JapanCenter for Quantum Information and Quantum Biology, The
University of Osaka, Osaka 560-0043, Japan

## Abstract

Nitrogen-vacancy (NV) center ensembles provide a powerful platform for high-precision temperature sensing, with ongoing efforts to further enhance their measurement performance. In ensemble NV optically detected magnetic resonance (ODMR) spectra, commonly used Lorentzian and Voigt fitting models fail to accurately describe the spectral shape near the resonance frequency, leading to degraded precision in resonance-frequency determination and, consequently, temperature estimation. In this work, we analytically establish a new fitting method, termed dip–peak fitting, for extracting the resonance frequency from ensemble cw-ODMR spectra. Starting from a physical model that describes ensemble cw-ODMR spectra as a convolution of single-NV responses with distributed zero-field splitting and strain, we show that the spectral feature near resonance can be accurately approximated by a single Lorentzian function with a background term. The proposed fitting model reproduces the cw-ODMR spectrum around resonance more faithfully than conventional approaches, enabling faster and more accurate resonance-frequency determination under weaker microwave excitation. Experiments using fluorescent nanodiamond ensembles confirm the robustness and applicability of this method for high-precision temperature sensing.††preprint:APS/123-QED

## IINTRODUCTION

The negatively charged nitrogen-vacancy (NV) center in diamond is a versatile solid-state quantum sensor, as its spin state can be optically initialized, coherently manipulated, and read out under ambient conditions at room temperature[10,5,19].
For many sensing applications, achieving high sensitivity requires sufficient photon collection and signal stability, which can be challenging for measurements based on single NV centers.
Ensembles of NV centers address this limitation by providing enhanced signal-to-noise ratios through collective optical readout, enabling high-sensitivity measurements under practical experimental conditions[11]. Fluorescent nanodiamonds (FNDs) hosting NV ensembles combine this ensemble signal enhancement with nanoscale probe dimensions, allowing quantum sensing with both high sensitivity and nanoscale spatial resolution[19].
These properties enable detection of various physical quantities, including magnetic fields[2,17], electric fields[6,7], and temperature[14].

The NV center has a spin-1 ground state, with the|ms=±1⟩\ket{m_{s}=\pm 1}levels separated from the|ms=0⟩\ket{m_{s}=0}level by
the zero-field splitting of approximately 2.87 GHz [Fig.1(a)].
Owing to spin-state-dependent fluorescence under green
laser excitation, the NV electron spin can be efficiently
initialized and read out optically[9][Fig.1(b)].
Sweeping the microwave frequency around the zero-field
splitting gives rise to optically detected magnetic resonance
(ODMR) spectra.
Because the zero-field splitting depends on temperature via thermal expansion of the diamond lattice, shifts in the ODMR spectra allow for quantitative thermometry[1,3].Figure 1:(a) Schematic illustration of a nitrogen–vacancy center (NVC) in diamond. The NVC is a point defect in the diamond lattice, consisting of a substitutional nitrogen atom adjacent to a lattice vacancy. The NVC is a spin-1 system and exhibits unique optical properties.
(b) Energy-level diagram of a NVC.

Accurate temperature sensing is crucial in a wide range of physical and biological systems.
Compared with other fluorescent thermometers, FNDs enable temperature to be extracted independently of fluctuations in other physical parameters and chemical environments, thereby allowing for reliable temperature measurements[20].
This capability has led to their widespread use in biological systems, including intracellular thermometry[14,22,4,23,15,21].

There are two principal strategies for temperature measurement using FNDs. One approach tracks temperature changes within the same diamond, while the other compares temperatures across different diamonds at different spatial and temporal locations. In the former case, temperature variations can be inferred by monitoring fluorescence intensity at one or several fixed microwave frequencies[14,23,8,21]. In contrast, the latter approach requires sweeping the microwave frequency to acquire ODMR spectra, from which the resonance frequency is identified via spectral fitting[22,4,15].

To date, Lorentzian and Voigt functions have been widely employed to fit ensemble ODMR spectra. The Lorentzian function is based on the response of an ideal two-level system and is typically expressed as a superposition of two Lorentzian components corresponding to the|ms=0⟩→(1/2)​(|1⟩−|−1⟩)\ket{m_{s}=0}\rightarrow(1/\sqrt{2})\left(\Ket{1}-\Ket{-1}\right)and|ms=0⟩→(1/2)​(|1⟩+|−1⟩)\ket{m_{s}=0}\rightarrow(1/\sqrt{2})\left(\Ket{1}+\Ket{-1}\right)transitions. In practice, however, each NV center experiences a distinct local environment, and consequently, not all NV centers exhibit identical spectral line shapes. As a result, Lorentzian functions alone fail to adequately describe ensemble ODMR spectra[13,24]. To address this limitation, Voigt functions—assuming a distribution of lattice strain or electric-field interactions among NV centers—have also been employed. Nevertheless, even Voigt functions cannot fully reproduce ensemble ODMR spectra.

Such fitting functions, which do not fully capture the ODMR spectrum, have limited the achievable performance of temperature measurements.
In practice, the achieved temperature precision has been substantially worse than the limits expected from fundamental noise sources, such as shot-noise-limited detection.
This discrepancy indicates that further improvements require the development of more appropriate fitting models.
To address this issue, various approaches and fitting strategies have been proposed and investigated in previous studies[11,24]. In this context, alternative fitting strategies have been explored that focus on spectral features in the immediate vicinity of the resonance frequency, rather than on the global ODMR line shape.

Kołodziej et al. proposed a practical fitting approach in which the peak-like feature within the cw-ODMR dip in the vicinity of the resonance frequency is modeled by a single Lorentzian function plus a background term[12]. However, the physical basis of this fitting form and its quantitative utility have not been clarified, and the method has not yet been widely adopted. In this paper, we analytically elucidate the physical origin of this fitting model—hereafter referred to as dip-peak fitting—and rigorously demonstrate its effectiveness.

We begin by expressing the ensemble cw-ODMR spectrum as a convolution integral of single-NV cw-ODMR spectra. Through an analytical transformation of this expression, we show that the spectral feature in the vicinity of the resonance frequency can be described by a single Lorentzian function. Experimentally, we demonstrate that dip-peak fitting reproduces the cw-ODMR spectrum near resonance more faithfully than conventional fitting methods and enables high-precision estimation of the resonance frequency with significantly reduced acquisition time. We further investigate the range of microwave excitation strengths compatible with dip–peak fitting, and demonstrate that accurate fitting is achievable over a wide range, with optimal performance obtained at relatively low excitation powers. Finally, by varying the temperature of FNDs, we confirm that dip-peak fitting captures the temperature-induced resonance shifts observed using established fitting approaches.

## IIEXPERIMENTAL METHODFigure 2:(a) Optical setup for cw-ODMR measurements.
(b) Fluorescence image of bright spots from FNDs dispersed on a glass substrate.
(c–e) cw-ODMR spectra obtained from ensembles consisting of a single bright spot (c), 30 bright spots (d), and 988 bright spots (e).

Nanodiamonds with an average diameter of approximately 100 nm, synthesized using the high-pressure high-temperature (HPHT) method, were used. To generate optically active NVCs, we introduced vacancies via electron irradiation with 2 MeV at a fluence of4×1018​cm−24\times 10^{18}\text{cm}^{-2}, followed by thermal annealing to pair nitrogen atoms and vacancies. Subsequent air oxidation removed sp2carbon from the particle surface, yielding FNDs.

The FNDs were spin-coated onto a glass substrate, yielding a uniform dispersion dominated by isolated single particles [Fig.2(b)]. The cw-ODMR spectrum measurements were performed using a homemade microscope [Fig.2(a)]. A continuous neodymium-doped yttrium aluminum garnet (Nd:YAG) laser at 532 nm illuminated FNDs to initialize and read out the spin state of NVCs on an inverted microscope system. Fluorescence from the NVCs was collected by an oil immersion objective lens, spectrally filtered by a long-pass filter to suppress the excitation light, and imaged onto a camera.

Microwave (MW) excitation was applied using a two-turn copper coil with a diameter of approximately 1 mm, positioned directly above the coverslip to irradiate the sample at frequencies near the electron spin resonance of the NVCs. The MW signal generated by a microwave source was amplified using linear microwave power amplifiers and delivered to the coil via a coaxial cable.

cw-ODMR spectra were obtained from the ratio of fluorescence intensities measured with the MW field switched on and off. While the cw-ODMR spectrum acquired from single bright spots exhibits significant noise, summing the fluorescence signals from multiple bright spots yields a cw-ODMR spectrum with substantially reduced noise [Fig.2(c, d, e)].

## IIIMODEL

We propose a novel fitting method for cw-ODMR spectra. When the external magnetic field and nuclear spins can be neglected, The Hamiltonian of the NV center is described asH=D​(T)​Sz2+E1​(Sx2−Sy2)+E2​(Sx​Sy+Sy​Sx).\displaystyle H=D(T)S_{z}^{2}+E_{1}\left(S_{x}^{2}-S_{y}^{2}\right)+E_{2}\left(S_{x}S_{y}+S_{y}S_{x}\right).(1)

whereSiS_{i}(i=x,y,zi=x,y,z) are the spin-1 operators of the NV
electron spin,D​(T)D(T)is the temperature-dependent
zero-field splitting parameter, andE1E_{1}andE2E_{2}describe transverse strain- or electric-field-induced
splittings[11]. The eigenvalues of this Hamiltonian are given by0,D−E12+E22,D+E12+E22\displaystyle 0,\qquad D-\sqrt{E_{1}^{2}+E_{2}^{2}},\qquad D+\sqrt{E_{1}^{2}+E_{2}^{2}}(2)

Assuming that the cw-ODMR spectrum of a single NV center can be described as a linear superposition of Lorentzian functions centered atD−E12+E22D-\sqrt{E_{1}^{2}+E_{2}^{2}}andD+E12+E22D+\sqrt{E_{1}^{2}+E_{2}^{2}}, it can be written asP1​(ω)\displaystyle P_{1}(\omega)=\displaystyle=1−λ′[L(ω,D+E12+E22,Γ)\displaystyle 1-\lambda^{\prime}\Bigg[L\left(\omega,D+\sqrt{E_{1}^{2}+E_{2}^{2}},\Gamma\right)(4)+L(ω,D−E12+E22,Γ)]\displaystyle+L\left(\omega,D-\sqrt{E_{1}^{2}+E_{2}^{2}},\Gamma\right)\Bigg]

whereL​(x,x0,γ)=γ/[π​{(x−x0)2+γ2}]L\left(x,x_{0},\gamma\right)=\gamma/[\pi\{(x-x_{0})^{2}+\gamma^{2}\}]is a Lorentzian function, andλ′\lambda^{\prime}is a scaling factor corresponding to the ODMR contrast.
The ensemble cw-ODMR spectrum is formed by the superposition of single-NV cw-ODMR spectra. Monte Carlo simulations suggest that the sharp cw-ODMR spectrum of each individual NV center varies due to fluctuations in the parametersDD,E1E_{1}, andE2E_{2}, which follow Lorentzian distributions (see Appendix A). Consequently, in systems containing a sufficiently large number of NV centers, the ensemble cw-ODMR spectrumPPcan be described asP\displaystyle P=\displaystyle=1−λ′​∫−∞∞𝑑D​∫−∞∞𝑑E1​∫−∞∞𝑑E2​L​(E1,0,γE1)​L​(E2,0,γE2)​L​(D,D0,γD)\displaystyle 1-\lambda^{\prime}\int_{-\infty}^{\infty}dD\int_{-\infty}^{\infty}dE_{1}\int_{-\infty}^{\infty}dE_{2}L\left(E_{1},0,\gamma_{E_{1}}\right)L\left(E_{2},0,\gamma_{E_{2}}\right)L\left(D,D_{0},\gamma_{D}\right)(6)×[L​(ω,D+E12+E22,Γ)+L​(ω,D−E12+E22,Γ)]\displaystyle\qquad\qquad\times\left[L\left(\omega,D+\sqrt{E_{1}^{2}+E_{2}^{2}},\Gamma\right)+L\left(\omega,D-\sqrt{E_{1}^{2}+E_{2}^{2}},\Gamma\right)\right]

Here, for simplicity, we setγE1=γE2≡γE\gamma_{E_{1}}=\gamma_{E_{2}}\equiv\gamma_{E}. This assumption reflects the comparable statistical spreads ofE1E_{1}andE2E_{2}and is justified by numerical simulations. For the integration overDDthe convolution of two Lorentzian functions yields another Lorentzian function whose center and half width at half maximum are given by the sums of those of the original functions. By introducingr=E12+E22r=\sqrt{E_{1}^{2}+E_{2}^{2}}, the integration can be carried out explicitly asP\displaystyle P=\displaystyle=1−λ′​∫0∞𝑑r​4​γE​rπ​γE2+r2​(r2+2​γE2)​[L​(ω−D0,r,Γ′)+L​(ω−D0,−r,Γ′)]\displaystyle 1-\lambda^{\prime}\int_{0}^{\infty}dr\frac{4\gamma_{E}r}{\pi\sqrt{\gamma_{E}^{2}+r^{2}}\left(r^{2}+2\gamma_{E}^{2}\right)}[L(\omega-D_{0},r,\Gamma^{\prime})+L(\omega-D_{0},-r,\Gamma^{\prime})](7)=\displaystyle=1−λ′​(L​(ω,D0,2​γE+Γ′)−L​(ω,D0,2​γE−Γ′)+8​Γ′π2​ℜ⁡[βu+​ln⁡(1+u+1−u+)])\displaystyle 1-\lambda^{\prime}\left(L(\omega,D_{0},\sqrt{2}\,\gamma_{E}+\Gamma^{\prime})-L(\omega,D_{0},\sqrt{2}\,\gamma_{E}-\Gamma^{\prime})+\frac{8\Gamma^{\prime}}{\pi^{2}}\Re\left[\frac{\beta}{\sqrt{u_{+}}}\ln\!\left(\frac{1+\sqrt{u_{+}}}{1-\sqrt{u_{+}}}\right)\right]\right)(8)

whereΓ′=Γ+γD\Gamma^{\prime}=\Gamma+\gamma_{D}, andu+\displaystyle u_{+}=\displaystyle=(ω−D0+i​Γ′)2+γE2γE2,\displaystyle\frac{(\omega-D_{0}+i\Gamma^{\prime})^{2}+\gamma_{E}^{2}}{\gamma_{E}^{2}},(9)β\displaystyle\beta=\displaystyle=ω−D0+i​Γ′2​i​Γ′​((ω−D0)2+2​γE2−Γ′⁣2+2​i​(ω−D0)​Γ′).\displaystyle\frac{\omega-D_{0}+i\Gamma^{\prime}}{2i\Gamma^{\prime}\left((\omega-D_{0})^{2}+2\gamma_{E}^{2}-\Gamma^{\prime 2}+2i(\omega-D_{0})\Gamma^{\prime}\right)}.(10)

The results of this calculation are presented in Appendix B. These results demonstrate that the emergence of a small peak at the bottom of the dip in the ensemble cw-ODMR spectrum, as observed in [Fig.2], originates from lattice-strain fluctuations whose magnitude exceeds the half width at half maximum of the single-NV cw-ODMR spectrum. This interpretation is consistent with previous reports on high-density NV ensembles[16,18].

In the vicinity of this small peak, namely aroundω=D0\omega=D_{0}the ensemble cw-ODMR spectrum can be approximated asP​(ω)=A+B​L​(ω,D0,Γdip)+o​((ω−D0)6)P(\omega)=A+B\,L(\omega,D_{0},\Gamma_{\mathrm{dip}})+o\bigl((\omega-D_{0})^{6}\bigr)(11)

Here, the parameters are determined by matching the expansion ofP​(ω)P(\omega)up to fourth order atω=D0\omega=D_{0}:Γdip\displaystyle\Gamma_{\mathrm{dip}}=−12​P′′​(D0)P(4)​(D0),\displaystyle=\sqrt{-12\frac{P^{\prime\prime}(D_{0})}{P^{(4)}(D_{0})}},(12)B\displaystyle B=−π2​Γdip3​P′′​(D0),\displaystyle=-\frac{\pi}{2}\Gamma_{\mathrm{dip}}^{3}P^{\prime\prime}(D_{0}),(13)A\displaystyle A=P​(D0)+Γdip22​P′′​(D0).\displaystyle=P(D_{0})+\frac{\Gamma_{\mathrm{dip}}^{2}}{2}P^{\prime\prime}(D_{0}).(14)

Plots of this approximation are presented in Appendix B.
For the parameter range0.2≤Γ′/γE≤0.60.2\leq\Gamma^{\prime}/\gamma_{E}\leq 0.6,
the Lorentzian approximation reproduces the central dip–peak structure
withR2>0.995R^{2}>0.995within the interval bounded by the two inflection points of the
ensemble cw-ODMR spectrum.

These calculations and approximations provide a new fitting framework for a cw-ODMR spectrum exhibiting a small peak at the bottom of the dip. We refer to this approach—in which the central peak feature embedded within the cw-ODMR dip is modeled using a single Lorentzian termB​L​(ω,D0,Γdip)B\,L(\omega,D_{0},\Gamma_{\mathrm{dip}})combined with a background termAA[Eq. (11)]—as the dip–peak fitting.

## IVRESULTS AND DISCUSSION

## IV.1Residual comparison between conventional and dip–peak fittingFigure 3:Fitting results of cw-ODMR spectra. cw-ODMR spectra measured under weak microwave excitation (a, c, e) and strong microwave excitation (b, d, f) are fitted using a Lorentzian function (a, b), a Voigt function (c, d), and a dip–peak fitting model (e, f). Black dots represent the experimental cw-ODMR data, while red solid lines indicate the fitting results. For panels (e) and (f), the fitting results within the fitting range are shown as red solid lines, while those outside the range are shown as gray solid lines. Red dots shown below each spectrum correspond to the residuals between the experimental data and the fitting curves. In panels (e) and (f), the residuals within the fitting range are shown as red dots, while those outside the range are shown as gray dots.

Fig.3shows ensemble cw-ODMR spectra with exceptionally low noise, obtained by averaging over approximately 1000 bright spots under conditions of strong and weak microwave excitation. The spectra measured were fitted using conventional Lorentzian fitting, Voigt fitting, and the dip–peak fitting method newly introduced in this work. For the conventional methods, the full spectral range was used, whereas the dip–peak fitting was applied only within the frequency range of 2866–2872 MHz. In the dip–peak fitting, the center frequency, linewidth, amplitude, and offset of the Lorentzian function were treated as fitting parameters.

The conventional Lorentzian and Voigt fittings exhibit large residuals in the vicinity of the resonance frequency, indicating that these models do not adequately describe the cw-ODMR spectra in this region[Fig.3(a,b,d,e)]. In contrast, the dip–peak fitting reproduces the spectral features remarkably well in both excitation conditions, particularly capturing the small peak embedded within the resonance dip[Fig.3(c,f)].
Quantitatively, within the frequency range of 2866–2872 MHz around the resonance,
the coefficient of determinationR2R^{2}obtained using conventional Lorentzian and Voigt fittings falls below 0.5,
whereas the present model yieldsR2R^{2}values exceeding 0.99 under both excitation conditions.

These results demonstrate that the dip–peak fitting provides a more accurate description of the cw-ODMR spectrum near the resonance frequency than the previously employed fitting approaches.

## IV.2Resonance Frequency Determination Capability and the Law of Large Numbers

To demonstrate that the dip–peak fitting is suitable for determining the resonance frequency more reliably than conventional fitting methods, we analyzed cw-ODMR spectra with different noise levels by varying the number of bright spots included in the ensemble averaging. Since each field of view contains approximately 1000 bright spots, we randomly selectednnbright spots from the field of view to construct an ensemble cw-ODMR spectrum. This spectrum was then fitted using each fitting method, and the resonance frequency was extracted. By repeating this procedure multiple times, we evaluated the statistical variation of the resonance frequency determined from ensemble cw-ODMR spectra composed ofnnbright spots.Figure 4:Dependence of the resonance-frequency fluctuation and fitting uncertainty on the number of bright spots and the measurement time. When the number of bright spots constituting the cw-ODMR spectrum is increased (a, b) and when the measurement time is increased (c, d, e, f) the resonance-frequency fluctuation (a, c, e) and the fitting error (b, d, f) are evaluated for different fitting methods. Blue crosses indicate results obtained using Lorentzian fitting, green triangles correspond to Voigt fitting, and red circles represent results obtained using the dip–peak fitting model.
The effective measurement times for panels (a, b) are 15 min for Lorentzian and Voigt fitting, and 1.5 min for the dip–peak fitting model. Panels (c, d) are based on ensemble cw-ODMR spectra composed of 100 bright spots, while panels (e, f) use cw-ODMR spectra from a single bright spot. The dashed lines represent fits to the resonance-frequency fluctuations obtained using the dip–peak fitting model, assuming a scaling proportional to the inverse square root of the number of bright spots or the measurement time. The corresponding fitting parameters are indicated in the figure.

As the number of bright spots was increased, the variance of the resonance frequencies obtained from all fitting methods decreased in accordance with the law of large numbers[Fig.4(a)]. The dip–peak fitting achieved a precision in determining the resonance frequency that is comparable to that of the conventional fitting approaches.

We also evaluated the fitting uncertainty estimated from the diagonal elements of the covariance matrix. For the conventional fitting methods, the fitting functions do not adequately describe the cw-ODMR spectra, and as a result, the estimated fitting uncertainties do not follow the law of large numbers even as the number of averaged bright spots is increased[Fig.4(b)].
In particular, the fitting uncertainty does not decrease below approximately 0.1 MHz even for the largest number of averaged bright spots considered.
Moreover, the fitting uncertainties are significantly larger than the actual statistical variations of the resonance frequencies obtained above.

In contrast, for the dip–peak fitting, the fitting function accurately captures the spectral features of the cw-ODMR spectra, leading to fitting uncertainties that decrease in accordance with the law of large numbers. The estimated fitting uncertainty is comparable to the empirical standard deviation of the extracted resonance frequencies, amounting to approximately 0.6 times the observed statistical variation. This property is particularly advantageous for practical temperature measurements, as it enables a reliable estimation of the confidence in the determined resonance frequency directly from the fitting uncertainty.

Next, we examined, using the same procedure, how the statistical variation of the resonance frequency and the fitting uncertainty depend on the measurement time for ensemble cw-ODMR spectra composed of 100 bright spots and a single bright spot[Fig.4(c,d,e,f)]. For both conditions, the variance of the resonance frequency decreased with increasing measurement time, consistent with the law of large numbers. At a measurement time of 6 min, the empirical standard deviation of the resonance frequency is reduced to approximately 0.6 times its initial value for spectra composed of 100 bright spots and to approximately 0.75 times for a single bright spot.
The dip–peak fitting therefore enables a more precise determination of the resonance frequency within a shorter measurement time compared to conventional fitting methods.
This improvement is partly attributable to the fact that the microwave frequency sweep range required for the dip–peak fitting is approximately one tenth of that required for the conventional approaches. When the cw-ODMR spectrum of a single bright spot was analyzed using the dip–peak fitting, a residual uncertainty of approximately 0.4 MHz remained even for long measurement times[Fig.4(e)]. This residual error is attributed to the intrinsic variation of the resonance frequency inherent to the particle itself.

With respect to the fitting uncertainty, the dip–peak fitting follows the law of large numbers as the measurement time increases, whereas conventional fitting methods do not exhibit such behavior.

A consistent trend was observed across all investigated FND samples, including those with different NV center concentrations and from different manufacturers (see Appendix C). These results demonstrate that the dip–peak fitting enables the resonance frequency to be determined with higher accuracy within a shorter measurement time than the conventional fitting methods. In addition, it allows for a more reliable estimation of the confidence in the extracted values based on the fitting uncertainty.

## IV.3Appropriate microwave intensity for dip–peak fittingFigure 5:(a) cw-ODMR spectra measured at different microwave powers. Black solid lines represent results of Monte Carlo simulations (Appendix A). The microwave power was estimated from the Rabi frequency obtained by fitting the Monte Carlo simulations.
(b) Microwave-power dependence of the shot-noise-limited sensitivity obtained using Lorentzian fitting, Voigt fitting (black dots), and the dip–peak fitting model (red dots).
(c, d) Microwave-power dependence of the resonance-frequency fluctuation (c) and the fitting accuracy (d) for each fitting model. Blue crosses indicate results obtained using Lorentzian fitting, green triangles correspond to Voigt fitting, and red circles represent results obtained using the dip–peak fitting model. The effective measurement times for panels (c, d) are 15 min for Lorentzian and Voigt fitting, and 1.5 min for the dip–peak fitting model.

To determine the microwave power suitable for temperature measurements when using the dip–peak fitting, we investigated the dependence on microwave power using nine cw-ODMR spectra measured at different microwave powers[Fig.5(a)]. The shot-noise-limited sensitivity is given by the following expression, asμ=1(slope)max​cT​N\mu=\frac{1}{(\text{slope})_{\text{max}}c_{T}\sqrt{N}}(15)

Where(slope)max(\text{slope})_{\text{max}}is the maximum slope of the cw-ODMR spectrum andcTc_{T}is the temperature dependence of the zero-field splitting. We calculated the shot-noise-limited sensitivity for both the conventional fitting methods and the dip–peak fitting. For the conventional fitting, the maximum slope of the spectrum in the frequency range from 2840 MHz to 2865 MHz was used, whereas for the dip–peak fitting, the maximum slope in the frequency range from 2865 MHz to 2870 MHz was employed.

The minimum shot-noise-limited sensitivity was found
to be comparable between the conventional methods and
the dip–peak fitting, with a minimum value of
approximately 5K/Hz\mathrm{K}/\sqrt{\mathrm{Hz}}for a single particle[Fig.5(b)]. However, the microwave power corresponding to the minimum sensitivity differed between the two approaches. For the dip–peak fitting, the minimum sensitivity was obtained at a microwave power corresponding to a cw-ODMR contrast of approximately 5% (ON/OFF), whereas for the conventional methods it occurred at approximately 10%. These results suggest that, under low microwave power conditions, the dip–peak fitting has the potential to achieve higher measurement precision than the conventional fitting approaches.

Using the same procedure as described in the previous section, we experimentally evaluated the statistical variation of the resonance frequency and the fitting precision using ensemble cw-ODMR spectra composed of 100 bright spots[Fig.5(c,d)]. The results indicate that high-precision determination of the resonance frequency is maintained over a wide range of microwave excitation strengths, with the highest precision achieved when the maximum cw-ODMR contrast is approximately 5% (ON/OFF), which is consistent with the trend predicted from the shot-noise-limited sensitivity analysis.

To further quantify the performance, we compared the experimentally observed temperature variation with the shot-noise-limited uncertainty.
For the conventional fitting method, although the effective acquisition time is approximately 900 s, the experimentally observed temperature variation is about 25 times larger than the shot-noise limit. This indicates that the measurement operates far from the fundamental noise limit.
In contrast, for the dip–peak fitting, with an effective acquisition time of only 90 s, the experimentally observed variation is approximately 10 times larger than the shot-noise limit. Thus, the dip–peak fitting operates substantially closer to the shot-noise-limited regime despite the shorter acquisition time.

These results demonstrate that, when using the dip–peak fitting, the optimal measurement condition corresponds to a maximum cw-ODMR contrast of approximately 5% (ON/OFF).
This value is lower than the contrast of approximately 10% predicted from the shot-noise limit as optimal when using conventional fitting methods, indicating that experiments employing dip–peak fitting can be performed at lower microwave power.
Because reducing the microwave power significantly suppresses heating from the microwave coil, the dip–peak fitting provides a highly advantageous approach for practical temperature measurements.
Furthermore, comparison with the shot-noise-limited sensitivity reveals that the experimentally observed temperature variation using dip–peak fitting is approximately ten times the shot-noise limit, whereas the conventional approach remains about twenty-five times above this fundamental bound. These results demonstrate that dip–peak fitting enables operation significantly closer to the shot-noise-limited regime while reducing microwave power.

## IV.4Temperature dependence of resonance frequency

We further investigated whether the resonance frequencies obtained using the dip–peak fitting exhibit the same temperature dependence as those obtained using conventional fitting methods when the temperature of FNDs was varied [Fig.6]. The resonance frequency obtained using the dip–peak fitting shifts with temperature in a manner consistent with that obtained using conventional fitting approaches.Figure 6:(a, b) Temperature dependence of the cw-ODMR spectra.
(c) Temperature dependence of the resonance frequency obtained by fitting the cw-ODMR spectra using a Lorentzian function (blue crosses), a Voigt function (green triangles), and the dip–peak fitting model (red circles).

From these results, we conclude that the dip–peak fitting provides a reliable method for identifying the resonance frequency from cw-ODMR spectra for temperature-sensing applications. Compared with conventional fitting methods, the dip–peak fitting enables higher-precision determination of the resonance frequency within a shorter measurement time and operates effectively under lower microwave power conditions.

## VCONCLUSION

In this study, we analytically clarified the physical origin of the dip–peak fitting method, a practical approach for modeling peak-like features observed within the dip near the resonance frequency in ensemble cw-ODMR spectra. By expressing the ensemble cw-ODMR spectrum as a convolution of single-NV spectra and transforming it analytically, we demonstrate that the spectral response around the resonance can be accurately described by a single Lorentzian function with a background term. This establishes a clear physical foundation for dip–peak fitting.

We further validate the effectiveness of this method experimentally. Compared with conventional fitting approaches, dip–peak fitting provides a more accurate description of the ODMR lineshape near resonance. Importantly, it enables more precise determination of the resonance frequency within a shorter measurement time, achieving an improvement in precision by approximately a factor of 1.6 under identical acquisition conditions. In addition, this method allows for more reliable estimation of confidence intervals based on fitting uncertainties, which has been difficult to achieve with conventional methods.

We find that dip–peak fitting maintains high accuracy over a wide range of microwave excitation strengths, with optimal performance achieved at lower microwave powers, corresponding to a contrast of approximately 5%. Despite the reduced excitation strength, the temperature fluctuations measured using dip–peak fitting reach within a factor of  10 of the shot-noise limit, whereas conventional methods remain at  25 times the limit. Notably, both methods capture consistent temperature variations, confirming the reliability of dip–peak fitting.

Overall, dip–peak fitting provides a simple yet physically grounded and experimentally robust method for extracting resonance frequencies from cw-ODMR spectra. Its ability to achieve high precision with reduced microwave power and shorter acquisition time makes it particularly promising for high-accuracy temperature sensing using fluorescent nanodiamonds. This approach is expected to enable high-precision temperature measurements at the nanoscale.

## Acknowledgements.We would like to acknowledge Dr. Hitoshi Ishida for his support in mathematics, and Dr. Hiroshi Abe and Dr. Takeshi Ohshima for the fabrication of FNDs. This work was supported by Early-Career Scientists (19K16089 and 21K15053 to S.S.), Toyota Riken Scholar Program (to S.S.), Kyoto Technoscience Center (to S.S.), JST-FOREST Program (JPMJFR2428 to S.S.), JSPS KAKENHI (22H02583 and 24H02306 to Y.H., and 25K08446 to K.F.), MEXT Q-LEAP (JPMXS0120330644 to Y.H.), and JST CREST (JPMJCR24B6 to Y.H.)

## Appendix AMonte Carlo simulations

We perform Monte Carlo simulations of an ensemble of NV centers following the approach of Ref.[25,11].
The Hamiltonian of the NV center is described asH\displaystyle H=\displaystyle=D​(T)​Sz2+E1​(Sx2−Sy2)\displaystyle D(T)S_{z}^{2}+E_{1}\left(S_{x}^{2}-S_{y}^{2}\right)(17)+E2​(Sx​Sy+Sy​Sx)+λ​cos⁡(ω​t)​Sx\displaystyle+E_{2}\left(S_{x}S_{y}+S_{y}S_{x}\right)+\lambda\cos(\omega t)\,S_{x}

Applying the unitary transformationU=e−i​ω​Sz2​tU=e^{-i\omega S_{z}^{2}t}, the Hamiltonian in the rotating frame is written asH′\displaystyle H^{\prime}=\displaystyle=(D−ω)​Sz2+E1​(Sx2−Sy2)\displaystyle(D-\omega)S_{z}^{2}+E_{1}\left(S_{x}^{2}-S_{y}^{2}\right)(19)+E2​(Sx​Sy+Sy​Sx)+λ2​Sx\displaystyle+E_{2}\left(S_{x}S_{y}+S_{y}S_{x}\right)+\frac{\lambda}{2}S_{x}=\displaystyle=(D−ω)​(|B⟩​⟨B|+|D⟩​⟨D|)\displaystyle(D-\omega)(\Ket{B}\Bra{B}+\Ket{D}\Bra{D})(22)+E1​(|B⟩​⟨B|−|D⟩​⟨D|)\displaystyle+E_{1}(\Ket{B}\Bra{B}-\Ket{D}\Bra{D})+i​E2​(|B⟩​⟨D|−|D⟩​⟨B|)+λ2​Sx\displaystyle+iE_{2}\left(\Ket{B}\Bra{D}-\Ket{D}\Bra{B}\right)+\frac{\lambda}{2}S_{x}

Where|B⟩=(1/2)​(|1⟩+|−1⟩)\Ket{B}=(1/\sqrt{2})\left(\Ket{1}+\Ket{-1}\right), and|D⟩=(1/2)​(|1⟩−|−1⟩)\Ket{D}=(1/\sqrt{2})\left(\Ket{1}-\Ket{-1}\right).
The time evolution of the density matrixρ\rhounder this Hamiltonian is analyzed using the Lindblad master equation to incorporate decoherence effects.d​ρ​(t)d​t\displaystyle\frac{d\rho(t)}{dt}=\displaystyle=−iℏ[H,ρ(t)]+∑j=14γj[2Ljρ(t)Lj†\displaystyle-\frac{i}{\hbar}\bigl[H,\rho(t)\bigr]+\sum_{j=1}^{4}\gamma_{j}[2L_{j}\rho(t)L_{j}^{\dagger}(24)−Lj†Ljρ(t)−ρ(t)Lj†Lj].\displaystyle-L_{j}^{\dagger}L_{j}\rho(t)-\rho(t)L_{j}^{\dagger}L_{j}].

whereL1=|B⟩​⟨D|,L2=|D⟩​⟨B|,L3=|B⟩​⟨0|L_{1}=\Ket{B}\Bra{D},L_{2}=\Ket{D}\Bra{B},L_{3}=\Ket{B}\Bra{0}, andL4=|D⟩​⟨0|L_{4}=\Ket{D}\Bra{0}. The corresponding decay rates are taken asγ1=γ2≡γ\gamma_{1}=\gamma_{2}\equiv\gamma,γ3=γ4≡γrel\gamma_{3}=\gamma_{4}\equiv\gamma_{\text{rel}}Figure 7:Monte Carlo simulation results of cw-ODMR spectra under weak microwave excitation (a) and strong microwave excitation (b). The simulation parameters wereγ=0.076\gamma=0.076MHz,γrel=0.0061\gamma_{\mathrm{rel}}=0.0061MHz,η=0.57\eta=0.57,λ=0.41\lambda=0.41MHz,D0=2869.25D_{0}=2869.25MHz,γD=0.53\gamma_{D}=0.53MHz,γE1=3.90\gamma_{E_{1}}=3.90MHz,E10=−0.34E_{1}^{0}=-0.34MHz, andγE2=3.47\gamma_{E_{2}}=3.47MHz for (a), andγ=0.20\gamma=0.20MHz,γrel=0.012\gamma_{\mathrm{rel}}=0.012MHz,η=0.59\eta=0.59,λ=0.74\lambda=0.74MHz,D0=2869.20D_{0}=2869.20MHz,γD=0.87\gamma_{D}=0.87MHz,γE1=4.32\gamma_{E_{1}}=4.32MHz,E10=−0.21E_{1}^{0}=-0.21MHz, andγE2=3.40\gamma_{E_{2}}=3.40MHz for (b).

By solving this equation, the cw-ODMR spectrum of a single NV center can be described. Furthermore, by solving the equation for a large number of NV centers and statistically averaging the results, the ensemble cw-ODMR spectrum can be obtained. In practice, this ensemble behavior is evaluated using Monte Carlo simulations. In the fitting procedure, the parameters listed in Table I were taken to be common to all NV centers, while the parameters listed in Table II were randomly varied for each NV center. Using this approach, the cw-ODMR spectra were fitted.

The results of this fitting are shown in Fig. 7. The cw-ODMR spectrum is well reproduced by this model, indicating that the essential spectral features are captured by the present description. These results suggest that the ensemble cw-ODMR spectrum arises from the superposition of sharp single-NV cw-ODMR spectra. Furthermore, the spectral variations of the individual single-NV cw-ODMR spectra are governed by fluctuations in the parametersDD,E1E_{1},E2E_{2}, which follow Lorentzian distributions.Table 1:ParameterPhysical meaningγ\gammaDissipation rate between the excited states|B⟩\Ket{B}and|D⟩\Ket{D}γrel\gamma_{\mathrm{rel}}Relaxation rate from the excited states|B⟩\Ket{B}or|D⟩\Ket{D}to the ground state|0⟩\Ket{0}.η\etacw-ODMR detection efficiency, accounting forthe fact that fluorescence can be emittedeven when the system is in the excited-state.λ\lambdaMicrowave drive strength (Rabi frequency)Table 2:ParameterPhysical meaningdistributionDDZero-field splittingLorentzian distribution withcenterD0D_{0}and half widthγD\gamma_{D}E1E_{1}Lattice distortionLorentzian distribution withcenterE10≃0E_{1}^{0}\simeq 0and halfwidthγE1\gamma_{E_{1}}E2E_{2}Lattice distortionLorentzian distribution withcenter 0 and half widthγE2\gamma_{E_{2}}

## Appendix BVisualization of the Lorentzian Approximation

In the main text, we derive the analytical solution in Eq. (8) and present an approximate form described by a single Lorentzian in Eq. (11). Here, we verify the validity of this approximation by plotting both expressions.

To clarify the dependence of the spectral shape on the system parameters, we introduce the dimensionless variablesx=ω−D0γE,g=Γ′γE,λ~=λ′γE,x=\frac{\omega-D_{0}}{\gamma_{E}},\qquad g=\frac{\Gamma^{\prime}}{\gamma_{E}},\qquad\tilde{\lambda}=\frac{\lambda^{\prime}}{\gamma_{E}},(25)

Eq. (8) can be rewritten asP​(x)=\displaystyle P(x)=1−λ~(L(x,0,2+g)−L(x,0,2−g)\displaystyle 1-\tilde{\lambda}\,\Biggl(L(x,0,\sqrt{2}+g)-L(x,0,\sqrt{2}-g)(26)+8​gπ2ℜ[β~1u~+ln(1+u~+1−u~+)])\displaystyle+\frac{8g}{\pi^{2}}\Re\left[\tilde{\beta}\frac{1}{\sqrt{\tilde{u}_{+}}}\ln\left(\frac{1+\sqrt{\tilde{u}_{+}}}{1-\sqrt{\tilde{u}_{+}}}\right)\right]\Biggl)(27)

whereu~+=(x+i​g)2+1,\tilde{u}_{+}=(x+ig)^{2}+1,(28)

andβ~=x+i​g2​i​g​(x2+2−g2+2​i​x​g).\tilde{\beta}=\frac{x+ig}{2ig\left(x^{2}+2-g^{2}+2ixg\right)}.(29)

In this dimensionless representation, the spectral shape is
governed solely by the ratiog=Γ′/γEg=\Gamma^{\prime}/\gamma_{E},
apart from the overall amplitude factorλ~\tilde{\lambda}.
To examine the validity of the Lorentzian approximation,
we compare the analytical expression with the approximate
Lorentzian form for several values ofgg.
As shown in Fig. 8, the approximation accurately reproduces
the spectral feature near the resonance frequencyD0D_{0}over the range0.2<Γ′/γE<0.60.2<\Gamma^{\prime}/\gamma_{E}<0.6.Figure 8:Graphical representation of the analysis results forΓ′/γE\Gamma^{\prime}/\gamma_{E}values of (a) 0.20, (b) 0.25, (c) 0.30, (d) 0.35, (e) 0.40, (f) 0.45, (g) 0.50, and (h) 0.60. The blue solid line represents P in eq 8, and the orange dashed line representsA+B​L​(ω,D0,Γdip)A+B\,L(\omega,D_{0},\Gamma_{\mathrm{dip}})in eq 11.

## Appendix CApplication of Dip–Peak Fitting to Various FNDsFigure 9:Results of dip–peak fitting for 100 nm FNDs with electron irradiation doses of4×1018​cm−24\times 10^{18}~\mathrm{cm^{-2}}(a, f),6×1018​cm−26\times 10^{18}~\mathrm{cm^{-2}}(b, g), and1×1019​cm−21\times 10^{19}~\mathrm{cm^{-2}}(c, h), as well as for commercially available FNDs of 100 nm (d, i) and 40 nm (e, j). (a, b, c, d, e) Black dots represent the experimental cw-ODMR data. The fitting results are shown as red solid lines within the fitting range and as gray solid lines outside the range. Residuals shown below each spectrum correspond to the differences between the experimental data and the fitting curves; those within the fitting range are shown as red dots, while those outside the range are shown as gray dots. (f, g, h, i, j)
Dependence of the resonance-frequency fluctuation on the measurement time, obtained from fitting ensemble cw-ODMR spectra composed of 100 bright spots. Blue crosses indicate results obtained using Lorentzian fitting, green triangles correspond to Voigt fitting, and red circles represent results obtained using the dip–peak fitting model.
The dashed lines represent fits to the resonance-frequency fluctuations obtained using the dip–peak fitting model, assuming a scaling proportional to the inverse square root of the measurement time. The corresponding fitting parameters are indicated in the figure.

To evaluate the applicability of the dip–peak fitting across different FNDs, we investigated its performance not only for the 100 nm FND with an electron irradiation dose of4×1018​cm−24\times 10^{18}\text{cm}^{-2}, which is primarily used in this study, but also for FNDs with different NV center concentrations corresponding to irradiation doses of6×1018​cm−26\times 10^{18}\text{cm}^{-2}and10×1018​cm−210\times 10^{18}\text{cm}^{-2}.
In addition, commercially available 100 nm and 40 nm FNDs were examined [Fig. 9].
For all tested samples, dip–peak fitting consistently enabled faster and more accurate determination of the resonance frequency than conventional methods for cw-ODMR spectra with a contrast of approximately 5%. These results demonstrate the robustness and broad applicability of the dip–peak fitting approach.

## References
- [1]V. M. Acosta, E. Bauch, M. P. Ledbetter, A. Waxman, L.-S. Bouchard, and D. Budker(2010-02)Temperature Dependence of the Nitrogen-Vacancy Magnetic Resonance in Diamond.Physical Review Letters104(7),pp. 070801.External Links:ISSN 0031-9007, 1079-7114,Link,DocumentCited by:§I.
- [2]G. Balasubramanian, I. Y. Chan, R. Kolesov, M. Al-Hmoud, J. Tisler, C. Shin, C. Kim, A. Wojcik, P. R. Hemmer, A. Krueger, T. Hanke, A. Leitenstorfer, R. Bratschitsch, F. Jelezko, and J. Wrachtrup(2008-10)Nanoscale imaging magnetometry with diamond spins under ambient conditions.Nature455(7213),pp. 648–651.External Links:ISSN 0028-0836, 1476-4687,Link,DocumentCited by:§I.
- [3]M. C. Cambria, G. Thiering, A. Norambuena, H. T. Dinani, A. Gardill, I. Kemeny, V. Lordi, Á. Gali, J. R. Maze, and S. Kolkowitz(2023-11)Physically motivated analytical expression for the temperature dependence of the zero-field splitting of the nitrogen-vacancy center in diamond.Physical Review B108(18),pp. L180102.External Links:ISSN 2469-9950, 2469-9969,Link,DocumentCited by:§I.
- [4]S. Chuma, K. Kiyosue, T. Akiyama, M. Kinoshita, Y. Shimazaki, S. Uchiyama, S. Sotoma, K. Okabe, and Y. Harada(2024-05)Implication of thermal signaling in neuronal differentiation revealed by manipulation and measurement of intracellular temperature.Nature Communications15(1),pp. 3473.External Links:ISSN 2041-1723,Link,DocumentCited by:§I,§I.
- [5]M. W. Doherty, N. B. Manson, P. Delaney, F. Jelezko, J. Wrachtrup, and L. C.L. Hollenberg(2013-07)The nitrogen-vacancy colour centre in diamond.Physics Reports528(1),pp. 1–45.External Links:ISSN 03701573,Link,DocumentCited by:§I.
- [6]F. Dolde, H. Fedder, M. W. Doherty, T. Nöbauer, F. Rempp, G. Balasubramanian, T. Wolf, F. Reinhard, L. C. L. Hollenberg, F. Jelezko, and J. Wrachtrup(2011-06)Electric-field sensing using single diamond spins.Nature Physics7(6),pp. 459–463.External Links:ISSN 1745-2473, 1745-2481,Link,DocumentCited by:§I.
- [7]F. Dolde, M. W. Doherty, J. Michl, I. Jakobi, B. Naydenov, S. Pezzagna, J. Meijer, P. Neumann, F. Jelezko, N. B. Manson, and J. Wrachtrup(2014-03)Nanoscale Detection of a Single Fundamental Charge in Ambient Conditions Using the NV - Center in Diamond.Physical Review Letters112(9),pp. 097603.External Links:ISSN 0031-9007, 1079-7114,Link,DocumentCited by:§I.
- [8]M. Fujiwara, A. Dohms, K. Suto, Y. Nishimura, K. Oshimi, Y. Teki, K. Cai, O. Benson, and Y. Shikano(2020-12)Real-time estimation of the optically detected magnetic resonance shift in diamond quantum thermometry toward biological applications.Physical Review Research2(4),pp. 043415.External Links:ISSN 2643-1564,Link,DocumentCited by:§I.
- [9]Á. Gali(2019-11)Ab initiotheory of the nitrogen-vacancy center in diamond.Nanophotonics8(11),pp. 1907–1943.External Links:ISSN 2192-8614, 2192-8606,Link,DocumentCited by:§I.
- [10]A. Gruber, A. Dräbenstedt, C. Tietz, L. Fleury, J. Wrachtrup, and C. V. Borczyskowski(1997-06)Scanning Confocal Optical Microscopy and Magnetic Resonance on Single Defect Centers.Science276(5321),pp. 2012–2014.External Links:ISSN 0036-8075, 1095-9203,Link,DocumentCited by:§I.
- [11]K. Hayashi, Y. Matsuzaki, T. Taniguchi, T. Shimo-Oka, I. Nakamura, S. Onoda, T. Ohshima, H. Morishita, M. Fujiwara, S. Saito, and N. Mizuochi(2018-09)Optimization of Temperature Sensitivity Using the Optically Detected Magnetic-Resonance Spectrum of a Nitrogen-Vacancy Center Ensemble.Physical Review Applied10(3),pp. 034009.External Links:ISSN 2331-7019,Link,DocumentCited by:Appendix A,§I,§I,§III.
- [12]T. Kołodziej, M. Mrózek, S. Sengottuvel, M. J. Głowacki, M. Ficek, W. Gawlik, Z. Rajfur, and A. M. Wojciechowski(2024-07)Multimodal analysis of traction forces and the temperature dynamics of living cells with a diamond-embedded substrate.Biomedical Optics Express15(7),pp. 4024.External Links:ISSN 2156-7085, 2156-7085,Link,DocumentCited by:§I.
- [13]Y. Kubo, F. R. Ong, P. Bertet, D. Vion, V. Jacques, D. Zheng, A. Dréau, J.-F. Roch, A. Auffeves, F. Jelezko, J. Wrachtrup, M. F. Barthe, P. Bergonzo, and D. Esteve(2010-09)Strong Coupling of a Spin Ensemble to a Superconducting Resonator.Physical Review Letters105(14),pp. 140502.External Links:ISSN 0031-9007, 1079-7114,Link,DocumentCited by:§I.
- [14]G. Kucsko, P. C. Maurer, N. Y. Yao, M. Kubo, H. J. Noh, P. K. Lo, H. Park, and M. D. Lukin(2013-08)Nanometre-scale thermometry in a living cell.Nature500(7460),pp. 54–58.External Links:ISSN 0028-0836, 1476-4687,Link,DocumentCited by:§I,§I,§I.
- [15]Y. Lee, K. Kim, D. Kim, and J. S. Lee(2025-04)Organelle-Specific Quantum Thermometry Using Fluorescent Nanodiamonds: Insights into Cellular Metabolic Thermodynamics.Journal of the American Chemical Society147(16),pp. 13180–13189.External Links:ISSN 0002-7863, 1520-5126,Link,DocumentCited by:§I,§I.
- [16]Y. Matsuzaki, H. Morishita, T. Shimooka, T. Tashima, K. Kakuyanagi, K. Semba, W. J. Munro, H. Yamaguchi, N. Mizuochi, and S. Saito(2016-07)Optically detected magnetic resonance of high-density ensemble of NV-{}^{\textrm{-}}centers in diamond.Journal of Physics: Condensed Matter28(27),pp. 275302.External Links:ISSN 0953-8984, 1361-648X,Link,DocumentCited by:§III.
- [17]J. R. Maze, P. L. Stanwix, J. S. Hodges, S. Hong, J. M. Taylor, P. Cappellaro, L. Jiang, M. V. G. Dutt, E. Togan, A. S. Zibrov, A. Yacoby, R. L. Walsworth, and M. D. Lukin(2008-10)Nanoscale magnetic sensing with an individual electronic spin in diamond.Nature455(7213),pp. 644–647.External Links:ISSN 0028-0836, 1476-4687,Link,DocumentCited by:§I.
- [18]T. Mittiga, S. Hsieh, C. Zu, B. Kobrin, F. Machado, P. Bhattacharyya, N. Z. Rui, A. Jarmola, S. Choi, D. Budker, and N. Y. Yao(2018-12)Imaging the Local Charge Environment of Nitrogen-Vacancy Centers in Diamond.Physical Review Letters121(24),pp. 246402.External Links:ISSN 0031-9007, 1079-7114,Link,DocumentCited by:§III.
- [19]R. Schirhagl, K. Chang, M. Loretz, and C. L. Degen(2014-04)Nitrogen-Vacancy Centers in Diamond: Nanoscale Sensors for Physics and Biology.Annual Review of Physical Chemistry65(1),pp. 83–105.External Links:ISSN 0066-426X, 1545-1593,Link,DocumentCited by:§I.
- [20]T. Sekiguchi, S. Sotoma, and Y. Harada(2018)Fluorescent nanodiamonds as a robust temperature sensor inside a single cell.Biophysics and Physicobiology15(0),pp. 229–234.External Links:ISSN 2189-4779,Link,DocumentCited by:§I.
- [21]F. T.-K. So, N. Hariki, M. Nemoto, A. I. Shames, M. Liu, A. Tsurui, T. Yoshikawa, Y. Makino, M. Ohori, M. Fujiwara, E. D. Herbschleb, N. Morioka, I. Ohki, M. Shirakawa, R. Igarashi, M. Nishikawa, and N. Mizuochi(2024-05)Small multimodal thermometry with detonation-created multi-color centers in detonation nanodiamond.APL Materials12(5),pp. 051102.External Links:ISSN 2166-532X,Link,DocumentCited by:§I,§I.
- [22]S. Sotoma, C. Zhong, J. C. Y. Kah, H. Yamashita, T. Plakhotnik, Y. Harada, and M. Suzuki(2021-01)In situ measurements of intracellular thermal conductivity using heater-thermometer hybrid diamond nanosensors.Science Advances7(3),pp. eabd7888.External Links:ISSN 2375-2548,Link,DocumentCited by:§I,§I.
- [23]K. Wu, Q. Lu, Y. Ren, P. Balasubramanian, K. Ebadi Jalal, H. Klug, M. Klein, T. Bohn, T. Bopp, F. Jelezko, Y. Wu, and T. Weil(2026-02)Single‐Cell Hyperthermia: Diamond Quantum Thermometry Reveals Thermal Control of Macrophage Polarization.Advanced Materials38(8),pp. e17076.External Links:ISSN 0935-9648, 1521-4095,Link,DocumentCited by:§I,§I.
- [24]K. Yamamoto, K. Ogawa, M. Tsukamoto, Y. Ashida, K. Sasaki, and K. Kobayashi(2025-02)Nanodiamond quantum thermometry assisted with machine learning.Applied Physics Express18(2),pp. 025001.External Links:ISSN 1882-0778, 1882-0786,Link,DocumentCited by:§I,§I.
- [25]X. Zhu, Y. Matsuzaki, R. Amsüss, K. Kakuyanagi, T. Shimo-Oka, N. Mizuochi, K. Nemoto, K. Semba, W. J. Munro, and S. Saito(2014-04)Observation of dark states in a superconductor diamond quantum hybrid system.Nature Communications5(1),pp. 3524.External Links:ISSN 2041-1723,Link,DocumentCited by:Appendix A.

## 


- 


Major funding support from
