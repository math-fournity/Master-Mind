# Structured High-Angular-Momentum Coulomb Tensors from Real and Complex Solid-Harmonic Integral Engines: A Perspective

**arXiv ID**: 2607.25245v1
**Authors**: Bo Peng
**Published**: 2026-07-28
**Categories**: physics.chem-ph, quant-ph
**HTML URL**: https://arxiv.org/html/2607.25245v1

## Abstract

Electron-repulsion integrals describe the Coulomb interaction between charge distributions built from orbital basis functions. Most integral algorithms generate these quantities through Cartesian Gaussian functions, whose angular shapes are written as powers of $x$, $y$, and $z$, and then transform the result to spherical functions. This route is effective, but from $d$ shells onward the Cartesian representation contains more functions than the spherical space required by the calculation. Direct real or complex solid-harmonic engines work in that target space from the beginning. They therefore produce a smaller final Coulomb tensor while preserving the ordering, phase, and magnetic-quantum-number labels that describe its angular structure. Following this structure beyond integral evaluation reveals direct connections to the algorithms that use the tensor. Simple analytical counts quantify tensor size, angular blocks, radial Slater--Condon parameters, and pair-space work. These quantities guide low-rank factorization, local Hamiltonian construction, quantum simulation, and transformations to spinor or effective-model bases. In this way, solid-harmonic integral engines provide a direct bridge between efficient integral generation and structured many-electron computation.

## Full Text

Structured High-Angular-Momentum Coulomb Tensors from Real and Complex Solid-Harmonic Integral Engines: A Perspective

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
- License: CC BY 4.0arXiv:2607.25245v1 [physics.chem-ph] 28 Jul 2026

## Structured High-Angular-Momentum Coulomb Tensors from Real and Complex Solid-Harmonic Integral Engines: A PerspectiveBo Pengpeng398@pnnl.govIntegrated Discovery Sciences Directorate, Pacific Northwest National Laboratory, Richland, WA 99354 USA

## Abstract

Electron-repulsion integrals describe the Coulomb interaction between charge distributions built from orbital basis functions. Most integral algorithms generate these quantities through Cartesian Gaussian functions, whose angular shapes are written as powers ofxx,yy, andzz, and then transform the result to spherical functions. This route is effective, but fromddshells onward the Cartesian representation contains more functions than the spherical space required by the calculation. Direct real or complex solid-harmonic engines work in that target space from the beginning. They therefore produce a smaller final Coulomb tensor while preserving the ordering, phase, and magnetic-quantum-number labels that describe its angular structure. Following this structure beyond integral evaluation reveals direct connections to the algorithms that use the tensor. Simple analytical counts quantify tensor size, angular blocks, radial Slater–Condon parameters, and pair-space work. These quantities guide low-rank factorization, local Hamiltonian construction, quantum simulation, and transformations to spinor or effective-model bases. In this way, solid-harmonic integral engines provide a direct bridge between efficient integral generation and structured many-electron computation.solid harmonics, high angular momentum, electron repulsion integrals, Cholesky decomposition, Slater-Condon parameters, relativistic Hamiltonians, quantum simulation

## IIntroductionFigure 1:Seven decades of ERI design, from tractability to representation awareness. Successive methods redistributed numerical work, reusable quantities, angular handling, and hardware constraints across integral evaluation. These method families now coexist, while the direct solid-harmonic route makes angular representation explicit for downstream tensor algorithms.

Electronic-structure theory tries to predict how electrons behave in atoms, molecules, and materials. One of its central physical ingredients is Coulomb repulsion. Two electrons repel one another more strongly when they are close together, and in atomic units this interaction has the form1/r121/r_{12}. The symbolr12r_{12}is simply the distance between electron 1 and electron 2. The physical expression is compact, but evaluating it accurately and repeatedly in a molecular calculation is a major computational task.

To make that task manageable, an electronic orbital is expanded in a finite set of basis functions. A basis function is a mathematical building block that describes part of the spatial shape of an orbital. Gaussian basis functions are widely used because products of Gaussians on different atoms can be rewritten as a new Gaussian centered between them.[8]This Gaussian product property converts difficult molecular integrals into quantities that can be built from simpler intermediates. Each Gaussian basis function also has an angular part. That angular part determines whether the function has anss,pp,dd,ff, or higher-angular-momentum shape around its center.

The electron-repulsion integral, abbreviated ERI, is the central quantity. An ERI measures the Coulomb interaction between two charge distributions. Each charge distribution is formed by multiplying two basis functions at the same electron coordinate. Because there are two basis functions for electron 1 and two for electron 2, an ERI carries four basis-function labels. In generalized chemists’ notation, it is[8,72,59,52,25,75](μ​ν|λ​σ)=∫∫χμ∗​(𝐫1)​χν​(𝐫1)​χλ∗​(𝐫2)​χσ​(𝐫2)r12​𝑑𝐫1​𝑑𝐫2.(\mu\nu|\lambda\sigma)=\int\!\!\int\frac{\chi_{\mu}^{*}(\mathbf{r}_{1})\chi_{\nu}(\mathbf{r}_{1})\chi_{\lambda}^{*}(\mathbf{r}_{2})\chi_{\sigma}(\mathbf{r}_{2})}{r_{12}}d\mathbf{r}_{1}d\mathbf{r}_{2}.(1)

Hereχμ\chi_{\mu},χν\chi_{\nu},χλ\chi_{\lambda}, andχσ\chi_{\sigma}are basis functions. The variables𝐫1\mathbf{r}_{1}and𝐫2\mathbf{r}_{2}are the electron positions. The star denotes complex conjugation. It has no effect when the basis functions are real, which is the usual situation for nonrelativistic real-spherical calculations. If the basis containsNNfunctions, the full dense ERI array has a formal size proportional toN4N^{4}because each of its four labels can takeNNvalues.

Integral algorithms often group the labels inEq.1as two charge distributions. Later applications, especially second-quantized Hamiltonians and transformations to complex orbitals, instead group them as the initial and final states of two electrons. The corresponding two-particle matrix element is therefore defined asVμ​ν;λ​σ≡⟨μ​ν|r12−1|λ​σ⟩=(μ​λ|ν​σ).V_{\mu\nu;\lambda\sigma}\equiv\langle\mu\nu|r_{12}^{-1}|\lambda\sigma\rangle=(\mu\lambda|\nu\sigma).(2)

The first two labels ofVVidentify the two functions on the bra side, which describes the final two-electron state. The last two labels identify the ket side, which describes the initial state. The equality to(μ​λ|ν​σ)(\mu\lambda|\nu\sigma)shows exactly how this bra-ket order is related to chemists’ notation. This mapping will later keep the magnetic-quantum-number rule, the second-quantized Hamiltonian, and the spinor transformation consistent.

The word “quartet” describes another common grouping. A basis-function quartet is one choice of four functions, such as(μ​ν|λ​σ)(\mu\nu|\lambda\sigma). A shell quartet is a collection of many such integrals. A shell contains basis functions on the same atomic center with the same angular momentum. For example, a real sphericalddshell contains five angular functions. A shell quartet contains every ERI formed by choosing one function from each of four shells. Integral engines work with shell quartets because many intermediate quantities can then be reused.[52,54,25,75]

The history of ERI algorithms is largely the history of making these shell quartets affordable. Gaussian product formulas first made molecular integrals tractable.[8,72,67,68,32,31]Quadrature methods later rewrote an ERI as a weighted sum over numerical roots.[17,44,65]Cartesian recurrence methods built high-angular-momentum integrals step by step from simpler starting values.[52,54]Contraction-aware algorithms then optimized when intermediate quantities should be transformed, combined, and reused.[30,23,24,25]Direct solid-harmonic methods asked whether pure spherical angular structure could enter the calculation earlier.[14,15,16,21,36,37,38,39]More recent libraries and accelerator implementations have emphasized broad integral coverage, vectorization, and memory movement.[75,78,86,60,85,2,48]Figure1summarizes this cumulative development, in which different methods move different parts of the work.

