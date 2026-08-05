# Dynamical control of particle jets from a driven condensate in a one-dimensional lattice with double-well potential

**arXiv ID**: 2607.23533v1
**Authors**: Z. Li, L. Q. Lai
**Published**: 2026-07-26
**Categories**: cond-mat.quant-gas, quant-ph
**Comments**: 9 pages, 8 figures
**DOI**: 10.1002/andp.70253
**HTML URL**: https://arxiv.org/html/2607.23533v1

## Abstract

We investigate the nonlinear dynamics of a Bose-Einstein condensate trapped in a double-well potential of a one-dimensional lattice, where the interatomic interactions are periodically modulated in time. In the typical case of a symmetric double-well, we observe collective particle emission under resonant driving, where the excitation regimes are explicitly constrained by the interplay between the drive strength and the hopping amplitude. By introducing a depth asymmetry between the wells, we find that moderate bias specifically enhances the emission rate, while large asymmetry suppresses it. The particle jets can be further controlled by modulating the hopping amplitudes, where the emission is weakened for finite hopping imbalances. These results outline the roles of asymmetry and external driving in precisely manipulating quantum many-body transport, and may offer insights into the design of atomtronic devices.

## Full Text

Dynamical control of particle jets from a driven condensate in a one-dimensional lattice with double-well potential

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
- License: CC BY-NC-ND 4.0arXiv:2607.23533v1 [cond-mat.quant-gas] 26 Jul 2026

## Dynamical control of particle jets from a driven condensate in a one-dimensional lattice with double-well potentialZ. LiBasic Teaching Department, Nanhang Jincheng College, Nanjing 211156, ChinaL. Q. Lailqlai@njupt.edu.cnSchool of Science, Nanjing University of Posts and Telecommunications, Nanjing 210023, China

## Abstract

We investigate the nonlinear dynamics of a Bose-Einstein condensate trapped in a double-well potential of a one-dimensional lattice, where the interatomic interactions are periodically modulated in time. In the typical case of a symmetric double-well, we observe collective particle emission under resonant driving, where the excitation regimes are explicitly constrained by the interplay between the drive strength and the hopping amplitude. By introducing a depth asymmetry between the wells, we find that moderate bias specifically enhances the emission rate, while large asymmetry suppresses it. The particle jets can be further controlled by modulating the hopping amplitudes, where the emission is weakened for finite hopping imbalances. These results outline the roles of asymmetry and external driving in precisely manipulating quantum many-body transport, and may offer insights into the design of atomtronic devices.Bose-Einstein condensate, one-dimensional lattice, double-well potential, periodic driving

## IIntroduction

The quantum dynamics of ultracold atomic gases has been attracting intensive attention for the past few decades since the realization of Bose-Einstein condensation[1], as it constitutes a versatile platform for concrete investigations of many-body phenomena relevant to condensed matter physics. In particular, the ability of precisely controlling the interatomic interactions via Feshbach resonance enables explorations of exotic quantum matter and quantum engineering[2]. Among the prominent examples, the system of bosonic atoms confined in a symmetric double-well potential is straightforwardly related to the celebrated Josephson effect in superconductors, popularly known as the bosonic Josephson junction[3], which has been extensively investigated both theoretically and experimentally[4,5,6,7,8,9,10,11,12,13,14,15,16,17].

Such a system serves as a paradigm model for studying various fundamental quantum features and offering insights into rich nonlinear dynamics that are not accessible for conventional superconducting junctions, including Josephson oscillations[18,19,20,21,22,23,24,25], macroscopic quantum self-trapping[26,27,28,29,30]and tunneling dynamics[31,32,33,34,35,36,37]. The advances of precision measurement techniques have further established these systems as powerful quantum simulators for exploring many-body dynamics in optical lattices under tunable conditions[38,39,40].

The scenario becomes particularly intriguing in an asymmetric double-well configuration, where the explicit breaking of spatial symmetry gives rise to qualitatively new physics[41,42,43,44,45,46,47,48,49,50]. The asymmetry typically induces significant changes in the dynamical behavior, and is associated with symmetry-breaking quantum phase transitions[51]. From an experimental perspective, an asymmetric double well can be realized as a fundamental building block of tilted optical lattices, which has been vital to the recent studies of resonantly enhanced tunneling[52,53,54,55,56]. Moreover, even a slight asymmetry, often unavoidable in realistic trapping potentials, can influence various properties of the system in nontrivial ways, such as dynamical instabilities, population imbalance and tunneling rates[49,50], facilitating verifications of the crucial role of the interplay between interactions and asymmetries in quantum transports.

In the previous studies, we uncovered a variety of particle-emission phenomena in a parametrically driven Bose-Einstein condensate, including resonantly enhanced emission[36], drive-imbalance effects[37], interference-induced suppression of the emission[57]and intermittent jet formation[58], while mainly focusing on the symmetric lattice geometries with homogeneous hopping amplitudes. In this work, we theoretically investigate the nonlinear dynamics within a one-dimensional lattice, where an asymmetric double-well potential is specifically applied to trap the condensate and the interatomic interactions are periodically modulated. We identify the distinct excitation regimes, and further demonstrate tunable control of collective particle jets via well asymmetries and hopping imbalances.

The paper is organized as follows. In Sec.II, we introduce the lattice model and illustrate a brief outline of the framework. In Sec.III, we present the numerical analysis of nonlinear dynamics and compare the results with analytical solutions. We summarize our work and give some concluding remarks in Sec.IV.

## IITheoretical model

As schematically shown in Fig.1, we consider a one-dimensional infinite lattice featuring a double-well potential that traps a Bose-Einstein condensate in the central lattice sites labeledbbandcc, and the remaining sites in the leads are symbolized by nonzero integers. The coupling between the central sites is quantified by strengthJhJ_{h}, which facilitates the back-and-forth tunneling of atoms. Excited particles with sufficient energy can escape from the wells and hop to the nearest-neighboring sites with hopping amplitudeJbJ_{b}andJcJ_{c}, respectively, while traveling along the leads to infinity with a tunneling strengthJlJ_{l}. Since the atomic density and the resulting particle jets are low outside the wells when compared with the condensate, it is reasonable to only include the interatomic interactions in the central sites. The system can thus be mathematically described by the HamiltonianH^\displaystyle\hat{H}=\displaystyle=Vb​b^0†​b^0+Vc​c^0†​c^0−Jh​(b^0†​c^0+c^0†​b^0)\displaystyle V_{b}\hat{b}_{0}^{\dagger}\hat{b}_{0}+V_{c}\hat{c}_{0}^{\dagger}\hat{c}_{0}-J_{h}(\hat{b}_{0}^{\dagger}\hat{c}_{0}+\hat{c}_{0}^{\dagger}\hat{b}_{0})(1)+G​(t)2​(b^0†​b^0†​b^0​b^0+c^0†​c^0†​c^0​c^0)\displaystyle+\frac{G\left(t\right)}{2}\left(\hat{b}_{0}^{\dagger}\hat{b}_{0}^{\dagger}\hat{b}_{0}\hat{b}_{0}+\hat{c}_{0}^{\dagger}\hat{c}_{0}^{\dagger}\hat{c}_{0}\hat{c}_{0}\right)−Jb​(b^0†​b^1+b^1†​b^0)−Jc​(c^0†​c^1+c^1†​c^0)\displaystyle-J_{b}\left(\hat{b}_{0}^{\dagger}\hat{b}_{1}+\hat{b}_{1}^{\dagger}\hat{b}_{0}\right)-J_{c}\left(\hat{c}_{0}^{\dagger}\hat{c}_{1}+\hat{c}_{1}^{\dagger}\hat{c}_{0}\right)−Jl∑j=1∞(b^j+1†b^j+c^j+1†c^j+H.c.).\displaystyle-J_{l}\sum_{j=1}^{\infty}\left(\hat{b}_{j+1}^{\dagger}\hat{b}_{j}+\hat{c}_{j+1}^{\dagger}\hat{c}_{j}+{\rm{H.c.}}\right).

