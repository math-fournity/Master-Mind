# Measurement and control of the interaction frequency shift in bosonic optical lattice clocks

**arXiv ID**: 2608.02425v1
**Authors**: J. P. Salvatierra, M. Barbiero, G. Bertaina, D. Calonico, F. Levi, M. G. Tarallo
**Published**: 2026-08-03
**Categories**: physics.atom-ph, quant-ph
**HTML URL**: https://arxiv.org/html/2608.02425v1

## Abstract

We report precise measurements of inter-level interactions in a bosonic optical lattice clock based on $^{88}$Sr atoms. We observe a nonlinear density dependence of the clock shift, even without reaching quantum degeneracy. In a 2D lattice, the Rabi line shape exhibits an interaction sideband consistent with a collective spin model, while in a 1D lattice the shift is modified by density-induced dephasing. These findings, combined with a careful choice of interrogation detuning and atomic density, can enable operation at a net-zero systematic density shift in $^{88}$Sr lattice clocks. We discuss the implications of these findings in many-body physics, quantum simulation, and precision isotope shift measurements, which provide a powerful probe for new physics beyond the Standard Model.

## Full Text

Measurement and control of the interaction frequency shift in bosonic optical lattice clocks

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- 
- License: arXiv.org perpetual non-exclusive licensearXiv:2608.02425v1 [physics.atom-ph] 03 Aug 2026

## Measurement and control of the interaction frequency shift in bosonic optical lattice clocksJ. P. SalvatierraIstituto Nazionale di Ricerca Metrologica, Strada delle Cacce 91, 10135 Torino, ItalyM. BarbieroIstituto Nazionale di Ricerca Metrologica, Strada delle Cacce 91, 10135 Torino, ItalyG. BertainaIstituto Nazionale di Ricerca Metrologica, Strada delle Cacce 91, 10135 Torino, ItalyD. CalonicoF. LeviM. G. Tarallom.tarallo@inrimIstituto Nazionale di Ricerca Metrologica, Strada delle Cacce 91, 10135 Torino, Italy

## Abstract

We report precise measurements of inter-level interactions in a bosonic optical lattice clock based on88Sr atoms. We observe a nonlinear density dependence of the clock shift, even without reaching quantum degeneracy. In a 2D lattice, the Rabi line shape exhibits an interaction sideband consistent with a collective spin model, while in a 1D lattice the shift is modified by density-induced dephasing. These findings, combined with a careful choice of interrogation detuning and atomic density, can enable operation at a net-zero systematic density shift in88Sr lattice clocks. We discuss the implications of these findings in many-body physics, quantum simulation, and precision isotope shift measurements, which provide a powerful probe for new physics beyond the Standard Model.

## Introduction

Optical lattice clocks (OLCs) are currently at the forefront of precision metrology, offering the potential for unprecedented accuracy in timekeeping[1,2]. Their remarkable achievements include pushing the boundaries of measurement precision to the10−1810^{-18}level and beyond[3,4,5], enabling new tests of fundamental physics such as searches for dark matter[6], investigations into the potential variation of fundamental constants[7,8], and relativistic geodesy[9]. These advancements are also pivotal in contributing to the future redefinition of the SI second, moving towards an optical standard[10]. However, significant challenges remain in their development and deployment. Precise mitigation of systematic shifts arising from atom-atom interactions has been theoretically modeled[11]and experimentally achieved in fermionic OLCs[12], while strong s-wave interactions in bosonic species lead to significant density-dependent shifts and decoherence, thereby preventing bosonic clocks from competing with their fermionic counterparts in terms of ultimate accuracy, despite their simpler atomic structure and potentially longer coherence times. However, precise spectroscopy of clock transitions in bosonic isotopes has recently gained interest because of the possibility of probing new long-range interactions beyond the Standard Model by isotope shift spectroscopy[13,14,15].

To overcome the s-wave interaction limit in bosonic OLCs, several technical expedients have been utilized, such as eliminating multiply occupied lattice sites by photoassociation[16], or employing 3D optical lattices with very low average occupation number[17], or both. This results in other systematic shifts, such as those arising from imperfect lattice potentials and their polarization control. Previous experimental measurements of the atom-atom interaction shift on bosonic OLCs, and in particular of the88Sr OLC, have considered only the linear dependence with respect to the number of atoms (or the atomic density)[18,19,20]. However, simple mean-field elastic interaction theory[21,22]of the linear density shift was unable to correctly reproduce the values of the elastic s-wave scattering lengths of the88Sr clock states[23].

The possibility of finding a nonlinear regime in which the effect of interactions can be suppressed or reduced by coherent manipulation of the atomic ensemble considered as a pseudo-spin ensemble has been extensively studied in the framework of atom interferometry[24], mainly in terms of increased atomic coherence.

In this work, we probe the interaction properties of the88Sr lattice clock by precise density shift measurements, also enhancing the interaction in a two-dimensional lattice. We show an optical lattice clock based on bosonic atoms exhibiting a nonlinear clock frequency shift as a function of the number of atoms in each well of the lattice, with a nonlinearity amplified or suppressed by tuning the clock-locking point on the Rabi resonance. The experimental results are analyzed both in terms of unitary many-body and dissipative mean-field theory. The density shift nonlinearity allows the88Sr optical lattice clock to be tuned to a “magic” density at which the collisional shift is canceled.Figure 1:Rabi spectroscopy of interacting bosons in optical lattices. a) Fraction of the atomic population contributing to the spectroscopic signal with a given site occupancymmfor the 1D and 2D lattice configurations forNtot=7×104N_{\text{tot}}=7\times 10^{4}, with a pictorial view of their confinement volumes.
b) Measured Rabi line shapes of the excited fraction forggtoeeinterrogation forNtot=7×104N_{\text{tot}}=7\times 10^{4}atoms, taken in a 1D lattice (orange circles) and in a 2D lattice (blue squares).
While both profiles show a substantial broadening, the 2D profile is clearly asymmetric, revealing a many-body interaction structure. c) The reconstructed resolved atomic interaction sideband is plotted for both lattice topologies. The data from each line shape are collected into bins 3 Hz wide.

## Theory

In essence, the optical lattice clock physical system[2]consists of a series of independent atomic ensembles tightly confined in the maxima or minima, depending on the polarizability of the atom at the trapping frequency, of a periodic potential generated by interfering far-off resonance intense Gaussian laser beams. The number of standing waves employed in the system determines the dimensionality of the resulting lattice[25]. Tuning the trapping laser frequency to cancel the AC Stark shift[26], the tight confinement along the lattice direction suppresses the motional systematic effects[27], while thermal motion in the dimensions transverse to the lattice direction allows the atoms to interact, both elastically and inelastically.

Assuming operation of an optical lattice with negligible tunneling between nearest-neighbor lattice wells, as well as other typical conditions like longitudinal freezing, stationary thermal radial state at temperatureTrT_{r}, weak backaction of spin dynamics on the radial distribution[28], and short radial correlation time compared with the other clock times[11], it is possible to trace over the radial modes and keep only an effective spin dynamics, obtaining the Hamiltonian governing the dynamics of an ensemble ofNNtwo-level bosons in a single well, driven by an external clock field as the spin Hamiltonian[29]:H^=−ℏ​δ​S^z−ℏ​Ω​S^x+C​(N−1)​S^z+χ​S^z2.\hat{H}=-\hbar\delta\hat{S}_{z}-\hbar\Omega\hat{S}_{x}+C(N-1)\hat{S}_{z}+\chi\hat{S}_{z}^{2}\,.(1)

HereS→^={S^x,S^y,S^z}\hat{\vec{S}}=\{\hat{S}_{x},\hat{S}_{y},\hat{S}_{z}\}are the collective spin operators derived from the bosonic field operators, withS^z≡(N^e−N^g)/2\hat{S}_{z}\equiv(\hat{N}_{e}-\hat{N}_{g})/2the atomic inversion operator andeeandgglabel the excited and ground clock levels, respectively, whileC=(Ue​e−Ug​g)/2C=(U_{ee}-U_{gg})/2andχ=(Ue​e+Ug​g−2​Ue​g)/2\chi=(U_{ee}+U_{gg}-2U_{eg})/2represent the linear and nonlinear interaction energy scales, respectively, as a function of the thermally averaged over the radial modes two-body interaction strengthsUi​j=κi​j(2)​(4​π​ℏ2​ai​j)/M​∫|w​(𝐫)|4​d3​rU_{ij}=\kappa_{ij}^{(2)}(4\pi\hbar^{2}a_{ij})/M\,\int|w(\mathbf{r})|^{4}d^{3}r, whereai​ja_{ij}are the scattering lengths for levelsi,ji,j, theκi​j(2)\kappa_{ij}^{(2)}coefficients encode same-mode pair correlations which for an ideal thermal bosonic radial mode is equal to 2, andw​(𝐫)w(\mathbf{r})are the thermally averaged Wannier functions[29]. The latter integral can be seen as the single atom densityn0n_{0}and depends on the details of the depth of the lattice confinement and the thermal energy of each atom[29]. The effect of non-vanishing interaction energies on the optical clock experimental observable, the excitation probabilityPe=⟨S^z⟩/N+1/2P_{e}=\langle\hat{S}_{z}\rangle/N+1/2, is both a shift of the resonance peak and an asymmetric lineshape, affecting the operating clock frequency which obeys the simple relationPe​(δint+δlock)−Pe​(δint−δlock)=0,P_{e}(\delta_{\rm int}+\delta_{\text{lock}})-P_{e}(\delta_{\rm int}-\delta_{\text{lock}})=0\,,(2)

whereδlock\delta_{\text{lock}}is the clock laser offset frequency used in the clock cycle to extrapolate the clock resonance frequency, andδint\delta_{\text{int}}is the detuning of the clock frequency with respect to the unperturbed atom.

The dynamics of the system can experience different regimes depending on the magnitude of the interaction parameters with respect to the Rabi frequencyΩ\Omegaand the lattice site occupation valuemm. Regarding the interaction strengths, at typical temperatures (∼1​μ\sim 1\,\muK) and lattice depths (∼100​Er\sim 100\,E_{r}) of a 1D optical lattice clock, we expect thatℏ​Ω≫χ,C\hbar\Omega\gg\chi,C, so that no effect on the Rabi spectrum should be visible. On the other hand, reducing the dimensionality of the system by introducing a second lattice can easily shift the system from the weakly to the strongly interacting regime even atμ\muK temperatures and relatively low density[30,31], with visible interaction sidebands.