Across this history, angular representation determines the mathematical language used to describe the shape of a basis function. Cartesian Gaussian functions use powers ofxx,yy, andzz. For example, the six Cartesianddfunctions can be associated withx2x^{2},y2y^{2},z2z^{2},x​yxy,x​zxz, andy​zyz. This language is convenient because the three coordinate directions can be handled separately. Spherical functions instead describe pure angular momentum.[19,14,16,21]Real spherical functions are often convenient in nonrelativistic molecular calculations because the orbitals and integrals can remain real. Complex spherical functions carry an explicit magnetic quantum numbermm. They are therefore natural for atomic multiplets, spin-orbit coupling, and time-reversal-related spinor partners, which are often called Kramers pairs.[66,63]

Cartesian and sphericalssshells both contain one function, and both forms of appshell contain three. Their dimensions first differ forddfunctions. A Cartesianddshell has six functions, while a pure sphericalddshell has five, and the difference grows with angular momentum. As a result, a conventional Cartesian-to-spherical route may build, store, screen, or transform a larger intermediate tensor before projecting it to the smaller spherical target.[14,16,21,36,37,38,39]Mature Cartesian implementations can still be highly efficient, yet the angular labels needed later may appear only after the calculation has passed through the larger representation.

That delay matters because ERIs are rarely the final scientific result. Density fitting, resolution of the identity, Cholesky decomposition, tensor hypercontraction, compound decomposition, double factorization, and related methods all reorganize or compress the same Coulomb information.[84,13,79,82,5,45,34,56,57,53,6,47]Quantum-simulation algorithms use the ERIs to build a fermionic Hamiltonian and then map that Hamiltonian to qubits.[10,51,4,3,77,80]Relativistic and heavy-element calculations often transform the Coulomb tensor to complex orbitals or spinors.[20,12,33,18,46,35,50,66,63]Each application needs not only accurate values, but also a clear statement of the tensor order, normalization, and phases.

High-angular-momentum shells make this interface problem especially visible. Here “high angular momentum” means shells beyondpp. Addshell hasl=2l=2, anffshell hasl=3l=3, aggshell hasl=4l=4, and anhhshell hasl=5l=5. Accurate basis sets and heavy-element calculations often include these functions.[76,28]A direct real or complex solid-harmonic engine can produce their Coulomb tensors in the compact spherical space and attach the angular labels at the same time. The important question is therefore not only whether the engine evaluates integrals quickly. It is also whether it delivers those integrals in a form that downstream algorithms can use without rebuilding their angular meaning.

A representation-aware interface connects integral generation to later tensor algorithms. A solid-harmonic engine can expose convention-controlled spherical shell-pair objects and complex-mmblocks, whose analytical structure can then guide low-rank methods, local Hamiltonians, quantum simulation, and spinor transformations. Exact total-MMblocks and the compact Slater–Condon form provide one-center reference limits. Molecular benchmarks measure how strongly realistic environments depart from those limits.Figure2summarizes the resulting data path.

Understanding this interface begins by separating Cartesian, real-spherical, and complex-spherical representations. Their dimensions and angular labels lead to exact counts for tensor size, angular blocks, local parameters, and pair-space work. Those counts then connect integral generation to low-rank preprocessing, local and quantum Hamiltonians, and relativistic or downfolded models. A common benchmark program can test whether the predicted structure survives in molecules and through downstream transformations.

The broader opportunity is to make angular representation a persistent part of the computational workflow. Integral libraries and downstream tensor methods could then exchange not only numerical values, but also the angular information needed to interpret and reorganize them. Establishing that connection across molecular, relativistic, and quantum-simulation benchmarks would turn solid-harmonic integral generation into the starting point for a new class of representation-aware many-electron algorithms.Figure 2:Two routes to the same spherical Coulomb tensor. The difference is when redundant Cartesian angular structure is removed. The conventional route projects to the real-spherical basis after integral formation, whereas the direct route works in the target shell dimension from the start. A phase- and ordering-controlled real-to-complex transformation then exposes|l,m⟩|l,m\ranglepair blocks for low-rank, local-Hamiltonian, and spinor or downfolding applications.

## IIWhy Starting in a Spherical Basis Changes the Tensor

The first change is simply the number of functions used to describe one angular-momentum shell. A Cartesian Gaussian shell with angular momentumllcontains[59,52,16]Cl=(l+1)​(l+2)2C_{l}=\frac{(l+1)(l+2)}{2}(3)

functions. The symbolClC_{l}counts products ofxx,yy, andzzwhose powers add toll. For addshell, examples includex2x^{2},x​yxy, andz2z^{2}. A pure spherical shell instead containsSl=2​l+1S_{l}=2l+1(4)

functions. HereSlS_{l}counts one function for each magnetic labelm=−l,…,lm=-l,\ldots,l. The two counts agree forssandppshells, so the choice of representation does not change their size. Fromddshells onward, the Cartesian description contains extra functions. Addshell has66Cartesian functions but only55spherical functions. The corresponding counts forff,gg, andhhshells are1010versus77,1515versus99, and2121versus1111.

An ERI shell quartet has four slots, one for each basis function in the integral. Therefore, the size difference for one shell is raised to the fourth power for an equal-shell quartet such as(l​l|l​l)(ll|ll). This fourth-power count isolates the contribution from representation size. Actual runtime also depends on screening small integrals, combining primitive Gaussians into contracted functions, arranging operations for the processor, and moving data through memory. A direct spherical calculation nevertheless avoids forming the extra Cartesian entries.

The term “solid harmonic” refers to a polynomial with a definite angular momentum. Multiplying this angular polynomial by a Gaussian factor that controls the radial decay gives a solid-harmonic Gaussian basis function. A direct solid-harmonic engine uses these functions while it evaluates the integrals. It therefore avoids first building the larger Cartesian tensor and then projecting that tensor into the spherical basis.[19,14,15,16,21]

Once the tensor is spherical, it can be written in either a real or a complex form. Real spherical functions allow many nonrelativistic molecular calculations to use only real numbers. Complex spherical functions carry the label|l,m⟩|l,m\rangle, wheremmgives the angular momentum projection along a chosen axis. The two forms contain the same physical information because each real spherical function is a linear combination of complex spherical functions.

Moving safely between the two forms requires three conventions to be stated. The ordering convention says which function occupies each tensor position. The normalization convention fixes the scale of each function. The phase convention fixes its sign or complex phase. These choices matter because the sameddshell can be listed as(dx​y,dy​z,dz2,dx​z,dx2−y2)(d_{xy},d_{yz},d_{z^{2}},d_{xz},d_{x^{2}-y^{2}}), asm=−2,…,2m=-2,\ldots,2, or in a library-specific order. If the choices remain hidden, later transformations to complex spherical functions, spinors, local orbitals, or qubit Hamiltonians can silently permute indices or change signs.

The smaller shell dimension is therefore only the first consequence of starting in a spherical basis. The explicit angular labels also show which tensor entries are allowed by symmetry, which entries are controlled by the same radial quantities, and which calculations can be separated into independent blocks. Because these consequences follow from the representation itself, they can be counted before considering the speed of any particular code.

## IIIWhat Can Be Counted Before Timing a Code

Four exact counts separate the effects of spherical representation from the details of a particular implementation. They describe the number of tensor entries, the entries allowed by angular symmetry, the number of independent radial quantities in an ideal one-center shell, and a rough operation count for calculations organized by magnetic quantum number. Runtime adds further dependence on the screening threshold, basis contraction, data placement in memory, and hardware.

## III.1Final Tensor Size

For an equal-angular-momentum shell quartet(l​l|l​l)(ll|ll), the ratio of spherical tensor entries to Cartesian tensor entries isRtensor​(l)=(SlCl)4=[2​(2​l+1)(l+1)​(l+2)]4.R_{\mathrm{tensor}}(l)=\left(\frac{S_{l}}{C_{l}}\right)^{4}=\left[\frac{2(2l+1)}{(l+1)(l+2)}\right]^{4}.(5)

HereRtensor​(l)R_{\mathrm{tensor}}(l)compares two entry counts and therefore has no units. A value of11means that the Cartesian and spherical tensors have the same number of entries. A value below11means that the spherical tensor is smaller. The fourth power appears because a two-electron shell quartet has four angular axes. At largell, the ratio approaches256/l4256/l^{4}, so the size difference grows rapidly with angular momentum.

The more intuitive quantity is the fractional reduction,Δtensor​(l)=1−Rtensor​(l).\Delta_{\mathrm{tensor}}(l)=1-R_{\mathrm{tensor}}(l).(6)