Here,VbV_{b}andVcV_{c}represent the respective depth of the double wells.b^0†\hat{b}_{0}^{\dagger}(b^0)(\hat{b}_{0})andc^0†\hat{c}_{0}^{\dagger}(c^0)(\hat{c}_{0})are the bosonic creation (annihilation) operators of the central sites, whileb^j†\hat{b}_{j}^{\dagger}(b^j)(\hat{b}_{j})andc^j†\hat{c}_{j}^{\dagger}(c^j)(\hat{c}_{j})correspond to thejjth site on the right or left leads. The time-dependent termG​(t)=U+g​(t)G(t)=U+g\left(t\right)characterizes the on-site pairwise interactions, whereUUis a constant andg​(t)=g​sin⁡(ω​t)g(t)=g\sin(\omega t)is a sinusoidally oscillating driving, withggbeing the drive strength andω\omegabeing the drive frequency.Figure 1:Sketch of the one-dimensional infinite lattice under consideration. A double-well potential of depthVbV_{b}andVcV_{c}is applied to the central lattice sites labeledbbandcc, and the blue empty circles indexed by integers1,2,…,∞1,2,\ldots,\inftydenote the remaining sites outside the wells.

We study the dynamics under the mean-field approximation, such that the operators can be approximately replaced by their expectation values with complex numbersμj=⟨μ^j⟩≡φμ,j\mu_{j}=\langle\hat{\mu}_{j}\rangle\equiv\varphi_{\mu,j}(μ={b,c}\mu=\{b,c\}), and physically|φμ,j|2|\varphi_{\mu,j}|^{2}represents the particle number on thejjth site. The time evolution of the system is governed by the Hamiltonian, which yields the corresponding Heisenberg equations of motion for sitej=0j=0(ℏ=1\hbar=1throughout)i​∂tφb,0\displaystyle i\partial_{t}\varphi_{b,0}=\displaystyle=Vb​φb,0+G​(t)​|φb,0|2​φb,0−Jh​φc,0−Jb​φb,1,\displaystyle V_{b}\varphi_{b,0}+G\left(t\right)|\varphi_{b,0}|^{2}\varphi_{b,0}-J_{h}\varphi_{c,0}-J_{b}\varphi_{b,1},(2)i​∂tφc,0\displaystyle i\partial_{t}\varphi_{c,0}=\displaystyle=Vc​φc,0+G​(t)​|φc,0|2​φc,0−Jh​φb,0−Jc​φc,1,\displaystyle V_{c}\varphi_{c,0}+G\left(t\right)|\varphi_{c,0}|^{2}\varphi_{c,0}-J_{h}\varphi_{b,0}-J_{c}\varphi_{c,1},(3)

and for the remaining sitesj≥1j\geq 1,i​∂tφμ,1\displaystyle i\partial_{t}\varphi_{\mu,1}=\displaystyle=−Jμ​φμ,0−Jl​φμ,2,\displaystyle-J_{\mu}\varphi_{\mu,0}-J_{l}\varphi_{\mu,2},(4)i​∂tφμ,j\displaystyle i\partial_{t}\varphi_{\mu,j}=\displaystyle=−Jl​(φμ,j−1+φμ,j+1).\displaystyle-J_{l}(\varphi_{\mu,j-1}+\varphi_{\mu,j+1}).(5)

In cold atom experiments, the dc component of the scattering length is generally kept small, and a finite interactionUUdoes not qualitatively affect the relevant physics[57,58,59,60]; thus, we work in the limit ofU=0U=0to further simplify the analysis (see AppendixA). In the absence of an external periodic driving (g=0g=0), the system remains in equilibrium, and can be explicitly described by the two-mode approximation[21,5].

We begin with the extensively studied case of equivalent depth of the wells (Vb=VcV_{b}=V_{c}) and introduce the stationary ansatzb0=β​e−i​ϵb​tb_{0}=\beta e^{-i\epsilon_{b}t}andc0=γ​e−i​ϵc​tc_{0}=\gamma e^{-i\epsilon_{c}t}(β\betaandγ\gammaare constant), which naturally recovers the typical scenario withϵb=ϵc\epsilon_{b}=\epsilon_{c}, reaching(ΛbJhJhΛc)​(βγ)=0\displaystyle\left(\begin{array}[]{cc}\Lambda_{b}&J_{h}\\
J_{h}&\Lambda_{c}\end{array}\right)\left(\begin{array}[]{cc}\beta\\
\gamma\end{array}\right)=0(10)

withΛμ=ϵμ−Vμ−Jμ2​𝒢11​(ϵμ)\Lambda_{\mu}=\epsilon_{\mu}-V_{\mu}-J_{\mu}^{2}\mathcal{G}_{11}(\epsilon_{\mu}), and as derived in AppendixB,𝒢11​(ϵ)=ϵ2​Jl2−i​1Jl2−ϵ24​Jl4\displaystyle\mathcal{G}_{11}\left(\epsilon\right)=\frac{\epsilon}{2J_{l}^{2}}-i\sqrt{\frac{1}{J_{l}^{2}}-\frac{\epsilon^{2}}{4J_{l}^{4}}}(11)

is the frequency-domain Green’s function. When involving the asymmetric double well (Vb≠VcV_{b}\neq V_{c}), a perturbative solution can be readily obtained with weak drive strengthggand weak hopping amplitudeJμJ_{\mu}. For the case ofβ=γ\beta=\gamma, to the zeroth order inJμJ_{\mu}we haveϵμ,s(0)=Vμ−Jh,\displaystyle\epsilon_{\mu,{\rm s}}^{(0)}=V_{\mu}-J_{h},(12)

while for the antisymmetric case ofβ=−γ\beta=-\gammait givesϵμ,as(0)=Vμ+Jh.\displaystyle\epsilon_{\mu,{\rm as}}^{(0)}=V_{\mu}+J_{h}.(13)

To the second order in the hopping amplitudeJμJ_{\mu}, a slick way involves the direct substitution of the zeroth-order solutions into the above matrix equation, leading toϵμ,s(2)=ϵμ,s(0)+Jμ22​Jl2​[ϵμ,s(0)−i​4​Jl2−(ϵμ,s(0))2],\displaystyle\epsilon_{\mu,{\rm s}}^{(2)}=\epsilon_{\mu,{\rm s}}^{(0)}+\frac{J_{\mu}^{2}}{2J_{l}^{2}}\left[\epsilon_{\mu,{\rm s}}^{(0)}-i\sqrt{4J_{l}^{2}-\left(\epsilon_{\mu,{\rm s}}^{(0)}\right)^{2}}\right],(14)

andϵμ,as(2)=ϵμ,as(0)+Jμ22​Jl2​[ϵμ,as(0)−i​4​Jl2−(ϵμ,as(0))2].\displaystyle\epsilon_{\mu,{\rm as}}^{(2)}=\epsilon_{\mu,{\rm as}}^{(0)}+\frac{J_{\mu}^{2}}{2J_{l}^{2}}\left[\epsilon_{\mu,{\rm as}}^{(0)}-i\sqrt{4J_{l}^{2}-\left(\epsilon_{\mu,{\rm as}}^{(0)}\right)^{2}}\right].(15)

The presence of a real-valued solution in the square roots imposes specific constraints to the allowed depthVμV_{\mu}. To observe significant particle jets under time-periodic driving, we need to be in the regime where the symmetric mode remains stable while the antisymmetric mode is damped, i.e.,|ϵμ,s(0)|>2​Jl|\epsilon_{\mu,{\rm s}}^{(0)}|>2J_{l}and|ϵμ,as(0)|<2​Jl|\epsilon_{\mu,{\rm as}}^{(0)}|<2J_{l}. As we specialize to negative trapping potentialsVμ=−|Vμ|<0V_{\mu}=-|V_{\mu}|<0, the inequalities yield−Jh−2​Jl<Vμ<Jh−2​Jl-J_{h}-2J_{l}<V_{\mu}<J_{h}-2J_{l}.

