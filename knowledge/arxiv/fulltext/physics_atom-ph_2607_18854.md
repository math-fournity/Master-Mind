# Quantum Dynamics of $H_2^+$ in Orthogonal Two-Color Fields

**arXiv ID**: 2607.18854v1
**Authors**: Jinzhen Zhu
**Published**: 2026-07-21
**Categories**: physics.atom-ph, math-ph, quant-ph
**HTML URL**: https://arxiv.org/html/2607.18854v1

## Abstract

We present full-dimensional quantum simulations of $H_2^+$ dissociative ionization driven by strong orthogonal laser fields. We consider equal-frequency orthogonal components, which generate elliptical or circular polarization depending on their relative phase and amplitude, as well as orthogonal $800$- and $400$-nm two-color fields. These two-dimensional fields strongly modify the fragmentation dynamics. Most notably, we identify a high-energy peak in the proton kinetic-energy-release (KER) spectrum at approximately $4-5$ eV that is absent from the corresponding single-color, linearly polarized calculations. The yield of this peak can be coherently controlled by varying the relative carrier-envelope phase of the perpendicular field component. The perpendicular field also disrupts the clear electron-proton energy-sharing pattern observed in the main $3-3.5$ eV dissociation channel, indicating more complex multichannel dynamics. Time-dependent state projections and calculations initiated from individual excited states attribute the additional peak to laser-induced vibrational excitation of $H_2^+$. Furthermore, the perpendicular field rotates the fragment angular distributions, causing the most probable proton and electron emission directions to deviate substantially from the principal $z$ axis. These findings demonstrate that the spatial and temporal geometry of orthogonal laser fields provides an additional degree of freedom for controlling ultrafast electron-nuclear dynamics.

## Full Text

Quantum Dynamics of 𝐻₂⁺ in Orthogonal Two-Color Fields

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
- License: CC BY-NC-ND 4.0arXiv:2607.18854v1 [physics.atom-ph] 21 Jul 2026

## Quantum Dynamics ofH2+H_{2}^{+}in Orthogonal Two-Color FieldsJinzhen Zhuzhujinzhenlmu@gmail.comPhysics Department, Ludwig Maximilians Universität, D-80333 Munich, GermanyShanghai Artificial Intelligence Laboratory, 129 Longwen Road, Shanghai, China

## Abstract

We present full-dimensional quantum simulations ofH2+H_{2}^{+}dissociative ionization driven by strong orthogonal laser fields.
We consider equal-frequency orthogonal components, which generate elliptical or circular polarization depending on their relative phase and amplitude, as well as orthogonal800800- and400400-nm two-color fields.
These two-dimensional fields strongly modify the fragmentation dynamics. Most notably, we identify a high-energy peak in the proton kinetic-energy-release (KER) spectrum at approximately4−54-5eV that is absent from the corresponding single-color, linearly polarized calculations.
The yield of this peak can be coherently controlled by varying the relative carrier-envelope phase of the perpendicular field component.
The perpendicular field also disrupts the clear electron–proton energy-sharing pattern observed in the main3−3.53-3.5eV dissociation channel, indicating more complex multichannel dynamics.
Time-dependent state projections and calculations initiated from individual excited states attribute the additional peak to laser-induced vibrational excitation ofH2+H_{2}^{+}.
Furthermore, the perpendicular field rotates the fragment angular distributions, causing the most probable proton and electron emission directions to deviate substantially from the principalzzaxis.
These findings demonstrate that the spatial and temporal geometry of orthogonal laser fields provides an additional degree of freedom for controlling ultrafast electron–nuclear dynamics.

## pacs:32.80.-t,32.80.Rm,32.80.Fb††preprint:APS/123-QED

## IIntroduction

The hydrogen molecular ionH2+H_{2}^{+}, the simplest molecule containing one electron and two protons, is a benchmark system for studying molecular dynamics in intense laser fieldsKrausz and Ivanov (2009); Bucksbaumet al.(1990). Its principal fragmentation mechanisms, including dissociative ionization (DI), above-threshold dissociation (ATD), and bond softening (BS), have been investigated extensively in both experiments and theoryGiusti-Suzoret al.(1995); Odenwelleret al.(2011,2014); Wuet al.(2013); Gonget al.(2016). These studies have shown that strong laser fields reshape molecular potential-energy surfaces and thereby control both the fragment kinetic energies and the direction of bond breakingPavičićet al.(2005); Madsenet al.(2012); Scrinzi (2012). A characteristic example is the KER peak near3−43-4eV that is frequently observed whenH2+H_{2}^{+}dissociates in strong infrared fieldsBucksbaumet al.(1990); Wuet al.(2013); Odenwelleret al.(2014); Gonget al.(2016). The initial vibrational state also strongly affects molecular excitation, ionization, and fragmentationKulanderet al.(1996). In particular, fragmentation from excited vibrational states can produce additional features in the KER spectrumZhou and Chu (2005), and excited-state populations can be essential for interpreting the structure of the joint energy spectrum (JES)Yue and Madsen (2014).

More complex laser fields provide additional control over these ultrafast processes. Tailoring the polarization and combining multiple frequencies introduce new degrees of freedom into the laser–molecule interactionPenget al.(2015). Circularly and elliptically polarized fields, for example, can suppress electron recollision with the parent ion and thereby reveal signatures of direct ionization and below-threshold dissociation (BTD) that may be obscured by interference effects in linearly polarized fieldsZnakovskayaet al.(2012). Recent experiments have used different polarization states to measure molecular-frame photoelectron angular distributions (PADs), providing detailed information about molecular electron dynamicsGranadoset al.(2024); Wanget al.(2025a). Two-color fields further enable coherent control through their relative phase, intensity, frequency, and polarizationCharronet al.(1993); Wanget al.(2025b). Such fields can steer electron localization, induce asymmetric bond breaking, and modify dissociation probabilitiesRayet al.(2009); Maet al.(2025); Yue and Madsen (2013,2014). Nevertheless, full-dimensional quantum simulations of phase-dependent fragmentation in orthogonal fields remain challenging because the coupled electron–nuclear motion must be represented in six spatial dimensionsYue and Madsen (2013,2014); Ranitovicet al.(2014).

