# Inhomogeneous Ising Model on 2D kagomé Lattice: Fermionic field approach

**arXiv ID**: 2608.02156v1
**Authors**: Shahane A. Khachatryan, Zhidong Zhang, Ara G. Sedrakyan
**Published**: 2026-08-03
**Categories**: cond-mat.stat-mech, cond-mat.str-el, math-ph
**Comments**: 31 pages, 4 figures
**HTML URL**: https://arxiv.org/html/2608.02156v1

## Abstract

We investigate the two-dimensional inhomogeneous Ising model (2DIM) on the kagom'e lattice by mapping it onto a particular non-symmetric eight-vertex model and constructing the corresponding $R$-matrix. Using a fermionic representation, we evaluate the partition function and derive explicit expressions for the main thermodynamic quantities. In the thermodynamic limit, we obtain an exact equation for the critical surface determining the phase transition of the model. We also calculate the free energy, specific heat, and spontaneous magnetization in the ferromagnetic case. Furthermore, we show that when one or two coupling constants vanish, the model reduces, respectively, to the square-lattice and one-dimensional Ising models. In both limits, our results reproduce the corresponding exact critical couplings and free energies.

## Full Text

1 Introduction

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2608.02156v1 [cond-mat.stat-mech] 03 Aug 2026

Inhomogeneous Ising Model on 2D kagomé Lattice: Fermionic field approach.

Shahane A. Khachatryan111e-mail:shah@mail.yerphi.am,a,
Zhidong Zhang222e-mail:zdzhang@imr.ac.cn,band
Ara G. Sedrakyan333e-mail:sedrak@mail.yerphi.am,a,b


aAlikhanyan National Sience Laboratory (Yerevan Physics Institute), Alikhanian Br. str. 2, Yerevan 36, Armenia
bShenyang National Laboratory for Material Science,
Institute of Metal Research, China Academy of Sciences,
72 Wenhua Road, Shenyang, 110016, P.R.China

## Abstract

We investigate the two-dimensional inhomogeneous Ising model (2DIM) on the kagom’e lattice by mapping it onto a particular non-symmetric eight-vertex model and constructing the correspondingRR-matrix. Using a fermionic representation, we evaluate the partition function and derive explicit expressions for the main thermodynamic quantities. In the thermodynamic limit, we obtain an exact equation for the critical surface determining the phase transition of the model. We also calculate the free energy, specific heat, and spontaneous magnetization in the ferromagnetic case.

Furthermore, we show that when one or two coupling constants vanish, the model reduces, respectively, to the square-lattice and one-dimensional Ising models. In both limits, our results reproduce the corresponding exact critical couplings and free energies.

## 1Introduction

The Ising model is one of the most fundamental models in statistical mechanics for studying phase transitions and critical phenomena. In this model, each lattice site carries a spin variablesi=±1s_{i}=\pm 1, representing two possible magnetic orientations. Spins interact with their nearest neighbors, and the collective behavior of these interactions determines the macroscopic magnetic properties of the system.

In two dimensions, the Ising model has been extensively studied on various lattice geometries. The exact solution of the model on a square lattice by Lars Onsager in 1944,[1,2], established a cornerstone result in the theory of critical phenomena. However, when the lattice geometry changes, the physical properties and analytical treatment of the model may differ significantly. After Onsagers solution of the two dimensional Ising Model (2DIM) the integrability of two dimensional
statistical or quantum chain models[3,4]become an interesting topic in theoretical physics, which gain more and more applications
in modern low-dimensional condensed matter problems.

The exact-solution program is also tightly connected with duality, lattice transformations, Pfaffian/dimer methods, and fermionization: the Kramers–Wannier construction fixes the square-lattice critical point, triangular and honeycomb nets provide canonical non-square benchmarks, planar Ising models can be reduced to Pfaffian or dimer problems, and the free-fermion/eight-vertex formulation gives the natural vertex-model language for the present construction[5,6,7,8,9,10,11,12,13].

The transfer-matrix construction used below is aligned with Baxter’s zero-field eight-vertex solution: the partition function, special transfer-matrix eigenvectors, and equivalence to generalized ice-type/Ising formulations provide the natural algebraic setting for the present kagoméRR-matrix. Modern free-fermion developments additionally connect this point to bipartite dimers,ZZ-invariant structures, and direct free-fermion formulations of honeycomb, triangular, and kagomé Ising models[12,14,15,16,17].

One particularly interesting geometry is the kagomé lattice, a two-dimensional lattice composed of corner-sharing triangles. The kagomé lattice has a lower coordination symmetry compared with the square lattice and contains triangular units that can produce geometric frustration, especially when the spin interactions are antiferromagnetic. Because of this feature, the kagome lattice has become an important structure for studying frustrated magnetism and exotic magnetic states in condensed-matter physics.

For the ferromagnetic interaction case, the kagomé -lattice Ising model can be solved exactly through lattice-transformation techniques such as the star–triangle transformation, which maps the kagomé lattice to the honeycomb lattice. This mapping allows the determination of the system’s critical temperature and thermodynamic properties. The theoretical analysis of this system was developed in early works by K.Kano, S.Naya, I. Syozi and H.Nakano[18,19,20], who studied decorated lattices and their transformations in the context of the Ising model. In two previous papers[21,22]the 2DIM was considered also on other
heteropolygonal lattices.

The study of the Ising model on the kagomé lattice is therefore important for several reasons. First, it provides insight into how lattice geometry affects phase transitions in two-dimensional systems. Second, it serves as a theoretical framework for understanding frustrated magnetic materials, many of which possess kagomé-type structures. Finally, the model continues to play a role in modern research on strongly correlated systems, spin liquids, and complex magnetic ordering.

Exact mappings on closely related decorated or triangular-kagomé geometries further show that summing over internal spins can produce effective kagomé or honeycomb models with analytically tractable critical manifolds[23].

Recent kagomé-specific developments include exact analysis of interaction-generated frustration on a star kagomelike recursive lattice, quantum-simulation studies of the transverse-field kagomé Ising antiferromagnet, and finite-temperature phase diagrams of decorated kagomé Ising systems with competing interactions[24,25,26]. Recent review on models on kagomé lattice one can find in[27].

In this work, we present an interpretation of 2DIM on the inhomogeneous kagomé lattice[18,19]as a particular case of a generalized XYZ model. For the case of a regular lattice, the exact correspondence between the 2DIM and an inhomogeneous integrable XYZ model was established in[28,29], where the partition function of the classical model was reformulated as a trace over a product of appropriate R-matrices.

In the present work, we construct the corresponding R-matrix for the inhomogeneous 2D Ising model on the kagomé lattice (Section 2), and fermionize it using the technique developed in[30,28,29]. The formulation in terms of Grassmann variables has also been applied in[31,32]. This technique allows us to derive the partition function in the Fourier transform basis as a product of the determinants (Section 3).

A central result then for the kagomé lattice model is the determination of the parametric surface of critical points, which is obtained in Section 4. For homogeneous case the critical value for coupling was known -sinh⁡[2​Jc]=(4/3)1/4\sinh[2J_{c}]=(4/3)^{1/4}, and we have reproduced this formulae. We show here that for the inhomogeneous case the critical points belong to the two-dimensional
critical surface, depicted in the three dimensional space of the real coupling parameters, formulated by this equation:[∑k=13cosh⁡[2​Jk]−∏k=13sinh⁡[2​Jk]−∏k=13cosh⁡[2​Jk]][\sum^{3}_{k=1}\cosh[2J_{k}]-\prod_{k=1}^{3}\sinh[2J_{k}]-\prod_{k=1}^{3}\cosh[2J_{k}]]. We also present the exact expressions for the free energy as an integral, heat capacity in the thermodynamic limit (Section 4) and the expression of the spontaneous magnetization in the case of a homogeneous lattice (Section 5). The results show how
lattice geometry and coupling inhomogeneity modify the critical behavior
compared to the standard two-dimensional Ising model.

## 2Partition function:RR-matrix

The kagomé lattice is demonstrated on the Fig.1. It is constructed by periodic disposed triangles and hexagons. The spinssα=±1s_{\alpha}=\pm 1of the Ising model are situated on the vertices of the lattice and only nearest neighbor interactions are considered. The spin-spin interactions for the inhomogeneous case are described by three different couplingsJiJ_{i},i=1,2,3i=1,2,3, attached to the links oriented by three different directions. The
partition function looks likeZ=∑sα​β​γ∏α​β​γeJ1​sα​sβ′+J2​sβ​sγ+J3​sα​sγ.\displaystyle Z=\sum_{s_{\alpha\beta\gamma}}\prod_{\alpha\beta\gamma}e^{J_{1}s_{\alpha}s_{\beta^{\prime}}+J_{2}s_{\beta}s_{\gamma}+J_{3}s_{\alpha}s_{\gamma}}.(2.1)

However it is possible to represent the lattice as a checkerboard picture with square cells, constructed by means of two triangles as it is shown in the Fig.1byWi​jW_{ij}.J1{J_{1}}J1{J_{1}}J2{J_{2}}J2{J_{2}}J3{J_{3}}J3{J_{3}}(2​i,2​j)\scriptstyle(2i,2j)(2​i+1,2​j−1)\scriptstyle(\!2i\!+\!1,\!2j\!-\!1\!)(2​i+1,2​j+1)\scriptstyle(\!2i\!+\!1,2j\!+\!1\!)(2​i+2,2​j)\scriptstyle(2i+2,2j)Wα​βα′​β′{W}_{\alpha\beta}^{\alpha^{\prime}\beta^{\prime}}=β\betaα\alphaα′\alpha^{\prime}β′\beta^{\prime}γ\gammaFigure 1:kagomé lattice

In this formulation the partition function can be rewritten asZ=∑sα​β∏α​βWα​β,Wα​β=∑sγ=±1eJ1​[sα​sβ′+sβ​sα′]+J2​[sβ+sβ′]​sk+J3​[sα+sα′]​sγ.\displaystyle Z=\sum_{s_{\alpha\beta}}\prod_{\alpha\beta}W_{\alpha\beta},\quad W_{\alpha\beta}=\sum_{s_{\gamma}=\pm 1}e^{J_{1}[s_{\alpha}s_{\beta^{\prime}}+s_{\beta}s_{\alpha^{\prime}}]+J_{2}[s_{\beta}+s_{\beta^{\prime}}]s_{k}+J_{3}[s_{\alpha}+s_{\alpha^{\prime}}]s_{\gamma}}.(2.2)

As for the original kagomé lattice there is rotational symmetry at the centers of the hexagons interchanging the axes, and the model has symmetry in respect to the interchange of the parametersJiJ_{i},i=1,2,3i=1,2,3, we could define theRR-matrices by three different ways. In the Fig.1 we have separated the direction along the hoppingJ1J_{1}. Here we shall consider large lattice with periodic boundary conditions along the axes described by the hopping parametersJ2,3J_{2,3}. Then, as in[28], the partition function can be written as the product of the transfer matrices, defined asZ=t​r{s(2​i+1,1)}i=1,…,N​∏jτj,τj=t​rs(0,2​j)​∏iR(2​i,2​j)​(2​i+1,2​j−1)(2​i+2,2​j)​(2​i+1,2​j+1),\displaystyle Z=tr_{\{s_{(2i+1,1)}\}_{i=1,...,N}}\prod_{j}\tau_{j},\quad\tau_{j}=tr_{s_{(0,2j)}}\prod_{i}R_{(2i,2j)(2i+1,2j-1)}^{(2i+2,2j)(2i+1,2j+1)},(2.3)

Below we shall consider the notation of the indexes asi=0,…,N−1i=0,...,N-1,j=1,…,Nj=1,...,N, and the following
boundary conditionssp,k+N=sp,ks_{p,k+N}=s_{p,k},sp+N,k=sp,ks_{p+N,k}=s_{p,k}.

Note that in the early work[18], a different method was used to evaluate the partition function for the homogeneous model. The advantage of the present formulation (2.2,2.3) is that it allows one to interpret the general model as an eight-vertex model with an inhomogeneous
R-matrix, which coincides with the weight functionWi​jW_{ij}up to a local unitary transformation, as shown in[28].

By inserting at each vertex the identity operatorI=U​U−1I=UU^{-1}with the unitary operatorU=12()1  11−1U=\frac{1}{\sqrt{2}}\left({}^{1-1}_{1\;\;1}\right),
the partition function can be rewritten asZ=∑sα​β∏α​βRα​β,Rα​β=Uα−1​Uβ−1​Wα​β​Uα′​Uβ′.\displaystyle Z=\sum_{s_{\alpha\beta}}\prod_{\alpha\beta}R_{\alpha\beta},\quad R_{\alpha\beta}=U^{-1}_{\alpha}U^{-1}_{\beta}W_{\alpha\beta}U_{\alpha^{\prime}}U_{\beta^{\prime}}.(2.4)

One can easily calculateWα​βW_{\alpha\beta}according to formula2.2and represent it as follows:W=\qquad W=2​(e2​J1​cosh⁡2​[J2+J3]cosh⁡2​J2cosh⁡2​J3e−2​J1cosh⁡2​J2e−2​J1​cosh⁡2​[J2−J3]e2​J1cosh⁡2​J3cosh⁡2​J3e2​J1e−2​J1​cosh⁡2​[J2−J3]cosh⁡2​J2e−2​J1cosh⁡2​J3cosh⁡2​J2e2​J1​cosh⁡2​[J2+J3])\displaystyle 2\!\left(\!\!\begin{array}[]{cccc}e^{2J_{1}}\cosh{2[J_{2}+\!J_{3}]}&\cosh{2J_{2}}&\cosh{2J_{3}}&e^{-2J_{1}}\\
\cosh{2J_{2}}&e^{-2J_{1}}\cosh{2[J_{2}-\!J_{3}]}&e^{2J_{1}}&\cosh{2J_{3}}\\
\cosh{2J_{3}}&e^{2J_{1}}&e^{-2J_{1}}\cosh{2[J_{2}-\!J_{3}]}&\cosh{2J_{2}}\\
e^{-2J_{1}}&\cosh{2J_{3}}&\cosh{2J_{2}}&e^{2J_{1}}\cosh{2[J_{2}+\!J_{3}]}\end{array}\!\!\right)(2.9)

The correspondingRR-matrix, maximally simplified by applying local unitary
transformationsUUat each vertex, takes the standard form of the eight-vertex matrix.R=(R000000R00110R0101R011000R1001R10100R110000R1111)\displaystyle R=\left(\begin{array}[]{cccc}R_{00}^{00}&0&0&R_{00}^{11}\\
0&R_{01}^{01}&R_{01}^{10}&0\\
0&R_{10}^{01}&R_{10}^{10}&0\\
R_{11}^{00}&0&0&R_{11}^{11}\end{array}\right)(2.14)

