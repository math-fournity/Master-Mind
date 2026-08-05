# Surface Excitations, Energy Loss, and Decoherence in Electron Interferometry

**arXiv ID**: 2606.01004v2
**Authors**: David Kordahl
**Published**: 2026-05-31
**Categories**: physics.app-ph, cond-mat.mes-hall, quant-ph
**Comments**: 9 pages, 5 figures
**HTML URL**: https://arxiv.org/html/2606.01004v2

## Abstract

A recent pedagogical paper by Strauch concretely demonstrated how interaction-mediated entanglement can suppress fringe visibility in a one-dimensional model of the electron double-slit experiment. Here we extend that framework to model actual experimental data from electron biprism interferometry. Kerker et al. showed that the macroscopic QED model of Scheel and Buhmann successfully describes their measured results. We show that this Scheel-Buhmann model can be recovered from Strauch's simplified framework by employing a Markov approximation and including thermal effects. The resulting decoherence rate is expressed in terms of mode-resolved scattering probabilities familiar from electron energy-loss spectroscopy (EELS), directly relating EELS to decoherence. The thermal dependence is significant in its own right, as recent theoretical work suggests that visibility reduction could serve as a non-invasive thermal probe for nanoscale systems. This progression from a toy model, to a quantitative account of real data, to a measurement application offers a case study in how simplified models can be made experimentally relevant.

## Full Text

Surface Excitations, Energy Loss, and Decoherence in Electron Interferometry

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2606.01004v2 [physics.app-ph] 15 Jul 2026

## Surface Excitations, Energy Loss, and Decoherence in Electron InterferometryDavid Kordahldkordahl@centenary.eduDepartment of Physics and Engineering, Centenary College of Louisiana, Shreveport, LA 71104

## Abstract

A recent pedagogical paper by Strauch concretely demonstrated how interaction-mediated entanglement can suppress fringe visibility in a one-dimensional model of the electron double-slit experiment. Here we extend that framework to model actual experimental data from electron biprism interferometry. Kerkeret al.showed that the macroscopic QED model of Scheel and Buhmann successfully describes their measured results. We show that this Scheel-Buhmann model can be recovered from Strauch’s simplified framework by employing a Markov approximation and including thermal effects. The resulting decoherence rate is expressed in terms of mode-resolved scattering probabilities familiar from electron energy-loss spectroscopy (EELS), directly relating EELS to decoherence. The thermal dependence is significant in its own right, as recent theoretical work suggests that visibility reduction could serve as a non-invasive thermal probe for nanoscale systems. This progression from a toy model, to a quantitative account of real data, to a measurement application offers a case study in how simplified models can be made experimentally relevant.

## IIntroduction

In electron interferometry experiments, decoherence arises from extended electromagnetic interactions with material environments, entangling a system’s path degree of freedom with material excitations. This kind of interaction-based entanglement has been explored in pedagogical models emphasizing the role of subsystems18,11, and in treatments of decoherence in interferometric geometries9,13. Strauch20gives a particularly clear pedagogical illustration of entanglement-induced suppression of interference visibility in a simplified double-slit model. Here we show how this general approach can be extended into a quantitative account of real electron interferometry data, an example of how a simplified pedagogical model can be elaborated to become experimentally relevant.

This work is motivated by electron biprism interferometry experiments in which decoherence arises from electromagnetic coupling between an electron and a nearby dielectric surface. Sonnentag and Hasselbach19demonstrated that fringe visibility decreases as electron trajectories approach dielectric surfaces, and Kerkeret al.8showed that fringe visibility also decreases with increasing electron path separation. Kerkeret al.tested several theoretical descriptions and found the best agreement with the macroscopic QED treatment of Scheel and Buhmann17. We show that this model can be recovered from Strauch’s general framework once two extensions are imposed: a Markov approximation, and the inclusion of thermal occupation effects. This derivation highlights the connection of such results to well-established models in electron energy-loss spectroscopy (EELS).

By isolating the influence of different physical effects in such calculations, we can determine which mechanisms have the most observable importance. The central result of this analysis is that the decoherence rate can be written as a weighted integral over the differential EELS probability, with the weighting factor encoding the path distinguishability of the two electron trajectories. The structure of the final expression also suggests further experimental tests, including temperature-dependent visibility measurements. Recent theoretical work by Velascoet al.21,22makes a compelling case that the predicted decline in visibility with temperature could be exploited as a novel thermal probe at the nanoscale, a suggestion with which the present analysis concurs.

The remainder of the paper is organized as follows. Sec.IIintroduces a schematic framework for relating fringe visibility to entanglement-induced decoherence before discussing the effects of many surface modes, the Markov approximation, and thermal effects. Sec.IIIcontrasts models for the visibility decay and connects them to EELS models. Finally, Sec.IVmakes comparisons with published experimental results, and discusses what further tests could be carried out. Some calculational details have been relegated to an appendix. Taken together, these results illustrate how a pedagogical model can be refined into a quantitative tool, recovering an empirically successful theory and encouraging future experiments.

## IIVisibility Calculation Structure

This section derives the electron fringe visibility for the geometry shown in Fig.1. We adopt a Cartesian coordinate system in which a dielectric fills the half-spacey<0y<0, with vacuum iny≥0y\geq 0. Two split electron trajectories propagate predominantly along thezzdirection with velocityvv, separated laterally by a distanceddalongxx(i.e., atx=±d/2x=\pm d/2) and located at a heighty=by=babove the surface, over an interaction lengthLL.

We start with a schematic calculation modeled on Strauch’s discussion of the double-slit system (Sec.II.1) and show how to recover the fringe visibility for the toy model with a single excited mode (Sec.II.2). The discussion then broadens to show how the calculation changes when many surface modes are included (Sec.II.3), including the role of symmetry in simplifying the visibility (Sec.II.4). Finally, we note the role of a Markov approximation (Sec.II.5) and thermal state occupation (Sec.II.6) in connecting theory with experiment.Figure 1:Schematic of the interaction geometry. Two electron paths are separated by a distancedd, propagate at a heightbbabove the substrate with velocityvv, over a lengthLL.

## II.1Schematic Calculation

Before taking on the full case, we first consider a simplified calculation. Suppose an electron has been split into two distinct paths: arightside and aleftside, such that its𝐱⟂=(x,z)\mathbf{x}_{\perp}=(x,\,z)profile at a particularzztakes on the form|Ψe⟩=12​[ψR​(𝐱⟂)+ψL​(𝐱⟂)].\ket{\Psi_{e}}=\frac{1}{\sqrt{2}}\left[\psi_{\text{R}}(\mathbf{x}_{\perp})+\psi_{\text{L}}(\mathbf{x}_{\perp})\right].(1)

If the substrate begins in its ground state, we can write this “initial” state of the combined system as|Ψi⟩=|Ψe⟩⊗|0⟩=12​[ψR​(𝐱⟂)+ψL​(𝐱⟂)]​|0⟩.\ket{\Psi_{i}}=\ket{\Psi_{e}}\otimes\ket{0}=\frac{1}{\sqrt{2}}\left[\psi_{\text{R}}(\mathbf{x}_{\perp})+\psi_{\text{L}}(\mathbf{x}_{\perp})\right]\ket{0}.(2)

As will be discussed in detail below, the substrate will have many modes, indexed on their surface wavevector, but for simplicity consider a substrate with only two possible modes,|0⟩\ket{0}and|1⟩\ket{1}, representing internal degrees of freedom of the substrate. The “final” state of the combined system after all interactions between the electron and the substrate have effectively stopped can generically be written as|Ψf⟩≈+12​ψR​(𝐱⟂)​[cR​0​|0⟩+cR​1​|1⟩]+12​ψL​(𝐱⟂)​[cL​0​|0⟩+cL​1​|1⟩],\begin{split}\ket{\Psi_{f}}\approx&+\frac{1}{\sqrt{2}}\psi_{\text{R}}(\mathbf{x}_{\perp})\left[c_{\text{R}0}\ket{0}+c_{\text{R}1}\ket{1}\right]\\
&+\frac{1}{\sqrt{2}}\psi_{\text{L}}(\mathbf{x}_{\perp})\left[c_{\text{L}0}\ket{0}+c_{L1}\ket{1}\right],\end{split}(3)