Fordd,ff,gg, andhhequal-shell quartets, this reduction is approximately51.8%51.8\%,76.0%76.0\%,87.0%87.0\%, and92.5%92.5\%. These percentages quantify the reduction in stored or processed entries, while timing also reflects which entries an implementation forms and how it evaluates them.

## III.2Separating the Tensor by Total Magnetic Quantum Number

The entry count describes the size of the tensor but not its internal organization. The complex spherical basis reveals a second structure because every function has a magnetic labelmm. Consider an ideal one-center shell, meaning that all functions share one center and the interaction is unchanged when the system is rotated. For the scalar Coulomb tensor defined inEq.2, the sum of the two magnetic labels is then conserved between the bra and ket pairs:[73,11,61,19,15]m1+m2=m3+m4.m_{1}+m_{2}=m_{3}+m_{4}.(7)

The labelsm1m_{1}andm2m_{2}belong to the bra pair ofVm1​m2;m3​m4V_{m_{1}m_{2};m_{3}m_{4}}, whilem3m_{3}andm4m_{4}belong to the ket pair. Their sums define the total magnetic quantum numberMMof each pair. Equation (7) therefore says that the Coulomb interaction connects only pairs with the sameMM.

Letn=2​l+1n=2l+1be the number of complex spherical functions in the shell. A dense four-index local tensor hasn4n^{4}entries. The number of entries allowed by the total-MMrule isNM​(l)\displaystyle N_{M}(l)=∑M=−2​l2​l(2​l+1−|M|)2\displaystyle=\sum_{M=-2l}^{2l}\left(2l+1-|M|\right)^{2}=(2​l+1)2+2​∑M=12​l(2​l+1−M)2\displaystyle=(2l+1)^{2}+2\sum_{M=1}^{2l}(2l+1-M)^{2}=(2​l+1)2+2​∑j=12​lj2\displaystyle=(2l+1)^{2}+2\sum_{j=1}^{2l}j^{2}=(2​l+1)2+(2​l)​(2​l+1)​(4​l+1)3\displaystyle=(2l+1)^{2}+\frac{(2l)(2l+1)(4l+1)}{3}=(2​l+1)​(8​l2+8​l+3)3.\displaystyle=\frac{(2l+1)(8l^{2}+8l+3)}{3}.(8)

The counting follows directly from this rule. For a fixed value ofMM, there aren−|M|=2​l+1−|M|n-|M|=2l+1-|M|ordered pairs(m1,m2)(m_{1},m_{2}). The bra and ket can each choose any pair with that same value, which gives(n−|M|)2(n-|M|)^{2}entries in theMMblock. TheM=0M=0block contributesn2n^{2}entries, while the+M+Mand−M-Mblocks have equal sizes. These observations give the second line ofEq.8. The remaining lines use the standard formula for the sum of squares. For example, addshell has block sizes1,2,3,4,5,4,3,2,11,2,3,4,5,4,3,2,1. Squaring and adding these sizes gives8585, which agrees withEq.8forl=2l=2. At largell, the allowed fractionNM​(l)/n4N_{M}(l)/n^{4}decreases approximately as1/(3​l)1/(3l).

In a molecule, nearby atoms change the local environment. Their electric fields, orbital mixing, and basis functions on other centers can therefore couple different values ofMM. The one-center pattern provides a reference against which this mixing can be measured. SectionIVintroduces such a measurement after first explaining a second kind of one-center structure.

## III.3Replacing Many Entries with a Few Radial Parameters

The total-MMrule tells us which entries can be nonzero. Rotational symmetry provides an additional simplification by relating the values of those allowed entries. The Slater–Condon decomposition expresses these relations through a small set of radial parameters.[73,11,61,62,74,29]Each parameter measures a different radial part of the Coulomb interaction, while fixed angular formulas determine how it contributes to the tensor. Many tensor entries therefore share the same underlying physical quantities.

A rotationally invariant Coulomb interaction within a fixedllshell can be expressed through even-rank radial parameters,k=0,2,…,2​l.k=0,2,\ldots,2l.(9)

The integerkklabels one angular pattern, or channel, of the Coulomb interaction. Only evenkkvalues appear for a scalar Coulomb interaction within a fixed shell. The number of radial parameters is thereforeNSC​(l)=l+1.N_{\mathrm{SC}}(l)=l+1.(10)

The notationNSCN_{\mathrm{SC}}means the number of Slater–Condon radial parameters. Addshell usesF0F^{0},F2F^{2}, andF4F^{4}. Anffshell also usesF6F^{6}, whileggandhhshells require five and six parameters. The parameterF0F^{0}sets the repulsion averaged over all directions. The higher parameters describe how that repulsion changes with direction and how it splits atomic states with different arrangements of the electrons. These splittings are often called multiplet splittings. The parameter count is therefore much smaller than then4=(2​l+1)4n^{4}=(2l+1)^{4}entries of a dense local tensor.

The usual Slater–Condon form can be summarized asVm1​m2;m3​m4=∑k=0,2,…,2​lFk​Bm1​m2;m3​m4(k,l).V_{m_{1}m_{2};m_{3}m_{4}}=\sum_{k=0,2,\ldots,2l}F^{k}B_{m_{1}m_{2};m_{3}m_{4}}^{(k,l)}.(11)

HereVm1​m2;m3​m4V_{m_{1}m_{2};m_{3}m_{4}}is one local Coulomb matrix element in the complex spherical basis. The parameterFkF^{k}gives the radial strength of channelkk. The tensorB(k,l)B^{(k,l)}contains fixed numbers that distribute this strength among the angular states. These numbers include Gaunt coefficients, which are integrals of products of spherical harmonics.[19,15]The equation therefore separates the radial part that depends on the shell from the angular part fixed by symmetry.

This compact form reconstructs every symmetry-allowed tensor entry froml+1l+1parameters. In other words, the parameters generate the full tensor rather than selectingl+1l+1of its entries. The relation is exact when the functions belong to one rotationally symmetric shell and share the same radial shape. In a molecule or embedded region, the same formula becomes a model that can be fitted to the calculated tensor. The difference between the fitted model and the tensor then measures how much of the ideal angular structure survives.

## III.4Organizing Calculations in Pair SpaceFigure 3:Four ratios determined by angular representation for equal-llshells fromddthroughhh. Panel (a) shows the percentage reduction in final spherical versus Cartesian tensor entries. Panel (b) shows the percentage of complex-spherical entries that satisfy the total-MMrule. Panel (c) compares the number of independent Slater–Condon radial parameters with the number of entries in the full spherical tensor. It counts independent inputs rather than retained tensor entries. Panel (d) compares a rough operation count for blockwise pair-space updates with the corresponding dense count. Together, the panels isolate representation effects from implementation-dependent timing.

The previous two counts describe the tensor itself. The fourth count describes work performed on that tensor. Many algorithms combine two orbital indices into one pair index and then treat the four-index Coulomb tensor as an ordinary matrix. The resulting matrix is said to be in pair space. Density fitting, Cholesky decomposition, and related methods all use this organization.[84,13,79,82,5,45,34]If the shell hasn=2​l+1n=2l+1functions, then the number of ordered pairs isNpair=n2.N_{\mathrm{pair}}=n^{2}.(12)

A calculation that combines every pair with every other pair often has a leading operation count proportional to the cube of the pair-space dimension. A simple cubic reference count isNpair3=n6.N_{\mathrm{pair}}^{3}=n^{6}.(13)

If the pair states are grouped by total magnetic quantum numberMM, then the block with labelMMhas sizenM=2​l+1−|M|.n_{M}=2l+1-|M|.(14)

The corresponding blockwise work proxy isKM​(l)=∑M=−2​l2​lnM3=(2​l+1)2​(2​l2+2​l+1).K_{M}(l)=\sum_{M=-2l}^{2l}n_{M}^{3}=(2l+1)^{2}(2l^{2}+2l+1).(15)

The ratioKM​(l)/n6K_{M}(l)/n^{6}decreases approximately as1/(8​l2)1/(8l^{2})at largell. It compares idealized operation counts for blockwise and dense calculations. Separating pair states byMMmay therefore reduce the work of matrix updates, low-rank factorizations, and later reductions that operate block by block.

Figure3shows how these four consequences grow fromddthroughhhshells. The first ratio measures how much smaller the spherical tensor is. The second and third describe two levels of physical structure within that tensor: the entries allowed by angular momentum and the radial parameters that determine their values. The fourth shows how an algorithm could use the block structure to organize its work. This sequence leads from tensor representation to the first application, low-rank factorization.

