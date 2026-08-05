# Anomalous Microwave Response in YBCO Resonators beyond the Two-Level-System Model

**arXiv ID**: 2607.27392v1
**Authors**: Kaiwen Zheng, Nathan J. Johnson, Nathan T. Thobaben, Sidharth Duthaluru, Haochen Shen, Denae T. Cherry, David S. Wisbey, Kater W. Murch
**Published**: 2026-07-29
**Categories**: cond-mat.supr-con, cond-mat.mes-hall, quant-ph
**Comments**: 8 pages, 5 figures
**HTML URL**: https://arxiv.org/html/2607.27392v1

## Abstract

We report the microwave response of coplanar-waveguide (CPW) resonators fabricated from $\mathrm{YBa_2Cu_3O_{7-δ}}$ (YBCO) thin films over temperatures from approximately $70~\mathrm{mK}$ to $40~\mathrm{K}$. The resonators exhibit internal quality factors $Q_\mathrm{i}$ in the range of $4\times10^3$ to $10^4$ at 70 mK, which increase to a maximum of approximately $8\times10^3$ to $1.2\times10^4$ near $6~\mathrm{K}$. At low temperatures, both $Q_\mathrm{i}$ and the fractional shift of the resonance frequency $Δf_\mathrm{r}/f_\mathrm{r}$ increases with temperature, qualitatively resembling behavior commonly associated with two-level-system (TLS) defects. However, neither response saturates on the temperature scale set by the resonator frequency, and the loss exhibits no observable microwave-power dependence. We show that low-temperature frequency upturn may be better described by an additional paramagnetic response associated with defect-induced local moments or Andreev bound states, while the low-temperature loss follows an approximately logarithmic temperature dependence whose microscopic origin remains unresolved. These measurements establish the millikelvin performance of patterned YBCO resonators and show that their low-temperature response cannot be understood within the conventional TLS framework alone.

## Full Text

Anomalous Microwave Response in YBCO Resonators beyond the Two-Level-System Model

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.27392v1 [cond-mat.supr-con] 29 Jul 2026\DeclareMathOperator\sgn

sgn

## Anomalous Microwave Response in YBCO Resonators beyond the Two-Level-System ModelKaiwen ZhengDepartment of Physics, Washington University, Saint Louis, MO, USA, 63130.Nathan J. JohnsonDepartment of Physics, Washington University, Saint Louis, MO, USA, 63130.Nathan T. ThobabenDepartment of Electrical Engineering, Saint Louis University, Saint Louis, MO, USA, 63103.Sidharth DuthaluruDepartment of Physics, Washington University, Saint Louis, MO, USA, 63130.Haochen ShenDepartment of Physics, Washington University, Saint Louis, MO, USA, 63130.Denae T. CherryDepartment of Electrical Engineering, Saint Louis University, Saint Louis, MO, USA, 63103.David S. WisbeyDepartment of Electrical Engineering, Saint Louis University, Saint Louis, MO, USA, 63103.Kater W. Murchkatermurch@berkeley.eduDepartment of Physics, Washington University, Saint Louis, MO, USA, 63130.Department of Electrical Engineering and Computer Science, University of California Berkeley, Berkeley, CA, USA, 94720.Department of Physics, University of California Berkeley, Berkeley, CA, USA, 94720.

## Abstract

We report the microwave response of coplanar-waveguide (CPW) resonators fabricated fromYBa2​Cu3​O7−δ\mathrm{YBa_{2}Cu_{3}O_{7-\delta}}(YBCO) thin films over temperatures from approximately70​mK70~\mathrm{mK}to40​K40~\mathrm{K}. The resonators exhibit internal quality factorsQiQ_{\mathrm{i}}in the range of4×1034\times 10^{3}to10410^{4}at 70 mK, which increase to a maximum of approximately8×1038\times 10^{3}to1.2×1041.2\times 10^{4}near6​K6~\mathrm{K}. At low temperatures, bothQiQ_{\mathrm{i}}and the fractional shift of the resonance frequencyΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}increases with temperature, qualitatively resembling behavior commonly associated with two-level-system (TLS) defects. However, neither response saturates on the temperature scale set by the resonator frequency, and the loss exhibits no observable microwave-power dependence. We show that low-temperature frequency upturn may be better described by an additional paramagnetic response associated with defect-induced local moments or Andreev bound states, while the low-temperature loss follows an approximately logarithmic temperature dependence whose microscopic origin remains unresolved. These measurements establish the millikelvin performance of patterned YBCO resonators and show that their low-temperature response cannot be understood within the conventional TLS framework alone.††preprint:APS/123-QED

## IIntroduction

On-chip superconducting microwave resonators are widely used as particle detectors, readout elements for solid-state qubits, and sensitive probes of condensed-matter systems[1,2,3,4,5,6,7]. Their resonance frequency and internal quality factor can be quantitatively related to the reactive and dissipative response of the constituent materials[1,8,9,10]. In resonators fabricated from conventional superconductors, low-temperature frequency shifts and loss are commonly interpreted in terms of two-level-system (TLS) defects in interface dielectric and thermally generated quasiparticles[11,8,12]. This framework has been extensively developed and has helped guide the optimization of superconducting resonator fabrication[12].

The same interpretation may not apply directly when the resonator is fabricated from an unconventional superconductor. Nodal quasiparticles[13], impurity-induced local moments[14,15], surface Andreev bound states[16,17], and other intrinsic responses of the superconducting film can contribute to both the reactive and dissipative microwave response. These contributions may produce temperature dependences that superficially resemble conventional TLS behavior, making it important to distinguish dielectric loss from electrodynamic effects intrinsic to the superconducting film.

Among unconventional superconductors, YBCO has been studied extensively at microwave frequencies, both as a probe of the superconducting pairing symmetry and as a low-loss conductor for operation at elevated cryogenic temperatures[18,13]. More recently, its high critical temperature and resilience to magnetic fields have motivated interest in YBCO for hybrid quantum systems, spin spectroscopy, and other cryogenic microwave devices[19,20,21,22]. These applications require an understanding not only of the intrinsic surface impedance of the material, but also of the loss and dispersion of lithographically patterned planar circuits under their intended operating conditions.

