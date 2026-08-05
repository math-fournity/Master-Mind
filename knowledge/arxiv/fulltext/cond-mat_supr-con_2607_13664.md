# Direct observation of photon-induced vortices in superconducting films

**arXiv ID**: 2607.13664v1
**Authors**: Takeshi Jodoi, Fuminori Hirayama, Tetsuya Tsuruta, Takahiro Kikuchi, Daiji Fukuda
**Published**: 2026-07-15
**Categories**: cond-mat.supr-con, quant-ph
**Comments**: Submitted to Physical Review Applied. Presented at SPW 2026
**HTML URL**: https://arxiv.org/html/2607.13664v1

## Abstract

Nucleation of vortex-antivortex pairs (VAPs) is believed to play a central role in the photon detection mechanism of superconducting detectors; however, their direct dynamic observation has remained challenging. Here, we report the direct observation of photon-induced VAP dynamics in a current-carrying superconductor as quantized voltage signals following photon absorption. The observed signals are interpreted as discrete phase-slip events, where each vortex traversal induces a 2-pi phase change of the superconducting order parameter, resulting in a quantized voltage pulse whose time integral is given by the magnetic flux quantum. We analyze the resulting quantized signals as a function of bias current, base temperature, and input photon-number states, and find that the number of VAPs generated per absorbed photon becomes effectively stabilized under specific conditions. Under these conditions, we demonstrate photon-number-resolving capability by directly counting phase-slip-induced voltage quanta. Our results reveal a detection mechanism governed by phase dynamics rather than conventional resistive transitions. We further show that photon-number resolution emerges when the fluctuation of photon-induced vortex-antivortex pair generation becomes statistically suppressed. These findings establish a new route toward photon-number-resolving detection based on phase-slip counting and open opportunities for high-speed superconducting detectors for quantum optics and photonic quantum technologies.

## Full Text

Direct observation of photon-induced vortices in superconducting films

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.13664v1 [cond-mat.supr-con] 15 Jul 2026

## Direct observation of photon-induced vortices in superconducting filmsTakeshi JodoiNational Institute of Advanced Industrial Science and Technology, 1-1-1, Umezono, Tsukuba, Ibaraki 305-8563, JapanSchool of Engineering, The University of Tokyo, 2-11-16, Yayoi, Bunkyo, Tokyo 113-8656, JapanFuminori HirayamaNational Institute of Advanced Industrial Science and Technology, 1-1-1, Umezono, Tsukuba, Ibaraki 305-8563, JapanTetsuya TsurutaNational Institute of Advanced Industrial Science and Technology, 1-1-1, Umezono, Tsukuba, Ibaraki 305-8563, JapanTakahiro KikuchiNational Institute of Advanced Industrial Science and Technology, 1-1-1, Umezono, Tsukuba, Ibaraki 305-8563, JapanDaiji FukudaNational Institute of Advanced Industrial Science and Technology, 1-1-1, Umezono, Tsukuba, Ibaraki 305-8563, Japan

## Abstract

Nucleation of vortex–antivortex pairs (VAPs) is believed to play a central role in the photon detection mechanism of superconducting detectors;
however, their direct dynamic observation has remained challenging.
Here, we report the direct observation of photon-induced VAP dynamics in a current-carrying superconductor as quantized voltage signals following photon absorption.
The observed signals are interpreted as discrete phase-slip events, where each vortex traversal induces a2​π2\piphase change of the superconducting order parameter,
resulting in a quantized voltage pulse whose time integral is given by the magnetic flux quantumΦ0\Phi_{0}.
We analyze the resulting quantized signals as a function of bias current, base temperature, and input photon-number states,
and find that the number of VAPs generated per absorbed photon becomes effectively stabilized under specific conditions.
Under these conditions, we demonstrate photon-number-resolving capability by directly counting phase-slip-induced voltage quanta.
Our results reveal a detection mechanism governed by phase dynamics rather than conventional resistive transitions.
We further show that photon-number resolution emerges when the fluctuation of photon-induced vortex–antivortex pair generation becomes statistically suppressed.
These findings establish a new route toward photon-number-resolving detection based on phase-slip counting and open opportunities for high-speed superconducting
detectors for quantum optics and photonic quantum technologies.††preprint:APS/123-QED††preprint:Submitted to Physical Review Applied

## IIntroduction

The detection of single photons using superconducting devices is a key technology for quantum information, sensing, and optical communication. Conventional superconducting photon detectors,
such as transition-edge sensors (TESs)[7,15]and superconducting nanowire single-photon detectors
(SNSPDs)[3,9,10],
rely on photon-induced suppression of superconductivity and the resulting resistive response.

In these detectors, photon absorption creates a nonequilibrium region in which the superconducting order parameter is locally suppressed. This process is commonly described by hotspot-based models,
including early theoretical descriptions[12,14]and subsequent refinements and analyses[17,16,11,5].
Under a bias current, such nonequilibrium regions facilitate the generation of multiple vortex–antivortex pairs (VAPs), whose motion leads to Joule heating and can trigger the formation of a normal conducting domain.

In particular, vortex-based descriptions have been proposed, where photon absorption induces vortex–antivortex pair (VAP) nucleation through the temporal suppression and recovery of the superconducting
order parameter[2,17,13].
The number of such events is expected to depend on the ratio between the strip width and the superconducting coherence length[17].
In conventional SNSPDs with relatively narrow strips, multiple VAPs are generated, and their motion results in the formation of a resistive region. The detection signal is therefore governed
by the resulting resistive transition, which depends on the bias current, thermal relaxation, and circuit conditions.

