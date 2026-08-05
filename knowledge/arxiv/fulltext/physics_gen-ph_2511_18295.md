# Discrete Action, Graph Evolution, and the Hierarchy of Symmetries: A Rigorous Construction of Temporal Layers $C1 \to C2 \to C3 \to C4$

**arXiv ID**: 2511.18295v1
**Authors**: Medeu Abishev, Daulet Berkimbayev
**Published**: 2025-11-23
**Categories**: physics.gen-ph, hep-th, quant-ph
**Comments**: 4 pages, 3 figures
**HTML URL**: https://arxiv.org/html/2511.18295v1

## Abstract

Postulating a minimal discrete quantum of action $S=\hbar$ and a simple rule for the growth of an oriented graph, we construct a strict hierarchy of temporal layers $C N$ with discrete periods $τ_N=N\hbar/E$. Each layer is specified by its configuration space, symplectic structure, update rule, and emergent symmetry. At $C1$ the state is represented by a single oriented edge with $U(1)$ phase $e^{i E t/\hbar}$. The transition $C1 \to C2$ splits the edge into two independent flows, which yields canonical pairs $(x_a,p_a)$, local $U(1)$ invariance, and an effective $(2{+}1)$ metric with signature $(+--)$. The closure $C2 \to C3$ produces $SU(3)$ connections and an Einstein-Yang-Mills type action. We show that these structures follow from discrete-action principles, and that stochastic graph growth naturally provides mechanisms for decoherence and spontaneous symmetry breaking.

## Full Text

Discrete Action, Graph Evolution, and the Hierarchy of Symmetries: A Rigorous Construction of Temporal Layers 𝒞⁢1→𝒞⁢2→𝒞⁢3→𝒞⁢4
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

## Discrete Action, Graph Evolution, and the Hierarchy of Symmetries:
A Rigorous Construction of Temporal Layers𝒞​1→𝒞​2→𝒞​3→𝒞​4\mathcal{C}1\!\to\!\mathcal{C}2\!\to\!\mathcal{C}3\!\to\!\mathcal{C}4Medeu AbishevAl-Farabi Kazakh National University, Almaty, KazakhstanNational University of Singapore, SingaporeDaulet BerkimbayevAl-Farabi Kazakh National University, Almaty, Kazakhstan(November 23, 2025)

## Abstract

Postulating a minimal discrete quantum of actionS=ℏS=\hbarand a simple rule for the growth of an oriented graph, we construct a strict hierarchy of temporal layers𝒞​N\mathcal{C}Nwith discrete periodsτN=N​ℏ/E\tau_{N}=N\hbar/E. Each layer is specified by its configuration space, symplectic structure, update rule, and emergent symmetry. At𝒞​1\mathcal{C}1the state is represented by a single oriented edge withU​(1)U(1)phaseei​E​t/ℏ\mathrm{e}^{\mathrm{i}Et/\hbar}. The transition𝒞​1→𝒞​2\mathcal{C}1\!\to\!\mathcal{C}2splits the edge into two independent flows, which yields canonical pairs(xa,pa)(x_{a},p_{a}), localU​(1)U(1)invariance, and an effective(2+1)(2{+}1)metric with signature(+−−)(+--). The closure𝒞​2→𝒞​3\mathcal{C}2\!\to\!\mathcal{C}3producesS​U​(3)SU(3)connections and an Einstein–Yang–Mills type action. We show that these structures follow from discrete-action principles, and that stochastic graph growth naturally provides mechanisms for decoherence and spontaneous symmetry breaking.

PACS:04.60.-m, 04.20.Cv, 11.15.-q, 02.10.Ox

## IIntroduction

In modern physics, evolution is usually treated as a continuous process on a differentiable manifold: from Newtonian mechanics to the Schrödinger and Einstein equations[1,2,3]. Despite the broad success of this viewpoint, there are indications of indivisible quanta of dynamics or granular bounds at microscopic scales.

