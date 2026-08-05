# New class of exactly flat topological bands - compact localised states protected by local graph topology

**arXiv ID**: 2607.22831v1
**Authors**: Tamaghna Hazra
**Published**: 2026-07-24
**Categories**: cond-mat.str-el, cond-mat.dis-nn, cond-mat.mtrl-sci, math-ph, quant-ph
**Comments**: 19 pages main text, 8 figures, 1 appendix. Comments welcome and will be gratefully acknowledged upon submission
**HTML URL**: https://arxiv.org/html/2607.22831v1

## Abstract

Strongly correlated quantum matter is fundamentally defined by the tension between non-commuting quantum operators. Hamiltonians exhibiting macroscopic degeneracies are of general interest in this field because they imply an infinite susceptibility to any non-commuting perturbation. In moiré heterostructures, engineering such extensive degeneracies in the kinetic Hamiltonian creates a fertile garden for exotic strongly correlated phases of matter to emerge from the resulting flat bands. Here, we introduce a prescription to construct an infinite family of exact flat band Hamiltonians supported on the faces of arbitrary graphs. We demonstrate this algorithm on the faces of four Bravais lattices. Using a discrete graph generalization of the Atiyah-Singer index theorem, we prove that the extensive degeneracies of such face-graph Hamiltonians are protected by the local topology of the face-graph connectivity. The resulting macroscopic null spaces yield compact localised states that remain localised over time due to frustration in hopping pathways. We discuss the broad implications of such non-dispersing quantum modes in diverse settings, from arrested dynamics in quantum networks and quantum machine learning algorithms to Majorana-free topological quantum computation.

## Full Text

Abstract

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
- License: CC BY-NC-SA 4.0arXiv:2607.22831v1 [cond-mat.str-el] 24 Jul 2026

New class of exactly flat topological bands - compact localised states protected by local graph topology

Tamaghna Hazra

Institute for Theory of Condensed Matter, Karlsruhe Institute of Technology, Kaiserstrasse 12, Karlsruhe 76131, Germany

## Abstract

Strongly correlated quantum matter is fundamentally defined by the tension between non-commuting quantum operators. Hamiltonians exhibiting macroscopic degeneracies are of general interest in this field because they imply an infinite susceptibility to any non-commuting perturbation. In moiré heterostructures, engineering such extensive degeneracies in the kinetic Hamiltonian creates a fertile garden for exotic strongly correlated phases of matter to emerge from the resulting flat bands. Here, we introduce a prescription to construct an infinite family of exact flat band Hamiltonians supported on the faces of arbitrary graphs. We demonstrate this algorithm on the faces of four Bravais lattices. Using a discrete graph generalization of the Atiyah-Singer index theorem, we prove that the extensive degeneracies of such face-graph Hamiltonians are protected by the local topology of the face-graph connectivity. The resulting macroscopic null spaces yield compact localised states that remain localised over time due to frustration in hopping pathways. We discuss the broad implications of such non-dispersing quantum modes in diverse settings, from arrested dynamics in quantum networks and quantum machine learning algorithms to Majorana-free topological quantum computation.

Copyright attribution to authors.
This work is a submission to SciPost Physics.
License information to appear upon publication.
Publication information to appear upon publication.Received Date
Accepted Date
Published Date

## 
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

## 1Introduction

The mathematical guarantee of extended degeneracies in positive semi-definite matrices has direct implications across multiple scientific and computational disciplines. When a linear operator onℝN\mathbb{R}^{N}is constructed in the formBT​BB^{T}B(orB†​BB^{\dagger}Bfor operators onℂN\mathbb{C}^{N}), where the domain and range of the operatorBBhave dimensionmmandnnrespectively, the rank-nullity theorem dictates that the dimension of the null space is atleast the differencem−nm-n. If this difference scales with the system size, this results in an extensive degeneracy in the eigenspectrum independent of any microscopic details of the system under consideration.

In condensed matter physics, such macroscopic degeneracies of the Hamiltonian operator that describes the kinetic energy of electrons results in flat electronic bands, prominent examples include Landau levels and flat bands in medial lattices like the Kagome lattice and subdivided graphs like the Lieb lattice[landau1930,lieb1989,vonklitzing1986,mielkeFerromagnetismHubbardmodel1991,tasakiFerromagnetismHubbardModels1992,tasakiPhysicsMathematicsQuantum2020]. The complete quenching of kinetic energy in these bands causes electron-electron interactions to dominate the low energy physics, providing a natural platform for various strongly correlated phases of matter, such as unconventional superconductivity, Wigner crystals, strange metals, and fractionalized topological phases. In recent years, there has been a resurgence in such flat bands following the discovery of moire heterostructures[li2010,caoCorrelatedInsulatorBehaviour2018,caoUnconventionalSuperconductivityMagicangle2018]where different layers of two-dimensional materials are placed in contact with a relative twist. The resulting moire superlattice has a large spatial periodicity and consequently narrow bands that can be tuned by the relative twist angle. Many novel strongly correlated phases of matter have been discovered in these platforms[andrei2020,andrei2021,mak2022a,nuckolls2024a,mellado2025], including a fractional quantum hall state at zero magnetic field[cai2023,zeng2023,xu2023,lu2024a]. This work introduces a prescription to engineer an infinite family of such flat band Hamiltonians of the formBT​BB^{T}B, supported on arbitrary lattices, by interpreting the hitherto abstract operatorBBas the incidence matrix of the faces of the lattice on its vertices.

The topology of the positive semi-definite formBT​BB^{T}Band its macroscopic null-space have profound consequences beyond standard band theory. For instance, this incidence matrix structure governs the dynamical matrices of isostatic mechanical networks, where the null space identifies the number of topologically protected, zero-frequency floppy modes[kane2014]. The same incidence matrix structure has been exploited[roychowdhury2024]to provide fresh perspectives on lattice models for supersymmetry[rana1993,fendley2003]. The connection of the macroscopic nullspace to the local topology of graph connectivity was first pointed out by Sutherland[sutherland1986]and later interpreted[roychowdhury2024]as a discrete lattice analogue of the Witten index[witten1982constraints]. Quite generally, frustration-free Hamiltonians of the formB†​BB^{\dagger}Bhave a long history as exactly solvable points of a wide variety of strongly correlated systems, from frustrated magnetism to Fractional Quantum Hall phases[arovas1992,ardonneTopologicalOrderConformal2004]. More recently[tan2025], extensive degeneracies in the many-body eigenspectrum of kinetically constrained models of various origins have been discussed as a novel form of eigenstate order[ben-amiManybodyCagesDisorderfree2025], variously dubbed as glasses, scars, cages and collective bound states by different groups[ben-amiManybodyCagesDisorderfree2025,tan2025,jonay2026,mohapatra2026,nicolau2026,hazra2026]. These extensive many-body degeneracies have been demonstrated to originate from compact localized states in the many-body transition graph, mapping directly to the single-particle flat bands of a fictitious particle hopping on the transition graph[tan2025].

These compact localised states have been discussed as eigenmodes of line-graphs and subdivided graphs of a an arbitray root graph[leykam2018,kollarLineGraphLatticesEuclidean2020], leading to a family of models like the Kagome lattice and the Lieb lattice with exactly flat bands. Here we present a prescription to construct a family of models on the faces of an arbitrary graph, as defined in Section2, that have exactly flat bands and an extensive degeneracy of compact localized states when the number of faces|F||F|exceeds the number of vertices|V||V|. This framework extends straightforwardly from faces of a graph to arbitrarykk-cells in a CW complex defined on the root graph or any of the derivative graphs. The known results on line-graphs are understood as thek=1k=1case of a infinite family of flat band models. In Section3, we demonstrate this prescription on the simplest case of the nearest-neighbour (NN) graph of a cubic lattice. In Section4, we generalize to an arbitrary graph whose faces have the same coordination (triangles or rectangles). In Section5, we demonstrate the application to the NN graph of the simple hexagonal lattice, which has both triangular and rectangular faces. In Section6, we generalize to an arbitrary graph with such a heterogenous face set, and discuss the compact localized states. In Section7, we connect the extensive degeneracy of face-graph adjacency matrices to topological index which is a discrete version of the Atiyah-Singer index, rigorously establishing that the compact localized states in the bulk of the face-graph are protected by the local topology of the graph connectivity. Finally, in Section8, we discuss the broad-ranging implications of such compact localized states for quantum algorithms, disordered quantum networks, many-body quantum dynamics and a potentially new route to topologically protected quantum information without Majorana fermions or Majorana bound states.

## 2Defining the Faces of an Arbitrary Graph

