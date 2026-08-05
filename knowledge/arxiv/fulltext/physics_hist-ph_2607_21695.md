# Dimensional Analysis is a Gauge Theory

**arXiv ID**: 2607.21695v1
**Authors**: Benjamin Muntz
**Published**: 2026-07-23
**Categories**: physics.hist-ph, gr-qc, hep-th, math-ph
**Comments**: 55 pages, comments are welcome!
**HTML URL**: https://arxiv.org/html/2607.21695v1

## Abstract

I argue that dimensional analysis can appropriately be thought of as a gauge theory. This picture naturally leads to the usual quantity calculus through inherent properties of Lie groups, Lie algebras, and representation theory. The gauge theory interpretation is perhaps strongest for non-constant units. I explain how Stevens's classification of scales of measurement can be understood by choices of different gauge groups. Finally, I reinterpret and rephrase the Buckingham-Π Theorem in a way that also applies to typical gauge theories. Counting the number of ''Π''s becomes a well-known problem of invariant theory.

## Full Text

Dimensional Analysis is a Gauge Theory

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
- License: CC BY 4.0arXiv:2607.21695v1 [physics.hist-ph] 23 Jul 2026

## Dimensional Analysis is a Gauge TheoryBenjamin Muntz111benjamin.muntz@nottingham.ac.uk

## Abstract

I argue that dimensional analysis can appropriately be thought of as a gauge theory. This picture naturally leads to the usual quantity calculus through inherent properties of Lie groups, Lie algebras, and representation theory. The gauge theory interpretation is perhaps strongest for non-constant units. I explain how Stevens’s classification of scales of measurement can be understood by choices of different gauge groups. Finally, I reinterpret and rephrase the Buckingham-Π\PiTheorem in a way that also applies to typical gauge theories. Counting the number of “Π\Pi”s becomes a well-known problem of invariant theory.

## 1Introduction

Consider the following riddle:

Vectors live in vector spaces.
Symmetries live in groups.
But units — the meter, second, gram, and so on — live where?

A lot can be intuited from where someone lives. The same is true for mathematical objects. How and why vectors may be added, scaled, or transformed becomes mathematically firmer once we abandon cartoonish arrows and situate them in vector spaces. Likewise, symmetry transformations acquire foundation once we consider them as elements of groups (typically acting on something). But for units, the situation is strangely unclear. From everyday reasoning we understand and picture how one can add one meter to another meter, or one second to another second, yet adding one second to a meter is completely nonsensical. Moreover, multiplying two lengths yields an area, dividing distance by time yields a speed, and so on. There is clearly a coherent algebraic structure at play — the so-calledquantity calculus— but it is nowhere stated where that structure actually originates from. If vectors inherit their algebraic properties from the fact that they inhabit vector spaces, in what space do things like meters, seconds, and grams reside?

Since the late nineteenth century, physicists and philosophers alike have sought to say precisely what quantities are and what role dimensionality plays in equations of physics and in theory of measurement. Today, discussions more often revolve around understanding the representational status of dimensionful quantities — whether dimensionality is merely a conventional bookkeeping tool, or instead tracks objective quantitative structure, perhaps only up to equivalence under admissible reparameterisations of base units and dimensions(see, e.g.,Skow,2017;Grozier,2020;Sterrett,2021;Jacobs,2024;Jalloh,2025). Untangling all the accounts and long-standing debates would take us too far afield from the purpose of this paper, and, that being said, even my honest physicist attempt would most likely not do the subject proper justice. For that reason I will humbly point the reader to other excellent historical overviews such asde Boer(1995),Roche(1998),Mitchell(2017), andDe Clark(2017).

Let us instead seize the luxury of brevity to jump right into action.

One outstanding problem in dimensional analysis today is the question of structural foundation. While the basic rules of quantity calculus are somewhat uncontroversial (add only like dimensions, multiplication of units adds their exponents, equations must be dimensionally homogeneous), the literature lacks consensus where exactly these properties are mathematically rooted. Several attempts exist: modern takes likeJanyška, Modugno and Vitolo(2007,2010),Tao(2012),Domotor(2017),Raposo(2018), andZapata-Carratalá(2022)have put forward specialised axiomatic models, but these approaches often take some version of the quantity algebra as primitive, rather than explaining it as an instance of a broader structure already familiar from physics. Multiplying mathematical definitions can at times contribute to shrouding physical intuition, leaving the physicist faintly unsatisfied. Dimensional analysis — a discipline whose strength lies in its closeness to physical intuition — is by no means immune to this pitfall. Burying dimensional analysis under a mountain of mathematical sediment for purely structural purposes therefore misses the mark; what gain is there when the soil does not nourish the roots? One would hope that an encompassing mathematical foundation ought not merely to recover said intuition, but to illuminate and more importantlyfurtherit. We need not look far to achieve this. In fact, I hope to persuade the reader that there is no need to reinvent the wheel at all, and that the mathematical foundation for dimensional analysis has already been well-established and employed in physics for many decades. My message is precisely this:

Dimensional analysis can be wholly understood as a gauge theory.

The paper is organised as follows: inSection2I detail how dimensional analysis reads as a gauge theory in the language of principal fibre bundles. Since the basic structure involves an abelian group (isomorphic toℝ+k\mathbb{R}_{+}^{k}withk∈ℕk\in\mathbb{N}),222I denoteℝ+\mathbb{R}_{+}as the Lie group of positive reals with multiplication as group operation. Some literature may prefer the notationℝ>0\mathbb{R}_{>0}orℝ+\mathbb{R}^{+}.I will draw several parallels toU​(1)kU(1)^{k}gauge theory along the way. InSection3I explain how the gauge theory description also accommodates units that vary in spacetime — a convention often discussed in the context of gravitational theories but nevertheless left out in most dimensional analysis literature. InSection4I discuss how Stevens’s classification of scales of measurement can be accounted for by the choice of structure group, yielding a gauge-theoretic distinction between notions of dimensionless and unit-invariant quantities. Finally, inSection5, I show how the infamoustheorem10can be understood from a gauge theory perspective. Importing it back into the context of gauge theory, I then discuss several examples and applications of the analogous version of thetheorem10for general (including non-abelian) gauge theories.

## 2Dimensional Analysis as a Gauge Theory

In this section I outline how dimensional analysis can be viewed as a gauge theory. I expect that the reader may find the mathematics presented here suspiciously elementary (in fact, it could just as well be used as a basic reminder of the mathematics of gauge theory). This is meant to reinforce the point that nothing exotic is required; all key features of dimensional analysis and quantity calculus will follow from very basic definitions and properties of fibre bundles and representation theory, paralleling the physicist’s way of introducing ordinary gauge theory relevant to particle physics. That being said, my intention is by no means to undermine the core message and perspective that is being conveyed. Notions such as unit ‘transformations’, ‘-independence’, and ‘choosing a basis of units’ become exact mirrors of gauge ‘transformations’, ‘-invariance’, and ‘-fixing’. Notwithstanding, I daresay most theoretical physicists today find discussions of units much less palatable than discussions of gauge theory. Today there is widespread culture and convention in theoretical physics to set all base units equal to 1 in order to circumvent the hassle of keeping track of units altogether. Yet, we are all taught cautionary tales about how “gauge-fixing too early” can obstruct our physical understanding.333Consider for example classical electromagnetism whereA0A_{0}plays the role of a Lagrange multiplier imposing Gauß’s law∇→⋅E→=ρ\vec{\nabla}\cdot\vec{E}=\rho. If one picks temporal gaugeA0=0A_{0}=0beforevarying the action, this removes the constraint and Gauß’s law is no longer enforced.Fixing units from the get-go can in certain cases also lead one astray. An example of this was highlighted inKaramitsos and Muntz(2025)in the context of the Swampland Programme, which sparked the idea to pursue this work.

Now, just as the concept of symmetries is inseparable from gauge theory, the role of symmetries in dimensional analysis has always been lurking on the surface since its historical origin.Fourier(1878)recognised early on that dimensional homogeneity should be understood as the requirement that an equation remains valid under changes of units; when a base unit is replaced by a rescaled one, numerical values transform by definiteconversion factors, and “dimensions” encode the exponents governing this transformation(De Clark,2017). This perspective later became central in the nineteenth-century development of dimensional formulae, where these were used to organise unit conversion and systems of measurement. Put this way, changing units is in broad strokes a symmetry of representation. ‘Conversion factors’ are emphasised here because they are arguably more universal than the numerical coefficients of quantities: translating a length expressed in, say, metres to feet requires only a single scale factor that applies uniformly across any numerical input. The freedom to rescalekkindependent base units can accordingly be encoded in the multiplicative groupℝ+k\mathbb{R}_{+}^{k}. The presence of a group structure, however, does not in itself lend credence to a gauge theory prescription. Most elementary discussions of dimensional analysis stop at a single, global choice of scale. As I will further argue inSection3, there is no reason to impose that restriction from the outset. Imagine a world where Europe and the US were two isolated regions with no communication between their respective residents — Europeans could go about using metric units completely unaware that their friends across the pond enjoy Imperial units instead. Only upon bridging the gap need we be mindful how to convert our measurements so that we may understand one another. Luckily we do not live in such a world. It does, however, exemplify an important detail: the choice of unit is evidentlylocal. Organising the freedom to make such a local choice of scale and compare choices on overlaps is precisely what a principal bundle is for.444I should also acknowledge that much of my thinking has been influenced by conformal geometry as explained inCurry and Gover(2018). Here, an object of interest is𝒬⊂S2​T∗​M{\mathcal{Q}\subset S^{2}T^{*}M}, the bundle of symmetric(0,2)(0,2)-tensorsggonMM, where allggbelong to the same conformal equivalence class[g][g]. That is,g∼g′g\sim g^{\prime}if they are related by a Weyl transformationg′=Ω2​gg^{\prime}=\Omega^{2}gwhereΩ2\Omega^{2}is some positive function onMM. This has the structure of a principalℝ+\mathbb{R}_{+}-bundle (also known as a ray subbundle)𝒬→𝒢→M\mathcal{Q}\to\mathcal{G}\to Mwhere locally𝒢≃U×{g}\mathcal{G}\simeq U\times\{g\}, i.e. the fibre of𝒢\mathcal{G}contains only the representativeggof[g][g]. Note that there is no unique choice of𝒢\mathcal{G}since one can pick anyg~∈[g]\tilde{g}\in[g]as the representative. Still, they all lead to isomorphic bundle structures. A ‘choice of scale’ on a conformal manifold can be related to a choice of unit, as also alluded to inKaramitsos and Muntz(2025)and later inSection3.1.This motivates the following basic definition.

## Definition 1.

Thescale bundleis a principalℝ+k\mathbb{R}_{+}^{k}-bundleP→MP\to Mfor somek∈ℕk\in\mathbb{N}.

For example, fork=3k=3, we could label eachℝ+\mathbb{R}_{+}by the mechanical base dimensionsM,L,T\mathrm{M,L,T}. The right action of(1,2,1)∈ℝ+3(1,2,1)\in\mathbb{R}_{+}^{3}sends a frame to one in which the length scale is doubled. Note however that, a priori,M,L\mathrm{M,L}, andT\mathrm{T}are just names. One could attach physical meaning to each dimension — e.g.L\mathrm{L}is associated with physical lengths between points on the base manifold — but that is strictly not necessary as far as dimensional analysis is concerned. As a mere calculational tool, the ‘practice of dimensional analysis’ (by this I mean for instance algebraically manipulating dimensionalities or testing an equation for dimensional homogeneity) is indifferent to what the base dimensions are called or what they physically represent. Moreover, any other choice of base dimensions, sayM,L\mathrm{M,L}, andV=LT−1\mathrm{V=LT^{-1}}, we can just recognise as a change of basis inℝ+3\mathbb{R}_{+}^{3}. These arguments generalise to anykk.

Notice also that the element(1,2,1)∈ℝ+3(1,2,1)\in\mathbb{R}_{+}^{3}in the above example does more than just double lengths: it scales areas by four, volumes by eight, and so on. How is this accounted for? The common strategy employed by many models of dimensional analysis, including some mentioned previously in the introduction, is to functorially carry over the appropriate transformation properties by engineering quantities such as areas and volumes as ‘tensor powers’ (integer or rational555Another common disposition in the dimensional analysis literature is to consider only quantities whose units are raised to rational powers.Raposo(2019, p. 71)even goes as far as to argue that the reals are “unnecessarily oversized” and in fact integers are entirely sufficient. I find this propensity confusing and surmise that this modelling choice stems from the fact that most physics disciplines only ever encounter rational powers in practice (in particular classical mechanics, where there is a long tradition of applying dimensional analysis). But again, as far as dimensional analysis as a calculational tool is concerned, nothing is stopping us from manipulating e.g. a length to some irrational power. A comment underTao’s blog post also rightfully points out that irrational powers do in fact show up in physics: for CFT two-point functions, schematically∼(length)−2​Δ\sim(\text{length})^{-2\Delta}, the scaling dimensionΔ\Deltacan be non-rational (and is in practice not expected to be rational). Restricting toℤ\mathbb{Z}orℚ\mathbb{Q}thus reads more like artificial aesthetics rather than inferred by some underlying physical principle. The gauge theory picture renders this commitment unnecessary.) of lengths. This enforces the correct scaling by splitting quantities of different dimensions into a proliferating family of distinct bundles or graded components. Subsequently, one stipulates a coherence principle (functor) that makes the same scale or unit transformation act compatibly on all of them. That is, it manufactures the simultaneity rather than explaining it.
Turning to the gauge theory point of view, the interpretation is somewhat different. Now is a good time to make an analogy withU​(1)U(1)gauge theory. Under the group action by some elementei​θ∈U​(1)e^{i\theta}\in U(1), one field (i.e. a section of a vector bundle associated with the principalU​(1)U(1)-bundle) may pick up a phaseϕ↦ei​α​θ​ϕ\phi\mapsto e^{i\alpha\theta}\phiand anotherψ↦ei​β​θ​ψ\psi\mapsto e^{i\beta\theta}\psi, withα≠β\alpha\neq\beta. Any physicist will perhaps appreciate at a basic level that this is becauseϕ,ψ\phi,\psipossess differentU​(1)U(1)charges. Put in more mathematical terms, what is really meant is thatϕ\phiandψ\psitransform under differentweighted representationsofU​(1)U(1). My claim is that it is natural to think similarly about the dimensionality of quantities: two quantities whose dimensionalities are e.g.Lα\mathrm{L}^{\alpha}andLβ\mathrm{L}^{\beta}simply transform under different weighted representations ofℝ+k\mathbb{R}_{+}^{k}. They have “different charges” under scale transformations.666In the language ofGomes(2024,2025), here I am adopting a symmetry-first perspective of gauge theory. Alternatively, one could explore dimensional analysis in a geometry-first formulation, where the symmetry group manifests as the automorphisms of the internal geometry. While it is unclear to me at the present moment whether this presents any merit parallelingGomes’s account of the Standard Model, I find the option very interesting.

That being said, there are subtle differences between dimensional analysis and itsU​(1)U(1)counterpart. Becauseℝ+k\mathbb{R}_{+}^{k}is contractible, any principalℝ+k\mathbb{R}_{+}^{k}-bundle over a paracompact manifold is (topologically) trivial. In other words, any local trivialisation extends to a global trivialisationP≃M×ℝ+kP\simeq M\times\mathbb{R}_{+}^{k}. Although we lose some of the interesting structure and properties of fibre bundles, the picture still remains conceptually useful. Perhaps it is even a benefit, as it distinguishes dimensional analysis from other gauge theories we usually encounter in physics: there is no charge quantization, no monopoles/instantons, and representations classify flat connections up to gauge. A particle physicist may likely label dimensional analysis as the most boring gauge theory.

Now, withG=ℝ+kG=\mathbb{R}_{+}^{k}as our Lie group, its Lie algebra is𝔤≃ℝk\mathfrak{g}\simeq\mathbb{R}^{k}. Viewing𝔤\mathfrak{g}as an additive group, the log map is a smooth Lie group isomorphism.log:G⟶𝔤(g1,…,gk)⟼(log⁡g1,…,log⁡gk)\begin{split}\log\colon\qquad\qquad\quad G&\longrightarrow\mathfrak{g}\\
(g_{1},\dots,g_{k})&\longmapsto(\log g_{1},\dots,\log g_{k})\end{split}(2.1)