with the following matrix elements:R0000\displaystyle R_{00}^{00}=\displaystyle=8​(cosh⁡J1​cosh⁡J2​cosh⁡J3+sinh⁡J1​sinh⁡J2​sinh⁡J3)2,\displaystyle 8\left(\cosh{J_{1}}\cosh{J_{2}}\cosh{J_{3}}+\sinh{J_{1}}\sinh{J_{2}}\sinh{J_{3}}\right)^{2},(2.15)R1111\displaystyle R_{11}^{11}=\displaystyle=8​(sinh⁡J1​cosh⁡J2​cosh⁡J3+cosh⁡J1​sinh⁡J2​sinh⁡J3)2,\displaystyle 8\left(\sinh{J_{1}}\cosh{J_{2}}\cosh{J_{3}}+\cosh{J_{1}}\sinh{J_{2}}\sinh{J_{3}}\right)^{2},(2.16)R0011\displaystyle R_{00}^{11}=\displaystyle=R1100=2​(cosh⁡2​J2​cosh⁡2​J3−1)​sinh⁡2​J1+2​cosh⁡2​J1​sinh⁡2​J2​sinh⁡2​J3,\displaystyle R_{11}^{00}=2\left(\cosh{2J_{2}}\cosh{2J_{3}}-1\right)\sinh{2J_{1}}+2\cosh{2J_{1}}\sinh{2J_{2}}\sinh{2J_{3}},(2.17)R0110\displaystyle R_{01}^{10}=\displaystyle=R1001=2​(cosh⁡2​J2​cosh⁡2​J3+1)​sinh⁡2​J1+2​cosh⁡2​J1​sinh⁡2​J2​sinh⁡2​J3,\displaystyle R_{10}^{01}=2\left(\cosh{2J_{2}}\cosh{2J_{3}}+1\right)\sinh{2J_{1}}+2\cosh{2J_{1}}\sinh{2J_{2}}\sinh{2J_{3}},(2.18)R0101\displaystyle R_{01}^{01}=\displaystyle=8​(sinh⁡J3​cosh⁡J2​cosh⁡J1+cosh⁡J3​sinh⁡J2​sinh⁡J1)2,\displaystyle 8\left(\sinh{J_{3}}\cosh{J_{2}}\cosh{J_{1}}+\cosh{J_{3}}\sinh{J_{2}}\sinh{J_{1}}\right)^{2},(2.19)R1010\displaystyle R_{10}^{10}=\displaystyle=8​(sinh⁡J2​cosh⁡J1​cosh⁡J3+cosh⁡J2​sinh⁡J1​sinh⁡J3)2.\displaystyle 8\left(\sinh{J_{2}}\cosh{J_{1}}\cosh{J_{3}}+\cosh{J_{2}}\sinh{J_{1}}\sinh{J_{3}}\right)^{2}.(2.20)

The first property we have verified is the free-fermion condition, characteristic of the two-dimensional Ising model, which is found to be satisfied in this case as well.R0000​R1111−R0011​R1100=R0110​R1001−R0101​R1010.\displaystyle R_{00}^{00}R_{11}^{11}-R_{00}^{11}R_{11}^{00}=R_{01}^{10}R_{10}^{01}-R_{01}^{01}R_{10}^{10}.(2.21)

This give us possibility to represent in Section 3 the action of the model as a quadratic form of
Grassmann variables and write the partition function as a continual integral over them
by following the technique developed in[30,28,29]. After that we explore the physical characteristics of the model, namely, we find the surface
of critical points, calculate thermal capacity and magnetization.

We consider periodic boundary conditions in the same way, as in the work[28].

## 3Fermionic field representation

In Ref.[28], the fermionic realization of the partition function of the eight-vertex model was employed for its analysis. In the present work, we apply those results to the particular case defined by Eq. (2.15).

The two-dimensional spin states at each lattice site(i,j)(i,j)are represented in fermionic form as basis elements of a two-dimensional Fock space,|0⟩i​j|0\rangle_{ij}and|1⟩i​j|1\rangle_{ij}. These states satisfyci​j​|0⟩i​j=0,ci​j+​|0⟩i​j=|1⟩i​j,c_{ij}|0\rangle_{ij}=0,\qquad c^{+}_{ij}|0\rangle_{ij}=|1\rangle_{ij},

whereci​jc_{ij}andci​j+c^{+}_{ij}are fermionic annihilation and creation operators obeying the anticommutation relation{c,c+}+=0\{c,c^{+}\}_{+}=0, corresponding to scalar fermions.

It should be noted that in Section II of Ref.[28], theRR-matrix was written in the so-called “check” form, although this was not explicitly emphasized there; its role is clarified in Section III of that work. Applying Eqs. (3.1)–(3.3) from[28], we obtainℛ12=Rα​βα′​β′|β⟩2|α⟩12⟨β′|⟨α′|1\displaystyle\mathcal{R}_{12}=R_{\alpha\beta}^{\alpha^{\prime}\beta^{\prime}}|\beta\rangle_{2}|\alpha\rangle_{1}{}_{2}\langle\beta^{\prime}|{}_{1}\langle\alpha^{\prime}|=\displaystyle=Rα​βα′​β′​(−1)p​(α)​p​(β′)​|β⟩2​⟨β′|​|α⟩1​⟨α′|,\displaystyle R_{\alpha\beta}^{\alpha^{\prime}\beta^{\prime}}(-1)^{p(\alpha)p(\beta^{\prime})}|\beta\rangle_{2}\langle\beta^{\prime}||\alpha\rangle_{1}\langle\alpha^{\prime}|,(3.22)|α⟩k​⟨α′|(α,α′=0,1)\displaystyle|\alpha\rangle_{k}\langle\alpha^{\prime}|_{(\alpha,\alpha^{\prime}=0,1)}=\displaystyle=([1−ck+​ck]ckck+[ck+​ck])\displaystyle{\left({\begin{array}[]{cc}[1-c^{+}_{k}c_{k}]&c_{k}\\
c^{+}_{k}&[c^{+}_{k}c_{k}]\end{array}}\right)}(3.25)

Here,p​(α)p(\alpha)denotes the fermionic parity of the state, defined asp​(α)=αp(\alpha)=\alpha, withα=0,1\alpha=0,1.

Substituting these expressions, we obtainℛ12\displaystyle\mathcal{R}_{12}=\displaystyle=R0000+(R0101−R0000)​c1+​c1+(R1010−R0000)​c2+​c2+R0110​c1+​c2+R1001​c2+​c1\displaystyle R_{00}^{00}+(R_{01}^{01}-R_{00}^{00})c^{+}_{1}c_{1}+(R_{10}^{10}-R_{00}^{00})c^{+}_{2}c_{2}+R_{01}^{10}c^{+}_{1}c_{2}+R_{10}^{01}c^{+}_{2}c_{1}(3.26)+\displaystyle+R0011c2+c1++R1100c2c1++[R0000−R1010−R0101−R1111]c2+c2c1+c1.\displaystyle R_{00}^{11}c^{+}_{2}c^{+}_{1}+R_{11}^{00}c_{2}c_{1}++[R_{00}^{00}-R_{10}^{10}-R_{01}^{01}-R_{11}^{11}]c^{+}_{2}c_{2}c^{+}_{1}c_{1}.

ForRR-matrices satisfying the above-mentioned free-fermion condition, the operatorℛ12\mathcal{R}_{12}admits a particularly simple representation in terms of an exponential of a quadratic form in fermionic operators. More precisely, it can be written as the exponential of a local (cell) action𝒜12​(c+,c)\mathcal{A}_{12}(c^{+},c), which is quadratic in the fermionic creation and annihilation operators. Here, the symbol::::denotes normal ordering with respect to the fermionic operators.ℛ12\displaystyle\mathcal{R}_{12}=\displaystyle=R0000:e𝒜12​(c+,c):,\displaystyle R_{00}^{00}:e^{\mathcal{A}_{12}(c^{+},c)}:,(3.27)

where the quadratic form𝒜12​(c+,c)\mathcal{A}_{12}(c^{+},c)is given by𝒜12​(c+,c)\displaystyle\mathcal{A}_{12}(c^{+},c)=\displaystyle=(R0101R0000−1)​c1+​c1+(R1010R0000−1)​c2+​c2+\displaystyle\left(\frac{R_{01}^{01}}{R_{00}^{00}}-1\right)c^{+}_{1}c_{1}+\left(\frac{R_{10}^{10}}{R_{00}^{00}}-1\right)c^{+}_{2}c_{2}+(3.28)R0110R0000​c2+​c1+R1001R0000​c1+​c2+R0011R0000​c2+​c1++R1100R0000​c2​c1.\displaystyle\frac{R_{01}^{10}}{R_{00}^{00}}c^{+}_{2}c_{1}+\frac{R_{10}^{01}}{R_{00}^{00}}c^{+}_{1}c_{2}+\frac{R_{00}^{11}}{R_{00}^{00}}c^{+}_{2}c^{+}_{1}+\frac{R_{11}^{00}}{R_{00}^{00}}c_{2}c_{1}.

This representation makes explicit the quadratic (free-fermion) structure of the model and provides a convenient starting point for further analytical treatment, in particular for constructing the corresponding Grassmann path integral.

The indexing of the states on the lattice can be introduced as follows (see Fig. 1):Figure 2:R-operator

The periodic boundary conditions imposed on the spin variables of the two-dimensional lattice translate into antiperiodic boundary conditions for the corresponding fermionic variables. This must be taken into account when passing to Grassmann field variablesψ,ψ¯\psi,\bar{\psi}in order to represent the trace in the partition function as a functional integral.

The fermionic variablesψ,ψ¯\psi,\bar{\psi}are associated with coherent states (eigenstates) of the fermionic annihilation operators,|ψ⟩=ec+​ψ​|0⟩,c​|ψ⟩=ψ​|ψ⟩.|\psi\rangle=e^{c^{+}\psi}|0\rangle,\qquad c|\psi\rangle=\psi|\psi\rangle.

To avoid repeating the detailed derivations presented in Ref.[28], we provide here only the key formulas, using a compact notation.Z\displaystyle Z=\displaystyle=t​r​∏i​jRi​j=[R0000]N×N​∫D​ψ¯​D​ψ​e−∑i​jA​(χ¯,ψ)i​j,\displaystyle tr\prod_{ij}R_{ij}=[R_{00}^{00}]^{N\times N}\int D\bar{\psi}D\psi e^{-\sum_{ij}{A}(\bar{\chi},\psi)_{ij}},(3.29)ψ(i,j)\displaystyle\psi_{(i,j)}=\displaystyle=(ψ​(2​i,2​j)ψ​(2​i+1,2​j−1)),χ¯(i,j)=(ψ¯​(2​i+2,2​j),ψ¯​(2​i+1,2​j+1))\displaystyle\left(\begin{array}[]{c}\psi(2i,2j)\\
\psi(2i+1,2j-1)\end{array}\right),\quad\bar{\chi}_{(i,j)}=\left(\begin{array}[]{cc}\bar{\psi}(2i+2,2j),&\bar{\psi}(2i+1,2j+1)\end{array}\right)(3.33)ψ(i,j)\displaystyle\psi_{(i,j)}=\displaystyle=−ψ(i+N,j),ψ(i,j)=−ψ(i,j+N),χ¯(i,j)=−χ¯(i+N,j),χ¯(i,j)=−χ¯(i,j+N)\displaystyle-\psi_{(i+N,j)},\quad\psi_{(i,j)}=-\psi_{(i,j+N)},\quad\bar{\chi}_{(i,j)}=-\bar{\chi}_{(i+N,j)},\quad\bar{\chi}_{(i,j)}=-\bar{\chi}_{(i,j+N)}\qquad(3.34)

The above relations encode the antiperiodic boundary conditions for the fermionic fields on the torus.

The fermionic action can be written as−\displaystyle-A​(ψ¯,ψ)i​j=−∑i​j[ψ¯​(2​i,2​j)​ψ​(2​i,2​j)+ψ¯​(2​i+1,2​j+1)​ψ​(2​i+1,2​j+1)]\displaystyle A(\bar{\psi},\psi)_{ij}=-\sum_{ij}\left[\bar{\psi}(2i,2j){\psi}(2i,2j)+\bar{\psi}(2i+1,2j+1){\psi}(2i+1,2j+1)\right](3.37)+\displaystyle+∑jψ¯​(2​N,2​j)​ψ​(0,2​j)+∑iψ¯​(2​N+1,2​j+1)​ψ​(1,2​j+1)+∑i,jχ¯(i,j)​(R0101R0000R0110R0000R1001R0000R1010R0000)​ψ(i,j)\displaystyle\sum_{j}\bar{\psi}(2N,2j){\psi}(0,2j)+\sum_{i}\bar{\psi}(2N+1,2j+1){\psi}(1,2j+1)+\sum_{i,j}\bar{\chi}_{(i,j)}\left(\begin{array}[]{cc}\frac{R_{01}^{01}}{R_{00}^{00}}&\frac{R_{01}^{10}}{R_{00}^{00}}\\
\frac{R_{10}^{01}}{R_{00}^{00}}&\frac{R_{10}^{10}}{R_{00}^{00}}\end{array}\right)\psi_{(i,j)}+\displaystyle+∑i,j[R1100R0000​ψ¯​(2​i+2,2​j)​ψ¯​(2​i+1,2​j+1)+R0011R0000​ψ​(2​i,2​j)​ψ​(2​i+1,2​j−1)]\displaystyle\sum_{i,j}\left[\frac{R_{11}^{00}}{R_{00}^{00}}\bar{\psi}(2i+2,2j)\bar{\psi}(2i+1,2j+1)+\frac{R_{00}^{11}}{R_{00}^{00}}{\psi}(2i,2j){\psi}(2i+1,2j-1)\right](3.38)

Since the action is quadratic in the Grassmann variables, the partition function can be evaluated exactly by transforming to momentum space. In this representation, the model describes free scalar fermions with periodic hopping amplitudes on a toroidal lattice.

Due to the antiperiodic boundary conditions, the Fourier expansion must be performed over half-integer (odd) momenta[28]:ψ(i,j)=1N​∑i,jN(e−i​π2​N​((2​ni+1)​(2​i)+(2​nj+1)​(2​j))​ψ1​(π​(2​ni+1)2​N,π​(2​nj+1)2​N)e−i​π2​N​((2​ni+1)​(2​i+1)+(2​nj+1)​(2​j−1))​ψ2​(π​(2​ni+1)2​N,π​(2​nj+1)2​N))\displaystyle\psi_{(i,j)}=\frac{1}{N}\sum_{i,j}^{N}\left(\begin{array}[]{c}e^{-\frac{i\pi}{2N}\left((2n_{i}+1)(2i)+(2n_{j}+1)(2j)\right)}\psi_{1}{(\frac{\pi(2n_{i}+1)}{2N},\frac{\pi(2n_{j}+1)}{2N})}\\
e^{-\frac{i\pi}{2N}\left((2n_{i}+1)(2i+1)+(2n_{j}+1)(2j-1)\right)}\psi_{2}{(\frac{\pi(2n_{i}+1)}{2N},\frac{\pi(2n_{j}+1)}{2N})}\end{array}\right)(3.41)