In the case of high occupation number,88Sr has previously exhibited a strong dephasing rate[18], which may imply a leakage from the collective spin manifold due to local radial mode-changing interactions. These dissipative effects can be included at the microscopic level (see[29]), however the solution of such dissipative many-body model is cumbersome. Therefore, we efficiently simulate the dynamics of the expectation values of the spin operators reduced to c-numbers in the mean-field approximation[32], including dissipation. This is equivalent to approximating quadratic spin correlators as products of expectation values of collective spin operators. Introducing the single-particle Bloch vector variablesu=2​⟨S^x⟩/Nu=2\langle\hat{S}_{x}\rangle/N,v=2​⟨S^y⟩/Nv=2\langle\hat{S}_{y}\rangle/N,w=2​⟨S^z⟩/Nw=2\langle\hat{S}_{z}\rangle/N, the nonlinear optical Bloch equations including interaction-induced dephasing are (see Suppl. Mat.[29]for a microscopic derivation, including two-body losses)u˙\displaystyle\dot{u}=(δ−δ​νint​(w))​v−γdeph4​(N−1)​(1−w)​u,\displaystyle=(\delta-\delta\nu_{\rm int}(w))v-\frac{\gamma_{\rm deph}}{4}(N-1)\left(1-w\right)u,v˙\displaystyle\dot{v}=Ω​w−(δ−δ​νint​(w))​u−γdeph4​(N−1)​(1−w)​v,\displaystyle=\Omega w-(\delta-\delta\nu_{\rm int}(w))u-\frac{\gamma_{\rm deph}}{4}(N-1)\left(1-w\right)v,w˙\displaystyle\dot{w}=−Ω​v.\displaystyle=-\Omega v.(3)

whereℏ​δ​νint=C​(N−1)+χ​N​w\hbar\delta\nu_{\rm int}=C(N-1)+\chi Nwis the nonlinear interaction shift, which in the limit ofN≫1N\gg 1reduces to the well-known mean-field density shift formula[22], whileγdeph\gamma_{\rm deph}is the dephasing rate constant of the density dependent coherence relaxation. Fromδ​νint\delta\nu_{\rm int}one can appreciate that it is possible to tuneww(or⟨S^z⟩\langle\hat{S}_{z}\ranglefrom (1)), by means ofδlock\delta_{\rm lock}, to reduce or cancel out the interaction shift or, vice-versa, to find a “magic” lattice atomic numberNNat which the interaction shift vanishes, depending on the interaction energiesUi​jU_{ij}. Interaction shift cancellation in fermionic clocks in a Rabi spectroscopy protocol has already been devised[33], but without including the nonlinear interaction effect.

In order to take into account the nonlinear interaction term and thus accurately calculate the interaction frequency shifts, we numerically solve both the unitary many-body Schrödinger equation using Eq. (1) and the dissipative optical Bloch equations (3). Finally, we compare their predictions with our data by integrating over lattice site occupation distributionm​ℛ​(m)m\mathcal{R}(m), whereℛ​(m)\mathcal{R}(m)is the probability of havingmmatoms at any lattice site which is obtained from a Poisson distribution, with the mean occupation number at each site determined by a Gaussian distribution and averaged over all sites[11](see Fig.1(a)).

## Experimental setup.

The experimental setup for the88Sr optical lattice clock used in these experiments has been extensively described in previous works[34,35]. After laser cooling and trapping, the ultracold atomic ensemble is interrogated by the clock laser beam aligned along the horizontal lattice (namely, thezzaxis). Additionally, a second optical lattice has been included along the vertical direction (theyyaxis), orthogonal to the existing lattice. The two lattice laser beams are independently controlled by acousto-optic modulators and detuned from each other by roughly 160 MHz to avoid unwanted interference and phase instabilities. The geometrical and thermodynamic properties of the 1D and 2D lattice configurations are characterized by precise sideband spectroscopy, time-of-flight absorption imaging, and parametric heating measurements. Typical clock operations are performed with a lattice temperature of 1.2μ\muK and 2μ\muK for the 1D and 2D lattice, respectively, and trap frequencies ofνz\nu_{z}= 68 kHz andνy\nu_{y}= 14 kHz.

By controlling the laser power of the cold atomic source[36]we change the atomic population loaded into the optical lattice. In the 1D lattice case, atoms are loaded from a MOT operating on the1S0–3P1transition, which produces an approximately Gaussian spatial distribution with a standard deviationσz1D=σMOT=192​(7)µ​m\sigma_{z}^{\text{1D}}=\sigma_{\text{MOT}}=$192(7)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}$.Figure 2:Observation of clock frequency shift in a 2D lattice as function of the excitation fractionPeP_{e}as set by the locking pointδlock\delta_{\text{lock}}(main panel) fitted by spin model integration (solid red line), with the absolute shift at the reference point pinned by the density shift measurement at differentNtotN_{\text{tot}}(in the inset). See main text for details.

For the 2D lattice, to avoid loading lattice sites away from the intersection of the two orthogonal beams, the two lattice beams are alternately switched on and off adiabatically, so that the final spatial extent of the 2D lattice is due to the transverse width of the vertical lattice for thezzdirection, and by the transverse width of the horizontal lattice in theyyaxis. The resulting spatial widths are estimated to beσz2D=70​(5)​μ\sigma_{z}^{\text{2D}}=70(5)\,\mum andσy2D=12​(5)​μ\sigma_{y}^{\text{2D}}=12(5)\,\mum. We also apply to the 2D lattice case the Gaussian approximation for determining the lattice occupation probability in our numerical treatment.

Since the interaction strength heavily depends on the single atom density, we make use of the measurement of the two-body inelastic scattering rate for the clock excited state, which has the same functional dependence on the atomic volume[37], as a check for both the 1D and 2D lattices[29]. For the 1D lattice, the single atom density is about1.2×10101.2\times 10^{10}cm-3, while the two-body loss parameterβP03=21​(7)\beta_{{}^{3}P_{0}}=21(7)μ\mum3/s, which is consistent with the previously measured value[38,39]. For the 2D lattice, the single atom density is evaluated at about7.9×1011cm−37.9\text{\times}{10}^{11}\text{\,}\mathrm{c}\mathrm{m}^{-3}.

Interleaved frequency measurements between different values of the atomic population allow us to precisely address the interaction shift. The two lattice populations are stable during the hour-long averaging time within 10%. Rabi spectroscopy on the atomic ensemble is performed with a clock pulse ofTπ=15T_{\pi}=15ms, corresponding to aΩ=2π×\Omega=2\pi\times34Hz34\text{\,}\mathrm{H}\mathrm{z}. The relative clock frequency instability for these measurements is about1×10−14/τ1\times 10^{-14}/\sqrt{\tau}, mainly limited by the residual Dick effect due to the residual phase noise of the local oscillator frequency reference and the low duty cycle (∼4\sim 4%). This allows us to estimate frequency differences with a statistical uncertainty of about3×10−163\times 10^{-16}after1×103s1\text{\times}{10}^{3}\text{\,}\mathrm{s}of integration.

## Results

We first consider experimental lineshapes for highly populated (>104>10^{4}) 1D and 2D lattices, as shown in Fig.1. These lineshapes were obtained by scanning the laser frequency across the clock resonance several times and averaging the atomic response at each detuning. In the 1D lattice, we observe a nearly symmetric peak whose broadening is mainly due to contributions from lattice sites with high occupation numbersmm, as expected from the occupation distribution shown in Fig.1(a). However, in the 2D lattice, strong interactions in multiply occupied lattice tubes lead to both a slight asymmetry at negative detuning and a slightly increased excitation fraction at resonance.
This can also be understood as a consequence of the relative majority of singly populated lattice sites.
An interaction sideband can be constructed by subtracting the excitation values at positive detunings to their corresponding negative values[40], as reported in Fig.1(c). The negative detuning of the interaction sideband implies that theUe​g−Ug​gU_{eg}-U_{gg}energy difference is negative and due to the very small value ofag​ga_{gg}[41](which we neglect in the following),ae​ga_{eg}must also be negative. The interaction sideband can be heuristically modeled as the result of the sum of the single-atom excitation probabilities of themm-populated lattice tubes, i.e.ISB​(δ)∝∑mm​ℛ​(m)​[f​(δ−(m−1)​Ue​g/h,Γ)−f​(−δ−(m−1)​Ue​g/h,Γ)]\text{ISB}(\delta)\propto\sum_{m}m\mathcal{R}(m)[f(\delta-(m-1)U_{eg}/h,\Gamma)-f(-\delta-(m-1)U_{eg}/h,\Gamma)], wheref​(δ,Γ)f(\delta,\Gamma)is the Rabi spectral response with a full width at half-maximumΓ\Gammathat could incorporate broadening effects. This model provides a basic understanding of the data, as shown by the line in Fig.1(c), whereUe​g/h=U_{eg}/h=-32(8) Hz is the inter-level interaction energy.

We also directly measure the effect of interactions on the OLC frequency in the 2D lattice by interleaved self-comparison. The interaction-induced frequency shift at a fixed total atom number (Ntot0=8.4×103N_{\text{tot}}^{0}=8.4\times 10^{3}) with respect to a reference lock pointδlock0/2​π=\delta_{\text{lock}}^{0}/2\pi=25 Hz clearly shows a dependence on the locking pointδlock\delta_{\text{lock}}spanning more than2×10−152\text{\times}{10}^{-15}\text{\,}in relative units, as shown in Fig.2. In order to find the absolute frequency shift, we also performed differential frequency measurements as a function of the total lattice occupationNtot2DN_{\text{tot}}^{{}_{\text{2D}}}atδlock0\delta_{\rm lock}^{0}, as shown in the inset of Fig.2. The interaction-induced shift exhibits a marked deviation from linearity already forNtot>N_{\text{tot}}>3×1043\text{\times}{10}^{4}\text{\,}.
The two data sets are simultaneously fit by numerical integration of the spin model equation, implemented with QuTiP[42], and finding the clock laser detuning fulfilling (2), and forced to share the same interaction parameters, while keeping independent absolute offsets.
The resulting interaction values areUe​g/h=U_{eg}/h=−15​(2)Hz-15(2)\text{\,}\mathrm{H}\mathrm{z}andUe​e/h=U_{ee}/h=12​(4)Hz12(4)\text{\,}\mathrm{H}\mathrm{z}, while the frequency offsets are0.16​(4)Hz0.16(4)\text{\,}\mathrm{H}\mathrm{z}and0.16​(12)Hz0.16(12)\text{\,}\mathrm{H}\mathrm{z}respectively, which are consistent with a single frequency offset corresponding to the absolute frequency shift forδint​(Ntot0,δlock0)\delta_{\rm int}(N_{\text{tot}}^{0},\delta_{\rm lock}^{0})for both measurements. We therefore find that the interaction-induced frequency shift is canceled forδlock/2​π=\delta_{\text{lock}}/2\pi=32​(1)Hz32(1)\text{\,}\mathrm{H}\mathrm{z}(orδlock/Ω=0.94​(3)\delta_{\text{lock}}/\Omega=0.94(3), close to the peak sensitivity point at about∼0.8\sim 0.8[43]). We also fit this data with the mean-field model including dephasing. The fitted dephasing rateγdeph\gamma_{\rm deph}is consistent with zero. This can be explained as a consequence of the lower occupation number per lattice site and the reduced dimensionality of the transverse spatial degrees of freedom.Figure 3:Measurement of the interaction frequency shift in a 1D88Sr optical lattice clock. Main panel: interleaved interaction shift measurements as function of the total lattice occupationNtotN_{\text{tot}}at three different lock detuningsδlock/Ω\delta_{\text{lock}}/\Omega: 0.4 (triangles, green), 0.7 (squares, orange), 1.0 (circles, blue). Solid lines represents numerical fit by integrating the mean-field dissipative optical Bloch equations at the differentδlock\delta_{\text{lock}}values, dashed lines are the unitary many-body spin-model interaction shift with same scattering parameters. Inset: Interaction frequency shift at a fixed total atom numberNtot=7×103N_{\text{tot}}=7\times 10^{3}as function ofδlock\delta_{\text{lock}}. Colored points correspond to the frequency offsets determined from fitting the data in the main panel. Details in the main text.