In addition, photon-number-resolving capabilities have also been actively explored in superconducting nanowire detectors[8].In contrast to these conventional approaches, the present work focuses on the nonequilibrium phase dynamics associated with photon absorption in a current-carrying superconductor.
Rather than relying on the formation of a macroscopic resistive state,
we investigate the regime in which only a small number of vortex–antivortex pairs are generated and their dynamics can be directly resolved.
The conceptual difference between these two detection mechanisms is illustrated schematically in Fig.1.

Photon absorption locally suppresses the superconducting order parameter, forming a transient nonequilibrium region (hotspot-like region).
This region should not be confused with the normal core of a vortex; rather, it represents a temporary reduction of the superconducting condensate.
Under bias current, the nonuniform current distribution leads to an instability in the phase gradient of the superconducting order parameter.
This instability is released through the nucleation of vortex–antivortex pairs, which corresponds to discrete phase-slip events.

When a vortex traverses the superconducting strip, the superconducting phase undergoes a2​π2\pichange.
According to the Josephson relation,V=ℏ2​e​d​ϕd​t,{\color[rgb]{0,0,0}V=\frac{\hbar}{2e}\frac{d\phi}{dt},}

each phase-slip event produces a voltage pulse whose time integral satisfies∫V​(t)​𝑑t=Φ0,{\color[rgb]{0,0,0}\int V(t)\,dt=\Phi_{0},}

whereΦ0=h/2​e\Phi_{0}=h/2eis the flux quantum. Thus, the observed voltage pulses directly reflect the underlying phase evolution associated with vortex motion.Figure 1:Schematic illustration of photon detection mechanisms:
(a) conventional resistive detection, in which photon absorption generates many vortex–antivortex pairs, resulting in heating, normal-domain formation, and a resistive response;
and (b) VAP-mediated phase-slip detection (VBD in this work), in which only a few VAPs are generated and directly detected as quantized voltage pulses. The lower panels illustrate the transient suppression and recovery of the superconducting order parameterΔ​(t)\Delta(t)and the corresponding phase evolutionϕ​(t)\phi(t)associated with discrete phase-slip events.

In this work, we demonstrate the direct observation of photon-induced vortex–antivortex dynamics through quantized voltage signals.
By resolving the number of phase-slip events occurring after photon absorption,
we show that photon-number information does not automatically emerge from quantized phase-slip signals.
Instead, it appears only when the fluctuation of the VAP generation process becomes sufficiently suppressed.
Under these conditions, the VAP statistics approach the photon statistics of the incident light, enabling photon-number resolution through direct phase-slip counting.

The key distinction of this approach is that the detection signal is governed by discrete phase-slip events rather than by a continuous resistive transition.
While the peak amplitude of the voltage signal depends on the readout circuit and bias current, the time-integrated voltage is determined solely by the phase change and remains quantized in units ofΦ0\Phi_{0}.
This allows direct access to the number of phase-slip events induced by photon absorption.In the following, we refer to this device as a vortex-based detector (VBD).

The remainder of this paper is organized as follows. We first describe the device structure and measurement setup,
and then present experimental observations of quantized voltage pulses.
Finally, we analyze the dependence of the phase-slip dynamics on bias current, temperature, and photon number, and discuss the implications for photon-number-resolving detection.

## IIExperiment

## II.1Experimental Methods

The VBD used in the experiment consisted of a bilayer superconducting film composed of titanium and gold with thicknesses of 20 nm and 10 nm, respectively.
This bilayer film was patterned into a square strip measuring8µ​m8\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}×\times8µ​m8\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}. The substrate of this device was a Si wafer. To enhance the detection efficiency, a Ti (5 nm)/Au (50 nm)/Ti (5 nm) was sputtered to form an Au mirror, and anSiO2\rm{SiO_{2}}layer was subsequently deposited on top of the Au mirror to electrically insulate the active area. The titanium layers in this trilayer served as an adhesion layer. The Ti/Au bilayer was then deposited on theSiO2\rm{SiO_{2}}layer, and an additional five-layerSiO2/Si3​N4\rm{SiO_{2}}/\rm{Si_{3}N_{4}}stacks were sputtered to form an anti-reflection layer. Niobium superconducting leads were fabricated on opposite sides of the square to read the VBD response signal.
The superconducting properties of the VBD were measured in a dilution refrigerator and are summarized in Table1.The device performance is comparable to previously reported low-TcT_{\mathrm{c}}optical TES devices[4].

Based on the measured superconducting parameters, we estimatedξGL​(0)=62.5​nm\xi_{\mathrm{GL}}(0)=62.5~\mathrm{nm}forTc=128​mKT_{c}=128~\mathrm{mK}andD=1.67​cm2/sD=1.67~\mathrm{cm}^{2}/\mathrm{s}[6,7].The coherence length was not directly measured from magnetic-field-dependent measurements, but estimated from the diffusion constant using standard relations.Thus, the ratiow/ξGL​(0)≈128w/\xi_{\mathrm{GL}}(0)\approx 128for our VBD.
In contrast to conventional narrow SNSPDs, where rapid formation of extended resistive regions can dominate the response depending on the bias current,
this large ratio places the device in a regime in which only a limited number of vortex–antivortex pairs are generated,
enabling direct observation of discrete phase-slip events.