Before exploring the consequences of hopping models on face-graphs, we need an unambiguous definition of what constitutes a "face" in an abstract graphG​(V,E)G(V,E). In regular lattices, faces are intuitively identified as the elementary plaquettes that geometrically tile 3D voids. For an arbitrary graph, we define the facesFFof the graph as the set of its relevant cycles, which is identical to the set of its irreducible cycles[vismara1997]. Physically, an irreducible cycle is simply a contiguous sequence of edges that cannot be expressed as a modulo-2 sum of shorter cycles. Thus defined, the face-set can be enumerated in polynomial time[horton1987,vismara1997,kavitha2009], and individual faces of an arbitrary graph can be identified from the local edge-connectivity. To verify if a candidate cycle is a face, one only needs to search its immediate structural neighborhood to verify that it cannot be decomposed into a modulo-2 sum of shorter cycles. For example, in the Face-Centered Cubic (FCC) lattice in Fig.3, an equatorial square of the octahedral void isreduciblebecause it can be decomposed into four shorter triangles that share the apex of the octahedron; therefore, it is not a face.
Note that this definition of a face is not unique, but this is the one that we will use for demonstration in the next four sections. Other definitions yield distinct face-graphs, which also have extensive degeneracies. In AppendixA, we use physical intuition to motivate our definition of a face of a graph.

## 3Tight binding model on the faces of a cubic lattice

In this section, we demonstrate the prescription to generate exact
flat bands for hopping between faces of a simple cubic lattice. We
generalize the line-graph construction to the corner-sharing face-graphs
and edge-sharing face-graphs and show that on very general grounds
hopping on these graphs leads to multiply-degenerate exactly-flat
bands.

Consider the graphG​(E,V)G(E,V)defined with the verticesVVbeing
the sites of a simple cubic lattice and the edgesEEbeing the nearest
neighbour links. The facesFFof this graph are the regions
bounded by an elementary induced cycle - a contiguous series of edges that cannot
be divided into smaller cycles111LetCn=(v1,v2,…,vn,v1)C_{n}=(v_{1},v_{2},\dots,v_{n},v_{1})be a cycle of lengthnninGG. The cycleCnC_{n}defines a face if and only if there
are no edges inEEconnecting any two non-adjacent vertices inCnC_{n}.. We define the face-vertex incidence matrix byBv​f=1B_{vf}=1if the
vertexvvis an element of this cycle andBv​f=0B_{vf}=0otherwise.
For a simple cubic lattice with|V|=N|V|=Nvertices and|F|=3​N|F|=3Nfaces,BBis anN×3​NN\times 3Nmatrix. We then consider the positive semi-definite
matrixBT​BB^{T}Bwhich counts the number of shared vertices between
any two faces:(BT​B)f1,f2=∑v∈VBv,f1​Bv,f2(B^{T}B)_{f_{1},f_{2}}=\sum_{v\in V}B_{v,f_{1}}B_{v,f_{2}}(1)

Since the rank of the rectangular incidence matrixBB(and hence
ofBT​BB^{T}B) is at most|V||V|when|F|>|V||F|>|V|, the rank-nullity
theorem𝒩=dim−rank\mathcal{N}={\rm dim}-{\rm rank}dictatesBT​BB^{T}Bhas
a null-space of dimension𝒩=|F|−|V|\mathcal{N}=|F|-|V|. Following Mielke[mielkeFerromagnetismHubbardmodel1991],
we decompose this operator into its diagonal and off-diagonal components
as:BT​B=4​I+2​Aedge+AcornerB^{T}B=4I+2A_{\text{edge}}+A_{\text{corner}}(2)

where the diagonal term counts the 4 corners of the square faces andAedgeA_{\text{edge}}andAcornerA_{\text{corner}}are the adjacency matrices
for the edge-sharing face-graph and corner-sharing face-graph, respectively.
Thus the Hamiltonian obtained by scaling this matrix with a positive
hopping amplitudet>0t>0,H=2​t​Aedge+t​Acorner=t​(BT​B−4​I)H=2tA_{\text{edge}}+tA_{\text{corner}}=t(B^{T}B-4I)(3)

realizes a extensive2​N2N-fold ground-state degeneracy, corresponding
to 2 flat bands atE=−4​tE=-4t. These bands are exactly flat by construction.
Physically, this represents orbital degrees of freedom (bosonic or
fermionic) supported on they​zyz,z​xzxandx​yxyfaces of the cubic
lattice that can hop to their edge-sharing neighbours with twice the
probability amplitude that they can hop to their corner-sharing neighbours.

## 3.1Basis Elements and Face-Graph Adjacency Matrices

To construct the momentum-space HamiltonianH=∑𝐤H​(𝐤)H=\sum_{\bf k}H({\bf k}), we first define the basis elements for the vector space of faces and vertices. Let the vertices of the simple cubic lattice be located at integer coordinates𝐑∈ℤ3\mathbf{R}\in\mathbb{Z}^{3}. The basis for the vertex vector space is given by the localized states|𝐑⟩|\mathbf{R}\rangle. The facesff(∈{x,y,z}\mu\in\{x,y,z\}) are centered at half-integer coordinates. For instance, thexx-faces are centered at𝐑+12​y^+12​z^\mathbf{R}+\frac{1}{2}\hat{y}+\frac{1}{2}\hat{z}, and we denote their basis states as|fx,𝐑⟩|f_{x,\mathbf{R}}\rangle.

We define the corresponding Bloch wavefunctions using a Fourier transform:|v𝐤⟩\displaystyle|v_{\mathbf{k}}\rangle=1N​∑𝐑ei​𝐤⋅𝐑​|𝐑⟩\displaystyle=\frac{1}{\sqrt{N}}\sum_{\mathbf{R}}e^{i\mathbf{k}\cdot\mathbf{R}}|\mathbf{R}\rangle(4)|f,𝐤⟩\displaystyle|f_{\mu,\mathbf{k}}\rangle=1N​∑𝐑ei​𝐤⋅(𝐑+𝐫)​|f,𝐑⟩\displaystyle=\frac{1}{\sqrt{N}}\sum_{\mathbf{R}}e^{i\mathbf{k}\cdot(\mathbf{R}+\mathbf{r})}|f_{\mu,\mathbf{R}}\rangle(5)

where𝐫x=12​(y^+z^)\mathbf{r}_{x}=\frac{1}{2}(\hat{y}+\hat{z}),𝐫y=12​(x^+z^)\mathbf{r}_{y}=\frac{1}{2}(\hat{x}+\hat{z}), and𝐫z=12​(x^+y^)\mathbf{r}_{z}=\frac{1}{2}(\hat{x}+\hat{y})are the relative centers of the faces within the unit cell.

With this symmetric gauge choice in the Bloch basis, we can block-diagonalize the edge-sharing adjacency matrixAedge=∑𝐤Aedge​(𝐤)A_{\text{edge}}=\sum_{\bf k}A_{\text{edge}}(\mathbf{k})and the corner-sharing adjacency matrixAcorner=∑𝐤Acorner​(𝐤)A_{\text{corner}}=\sum_{\bf k}A_{\text{corner}}(\mathbf{k}). For the diagonal elements (intra-orbital hopping), coplanar faces of the same orientation share edges along two axes and corners along the face diagonals (See Fig.1(a)), leading to[Aedge​(𝐤)]\displaystyle[A_{\text{edge}}(\mathbf{k})]=2​(cos⁡k+cos⁡k)\displaystyle=2(\cos k+\cos k)(6)[Acorner​(𝐤)]\displaystyle[A_{\text{corner}}(\mathbf{k})]=4​cos⁡k​cos⁡k\displaystyle=4\cos k\cos k(7)

where(,,)(\mu,\nu,\lambda)is a permutation of(x,y,z)(x,y,z).xxyy(a)Intra-orbital hopping (zz-face tozz-face)xxyyzz(b)Inter-orbital hopping (zz-face toxx-face)Figure 1:Illustration of hopping processes. (a) Intra-orbital hoppings between coplanarzz-faces. Edge-sharing hoppings (solid dark blue arrows) have amplitude2​t2t, while corner-sharing hoppings (dashed dark green arrows) have amplitudett. (b) Inter-orbital hoppings between an orthogonalzz-face andxx-faces, exhibiting analogous edge- and corner-sharing amplitudes.

For the off-diagonal elements (inter-orbital hopping), orthogonal faces share a single edge along their intersecting axis, while corner-sharing orthogonal faces are displaced along the remaining spatial dimension (See Fig.1(b)), leading to[Aedge​(𝐤)]\displaystyle[A_{\text{edge}}(\mathbf{k})]=4​cos⁡k2​cos⁡k2\displaystyle=4\cos\frac{k}{2}\cos\frac{k}{2}(8)[Acorner​(𝐤)]\displaystyle[A_{\text{corner}}(\mathbf{k})]=8​cos⁡k​cos⁡k2​cos⁡k2\displaystyle=8\cos k\cos\frac{k}{2}\cos\frac{k}{2}(9)

with≠≠\mu\neq\nu\neq\lambda.

## 3.2Total Hamiltonian and Incidence Matrix