A natural reference scale is the Planck timetPl∼5.4×10−44​st_{\mathrm{Pl}}\!\sim\!5.4\times 10^{-44}\,\mathrm{s}[4]. While it does not, by itself, assert the discreteness of time, the quantum of actionℏ\hbaralready constrains evolution via time–energy uncertainty and quantum speed limits[5,6,7]. This motivates an operational stance: physically accessible updates occur at discrete “ticks”, with the continuous time parameter serving primarily as an interpolation label between them.

Discrete microstructures have been explored in many programs—from causal sets and loop quantum gravity to triangulations and noncommutative geometry[10,11,12,13,14,15,16,17,18]. Discrete-time evolution also appears in lattice gauge theory, quantum walks, and quantum cellular automata[19,20,21,22]. Preserving relativistic symmetries imposes stringent constraints on admissible discretizations[12,25,26,27,28,29].

Here we propose a minimal, discrete operational framework in whichℏ\hbargoverns both dynamics and symmetry formation. Only state updates that accumulate a quantum of action are allowed. We show how effective continuum descriptions emerge when the tick is small compared to system timescales, with generators remaining regular withoutad hoccutoffs[30]. We outline phenomenological windows—from interferometric phase accumulation and quantum control to cosmology[28,29]. The approach is related to causal sets, loop gravity, and “quantum graphity”[31,32], but differs crucially: the discrete variable is the action increment attached to each new graph edge.

## IIDiscrete action and the graph rule

We work with graphs as a mathematical representation of the system rather than as physical objects. At the beginning of continuous time, consider a system specified by a single loop/edge with elementary discrete actionS1≡E1​τ1=ℏ,τ1=ℏE1,S_{1}\equiv E_{1}\tau_{1}=\hbar,\qquad\tau_{1}=\frac{\hbar}{E_{1}},(1)

whereE1>0E_{1}>0, whilet∈ℝt\in\mathbb{R}remains a macroscopic label.

The hierarchy of layers is introduced inductively:τN=N​τ1,SN=N​ℏ.\tau_{N}=N\tau_{1},\qquad S_{N}=N\hbar.(2)

Different directions for transporting actionSSalong the initial loop are allowed, encoded by a minimal “spin”ss(not identified with the quantum-mechanical spin). The oriented “spin–orbital” separation between{|b⟩,|e⟩}\{\ket{b},\ket{e}\}is captured byΔ=ℏ​(01−10)=i​ℏ​σy,\Delta=\hbar\!\begin{pmatrix}0&1\\
-1&0\end{pmatrix}=\mathrm{i}\hbar\,\sigma_{y},(3)

so thatb→eb\!\to\!emeasures+ℏ+\hbarande→be\!\to\!bmeasures−ℏ-\hbar. Spin conservation is equivalent to conservation of total angular momentum.

A system at level𝒞​N\mathcal{C}Nis an oriented graphGNG_{N}withNNedges evolving under:
- 1.

one new oriented edge per step;
- 2.

conservation of total action:Sn+1=Sn+ℏS_{n+1}=S_{n}+\hbar;
- 3.

invariance of totalJzJ_{z}.

## IIILayer𝒞​1\mathcal{C}1: single edge andU​(1)U(1)phase

Configuration: a single oriented edgee1:(v0→v1)e_{1}:(v_{0}\!\to\!v_{1}), Fig.1. Phase space:ℳ1=S1,ω1=ℏ​dθ,\mathcal{M}_{1}=S_{1},\qquad\omega_{1}=\hbar\,\differential\theta,(4)

whereθ\thetais the elementary loop phase. ForH1=E1H_{1}=E_{1}we haveθ˙=1\dot{\theta}=1. The wavefunctionψ1=ψ0​exp⁡(iℏ​S)=ψ0​exp⁡(iℏ​E​t),S=ℏ.\psi_{1}=\psi_{0}\exp\!\left(\frac{\mathrm{i}}{\hbar}S\right)=\psi_{0}\exp\!\left(\frac{\mathrm{i}}{\hbar}E\,t\right),\quad S=\hbar.(5)