Figure2(a) shows the readout circuit for the VBD, where the VBD and an inductor with inductanceLLare shunted by a resistorRsR_{\mathrm{s}}.
A bias currentIbI_{\mathrm{b}}is supplied to the VBD from an external current source. The VBD is cooled to a base temperatureTb<TcT_{\mathrm{b}}<T_{\mathrm{c}}so that under equilibrium conditions, almost all ofIbI_{\mathrm{b}}flows through the VBD. The VBD is optically coupled to a fiber,
and a laser pulse with an average photon numberμin\mu_{\mathrm{in}}is delivered to it through the fiber.The wavelength of the incident photons was1526nm1526\text{\,}\mathrm{n}\mathrm{m}.After photon absorption in the VBD, a voltage signalΔ​v​(t)\Delta v(t)results from either the formation of resistance or the induced electromotive force due to the VAP motion, which is read out by the current amplifier of a superconducting quantum interference device (SQUID). From the observed current changeΔ​I​(t)\Delta I(t)at the SQUID output, we obtainΔ​v​(t)=Rs×Δ​I​(t)\Delta v(t)=R_{\mathrm{s}}\times\Delta I(t)

with a bandwidth of0.35/τel0.35/\tau_{\mathrm{el}}, where we define the electrical time constantτel=L/Rs\tau_{\mathrm{el}}=L/R_{\mathrm{s}}.

For reference, the device can also exhibit a resistive response similar to electrothermal-feedback-based TES detection. However, in the present work we focus on a regime where the device remains superconducting and the detection signal arises from discrete phase-slip events associated with vortex motion. Figure2(b) illustrates the VBD structure fabricated on a key-shaped Si substrate, and Fig.2(c) shows the Ti/Au active area of the VBD together with the niobium electrodes. Table1summarizes representative ETF-TES-mode performance metrics for reference.To determine the appropriate operating conditions for the VBD mode, in particular the bias current relative to the critical current,
we first investigated the dependence of the critical currentIcI_{\mathrm{c}}on the base temperatureTbT_{\mathrm{b}}by applying a triangular-shaped current to the VBD.
The critical currentIcI_{\mathrm{c}}was defined as the current at which the resistance of the VBD exceeded3​m​Ω3~\mathrm{m\Omega}.The temperature dependence ofIcI_{\mathrm{c}}is shown in Fig.3(a).
At lower values ofTbT_{\mathrm{b}},Ic​(T)I_{\mathrm{c}}(T)is almost constant.We evaluatedIc​(0)I_{\mathrm{c}}(0)= 7.36µ​A\mathrm{\SIUnitSymbolMicro}\mathrm{A}by extrapolating the data obtained in the range30​mK<Tb<50​mK30~\mathrm{mK}<T_{\mathrm{b}}<50~\mathrm{mK}.Ic​(T)I_{\mathrm{c}}(T)gradually vanishes asTbT_{\mathrm{b}}approachesTcT_{\mathrm{c}}.Table 1:Performance of the superconducting device in the ETF-TES mode.MaterialTi (20 nm)/Au (10 nm)Size8µ​m8\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}×\times8µ​m8\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}Critical temperatureTcT_{\mathrm{c}}128mK\mathrm{m}\mathrm{K}Effective time constantτeff\tau_{\mathrm{eff}}4.82µ​s\mathrm{\SIUnitSymbolMicro}\mathrm{s}(Tb=6T_{\mathrm{b}}=6mK)29.1µ​s\mathrm{\SIUnitSymbolMicro}\mathrm{s}(Tb=117T_{\mathrm{b}}=117mK)Normal resistanceRnR_{\mathrm{n}}2.87Ω\mathrm{\SIUnitSymbolOhm}Detection efficiencyη\eta76 %Critical currentIc​(T→0)I_{\mathrm{c}}(T\to 0)7.36µ​A\mathrm{\SIUnitSymbolMicro}\mathrm{A}(extrapolated)Figure 2:Readout circuit for the VBD. The rectangle with an arrow represents the VBD as the photon detection device.RsR_{\mathrm{s}}: shunt resistance;IbI_{\mathrm{b}}: bias current;LL: kinetic inductance;Δ​I\Delta{I}: change in current flowing in this readout circuit. (b) The VBD is fabricated on a key-shaped Si substrate to improve alignment between the optical fiber and the VBD. (c) The active area of the VBD. This active area consists of the Ti (20 nm)/Au (10 nm) bilayer, and the electrodes are made of niobium.

## II.2Photon Response of the VBD

To evaluate the photon response, we irradiated the VBD with photons while applying a bias currentIb<IcI_{\mathrm{b}}<I_{\mathrm{c}}, ensuring that the device remained in its superconducting equilibrium state. This condition closely resembles the standard operating mode of SSPDs.
Figure3(b) shows the signals observed underIb=5.0I_{\mathrm{b}}=5.0µ​A\mathrm{\SIUnitSymbolMicro}\mathrm{A},Tb=6​mKT_{\mathrm{b}}=6~\mathrm{mK},Rs=21.4​m​ΩR_{\mathrm{s}}=21.4~\mathrm{m\Omega}, andμin=10\mu_{\mathrm{in}}=10photons/pulse.Here,μin\mu_{\mathrm{in}}denotes the average number of incident photons per pulse.The corresponding average number of detected photons is given byη​μin\eta\mu_{\mathrm{in}}, whereη\etais the detection efficiency.The pulse heights are quantized into discrete voltage steps in response to the incident laser pulses, a behavior fundamentally different from that of SSPDs.

