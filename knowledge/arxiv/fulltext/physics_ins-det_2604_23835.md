# Squeezed state degradations due to mode mismatch and thermal aberrations in gravitational wave detectors

**arXiv ID**: 2604.23835v1
**Authors**: Kevin Kuns, Daniel Brown
**Published**: 2026-04-26
**Categories**: physics.ins-det, physics.optics, quant-ph
**Comments**: 35 pages, 10 figures
**HTML URL**: https://arxiv.org/html/2604.23835v1

## Abstract

To date, frequency-dependent squeezed light has been used to reduce quantum noise in interferometric gravitational wave detectors by 6.1 dB (a factor of two). Future upgrades and detectors aim to both reduce quantum noise by 10 dB (a factor of three) and to increase the circulating power in the interferometer arm cavities. Achieving these goals will be extremely challenging due, in part, to the degradations to the squeezed state caused by mode mismatch between the internal interferometer optical cavities and between the auxiliary external cavities. It is therefore imperative to gain a detailed understanding of all sources of mismatch and to obtain experience in mitigating their effects in the current detectors in order to improve astrophysical sensitivity now and in the future. Two types of internal mismatch are identified which are due to the thermal aberrations generated when the test mass optics absorb a small fraction of the circulating arm power. It is found that the dynamics responsible for the degradations caused by the mismatch between the quadratic part of the wavefront of two modes has a characteristic low-pass frequency dependence while the dynamics of the mismatch due to all higher order thermal aberrations has a high-pass behavior. As a consequence, the two types of mismatch are predominantly responsible for different squeezing degradations -- some of which are significant for the current detectors and some of which will only be important for future detectors with longer arms. The behavior of these two types of internal mismatch are described and the implications for detector design, operation, and characterization are discussed.

## Full Text

Squeezed state degradations due to mode mismatch and thermal aberrations in gravitational wave detectors

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
- 
- 
- 
- License: arXiv.org perpetual non-exclusive licensearXiv:2604.23835v1 [physics.ins-det] 26 Apr 2026

## Squeezed state degradations due to mode mismatch and thermal
aberrations in gravitational wave detectorsKevin KunsLIGO Laboratory, Department of Physics, Massachusetts Institute of
Technology, Cambridge, MA 02139, USADaniel BrownOzGrav, University of Adelaide, Adelaide, South Australia 5005, Australia(April 26, 2026)

## Abstract

To date, frequency-dependent squeezed light has been used to reduce
quantum noise in interferometric gravitational wave detectors by\qty6.1 (a factor of two). Future upgrades and detectors aim to
both reduce quantum noise by\qty10 (a factor of three) and to
increase the circulating power in the interferometer arm cavities.
Achieving these goals will be extremely challenging due, in part, to
the degradations to the squeezed state caused by mode mismatch between
the internal interferometer optical cavities and between the auxiliary
external cavities. It is therefore imperative to gain a detailed
understanding of all sources of mismatch and to obtain experience in
mitigating their effects in the current detectors in order to improve
astrophysical sensitivity now and in the future. Two types of internal
mismatch are identified which are due to the thermal aberrations
generated when the test mass optics absorb a small fraction of the
circulating arm power. It is found that the dynamics responsible for
the degradations caused by the mismatch between the quadratic part of
the wavefront of two modes has a characteristic low-pass frequency
dependence while the dynamics of the mismatch due to all higher order
thermal aberrations has a high-pass behavior. As a consequence, the
two types of mismatch are predominantly responsible for different
squeezing degradations—some of which are significant for the current
detectors and some of which will only be important for future
detectors with longer arms. The behavior of these two types of
internal mismatch are described and the implications for detector
design, operation, and characterization are discussed.

## IIntroduction

The LIGO-Virgo-KAGRA network of gravitational wave observatories have
detected over 200 compact binary coalescences to date[1]and
have opened the door to multimessenger astronomy by enabling the
simultaneous observation of both gravitational and electromagnetic
radiation[3]. These detectors are now limited by quantum
noise throughout large regions of the detection
band[18], and it is therefore necessary to understand
and reduce all sources of quantum noise in order to continue to
advance the astrophysics, cosmology, and fundamental physics enabled
by the observation of gravitational waves.

Gravitational wave detectors now make routine use of squeezed light to
reduce quantum
noise[9,55,5,31,37,26,39,58].
Most significantly, LIGO has achieved\qty6.1 of broadband
quantum noise reduction—simultaneously reducing radiation pressure
and shot noise—through the use of frequency-dependent squeezed
vacuum states[26,18].
These squeezed states are fragile and are susceptible to
several degradation mechanisms which include the effects of the
mismatch between the spatial modes of the numerous optical cavities which make
up these detectors. In particular, the arm cavities must be matched to
the signal extraction cavity used to tune the detector sensitivity.
The interferometer must then be matched to three external optical
cavities which together generate the squeezed light, provide the
frequency dependence needed for broadband quantum noise reduction, and
filter the signal exiting the interferometer before detection. In
addition to matching the interferometer to these three external
cavities, they must also all be matched to one another.

The mismatch between these external cavities has been studied in
detail theoretically[40,36], and these models
have been successfully compared with measurements of the current
detectors[40]. Several degradation mechanisms to the
squeezed states were identified in this analysis. Critically, it was
shown that these sources of mismatch make complex frequency-dependent
contributions to the squeezing degradations due, in part, to the
coherent nature in which the higher order modes (HOMs) excited by the
mismatch interfere with themselves and with the fundamental
mode. While Ref.[40]outlined how the effects of one
type of internal mode mismatch can be included in the analysis of
quantum noise, no in-depth study of internal mismatch has been done to
date as far as we are aware.

In this work we identify two types of internal mode mismatch which are
mainly caused by the absorption of a small fraction of the power
circulating in the interferometer cavities by the test mass optics.
This induces both a thermorefractive lens in the test mass substrates
and a thermoelastic deformation of the optic
surfaces[32,33,56]. These
aberrations degrade the signals needed to control the interferometers
and increase technical noise couplings. They are also the source of
several squeezing degradations that are the focus of this work. The
thermal aberrations can be decomposed into the mismatch between the
quadratic part of the wavefront of two optical modes and the mismatch
due to all higher order thermal aberrations. Due to the differences in
how the HOMs excited by these two types of mismatch interfere, the
HOMs generated by quadratic mismatch experience dynamics with a
low-pass frequency dependence while the HOMs generated by higher order
aberrations experience high-pass dynamics. As a consequence, each type
of mismatch is predominantly responsible for different
frequency-dependent squeezing degradations.

Efforts to quantitatively understand quantum noise in the current
detectors have met with some
success[40,18,34]. Generally, after the
known losses have been included in the accounting, the remaining
unknown loss is attributed to mode mismatch. In order to continue to
improve the detectors, it is important to understand this putative
mismatch in more detail, and to this end efforts are made to reconcile
various measurements with noise models.
The analysis of Refs.[18,34]included the effects
of internal quadratic mismatch as outlined in
Ref.[40]. Importantly, however, these studies did not
consider higher order aberrations and the potentially significant
frequency-dependent losses that they contribute due to their high-pass
dynamics. Attributing losses to external mismatch can incorrectly
account for the effects of internal mismatch up to a point, and this
can confuse efforts to characterize the detectors. Failing to properly
account for internal mismatch—especially the loss due to higher
order aberrations—will become increasingly insufficient as the arm
power is increased and thermal aberrations become more significant.

In practice, the thermal state of the interferometers drifts, which is
accompanied by changes both to the optical dynamics and to different
thermal aberrations generating different mode mismatch. This produces
numerous technical challenges and further complicates efforts to
characterize and improve the detectors. An understanding of the
effects of internal mode mismatch provides insight into the changing
behavior of the interferometers and can suggest measurements and
adjustments to make in order to diagnose and tune the state of the
detectors—both to decrease squeezing degradations and to improve
other technical difficulties.

Moving beyond the current detectors, an upgrade to the existing LIGO
facilities, known as LIGO A♯\sharp[46], and an upgrade to
the Virgo facility, known as Virgo_nEXT[53], are being
planned with the goals of achieving\qty10 of broadband
frequency-dependent quantum noise reduction and\qty1.5 of
circulating arm power—roughly a factor of four more than the highest
power achieved to date. At the same time, the next generation of
gravitational wave observatories are being designed. In the United
States, Cosmic Explorer (CE) would be a\qty40 long detector
with the same quantum noise reduction and arm power
targets[25]. In Europe, the Einstein Telescope (ET) would
include a\qty10 long interferometer with\qty3 arm
power and the same quantum noise reduction[24].
Achieving these ambitious goals will require significant advances in
the ability to characterize and understand the effects of mode
mismatch responsible for squeezing degradations and to control the
sources of the mismatch responsible for them. Furthermore, the success
of future detectors will benefit greatly from the simultaneous design,
from the start, of the optical layout and the thermal compensation
schemes informed by knowledge of these squeezing degradations and by
experience mitigating their effects in the current detectors.

The long arms of future detectors further introduce new challenges not
present in the current kilometer-scale detectors. Higher order modes
will become resonant in the arm cavities at frequencies
within the detection band. Internal mismatch—especially quadratic
mismatch—will then be responsible for significant squeezing
degradations at these frequencies where the HOMs that they excite
become resonant in the arms. Understanding the details of
these degradations is critical in designing the future detectors, but
such knowledge may also prove useful for characterizing and improving
the current detectors even though these degradations do not impact
their sensitivity.

In order to investigate these effects of internal mode mismatch, we
study a three mirror coupled cavity system which provides a good
description of a gravitational wave detector for many purposes. The
main numerical results of this paper, shown in all of the figures, are
thus obtained using a modal model of such a system, described inAppendixD, which includes the exact couplings generated by
thermal aberrations between many HOMs. The discussion in the main body
of the work, however, relies on a simpler phenomenological model which
includes a single HOM, along with simple approximations of limited
validity to this model, in order to better understand the exact
behavior. This is described inSectionsIIandC.SectionIIIdescribes the two types of thermal
aberrations and connects their characteristics to the phenomenological
parameters of this simpler model. The resulting squeezing degradations
are then discussed inSectionIV.

We stress that we are not attempting to quantitatively account for the
quantum noise present in the current detectors and are not making
projections about the sensitivity that a future detector or upgrade
can reach. The quantitative results depend sensitively on the details
of the thermal aberrations—our treatment of these is
simplistic—and while briefly discussed, we have not included the
effects of external mode mismatch in our detailed analysis. The goal
of this work is simply to identify two types of internal mismatch in a
gravitational wave detector and to explain the phenomenology of their
impact to the degradations to the squeezed states in order to inform
efforts to understand and improve the current detectors and to design
the future ones.

## IICoupled Cavity Dynamics

A significant part of understanding quantum noise is understanding how
quantum vacuum propagates throughout an optomechanical system. The
ultimate goal of this section is thus to obtain the transfer functions
necessary to calculate the squeezing degradations inSectionIVand to understand how the low-pass
dynamics of quadratic mismatch and the high-pass dynamics of higher
order aberrations arise.ITMETMSEMts​𝟏t_{\text{s}}\mathbf{1}𝐏s\mathbf{P}_{\text{s}}𝐋sa\mathbf{L}_{\text{sa}}ti​𝐒hst_{\text{i}}\mathbf{S}_{\text{hs}}𝐏a\mathbf{P}_{\text{a}}−re​𝟏-r_{\text{e}}\mathbf{1}𝐏a\mathbf{P}_{\text{a}}−ri​𝐒hh-r_{\text{i}}\mathbf{S}_{\text{hh}}ti​𝐒sht_{\text{i}}\mathbf{S}_{\text{sh}}ri​𝐒ssr_{\text{i}}\mathbf{S}_{\text{ss}}𝐋as\mathbf{L}_{\text{as}}𝐏s\mathbf{P}_{\text{s}}−rs​𝟏-r_{\text{s}}\mathbf{1}ts​𝟏t_{\text{s}}\mathbf{1}rs​𝟏r_{\text{s}}\mathbf{1}−qsub∗-q_{\text{sub}}^{*}−qar∗-q_{\text{ar}}^{*}−qhr∗-q_{\text{hr}}^{*}qarq_{\text{ar}}qsubq_{\text{sub}}qhrq_{\text{hr}}μa,i\mu_{\text{a,i}}μa,r\mu_{\text{a,r}}μas,i\mu_{\text{as,i}}μas,r\mu_{\text{as,r}}μx\mu_{x}μs,i\mu_{\text{s,i}}μs,r\mu_{\text{s,r}}Eas,iE_{\text{as,i}}01injected squeezedvacuumEas,rE_{\text{as,r}}01detected signalEsec,iE_{\text{sec,i}}01SEC lossvacuumεs​𝟏\sqrt{\varepsilon}_{\text{s}}\mathbf{1}signal extraction cavityarm cavitySubstrate thermal lensquadraticmismatch𝐋as=𝐋sa=𝟏𝐒sh=𝐒hs⊺≠𝟏higher orderaberrations𝐋as=𝐋sa≠𝟏𝐒sh=𝐒hs=𝟏\begin{array}[]{c@{\hspace{1em}}c}\lx@intercol\hfil\textbf{Substrate thermal lens}\hfil\lx@intercol\\
\vskip 4.0pt\cr\begin{array}[]{c}\textbf{quadratic}\\
\textbf{mismatch}\\
\vskip 1.0pt\cr\hline\cr\vskip 4.0pt\cr\begin{aligned} \mathbf{L}_{\text{as}}&=\mathbf{L}_{\text{sa}}=\mathbf{1}\\
\mathbf{S}_{\text{sh}}&=\mathbf{S}_{\text{hs}}^{\intercal}\neq\mathbf{1}\end{aligned}\end{array}\hfil\hskip 10.00002pt&\begin{array}[]{c}\textbf{higher order}\\
\textbf{aberrations}\\
\vskip 1.0pt\cr\hline\cr\vskip 4.0pt\cr\begin{aligned} \mathbf{L}_{\text{as}}&=\mathbf{L}_{\text{sa}}\neq\mathbf{1}\\
\mathbf{S}_{\text{sh}}&=\mathbf{S}_{\text{hs}}=\mathbf{1}\end{aligned}\end{array}\end{array}Figure 1:Coupled cavity equivalent to the differential arm motion
of a gravitational wave detector. The ellipses and circles
represent (potentially squeezed) quantum vacuum of the
electromagnetic field at several locations. The 0 modes
represent the fundamental vacuum and the 1 and subsequent modes
represent the HOM vacuum. Several nodes of the system are marked
with theμi\mu_{i}labels. The squeezed states are injected at the
nodeμas,i\mu_{\text{as,i}}after being reflected off of the filter
cavity (not shown but included in the analysis). The signal is
detected at the nodeμas,r\mu_{\text{as,r}}after passing through the
output mode cleaner which ensures that only the fundamental mode
is measured. The power absorbed in the test mass coatings
generates a thermorefractive lens in the ITM substrate, depicted
as a thin lens in the figure, and deforms the HR surfaces of the
ITM and ETM. The thermal aberrations can be decomposed into
quadratic mismatch and higher order aberrations as shown inFig.3. The Gaussianqqparameters at several
nodes important to the analysis ofSectionIIIare also shown. Reversed
parameters−q∗-q^{*}describe beams propagating in a coordinate
system with an inversion in the tangential direction. The box
summarizes the main result ofSectionIIIfor
thermal aberrations generated by a substrate thermal lens. The
operators𝐋i​j\mathbf{L}_{ij}describe how a field propagates through
the lens, i.e. the ITM substrate, and the𝐒i​j\mathbf{S}_{ij}describe how a field transmits through or reflects from the HR
surface. (While𝐋as=𝐋sa=𝟏\mathbf{L}_{\text{as}}=\mathbf{L}_{\text{sa}}=\mathbf{1}for the surface
deformations,𝐒sh\mathbf{S}_{\text{sh}}and𝐒hs\mathbf{S}_{\text{hs}}are not always𝟏\mathbf{1}for the
substrate lens since the lens can change the mode of the SEC and thus the
coupling between the fields on either side of the HR surface.)

Modern gravitational wave detectors employ the so-called dual-recycled
Fabry–Perot Michelson (DRFPMI) optical topology. In this
configuration, the arms of a Michelson interferometer are made into
two mirror Fabry–Perot cavities each made up of an end test mass (ETM)
and an input test mass (ITM) in order to increase the power stored in
the arm cavities and to increase the sensitivity to gravitational wave
signals. A signal extraction mirror (SEM) is placed between the
beamsplitter and the readout of the interferometer—thus forming an
optical cavity with the ITMs known as the signal extraction cavity
(SEC)—in order to tune the response of the detector to a
gravitational wave signal. The SEC can be operated in the resonant
sideband extraction (RSE) configuration which broadens the
bandwidth[44]or in the signal recycling configuration
(SR) which narrows the bandwidth[42]. To a good
approximation, the dynamics of the differential arm motion of a DRFPMI
can be described by a three mirror coupled cavity as illustrated inFig.1. A single ITM and ETM form an effective arm
cavity sensitive to differential arm motion, and the SEC is formed by
the addition of an SEM.

We review the dynamics of both RSE and SR with perfect mode matching
inSectionII.1before delving into the details of RSE
in the presence of mode mismatch inSectionII.2. We
will ultimately be interested only in RSE, the case relevant to
gravitational wave detectors, however the dynamics of the higher order
modes in an interferometer operating in the RSE configuration will
sometimes be those of the fundamental mode operating in the SR
configuration and it is therefore useful to have an understanding of
both.

As this work is primarily focused on the effects of mode mismatch, we
ignore optical loss in most of the discussion in order to simplify the
analytic expressions. However, all sources of loss listed inTable2are included in all of the numerical
results presented in the figures. Furthermore, the rational
approximations given to the exact expressions are valid in the limit
of large cavity finesses and for frequencies far below the free
spectral range (FSR). While some require corrections to account for
the relatively low SEC finesse of LIGO and the low FSR of CE, they
properly account for the gross dynamics of the fields and their
scalings with detector parameters in all cases.

## II.1Resonant sideband extraction and signal recycling with perfect mode matching

Figure1depicts an operator graph of a general
coupled cavity system with many higher order modes (HOMs) in the
presence of mode mismatch and thermal aberrations which will be
analyzed inSectionIII. In the simple case of a
single mode in a perfectly matched system considered here, the lens
and surface operators describing the aberrations are𝐋i​j=𝐒i​j→1\mathbf{L}_{ij}=\mathbf{S}_{ij}\to 1. If the arm cavity is detuned from resonance by a
frequencyδ​ωa\delta\omega_{\text{a}}and the SEC is detuned from resonance by
an angleϕs\phi_{\text{s}}, the one-way propagation of a field through the
arm cavity𝐏a\mathbf{P}_{\text{a}}and through the SEC𝐏s\mathbf{P}_{\text{s}}are𝐏a→e−i​(Ω−δ​ωa)​La/c,𝐏s→e−i​(Ω​Ls/c+ϕs)\mathbf{P}_{\text{a}}\to\mathrm{e}^{-\mathrm{i}(\Omega-\delta\omega_{\text{a}})L_{\text{a}}/c},\quad\mathbf{P}_{\text{s}}\to\mathrm{e}^{-\mathrm{i}(\Omega L_{\text{s}}/c+\phi_{\text{s}})}(1)

whereLaL_{\text{a}}andLsL_{\text{s}}are the lengths of the arm cavity and SEC,
respectively. The arm cavity detuning could be due to introducing an
offsetΔ​La\Delta L_{\text{a}}in the length of the cavity so thatδ​ωa=−c​k​Δ​La/La\delta\omega_{\text{a}}=-ck\Delta L_{\text{a}}/L_{\text{a}}for the fundamental
mode. If the field is a higher order mode, the detuning could be due
to the additional one-way Gouy phaseψa\psi_{\text{a}}that the HOM
accumulates relative to the fundamental which may itself be on
resonance withΔ​La=0\Delta L_{\text{a}}=0. In this caseδ​ωa=ωfsr​ψa/π\delta\omega_{\text{a}}=\omega_{\text{fsr}}\psi_{\text{a}}/\piwhereωfsr=π​c/La\omega_{\text{fsr}}=\pi c/L_{\text{a}}is the free spectral range (FSR).

Consider first the dynamics of the arm alone, unmodified by the SEC,
without the presence of the SEM. A field in the cavity experiences a
round-trip gain ofri​re​e−2​i​(Ω−δ​ωa)​La/cr_{\text{i}}r_{\text{e}}\mathrm{e}^{-2\mathrm{i}(\Omega-\delta\omega_{\text{a}})L_{\text{a}}/c}. When
this open-loop gain is positive, the cavity enhances the dynamics of a
field in the cavity; when it is negative, the dynamics are
suppressed. These dynamics are described by the arm cavity loop
suppressionHa​(Ω)=[1−ri​re​e−2​i​(Ω−δ​ωa)​La/c]−1H_{\text{a}}(\Omega)=[1-r_{\text{i}}r_{\text{e}}\mathrm{e}^{-2\mathrm{i}(\Omega-\delta\omega_{\text{a}})L_{\text{a}}/c}]^{-1}.

We will be chiefly interested in two quantities. The first is the
reflection of a field off of the cavity𝔯a​(Ω)=Ea,rEa,i=ri−ti2​re​e−2​i​(Ω−δ​ωa)​La/c1−ri​re​e−2​i​(Ω−δ​ωa)​La/c\mathfrak{r}_{\text{a}}(\Omega)=\frac{E_{\text{a,r}}}{E_{\text{a,i}}}=r_{\text{i}}-\frac{t_{\text{i}}^{2}r_{\text{e}}\mathrm{e}^{-2\mathrm{i}(\Omega-\delta\omega_{\text{a}})L_{\text{a}}/c}}{1-r_{\text{i}}r_{\text{e}}\mathrm{e}^{-2\mathrm{i}(\Omega-\delta\omega_{\text{a}})L_{\text{a}}/c}}(2)

which is made by the interference between the field which is promptly
reflected from the ITM and the field which enters the cavity,
experiences its closed loop dynamics, and then leaks back out. The
second is the transmission of a signal through the cavity𝔱a​(Ω)=Ea,rEx=ti​e−i​(Ω−δ​ωa)​La/c1−ri​re​e−2​i​(Ω−δ​ωa)​La/c\\
\mathfrak{t}_{\text{a}}(\Omega)=\frac{E_{\text{a,r}}}{E_{x}}=\frac{t_{\text{i}}\mathrm{e}^{-\mathrm{i}(\Omega-\delta\omega_{\text{a}})L_{\text{a}}/c}}{1-r_{\text{i}}r_{\text{e}}\mathrm{e}^{-2\mathrm{i}(\Omega-\delta\omega_{\text{a}})L_{\text{a}}/c}}(3)

whereExE_{x}is the field reflecting off of the ETM surface at the nodeμx\mu_{x}inFig.1.

Gravitational wave detectors employ so-called high finesse overcoupled
cavities where the ITM is highly reflective yet still less
reflective than the ETM:1≫ti>te≈01\gg t_{\text{i}}>t_{\text{e}}\approx 0. For such an overcoupled cavity,Eqs.3and2can
be written in a zero, pole, gain form as𝔯a​(Ω)\displaystyle\mathfrak{r}_{\text{a}}(\Omega)=−1−i​(Ω−δ​ωa)/γa1+i​(Ω−δ​ωa)/γa\displaystyle=-\frac{1-\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{a}}}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{a}}}(4)𝔱a​(Ω)\displaystyle\mathfrak{t}_{\text{a}}(\Omega)=2​ℱaπ​11+i​(Ω−δ​ωa)/γa\displaystyle=\sqrt{\frac{2\mathcal{F}_{\text{a}}}{\pi}}\frac{1}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{a}}}(5)

where the half-bandwidth of the armγa\gamma_{\text{a}}, also known as the arm
cavity pole, and arm cavity finesse are defined asℱa\displaystyle\mathcal{F}_{\text{a}}=π1−ri,γa=cLa​1−ri1+ri=π​c2​ℱa​La\displaystyle=\frac{\pi}{1-r_{\text{i}}},\quad\gamma_{\text{a}}=\frac{c}{L_{\text{a}}}\frac{1-r_{\text{i}}}{1+r_{\text{i}}}=\frac{\pi c}{2\mathcal{F}_{\text{a}}L_{\text{a}}}(6a)ℱs\displaystyle\mathcal{F}_{\text{s}}=π1−rs,γs=cLs​1−rs1+rs=π​c2​ℱs​Ls\displaystyle=\frac{\pi}{1-r_{\text{s}}},\quad\gamma_{\text{s}}=\frac{c}{L_{\text{s}}}\frac{1-r_{\text{s}}}{1+r_{\text{s}}}=\frac{\pi c}{2\mathcal{F}_{\text{s}}L_{\text{s}}}(6b)

For future use, we have also defined the SEC finesseℱs\mathcal{F}_{\text{s}}and SEC
poleγs\gamma_{\text{s}}. Of particular note, the cavity imparts aπ\piphase
shift on reflection for fields resonant in the cavity:𝔯a​(|Ω−δ​ωa|≪γa)=−1\mathfrak{r}_{\text{a}}(|\Omega-\delta\omega_{\text{a}}|\ll\gamma_{\text{a}})=-1, rather than+ri+r_{\text{i}}; and imparts
no phase shift for fields far from resonance:𝔯a​(|Ω−δ​ωa|≫γa)=+1\mathfrak{r}_{\text{a}}(|\Omega-\delta\omega_{\text{a}}|\gg\gamma_{\text{a}})=+1. This sign change around the cavity
pole has important implications for the coupled cavity
dynamics.111It is sometimes said that a non-resonant field does
not “see the cavity,” but this is misleading as the field still
enters the cavity and the ensuing dynamics, while being suppressed by
the arm loop rather than being enhanced by it, still interferes with
and modifies the prompt reflection. In addition to changing the
magnitude of the reflection—even more so thanEq.4suggests in the presence of optical
loss—it also imparts a small phase shift for a field which is not
exactly anti-resonant, i.e.Ω−δ​ωa≠N​ωfsr\Omega-\delta\omega_{\text{a}}\neq N\omega_{\text{fsr}}for integerNN.

Next consider how the SEC, formed by the addition of the SEM, modifies
the dynamics of the arm cavity. If the SEC is tuned so that the
fundamental accumulates a one-way phase shiftϕs\phi_{\text{s}}in the
cavity, then the reflection of a field off of the coupled cavity is
again made by the interference of the field which is promptly
reflected from the SEM and the field that enters the coupled cavity:𝔯cc​(Ω)=Eas,rEas,i=rs+ts2​𝔯a​(Ω)​e−2​i​(Ω​Ls/c+ϕs)1+rs​𝔯a​(Ω)​e−2​i​(Ω​Ls/c+ϕs),\mathfrak{r}_{\text{cc}}(\Omega)=\frac{E_{\text{as,r}}}{E_{\text{as,i}}}=r_{\text{s}}+\frac{t_{\text{s}}^{2}\mathfrak{r}_{\text{a}}(\Omega)\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c+\phi_{\text{s}})}}{1+r_{\text{s}}\mathfrak{r}_{\text{a}}(\Omega)\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c+\phi_{\text{s}})}},(7)

and the transmission through the coupled cavity is𝔱cc​(Ω)=Eas,rEx=ts​𝔱a​(Ω)​e−i​(Ω​Ls/c+ϕs)1+rs​𝔯a​(Ω)​e−2​i​(Ω​Ls/c+ϕs).\mathfrak{t}_{\text{cc}}(\Omega)=\frac{E_{\text{as,r}}}{E_{x}}=\frac{t_{\text{s}}\mathfrak{t}_{\text{a}}(\Omega)\mathrm{e}^{-\mathrm{i}(\Omega L_{\text{s}}/c+\phi_{\text{s}})}}{1+r_{\text{s}}\mathfrak{r}_{\text{a}}(\Omega)\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c+\phi_{\text{s}})}}.(8)

This is exactly like the single arm cavity with the arm cavity itself
serving as a compound mirror and taking the place of the ETM and with
the SEM taking the place of the ITM.

We will only consider in detail the extreme cases of signal recycling
(SR)[42], whereϕs=0\phi_{\text{s}}=0, and resonant sideband
extraction (RSE)[44], whereϕs=π/2\phi_{\text{s}}=\pi/2. In these
two cases, the SEC loop suppression, evident inEqs.7and8, isHs​(Ω)\displaystyle H_{\text{s}}(\Omega)=11+rs​𝔯a​(Ω)​e−2​i​(Ω​Ls/c+ϕs)\displaystyle=\frac{1}{1+r_{\text{s}}\mathfrak{r}_{\text{a}}(\Omega)\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c+\phi_{\text{s}})}}=11±rs​1+i​(Ω−δ​ωa)/γa1+i​(Ω−δ​ωa)/γcc\displaystyle=\frac{1}{1\pm r_{\text{s}}}\frac{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{a}}}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{cc}}}(9)

where the coupled cavity pole isγcc=1±rs1∓rs​γa={γrse=2​ℱsπ​γaϕs=π/2γsr=π2​ℱs​γaϕs=0\gamma_{\text{cc}}=\frac{1\pm r_{\text{s}}}{1\mp r_{\text{s}}}\gamma_{\text{a}}=\begin{cases}\displaystyle\gamma_{\text{rse}}=\frac{2\mathcal{F}_{\text{s}}}{\pi}\gamma_{\text{a}}&\phi_{\text{s}}=\pi/2\\[10.00002pt]
\displaystyle\gamma_{\text{sr}}=\frac{\pi}{2\mathcal{F}_{\text{s}}}\gamma_{\text{a}}&\phi_{\text{s}}=0\end{cases}(10)

and where the upper sign is taken for RSE and the lower for SR. With
RSE, the field picks up a round-trip propagation phase ofπ\pi. Since
the arm cavity reflection is negative for frequencies|Ω−δ​ωa|≪γa|\Omega-\delta\omega_{\text{a}}|\ll\gamma_{\text{a}}within the arm cavity bandwidth, and since the HR surface of the SEM
is inside the cavity, the total round-trip phase is negative and the
SEC suppresses the dynamics by a factor of 2 within the arm cavity
bandwidth. Outside the arm cavity bandwidth, the reflection changes
sign, the round-trip phase is positive, and the SEC enhances the
dynamics by a factor ofℱs/π\mathcal{F}_{\text{s}}/\pifor frequencies|Ω−δ​ωa|≫γrse|\Omega-\delta\omega_{\text{a}}|\gg\gamma_{\text{rse}}outside the RSE bandwidth. With SR, on the other hand, these phasings
differ byπ\pisince a field in the cavity does not accumulate any
propagation phase at low frequencies. Therefore for SR, the SEC
enhances the dynamics by a factor ofℱs/π\mathcal{F}_{\text{s}}/\pifor frequencies|Ω−δ​ωa|≪γsr|\Omega-\delta\omega_{\text{a}}|\ll\gamma_{\text{sr}}within the SR bandwidth and suppresses them by a
factor of 2 outside the arm cavity bandwidth.

The reflection from the coupled cavity can then be written in a zero,
pole, gain form as𝔯cc​(Ω)={𝔯rse=1−i​(Ω−δ​ωa)/γrse1+i​(Ω−δ​ωa)/γrse𝔯sr=−1−i​(Ω−δ​ωa)/γsr1+i​(Ω−δ​ωa)/γsr,\mathfrak{r}_{\text{cc}}(\Omega)=\begin{cases}\displaystyle\mathfrak{r}_{\text{rse}}=\frac{1-\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{rse}}}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{rse}}}\\[10.00002pt]
\mathfrak{r}_{\text{sr}}=-\displaystyle\frac{1-\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{sr}}}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{sr}}}\end{cases},(11)

