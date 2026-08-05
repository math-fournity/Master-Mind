# Anomalous Boundary Modes in a Floquet Hyperbolic System

**arXiv ID**: 2607.28719v1
**Authors**: Ali Fahimniya, Hossein Dehghani, Alicia J. Kollár, Alexey V. Gorshkov
**Published**: 2026-07-30
**Categories**: cond-mat.mes-hall, cond-mat.other, quant-ph
**Comments**: 15 pages, 11 figures
**HTML URL**: https://arxiv.org/html/2607.28719v1

## Abstract

We construct an anomalous Floquet topological phase on a negatively curved hyperbolic lattice. The model is a tight-binding Hamiltonian with a periodically repeated four-color edge-hopping sequence and a sublattice-staggered onsite potential step. The topological regime is reached near the limit in which a single hopping step transfers amplitude completely across an active edge, while the trivial regime is reached near the point where two full hops occur along an active edge during a single hopping step, returning the amplitude to its starting site. In finite open patches, the topological regime is characterized by bulk quasienergy gaps at $0$ and $π$ that are populated by in-gap states, in contrast to a trivial regime where these gaps remain empty. Using compact periodic lattices, we map the bulk $0$ and $π$ quasienergy gaps and identify the gapped regions connected to the trivial and anomalous open-boundary spectra. We diagnose the in-gap states as chiral boundary modes by their real-space dynamics. Finally, we introduce a small-boundary spectral-flow diagnostic based on punctured periodic hyperbolic lattices, which avoids the ambiguity associated with the extensive outer boundary of finite hyperbolic patches. This puncture-based diagnostic should be useful for studying other topological hyperbolic systems.

## Full Text

Anomalous Boundary Modes in a Floquet Hyperbolic System

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
- License: CC BY 4.0arXiv:2607.28719v1 [cond-mat.mes-hall] 30 Jul 2026

## Anomalous Boundary Modes in a Floquet Hyperbolic SystemAli Fahimniyafahim@umd.eduJoint Center for Quantum Information and Computer Science, NIST/University of Maryland, College Park, Maryland 20742, USAJoint Quantum Institute, NIST/University of Maryland, College Park, Maryland 20742, USAHossein DehghaniCurrent address: QuEra Computing Inc., Boston, MA 02135, USAJoint Center for Quantum Information and Computer Science, NIST/University of Maryland, College Park, Maryland 20742, USAJoint Quantum Institute, NIST/University of Maryland, College Park, Maryland 20742, USAAlicia J. KollárJoint Quantum Institute, NIST/University of Maryland, College Park, Maryland 20742, USADepartment of Physics, University of Maryland, College Park, MD 20742, USAMaryland Quantum Materials Center, Department of Physics, University of Maryland, College Park, MD 20742, USAAlexey V. GorshkovJoint Center for Quantum Information and Computer Science, NIST/University of Maryland, College Park, Maryland 20742, USAJoint Quantum Institute, NIST/University of Maryland, College Park, Maryland 20742, USA

## Abstract

We construct an anomalous Floquet topological phase on a negatively curved hyperbolic lattice. The model is a tight-binding Hamiltonian with a periodically repeated four-color edge-hopping sequence and a sublattice-staggered onsite potential step. The topological regime is reached near the limit in which a single hopping step transfers amplitude completely across an active edge, while the trivial regime is reached near the point where two full hops occur along an active edge during a single hopping step, returning the amplitude to its starting site. In finite open patches, the topological regime is characterized by bulk quasienergy gaps at0andπ\pithat are populated by in-gap states, in contrast to a trivial regime where these gaps remain empty. Using compact periodic lattices, we map the bulk0andπ\piquasienergy gaps and identify the gapped regions connected to the trivial and anomalous open-boundary spectra. We diagnose the in-gap states as chiral boundary modes by their real-space dynamics. Finally, we introduce a small-boundary spectral-flow diagnostic based on punctured periodic hyperbolic lattices, which avoids the ambiguity associated with the extensive outer boundary of finite hyperbolic patches. This puncture-based diagnostic should be useful for studying other topological hyperbolic systems.

## IIntroduction

Floquet engineering provides a route to designing band structures, gauge fields, and topological phases through periodic time dependence rather than through static material parameters[1,2,3,4]. Early proposals showed that irradiation can induce Hall or topological-insulator responses in otherwise ordinary systems, including graphene and semiconductor quantum wells[5,6]. More generally, a periodically driven system with driving periodTTis governed stroboscopically by a one-period unitary evolution operator, whose eigenphases define quasienergies modulo2​π/T2\pi/T. This quasienergy periodicity gives Floquet band topology a structure that is richer than that of static Bloch bands[7,8,9,10,11]. In particular, the anomalous Floquet insulator introduced by Rudneret al.supports chiral edge modes even when the Chern numbers of all Floquet bands vanish[8]. Such anomalous edge transport is not only a theoretical possibility: photonic Floquet topological insulators and anomalous Floquet edge modes have been observed in periodically modulated waveguide lattices[12,13,14]. Related anomalous-Floquet physics has also been realized in acoustic, ultracold-atom, and nanophotonic resonator platforms[15,16,17]. Periodic driving therefore separates the topology of the full time evolution from the topology of individual static-like bands, making it a natural setting for engineering boundary motion directly.

Hyperbolic lattices provide a complementary setting in which boundary physics is unusually prominent. A regular tiling may be denoted by a Schläfli symbol{p,q}\{p,q\}, whereppis the number of sides of each polygonal face andqqis the number of polygons meeting at each vertex[18]. Hyperbolic tilings obey(p−2)​(q−2)>4(p-2)(q-2)>4, in contrast to Euclidean regular tilings where equality holds. A key consequence of negative curvature is that finite patches of hyperbolic lattices have an extensive boundary: the number of boundary sites remains a finite fraction of the total number of sites even as the system grows. This feature is especially relevant for topological systems, whose most visible physical signatures are often boundary modes. It also complicates standard diagnostics because the usual separation between a large bulk and a negligible boundary is absent in open hyperbolic flakes.

The experimental motivation for hyperbolic tight-binding models has grown rapidly. Networks of superconducting coplanar waveguide resonators have realized effective hyperbolic lattices for microwave photons[19]. Classical electric-circuit platforms have independently emulated hyperbolic space on a circuit board and have been used to engineer hyperbolic matter with tunable complex phases[20,21]. Related circuit experiments have observed boundary-dominated topological states and higher-order modes in engineered hyperbolic lattices[22]. Photonic platforms are also emerging: coupled optical ring resonators on silicon chips have realized hyperbolic photonic topological insulators, and programmable coupled-resonator photonics has been proposed as a scalable route for emulating hyperbolic-lattice wave dynamics[23,24]. These developments make hyperbolic lattices a realistic synthetic-matter platform rather than only a mathematical generalization of Euclidean crystalline systems.

On the theory side, hyperbolic band theory differs sharply from ordinary Bloch theory because the relevant translation groups are nonabelian. Work on hyperbolic Bloch theory, automorphic Bloch theorems, hyperbolic crystallography, and higher-dimensional representations has developed tools for describing spectra of infinite or compactified hyperbolic lattices[25,26,27,28]. Complementary progress on converging periodic boundary conditions and supercell constructions has provided practical routes to approximating thermodynamic-limit spectra and non-Abelian Bloch sectors of hyperbolic lattices[29,30]. Topological hyperbolic systems have also been explored in several forms, including hyperbolic analogues of quantum spin Hall systems[31], Chern insulators on the{8,3}\{8,3\}lattice[32], hyperbolic Haldane and Kane–Mele models[33], higher-order topological hyperbolic phases[34,35,36], linear Chern responses[37], and nonreciprocal hyperbolic scattering networks with anomalous and Chern chiral edge modes[38]. This body of work establishes that hyperbolic geometry is not a passive background: the extensive boundary, noncommutative translation structure, and available synthetic implementations all reshape the usual questions of band topology and bulk-boundary correspondence.

Here we construct a Hamiltonian Floquet model on the{8,3}\{8,3\}hyperbolic lattice, in the spirit of the Rudner hopping protocol[8](see Fig.1). The lattice consists of regular octagons with three octagons meeting at each vertex. We use a periodic 16-site coloring of the lattice edges into four classes (four colors). During the drive, hopping is activated on these four edge classes in a repeated sequence, followed by a sublattice-staggered onsite potential. We identify a topological regime near the perfect-hopping limit, where one active step transfers amplitude completely across an edge, and a trivial regime near the point where two full hops occur along an active edge during a single hopping step, returning the amplitude to its starting site. We diagnose the resulting anomalous Floquet regime through the density of states of finite flakes and periodic lattices, chiral boundary wave-packet dynamics, and finally, spectral flow in punctured compact hyperbolic geometries.