The measured time constant was445​ns445~\mathrm{ns}, approximately ten times faster than that in the ETF-TES mode (see Table I).
To clarify whether quantization originates from resistance or voltage changes, we measured the dependence ofΔ​v\Delta vonIbI_{\mathrm{b}}andTbT_{\mathrm{b}}.
IfΔ​v\Delta vis caused by a resistance changeΔ​R\Delta R, it will scale proportionally withIbI_{\mathrm{b}}becauseΔ​R\Delta Rremains nearly constant at a fixedTbT_{\mathrm{b}}. Likewise, for a constantIbI_{\mathrm{b}},Δ​v\Delta vwill vary withTbT_{\mathrm{b}}because the heat capacity of the VBD changes with the temperatureTbT_{\mathrm{b}}.

Figure4shows the pulse-height distribution forμin=5\mu_{\mathrm{in}}=5photons/pulse, including markers for the peak positions and an overlaid envelope curve.
Figure4(a) and4(b), obtained atTb=6​mKT_{\mathrm{b}}=6~\mathrm{mK}, demonstrate that increasingIbI_{\mathrm{b}}from4µ​A4\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}to6µ​A6\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}produces additional peaks, even at the same photon input. Similarly, for a constantIbI_{\mathrm{b}}, thepeak indexincreases asTbT_{\mathrm{b}}rises from63​mK63~\mathrm{mK}to91​mK91~\mathrm{mK}. Across all conditions, the voltage pulses remain quantized at intervals of approximately0.45​nV0.45~\mathrm{nV}, forming discrete peaks regardless ofIbI_{\mathrm{b}}orTbT_{\mathrm{b}}.

In Fig.4(d), pulses with amplitudes exceeding 8 nV are not observed.
When the pulse height at single peak is 0.45 nV, the current diverted to the shunt resistor is approximately0.2µ​A0.2\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}.
Thus, the number of pulse peaks is determined by the bias current. Therefore, the pulse heights in Fig.4(d) are truncated at around 8 nV because theIb=I_{\mathrm{b}}=3µ​A3\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}.
Furthermore, the minimum peak amplitude in Fig.3(b) is approximately an order of magnitude smaller than that in Fig.4.
This difference is attributed to the change in the electrical time constant resulting from the different value ofRsR_{\mathrm{s}}.These results indicate that photon detection in a VBD is governed by a mechanism fundamentally distinct from that of resistance variation.
Notably, Fig.4(b) and4(d), whereIbI_{\mathrm{b}}orTbT_{\mathrm{b}}is close toIcI_{\mathrm{c}}orTcT_{\mathrm{c}}, respectively,
exhibit periodic modulations of the peak counts. These modulations are evident from the envelope formed by connecting the peak maxima in the figure.This behavior indicates enhanced fluctuations in the number of VAP events under these operating conditions, suggesting that the VAP generation process is not fully stabilized and motivating the statistical analysis presented in Section III.Figure 3:(a) Experimental data showing the dependence of the critical current on the base temperature.
These experimental data of the critical current are obtained from the current–voltage characteristics, and the dotted line is extrapolated to determineIc​(T=0​mK)I_{\mathrm{c}}(T=0\,\rm{mK}).
(b) Recorded signals atIb=I_{\rm{b}}=5.0µ​A5.0\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A},Tb=T_{\rm{b}}=6mK6\text{\,}\mathrm{m}\mathrm{K},Rs=21.4R_{\rm{s}}=21.4m​Ω\mathrm{m\Omega}, andμin=10\mu_{\rm{in}}=10photons per pulse. Under this condition, the time constant of the VBD isτ=445\tau=445ns.Figure 4:Pulse-height distributions under four different experimental conditions, where the peak positions are marked.The envelope curves are included only as visual guides for peak evolution and do not represent a theoretical model.(a)Ib=I_{\rm b}=4.0µ​A4.0\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A},Tb=6​mKT_{\rm b}=6~\mathrm{mK},μin=5\mu_{\rm in}=5photons per pulse;
(b)Ib=I_{\rm b}=6.0µ​A6.0\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A},Tb=6​mKT_{\rm b}=6~\mathrm{mK},μin=5\mu_{\rm in}=5photons per pulse;
(c)Ib=I_{\rm b}=3.0µ​A3.0\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A},Tb=63​mKT_{\rm b}=63~\mathrm{mK},μin=5\mu_{\rm in}=5photons per pulse;
(d)Ib=I_{\rm b}=3.0µ​A3.0\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A},Tb=91​mKT_{\rm b}=91~\mathrm{mK},μin=5\mu_{\rm in}=5photons per pulse.In all cases, discrete peaks are observed, where each peak corresponds to the number of phase-slip events. The peak structure depends on both bias currentIbI_{\rm b}and base temperatureTbT_{\rm b}, indicating that the number of generated VAPs varies systematically with the operating conditions.Figure 5:(a) Relationship between voltage–time integral at each bias current and magnetic flux quantum. We obtained these data fromIb=I_{\mathrm{b}}=1µ​A1\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}to6µ​A6\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}atTb=T_{\mathrm{b}}=6mK6\text{\,}\mathrm{m}\mathrm{K}, following theIbI_{\mathrm{b}}dependency in Fig.3(a). (b) Relationship between voltage–time integral at each base temperature and magnetic flux quantum.
The data was obtained fromTb=T_{\mathrm{b}}=52mK52\text{\,}\mathrm{m}\mathrm{K}to98mK98\text{\,}\mathrm{m}\mathrm{K}(52mK52\text{\,}\mathrm{m}\mathrm{K},63mK63\text{\,}\mathrm{m}\mathrm{K},73mK73\text{\,}\mathrm{m}\mathrm{K},83mK83\text{\,}\mathrm{m}\mathrm{K},92mK92\text{\,}\mathrm{m}\mathrm{K},98mK98\text{\,}\mathrm{m}\mathrm{K}) atIb=I_{\mathrm{b}}=3µ​A3\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}, following theTbT_{\mathrm{b}}dependency in Fig.3(a). AtTbT_{\mathrm{b}}= 98 mK, the voltage–time integral is calculated from the time constant of the first stage in the averaged pulse.

