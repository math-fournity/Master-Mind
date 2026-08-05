# Continuous Game of Life: cell emergence and self-organization at the edge of growth

**arXiv ID**: 2607.27402v1
**Authors**: Alexandre Guillet, Frank Jülicher
**Published**: 2026-07-29
**Categories**: physics.bio-ph, nlin.AO, nlin.PS
**Comments**: Code is available at: https://codeberg.org/A-Guillet/cGoL To be published in Artificial Life 26 pages, 7 figures
**HTML URL**: https://arxiv.org/html/2607.27402v1

## Abstract

Conway's Game of Life shows that simple rules can generate a rich diversity of emerging structures. This cellular automaton has been translated to continuous space by Rafler (2011) in a simulation called SmoothLife. The isotropic rule of this continuous Game of Life generates patterns whose beauty has attracted the attention of a growing community at the intersection of science and computer art. We study a minimal variant of this model, continuous in space and time, that generates cell-like patterns capable of self-replicating, gliding and disappearing. The phenomenology of these unit patterns is reported and related to homogeneous-state bifurcations, symmetry breaking, observed shape instabilities, finite-amplitude morphological changes, and a dilute-to-dense transition associated with cell proliferation. Its mapping onto a large reaction--diffusion system is interpreted in terms of homeostatic concentrations of morphogens, regulated by the nonlinear survival rule and generated through a cell-sourced cascade of auxiliary reactions. Introducing a global conservation law that limits resource availability causes the system to self-organize at this dilute-to-dense transition, which we call the edge of growth. A further exploration of parameter space reveals a variety of phases and the richness of life-like morphologies organized around this edge. Resemblance to biological processes such as division, motility, and death, together with a concise formulation and numerical implementation, makes the continuous Game of Life an appealing model system for investigating the emergence and self-organization of life-like patterns.

## Full Text

Continuous Game of Life: cell emergence and self-organization at the edge of growth

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
- License: CC BY 4.0arXiv:2607.27402v1 [physics.bio-ph] 29 Jul 2026

## Continuous Game of Life:
cell emergence and self-organization at the edge of growth

## keywords:continuous Game of Life, cellular automata, morphogenesis, self-organization, reaction–diffusion, phase transition

[
BoldFont = AtkinsonHyperlegible-Bold.ttf,
ItalicFont = AtkinsonHyperlegible-Italic.ttf,
BoldItalicFont = AtkinsonHyperlegible-BoldItalic.ttf]\authAlexandre Guillet ,
Frank Jülicher\correspondingAlexandre Guilletaguillet@ik.me\affiliationsMax Planck Institute for the Physics of Complex Systems, Dresden, Germany\coverpage

## 1Introduction

## Review

Since its inception in 1970, the cellular automatonGame of Life(GoL) defined by Conway[12], famous for its complexity arising from simple rules on the 2-dimensional grid, has fostered a strong interest and numerous developments.
After pioneering efforts in porting the GoL to continuous space[18], in particular its glider pattern via a scaling limit of large (inner and outer) discrete neighbourhoods[10,11,21], the quest for more realistic Life-like automata has slowly faded from academia.

In contrast, the exploration of theGame of Lifebecame active in
online communities of enthusiasts111Seeconwaylife.comand the Golly software.supported by the popularization of computers. This activity has produced increasingly complex structures within the original GoL rules, such as aprogrammable computerand ameta-pixelcapable of emulating other cellular automata, illustrating its Turing-completeness[26].
Despite extensive efforts, no finiteself-replicating machinehas been found in the GoL.

The continued interest in the GoL and its variants has resulted in the first successful implementation of a space-continuous isotropic rule, calledSmoothLife[23], based on disk and annulus-shaped integration domains in place of neighbour counting regions.
Simulations of gliders with better continuity in time have quickly followed, based on the explicit Euler method modified with a clamp regularization[24,15].
This breakthrough has laid the foundation for a renewed exploration of Life-like continuous systems inspired by cellular automata but freed from discrete states and the 4-fold symmetry of the grid. We call themcontinuous Games of Life(cGoL).

AmongSmoothLifevariations, several conceptual simplifications were introduced while maintaining a rich phenomenology.
Most relevant for this article, the little-knownSmootherLiferefinement from CornusAmmonis (2015) unifies the inner and outer integrals as convolutions with respect to a small kernel and a large kernel with the same Gaussian shape[8,15].
This model generates clear self-replicating unit patterns made of a nucleus and a shell that resemble dividing (and sometimes dying) biological cells. This striking observation has motivated our investigation.

Another variation consists in reducing the nonlinearity of the GoL’s survival rule, from its original bivariate form to a univariate function of the convolution integral. CalledLenia, this simplification comes at the price of a more sophisticated shape for the unique isotropic convolution kernel[6]. The resulting simulation can generate single gliders (or oscillators) with surprisingly diverse morphologies, leading to the proposal of a naturalistic classification for artificial lifeforms. This exploration is pursued in[7], where the extendedLeniamodel returns to a multivariate survival function (restricted to a sum of univariate ones), along with other higher-dimensional extensions.

TheLeniamodel has generated a strong interest, uncovering certain caveats and fostering developments. In spite of the small time steps, discreteness in time still plays an important role in the stability of the patterns:Lenia’s gliders tend to be destabilized and vanish in the continuous-time limit[9,17]. When reformulating theLeniamodel without the clamp regularization step, gliders can still be found in the continuous-time limit although with differing morphologies[16]. The mathematical implications of these two modelling approaches are discussed in[5];[28]analyse continuous-time formulations with dynamical-systems tools including symmetries, Lyapunov spectra, covariant Lyapunov vectors, and attractor dimensions.
The resulting integro-differential equation can be interpreted in terms of a particular reaction–diffusion system[17]: the slow field reacts to a combination of many fast-diffusing and -decaying species that it generates.

Furthermore,Lenia’s gliders are metastable local structures, coexisting with stable global solutions: they easily vanish or explode into a space-filling pattern upon interaction. In order to address this issue, an environmental feedback from resource rarefaction has been introduced in[27].
Finally, a family of models enforcing a strict local conservation law on extendedLeniahas been introduced:Flow-Lenia[22]proposes a complete reformulation in terms of fluxes, andMaCELenia[20]refines it into a compact continuity equation.

In this article, we combine these modelling approaches into a continuous and minimal formulation of theGame of Lifethat produces clear self-replicating and motile elementary patterns.

## Roadmap

We first introduce the cGoL model, moving from a general formulation of the dynamics to a parsimonious parametrization with 6 + 1 parameters. In two dimensions, a fine-tuned reference choice generates cell-like patterns that divide, glide and oscillate, or disappear, while nearby parameter values reveal a broader diversity of behaviours and morphologies. This phenomenology is charted empirically, from the homogeneous states and their saddle-node structure, through observed symmetry breaking, shape instabilities and finite-amplitude morphological transitions, occurring in the vicinity of a collective dilute-to-dense phase transition.

We then cast the same equations in reaction–diffusion terms: auxiliary fields become fast-relaxed morphogen concentrations, held within homeostatic ranges set by the nonlinear survival rule, while the Gaussian shape of the kernels emerges from an underlying cascade of auxiliary reactions. We next introduce a global conservation law for a finite resource, consumed by growth and released by decay, and show that it follows from a local mass-conserving dynamics in the well-mixed limit. Given a sufficient volume, the resulting resource feedback drives a system initialized in the dense phase to self-organize at the edge of growth, the boundary with the dilute phase. Finally, scanning a targeted slice of parameter space maps the phase structure around this edge, where morphologies are richest and most life-like. The article concludes with a discussion of dynamical-systems perspectives, self-organization and criticality, and questions of dimensionality and evolution.

## 2Definition of a continuous Game of Life

The cGoL transposes the GoL into the continuum: neighbour counts become spatial convolutions, and the binary update table becomes a smooth target function. We first state the general dynamics, then specialize to the parametrization used throughout this article.

## 2.1General dynamics

LetL​(𝐱,t)L(\mathbf{x},t)be the “Life”
field of acontinuous Game of Life(cGoL), in Euclidean space𝐱∈ℝd\mathbf{x}\in\mathbb{R}^{d}and timet>0t>0, taking scalar values inℝ\mathbb{R}.
The continuous dynamics is determined by a nonlinear partial integro-differential equation of the form∂tL\displaystyle\partial_{t}L=Γ​({Φk∗L})−L\displaystyle=\Gamma(\{\Phi_{k}\ast L\})-L(1)Φk∗L​(𝐱,t)\displaystyle\Phi_{k}\ast L(\mathbf{x},t)=∫Φk​(𝐱−𝐲)​L​(𝐲,t)​d𝐲.\displaystyle=\int\Phi_{k}(\mathbf{x}-\mathbf{y})L(\mathbf{y},t)\,\mathrm{d}\mathbf{y}\quad.(2)

Here,Γ\Gammais a nonlinear function of multiple variables indexed byk=1,2,…k=1,2,\dots, extending the univariate (continuous-timeLenia) case formulated in[16].
The variablesΦk∗L\Phi_{k}\ast Lare auxiliary fields: smoothed versions ofLLthat represent neighbourhood population states.
The convolution integral Eq. (2) is the continuous analogue of neighbour counting: it locally averagesLLaround any spatial coordinate𝐱\mathbf{x}.

Convolution kernelsΦk\Phi_{k}correspond to different types of neighbourhood, typically a small one (k=1k=1) and a large one (k=2k=2) about 3 times wider. Isotropic kernels,Φk​(𝐱)=Φk​(|𝐱|)\Phi_{k}(\mathbf{x})=\Phi_{k}(|\mathbf{x}|), are a natural choice to restore the symmetry lacking in the discrete model. A constant kernel amounts to a simple integration, and will be introduced through a global conservation law (k=3k=3).