whereni,nj=1,…,Nn_{i},\;n_{j}=1,\dots,N.

To diagonalize the action, it is convenient to redefine the fermionic Fourier modesψk​(ni,nj)\psi_{k(n_{i},n_{j})},k=1,2k=1,2, by restricting the momentum space to half of the Brillouin zone,ni=1,…,[N]/2n_{i}=1,\dots,[N]/2,nj=1,…,Nn_{j}=1,\dots,N, and introducing the following relations:ψ1​(N−ni,N−nj)≡−ψ¯3​(ni,nj),ψ2​(N−ni,N−nj)≡−ψ¯4​(ni,nj)\displaystyle\psi_{1(N-n_{i},N-n_{j})}\equiv-\bar{\psi}_{3(n_{i},n_{j})},\quad\psi_{2(N-n_{i},N-n_{j})}\equiv-\bar{\psi}_{4(n_{i},n_{j})}ψ¯1​(N−ni,N−nj)≡ψ3​(ni,nj),ψ¯2​(N−ni,N−nj)≡ψ4​(ni,nj).\displaystyle\bar{\psi}_{1(N-n_{i},N-n_{j})}\equiv{\psi}_{3(n_{i},n_{j})},\quad\bar{\psi}_{2(N-n_{i},N-n_{j})}\equiv{\psi}_{4(n_{i},n_{j})}.(3.42)

This transformation leads to the following expression for the effective fermionic action in momentum space:∑i,jN,NA​(ψ¯,ψ)i​j=∑ni,njN2,N∑k,r4ψ¯k​(ni,nj)​𝒜k​r​(ni,nj)​ψr​(ni,nj),\displaystyle\sum_{i,j}^{N,N}A(\bar{\psi},\psi)_{ij}=\sum_{n_{i},n_{j}}^{\frac{N}{2},N}\sum_{k,r}^{4}\bar{\psi}_{k(n_{i},n_{j})}\mathcal{A}_{kr(n_{i},n_{j})}{\psi}_{r(n_{i},n_{j})},(3.43)

where the matrix𝒜(ni,nj)\mathcal{A}_{(n_{i},n_{j})}is given by𝒜(ni,nj)=(R0101R0000​ei​π​(2​ni+1)N−1R0110R0000​ei​π​(ni+nj+1)N0−R1100R0000​ei​π​(ni−nj)NR1001R0000​ei​π​(ni+nj+1)NR1010R0000​ei​π​(2​nj+1)N−1R1100R0000​ei​π​(nj−ni​1)N00R0011R0000​ei​π​(nj−ni)NR0101R0000​e−i​π​(2​ni+1)N−1R1001R0000​e−i​π​(ni+nj+1)N−R0011R0000​ei​π​(ni−nj)N0R0110R0000​e−i​π​(ni+nj+1)NR1010R0000​e−i​π​(2​nj+1)N−1).\displaystyle\mathcal{A}_{(n_{i},n_{j})}\!=\!\!\left(\!\!\begin{array}[]{cccc}\frac{R_{01}^{01}}{R_{00}^{00}}e^{\frac{i\pi(2n_{i}+1)}{N}}-1&\frac{R_{01}^{10}}{R_{00}^{00}}e^{\frac{i\pi(n_{i}+n_{j}+1)}{N}}&0&-\frac{R_{11}^{00}}{R_{00}^{00}}e^{\frac{i\pi(n_{i}-n_{j})}{N}}\\
\frac{R_{10}^{01}}{R_{00}^{00}}e^{\frac{i\pi(n_{i}+n_{j}+1)}{N}}&\frac{R_{10}^{10}}{R_{00}^{00}}e^{\frac{i\pi(2n_{j}+1)}{N}}-1&\frac{R_{11}^{00}}{R_{00}^{00}}e^{\frac{i\pi(n_{j}-n_{i}1)}{N}}&0\\
0&\frac{R_{00}^{11}}{R_{00}^{00}}e^{\frac{i\pi(n_{j}-n_{i})}{N}}&\frac{R_{01}^{01}}{R_{00}^{00}}e^{\frac{-i\pi(2n_{i}+1)}{N}}-1&\frac{R_{10}^{01}}{R_{00}^{00}}e^{-\frac{i\pi(n_{i}+n_{j}+1)}{N}}\\
-\frac{R_{00}^{11}}{R_{00}^{00}}e^{\frac{i\pi(n_{i}-n_{j})}{N}}&0&\frac{R_{01}^{10}}{R_{00}^{00}}e^{-\frac{i\pi(n_{i}+n_{j}+1)}{N}}&\frac{R_{10}^{10}}{R_{00}^{00}}e^{\frac{-i\pi(2n_{j}+1)}{N}}-1\end{array}\!\!\right).(3.48)

————————————————————————————–

The action in momentum space decomposes into independent blocks labeled by(ni,nj)(n_{i},n_{j}).
For each momentum sector, it takes the form of a4×44\times 4matrix, similar to the structure
of the eight-vertex (or IM) model on the square lattice[28]. As a result, the partition
function factorizes into a product of determinants:Z=[R0000]N×N​∏ni,njN/2,NDet​𝒜(ni,nj),\displaystyle Z=[R_{00}^{00}]^{N\times N}\prod_{n_{i},n_{j}}^{N/2,N}\mathrm{Det}{\mathcal{A}_{(n_{i},n_{j})}},(3.49)

Each determinant can be calculated explicitly and has the simple form[Det​𝒜(ni,nj)]​[R0000]2\displaystyle\left[\mathrm{Det}{\mathcal{A}_{(n_{i},n_{j})}}\right][R_{00}^{00}]^{2}=\displaystyle=𝔸1+𝔸2​cos⁡[π​(2​ni+1)N]+𝔸3​cos⁡[π​(2​nj+1)N]\displaystyle\mathbb{A}_{1}+\mathbb{A}_{2}\cos{[\frac{\pi(2n_{i}+1)}{N}]}+\mathbb{A}_{3}\cos{[\frac{\pi(2n_{j}+1)}{N}]}+\displaystyle+𝔸4​cos⁡[π​(ni+nj+1)N]+𝔸5​cos⁡[π​(ni−nj)N],\displaystyle\mathbb{A}_{4}\cos{[\frac{\pi(n_{i}+n_{j}+1)}{N}]}+\mathbb{A}_{5}\cos{[\frac{\pi(n_{i}-n_{j})}{N}]},

where𝔸1\displaystyle\hskip-34.14322pt\mathbb{A}_{1}=\displaystyle=4​((6+3​∑k3cosh⁡[4​Jk])+∏k3sinh⁡[4​Jk]+∏k3cosh⁡[4​Jk]),\displaystyle 4((6+3\sum_{k}^{3}\cosh{[4J_{k}]})+\prod_{k}^{3}\sinh{[4J_{k}]}+\prod_{k}^{3}\cosh{[4J_{k}]}),(3.51)𝔸2\displaystyle\hskip-34.14322pt\mathbb{A}_{2}=\displaystyle=−32​sinh⁡[2​J2]​(cosh⁡[2​J2]​sinh⁡[2​J1]​sinh⁡[2​J3]+sinh⁡[2​J2]​cosh⁡[2​J1]​cosh⁡[2​J3]),\displaystyle-32\sinh{[2J_{2}]}(\cosh{[2J_{2}]}\sinh{[2J_{1}]}\sinh{[2J_{3}]}+\sinh{[2J_{2}]}\cosh{[2J_{1}]}\cosh{[2J_{3}]}),(3.52)𝔸3\displaystyle\hskip-34.14322pt\mathbb{A}_{3}=\displaystyle=−32​sinh⁡[2​J3]​(cosh⁡[2​J3]​sinh⁡[2​J2]​sinh⁡[2​J1]+sinh⁡[2​J3]​cosh⁡[2​J2]​cosh⁡[2​J1]),\displaystyle-32\sinh{[2J_{3}]}(\cosh{[2J_{3}]}\sinh{[2J_{2}]}\sinh{[2J_{1}]}+\sinh{[2J_{3}]}\cosh{[2J_{2}]}\cosh{[2J_{1}]}),(3.53)𝔸4\displaystyle\hskip-34.14322pt\mathbb{A}_{4}=\displaystyle=−32​sinh⁡[2​J1]​(cosh⁡[2​J1]​sinh⁡[2​J2]​sinh⁡[2​J3]+sinh⁡[2​J1]​cosh⁡[2​J2]​cosh⁡[2​J3]),\displaystyle-32\sinh{[2J_{1}]}(\cosh{[2J_{1}]}\sinh{[2J_{2}]}\sinh{[2J_{3}]}+\sinh{[2J_{1}]}\cosh{[2J_{2}]}\cosh{[2J_{3}]}),(3.54)𝔸5\displaystyle\hskip-34.14322pt\mathbb{A}_{5}=\displaystyle=[R0101]​[R1010]−[R0011]​[R1100]=0.\displaystyle[R_{01}^{01}][R_{10}^{10}]-[R_{00}^{11}][R_{11}^{00}]=0.(3.55)

## 4Critical points

The partition function can be written in a compact product form by introducing the notation𝔸​[J1,J2,J3]≡𝔸2\mathbb{A}[J_{1},J_{2},J_{3}]\equiv\mathbb{A}_{2}(see Eq.3.52) andpi​j≡[π​(ni+nj+1)N]p_{ij}\equiv[\frac{\pi(n_{i}+n_{j}+1)}{N}]:Z​(J1,J2,J3)=∏ni,njN2,N{𝔸1+𝔸​[J1,J2,J3]​cos⁡pi​i+𝔸​[J2,J3,J1]​cos⁡pj​j+𝔸​[J3,J1,J2]​cos⁡pi​j}\displaystyle Z(J_{1},J_{2},J_{3})=\prod_{n_{i},n_{j}}^{\frac{N}{2},N}\Big\{\mathbb{A}_{1}+\mathbb{A}[J_{1},J_{2},J_{3}]\cos{p_{ii}}+\mathbb{A}[J_{2},J_{3},J_{1}]\cos{p_{jj}}+\mathbb{A}[J_{3},J_{1},J_{2}]\cos{p_{ij}}\Big\}

The critical behavior of the system is determined by the zeroes of the determinant.
These zeroes correspond to singularities of the free energy and therefore define the
critical surface.

As in the ordinary Ising model on the square lattice, the thermodynamic limitN→∞N\to\inftyis controlled by the long-wavelength modes. In particular, one must consider the sector
withni=0n_{i}=0andnj=0,N−1n_{j}=0,N-1. In these points the zeroes of the partition function are determined by the equation(∑k=13cosh⁡[2​Jk]−∏k=13sinh⁡[2​Jk]−∏k=13cosh⁡[2​Jk])=0\displaystyle\left(\sum_{k=1}^{3}\cosh{[2J_{k}]}-\prod_{k=1}^{3}\sinh{[2J_{k}]}-\prod_{k=1}^{3}\cosh{[2J_{k}]}\right)=0(4.57)

which defines the critical surface (Fig. 3).
All calculations presented so far are valid for arbitrary signs of the coupling constants. Therefore, in Fig. 3 we show both the positive and negative regions of the coupling-constant parameter space.
Equation (4.57) has two analytic solutions expressingJ3J_{3}viaJ1,2J_{1,2}:J3±=12​log⁡[(cosh⁡2​[J1]±cosh⁡[2​J2])2[cosh[2(J1+J2])−1]]\displaystyle J_{3}^{\pm}=\frac{1}{2}\log\Big[\frac{\big(\sqrt{\cosh 2[J_{1}]}\pm\sqrt{\cosh[2J_{2}]}\big)^{2}}{[\cosh{[2(J_{1}+J_{2}])}-1]}\Big](4.58)

The choiceJ1,2,3>0J_{1,2,3}>0corresponds to the ferromagnetic model, for which we present below the isotropic limit as a particular case. Equation (4.57) is invariant under the simultaneous sign reversal of any two coupling constants,JkJ_{k}andJpJ_{p}. In contrast, if only one coupling constant or all three coupling constants change sign, the equation is no longer invariant and yields different solutions. This gives rise to the exotic frustration effects characteristic of the antiferromagnetic phases.Figure 3:Critical subsurfaces on the real coordinate space {J1,J2,J3J_{1},J_{2},J_{3}}

The factorization of the partition function into momentum-dependent determinants is the consequence of that
the model has an effective quadratic (free-fermion–like) structure. Each momentum mode
contributes independently to the thermodynamics. The critical surface is determined by the condition that the momentum-space fermionic kernel develops a zero eigenvalue at some momentum in the Brillouin zone. Equivalently,d​e​t​A​(p0,q0)=0detA(p_{0},q_{0})=0for a certain(p0,q0)(p_{0},q_{0}). In ferromagnetic case usuallyp0=q0=0p_{0}=q_{0}=0, while in frustrated
case gap may disappear in the corner of Brillouin zone.
This does not imply that the free energy vanishes; rather, the logarithmic integrand becomes singular, producing a nonanalyticity of the free energy in the thermodynamic limit. Since the vanishing eigenvalue corresponds to a zero fermionic mass, the fermionic spectrum is gapless at every physical point of the critical surface.
This corresponds to the closing of the excitation
gap and leads to a second-order phase transition. Compared to the square-lattice Ising model,
the form of the critical condition is modified by the kagomé lattice geometry and by the
presence of three coupling constants, but the physical mechanism remains the same.

For the isotropic case we have(3+cosh⁡[4​Jc]−2​sinh⁡[4​Jc])=0,sinh⁡2​Jc=234,\displaystyle\left(3+\cosh{[4J_{c}]-2\sinh{[4J_{c}]}}\right)=0,\quad\sinh{2J_{c}}=\frac{\sqrt{2}}{\sqrt[4]{3}},(4.59)

which agrees with the results of Refs.[19,33,21]and gives the known numerical value1/Jc≈2.14332\displaystyle 1/{J_{c}}\approx 2.14332(4.60)

For other momentum values, the partition function may have zeroes at complex temperatures. These are Fisher zeroes and do not correspond to physical phase transitions on the real temperature axis.

