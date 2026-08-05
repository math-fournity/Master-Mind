# Simulating neural network criticality and resource dynamics with Rydberg gases

**arXiv ID**: 2607.16368v2
**Authors**: Patrick Mischke, Herwig Ott, Michael Fleischhauer, Thomas Niederprüm
**Published**: 2026-07-17
**Categories**: physics.atom-ph, cond-mat.quant-gas, quant-ph
**HTML URL**: https://arxiv.org/html/2607.16368v2

## Abstract

Efficient operation of neural networks has been linked to criticality in their underlying non-equilibrium excitation dynamics. However, obtaining experimental evidence of this conjecture remains challenging due to limited control and undersampling in biological systems. Here, we experimentally explore neural network criticality using an ultracold Rydberg gas as a highly controllable simulator. We highlight the similarity of the excitation spreading via Rydberg facilitation and the synaptic connection of spiking activity of neurons, giving rise to distinct absorbing and active phases. We systematically explore and resolve criticality criteria, including power-law scaling of excitation avalanches and the emergence of universal avalanche shape collapse. Crucially, we implement a controlled gain mechanism to compensate for atom loss, mimicking metabolic resource replenishment and stabilizing the system in a controlled non-equilibrium steady state. We find peak temporal correlations at the critical point and stochastic oscillations with dragon king avalanches in the active phase, consistent with predictions for systems orbiting criticality. Our work establishes facilitated Rydberg gases as a platform for investigating criticality, resource dynamics, and emergent oscillations in neural networks.

## Full Text

Simulating neural network criticality and resource dynamics with Rydberg gases

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- License: CC BY 4.0arXiv:2607.16368v2 [physics.atom-ph] 21 Jul 2026

## Simulating neural network criticality and resource dynamics with Rydberg gasesPatrick Mischkeagott-publication@physik.rptu.deRPTU University Kaiserslautern-Landau, Department of Physics and State Research Center OPTIMAS, Kaiserslautern, GermanyMax Planck Graduate Center with Johannes Gutenberg University Mainz (MPGC), 55128 Mainz, GermanyHerwig OttRPTU University Kaiserslautern-Landau, Department of Physics and State Research Center OPTIMAS, Kaiserslautern, GermanyMichael FleischhauerRPTU University Kaiserslautern-Landau, Department of Physics and State Research Center OPTIMAS, Kaiserslautern, GermanyThomas NiederprümRPTU University Kaiserslautern-Landau, Department of Physics and State Research Center OPTIMAS, Kaiserslautern, Germany

## Abstract

Efficient operation of neural networks has been linked to criticality in their underlying non-equilibrium excitation dynamics.
However, obtaining experimental evidence of this conjecture remains challenging due to limited control and undersampling in biological systems.
Here, we experimentally explore neural network criticality using an ultracold Rydberg gas as a highly controllable simulator.
We highlight the similarity of the excitation spreading via Rydberg facilitation and the synaptic connection of spiking activity of neurons, giving rise to distinct absorbing and active phases.
We systematically explore and resolve criticality criteria, including power-law scaling of excitation avalanches and the emergence of universal avalanche shape collapse.
Crucially, we implement a controlled gain mechanism to compensate for atom loss, mimicking metabolic resource replenishment and stabilizing the system in a controlled non-equilibrium steady state.
We find peak temporal correlations at the critical point and stochastic oscillations with dragon king avalanches in the active phase, consistent with predictions for systems orbiting criticality.
Our work establishes facilitated Rydberg gases as a platform for investigating criticality, resource dynamics, and emergent oscillations in neural networks.

## Introduction

In recent years, converging evidence has been obtained that efficient operation of neural networks is connected to criticality in the underlying non-equilibrium excitation dynamics[1,2,3,4,5,6,7,8].
In particular, it has been shown that the ability of neural networks to react to very different input magnitudes (dynamic range)[9,10,11], the ability to detect very small input changes (susceptibility)[12], and the ability to learn[4]maximize in the presence of criticality.
Even more, the shortcomings of current artificial deep neural networks with respect to robustness, efficiency, and pathologies in comparison to their biological counterparts might indicate that operation in the vicinity of a critical point is possibly a crucial ingredient for proper function[13].
On the other hand, it has been questioned whether neural networks truly exhibit a sharp critical point combined with a self-organization mechanism, or whether an extended long-range ordered phase instead gives rise to a similar phenomenology[14,15].
Moreover, the dynamic adaptation of the network through consumption and replenishment of metabolic resources has been identified as a process relevant to the phase space dynamics in the vicinity of the critical point[16,17,18].
It is thus a field of intense study to elucidate the role of criticality in such networks and how phenomena like, e.g., stochastic oscillations[19]and dragon king avalanches[20,21]arise in them.
While many of these phenomena are clearly visible in numerical models, it is challenging to experimentally study the role of criticality in physical realizations of neural networks.
At present, research on this important question is largely driven by comparing predictions of a broad set of numerical models with different initial assumptions to a rather small set of experimental data taken from biological samples.
However, these experiments typically suffer from undersampling and the lack of suitable fine-grained control parameters to judge how well a certain numerical model fits the studied system.Figure 1:(a)The dynamics of a neural network is based on active neurons (yellow) that activate connected neurons (light green) via synaptic activation (purple), leading to cascaded, spiking activity of the network.
Analogously, in an ultracold gas, an emergent local network (purple lines) is formed by those ground state atoms (green) that are approximately in the facilitation distancerfacr_{\mathrm{fac}}(purple circle).
Through Rydberg facilitation an existing excitation (yellow) can efficiently spread to connected nodes (light green) of the network, leading to excitation cascades/avalanches in the network.(b)The synaptic process in the simulator arises through Rydberg facilitation which off-resonantly couples one atom from a pair of atoms in the|g⟩\ket{g}state to form the pair state|g​r⟩\ket{gr}or|r​g⟩\ket{rg}.
Due to the strong interaction between two Rydberg atoms, the energy of the doubly excited|r​r⟩\ket{rr}state depends on the distance between the atoms and the second excitation only occurs in the facilitation distancerfacr_{\mathrm{fac}}where the driving laser with Rabi frequencyΩ\Omegabecomes resonant.
Via optical pumping atoms can be continuously transferred from the facilitation-inactive reservoir state|s⟩\ket{s}into the|g⟩\ket{g}state and replace lost atoms.(c)Typical integrated activity signal obtained from the simulator close to the critical point. The signal shows characteristic features such as non-Poissonian spiking patterns, burst-like avalanches and variable inter-spike intervals.