## IIIPhoton detection mechanism based on phase-slip dynamics

## III.1Quantization of Signal Waveforms in Units of Magnetic Flux Quantum

As discussed in the previous section,the observed signal in the VBD mode does not primarily originate from the generation of resistance following photon absorption because the minimum pulse integral remains independent of bothIbI_{\mathrm{b}}andTbT_{\mathrm{b}}.Instead, we interpret the observed voltage in terms of the phase evolution of the superconducting order parameter.
According to the Josephson relation,V​(t)=ℏ2​e​d​ϕd​t,{\color[rgb]{0,0,0}V(t)=\frac{\hbar}{2e}\frac{d\phi}{dt},}(1)

whereϕ\phiis the superconducting phase. When a vortex traverses the superconducting strip, the phase changes by2​π2\pi, and therefore the time-integrated voltage satisfies∫V​(t)​𝑑t=ℏ2​e​Δ​ϕ=nVAP​Φ0,{\color[rgb]{0,0,0}\int V(t)\,dt=\frac{\hbar}{2e}\Delta\phi=n_{\mathrm{VAP}}\Phi_{0},}(2)

wherenVAPn_{\mathrm{VAP}}denotes the number of phase-slip events (or equivalently the number of traversing VAPs) andΦ0=h/2​e\Phi_{0}=h/2eis the flux quantum.

From this point of view, we obtained the voltage–time integral in Eq. (2) for the minimum-amplitude pulses under different experimental conditions involvingIbI_{\mathrm{b}}andTbT_{\mathrm{b}}. Figure5(a) and5(b) show the dependence of this quantity on the bias current and base temperature, respectively. In Fig.4, the voltage pulses remain quantized with a constant interval of approximately 0.45 nV. Therefore, we extracted the waveform corresponding to the first peak index and calculated its voltage–time integral to discuss its dependence onIbI_{\mathrm{b}}andTbT_{\mathrm{b}}. AtTb=98T_{\mathrm{b}}=98mK, the first-peak statistics were insufficient, so we instead used the waveform corresponding to peak index 3 and divided the resulting integral by the peak index to compare with the single-event value.

For all experimental conditions, the minimum pulse integral remains almost constant and close to the magnetic flux quantumΦ0=2.07×10−15​Wb\Phi_{0}=2.07\times 10^{-15}~\mathrm{Wb}. The value does not depend onRsR_{\mathrm{s}}. These results show that the minimum-amplitude voltage pulse corresponds to a single phase-slip event, i.e.,nVAP=1n_{\mathrm{VAP}}=1.

Here, we assume that the quantized pulse shape originates from the quantum numbernVAPn_{\mathrm{VAP}}and examine the dependence ofΦ\PhionnVAPn_{\mathrm{VAP}}.
Figure 6(a) shows the results under two different experimental conditions with respect toIbI_{\mathrm{b}}andTbT_{\mathrm{b}}. Specifically, we define case 1 asIb=I_{\mathrm{b}}=6µ​A6\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}andTb=6​mKT_{\mathrm{b}}=6~\mathrm{mK},
and case 2 asIb=I_{\mathrm{b}}=3µ​A3\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}andTb=98​mKT_{\mathrm{b}}=98~\mathrm{mK}.
For case 1, the value ofΦ\Phiis proportional tonVAPn_{\mathrm{VAP}}up to approximately 17, which clearly indicates that the observed signals in Fig. 3(b) are quantized according tonVAPn_{\mathrm{VAP}}. However, fornVAP>17n_{\mathrm{VAP}}>17, this proportionality is no longer valid. Under the conditions of case 2, the value ofΦ\Phisignificantly exceedsΦ0\Phi_{0}even for small values ofnVAPn_{\mathrm{VAP}}.
To investigate this, we focus on the pulse shape of the observed voltage signals. Figure 6(b) shows an example of the averaged pulse shape used for the decomposition analysis.
Apparently, the signal shape consists of two exponential components with distinct time constants, which is completely different from the shape shown in Fig. 3(b).Figure 6:(a) Dependence of the voltage–time integral of individual pulse peaks on the peak index. Closed circles and rectangles represent∫v​𝑑t\int{v}dtof the obtained average pulse, whereas the results obtained by integrating theτfast\tau_{\mathrm{fast}}component of the separated signals are replotted as open circles or rectangles. The open symbols exhibit good consistency with the straight line having a slope ofΦ0\Phi_{0}. (b) Averaged pulse obtained from the VBD atTbT_{\rm{b}}= 98 mK. The time constant of this waveform appears to increase in the later part owing to Joule heating.

To separate the two components, we fit the signal withf​(t)=a​exp⁡(−t/τfast)+b​exp⁡(−t/τslow),f(t)=a\exp(-t/\tau_{\mathrm{fast}})+b\exp(-t/\tau_{\mathrm{slow}}),(3)

which givesa=0.397​nVa=0.397~\mathrm{nV},b=0.207​nVb=0.207~\mathrm{nV},τfast=\tau_{\mathrm{fast}}=5.06µ​s5.06\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{s}, andτslow=\tau_{\mathrm{slow}}=32.4µ​s32.4\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{s}.
We performed this separation for the other signals for eachnVAPn_{\mathrm{VAP}},
and the results obtained by integrating theτfast\tau_{\mathrm{fast}}component of the separated signals are replotted in Fig. 6(a) as open circles or rectangles.