Charges then live in what is known as the weight space.

## Definition 2.

Theweight spacerelated to the scale bundle is the dual vector space𝔤∗=Homℝ​(𝔤,ℝ)\mathfrak{g}^{*}=\mathrm{Hom}_{\mathbb{R}}(\mathfrak{g},\mathbb{R}). Aweightw∈𝔤∗w\in\mathfrak{g}^{*}defines a one-dimensional representationρw:ℝ+k→ℝ+⊂GL​(1,ℝ)\rho_{w}\colon\mathbb{R}_{+}^{k}\to\mathbb{R}_{+}\subset\mathrm{GL}(1,\mathbb{R})given byρw​(g)=exp⁡(w​(log⁡g))\rho_{w}(g)=\exp(w(\log g))forg∈ℝ+kg\in\mathbb{R}_{+}^{k}.

Consider again the example wherek=3k=3. The representation corresponding to the weightw=(w1,w2,w3)∈𝔤∗≃ℝ3w=(w_{1},w_{2},w_{3})\in\mathfrak{g}^{*}\simeq\mathbb{R}^{3}mapsg=(g1,g2,g3)∈ℝ+3g=(g_{1},g_{2},g_{3})\in\mathbb{R}_{+}^{3}toρw​(g)=ew​(log⁡g)=g1w1​g2w2​g3w3\rho_{w}(g)=e^{w(\log g)}=g_{1}^{w_{1}}g_{2}^{w_{2}}g_{3}^{w_{3}}(2.2)

which is the appropriate scale factor associated to a quantity with dimensionality(w1,w2,w3)(w_{1},w_{2},w_{3}).

Returning to the case ofU​(1)U(1)(and also other non-trivial Lie groups), one has to be slightly more careful in identifying the set of possible charges. Although anyλ∈𝔤∗\lambda\in\mathfrak{g}^{*}defines a Lie algebra representation, only some exponentiate to global charactersχ:U​(1)→ℂ×\chi\colon U(1)\to\mathbb{C}^{\times}. Compactness implies a bounded image, and thus only the subset𝔴∗⊂𝔤∗\mathfrak{w}^{*}\subset\mathfrak{g}^{*}that is integral onker(exp:𝔤→G)\mathrm{ker}(\exp\colon\mathfrak{g}\to G)is compatible with the global topology. ForU​(1)U(1)the weights lie on a lattice𝔴∗≃ℤ\mathfrak{w}^{*}\simeq\mathbb{Z}which is why charges become quantized. Forℝ+\mathbb{R}_{+}the exponential map is a global diffeomorphism with trivial kernel, so any suchλ\lambdaexponentiates to a global character, i.e.𝔴∗=𝔤∗\mathfrak{w}^{*}=\mathfrak{g}^{*}.

The fact that charges effectively add up under multiplication then follows from basic representation theory.

## Lemma 3.

Letw,w′∈𝔤∗w,w^{\prime}\in\mathfrak{g}^{*}andρw,ρw′\rho_{w},\rho_{w^{\prime}}be the corresponding one-dimensional representations. Thenρw⊗ρw′≃ρw+w′\rho_{w}\otimes\rho_{w^{\prime}}\simeq\rho_{w+w^{\prime}}.

## Proof.

Forg∈Gg\in Gwe can simply compute(ρw⊗ρw′)​(g)=ρw​(g)​ρw′​(g)=ew​(log⁡g)​ew′​(log⁡g)=e(w+w′)​(log⁡g)=ρw+w′​(g).(\rho_{w}\otimes\rho_{w^{\prime}})(g)=\rho_{w}(g)\rho_{w^{\prime}}(g)=e^{w(\log g)}e^{w^{\prime}(\log g)}=e^{(w+w^{\prime})(\log g)}=\rho_{w+w^{\prime}}(g)\,.(2.3)

∎

In the previous discussion I motivated how one can get away with thinking about quantities like charged fields in ordinary gauge theory. Let us intuit this structural equivalence from another perspective by consideringPoincaré’s famous thought experiment. For the sake of conciseness I provide here only a compact version, however a more elaborate account can be found inPoincaré(1906)(see alsoJalloh,2025): imagine you wake up one morning in a world where every physical realisation of length has uniformly become a thousand times greater, with no additional mark left behind. Would you notice? Empirically speaking, the answer to this question appears to be no, since every comparative statement producing dimensionless observables would return the exact same output.Jalloh(2025)labels this as exhibiting anontic symmetry: there is a transformation which changes the numerical representatives of quantities for any given unit system while leaving their ratios unchanged. Descriptions related by such a transformation should therefore be treated as equivalent, insofar as the transformation generates an empirically indistinguishable system. Notwithstanding, once we turn to the language of fibre bundles,Poincaré’s thought experiment receives a straightforward reinterpretation. Imagine (as an inhabitant on the scale bundle) you wake up one morning and overnight someone has performed a right action of an elementg∈ℝ+kg\in\mathbb{R}_{+}^{k}, sendingp↦p⋅gp\mapsto p\cdot gfor an original choice of framep∈Pp\in P. Ifq∈ℝq\in\mathbb{R}denotes a putative numerical representative of a weight-wwquantity, then the overnight transformationp↦p⋅gp\mapsto p\cdot gis equivalently representable by a corresponding rescaled numberρw​(g)​q\rho_{w}(g)q(an active scale transformation). Using some suggestive notation, allow me to write this identification or equivalence relation as[p⋅g,q]∼[p,ρw​(g)​q].[p\cdot g,q]\sim[p,\rho_{w}(g)q]\,.(2.4)

That is just the intrinsic property of an associated bundle!

## Definition 4.

Given the weighted representationρw\rho_{w}we define the associated line bundleℒw=P×ρwℝ\mathcal{L}_{w}=P\times_{\rho_{w}}\mathbb{R}. Aquantity of weightwwis a sectionQ∈Γ​(ℒw)Q\in\Gamma(\mathcal{L}_{w}).

The definition above considers quantities asℝ\mathbb{R}-valued sections. This of course does not accommodate all of physics. The velocity vector, Maxwell tensor, Dirac spinor, and so on, are not scalars but can nevertheless be dimensionful. Rest assured that the definition is easily generalised. It goes as follows: let𝒱\mathcal{V}be anℝ\mathbb{R}-vector space (or more generally over any field𝔽⊇ℝ\mathbb{F}\supseteq\mathbb{R}) and𝒱​M\mathcal{V}Mits vector bundle over the base manifoldMM. Define𝒱\mathcal{V}-valued quantities of weightwwas sections of𝒱​M⊗ℒw\mathcal{V}M\otimes\mathcal{L}_{w}. As such, it entirely suffices to work at the level ofℒw\mathcal{L}_{w}. I will therefore stick to real quantities for simplicity and to stay close to default discussions of dimensional analysis.

In the global trivializationP≃M×ℝ+kP\simeq M\times\mathbb{R}_{+}^{k}, a section ofℒw\mathcal{L}_{w}is equivalent to an equivariant functionq:P→ℝq\colon P\to\mathbb{R}such thatq​(p⋅g)=ρw​(g)−1​q​(p)q(p\cdot g)=\rho_{w}(g)^{-1}q(p)for allp∈Pp\in Pandg∈ℝ+kg\in\mathbb{R}_{+}^{k}. Whenw=0w=0we say that the quantity isdimensionless(invariant under the fibre action).777Note that a quantity being dimensionless does not necessarily imply that it is unit-invariant. This subtlety is discussed in more detail inSection4.

## Lemma 5.

Consider the scale bundleP→MP\to Mand letρw\rho_{w}denote any one-dimensional representation as above. The space of smooth equivariant functions is isomorphic to the space of smooth sectionsΓ​(ℒw)\Gamma(\mathcal{L}_{w}).

## Proof.

Given an equivariantq:P→ℝq\colon P\to\mathbb{R}defineQ​(π​(p))=[p,q​(p)]Q(\pi(p))=[p,q(p)]in the associated bundle; equivariance ensures the element[p,q​(p)][p,q(p)]is independent of the choice of representative in the fibre. Conversely, any representative of a section in a trivialization gives an equivariant function.
∎

We do not have to look far to realise that quantities defined as above obey the well-known algebraic rules of dimensional analysis. They again follow from basic representation theory.

## Proposition 6.

Properties of quantity calculus follow naturally.
- a)

IfQ,Q′Q,Q^{\prime}are quantities of weightw,w′w,w^{\prime}, thenQ​Q′QQ^{\prime}is a quantity of weightw+w′w+w^{\prime}.
- b)

IfQ,Q′Q,Q^{\prime}are quantities of weightww, thenQ+Q′Q+Q^{\prime}is a quantity of weightww.
- c)

One can only add/subtract quantities of equal weight (dimensional homogeneity).

## Proof.

WriteQ=[p,q​(p)]Q=[p,q(p)]andQ′=[p,q′​(p)]Q^{\prime}=[p,q^{\prime}(p)]. By invokingLemma5we can work at the level of the equivariant functionsq,q′q,q^{\prime}. One by one:
- a)

SupposeQ∈Γ​(ℒw)Q\in\Gamma(\mathcal{L}_{w})andQ′∈Γ​(ℒw′)Q^{\prime}\in\Gamma(\mathcal{L}_{w^{\prime}}).q​(p⋅g)​q′​(p⋅g)=ρw​(g)−1​ρw′​(g)−1​(q​(p)​q′​(p))=ρw+w′​(g)−1​(q​(p)​q′​(p))\begin{split}q(p\cdot g)q^{\prime}(p\cdot g)&=\rho_{w}(g)^{-1}\rho_{w^{\prime}}(g)^{-1}(q(p)q^{\prime}(p))\\
&=\rho_{w+w^{\prime}}(g)^{-1}(q(p)q^{\prime}(p))\\
\end{split}(2.5)

Hence(q​q′)​(p)≔q​(p)​q′​(p)(qq^{\prime})(p)\coloneqq q(p)q^{\prime}(p)corresponds to a quantityQ​Q′∈Γ​(ℒw+w′)QQ^{\prime}\in\Gamma(\mathcal{L}_{w+w^{\prime}}).
- b)

Bilinearity inℝ\mathbb{R}as a real vector space carries over to bilinearity inℒw\mathcal{L}_{w}. Leta,b∈ℝa,b\in\mathbb{R}andQ,Q′∈Γ​(ℒw)Q,Q^{\prime}\in\Gamma(\mathcal{L}_{w}).a​q​(p⋅g)+b​q′​(p⋅g)=ρw​(g)−1​(a​q​(p)+b​q′​(p))\begin{split}aq(p\cdot g)+bq^{\prime}(p\cdot g)&=\rho_{w}(g)^{-1}(aq(p)+bq^{\prime}(p))\end{split}(2.6)

Thusa​Q+b​Q′∈Γ​(ℒw)aQ+bQ^{\prime}\in\Gamma(\mathcal{L}_{w}).
- c)

Homogeneity follows from the fact that quantities of different dimensionality simply live in different spaces. IfQ∈Γ​(ℒw)Q\in\Gamma(\mathcal{L}_{w})andQ′∈Γ​(ℒw′)Q^{\prime}\in\Gamma(\mathcal{L}_{w^{\prime}})withw≠w′w\neq w^{\prime}, addition between them is mathematically ill-defined.

∎

There is also a more operational way to understand dimensionful quantities from the gauge-theoretic perspective. Consider for instancecc, the speed of light. Viewed as a quantity in its own right, with non-zero weightswL=1w_{\mathrm{L}}=1andwT=−1w_{\mathrm{T}}=-1, we have demonstrated that it (and any other speed for that matter) can be interpreted as a particular section of a weighted line bundle. But the speed of light also serves another purpose; as often brought to bear in relativistic physics, it can equivalently be viewed as a mapt↦c​tt\mapsto ctsending time intervals to length intervals, or vice versax↦x/cx\mapsto x/clength into time. This is close to whatJacobs(2023b)has described as aninter-quantity relation: a dimensionful constant articulates how distinct families of quantities (time and length in the example involvingcc) are related in a way that is stable under changes of scale. Weighted line bundles manifestly embody this intuition.

## Corollary 7.

An equivalent way to view quantities is as homomorphisms between weighted line bundles, since homomorphismsℒw→ℒw+w′\mathcal{L}_{w}\to\mathcal{L}_{w+w^{\prime}}correspond to pointwise multiplication by a section ofℒw′\mathcal{L}_{w^{\prime}}.

It is important to remark that any trivialisationφ:M→P\varphi\colon M\to Pof the scale bundle naturally induces a canonical sectionμ=[φ,1]\mu=[\varphi,1]in the associated bundleℒw+≔P×ρwℝ+.\mathcal{L}_{w}^{+}\coloneqq P\times_{\rho_{w}}\mathbb{R}_{+}\,.(2.7)

In other words,μ\mucan be viewed as a strictly positive weight-wwquantity. Notice now the isomorphismΓ(ℒw)≃/∼(C∞​(M,ℝ)×Γ​(ℒw+))\Gamma(\mathcal{L}_{w})\simeq{}^{\displaystyle\left(C^{\infty}(M,\mathbb{R})\times\Gamma(\mathcal{L}_{w}^{+})\right)}{\big/\penalty 50}_{\displaystyle\sim}(2.8)

where the quotient identifies(Π,μ)∼(λ−1​Π,λ​μ)(\Pi,\mu)\sim(\lambda^{-1}\Pi,\lambda\mu)forλ∈C∞​(M,ℝ+)\lambda\in C^{\infty}(M,\mathbb{R}_{+}). I highlight this isomorphism for the following observation: provided aμ∈Γ​(ℒw+){\mu\in\Gamma(\mathcal{L}_{w}^{+})}(for instance induced by a trivialisationφ\varphi), any quantityQ∈Γ​(ℒw)Q\in\Gamma(\mathcal{L}_{w})can be written uniquely asQ=Π​μQ=\Pi\mu(2.9)

for a unique smooth functionΠ∈C∞​(M,ℝ)≃Γ​(ℒ0)\Pi\in C^{\infty}(M,\mathbb{R})\simeq\Gamma(\mathcal{L}_{0}). Moreover, becauseμ\muis everywhere non-vanishing, the map is invertible; the ratioΠ=Q/μ\Pi=Q/\muis also well-defined. The reader may recognise this as the familiar metrological picture in which a quantity is expressed as a number-unit pair! WritingQ=[p,q]Q=[p,q], the numerical coefficientΠ\Piis related to the equivariantqqby888Note that, whileΠ\Piis a function onMMrather thanPP, it transforms underφ↦φ​g\varphi\mapsto\varphi gasΠ​(x)↦ρw​(g)−1​Π​(x)\Pi(x)\mapsto\rho_{w}(g)^{-1}\Pi(x)due to equivariance ofqq. This is just the passive transformation ensuringQ=Π​μQ=\Pi\,\muis invariant under the group action.Π=q∘φ.\Pi=q\circ\varphi\,.(2.10)

In fact, because the associated bundleℒw+\mathcal{L}_{w}^{+}is just the extension of the structure group ofPPalong the homomorphismρw:ℝ+k→ℝ+\rho_{w}\colon\mathbb{R}_{+}^{k}\to\mathbb{R}_{+}, it is also itself a principalℝ+\mathbb{R}_{+}-bundle, with right action given by scale factors[p,q]⋅ρw​(g)=[p,ρw​(g)​q][p,q]\cdot\rho_{w}(g)=[p,\rho_{w}(g)q]. Fork=1k=1andw≠0w\neq 0,ρw\rho_{w}is an isomorphism, soP≃ℒw+P\simeq\mathcal{L}_{w}^{+}is just the scale bundle itself; the structure group has been relabelled throughρw\rho_{w}. Moreover, sectionsμ∈Γ​(ℒw+)\mu\in\Gamma(\mathcal{L}_{w}^{+})become trivialisations ofPP.

Finally, we are able to return to the riddle posed in the introduction of this paper:

Where do units live?

We now have the answer:

A unit is a sectionμ∈Γ​(ℒw+)\mu\in\Gamma(\mathcal{L}_{w}^{+}).