The remainder of this paper is organized as follows. SectionIIintroduces the hyperbolic{8,3}\{8,3\}lattice, its four-color edge decomposition, and the corresponding Floquet drive, including the real-space dynamics at the perfect-hopping point. SectionIIIpresents the numerical characterization of the resulting phases. We first compare the quasienergy densities of states of finite open patches in Sec.III.1, and then map the bulk0andπ\pigaps using periodic lattices in Sec.III.2. SectionIII.3demonstrates the chiral propagation of a boundary wave packet, while Sec.III.4introduces a controlled internal boundary in a compact periodic lattice and diagnoses the anomalous Floquet phase through puncture-boundary spectral flow. Finally, Sec.IVsummarizes the implications of these results and discusses generalizations to other hyperbolic lattices, real-space topological diagnostics, and possible experimental realizations.

## IIModel

## II.1Hyperbolic lattice and periodic edge coloringFigure 1:Hyperbolic{8,3}\{8,3\}lattice and four-color hopping protocol.The lattice consists of regular octagons with three octagons meeting at each bulk vertex. Black and white vertices denote the two sublattices. The shaded region marks a 16-site fundamental domain of the colored lattice. The lattice edges are divided into four color classes, blue, green, red, and orange. The four-step color cycle blue–green–red–orange is repeated four times and is followed by a sublattice-staggered onsite potential step. Purple-circled vertices mark the four inequivalent bulk vertex types of the colored lattice, while cyan-circled vertices show representative boundary-propagating sites. Arrows show perfect-hopping point motion of each site over one quarter of the hopping schedule.

We consider the regular hyperbolic tessellation{8,3}\{8,3\}, whose faces are octagons and whose bulk vertices have coordination number three. Finite open-boundary systems are generated by starting from a central octagon and adding shells of neighboring octagons. The first shell is the central octagon; the next shell consists of octagons adjacent to it; subsequent shells are defined recursively by adding octagons adjacent to the previous shells but not already included. Boundary sites of an open patch are defined graph-theoretically as vertices whose degree is reduced from the bulk value three to degree two. This definition distinguishes sites affected by the finite boundary truncation, which are candidates for supporting the boundary states discussed below, from degree-three sites that primarily contribute to bulk states.

The hopping protocol is based on a periodic coloring of the edges. The colored lattice has a 16-site fundamental domain, shown schematically in Fig.1. This unit cell is associated with the hyperbolic crystallographic description of the{8,3}\{8,3\}lattice[27]. Every edge belongs to exactly one of four color classes, denotedEb,Eg,Er,Eo,E_{b},\quad E_{g},\quad E_{r},\quad E_{o},(1)

corresponding to blue, green, red, and orange edges. The blue and red edges each form a perfect matching, i.e., each vertex is at the end of exactly one blue and exactly one red edge. The green and orange edges together form a third perfect matching. Consequently, each bulk vertex is incident on one blue edge, one red edge, and one edge that is either green or orange. The green and orange colors alternate spatially: after traversing a green edge and then a blue or red edge, one arrives at a vertex whose green-or-orange matching edge is orange, and conversely with green and orange interchanged. The coloring, along with the sublattice-staggered onsite potential defined below, breaks the full vertex equivalence of the uncolored{8,3}\{8,3\}lattice. As indicated by the purple-circled vertices in Fig.1, the 16 sites in the fundamental domain reduce to four inequivalent vertex types under the residual fourfold rotation symmetry.

The graph is bipartite, and we denote the two sublattices byAAandBB, indicated by white and black vertices in Fig.1, respectively. The bipartite structure is used in the onsite potential step of the drive below.

## II.2Floquet hopping protocol

For each color classμ=b,g,r,o\mu=b,g,r,o, we define a nearest-neighbor hopping HamiltonianHμ=−J​∑⟨i​j⟩∈Eμ(ci†​cj+cj†​ci),J>0,H_{\mu}=-J\sum_{\langle ij\rangle\in E_{\mu}}\left(c_{i}^{\dagger}c_{j}+c_{j}^{\dagger}c_{i}\right),\qquad J>0,(2)

whereci†c_{i}^{\dagger}creates a particle on siteii, and we setℏ=1\hbar=1. The hopping is real and thus reciprocal in the main model. Peierls phases are introduced only in the spectral-flow calculations discussed in Sec.III.4.