Here, we present full-dimensional simulations ofH2+H_{2}^{+}dissociative ionization in orthogonal laser fields. A primary800800-nm component is polarized along the molecularzzaxis, while a second800800- or400400-nm component is polarized along the perpendicularxxaxis. We solve the TDSE with the tRecX codeScrinzi (2010); Tao and Scrinzi (2012). Related implementations have been applied to double ionization of heliumScrinzi (2012); Zielinskiet al.(2016); Zhu and Scrinzi (2020), molecular single ionizationMajety and Scrinzi (2015a); Majetyet al.(2015a); Majety and Scrinzi (2015c); Majetyet al.(2015b); Majety and Scrinzi (2015b); Chundayilet al.(2024), and full-dimensionalH2+H_{2}^{+}dynamics in linearly polarized fieldsZhu (2020,2021). We identify an additional proton KER peak at approximately4−54-5eV that is absent from the corresponding single-color calculations. Its yield varies strongly with the relative phase of the perpendicular component, demonstrating coherent control of this fragmentation channel. State-projection analysis and calculations initiated from individual excited states associate the peak with laser-induced vibrational excitation. These results show that orthogonal fields can manipulate correlated electron–nuclear dynamics through both their spatial geometry and their relative phase.

## IIMethods

Atomic units, withℏ=e2=me=4​π​ϵ0≡1\hbar=e^{2}=m_{e}=4\pi\epsilon_{0}\equiv 1, are used unless stated otherwise.
We employ spherical coordinates centered at the midpoint between the two protons.
Rather than using the internuclear vectorR→\vec{R}as a coordinateYue and Madsen (2013,2014); Madsenet al.(2012), we place the protons atr1→\vec{r_{1}}and−r1→-\vec{r_{1}}and denote the electron coordinate byr2→\vec{r_{2}}.
The proton mass is denoted byM=1836M=1836a.u.

## II.1Hamiltonian

The total Hamiltonian is the sum of the electron–proton interactionHE​PH_{EP}and two one-particle Hamiltonians,H=HB=H(+)⊗𝟙+𝟙⊗H(−)+HE​P,H=H_{B}=H^{(+)}\otimes\mathds{1}+\mathds{1}\otimes H^{(-)}+H_{EP},(1)

where𝟙\mathds{1}is the identity operator,H(+)H^{(+)}is the nuclear Hamiltonian, andH(−)H^{(-)}is the electronic Hamiltonian.
We denote the full Hamiltonian in the bound region byHBH_{B}.
After the coordinate transformation, the electronic Hamiltonian isH(−)=−Δ2​m−i​β​A→​(t)⋅▽→,H^{(-)}=-\frac{\Delta}{2m}-\text{i}\beta\vec{A}(t)\cdot\vec{\triangledown},(2)

and the nuclear Hamiltonian isH(+)=−Δ4​M+12​r,H^{(+)}=-\frac{\Delta}{4M}+\frac{1}{2r},(3)

wherem=2​M2​M+1≈1m=\frac{2M}{2M+1}\approx 1is the reduced electron mass andβ=1+MM≈1\beta=\frac{1+M}{M}\approx 1.
The electron–proton interaction isHE​P=−1|r1→+r2→|−1|r1→−r2→|.H_{EP}=-\frac{1}{|\vec{r_{1}}+\vec{r_{2}}|}-\frac{1}{|\vec{r_{1}}-\vec{r_{2}}|}.(4)

## II.2tSurff for dissociative ionization

We calculate the JES using the tSurff method described in Refs.Zhu (2020,2021). The essential elements are summarized here for completeness.

Within the tSurff approximation, all particle interactions are neglected beyond sufficiently large radiiRc(+/−)R_{c}^{(+/-)}. The corresponding asymptotic Hamiltonians areHV(+)=−Δ4​MH_{V}^{(+)}=-\frac{\Delta}{4M}for the nuclei andHV(−)=−Δ2​m−i​β​A→​(t)⋅▽→H_{V}^{(-)}=-\frac{\Delta}{2m}-\text{i}\beta\vec{A}(t)\cdot\vec{\triangledown}for the electron.
The nuclear scattering states satisfyingi​∂tχk1→​(r1→)=HV(+)​χk1→​(r1→)\text{i}\partial_{t}\chi_{\vec{k_{1}}}(\vec{r_{1}})=H_{V}^{(+)}\chi_{\vec{k_{1}}}(\vec{r_{1}})areχk1→​(r1→)=1(2​π)3/2​exp⁡(−i​∫t0tk124​M​𝑑τ)​exp⁡(−i​k1→​r1→),\chi_{\vec{k_{1}}}(\vec{r_{1}})=\frac{1}{(2\pi)^{3/2}}\exp(-\text{i}\int_{t_{0}}^{t}\frac{k_{1}^{2}}{4M}d\tau)\exp(-\text{i}\vec{k_{1}}\vec{r_{1}}),(5)

and the electronic scattering states satisfyingi​∂tχk2→​(r2→)=HV(−)​χk2→​(r2→)\text{i}\partial_{t}\chi_{\vec{k_{2}}}(\vec{r_{2}})=H_{V}^{(-)}\chi_{\vec{k_{2}}}(\vec{r_{2}})areχk2→​(r2→)=1(2​π)3/2​exp⁡(−i​∫t0tk222​m−i​β​A→​(τ)⋅▽→​d​τ)​exp⁡(−i​k2→​r2→),\chi_{\vec{k_{2}}}(\vec{r_{2}})=\frac{1}{(2\pi)^{3/2}}\exp(-\text{i}\int_{t_{0}}^{t}\frac{k_{2}^{2}}{2m}-\text{i}\beta\vec{A}(\tau)\cdot\vec{\triangledown}d\tau)\exp(-\text{i}\vec{k_{2}}\vec{r_{2}}),(6)

where the laser field begins att0t_{0}, whilek1→\vec{k_{1}}andk2→\vec{k_{2}}denote the nuclear and electronic momenta, respectively.

The tSurff surfaces divide configuration space into four regions, denoted byBB,II,DD, andD​IDIin Fig.1. The bound regionBBretains the full Hamiltonian of Eq. (1). In the dissociation and ionization regions, propagation is governed by the single-particle HamiltoniansHD​(r2→,t)=HV(−)​(r2→,t)=−Δ2​m−i​β​A→​(t)⋅▽→H_{D}(\vec{r_{2}},t)=H_{V}^{(-)}(\vec{r_{2}},t)=-\frac{\Delta}{2m}-\text{i}\beta\vec{A}(t)\cdot\vec{\triangledown}(7)