The fieldΓ​({Φk∗L})\Gamma(\{\Phi_{k}\ast L\}), evaluated from neighbourhood states at each point in space, is called thetarget. It can change as the primary fieldLLrelaxes locally towards it, with the relaxation timescale taken as the time unit in Eq. (1). Defining the target field of thecontinuous Game of Lifeamounts to specifying the discrete rule in the originalGame of Life.Figure 1:Primary and auxiliary fields:LL,M=Φ1∗LM=\Phi_{1}\ast LandN=Φ2∗LN=\Phi_{2}\ast L(top, from left to right). Target functionΓ\Gamma(bottom left, same grey scale as forL,M,NL,M,N). Special homogeneous states are marked in red: post-bifurcation unstable and stable (empty and full triangles) steady states, and pre-bifurcation non-steady optimum (empty circle). Spatial distribution of pairs(M,N)(M,N), whereΓ\Gammagets evaluated (bottom centre, pixel count). Growth or decay rate of the fieldLL, Eq. (1) (bottom right).

## 2.2Specific rule

In this article, we remain close to the original rule of theGame of Lifein two ways: by starting with a bivariate target function (survival rule), as inSmoothLife, and by using the same shape for the corresponding convolution kernels (neighbourhoods) as inSmootherLife. By adapting those precursor models to the dynamics Eq. (1), we complete the continuous formulation of the GoL.

Instead of discrete squares (of widths 1 and 3), the Gaussian shape describes neighbourhoods as isotropic and smooth kernels:Φ1​(𝐱)\displaystyle\Phi_{1}(\mathbf{x})=e−π​|𝐱|2,\displaystyle=e^{-\pi|\mathbf{x}|^{2}}\quad,\qquadM=Φ1∗L\displaystyle M=\Phi_{1}\ast L(3)Φ2​(𝐱)\displaystyle\Phi_{2}(\mathbf{x})=λ−d​Φ1​(𝐱/λ),\displaystyle=\lambda^{-d}\Phi_{1}(\mathbf{x}/\lambda)\quad,\qquadN=Φ2∗L.\displaystyle\,N=\Phi_{2}\ast L\quad.

The two auxiliary fieldsMMandNNare thus Gaussian blurs of the primary field, averaging it at a small and a large neighbourhood scale, respectively, as illustrated in Fig.1(top). They play the role of continuous inner and outer neighbour counts, while the target functionΓ​(M,N)\Gamma(M,N)specifies which combinations of these counts favour growth. We use the small scale as the unit length and set the large-to-small scale ratio to its original valueλ=3\lambda=3.
A reaction–diffusion interpretation is discussed in Section4.

By evaluating the target functionΓ\Gammafor pairs of values(M,N)(M,N)at every spatial coordinate, one obtains the target fieldΓ​(M,N)\Gamma(M,N)that drives the dynamics Eq. (1) of the primary fieldLL, as illustrated in Fig.1(bottom).
The target is chosen to take values in[0,1][0,\,1], so that this interval is absorbing forLL: values initialized or perturbed outside it relax towards it.
The functionΓ\Gamma, replacing the Boolean update table of the GoL, specifies which large-neighbourhood populationsNNfavour growth; the centreNc​(M)N_{c}(M)and widthδ​Nc​(M)\delta N_{c}(M)of this survival range are modulated by the small-neighbourhood populationMM.
Building upon previous definitions that parametrize the kink of the discrete rule, we retain the form represented in Figs.1and2,Γ​(M,N)\displaystyle\Gamma(M,N)=S′​(N−Nc​(M)δ​Nc​(M))\displaystyle=S^{\prime}(\tfrac{N-N_{c}(M)}{\delta N_{c}(M)})(4)Nc​(M)\displaystyle N_{c}(M)=N0+(N1−N0)S(M−Mcδ​Mc),S(m)=(1+e−4​m)−1\displaystyle=N_{0}+(N_{1}-N_{0})S(\tfrac{M-M_{\text{c}}}{\delta M_{\text{c}}})\quad,\qquad S(m)=(1+e^{-4m})^{-1}(5)δ​Nc​(M)\displaystyle\delta N_{c}(M)=δ​N0+(δ​N1−δ​N0)​S​(M−Mcδ​Mc),\displaystyle=\delta N_{0}+(\delta N_{1}-\delta N_{0})S(\tfrac{M-M_{\text{c}}}{\delta M_{\text{c}}})\quad,

where the derivativeS′S^{\prime}of the sigmoid is a bell shape:S′​(n)=4​S​(n)​(1−S​(n))=sech​(2​n)2S^{\prime}(n)=4S(n)(1-S(n))=\text{sech}(2n)^{2}. The target parameters are specific values of the auxiliary fieldsMMandNNdenoted with an index, see Eq. (7). This definition of the survival range effectively diminishes parametric degrees of freedom by one as compared to[23,8]. The locality of the growth region appears crucial; other fast-decaying bell shapes such as the Gaussian function yield comparable results.

The equivalent formΓ(M,N)=S′(n0+(n1−n0)S(m~)),(m~,n0,n1)=(M−M~cδ​Mc,N−N0δ​N0,N−N1δ​N1)\Gamma(M,N)=S^{\prime}(n_{0}+(n_{1}-n_{0})S(\tilde{m}))\quad,\qquad(\tilde{m},n_{0},n_{1})=(\tfrac{M-\tilde{M}_{\text{c}}}{\delta M_{\text{c}}},\tfrac{N-N_{0}}{\delta N_{0}},\tfrac{N-N_{1}}{\delta N_{1}})(6)

arises from properties of the sigmoid functionSSdefined in Eq. (5). Note that the first parameter differs from the corresponding one in Eq. (4):M~c=Mc−δ​Mc4​log⁡δ​N1δ​N0\tilde{M}_{\text{c}}=M_{\text{c}}-\tfrac{\delta M_{\text{c}}}{4}\log\tfrac{\delta N_{1}}{\delta N_{0}}.

The rule of the Game is fully specified by the shapesΓ\Gamma(based on the sigmoidSS) andΦ\Phi(Gaussian), and their parameters(Mc,δ​Mc,N0,δ​N0,N1,δ​N1)(M_{\text{c}},\delta M_{\text{c}},N_{0},\delta N_{0},N_{1},\delta N_{1})andλ\lambda. Given these parametrizations of the target function and kernels, the parameter space thus has 6 + 1 dimensions (to which one can add the dimensionality of spacedd).
In this article, the reference system uses Eqs. (4–5) in space withd=2d=2dimensions, original scalingλ=3\lambda=3, and target parameters𝐩=(Mc,δ​Mc,N0,δ​N0,N1,δ​N1)=(0.50,0.10,0.23,0.015,0.35,0.26).\mathbf{p}=(M_{\text{c}},\;\,\delta M_{\text{c}},\;\,N_{0},\;\,\delta N_{0},\;\,N_{1},\;\,\delta N_{1})=(0.50,\,0.10,\,0.23,\,0.015,\,0.35,\,0.26)\quad.(7)

These parameters have been fine-tuned (and rounded to the closest values with two significant digits),
so that the elementary localized state can divide several times, glide while oscillating, and disappear.
Because of this evocative phenomenology, illustrated in Fig.2and detailed in the next section, we will refer to this emergent unit pattern as a cell.

## 3Emergence of cell-like patterns

We now turn from the rule itself to the structures it generates. Near the reference parameters Eq. (7), localized states emerge as coherent units with a nucleus and a shell, able to divide, move, oscillate, or disappear depending on their symmetry, perturbations and interactions. We first examine the homogeneous states, which anchor this phenomenology, before describing the resulting morphologies and shape transitions, which eventually hint at the proximity of a collective dilute-to-dense phase transition.

## 3.1Homogeneous states and bifurcations

Some aspects of this system can be discussed from the scalar cased=0d=0, which corresponds to homogeneous solutions ford>0d>0. In this case, the convolution kernel is just a coefficient, equal to one since normalized in Eq. (2):L=M=NL=M=N.
Near the reference parameters Eq. (7), the system has three homogeneous steady states (fixed points), marked with triangles in Fig.1.
These solutions of the equationΓ​(L∗,L∗)=L∗\Gamma(L_{\ast},L_{\ast})=L_{\ast}are practically indistinguishable from the solutions ofS′​(L∗−N0δ​N0)=L∗S^{\prime}(\tfrac{L_{\ast}-N_{0}}{\delta N_{0}})=L_{\ast}as they occur in the lower region of the target before the transition (N0<Mc−2​δ​McN_{0}<M_{\text{c}}-2\delta M_{\text{c}}).

Since the survival range in this region is very thin,δ​N0≪N0\delta N_{0}\ll N_{0}, the lowest (empty) homogeneous steady state is practically vanishing, and it is stable (Game over). The two other ones lie in the vicinity ofN0±δ​N0N_{0}\pm\delta N_{0}, hence they are very close to one another and related to the shell of the cell pattern. This pair of unstable and stable fixed points may be understood as reflecting the proximity of a saddle-node bifurcation.
An empty state with exact zero value, or a crossing of the bifurcation would both require a reparametrization ofΓ\Gamma. The two stable homogeneous states are especially relevant and denotedL∗±L_{\ast}^{\pm}.

For widely different target parameters, another saddle-node bifurcation can occur. The local maximum ofΓ​(L,L)−L\Gamma(L,L)-Lcorresponds to the non-steady homogeneous state closest to the bifurcation. This special value, marked with a circle in Fig.1, depends on the four other parameters,Mc,δ​Mc,N1,δ​N1M_{\text{c}},\delta M_{\text{c}},N_{1},\delta N_{1}, and relates to the nucleus of the cell pattern.