In the 1D lattice configuration, we measure the effect of interactions on the OLC frequency by interleaved self-comparison with respect to a clock set toNtot0=7×103N_{\text{tot}}^{0}=7\times 10^{3}andδlock0/2​π\delta_{\rm lock}^{0}/2\pi=25Hz25\text{\,}\mathrm{H}\mathrm{z}. The resulting differential measurement is shown in Fig.3, where each data set corresponds to a different clock locking detuningδlock\delta_{\text{lock}}.
Each data set shows at small values ofNtot≲N_{\text{tot}}\lesssim2×1042\text{\times}{10}^{4}\text{\,}a positive linear interaction shift, while for higher occupation values the shift changes sign, implying a zero crossing at which the interaction shift can be canceled.
Again, the data are fit by numerical integration of the spin model with and without including relaxation in the mean-field approximation, and by performing a spatial averaging over all possible lattice occupation values[11]. We find better agreement with the data for the dissipative mean-field equations, where the additional dephasing parameterγdeph\gamma_{\rm deph}is included. However, in the 1D case, the estimated absolute value of the excited-excited two-body interaction energy|Ue​e||U_{ee}|is larger than|Ue​g||U_{eg}|. The fit results for the interaction energies for the 1D lattice at 80ErE_{r}and a typical lattice temperature areUe​e/h=U_{ee}/h=0.25​(3)Hz0.25(3)\text{\,}\mathrm{H}\mathrm{z}andUe​g/h=U_{eg}/h=−0.14​(4)Hz-0.14(4)\text{\,}\mathrm{H}\mathrm{z}, respectively; all measurements are consistent within 1σ\sigma. The estimated dephasing rateγdeph=\gamma_{\rm deph}=1.3​(2)s−11.3(2)\text{\,}\mathrm{s}^{-1}, orγdeph/n0=\gamma_{\rm deph}/n_{0}=120​(20)µ​m3​s−1120(20)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}^{3}\,\mathrm{s}^{-1}, consistent with previous experiments[18]and an independent estimate from Rabi oscillations[29]. This apparent discrepancy with 2D data may be reconciled by considering a reduced bosonic correlation coefficientκe​g(2)=1\kappa_{eg}^{(2)}=1due to collapse of thee−ge-gcoherence on the relevant collision timescale (see[29]).

We also compare the interaction-induced frequency shift at a fixed total atom number,Ntot=7×103N_{\text{tot}}=7\times 10^{3}, for various locking pointsδlock\delta_{\text{lock}}, which correspond to different clock excitation fractions[44,45]. These are compared with the expected shifts calculated using the interaction energies extracted from the density shift measurements, as shown in the inset of Fig.3. The differential measurement points are corrected by the absolute frequency offset extracted by the fit performed onNtotN_{\text{tot}}. The expected shift is comparable to the current experimental sensitivity; nevertheless, the data are consistent with the predicted trend.
We therefore find that the interaction-induced frequency shift in the 1D lattice is canceled forδlock/2​π\delta_{\text{lock}}/2\pi=48​(1)Hz48(1)\text{\,}\mathrm{H}\mathrm{z}(orδlock/Ω=\delta_{\text{lock}}/\Omega=1.4, which is not suitable for optimal clock operation).

To highlight the crucial role of dissipation, we also show (dashed lines in Fig.3) the prediction of unitary dynamics, using the coupling parameters from the fit. However, we double the value ofUe​gU_{eg}, to take into account that in this case no dissipation mechanism bringsκe​g(2)→1\kappa_{eg}^{(2)}\to 1. We observe that the data deviate from this prediction both at large values ofNtotN_{\text{tot}}(main panel) and at largeδlock\delta_{\rm lock}(inset), where the influence of the nonlinear interaction is lower than the linear term. This implies that the expected sign change near the half-maximum point of the Rabi fringe is not observed.Table 1:Summary of the measured interaction energies for the 1D and 2D lattices and the derived s-wave scattering lengths for the clock states of the two-level88Sr bosonic system.QuantityValueRef.(Ue​e−Ug​g)/h(U_{ee}-U_{gg})/h0.25(3) Hz[This work, 1D OL]12(4) Hz[This work, 2D OL]Ue​g/hU_{eg}/h-0.14(4) Hz[This work, 1D OL]-15(2) Hz[This work, 2D OL]ag​ga_{gg}-2.2(2)a0a_{0}[41]|ae​e||a_{ee}|100​(50)100(50)a0a_{0}[38]ae​ea_{ee}105(16)a0a_{0}[This work]ae​ga_{eg}-125(12)a0a_{0}[This work]

Finally, we extract the values for the s-wave scattering lengths from the experimentally estimated interaction energies and the thermally averaged atomic volumes, which results in the main source of uncertainty[29]. The calculated values are reported in Tab.1after averaging among the three different experimental methods described here. Regarding thee−ee-escattering length, our estimate is in agreement with previously reported values[38]. For the inter-level scattering length, the reported valueae​g=a_{eg}=−125​(12)-125(12)\text{\,}a0a_{0}is the first reported estimate. This can be used as a benchmark for bothab initioquantum chemistry calculations for the1S0–3P0interaction potential, and for clock-line photoassociation[46,47].

## Conclusions

In conclusion, we report the first extensive study of the measurement and control of interaction-induced frequency shifts in a bosonic optical lattice clock, both varying the total lattice population over almost two orders of magnitude (Ntot∼103−105N_{\text{tot}}\sim 10^{3}-10^{5}) and the clock excitation level. In the case of the 2D lattice, with two spatial degrees of freedom tightly confined and a low average site occupation number, we observe many-body features like the emergence of an interaction sideband. We find that a collective spin model approximation to describe the interaction dynamics is valid even in a thermal atomic ensemble. Here cancellation of the interaction-induced shift is possible in the proximity of the optimal sensitivity point. Regarding the 1D lattice, we observe reduced inter-level interaction energy and dynamics influenced by dephasing, possibly due to radial-mode-changing (or lateral) collisions. However, a dissipative mean-field approach can still reproduce the nonlinear density shift measured for this clock transition. In this way we are able to extrapolate to the interaction shift at level of3​(2)×10−163(2)\text{\times}{10}^{-16}\text{\,}[48]. This approach can be useful for bosonic clocks based on other atomic species that are used for tests of fundamental physics by isotope shift measurements[49,14].
Knowledge of the coupling constants of theg​ggg,e​eeeande​gegchannels opens the intriguing perspective of realizing an XXZ spin model[50], provided sufficiently low temperatures are attained[51]. Combining this with Rabi driving in the rotating frame of the clock laser realizes the XXZ model in a transverse field, which has been proposed as a novel method to adiabatically prepare scalable spin-squeezed states[52].

## Acknowledgements.We thank C. D’Errico, F. Pereira dos Santos and T. Roscilde for their expertise and for stimulating discussions. The project 23FUN02 CoCoRICO has received funding from the European Partnership on Metrology, co-financed from the European Union’s Horizon Europe Research and Innovation Programme and by the Participating States.

