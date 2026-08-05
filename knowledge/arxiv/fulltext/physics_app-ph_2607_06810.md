# Soft cells, Tubular Tilings and the Hidden Phases in Binary Mixtures

**arXiv ID**: 2607.06810v1
**Authors**: Gábor Domokos
**Published**: 2026-07-07
**Categories**: physics.app-ph, math.GT, math.MG
**Comments**: 25 pages, 8 figures
**HTML URL**: https://arxiv.org/html/2607.06810v1

## Abstract

Biological and physical systems ranging from Fermi surfaces and skeletal structures to reaction--diffusion patterns and cosmological models may be viewed as binary mixtures in which a smooth interface separates two complementary phases. While the interface is often directly observable, the topology of one of the phases may remain hidden. To study such systems, we introduce tubular tilings, a geometric framework for discretizing binary mixtures on smooth manifolds of arbitrary dimension and topology. We prove that tubular tilings satisfy global Euler balance laws relating the topology of the ambient manifold, the discretized phases, and their interfaces. These balance laws provide a practical inference principle: topological information about a hidden phase can be recovered from the observable phase and the geometry of the separating interface. We further show that, in dimensions $d>2$, tubular tilings form a subclass of soft tilings, the recently discovered class of corner-free tessellations. Applications to Fermi surfaces and cosmological shell decompositions illustrate how the theory can be used to extract otherwise inaccessible topological information about complex geometric structures.

## Full Text

Soft cells, Tubular Tilings and the Hidden Phases in Binary Mixtures

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.06810v1 [physics.app-ph] 07 Jul 2026

## Soft cells, Tubular Tilings and the Hidden Phases in Binary MixturesGábor DomokosGábor Domokos, HUN-REN-BME Morphodynamics Research Group and Dept. of Morphology and Geometric Modeling, Budapest University of Technology,
Műegyetem rakpart 1-3., Budapest, Hungary, 1111domokos@iit.bme.hu

## Abstract.

Biological and physical systems ranging from Fermi surfaces and skeletal structures to reaction–diffusion patterns and cosmological models may be viewed as binary mixtures in which a smooth interface separates two complementary phases. While the interface is often directly observable, the topology of one of the phases may remain hidden. To study such systems, we introduce tubular tilings, a geometric framework for discretizing binary mixtures on smooth manifolds of arbitrary dimension and topology. We prove that tubular tilings satisfy global Euler balance laws relating the topology of the ambient manifold, the discretized phases, and their interfaces. These balance laws provide a practical inference principle: topological information about a hidden phase can be recovered from the observable phase and the geometry of the separating interface. We further show that, in dimensionsd>2d>2, tubular tilings form a subclass of soft tilings, the recently discovered class of corner-free tessellations. Applications to Fermi surfaces and cosmological shell decompositions illustrate how the theory can be used to extract otherwise inaccessible topological information about complex geometric structures.

## Key words and phrases:Binary mixture, tessellation, triply periodic minimal surface, soft cell

## 1991 Mathematics Subject Classification:00A69, 52C22, 05B45, 54H99

## 1.Introduction

Tilings of space are among the most striking geometric patterns in nature and art.
In mathematical language, they are coverings of a smooth, boundaryless manifoldMdM^{d}by compact sets (tiles) without gaps or overlaps.
Beyond their role as models of physical and biological structures, tilings also provide an intuitive bridge between continuous space and discrete description.

Many natural systems may be interpreted as binary mixtures: the ambient manifold is partitioned into two complementary phases separated by a smooth interface. Examples range from biological tissues and porous materials to reaction–diffusion patterns, triply periodic minimal surfaces (TPMS) and cosmological decompositions of space. In many applications the separating interface is directly observed, whereas only one of the two complementary phases is naturally interpreted as the physical object. Throughout the paper we refer to the other complementary phase as the hidden phase, although the interface determines both complementary phases equally. While the interface itself is often the primary object of study, many applications require a finite geometric representation of the two phases. A prominent example is provided by TPMS, whose complementary labyrinths admit natural discretizations into unit cells. This motivates the search for natural discretizations of binary mixtures.

In this paper we introduce such discretizations, which we call tubular tilings, and derive topological balance laws governing their structure. These balance laws allow the topology of the hidden phase to be inferred from the observed phase together with the geometry of the separating interface. The resulting framework connects smooth interfaces, soft tilings and topological invariants of discretized binary mixtures.

## 1.1.Tubular tilings

The motivation for tubular tilings originates from the observation that many binary mixtures naturally admit finite geometric representations. Discretizations analogous to TPMS structures appear in cellular materials, porous media, biological tissues and reaction–diffusion systems.
To capture these structures in a unified setting, we introducetubular tilings.

Informally, one starts with a tiling𝒯\mathcal{T}and assigns each tile one of two labels,AAorBB, producing two complementary spatial components.
Interfaces shared by tiles within the same component form theinternal interfaceof a tile, whereas interfaces shared with tiles of the opposite component form itsexternal interface.

A tiling is calledtubularif there exists a smooth embedded hypersurfaceTTsuch that the external interfaces collectively tileTT(tiling condition), while the internal interfaces of tiles remain disjoint unions of faces (tubularity condition).
In this case, we callTTatubular (hyper)surface.
A rigorous definition is given in AppendixA(Definition1).

Figure1illustrates the concept. Figure1(a) shows the frontal view of a brick wall interpreted as a tubular tiling, while Figure1(b) shows the analogous construction for the Schwarz D surface. Although geometrically very different, both examples share the same topological structure: a smooth interface separating two complementary phases whose discretization defines a tubular tiling.Figure 1.Tubular tilings: basic concepts. (a1) Frontal view of brick wall laid in bond. Tubular domainsAAandBBcorrespond to alternating layers. Tubular surfaceTTis the union of horizontal lines separating layers. Tubular tiles are rectangular views of bricks. (a2) External (A/BA/B) and internal (A/AA/A,B/BB/B) interfaces on brick wall. (b1) Schwarz D surface interpreted as tubular tiling. Tubular surface (grey),AAandBBtiles indicated by green and blue semi-transparent interiors. (b2) External (A/BA/B) interfaces (grey) and internal interfaces (A/AA/Agreen,B/BB/Bblue) on tubular tiles of the Schwarz D surface.

Tubular tilings occur naturally in a wide range of systems. Examples on two-dimensional manifolds are shown in Figure2, while Figure3illustrates examples in three dimensions, including cellular structures, reaction–diffusion patterns, porous materials and cosmological decompositions.Figure 2.Examples of tubular tilings on two dimensional manifolds. (a)Md=T2M^{d}=T^{2}(flat torus): the honeycomb andMd=S1×𝕀1M^{d}=S^{1}\times\mathbb{I}^{1}(periodic cylinder): cactus skeleton (b)Md=S2M^{d}=S^{2}(sphere): pollen. (c)Md=T2M^{d}=T^{2}(non-flat torus): Turing patterns computed on a torus.Figure 3.Examples of tubular tilings on three dimensional manifolds. (a)Md=T3M^{d}=T^{3}(flat torus): (a1) metal foam (a2) tafoni rock (b)Md=S3M^{d}=S^{3}(b1) Thick shell decomposition of the Robertson-Walker universe. Tubular surface is the union of planetary surfaces. (c)Md=R3M^{d}=R^{3}(Euclidean space): (c1) butterfly wing/gyroid structure (c2) diblock copolymer (c3) human bone structure

The same geometric structure that underlies tubular tilings also endows them with remarkable regularity properties, making it possible to derive global Euler balance laws and relate them to soft tilings.

## 1.2.The main result

Tubular tilings provide a framework for studying the topology of discretized binary mixtures on smooth, boundaryless manifolds of finite topological type.
Under the tiling and tubularity conditions, the topology of the ambient manifold constrains the topology of the discretization.

Our main result, proved in AppendixB, is an Euler-type balance law relating the topology of tubular cells, their internal interfaces and the ambient manifold.

## Theorem 1.

LetMdM^{d}be a smoothdd–manifold without boundary and of finite
topological type and let𝒯\mathcal{T}be a tubular tiling ofMdM^{d},
consisting ofAA–tiles andBB–tiless.

Assume that the average Euler characteristicsχ𝐀,χ𝐁\chi_{\mathbf{A}},\chi_{\mathbf{B}}of theAA– andBB–tiles,
respectively, and the average Euler characteristicsχA¯,χB¯\chi_{\bar{A}},\chi_{\bar{B}}of their corresponding internal
interfaces exist. LetNNdenote the total number of tiles and assume that
the respective relative frequenciespA,pBp_{A},p_{B}ofAA– andBB–tiles also exist.
Then(1)pA​(2​χ𝐀−χA¯)+(−1)d​pB​(2​χ𝐁−χB¯)=χ​(Md)N​((−1)d+1).p_{A}(2\chi_{\mathbf{A}}-\chi_{\bar{A}})+(-1)^{d}p_{B}(2\chi_{\mathbf{B}}-\chi_{\bar{B}})=\frac{\chi(M^{d})}{N}\bigl((-1)^{d}+1\bigr).

We immediately observe that the right-hand side of (1) vanishes whenever eitherMdM^{d}is noncompact (in which caseNNis infinite) orddis odd.
In these cases the balance law reduces to a homogeneous relation.

Theorem1also recovers balance relations for classical convex mosaics as a special case.
In particular, for a normal, balanced convex tiling ofℝ3\mathbb{R}^{3}, letFFandVVdenote the average numbers of faces and vertices of cells, and letffandvvdenote the corresponding quantities for vertex polyhedra.
We prove (Corollary1in Section2) thatV​(2−v)−f​(2−F)=0.V(2-v)-f(2-F)=0.

Beyond its geometric consequences, Theorem1provides a topological tool for studying binary mixtures through their discretizations.
In many physical systems one phase is directly observable, whereas the complementary phase is accessible only indirectly or incompletely. We will call the related
tubular tiling in which one phase is observable and the complementary phase is hidden asemi-hiddentubular tiling.
The theorem enables one to infer topological information
about a hidden phase from
geometric data associated with the observable phase and
their common interface.

## 1.3.Relation to soft tilings

The concept of tubular tilings grew out of the theory ofsoft tilingsintroduced in[1]. Soft tilings
were originally motivated by the study of space-filling structures
with a minimal number of sharp corners and by geometric models of
natural forms such as the chambered shell of the Nautilus[1,2], biological tissues[3]and corals[4].
The Edge Bending (EB) algorithm of[1,5]generates such
tilings from convex mosaics, while its extension in[6]revealed a broader family of soft cells, including the unit cells of
classical TPMS (Figure4).Figure 4.Soft cells. First row: soft cells obtained by the edge bending (EB) algorithm. (a) The f2 soft cell obtained from the truncated octahedron. (b) Soft cell withZ2×Z2×Z2Z_{2}\times Z_{2}\times Z_{2}symmetry, obtained from the cube. (c) Soft cell withZ2×Z2Z_{2}\times Z_{2}symmetry, obtained from the cube. Second row: soft cells associated with classical triply periodic minimal surfaces (TPMS). (d) Schwarz P unit cell. (e) Schwarz D unit cell. (f) Gyroid unit cell.