The parrot-shaped distribution of joint values(M,N)(M,N)shown in Fig.1(bottom centre), which corresponds to an inhomogeneous non-steady stateLL, has visible traces of these special values as cusps and a recess near their location.

The rich morphogenesis generated by this nonlinear system suggests many further transitions between localized states, which lie well beyond the homogeneous-state analysis above. We therefore investigate these phenomena empirically.Figure 2:Cell dynamics at and near reference parameters Eq. (7), with colour coding of corresponding regions of the target functionΓ\Gamma(A) and the fieldLL(B–E). Reference behaviours: dividing cell (B) or oscillating glider (C), depending on its symmetry axes (left). Time advances from left to right in steps of 10 (B) and 6 (C) time units. (D–E) Variants: (steady) isotropic egg (D) and (clockwise) turning glider (E) forN1N_{1}respectively increased and decreased by0.030.03.

## 3.2Morphological diversity and transitions

Near the reference parameters Eq. (7), thecontinuous Game of Lifehas a diversity of steady and non-steady localized states, all variants of a recognizable elementary pattern.
Activated regionsLLform a nucleus and a shell, which correspond respectively to the broad and narrow parts of the survival region in the target functionΓ\Gamma, for high and lowMM. This correspondence is colour-coded in Fig.2. The inner and outer empty areas correspond to the regions to the right and to the left of the survival range respectively.
By analogy with biology, we call this unit pattern acell, due to its self-replication, motility and disappearance.

In unfavourable regions of the parameter space where the unit pattern can still be initialized222We use the seedL​(0,𝐱)=e−π​𝐱T​Σ−1​𝐱L(0,\mathbf{x})=e^{-\pi\mathbf{x}^{T}\Sigma^{-1}\mathbf{x}}with a slight elongation to facilitate the first division by breaking isotropy., the cell remains in the form of a dormantegg, an isotropic localized steady state shown in Fig.2(D), or may die (vanish). Bistability can already be observed, with two possible radii of the egg at certain parameter values.

For more favourable parameters, the egg grows and can undergo various shape instabilities, triggered by environmental perturbations (such as interaction with neighbour cell patterns).
The first observed symmetry breaking polarizes the egg, defining long and short symmetry axes.
The elongation of the cell can lead to itsdivision, while keeping its two symmetry axes (see Fig.2B).
Some parameters lead tofailed division, in which case the cells die shortly after the division of the nucleus. If isotropy is not broken, the egg may grow into abubble.

The short symmetry axis can turn unstable, leading to a second symmetry breaking. The result is aglider: a bilateral cell morphology associated with motion. The glider can have a variety of behaviours and shape instabilities.
In the reference case illustrated in Fig.2(B, C), the short axis is metastable, so that dividing cells can be destabilized into a glider. Conversely, interacting gliders can stop and divide.
These switches are changes of dynamical regime triggered by interactions, rather than linear instabilities of an isolated pattern.
This glider is notable for its shapeoscillationsduring motion.
When amplified, this oscillation leads back to cell division, with intermediate cases for which division fails asymmetrically. For other parameters, oscillations can be damped and result in a glider with a steady shape.

A further symmetry breaking of the long axis typically yields a clockwise or anti-clockwiseturning glider, shown in Fig.2(E), with various radii for its circular trajectory. Atripod, steady cell with order 3 symmetry, can also be found, and observed to switch its morphology to different gliders upon perturbation.

The shape instability of an elongating cell may also be absent or insufficient to produce a successful division. This situation yields various extended patterns.
If the division of the nucleus is not followed by the scission of the shell, an intermediary body can be formed in the centre, which may turn into a full nucleus. Otherwise, the formation of segmentedchainsor non-segmentedfilamentsis initiated and can percolate. A nucleus that elongates but has difficulty dividing leads to asnake, with growing or shrinking ends. An ever-growing snake can fill space and generate various mazes and Turing patterns.

The phenomenology near the reference parameters is unexpectedly diverse, in spite of the simple morphology of the cell-like pattern compared with manyLeniagliders.
Taken together, these observations suggest that the reference cell is poised among several long-lived localized morphologies, connected by symmetry breaking, shape instabilities, and finite-amplitude transitions.

## 3.3Dynamical phase transition

The localized transitions described above motivate a broader question: how close are the reference parameters to a collective transition?
To make this question tractable in the 6-dimensional target-parameter space, we first probe a single control direction, then visualize selected additional directions through spatial parameter gradients.

Consider the scaling of the target functionr​Γr\Gammawith a constant coefficientrr(close to 1):r>1r>1enhances the growth rate whereasr<1r<1reduces it, according to Eq. (1). As a result, the fieldLLtakes values in the interval[0,r][0,\,r].
Since the scaling coefficientrris constant, this modulation of growth amounts to scaling all auxiliary fields, by redefiningLLon[0,1][0,\,1].
In turn, this is equivalent to rescaling all target parameters, given the parametrization Eq. (4) ofΓ\Gamma. One obtains a simple interpretation of a perturbation along a particular direction of the parameter space:r​Γ​(M,N;𝐩)∼Γ​(r​M,r​N;𝐩)=Γ​(M,N;𝐩/r)r\Gamma(M,N;\mathbf{p})\sim\Gamma(rM,rN;\mathbf{p})=\Gamma(M,N;\mathbf{p}/r)(8)

where∼\simdenotes the equivalence of the resulting dynamics up to a rescaling ofLL.
As expected, the scaling𝐩/r\mathbf{p}/rof Eq. (7) promotes growth forr>1r>1and inhibits it forr<1r<1, interpolating between two coarse phases, dense or dilute, through many of the morphologies described above.Figure 3:Dynamic states of the cGoL model in the presence of a spatial variation of the target parameters𝐩=𝐩​(𝐱)\mathbf{p}=\mathbf{p}(\mathbf{x}). For each panel, a subset of the parameters (specified on the left) is increased linearly from left to right around its reference value Eq. (7) (centre). The top panel corresponds to Eq. (8) with a position-dependent scalingr=r​(𝐱)r=r(\mathbf{x})(top axis).

We further attempt to visualize the role of individual target parameters or subsets of them on the morphogenesis by simulating the cGoL with spatial parameter scans𝐩=𝐩​(𝐱)\mathbf{p}=\mathbf{p}(\mathbf{x})along the horizontal direction. The resulting overview Fig.3maps adjacent patterns, such as mazes, filaments and homogeneous states, around the reference cell and reveals the sensitivity of the tuning with respect to the different target parameters.

In the top panel of Fig.3, one can observe that the scaling Eq. (8) of all target parameters is dominated by the effect of scaling the auxiliary fieldMM, in particular the first target parameterMc=12M_{\text{c}}=\tfrac{1}{2}. The isotropic egg and turning glider variants from Fig.2(D, E), with values ofN1N_{1}differing by nearly±9%\pm 9\%, can be located on the map Fig.3in the second panel from the bottom. We note the propensity of this turning glider to assemble in chains.

These spatial scans suggest that the reference cell morphology has been selected close to a dynamical transition, but the evidence remains qualitative and restricted toλ=3\lambda=3.
Phase boundaries between dynamical regimes have likewise been identified in the parameter space ofLenia-like systems[19,29,14].
After the reaction–diffusion reinterpretation of the next section, we return to this transition quantitatively: resource feedback identifies a transition valuer∗r_{\ast}forλ=3\lambda=3, and a scan usingrrandλ\lambdaas control parameters, with mean density as order parameter, maps the surrounding phase structure.

## 4Reaction–diffusion interpretation

The nucleus and shell of the cell-like pattern occupy distinct regions of the target function, itself evaluated from the auxiliary fieldsMMandNN. We now reinterpret the same equations as a coarse-grained reaction–diffusion system, in which the slow, non-diffusing fieldLLresponds to fast-relaxed morphogen concentrations. This nonlinear reaction specifies the homeostatic morphogen ranges maintained within the cell. The Gaussian kernel shape further arises from a cascade of auxiliary reactions.

## 4.1Morphogen concentrations at homeostasis

As shown in[17]for continuous-timeLenia, cGoL equations of the form Eq. (1) can be mapped to the asymptotic regime of a reaction–diffusion systemτk​∂tCk=σk2​∇2Ck+fk​({Cj})\tau_{k}\partial_{t}C_{k}=\sigma_{k}^{2}\nabla^{2}C_{k}+f_{k}(\{C_{j}\})(9)

in which the primary fieldC0=LC_{0}=Ldoes not diffuse,σ0=0\sigma_{0}=0, and multiple auxiliary concentration fieldsCkC_{k}diffuse and react much faster,τk≪τ0\tau_{k}\ll\tau_{0}fork≥1k\geq 1.
The selected chemical species to whichLLreacts are calledmorphogens.
Eq. (1) describes the slow nonlinear reactionf0=Γ​(M,N)−Lf_{0}=\Gamma(M,N)-L, with morphogen concentrationsMMandNN.
Extended models such as in[7,22]consider multiple primary (slow) fields.

The convolution form Eq. (2) for morphogen fields is a coarse-grained description of the fast-relaxed subsystem, assumed to follow first-order kinetics: linear reactionsfk≥1f_{k\geq 1}only allow conversion, decay and diffusion of auxiliary species.
Due to the timescale separation, each auxiliary field is linearly related to the slow fieldLLthrough a Green function that reflects the reaction network. When translation invariance is satisfied (with constant coefficients in unbounded or periodic space), these solutions reduce to convolutions:Ck=Φk∗LC_{k}=\Phi_{k}\ast L.