and the transmission through the coupled cavity can be written as𝔱cc​(Ω)={𝔱rse=−ℱaℱs​i1+i​(Ω−δ​ωa)/γrse𝔱sr=4​ℱa​ℱsπ2​11+i​(Ω−δ​ωa)/γsr.\mathfrak{t}_{\text{cc}}(\Omega)=\begin{cases}\displaystyle\mathfrak{t}_{\text{rse}}=-\sqrt{\frac{\mathcal{F}_{\text{a}}}{\mathcal{F}_{\text{s}}}}\frac{\mathrm{i}}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{rse}}}\\[10.00002pt]
\displaystyle\mathfrak{t}_{\text{sr}}=\sqrt{\frac{4\mathcal{F}_{\text{a}}\mathcal{F}_{\text{s}}}{\pi^{2}}}\frac{1}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{sr}}}\end{cases}.(12)

The coupled cavity therefore behaves like the simple arm cavity with three differences.
First, the bandwidth of the coupled cavity is broadened with RSE and narrowed with SR by
a factor of2​ℱs/π2\mathcal{F}_{\text{s}}/\pi(Eq.10). Second, the DC gain of the cavity is
decreased with RSE and increased with SR by a factor of2​ℱs/π\sqrt{2\mathcal{F}_{\text{s}}/\pi}(Eqs.5and12). And third, the RSE reflection
phase differs by that of the arm reflection by a factor ofπ\pi, and the RSE
transmission is rotated byπ/2\pi/2relative to the arm transmission.tst_{\text{s}}−rs-r_{\text{s}}tst_{\text{s}}rsr_{\text{s}}e−i​(Ω​Ls/c+ϕs)\mathrm{e}^{-\mathrm{i}(\Omega L_{\text{s}}/c+\phi_{\text{s}})}1−Υ\sqrt{1-\Upsilon}𝔯a​0​(Ω)\mathfrak{r}_{\text{a}0}(\Omega)(fund. arm)1−Υ\sqrt{1-\Upsilon}e−i​(Ω​Ls/c+ϕs)\mathrm{e}^{-\mathrm{i}(\Omega L_{\text{s}}/c+\phi_{\text{s}})}fundamental SECtst_{\text{s}}−rs-r_{\text{s}}tst_{\text{s}}rsr_{\text{s}}e−i​(Ω​Ls/c+ϕs−ψs)\mathrm{e}^{-\mathrm{i}(\Omega L_{\text{s}}/c+\phi_{\text{s}}-\psi_{\text{s}})}1−Υ\sqrt{1-\Upsilon}𝔯a​1​(Ω)\mathfrak{r}_{\text{a}1}(\Omega)(HOM arm)1−Υ\sqrt{1-\Upsilon}e−i​(Ω​Ls/c+ϕs−ψs)\mathrm{e}^{-\mathrm{i}(\Omega L_{\text{s}}/c+\phi_{\text{s}}-\psi_{\text{s}})}HOM SECΥ\sqrt{\Upsilon}−Υ-\sqrt{\Upsilon}α​Υ\alpha\sqrt{\Upsilon}−α​Υ-\alpha\sqrt{\Upsilon}μas,i0\mu_{\text{as,i}}^{0}μas,r0\mu_{\text{as,r}}^{0}μas,i1\mu_{\text{as,i}}^{1}μas,r1\mu_{\text{as,r}}^{1}μa,r0\mu_{\text{a,r}}^{0}μa,i0\mu_{\text{a,i}}^{0}μa,r1\mu_{\text{a,r}}^{1}μa,i1\mu_{\text{a,i}}^{1}Eas,i0E_{\text{as,i}}^{0}injected fundamentalsqueezed vacuumEas,r0E_{\text{as,r}}^{0}detected fundamentalsignalEas,i1E_{\text{as,i}}^{1}“injected” HOMunsqueezed vaccumEas,r1E_{\text{as,r}}^{1}rejected HOM“signal”εs\sqrt{\varepsilon_{\text{s}}}Esec,i0E_{\text{sec,i}}^{0}SEC lossvacuumquadraticmismatchα=−1𝐔r=𝐔i−1𝐔i=𝐒hs𝐔r=𝐒shhigher orderaberrationsα=+1𝐔r=𝐔i𝐔i=𝐋sa𝐔r=𝐋as\begin{array}[]{c@{\hspace{1em}}c}\begin{array}[]{c}\textbf{quadratic}\\
\textbf{mismatch}\\
\vskip 1.0pt\cr\hline\cr\vskip 4.0pt\cr\begin{aligned} &\alpha=-1\quad&\mathbf{U}_{\text{r}}&=\mathbf{U}_{\text{i}}^{-1}\\
&\mathbf{U}_{\text{i}}=\mathbf{S}_{\text{hs}}\quad&\mathbf{U}_{\text{r}}&=\mathbf{S}_{\text{sh}}\end{aligned}\end{array}\hfil\hskip 10.00002pt&\begin{array}[]{c}\textbf{higher order}\\
\textbf{aberrations}\\
\vskip 1.0pt\cr\hline\cr\vskip 4.0pt\cr\begin{aligned} &\alpha=+1\quad&\mathbf{U}_{\text{r}}&=\mathbf{U}_{\text{i}}\\
&\mathbf{U}_{\text{i}}=\mathbf{L}_{\text{sa}}\quad&\mathbf{U}_{\text{r}}&=\mathbf{L}_{\text{as}}\end{aligned}\end{array}\end{array}Figure 2:Coupled cavity signal flow diagram for the model of the
fundamental and a single HOM described inSectionII.2. This system can be thought of as
two separate coupled cavities which are coupled by the mismatch
between the SEC and arm cavity at the ITM. As explained byEq.24, the HOM SEC is AC coupled
with the fundamental SEC through higher order aberrations while
being DC coupled through quadratic mismatch. The vacuum and
important nodes fromFig.1are reproduced
here with the superscripts 0 and 1 to indicate the fundamental
and HOM, respectively. Rather than drawing the arm cavities in
full, the fundamental arm cavity𝔯a​0​(Ω)\mathfrak{r}_{\text{a}0}(\Omega)is given
byEq.4withδ​ωa=0\delta\omega_{\text{a}}=0and
the HOM arm cavity𝔯a​1​(Ω)\mathfrak{r}_{\text{a}1}(\Omega)is given byEq.4withδ​ωa=ωfsr​ψa/π\delta\omega_{\text{a}}=\omega_{\text{fsr}}\,\psi_{\text{a}}/\pi. The one-way Gouy phases of
the arm cavity and the SEC areψa\psi_{\text{a}}andψs\psi_{\text{s}},
respectively, and the SEC detuningϕs\phi_{\text{s}}isπ/2\pi/2for
RSE. The fieldEas,i1E_{\text{as,i}}^{1}is the HOM of the fundamental
squeezed fieldEas,i0E_{\text{as,i}}^{0}which is injected into the
interferometer. The fieldEas,r0E_{\text{as,r}}^{0}is the fundamental
field which is detected;Eas,r1E_{\text{as,r}}^{1}is its HOM which is
rejected by the output mode cleaner. Note that only a single
mode propagates along the edges here while the full vector of
HOMs propagate along the edges shown inFig.1. The box summarizes how this model is
related to the operators describing the exact dynamics shown inFig.1.

Equation12describes the propagation of a field
leaving the ETM (Ex​(Ω)E_{x}(\Omega)) to a field measured in reflection of
the coupled cavity (Eas,r​(Ω)E_{\text{as,r}}(\Omega)). In the context of
gravitational wave detectors, we will be interested in the
transduction of ETM motion to the fundamental mode of the same
optical field measured in reflection of the coupled cavity. The
modulation of the position of a mirrorx​(Ω)x(\Omega)produces a
modulationEx​(Ω)=2​k​x​(Ω)​PaE_{x}(\Omega)=2k\,x(\Omega)\sqrt{P_{\text{a}}}in the phase of
an electromagnetic field of powerPaP_{\text{a}}reflected from that
mirror. These fluctuations will then be rotated into the amplitude
quadrature due to the extraπ/2\pi/2rotation for RSE, and so the
amplitude quadrature (with respect to the light generating the phase
signal) is generally measured. Furthermore, in the main text we will
ultimately only be interested in the case whereδ​ωa=0\delta\omega_{\text{a}}=0for the fundamental so that𝔱rse​(+Ω)=−𝔱rse∗​(−Ω)\mathfrak{t}_{\text{rse}}(+\Omega)=-\mathfrak{t}_{\text{rse}}^{*}(-\Omega)and so this quantity, known as the
optomechanical plant, is given byC​(Ω)=12×Ex​(Ω)x​(Ω)=12×2​k​Pa​𝔱rse​(Ω).C(\Omega)=\frac{1}{\sqrt{2}}\times\frac{E_{x}(\Omega)}{x(\Omega)}=\frac{1}{\sqrt{2}}\times 2k\sqrt{P_{\text{a}}}\,\mathfrak{t}_{\text{rse}}(\Omega).(13)

The extra factor of1/21/\sqrt{2}accounts for the presence of the
beamsplitter when mapping the dynamics of the coupled cavity onto
those of an interferometric gravitational wave detector.

Finally, we will occasionally be interested in the
radiation-pressure-mediated-correlation of the upper and lower
sidebands which is responsible for quantum radiation pressure noise
and ponderomotive squeezing. This is best analyzed in the two-photon
formalism[20], but for our purposes it is enough to note
that an amplitude quadrature fluctuation of a field incident on a
mirror is converted into a phase quadrature fluctuation of the field
on reflection of that mirror through the radiation pressure forceFrp​(Ω)F_{\text{rp}}(\Omega)of the laser light acting on the mirror. This
force produces a motionx​(Ω)=χ​(Ω)​Frp​(Ω)x(\Omega)=\chi(\Omega)F_{\text{rp}}(\Omega)of the mirror whereχ​(Ω)\chi(\Omega)is the mechanical susceptibility,
or mechanical plant. For a field of powerPaP_{\text{a}}incident on a
perfectly reflecting free mass mirror with susceptibilityχ​(Ω)=−1/M​Ω2\chi(\Omega)=-1/M\Omega^{2}, this optomechanical coupling
is[22]𝒦fm​(Ω)\displaystyle\mathcal{K}_{\text{fm}}(\Omega)=8​k​χ​(Ω)​Pac=−8​k​Pac​M​Ω2=−(ΩsqlfmΩ)2\displaystyle=\frac{8k\chi(\Omega)P_{\text{a}}}{c}=-\frac{8kP_{\text{a}}}{cM\Omega^{2}}=-\left(\frac{\Omega_{\text{sql}}^{\text{fm}}}{\Omega}\right)^{2}(14a)(Ωsqlfm)2\displaystyle\left(\Omega_{\text{sql}}^{\text{fm}}\right)^{2}=8​k​PaM​c\displaystyle=\frac{8kP_{\text{a}}}{Mc}(14b)

whereMMis the mass of the mirror and whereΩsqlfm\Omega_{\text{sql}}^{\text{fm}}is
known as the standard quantum limit (SQL) frequency for a free mass.
In a coupled cavity with two identical mirrors, this coupling is
modifed as222As in Ref.[40]and unlike in many
other references, we keep the optomechanical coupling complex so that
it describes all of the optical dynamics.𝒦cc​(Ω)=𝔱cc2​(Ω)×2​𝒦fm​(Ω)=−(ΩsqlccΩ)2​1(1+i​Ω/γcc)2\mathcal{K}_{\text{cc}}(\Omega)=\mathfrak{t}^{2}_{\text{cc}}(\Omega)\!\times\!2\mathcal{K}_{\text{fm}}(\Omega)=-\left(\frac{\Omega_{\text{sql}}^{\text{cc}}}{\Omega}\right)^{2}\frac{1}{(1+\mathrm{i}\Omega/\gamma_{\text{cc}})^{2}}(15)

where the extra factor of two accounts for the fact that there are two
mirrors in the arm cavity. One factor of𝔱cc\mathfrak{t}_{\text{cc}}accounts for
amplitude fluctuations entering the back of the SEM propagating to the
arms, and the second factor for the phase fluctuations propagating
back to the SEM. The coupled cavity SQL frequency is(Ωsqlcc)2\displaystyle\left(\Omega_{\text{sql}}^{\text{cc}}\right)^{2}=|𝔱cc​(0)|2×2​(Ωsqlfm)2\displaystyle=\left|\mathfrak{t}_{\text{cc}}(0)\right|^{2}\!\times\!2\left(\Omega_{\text{sql}}^{\text{fm}}\right)^{2}={(Ωsqlrse)2=ℱaℱs​16​k​PaM​c(Ωsqlsr)2=4​ℱa​ℱsπ2​16​k​PaM​c\displaystyle=\begin{cases}\displaystyle\left(\Omega_{\text{sql}}^{\text{rse}}\right)^{2}=\frac{\mathcal{F}_{\text{a}}}{\mathcal{F}_{\text{s}}}\frac{16kP_{\text{a}}}{Mc}\\[10.00002pt]
\displaystyle\left(\Omega_{\text{sql}}^{\text{sr}}\right)^{2}=\frac{4\mathcal{F}_{\text{a}}\mathcal{F}_{\text{s}}}{\pi^{2}}\frac{16kP_{\text{a}}}{Mc}\end{cases}(16)

The coupled cavity thus modifies the optomechanical coupling by adding
two poles to the response and by effectively changing the arm power by
a factor ofℱa/ℱs\mathcal{F}_{\text{a}}/\mathcal{F}_{\text{s}}for RSE and4​ℱa​ℱs/π24\mathcal{F}_{\text{a}}\mathcal{F}_{\text{s}}/\pi^{2}for SR.

## II.2Resonant sideband extraction in the presence of mode mismatch

For the remainder of the paper we focus on the case where the coupled cavity is operated
in the RSE configuration for the fundamental mode (ϕs=π/2\phi_{\text{s}}=\pi/2) but where there is a
mismatch between the mode of the arm cavity and the mode of the SEC. For small
mismatch, these dynamics can be described to a good approximation by a phenomenological
model similar to that of Ref.[40]tailored to studying internal mismatch
where the fundamental mode mixes with a single higher order mode at the interface
between the arm cavity and the SEC. We will see that it is useful to think of this
system as two separate coupled cavities—one for the fundamental operating in RSE and
one for the HOM with an arbitrary SEC detuning—with the coupling between the two
occurring at this interface. This picture is illustrated inFig.2.
Since we focus on internal mismatch, we imagine that the active wavefront control keeps
the external cavities perfectly matched to the SEC mode as the internal mismatch
changes; seeSectionIV.4for a brief discussion of the general case.

Mathematically, this is described by2×22\times 2matrices transforming
a vector representing the amplitudes of the fundamental and higher
order mode. The dynamics are the same as those described inSectionII.1except that the modes incident on the arm
cavity mix with the matrix𝐔i\mathbf{U}_{\text{i}}before encountering the dynamics of
the arm cavity described above, and then mix with the matrix𝐔r\mathbf{U}_{\text{r}}on
reflection of the arm cavity before reentering the SEC. Referring to
the nodes inFig.2, the matrix describing the
reflection of both fields off of the mismatched arm cavity is thus𝐑a\displaystyle\mathbf{R}_{\text{a}}=[Ea,r0/Ea,i0Ea,r0/Ea,i1Ea,r1/Ea,i0Ea,r1/Ea,i1]≡[𝔯00​(Ω)𝔱01​(Ω)𝔱10​(Ω)𝔯11​(Ω)]\displaystyle=\begin{bmatrix}E_{\text{a,r}}^{0}/E_{\text{a,i}}^{0}&E_{\text{a,r}}^{0}/E_{\text{a,i}}^{1}\\
E_{\text{a,r}}^{1}/E_{\text{a,i}}^{0}&E_{\text{a,r}}^{1}/E_{\text{a,i}}^{1}\end{bmatrix}\equiv\begin{bmatrix}\mathfrak{r}_{00}(\Omega)&\mathfrak{t}_{01}(\Omega)\\
\mathfrak{t}_{10}(\Omega)&\mathfrak{r}_{11}(\Omega)\end{bmatrix}=𝐔r​[𝔯a​0​(Ω)00𝔯a​1​(Ω)]​𝐔i,\displaystyle=\mathbf{U}_{\text{r}}\begin{bmatrix}\mathfrak{r}_{\text{a}0}(\Omega)&0\\
0&\mathfrak{r}_{\text{a}1}(\Omega)\end{bmatrix}\mathbf{U}_{\text{i}},(17)

where𝔯a​0​(Ω)\mathfrak{r}_{\text{a}0}(\Omega)is the arm reflection for the fundamental
in the absence of any mismatch (Eq.4withδ​ωa=0\delta\omega_{\text{a}}=0) and𝔯a​1​(Ω)\mathfrak{r}_{\text{a}1}(\Omega)is the arm
reflection for the HOM in the absence of any mismatch
(Eq.4withδ​ωa=ωfsr​ψa/π\delta\omega_{\text{a}}=\omega_{\text{fsr}}\,\psi_{\text{a}}/\pi). These mismatch
matrices are given by𝐔i=[1−Υ−ΥΥ1−Υ],𝐔r=[1−Υ−α​Υα​Υ1−Υ]\mathbf{U}_{\text{i}}=\begin{bmatrix}\sqrt{1-\Upsilon}&-\sqrt{\Upsilon}\\
\sqrt{\Upsilon}&\sqrt{1-\Upsilon}\end{bmatrix},\quad\mathbf{U}_{\text{r}}=\begin{bmatrix}\sqrt{1-\Upsilon}&-\alpha\sqrt{\Upsilon}\\
\alpha\sqrt{\Upsilon}&\sqrt{1-\Upsilon}\end{bmatrix}(18)

whereα=±1\alpha=\pm 1.333More generally,𝐔i\mathbf{U}_{\text{i}}and𝐔r\mathbf{U}_{\text{r}}could be
arbitrary unitary matrices with a complex phase describing the phasing
of the mismatch between the two cavities.
However, we only discuss the mismatch between the arms and the SEC in
this work and this possibility results in different dynamics only if
there are multiple sources of mismatch. This is accounted for by the
model ofAppendixC. Importantly, while𝐔i\mathbf{U}_{\text{i}}and𝐔r\mathbf{U}_{\text{r}}can be unitary in general,𝐔r=𝐔i†\mathbf{U}_{\text{r}}=\mathbf{U}_{\text{i}}^{\dagger}only for quadratic
mismatch and the restriction toα=±1\alpha=\pm 1is a convenient way of
expressing the defining relationship ofEq.19.As will be shown inSectionIII, the exact arm
reflection given byEq.32is equivalent toEqs.17and18for small
mismatch, and these two possibilities forα\alphacorrespond to the
two types of thermal aberrations which can occur inside a coupled
cavity:𝐔r={𝐔i−1,α=−1​(quadratic mismatch)𝐔i,α=+1​(higher order aberrations)\mathbf{U}_{\text{r}}=\begin{cases}\mathbf{U}_{\text{i}}^{-1},&\alpha=-1\penalty 10000\ (\text{quadratic mismatch})\\
\mathbf{U}_{\text{i}},&\alpha=+1\penalty 10000\ (\text{higher order aberrations})\end{cases}(19)

Whether𝐔r\mathbf{U}_{\text{r}}is the same as𝐔i\mathbf{U}_{\text{i}}or is its
inverse is the fundamental difference between the two types of
mismatch from which all of the differences in their dynamics
follow.The origin of this difference is explained byEq.35and the surrounding discussion.

In order to understand the squeezing degradations inSectionIV, it is necessary to understand how
fundamental and HOM fields couple into the fundamental mode of the
SEC, i.e. how they enter the fundamental SEC ofFig.2at the locationμa,r0\mu_{\text{a,r}}^{0}. It is
therefore instructive to analyze the reflection of fields in the SEC
incident on the arm (those atμa,i0\mu_{\text{a,i}}^{0}andμa,i1\mu_{\text{a,i}}^{1})
off of the mismatched arm cavity in some detail.
The𝔯i​i​(Ω)\mathfrak{r}_{ii}(\Omega)and𝔱i​j​(Ω)\mathfrak{t}_{ij}(\Omega)inEq.17describe the reflection of fields off
of the arm including the dynamics of the arm cavity alone. Two
quantities are of particular interest when additionally accounting for
the full dynamics of the HOM in the SEC.
In the picture suggested byFig.2, in addition to
the dynamics of its own cavity, the fundamental can be thought of as
interacting with the HOM’s coupled cavity which itself behaves as an
effective cavity as described byEqs.2and3. Here,
the transmission into the HOM cavity is𝔱10=Υ​(1−Υ)​(𝔯a​1+α​𝔯a​0)\mathfrak{t}_{10}=\sqrt{\Upsilon(1-\Upsilon)}(\mathfrak{r}_{\text{a}1}+\alpha\mathfrak{r}_{\text{a}0}), rather thantit_{\text{i}}, the transmission out of the cavity is𝔱01=−Υ​(1−Υ)​(𝔯a​0+α​𝔯a​1)\mathfrak{t}_{01}=-\sqrt{\Upsilon(1-\Upsilon)}(\mathfrak{r}_{\text{a}0}+\alpha\mathfrak{r}_{\text{a}1}),
rather thantit_{\text{i}},
and the HOM cavity SEC loop suppression is[1−rs​𝔯11​e−2​i​(Ω​Ls/c−ψs)]−1[1-r_{\text{s}}\mathfrak{r}_{11}\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c-\psi_{\text{s}})}]^{-1}where𝔯11=𝔯a​1−Υ​(𝔯a​1+α​𝔯a​0)\mathfrak{r}_{11}=\mathfrak{r}_{\text{a}1}-\Upsilon(\mathfrak{r}_{\text{a}1}+\alpha\mathfrak{r}_{\text{a}0}).

The first quantity of interest is the reflection of the fundamental
mode off of the mismatched arm cavity,
i.e.Ea,r0/Ea,i0E_{\text{a,r}}^{0}/E_{\text{a,i}}^{0}including the full dynamics of
the HOM but without the presence of the fundamental’s SEC, which is𝔯~a​(Ω)=𝔯00​(Ω)+rs​𝔱01​(Ω)​𝔱10​(Ω)​e−2​i​(Ω​Ls/c−ψs)1−rs​𝔯11​(Ω)​e−2​i​(Ω​Ls/c−ψs).\tilde{\mathfrak{r}}_{\text{a}}(\Omega)=\mathfrak{r}_{00}(\Omega)+\frac{r_{\text{s}}\mathfrak{t}_{01}(\Omega)\mathfrak{t}_{10}(\Omega)\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c-\psi_{\text{s}})}}{1-r_{\text{s}}\mathfrak{r}_{11}(\Omega)\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c-\psi_{\text{s}})}}.(20)

To orderΥ\Upsilon, this is𝔯~a​(Ω)=(1−Υ)​𝔯a​0−α​Υ​𝔯a​1−Υ​(𝔯a​0+α​𝔯a​1)​(𝔯a​1+α​𝔯a​0)​rs​e−2​i​(Ω​Ls/c−ψs)1−rs​𝔯a​1​e−2​i​(Ω​Ls/c−ψs).\tilde{\mathfrak{r}}_{\text{a}}(\Omega)=(1-\Upsilon)\mathfrak{r}_{\text{a}0}-\alpha\Upsilon\mathfrak{r}_{\text{a}1}\\
-\Upsilon(\mathfrak{r}_{\text{a}0}+\alpha\mathfrak{r}_{\text{a}1})(\mathfrak{r}_{\text{a}1}+\alpha\mathfrak{r}_{\text{a}0})\frac{r_{\text{s}}\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c-\psi_{\text{s}})}}{1-r_{\text{s}}\mathfrak{r}_{\text{a}1}\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c-\psi_{\text{s}})}}.(21)

The mismatched reflection𝔯~a​(Ω)\tilde{\mathfrak{r}}_{\text{a}}(\Omega)given byEq.21should then be used in place of
the perfectly matched reflection𝔯a​(Ω)\mathfrak{r}_{\text{a}}(\Omega)given byEq.2inSectionII.1in
order to compute the RSE reflection𝔯rse​(Ω)\mathfrak{r}_{\text{rse}}(\Omega)Eq.7in the presence of mode mismatch.

The first term in this mismatched fundamental arm reflectionEq.21is just the direct reflection of
the fundamental off of the arm cavity (reduced by the fractionΥ\Upsilonof the fundamental scattered into the HOM). The second term
represents the process where the fundamental scatters into the HOM,
the HOM reflects directly off of the arm cavity, and then the HOM
scatters back into the fundamental. This is the analogue of the prompt
reflection off of a simple cavity, i.e. the first term inEq.2. The final term describes the
process where the fundamental scatters into the HOM, the HOM
experiences the dynamics of its SEC, followed by the scattering of the
HOM back into the fundamental. This is the analogue of the second term
inEq.2.

The second quantity of interest is the reflection of the HOM off of
the mismatched arm and the subsequent scattering into the
fundamental. This can equivalently be thought of as the transmission
of a HOM incident on the mismatched arm cavity into the fundamental on
reflection, i.e.Ea,r0/Ea,i1E_{\text{a,r}}^{0}/E_{\text{a,i}}^{1}including the full
dynamics of the HOM but without the presence the fundamental’s SEC,
which is𝔱a,h​(Ω)=𝔱01​(Ω)1−rs​𝔯11​(Ω)​e−2​i​(Ω​Ls/c−ψs).\mathfrak{t}_{\text{a,h}}(\Omega)=\frac{\mathfrak{t}_{01}(\Omega)}{1-r_{\text{s}}\mathfrak{r}_{11}(\Omega)\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c-\psi_{\text{s}})}}.(22)

To orderΥ\sqrt{\Upsilon}, which is sufficient for calculating the
squeezing degradations to orderΥ\Upsilon, this is𝔱a,h​(Ω)=Υ​(𝔯a​0+α​𝔯a​1)1−rs​𝔯a​1​e−2​i​(Ω​Ls/c−ψs).\mathfrak{t}_{\text{a,h}}(\Omega)=\frac{\sqrt{\Upsilon}(\mathfrak{r}_{\text{a}0}+\alpha\mathfrak{r}_{\text{a}1})}{1-r_{\text{s}}\mathfrak{r}_{\text{a}1}\mathrm{e}^{-2\mathrm{i}(\Omega L_{\text{s}}/c-\psi_{\text{s}})}}.(23)

In the picture suggested byFig.2, this is the
transmissionΥ​(𝔯a​0+α​𝔯a​1)\sqrt{\Upsilon}(\mathfrak{r}_{\text{a}0}+\alpha\mathfrak{r}_{\text{a}1})of a
HOM through the HOM coupled cavity, which is analogous to the
transmissionEq.3through a simple
cavity.

The HOM does not experience the same optical system configured for RSE
that the fundamental experiences. In particular, the extra Gouy phaseψs\psi_{\text{s}}that the HOM accumulates in the SEC means that the HOM SEC
is generically detuned even though the fundamental is not. The
different resonance conditions in the arm further change the dynamics
of the HOM in the SEC. There is a continuum of behavior between exact
HOM anti-resonance withψs=π/2\psi_{\text{s}}=\pi/2and exact HOM resonance withψs=0\psi_{\text{s}}=0, but we will often consider these two extreme cases in
detail inSectionIV. Since the HOM does not
experience the phase change on reflection of the arm cavities that the
fundamental does—except for frequencies where the HOM is resonant in
the arms as is discussed inSectionIV.2—their
dynamics are enhanced forψs=0\psi_{\text{s}}=0when the round-trip phase is
positive, and are suppressed forψs=π/2\psi_{\text{s}}=\pi/2when the round-trip
phase is negative. This enhancement is sometimes known as mode harming
and this suppression known as mode healing[41,10].

These dynamics will be analyzed in various limits inSectionIVin order to calculate the squeezing
degradations.Crucially, the interference between the
fundamental and HOM on reflection of the arm cavity determines the
frequency dependence of the different types of internal mismatch
within the coupled cavity.Generally, either the fundamental or the
HOM will be near resonance of the arm cavity, and therefore either𝔯a​0​(Ω)\mathfrak{r}_{\text{a}0}(\Omega)or𝔯a​1​(Ω)\mathfrak{r}_{\text{a}1}(\Omega)will be given byEq.4while the other will be+1+1. This
interference is therefore described by the following quantity,
featured prominently inEqs.21and23,444All of the factors of𝔯a​i+α​𝔯a​j\mathfrak{r}_{\text{a}i}+\alpha\mathfrak{r}_{\text{a}j}are
proportional to1+α​𝔯a1+\alpha\mathfrak{r}_{\text{a}}sinceα=±1\alpha=\pm 1and since
one of𝔯a​i\mathfrak{r}_{\text{a}i}is𝔯a\mathfrak{r}_{\text{a}}while the other is+1+1.1+α​𝔯a​(Ω)2\displaystyle\frac{1+\alpha\mathfrak{r}_{\text{a}}(\Omega)}{2}=12​(1−α)+(1+α)​i​(Ω−δ​ωa)/γa1+i​(Ω−δ​ωa)/γa\displaystyle=\frac{1}{2}\frac{(1-\alpha)+(1+\alpha)\,\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{a}}}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{a}}}={11+i​(Ω−δ​ωa)/γa,α=−1(quad.)i​(Ω−δ​ωa)/γa1+i​(Ω−δ​ωa)/γa,α=+1​(HOA)\displaystyle=\begin{cases}\displaystyle\frac{1}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{a}}},&\alpha=-1\penalty 10000\ (\text{quad}.)\\[10.00002pt]
\displaystyle\frac{\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{a}}}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{a}}},&\alpha=+1\penalty 10000\ (\text{HOA})\end{cases}(24)

With quadratic mismatch, the interference is constructive at low
frequencies and becomes destructive above the arm cavity pole when the
reflection of the resonant field off of the arm cavity changes
sign. The frequency dependence of quadratic mismatch thus has a
characteristic low-pass behavior. For higher order aberrations, on the
other hand, the interference is destructive at low frequencies and so
the frequency dependence has a characteristic high-pass
behavior.555The interference will not be exactly high-pass or
low-pass since𝔯a\mathfrak{r}_{\text{a}}is not exactly+1+1for a non-resonant field
due both to the small phase shift present inEq.4even when|Ω−δ​ωa|≫1|\Omega-\delta\omega_{\text{a}}|\gg 1and due to
optical loss in the arm cavity.SinceEq.24is proportional to𝔱i​j​(Ω)\mathfrak{t}_{ij}(\Omega), in the picture suggested byFig.2,Eq.24is
the transmission between the two coupled cavities. The HOM SEC can
therefore be thought of as being AC coupled into the fundamental SEC
through higher order aberrations while being DC coupled through
quadratic mismatch.

## IIIQuadratic and higher order thermal aberrations

Thermal aberrations are the result of unwanted heating occurring in
optics that induce both thermorefractive and thermoelastic
effects. The primary issue in gravitational wave detectors is the
thermal aberrations generated by heating in the arm cavity test mass
optics due to absorbing parts-per-million (ppm) of the high
intracavity power in their Bragg coatings[30]. In this
context, there are two significant sources of thermal
aberrations[32,33,56]. The
first and most significant for fused silica optics is the
thermorefractive lens in the input test mass (ITM) substrates through
which the optical fields must pass in order to enter and exit the arm
cavities. The second is the thermoelastic deformations which alter the
shape of the high reflective mirror surface of the test mass
mirrors.SectionIII.1describes how these thermal
aberrations can be decomposed into quadratic and higher order effects
and the resulting higher order mode couplings that they
generate.SectionIII.2describes the effects of these
aberrations inside a coupled cavity, as inFig.1,
and justifies the simple model described inSectionsII.2and2.

## III.1Higher order mode couplings due to quadratic and higher order thermal aberrations