## References
- Ludlowet al.[2015]A. D. Ludlow, M. M. Boyd, J. Ye, E. Peik, and P. O. Schmidt, Optical atomic clocks,Rev. Mod. Phys.87, 637 (2015).
- Derevianko and Katori [2011]A. Derevianko and H. Katori, Colloquium: Physics of optical lattice clocks,Reviews of Modern Physics83, 331 (2011).
- McGrewet al.[2018]W. F. McGrew, X. Zhang, R. J. Fasano, S. A. Schäffer, K. Beloy, D. Nicolodi, R. C. Brown, N. Hinkley, G. Milani, M. Schioppo, T. H. Yoon, and A. D. Ludlow, Atomic clock performance enabling geodesy below the centimetre level,Nature564, 87 (2018).
- Bothwellet al.[2022]T. Bothwell, C. J. Kennedy, A. Aeppli, D. Kedar, J. M. Robinson, E. Oelker, A. Staron, and J. Ye, Resolving the gravitational redshift across a millimetre-scale atomic sample, Nature602, 420 (2022).
- Aeppliet al.[2024]A. Aeppli, K. Kim, W. Warfield, M. S. Safronova, and J. Ye, Clock with8×10−198\times 10^{-19}systematic uncertainty, Physical Review Letters133,10.1103/physrevlett.133.023401(2024).
- Filzingeret al.[2023]M. Filzinger, S. Dörscher, R. Lange, J. Klose, M. Steinel, E. Benkler, E. Peik, C. Lisdat, and N. Huntemann, Improved limits on the coupling of ultralight bosonic dark matter to photons from optical atomic clock comparisons, Physical Review Letters130,10.1103/physrevlett.130.253001(2023).
- Safronova [2019]M. S. Safronova, The search for variation of fundamental constants with clocks, Annalen der Physik531,10.1002/andp.201800364(2019).
- Sherrillet al.[2023]N. Sherrill, A. O. Parsons, C. F. A. Baynham, W. Bowden, E. Anne Curtis, R. Hendricks, I. R. Hill, R. Hobson, H. S. Margolis, B. I. Robertson, M. Schioppo, K. Szymaniec, A. Tofful, J. Tunesi, R. M. Godun, and X. Calmet, Analysis of atomic-clock data to constrain variations of fundamental constants,New Journal of Physics25, 093012 (2023).
- Shinkaiet al.[2025]H. Shinkai, M. Takamoto, and H. Katori, Transportable optical lattice clocks and general relativity,International Journal of Modern Physics D34, 2540012 (2025),https://doi.org/10.1142/S0218271825400127.
- Riehle [2015]F. Riehle, Towards a redefinition of the second based on optical atomic clocks,Comptes Rendus Physique16, 506 (2015), the measurement of time / La mesure du temps.
- Reyet al.[2014]A. Rey, A. Gorshkov, C. Kraus, M. Martin, M. Bishof, M. Swallows, X. Zhang, C. Benko, J. Ye, N. Lemke, and A. Ludlow, Probing many-body interactions in an optical lattice clock,Annals of Physics340, 311 (2014).
- Aeppliet al.[2022]A. Aeppli, A. Chu, T. Bothwell, C. J. Kennedy, D. Kedar, P. He, A. M. Rey, and J. Ye, Hamiltonian engineering of spin-orbit–coupled fermions in a wannier-stark optical lattice clock, Science Advances8,10.1126/sciadv.adc9242(2022).
- Berengutet al.[2018]J. C. Berengut, D. Budker, C. Delaunay, V. V. Flambaum, C. Frugiuele, E. Fuchs, C. Grojean, R. Harnik, R. Ozeri, G. Perez, and Y. Soreq, Probing new long-range interactions by isotope shift spectroscopy,Phys. Rev. Lett.120, 091801
(2018).
- Onoet al.[2022]K. Ono, Y. Saito, T. Ishiyama, T. Higomoto, T. Takano, Y. Takasu, Y. Yamamoto, M. Tanaka, and Y. Takahashi, Observation of nonlinearity of generalized king plot in the search for new boson,Phys. Rev. X12, 021033 (2022).
- Berengut and Delaunay [2025]J. C. Berengut and C. Delaunay, Precision isotope-shift spectroscopy for new physics searches and nuclear insights,Nature Reviews Physics7, 119 (2025).
- Zelevinskyet al.[2006]T. Zelevinsky, M. M. Boyd, A. D. Ludlow, T. Ido, J. Ye, R. Ciuryło, P. Naidon, and P. S. Julienne, Narrow line photoassociation in an optical lattice,Physical Review Letters96, 203201 (2006).
- Akatsukaet al.[2008]T. Akatsuka, M. Takamoto, and H. Katori, Optical lattice clocks with non-interacting bosons and fermions,Nature Physics4, 954 (2008).
- Lisdatet al.[2009]C. Lisdat, J. S. R. V. Winfred, T. Middelmann, F. Riehle, and U. Sterr, Collisional losses, decoherence, and frequency shifts in optical lattice clocks with bosons,Physical Review Letters103, 090801 (2009).
- Takanoet al.[2017]T. Takano, R. Mizushima, and H. Katori, Precise determination of the isotope shift of88sr–87sr optical lattice clock by sharing perturbations,Applied Physics Express10, 072801 (2017).
- Origliaet al.[2018]S. Origlia, M. S. Pramod, S. Schiller, Y. Singh, K. Bongs, R. Schwarz, A. Al-Masoudi, S. Dörscher, S. Herbers, S. Häfner, U. Sterr, and C. Lisdat, Towards an optical clock for space: Compact, high-performance optical lattice clock based on bosonic atoms,Physical Review A98, 053443 (2018).
- Killianet al.[1998]T. C. Killian, D. G. Fried, L. Willmann, D. Landhuis, S. C. Moss, T. J. Greytak, and D. Kleppner, Cold collision frequency shift of the1s-2stransition in hydrogen,Physical Review Letters81, 3807 (1998).
- Harberet al.[2002]D. M. Harber, H. J. Lewandowski, J. M. McGuirk, and E. A. Cornell, Effect of cold collisions on spin coherence and resonance shifts in a magnetically trapped ultracold gas,Phys. Rev. A66, 053616 (2002).
- Vellore Winfred [2010]J. S. R. Vellore Winfred,Investigation of collisional losses and decoherence in a 1-D optical lattice clock with 88Sr,phdthesis, Gottfried Wilhelm Leibniz Universität Hannover (2010).
- Bonninet al.[2019]A. Bonnin, C. Solaro, X. Alauze, and F. Pereira dos Santos, Magic density in a self-rephasing ensemble of trapped ultracold atoms,Phys. Rev. A99, 023627 (2019).
- Bloch [2005]I. Bloch, Ultracold quantum gases in optical lattices,Nature Physics1, 23 (2005).
- Katoriet al.[1999]H. Katori, T. Ido, and M. Kuwata-Gonokami, Optimal design of dipole potentials for efficient loading of sr atoms,Journal of the Physical Society of Japan68, 2479 (1999).
- Dicke [1953]R. H. Dicke, The effect of collisions upon the doppler width of spectral lines,Physical Review89, 472 (1953).
- Lhuillier and Laloë [1982]C. Lhuillier and F. Laloë, Transport properties in a spin polarized gas, i,Journal de Physique43, 197 (1982).
- [29]See Supplemental Material at [URL], which includes Refs.[53,54,55,56,57,58,59,37].
- Swallowset al.[2011]M. D. Swallows, M. Bishof, Y. Lin, S. Blatt, M. J. Martin, A. M. Rey, and J. Ye, Suppression of collisional shifts in a strongly interacting lattice clock,Science331, 1043 (2011).
- Swallowset al.[2012]M. D. Swallows, M. J. Martin, M. Bishof, C. Benko, Y. Lin, S. Blatt, A. M. Rey, and J. Ye, Operating a 87sr optical lattice clock with high precision and at high density,IEEE Transactions on Ultrasonics, Ferroelectrics and Frequency Control59, 416 (2012).
- Band and Vardi [2006]Y. B. Band and A. Vardi, Collisional shifts in optical-lattice atom clocks,Phys. Rev. A74, 033807 (2006).
- Leeet al.[2016]S. Lee, C. Y. Park, W.-K. Lee, and D.-H. Yu, Cancellation of collisional frequency shifts in optical lattice clocks with rabi spectroscopy,New Journal of Physics18, 033030 (2016).
- Barbieroet al.[2022]M. Barbiero, D. Calonico, F. Levi, and M. G. Tarallo, Optically loaded strontium lattice clock with a single multi-wavelength reference cavity,IEEE Transactions on Instrumentation and Measurement71, 1 (2022).
- Barbieroet al.[2023]M. Barbiero, J. P. Salvatierra, M. Risaro, C. Clivati, D. Calonico, F. Levi, and M. G. Tarallo, Broadband serrodyne phase modulation for optical frequency standards and spectral purity transfer,Optics Letters48, 1958 (2023).
- Barbieroet al.[2020]M. Barbiero, M. G. Tarallo, D. Calonico, F. Levi, G. Lamporesi, and G. Ferrari, Sideband-enhanced cold atomic source for optical clocks,Physical Review Applied13, 014013 (2020).
- Bouganneet al.[2017]R. Bouganne, M. B. Aguilera, A. Dareau, E. Soave, J. Beugnon, and F. Gerbier, Clock spectroscopy of interacting bosons in deep optical lattices,New Journal of Physics19, 113006 (2017).
- Traversoet al.[2009]A. Traverso, R. Chakraborty, Y. N. M. de Escobar, P. G. Mickelson, S. B. Nagel, M. Yan, and T. C. Killian, Inelastic and elastic collision rates for triplet states of ultracold strontium,Physical Review A79, 060702 (2009),arXiv:0809.0936v1 [physics.atom-ph].
- Doldeet al.[2025]J. Dolde, D. Ganapathy, X. Zheng, S. Ma, K. Beloy, and S. Kolkowitz, Direct measurement of thep03{}^{3}p_{0}clock state natural lifetime inSr87{}^{87}\mathrm{Sr},Phys. Rev. A112, 023121 (2025).
- Bishofet al.[2011a]M. Bishof, Y. Lin, M. D. Swallows, A. V. Gorshkov, J. Ye, and A. M. Rey, Resolved atomic interaction sidebands in an optical clock transition,Phys. Rev. Lett.106, 250801 (2011a).
- Stellmeret al.[2013]S. Stellmer, R. Grimm, and F. Schreck, Production of quantum-degenerate strontium gases,Phys. Rev. A87, 013611 (2013).
- Johanssonet al.[2012]J. Johansson, P. Nation, and F. Nori, Qutip: An open-source python framework for the dynamics of open quantum systems,Computer Physics Communications183, 1760 (2012).
- Dick [1989]G. J. Dick, Local oscillator induced instabilities in trapped ion frequency standards, inProceedings of the 19th Annual Precise Time and Time Interval Systems and Applications Meeting(1989) pp. 133–147.
- Campbellet al.[2009]G. K. Campbell, M. M. Boyd, J. W. Thomsen, M. J. Martin, S. Blatt, M. D. Swallows, T. L. Nicholson, T. Fortier, C. W. Oates, S. A. Diddams, N. D. Lemke, P. Naidon, P. Julienne, J. Ye, and A. D. Ludlow, Probing interactions between ultracold fermions,Science324, 360 (2009).
- Lemkeet al.[2011]N. D. Lemke, J. von Stecher, J. A. Sherman, A. M. Rey, C. W. Oates, and A. D. Ludlow,pp-wave cold collisions in an optical lattice clock,Phys. Rev. Lett.107, 103902 (2011).
- Borkowski [2018]M. Borkowski, Optical lattice clocks with weakly bound molecules,Phys. Rev. Lett.120, 083202 (2018).
- Bettermannet al.[2023]O. Bettermann, N. Darkwah Oppong, G. Pasqualetti, L. Riegger, I. Bloch, and S. Fölling, Clock-line photoassociation of strongly bound dimers in a magic-wavelength lattice,Phys. Rev. A108, L041302 (2023).
- Salvatierra [2026]J. P. Salvatierra,Advancing Optical Lattice Clocks: Accurate Measurements on a Bosonic System and Development of a Hybrid Cavity-Lattice Clock, Ph.D. thesis, Politecnico di Torino (2026).
- Miyakeet al.[2019]H. Miyake, N. C. Pisenti, P. K. Elgee, A. Sitaram, and G. K. Campbell, Isotope-shift spectroscopy of theS01→3P1{}^{1}S_{0}\rightarrow^{3}P_{1}andS01→3P0{}^{1}S_{0}\rightarrow^{3}P_{0}transitions in strontium,Phys. Rev. Res.1, 033113 (2019).
- Duanet al.[2003]L.-M. Duan, E. Demler, and M. D. Lukin, Controlling Spin Exchange Interactions of Ultracold Atoms in Optical Lattices,Phys. Rev. Lett.91, 090402 (2003).
- Chenet al.[2025]C.-C. Chen, R. Takeuchi, S. Okaba, and H. Katori, Narrow-line-mediated sisyphus cooling in thep23{}^{3}p_{2}metastable state of strontium,Phys. Rev. Res.7, L022076 (2025).
- Comparinet al.[2022]T. Comparin, F. Mezzacapo, M. Robert-de Saint-Vincent, and T. Roscilde, Scalable spin squeezing from spontaneous breaking of a continuous symmetry,Phys. Rev. Lett.129, 113201 (2022).
- Breuer and Petruccione [2002]H. Breuer and F. Petruccione,The Theory of Open Quantum Systems(Oxford University Press, 2002).
- Gonzalez-Ballestero [2024]C. Gonzalez-Ballestero, Tutorial: Projector approach to master equations for open quantum systems,Quantum8, 1454 (2024).
- Giaccariet al.[2026]S. Giaccari, G. Dellea, M. G. Genoni, and G. Bertaina, Higher-order adiabatic elimination in atom-cavity systems and its impact on spin-squeezing generation,Quantum Sci. Technol.11, 035019 (2026).
- Bertainaet al.[2026]G. Bertaina, J. P. Salvatierra, and M. G. Tarallo (2026), in preparation.
- Pethick and Smith [2002]C. J. Pethick and H. Smith,Bose–Einstein Condensation in Dilute Gases(Cambridge University Press, 2002).
- Fetter and Walecka [2003]A. L. Fetter and J. D. Walecka,Quantum Theory of Many-Particle Systems(Dover Publications, 2003).
- Bishofet al.[2011b]M. Bishof, M. J. Martin, M. D. Swallows, C. Benko, Y. Lin, G. Quemener, A. M. Rey, and J. Ye, Inelastic collisions and density-dependent excitation suppression in a Sr-87 optical lattice clock,Phys. Rev. A84, 052716 (2011b).