We address these challenges by building a physical simulator for critical neural network dynamics using a bottom-up approach.
By starting from well-controlled particles with tunable interactions we create an accessible and controllable many-body system that is able to simulate the essential features of neural network criticality and its dynamics.
To accurately implement the proper criticality features, our simulator exhibits the same kind of absorbing state phase transition, possesses an inhibition channel which scales with the activity, and has a controllable resource replenishment mechanism which stabilizes the operation near the critical point.
Here, we show that our simulator provides these ingredients through replicating the non-linear excitation spreading in neural networks in combination with a tailored gain process, giving rise to a non-equilibrium phase transition with high control over the microscopic degrees of freedom and a controlled resource replenishment which allows us to stabilize the system in the active phase and to study long-term dynamics of the system in the vicinity of the critical point.

## Neural network simulator

In our simulator, the most basic conceptual elements, the neurons, are replaced by the individual atoms in an ultracold gas (Fig.1a).
The atoms can either be in the ground state|g⟩\ket{g}, corresponding to an inactive neuron, or in the excited state|r⟩\ket{r}, representing an active (firing) neuron.
The synaptic connection is realized by the Rydberg facilitation process[22,23], where an active atom, together with a suitable global driving laser, can induce the activation of another atom at the facilitation distancerfac=C6Δ6r_{\mathrm{fac}}=\sqrt[6]{\frac{C_{6}}{\Delta}}(see Fig.1b).
This facilitation criterion defines spherical shells around each active atom, in which the activation of other atoms can take place.
As a result, a network with dynamic and local connectivity emerges from those atoms in the gas that have a matching distance (Fig.1a).
Since the atoms in our experiment are confined as an ultracold gas in a crossed optical dipole trap (see methods), the resulting network structure has the node degree distribution of an Erdős-Rényi random graph[24,25].
Furthermore, the inherent dephasing in the facilitation-based offspring creation leads to a classical contact process[26].
The competition between facilitated excitation and decay of the Rydberg state maps the system onto the susceptible-infected-susceptible (SIS) epidemic model which features an absorbing state phase transition that shows a critical point[25,27,28,29,30]and gives rise to activation avalanches and epidemic growth of excitations[31]. Near the critical point of this phase transition, characteristic non-Poissonian spiking patterns and burst-like avalanches of activity (see Fig.1c) emerge.

A biological neural network consumes metabolic resources that have to be replenished for stable long-term operation, e.g., via the glial network.
This process is known to play a decisive role in determining the system’s critical behavior[17].
It is therefore crucial to implement such a mechanism in a simulator.
As biological neural networks and facilitated Rydberg gases share strong conceptual similarities not only on a general level but also on a microscopic level (Fig.1a), this can be achieved in a straightforward way: much like a neuron that can fire several times, a single atom can perform multiple cycles of excitation and decay to the ground state.
Eventually, an excited atom will, however, be ionized or decays to an uncoupled ground state|g1⟩\ket{g_{1}}effectively removing it from the system.
Atom loss in our system serves as a functional proxy for the net reduction of excitable units in biological networks, which arises from refractory periods, synaptic depression, and metabolic constraints rather than cell loss.
As the atom density shrinks, the likelihood of excitation spreading decreases.
This loss mechanism leads to a self-organization process that pushes the system from the active phase towards the critical point[30,32]and, on a slower timescale, deeper into the absorbing state.
We compensate this loss process by adding a dedicated gain channel based on optical pumping, which stabilizes and fine-tunes the system in the vicinity of the critical point.
Both processes together allow us to capture critical neural network dynamics[33,15]with a control knob for all relevant system parameters.Figure 2:2D phase diagrams of the system for(a)varied particle density and driving laser power with fixed detuningΔ=2​π⋅40MHz\Delta=2\pi\cdot$40\text{\,}\mathrm{MHz}$or(c)driving laser detuning with fixed driving strengthΩ=5.5MHz\Omega=$5.5\text{\,}\mathrm{MHz}$.
The system is always prepared at a certain densitynn(y-axis) and the measured activityϕ\phifor a1ms1\text{\,}\mathrm{ms}excitation pulse of Rabi frequencyΩ\Omegaand detuningΔ\Deltais shown as color code.
The red star indicates the position of the measurement shown in Fig.4with maximal fluctuations.
In the central panel(b)a dedicated measurement along a vertical cut on a linear activity scale is shown along with a fit of the power-law scalingϕ=(n−nc)β\phi=(n-n_{c})^{\beta}(light green), yieldingnc=20.9​(7)​μ​m−3n_{c}=20.9(7)\,\mathrm{\mu m}^{-3}andβ=0.78​(2)\beta=0.78(2).
The yellow dashed line denotes the predicted phase transition in a parameter-free model of the spreading process (see Methods).
Additional features arise in theΔ\Delta-dependent measurement because pair states atΔ≈135MHz\Delta\approx$135\text{\,}\mathrm{MHz}$causing deviations from ther−6r^{-6}interaction.