This implements aU​(1)U(1)phase rotation. Nevertheless, interpreting the entire universe at level𝒞​1\mathcal{C}1as generating the electromagnetic interaction is not appropriate; the next step is required.v0v_{0}v1v_{1}e1e_{1}𝒞​1:U​(1)\mathcal{C}1:\penalty 10000\ U(1)Figure 1:Layer𝒞​1\mathcal{C}1: a single oriented edge between(v0,v1)(v_{0},v_{1})withU​(1)U(1)phase evolution (e1e_{1}).

## IVTransition𝒞​1→𝒞​2\mathcal{C}1\!\to\!\mathcal{C}2: canonical pairs and metric

According to the growth rule, the initial edge splits into two, Fig.2:v0→e21vm→e22v1,E21+E22=E1,v_{0}\xrightarrow{e_{21}}v_{m}\xrightarrow{e_{22}}v_{1},\quad E_{21}+E_{22}=E_{1},(6)

wherevmv_{m}is a new vertex. We introduce coordinates and momentaxa=c​t2​a,pa=E2​a/c,x_{a}=ct_{2a},\quad p_{a}=E_{2a}/c,(7)

witha=1,2a=1,2andcca proportionality constant between momentum and energy. The timest2​at_{2a}are arbitrary subject tot21+t22=2​τ1=τ2t_{21}{+}t_{22}=2\tau_{1}=\tau_{2}. Conservation of action allows reparametrizing times into coordinates; henceω2=∑a=12dpa∧dxa,[xa,pb]=i​ℏ​δa​b.\omega_{2}=\sum_{a=1}^{2}\differential p_{a}\wedge\differential x_{a},\qquad[x_{a},p_{b}]=\mathrm{i}\hbar\,\delta_{ab}.(8)v0v_{0}vmv_{m}v1v_{1}e21e_{21}e22e_{22}𝒞​2:U​(1)\mathcal{C}2:\penalty 10000\ U(1),(xa,pa)(x_{a},p_{a})Figure 2:Layer𝒞​2\mathcal{C}2: edge splitting introduces canonical pairs and localU​(1)U(1)invariance.

The Hamilton–Jacobi actionS​[xa]=∫(E1​dt2−pa​dxa)S[x_{a}]=\int(E_{1}\,\differential t_{2}-p_{a}\differential x_{a})(9)

yields the metricd​s2=c2​dt22−δa​b​dxa​dxb,ds^{2}=c^{2}\differential t_{2}^{2}-\delta_{ab}\differential x^{a}\differential x^{b},(10)

i.e., an effective spacetime with signature(+−−)(+--).

SinceSmin(2)=2​ℏS^{(2)}_{\min}=2\hbar, common phase shiftsθ\thetaact asΦ\displaystyle\Phi↦Φ+θ,\displaystyle\mapsto\Phi+\theta,(11)E2\displaystyle E_{2}↦E2−q​A0,\displaystyle\mapsto E_{2}-qA_{0},\quad(12)pa\displaystyle p_{a}↦pa−q​Aa,\displaystyle\mapsto p_{a}-qA_{a},(13)(A0,Aa)\displaystyle(A_{0},A_{a})=∂(t2,xa)θ,\displaystyle=\partial_{(t_{2},x_{a})}\theta,(14)

realizing aU​(1)U(1)fiber over(t2,x1,x2)(t_{2},x_{1},x_{2}). On graphs this is the Peierls phase on edges. The(2+1)(2{+}1)action with gravity, Abelian gauge field, and matter isS2\displaystyle S_{\text{2}}=12​κ2​∫d3​x​|g|​R−14​∫d3​x​|g|​Fμ​ν​Fμ​ν\displaystyle=\frac{1}{2\kappa_{2}}\int d^{3}x\,\sqrt{|g|}\,R-\frac{1}{4}\int d^{3}x\,\sqrt{|g|}\,F_{\mu\nu}F^{\mu\nu}+∫d3​x​|g|​ℒmatter​(g,A,…),\displaystyle\quad+\int d^{3}x\,\sqrt{|g|}\,\mathcal{L}_{\text{matter}}(g,A,\ldots),(15)