In this work, we characterize CPW resonators fabricated from YBCO thin films over temperatures ranging from 70 mK to 40 K. At higher temperatures,Δ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}andQiQ_{\mathrm{i}}are well described by the expected temperature dependence of the London penetration depth and quasiparticle scattering rate. At low temperatures, however, the response is anomalous. Below approximately 6 K, bothΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}andQiQ_{\mathrm{i}}increase with temperature, qualitatively resembling signatures commonly attributed to TLS defects. We show, however, a conventional TLS interpretation cannot account for the low-temperature behavior:QiQ_{\mathrm{i}}exhibits no observable microwave-power dependence, and bothQiQ_{\mathrm{i}}andΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}persist over a temperature range far above the characteristic scale set by the resonator frequency. Instead, the low-temperatureΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}is consistent with an additional paramagnetic contribution, potentially arising from localized magnetic moments or Andreev bound states in the YBCO film[14,16]. The low-temperature loss follows an approximately logarithmic temperature dependence and is not captured by existing models of either TLS loss or quasiparticle dissipation indd-wave superconductors.

## IIYBCO resonators

The CPW resonators used in this study are fabricated from YBCO films purchased from Ceraco GmbH. The manufacturer designates two film compositions: S-type films are grown with a slight Cu excess, whereas M-type films contain excess Y. These distinct growth conditions may lead to differences in the microwave properties of the patterned devices. We characterize two devices, with chip 1 patterned from an S-type film and chip 2 from an M-type film. Both as-purchased films consist of a 200-nm Au/210-nm YBCO/10-nmCeO2\mathrm{CeO_{2}}/r-plane sapphire stack and haveTc≈87​KT_{\mathrm{c}}\approx 87~\mathrm{K}and residual resistivity ratios∼3\sim 3. Here the Au layer is for protecting the YBCO film from moisture during storage and theCeO2\mathrm{CeO_{2}}buffer improves lattice matching while preventing inter-diffusion between sapphire and YBCO[23,24]. The majority of the Au film is removed with standardKI/I2\mathrm{KI/I_{2}}-based Au etchant, leaving only a few small regions for wire bonding. The YBCO structures are then defined using electron-beam lithography and a wet etch process withH3​PO4\mathrm{H_{3}PO_{4}}diluted with de-ionized water. A concentration of0.5−1%0.5-1\%ofH3​PO4\mathrm{H_{3}PO_{4}}by volume results in an etch rate of∼3\sim 3nm/s.Figure 1:Microwave response of a single resonator.(a) Layout of a single CPW resonator. The microwave signal travels through the feedline capacitively coupled to individual CPW resonators. (b) Typical|S21||S_{21}|vs. frequency of a resonator, measured at−-130 dBm drive power. The red line shows the best fit to the data. (c) The real vs. the imaginary part of the sameS21S_{21}data. The red line shows the best circle fit to the raw data.Figure 2:Characterization of all the resonators.(a) Power dependence ofQiQ_{\mathrm{i}}of all resonators of chip 1 (S-type film) and chip 2 (M-type film). Data points of the same resonator are connected with solid lines. (b) Temperature dependence ofΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}of all resonators measured at -80 dBm. The error bars are smaller than the size of the markers. A temperature-independent offset is added to each resonator for clarity. (c) Temperature dependence ofQiQ_{\mathrm{i}}of all resonators measured at -80 dBm.

The finished device chip contains multiple CPW resonators capacitively coupled to a shared feedline. A representative schematic of a resonator is shown in Fig.1(a). These resonators have resonance frequenciesfrf_{\mathrm{r}}between 4 and 6 GHz. The chip is attached to a Au-plated sample package using GE varnish and is wire bonded to feedlines on a microwave launch board. The package is then attached to an adiabatic demagnetization refrigerator (ADR) with a base temperature of∼65​mK\sim 65~\mathrm{mK}. The input microwave signal travels through a total of 70 dB of attenuation and an infrared filter before reaching the sample. The output signal passes through two circulators and a high-electron-mobility-transistor (HEMT) amplifier before being further amplified at room temperature. Because the measurements span a wide temperature range, stainless steel cables are used between low-temperature stages instead of NbTi or Nb cables to avoid impedance changes associated with superconducting transitions in the microwave line.

Figure1(b, c) shows the transmitted signal near the resonance of a typical resonator at−-120 dBm of drive power. We extract the intrinsic quality factorQiQ_{\mathrm{i}}, the coupling quality factorQcQ_{\mathrm{c}}, andfrf_{\mathrm{r}}by fitting the resonance feature to[25,26]S21=p⋅ei​s−2​π​i​f​ζ​[1−(Ql/|Qc|)⋅ei​ϕ1+2​i​Ql⋅(f/fr−1)],S_{21}=p\cdot e^{is-2\pi if\zeta}\left[1-\frac{\left(Q_{\mathrm{l}}/|Q_{\mathrm{c}}|\right)\cdot e^{i\phi}}{1+2iQ_{\mathrm{l}}\cdot\left(f/f_{\mathrm{r}}-1\right)}\right],(1)

whereffis the frequency being measured,ppis the amplitude of the background,ssis the phase offset of the background,ζ\zetais the phase delay of the background,ϕ\phiis the phase delay caused by the impedance mismatch between the resonator and the feedline, andQl=(Qi−1+Re​{Qc}−1)−1Q_{\mathrm{l}}=\left(Q_{\mathrm{i}}^{-1}+\mathrm{Re}\{Q_{\mathrm{c}}\}^{-1}\right)^{-1}is the loaded quality factor. HereQcQ_{\mathrm{c}}is a complex number to account for the impedance mismatch to prevent overestimating the extractedQiQ_{\mathrm{i}}[25].

When the temperature is fixed at∼70​mK\sim 70~\mathrm{mK}, theQiQ_{\mathrm{i}}of the YBCO resonators on two separate chips are measured to be between4⋅1034\cdot 10^{3}to10410^{4}, consistent with devices fabricated with similar films[22,19,21]. As shown in Fig.2,QiQ_{\mathrm{i}}shows negligible dependence on the microwave drive power up to−-80 dBm. This indicates that the microwave loss of YBCO samples are likely not dominated by TLS loss in spite of a 10 nm thickCeO2\mathrm{CeO_{2}}buffer layer. Despite a lack of power dependence, bothQiQ_{\mathrm{i}}andΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}increase as temperature is increased, qualitatively resembling the behavior caused by TLS defects. At∼6​K\sim 6~\mathrm{K},QiQ_{\mathrm{i}}reaches a maximum of8×1038\times 10^{3}to1.2×1041.2\times 10^{4}among the resonators. As the temperature is further increased, bothQiQ_{\mathrm{i}}andΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}continue to decrease, consistent with the effect of quasiparticle loss[13,27,18].Figure 3:Analysis of the temperature dependence of resonator frequency shift.(a) Temperature dependence ofΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}of a representative resonator fitted to the TLS + quasiparticle model (Eqs.2,3,4,5) and paramagnetic response + quasiparticle model (Eqs.3,5,6). (b) Zoom in plot in the low temperature region revealing the different behavior of the two models.