In this case, all the values are proportional toΦ0\Phi_{0}withnVAPn_{\mathrm{VAP}}, which shows that the first component of Eq. (3) can
be attributed to the traversal of the magnetic flux quanta, consistent with the expected phase-slip dynamics.

In addition,τslow\tau_{\mathrm{slow}}in the slow component of Eq. (3) is close to the ETF-TES time constantτETF=29.1​µ​s\tau_{\mathrm{ETF}}=29.1~$\mathrm{\SIUnitSymbolMicro}\mathrm{s}$,
measured atTb=117​mKT_{\mathrm{b}}=117~\mathrm{mK}, as shown in Table1.In the ETF-TES operation, the effective time constant increases as the base temperature approaches the critical temperature.Therefore, the slow component can be attributed to the generation of a resistive change in the transition region after the traversal of the magnetic flux quanta.Figure 7:(a) Dependence of the second-order correlation functiongVAP(2)g^{(2)}_{\mathrm{VAP}}, calculated from the number of observed vortex–antivortex (VAP) events per pulse, on the bias currentIbI_{\rm b}at a base temperature ofTb=97T_{\rm b}=97mK.
(b) Dependence ofgVAP(2)g^{(2)}_{\mathrm{VAP}}on the base temperatureTbT_{\rm b}at a fixed bias current ofIb=3µ​AI_{\rm b}=$3\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}$.
In both cases,gVAP(2)g^{(2)}_{\mathrm{VAP}}approaches unity with increasingIbI_{\rm b}orTbT_{\rm b}, corresponding to the Poisson limit.
These results indicate that fluctuations in the number of VAP events per pulse are suppressed, identifying the operating conditions under which
the VAP generation process becomes effectively stabilized.

## III.2Signal Response Speed

In the VBD operation mode, the signal response time is in the order ofτ∼w/v\tau\sim w/v, wherewwandvvdenote the strip width of the superconducting film and traversing velocity of the VAPs, respectively. The velocityvvfor the titanium/gold superconducting film is not known; however, previous research reports that the velocity for an NbC superconductor is approximately104​m/s10^{4}~\mathrm{m/s}[1].
Assuming this estimation holds for the TiAu film, the signal response time can be approximated asτ∼800​ps\tau\sim 800~\mathrm{ps}forw=w=8µ​m8\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{m}. Consequently, the VBD mode is expected to exhibit a substantially faster response when compared with that of the ETF mode. Nevertheless, the observed time constant in Fig. 3(b) is restricted toτ=445​ns\tau=445~\mathrm{ns}. This limitation arises from the bandwidth of the bias circuit depicted in Fig. 2, where the signal response is governed by the electrical time constantτelc=L/Rs\tau_{\mathrm{elc}}=L/R_{\mathrm{s}}. We estimatedL=9.8​nHL=9.8~\mathrm{nH}by measuring the noise spectrum of the VBD, which yieldsτelc=458​ns\tau_{\mathrm{elc}}=458~\mathrm{ns}forRs=21.4​m​ΩR_{\mathrm{s}}=21.4~\mathrm{m\Omega}.
This value is in good agreement with the time constant of the observed signals.
Therefore, a wide-bandwidth readout is crucial for achieving an intrinsically faster signal response in the VBD.

## III.3PNR Capability

As discussed in the previous section, the response signal is quantizedaccording to the number of phase-slip events. This quantization enables photon-number resolution
by directly counting vortex–antivortex (VAP) events.To quantitatively evaluate this behavior, we introduce the average number
of traversing VAPs per absorbed photon, denoted asnVAPn_{\mathrm{VAP}},
which refers to the average number of traversing VAPs per absorbed photon
as defined in Eq. (4). This quantity provides a measure of the
conversion between absorbed photons and the resulting phase-slip events.

The average number of traversing VAPs is obtained from the observed distribution of phase-slip events using the following equation:nVAP=1η​μin​∑n=0n​P​(n),{\color[rgb]{0,0,0}n_{\mathrm{VAP}}=\frac{1}{\eta\,{\mu}_{\mathrm{in}}}\sum_{n=0}n\,P(n),}(4)

whereP​(n)P(n)represents the probability of observingnnmagnetic flux quanta, andη\etais the detection efficiency.

To identify the operating conditions under which fluctuations ofnVAPn_{\mathrm{VAP}}are suppressed, we evaluate the second-order correlation functiongVAP(2)g^{(2)}_{\mathrm{VAP}}, defined from the number of VAP events observed per pulse, as a function of bias current and base temperature,
as shown in Fig.7.

Figure7(a) shows the dependence ofgVAP(2)g^{(2)}_{\mathrm{VAP}}on the bias current atTb=T_{b}=97mK97\text{\,}\mathrm{m}\mathrm{K},
while Fig.7(b) shows its dependence on the base temperature
atIb=I_{b}=3µ​A3\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}.
We find thatgVAP(2)g^{(2)}_{\mathrm{VAP}}approaches unity
under specific combinations ofIbI_{b}andTbT_{b},
indicating that fluctuations in the number of VAP events per pulse are suppressed.
 Using these operating conditions, we examine the photon-number-resolving (PNR) behavior underTb=98​mKT_{\mathrm{b}}=98~\mathrm{mK}andIb=I_{\mathrm{b}}=3µ​A3\text{\,}\mathrm{\SIUnitSymbolMicro}\mathrm{A}, withμin=1​photon/pulse{\mu}_{\mathrm{in}}=1~\text{photon/pulse}.Figure 8:Photon-number-resolving behavior measured under operating conditions