The Hello-Vinet
model[32,33,56]provides a
reasonable approximation for the thermal lensing and thermoelastic
effects and is the basis for the analysis in this work. The model
computes the effective optical path difference (OPD) that an optical
field experiences across its wavefront due to thermal
aberrations.Figure3shows the thermal lensing that
develops in the substrate of the test mass optic of a LIGO-like arm
cavity due to the heating of the laser incident on the high
reflective (HR) coating of the mirror. It also depicts how we
separate the thermal aberrations into a quadratic and higher order
term by writing the OPD asZ​(r,ϕ)=a​r2+zhoa​(r,ϕ),Z(r,\phi)=ar^{2}+z_{\text{hoa}}(r,\phi),(25)

whererris the radial coordinate andϕ\phiis the azimuthal
coordinate of the plane perpendicular to the direction of travel of
the optical field.
WhenZ​(r,ϕ)Z(r,\phi)describes the OPD obtained by propagation through the
test mass substrate, the quadratic term isa=−1/2​ftha=-1/2f_{\text{th}}and
represents the equivalent thin lens with focal lengthfthf_{\text{th}}that could be used to describe the thermal lensing effect and is shown
in orange inFig.3. WhenZ​(r,ϕ)Z(r,\phi)describes the
displacement due to elastic deformation of the surface of a mirror, the quadratic term isa=1/2​Rtha=1/2R_{\text{th}}. If the radius of curvature of the cold mirror isRcR_{\text{c}}, a mirror with radius of curvatureR=(1/Rc+1/Rth)−1R=(1/R_{\text{c}}+1/R_{\text{th}})^{-1}could be used to describe how the thermoelastic
effect changes the wavefront curvature.
More broad analysis of this equivalent thin lens and effective mirror
has been performed to quantify the impact of such aberrations on the
detectors[52,57].

On top of this quadratic lensing there are higher order termszhoa​(r,ϕ)z_{\text{hoa}}(r,\phi)in the OPD that can be expanded into bases such
as Zernike or Seidel polynomials. The residual between the actual
thermal lensing and the quadratic approximation is shown in red inFig.3. This residual is relatively small at the
center where the bulk of the optical intensity is found but quickly
rises towards the edges of the optic. We define this residual as the
higher order aberrations (HOA) which contains everything beyond the
quadratic term, such as spherical aberrations due to the non-parabolic
nature of the thermal lensing and elastic deformations.Figure 3:Optical path length differences resulting from the
propagation through the substrate of a LIGO-like test mass due to
thermal aberrations generated by the uniform absorption of a4​σ=\qty​10.64\sigma=\qty{10.6}{}diameter beam. Computed using the
axisymmetric Hello-Vinet[32]model. The
equivalent quadratic thin lens is shown along with the residual
OPD relative to this lens. We refer to the aberrations generated
by these distortions as quadratic mismatch and higher order
aberrations (HOA), respectively. We parameterize the HOA mismatch
by the equivalent OPDrelativeto the perfect
compensation of an optic which may have of order one watt
absorbed in the coatings. This parameterization thus allows for negative
relative absorbed powerPrelP_{\text{rel}}which corresponds to an imperfect
compensation resulting in a negative thermal lens. The quadratic
mismatch is parameterized by the fractional changeΔ​w/w\Delta w/wbetween
the beam sizes of the eigenmodes on either side of the ITM. See the
last paragraph ofSectionIII.1for details.

In the absence of higher order modes, an optical field at a given
point is described by two parameters, which can be taken to be the beam
radiuswwand the wavefront curvature, or defocus,SS. These are
typically combined into a complexqqparameter as1/q=S−2​i/k​w21/q=S-2\mathrm{i}/kw^{2}so that the spatial profile of the field is proportional
to the Gaussiane−i​k​r2/2​q\mathrm{e}^{-\mathrm{i}kr^{2}/2q}. The thin lensing is used to
propagate beams throughout the optical system using the standard ABCD
matrices for components, such as surface reflections and
transmissions, and lenses[49]. In particular, in the
case of the substrate thermal lens, the beam parameterqqbefore
passing through the substrate is related to the beam parameterq^\hat{q}after the substrate by1q^=C+D/qA+B/q=1q−1fth.\frac{1}{\hat{q}}=\frac{C+D/q}{A+B/q}=\frac{1}{q}-\frac{1}{f_{\text{th}}}.(26)

The case of the thermoelastic deformation is similar, with the defocus
changing by something proportional to2/R2/R, rather than1/fth1/f_{\text{th}}, with the details depending on whether the field is
reflecting from or transmitting through the substrate and from which
direction. In general, we use hats onqqparameters to denote theqqparameter transformed by the ABCD matrix between two neighboring nodes
inFig.1.

The total round-trip ABCD matrix is used to approximate the resonant
spatial eigenmode of a cavity including all quadratic effects for
infinite sized optics as is discussed further inAppendixB.
For a geometrically stable cavity, a complexqqparameter can be
determined at every spatial pointμ\mu.Figure1shows
several points of particular interest. Following the beam entering the
arm cavity from the SEC,qarq_{\text{ar}}in the SEC incident on the AR surface
of the ITM,qsubq_{\text{sub}}inside the substrate of the ITM incident on the HR
surface, andqhrq_{\text{hr}}inside the arm cavity transmitted through the
ITM. The reversed beam parameters−q∗-q^{*}describe the beam propagating
in the opposite direction leaving the arm cavity and entering the SEC.

The above analysis only describes the fundamental mode and thus the
quadratic part of the wavefront characterized by the beam size and
defocus. When there is higher order spatial structure, optical fields
are typically defined in terms of orthogonal modes whose spatial
profile is usually described by Hermite- or Laguerre-Gauss modes with
shapes that are also determined by the complexqqparameters[49]. For our purposes it is most convenient
to define the mode shapes in terms of the associated Laguerre
polynomialsLpℓL_{p}^{\ell}asu\displaystyle u(r,ϕ;q)p​ℓ{}_{p\ell}(r,\phi;q)=2​p!π​(p+|ℓ|)!​1w​(2​rw)|ℓ|​Lp|ℓ|​(2​r2w2)​ei​ℓ​ϕ​e−i​k​r2/2​q\displaystyle=\sqrt{\frac{2p!}{\pi(p+|\ell|)!}}\frac{1}{w}\left(\frac{\sqrt{2}r}{w}\right)^{|\ell|}\!\!L_{p}^{|\ell|}\!\left(\frac{2r^{2}}{w^{2}}\right)\mathrm{e}^{\mathrm{i}\ell\phi}\,\mathrm{e}^{-\mathrm{i}kr^{2}/2q}≡Up​ℓ​(r,ϕ,w)​e−i​k​r2/2​q,\displaystyle\equiv U_{p\ell}(r,\phi,w)\,\mathrm{e}^{-\mathrm{i}kr^{2}/2q},(27)

and then expand the field at a given pointμ\muin terms of these
higher order modes (HOMs) as[11]Eμ​(r,ϕ)=∑p=0∞∑ℓ=−∞∞cp​ℓ​(qμ)​up​ℓ​(r,ϕ;qμ)​ei​(2​p+|ℓ|+1)​ΞμE_{\mu}(r,\phi)=\sum_{p=0}^{\infty}\sum_{\ell=-\infty}^{\infty}c_{p\ell}(q_{\mu})\,u_{p\ell}(r,\phi;q_{\mu})\,\mathrm{e}^{\mathrm{i}(2p+|\ell|+1)\Xi_{\mu}}(28)

whereΞμ=arccos⁡(Re⁡qμ/Im⁡qμ)\Xi_{\mu}=\arccos(\operatorname{Re}q_{\mu}/\operatorname{Im}q_{\mu})is “the” Gouy phase at
the pointμ\mu.666Most references include the exponentialei​(2​p+|ℓ|+1)​Ξ\mathrm{e}^{\mathrm{i}(2p+|\ell|+1)\Xi}in the definition ofup​ℓ​(r,ϕ;q)u_{p\ell}(r,\phi;q), however we write it like this because it makes
the concept of the Gouy phase of a cavity more clear and simplifies
the definition of the operators inEqs.32and35.SeeAppendixBfor a detailed discussion of the
various meanings of a Gouy phase. Different mode shapes,
i.e. differentqqparameters, can then describe the same field with
different expansion coefficientscp​ℓ​(q)c_{p\ell}(q). The coupling between
different modes described with differentqqparameters is given by
the overlap⟨us​m​(q2)|up​ℓ​(q1)⟩=∫us​m∗​(r,ϕ;q2)​up​ℓ​(r,ϕ;q1)​dA\langle u_{sm}(q_{2})|u_{p\ell}(q_{1})\rangle=\int\!u_{sm}^{*}(r,\phi;q_{2})\,u_{p\ell}(r,\phi;q_{1})\,\mathrm{d}A(29)

whered​A=r​d​r​d​ϕ\mathrm{d}A=r\,\mathrm{d}r\,\mathrm{d}\phiand the integral is taken over
the cross-sectional area of the beam.

The quadratic mode mismatch between two beams described byq1q_{1}andq2q_{2}is represented in a two-dimensional space of beam sizewwand
defocusSS[45]. For two separate cavities connected by
some arbitrary telescope, they could be mismatched in eitherwworSS. However, the steady-state boundary condition for a coupled cavity
sharing an interface with standing waves on either side is that the
wavefront curvature of the resonant fields must match at this
interface. This has the consequence that any quadratic lensing change
in the extraction cavity, regardless of where it happens, results only
in a beam size difference between the arm and extraction cavity
eigenmodes at the ITM HR surface. The fractional mismatch between two
modes with the same curvature but different beam sizesw1w_{1}andw2w_{2}is1−|⟨u00​(q2)|u00​(q1)⟩|2=1−4​(w1​w2w12+w22)2≈(Δ​ww)21-|\langle u_{00}(q_{2})|u_{00}(q_{1})\rangle|^{2}=1-4\left(\frac{w_{1}w_{2}}{w_{1}^{2}+w_{2}^{2}}\right)^{2}\approx\left(\frac{\Delta w}{w}\right)^{2}(30)

whereΔ​w=w1−w2\Delta w=w_{1}-w_{2}andw=(w1+w2)/2w=(w_{1}+w_{2})/2.

Now suppose that an optical field described byq1q_{1}passes through a
substrate thermal lens with an OPD given byEq.25and then interacts with another field
described byq2q_{2}. Sincea=−1/2​ftha=-1/2f_{\text{th}}in this case, the
scattering of the HOMs between these two fields is⟨us​m(\displaystyle\big\langle u_{sm}(q2)|e−i​k​Z​(r,ϕ)|up​ℓ(q1)⟩\displaystyle q_{2})\big|\mathrm{e}^{-\mathrm{i}kZ(r,\phi)}\big|u_{p\ell}(q_{1})\big\rangle=∫Us​m∗(r,ϕ,w2)Up​ℓ(r,ϕ,w1)e−i​k​zhoa​(r,ϕ)×exp⁡{i​k​r22​[1q2∗−(1q1−1fth)]}​d​A\displaystyle=\begin{aligned} \int\!U_{sm}^{*}(&r,\phi,w_{2})\,U_{p\ell}(r,\phi,w_{1})\,\mathrm{e}^{-\mathrm{i}kz_{\text{hoa}}(r,\phi)}\\
&\times\exp\!{\left\{\!\frac{\mathrm{i}kr^{2}}{2}\!\left[\frac{1}{q_{2}^{*}}-\left(\!\frac{1}{q_{1}}-\frac{1}{f_{\text{th}}}\!\right)\right]\!\right\}}\,\mathrm{d}A\end{aligned}=⟨us​m​(q2)|e−i​k​zhoa​(r,ϕ)|up​ℓ​(q^1)⟩\displaystyle=\big\langle u_{sm}(q_{2})\big|\mathrm{e}^{-\mathrm{i}kz_{\text{hoa}}(r,\phi)}\big|u_{p\ell}(\hat{q}_{1})\big\rangle(31)

where the second line follows since the term in parenthesis is1/q^11/\hat{q}_{1}(cf.Eq.26) and since the lens does not
change the beam sizew^1=w1\hat{w}_{1}=w_{1}. In other words, the coupling
between the HOMs of a field directly before it encounters a thermal
lens with those of a field after it experiences those thermal
aberrations is described by two effects. First, the quadratic terma​r2ar^{2}transformsqq, thus changing the defocusSS. The remaining
coupling is then the scattering between the two fields with the new
defocus (in the new basisq^1\hat{q}_{1}) due only to the higher order
aberrations. The situation is the same for a thermoelastic deformation
wherea=1/2​Rtha=1/2R_{\text{th}}, andEq.31holds for
any OPD or elastic deformation of the formEq.25.

For the rest of this work, we describe the thermal aberrations as the
deviation from a perfectly compensated state as follows. We imagine a
scenario where the thermal actuators are set to perfectly compensate
for of order one watt of absorbed power but where the actual absorbed
power differs from that byPrelP_{\text{rel}}. This difference can be positive in
which case the residual thermal aberrations result in a positive
thermal lens and elastic deformations with negative defocus; whenPrelP_{\text{rel}}is negative, the signs are reversed. We further imagine that
in this imperfectly compensated state the thermal actuators can
independently target the quadratic mismatch without changing the
higher order aberrations. We then generate the appropriate OPDEq.25for a givenPrelP_{\text{rel}}relative to the
perfectly compensated state and parameterize the two types of
aberrations by
- 1.

Removing the quadratic terma​r2ar^{2}fromEq.25. Rather than using the equivalent thin
lens with focal lengthfth=−1/2​af_{\text{th}}=-1/2a, we directly set the
focal lengthfthf_{\text{th}}of the substrate lens to produce a givenΔ​w/w\Delta w/windependent ofPrelP_{\text{rel}}.Quadratic mismatch is thus
parameterized byΔ​w/w\Delta w/w.
- 2.

The remaining termszhoa​(r)z_{\text{hoa}}(r)are added as the OPD of
the substrate lens or the elastic deformation of the optic
surface.The higher order aberrations are thus parameterized
directly by the absorptionPrelP_{\text{rel}}relative to the perfectly
compensated state.

In other words, we use the red curve inFig.3to
define the higher order aberrations for a given powerPrelP_{\text{rel}}relative
to the perfectly compensated state and choose the orange curve
independently of the total blue curve to produce a givenΔ​w/w\Delta w/w.
For a sense of scale, the equivalent thin lens needed to produceΔ​w/w=\qty​5%\Delta w/w=\qty{5}{\%}is generated by of order\qty30 of uniform
absorption for both LIGO A♯\sharpand CE. This parameterization is,
heuristically, a measure of how well a thermal actuator must correct
each type of aberration (expressed in terms of equivalent residual
beam-heating and beam size error) in order to reduce the squeezing
degradations discussed inSectionIVbelow some
target. However, this cannot be taken too far as the quantitative
squeezing degradations due to some thermal aberrations are highly
sensitive to the details of those aberrations and the way in which
they have been decomposed, and it would be difficult to derive
meaningful quantitative requirements without having a complete design
for a thermal actuator in hand.

## III.2Thermal aberrations inside a coupled cavity

Calculating squeezing degradations requires knowing how optical fields
propagate throughout the coupled cavity. As inSectionII.2, it is therefore useful to analyze the
reflection of an optical field off of the arm cavity in the presence
of thermal aberrations. This is the reflection of a field at the nodeμa,i\mu_{\text{a,i}}(with beam parameterqarq_{\text{ar}}) shown inFig.1to the field at the nodeμa,r\mu_{\text{a,r}}(with beam parameter−qar∗-q_{\text{ar}}^{*}) without the SEM present. FromFig.1, the exact operator for this reflection is𝐑a=𝐋as[ri𝐒ss−reti2𝐒sh(𝟏−rire𝐏a2𝐒hh)−1𝐏a2𝐒hs]𝐋sa.\mathbf{R}_{\text{a}}=\mathbf{L}_{\text{as}}\Big[\\
r_{\text{i}}\mathbf{S}_{\text{ss}}-r_{\text{e}}t_{\text{i}}^{2}\mathbf{S}_{\text{sh}}\left(\mathbf{1}-r_{\text{i}}r_{\text{e}}\mathbf{P}_{\text{a}}^{2}\mathbf{S}_{\text{hh}}\right)^{-1}\mathbf{P}_{\text{a}}^{2}\mathbf{S}_{\text{hs}}\Big]\mathbf{L}_{\text{sa}}.(32)

In the absence of any thermal aberrations all of the lens𝐋i​j\mathbf{L}_{ij}and surface𝐒i​j\mathbf{S}_{ij}operators are𝟏\mathbf{1}.
The exact dynamics described byEq.32are
equivalent to those described inSectionII.2ifEq.32is equivalent toEq.17, i.e. if matrices𝐔i\mathbf{U}_{\text{i}}and𝐔r\mathbf{U}_{\text{r}}exist such thatEq.32can be written as𝐑a=𝐔r​[ri​𝟏−re​ti2​(𝟏−ri​re​𝐏a2)−1​𝐏a2]​𝐔i\mathbf{R}_{\text{a}}=\mathbf{U}_{\text{r}}\Big[r_{\text{i}}\mathbf{1}-r_{\text{e}}t_{\text{i}}^{2}\left(\mathbf{1}-r_{\text{i}}r_{\text{e}}\mathbf{P}_{\text{a}}^{2}\right)^{-1}\mathbf{P}_{\text{a}}^{2}\Big]\mathbf{U}_{\text{i}}(33)

since the term in brackets is the arm reflection in the absence of any
aberrations. This term is diagonal with each element corresponding to
the reflection of one of the HOMs off of the arm given byEq.2with the cavity detuningδ​ωa=ωfsr​ψa/π\delta\omega_{\text{a}}=\omega_{\text{fsr}}\psi_{\text{a}}/\pidetermined by the
one-way Gouy phaseψa\psi_{\text{a}}of that mode in the arm cavity.

First consider the quadratic mismatch alone which transforms theqqparameters and only affects the beam size and defocus. The round-trip
ABCD matrix of the arm cavity determinesqhrq_{\text{hr}}and the round-trip
ABCD matrix of the SEC determinesqarq_{\text{ar}}andqsubq_{\text{sub}}. Therefore there
can be no quadratic mismatch betweenqarq_{\text{ar}}andqsubq_{\text{sub}},
i.e.q^ar=qsub\hat{q}_{\text{ar}}=q_{\text{sub}}. The only quadratic mismatch which
can occur is between the modes of the two cavities, and soq^sub≠qhr\hat{q}_{\text{sub}}\neq q_{\text{hr}}in general. This also means that the
beam size and defocus of the SEC eigenmode are determined by both the
substrate thermal lens and the ITM thermoelastic deformation while the
arm eigenmode is only affected by the surface deformation. Following
the beam traveling from the SEC (at the nodeμa,i\mu_{\text{a,i}}) into the
arm cavity, the thermal lens first changes the defocus of the beamSsub=Sar−1/fthS_{\text{sub}}=S_{\text{ar}}-1/f_{\text{th}}but does not affect the
beam sizew^ar=war=wsub\hat{w}_{\text{ar}}=w_{\text{ar}}=w_{\text{sub}}. The radius
of curvature of the ITM isRi=(1/Ri​0+1/Rth)−1R_{\text{i}}=(1/R_{\text{i}0}+1/R_{\text{th}})^{-1}whereRi​0R_{\text{i}0}is the radius of curvature of the perfectly
compensated mirror. Upon passing through the HR surface of the mirror,
the defocus of the beam is transformed toS^sub=Ssub+(n−1)/Ri\hat{S}_{\text{sub}}=S_{\text{sub}}+(n-1)/R_{\text{i}}, wherennis the index of refraction of the
substrate, but again does not change the beam sizew^sub=wsub\hat{w}_{\text{sub}}=w_{\text{sub}}. Due to the steady state boundary conditions at the
ITM HR surface discussed above, it must be the case thatShr=S^subS_{\text{hr}}=\hat{S}_{\text{sub}}and soShr\displaystyle S_{\text{hr}}(Ri​0,Rth)=\displaystyle(R_{\text{i}0},R_{\text{th}})=S\displaystyle S(Ri​0,Rth,fth)ar−1fth+(n−1)(1Ri​0+1Rth).{}_{\text{ar}}(R_{\text{i}0},R_{\text{th}},f_{\text{th}})-\frac{1}{f_{\text{th}}}+(n-1)\left(\frac{1}{R_{\text{i}0}}+\frac{1}{R_{\text{th}}}\right).(34)

It is not necessarily the case thatw^sub=whr\hat{w}_{\text{sub}}=w_{\text{hr}}, though, and so the only question is whetherwhrw_{\text{hr}}is the same aswarw_{\text{ar}}. Note that while the
defocusSarS_{\text{ar}}is determined entirely by the ITM lens and
curvature, the beam sizewarw_{\text{ar}}is determined by the full
geometry of the SEC which, in the actual detectors, is additionally
controlled by other optics and thermal actuators which are not
necessarily located at the
ITM[13,48,29]. Nevertheless,Eq.34is always true, and any lensing caused by any of
these actuators or optics can only changewarw_{\text{ar}}regardless of
the Gouy phase in which they operate.

We next examine the exact form of the operators shown inFig.1and focus on the case of azimuthal
symmetry. From now on we will also denote the matrix of couplings⟨us​m​(q2)|O​(r)|up​ℓ​(q1)⟩\langle u_{sm}(q_{2})|O(r)|u_{p\ell}(q_{1})\ranglefor some arbitrary
aberrationO​(r)O(r)simply as⟨q2|O​(r)|q1⟩\langle q_{2}|O(r)|q_{1}\rangle. The
coupling between any two of the nodes describing the aberrations in
the ITM shown inFig.1is⟨q2|e−i​k​Z​(r)|q1⟩\langle q_{2}|\mathrm{e}^{-\mathrm{i}kZ(r)}|q_{1}\ranglewhich, byEq.31, is⟨q2|e−i​k​zhoa​(r)|q^1⟩\langle q_{2}|\mathrm{e}^{-\mathrm{i}kz_{\text{hoa}}(r)}|\hat{q}_{1}\ranglein
all cases. Ifzl​(r)z_{\text{l}}(r)is the higher order OPD of the substrate thermal
lens andzs​(r)z_{\text{s}}(r)is the higher order thermoelastic
deformations of the mirror HR surface, these operators are
therefore777Due to our simplification of azimuthal symmetry, we
can ignore odd order modes. Therefore, two operations are simplified in the tangential
plane:
We exclude the parity operation
for the backwards propagation through an OPD which would otherwise be
necessary since a beam traveling right-to-left vs. left-to-right will
see an inversion in this direction; and we do not explicitly include
the parity operator for the coordinate system transformation on
reflection which applies aπ\piphase shift to tangential odd order modes.𝐋sa\displaystyle\mathbf{L}_{\text{sa}}\!=⟨qsub|e−i​k​zl|q^ar⟩\displaystyle=\!\big\langle q_{\text{sub}}\big|\mathrm{e}^{-\mathrm{i}kz_{\text{l}}}\big|\hat{q}_{\text{ar}}\big\rangle𝐋as\displaystyle\mspace{12.0mu}\mathbf{L}_{\text{as}}\!=⟨−qar∗|e−i​k​zl|−q^sub∗⟩\displaystyle=\!\big\langle\!\!-\!q_{\text{ar}}^{*}\big|\mathrm{e}^{-\mathrm{i}kz_{\text{l}}}\big|\!-\!\hat{q}^{*}_{\text{sub}}\big\rangle(35a)𝐒hh\displaystyle\mathbf{S}_{\text{hh}}\!=⟨qhr|e2​i​k​zs|−q^hr∗⟩\displaystyle=\!\big\langle q_{\text{hr}}\big|\mathrm{e}^{2\mathrm{i}kz_{\text{s}}}\big|\!-\!\hat{q}_{\text{hr}}^{*}\big\rangle𝐒ss\displaystyle\mspace{12.0mu}\mathbf{S}_{\text{ss}}\!=⟨−qsub∗|e−2​i​n​k​zs|q^sub⟩\displaystyle=\!\big\langle\!\!-\!q_{\text{sub}}^{*}\big|\mathrm{e}^{-2\mathrm{i}nkz_{\text{s}}}\big|\hat{q}_{\text{sub}}\big\rangle(35b)𝐒hs\displaystyle\mathbf{S}_{\text{hs}}\!=⟨qhr|ei​(1−n)​k​zs|q^sub⟩\displaystyle=\!\big\langle q_{\text{hr}}\big|\mathrm{e}^{\mathrm{i}(1-n)kz_{\text{s}}}\big|\hat{q}_{\text{sub}}\big\rangle𝐒sh\displaystyle\mspace{12.0mu}\mathbf{S}_{\text{sh}}\!=⟨−qsub∗|ei​(1−n)​k​zs|−q^hr∗⟩\displaystyle=\!\big\langle\!\!-\!q_{\text{sub}}^{*}\big|\mathrm{e}^{\mathrm{i}(1-n)kz_{\text{s}}}\big|\!-\!\hat{q}_{\text{hr}}^{*}\big\rangle(35c)

We now examine the thermal lens and thermoelastic deformation
separately to identify which operators inEq.35are
the𝐔i\mathbf{U}_{\text{i}}and𝐔r\mathbf{U}_{\text{r}}inEq.33which
reproduceEq.32in each of these cases, thus
justifyingEqs.17and19and the model ofSectionsII.2and2.

## Substrate thermal lens

First consider the case where there is only a substrate thermal lens,
which is the most significant effect for fused silica optics. In this
case,zs=0z_{\text{s}}=0and so the surface operators are𝐒hh=𝐒ss=𝟏,𝐒hs=⟨qhr|q^sub⟩=𝐒sh⊺=⟨−q^hr∗|−qsub∗⟩.\mathbf{S}_{\text{hh}}=\mathbf{S}_{\text{ss}}=\mathbf{1},\quad\mathbf{S}_{\text{hs}}=\langle q_{\text{hr}}|\hat{q}_{\text{sub}}\rangle=\mathbf{S}_{\text{sh}}^{\intercal}=\langle-\hat{q}_{\text{hr}}^{*}|-q_{\text{sub}}^{*}\rangle.(36)
- •

For quadratic lensing,zl=0z_{\text{l}}=0and so𝐋as=𝐋sa=𝟏\mathbf{L}_{\text{as}}=\mathbf{L}_{\text{sa}}=\mathbf{1}. In this case, the quadratic thermal lensfthf_{\text{th}}produces a beam size errorΔ​w/w\Delta w/wbetween the modes of the two
cavities so thatq^sub≠qhr\hat{q}_{\text{sub}}\neq q_{\text{hr}}. Therefore𝐒hs=𝐒sh⊺≠1\mathbf{S}_{\text{hs}}=\mathbf{S}_{\text{sh}}^{\intercal}\neq 1.Equation33is thusEq.32if𝐔i=𝐒hs\mathbf{U}_{\text{i}}=\mathbf{S}_{\text{hs}}and𝐔r=𝐒sh\mathbf{U}_{\text{r}}=\mathbf{S}_{\text{sh}}. For
small mismatch, to orderΔ​w/w\Delta w/w,𝐒sh⊺=𝐒sh−1\mathbf{S}_{\text{sh}}^{\intercal}=\mathbf{S}_{\text{sh}}^{-1}, and
so𝐔r=𝐔i−1\mathbf{U}_{\text{r}}=\mathbf{U}_{\text{i}}^{-1}.
- •

For higher order aberrations, on the other hand,𝐋as=𝐋sa≠𝟏\mathbf{L}_{\text{as}}=\mathbf{L}_{\text{sa}}\neq\mathbf{1}sincezl≠0z_{\text{l}}\neq 0, and𝐒hs=𝐒sh=𝟏\mathbf{S}_{\text{hs}}=\mathbf{S}_{\text{sh}}=\mathbf{1}since there is no quadratic lensing (q^sub=qhr\hat{q}_{\text{sub}}=q_{\text{hr}}).Equation33is thusEq.32if𝐔i=𝐋sa\mathbf{U}_{\text{i}}=\mathbf{L}_{\text{sa}}and𝐔r=𝐋as\mathbf{U}_{\text{r}}=\mathbf{L}_{\text{as}}, and
so𝐔r=𝐔i\mathbf{U}_{\text{r}}=\mathbf{U}_{\text{i}}.

Taken together, this reproducesEq.17and the
defining relationship ofEq.19.

## Thermoelastic surface deformation

Next consider the case where there is only a thermoelastic
deformation. In this casezl=0z_{\text{l}}=0and so the lens operators are𝐋as=𝐋sa=𝟏\mathbf{L}_{\text{as}}=\mathbf{L}_{\text{sa}}=\mathbf{1}.
- •

For a quadratic deformation,zs=0z_{\text{s}}=0and so the surface
operators are again given byEq.36with𝐒hs=𝐒sh⊺≠1\mathbf{S}_{\text{hs}}=\mathbf{S}_{\text{sh}}^{\intercal}\neq 1since the quadratic surface deformationRthR_{\text{th}}produces a beam ize errorΔ​w/w\Delta w/w. As with the
quadratic thermal lens,𝐔i=𝐒hs\mathbf{U}_{\text{i}}=\mathbf{S}_{\text{hs}}and𝐔r=𝐒sh\mathbf{U}_{\text{r}}=\mathbf{S}_{\text{sh}}, and so𝐔r=𝐔i−1\mathbf{U}_{\text{r}}=\mathbf{U}_{\text{i}}^{-1}to orderΔ​w/w\Delta w/w.
- •

The case for a higher order thermoelastic deformation withzs≠0z_{\text{s}}\neq 0is more complicated since the surface operators
cannot be simplified from the general case given byEqs.35band35c. It
is therefore not possible to find operators𝐔i\mathbf{U}_{\text{i}}and𝐔r\mathbf{U}_{\text{r}}such
thatEq.33is satisfied and the
dynamics of this type of mismatch does not map cleanly onto the
dynamics described inSectionII.2.

In practice, the effects of higher order surface deformations are far
weaker than those due to the other sources of mismatch and the
dynamics are still well described byEq.33and the model ofSectionII.2.

Finally we note that, while we have focused on wavefront aberrations
generated by thermal distortions, any aberration can be broken up into
quadratic mismatch and higher order aberrations as inEq.25and all of the ensuing squeezing
degradations will behave in the same way.

## IVSqueezing degradations

Quantum noise in an interferometer used for gravitational wave
detection is caused by vacuum fluctuations in the fundamental mode of
the electromagnetic field which enter the anti-symmetric (AS)
port[19,21]. In the case of the effective coupled
cavity, these are the vacuum entering in the portμas,i\mu_{\text{as,i}}ofFig.1. Gravitational wave detectors therefore
inject squeezed vacuum states, with reduced uncertainty in one optical
quadrature, into the AS port in order to reduce this quantum noise in
that
quadrature[9,55,5,31,37,39,26,39,58]. Various
processes degrade the extent to which these squeezed vacuum states can
reduce the quantum noise, and in order to improve and design detectors
it is important to understand the frequency-dependent contribution of
each noise source to the total.