## IIITemperature dependence of frequency shift

We first analyze the temperature dependence of theΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}in terms of two standard contributions: the dispersive response of a TLS bath at low temperature and the kinetic-inductance shift associated with thermally generated quasiparticles at higher temperature.

At low temperatures,Δ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}increases with temperature. Such an upturn is often associated with the dispersive response of a TLS bath[28,29,8]. Although a TLS interpretation is already disfavored by the absence of measurable power dependence shown in Fig.2, we nevertheless first test whether the low-temperature frequency shift can be described by the standard TLS expression[11,8],(d​frfr)TLS=F​δTLSπRe[Ψ(12+i​h​fr2​π​kB​T)−ln(h​fr2​π​kB​T)],\begin{split}\left(\frac{\mathrm{d}f_{\mathrm{r}}}{f_{\mathrm{r}}}\right)_{\mathrm{TLS}}={}&\frac{F\delta_{\mathrm{TLS}}}{\pi}\operatorname{Re}\Bigg[\Psi\left(\frac{1}{2}+\frac{ihf_{\mathrm{r}}}{2\pi k_{\mathrm{B}}T}\right)\\
&\qquad-\ln\left(\frac{hf_{\mathrm{r}}}{2\pi k_{\mathrm{B}}T}\right)\Bigg],\end{split}(2)

whereF​δTLSF\delta_{\mathrm{TLS}}is the filling-factor adjusted TLS loss tangent,Ψ\Psiis the complex digamma function,hhis Planck’s constant, andkBk_{\mathrm{B}}is the Boltzmann constant.

At high temperatures,Δ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}decreases withTT, consistent with the behavior of thermally generated quasiparticles, which induce a change in the kinetic inductance. We take(d​frfr)qp=Lg′+Lk′​(0)Lg′+Lk′​(T)−C,\left(\frac{\mathrm{d}f_{\mathrm{r}}}{f_{\mathrm{r}}}\right)_{\mathrm{qp}}=\sqrt{\frac{L_{\mathrm{g}}^{\prime}+L_{\mathrm{k}}^{\prime}\left(0\right)}{L_{\mathrm{g}}^{\prime}+L_{\mathrm{k}}^{\prime}\left(T\right)}}-C,(3)

whereLg′L_{\mathrm{g}}^{\prime}is the geometric inductance per unit length of the CPW, andLk′L_{\mathrm{k}}^{\prime}is the kinetic inductance per unit length, andC≈1C\approx 1is a normalization constant that accounts for a small offset in the referencefrf_{\mathrm{r}}. For a CPW structure[30,31],Lk′=G​μ0​λab​(T)​coth⁡([dλab​(T)]),L_{\mathrm{k}}^{\prime}=G\mu_{0}\lambda_{\mathrm{ab}}\left(T\right)\coth{\left[\frac{d}{\lambda_{\mathrm{ab}}\left(T\right)}\right]},(4)

whereGGis a geometric factor dependent on the CPW geometry,μ0\mu_{0}is the vacuum permeability,λab\lambda_{\mathrm{ab}}is the in-plane London penetration depth, andddis the film thickness.

For YBCO with finite impurity scattering, the penetration-depth variation has been described byλab​(T)−λab​(0)∝T2/(T+T∗)\lambda_{\mathrm{ab}}(T)-\lambda_{\mathrm{ab}}(0)\propto T^{2}/(T+T^{*}), whereT∗T^{*}characterizes the crossover from impurity-inducedT2T^{2}behavior at low temperature to approximately linear-TTbehavior at higher temperature[13]. A fit to this equation returnsT∗≫TcT^{*}\gg T_{\mathrm{c}}, we therefore choose to fit to another widely-used phenomenological model[19]λab​(T)=λab​(0)⋅[1+a​(TTc)β],\lambda_{\mathrm{ab}}\left(T\right)=\lambda_{\mathrm{ab}}\left(0\right)\cdot\left[1+a\left(\frac{T}{T_{\mathrm{c}}}\right)^{\beta}\right],(5)

where the exponentβ\betais expected to be around 2.

We fit a representative resonator using the combined TLS + quasiparticle model defined by Eqs.2,3,4, and5, as shown in Fig.3.
Although the model describes the high-TTbehavior well, it fails to reproduce the low-TTfeatures. Specifically, Eq.2predicts that, at a characteristic temperatureT∼h​fr/2​kBT\sim hf_{\mathrm{r}}/2k_{\mathrm{B}}, near-resonant TLSs become thermally saturated, producing an initial dip inΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}. For a TLS bath large enough to produce the observed upturn, the accompanying minimum near100​mK100~\mathrm{mK}would be clearly resolved in our data. Moreover, the curvature of the measured upturn differs substantially from that predicted for a TLS bath.

We next consider mechanisms intrinsic to YBCO that can produce a low-temperature paramagnetic response and thereby account for the discrepancy with the TLS model. Two natural candidates are defect-induced local magnetic moments[14]and Andreev bound states[16,17]near the YBCO surface. Both mechanisms can increase the effective kinetic inductance at low temperature and therefore produce an upturn in the resonance frequency with increasing temperature.

Previous studies have shown that substitution of nonmagnetic ions such as lithium and zinc on Cu sites can induce local magnetic moments that are detectable by nuclear magnetic resonance[32,33,15,34]. Structural defects intrinsic to the thin film may similarly disturb the magnetic correlations of the CuO2planes and generate local moments. These moments produce a Curie-Weiss-like correction to the permeability,μ=μ0​μr\mu=\mu_{0}\mu_{\mathrm{r}},μr=1+cT+θ\mu_{\mathrm{r}}=1+\frac{c}{T+\theta}, whereccdetermines the strength of the paramagnetic response andθ\thetais its characteristic temperature scale. Including this correction modifies Eq.4toLk′=G​μ0​μr​λab​(T)​coth⁡[d​μrλab​(T)].L_{\mathrm{k}}^{\prime}=G\mu_{0}\sqrt{\mu_{\mathrm{r}}}\lambda_{\mathrm{ab}}(T)\coth\left[\frac{d\sqrt{\mu_{\mathrm{r}}}}{\lambda_{\mathrm{ab}}(T)}\right].(6)