We show (AppendixA,
Proposition2) that tubular tilings possess strong
regularity properties. In particular, whend>2d>2they contain no
sharp corners and therefore belong to the class of soft tilings.
From this perspective, softness emerges naturally from the topology
of discretized binary mixtures rather than solely from local
geometric constraints.

To compare tubular tilings with earlier constructions, we adopt a
generalized notion of softness (AppendixA,
Definition2). A tile is calledkk-soft if the
highest codimension of its smooth boundary strata iskk. This
definition admits multiply connected tiles, extends naturally to
arbitrary dimensions and, in dimension three, identifies
corner-free tilings with 2-soft tilings.

## 1.4.Strategy of proof

In AppendixAwe give the formal definitions of tubular tilings and soft cells, while AppendixBcontains the proof of Theorem1.
Below we motivate both the definitions and the strategy of the proof.

Tubular tilings may be introduced in two complementary ways: either by first defining a tubular surface and subsequently introducing a discretization, or conversely by associating a smooth surface with an existing tiling.
In the Introduction we followed the latter approach, and in AppendixAwe give a formal definition (Definition1) in the same spirit.

In the proof, rather than refining tubular tilings into CW complexes, we work directly with their natural geometric structure using inclusion–exclusion for Euler characteristic.

Convex tilings by polyhedral cells naturally define CW complexes, and their topology is captured by the Euler–Poincaré formula(2)χ​(Md)=∑k=0d(−1)k​ck,\chi(M^{d})=\sum_{k=0}^{d}(-1)^{k}c_{k},

which computes the Euler characteristic of the ambient manifold as an alternating sum of the numbers ofkk–cells.

Tubular tilings, however, are not naturally CW complexes. A tubular tile is a compactdd–manifold with piecewise smooth boundary whose geometric structure consists of(d−1)(d-1)–dimensional strata (the internal interface, given by disjoint cross-sectional manifolds, and the external interface, consisting of disjoint smooth tubular patches) together with(d−2)(d-2)–dimensional strata (their smooth boundaries). Such cells generally have nontrivial topology, and their Euler characteristic is not determined solely by dimension. Converting this geometric decomposition into a CW complex would require introducing numerous auxiliary strata and subdividing the geometric cells into contractible pieces.

While such a refinement would make the Euler–Poincaré formula (2) formally applicable, it has two disadvantages for the present purposes. First, it introduces substantial auxiliary combinatorial detail unrelated to the intrinsic geometric structure of tubular cells. Second, it obscures essential geometric information by replacing multiply connected geometric cells with collections of disks. In particular, adjacency relations and disk valencies, which play a central role in the balance laws, are not naturally encoded at the CW level without additional bookkeeping.

For this reason, the Euler balance laws are formulated directly at the level of the natural geometric strata of the tiling using inclusion–exclusion[7]:(3)χ​(X∪Y)=χ​(X)+χ​(Y)−χ​(X∩Y).\chi(X\cup Y)=\chi(X)+\chi(Y)-\chi(X\cap Y).

Conceptually, this may be viewed as a geometry-adapted compression of the full CW Euler bookkeeping: auxiliary strata are suppressed, while the gluing relations between tubular cells and separating disks are kept explicit.

## 2.Geometric constructions and physical applications

Theorem1establishes a topological balance law between the two phases of a tubular tiling, and in the Introduction we presented several geometric examples. However, neither the theorem nor the examples provide analgorithmfor constructing tubular tilings.

As noted in the Introduction, TPMS such as the Gyroid and the SchwarzPPandDDsurfaces (see Figure1(b1)) provide examples of binary mixtures, the natural discretizations of which are tubular tilings where
the complementary domainsAAandBBcan be deformation retracted on two skeletal graphsGA,GBG_{A},G_{B}. Here we follow the opposite path: we assume that the skeletal graphGAG_{A}for phaseAA(the observable phase
) is given, and we provide an algorithm to construct the corresponding tubular surfaceTTand the tubular tiling𝒯\mathcal{T}which also includes the hidden phaseBB. We describe two examples, both related tod=3d=3dimensional ambient manifoldsMdM^{d}.

First we consider the case whenMd=ℝ3M^{d}=\mathbb{R}^{3}and the skeletal graphGAG_{A}is a polyhedral skeleton. Here we introduce thefrozen wire algorithmand illustrate it on the example
of the Fermi surface of Copper. Next we consider the case whenMd=S3M^{d}=S^{3}and the skeletal graphGAG_{A}degenerates to a discrete set of isolated vertices. Here we introduce thedouble bubble algorithmand illustrate it on the thick shell decomposition of the positively curved Robertson-Walker universe model.

## 2.1.The Fermi surface of Copper: soft cells on sub-atomic scale

## 2.1.1.Polyhedral skeleta and the frozen wire algorithm

In our first example we consider the case where the skeletal graphGAG_{A}of the observable phase is given as a polyhedral skeleton. To establish the tiling for theBB-phase, we first prove a simple corollary concerning polyhedral tilings.

## Corollary 1.

Letℳ\mathcal{M}be a normal, balanced convex tiling inℝ3\mathbb{R}^{3}[8], withF,V,f,vF,V,f,vdenoting the respective average numbers of faces of tiles, vertices of tiles, faces of vertex polyhedra, and vertices of vertex polyhedra. Then(4)V​(2−v)−f​(2−F)=0.V(2-v)-f(2-F)=0.

## Proof.

LetE​(ℳ)E(\mathcal{M})denote the edge skeleton ofℳ\mathcal{M}. For sufficiently small tube radius, a tubular neighbourhood ofE​(ℳ)E(\mathcal{M})defines a smooth embedded surfaceTTseparatingℝ3\mathbb{R}^{3}into two phases. We call this construction thefrozen wire algorithm.

The resulting tubular tiling has oneAA–cell associated with each vertex ofℳ\mathcal{M}and oneBB–cell inside each polyhedral cell ofℳ\mathcal{M}. Since both cell types are simply connected,(5)χ𝐀=χ𝐁=1.\chi_{\mathbf{A}}=\chi_{\mathbf{B}}=1.

The internal interfaces of anAA–cell correspond to the vertices of the vertex polyhedron, while the internal interfaces of aBB–cell correspond to the faces of the original polyhedron. Hence(6)χA¯=v,χB¯=F.\chi_{\bar{A}}=v,\qquad\chi_{\bar{B}}=F.

IfNCN_{C}andNVN_{V}denote the numbers of cells and vertices ofℳ\mathcal{M}, respectively, then double counting cell–vertex incidences yieldsNV​f=NC​V.N_{V}f=N_{C}V.

Therefore(7)pApB=Vf.\frac{p_{A}}{p_{B}}=\frac{V}{f}.

SinceMd=ℝ3M^{d}=\mathbb{R}^{3}, Theorem1has vanishing right-hand side.
Dividing (1) bypBp_{B}and substituting (5)-(7) we get
a formula equivalent to (4).
∎Figure 5.Tubular soft tilings constructed on polyhedral skeletons. (a) The cubic grid: (a1) tiling (a2)AA-cell (a3)BB-cell (b) The hexagonal prismatic grid: (b1) tiling (b2)AA-cell (b3)BB-cell

## Remark 1.

Letℳ\mathcal{M}be a polyhedral tiling ofℝ3\mathbb{R}^{3}and letE​(ℳ)E(\mathcal{M})denote its edge skeleton. We call a graphE¯\bar{E}asuperpolyhedral gridif it has the same nodal set asE​(ℳ)E(\mathcal{M})and may contain additional straight edges.
If a smooth embedded surfaceT⊂ℝ3T\subset\mathbb{R}^{3}satisfiesT∩E¯=∅,T\cap\bar{E}=\emptyset,

thenTTalso avoidsE​(ℳ)E(\mathcal{M})and therefore defines a tubular surface associated with the tubular tiling obtained from the frozen wire algorithm applied toE​(ℳ)E(\mathcal{M}).

## 2.1.2.Geometry of Fermi surfaces

A crystalline solid determines a lattice in physical space and an associated reciprocal lattice in momentum space. Physically, reciprocal space is considered modulo reciprocal lattice translations, yielding the Brillouin zone, which is topologically a three-dimensional torus. The Fermi surface is the level surface separating occupied and unoccupied electron states.

For the present topological computation it is more convenient to work with the equivalent triply periodic representation inℝ3\mathbb{R}^{3}. Geometrically, the Fermi surface defines a binary decomposition of reciprocal space into two complementary phases separated by a smooth embedded surface. Since only one phase (the occupied phase) is directly observable in many experiments, Fermi surfaces provide natural examples of semi-hidden tubular tilings.Figure 6.The Fermi surface of copper and the associated tubular tiling. (a) Fermi surface of copper (grey surface) with internal interfaces for the occupied, observableAA-phase (green disks), internal interfaces for the
non-occupied, hiddenBB-phase (blue disks) and theBDB_{D}superpolyhedral skeleton (green lines). Observe that theAA-phase avoids theBDB_{D}skeleton. (b1) The soft unit cell of the occupied, observableAA-phase, illustrated inside the truncated octahedron cell. (b2) The soft unit cell with torus topology of the non-occupied, hiddenBB-phase, illustrated inside the rhombohedron.

## 2.1.3.The Fermi surface of copper

LetBDB_{D}denote the union of the diagonal edges of the BCC lattice. These edges form a superpolyhedral grid since they coincide with the union of the edge skeletons of the two rhombohedral tilings associated with the BCC lattice.

The Brillouin zone of copper is a truncated octahedron. Its Fermi surface is approximately spherical but develops eight necks passing through the centres of the hexagonal faces. Consequently, the Fermi surface avoids the diagonal BCC gridBDB_{D}and intersects each hexagonal face in a simply connected patch.

We call the occupied phase theAA–phase. Since the occupied region inside a truncated octahedron is simply connected,(8)χ𝐀=1.\chi_{\mathbf{A}}=1.

The internal interface of anAA–cell consists of eight disjoint discs, one on each hexagonal face, hence(9)χA¯=8.\chi_{\bar{A}}=8.