## Proximity to a Critical Point

While well established frameworks exist to describe equilibrium phase transitions and the connected criticality, the non-equilibrium case has less stringent theoretical foundation.
In addition, the presence of dissipative processes like resource consumption, or atom loss in our case, complicates the situation as the system might not be able to actually reside at the critical point.
We here follow Ref.[12], which has put forward six criteria (I - VI) that have to be fulfilled in such systems.

The first three criteria impose the presence of distinct phases characterized by an order parameter (III), a control parameter to tune between them (II) and a transition between them at a branching ratio of 1 (I) where the branching ratio is the average number of offspring events per parent event in an avalanche and can thus serve as an indicator of whether a system is subcritical (ratio < 1), critical (ratio = 1), or supercritical (ratio > 1).
These criteria can be simultaneously demonstrated by carefully measuring the phase diagram and comparing it to the calculated branching ratio (see methods).

The experimental phase diagrams (see methods for an explanation of the experimental protocol) are obtained by varying different control parameters and measuring the system activityϕ\phi(Fig.2).
One can clearly identify the phase transition between the absorbing phase, where the activity is close to zero, and the active phase, where it is large.
Thereby, the activity serves as the order parameter of the phase transition (criterion (III)).

To show that the branching ratio at the transition is close to 1 (criterion (I)), we numerically calculate it in a mean-field model without any free fit parameters.
The details of the model are outlined in the methods section.
The transition point resulting from the model is shown as a yellow line in Fig.2and is in good agreement with the measured onset of activity across a wide range of the phase diagram.

The ground state densitynntakes the role of a control parameter that tunes across the critical point (criterion (II)).
The Rabi frequencyΩ\Omegaand the detuningΔ\Deltadefine the systems characteristics in a similar way, i.e. they tune the critical densityncn_{c}, and are experimentally easily accessible.
While tuning across the phase transition using these parameters is possible, additional effects such as power broadening and the vicinity of nearby Rydberg pair states make quantitative evaluations easier when choosing the density as a control parameter.
Nevertheless, the ability to tune those additional two parameters in the Rydberg system enhances the control over the microscopic spreading process to a level which is hard or even impossible to achieve in other platforms.Figure 3:Top Row: Power-law behavior in the avalanche distributions close to the critical point:
distribution of(a)avalanche magnitudesP​(m)P(m)and(b)avalanche durationsP​(t)P(t).
We fit power-law exponents ofτm=1.72\tau_{m}=1.72andτt=2.31\tau_{t}=2.31(light green lines).
Panel(c)shows all recorded avalanches with their respective durationttand magnitudemmas green circles with the crosses denoting the mean value⟨m⟩t\langle m\rangle_{t}for each discrete durationtt.
We fit a power-law exponent ofγ=1.77\gamma=1.77(light green line).
Data points with insufficient statistics (gray) have been omitted for fitting the exponent.
Bottom row: Avalanche shapes close to the critical point.(d)Averaged signal of all avalanches of a specific durationTTrangingT=0.1msT=$0.1\text{\,}\mathrm{ms}$(bright green) toT=0.7msT=$0.7\text{\,}\mathrm{ms}$.(e)Collapse of the avalanche shapes shown in (d) by normalizing the duration and rescaling the amplitude byϕ/Tγ−1\phi/T^{\gamma-1}with the value forγ\gammaobtained in (c).
Due to missing temporal resolution, the first two durations have been omitted.

Three more criteria target the scale-invariance of a system at criticality by requiring the existence of power laws (IV), a defined scaling relation between them (V), and a universal scaling function to collapse, e.g., avalanche shapes (VI).
Observing power-laws is often considered one of the key features of criticality[30].
In addition to the scaling of the order parameter,ϕ=(n−nc)β\phi=(n-n_{c})^{\beta}(see fit in Fig.2), excitation avalanches are expected to show power-law scaling:
The distributionsP​(m)P(m)andP​(t)P(t)of avalanches with magnitudemmor durationttare scaling with the exponentsP​(m)∼m−τmP(m)\sim m^{-\tau_{m}}andP​(t)∼t−τtP(t)\sim t^{-\tau_{t}}.
The relation between magnitude and duration of an avalanche should also follow a power-law with⟨m⟩t∼tγ\langle m\rangle_{t}\sim t^{\gamma}, withγ≈τt−1τm−1\gamma\approx\frac{\tau_{t}-1}{\tau_{m}-1}[34,35].
Fig.3(a) and (b) show the avalanche distributions when preparing the system at a density close to the critical density.
Both distributions follow power laws and fulfill the exponent relation forγ\gamma(criterion (IV) and (V)).
The measuredβ\betaexponent is compatible with the expectations for (anomalous) directed percolation within the error bounds[36], while the avalanche exponents are above theoretically predicted values.
Universal exponents in non-equilibrium transitions can depend on additional parameters.
For example, we have shown previously that the avalanche exponents increase from the expected value when dissipation is present[25].
In this regard our experiment qualitatively agrees well with observations on biological neural networks that frequently show varying avalanche exponents, while the exponent relations remains valid[37].
Such systems were named quasi-critical, as they are near a critical point, but don’t allow for direct extraction of universal exponents.