Figure4shows a budget of the quantum noises in
Cosmic Explorer using the baseline parameters ofTable2. We will describe the squeezing
degradations by the McCuller squeezing
metrics[40]. The details of using these four metrics
to make noise budgets such asFig.4are given
inAppendixA. We first give a brief overview of these
metrics and how mode mismatch contributes to them before delving into
the details of how they quantify the effects of several sources of
squeezing degradations in the following sections. Note that while we
focus on mode mismatch, the HOMs responsible for misalignment produce
squeezing degradations just as the HOMs responsible for mode mismatch
do, and so this discussion is applicable to both cases. The solid
green line labeled “AS Port SQZ” inFig.4represents the quantum noise due to the injected squeezed states in
the absence of any degradations (reduced by the fraction of squeezed
vacuum lost through either an optical loss or a mode mismatch). All of
the other traces represent one of the squeezing degradations which
limit the extent to which this squeezed vacuum can reduce the quantum
noise as follows.Figure 4:Quantum noise budget for Cosmic Explorer withΔ​w/w=\qty​5%\Delta w/w=\qty{5}{\%}andPrel=\qty​100P_{\text{rel}}=\qty{100}{}using the parameters ofTable2. Note
that this is adisplacement, rather than strain, budget. The peaks in the
noise above\qty800 are due to higher order mode resonances in the arm
cavities which both rotate the squeezed state and induce up to\qty520\milliof intrinsic phase noise; seeSectionIV.2.

## Loss or efficiency

What is called “loss” in an optomechanical system can be thought of
as the quantum noise generated by the unsqueezed vacuum coupling into
the fundamental mode of the system through either an optical loss or a
mode mismatch. When the squeezed state encounters a source of optical
loss, some of the reduced uncertainty squeezed vacuum is lost from the
system and is replaced with unsqueezed vacuum, thereby increasing the
quantum noise. This will be a frequency-dependent noise because the
transmission𝔱μ​(Ω)\mathfrak{t}_{\mu}(\Omega)of a field entering some pointμ\muin
the system
to the readout is, in general, frequency-dependent, and this frequency
dependence will be different for every source of loss. The total
quantum noise due to optical loss can be understood by incoherently
adding the unsqueezed vacuum from every loss
location[15,43].

Mode mismatch induces a loss by a similar mechanism, except in this
case, rather than being lost from the system, the squeezed vacuum in the
fundamental mode is scattered into higher order modes and is replaced
with the unsqueezed HOM vacuum which scatters into the
fundamental. Unlike with optical loss, however, this process is
coherent and the HOMs interfere with themselves and with the
fundamental. This process of scattering squeezed vacuum between the
various optical modes as they propagate throughout the optical system
and encounter different sources of mismatch will then become a true
loss when only the fundamental mode is ultimately measured on a
photodetector. Rather than coherently adding the contributions from
each HOM, it is therefore easier
to calculate the loss as the fraction of the squeezed vacuum injected
into the system which is ultimately not detected.
However, conceptually mismatch loss is caused by the same mechanism as
optical loss and its frequency dependence could, in principle, be
understood by following the dynamics of the HOMs throughout the
optical system. The combined effects of these loss mechanisms could be
quantified by the efficiencyη​(Ω)\eta(\Omega), which is the fraction of
the squeezed state injected into the AS port that is ultimately
detected.

Additionally, vacuum fluctuations produce quantum radiation
pressure noise (QRPN) when they enter the arm cavities and beat with
the carrier power circulating there. (Unsqueezed vacuum entering the system
through an optical loss or a mode mismatch in the output path between
the interferometer and photodetectors do not cause QRPN since they
never enter the arm cavities.) Ref.[40]therefore
introduces the quantum noise gainΓ​(Ω)\Gamma(\Omega), which describes how
the ponderomotive squeezing of the interferometer produces QRPN by
defining the efficiency–gain product asΓ​(Ω)​η​(Ω)=|𝔯rse​(+Ω)|2+|𝔯rse∗​(−Ω)|22.\Gamma(\Omega)\eta(\Omega)=\frac{|\mathfrak{r}_{\text{rse}}(+\Omega)|^{2}+|\mathfrak{r}_{\text{rse}}^{*}(-\Omega)|^{2}}{2}.(37)

Likewise,Γ​(Ω)​Λμ​(Ω)\Gamma(\Omega)\Lambda_{\mu}(\Omega)quantifies how much
unsqueezed vacuum coupling into the system through some sourceμ\muof
optical loss or mode mismatch is detected in the fundamental mode
including the effects of QRPN. In the case of optical loss, if𝔱μ​(Ω)\mathfrak{t}_{\mu}(\Omega)is the transfer function of the field entering the
system to the detected field, this loss isΓ​(Ω)​Λμ​(Ω)=|𝔱μ​(+Ω)|2+|𝔱μ∗​(−Ω)|22.\Gamma(\Omega)\Lambda_{\mu}(\Omega)=\frac{|\mathfrak{t}_{\mu}(+\Omega)|^{2}+|\mathfrak{t}_{\mu}^{*}(-\Omega)|^{2}}{2}.(38)

Since the loss due to mode mismatch is coherent, all sources of
mismatch must be analyzed together and this loss cannot be calculated
as simply in general. In the absence of QRPN,Γ​(Ω)=1\Gamma(\Omega)=1and
the total lossΛ​(Ω)=∑μΛμ​(Ω)\Lambda(\Omega)=\sum_{\mu}\Lambda_{\mu}(\Omega)is related to
the efficiency byΛ​(Ω)=1−η​(Ω)\Lambda(\Omega)=1-\eta(\Omega). It
is important to stress thatΓ​(Ω)​η​(Ω)\Gamma(\Omega)\eta(\Omega)andΓ​(Ω)​Λμ​(Ω)\Gamma(\Omega)\Lambda_{\mu}(\Omega)aredimensionless couplingsof how quantum vacuum (squeezed or unsqueezed) entering the system
through some mechanism is detected at the readout and do not quantify
how quantum noise affects a gravitational wave strain signal itself,
as is further discussed inSectionIV.1.3. Several
sources of loss are shown inFig.4as the
solid non-green colored traces.

The remaining two degradation mechanisms are due to the squeezed state
when it encounters dynamics that the upper and lower sidebands
experience differently. They are not caused by the unsqueezed vacuum,
but the sources of optical loss and mode mismatch which couple
unsqueezed vacuum into the fundamental mode add to the dynamics
generating these imbalances—either in phase or in magnitude. Detuned
optical cavities are a common cause of imbalanced sidebands. Since a
HOM accumulates an extra phase shift relative to the fundamental mode
due to its Gouy phase, even cavities that are tuned for the
fundamental are generally detuned for a HOM. Almost any dynamics that
couple the fundamental mode with a higher order mode will thus cause
degradations of this sort. As they are sourced by the squeezed state,
their effects on the noise are squeezing-level-dependent and can be
mitigated by reducing the magnitude of the injected squeezed vacuum at
the expense of decreasing the quantum noise reduction provided by this
vacuum.

## Squeezed state rotation

The squeezed state rotates relative to the angle at which it is
injected as it propagates through the optomechanical system when the
upper and lower sidebands acquire differential phases asθ​(Ω)=arg⁡𝔯rse​(+Ω)−arg⁡𝔯rse∗​(−Ω)2.\theta(\Omega)=\frac{\arg\mathfrak{r}_{\text{rse}}(+\Omega)-\arg\mathfrak{r}_{\text{rse}}^{*}(-\Omega)}{2}.(39)

When the signal is detected at a quadrature angleϕ≠−θ​(Ω)\phi\neq-\theta(\Omega),
some of the anti-squeezing of the squeezed vacuum injected into the AS
port is observed along with the squeezing. Radiation pressure
generates such a rotation, and detuned optical cavities, known as
filter cavities, are purposely used in gravitational wave detectors to
counteract this
rotation[35,39,58,26];
however, such a rotation is often unwanted as in the case of that due
to mode mismatch. The effects of such a frequency-dependent rotation
are shown as the dashed green line labeled “AS Port anti-SQZ” inFig.4.Quadratic HealedQuadratic HarmedHOA HealedHOA HarmedFundamental(α=−1,β=−1\alpha=-1,\beta=-1)(α=−1,β=+1\alpha=-1,\beta=+1)(α=+1,β=−1\alpha=+1,\beta=-1)(α=+1,β=+1)\alpha=+1,\beta=+1)Direct Coupling [\unit/\unit\unit{}\big/\unit{}]MM loss SNΩ≫γrse\Omega\gg\gamma_{\text{rse}}π2​c2​ΥLa2​1ℱa2​1Ω2\displaystyle\frac{\pi^{2}c^{2}\Upsilon}{L_{\text{a}}^{2}}\frac{1}{\mathcal{F}_{\text{a}}^{2}}\frac{1}{\Omega^{2}}4​c2​ΥLa2​(ℱsℱa)2​1Ω2\displaystyle\frac{4c^{2}\Upsilon}{L_{\text{a}}^{2}}\left(\frac{\mathcal{F}_{\text{s}}}{\mathcal{F}_{\text{a}}}\right)^{2}\frac{1}{\Omega^{2}}4​Υ\displaystyle 4\Upsilon16​Υ​ℱs2π2\displaystyle\frac{16\Upsilon\mathcal{F}_{\text{s}}^{2}}{\pi^{2}}—MM loss SNΩ≪γrse\Omega\ll\gamma_{\text{rse}}π2​Υℱs2\displaystyle\frac{\pi^{2}\Upsilon}{\mathcal{F}_{\text{s}}^{2}}4​Υ4\Upsilon4​La2​Υc2​(ℱaℱs)2​Ω2\displaystyle\frac{4L_{\text{a}}^{2}\Upsilon}{c^{2}}\left(\frac{\mathcal{F}_{\text{a}}}{\mathcal{F}_{\text{s}}}\right)^{2}\Omega^{2}16​La2​ℱa2​Υπ2​c2​Ω2\displaystyle\frac{16L_{\text{a}}^{2}\mathcal{F}_{\text{a}}^{2}\Upsilon}{\pi^{2}c^{2}}\Omega^{2}—MM loss QRPNΥ​π2​ℱa2​𝒦24​ℱs4\displaystyle\frac{\Upsilon\pi^{2}\mathcal{F}_{\text{a}}^{2}\mathcal{K}^{2}}{4\mathcal{F}_{\text{s}}^{4}}Υ​ℱa2​𝒦2ℱs2\displaystyle\frac{\Upsilon\mathcal{F}_{\text{a}}^{2}\mathcal{K}^{2}}{\mathcal{F}_{\text{s}}^{2}}Υ​ℱa2​𝒦2ℱs2\displaystyle\frac{\Upsilon\mathcal{F}_{\text{a}}^{2}\mathcal{K}^{2}}{\mathcal{F}_{\text{s}}^{2}}4​Υ​ℱa2​𝒦2π2\displaystyle\frac{4\Upsilon\mathcal{F}_{\text{a}}^{2}\mathcal{K}^{2}}{\pi^{2}}—SEC loss SNΩ≫γrse\Omega\gg\gamma_{\text{rse}}————2​ℱs​εsπ\displaystyle\frac{2\mathcal{F}_{\text{s}}\varepsilon_{\text{s}}}{\pi}SEC loss SNΩ≪γa\Omega\ll\gamma_{\text{a}}————π​εs2​ℱs\displaystyle\frac{\pi\varepsilon_{\text{s}}}{2\mathcal{F}_{\text{s}}}SEC loss QRPN————εs​ℱa2​𝒦22​π​ℱs\displaystyle\frac{\varepsilon_{\text{s}}\mathcal{F}_{\text{a}}^{2}\mathcal{K}^{2}}{2\pi\mathcal{F}_{\text{s}}}Strain-Referred [1​\unit1\unit{}]MM loss SNπ2​k​La​Υℱa​ℱs​ℏ​ω0Pa\displaystyle\frac{\pi}{2kL_{\text{a}}}\sqrt{\frac{\Upsilon}{\mathcal{F}_{\text{a}}\mathcal{F}_{\text{s}}}\frac{\hbar\omega_{0}}{P_{\text{a}}}}1k​La​Υ​ℱsℱa​ℏ​ω0Pa\displaystyle\frac{1}{kL_{\text{a}}}\sqrt{\frac{\Upsilon\mathcal{F}_{\text{s}}}{\mathcal{F}_{\text{a}}}\frac{\hbar\omega_{0}}{P_{\text{a}}}}Ωc​k​Υ​ℱaℱs​ℏ​ω0Pa\displaystyle\frac{\Omega}{ck}\sqrt{\frac{\Upsilon\mathcal{F}_{\text{a}}}{\mathcal{F}_{\text{s}}}\frac{\hbar\omega_{0}}{P_{\text{a}}}}2​Ωπ​c​k​Υ​ℱa​ℱs​ℏ​ω0Pa\displaystyle\frac{2\Omega}{\pi ck}\sqrt{\Upsilon\mathcal{F}_{\text{a}}\mathcal{F}_{\text{s}}\frac{\hbar\omega_{0}}{P_{\text{a}}}}—MM loss QRPN4​π​QLa​ℱs​Υ​ℱaℱs\displaystyle\frac{4\pi Q}{L_{\text{a}}\mathcal{F}_{\text{s}}}\sqrt{\frac{\Upsilon\mathcal{F}_{\text{a}}}{\mathcal{F}_{\text{s}}}}8​QLa​Υ​ℱaℱs\displaystyle\frac{8Q}{L_{\text{a}}}\sqrt{\frac{\Upsilon\mathcal{F}_{\text{a}}}{\mathcal{F}_{\text{s}}}}8​QLa​Υ​ℱaℱs\displaystyle\frac{8Q}{L_{\text{a}}}\sqrt{\frac{\Upsilon\mathcal{F}_{\text{a}}}{\mathcal{F}_{\text{s}}}}16​Qπ​La​Υ​ℱa​ℱs\displaystyle\frac{16Q}{\pi L_{\text{a}}}\sqrt{\Upsilon\mathcal{F}_{\text{a}}\mathcal{F}_{\text{s}}}—SEC loss SNΩ≫γa\Omega\gg\gamma_{\text{a}}————Ω2​c​k​2​ℱa​εsπ​ℏ​ω0Pa\displaystyle\frac{\Omega}{2ck}\sqrt{\frac{2\mathcal{F}_{\text{a}}\varepsilon_{\text{s}}}{\pi}\frac{\hbar\omega_{0}}{P_{\text{a}}}}SEC loss SNΩ≪γa\Omega\ll\gamma_{\text{a}}————12​k​La​π​εs2​ℱa​ℏ​ω0Pa\displaystyle\frac{1}{2kL_{\text{a}}}\sqrt{\frac{\pi\varepsilon_{\text{s}}}{2\mathcal{F}_{\text{a}}}\frac{\hbar\omega_{0}}{P_{\text{a}}}}SEC loss QRPN————8​QLa​ℱa​εs2​π\displaystyle\frac{8Q}{L_{\text{a}}}\sqrt{\frac{\mathcal{F}_{\text{a}}\varepsilon_{\text{s}}}{2\pi}}HOM Res.SQZ rotation gain16​ℱs3​ℱaπ4​Lac\displaystyle\frac{16\mathcal{F}_{\text{s}}^{3}\mathcal{F}_{\text{a}}}{\pi^{4}}\frac{L_{\text{a}}}{c}ℱaℱs​Lac\displaystyle\frac{\mathcal{F}_{\text{a}}}{\mathcal{F}_{\text{s}}}\frac{L_{\text{a}}}{c}8​ℱs2​ℱaπ3​Lac\displaystyle\frac{8\mathcal{F}_{\text{s}}^{2}\mathcal{F}_{\text{a}}}{\pi^{3}}\frac{L_{\text{a}}}{c}2​ℱaπ​Lac\displaystyle\frac{2\mathcal{F}_{\text{a}}}{\pi}\frac{L_{\text{a}}}{c}—Loss gain8​ℱs2π2\displaystyle\frac{8\mathcal{F}_{\text{s}}^{2}}{\pi^{2}}224​ℱsπ\displaystyle\frac{4\mathcal{F}_{\text{s}}}{\pi}4​ℱsπ\displaystyle\frac{4\mathcal{F}_{\text{s}}}{\pi}—Dephasing gain16​ℱs4π4\displaystyle\frac{16\mathcal{F}_{\text{s}}^{4}}{\pi^{4}}114​ℱs2π2\displaystyle\frac{4\mathcal{F}_{\text{s}}^{2}}{\pi^{2}}4​ℱs2π2\displaystyle\frac{4\mathcal{F}_{\text{s}}^{2}}{\pi^{2}}—Table 1:Summary of important squeezing degradations and their
dependence on detector parameters. MM loss is mode mismatch loss, SEC
loss is optical loss in the signal extraction cavity, SN is shot
noise, and QRPN is quantum radiation pressure noise. The column
headers also summarize the notation used throughout the paper
whereα\alphadetermines the type of mismatch
(cf.Eq.19) andβ=e2​i​ψs\beta=\mathrm{e}^{2\mathrm{i}\psi_{\text{s}}}determines the resonance condition of
the HOM in the SEC withβ=−1\beta=-1corresponding to mode healing
andβ=+1\beta=+1corresponding to mode harming;ψs\psi_{\text{s}}is the
one-way Gouy phase of the HOM in the SEC. Strain-referred QRPN is
multiplied by the factorQ=Pa​ℏ​ω0/M​c​Ω2Q=\sqrt{P_{\text{a}}\hbar\omega_{0}}/Mc\Omega^{2}and𝒦=−16​k​Pa/M​c​Ω2\mathcal{K}=-16kP_{\text{a}}/Mc\Omega^{2}. The direct loss couplings are
described inSectionsIV.1.1andIV.1.2and
the strain-referred loss is described inSectionIV.1.3. Note that the shot noise loss
scalings below the arm cavity pole are not relevant in practice
because the QRPN loss will be dominant
here.SectionIV.2describes the degradations
around HOM arm resonances. The HOM resonance gains are the
frequency independent factors in the McCuller metrics inEqs.53,54and55:
SQZ rotation isgs/γccg_{\text{s}}/\gamma_{\text{cc}}, loss is2​gs2g_{\text{s}}, and dephasing isgs2g_{\text{s}}^{2}.

## Dephasing

An intrinsic dephasing is generated when the magnitude of the response
to the upper and lower sidebands differ; it is quantified
by[40]Ξ​(Ω)=[|𝔯rse​(+Ω)|−|𝔯rse∗​(−Ω)|]24​Γ​(Ω)​η​(Ω).\Xi(\Omega)=\frac{\left[|\mathfrak{r}_{\text{rse}}(+\Omega)|-|\mathfrak{r}_{\text{rse}}^{*}(-\Omega)|\right]^{2}}{4\Gamma(\Omega)\eta(\Omega)}.(40)

This phase noise can be understood by the fact that the noise in the
upper and lower sidebands of a squeezed vacuum is increased relative to
that of the unsqueezed vacuum, but in a correlated way so that the
noise in one quadrature is reduced while the noise in the orthogonal
quadrature is increased[8,9]. A phase noise
is thus introduced when the sidebands experience different losses
which preserve the increased noise while degrading the correlations
responsible for defining the angle of the squeeze
ellipse[40]. The phase noise generated by this
intrinsic dephasing is shown as the dotted green line inFig.4. The other non-green dashed curves inFig.4are technical sources of phase noise as
is discussed further inAppendixA.

In the following sections we give simple approximations to these
metrics for the phenomenological model ofSectionII.2in the limits of exact HOM resonanceψs=0\psi_{\text{s}}=0and anti-resonanceψs=π/2\psi_{\text{s}}=\pi/2in the SEC. There is a continuum of behavior between
these two cases, but the dynamics of a general field will mostly be
characteristic of anti-resonance unless the mode is close to an SEC
resonance. These expressions well explain many aspects of the exact
calculations shown in all of the figures and described inAppendixDsince the dominant degradation effects will
generally be due to one of many HOMs. The degradations can then be
qualitatively understood by considering this dominant HOM as the
single HOM in this simpler model keeping in mind that the specifics of
its coupling and interference with the other HOMs not considered alter
the exact details of its dynamics and thus the resulting squeezing
degradations.

SectionIV.1discusses the broadband loss due both to the two types of
internal mode mismatch and to optical loss in the SEC.SectionIV.2describes the squeezing degradations that arise from a HOM which becomes resonant in the
arm cavities, how the locations of these resonances are determined by the detector
design, and how they may be leveraged to diagnose the thermal state of the detectors and
to tune them to improve the detector performance.Table1summarizes
how the degradations described in these sections depend on detector parameters.SectionIV.3describes a broadband rotation of the squeezed state
induced by a detuning of the SEC which can arise either by a mode mismatch or an SEC
length detuning.SectionIV.4discusses the interactions between
internal and external mismatch.SectionIV.5summarizes these
effects and how they are affected by detector design.

As this work is primarily focused on the effects of mode mismatch, we
neglect optical loss in most of the approximations to an exact model
in order to arrive at tractable expressions. However, all sources of
loss detailed inTable2are included in all of
the numerical results presented in the figures and are discussed where
appropriate in the text.

## IV.1Broadband loss

Out of all of the squeezing degradations due to mode mismatch,
broadband loss generally has the most significant impact to the overall
sensitivity of a gravitational wave detector. Since radiation pressure
obscures some characteristics of the purely optical propagation of
quantum vacuum throughout the optomechanical system, we first discuss
the direct coupling of quantum vacuum entering the
optomechanical system to the readout, as inEqs.37and38, inSectionIV.1.1in the absence of radiation
pressure and then discuss QRPN inSectionIV.1.2. The quantity that is ultimately
relevant to gravitational wave detectors, and the one that is shown in
noise budgets such asFig.4, is the effective
loss that contaminates the strain measurement itself, also known as
the signal- or strain-referred loss, as is discussed inSectionIV.1.3. Both of these losses are
summarized inTable1.

The loss due to the mode mismatch between the arm cavities and the SEC
is sometimes treated as being a contributor to the optical loss
present in the SEC. They do have some similarities since the
unsqueezed quantum vacuum responsible for each of these losses couple
into the fundamental mode in similar ways; however, there are
important differences, even in addition to the coherent nature of the
former, and they must be treated separately. We therefore describe
both of these losses to highlight the connection between the two. In
both LIGO A♯\sharpand Cosmic Explorer the total round-trip SEC loss
is\qty500. This should be taken as the totalequivalentSEC loss properly budgeting the combined effects of
both mode mismatch and optical loss as explained in this section.

## IV.1.1Direct loss coupling in the absence of radiation pressure

Since we do not consider the effects of radiation pressure in this
section, the quantum noise gain isΓ​(Ω)=1\Gamma(\Omega)=1and all of the
equations ofSectionIIdirectly apply. Furthermore, the
analytic expressions we give in this section are all for balanced
sidebands where|𝔱μ​(+Ω)|=|𝔱μ​(−Ω)||\mathfrak{t}_{\mu}(+\Omega)|=|\mathfrak{t}_{\mu}(-\Omega)|, and so the
loss inEq.38is justΛμ​(Ω)=|𝔱μ​(Ω)|2\Lambda_{\mu}(\Omega)=|\mathfrak{t}_{\mu}(\Omega)|^{2}.

Optical SEC loss could be due to, for example, the anti-reflective
coatings of the optics in that cavity. In the coupled cavity model,
this loss is due to the fundamental mode quantum vacuum entering the
system at the portμa,r\mu_{\text{a,r}}ofFig.1orμa,r0\mu_{\text{a,r}}^{0}ofFig.2. The transmission of a
fundamental field entering the system here to the detected field read
out atμas,r0\mu_{\text{as,r}}^{0}is𝔱sec​(Ω)=Eas,r0Esec,i0=π​εs2​ℱs​1+i​Ω/γa1+i​Ω/γrse.\mathfrak{t}_{\text{sec}}(\Omega)=\frac{E_{\text{as,r}}^{0}}{E_{\text{sec,i}}^{0}}=\sqrt{\frac{\pi\varepsilon_{\text{s}}}{2\mathcal{F}_{\text{s}}}}\frac{1+\mathrm{i}\Omega/\gamma_{\text{a}}}{1+\mathrm{i}\Omega/\gamma_{\text{rse}}}.(41)

Such a field simply experiences the SEC RSE loop suppressionEq.9followed by the transmissionts≈2​π/ℱst_{\text{s}}\approx\sqrt{2\pi/\mathcal{F}_{\text{s}}}through the SEM. The resultingΛsec​(Ω)=|𝔱sec​(Ω)|2\Lambda_{\text{sec}}(\Omega)=|\mathfrak{t}_{\text{sec}}(\Omega)|^{2}for LIGO
A♯\sharpis shown as the dashed teal curve inFig.5forεs=\qty​500\varepsilon_{\text{s}}=\qty{500}{}.