In the limit where one of the coupling constantsJkJ_{k}vanishes, the model reduces to the ordinary square-lattice Ising model. In the caseJ​[1]=0J[1]=0, the equation (4.57) for critical couplings become(1−2sinh[J2]2sinh[J3]2)=0,\displaystyle(1-2\sinh{[J_{2}]}^{2}\sinh{[J_{3}]}^{2})=0,(4.61)

which reproduces the standard result.
Indeed, from Fig. 1 it is easy to see that, upon settingJ1=0J_{1}=0, the hopping terms in the action (2.1) along direction11disappear, leaving a modified square (regular) lattice with additional sites of degree22inserted in the middle of the links carrying couplingsJ2J_{2}andJ3J_{3}. The spins on these degree-22sites can be summed over exactly in the partition function, yielding renormalized couplings for the ordinary Ising model on the square lattice. Namely, for each link along thea=2,3a=2,3directions, the two hopping terms contribute∑s0=±1eJa​s1​s0+Ja​s0​s2=∑s0=±1(cosh⁡[Ja]+sinh⁡[Ja]​s1​s0)​(cosh⁡[Ja]+sinh⁡[Ja]​s0​s2)\displaystyle\sum_{s_{0}=\pm 1}e^{J_{a}s_{1}s_{0}+J_{a}s_{0}s_{2}}=\sum_{s_{0}=\pm 1}\left(\cosh[J_{a}]+\sinh[J_{a}]s_{1}s_{0}\right)\left(\cosh[J_{a}]+\sinh[J_{a}]s_{0}s_{2}\right)(4.62)=\displaystyle=2(cosh[Ja]2+sinh[Ja]2s1s2)=2eJ¯a(cosh[J¯a]+sinh[J¯a]s1s2),\displaystyle 2\left(\cosh[J_{a}]^{2}+\sinh[J_{a}]^{2}s_{1}s_{2}\right)=2e^{\bar{J}_{a}}\left(\cosh[\bar{J}_{a}]+\sinh[\bar{J}_{a}]s_{1}s_{2}\right),

is precisely the Boltzmann weight of the Ising model on the regular square lattice with the renormalized couplingJ¯a\bar{J}_{a}. Comparing both sides, one immediately obtainse2​J¯a=cosh⁡(2​Ja).\displaystyle e^{2\bar{J}_{a}}=\cosh(2J_{a}).(4.63)

This equation, or equivalently the equationtanh⁡J¯a=(tanh⁡Ja)2\tanh{\bar{J}_{a}}=(\tanh{J_{a}})^{2}shows, that the resulting
two dimensional square Ising model must be ferromagnetic. The critical equation for the square IM with couplingsJ¯a=2,3\bar{J}_{a=2,3}can be presented by(1−sinh⁡2​J¯2​sinh⁡2​J¯3=0)(1-\sinh{2\bar{J}_{2}}\sinh{2\bar{J}_{3}}=0)or, equivalently, for the ferromagnetic IM, by relationse−2​J¯2,3=tanh⁡J¯3,2e^{-2\bar{J}_{2,3}}=\tanh{\bar{J}_{3,2}}, as1−sinh⁡[2​J¯]​sinh⁡[2​J¯′]=(1−e2​J¯​tanh⁡[J¯′])​(1+e−2​J¯​tanh⁡[J¯])​cosh⁡[J¯]​cosh⁡[J¯′]​eJ¯−J¯′\displaystyle 1-\sinh{[2\bar{J}]}\sinh{[2\bar{J}^{\prime}]}=\left(1-e^{2\bar{J}}\tanh[\bar{J}^{\prime}]\right)\left(1+e^{-2\bar{J}}\tanh[\bar{J}]\right)\cosh[\bar{J}]\cosh[\bar{J}^{\prime}]e^{\bar{J}-\bar{J}^{\prime}}

Denote, duality transformation of the square
lattice equivalent to interchanging of couplingsJ2,3→J3,2J_{2,3}\rightarrow J_{3,2}. Applying the transformation
expression (4.63) we find out(1−e2​J¯2tanh[J¯3])=1−cosh[2J2]tanh[J3]2=1−2sinh[J2]2sinh[J3]2cosh[J3]2=0,\displaystyle(1-e^{2\bar{J}_{2}}\tanh{[\bar{J}_{3}]})=1-\cosh{[2J_{2}]}\tanh{[J_{3}]}^{2}=\frac{1-2\sinh{[J_{2}]}^{2}\sinh{[J_{3}]}^{2}}{\cosh[J_{3}]^{2}}=0,(4.64)

coinciding with the equation (4.61).

It is straightforward to check also, that in the homogeneous caseJ2=J3=J=arcsinh⁡(2−1/4)J_{2}=J_{3}=J=\operatorname{arcsinh}(2^{-1/4}), the solution of Eq. (4.61) reproduces the well-known critical coupling of the square-lattice Ising model,2​J¯a=ln⁡[cosh⁡[2​arcsinh⁡[2−1/4]]]=arcsinh⁡[1].\displaystyle 2\bar{J}_{a}=\ln\left[\cosh[2\;\operatorname{arcsinh}[2^{-1/4}]]\right]=\operatorname{arcsinh}[1].(4.65)

Hence, the criticality condition (4.57) for the kagom’e Ising model correctly reduces to the exact critical coupling of the two-dimensional square-lattice Ising model[12].

We can consider also second coupling to be zeroJ2=0J_{2}=0, then we have one dimensional Ising limit. Taking limitJ2→0J_{2}\rightarrow 0in the solution of equation (4.61) we getlimJ2→0sinh⁡[J3]=limJ2→012​sinh⁡[J2]=∞,\displaystyle\lim_{J_{2}\rightarrow 0}\sinh[J_{3}]=\lim_{J_{2}\rightarrow 0}\frac{1}{2\sinh[J_{2}]}=\infty,(4.66)

indicating that phase transition happened atJ3=∞J_{3}=\infty, equivalent toT=0T=0, which is precisely
critical point of 1dIM[12].

## Free energy per site and thermal capacity.

We now calculate the free energy of the 2D Ising model on the kagomé lattice in ferromagnetic case. In the thermodynamic limitN→∞N\to\infty, the sums over momenta can be replaced by integrals. At the same time, we restore the temperature dependence by the substitutionJ→J/TJ\to J/T:1N​∑niN/2→1π​∫0π/2𝑑p,1N​∑njN→1π​∫0π𝑑q,J→JT.\displaystyle\frac{1}{N}\sum_{n_{i}}^{N/2}\to\frac{1}{\pi}\int_{0}^{\pi/2}dp,\quad\frac{1}{N}\sum_{n_{j}}^{N}\to\frac{1}{\pi}\int_{0}^{\pi}dq,\qquad J\to\frac{J}{T}.(4.67)

This leads to the following integral expression for the free energy in the continuum limit:F\displaystyle F=\displaystyle=−(T​ln​Z)N2=−TN2​∑(ni,nj)N/2,Nln​[Det​𝒜(ni,nj)​[R0000]2]\displaystyle-\frac{(T\mathrm{ln}Z)}{N^{2}}=-\frac{T}{N^{2}}\sum_{(n_{i},n_{j})}^{N/2,N}\mathrm{ln}\left[\mathrm{Det}{\mathcal{A}_{(n_{i},n_{j})}}[R_{00}^{00}]^{2}\right]=\displaystyle=−Tπ2​∫0π/2𝑑p​∫0π𝑑q​ln⁡[𝔸1+𝔸2​cos⁡[2​p]+𝔸3​cos⁡[2​q]+𝔸4​cos⁡[2​(p+q)]],\displaystyle-\frac{T}{\pi^{2}}\int_{0}^{\pi/2}dp\int_{0}^{\pi}dq\ln\left[\mathbb{A}_{1}+\mathbb{A}_{2}\cos{[2p]}+\mathbb{A}_{3}\cos{[2q]}+\mathbb{A}_{4}\cos{[2(p+q)]}\right],

This expression has the same structure as in other exactly solvable lattice models.

In the isotropic case, the coefficients𝔸k\mathbb{A}_{k}withk=2,3,4k=2,3,4become equal. The free energy then simplifies toF\displaystyle\hskip-56.9055ptF=\displaystyle=−Tπ2​∫0π2𝑑p​∫0π𝑑q​ln⁡[𝔸1+𝔸​[JT,JT,JT]​(cos⁡[2​p]+cos⁡[2​q]+cos⁡[2​(p+q)])]\displaystyle-\frac{T}{\pi^{2}}\int_{0}^{\frac{\pi}{2}}dp\int_{0}^{\pi}dq\ln\left[\mathbb{A}_{1}+\mathbb{A}\Big[\frac{J}{T},\frac{J}{T},\frac{J}{T}\Big]\big(\cos{[2p]}+\cos{[2q]}+\cos{[2(p+q)]}\big)\right]=\displaystyle=−Tπ2∫0π2dp∫0πdq×ln[24+21e−4​J+18e4​J+e12​J−32e2​Jsinh[2J]2cosh[2J]\displaystyle-\frac{T}{\pi^{2}}\int_{0}^{\frac{\pi}{2}}dp\int_{0}^{\pi}dq\times\ln\left[24+21e^{-4J}+18e^{4J}+e^{12J}-32\;e^{2J}\sinh[2J]^{2}\cosh[2J]\right.×\displaystyle\times(cos[2p]+cos[2q]+cos[2(p+q)])]\displaystyle\left.(\cos[2p]+\cos[2q]+\cos[2(p+q)])\right]

After obtaining the free energy, the thermal capacity can be calculated in a standard way:C=−T​∂2F∂T2,\displaystyle C=-T\frac{\partial^{2}F}{\partial T^{2}},(4.70)

This leads to expressions involving complete elliptic integralsEEandKK, similar to the square-lattice Ising model, where the same method reproduces Onsager’s result[28]. To avoid very long expressions, we consider only the isotropic case.

Introducing the notationz≡e4​JT,c​[p,q]≡cos⁡2​q+cos⁡2​p+cos⁡2​(p+q),\displaystyle z\equiv e^{\frac{4J}{T}},\quad c[p,q]\equiv\cos{2q}+\cos{2p}+\cos{2(p+q)},(4.71)

the heat capacity can be written asC=(2​JT​sinh⁡[4​JT])2((3+cosh[4​JT])−1π2∫0π/2dp∫0πdq×\displaystyle C=\left(\frac{2J}{T\sinh{[\frac{4J}{T}]}}\right)^{2}\left((3+\cosh{[\frac{4J}{T}]})-\frac{1}{\pi^{2}}\int_{0}^{\pi/2}dp\int_{0}^{\pi}dq\times\right.[45+291​z+501​z2+523​z3+159​z4+17​z5−z6+z7z​(21+24​z+18​z2+z4−4​c​[p,q]​(1−z)2​(1+z)2)]+\displaystyle\left.\left[\frac{{45+291z+501z^{2}+523z^{3}+159z^{4}+17z^{5}-z^{6}+z^{7}}}{z(21+24z+18z^{2}+z^{4}-4c[p,q](1-z)^{2}(1+z)^{2})}\right]+\right.(4.72)1π2∫0π/2dp∫0πdq[(3+z)​(3+6​z−z2)​(5+2​z+z2)(21+24​z+18​z2+z4−4​c​[p,q]​(1−z)2​(1+z))]2)\displaystyle\left.\frac{1}{\pi^{2}}\int_{0}^{\pi/2}dp\int_{0}^{\pi}dq\left[\frac{(3+z)(3+6z-z^{2})(5+2z+z^{2})}{(21+24z+18z^{2}+z^{4}-4c[p,q](1-z)^{2}(1+z))}\right]^{2}\right)

After performing the integrations, we obtain the final result:C=4​J2T2sinh[4​JT]2(3+cosh[4​JT])−4​J2T2sinh[4​JT]2π×\displaystyle C=\frac{4J^{2}}{T^{2}\sinh{[\frac{4J}{T}]}^{2}}\left(3+\cosh{[\frac{4J}{T}]}\right)-\frac{4J^{2}}{T^{2}\sinh{[\frac{4J}{T}]}^{2}\pi}\times\quad18+93​z+84​z2+58​z3+2​z4+z52​(5+2​z+z2)​E​l​l​i​p​t​i​k​𝐊​[16​(1+z)​(z−1)2(5+2​z+z2)2]\displaystyle\frac{18+93z+84z^{2}+58z^{3}+2z^{4}+z^{5}}{2(5+2z+z^{2})}Elliptik{\mathbf{K}}[\frac{16(1+z)(z-1)^{2}}{(5+2z+z^{2})^{2}}](4.73)−4​J2T2sinh[4​JT]2π​(3+z)22​E​l​l​i​p​t​i​k​𝐄​[16​(1+z)​(z−1)2(5+2​z+z2)2]\displaystyle-\frac{4J^{2}}{T^{2}\sinh{[\frac{4J}{T}]}^{2}\pi}\frac{(3+z)^{2}}{2}Elliptik{\mathbf{E}}[\frac{16(1+z)(z-1)^{2}}{(5+2z+z^{2})^{2}}]\quad

## Reduction to the square-lattice Ising model atJ1=0J_{1}=0.

As we have mentioned earlier atJ1=0J_{1}=0(or any other coefficient) we obtain square lattice.
Lets check this statement on free energy (4). AtJ1=0J_{1}=0the expressions (3.51) for coefficients becomeA1\displaystyle A_{1}=\displaystyle=16(cosh[2J2]2+1)(cosh[2J3]2+1)\displaystyle 16(\cosh[2J_{2}]^{2}+1)(\cosh[2J_{3}]^{2}+1)A2\displaystyle A_{2}=\displaystyle=−32cosh[2J3]sinh[2J2]2\displaystyle-32\cosh[2J_{3}]\sinh[2J_{2}]^{2}(4.74)A3\displaystyle A_{3}=\displaystyle=−32cosh[2J2]sinh[2J3]2,A4=A5=0\displaystyle-32\cosh[2J_{2}]\sinh[2J_{3}]^{2},\;\;A_{4}=A_{5}=0

and from (4) we obtain (below we skip the notation of the temperatureTTin the expressions ofJk/TJ_{k}/T)F​(0,J2,J3)\displaystyle\hskip 0.0ptF(0,J_{2},J_{3})=\displaystyle=−Tπ2∫0π/2dp∫0πdqln{16[(cosh[2J2]2+1)(cosh[2J3]2+1)\displaystyle-\frac{T}{\pi^{2}}\int_{0}^{\pi/2}dp\int_{0}^{\pi}dq\ln\Big\{16\Big[(\cosh[2J_{2}]^{2}+1)(\cosh[2J_{3}]^{2}+1)(4.75)−\displaystyle-2cosh[2J2]sinh[2J3]2cos[2p]−2cosh[2J3]sinh[2J2]2cos[2q]]}\displaystyle 2\cosh[2J_{2}]\sinh[2J_{3}]^{2}\cos[2p]-2\cosh[2J_{3}]\sinh[2J_{2}]^{2}\cos[2q]\Big]\Big\}