Or equivalently, fork=1k=1, a trivialisation of the scale bundle — units arechoices of gauge.

Fork>1k>1, one has to be slightly more careful. In this caseρw\rho_{w}has non-trivial kernel andℒw+\mathcal{L}_{w}^{+}remembers only a one-dimensional quotient of the full scale bundle. I.e.P≄ℒw+P\not\simeq\mathcal{L}_{w}^{+}for anywwifk>1k>1. If we wanted to reconstruct the scale bundle, we would needkknon-degenerate associated bundles. The picture is again familiar from dimensional analysis: suppose we havekkbase dimensionalities (e.g.M,L,T,…\mathrm{M},\mathrm{L},\mathrm{T},\dots), we need to specifykklinearly independent base units (e.g.1kg,1m,1s,…$1\text{\,}\mathrm{kg}$,$1\text{\,}\mathrm{m}$,$1\text{\,}\mathrm{s}$,\dots) in order to parameterise any dimensionful quantity. When there are either fewer units than dimensions or they are degenerate, this is clearly not possible. With more units than dimensions it is on the other hand possible, but the decomposition is no longer unique(Jacobs,2024).

## Proposition 8.

LetP→MP\to Mbe the scale bundle andw1,…,wn∈𝔤∗w_{1},\dots,w_{n}\in\mathfrak{g}^{*}for somen∈ℕn\in\mathbb{N}. The mapΦ:P→ℒw1+×M⋯×Mℒwn+p↦([p,1],…,[p,1])\begin{split}\mathsf{\Phi}\colon\quad P&\to\mathcal{L}_{w_{1}}^{+}\times_{M}\cdots\times_{M}\mathcal{L}_{w_{n}}^{+}\\
p&\mapsto([p,1],\dots,[p,1])\end{split}(2.11)

is a smooth bundle morphism. It is an isomorphism iff{w1,…,wn}\{w_{1},\dots,w_{n}\}forms a complete basis of𝔤∗\mathfrak{g}^{*}. Equivalently, iff the character mapχ:G→ℝ+ng↦(ρw1​(g),…,ρwn​(g))\begin{split}\chi\colon\quad G&\to\mathbb{R}^{n}_{+}\\
g&\mapsto(\rho_{w_{1}}(g),\dots,\rho_{w_{n}}(g))\end{split}(2.12)

is a Lie group isomorphism.

## Proof.

ComputeΦ​(p​g)=([p​g,1],…,[p​g,1])=([p,ρw1​(g)],…,[p,ρwn​(g)])=Φ​(p)⋅χ​(g)\begin{split}\mathsf{\Phi}(pg)&=([pg,1],\dots,[pg,1])\\
&=([p,\rho_{w_{1}}(g)],\dots,[p,\rho_{w_{n}}(g)])\\
&=\mathsf{\Phi}(p)\cdot\chi(g)\end{split}(2.13)

where the last equality indicates the character acting diagonally from the right. SoΦ\mathsf{\Phi}isGG-equivariant after transporting theGG-action throughχ\chi. Ifχ\chiis an isomorphism, thenΦ\mathsf{\Phi}becomes a bundle morphism between two principalGG-bundles.
Next we need to show that this is equivalent to saying{w1,…,wn}\{w_{1},\dots,w_{n}\}must be a complete basis of𝔤∗\mathfrak{g}^{*}. Consider therefore the mapW:𝔤→ℝnW\colon\mathfrak{g}\to\mathbb{R}^{n}withW​(X)≔(w1​(X),…,wk​(X))W(X)\coloneqq(w_{1}(X),\dots,w_{k}(X))such thatχ=exp∘W∘log\chi=\exp\circ W\circ\log. Sincelog\logandexp\expare diffeomorphisms,χ\chiis an isomorphism iffWWis a linear isomorphism. But that is only the case iff{w1,…,wn}\{w_{1},\dots,w_{n}\}is a complete basis of𝔤∗\mathfrak{g}^{*}. (And so necessarilyn=k=dim​𝔤∗n=k=\mathrm{dim}\,\mathfrak{g}^{*}.) This completes the proof.
∎

Provided{w1,…,wk}\{w_{1},\dots,w_{k}\}forms a complete basis of𝔤∗\mathfrak{g}^{*}, any trivialisationφ\varphiofPPcorresponds, viaProposition8, to a sectionμ=(μ1,…,μk)∈Γ​(ℒw1+×M⋯×Mℒwk+)\mu=(\mu_{1},\dots,\mu_{k})\in\Gamma(\mathcal{L}_{w_{1}}^{+}\times_{M}\cdots\times_{M}\mathcal{L}_{w_{k}}^{+})(2.14)

withμi=[φ,1]\mu_{i}=[\varphi,1]for alli=1,…,ki=1,\dots,k. In more basic terms we could call(μ1,…,μk)(\mu_{1},\dots,\mu_{k})a choice ofbase units.
It follows that we can always decompose any dimensionful quantity in terms of a choice of base units.

## Corollary 9.

Let{wi}i=1,…,k\{w_{i}\}_{i=1,\dots,k}be a complete basis of𝔤∗\mathfrak{g}^{*}and{μi}i=1,…,k\{\mu_{i}\}_{i=1,\dots,k}be a choice of base units. For everyv∈𝔤∗v\in\mathfrak{g}^{*}and every quantityQ∈Γ​(ℒv)Q\in\Gamma(\mathcal{L}_{v})there exists a unique set of real numbersri∈ℝr_{i}\in\mathbb{R}and a unique smooth functionΠ∈Γ​(ℒ0)≃C∞​(M,ℝ)\Pi\in\Gamma(\mathcal{L}_{0})\simeq C^{\infty}(M,\mathbb{R})such thatQ​(x)=Π​(x)​∏i=1k(μi​(x))ri.Q(x)=\Pi(x)\prod_{i=1}^{k}(\mu_{i}(x))^{r_{i}}\,.(2.15)

Overall, we have shown how dimensionalities, units, quantity calculus, and the number-unit decomposition immediately manifest once we recognise dimensional analysis as a gauge theory. It is useful to summarise some important notions:itemBase dimensionalities:

a choice of basis{wi}\{w_{i}\}on𝔤∗\mathfrak{g}^{*}.itemBase units:

a section of the product bundle∏iℒwi+\prod_{i}\mathcal{L}_{w_{i}}^{+}or, equivalently, a trivialisation of the scale bundle.

Let me thereby highlight that imposing a set of base units is (by following the isomorphism (2.11)) precisely the same as choosing a gauge. A global basis of units always exists becausePPis trivial.

Within this construction, base dimensionalities are logically prior to base units in a precise structural sense (echoingSterrett(2021)). To specify base unitsμi∈Γ​(ℒwi+)\mu_{i}\in\Gamma(\mathcal{L}_{w_{i}}^{+})already presupposes weightswiw_{i}, and these sections determine a trivialisation of the scale bundle only when the{wi}i=1,…,k\{w_{i}\}_{i=1,\dots,k}form a basis of𝔤∗\mathfrak{g}^{*}. Thus a system of base units is a choice of sections associated with a prior choice of base dimensionalities.

Let me close this section with one brief comment on related mathematical accounts of dimensional analysis. It is intentional that I have not attempted a systematic comparison with such approaches here. Still, it is worth acknowledging that other authors have not been very far from the structure used above.Tao(2012)andDomotor(2017), for instance, both motivate and make contact with the notion ofGG-torsors as an appropriate mathematical framework. From the present point of view, this is not particularly surprising: asBaez(2009)explains beautifully, the fibre of a principalGG-bundleisaGG-torsor. In that sense, while the novel idea of this paper is to thoroughly phrase dimensional analysis as a gauge theory, some of the mathematical ingredients have already appeared in parallel approaches.

For the remainder of the paper, we will explore the conceptual consequences of this account as well as more grounded comparisons with ordinary gauge theory and particle physics.

## 2.1Analogy:U​(1)kU(1)^{k}gauge theory

ConsiderU​(1)kU(1)^{k}gauge theory, which, as a close cousin toℝ+k\mathbb{R}_{+}^{k}, concerns an abelian Lie group of dimensionkk. The fundamental object of interest here is the principalU​(1)kU(1)^{k}-bundle, denotedPU​(1)→MP^{U(1)}\to M, from which we can build things such as complex associated line bundles𝒞w=PU​(1)×ρwℂ\mathcal{C}_{w}=P^{U(1)}\times_{\rho_{w}}\mathbb{C}. Saying thatΨ\Psiis a complex scalar of chargewwjust means that it is a sectionΨ∈Γ​(𝒞w)\Psi\in\Gamma(\mathcal{C}_{w}). This is of course analogous toDefinition4of a dimensionful quantity. (Recall however that the charge in this case is a vectorw=(w1,…,wk)∈ℤkw=(w_{1},\dots,w_{k})\in\mathbb{Z}^{k}, with quantization due to the compactness ofU​(1)kU(1)^{k}.) Likewise, the complex scalarsΨ\Psiare in one-to-one correspondence with equivariant functionsψ:PU​(1)→ℂ\psi\colon P^{U(1)}\to\mathbb{C}. For someg=(ei​θ1,…,ei​θk)∈U​(1)kg=(e^{i\theta_{1}},\dots,e^{i\theta_{k}})\in U(1)^{k}the function transforms asψ​(p​g)=ρw​(g)−1​ψ​(p)=e−i​(w1​θ1+⋯+wk​θk)​ψ​(p).\psi(pg)=\rho_{w}(g)^{-1}\psi(p)=e^{-i(w_{1}\theta_{1}+\cdots+w_{k}\theta_{k})}\psi(p)\,.(2.16)

Now, ifψ\psihas chargewwandψ′\psi^{\prime}has chargew′w^{\prime}, then the productψ​ψ′\psi\psi^{\prime}transforms as a field with chargew+w′w+w^{\prime}. This is again just the statement that tensoring one-dimensional representations adds the charges. Likewise, the sumψ+ψ′\psi+\psi^{\prime}transforms covariantly if and only ifw=w′w=w^{\prime}; otherwise a gauge transformation rotates the two summands out of sync and the sum does not transform by a single overall phase. Dimensional homogeneity is the equivalent statement that substitutes phases for rescaling factors: a linear combination of quantities is ‘gauge-covariant’ if and only if the summands have equal dimensionality.

Given such a complex scalar charged underU​(1)kU(1)^{k}, it is common to see it represented (locally) by a magnitude and a phaseψ=ϱ​ei​ϑ.\psi=\varrho\,e^{i\vartheta}\,.(2.17)

We understand thatϱ=|ψ|\varrho=\absolutevalue{\psi}is gauge-invariant and the phaseei​ϑe^{i\vartheta}transforms under theU​(1)kU(1)^{k}action. In other words, all we have done is splitψ\psiinto a ‘chargeless’ and ‘charged’ piece, akin to how we have seen quantities being written as number-unit pairsQ=Π​μ.Q=\Pi\,\mu\,.(2.18)

Analogously, one could say that the coefficientΠ\Piand unitμ\muare respectively ‘chargeless’ and ‘charged’ with respect to the group of scale transformationsℝ+k\mathbb{R}_{+}^{k}. Allow me to expand further on this correspondence. Although it is rarely ever useful to invoke in particle physics, forU​(1)kU(1)^{k}-charged gauge fields there is a way to decompose the phase into its ‘base phases’. Analogous toProposition8, the mapΦU​(1):PU​(1)→𝒞w1U​(1)×M⋯×M𝒞wkU​(1)p↦([p,1],…,[p,1])\begin{split}\mathsf{\Phi}^{U(1)}\colon\quad P^{U(1)}&\to\mathcal{C}_{w_{1}}^{U(1)}\times_{M}\cdots\times_{M}\mathcal{C}_{w_{k}}^{U(1)}\\
p&\mapsto([p,1],\dots,[p,1])\end{split}(2.19)

where𝒞wU​(1)≔PU​(1)×ρwU​(1)\mathcal{C}_{w}^{U(1)}\coloneqq P^{U(1)}\times_{\rho_{w}}U(1), is also a principal bundle morphism and an isomorphism if{w1,…,wk}\{w_{1},\dots,w_{k}\}is a complete basis of the weight space𝔴∗≃ℤk\mathfrak{w}^{*}\simeq\mathbb{Z}^{k}. It tells us that there is a freedom to linearly decompose the phase ofψ\psiei​ϑ=∏i=1k(ei​ϑi)rie^{i\vartheta}=\prod_{i=1}^{k}\left(e^{i\vartheta_{i}}\right)^{r_{i}}(2.20)

such that, under aU​(1)kU(1)^{k}gauge transformation, each base phase acts like a charge-wiw_{i}objectei​ϑi↦ρwi​(g)−1​ei​ϑie^{i\vartheta_{i}}\mapsto\rho_{w_{i}}(g)^{-1}e^{i\vartheta_{i}}. Writingψ=ϱ​∏i=1k(ei​ϑi)ri\psi=\varrho\prod_{i=1}^{k}\left(e^{i\vartheta_{i}}\right)^{r_{i}}(2.21)

with integerrir_{i}is just theU​(1)kU(1)^{k}analogue ofCorollary9which casts a dimensionful quantity in terms of a set of base units. Note again that the choice of basis is not unique: any other set of base phases{ei​ϑi′}i=1,…,k\{e^{i\vartheta^{\prime}_{i}}\}_{i=1,\dots,k}with weights{wi′}i=1,…,k\{w_{i}^{\prime}\}_{i=1,\dots,k}for whichei​ϑ=∏i(ei​ϑi′)ri′=∏i(ei​ϑi)rie^{i\vartheta}=\prod_{i}\big(e^{i\vartheta_{i}^{\prime}}\big)^{r_{i}^{\prime}}=\prod_{i}\big(e^{i\vartheta_{i}}\big)^{r_{i}}(2.22)

does the same job. The only difference is that this can only be done locally, asU​(1)kU(1)^{k}has non-trivial topology; a local trivialisation does not ascend uniquely to a global one. Because the phases have non-vanishing norm, the ratioϱ=ψ/ei​ϑ\varrho=\psi/e^{i\vartheta}is also well-defined and isolates the gauge-invariant part ofψ\psi. Analogously, dividing by the unit extracts the scale-invariantΠ=Q/μ\Pi=Q/\mu.

## 3On Non-Constant Units

A major practical concern in metrology is the constancy of base units for ensuring replicability of precision measurements and comparisons across experimental settings: when measuring lengths for instance, we would like our reference meter stick to retain its ‘one-meter-ness’ over long periods of time or under different laboratory conditions (temperature, pressure, and so on). That not being the case can blur the physical situation at hand when it comes to interpreting measurement outcomes. Consider a simple thought experiment to illustrate this point. Suppose I wish to measure the mass of a metal cube using a particular glass of water as my reference unit; ‘one glass’ is my standard of mass. The next day I repeat the same measurement and find that the cube’s mass has increased. Presuming the cube was safely stored and left untouched, could it really be the case that it magically gained mass overnight? Of course not. More realistically, some of the water from the glass of water had evaporated overnight, increasing the relative mass ratio. Maybe I got thirsty and took a sip? The apparent change in measurement outcome is simply an artefact of having chosen a reference whose ‘one-glass-ness’ is not stable over time. I could in fact also have run the inverted experiment — measure the mass of the glass of water using the metal cube as a reference unit — and concluded that the glass has lost mass the next day.999The two conclusions manifest from the mathematical fact that, for a ratio of two unknown functionsf1f2\frac{f_{1}}{f_{2}}with∂(f1f2)≠0\partial(\frac{f_{1}}{f_{2}})\neq 0, it is impossible to tell from this information alone whether the variation is due tof1,f2f_{1},f_{2}or both simultaneously. Further deduction requires external insight. For instance, if physical reasoning suggests thatf2f_{2}does not vary much, we can justify that deviations should for the most part be governed byf1f_{1}.This second convention more accurately fits our physical understanding of the situation at hand because the metal cube is the more stable standard. It does not make it illegal to use the glass of water as a measure of mass; it just implies we have to be sufficiently careful and aware about comparing measurement results made at different points in space and time.