The unsqueezed quantum vacuum responsible for mode mismatch loss are
the higher order modes of the squeezed fieldEas,iE_{\text{as,i}}injected
into the interferometer atμas,i\mu_{\text{as,i}}shown inFig.1which scatter into the fundamental mode when
that field encounters the thermal aberrations described by the surface𝐒i​j\mathbf{S}_{ij}and lens𝐋i​j\mathbf{L}_{ij}operators as discussed inSectionIII.2. In the two mode model ofSectionsIIand2, it is possible to
calculate the mismatch loss directly by propagating the single HOMEas,i1E_{\text{as,i}}^{1}entering the interferometer along with the
fundamental squeezed fieldEas,i0E_{\text{as,i}}^{0}to the fundamental modeEas,r0E_{\text{as,r}}^{0}which is measured. This HOM couples into the
fundamental mode of the SEC atμa,r0\mu_{\text{a,r}}^{0}throughts​𝔱a,h​(Ω)t_{\text{s}}\mathfrak{t}_{\text{a,h}}(\Omega)where𝔱a,h​(Ω)\mathfrak{t}_{\text{a,h}}(\Omega)is the
transmission of the HOM from the HOM SEC into the fundamental SEC
given byEq.23; equivalently, this
is the reflection of the HOM off of the mismatched arm cavity and the
subsequent scattering into the fundamental. This field then
experiences the fundamental’s SEC loop suppression, exactly as the
vacuum due to optical SEC loss does, to give a total transmission of
the HOM to the fundamental readout of𝔱rse,h​(Ω)\displaystyle\mathfrak{t}_{\text{rse,h}}(\Omega)=Eas,r0Eas,i1=Υ​b​1−rs1−β​rs​(α−1)+(1+α)​i​Ω/γa1+i​Ω/γrse\displaystyle=\frac{E_{\text{as,r}}^{0}}{E_{\text{as,i}}^{1}}=\sqrt{\Upsilon}b\frac{1-r_{\text{s}}}{1-\beta r_{\text{s}}}\frac{(\alpha-1)+(1+\alpha)\mathrm{i}\Omega/\gamma_{\text{a}}}{1+\mathrm{i}\Omega/\gamma_{\text{rse}}}(42a)={−i​π​Υℱs​11+i​Ω/γrseα=−1,β=−12​Υ1+i​Ω/γrseα=−1,β=+1−2​i​Υ​i​Ω/γrse1+i​Ω/γrseα=+1,β=−14​ℱs​Υπ​i​Ω/γrse1+i​Ω/γrseα=+1,β=+1\displaystyle=\begin{cases}\displaystyle\frac{-\mathrm{i}\pi\sqrt{\Upsilon}}{\mathcal{F}_{\text{s}}}\frac{1}{1+\mathrm{i}\Omega/\gamma_{\text{rse}}}&\alpha=-1,\beta=-1\\[10.00002pt]
\displaystyle\frac{2\sqrt{\Upsilon}}{1+\mathrm{i}\Omega/\gamma_{\text{rse}}}&\alpha=-1,\beta=+1\\[10.00002pt]
\displaystyle-2\mathrm{i}\sqrt{\Upsilon}\frac{\mathrm{i}\Omega/\gamma_{\text{rse}}}{1+\mathrm{i}\Omega/\gamma_{\text{rse}}}&\alpha=+1,\beta=-1\\[10.00002pt]
\displaystyle\frac{4\mathcal{F}_{\text{s}}\sqrt{\Upsilon}}{\pi}\frac{\mathrm{i}\Omega/\gamma_{\text{rse}}}{1+\mathrm{i}\Omega/\gamma_{\text{rse}}}&\alpha=+1,\beta=+1\end{cases}(42b)

whereβ=e2​i​ψs\beta=\mathrm{e}^{2\mathrm{i}\psi_{\text{s}}}and is+1+1for resonant HOMs and−1-1for
anti-resonant HOMs; andb=e−i​π​(1−β)/4b=\mathrm{e}^{-\mathrm{i}\pi(1-\beta)/4}and is 1 forβ=+1\beta=+1and−i-\mathrm{i}forβ=−1\beta=-1. The resulting loss due to mode mismatchΛmm​(Ω)=|𝔱rse,h​(Ω)|2\Lambda_{\text{mm}}(\Omega)=|\mathfrak{t}_{\text{rse,h}}(\Omega)|^{2}is detailed inTable1. It is shown inFig.5as the dashed blue
curve for A♯\sharpusing the exact model ofFigs.1andDwithΔ​w/w=\qty​5%\Delta w/w=\qty{5}{\%}andPrel=\qty​100P_{\text{rel}}=\qty{100}{}—calculated now usingEq.83since there are many HOMs which cannot be easily
propagated as inEq.42. The figure also shows the loss if
only the quadratic or only the higher order aberrations were present. The low-pass
dynamics of quadratic mismatch and high-pass dynamics of higher order aberrations are
evident in bothEqs.42and5. This is
explained in the model ofSectionIIby the different interference between
the HOM and the fundamental on reflection of the arm cavity leading to the HOM and
fundamental SECs being AC coupled through higher order aberrations while being DC
coupled through quadratic mismatch as explained byEq.24. Though the details are more complicated, the same
is true in the general case where the arm reflection is described byEqs.32and33, rather than byEqs.17,18and19, and
aberrations where𝐔r≈𝐔i−1\mathbf{U}_{\text{r}}\approx\mathbf{U}_{\text{i}}^{-1}tend to have interference leading to low-pass
dynamics while aberrations where𝐔r≈𝐔i\mathbf{U}_{\text{r}}\approx\mathbf{U}_{\text{i}}tend to have interference resulting in
high-pass dynamics.Figure 5:Direct mode mismatch loss forΔ​w/w=\qty​5%\Delta w/w=\qty{5}{\%}andPrel=\qty​100P_{\text{rel}}=\qty{100}{}along with both types of aberrations
separately for LIGO A♯\sharpusing the parameters ofTable2. The dashed lines do not include
radiation pressure and correspond to the discussion inSectionIV.1.1while the solid lines include
radiation pressure as discussed inSectionIV.1.2. The low-pass nature of quadratic
mismatch and high-pass nature of higher order aberrations is
evident, along with the fact that higher order modes can interfere
destructively to produce less loss.\qty500 of SEC loss is
also shown for comparison.

Higher order aberrations will usually be the largest source of
mismatch loss for the frequencies where mismatch loss is significant
due to their high-pass nature. However,Fig.5also
underscores the fact that the dynamics responsible for mode mismatch
loss are coherent: even though quadratic mismatch is sub-dominant by
several orders of magnitude at high frequencies, its presence stilldecreasesthe noise relative to the case where only higher
order aberrations are presentin the particular thermal state
and optical configuration shown in the figure. This is because in
the particular case ofFig.5, the mode content
interferes destructively in this particular thermo-optical system. This is a
generic, but not universal, occurrence and it is difficult to predict
what kind of interference will arise for a given thermal state and
optical configuration.

The Gouy phase and finesse of the SEC have a critical impact on the loss due to mode
mismatch within the coupled cavity. Since mode mismatch loss and optical SEC loss have
the same spectral shape above the arm cavity pole in most cases of interest, one way of
quantifying this impact is to find the amount of optical SEC loss which would be
equivalent to the amount of mismatch loss given a particular thermal stateandoptical configuration. This parameterization gives a measure of how much that particular
mode mismatch loss would contribute to the optical SEC loss if it were, incorrectly,
included in that loss budget as is often done. This is shown inFig.6for CE as a function of the SEC Gouy phase for three
different thermal states. As described in the last paragraph ofSectionIII.1, we imagine that the thermal actuators can perfectly correct
the thermal aberrations in some hot state with of order one watt of power absorbed in
the test mass coatings andPrelP_{\text{rel}}is the difference between the actual absorption and this perfect compensation. The Gouy phaseΨs\Psi_{\text{s}}shown in the figure is the one-way
Gouy phase of the SEC as calculated from the round-trip ABCD matrix of the cavity in
this perfectly matched state. This is the Gouy phase that is usually considered when
designing or diagnosing a detector, and it should be emphasized that figures like this
should be considered in the target hot state when being used in a detector design. In
contrast, the Gouy phase referred to in most of our discussion, denoted asψs\psi_{\text{s}}andβ=e2​i​ψs\beta=\mathrm{e}^{2\mathrm{i}\psi_{s}}, is the true one-way phase that a given mode accumulates.
In the absence of thermal aberrations and apertures,ψs=N​Ψs\psi_{\text{s}}=N\Psi_{\text{s}}for a mode
of orderNN. SeeAppendixBfor details about the general
relationship between these two notions of Gouy phase, but theΨs\Psi_{\text{s}}shown in the
figure is the metric most useful for choosing an optical design or characterizing a
detector whileψs\psi_{\text{s}}is the phase relevant for understanding the dynamics
responsible for the squeezing degradations.

Since the HOM vacuum experiences a different SEC than the fundamental,
it will be enhanced or suppressed to a varying degree depending on its
Gouy phaseψs\psi_{\text{s}}in the cavity. The round-trip phase for an
anti-resonant HOM (β=−1\beta=-1) is negative, and so it is suppressed by
the SEC dynamics. Such modes are said to be “healed” by the cavity. The
round-trip phase for a resonant HOM (β=+1\beta=+1) is positive so it is
enhanced in the SEC. Such modes are said to be “harmed” by the
cavity.Table1gives the mismatch loss for these two
cases for both quadratic and higher order aberrations. Mode harmed
loss is enhanced by a factor ofℱs\mathcal{F}_{\text{s}}relativeto SEC loss
and mode healed loss is suppressed by a factor ofℱs\mathcal{F}_{\text{s}}relativeto SEC loss. There will be a continuum of behavior
between exact anti-resonanceβ=−1\beta=-1and exact resonanceβ=+1\beta=+1, and thus between suppression byℱs\mathcal{F}_{\text{s}}or enhancement byℱs\mathcal{F}_{\text{s}}, but most HOMs will be more characteristic of anti-resonance and
thus suppression by the SEC to some degree.

Most of the peaks in the noise evident inFig.6are due to a single HOM becoming
resonant in the SEC (all HOMs are resonant at0​°and mode orders
which are integer multiples of four are resonant at45​°). These
resonances become both larger and narrower asℱs\mathcal{F}_{\text{s}}is increased. In
the absence of higher order aberrations and apertures, the eighth
order modes are resonant at22.5​°and the sixth order modes are
resonant at30​°; these frequencies are marked with vertical
dashed lines in the figure. As higher order aberrations are
introduced, the magnitude of the loss increases and the locations of
the resonances shift in a direction determined by the sign ofPrelP_{\text{rel}}. Note
that the Gouy phase of the cavityΨs\Psi_{\text{s}}is not changing here
because the quadratic part of the thermal lens is being held constant;
rather, the relationψs=N​Ψs\psi_{\text{s}}=N\Psi_{\text{s}}between the true phase that a
given HOM accumulates and the ABCD cavity Gouy phase is no longer
valid in the presence of higher order aberrations or
apertures. Varying the quadratic mismatch does change the cavity Gouy
phaseΨs\Psi_{\text{s}}, thus further shifting the resonances, in addition to
changing the overall magnitude of the loss due to the interference
described above. This underscores the necessity of controlling both
the quadratic and higher order aberrations in order to keep the SEC
Gouy phase constant, and thus prevent shifting HOMs from becoming
resonant.Figure 6:Mode mismatch loss for Cosmic Explorer varyingPrelP_{\text{rel}}while keepingΔ​w/w=\qty​5%\Delta w/w=\qty{5}{\%}as a function of
SEC Gouy phase. The vertical dashed lines mark the 8th order
resonance at22.5​°and the 6th order resonance at30​°in
the absence of thermal aberrations and apertures. The Gouy phase
is the one-way Gouy phase as computed from the round-trip ABCD
matrix of the SEC; seeAppendixB. RecallFig.3and the fact thatPrelP_{\text{rel}}can be
negative in our parameterization.

The addition of apertures in the cavity clips the HOMs and therefore
introduces extra loss for the HOMs which are clipped. Furthermore, the
higher order HOMs (the ones mainly responsible for the higher order
aberrations) will be clipped more than the lower order ones due to
their larger spatial extent. This increased loss will drastically
reduce the extent to which the modes are enhanced, or mode harmed, in the SEC and will
slightly increase the mode mismatch loss away from the resonance
peaks. Note that a change in the quadratic mismatch will be
accompanied by a change in the beam size and thus also the extent
to which the HOMs are clipped by the apertures.

Figure6does not illustrate the fact that
for some thermal states simply increasing the finesse may change the
high-pass vs. low-pass character of the mismatch loss. This may seem
counterintuitive since whether the mismatch has a low-pass or
high-pass character depends only on whether the mismatch is mainly due
to quadratic mismatch or to higher order aberrations and not on the
dynamics of the SEC
(cf.Eqs.24and42). However,
when there are many HOMs present, the HOMs mainly responsible for one
type of mismatch may be mode harmed while the HOMs mainly responsible
for the other type are mode healed. Thus, whether the total mismatch
loss is mostly high-pass or mostly low-pass can change as the finesse
is varied and the loss due to the two types of mismatch is variably
enhanced or suppressed. Similarly, the frequency dependence of the
mismatch can change as the Gouy phase, and hence which modes are
resonant, changes.

The desired instrument bandwidth is the main driver for the SEC finesse with a higher
finesse resulting in a wider bandwidth (cf.Eq.10). In order to keep a fixed
bandwidth, the finesse must scale asℱs∝ℱa​La\mathcal{F}_{\text{s}}\propto\mathcal{F}_{\text{a}}L_{\text{a}}, and so longer and higher
finesse arm cavities generally result in higher finesse SECs. Nevertheless, there is
some choice in the bandwidth, and this discussion has highlighted the fact that higher
finesse SECs are generally favorable for reducing loss due to mode mismatch as long as a
reasonable SEC Gouy phase is chosen along with the ability to control it in the presence
of realistic thermal aberrations. The case ofPrel=\qty​100P_{\text{rel}}=\qty{100}{}andΔ​w/w=\qty​5%\Delta w/w=\qty{5}{\%}shown inFig.6with a20​°Gouy phase
results in\qty30 equivalent SEC loss for Cosmic Explorer with the baseline SEM
transmission ofTs=\qty​2%T_{\text{s}}=\qty{2}{\%}(ℱs≈310\mathcal{F}_{\text{s}}\approx 310). For comparison, LIGO currently
hasTs=\qty​32.5%T_{\text{s}}=\qty{32.5}{\%}(ℱs≈18\mathcal{F}_{\text{s}}\approx 18) which results in\qty650
equivalent loss for the same thermal state and Gouy phase. A potential near-term change
to slightly broaden the bandwidth usingTs=\qty​20%T_{\text{s}}=\qty{20}{\%}(ℱs≈30\mathcal{F}_{\text{s}}\approx 30) results
in\qty370 equivalent loss, and a more wideband tuning usingTs=\qty​5%T_{\text{s}}=\qty{5}{\%}(ℱs≈125\mathcal{F}_{\text{s}}\approx 125), proposed for its increased sensitivity to high frequency
signals[27], would result in\qty90 equivalent SEC loss.

We also stress that the relatively low mismatch loss shown inFig.4and inFig.6for some ranges of Gouy phase—having an equivalent SEC loss that is a
small fraction of the\qty500 target—should not be taken as
an indication that mismatch loss will not be significant in a future
detector with a higher finesse SEC such as CE. In reality, the thermal
aberrations will not be as simple as the beam-heating of a test mass
optic shown inFig.3considered here, and
aberrations with more spatial structure may have significantly
more—or even occasionally less—loss than this analysis suggests
due to the details of the residual mode content, optical dynamics, and
the ensuing interference of the HOMs.

## IV.1.2Quantum radiation pressure noise due to mode mismatch

The direct loss coupling described above does not include quantum
radiation pressure noise (QRPN). Recall that amplitude quadrature
fluctuations are converted into phase quadrature fluctuations through
the optomechanical interaction between the light in the arm cavities
and the test mass mirrors. This correlates the upper and lower
sidebands so thatEas,r0​(Ω)/Esec,i0​(Ω)E^{0}_{\text{as,r}}(\Omega)/E^{0}_{\text{sec,i}}(\Omega)is no longer given byEq.41andEas,r0​(Ω)/Eas,i1​(Ω)E^{0}_{\text{as,r}}(\Omega)/E^{1}_{\text{as,i}}(\Omega)is no longer given byEq.42for the low frequencies where the
interferometer ponderomotively squeezes the vacuum and radiation
pressure is significant. Rather, the fieldEas,r0​(Ω)E^{0}_{\text{as,r}}(\Omega)in reflection of the coupled cavity is a function of both the upperEμ​(+Ω)E_{\mu}(+\Omega)and conjugate lowerEμ∗​(−Ω)E_{\mu}^{*}(-\Omega)sidebands. The necessary transfer functions are still computed as
described above except that the upper and lower sidebands must be
propagated together and the reflection from the ETM—in the exact
case illustrated inFig.1—or from the arm
cavity—in the phenomenological case illustrated inFig.2—must be replaced by matrices which mix
the sidebands.

In particular, in the analysis ofSectionII.2, the
perfectly matched arm reflection given byEq.4can be evaluated atΩ=0\Omega=0when
analyzing QRPN, and the following substitutions should be made𝔯a​0​(Ω)\displaystyle\mathfrak{r}_{\text{a}0}(\Omega)→[−1+i​𝒦a​(Ω)/2i​𝒦a​(Ω)/2−i​𝒦a​(Ω)/2−1−i​𝒦a​(Ω)/2]\displaystyle\to\begin{bmatrix}-1+\mathrm{i}\mathcal{K}_{\text{a}}(\Omega)/2&\mathrm{i}\mathcal{K}_{\text{a}}(\Omega)/2\\
-\mathrm{i}\mathcal{K}_{\text{a}}(\Omega)/2&-1-\mathrm{i}\mathcal{K}_{\text{a}}(\Omega)/2\end{bmatrix}(43a)𝔯a​1​(Ω)\displaystyle\mathfrak{r}_{\text{a}1}(\Omega)→[1001]\displaystyle\to\begin{bmatrix}1&0\\
0&1\end{bmatrix}(43b)

where the first column corresponds to the upper sideband and the
second to the conjugate lower. Here,𝒦a​(Ω)=2​ℱa/π×2​𝒦fm​(Ω)\mathcal{K}_{\text{a}}(\Omega)=2\mathcal{F}_{\text{a}}/\pi\times 2\mathcal{K}_{\text{fm}}(\Omega)is the optomechanical coupling
of the arm cavity where𝒦fm​(Ω)\mathcal{K}_{\text{fm}}(\Omega)is the optomechanical
coupling of a free mass given byEq.14. Since there is essentially no HOM
power in the arm cavity for the HOM vacuum to beat with, the HOM is
not ponderomotively squeezed on direct reflection from the arm and its
sidebands are not correlated by𝔯a​1​(Ω)\mathfrak{r}_{\text{a}1}(\Omega). However, the
HOM vacuum is still responsible for radiation pressure through the
process where it scatters into the fundamental mode before reflecting
off of the arm cavity. In the picture suggested byFig.2, the HOM and fundamental SECs are thus no
longer AC coupled through higher order aberrations in the presence of
radiation pressure.

The resulting QRPN due to mode mismatch loss fromEq.38isΓ​(Ω)​Λmm​(Ω)\displaystyle\Gamma(\Omega)\Lambda_{\text{mm}}(\Omega)=Υ​|𝒦rse​(Ω)|2​(1+α​rs1−β​rs)2\displaystyle=\Upsilon|\mathcal{K}_{\text{rse}}(\Omega)|^{2}\left(\frac{1+\alpha r_{\text{s}}}{1-\beta r_{\text{s}}}\right)^{2}(44a)=Υ​|𝒦rse​(Ω)|2×{(π2​ℱs)2α=β=−11α=−β(2​ℱsπ)2α=β=+1\displaystyle=\Upsilon|\mathcal{K}_{\text{rse}}(\Omega)|^{2}\times\begin{cases}\displaystyle\left(\!\frac{\pi}{2\mathcal{F}_{\text{s}}}\!\right)^{2}&\alpha=\beta=-1\\
1&\alpha=-\beta\\
\displaystyle\left(\!\frac{2\mathcal{F}_{\text{s}}}{\pi}\!\right)^{2}&\alpha=\beta=+1\end{cases}(44b)

which is to be compared to the QRPN due to optical SEC lossΓ​(Ω)​Λsec​(Ω)=ℱs​εs2​π​|𝒦rse​(Ω)|2.\Gamma(\Omega)\Lambda_{\text{sec}}(\Omega)=\frac{\mathcal{F}_{\text{s}}\varepsilon_{\text{s}}}{2\pi}\,|\mathcal{K}_{\text{rse}}(\Omega)|^{2}.(45)

These losses are shown inFig.5for LIGO A♯\sharpas the solid lines. The dashed lines inFig.5correspond to the analysis ofSectionIV.1.1where
there is no radiation pressure. It is also useful to instead look atΛmm​(Ω)\Lambda_{\text{mm}}(\Omega)including QRPN but with the quantum noise
gainΓ​(Ω)∝|𝒦rse​(Ω)|2∝Pa2/M2​Ω4\Gamma(\Omega)\propto|\mathcal{K}_{\text{rse}}(\Omega)|^{2}\propto P_{\text{a}}^{2}/M^{2}\Omega^{4}factored out as is shown inFig.10.

Note that while the shot noise and radiation pressure due to quantum
vacuum entering the system along the injection path are equal at the
RSE SQL frequencyΩsqlrse\Omega_{\text{sql}}^{\text{rse}}given byEq.16, shot noise and radiation pressure due to
the vacuum entering inside the coupled cavity through either higher
order aberrations or optical SEC loss are equal at the generally
higher frequencyΩint6=(ℱa​γa/π)2×(Ωsqlfm)4=(c/4​La)2×(Ωsqlfm)4\Omega_{\text{int}}^{6}=(\mathcal{F}_{\text{a}}\gamma_{\text{a}}/\pi)^{2}\times(\Omega_{\text{sql}}^{\text{fm}})^{4}=(c/4L_{\text{a}})^{2}\times(\Omega_{\text{sql}}^{\text{fm}})^{4}as is
evident inFig.4.

## IV.1.3Strain-referred loss

We have so far discussed the direct coupling of optical SEC loss and
mode mismatch loss due to HOM vacuum scattering into the fundamental
mode of the field which is ultimately detected. This is shown inFig.5and is the transmission of the unsqueezed
vacuum fields entering the system at the nodesμas,i\mu_{\text{as,i}}andμa,r\mu_{\text{a,r}}inFig.1to the fundamentalEas,r0E_{\text{as,r}}^{0}. However, the quantity that is directly relevant for
gravitational wave detectors is the strain- or signal-referred loss
which is shown inFig.4. This is the effective
loss as it would appear if it entered the system in the same way that
a gravitational wave strain signal enters; inFig.1a strain signal excites the optical field at
the nodeμx\mu_{x}. Since the optomechanical
plantEq.13, also known as the sensing
function[2], describes the propagation of a
gravitational wave signal to the readout, the strain-referred loss is
given by dividing the direct coupling by the optomechanical plant in
order to “calibrate” the noise into an equivalent displacement noise
and then dividing by the arm lengthLaL_{\text{a}}to give an equivalent
strain noise.888This is not precisely strain for detectors with
long arms such as CE because displacement and strain do not differ
simply by a factor of arm length for frequencies comparable to or
larger than the FSR. Rather, they have an additional frequency and
source location dependent
correction[47,23]. We only show displacement
noise in this paper to avoid this complication. Simply dividing byLaL_{\text{a}}, however, correctly captures the scaling of the noises with
arm length which is relevant for a strain measurement.The amplitude
spectral density of this strain-referred noise is thenSh​h1/2​(Ω)=1La​Γ​(Ω)​Λ​(Ω)|C​(Ω)|2​ℏ​ω02,S_{hh}^{1/2}(\Omega)=\frac{1}{L_{\text{a}}}\sqrt{\frac{\Gamma(\Omega)\Lambda(\Omega)}{|C(\Omega)|^{2}}\frac{\hbar\omega_{0}}{2}},(46)

whereΛ​(Ω)\Lambda(\Omega)is the appropriate direct coupling, eitherΛmm​(Ω)\Lambda_{\text{mm}}(\Omega)orΛsec​(Ω)\Lambda_{\text{sec}}(\Omega)in this
case. Theℏ​ω0/2\hbar\omega_{0}/2is the half-quanta of vacuum energy which
must be propagated through the direct couplingΛ​(Ω)\Lambda(\Omega)in
order to produce the quantum noise measured on a photodetector in
physical units.

strain-referred SEC loss and mode mismatch loss are not affected by
the fundamental mode SEC because they experience the dynamics of this
cavity in exactly the same way as a strain signal does once the
relevant fields enter the cavity (at the nodeμa,r0\mu_{\text{a,r}}^{0}ofFig.2). Mathematically, the optomechanical plant
(Eqs.12and13) and the relevant
vacuum transmissions to the readout
(Eqs.41and42) are|C​(Ω)|22​k2​Pa=|𝔱rse​(Ω)|2\displaystyle\frac{|C(\Omega)|^{2}}{2k^{2}P_{\text{a}}}=|\mathfrak{t}_{\text{rse}}(\Omega)|^{2}=|ts​Hs​(Ω)×1−Υ​𝔱a​(Ω)|2\displaystyle=|t_{\text{s}}H_{\text{s}}(\Omega)\!\times\!\sqrt{1-\Upsilon}\,\mathfrak{t}_{\text{a}}(\Omega)|^{2}(47)|Eas,r0Eas,i1|2=|𝔱rse,h​(Ω)|2\displaystyle\left|\frac{E_{\text{as,r}}^{0}}{E_{\text{as,i}}^{1}}\right|^{2}=|\mathfrak{t}_{\text{rse,h}}(\Omega)|^{2}=|ts​Hs​(Ω)×ts​𝔱a,h​(Ω)|2\displaystyle=|t_{\text{s}}H_{\text{s}}(\Omega)\!\times\!t_{\text{s}}\mathfrak{t}_{\text{a,h}}(\Omega)|^{2}(48)|Eas,r0Esec0|2=|𝔱sec​(Ω)|2\displaystyle\left|\frac{E_{\text{as,r}}^{0}}{E_{\text{sec}}^{0}}\right|^{2}=|\mathfrak{t}_{\text{sec}}(\Omega)|^{2}=|ts​Hs​(Ω)×εs|2.\displaystyle=|t_{\text{s}}H_{\text{s}}(\Omega)\!\times\!\sqrt{\varepsilon_{\text{s}}}|^{2}.(49)

Therefore, for these internal losses and mismatches, the SEC dynamics
encoded in the fundamental’s loop suppressionHs​(Ω)H_{\text{s}}(\Omega)cancels,
the only difference is how they enter the SEC, and they therefore
differ only by thearmtransmission𝔱a​(Ω)\mathfrak{t}_{\text{a}}(\Omega). This
is in contrast to all of the other losses generated by quantum vacuum
entering the system outside the coupled cavity shown inFig.4which are modified by thecoupled
cavitytransmission𝔱cc​(Ω)\mathfrak{t}_{\text{cc}}(\Omega)once calibrated into
an equivalent strain. The effects of the SEC are imprinted on the
mismatch loss only through the transmission of the HOMs from the HOM
SEC—where they experience the HOM SEC loop suppression—into the
fundamental SEC given byEq.23.

This strain-referred loss is given inTable1for all
of the noises discussed above. Several facts are of particular
interest:
- •

Shot noise due to HOA and SEC loss above the arm cavity pole
rise likeΩ\Omegaand are independent of arm length. Therefore
these noises will become relatively more important for detectors
with long arms since most other noises fall with some power of arm
length.
- •

Shot noise due to HOA and SEC loss above the arm cavity pole are
enhanced by a factor ofℱa\sqrt{\mathcal{F}_{\text{a}}}.
- •

Shot noise due to HOMs that are mode healed is suppressed by a
factor ofℱs\sqrt{\mathcal{F}_{\text{s}}}and shot noise due to HOMs that are mode
harmed is enhanced by a factor ofℱs\sqrt{\mathcal{F}_{\text{s}}}.
- •

Mode harmed HOA QRPN is enhanced by a factor ofℱs\sqrt{\mathcal{F}_{\text{s}}},
quadratic healed QRPN is suppressed by a factor ofℱs3/2\mathcal{F}_{\text{s}}^{3/2}, and
both quadratic harmed and HOA healed QRPN are suppressed by a factor
ofℱs\sqrt{\mathcal{F}_{\text{s}}}.
- •

All sources of QRPN are enhanced by a factor ofℱa\sqrt{\mathcal{F}_{\text{a}}}and are inversely proportional to arm length.
- •

Optical SEC loss is independent of SEC finesse. It is more
important for CE because of its independence with arm length. It is
more important for other detectors which happen to have large SEC
finesses because those detectors also have large arm finesses.

Note that while the shot noise behavior below the arm cavity pole is interesting in
understanding the optical dynamics, it is ultimately not relevant to a gravitational
wave detector because the QRPN contributions will be dominant at these low frequencies.

Finally, we note that the possibility of “tuning” the detector to
have extra sensitivity at frequencies relevant to post-merger neutron
star physics at the expense of broadband sensitivity is sometimes
discussed[50,38,6]. This is
achieved by making the SEC poleγs\gamma_{\text{s}}sufficiently small that the
single pole approximation for the RSE transmissionEq.12breaks down. In this case, the pole atγrse\gamma_{\text{rse}}in the SEC loop suppressionEq.9is replaced by a complex pair of
poles resulting in an optical plant with a resonant gain of bandwidthγs\gamma_{\text{s}}around these poles at a frequency of approximatelyγrse​γs\sqrt{\gamma_{\text{rse}}\gamma_{\text{s}}}. This thus results in a resonant dip in several
noise sources when they are calibrated into an equivalent
strain. However, as described above, the internal SEC loss and mode
mismatch loss are not affected by the dynamics of the SEC encoded in
the loop suppression and thus do not gain the benefit of a resonant
dip when calibrated into strain. This is one of several reasons why
attempting such a tuning is of limited utility in the presence of SEC
loss or internal mode mismatch loss.

## IV.2Degradations around a higher order mode arm cavity resonance

When a higher order mode becomes resonant in the arm cavities, the
behavior of the HOM and the fundamental is swapped: the reflection off
of the arm for the fundamental is𝔯a​0​(Ω)=+1\mathfrak{r}_{a0}(\Omega)=+1since it is
non-resonant, and the reflection off of the arm for the HOM𝔯a​1​(Ω)\mathfrak{r}_{a1}(\Omega)is given byEq.4. Furthermore, the arm cavities are
detuned for the HOM due to the extra Gouy phase accumulated relative
to the fundamental so thatδ​ωa≠0\delta\omega_{\text{a}}\neq 0inEq.4.

The squeezing degradations around a HOM arm cavity resonance have many
parallels to those due to the filter cavity used to generate the
frequency-dependent squeezed state rotation needed for broadband
quantum noise reduction. The required rotation is imparted to a
frequency-independent squeezed state by reflecting it off of the
filter cavity which is itself a cavity detuned for the
fundamental[35,39,58,26]. The
arm cavities therefore act like filter cavities for the HOM due to the
same principle, and the HOM will experience all of the degradations
that the fundamental experiences due to the filter
cavity[40,36]—including an (unwanted)
rotation.999This is similar to the effect studied in
Ref.[54]where HOMs become resonant in the filter cavity
itself. However, the effect described there should not be significant
in practice because it relies on optical parameters chosen to be
problematic.These degradations will then couple into the fundamental
through the mode mismatch.

These dynamics around a higher order mode resonance at a frequencyδ​ωa\delta\omega_{\text{a}}result in a reflection for the fundamental mode off
of the coupled cavity of𝔯rse​(Ω)=−1−i​Ω/γs1+i​Ω/γs+gs​Υ(1+i​Ω/γs)2​(1−α)+(1+α)​i​(Ω−δ​ωa)/γa1+i​(Ω−δ​ωa)/γcc\mathfrak{r}_{\text{rse}}(\Omega)=-\frac{1-\mathrm{i}\Omega/\gamma_{\text{s}}}{1+\mathrm{i}\Omega/\gamma_{\text{s}}}\\
+\frac{g_{\text{s}}\Upsilon}{(1+\mathrm{i}\Omega/\gamma_{\text{s}})^{2}}\frac{(1-\alpha)+(1+\alpha)\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{a}}}{1+\mathrm{i}(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{cc}}}(50)

where the relevant coupled cavity pole isγcc=1+β​rs1−β​rs​γa={γsrβ=−1γrseβ=+1\gamma_{\text{cc}}=\frac{1+\beta r_{\text{s}}}{1-\beta r_{\text{s}}}\gamma_{\text{a}}=\begin{cases}\gamma_{\text{sr}}&\beta=-1\\
\gamma_{\text{rse}}&\beta=+1\end{cases}(51)

and wheregs=ts2(1−rs)2​1+α​β​rs1+β​rs={1α=−1,β=+1(2​ℱsπ)2α=−1,β=−12​ℱsπα=+1,β=±1g_{\text{s}}=\frac{t_{\text{s}}^{2}}{(1-r_{\text{s}})^{2}}\frac{1+\alpha\beta r_{\text{s}}}{1+\beta r_{\text{s}}}=\begin{cases}1&\alpha=-1,\beta=+1\\[5.0pt]
\displaystyle\left(\!\frac{2\mathcal{F}_{\text{s}}}{\pi}\!\right)^{2}&\alpha=-1,\beta=-1\\[10.00002pt]
\displaystyle\frac{2\mathcal{F}_{\text{s}}}{\pi}&\alpha=+1,\beta=\pm 1\end{cases}(52)

The SEC is tuned to operate in RSE for the fundamental. A HOM
anti-resonant in the SEC with a Gouy phaseψs=π/2\psi_{\text{s}}=\pi/2(a mode
“healed” HOM) experiences an extra round-tripπ\piphase shift in
the SEC relative to the fundamental, and therefore a total roundtrip
phase of0near a resonance. An anti-resonant HOM is therefore
characterized by the SR coupled cavity pole rather than the RSE
pole. A HOM resonant in the SEC with a Gouy phase ofψs=0\psi_{\text{s}}=0(a
mode “harmed” HOM) experiences the same total roundtrip phase as the
fundamental and is therefore characterized by the same RSE coupled
cavity pole. Since most HOMs will be more characteristic of an
anti-resonant field in the SEC, especially in the presence of
apertures as discussed below, these degradations will generally be
narrow with a width characteristic of the SR pole—thus getting
narrower as the SEC finesse and RSE pole get larger
(cf.Eq.10).

InSectionIV.2.1we discuss the squeezing degradations
which result from the dynamics described byEq.50; inSectionIV.2.2we discuss how the locations
of these resonances are determined; and inSectionIV.2.3we
discuss how these degradations could be monitored in order to
characterize the detectors and as an aid in tuning them to minimize
mode mismatch.

## IV.2.1Rotation, loss, and dephasing

As can be seen fromFig.4, the most prominent
degradation around a higher order mode resonance for reasonable values
of mismatch for Cosmic Explorer is due to the anti-squeezing caused by
the squeezed state rotation. For more extreme values of mismatch, the
dephasing can become even more significant but can no longer be
described by the approximate expressions of this section. Either the
upper or the lower HOM sideband will be resonant in the arm and
experience theπ\piphase shift on reflection of a resonant cavity,
and the squeezed state will therefore rotate within the band where
this resonance occurs. This bandwidth will be characterized by the
appropriate coupled cavity poleEq.51. The
rotation thus generated by the reflectionEq.50isθ​(Ω)=−gs​Υ​(Ω−δ​ωa)/γcc1+(Ω−δ​ωa)2/γcc2.\theta(\Omega)=-g_{\text{s}}\Upsilon\frac{(\Omega-\delta\omega_{\text{a}})/\gamma_{\text{cc}}}{1+(\Omega-\delta\omega_{\text{a}})^{2}/\gamma_{\text{cc}}^{2}}.(53)

This rotation is enhanced by a factor ofgs/γccg_{\text{s}}/\gamma_{\text{cc}}which is
summarized inTable1. The most significant rotation
is due to an anti-resonant HOM excited by a quadratic
mismatch.Figure7shows this rotation
for four slightly different thermal states in LIGO as is discussed
further inSectionIV.2.3.Figure 7:Squeezed state rotation around the first HOM arm cavity resonance in
A♯\sharpwith a SEM transmissivity ofTs=\qty​20%T_{\text{s}}=\qty{20}{\%}for
slightly different thermal states. This exact behavior is well
accounted for byEq.53. The RSE pole in
this case is\qty750 and the SR pole is\qty2. Fits
to these curves give widths of between 6 and\qty10 showing
that the dynamics are characteristic of those of a signal recycled
interferometer for the fundamental mode. Measuring this rotation with
an audio diagnostic field[28]may prove useful in
characterizing the detectors and optimizing their configurations
as discussed inSectionIV.2.3.

Next consider the loss which is given byΛ​(Ω)={2​gs​Υ1+(Ω−δ​ωa)2/γcc2α=−12​gs​Υ​[1+(Ω−δ​ωa)2/γcc21+(Ω−δ​ωa)2/γcc2]α=+1\Lambda(\Omega)=\begin{cases}\displaystyle\frac{2g_{\text{s}}\Upsilon}{1+(\Omega-\delta\omega_{\text{a}})^{2}/\gamma_{\text{cc}}^{2}}&\alpha=-1\\[8.61108pt]
\displaystyle 2g_{\text{s}}\Upsilon\left[1+\frac{(\Omega-\delta\omega_{\text{a}})^{2}/\gamma_{\text{cc}}^{2}}{1+(\Omega-\delta\omega_{\text{a}})^{2}/\gamma_{\text{cc}}^{2}}\right]&\alpha=+1\end{cases}(54)

Due to its low-pass dynamics, for quadratic mismatch only one of the sidebands will be
transmitted into the SEC and this transmission diminishes for frequencies above the
cavity pole. This leads to a Lorentzian loss. On the other hand, due to its high-pass
dynamics, for higher order aberrations one of the sidebands is always maximally
transmitted into the SEC and always contributes to the loss. When the other sideband is
resonant in the arm, it is not transmitted into the SEC and does not contribute. This
leads to an inverse Lorentzian-like loss with a dip reaching half the maximum on exact
resonance.

Finally, consider the dephasing. In the case of quadratic mismatch, the
single sideband which is transmitted into the SEC on resonance is
attenuated above the cavity pole. For higher order aberrations, one of
the sidebands is always maximally transmitted into the SEC and the
second only significantly couples into the SEC above the cavity
pole. In both cases the sidebands are maximally imbalanced on
resonance, and this leads to the following Lorentzian dephasing profileΞ​(Ω)=gs2​Υ2[1+(Ω−δ​ωa)2/γcc2]2.\Xi(\Omega)=\frac{g_{\text{s}}^{2}\Upsilon^{2}}{\left[1+(\Omega-\delta\omega_{\text{a}})^{2}/\gamma_{\text{cc}}^{2}\right]^{2}}.(55)

For the particular thermal state shown inFig.4, this dephasing adds approximately\qty520\milliof phase noise around the most prominent HOM
resonance at about\qty3.

As we have seen from the fundamental dynamics of the HOMs summarized
inTable1, the quadratic mismatch will produce the
most significant squeezing degradations around HOM arm cavity resonances. This
will be even more true in practice with the addition of apertures in
the arms. The quadratic mismatch mostly excites second order HOMs
while the higher order aberrations excite mostly higher order HOMs
with larger spatial extent. The HOMs excited by higher order
aberrations are therefore clipped more than those excited by quadratic
mismatch making them even less important than the scalings ofTable1suggest. However, just as quadratic mismatch
affects the broadband loss despite being significantly subdominant to
the effects of the higher order aberrations as discussed inSectionIV.1, the higher order aberrations affect the
magnitude of the degradations discussed here which are mainly due to
quadratic mismatch due to the interference between the HOMs which are
responsible.

## IV.2.2Placement of higher order mode resonances

In the absence of thermal aberrations and apertures, a higher order mode of orderNNwill become resonant in the arm cavities around frequencies[49]δ​ωa\displaystyle\delta\omega_{\text{a}}=|p​N​ωtms−q​ωfsr|=ωfsr​|p​N​Ψaπ−q|\displaystyle=\left|pN\omega_{\text{tms}}-q\omega_{\text{fsr}}\right|=\omega_{\text{fsr}}\left|pN\frac{\Psi_{\text{a}}}{\pi}-q\right|(56a)ωtms\displaystyle\omega_{\text{tms}}=ωfsr​Ψaπ,ωfsr=π​cLa\displaystyle=\omega_{\text{fsr}}\frac{\Psi_{\text{a}}}{\pi},\qquad\omega_{\text{fsr}}=\frac{\pi c}{L_{\text{a}}}(56b)

for integersppandqqwhereωfsr\omega_{\text{fsr}}is the free
spectral range (FSR),ωtms\omega_{\text{tms}}is the transverse mode
spacing (TMS), andΨa\Psi_{\text{a}}is the one-way arm cavity Gouy
phase. The FSR is the difference in frequencies between resonances of
the fundamental mode, and the TMS is the frequency difference between
HOM resonances. In the context of gravitational wave detectors it is
desirable to have a large TMS so that there are fewer HOM resonances
within the detection band. This is a more significant problem for
detectors with long arms, like CE, since the TMS is inversely
proportional to arm length.

The arm cavity Gouy phase, and thus the HOM locations, is determined
by the geometry of the arm cavity, i.e. the cavitygg-factors or,
equivalently, the radii of curvature of the input and end test masses
asΨa=arccos⁡(sgn⁡gi​gi​ge),gi=1−LaRi.\Psi_{\text{a}}=\arccos\left(\operatorname{sgn}g_{\text{i}}\,\sqrt{g_{\text{i}}g_{\text{e}}}\right),\qquad g_{i}=1-\frac{L_{\text{a}}}{R_{i}}.(57)

In reality, the presence of apertures in the arms will slightly shift
the locations of these resonancesδ​ωa\delta\omega_{\text{a}}: the one-way Gouy phase
accumulated by a HOM of orderNNis no longer preciselyψa=N​Ψa\psi_{\text{a}}=N\Psi_{\text{a}}in the presence of apertures or thermal aberrations as
explained inAppendixB. Furthermore, the
dynamics of the SEC for HOMs not exactly resonant or anti-resonant in
that cavity will slightly shift the frequencies at which the
degradations will occur from the exact arm resonances. These details
must be accounted for when characterizing an existing detector or
designing a new one, however the dominant factor determining where the
degradations will occur is, by far, the arm cavity
geometry.Figure8show how the arm cavity
geometry determines the resonances in CE.Figure 8:Higher order mode resonances in CE for two different arm
cavity geometries with\qty​70​∅\qty{70}{}\penalty 10000\ \varnothingarm cavity
apertures. Only second order mode resonances are significant after
the addition of apertures. The free spectral range is\qty3750 and the transverse mode spacing is\qty1460
for thew=\qty​12w=\qty{12}{}case and\qty1110 for thew=\qty​13w=\qty{13}{}case. In both cases, the first peak is due to
the second order resonance in the first FSR, the second peak is
due to the same resonance in the zeroth FSR, and the third peak is
due to the resonance in the second FSR.

The locations of these resonances cannot be arbitrarily placed
however. The arm cavity geometry also determines the size of the beams
on the test mass mirrors as[49]wi​(e)2=λ​Laπ​ge​(i)gi​(e)​(1−gi​ge),w^{2}_{\text{i}(\text{e})}=\frac{\lambda L_{\text{a}}}{\pi}\sqrt{\frac{g_{\text{e}(\text{i})}}{g_{\text{i}(\text{e})}(1-g_{\text{i}}g_{\text{e}})}},(58)

and so the location of the HOM resonances can equivalently be thought of as being
determined by the size of the beams on the test masses. There are other constraints on
thegg-factors and beam sizes which must be satisfied or implications to be considered
that are too numerous to discuss here but which therefore limit where these resonances
can be placed. Minimizing the impact of these squeezing degradations will therefore be
just one of many considerations that must be made when designing the arm cavities of a
new detector.

Finally we note that a real gravitational wave detector has two arms
which do not have precisely the same geometry for a variety of
technical reasons and which will furthermore be slightly
astigmatic. Astigmatism in the SEC will also slightly alter their
behavior. There will therefore be four closely spaced peaks
responsible for these squeezing degradations near each HOM resonance
which will nonetheless largely behave like the single peak described
here.

## IV.2.3Use in tuning and characterizing detectors

It may be possible to take advantage of these squeezed state degradations
around a HOM arm cavity resonance by carefully measuring them in order to
characterize the detector state and tune the interferometer for better
mode matching. It is possible to measure the McCuller metrics directly
using an audio diagnostic field (ADF) injected into the system along
with the squeezed state[28]. HOM resonances outside
the detection band provide as much information as those within the
band, and this technique can thus be useful in both LIGO and CE.
It is also important to note that the ADF is a transfer function
measurement and does not require measuring noise spectra or
distinguishing quantum from classical noise as is often done to
characterize detectors and to tune them to maximize the broadband
quantum noise reduction.

Figure7shows the squeezed state rotation around the
first HOM arm cavity resonance in LIGO for four different thermal states and illustrates
the kind of information that could, in principle, be gained by monitoring this feature.
The blue curve shows a nominal case withΔ​w/w=\qty​5%\Delta w/w=\qty{5}{\%}andPrel=\qty​100P_{\text{rel}}=\qty{100}{}relative absorption. The orange curve shows the same state with the quadratic mismatch
increased toΔ​w/w=\qty​7%\Delta w/w=\qty{7}{\%}. The amplitude of the rotation is simply increased
because this feature is predominantly due to the quadratic mismatch as discussed above.
The red curve shows the original state with the relative absorbed power decreased toPrel=\qty​90P_{\text{rel}}=\qty{90}{}keeping the quadratic mismatch constant. In this case the
amplitude is constant because it is largely unaffected by higher order aberrations. The
location of the maximum rotation is slightly shifted, however, because the higher order
aberrations slightly shift the arm cavity Gouy phase away from the frequency determined
by the arm cavity geometry alone (Eqs.56and57). Finally, the
teal curve shows the same thermal state but with an SEC Gouy phase ofΨs=25​°\Psi_{\text{s}}=$$rather than theΨs=20​°\Psi_{\text{s}}=$$for the other three cases. In
this case the amplitude is increased because the HOM dynamics are enhanced in the SEC to
a slightly greater degree at this Gouy phase. The peak is also shifted because the SEC
Gouy phase also slightly shifts the peak rotation away from the arm HOM resonance
determined by the arm cavity geometry alone. The measurements of
Ref.[28]show that it is in principle possible to measure changes of
this magnitude with the ADF.

As inFig.6, the SEC Gouy phase has been artificially held
constant inFig.7; seeAppendixBfor details. In reality, the thermal lensing in the ITM substrates would induce both
higher order aberrations and change the Gouy phase, so the effects are not completely
orthogonal. (The actual detectors do have actuators capable of independently changing
only the SEC Gouy phase without affecting any of the test mass thermal aberrations,
however.) Nevertheless, it is an especially sensitive indicator of quadratic mismatch
and, especially when combined with other independent measurements, this illustrates how
monitoring the squeezing degradations around a HOM arm cavity resonance can be used as a
guide in how to tune the thermal actuators to improve the internal mode matching.

Finally, as is discussed inSectionIV.4, the
inevitable mode mismatch with the external optical cavities not
studied here will produce degradations that are in many ways
indistinguishable from the degradations due to the internal quadratic
mismatch and higher order aberrations discussed here. Crucially, the
degradations around a HOM resonance are only caused by internal
mismatch, and so monitoring them can be an important tool in
disentangling what mismatch is most responsible for the observed
degradations in order to know where to focus on improving them.

## IV.3Broadband rotation

Detuning the SEC by an angleϕs\phi_{\text{s}}induces a broadband squeezed
state rotation of101010The approximate expression ofEq.59describes the same rotation as does Eq. (69) of
Ref.[40]but is consistent with the exact model ofSectionII.2over a wider parameter regime. Note that
in the notation of Ref.[40],γrse\gamma_{\text{rse}}isγA\gamma_{\text{A}},γs\gamma_{\text{s}}isγS\gamma_{\text{S}}, andℱs=π/us\mathcal{F}_{\text{s}}=\pi/u_{\text{s}}.θ​(Ω)=−4​ℱsπ​ϕs​(Ω/γrse)2(Ω/γrse)2+(1−Ω2/γrse​γs)2.\theta(\Omega)=-\frac{4\mathcal{F}_{\text{s}}}{\pi}\frac{\phi_{\text{s}}\,(\Omega/\gamma_{\text{rse}})^{2}}{(\Omega/\gamma_{\text{rse}})^{2}+(1-\Omega^{2}/\gamma_{\text{rse}}\gamma_{\text{s}})^{2}}.(59)

Such a rotation is illustrated inFig.9. The optical
response to the detuningϕs\phi_{\text{s}}produces no rotation at low
frequencies below the RSE poleγrse\gamma_{\text{rse}}, a rotation reachingΔ​θs≃4​ℱs/π×ϕs\Delta\theta_{\text{s}}\simeq 4\mathcal{F}_{\text{s}}/\pi\times\phi_{\text{s}}in the mid-band
between the RSE pole and the SEC poleγs\gamma_{\text{s}}, and a rotation back to
zero at high frequencies above the SEC pole.

One way that such a rotation can arise is by detuning the length of
the SEC byΔ​Ls\Delta L_{\text{s}}to introduce an extra phase ofϕs=k​Δ​Ls\phi_{\text{s}}=k\Delta L_{\text{s}}to the
fundamental[40]. However, even if there is no detuning
of the SEC length, the cavity will still be detuned for a HOM which is
not exactly resonant or anti-resonant due to its extra Gouy phase. The
cavity will then become detuned for the fundamental, not by detuning
the length, but through the coupling with the HOM introduced by a mode
mismatch. Theϕs\phi_{\text{s}}introduced by a higher order aberration for a
HOM near resonance (ψs=δ​ψs\psi_{\text{s}}=\delta\psi_{\text{s}}) or anti-resonance
(ψs=π/2+δ​ψs\psi_{\text{s}}=\pi/2+\delta\psi_{\text{s}}) isϕmm≈{δ​ψs​Υπ2/4​ℱs2+(δ​ψs)2β≈+1+2​i​δ​ψs−δ​ψs​Υβ≈−1−2​i​δ​ψs.\phi_{\text{mm}}\approx\begin{cases}\displaystyle\frac{\delta\psi_{\text{s}}\Upsilon}{\pi^{2}/4\mathcal{F}_{\text{s}}^{2}+(\delta\psi_{\text{s}})^{2}}&\beta\approx+1+2\mathrm{i}\delta\psi_{\text{s}}\\[10.00002pt]
\displaystyle-\delta\psi_{\text{s}}\Upsilon&\beta\approx-1-2\mathrm{i}\delta\psi_{\text{s}}\end{cases}.(60)

The detuning due to a nearly resonant HOM is therefore enhanced by the
SEC finesse with the maximumℱs​Υ/π\mathcal{F}_{\text{s}}\Upsilon/\pioccurring at a Gouy
phase ofπ/2​ℱs\pi/2\mathcal{F}_{\text{s}}, while the detuning due to a nearly anti-resonant
HOM is independent of finesse. Quadratic mismatch does not produce
any significant broadband rotation due to its low-pass nature.

The rotation described byEq.59is due solely to the
optical response of a field reflecting off of a detuned coupled
cavity. There are two more related but distinct effects due to such a
detuning that arise under the influence of radiation pressure. First,
detuning the SEC by introducing a length offsetΔ​Ls\Delta L_{\text{s}}will
also produce an optical spring whereby the dynamics of the mirrors
themselves are modified so that the light provides a restoring (or
anti-restoring) force between the mirrors[15,16]. This
will modify the optomechanical plantC​(Ω)C(\Omega)Eq.13—as well as the test mass
susceptibility. (There will also be an associated optical resonance
introduced in the plant at high frequencies because the system is now
not exactly operating in RSE and so the signal sidebands have become
slightly imbalanced.) The same changes to the optomechanical plant
will also occur for a detuning caused by a mode mismatch such asEq.60. Since this is a change only to the
optical plant it will only affect the strain-referred noise
(cf.SectionIV.1.3).

The second effect is that the optomechanical coupling𝒦rse\mathcal{K}_{\text{rse}}will be modified by an SEC detuning introduced
through any mechanism. The SQL frequency will therefore be slightly
shifted and the squeezed state rotation due to the interferometerθifo​(Ω)\theta_{\text{ifo}}(\Omega)will be slightly altered. The filter
cavity is tuned to produce a rotation ofθfc​(Ω)\theta_{\text{fc}}(\Omega)to
cancel the rotation caused by the ponderomotive squeezing of the
interferometerθifo​(Ω)\theta_{\text{ifo}}(\Omega)by targeting a specific SQL
frequency. With aθifo​(Ω)\theta_{\text{ifo}}(\Omega)altered by a SEC
detuning, the rotationθfc​(Ω)\theta_{\text{fc}}(\Omega)provided by the
filter cavity no longer perfectly compensates the ponderomotive
squeezing of the interferometer and there will be a residual total
“misrotation” of the squeezed stateθ​(Ω)=θfc​(Ω)+θifo​(Ω)\theta(\Omega)=\theta_{\text{fc}}(\Omega)+\theta_{\text{ifo}}(\Omega)around the SQL
frequency. This only affects the squeezed state rotationθ​(Ω)\theta(\Omega)and does not modify the optomechanical plantC​(Ω)C(\Omega)or the dynamics of the mirrors. This difference is
important when considering the interactions between the internal
mismatch discussed here and the external mismatch as discussed inSectionIV.4.Figure 9:Broadband rotation of the squeezed state. The peaks are due to the HOM arm cavity resonances discussed inSectionIV.2superimposed on the broadband rotation described byEq.59. The dashed lines
do not include radiation pressure and thus only illustrate the
purely optical rotation described byEq.59. The
solid lines include radiation pressure and thus also include the
rotation due to the shifted SQL frequency.
The rotation cannot be completely flattened between the SQL and RSE pole by introducing a
length detuningΔ​Ls\Delta L_{\text{s}}because, independent of any
mismatch or length detuning, two filter cavities are required to
perfectly compensate the rotation due to the ponderomotive
squeezing of the interferometer[35].

Both the rotation of the squeezed stateθ​(Ω)\theta(\Omega)—due both to
the optical rotation described byEq.59and to the
shifted SQL frequency—and the optical spring generated by a mode
mismatch can be corrected by detuning the SEC length byk​Δ​Ls≈π/4​ℱs×Δ​θmm≈−ϕmmk\Delta L_{\text{s}}\approx\pi/4\mathcal{F}_{\text{s}}\times\Delta\theta_{\text{mm}}\approx-\phi_{\text{mm}}. Note that a higher finesse SEC will produce a larger
squeezed state rotationΔ​θmm\Delta\theta_{\text{mm}}for a given mismatch;
however, the rotation due to an SEC length detuning is amplified by
the same amount and so a similarΔ​Ls\Delta L_{\text{s}}will be needed to
correct the rotation from the same mode mismatchϕmm\phi_{\text{mm}}regardless of the SEC finesse. The magnitude ofϕmm\phi_{\text{mm}}will
still be amplified by the SEC finesse for nearly resonant HOMs,
however (cf.Eq.60).Figure9shows the squeezed state rotation as an SEC detuning due to a length
offsetk​Δ​Lsk\Delta L_{\text{s}}is introduced to compensate for the rotation
caused by the detuning due to a mode mismatchEq.60.
Note that since increasing the SEC finesseℱs\mathcal{F}_{\text{s}}both increases the
RSE poleγrse\gamma_{\text{rse}}and decreases the SQL frequencyΩsqlrse\Omega_{\text{sql}}^{\text{rse}},
increasing the finesse would broaden the region over which minimal
rotation occurs both by decreasing the start of the low frequency
rotation aroundΩsqlrse\Omega_{\text{sql}}^{\text{rse}}and increasing the start of the
high frequency rotation aroundγrse\gamma_{\text{rse}}.

Finally we note that the detuning due to mode mismatch also induces
broadband dephasing due to the imbalanced sidebands which can
occasionally be significant. However, introducing the same SEC length
detuning needed to cancel the broadband rotation also cancels this
broadband dephasing, i.e. the same detuning needed to re-balance the
phase of the upper and lower sideband also re-balances their
magnitude.

## IV.4Interaction with external mode mismatch

While a detailed study of the interaction between the internal
mismatch discussed here and the external mismatch is left for future
work, we can get a rough idea of what those interactions will be and
how this will affect efforts to understand and tune the detectors. We
will find that the similarities between the internal and external
mismatch will confound efforts to understand them separately in
practice in order to know how to tune the detectors to reduce the
squeezing degradations. Crucially, however, there are key differences
in how the internal and external mismatch affect the rotation of the
squeezed state that can be used to disentangle them to some degree.

The phenomenological two mode model of the internal mismatch presented
here can be combined with the two mode model of the external mismatch
described in Ref.[40]. The two external cavities that
are most significant in terms of mode matching are the output mode
cleaner (OMC), which filters the signal from the interferometer before
detection, and the optical parametric amplifier (OPA) in which the
squeezed state is generated. The mode matching with the filter cavity
is negligible compared with the matching between these two
cavities[26].

Recall that the reason that it is only possible to have a beam size
error in the mismatch between the mode of the arm cavity and the mode
of the SEC is because these cavities form a coupled cavity with
standing waves on either side. The OMC, OPA, and the interferometer do
not form a coupled cavity system and it is therefore possible to have
both beam size and curvature errors in the mismatches between these
three cavities. Ref.[40]parametrizes where in this
phase space of beam size and curvature errors the mismatch takes place
by the angleψR\psi_{\text{R}}, and denotes the magnitude of the
mismatch between the OPA and the interferometer byΥI\Upsilon_{\text{I}}and between the OPA and the OMC byΥO\Upsilon_{\text{O}}. Active
wavefront control (AWC) is provided by the telescopes which match the
OMC and OPA to the interferometer (and therefore to each other) and
which are made by mirrors which can change both the magnitude and
phasings of these mismatches by adjusting their radii of
curvature[51,17]. It is also important to note
that the external mismatch should be mostly quadratic and excite
mostly the second order modes.

Ref.[40]showed that the rotation due to external mode mismatch in this
model is approximately111111Equation61describes the same rotation
as does Eq. (89) of Ref.[40]over a wider parameter regime.θext​(Ω)=−2​ΥI​ΥO​sin⁡ψR​(Ω/γrse)2(Ω/γrse)2+(1−Ω2/γrse​γs)2.\theta_{\text{ext}}(\Omega)=-\frac{2\Upsilon_{\text{I}}\Upsilon_{\text{O}}\sin\psi_{\text{R}}\,(\Omega/\gamma_{\text{rse}})^{2}}{(\Omega/\gamma_{\text{rse}})^{2}+(1-\Omega^{2}/\gamma_{\text{rse}}\gamma_{\text{s}})^{2}}.(61)

We therefore expect external mismatch to cause a squeezed state rotation with the same
frequency dependence as the rotation described byEq.59caused by an SEC
detuningϕs\phi_{\text{s}}, due either to internal mismatch or a length detuning, does except
that the maximum rotation in the mid-band in this model isΔ​θext≃2​ΥI​ΥO​sin⁡ψR\Delta\theta_{\text{ext}}\simeq 2\Upsilon_{\text{I}}\Upsilon_{\text{O}}\sin\psi_{\text{R}}rather thanΔ​θs≃4​ℱs/π×ϕs\Delta\theta_{\text{s}}\simeq 4\mathcal{F}_{\text{s}}/\pi\times\phi_{\text{s}}.
The important point is that in reality, regardless of the
details of the mismatch, this rotation will be indistinguishable from
one generated by an SEC detuning and that its magnitude will be a
function of both the magnitude and phasings of the external
mismatch—and therefore controllable to some extent by the AWC. The
external mismatch will also cause a rotation around the SQL frequency
due to radiation pressure in the same way as the internal
mismatch. However, unlike internal mismatch, the external mismatch
does not detune the SEC and it does not create an optical spring and
thus does not modify the optomechanical plantC​(Ω)C(\Omega)or the
dynamics of the mirrors.

As with the internal mismatch where a SEC length detuningΔ​Ls\Delta L_{\text{s}}could be introduced to cancel the rotation caused by internal
mode mismatch—both that described byEq.59and that
due to the modified SQL frequency—a length detuning can counteract
the rotation due to external mismatch to some degree. However, the
mechanism of this rotation is not through a SEC detuning, and it will
therefore not in general be possible to find aΔ​Ls\Delta L_{\text{s}}that
simultaneously cancels the rotation due to both effects. Furthermore,
attempting to cancel the rotation due to external mismatch in anyway
will introduce an optical spring since the external mismatch does not
produce an optical spring in the first place. Thus, attempting to
measure the rotationΔ​θ\Delta\thetaas suggested inSectionIV.3, either with the ADF or through some
other means, in order to determine the correct length detuning to
introduce to cancel the rotation (k​Δ​Ls≈π/4​ℱs×Δ​θk\Delta L_{\text{s}}\approx\pi/4\mathcal{F}_{\text{s}}\times\Delta\theta) is not likely to be successful becauseΔ​θ\Delta\thetawill be a mix of theΔ​θmm\Delta\theta_{\text{mm}}andΔ​θext\Delta\theta_{\text{ext}}. A more successful strategy may be to try to
introduce an SEC detuning to reduce the optical spring followed by
adjusting the AWC to reduce the remaining squeezed state rotationθ​(Ω)\theta(\Omega)due to the external mismatch. Though this will run
into difficulties if the optical spring is generated partially through
other technical means not discussed here.

Finally, the external mismatch will not cause any of the degradations
around higher order mode arm cavity resonances discussed inSectionIV.2. In particular, while external and
internal mismatch affect the broadband loss and rotation in the same
way, the magnitude of the rotation around a HOM resonance will be a
clean error signal for the internal mismatch, especially the quadratic
part.

Ref.[40]further showed that the loss due to external
mode mismatch in this model is approximatelyΛext​(Ω)=ΥO1+Ω2/γrse2+(ΥO+ΥR)​Ω2/γrse21+Ω2/γrse2\Lambda_{\text{ext}}(\Omega)=\frac{\Upsilon_{\text{O}}}{1+\Omega^{2}/\gamma_{\text{rse}}^{2}}+\left(\Upsilon_{\text{O}}+\Upsilon_{\text{R}}\right)\frac{\Omega^{2}/\gamma_{\text{rse}}^{2}}{1+\Omega^{2}/\gamma_{\text{rse}}^{2}}(62)

whereΥR≈4​ΥI−4​ΥI​ΥO​cos⁡ψR.\Upsilon_{\text{R}}\approx 4\Upsilon_{\text{I}}-4\sqrt{\Upsilon_{\text{I}}\Upsilon_{\text{O}}}\cos\psi_{\text{R}}.(63)

We thus expect external output mismatch to coherently add to the
quadratic mismatch to produce low-pass losses and for a combination of
the output and input mismatches to coherently add to the higher order
aberrations to produce high-pass losses with the same RSE pole
frequency. The external mismatch will also be responsible for
radiation pressure noise. The phasing of the external mismatch will
also affect the frequency dependence of this loss, and can thus be
influenced by the AWC, both because it changes the relative amount of
high-pass and low-pass loss inEq.62and because it
will change the interference with the HOMs generated with the internal
mismatch between the arms and SEC.

Taken together, some aspects of a detector’s behavior due to thermal
changes could plausibly be explained by something like the following.
As the thermal state of the interferometer drifts, the frequency-dependent losses due to the internal mismatch will change due to the sensitivity of these losses to the details of the thermal
aberrations as discussed inSectionIV.1. The detuning
of the SEC due to a mismatch such asEq.60will
also change requiring a different SEC length offsetΔ​Ls\Delta L_{\text{s}}to
be introduced to correct the broadband rotationEq.59and the optical spring as discussed inSectionIV.3. In practice, it may not be possible
to continue introducing a larger length offset if needed since this
may saturate photodetector electronics. The HOM peaks will shift
predominantly by quadratic changes to the arm cavity geometry but also
due to changes in other interferometer parameters such as the Gouy
phase of the SEC; the magnitude will also change predominantly due to
changes in the quadratic matching but also due to changes in other
detector parameters to a lesser degree as described inSectionIV.2.3. Even though the modes of the external cavities
are unaffected by the thermal changes in the interferometer, the
external mismatch will be affected since the matching of those
cavities to the altered interferometer mode will have changed; this is
described byΥI\Upsilon_{\text{I}},ψR\psi_{\text{R}}, andΥR\Upsilon_{\text{R}}in the simple model described here. The
internal thermal changes will thus also be accompanied by changes to the
frequency-dependent losses (Eq.62) and broadband
rotation (Eq.61) due to external mismatch which
will need to be corrected with the AWC. These external effects
will be largely indistinguishable from the effects of the internal
mismatch studied throughout the rest of this work. The use of thermal
actuators to correct the thermal aberrations will likewise produce all
of these effects needing further adjustment of the AWC and SEC length
offset.

## IV.5Summary of effects and implications for detector design

In this section we summarize how detector design choices impact the
squeezing degradations discussed above. First we note that
- •

Higher order aberrations are the most significant source of
broadband mismatch loss for the frequencies where mismatch loss is
significant due to their high-pass dynamics
(SectionIV.1).
- •

Quadratic mismatch generates the most significant degradations
around frequencies that a HOM is resonant in the arms
(SectionIV.2) since 1) the degradations due to
quadratic mismatch are amplified to a greater extant than those due
to HOA as summarized inTable1; and 2) since the
HOMs mainly responsible for quadratic mismatch are not clipped by
the arm apertures as much as the HOMs mainly responsible for HOA
are.
- •

Higher order aberrations are the most significant source of
broadband rotation (SectionIV.3). While their
effects may be mitigated by properly tuning the detector to a large
degree, doing so is not independent of external mismatch
(SectionIV.4) and may furthermore be limited by
other technical challenges, so it is still important to minimize
these effects.

The location of several frequency scales are determined by a
combination of other detector parameters and affect the squeezing
degradations in the following waysγrse\gamma_{\text{rse}}RSE poleEq.10

Sets the instrument
bandwidth. The pole frequency of the full coupled cavity low-pass
dynamics of quadratic mismatch and the high-pass dynamics of HOA is
alsoγrse\gamma_{\text{rse}},
cf.Eqs.42and5. The
frequency dependence of the external mismatch loss is similarly
aroundγrse\gamma_{\text{rse}}, cf.Eq.62. Finally, the broadband
rotation also occurs aroundγrse\gamma_{\text{rse}},
cf.Eqs.59,9and61.γsr\gamma_{\text{sr}}SR poleEq.10

Generally sets the bandwidth
of the degradations around HOM arm cavity resonances; seeEq.51and surrounding
discussion. Typically, broader instrument bandwidths thus lead to
narrower HOM resonance degradations.Ωsqlrse\Omega_{\text{sql}}^{\text{rse}}SQL frequencyEq.16

The frequency at which QRPN and shot noise coming from all external vacuum are equal;
QRPN and shot noise coming from SEC loss and higher order aberrations are equal at a
higher frequency (SectionIV.1.2). The squeezed state also rotates
aroundΩsqlrse\Omega_{\text{sql}}^{\text{rse}}due to SEC detunings (caused by both mode mismatch or
length detunings) as well as external mismatch, cf.Fig.9.
Furthermore, the larger is the ratioγrse/Ωsqlrse\gamma_{\text{rse}}/\Omega_{\text{sql}}^{\text{rse}}the better a single
filter cavity can properly compensate the ponderomotive squeezing from the
interferometer and the larger is the region with minimal broadband rotation. Finally,
a larger filter cavity finesse is required for a lower SQL frequency, and the
squeezing degradations due to the filter cavity are enhanced by the filter cavity
finesse[36,40]; however, these degradations are pushed towards
lower frequencies asΩsqlrse\Omega_{\text{sql}}^{\text{rse}}is decreased.γs\gamma_{\text{s}}SEC poleEq.6

The broadband
rotation starts reversing direction aroundγs\gamma_{\text{s}},
cf.Eqs.59,9and61. The
bandwidth of the instrument will also start to be limited byγs\gamma_{\text{s}}if it gets close enough toγrse\gamma_{\text{rse}}. It is generally desirable to
keepγs\gamma_{\text{s}}sufficiently large that its effects are kept out of the
detection band. Ifγs\gamma_{\text{s}}is intentionally made sufficiently small
to target post-merger neutron star physics as is sometimes
discussed, a resonant dip with a width and frequency set byγs\gamma_{\text{s}}will appear in several noise sources; however, SEC loss and internal mode
mismatch loss do not experience this benefit
(SectionIV.1.3).

In addition to determining the frequency scales described above, some
important consequences of detector parameters to the squeezing
degradations are the followingℱa\mathcal{F}_{\text{a}}Arm cavity finesse

The arm cavity finesse enhances every
relevant degradation, as summarized inTable1, and
should be kept as small as possible from a squeezing degradation
perspective.ℱs\mathcal{F}_{\text{s}}SEC finesse

The SEC finesse determines the extent to
which HOMs will be suppressed (mode healed) or enhanced (mode
harmed) in the SEC—both for the mismatch loss
(cf.Figs.6,42and1),
and for the degradations around a HOM arm resonance (cf.Eqs.53,54,55and1). It
also amplifies the broadband rotation due to an SEC detuning,
cf.Eq.59. Notably, it does not affect the optical
SEC loss. The SEC finesse will be chosen primarily to set the
desired instrument bandwidth. In order to keep a fixed bandwidth, it
is necessary to chooseℱs∝ℱa​La\mathcal{F}_{\text{s}}\propto\mathcal{F}_{\text{a}}L_{\text{a}}(cf.Eqs.10and6). Longer and higher
finesse arm cavities therefore generally require higher SEC
finesses.Ψs\Psi_{\text{s}}SEC Gouy phase

Determines the resonance conditions
of the HOMs in the SEC and thus which HOMs will be enhanced or
suppressed in that cavity; seeFig.6.Ψa\Psi_{\text{a}}Arm cavity Gouy phase

Predominately sets the
location of the degradations around arm cavity HOM resonances; seeSectionsIV.2.2and8.LsL_{\text{s}}SEC length

The main effect ofLsL_{\text{s}}is through its
determination of the SEC poleγs\gamma_{\text{s}}, and this favors a cavity
short enough to keep the effects ofγs\gamma_{\text{s}}out of the detection
band.121212The proposed NEMO detector favors a long
SEC[6]because that detector aims to move the effects
ofγs\gamma_{\text{s}}into the detection band to target neutron star
physics. But as described inSectionIV.1.3,γs\gamma_{\text{s}}determines the width of these resonances while their
location is approximatelyγrse​γs=γa​c/Ls\sqrt{\gamma_{\text{rse}}\gamma_{\text{s}}}=\sqrt{\gamma_{\text{a}}c/L_{\text{s}}}. So
if a detector with longer arms like CE, with a
correspondingly lower arm cavity poleγa\gamma_{\text{a}}, were to try to target
the same signals, it would still need a short SEC length in order to
keep this resonance above the roughly\qty2
required[50]. This is another reason why trying to
target neutron star physics in this way is of limited utility in
CE.However, shorter cavities require stronger
telescopes to realize and thus may make it difficult to robustly
achieve the required levels of mode matching in practice.LaL_{\text{a}}Arm cavity length

Since most noises decrease as some
power of the arm length, the biggest effect of longer arms is the
increased sensitivity[25,4]. Notably, however,
SEC loss and the loss due to higher order aberrations are
independent of arm length and therefore become relatively more
significant as the arm length is increased
(SectionsIV.1.3and1). Longer arms
also have lower free spectral ranges—thus limiting the instrument
bandwidth—and lower transverse mode spacings—thus having more
degradations due to HOM arm cavity resonances in the detection band; seeSectionIV.2.SEC apertures

Smaller apertures in the SEC can drastically
reduce the degree to which HOMs resonant in the SEC are mode harmed
while at the same time introduce extra loss away from these
resonances; seeFig.6.Arm cavity apertures

Apertures in the arm cavities reduce the
degradations around HOM arm cavity resonances. In practice, these
degradations due to higher order aberrations can be largely
eliminated by moderate apertures leaving only the effects of
quadratic mismatch and second order modes.

## VOutlook

We have identified two types of internal mode mismatch between the arm
cavities and the signal extraction cavity in a gravitational wave
detector: those due to the quadratic mismatch between the wavefront of
two optical modes and those due to all residual higher order
aberrations. These two types of mismatch are predominantly responsible
for different frequency-dependent squeezed state degradations which
have been detailed here for the first time. While we have focused on
the degradations due to thermal effects in the test mass optics, the
main issue in gravitational wave detectors, the degradations to the
squeezed states due to these two types of mismatch generated through
other means will have similar behavior.

We have studied these degradations theoretically using a modal model
of a coupled cavity system which includes the exact couplings between
the higher order modes produced by the thermal aberrations generated
by the absorption of a small fraction of the power circulating in the
interferometer arm cavities by the test mass optics.
However, given our lack of detailed knowledge of the exact thermal
aberrations in and optical parameters of the current detectors and
given the state-of-the-art modeling tools existing today, it is
unlikely that such models will quantitatively describe these complex
thermo-optomechanical systems by exactly predicting the squeezing
degradations. We believe that experiments on simpler optical systems
are needed in order to validate the effects described in this work, to
quantitatively understand the detailed behavior resulting from
complications not discussed, and to investigate and develop the
techniques suggested for diagnosing and mitigating the effects of the
squeezing degradations including the effects of external mode
mismatch. On the modelling tool perspective, further verification is
needed to determine the model accuracy when dealing with apertured
HOMs and large thermal aberrations, which should also be verified in
small scale experiments.

We have also described a simpler phenomenological model—the full
details of which are given inAppendixC—which
makes no attempt to predict the mode couplings which result from a
given thermal state, but which better elucidates the physics of the
squeezing degradations. Even so, it is often possible to find
phenomenological parameters of this model which produce degradations
that agree with those of the more complicated but exact model for
small mismatch. For some applications, this type of model is therefore
sufficient for characterizing, improving, and designing the detectors
in practice.

Building on the work of Ref.[40]in particular, this
work extends the understanding of mode mismatch in gravitational wave
detectors which is necessary to continue to improve the astrophysical
sensitivity of the current observatories and to design the next
generation ones. This analysis has also shown that the optical
configuration and thermal state of these detectors are inextricably
linked and that the optical system and thermal actuators should
therefore be designed simultaneously informed by an understanding of
the effects of mode mismatch on squeezing degradations as well as its
impacts on other technical challenges.

## Acknowledgements.We thank Lee McCuller, Huy-Tuong Cao, and Aidan Brooks for early
discussions about internal mode mismatch which helped to inspire this
work, and thank Sheila Dwyer and Evan Hall for detailed comments on
the manuscript.
KK thanks Sheila Dwyer and Vicky Xu for assistance in studying
squeezing degradations at the LIGO Hanford observatory and for further
discussions.
KK was supported by NSF PHY–2309200, PHY–2309064, and PHY–2309267.
DB was supported from the Australian Research Council (ARC) on Grant
DE230101035.
DB and KK would like to thank OzGrav (ARC Grant CE170100004 and
CE230100016) for their support for this research with various travel
funded over the years. This material is based upon work supported by
NSF’s LIGO Laboratory, which is a major facility fully funded by the
US National Science Foundation. LIGO was constructed by the
California Institute of Technology and Massachusetts Institute of
Technology with funding from the NSF and operates under NSF
Cooperative Agreement PHY–2309200. Advanced LIGO was built under NSF
PHY–0823459. The LIGO A+ Upgrade to Advanced LIGO is supported by NSF
PHY–1834382

## Appendix AQuantum noise budget factorization in terms of the McCuller squeezing metrics

The noise budget factorization in terms of the McCuller metrics,
developed in Ref.[40], used throughout this paper is
not novel and has been used in, for example,
Refs.[34,18]. We here give a more explicit
description of this factorization and the meaning of all of the traces
shown in the noise budgets than has been given elsewhere.

In the simplest case where a squeezed state is detected without
encountering any optomechanical system that would either introduce a
frequency dependence, due to cavity dispersion for example, or source
radiation pressure, due to acting on a suspended mirror for example,
the quantum noise relative to theℏ​ω0/2\hbar\omega_{0}/2of unsqueezed
vacuum is (cf. Eq. (6) of Ref.[40])N\displaystyle N=η​(S−​cos2⁡ϕ+S+​sin2⁡ϕ)+(1−η)\displaystyle=\eta\left(S_{-}\cos^{2}\phi+S_{+}\sin^{2}\phi\right)+(1-\eta)(64a)S±\displaystyle S_{\pm}=(1−ϕrms2)​e±2​r+ϕrms2​e∓2​r\displaystyle=\left(1-\phi_{\text{rms}}^{2}\right)\mathrm{e}^{\pm 2r}+\phi_{\text{rms}}^{2}\mathrm{e}^{\mp 2r}(64b)

whererris the amplitude of the squeezed state injected into the
system,η\etais the efficiency,ϕ\phiis the relative angle between
the injected squeezed state and the measurement quadrature, andϕrms\phi_{\text{rms}}is the RMS fluctuations in that angle. The quantum
noise in this case is due to three frequency independent effects, or
degradations: 1) lossΛ=1−η\Lambda=1-\etadue to squeezed vacuum
being replaced by unsqueezed vacuum; 2) phase noiseϕrms2\phi_{\text{rms}}^{2}due to mixing the squeezed and anti-squeezed
quadratures; and 3) simply observing more noise by detecting a
quadrature other than the one which was squeezed, i.e. observingϕ≠0\phi\neq 0.