## IVApplication I: Organizing Low-Rank Coulomb RepresentationsFigure 4:Coulomb matrices in pair space for one-centerdd,ff,gg, andhhshells before and after the reversible real-to-complex spherical transformation. Pair states are sorted by total magnetic quantum numberMM. In the real-spherical basis, nonzero entries are spread across the matrices. In the complex|l,m⟩|l,m\ranglebasis, they collect into the blocks required bym1+m2=m3+m4m_{1}+m_{2}=m_{3}+m_{4}. Color shows the base-10 logarithm of each magnitude relative to the largest entry in that matrix. In a molecule, coupling between different blocks would appear as measurable intensity outside the bright block pattern.

Low-rank methods reduce storage and computation by writing a large Coulomb tensor as products of smaller arrays. Density fitting, also called resolution of the identity (RI), introduces an auxiliary basis that approximates products of orbital basis functions. Cholesky decomposition instead builds the smaller factors directly from the Coulomb matrix in pair space. Tensor hypercontraction, compound decomposition, double factorization, and factorizations for quantum simulation break the interaction into other sequences of smaller factors. Although their formulas differ, all of these methods avoid carrying every element of the dense four-index tensor explicitly.[84,13,79,82,5,45,34,56,57,53,6,47]

All of these methods combine two orbital labels into a pair label. Consequently, the angular representation becomes part of their basic data structure. A real spherical pair is compact, but its magnetic labels are not directly visible. A complex spherical pair carriesm1m_{1}andm2m_{2}, so its total label isM=m1+m2M=m_{1}+m_{2}. In the ideal one-center limit, pairs with different values ofMMdo not interact. The pair matrix can therefore be separated into smaller independent blocks:V=⨁MV(M).V=\bigoplus_{M}V^{(M)}.(16)

HereVVis the full local Coulomb matrix in pair space, andV(M)V^{(M)}contains only the pairs with total magnetic quantum numberMM. The direct-sum symbol means that the blocks can be stored and processed independently.

The real-to-complex transformation is unitary, meaning that it is a reversible change of basis that preserves lengths and angles. It therefore preserves the matrix rank, which is the minimum number of independent factors needed to represent the matrix exactly, while making the block structure explicit. Under exact one-center symmetry, a Cholesky approximation can then be written one block at a time:Vp​q(M)≈∑PLp​P(M)​Lq​P(M)⁣∗.V_{pq}^{(M)}\approx\sum_{P}L_{pP}^{(M)}L_{qP}^{(M)*}.(17)

The indicesppandqqlabel pair states inside one total-MMblock. The indexPPlabels one Cholesky vector, which is one column of the low-rank factorL(M)L^{(M)}. Because each factor is confined to a block, a blockwise implementation can avoid storing zeros between different values ofMM. In a molecule, the blocks mix and the useful numerical sparsity then depends on the chosen orbitals, the error threshold, the order in which factor vectors are selected, and the factorization method. Direct measurement therefore determines how much block structure remains.

AsFigure3shows, the fraction of entries inside the ideal total-MMblocks decreases withll, and the rough blockwise operation count decreases even faster. High-llshells are therefore useful test cases for RI, Cholesky, and quantum factorizations that can work with blocks. To test whether the one-center pattern remains useful in a molecule, first construct a reference tensor that keeps only entries with the sameMMon the bra and ket:(Vblock)m1​m2;m3​m4=δm1+m2,m3+m4​Vm1​m2;m3​m4.\left(V_{\mathrm{block}}\right)_{m_{1}m_{2};m_{3}m_{4}}=\delta_{m_{1}+m_{2},m_{3}+m_{4}}V_{m_{1}m_{2};m_{3}m_{4}}.(18)

The Kronecker delta inEq.18equals one when the two sums of magnetic labels are equal and zero otherwise. It therefore keeps entries inside the ideal blocks and removes all other entries. The fraction of the tensor outside those blocks isηoff=‖V−Vblock‖F‖V‖F.\eta_{\mathrm{off}}=\frac{\|V-V_{\mathrm{block}}\|_{F}}{\|V\|_{F}}.(19)

Here∥⋅∥F\|\cdot\|_{F}is the Frobenius norm, which is the square root of the sum of the squared magnitudes of all tensor entries. A smallηoff\eta_{\mathrm{off}}means that most of the tensor remains inside the ideal blocks. A large value means that the molecular environment or the chosen orbitals strongly mix different values ofMM.

The value ofηoff\eta_{\mathrm{off}}depends on which local orbitals are included and how they are defined. A reproducible benchmark must therefore state how the local orbital subspace was selected and how its orbitals were made orthonormal, meaning mutually perpendicular and individually normalized. It must also report the local center and axes, the real and complex spherical order, the phase and normalization conventions, and the four tensor axes underEq.2. If the axes are rotated to minimizeηoff\eta_{\mathrm{off}}, the benchmark should give both the value in a fixed chemically defined frame and the minimized value. Reporting these choices makes comparisons across molecules and codes meaningful.

This measurement also suggests a different computational route. A conventional calculation may first form Cartesian intermediate arrays, project them to spherical functions, assemble a four-index tensor, transform it to complex or local orbitals, and only then begin the factorization. A representation-aware route could instead form spherical shell-pair objects during integral evaluation and pass those objects directly to RI or Cholesky routines. When the factorization needs only selected blocks, newly chosen factor columns, or the remaining approximation error, this route could avoid explicitly forming larger intermediate tensors.

Figure4makes the reorganization visible. The real and complex matrices contain the same information, but the complex basis gathers related pair states into separate blocks. A molecular calculation can useηoff\eta_{\mathrm{off}}to measure how much intensity moves outside this ideal pattern.

Pair-space blocks organize the numerical calculation. If the local interaction also remains close to rotationally symmetric, the Slater–Condon relations organize the physical content of the same tensor using only a few radial parameters. That additional connection leads directly to local Hamiltonians and quantum simulation.

## VApplication II: Building Local Interactions for Quantum SimulationFigure 5:Three levels of one-center Coulomb information fordd,ff,gg, andhhshells. Each line begins with every entry in the four-index spherical tensor. The middle point counts the entries that satisfy the total-MMrule. The final point counts the independent Slater–Condon radial parameters that determine all of those allowed entries in an ideal rotationally symmetric shell. Thus the three points represent the full tensor, its symmetry-allowed entries, and the smaller set of physical inputs from which those entries can be reconstructed.

Quantum simulation does not begin with qubits. It begins with a fermionic Hamiltonian, an operator that describes electrons in a chosen set of orbitals and respects their particle statistics. Creation and annihilation operators in that Hamiltonian add or remove an electron from an orbital. A Jordan–Wigner, Bravyi–Kitaev, or related transformation then translates these electron operators into operations on qubits.[41,9,71,10,51]Because the translation occurs after the electronic Hamiltonian is built, the structure of the final qubit Hamiltonian depends on the Coulomb tensor supplied at the beginning.

If a local high-llinteraction is supplied only as a dense tensor, its many entries can look like unrelated coefficients. In an atomic-like shell, however, different arrangements of the electrons form related energy levels called multiplets. The Slater–Condon construction explains these relationships by deriving every tensor entry from a few radial parameters and fixed angular formulas. The parameterF0F^{0}sets the average repulsion, while the higherFkF^{k}values describe how that repulsion depends on the angular arrangement of the electrons.[73,11,61,62,74]

This shared structure becomes useful when an active space contains localddorffshells together with higher-llpolarization functions.[64,69]An active space is the selected group of orbitals whose electron configurations are treated explicitly. Polarization functions give those orbitals additional freedom to change shape. Within this space, a dense tensor can hide which coefficients come from the same angular interaction. A Slater–Condon-like representation keeps those relationships visible. It can therefore connect the tensor to model quantities such as HubbardUU, which measures an average local repulsion, and Hund coupling, which describes important energy differences between spin arrangements. Kanamori and Racah parameters provide related ways to describe the same local interaction when their assumptions are appropriate.[42,1,49,22]

Each radial parameter contributes to many electron-interaction terms, and each of those terms can become several Pauli strings, which are products of simple operators acting on individual qubits. The final qubit Hamiltonian can therefore remain large even though its coefficients originate from a small set of related Coulomb inputs. Keeping these relationships visible can help organize coefficients, group terms, compare active spaces, and trace errors through the mapping.[4,3,53,6,77,80]