The only nonlinearity is carried by the target functionΓ\Gammain the slow reaction.333Previous discrete-time formulations such asSmoothLifeorLeniaalso includeLLin the nonlinearity, through the clamp function used to saturateLLto[0,1][0,1].Morphogen concentrations set the target valueΓ​(M,N)\Gamma(M,N)towards whichLLrelaxes.
The survival rule encoded inΓ\Gammatherefore specifies the morphogen ranges in whichLLis maintained or amplified:
for each value ofMM, growth is favoured only within a corresponding range ofNN, centred onNc​(M)N_{c}(M)and set by the widthδ​Nc​(M)\delta N_{c}(M).
In the reference morphology, the shell lies in the low-MMregion, where this range is narrow and close to the iso-concentration contourN≃N0N\simeq N_{0}, whereas the nucleus occupies a broader region at higher morphogen concentrations.
This correspondence between morphology and concentration-space regions is colour-coded in Fig.2.
Thus, the target parameters Eq. (7) directly definehomeostatic concentrationranges for the morphogens inside the emergent cell-like pattern.

## 4.2Fast reaction cascade and Gaussian kernels

The Gaussian shape of the kernels Eq. (3) can be accounted for by a long cascade of fast auxiliary reactions. To see this, consider a chain of auxiliary speciesCkC_{k},k=1,2,…k=1,2,\dots, sourced by the slow fieldC0=LC_{0}=L, and described by the simple linear reaction–diffusion networkτ​∂tCk=σ2​∇2Ck−Ck+Ck−1.\tau\partial_{t}C_{k}=\sigma^{2}\nabla^{2}C_{k}-C_{k}+C_{k-1}\quad.(10)

This network represents a cascade of diffusing and decaying species, each successively produced from the previous one and ultimately sourced by the slow fieldLL.
Using the separation of timescalesτ≪1\tau\ll 1, relaxed states are formally expressed asCk=[1−σ2​∇2]−k​L=ϕk∗L.C_{k}=[1-\sigma^{2}\nabla^{2}]^{-k}L=\phi_{k}\ast L\quad.(11)

The corresponding kernel shapesϕk=ϕ1∗⋯∗ϕ1\phi_{k}=\phi_{1}\ast\dots\ast\phi_{1}are obtained from Fourier transforms, expressing the Laplace operator∇2\nabla^{2}in terms of the spatial frequency (wave vector),−(2​π​|𝐪|)2-(2\pi|\mathbf{q}|)^{2}. The inverse Fourier transform yields their functional form, known as the Matérn kernelϕk​(𝐱)\displaystyle\phi_{k}(\mathbf{x})=∫ei​2​π​𝐪⋅𝐱(1+(2​π​σ​|𝐪|)2)k​d𝐪=(|𝐱|/σ)k​Kd2−k​(|𝐱|/σ)2k−1​(2​π​σ​|𝐱|)d2\displaystyle=\int\frac{e^{i2\pi\mathbf{q}\cdot\mathbf{x}}}{(1+(2\pi\sigma|\mathbf{q}|)^{2})^{k}}\,\mathrm{d}\mathbf{q}=\frac{(|\mathbf{x}|/\sigma)^{k}K_{\frac{d}{2}-k}(|\mathbf{x}|/\sigma)}{2^{k-1}(2\pi\sigma|\mathbf{x}|)^{\frac{d}{2}}}(12)

involving the modified Bessel function of the second kind, with exponential tailKν​(x)∼π2​x​e−xK_{\nu}(x)\sim\sqrt{\tfrac{\pi}{2x}}e^{-x}. This kernel corresponds to the steady spatial profile of thekthk^{\text{th}}species in the cascade, decaying and diffusing from a point source. This Green function is valid in unbounded space,𝐱∈ℝd\mathbf{x}\in\mathbb{R}^{d}. In the case of a short cascade,k≤d+12k\leq\frac{d+1}{2}, a singularity (or a cusp on the bound) is present at the origin.

The Gaussian kernels used in Eq. (3) are recovered in the limit of a long cascadek≫1k\gg 1: thekk-fold convolution of the elementary Green function approaches a Gaussian by the central limit theorem, summarized at the level of the space operator as[1−σ2​∇2]−k∼ek​σ2​∇2.[1-\sigma^{2}\nabla^{2}]^{-k}\sim e^{k\sigma^{2}\nabla^{2}}\quad.(13)

The unit-scale kernel in Eq. (3) is matched by taking the scaling limitσ2∼(4​π​k)−1\sigma^{2}\sim(4\pi k)^{-1}.
The small- and large-neighbourhood morphogen fieldsMMandNNare thus idealized as two selected species in theLL-sourced cascade Eq. (10), located at depthskkandλ2​k\lambda^{2}k, withk≫1k\gg 1.

Without a cascade, the simplest Bessel shapeϕ1\phi_{1}represents morphogens with different diffusion coefficients, directly sourced fromLLwithout intermediate reaction. In this case, gliding does not occur and divisions are incomplete, with the systematic formation of an intermediary body. A small cascade withM=ϕ1∗LM=\phi_{1}\ast LandN=ϕ9∗LN=\phi_{9}\ast L(or as small asϕ4\phi_{4}) is sufficient for complete divisions.

In line with the mapping proposed by[17], and extending its interpretation, the cGoL model can be viewed as a coarse-grained description of a large reaction–diffusion system in which the slow field responds nonlinearly to a few morphogens. Its distinctive feature is the non-standard nonlinearity encoded byΓ\Gamma, inherited from the GoL survival rule, which directly specifies homeostatic morphogen concentration ranges and the associated growth target.
The Gaussian shape of the kernels arises in the long-cascade limit of a linear reaction network of fast-diffusing and -decaying auxiliary species.

## 5Resource limitation as self-tuning feedback

Repeated cell division leads to unbounded proliferation, limited only by domain size. To address this unphysical behaviour, we extend the model with a global coupling to a finite resource. This global constraint is then shown to follow from a local conservation law, valid when the available resource diffuses fast. Finally, resource feedback dynamically retunes the parameters, driving the system to the edge of growth between the dense and dilute phases.

## 5.1Global constraint from finite resource

Let us assume that growth of the cell-like patterns consumes a finite resource, which is replenished when they decay. A global constraint can then be enforced by allowing only transfers between a reservoir and the slow fieldLL: the fixed total resourceRRis split into an available resourceRaR_{\text{a}}and a consumed resourceR−RaR-R_{\text{a}}modelled as the mass stored inLL444In unbounded space, one should not neglect the empty backgroundL∗−L_{\ast}^{-}, and define the consumed resource as∫(L−L∗−)​d𝐱\int(L-L_{\ast}^{-})\,\mathrm{d}\mathbf{x}.:R=Ra+∫Ld𝐱,∂tR=0.R=R_{\text{a}}+\int L\,\mathrm{d}\mathbf{x}\quad,\qquad\partial_{t}R=0\quad.(14)

Drawing inspiration from the resource abundance field in[27], a resource feedback can be introduced in the cGoL model via an abundance coefficientr​(t)=Ra​(t)R,r(t)=\frac{R_{\text{a}}(t)}{R}\quad,(15)

which is at most 1 for abundant available resource (as previously), and vanishing when the resource is fully consumed. A negative feedback onLLfrom decreasing globally available resourceRaR_{\text{a}}can be achieved by insertingr​(t)≤1r(t)\leq 1in the target,Γ​(M,N,r​(t))\Gamma(M,N,r(t)), as in Eq. (8).

The temporal modulationr​(t)r(t)breaks the equivalence in Eq. (8), yielding two distinct implementations: feedback type I (left-hand side) limits growth by decreasing the targetr​(t)​Γr(t)\Gamma, whereas feedback type II (right-hand side) decreases auxiliary fields,r​(t)​Mr(t)Mandr​(t)​Nr(t)N, or equivalently increases target parameters,𝐩/r​(t)\mathbf{p}/r(t).
Feedback of type II can be visualized as pushing the reference system towards the right in the top panel of Fig.3, as the available resource is consumed. Both types I and II introduce the mass∫L​d𝐱=1∗L\int L\,\mathrm{d}\mathbf{x}=1\ast Las a third variable (with constant kernel) in the nonlinearityΓ\Gamma.

By comparing perturbations of different parameters in Fig.3, it is apparent that the resource rarefaction effect is dominated by the increase of the first parameterMcM_{\text{c}}. Therefore, we further devise feedback type III that affects this parameter only.
One can preserve the bivariate formulation of the target functionΓ​(M,N)\Gamma(M,N)by merging1∗L1\ast Linto the definition of a perturbed kernel for the first auxiliary field:M=(Φ1−McR)∗LM=(\Phi_{1}-\tfrac{M_{\text{c}}}{R})\ast L.

We then quantify the effect of coupling the fieldLLto the globally available resourceRa​(t)R_{\text{a}}(t)from the conservation law Eq. (14).
The three feedback types are summarized as follows:r​(t)​Γ​(M,N;𝐩)\displaystyle r(t)\Gamma(M,N;\mathbf{p})type I𝐩​(t)=𝐩/r​(t)\displaystyle\mathbf{p}(t)=\mathbf{p}/r(t)type II(16)Mc​(t)=Mc​(1+1∗LR)≃Mc/r​(t)\displaystyle M_{\text{c}}(t)=M_{\text{c}}(1+\tfrac{1\ast L}{R})\simeq M_{\text{c}}/r(t)type III.\displaystyle\qquad\text{type III}\quad.

Among many other possibilities, the feedback mechanisms II and III can be interpreted as dynamically and autonomously retuning either all reference parameters Eq. (7), or just the first one, with coupling strengthR−1R^{-1}.

## 5.2Local conservation and the well-mixed limit