Ref.[40]defines four frequency dependent metrics so
that the noise of a general optomechanical system can be factored in
the same way asEq.64. Using these
metrics, the noiseN​(Ω)N(\Omega)relative to theℏ​ω0/2\hbar\omega_{0}/2of
unsqueezed vacuum is (Eqs. (7) to (9) of Ref.[40])N​(Ω)\displaystyle N(\Omega)=Γ​(Ω)​[η​(Ω)​S​(Ω)+Λ​(Ω)]\displaystyle=\Gamma(\Omega)\left[\eta(\Omega)S(\Omega)+\Lambda(\Omega)\right](65a)S​(Ω)\displaystyle S(\Omega)=S−​(Ω)​cos2⁡[ϕ+θ​(Ω)]+S+​(Ω)​sin2⁡[ϕ+θ​(Ω)]\displaystyle=S_{-}(\Omega)\cos^{2}\left[\phi+\theta(\Omega)\right]+S_{+}(\Omega)\sin^{2}\left[\phi+\theta(\Omega)\right](65b)S±​(Ω)\displaystyle S_{\pm}(\Omega)=[1−Ξ′​(Ω)]​e±2​r+Ξ′​(Ω)​e∓2​r.\displaystyle=\left[1-\Xi^{\prime}(\Omega)\right]\mathrm{e}^{\pm 2r}+\Xi^{\prime}(\Omega)\mathrm{e}^{\mp 2r}.(65c)