The integral over p can be taken precisely giving one dimensional integral form for free energyF​(0,J2,J3)\displaystyle F(0,J_{2},J_{3})=\displaystyle=−T2​π​∫0π𝑑q​ln⁡[8​(f0​(q)+M(q)2−4cosh[2J2]sinh[J3]4)],\displaystyle-\frac{T}{2\pi}\int_{0}^{\pi}dq\ln\Big[8\big(f_{0}(q)+\sqrt{M(q)^{2}-4\cosh[2J_{2}]\sinh[J_{3}]^{4}}\big)\Big],(4.76)

wheref0(q)=(cosh[2J2]2+1)(cosh[2J3]2+1)−2cosh[2J3]sinh[2J2]2cos[2q].\displaystyle f_{0}(q)=(\cosh[2J_{2}]^{2}+1)(\cosh[2J_{3}]^{2}+1)-2\cosh[2J_{3}]\sinh[2J_{2}]^{2}\cos[2q].(4.77)

This is the usual one-dimensional integral representation of the anisotropic square-lattice Ising free energy. Now, by using formulas (4.63) for renormalized couplings in
reduced Ising model from kagomé to square lattice one will getF​(0,J2,J3)=FI​s​i​n​g​(J¯2,J¯3)−T​ln⁡[4​cosh⁡[2​J2]​cosh⁡[2​J3]]\displaystyle F(0,J_{2},J_{3})=F_{Ising}(\bar{J}_{2},\bar{J}_{3})-T\ln\Big[4\sqrt{\cosh[2J_{2}]\cosh[2J_{3}]}\Big]Z​(0,J2,J3)=[4​cosh⁡[2​J2]​cosh⁡[2​J3]]N2​ZI​s​i​n​g​(J¯2,J¯3),\displaystyle Z(0,J_{2},J_{3})=\Big[4\sqrt{\cosh[2J_{2}]\cosh[2J_{3}]}\Big]^{N^{2}}Z_{Ising}(\bar{J}_{2},\bar{J}_{3}),(4.78)

which is sound with formula (4.63).

Thus, the free-energy expression obtained from the fermionic formulation is fully consistent with the reduction formula (4.63) and confirms that, atJ1=0J_{1}=0, the model is equivalent to the anisotropic square-lattice Ising model with renormalized couplingsJ¯2\bar{J}_{2}andJ¯3\bar{J}_{3}.

## Reduction to the Ising model on a line atJ1=J2=0J_{1}=J_{2}=0.

In this case we have only two nonzero coefficients in the general free energy expression
(4). Those areA1\displaystyle A_{1}=\displaystyle=32(cosh[2J3]2+1)\displaystyle 32(\cosh[2J_{3}]^{2}+1)(4.79)A2\displaystyle A_{2}=\displaystyle=−32sinh[2J3]2,A3=A4=A5=0.\displaystyle-32\sinh[2J_{3}]^{2},\;\qquad A_{3}=A_{4}=A_{5}=0.

Therefore, the free energy reduces toF​(0,0,J3)\displaystyle F(0,0,J_{3})=\displaystyle=−Tπ2∫0π/2dp∫0πdqln{32[cosh[2J3]2+1−sinh[2J3]2cos[2p]]}\displaystyle-\frac{T}{\pi^{2}}\int_{0}^{\pi/2}dp\int_{0}^{\pi}dq\ln\Big\{32\Big[\cosh[2J_{3}]^{2}+1-\sinh[2J_{3}]^{2}\cos[2p]\Big]\Big\}(4.80)

Since the integrand is independent of q, the q-integration gives a factorπ\piand
after integration over p we obtainF​(0,0,J3)=−T​ln⁡[4​(cosh⁡[2​J3]+1)].\displaystyle F(0,0,J_{3})=-T\ln\Big[4(\cosh[2J_{3}]+1)\Big].(4.81)

After making renormalization by (4.63) we receiveF​(0,0,J3)\displaystyle F(0,0,J_{3})=\displaystyle=F1​D​I​M​(J¯3)−T​ln⁡[4​eJ¯3],\displaystyle F_{1DIM}(\bar{J}_{3})-T\ln\Big[4e^{\bar{J}_{3}}\Big],F1​D​I​M​(J¯3)\displaystyle F_{1DIM}(\bar{J}_{3})=\displaystyle=−T​ln⁡[2​cosh⁡[J¯3]],\displaystyle-T\ln\Big[2\cosh[\bar{J}_{3}]\Big],(4.82)

whereF1​D​I​M​(J¯3)F_{1DIM}(\bar{J}_{3})is correct free energy of one dimensional Ising model.

## 5Spontaneous magnetization

In Ref.[28]we developed a method to calculate the magnetization in ferromagnetic case of two-dimensional spin models with the free-fermion property. The method is based
on a fermionic (Grassmann) representation of the model in terms of scalar
fermions and continuum functional integrals.

The spontaneous magnetization⟨s(i,j)⟩\langle s_{(i,j)}\ranglecan be obtained from the
long-distance behavior of the spin-spin correlation functions on an infiniteN×NN\times Nlattice:⟨σα​(i,j)⟩2=limN→∞​(limK→∞​⟨s(0,0)​s(K,K)⟩)=limN→∞​(limK→∞​⟨s(0,0)​s(0,K)⟩).\displaystyle\langle\sigma_{\alpha}(i,j)\rangle^{2}=\textrm{lim}_{N\to\infty}\left(\textrm{lim}_{K\to\infty}\langle s_{(0,0)}s_{(K,K)}\rangle\right)=\textrm{lim}_{N\to\infty}\left(\textrm{lim}_{K\to\infty}\langle s_{(0,0)}s_{(0,K)}\rangle\right).(5.83)

Thus, the spontaneous magnetization is determined by the asymptotic value of the
two-point correlation function at large separation.

In the general case, the finite-distance spin-spin correlation function in the
fermionic representation can be written as a Pfaffian. Without loss of generality,
one can fix a direction and consider even-even or odd-odd lattice sites.
For example, for even-even sites, the analysis of Ref.[28]givesG​(k)=⟨s(0,2​k)​s(0,0)⟩=⟨[c(0,2​k)++c(0,2​k)]​(∏r=0k[c(0,2​r)−c(0,2​r)+]​[c(0,2​r)++c(0,2​r)])​[c(0,0)−c(0,0)+]⟩.\displaystyle G(k)=\!\langle s_{(0,2k)}s_{(0,0)}\rangle\!=\!\langle[c^{+}_{(0,2k)}\!+\!c_{(0,2k)}]\!\left(\!\prod^{k}_{r=0}\![c_{(0,2r)}\!-\!c^{+}_{(0,2r)}]\![c^{+}_{(0,2r)}\!+\!c_{(0,2r)}]\!\right)[c_{(0,0)}\!-\!c^{+}_{(0,0)}]\rangle.(5.84)

Using translational invariance, the coordinates(0,0)(0,0)and(0,2​k)(0,2k)can be
shifted to arbitrary points(2​i,2​j)(2i,2j)and(2​i,2​j+2​k)(2i,2j+2k).

In the operator formulation, the expectation value of a spin-dependent functionf​[si,j]f[s_{i,j}]is defined as⟨f​[si,j]⟩=T​rs​[f​[si,j]​∏i,jRi,j].\displaystyle\langle f[s_{i,j}]\rangle=Tr_{s}\left[f[s_{i,j}]\prod_{i,j}R_{i,j}\right].(5.85)

To rewrite this expression as a Grassmann integral, the fermionic operators must
be brought to normal-ordered form. The spin variable can be expressed through
fermions using a two-dimensional analog of the Jordan–Wigner transformation
(see the Appendix of Ref.[28]):s(i,j)=[c(i,j)++c(i,j)]​∏(k,r)=(0,0)(i,j)[c(k,r)++c(k,r)]​[c(k,r)+−c(k,r)].\displaystyle s_{(i,j)}=[c_{(i,j)}^{+}+c_{(i,j)}]\prod_{(k,r)=(0,0)}^{(i,j)}[c^{+}_{(k,r)}+c_{(k,r)}][c^{+}_{(k,r)}-c_{(k,r)}].(5.86)

The path connecting(0,0)(0,0)and(i,j)(i,j)can be chosen arbitrarily, as discussed
in Ref.[28].

Applying Wick’s theorem, the correlation function (5.84) can be written as a
Gaussian Grassmann integral:G​(k)=∫D​χ​e12​∑i,j2​k𝒢i​j​χi​χj−∑ikχ2​i+1​χ2​i,\displaystyle G(k)=\int D\chi\,e^{\frac{1}{2}\sum_{i,j}^{2k}\mathcal{G}_{ij}\chi_{i}\chi_{j}-\sum_{i}^{k}\chi_{2i+1}\chi_{2i}},(5.87)

where𝒢i​j\mathcal{G}_{ij}is an antisymmetric matrix. Introducing the notationc(0,2​i)≡𝐜ic_{(0,2i)}\equiv\mathbf{c}_{i}, its elements are given by{𝒢(2​i,2​j),𝒢(2​i+1,2​j+1),𝒢(2​i,2​j+1)}=\displaystyle\{\mathcal{G}_{(2i,2j)},\mathcal{G}_{(2i+1,2j+1)},\mathcal{G}_{(2i,2j+1)}\}=(5.88){⟨[𝐜i++𝐜i][𝐜j++𝐜j]⟩,⟨[𝐜i+−𝐜i][𝐜j+−𝐜j]⟩,⟨[𝐜i++𝐜i][𝐜j+−𝐜j]⟩.}\displaystyle\{\langle[\mathbf{c}^{+}_{i}+\mathbf{c}_{i}][\mathbf{c}^{+}_{j}+\mathbf{c}_{j}]\rangle,\langle[\mathbf{c}^{+}_{i}-\mathbf{c}_{i}][\mathbf{c}^{+}_{j}-\mathbf{c}_{j}]\rangle,\langle[\mathbf{c}^{+}_{i}+\mathbf{c}_{i}][\mathbf{c}^{+}_{j}-\mathbf{c}_{j}]\rangle.\}

These matrix elements admit the following integral representation:𝒢(i,j)=(R0000)N2Z​∫D​ψ¯​D​ψ​eA​(ψ¯,ψ)​(x1′​ψ(0,2​i)+x2′​ψ(1,2​i−1)+x3′​ψ¯(2,2​i)+x4′​ψ¯(1,2​i+1))\displaystyle\mathcal{G}_{(i,j)}=\frac{(R_{00}^{00})^{N^{2}}}{Z}\int D\bar{\psi}D\psi\,e^{A(\bar{\psi},\psi)}\left(x^{\prime}_{1}\psi_{(0,2i)}+x^{\prime}_{2}\psi_{(1,2i-1)}+x^{\prime}_{3}\bar{\psi}_{(2,2i)}+x^{\prime}_{4}\bar{\psi}_{(1,2i+1)}\right)×(x1′′​ψ(0,2​j)+x2′′​ψ(1,2​j−1)+x3′′​ψ¯(2,2​j)+x4′′​ψ¯(1,2​j+1)).\displaystyle\times\left(x^{\prime\prime}_{1}\psi_{(0,2j)}+x^{\prime\prime}_{2}\psi_{(1,2j-1)}+x^{\prime\prime}_{3}\bar{\psi}_{(2,2j)}+x^{\prime\prime}_{4}\bar{\psi}_{(1,2j+1)}\right).(5.89)

Here we introduce the parameters{xa′,xc′′}\{x^{\prime}_{a},\;x^{\prime\prime}_{c}\}entering Eq. (5.88).
For even and odd matrix indices{k,r}\{k,r\}, they are defined as{x1,x2,x3,x4}o​d​de​v​e​n={±1,R0011R0000,R0101R0000,R0110R0000}.\displaystyle\{x_{1},x_{2},x_{3},x_{4}\}_{odd}^{even}=\{\pm 1,\frac{R_{00}^{11}}{R_{00}^{00}},\frac{R_{01}^{01}}{R_{00}^{00}},\frac{R_{01}^{10}}{R_{00}^{00}}\}.(5.90)

After transforming to the Fourier basis, the Grassmann integration leads to an
exact expression. For symmetricRR-matrices, this result was obtained in
Ref.[28]:𝒢(i,j)=1N2​∑n1=1,n2=1N/2,N∑l,p4ℱ​(j−i,x′,x′′,n1,n2)l​p​[𝒜−1]l​p​(n1,n2).\displaystyle\mathcal{G}_{(i,j)}=\frac{1}{N^{2}}\sum_{n_{1}=1,n_{2}=1}^{N/2,N}\sum_{l,p}^{4}\mathcal{F}(j-i,x^{\prime},x^{\prime\prime},n_{1},n_{2})^{lp}[\mathcal{A}^{-1}]_{lp}(n_{1},n_{2}).(5.91)