Summing these components according toH​(𝐤)=t​(2​Aedge​(𝐤)+Acorner​(𝐤))H(\mathbf{k})=t(2A_{\text{edge}}(\mathbf{k})+A_{\text{corner}}(\mathbf{k}))provides the full tight-binding Hamiltonian. For instance, the diagonal elements evaluate to4​t​(cos⁡ky+cos⁡kz+cos⁡ky​cos⁡kz)4t(\cos k_{y}+\cos k_{z}+\cos k_{y}\cos k_{z}), which can be rewritten as:4​t​(cos⁡ky+cos⁡kz+cos⁡ky​cos⁡kz)\displaystyle 4t(\cos k_{y}+\cos k_{z}+\cos k_{y}\cos k_{z})=4​t​((1+cos⁡ky)​(1+cos⁡kz)−1)\displaystyle=4t\left((1+\cos k_{y})(1+\cos k_{z})-1\right)=16​t​(cos2⁡ky2​cos2⁡kz2−14)\displaystyle=16t\left(\cos^{2}\frac{k_{y}}{2}\cos^{2}\frac{k_{z}}{2}-\frac{1}{4}\right)(10)

By applying this to all diagonal elements, we assemble the full tight-binding Hamiltonian:H​(𝐤)=16​t​(cos2⁡ky2​cos2⁡kz2−14cos⁡kx2​cos⁡ky2​cos2⁡kz2cos⁡kx2​cos2⁡ky2​cos⁡kz2cos⁡kx2​cos⁡ky2​cos2⁡kz2cos2⁡kx2​cos2⁡kz2−14cos2⁡kx2​cos⁡ky2​cos⁡kz2cos⁡kx2​cos2⁡ky2​cos⁡kz2cos2⁡kx2​cos⁡ky2​cos⁡kz2cos2⁡kx2​cos2⁡ky2−14)H(\mathbf{k})=16t\begin{pmatrix}\cos^{2}\frac{k_{y}}{2}\cos^{2}\frac{k_{z}}{2}-\frac{1}{4}&\cos\frac{k_{x}}{2}\cos\frac{k_{y}}{2}\cos^{2}\frac{k_{z}}{2}&\cos\frac{k_{x}}{2}\cos^{2}\frac{k_{y}}{2}\cos\frac{k_{z}}{2}\\
\cos\frac{k_{x}}{2}\cos\frac{k_{y}}{2}\cos^{2}\frac{k_{z}}{2}&\cos^{2}\frac{k_{x}}{2}\cos^{2}\frac{k_{z}}{2}-\frac{1}{4}&\cos^{2}\frac{k_{x}}{2}\cos\frac{k_{y}}{2}\cos\frac{k_{z}}{2}\\
\cos\frac{k_{x}}{2}\cos^{2}\frac{k_{y}}{2}\cos\frac{k_{z}}{2}&\cos^{2}\frac{k_{x}}{2}\cos\frac{k_{y}}{2}\cos\frac{k_{z}}{2}&\cos^{2}\frac{k_{x}}{2}\cos^{2}\frac{k_{y}}{2}-\frac{1}{4}\end{pmatrix}(11)

To write the face-vertex incidence matrixB​(𝐤)B(\mathbf{k})in the Bloch basis, we maintain the same symmetric gauge choice defined in the previous subsection. The incidence matrix elementsB​(𝐤)=⟨v𝐤|B^|f,𝐤⟩B(\mathbf{k})=\langle v_{\mathbf{k}}|\hat{B}|f_{\mu,\mathbf{k}}\rangleconnect a face to its four bounding vertices. For thexx-faces, the four vertices are displaced from the face center by±12​y^±12​z^\pm\frac{1}{2}\hat{y}\pm\frac{1}{2}\hat{z}. This yields the momentum-space incidence vectorB(𝐤)=[(𝐤)x,(𝐤)y,(𝐤)z]B(\mathbf{k})=[{}_{x}(\mathbf{k}),{}_{y}(\mathbf{k}),{}_{z}(\mathbf{k})], where:(𝐤)x\displaystyle{}_{x}(\mathbf{k})=4​cos⁡ky2​cos⁡kz2\displaystyle=4\cos\frac{k_{y}}{2}\cos\frac{k_{z}}{2}(12)(𝐤)y\displaystyle{}_{y}(\mathbf{k})=4​cos⁡kx2​cos⁡kz2\displaystyle=4\cos\frac{k_{x}}{2}\cos\frac{k_{z}}{2}(13)(𝐤)z\displaystyle{}_{z}(\mathbf{k})=4​cos⁡kx2​cos⁡ky2\displaystyle=4\cos\frac{k_{x}}{2}\cos\frac{k_{y}}{2}(14)

from which it is easy to identify the HamiltonianH​(𝐤)=t​(2xyxzxxy2yzyxzyz2z)​(𝐤)−4​t=t​(B†​(𝐤)​B​(𝐤)−4​I)H(\mathbf{k})=t\begin{pmatrix}{}_{x}^{2}&{}_{x}{}_{y}&{}_{x}{}_{z}\\
{}_{y}{}_{x}&{}_{y}^{2}&{}_{y}{}_{z}\\
{}_{z}{}_{x}&{}_{z}{}_{y}&{}_{z}^{2}\end{pmatrix}({\bf k})-4t=t(B^{\dagger}(\mathbf{k})B(\mathbf{k})-4I)(15)

as expected from the general construction above.

## 3.3Band Structure and the -Point Eigenvectors

BecauseB†​BB^{\dagger}Bis an outer product of a vector with itself, it has rank 1. Thus, for every momentum𝐤\mathbf{k}, the matrixB†​(𝐤)​B​(𝐤)B^{\dagger}(\mathbf{k})B(\mathbf{k})has exactly two zero eigenvalues and one non-zero eigenvalue given by|B(𝐤)|2=||2x+||2y+||2z|B(\mathbf{k})|^{2}=|{}_{x}|^{2}+|{}_{y}|^{2}+|{}_{z}|^{2}.

Consequently,H​(𝐤)H(\mathbf{k})features two strictly flat bands pinned at energyE=−4​tE=-4t, and one dispersive bandE(𝐤)=t(||2x+||2y+||2z−4)E(\mathbf{k})=t(|{}_{x}|^{2}+|{}_{y}|^{2}+|{}_{z}|^{2}-4).

At the -point (𝐤=0\mathbf{k}=0), we have=x=y=z4{}_{x}={}_{y}={}_{z}=4. The incidence vector isB​(0)=[4,4,4]B(0)=[4,4,4]. The eigenvectors of the flat bands|⟩flat=(ux,uy,uz)T|{}_{\text{flat}}\rangle=(u_{x},u_{y},u_{z})^{T}must satisfyB(0)|⟩flat=0B(0)|{}_{\text{flat}}\rangle=0, which yields the condition:ux+uy+uz=0u_{x}+u_{y}+u_{z}=0(16)

This symmetric equation defines the two-dimensional null space at the -point.

## 3.4Compact Localized States and real-space topology

The degenerate manifold of flat band eigenstates can be spanned by entirely real-space localized wavefunctions, known as Compact Localized States (CLSs), augmented by localized states which wind around the 3-torus, as in flat bands in line graphs[bergman2008,maimaiti2017,maimaiti2021,kollarLineGraphLatticesEuclidean2020].

We demonstrate the minimal wavefunctions defined on three faces in the unit-cell at the origin|fx,𝟎⟩,|fy,𝟎⟩,|fz,𝟎⟩|f_{x,\mathbf{0}}\rangle,|f_{y,\mathbf{0}}\rangle,|f_{z,\mathbf{0}}\rangle. To satisfy the destructive interference condition, there is one state that has an opposite sign on thexxandyyfaces (and zero amplitude on thezzface):|⟩CLS,1=|fx,𝟎⟩−|fy,𝟎⟩|{}_{\text{CLS,1}}\rangle=|f_{x,\mathbf{0}}\rangle-|f_{y,\mathbf{0}}\rangle(17)

There are two others related to it by symmetry:|⟩CLS,2=|fy,𝟎⟩−|fz,𝟎⟩|{}_{\text{CLS,2}}\rangle=|f_{y,\mathbf{0}}\rangle-|f_{z,\mathbf{0}}\rangleand|⟩CLS,3=|fz,𝟎⟩−|fx,𝟎⟩|{}_{\text{CLS,3}}\rangle=|f_{z,\mathbf{0}}\rangle-|f_{x,\mathbf{0}}\rangle. Of these three symmetric states, only two are linearly independent (since|⟩1+|⟩2+|⟩3=0|{}_{1}\rangle+|{}_{2}\rangle+|{}_{3}\rangle=0), precisely reflecting the two-fold macroscopic degeneracy of the flat bands.

## 4Generalization to arbitrary homogeneous face-graphs