In a general system, the rotation of the squeezed stateθ​(Ω)\theta(\Omega)will be frequency dependent and soϕ+θ​(Ω)\phi+\theta(\Omega)replaces the angleϕ\phiinEq.64. In the context of gravitational
wave detectors, a filter cavity is employed to attempt to keepϕ+θ​(Ω)=0\phi+\theta(\Omega)=0at all frequencies. The noise gainΓ​(Ω)\Gamma(\Omega)describes the radiation pressure responsible for the
ponderomotive squeezing in a general optomechanical
system. In a general system, both the lossΛ​(Ω)\Lambda(\Omega)and
efficiencyη​(Ω)\eta(\Omega)are frequency-dependent; whereΓ​(Ω)≈1\Gamma(\Omega)\approx 1, they approximately satisfy the usual
frequency-independent relationshipΛ​(Ω)≈1−η​(Ω)\Lambda(\Omega)\approx 1-\eta(\Omega). Phase noise is quantified by an effective dephasingΞ′​(Ω)\Xi^{\prime}(\Omega)which includes an intrinsic dephasingΞ​(ω)\Xi(\omega)as
well as other sources of phase noise such as RMS phase noiseϕrms2\phi_{\text{rms}}^{2}.

These metrics are given explicitly
by[40,28]θ​(Ω)\displaystyle\theta(\Omega)=12​arg⁡(mp+i​mqmp−i​mq)\displaystyle=\frac{1}{2}\arg\left(\frac{m_{p}+\mathrm{i}m_{q}}{m_{p}-\mathrm{i}m_{q}}\right)(66)Ξ​(Ω)\displaystyle\Xi(\Omega)=12−(|mp|2−|mq|2)2+4​[Re⁡(mq​mp∗)]24​(|mp|2+|mq|2)2\displaystyle=\frac{1}{2}-\sqrt{\frac{(|m_{p}|^{2}-|m_{q}|^{2})^{2}+4[\operatorname{Re}(m_{q}m_{p}^{*})]^{2}}{4(|m_{p}|^{2}+|m_{q}|^{2})^{2}}}(67)η​(Ω)​Γ​(Ω)\displaystyle\eta(\Omega)\Gamma(\Omega)=|mp|2+|mq|2,\displaystyle=|m_{p}|^{2}+|m_{q}|^{2},(68)

wheremp​(Ω)m_{p}(\Omega)andmq​(Ω)m_{q}(\Omega)are the observed noise due to a
squeezed state injected in the phase and amplitude quadratures,
respectively.131313If the phase quadrature is measured, thenmp=[𝔯rse​(+Ω)+𝔯rse∗​(−Ω)]/2m_{p}=[\mathfrak{r}_{\text{rse}}(+\Omega)+\mathfrak{r}_{\text{rse}}^{*}(-\Omega)]/2andmq=[𝔯rse​(+Ω)−𝔯rse∗​(−Ω)]/2​im_{q}=[\mathfrak{r}_{\text{rse}}(+\Omega)-\mathfrak{r}_{\text{rse}}^{*}(-\Omega)]/2\mathrm{i}. In this case,Eqs.66,67and68simplify toEqs.37,39and40in the sideband picture.They can be measured experimentally by
measuring the response to a diagnostic field injected into the system
as described in Ref.[28]. They are calculated byEq.82for the noise budgets in this
paper.Figure 10:A♯\sharpquantum noise budget plotted as10​log10⁡[N​(Ω)/Γ​(Ω)]10\log_{10}[N(\Omega)/\Gamma(\Omega)]for the thermal state ofFig.5.

Rather than plotting the noise relative to shot noiseN​(Ω)N(\Omega),
noise budgets are usually shown in terms of the equivalent
displacement noise. The amplitude spectral density of this
displacement-referred noise is related toN​(Ω)N(\Omega)bySx​x1/2​(Ω)=N​(Ω)|C​(Ω)|2​ℏ​ω02S^{1/2}_{xx}(\Omega)=\sqrt{\frac{N(\Omega)}{|C(\Omega)|^{2}}\frac{\hbar\omega_{0}}{2}}(69)

whereC​(Ω)C(\Omega)is the interferometer response to differential arm
motion, known as the optomechanical plant, with units of\unit/, cf.Eq.46. SinceN​(Ω)N(\Omega)is relative to shot noise, theℏ​ω0/2\hbar\omega_{0}/2converts to an
amplitude spectral density in physical
units.Figure4is in terms ofSx​x1/2S_{xx}^{1/2}.

It is also common to look at the noise relative to unsqueezed vacuum
in decibels. Rather than directly comparing to the frequency
independentℏ​ω0/2\hbar\omega_{0}/2of unsqueezed shot noise usingN​(Ω)N(\Omega), it is more useful to compare to the unsqueezed vacuum
that travels through the optomechanical system along the same path
that the squeezed state takes and which therefore experiences the same
ponderomotive squeezing,
i.e.10​log10⁡[N​(Ω)/Γ​(Ω)]10\log_{10}[N(\Omega)/\Gamma(\Omega)].Figure10shows the A♯\sharpnoise budget for the thermal state ofFig.5in this way.

The noises in these budgets are explicitly the following:

AS Port SQZthe noise arising from the squeezed state injected
into the anti-symmetric (AS) port of the interferometer. Its
contribution toN​(Ω)/Γ​(Ω)N(\Omega)/\Gamma(\Omega)isη​(Ω)​[1−Ξ′​(Ω)]​e−2​r​cos2⁡[ϕ+θ​(Ω)].\eta(\Omega)\left[1-\Xi^{\prime}(\Omega)\right]\mathrm{e}^{-2r}\cos^{2}\left[\phi+\theta(\Omega)\right].(70)

In an ideal system with no squeezing degradations and a filter cavity
that perfectly cancels the rotation due to the ponderomotive
squeezing of the interferometer so thatϕ+θ​(Ω)=0\phi+\theta(\Omega)=0,
this would be the only source of quantum noise. With no filter cavity
and no detuning, this is the shot noise due to the field injected into
the AS port.

AS port Anti-SQZThe noise due to measuring the anti-squeezing rather than the
squeezing. Its contribution toN​(Ω)/Γ​(Ω)N(\Omega)/\Gamma(\Omega)isη​(Ω)​S+​(Ω)​sin2⁡[ϕ+θ​(Ω)].\eta(\Omega)S_{+}(\Omega)\sin^{2}\left[\phi+\theta(\Omega)\right].(71)

If there is a filter cavity, this is the noise due to the filter cavity not perfectly
compensating the squeezing angle rotation throughout the optical system in order to keep
the totalθ​(Ω)=ϕ+θifo​(Ω)+θfc​(Ω)=0\theta(\Omega)=\phi+\theta_{\text{ifo}}(\Omega)+\theta_{\text{fc}}(\Omega)=0at all frequencies, i.e. a “misrotation” relative to the optimal angle. With no
filter cavity and no detuning, it is just the standard radiation pressure contribution
due to the ponderomotive anti-squeezing.

DephasingThere are several sources of dephasing. The total effective dephasing
degrades the squeezed state with a contribution toN​(Ω)/Γ​(Ω)N(\Omega)/\Gamma(\Omega)ofη​(Ω)​Ξ′​(Ω)​e+2​r​cos2⁡[ϕ+θ​(Ω)].\eta(\Omega)\Xi^{\prime}(\Omega)\mathrm{e}^{+2r}\cos^{2}\left[\phi+\theta(\Omega)\right].(72)

The effective dephasingΞ′​(Ω)\Xi^{\prime}(\Omega)includes an intrinsic dephasing inherent to the
system and several sources of technical noise:

Intrinsic Dephasingthe fundamental phase noiseΞ​(Ω)\Xi(\Omega)given byEq.67. It is due to the
upper and lower sidebands experiencing different loss or by the
interaction with a lossy mechanical system.

SQZ RMS Phaseis the usual frequency independent
RMS phase noiseϕrms\phi_{\text{rms}}in the angleϕ\phi; it is simplyΞϕrms=ϕrms2\Xi_{\phi_{\text{rms}}}=\phi_{\text{rms}}^{2}.

Length RMSSince the rotation of the squeezed state depends on
the detunings of the cavities that it encounters as it propagates
throughout the optical system, any fluctuation in the length of
a cavity will also be converted into a phase fluctuation asΞLrms​(Ω)=|∂θ​(Ω)∂L|2​Lrms2,\Xi_{L_{\text{rms}}}(\Omega)=\left|\frac{\partial\theta(\Omega)}{\partial L}\right|^{2}L_{\text{rms}}^{2},(73)

whereLLis the length of the cavity andLrmsL_{\text{rms}}is the RMS
fluctuation in that length. The two “Length RMS” traces shown in
the budgets of this paper are the dephasings due to RMS fluctuations
in the lengths of either the SEC or the filter cavity.

The individual sources of dephasing are combined into the total
effective dephasing as described in Appendix B of
Ref.[40]. Namely, the effective dephasing due to the
individual dephasingsΞ1\Xi_{1}andΞ2\Xi_{2}is141414The individual
dephasing contributions shown in the noise budgets of this paper are
not precisely the individualΞi​(Ω)\Xi_{i}(\Omega)due to the way in which
they must be combined according toEq.74. Rather,
they areΞi−2​Ξi​Ξi−1′\Xi_{i}-2\Xi_{i}\Xi_{i-1}^{\prime}whereΞi−1′\Xi_{i-1}^{\prime}is the
effective dephasing computed by combining the previousi−1i-1dephasing
sources. The dephasing sources in these budgets are combined in the
order in which they appear. So the intrinsic dephasing is justΞ\Xiand the SQZ RMS phase isϕrms2−2​Ξ​ϕrms\phi_{\text{rms}}^{2}-2\Xi\phi_{\text{rms}},
etc. The relative difference2​Ξi−1′2\Xi^{\prime}_{i-1}, however, is generally
small; only\qty2% for\qty100\milliof dephasing.Ξ′​(Ω)=Ξ1​(Ω)+Ξ2​(Ω)−2​Ξ1​(Ω)​Ξ2​(Ω).\Xi^{\prime}(\Omega)=\Xi_{1}(\Omega)+\Xi_{2}(\Omega)-2\,\Xi_{1}(\Omega)\Xi_{2}(\Omega).(74)

LossThe remaining traces in the noise budgets shown in this
paper are due to the various sources of loss where squeezed photons
are lost and replaced with unsqueezed vacuum as discussed inSectionIV.1.1. They are calculated usingEqs.83and84for the noise
budgets in this paper. The optical loss for a given source is the
transfer function from that source to the readout. The mode mismatch
loss is the fraction of total power in the higher order modes rather
than in the fundamental mode.

## Appendix BCavity eigenmodes

The Laguerre-Gauss (LG) modesEq.27—or the equivalent
Hermite-Gauss (HG) modes—are not the true eigenmodes of an optical
cavity. They are a very good approximation in a cavity with no
aberrations and large apertures, but the differences between the true
eigenmodes can become significant in the presence of realistic thermal
aberrations or apertures. Of particular significance is the round-trip
Gouy phase of each eigenmode in the cavity which determines the
resonance conditions of the cavity and thus the extent to which
dynamics are enhanced or suppressed.

Colloquially, the Gouy phase can refer to one of four quantities. It
could be the excess phase that the fundamental mode accumulates over a
plane waverelative to its beam waistas determined by theqqparameter at a point, as inEq.28, which we
denote asΞ\Xi; or it could be the excess phase that the fundamental
accumulatesbetween two spatial locations, which we denote asΨ\Psi. The Gouy phase can also refer to the same quantities for a
particular higher order mode relative to the fundamental. We denote
these with the lower caseξ\xiandψ\psi. When the true eigenmodes
are described by the LG or HG modes,ψ=N​Ψ\psi=N\Psifor a mode of
orderNN, but this is not always the case.

When only the quadratic effects of an optical cavity are accounted for, the eigenmodes
of that cavity are given byEq.27(or the equivalent HG modes). To describe
an optical field at a spatial pointμ\mu, as inEq.28, it is then
necessary to specify the complex beam parameterqμq_{\mu}at that point, i.e. specifying
the beam sizewμw_{\mu}and defocusSμS_{\mu}at that point. It is possible to use any beam
parameter, but the natural choice and the one that requires the fewest modes to describe
that field is the one describing the quadratic fundamental eigenmode of the cavity. That
mode is the eigenmode of the round-trip ABCD matrix for the cavity.151515If the true
eigenmodes differ significantly from the LG or HG modes, the natural choice ofqqparameters—in the sense of requiring the fewest terms in an expansionEq.28to well describe a true eigenmode—is not always obvious or the
one given by the eigenmode ofEq.75.For example, in the case
of the signal extraction cavity shown inFig.1, starting from the
nodena,in_{\text{a,i}}, this is the matrix𝑺​(Ls)​𝑭​(2/Rs)​𝑺​(Ls)​𝑭​(1/fth)​𝑭​(−2​n/Ri)​𝑭​(1/fth)\bm{S}(L_{\text{s}})\,\bm{F}(2/R_{\text{s}})\,\bm{S}(L_{\text{s}})\,\bm{F}(1/f_{\text{th}})\,\bm{F}(-2n/R_{\text{i}})\,\bm{F}(1/f_{\text{th}})(75)

where𝑭​(D)\bm{F}(D)is the ABCD matrix for a focusing element (a lens or a mirror) with
defocusDDand𝑺​(L)\bm{S}(L)is the ABCD matrix for a space of lengthLL. We write the
ABCD matrices in a different font to emphasize that they are2×22\times 2matrices
transforming the complexqqparameters, while the matrices inEqs.35and1are high dimensional matrices transforming the
HOMs themselves, i.e. acting on the vector ofcp​ℓ​(qμ)c_{p\ell}(q_{\mu})coefficients inEq.28.

Once theqqparameters have been determined from the cavity eigenmode, thus defining
the HOMs, the Gouy phase accumulated between two spatially separated points is the
difference between the Gouy phasesΞμ\Xi_{\mu}inEq.28at each point.
For example, the Gouy phase accumulated between the SEM and the ITM AR surface isΨ=Ξa,i−Ξs,r\Psi=\Xi_{\text{a,i}}-\Xi_{\text{s,r}}. The total phase accumulated for a HOM of orderN=2​p+|ℓ|N=2p+|\ell|relative to the fundamental is thenψ=N​Ψ\psi=N\Psi. The total
round-trip Gouy phase in the cavity is[7]2​Ψ=sgn⁡B​arccos⁡(A+D2)2\Psi=\operatorname{sgn}B\,\arccos\left(\frac{A+D}{2}\right)(76)

whereA,B,A,B,andDDare the elements of the round-trip ABCD matrix, given byEq.75in the example of the SEC. For the arm cavity with only
the ITM and ETM,Eq.76is justEq.57.

In reality, the eigenmodes of the cavity are the eigenmodes of the
round-trip operator of that cavity.161616Unlike the LG and HG
modes, the true cavity eigenmodes are bi-orthogonal rather than
orthogonal and are not guaranteed to be complete[49].In the case of the SEC starting from the same nodena,in_{\text{a,i}},
this is𝐏s​(−rs​𝟏)​𝐏s​𝐋as​(ri​𝐒ss)​𝐋sa.\mathbf{P}_{\text{s}}(-r_{\text{s}}\mathbf{1})\mathbf{P}_{\text{s}}\mathbf{L}_{\text{as}}(r_{\text{i}}\mathbf{S}_{\text{ss}})\mathbf{L}_{\text{sa}}.(77)

The phase of the eigenvalue of each mode is the true round-trip Gouy
phase2​ψ2\psifor that mode. Each eigenmode can be expanded as inEq.28and, while the modesup​ℓu_{p\ell}have Gouy
phasesξ=N​Ξ\xi=N\Xidetermined fromEq.76, the summation of
all of these LG modes results in a phase determined byEq.77, and this phaseψ\psiis not necessarily an
integer multiple of the phaseΨ\Psiof the first eigenmode.

Now consider how thermal aberrations affect the mode couplings and the
Gouy phase as calculated byEqs.77and76. First we note that in
addition to the phase evolution of an optical field described by the
OPDEq.25, there will be aperturesA​(r,ϕ)A(r,\phi)due to the finite spatial extent of the optics for example. The
reasoning leading to the general coupling between modesEq.31being broken up into a quadratic and
higher order part is still valid in the presence of apertures and so⟨q2|A​(r,ϕ)​e−i​k​Z​(r,ϕ)|q1⟩=⟨q2|A​(r,ϕ)​e−i​k​zhoa​(r,ϕ)|q^1⟩\big\langle q_{2}\big|A(r,\phi)\,\mathrm{e}^{-\mathrm{i}kZ(r,\phi)}\big|q_{1}\big\rangle=\big\langle q_{2}\big|A(r,\phi)\,\mathrm{e}^{-\mathrm{i}kz_{\text{hoa}}(r,\phi)}\big|\hat{q}_{1}\big\rangle(78)

in general. All of the lens𝐋i​j\mathbf{L}_{ij}and surface𝐒i​j\mathbf{S}_{ij}operators are thus the same as inEq.35with the
addition ofA​(r,ϕ)A(r,\phi)multiplying the exponentials.

Several effects will modify the couplings and round-trip Gouy
phase. First, any quadratic change due to the quadratic terma​r2ar^{2}inEq.25directly changes the eigenmodeqqparameter and thus changes the Gouy phase as calculated byEq.76. Second, higher order aberrationszhoa​(r)z_{\text{hoa}}(r), and thus the operators inEq.35,
do not change the eigenmode or the round-trip Gouy phase as computed
by the quadratic effects andEq.76, but do change
the Gouy phase of the true eigenmodes as calculated byEq.77. Since quadratic effects vary the beam sizeww, they also affect the extent to which modes are clipped by
apertures. This is another effect that alters the operators inEq.35and thus the Gouy phases of the true
eigenmodes. Furthermore, any quadratic change to the beam parametersqqchanges the modal basis of the HOMs and thus the matrix
elements of the operatorsEq.35irrespective of any
higher order aberration effects.

Finally, there are several methods of removing the quadratic terma​r2ar^{2}from an OPD as inEq.25, and some of
these depend on the beam size[11]. Therefore different
methods will yield varying fractions of quadratic or higher order
aberrations for the same original OPD. The important point, however,
is that regardless of the details of how an OPD is broken up or how
theqqparameters are chosen, there will always be a quadratic part
that behaves likeEq.33with𝐔r≈𝐔i−1\mathbf{U}_{\text{r}}\approx\mathbf{U}_{\text{i}}^{-1}, thus having low-pass dynamics, and the remaining higher
order aberrations which behave likeEq.33with𝐔r≈𝐔i\mathbf{U}_{\text{r}}\approx\mathbf{U}_{\text{i}}, thus having
high-pass dynamics. Furthermore, the ensuing squeezing degradations
will be identical no matter how the coefficientaainEq.25is determined and subtracted as long as
the equivalentfth=−1/2​af_{\text{th}}=-1/2ais used for the substrate thermal
lens focal length instead of that giving an arbitraryΔ​w/w\Delta w/w, and as
long as enough HOMs are used in the calculation. Indeed, it is not
even necessary to break the OPD up into a quadratic and higher order
part in a calculation in order to get the same numerical
results.171717It is, however, computationally more efficient to
attribute some quadratic part of an OPD to the focal length of a thin
lens because the resultingqqparameters as determined byEq.75will then more closely resemble the true
eigenmodes, thus requiring fewer terms in an expansionEq.28to accurately describe the true eigenmodes.Nevertheless, the squeezing degradations are still highly sensitive to
the full details ofZ​(r)Z(r)regardless of the details of the
calculation.

It is also important to understand how we study the effects of changing cavity Gouy
phases as presented inFigs.6,7and8.
In these analyses, the Gouy phase displayed on thexx-axis or noted in the legends, is
theone-wayGouy phaseΨ\Psiof the fundamental mode in that cavity as
computed withEq.76. The question of which Gouy phase to design a
cavity for in the absence of thermal aberrations is a critical design choice and is
determined by the cavity geometry: lengths between optics, radii of curvatures of
mirrors, lenses purposely polished into optic substrates, etc. It is thus difficult to
change the Gouy phase in an analysis as that requires redesigning the cavities and
ensuring that they are well mode-matched. Furthermore, quadraticΔ​w/w\Delta w/wchanges are
unavoidably accompanied by SEC Gouy phase changes. To avoid these complications we thus
adjust the Gouy phasesΞμ\Xi_{\mu}inEq.28ad hoc, independent of theirqqparameters determined byEq.75, so that all of the phasesΨμ\Psi_{\mu}in the propagators𝐏s\mathbf{P}_{\text{s}}produce the desired Gouy phase for the
fundamental mode. However, given these adjusted propagators, the exact eigenmodes and
Gouy phases as computed byEq.77are still used and thus most of the
effects of higher order aberrations are captured. The one exception is that the beam
size change which must accompany a change in Gouy phase is not accounted for and thus
the change in the degree to which HOMs are clipped by apertures as would really happen
is not captured. This is not significant at the level of detail and for the goals of
this work, but it does need to be accounted for when characterizing an existing detector
or designing a new one. This treatment can also be justified by imagining that as the
Gouy phase and beam size change, the apertures are adjusted to keep the same aperture
ratios given inTable2fixed.

Finally we note that the details discussed above could, in principle,
offer a mundane un-physical explanation for why inFig.5the total loss with the addition of quadratic
mismatch appears to be less than that with the higher order
aberrations alone as parameterized by our artificial separation of the
two effects. However, as described inAppendixD, our
calculation ensures that identical higher order aberrations are used
regardless of the amount of quadratic mismatch. Furthermore, we have
used enough HOMs in the simulation that the physical observables do
not depend on the modal basis of the HOMs which is indirectly
affected byΔ​w/w\Delta w/w. Therefore, the explanation for this behavior is
the destructive interference of the HOMs.

## Appendix CPhenomenological model

When generalized to include radiation pressure and external mode
mismatch, the phenomonelogical model used throughout the body of the
paper is a slight extension of the model presented in Appendix E of
Ref.[40]to include both quadratic mismatch and higher
order aberrations. Ref.[40]considers the fundamental
and a single HOM with output mismatchΥO\Upsilon_{\text{O}}between the
OPA and the OMC, input mismatchΥI\Upsilon_{\text{I}}between the OPA
and the interferometer, and quadratic mismatchΥA\Upsilon_{\text{A}}between the arms and the SEC. Each of these mismatches also have a
phasingψ\psiand are described by the4×44\times 4matrices𝐔⇔​(Υ,ψ)=[1−Υ​1−Υ​R​(ψ)Υ​R​(−ψ)1−Υ​1],\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}(\Upsilon,\psi)=\begin{bmatrix}\sqrt{1\!-\!\Upsilon}\,\mathbbl{1}&-\sqrt{\Upsilon}\,\mathbbl{R}(\psi)\\
\sqrt{\Upsilon}\,\mathbbl{R}(-\psi)&\sqrt{1\!-\!\Upsilon}\,\mathbbl{1}\end{bmatrix},(79)