Scale invariance close to the critical point implies that certain self-similar patterns are observable when looking at different sizes of the same observable.
Most prominently, the temporal activity pattern of an avalanche, averaged over all avalanches with a certain durationTT, should be independent of its duration.
Our experimental results are displayed in Fig.3(e), where we scale all measured avalanches to the same duration and show that the activity, rescaled with1Tγ−1\frac{1}{T^{\gamma-1}}, collapses on a single curve (criterion (VI)).
The avalanche shape resembles a skewed parabola that has been observed in other systems as well[38,34,8,6].
These results demonstrate that facilitated Rydberg gases possess all the necessary properties to simulate critical dynamics in realistic neural networks.

## Resource ReplenishmentFigure 4:(a)Long-term evolution of the system’s activity averaged across 90 realizations per curve with a constant gain rate.
The collapse of the average activity for different starting densities aftert≈20mst\approx$20\text{\,}\mathrm{ms}$(dashed black line) shows that the system is attracted towards and stabilizes at the dynamical steady state where the applied constant gain equals the intrinsic loss.
The inset shows the opposing case: Different steady states can be achieved with different applied gain.(b)Temporal correlation functiong(2)​(τ)g^{(2)}(\tau)extracted at steady states close to criticality (light green, taken at position of the marker in Fig.2a) and slightly in the active phase (dark green).
Close to criticality the correlations show strong bunching ofg(2)​(τ=0)=13.2g^{(2)}(\tau=0)=13.2with a characteristic timescale much longer than the lifetime of a single Rydberg excitation.
Additionally, in the active phase, these correlations are followed by a clear anti-bunching for delays betweenτ≈0.5ms\tau\approx$0.5\text{\,}\mathrm{ms}$andτ≈4ms\tau\approx$4\text{\,}\mathrm{ms}$, indicating stochastic oscillations in the activity of the system.
Inset:g(2)​(τ=0)g^{(2)}(\tau=0)at different points in the phase diagram.
Light green points without gain, dark green points with gain stabilization.
The correlations peak close to the critical point.
Since the density that we reach at the steady state is not always known, we characterize the position across the phase transition by the mean activityϕ¯\bar{\phi}of the steady state.(c)Dragon king avalanches appearing in the magnitude distribution in the active phase.
Avalanches withm≈500m\approx 500occur orders of magnitude more frequently than expected from an extrapolated power law.
To improve visibility, points withm>67m>67show averages for intervals of width 10.

To accurately simulate the long-term criticality dynamics of biological neural networks around the critical point it is necessary to also consider resource replenishment processes that counteract dissipation.
Multiple mechanisms like inhibitory neurons provide short term stability and protection against run-away activity, but metabolic resource distribution is a key factor on a timescale much longer than the firing dynamics of the neurons[17].
Analogous to this metabolic resource consumption, atom loss in our Rydberg system takes place on a longer timescale than the facilitation dynamics and reduces the average probability to spread an excitation.
We compensate for this resource consumption, i.e. atom loss, by using the facilitation-inactiveF=1F=1ground state as a reservoir from which we optically pump atoms into theF=2F=2state that can be facilitated (see Fig.1b).
Movement of the atoms compensates local density variations and has been described as hydrodynamic stabilization mechanism for short time scales[32], while the pump process controls the global density on longer time scales.
Adjusting the effective gain rate via the strength of optical pumping, we tune the equilibrium between consumption and replenishment of resources and thus set the position of the steady state in the phase diagram.
For a given gain, the system then moves towards the same steady state irrespective of the initial position set by differing initial densities (see Fig.4a).
Similarly, it evolves from a common starting point to different steady states if different effective gain rates are set (see inset of Fig.4a).

With this crucial ingredient implemented as an additional tuning knob, we study the system’s long-term dynamics by analyzing the temporal correlations of the driven system in the steady state.
Fig.4shows theg(2)​(τ)g^{(2)}(\tau)temporal correlation function of firing events for two different points in the phase diagram: one close to the critical point and one slightly in the active phase.
For both points a strong instantaneous correlation of excitation events (bunching) atτ=0\tau=0appears, reflecting the excitation cascades driven by the non-linear synaptic connection implemented through facilitation.
Analyzing this bunching behavior ing(2)​(τ=0)g^{(2)}(\tau=0)across the phase transition reveals that the correlations as a function of the mean activityϕ¯\bar{\phi}show a clear peak structure (inset in Fig.4).
The position of maximum fluctuations is shown as red marker in the phase diagram Fig.2.
It is both close to the critical point predicted by the branching ratio calculations and the steep increase in the activity from​10−3MHz{10}^{-3}\text{\,}\mathrm{MHz}to​10−1MHz{10}^{-1}\text{\,}\mathrm{MHz}.
This demonstrates that the amount of correlations is a suitable measure to pinpoint the phase transition in neural networks.

While the strength of the correlations maximizes at the critical point,
correlation times do not show such a pronounced peak structure due to limited separation of time scales between facilitation, decay and pump processes.
In the vicinity of the critical point, this correlation relaxes on a timescale ofτ≈150µ​s\tau\approx$150\text{\,}\mathrm{\SIUnitSymbolMicro s}$, much longer than the lifetime of an individual Rydberg atom (≈50µ​s\approx$50\text{\,}\mathrm{\SIUnitSymbolMicro s}$), but compatible with the average loss timescale after multiple excitation cycles.
In the active phase, the correlation drops on a similar timescale but does not directly relax to an uncorrelated state.
It rather shows an oscillatory behavior that turns into an anti-correlation for an even longer timescale ofτrepl≈2ms\tau_{\mathrm{repl}}\approx$2\text{\,}\mathrm{ms}$.
As seen from Fig.4, the averaged activity across multiple experiment repetitions is constant, indicating that these oscillations are a stochastic and intrinsic property of the system and not externally induced.
This oscillatory behavior around the steady state driven by stochastic perturbations was numerically predicted to occur in neural networks when the system orbits the critical point[19,39,40,41,42].
These arise when, following a stochastic seed event in an over-critical system, the activity increases rapidly and the associated dissipation causes the density to rapidly fall below the critical point - the avalanche leaves a depleted region behind.
When the outburst eventually ends, the system is below the critical point and starts to accumulate density on a longer timescale due to the gain mechanism, eventually enabling a start of the next oscillatory cycle triggered by a stochastically appearing seed event.
As known from the numerical simulations[19], this behavior is associated with so-called dragon king avalanches: Outbursts with a large magnitude, that occur more frequently than an extrapolation of the probability distribution of the smaller events would predict.
When analyzing the probability distribution for different avalanche magnitudes slightly in the active phase (Fig.4c), we can demonstrate also this phenomenon predicted to appear in neuronal networks to be present in our simulator.