## IIINonlinear dynamics

In the following, we parametrically drive the system, and analyze the nonlinear dynamics by numerically solving Eqs. (2)-(5). We assume that the condensate is stable att<0t<0, with all the particles initially prepared in the central sites at the lowest symmetric mode before the periodic perturbation is turned on. Without any loss of generality, the antisymmetric mode is then seeded by takingβ≈γ=1\beta\approx\gamma=1with a slight difference, and in the numerics we measure the energy in units ofJh=1J_{h}=1, such that the times and the frequencies are measured in units of1/Jh1/J_{h}andJhJ_{h}, respectively.

## III.1Symmetric double-well potential

We first focus on the general case of a symmetric double well with equivalent depth (Vb=Vc≡VV_{b}=V_{c}\equiv V) and hopping amplitude (Jb=Jc≡JJ_{b}=J_{c}\equiv J) to demonstrate the regimes for exciting the particles. The time evolution of atoms in the condensate is highly nonlinear, especially when the drive strengthggis large. One can, however, characterize the decay by fitting the total particle number in the central sites to an asymptotically exponential function asN0​(t)=|φb,0​(t)|2+|φc,0​(t)|2≈α​e−ξ​t,\displaystyle N_{0}(t)=|\varphi_{b,0}(t)|^{2}+|\varphi_{c,0}(t)|^{2}\approx\alpha e^{-\xi t},(16)

whereξ\xidenotes the average emission rate of the particles from the condensate andα\alphais a constant. As shown in Fig.2, when the well depth is roughlyV<−1V<-1, the symmetric mode remains quite stable for generic hopping amplitudeJJ, while the antisymmetric mode can be unstable in the range of−3<V<−1-3<V<-1, with the analytical solutions clearly delineating the boundaries. For subsequent analysis, we mainly takeV=−2V=-2with a relatively smallJJ, and select appropriate driving parameters based upon the excitation regimes.Figure 2:Regimes for the symmetric mode and antisymmetric mode. The numerical results (color areas) are obtained by directly solving Eqs. (2) and (3), while the analytical solutions (dashed lines) come from Eqs. (14) and (15). Color bars denotes the emission rateξ\xiof the particles. Here, the tunneling strength isJl=1J_{l}=1, and the drive strength isg=0.2g=0.2. We have taken the simulation timeτ=50\tau=50.Figure 3:Total particle number of the condensateN0N_{0}as a function of time with different drive frequencyω\omega. Here, the depth of the well isV=−2V=-2, and the drive strength isg=0.2g=0.2. The hopping amplitude isJ=0.1J=0.1, and the tunneling strength isJl=1J_{l}=1.

Figure3shows the short-time decay behavior of the total particle numberN0N_{0}under a fixed drive strength, with the drive frequencyω\omegavarying in multiples ofJhJ_{h}. It is clear that the system remains stable, unless the drive is resonant atω=4​Jh\omega=4J_{h}. This arises from the fact that the wells support discrete bands corresponding to the local ground state (symmetric mode) and the local first excited state (antisymmetric mode), such that significant excitation occurs when the drive frequency matches the energy differenceω=2​(ϵμ,as(0)−ϵμ,s(0))=4​Jh\omega=2(\epsilon_{\mu,{\rm as}}^{(0)}-\epsilon_{\mu,{\rm s}}^{(0)})=4J_{h}. Under this circumstance, pair atoms share half of the driving energy and are pumped to the excited state, after which they eject from the wells and propagate along the leads.Figure 4:Number of excited particlesΔ​N\Delta Nvs the drive strengthggand the hopping amplitudeJJ. The color area results from the numerics of Eqs. (2) and (3), and the red dashed line comes from the analytical solution in Eqs. (20) and (21). We have taken the depth of the wellV=−2V=-2and the drive frequencyω=4​Jh\omega=4J_{h}. The tunneling strength isJl=1J_{l}=1, and the evolution time isτ=100\tau=100.

Since we focus on the regime of weak drive strength and weak hopping amplitude, the instabilities may be modified if the driving parameters are further increased. We thus define the number of excited particlesΔ​N=N0​(t=0)−N0​(t=τ),\displaystyle\Delta N=N_{0}\left(t=0\right)-N_{0}\left(t=\tau\right),(17)

and verify more quantitatively the interplay between the drive strengthggand the hopping amplitudeJJ. As can be plainly seen in Fig.4, for generic hopping amplitude and weak drive strength, few particles can be ejected andΔ​N\Delta Nremains small. In contrast, for stronger drives even a small hopping amplitude gives rise to significant emission. We see that a largerJJrequires a strongergg, which can be described by the two-mode approximationb0​(t)\displaystyle b_{0}\left(t\right)=\displaystyle=e−i​(V−Jh)​t​χ​(t)+e−i​(V+Jh)​t​λ​(t),\displaystyle e^{-i(V-J_{h})t}\chi(t)+e^{-i(V+J_{h})t}\lambda(t),(18)c0​(t)\displaystyle c_{0}\left(t\right)=\displaystyle=e−i​(V−Jh)​t​χ​(t)−e−i​(V+Jh)​t​λ​(t),\displaystyle e^{-i(V-J_{h})t}\chi(t)-e^{-i(V+J_{h})t}\lambda(t),(19)

whereχ​(t)\chi(t)andλ​(t)\lambda(t)are the slowly varying amplitudes of symmetric and antisymmetric modes, respectively, and it yields (see AppendixC)∂tχ\displaystyle\partial_{t}\chi=\displaystyle=−g2​λ2​χ,\displaystyle-\frac{g}{2}\lambda^{2}\chi,(20)∂tλ\displaystyle\partial_{t}\lambda=\displaystyle=−Ωas2​λ+g2​χ2​λ,\displaystyle-\frac{\Omega_{\rm as}}{2}\lambda+\frac{g}{2}\chi^{2}\lambda,(21)

withΩas=−2​J2​Im​𝒢11​(ϵas)\Omega_{\rm as}=-2J^{2}{\rm Im}\mathcal{G}_{11}\left(\epsilon_{\rm as}\right). This suggests that whenΩas>g​χ2\Omega_{\rm{as}}>g\chi^{2}, the particles remain bound and balanced in the two wells, while forΩas<g​χ2\Omega_{\rm{as}}<g\chi^{2}we get a buildup, followed by a significant particle emission. The threshold behavior appropriately delineates the numerics in Fig.4, and reflects the competition between dissipation induced by the leads and parametric amplification driven by interaction modulation. Notably, when the hopping amplitude is too small (roughlyJ<0.05J<0.05), the excitation becomes greatly suppressed.

## III.2Asymmetric double-well potential

We now turn to the asymmetric configuration withVb≠VcV_{b}\neq V_{c}. The depth asymmetry between the two wells, characterized byΔ​V=Vb−Vc\Delta V=V_{b}-V_{c}, induces a relative on-site energy shift and consequently modifies the resonance conditions of the excitation spectrum. To ensure a consistent comparison, we choose parameters based upon the distinct instabilities identified in Fig.4and explore how the nonlinear dynamics develop. Figure5shows the influence of the depth asymmetry on collective particle emission at a fixed hopping amplitude. When the drive strength is as small asg=0.1g=0.1, which lies outside the parametric instability regions, the total particle number in the central sites exhibits only bounded oscillations for different values ofΔ​V\Delta V, and the number of ejected particles remains negligible, i.e.,|Δ​N|≈0|\Delta N|\approx 0.Figure 5:Decay of the particle numberN0N_{0}under typical asymmetric double wellΔ​V\Delta Vfor different drive strengthgg. Here, the depth of the left well is kept asVb=−2V_{b}=-2, while the depth of the right one is varied asVc=−2.8V_{c}=-2.8,−2.4-2.4,−2-2,−1.6-1.6and−1.2-1.2, respectively. We have also taken the hopping amplitudeJb=Jc=0.3J_{b}=J_{c}=0.3, the tunneling strengthJl=1J_{l}=1, and the drive frequencyω=4\omega=4.