where the coefficients follow the normalization conditions|cR​0|2+|cR​1|2=1and|cL​0|2+|cL​1|2=1.\begin{split}|c_{\text{R}0}|^{2}+|c_{\text{R}1}|^{2}&=1\quad\text{and}\\
|c_{\text{L}0}|^{2}+|c_{\text{L}1}|^{2}&=1.\end{split}(4)

Now suppose that, after the interaction time, the wave packetsψR​(𝐱⟂)\psi_{\text{R}}(\mathbf{x}_{\perp})andψL​(𝐱⟂)\psi_{\text{L}}(\mathbf{x}_{\perp})are brought to overlap (typically by the action of a downstream biprism). In this case,ψR​(𝐱⟂)\psi_{\text{R}}(\mathbf{x}_{\perp})andψL​(𝐱⟂)\psi_{\text{L}}(\mathbf{x}_{\perp})are related to one another asψR​(𝐱⟂)=ψ0​(𝐱⟂)andψL​(𝐱⟂)=ψ0∗​(𝐱⟂),\begin{split}\psi_{\text{R}}(\mathbf{x}_{\perp})&=\psi_{0}(\mathbf{x}_{\perp})\quad\text{and}\\
\psi_{\text{L}}(\mathbf{x}_{\perp})&=\psi_{0}^{*}(\mathbf{x}_{\perp}),\end{split}(5)

which implies that they have the same spatial profile but are traveling in opposite transverse directions, since complex conjugation reverses the sign of the transverse momentum phase factor.

What pattern of electrons will be observed in the observation plane? The probability density is computed by summing over the substrate modes:Pe​(𝐱⟂)=∑n=0,1⟨Ψf|(𝕀el⊗|n⟩​⟨n|)|Ψf⟩.P_{e}(\mathbf{x}_{\perp})=\sum_{n=0,1}\braket{\Psi_{f}|\left(\mathbb{I}_{\text{el}}\otimes\ket{n}\bra{n}\right)|\Psi_{f}}.(6)

The wavefunction in Eq.3has four terms, so the sum in Eq.6yields sixteen terms, but we can simplify using orthogonality of modes (e.g.,⟨0|1⟩=0\braket{0|1}=0, and⟨0|0⟩=1\braket{0|0}=1), normalization (Eq.4), and the relationship betweenψR\psi_{\text{R}}andψL\psi_{\text{L}}(Eq.5) to yieldPe​(𝐱⟂)=|ψ0​(𝐱⟂)|2+12​(ψ0​(𝐱⟂))2​[cR​0∗​cL​0+cR​1∗​cL​1]+12​(ψ0∗​(𝐱⟂))2​[cR​0​cL​0∗+cR​1​cL​1∗].\begin{split}P_{e}(\mathbf{x}_{\perp})=&|\psi_{0}(\mathbf{x}_{\perp})|^{2}\\
&+\frac{1}{2}(\psi_{0}(\mathbf{x}_{\perp}))^{2}\left[c^{*}_{\text{R}0}c_{\text{L}0}+c^{*}_{\text{R}1}c_{\text{L}1}\right]\\
&+\frac{1}{2}(\psi^{*}_{0}(\mathbf{x}_{\perp}))^{2}\left[c_{\text{R}0}c^{*}_{\text{L}0}+c_{\text{R}1}c^{*}_{\text{L}1}\right].\end{split}(7)

This form reveals the structure of the calculation. The first line is an average “background” term, and the others account for the possibility of an interference fringe.

## II.2Fringe Visibility

Notice the structure of the probability density in Eq.7. The second and third lines are complex conjugates of one another, so we can write this more neatly asPe​(𝐱⟂)=|ψ0​(𝐱⟂)|2+Re​[Γ​(ψ0​(𝐱⟂))2]P_{e}(\mathbf{x}_{\perp})=|\psi_{0}(\mathbf{x}_{\perp})|^{2}+\mathrm{Re}\left[\Gamma(\psi_{0}(\mathbf{x}_{\perp}))^{2}\right](8)

where the factorΓ\Gammais the (possibly complex) valueΓ=cR​0∗​cL​0+cR​1∗​cL​1.\Gamma=c^{*}_{\text{R}0}c_{\text{L}0}+c^{*}_{\text{R}1}c_{\text{L}1}.(9)

The magnitude ofΓ\Gammais the fringe visibility𝒱\mathcal{V}:𝒱=|Γ|.\mathcal{V}=|\Gamma|.(10)

Fig.2illustrates schematically how the visibility reduction in an electron fringe appears experimentally. The peak-to-trough intensity difference isΔ​I=Imax−Imin=2​𝒱​Iavg,\Delta I=I_{\rm max}-I_{\rm min}=2\mathcal{V}I_{\rm avg},(11)

so decreasing the visibility𝒱\mathcal{V}directly reduces the observable modulation of the fringes.Figure 2:Illustration of fringe visibility𝒱\mathcal{V}in an interference pattern. The dashed curve shows the ideal case of perfect coherence𝒱=1\mathcal{V}=1, while the solid curve shows a partially coherent pattern with visibility𝒱=0.4\mathcal{V}=0.4. The average intensityIavgI_{\rm avg}is unchanged with the reduced visibility, but the maximaImaxI_{\rm max}and minimaIminI_{\rm min}are compressed toward the mean.

Three limits for𝒱\mathcal{V}are important to appreciate. Suppose that the mode coefficients for the right and left paths of the electron are equal, such thatcR​0=cL​0andcR​1=cL​1.c_{\text{R}0}=c_{\text{L}0}\quad\text{and}\quad c_{\text{R}1}=c_{\text{L}1}.(12)

In this case, we obtain𝒱=1\mathcal{V}=1, withPe​(𝐱⟂)=|ψ0​(𝐱⟂)|2+Re​[(ψ0​(𝐱⟂))2],P_{e}(\mathbf{x}_{\perp})=|\psi_{0}(\mathbf{x}_{\perp})|^{2}+\text{Re}\left[(\psi_{0}(\mathbf{x}_{\perp}))^{2}\right],(13)

which allowsPeP_{e}to vary from complete destructive interference to maximal constructive interference. This is the limit offull coherence.

As a second possibility, suppose that the mode-path coefficients are unequal, but are related bycR​0=cL​0∗=c0andcR​1=cL​1∗=c1.c_{\text{R}0}=c_{\text{L}0}^{*}=c_{0}\quad\text{and}\quad c_{\text{R}1}=c_{\text{L}1}^{*}=c_{1}.(14)

This gives usPe​(𝐱⟂)=|ψ0​(𝐱⟂)|2+Re​[(c02+c12)​(ψ0​(𝐱⟂))2],P_{e}(\mathbf{x}_{\perp})=|\psi_{0}(\mathbf{x}_{\perp})|^{2}+\text{Re}\left[(c_{0}^{2}+c_{1}^{2})(\psi_{0}(\mathbf{x}_{\perp}))^{2}\right],(15)

In generalc02+c12c_{0}^{2}+c_{1}^{2}is complex-valued, and its magnitude𝒱=|c02+c12|\mathcal{V}=|c_{0}^{2}+c_{1}^{2}|(16)

lies in the range0<𝒱≤10<\mathcal{V}\leq 1. This is one version of the most typical case, that ofpartial coherence.

How wouldfull incoherenceoccur? Consider the (physically unlikely) case where the left path fully excites the substrate, while the right path completely fails to excite the substrate. Up to phase factors, this meanscR​0=1,cR​1=0,cL​0=0,cL​1=1,\begin{split}c_{\text{R}0}=1,\,c_{\text{R}1}&=0,\\
c_{\text{L}0}=0,\,c_{\text{L}1}&=1,\end{split}(17)

which is easy to confirm will lead toPe​(𝐱⟂)=|ψ0​(𝐱⟂)|2,P_{e}(\mathbf{x}_{\perp})=|\psi_{0}(\mathbf{x}_{\perp})|^{2},(18)

i.e., to𝒱=0\mathcal{V}=0, corresponding to the limit offull incoherence, where no interference fringes are observable despite the spatial overlap of the wave packets.