A similar low-temperature response can arise from Andreev bound states formed near pair-breaking surfaces or interfaces of YBCO[16,17,35]. In the clean limit, the paramagnetic response of these states produces an effective penetration-depth correction proportional to1/T1/T, with the divergence expected to be cut off at sufficiently low temperature by finite broadening or splitting of the bound states. For small paramagnetic response, localized magnetic moments and Andreev bound states therefore produce corrections proportional to1/(T+θ)1/(T+\theta)and1/T1/T, respectively. The two mechanisms produce qualitatively similar changes in the kinetic inductance and resonance frequency. We therefore do not introduce a separate Andreev bound state fit and instead regard the paramagnetic fit as phenomenologically consistent with contributions from either localized magnetic moments or surface Andreev bound states.

As shown in Fig.3, the model defined by Eqs.3,5,6captures the measured frequency shift over the full temperature range. The fits yieldβ=2.07±0.06\beta=2.07\pm 0.06for chip 1 andβ=2.26±0.04\beta=2.26\pm 0.04for chip 2, consistent with the approximately quadratic temperature dependence reported for YBCO thin films[13,18,19]. The extracted zero-temperature penetration depths areλab​(0)=232±6​nm\lambda_{\mathrm{ab}}(0)=232\pm 6~\mathrm{nm}for chip 1 andλab​(0)=160±9​nm\lambda_{\mathrm{ab}}(0)=160\pm 9~\mathrm{nm}for chip 2. Although the fit supports a low-temperature paramagnetic contribution beyond the standard TLS response, the present data do not distinguish whether it originates from localized magnetic moments or surface Andreev bound states.

## IVTemperature dependence of microwave loss

Similar toΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}},QiQ_{\mathrm{i}}has a temperature dependence that resembles quasiparticle-dominated loss at highTTand TLS-dominated loss at lowTT[28,29,8]. The quasiparticle contribution toQiQ_{\mathrm{i}}is[31]Qqp=2α​μ0​ω​λab2​σ1​[1+2​d/λabsinh⁡(2​d/λab)],Q_{\mathrm{qp}}=\frac{2}{\alpha\mu_{0}\omega\lambda_{\mathrm{ab}}^{2}\sigma_{1}\left[1+\frac{2d/\lambda_{\mathrm{ab}}}{\sinh{\left(2d/\lambda_{\mathrm{ab}}\right)}}\right]},(7)

whereα=Lk′/(Lg′+Lk′)\alpha=L_{\mathrm{k}}^{\prime}/\left(L_{\mathrm{g}}^{\prime}+L_{\mathrm{k}}^{\prime}\right)is the kinetic inductance ratio, andσ1\sigma_{1}is the real part of complex microwave conductivity, which can be described asσ1=nqp​e2m∗⋅τ1+ω2​τ2,\sigma_{1}=\frac{n_{\mathrm{qp}}e^{2}}{m^{*}}\cdot\frac{\tau}{1+\omega^{2}\tau^{2}},(8)

wherenqpn_{\mathrm{qp}}is the quasiparticle density,eeis the electron charge,m∗m^{*}is the effective mass,τ\tauis the quasiparticle scattering time, andω\omegais the angular frequency. Usingλab​(T)\lambda_{\mathrm{ab}}\left(T\right)andLk′L_{\mathrm{k}}^{\prime}extracted from the temperature dependence ofΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}and assuming the high temperatureQiQ_{\mathrm{i}}is limited by quasiparticles, we calculateσ1\sigma_{1}above the inflection point ofQiQ_{\mathrm{i}}. As shown in Fig.4(a),σ1\sigma_{1}falls in the range of106​S/m10^{6}~\mathrm{S/m}and increases with temperature, consistent with previous observations[18,36,27].

Additionally, we attempt to fit the low temperature behavior ofQiQ_{\mathrm{i}}with the TLS modelQTLS\displaystyle Q_{\mathrm{TLS}}=1+⟨np⟩ncF​δTLS⋅tanh⁡((h​fr2​kB​T))\displaystyle=\frac{\sqrt{1+\frac{\left<n_{\mathrm{p}}\right>}{n_{\mathrm{c}}}}}{F\delta_{\mathrm{TLS}}\cdot\tanh{\left(\frac{hf_{\mathrm{r}}}{2k_{\mathrm{B}}T}\right)}}(9)=1F​δTLS′⋅tanh⁡((h​fr2​kB​T)),\displaystyle=\frac{1}{F\delta_{\mathrm{TLS}}^{\prime}\cdot\tanh{\left(\frac{hf_{\mathrm{r}}}{2k_{\mathrm{B}}T}\right)}},(10)

whereQTLSQ_{\mathrm{TLS}}is the TLS contribution toQiQ_{\mathrm{i}},⟨np⟩\left<n_{\mathrm{p}}\right>is the average photon number inside the resonator, andncn_{\mathrm{c}}is the critical photon number for power saturating the TLS. As only negligible power dependence is observed in Fig.2, we do not explicitly fit for⟨np⟩\left<n_{\mathrm{p}}\right>andncn_{\mathrm{c}}and absorb them intoF​δTLS′=F​δTLS1+⟨np⟩/ncF\delta_{\mathrm{TLS}}^{\prime}=\frac{F\delta_{\mathrm{TLS}}}{\sqrt{1+\left<n_{\mathrm{p}}\right>/n_{\mathrm{c}}}}.Figure 4:Analysis of the temperature dependence of the intrinsic quality factor.(a) Effectiveσ1\sigma_{1}of all resonators in the high temperature regime. (b) Temperature dependence ofQiQ_{\mathrm{i}}of a representative resonator at low temperature fitted to Eq.10and11.