To construct the complementaryBB–cells we choose one of the rhombohedral tilings contained inBDB_{D}and apply the frozen wire algorithm. Since a rhombohedron has six faces, the internal interface of aBB–cell consists of six disjoint discs, yielding(10)χB¯=6.\chi_{\bar{B}}=6.

Both the truncated octahedron and the rhombohedron tilesℝ3\mathbb{R}^{3}without gaps and overlaps and both are associated with the BCC lattice.
If the edge length of the cube is taken as unit, both cells have volume1/21/2, so they occur with equal asymptotic frequency, so(11)pA=pB.p_{A}=p_{B}.

Since the ambient manifold isMd=ℝ3M^{d}=\mathbb{R}^{3}, Theorem1has vanishing right-hand side. Substituting (8)–(11) into (1) yields(12)χ𝐁=0.\chi_{\mathbf{B}}=0.

This is illustrated in Figure6(b1) where we can see theBB-cell with torus topology.
As we can see, the topology of the hiddenBB-phase can be inferred directly from
the topology of the observable phase together with geometric information,
namely the relative volumes of the corresponding cells. Although the Fermi surface determines both complementary regions equally,
physical intuition naturally singles out the occupied region. The Euler balance theorem restores this symmetry by allowing the
topology of the complementary region to be inferred from the observed interface.

In the next
example we consider a different ambient manifold and a very different
physical setting; nevertheless, the argument follows a similar pattern,
combining topological and geometric information to recover properties of
the hidden phase.

## 2.2.The Robertson-Walker universe: soft cells and cosmic shells

In the forthcoming example we regard the case where the skeletal graphGAG_{A}of the observable phase has no edges and is thus reduced to a finite point set.
First, in Corollary2we show that in theMd=S3M^{d}=S^{3}ambient space, by using two finite sets of embeddedS2S^{2}spheres (’double bubbles’), a broad range of soft tilings can be constructed
for this special skeletal graph.
Then we use the double bubble algorithm to construct a soft tiling for the positively curved Robertson-Walker model of the universe where we regard the union of the planets as the observableAA-phase and use the corollary to construct the soft tiling of theBB-phase which corresponds to a thick shell decomposition.

## 2.2.1.Degenerate skeleta and the double bubble algorithm

## Corollary 2.

LetMd=S3M^{d}=S^{3}and letFnA⊂S3F^{A}_{n}\subset S^{3}be the union ofn>1n>1pairwise disjoint, embeddedS2S^{2}spheres.
Then, for arbitraryq<nq<nthere exist two soft
tubular tilings, both withT=FnAT=F^{A}_{n}as tubular surface andχ𝐀=1\chi_{\mathbf{A}}=1, and
- (1)

one tiling withχ𝐁>q\chi_{\mathbf{B}}>qand
- (2)

another tiling withχ𝐁<q\chi_{\mathbf{B}}<q.

## Proof.

The surfaceFnAF^{A}_{n}decomposesS3S^{3}inton+1n+1connected components,nnof which are 3-balls
bounded by thennspheres. We
identify theAA-tiles with these balls and so we can write:(13)χ𝐀=1,χA¯=0,\chi_{\mathbf{A}}=1,\quad\chi_{\bar{A}}=0,

and for brevity we will refer to theS2S^{2}spheres inFnAF^{A}_{n}asAA-spheres.
To construct the tiling of theBB-phase we introduceFmBF^{B}_{m}as a set ofmmpairwise disjoint, embeddedS2S^{2}spheres inS3S^{3}to which we refer as theBBspheres.
We assume that if the intersectionFnA∩FmBF^{A}_{n}\cap F^{B}_{m}is not empty then it is transversal and consists ofNNdisjoint copies ofS1S^{1}, to which we refer asCC-circles.
The transversality assumptions guarantee that the induced decomposition satisfies the tubularity conditions. Indeed, every point of aCC-circle is incident to exactly two external interface patches and one internal interface patch, so the triple-junction condition is satisfied.

We note that form>0m>0,NNmay be regarded as an arbitrary nonnegative integer.
Indeed, by introducing sufficiently small local wiggles on theBB-spheres, one may realize any prescribed finite number of transverseCC-circles with the fixed familyFnAF_{n}^{A}.
While the surfacesFnAF^{A}_{n}andFmBF^{B}_{m}always define a tubular tiling, and their definition is analogous, they play entirely different roles in the
tubular tiling. The union ofAA-spheres is the tubular surfaceTTand eachAA-sphere is the entire external interface
of anAA-tile and (possibly part of) the external interface of aBB-tile. On the other hand, aBBsphere
is (possibly part of) the internal interface of aBB-tile but it is never part of an external interface.

Let us write the Euler characteristic for the internal interface∂¯​Bi\bar{\partial}B_{i}of theiithBB-tile.
Since theBB-spheres are disjoint, the interface contains an integer number of spheres which we denote bybib_{i}.
We denote the number ofCC-circles on the boundary bycic_{i}and since each boundary circle decreases the Euler characteristic by one, inclusion-exclusion yields(14)χ​(∂¯​Bi)=2​bi−ci,i=1,…,m+1.\chi(\bar{\partial}B_{i})=2b_{i}-c_{i},\qquad i=1,\dots,m+1.

Our next goal is to rewrite (14) for the respective averages which we denote bybbandcc. Since there arem+1m+1BB-tiles, we getb=1m+1​∑ibi,c=1m+1​∑ici.b=\frac{1}{m+1}\sum_{i}b_{i},\quad c=\frac{1}{m+1}\sum_{i}c_{i}.

EachBB-sphere belongs to the internal interfaces of exactly twoBB-tiles. Hence∑ibi=2​m.\sum_{i}b_{i}=2m.

Likewise, eachCC-circle belongs to the boundaries of exactly two
internal interfaces, so∑ici=2​N.\sum_{i}c_{i}=2N.

Henceb=2​mm+1,c=2​Nm+1=b​k,b=\frac{2m}{m+1},\qquad c=\frac{2N}{m+1}=bk,

wherek=N/mk=N/mis the average number ofCC-circles perBB-sphere.
Averaging (14) therefore yields(15)χB¯=2​b−c=2​mm+1​(2−k).\chi_{\bar{B}}=2b-c=\frac{2m}{m+1}(2-k).

The relative frequencies for the two phases arepA=nn+m+1,pB=m+1n+m+1.p_{A}=\frac{n}{n+m+1},\qquad p_{B}=\frac{m+1}{n+m+1}.

Now we can substitute into (1). Sinceχ​(S3)=0\chi(S^{3})=0, the right hand side is zero and we obtain:(16)χ𝐁=2​m−N+nm+1.\chi_{\mathbf{B}}=\frac{2m-N+n}{m+1}.

Form=N=0m=N=0we obtainχ𝐁=n\chi_{\mathbf{B}}=n, proving the existence of the first tiling in Corollary2.
Next we fixnnandmm. Then, sinceNNmay be arbitrarily large, the right-hand side of (16) can be made smaller thanqq, proving the second claim.
∎Figure 7.Thick shell decomposition of theS3S^{3}Robertson-Walker universe interpreted as a soft tubular tiling. (a) Schematic cross section. Observer located at centerCC. Solid line (union of circles with radiirir_{i},i=1,2,…​ni=1,2,\dots n,nnbeing the number of planets) corresponds to smooth tubular surfaceTTwhich is the union ofnndisjoint copies ofS2S^{2}spheres. DomainAAis the interior of planets, filled with grey. Each planet is one soft tileAiA_{i},i=1,2,…​ni=1,2,\dots n. Dotted line (union of circles with radiiRj=j​R0R_{j}=jR_{0},j=1,2,…​mj=1,2,\dots m) corresponds to the internal interfaces betweenBB-tiles, each of which is a spherical shell with thicknessR0R_{0}. One thick shell filled with light grey. (b) 3D visualization of the double bubble construction for theS3S^{3}RW universe. Tubular surface (external interface) appears as a collection of small grey spheres. Internal interface ofBBtiles appears as large, concentric blue spheres. TheAA-phase is the interior ofAA-tiles (planets), shown in green. Observe that despite transversal intersection, all boundary strata are smooth and no sharp corners arise, hence the tiling is soft.

## 2.2.2.The RW universe and its radial shell decomposition

The Robertson–Walker (RW) model of the Universe[9,10]assumes spatial slices of constant
curvature. Depending on the sign of the curvature, the corresponding
spatial geometry is modeled onS3S^{3},ℝ3\mathbb{R}^{3}(or compact
quotients such asT3T^{3}), orH3H^{3}.
Here we discuss the positively curvedS3S^{3}case.
We assume that theS3S^{3}RW universe is decomposed into a finite set of concentric thick spherical
shells with centerCC. This radial shell decomposition underlies many standard constructions
in cosmology, such as radial binning in galaxy surveys[11,12],
tomographic analysis of large–scale structure[13], and harmonic
decompositions based on spherical Fourier–Bessel basis functions[14,15]. It provides
a natural way to discretize the Universe into thick shells of fixed
radial width around an observer.

In the RWS3S^{3}universe a finite set of thick shells exhaust the entire domain
and, due to the simple internal metric, the radial distance corresponds to geodesic distance.
If we consider theS3S^{3}universe embedded intoℝ4\mathbb{R}^{4}then the thick shell decomposition with centerCCis equivalent to slices ofS3S^{3}by hyperplanes which are parallel to the tangent hyperplane atCC.
Next we show that the radial shell decomposition of the RW Universe can be identified with a semi-hidden tubular soft tiling.

We emphasize that the purpose of this example is not to derive a new
cosmological result. Rather, the Robertson–Walker setting provides a
geometric framework, inspired by standard radial shell
decompositions used in cosmology, in which a semi-hidden tubular
tiling arises naturally. Our aim is to illustrate how
Theorem1organizes the topology of such a tiling and
permits the inference of less obvious topological quantities associated
with the hidden phase.

## 2.2.3.Interpretation of the double bubble formula to the RW universe

The double bubble algorithm of Corollary2can be directly applied to this
system if we assume that the planets are modeled by 3-balls and their boundaries
are theAA-spheres. The concentric shells of the RW decomposition correspond to theBB-spheres.
We can re-write (16) as:(17)χ𝐁=(2+1m​(n−N))​mm+1.\chi_{\mathbf{B}}=\left(2+\frac{1}{m}(n-N)\right)\frac{m}{m+1}.