The historical development of the meter has been, in effect, an attempt to stop measuring against evaporating glasses of water. From 1799, theMètre des Archivesplatinum bar was used as the material standard for defining the meter, later replaced by the international prototype meter in 1889, which was kept under controlled conditions.(For a concise timeline, seeBIPM,2019, Appendix 4.)Naturally, material standards are vulnerable to small variations over time. They can be scratched, contaminated, stressed, or change subtly under handling and aging. Before 1983, the speed of lightccmeasured inm/s\text{\,}\mathrm{m}\mathrm{/}\penalty 50\mathrm{s}would shift over time due to drifts in metrological standards. This is no longer the case, since the meter is nowdefinedin terms of the distance light travels in a vacuum during a specified fraction of a second. Does this mean the speed of light was a function of time until precisely 1983, after which it magically became constant? Of course not. The apparent change in measurement outcome was, like the metal cube and glass of water thought experiment, an artefact of having chosen a reference unit that was not stable over time.

The discussion so far is by no means to advertise for a particular system of base units as the ‘most stable’ or ‘correct’ one to adopt. In fact, it should not matter at all whether one adopts a constant or non-constant system of units (that is a human choice after all), as long as one knows how to subtract the possible phantom contributions due to how the standard varies in space and time. My intention is rather to point out that non-constant units evidently play a significant role in real-life metrology, and any mathematical foundation of dimensional analysis ought to build them in from the outset. Notwithstanding, many discussions of dimensional analysis in the physics and philosophy literature tacitly assume constant units. There are at least two ways one may assert this:
- 1.

Conduct dimensional analysis on the dummy manifoldM={pt}M=\{\text{pt}\}.
- 2.

Take the stance that genuine unitsmustbe constant.

I think it is fair to claim that traditional dimensional analysis takes place on the point where,ipso facto, the distinction between constant and varying units is invisible. Metrology on an extended manifold is on the other hand much less straightforward; questions such as “is our notion of a meter atx∈Mx\in Mthe same as our notion of a meter atx′∈Mx^{\prime}\in M?” become tricky to address (c.f. the history of the meter). In fact, we recognise the same situation when needing to compare, say, vectors on a manifold: comparing a vectorv∈Tx​Mv\in T_{x}Mwith another vectorv′∈Tx′​Mv^{\prime}\in T_{x^{\prime}}Mcannot be done from afar. That is, one requires a method to parallel transportvvandv′v^{\prime}to the same tangent space and manipulate them there. Applying the same logic to dimensional analysis, what we require is some notion of a ‘connection’ to instruct how to ‘parallel transport’ units and quantities between spacetime points. It should not come as a surprise that the formalism laid out here naturally takes care of this — connections are after all the bread and butter of gauge theory!

In the language of principal bundles, the standard description of parallel transport relies on defining a Lie algebra-valued one-form,ω∈Ω1​(P,𝔤)\omega\in\Omega^{1}(P,\mathfrak{g}), known as an Ehresmann connection. I will not dive deep into its precise definition or properties; the interested reader can consultKobayashi and Nomizu(1963)orGomes(2024, Appendix A). For our purposes a simple picture is sufficient: intuitively, one can imagine that parallel transport onPPtakes place on a distribution of ‘horizontal spaces’H⊂T​PH\subset TPthat fibre-wise look like the tangent space of the base manifold,Hp≃Tπ​(p)​MH_{p}\simeq T_{\pi(p)}M. The splitting ofTp​PT_{p}Pinto its horizontal and complementary ‘vertical’ subspace is a priori arbitrary — it is the Ehresmann connection which assigns a horizontal subspace to each pointp∈Pp\in Pin a way that is compatible with theGG-action onPP.

More important for our purposes is that the connectionω\omegainduces a covariant derivative on the associated bundles. Given any trivialisationφ\varphi, we can pull backω\omegato obtain a Lie algebra-valued one-form on the base manifold,A(φ)≔φ∗​ωA^{(\varphi)}\coloneqq\varphi^{*}\omega. (The physicist may intuit this as the gauge potential.) Then for anyv∈𝔤∗v\in\mathfrak{g}^{*}andQ=Π​μ(φ)∈Γ​(ℒv)Q=\Pi\,\mu^{(\varphi)}\in\Gamma(\mathcal{L}_{v})in the associated bundle, expressed in the frameμ(φ)=[φ,1]\mu^{(\varphi)}=[\varphi,1],∇φQ=(dΠ+v​(A(φ))​Π)⊗μ(φ)∈Ω1​(M,ℒv)\nabla^{\varphi}Q=(\differential\Pi+v(A^{(\varphi)})\Pi)\otimes\mu^{(\varphi)}\in\Omega^{1}(M,\mathcal{L}_{v})(3.1)

is the coordinatised definition for the covariant derivative∇φ\nabla^{\varphi}. In particular, we say thatω\omegaisadaptedtoφ\varphiifA(φ)=0A^{(\varphi)}=0.

Specialising to dimensional analysis, we already saw, followingProposition8, what it means to have a trivialisationφ\varphiof the scale bundle: upon fixing a set of base dimensionalities{wi}i=1,…,k⊂𝔤∗\{w_{i}\}_{i=1,\dots,k}\subset\mathfrak{g}^{*},Φ​(φ)=(μ1,…,μk)\mathsf{\Phi}(\varphi)=(\mu_{1},\dots,\mu_{k})gives a set of base units in the associated bundles,μi∈Γ​(ℒwi+)\mu_{i}\in\Gamma(\mathcal{L}_{w_{i}}^{+}). Suppose therefore that we chose a connection adapted toφ\varphi. Carrying it throughΦ\mathsf{\Phi}implies that∇φμi=0\nabla^{\varphi}\mu_{i}=0on eachℒwi+\mathcal{L}_{w_{i}}^{+}. In other words, adapting the connection to a trivialisationφ:M→P\varphi\colon M\to Pis precisely equivalent tochoosingwhich set of base units are ‘covariantly constant’. IfQ=Π​μ(φ)Q=\Pi\,\mu^{(\varphi)}is expressed in this unit system,∇φQ=dΠ⊗μ(φ).\nabla^{\varphi}Q=\differential\Pi\otimes\mu^{(\varphi)}\,.(3.2)

Let me emphasise this point clearly. There is no privileged system of units that is intrinsically or by definition “constant”. I take here the point of view that variation presumes a fixed background structure and, as such, before determining any rate of change, we must first articulatewhatwe root ourselves against. This is what adapting the connection to some trivialisationφ\varphiachieves: it determines the set of unitsΦ​(φ)=(μ1,…,μk)\mathsf{\Phi}(\varphi)=(\mu_{1},\dots,\mu_{k})that we treat as constant via the property that∇φμi=0\nabla^{\varphi}\mu_{i}=0. Put bluntly, no unit varies against itself. InSection2we found that dimensionalities are logically prior to units; prolonging that line of thought, one can add that units are logically prior toconstantunits.

So let us ask the question: what exactly happened in 1983, when the speed of light ceased to vary and truly ‘became a constant’? On a bundle reading, nothing changed about the speed of light sectionc∈Γ​(ℒwc)c\in\Gamma(\mathcal{L}_{w_{c}}). The answer is simply that we chose to work with a connection adapted to a different trivialisation; one that implies∇φc=0\nabla^{\varphi}c=0.
The same section can appear to be constant in one choice of background units and vary in another, without anything having changed about the underlying quantity. To see this, suppose we pass fromφ\varphito another sectionφg=φ⋅g\varphi^{g}=\varphi\cdot gfor someg:M→Gg\colon M\to G. This gives rise to a different set of base unitsμiφg=μiφ⋅ρwi​(g)=[φ,ρwi​(g)].\mu^{\varphi^{g}}_{i}=\mu^{\varphi}_{i}\cdot\rho_{w_{i}}(g)=[\varphi,\rho_{w_{i}}(g)]\,.(3.3)

Under the group action the connection transforms via101010In general(φg)∗​ω=Ad​(g)−1​φ∗​ω+g−1​dg(\varphi^{g})^{*}\omega=\mathrm{Ad}(g)^{-1}\varphi^{*}\omega+g^{-1}\differential g. As the group is abelian, the adjoint yields the identity. The second term comes from observing thatlog∘χ=W∘log\log\circ\chi=W\circ\log(c.f.Proposition8). Differentiating givesg−1​dg=W−1​(dlog⁡χ​(g))g^{-1}\differential g=W^{-1}(\differential\log\chi(g)).A(φg)=A(φ)+W−1​(dlog⁡ρw1​(g),…,dlog⁡ρwk​(g)).A^{(\varphi^{g})}=A^{(\varphi)}+W^{-1}(\differential\log\rho_{w_{1}}(g),\dots,\differential\log\rho_{w_{k}}(g))\,.(3.4)

Consider then the same weight-vvquantity written in terms of this other set of (non-constant) unitsQ=Π​μ(φ)=Πg​μ(φg)∈Γ​(ℒv)Q=\Pi\,\mu^{(\varphi)}=\Pi^{g}\,\mu^{(\varphi^{g})}\in\Gamma(\mathcal{L}_{v}), withΠg=ρv​(g)−1​Π{\Pi^{g}=\rho_{v}(g)^{-1}\Pi}(c.f.footnote8). Moreover, decomposev=∑iri​wiv=\sum_{i}r_{i}w_{i}in terms of the base dimensionalities. The covariant derivative now picks up a contribution from the fact that the unit itself is no longer constant (more precisely, the conversion factor relating it to the background which the connection is adapted to)∇φQ=(dΠg+Πg​∑iri​dlog⁡ρwi​(g))⊗μ(φg).\nabla^{\varphi}Q=(\differential\Pi^{g}+\Pi^{g}\sum_{i}r_{i}\differential\log\rho_{w_{i}}(g))\otimes\mu^{(\varphi^{g})}\,.(3.5)

Sinceρv​(g)=∏i(ρwi​(g))ri\rho_{v}(g)=\prod_{i}(\rho_{w_{i}}(g))^{r_{i}}, equivariance of the numerical coefficient follows∇φQ=ρv​(g)−1​dΠ⊗μ(φg),\nabla^{\varphi}Q=\rho_{v}(g)^{-1}\differential\Pi\otimes\mu^{(\varphi^{g})}\,,(3.6)

familiar from gauge-covariant derivatives. Structurally, it should be clear that a local unit transformation is precisely a gauge transformation taking us between trivialisationsφ↦φg\varphi\mapsto\varphi^{g}and appropriately transforming the connectionA(φ)↦A(φg)A^{(\varphi)}\mapsto A^{(\varphi^{g})}. Indeed,∇φQ\nabla^{\varphi}Qis also itself a dimensionful (1-form valued) quantity, in the sense that it is a section of the weighted bundleT∗​M⊗ℒvT^{*}M\otimes\mathcal{L}_{v}.

## 3.1On scalar-tensor theories and frame covariance

Although non-constant units have received comparatively little direct attention in the dimensional analysis literature, the closely related problem of spacetime variation of fundamental constants has been extensively discussed in cosmology(Uzan,2025). As cosmologists, we are understandably tempted to ponder whether the reference scales and constants we rely on when it comes to physics here on Earth (the speed of light, Planck’s constant, Newton’s constant, and so on) have varied over cosmic timescales or distances — where any variation might otherwise pass unnoticed in local laboratory settings. Toying with fundamental constants by, for example, promoting them to new dynamical scalars or allowing them to depend on vacuum expectation values of other fields, provides a wide arena in which to address long-standing problems in cosmology; including but not limited to questions surrounding dark matter, dark energy, inflation, and naturalness. This is nothing new. But since gravity plays a central role in these settings, perhaps an instinctive place to start and appreciate the physics is by granting dynamics to the gravitational couplingκ=8​π​G​c−4\kappa=8\pi Gc^{-4}by replacingκ−1↦f​(ϕ)\kappa^{-1}\mapsto f(\phi)whereϕ\phiis some new scalar. Doing so for standard Einstein-Hilbert gravity coupled to matter yields, in the simplest example, a scalar-tensor theory expressed in the so-called Jordan frame,S=∫d4x​−g𝖩​f​(ϕ)2​R𝖩+Sm​[gμ​ν𝖩;ψ].S=\int\differential^{4}x\sqrt{-g_{\mathsf{J}}}\frac{f(\phi)}{2}R_{\mathsf{J}}+S_{\text{m}}[g^{\mathsf{J}}_{\mu\nu};\psi]\,.(3.7)

These theories are often phenomenologically challenged because they introduce light propagating degrees of freedom and by fifth force constraints. In any event, it is maybe not immediately obvious that the action should face these problems, since it does not contain explicitly a kinetic term for the scalarϕ\phi. This is easier to realise after performing a Weyl transformationgμ​ν𝖩⟼gμ​ν𝖤=Ω2​gμ​ν𝖩g^{\mathsf{J}}_{\mu\nu}\longmapsto g^{\mathsf{E}}_{\mu\nu}=\Omega^{2}g^{\mathsf{J}}_{\mu\nu}(3.8)

withΩ2∈C∞​(M,ℝ+)\Omega^{2}\in C^{\infty}(M,\mathbb{R}_{+})some function. For the particular choiceΩ2=f/M2\Omega^{2}=f/M^{2}whereM2M^{2}is some constant with the same dimension asff, the action is put in Einstein frameS=∫d4x​−g𝖤​{M22​R𝖤−34​M2​(f′​(ϕ)f​(ϕ))2​g𝖤μ​ν​∂μϕ​∂νϕ}+Sm​[Ω−2​gμ​ν𝖤;ψ]S=\int\differential^{4}x\sqrt{-g_{\mathsf{E}}}\left\{\frac{M^{2}}{2}R_{\mathsf{E}}-\frac{3}{4}M^{2}\left(\frac{f^{\prime}(\phi)}{f(\phi)}\right)^{2}g_{\mathsf{E}}^{\mu\nu}\partial_{\mu}\phi\partial_{\nu}\phi\right\}+S_{\text{m}}[\Omega^{-2}g^{\mathsf{E}}_{\mu\nu};\psi](3.9)

so that the non-minimal coupling has been exchanged with an explicit kinetic term and a modified matter coupling.

This slight digression on the Einstein and Jordan frame representations is to spotlight how Weyl transformations in gravitational theories inevitably lead us to confront non-constant units. Consider the line elementds2=gμ​ν​dxμ​dxν\differential s^{2}=g_{\mu\nu}\differential x^{\mu}\differential x^{\nu}as a natural candidate for a spacetime ruler and measure of distances. In special relativity, for instance, we know that two observers linked by Lorentz transformations will see the same line element, allowing them to unambiguously share the same spacetime ruler. But, as we have just seen, the situation is more subtle once we look to general relativity. Under a Weyl transformation, the line element is no longer invariant,ds2↦Ω2​ds2\differential s^{2}\mapsto\Omega^{2}\differential s^{2}, and we are now nudged to think in terms of a new (spacetime-dependent) ruler that differs by a scale factorΩ\Omega(see alsoEddington,1921,1923).

Dicke(1962)realised that the passage between the Einstein and Jordan frame can effectively be viewed as — and thereby also undone by — an appropriate unit transformation. That is, working in units of the Planck massMMin Einstein frame yields the same dimensionless ratios when working in units of the couplingf\sqrt{f}in Jordan frame.111111This is further detailed inKaramitsos and Muntz(2025)(see alsoBento et. al.,2025, for a related discussion). We also highlight that there is really no such thing astheEinstein or Jordan frame, as there exist infinitely many smooth families of conformal frames one can choose from. E.g. all Einstein frames are related by the scale transformations that leave the connection (3.4) invariant.The question of whether different conformal frames represent physically indistinguishable theories has been dubbed theframe problem. Although it was arguably resolved byDickealready in1962, the debate somehow prevailed many years later(seeFaraoni, Gunzig and Nardone,1999, Section 3).121212Specifically I am referring to the question of semiclassical equivalence. It remains an open question whether conformal frame equivalence also holds at the quantum level.One attempt to untangle the situation is in the frame-covariant formalism of scalar-tensor theories(Flanagan,2004;Kuusk, Järv and Vilson,2016;Karamitsos and Pilaftsis,2018). There it is noticed that the action can be cast in a way that is manifestly form-invariant under Weyl transformations,S​[g,ϕ,…]=S​[gΩ,ϕΩ,…].S[g,\phi,\dots]=S[g^{\Omega},\phi^{\Omega},\dots]\,.(3.10)