withF=d​AF=dAand matter covariant derivativeDμ=∂μ+14​ωμI​J​γI​J−i​q​AμD_{\mu}=\partial_{\mu}+\frac{1}{4}\omega_{\mu}^{IJ}\gamma_{IJ}-iqA_{\mu}.

In phase-locked domains of𝒞​2\mathcal{C}2the bulk gravitational sector can be rewritten in Chern–Simons form. ForΛ=0\Lambda=0, the gauge field𝒜=ωI​JI+eI​PI∈𝔦​𝔰​𝔬​(2,1)\mathcal{A}=\omega^{I}J_{I}+e^{I}P_{I}\in\mathfrak{iso}(2,1)andSCS​[𝒜]=k4​π​∫tr​(𝒜∧d​𝒜+23​𝒜∧𝒜∧𝒜),S_{\text{CS}}[\mathcal{A}]=\frac{k}{4\pi}\int\!\text{tr}\!\left(\mathcal{A}\wedge d\mathcal{A}+\tfrac{2}{3}\mathcal{A}\wedge\mathcal{A}\wedge\mathcal{A}\right),(16)

impose flatness of𝒜\mathcal{A}, equivalent to vacuum Einstein equations in(2+1)(2{+}1). ForΛ≠0\Lambda\neq 0the group becomesSO​(2,2)\mathrm{SO}(2,2)orSO​(3,1)\mathrm{SO}(3,1); matter adds Wilson lines.

## VTransition𝒞​2→𝒞​3\mathcal{C}2\!\to\!\mathcal{C}3: triple closure andS​U​(3)SU(3)

At the next step each chain closes into a triple path(e31,e32,e33)(e_{31},e_{32},e_{33})withE31+E32+E33=E1E_{31}{+}E_{32}{+}E_{33}=E_{1}, Fig.3. Define(Aμ)a≡b1ℏ(paxa−pbxb)kμa.b(A_{\mu})^{a}{}_{b}\;\equiv\;\frac{1}{\hbar}\bigl(p_{a}x_{a}-p_{b}x_{b}\bigr)\,k_{\mu}^{\,a}{}_{b}.(17)

The commutator in the fundamental representation[Aμ,Aν]a=b(Aμ)ac(Aν)c−b(Aν)ac(Aμ)c,b\bigl[A_{\mu},A_{\nu}\bigr]^{a}{}_{b}\;=\;(A_{\mu})^{a}{}{c}\,(A\nu)^{c}{}_{b}\;-\;(A_{\nu})^{a}{}{c}\,(A\mu)^{c}{}_{b}\,,(18)

is traceless and closes on3×33\times 3trace-free matrices, realizing𝔰​𝔲​(3)\mathfrak{su}(3). Expanding in generatorsTcT^{c}:Aμ=Aμc​Tc,c=1,…,8,A_{\mu}\;=\;A_{\mu}^{c}\,T^{c}\,,\qquad c=1,\dots,8\,,(19)[Tc,Td]=i​fc​d​e​Te,tr​(Tc​Td)=12​δc​d.[T^{c},T^{d}]\;=\;if^{cde}\,T^{e},\qquad\mathrm{tr}\bigl(T^{c}T^{d}\bigr)\;=\;\frac{1}{2}\,\delta^{cd}\,.(20)

The maps between representations are(Aμ)a=bAμc(Tc)a,bAμc=2tr(TcAμ).(A_{\mu})^{a}{}_{b}\;=\;A_{\mu}^{c}\,(T^{c})^{a}{}_{b}\,,\qquad A_{\mu}^{c}\;=\;2\,\mathrm{tr}\!\left(T^{c}A_{\mu}\right).(21)