As we can observe, the topology of theBB-cells is essentially controlled by the term(n−N)/m(n-N)/mwhich we can interpret heuristically.
If there would be no planets(n=0)(n=0)and no intersections(N=0)(N=0)then, except for the two
3-ballsB1,BmB_{1},B_{m}at the north and south poles, all remainingBB-cells would be spherical shells
withχ​(Bi)=2\chi(B_{i})=2,(i=2,3,…​m−1)(i=2,3,\dots m-1). Planets can cause two types of local ”topological defects”:
they can either appear as enclosed cavities (adding 1 to the Euler characteristic) or they can intersect both
boundary shells, resulting in a hole (subtracting 1 from the Euler characteristic). Ifn=Nn=Nthen these
two effects cancel each other because, on average, each planet (AA-sphere) is intersected by exactly oneBB-sphere,
producing oneCC-circle, so the intersection produces neither a cavity nor a hole. Ifn>Nn>Nthen cavities dominate and ifn<Nn<Nthen
holes dominate.

Corollary2showed that, in the general case, the range ofχ𝐁\chi_{\mathbf{B}}is infinite. However, if we
also consider metric information on the topologicalAA-spheres andBBspheres then this range becomes much more
restricted and may even be narrowed down to a single value.
In the case of the RW universe we treat a very special case of the double bubble algorithm because both
theAA-spheres and theBB-spheres are not just topological spheres but also spheres in the metric sense.
Since oneAA-sphere and oneBB-sphere can intersect transversely
in at most oneCC-circle, so we haveN≤n​mN\leq nm.
This constrains the Euler characteristicχ𝐁\chi_{\mathbf{B}}of the hiddenBB-tiles
more than the condition in Corollary2and we obtain the finite bounds2−n<χ𝐁≤n,2-n<\chi_{\mathbf{B}}\leq n,

with the lower bound corresponding to them→∞m\to\inftylimit, the upper bound attained atm=0m=0.
As we can observe, the admissible range of the topological quantityχ𝐁\chi_{\mathbf{B}}can be narrowed using metric information.

By adding further metric information, for fixedn,mn,mthe actual expected numberNNof intersections can be also expressed
and the admissible interval forχ𝐁\chi_{\mathbf{B}}can be narrowed to a single value. Let us assume that centers of planets are uniformly distributed in space
and let us denote the average radius of a planet byrr. Let us further assume that spacing betweenBB-spheres is uniform
at radial distanceR0R_{0}(see Figure7). Then, geometric probability suggests that the average numberN/nN/nofCC-circles per planet can be written asN/n≈2​r/R0N/n\approx 2r/R_{0}. Fixingn,mn,mand substitutingN=2​r​n/R0N=2rn/R_{0}into (17) yieldsχ𝐁\chi_{\mathbf{B}}.

Both examples discussed in this section exhibit an observable phase and a hidden phase.
In both cases the topology of the soft tiling for the hidden phase could be determined by relying on two sources of information:
equation (1) in Theorem1and additional, geometric information. In the Fermi-surface example the latter
was derived from the geometry of the BCC lattice and, jointly with equation (1) this determined the hidden phase essentially uniquely. In the RW example metric spherical geometry reduced
an initially infinite range of possibilities to a finite interval and using geometric averaging the actual value ofχ𝐁\chi_{\mathbf{B}}could be computed.

## 3.Summary

In this paper we introducedtubular tilings, natural discretizations of binary mixtures defined on smooth manifolds by separating interfaces. We proved that every tubular tiling in dimensionsd>2d>2is at least2-soft, so the boundaries of its tiles contain no strata of codimension greater than two. We also derived a global Euler balance law (Theorem1) relating the Euler characteristics of tubular tiles, their internal interfaces and the ambient manifold.

The present work suggests that the triple-junction tubularity condition (23) may be viewed as the first member of a broader hierarchy. By excluding boundary strata of codimension greater than two, it naturally leads to 2-soft tilings and to the Euler balance law proved here. This raises the possibility that higher-order junction conditions may produce higher degrees of softness together with corresponding higher-order Euler balance laws.

Binary mixtures arise in a wide range of physical settings, including Fermi surfaces, skeletal structures in biology, Turing patterns in reaction–diffusion systems and cosmological models. In many such applications the separating interface is directly observed, whereas physical interpretation naturally focuses on only one of the two complementary regions. Although the interface determines both regions equally, the second region often remains a hidden geometric phase. Theorem1restores this symmetry by assigning tubular cells to both phases and relating their topology through a global Euler balance law. We illustrated this principle in two examples. For the Copper Fermi surface we showed that the soft cell associated with the unoccupied phase has torus topology. For the thick-shell decomposition of the positively curved Robertson–Walker universe we computed the Euler characteristic of the cells tiling the cosmic void.

Beyond these applications, tubular tilings provide a common framework for comparing and classifying binary mixtures through the topology of their discretizations. Several questions naturally arise. While compact ambient manifolds appear to admit 1-soft tilings, a simple inductive argument from[1]shows that no 1-soft tilings exist in Euclidean spaceℝd\mathbb{R}^{d}. The present work suggests that 2-soft tilings are the natural replacement, although it remains unclear which other noncompact manifolds share this property.

The notion ofkk-softness also suggests finer geometric classifications. Whilekk-softness excludes boundary strata of codimension greater thankk, one may further distinguishkk-soft tilings by suitable integral measures supported on codimension-kkstrata. In particular, for 2-soft monohedral tilings ofℝ3\mathbb{R}^{3}, where the lowest-dimensional boundary strata are edges, a natural candidate is the total Gaussian curvature integrated along all edges. We conjecture that this quantity satisfies the sharp lower boundKE≥6​πK_{E}\geq 6\pi. If true, the tubular soft cell associated with the Gyroid (Figure4(f)) would realize the extremal configuration. More broadly, such extremal principles would complement the topological balance laws developed here by linking them to quantitative geometric optimization.

## Appendix ABasic concepts

## A.1.Tubular tilings

## Definition 1(Tubular tilings).

LetMd⊂ℝd+1M^{d}\subset\mathbb{R}^{d+1}be an embedded, smoothdd–dimensional manifold without boundary, and let𝒯M\mathcal{T}_{M}be a locally finite tiling ofMdM^{d}with tilesτi\tau_{i}.
We require that there exist constants0<r−≤r+<∞0<r_{-}\leq r_{+}<\inftysuch that every tileτi\tau_{i}contains a Euclidean ball of radiusr−r_{-}and is contained in a Euclidean ball of radiusr+r_{+}.

We also require that the interface componentsτi,j=τi∩τj\tau_{i,j}=\tau_{i}\cap\tau_{j}

are either empty or smooth, compact(d−1)(d-1)–dimensional manifolds
and we assume that the boundary of each tile is given by pairwise intersections with neighboring tiles:∂τi=⋃j≠i(τi∩τj).\partial\tau_{i}=\bigcup_{j\neq i}(\tau_{i}\cap\tau_{j}).

We also assume that any two distinct connected componentsτi,j\tau_{i,j}of interface setsτi∩τj\tau_{i}\cap\tau_{j}intersect transversely whenever they intersect.

Each tile is assigned a label of the formAiA_{i}orBjB_{j}, where indices distinguish tiles within each class, i.e.Ai≠AjA_{i}\neq A_{j}fori≠ji\neq j, and similarlyBi≠BjB_{i}\neq B_{j}. Thus we obtain abinary labeling𝒯M(A,B)\mathcal{T}^{(A,B)}_{M}of the tiling.
Each tileτi\tau_{i}is assigned exactly one labelAjA_{j}orBkB_{k}, and we identify the tile with its label for notational convenience.
We define the structure for the boundary∂Ai\partial A_{i}for a tileAiA_{i}. We call(18)∂^​Ai:=⋃jAi∩Bj\hat{\partial}A_{i}:=\bigcup_{j}A_{i}\cap B_{j}

itsexternal interfaceand(19)∂¯​Ai:=⋃j≠iAi∩Aj\bar{\partial}A_{i}:=\bigcup_{j\neq i}A_{i}\cap A_{j}

itsinternal interface. Using these concepts, the boundary of the tile can be decomposed as(20)∂Ai=∂^​Ai∪∂¯​Ai,\partial A_{i}=\hat{\partial}A_{i}\cup\bar{\partial}A_{i},

and we call(21)∂̊​Ai:=∂^​Ai∩∂¯​Ai,\mathring{\partial}A_{i}:=\hat{\partial}A_{i}\cap\bar{\partial}A_{i},

theseparation boundary(see Figure8).
We call𝒯M\mathcal{T}_{M}atubular tilingif there exists a smooth embedded hypersurfaceT⊂MdT\subset M^{d}and a binary labeling𝒯M(A,B)\mathcal{T}^{(A,B)}_{M}such that:(22)⋃i,jAi∩Bj=T,\bigcup_{i,j}A_{i}\cap B_{j}=T,

and(23)Ai∩Aj∩Ak=Bi∩Bj∩Bk=∅for all​i≠j≠k.A_{i}\cap A_{j}\cap A_{k}=B_{i}\cap B_{j}\cap B_{k}=\emptyset\qquad\text{for all }i\neq j\neq k.

If these conditions are met then we callTTatubular (hyper)surface.Figure 8.Boundary structure of tubular cell.

## Remark 2(Boundary decomposition of a tubular tile, perfect tilings).

For the boundary∂Ai\partial A_{i}of each tileAiA_{i}, equations (20) and (21) define a decomposition into the external and internal interfaces∂^​Ai\hat{\partial}A_{i}and∂¯​Ai\bar{\partial}A_{i}. Both interfaces are unions of compact(d−1)(d-1)–manifolds, intersecting transversely along smooth compact(d−2)(d-2)–manifolds. The union of these intersections is called theseparation boundaryand is denoted by∂̊​Ai\mathring{\partial}A_{i}(see Figure8).

We say that a tile isactiveif its external interface is nonempty, andpassiveotherwise. In the latter case the separation boundary is empty.
A tubular tiling is calledperfectif all of its tiles are active.
Theorem1remains valid for imperfect tilings.
Nevertheless, many physical systems appear naturally as perfect tubular tilings.
For an imperfect tubular tiling, one may often obtain a perfect tiling either by amalgamating passive tiles with neighboring tiles of the same label or by relabelling the tiling. The first operation preserves the tubular hypersurfaceTTwhile modifying the combinatorial structure of the tiling, whereas the second preserves the combinatorial structure while modifying the associated tubular hypersurface.

## Remark 3(Induced tilings on the interface hypersurface).

Definition1implies that external interfaces of theactivetiles tileTTin two different manners.
Let𝒯M\mathcal{T}_{M}be a tubular tiling with associated hypersurfaceT⊂MT\subset M. Then the external interfacesAi∩Bj⊂TA_{i}\cap B_{j}\subset T

induce two natural tilings ofTT.
From theAA-side,TTis decomposed asT=⋃i∂^​Ai=⋃i(⋃jAi∩Bj),T=\bigcup_{i}\hat{\partial}A_{i}=\bigcup_{i}\left(\bigcup_{j}A_{i}\cap B_{j}\right),