Supplemental Material
for
Measurement and control of the interaction frequency shift in bosonic optical lattice clocks

## Spin model of interacting bosons in an optical lattice

In this section, we aim to derive the spin model presented in Eq.1from the general many-body theoretical framework, employing adiabatic elimination techniques for open quantum systems[53,54,55]. A full derivation will be presented elsewhere[56].

The Hamiltonian of an ensemble of trapped and interacting bosons with two internal states is[57,58]:H^\displaystyle\hat{H}=\displaystyle=∑α∫d3​r​ψ^α†​(𝐫)​(−ℏ22​M​∇2+Vext​(𝐫))​ψ^α​(𝐫)\displaystyle\sum_{\alpha}\int d^{3}r\,\hat{\psi}^{\dagger}_{\alpha}(\mathbf{r})\left(-\frac{\hbar^{2}}{2M}\nabla^{2}+V_{\text{ext}}(\mathbf{r})\right)\hat{\psi}_{\alpha}(\mathbf{r})(S.1)+\displaystyle+12​∑α​β∫d3​r​d3​r′​ψ^α†​(𝐫)​ψ^β†​(𝐫′)​Vα​β​(𝐫−𝐫′)​ψ^β​(𝐫′)​ψ^α​(𝐫),\displaystyle\frac{1}{2}\sum_{\alpha\beta}\int d^{3}rd^{3}r^{\prime}\,\hat{\psi}^{\dagger}_{\alpha}(\mathbf{r})\hat{\psi}^{\dagger}_{\beta}(\mathbf{r^{\prime}})V_{\alpha\beta}(\mathbf{r}-\mathbf{r^{\prime}})\hat{\psi}_{\beta}(\mathbf{r^{\prime}})\hat{\psi}_{\alpha}(\mathbf{r}),−\displaystyle-ℏ​Ω2​∫d3​r​[ψ^e†​(𝐫)​e−i​(𝐤⋅𝐫−ωL​t)​ψ^g​(𝐫)+h.c.]\displaystyle\frac{\hbar\Omega}{2}\int d^{3}r\,\left[\hat{\psi}^{\dagger}_{e}(\mathbf{r})e^{-i(\mathbf{k}\cdot\mathbf{r}-\omega_{L}t)}\hat{\psi}_{g}(\mathbf{r})+\text{h.c.}\right]

where𝒓\bm{r}indicates the translational degree of freedom, whileα,β\alpha,\betalabel the two internal degrees of freedome,ge,g(e.g. hyperfine or optical clock states).Vα​β​(𝐫−𝐫′)V_{\alpha\beta}(\mathbf{r}-\mathbf{r^{\prime}})describes the interactions between bosons in internal statesα\alphaandβ\beta. The factor1/21/2in the interaction term comes from avoiding double counting of pairwise interactions between bosons at the same site.VextV_{\text{ext}}is the external trapping potential, which we assume to be independent of the internal state at the dominant order (magic wavelength condition[26]). Finally, the last line encapsulates the coupling of the internal levels to the external semiclassical clock laser field, modeled by Rabi coupling frequencyΩ\Omega, laser frequencyωL\omega_{L}and wavevector𝐤\mathbf{k}.

As a starting point in the 1D configuration, we assume that longitudinal motion is frozen to a single orbitalϕ0​(z)\phi_{0}(z), while the radial plane supports modesφμ​(𝝆)\varphi_{\mu}(\bm{\rho}), and make the expansionψ^α​(𝒓)=ϕ0​(z)​∑μφμ​(𝝆)​a^α​μ.\hat{\psi}_{\alpha}(\bm{r})=\phi_{0}(z)\sum_{\mu}\varphi_{\mu}(\bm{\rho})\,\hat{a}_{\alpha\mu}\,.(S.2)

An analog expansion holds in the 2D lattice configuration, with the difference that two directions are tightly confined. In the following, we indicate byNNthe number of atoms in the considered trap well.
The Rabi-driven multimode Hamiltonian is thenH^\displaystyle\hat{H}=H^tr+H^Rabi+H^int,\displaystyle=\hat{H}_{\rm tr}+\hat{H}_{\rm Rabi}+\hat{H}_{\rm int},(S.3)H^tr\displaystyle\hat{H}_{\rm tr}=∑μ,αϵμ​a^α​μ†​a^α​μ,\displaystyle=\sum_{\mu,\alpha}\epsilon_{\mu}\hat{a}^{\dagger}_{\alpha\mu}\hat{a}_{\alpha\mu},(S.4)H^Rabi\displaystyle\hat{H}_{\rm Rabi}=−ℏ​Ω​∑μS^xμ−ℏ​δ​∑μS^zμ,\displaystyle=-\hbar\Omega\sum_{\mu}\hat{S}_{x}^{\mu}-\hbar\delta\sum_{\mu}\hat{S}_{z}^{\mu},(S.5)

with mode-resolved spinsS^xμ=a^e​μ†​a^g​μ+a^g​μ†​a^e​μ2,S^zμ=N^eμ−N^gμ2,\hat{S}_{x}^{\mu}=\frac{\hat{a}^{\dagger}_{e\mu}\hat{a}_{g\mu}+\hat{a}^{\dagger}_{g\mu}\hat{a}_{e\mu}}{2},\quad\hat{S}_{z}^{\mu}=\frac{\hat{N}_{e}^{\mu}-\hat{N}_{g}^{\mu}}{2},(S.6)

andN^αμ=a^α​μ†​a^α​μ\hat{N}_{\alpha}^{\mu}=\hat{a}^{\dagger}_{\alpha\mu}\hat{a}_{\alpha\mu}. The interaction isH^int=12​∑μ​ν​η​λ∑α,βUα​βμ​ν​η​λ​a^α​μ†​a^β​ν†​a^β​η​a^α​λ,\hat{H}_{\rm int}=\frac{1}{2}\sum_{\mu\nu\eta\lambda}\sum_{\alpha,\beta}U_{\alpha\beta}^{\mu\nu\eta\lambda}\hat{a}^{\dagger}_{\alpha\mu}\hat{a}^{\dagger}_{\beta\nu}\hat{a}_{\beta\eta}\hat{a}_{\alpha\lambda}\,,(S.7)

where the coefficients are radial overlap integrals multiplied by scattering amplitudes.

## Inelastic two-body channels.

In addition to the Hamiltonian dynamics, inelastic collisions transfer atom pairs to internal or motional states that are not retained in the two-level model. After tracing over these product channels (that are untrapped and thus lost), the continuum master equation containsρ^˙=−iℏ​[H^,ρ^]+∫d3​r​[𝒟​[L^e​e​(𝒓)]+𝒟​[L^e​g​(𝒓)]]​ρ^,\dot{\hat{\rho}}=-\frac{i}{\hbar}[\hat{H},\hat{\rho}]+\int d^{3}r\,\left[\mathcal{D}[\hat{L}_{ee}(\bm{r})]+\mathcal{D}[\hat{L}_{eg}(\bm{r})]\right]\hat{\rho},(S.8)

where the dissipation superoperator is𝒟[L^]∙=L^∙L^†−{L^†L^,∙}/2\mathcal{D}[\hat{L}]\bullet=\hat{L}\bullet\hat{L}^{\dagger}-\{\hat{L}^{\dagger}\hat{L},\bullet\}/2and the two-body loss operators areL^e​e​(𝒓)\displaystyle\hat{L}_{ee}(\bm{r})=βe​e2​ψ^e​(𝒓)​ψ^e​(𝒓),\displaystyle=\sqrt{\frac{\beta_{ee}}{2}}\,\hat{\psi}_{e}(\bm{r})\hat{\psi}_{e}(\bm{r}),L^e​g​(𝒓)\displaystyle\hat{L}_{eg}(\bm{r})=βe​g​ψ^e​(𝒓)​ψ^g​(𝒓).\displaystyle=\sqrt{\beta_{eg}}\,\hat{\psi}_{e}(\bm{r})\hat{\psi}_{g}(\bm{r}).(S.9)

## Assumptions for radial elimination.

We trace over the radial sector and keep only an effective spin dynamics under:
(i) longitudinal freezing; (ii) stationary thermal radial state at temperatureTrT_{r}; (iii) weak backaction of spin dynamics on the radial distribution; (iv) short radial correlation time compared with the spin timesΩ−1\Omega^{-1},|δ|−1|\delta|^{-1},ℏ/|χ|\hbar/|\chi|; (v) Born factorizationρ^​(t)≈ρ^s​(t)⊗ρ^rth;\hat{\rho}(t)\approx\hat{\rho}_{s}(t)\otimes\hat{\rho}_{r}^{\rm th};(S.10)