Hence[Aμ,Aν]=Aμc​Aνd​[Tc,Td]=i​fc​d​e​Aμc​Aνd​Te,[A_{\mu},A_{\nu}]\;=\;A_{\mu}^{c}A_{\nu}^{d}\,[T^{c},T^{d}]\;=\;if^{cde}A_{\mu}^{c}A_{\nu}^{d}\,T^{e}\,,(22)

and in the adjoint representation[Aμ,Aν]e=i​fe​c​d​Aμc​Aνd.\bigl[A_{\mu},A_{\nu}\bigr]^{e}\;=\;if^{ecd}\,A_{\mu}^{c}A_{\nu}^{d}\,.(23)

Introducing the standard field tensor and the action for𝒞​3\mathcal{C}3,Fμ​νa\displaystyle F^{a}_{\mu\nu}=∂μAνa−∂νAμa+g​fa​b​c​Aμb​Aνc,\displaystyle=\partial_{\mu}A^{a}_{\nu}-\partial_{\nu}A^{a}_{\mu}+gf^{abc}A^{b}_{\mu}A^{c}_{\nu},(24)S3\displaystyle S_{3}=∫d3x​|g|​[12​κ3​R−14​Fμ​νa​Fa​μ​ν],\displaystyle=\!\int\!\differential^{3}x\,\sqrt{\absolutevalue{g}}\!\left[\frac{1}{2\kappa_{3}}R-\frac{1}{4}F^{a}_{\mu\nu}F^{a\mu\nu}\right],(25)

one obtains the Einstein–Yang–Mills equations. The rotational generators satisfy[Li,Lj]=i​ℏ​fi​j​Lkk[L_{i},L_{j}]=\mathrm{i}\hbar f_{ij}{}^{k}L_{k}withJi=Li+SiJ_{i}=L_{i}+S_{i}.v0v_{0}vm​1v_{m1}vm​2v_{m2}v1v_{1}e31e_{31}e32e_{32}e33e_{33}𝒞​3:S​U​(3)\mathcal{C}3:\penalty 10000\ SU(3)Figure 3:Layer𝒞​3\mathcal{C}3: a triple closure yieldsS​U​(3)SU(3)-type connections.

## VIFourth Layer𝒞​4\mathcal{C}4: dimensional reduction and gauge consistency

The fourth layer hasτ4=4​τ1=2​τ2\tau_{4}=4\tau_{1}=2\tau_{2}and can be viewed as4×𝒞​14\times\mathcal{C}1or2×𝒞​22\times\mathcal{C}2. At energies below the layer scale these descriptions agree:𝒞​4\mathcal{C}4is the minimal structure with coexisting pair locking.

Four internal times(t41,t42,t43,t44)(t_{41},t_{42},t_{43},t_{44})form the pairs(1,3)(1,3)and(2,4)(2,4). Strong intra-pair couplingκ2\kappa_{2}locks phases within each pair, while weaker inter-pair couplingδ\deltaacts across pairs. Introducing mean coordinatesX1=12​(x1+x3),X2=12​(x2+x4),X_{1}=\tfrac{1}{2}(x_{1}+x_{3}),\qquad X_{2}=\tfrac{1}{2}(x_{2}+x_{4}),(26)

and integrating out heavy relative modes gives an effective metricd​seff2=c2​d​τ2−Gi​j​(X)​d​Xi​d​Xj,i,j=1,2,ds_{\mathrm{eff}}^{2}=c^{2}d\tau^{2}-G_{ij}(X)\,dX^{i}dX^{j},\quad i,j=1,2,(27)

so the infrared behavior of𝒞​4\mathcal{C}4is that of a(2+1)(2{+}1)sheet.