For a stronger driveg=0.2g=0.2, a relatively large depth asymmetry, either positive or negative (exemplified byΔ​V=±0.8\Delta V=\pm 0.8), gives rise to only a weak enhancement of the emission, as the pronounced energy offset between the wells introduces a strong effective detuning, which reduces coherent tunneling and shifts the system away from optimal parametric resonance conditions. By contrast, for somewhat smaller asymmetries (e.g.,Δ​V=±0.4\Delta V=\pm 0.4), the decay can be significantly enhanced. In this regime, moderate asymmetry hybridizes the symmetric and antisymmetric modes, modifying their eigenfrequencies and effectively improving the resonance condition under parametric driving, and thereby the emission process becomes more efficient. When the drive strength is further increased tog=0.3g=0.3and0.40.4, the symmetric case (Δ​V=0\Delta V=0) exhibits very weak decay at short times, followed by the emergence of a large pulse at intermediate driving intervals, and the excited numberΔ​N\Delta Nincreases rapidly. For large values of depth asymmetry (|Δ​V|=0.8|\Delta V|=0.8), the emission remains suppressed due to strong detuning, while the case with|Δ​V|=0.4|\Delta V|=0.4shows explicit enhancement, where the buildup stages becomes much shorter and the excited particles saturate faster than that ofΔ​V=0\Delta V=0.Figure 6:Time evolution of the excited particle number under typical depth asymmetryΔ​V\Delta V, with the hopping imbalanceΔ​J\Delta Jranging from−0.2-0.2to0.20.2. Accordingly, the depth of the wells areVc=−2V_{c}=-2, andVb=−2V_{b}=-2,−1.6-1.6, and−2.4-2.4, respectively. We have kept the hopping amplitudeJc=0.3J_{c}=0.3, and the other parameters areJl=1J_{l}=1,g=0.3g=0.3, andω=4\omega=4.

One can further explore how to control the excitation dynamics by tuning the hopping imbalanceΔ​J=Jb−Jc\Delta J=J_{b}-J_{c}at a fixed drive strength. As shown in Fig.6, for the case ofΔ​V=0\Delta V=0negative hopping imbalance (e.g.,Δ​J=−0.1\Delta J=-0.1and−0.2-0.2) enhances the particle emission and shortens the buildup stage, while positiveΔ​J\Delta Jleads to insignificant excitations within the driving interval. SinceJcJ_{c}is kept fixed, a negativeΔ​J\Delta Jimplies a relative smaller amplitudeJbJ_{b}, which breaks the dynamical balance between the two wells and modifies the effective coupling of the unstable modes to the emission channel, and hence facilitates particle outflow once parametric instability sets in. To further elucidate the behavior, we calculate the particle imbalance|φb,0|2−|φc,0|2|\varphi_{b,0}|^{2}-|\varphi_{c,0}|^{2}, where forΔ​J=0.0\Delta J=0.0,−0.1-0.1and−0.2-0.2the imbalance first increases and subsequently decreases, indicating a buildup followed by particle emission and decay. In contrast, forΔ​J=0.1\Delta J=0.1and0.20.2the imbalance keeps growing throughout, where the system maintains in the stage of buildup with only weak emission. As for the case of|Δ​V|=0.4|\Delta V|=0.4, the interplay between energy detuning and hopping imbalance further enhances the instability. As a consequence, the emission rates can be increased under differentΔ​J\Delta Jwith shorter buildup intervals when compared with that ofΔ​V=0\Delta V=0, and the excited particles gradually saturate.Figure 7:Number of particles|φμ,j|2|\varphi_{\mu,j}|^{2}on thejjth site of each lead as a function of time, when the drive frequency is tuned toω=4\omega=4andω=2\omega=2. The depth of the left well is kept asVc=−2V_{c}=-2, while the right one varies asVb=−2V_{b}=-2,−1.6-1.6, and−2.4-2.4, respectively. The other parameters areg=0.3g=0.3,Jb=0.1J_{b}=0.1,Jc=0.3J_{c}=0.3, andJl=1J_{l}=1.

Finally, we illustrate the structure of the jets by plotting the density distribution of particles on each lead. Since the periodic driving also provides energy in multiples, there can be another drive frequencyω=2\omega=2resulting in significant particle emission. We compare the characteristics of particle jets under the two frequenciesω=4\omega=4andω=2\omega=2for different degrees of depth asymmetry at a fixed hopping imbalance, as shown in Fig.7. For the case ofΔ​V=0\Delta V=0withω=4\omega=4, most of the excited particles move towards the left after the buildup stage due to the hopping imbalance, and then propagate along the left lead. Upon reaching boundary sites, they reverse the direction of motion and gradually return to the central sites, repeating the emission behaviors over time. As forΔ​V=0\Delta V=0andω=2\omega=2the propagation appears similarly, yet with much fewer particles ejected. When the depth asymmetry is tuned toΔ​V=0.4\Delta V=0.4, the emission withω=4\omega=4is slightly reduced, whileω=2\omega=2leads to larger particle jets when compared with that ofΔ​V=0\Delta V=0. With respect toΔ​V=−0.4\Delta V=-0.4, both frequencies result in the enhancement of the visible pulses.

## IVConclusions

We have considered a one-dimensional infinite lattice in which a Bose-Einstein condensate is confined by a double-well potential, and external time-periodic driving is applied to modulate the interatomic interactions. We focus on the nonequilibrium dynamics of collective particle emission from the central sites into the leads, and analyze the roles of the depth asymmetry and the hopping imbalance.

For a symmetric double-well configuration, significant particle jets can be observed when the drive frequency resonates with the energy difference between the local ground state and the first excited state, and the interplay between the drive strength and the hopping amplitude explicitly determines the excitation regimes. When a depth asymmetry between the wells is introduced, moderate biases substantially enhance the emission by improving the resonance condition, whereas excessive asymmetry leads to its suppression due to detuning-induced localization. Further control over the particle jets can be achieved by tuning the hopping amplitudes between the wells and the leads. A finite hopping imbalance modifies the coupling of the unstable modes to the emission channels, thereby altering the emission rate. One can thus, in a specific experiment, manipulate both the intensity and directionality of the jets through the adjustments of either the depth asymmetry or the hopping imbalance, which contributes to the understanding of symmetry-breaking effects in driven quantum systems.

## Acknowledgements

This work was supported by National Natural Science Foundation of China (Grant No. 12505022) and the Natural Science Research Start-up Foundation of Recruiting Talents of Nanjing University of Posts and Telecommunications (Grant No. NY223065). Z.L. received support from Nanhang Jincheng College (Grant Nos. XJ2025003 and 2025JCXY62).

## Appendix AFinite interactionUU

We consider the general case ofVb=Vc≡VV_{b}=V_{c}\equiv Vwith the finite on-site interaction strengthUUbeing included and the periodic driving being absent. Based upon Eqs. (2) and (3) and the stationary ansatz with|β|=|γ|≡ξ|\beta|=|\gamma|\equiv\xi, we obtain the similar energy levels with respect to the symmetric mode and antisymmetric mode, respectively,ϵs(2)\displaystyle\epsilon_{\rm s}^{(2)}=\displaystyle=(V+Uξ2−Jh)+Jμ22​Jl2[(V+Uξ2−Jh)\displaystyle\left(V+U\xi^{2}-J_{h}\right)+\frac{J_{\mu}^{2}}{2J_{l}^{2}}\left[\left(V+U\xi^{2}-J_{h}\right)\right.(22)−i4​Jl2−(V+U​ξ2−Jh)2],\displaystyle\left.-i\sqrt{4J_{l}^{2}-\left(V+U\xi^{2}-J_{h}\right)^{2}}\right],