Superscripts denote the Weyl-transformed arguments and the ellipsis is a placeholder for other possible fields, couplings, or model functions of the theory. Form-invariance is therefore also reflected at the level of the equations of motion. This is made manifest by defining the ‘frame-covariant derivative’ meant to replace ordinary derivatives,131313Herewwdenotes the conformal weight, where conventionallyX↦Ω−w​XX\mapsto\Omega^{-w}Xunder Weyl transformations. The metricg↦Ω2​gg\mapsto\Omega^{2}gthus has weight−2-2. Note thatXXin the original definition is allowed to be tensorial. I suppress indices for ease of discussion.D​X≔dX−w​(dlog⁡f)​X.DX\coloneqq\differential X-w(\differential\log\sqrt{f})X\,.(3.11)

We can check that it transforms covariantly under Weyl transformations,DΩ​XΩ=d(Ω−w​X)−w​(dlog⁡Ω−2​f)​(Ω−w​X)=Ω−w​D​X.\begin{split}D^{\Omega}X^{\Omega}&=\differential(\Omega^{-w}X)-w(\differential\log\sqrt{\Omega^{-2}f})(\Omega^{-w}X)\\
&=\Omega^{-w}DX\,.\end{split}(3.12)

This derivative is introduced inKaramitsos and Pilaftsis(2018)on operational grounds by requiring derivatives to transform covariantly under frame transformations. Hopefully the reader will agree that this smells a lot like a gauge-covariant derivative. There are at the very least many analogies to be made between the frame-covariant formalism and gauge theory; these have not gone entirely unnoticed.Quiros and De Arcia(2018, p. 3)for instance intuit “Actually, following the spirit of the above examples: coordinate invariance of the laws of gravity in GR and gauge invariance of the laws of electromagnetism, one should require the action and the field equations of the theory – representing the physical laws – to be invariant under [Weyl transformations].” More recently,Järv and Karamitsos(2026, p. 8)motivate the same construction, emphasising its role as a representational tool for building frame-invariant objects: “The definition of frame-covariant derivatives is useful because it gives us a recipe to construct invariant quantities even when derivatives are involved, and helps us keep track of conformal weights. … reminiscent as it is to a gauge-covariant derivative, [it] is a straightforward way to promote quantities to their covariant counterparts.”

What has to my knowledge not been explicitly argued in the literature is that this analogy can be made exact: the frame-covariant derivativeisliterally obtained from the gauge-covariant derivative induced on the weighted bundles associated with the principalℝ+\mathbb{R}_{+}-bundle of local scales.141414Note that the quantityXXshould not be understood as a section of an associated bundle, but rather as the equivariant function related to it via Eq. (2.10). In our notation, for a weight-one quantity represented byXX, the associated sectionQ=X⊗(f)−1Q=X\otimes(\sqrt{f})^{-1}. If∇\nablais adapted to the Einstein-frame Planck mass, then∇Q=D​X⊗(f)−1{\nabla Q=DX\otimes(\sqrt{f})^{-1}}. More precisely, it is nothing other than the unit-covariant derivative written in the particular gaugeμ=(f)−1{\mu=(\sqrt{f})^{-1}}, and the term−dlog⁡f-\differential\log\sqrt{f}is the local connection 1-form in this trivialisation.

The bundle language makes this identification more precise. Consider the principalℝ+\mathbb{R}_{+}-bundle of conformal metricsS2​T∗​M⊃𝒬→𝒢→MS^{2}T^{*}M\supset\mathcal{Q}\to\mathcal{G}\to M(c.f.footnote4). I will assume that the relevant scale bundle has been identified with𝒬\mathcal{Q}by an isomorphism of principalℝ+\mathbb{R}_{+}-bundles.151515I henceforth assumek=1k=1, which is usually taken to be the case in the study of scalar-tensor theories, where one works in natural units.Then every weighted line bundle is associated to𝒬\mathcal{Q}. We may for instance write down the bundle of dimensionful metricsℓ2g∈Γ(𝒬−2)≃/∼(Γ​(𝒬)×Γ​(ℒ−2+))\ell^{2}g\in\Gamma(\mathcal{Q}_{-2})\simeq{}^{\displaystyle\left(\Gamma(\mathcal{Q})\times\Gamma(\mathcal{L}_{-2}^{+})\right)}{\big/\penalty 50}_{\displaystyle\sim}(3.13)

identifying(g,ℓ2)∼(Ω2​g,Ω−2​ℓ2)(g,\ell^{2})\sim(\Omega^{2}g,\Omega^{-2}\ell^{2}). If we want to consider a collection of other fields occupying the sum of associated vector bundles𝒱=⨁α𝒱α\mathcal{V}=\bigoplus_{\alpha}\mathcal{V}_{\alpha}, with each𝒱α\mathcal{V}_{\alpha}carrying some definite weight, then a field configuration is naturally a sectionΨ\Psiof the total field bundleℰ≔𝒬−2⊕𝒱\mathcal{E}\coloneqq\mathcal{Q}_{-2}\oplus\mathcal{V}. A scalar-tensor theory is then described by an appropriate functionalS:Γ(ℰ)→ℝS\colon\quad\Gamma(\mathcal{E})\to\mathbb{R}(3.14)

(i.e. it takes a familiar form like (3.7)) built from the fields inℰ\mathcal{E}, the spacetime differential, and the covariant derivatives induced from the principal connection on𝒬\mathcal{Q}. At the level of the dynamics defined by this action, the equations of motion are represented by a differential operator of ordernn. That is, they correspond to a bundle map𝖣:Jnℰ→𝒲\mathsf{D}\colon\quad J^{n}\mathcal{E}\to\mathcal{W}(3.15)

from thennthjet bundle to some (weighted) target bundle𝒲\mathcal{W}, where the solution set consists of those field configurationsΨ∈Γ​(ℰ)\Psi\in\Gamma(\mathcal{E})for which𝖣∘jn​Ψ=0{\mathsf{D}\circ j^{n}\Psi=0}. If𝖣\mathsf{D}isℝ+\mathbb{R}_{+}-equivariant then the zero section in𝒲\mathcal{W}is fixed by the group action,𝖣​(jn​Ψ)=0⟹𝖣​(jn​(g⋅Ψ))=g⋅𝖣​(jn​Ψ)=0,\mathsf{D}(j^{n}\Psi)=0\qquad\implies\qquad\mathsf{D}(j^{n}(g\cdot\Psi))=g\cdot\mathsf{D}(j^{n}\Psi)=0\,,(3.16)

sog⋅Ψg\cdot\Psiis a solution wheneverΨ\Psiis.ℝ+\mathbb{R}_{+}-equivariance is precisely the property that fails for ordinary derivatives acting on non-zero-weight fields, and what is restored by promoting ordinary derivatives to covariant ones. However, recall the key insight highlighted earlier; the action functionalSSis(form-)invariantunder the localℝ+\mathbb{R}_{+}-action onΓ​(ℰ)\Gamma(\mathcal{E}), implying that its first variation as well as the Euler-Lagrange equations, given by such an operator𝖣\mathsf{D}, will beℝ+\mathbb{R}_{+}-equivariant.161616Consider the simpler example of a charged massive scalar,S⊃∫d4x​ϕ†​(□+m2)​ϕS\supset\int\differential^{4}x\,\phi^{\dagger}(\Box+m^{2})\phi. This part of the action is gauge-invariant only when□\Boxis built from the corresponding gauge-covariant derivatives. The same goes for equivariance of the Klein-Gordon equation of motion𝖣​ϕ=0\mathsf{D}\phi=0, where𝖣:ϕ↦(□+m2)​ϕ{\mathsf{D}\colon\phi\mapsto(\Box+m^{2})\phi}is viewed as a map. If□\Boxwas built from ordinary derivatives, the gauge group need not be an endomorphism on the space of solutionsker​𝖣\mathrm{ker}\mathsf{D}.The classical equivalence of conformal frames is then a simple corollary: the solution space descends to the quotientker⁡𝖣⟶ker⁡𝖣/C∞​(M,ℝ+).\ker\mathsf{D}\longrightarrow\ker\mathsf{D}/\penalty 50C^{\infty}(M,\mathbb{R}_{+})\,.(3.17)

Structurally, what this means is that solutions to the field equations in the Jordan and Einstein frame (and any other related conformal frame), respectively lie in the sameℝ+\mathbb{R}_{+}-orbit in configuration space and describe the same dynamics up to local rescaling. The coordinates probing directions inker⁡𝖣\ker\mathsf{D}transverse to the orbit are exactly the frame-invariant (gauge-invariant) combinations of fields into weight-zero objects. InSection5we shall see that this is just another manifestation of thetheorem10.

## 4On Dimensionlessness and Unit-independence

In particle physics, we are accustomed to the fact that not all particles are born the same. Leptons and quarks, for instance, manifest distinct physical properties because of how they transform under different representations of the Standard Model gauge group. Adopting language to pinpoint these properties is incredibly helpful in daily discourse — and fortunately physicists have standardised such nomenclature: jargon like ‘the electron iscolourless’ is really just to say that the electron associated bundle transforms in the singlet representation of theS​U​(3)cSU(3)_{c}subgroup (quite a mouthful in comparison), while ‘the Yukawa interaction term isgauge-invariant’ points out how this term is invariant under the full structure groupGSMG_{\text{SM}}.

A similar story can be told about dimensional analysis. In the theory of measurement, it has long been recognised that not all quantities are born the same, in the sense that quantities can admit different classes of admissible transformations. The classic account is due toStevens(1946), who classified scales of measurement into four types: nominal, ordinal, interval, and ratio. In contrast to particle physics, however, the corresponding terminology (and awareness of the fact) is far from established.Stevensexemplifies how discussions of measurement turn volatile once one conflates different empirical operations under colloquial umbrella terms such as ‘scale of measurement’. Without a structural foundation, it becomes almost too easy to sweep substantive distinctions under the semantic carpet. This motivatesStevensto offload part of the burden of articulation onto an underlying group structure. “Perhaps agreement can better be achieved if we recognize that measurement exists in a variety of forms and that scales of measurement fall into certain definite classes.”(Stevens,1946, p. 677)Other terms like units, dimensions, and quantities face similar obfuscations. For example, while torque ‘has the dimension of energy’ and can be expressed in the same units, we should not conclude from this alone that they are the same kind of quantity. AsEmerson(2005, p. L22)puts it: “The ‘dimension’ of a quantity tells us far less about it than its definition does, if indeed its dimension tells us anything at all.”, to whichHall(2022, p. 120)echoes this point when he writes “Unfortunately, ‘quantity’ and ‘dimension’ have become hopelessly entangled.” In the spirit ofStevens, let us therefore explore how gauge theory may help us codify some of these terms.171717All that being said, colloquialisation is not entirely alien to gauge theory either. A mild version of the same phenomenon can be heard in particle physics, where one occasionally encounters loose statements like “the neutrino is chargeless”, referring to the fact that the neutrino is electromagnetically neutral, transforming trivially underU​(1)em⊂GSMU(1)_{\text{em}}\subset G_{\text{SM}}. However, to the extent that particles may be ‘charged’ under other gauge subgroups, the colloquial meaning of the statement does not intend to claim that the neutrino is gauge-invariant. Why does this not spark confusion? My guess is that the basic nomenclature has largely stabilised in particle physics, whereas in dimensional analysis one still regularly encounters semantic disputes at the level of the central terms themselves.

FollowingStevens’s classification, ratio scales involve quantities whose admissible numerical coefficients are related by pure scale transformations,Π↦Π′=ρ​Π\Pi\mapsto\Pi^{\prime}=\rho\,\Piwithρ\rhosome conversion factor, when expressed in different units or representations of said quantity. They are the ones we most often encounter in physics: examples include mechanical quantities such as mass, length, and time. Another example is financial currencies.181818In fact, the connection between currency conversion and gauge theory is already known in the literature. Building onYoung(1999),Maldacena(2016)actually uses the finance of currency conversion as a more pedagogical introduction to the concept of gauge theories. It is notably anℝ+\mathbb{R}_{+}gauge theory.What these structurally all have in common is that ratio scales admit a unit-independent zero point. That is,Π=0\Pi=0always maps to the same zero in any other allowed units. We immediately recognise that admissible transformations of ratio quantities may be captured by the groupℝ+\mathbb{R}_{+}.

Interval scales, on the other hand, provide the simplest example where we must look beyond the groupℝ+\mathbb{R}_{+}of scale transformations. The canonical example of such a quantity is temperature. Conversion from Celsius to Kelvin or Fahrenheit can involve both a scaling and a shift.191919I want to thank Caspar Jacobs for bringing this to my attention.Π(°C)↦Π(K)=Π(°C)+273.15,Π(°C)↦Π(°​F)=95​Π(°C)+32\Pi^{($\text{\,}\mathrm{\SIUnitSymbolCelsius}$)}\mapsto\Pi^{($\text{\,}\mathrm{K}$)}=\Pi^{($\text{\,}\mathrm{\SIUnitSymbolCelsius}$)}+273.15\,,\qquad\Pi^{($\text{\,}\mathrm{\SIUnitSymbolCelsius}$)}\mapsto\Pi^{($\text{\,}\mathrm{\SIUnitSymbolDegree}\mathrm{F}$)}=\frac{9}{5}\Pi^{($\text{\,}\mathrm{\SIUnitSymbolCelsius}$)}+32(4.1)

In other words, scale transformations donotexhaust the set of possible unit transformations for temperature. One must look to the affine groupAff​(1,ℝ)≃ℝ⋊ℝ+\mathrm{Aff}(1,\mathbb{R})\simeq\mathbb{R}\rtimes\mathbb{R}_{+}.202020That is at least before the adoption of the Kelvin scale, which distinguishes ‘absolute zero temperature’,0K0\text{\,}\mathrm{K}, asthezero point. In statistical physics, for example, one will rarely (if ever) work in units like Celsius or Fahrenheit, related to Kelvin via shifts, such as to discern zero temperature. Fixing an origin as such reducesAff​(1,ℝ)\mathrm{Aff}(1,\mathbb{R})to itsℝ+\mathbb{R}_{+}subgroup, effectively treating temperature as a ratio quantity instead of an interval quantity.

The remaining two classes inStevens’s taxonomy may be understood by looking to even larger groups. For ordinal quantities, only hierarchies or inequalities between representatives are preserved under a change of units. Hardness scales of minerals provide a standard example: passing from the Mohs to Vickers preserves order, but not differences or ratios. “Diamond is harder than quartz” is indeed a unit-independent statement, but there is no unit-invariant way of stating numericallyhow muchharder diamond is than quartz. It is therefore fitting to identify the admissible transformations of ordinal quantities with order-preserving diffeomorphismsDiff+​(ℝ)\mathrm{Diff}_{+}(\mathbb{R}).

Nominal quantities are weaker still. Here, only sameness and difference survive. Library sorting systems, social security numbers, telephone area codes, football player jerseys, and other classificatory tags are all nominal. Although people in practice adopt particular tags with other conveniences in mind (for instance the first four digits of modern arXiv identifiers also refer to the date on which the article was uploaded), relabelling them does not alter the represented content. Nominal quantities might possibly take us beyond the physicist’s typical notion of what a quantity entails. Even so, it is conceptually befitting to place it in the hierarchy of structure groups we have seen so far. More specifically, if we insist on usingℝ\mathbb{R}as an auxiliary carrier of labels, we can model arbitrary relabelling by the full diffeomorphism groupDiff​(ℝ)\mathrm{Diff}(\mathbb{R}). I summarise this discussion inTable1.

