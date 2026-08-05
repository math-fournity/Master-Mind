# Sixteen-State Energy Mapping for First-Principles Four-Spin Ring Exchange: Validation on $La_2CuO_4$ and $SrFeO_2$

**arXiv ID**: 2607.18986v2
**Authors**: Xavier Rocquefelte, Peter Blaha
**Published**: 2026-07-21
**Categories**: cond-mat.mtrl-sci, cond-mat.str-el, quant-ph
**Comments**: 37 pages, 4 figures, 6 Tables
**HTML URL**: https://arxiv.org/html/2607.18986v2

## Abstract

Four-spin ring (cyclic) exchange $J_{ring}$ is an essential ingredient of the Heisenberg spin Hamiltonian of cuprates and other square-lattice magnets, yet it has lacked the kind of direct, local first-principles extraction that the four-state method provides for bilinear exchange, $J$. We supply it by generalizing that method to a sixteen-state ($2^4$) scheme. Symmetry reduces the sixteen configurations to six or eight inequivalent energies, so the cost is modest. The derivation also shows that the conventional four-state magnetic coupling, $J$, is itself ring-renormalized, by $\pm 2 J_{ring} S^2$ with the sign set by the reference state. T-La$_2$CuO$_4$ confirms this quantitatively: three independent routes agree on $J_{ring}$ to $0.2\%$, giving $J_{ring}/J_1 = 0.25$, and a four-state $J_1$ quoted without naming its reference is wrong by $12\%$ in this material. The direct sixteen-state extraction itself proves reference-dependent, the Néel and ferromagnetic baths bracketing the mapping value: a fourth-order fingerprint of interactions beyond the pair-plus-ring model, which additional reference baths resolve into a bare $J_{ring}$ and a converging tower of six- and eight-spin loop couplings. SrFeO$_2$ ($S = 2$), with the same plaquette yet $J_{ring}/J = 0.006$, provides the negative control: a plaquette is necessary for ring exchange, far from sufficient. The complete workflow, including the band-gap and local-moment diagnostics that certify any such extraction, is implemented in the openly available Mag4 package, so that $J_{ring}$ costs no more effort to obtain than $J$.

## Full Text

Sixteen-State Energy Mapping for First-Principles Four-Spin Ring Exchange: Validation on La2CuO4 and SrFeO2

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.18986v2 [cond-mat.mtrl-sci] 22 Jul 2026

## Sixteen-State Energy Mapping for First-Principles Four-Spin Ring
Exchange: Validation on La2CuO4and SrFeO2Xavier RocquefelteUniv Rennes, CNRS, Institut des Sciences Chimiques de Rennes - UMR 6226, F-35000 Rennes, Francexavier.rocquefelte@univ-rennes.frPeter BlahaTechnische Universität Wien, Institute for Materials Chemistry, A-1060 Vienna, Austria

## Abstract

Four-spin ring (cyclic) exchangeJringJ_{\mathrm{ring}}is an essential ingredient of the Heisenberg spin
Hamiltonian of cuprates and other square-lattice magnets, yet it has lacked the kind of
direct, local first-principles extraction that the four-state method provides for
bilinear exchange,JJ. We supply it by generalizing that method to a sixteen-state (242^{4})
scheme. Symmetry reduces the sixteen configurations to six or eight inequivalent
energies, so the cost is modest. The derivation also shows that the conventional
four-state magnetic coupling,JJ, is itself ring-renormalized, by∓2​Jring​S2\mp 2J_{\mathrm{ring}}S^{2}with the sign
set by the reference state. T-La2CuO4confirms this quantitatively: three
independent routes agree onJringJ_{\mathrm{ring}}to0.2%0.2\%, givingJring/J1=0.25J_{\mathrm{ring}}/J_{1}=0.25, and a
four-stateJ1J_{1}quoted without naming its reference is wrong by12%12\%in this
material. The direct sixteen-state extraction itself proves reference-dependent, the
Néel and ferromagnetic baths bracketing the mapping value: a fourth-order fingerprint
of interactions beyond the pair-plus-ring model, which additional reference baths
resolve into a bareJringJ_{\mathrm{ring}}and a converging tower of six- and eight-spin loop
couplings. SrFeO2(S=2S=2), with
the same plaquette yetJring/J=0.006J_{\mathrm{ring}}/J=0.006, provides the negative control: a plaquette
is necessary for ring exchange, far from sufficient. The complete workflow, including
the band-gap and local-moment diagnostics that certify any such extraction, is
implemented in the openly availableMag4package, so thatJringJ_{\mathrm{ring}}costs no
more effort to obtain thanJJ.

## keywords:ring exchange, four-spin interaction, magnetic exchange,
energy mapping, four-state method, density functional theory, cuprates\abbreviations

DFT,GGA,DMI,SIA

Dedicated to Myung-Hwan (Mike) Whangbo on the occasion of his 80th birthday.

## 1Introduction

Investigating the magnetic properties of solids is like embarking on a journey that
needs more than a lifetime simply to touch,du bout des doigts. Along such a
journey, to meet Mike Whangbo and to share his scientific enthusiasm for this field is
one of the precious gifts that life may give.

What has always characterized the Whangbo approach is that the focus falls on thedriving force: on the mechanism at the origin of a complex property, rather than
on the number that happens to describe it. As is usual in physics, in chemistry and in
materials science, the interesting problems live at an interface, with complex materials
on one side and sophisticated theories on the other. To answer a scientific question it is
essential to know where the approximations are being made: in the system, in the physics,
and in the method that carries the physics. With Mike, in the spirit of Roald
Hoffmann,22,1the physics is of prime importance, but the
chemistry stands at exactly the same level. The resultingjeu d’équilibristeconsists in choosing the best approximants of both, so that the model is just good
enough to meet the outcome it is asked to deliver: to explain, to rationalize, and also
to predict. Numerical accuracy, in this view, is not the point; trends are.

This is Mike’s way with magnetism, the distillation of many years spent in the
company of magnetic materials. The spin-dimer
analysis23,6estimates the exchange couplings of an extended solid
from calculations on the dimer that actually matters, isolating the relevant pair from
the crystal that surrounds it and reading the trend directly from the orbital
interaction. The four-state
method24,26is the natural descendant of that idea. By flipping the
two spins of a chosen pair through their four relative orientations and combining the
resulting total energies, itdecontaminatesa periodic DFT calculation from the
neighborhood of the selected dimer: every coupling of the pair to the surrounding sea of
spins, and the spin-independent energy itself, cancel identically, and a singleJi​jJ_{ij}survives. The method is exact within the Ising decomposition of the collinear energy and
extends without modification to the full anisotropic exchange tensor.18

The bilinear Heisenberg Hamiltonian that the four-state method serves is not, however,
always sufficient. Whenever the on-site repulsionUUis not overwhelmingly larger than
the hoppingtt, higher-order multi-spin interactions arise in the systematict/Ut/Uexpansion of the half-filled Hubbard model, derived by Takahashi19and
given in closed form to fourth order by MacDonald, Girvin and
Yoshioka.11The leading term of this kind is the four-spin ring (cyclic)
exchangeJringJ_{\mathrm{ring}}, which describes the coherent circulation of the electrons around a
closed loop of fourcoplanarmagnetic centers, each a nearest neighbor of the
next: it appears at ordert4/U3t^{4}/U^{3}as the
coefficient of the plaquette operator of Eq. (1) below, accompanied by
corrections of the same order to the bilinear couplings. Whether it matters at all is,
in the first place, a question of local structure. The loop must actually exist: only when the four hops that carry an electron once around
the ring are equivalent do their amplitudes add coherently. Its archetype is a square net
of transition-metal cations bridged by ligands, such as the CuO2plane of a cuprate,
but any four-site plaquette will serve; where no such loop exists there is no ring
exchange, and even where one doesJringJ_{\mathrm{ring}}may be small. Where the loop is present and the
electronic structure cooperates, however,JringJ_{\mathrm{ring}}can be large, contributing both
four-spin and renormalized two-spin terms to the effective Hamiltonian.20

The archetype is the Cu4O4plaquette of the cuprate CuO2plane.
Polarized-neutron diffuse-scattering measurements on La2CuO4gave direct
experimental evidence for four-spin cyclic exchange,20and periodic
first-principles calculations subsequently confirmedJring≈0.2J_{\mathrm{ring}}\approx 0.2–0.3​J0.3\,Jfor
several cuprate parents,13,4whereJJdenotes the
nearest-neighbor Heisenberg exchange, the largest coupling in these materials. The orthorhombic manganites
supply a second and quite different setting: Fedorova\latinet al. found that the DFT
energies of many collinear configurations of o-RRMnO3simply cannot be fitted by a
Heisenberg-plus-biquadratic model, that adding the four-spin ring term improves the fit
dramatically, and that the resulting coupling, carried by the four-site Mn plaquettes both
within thea​babplanes and between them, is strong enough to stabilize entirely new
magnetic orders.9,8The ring term carries a sting in the
tail, moreover: it is invisible to linear spin-wave theory on the two-sublattice Néel
state, so that determining it demands either the paramagnetic structure factor or a
total-energy approach sensitive to the four-spin term.

The four-state method does not provide it. The ring operator is quadrilinear in the
spins, so a two-spin flip cannot isolate it: whatever combination of four energies one
forms, the four-spin term either cancels along with everything else or survives mixed
with the pair couplings. What is needed is not a different philosophy but the next member
of the same family.

Here we propose that extension. Flipping the four spins of a nearest-neighbor plaquette
through their242^{4}collinear arrangements and combining the total energies in a single
signed sum, we obtain asixteen-statemethod that cancels the spin-independent
constant, the molecular fields exerted by the surrounding bath, and every pair coupling,
leavingJringJ_{\mathrm{ring}}alone. It is the same act of decontamination, performed one order higher.
Symmetry reduces the sixteen configurations to six or eight inequivalent energies,
depending on the stacking of the layers, so the cost remains modest. To test its relevance we compareJringJ_{\mathrm{ring}}extracted by two independent
routes: energy mapping over many collinear configurations, and the sixteen-state method
proposed here. We find, as a by-product of the derivation, that the four-state pair
coupling is itself ring-renormalized, a prediction we confirm quantitatively.

The method is tested on two materials chosen to be as different as possible.
La2CuO4is the archetypal parent of the high-TcT_{c}cuprates, aS=1/2S=1/2square-lattice antiferromagnet in which ring exchange is known to matter. SrFeO2is an
infinite-layer iron oxide whose surprising “flat” chemistry (square-planar Fe(II) in an
oxide, unprecedented until its discovery21) placesS=2S=2spins on a
square lattice of a completely different electronic character. The two structures are shown in Fig.1.Figure 1:The two test materials. (a) T-phase La2CuO4(K2NiF4type,I​4/m​m​mI4/mmm; Cu blue, O red, La green). Each Cu sits at the centre of a Jahn–Teller
elongated CuO6octahedron, the apical oxygen lying along𝐜\mathbf{c}, and the CuO2layers are stacked body-centred. (b) A CuO2layer viewed along𝐜\mathbf{c}: the Cu
ions form a square lattice bridged by oxygen, so that the nearest-neighbor coupling
proceeds through a180∘180^{\circ}Cu–O–Cu superexchange path. Four such Cu and the four
bridging O define the Cu4O4plaquette on which the ring exchange of
Fig.2circulates. (c) Infinite-layer SrFeO2(P​4/m​m​mP4/mmm; Fe gold, O red,
Sr green). Here there isnoapical oxygen: the Fe(II) is square-planar
coordinated, a coordination unprecedented in an oxide until this compound was
discovered.21The Fe ions nevertheless form the same magnetic square
lattice within each FeO2plane, but carryS=2S=2and a very different electronic
structure, which is what makes the pair a demanding test of a single formula.