We show the low temperatureQiQ_{\mathrm{i}}data of a representative resonator below 6 K and its fit to Eq.10in Fig.4(b). Although the TLS model does predict an increasingQiQ_{\mathrm{i}}with temperature, the resultingQiQ_{\mathrm{i}}fit increases and then begins to saturate within the temperature scale ofh​fr/kBhf_{\mathrm{r}}/k_{\mathrm{B}}, while the measuredQiQ_{\mathrm{i}}continues to increase until∼6​K\sim 6~\mathrm{K}. Notably, the low temperatureQiQ_{\mathrm{i}}data can be well captured by a phenomenological model that scales logarithmically with temperature,QiL​T=A+B⋅ln⁡((T1​K)).Q_{\mathrm{i}}^{LT}=A+B\cdot\ln{\left(\frac{T}{1~\mathrm{K}}\right)}.(11)

Asdd-wave superconductors may have non-negligiblenqpn_{\mathrm{qp}}at low temperatures[13], quasiparticle loss may also dominate the low temperature regime. As neitherλab\lambda_{\mathrm{ab}}nornqpn_{\mathrm{qp}}is expected to have significant temperature dependence at low temperatures, the temperature dependence ofQiQ_{\mathrm{i}}may originate from changes in the quasiparticle scattering timeτ\tau. One possible mechanism that would result in a logarithmic temperature dependence inτ\tauis Kondo scattering[37], which has been observed in cuprates with heavy impurities[38,39,40]. However, previous studies have reportedτ\tauin the range of 1 ps for YBCO[18,36]. This results inω​τ≪1\omega\tau\ll 1, which leads toσ1∝τ\sigma_{1}\propto\tauandQqp∝1/τQ_{\mathrm{qp}}\propto 1/\tau. Typically Kondo scattering would lead to a scattering rate1/τ∝−ln​(T)1/\tau\propto-\mathrm{ln}\left(T\right), which is in the opposite direction from the observed trend. We therefore conclude that Kondo scattering is likely not responsible for the observed logarithmic trend.

## Vdiscussion

Although the microscopic origin of the logarithmic loss remains unknown, it is plausible that it is related to the same low-temperature degrees of freedom responsible for the paramagnetic frequency shift. Both contributions become prominent over a similar temperature range, and magnetic moments or Andreev-bound-state can both in principle produce a dissipative microwave in addition to the reactive response. If the loss and frequency upturn are connected, identifying the origin of the paramagnetic response becomes an important step toward understanding the unresolved dissipative channel.

In the thin film limit (d≪λabd\ll\lambda_{\mathrm{ab}}), Eq.6reduces toLk′≃G​μ0​λab2dL_{\mathrm{k}}^{\prime}\simeq G\mu_{0}\frac{\lambda_{\mathrm{ab}}^{2}}{d}[30], which cancels out theμr\mu_{\mathrm{r}}dependence. In contrast, the paramagnetic response of surface Andreev bound state enters through an additional surface-current response and will persist in the thin-film limit. Measurements of otherwise comparable resonators fabricated from thinner films may therefore help distinguish the two mechanisms. Magnetic-field and microwave-power dependence could provide additional tests. In particular, the microwave drive used in the present measurements is many orders of magnitude weaker than the power scale reported to suppress the Andreev bound state response[35,14]. Consequently, the absence of measurable power dependence in our data does not exclude an Andreev bound state contribution.

Despite the anomalous low-temperature contribution, the resonators reach maximum internal quality factors of approximately7×1037\times 10^{3}to1.7×1041.7\times 10^{4}near 6 to8​K8~\mathrm{K}. These values establish a quantitative loss benchmark for microwave resonators made from high-TcT_{\mathrm{c}}materials. TheseQiQ_{\mathrm{i}}values may enable parametric amplifiers[41], microwave detectors[42], and other superconducting microwave circuits[43]that could benefit from the highTcT_{\mathrm{c}}, highHcH_{\mathrm{c}}, and uniquedd-wave behavior of YBCO.

## VIConclusion

In summary, we characterize CPW resonators fabricated using YBCO thin films from∼70​mK\sim 70~\mathrm{mK}to∼40​K\sim 40~\mathrm{K}. The high temperature response is consistent with the temperature dependence ofλab\lambda_{\mathrm{ab}}andτ\tauexpected fromdd-wave superconductors[13,27,18]. Although bothQiQ_{\mathrm{i}}andΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}qualitatively agree with the behavior expected from the TLS model, their low-temperature trend extends considerably beyond the temperature scale ofh​fr/kBhf_{\mathrm{r}}/k_{\mathrm{B}}expected from a TLS bath. We show that the low temperatureΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}is consistent with a paramagnetic response from dilute magnetic moments or Andreev bound states in the YBCO film[14,16]andQiQ_{\mathrm{i}}follows an approximate logarithmic temperature dependence with unknown microscopic origin. Our work reveals an unresolved low-temperature loss channel in YBCO and show that microwave response from unconventional superconducting films may mimic signatures commonly associated with TLS.

## Acknowledgements.The authors would like to thank Steven Anlage for insightful discussion. This work is supported by the Gordon and Betty Moore Foundation, DOI 10.37807/gbmf11557 and the National Science Foundation award No. 2427093. The authors acknowledge the use of facilities at the Institute of Materials Science and Engineering in Washington University.

## Appendix AEstimation of the penetration depthFigure A1:Estimated penetration depth of all resonators.Estimatedλab​(0)\lambda_{\mathrm{ab}}\left(0\right)vs.frf_{\mathrm{r}}of all measured resonators. Within each chip, the extracted values are consistent across different resonator geometries and frequencies, while a systematic difference is observed between the two chips.

We first extract the expected resonator frequency without any kinetic inductance contributionfsf_{\mathrm{s}}by simulating the resonator structures in ANSYS High Frequency Structure Simulator (HFSS) using the actual device dimensions measured with atomic force microscopy and scanning electron microscopy. Then we estimateLg′L_{\mathrm{g}}^{\prime}by simulating the cross section of the resonators using ANSYS Q3D. Combined with the measuredfrf_{\mathrm{r}},Lk′L_{\mathrm{k}}^{\prime}can be estimated throughLk′=Lg′⋅fs2−fr2fr2.L_{\mathrm{k}}^{\prime}=L_{\mathrm{g}}^{\prime}\cdot\frac{f_{\mathrm{s}}^{2}-f_{\mathrm{r}}^{2}}{f_{\mathrm{r}}^{2}}.(12)

We then estimateGGby sweeping a sheet impedanceω​Lk′/G\omega L_{\mathrm{k}}^{\prime}/Gon the superconducting film and simulating the resonator frequency.