## II.3Summing over Multiple Modes

Now let us revisit the case where the substrate has a countably infinite number of surface modes. The initial state of the system is still given by Eq.2, but, working to first order in perturbation theory so that at most a single surface mode is excited, the final state after the electron has decoupled from the substrate may be written as|Ψf⟩=12[ψR​(𝐱⟂)​(cR0​|0⟩+∑𝐤cR​𝐤​|1𝐤⟩)+ψL(𝐱⟂)(cL0|0⟩+∑𝐤cL​𝐤|1𝐤⟩)],\begin{split}\ket{\Psi_{f}}=\frac{1}{\sqrt{2}}\Bigg[&\psi_{\mathrm{R}}(\mathbf{x}_{\perp})\left(c_{\mathrm{R}0}\ket{0}+\sum_{\mathbf{k}}c_{\mathrm{R}\mathbf{k}}\ket{1_{\mathbf{k}}}\right)\\
+&\psi_{\mathrm{L}}(\mathbf{x}_{\perp})\left(c_{\mathrm{L}0}\ket{0}+\sum_{\mathbf{k}}c_{\mathrm{L}\mathbf{k}}\ket{1_{\mathbf{k}}}\right)\Bigg],\end{split}(19)

where|1𝐤⟩\ket{1_{\mathbf{k}}}denotes a single excitation of a surface mode labeled by the surface wavevector𝐤=(kx,0,kz)\mathbf{k}=(k_{x},0,k_{z}), and the coefficients satisfy the normalization conditions|cj​0|2+∑𝐤|cj​𝐤|2=1,j∈{R,L}.|c_{j0}|^{2}+\sum_{\mathbf{k}}|c_{j\mathbf{k}}|^{2}=1,\qquad j\in\{\mathrm{R},\mathrm{L}\}.(20)

As above, the observed electron probability density is obtained by summing over the unobserved substrate degrees of freedom at the screen position asPe​(𝐱⟂)=∑{n𝐤}⟨Ψf|𝕀el⊗|{n𝐤}⟩​⟨{n𝐤}||Ψf⟩.P_{e}(\mathbf{x}_{\perp})=\sum_{\{n_{\mathbf{k}}\}}\braket{\Psi_{f}|\mathbb{I}_{\mathrm{el}}\otimes\ket{\{n_{\mathbf{k}}\}}\bra{\{n_{\mathbf{k}}\}}|\Psi_{f}}.(21)

Here|{n𝐤}⟩\ket{\{n_{\mathbf{k}}\}}denotes a complete Fock basis of substrate excitation states, labeled by the occupation numbers of the surface modes𝐤\mathbf{k}.

For the recombined beams, we presume the spatial profiles on the right and left for the overlap are related asψR​(𝐱⟂)=ψ0​(𝐱⟂)andψL​(𝐱⟂)=ψ0∗​(𝐱⟂).\psi_{\mathrm{R}}(\mathbf{x}_{\perp})=\psi_{0}(\mathbf{x}_{\perp})\quad\text{and}\quad\psi_{\mathrm{L}}(\mathbf{x}_{\perp})=\psi_{0}^{*}(\mathbf{x}_{\perp}).(22)

At the same time, we relate the zero-loss transition coefficients on the right and left ascR0=cL0=c0.c_{\mathrm{R}0}=c_{\mathrm{L}0}=c_{0}.(23)

These choices correspond to a symmetric recombination of beams with opposite transverse momentum.

Using orthogonality relations (e.g.,⟨0|1𝐤⟩=0\braket{0|1_{\mathbf{k}}}=0and⟨1𝐤|1𝐤′⟩=δ𝐤,𝐤′\braket{1_{\mathbf{k}}|1_{\mathbf{k}^{\prime}}}=\delta_{\mathbf{k},\mathbf{k}^{\prime}}),
the probability density reduces toPe​(𝐱⟂)=|ψ0​(𝐱⟂)|2+Re​{(ψ0​(𝐱⟂))2​[cR0∗​cL0+∑𝐤cR​𝐤∗​cL​𝐤]}.\begin{split}P_{e}(\mathbf{x}_{\perp})=&|\psi_{0}(\mathbf{x}_{\perp})|^{2}+\\
&\mathrm{Re}\Bigg\{(\psi_{0}(\mathbf{x}_{\perp}))^{2}\left[c_{\mathrm{R}0}^{*}c_{\mathrm{L}0}+\sum_{\mathbf{k}}c_{\mathrm{R}\mathbf{k}}^{*}c_{\mathrm{L}\mathbf{k}}\right]\Bigg\}.\end{split}(24)

Comparing this with Eq8above, we recognize that the coherence factorΓ\GammaisΓ=cR0∗​cL0+∑𝐤cR​𝐤∗​cL​𝐤,\Gamma=c_{\mathrm{R}0}^{*}c_{\mathrm{L}0}+\sum_{\mathbf{k}}c_{\mathrm{R}\mathbf{k}}^{*}c_{\mathrm{L}\mathbf{k}},(25)

and, as above, the modulation depth of the interference pattern, will be determined by the magnitude ofΓ\Gamma:𝒱=|Γ|,0≤𝒱≤1.\mathcal{V}=|\Gamma|,\qquad 0\leq\mathcal{V}\leq 1.(26)

In the present caseΓ\Gammais real, since the coordinates have been chosen in a symmetric way, so that𝒱=Γ\mathcal{V}=\Gamma.

## II.4System Symmetry and Fringe Visibility

To evaluate therightandleftscattering coefficients, it is convenient to define a reference trajectory. Supposec𝐤c_{\mathbf{k}}is the excitation coefficient that would arise for an unsplit beam traveling midway between the two paths along the central axis (x=0x=0). By shifting the coordinate origin to the actual trajectories atx=±d/2x=\pm d/2, the coefficients for the right and left trajectories differ from the reference beam only by a geometric phase—specifically,cR​𝐤=e+i​kx​d/2​c𝐤andcL​𝐤=e−i​kx​d/2​c𝐤.c_{\mathrm{R}\mathbf{k}}=e^{+ik_{x}d/2}c_{\mathbf{k}}\quad\text{and}\quad c_{\mathrm{L}\mathbf{k}}=e^{-ik_{x}d/2}c_{\mathbf{k}}.(27)

Substituting into Eq.25givesΓ=|c0|2+∑𝐤|c𝐤|2​e−i​kx​d.\Gamma=|c_{0}|^{2}+\sum_{\mathbf{k}}|c_{\mathbf{k}}|^{2}e^{-ik_{x}d}.(28)

The setup is symmetric under reflection across the central plane between the two trajectories (i.e., fromx→−xx\to-xacross they​zyzplate atx=0x=0), which means that the imaginary sine components cancel upon summation over all𝐤\mathbf{k}, leaving only the real cosine part. Using this and the first-order normalization condition|c0|2+∑𝐤|c𝐤|2=1,|c_{0}|^{2}+\sum_{\mathbf{k}}|c_{\mathbf{k}}|^{2}=1,(29)

we can therefore rewrite Eq.28as𝒱=1−∑𝐤|c𝐤|2​[1−cos⁡(kx​d)].\mathcal{V}=1-\sum_{\mathbf{k}}|c_{\mathbf{k}}|^{2}\left[1-\cos(k_{x}d)\right].(30)

This quantifies how interference contrast is reduced by entanglement with substrate excitations, with coherence preserved by processes that leave the substrate in the same final state for both paths and suppressed by excitations that do not. For an extended interaction region, this overlap accumulates continuously, motivating the Markovian approximation developed below.

## II.5Markovian Approximation

For an extended interaction region, we may use a Markovian approximation that imposes Poisson statistics for independent scattering events. The excitation probability grows linearly with propagation length as|c𝐤|2=L​d​P𝐤d​z,|c_{\mathbf{k}}|^{2}=L\,\frac{\mathrm{d}P_{\mathbf{k}}}{\mathrm{d}z},(31)