and from theBB-side asT=⋃j∂^​Bj=⋃j(⋃iAi∩Bj).T=\bigcup_{j}\hat{\partial}B_{j}=\bigcup_{j}\left(\bigcup_{i}A_{i}\cap B_{j}\right).

Each of these decompositions defines a normal tiling ofTT(with respect to the induced(d−1)(d-1)-dimensional geometry), and may be interpreted as the interface structure as seen from theAA-phase andBB-phase, respectively.
In particular, codimension-2 strata inMMcorrespond to codimension-1 interfaces within these induced tilings ofTT.

## Remark 4(Induced decompositions of the interface hypersurface).

Let𝒯M\mathcal{T}_{M}be a tubular tiling with associated hypersurfaceT⊂MdT\subset M^{d}. Then the external interfacesAi∩Bj⊂TA_{i}\cap B_{j}\subset T

define two natural decompositions ofTT.

From theAA–side we haveT=⋃i∂^​Ai=⋃i(⋃jAi∩Bj),T=\bigcup_{i}\hat{\partial}A_{i}=\bigcup_{i}\Bigl(\bigcup_{j}A_{i}\cap B_{j}\Bigr),

and from theBB–sideT=⋃j∂^​Bj=⋃j(⋃iAi∩Bj).T=\bigcup_{j}\hat{\partial}B_{j}=\bigcup_{j}\Bigl(\bigcup_{i}A_{i}\cap B_{j}\Bigr).

If the tubular tiling is canonical, then every tile has nonempty
external interface and these decompositions may be viewed as two
natural tilings ofTT, corresponding to the interface structure seen
from theAA–phase and theBB-phase, respectively.
In particular, codimension-22strata of the tubular tiling inMdM^{d}appear as codimension-11interfaces in the induced decompositions ofTT.

## A.2.Soft shapes and soft cells

Softness of shapes and tilings was first defined in[1]ford=2d=2andd=3d=3dimensions by prescribing that the number of sharp corners should be minimized.
Here we aim, on one hand, to extend this notion to arbitrary dimensions. On the other hand, we want to connect the concept of softness and the concept of smoothness.
The following definition of softnessσ\sigmameasures what is the boundary stratum with highest codimension. Ifσ=1\sigma=1then the boundary is smooth. Ind=3d=3dimensions,σ=2\sigma=2characterizes the same shapes identified by the definition in[1]. Ind=2d=2dimensions the new definition is vacuous and therefore we suggest to keep the old definition
because it selects shapes also observed in nature.

## Definition 2(Soft shape).

LetMd⊂ℝd+1M^{d}\subset\mathbb{R}^{d+1}be an embedded, smoothdd-dimensional manifold without boundary, and letS⊂MdS\subset M^{d}be a compact, connected, orientabledd–manifold with piecewise smooth boundary∂S\partial S.

We callSSakk-soft shape(or, alternatively we writeσ​(S)=k\sigma(S)=k) ifkkis the smallest integer such that for every pointp∈∂Sp\in\partial Sthere exists a smooth embeddedkk-codimensional submanifoldγ⊆∂S\gamma\subseteq\partial S

such thatpplies in the relative interior ofγ\gamma.

## Remark 5(Soft cell terminology).

Regarding the parameterkkwe make some simple observations:
- •

Sincedim(∂S)=d−1\dim(\partial S)=d-1, sok>0k>0.
- •

Ifk=1k=1then every boundary pointppadmits a neighborhood in∂S\partial Sthat is a smooth(d−1)(d-1)-manifold. Hence∂S\partial Sis smooth. In other words, we recognize that being11-soft is equivalent to being smooth.
- •

For brevity, ifd>2d>2then we call22-soft shapes simply soft shapes.

## Remark 6.

Ford=2d=2, every boundary point of a piecewise smooth curve lies in the interior of a smooth 0-manifold (a point). Hence every planar shape is automatically22-soft, so the definition carries no geometric information. Therefore, in dimension two we retain the earlier notion of softness introduced in[1].

## Definition 3(Soft tiling and soft cell).

LetMd⊂ℝd+1M^{d}\subset\mathbb{R}^{d+1}be a smooth embeddeddd–manifold without boundary, and let0<k<d0<k<dbe an integer.
If a tiling𝒯M\mathcal{T}_{M}consists of tiles, each of which is akk-soft shape, we call𝒯M\mathcal{T}_{M}akk-soft tiling.
If copies of a singlekk-soft shape tileMdM^{d}, we call that shape akk-soft cell.

## Proposition 1.

LetMd⊂ℝd+1M^{d}\subset\mathbb{R}^{d+1}be an embedded, smoothdd–dimensional manifold without boundary, and let𝒯M\mathcal{T}_{M}be a tubular tiling ofMdM^{d}. Then, ifd>2d>2, the tiling𝒯M\mathcal{T}_{M}is a22-soft tiling.

## Proof.

LetAiA_{i}be a tile and letp∈∂Aip\in\partial A_{i}.
Because the tiling is tubular, every interface component is a smooth(d−1)(d-1)–manifold. Moreover, the condition (23)
implies that at most two interface components (faces) of∂Ai\partial A_{i}can meet at the pointpp.
Since external interfaces tileTT, each tileAiA_{i}has at least one external facefi1=Ai∩Bjf_{i}^{1}=A_{i}\cap B_{j}, and this face satisfiesfi1⊂Tf_{i}^{1}\subset T.

There are two cases:

(1)pplies on exactly one face.Thenpplies on a smooth(d−1)(d-1)–manifold contained in∂Ai\partial A_{i}, thusAiA_{i}is11–soft atpp.
This also implies thatAiA_{i}is22–soft atpp.

(2)pplies on two faces.One face is the external facefi1⊂Tf_{i}^{1}\subset T.
Let the second face be the internal facefi2=Ai∩Akf_{i}^{2}=A_{i}\cap A_{k}.
Bothfi1f_{i}^{1}andfi2f_{i}^{2}are smooth(d−1)(d-1)–manifolds. Their intersection isfi1,2=fi1∩fi2=T∩(Ai∩Ak),f_{i}^{1,2}=f_{i}^{1}\cap f_{i}^{2}=T\cap(A_{i}\cap A_{k}),

which is a smooth(d−2)(d-2)–manifold because it is the transverse intersection of two smooth hypersurfaces inMdM^{d}.

Thuspplies in the interior of the smooth(d−2)(d-2)–manifoldfi1,2f_{i}^{1,2}, andAiA_{i}is22–soft atpp.

In all cases, each boundary pointp∈∂Aip\in\partial A_{i}lies in the interior of a smooth(d−2)(d-2)–dimensional submanifold of∂Ai\partial A_{i}. HenceAiA_{i}is a22–soft shape.
Since this holds for each tile,𝒯M\mathcal{T}_{M}is a22–soft tiling.
∎

## Proposition 2.

LetMd⊂ℝd+1M^{d}\subset\mathbb{R}^{d+1}be an embedded, smoothdd–dimensional manifold without boundary, and let𝒯M\mathcal{T}_{M}be a tubular tiling ofMdM^{d}. Then, ifd>2d>2, the tiling𝒯M\mathcal{T}_{M}is a22-soft tiling.

## Proof.

LetAiA_{i}be a tile and letp∈∂Aip\in\partial A_{i}.
Because the tiling is tubular, every interface component is a smooth(d−1)(d-1)–manifold. Moreover, the condition (23)
implies that atn≤3n\leq 3interface components (faces) of∂Ai\partial A_{i}can meet at the pointpp: since two internal faces already force anA​A​AAAA-violation
of (23), regardless of any other faces present, and three external faces force aB​B​BBBB-violation, any configuration withn≥4n\geq 4automatically contains one of these forbidden patterns.
As we can see, external multiplicity never creates a genuine crease, so only internal-face count and the internal/external mix matter.
If we haven≤3n\leq 3then only the following combinations are possible:
- (1)

n=1n=1:
- (a)

ppis an interior point of one internal face ofAiA_{i}. Thenpplies on a smooth(d−1)(d-1)–manifold contained in∂Ai\partial A_{i}, thusAiA_{i}is11–soft atpp.
This also implies thatAiA_{i}is22–soft atpp.
- (b)

ppis an interior point of one external face ofAiA_{i}. Argument is the same as above.
- (2)

n=2n=2:
- (a)

ppis on the boundary between an external and an internal face ofAiA_{i}. Letfi1⊂Tf_{i}^{1}\subset Tbe the external face andfi2=Ai∩Akf_{i}^{2}=A_{i}\cap A_{k}be the internal face.
Bothfi1f_{i}^{1}andfi2f_{i}^{2}are smooth(d−1)(d-1)–manifolds. Their intersection isfi1,2=fi1∩fi2=T∩(Ai∩Ak),f_{i}^{1,2}=f_{i}^{1}\cap f_{i}^{2}=T\cap(A_{i}\cap A_{k}),

which is a smooth(d−2)(d-2)–manifold because it is the transverse intersection of two smooth hypersurfaces inMdM^{d}.
Thuspplies in the interior of the smooth(d−2)(d-2)–manifoldfi1,2f_{i}^{1,2}, andAiA_{i}is22–soft atpp.
- (b)

ppis on the boundary between two internal faces. This case can be excluded because it would violate the triple-junction criterion (23).
- (c)

ppis on the boundary between two external faces. Since both external faces are patches of the smooth tubular surfaceTT, this case reduces to case (1)(b).
- (3)

n=3n=3
- (a)

ppis at the intersection of three internal faces ofAiA_{i}. This case can be excluded because it would violate the triple-junction criterion (23)
- (b)

ppis at the intersection of three external faces ofAiA_{i}.This case can be excluded because it would violate the triple-junction criterion (23)
- (c)

ppis at the intersection of one external face and two internal faces ofAiA_{i}. This case can be excluded because it would violate the triple-junction criterion (23)
- (d)

ppis at the intersection of one internal face and two external faces ofAiA_{i}. Since both external faces are patches of the smooth tubular surfaceTT, this case reduces to case (2)(a).

In all cases, each boundary pointp∈∂Aip\in\partial A_{i}lies in the interior of a smooth(d−2)(d-2)–dimensional submanifold of∂Ai\partial A_{i}. HenceAiA_{i}is a22–soft shape.
Since this holds for each tile,𝒯M\mathcal{T}_{M}is a22–soft tiling.
∎

## Remark 7.