andϵas(2)\displaystyle\epsilon_{\rm as}^{(2)}=\displaystyle=(V+Uξ2+Jh)+Jμ22​Jl2[(V+Uξ2+Jh)\displaystyle\left(V+U\xi^{2}+J_{h}\right)+\frac{J_{\mu}^{2}}{2J_{l}^{2}}\left[\left(V+U\xi^{2}+J_{h}\right)\right.(23)−i4​Jl2−(V+U​ξ2+Jh)2].\displaystyle\left.-i\sqrt{4J_{l}^{2}-\left(V+U\xi^{2}+J_{h}\right)^{2}}\right].

The square roots𝒜s=4​Jl2−(V+U​ξ2−Jh)2\mathcal{A}_{\rm s}=\sqrt{4J_{l}^{2}-\left(V+U\xi^{2}-J_{h}\right)^{2}}and𝒜as=4​Jl2−(V+U​ξ2+Jh)2\mathcal{A}_{\rm as}=\sqrt{4J_{l}^{2}-\left(V+U\xi^{2}+J_{h}\right)^{2}}explicitly determine the excitation regimes, and basically the availableVVvaries with differentUU.Figure A1:𝒜s\mathcal{A_{\rm s}}and𝒜as\mathcal{A_{\rm as}}vsUUforV=−2V=-2,Jh=1J_{h}=1, andξ=1\xi=1.

According to the typical parameters in the main text, one can verify the properties of𝒜s\mathcal{A}_{\rm s}and𝒜as\mathcal{A}_{\rm as}from Fig.A1: For large on-site interaction strengthU>3U>3, the antisymmetric mode keeps stable and the particle emission can be significantly suppressed (i.e., the self-trapping), while at moderate interactions1<U<31<U<3nonlinear excitations might become prominent and higher-order effects appear, which falls beyond the primary scope of the present work. We are particularly interested in the scenario where the symmetric mode remains stable and the antisymmetric mode is damped (roughly forU<1U<1), and thus in the calculations we specifically work at the limit ofU=0U=0to largely simplify the analysis.

## Appendix BFrequency-domain Green’s function

Here we present the derivation of the frequency-domain Green’s function𝒢11\mathcal{G}_{11}in the main text. We begin from the matrix form of equation of motion forj≥1j\geq 1in Eq. (5),i​∂∂t​(φμ,1φμ,2φμ,3φμ,4⋮)\displaystyle i\frac{\partial}{\partial t}\left(\begin{array}[]{c}\varphi_{\mu,1}\\
\varphi_{\mu,2}\\
\varphi_{\mu,3}\\
\varphi_{\mu,4}\\
\vdots\end{array}\right)=\displaystyle=(0−Jl00⋯−Jl0−Jl0⋯0−Jl0−Jl⋯00−Jl0⋯⋮⋮⋮⋮⋱)​(φμ,1φμ,2φμ,3φμ,4⋮)\displaystyle\left(\begin{array}[]{ccccc}0&-J_{l}&0&0&\cdots\\
-J_{l}&0&-J_{l}&0&\cdots\\
0&-J_{l}&0&-J_{l}&\cdots\\
0&0&-J_{l}&0&\cdots\\
\vdots&\vdots&\vdots&\vdots&\ddots\end{array}\right)\left(\begin{array}[]{c}\varphi_{\mu,1}\\
\varphi_{\mu,2}\\
\varphi_{\mu,3}\\
\varphi_{\mu,4}\\
\vdots\end{array}\right)(45)−Jl​(φμ,0000⋮).\displaystyle-J_{l}\left(\begin{array}[]{c}\varphi_{\mu,0}\\
0\\
0\\
0\\
\vdots\end{array}\right).

Using the Fourier transformφμ,j​(ω)=∫𝑑t​e−i​ω​t​φμ,j​(t)\varphi_{\mu,j}\left(\omega\right)=\int dte^{-i\omega t}\varphi_{\mu,j}\left(t\right), in the frequency domain we get(φμ,1​(ω)φμ,2​(ω)φμ,3​(ω)φμ,4​(ω)⋮)\displaystyle\left(\begin{array}[]{c}\varphi_{\mu,1}\left(\omega\right)\\
\varphi_{\mu,2}\left(\omega\right)\\
\varphi_{\mu,3}\left(\omega\right)\\
\varphi_{\mu,4}\left(\omega\right)\\
\vdots\end{array}\right)=\displaystyle=(ωJl00⋯JlωJl0⋯0JlωJl⋯00Jlω⋯⋮⋮⋮⋮⋱)−1​(−Jl​φμ,0​(ω)000⋮)\displaystyle\left(\begin{array}[]{ccccc}\omega&J_{l}&0&0&\cdots\\
J_{l}&\omega&J_{l}&0&\cdots\\
0&J_{l}&\omega&J_{l}&\cdots\\
0&0&J_{l}&\omega&\cdots\\
\vdots&\vdots&\vdots&\vdots&\ddots\end{array}\right)^{-1}\left(\begin{array}[]{c}-J_{l}\varphi_{\mu,0}\left(\omega\right)\\
0\\
0\\
0\\
\vdots\end{array}\right)(61)=\displaystyle=(𝒢11𝒢12𝒢13⋯𝒢21𝒢22𝒢23⋯𝒢31𝒢32𝒢33⋯𝒢41𝒢42𝒢43⋯⋮⋮⋮⋱)​(−Jl​φμ,0​(ω)000⋮)\displaystyle\left(\begin{array}[]{ccccc}\mathcal{G}_{11}&\mathcal{G}_{12}&\mathcal{G}_{13}&\cdots\\
\mathcal{G}_{21}&\mathcal{G}_{22}&\mathcal{G}_{23}&\cdots\\
\mathcal{G}_{31}&\mathcal{G}_{32}&\mathcal{G}_{33}&\cdots\\
\mathcal{G}_{41}&\mathcal{G}_{42}&\mathcal{G}_{43}&\cdots\\
\vdots&\vdots&\vdots&\ddots\end{array}\right)\left(\begin{array}[]{c}-J_{l}\varphi_{\mu,0}\left(\omega\right)\\
0\\
0\\
0\\
\vdots\end{array}\right)(72)=\displaystyle=(−Jl​φμ,0​(ω)​𝒢11−Jl​φμ,0​(ω)​𝒢21−Jl​φμ,0​(ω)​𝒢31−Jl​φμ,0​(ω)​𝒢41⋮),\displaystyle\left(\begin{array}[]{c}-J_{l}\varphi_{\mu,0}\left(\omega\right)\mathcal{G}_{11}\\
-J_{l}\varphi_{\mu,0}\left(\omega\right)\mathcal{G}_{21}\\
-J_{l}\varphi_{\mu,0}\left(\omega\right)\mathcal{G}_{31}\\
-J_{l}\varphi_{\mu,0}\left(\omega\right)\mathcal{G}_{41}\\
\vdots\end{array}\right),(78)

with𝒢m​n\mathcal{G}_{mn}being the element of the inverse matrix, and a general form forφμ,j\varphi_{\mu,j}is thus straightforward,φμ,j​(ω)=−Jl​φμ,0​(ω)​𝒢j​1​(ω).\varphi_{\mu,j}(\omega)=-J_{l}\varphi_{\mu,0}(\omega)\mathcal{G}_{j1}(\omega).(79)

We assume thatφμ,j​(ω)=η​e−κ​(ω)​j\varphi_{\mu,j}\left(\omega\right)=\eta e^{-\kappa\left(\omega\right)j}. Forj=1j=1,ω​η​e−κ​(ω)=−Jl​[η​e−2​κ​(ω)+φ0​(ω)],\omega\eta e^{-\kappa(\omega)}=-J_{l}\left[\eta e^{-2\kappa(\omega)}+\varphi_{0}(\omega)\right],(80)