Here[𝒜−1]l​p[\mathcal{A}^{-1}]_{lp}is the inverse of the Fourier-transformed matrix
of the fermionic action (3.48). In the general (non-symmetric) case, the
functionsℱ\mathcal{F}have a more complicated structure. Using the notationa=[i−j]a=[i-j], we defineK=ei​2​π​(2​n2+1)​aN,k1=ei​π​(2​n1+1)N,k2=ei​π​(2​n2+1)N,{ℱ11,ℱ22,ℱ33,ℱ44}=\displaystyle K=e^{i2\pi\frac{(2n_{2}+1)a}{N}},\quad k_{1}=e^{i\pi\frac{(2n_{1}+1)}{N}},\quad k_{2}=e^{i\pi\frac{(2n_{2}+1)}{N}},\quad\{\mathcal{F}_{11},\mathcal{F}_{22},\mathcal{F}_{33},\mathcal{F}_{44}\}=(5.92){k12​(K​x3′​x1′′−x1′​x3′′K),k22​(K​x4′​x2′′−x2′​x4′′K),1k12​(x3′​x1′′K−x1′​x3′′​K),1k22​(x4′​x2′′K−x2′​x4′′​K)}\displaystyle\{k_{1}^{2}(Kx^{\prime}_{3}x^{\prime\prime}_{1}-\frac{x^{\prime}_{1}x^{\prime\prime}_{3}}{K}),k_{2}^{2}(Kx^{\prime}_{4}x^{\prime\prime}_{2}-\frac{x^{\prime}_{2}x^{\prime\prime}_{4}}{K}),\frac{1}{k_{1}^{2}}(\frac{x^{\prime}_{3}x^{\prime\prime}_{1}}{K}-x^{\prime}_{1}x^{\prime\prime}_{3}K),\frac{1}{k_{2}^{2}}(\frac{x^{\prime}_{4}x^{\prime\prime}_{2}}{K}-x^{\prime}_{2}x^{\prime\prime}_{4}K)\}{ℱ12,ℱ21,ℱ43,ℱ34}=\displaystyle\{\mathcal{F}_{12},\mathcal{F}_{21},\mathcal{F}_{43},\mathcal{F}_{34}\}=(5.93){k1​k2​(K​x3′​x2′′−x2′​x3′′K),k1​k2​(K​x4′​x1′′−x1′​x4′′K),1k1​k2​(x3′​x2′′K−x2′​x3′′​K),1k1​k2​(x4′​x1′′K−x1′​x4′′​K)}\displaystyle\{k_{1}k_{2}(Kx^{\prime}_{3}x^{\prime\prime}_{2}-\frac{x^{\prime}_{2}x^{\prime\prime}_{3}}{K}),k_{1}k_{2}(Kx^{\prime}_{4}x^{\prime\prime}_{1}-\frac{x^{\prime}_{1}x^{\prime\prime}_{4}}{K}),\frac{1}{k_{1}k_{2}}(\frac{x^{\prime}_{3}x^{\prime\prime}_{2}}{K}-x^{\prime}_{2}x^{\prime\prime}_{3}K),\frac{1}{k_{1}k_{2}}(\frac{x^{\prime}_{4}x^{\prime\prime}_{1}}{K}-x^{\prime}_{1}x^{\prime\prime}_{4}K)\}{ℱ23,ℱ32,ℱ41,ℱ14}=\displaystyle\{\mathcal{F}_{23},\mathcal{F}_{32},\mathcal{F}_{41},\mathcal{F}_{14}\}=(5.94)k2k1​{(K​x4′​x3′′−x3′​x4′′K),k2k1​(x2′​x1′′K−K​x1′​x2′′),k1k2​(x1′​x2′′K−x2′​x1′′​K),k1k2​(K​x3′​x4′′−x4′​x3′′K)}\displaystyle\frac{k_{2}}{k_{1}}\{(Kx^{\prime}_{4}x^{\prime\prime}_{3}-\frac{x^{\prime}_{3}x^{\prime\prime}_{4}}{K}),\frac{k_{2}}{k_{1}}(\frac{x^{\prime}_{2}x^{\prime\prime}_{1}}{K}-Kx^{\prime}_{1}x^{\prime\prime}_{2}),\frac{k_{1}}{k_{2}}(\frac{x^{\prime}_{1}x^{\prime\prime}_{2}}{K}-x^{\prime}_{2}x^{\prime\prime}_{1}K),\frac{k_{1}}{k_{2}}(Kx^{\prime}_{3}x^{\prime\prime}_{4}-\frac{x^{\prime}_{4}x^{\prime\prime}_{3}}{K})\}{ℱ13,ℱ31,ℱ42,ℱ24}=\displaystyle\{\mathcal{F}_{13},\mathcal{F}_{31},\mathcal{F}_{42},\mathcal{F}_{24}\}=(5.95){x3′​x3′′​(K−K−1),x1′​x1′′​(K−1−K),x2′​x2′′​(K−1−K),x4′​x4′′​(K−K−1)}\displaystyle\{x^{\prime}_{3}x^{\prime\prime}_{3}(K-{K}^{-1}),x^{\prime}_{1}x^{\prime\prime}_{1}({K}^{-1}-K),x^{\prime}_{2}x^{\prime\prime}_{2}({K}^{-1}-K),x^{\prime}_{4}x^{\prime\prime}_{4}(K-K^{-1})\}

For the 2D Ising model, the even-even and odd-odd matrix elements vanish in the
symmetric caseJ1=J2J_{1}=J_{2}, and also in the thermodynamic limitN→∞N\to\inftyfor
the inhomogeneous case. As a result, the Pfaffian reduces to a determinant of the
antisymmetric matrix𝒢2​i,2​j+1=−𝒢2​j+1,2​i\mathcal{G}_{2i,2j+1}=-\mathcal{G}_{2j+1,2i}. This matrix
has a Toeplitz structure, which allows one to evaluate the determinant exactly
using Szegö’s theorem.

Although the structure of theRR-matrix is similar to the symmetric case, there
are important differences. In general, the matrix elements are not symmetric, for
exampleR0101≠R1010R_{01}^{01}\neq R_{10}^{10}. As a result, the functions𝒢k,r\mathcal{G}_{k,r}have a more complicated form, as seen in Eq. (5.92).
For spins located at odd-odd sites, the correlation function⟨s(1,2​k+1)​s(1,1)⟩\langle s_{(1,2k+1)}s_{(1,1)}\rangleis obtained by the substitutionR0101↔R1010R_{01}^{01}\leftrightarrow R_{10}^{10}.

We now write explicit expressions for the matrix elements
(5.87,5.89) in the thermodynamic limit:𝒢(2​i,2​j)\displaystyle\mathcal{G}_{(2i,2j)}=\displaystyle=𝒢(2​j+1,2​i+1)=∫0π∫0π2d​pπ​d​qπ​4​sin⁡[2​(i−j)​q]​(g1​sin⁡[2​(p+q)]+g2​sin⁡[2​p])det𝒜​(p,q),\displaystyle\mathcal{G}_{(2j+1,2i+1)}=\int_{0}^{\pi}\int_{0}^{\frac{\pi}{2}}\frac{dp}{\pi}\frac{dq}{\pi}\frac{4\sin{[2(i-j)q]}\left(g_{1}\sin{[2(p+q)]}+g_{2}\sin{[2p]}\right)}{\det{\mathcal{A}}(p,q)},\qquad\qquad(5.96)𝒢(2​i,2​j+1)\displaystyle\mathcal{G}_{(2i,2j+1)}=\displaystyle=−𝒢(2​j+1,2​i)=∫0π∫0π2d​pπd​qπ(sin⁡[2​(i−j)​q]​(g3​sin⁡[2​q])det𝒜​(p,q)\displaystyle-\mathcal{G}_{(2j+1,2i)}=\int_{0}^{\pi}\int_{0}^{\frac{\pi}{2}}\frac{dp}{\pi}\frac{dq}{\pi}\left(\frac{\sin{[2(i-j)q]}\left(g_{3}\sin{[2q]}\right)}{\det{\mathcal{A}}(p,q)}\right.(5.97)+cos⁡[2​(i−j)​q]​(g4+g1​cos⁡[2​q]+g5​cos⁡[2​p]+g2​cos⁡[2​(p+q)])det𝒜​(p,q)).\displaystyle\left.+\frac{\cos{[2(i-j)q]}\left(g_{4}+g_{1}\cos{[2q]}+g_{5}\cos{[2p]}+g_{2}\cos{[2(p+q)]}\right)}{\det{\mathcal{A}}(p,q)}\right).

Heredet𝒜​(p,q)\det\mathcal{A}(p,q)is given in Eq. (3). The coefficientsgig_{i}are defined asg1\displaystyle g_{1}=\displaystyle=R0110R0000​R1001R0000−R0101R0000​R1010R0000,g2=R0110R0000−R1001R0000​R0101R0000​R1010R0000,\displaystyle\frac{R_{01}^{10}}{R_{00}^{00}}\frac{R_{10}^{01}}{R_{00}^{00}}-\frac{R_{01}^{01}}{R_{00}^{00}}\frac{R_{10}^{10}}{R_{00}^{00}},\quad g_{2}=\frac{R_{01}^{10}}{R_{00}^{00}}-\frac{R_{10}^{01}}{R_{00}^{00}}\frac{R_{01}^{01}}{R_{00}^{00}}\frac{R_{10}^{10}}{R_{00}^{00}},(5.98)g3\displaystyle g_{3}=\displaystyle=2​R0110R0000​R0011R0000,g4=[R0110R0000​R1001R0000]2−[R0101R0000]2,g5=2​R0110R0000​R1001R0000​R0101R0000.\displaystyle 2\frac{R_{01}^{10}}{R_{00}^{00}}\frac{R_{00}^{11}}{R_{00}^{00}},\quad g_{4}=\left[\frac{R_{01}^{10}}{R_{00}^{00}}\frac{R_{10}^{01}}{R_{00}^{00}}\right]^{2}-\left[\frac{R_{01}^{01}}{R_{00}^{00}}\right]^{2},\quad g_{5}=2\frac{R_{01}^{10}}{R_{00}^{00}}\frac{R_{10}^{01}}{R_{00}^{00}}\frac{R_{01}^{01}}{R_{00}^{00}}.

These expressions simplify in homogeneous cases, such asJ1=±J2=±J3J_{1}=\pm J_{2}=\pm J_{3},
and in the square-lattice limit, whenJk=0J_{k}=0for one of the indexes=1,2,3=1,2,3. In these cases, the even-even and
odd-odd elements vanish in the thermodynamic limit. In particular, forJk≡JJ_{k}\equiv J,k=1,2,3k=1,2,3, we obtain𝒢(2​i,2​j)=∫0π∫0π2d​pπ​d​qπ​128​(sin⁡[2​(i−j)​q]​sin⁡q​sin⁡[2​p+q]​e2​J​cosh⁡[2​J]​(sinh⁡2​J)2)(𝒜1+𝒜​(J,J,J)​(cos⁡2​p)+cos⁡2​q+cos⁡[2​p+2​q]).\displaystyle\mathcal{G}_{(2i,2j)}=\int_{0}^{\pi}\int_{0}^{\frac{\pi}{2}}\frac{dp}{\pi}\frac{dq}{\pi}\frac{128\left(\sin{[2(i-j)q]}\sin{q}\sin{[2p+q]}e^{2J}\cosh{[2J]}(\sinh{2J})^{2}\right)}{\left(\mathcal{A}_{1}+\mathcal{A}(J,J,J)(\cos{2p})+\cos{2q}+\cos{[2p+2q]}\right)}.(5.99)

After integration overpp, this contribution vanishes. Therefore, only the
odd-even (even-odd) elements remain, forming the matrix𝒢(i,j)′=[𝒢(2​i,2​j+1)+δi​j]\mathcal{G}^{\prime}_{(i,j)}=[\mathcal{G}_{(2i,2j+1)}+\delta_{ij}], whose determinant
gives the magnetization[28]. These elements can be written as𝒢(2​i,2​j+1)=∫0π∫0π2d​pπ​d​qπ​64(1+e4​J)sinh[2J]2cos[q]cos[2(i−j)q]cos[2p+q](𝒜1+𝒜​(J,J,J)​(cos⁡2​p)+cos⁡2​q+cos⁡[2​p+2​q])\displaystyle\mathcal{G}_{(2i,2j+1)}=\int_{0}^{\pi}\int_{0}^{\frac{\pi}{2}}\frac{dp}{\pi}\frac{dq}{\pi}\frac{64(1+e^{4J})\sinh{[2J]}^{2}\cos{[q]}\cos{[2(i-j)q]}\cos{[2p+q]}}{\left(\mathcal{A}_{1}+\mathcal{A}(J,J,J)(\cos{2p})+\cos{2q}+\cos{[2p+2q]}\right)}+\displaystyle+∫0π∫0π2d​pπ​d​qπ​64e4​Jsinh[2J]3cosq(cos[2(i−j)q+q]e−2​J+cosh2Jcos[2(i−j)q−q])(𝒜1+𝒜​(J,J,J)​(cos⁡2​p)+cos⁡2​q+cos⁡[2​p+2​q]).\displaystyle\int_{0}^{\pi}\int_{0}^{\frac{\pi}{2}}\frac{dp}{\pi}\frac{dq}{\pi}\frac{64e^{4J}\sinh{[2J]}^{3}\cos{q}\left(\cos{[2(i-j)q+q]}e^{-2J}+\cosh{2J}\cos{[2(i-j)q-q]}\right)}{\left(\mathcal{A}_{1}+\mathcal{A}(J,J,J)(\cos{2p})+\cos{2q}+\cos{[2p+2q]}\right)}.

Integration over the variableppbrings to the following result𝒢(2​i,2​j+1)=−δi​j+∫0π2𝑑q​2A1−32(1+e4​J)sinh[2J]2cos[2q]cos[2(i−j)q]π​((𝒜1+𝒜​(J,J,J)​cos⁡2​p)2−4​A​(J,J,J)2​cos⁡q2)\displaystyle\mathcal{G}_{(2i,2j+1)}=-\delta_{ij}+\int_{0}^{\frac{\pi}{2}}dq\frac{2A_{1}-32(1+e^{4J})\sinh{[2J]}^{2}\cos{[2q]}\cos{[2(i-j)q]}}{\pi\left(\sqrt{(\mathcal{A}_{1}+\mathcal{A}(J,J,J)\cos{2p})^{2}-4A(J,J,J)^{2}\cos{q}^{2}}\right)}(5.101)+∫0π2𝑑p​64e4​Jsinh[2J]3cosq(cos[2(i−j)q+q]e−2​J+cosh2Jcos[2(i−j)q−q])π​((𝒜1+𝒜​(J,J,J)​cos⁡2​p)2−4​A​(J,J,J)2​cos⁡q2)\displaystyle+\int_{0}^{\frac{\pi}{2}}dp\frac{64e^{4J}\sinh{[2J]}^{3}\cos{q}\left(\cos{[2(i-j)q+q]}e^{-2J}+\cosh{2J}\cos{[2(i-j)q-q]}\right)}{\pi\left(\sqrt{(\mathcal{A}_{1}+\mathcal{A}(J,J,J)\cos{2p})^{2}-4A(J,J,J)^{2}\cos{q}^{2}}\right)}

which can be written in a more compact form, see below.

The structure of the matrix𝒢′i​j≡𝒢(i−j)′\mathcal{G^{\prime}}_{ij}\equiv\mathcal{G}^{\prime}_{(i-j)}reflects the fermionic nature of
the problem. In the thermodynamic limit, many matrix elements vanish, and the
problem reduces to a Toeplitz determinant. This reduction is essential for
obtaining exact results for the spontaneous magnetization. The remaining nonzero elements
encode the long-range correlations of the system. The dependence on momentum
variables(p,q)(p,q)shows that the correlations are built from collective modes,
and the behavior near the critical point is governed by low-momentum
(fluctuation) contributions.

## 5.1Spontaneous magnetization for more general symmetric eight-vertex free field case

The above integral representation can be extended to a general class of
free-fermion models with an eight-vertexRR-matrix structure. In such models,
the partition function (or free energy) has the same dependence on the momentum
variables as in Eq. (4).