The hopping part of the drive consists of a 16-step sequence obtained by repeating the four-step blue–green–red–orange hopping schedule four times.
Each step has durationTsT_{s}. The hopping sequence is followed by a sublattice-staggered onsite potential stepHδ=δ​∑iηi​ci†​ci,ηi={+1,i∈A,−1,i∈B.H_{\delta}=\delta\sum_{i}\eta_{i}c_{i}^{\dagger}c_{i},\qquad\eta_{i}=\begin{cases}+1,&i\in A,\\
-1,&i\in B.\end{cases}(3)

The full Floquet period is thereforeT=17​Ts.T=17T_{s}.(4)

LetUμ=e−i​Hμ​Ts,Uδ=e−i​Hδ​Ts.U_{\mu}=e^{-\mathrm{i}H_{\mu}T_{s}},\qquad U_{\delta}=e^{-\mathrm{i}H_{\delta}T_{s}}.(5)

The unitary evolution during a Floquet period is determined by the Floquet operator that isUF=Uδ​(Uo​Ur​Ug​Ub)4.U_{F}=U_{\delta}\left(U_{o}U_{r}U_{g}U_{b}\right)^{4}.(6)

Because the Hamiltonian is periodic in time,H​(t+T)=H​(t)H(t+T)=H(t), the eigenvectors ofUFU_{F}are Floquet states and the eigenphases ofUFU_{F}define quasienergies,UF​|ψα⟩=e−i​εα​T​|ψα⟩,εα​T∈(−π,π].U_{F}|\psi_{\alpha}\rangle=e^{-\mathrm{i}\varepsilon_{\alpha}T}|\psi_{\alpha}\rangle,\qquad\varepsilon_{\alpha}T\in(-\pi,\pi].(7)

The quasienergy is defined only modulo2​π/T2\pi/T, so the spectrum is naturally defined on a circle rather than on a line. As a result, gaps atε​T=0\varepsilon T=0andε​T=π\varepsilon T=\piare both meaningful. In an anomalous Floquet phase, chiral boundary states can traverse these quasienergy gaps even when static-like band invariants do not distinguish the bands[8]. We therefore focus on the quasienergy spectrum ofUFU_{F}and on the spatial structure and dynamics of states inside the0andπ\pigaps.

The perfect-hopping value of a single active bond isJ​Ts=π2,JT_{s}=\frac{\pi}{2},(8)

for which the two-site hopping unitary transfers amplitude completely across the active bond, up to a phase. We identify the topological regime near this value. The trivial regime is obtained near the no-transfer points, includingJ​Ts=0JT_{s}=0and, by the single-bond periodicity of the hopping pulse,J​Ts=πJT_{s}=\pi.

At the perfect-hopping point, which we also refer to as the perfect-point, the hopping part of the evolution reduces to a deterministic map of site amplitudes. The local motion can be read off from the four inequivalent bulk sites highlighted by purple circles in Fig.1. During one quarter of the hopping schedule, i.e., one blue–green–red–orange sequence, two of these inequivalent sites undergo two hops, while the other two undergo four hops. In all four cases, the hops circulate clockwise around bulk octagons. After the full 16-step hopping protocol, the first pair of bulk-site types completes one loop around an octagon, while the second pair completes two loops. The onsite potential step only adds sublattice-dependent phases and does not change this site map.

The boundary behaves differently. Some degree-two boundary sites still complete local loops around octagons if the octagon selected by the hopping schedule remains intact after the finite boundary truncation. However, when the octagon that would close the local loop has been removed by the boundary cut, the same perfect-point dynamics translates the amplitude along the outer boundary instead. The cyan-circled sites and black arrows in Fig.1show representative examples over one quarter of the hopping schedule. These propagating boundary sites move counterclockwise, opposite to the clockwise circulation of the bulk loops. We use this perfect-point motion to distinguish degree-two boundary sites that participate in propagating boundary motion from degree-two sites that close local loops. For the shell-by-shell construction of finite patches considered here, we estimate that approximately43%43\%of all sites participate in propagating boundary motion rather than local perfect-point loops in the thermodynamic limit. This estimate is obtained by comparing the corresponding fractions for patches containing four, five, and six shells and extrapolating their finite-size trend.

## IIIResults

## III.1Quasienergy density of states

We first compare representative open-boundary spectra in the topological and trivial regimes. Figure2shows the quasienergy density of states for a six-shell open patch containingN=10800N=10800sites. The boundary, defined by reduced graph degree, containsN∂=6240N_{\partial}=6240sites, so that approximately58%58\%of the sites lie on the open boundary. This extensive boundary fraction is a characteristic feature of finite hyperbolic patches and motivates the complementary diagnostics below.Figure 2:Quasienergy density of states of a six-shell open patch withN=10800N=10800sites.The quasienergy phaseε​T\varepsilon Tis defined byUF​|ψα⟩=e−i​εα​T​|ψα⟩U_{F}|\psi_{\alpha}\rangle=e^{-i\varepsilon_{\alpha}T}|\psi_{\alpha}\rangle. The green curve,J​Ts=1.9​π/2JT_{s}=1.9\pi/2, shows the trivial regime with gaps atε​T=0\varepsilon T=0andπ\pi. The blue curve,J​Ts=1.1​π/2JT_{s}=1.1\pi/2, shows the topological regime, where both quasienergy gaps, shaded in gray, are populated by boundary states. Both curves useδ​Ts=0.8​π/2{\delta T_{s}=0.8\pi/2}. The red star indicates the quasienergy of the in-gap state used for boundary dynamics in Fig.4.

The density of states is obtained by exact diagonalization of the finite-system Floquet operator in Eq. (6). To produce the continuous curves shown in Fig.2, each quasienergy is broadened by a Lorentzian with widthη=8×10−3\eta=8\times 10^{-3}in units ofε​T\varepsilon T. The green curve corresponds toJ​Ts=1.9​π2,JT_{s}=1.9\frac{\pi}{2},(9)

which is close to the trivial no-transfer pointJ​Ts=πJT_{s}=\pi. In this regime the spectrum forms two quasienergy bands separated by clear gaps atε​T=0\varepsilon T=0andε​T=π\varepsilon T=\pi. The gap at0is opened by the finite sublattice-staggered onsite potential in Eq. (3). For both curves in Fig.2, the onsite pulse strength isδ​Ts=0.8​π/2{\delta T_{s}=0.8\pi/2}.

The blue curve corresponds toJ​Ts=1.1​π2,JT_{s}=1.1\frac{\pi}{2},(10)

which is close to the perfect-hopping point. In this regime, the same bulk gaps are populated by in-gap states. The density of states alone does not establish the spatial character of these states. We identify them as boundary-localized through the wave-packet dynamics in Sec.III.3and through the spectral-flow diagnosis discussed in Sec.III.4.

The open-boundary density of states therefore identifies the two representative regimes used in the rest of the paper. To determine where these regimes sit relative to bulk gap closings, we next compute the0andπ\pigaps on a compact periodic{8,3}\{8,3\}lattice, where the spectrum is not contaminated by the extensive boundary of an open hyperbolic patch.

## III.2Bulk gap phase diagramFigure 3:Bulk quasienergy gap phase diagram on a20482048-site periodic{8,3}\{8,3\}lattice.The color scale shows the geometric meanΔ¯=Δ0​Δπ\bar{\Delta}=\sqrt{\Delta_{0}\Delta_{\pi}}, whereΔ0\Delta_{0}andΔπ\Delta_{\pi}are the quasienergy-phase gaps acrossε​T=0\varepsilon T=0andε​T=π\varepsilon T=\pi, respectively. Dark regions indicate that both bulk gaps are resolved in the finite periodic spectrum, while light regions indicate that at least one of the two gaps is numerically small. The blue square and circle correspond to the two open-boundary spectra shown in Fig.2: the blue square atJ​Ts=1.1​π/2JT_{s}=1.1\pi/2lies in the anomalous Floquet region, while the blue circle atJ​Ts=1.9​π/2JT_{s}=1.9\pi/2lies in the trivial region. Both marked points useδ​Ts=0.8​π/2\delta T_{s}=0.8\pi/2.

The open-boundary density of states in Fig.2distinguishes the two representative parameter points used throughout this work. However, because a finite hyperbolic patch has an extensive boundary, the open-boundary spectrum alone does not cleanly locate the bulk gap closings that separate distinct regimes. To isolate the bulk spectrum, we compute the quasienergy gaps on a compact periodic{8,3}\{8,3\}lattice, following the strategy used in hyperbolic Hofstadter calculations to avoid open-boundary contamination of the bulk spectrum[39]. The periodic lattice used here hasN=2048N=2048sites and is taken from the list of trivalent symmetric graphs of Conder and Dobcsányi[40]111Reference[40]includes methodology and graphs up to 768 vertices. Graphs with up to 10,000 vertices can be foundhere.. It realizes a closed finite quotient of the{8,3}\{8,3\}tiling on a genus-129129manifold and has no open boundary.Figure 4:Stroboscopic evolution of a boundary wave packet in the anomalous Floquet regime,J​Ts=1.1​π/2JT_{s}=1.1\pi/2.The system is a five-shell open{8,3}\{8,3\}patch withN=2888N=2888sites. This is a schematic radial plot where the sites on each shell are plotted on a circle. The initial state is obtained from the in-gap boundary state at the quasienergy marked by the red star in Fig.2by applying the angular envelope in Eq. (13). The area of purple disks are proportional to|ψi​(t)|2|\psi_{i}(t)|^{2}and are rescaled independently at each time so that the largest marker has a fixed display area; disk sizes should therefore not be compared quantitatively across panels. The panels showt=0,50​T,100​T,150​T,200​T,250​T,300​T,350​Tt=0,50T,100T,150T,200T,250T,300T,350T. The wave packet remains localized near the outer boundary and propagates counterclockwise around the sample.

For each pair of drive parameters(J​Ts,δ​Ts)(JT_{s},\delta T_{s}), we diagonalize the Floquet operator on this periodic lattice and sort the eigenphasesθα=εα​T\theta_{\alpha}=\varepsilon_{\alpha}Tin the Floquet zone(−π,π](-\pi,\pi]. We defineΔ0\Delta_{0}as the quasienergy-phase spacing acrossθ=0\theta=0, i.e., the difference between the smallest positive eigenphase and the largest negative eigenphase. Theπ\pigap is defined across the Floquet-zone edge,Δπ=2​π+θ1−θN,\Delta_{\pi}=2\pi+\theta_{1}-\theta_{N},(11)

whereθ1\theta_{1}andθN\theta_{N}are the smallest and largest sorted eigenphases. The quantity plotted in Fig.3is the geometric meanΔ¯=Δ0​Δπ.\bar{\Delta}=\sqrt{\Delta_{0}\Delta_{\pi}}.(12)

This quantity is nonzero only when both Floquet gaps are resolved in the finite periodic spectrum, and therefore identifies the parameter regions where the gap topology can be meaningfully compared.

Figure3shows extended regions in which both the0andπ\pibulk gaps are resolved, separated by regions where at least one of the two gaps becomes numerically small. The individual gap maps,Δ0\Delta_{0}andΔπ\Delta_{\pi}, are shown in AppendixA. The two parameter points used in Fig.2lie in distinct gapped regions. The point near complete transfer across an active bond,J​Ts=1.1​π/2JT_{s}=1.1\pi/2withδ​Ts=π/4\delta T_{s}=\pi/4, lies in the anomalous Floquet region. In the corresponding open-boundary system, both quasienergy gaps contain in-gap states identified as boundary states by the dynamical and spectral-flow diagnostics in Secs.III.3andIII.4. The point near two transfers during one hopping pulse,J​Ts=1.9​π/2JT_{s}=1.9\pi/2withδ​Ts=π/4\delta T_{s}=\pi/4, lies in the trivial region, where the open-boundary spectrum retains empty gaps.

Within the gapped regions resolved in this finite periodic system, we find no numerical evidence for an additional Chern-band regime. In a Floquet system with two isolated quasienergy band groups, a nonzero Chern number for one band group would be reflected in a difference between the net chiral edge content of the two quasienergy gaps. Instead, the open-boundary spectra distinguish only the two regimes discussed above: a trivial regime with no boundary states in either gap, and an anomalous Floquet regime in which boundary states appear in both gaps.

## III.3Chiral boundary dynamics

Having identified the bulk-gapped regions in Fig.3, we now return to an open finite patch and examine the real-space dynamics of a boundary wave packet in an open five-shell patch withN=2888N=2888sites. The smaller system is used for visual clarity. Because no conventional translation-invariant momentum-space description is available for the boundary of this finite hyperbolic patch, we construct the localized wave packet directly in real space[27,28]. We choose an eigenstate associated with an in-gap boundary mode and form a localized wave packet by multiplying its site amplitudes by an angular Gaussian envelope,ψi​(0)∝ϕi​exp⁡[−dθ​(θi,θ0)2σθ2],\psi_{i}(0)\propto\phi_{i}\exp\left[-\frac{d_{\theta}(\theta_{i},\theta_{0})^{2}}{\sigma_{\theta}^{2}}\right],(13)

whereϕi\phi_{i}is the chosen boundary eigenstate,θi\theta_{i}is the polar angle of siteiiin the Poincaré disk representation, anddθ​(θ,θ0)=minn∈ℤ⁡|θ−θ0+2​π​n|d_{\theta}(\theta,\theta_{0})=\min_{n\in\mathbb{Z}}|\theta-\theta_{0}+2\pi n|(14)

is the periodic angular distance betweenθ\thetaandθ0\theta_{0}on the
circle. The center angle is denoted byθ0\theta_{0}and the widthσθ\sigma_{\theta}is chosen to be0.50.5. The state is then evolved stroboscopically,|ψi​(n​T)⟩=UFn​|ψi​(0)⟩.|\psi_{i}(nT)\rangle=U_{F}^{n}|\psi_{i}(0)\rangle.(15)

Figure4shows the resulting evolution atJ​Ts=1.1​π/2JT_{s}=1.1\pi/2, using the in-gap boundary eigenstate with a quasienergy marked by the red star in Fig.2to construct the initial wave packet. Other in-gap boundary eigenstates give qualitatively similar dynamics, differing mainly in their group velocity. The area of each purple disk is proportional to the site probability density|ψi​(n​T)|2|\psi_{i}(nT)|^{2}. Over the time interval shown, the wave packet remains confined to the outer boundary region, with no visible weight propagating into the inner shells. At the same time, the packet moves counterclockwise around the sample. This chiral boundary propagation provides a real-space dynamical signature of the in-gap boundary states inferred from the density of states. The unfiltered boundary state, together with a representative bulk-band state and the corresponding bulk wave-packet dynamics, is shown in AppendixB.

## III.4Flux dispersion and puncture-boundary spectral flow in the Hofstadter butterfly

The open-boundary spectra and wave-packet dynamics above identify the anomalous Floquet regime through states on the outer boundary of a finite hyperbolic patch. We now give a complementary diagnostic that avoids the extensive outer boundary altogether. This diagnostic isolates boundary behavior in hyperbolic systems where extensive boundaries and the lack of conventional momentum-space tools complicate Euclidean-style diagnostics.

We start from a compact periodic{8,3}\{8,3\}lattice withN=2048N=2048sites, chosen from the list of trivalent symmetric graphs of Conder and Dobcsányi[40], and introduce a small internal boundary by deleting a single vertex and its three incident edges. The unpunctured graph is a periodic{8,3}\{8,3\}lattice with no open boundary, while the punctured graph has20472047sites and a controlled local boundary.Figure 5:Flux dispersion and puncture-boundary spectral flow in compact periodic{8,3}\{8,3\}lattices.(a) Local geometry of the puncture in a20482048-site periodic lattice. A single vertex and its three incident edges are removed, creating a small boundary associated with the three octagons meeting at the deleted vertex. Cyan circles mark the seven puncture-boundary sites that cycle clockwise under one quarter of the hopping schedule at the perfect-hopping point. (b) Hofstadter density of states map in the trivial regime,J​Ts=1.9​π/2JT_{s}=1.9\pi/2, withδ​Ts=0.8​π/2\delta T_{s}=0.8\pi/2. The blue background is the logarithmic density of states of the full periodic lattice, while the red overlay shows the puncture-induced excess density of states. No in-gap puncture-boundary branches are visible. (c) Corresponding map in the anomalous Floquet regime,J​Ts=1.1​π/2JT_{s}=1.1\pi/2, withδ​Ts=0.8​π/2\delta T_{s}=0.8\pi/2. The puncture produces seven boundary branches that traverse the quasienergy gaps and hybridize with the bulk bands where they overlap. The colorbars on the right apply to both (b) and (c).

The local puncture geometry is shown in Fig.5(a). The removed vertex is shared by three octagons. At the perfect-hopping point, seven sites around the puncture, marked by cyan circles, form a closed puncture-boundary cycle. During one blue–green–red–orange quarter of the hopping schedule, each of these seven sites hops to the next cyan-circled site in the clockwise direction. Other nearby degree-deficient sites execute closed clockwise loops around intact octagons at the perfect point and do not contribute to this propagating puncture-boundary cycle. Thus the puncture creates a small, well-controlled version of the same boundary physics seen on the outer edge of the finite patches. In the fixed orientation of Fig.5(a), both the seven-site puncture-boundary cycle and the local octagon loops circulate clockwise. This contrasts with the counterclockwise motion at the outer boundary of an open patch and reflects the fact that the puncture forms an internal, rather than external, boundary.

We turn this puncture construction into a Hofstadter spectral-flow diagnostic by threading a uniform magnetic flux through the compact periodic lattice. Flux-dependent gap traversal in Hofstadter spectra provides a useful probe of global topology, including for Floquet quasienergy spectra[41]. We use a uniform Hofstadter fluxϕ\phiper octagonal plaquette, implemented through Peierls phases following the construction used for hyperbolic Hofstadter butterflies in Ref.[39]. Details of the phase assignment, including our choice of vanishing AB phases along a fixed basis of noncontractible cycles, are given in AppendixC. The unpunctured20482048-site lattice has 768 octagonal faces, so the allowed uniform fluxes areϕ/ϕ0=n/768\phi/\phi_{0}=n/768, withn=0,…,768n=0,\ldots,768, whereϕ0\phi_{0}is the magnetic flux quantum. For each flux value we compute the quasienergy density of states of the full periodic lattice,ρF​(ε​T,ϕ)\rho_{F}(\varepsilon T,\phi), and of the punctured lattice,ρP​(ε​T,ϕ)\rho_{P}(\varepsilon T,\phi), using the same Peierls gauge and normalization. These densities of states are normalized per site and obtained with a Lorentzian broadening withη=8×10−3{\eta=8\times 10^{-3}}. In Figs.5(b) and5(c), the blue background showslog⁡ρF\log\rho_{F}. The red overlay shows the positive part of the difference,[log⁡ρP​(ε​T,ϕ)−log⁡ρF​(ε​T,ϕ)]+,\left[\log\rho_{P}(\varepsilon T,\phi)-\log\rho_{F}(\varepsilon T,\phi)\right]_{+},(16)

and therefore isolates spectral weight corresponding to the boundary states, if any. For completeness, the correspondinglog⁡ρF\log\rho_{F}andlog⁡ρP\log\rho_{P}maps are shown separately in AppendixD.

Figures5(b) and5(c) show the resulting Hofstadter butterflies for representative points in the trivial and topological regimes, respectively. For visual clarity, we use points withδ​Ts=0.8​π/2\delta T_{s}=0.8\pi/2andJ​Ts=1.1{JT_{s}=1.1}and1.9​π/21.9\pi/2that lie in the same gapped regions as the blue square and circle in Fig.3, rather than the exact parameter points used for the open-boundary spectra in Sec.III.1. At these nearby points, the spectral flow is more clearly resolved. In the trivial regime [Fig.5(b)] the bulk bands are nearly horizontal as the flux is varied, and the puncture does not introduce visible in-gap spectral weight. This is consistent with the open-boundary density of states in Fig.2, where the same parameter regime has empty quasienergy gaps.

In the anomalous Floquet regime [Fig.5(c)] the blue bulk bands themselves disperse with flux. This flux dispersion reflects the local clockwise loops of the bulk states near the perfect-hopping point: as shown by the purple-circled bulk vertices in Fig.1, two of the four inequivalent vertex types undergo two hops during each quarter of the hopping schedule and therefore complete one clockwise loop of an octagon over the full hopping schedule. The other two vertex types undergo four hops per quarter and complete two clockwise loops. Accordingly, the blue spectrum contains two families of flux-dispersing bulk bands, associated with states that complete either one or two octagon loops per period. Since the latter enclose twice as much flux during their evolution, their quasienergy slopes are approximately twice those of the one-loop bands. At the perfect-hopping point, these slopes ared​(ε​T)/d​(ϕ/ϕ0)=2​πd(\varepsilon T)/d(\phi/\phi_{0})=2\piand4​π4\pi, respectively; away from that point, the same two characteristic slopes remain visible except near band crossings.

The red features in Fig.5(c) are qualitatively different. They are induced by the puncture and form seven boundary branches at a generic vertical cut through the Hofstadter map, except where they hybridize with the bulk bands. These branches traverse both the0andπ\piquasienergy gaps, providing a spectral-flow diagnostic of the puncture-boundary states. Their number and slope can be understood directly from the perfect-point motion in Fig.5(a). Label the seven puncture-boundary sites byj=0,…,6j=0,\ldots,6. At the perfect-hopping point, one full Floquet period advances a state by four sites along this seven-site cycle, up to site-dependent phases:U∂​(ϕ)​|j⟩=e−i​αj​(ϕ)​|j+4​mod​7⟩.U_{\partial}(\phi)|j\rangle=e^{-i\alpha_{j}(\phi)}|j+4\;\mathrm{mod}\;7\rangle.(17)

The phasesαj\alpha_{j}need not be uniform; they include local hopping phases and the sublattice-staggered onsite step. After seven periods and28=7×428=7\times 4advances along the cycle, however, the state has visited all seven sites and returned to its starting point. The site-dependent, flux-independent part of the accumulated phase is therefore a single constant, which we denote byγ0\gamma_{0}. During the same seven periods, the state winds four times around the puncture. Since the puncture encloses three octagons, the flux-dependent phase corresponds to12​ϕ12\phi. ThusU∂​(ϕ)7=exp⁡[−i​(γ0+2​π​12​ϕϕ0)]​I∂,U_{\partial}(\phi)^{7}=\exp\left[-i\left(\gamma_{0}+2\pi\,12\,\frac{\phi}{\phi_{0}}\right)\right]I_{\partial},(18)

with the sign fixed by the clockwise orientation in Fig.5(a). HereI∂I_{\partial}denotes the identity operator on the seven-site puncture-boundary subspace. The seven puncture-boundary quasienergy branches satisfyεm​T=γ07+2​π​127​ϕϕ0+2​π​m7(mod2​π),m=0,…,6.\varepsilon_{m}T=\frac{\gamma_{0}}{7}+2\pi\frac{12}{7}\frac{\phi}{\phi_{0}}+\frac{2\pi m}{7}\pmod{2\pi},\quad m=0,\ldots,6.(19)

Consequently, away from hybridization with the bulk bands, the boundary branches are separated by2​π/72\pi/7and have sloped​(ε​T)d​(ϕ/ϕ0)=2​π​127.\frac{d(\varepsilon T)}{d(\phi/\phi_{0})}=2\pi\frac{12}{7}.(20)

The onsite step shifts the common intercept throughγ0\gamma_{0}, but does not change the spacing or the flux slope.

This puncture diagnostic connects the local perfect-point picture to the Floquet topology. In the trivial regime, creating a small boundary does not add in-gap spectral flow. In the anomalous Floquet regime, the puncture produces chiral branches in both the0andπ\pigaps. The appearance of boundary states in both gaps with the same chirality is consistent with a Rudner-type anomalous phase rather than a Chern-band phase: in a two-band-group Floquet system, unequal net chiral content in the two gaps would indicate a nonzero Chern number for the intervening band group. Within the finite periodic systems studied here, we find no numerical evidence for such a separate Chern-band regime. Additional Hofstadter maps at representative points across the phase diagram are shown in AppendixE. These maps do not reveal a robust region with unequal gap flow characteristic of a Chern-insulating phase; in the small apparent gapped regions away from the two main regimes, one of the two quasienergy gaps remains too small to support an unambiguous identification of a separate phase.

## IVDiscussion and outlook

We have constructed a Rudner-type anomalous Floquet phase on the hyperbolic{8,3}\{8,3\}lattice. The model is based on a periodic four-coloring of the edges and a 17-step drive consisting of 16 hopping steps followed by a sublattice-staggered onsite pulse. Near the perfect-hopping point, where a single active bond transfers amplitude completely during one hopping step, the bulk dynamics reduces to local loops around octagons, while interrupted loops at a boundary become chiral boundary motion in the opposite direction. Near the perfect-hopping point, the same phase is visible through three complementary diagnostics: in-gap states in the open-boundary density of states, chiral wave-packet propagation along the outer boundary, and puncture-boundary spectral flow in a Hofstadter calculation.

The hyperbolic setting changes the role of boundaries in an essential way. In Euclidean systems, the boundary contribution becomes negligible compared with the bulk in the thermodynamic limit. Finite hyperbolic patches do not have this property: the number of boundary sites remains a finite fraction of the total system size. This makes boundary physics unusually prominent, which is advantageous for realizing and observing topological boundary modes. At the same time, it complicates the usual separation between bulk and boundary spectra. The compact periodic lattices used in the phase diagram and spectral-flow calculations address this problem by removing the outer boundary altogether. Puncturing such a lattice then introduces a small, controlled internal boundary, allowing the same chiral edge physics to be detected without relying on a finite flake whose boundary contains a large fraction of all sites.

The observed signatures are consistent with an anomalous Floquet phase rather than a Chern-band phase. In the topological regime, boundary states appear in both the0andπ\piquasienergy gaps with the same chirality. In a two-band-group Floquet problem, the difference between the net chiral contents of the two gaps determines the Chern number of the intervening bulk band group. The equal gap content observed here is therefore consistent with vanishing Floquet-band Chern numbers and topology carried by the full time evolution, as in the Rudner model[8]. Within the finite periodic systems and parameter ranges studied here, we find no numerical evidence for a separate regime with unequal gap flow characteristic of Chern bands. We do not assign a numerical winding invariant in this work; instead, the anomalous character is diagnosed through the combined boundary, bulk-gap, and puncture-flow signatures.

The present work focuses on a clean Hamiltonian construction and on a set of numerical diagnostics that are directly tied to the perfect-hopping picture. This scope keeps the connection between local Floquet loops, interrupted boundary motion, and puncture-boundary spectral flow transparent. It also points to several natural extensions. The bulk phase diagram obtained from finite periodic lattices should be viewed as a practical finite-size bulk diagnostic: regions where the gap measure becomes small identify the parameter ranges in which the0orπ\pigap closes within the numerical resolution of the quotient. Comparing different periodic lattices, especially those designed to converge in the sense of hyperbolic periodic boundary conditions constructions or supercell sequences[29,30], or using continued-fraction methods to compute bulk densities of states directly in large hyperbolic systems[42], would sharpen this picture. Similarly, disorder, imperfect edge coloring, boundary roughness, and pulse-shape errors can be incorporated into the same open-boundary and puncture-based diagnostics; disorder is particularly interesting because it may also provide a route to disorder-induced Floquet topological phases and anomalous Floquet-Anderson regimes[43,9]. Because boundary sites form a finite fraction of a hyperbolic patch, such perturbations are not merely edge corrections but part of the central physics of hyperbolic Floquet topological systems.

A complementary theoretical direction is to formulate real-space invariants for Floquet phases on hyperbolic lattices. Real-space Chern markers and Bott indices have already proved useful for static topological phases without ordinary translational symmetry[44,45,46]. Other many-body real-space approaches may also be relevant, including polarization-operator formulas in the spirit of Resta[47]and swap-operator formulas that extract Chern numbers from a single many-body wave function without introducing a family of twisted boundary conditions[48]. The latter feature is especially appealing for hyperbolic lattices, where ordinary momentum-space and twist-angle constructions are less natural. These tools could provide direct diagnostics of Chern-type content in Floquet bands or eigenstates. The anomalous Floquet phase studied here, however, requires an invariant sensitive to the full periodized time evolution, not only to individual Floquet bands. Translation-independent bulk-edge indices and recent local or response-based formulations for Floquet systems provide promising starting points[49,50,51]. Extending these approaches to hyperbolic lattices would provide a bulk diagnostic independent of open-boundary spectra and help clarify Floquet bulk-boundary correspondence in geometries with extensive boundaries.

The coloring construction itself also suggests a broader class of Floquet models on hyperbolic lattices. The essential ingredient is not specific to the{8,3}\{8,3\}tiling, but to the existence of a compatible face coloring. For a trivalent lattice whose faces admit a proper three-coloring, one can convert the face coloring into a three-coloring of edges by assigning each edge the color not used by the two faces adjacent to it. Two of these edge colors can then be kept as independent hopping steps, while the third edge color can be split into two alternating colors. This produces the same four-color structure used here: two color classes form perfect matchings, and the remaining two together form a third matching. The resulting blue–green–red–orange protocol therefore gives a direct route to Rudner-type Floquet models on other face-three-colorable hyperbolic tilings. Exploring how the anomalous phase depends on the choice of tiling would clarify which features are universal and which are specific to the{8,3}\{8,3\}construction studied here.

## Acknowledgements.We thank Yang-Zhi Chou, Huy Nguyen, Alexandra Behne, Kishor Bharti, Sheryl Mathew, and Michael Gullans for useful discussions. H.D. acknowledges support from NSF Grant No. OMA-2120757 and the Simons Foundation. A.F. and A.V.G. were supported in part by the NSF QLCI (award No. OMA-2120757), DoE ASCR Quantum Testbed Pathfinder program (award No. DE-SC0024220), NSF STAQ program, AFOSR MURI, ONR MURI, ARL (W911NF-24-2-0107), and NQVL:QSTD:Pilot:FTL. A.F. and A.V.G. also acknowledge support from the U.S. Department of Energy, Office of Science, National Quantum Information Science Research Centers, Quantum Systems Accelerator (award No. DE-SCL0000121) and from the U.S. Department of Energy, Office of Science, Accelerated Research in Quantum Computing, Fundamental Algorithmic Research toward Quantum Utility (FAR-Qu).
A.K. was supported in part by the NSF (QLCI award No. OMA-2120757 and award No. PHY2047732), AFOSR (award No. FA9550-21-1-0129).

## References
- Goldman and Dalibard [2014]N. Goldman and J. Dalibard, Periodically Driven
Quantum Systems: Effective Hamiltonians and Engineered Gauge
Fields,Physical Review X4, 031027 (2014).
- Bukovet al.[2015]M. Bukov, L. D’Alessio, and A. Polkovnikov, Universal high-frequency behavior of
periodically driven systems: From dynamical stabilization to Floquet
engineering,Advances in Physics64, 139 (2015).
- Eckardt [2017]A. Eckardt, Colloquium: Atomic
quantum gases in periodically driven optical lattices,Reviews of Modern Physics89, 011004 (2017).
- Rudner and Lindner [2020]M. S. Rudner and N. H. Lindner, Band structure
engineering and non-equilibrium dynamics in Floquet topological
insulators,Nature Reviews Physics2, 229 (2020).
- Oka and Aoki [2009]T. Oka and H. Aoki, Photovoltaic Hall effect in
graphene,Physical Review B79, 081406 (2009).
- Lindneret al.[2011]N. H. Lindner, G. Refael, and V. Galitski, Floquet topological insulator in
semiconductor quantum wells,Nature Physics7, 490 (2011).
- Kitagawaet al.[2010]T. Kitagawa, E. Berg,
M. Rudner, and E. Demler, Topological characterization of periodically driven
quantum systems,Physical Review B82, 235114 (2010).
- Rudneret al.[2013]M. S. Rudner, N. H. Lindner,
E. Berg, and M. Levin, Anomalous Edge States and the Bulk-Edge
Correspondence for Periodically Driven Two-Dimensional Systems,Physical Review X3, 031005 (2013).
- Titumet al.[2016]P. Titum, E. Berg,
M. S. Rudner, G. Refael, and N. H. Lindner, Anomalous Floquet-Anderson Insulator as a
Nonadiabatic Quantized Charge Pump,Physical Review X6, 021013 (2016).
- Nathan and Rudner [2015]F. Nathan and M. S. Rudner, Topological singularities
and the general classification of Floquet–Bloch systems,New Journal of Physics17, 125014 (2015).
- Roy and Harper [2017]R. Roy and F. Harper, Periodic table for Floquet
topological insulators,Physical Review B96, 155118 (2017).
- Rechtsmanet al.[2013]M. C. Rechtsman, J. M. Zeuner, Y. Plotnik,
Y. Lumer, D. Podolsky, F. Dreisow, S. Nolte, M. Segev, and A. Szameit, Photonic Floquet topological insulators,Nature496, 196 (2013).
- Maczewskyet al.[2017]L. J. Maczewsky, J. M. Zeuner, S. Nolte, and A. Szameit, Observation of photonic anomalous Floquet
topological insulators,Nature Communications8, 13756 (2017).
- Mukherjeeet al.[2017]S. Mukherjee, A. Spracklen, M. Valiente,
E. Andersson, P. Öhberg, N. Goldman, and R. R. Thomson, Experimental observation of anomalous topological edge
modes in a slowly driven photonic lattice,Nature Communications8, 13918 (2017).
- Penget al.[2016]Y.-G. Peng, C.-Z. Qin,
D.-G. Zhao, Y.-X. Shen, X.-Y. Xu, M. Bao, H. Jia, and X.-F. Zhu, Experimental demonstration of
anomalous Floquet topological insulator for sound,Nature Communications7, 13368 (2016).
- Winterspergeret al.[2020]K. Wintersperger, C. Braun, F. N. Ünal,
A. Eckardt, M. D. Liberto, N. Goldman, I. Bloch, and M. Aidelsburger, Realization of an anomalous Floquet topological system with ultracold
atoms,Nature Physics16, 1058 (2020).
- Afzalet al.[2020]S. Afzal, T. J. Zimmerling, Y. Ren,
D. Perron, and V. Van, Realization of Anomalous Floquet Insulators in
Strongly Coupled Nanophotonic Lattices,Physical Review Letters124, 253601 (2020).
- A. Blatovet al.[2010]V. A. Blatov, M. O’Keeffe, and D. M. Proserpio, Vertex-, face-,
point-, Schläfli-, and Delaney-symbols in nets, polyhedra and
tilings: Recommended terminology,CrystEngComm12, 44 (2010).
- Kolláret al.[2019]A. J. Kollár, M. Fitzpatrick, and A. A. Houck, Hyperbolic lattices in
circuit quantum electrodynamics,Nature571, 45 (2019).
- Lenggenhageret al.[2022]P. M. Lenggenhager, A. Stegmaier, L. K. Upreti, T. Hofmann,
T. Helbig, A. Vollhardt, M. Greiter, C. H. Lee, S. Imhof, H. Brand, T. Kießling, I. Boettcher, T. Neupert, R. Thomale, and T. Bzdušek, Simulating hyperbolic space on a circuit board,Nature Communications13, 4373 (2022).
- Chenet al.[2023]A. Chen, H. Brand,
T. Helbig, T. Hofmann, S. Imhof, A. Fritzsche, T. Kießling, A. Stegmaier, L. K. Upreti, T. Neupert, T. Bzdušek, M. Greiter,
R. Thomale, and I. Boettcher, Hyperbolic matter in electrical circuits with tunable
complex phases,Nature Communications14, 622 (2023).
- Zhanget al.[2022]W. Zhang, H. Yuan,
N. Sun, H. Sun, and X. Zhang, Observation of novel topological states in hyperbolic lattices,Nature Communications13, 2937 (2022).
- Huanget al.[2024]L. Huang, L. He, W. Zhang, H. Zhang, D. Liu, X. Feng, F. Liu, K. Cui, Y. Huang, W. Zhang, and X. Zhang, Hyperbolic photonic topological insulators,Nature Communications15, 1647 (2024).
- Parket al.[2024]H. Park, X. Piao, and S. Yu, Scalable and Programmable Emulation of
Photonic Hyperbolic Lattices,ACS Photonics11, 3890 (2024).
- Maciejko and Rayan [2021]J. Maciejko and S. Rayan, Hyperbolic band theory,Science Advances7(2021),arXiv:2008.05489.
- Maciejko and Rayan [2022]J. Maciejko and S. Rayan, Automorphic Bloch
theorems for hyperbolic lattices,Proceedings of the National
Academy of Sciences119, e2116869119 (2022),arXiv:2108.09314.
- Boettcheret al.[2022]I. Boettcher, A. V. Gorshkov, A. J. Kollár, J. Maciejko, S. Rayan, and R. Thomale, Crystallography of hyperbolic
lattices,Physical Review B105, 125118 (2022).
- Chenget al.[2022]N. Cheng, F. Serafin,
J. McInerney, Z. Rocklin, K. Sun, and X. Mao, Band Theory and Boundary Modes of High-Dimensional
Representations of Infinite Hyperbolic Lattices,Physical Review Letters129, 088002 (2022).
- Lux and Prodan [2023]F. R. Lux and E. Prodan, Converging Periodic Boundary
Conditions and Detection of Topological Gaps on Regular
Hyperbolic Tessellations,Physical Review Letters131, 176603 (2023).
- Lenggenhageret al.[2023]P. M. Lenggenhager, J. Maciejko, and T. Bzdušek, Non-Abelian
Hyperbolic Band Theory from Supercells,Physical Review Letters131, 226401 (2023).
- Yuet al.[2020]S. Yu, X. Piao, and N. Park, Topological Hyperbolic Lattices,Physical Review Letters125, 053901 (2020).
- Liuet al.[2022]Z.-R. Liu, C.-B. Hua,
T. Peng, and B. Zhou, Chern insulator in a hyperbolic lattice,Physical Review B105, 245301 (2022).
- Urwyleret al.[2022]D. M. Urwyler, P. M. Lenggenhager, I. Boettcher, R. Thomale, and T. Neupert, Hyperbolic Topological Band
Insulators, PHYSICAL REVIEW LETTERS (2022).
- Liuet al.[2023]Z.-R. Liu, C.-B. Hua,
T. Peng, R. Chen, and B. Zhou, Higher-order topological insulators in hyperbolic lattices,Physical Review B107, 125302 (2023).
- Tao and Xu [2023]Y.-L. Tao and Y. Xu, Higher-order topological hyperbolic
lattices,Physical Review B107, 184201 (2023).
- Zhanget al.[2023]W. Zhang, F. Di, X. Zheng, H. Sun, and X. Zhang, Hyperbolic band topology with non-trivial second Chern
numbers,Nature Communications14, 1083 (2023).
- Sunet al.[2024]C. Sun, A. Chen, T. Bzdušek, and J. Maciejko, Topological linear response of hyperbolic Chern
insulators,SciPost Physics17, 124 (2024).
- Chenet al.[2024]Q. Chen, Z. Zhang,
H. Qin, A. Bossart, Y. Yang, H. Chen, and R. Fleury, Anomalous and Chern topological
waves in hyperbolic networks,Nature Communications15, 2293 (2024).
- Stegmaieret al.[2022]A. Stegmaier, L. K. Upreti, R. Thomale, and I. Boettcher, Universality of Hofstadter
Butterflies on Hyperbolic Lattices,Physical Review Letters128, 166402 (2022).
- Conder and Dobcsányi [2002]M. Conder and P. Dobcsányi, Trivalent symmetric
graphs on up to 768 vertices,Journal of Combinatorial
Mathematics and Combinatorial Computing40, 41 (2002).
- Asbóth and Alberti [2017]J. K. Asbóth and A. Alberti, Spectral Flow and
Global Topology of the Hofstadter Butterfly,Physical Review Letters118, 216801 (2017).
- Mosseri and Vidal [2023]R. Mosseri and J. Vidal, Density of states of
tight-binding models in the hyperbolic plane,Physical Review B108, 035154 (2023).
- Titumet al.[2015]P. Titum, N. H. Lindner,
M. C. Rechtsman, and G. Refael, Disorder-induced Floquet Topological
Insulators,Physical Review Letters114, 056801 (2015),arXiv:1403.0592 [cond-mat].
- Bianco and Resta [2011]R. Bianco and R. Resta, Mapping topological order in
coordinate space,Physical Review B84, 241106 (2011).
- Hastings and Loring [2011]M. B. Hastings and T. A. Loring, Topological insulators andC∗\ast-algebras: Theory and numerical practice,Annals of Physics July 2011 Special Issue,326, 1699 (2011).
- Loring and Hastings [2011]T. A. Loring and M. B. Hastings, Disordered topological
insulators via C*-algebras,Europhysics Letters92, 67004 (2011).
- Resta [1998]R. Resta, Quantum-Mechanical
Position Operator in Extended Systems,Physical Review Letters80, 1800 (1998).
- Dehghaniet al.[2021]H. Dehghani, Z.-P. Cian,
M. Hafezi, and M. Barkeshli, Extraction of the many-body Chern number from a single
wave function,Physical Review B103, 075102 (2021).
- Graf and Tauber [2018]G. M. Graf and C. Tauber, Bulk–Edge Correspondence for
Two-Dimensional Floquet Topological Insulators,Annales Henri Poincaré19, 709 (2018).
- Ghoshet al.[2024]A. K. Ghosh, R. Arouca, and A. M. Black-Schaffer, Local and energy-resolved topological
invariants for Floquet systems,Physical Review B110, 245306 (2024).
- Peralta Gavenskyet al.[2025]L. Peralta Gavensky, G. Usaj, and N. Goldman, Středa Formula for
Floquet Systems: Topological Invariants and Quantized Anomalies
from Cesàro Summation,Physical Review X15, 031067 (2025).

## Appendix AIndividual quasienergy gaps

In the main text, the bulk phase diagram is shown using the geometric meanΔ¯=Δ0​Δπ\bar{\Delta}=\sqrt{\Delta_{0}\Delta_{\pi}}of the quasienergy gaps atε​T=0\varepsilon T=0andε​T=π\varepsilon T=\pi. This quantity is useful because it is nonzero only when both gaps are resolved in the finite periodic spectrum. For completeness, Fig.A1shows the two gap measures separately, using the same 2048-site periodic{8,3}\{8,3\}lattice and the same parameter range as Fig.3. Small values of eitherΔ0\Delta_{0}orΔπ\Delta_{\pi}produce the low-gap regions in the geometric-mean phase diagram.Figure A1:Individual bulk quasienergy gaps on the20482048-site periodic{8,3}\{8,3\}lattice.(a)Δ0\Delta_{0}and (b)Δπ\Delta_{\pi}. Both gaps are shown in quasienergy-phase units over the same parameter range as Fig.3.

The gap maps in Fig.A1, as well as the geometric-mean phase diagram in Fig.3, were obtained by diagonalizing the Floquet operator on a uniform401×401401\times 401grid in the(J​Ts,δ​Ts)(JT_{s},\delta T_{s})parameter plane.

## Appendix BBoundary- and bulk-state wave-packet dynamicsFigure A2:Floquet eigenstates used to construct the boundary and bulk wave packets.Both states are shown on the five-shell open-boundary{8,3}\{8,3\}patch withN=2888N=2888sites atJ​Ts=1.1​π/2JT_{s}=1.1\pi/2andδ​T1​h=π/4\delta T_{1h}=\pi/4. The sites belonging to each shell are plotted on a circle, as in Fig.4, and the area of each purple disk is proportional to the eigenstate probability|ϕi|2|\phi_{i}|^{2}. (a) The in-gap boundary state whose quasienergy is marked in Fig.2. (b) A representative state from a bulk quasienergy band atε​T=1.3\varepsilon T=1.3. The states are shown before application of the angular Gaussian envelope in Eq. (13). The disk areas are rescaled independently in each panel so that the largest disk has the same fixed display area. The disk sizes therefore show the relative spatial distribution within each state, but do not provide a direct comparison of absolute site probabilities between the two states.

In Sec.III.3, the initial boundary wave packet is constructed by applying the angular Gaussian envelope in Eq. (13) to a Floquet eigenstate. Here we show the unfiltered eigenstate used in that construction and compare it with a representative state selected from a bulk quasienergy band. We also show the stroboscopic evolution of the wave packet constructed from the bulk-band state.

FigureA2shows the two normalized Floquet eigenstates before the angular envelope is applied. Both states are obtained from the same five-shell open-boundary{8,3}\{8,3\}patch withN=2888N=2888sites and at the same anomalous-regime parameter point used for the boundary dynamics in the main text,J​Ts=1.1​π/2JT_{s}=1.1\pi/2andδ​T1​h=π/4\delta T_{1h}=\pi/4. The boundary state in Fig.A2(a) is the in-gap state whose quasienergy is marked in the density of states in Fig.2. Its probability density is concentrated in the outer boundary region. The state in Fig.A2(b) is selected from a bulk quasienergy band atε​T=1.3\varepsilon T=1.3and has appreciable weight over several shells. Here, “bulk state” refers to the spectral location of the state within a bulk band and does not imply localization near the geometric center of the finite hyperbolic patch.

For each seed eigenstate, we construct an initial wave packet using the same angular envelope as in Eq. (13) and normalize the resulting state. The labels “boundary” and “bulk” refer to the corresponding seed eigenstates; after multiplication by the spatial envelope, the resulting wave packets are no longer Floquet eigenstates. Because the envelope depends only on the angular coordinate, it localizes the state azimuthally while retaining the shell-resolved probability profile inherited from the seed eigenstate. The bulk wave packet therefore has a broad radial profile already att=0t=0.Figure A3:Stroboscopic evolution of a wave packet constructed from a bulk-band state in the anomalous Floquet regime.The seed Floquet eigenstate is the state atε​T=1.3\varepsilon T=1.3shown in Fig.A2(b). The system and drive parameters are the same as in Fig.4: a five-shell open-boundary{8,3}\{8,3\}patch withN=2888N=2888sites,J​Ts=1.1​π/2JT_{s}=1.1\pi/2, andδ​T1​h=π/4\delta T_{1h}=\pi/4. The initial state is obtained by applying the angular Gaussian envelope in Eq. (13) and then normalizing the result. The area of purple disks are proportional to|ψi​(t)|2|\psi_{i}(t)|^{2}and are rescaled independently at each time so that the largest marker has a fixed display area; disk sizes should therefore not be compared quantitatively across panels. The panels showt=0,50​T,100​T,150​T,200​T,250​T,300​T,t=0,50T,100T,150T,200T,250T,300T,and350​T350T. The packet develops probability over multiple shells and does not exhibit the persistent chiral boundary propagation seen in Fig.4.

FigureA3shows the subsequent stroboscopic evolution of the bulk wave packet. In contrast to the boundary wave packet in Fig.4, the bulk packet does not remain confined to the outer boundary region or translate around the sample as a compact packet with a definite chirality. Instead, it loses its initial angular localization and develops substantial probability around multiple shells. This comparison shows that the persistent counterclockwise propagation in Fig.4is a property of the in-gap boundary-state sector rather than a generic consequence of the angular localization procedure.

## Appendix CPeierls phases in the Hofstadter calculations

We implement a uniform magnetic flux on the compact periodic{8,3}\{8,3\}lattices using the Peierls substitution, following the construction of Ref.[39]. For an oriented edge(i,j)(i,j), we introduce a hopping phaseφi​j=−φj​i\varphi_{ij}=-\varphi_{ji}and replace the hopping Hamiltonian in each color sector byHμ​(ϕ)=−J​∑⟨i​j⟩∈Eμ(ei​φi​j​ci†​cj+e−i​φi​j​cj†​ci),μ=b,g,r,o.H_{\mu}(\phi)=-J\sum_{\langle ij\rangle\in E_{\mu}}\left(e^{i\varphi_{ij}}c_{i}^{\dagger}c_{j}+e^{-i\varphi_{ij}}c_{j}^{\dagger}c_{i}\right),\qquad\mu=b,g,r,o.(A1)

The same hopping phase is used each time a given edge is activated during the Floquet drive, while the sublattice-staggered onsite step remains unchanged.

The hopping phases are chosen such that the oriented phase accumulated around every octagonffis∑⟨i​j⟩∈∂fφi​j=2​π​ϕϕ0(mod2​π),\sum_{\langle ij\rangle\in\partial f}\varphi_{ij}=2\pi\frac{\phi}{\phi_{0}}\pmod{2\pi},(A2)

where the sum follows the edges clockwise around the octagon,ϕ\phiis the magnetic flux through each octagon, andϕ0\phi_{0}is the magnetic flux quantum. On a closed regular map, onlyF−1F-1of theFFoctagon constraints are independent, and consistency requiresF​ϕϕ0∈ℤ.F\frac{\phi}{\phi_{0}}\in\mathbb{Z}.(A3)

The20482048-site periodic lattice used in the Hofstadter calculations containsF=768F=768octagons. The inequivalent uniform flux values are thereforeϕϕ0=n768,n=0,…,767.\frac{\phi}{\phi_{0}}=\frac{n}{768},\qquad n=0,\ldots,767.(A4)

We additionally includen=768n=768in the plots to display the endpointϕ/ϕ0=1\phi/\phi_{0}=1, which is equivalent to zero flux.

The octagon constraints do not completely determine the hopping phases on a compact surface. In addition to theF−1F-1independent octagon cycles, a genus-ggregular map has2​g2gindependent noncontractible Aharonov–Bohm (AB) cycles. Together, these cycles form a basis of the cycle space. We choose representative noncontractible cycles𝒞a\mathcal{C}_{a}and specify their AB phases through∑⟨i​j⟩∈𝒞aφi​j=ka(mod2​π),a=1,…,2​g.\sum_{\langle ij\rangle\in\mathcal{C}_{a}}\varphi_{ij}=k_{a}\pmod{2\pi},\qquad a=1,\ldots,2g.(A5)

A local gauge can then be fixed, for example, by setting the hopping phases on the edges of a spanning tree.

For the calculations presented here, we use a single AB-flux configuration and setka=0,a=1,…,2​g,k_{a}=0,\qquad a=1,\ldots,2g,(A6)

for the chosen representatives of the noncontractible cycles. Once the octagon fluxes and AB holonomies are fixed, a local gauge transformation may redistribute the hopping phases among individual edges but does not change the quasienergy spectrum or any gauge-invariant observable. The Floquet eigenstates in different gauges are related by site-dependent phase rotations. At nonzero octagon flux, a deformation of a noncontractible-cycle representative by adding octagon boundaries also adds the flux enclosed by those octagons. Consequently, changing the cycle representatives requires a corresponding redefinition of the AB phases in order to preserve the same physical holonomies. Our choiceka=0k_{a}=0should therefore be understood relative to the fixed cycle basis used in the numerical calculation.

Unlike Ref.[39], where multiple AB-flux configurations are sampled to obtain a denser approximation to the infinite-lattice spectrum, we retain this single zero-AB-phase configuration throughout. The same hopping-phase assignment is used for the full and punctured periodic lattices.

For the punctured calculation, the Peierls phases are first assigned on the full regular map. We then remove one vertex and its three incident edges, leaving the phases on all remaining edges unchanged. No additional AB flux is inserted through the puncture. The puncture-boundary cycle encloses the three octagons adjacent to the removed vertex, so its accumulated magnetic phase isφpuncture=2​π​3​ϕϕ0(mod2​π).\varphi_{\mathrm{puncture}}=2\pi\frac{3\phi}{\phi_{0}}\pmod{2\pi}.(A7)

This gives the factor of three in the puncture-boundary spectral-flow slope discussed in Sec.III.4.

## Appendix DSeparate full and punctured Hofstadter density of states maps

In the main text, the Hofstadter maps are shown as overlays in Fig.5: the full periodic-lattice density of states is plotted in blue, while the puncture-induced excess density of states is plotted in red. For completeness, Figs.A4andA5show the full and punctured density of states maps separately. The parameters are the same as in Fig.5. Comparing the two panels in each figure shows directly which spectral features are already present in the full periodic lattice and which ones are introduced by the puncture. While the bulk density of states is essentially unchanged by the puncture in both regimes, only the anomalous Floquet regime develops puncture-induced boundary states that traverse the bulk quasienergy gaps.Figure A4:Separate Hofstadter density of states maps in the trivial regime,J​Ts=1.9​π/2JT_{s}=1.9\pi/2andδ​Ts=0.8​π/2\delta T_{s}=0.8\pi/2.(a) Full 2048-site periodic lattice. (b) Punctured periodic lattice obtained by removing one vertex and its three incident edges.Figure A5:Separate Hofstadter density of states maps in the anomalous Floquet regime,J​Ts=1.1​π/2JT_{s}=1.1\pi/2andδ​Ts=0.8​π/2\delta T_{s}=0.8\pi/2.(a) Full 2048-site periodic lattice. (b) Punctured periodic lattice obtained by removing one vertex and its three incident edges.

## Appendix EAdditional Hofstadter maps across the phase diagram

In the main text, the Hofstadter density of states maps are shown for two representative points: the anomalous Floquet regime and the trivial regime. For completeness, Fig.A6shows additional Hofstadter maps at several points in the bulk gap phase diagram. The central panel is a zoomed-in version of the geometric-mean gap diagramΔ¯=Δ0​Δπ\bar{\Delta}=\sqrt{\Delta_{0}\Delta_{\pi}}shown in Fig.3, with markers indicating the parameters used for the surrounding density of states maps. The central panel covers the regionJ​Ts∈[π/2,π]JT_{s}\in[\pi/2,\pi]andδ​Ts∈[0,π/2]\delta T_{s}\in[0,\pi/2]. The remainder of the phase diagram in Fig.3is obtained by mirror-symmetric extension of the displayed region.

PanelsA6(d) andA6(e) correspond to the two representative points discussed in the main text, withJ​Ts=1.1​π/2JT_{s}=1.1\pi/2andJ​Ts=1.9​π/2JT_{s}=1.9\pi/2, respectively, at fixedδ​Ts=0.8​π/2\delta T_{s}=0.8\pi/2. PanelsA6(a)–(c) show intermediate values,J​Ts=1.3​π/2JT_{s}=1.3\pi/2,1.5​π/21.5\pi/2, and1.7​π/21.7\pi/2, at the same value ofδ​Ts\delta T_{s}, illustrating how the Hofstadter spectrum evolves between the anomalous and trivial regimes.

PanelsA6(f)–(h) show three additional points where the finite-size gap diagnostic indicates an apparent isolated region of nonzeroΔ¯\bar{\Delta}. These points are(J​Ts,δ​Ts)=(1.06​π/2,0.10​π/2)(JT_{s},\delta T_{s})=(1.06\pi/2,0.10\pi/2),(1.21​π/2,0.52​π/2)(1.21\pi/2,0.52\pi/2), and(1.46​π/2,0.39​π/2)(1.46\pi/2,0.39\pi/2), respectively. In these cases, one of the two quasienergy gaps is too small to support a clear identification of a separate phase, while the other gap shows puncture-induced boundary states. We therefore do not assign these regions to distinct Chern-insulating phases.Figure A6:Additional Hofstadter density of states maps across the phase diagram.The central panel shows a zoomed-in geometric-mean gap diagram,Δ¯=Δ0​Δπ\bar{\Delta}=\sqrt{\Delta_{0}\Delta_{\pi}}, with markers indicating the parameters of panels (a)–(h). The surrounding panels show Hofstadter maps with the same full-lattice density of states and puncture-induced excess-density convention used in the main text. The blue background is the logarithmic density of states of the full periodic lattice, while the red overlay shows the puncture-induced excess density of states. The colorbars on the right apply to all Hofstadter maps.

## 


- 


Major funding support from