Pair locking yieldsU​(1)​(13)(+)×U​(1)​(24)(+)U(1){(13)}^{(+)}\times U(1){(24)}^{(+)},
and the weaker cross-pair coupling identifies the diagonal combination,U​(1)​(13)(+)×U​(1)​(24)(+)→U​(1)diag,\displaystyle U(1){(13)}^{(+)}\times U(1){(24)}^{(+)}\rightarrow U(1)_{\mathrm{diag}},(28)Aμdiag=14​∑a=14Aμ(a).\displaystyle A_{\mu}^{\mathrm{diag}}=\tfrac{1}{4}\sum_{a=1}^{4}A_{\mu}^{(a)}.(29)

All orthogonal combinations become massive; the surviving massless photon is identical to theU​(1)U(1)of𝒞​2\mathcal{C}2. Charge quantization and theℤ2\mathbb{Z}_{2}structure are preserved. At UV scales𝒞​4\mathcal{C}4behaves as a(4+1)(4{+}1)system; belowκ2\kappa_{2}it reduces to two𝒞​2\mathcal{C}2-like doublets; belowδ\deltaonly the diagonalU​(1)U(1)remains.

## VIIConclusion

The discrete-action axiomS1=ℏS_{1}=\hbarand the oriented-graph growth rule suffice to build a hierarchy of layers𝒞​N\mathcal{C}N. Each transition𝒞​N→𝒞​N+1\mathcal{C}N\!\to\!\mathcal{C}{N+1}adds canonical pairs and strengthens symmetry:𝒞​2\mathcal{C}2exhibits localU​(1)U(1)and a(+−−)(+--)metric,𝒞​3\mathcal{C}3yieldsS​U​(3)SU(3)and the Einstein–Yang–Mills action, and𝒞​4\mathcal{C}4ensures gauge consistency with dimensional reduction in the infrared. Stochastic graph growth naturally leads to decoherence and symmetry-breaking mechanisms.

## Appendix A: Formal derivations

## .1Variation of a discrete action

Each elementary edgeeie_{i}carriesδ​Si=ℏ\delta S_{i}=\hbar. With fixedJzJ_{z}, the variation ofSN=N​ℏS_{N}=N\hbargivesδ​SN=∑i(pi​δ​xi−Ei​δ​ti)=0,\delta S_{N}=\sum_{i}(p_{i}\,\delta x_{i}-E_{i}\,\delta t_{i})=0,(30)

from which the symplectic formω=∑idpi∧dxi\omega=\sum_{i}\differential p_{i}\wedge\differential x_{i}follows.

## .2Emergence of canonical pairs

At𝒞​2\mathcal{C}2, splittinge1e_{1}doubles the action to2​ℏ2\hbar. WithE21+E22=E1E_{21}{+}E_{22}=E_{1}andpa=E2​a/cp_{a}=E_{2a}/cwe obtain[xa,pb]=i​ℏ​δa​b[x_{a},p_{b}]=\mathrm{i}\hbar\,\delta_{ab}—the minimal discrete analogue of phase space.

## .3Derivation of theS​U​(3)SU(3)structure

At𝒞​3\mathcal{C}3, with phasesϕa\phi_{a}, the closure conditionϕ12+ϕ23+ϕ31=0\phi_{12}+\phi_{23}+\phi_{31}=0(31)

yields three independent differences forming𝔰​𝔲​(3)\mathfrak{su}(3):[Ta,Tb]=i​fa​b​c​Tc.[T_{a},T_{b}]=\mathrm{i}f^{abc}T_{c}.Mappingϕa​b→Aμ(a​b)​Ta​b\phi_{ab}\!\to\!A_{\mu}^{(ab)}T_{ab}leads to the curvatureF=dA+g​A∧A.F=\differential A+gA\wedge A.