The global resource feedback can be viewed as the well-mixed limit of a locally conserved resource dynamics.
Letρa​(𝐱,t)\rho_{\text{a}}(\mathbf{x},t)denote the density of available resource, and letρ\rhobe the average density of total resource.
Feedback type I provides a natural form for the local dynamics:∂tL\displaystyle\partial_{t}L=r(𝐱,t)Γ(M,N)−L,r(𝐱,t)=ρa​(𝐱,t)ρ\displaystyle=r(\mathbf{x},t)\Gamma(M,N)-L\quad,\qquad r(\mathbf{x},t)=\frac{\rho_{\text{a}}(\mathbf{x},t)}{\rho}(17)∂t(L+ρa)\displaystyle\partial_{t}(L+\rho_{\text{a}})=Da​∇2ρa.\displaystyle=D_{\text{a}}\nabla^{2}\rho_{\text{a}}\quad.

The total densityL+ρaL+\rho_{\text{a}}follows a continuity equation with diffusive flux of the available resource, and therefore obeys a local conservation law.
The source terms in the dynamics ofLLandρa\rho_{\text{a}}are equal and opposite: growth ofLLconsumes locally available resource, whereas decay ofLLreplenishes it.
Integrating Eq. (17) recovers the global constraint Eq. (14), withRa=∫ρa​d𝐱R_{\text{a}}=\int\rho_{\text{a}}\,\mathrm{d}\mathbf{x}.
This local environmental feedback constitutes a mass-conserving counterpart to the non-conserved version introduced in[27], where resource is consumed to maintainLL, and continually restored to a target availability.

In the well-mixed limitDa→∞D_{\text{a}}\to\infty, the available resource becomes homogeneously distributed, so the local abundancer​(𝐱,t)r(\mathbf{x},t)reduces to the global one,Ra​(t)/R=r​(t)R_{\text{a}}(t)/R=r(t), recovering the global coupling with feedback type I introduced above.
The global resource model is thus a spatially averaged description of a locally conserved resource, accurate when this resource is a fast-relaxing species.

This finite-diffusion resource-feedback extension connects the original non-conserved cGoL dynamics to mass-conserving reaction–diffusion systems[13].
HereLLis conserved only together with the available-resource reservoir, unlike in strictly conservative reformulations[22,20], but in line with their food-channel extensions.
At fixedΓ​(M,N)\Gamma(M,N), the local conversion betweenLLandρa\rho_{\text{a}}satisfies detailed balance and admits a gradient-flow formulation with free-energy densityL​(log⁡L−1)+ρa​(log⁡ρa−1)+L​log⁡(ρ/Γ)L(\log L-1)+\rho_{\text{a}}(\log\rho_{\text{a}}-1)+L\log(\rho/\Gamma).
The full model is generically non-variational, however, becauseM,NM,NregulateLLwithout the reciprocal thermodynamic back-reactions required by a common free energy.
We leave the analysis of the finite-diffusion dynamics to future work, but preliminary observations suggest that finite resource diffusion can affect cell motion.

## 5.3From volume-limited growth to resource-limited self-tuning

Given a finite total resourceRRand a finite spatial domainΩ⊂ℝd\Omega\subset\mathbb{R}^{d}of volume|Ω||\Omega|, we count cells once at equilibrium555Starting from a low initial cell count, to leave room for growth., by thresholding the fieldMMat the transition valueMc=12M_{\text{c}}=\frac{1}{2}and by counting connected subsets ofΩ\OmegasatisfyingM>McM>M_{\text{c}}(distinct nuclei). This number may still fluctuate at long times, hence we estimate its mean valueν\nufrom both a temporal and an ensemble average across many simulations that have reached equilibrium.
Similarly, the fieldLLrelaxes to an equilibrium mean valueμ\mu, estimated by averaging the density∫ΩL​d𝐱/|Ω|\int_{\Omega}L\,\mathrm{d}\mathbf{x}/|\Omega|in the same way.
The average mass per cellm=μ​|Ω|νm=\frac{\mu|\Omega|}{\nu}is then deduced.

Their dependence on the resourceRRand volume|Ω||\Omega|is summarized in Fig.4:
the number of cellsν\nuis extensive in the limited resourceRR, provided the volume is sufficient, or extensive in the limited volume|Ω||\Omega|, provided the resource is sufficient. The discreteness of unit patterns is visible as steps for low cell countν=1,2,4,…\nu=1,2,4,\dotsThe cross-over between the resource-limited and volume-limited regimes occurs around a specific valueρ∗\rho_{\ast}of the resource density. The average value ofLLis well approximated byμ≃μ∞(ρ∗/ρ)2+1,ρ=R|Ω|,\mu\simeq\frac{\mu_{\infty}}{\sqrt{(\rho_{\ast}/\rho)^{2}+1}}\quad,\qquad\rho=\frac{R}{|\Omega|}\quad,(18)

used to fit the asymptotes shown in Fig.4(excludingν<4\nu<4):
for abundant resource,μ∞=0.131±0.001\mu_{\infty}=0.131\pm 0.001is a property of the reference cGoL model (r=1r=1), whereas for limited resource,μ∼μ∞​ρ/ρ∗\mu\sim\mu_{\infty}\rho/\rho_{\ast}is specific to the feedback type, withρ∗(I, II)=10.5±0.5\rho^{\text{(I, II)}}_{\ast}=10.5\pm 0.5andρ∗(III)=13.5±0.5\rho^{\text{(III)}}_{\ast}=13.5\pm 0.5.Figure 4:Equilibrium states as a function of resourceRRand volume|Ω||\Omega|, in terms of the number of cellsν\nu, the average densityμ\mu, and the mass per cellmm. Lines encode different volumes (colours) and resource feedback types: target scaling (I), morphogen scaling (II), and kernel shift (III). Grey lines show the asymptotes of the fitted Eq. (18).

Irrespective of the approximation Eq. (18), the equalityμ(I)=μ(II)⇔r(I)=r(II)\mu^{\text{(I)}}=\mu^{\text{(II)}}\,\Leftrightarrow\,r^{\text{(I)}}=r^{\text{(II)}}is observed to be robust in all regimes.
Since feedback types I and II share the same long-term resource abundance coefficientr=r(I, II)=1−μ(I, II)/ρr=r^{\text{(I, II)}}=1-\mu^{\text{(I, II)}}/\rho, the same cell morphology is expected from Eq. (8), up to a rescaling ofLL. This rescaling explains the mismatch of the mass per cell at limited resource (r<1r<1):m(II)=m(I)/rm^{\text{(II)}}=m^{\text{(I)}}/r, visible in Fig.4and rescaled in the inset. As a consequence, the number of cells also differs:ν(II)=r​ν(I)\nu^{\text{(II)}}=r\nu^{\text{(I)}}.