The restrictiond>2d>2is imposed not because the statement fails ford=2d=2,
but because in that case the notion of22–softness becomes vacuous:
a smooth0–manifold is just a point, so every boundary point already satisfies the condition,
and the proposition carries no geometric content.
If we regard points as smooth manifolds then all polygonal tilings
will be classified as soft tilings and for this reason, the cased=2d=2is excluded from the present definition and
will be treated separately. A slightly different approach, motivated by natural examples,
aims to minimize the number of geometric corners. Ind≥3d\geq 3dimensions any soft tiling satisfies this
condition because the number of corners is zero. For the 2D case, in[16]it was proven that
in a normal, balanced tiling ofℝ2\mathbb{R}^{2}the minimal number
for the average number of geometric corners is 2. Planar tilings with this property are also called soft.

## Remark 8.

Tubular soft tilesAiA_{i}satisfy a strengthened softness property that is not
required by Definition2.
Not only is the boundary∂Ai\partial A_{i}a closed, piecewise smooth(d−1)(d-1)–manifold,
but the(d−2)(d-2)–dimensional separation boundary∂̊​Ai\mathring{\partial}A_{i}is adisjoint unionof closed, smooth manifolds.
In order to satisfy Definition2,this is not necessary:
the smooth(d−2)(d-2)–manifolds defining the separation boundary could, in principle,
have transverse or tangential intersections. In[16]and[1]such soft cells with non-disjoint
separation boundaries were presented.

## Remark 9.

Atubular soft cellis add-dimensional compact objectSSsuch that
identical copies ofSSfillMdM^{d}without gaps and overlaps and the boundary∂S\partial Sconsists ofnndisjoint,d−1d-1domains with smooth,(d−2)(d-2)dimensional boundaries andmmdisjoint, smooth,(d−1)(d-1)-dimensional patches of a smooth manifold. It is important to recognize that these properties are sufficient to guarantee thatSSis a soft cell but they are not sufficient
to guarantee thatSSis a tubular soft cell. For the latter, the global existence of a smooth,(d−1)(d-1)dimensional separating surface is also required.
The soft cell illustrated in Figure4(b) has all the listed properties but does not belong to a tubular tiling.

## Appendix BProof of the Euler balance theorem (Theorem1)

## Proof.

(Theorem1)
We first introduce the finite volume setup for noncompact manifolds
then write general equations (independent of the parity of the dimension) and finally
we separate the odd and even dimensional case.

## B.1.Finite volume setup

LetMd⊂ℝd+1M^{d}\subset\mathbb{R}^{d+1}be an embedded, smoothdd–dimensional manifold without boundary, and let𝒯M\mathcal{T}_{M}be a tubular tiling ofMdM^{d}with tilesτi\tau_{i}.
LetT⊂MdT\subset M^{d}be an embedded hypersurface associated with𝒯\mathcal{T}.
ForR>0R>0, letℬR​(P)⊂Md\mathcal{B}_{R}(P)\subset M^{d}denote the closed, intrinsic ball of radiusRRwith centerP∈MdP\in M^{d}:(24)BR​(P)={x∈Md:d​(P,x)<R},B_{R}(P)=\{x\in M^{d}:d(P,x)<R\},

whered​(P,x)d(P,x)is the geodesic distance betweenxxandPP.

We define the truncated surfaceTR:=T∩ℬR.T_{R}:=T\cap\mathcal{B}_{R}.

Then we always have(25)limR→∞ℬR​(P)=⋃R>0ℬR​(P)=Md.\lim_{R\to\infty}\mathcal{B}_{R}(P)=\bigcup_{R>0}\mathcal{B}_{R}(P)=M^{d}.

## Remark 10.

IfMdM^{d}is compact, then there exists a finite radiusR=R0R=R_{0}(the intrinsic diameter fromPP) such that∀R>R0:ℬR(P)=Md,\forall R>R_{0}:\quad\mathcal{B}_{R}(P)=M^{d},

so the limit process
described in equation (25) saturates already at some finite radiusR0R_{0}.
IfMdM^{d}is noncompact then there is no finite saturation radiusR0R_{0}, the union over allR>0R>0still exhausts the manifoldMdM^{d}.

Thus, equation (25) remains valid both in the compact and the non-compact case.
Henceforth we write equations which are formally valid in both cases but we keep in mind that
the limit process is slightly different. In the case of compactMdM^{d}we will assume
thatR>R0R>R_{0}.

We denote byNA​(R)N_{A}(R)andNB​(R)N_{B}(R)the numbers ofAA-tiles andBB-tiles,
respectively, that are entirely contained inℬR\mathcal{B}_{R}and we writeN​(R):=NA​(R)+NB​(R).N(R):=N_{A}(R)+N_{B}(R).

We also define the finite portions of the partitionsAAandBB, contained inℬR\mathcal{B}_{R}asAR\displaystyle A_{R}:=(A∪∂A)∩ℬR=(A∪T)∩ℬR,\displaystyle=(A\cup\partial A)\cap\mathcal{B}_{R}=(A\cup T)\cap\mathcal{B}_{R},BR\displaystyle B_{R}:=(B∪∂B)∩ℬR=(B∪T)∩ℬR,\displaystyle=(B\cup\partial B)\cap\mathcal{B}_{R}=(B\cup T)\cap\mathcal{B}_{R},

ThenARA_{R},BRB_{R}, andTRT_{R}are compact, and satisfy(26)AR∪BR=ℬR,AR∩BR=TR,A_{R}\cup B_{R}=\mathcal{B}_{R},\qquad A_{R}\cap B_{R}=T_{R},

and for theR→∞R\to\inftylimit we can writeA​⋃B=Md,A​⋂B=T.A\bigcup B=M^{d},\qquad A\bigcap B=T.

The relative frequencies ofAA- andBB-tiles can be obtained as(27)pA​(R)=NA​(R)N​(R),pB​(R)=NB​(R)N​(R).p_{A}(R)=\frac{N_{A}(R)}{N(R)},\,p_{B}(R)=\frac{N_{B}(R)}{N(R)}.

We introduce shorthand notations for the Euler characteristics for the tiles and their boundaries asχ𝐀,i=χ​(Ai),χA,i=χ​(∂Ai),\chi_{\mathbf{A},i}=\chi(A_{i}),\quad\chi_{A,i}=\chi(\partial A_{i}),

and the components of the boundary asχA^,i=χ​(∂^​Ai),χA¯,i=χ​(∂¯​Ai),χÅ,i=χ​(∂̊​Ai)\chi_{\hat{A},i}=\chi(\hat{\partial}A_{i}),\,\chi_{\bar{A},i}=\chi(\bar{\partial}A_{i}),\,\chi_{\mathring{A},i}=\chi(\mathring{\partial}A_{i})

with corresponding averages(28)χ𝐀​(R)=1NA​(R)​∑i=1NA​(R)χ​(Ai),χA​(R)=1NA​(R)​∑i=1NA​(R)χ​(∂Ai),\chi_{\mathbf{A}}(R)=\frac{1}{N_{A}(R)}\sum_{i=1}^{N_{A}(R)}\chi(A_{i}),\quad\chi_{A}(R)=\frac{1}{N_{A}(R)}\sum_{i=1}^{N_{A}(R)}\chi(\partial A_{i}),(29)χA¯​(R)=1NA​(R)​∑i=1NA​(R)χA¯,i,χA^​(R)=1NA​(R)​∑i=1NA​(R)χA^,i,χÅ​(R)=1NA​(R)​∑i=1NA​(R)χÅ,i.\chi_{\bar{A}}(R)=\frac{1}{N_{A}(R)}\sum_{i=1}^{N_{A}(R)}\chi_{\bar{A},i},\quad\chi_{\hat{A}}(R)=\frac{1}{N_{A}(R)}\sum_{i=1}^{N_{A}(R)}\chi_{\hat{A},i},\quad\chi_{\mathring{A}}(R)=\frac{1}{N_{A}(R)}\sum_{i=1}^{N_{A}(R)}\chi_{\mathring{A},i}.

For theBBpartition the notations and averages are analogous.

## B.2.Limits

By the assumptions of Theorem1, asR→∞R\to\infty, the averages in (27), (28), (29) approach respective finite limits.
As noted in Remark10, this limit is already saturated at finiteR=R0R=R_{0}ifMdM^{d}is compact and in this caseNA,NB,NN_{A},N_{B},Nremain finite. In the noncompact caseNA​(R),NB​(R)N_{A}(R),N_{B}(R)andN​(R)N(R)will approach infinity and boundary contributions coming from∂BR\partial B_{R}disappear after normalization byN​(R)N(R). We can write formally both for the compact and the non-compact case:pA:=limR→∞pA​(R),pB:=limR→∞pB​(R),p_{A}:=\lim_{R\to\infty}p_{A}(R),\quad p_{B}:=\lim_{R\to\infty}p_{B}(R),χ𝐀:=limR→∞χ𝐀​(R),χA:=limR→∞χA​(R),\chi_{\mathbf{A}}:=\lim_{R\to\infty}\chi_{\mathbf{A}}(R),\quad\chi_{A}:=\lim_{R\to\infty}\chi_{A}(R),χA¯:=limR→∞χA¯​(R),χA^:=limR→∞χA^​(R),χÅ:=limR→∞χÅ​(R).\chi_{\bar{A}}:=\lim_{R\to\infty}\chi_{\bar{A}}(R),\quad\chi_{\hat{A}}:=\lim_{R\to\infty}\chi_{\hat{A}}(R),\quad\chi_{\mathring{A}}:=\lim_{R\to\infty}\chi_{\mathring{A}}(R).

These limits define the averages associated withAA-partition of the tubular tiling𝒯M\mathcal{T}_{M}with analogous limits for theBB–partition.

## B.3.General equations

Using (26), we can directly apply (3) to obtain(30)χ​(ℬR)=χ​(AR)+χ​(BR)−χ​(TR).\chi(\mathcal{B}_{R})=\chi(A_{R})+\chi(B_{R})-\chi(T_{R}).

Our goal is to obtain the three terms on the right hand side of (30)
as functions of of the averages (28)-(29).

## B.3.1.Cell boundary equations

Both theAA-type and theBB-type external interfaces∂^​Ai,∂^​Bj\hat{\partial}A_{i},\hat{\partial}B_{j}tileTRT_{R}, so we have(31)TR=⋃i=1NA​(R)∂^​Ai=⋃j=1NB​(R)∂^​Bj.T_{R}=\bigcup_{i=1}^{N_{A}(R)}\hat{\partial}A_{i}=\bigcup_{j=1}^{N_{B}(R)}\hat{\partial}B_{j}.