This derivation extends naturally to any cell complex defined by the verticesVV, edgesEE(specified as pairs of vertices) and facesFF(specified by cycles on the graphG​(V,E)G(V,E))222Formally we can consider a topological space with dimensionk≥2k\geq 2, with the skeletaX0,X1,X2X^{0},X^{1},X^{2}corresponding to the setsV,E,FV,E,F. Alternatively, we can consider a face poset with the ground setP=V∪E∪FP=V\cup E\cup Fand the covering relations encoding the face-edge and edge-vertex incidences.,
assuming every face hasppvertices. The vertex-face incidence matrixBBis a|V|×|F||V|\times|F|matrix333Formally,BBis an unoriented bi-adjacency matrix. In a topological space, it is extracted from the integer matrix representationsB1B_{1}andB2B_{2}of the standard boundary operators∂n\partial_{n}asB=12​|B1|​|B2|B=\frac{1}{2}|B_{1}||B_{2}|. Alternatively, when the cell complex is structured as a face poset,BBencodes the transitive closure of the covering relations, with elementsBv,f=1B_{v,f}=1if the relationv<fv<fholds.and thereforeBT​BB^{T}Bis an|F|×|F||F|\times|F|matrix with rank at-most|F||F|and nullity atleast|F|−|V||F|-|V|.

Thus the face-graph hopping Hamiltonian defined asH=t​(BT​B−p​I)H=t(B^{T}B-pI)by removing the diagonal entries is guaranteed to have a|F|−|V||F|-|V|-fold ground state degeneracy whent>0t>0. Note that this extensive degeneracy does not require a regular crystal lattice. When the cell complex has discrete translation symmetry,HHis guaranteed to have exact flat bands atE=−p​tE=-ptwhereppis the degree of the faces. For the simple cubic lattice,|F|=3​N|F|=3Nand|V|=N|V|=N, guaranteeing at least 2 flat bands as we found in Sec.3.3. For demonstration, we show the flat bands in the cubic, FCC and BCC lattices below (see Appendix for details). All the other 3D Bravais lattices can also be similarly shown to generate flat bands on the face-graph hopping Hamiltonian defined herein, except the hexagonal lattice which we discuss next.Figure 2:Bandstructure of the hopping Hamiltonian defined on the faces of a cubic latticeFigure 3:8 distinct classes of faces of an FCC lattice, shown in the conventional unit cellFigure 4:Bandstructure of the hopping Hamiltonian defined on the faces of an FCC latticeFigure 5:6 distinct faces of a BCC lattice, shown in the conventional unit cellFigure 6:Bandstructure of the hopping Hamiltonian defined on the faces of a BCC lattice

## 5Tight binding model of the faces of a simple hexagonal lattice

We consider a three-dimensional simple hexagonal lattice defined by primitive vectors𝐚1=(1,0,0)\mathbf{a}_{1}=(1,0,0),𝐚2=(1/2,3/2,0)\mathbf{a}_{2}=(1/2,\sqrt{3}/2,0), and𝐚3=(0,0,c)\mathbf{a}_{3}=(0,0,c). A single primitive unit cell contains 1 vertex centered at the origin,𝐫v=(0,0,0)\mathbf{r}_{v}=(0,0,0), and 5 elementary faces (See Fig.7): 2 triangles on the basal planes (|t1⟩,|t2⟩|t_{1}\rangle,|t_{2}\rangle) centered at𝐫t​1=−13​(𝐚1+𝐚2)\mathbf{r}_{t1}=-\frac{1}{3}(\mathbf{a}_{1}+\mathbf{a}_{2})and𝐫t​2=13​(𝐚1+𝐚2)\mathbf{r}_{t2}=\frac{1}{3}(\mathbf{a}_{1}+\mathbf{a}_{2}), and 3 rectangles forming the vertical prism walls (|r1⟩,|r2⟩,|r3⟩|r_{1}\rangle,|r_{2}\rangle,|r_{3}\rangle) centered at𝐫r​1=12​(𝐚1+𝐚3)\mathbf{r}_{r1}=\frac{1}{2}(\mathbf{a}_{1}+\mathbf{a}_{3}),𝐫r​2=12​(𝐚2+𝐚3)\mathbf{r}_{r2}=\frac{1}{2}(\mathbf{a}_{2}+\mathbf{a}_{3}), and𝐫r​3=12​(𝐚1−𝐚2+𝐚3)\mathbf{r}_{r3}=\frac{1}{2}(\mathbf{a}_{1}-\mathbf{a}_{2}+\mathbf{a}_{3}). The presence of a heterogeneous face set, 3-cycles and 4-cycles makes this case fundamentally different from the previous cases where all the faces had the same degree.Figure 7:5 distinct faces of a simple hexagonal lattice, shown in the conventional unit cell

Consider the real-space HamiltonianH^=t​BT​B\hat{H}=tB^{T}B, whereBBis the full face-vertex incidence matrix. By construction, it has a nullspace of degree|F|−|V|=4​N|F|-|V|=4N. This Hamiltonian can be separated into a diagonalD^\hat{D}that counts the number of vertices incident on a given face and an off-diagonal part representing hopping on the corner-sharing and edge-sharing face graphs as before:H^=D^+t​(Acorner+2​Aedge).\hat{H}=\hat{D}+t(A_{\text{corner}}+2A_{\text{edge}}).(18)

Because the face set has mixed degree, the diagonal matrixD^\hat{D}is not proportional to the identity, which means that the off-diagonal part does not necessarily inherit the full nullspace ofB†​BB^{\dagger}B. The hopping Hamiltonian can be explicitly partitioned into a homogeneous triangle-to-triangle sectorH^T\hat{H}_{T}, a rectangle-to-rectangle sectorH^R\hat{H}_{R}, and a bipartite cross-term sectorH^T​R\hat{H}_{TR}.H^\displaystyle\hat{H}=D^+H^T+H^R+H^T​R\displaystyle=\hat{D}+\hat{H}_{T}+\hat{H}_{R}+\hat{H}_{TR}(19)H^T\displaystyle\hat{H}_{T}=t​(AcornerT+2​AedgeT)\displaystyle=t(A^{T}_{\text{corner}}+2A^{T}_{\text{edge}})(20)H^R\displaystyle\hat{H}_{R}=t​(AcornerR+2​AedgeR)\displaystyle=t(A^{R}_{\text{corner}}+2A^{R}_{\text{edge}})(21)H^T​R\displaystyle\hat{H}_{TR}=t​(AcornerT​R+2​AedgeT​R).\displaystyle=t(A^{TR}_{\text{corner}}+2A^{TR}_{\text{edge}}).(22)

The homogeneous sub-graph HamiltoniansH^T\hat{H}_{T}andH^R\hat{H}_{R}can be identified as having the familiar structureH^T\displaystyle\hat{H}_{T}=t​(BTT​BT−3)\displaystyle=t(B_{T}^{T}B_{T}-3)(23)H^R\displaystyle\hat{H}_{R}=t​(BRT​BR−4)\displaystyle=t(B_{R}^{T}B_{R}-4)(24)

whereBTB_{T}andBRB_{R}are the face-vertex incidence matrices of the homogeneous sub-sets of faces with dimensionsN×2​NN\times 2NandN×3​NN\times 3Nrespectively. These incidence matrices mathematically guaranteeNN- and2​N2N-fold degenerate macroscopic flat bands atE=−3​tE=-3tandE=−4​tE=-4t, respectively. This accounts for 3 of the 4 flat bands of the full HamiltonianH^=t​BT​B\hat{H}=tB^{T}B, the remaining flat band arises for frustrated hopping between the triangular and rectangular faces, and will be discussed in Sec.5.2.

## 5.1Explicit momentum-space Hamiltonian and flat bands

The momentum-space basis functions are explicitly defined as the Bloch wave functions of the orbitals supported on each of the five elementary faces:(|t1⟩,|t2⟩,|r1⟩,|r2⟩,|r3⟩)(|t_{1}\rangle,|t_{2}\rangle,|r_{1}\rangle,|r_{2}\rangle,|r_{3}\rangle). In this basis, we construct the momentum-space face-vertex incidence vectorB~​(𝐤)\tilde{B}(\mathbf{k})using a symmetric gauge, as in Sec.3.2. Definingki=𝐤⋅𝐚ik_{i}=\mathbf{k}\cdot\mathbf{a}_{i}, the symmetric Fourier sums over the vertices of each face relative to its center yield:~t​1​(𝐤)\displaystyle\tilde{\gamma}_{t1}(\mathbf{k})≡(𝐤)=ei​k1+k23+ei​−2​k1+k23+ei​k1−2​k23\displaystyle\equiv\Delta(\mathbf{k})=e^{i\frac{k_{1}+k_{2}}{3}}+e^{i\frac{-2k_{1}+k_{2}}{3}}+e^{i\frac{k_{1}-2k_{2}}{3}}(25)~t​2​(𝐤)\displaystyle\tilde{\gamma}_{t2}(\mathbf{k})=(𝐤)∗\displaystyle={}^{*}(\mathbf{k})(26)~r​1​(𝐤)\displaystyle\tilde{\gamma}_{r1}(\mathbf{k})=4​cos⁡(k12)​cos⁡(k32)\displaystyle=4\cos\left(\frac{k_{1}}{2}\right)\cos\left(\frac{k_{3}}{2}\right)(27)~r​2​(𝐤)\displaystyle\tilde{\gamma}_{r2}(\mathbf{k})=4​cos⁡(k22)​cos⁡(k32)\displaystyle=4\cos\left(\frac{k_{2}}{2}\right)\cos\left(\frac{k_{3}}{2}\right)(28)~r​3​(𝐤)\displaystyle\tilde{\gamma}_{r3}(\mathbf{k})=4​cos⁡(k1−k22)​cos⁡(k32)\displaystyle=4\cos\left(\frac{k_{1}-k_{2}}{2}\right)\cos\left(\frac{k_{3}}{2}\right)(29)