The mass per cell varies from aboutm∗(II)=m∗(I)/r∗=6.10±0.05m_{\ast}^{\text{(II)}}=m_{\ast}^{\text{(I)}}/r_{\ast}=6.10\pm 0.05orm∗(III)=6.05±0.05m_{\ast}^{\text{(III)}}=6.05\pm 0.05in the resource-limited regime, tom∞=5.725±0.005m_{\infty}=5.725\pm 0.005otherwise. This mass reduction for abundant resource can be explained as follows: when volume-limited, cells keep dividing and vanishing after reaching confluence, hence they are in different elongation states. In contrast, resource-limited cells stop dividing (and glide without oscillation) when they reach equilibrium, but they remain in an elongated state with enhanced mass below the division point.
The number of cellsν\nu, when sufficiently large, can be expressed in terms of the previously identified quantitiesν≃{μ∞​Rm∗​ρ∗,ρ≪ρ∗μ∞​|Ω|m∞,ρ≫ρ∗\displaystyle\nu\simeq\begin{cases}\displaystyle\frac{\mu_{\infty}R}{m_{\ast}\rho_{\ast}}\quad\;\,,\qquad\rho\ll\rho_{\ast}\\
\displaystyle\frac{\mu_{\infty}|\Omega|}{m_{\infty}}\quad,\qquad\rho\gg\rho_{\ast}\end{cases}(19)

with the specific relations between types I and II:ρ∗(I)=ρ∗(II)\rho_{\ast}^{\text{(I)}}=\rho_{\ast}^{\text{(II)}}andm∗(I)=r∗​m∗(II)m_{\ast}^{\text{(I)}}=r_{\ast}m_{\ast}^{\text{(II)}}.

The equilibrium system with resource feedback effectively behaves as a retuned version of the original model without feedback.
In the resource-limited regimeρ≪ρ∗\rho\ll\rho_{\ast}, always reached in the large-volume limit|Ω|→∞|\Omega|\!\to\!\inftyat fixedRR, the extensive behaviour of the reference model saturates at a total massμ​|Ω|∼μ∞​R/ρ∗\mu|\Omega|\!\sim\!\mu_{\infty}R/\rho_{\ast}.
During the transient growth, the system adjusts itself to a boundary point on the transition manifold between the extensive (volume-limited, dense) and non-extensive (resource-limited, dilute) phases of the parameter space.
With feedback type II, all reference parameters are rescaled to𝐩/r∗\mathbf{p}/r_{\ast}by the common factorr∗=1−μ∞/ρ∗(I, II)≃0.987r_{\ast}=1-\mu_{\infty}/\rho^{\text{(I, II)}}_{\ast}\simeq 0.987, while feedback type III only modifies the first parameter toM∗=(1+μ∞/ρ∗(III))​Mc≃1.010​McM_{\ast}=(1+\mu_{\infty}/\rho^{\text{(III)}}_{\ast})M_{\text{c}}\simeq 1.010\,M_{\text{c}}.
Consequently, the hand-tuned reference parameters of Eq. (7) reside in the dense, volume-limited phase, within∼1\sim\!1% of the edge of growth, motivating a broader exploration of the surrounding phase structure.

## 6Exploration of phase structure

The resource-feedback model identified a critical abundancer∗r_{\ast}marking the edge of growth, for the neighbourhood scale ratioλ=3\lambda=3. We now broaden this picture through an extensive scan of density and contrast order parameters across the two-parameter plane(r,λ)(r,\lambda), mapping the changeover between background basins, each containing a stability boundary for single droplet patterns and an edge of growth. Finally, we extend the self-tuning estimate ofr∗r_{\ast}acrossλ\lambda, uncovering the richness of life-like morphologies that self-organize near this edge.

## 6.1Control and order parameters

We first treat the resource abundance coefficientrras a constant control parameter, without feedback.
As shown in Eq. (8), scaling the target function byrris equivalent to moving along the parameter-space line𝐩/r\mathbf{p}/r, with𝐩\mathbf{p}as in Eq. (7).
This rescales the 6 target parameters setting homeostatic morphogen concentration ranges: increasingrrpromotes growth, whereas decreasingrrinhibits it.

The neighbourhood scale ratioλ\lambda, kept fixed so far, controls the separation between the two averaging kernels and is the only geometric parameter of the model.
It therefore provides a natural second control parameter.

As previously studied for a limited resource, the averaged densityμ\muprovides a simple order parameter, or observable. In the absence of resource feedback,μ\muis
expected to jump near transition values ofrr, separating dilute from dense phases, in which growing patterns fill the available volume until the average density reaches its saturation valueμ∞\mu_{\infty}.
This expectation is confirmed in Fig.5, where several
transitions are visible in the profileμ​(r)\mu(r)and later described; the sharpest cliff lies in the previously identified intervalr∈[0.987,1]r\in[0.987,1].

To complement the averaged densityμ\muand better distinguish the upper homogeneous state (visible in Fig.5between D and E) from inhomogeneous patterns, we introduce a second order parameter capturing the field contrast.
As the average densityμ∈[0,1]\mu\in[0,1], it can be defined from the distributionℙ​(ℓ)\mathbb{P}(\ell)of field values (the histogram ofLL) as a diversity index or exponential entropyκ∈[0,1]\kappa\in[0,1]:μ\displaystyle\mu=∫01ℓℙ(ℓ)dℓ,ℙ(ℓ)=limt→∞|Ω|−1∫Ωδ(ℓ−L(𝐱,t))d𝐱\displaystyle=\int_{0}^{1}\ell\mathbb{P}(\ell)\,\mathrm{d}\ell\quad,\qquad\mathbb{P}(\ell)=\lim_{t\to\infty}|\Omega|^{-1}\int_{\Omega}\delta(\ell-L(\mathbf{x},t))\,\mathrm{d}\mathbf{x}(20)κ\displaystyle\kappa=exp⁡(−∫01ℙ​(ℓ)​log⁡ℙ​(ℓ)​dℓ).\displaystyle=\exp\left(-\int_{0}^{1}\mathbb{P}(\ell)\log\mathbb{P}(\ell)\,\mathrm{d}\ell\right)\quad.

Indeed, the quantitylog⁡κ\log\kappais a differential entropy over the unit interval[0,1][0,1]that is the span of the targetΓ\Gamma(hence ofLL). More generally,−log⁡κ-\log\kappacan be understood as the relative entropy (Kullback–Leibler divergence) betweenℙ​(L)\mathbb{P}(L)and the uniform statistical distribution, hereℙ0=1\mathbb{P}_{0}=1, which represents the most heterogeneous case (κ=1\kappa=1). A homogeneous fieldL=L∗L=L_{\ast}, henceℙ​(ℓ)=δ​(ℓ−L∗)\mathbb{P}(\ell)=\delta(\ell-L_{\ast}), has vanishing contrastκ=d​ℓ→0\kappa=\,\mathrm{d}\ell\to 0(bin size).

Both order parameters, density and contrast, can be compared in Fig.6.
Their coefficient of variation across independent simulations also turns out to be informative to detect lack of convergence or dependence on initial conditions.Figure 5:Scan of the densityμ\mu(order parameter), with constant resource abundancerras control parameter. Standard deviation around the mean (coloured area) over independent simulations for a given volume|Ω||\Omega|. Edges of growth and droplet stability (dotted and dashed lines). Scale ratioλ=3\lambda=3, initial state with 2 seeds, cutoff timetmax=5000t_{\max}=5000.

## 6.2Lower and upper background basins

The numerous phases visible in Figs.5and6form a sequence that appears twice, see Fig.5(A–C) and (E–G).
This repetition reflects the two homogeneous stable fixed points,L∗−L_{\ast}^{-}andL∗+L_{\ast}^{+}, which can each serve as an empty background for localized patterns.
The changeover around Fig.5(D) separates the corresponding background basins, at lower and higherrrrespectively.

In Fig.5(λ=3\lambda=3), the stateL∗−≃0L_{\ast}^{-}\simeq 0is dominant forr<1.1r<1.1, whileL∗+≃N0/rL_{\ast}^{+}\simeq N_{0}/rtakes over forr>1.1r>1.1, with overlap aroundr=1.10±0.05r=1.10\pm 0.05in Fig.5(C–D).
Asrrincreases, crowded cell or snake dynamical patterns on theL∗−L_{\ast}^{-}background are increasingly bridged and surrounded by local patches ofL∗+L_{\ast}^{+}, until chaotic fluctuations allowL∗+L_{\ast}^{+}to percolate (D) and fully replaceL∗−L_{\ast}^{-}.
When this happens, the localized patterns usually dissolve intoL∗+L_{\ast}^{+}, which then becomes the empty background for patterns at higherrr.

The observed transition between the two background basins is sensitive to finite-size effects and exhibits a broad probability distribution.
Increasing the time cutoff reduces the transition value ofrr, while increasing the volume|Ω||\Omega|increases it (see Fig.5D). A dependence on the initial condition is also observed forλ<3\lambda<3, making accurate estimation challenging in the ideal unbounded case.

Visible as a sharp and noisy drop of the exp-entropyκ\kappain Fig.6, this transition roughly separates the two background basins, whose boundaries are marked in blue and orange for the lower and upper basins, respectively.Figure 6:Scan of order parameters(μ,κ)(\mu,\kappa)with control parameters(r,λ)(r,\lambda).
The median over 20 trials is retained for|Ω|=212|\Omega|=2^{12}, 5λ\lambda-scaled seeds,tmax=1000t_{\max}=1000.
Edge of growth (left, multiple estimates) and stability boundary for a single droplet (right) in the lower and upper background basins (blue and orange lines). Localized states along these lines (bottom,λ\lambdaincreases from left to right).

## 6.3Boundary of droplet stability

The first type of boundary delimits the stability of single droplet patterns in a dilute phase.

Visible in Fig.6at lowμ\muandκ\kappa, the region of successful initialization, which depends on the seed characteristics, is more fundamentally bounded by the region of stability of localized states. The egg pattern in Fig.2(D) is ubiquitous in the lower basin. A similar localized state exists in the upper basin in the form of a dot pattern. A single such droplet is only stable above the boundary lines plotted in each basin in Fig.6(top right, also reported in Fig.5, dotted lines).

These stability boundaries are determined accurately, albeit numerically, by bisecting the value ofrrstarting from a successful seed, best with radius proportional toλ\lambda.
They do not constitute an absolute bound for the existence of non-homogeneous stable solutions: the stability boundary of droplets in dimensiond=1d=1, which corresponds ind=2d=2to a column or stripe pattern (local in the first dimension, constant and extended in the second), can stably occur at lowerrrbut is not observed in the scan due to the lack of space-spanning initial seed.

Long-lived or stable non-dissolved patterns are visible below the upper-rrdroplet (dot) stability boundary (orange line) as low but non-zeroκ\kappavalues atλ>3\lambda>3in Fig.6(top right). A ring (or bubble) is an example of such a structure, another example is shown to the right of the sequence of dot patterns at the largest valueλ=5\lambda=5: the dot has vanished but surrounding small-scale structures survive (a similar behaviour can occur ind=1d=1).

The limit of survival of an egg pattern (lower-rrdroplet) is reached when the empty space between the shell and the nucleus has vanished, as is the case in the lower droplet illustration of Fig.5. Collective effects have been observed to extend the survival region of these droplet-like patterns, in accordance with the original rule of theGame of Life.

## 6.4Edge of growth: dilute-to-dense transition

The second type of boundary marks the transition between the dilute phase, with non-growing cells or eggs and dots (see Fig.5A and E respectively), and the dense space-filling phase (C and G). The lower dense phase (C) is very dynamical, with dividing-dying cells and growing-shrinking snakes, whereas the upper one reaches a static space-filling configuration (Turing-like pattern in G).

In both the lower and upper basins,
values of order parametersμ\muandκ\kappain the dilute phase depend on the initial state and the number of surviving patterns (the average density is at leastL∗±L_{\ast}^{\pm}), whereas they converge to a saturation value in the dense phase.

The edge of growth in the lower basin, previously determined forλ=3\lambda=3at the critical valuer∗≃0.987r_{\ast}\simeq 0.987, relies on the self-tuning ofrrfrom the resource limitation feedback at large volume.
At constantrr, however, growth is difficult to ignite slightly beyond the edge, because spontaneous growth from a single isolated cell often requires a larger value ofr>r∗r>r_{\ast}. A simulation initialized with a single seed can therefore remain dilute, although growth may occur after a sufficient finite-amplitude perturbation.666Similarly, manyLeniagliders turn into space-filling patterns upon destabilization, although more explosively.An overestimate ofr∗r_{\ast}is usually read from the location of the sharp cliff ofμ\muobserved in Figs.5(B) and6(top left), which matches the spontaneous growth threshold of a single cell (thick blue line, see the sequence of division patterns below).
The cliff’s location tends to get closer tor∗r_{\ast}with the number of collisions (higher number of seeds, longer times).
The edge of growth therefore appears as a collective transition of interacting patterns, for which single-cell growth thresholds provide useful but generally biased estimates.

In the upper basin, the edge of growth has been estimated by bisecting the value ofrrfor which the growth or shrinkage of a single snake-like pattern stops, see the bottom sequence of patterns in Fig.6. This single-snake estimation is quite predictive, since this pattern is the main generator of growth in this slice of the parameter space. However, a snake making a U-turn can still generate growth below the estimatedrr.
Here again, collective effects and self-contact affect the accurate position of the edge of growth, visible as a slight misalignment of the estimates (top left, orange line) with the scans.

The variety of growth-generating patterns at the lower edge makes the estimation particularly delicate. The ones illustrated in Fig.6are located on the cliff (top left, thick blue line).
While metastable growing bubbles can be found at quite lowrrvalues forλ>3\lambda>3and even produce numerous gliding cells when destabilized, those cells can be fragile and easily disappear after a collision. The statistical nature of this transition is clear in this situation. The opposite regimeλ<3\lambda<3is characterized by the emergence of chains and filaments, forming a foam that
can persist at lowerrrvalues than the cliff’s overestimate and eventually percolate. The extent of the foam region (top left, thin blue line) is estimated from therrlocation of a smaller jump of the maximum order parameter obtained with 50 seeds instead of 5. The foam is generated by gliding cell-like patterns at the tip of extending filaments. Visible in Fig.7, this growth pattern is reminiscent of spores and hyphae forming a mycelium.

## 6.5Self-organization near the edge of growth

Starting from an overestimater∞r_{\infty}of the lower edge of growth at fixedλ\lambda, we conduct a self-tuned estimation based on the resource-limitation mechanism. We introduce a finite total resourceRRand the associated negative feedback of type II at a fixed volume|Ω|=212|\Omega|=2^{12}. The equilibrium density of the systemμ\muand the corresponding resource abundance scaling factorr∞​(1−μ​|Ω|/R)r_{\infty}\,(1-\mu|\Omega|/R)are monitored at decreasing values ofRR. The resource must be limiting enough to leave the volume-saturated regime (extensivity withRRmust be verified), but also sufficient to generate many interacting cells.
An estimate ofr∗r_{\ast}is extracted from a noisy resource abundance plateau in the suitableRR-range, and can sometimes be refined without increasing|Ω||\Omega|, by loweringr∞>r∗r_{\infty}>r_{\ast}to enlarge this range.

A selection of patterns produced near the edge of growth by such resource-limited estimations is presented in Fig.7. Although the mass and available resource can fluctuate, these near-transition morphologies can be mapped in Fig.6(top left, blue markers) with coordinates(r≃r∗,λ)(r\simeq r_{\ast},\lambda).

Disappearance provides an imperfect restoring mechanism from the dilute phase back to the edge, since cells can survive down to the droplet stability boundary region. Thus, decreasingRRin the dilute phase is often associated with mass hysteresis and produces underestimates ofr∗r_{\ast}, unless the system is reset at a lower mass to ensure starting in the dense phase. Large mass collapses are also frequent in the foam state, so that a sufficient value ofr∞r_{\infty}is needed to reignite growth.

Complex phenomena arise from the delicate interplay of growth- and decay-inducing dynamics, subtly encoded in the morphological variations of these emergent life-like patterns.\begin{overpic}[width=433.62pt,decodearray=1 0 1 0 1 0]{figs/field_cliff_v1.pdf}
\put(1.5,51.2){$\;r_{\ast}\simeq 1.5\;\;\;\,\lambda=1.68$}
\put(26.5,51.2){$\;r_{\ast}\simeq 1.3\;\;\;\,\lambda=1.86$}
\put(51.5,51.2){$\,r_{\ast}\simeq 1.10\;\;\;\lambda=2.20$}
\put(76.5,51.2){$r_{\ast}\simeq 1.025\;\;\lambda=2.56$}
\put(1.5,-2.2){$r_{\ast}\simeq 0.998\;\;\lambda=2.77$}
\put(26.5,-2.2){$r_{\ast}\simeq 0.981\;\;\lambda=3.22$}
\put(51.5,-2.2){$r_{\ast}\simeq 0.973\;\;\lambda=3.93$}
\put(76.5,-2.2){$r_{\ast}\simeq 0.985\;\;\lambda=4.80$}
\end{overpic}
Figure 7:Resource-limited patterns, self-organized near the (lower) edge of growth, indicated by blue markers in Fig.6. Volume|Ω|=212|\Omega|=2^{12}.

## 7Discussion and outlook

## Synthesis

Strikingly, translating theGame of Lifeinto a continuous and minimal model leads to the emergence of cell-like patterns with a nucleus and a shell, capable of self-replication, motility, and disappearance.
The cGoL model admits a coarse-grained, non-standard reaction–diffusion interpretation: its two auxiliary fields encode the state of the neighbourhood at distinct scales and serve as fast-relaxed morphogen concentrations, produced through a cell-sourced cascade of intermediate reactions.
The nonlinear survival rule then specifies growth conditions as homeostatic concentration ranges for these morphogens.
In this chemical interpretation, the shell is maintained in a narrow band near a low-concentration contour, enclosing a nucleus regulated by a broader range of higher morphogen concentrations.
Slight variations around this morphology reveal a rich diversity of behaviours and dynamical phenomena.
These are organized near a dynamical phase transition separating a dilute phase with quiescent patterns from a dense one in which cells proliferate through successive divisions.
A related transition also appears in a distinct region of parameter space associated with a non-vanishing background state, where snake-like patterns elongate or shrink into droplets.

Assuming that growth locally consumes a diffusive environmental resource, the model can be embedded in a mass-conserving dynamics; in the well-mixed regime, this reduces to a global resource constraint.
Resource limitation then acts as a self-organization mechanism: when initialized in the dense phase, the feedback effectively retunes the parameters and drives the system toward the edge of growth.
At this boundary, collective interactions can stimulate divisions below the spontaneous growth threshold of an isolated cell.
Across neighbourhood scale ratios, the same self-tuning procedure estimates the location of the edge and reveals a diversity of surviving and growth-generating life-like morphologies.
We now turn to the perspectives and implications of this study.

## Dynamical systems

Our description of the emergent cells is primarily phenomenological.
Beyond the saddle-node structure of homogeneous states, localized morphologies are described in terms of observed symmetry breaking, shape instabilities, bifurcations, and finite-amplitude transitions.
This empirical picture suggests that the reference cell lies near several long-lived localized morphologies and close to a collective dilute-to-dense transition, where self-replication either ceases or is balanced by disappearance.
A natural continuation is to analyse these phenomena with the dynamical-systems tools recently applied to localized patterns in continuous-timeLeniaby[28]: Lyapunov spectra, covariant Lyapunov vectors, and symmetry-generated neutral modes provide a linear-perturbation framework.
In the present model, this framework could characterize infinitesimal instabilities of isolated cells, distinguish regular from chaotic regimes, and guide the construction of bifurcation diagrams linking eggs, gliders, and related morphologies.

However, some division events, collision-induced switches, and activity avalanches involve finite-amplitude transitions; the associated infinitesimal instabilities can nevertheless be probed by linearizing the dynamics along trajectories in which these events occur.
Self-replication raises an additional challenge, since the number of localized patterns changes in time and the effective attractor dimension may become extensive in the dense phase.
A full dynamical description should therefore connect single-pattern stability with finite-time diagnostics and event-conditioned perturbations, then extend to basin-level and statistical descriptions of collective transitions.

## Self-organization and criticality

The resource feedback illustrates how a conservation law, introduced into otherwise non-conserved dynamics, can become an organizing principle: it embeds parameter tuning into the dynamics itself.
This invites comparison with classical self-organized critical systems, while also exposing important differences. The model combines several relevant ingredients: conservation, an autonomous approach to a transition in the large-volume limit, a boundary reminiscent of quiescent-to-active transitions, and robustness to feedback details and parameter variations, provided the system is initialized in the active phase. Important differences remain: the restoring mechanism on the dilute side is imperfect, drive and relaxation are not imposed as separate processes, and the relevant activity order parameter remains unclear in a continuous system where persistent localized dynamics need not imply net growth.

Nevertheless, previous studies have reported evidence for self-organized criticality or near-criticality in the discreteGame of Life[3,2,25]; its continuously adjustable logistic extension displays two critical points[1], one with a quiescent-to-active transition resembling the edge of growth, the other percolation-like and perhaps closer to the background-basin change observed here.
In the cGoL, the jump in the density order parameter suggests that parts of the sampled edge behave as first-order or coexistence-like transitions; however, this does not exclude near-critical behaviour, nor a genuine continuous transition in an underlying activity observable tied to proliferation, disappearance or avalanches. More broadly, the present(r,λ)(r,\lambda)scan samples only a restricted slice of a likely high-dimensional edge-of-growth manifold, which already appears to include coexistence fronts, hysteretic foams or filaments with episodic collapses, and long-range organized states such as the polarized cell alignments visible in Fig.7. This diversity is naturally discussed within the broader framework reviewed by[4], which includes self-organization near criticality, self-organized bistability, and related scenarios. Distinguishing these possibilities will likely require activity measures adapted to continuous life-like patterns, together with avalanche statistics, hysteresis tests, finite-size scaling and correlation diagnostics.

## Dimension, degrees of freedom and evolution

The spatial dimension was fixed tod=2d=2for the main presentation, but it remains a structural variable controlling the morphologies and instabilities available to localized patterns.
At fixed parameters, lower-dimensional solutions can be embedded in higher dimensions by extending them uniformly along the additional coordinates: one-dimensional patterns become stripes or walls, while two-dimensional cells become columns.
Transverse instabilities can destabilize these embedded states and generate new morphologies.
Conversely,d=1d=1lacks the transverse pinching mechanism required for autonomous scission, although certain metastable growing patterns can split after external perturbations.
Cell division also occurs ind=3d=3, and gliders or oscillators occur in bothd=1d=1andd=3d=3, though generally at shifted parameter values.
Understanding how dimension affects morphology and stability may reveal a more natural parametrization of the target function and further reduce the model’s effective degrees of freedom.

The target function was deliberately kept parsimonious, with 6 target parameters and the geometric scale ratioλ\lambda.
Nevertheless, locating a life-like region such as the one presented here would be difficult without relying on successive rule refinements, from theGame of Lifecellular automaton to the continuous-space systemSmootherLife[8], the immediate precursor of the present formulation.
Resource feedback reframes this tuning problem rather than removing it: the abundance parameter, previously hand-tuned and implicit, is replaced by a fixed total resource, an environmental quantity that need not itself be carefully tuned.
This cell–environment split also confers robustness: the system needs only start in the dense phase, rather than at the edge, since it self-organizes towards it.
The harder challenge remains identifying, for other parametrizations, comparable regions of dilute-to-dense transition that support such self-replicating, life-like behaviour—or discovering novel self-tuning mechanisms that narrow this search.

Finally, viewing the cGoL as a minimal model for hypothetical primordial life-forms raises the question of evolution.
A biologically motivated extension would allow each cell to carry potentially distinct heritable values of the parameters, subject to mutations at the individual level.
Selection would then act indirectly on these parameters through phenotypic behaviours such as self-replication, motility, and robustness to interactions, so that persistence, propagation, and disappearance—all emergent from the dynamics itself—define an autonomous selection process in which individual mutations drive a coupled stochastic exploration of high-dimensional parameter spaces across interacting cells.
Preliminary observations suggest the importance of self-organization near the edge of growth: without this resource feedback, selection favours parameters yielding rapid spatial expansion, whereas resource limitation keeps the dynamics in a marginal regime where survival and reproduction depend on the detailed behaviour of localized patterns.
Implementing inter-individual diversity in the cGoL and studying its evolutionary consequences will be addressed in a separate article.

## Data and Code Availability

Code is available at:codeberg.org/A-Guillet/cGoL.

## Acknowledgements

We acknowledge the cross-fertilizing contributions from citizen science, generative arts and software engineering, which have fostered important progress, not only through models but also via efficient cross-platform implementations, interactive tools and empirical exploration techniques that help manage the complexity of these life-like systems and enable enthusiasts to explore their beauty.
A.G. gratefully acknowledges Théotime Girardot, CornusAmmonis, Daniel M. Busiello, Jérémy Sourd and the anonymous reviewers for their valuable feedback and thoughtful suggestions, which played a significant role at various stages of development of this project.

This work has been funded by the Max Planck Society.

## References
- [1]H. Akgün, X. Yan, T. Taşkıran, M. Ibrahimi, C. H. Lee, and S. Jahangirov(2026-03)Deterministic scale-invariant dynamics in a logistic Game-of-Life model.Communications Physics9(1),pp. 173.External Links:ISSN 2399-3650,Document,LinkCited by:§7.
- [2]P. Alstrøm and J. Leão(1994-04)Self-organized criticality in the “game of Life”.Physical Review E49(4),pp. R2507–R2508.External Links:ISSN 1063-651X, 1095-3787,Document,LinkCited by:§7.
- [3]P. Bak, K. Chen, and M. Creutz(1989-12)Self-organized criticality in the ’Game of Life’.Nature342(6251),pp. 780–782.External Links:ISSN 0028-0836, 1476-4687,Document,LinkCited by:§7.
- [4]V. Buendía, S. Di Santo, J. A. Bonachela, and M. A. Muñoz(2020-09)Feedback mechanisms for self-organization to the edge of a phase transition.Frontiers in Physics8,pp. 333.External Links:ISSN 2296-424X,Document,LinkCited by:§7.
- [5]C. Calcaterra and A. Boldt(2023-01)Existence of life in Lenia.International Journal of Dynamical Systems and Differential Equations13(3),pp. 218–230.External Links:2203.14390,ISSN 1752-3583,Document,LinkCited by:§1.
- [6]B. W. Chan(2019-10)Lenia: biology of artificial life.Complex Systems28(3),pp. 251–286.External Links:1812.05433,ISSN 08912513,Document,LinkCited by:§1.
- [7]B. W. Chan(2020)Lenia and expanded universe.InThe 2020 Conference on Artificial Life,Online,pp. 221–229.External Links:2005.03742,Document,LinkCited by:§1,§4.1.
- [8]CornusAmmonis(2017-01)Smoother Life.External Links:LinkCited by:§1,§2.2,§7.
- [9]Q. T. Davis and J. Bongard(2022)Step size is a consequential parameter in continuous cellular automata.InThe 2022 Conference on Artificial Life,Online,pp. 43.External Links:Document,LinkCited by:§1.
- [10]K. M. Evans(2001)Larger than Life: digital creatures in a family of two-dimensional cellular automata.InDiscrete Mathematics & Theoretical Computer Science Proceedings,Vol.AA,pp. 177–192.External Links:ISSN 1365-8050,Document,LinkCited by:§1.
- [11]K. M. Evans(2003-09)Larger than Life: threshold-range scaling of Life’s coherent structures.Physica D: Nonlinear Phenomena183(1-2),pp. 45–67.External Links:ISSN 01672789,Document,LinkCited by:§1.
- [12]M. Gardner(1970-10)Mathematical Games.Scientific American223(4),pp. 120–123.External Links:ISSN 0036-8733,Document,LinkCited by:§1.
- [13]J. Halatek and E. Frey(2018-05)Rethinking pattern formation in reaction–diffusion systems.Nature Physics14(5),pp. 507–514.External Links:ISSN 1745-2481,Document,LinkCited by:§5.2.
- [14]B. Hudcová, F. Dušek, M. Tuccio, and C. Hongler(2026-01)Visualizing the structure of Lenia parameter space.arXiv.External Links:2601.01932,Document,LinkCited by:§3.3.
- [15]T. Hutton, R. Munafo, A. Trevorrow, T. Rokicki, and D. Wills(2015)Ready, a cross-platform implementation of various reaction-diffusion systems.External Links:LinkCited by:§1,§1.
- [16]T. Kawaguchi, R. Suzuki, T. Arita, and B. Chan(2021)Introducing asymptotics to the state-updating rule in Lenia.InThe 2021 Conference on Artificial Life,Online,pp. 91.External Links:Document,LinkCited by:§1,§2.1.
- [17]H. Kojima and T. Ikegami(2023)Implementation of Lenia as a reaction-diffusion system.InThe 2023 Conference on Artificial Life,pp. 43.External Links:Document,LinkCited by:§1,§4.1,§4.2.
- [18]B. J. MacLennan(1990-11)Continuous spatial automata.Technical reportTechnical ReportCS-90-121,University of Tennessee, Department of Computer Science,Knoxville, TN.Cited by:§1.
- [19]V. Papadopoulos, G. Doat, A. Renard, and C. Hongler(2024-07)Looking for complexity at phase boundaries in continuous cellular automata.InProceedings of the Genetic and Evolutionary Computation Conference Companion,Melbourne VIC Australia,pp. 179–182.External Links:Document,Link,ISBN 979-8-4007-0495-6Cited by:§3.3.
- [20]V. Papadopoulos and E. Guichard(2025-07)MaCE: general mass conserving dynamics for cellular automata.arXiv.External Links:2507.12306,Document,LinkCited by:§1,§5.2.
- [21]M. Pivato(2007-03)RealLife: The continuum limit of Larger than Life cellular automata.Theoretical Computer Science372(1),pp. 46–68.External Links:ISSN 0304-3975,Document,LinkCited by:§1.
- [22]E. Plantec, G. Hamon, M. Etcheverry, P. Oudeyer, C. Moulin-Frier, and B. W. Chan(2023)Flow-Lenia: towards open-ended evolution in cellular automata through mass conservation and parameter localization.InThe 2023 Conference on Artificial Life,pp. 131.External Links:Document,LinkCited by:§1,§4.1,§5.2.
- [23]S. Rafler(2011-12)Generalization of Conway’s “Game of Life” to a continuous domain - SmoothLife.arXiv.External Links:1111.1567,LinkCited by:§1,§2.2.
- [24]S. Rafler(2012-06)SmoothLife.External Links:LinkCited by:§1.
- [25]S. M. Reia and O. Kinouchi(2014-05)Conway’s game of life is a near-critical metastable state in the multiverse of cellular automata.Physical Review E89(5),pp. 052123.External Links:Document,LinkCited by:§7.
- [26]P. Rendell(2002)Turing Universality of the Game of Life.InCollision-Based Computing,A. Adamatzky (Ed.),pp. 513–539.External Links:Document,Link,ISBN 978-1-85233-540-3 978-1-4471-0129-1Cited by:§1.
- [27]R. Suzuki, K. Asakura, and T. Arita(2023)Lenia in a petri dish: Interactions between organisms and their environment in a Lenia with growth based on resource consumption.InThe 2023 Conference on Artificial Life,pp. 27.External Links:Document,LinkCited by:§1,§5.1,§5.2.
- [28]I. Yevenko, H. Kojima, and C. L. Nehaniv(2025-08)Using dynamical systems theory to quantify complexity in asymptotic Lenia.arXiv.External Links:2508.02935,Document,LinkCited by:§1,§7.
- [29]I. Yevenko(2024)Classifying the fractal parameter space of the Lenia Orbium.InThe 2024 Conference on Artificial Life,Online,pp. 14.External Links:Document,LinkCited by:§3.3.

## 


- 


Major funding support from