identified in Fig. 7, wheregVAP(2)≈1g^{(2)}_{\mathrm{VAP}}\approx 1(atTb=97T_{\rm b}=97mK), indicating stabilized VAP generation.
(a) Distribution of the number of observed VAP events per pulse.
(b) Corresponding photon-number distribution inferred from the VAP counts.
Under these conditions, both distributions follow Poisson statistics.
The second-order correlation function evaluated from the photon-number
distribution,gphoton(2)≈1g^{(2)}_{\mathrm{photon}}\approx 1, is consistent with Poissonian photon statistics.
These results demonstrate that the Poissonian nature of the VAP statistics
(gVAP(2)≈1g^{(2)}_{\mathrm{VAP}}\approx 1) is directly transferred to the photon-number statistics, enabling photon-number-resolving behavior.

Under these conditions, we directly evaluate the statistical distributions of the detected events to verify the emergence of photon-number-resolving behavior.
The bars in Fig.8(a) show the distribution of the individual magnetic quantum peaks under these conditions. The total number of events isNall=105N_{\mathrm{all}}=10^{5}.
From this distribution, we obtainednVAPn_{\mathrm{VAP}}using Eq. (4), which yieldsnVAP=3.22​Φ0/photon.n_{\mathrm{VAP}}=3.22~\Phi_{0}/\text{photon}.

In addition to this method, we applied a multi-Gaussian fitting to the distribution to determinenVAPn_{\mathrm{VAP}}. The fitting function is expressed asf​(x)=Nall2​π​∑n=0Pphoton​(n)σn​exp⁡[−(x−bn)22​σn2],f(x)=\frac{N_{\mathrm{all}}}{\sqrt{2\pi}}\sum_{n=0}\frac{P_{\mathrm{photon}}(n)}{\sigma_{n}}\exp\left[-\frac{(x-b_{n})^{2}}{2\sigma_{n}^{2}}\right],(5)

whereNallN_{\mathrm{all}}is the total number of events,Pphoton​(n)P_{\mathrm{photon}}(n)is the probability of thenn-photon state,bnb_{n}is the center position of thennth peak, andσn\sigma_{n}is its standard deviation.
After fitting, we obtainednVAP=∑bn/∑n=3.18,n_{\mathrm{VAP}}=\sum b_{n}/\sum n=3.18,which agrees well with the value obtained by the previous method in Eq. (4).
The bars in Fig.8(b) show the probability of the photon-number statesPphoton​(n)P_{\mathrm{photon}}(n)determined by the fitting.
The dotted line represents the Poisson distribution under the same condition, with an average photon number ofη​μin=0.77\eta\mu_{\mathrm{in}}=0.77.
We conducted a chi-square test on the datasets, and the results revealed no significant differences among the conditions (χ2=3.41\chi^{2}=3.41,p=0.333p=0.333).

Moreover, the second-order correlation functiongphoton(2)g^{(2)}_{\mathrm{photon}}for photons was evaluated to begphoton(2)=0.972g^{(2)}_{\mathrm{photon}}=0.972, consistent with Poissonian photon statistics.
This result demonstrates that the Poissonian nature of the VAP statistics
(gVAP(2)≈1g^{(2)}_{\mathrm{VAP}}\approx 1) is directly transferred to the
photon-number statistics.It should be noted that these measurements are performed under specific
operating conditions identified through thegVAP(2)g^{(2)}_{\mathrm{VAP}}analysis,
in contrast to the general response shown in Fig.4,
where the VAP number fluctuates and does not directly reflect photon statistics.

To compare the experimentally obtained value with a simple energy-scale estimate, we introduce the kinetic-inductive energy scale associated with a2​π2\piphase-slip event,EΦ0=Φ022​Lk,{\color[rgb]{0,0,0}E_{\Phi_{0}}=\frac{\Phi_{0}^{2}}{2L_{\mathrm{k}}},}(6)

whereLkL_{\mathrm{k}}is the kinetic inductance of our device. Using the estimated kinetic inductance underTb=98T_{\mathrm{b}}=98mK,Ib=3​μI_{\mathrm{b}}=3~\muA, and an input wavelength of 1526 nm, we obtainEγ/EΦ0≈2.88E_{\gamma}/E_{\Phi_{0}}\approx 2.88, which is in reasonable agreement with the experimentally obtained value. We emphasize that this estimate is not a rigorous prediction of the number of VAPs; rather, it provides an order-of-magnitude consistency check, since the actual number of events is governed by nonequilibrium phase-slip dynamics under the given bias and thermal conditions.

The present work establishes the existence of a direct statistical link between absorbed-photon energy and vortex–antivortex generation.
Future studies of wavelength dependence and dynamic range will provide further insight into the energy-conversion process from photons to phase-slip events.

## IVConclusion

In summary, we experimentally demonstrated the direct observation of photon-induced VAP dynamics in superconducting films operated in a vortex-based detection mode.By analyzing the quantized voltage signals associated with phase-slip events,we confirmed that the observed responseassociated with phase-slip events (i.e., magnetic flux quanta traversing the superconducting strip)rather than the resistance changes in the transition region.
The voltage-time integrals exhibit clear quantization in units of the magnetic flux quantum, establishing a direct link between the signal amplitude and the number of VAPs. Furthermore, we identified that the measured response time is limited by the readout circuit bandwidth, suggesting that sub-nanosecond intrinsic timescales are achievable through circuit optimization.