To preserve these relationships, the tensor convention must agree with the order of the electron operators. With the convention inEq.2, one fixed-llcomplex-spherical matrix element isVm1​m2;m3​m4\displaystyle V_{m_{1}m_{2};m_{3}m_{4}}=∫∫ϕl​m1∗​(𝐫1)​ϕl​m2∗​(𝐫2)​1r12\displaystyle=\int\!\!\int\phi_{lm_{1}}^{*}(\mathbf{r}_{1})\phi_{lm_{2}}^{*}(\mathbf{r}_{2})\frac{1}{r_{12}}×ϕl​m3​(𝐫1)​ϕl​m4​(𝐫2)​d​𝐫1​d​𝐫2.\displaystyle\qquad\times\phi_{lm_{3}}(\mathbf{r}_{1})\phi_{lm_{4}}(\mathbf{r}_{2})d\mathbf{r}_{1}d\mathbf{r}_{2}.(20)

The same tensor enters the following operator form for a local interaction that preserves spin:H^U=12​∑σ,τm1,m2,m3,m4Vm1​m2;m3​m4​a^m1​σ†​a^m2​τ†​a^m4​τ​a^m3​σ.\displaystyle\hat{H}_{U}=\frac{1}{2}\sum_{\begin{subarray}{c}\sigma,\tau\\
m_{1},m_{2},m_{3},m_{4}\end{subarray}}V_{m_{1}m_{2};m_{3}m_{4}}\hat{a}_{m_{1}\sigma}^{\dagger}\hat{a}_{m_{2}\tau}^{\dagger}\hat{a}_{m_{4}\tau}\hat{a}_{m_{3}\sigma}.(21)

Hereσ\sigmaandτ\taulabel the electron spins. The operatora^†\hat{a}^{\dagger}creates an electron in the orbital named by its subscripts, whilea^\hat{a}removes one. The factor of1/21/2avoids counting the same electron pair twice. BecauseEq.20fixes both complex conjugation and index order, the total-MMrule and the operator order inH^U\hat{H}_{U}refer to the same tensor entries.

A solid-harmonic integral engine can therefore prepare more than a list of Coulomb values. It can provide local blocks with the angular labels and index order needed to connect the original integrals to multiplet models and, later, to qubit operators.

Figure5shows the two reductions in sequence. Choosing the complex spherical basis first reveals which entries satisfy the total-MMrule. Rotational symmetry then relates the values of those allowed entries through a much smaller set of radial parameters.

This traceable angular structure becomes even more important when orbital and spin labels are combined. Relativistic calculations use spinors that mix those two kinds of information, which makes the Coulomb tensor’s change of basis central to preserving its physical meaning.

## VIApplication III: Transforming Coulomb Tensors for Relativistic and Effective ModelsFigure 6:A Coulomb tensor passes through several representations on its way to an effective model. The first transformation converts the real-spherical tensorGRG_{\mathrm{R}}to the complex|l,m⟩|l,m\rangletensorGCG_{\mathrm{C}}. The next transformation produces interactions in spinor or local orbitals. The low-energy reduction then separates the states that are kept (PP) from those removed from the explicit model (QQ), producing an effective Hamiltonian and transformed observables. Gaunt, Breit, and other spin-dependent two-electron corrections require additional operators and are not supplied by the scalar Coulomb engine.

Relativistic electronic-structure methods introduce another change of representation. Their working orbitals can be complex spinors, which are functions with coupled spatial and spin components. Four-component Dirac methods and exact-two-component methods obtain these spinors from a relativistic one-electron equation. This description is especially important for heavy elements. There, scalar relativistic effects change orbital energies and shapes, while spin-orbit coupling links an electron’s spatial motion to its spin.[20,12,33,18,46,35,50,58,66,63]

The ordinary scalar Coulomb interaction remains one part of this relativistic problem. A solid-harmonic Coulomb engine can supply that part with a well-defined ordering and phase convention. Additional operators are needed for a complete relativistic two-electron treatment. These include Gaunt and Breit terms, which describe magnetic and retardation corrections, as well as picture-change corrections that arise when operators are transformed between relativistic representations.[58,66,63]Keeping these contributions separate makes the role of the scalar Coulomb tensor clear.

The scalar tensor can then pass through the following sequence:GR\displaystyle G_{\mathrm{R}}→GC​(|l,m⟩)→Uspinor/local\displaystyle\rightarrow G_{\mathrm{C}}(|l,m\rangle)\rightarrow U_{\mathrm{spinor/local}}→Heff.\displaystyle\rightarrow H_{\mathrm{eff}}.(22)

HereGRG_{\mathrm{R}}is the Coulomb tensor in a real spherical basis, andGCG_{\mathrm{C}}is the same tensor in the complex spherical|l,m⟩|l,m\ranglebasis. Both use the bra-ket axis order inEq.2. Transforming the orbital indices producesUspinor/localU_{\mathrm{spinor/local}}, the interaction in a spinor or localized-orbital basis. A later reduction producesHeffH_{\mathrm{eff}}, an effective Hamiltonian for the low-energy states that the calculation keeps.

The orbital transformation can be written schematically asUia​b;c​d=∑μ​ν​λ​σCμ​ai⁣∗​Cν​bi⁣∗​Vμ​ν;λ​σ​Cλ​ci​Cσ​di.U_{i}^{ab;cd}=\sum_{\mu\nu\lambda\sigma}C_{\mu a}^{i*}C_{\nu b}^{i*}V_{\mu\nu;\lambda\sigma}C_{\lambda c}^{i}C_{\sigma d}^{i}.(23)

The site labeliiidentifies an atom, fragment, or other region chosen for a local model. The labelsaa,bb,cc, andddidentify the local orbitals kept in that model, while the Greek labels identify the original atomic-orbital functions. The coefficientsCiC^{i}express each local orbital as a combination of the original functions. Because the first two axes ofVVbelong to the bra side, the corresponding coefficients are complex conjugated. The equation therefore carries the tensor convention inEq.2into the local basis.

The next step, often called downfolding, replaces a large Hamiltonian with a smaller one for selected low-energy states. High-energy states are removed from the explicit calculation, but their influence is retained through modified interactions and observables. Schrieffer–Wolff transformations, Bloch and Okubo effective Hamiltonians, similarity-renormalization methods, and flow-equation approaches are different ways to carry out this reduction.[55,7,70,26,27,81,83,43]Because the reduction must update both the interactions and the measured quantities, forming a dense spinor Coulomb tensor beforehand can require substantial storage and transformation work.

A representation-aware interface offers a different order of operations. A solid-harmonic engine can provide real or complex spherical pair blocks before the calculation forms the full spinor tensor. Later code can transform, screen, factor, or select those blocks while their angular labels remain visible. The physical reduction is unchanged, but the calculation gains control over which intermediate tensors are formed and which labels remain available at each step.

This traceability is central for multiorbital Hubbard models with spin-orbit coupling. In these models, the retained orbitals mix spin and high-llangular character, so a single unlabeled interaction value cannot describe the local physics.[40]The full tensorUia​b;c​dU_{i}^{ab;cd}is needed, and each of its axes should remain connected to the parent angular momentum, spinor composition, and multiplet structure. A convention-controlled solid-harmonic tensor provides that starting point.Figure6separates the changes of basis from the later removal of high-energy states.

Low-rank factorization, local-model construction, and relativistic or low-energy transformations therefore share one requirement: angular information must remain useful and traceable after each change of representation. A common set of measurable tests can determine whether that requirement is met.

## VIIFrom Perspective to a Testable Benchmark ProgramFigure 7:Five checks follow the same Coulomb tensor from integral generation to later applications. First, a complete record of ordering, phase, normalization, and axis conventions makes every transformation reproducible. Second, the weight outside ideal total-MMblocks measures how strongly a molecular environment mixes angular sectors. Third, the locations of nonzero factor entries show whether the block pattern remains useful in a low-rank representation. Fourth, fitted local parameters test whether a dense tensor retains a simple physical interpretation. Fifth, the final calculation checks whether the original angular labels remain traceable after mapping and reduction.