where1\mathbbl{1}andR​(ψ)\mathbbl{R}(\psi)are the2×22\times 2identity and rotation matrices, respectively.
That model can be extended by replacing the mismatch matrix𝐔⇔A=𝐔⇔​(ΥA,ψA)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}_{\text{A}}=\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}(\Upsilon_{\text{A}},\psi_{\text{A}})and
its inverse with ones including both types of internal mismatch as described
byEqs.17,18and19𝐔⇔A\displaystyle\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}_{\text{A}}→𝐔⇔i=𝐔⇔quad​(Υquad,ψquad)​𝐔⇔hoa​(Υhoa,ψhoa)\displaystyle\rightarrow\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}_{\text{i}}=\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}_{\text{quad}}(\Upsilon_{\text{quad}},\psi_{\text{quad}})\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}_{\text{hoa}}(\Upsilon_{\text{hoa}},\psi_{\text{hoa}})(80a)𝐔⇔A−1\displaystyle\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}_{\text{A}}^{-1}→𝐔⇔r=𝐔⇔hoa​(Υhoa,ψhoa)​𝐔⇔quad−1​(Υquad,ψquad)\displaystyle\rightarrow\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}_{\text{r}}=\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}_{\text{hoa}}(\Upsilon_{\text{hoa}},\psi_{\text{hoa}})\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}_{\text{quad}}^{-1}(\Upsilon_{\text{quad}},\psi_{\text{quad}})(80b)

In particular, these substitutions should be made in Eqs. (E13) to
(E18).

This is sufficient for many purposes. Since second order modes are
generally responsible for quadratic mismatch and higher order HOMs are
generally responsible for higher order aberrations, it can
occasionally be useful to include two HOMs in order to more carefully
investigate resonance effects. In this case, there are three couplings
and phases, and the mismatch matrices are of the form𝐔⇔​({Υ},{ψ})=\displaystyle\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{U}}(\{\Upsilon\},\{\psi\})=[1−Υ10−Υ20​1−Υ10​R​(ψ10)−Υ20​R​(ψ20)Υ10​R​(−ψ10)1−Υ10−Υ21​1−Υ21​R​(ψ21)Υ20​R​(−ψ20)Υ21​R​(−ψ21)1−Υ20−Υ21​1]\displaystyle\begin{bmatrix}\sqrt{1\!-\!\Upsilon_{10}\!-\!\Upsilon_{20}}\,\mathbbl{1}&-\sqrt{\Upsilon_{10}}\,\mathbbl{R}(\psi_{10})&-\sqrt{\Upsilon_{20}}\,\mathbbl{R}(\psi_{20})\\
\sqrt{\Upsilon_{10}}\,\mathbbl{R}(-\psi_{10})&\sqrt{1\!-\!\Upsilon_{10}\!-\!\Upsilon_{21}}\,\mathbbl{1}&-\sqrt{\Upsilon_{21}}\,\mathbbl{R}(\psi_{21})\\
\sqrt{\Upsilon_{20}}\,\mathbbl{R}(-\psi_{20})&\sqrt{\Upsilon_{21}}\,\mathbbl{R}(-\psi_{21})&\sqrt{1\!-\!\Upsilon_{20}\!-\!\Upsilon_{21}}\,\mathbbl{1}\end{bmatrix}(81)

Extending this further is of limited utility, and a model such asAppendixDshould be used if more detail is needed. It
should also be noted that, even in the single HOM case, many
parameters are degenerate in such a model and some parameters can thus
not be easily fit to data. The utility of such a model is in getting a
feel for what combinations of mismatch are consistent with some data,
or in understanding what range of behavior could be expected in some
optical design.

## Appendix DSimulation detailsParameterSymbolUnitsLIGO A♯\sharpCEArm powerPaP_{\text{a}}\unit\mega1.51.51.51.5Arm lengthLaL_{\text{a}}\unit444040SEC lengthLsL_{\text{s}}\unit5555120120Test mass massMM\unit100100320320ITM transmissionTiT_{\text{i}}\unit%1.41.41.41.4SEM transmissionTsT_{\text{s}}\unit%32.532.522Arm Gouy phaseΨa\Psi_{\text{a}}\unitdeg310310220220SEC Gouy phaseΨs\Psi_{\text{s}}\unitdeg20202020SEC lossεs\varepsilon_{\text{s}}\unit500500500500Arm lossεa\varepsilon_{\text{a}}\unit75754040Readout lossεro\varepsilon_{\text{ro}}\unit%3.53.53.53.5Injection lossεinj\varepsilon_{\text{inj}}\unit%4433Filter cavity lossεfc\varepsilon_{\text{fc}}\unit%30308080Filter cavity lengthLfcL_{\text{fc}}\unit30030040004000Filter cavity transmissionTfcT_{\text{fc}}\unit1000100017001700Injected squeezinge2​r\mathrm{e}^{2r}\unit18181818RMS phase noiseϕrms\phi_{\text{rms}}\unit\milli10101010Arm aperture ratio——3.13.12.92.9SEC aperture ratio——2.62.62.52.5Table 2:Baseline parameters used for LIGO A♯\sharpand Cosmic
Explorer unless otherwise stated. The arm and SEC aperture ratios
are the ratio between the diameter of the apertures and the
diameter of the beams in the arm cavity and SEC, respectively. The
Gouy phases are one-way and the losses are round-trip. Note that
the injected squeezing is the idealized and lossless squeezing
level generated at the source before encountering any losses.

The main numerical results of this paper shown in all of the figures
are obtained using thefinessesimulation
package[14]to simulate the DARM coupled cavity system
shown inFig.1using the parameters given inTable2. In order to simulate thermal lensing
in the ITM substrate, a thin lens is placed next to the AR surface of
the ITM. Finally, the squeezed state is injected into the coupled
cavity system through the AR surface of the SEM after reflecting off
of an external Fabry-Perot cavity acting as the filter cavity which is
not shown in the figure. When the SEC finesseℱs\mathcal{F}_{\text{s}}is varied, the
filter cavity bandwidth and detuning are reoptimized according to
Ref.[36].

The ITM lens initially has an infinite focal length and the radii of curvature of all
optics are adjusted to give perfect mode matching between all three cavities of the
system. Future work will expand on the discussion inSectionIV.4by
introducing mismatch between all optical cavities while at the same time adding an
additional two cavities to serve as the optical parametric amplifier (OPA), in which the
squeezed state is generated, and the output mode cleaner (OMC), which filters the signal
before detection.

Our treatment of the thermal aberrations is described inSectionsIIIand3. In particular, the thermal aberrations
due to the beam-heating of the laser are computed using the Hello-Vinet
model[32,33,56]. The total optical path length
is decomposed into the quadratic terms and the higher order aberrations (HOA) as shown
inFig.3. First the piston and then the quadratic terms are removed by
weighting the optical path length by a Gaussian with a radius equal to the beam size of
the laser on the relevant optic. The remaining terms are the HOA and are added as an OPD
map to the lens[11]. Normally the quadratic terms which were removed would
then be added to the focal length of the lens; however, in this work we study the
quadratic and higher order aberrations separately and thus set the focal length of the
lens to produce a given quadraticΔ​w/w\Delta w/waverage beam size error. The thermoelastic
deformations of the surface of the mirrors are treated similarly except that the HOA due
to the thermoelastic deformations are added as surface maps to the HR surfaces of the
mirrors. Circular apertures are also added to the lens and mirror HR surfaces. Future
work will include the effects of thermal
actuators[13,48,29]and other imperfections such as coating
defects[12]or mis-centered laser beams on the test mass optics.

It is important to note that changingΔ​w/w\Delta w/win this way by changing
the focal length of the thin lens changes the beam size on the back of
the ITM in the extraction cavity and therefore the eigenmodes of the
SEC. However, it does not change the beam size on the front of the ITM
in the arm cavity and thus does not change the eigenmodes of the arm
cavities; see discussion aroundEq.34. Since we use
the beam size of the beam on the HR surface of the mirrors when
removing the piston and quadratic terms of the OPD or surface
deformation, the higher order aberrations used for differentΔ​w/w\Delta w/ware identical. SeeAppendixBfor a detailed
discussion of how this parameterization of thermal aberrations affects
cavity eigenmodes.

Since this is a simple coupled cavity model, the DC fields are added ad hoc to produce a
given arm power in the fundamental mode of the arm cavity. The ITM and ETM are simulated
as free masses. We then simulate all even Hermite-Gauss modes up to order 10 and collect
transfer functions for the optical fields between several locations in the
optomechanical system into42×4242\times 42matrices corresponding to the phase and
amplitude quadratures for the fundamental and each of the 20 HOMs. The total path the
squeezed state takes from its injection into the filter cavity to the readout, the path
fromμas,i\mu_{\text{as,i}}toμas,r\mu_{\text{as,r}}inFig.1, is𝐇⇔​(Ω)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{H}}(\Omega). The transfer functions from each loss location to the readout are
collected in the matrices𝐓⇔μ​(Ω)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{T}}_{\mu}(\Omega). For SEC loss, this is the path fromμa,r\mu_{\text{a,r}}toμas,r\mu_{\text{as,r}}inFig.1, for example.
Finally, the transfer functions of ETM motion to the readout are collected into a42×142\times 1vector𝐓⇒rse​(Ω)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{T}}_{\text{rse}}(\Omega)The units of𝐇⇔​(Ω)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{H}}(\Omega)and𝐓⇔μ​(Ω)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{T}}_{\mu}(\Omega)are\unit/ and the units of𝐓⇒rse​(Ω)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{T}}_{\text{rse}}(\Omega)are\unit/.

The quantum noise budgets described inAppendixAare then
computed using a procedure similar to the one outlined in Appendix E
of Ref.[40]. First the local oscillator𝐯⇒†\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}is defined byEq.87as described below and then
the McCuller metrics are calculated byEqs.66,67and68using the noise quadraturesmp​(Ω)=𝐯⇒†​𝐇⇔​(Ω)​𝐞⇒p​0,mq=𝐯⇒†​𝐇⇔​(Ω)​𝐞⇒q​0,m_{p}(\Omega)=\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{H}}(\Omega)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{p0},\qquad m_{q}=\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{H}}(\Omega)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{q0},(82)

where𝐞⇒q​0\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{q0}and𝐞⇒p​0\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{p0}are the basis vectors for
the amplitude and phase quadratures of the fundamental mode,
respectively. The loss due to mode mismatch is the fraction of the
total power in the higher order modes rather than in the fundamentalΓ​(Ω)​Λmm​(Ω)=|𝐯⇒†​𝐇⇔​(Ω)|2−η​(Ω)​Γ​(Ω).\Gamma(\Omega)\Lambda_{\text{mm}}(\Omega)=\left|\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{H}}(\Omega)\right|^{2}-\eta(\Omega)\Gamma(\Omega).(83)

The total lossΛ​(Ω)\Lambda(\Omega)inEq.65ais
obtained by additionally propagating theεμ\varepsilon_{\mu}of unsqueezed
vacuum entering at each locationμ\muto the readoutΓ​(Ω)​Λ​(Ω)=Γ​(Ω)​Λmm​(Ω)+∑μ|𝐯⇒†​𝐓⇔μ​(Ω)|2.\Gamma(\Omega)\Lambda(\Omega)=\Gamma(\Omega)\Lambda_{\text{mm}}(\Omega)+\sum_{\mu}\left|\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{T}}_{\mu}(\Omega)\right|^{2}.(84)

For vacuum entering the SEC,|𝐯⇒†​𝐓⇔μ​(Ω)|2\left|\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{T}}_{\mu}(\Omega)\right|^{2}is theΛsec​(ω)\Lambda_{\text{sec}}(\omega)ofSectionIV.1. The
quantum noise gain is calculated as181818As discussed in
Ref.[40], there is freedom in definingΓ\Gammasince
only the combinationη​Γ\eta\Gammacan be measured.Equation85sums over all sources of loss and corresponds to the choice thatΓ=N|S=1\Gamma=N|_{S=1}, i.e. the gain is just the noise in the absence
of an injected squeezed stater=0r=0. Equations (40) and (E20) of
Ref.[40]only sum over the internal losses as that
work is primarily focused on external mismatch.Γ​(Ω)=|𝐯⇒†​𝐇⇔​(Ω)|2+∑μ|𝐯⇒†​𝐓⇔μ​(Ω)|2.\Gamma(\Omega)=\left|\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{H}}(\Omega)\right|^{2}+\sum_{\mu}\left|\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{T}}_{\mu}(\Omega)\right|^{2}.(85)

The efficiencyη​(Ω)\eta(\Omega)is then calculated by dividing theη​Γ\eta\Gammaas computed byEq.68by theΓ\Gammacomputed byEq.85.

The optomechanical plant is calculated from𝐓⇒rse\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{T}}_{\text{rse}}asC​(Ω)=12​𝐯⇒†​𝐓⇒rse​(Ω)C(\Omega)=\frac{1}{\sqrt{2}}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{T}}_{\text{rse}}(\Omega)(86)

where the factor of1/21/\sqrt{2}accounts for the presence of the
beamsplitter when mapping the dynamics of the coupled cavity onto
those of an interferometric gravitational wave detector.

Finally, the dephasing due to RMS length fluctuations of an optical
cavity is computed by repeating the calculation of𝐇⇔\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{H}}after
detuning that cavity by a small amount. The squeezing angleθ​(Ω)\theta(\Omega)of this detuned system is then calculated using the
newmpm_{p}andmqm_{q}which is then used to find the derivative∂θ​(Ω)/∂L\partial\theta(\Omega)/\partial Lneeded for the calculation of the
dephasing given byEq.73.

As discussed around Eq. (E21) of Ref.[40], the local
oscillator should be defined taking the optical DC response of the coupled
cavity into account. To this end, the transfer functions𝐓⇔lo\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{T}}_{\text{lo}}are computed with infinite mass mirrors atΩ=0\Omega=0from the fields leaving the ITM HR surface at the point
with Gaussianqqparameter−qhr∗-q_{\text{hr}}^{*}inFig.1to
the readout. The local oscillator is then defined as𝐯⇒†=(𝐏⇔​𝐓⇔lo​𝐞⇒p​0|𝐏⇔​𝐓⇔lo​𝐞⇒p​0|)†​𝐑⇔​(ζ)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}=\left(\frac{\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{P}}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{T}}_{\text{lo}}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{p0}}{\left|\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{P}}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{T}}_{\text{lo}}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{p0}\right|}\right)^{\dagger}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{R}}(\zeta)(87)

whereζ\zetais the homodyne angle and𝐏⇔=𝐞⇒q​0​𝐞⇒q​0†+𝐞⇒p​0​𝐞⇒p​0†\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{P}}=\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{q0}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{q0}^{\dagger}+\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{p0}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{p0}^{\dagger}represents the OMC by rejecting all HOMs. Even though when using
balanced homodyne readout, as we assume will be done for both
A♯\sharpand CE, the local oscillator can be defined simply as𝐯⇒†=𝐞⇒p​0†​𝐑⇔​(ζ)\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{v}}^{\dagger}=\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Rightarrow}$}}}{\mathbf{e}}_{p0}^{\dagger}\overset{\raisebox{-1.0pt}{\text{\tiny$\bm{\Leftrightarrow}$}}}{\mathbf{R}}(\zeta), it is easier to
define it asEq.87because this best represents a pure phase
signal by taking into account the extra phases accumulated by the mode
scattering and propagation through the SEC. In doing so, we always
measure the phase quadratureζ=0\zeta=0throughout this work without
further optimizing the homodyne angle to produce the best sensitivity.

While the procedure for finding the operating point of the system is
fairly clear—as described in the main text (especiallySectionIV.3)—it is difficult to write down an
algorithm that will reliably find the correct operating points in
practice. Therefore, the simulation for each thermal state is tuned by
hand using the optomechanical plantC​(Ω)C(\Omega), as would be obtained
through detector calibration, and the rotation of the squeezed stateθ​(Ω)\theta(\Omega), as would be obtained from ADF
injections[28]or some other means, to ensure that a
reasonable operating point is found. In particular, an SEC length
detuningΔ​Ls\Delta L_{\text{s}}is introduced both to cancel the broadband
squeezed state rotation as illustrated inFig.9and
ensure that the resultingC​(Ω)C(\Omega)is the proper RSE plant without
an optical spring.

## References
- [1]A. G. Abacet al.(2025)GWTC-4.0: An Introduction to Version 4.0 of the Gravitational-Wave Transient Catalog.Astrophys. J. Lett.995(1),pp. L18.External Links:2508.18080,DocumentCited by:§I.
- [2]B. P. Abbottet al.(2017)Calibration of the Advanced LIGO detectors for the discovery of the binary black-hole merger GW150914.Phys. Rev. D95(6),pp. 062003.External Links:1602.03845,DocumentCited by:§IV.1.3.
- [3]B. P. Abbottet al.(2017)GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral.Phys. Rev. Lett.119(16),pp. 161101.External Links:1710.05832,DocumentCited by:§I.
- [4]B. P. Abbottet al.(2017)Exploring the Sensitivity of Next Generation Gravitational Wave Detectors.Class. Quant. Grav.34(4),pp. 044001.External Links:1607.08697,DocumentCited by:itemLaL_{\text{a}}Arm cavity length.
- [5]F. Acerneseet al.(2019)Increasing the Astrophysical Reach of the Advanced Virgo Detector via the Application of Squeezed Vacuum States of Light.Phys. Rev. Lett.123(23),pp. 231108.External Links:DocumentCited by:§I,§IV.
- [6]K. Ackleyet al.(2020)Neutron Star Extreme Matter Observatory: A kilohertz-band gravitational-wave detector in the global network.Publ. Astron. Soc. Austral.37,pp. e047.External Links:2007.03128,DocumentCited by:§IV.1.3,footnote 12.
- [7]K. Arai(2013)On the accumulated round-trip Gouy phase shift for a general optical cavity.Technical NoteTechnical ReportLIGO-T1300189.External Links:LinkCited by:Appendix B.
- [8]Hans-A. Bachor and T. C. Ralph(2004)A Guide to Experiments in Quantum Optics, 2nd, Revised and Enlarged Edition.Cited by:§IV.
- [9]L. Barsotti, J. Harms, and R. Schnabel(2019)Squeezed vacuum states of light for gravitational wave detectors.Rept. Prog. Phys.82(1),pp. 016905.External Links:DocumentCited by:§I,§IV,§IV.
- [10]B. Bochner(2003-06)Simulating a Dual-Recycled Gravitational Wave Interferometer with Realistically Imperfect Optics.General Relativity and Gravitation35(6),pp. 1029–1057.External Links:Document,astro-ph/0306133Cited by:§II.2.
- [11]C. Bond, D. Brown, A. Freise, and K. A. Strain(2016-12)Interferometer techniques for gravitational-wave detection.Living Reviews in Relativity19(1),pp. 3.External Links:DocumentCited by:Appendix B,Appendix D,§III.1.
- [12]A. F. Brookset al.(2021)Point absorbers in Advanced LIGO.Appl. Opt.60(13),pp. 4047–4063.External Links:2101.05828,DocumentCited by:Appendix D.
- [13]A. F. Brookset al.(2016)Overview of Advanced LIGO Adaptive Optics.Appl. Opt.55,pp. 8256.External Links:1608.02934,DocumentCited by:Appendix D,§III.2.
- [14]FINESSEExternal Links:Document,LinkCited by:Appendix D.
- [15]A. Buonanno and Y. Chen(2001)Quantum noise in second generation, signal recycled laser interferometric gravitational wave detectors.Phys. Rev. D64,pp. 042006.External Links:gr-qc/0102012,DocumentCited by:§IV,§IV.3.
- [16]A. Buonanno and Y. Chen(2002)Signal recycled laser interferometer gravitational wave detectors as optical springs.Phys. Rev. D65,pp. 042001.External Links:gr-qc/0107021,DocumentCited by:§IV.3.
- [17]H. T. Cao, S. W. S. Ng, M. Noh, A. Brooks, F. Matichard, and P. J. Veitch(2020-12)Enhancing the dynamic range of deformable mirrors with compression bias.Optics Express28(26),pp. 38480.External Links:DocumentCited by:§IV.4.
- [18]E. Capoteet al.(2025)Advanced LIGO detector performance in the fourth observing run.Phys. Rev. D111(6),pp. 062002.External Links:2411.14607,DocumentCited by:Appendix A,§I,§I,§I.
- [19]C. M. Caves(1981)Quantum Mechanical Noise in an Interferometer.Phys. Rev. D23,pp. 1693–1708.External Links:DocumentCited by:§IV.
- [20]C. M. Caves and B. L. Schumaker(1985)New formalism for two-photon quantum optics. 1. Quadrature phases and squeezed states.Phys. Rev. A31,pp. 3068–3092.External Links:DocumentCited by:§II.1.
- [21]C. Caves(1980)Quantum-Mechanical Radiation-Pressure Fluctuations in an Interferometer.Phys. Rev. Lett.45(2),pp. 75–79.External Links:DocumentCited by:§IV.
- [22]S. L. Danilishin and F. Ya. Khalili(2012)Quantum Measurement Theory in Gravitational-Wave Detectors.Living Rev. Rel.15,pp. 5.External Links:1203.1706,DocumentCited by:§II.1.
- [23]R. Essick, S. Vitale, and M. Evans(2017)Frequency-dependent responses in third generation gravitational-wave detectors.Phys. Rev. D96(8),pp. 084004.External Links:1708.06843,DocumentCited by:footnote 8.
- [24]ET Steering Committee(2020-11-29)ET design report update 2020.Technical reportTechnical ReportET-0007A-20,Einstein Telescope.External Links:LinkCited by:§I.
- [25]M. Evanset al.(2021-09)A Horizon Study for Cosmic Explorer: Science, Observatories, and Community.arXiV.External Links:2109.09882Cited by:§I,itemLaL_{\text{a}}Arm cavity length.
- [26]D. Ganapathyet al.(2023)Broadband Quantum Enhancement of the LIGO Detectors with Frequency-Dependent Squeezing.Phys. Rev. X13(4),pp. 041021.External Links:DocumentCited by:§I,§IV,§IV.2,§IV.4,§IV.
- [27]D. Ganapathy, L. McCuller, J. Graef Rollins, E. D. Hall, L. Barsotti, and M. Evans(2021)Tuning Advanced LIGO to kilohertz signals from neutron-star collisions.Phys. Rev. D103(2),pp. 022002.External Links:2010.15735,DocumentCited by:§IV.1.1.
- [28]D. Ganapathy, V. Xu, W. Jia, C. Whittle, M. Tse, L. Barsotti, M. Evans, and L. McCuller(2022-06)Probing squeezing for gravitational-wave detectors with an audio-band field.Phys. Rev. D105(12),pp. 122005.External Links:Document,2203.03849Cited by:Appendix A,Appendix A,Appendix D,Figure 7,§IV.2.3,§IV.2.3.
- [29]A. W. Goodwin-Jones, R. Cabrita, M. Korobko, M. Van Beuzekom, D. D. Brown, V. Fafone, J. Van Heijningen, A. Rocchi, M. G. Schiworski, and M. Tacca(2024-02)Transverse mode control in quantum enhanced interferometers: a review and recommendations for a new generation.Optica11(2),pp. 273.External Links:Document,2311.04736Cited by:Appendix D,§III.2.
- [30]M. Granata, A. Amato, L. Balzarini, M. Canepa, J. Degallaix, D. Forest, V. Dolique, L. Mereni, C. Michel, L. Pinard, B. Sassolas, J. Teillon, and G. Cagnoli(2020-05)Amorphous optical coatings of present gravitational-wave interferometers.Classical and Quantum Gravity37(9),pp. 095004.External Links:Document,1909.03737Cited by:§III.
- [31]H. Grote, K. Danzmann, K. L. Dooley, R. Schnabel, J. Slutsky, and H. Vahlbruch(2013)First Long-Term Application of Squeezed States of Light in a Gravitational-Wave Observatory.Phys. Rev. Lett.110(18),pp. 181101.External Links:1302.2188,DocumentCited by:§I,§IV.
- [32]P. Hello and J. Vinet(1990)Analytical models of thermal aberrations in massive mirrors heated by high power laser beams.Journal de Physique51(12),pp. 1267–1282.External Links:ISSN 0302-0738,DocumentCited by:Appendix D,§I,Figure 3,§III.1,§III.
- [33]P. Hello and J. Vinet(1990)Analytical models of transient thermoelastic deformations of mirrors heated by high power cw laser beams.J. Phys. France51(20),pp. 2243–2261.External Links:Document,LinkCited by:Appendix D,§I,§III.1,§III.
- [34]W. Jiaet al.(2024)Squeezing the quantum noise of a gravitational-wave detector below the standard quantum limit.Science385(6715),pp. ado8069.External Links:2404.14569,DocumentCited by:Appendix A,§I.
- [35]H. J. Kimble, Y. Levin, A. B. Matsko, K. S. Thorne, and S. P. Vyatchanin(2001-12)Conversion of conventional gravitational-wave interferometers into quantum nondemolition interferometers by modifying their input and/or output optics.Phys. Rev. D65(2),pp. 022002.External Links:Document,gr-qc/0008026Cited by:Figure 9,§IV,§IV.2.
- [36]P. Kwee, J. Miller, T. Isogai, L. Barsotti, and M. Evans(2014-09)Decoherence and degradation of squeezed states in quantum filter cavities.Phys. Rev. D90(6),pp. 062006.External Links:Document,1704.03531Cited by:Appendix D,§I,itemΩsqlrse\Omega_{\text{sql}}^{\text{rse}}SQL frequencyEq.16,§IV.2.
- [37]J. Loughet al.(2021)First Demonstration of 6 dB Quantum Noise Reduction in a Kilometer Scale Gravitational Wave Observatory.Phys. Rev. Lett.126(4),pp. 041102.External Links:2005.10292,DocumentCited by:§I,§IV.
- [38]D. Martynovet al.(2019)Exploring the sensitivity of gravitational wave detectors to neutron star physics.Phys. Rev. D99(10),pp. 102004.External Links:1901.03885,DocumentCited by:§IV.1.3.
- [39]L. McCulleret al.(2020)Frequency-Dependent Squeezing for Advanced LIGO.Phys. Rev. Lett.124(17),pp. 171102.External Links:2003.13443,DocumentCited by:§I,§IV,§IV.2,§IV.
- [40]L. McCulleret al.(2021)LIGO’s quantum response to squeezed states.Phys. Rev. D104(6),pp. 062006.External Links:2105.12052,DocumentCited by:Appendix A,Appendix A,Appendix A,Appendix A,Appendix A,Appendix C,Appendix D,Appendix D,§I,§I,§II.2,itemΩsqlrse\Omega_{\text{sql}}^{\text{rse}}SQL frequencyEq.16,§IV,§IV,§IV,§IV.2,§IV.3,§IV.4,§IV.4,§IV.4,§IV.4,§IV,§V,footnote 10,footnote 11,footnote 18,footnote 2.
- [41]B. J. Meers and K. A. Strain(1991-05)Wave-front distortion in laser-interferometric gravitational-wave detectors.Phys. Rev. D43(10),pp. 3117–3130.External Links:DocumentCited by:§II.2.
- [42]B. J. Meers(1988-10)Recycling in laser-interferometric gravitational-wave detectors.Phys. Rev. D38(8),pp. 2317–2326.External Links:DocumentCited by:§II.1,§II.
- [43]H. Miao, N. D. Smith, and M. Evans(2019-01)Quantum Limit for Laser Interferometric Gravitational-Wave Detectors from Optical Dissipation.Physical Review X9(1),pp. 011053.External Links:Document,1807.11734Cited by:§IV.
- [44]J. Mizuno, K. A. Strain, P. G. Nelson, J. M. Chen, R. Schilling, A. Rüdiger, W. Winkler, and K. Danzmann(1993-04)Resonant sideband extraction: a new configuration for interferometric gravitational wave detectors.Physics Letters A175(5),pp. 273–276.External Links:DocumentCited by:§II.1,§II.
- [45]A. Perreca, A. Brooks, J. Richardson, D. Toyra, and R. Smith(2020)Analysis and visualization of the output mode-matching requirements for squeezing in Advanced LIGO and future gravitational wave detectors.Phys. Rev. D101(10),pp. 102005.External Links:2001.10132,DocumentCited by:§III.1.
- [46]Post-O5 Study Group(2023)Report of the LSC Post-O5 Study Group.Technical NoteTechnical ReportLIGO-T2200287.External Links:LinkCited by:§I.
- [47]M. Rakhmanov, J. D. Romano, and J. T. Whelan(2008)High-frequency corrections to the detector response and their effect on searches for gravitational waves.Class. Quant. Grav.25,pp. 184017.External Links:0808.3805,DocumentCited by:footnote 8.
- [48]A. Rocchi, E. Coccia, V. Fafone, V. Malvezzi, Y. Minenkov, and L. Sperandio(2012)Thermal effects and their compensation in advanced Virgo.J. Phys. Conf. Ser.363,pp. 012016.External Links:DocumentCited by:Appendix D,§III.2.
- [49]A. E. Siegman(1986)Lasers.Cited by:§III.1,§III.1,§IV.2.2,§IV.2.2,footnote 16.
- [50]V. Srivastava, D. Davis, K. Kuns, P. Landry, S. Ballmer, M. Evans, E. D. Hall, J. Read, and B. S. Sathyaprakash(2022)Science-driven Tunable Design of Cosmic Explorer Detectors.Astrophys. J.931(1),pp. 22.External Links:2201.10668,DocumentCited by:§IV.1.3,footnote 12.
- [51]V. Srivastavaet al.(2022)Piezo-deformable mirrors for active mode matching in advanced LIGO.Opt. Express30(7),pp. 10491–10501.External Links:2110.00674,DocumentCited by:§IV.4.
- [52]K. A. Strain, K. Danzmann, J. Mizuno, P. G. Nelson, A. Rüdiger, R. Schilling, and W. Winkler(1994-10)Thermal lensing in recycling interferometric gravitational wave detectors.Physics Letters A194(1),pp. 124–132.External Links:ISSN 0375-9601,DocumentCited by:§III.1.
- [53]The VIRGO Collaboration(2022)Virgo_nEXT: Beyond the AdV+ project A concept study.Technical NoteTechnical ReportVIR-0497A-22.Cited by:§I.
- [54]D. Töyrä, D. D. Brown, M. Davis, S. Song, A. Wormald, J. Harms, H. Miao, and A. Freise(2017)Multi-spatial-mode effects in squeezed-light-enhanced interferometric gravitational wave detectors.Phys. Rev. D96(2),pp. 022006.External Links:1704.08237,DocumentCited by:footnote 9.
- [55]M. Tseet al.(2019)Quantum-Enhanced Advanced LIGO Detectors in the Era of Gravitational-Wave Astronomy.Phys. Rev. Lett.123(23),pp. 231107.External Links:DocumentCited by:§I,§IV.
- [56]J. Vinet(2009)On special optical modes and thermal issues in advanced gravitational wave interferometric detectors.Living Rev. Rel.12,pp. 5.External Links:DocumentCited by:Appendix D,§I,§III.1,§III.
- [57]W. Winkler, K. Danzmann, A. Ruediger, and R. Schilling(1991)Heating by optical absorption and the performance of interferometric gravitational wave detectors.Phys. Rev. A44,pp. 7022–7036.External Links:DocumentCited by:§III.1.
- [58]Y. Zhaoet al.(2020)Frequency-Dependent Squeezed Vacuum Source for Broadband Quantum Noise Reduction in Advanced Gravitational-Wave Detectors.Phys. Rev. Lett.124(17),pp. 171101.External Links:2003.10672,DocumentCited by:§I,§IV,§IV.2,§IV.

## 


- 


Major funding support from