whered​P𝐤/d​z\mathrm{d}P_{\mathbf{k}}/\mathrm{d}zis the excitation probability per unit length. Retaining terms linear inLLgives𝒱​(L)≈1−L​∑𝐤d​P𝐤d​z​[1−cos⁡(kx​d)].\mathcal{V}(L)\approx 1-L\sum_{\mathbf{k}}\frac{\mathrm{d}P_{\mathbf{k}}}{\mathrm{d}z}\bigl[1-\cos(k_{x}d)\bigr].(32)

Assuming successive longitudinal slices are statistically independent, each slice will contribute to a small reduction in coherence, leading to a differential rate equation:d​𝒱d​z=−γ​(b,d)​𝒱,\frac{\mathrm{d}\mathcal{V}}{\mathrm{d}z}=-\gamma(b,d)\,\mathcal{V},(33)

withγ​(b,d)=∑𝐤d​P𝐤d​z​[1−cos⁡(kx​d)].\gamma(b,d)=\sum_{\mathbf{k}}\frac{\mathrm{d}P_{\mathbf{k}}}{\mathrm{d}z}\bigl[1-\cos(k_{x}d)\bigr].(34)

We can generalize this result by analogy. Suppose we have the differential EELS expression ford3​P/d​ω​d​kx​d​z\mathrm{d}^{3}P/\mathrm{d}\omega\,\mathrm{d}k_{x}\,\mathrm{d}z. A generalized version of Eq.34isγ​(b,d)=\displaystyle\gamma(b,d)=(35)∫0∞dω​∫−∞∞dkx​d3​Pd​ω​d​kx​d​z​[1−cos⁡(kx​d)],\displaystyle\int_{0}^{\infty}\mathrm{d}\omega\int_{-\infty}^{\infty}\mathrm{d}k_{x}\,\frac{\mathrm{d}^{3}P}{\mathrm{d}\omega\,\mathrm{d}k_{x}\,\mathrm{d}z}\,\bigl[1-\cos(k_{x}d)\bigr],

which leads to an exponential loss in fringe visibility as𝒱​(b,d,L)=exp⁡[−γ​(b,d)​L].\mathcal{V}(b,d,L)=\exp[-\gamma(b,d)L].(36)

This is the basic structure of each of the models discussed below. Eq.35makes explicit that decoherence is governed by the same differential loss spectrum that appears in EELS, weighted by how well a given mode distinguishes the two electron paths.

## II.6Thermal Effects

Until now, all thermal effects have been ignored. But at finite temperatureTT, the surface modes are no longer in the vacuum state, but are thermally occupied according to Bose-Einstein statistics:n¯𝐤=1eℏ​ω𝐤/kB​T−1.\bar{n}_{\mathbf{k}}=\frac{1}{e^{\hbar\omega_{\mathbf{k}}/k_{B}T}-1}.(37)

Each electron’s interaction with these populated modes has two consequences: an emission channel in which the electron excites the mode and produces the usual factorn¯𝐤+1\bar{n}_{\mathbf{k}}+1, and an absorption channel in which the electron removes a thermally populated quantum and produces a factorn¯𝐤\bar{n}_{\mathbf{k}}. The total thermal weighting is thus(n¯𝐤+1)+n¯𝐤=2​n¯𝐤+1=coth⁡(ℏ​ω𝐤2​kB​T).(\bar{n}_{\mathbf{k}}+1)+\bar{n}_{\mathbf{k}}=2\bar{n}_{\mathbf{k}}+1=\coth\!\left(\frac{\hbar\omega_{\mathbf{k}}}{2k_{B}T}\right).(38)

The finite-temperature decoherence rate is obtained from theT=0T=0expression by multiplying each mode contribution by this term15,6.

An alternative way to approach the question of thermal occupancies is to introduce a substrate in state|n𝐤⟩\ket{n_{\mathbf{k}}}and to calculate the transition probabilities for that particular case, then to propose that the physically observed effect will result from a thermally weighted (classical) average of these interactions. Such an analysis recovers this same factor ofcoth⁡(ℏ​ω𝐤/2​kB​T)\coth(\hbar\omega_{\mathbf{k}}/2k_{B}T).

This thermal weighting implies in general that the decoherence weight for each mode needs to be weighted asγ​(b,d,T)=\displaystyle\gamma(b,d,T)=(39)∫0∞dω​∫−∞∞dkx​d3​Pd​ω​d​kx​d​z​[1−cos⁡(kx​d)]​coth⁡(ℏ​ω2​kB​T),\displaystyle\int_{0}^{\infty}\mathrm{d}\omega\int_{-\infty}^{\infty}\mathrm{d}k_{x}\,\frac{\mathrm{d}^{3}P}{\mathrm{d}\omega\,\mathrm{d}k_{x}\,\mathrm{d}z}\,\bigl[1-\cos(k_{x}d)\bigr]\coth\!\left(\frac{\hbar\omega}{2k_{B}T}\right),

which, as before, can generate experimental predictions for the fringe visibility via𝒱=exp⁡(−γ​(b,d,T)​L)\mathcal{V}=\exp(-\gamma(b,d,T)L).Figure 3:Mode-resolved contributions to the decoherence rate integrand in the(kx,ω)(k_{x},\omega)plane for an electron beam at heightb=7.0​μb=7.0\,\mum above ann-doped silicon surface, with path separationd=8.1​μd=8.1\,\mum, and at temperatureT=293T=293K. (Model specifics are given in Sec.IIIbelow.) Top left: differential EEL spectrumd3​P/(d​z​d​ω​d​kx)\mathrm{d}^{3}P/(\mathrm{d}z\,\mathrm{d}\omega\,\mathrm{d}k_{x}). Top right: product of the EEL spectrum with the path weighting factor1−cos⁡(kx​d)1-\cos(k_{x}d). Bottom left: product of EEL spectrum with the thermal factorcoth⁡(ℏ​ω/2​kB​T)\coth(\hbar\omega/2k_{B}T). Bottom right: the full integrand enteringγ​(b,d,T)\gamma(b,d,T)—the differential EEL spectrum multiplied both by the path and the thermal weighting.

Fig.3illustrates how the integrand in Eq.39combines geometric, interference, and thermal effects. The impact parameterbbenters through the differential EEL spectrumd3​P/d​ω​d​kx​d​z\mathrm{d}^{3}P/\mathrm{d}\omega\,\mathrm{d}k_{x}\,\mathrm{d}zvia an evanescent factor that suppresses coupling to modes with large lateral wavevector. The path separationddappears in the factor1−cos⁡(kx​d)1-\cos(k_{x}d), which produces oscillatory zeros atkx​d=2​π​nk_{x}d=2\pi n. Finally, the temperatureTTenters through the factorcoth⁡(ℏ​ω/2​kB​T)\coth(\hbar\omega/2k_{B}T), which enhances low-frequency modes and increases their contribution to the decoherence rate.

From this, we may already draw some broad conclusions. The dominant contributions toγ​(b,d,T)\gamma(b,d,T)arise from those modes that are sufficiently long-wavelength to reach the beam at heightbb, with lateral wavevector large enough to distinguish the two paths, and with frequencies low enough to be thermally populated.

## IIIVisibility Loss Models

For numerical predictions, the theoretical framework above must be informed both with experimental parameters (e.g., with thevv,bb,dd, andLLvalues as labeled in Fig.1), as well as material models for the dielectric substrate that feed into the differential EELS models. One advantage of this option is that we can choose to inform our EELS models with different physics to examine which effects are observationally most significant. Of course, constructing such EELS models takes an extra step. Here we quote the relevant results. Such results are themselves semi-classical, but for those readers who are interested in a quantized approach we have derived the simplest case (see Sec.III.1below) as AppendixA.

In Sec.IV, we compare calculations with experimental results from Kerkeret al.8, so here we will quote the model that they used to capture material excitations. They studied the decohering properties of both gold andnn-doped silicon, each of which can (at low frequencies) be modeled by a three-parameter Drude model with background dielectric constant:ε​(ω)=ϵL​(1−ωp2ω​(ω+i​γrel)).\varepsilon(\omega)=\epsilon_{L}\left(1-\frac{\omega_{\rm p}^{2}}{\omega(\omega+\mathrm{i}\gamma_{\rm rel})}\right).(40)