from which we obtainη=−Jl​eκ​(ω)ω+J​e−κ​(ω),\eta=\frac{-J_{l}e^{\kappa(\omega)}}{\omega+Je^{-\kappa(\omega)}},(81)

while forj>1j>1,ω​e−κ​(ω)​j\displaystyle\omega e^{-\kappa\left(\omega\right)j}=\displaystyle=−Jl​[e−κ​(ω)​(j+1)+e−κ​(ω)​(j−1)],\displaystyle-J_{l}\left[e^{-\kappa\left(\omega\right)\left(j+1\right)}+e^{-\kappa\left(\omega\right)\left(j-1\right)}\right],(82)

i.e.,2​cosh⁡κ​(ω)=−ωJl.2\cosh\kappa\left(\omega\right)=-\frac{\omega}{J_{l}}.(83)

The value ofκ\kappatypically depends on the driving frequency. For|ω|>2​Jl|\omega|>2J_{l},κ\kappais real, giving rise to evanescent modes in the leads and hence bound-state behavior without dissipation. As for|ω|<2​Jl|\omega|<2J_{l}, the complexκ\kappacorresponds to propagating modes in the leads. In this regime, the leads act as a continuum bath, allowing particles to escape to infinity and thus leading to distinct particle jets. Inserting Eq. (83) into Eq. (81) that we immediately haveλ=φ0​(ω)\lambda=\varphi_{0}(\omega), and according to Eq. (79) we can reach𝒢j​1​(ω)=−e−κ​(ω)​jJl\mathcal{G}_{j1}\left(\omega\right)=-\frac{e^{-\kappa\left(\omega\right)j}}{J_{l}}(84)

withκ​(ω)=Arc​[cosh⁡(−ω2​Jl)].\kappa\left(\omega\right)={\rm Arc}\left[\cosh\left(-\frac{\omega}{2J_{l}}\right)\right].(85)

As for𝒢11​(ω)\mathcal{G}_{11}\left(\omega\right), we have the quadratic equationJl2​𝒢11​(ω)+1𝒢11​(ω)\displaystyle J_{l}^{2}\mathcal{G}_{11}(\omega)+\frac{1}{\mathcal{G}_{11}(\omega)}=\displaystyle=−Jl​e−κ​(ω)−Jl​eκ​(ω),\displaystyle-J_{l}e^{-\kappa\left(\omega\right)}-J_{l}e^{\kappa\left(\omega\right)},(86)

which yields𝒢11​(ω)\displaystyle\mathcal{G}_{11}(\omega)=\displaystyle=ω2​Jl2−i​1Jl2−ω24​Jl4.\displaystyle\frac{\omega}{2J_{l}^{2}}-i\sqrt{\frac{1}{J_{l}^{2}}-\frac{\omega^{2}}{4J_{l}^{4}}}.(87)

## Appendix CMethod of multiple scales

Based on the two-mode approximation, we utilize the method of multiple scales and make the ansatzb0​(t)\displaystyle b_{0}\left(t\right)=\displaystyle=e−i​(V−Jh)​t​χ​(t)+e−i​(V+Jh)​t​λ​(t),\displaystyle e^{-i(V-J_{h})t}\chi(t)+e^{-i(V+J_{h})t}\lambda(t),(88)c0​(t)\displaystyle c_{0}\left(t\right)=\displaystyle=e−i​(V−Jh)​t​χ​(t)−e−i​(V+Jh)​t​λ​(t).\displaystyle e^{-i(V-J_{h})t}\chi(t)-e^{-i(V+J_{h})t}\lambda(t).(89)

We also use the notationϵs=V−Jh\epsilon_{\rm{s}}=V-J_{h},ϵas=V+Jh\epsilon_{\rm{as}}=V+J_{h}andJμ≡JJ_{\mu}\equiv Jin the following, and the equations of motion forχ\chiandλ\lambdaare thus straightforwardi​ei​ϵs​t​∂tb0+c02\displaystyle ie^{i\epsilon_{\rm{s}}t}\partial_{t}\frac{b_{0}+c_{0}}{2}=\displaystyle=(ϵs+i​∂t)​χ\displaystyle\left(\epsilon_{\rm{s}}+i\partial_{t}\right)\chi(90)=\displaystyle=[V−Jh+J2​𝒢11​(ϵs)]​χ\displaystyle\left[V-J_{h}+J^{2}\mathcal{G}_{11}\left(\epsilon_{\rm{s}}\right)\right]\chi+ei​ϵs​t2​g​(t)​(|b0|2​b0+|c0|2​c0),\displaystyle+\frac{e^{i\epsilon_{\rm{s}}t}}{2}g\left(t\right)\left(|b_{0}|^{2}b_{0}+|c_{0}|^{2}c_{0}\right),i​ei​ϵas​t​∂tb0−c02\displaystyle ie^{i\epsilon_{\rm{as}}t}\partial_{t}\frac{b_{0}-c_{0}}{2}=\displaystyle=(ϵas+i​∂t)​λ\displaystyle\left(\epsilon_{\rm{as}}+i\partial_{t}\right)\lambda(91)=\displaystyle=[V+Jh+J2​𝒢11​(ϵas)]​λ\displaystyle\left[V+J_{h}+J^{2}\mathcal{G}_{11}\left(\epsilon_{\rm{as}}\right)\right]\lambda+ei​ϵas​t2​g​(t)​(|b0|2​b0−|c0|2​c0).\displaystyle+\frac{e^{i\epsilon_{\rm{as}}t}}{2}g\left(t\right)\left(|b_{0}|^{2}b_{0}-|c_{0}|^{2}c_{0}\right).

There will be a resonance when the drive frequency is tuned toω=2​(ϵas−ϵs)\omega=2\left(\epsilon_{\rm{as}}-\epsilon_{\rm{s}}\right), and we keep only the resonant terms, such thatei​ϵs​t2​g​sin⁡(ω​t)​(|b0|2​b0+|c0|2​c0)\displaystyle\frac{e^{i\epsilon_{\rm{s}}t}}{2}g\sin\left(\omega t\right)\left(|b_{0}|^{2}b_{0}+|c_{0}|^{2}c_{0}\right)≈\displaystyle\approxg2​i​λ2​χ∗,\displaystyle\frac{g}{2i}\lambda^{2}\chi^{*},(92)ei​ϵas​t2​g​sin⁡(ω​t)​(|b0|2​b0−|c0|2​c0)\displaystyle\frac{e^{i\epsilon_{\rm{as}}t}}{2}g\sin\left(\omega t\right)\left(|b_{0}|^{2}b_{0}-|c_{0}|^{2}c_{0}\right)≈\displaystyle\approx−g2​i​χ2​λ∗,\displaystyle\frac{-g}{2i}\chi^{2}\lambda^{*},(93)

and the equations of motion becomei​∂tχ\displaystyle i\partial_{t}\chi=\displaystyle=Jh2​𝒢11​(ϵs)​χ+g2​i​λ2​χ∗,\displaystyle J_{h}^{2}\mathcal{G}_{11}\left(\epsilon_{\rm{s}}\right)\chi+\frac{g}{2i}\lambda^{2}\chi^{*},(94)i​∂tλ\displaystyle i\partial_{t}\lambda=\displaystyle=Jh2​𝒢11​(ϵas)​λ−g2​i​χ2​λ∗,\displaystyle J_{h}^{2}\mathcal{G}_{11}\left(\epsilon_{\rm as}\right)\lambda-\frac{g}{2i}\chi^{2}\lambda^{*},(95)