andHI​(r1→,t)=−Δ4​M+12​r1,H_{I}(\vec{r_{1}},t)=-\frac{\Delta}{4M}+\frac{1}{2r_{1}},(8)

respectively, while theD​IDIcontribution is obtained by time integration of the outgoing flux. This partition was introduced for the double ionization of helium in Ref.Scrinzi (2012)and subsequently applied to a two-dimensional model ofH2+\text{H}_{2}^{+}in Ref.Yue and Madsen (2013).Figure 1:Partition of configuration space used for the tSurff propagation of dissociative ionization.BBdenotes the bound region. InDD, the nuclei have crossedRc(+)R_{c}^{(+)}while the electron remains insideRc(−)R_{c}^{(-)}; inII, the electron has crossedRc(−)R_{c}^{(-)}while the nuclei remain insideRc(+)R_{c}^{(+)}. In theD​IDIregion, both the nuclei and the electron have crossed their respective tSurff surfaces. Here,Rc(+)R_{c}^{(+)}andRc(−)R_{c}^{(-)}are the tSurff radii associated withr1=|r1→|r_{1}=|\vec{r_{1}}|andr2=|r2→|r_{2}=|\vec{r_{2}}|, respectively.

For a sufficiently long propagation timeTT, we assume that the asymptotic electronic and nuclear scattering states are disentangled.
Introducing the step functionsΘ1/2(Rc)={0,r1/2<Rc(+/−)1,r1/2≥Rc(+/−),\Theta_{1/2}(R_{c})=\left\{\begin{matrix}0\;,r_{1/2}<R_{c}^{(+/-)}\\
1\;,r_{1/2}\geq R_{c}^{(+/-)},\end{matrix}\right.(9)

the unbound spectra can be written asP​(k1→,k2→)=P​(ϕ1,θ1,k1,ϕ2,θ2,k2)=|b​(k1→,k2→,T)|2.P(\vec{k_{1}},\vec{k_{2}})=P(\phi_{1},\theta_{1},k_{1},\phi_{2},\theta_{2},k_{2})=\left|b(\vec{k_{1}},\vec{k_{2}},T)\right|^{2}.(10)

The scattering amplitudeb​(k1→,k2→,T)b(\vec{k_{1}},\vec{k_{2}},T)isb​(k1→,k2→,T)=∫−∞T[F​(k1→,k2→,t)+F¯​(k1→,k2→,t)]​𝑑tb(\vec{k_{1}},\vec{k_{2}},T)=\int_{-\infty}^{T}[F(\vec{k_{1}},\vec{k_{2}},t)+\bar{F}(\vec{k_{1}},\vec{k_{2}},t)]dt(11)

with two source terms,F​(k1→,k2→,t)=⟨χk2→​(r2→,t)|[HV(−)​(r2→,t),Θ2​(Rc)]|φk1→​(r2→,t)⟩F(\vec{k_{1}},\vec{k_{2}},t)=\langle\chi_{\vec{k_{2}}}(\vec{r_{2}},t)\left|[H_{V}^{(-)}(\vec{r_{2}},t),\Theta_{2}(R_{c})]\right|\varphi_{\vec{k_{1}}}(\vec{r_{2}},t)\rangle(12)

andF¯​(k1→,k2→,t)=⟨χk1→​(r1→,t)|[HV(+)​(r1→,t),Θ1​(Rc)]|φk2→​(r1→,t)⟩.\bar{F}(\vec{k_{1}},\vec{k_{2}},t)=\langle\chi_{\vec{k_{1}}}(\vec{r_{1}},t)\left|[H_{V}^{(+)}(\vec{r_{1}},t),\Theta_{1}(R_{c})]\right|\varphi_{\vec{k_{2}}}(\vec{r_{1}},t)\rangle.(13)

The single-particle wave functionsφk1→​(r2→,t)\varphi_{\vec{k_{1}}}(\vec{r_{2}},t)andφk2→​(r1→,t)\varphi_{\vec{k_{2}}}(\vec{r_{1}},t)satisfyi​dd​t​φk1→​(r2→,t)=HD​(r2→,t)​φk1→​(r2→,t)−Ck1→​(r2→,t)\text{i}\frac{d}{dt}\varphi_{\vec{k_{1}}}(\vec{r_{2}},t)=H_{D}(\vec{r_{2}},t)\varphi_{\vec{k_{1}}}(\vec{r_{2}},t)-C_{\vec{k_{1}}}(\vec{r_{2}},t)(14)

andi​dd​t​φk2→​(r1→,t)=HI​(r1→,t)​φk2→​(r1→,t)−Ck2→​(r1→,t).\text{i}\frac{d}{dt}\varphi_{\vec{k_{2}}}(\vec{r_{1}},t)=H_{I}(\vec{r_{1}},t)\varphi_{\vec{k_{2}}}(\vec{r_{1}},t)-C_{\vec{k_{2}}}(\vec{r_{1}},t).(15)

The source terms are projections of the full wave function onto the asymptotic solutions,Ck1→​(r2→,t)=∫𝑑r1→​χk1→​(r1→,t)¯​[HV(+)​(r1→,t),Θ1​(Rc)]​ψ​(r1→,r2→,t)C_{\vec{k_{1}}}(\vec{r_{2}},t)=\int d\vec{r_{1}}\overline{\chi_{\vec{k_{1}}}(\vec{r_{1}},t)}[H_{V}^{(+)}(\vec{r_{1}},t),\Theta_{1}(R_{c})]\psi(\vec{r_{1}},\vec{r_{2}},t)(16)

andCk2→​(r1→,t)=∫𝑑r2→​χk2→​(r2→,t)¯​[HV(−)​(r2→,t),Θ2​(Rc)]​ψ​(r1→,r2→,t),C_{\vec{k_{2}}}(\vec{r_{1}},t)=\int d\vec{r_{2}}\overline{\chi_{\vec{k_{2}}}(\vec{r_{2}},t)}[H_{V}^{(-)}(\vec{r_{2}},t),\Theta_{2}(R_{c})]\psi(\vec{r_{1}},\vec{r_{2}},t),(17)

with zero initial values. We use equal tSurff radii,Rc(+)=Rc(−)R_{c}^{(+)}=R_{c}^{(-)}. Beyond either surface, all Coulomb interactions involving the outgoing particle are neglected. Previous studies have shown that the resulting spectra become independent ofRcR_{c}when the asymptotic Hamiltonian is used consistently and the wave function is propagated sufficiently long after the pulseZielinskiet al.(2016); Scrinzi (2012). Infinite-range exterior complex scaling (irECS) is used to absorb outgoing fluxScrinzi (2010).

## IIINumerical results

We use the angular basis0≤m1/2≤20\leq m_{1/2}\leq 2and0≤l1/2≤80\leq l_{1/2}\leq 8, consistent with the parameters employed in our previous full-dimensional study of linearly polarized ionizationZhu (2020). The enlarged basis is required by the reduced symmetry of the present orthogonal-field calculations. For comparison, six-dimensional double-emission calculations for helium can exploit axial symmetry and converge withm1/2=0m_{1/2}=0and0≤l1/2≤20\leq l_{1/2}\leq 2Zielinskiet al.(2016).
The cutoff radii areRc(+)=Rc(−)=12.5R_{c}^{(+)}=R_{c}^{(-)}=12.5a.u., corresponding to a maximum internuclear separation ofR=25R=25a.u. and consistent with previous benchmarksYue and Madsen (2013). The wave function is propagated sufficiently long after the pulse to resolve low-energy outgoing contributions. A complete convergence study at the reduced symmetry of the orthogonal field would require substantially greater memory and computational time. Nevertheless, calculations with coarser angular representations reproduce the secondary peak at the same KER. Together with the use of parameters established in the previous linearly polarized study, this indicates that the peak position and the qualitative trends discussed below are numerically stable, although the precise relative yields may retain some basis dependence.

Including nuclear kinetic energy, we obtain a field-free ground-state energy ofE0=−0.592E_{0}=-0.592a.u. and an equilibrium internuclear distance of2.052.05a.u.
When nuclear kinetic energy is excluded, the ground-state energy is−0.597-0.597a.u., in agreement to three decimal places with the fixed-nuclei quantum-chemistry result of Ref.Bressaniniet al.(1997). The corresponding equilibrium distance is1.9971.997a.u., also agreeing to three decimal places with the accurate value reported in Ref.Schaad and Hicks (1970).

## III.1Laser pulses

The peak intensities of thezz- andxx-polarized components areIz=ℰz,02I_{z}=\mathcal{E}_{z,0}^{2}andIx=ℰx,02I_{x}=\mathcal{E}_{x,0}^{2}, respectively, in atomic units. The total field is the superposition of the two orthogonal components,ℰ→​(t)=ℰz​(t)​z^+ℰx​(t)​x^\vec{\mathcal{E}}(t)=\mathcal{E}_{z}(t)\hat{z}+\mathcal{E}_{x}(t)\hat{x}(18)

The components are obtained from their vector potentials throughℰz​(t)=−∂tAz​(t)\mathcal{E}_{z}(t)=-\partial_{t}A_{z}(t)andℰx​(t)=−∂tAx​(t)\mathcal{E}_{x}(t)=-\partial_{t}A_{x}(t), whereAz​(t)=ℰz,0ωz​az​(t)​sin⁡(ωz​t+ϕz,C​E​P)Ax​(t)=ℰz,0ωx​ax​(t)​sin⁡(ωx​t+ϕx,C​E​P)\begin{split}A_{z}(t)=\frac{\mathcal{E}_{z,0}}{\omega_{z}}a_{z}(t)\sin(\omega_{z}t+\phi_{z,CEP})\\
A_{x}(t)=\frac{\mathcal{E}_{z,0}}{\omega_{x}}a_{x}(t)\sin(\omega_{x}t+\phi_{x,CEP})\\
\end{split}(19)

Thezzaxis is aligned with the molecular axis, and thexxaxis is perpendicular to it. For equal frequencies, envelopes, and amplitudes, a relative phase ofπ/2\pi/2or3​π/23\pi/2produces circular polarization; other relative phases or unequal amplitudes produce elliptical polarization. Whenωx≠ωz\omega_{x}\neq\omega_{z}, the field is an orthogonally polarized two-color field rather than a conventional circularly polarized field. We use either acos8\cos^{8}envelope,a​(t)=[cos⁡(tn​τ)]8a(t)=[\cos(\frac{t}{n\tau})]^{8}, or the flat-top envelope defined in Eq.27. Here,nnspecifies the number of optical cycles associated with the full width at half maximum (FWHM).

## III.2Joint energy spectra

The JES of the three outgoing particles is obtained by integrating Eq.10over all angular coordinates,σ​(EN,Ee)=∫𝑑ϕ1​∫𝑑ϕ2​∫𝑑θ1​sin⁡θ1​∫𝑑θ2​sin⁡θ2P​(ϕ1,θ1,4​M×EN,ϕ2,θ2,2​m×Ee),\begin{split}\sigma(E_{N},E_{e})=&\int d\phi_{1}\int d\phi_{2}\int d\theta_{1}\sin\theta_{1}\int d\theta_{2}\sin\theta_{2}\\
&P(\phi_{1},\theta_{1},\sqrt{4M\times E_{N}},\phi_{2},\theta_{2},\sqrt{2m\times E_{e}}),\end{split}(20)

whereENE_{N}is the total kinetic energy of the two protons andEeE_{e}is the electron kinetic energy. The quantityσ​(EN,Ee)\sigma(E_{N},E_{e})is shown in Fig.2and in the subsequent JES plots. The tilted lines overlaid on these spectra follow the energy-conservation conditionEN+Ee=N​ω+E0−UpE_{N}+E_{e}=N\omega+E_{0}-U_{p}(21)

withUp=Az,024​mU_{p}=\frac{A_{z,0}^{2}}{4m}. The lines indicate the energy sharing expected after absorption ofNNphotons, whereE0E_{0}is the molecular ground-state energy. Structure aligned with these lines reflects correlated electron–nuclear emission, as also observed in our previous400400-nm calculationsZhu (2020,2021). Unless stated otherwise, the spectra are normalized for comparison of their shapes and relative peak strengths; no conclusions are drawn from their absolute magnitudes.

Figure2compares the JES obtained with short (22optical cycles) and long (66optical cycles)800800-nm pulses under linear and circular polarization. A distinct energy-sharing pattern is visible in the linearly polarized cases, panels (a) and (c), and becomes sharper for the longer pulse. Under circular polarization, panels (b) and (d), this structure is less clearly resolved. In all four cases, the dominant proton KER lies near2−42-4eV. An additional peak at approximately4−54-5eV appears only in the circularly polarized calculations and is present for both pulse durations.Figure 2:JES ofH2+\text{H}_{2}^{+}dissociative ionization driven by800800-nm,cos8\cos^{8}pulses with a peak intensity of8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}: (a) linearly polarized, FWHM22optical cycles; (b) circularly polarized, FWHM22optical cycles; (c) linearly polarized, FWHM66optical cycles; and (d) circularly polarized, FWHM66optical cycles. The dashed lines show the energy-sharing condition of Eq.21for absorption ofNNphotons.

To test the robustness and controllability of the additional peak, we performed calculations for several perpendicularxx-polarized fields. The primaryzz-polarized pulse was fixed at800800nm,8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}, acos8\cos^{8}envelope with FWHM22optical cycles, and carrier-envelope phaseϕCEO=0\phi_{\text{CEO}}=0. The frequency, intensity, and phase of thexx-polarized control field were varied. We quantify the prominence of the additional channel by the ratio of its peak height to that of the main KER peak,H=max4≤EN<5⁡σ​(EN)max2≤EN<4⁡σ​(EN),σ​(EN)=∫σ​(EN,Ee)​𝑑Ee.H=\frac{\max_{4\leq E_{N}<5}\sigma(E_{N})}{\max_{2\leq E_{N}<4}\sigma(E_{N})},\sigma(E_{N})=\int\sigma(E_{N},E_{e})dE_{e}.(22)