This form reflects that the dielectric response is dominated at low frequencies by the static lattice contributionϵL\epsilon_{L}, while the motion of free charges is captured byωp\omega_{\rm p}. The parameterγrel\gamma_{\rm rel}quantifies the rate of mode relaxation.

Using this concrete model ofε​(ω)\varepsilon(\omega), it is straightforward to verify that each of the models of decoherence below reduces to the one discussed immediately before it.

## III.1Lossless model without signal retardation

First we consider the limiting case of electrostatic coupling (ω/c→0\omega/c\rightarrow 0) with undamped surface modes, for which the Drude-Lorentz model is used forε​(ω)\varepsilon(\omega)but withγrel=0\gamma_{\rm rel}=0. The modes are each labeled by their wavevector𝐤\mathbf{k}. From the electrostatic boundary condition, their oscillation frequencyω𝐤\omega_{\mathbf{k}}must satisfyε​(ω𝐤)=−1,\varepsilon(\omega_{\mathbf{k}})=-1,(41)

the familiar condition for nonretarded surface plasmons at a planar interface with the vacuum.16This can be inverted to findω𝐤\omega_{\mathbf{k}}:ω𝐤=ωp​ϵLϵL+1.\omega_{\mathbf{k}}=\omega_{\mathrm{p}}\sqrt{\frac{\epsilon_{L}}{\epsilon_{L}+1}}.(42)

We have included a full derivation of this case in AppendixA, including explicitly quantized modes.

This model severely underestimates the observed loss of visibility𝒱\mathcal{V}in all regions, but it has the benefit of being analytically tractable. In the end,γ​(b,d)\gamma(b,d)can be expressed in terms of modified Bessel functions asγ​(b,d)=2​α​c​ω𝐤(ϵL+1)​v2​[K0​(2​b​ω𝐤v)−K0​(ω𝐤v​(2​b)2+d2)],\begin{split}&\gamma(b,d)=\\
&\frac{2\alpha c\omega_{\mathbf{k}}}{(\epsilon_{L}+1)\,v^{2}}\,\left[K_{0}\!\left(\frac{2b\omega_{\mathbf{k}}}{v}\right)-K_{0}\!\left(\frac{\omega_{\mathbf{k}}}{v}\sqrt{(2b)^{2}+d^{2}}\right)\right],\end{split}(43)

whereα≈1/137\alpha\approx 1/137is the fine structure constant,vvis the electron speed, andccis the speed of light.

A largerγ\gammaleads to a quicker reduction in the fringe visibility𝒱\mathcal{V}, so despite its limitations this model captures the relevant qualitative effects. It is notable that as the path separationd→0d\rightarrow 0, the visibility𝒱→1\mathcal{V}\rightarrow 1. Furthermore, whend→∞d\rightarrow\infty,γ​(b,d)\gamma(b,d)simply reduces tod​P/d​z\mathrm{d}P/\mathrm{d}z.

## III.2Damped model without signal retardation

A more general model allows us to incorporate mode damping into the physical description (i.e.,γrel≠0\gamma_{\rm rel}\neq 0), while still ignoring magnetic effects from signal retardation (i.e.,ω/c→0\omega/c\rightarrow 0). When an electron travels in vacuum at a distancebbabove a planar dielectric half-space, the differential energy loss expression in the nonretarded limit1isd3​Pd​ω​d​kx​d​z=α​cπ​v2​e−2​k∥​bk∥​ℑ⁡[ε​(ω)−1ε​(ω)+1],\frac{\mathrm{d}^{3}P}{\mathrm{d}\omega\,\mathrm{d}k_{x}\,\mathrm{d}z}=\frac{\alpha\,c}{\pi\,v^{2}}\;\frac{\mathrm{e}^{-2k_{\parallel}b}}{k_{\parallel}}\;\Im\!\left[\frac{\varepsilon(\omega)-1}{\varepsilon(\omega)+1}\right],(44)

wherek∥=kx2+(ω/v)2,k_{\parallel}=\sqrt{k_{x}^{2}+\left(\omega/v\right)^{2}},(45)

andε​(ω)\varepsilon(\omega)is the complex dielectric function of the substrate. Plugging this into Eq.35and performing the integral overkxk_{x}yields a semi-analytic expression forγ​(b,d)\gamma(b,d):γ​(b,d)=2​α​cπ​v2​∫0∞dωℑ[ε​(ω)−1ε​(ω)+1]×[K0​(2​b​ωv)−K0​(ωv​(2​b)2+d2)].\begin{split}\gamma(b,d)=\qquad&\\
\frac{2\alpha c}{\pi\,v^{2}}\int_{0}^{\infty}\mathrm{d}\omega&\;\Im\!\left[\frac{\varepsilon(\omega)-1}{\varepsilon(\omega)+1}\right]\times\\
&\left[K_{0}\!\left(\frac{2b\omega}{v}\right)-K_{0}\!\left(\frac{\omega}{v}\sqrt{(2b)^{2}+d^{2}}\right)\right].\end{split}(46)

If we expandε​(ω)\varepsilon(\omega)around−1-1, Eq.46reduces to the lossless model forγ​(b,d)\gamma(b,d), Eq.43, in the limit thatγrel→0\gamma_{\rm rel}\rightarrow 0.

## III.3Damped model with signal retardation

The same logic can be used to generate predictions from a model that includes retardation. Retardation is incorporated through the functionsν​(ω,kx)=k∥2−ε​(ω)​ω2c2andν0​(ω,kx)=k∥2−ω2c2,\begin{split}\nu(\omega,\,k_{x})&=\sqrt{k_{\parallel}^{2}-\varepsilon(\omega)\frac{\omega^{2}}{c^{2}}}\qquad\text{and}\\
\nu_{0}(\omega,\,k_{x})&=\sqrt{k_{\parallel}^{2}-\frac{\omega^{2}}{c^{2}}},\end{split}(47)

whereε​(ω)\varepsilon(\omega)is the complex dielectric function of the substrate andk∥=kx2+(ω/v)2k_{\parallel}=\sqrt{k_{x}^{2}+(\omega/v)^{2}}as before. In the retarded formulation, the differential EELS expression3isd3​Pd​ω​d​kx​d​z=α​cπ​v2​e−2​ν0​bν0​ℑ⁡[λel​(ω,kx)],\frac{\mathrm{d}^{3}P}{\mathrm{d}\omega\,\mathrm{d}k_{x}\,\mathrm{d}z}=\frac{\alpha\,c}{\pi v^{2}}\,\frac{\mathrm{e}^{-2\nu_{0}b}}{\nu_{0}}\,\Im\!\left[\lambda_{\rm el}(\omega,\,k_{x})\right],(48)

where the loss functionλel​(ω,kx)\lambda_{\rm el}(\omega,\,k_{x})is given byλel​(ω,kx)=1ν0+ν​(2​ν02​(ε−1)ε​ν0+ν−(1−v2c2)​(ν0−ν)).\begin{split}&\lambda_{\rm el}(\omega,k_{x})=\qquad\\
&\frac{1}{\nu_{0}+\nu}\left(\frac{2\nu_{0}^{2}(\varepsilon-1)}{\varepsilon\nu_{0}+\nu}-\left(1-\frac{v^{2}}{c^{2}}\right)(\nu_{0}-\nu)\right).\end{split}(49)

The retarded loss expressionℑ⁡[λel]\Im[\lambda_{\rm el}]reduces to the non-retarded expressionℑ⁡[(ε−1)/(ε+1)]\Im[(\varepsilon-1)/(\varepsilon+1)]in the limitω/c→0\omega/c\rightarrow 0.

This retarded, thermally weighted EELS model is the central result of the present derivation. Substituting Eq.48into the thermally weighted decoherence rateγ​(b,d,T)\gamma(b,d,T)(Eq.39) recovers the macroscopic QED model of Scheel and Buhmann in its Markovian limit17, the model Kerkeret al.identified as giving the best agreement with their measured fringe visibilities.8To our knowledge this connection has not been previously reported. It shows that the entanglement-based decoherence framework developed above, following Strauch’s pedagogical treatment,20is not just qualitatively suggestive but reduces exactly to the specific model already validated against experiment.