## Discussion

Our findings establish facilitated Rydberg gases as a versatile experimental platform for dissecting the interplay between criticality, resource dynamics, and emergent long-term features in neural networks.
The ability to map out the phase diagram helps to understand how self-organizing dynamics allow a physical system to operate near the critical point.
Our work opens a way of qualitatively investigating stochastic oscillations and the appearance of dragon king avalanches.
Rapid progress on tweezer platforms for ultracold atoms[43]opens the prospect of creating networks with full control over the network topology and the read-out.
While the measurements presented here rely on classical excitation spreading due to strong dephasing, the platform inherently supports coherent dynamics.
Future implementations tailored for coherent interactions could thus enable the study of quantum neural networks with10510^{5}nodes, regimes that remain out of reach for classical simulation.
In particular, this would allow studying the interplay between criticality and quantum entanglement.
Quantum entanglement in neural networks has been suggested as a relevant property in biological settings[44,45,46], but remains an open question.
Furthermore, the quantum mechanical nature of the facilitation process could be harnessed to improve computational features of the network[47].
Ultimately, this approach offers a pathway to significantly deepen our understanding of the fundamental working principles of neural networks and non-equilibrium critical systems.

## Methods

## Experimental Apparatus

To take the presented measurements we employ two-stage laser cooling in a 2D-MOT and 3D-MOT to prepare a cigar-shaped sample ofRb87{}^{87}\mathrm{Rb}atoms inside a crossed optical dipole trap where we drive forced evaporation until we end up withN=5×105N=5\times 10^{5}atoms at trapping frequencies ofωx,y,z=2​π×(425,115,439)​Hz\omega_{x,y,z}=2\pi\times(425,115,439)\,$\mathrm{Hz}$and a temperature ofT=2.25µ​KT=$2.25\text{\,}\mathrm{\SIUnitSymbolMicro K}$.
All atoms are initially in the reservoir state|g0⟩=|s⟩≡|5​S1/2,F=1⟩\ket{g_{0}}=\ket{s}\equiv\ket{5\mathrm{S}_{1/2},\mathrm{F}=1}.

Using optical pumping via the5​P3/25\mathrm{P}_{3/2}state, we can transfer atoms in the|g⟩≡|5​S1/2,F=2⟩\ket{g}\equiv\ket{5\mathrm{S}_{1/2},\mathrm{F}=2}hyperfine ground state.
The repumping laser from the initial MOT phase serves as optical pumping laser.
Due to the better control over this parameter, the detuning of the pumping laser is used to control the pumping rate and a calibration measurement allows for a direct correspondence between laser detuning and global pumping rateγ\gamma.
When keeping up a constant gain rate over extended periods of time, the reservoir state|s⟩\ket{s}is depleted and thus the absolute pumping rate drops.
To compensate for this, the pumping laser is ramped according toγ​(t)=γ01−γ0​t\gamma(t)=\frac{\gamma_{0}}{1-\gamma_{0}t}to obtain a constant gain rateγ0\gamma_{0}for an extended time.

The|g⟩\ket{g}state is coupled to the|r⟩≡40​P3/2\ket{r}\equiv 40\mathrm{P}_{3/2}Rydberg state via a single photon transition by a297nm297\text{\,}\mathrm{nm}excitation laser that is focused to a Gaussian waist ofw0=100µ​mw_{0}=$100\text{\,}\mathrm{\SIUnitSymbolMicro m}$and linearly polarized.
External magnetic fields are compensated during the measurement such that the linear polarization of the excitation laser sets the quantization axis.
The laser globally illuminates the sample at an angle of 45° with respect to the long axis of the sample.
To allow for Rydberg facilitation and to suppress resonant excitation, a blue detuning ofΔ=2​π⋅(−15​⋯+175MHz)\Delta=2\pi\cdot(-15\dots+$175\text{\,}\mathrm{MHz}$)to the atomic Rydberg resonance can be set.
All measurements are taken withΔ=2​π⋅40MHz\Delta=2\pi\cdot$40\text{\,}\mathrm{MHz}$unless noted otherwise.
This leads to an adjustable facilitation distance ofrfac≈1.2µ​mr_{\mathrm{fac}}\approx$1.2\text{\,}\mathrm{\SIUnitSymbolMicro m}$(for40​P3/240\mathrm{P}_{3/2}andΔ=40MHz\Delta=$40\text{\,}\mathrm{MHz}$, withC6=0.111GHz​µ​m6C_{6}=$0.111\text{\,}\mathrm{G}\mathrm{Hz}\mathrm{\SIUnitSymbolMicro}\mathrm{m}^{6}$calculated using the pairinteraction software package[48]).
By changing the coupling laser power, the resonant coupling strength for atoms in the facilitation distance can be set in the rangeΩ=0​…​6.5MHz\Omega=0\dots$6.5\text{\,}\mathrm{MHz}$.
The coupling strengthΩ\Omegais calibrated by performing microwave spectroscopy on the|s⟩→|g⟩\ket{s}\rightarrow\ket{g}transition and observing the light shift for different coupling laser intensities.