Theedgesof the above tilings, along which the smooth patches (external interfaces)∂^​Ai,∂^​Bj\hat{\partial}A_{i},\hat{\partial}B_{j}are glued to each other, are the separation boundaries∂̊​Ai,∂̊​Bj\mathring{\partial}A_{i},\mathring{\partial}B_{j}.
Considering this fact, and using equations (23) and (31), we can compute the Euler characteristic for the union of the smooth patches∂^​Ai\hat{\partial}A_{i}under the exclusion-inclusion principle (3) as(32)χ​(TR)=χ​(⋃i=1NA​(R)∂^​Ai)=∑i=1NA​(R)χ​(∂^​Ai)−χ​(⋃i=1NA​(R)∂̊​Ai).\chi(T_{R})=\chi\left(\bigcup_{i=1}^{N_{A}(R)}\hat{\partial}A_{i}\right)=\sum_{i=1}^{N_{A}(R)}\chi(\hat{\partial}A_{i})-\chi\left(\bigcup_{i=1}^{N_{A}(R)}\mathring{\partial}A_{i}\right).

Now we observe that each connected component of the boundary⋃∂̊​Ai\bigcup\mathring{\partial}A_{i}is a closed smooth(d−2)(d-2)–manifold and, because of the condition (23)
appears, in theR→∞R\to\inftylimit as a boundary component of exactly two tubular soft tiles. Therefore, in theR→∞R\to\inftylimit,⋃∂̊​Ai\bigcup\mathring{\partial}A_{i}is covered exactly twice by the family{∂̊​Ai}\{\mathring{\partial}A_{i}\}.
By the inclusion–exclusion principle (3) for Euler characteristic, at finite values ofRRwe can write(33)χ​(⋃i=1NA​(R)∂̊​Ai)=12​∑i=1NA​(R)χ​(∂̊​Ai)+ϵÅ​(R),\chi\left(\bigcup_{i=1}^{N_{A}(R)}\mathring{\partial}A_{i}\right)=\frac{1}{2}\sum_{i=1}^{N_{A}(R)}\chi(\mathring{\partial}A_{i})+\epsilon_{\mathring{A}}(R),

whereϵÅ​(R)\epsilon_{\mathring{A}}(R)is a boundary error term.

## Remark 11.

The error termϵÅ​(R)\epsilon_{\mathring{A}}(R)(and the analogous error termϵB̊​(R)\epsilon_{\mathring{B}}(R)for theBBpartition) only arises in the noncompact case
and we discuss them subsectionB.3.3.

Plugging (33) and (32) into (31) yields:(34)χ​(TR)=∑i=1NA​(R)χ​(∂^​Ai)−12​∑i=1NA​(R)χ​(∂̊​Ai)−ϵÅ​(R).\chi(T_{R})=\sum_{i=1}^{N_{A}(R)}\chi(\hat{\partial}A_{i})-\frac{1}{2}\sum_{i=1}^{N_{A}(R)}\chi(\mathring{\partial}A_{i})-\epsilon_{\mathring{A}}(R).

Next we rewrite (33) for the averages as(35)χ​(TR)=NA​(R)​(χA^−12​χÅ)−ϵÅ​(R).\chi(T_{R})=N_{A}(R)\left(\chi_{\hat{A}}-\frac{1}{2}\chi_{\mathring{A}}\right)-\epsilon_{\mathring{A}}(R).

In the next step we write the Euler characteristics for the boundary of the individual cell.
Using (3), (20) and(21), we can write(36)χ​(∂Ai)=χ​(∂^​Ai)+χ​(∂¯​Ai)−χ​(∂̊​Ai).\chi(\partial A_{i})=\chi(\hat{\partial}A_{i})+\chi(\bar{\partial}A_{i})-\chi(\mathring{\partial}A_{i}).

Rearranging (36) and replacing individual Euler characteristics by their respective averages yields(37)χA^=χA−χA¯+χÅ.\chi_{\hat{A}}=\chi_{A}-\chi_{\bar{A}}+\chi_{\mathring{A}}.

Now we plug (37) into (35):(38)χ​(TR)=NA​(R)​((χA−χA¯+χÅ)−12​χÅ)−ϵÅ​(R).\chi(T_{R})=N_{A}(R)\left((\chi_{A}-\chi_{\bar{A}}+\chi_{\mathring{A}})-\frac{1}{2}\chi_{\mathring{A}}\right)-\epsilon_{\mathring{A}}(R).

After rearranging terms and with analogous considerations for theBBpartition, using (31), we obtain(39)χ​(TR)=NA​(R)​(χA−χA¯+12​χÅ)−ϵÅ​(R)=NB​(R)​(χB−χB¯+12​χB̊)−ϵB̊​(R).\chi(T_{R})=N_{A}(R)\left(\chi_{A}-\chi_{\bar{A}}+\frac{1}{2}\chi_{\mathring{A}}\right)-\epsilon_{\mathring{A}}(R)=N_{B}(R)\left(\chi_{B}-\chi_{\bar{B}}+\frac{1}{2}\chi_{\mathring{B}}\right)-\epsilon_{\mathring{B}}(R).

## B.3.2.Solid cell equations

Next we consider thedd-dimensional cellsAi,BjA_{i},B_{j}themselves for which we have(40)AR=⋃i=1NA​(R)Ai,BR=⋃j=1NB​(R)Bj.A_{R}=\bigcup_{i=1}^{N_{A}(R)}A_{i},\,B_{R}=\bigcup_{j=1}^{N_{B}(R)}B_{j}.

In each partition, they are glued on the internal interfaces∂¯​Ai,∂¯​Bj\bar{\partial}A_{i},\bar{\partial}B_{j}.
Analogously to (32), for the union of the cells (tilingAA) we can write:(41)χ​(AR)=χ​(⋃i=1NA​(R)Ai)=∑i=1NA​(R)χ​(Ai)−χ​(⋃i=1NA​(R)∂¯​Ai).\chi(A_{R})=\chi\left(\bigcup_{i=1}^{N_{A}(R)}A_{i}\right)=\sum_{i=1}^{N_{A}(R)}\chi(A_{i})-\chi\left(\bigcup_{i=1}^{N_{A}(R)}\bar{\partial}A_{i}\right).

Since, based on condition (23), in theR→∞R\to\inftylimit, each internal interface∂¯​Ai\bar{\partial}A_{i}is counted exactly twice in the union, under the exclusion-inclusion principle we write for finiteRR:(42)χ​(AR)=∑i=1NA​(R)χ​(Ai)−12​∑i=1NA​(R)χ​(∂¯​Ai)−ϵA¯​(R).\chi(A_{R})=\sum_{i=1}^{N_{A}(R)}\chi(A_{i})-\frac{1}{2}\sum_{i=1}^{N_{A}(R)}\chi(\bar{\partial}A_{i})-\epsilon_{\bar{A}}(R).

whereϵÅ​(R)\epsilon_{\mathring{A}}(R)is a boundary error term and the Euler characteristic for theBBpartition can be written in an analogous manner.

## Remark 12.

The error termϵA¯​(R)\epsilon_{\bar{A}}(R)(and the analogous error termϵB¯​(R)\epsilon_{\bar{B}}(R)for theBBpartition) only arises in the noncompact case and
we discuss them in subsectionB.3.3.

Rewriting (42) for the averages and writing the analogous formula for theBBpartition we get(43)χ​(AR)=NA​(R)​(χ𝐀−12​χA¯)−ϵA¯​(R),χ​(BR)=NB​(R)​(χ𝐁−12​χB¯)−ϵB¯​(R)\chi(A_{R})=N_{A}(R)\left(\chi_{\mathbf{A}}-\frac{1}{2}\chi_{\bar{A}}\right)-\epsilon_{\bar{A}}(R),\quad\chi(B_{R})=N_{B}(R)\left(\chi_{\mathbf{B}}-\frac{1}{2}\chi_{\bar{B}}\right)-\epsilon_{\bar{B}}(R)

## B.3.3.Unified equation

In the next step we plug (39) and (43) into (30) and divide byN​(R)=(NA​(R)+NB​(R))N(R)=(N_{A}(R)+N_{B}(R)):(44)χ​(ℬR)N​(R)=pA​(R)​(χ𝐀−12​χA¯)−ϵA¯​(R)N​(R)+pB​(R)​(χ𝐁−12​χB¯)−ϵB¯​(R)N​(R)−pA​(R)​(χA−χA¯+12​χÅ)+ϵÅ​(R)N​(R).\frac{\chi(\mathcal{B}_{R})}{N(R)}=p_{A}(R)\left(\chi_{\mathbf{A}}-\frac{1}{2}\chi_{\bar{A}}\right)-\frac{\epsilon_{\bar{A}}(R)}{N(R)}+p_{B}(R)\left(\chi_{\mathbf{B}}-\frac{1}{2}\chi_{\bar{B}}\right)-\frac{\epsilon_{\bar{B}}(R)}{N(R)}-p_{A}(R)\left(\chi_{A}-\chi_{\bar{A}}+\frac{1}{2}\chi_{\mathring{A}}\right)+\frac{\epsilon_{\mathring{A}}(R)}{N(R)}.(45)χ​(ℬR)N​(R)=pA​(R)​(χ𝐀−12​χA¯)−ϵA¯​(R)N​(R)+pB​(R)​(χ𝐁−12​χB¯)−ϵB¯​(R)N​(R)−pB​(R)​(χB−χB¯+12​χB̊)+ϵB̊​(R)N​(R).\frac{\chi(\mathcal{B}_{R})}{N(R)}=p_{A}(R)\left(\chi_{\mathbf{A}}-\frac{1}{2}\chi_{\bar{A}}\right)-\frac{\epsilon_{\bar{A}}(R)}{N(R)}+p_{B}(R)\left(\chi_{\mathbf{B}}-\frac{1}{2}\chi_{\bar{B}}\right)-\frac{\epsilon_{\bar{B}}(R)}{N(R)}-p_{B}(R)\left(\chi_{B}-\chi_{\bar{B}}+\frac{1}{2}\chi_{\mathring{B}}\right)+\frac{\epsilon_{\mathring{B}}(R)}{N(R)}.

Our goal is to take theR→∞R\to\inftylimit for (44)-(45).
Using equation (25) and Remark10, we can replace the left hand side:(46)limR→∞χ​(ℬR)N​(R)=χ​(Md)N,\lim_{R\to\infty}\frac{\chi(\mathcal{B}_{R})}{N(R)}=\frac{\chi(M^{d})}{N},

noting thatNNwill be infinite ifMdM^{d}is noncompact, so in ifMdM^{d}is noncompact then this term will vanish.