From the standpoint of gauge theory, we therefore see that dimensional analysis is not intrinsically tied to the principalℝ+k\mathbb{R}_{+}^{k}-bundle. That is merely the special case appropriate to ratio quantities. More generally, we may consider a principalGG-bundle, whereGGis the group of admissible transformations appropriate to the types of quantities under discussion. Interval, ordinal, and nominal quantities are obtained by choosing larger structure groups.Quantity typeGauge groupInvariantRatioℝ+\mathbb{R}_{+}Ratiosq1q2\tfrac{q_{1}}{q_{2}}IntervalAff​(1,ℝ)\mathrm{Aff}(1,\mathbb{R})Ratio of differencesΔ​q1Δ​q2\tfrac{\Delta q_{1}}{\Delta q_{2}}OrdinalDiff+​(ℝ)\mathrm{Diff}_{+}(\mathbb{R})Inequalitiesq1≤q2q_{1}\leq q_{2}NominalDiff​(ℝ)\mathrm{Diff}(\mathbb{R})Equalityq1=q2q_{1}=q_{2}Table 1:A summary of different types of quantities, the corresponding admissible transformation group, and the kind of invariants one can build from its action. For interval, ordinal, and nominal scales these actions should be understood as actions on an associated fibre, not necessarily as linear representations.

Enlarging the structure group also highlights a crucial subtlety concerning the notion of a dimensionless quantity(Emerson,2005;Hall,2022). Consider, for instance, the ratio of two temperaturesT1T2.\frac{T_{1}}{T_{2}}\,.(4.2)

From common intuition of dimensional analysis we readily appreciate that the result will give us a dimensionless quantity, in the mundane sense that one would ordinarily write down no unit symbol (or at least append a formal ‘1’). Or, in the gauge theory language laid out in this paper, we may say more concretely that it has weightw=0w=0under scale transformations. Writing a ‘1’ as the unit can however be misleading because it superficially tempts us to compare the result with ordinary numbers. Despite being dimensionless in the scaling sense, the ratio of two temperatures does not behave like a unit-independent number. Take0°C/5°C=0$0\text{\,}\mathrm{\SIUnitSymbolCelsius}$/$5\text{\,}\mathrm{\SIUnitSymbolCelsius}$=0whereas when expressed in Fahrenheit32°​F/41°​F≠0$32\text{\,}\mathrm{\SIUnitSymbolDegree}\mathrm{F}$/$41\text{\,}\mathrm{\SIUnitSymbolDegree}\mathrm{F}$\neq 0. In contrast, a ratio of temperature differencesΔ​T1Δ​T2=T1−T1′T2−T2′\frac{\Delta T_{1}}{\Delta T_{2}}=\frac{T_{1}-T_{1}^{\prime}}{T_{2}-T_{2}^{\prime}}(4.3)

is dimensionlessandwill agree numerically no matter what units they are expressed in, precisely because the affine shifts cancel. Dimensionless ratios ofintervalquantities evidently behave differently from dimensionless ratios ofratioquantities: the former need not be unit-independent. The same observation of course extends to the remaining scale types. While the clash appears to be mainly semantic(Hall,2022), the gauge theory picture allows us to make the separation more transparent:itemDimensionless:

invariant under scale transformationsℝ+k≤G\mathbb{R}_{+}^{k}\leq G.itemUnit-independent:

invariant under the full structure groupGG.

One can draw a straightforward parallel with the ‘colourless’ versus ‘gauge-invariant’ distinction explained at the start of this section (see alsofootnote17). For instance, whilst a dimensionless quantity is not necessarily unit-independent, all unit-independent quantities must also be dimensionless. Only for ratio quantities do these two notions coincide (‘chargeless’ analogously coincides with ‘gauge-invariant’ for pure electromagnetism). The fact that a word like ‘dimensionless’ is so widespread in daily speech perhaps also reflects the over-abundance of ratio quantities in physics, which understandably makes the difference easy to miss.Roche(1998)is one of the rare examples where unit-independence receives separate attention — actually he arrives incredibly close to the intuition presented here, referring to the invariance under unit transformations as a “gauge invariance”. This has not, to my knowledge, been defended elsewhere. On the contrary,Grozier(2020)findsRoche’s nomenclature somewhat unsatisfactory. He elaborates “because “variation in unit size” makes sense only after one has chosen a unit, whereas I see unit-invariance as a property independent ofanyunit system”(Grozier,2020, p. 10). While I concur that unit-independence as a property appears prior to specifying a set of base units, I will nevertheless argue thatRoche’s use of the term is structurally accurate and aligns withGrozier’s sentiment. To see this, recall fromSection2how adopting a set of base units is the same as trivialising the underlying principal bundle. It is only once a trivialisation is chosen that it becomes possible to parametrise how gauge transformations act on sections of associated bundles.Grozieris therefore right in claiming that to see “variation in unit size” we must specify the units in the first place. Structurally, however, ‘invariation in unit size’ makes sensebeforespecifying the units; invariant quantities (those transforming in the trivial representation) are completely indifferent to the choice of trivialisation.Roche’s terminology therefore correctly captures the structural point that unit-independence corresponds to invariance under the entire structure group and aligns withGrozierwhen he writes that invariance itself is not tied to any particular system of units.

On a final note, let me briefly comment on the interpreted attitude towards dimensionful quantities in relation to the physical significance of unit-independence. As a heuristic statement, it is a widely agreed upon view that physically meaningful expressions should not depend on the choice of unit. Indeed, if the choice of units is merely a conventional representation of quantities, it is not bold to opine that something more fundamental to the laws of nature should not be variant under these choices. Following this rule strictly, we should conclude thatonlyobjects built out of invariant building blocks — like those presented inTable1— are physically meaningful. Philosophers have referred to this as theInvariance Principle: a quantity is physically real only if it is invariant under the symmetries of our theory(Møller-Nielsen,2017;Jacobs,2021). This is not particularly uncontroversial as a first approximation, but it does beg the question: where does this leave quantities themselves, which do generally vary under change of scale? Or, for that matter, relations likeF=m​aF=mabuilt out of variant quantities, which the average physicist most likely will appreciate as physically meaningful.Jacobs(2021)has argued that adopting the Invariance Principle for dimensionful quantities might read a bit too restrictive.Luce(1978)andNarens and Luce(1987)are helpful comparisons. Their notion of meaningfulness is that the truth or falsity of a statement is preserved across all its possible representations; whatJacobsdefends as a criterion forsophistication(Dewar,2019), which rejects the Invariance Principle but retains that symmetry-related models represent the same state of affairs. Translated into the principal bundle language, the sophisticated interpretation of gauge theories thereby accepts that configurations related by gauge transformations are physically equivalent (provided they are isomorphic), but does not require every physically meaningful object or statement to be gauge-invariant(Jacobs,2023a;Gomes,2026). In particular, meaningfulness can also extend toequivariantobjects and statements. Consider the map𝖥:ℒw→ℒw′\mathsf{F}\colon\mathcal{L}_{w}\to\mathcal{L}_{w^{\prime}}. If𝖥\mathsf{F}is equivariant with respect to the group action, then applying a gauge transformation to the statement𝖥=0\mathsf{F}=0givesρw′​(g)−1​𝖥=0\rho_{w^{\prime}}(g)^{-1}\mathsf{F}=0and preserves its truth value across every gauge-related representative (c.f. Eq. (3.16)). There is hence no requirement to restrict meaningfulness to exclusively unit-independent quantities in our account. On a sophisticated reading, quantities are themselves physically meaningful despite transforming non-trivially under unit-transformations, and may still enter into meaningful relations whose content is preserved across all choices of units. Compare this again to ordinary gauge theory. As particle physicists, it would also appear somewhat puzzling if we adopted the stance that only gauge-invariant objects are physically meaningful when the rudimentary building blocks (fields and their corresponding particles) are themselvesvariantunder gauge. Although I do not want to draw any broad conclusions here about the metaphysics of gauge theory and scales of measurement, I do find it relevant to draw the physicist reader’s attention to the sophisticated attitude that appears motivated in the present setting.

## 5The Buckingham-Π\PiTheorem

Having discussed several aspects of dimensional analysis and how it may be appropriately viewed as a gauge theory, we now arrive at perhaps the most famous theorem in dimensional analysis.

## Theorem 10(Buckingham-Π\Pi).

Any lawF​(Q1,…,Qm)=0F(Q_{1},\dots,Q_{m})=0expressed in terms ofmmquantitiesQ1,…,QmQ_{1},\dots,Q_{m}ofkkbase dimensions can be rewritten as a lawf​(Π1,…,Πm−k)=0f(\Pi_{1},\dots,\Pi_{m-k})=0in terms ofm−km-kdimensionless quantitiesΠ\Pi.

SinceBuckingham’s1914paper, the now eponymoustheorem10has occupied a privileged place in the subject. Historically, it crystallised a line of thought already present inFourier’s principle of dimensional homogeneity(Fourier,1878)and in the later work ofRayleigh(1915),Ehrenfest-Afanassjewa(1926), andBridgman(1931), that if a physical equation is to make sense independently of our choice of units, then its form is strongly constrained before any detailed dynamics has been solved(Jalloh,2024,2026).

What makes the theorem so useful in practice is possibly also what made dimensional analysis appear slightly peculiar as a subject. On the one hand, the methodology most physicists will have practised — listing all relevant quantities, noting their dimensions, and reducing the problem to a smaller set of dimensionless combinations — is straightforward and works incredibly well to constrain the algebraic relations among physical quantities. On the other hand, the fact that this works at all is already telling us something structural about physical laws. For that reason the theorem has been so central not only in physical sciences, but also in philosophical discussions of similarity and the explanatory role of dimensions(Sterrett,2009,2021;Jalloh,2025).

For our purposes, however, I do not want to re-prove the theorem merely for the sake of supplying yet another proof. Many roads lead to Rome, and several of them are already well paved(Ehrenfest-Afanassjewa,1916;Gibbings,1982,2011). The point of this section is instead to convey a different flavour of the theorem; one inspired by the gauge theory perspective adopted in this paper. FollowingSection4, it is more transparent that thetheorem10does not necessarily have anything to do with special properties of quantities or how to engineer laws of physics. Rather, it is a statement about countinginvariants.212121Also following the discussion inSection4, it should be clear that the theorem mainly concerns properties of ratio quantities. Strictly speaking,Theorem10does not requireffto be invariant, since the quantitiesΠ\Pineed not be unit-independent; only dimensionless.f=0f=0is therefore only guaranteed invariant under theℝ+\mathbb{R}_{+}action.Let us unpack: suppose we have some physical law or statement𝖥​(Q1,…,Qm)=0\mathsf{F}(Q_{1},\dots,Q_{m})=0(5.1)

whereQi∈Γ​(ℒwi)Q_{i}\in\Gamma(\mathcal{L}_{w_{i}})are quantities of weightwiw_{i}. The tuple of quantities(Q1,…,Qm)(Q_{1},\dots,Q_{m})is then a section of the sumℰ=ℒw1⊕⋯⊕ℒwm.\mathcal{E}=\mathcal{L}_{w_{1}}\oplus\cdots\oplus\mathcal{L}_{w_{m}}\,.(5.2)

For instance, in a textbook dimensional analysis problem where we may be dealing withmmreal quantities, the typical fibreVVofℰ\mathcal{E}isV≃ℝ⊕⋯⊕ℝ⏟mtimesV\simeq\underbrace{\mathbb{R}\oplus\cdots\oplus\mathbb{R}}_{\text{$m$ times}}. Locally, the fibre carries the diagonal actiong⋅(q1,…,qm)=(ρw1​(g)−1​q1,…,ρwm​(g)−1​qm).g\cdot(q_{1},\dots,q_{m})=(\rho_{w_{1}}(g)^{-1}q_{1},\dots,\rho_{w_{m}}(g)^{-1}q_{m})\,.(5.3)

The map𝖥\mathsf{F}then picks out a subspaceℰ𝖥≔𝖥−1​(0)⊂ℰ\mathcal{E}_{\mathsf{F}}\coloneqq\mathsf{F}^{-1}(0)\subset\mathcal{E}that obeys Eq. (5.1). However, we are not interested in just any type of equation: in dimensional analysis (and by analogy in gauge theory) we are interested in equations whose truth value remains the same under rescaling of units (gauge transformations); c.f. the discussion at the end ofSection4orSection3.1for comparison. As a local statement at the level of the fibre, equations of interest are precisely the ones whose (local) solution space descends to the quotient over the typical fibre,V/GV/G. That is, a map𝖥\mathsf{F}for which(Q1,…,Qm)∈ℰ𝖥(Q_{1},\dots,Q_{m})\in\mathcal{E}_{\mathsf{F}}impliesg⋅(Q1,…,Qm)∈ℰ𝖥g\cdot(Q_{1},\dots,Q_{m})\in\mathcal{E}_{\mathsf{F}}.

It is then a fact that (on a regular stratification)GG-invariant functions onVVdepend only on coordinates on the orbit spaceV/GV/\penalty 50G.222222The orbit spaceV/GV/\penalty 50Gmay fail to be Hausdorff when some orbits are not closed. Consider for exampleℝ+\mathbb{R}_{+}acting onℝ2\mathbb{R}^{2}byg⋅(x,y)=(g​x,g−1​y)g\cdot(x,y)=(gx,g^{-1}y). The orbit of(x,0)(x,0)withx>0x>0has(0,0)(0,0)in its closure, however the origin is its own distinct orbit.ℝ2/ℝ+\mathbb{R}^{2}/\penalty 50\mathbb{R}_{+}is therefore non-Hausdorff. That being said, I would not think this to be a problem for Buckingham-Π\Pi, since it is intended as a statement about generic quantities away from ill-behaved loci such as this; e.g. where certain quantities vanish.The local dimension of the quotient isdim​(V/G)=dim​(V)−dim​(G)+dim​(Gstab),\mathrm{dim}(V/\penalty 50G)=\mathrm{dim}(V)-\mathrm{dim}(G)+\mathrm{dim}(G_{\text{stab}})\,,(5.4)

whereGstabG_{\text{stab}}is the generic stabiliser. When the group acts freely then the last term vanishes. It becomes simple to see why we should recover thetheorem10: if there aremmreal-valued ratio quantities whose weights span thekkbase dimensionalities, we may identifyV=ℝmV=\mathbb{R}^{m}andG=ℝ+kG=\mathbb{R}_{+}^{k}, and thusdim​(V/G)=m−k\mathrm{dim}(V/\penalty 50G)=m-k.

Let us look at some illustrative examples:

## Rotational symmetry:

considerSO​(3)\mathrm{SO}(3)-invariant functions overℝ3\mathbb{R}^{3}, with the group acting by rotations. The stabiliser of any non-zero vector inℝ3\mathbb{R}^{3}isSO​(2)\mathrm{SO}(2), so away from the origin we find thatdim​(ℝ3/SO​(3))=3−3+1=1\mathrm{dim}(\mathbb{R}^{3}/\penalty 50\mathrm{SO}(3))=3-3+1=1. In other words, such functions depend only on one variable (the radius).

## Simple pendulum:

the simple pendulum is a textbook example in dimensional analysis. The task is to find a general expression relating various parameters of the system. A preliminary physics guess is that the period of the pendulumTTmay depend on its lengthℓ\ell, the gravitational accelerationγ\gamma(to avoid conflating with group elementsgg), and massmm. We identify three base dimensionalities: mass, length, time (all of the ratio type). As a gauge theory, the structure group is thereforeG=ℝ+3G=\mathbb{R}_{+}^{3}and acts on the fibreV≃ℝ4V\simeq\mathbb{R}^{4}where the quantities take their values. Assuming the weights span𝔤∗\mathfrak{g}^{*},232323If too many weights are degenerate, there is a possibility that the stabiliser becomes non-trivial as the weights fail to span all of𝔤∗\mathfrak{g}^{*}. E.g. if all weights are proportional,dim​(ℝ4/ℝ+3)=4−3+2=3{\mathrm{dim}(\mathbb{R}^{4}/\penalty 50\mathbb{R}_{+}^{3})=4-3+2=3}.one readily findsdim​(ℝ4/ℝ+3)=1\mathrm{dim}(\mathbb{R}^{4}/\penalty 50\mathbb{R}_{+}^{3})=1. Any unit-independent function over the four quantities must therefore locally be expressible as a function of one invariant combination,Π=∏Q∈{T,ℓ,γ,m}QrQsuch that∑QrQ​wQ=0\Pi=\prod_{Q\in\{T,\ell,\gamma,m\}}Q^{r_{Q}}\qquad\text{such that}\qquad\sum_{Q}r_{Q}w_{Q}=0(5.5)