This dimensionless measure compares spectral shapes independently of their overall normalization.

As shown in Fig.3, the relative height of the4−54-5eV peak depends strongly on the phase of the perpendicular field. Every orthogonal-field calculation produces a larger secondary contribution than the single-color, linearly polarized reference (dashed line). For the equal-frequency configuration, the enhancement is largest nearϕCEO=π/2\phi_{\text{CEO}}=\pi/2and3​π/23\pi/2, where the field is circularly polarized, and smallest near0andπ\pi, where the combined field is linearly polarized. Increasing the control-field intensity or reducing its wavelength further enhances the secondary contribution, as illustrated by the red and cyan curves. The corresponding JES are shown in Figs.9,10, and11.

These results may also help interpret the broader experimental KER distribution reported for circular polarization by Odenwelleret al.Odenwelleret al.(2014). Relative to the linearly polarized result, the circularly polarized distribution retains more yield at higher KER and therefore appears flatter. Although the experiment did not resolve a distinct peak at4−54-5eV, the secondary channel found here would enhance this high-energy region and may contribute to the observed broadening. This comparison remains qualitative because the experimental intensity and pulse duration differ from those used in the present calculations.Figure 3:Relative height of the secondary proton KER peak at4−54-5eV with respect to the main peak at2−42-4eV, plotted as a function of the relative phase of the perpendicular field. Thezz-polarized pulse is fixed at800800nm,8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}, with acos8\cos^{8}envelope of FWHM22optical cycles. The dashed line is the single-color, linearly polarized reference. The control-field parameters are800800nm and8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}(green),400400nm and8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}(red), and400400nm and1.6×1014​W/cm21.6\times 10^{14}\ \text{W/cm}^{2}(cyan).