We partition the momentum-space incidence vector into two sub-vectors,BT​(𝐤)B_{T}(\mathbf{k})andBR​(𝐤)B_{R}(\mathbf{k}), corresponding to the triangular (p=3p=3) and rectangular (q=4q=4) faces respectively:B~​(𝐤)=[BT​(𝐤)BR​(𝐤)]=[∗~r​1~r​2~r​3].\tilde{B}(\mathbf{k})=\begin{bmatrix}B_{T}(\mathbf{k})&B_{R}(\mathbf{k})\end{bmatrix}=\begin{bmatrix}\Delta&{}^{*}&\vline&\tilde{\gamma}_{r1}&\tilde{\gamma}_{r2}&\tilde{\gamma}_{r3}\end{bmatrix}.(30)

The momentum-space hopping Hamiltonian is constructed as the outer productH​(𝐤)=t​B~†​(𝐤)​B~​(𝐤)H(\mathbf{k})=t\tilde{B}^{\dagger}(\mathbf{k})\tilde{B}(\mathbf{k}). Utilizing the partitioned incidence vectorsBT​(𝐤)B_{T}(\mathbf{k})andBR​(𝐤)B_{R}(\mathbf{k}), the Hamiltonian naturally inherits the block structure established in real space:H​(𝐤)=t​(BT†​(𝐤)​BT​(𝐤)BT†​(𝐤)​BR​(𝐤)BR†​(𝐤)​BT​(𝐤)BR†​(𝐤)​BR​(𝐤)).H(\mathbf{k})=t\begin{pmatrix}B_{T}^{\dagger}(\mathbf{k})B_{T}(\mathbf{k})&B_{T}^{\dagger}(\mathbf{k})B_{R}(\mathbf{k})\\
B_{R}^{\dagger}(\mathbf{k})B_{T}(\mathbf{k})&B_{R}^{\dagger}(\mathbf{k})B_{R}(\mathbf{k})\end{pmatrix}.(31)

This block matrix explicitly demonstrates the Fourier-space counterparts of the homogeneous and bipartite sectors. The diagonal blocks correspond to the homogeneous face-graph Hamiltonians shifted by their respective degrees:HT​(𝐤)\displaystyle H_{T}(\mathbf{k})=t​(BT†​(𝐤)​BT​(𝐤)−3​𝐈2×2)=t​(AcornerT​(𝐤)+2​AedgeT​(𝐤)),\displaystyle=t(B_{T}^{\dagger}(\mathbf{k})B_{T}(\mathbf{k})-3\mathbf{I}_{2\times 2})=t(A^{T}_{\text{corner}}(\mathbf{k})+2A^{T}_{\text{edge}}(\mathbf{k})),(32)HR​(𝐤)\displaystyle H_{R}(\mathbf{k})=t​(BR†​(𝐤)​BR​(𝐤)−4​𝐈3×3)=t​(AcornerR​(𝐤)+2​AedgeR​(𝐤)),\displaystyle=t(B_{R}^{\dagger}(\mathbf{k})B_{R}(\mathbf{k})-4\mathbf{I}_{3\times 3})=t(A^{R}_{\text{corner}}(\mathbf{k})+2A^{R}_{\text{edge}}(\mathbf{k})),(33)

while the off-diagonal blockst​BT†​(𝐤)​BR​(𝐤)tB_{T}^{\dagger}(\mathbf{k})B_{R}(\mathbf{k})andt​BR†​(𝐤)​BT​(𝐤)tB_{R}^{\dagger}(\mathbf{k})B_{T}(\mathbf{k})directly correspond to the bipartite cross-termsHT​R​(𝐤)H_{TR}(\mathbf{k}).

ExpandingH​(𝐤)H(\mathbf{k})completely yields a5×55\times 5Hermitian matrix:H​(𝐤)=t​(||22~r​1∗~r​2∗~r​3∗()∗2||2~r​1~r​2~r​3~r​1~r​1∗~r​12~r​1​~r​2~r​1​~r​3~r​2~r​2∗~r​1​~r​2~r​22~r​2​~r​3~r​3~r​3∗~r​1​~r​3~r​2​~r​3~r​32)H(\mathbf{k})=t\begin{pmatrix}|\Delta|^{2}&{}^{2}&{}^{*}\tilde{\gamma}_{r1}&{}^{*}\tilde{\gamma}_{r2}&{}^{*}\tilde{\gamma}_{r3}\\
({}^{*})^{2}&|\Delta|^{2}&\Delta\tilde{\gamma}_{r1}&\Delta\tilde{\gamma}_{r2}&\Delta\tilde{\gamma}_{r3}\\
\Delta\tilde{\gamma}_{r1}&{}^{*}\tilde{\gamma}_{r1}&\tilde{\gamma}_{r1}^{2}&\tilde{\gamma}_{r1}\tilde{\gamma}_{r2}&\tilde{\gamma}_{r1}\tilde{\gamma}_{r3}\\
\Delta\tilde{\gamma}_{r2}&{}^{*}\tilde{\gamma}_{r2}&\tilde{\gamma}_{r1}\tilde{\gamma}_{r2}&\tilde{\gamma}_{r2}^{2}&\tilde{\gamma}_{r2}\tilde{\gamma}_{r3}\\
\Delta\tilde{\gamma}_{r3}&{}^{*}\tilde{\gamma}_{r3}&\tilde{\gamma}_{r1}\tilde{\gamma}_{r3}&\tilde{\gamma}_{r2}\tilde{\gamma}_{r3}&\tilde{\gamma}_{r3}^{2}\end{pmatrix}(34)

BecauseH​(𝐤)H(\mathbf{k})is defined by the outer product of a single vectorB~​(𝐤)\tilde{B}(\mathbf{k}), it is mathematically constrained to rank 1. By the rank-nullity theorem, for every momentum𝐤\mathbf{k}, the matrix possesses exactly5−1=45-1=4zero eigenvalues and one dispersive band defined by the trace,E​(𝐤)=Tr​[H​(𝐤)]=2​t​[9+4​C𝐤+2​(3+C𝐤)​cos⁡(k3)],E(\mathbf{k})=\text{Tr}[H(\mathbf{k})]=2t\left[9+4C_{\mathbf{k}}+2\left(3+C_{\mathbf{k}}\right)\cos(k_{3})\right],

whereC𝐤=cos⁡(k1)+cos⁡(k2)+cos⁡(k1−k2)C_{\mathbf{k}}=\cos(k_{1})+\cos(k_{2})+\cos(k_{1}-k_{2}).
This guarantees 4 macroscopic exactly flat bands pinned atE=0E=0, touching the dispersive band at theHHandH′H^{\prime}points of the Brillouin zone.Figure 8:Bandstructure of the hopping Hamiltonian defined on the heterogeneous face-set of a simple hexagonal lattice

As established in the real-space discussion, the homogeneous momentum-space blocksHT​(𝐤)H_{T}(\mathbf{k})andHR​(𝐤)H_{R}(\mathbf{k})mathematically guarantee11and22macroscopic flat bands, respectively. This accounts for33of the44total flat bands ofH​(𝐤)H(\mathbf{k}). The remaining fourth flat band emerges from the frustrated bipartite hopping between the triangular and rectangular faces, which we now analyze.

## 5.2Nullspace of the Bipartite Cross-Terms

To understand the origin of the four macroscopic flat bands in the simple hexagonal lattice, we analyze the nullspace of its5​N×N5N\times Nincidence matrixBB, which we partitioned into sub-blocks:B=[BTBR]B=\begin{bmatrix}B_{T}&B_{R}\end{bmatrix}. The triangular blockBTB_{T}(2​N×N2N\times N) and rectangular blockBRB_{R}(3​N×N3N\times N) each have rankNNand nullities𝒩T=N\mathcal{N}_{T}=Nand𝒩R=2​N\mathcal{N}_{R}=2N. Together, they provide3​N3Ndegenerate zero-modes, meaning the remainingNN-fold degeneracy emerges from the bipartite network coupling the triangular and rectangular faces. A state=(,T)RT\Psi=({}_{T},{}_{R})^{T}in this mixed nullspace requiresBT+TBR=R0,||T≠0,||R≠0B_{T}{}_{T}+B_{R}{}_{R}=0,|{}_{T}|\neq 0,|{}_{R}|\neq 0.

## 5.2.1-point Flat band Wavefunctions and Compact Localized States