which leads to∂t|χ|2\displaystyle\partial_{t}|\chi|^{2}=\displaystyle=−Ωs​|χ|2−g2​[(χ∗​λ)2+(λ∗​χ)2],\displaystyle-\Omega_{\rm s}|\chi|^{2}-\frac{g}{2}\left[\left(\chi^{*}\lambda\right)^{2}+\left(\lambda^{*}\chi\right)^{2}\right],(96)∂t|λ|2\displaystyle\partial_{t}|\lambda|^{2}=\displaystyle=−Ωas​|λ|2+g2​[(χ∗​λ)2+(λ∗​χ)2],\displaystyle-\Omega_{\rm as}|\lambda|^{2}+\frac{g}{2}\left[\left(\chi^{*}\lambda\right)^{2}+\left(\lambda^{*}\chi\right)^{2}\right],(97)

whereΩs=−2​J2​Im​𝒢11​(ϵs)\Omega_{\rm s}=-2J^{2}{\rm Im}\mathcal{G}_{11}\left(\epsilon_{\rm s}\right)andΩas=−2​J2​Im​𝒢11​(ϵas)\Omega_{\rm as}=-2J^{2}{\rm Im}\mathcal{G}_{11}\left(\epsilon_{\rm as}\right). Since we seed the system in the symmetric modeΩs=0\Omega_{s}=0, a simplification of treatingχ\chiandλ\lambdato be real yields∂tχ\displaystyle\partial_{t}\chi=\displaystyle=−g2​λ2​χ,\displaystyle-\frac{g}{2}\lambda^{2}\chi,(98)∂tλ\displaystyle\partial_{t}\lambda=\displaystyle=−Ωas2​λ+g2​χ2​λ.\displaystyle-\frac{\Omega_{\rm as}}{2}\lambda+\frac{g}{2}\chi^{2}\lambda.(99)

These equations can readily be solved numerically, and the total particle number and particle imbalance are approximated, respectively,|b0|2+|c0|2\displaystyle|b_{0}|^{2}+|c_{0}|^{2}=\displaystyle=2​(χ2+λ2),\displaystyle 2\left(\chi^{2}+\lambda^{2}\right),(100)|b0|2−|c0|2\displaystyle|b_{0}|^{2}-|c_{0}|^{2}=\displaystyle=4​χ​λ​cos⁡(2​Jh​t).\displaystyle 4\chi\lambda\cos\left(2J_{h}t\right).(101)