## III.3Population analysis

To investigate the origin of the additional4−54-5eV proton KER peak and exclude an artifact of thecos8\cos^{8}envelope, we repeated the calculation with a flat-top pulse. The pulse has a wavelength of800800nm, a peak intensity of8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}, and a FWHM of66optical cycles. As shown in Fig.4, circular polarization again produces the additional peak, whereas the linearly polarized calculation retains a clear energy-sharing structure.Figure 4:JES ofH2+\text{H}_{2}^{+}dissociative ionization driven by an800800-nm flat-top pulse with FWHM66optical cycles and peak intensity8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}: (a) linear polarization and (b) circular polarization. The dashed lines show the energy-sharing condition of Eq.21.

We calculated the first four excited eigenstates ofH2+\text{H}_{2}^{+}and monitored the magnitudes of their projection amplitudes during linearly and circularly polarized pulses. Figure5shows that circular polarization produces substantially larger projections ontoE2E_{2}andE4E_{4}, indicating more efficient excitation of these states by the perpendicular field component. To determine whether these excited components can generate the secondary peak, we performed additional linearly polarized calculations initiated from each excited state rather than from the ground state. The resulting JES are shown in Fig.6. Calculations initiated fromE2E_{2}andE4E_{4}reproduce the4−54-5eV peak with a strength comparable to that of the main peak near33eV. This state-resolved test links the secondary channel to enhanced excitation ofE2E_{2}andE4E_{4}and is consistent with earlier studies showing that vibrational excitation can strongly modify fragmentation spectraKulanderet al.(1996); Zhou and Chu (2005); Yue and Madsen (2014).

ReferenceZhu (2026)provides a complementary geometric picture for the sudden fragmentation of a single hydrogen-like radial state. In that model, a radial wave functionψv​(r)\psi_{v}(r)is mapped onto a distribution of local fragment energies,Ev​(r)=−12​μ​∇2ψv​(r)ψv​(r)+Qr,E_{v}(r)=-\frac{1}{2\mu}\frac{\nabla^{2}\psi_{v}(r)}{\psi_{v}(r)}+\frac{Q}{r},(23)

whereμ\muis the effective radial mass, the first term is the local quantum kinetic energy, andQ/rQ/ris the repulsive Coulomb energy. The corresponding spectrum is obtained by samplingEv​(r)E_{v}(r)with the three-dimensional radial probability density,Pv​(E)=∫0∞4​π​r2​|ψv​(r)|2​δ​[E−Ev​(r)]​𝑑r.P_{v}(E)=\int_{0}^{\infty}4\pi r^{2}|\psi_{v}(r)|^{2}\delta\!\left[E-E_{v}(r)\right]dr.(24)

The factor4​π​r24\pi r^{2}acts as a geometric filter that connects the spatial structure of the initial state to the KER distribution. Radial nodes generate rapid variations in the curvature term∇2ψv/ψv\nabla^{2}\psi_{v}/\psi_{v}and can therefore redistribute spectral weight toward additional kinetic-energy features.