for some set ofrQ∈ℝr_{Q}\in\mathbb{R}.

Note how this approach does not directly tell us what the invariantΠ\Piis. That is a subsequent task requiring us to solve the set of equations involving the exponentsrQr_{Q}and weightswQ∈𝔤∗w_{Q}\in\mathfrak{g}^{*}. Suppose we pick a “mechanical” basis on𝔤∗\mathfrak{g}^{*}, such that the weight vector components read as follows:MassLengthTimewTw_{T}0011wℓw_{\ell}0110wγw_{\gamma}011−2-2wmw_{m}1100

One finds the unique solutionΠ=T2​ℓ−1​γ\Pi=T^{2}\ell^{-1}\gammaup to an overall power. The simple pendulum is therefore described by some unit-invariant equation𝖿​(Π)=0\mathsf{f}(\Pi)=0. As always, symmetries can only take us so far when it comes to fixing the precise law or dynamics of the system — only through further physical insight or more detailed calculations, e.g. by explicitly solving the equations of motion, would we find for the simple pendulum (in the small-angle approximation) that𝖿\mathsf{f}takes the form𝖿​(Π)=Π−2​π=0.\mathsf{f}(\Pi)=\sqrt{\Pi}-2\pi=0\,.(5.6)

## A “U​(1)U(1)simple pendulum”:

in the spirit ofSection2.1, let us explore how the same dimensional analysis exercise carries over to gauge theory. Consider aU​(1)3U(1)^{3}gauge theory describing four charged complex scalars{Ψi}i=1,…,4\{\Psi_{i}\}_{i=1,\dots,4}. A relevant exercise is to find the most general (local) gauge-invariant function written in terms of the four fields (for instance a scalar potential𝖵​(Ψi)\mathsf{V}(\Psi_{i})). Since the fields take values inV≃ℂ4V\simeq\mathbb{C}^{4}(and assuming their weights span𝔴∗\mathfrak{w}^{*}), we computedimℝ​(V/G)=8−3=5{\mathrm{dim}_{\mathbb{R}}(V/\penalty 50G)=8-3=5}. Any gauge-invariant function can therefore be written in terms of the real and imaginary part of the complex singletsΠ=∏i=14Ψiri​Ψ¯iri′such that∑i(ri−ri′)​wi=0.\Pi=\prod_{i=1}^{4}\Psi_{i}^{r_{i}}\bar{\Psi}_{i}^{r^{\prime}_{i}}\qquad\text{such that}\qquad\sum_{i}(r_{i}-r_{i}^{\prime})w_{i}=0\,.(5.7)

This is just theU​(1)U(1)-analogue of the simple pendulum, with additional real invariants appearing because the fields are complex. Once again, this exercise alone is not sufficient in order to solve for the expression ofΠ\Pi. Suppose that the charges took the following values in the canonical basis of𝔴∗≃ℤ3\mathfrak{w}^{*}\simeq\mathbb{Z}^{3}:U​(1)1U(1)_{1}U​(1)2U(1)_{2}U​(1)3U(1)_{3}w1w_{1}0011w2w_{2}0110w3w_{3}011−2-2w4w_{4}1100

Four of these invariants are the normsΠi=Ψi​Ψ¯i\Pi_{i}=\Psi_{i}\bar{\Psi}_{i}, while the remaining invariant is the less trivial complex combinationΠ5=Ψ12​Ψ¯2​Ψ3\Pi_{5}=\Psi_{1}^{2}\bar{\Psi}_{2}\Psi_{3}, analogous toT2​ℓ−1​γT^{2}\ell^{-1}\gammain the previous example. Although naïvely this yields six real invariants (two coming from the real and imaginary part ofΠ5\Pi_{5}), they are subject to one constraint,Π5​Π¯5=Π12​Π2​Π3\Pi_{5}\bar{\Pi}_{5}=\Pi_{1}^{2}\Pi_{2}\Pi_{3}. Thus we find that the quotient has the expected five real dimensions. A general gauge-invariant function can thus be written as𝖿​(Π1,…,Π4,Re​Π5,Im​Π5)\mathsf{f}(\Pi_{1},\dots,\Pi_{4},\mathrm{Re}\,\Pi_{5},\mathrm{Im}\,\Pi_{5})subject to this relation.

## The Standard Model Yukawa sector:

let us look at a slightly more involved example familiar from particle physics. In the quark sector of the Standard Model, the gauge and kinetic terms admit a global flavour symmetryG=U​(N)QL×U​(N)uR×U​(N)dRG=U(N)_{Q_{L}}\times U(N)_{u_{R}}\times U(N)_{d_{R}}, whereNNis the number of generations. This symmetry is broken by the Yukawa interactionsℒYukawa=−Q¯L​Yu​H~​uR−Q¯L​Yd​H​dR+h.c.\mathcal{L}_{\text{Yukawa}}=-\bar{Q}_{L}Y_{u}\widetilde{H}u_{R}-\bar{Q}_{L}Y_{d}Hd_{R}+\text{h.c.}(5.8)

whereYu,Yd∈ℂN×NY_{u},Y_{d}\in\mathbb{C}^{N\times N}. Equivalently, however, one may retain the flavour symmetry by regarding the Yukawa matrices as spurions transforming according toYu↦VQ​Yu​Vu†,Yd↦VQ​Yd​Vd†Y_{u}\mapsto V_{Q}Y_{u}V_{u}^{\dagger}\,,\qquad Y_{d}\mapsto V_{Q}Y_{d}V_{d}^{\dagger}(5.9)

for(VQ,Vu,Vd)∈G(V_{Q},V_{u},V_{d})\in G. The problem of counting the number of independent physical parameters controlling the Yukawa couplings then becomes a problem of determining the dimension of the orbit space over the pair(Yu,Yd)(Y_{u},Y_{d}). The only generic stabiliser isVQ=Vu=Vd=ei​α​1NV_{Q}=V_{u}=V_{d}=e^{i\alpha}1_{N}(corresponding to the baryon numberU​(1)BU(1)_{B}) acting trivially onYuY_{u}andYdY_{d}. Hence the orbit space has dimensiondimℝ​((ℂN×N⊕ℂN×N)/U​(N)3)=4​N2−3​N2+1=N2+1.\mathrm{dim}_{\mathbb{R}}((\mathbb{C}^{N\times N}\oplus\mathbb{C}^{N\times N})/\penalty 50U(N)^{3})=4N^{2}-3N^{2}+1=N^{2}+1\,.(5.10)

In other words, the Yukawa matrices contain the information ofN2+1N^{2}+1independent physical parameters. It is well-known that these comprise the2​N2Nquark masses after symmetry breaking,N​(N−1)2\tfrac{N(N-1)}{2}mixing angles, and(N−1)​(N−2)2\tfrac{(N-1)(N-2)}{2}CP-violating phases.

Finding all the invariant combinations is once again a supplementary exercise(seeJenkins and Manohar,2009, Section 5). DefineXu≔Yu​Yu†{X_{u}\coloneqq Y_{u}Y_{u}^{\dagger}}andXd≔Yd​Yd†{X_{d}\coloneqq Y_{d}Y_{d}^{\dagger}}. The relevant flavour action then acts via simultaneous conjugationXu⟼VQ​Xu​VQ†,Xd⟼VQ​Xd​VQ†.X_{u}\longmapsto V_{Q}X_{u}V_{Q}^{\dagger}\,,\qquad X_{d}\longmapsto V_{Q}X_{d}V_{Q}^{\dagger}\,.(5.11)

ForN=3N=3in the Standard Model, it turns out that there are ten algebraically independent CP-even invariantstr⁡Xutr⁡Xdtr⁡Xu2tr⁡Xu​Xdtr⁡Xd2tr⁡Xu3tr⁡Xu2​Xdtr⁡Xu​Xd2tr⁡Xd3tr⁡Xu2​Xd2\begin{gathered}\tr X_{u}\qquad\tr X_{d}\\
\tr X_{u}^{2}\qquad\tr X_{u}X_{d}\qquad\tr X_{d}^{2}\\
\tr X_{u}^{3}\qquad\tr X_{u}^{2}X_{d}\qquad\tr X_{u}X_{d}^{2}\qquad\tr X_{d}^{3}\\
\tr X_{u}^{2}X_{d}^{2}\end{gathered}(5.12)

The remaining CP-odd invariant was found byJarlskog(1985),J∝itr[Xu,Xd]3.J\propto i\tr[X_{u},X_{d}]^{3}\,.(5.13)

Its square yields a polynomial in the ten CP-even invariants. Just like in the previous example, despite having naïvely discovered more thanN2+1=10{N^{2}+1=10}invariants expected from dimension counting, the surplus is accounted for by algebraic constraints. The most generalGG-invariant polynomial is accordingly of the form242424Coordinates on the orbits may thus not suffice to generate theGG-invariant algebra, since additional invariants can be required to distinguish different branches or orientations. For example, letU​(1)U(1)act diagonally on(x,y)∈ℂ2(x,y)\in\mathbb{C}^{2}. A convenient set of real polynomial invariants is|x|2,|y|2,Re​(x¯​y),Im​(x¯​y)\absolutevalue{x}^{2},\absolutevalue{y}^{2},\mathrm{Re}(\bar{x}y),\mathrm{Im}(\bar{x}y)subject to the relationRe​(x¯​y)2+Im​(x¯​y)2=|x|2​|y|2\mathrm{Re}(\bar{x}y)^{2}+\mathrm{Im}(\bar{x}y)^{2}=\absolutevalue{x}^{2}\absolutevalue{y}^{2}. This is consistent withdimℝ​(ℂ2/U​(1))=3\mathrm{dim}_{\mathbb{R}}(\mathbb{C}^{2}/\penalty 50U(1))=3. The orbit can be parametrised by two magnitudes and one relative angleθ\theta. However, if one only keepsRe​(x¯​y)\mathrm{Re}(\bar{x}y), one cannot distinguish between relative phasesθ\thetaand−θ-\theta; the phase-odd invariantIm​(x¯​y)\mathrm{Im}(\bar{x}y)is also required to explore the fullGG-invariant algebra.𝖿1​(ΠCP-even)+J​𝖿2​(ΠCP-even).\mathsf{f}_{1}(\Pi_{\text{CP-even}})+J\mathsf{f}_{2}(\Pi_{\text{CP-even}})\,.(5.14)

I hope it is clear from the examples above that the gist of thetheorem10is not unique to dimensional analysis, and that it generalises to much broader applications in gauge theory and particle physics as well. Counting and determining invariant combinations is evidently not a specialist task in dimensional analysis. It is quite the opposite: there is an entire field in mathematics dedicated to it, known asinvariant theory.

Suffice it to say, the overarching goal of classical invariant theory is to identify the properties of mathematical objects that remain invariant under a specified group action. Given a groupGGacting linearly on a finite-dimensional vector spaceVVover a field𝕜\Bbbk, one can study the properties of the space ofGG-invariant polynomials𝕜​[V]G\Bbbk[V]^{G}. For instance, Hilbert famously proved for a wide range of cases that𝕜​[V]G\Bbbk[V]^{G}is a finitely generated algebra over𝕜\Bbbk. From the examples above we can imagine how determining all generators and relations (syzygies) among them is generally a very complicated task. For a general compact Lie group, invariant-building becomes much harder because fields usually sit in non-trivial representations and involve contracting fields into singlets using various available invariant tensors, such as Kronecker deltas, Levi-Civita symbols, traces, etc. These contractions can satisfy non-trivial algebraic relations, so the number of invariant generators need not coincide with the dimension of the orbit space (c.f. the Yukawa example andfootnote24).

It should be highlighted, though, that applications of invariant theory to gauge theory and particle physics have been studied for many years. Suppose, for example, we are tasked to build the most general extension of the Standard Model by including higher-dimensional operators, as in the Standard Model Effective Field Theory (SMEFT) or Higgs Effective Field Theory (HEFT). There are many ways to combine and contract fields into Lorentz- and gauge-invariant combinations. At low mass dimension this can be done by hand. For higher mass dimension, however, the combinatorics quickly become unmanageable if one also takes into account redundancies due to identities, integration by parts, and so on. Counting and organising the algebraically independent operators at each order in the EFT expansion is therefore naturally a problem for invariant theory. Hilbert series methods have become a systematic way to attack this problem and are extensively explored inJenkins and Manohar(2009);Hanany et. al.(2011);Lehman and Martin(2015,2016);Henning et. al.(2016)as well as in later literature.

All this begs a natural question. If thetheorem10is anℝ+k\mathbb{R}_{+}^{k}instance of a more generic invariant-counting problem, is there an analogous statement for other groups — possibly ones familiar from particle physics? The answer isyes. A beautiful theorem due toSchwarzgoes as follows:

## Theorem 11(Schwarz(1975)).

LetVVbe a real finite dimensional representation of a compact Lie groupGG. LetΠ1,…,Πn\Pi_{1},\dots,\Pi_{n}be generators ofℝ​[V]G\mathbb{R}[V]^{G}, the algebra ofGG-invariant polynomials onVV. EachGG-invariantC∞C^{\infty}-functionFFonVVhas the formF=f​(Π1,…,Πn)F=f(\Pi_{1},\dots,\Pi_{n})for someC∞C^{\infty}-functionffonℝn\mathbb{R}^{n}.

theorem11on invariant functions is the cousin of thetheorem10for compact Lie groups, although it does not predict the numbernnof invariant generators. For a general compact Lie groupGG, determiningnnis a central problem of classical invariant theory (and therefore not one I shall attempt to solve here).

From the present discussion I hope to have conveyed that thetheorem10and its application to dimensional analysis are but an unusually tractable corner of a much larger invariant-theoretic problem. In the case of ordinary dimensional analysis the solution is relatively straightforward. In particle physics, on the other hand, the structure is usually much richer. That these methods and theorems are already woven into the technology used in modern gauge theory is a curious hint that the gauge-theoretic reading of dimensional analysis was never actually far away. Perhaps they were only ever speaking different dialects of the same language.

## 6Conclusion

In1918,ite]cite.Weyl1918Hermann Weyl introduced the world to what is now retrospectively regarded as the first gauge theory. His original model — an attempt to unify gravity and electromagnetism — did not involve the compact Lie groups we usually associate with modern particle physics. Rather, it was built on the idea ofscalesymmetry, withℝ+\mathbb{R}_{+}playing the role of the gauge group. Indeed,Eddingtonalready made explicit at the time the intuition thatWeyl’s gauge transformations could be understood as local changes of units (Eddington,1921; see alsoEddington,1923, Sec. 85–86).Weyl’s model, however, did not achieve its intended physical unification, and the local scale transformations soon gave way, in what would become the mainstream continuation of gauge theory, to local phase transformations during the late-1920s development of quantum mechanics.
I find the history particularly noteworthy. At roughly the same time, the early twentieth century saw an active debate concerning the methodology and metaphysical foundations of dimensional analysis(Jalloh,2024). I will not speculate why these circles did not merge their ideas, but it is useful to observe that the two traditions developed in different disciplines: gauge theory in relativity and field theory, and dimensional analysis in more classical settings such as mechanics and hydrodynamics. Even so, they were never very far apart. This becomes especially clear when considered in the same light, as later made explicit byDicke(1962), who placed unit transformations and Weyl transformations on the same footing. The connection is easy to miss, not least because the habitual use of natural units in theoretical physics today tends to hide the choice of scale.

One purpose of the present paper has been to assemble the pieces of this puzzle. It has long been unclear what mathematical foundation underlies dimensional analysis. Yet, as a methodology, dimensional analysis is something most physicists learn early in their careers — it is simple, intuitive, and oftentimes incredibly powerful. A mathematical scaffolding should not merely accommodate these qualities, but strengthen and extend them. On structural grounds, and with these perspectives in mind, I defended the claim that dimensional analysis can quite literally be understood as a gauge theory. In the simplest case of ratio quantities, it is equipped with structure groupℝ+k\mathbb{R}_{+}^{k}, wherekkis the number of base dimensionalities. Dimensional quantities then appear as analogues of charged fields, as associated bundles transforming under different representations of the structure group. Quantity calculus also follows immediately from basic representation theory. Furthermore, I showed that any complete set of base units corresponds to a trivialisation of the underlying principal bundle; in this precise sense, a choice of base units is a choice of gauge.