## 2From four states to sixteen states

## 2.1Collinear reduction of the ring operator

We consider a classical Heisenberg system whose energy isE=E0+EspinE=E_{0}+E_{\rm spin}, withE0E_{0}independent of the spin orientations andEspin=∑⟨i,j⟩Ji​j​(𝐒i⋅𝐒j)+∑⟨i,j,k,l⟩Jring​[(𝐒i⋅𝐒j)​(𝐒k⋅𝐒l)+(𝐒i⋅𝐒l)​(𝐒k⋅𝐒j)−(𝐒i⋅𝐒k)​(𝐒j⋅𝐒l)],E_{\rm spin}=\sum_{\langle i,j\rangle}J_{ij}\,(\mathbf{S}_{i}\!\cdot\!\mathbf{S}_{j})\;+\;\sum_{\langle i,j,k,l\rangle}J_{\mathrm{ring}}\Big[(\mathbf{S}_{i}\!\cdot\!\mathbf{S}_{j})(\mathbf{S}_{k}\!\cdot\!\mathbf{S}_{l})+(\mathbf{S}_{i}\!\cdot\!\mathbf{S}_{l})(\mathbf{S}_{k}\!\cdot\!\mathbf{S}_{j})-(\mathbf{S}_{i}\!\cdot\!\mathbf{S}_{k})(\mathbf{S}_{j}\!\cdot\!\mathbf{S}_{l})\Big],(1)

where⟨i,j⟩\langle i,j\rangleruns over pairs of spin sites and⟨i,j,k,l⟩\langle i,j,k,l\rangleover the four-site nearest-neighbor plaquettes, whose corners are labeled cyclically so
that(i,j)(i,j),(j,k)(j,k),(k,l)(k,l)and(l,i)(l,i)are the plaquetteedgesand(i,k)(i,k)and(j,l)(j,l)itsdiagonals(Fig.2). We follow the notation of
Fedorova\latinet al.,8,9whose four-spin couplingKi​j​k​lK_{ijkl}is ourJringJ_{\mathrm{ring}}. In a collinear state with quantization axiszzwe write𝐒i=σi​S\mathbf{S}_{i}=\sigma_{i}Swithσi=±1\sigma_{i}=\pm 1, so that𝐒i⋅𝐒j=σi​σj​S2\mathbf{S}_{i}\!\cdot\!\mathbf{S}_{j}=\sigma_{i}\sigma_{j}S^{2}. The three products in the bracket of
Eq. (1) then each reduce toσi​σj​σk​σl​S4\sigma_{i}\sigma_{j}\sigma_{k}\sigma_{l}S^{4}, two with a
plus sign and one with a minus, so that foranyplaquetteQQof the latticeEring​(Q)|collinear=Jring​S4​∏i∈Qσi.E_{\rm ring}(Q)\big|_{\rm collinear}=J_{\mathrm{ring}}S^{4}\prod_{i\in Q}\sigma_{i}.(2)

The cyclic operator collapses, on any collinear configuration, to the plain
product of its four spin signs (Fig.2). This single observation underlies
the whole scheme.Figure 2:Origin and structure of the four-spin ring exchange on a square plaquette.
(a) The four sitesii,jj,kk,llof a nearest-neighbor plaquette, with the
edge hopping integralsti​jt_{ij},tj​kt_{jk},tk​lt_{kl},tl​it_{li}and the diagonal
hoppingsti​kt_{ik},tj​lt_{jl}of the underlying Hubbard model; cyclic circulation of the
electrons around this loop generatesJringJ_{\mathrm{ring}}at fourth order in the hopping,Jring∝t4/U3J_{\mathrm{ring}}\propto t^{4}/U^{3},19,11wherettis the transfer integral between neighboring magnetic
sites andUUthe on-site Coulomb repulsion.
(b) The bilinear couplings retained in Eq. (1): the nearest-neighbor
exchangeJJalong a plaquette edge and the next-nearest-neighbor exchangeJdJ_{d}along a
plaquette diagonal. (c) The three spin pairings entering the cyclic ring operator of
Eq. (1):(𝐒i⋅𝐒j)​(𝐒k⋅𝐒l)(\mathbf{S}_{i}\!\cdot\!\mathbf{S}_{j})(\mathbf{S}_{k}\!\cdot\!\mathbf{S}_{l}),(𝐒i⋅𝐒l)​(𝐒j⋅𝐒k)(\mathbf{S}_{i}\!\cdot\!\mathbf{S}_{l})(\mathbf{S}_{j}\!\cdot\!\mathbf{S}_{k})and(𝐒i⋅𝐒k)​(𝐒j⋅𝐒l)(\mathbf{S}_{i}\!\cdot\!\mathbf{S}_{k})(\mathbf{S}_{j}\!\cdot\!\mathbf{S}_{l}), the last entering with a minus sign.
On any collinear configuration all three collapse to the single productσi​σj​σk​σl​S4\sigma_{i}\sigma_{j}\sigma_{k}\sigma_{l}S^{4}[Eq. (2)], which is the observation
that makes the sixteen-state extraction possible.

## 2.2Exact decomposition and the extraction formula

Following the four-state construction, we single out one plaquette with cornersi,j,k,li,j,k,l, flip only its four spins, and hold every remaining spin of the supercell
fixed in a reference configuration; these fixed surrounding spins we call thebath.
Sorting each term of Eq. (1) by how many of the
four chosen sites it touches gives an exact decomposition,E​(σi,σj,σk,σl)=Eother\displaystyle E(\sigma_{i},\sigma_{j},\sigma_{k},\sigma_{l})=E_{\rm other}+S​(Ki​σi+Kj​σj+Kk​σk+Kl​σl)\displaystyle+S\,\big(K_{i}\sigma_{i}+K_{j}\sigma_{j}+K_{k}\sigma_{k}+K_{l}\sigma_{l}\big)(3)+S2​(J~i​j​σi​σj+J~j​k​σj​σk+J~k​l​σk​σl+J~l​i​σl​σi)\displaystyle+S^{2}\big(\tilde{J}_{ij}\sigma_{i}\sigma_{j}+\tilde{J}_{jk}\sigma_{j}\sigma_{k}+\tilde{J}_{kl}\sigma_{k}\sigma_{l}+\tilde{J}_{li}\sigma_{l}\sigma_{i}\big)+S2​(J~i​k​σi​σk+J~j​l​σj​σl)+Jring​S4​σi​σj​σk​σl,\displaystyle+S^{2}\big(\tilde{J}_{ik}\sigma_{i}\sigma_{k}+\tilde{J}_{jl}\sigma_{j}\sigma_{l}\big)+J_{\mathrm{ring}}S^{4}\,\sigma_{i}\sigma_{j}\sigma_{k}\sigma_{l},

in whichEotherE_{\rm other}collects everything independent of the four flipped
spins,KiK_{i}is the molecular field the bath exerts on siteii(the plaquette
counterpart of the𝐊1,𝐊2\mathbf{K}_{1},\mathbf{K}_{2}of Xiang\latinet al.24),
andJ~i​j\tilde{J}_{ij}is aneffectivepair coupling. The decisive property is that all
of these depend on the fixed bath butnotonσi,σj,σk,σl\sigma_{i},\sigma_{j},\sigma_{k},\sigma_{l}, so
they are common to all sixteen states. Two features of the coefficients matter for what
follows, and both are derived in full in the Supporting Information. First, the effective
edge couplings are ring-renormalized,J~i​j=Ji​j+Jring​S2​σe1​σe2\tilde{J}_{ij}=J_{ij}+J_{\mathrm{ring}}S^{2}\,\sigma_{e_{1}}\sigma_{e_{2}},
whereσe1​σe2\sigma_{e_{1}}\sigma_{e_{2}}is the product of the two bath spins of the neighboring
plaquette that shares the edge(i,j)(i,j), while the two diagonals carry no ring term. Second,
the expansion containsnoterm of odd degree in the flipped spins and only the
chosen plaquette supplies a degree-four term, because two distinct nearest-neighbor
plaquettes share at most an edge; this is the structural reasonJringJ_{\mathrm{ring}}can be isolated
cleanly.
Label the sixteen sign patternsn=1,…,16n=1,\ldots,16, and letEnE_{n}be the energy of patternnngiven by Eq. (3). Isolation is achieved by weighting eachEnE_{n}by its own
ring productσi​σj​σk​σl\sigma_{i}\sigma_{j}\sigma_{k}\sigma_{l}and summing. Every lower-degree term cancels
identically (∑nσi​σj​σk​σl=0\sum_{n}\sigma_{i}\sigma_{j}\sigma_{k}\sigma_{l}=0over the sixteen states, and likewise
against each single spin and each pair), leavingJring=116​S4​∑n=116σi​σj​σk​σl​En\boxed{\;J_{\mathrm{ring}}=\frac{1}{16S^{4}}\sum_{n=1}^{16}\sigma_{i}\sigma_{j}\sigma_{k}\sigma_{l}\,E_{n}\;}(4)

the four-spin counterpart of the four-state formula24,18J12=(E1+E4−E2−E3)/4​S2J_{12}=(E_{1}+E_{4}-E_{2}-E_{3})/4S^{2}. The prefactor is16​S4=116S^{4}=1forS=1/2S=1/2(La2CuO4), so thatJringJ_{\mathrm{ring}}is then simply the signed sum of the sixteen energies,
and16​S4=25616S^{4}=256forS=2S=2(SrFeO2).

## 2.3Symmetry reduction

Because the coefficients of Eq. (3) are common to all sixteen states,
states related by the symmetry of the fixed bath share an energy, and the sixteen
collinear arrangements collapse to few inequivalentmodelenergies: six
on the ideal single-layer square lattice, and eight in the body-centered stacking of
T-La2CuO4, where the layers are offset by(12,0,12)(\tfrac{1}{2},0,\tfrac{1}{2})and the
plaquette-centeredC4C_{4}is not a crystallographic operation. The reduction must be
carried out in the magnetic (grey) group, with time reversal included; the
antiunitaryC4×𝒯C_{4}\times\mathcal{T}is what completes the collapse to six on the ideal
lattice. The full class structure, multiplicities, and cancellation identity are given in
the Supporting Information; in practice Eq. (4) is evaluated over the
inequivalent classes alone, each weighted by its ring product and multiplicity, for any
choice of reference bath.

The reduction to six energies is a property of the spin Hamiltonian, not of the
crystal, so the extra configurations left inequivalent by a lower-symmetry cell become atestof the model rather than a cost. In the body-centered supercell, the two extra degeneracies link configurations of
opposite magnetization whose energies the crystal could split only through the interlayer
coupling (negligible here), so our VASP calculations (16 Cu, Néel bath, all eight
configurations insulating, gaps 1.10–1.88 eV; Table3) find the pair
degenerate to 10μ\mueV. Details are given in the Supporting Information.

## 2.4Ring exchange contaminates the four-state pair couplings