Importantly, we demonstrated the PNR capability based on the correlation between the number of absorbed photons and number of traversing VAPs.
The reconstructed photon-number distribution agrees with the Poisson statistics, confirming the feasibility of multi-photon resolution in this detection scheme. These findings represent the first experimental evidence of VAP-mediated photon detection and provide a pathway toward fast, high-efficiency, multi-photon-resolving superconducting detectors.
Such detectors could play a crucial role in quantum optics and quantum information processing, where precise photon-number discrimination and ultra-fast response are essential.These results demonstrate that photon detection can be governed by phase-slip dynamics rather than conventional resistive transitions.


Acknowledgments-This work was supported in part by the BRIDGE program, Cross-ministerial SIP, JSPS KAKENHI Grant Number 24K01374, and JST Moonshot R&D Program Grant Number JPMJMS2064-6 and JPMJMS256I-4.
D. Fukuda contributed equally to this work. F. Hirayama, T. Tsuruta, and T. Kikuchi led the discussion and interpretation of the results.

## References
- [1]O. Dobrovolskiy, D. Y. Vodolazov, F. Porrati, R. Sachser, V. Bevz, M. Y. Mikhailov, A. Chumak, and M. Huth(2020)Ultra-fast vortex motion in a direct-write nb-c superconductor.Nature communications11(1),pp. 3291.Cited by:§III.2.
- [2]A. Engel, J. Renema, K. Il’in, and A. Semenov(2015)Detection mechanism of superconducting nanowire single-photon detectors.Superconductor Science and Technology28(11),pp. 114003.Cited by:§I.
- [3]G. Gol’Tsman, O. Okunev, G. Chulkova, A. Lipatov, A. Semenov, K. Smirnov, B. Voronov, A. Dzardanov, C. Williams, and R. Sobolewski(2001)Picosecond superconducting single-photon optical detector.Applied physics letters79(6),pp. 705–707.Cited by:§I.
- [4]K. Hattori, T. Konno, Y. Miura, S. Takasu, and D. Fukuda(2022)An optical transition-edge sensor with high energy resolution.Superconductor Science and Technology35(9),pp. 095002.Cited by:§II.1.
- [5]M. Hofherr, D. Rall, K. Ilin, M. Siegel, A. Semenov, H. Hübers, and N. Gippius(2010)Intrinsic detection efficiency of superconducting nanowire single-photon detectors with different thicknesses.Journal of Applied Physics108(1).Cited by:§I.
- [6]J. R. Hook and H. E. Hall(2013)Solid state physics.John Wiley & Sons.Cited by:§II.1.
- [7]K. D. Irwin and G. C. Hilton(2005)Transition-edge sensors.Cryogenic particle detection,pp. 63–150.Cited by:§I,§II.1.
- [8]F. Mattioli, Z. Zhou, A. Gaggero, R. Gaudio, S. Jahanmirinejad, D. Sahin, F. Marsili, R. Leoni, and A. Fiore(2015)Photon-number-resolving superconducting nanowire detectors.Superconductor Science and Technology28(10),pp. 104001.Cited by:§I.
- [9]C. M. Natarajan, M. G. Tanner, and R. H. Hadfield(2012)Superconducting nanowire single-photon detectors: physics and applications.Superconductor science and technology25(6),pp. 063001.Cited by:§I.
- [10]D. V. Reddy, R. R. Nerem, S. W. Nam, R. P. Mirin, and V. B. Verma(2020)Superconducting nanowire single-photon detectors with 98% system detection efficiency at 1550 nm.Optica7(12),pp. 1649–1653.Cited by:§I.
- [11]J. Renema, G. Frucci, Z. Zhou, F. Mattioli, A. Gaggero, R. Leoni, M. J. de Dood, A. Fiore, and M. P. van Exter(2013)Universal response curve for nanowire superconducting single-photon detectors.Physical Review B—Condensed Matter and Materials Physics87(17),pp. 174526.Cited by:§I.
- [12]A. D. Semenov, G. N. Gol’tsman, and A. A. Korneev(2001)Quantum detection by current carrying superconducting film.Physica C: Superconductivity351(4),pp. 349–356.Cited by:§I.
- [13]A. D. Semenov, P. Haas, H. Hübers, K. Ilin, M. Siegel, A. Kirste, T. Schurig, and A. Engel(2008)Vortex-based single-photon response in nanostructured superconducting detectors.Physica C: Superconductivity and its applications468(7-10),pp. 627–630.Cited by:§I.
- [14]A. Semenov, A. Engel, H. Hübers, K. Il’in, and M. Siegel(2005)Spectral cut-off in the efficiency of the resistive state formation caused by absorption of a single-photon in current-carrying superconducting nano-strips.The European Physical Journal B-Condensed Matter and Complex Systems47,pp. 495–501.Cited by:§I.
- [15]J. N. Ullom and D. A. Bennett(2015)Review of superconducting transition-edge sensors for x-ray and gamma-ray spectroscopy.Superconductor Science and Technology28(8),pp. 084003.Cited by:§I.
- [16]D. Y. Vodolazov(2014)Current dependence of the red boundary of superconducting single-photon detectors in the modified hot-spot model.Physical Review B90(5),pp. 054515.Cited by:§I.
- [17]A. Zotova and D. Y. Vodolazov(2012)Photon detection by current-carrying superconducting film: a time-dependent ginzburg-landau approach.Physical Review B—Condensed Matter and Materials Physics85(2),pp. 024509.Cited by:§I,§I.

## 


- 


Major funding support from