Next we compute the error terms.
In the compact case, as mentioned in Remarks11and12, there are no error terms.
In the noncompact case, since the size of the tiles is uniformly bounded from below and from above, the number of tiles on the boundaryNb​o​u​n​d​a​r​y​(R)N_{boundary}(R)ofℬR\mathcal{B}_{R}is growing withRd−1R^{d-1}while the number of tilesNRN_{R}contained inℬR\mathcal{B}_{R}is growing withRdR^{d}. Since the all errorsϵÅ​(R),ϵB̊​(R),\epsilon_{\mathring{A}}(R),\epsilon_{\mathring{B}}(R),ϵA¯​(R),ϵB¯​(R)\epsilon_{\bar{A}}(R),\epsilon_{\bar{B}}(R)are proportional toNb​o​u​n​d​a​r​y​(R)N_{boundary}(R), we can write(47)limR→∞ϵÅ​(R)N​(R)=limR→∞ϵB̊​(R)N​(R)=limR→∞ϵA¯​(R)N​(R)=limR→∞ϵB¯​(R)N​(R)=0.\lim_{R\to\infty}\frac{\epsilon_{\mathring{A}}(R)}{N(R)}=\lim_{R\to\infty}\frac{\epsilon_{\mathring{B}}(R)}{N(R)}=\lim_{R\to\infty}\frac{\epsilon_{\bar{A}}(R)}{N(R)}=\lim_{R\to\infty}\frac{\epsilon_{\bar{B}}(R)}{N(R)}=0.

Using the notation from SubsectionB.2, plugging (46) and (47) into (44)-(45) and swapping the right hand and left hand sides we get:(48)pA​(χ𝐀−12​χA¯)+pB​(χ𝐁−12​χB¯)−pA​(χA−χA¯+12​χÅ)=χ​(Md)Np_{A}\left(\chi_{\mathbf{A}}-\frac{1}{2}\chi_{\bar{A}}\right)+p_{B}\left(\chi_{\mathbf{B}}-\frac{1}{2}\chi_{\bar{B}}\right)-p_{A}\left(\chi_{A}-\chi_{\bar{A}}+\frac{1}{2}\chi_{\mathring{A}}\right)=\frac{\chi(M^{d})}{N}(49)pA​(χ𝐀−12​χA¯)+pB​(χ𝐁−12​χB¯)−pB​(χB−χB¯+12​χB̊)=χ​(Md)N.p_{A}\left(\chi_{\mathbf{A}}-\frac{1}{2}\chi_{\bar{A}}\right)+p_{B}\left(\chi_{\mathbf{B}}-\frac{1}{2}\chi_{\bar{B}}\right)-p_{B}\left(\chi_{B}-\chi_{\bar{B}}+\frac{1}{2}\chi_{\mathring{B}}\right)=\frac{\chi(M^{d})}{N}.

If we take the sum or the difference of (48) and (49), we get, respectively(50)pA​(2​χ𝐀−χA−12​χÅ)+pB​(2​χ𝐁−χB−12​χB̊)\displaystyle p_{A}\left(2\chi_{\mathbf{A}}-\chi_{A}-\frac{1}{2}\chi_{\mathring{A}}\right)+p_{B}\left(2\chi_{\mathbf{B}}-\chi_{B}-\frac{1}{2}\chi_{\mathring{B}}\right)=\displaystyle=2​χ​(Md)N.\displaystyle\frac{2\chi(M^{d})}{N}.(51)pA​(χA−χA¯+12​χÅ)−pB​(χB−χB¯+12​χB̊)\displaystyle p_{A}\left(\chi_{A}-\chi_{\bar{A}}+\frac{1}{2}\chi_{\mathring{A}}\right)-p_{B}\left(\chi_{B}-\chi_{\bar{B}}+\frac{1}{2}\chi_{\mathring{B}}\right)=\displaystyle=0.\displaystyle 0.

## B.4.Odd dimensions

Ifd=2​k+1d=2k+1is an odd number, then(52)χÅ=χB̊=0,\chi_{\mathring{A}}=\chi_{\mathring{B}}=0,

because the separation boundary is the disjoint union of closed,(d−2)(d-2)-dimensional manifolds.

## Lemma 1.

Ifddis odd then(53)2​χ​(Md)N=0.\frac{2\chi(M^{d})}{N}=0.

## Proof.

IfMdM^{d}is compact andddis odd, then we haveχ​(Md)=0\chi(M^{d})=0, so the claim is proven. IfMdM^{d}is noncompact thenN=∞N=\infty.
SinceMdM^{d}is of finite topological type,χ​(Md)\chi(M^{d})is finite,
so the claim is also proven for the noncompact case.
∎

Ifddis odd, then we can also use(54)χA=2​χ𝐀,χB=2​χ𝐁.\chi_{A}=2\chi_{\mathbf{A}},\quad\chi_{B}=2\chi_{\mathbf{B}}.

Plugging (52), (53) and (54) into (50) we get an identity. Equation (51) can be written as(55)pA​(2​χ𝐀−χA¯)−pB​(2​χ𝐁−χB¯)=0.p_{A}\left(2\chi_{\mathbf{A}}-\chi_{\bar{A}}\right)-p_{B}\left(2\chi_{\mathbf{B}}-\chi_{\bar{B}}\right)=0.

## B.5.Even dimensions

Ifd=2​kd=2kis an even number then∂Ai,∂Bj\partial A_{i},\partial B_{j}are odd-dimensional closed manifolds, so we have(56)χA=χB=0.\chi_{A}=\chi_{B}=0.

We also observe that the internal interfaces∂¯​Ai,∂¯​Bj\bar{\partial}A_{i},\bar{\partial}B_{j}are compact, odd-dimensional manifolds the respective boundaries of which is the separation boundary∂̊​A\mathring{\partial}A, so we can write(57)χA¯=12​χÅ,χB¯=12​χB̊.\chi_{\bar{A}}=\frac{1}{2}\chi_{\mathring{A}},\quad\chi_{\bar{B}}=\frac{1}{2}\chi_{\mathring{B}}.

Plugging (56) and (57) into (51) yields an identity and (50) can be written as(58)pA​(2​χ𝐀−χA¯)+pB​(2​χ𝐁−χB¯)=2​χ​(Md)N.p_{A}\left(2\chi_{\mathbf{A}}-\chi_{\bar{A}}\right)+p_{B}\left(2\chi_{\mathbf{B}}-\chi_{\bar{B}}\right)=\frac{2\chi(M^{d})}{N}.

## B.6.Completing the proof

Equation (55) proves Theorem1for odd values ofddwhile equation (58) proves Theorem1for even values ofdd. This completes the proof of Theorem1.
∎

## Appendix CSubstitution table for the examples#NameFigddMdM^{d}χ​(Md)\chi(M^{d})pAp_{A}pBp_{B}χ𝐀\chi_{\mathbf{A}}χ𝐁\chi_{\mathbf{B}}χA¯\chi_{\bar{A}}χB¯\chi_{\bar{B}}1Schwarz P5(a)33ℝ3\mathbb{R}^{3}1112\frac{1}{2}12\frac{1}{2}111166662Schwarz D1(b)33ℝ3\mathbb{R}^{3}1112\frac{1}{2}12\frac{1}{2}111144443Gyroid4(f)33ℝ3\mathbb{R}^{3}1112\frac{1}{2}12\frac{1}{2}111133334Fermi Cu633ℝ3\mathbb{R}^{3}1112\frac{1}{2}12\frac{1}{2}11088665Honeycomb2(a)22T2T^{2}0nn+1\frac{n}{n+1}1n+1\frac{1}{n+1}11−n-n006Pollen3(b)22S2S^{2}22nn+1\frac{n}{n+1}1n+1\frac{1}{n+1}112−n2-n007RW733S3S^{3}0nn+m+1\frac{n}{n+m+1}m+1n+m+1\frac{m+1}{n+m+1}112​m+n−Nm+1\frac{2m+n-N}{m+1}02​m​(2−k)m+1\frac{2m(2-k)}{m+1}Table 1.Substitution table for the examples illustrated in the article.

## Acknowledgement

The author is indebted to Gegő Almádi who
geometrically constructed the toroidalBB-cell of the Fermi Copper surface and to László Strommer who designed all figures. This research was supported by NKFIH grant K149429.

## References
- [1]G. Domokos, A. Goriely, Á. G. Horváth, and K. Regős.Soft cells and the geometry of seashells.PNAS Nexus, 3(9):pgae311, 2024.
- [2]Galo José R.Modelo matemático tridimensional uniforme del Nautilus.RED Descartes, Cordoba, 12 2024.
- [3]Sophie Theis, Mario A Mendieta-Serrano, Bernardo Chapa-y Lazo, Juliet Chen, and
Timothy E Saunders.Cellmet: Extracting 3d shape and topology metrics from confluent
cells within tissues.PLOS Computational Biology, 21:1–18, 2025.
- [4]Matan Yuval, Amit Peleg, Elvan Ceyhan, Dan Tchernov, Yossi Loya, Avi
Bar-Massada, and Tali Treibitz.Intratentacular budding and zooid-dynamics in two coral genera.Ecological Informatics, page 103293, 2025.
- [5]Gergely Ambrus and Dancsó Dorottya.Soft tilings.arXiv preprint, https://arxiv.org/abs/2604.18545, 2026.
- [6]G. Domokos, A. Goriely, Á. G. Horváth, and K. Regős.Soft cells, Kelvin’s foam and the minimal surfaces of Schwarz.arXiv preprint, page https://arxiv.org/abs/2412.04491, 2025.
- [7]Allen Hatcher.Algebraic Topology.Cambridge University Press, 2002.
- [8]B. Grünbaum and G.C. Shepard.Tilings and Patterns.Freeman and Co., New York, 1987.
- [9]H. P. Robertson.Kinematics and world-structure.Astrophysical Journal, 82:284–301, 1935.
- [10]A. G. Walker.On milne’s theory of world-structure.Proceedings of the London Mathematical Society, 42:90–127,
1937.
- [11]P. J. E. Peebles.The Large–Scale Structure of the Universe.Princeton University Press, 1980.
- [12]M. Davis and P. J. E. Peebles.A survey of galaxy redshifts. v. the two–point position and
velocity correlations.The Astrophysical Journal, 267:465–482, 1983.
- [13]T. D. Kitching et al.3d weak lensing with the cfhtlens tomographic data.Monthly Notices of the Royal Astronomical Society,
442:1326–1349, 2014.
- [14]A. F. Heavens and A. N. Taylor.A spherical analysis of redshift–space distortions.Monthly Notices of the Royal Astronomical Society,
276:L59–L63, 1995.
- [15]K. B. Fisher, A. F. Heavens, and A. N. Taylor.Spherical harmonic analysis of galaxy redshift surveys.Monthly Notices of the Royal Astronomical Society,
276:885–907, 1995.
- [16]G. Domokos, A. G. Horváth, and K. Regős.A two-vertex theorem for normal tilings.Aequationes Math., 97:185–193, 2023.

## 


- 


Major funding support from