The extractedLk′L_{\mathrm{k}}^{\prime}andGGis then used to fit forλab\lambda_{\mathrm{ab}}. We first seta=c=0a=c=0to obtain a rough estimate ofλab​(0)\lambda_{\mathrm{ab}}\left(0\right). We then fixλab​(0)\lambda_{\mathrm{ab}}\left(0\right)and fitΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}to obtainaa,cc,θ\theta, andnn. We then fit these parameters to extract an updatedλab​(0)\lambda_{\mathrm{ab}}\left(0\right)based onfrf_{\mathrm{r}}measured at∼70​mK\sim 70~\mathrm{mK}. This process is repeated untilλab​(0)\lambda_{\mathrm{ab}}\left(0\right)does not change more than0.1%0.1\%between iterations. The resonators on each chip fall into two designs. Both designs have∼18​μ​m\sim 18~\mathrm{\mu m}trace width but they have a different gap width of either∼14​μ​m\sim 14~\mathrm{\mu m}or∼50​μ​m\sim 50~\mathrm{\mu m}. As shown in Fig.A1, despite the different geometries, our approach is able to find a globalλab​(0)\lambda_{\mathrm{ab}}\left(0\right)across each chip which is dominated by the growth method of the respective film.

## Appendix BFitting results for all resonators

In Tab.B, we summarize the basic parameters of all the resonators measured in this study, fitting parameters obtained by fitting the temperature-dependentΔ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}data to Eqs.3,5,6, and fitting parameters obtained by fitting the low temperatureQiQ_{\mathrm{i}}data to the phenomenological Eq.11.

TABLE A1. Resonator parameters and fit results.ChipRes.frf_{\mathrm{r}}Qi,maxQ_{\mathrm{i,max}}Qi,baseQ_{\mathrm{i,base}}Δ​fr/fr\Delta f_{\mathrm{r}}/f_{\mathrm{r}}fitQiQ_{\mathrm{i}}fit(GHz)aaβ\betacc(K)θ\theta(K)A⋅10−3A\cdot 10^{-3}B⋅10−2B\cdot 10^{-2}11A4.17128986±988986\pm 986003±146003\pm 140.38±0.010.38\pm 0.012.09±0.062.09\pm 0.060.85±0.350.85\pm 0.358.28±2.028.28\pm 2.027.974±0.097.974\pm 0.097.92±0.087.92\pm 0.0811B4.746612974±612974\pm 68809±48809\pm 40.44±0.010.44\pm 0.012.12±0.062.12\pm 0.060.86±0.320.86\pm 0.328.39±1.858.39\pm 1.8511.370±0.00611.370\pm 0.00610.74±0.0510.74\pm 0.0511C4.92797919±227919\pm 225423±105423\pm 100.38±0.010.38\pm 0.012.10±0.062.10\pm 0.060.86±0.360.86\pm 0.368.39±2.118.39\pm 2.116.963±0.0046.963\pm 0.0046.51±0.036.51\pm 0.0311D5.56119817±729817\pm 727060±347060\pm 340.35±0.020.35\pm 0.021.96±0.071.96\pm 0.071.55±0.701.55\pm 0.7010.81±2.6510.81\pm 2.658.700±0.0108.700\pm 0.0106.89±0.106.89\pm 0.1011E5.66836831±136831\pm 134765±54765\pm 50.37±0.010.37\pm 0.012.11±0.062.11\pm 0.060.82±0.330.82\pm 0.338.13±1.978.13\pm 1.975.976±0.0055.976\pm 0.0055.25±0.055.25\pm 0.0522A4.241411052±15211052\pm 1526537±576537\pm 570.55±0.010.55\pm 0.012.20±0.042.20\pm 0.040.63±0.120.63\pm 0.126.22±0.736.22\pm 0.739.25±0.059.25\pm 0.0511.4±0.411.4\pm 0.422B4.844916564±8416564\pm 849996±329996\pm 320.67±0.020.67\pm 0.022.25±0.042.25\pm 0.040.56±0.100.56\pm 0.105.76±0.655.76\pm 0.6513.29±0.0713.29\pm 0.0715.0±0.515.0\pm 0.522C5.01119698±129698\pm 125834±55834\pm 50.53±0.010.53\pm 0.012.24±0.042.24\pm 0.040.56±0.100.56\pm 0.105.92±0.715.92\pm 0.717.74±0.057.74\pm 0.058.9±0.38.9\pm 0.322D5.700812074±23712074\pm 2377838±927838\pm 920.68±0.020.68\pm 0.022.31±0.042.31\pm 0.040.46±0.090.46\pm 0.095.35±0.665.35\pm 0.669.90±0.059.90\pm 0.059.4±0.39.4\pm 0.322E5.77648415±1598415\pm 1595019±735019\pm 730.54±0.160.54\pm 0.162.32±0.052.32\pm 0.050.45±0.090.45\pm 0.095.32±0.735.32\pm 0.736.64±0.046.64\pm 0.047.7±0.37.7\pm 0.3