This radial single-state model is not evaluated directly for the present eigenstates, which contain multiple orbital components and nontrivial angular dependence. It should therefore be regarded as a qualitative analogy rather than a quantitative derivation of the4−54-5eV peak. Nevertheless, it illustrates how the different nodal structures and spatial distributions of excited components can produce fragmentation energies that differ from those of the ground state. Together with the state-projection and excited-state calculations, this picture supports an excitation-assisted origin of the secondary channel. The state-resolved JES also display energy-sharing structures associated with both the main and secondary peaks.Figure 5:Time-dependent magnitudes of the projection amplitudes,|⟨Ev|ψ​(t)⟩||\langle E_{v}|\psi(t)\rangle|, for the first four excited eigenstates ofH2+\text{H}_{2}^{+}. These quantities are used as relative indicators of laser-induced excitation. The molecule is driven by an800800-nm flat-top pulse with peak intensity8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}and FWHM66optical cycles. The upper and lower panels show linear and circular polarization, respectively.Figure 6:JES obtained from calculations initiated in individual excited eigenstates: (a)E1E_{1}, (b)E2E_{2}, (c)E3E_{3}, and (d)E4E_{4}. A linearly polarized800800-nm flat-top pulse is applied along thezzaxis, with peak intensity8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}and FWHM66optical cycles. The dashed lines show the energy-sharing condition of Eq.21.

## III.4Angular distribution

We finally examine how the perpendicular field modifies the proton and electron angular distributions. The distributions are projected onto thex​zxzplane, perpendicular to the laser-propagation directionyy, by integrating over the remaining momentum coordinates as in Refs.Zhu (2020,2021). Starting from the six-dimensional probability distributionP​(k1→,k2→)P(\vec{k_{1}},\vec{k_{2}})of Eq.10, the proton distribution ispN​(θ,E)={∫𝑑k2→​P​(0,θ,8​M​E,k2→),0≤θ<π∫𝑑k2→​P​(π,2​π−θ,8​M​E,k2→),π≤θ<2​π}p_{N}(\theta,E)=\left\{\begin{matrix}\int d\vec{k_{2}}P(0,\theta,\sqrt{8ME},\vec{k_{2}}),0\leq\theta<\pi\\
\int d\vec{k_{2}}P(\pi,2\pi-\theta,\sqrt{8ME},\vec{k_{2}}),\pi\leq\theta<2\pi\end{matrix}\right\}(25)

and the electron distribution ispe​(θ,E)={∫𝑑k1→​P​(k1→,0,θ,2​m​E),0≤θ<π∫𝑑k1→​P​(k1→,π,2​π−θ,2​m​E),π≤θ<2​π}p_{e}(\theta,E)=\left\{\begin{matrix}\int d\vec{k_{1}}P(\vec{k_{1}},0,\theta,\sqrt{2mE}),0\leq\theta<\pi\\
\int d\vec{k_{1}}P(\vec{k_{1}},\pi,2\pi-\theta,\sqrt{2mE}),\pi\leq\theta<2\pi\end{matrix}\right\}(26)

Here,EEdenotes the kinetic energy of an individual proton or electron rather than the total nuclear KER.

Figure7compares the angular distributions produced by linearly and circularly polarized800800-nm,cos8\cos^{8}pulses with peak intensity8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}and FWHM66optical cycles. Under linear polarization, both protons and electrons are emitted preferentially along thezzaxis. Circular polarization rotates and broadens the distributions, producing substantial emission toward both positive and negativexx. No clear preference between the twoxxdirections remains for either particle. Thus, for the long pulses considered here, the relative phase has little influence on directional asymmetry.

For the shorter pulses with FWHM22optical cycles, the angular distributions depend strongly on the relative phase, as shown in Fig.8. Changing the phase of thexx-polarized component rotates the preferred emission direction from quadrants in which thexxandzzcomponents have the same sign to quadrants in which they have opposite signs. The relative phase of the orthogonal field can therefore steer the fragment emission direction.Figure 7:Logarithmic angular probability distributions forH2+\text{H}_{2}^{+}dissociative ionization driven by800800-nm,cos8\cos^{8}pulses with peak intensity8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}and FWHM66optical cycles. The upper and lower rows correspond to linear and circular polarization, respectively; the left and right columns show protons and electrons. The radial coordinateE1/2E_{1/2}is the individual-fragment kinetic energy. Arrows indicate the directions ofEz​(t)E_{z}(t)andEx​(t)E_{x}(t). Each distribution is normalized to its maximum.Figure 8:Logarithmic fragment angular distributions forcos8\cos^{8}pulses with FWHM22optical cycles and peak intensity8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}in each component. The top row is the single-color,zz-polarized reference. The remaining rows use equal-frequency orthogonal components with relative phases0,π/2\pi/2,π\pi, and3​π/23\pi/2. Other definitions are as in Fig.7.

## IVConclusions and discussion

We have presented full-dimensional quantum simulations ofH2+H_{2}^{+}dissociative ionization in strong orthogonal laser fields. The central result is an additional proton KER peak at approximately4−54-5eV that is absent from the corresponding single-color, linearly polarized calculations. The perpendicular field enhances excitation of specific molecular eigenstates, particularlyE2E_{2}andE4E_{4}, and calculations initiated from these states reproduce the secondary peak. This evidence associates the new channel with laser-induced vibrational excitation.

The relative yield of the secondary peak can be controlled through the phase, frequency, and intensity of the perpendicular field. Orthogonal fields also weaken the simple electron–nuclear energy-sharing pattern observed under linear polarization and steer both proton and electron emission away from the principalzzaxis. These results demonstrate that the spatial geometry and relative phase of a multidimensional field provide effective control parameters for correlated electron–nuclear fragmentation dynamics.

## Acknowledgments

The author thanks Prof. Armin Scrinzi for suggesting the investigation of vibrational excitation and for fruitful discussions that helped clarify the mechanism underlying the secondary KER peak.

## Appendix AFlat-top pulse shapea​(t)=fn2​τ,(n2+1)​τ​(−t)​fn2​τ,(n2+1)​τ​(t),−(1+n2)​τ≤t≤(1+n2)a(t)=f_{\frac{n}{2}\tau,(\frac{n}{2}+1)\tau}(-t)f_{\frac{n}{2}\tau,(\frac{n}{2}+1)\tau}(t),-(1+\frac{n}{2})\tau\leq t\leq(1+\frac{n}{2})(27)