(vi) diagonal radial thermal state in the radial occupation basis. Only radial-number-conserving terms
survive in the interaction and the reduced spin state isρ^s=Trr⁡ρ^\hat{\rho}_{s}=\Tr_{r}\hat{\rho}.

The first-order reduction gives the thermally averaged Hamiltonian and renormalizes the loss channels already present in the continuum master equation. New dephasing terms generated by the Hermitian interaction appear only at second order in the centered radial fluctuations.

## First-order effective Hamiltonian.

At first order, the effective spin Hamiltonian isH^(1)=Trr⁡(H^​ρ^rth).\hat{H}^{(1)}=\Tr_{r}\!\left(\hat{H}\,\hat{\rho}_{r}^{\rm th}\right).(S.11)

The Rabi term remains−ℏ​Ω​S^x−ℏ​δ​S^z-\hbar\Omega\hat{S}_{x}-\hbar\delta\hat{S}_{z}, whereS^α=∑μS^αμ,S^z=N^e−N^g2,N^α=∑μN^αμ.\hat{S}_{\alpha}=\sum_{\mu}\hat{S}_{\alpha}^{\mu},\qquad\hat{S}_{z}=\frac{\hat{N}_{e}-\hat{N}_{g}}{2},\qquad\hat{N}_{\alpha}=\sum_{\mu}\hat{N}_{\alpha}^{\mu}.(S.12)

TheUα​βμ​ν=Uβ​αμ​ν=Uα​βμ​ν​ν​μU^{\mu\nu}_{\alpha\beta}=U^{\mu\nu}_{\beta\alpha}=U^{\mu\nu\nu\mu}_{\alpha\beta}interaction coefficient matrix is dominated by diagonal termsν=μ\nu=\muin the harmonic confinement approximation[11], with off-diagonal terms strongly suppressed at typical operating temperature. Therefore, the radial-number-conserving interaction terms are:H^intdiag=12​∑μ\displaystyle\hat{H}_{\rm int}^{\rm diag}=\frac{1}{2}\sum_{\mu}[Ue​eμ​μN^eμ(N^eμ−1)+Ug​gμ​μN^gμ(N^gμ−1)\displaystyle\left[U_{ee}^{\mu\mu}\hat{N}_{e}^{\mu}(\hat{N}_{e}^{\mu}-1)+U_{gg}^{\mu\mu}\hat{N}_{g}^{\mu}(\hat{N}_{g}^{\mu}-1)\right.+2Ue​gμ​μN^eμN^gμ].\displaystyle+\left.2U_{eg}^{\mu\mu}\hat{N}_{e}^{\mu}\hat{N}_{g}^{\mu}\right]\,.(S.13)

We assume thermal radial occupationspμ=e−βr​ϵμ/Z​(βr)p_{\mu}=e^{-\beta_{r}\epsilon_{\mu}}/Z(\beta_{r}), withβr=(kB​Tr)−1\beta_{r}=(k_{B}T_{r})^{-1}and∑μpμ=1\sum_{\mu}p_{\mu}=1. Forμ=ν\mu=\nuwe keep Gaussian coefficients,Trr⁡(N^αμ​(N^αμ−1)​ρ^)\displaystyle\Tr_{r}\!\left(\hat{N}_{\alpha}^{\mu}(\hat{N}_{\alpha}^{\mu}-1)\hat{\rho}\right)=κα​α,μ(2)​pμ2​N^α​(N^α−1)​ρ^s,α=g,e\displaystyle=\kappa_{\alpha\alpha,\mu}^{(2)}\,p_{\mu}^{2}\hat{N}_{\alpha}(\hat{N}_{\alpha}-1)\hat{\rho}_{s},\;\;\alpha=g,eTrr⁡(N^eμ​N^gμ​ρ^)\displaystyle\Tr_{r}\!\left(\hat{N}_{e}^{\mu}\hat{N}_{g}^{\mu}\hat{\rho}\right)=κe​g,μ(2)​pμ2​N^e​N^g​ρ^s.\displaystyle=\kappa_{eg,\mu}^{(2)}\,p_{\mu}^{2}\hat{N}_{e}\hat{N}_{g}\hat{\rho}_{s}.(S.14)

For completely indistinguishable ideal thermal bosonic radial modes, the bunching factor isg(2)=2g^{(2)}=2andκe​e,μ(2)=κg​g,μ(2)=κe​g,μ(2)=g(2),\kappa_{ee,\mu}^{(2)}=\kappa_{gg,\mu}^{(2)}=\kappa_{eg,\mu}^{(2)}=g^{(2)},(S.15)

for all combinations and modes. We argue that this is the consistent choice for an initially spin-coherent state with coherent Rabi dynamics faster than dephasing and spin-dependent thermal processes. However, since Born factorization is an approximation, and we cannot completely exclude spin-dependent motional decorrelation or independent rethermalization, we have admitted that the thermal bunching factor can be different for the various spin combinations and we have tested the caseκe​g,μ(2)≃1\kappa_{eg,\mu}^{(2)}\simeq 1which is the expected result for an incoherente/ge/gmixture.

This yields the effective spin HamiltonianH^int(1)=12​U¯e​e​N^e​(N^e−1)+12​U¯g​g​N^g​(N^g−1)+U¯e​g​N^e​N^g,\hat{H}_{\rm int}^{(1)}=\frac{1}{2}\bar{U}_{ee}\hat{N}_{e}(\hat{N}_{e}-1)+\frac{1}{2}\bar{U}_{gg}\hat{N}_{g}(\hat{N}_{g}-1)+\bar{U}_{eg}\hat{N}_{e}\hat{N}_{g},(S.16)

withU¯α​β=∑μUα​βμ​μ​κα​β,μ(2)​pμ2\bar{U}_{\alpha\beta}=\sum_{\mu}U_{\alpha\beta}^{\mu\mu}\kappa_{\alpha\beta,\mu}^{(2)}\,p_{\mu}^{2}(S.17)

We apply a Gaussian approximation to Eq. (S.17), and getU¯α​β≃κα​β(2)​(4​π​ℏ2​aα​β)/M​∫|w​(𝐫)|4​d3​r\bar{U}_{\alpha\beta}\simeq\kappa_{\alpha\beta}^{(2)}(4\pi\hbar^{2}a_{\alpha\beta})/M\,\int|w(\mathbf{r})|^{4}d^{3}r(S.18)

that we denote asUα​βU_{\alpha\beta}in the main text, wherew​(𝐫)w(\mathbf{r})is a temperature-dependent spatial wavefunction approximated by Gaussian harmonic oscillator orbital functions[31], whose1/e1/ewidths areLj=ℏ2​π​M​νj×2​⟨nj⟩+1=ℓ0j​2​⟨nj⟩+1L_{j}=\sqrt{\frac{\hbar}{2\pi M\nu_{j}}}\times\sqrt{2\langle n_{j}\rangle+1}=\ell_{0}^{j}\sqrt{2\langle n_{j}\rangle+1}(S.19)

whereνj\nu_{j}is the trap oscillation frequency alongj^\hat{j}, and⟨nj⟩=(exp⁡[βr​h​νj]−1)−1.\langle n_{j}\rangle=\left(\exp\left[\beta_{r}{h\nu_{j}}\right]-1\right)^{-1}\,.(S.20)

WritingN^e=N/2+S^z\hat{N}_{e}=N/2+\hat{S}_{z},N^g=N/2−S^z\hat{N}_{g}=N/2-\hat{S}_{z}, andC=(Ue​e−Ug​g)/2C=(U_{ee}-U_{gg})/2,χ=(Ue​e+Ug​g−2​Ue​g)/2\chi=(U_{ee}+U_{gg}-2U_{eg})/2, we obtain the effective spin Hamiltonian in the Main text, Eq. (1).

## Local-spin embedding and second-order dephasing.

The strict two-mode bosonic model spans only the symmetricJ=N/2J=N/2sector.
To expose the local structure of the reduced dissipator, we embed the
internal dynamics in the Hilbert space ofNNspin-1/21/2particles,S^α=∑i=1Ns^α(i),s^α(i)=σ^α(i)2,P^e,g(i)=𝟙2±s^z(i),\hat{S}_{\alpha}=\sum_{i=1}^{N}\hat{s}_{\alpha}^{(i)},\quad\hat{s}_{\alpha}^{(i)}=\frac{\hat{\sigma}_{\alpha}^{(i)}}{2},\quad\hat{P}_{e,g}^{(i)}=\frac{\mathbbm{1}}{2}\pm\hat{s}_{z}^{(i)},(S.21)

where the particle labels are a bookkeeping device for the symmetrized bosonic many-body state, and we also consider the radial projector|μi⟩​⟨μi||\mu_{i}\rangle\langle\mu_{i}|.
It is now useful to identify the mode-resolved occupation operator withN^αμ=∑iP^α(i)​|μi⟩​⟨μi|,\hat{N}_{\alpha}^{\mu}=\sum_{i}\hat{P}_{\alpha}^{(i)}|\mu_{i}\rangle\langle\mu_{i}|\,,(S.22)

and the radial interaction operator for an ordered particle pair withB^i​jα​β≡∑μUα​βμ​μ​|μi​μj⟩​⟨μi​μj|,\hat{B}_{ij}^{\alpha\beta}\equiv\sum_{\mu}U_{\alpha\beta}^{\mu\mu}|\mu_{i}\mu_{j}\rangle\langle\mu_{i}\mu_{j}|\,,(S.23)

within the same-mode approximation used in Eq. (S.13), so that the Hamiltonian can be equivalently written asH^intdiag=12∑i≠j[\displaystyle\hat{H}_{\rm int}^{\rm diag}=\frac{1}{2}\sum_{i\neq j}\Big[B^i​je​e​P^e(i)​P^e(j)+B^i​jg​g​P^g(i)​P^g(j)\displaystyle\hat{B}_{ij}^{ee}\hat{P}_{e}^{(i)}\hat{P}_{e}^{(j)}+\hat{B}_{ij}^{gg}\hat{P}_{g}^{(i)}\hat{P}_{g}^{(j)}+B^i​je​g(P^e(i)P^g(j)+P^g(i)P^e(j))].\displaystyle+\hat{B}_{ij}^{eg}\left(\hat{P}_{e}^{(i)}\hat{P}_{g}^{(j)}+\hat{P}_{g}^{(i)}\hat{P}_{e}^{(j)}\right)\Big]\,.(S.24)