## References
- [1]I. Newton, Philosophiae Naturalis Principia Mathematica (London, 1687).
- [2]E. Schrödinger, Quantisierung als Eigenwertproblem, Ann. Phys.79, 361 (1926).
- [3]A. Einstein, Die Feldgleichungen der Gravitation, Preuss. Akad. Wiss. Berlin, Sitzungsberichte, 844 (1915).
- [4]M. Planck, Über das Gesetz der Energieverteilung im Normalspectrum, Ann. Phys.4, 553 (1901).
- [5]L. Mandelstam and I. Tamm, The uncertainty relation between energy and time, J. Phys. (USSR)9, 249 (1945).
- [6]S. Deffner and S. Campbell, Quantum speed limits: from Heisenberg’s uncertainty principle to optimal quantum control, J. Phys. A50, 453001 (2017).
- [7]V. Giovannetti, S. Lloyd, and L. Maccone, Quantum limits to dynamical evolution, Phys. Rev. A67, 052109 (2003).
- [8]H. S. Snyder, Quantized space-time, Phys. Rev.71, 38 (1947).
- [9]P. Caldirola, The introduction of a fundamental time interval (chronon) in quantum theory, Nuovo Cimento3, 297 (1956).
- [10]L. Bombelli, J. Lee, D. Meyer, and R. D. Sorkin, Space-time as a causal set, Phys. Rev. Lett.59, 521 (1987).
- [11]F. Dowker, Causal sets and the deep structure of spacetime, in 100 Years of Relativity, World Scientific (2005).
- [12]R. D. Sorkin, Causal set hypothesis, Gen. Rel. Grav.39, 1731 (2007).
- [13]A. Ashtekar and J. Lewandowski, Background independent quantum gravity: A status report, Class. Quant. Grav.21, R53 (2004).
- [14]C. Rovelli and L. Smolin, Discreteness of area and volume in quantum gravity, Nucl. Phys. B442, 593 (1995).
- [15]J. Ambjørn, A. Görlich, J. Jurkiewicz, and R. Loll, Nonperturbative quantum gravity, Phys. Rep.519, 127 (2012).
- [16]T. Regge, General relativity without coordinates, Nuovo Cimento19, 558 (1961).
- [17]A. Connes, Noncommutative Geometry (Academic Press, 1994).
- [18]D. Oriti, The microscopic dynamics of quantum space as a group field theory, in Foundations of Space and Time, Cambridge Univ. Press (2012).
- [19]K. G. Wilson, Confinement of quarks, Phys. Rev. D10, 2445 (1974).
- [20]S. E. Venegas-Andraca, Quantum walks: a comprehensive review, Quantum Inf. Process.11, 1015 (2012).
- [21]B. Schumacher and R. Werner, Reversible quantum cellular automata, arXiv:quant-ph/0405174.
- [22]G. ’t Hooft, The Cellular Automaton Interpretation of Quantum Mechanics (Springer, 2016).
- [23]D. N. Page and W. K. Wootters, Evolution without evolution: Dynamics described by stationary observables, Phys. Rev. D27, 2885 (1983).
- [24]A. Connes and C. Rovelli, Von Neumann algebra automorphisms and time-thermodynamics relation, Class. Quant. Grav.11, 2899 (1994).
- [25]A. Ashtekar, S. Fairhurst, and J. L. Willis, Quantum gravity, shadow states, and quantum mechanics, Class. Quant. Grav.20, 1031 (2003).
- [26]G. Amelino-Camelia, Relativity in space-times with short-distance structure governed by an observer-independent (Planckian) length scale, Int. J. Mod. Phys. D11, 35 (2002).
- [27]D. Mattingly, Modern tests of Lorentz invariance, Living Rev. Relativ.8, 5 (2005).
- [28]S. Hossenfelder, Minimal length scale scenarios for quantum gravity, Living Rev. Relativ.16, 2 (2013).
- [29]G. Amelino-Camelia, J. Ellis, N. Mavromatos, D. Nanopoulos, and S. Sarkar, Tests of quantum gravity from observations of gamma-ray bursts, Nature393, 763 (1998).
- [30]J. M. Sanz-Serna and M. Calvo, Numerical Hamiltonian Problems (Chapman and Hall, 1994).
- [31]C. Rovelli,Quantum Gravity, Cambridge Univ. Press (2004).
- [32]M. Marcolli,Quantum Statistical Models on Graphs, arXiv:2205.12345 (2022).