## References
- [1]I. Bloch, J. Dalibard, and W. Zwerger, Many-body physics with ultracold gases,Rev. Mod. Phys.80, 885 (2008).
- [2]C. Chin, R. Grimm, P. Julienne, and E. Tiesinga, Feshbach resonances in ultracold gases,Rev. Mod. Phys.82, 1225 (2010).
- [3]R. Gati and M. K. Oberthaler, A bosonic Josephson junction,J. Phys. B: At. Mol. Opt. Phys.40, R61 (2007).
- [4]G. J. Milburn, J. Corney, E. M. Wright, and D. F. Walls, Quantum dynamics of an atomic Bose-Einstein condensate in a double-well potential,Phys. Rev. A55, 4318 (1997).
- [5]D. Ananikian and T. Bergeman, Gross-Pitaevskii equation for Bose particles in a double-well potential: Two-mode models and beyond,Phys. Rev. A73, 013604 (2006).
- [6]S. Giovanazzi, A. Smerzi, and S. Fantoni, Josephson Effects in Dilute Bose-Einstein Condensates,Phys. Rev. Lett.84, 4521 (2000).
- [7]Y. Shin, M. Saba, A. Schirotzek, T. A. Pasquini, A. E. Leanhardt, D. E. Pritchard, and W. Ketterle, Distillation of Bose-Einstein Condensates in a Double-Well Potential,Phys. Rev. Lett.92, 150401 (2004).
- [8]S. Giovanazzi, J. Esteve, and M. K. Oberthaler, Effective parameters for weakly coupled Bose-Einstein condensates,New J. Phys.10, 045009 (2008).
- [9]B. Juliá-Díaz, J. Martorell, M. Melé-Messeguer, and A. Polls, Beyond standard two-mode dynamics in bosonic Josephson junctions,Phys. Rev. A82, 063626 (2010).
- [10]Y. Y. Qian, M. Gong, and C. W. Zhang, Quantum transport of bosonic cold atoms in double-well optical lattices,Phys. Rev. A84, 013608 (2011).
- [11]H. Susanto, J. Cuevas, and P. Krüger, Josephson tunnelling of dark solitons in a double-well potential,J. Phys. B: At. Mol. Opt. Phys.44, 095003 (2011).
- [12]D.-W. Zhang, L.-B. Fu, Z. D. Wang, and S.-L. Zhu, Josephson dynamics of a spin-orbit-coupled Bose-Einstein condensate in a double-well potential,Phys. Rev. A85, 043609 (2012).
- [13]H.-L. Zheng and Q. Gu, Dynamics of Bose-Einstein condensates in a one-dimensional optical lattice with double-well potential,Front. Phys.8, 375 (2013).
- [14]J. P. Hou, X.-W. Luo, K. Sun, T. Bersano, V. Gokhroo, S. Mossman, P. Engels, and C. W. Zhang, Momentum-Space Josephson Effects,Phys. Rev. Lett.120, 120401 (2018).
- [15]Y.-J. Ying and H.-B. Li, Dynamics of Bose-Einstein condensation in an asymmetric double-well potential,Acta Phys. Sin.72, 130303 (2023).
- [16]J. Sicks and H. Rieger, Double-well Bose-Hubbard model with nearest-neighbor and cavity-mediated long-range interactions,Phys. Rev. A109, 033317 (2024).
- [17]D. A. Hamza and J. Chwedeńczuk, Metrology using atoms in an array of double-well potentials,arXiv:2507.11395.
- [18]L. Pitaevskii and S. Stringari, Thermal vs Quantum Decoherence in Double Well Trapped Bose-Einstein Condensates,Phys. Rev. Lett.87, 180402 (2001).
- [19]Y. Shin, M. Saba, T. A. Pasquini, W. Ketterle, D. E. Pritchard, and A. E. Leanhardt, Atom Interferometry with Bose-Einstein Condensates in a Double-Well Potential,Phys. Rev. Lett.92, 050405 (2004).
- [20]S. Raghavan, A. Smerzi, S. Fantoni, and S. R. Shenoy, Coherent oscillations between two weakly coupled Bose-Einstein condensates: Josephson effects,π\pioscillations, and macroscopic quantum self-trapping,Phys. Rev. A59, 620 (1999).
- [21]A. N. Salgueiro, A.F.R. de Toledo Piza, G. B. Lemos, R. Drumond, M. C. Nemes, and M. Weidemüller, Quantum dynamics of bosons in a double-well potential: Josephson oscillations, self-trapping and ultralong tunneling times,Eur. Phys. J. D44, 537 (2007).
- [22]W. Wang, L. B. Fu, and X. X. Yi, Effect of decoherence on the dynamics of Bose-Einstein condensates in a double-well potential,Phys. Rev. A75, 045601 (2007).
- [23]S. K. Adhikari, Josephson oscillation and induced collapse in an attractive Bose-Einstein condensate,Phys. Rev. A72, 013619 (2005).
- [24]M. Abad, M. Guilleumas, R. Mayol, F. Piazza, D. M. Jezek, and A. Smerzi, Phase slips and vortex dynamics in Josephson oscillations between Bose-Einstein condensates,EPL109, 40005 (2015).
- [25]Y. D. van Nieuwkerk, J. Schmiedmayer, and F. H. L. Essler, Josephson oscillations in split one-dimensional Bose gases,SciPost Phys.10, 090 (2021).
- [26]J. Gillet, M. A. Garcia-March, Th. Busch, and F. Sols, Tunneling, self-trapping, and manipulation of higher modes of a Bose-Einstein condensate in a double well,Phys. Rev. A89, 023614 (2014).
- [27]T. Zibold, E. Nicklas, C. Gross, and M. K. Oberthaler, Classical Bifurcation at the Transition from Rabi to Josephson Dynamics,Phys. Rev. Lett.105, 204101 (2010).
- [28]R. Roy, B. Chakrabarti, and A. Trombettoni, Quantum dynamics of few dipolar bosons in a double-well potential,Eur. Phys. J. D76, 24 (2022).
- [29]A. Smerzi, S. Fantoni, S. Giovanazzi, and S. R. Shenoy, Quantum Coherent Atomic Tunneling between Two Trapped Bose-Einstein Condensates,Phys. Rev. Lett.79, 4950 (1997).
- [30]M. Abad, M. Guilleumas, R. Mayol, M. Pi, and D. M. Jezek, Phase slippage and self-trapping in a self-induced bosonic Josephson junction,Phys. Rev. A84, 035601 (2011).
- [31]M. Albiez, R. Gati, J. F?lling, S. Hunsmann, M. Cristiani, and M. K. Oberthaler, Direct Observation of Tunneling and Nonlinear Self-Trapping in a Single Bosonic Josephson Junction,Phys. Rev. Lett.95, 010402 (2005).
- [32]S. Z?llner, H.-D. Meyer, and P. Schmelcher, Tunneling dynamics of a few bosons in a double well,Phys. Rev. A78, 013621 (2008).
- [33]S. Z?llner, H.-D. Meyer, and P. Schmelcher, Few-Boson Dynamics in Double Wells: From Single-Atom to Correlated Pair Tunneling,Phys. Rev. Lett.100, 040401 (2008).
- [34]B. Chatterjee, I. Brouzos, S. Z?llner, and P. Schmelcher, Few-boson tunneling in a double well with spatially modulated interaction,Phys. Rev. A82, 043619 (2010).
- [35]M. Maraj, J.-B. Wang, J.-S. Pan, and W. Yi, Interaction-modulated tunneling dynamics in a mixture of Bose-Einstein condensates,Eur. Phys. J. D71, 300 (2017).
- [36]L. Q. Lai, Y. B. Yu, and E. J. Mueller, Resonant enhancement of particle emission from a parametrically driven condensate in a one-dimensional lattice,Phys. Rev. A106, 033302 (2022).
- [37]L. Q. Lai and Z. Li, Effects of drive imbalance on the particle emission from a Bose-Einstein condensate in a one-dimensional lattice,Chin. Phys. B33, 030308 (2024).
- [38]F. S. Cataliotti, S. Burger, C. Fort, P. Maddaloni, F. Minardi, A. Trombettoni, A. Smerzi, and M. Inguscio, Josephson Junction Arrays with Bose-Einstein Condensates,Science293, 843 (2001).
- [39]O. Morsch and M. Oberthaler, Dynamics of Bose-Einstein condensates in optical lattices,Rev. Mod. Phys.78, 179 (2006).
- [40]S. I. Mistakidis, A. G. Volosniev, R. E. Barfknecht, T. Fogarty, Th. Busch, A. Foerster, P. Schmelcher, and N. T. Zinner, Few-body Bose gases in low dimensions—A laboratory for quantum dynamics,Phys. Rep.1042, 1 (2023).
- [41]T. Schumm, S. Hofferberth, L. M. Andersson, S. Wildermuth, S. Groth, I. Bar-Joseph, J. Schmiedmayer, and P. Krüger, Matter-wave interferometry in a double well on an atom chip,Nat. Phys.1, 57 (2005).
- [42]G. Theocharis, P. G. Kevrekidis, D. J. Frantzeskakis, and P. Schmelcher, Symmetry breaking in symmetric and asymmetric double-well potentials,Phys. Rev. E74, 056608 (2006).
- [43]B. V. Hall, S. Whitlock, R. Anderson, P. Hannaford, and A. I. Sidorov, Condensate Splitting in an Asymmetric Double Well for Atom Chip Based Sensors,Phys. Rev. Lett.98, 030402 (2007).
- [44]H. M. Cataldo and D. M. Jezek, Dynamics in asymmetric double-well condensates,Phys. Rev. A90, 043610 (2014).
- [45]S. J. Kim, H. Yu, S. T. Gang, D. Z. Anderson, and J. B. Kim, Controllable asymmetric double well and ring potential on an atom chip,Phys. Rev. A93, 033612 (2016).
- [46]M. Gavrilov and J. Bechhoefer, Erasure without Work in an Asymmetric Double-Well Potential,Phys. Rev. Lett.117, 200601 (2016).
- [47]J. G. Cosme, M. F. Andersen, and J. Brand, Interaction blockade for bosons in an asymmetric double well,Phys. Rev. A96, 013616 (2017).
- [48]S. K. Haldar and O. E. Alon, Many-body quantum dynamics of an asymmetric bosonic Josephson junction,New J. Phys.21, 103037 (2019).
- [49]D. R. Lindberg, N. Gaaloul, L. Kaplan, J. R. Williams, D. Schlippert, P. Boegel, E.-M. Rasel, and D. I. Bondar, Asymmetric tunneling of Bose-Einstein condensates,J. Phys. B: At. Mol. Opt. Phys.56, 025302 (2023).
- [50]K. Korshynska and S. Ulbricht, Generalized Josephson effect in an asymmetric double-well potential at finite temperatures,Phys. Rev. A109, 043321 (2024).
- [51]A. Trenkwalder, G. Spagnolli, G. Semeghini, S. Coop, M. Landini, P. Castilho, L. Pezzè, G. Modugno, M. Inguscio, A. Smerzi, and M. Fattori, Quantum phase transitions with parity-symmetry breaking and hysteresis,Nat. Phys.12, 826 (2016).
- [52]C. P. Rubbo, S. R. Manmana, B. M. Peden, M. J. Holland, and A. M. Rey, Resonantly enhanced tunneling and transport of ultracold atoms on tilted optical lattices,Phys. Rev. A84, 033638 (2011).
- [53]C. Sias, A. Zenesini, H. Lignier, S. Wimberger, D. Ciampini, O. Morsch, and E. Arimondo, Resonantly Enhanced Tunneling of Bose-Einstein Condensates in Periodic Potentials,Phys. Rev. Lett.98, 120403 (2007).
- [54]A. Zenesini, C. Sias, H. Lignier, Y. Singh, D. Ciampini, O. Morsch, R. Mannella, E. Arimondo, A. Tomadin, and S. Wimberger, Resonant tunneling of Bose-Einstein condensates in optical lattices,New J. Phys.10, 053038 (2008).
- [55]A. S. Buyskikh, L. Tagliacozzo, D. Schuricht, C. A. Hooley, D. Pekker, and A. J. Dale, Resonant two-site tunneling dynamics of bosons in a tilted optical superlattice,Phys. Rev. A100, 023627 (2019).
- [56]A. Bhowmik and O. E. Alon, Longitudinal and transversal resonant tunneling of interacting bosons in a two-dimensional Josephson junction,Sci. Rep.12, 627 (2022).
- [57]L. Q. Lai and Z. Li, Interference-induced suppression of particle emission from a Bose-Einstein condensate in lattice with time-periodic modulations,Chin. Phys. B33, 100303 (2024).
- [58]L. Q. Lai, Z. Li, Q. H. Liu, and Y. B. Yu, Intermittent Emission of Particles from a Bose-Einstein Condensate in a 1D Lattice,Ann. Phys. (Berlin)536, 2300365 (2024).
- [59]L. W. Clark, A. Gaj, L. Feng, and C. Chin, Collective emission of matter-wave jets from driven Bose–Einstein condensates,Nature551, 356 (2017).
- [60]H. Fu, L. Feng, B. M. Anderson, L. W. Clark, J. Z. Hu, J. W. Andrade, C. Chin, and K. Levin, Density Waves and Jet Emission Asymmetry in Bose Fireworks,Phys. Rev. Lett.121, 243001 (2018).

## 


- 


Major funding support from