To find the state uniquely associated with this mixed nullspace, we must construct a state that is orthogonal to both the triangular and rectangular nullspaces. Orthogonality to the triangular nullspace (defined byut​1=−ut​2u_{t1}=-u_{t2}) requires a uniform triangular amplitudeut​1=ut​2≡utu_{t1}=u_{t2}\equiv u_{t}. Simultaneously, orthogonality to the rectangular nullspace (defined byur​1+ur​2+ur​3=0u_{r1}+u_{r2}+u_{r3}=0) requires a uniform rectangular amplitudeur​1=ur​2=ur​3≡uru_{r1}=u_{r2}=u_{r3}\equiv u_{r}.

Applying this uniform weight requirement at the -point (𝐤=0\mathbf{k}=0), where the incidence vector evaluates toB​(0)=[33444]B(0)=\begin{bmatrix}3&3&4&4&4\end{bmatrix}, the destructive interference conditionB​(0)=0B(0)\Psi=0for|(𝐪=0)flatmixed⟩≡(ut,ut,ur,ur,ur)T|{}_{\rm flat}^{\rm mixed}({\bf q}=0)\rangle\equiv(u_{t},u_{t},u_{r},u_{r},u_{r})^{T}simplifies to:ut+2​ur=0.u_{t}+2u_{r}=0.(35)

This momentum-space state can be represented in real space by Compact Localized States (CLSs) that reside in this mixed nullspace. We construct this symmetric CLS by taking a localized configuration centered on a single central vertical axis between𝟎\mathbf{0}and𝐚3\mathbf{a}_{3}. We assign an amplitude of+2+2to the 12 basal triangles, an amplitude of−2-2to the 6 internal radial rectangles, and an amplitude of−1-1to the 6 outer perimeter rectangles:|⟩CLS=2∑t∈T0∪Tc|t⟩−2∑r∈Rrad|r⟩−∑r∈Rper|r⟩|{}_{\text{CLS}}\rangle=2\sum_{t\in T_{0}\cup T_{c}}|t\rangle-2\sum_{r\in R_{\text{rad}}}|r\rangle-\sum_{r\in R_{\text{per}}}|r\rangle(36)

whereT0T_{0}andTcT_{c}are the sets of 6 triangles meeting at the central vertices𝟎\mathbf{0}and𝐚3\mathbf{a}_{3}respectively,RradR_{\text{rad}}are the 6 radial rectangles sharing the central vertical axis, andRperR_{\text{per}}are the 6 rectangles forming the outer boundary of the hexagonal prism. One can check that the destructive interference conditionB|⟩CLS=0B|{}_{\text{CLS}}\rangle=0is satisfied at all vertices. Because the sum of weights on thet1t_{1}andt2t_{2}faces are equal,|⟩CLS|{}_{\text{CLS}}\rangleis orthogonal to the nullspace ofBTB_{T}. Because the total weights on the 3 rectangular face classes is also equal|⟩CLS|{}_{\text{CLS}}\rangleis orthogonal to the nullspace ofBRB_{R}.

## 6Generalization to arbitrary heterogeneous face-graphs

The extension of the proof to a heterogenous face-set demonstrated in the simple hexagonal lattice in the previous section applies to any cell complex containing faces of mixed degrees. Consider an arbitrary lattice graph where the faces are partitioned into sets based on their degree, for instance,pp-cycle faces (setFpF_{p}) andqq-cycle faces (setFqF_{q}). The HamiltonianH=t​BT​BH=tB^{T}Bhas a block structure reflecting these homogeneous subsets and their bipartite coupling.

By separating the face-vertex incidence matrix into corresponding blocksB=[BpBq]B=\begin{bmatrix}B_{p}&B_{q}\end{bmatrix},HHexpands to:H=t​(BpT​BpBpT​BqBqT​BpBqT​Bq)H=t\begin{pmatrix}B_{p}^{T}B_{p}&B_{p}^{T}B_{q}\\
B_{q}^{T}B_{p}&B_{q}^{T}B_{q}\end{pmatrix}(37)

and similar to the hexagonal case, this operator decomposes into homogeneous intra-sector termsHp=t​(BpT​Bp−p)H_{p}=t(B_{p}^{T}B_{p}-p)andHq=t​(BqT​Bq−q)H_{q}=t(B_{q}^{T}B_{q}-q), alongside the bipartite inter-sector couplingHp​q=t​(BpT​Bq+BqT​Bp)H_{pq}=t(B_{p}^{T}B_{q}+B_{q}^{T}B_{p}). Crucially, because the full structural operatorHHis constructed using the|V|×|F||V|\times|F|incidence matrixBB, its rank cannot exceed|V||V|. The rank-nullity theorem thus guarantees thatHHpossesses a macroscopic nullspace of dimension at least|F|−|V||F|-|V|. When the cell complex is a regular lattice, these|F|−|V||F|-|V|degenerate states yield exactly flat bands. The diagonal ofHHconstitutes a heterogeneous degree matrixDDwith entriesp​tptfor faces inFpF_{p}andq​tqtfor faces inFqF_{q}. Consequently, the flat bands ofHHdo not correspond to the eigenstates of hopping on the corner-sharing and edge-sharing face-graphsH−D=t​(Acorner+2​Aedge)H-D=t(A_{\rm corner}+2A_{\rm edge}), but they can be understood as emerging separately from hopping Hamiltonians on the homogeneous face-graphsHp,HqH_{p},H_{q}and a bipartite hopping HamiltonianHp​qH_{pq}between the two face-sets.

## 6.1Nullspace decomposition for arbitrary face combinations

To count the exact flat bands of the HamiltonianHH, we evaluate the nullity of the face-vertex incidence matrixBB. By the rank-nullity theorem, the total number of zero modes is the overall nullity:𝒩total=|Fp|+|Fq|−rank​(B).\mathcal{N}_{\text{total}}=|F_{p}|+|F_{q}|-\text{rank}(B).(38)

The rank ofBBis given by the sum of the ranks of its sub-matricesBpB_{p}andBqB_{q}minus the dimension of the intersection of their column spaces. Substituting this into the nullity equation, we can isolate the nullities of the sub-matrices, defined as𝒩p=|Fp|−rank​(Bp)\mathcal{N}_{p}=|F_{p}|-\text{rank}(B_{p})and𝒩q=|Fq|−rank​(Bq)\mathcal{N}_{q}=|F_{q}|-\text{rank}(B_{q})and the identify the remaining states in the nullspace as the nullity of the bipartite hopping HamiltonianHp​qH_{pq}𝒩total=𝒩p+𝒩q+dim(col​(Bp)∩col​(Bq))\mathcal{N}_{\text{total}}=\mathcal{N}_{p}+\mathcal{N}_{q}+\dim(\text{col}(B_{p})\cap\text{col}(B_{q}))(39)

Thus we find that the ground state degeneracy ofHHis a sum of the nullities of the hopping HamiltoniansHp,HqH_{p},H_{q}on the homogeneous face-graphs and the nullity of the hopping HamiltonianHp​qH_{pq}on the inter-sector bipartite face-graph. Any zero modes not intrinsic to the isolatedpp-gon orqq-gon face-graphs arise from the bipartite graph connecting them. A state=(,p)qT\Psi=({}_{p},{}_{q})^{T}in this mixed-topology nullspace requires a non-trivial solution satisfyingBp=p−BqqB_{p}{}_{p}=-B_{q}{}_{q}. The exact number of these inter-sector flat bands is the intersection dimensiondim(col​(Bp)∩col​(Bq))\dim(\text{col}(B_{p})\cap\text{col}(B_{q})).

We do not see an obstacle to generalizing this to a larger heterogeneous set of faces{Fq,Fq,Fr,…}\{F_{q},F_{q},F_{r},\ldots\}and therefore these two cases (homogeneous and heterogeneous face-graphs) enumerate a countable infinity of ‘flat band’ Hamiltonians arising from destructive interference of hopping on the faces of any cell complex, with or without discrete translation invariance.

## 7Topological Protection of Flat Bands in Face Graphs via the Discrete Atiyah-Singer Index Theorem

To establish that the macroscopic degeneracy of the flat bands in face-graph tight-binding models is topologically protected, we map the system to a topological hypergraph and apply the finite-graph generalization of the Atiyah-Singer index theorem[levitt1992,knill2012,knill2013]. The key point is that we want to understand the degeneracy of the nullspace of theBT​BB^{T}Boperator, which is at the root of all the macroscopic degeneracies discussed above.

## 7.1The Graded Vector Space and Discrete Operators

Consider a topological hypergraph with verticesVVand generalized edgesFF. These generalized edgesFFincident onp>2p>2vertices correspond to the faces of the root graphG​(V,E)G(V,E)(specified by irreducible cycles), as defined in Section2.

Definition (Graded Hilbert Space).Letℋ\mathcal{H}be the vector space of localized states on the hypergraph, decomposed into two orthogonal sectors graded by a parity operator :ℋ=ℋF⊕ℋV\mathcal{H}=\mathcal{H}_{F}\oplus\mathcal{H}_{V}(40)