The three applications raise two separate questions. How quickly can an integral engine produce the tensor, and how much of the tensor’s angular structure remains useful afterward? Timings alone answer only the first question. They also depend on engineering choices such as screening, which skips negligible integrals, batching, which groups similar work, and vectorization, which processes many values together. A useful benchmark should therefore combine performance measurements with diagnostics, meaning measurable checks of the tensor and its later transformations. The five checks inFigure7follow the same Coulomb information from integral generation to its final use.

The first check asks whether the tensor convention is complete. A reported high-lltensor should specify the chemists-to-pair mapping inEq.2, the order of its four axes, the order of the real and complex spherical functions, the phase convention, and the normalization convention. This descriptive information is often called metadata. Without it, two codes can store the same physics in different index orders or with different signs, and a later transformation may silently combine incompatible tensors.

The second check measures local angular mixing. For an isolated one-center shell, the total-MMrule is exact. A molecular environment can move tensor weight outside those ideal blocks. The benchmark should constructVblockV_{\mathrm{block}}withEq.18and report the off-block fractionηoff\eta_{\mathrm{off}}fromEq.19. It should also state how the local orbitals were chosen and made orthonormal, which center and axes were used, and whether the axes were rotated to reduce the mixing. If a local orbital contains several angular momenta, the benchmark should report the fraction belonging to the shell being analyzed. These details ensure that differences inηoff\eta_{\mathrm{off}}reflect the molecular system rather than hidden choices in the analysis.

The third check asks whether the angular blocks remain useful after factorization. A Cholesky, RI, tensor-hypercontraction, or quantum low-rank calculation should report how many factors it produces and where their nonzero entries occur inside and outside the angular blocks. It should also state the error threshold used to stop the decomposition, the rule used to choose each new factor, and the orbital basis in which the decomposition was performed. These details matter because a reversible change of basis preserves exact rank, while the pattern of small numerical entries can change with the factorization procedure.

The fourth check asks whether the local tensor still has a compact physical interpretation. For a correlated shell, the benchmark should report the full local tensor, the fitted Slater–Condon or related model parameters, and the residual, which is the part of the tensor that the fitted model does not reproduce. Racah, Kanamori, Hubbard-UU, or Hund-coupling values can then be given when the corresponding model is appropriate. The residual shows how far the molecular interaction has moved away from the ideal rotationally symmetric shell.

The fifth check follows the labels to the end of the calculation. When the same local block passes through a spinor transformation, active-space selection, low-rank factorization, or qubit mapping, the benchmark should record whether its angular and orbital labels remain traceable. This final check connects integral generation to scientific interpretation because an efficient intermediate tensor has limited value if its later transformations cannot be reconstructed or verified.

Together, the five checks turn the representation argument into questions that can be answered with data. Integral engines can report fully described pair objects. Molecular calculations can measure angular mixing. Factorization methods can show where their factors are nonzero at a stated accuracy. Local-model builders can compare dense tensors with a few fitted physical parameters. Spinor and quantum workflows can then verify that the same labels survive to their final outputs. These results provide the evidence needed to guide the future interface described in the Outlook.

## VIIIOutlook

The most immediate opportunity is to make angular representation a usable part of the integral interface. A real or complex solid-harmonic engine can return compact shell tensors together with explicit ordering, normalization, phase, and magnetic-quantum-number labels. If these descriptors travel with the tensor, downstream codes can organize low-rank factors, local interactions, spinor transformations, and qubit mappings without reconstructing the angular meaning after integral generation.

Turning this idea into a practical standard will require benchmarks at two levels. At the integral level, direct solid-harmonic and Cartesian-to-spherical routes should be compared with the same basis sets, thresholds, contraction patterns, and hardware. At the tensor level, the resulting objects should be tested throughηoff\eta_{\mathrm{off}}, factor support, parameter-fit residuals, and convention checks. Together, these measurements can reveal which benefits come from the smaller spherical representation, which arise from angular organization, and which depend on a particular implementation.

An especially useful next step is to map how one-center angular structure survives in molecules. Total-MMblocks and compact Slater–Condon parameters provide exact reference patterns for an isolated rotationally invariant shell. Across ligand fields, low-symmetry geometries, and heavy-element environments, controlled studies can determine when those patterns remain accurate enough to guide screening, factorization, or local-model construction. Such studies would build a quantitative connection between atomic angular physics and molecular tensor algorithms.

Longer term, representation-aware ERIs could support closer integration across electronic-structure workflows. Relativistic calculations could carry convention-controlled complex spherical blocks into spinor bases. Local-Hamiltonian builders could fit and validate multiplet parameters directly from those blocks. Quantum-simulation codes could test whether angular sectors improve factorization or reduce data movement before fermion-to-qubit mapping. Because the same metadata would accompany each transformation, results would become easier to audit and compare across codes.

The broader outlook is therefore a shift from integral engines that return numerical arrays to integral engines that return structured Coulomb objects. Such an interface would connect efficient integral generation to the symmetries, physical models, and computational choices that shape the rest of a many-electron calculation.

## acknowledgments

This work was supported by the Early Career Research Program of the U.S. Department of Energy, Office of Science, under Grant No. FWP 83466.