Equation (3) has a consequence that deserves emphasis. In the
conventional four-state extraction of a nearest-neighbor coupling only the two
spins of the dimer are flipped, sobothplaquettes containing that bond
have their two remaining corners in the fixed bath. On a Néel bath the spins on each of
those corner pairs are antiparallel, so the quantity actually returned is not the bare
coupling but the effective one,JNN4-state​(Néel)=J~NN=JNN−2​Jring​S2,JNN4-state​(FM)=JNN+2​Jring​S2,J^{\text{4-state}}_{\rm NN}(\text{N\'{e}el})=\tilde{J}_{\rm NN}=J_{\rm NN}-2J_{\mathrm{ring}}S^{2},\qquad J^{\text{4-state}}_{\rm NN}(\text{FM})=J_{\rm NN}+2J_{\mathrm{ring}}S^{2},(5)

the sign of the renormalization being set by the reference. This is the microscopic
counterpart of the well-known result that cyclic exchange renormalizes the effective pair
exchange entering a spin-wave fit.20The shift is−Jring/2-J_{\mathrm{ring}}/2forS=1/2S=1/2and−8​Jring-8J_{\mathrm{ring}}forS=2S=2: far from negligible, so the sixteen-state scheme is
needed not only to obtainJringJ_{\mathrm{ring}}but to correctJJitself.

## 2.5A two-bath determination of the ring coupling

The two references in Eq. (5) differ only in the sign of the ring term,
which affords an independent route toJringJ_{\mathrm{ring}}requiring no sixteen-state calculation at
all:Jring=JNN4-state​(FM)−JNN4-state​(Néel)4​S2\boxed{\;J_{\mathrm{ring}}=\frac{J^{\text{4-state}}_{\rm NN}(\text{FM})-J^{\text{4-state}}_{\rm NN}(\text{N\'{e}el})}{4S^{2}}\;}(6)

Two standard four-state calculations with different baths therefore determine the ring
coupling. Because Eq. (6) involves entirely different energy differences
from Eq. (4), agreement between the two is a strong internal consistency
check, carried out below. A four-stateJJreported without its reference bath is therefore ill-defined whenever ring exchange is present.

Equation (6) carries a second, sharper prediction that could fail. It
applies to the plaquetteedge. The plaquettediagonalbehaves differently:
the single plaquette containing both diagonal sites has its two remaining corners as
next-nearest neighbors, whose spins are parallel in a ferromagneticandin a
Néel bath alike, soJNNN4-state=JNNN+Jring​S2for either bath.J^{\text{4-state}}_{\rm NNN}=J_{\rm NNN}+J_{\mathrm{ring}}S^{2}\qquad\text{for either bath.}(7)

A single pair of four-state calculations therefore tests two things at once: one coupling
must shift by exactly4​Jring​S24J_{\mathrm{ring}}S^{2}, and the other must not shift at all.

## 2.6Scope of the method

Two limitations should be stated explicitly. First, the collinear construction is blind to
the two-site biquadratic termBi​j​(𝐒i⋅𝐒j)2B_{ij}(\mathbf{S}_{i}\!\cdot\!\mathbf{S}_{j})^{2}, which reduces to a
spin-independent constant on any collinear state; for the isolation ofJringJ_{\mathrm{ring}}this is an
advantage, but a biquadratic coupling, if required, must be obtained separately from
non-collinear states. Second, the scheme returns thediagonalmatrix element of the
ring operator in the broken-symmetry (Ising) sense of Moreira, Calzado and
Malrieu;13,4the off-diagonal flip-flop parts of the
cyclic-permutation operator are invisible to collinear DFT. This is precisely what is
required to extract the coefficientJringJ_{\mathrm{ring}}of Eq. (1), but it is not the same
object as the Dirac permutation amplitude, as discussed with the results.

## 3Computational details

Spin-polarized total energies were computed with the projector augmented-wave
method3as implemented in VASP,10using the PBE
form of the generalized-gradient approximation14with a Hubbard
correction (GGA+U+U)7on the transition-metalddstates. A
plane-wave cutoff of 500 eV and an energy convergence threshold of10−510^{-5}eV
were used throughout. Brillouin-zone integrations for the SrFeO2energy mapping used
the tetrahedron method with Blöchl corrections (ISMEAR=−5=-5); the
per-configuration band gaps and local moments quoted as diagnostics below were verified
to be unchanged under Gaussian smearing (ISMEAR=0=0,σ=0.01\sigma=0.01eV).

For La2CuO4we adopt the ideal tetragonal (K2NiF4,I​4/m​m​mI4/mmm) T-phase cell,a=3.7817a=3.7817Å, withUeff=8U_{\rm eff}=8eV on Cu; the ring plaquette is the Cu4O4square, whose edges are the nearest-neighbor bonds (3.7817 Å) and whose diagonals are
the next-nearest-neighbor bonds (5.3481 Å). For SrFeO221we use theP​4/m​m​mP4/mmminfinite-layer cell (a=5.6356a=5.6356Å,c=3.4580c=3.4580Å), withUeff=4U_{\rm eff}=4eV on Fe; the ring plaquette is the in-plane Fe4square of edge
3.9850 Å, whose diagonal is 5.6356 Å. The magnetic moments correspond toS=1/2S=1/2(Cu2+) andS=2S=2(Fe2+).

Several supercells were used, and each is named with the result it produced; they were
chosen so that the probed dimer or plaquette is isolated from its periodic images beyond
the longest coupling retained, a requirement discussed further below. Two cell shapes
recur: direct repetitions of the crystallographic cell, and repetitions of the2​a×2​a×c\sqrt{2}a\times\sqrt{2}a\times ccell, whose in-plane vectors run along the diagonals
of the magnetic square lattice, at45∘45^{\circ}to the crystallographic axes, and which
holds two magnetic sites per layer. We refer to the latter as the2\sqrt{2}cell; it is
the natural cell of the Néel order, and its repetitions isolate a plaquette with fewer
atoms than repetitions of the crystallographic cell.

The decomposition and extraction are written out explicitly for the
SrFeO2coupling topology in the Supporting Information: there the plaquette lies in
the FeO2plane, whileJ1J_{1}(along𝐜\mathbf{c}) andJ3J_{3}(the inter-layer
diagonal) connect the plaquette only to the bath and cancel identically in the
extraction.

## 3.1Implementation: the MAG4 package

The obstacle to using these methods is rarely the physics, but the chain of practical
steps that surrounds it. One must
identify the magnetic sublattice and its coupling shells, choose a supercell large enough
to isolate the probed dimer or plaquette from its periodic images, enumerate the
symmetry-inequivalent spin configurations together with their multiplicities, write the
corresponding inputs, and then reduce the resulting total energies with the right signs and
weights. Each step is elementary and each is easy to get wrong, as the discussion of
supercell aliasing below illustrates.

All the calculations reported here were prepared and analysed withMag4, a Python
suite we have developed for this purpose.16Starting from a crystallographic
information file, it determines the magnetic sublattice and the inequivalent exchange paths
by symmetry, builds the supercell, and generates the spin configurations required for
energy mapping, for the four-state method, and for the sixteen-state method introduced
here, reducing them with the magnetic (grey) group so that time reversal is included. It
writes ready-to-run inputs for either VASP or WIEN2k, and afterwards parses the outputs,
checks that every configuration is converged and carries the intended local moments, and
returns the couplings, either by the closed-form combination of Eq. (4)
(evaluated over the inequivalent classes, each weighted by its ring product and
multiplicity) or by a least-squares fit over many configurations, with residuals and error bars. The figures of merit quoted throughout this paper, the fit root-mean-square (RMS) residual and the per-configuration residuals of Fig.5among them, are produced by it.Mag4is openly available.16A full description of the package, of its
symmetry analysis and of the additional interactions it can treat will be published
separately; here we record only that the results below were obtained with it, and that the
sixteen-state method requires no more effort from the user than the four-state method it
extends.

## Gap and moment as validity diagnostics.

A final, practical point belongs with the package, because it governs when the couplings it returns can be trusted. Every one of these methods, energy mapping, the four-state method and the sixteen-state method, rests on the assumption that each configuration entering the extraction remains in the localized-spin regime that Eq. (1)
describes. The two quantities that decide whether it does, the band gap and the local moment, are obtained for free in any total-energy calculation, andMag4prints both for every configuration, flagging any that is metallic or whose magnetization is inconsistent with its intended pattern. Of the two the gap is the more incisive: a configuration can keep a healthy local moment yet cross into the gapless regime, where a Heisenberg mapping no longer applies, so a moment check alone can give false reassurance.
The gap and the moment should therefore accompany any extracted coupling as a validity certificate, not be left implicit.

This carries a direct consequence for the choice of reference. Because the gap falls with the ferromagnetic character of a configuration, a ferromagnetic reference operates the calculation closest to the metallic edge and is the first to cross it as correlations weaken. For gap-sensitive materials the couplingsJJandJringJ_{\mathrm{ring}}are therefore best extracted with the four-state and sixteen-state methods anchored on the ground-state-like reference, which keeps the largest gap and the best-conserved moments, rather than on a ferromagnetic reference or on an energy mapping forced to sample high-energy
configurations of uncertain character. The local methods are in this sense the safer
instrument: they never have to leave the neighbourhood of the ground state, where the localized-spin model is secure. La2CuO4and SrFeO2illustrate the two regimes; the supporting gaps, moments and couplings are given with the results below.

## 4Results and discussion

## La2CuO4: bilinear couplings and ring exchange.

Couplings were obtained from two independent supercells (Table1). In a2×2×12\times 2\times 1cell (8 Cu, 13 configurations,9×9×59\times 9\times 5kk-mesh) the
energy-mapping fit has RMS=8.6=8.6μ\mueV and givesJ1=130.51J_{1}=130.51meV,J2=6.41J_{2}=6.41meV, a negligible interlayer term, andJring=32.69J_{\mathrm{ring}}=32.69meV. The quality of
that fit, and the resulting couplings, are shown in Fig.3. In a2×3×12\times 3\times 1cell (12 Cu, 49 configurations) the same analysis givesJ1=129.89J_{1}=129.89,J2=6.66J_{2}=6.66andJring=32.32J_{\mathrm{ring}}=32.32meV. Two cells of different shape,
with differentkk-meshes, therefore agree on the dimensionless ratio to better than1%1\%:Jring/J1=0.2505​(2×2×1),0.2488​(2×3×1),J_{\mathrm{ring}}/J_{1}=0.2505\;\;(2\times 2\times 1),\qquad 0.2488\;\;(2\times 3\times 1),(8)

in close agreement with the periodic-DFT result of Moreira\latinet
al.,13whose values are listed alongside ours in Table1.
Their hybrid-functional calculation givesJ=140.1J=140.1andJring=35.8J_{\mathrm{ring}}=35.8meV, both77–9%9\%above our GGA+U+Uvalues, a shift of the expected size and direction between
the two exchange-correlation treatments; the small diagonal coupling, more delicate as
discussed with the shell aliasing below, differs more (J2=8.8J_{2}=8.8against our6.46.4meV). The dimensionless ratio, however, agrees to2%2\%:0.2500.250here against
their0.2560.256. MeanwhileJring=32.7J_{\mathrm{ring}}=32.7meV lies within the
experimental estimates of Coldea\latinet al.5(38±838\pm 8meV) and
Mizuno\latinet al.12(40 meV). The experimental ratio itself
spreads with temperature and with the model used in the fit: the Hubbard-expansion
analysis of Coldea\latinet al.5givesJring/J1=0.27J_{\mathrm{ring}}/J_{1}=0.27at
295 K but0.420.42at 10 K, and the analysis of Toader\latinet
al.20reaches≈0.5\approx 0.5. As Moreira\latinet
al.13observed of their own, nearly identical ratio, values near0.250.25are in close agreement with the generally acceptedJring/J≈0.3J_{\mathrm{ring}}/J\approx 0.3for this compound, and our two supercells sit in the same
place.Figure 3:Energy mapping for T-La2CuO4in the2×2×12\times 2\times 1supercell.
(a) Model energies against DFT energies for the 13 inequivalent collinear
configurations, both measured from the lowest-energy state. The line isy=xy=x, not a
fit to the points. The residuals, plotted below on a scale four orders of magnitude
finer, lie within±0.02\pm 0.02meV and give an RMS of0.0090.009meV over an energy range of
more than11eV, so the spin model of Eq. (1) reproduces the first-principles
energies essentially exactly.
(b) The couplings extracted from that fit: the nearest-neighbor exchangeJ1J_{1}, the
next-nearest-neighborJ2J_{2}, the interlayerJ3J_{3}, and the four-spin ring couplingJringJ_{\mathrm{ring}}. Error bars are±2​σ\pm 2\sigmafrom the least-squares fit and are smaller than
the symbols. Two features are worth noting:J3J_{3}is indistinguishable from zero,
confirming that the interlayer coupling is negligible; andJringJ_{\mathrm{ring}}is not a small
correction but the second-largest term in the Hamiltonian, five timesJ2J_{2}and one
quarter ofJ1J_{1}.Table 1:Exchange couplings of T-phase La2CuO4(meV) from two supercells. The Moreira\latinet al.13column is their periodic hybrid-functional (Fock-35,Crystal) result on the experimental structure, with the same ring operator and broken-symmetry mapping; theirJJ,JdJ_{d},JringJ_{\mathrm{ring}}are ourJ1J_{1},J2J_{2},JringJ_{\mathrm{ring}}. The experimental column is thett–UUHubbard spin-wave fit of Coldea\latinet al.5at 295 K, theirJ′=J′′J^{\prime}=J^{\prime\prime}mapping to ourJ2J_{2}andJ4J_{4}; the same fit at 10 K givesJ=146.3±4J=146.3\pm 4andJring=61±8J_{\mathrm{ring}}=61\pm 8meV (Jring/J1=0.42J_{\mathrm{ring}}/J_{1}=0.42).Couplingdd(Å)2×2×12\times 2\times 12×3×12\times 3\times 1Ref.13Exp.5J1J_{1}(NN, plaquette edge)3.7817130.51129.89140.1138.3±4138.3\pm 4J2J_{2}(NNN, plaquette diagonal)5.34816.416.668.82.0±0.52.0\pm 0.5J3J_{3}(interlayer)7.1441−0.001-0.001−0.014-0.014J4J_{4}(3rd in-plane)7.5634indet.2.902.902.0±0.52.0\pm 0.5JringJ_{\mathrm{ring}}—32.6932.3235.838±838\pm 8Jring/J1J_{\mathrm{ring}}/J_{1}0.25050.24880.2560.27fit RMS (meV)0.00860.697

## Quantitative confirmation of the ring renormalization ofJJ.

Equation (5) makes a sharp, falsifiable prediction: a four-state
calculation performed on a Néel reference must return not the trueJ1J_{1}butJ1−2​Jring​S2J_{1}-2J_{\mathrm{ring}}S^{2}. We test it directly. In thesame2×2×12\times 2\times 1cell and
at thesame9×9×59\times 9\times 5kk-mesh as the reference mapping run, the
conventional four-state method returnsJ14-state​(Néel)=114.19J_{1}^{\text{4-state}}(\text{N\'{e}el})=114.19meV, a deficit of16.3116.31meV below the mapping valueJ1=130.51J_{1}=130.51meV.
Inverting Eq. (5), that deficit is an independent determination of the
ring coupling that uses only bilinear energy differences,Jring=J1−J14-state​(Néel)2​S2=16.310.5=32.62​meV,J_{\mathrm{ring}}=\frac{J_{1}-J_{1}^{\text{4-state}}(\text{N\'{e}el})}{2S^{2}}=\frac{16.31}{0.5}=32.62~\text{meV},(9)

in agreement with the32.6932.69meV of the energy mapping to0.2%0.2\%. This is a stringent,
parameter-free check of the entire framework, obtained without any sixteen-state
calculation: the four-state coupling is ring-renormalized by exactly the predicted
amount, and a four-stateJJquoted without reference to its bath is, in a material with
ring exchange, wrong by12%12\%here.

## Two independent determinations ofJringJ_{\mathrm{ring}}from bilinear energies.

Equation (6) can now be applied directly. Repeating the four-state
calculation of the nearest-neighbor bond in the same supercell andkk-mesh, but on a ferromagnetic reference, returnsJ14-state​(FM)=146.83J_{1}^{\text{4-state}}(\text{FM})=146.83meV, againstJ14-state​(Néel)=114.19J_{1}^{\text{4-state}}(\text{N\'{e}el})=114.19meV. Since4​S2=14S^{2}=1forS=1/2S=1/2, the
differenceisthe ring coupling:Jring=J14-state​(FM)−J14-state​(Néel)=146.83−114.19=32.64​meV.J_{\mathrm{ring}}=J_{1}^{\text{4-state}}(\text{FM})-J_{1}^{\text{4-state}}(\text{N\'{e}el})=146.83-114.19=32.64~\text{meV}.(10)

Three routes now give the same number from three different sets of energy differences:32.6932.69meV from the energy mapping,32.6232.62meV from inverting the deficit against the
mappingJ1J_{1}[Eq. (9)], and32.6432.64meV from the two baths
[Eq. (10)]. The spread is0.070.07meV, or0.2%0.2\%ofJringJ_{\mathrm{ring}}. Applying
the correction from either side likewise recovers the true coupling, and brackets it:146.83−2​Jring​S2=130.49146.83-2J_{\mathrm{ring}}S^{2}=130.49meV and114.19+2​Jring​S2=130.54114.19+2J_{\mathrm{ring}}S^{2}=130.54meV, against130.51130.51meV from the energy mapping. The Supporting Information collects, as a
practical recipe, the ring correction to apply to the four-state couplings for every
supercell and reference bath used here.

The same pair of calculations tests the second, more delicate prediction,
Eq. (7). The next-nearest-neighbor coupling should beunaffectedby the
choice of reference, because the spins on the two bath corners flanking the probed
diagonal (themselves next-nearest neighbors, on the same sublattice) are parallel in a
Néel bath as in a ferromagnetic one. The two calculations returnJ24-state​(FM)=14.582J_{2}^{\text{4-state}}(\text{FM})=14.582meV andJ24-state​(Néel)=14.588J_{2}^{\text{4-state}}(\text{N\'{e}el})=14.588meV: a difference of0.0060.006meV, where the
nearest-neighbor coupling in the very same calculations shifts by32.6432.64meV. One coupling
moves by exactlyJringJ_{\mathrm{ring}}and the other does not move at all, precisely as
Eqs. (6) and (7) require.

The absolute value should not be
misread, however:14.5814.58meV is theeffectivediagonal coupling, containing the
reference-independent ring shift+Jring​S2=8.17+J_{\mathrm{ring}}S^{2}=8.17meV of Eq. (7).
Subtracting it recovers the bareJ2=6.41J_{2}=6.41and6.426.42meV on the two references, both
matching the energy-mapping value; taken at face value an uncorrected four-state result
would overestimate the next-nearest-neighbor exchange by more than a factor of two. This
is the sharpest confirmation of the framework that we have, and it costs eight
self-consistent calculations.Table 2:JringJ_{\mathrm{ring}}for T-La2CuO4from three independent routes, all in the same2×2×12\times 2\times 1cell at the same9×9×59\times 9\times 5kk-mesh, and the reference-dependence
test of the pair couplings.S=1/2S=1/2, so4​S2=14S^{2}=1and2​S2=1/22S^{2}=1/2.RouteEnergy differences usedJringJ_{\mathrm{ring}}(meV)energy mapping13 collinear configurations, global fit32.69one-bath, Eq. (9)[J1−J14-state​(Néel)]/2​S2\big[J_{1}-J_{1}^{\text{4-state}}(\text{N\'{e}el})\big]/2S^{2}32.62two-bath, Eq. (6)[J14-state​(FM)−J14-state​(Néel)]/4​S2\big[J_{1}^{\text{4-state}}(\text{FM})-J_{1}^{\text{4-state}}(\text{N\'{e}el})\big]/4S^{2}32.64spread0.07Four-state couplingNéel ref.FM ref.differenceJ14-stateJ_{1}^{\text{4-state}}(plaquette edge), must shift by4​Jring​S2=Jring4J_{\mathrm{ring}}S^{2}=J_{\mathrm{ring}}114.19146.83+32.64+32.64J24-stateJ_{2}^{\text{4-state}}(plaquette diagonal), must not shift [Eq. (7)]14.58814.582−0.006-0.006

## Sixteen-state extraction: a genuine reference dependence.

The sixteen-state extraction was performed on a body-centered supercell of sixteen Cu, eight per CuO2layer (a2×2×12\times 2\times 1repetition of the2\sqrt{2}cell, 112 atoms,6×6×56\times 6\times 5kk-mesh) in which the probed plaquette is fully isolated: no periodic image shares an
edge or a corner with it, so the fixed-bath decomposition of
Eq. (3) applies without image contamination. Every
diagnostic of the preceding sections is clean. The grey group reduces the sixteen
states to eight configurations on the Néel reference and six on the ferromagnetic
one; all are insulating, with gaps of1.101.10to1.881.88eV (Néel) and0.580.58to0.600.60eV (FM); the local moments are healthy on every site,|μ|=0.74±0.03​μB|\mu|=0.74\pm 0.03\,\mu_{B}on the Néel
reference and0.80±0.03​μB0.80\pm 0.03\,\mu_{B}on the ferromagnetic one; and the two degeneracies
that the spin model predicts beyond the grey group are satisfied to1010μ\mueV. The
two references nevertheless return different couplings (Table3):Jring=27.54J_{\mathrm{ring}}=27.54meV on the Néel bath against34.5234.52meV on the ferromagnetic one,
each value identical to that obtained in the smaller eight-Cu cell. The
all-electron WIEN2k code2, run on the same supercell at matchedkk-mesh density,
reproduces the dependence in full,23.4523.45meV on the Néel bath against36.3536.35meV on the ferromagnetic one, with every configuration again insulating
(gaps of0.480.48–0.500.50eV on the ferromagnetic reference and1.021.02–1.851.85eV on the Néel one, close to their VASP counterparts): the
effect is not an artifact of the pseudopotential construction. Each number
is a small residual of near-cancelling energies,0.4%0.4\%of the configuration-energy
spread, so this double supercell-robustness is itself significant: the difference is
not noise.

Nor is it an artifact of the numerics: replacing the tetrahedron scheme by Gaussian
smearing and tightening the electronic convergence to10−810^{-8}eV moves both values by a
fewμ\mueV only. By construction Eq. (4) is reference-independent for the
Hamiltonian of Eq. (1), so a dependence that survives the isolation of the
plaquette, the gap and moment diagnostics, and the grey-group analysis is a genuine
signal that the spin Hamiltonian of La2CuO4contains interactions beyond the
pair-plus-ring model. Its character is clear from where it appears. The bilinear sector
is clean:J2J_{2}shifts by0.0060.006meV between the two references, and the three routes
resting on bilinear energy differences agree with the mapping to0.2%0.2\%. The
contamination is confined to the quadrilinear channel, as expected from the six-spin
loops of ordert6/U5t^{6}/U^{5}that extend over the plaquette and its bath: in theχ\chi-weighted sum of Eq. (4) such terms do not cancel but enter
multiplied by products of bath spins, and so change with the reference.

The practical consequence is read off directly: the two references bracket the
energy-mapping value,27.5<32.7<34.527.5<32.7<34.5meV, and the half-splitting of the
sixteen-state pair,±3.5\pm 3.5meV (i.e.±11%\pm 11\%), is the intrinsic accuracy with
which a strictly local quadrilinear probe can defineJringJ_{\mathrm{ring}}in a material this strongly
coupled. The same splitting is at the same time a cheap physical diagnostic: obtained from only
two short four-state calculations, the FM–Néel difference measures, at fourth order,
how far the material departs from the pair-plus-ring model of Eq. (1).Table 3:JringJ_{\mathrm{ring}}(meV) for T-La2CuO4from the sixteen-state method,
Eq. (4), on the isolated-plaquette supercell (16 Cu,2×2×12\times 2\times 1repetition of the2\sqrt{2}cell,6×6×56\times 6\times 5kk-mesh).NcfgN_{\rm cfg}is the grey-group count of inequivalent configurations. Both
VASP values are identical to those obtained in the eight-Cu cell. The WIEN2k
rows are the same supercell (indexed2×1×22\times 1\times 2in the WIEN2k axis
convention) at matchedkk-mesh density: the all-electron code reproduces the
dependence.CodeReferenceNcfgN_{\rm cfg}gap range (eV)JringJ_{\mathrm{ring}}VASPNéel81.10–1.8827.54VASPFerromagnetic60.58–0.6034.52WIEN2kNéel81.02–1.8523.45WIEN2kFerromagnetic60.48–0.5036.35energy mapping (Table1)32.69two-bath, Eq. (6)32.64

## Bath decomposition: the reference dependence resolved into couplings.

If longer loops are the cause, they can be measured, because each enters the
sixteen-state sum multiplied by aknownfunction of the bath. Thet/Ut/Uexpansion
that yieldsJringJ_{\mathrm{ring}}at ordert4/U3t^{4}/U^{3}generates on every longer closed loop an
analogous cyclic term of ordertℓ/Uℓ−1t^{\ell}/U^{\ell-1}, so the leading candidates beyond
the plaquette haveℓ=6\ell=6and88.19,11Adding these
terms to Eq. (1),Espin⟶Espin+∑ℓ=6,8,…∑L∈ℒℓJL​OL,OL|collinear=Sℓ​∏i∈Lσi,E_{\rm spin}\;\longrightarrow\;E_{\rm spin}\;+\;\sum_{\ell=6,8,\ldots}\;\sum_{L\in\mathcal{L}_{\ell}}J_{L}\,O_{L}\,,\qquad O_{L}\big|_{\rm collinear}=S^{\ell}\prod_{i\in L}\sigma_{i}\,,(11)

withℒℓ\mathcal{L}_{\ell}the loops ofℓ\ellsites and eachOLO_{L}reducing on collinear
states to the product of its spin signs [generalizing Eq. (2)]. A loop that
misses a plaquette corner carries at most three plaquette spins and is annihilated by theχ\chi-weighted sum, as the pair terms are; one thatcontainsthe plaquette
survives, its four plaquette spins absorbed and its remainingℓ−4\ell-4bath spins left as
a fixed number of the reference. The method therefore returns exactlyJ~ring​(ref)=Jring+S2​∑L6∋i,j,k,lJL6​⟨σb1​σb2⟩ref+S4​∑L8∋i,j,k,lJL8​⟨σb1​σb2​σb3​σb4⟩ref,\tilde{J}_{\mathrm{ring}}(\mathrm{ref})\;=\;J_{\mathrm{ring}}\;+\;S^{2}\!\!\sum_{L_{6}\,\ni\,i,j,k,l}\!\!J_{L_{6}}\,\big\langle\sigma_{b_{1}}\sigma_{b_{2}}\big\rangle_{\mathrm{ref}}\;+\;S^{4}\!\!\sum_{L_{8}\,\ni\,i,j,k,l}\!\!J_{L_{8}}\,\big\langle\sigma_{b_{1}}\sigma_{b_{2}}\sigma_{b_{3}}\sigma_{b_{4}}\big\rangle_{\mathrm{ref}}\,,(12)

aneffectivecoupling, tilded likeJ~i​j\tilde{J}_{ij}because it is what the probe
measures, not the model parameter. On the square lattice the surviving loops fall into
three families [Fig.4(a)]: the six-spindomino(purett, two bath
spins flanking one edge); thet′t^{\prime}-assisted six-spin loop whose path zigzags across the
plaquette (two bath spins facing across it on the same sublattice); and the eight-spin
loops, led by the pure-tt3×13\times 1strip (four bath spins on two opposite edges), of
which only this largest member is drawn, itst′t^{\prime}-assisted partners feeding the same
correlator suppressed by(t′/t)2(t^{\prime}/t)^{2}. Each family couples to one bath correlatorΓℓ−4\Gamma_{\ell-4}:Γ2(e)\Gamma_{2}^{(\mathrm{e})}the mean over the four edge-flanking bath
pairs,Γ2(zz)\Gamma_{2}^{(\mathrm{zz})}over the two across-plaquette pairs, andΓ4\Gamma_{4}the product of all four in-plane bath spins. Grouping Eq. (12) by them gives
the working formJ~ring​(ref)=Jring+Γ2(e)​Je(6)+Γ2(zz)​Jzz(6)+Γ4​J(8),\tilde{J}_{\mathrm{ring}}(\mathrm{ref})\;=\;J_{\mathrm{ring}}\;+\;\Gamma_{2}^{(\mathrm{e})}\,J^{(6)}_{\mathrm{e}}\;+\;\Gamma_{2}^{(\mathrm{zz})}\,J^{(6)}_{\mathrm{zz}}\;+\;\Gamma_{4}\,J^{(8)}\,,(13)

eachJ(ℓ)J^{(\ell)}being the spin-scaled sum over the symmetry-equivalent loops of its
family, so that no fragile loop counting enters.

The four unknowns are fixed by the baths the supercell provides. The FM and Néel
references have correlator triples(+1,+1,+1)(+1,+1,+1)and(−1,+1,+1)(-1,+1,+1); twostripebaths
zero the correlators in turn, stripe1 with(0,0,−1)(0,0,-1)and stripe3 with(0,−1,+1)(0,-1,+1). A
fifth, stripe2, repeats stripe1’s flanking signature but reverses all eight out-of-plane
bath Cu: no grey-group operation connects them, yet no loop family reaches the sites that
differ, so the model predictsJ~ring​(stripe2)=J~ring​(stripe1)\tilde{J}_{\mathrm{ring}}(\text{stripe2})=\tilde{J}_{\mathrm{ring}}(\text{stripe1})with no free parameter. All configurations are
insulating and the bilinear sector stays clean. The five values, spanning77meV
[Fig.4(b)], are reproduced by

Jring=29.57J_{\mathrm{ring}}=29.57,Je(6)=3.49J^{(6)}_{\mathrm{e}}=3.49,Jzz(6)=0.90J^{(6)}_{\mathrm{zz}}=0.90,J(8)=0.57J^{(8)}=0.57meV,

and the prediction holds: stripe2 returns29.002029.0020meV against29.000729.0007meV, a1.31.3μ\mueV deviation. The full data are collected in the Supporting Information.

The all-electron code reads the same decomposition across methods. Since FM and
Néel shareΓ2(zz)=Γ4=+1\Gamma_{2}^{(\mathrm{zz})}=\Gamma_{4}=+1and differ only inΓ2(e)\Gamma_{2}^{(\mathrm{e})}, half their difference is the domino amplitude and half their
sum the combinationJring+Jzz(6)+J(8)J_{\mathrm{ring}}+J^{(6)}_{\mathrm{zz}}+J^{(8)}both baths see alike:
WIEN2k givesJe(6)=6.45J^{(6)}_{\mathrm{e}}=6.45meV against VASP’s3.493.49, while the shared
combination agrees to4%4\%(29.9029.90against31.0331.03meV). The loop amplitudes, small
residuals of near-cancelling energies, are the code-sensitive part; the bare ring physics
is not. The amplitudes form a converging tower [Fig.4(c)], each order about(t/U)2(t/U)^{2}below the last, as the counting requires: the reference dependence of
Table3is not a failure of the construction but its sensitivity,
resolving the bareJring=29.57J_{\mathrm{ring}}=29.57meV from the loop corrections any local quadrilinear
probe must see.Figure 4:Bath decomposition of the sixteen-state extraction for T-La2CuO4.
(a) The loop families of Eq. (13) on the square lattice: plaquette spins
filled, bath spins open; solid bonds are nearest-neighbor hopstt, dashed bonds
diagonal hopst′t^{\prime}; the shaded square is the probed plaquette. Of the eight-spin
family only the largest, pure-ttloop is shown. (b) The measuredJ~ring​(ref)\tilde{J}_{\mathrm{ring}}(\mathrm{ref})for the five reference baths (the legend gives
each bath’s correlator triple; AFM denotes the Néel bath), against the bareJring=29.57J_{\mathrm{ring}}=29.57meV of
Eq. (13) (solid line) and the energy-mapping value (dashed). stripe2
repeats stripe1’s flanking signature with the out-of-plane bath Cu reversed, so the
model predicts the two values to coincide; the measurement confirms it to1.31.3μ\mueV. (c) The
solved amplitudes: the bare ring coupling and the three loop-family couplings, a
tower converging by roughly(t/U)2(t/U)^{2}per order.

## Supercell design: aliasing of the pair shells.

A practical warning follows, and it applies to energy mapping generally. In the2×2×12\times 2\times 1cell the third in-plane neighbor,J4J_{4}at2​a=7.56342a=7.5634Å, isthe atom’s own periodic image: every such bond contributesσi2=+1\sigma_{i}^{2}=+1,
the column is the constant+16+16, andJ4J_{4}is exactly collinear withE0E_{0}, so that it is
silently absorbed into the constant. The fit is then perfect (8.6μ\mueV) for a spurious reason.
In the2×3×12\times 3\times 1cellJ4J_{4}is nominally determinable, but the8.45628.4562Å
shell isexactlylinearly dependent on the lower ones, so the fittedJ4J_{4}absorbs it; omittingJ4J_{4}altogether inflates the RMS from 0.70 to 2.77 meV and leaves
residuals that track the symmetry classes rather than scattering randomly. At least
three repetitions alongbothin-plane axes are needed to separate these shells.
A related sensitivity was noted by Fedorova\latinet al.,8who found
that adding a single configuration to their overdetermined system shifted the interplane
couplings by up to25%25\%, and who consequently assigned a±25%\pm 25\%uncertainty to their
extracted exchanges. The lesson is the same in both cases: the bilinear couplings
obtained by energy mapping are delicate objects, sensitive to the configuration set and
to the shells the supercell can resolve.

Crucially,JringJ_{\mathrm{ring}}is almost untouched by all of this: it moves by1.4%1.4\%between the
two cells, and by1.4%1.4\%on addingJ4J_{4}to the2×3×12\times 3\times 1fit, whileJ1J_{1}moves by 1.1 meV andJ4J_{4}appears from nothing. The four-spin coupling is protected
because its column, being a product of four spins, is orthogonal to every bilinear
column, the same orthogonality that underlies Eq. (4).

## SrFeO2.

The infinite-layer ferrous oxide provides a second test at higher spin (S=2S=2).
Symmetry analysis of the Fe sublattice gives an out-of-plane couplingJ1J_{1}along𝐜\mathbf{c}(3.4580 Å), the in-plane nearest-neighbor couplingJ2J_{2}(3.9850 Å), an
inter-layer diagonalJ3J_{3}(5.2762 Å), and the in-plane next-nearest-neighborJ4J_{4}(5.6356 Å). In the language of the derivation above,J2J_{2}is the plaquette edge andJ4J_{4}the
plaquette diagonal; the shell numbering, being by distance, doesnotcoincide
with that of La2CuO4.J1J_{1}andJ3J_{3}both leave the FeO2plane, connect the
plaquette only to the bath, and cancel identically in Eq. (4)
(Supporting Information). Results are collected in Table5, alongside the
values obtained for the same four shells by Xiang, Wei and Whangbo25from
a five-configuration energy mapping atUeff=4.6U_{\rm eff}=4.6eV. Once their shell labels
are mapped onto ours by distance, the two determinations agree throughout, down to the
sign and magnitude of the small inter-layer diagonal coupling,−0.23-0.23against our−0.22-0.22meV, and their in-plane coupling of7.047.04meV coincides with our ring-corrected
four-state value of7.047.04meV.

The energy mapping is shown in Fig.5. The in-plane nearest-neighbor
coupling dominates,J2=6.99J_{2}=6.99meV, with the out-of-planeJ1=1.48J_{1}=1.48meV four times
smaller, andJ3J_{3},J4J_{4}andJ5J_{5}small or negligible. The four-spin ring coupling isJring=0.040J_{\mathrm{ring}}=0.040meV, which is to saynegligible on the scale of the pair exchange:Jring/J2=0.006​(SrFeO2),againstJring/J1=0.25​(La2​CuO4).J_{\mathrm{ring}}/J_{2}=0.006\;\;(\text{SrFeO}_{2}),\qquad\text{against}\qquad J_{\mathrm{ring}}/J_{1}=0.25\;\;(\text{La}_{2}\text{CuO}_{4}).(14)

The contrast is a factor of forty in the coupling constants, though not in the
energies. It isJ​SxJS^{x}, notJJ, that entersEspinE_{\rm spin}: the pair energiesJ​S2JS^{2}are nearly equal in the two materials and the ring energiesJring​S4J_{\mathrm{ring}}S^{4}differ by only a factor of three, as quantified below. The Fe4plaquette is
there, and the sixteen-state construction applies to it verbatim; but a plaquette is anecessarycondition for ring exchange, not a sufficient one. Ring exchange is a
fourth-order process in the transfer integralttbetween neighboring magnetic sites,Jring∝t4/U3J_{\mathrm{ring}}\propto t^{4}/U^{3}withUUthe on-site Coulomb repulsion, whereas the pair
exchange is only of second order,J∝t2/UJ\propto t^{2}/U, so the explanation that first comes
to mind is a weak hybridization. It is not the right one here. The electronegativity
difference with oxygen is nearly the same for Fe as for Cu, and the local moments show
that the covalency is comparable: the integrated Cu moment of La2CuO4is0.70.7–0.8​μB0.8\,\mu_{B}against the nominal1​μB1\,\mu_{B}and the Fe moment of SrFeO2is3.66​μB3.66\,\mu_{B}against44, so that in absolute terms the two ions delocalize a similar
amount of spin onto their ligands,0.20.2–0.3​μB0.3\,\mu_{B}each. The couplings say the same.
The pair-exchange energyJ​S2JS^{2}, which measures the hybridization summed over the
exchange channels of a bond, is nearly equal in the two materials,28.028.0against32.632.6meV, and even the quadrilinear energyJring​S4J_{\mathrm{ring}}S^{4}is suppressed only by a factor
of three,0.650.65against2.042.04meV. Hybridization alone cannot produce a factor of
forty.

The difference lies instead in the orbital structure of the magnetic center, and in the
spin it carries. In La2CuO4the Cu2+ion (d9d^{9},S=1/2S=1/2) holds a single
magnetically active orbital,dx2−y2d_{x^{2}-y^{2}},σ\sigma-bonded to the bridging oxygens: the
entire covalency of the ion is concentrated in the one orbital that circulates, and the
electron travels through the same orbital at every corner of the plaquette, by four
identicalσ\sigma-type steps whose amplitudes add coherently. In the high-spin
Fe2+ion (d6d^{6},S=2S=2) of SrFeO2the configuration is(dz2)2​(dx​z​dy​z)2​(dx​y)1​(dx2−y2)1(d_{z^{2}})^{2}(d_{xz}d_{yz})^{2}(d_{xy})^{1}(d_{x^{2}-y^{2}})^{1}:25,15the
same overall covalency is spread over four magnetic orbitals and inequivalent exchange
channels,dx2−y2d_{x^{2}-y^{2}}through the oxygenpσp_{\sigma}anddx​yd_{xy}throughpπp_{\pi},15and Hund coupling locks any circulating electron to theS=3/2S=3/2core it leaves behind, whereas the Cu electron leaves behind a closed shell,
a core of spin zero, and circulates unconstrained. Pair exchange is indifferent to this dilution, since it
simply sums over the orbital channels of each bond, which is whyJ​S2JS^{2}comes out
nearly the same in the two materials. The cyclic process is not indifferent: it requires
a single electron to complete four coherent hops within one orbital channel around the
loop, and essentially only theσ\sigmachannel qualifies; this is the modest factor of
three by whichJring​S4J_{\mathrm{ring}}S^{4}falls. The remaining factor of sixteen inJring/JJ_{\mathrm{ring}}/Jis the
classical normalization,S2=4S^{2}=4against1/41/4: the coupling constants divide
spin-invariant energies by powers ofSS, so the very quadrilinear energy that yieldsJring=33J_{\mathrm{ring}}=33meV for a spin1/21/2would yield only22meV for a spin22. The two
factors, one electronic and one of pure spin bookkeeping, act in the same direction, and
together they produce the factor of forty.

The ring renormalization of the pair coupling is nevertheless still detectable, and still
in the predicted direction. The four-state calculation on a Néel reference returnsJ2=6.72J_{2}=6.72meV against6.996.99meV from the energy mapping, a deficit of0.270.27meV;
adding the predicted2​Jring​S2=0.322J_{\mathrm{ring}}S^{2}=0.32meV gives7.047.04meV, recovering the mapping
value to0.050.05meV. Inverting the deficit as in Eq. (9) givesJring=0.034J_{\mathrm{ring}}=0.034meV, against0.0400.040meV from the mapping. The correction is
proportionally far smaller here than in the cuprate,4%4\%ofJ2J_{2}rather than12%12\%ofJ1J_{1}, but it acts with the predicted sign and magnitude at a spin value four times
larger.

## Why the SrFeO2mapping is poorer: gap closure, not a missing term.

One caveat must be recorded, and it proves to be the most instructive
single observation of the SrFeO2study. The fit is markedly poorer
than that of the cuprate: RMS=5.4=5.4meV over 22 configurations
[Fig.5(a)], with individual residuals reaching±11\pm 11meV, against8.68.6μ\mueV for La2CuO4. The scatter isnota missing biquadratic term, which is a constant on any
collinear state and therefore cannot produce residuals at all. Its
origin is written plainly in the per-configuration band gaps thatMag4reports alongside every energy (Table4). Six
of the 22 configurations, the fully ferromagnetic one among them, aremetallic, their gap closing entirely, whereas the remaining
sixteen keep gaps of0.220.22to0.830.83eV and La2CuO4stays gapped
throughout, from0.580.58eV for its ferromagnetic configuration to1.891.89eV for the Néel one. The local moments, tellingly, give no such
warning: every SrFeO2configuration retains a well-formed Fe moment,|μ|≈3.66​μB|\mu|\approx 3.66\,\mu_{B}per site, uniform to0.04​μB0.04\,\mu_{B}across the
entire set and unchanged whether the run uses the tetrahedron method or
Gaussian smearing, so that a moment check alone passes all 22. (The
metallic states betray themselves instead in thetotalmagnetization, which is non-integer,31.71​μB31.71\,\mu_{B}for the
ferromagnetic configuration against the nominal3232, as it must be
whenEFE_{F}crosses a band.) It is the
vanishing gap, not a collapsing moment, that marks a configuration as
having left the localized-spin regime that Eq. (1) presumes:
an itinerant magnetic state carries energy in channels that no sum of
pairwise spin products can represent, even while each ion still holds its
spin. The correlation with the fit is then exact. The six metallic
configurations are precisely the six whose residuals exceed±9\pm 9meV,
while all sixteen gapped configurations lie within±2.1\pm 2.1meV, an RMS
of1.41.4meV at the full-fit couplings; refitting on the sixteen gapped
configurations alone collapses the RMS further, to0.500.50meV, a factor
of ten below the full-set value. This confirms directly that the
scatter is a physical signal and not numerical noise, and the refit
validates the couplings themselves: every parameter the gapped subset
can resolve is unchanged while its uncertainty shrinks,J1=1.488±0.021J_{1}=1.488\pm 0.021against1.482±0.1381.482\pm 0.138meV andJ3=−0.196±0.010J_{3}=-0.196\pm 0.010against−0.199±0.044-0.199\pm 0.044meV.

The subset carries a lesson of its own, however. With the six metallic
configurations removed, the fit columns ofJ2J_{2},J4J_{4}andJringJ_{\mathrm{ring}}become exactly collinear (Mag4flags the degeneracy through
infinite variance-inflation factors), so the three can no longer be
separated; only two combinations remain determined, and both agree with
the full fit,(J2−2​J4)​S2=25.2(J_{2}-2J_{4})S^{2}=25.2against25.225.2meV andJ4​S2−Jring​S4=0.74J_{4}S^{2}-J_{\mathrm{ring}}S^{4}=0.74against0.730.73meV. The high-magnetization
configurations, which are exactly the ones that go metallic, are also
exactly the ones that lift this degeneracy. One therefore cannot simply
discard the suspect configurations after the fact and keep the full
coupling model, a configuration-set analogue of the supercell aliasing
discussed below; the SrFeO2paircouplings thus carry a larger
uncertainty than their formal error bars suggest, whileJringJ_{\mathrm{ring}}, whose
column over thefullconfiguration set is orthogonal to every
bilinear one, is protected in the full fit but not resolvable from the
gapped subset alone.

The four-state method fails on the ferromagnetic reference in the same way, and
the diagnostics of Table4say why, turning what would otherwise be an
unexplained outlier into the clearest illustration of the reference-choice argument
developed above. In the original run (3×3×33\times 3\times 3cell,3×3×33\times 3\times 3kk-mesh) the correctedJ2=5.83J_{2}=5.83meV lies1.21.2meV below the
mapping value andJ3=+0.61J_{3}=+0.61meV carries the wrong sign; repeating it at a denser5×5×55\times 5\times 5kk-mesh changes nothing,J2=5.78J_{2}=5.78meV andJ3=+0.70J_{3}=+0.70meV,
because the problem is not one of numerical convergence. All five configurations of
the ferromagnetic-reference set are metallic, while their local Fe moments remain
perfectly healthy at3.593.59–3.69​μB3.69\,\mu_{B}: the reference has crossed the metallic
edge, and every coupling extracted on it is compromised. The symptoms are exactly
the predicted ones. The out-of-planeJ1J_{1}, which belongs to no plaquette and must
therefore be reference-independent, shifts from1.551.55meV (Néel) to2.362.36meV
(FM); and the two-bath formula of Eq. (6), fed with this reference,
returnsJring=(6.10−6.72)/4​S2=−0.04J_{\mathrm{ring}}=(6.10-6.72)/4S^{2}=-0.04meV, wrong even in sign against the+0.04+0.04meV of the mapping. The two-bath route is therefore simply not available in
SrFeO2: it requires a trustworthy ferromagnetic reference, and the material
declines to provide one. The Néel-reference values, by contrast, reproduce the
mappingJ2J_{2}to0.110.11and0.050.05meV, and do so consistently in two supercells
of different shape and size, both built on the2\sqrt{2}in-plane cell, 24 Fe
(2×2×32\times 2\times 3) and 54 Fe (3×3×33\times 3\times 3): every configuration of both sets
is gapped, at0.440.44to0.720.72eV in the larger cell, small but nonzero, which is
again the distinction that matters, and the two cells agree,J1=1.557J_{1}=1.557against1.5541.554,J2=6.774J_{2}=6.774against6.7176.717, andJ3=−0.222J_{3}=-0.222against−0.222-0.222meV.
This is the practical content of the recommendation made with the
diagnostics: in a gap-sensitive material, anchor the local methods on the gapped,
ground-state-like reference.Table 4:Band gap and local-moment diagnostics printed byMag4for every
configuration. (a) Energy-mapping sets: both materials keep well-formed moments
throughout, so the gap is the discriminating quantity. La2CuO4is gapped on all 13 configurations (mapping exact); six of the 22 SrFeO2configurations are metallic and carry all the large residuals, and removing them drops the RMS tenfold. (b) Four-state sets, with the raw (uncorrected) plaquette-edge coupling:J1J_{1}for La2CuO4(2×2×12\times 2\times 1,9×9×59\times 9\times 5),J2J_{2}for SrFeO2(FM:3×3×33\times 3\times 3, 27 Fe,5×5×55\times 5\times 5; Néel:2\sqrt{2}-cell3×3×33\times 3\times 3, 54 Fe,3×3×53\times 3\times 5).aMoments are stable throughout,|μ|≈3.7​μB|\mu|\approx 3.7\,\mu_{B}per Fe and0.70.7–0.8​μB0.8\,\mu_{B}per Cu.(a) Energy-mapping configuration setsMaterialNcfgN_{\rm cfg}# metallicgap range∗(eV)momentsRMS (all→\togapped)La2CuO4(2×2×12\times 2\times 1)1300.578–1.885all passa0.0086 meVSrFeO2(2×2×22\times 2\times 2)2260.220–0.833all passa5.4→\to0.50 meV

∗range over the gapped configurations; the
metallic ones have zero gap.(b) Four-state configuration sets (plaquette-edge coupling, raw)MaterialReferenceNcfgN_{\rm cfg}gap range (eV)momentsJedgeJ_{\rm edge}(meV)La2CuO4FM40.578–0.596all passa146.83La2CuO4Néel40.596–1.885all passa114.19SrFeO2FM5all metallicall passa6.10SrFeO2Néel50.435–0.724all passa6.72Figure 5:Energy mapping for SrFeO2:2×2×22\times 2\times 2supercell,10×10×1010\times 10\times 10kk-mesh, 22 inequivalent collinear configurations, tetrahedron
integration. (a) Model energies against DFT energies, both referred to the lowest
configuration, with the residuals below. The six configurations whose gap closes
(Table4) are drawn in orange, the sixteen insulating ones in blue: the
metallic configurations carry all the large residuals, near±10\pm 10meV where every
insulating configuration lies within±2.1\pm 2.1meV (RMS1.41.4meV for the blue points);
a refit restricted to the sixteen insulating configurations reaches0.500.50meV (see
text). The origin of the poorer SrFeO2fit is thus visible at
a glance: gap closure, not a missing term in the Hamiltonian. (b) The extracted
couplings, with±2​σ\pm 2\sigmaerror bars. The in-plane nearest-neighbor exchangeJ2J_{2}(the plaquette edge) dominates at6.996.99meV; the out-of-planeJ1J_{1}is1.481.48meV;J3J_{3},J4J_{4}andJ5J_{5}are small; and the four-spin ring coupling is negligible on this
scale,Jring=0.040J_{\mathrm{ring}}=0.040meV, i.e.Jring/J2=0.006J_{\mathrm{ring}}/J_{2}=0.006. In La2CuO4the same
ratio is0.250.25. SrFeO2therefore possesses the four-site plaquette but not the ring
exchange it could support, a reminder that a plaquette is necessary forJringJ_{\mathrm{ring}}but
far from sufficient.Table 5:Exchange couplings of SrFeO2(meV),S=2S=2. Four-state values are quoted
before and after the ring correction of Eq. (5). The last column lists the
LDA+U+U(Ueff=4.6U_{\rm eff}=4.6eV) energy-mapping values of Xiang, Wei and
Whangbo,25obtained in the same Hamiltonian convention as
Eq. (1); their shells, labeled in a different order, are mapped onto ours by
distance (theirJ1J_{1},J2J_{2},J3J_{3},J4J_{4}are ourJ2J_{2},J1J_{1},J4J_{4},J3J_{3}), and they
report thatUUvalues between 3 and 6 eV lead to qualitatively the same results.Couplingdd(Å)mapping4-state (Néel)Ref.25J1J_{1}(out-of-plane∥𝐜\parallel\mathbf{c})3.45801.4821.5542.18J2J_{2}(in-plane NN = plaq. edge)3.98506.9896.7177.04J2J_{2}+ ring correction—7.040J3J_{3}(inter-layer diagonal)5.2762−0.199-0.199−0.222-0.222−0.23-0.23J4J_{4}(in-plane NNN = plaq. diag.)5.63560.345—0.43J5J_{5}—−0.004-0.004—JringJ_{\mathrm{ring}}—0.0404—JringJ_{\mathrm{ring}}(sixteen-state)d—0.0526Jring/J2J_{\mathrm{ring}}/J_{2}0.0058fit RMS (meV)5.4

dNéel reference, isolated plaquette in a2\sqrt{2}-cell2×2×22\times 2\times 2supercell (16 Fe); a2×2×12\times 2\times 1cell gives0.0740.074meV, and two of the eight configurations are metallic (see Supporting
Information).

## Code comparison: VASP versus WIEN2k.

All results above use the plane-wave PAW method. To check that they are not an artefact
of the pseudopotential construction, the same couplings were computed with the
all-electron full-potential linearized augmented-plane-wave code
WIEN2k,2at the sameUeffU_{\rm eff}(Table6). There, the muffin-tin radii
were chosen to coincide with the PAW projection radii used for the DFT+U
correction in VASP, so that the on-site term acts on comparable atomic
spheres in both methods. TheUUcorrection nonetheless acts on different radial wavefunctions in the two codes, so
exact agreement is not expected.

For La2CuO4the two codes agree to within a few per cent on every quantity that
can be compared. The nearest-neighbor coupling is130.5130.5meV in VASP (energy mapping)
against132.3132.3–137.0137.0meV in WIEN2k, and the sixteen-stateJringJ_{\mathrm{ring}}on a
ferromagnetic reference is34.534.5meV in VASP against36.436.4meV in WIEN2k, a5%5\%difference. The WIEN2k reproduction of the sixteen-state reference dependence,
and its reading in terms of the loop amplitudes, were presented with
Table3and Eq. (13) above; two further checks belong
here. The ferromagnetic sixteen-state value moves by only0.020.02meV between the
coarse and the dense mesh. And a least-squares fit of the same WIEN2k energies withJringJ_{\mathrm{ring}}included returnsJ1=134.0J_{1}=134.0–134.8134.8meV, bare as the derivation
requires, within3%3\%of the VASP mapping value.

Note that the WIEN2k1×1×21\times 1\times 2cell is one in whichJ1J_{1}carriesnoring term at all, so its
FM and Néel values are uncorrected and ought to coincide; that they differ by4.74.7meV reflects their differentkk-meshes (12×6×612\times 6\times 6against6×3×36\times 3\times 3) rather than any ring physics, and a matched-mesh pair is being
computed. For SrFeO2theJ2J_{2}values from WIEN2k are somewhat smaller than
the VASP ones, but internally consistent between two different supercells, one that
carries no ring correction and one (2×2×32\times 2\times 3) that does; the residual
offset against VASP could reflect the different projection of the on-siteUUin
the two methods.Table 6:Code comparison at matchedUeffU_{\rm eff}. Four-state values are quoted after
the ring correction of Eq. (5); in the WIEN2k1×1×21\times 1\times 2cellsJ1J_{1}(resp.J2J_{2}) carries no ring term, so those entries are uncorrected.CodeSupercell /kk-meshRef.Value (meV)T-La2CuO4,J1J_{1}VASP2×2×12\times 2\times 1/9×9×59\!\times\!9\!\times\!5—130.51 (mapping)VASP2×2×12\times 2\times 1/9×9×59\!\times\!9\!\times\!5Néel130.54WIEN2k1×1×21\times 1\times 2/12×6×612\!\times\!6\!\times\!6FM132.30WIEN2k1×1×21\times 1\times 2/6×3×36\!\times\!3\!\times\!3Néel137.02T-La2CuO4,JringJ_{\mathrm{ring}}(sixteen-state)VASP2\sqrt{2}-cell2×2×12\times 2\times 1/6×6×56\!\times\!6\!\times\!5Néel27.54VASP2\sqrt{2}-cell2×2×12\times 2\times 1/6×6×56\!\times\!6\!\times\!5FM34.52WIEN2ksame cellb/6×5×66\!\times\!5\!\times\!6Néel23.45WIEN2ksame cellb/3×3×33\!\times\!3\!\times\!3FM36.33WIEN2ksame cellb/6×5×66\!\times\!5\!\times\!6FM36.35SrFeO2,J2J_{2}VASP2×2×22\times 2\times 2/10×10×1010\!\times\!10\!\times\!10—6.99 (mapping)VASP2\sqrt{2}-cell2×2×32\times 2\times 3/5×5×55\!\times\!5\!\times\!5Néel7.10VASP2\sqrt{2}-cell3×3×33\times 3\times 3/3×3×53\!\times\!3\!\times\!5Néel7.04VASP3×3×33\times 3\times 3/3×3×33\!\times\!3\!\times\!3FM5.83cVASP3×3×33\times 3\times 3/5×5×55\!\times\!5\!\times\!5FM5.78cVASP2\sqrt{2}-cell2×2×32\times 2\times 3/5×5×55\!\times\!5\!\times\!5FM5.96cWIEN2k2\sqrt{2}-cell2×2×32\times 2\times 3/3×3×33\!\times\!3\!\times\!3Néel6.49WIEN2k2\sqrt{2}-cell1×1×21\times 1\times 2/12×12×1012\!\times\!12\!\times\!10Néel6.59

bthe same sixteen-Cu isolated-plaquette supercell, indexed2×1×22\times 1\times 2in the WIEN2k axis convention;kk-meshes as indexed in that
convention.cunreliable: all configurations of the ferromagnetic
reference are metallic (Table4), and the same runs returnJ3=+0.61J_{3}=+0.61,+0.70+0.70and+0.85+0.85meV against−0.20-0.20meV from every other
calculation; see text.

## Convention.

A caveat is worth stating, since it is a recurrent source of confusion. The
spin-productJringJ_{\mathrm{ring}}of Eq. (1) (and of Moreira\latinet
al.13) differs from the Dirac cyclic-permutation amplitudeJ4J_{4}of the multiple-spin-exchange and neutron-scattering
literature:17,20expanding the permutation operator
generates, besides the four-spin term, two-spin contributions that renormalize the
effective nearest- and next-nearest exchange. Values in the two conventions must be
converted before comparison. Equation (5) is the corresponding statement
at the level of the energy mapping, and Eq. (9) shows it holds
quantitatively.

## 5Conclusions

We have introduced a sixteen-state energy-mapping scheme that isolates the four-spin
ring couplingJringJ_{\mathrm{ring}}from collinear GGA+U+Utotal energies. The alternating sum over the
sixteen collinear arrangements of a nearest-neighbor plaquette cancels the
spin-independent constant, the molecular fields of the bath, and every pair coupling
exactly, for any choice of reference. Symmetry reduces the sixteen configurations to a few inequivalent energies in the magnetic (grey) group: six on the ideal single-layer lattice
and eight in the body-centered stacking of T-La2CuO4; the further degeneracies the spin model predicts, but symmetry does not enforce, are confirmed by the DFT energies to1010μ\mueV.

The derivation also shows that the conventional four-state pair coupling is
ring-renormalized, with a sign set by the reference, and T-La2CuO4bears this out:
three routes resting on different energy differences agree onJring=32.6J_{\mathrm{ring}}=32.6–32.732.7meV
to0.2%0.2\%, givingJring/J1=0.25J_{\mathrm{ring}}/J_{1}=0.25in line with periodic-DFT and experimental
estimates, while a four-stateJ1J_{1}quoted without naming its reference is wrong by12%12\%. The four-spin coupling is moreover remarkably insensitive to truncation of the
bilinear model, whereJ1J_{1}is not, because its four-spin column is orthogonal to every
pair column, the same orthogonality that underlies the extraction.

The direct sixteen-state extraction adds a finding of its own. On an isolated plaquette,
with every diagnostic clean, it still depends on the reference:27.527.5meV on a Néel
bath against34.534.5meV on a ferromagnetic one. A pure pair-plus-ring model forbids this,
and the bilinear couplings stay reference-independent, so the difference is a genuine
fourth-order signature of interactions beyond that model. Turned around, it becomes a measurement: each bath weights each loop family by a
known correlator, so four inequivalent baths separate the bareJring=29.57J_{\mathrm{ring}}=29.57meV from a
series of successively smaller six- and eight-spin loop corrections, and a fifth bath
confirms the parameter-free prediction to1.31.3μ\mueV.

The two test materials answer different questions. La2CuO4shows that the ring term
is large and that ignoring it corruptsJJ; SrFeO2shows the converse, withJring/J2=0.006J_{\mathrm{ring}}/J_{2}=0.006. The contrast in the
couplings overstates the contrast in the physics, since it isJ​SxJS^{x}that enters the
energies: the pair energiesJ​S2JS^{2}are nearly equal (28.028.0against32.632.6meV) and the
ring energiesJring​S4J_{\mathrm{ring}}S^{4}differ only by a factor of three (0.650.65against2.042.04meV),
the rest being the1/Sx1/S^{x}normalization.

Because it requires only collinear single-point energies and a small, symmetry-reduced set
of configurations, the method applies readily to the growing family of two-dimensional and
correlated magnets in which higher-order exchange is suspected. The whole workflow is
implemented in the openly availableMag4package,16so that obtainingJringJ_{\mathrm{ring}}costs no more effort than obtainingJJ.{acknowledgement}

The authors acknowledge Grand équipement national de calcul intensif (GENCI) for granting access to the High-performance computing (HPC) resources of TGCC (Très grand centre de calcul du CEA), CINES (Centre informatique national de l’enseignement supérieur) and IDRIS (Institut du développement et des ressources en informatique scientifique) networks under the allocation 2026-A0190907682.{suppinfo}

The complete derivation, written out step by step and with nothing contracted: the geometry
of the plaquette and of every plaquette touching it, the collinear reduction of the ring
operator, the exact decomposition of the energy, all sixteen energies in full, the
cancellation identities, the extraction formula, the role of time reversal in the symmetry
reduction, and the proof that the four-state method returns the effective coupling rather
than the bare one. This is followed by the derivation worked through for SrFeO2, with
the couplingsJ1J_{1}(out-of-plane),J2J_{2}(in-plane nearest-neighbor),J3J_{3}(inter-layer
diagonal) andJ4J_{4}(in-plane next-nearest-neighbor) classified explicitly, and by the
supercell and convergence checks, and by the full data of the five-bath
decomposition: the bath sign patterns, correlators, gap ranges, measured and modeledJ~ring\tilde{J}_{\mathrm{ring}}, and the total energies of all forty-four configurations.

## References
- T. A. Albright, J. K. Burdett, and M. Whangbo (1985)Orbital interactions in chemistry.Wiley,New York.Cited by:§1.
- P. Blaha, K. Schwarz, F. Tran, R. Laskowski, G. K. H. Madsen, and L. D. Marks (2020)WIEN2k: an APW+lo program for calculating the properties of solids.J. Chem. Phys.152,pp. 074101.External Links:DocumentCited by:§4,§4.
- P. E. Blöchl (1994)Projector augmented-wave method.Phys. Rev. B50,pp. 17953.External Links:DocumentCited by:§3.
- C. J. Calzado and J. Malrieu (2004)Proposal of an extended t-J Hamiltonian for high-TcT_{c}cuprates from ab initio calculations on embedded clusters.Phys. Rev. B69,pp. 094435.External Links:DocumentCited by:§1,§2.6.
- R. Coldea, S. M. Hayden, G. Aeppli, T. G. Perring, C. D. Frost, T. E. Mason, S.-W. Cheong, and Z. Fisk (2001)Spin waves and electronic interactions in La2CuO4.Phys. Rev. Lett.86,pp. 5377.External Links:DocumentCited by:§4,§4,Table 1,Table 1,Table 1.
- D. Dai and M. Whangbo (2001)Spin exchange interactions of a spin dimer: analysis of broken-symmetry spin states in terms of the eigenstates of Heisenberg and Ising spin Hamiltonians.J. Chem. Phys.114,pp. 2887.External Links:DocumentCited by:§1.
- S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton (1998)Electron-energy-loss spectra and the structural stability of nickel oxide: an LSDA+U study.Phys. Rev. B57,pp. 1505.External Links:DocumentCited by:§3.
- N. S. Fedorova, A. Bortis, C. Findler, and N. A. Spaldin (2018)Four-spin ring interaction as a source of unconventional magnetic orders in orthorhombic perovskite manganites.Phys. Rev. B98,pp. 235113.External Links:DocumentCited by:§1,§2.1,§4.
- N. S. Fedorova, C. Ederer, N. A. Spaldin, and A. Scaramucci (2015)Biquadratic and ring exchange interactions in orthorhombic perovskite manganites.Phys. Rev. B91,pp. 165122.External Links:DocumentCited by:§1,§2.1.
- G. Kresse and J. Furthmüller (1996)Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set.Phys. Rev. B54,pp. 11169.External Links:DocumentCited by:§3.
- A. H. MacDonald, S. M. Girvin, and D. Yoshioka (1988)t/Ut/Uexpansion for the Hubbard model.Phys. Rev. B37,pp. 9753.External Links:DocumentCited by:§1,Figure 2,Figure 2,§4.
- Y. Mizuno, T. Tohyama, and S. Maekawa (1998)Electronic states and magnetic properties of edge-sharing Cu-O chains.Phys. Rev. B58,pp. R14713.External Links:DocumentCited by:§4.
- I. d. P. R. Moreira, C. J. Calzado, J. Malrieu, and F. Illas (2006)First-principles periodic calculation of four-body spin terms in high-TcT_{c}cuprate superconductors.Phys. Rev. Lett.97,pp. 087003.External Links:DocumentCited by:§1,§2.6,§4,§4,§4,Table 1,Table 1,Table 1.
- J. P. Perdew, K. Burke, and M. Ernzerhof (1996)Generalized gradient approximation made simple.Phys. Rev. Lett.77,pp. 3865.External Links:DocumentCited by:§3.
- M. Rahman, Y. Nie, and G. Guo (2013)Electronic structures and magnetism of SrFeO2under pressure: a first-principles study.Inorg. Chem.52,pp. 12529.External Links:DocumentCited by:§4,§4.
- X. Rocquefelte (2026)MAG4: a Python suite for the extraction of magnetic exchange parameters by energy mapping and by the four- and sixteen-state methods.Note:https://gitlab.com/xrocquef/mag4Full description to be published separatelyCited by:§3.1,§3.1,§5.
- M. Roger, J. H. Hetherington, and J. M. Delrieu (1983)Magnetism in solid3He.Rev. Mod. Phys.55,pp. 1.External Links:DocumentCited by:§4.
- D. Šabani, C. Bacaksiz, and M. V. Milošević (2020)Ab initio methodology for magnetic exchange parameters: generic four-state energy mapping onto a Heisenberg spin Hamiltonian.Phys. Rev. B102,pp. 014457.External Links:DocumentCited by:§1,§2.2.
- M. Takahashi (1977)Half-filled Hubbard model at low temperature.J. Phys. C: Solid State Phys.10,pp. 1289.External Links:DocumentCited by:§1,Figure 2,Figure 2,§4.
- A. M. Toader, J. P. Goff, M. Roger, N. Shannon, J. R. Stewart, and M. Enderle (2005)Spin correlations in the paramagnetic phase and ring exchange in La2CuO4.Phys. Rev. Lett.94,pp. 197202.External Links:DocumentCited by:§1,§1,§2.4,§4,§4.
- Y. Tsujimoto, C. Tassel, N. Hayashi, T. Watanabe, H. Kageyama, K. Yoshimura, M. Takano, M. Ceretti, C. Ritter, and W. Paulus (2007)Infinite-layer iron oxide with a square-planar coordination.Nature450,pp. 1062.External Links:DocumentCited by:Figure 1,Figure 1,§1,§3.
- M. Whangbo and R. Hoffmann (1978)The band structure of the tetracyanoplatinate chain.J. Am. Chem. Soc.100,pp. 6093.External Links:DocumentCited by:§1.
- M. Whangbo, H. Koo, and D. Dai (2003)Spin exchange interactions and magnetic structures of extended magnetic solids with localized spins: theoretical descriptions on formal, quantitative and qualitative levels.J. Solid State Chem.176,pp. 417.External Links:DocumentCited by:§1.
- H. J. Xiang, E. J. Kan, S. Wei, M.-H. Whangbo, and X. G. Gong (2011)Predicting the spin-lattice order of frustrated systems from first principles.Phys. Rev. B84,pp. 224429.External Links:DocumentCited by:§1,§2.2,§2.2.
- H. J. Xiang, S. Wei, and M.-H. Whangbo (2008)Origin of the structural and magnetic anomalies of the layered compound SrFeO2: a density functional investigation.Phys. Rev. Lett.100,pp. 167207.External Links:DocumentCited by:§4,§4,Table 5,Table 5,Table 5.
- H. Xiang, C. Lee, H.-J. Koo, X. Gong, and M.-H. Whangbo (2013)Magnetic properties and energy-mapping analysis.Dalton Trans.42,pp. 823.External Links:DocumentCited by:§1.

## 


- 


Major funding support from