## References
- Gao [2008]J. Gao,The physics of superconducting microwave
resonators, Ph.D. thesis, California
Institute of Technology (2008).
- Blaiset al.[2021]A. Blais, A. L. Grimsmo,
S. M. Girvin, and A. Wallraff, Circuit quantum electrodynamics,Rev. Mod. Phys.93, 025005 (2021).
- Bøttcheret al.[2024]C. G. L. Bøttcher, N. R. Poniatowski, A. Grankin, M. E. Wesson, Z. Yan, U. Vool, V. M. Galitski, and A. Yacoby, Circuit quantum electrodynamics detection of induced
two-fold anisotropic pairing in a hybrid superconductor–ferromagnet
bilayer,Nature Physics20, 1609 (2024).
- Kreidelet al.[2025]M. Kreidel, J. Ingham,
X. Chu, J. Balgley, T. S. Chung, A. Antony, N. Verma, L. N. Holtzman, K. Barmak, R. Queiroz,
J. Hone, R. M. Westervelt, and K. C. Fong, Observing unconventional superconductivity via kinetic inductance in
weyl semimetal MoTe2(2025),arXiv:2512.24671 [cond-mat.supr-con].
- Zamanet al.[2026]S. Zaman, J. I.-J. Wang,
T. Werkmeister, M. Tanaka, T. Dinh, M. Hays, D. Rodan-Legrain, A. Goswami, R. Assouly,
A. K. Demir, D. K. Kim, B. M. Niedzielski, K. Serniak, M. E. Schwartz, K. Watanabe, T. Taniguchi, P. Kim, R. Comin, J. A. Grover,
T. P. Orlando, P. Jarillo-Herrero, and W. D. Oliver,Kinetic inductance of
few-layer NbSe2in the two-dimensional limit(2026),arXiv:2511.08466
[cond-mat.supr-con].
- Jinet al.[2025]H. Jin, G. Serpico,
Y. Lee, T. Confalone, C. N. Saggau, F. Lo Sardo, G. Gu, B. H. Goodge, E. Lesne, D. Montemurro, K. Nielsch, N. Poccia, and U. Vool, Exploring
van der waals cuprate superconductors using a hybrid microwave circuit,Nano Letters25, 3191 (2025).
- Banerjeeet al.[2025]A. Banerjee, Z. Hao,
M. Kreidel, P. Ledwith, I. Phinney, J. M. Park, A. Zimmerman, M. E. Wesson, K. Watanabe, T. Taniguchi,
R. M. Westervelt,
A. Yacoby, P. Jarillo-Herrero, P. A. Volkov, A. Vishwanath, K. C. Fong, and P. Kim, Superfluid stiffness of twisted trilayer graphene superconductors,Nature638, 93 (2025).
- McRaeet al.[2020]C. R. H. McRae, H. Wang, J. Gao, M. R. Vissers, T. Brecht, A. Dunsworth, D. P. Pappas, and J. Mutus, Materials
loss measurements using superconducting microwave resonators,Review of Scientific Instruments91, 091101 (2020).
- Kreidelet al.[2024]M. Kreidel, X. Chu,
J. Balgley, A. Antony, N. Verma, J. Ingham, L. Ranzani, R. Queiroz, R. M. Westervelt, J. Hone, and K. C. Fong, Measuring
kinetic inductance and superfluid stiffness of two-dimensional
superconductors using high-quality transmission-line resonators,Phys. Rev. Res.6, 043245 (2024).
- Chuet al.[2026]X. Chu, J. Park, J. Balgley, S. Clemons, T. S. Chung, K. Watanabe, T. Taniguchi, L. Ranzani, M. V. Gustafsson, K. C. Fong, and J. Hone, Measuring
reactive-load impedance with transmission-line resonators beyond the
perturbative limit,Phys. Rev. Appl.25, 044071 (2026).
- Mülleret al.[2019]C. Müller, J. H. Cole, and J. Lisenfeld, Towards understanding
two-level-systems in amorphous solids: insights from quantum circuits,Reports on Progress in Physics82, 124501 (2019).
- Crowleyet al.[2023]K. D. Crowley, R. A. McLellan, A. Dutta,
N. Shumiya, A. P. M. Place, X. H. Le, Y. Gang, T. Madhavan, M. P. Bland,
R. Chang, N. Khedkar, Y. C. Feng, E. A. Umbarkar, X. Gui, L. V. H. Rodgers, Y. Jia, M. M. Feldman, S. A. Lyon, M. Liu, R. J. Cava,
A. A. Houck, and N. P. de Leon, Disentangling losses in tantalum
superconducting circuits,Phys. Rev. X13, 041005 (2023).
- Hirschfeld and Goldenfeld [1993]P. J. Hirschfeld and N. Goldenfeld, Effect of strong
scattering on the low-temperature penetration depth of a d-wave
superconductor,Phys. Rev. B48, 4219(R) (1993).
- Prozorov and Giannetta [2006]R. Prozorov and R. W. Giannetta, Magnetic penetration
depth in unconventional superconductors,Superconductor Science and Technology19, R41 (2006).
- Bobroffet al.[1999]J. Bobroff, W. A. MacFarlane, H. Alloul,
P. Mendels, N. Blanchard, G. Collin, and J.-F. Marucco, Spinless impurities in high-Tc{T}_{c}cuprates:
Kondo-like behavior,Phys. Rev. Lett.83, 4381 (1999).
- Barashet al.[2000]Y. S. Barash, M. S. Kalenkov, and J. Kurkijärvi, Low-temperature
magnetic penetration depth in d-wave superconductors: Zero-energy bound state
and impurity effects,Phys. Rev. B62, 6665 (2000).
- Zhuravelet al.[2013]A. P. Zhuravel, B. G. Ghamsari, C. Kurter,
P. Jung, S. Remillard, J. Abrahams, A. V. Lukashenko, A. V. Ustinov, and S. M. Anlage, Imaging the anisotropic nonlinear meissner effect in nodalyba2​cu3​𝐨7−δ{\mathrm{yba}}_{2}{\mathrm{cu}}_{3}{\mathbf{o}}_{7-\delta}thin-film superconductors,Phys. Rev. Lett.110, 087002 (2013).
- Hosseiniet al.[1999]A. Hosseini, R. Harris,
S. Kamal, P. Dosanjh, J. Preston, R. Liang, W. N. Hardy, and D. A. Bonn, Microwave
spectroscopy of thermally excited quasiparticles inYBa2​Cu3​O6.99{\mathrm{YBa}}_{2}{\mathrm{Cu}}_{3}{\mathrm{O}}_{6.99},Phys. Rev. B60, 1349 (1999).
- Velluire-Pellatet al.[2023]Z. Velluire-Pellat, E. Maréchal, N. Moulonguet, G. Saïz, G. C. Ménard, S. Kozlov,
F. Couëdo, P. Amari, C. Medous, J. Paris, R. Hostein, J. Lesueur, C. Feuillet-Palma, and N. Bergeal, Hybrid
quantum systems with high-tct_{\mathrm{c}}superconducting resonators,Scientific Reports13, 14366 (2023).
- Ghirriet al.[2015]A. Ghirri, C. Bonizzoni,
D. Gerace, S. Sanna, A. Cassinese, and M. Affronte, Yba2cu3o7 microwave resonators for strong collective coupling with
spin ensembles,Applied Physics Letters106, 184101 (2015).
- Fohmannet al.[2026]K. Fohmann, T. J. Glebe-Märklin, B. Wilde, M. Kazouini,
C. Schmid, D. Koelle, R. Kleiner, and D. Bothner,Dually tunable ybco
coplanar waveguide resonators based on helium-ion-generated josephson
inductances(2026),arXiv:2605.30425 [quant-ph].
- Duthaluruet al.[2025]S. Duthaluru, K. Zheng,
E. A. Henriksen, and K. W. Murch,Real-time monitoring of
neon film growth for electron-on-neon qubits(2025),arXiv:2511.20765 [quant-ph].
- Denhoff and McCaffrey [1991]M. W. Denhoff and J. P. McCaffrey, EpitaxialY1​Ba2​Cu3​O7\mathrm{Y_{1}Ba_{2}Cu_{3}O_{7}}thin films onCeO2\mathrm{CeO_{2}}buffer layers on
sapphire substrates,Journal of Applied Physics70, 3986 (1991).
- Gaoet al.[1992]J. Gao, B. B. G. Klopman,
W. A. M. Aarnink,
A. E. Reitsma, G. J. Gerritsma, and H. Rogalla, Epitaxial YBa2Cu3Ox thin films on sapphire with a
PrBa2Cu3Ox buffer layer,Journal of Applied Physics71, 2333 (1992).
- Khalilet al.[2012]M. S. Khalil, M. J. A. Stoutimore, F. C. Wellstood, and K. D. Osborn, An analysis method for
asymmetric resonator transmission applied to superconducting devices,Journal of Applied Physics111, 054510 (2012).
- Probstet al.[2015]S. Probst, F. B. Song,
P. A. Bushev, A. V. Ustinov, and M. Weides, Efficient and robust analysis of complex scattering data
under noise in microwave resonators,Review of Scientific Instruments86, 024706 (2015).
- Hirschfeldet al.[1993]P. J. Hirschfeld, W. O. Putikka, and D. J. Scalapino, Microwave conductivity
of d-wave superconductors,Phys. Rev. Lett.71, 3705 (1993).
- w. Andersonet al.[1972]P. w. Anderson, B. I. Halperin, and c. M. Varma, Anomalous low-temperature thermal
properties of glasses and spin glasses,The Philosophical Magazine: A Journal of Theoretical Experimental
and Applied Physics25, 1 (1972),https://doi.org/10.1080/14786437208229210.
- Phillips [1972]W. A. Phillips, Tunneling states in
amorphous solids,Journal of Low Temperature Physics7, 351 (1972).
- López-Núñezet al.[2025]D. López-Núñez, A. Torras-Coloma, Q. Portell-Montserrat, E. Bertoldo, L. Cozzolino,
G. A. Ummarino, A. Zaccone, G. Rius, M. Martínez, and P. Forn-Díaz, Superconducting penetration depth of aluminum thin films,Superconductor Science and Technology38, 095004 (2025).
- Kleinet al.[1990]N. Klein, H. Chaloupka,
G. Müller, S. Orbach, H. Piel, B. Roas, L. Schultz, U. Klein, and M. Peiniger, The effective microwave surface
impedance of high tc thin films,Journal of Applied Physics67, 6940 (1990).
- Wang and Lee [2002]Z. Wang and P. A. Lee, Local moment formation in the
superconducting state of a doped mott insulator,Phys. Rev. Lett.89, 217002 (2002).
- Mahajanet al.[2000]A. V. Mahajan, H. Alloul,
G. Collin, and J. F. Marucco, 89y nmr probe of zn induced local magnetism inYBa2​(Cu1−y​Zny)3​O6+x\mathrm{YBa_{2}(Cu_{1-y}Zn_{y})_{3}O_{6+x}},The European Physical Journal B - Condensed Matter and Complex
Systems13, 457
(2000).
- Bobroffet al.[2001]J. Bobroff, H. Alloul,
W. A. MacFarlane,
P. Mendels, N. Blanchard, G. Collin, and J.-F. Marucco, Persistence of li induced kondo moments in the
superconducting state of cuprates,Phys. Rev. Lett.86, 4116 (2001).
- Zhuravelet al.[2018]A. P. Zhuravel, S. Bae,
S. N. Shevchenko,
A. N. Omelyanchouk,
A. V. Lukashenko,
A. V. Ustinov, and S. M. Anlage, Imaging the paramagnetic nonlinear meissner
effect in nodal gap superconductors,Phys. Rev. B97, 054504 (2018).
- Bonnet al.[1993]D. A. Bonn, R. Liang,
T. M. Riseman, D. J. Baar, D. C. Morgan, K. Zhang, P. Dosanjh, T. L. Duty, A. MacFarlane, G. D. Morris, J. H. Brewer,
W. N. Hardy, C. Kallin, and A. J. Berlinsky, Microwave determination of the quasiparticle scattering
time inYBa2{\mathrm{YBa}}_{2}Cu3{\mathrm{Cu}}_{3}O6.95{\mathrm{O}}_{6.95},Phys. Rev. B47, 11314 (1993).
- Kondo [1964]J. Kondo, Resistance minimum in
dilute magnetic alloys,Progress of Theoretical Physics32, 37 (1964),https://academic.oup.com/ptp/article-pdf/32/1/37/5193092/32-1-37.pdf.
- Sekitaniet al.[2003]T. Sekitani, M. Naito, and N. Miura, Kondo effect in underdoped n-type
superconductors,Phys. Rev. B67, 174503 (2003).
- Rullier-Albenqueet al.[2008]F. Rullier-Albenque, H. Alloul, F. Balakirev, and C. Proust, Disorder, metal-insulator crossover
and phase diagram in high-tc cuprates,Europhysics Letters81, 37008 (2008).
- Rullier-Albenqueet al.[2001]F. Rullier-Albenque, H. Alloul, and R. Tourbot, Disorder and transport in
cuprates: Weak localization and magnetic contributions,Phys. Rev. Lett.87, 157001 (2001).
- Ho Eomet al.[2012]B. Ho Eom, P. K. Day,
H. G. LeDuc, and J. Zmuidzinas, A wideband, low-noise superconducting amplifier
with high dynamic range,Nature Physics8, 623 (2012).
- Dayet al.[2003]P. K. Day, H. G. LeDuc,
B. A. Mazin, A. Vayonakis, and J. Zmuidzinas, A broadband superconducting detector suitable for use in
large arrays,Nature425, 817 (2003).
- Confaloneet al.[2025]T. Confalone, F. Lo Sardo,
Y. Lee, S. Shokri, G. Serpico, A. Coppo, L. Chirolli, V. M. Vinokur, V. Brosco, U. Vool,
D. Montemurro, F. Tafuri, K. Nielsch, G. Haider, and N. Poccia, Cuprate
twistronics for quantum hardware,Advanced Quantum Technologies8, 2500203 (2025).

## 


- 


Major funding support from