For symmetricRRand𝒜\mathcal{A}matrices, satisfying[R0011]2=[R0101]2[R^{11}_{00}]^{2}=[R_{01}^{01}]^{2}, the determinant of the action matrix takes a
simplified form, corresponding to the condition𝒜2=𝒜3=𝒜4\mathcal{A}_{2}=\mathcal{A}_{3}=\mathcal{A}_{4}. This occurs when the following
relation holds:([R1001R0000]2−R0101R0000)​(R0101R0000+1)=0.\displaystyle\left(\left[\frac{R_{10}^{01}}{R_{00}^{00}}\right]^{2}-\frac{R_{01}^{01}}{R_{00}^{00}}\right)\left(\frac{R_{01}^{01}}{R_{00}^{00}}+1\right)=0.(5.102)

For the homogeneous kagomé model,Jk≡JJ_{k}\equiv J,k=1,2,3k=1,2,3, the first factor
in Eq. (5.102) vanishes identically. In this case, the dependence on the spin
coupling is fully determined by the single parametercJ=R0101R0000=sinh2⁡(2​J)(sinh⁡2​J−2​cosh⁡2​J)2.\displaystyle c_{J}=\frac{R_{01}^{01}}{R_{00}^{00}}=\frac{\sinh^{2}(2J)}{(\sinh{2J}-2\cosh{2J})^{2}}.(5.103)

The integrals over the momentum variableppcan then be evaluated explicitly,
leading to𝒢(2​i,2​j)=8​∫πd​pπ​∫π/2d​qπ​cJ​(cJ−1)​cos⁡[q]​sin⁡[2​(i−j)​q]​sin⁡[2​p+q]det[𝒜​(p,q)]J=0,\displaystyle\mathcal{G}_{(2i,2j)}=8\int^{\pi}\frac{dp}{\pi}\int^{\pi/2}\frac{dq}{\pi}\frac{c_{J}(c_{J}-1)\cos[q]\sin[2(i-j)q]\sin[2p+q]}{\det{[\mathcal{A}(p,q)]_{J}}}=0,\qquad\qquad(5.104)𝒢(2​i+1,2​j)=−∫πd​pπ​∫π/2d​qπ​8​cJ​bJ​sin⁡[2​q]​sin⁡[2​(i−j)​q]det[𝒜​(p,q)]J\displaystyle\mathcal{G}_{(2i+1,2j)}=-\int^{\pi}\frac{dp}{\pi}\int^{\pi/2}\frac{dq}{\pi}\frac{8c_{J}b_{J}\sin[2q]\sin[2(i-j)q]}{\det[\mathcal{A}(p,q)]_{J}}\qquad\qquad\qquad\qquad\qquad−∫πd​pπ​∫π/2d​qπ​8​cJ​cos⁡[q]​cos⁡[2​(i−j)​q]​(2​cJ​cos⁡[q]+[cJ−1])​cos⁡(2​p+q)det[𝒜​(p,q)]J\displaystyle-\int^{\pi}\frac{dp}{\pi}\int^{\pi/2}\frac{dq}{\pi}\frac{8c_{J}\cos[q]\cos[2(i-j)q](2c_{J}\cos[q]+[c_{J}-1])\cos(2p+q)}{\det[\mathcal{A}(p,q)]_{J}}\qquad\quad=−2​∫π/2d​qπ​cos⁡[2​(i−j)​q]−∫πd​pπ​∫π/2d​qπ​8​cJ​bJ​sin⁡[2​q]​sin⁡[2​(i−j)​q]det[𝒜​(p,q)]J\displaystyle=-2\int^{\pi/2}\frac{dq}{\pi}\cos[2(i-j)q]-\int^{\pi}\frac{dp}{\pi}\int^{\pi/2}\frac{dq}{\pi}\frac{8c_{J}b_{J}\sin[2q]\sin[2(i-j)q]}{\det[\mathcal{A}(p,q)]_{J}}\qquad\qquad(5.105)−2​∫πd​pπ​∫π/2d​qπ​(cJ2−1+2​cJ​(cJ+1)​cos⁡[2​q])​cos⁡[2​(i−j)​q]det[𝒜​(p,q)]J\displaystyle-2\int^{\pi}\frac{dp}{\pi}\int^{\pi/2}\frac{dq}{\pi}\frac{(c_{J}^{2}-1+2c_{J}(c_{J}+1)\cos[2q])\cos[2(i-j)q]}{\det{[\mathcal{A}(p,q)]_{J}}}\qquad\qquad\qquad\qquad=−δi​j+12​∫0πd​qπ​ei​n​q​fJ​(q)+e−i​n​q​f¯J​(q)gJ​(q)=−δi​j+∫−ππd​q2​π​ei​n​q​fJ​(q)gJ​(q)\displaystyle=-\delta_{ij}+\frac{1}{2}\int_{0}^{\pi}\frac{dq}{\pi}\frac{e^{inq}f_{J}(q)+e^{-inq}\bar{f}_{J}(q)}{\sqrt{g_{J}(q)}}=-\delta_{ij}+\int_{-\pi}^{\pi}\frac{dq}{2\pi}\frac{e^{inq}f_{J}(q)}{\sqrt{g_{J}(q)}}\qquad\qquad\quad

wheren=[i−j]n=[i-j]fJ​(q)\displaystyle f_{J}(q)=\displaystyle=(cJ2−1)+(−2​cJ​bJ+cJ​(cJ+1))​ei​q+(cJ​(cJ+1)+2​cJ​bJ)​e−i​q,\displaystyle(c_{J}^{2}-1)+(-2c_{J}b_{J}+c_{J}(c_{J}+1))e^{iq}+(c_{J}(c_{J}+1)+2c_{J}b_{J})e^{-iq},f¯J​(q)\displaystyle\bar{f}_{J}(q)=\displaystyle=fJ​(−q).\displaystyle f_{J}(-q).(5.106)

In (5.104) and (5.1)det[𝒜​(p,q)]J\displaystyle\det[\mathcal{A}(p,q)]_{J}=\displaystyle=1+3​cJ2+2​cJ​(cJ−1)​(cos⁡[2​p]+cos⁡[2​q]+cos⁡[2​p+2​q]),\displaystyle 1+3c_{J}^{2}+2c_{J}(c_{J}-1)(\cos[2p]+\cos[2q]+\cos[2p+2q]),\qquad(5.107)

is the determinant of (3.48) explicitly expressed in terms of the momentappandqq, while after integration over the momentappthe denominator becomes the square root of the functiongJ(q)=(1−cJ2)2+16cJ3+4cJ(cJ2−1)(cJ+1)cos[q]+4cJ2(cJ−1)2cos[q]2\displaystyle g_{J}(q)=(1-c_{J}^{2})^{2}+16c_{J}^{3}+4c_{J}(c_{J}^{2}-1)(c_{J}+1)\cos[q]+4c_{J}^{2}(c_{J}-1)^{2}\cos[q]^{2}\qquad\qquad(5.108)

One can verify that, taking into account the relationbJ2=cJb_{J}^{2}=c_{J}, the following identity holds:gj​(q)=fJ​(q)​fj​(−q)=fJ​(q)​f¯j​(q).\displaystyle g_{j}(q)=f_{J}(q)f_{j}(-q)=f_{J}(q)\bar{f}_{j}(q).(5.109)

The expression in Eq. (5.1) defines the elements of a Töplitz-type matrix through the Fourier coefficients of the function𝒢f′​(q)\mathcal{G}^{\prime}_{f}(q)introduced above,𝒢f′​(q)≡fJ​(q)gJ​(q),𝒢f′​(q)​𝒢f′​(−q)=1.\displaystyle\mathcal{G}^{\prime}_{f}(q)\equiv\frac{f_{J}(q)}{\sqrt{g_{J}(q)}},\quad\mathcal{G}^{\prime}_{f}(q)\mathcal{G}^{\prime}_{f}(-q)=1.(5.110)

Spontaneous magnetization is the thermodynamic limit (lattice sizeL→∞L\to\infty) of the determinant of the correlation functionM2=limL→∞det𝒢(i−j)′M^{2}=\lim_{L\rightarrow\infty}\det{\mathcal{G}^{\prime}_{(i-j)}}, which can be evaluated using Szegö’s theorem[34,35]. This can be done in terms of the logarithmic Fourier coefficientsknFk_{n}^{F}:ln⁡fJ​(q)gJ​(q)\displaystyle\ln{\frac{f_{J}(q)}{\sqrt{g_{J}(q)}}}=\displaystyle=∑n=1∞knF​ei​n​q,\displaystyle\sum_{n=1}^{\infty}k_{n}^{F}e^{inq},(5.111)limL→∞det𝒢(i−j)′exp⁡[12​π​∫−ππ𝑑q​ln⁡fJ​(q)gJ​(q)]\displaystyle\lim_{L\to\infty}\frac{\det{\mathcal{G}^{\prime}_{(i-j)}}}{\exp\!\left[\frac{1}{2\pi}\int_{-\pi}^{\pi}dq\ln{\frac{f_{J}(q)}{\sqrt{g_{J}(q)}}}\right]}=\displaystyle=exp⁡(∑n∞n​knF​k−nF).\displaystyle\exp{\left(\sum^{\infty}_{n}nk_{n}^{F}k_{-n}^{F}\right)}.(5.112)

The properties of the function in Eq. (5.110) imply that its logarithm is odd inqq. As a result, the integral in the denominator of Eq. (5.112) vanishes, and the denominator reduces to unity.

For the evaluation of the infinite sum, one can apply known technique used for the standard Ising model (IM)[1,34,35]. In the present case, a similar (although less explicit) decomposition appears in the following integral:∫−ππd​q2​π​ei​n​q​fJ​(q)gJ​(q)=∫−ππd​q2​π​ei​n​q​fJ​(q)fJ​(−q)=∫−ππd​q2​π​ei​n​q​(ei​q​α−1)​(e−i​q​α¯−1)(e−i​q​α−1)​(ei​q​α¯−1).\displaystyle\int_{-\pi}^{\pi}\frac{dq}{2\pi}\frac{e^{inq}f_{J}(q)}{\sqrt{g_{J}(q)}}=\int_{-\pi}^{\pi}\frac{dq}{2\pi}\frac{e^{inq}\sqrt{f_{J}(q)}}{\sqrt{f_{J}(-q)}}=\int_{-\pi}^{\pi}\frac{dq}{2\pi}\frac{e^{inq}\sqrt{(e^{iq}\alpha-1)(e^{-iq}\bar{\alpha}-1)}}{\sqrt{(e^{-iq}\alpha-1)(e^{iq}\bar{\alpha}-1)}}.(5.113)

This identity follows directly from Eqs. (5.109) and (5.110). Introduction of new variablesα\alphaandα¯\bar{\alpha}makes
the integration overqqmore convenient.

It is known[36]that in the low-temperature regime (i.e., below the critical point), whereα<1\alpha<1andα¯<1\bar{\alpha}<1, the infinite determinant of such Töplitz matrices is given by .M2=limL→∞det𝒢′n=((1−α2)​(1−α¯2)(1−α​α¯)2)1/4.\displaystyle M^{2}=\lim_{L\to\infty}\det\mathcal{G^{\prime}}_{n}=\left(\frac{(1-\alpha^{2})(1-{\bar{\alpha}}^{2})}{(1-\alpha\bar{\alpha})^{2}}\right)^{1/4}.(5.114)

In order to determine the expression forlimL→∞det𝒢′n\lim_{L\to\infty}\det\mathcal{G^{\prime}}_{n}in terms ofcJc_{J}, one must relate the parametersα\alphaandα¯\bar{\alpha}tocJc_{J}using Eqs. (5.1) and (5.108), which define the functionsfJf_{J}andgJg_{J}, respectively.Explicit expressions for these parameters are not needed. It is sufficient to compare the following expressions in Eq. (5.113):(ei​q​α−1)​(e−i​q​α¯−1)(e−i​q​α−1)​(ei​q​α¯−1)=(1−ei​q​α−e−i​q​α¯+α​α¯)(1−e−i​q​α−ei​q​α¯+α​α¯)=\displaystyle\frac{\sqrt{(e^{iq}\alpha-1)(e^{-iq}\bar{\alpha}-1)}}{\sqrt{(e^{-iq}\alpha-1)(e^{iq}\bar{\alpha}-1)}}=\frac{\sqrt{(1-e^{iq}\alpha-e^{-iq}\bar{\alpha}+\alpha\bar{\alpha})}}{\sqrt{(1-e^{-iq}\alpha-e^{iq}\bar{\alpha}+\alpha\bar{\alpha})}}=(5.115)(cJ2−1)+(cJ​(cJ+1)−2​cJ​bJ)​ei​q+(cJ​(cJ+1)+2​cJ​bJ)​e−i​q(cJ2−1)+(cJ​(cJ+1)+2​cJ​bJ)​ei​q+(cJ​(cJ+1)−2​cJ​bJ)​e−i​q.\displaystyle\frac{\sqrt{(c_{J}^{2}-1)+(c_{J}(c_{J}+1)-2c_{J}b_{J})e^{iq}+(c_{J}(c_{J}+1)+2c_{J}b_{J})e^{-iq}}}{\sqrt{(c_{J}^{2}-1)+(c_{J}(c_{J}+1)+2c_{J}b_{J})e^{iq}+(c_{J}(c_{J}+1)-2c_{J}b_{J})e^{-iq}}}.

This comparison leads to the relationsα=[−cJ​(cJ+1)+2​cJ​bJ]​β,α¯=−[cJ​(cJ+1)+2​cJ​bJ]​β,1+α​α¯=(cJ2−1)​β,\displaystyle\alpha=[-c_{J}(c_{J}+1)+2c_{J}b_{J}]\beta,\quad\bar{\alpha}=-[c_{J}(c_{J}+1)+2c_{J}b_{J}]\beta,\quad 1+\alpha\bar{\alpha}=(c_{J}^{2}-1)\beta,(5.116)

which admit the solutionα=1−cJ2+(1−cJ)3​(1+3​cJ)2​(1+cJ)2​cJ,α¯=1−cJ2+(1−cJ)3​(1+3​cJ)2​(1−cJ)2​cJ.\displaystyle\alpha=\frac{1-c_{J}^{2}+\sqrt{(1-c_{J})^{3}(1+3c_{J})}}{2(1+\sqrt{c_{J}})^{2}c_{J}},\qquad\bar{\alpha}=\frac{1-c_{J}^{2}+\sqrt{(1-c_{J})^{3}(1+3c_{J})}}{2(1-\sqrt{c_{J}})^{2}c_{J}}.(5.117)