with truncation functionfα,β(r):={1r<α2(α−β)3​(r−β)2​(r−3​α−β2)α≤r<β0r≥βf_{\alpha,\beta}(r):=\left\{\begin{matrix}1&r<\alpha\\
\frac{2}{(\alpha-\beta)^{3}}(r-\beta)^{2}(r-\frac{3\alpha-\beta}{2})&\alpha\leq r<\beta\\
0&r\geq\beta\end{matrix}\right.(28)

## Appendix BJoint energy spectraFigure 9:JES for orthogonal800800-nm (zz-polarized) and400400-nm (xx-polarized)cos8\cos^{8}pulses, each with peak intensity8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}. The relative phases of the400400-nm component are (a)0, (b)π/2\pi/2, (c)π\pi, and (d)3​π/23\pi/2. The dashed lines show the energy-sharing condition of Eq.21.Figure 10:JES for an800800-nm,zz-polarized pulse with peak intensity8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}and an orthogonal400400-nm,xx-polarized pulse with peak intensity1.6×1014​W/cm21.6\times 10^{14}\ \text{W/cm}^{2}. Both pulses havecos8\cos^{8}envelopes. The relative phases of the400400-nm component are (a)0, (b)π/2\pi/2, (c)π\pi, and (d)3​π/23\pi/2. The dashed lines show the energy-sharing condition of Eq.21.Figure 11:JES for orthogonalzz- andxx-polarized800800-nm pulses withcos8\cos^{8}envelopes and peak intensity8×1013​W/cm28\times 10^{13}\ \text{W/cm}^{2}in each component. The relative phases of thexx-polarized component are (a)0, (b)π/2\pi/2, (c)π\pi, and (d)3​π/23\pi/2. The dashed lines show the energy-sharing condition of Eq.21.

## References
- D. Bressanini, M. Mella, and G. Morosi (1997)Nonadiabatic wavefunctions as linear expansions of correlated exponentials. A quantum Monte Carlo application to H+2 and Ps2.Chem. Phys. Lett.272(5-6),pp. 370–375.External Links:Document,ISSN 00092614Cited by:§III.
- P. H. Bucksbaum, A. Zavriyev, H. G. Muller, and D. W. Schumacher (1990)Softening of the H2+ molecular bond in intense laser fields.Phys. Rev. Lett.64(16),pp. 1883–1886.External Links:Document,ISSN 00319007Cited by:§I.
- E. Charron, A. Giusti-Suzor, and F. H. Mies (1993)Two-color coherent control of H2+ photodissociation in intense laser fields.Physical Review Letters71(5),pp. 692–695.External Links:Document,ISSN 00319007Cited by:§I.
- H. Chundayil, V. P. Majety, and A. Scrinzi (2024)The hybrid anti-symmetrized coupled channels method (haCC) for the tRecX code.Computer Physics Communications303(109279),pp. 1–12.External Links:Document,ISSN 00104655Cited by:§I.
- A. Giusti-Suzor, F. H. Mies, L. F. DiMauro, E. Charron, and B. Yang (1995)Dynamics of H2+ in intense laser fields.J. Phys. B At. Mol. Opt. Phys.28(3),pp. 309.External Links:Document,ISSN 0953-4075Cited by:§I.
- X. Gong, P. He, Q. Song, Q. Ji, K. Lin, W. Zhang, P. Lu, H. Pan, J. Ding, H. Zeng, F. He, and J. Wu (2016)Pathway-resolved photoelectron emission in dissociative ionization of molecules.Optica3(6),pp. 643.External Links:Document,ISSN 2334-2536Cited by:§I.
- C. Granados, E. G. Neyra, L. Rebón, and M. F. Ciappina (2024)Above-threshold ionization by polarization-crafted pulses.The European Physical Journal D78(9),pp. 115.External Links:Document,ISSN 1434-6079,LinkCited by:§I.
- F. Krausz and M. Ivanov (2009)Attosecond physics.Reviews of Modern Physics81(1),pp. 163–234.External Links:Document,ISSN 15390756Cited by:§I.
- K. C. Kulander, F. H. Mies, and K. J. Schafer (1996)Model for studies of laser-induced nonlinear processes in molecules.Phys. Rev. A - At. Mol. Opt. Phys.53(4),pp. 2562–2570.External Links:Document,ISSN 10941622Cited by:§I,§III.3.
- J. Ma, C. Jia, T. Xu, S. Pei, Y. Tang, H. Ju, X. Hu, Y. Wu, and J. Wang (2025)Coherent and incoherent control of ionization-fragmentation dynamics in H 2 driven by a two-color laser field.Physical Review A112(1),pp. 013120.External Links:Document,ISSN 2469-9926Cited by:§I.
- C. B. Madsen, F. Anis, L. B. Madsen, and B. D. Esry (2012)Multiphoton above threshold effects in strong-field fragmentation.Phys. Rev. Lett.109(16),pp. 163003.External Links:Document,ISSN 00319007Cited by:§I,§II.
- V. P. Majety and A. Scrinzi (2015a)Dynamic Exchange in the Strong Field Ionization of Molecules.Phys. Rev. Lett.115(10),pp. 1–5.External Links:Document,ISSN 10797114Cited by:§I.
- V. P. Majety and A. Scrinzi (2015b)Static field ionization rates for multi-electron atoms and small molecules.J. Phys. B48(24),pp. 245603.External Links:Document,ISSN 13616455,LinkCited by:§I.
- V. P. Majety, A. Zielinski, and A. Scrinzi (2015a)Mixed gauge in strong laser-matter interaction.J. Phys. B48(2),pp. 025601.External Links:Document,ISSN 13616455Cited by:§I.
- V. P. Majety, A. Zielinski, and A. Scrinzi (2015b)Photoionization of few electron systems: A hybrid coupled channels approach.New J. Phys.17(6),pp. 63002.External Links:Document,ISSN 13672630,LinkCited by:§I.
- V. Majety and A. Scrinzi (2015c)Photo-Ionization of Noble Gases: A Demonstration of Hybrid Coupled Channels Approach.Photonics2(1),pp. 93–103.External Links:Document,ISSN 2304-6732,LinkCited by:§I.
- M. Odenweller, J. Lower, K. Pahl, M. Schütt, J. Wu, K. Cole, A. Vredenborg, L. P. Schmidt, N. Neumann, J. Titze, T. Jahnke, M. Meckel, M. Kunitski, T. Havermeier, S. Voss, M. Schöffler, H. Sann, J. Voigtsberger, H. Schmidt-Böcking, and R. Dörner (2014)Electron emission from H 2 + in strong laser fields.Phys. Rev. A - At. Mol. Opt. Phys.89(1),pp. 1–12.External Links:Document,ISSN 10502947Cited by:§I,§III.2.
- M. Odenweller, N. Takemoto, A. Vredenborg, K. Cole, K. Pahl, J. Titze, L. P. H. Schmidt, T. Jahnke, R. Dörner, and A. Becker (2011)Strong field electron emission from fixed in space H2+ ions.Phys. Rev. Lett.107(14),pp. 1–4.External Links:Document,ISSN 00319007Cited by:§I.
- D. Pavičić, A. Kiess, T. W. Hänsch, and H. Figger (2005)Intense-laser-field ionization of the hydrogen molecular ions H 2+ and D2+ at critical internuclear distances.Phys. Rev. Lett.94(16),pp. 1–4.External Links:Document,ISSN 00319007Cited by:§I.
- P. Peng, S. Peng, H. Hu, N. Li, Y. Bai, P. Liu, H. Xu, R. Li, and Z. Xu (2015)Intensity-dependent study of strong-field Coulomb explosion of H_2.Optics Express23(14),pp. 18763.External Links:Document,ISSN 10944087Cited by:§I.
- P. Ranitovic, C. W. Hogle, P. Rivière, A. Palacios, X. M. Tong, N. Toshima, A. González-Castrillo, L. Martin, F. Martín, M. M. Murnane, and H. Kapteyn (2014)Attosecond vacuum UV coherent control of molecular dynamics.Proceedings of the National Academy of Sciences of the United States of America111(3),pp. 912–917.External Links:Document,ISSN 00278424Cited by:§I.
- D. Ray, F. He, S. De, W. Cao, H. Mashiko, P. Ranitovic, K. P. Singh, I. Znakovskaya, U. Thumm, G. G. Paulus, M. F. Kling, I. V. Litvinyuk, and C. L. Cocke (2009)Ion-energy dependence of asymmetric dissociation of D2 by a two-color laser field.Physical Review Letters103(22),pp. 223201.External Links:Document,ISSN 00319007Cited by:§I.
- L. J. Schaad and W. V. Hicks (1970)Equilibrium bond length in H2+.Vol.53.External Links:Document,ISSN 00219606,LinkCited by:§III.
- A. Scrinzi (2010)Infinite-range exterior complex scaling as a perfect absorber in time-dependent problems.Phys. Rev. A81(5),pp. 053845.External Links:Document,ISBN 1050-2947,ISSN 10502947,LinkCited by:§I,§II.2.
- A. Scrinzi (2012)t -SURFF: fully differential two-electron photo-emission spectra.New J. Phys.14(8),pp. 085008.External Links:Document,ISSN 1367-2630,LinkCited by:§I,§I,§II.2,§II.2.
- L. Tao and A. Scrinzi (2012)Photo-electron momentum spectra from minimal volumes: The time-dependent surface flux method.New J. Phys.14(1),pp. 013021.External Links:Document,ISBN 1367-2630,ISSN 13672630Cited by:§I.
- M. Wang, E. Zhang, Q. Liang, and Y. Liu (2025a)Molecular Alignment Under Strong Laser Pulses: Progress and Applications.Photonics12(5),pp. 422.External Links:Document,ISSN 23046732Cited by:§I.
- S. Wang, B. Liu, and W. Yu (2025b)Photoelectron momentum distributions of hydrogen atoms using parallel two-color chirped laser pulses.Optical Review32(2),pp. 325–334.External Links:Document,ISSN 1349-9432,LinkCited by:§I.
- J. Wu, M. Kunitski, M. Pitzer, F. Trinter, L. P. H. Schmidt, T. Jahnke, M. Magrakvelidze, C. B. Madsen, L. B. Madsen, U. Thumm, and R. Dörner (2013)Electron-nuclear energy sharing in above-threshold multiphoton dissociative ionization of H2.Phys. Rev. Lett.111(2),pp. 1–5.External Links:Document,ISSN 00319007Cited by:§I.
- L. Yue and L. B. Madsen (2013)Dissociation and dissociative ionization of H 2 + using the time-dependent surface flux method.Phys. Rev. A - At. Mol. Opt. Phys.88(6),pp. 1–11.External Links:Document,ISSN 10502947Cited by:§I,§II.2,§II,§III.
- L. Yue and L. B. Madsen (2014)Dissociative ionization of H2+ using intense femtosecond XUV laser pulses.Phys. Rev. A90(6),pp. 063408.External Links:Document,ISSN 10941622Cited by:§I,§I,§II,§III.3.
- Z. Zhou and S. Chu (2005)Exploration of Coulomb explosion dynamics through excited vibrational states of molecules.Phys. Rev. A71(1),pp. 011402(R).External Links:Document,ISSN 1050-2947Cited by:§I,§III.3.
- J. Zhu and A. Scrinzi (2020)Electron double-emission spectra for helium atoms in intense 400-nm laser pulses.Phys. Rev. A101(6),pp. 063407.External Links:Document,ISSN 2469-9926,LinkCited by:§I.
- J. Zhu (2020)Quantum simulation of dissociative ionization of H 2 + in full dimensionality with a time-dependent surface-flux method.Physical Review A102(5),pp. 053109.External Links:Document,ISSN 2469-9926,LinkCited by:§I,§II.2,§III.2,§III.4,§III.
- J. Zhu (2021)Theoretical investigation of the Freeman resonance in the dissociative ionization of H2+.Physical Review A103(1),pp. 013113.External Links:Document,ISSN 24699934,LinkCited by:§I,§II.2,§III.2,§III.4.
- J. Zhu (2026)The 1/3 Geometric Constant: Scale Invariance and the Origin of “Missing Energy” in 3D Quantum Fragmentation.arXiv preprint arXiv:2601.08255.External Links:Document,2601.08255Cited by:§III.3.
- A. Zielinski, V. P. Majety, and A. Scrinzi (2016)Double photoelectron momentum spectra of helium at infrared wavelength.Phys. Rev. A93(2),pp. 1–21.External Links:Document,ISSN 24699934Cited by:§I,§II.2,§III.
- I. Znakovskaya, P. von den Hoff, G. Marcus, S. Zherebtsov, B. Bergues, X. Gu, Y. Deng, M. J. J. Vrakking, R. Kienberger, F. Krausz, R. de Vivie-Riedle, and M. F. Kling (2012)Subcycle Controlled Charge-Directed Reactivity with Few-Cycle Midinfrared Pulses.Physical Review Letters108(6),pp. 63002.External Links:Document,LinkCited by:§I.

## 


- 


Major funding support from