## References
- [1]V. I. Anisimov, J. Zaanen, and O. K. Andersen(1991)Band theory and mott insulators: hubbard u instead of stoner i..Phys. Rev. B44,pp. 943–954.External Links:DocumentCited by:§V.
- [2]A. Asadchev and E. F. Valeev(2024)3-center and 4-center 2-particle gaussian ao integrals on modern accelerated processors..J. Chem. Phys.160,pp. 214110.External Links:DocumentCited by:§I.
- [3]R. Babbush, C. Gidney, D. W. Berry, N. Wiebe, J. McClean, A. Paler, A. Fowler, and H. Neven(2018)Encoding electronic spectra in quantum circuits with linear t complexity..Phys. Rev. X8,pp. 041015.External Links:DocumentCited by:§I,§V.
- [4]R. Babbush, N. Wiebe, J. McClean, J. McClain, H. Neven, and G. K.-L. Chan(2018)Low-depth quantum simulation of materials..Phys. Rev. X8,pp. 011044.External Links:DocumentCited by:§I,§V.
- [5]N. H. F. Beebe and J. Linderberg(1977)Simplifications in the generation and transformation of two-electron integrals in molecular calculations..Int. J. Quantum Chem.12,pp. 683–705.External Links:DocumentCited by:§I,§III.4,§IV.
- [6]D. W. Berry, C. Gidney, M. Motta, J. R. McClean, and R. Babbush(2019)Qubitization of arbitrary basis quantum chemistry leveraging sparsity and low rank factorization..Quantum3,pp. 208.External Links:DocumentCited by:§I,§IV,§V.
- [7]C. Bloch(1958)Sur la theorie des perturbations des etats lies..Nucl. Phys.6,pp. 329–347.External Links:DocumentCited by:§VI.
- [8]S. F. Boys(1950)Electronic wave functions. i. a general method of calculation for the stationary states of any molecular system..Proc. R. Soc. Lond. A200,pp. 542–554.External Links:DocumentCited by:§I,§I,§I.
- [9]S. B. Bravyi and A. Y. Kitaev(2002)Fermionic quantum computation..Ann. Phys.298,pp. 210–226.External Links:DocumentCited by:§V.
- [10]Y. Cao, J. Romero, J. P. Olson, M. Degroote, P. D. Johnson, M. Kieferova, I. D. Kivlichan, T. Menke, B. Peropadre, N. P. D. Sawaya, S. Sim, L. Veis, and A. Aspuru-Guzik(2019)Quantum chemistry in the age of quantum computing..Chem. Rev.119,pp. 10856–10915.External Links:DocumentCited by:§I,§V.
- [11]E. U. Condon(1930)The theory of complex spectra..Phys. Rev.36,pp. 1121–1133.External Links:DocumentCited by:§III.2,§III.3,§V.
- [12]M. Douglas and N. M. Kroll(1974)Quantum electrodynamical corrections to the fine structure of helium..Ann. Phys.82,pp. 89–155.External Links:DocumentCited by:§I,§VI.
- [13]B. I. Dunlap, J. W. D. Connolly, and J. R. Sabin(1979)On some approximations in applications of x alpha theory..J. Chem. Phys.71,pp. 3396–3402.External Links:DocumentCited by:§I,§III.4,§IV.
- [14]B. I. Dunlap(1990)Three-center gaussian-type-orbital integral evaluation using solid spherical harmonics..Phys. Rev. A42,pp. 1127–1137.External Links:DocumentCited by:§I,§I,§I,§II.
- [15]B. I. Dunlap(2002)Generalized gaunt coefficients..Phys. Rev. A66,pp. 032502.External Links:DocumentCited by:§I,§II,§III.2,§III.3.
- [16]B. I. Dunlap(2003)Angular momentum in solid-harmonic-gaussian integral evaluation..J. Chem. Phys.118,pp. 1036–1043.External Links:DocumentCited by:§I,§I,§I,§II,§II.
- [17]M. Dupuis, J. Rys, and H. F. King(1976)Evaluation of molecular integrals over gaussian basis functions..J. Chem. Phys.65,pp. 111–116.External Links:DocumentCited by:§I.
- [18]K. G. Dyall(1997)Interfacing relativistic and nonrelativistic methods. i. normalized elimination of the small component in the modified dirac equation..J. Chem. Phys.106,pp. 9618–9626.External Links:DocumentCited by:§I,§VI.
- [19]G. Fieck(1979)Racah algebra and talmi transformation in the theory of multi-centre integrals of gaussian orbitals..J. Phys. B: Atom. Molec. Phys.12,pp. 1063–1080.External Links:DocumentCited by:§I,§II,§III.2,§III.3.
- [20]L. L. Foldy and S. A. Wouthuysen(1950)On the dirac theory of spin 1/2 particles and its non-relativistic limit..Phys. Rev.78,pp. 29–36.External Links:DocumentCited by:§I,§VI.
- [21]A. Fortunelli and O. Salvetti(1993)Recurrence relations for the evaluation of electron repulsion integrals over spherical gaussian functions..Int. J. Quant. Chem.48,pp. 257–265.External Links:DocumentCited by:§I,§I,§I,§II.
- [22]A. Georges, L. de’ Medici, and J. Mravlje(2013)Strong correlations from hund’s coupling..Annu. Rev. Condens. Matter Phys.4,pp. 137–178.External Links:DocumentCited by:§V.
- [23]P. M. W. Gill, M. Head-Gordon, and J. A. Pople(1990)Efficient computation of two-electron-repulsion integrals and their nth-order derivatives using contracted gaussian basis sets..J. Phys. Chem.94,pp. 5564–5572.External Links:DocumentCited by:§I.
- [24]P. M. W. Gill and J. A. Pople(1991)The prism algorithm for two-electron integrals..Int. J. Quant. Chem.40,pp. 753–772.External Links:DocumentCited by:§I.
- [25]P. M. W. Gill(1994)Molecular integrals over gaussian basis functions..Adv. Quantum Chem.25,pp. 141–205.External Links:DocumentCited by:§I,§I,§I.
- [26]S. D. Glazek and K. G. Wilson(1993)Renormalization of hamiltonians..Phys. Rev. D48,pp. 5863–5872.External Links:DocumentCited by:§VI.
- [27]S. D. Glazek and K. G. Wilson(1994)Perturbative renormalization group for hamiltonians..Phys. Rev. D49,pp. 4214–4218.External Links:DocumentCited by:§VI.
- [28]A. S. P. Gomes, K. G. Dyall, and L. Visscher(2010)Relativistic double-zeta, triple-zeta, and quadruple-zeta basis sets for the lanthanides la–lu..Theor. Chem. Acc.127,pp. 369–381.External Links:DocumentCited by:§I.
- [29]J. S. Griffith(1961)The theory of transition-metal ions.Cambridge University Press,Cambridge.Cited by:§III.3.
- [30]M. Head-Gordon and J. A. Pople(1988)A method for two-electron gaussian integral and integral derivative evaluation using recurrence relations..J. Chem. Phys.89,pp. 5777–5786.External Links:DocumentCited by:§I.
- [31]D. Hegarty and G. van der Velde(1983)Integral evaluation algorithms and their implementation..Int. J. Quant. Chem.23,pp. 1135–1153.External Links:DocumentCited by:§I.
- [32]D. Hegarty(1984)Evaluation and processing of integrals.InAdvanced Theories and Computational Approaches to the Electronic Structure of Molecules,C. E. Dykstra (Ed.),Vol.133,pp. 39–66.External Links:DocumentCited by:§I.
- [33]B. A. Hess(1986)Relativistic electronic-structure calculations employing a two-component no-pair formalism with external-field projection operators..Phys. Rev. A33,pp. 3742–3748.External Links:DocumentCited by:§I,§VI.
- [34]E. G. Hohenstein, R. M. Parrish, and T. J. Martinez(2012)Tensor hypercontraction density fitting. i. quartic scaling second- and third-order moller-plesset perturbation theory..J. Chem. Phys.137,pp. 044103.External Links:DocumentCited by:§I,§III.4,§IV.
- [35]M. Ilias and T. Saue(2007)An infinite-order two-component relativistic hamiltonian by a simple one-step transformation..J. Chem. Phys.126,pp. 064102.External Links:DocumentCited by:§I,§VI.
- [36]K. Ishida(1998)Rigorous formula for the fast calculation of the electron repulsion integral over the solid harmonic gaussian-type orbitals..J. Chem. Phys.109,pp. 881–890.External Links:DocumentCited by:§I,§I.
- [37]K. Ishida(1999)Rigorous and rapid calculation of the electron repulsion integral over the uncontracted solid harmonic gaussian-type orbitals..J. Chem. Phys.111,pp. 4913–4922.External Links:DocumentCited by:§I,§I.
- [38]K. Ishida(2000)Rigorous algorithm for the electron repulsion integral over the generally contracted solid harmonic gaussian-type orbitals..J. Chem. Phys.113,pp. 7818–7829.External Links:DocumentCited by:§I,§I.
- [39]K. Ishida(2002)Accompanying coordinate expansion formulas derived with the solid harmonic gradient..J. Comput. Chem.23,pp. 378–393.External Links:DocumentCited by:§I,§I.
- [40]G. Jackeli and G. Khaliullin(2009)Mott insulators in the strong spin-orbit coupling limit: from heisenberg to a quantum compass and kitaev models..Phys. Rev. Lett.102,pp. 017205.External Links:DocumentCited by:§VI.
- [41]P. Jordan and E. Wigner(1928)Uber das paulische aquivalenzverbot..Z. Phys.47,pp. 631–651.External Links:DocumentCited by:§V.
- [42]J. Kanamori(1963)Electron correlation and ferromagnetism of transition metals..Prog. Theor. Phys.30,pp. 275–289.External Links:DocumentCited by:§V.
- [43]S. Kehrein(2006)The flow equation approach to many-particle systems.Springer,Berlin.Cited by:§VI.
- [44]H. F. King and M. Dupuis(1976)Numerical integration using rys polynomials..J. Comput. Phys.21,pp. 144–165.External Links:DocumentCited by:§I.
- [45]H. Koch, A. S. de Meras, and T. B. Pedersen(2003)Reduced scaling in electronic structure calculations using cholesky decompositions..J. Chem. Phys.118,pp. 9481–9484.External Links:DocumentCited by:§I,§III.4,§IV.
- [46]W. Kutzelnigg and W. Liu(2005)Quasirelativistic theory equivalent to fully relativistic theory..J. Chem. Phys.123,pp. 241102.External Links:DocumentCited by:§I,§VI.
- [47]J. Lee, D. W. Berry, C. Gidney, W. J. Huggins, J. R. McClean, N. Wiebe, and R. Babbush(2021)Even more efficient quantum computations of chemistry through tensor hypercontraction..PRX Quantum2,pp. 030305.External Links:DocumentCited by:§I,§IV.
- [48]R. Li, Q. Sun, X. Zhang, and G. K.-L. Chan(2025)Introducing gpu-acceleration into the python-based simulations of chemistry framework..J. Phys. Chem. A129,pp. 1459–1468.External Links:DocumentCited by:§I.
- [49]A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen(1995)Density-functional theory and strong interactions: orbital ordering in mott-hubbard insulators..Phys. Rev. B52,pp. R5467–R5470.External Links:DocumentCited by:§V.
- [50]W. Liu and D. Peng(2009)Exact two-component hamiltonians revisited..J. Chem. Phys.131,pp. 031104.External Links:DocumentCited by:§I,§VI.
- [51]J. R. McClean, J. Romero, R. Babbush, and A. Aspuru-Guzik(2016)The theory of variational hybrid quantum-classical algorithms..New J. Phys.18,pp. 023023.External Links:DocumentCited by:§I,§V.
- [52]L. E. McMurchie and E. R. Davidson(1978)One- and two-electron integrals over cartesian gaussian functions..J. Comput. Phys.26,pp. 218–231.External Links:DocumentCited by:§I,§I,§I,§II.
- [53]M. Motta, E. Ye, J. R. McClean, Z. Li, A. J. Minnich, R. Babbush, and G. K.-L. Chan(2021)Low rank representations for quantum simulation of electronic structure..npj Quantum Information7,pp. 83.External Links:DocumentCited by:§I,§IV,§V.
- [54]S. Obara and A. Saika(1986)Efficient recursive computation of molecular integrals over cartesian gaussian functions..J. Chem. Phys.84,pp. 3963–3974.External Links:DocumentCited by:§I,§I.
- [55]S. Okubo(1954)Diagonalization of hamiltonian and tamm-dancoff equation..Prog. Theor. Phys.12,pp. 603–622.External Links:DocumentCited by:§VI.
- [56]R. M. Parrish, E. G. Hohenstein, N. F. Schunck, C. D. Sherrill, and T. J. Martinez(2012)Tensor hypercontraction. ii. least-squares renormalization..J. Chem. Phys.137,pp. 224106.External Links:DocumentCited by:§I,§IV.
- [57]B. Peng and K. Kowalski(2017)Highly efficient and scalable compound decomposition of two-electron integral tensor and its application in coupled cluster calculations..J. Chem. Theory Comput.13,pp. 4179–4192.External Links:DocumentCited by:§I,§IV.
- [58]D. Peng, N. Middendorf, F. Weigend, and M. Reiher(2013)An efficient implementation of two-component relativistic exact-decoupling methods for large molecules..J. Chem. Phys.138,pp. 184105.External Links:DocumentCited by:§VI,§VI.
- [59]J. A. Pople and W. J. Hehre(1978)Computation of electron repulsion integrals involving contracted gaussian basis functions..J. Comput. Phys.27,pp. 161–168.External Links:DocumentCited by:§I,§II.
- [60]B. P. Pritchard and E. Chow(2016)Horizontal vectorization of electron repulsion integrals..J. Comput. Chem.37,pp. 2537–2546.External Links:DocumentCited by:§I.
- [61]G. Racah(1942)Theory of complex spectra. ii..Phys. Rev.62,pp. 438–462.External Links:DocumentCited by:§III.2,§III.3,§V.
- [62]G. Racah(1943)Theory of complex spectra. iii..Phys. Rev.63,pp. 367–382.External Links:DocumentCited by:§III.3,§V.
- [63]M. Reiher and A. Wolf(2015)Relativistic quantum chemistry: the fundamental theory of molecular science.Wiley-VCH,Weinheim.Cited by:§I,§I,§VI,§VI.
- [64]B. O. Roos, P. R. Taylor, and P. E. M. Siegbahn(1980)A complete active space scf method (casscf) using a density matrix formulated super-ci approach..Chem. Phys.48,pp. 157–173.External Links:DocumentCited by:§V.
- [65]J. Rys, M. Dupuis, and H. F. King(1983)Computation of electron repulsion integrals using the rys quadrature method..J. Comput. Chem.4,pp. 154–157.External Links:DocumentCited by:§I.
- [66]T. Saueet al.(2020)The dirac code for relativistic molecular calculations..J. Chem. Phys.152,pp. 204104.External Links:DocumentCited by:§I,§I,§VI,§VI.
- [67]V. R. Saunders(1975)An introduction to molecular integral evaluation.InComputational Techniques in Quantum Chemistry and Molecular Physics,G. H. F. Diercksen, B. T. Sutcliffe, and A. Veillard (Eds.),Vol.15,pp. 347–424.External Links:DocumentCited by:§I.
- [68]V. R. Saunders(1983)Molecular integrals for gaussian type functions.InMethods in Computational Molecular Physics,G. H. F. Diercksen and S. Wilson (Eds.),Vol.113,pp. 1–36.External Links:DocumentCited by:§I.
- [69]E. R. Sayfutyarova, Q. Sun, G. K.-L. Chan, and G. Knizia(2017)Automated construction of molecular active spaces from atomic valence orbitals..J. Chem. Theory Comput.13,pp. 4063–4078.External Links:DocumentCited by:§V.
- [70]J. R. Schrieffer and P. A. Wolff(1966)Relation between the anderson and kondo hamiltonians..Phys. Rev.149,pp. 491–492.External Links:DocumentCited by:§VI.
- [71]J. T. Seeley, M. J. Richard, and P. J. Love(2012)The bravyi-kitaev transformation for quantum computation of electronic structure..J. Chem. Phys.137,pp. 224109.External Links:DocumentCited by:§V.
- [72]I. Shavitt(1963)The gaussian function in calculations of statistical mechanics and quantum mechanics.InMethods in Computational Physics,B. Alder, S. Fernbach, and M. Rotenberg (Eds.),Vol.2,pp. 1–45.Cited by:§I,§I.
- [73]J. C. Slater(1929)The theory of complex spectra..Phys. Rev.34,pp. 1293–1322.External Links:DocumentCited by:§III.2,§III.3,§V.
- [74]S. Sugano, Y. Tanabe, and H. Kamimura(1970)Multiplets of transition-metal ions in crystals.Academic Press,New York.Cited by:§III.3,§V.
- [75]Q. Sun(2015)Libcint: an efficient general integral library for gaussian basis functions..J. Comput. Chem.36,pp. 1664–1671.External Links:DocumentCited by:§I,§I,§I.
- [76]Jr. T. H. Dunning(1989)Gaussian basis sets for use in correlated molecular calculations. i. the atoms boron through neon and hydrogen..J. Chem. Phys.90,pp. 1007–1023.External Links:DocumentCited by:§I.
- [77]T. Takeshita, N. C. Rubin, Z. Jiang, E. Lee, R. Babbush, and J. R. McClean(2020)Increasing the representation accuracy of quantum simulations of chemistry without extra quantum resources..Phys. Rev. X10,pp. 011004.External Links:DocumentCited by:§I,§V.
- [78]I. S. Ufimtsev and T. J. Martinez(2008)Quantum chemistry on graphical processing units. 1. strategies for two-electron integral evaluation..J. Chem. Theory Comput.4,pp. 222–231.External Links:DocumentCited by:§I.
- [79]O. Vahtras, J. Almlof, and M. W. Feyereisen(1993)Integral approximations for lcao-scf calculations..Chem. Phys. Lett.213,pp. 514–518.External Links:DocumentCited by:§I,§III.4,§IV.
- [80]V. von Burg, G. H. Low, T. Haner, D. S. Steiger, M. Reiher, M. Roetteler, and M. Troyer(2021)Quantum computing enhanced computational catalysis..Phys. Rev. Research3,pp. 033055.External Links:DocumentCited by:§I,§V.
- [81]F. Wegner(1994)Flow-equations for hamiltonians..Ann. Physik506,pp. 77–91.External Links:DocumentCited by:§VI.
- [82]F. Weigend(2002)A fully direct ri-hf algorithm: implementation, optimised auxiliary basis sets, demonstration of accuracy and efficiency..Phys. Chem. Chem. Phys.4,pp. 4285–4291.External Links:DocumentCited by:§I,§III.4,§IV.
- [83]S. R. White(2002)Numerical canonical transformation approach to quantum many-body problems..J. Chem. Phys.117,pp. 7472–7482.External Links:DocumentCited by:§VI.
- [84]J. L. Whitten(1973)Coulombic potential energy integrals and approximations..J. Chem. Phys.58,pp. 4496–4501.External Links:DocumentCited by:§I,§III.4,§IV.
- [85]X. Wu, T. Kenter, R. Schade, T. D. Kuhne, and C. Plessl(2023)Computing and compressing electron repulsion integrals on fpgas..In2023 IEEE 31st Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM),pp. 162–173.External Links:DocumentCited by:§I.
- [86]K. Yasuda(2008)Two-electron integral evaluation on the graphics processor unit..J. Comput. Chem.29,pp. 334–342.External Links:DocumentCited by:§I.

## 


- 


Major funding support from