While the detuning strongly suppresses excitations of atoms without a facilitation partner, off-resonant events still occur occasionally.
In comparison to neural networks, where input is typically from an external source, this results in an intrinsic seed process for excitations in the Rydberg system.

The loss of Rydberg atoms into ions through photoionization and associative ionization not only mimics the resource consumption, it also serves as a detection channel for the activity of the network, picking up discrete events comparable to electrodes for observing neural networks.
Rydberg atoms that eventually decay to ions after several iterations of excitation and decay, are guided to a time-resolved dynode detector with detection efficiencies ofηdet≈40%\eta_{\mathrm{det}}\approx 40\%using a small electric bias field.
The primary measurement signal is generated by binning the arrival of ions into bins with50µ​s50\text{\,}\mathrm{\SIUnitSymbolMicro s}duration.
The activity in counts per time unit is directly proportional to the Rydberg densitynRydn_{\mathrm{Ryd}}, where the proportionality factorη<1\eta<1depends on the decay rate, detection efficiency and trapping volume.
Our time-resolved measurement scheme with single count sensitivity allows us to identify individual avalanches, which is required to obtain the avalanche exponentsτ\tauandα\alpha.
To discriminate between avalanches, we consider an avalanche to end whenever there is an empty bin.

To measure the phase diagrams, we use the optical pumping process to prepare our system with ground state densitynnin the coupled state|g⟩\ket{g}while the excitation laser is off and subsequently switch on the excitation pulse at a set Rabi frequencyΩ\Omegaand detuningΔ\Deltafor a fixed duration of2ms2\text{\,}\mathrm{ms}.
This duration is chosen longer than the initial growth dynamics[31]and short enough that the density change due to atom loss, i.e. resource consumption, is limited.
Using absorption imaging in a time-of-flight scheme, we can measure atom number and temperature of the prepared sample in an independent measurement without excitation pulses.

## Calculation of Branching-Ratio

We consider the case of a test atom initially in the ground state and at distancerrfrom the seed atom, which decays with rateγ\gamma.
The dynamics of the test atom can be described in terms of the imbalancew=ρg​g−ρe​ew=\rho_{gg}-\rho_{ee}as given by the optical Bloch equations[49], wherew​(t)=w​(t,Ω,γ,γ∗,Δ′)w(t)=w(t,\Omega,\gamma,\gamma^{*},\Delta^{\prime})depends on the Rabi frequencyΩ\Omega, local detuningΔ′​(r)\Delta^{\prime}(r), decay rateγ\gammaand dephasingγ∗\gamma^{*}.
This allows to obtain the probabilityPfacP_{\mathrm{fac}}that the test atom is in the excited state at the time of decay:Pfac=∫0∞1−w2​γ​e−γ​t​𝑑tP_{\mathrm{fac}}=\int_{0}^{\infty}\frac{1-w}{2}\gamma e^{-\gamma t}dt

To obtain the branching ratioB​RBR, we calculate the number of atoms a given seed atom will have excited via the facilitation mechanism at the time of decay.
In a mean-field picture without correlations, this number can be obtained by integrating the probabilityPfacP_{\mathrm{fac}}over the volume of the system and the densitynnof ground state atoms.
The local detuning is given by the laser detuningΔ\Deltaand the Rydberg-Rydberg interaction asΔ′​(r)=Δ−C6r6\Delta^{\prime}(r)=\Delta-\frac{C_{6}}{r^{6}}:BR=∫R3n[Pfac(Ω,γ,γ∗,Δ′(r))−Pfac(Ω,γ,γ∗,Δ)]dVBR=\int_{R^{3}}n\left[P_{\mathrm{fac}}\left(\Omega,\gamma,\gamma*,\Delta^{\prime}(r)\right)-P_{\mathrm{fac}}\left(\Omega,\gamma,\gamma*,\Delta\right)\right]dV

As we are only interested in excitations via the facilitation mechanism, we subtract any off-resonant excitations that occur independently of the distance to our seed atom.
We numerically solve this equation forB​R=1BR=1to obtain the critical densityncn_{c}.
A more detailed derivation is given in the supplementary material.

## Acknowledgements

We would like to thank Volker Scheuss for helpful discussions and proofreading the manuscript.
The authors acknowledge financial support by the DFG within the collaborative research center TR 185 OSCAR (Number 277625399).
This work was also supported by the research initiative Quantum Computing for Artificial Intelligence (QC-AI) and by the Max Planck Graduate Center MPGC with the
University of Mainz.

## Data Availability

The data that support the plots within this paper and other findings of this study are publicly available[50].

## Author Contributions

P.M. performed the experiments and analyzed the data. P.M. and T.N. prepared the manuscript.
T.N. and H.O. and M.F. developed the concepts for the study.
T.N. and H.O. conceived and supervised the experiment.
All authors contributed to the data interpretation and final manuscript preparation.

## Competing financial interests

The authors declare no competing financial interests.