## IVExperimental Implications

Now we can compare models directly with experimental results from Kerkeret al.The Kerkeret al.experiments employed a coherent 1 keV electron beam (with speedv≈0.062​cv\approx 0.062c) propagating parallel to a surface of lengthL=0.01L=0.01m over eithern-doped silicon or gold, with the fringe visibility measured as a function of beam heightbbfor several fixed lateral path separationsdd.

Here we will restrict our attention to then-doped silicon. For the modified Drude model (Eq.40) of ann-doped silicon surface, we use the parametersϵL=11.7,ωp=2.48×1013​rad/s, andγrel=2.59×1012​rad/s.\begin{split}\epsilon_{L}&=11.7,\\
\omega_{\rm p}&=2.48\times 10^{13}\,\text{rad/s, and}\\
\gamma_{\rm rel}&=2.59\times 10^{12}\,\text{rad/s}.\end{split}(50)

These parameters are taken from Karstens7, following the analysis of Kerkeret al.8. Fig.4compares the resulting predictions with visibility data𝒱\mathcal{V}digitized from Kerkeret al., using their reported experimental geometry and distance calibration. As in that publication, an additional3​μ​m3~\mu\mathrm{m}offset has been added to the values ofbbto correct for a reported systematic error in the data.Figure 4:Visibility𝒱\mathcal{V}as a function of surface distancebbfor several fixed path separationsdd(indicated in each panel), for a 1 keV electron passing overn-doped silicon. Discrete points show digitized results from plots in Kerkeret al., and solid curves correspond to results from the retarded model (Eq.48) applied to the decoherence rate with aT=293T=293K thermal correction (Eq.39).

The plots in Fig.4show𝒱\mathcal{V}as a function ofbbfor a split-path electron passing overn-doped silicon, with each subplot corresponding to a fixed path separationdd. Visibility increases quickly with increasing beam distance from the interfacebb, and decreases with increasing path separationdd. This is just as we might expect. Entanglement between the probe and the substrate depends on how near they are to one another during their interaction. Likewise, the farther separated the electron paths, the more distinguishable their interactions with the substrate become. It is worth emphasizing that the theoretical curves here are not empirical fits, but the direct output of the macroscopic QED model of Scheel and Buhmann, the endpoint of the derivation developed above. The agreement therefore illustrates how a first-principles model, built from basic quantum considerations, can confront real experimental data without adjustable parameters.

Fig.5demonstrates that such models can do more than simply reproduce experimental results. The left subplot of Fig.5shows how calculations may isolate the relative importance of various effects. For instance, despite the relatively low-energy electron beam, non-retarded EELS models (dashed curves) significantly underestimate the visibility loss relative to retarded models (solid curves). Furthermore, non-thermal calculations (blue curves,T→0T\rightarrow 0) also underestimate the loss of𝒱\mathcal{V}relative to thermal calculations (red curves, calculated with thecoth⁡(ℏ​ω/2​kB​T)\coth\!\left(\hbar\omega/2k_{B}T\right)withT=293T=293K). Both retardation and thermal occupation effects are necessary to reproduce the observed scale of the visibility loss.

The right subplot of Fig.5suggests an experimental extension based on this framework. As Velascoet al.have explored,21,22fringe visibility depends sensitively on substrate temperature, since the thermal factorcoth⁡(ℏ​ω/2​kB​T)\coth(\hbar\omega/2k_{B}T)enters the decoherence rate as a multiplicative weight on the loss spectrum. From low temperatures to 600 K, visibility varies strongly with bothTTandbb. This raises the possibility of using fringe visibility as a non-invasive thermal probe for nanoscale systems.

Kerkeret al.also included results for a gold surface, for which𝒱\mathcal{V}increases much more quickly with increased distancebbthan for then-doped silicon, but indicated further experiments are needed to validate results at smallbb. Intriguingly, the retarded “correction” terms can be dominant for determining decoherence rates in metals.5Unlike in silicon, theγ​(b,d,T)\gamma(b,d,T)expression for gold has an apparent infrared divergence, requiring a low-frequency cutoff in the integral based on the time of flight of the electron over the surface.22We refer readers to the published sources for further discussions.Figure 5:Fringe visibility𝒱\mathcal{V}for 1 keV electrons passing overnn-doped silicon (d=5.7​μ​md=5.7\,\mu\mathrm{m}).Left: Model comparison showing that both retardation (solid curves) and thermal occupation atT=293T=293K (red curves) are necessary to reproduce the experimental data in Fig.4. Dashed curves show non-retarded limits, while blue curves showT→0T\to 0limits.Right: Temperature dependence of𝒱\mathcal{V}at three impact parametersbb, computed using the fully retarded, thermally weighted model.

## VConclusion

We have shown how a schematic model can be augmented by a small number of physically motivated steps (incorporating multiple surface modes, applying a Markov approximation, including thermal occupation effects) to recover an empirically predictive theory. Framing this connection through a mode-resolved scattering picture ties the decoherence rate directly to familiar models from electron energy-loss spectroscopy. This mode-resolved picture also clarifies why temperature matters, since the surface-mode energies are low enough that significant thermal population occurs even at room temperature. It further implies that fringe visibility measurably varies with temperature, suggesting applications as a thermal probe.

More broadly, this discussion illustrates a useful pattern for physics pedagogy. Idealized toy models can often be extended by a small number of well-motivated steps into tools with genuine predictive power.

## Acknowledgements.The author thanks Archie Howie for clarifying comments and Robin Röpke for help with numerics.

## Appendix AFrom surface modes to EELS

This appendix outlines the calculation of quantum scattering amplitudes coupling an electron beam to surface modes of a dielectric half-space, working its way up to a description of an EEL spectrum.

The quantization of surface plasmon polariton modes and their excitation by external charges is well-established in both semiclassical and quantum frameworks14,23,24. It has been applied to many regular geometries in the nonretarded (ω/c→0\omega/c\to 0) limit2,10. Substrate dynamics are encoded through the relative permittivityε​(ω)\varepsilon(\omega), which is generally complex, but for the lossless mode construction, we takeε​(ω)\varepsilon(\omega)to be real, so that the field can be decomposed into normal modes.

## A.1Electrostatic Surface Modes