whereℋF≅ℂ|F|\mathcal{H}_{F}\cong\mathbb{C}^{|F|}is the space of states localized on the faces or generalised edges (the even sector,=+1\Gamma=+1), andℋV≅ℂ|V|\mathcal{H}_{V}\cong\mathbb{C}^{|V|}is the space of states localized on the vertices (the odd sector,=−1\Gamma=-1).

Definition (Discrete Dirac Operator).LetBBbe the|V|×|F||V|\times|F|face-vertex incidence matrix as defined in Section3, whereBv​f=1B_{vf}=1if vertexvvis incident to faceff, and0otherwise. The discrete Dirac operatorD:ℋ→ℋD:\mathcal{H}\to\mathcal{H}is defined as:D=(0BTB0)D=\begin{pmatrix}0&B^{T}\\
B&0\end{pmatrix}(41)

The operatorDDis odd, satisfying{D,}=0\{D,\Gamma\}=0.

Definition (Discrete Laplace-Beltrami Operator).The Laplace-Beltrami operator is defined asL=D2L=D^{2}. Due to the block off-diagonal structure ofDD,LLis block diagonal and preserves the grading,[L,]=0[L,\Gamma]=0:L=(BT​B00B​BT)=(LF00LV)L=\begin{pmatrix}B^{T}B&0\\
0&BB^{T}\end{pmatrix}=\begin{pmatrix}L_{F}&0\\
0&L_{V}\end{pmatrix}(42)

The flat band degeneracy is thus given by the degeneracy of the nullspace of the even sector of the Laplacian,dim(ker⁡LF)\dim(\ker L_{F}).

## 7.2The McKean-Singer Spectral Symmetry and Analytical Index

Definition (Analytical Index).Following Knill[knill2013], the analytical index of the discrete Dirac operatorDDis defined as the supertrace of its heat kernel:inda​(D)≡str​(e−L)=Tr​(e−LF)−Tr​(e−LV)\text{ind}_{a}(D)\equiv\text{str}(e^{-\beta L})=\text{Tr}(e^{-\beta L_{F}})-\text{Tr}(e^{-\beta L_{V}})(43)

where>0\beta>0is a parameter scaling the evolution.

Theorem (McKean-Singer Symmetry).For any non-zero eigenvalue>0\lambda>0ofLFL_{F}, there exists a corresponding eigenvalue forLVL_{V}with identical multiplicity.

Proof.Let∈FℋF{}_{F}\in\mathcal{H}_{F}be an eigenvector ofLFL_{F}with eigenvalue>0\lambda>0, such thatBTB=FFB^{T}B{}_{F}=\lambda{}_{F}. Applying the operatorBBto both sides yields:B(BTB)F=B()F⟹(BBT)(B)F=(B)FB(B^{T}B{}_{F})=B(\lambda{}_{F})\implies(BB^{T})(B{}_{F})=\lambda(B{}_{F})(44)

Let=VBF{}_{V}=B{}_{F}. We know≠V0{}_{V}\neq 0, since=V0{}_{V}=0impliesBTB=F0B^{T}B{}_{F}=0, which contradicts≠F0\lambda{}_{F}\neq 0. Therefore,∈VℋV{}_{V}\in\mathcal{H}_{V}is an eigenvector ofLV=B​BTL_{V}=BB^{T}with the same eigenvalue444Physically, this indicates that any dispersive (kinetic) state propagating on the face lattice has a corresponding partner state of identical energy propagating on the vertex lattice. This spectral symmetry is the basis of supersymmetric theories but we do not need to appeal to this physics in this mathematical proof..

Corollary (Nullspace Reduction of Index).As a direct consequence of the McKean-Singer spectral symmetry, the contributions of all non-zero eigenvalues (>0\lambda>0) to the heat kernel trace cancel identically. Thus, the analytical index reduces to the difference between the zero-energy spaces of the even and odd sectors, independent of :inda​(D)=dim(ker⁡LF)−dim(ker⁡LV)=dim(ker⁡B)−dim(ker⁡BT)\text{ind}_{a}(D)=\dim(\ker L_{F})-\dim(\ker L_{V})=\dim(\ker B)-\dim(\ker B^{T})(45)

## 7.3Fractional Curvature and Topological Index

The discrete Atiyah-Singer theorem relates the analytical index to the local geometry of the graph. For a standard finite cell complex, the fractional Euler curvature at a vertexvvis generally defined as[levitt1992,knill2012]:K​(v)=∑x∋v(x)|x|K(v)=\sum_{x\ni v}\frac{\omega(x)}{|x|}(46)

wherexxare the spatial cells containingvv,(x)\omega(x)is the topological weight of the cell, and|x||x|is the number of vertices inxx.

For our topological hypergraph, we assign a topological weight of(f)=+1\omega(f)=+1to the generalized edges (faces) and(v)=−1\omega(v)=-1to the vertices, corresponding to their parity grading.

Definition (Fractional Euler Curvature).For a vertexv∈Vv\in V, the local discrete curvatureK​(v)K(v)is:K​(v)=(v)1+∑f∈Fv(f)d​(f)=−1+∑f∈Fv1d​(f)K(v)=\frac{\omega(v)}{1}+\sum_{f\in F_{v}}\frac{\omega(f)}{d(f)}=-1+\sum_{f\in F_{v}}\frac{1}{d(f)}(47)

whereFvF_{v}is the set of faces (hyperedges) incident tovv, andd​(f)d(f)is the number of vertices in faceff.

Theorem (Discrete Gauss-Bonnet).The sum of the local curvature over all vertices yields the difference in the number of faces and vertices:∑v∈VK​(v)=|F|−|V|\sum_{v\in V}K(v)=|F|-|V|(48)

Proof.∑v∈VK​(v)=∑v∈V(−1+∑f∈Fv1d​(f))=−|V|+∑f∈F∑v∈f1d​(f)=|F|−|V|.\sum_{v\in V}K(v)=\sum_{v\in V}\left(-1+\sum_{f\in F_{v}}\frac{1}{d(f)}\right)=-|V|+\sum_{f\in F}\sum_{v\in f}\frac{1}{d(f)}=|F|-|V|.(49)

## 7.4Topological Protection of the extensive nullspace ofBT​BB^{T}B

The discrete Atiyah-Singer index theorem equates the analytical index with the topological index computed via the Gauss-Bonnet sum:inda​(D)=∑v∈VK​(v)\text{ind}_{a}(D)=\sum_{v\in V}K(v)(50)

Substituting the established identities:dim(ker⁡BT​B)−dim(ker⁡B​BT)=|F|−|V|\dim(\ker B^{T}B)-\dim(\ker BB^{T})=|F|-|V|(51)

Sincedim(ker⁡B​BT)≥0\dim(\ker BB^{T})\geq 0, this establishes the bound on the macroscopic degeneracy of the flat band manifold:dim(ker⁡BT​B)≥|F|−|V|\dim(\ker B^{T}B)\geq|F|-|V|(52)

## 7.5Physical Intuition

The local curvature functionK​(v)K(v)represents a local geometric measure of the imbalance between the number of faces and vertices. The topologically protected degeneracy of the operatorBT​BB^{T}Bsurvives even if the hypergraph is disordered, because it counts the non-zero curvature on the vertices where this imbalance survives. The question of whether the hopping on the face-graphs we introduce is ‘fine-tuned’ does not arise as long as the adjacency of the graph isdefinedby the incidence matrix prescriptionBT​BB^{T}B, not by distances in the physical space where the graph is embedded. Physically, orbitals supported on the faces of a graph embedded in real space would be expected to hop on the face-graph defined by this construction when they are restricted to only hop to other faces through the vertices that they share.

## 8Discussion

In computer science and spectral graph theory[godsil2001,cvetkovic2009towards,cvetkovic2010,cvetkovic2010a], such incidence operators (BT​BB^{T}B) are known as signless Laplacians and the degeneracy of their zero-eigenvalue subspace governs network dynamics in strongly constrained environments.
In particular, high-dimensional cell complexes are increasingly used in machine learning to represent higher-order relational information in complex datasets[hajij2023].
Random walks on these generalized graph structures provide an overarching algorithmic framework for tasks such as representation learning and semi-supervised learning[mukherjee2016,yang2022].
Unlike the standard graph Laplacian, where the null space simply counts disconnected components, the macroscopic null space of the signless Laplacian operatorBT​BB^{T}Bdescribes localizedquantumstates on a fully connected graph[leykam2018]with compact support.
Because these compact localized states are exact eigenmodes, they represent quantum wavefunctions that fail to ergodically explore the network due to perfect destructive interference[bergman2008].
This has consequences not only for quantum machine learning algorithms[biamonte2017], but also quite generally for quantum search algorithms[childs2004]that rely on the physics of a quantum walk on a generalized graph, where compact localized eigenmodes break the implicit assumption that the perturbed walk is ergodic and always able to reach the target node.