## References
- Langton [1990]C. G. Langton, Computation at the edge
of chaos: Phase transitions and emergent computation,Physica D: Nonlinear Phenomena42, 12 (1990).
- Beggs and Plenz [2003]J. M. Beggs and D. Plenz, Neuronal Avalanches in
Neocortical Circuits,Journal of Neuroscience23, 11167 (2003).
- Beggs [2007]J. M. Beggs, The criticality hypothesis:
How local cortical networks might optimize information processing,Philosophical Transactions of the Royal Society A: Mathematical,
Physical and Engineering Sciences366, 329 (2007).
- de Arcangelis and Herrmann [2010]L. de
Arcangelis and H. J. Herrmann, Learning as a phenomenon
occurring in a critical state,Proceedings of the National Academy of Sciences107, 3977 (2010).
- Klauset al.[2011]A. Klaus, S. Yu, and D. Plenz, Statistical Analyses Support Power Law
Distributions Found in Neuronal Avalanches,PLOS ONE6, e19779 (2011).
- Friedmanet al.[2012]N. Friedman, S. Ito,
B. A. W. Brinkman,
M. Shimono, R. E. L. DeVille, K. A. Dahmen, J. M. Beggs, and T. C. Butler, Universal Critical Dynamics in High Resolution
Neuronal Avalanche Data,Physical Review Letters108, 208102 (2012).
- Shew and Plenz [2013]W. L. Shew and D. Plenz, The Functional Benefits of
Criticality in the Cortex,The Neuroscientist19, 88 (2013).
- Fagerholmet al.[2015]E. D. Fagerholm, R. Lorenz,
G. Scott, M. Dinov, P. J. Hellyer, N. Mirzaei, C. Leeson, D. W. Carmichael, D. J. Sharp, W. L. Shew, and R. Leech, Cascades and Cognitive State:
Focused Attention Incurs Subcritical Dynamics,Journal of Neuroscience35, 4626 (2015).
- Kinouchi and Copelli [2006]O. Kinouchi and M. Copelli, Optimal dynamical range
of excitable networks at criticality,Nature Physics2, 348
(2006).
- Shewet al.[2009]W. L. Shew, H. Yang, T. Petermann, R. Roy, and D. Plenz, Neuronal avalanches imply maximum dynamic range in cortical networks
at criticality,The Journal of Neuroscience: The
Official Journal of the Society for Neuroscience29, 15595 (2009).
- Gautamet al.[2015]S. H. Gautam, T. T. Hoang,
K. McClanahan, S. K. Grady, and W. L. Shew, Maximizing Sensory Dynamic Range by Tuning the
Cortical State to Criticality,PLOS Computational Biology11, e1004576 (2015).
- Beggs [2022]J. M. Beggs,The Cortex and the Critical Point:
Understanding the Power of Emergence(The MIT Press, 2022).
- [13]S. Vock and C. Meisel,Critical dynamics governs deep learning,2507.08527.
- Sunet al.[2025]J. K.-C. Sun, C. Sipling, Y.-H. Zhang, and M. Di Ventra, Memory in neural activity:
Long-range order without criticality,Physical Review E112, 064401 (2025).
- Siplinget al.[2026]C. Sipling, Y.-H. Zhang, and M. Di Ventra, A critical assessment of the brain
criticality hypothesis, Trends
Openhttps://doi.org/10.1016/j.treopn.2026.06.001(2026).
- Robertset al.[2014]J. A. Roberts, K. K. Iyer,
S. Vanhatalo, and M. Breakspear, Critical role for resource constraints in neural
models, Frontiers in Systems
Neuroscience8,10.3389/fnsys.2014.00154(2014).
- Virkaret al.[2016]Y. S. Virkar, W. L. Shew,
J. G. Restrepo, and E. Ott, Feedback control stabilization of critical
dynamics via resource transport on multilayer networks: How glia enable
learning dynamics in the brain,Physical Review E94, 042310 (2016).
- Franovićet al.[2022]I. Franović, S. Eydam,
S. Yanchuk, and R. Berner, Collective Activity Bursting in a Population of
Excitable Units Adaptively Coupled to a Pool of Resources, Frontiers in Network Physiology2,10.3389/fnetp.2022.841829(2022).
- Kinouchiet al.[2019]O. Kinouchi, L. Brochini,
A. A. Costa, J. G. F. Campos, and M. Copelli, Stochastic oscillations and dragon king avalanches in
self-organized quasi-critical systems,Scientific Reports9, 3874 (2019).
- de
Arcangelis [2012]L. de
Arcangelis, Are dragon-king
neuronal avalanches dungeons for self-organized brain activity?,The European Physical Journal Special Topics205, 243 (2012).
- Mishraet al.[2018]A. Mishra, S. Saha,
M. Vigneshwaran, P. Pal, T. Kapitaniak, and S. K. Dana, Dragon-king-like extreme events in coupled bursting neurons,Physical Review E97, 062311 (2018).
- Ateset al.[2007]C. Ates, T. Pohl, T. Pattard, and J. M. Rost, Antiblockade in Rydberg Excitation of an Ultracold Lattice
Gas,Physical Review Letters98, 023002 (2007).
- Amthoret al.[2010]T. Amthor, C. Giese,
C. S. Hofmann, and M. Weidemüller, Evidence of Antiblockade in an
Ultracold Rydberg Gas,Physical Review Letters104, 013001 (2010).
- Rutten and Sanders [2021]D. Rutten and J. Sanders, Modeling Rydberg
gases using random sequential adsorption on random graphs,Physical Review A103, 033302 (2021).
- Ohleret al.[2025]S. Ohler, D. Brady,
P. Mischke, J. Bender, H. Ott, T. Niederprüm, W. Ripken, J. S. Otterbach, and M. Fleischhauer, Nonequilibrium universality of Rydberg-excitation spreading on a dynamic
network,Physical Review Research7, 033167 (2025).
- Leviet al.[2016]E. Levi, R. Gutiérrez, and I. Lesanovsky, Quantum
non-equilibrium dynamics of Rydberg gases in the presence of dephasing
noise of different strengths,Journal of Physics B: Atomic, Molecular and Optical
Physics49, 184003
(2016).
- Schemppet al.[2014]H. Schempp, G. Günter,
M. Robert-de-Saint-Vincent, C. S. Hofmann, D. Breyel, A. Komnik,
D. W. Schönleber,
M. Gärttner, J. Evers, S. Whitlock, and M. Weidemüller, Full Counting Statistics of Laser Excited Rydberg
Aggregates in a One-Dimensional Geometry,Physical Review Letters112, 013002 (2014).
- Malossiet al.[2014]N. Malossi, M. M. Valado,
S. Scotto, P. Huillery, P. Pillet, D. Ciampini, E. Arimondo, and O. Morsch, Full
Counting Statistics and Phase Diagram of a Dissipative Rydberg
Gas,Physical Review Letters113, 023006 (2014).
- Marcuzziet al.[2015]M. Marcuzzi, E. Levi,
W. Li, J. P. Garrahan, B. Olmos, and I. Lesanovsky, Non-equilibrium universality in the dynamics of
dissipative cold atomic gases,New Journal of Physics17, 072003 (2015).
- Helmrichet al.[2020]S. Helmrich, A. Arias,
G. Lochead, T. M. Wintermantel, M. Buchhold, S. Diehl, and S. Whitlock, Signatures of self-organized criticality in an ultracold atomic
gas,Nature577, 481 (2020).
- Wintermantelet al.[2021]T. M. Wintermantel, M. Buchhold, S. Shevate,
M. Morgado, Y. Wang, G. Lochead, S. Diehl, and S. Whitlock, Epidemic growth and Griffiths effects on an emergent network of excited
atoms,Nature Communications12, 103 (2021).
- Klockeet al.[2021]K. Klocke, T. M. Wintermantel, G. Lochead, S. Whitlock, and M. Buchhold, Hydrodynamic Stabilization of
Self-Organized Criticality in a Driven Rydberg Gas,Physical Review Letters126, 123401 (2021).
- Virkar [2020]Y. S. Virkar, Dynamic regulation of
resource transport induces criticality in interdependent networks of
excitable units, Physical
Review E101,10.1103/PhysRevE.101.022303(2020).
- Sethnaet al.[2001]J. P. Sethna, K. A. Dahmen, and C. R. Myers, Crackling noise,Nature410, 242
(2001).
- Marković and Gros [2014]D. Marković and C. Gros, Power laws and
self-organized criticality in theory and nature,Physics Reports Power Laws and
Self-Organized Criticality in Theory and Nature,536, 41 (2014).
- Bradyet al.[2024]D. Brady, S. Ohler,
J. Otterbach, and M. Fleischhauer, Anomalous Directed Percolation on
a Dynamic Network Using Rydberg Facilitation,Physical Review Letters133, 173401 (2024).
- Fosqueet al.[2021]L. J. Fosque, R. V. Williams-García, J. M. Beggs, and G. Ortiz, Evidence
for quasicritical brain dynamics,Phys. Rev. Lett.126, 098101 (2021).
- Spasojevićet al.[1996]D. Spasojević, S. Bukvić, S. Milošević, and H. E. Stanley, Barkhausen noise:
Elementary signals, power laws, and scaling relations,Physical Review E54, 2531 (1996).
- Fries [2015]P. Fries, Rhythms for Cognition:
Communication through Coherence,Neuron88, 220 (2015).
- Zanget al.[2024]J. Zang, S. Liu, P. Helson, and A. Kumar, Structural constraints on the emergence of oscillations in
multi-population neural networks,eLife12, RP88777 (2024).
- Marenduzzoet al.[2025]D. Marenduzzo, A. T. Brown, C. W. Miller, and G. J. Ackland, Oscillation in the SIRS model,Journal of Theoretical Biology611, 112169 (2025).
- Aliakbarian and Moghimi-Araghi [2026]N. Aliakbarian and S. Moghimi-Araghi, Transition from
self-organized criticality towards self-organized bistability,Physica A: Statistical Mechanics and its Applications682, 131148 (2026).
- Kaufman and Ni [2021]A. M. Kaufman and K.-K. Ni, Quantum science with optical
tweezer arrays of ultracold atoms and molecules,Nature Physics17, 1324 (2021).
- Kerskens and López Pérez [2022]C. M. Kerskens and D. López Pérez, Experimental
indications of non-classical brain functions,Journal of Physics Communications6, 105001 (2022).
- Liuet al.[2024]Z. Liu, Y.-C. Chen, and P. Ao, Entangled biphoton generation in the myelin
sheath,Physical Review E110, 024402 (2024).
- Svanishvili [2025]G. Svanishvili,Exploring Consciousness: Photon Entanglement and Neural
Communication - Premier Science(2025).
- Bravoet al.[2022]R. A. Bravo, K. Najafi,
X. Gao, and S. F. Yelin, Quantum Reservoir Computing Using Arrays of Rydberg
Atoms,PRX Quantum3, 030325 (2022).
- Weberet al.[2017]S. Weber, C. Tresp,
H. Menke, A. Urvoy, O. Firstenberg, H. P. Büchler, and S. Hofferberth, Calculation of Rydberg interaction potentials,Journal of Physics B: Atomic, Molecular and Optical
Physics50, 133001
(2017).
- Noh and Jhe [2010]H.-R. Noh and W. Jhe, Analytic solutions of the optical
Bloch equations,Optics Communications283, 2353 (2010).
- Mischkeet al.[2026]P. Mischke, T. Niederprüm, and H. Ott,Simulating neural network criticality and resource
dynamics with ultracold rydberg gases [dataset] (unpublished)(2026).

## 


- 


Major funding support from