For the dielectric half-space, we introduce mode potentialsϕ𝐤​(𝐫)=1L2​k​{ei​𝐤⋅𝐫​e+k​y,fory<0;ei​𝐤⋅𝐫​e−k​y,fory≥0,\phi_{\mathbf{k}}(\mathbf{r})=\frac{1}{\sqrt{L^{2}k}}\begin{cases}e^{i\mathbf{k}\cdot\mathbf{r}}e^{+ky},\quad\text{for}\quad y<0;\\
e^{i\mathbf{k}\cdot\mathbf{r}}e^{-ky},\quad\text{for}\quad y\geq 0,\end{cases}(51)

whose wave vector𝐤\mathbf{k}lies parallel to thex​zxzplane as𝐤=(kx,0,kz)​and​k=kx2+kz2.\begin{split}\mathbf{k}&=(k_{x},0,k_{z})\text{ and }k=\sqrt{k_{x}^{2}+k_{z}^{2}}.\end{split}(52)

Though this expression includesLLas the box normalization length, all physical observables will be independent of this choice.

Defining the associated electric field modes as𝐮𝐤​(𝐫)=∇ϕ𝐤​(𝐫)\mathbf{u}_{\mathbf{k}}(\mathbf{r})=\mathbf{\nabla}\phi_{\mathbf{k}}(\mathbf{r})(53)

the modes are normalized such that integrating over the dielectric half-space yields∫y<0d3​𝐫​𝐮𝐤​(𝐫)⋅𝐮𝐤′∗​(𝐫)=δ𝐤,𝐤′.\int_{\mathrm{y<0}}\mathrm{d}^{3}\mathbf{r}\,\mathbf{u}_{\mathbf{k}}(\mathbf{r})\cdot\mathbf{u}^{*}_{\mathbf{k^{\prime}}}(\mathbf{r})=\delta_{\mathbf{k},\mathbf{k^{\prime}}}.(54)

At the planar interface, continuity of the normal component of the electric displacement requiresεr​(ω)​𝐧^⋅𝐮𝐤​(𝐫)|y→0−=𝐧^⋅𝐮𝐤​(𝐫)|y→0+.\varepsilon_{r}(\omega)\,\hat{\mathbf{n}}\!\cdot\!\mathbf{u}_{\mathbf{k}}(\mathbf{r})\big|_{y\to 0^{-}}=\hat{\mathbf{n}}\!\cdot\!\mathbf{u}_{\mathbf{k}}(\mathbf{r})\big|_{y\to 0^{+}}.(55)

For the dielectric half-space, this implies thatεr​(ω𝐤)=−1,\varepsilon_{r}(\omega_{\mathbf{k}})=-1,(56)

within the dielectric for all𝐤\mathbf{k}, which can be inverted to findω𝐤\omega_{\mathbf{k}}(cf. Sec.III.1above).

## A.2Quantization and Normalization

For a classical potential modeΦ𝐤​(𝐫)\Phi_{\mathbf{k}}(\mathbf{r})with physical units, the time-averaged electric field energy (cf. Landau and Lifshitz12, §80) isU𝐤=ϵ02​∫d3​𝐫​∂ω[ω​εr​(𝐫,ω)]ω=ω𝐤​|∇Φ𝐤​(𝐫)|2,U_{\mathbf{k}}=\frac{\epsilon_{0}}{2}\int\mathrm{d}^{3}\mathbf{r}\,\partial_{\omega}[\omega\varepsilon_{r}(\mathbf{r},\omega)]_{\omega=\omega_{\mathbf{k}}}|\nabla\Phi_{\mathbf{k}}(\mathbf{r})|^{2},(57)

where the integral is over all space, andεr​(ω)=1\varepsilon_{r}(\omega)=1in vacuum. For our normalized potentials, we may calculateN𝐤=12​∫d3​𝐫​∂ω[ω​εr​(𝐫,ω)]ω=ω𝐤​|∇ϕ𝐤​(𝐫)|2,N_{\mathbf{k}}=\frac{1}{2}\int\mathrm{d}^{3}\mathbf{r}\,\partial_{\omega}[\omega\varepsilon_{r}(\mathbf{r},\omega)]_{\omega=\omega_{\mathbf{k}}}|\nabla\phi_{\mathbf{k}}(\mathbf{r})|^{2},(58)

which, given the above conventions, reduces toN𝐤=12​(∂ω[ω​εr​(ω)]ω=ω𝐤+1),N_{\mathbf{k}}=\frac{1}{2}\left(\partial_{\omega}[\omega\varepsilon_{r}(\omega)]_{\omega=\omega_{\mathbf{k}}}+1\right),(59)

withεr​(ω)\varepsilon_{r}(\omega)now as the relative permittivity of the substrate, and the “+1” term arising from the integral over the vacuum half-space. We useN𝐤N_{\mathbf{k}}here to avoid confusion with the thermal occupation numbersn𝐤n_{\mathbf{k}}.

We now introduce creation and annihilation operatorsa^𝐤†\hat{a}_{\mathbf{k}}^{\dagger}anda^𝐤\hat{a}_{\mathbf{k}}satisfying[a^𝐤,a^𝐤′†]=δ𝐤𝐤′[\hat{a}_{\mathbf{k}},\hat{a}_{\mathbf{k^{\prime}}}^{\dagger}]=\delta_{\mathbf{k}\mathbf{k^{\prime}}}. The free Hamiltonian for these modes takes the form of a quantum harmonic oscillator:H^free=∑𝐤ℏ​ω𝐤​(a^𝐤†​a^𝐤+12).\hat{H}_{\mathrm{free}}=\sum_{\mathbf{k}}\hbar\omega_{\mathbf{k}}\left(\hat{a}_{\mathbf{k}}^{\dagger}\hat{a}_{\mathbf{k}}+\frac{1}{2}\right).(60)

To connect our classical fields to this quantum Hamiltonian, we must properly normalize the potential operator. The quantized potential operator bearing physical units isΦ^𝐤​(𝐫)=ℏ​ω𝐤2​ϵ0​N𝐤​(ϕ𝐤∗​(𝐫)​a^𝐤†+ϕ𝐤​(𝐫)​a^𝐤).\hat{\Phi}_{\mathbf{k}}(\mathbf{r})=\sqrt{\frac{\hbar\omega_{\mathbf{k}}}{2\epsilon_{0}N_{\mathbf{k}}}}\left(\phi^{*}_{\mathbf{k}}(\mathbf{r})\hat{a}^{\dagger}_{\mathbf{k}}+\phi_{\mathbf{k}}(\mathbf{r})\hat{a}_{\mathbf{k}}\right).(61)

The interaction Hamiltonian of these modes with a point chargeqqfollowing the prescribed trajectory𝐫q​(t)\mathbf{r}_{q}(t)is thenH^int​(t)=∑𝐤q​Φ^𝐤​(𝐫q​(t)).\hat{H}_{\mathrm{int}}(t)=\sum_{\mathbf{k}}q\hat{\Phi}_{\mathbf{k}}(\mathbf{r}_{q}(t)).(62)

## A.3Aloof Energy-Loss Spectrum

Using this interaction Hamiltonian, we now calculate the electron energy-loss spectrum for an electron traveling parallel to the surface, in the “aloof” geometry. The electron moves along the trajectory𝐫q​(t)=(0,b,v​t)\mathbf{r}_{q}(t)=(0,b,vt).

The first-order|0⟩→|1𝐤⟩\ket{0}\rightarrow\ket{1_{\mathbf{k}}}transition amplitude (denoted asc𝐤c_{\mathbf{k}}in the main text) isc0→1𝐤=−iℏ​∫t−t+dt​⟨1𝐤|​H^int​(t)​ei​ω𝐤​t​|0⟩,c_{0\rightarrow 1_{\mathbf{k}}}=-\frac{i}{\hbar}\int_{t_{-}}^{t_{+}}\mathrm{d}t\bra{1_{\mathbf{k}}}\hat{H}_{\mathrm{int}}(t)e^{i\omega_{\mathbf{k}}t}\ket{0},(63)

where the integral limits span the time of one box length (i.e.,t−=−L/2​vt_{-}=-L/2vtot+=+L/2​vt_{+}=+L/2v, the time taken to traverse one quantization length). This leads toc0→1𝐤=−i​qℏ​v​ℏ​ω𝐤2​ϵ0​N𝐤​e−k​bk​sinc​((ω𝐤−kz​v)​L2​v),c_{0\rightarrow 1_{\mathbf{k}}}=-\frac{iq}{\hbar v}\sqrt{\frac{\hbar\omega_{\mathbf{k}}}{2\epsilon_{0}N_{\mathbf{k}}}}\frac{e^{-kb}}{\sqrt{k}}\text{sinc}\left(\frac{(\omega_{\mathbf{k}}-k_{z}v)L}{2v}\right),(64)

wheresinc​(x)≡sin⁡(x)/x\text{sinc}(x)\equiv\sin(x)/x. In the largeLLlimit, the squared modulus ofc0→1𝐤c_{0\rightarrow 1_{\mathbf{k}}}becomes a delta function:|c0→1𝐤|2=π​q2ϵ0​ℏ​v2​ω𝐤N𝐤​e−2​k​bL​k​δ​(kz−ω𝐤/v).\begin{split}|c_{0\rightarrow 1_{\mathbf{k}}}|^{2}&=\frac{\pi q^{2}}{\epsilon_{0}\hbar v^{2}}\frac{\omega_{\mathbf{k}}}{N_{\mathbf{k}}}\frac{e^{-2kb}}{Lk}\delta(k_{z}-\omega_{\mathbf{k}}/v).\end{split}(65)

This is the probability of scattering for a single mode.

To find the probability of scattering from anyϕ𝐤\phi_{\mathbf{k}}mode, we evaluate sums as integrals and add up the probabilities:∑𝐤P0→1𝐤=L2(2​π)2​∫𝑑kx​𝑑kz​|c0→1𝐤|2=q2​L2​π​ϵ0​ℏ​v2​ω𝐤N𝐤​K0​(2​b​ω𝐤v),\begin{split}\sum_{\mathbf{k}}P_{0\rightarrow 1_{\mathbf{k}}}&=\frac{L^{2}}{(2\pi)^{2}}\int dk_{x}\,dk_{z}|c_{0\rightarrow 1_{\mathbf{k}}}|^{2}\\
&=\frac{q^{2}L}{2\pi\epsilon_{0}\hbar v^{2}}\frac{\omega_{\mathbf{k}}}{N_{\mathbf{k}}}K_{0}\left(\frac{2\,b\,\omega_{\mathbf{k}}}{v}\right),\end{split}(66)

whereK0​(x)K_{0}(x)is the modified Bessel function of the second kind. If the passing charge is an electron (q=−eq=-e), this result can be written in terms of the fine structure constantα≈1/137\alpha\approx 1/137and the speed of lightccas∑𝐤P0→1𝐤=2​α​c​Lv2​ω𝐤N𝐤​K0​(2​b​ω𝐤v).\sum_{\mathbf{k}}P_{0\rightarrow 1_{\mathbf{k}}}=2\alpha c\frac{L}{v^{2}}\frac{\omega_{\mathbf{k}}}{N_{\mathbf{k}}}K_{0}\left(\frac{2\,b\,\omega_{\mathbf{k}}}{v}\right).(67)

TheK0​(2​b​ω/v)K_{0}(2b\omega/v)term here expresses the exponential suppression of the excitation probability with increasing distance between the beam and the substrate.

The linear dependence of the total probability onLLsuggests an interpretation in terms of a probability per unit length. If we wish, we can rewrite Eq.65as an EEL spectrum, to be integrated overω\omegaandkxk_{x}, asd3​Pd​ω​d​kx​d​z=α​c​ωv2​N𝐤​e−2​b​k∥k∥​δ​(ω−ω𝐤)\frac{\mathrm{d}^{3}P}{\mathrm{d}\omega\,\mathrm{d}k_{x}\,\mathrm{d}z}=\alpha c\frac{\omega}{v^{2}N_{\mathbf{k}}}\,\frac{e^{-2bk_{\parallel}}}{k_{\parallel}}\,\delta(\omega-\omega_{\mathbf{k}})(68)

where, as above,k∥≡kx2+(ω/v)2k_{\parallel}\equiv\sqrt{k_{x}^{2}+(\omega/v)^{2}}. This result coincides with the semiclassical EELS expression in the limit of vanishing damping4.

## References
- P. M. Echenique and J. B. Pendry (1975)Absorption profile at surfaces.Journal of Physics C: Solid State Physics8(18),pp. 2936.External Links:Document,LinkCited by:§III.2.
- F. J. García de Abajo (2010)Optical excitations in electron microscopy.82,pp. 209–275.External Links:Document,LinkCited by:Appendix A.
- R. Garcia-Molina, A. Gras-Marti, A. Howie, and R. H. Ritchie (1985)Retardation effects in the interaction of charged particle beams with bounded condensed media.Journal of Physics C: Solid State PhysicsPhysical ReviewReviews of Modern PhysicsProgress in Surface SciencePhys. Rev. Lett.Rev. Mod. Phys.UltramicroscopyPhys. Rev. BPhys. Rev. BPhys. Rev. AReports on Progress in Physics18(27),pp. 5335.External Links:Document,LinkCited by:§III.3.
- A. Howie and R.H. Milne (1985)Excitations at interfaces and small particles.Ultramicroscopy18(1),pp. 427–433.External Links:ISSN 0304-3991,Document,LinkCited by:§A.3.
- A. Howie (2019)Continued skirmishing on the wave-particle frontier.203,pp. 52–59.External Links:ISSN 0304-3991,Document,LinkCited by:§IV.
- J. C. Idrobo, A. R. Lupini, T. Feng, R. R. Unocic, F. S. Walden, D. S. Gardiner, T. C. Lovejoy, N. Dellby, S. T. Pantelides, and O. L. Krivanek (2018)Temperature measurement by a nanoscale electron probe using energy gain and loss spectroscopy.120,pp. 095901.External Links:Document,LinkCited by:§II.6.
- K. Karstens (2014)Pfaddekohärenz von elektronen und ionen in der nähe dielektrischer oberflächen.Master’s thesis,Universität Rostock,Rostock, Germany.Cited by:§IV.
- N. Kerker, R. Röpke, L.M. Steinert, A. Pooch, and A. Stibor (2020)Quantum decoherence by Coulomb interaction.New Journal of Physics22(6),pp. 063039.External Links:DocumentCited by:§I,§III.3,§III,§IV.
- J. Kincaid, K. Mclelland, and M. Zwolak (2016)Measurement-induced decoherence and information in double-slit interference.American Journal of Physics84(7),pp. 522–530.External Links:ISSN 0002-9505,DocumentCited by:§I.
- D. Kordahl and C. Dwyer (2019)Enhanced vibrational electron energy-loss spectroscopy of adsorbate molecules.Phys. Rev. B99,pp. 104110.External Links:DocumentCited by:Appendix A.
- D. Kordahl (2023)Complementarity and entanglement in a simple model of inelastic scattering.American Journal of Physics91(10),pp. 796–804.External Links:ISSN 0002-9505,DocumentCited by:§I.
- L. D. Landau and E. M. Lifshitz (1984)Electrodynamics of continuous media.2nd edition,Course of Theoretical Physics, Vol.8,Pergamon Press,Oxford.External Links:ISBN 9780080302751,DocumentCited by:§A.2.
- Lerner,L. (2017)A demonstration of decoherence for beginners.American Journal of Physics85(11),pp. 870–872.External Links:DocumentCited by:§I.
- A.A. Lucas, E. Kartheuser, and R.G. Badro (1970)Quantum theory of electron-optical phonon interaction in ionic crystal films.Solid State Communications8(13),pp. 1075–1079.External Links:ISSN 0038-1098,DocumentCited by:Appendix A.
- A.A. Lucas and M. Šunjić (1972)Fast-electron spectroscopy of collective excitations in solids.2,pp. 75–137.External Links:ISSN 0079-6816,Document,LinkCited by:§II.6.
- J. M. Pitarke, V. M. Silkin, E. V. Chulkov, and P. M. Echenique (2006)Theory of surface plasmons and surface-plasmon polaritons.70(1),pp. 1.External Links:Document,LinkCited by:§III.1.
- S. Scheel and S. Y. Buhmann (2012)Path decoherence of charged and neutral particles near surfaces.Phys. Rev. A85,pp. 030101.External Links:DocumentCited by:§I,§III.3.
- D. V. Schroeder (2017)Entanglement isn’t just for spin.American Journal of Physics85(11),pp. 812–820.External Links:ISSN 0002-9505,DocumentCited by:§I.
- P. Sonnentag and F. Hasselbach (2007)Measurement of decoherence of electron waves and visualization of the quantum-classical transition.Phys. Rev. Lett.98,pp. 200402.External Links:DocumentCited by:§I.
- F. W. Strauch (2025)Decoherence, entanglement, and information in the electron double-slit experiment with monitoring.American Journal of Physics93(1),pp. 34–45.External Links:ISSN 0002-9505,DocumentCited by:§I,§III.3.
- C. I. Velasco, V. D. Giulio, and F. J. G. de Abajo (2024)Radiative loss of coherence in free electrons: a long-range quantum phenomenon.Light: Science & Applications13(1),pp. 31.External Links:Document,LinkCited by:§I,§IV.
- C. I. Velasco, V. D. Giulio, and F. J. G. de Abajo (2026)Free-electron decoherence: theory and applications.External Links:2602.14693,LinkCited by:§I,§IV,§IV.
- Z.L. Wang (1996)Valence electron excitations and plasmon oscillations in thin films, surfaces, interfaces and small particles.Micron27(3),pp. 265–299.External Links:ISSN 0968-4328,DocumentCited by:Appendix A.
- J. Zhang, L. Zhang, and W. Xu (2012)Surface plasmon polaritons: physics and applications.Journal of Physics D: Applied Physics45(11),pp. 113001.External Links:DocumentCited by:Appendix A.

## 


- 


Major funding support from