This allows us to consider beyond-leading-order effects. In fact, since the radial thermal average of the pair interaction isTrr⁡(B^i​jα​β​ρ^rth)=U¯α​β\Tr_{r}(\hat{B}_{ij}^{\alpha\beta}\,\hat{\rho}_{r}^{\text{th}})=\bar{U}_{\alpha\beta}, we can write the interaction Hamiltonian (S.24) as the already found radially averaged part, plus fluctuations with zero thermal meanH^intdiag≈H^int(1)+V^ϕ\hat{H}_{\rm int}^{\rm diag}\approx\hat{H}_{\rm int}^{(1)}+\hat{V}_{\phi}(S.25)

up to radial fluctuation terms proportional only to the identity or total occupation operators, which do not affect the internal spin dynamics. Here,V^ϕ=12​∑i≠j∑α=e,gδ​Δ^i​j,α​P^α(i)​s^z(j)\hat{V}_{\phi}=\frac{1}{2}\sum_{i\neq j}\sum_{\alpha=e,g}\delta\hat{\Delta}_{ij,\alpha}\,\hat{P}_{\alpha}^{(i)}\hat{s}_{z}^{(j)}(S.26)

andTrr⁡(V^ϕ​ρ^rth)=0\Tr_{r}(\hat{V}_{\phi}\hat{\rho}_{r}^{\text{th}})=0.
Hereδ​Δ^i​j,α=(B^i​jα​e−U¯α​e)−(B^i​jα​g−U¯α​g)\delta\hat{\Delta}_{ij,\alpha}=(\hat{B}_{ij}^{\alpha e}-\bar{U}_{\alpha e})-(\hat{B}_{ij}^{\alpha g}-\bar{U}_{\alpha g})can be interpreted as the fluctuation of the collisional
transition shift of atomjj, conditioned on atomiibeing in stateα\alpha. This induces a non-unitary second-order Born-Markov contribution to the evolution of the spin density matrix[53,54]ρ^˙s|ϕ=−1ℏ2​∫0∞𝑑τ​Trr⁡[V^ϕ​(t),[V^ϕ​(t−τ),ρ^s​(t)⊗ρ^rth]],\dot{\hat{\rho}}_{s}\big|_{\phi}=-\frac{1}{\hbar^{2}}\int_{0}^{\infty}d\tau\,\Tr_{r}\left[\hat{V}_{\phi}(t),\left[\hat{V}_{\phi}(t-\tau),\hat{\rho}_{s}(t)\otimes\hat{\rho}_{r}^{\rm th}\right]\right]\,,(S.27)

which, assuming short-lived and approximately pair-local radial correlations, reduces to a contribution of the Lindbladian of this formγe​∑i≠j𝒟​[P^e(i)​s^z(j)]​ρ^s+γg​∑i≠j𝒟​[P^g(i)​s^z(j)]​ρ^s,\gamma_{e}\sum_{i\neq j}\mathcal{D}[\hat{P}_{e}^{(i)}\hat{s}_{z}^{(j)}]\hat{\rho}_{s}+\gamma_{g}\sum_{i\neq j}\mathcal{D}[\hat{P}_{g}^{(i)}\hat{s}_{z}^{(j)}]\hat{\rho}_{s},(S.28)

where, schematically,γα∼14​ℏ2​∫−∞∞𝑑τ​Trr⁡[δ​Δ^i​j,α​(τ)​δ​Δ^i​j,α​(0)​ρ^rth].\gamma_{\alpha}\sim\frac{1}{4\hbar^{2}}\int_{-\infty}^{\infty}d\tau\,\Tr_{r}\left[\delta\hat{\Delta}_{ij,\alpha}(\tau)\delta\hat{\Delta}_{ij,\alpha}(0)\hat{\rho}_{r}^{\rm th}\right].(S.29)

Since the jumps in Eq. (S.28) are diagonal in the internal basis, they produce pure dephasing and do not modify the populations. This provides a microscopic motivation for a density-dependent dephasing channel of the form used phenomenologically in optical-clock models[18,59]: the instantaneous clock shift of an atom fluctuates because its collisional shift depends on the internal state and radial state of its collision partners.
Following[18], we considered only the term dependent on the ground-state population in Eq. (S.28), settingγdeph=γg\gamma_{\text{deph}}=\gamma_{g}as a fit parameter in our analysis.

## Two-body losses in the single-mode model.

Under the same spatial-mode reduction used for the Hamiltonian,
Eq. (S.9) becomesL^e​e=Γe​e2​a^e2,L^e​g=Γe​g​a^e​a^g,\hat{L}_{ee}=\sqrt{\frac{\Gamma_{ee}}{2}}\,\hat{a}_{e}^{2},\qquad\hat{L}_{eg}=\sqrt{\Gamma_{eg}}\,\hat{a}_{e}\hat{a}_{g}\,,(S.30)

whereΓe​e,Γe​g\Gamma_{ee},\Gamma_{eg}contain thermally averaged
spatial-overlap factors.

To represent the losses in a local-spin-like model, we enlarge each local
space by one vacancy state that models all possible loss statesℋi=span⁡{|0⟩i,|g⟩i,|e⟩i}\mathcal{H}_{i}=\operatorname{span}\{|0\rangle_{i},|g\rangle_{i},|e\rangle_{i}\}.
For every unordered pairi<ji<j, the pair-removal jumps in this local space are thus modeled byJ^i​je​e\displaystyle\hat{J}_{ij}^{ee}=Γe​e​|0i​0j⟩​⟨ei​ej|,\displaystyle=\sqrt{\Gamma_{ee}}\,|0_{i}0_{j}\rangle\langle e_{i}e_{j}|,J^i​je​g,+\displaystyle\hat{J}_{ij}^{eg,+}=Γe​g|0i0j⟩⟨eg,+i​j|,\displaystyle=\sqrt{\Gamma_{eg}}\,|0_{i}0_{j}\rangle\langle eg,+_{ij}|,(S.31)

with|e​g,+i​j⟩=(|ei​gj⟩+|gi​ej⟩)/2|eg,+_{ij}\rangle=(|e_{i}g_{j}\rangle+|g_{i}e_{j}\rangle)/\sqrt{2}.
Their rate operators count the appropriate pairs:∑i<jJ^i​je​e⁣†​J^i​je​e\displaystyle\sum_{i<j}\hat{J}_{ij}^{ee\dagger}\hat{J}_{ij}^{ee}=Γe​e2​N^e​(N^e−1),\displaystyle=\frac{\Gamma_{ee}}{2}\hat{N}_{e}(\hat{N}_{e}-1),∑i<jJ^i​je​g,+†​J^i​je​g,+\displaystyle\sum_{i<j}\hat{J}_{ij}^{eg,+\dagger}\hat{J}_{ij}^{eg,+}=Γe​g​N^e​N^g,\displaystyle=\Gamma_{eg}\hat{N}_{e}\hat{N}_{g},(S.32)

with the second equation holding exactly strictly-speaking only in symmetrized spin manifolds.

Thus the single sink state|0⟩|0\rangleallows the pair losses to be included
directly at the reduced spin-model level. These terms are inherited from
the original continuum Lindbladian and are not generated by the
second-order radial elimination.

## Mean-field optical Bloch equations

LetN0N_{0}denote the initial number of atoms. In the
presence of loss we use the unnormalized one-body density matrixρe​e=⟨N^e⟩N0,ρg​g=⟨N^g⟩N0,ρe​g=⟨S^−⟩N0,\rho_{ee}=\frac{\langle\hat{N}_{e}\rangle}{N_{0}},\quad\rho_{gg}=\frac{\langle\hat{N}_{g}\rangle}{N_{0}},\quad\rho_{eg}=\frac{\langle\hat{S}_{-}\rangle}{N_{0}},(S.33)

whose tracePtot=ρe​e+ρg​g≤1{P_{\text{tot}}}=\rho_{ee}+\rho_{gg}\leq 1(S.34)

is the surviving atom fraction⟨N^⟩/N0\langle\hat{N}\rangle/N_{0}. The Bloch variables areu=2​Reρe​g,v=−2​Imρe​g,w=ρe​e−ρg​g,u=2\real\rho_{eg},\quad v=-2\imaginary\rho_{eg},\quad w=\rho_{ee}-\rho_{gg},(S.35)

so thatρe​e=(Ptot+w)/2\rho_{ee}=({P_{\text{tot}}}+w)/2,ρg​g=(Ptot−w)/2\rho_{gg}=({P_{\text{tot}}}-w)/2.

## Mean-field dissipative terms.

The dephasing channel (S.28) only affects coherences and not populations. Under permutation symmetry and mean-field factorization, it givesρ˙e​g|ϕ=−Γϕ​ρe​g,ρ˙e​e|ϕ=ρ˙g​g|ϕ=0,\dot{\rho}_{eg}\big|_{\phi}=-\Gamma_{\phi}\,\rho_{eg},\qquad\dot{\rho}_{ee}\big|_{\phi}=\dot{\rho}_{gg}\big|_{\phi}=0,(S.36)

whereΓϕ=N0−12​(γe​ρe​e+γg​ρg​g).\Gamma_{\phi}=\frac{N_{0}-1}{2}\left(\gamma_{e}\rho_{ee}+\gamma_{g}\rho_{gg}\right).(S.37)

Conversely, the pair-removal jumps affect all components of the one-body density matrix, and give the standard two-body loss equationsρ˙e​e|loss\displaystyle\dot{\rho}_{ee}\big|_{\rm loss}=−(N0−1)​(Γe​e​ρe​e+Γe​g​ρg​g)​ρe​e,\displaystyle=-(N_{0}-1)\left(\Gamma_{ee}\rho_{ee}+\Gamma_{eg}\rho_{gg}\right)\rho_{ee},ρ˙g​g|loss\displaystyle\dot{\rho}_{gg}\big|_{\rm loss}=−(N0−1)​Γe​g​ρe​e​ρg​g,\displaystyle=-(N_{0}-1)\Gamma_{eg}\rho_{ee}\rho_{gg},ρ˙e​g|loss\displaystyle\dot{\rho}_{eg}\big|_{\rm loss}=−Γloss​ρe​g,\displaystyle=-\Gamma_{\rm loss}\rho_{eg},(S.38)

withΓloss=N0−12​[Γe​g​(ρe​e+ρg​g)+Γe​e​ρe​e].\Gamma_{\rm loss}=\frac{N_{0}-1}{2}\left[\Gamma_{eg}(\rho_{ee}+\rho_{gg})+\Gamma_{ee}\rho_{ee}\right].(S.39)