From Eq. (5.117) one obtainsα1+α​α¯=cJ​(cJ+1)−2​cJ​bJ1−cJ2,α¯1+α​α¯=cJ​(cJ+1)+2​cJ​bJ1−cJ2,\displaystyle\frac{\alpha}{1+\alpha\bar{\alpha}}=\frac{c_{J}(c_{J}+1)-2c_{J}b_{J}}{1-c_{J}^{2}},\quad\frac{\bar{\alpha}}{1+\alpha\bar{\alpha}}=\frac{c_{J}(c_{J}+1)+2c_{J}b_{J}}{1-c_{J}^{2}},(5.118)αα¯=cJ​(cJ+1)−2​cJ​bJcJ​(cJ+1)+2​cJ​bJ,α​α¯(1+α​α¯)2=cJ2​(1−cJ)2(1−cJ2)2=cJ2(1+cJ)2,\displaystyle\frac{\alpha}{\bar{\alpha}}=\frac{c_{J}(c_{J}+1)-2c_{J}b_{J}}{c_{J}(c_{J}+1)+2c_{J}b_{J}},\qquad\frac{\alpha\bar{\alpha}}{(1+\alpha\bar{\alpha})^{2}}=\frac{c_{J}^{2}(1-c_{J})^{2}}{(1-c_{J}^{2})^{2}}=\frac{c_{J}^{2}}{(1+c_{J})^{2}},(5.119)

wherebJ=cJb_{J}=\sqrt{c_{J}}. We next expand the expression under the square root in Eq. (5.114):(1−α2)​(1−α¯2)(1−α​α¯)2=1−α2−α¯2+(α​α¯)21−2​α​α¯+(α​α¯)2=α​α¯−αα¯−α¯α+1α​α¯α​α¯−2+1α​α¯.\displaystyle\frac{(1-\alpha^{2})(1-{\bar{\alpha}}^{2})}{(1-\alpha\bar{\alpha})^{2}}=\frac{1-\alpha^{2}-{\bar{\alpha}}^{2}+(\alpha\bar{\alpha})^{2}}{1-2\alpha\bar{\alpha}+(\alpha\bar{\alpha})^{2}}=\frac{\alpha\bar{\alpha}-\frac{\alpha}{\bar{\alpha}}-\frac{\bar{\alpha}}{\alpha}+\frac{1}{\alpha\bar{\alpha}}}{\alpha\bar{\alpha}-2+\frac{1}{\alpha\bar{\alpha}}}.(5.120)

It is therefore sufficient to evaluate the following two combinations using Eq. (5.118):αα¯+α¯α=2​(cJ+1)2+8​cJ(cJ−1)2,α​α¯+1α​α¯=(1+α​α¯)2α​α¯−2=1−cJ2+2​cJcJ2.\displaystyle\frac{\alpha}{\bar{\alpha}}+\frac{\bar{\alpha}}{\alpha}=\frac{2(c_{J}+1)^{2}+8c_{J}}{(c_{J}-1)^{2}},\qquad\alpha\bar{\alpha}+\frac{1}{\alpha\bar{\alpha}}=\frac{(1+\alpha\bar{\alpha})^{2}}{\alpha\bar{\alpha}}-2=\frac{1-c_{J}^{2}+2c_{J}}{c_{J}^{2}}.(5.121)

Substituting these results yields the expression for the square of the magnetization in the infinite-lattice limit.M2=((1−α2)​(1−α¯2)(1−α​α¯)2)1/4=[(1+cJ)3​(1−3​cJ)(1−cJ)3​(1+3​cJ)]1/4.\displaystyle M^{2}=\left(\frac{(1-\alpha^{2})(1-{\bar{\alpha}}^{2})}{(1-\alpha\bar{\alpha})^{2}}\right)^{1/4}=\left[\frac{(1+c_{J})^{3}(1-3c_{J})}{(1-c_{J})^{3}(1+3c_{J})}\right]^{1/4}.(5.122)

The critical point is determined by the conditionM=0M=0, which yields3​cJ=13c_{J}=1. Using the expression forcJc_{J}in Eq. (5.103) one can see that this condition coincides with Eq. (4.59).
SubstitutingcJc_{J}into Eq. (5.122), we obtain the following expression for the spontaneous magnetization:M=[(3+6​e4​J−e8​J)​(5+2​e4​J+e8​J)3128​(3+e8​J)​(1+e4​J)3]1/8.\displaystyle M=\left[\frac{(3+6e^{4J}-e^{8J})(5+2e^{4J}+e^{8J})^{3}}{128(3+e^{8J})(1+e^{4J})^{3}}\right]^{1/8}.(5.123)

Obtained expressions (5.122) and (5.123) for the spontaneous magnetization slightly differ from that expressions obtained in papers[33,21], however the positions of the critical points
coincides and arecJ=1/3c_{J}=1/3. The expressions are differ by somecJc_{J}dependent
factors, which are not critical: do not have zeros.

Physics discussion.The reduction to a Toeplitz matrix is a key step that allows an exact evaluation
of the spontaneous magnetization. In the homogeneous case, the problem simplifies
significantly and depends only on a single effective coupling parametercJc_{J}.
The vanishing of the even-even correlations shows that only mixed (odd-even)
correlations contribute to long-range order. The Fourier representation makes
clear that the correlations are built from momentum modes, and the critical
behavior is controlled by the low-momentum region, where the denominatordet[𝒜​(p,q)]\det[\mathcal{A}(p,q)]becomes small. This is the same mechanism that leads to
criticality in other exactly solvable two-dimensional models.

## 6Summary

We have presented a solution of the two-dimensional Ising model (2DIM) on the kagomé lattice using a fermionic representation of itsRR-matrix, following the technique developed in Refs.[30,28,29].
The fermionic representation provides a convenient and systematic way to analyze the model, as it maps the spin degrees of freedom onto fermionic variables with well-defined algebraic properties. This approach is especially useful for treating anisotropy, where the couplings depend on direction and lead to a nontrivial critical surface. The resulting phase transition is governed by the interplay between these couplings, and the exact determination of the free energy allows one to extract thermodynamic quantities such as the heat capacity and spontaneous magnetization. These quantities characterize the onset of long-range order and the singular behavior near criticality.

We have determined the surface of critical couplings associated with the phase transition. We have also calculated the free energy, specific heat capacity, and spontaneous magnetization of the model.

The limiting casesJ1=0J_{1}=0andJ1=J2=0J_{1}=J_{2}=0provide direct consistency checks of the exact solution. When one coupling vanishes, the kagom’e model reduces to an anisotropic square-lattice Ising model with renormalized couplingse2​J¯a=cosh⁡(2​Ja).e^{2\bar{J}_{a}}=\cosh(2J_{a}).When two couplings vanish, the system further reduces to independent one-dimensional Ising chains. The square-lattice critical condition is reproduced exactly, whereas in the one-dimensional limit the transition occurs only atT=0T=0. Thus, both reductions confirm the correctness of the obtained partition function and free energy.

## Acknowledgment

A.S. acknowledges the Institute of Metal Research for hospitality, where this work was initiated. The work of Sh. Kh. and A.S. were also supported by the HESC grants 21AG-1C024 and 24FP-1F039. The work of Z.Z was supported by the National Natural Science Foundation
of China under grant 52031014.

## References
- [1]L. Onsager,Crystal statistics. I. A two-dimensional model with an order-disorder transition, Phys. Rev. 65 (3–4) (1944) 117–149, http://dx.doi.org/10.1103/PhysRev.65.117
- [2]B. Kaufman,Crystal statistics. II. Partition function evaluated by spinor analysis, Phys. Rev. 76 (8) (1949) 1232–1243, http://dx.doi.org/10.1103/PhysRev.76. 1232.
- [3]R.J. Baxter,Exactly Solved Models
in Statistical Mechanics, Academic Press 1982.
- [4]Faddeev, L. D. and Takhtajan, L. A.-Hamiltonian Methods in the Theory of Solitons, Series- Classics in Mathematics, Springer, 2007
- [5]H. A. Kramers and G. H. Wannier,Statistics of the two-dimensional ferromagnet. Part I, Phys. Rev.60, 252–262 (1941), https://doi.org/10.1103/PhysRev.60.252.
- [6]R. M. F. Houtappel,Order-disorder in hexagonal lattices, Physica16, 425–455 (1950), https://doi.org/10.1016/0031-8914(50)90130-3.
- [7]G. H. Wannier,Antiferromagnetism. The triangular Ising net, Phys. Rev.79, 357–364 (1950), https://doi.org/10.1103/PhysRev.79.357.
- [8]T. D. Schultz, D. C. Mattis and E. H. Lieb,Two-dimensional Ising model as a soluble problem of many fermions, Rev. Mod. Phys.36, 856–871 (1964), https://doi.org/10.1103/RevModPhys.36.856.
- [9]P. W. Kasteleyn,Dimer statistics and phase transitions, J. Math. Phys.4, 287–293 (1963), https://doi.org/10.1063/1.1703953.
- [10]M. E. Fisher,On the dimer solution of planar Ising models, J. Math. Phys.7, 1776–1781 (1966), https://doi.org/10.1063/1.1704825.
- [11]C. Fan and F. Y. Wu,General lattice model of phase transitions, Phys. Rev. B2, 723–733 (1970), https://doi.org/10.1103/PhysRevB.2.723.
- [12]R. J. Baxter,Partition function of the eight-vertex lattice model, Ann. Phys.70, 193–228 (1972), https://doi.org/10.1016/0003-4916(72)90335-1.
- [13]L. P. Kadanoff and H. Ceva,Determination of an operator algebra for the two-dimensional Ising model, Phys. Rev. B3, 3918–3939 (1971), https://doi.org/10.1103/PhysRevB.3.3918.
- [14]R. J. Baxter,Eight-vertex model in lattice statistics and one-dimensional anisotropic Heisenberg chain. I. Some fundamental eigenvectors, Ann. Phys.76, 1–24 (1973), https://doi.org/10.1016/0003-4916(73)90439-9.
- [15]R. J. Baxter,Eight-vertex model in lattice statistics and one-dimensional anisotropic Heisenberg chain. II. Equivalence to a generalized ice-type lattice model, Ann. Phys.76, 25–47 (1973), https://doi.org/10.1016/0003-4916(73)90440-5.
- [16]P. Melotti,The free-fermion eight-vertex model: couplings, bipartite dimers and Z-invariance, Commun. Math. Phys.381, 33–82 (2021), https://doi.org/10.1007/s00220-020-03901-2.
- [17]D.-Z. Li, X. Wang and X.-B. Yang,Free-fermion models and two-dimensional Ising models under zero field and imaginary fieldi​(π/2)​kB​Ti(\pi/2)k_{B}T, Entropy27, 799 (2025), https://doi.org/10.3390/e27080799.
- [18]Kenzi Kanô, Shigeo Naya,Antiferromagnetism. The Kagomé Ising Net, Progress of Theoretical Physics Vol.10, No. 2 (1953) 158.
- [19]I. Syozi, H. Nakano,Statistical models of ferrimagnetism, Progr. Theoret. Phys. 13 (1) (1955) 69–78, http://dx.doi.org/10.1143/PTP.13.69.
- [20]I. Syozi, S. Naya,Symmetrical properties of two-dimensional Ising lattices, Progr. Theoret. Phys. 24 (4) (1960) 829–839, http://dx.doi.org/10.1143/PTP.24.829.
- [21]V. Matveev, R. Shrock,Complex-temperature properties of the Ising
model on 2D heteropolygonal lattices, J. Phys. A: Math. Gen.285235 (1995).
- [22]F.A.Kassan-Ogly, Spontaneous magnetization of Kagome lattice in Ising model, Journal of Magnetism and Magnetic Materials, 572, 170568 (2023).
- [23]J. Zheng and G. Sun,Exact results for Ising models on the triangular Kagomé lattice, Phys. Rev. B71, 052408 (2005), https://doi.org/10.1103/PhysRevB.71.052408.
- [24]E. Jurčišinová and M. Jurčišin,Interaction-generated frustration in the ferromagnetic spin system on the kagome lattice: exact analysis on the star kagomelike recursive lattice, Phys. Rev. E104, 044121 (2021), https://doi.org/10.1103/PhysRevE.104.044121.
- [25]P. Narasimhan, S. Humeniuk, A. Roy and V. Drouin-Touchette,Simulating the transverse-field Ising model on the kagome lattice using a programmable quantum annealer, Phys. Rev. B110, 054432 (2024), https://doi.org/10.1103/PhysRevB.110.054432.
- [26]V. A. Mutailamov and A. K. Murtazaev,Phase diagram of the decorated Ising model on the Kagome lattice with ferromagnetic nearest-neighbor and antiferromagnetic next-nearest-neighbor interactions, Physica A678, 130953 (2025), https://doi.org/10.1016/j.physa.2025.130953.
- [27]Di Sante, Domenico, Neupert, Titus, etal. and Wilson, Stephen D.Kagome metals-Rev.Mod.Phys.98.015002 (2026).
- [28]Sh. Khachatryan, A. Sedrakyan,Characteristics of 2D lattice from fermionc realization: Ising and XYZ models, Phys. Rev. B80, 125128 (2009), https://doi.org/10.1103/Phys.Rev.B.80.125128, arXiv:0712.0273v2.
- [29]Sh. Khachatryan, A. SedrakyanOn the solutions of the Yang-Baxter equations with general inhomogeneous eight-vertex -matrix: Relations with Zamolodchikov’s tetrahedral algebra, J. Stat. Phys.150, 130 (2013), http:/doi.org/10.48550/arXiv:1208.4339.
- [30]A. Sedrakyan,Edge excitations of an incompressible
fermionic liquid in a staggered magnetic field, Nuclear PhysicsB554 [FS] 514-536 (1999).
- [31]Sh. Khachatryan, R. Schrader, A. Sedrakyan,Grassmann-Gaussian integrals and generalized star products: J. Phys. A: Math. Theor.42(2009) 304019;in Liouville Gravity and Statistical Models, A special issue dedicated to the memory of Alexey Zamolodchikov.
- [32]Sh. Khachatryan, A. Sedrakyan, P.Sorba,Network Models: Action formulation, Nucl.Phys.B825: 444-465 (2010).
- [33]S. Naya,On the spontaneous magnetizations of honeycomb and Kagomé Ising
lattices, Progr. Theoret. Phys. 11 (1) (1954) 53–62, http://dx.doi.org/10.1143/
PTP.11.53.
- [34]E. W. Montroll and R. B. Potts and J. C. Ward,Correlations and spontaneous magnetization of the two-dimenional Ising Model, Journal
of Math. Physics4, N.2, (1963) 308-322,
- [35]M. Kac ad J. C. Ward, Phys. Rev. 88, 1332 (1952).
- [36]C. N. Yang, Phys. Rev.85, 808 (1952).

## 


- 


Major funding support from