Consequently, identifying and manipulating these extended degeneracies is critical for resolving arrested dynamics and information trapping in complex discrete quantum networks, whether they are built of quantum simulators in arbitrary graphs[kollarLineGraphLatticesEuclidean2020], Josephson junction arrays[chandra1995,bonamassa2023]in the quantum regime[dutta2021,nambisan2026]or the connectivity of many-body states in Hilbert space[tan2025].

In particular, the geometry of incidence matrices can be readily applied to the many-body transition graphs of kinetically constrained systems such as dimer models, where extensive degeneracies in the many-body spectrum have been reported and in some cases, connected explicitly to compact localized states on the transition graph. Just as we defined faces as induced cycles on the graph and the adjacency matrix of the face-graphs in terms of the face-vertex incidence matrix, we can define higher-dimensional analogs of faces as induced cycles of the line-graphs, the face-graphs and so on, to identify higher-order compact localized states defined on these higher-dimensional cell-complexes555Formally this can be done either by defining ann-dimensional topological space with the skeletaX0,X1,…​XnX^{0},X^{1},\ldots X^{n}identified by the sets of vertices, edges, and generalized facesV,E,…​FnV,E,\ldots F_{n}, or a poset with ground setP=V∪E∪…​FnP=V\cup E\cup\ldots F_{n}.. The prescription demonstrated here for face-graphs can be used to systematically enumerate such many-body Aharanov-Bohm cages[vidal1998]and the resulting extensive degeneracies in the many-body eigenspectrum that have been recently discussed as a new form of eigenstate order called quantum many-body caged spin-glass[ben-amiManybodyCagesDisorderfree2025], wherein strong correlations in the form of kinetic constraints cause arrested dynamics in the many-body Hilbert space.

The robustness of this macroscopic degeneracy also extends to disordered networks where a fraction of the edges violate the perfect local frustration-free connectivity implied by the positive-semidefinite operatorBT​BB^{T}B. When such structural defects are randomly introduced, the strict geometric symmetries (specifically local graph automorphisms) required for the perfect destructive interference are locally broken, partially lifting the exact degeneracy. However, the extensive nature of the degeneracy is expected to survive below a critical threshold, beyond which disorder-delocalized puddles may percolate to form a giant connected cluster. This persistence in disordered environments is facilitated by the spatial compactness of the localized states, which remain shielded from distant structural defects. These natural corollaries of the prescription for extensive degeneracies of the kind that we discuss are ripe for demonstration in simulations and experiments.

The extensive degeneracies of adjacency matrices of face-graph and line-graphs defined by this prescription of incidence geometries represents a novel failure mode of quantum networks with no analog in classical networks. A signal that is initiated with the particular quantum superposition of a compact localized state fails to propagate through the network even when it is fully connected. In stark contrast to classical networks, local defects in the connectivity or classical failure of nodes or edges of these graphs serve to heal these defect modes when they open additional non-frustrated hopping pathways, so that beyond a critical threshold of defects there are no localized eigenmodes that prevent quantum signals from propagating across a fully connected network. In this sense, this provides a complementary perspective to the standard lore of connectivity and dependency in interdependent networks pioneenered by Havlin and collaborators[buldyrev2010,bonamassa2023]where dependencies between nodes in two networks leads to cascades that cause both networks to fail together. In quantum networks defined on the line-graphs and face-graphs that are dependent of the networks defined on the root graph, failures on the latter make the former robust against arrested dynamics of quantum information.

In quantum condensed matter physics and chemistry, the face-graph construction may be relevant for systems whose orbitals have maximum probability amplitude away from the geometric center, supported on three or more spatial locations. Prominent examples are the so-called ‘fidget-spinner’ orbitals of magic-angle twisted bilayer graphene[koshinoMaximallyLocalizedWannier2018,po-prx-2018,kangSymmetryMaximallyLocalized2018], and the molecular orbitals of star-shaped organic polymers (eg. starphenes[clar1968]), open-shell graphene nanoflakes[clar1953,melle-franco2017,pavlicek2017].

Networks built out of such orbitals allow novel possibilities in the realm of spin-qubit-based quantum computing. Open-shell graphene nanoflakes are non-Kekulé structures (also known as unbalanced bipartite lattices in physics) with high-spin ground states and a degenerate set of zero-energy non-bonding orbitals because of Ovchinnikov’s rule[ovchinnikov1978](Lieb’s theorem[lieb1989]in physics). The resulting N-level system of N-triangulene is therefore recognized as a potential quantum memory and as a generalized qubit for quantum computation[mishra2021,wei2012,sato2009,mishra2020,valenta2022], where the quantum information of the spin-state is stored in the Singly Occupied Molecular Orbitals that are delocalized over the flake boundaries666In the thermodynamic limit, these are the familiar topologically protected edge-modes at the zigzag edges of graphene[fujita1996,ryu2002,castroneto2009]. Constructing arbitrary lattices of such flakes allows the possibility of compact localized states on the face-graphs and line-graphs, that have no overlap with any decoherence sources beyond a small finite number of flakes. The quantum information in the generalized qubit is then topologically protected in a way that is fundamentally distinct from the conventional routes to topological quantum computation which depend on the elusive Majorana bound states or Majorana quasiparticles[aliceaNewDirectionsPursuit2012].

Complementary to the recent interest in the Reimannian structure[provostRiemannianStructureManifolds1980,berryFiveYearsLater,chengQuantumGeometricTensor2010,marzariMaximallyLocalizedGeneralized1997]of flat-band wavefunctions that goes by the name of quantum geometry[ahn2022,verma2025], we provide an orthogonal perspective on the quantum mechanical implications of the discrete geometry of the graphs on which these flat bands are defined, and on which the extensive degeneracies of compact localized states are topologically guaranteed even when bands are not well-defined.

## 9Acknowledgments

I am grateful to Nick Sander and Lars Franke for pointing me to Ref.[kane2014]and to Daniel Schultz for a well-posed question that prompted the following appendix.

## Appendix APhysical Motivation for the Chosen Definition of Faces

In the main text, we defined the faces of an arbitrary graph as the set of its relevant (or irreducible) cycles. This definition emerges naturally from the physical requirements of defining gauge fields and fluxes on discrete networks.

Consider a graphG​(V,E)G(V,E)as a network of wires or bonds hosting a vector field, such as a vector potential𝐀\mathbf{A}. By the discrete Hodge-Helmholtz theorem, any edge-defined vector field on a graph can be uniquely decomposed into three orthogonal components:𝐀=∇+∇×+𝐡\mathbf{A}=\nabla\phi+\nabla\times\mathbf{\Phi}+\mathbf{h}(A.1)

comprising an irrotational gradient field (∇\nabla\phi), a solenoidal rotational field (∇×\nabla\times\mathbf{\Phi}), and a global harmonic component (𝐡\mathbf{h}). The harmonic component corresponds to an Aharanov-Bohm flux threaded through the holes of the periodic system, in practice implemented as a large gauge transformation. The physical observables are the magnetic fluxes, defined as the circulation of the vector potential around closed loops.

By the discrete Stokes’ theorem[grady2010], the total circulation around any cycle in the graph is given by the oriented sum of the fluxes through a set of plaquettes spanning the enclosed surface. Therefore, the rotational component of the vector field is uniquely determined by its fluxes through the elementary cycles that tile the graph in the sense that a modulo-2 sum of these cycles can describe any closed cycle of the graph. This requirement naturally leads to the graph-theoretic notion of the cycle space[biggs1993].
The closest analog to a measurable magnetic field is the discrete curl on the smallest possible cycles on the graph.
This motivates the use of a Minimum Weight Cycle Basis (MWCB)777Consider the edge spaceC1​(G;𝔽2)C_{1}(G;\mathbb{F}_{2})and the vertex spaceC0​(G;𝔽2)C_{0}(G;\mathbb{F}_{2})over the finite field of two elements. The boundary operator∂1:C1→C0\partial_{1}:C_{1}\to C_{0}maps edges to their incident vertices. Formally, the cycle space of the graph is the kernel of the boundary operator:𝒵=ker⁡(∂1)\mathcal{Z}=\ker(\partial_{1}). The dimension of this space is given by the cyclomatic number=|E|−|V|+c\mu=|E|-|V|+c, whereccis the number of connected components. The minimum weight cycle basis is defined by selecting a basis of𝒵\mathcal{Z}that minimizes the total length (or weight) of its constituent cycles.—a basis whose total cycle length is minimal.
However, choosing a single MWCB generally breaks some spatial symmetries that may exist on regular graphs, as there are often multiple equivalent shortest loops.
By taking the union of all MWCBs, which define therelevant cycles, we construct an overcomplete basis for the cycle space.
This definition uniquely identifies faces of a graph without any reference to spatial embedding.
For example, while the FCC equatorial square is reducible (as discussed in the main text), the length-4 rhombi in a bipartite lattice like the Body-Centered Cubic (BCC) lattice (Fig.5) are irreducible because the lattice contains no length-3 triangles to tile them.

## References

## 


- 


Major funding support from