The same framework also helped disentangle separate several subtleties related to scales of measurement. InSection3.1, I clarified the physical equivalence between conformal frames in scalar-tensor theories from a bundle perspective. In particular, frame transformations are structurally equivalent to, and can thus be undone by, appropriate unit transformations, echoing arguments byDicke(1962)and the frame-covariant formalism (Flanagan,2004;Kuusk, Järv and Vilson,2016;Karamitsos and Pilaftsis,2018; see alsoKaramitsos and Muntz,2025). InSection4, I argued that different types of scales of measurement can also be encoded in larger structure groups. This, in turn, clarifies a semantic challenge in distinguishing dimensionless from unit-independent quantities(Emerson,2005;Hall,2022): the former are invariant underℝ+k\mathbb{R}_{+}^{k}, whereas the latter are invariant under the full structure groupG≥ℝ+kG\geq\mathbb{R}_{+}^{k}.

Throughout this paper, I identified several ways in which dimensional analysis and gauge theory illuminate one another. Drawing analogies withU​(1)kU(1)^{k}gauge theory, for example, gives a useful picture of how number-unit decomposition of quantities parallels the magnitude-phase decomposition of complex fields. On the other hand,ℝ+k\mathbb{R}_{+}^{k}gauge theory is structurally less rich: in the setting considered here, it has no charge quantisation, and has trivial topology over paracompact bases. Moving from dimensional analysis back into gauge theory, I reinterpreted thetheorem10as a statement about gauge-invariant functions on representation spaces. Several pedagogical examples were used to demonstrate how the theorem carries over to similar counting problems in gauge theory. Notably,theorem11is the analogue of thetheorem10for compact Lie groups. Counting the minimum number ofΠ\Pi’s for a general compact Lie group and representation, however, is a difficult open problem of invariant theory in mathematics. Taken together, these perspectives strongly suggest that dimensional analysis and gauge theory are structurally equivalent formalisms: both rely on the same symmetry and covariance principles.

Allow me to close with a speculative observation concerning the role of dimensional analysis and units in fundamental physics. Throughout the present work, we have observed that the symmetry groups associated with scales of measurement are generally non-compact. If units are to be taken seriously as reflecting an internal gauge symmetry, on a par with the gauge groups of particle physics, this may have broader implications for the foundations of the theory. For example, there is an argument going back toBanks and Seiberg(2011)(see alsoGagliano and Tudball,2026)that effective theories obtainable from quantum gravity should not possess any non-compact gauge symmetries. If this adventuresome line of thought applies, it would suggest that effective theories of quantum gravity must fundamentally lack dimensionality; the respective gauge symmetries cannot be physical or dynamical, and are at best representational. An alternative possibility is that local changes of units must be tied to isomorphic symmetries that are not internal, such as Weyl transformations. That this framework potentially allows such questions even to be formulated precisely is, in my view, an inspiring prospect.

## Acknowledgements

I would like to thank Ali Bakhordarian, Ed Copeland, Zongzhe Du, Erik Søndergaard Gimsing, Henrique Gomes, Caspar Jacobs, Tony Padilla, and Kieran Wood for many helpful discussions and comments on the draft. I reserve a special thanks to Sotirios Karamitsos for many long discussions on dimensional analysis and units, and for bringing my attention to this topic.

## References
- Baez (2009)Baez, J. (2009).Torsors made easy.
https://math.ucr.edu/home/baez/torsors.html[Accessed: July 2026].
- Banks and Seiberg (2011)Banks, T. and Seiberg, N. (2011).Symmetries and Strings in Field Theory and Gravity.
Phys. Rev. D.83, 084019.
- Bento et. al. (2025)Bento, B. V., Chakraborty, D., Parameswaran, S. and Zavala, I. (2025).A guide to frames,2​π2\pi’s, scales and corrections in string compactifications.
Int. J. Mod. Phys. D34(10), 2530003.
- BIPM (2019)Bureau International des Poids et Mesures (BIPM) (2019).The International System of Units (SI).
9th ed. Sèvres: Bureau International des Poids et Mesures.https://www.bipm.org/en/publications/si-brochure.
- Bridgman (1931)Bridgman, P. W. (1931).
Dimensional Analysis.
Revised. New Haven: Yale University Press.
- Buckingham (1914)Buckingham, E. (1914).On Physically Similar Systems; Illustrations of the Use of Dimensional Equations.
Physical Review4(4), 345–376.
- Curry and Gover (2018)Curry, S. N. and Gover, A. R. (2018).An Introduction to Conformal Geometry and Tractor Calculus, with a view to Applications in General Relativity.
In: Daudé, T., Häfner, D., and Nicolas, J.-P. (eds.),Asymptotic Analysis in General Relativity.
London Mathematical Society Lecture Note Series443. Cambridge University Press, 86–170.
- de Boer (1995)de Boer, J. (1995).On the History of Quantity Calculus and the International System.
Metrologia31(6), 405–429.
- De Clark (2017)De Clark, S. G. (2017).Qualitative vs Quantitative Conceptions of Homogeneity in Nineteenth Century Dimensional Analysis.
Annals of Science74(4), 299–325.
- Dewar (2019)Dewar, N. (2019).Sophistication about symmetries.
The British Journal for the Philosophy of Science70(2), 485–521.
- Dicke (1962)Dicke, R. H. (1962).Mach’s principle and invariance under transformation of units.
Phys. Rev.125, 2163–2167.
- Domotor (2017)Domotor, Z. (2017).Torsor theory of physical quantities and their measurement.
Measurement Science Review17(4), 152–177.
- Eddington (1921)Eddington, A. S. (1921).A generalisation of Weyl’s theory of the electromagnetic and gravitational fields.
Proc. R. Soc. Lond. A99(697), 104–122.
- Eddington (1923)Eddington, A. S. (1923).The Mathematical Theory of Relativity.
Cambridge: Cambridge University Press.
- Ehrenfest-Afanassjewa (1916)Ehrenfest-Afanassjewa, T. (1916).On Mr. R. C. Tolman’s “Principle of Similitude.”.
Physical Review8(1), 1–7.
- Ehrenfest-Afanassjewa (1926)Ehrenfest-Afanassjewa, T. (1926).
XVII.Dimensional Analysis Viewed from the Standpoint of the Theory of Similitudes.
The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science1(1), 257–272.
- Emerson (2005)Emerson, W. H. (2005).On the concept of dimension.
Metrologia42(4), L21–L22.
- Faraoni, Gunzig and Nardone (1999)Faraoni, V., Gunzig, E. and Nardone, P. (1999).Conformal transformations in classical gravitational theories and in cosmology.
Fund. Cosmic Phys.20(2), 121–175.
- Fourier (1878)Fourier, J. (1878).
The Analytical Theory of Heat.
Translated by A. Freeman.
Cambridge: University Press.
- Finn, Karamitsos and Pilaftsis (2020)Finn, K., Karamitsos, S. and Pilaftsis, A. (2020).Frame Covariance in Quantum Gravity.
Phys. Rev. D.102(4), 045014.
- Flanagan (2004)Flanagan, E. E. (2004).The Conformal frame freedom in theories of gravitation.
Class. Quant. Grav.21, 3817–3829.
- Gagliano and Tudball (2026)Gagliano, F. and Tudball, C. (2026).Decompactification Limits of Non-Compact Gauge Theory.
[arXiv:2602.15680].
- Gomes (2024)Gomes, H. (2024).Gauge theory is about the geometry of internal spaces.
[arXiv:2404.10461].
- Gomes (2025)Gomes, H. (2025).Particles before symmetry.
[arXiv:2509.25276].
- Gomes (2026)Gomes, H. (2026).Making Symmetry Explicit: The Limits of Sophistication.
[arXiv:2602.13708].
- Gibbings (1982)Gibbings, J. C. (1982).A Logic of Dimensional Analysis.
Journal of Physics A: Mathematical and General15(7), 1991–2002.
- Gibbings (2011)Gibbings, J. C. (2011).Dimensional Analysis.
London: Springer.
- Grozier (2020)Grozier, J. (2020).Should physical laws be unit-invariant?.
Studies in History and Philosophy of Science Part A80, 9–18.
- Hall (2022)Hall, B. D. (2022).The Problem with ’Dimensionless Quantities’.
In:Proceedings of the 10th International Conference on Model-Driven Engineering and Software Development (MODELSWARD 2022). SCITEPRESS, 116–125.
- Hanany et. al. (2011)Hanany, A., Jenkins, E. E., Manohar, A. V. and Torri, G. (2011).Hilbert Series for Flavor Invariants of the Standard Model.
JHEP03, 096.
- Henning et. al. (2016)Henning, B., Lu, X., Melia, T. and Murayama, H. (2016).Hilbert series and operator bases with derivatives in effective field theories.
Commun. Math. Phys.347, 363–388.
- Jacobs (2021)Jacobs, C. (2021).Invariance or equivalence: A tale of two principles.
Synthese199(3–4), 9337–9357.
- Jacobs (2023a)Jacobs, C. (2023a).The Metaphysics of Fibre Bundles.
Studies in History and Philosophy of Science97, 34–43.
- Jacobs (2023b)Jacobs, C. (2023b).The Nature of a Constant of Nature: The Case of G.
Philosophy of Science90(4), 797–816.
- Jacobs (2024)Jacobs, C. (2024).In Defence of Dimensions.
The British Journal for the Philosophy of Science, advance online publication.https://doi.org/10.1086/729749.
- Jalloh (2024)Jalloh, M. (2024).Metaphysics and Convention in Dimensional Analysis, 1914–1917.
Hopos: The Journal of the International Society for the History of Philosophy of Science14(2), 275–322.
- Jalloh (2025)Jalloh, M. (2025).TheΠ\Pi-Theorem as a Guide to Quantity Symmetries and the Argument Against Absolutism.
Oxford Studies in Metaphysics14, Oxford University Press, 91–130.
- Jalloh (2026)Jalloh, M. (2026).Tatiana Ehrenfest-Afanassjewa’s Critical Contributions to Dimensional Analysis.
[Preprint].https://philsci-archive.pitt.edu/30317/.
- Janyška, Modugno and Vitolo (2007)Janyška, J., Modugno, M. and Vitolo, R. (2007).Semi-vector spaces and units of measurement.
[arXiv:0710.1313].
- Janyška, Modugno and Vitolo (2010)Janyška, J., Modugno, M. and Vitolo, R. (2010).An Algebraic Approach to Physical Scales.
Acta Appl. Math.110, 1249–1276.
- Jarlskog (1985)Jarlskog, C. (1985).Commutator of the Quark Mass Matrices in the Standard Electroweak Model and a Measure of Maximal CP Nonconservation.
Phys. Rev. Lett.55, 1039–1042.
- Järv and Karamitsos (2026)Järv, L. and Karamitsos, S. (2026).Frame invariant diffusive formulation of scalar-tensor gravity.
[arXiv:2604.16094].
- Jenkins and Manohar (2009)Jenkins, E. E. and Manohar, A. V. (2009).Algebraic Structure of Lepton and Quark Flavor Invariants and CP Violation.
JHEP10, 094.
- Karamitsos and Pilaftsis (2018)Karamitsos, S. and Pilaftsis, A. (2018).Frame Covariant Nonminimal Multifield Inflation.
Nucl. Phys. B927, 219–254.
- Karamitsos and Muntz (2025)Karamitsos, S. and Muntz, B. (2025).From Frame Covariance to the Swampland Distance Conjecture.
[arXiv:2512.07929].
- Kobayashi and Nomizu (1963)Kobayashi, S. and Nomizu, K. (1963).Foundations of Differential Geometry. Vol. I.
New York–London: Interscience Publishers, a division of John Wiley & Sons.
- Kuusk, Järv and Vilson (2016)Kuusk, P., Järv, L. and Vilson, O. (2016).Invariant quantities in the multiscalar-tensor theories of gravitation.
Int. J. Mod. Phys. A31(02n03), 1641003.
- Lehman and Martin (2015)Lehman, L. and Martin, A. (2015).Hilbert Series for Constructing Lagrangians: expanding the phenomenologist’s toolbox.
Phys. Rev. D.91, 105014.
- Lehman and Martin (2016)Lehman, L. and Martin, A. (2016).Low-derivative operators of the Standard Model effective field theory via Hilbert series methods.
JHEP02, 081.
- Luce (1978)Luce, R. Duncan (1978).Dimensionally invariant numerical laws correspond to meaningful qualitative relations.
Philosophy of Science45(1), 1–16.
- Maldacena (2016)Maldacena, J. (2016).The symmetry and simplicity of the laws of physics and the Higgs boson.
Eur. J. Phys.37(1), 015802.
- Mitchell (2017)Mitchell, D. J. (2017).Making Sense of Absolute Measurement: James Clerk Maxwell, William Thomson, Fleeming Jenkin, and the Invention of the Dimensional Formula.
Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics58, 63–79.
- Møller-Nielsen (2017)Møller-Nielsen, T. (2017).Invariance, Interpretation, and Motivation.
Philosophy of Science84(5), 1253–1264.
- Narens and Luce (1987)Narens, L. and Luce, R. D. (1987).Meaningfulness and invariance.
In: Eatwell, J., Milgate, M. and Newman, P. (eds.),The New Palgrave: A Dictionary of Economic Theory and Doctrine.
Macmillan Press, 417–421.
- Poincaré (1906)Poincaré, H. (1906).La relativité de l’espace.
L’Année psychologique13, 1–17.
(English translation:The Relativity of Space, translated by G. B. Halsted, The Monist23(2), 161–180 (1913)).
- Quiros and De Arcia (2018)Quiros, I. and De Arcia, R. (2018).On local scale invariance and the questionable theoretical basis of the conformal transformations’ issue.
[arXiv:1811.02458].
- Raposo (2018)Raposo, Á. P. (2018).The Algebraic Structure of Quantity Calculus.
Measurement Science Review, Slovak Academy of Sciences, Institute of Measurement Sciences,18(4), 147–157.
- Raposo (2019)Raposo, Á. P. (2019).The Algebraic Structure of Quantity Calculus II: Dimensional Analysis and Differential and Integral Calculus.
Measurement Science Review, Slovak Academy of Sciences, Institute of Measurement Sciences,19(2), 70–78.
- Rayleigh (1915)Rayleigh, Lord (1915).The Principle of Similitude.
Nature95, 66–68.
- Roche (1998)Roche, J. J. (1998).The mathematics of measurement: A critical history.
London: Athlone Press.
- Schwarz (1975)Schwarz, G. W. (1975).Smooth functions invariant under the action of a compact Lie group.
Topology14(1), 63–68.
- Skow (2017)Skow, B. (2017).The Metaphysics of Quantities and Their Dimensions.
Oxford Studies in Metaphysics10, 171–198.
- Sterrett (2009)Sterrett, S. G. (2009).Similarity and dimensional analysis.
In: Philosophy of technology and engineering sciences. Elsevier, 799–823.
- Sterrett (2021)Sterrett, S. G. (2021).Dimensions.
In: The Routledge Companion to Philosophy of Physics, 666–678.
- Stevens (1946)Stevens, S. S. (1946).On the theory of scales of measurement.
Science103(2684), 677–680.
- Tao (2012)Tao, T. (2012).A mathematical formalisation of dimensional analysis.
https://terrytao.wordpress.com/2012/12/29/a-mathematical-formalisation-of-dimensional-analysis/[Accessed: July 2026].
- Uzan (2025)Uzan, J.-P. (2025).Fundamental constants: from measurement to the universe, a window on gravitation and cosmology.
Living Rev. Rel.28(1), 6.
- Weyl (1918)Weyl, H. (1918).Gravitation und Elektrizität.
Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin, 465–480.
(English translation:Gravitation and electricity, in O’Raifeartaigh (1997),The dawning of gauge theory. Princeton, NJ: Princeton University Press).
- Young (1999)Young, K. (1999).Foreign exchange market as a lattice gauge theory.
Am. J. Phys.67, 862–868.
- Zapata-Carratalá (2022)Zapata-Carratalá, C. (2022).Dimensioned Algebra: Mathematics with Physical Quantities.
La Matematica1, 849–885.

## 


- 


Major funding support from