The full dissipation of the coherence is thereforeρ˙e​g|diss=−(Γϕ+Γloss)​ρe​g.\dot{\rho}_{eg}\big|_{\rm diss}=-\left(\Gamma_{\phi}+\Gamma_{\rm loss}\right)\rho_{eg}.(S.40)

Equivalently, for the optical Bloch vector,u˙|diss\displaystyle\dot{u}\big|_{\rm diss}=−(Γϕ+Γloss)​u,\displaystyle=-\left(\Gamma_{\phi}+\Gamma_{\rm loss}\right)u,v˙|diss\displaystyle\dot{v}\big|_{\rm diss}=−(Γϕ+Γloss)​v,\displaystyle=-\left(\Gamma_{\phi}+\Gamma_{\rm loss}\right)v,w˙|loss\displaystyle\dot{w}\big|_{\rm loss}=−(N0−1)​Γe​e​(Ptot+w)24,\displaystyle=-(N_{0}-1)\Gamma_{ee}\frac{({P_{\text{tot}}}+w)^{2}}{4},(S.41)

together with Eqs. (S.34),(S.35).

## Inclusion of mean-field unitary terms.

The Bloch components evolve, under the spin Hamiltonian in the Main text, Eq. (1), asu˙\displaystyle\dot{u}=(δ−C​(N0−1)/ℏ)​v−2​χN0​ℏ​⟨S^z​S^y+S^y​S^z⟩,\displaystyle=(\delta-C(N_{0}-1)/\hbar)v-\frac{2\chi}{N_{0}\hbar}\left\langle\hat{S}_{z}\hat{S}_{y}+\hat{S}_{y}\hat{S}_{z}\right\rangle,v˙\displaystyle\dot{v}=−(δ−C​(N0−1)/ℏ)​u+Ω​w+2​χN0​ℏ​⟨S^z​S^x+S^x​S^z⟩,\displaystyle=-(\delta-C(N_{0}-1)/\hbar)u+\Omega w+\frac{2\chi}{N_{0}\hbar}\left\langle\hat{S}_{z}\hat{S}_{x}+\hat{S}_{x}\hat{S}_{z}\right\rangle,w˙\displaystyle\dot{w}=−Ω​v.\displaystyle=-\Omega v.(S.42)

Technically speaking, having introduced losses, theNNmultiplying the linear shiftCCshould have been promoted to the operatorN^=N^e+N^g\hat{N}=\hat{N}_{e}+\hat{N}_{g}, but we set it equal to its initial value, due to the small role of losses.
Under the mean-field closure⟨S^α​S^β+S^β​S^α⟩≈2​⟨S^α⟩​⟨S^β⟩,\langle\hat{S}_{\alpha}\hat{S}_{\beta}+\hat{S}_{\beta}\hat{S}_{\alpha}\rangle\approx 2\langle\hat{S}_{\alpha}\rangle\langle\hat{S}_{\beta}\rangle,(S.43)

and including the dissipative terms (S.41), one gets the mean-field optical Bloch equationsu˙\displaystyle\dot{u}=(δ−δ​νint​(w))​v−(Γϕ+Γloss)​u\displaystyle=(\delta-\delta\nu_{\rm int}(w))v-\left(\Gamma_{\phi}+\Gamma_{\rm loss}\right)uv˙\displaystyle\dot{v}=−(δ−δ​νint​(w))​u+Ω​w−(Γϕ+Γloss)​v\displaystyle=-(\delta-\delta\nu_{\rm int}(w))u+\Omega w-\left(\Gamma_{\phi}+\Gamma_{\rm loss}\right)vw˙\displaystyle\dot{w}=−Ω​v−(N0−1)​Γe​e​(Ptot+w)24,\displaystyle=-\Omega v-(N_{0}-1)\Gamma_{ee}\frac{({P_{\text{tot}}}+w)^{2}}{4}\,,(S.44)

whereℏ​δ​νint=C​(N0−1)+χ​N0​w\hbar\delta\nu_{\rm int}=C(N_{0}-1)+\chi N_{0}w, orℏ​δ​νint=C​(N0​Ptot−1)+χ​N0​w\hbar\delta\nu_{\rm int}=C(N_{0}{P_{\text{tot}}}-1)+\chi N_{0}w, in case a loss-weighted shift is considered at the mean-field level. For a clock interrogation timeTπ≪(N0​Γe​e)−1T_{\pi}\ll(N_{0}\Gamma_{ee})^{-1}the two-body loss terms in (S.44) can be neglected, and the first definition ofδ​νint\delta\nu_{\rm int}can be used, reducing our model to Eqs. (3) in the Main text.

## Relaxation rate measurementsFigure S1:Atomic fraction of the ground statePgP_{g}in a 1D (blue circles) and 2D (blue diamonds) and the atomic fraction of the excited statePeP_{e}in a 1D (red circles) and 2D (red diamonds) as a function of the hold time in the lattice.

The88Sr excited clock state suffers from two-body inelastic scattering. The two-body loss rate can generally be written asΓα​β=βα​β​∫d3​r​|w​(𝐫)|4=βα​β𝒱​(T,U0),\Gamma_{\alpha\beta}=\beta_{\alpha\beta}\int d^{3}r\,|w(\mathbf{r})|^{4}=\frac{\beta_{\alpha\beta}}{\mathcal{V}(T,U_{0})},(S.45)

sharing the same spatial dependence on the atomic wavefunction of the elastic interactionsUα​βU_{\alpha\beta}, condensed in the wavefunction volume𝒱=𝒱0​(∏jLj/ℓ0j)\mathcal{V}=\mathcal{V}_{0}(\prod_{j}L^{j}/\ell_{0}^{j}). In the case ofe−ee-einteraction, knowledge of the two-body density decayβe​e\beta_{ee}and direct measurements ofΓe​e\Gamma_{ee}andUα​βU_{\alpha\beta}can lead to a determination of the s-wave scattering lengthaα​βa_{\alpha\beta}[37].

Assuming constant sample temperature and same site volume along the optical lattice, the time evolution of the excited clock state population for each siteNe,iN_{e,i}can be described as follows:N˙e,i=−Ne,i/τ−Γe​e​Ne,i​(Ne,i−1)\dot{N}_{e,i}=-N_{e,i}/\tau-\Gamma_{ee}N_{e,i}(N_{e,i}-1)(S.46)

whereτ\tauis the lifetime of the atoms trapped in the lattice due to background gas scattering and lattice scattering. Integrating Eq.S.46, and summing over all lattice sites, the time evolution of the total number of atomsNe​(t)N_{e}(t), in the large number limit, can be written as follows:Ne​(t)=∑iNi,e​(0)​e−t/τ1+Ni,e​(0)​τ​Γe​e​(1−e−t/τ)N_{e}(t)=\sum_{i}N_{i,e}(0)\frac{e^{-t/\tau}}{1+N_{i,e}(0)\tau\Gamma_{ee}(1-e^{-t/\tau})}(S.47)

whereNi,e​(0)N_{i,e}(0)is the initial atom number in theii-lattice site. We assume thatτ\taudoes not depend on the particular energy state, so that it can be measured by looking at the trap losses of the ground-state population, which do not suffer from significant two-body losses.

We measured the relaxation of trap populations in both the 1D and 2D lattice cases under typical experimental conditions, as shown in Fig.S1. We use Eq. (S.47) as a fit function to the experimental data for both the 1D and 2D lattice geometry. In this fit procedure, the values ofτ\tauare constrained to be equal to the value extracted fromNgN_{g}time evolution and reported in TableS1for the 1D and 2D geometry. Finally, the valuesNe,i​(0)N_{e,i}(0)for each siteiiare computed considering a Gaussian distributionGi1DG^{\text{1D}}_{i}(Gi2​D)G^{2D}_{i})along the trapping region with a spatial dimension ofσM​O​T=192​(7)µ​m\sigma_{MOT}=$192(7)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}$(σz=70​(5)µ​m\sigma_{z}=$70(5)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}$andσy=12​(4)µ​m\sigma_{y}=$12(4)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}$) with an initial number of atoms ofNe​(0)=1.3​(1)×105N_{e}(0)=$1.3(1)\text{\times}{10}^{5}$. The fit results are reported in the Tab.S1.ParameterValueReferenceτ1D\tau^{\text{1D}}14​(1)s14(1)\text{\,}\mathrm{s}This workτ2​D\tau^{2D}14.2​(4)s14.2(4)\text{\,}\mathrm{s}This workβe​e1D\beta_{ee}^{\text{1D}}21​(7)µ​m3/s21(7)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}^{3}\mathrm{/}\mathrm{s}This workβe​e2​D\beta_{ee}^{2D}10.0​(15)µ​m3/s10.0(15)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}^{3}\mathrm{/}\mathrm{s}This workβe​e\beta_{ee}4.0​(2.5)µ​m3/s4.0(2.5)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}^{3}\mathrm{/}\mathrm{s}[18]19​(12)µ​m3/s19(12)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}^{3}\mathrm{/}\mathrm{s}[38]26.2​(6)µ​m3/s26.2(6)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}^{3}\mathrm{/}\mathrm{s}[39]Table S1:Parameters and fit results obtained from the experimental data reported in Fig.S1.

We also characterize the elastic dephasing rate, introduced in the previous section, in our88Sr clock by measuring Rabi oscillations at different atom numbers while keeping fixed the lattice depth. A sample measurement is shown in Fig.S2.Figure S2:(a) Rabi oscillation measurement atU0=80​(1)​ErU_{0}=80(1)\,E_{r}, andNtot≃7×103N_{\text{tot}}\simeq 7\times 10^{3}. (b) Lineshape of the clock transition at the peak of the excitation, corresponding to the Rabiπ\pi-pulse at 15 ms.

For each lattice site occupation, the dynamics defined by the set of ordinary differential equations arising fromS.44, including two-body losses and assumingδ=δ​νint\delta=\delta\nu_{\rm int}, is numerically integrated up to the interrogation time, and the total observed populations are computed by summing over all the lattice sites. In the fitting procedure, all the parameters are fixed, except the elastic dephasing coefficientγdeph\gamma_{\rm deph}and the effective Rabi frequencyΩ\Omega. The resulting density dephasing rate isγdeph​𝒱=\gamma_{\rm deph}\mathcal{V}=186​(16)µ​m3​s−1186(16)\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}^{3}\,\mathrm{s}^{-1}. This corresponds to a dephasing rate at typical lattice clock conditions of about1.3s−11.3\text{\,}\mathrm{s}^{-1}.


## 


- 


Major funding support from
