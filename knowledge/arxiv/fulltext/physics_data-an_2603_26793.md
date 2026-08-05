# Chiral moments make chiral measures

**arXiv ID**: 2603.26793v1
**Authors**: Emilio Pisanty, Nicola Mayer, Andrés Ordóñez, Alexander Löhr, Margarita Khokhlova
**Published**: 2026-03-25
**Categories**: physics.data-an, physics.optics, quant-ph
**Comments**: 8 pages main text, 24 pages with appendices and references
**HTML URL**: https://arxiv.org/html/2603.26793v1

## Abstract

We develop a family of chiral measures to quantify the chirality of a distribution and assign it a handedness. Our measures are built using the tensorial moments of the distribution, which naturally encode its spatial character, not only via its angular shape consistently with existing multipolar-moment approaches, but also its radial dependence. We combine these tensorial moments into a rotationally-invariant pseudoscalar using a newly-defined cross product and triple product for arbitrary symmetric tensors. We analyze these measures for a variety of toy-model distributions, providing intuition for the geometry and guiding the choice of chiral measure optimal for a given distribution. We also apply our measures to a physically-motivated example coming from photoionization in polychromatic chiral light. Our work provides a robust, flexible, intuitive, highly geometrical, and physically-driven framework for understanding and quantifying the chirality of a wide variety of distributions, together with an open-source software package that makes this toolbox readily applicable for the analysis of numerical or experimental data.

## Full Text

Chiral moments make chiral measures

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2603.26793v1 [physics.data-an] 25 Mar 2026

## Chiral moments make chiral measuresEmilio PisantyDepartment of Physics, King’s College London, Strand Campus, London WC2R 2LS, UKNicola MayerDepartment of Physics, King’s College London, Strand Campus, London WC2R 2LS, UKAndrés OrdóñezDepartment of Physics, Freie Universität Berlin, 14195 Berlin, GermanyAlexander LöhrMax Born Institute for Nonlinear Optics and Short Pulse Spectroscopy, Berlin, GermanyDepartment of Physics, Humboldt University, Berlin, GermanyMargarita KhokhlovaDepartment of Physics, King’s College London, Strand Campus, London WC2R 2LS, UK

## Abstract

We develop a family of chiral measures to quantify the chirality of a distribution and assign it a handedness.
Our measures are built using the tensorial moments of the distribution, which naturally encode its spatial character,
not only via its angular shape consistently with existing multipolar-moment approaches,
but also its radial dependence.
We combine these tensorial moments into a rotationally-invariant pseudoscalar using a newly-defined cross product and triple product for arbitrary symmetric tensors.
We analyze these measures for a variety of toy-model distributions, providing intuition for the geometry and guiding the choice of chiral measure optimal for a given distribution.
We also apply our measures to a physically-motivated example coming from photoionization in polychromatic chiral light.
Our work provides a robust, flexible, intuitive, highly geometrical, and physically-driven framework for understanding and quantifying the chirality of a wide variety of distributions,
together with an open-source software package that makes this toolbox readily applicable for the analysis of numerical or experimental data.

## IIntroduction

Chirality is an essential concept in our description of the world, capturing physical shapes, structures and dynamics in three-dimensional space, by defining whether a given object is equivalent to its mirror image[67].
Beyond abstract geometrical shapes,
we are surrounded by a kaleidoscope of chiral objects and structures:
from fundamental particles[141]and nuclei[114]all the way to cosmological structures[26,25],
passing by
liquid crystals[82,50],
nanoparticles and nanostructures[60,49,140,139,134,64,118,83]and bulk solid structures[41],
and, most importantly for human life, the homochiral biochemistry of organic molecules[39,47,16].
Even light itself can form chiral structures both in its spatial distribution[130,17]and in its evolution over time[8,91], often with deep links to the foundations of electromagnetism[27,35].

In all of these contexts, however, it is frequently not enough to know that an object is different from its mirror image: it is also necessary to understandhowdifferent the two versions are –
not just to identify chirality, but to quantify it.

A number of approaches have appeared over the years to fulfil this need[103,21,46].
Some rely on abstract geometry, quantifying the difference between a given shape and its mirror image[52,22,38,91]or between the shape and an achiral reference[21,137,142,2].
In these geometrical approaches, a central challenge is the assignment of a handedness to a given object, i.e., actively distinguishing the two mirror versions from each other, and labelling them as ‘left-handed’ or ‘right-handed’[116].

This problem is easier to solve in the chemical domain,
either via conventional priority rules used to describe the structural backbone of a molecule[24],
or through more observable-based approaches such as circular dichroism or optical rotatory power[34,44].
However, those methods rarely extend to structures beyond the molecular realm,
setting the demand for a robust and universal measure of chirality,
which is applicable both to concrete shapes as well as to more general distributions, and thus directly relevant to the vast array of experiments where the measured observable is a distribution.

As a general rule, we demand from a measure of chirality that it
(i) be independent of the orientation of the object,
(ii) be a continuous function of its shape, and
(iii) assign opposite signs to mirror-image objects.
For semantic clarity, for quantities that can detect chirality, but are unable to assign a handedness, we use the term ‘measure of asymmetry’.

An important and unavoidable feature of any such measures of chirality is the so-called ‘rubber-glove theorem’[136,138,56,84](also known as ‘chiral connectedness’[46,86]):
informally, given a left-handed rubber glove, it is possible to pull it inside out, finger by finger, so that it becomes a right-handed glove without passing at any time through an achiral or mirror-symmetric configuration.
For a continuous chirality measure, this smooth passage between positive and negative values implies that at some point the measure must pass by zero, but, since the object is never achiral, that vanishing-measure point must occur for a chiral object:
in other words, the measure must have a ‘blind spot’.
The presence of such blind spots is generic and expected, with two important consequences.
Firstly, if we wish to quantify the chirality of a wide variety of shapes, we should expect to need a family of different measures[113], with different measures covering different blind spots.
Secondly, since different measures of the same family can disagree on the handedness of shapes, it is rarely possible to provide an absolute assignment of handedness, as it is challenging to give any priority within such a family.
That said, every member of the family still provides a valid sense of handedness for the shapes that it describes.

Perhaps the most attractive option currently available for quantifying the chirality of a distribution is based on the multipolar moments of the distribution[56,98,90,57], which are then combined into a pseudo-scalar using the angular-momentum algebra of the rotation group,SO​(3)\mathrm{SO}(3).
These provide robust and flexible measures, but their wide-scale application is held back by unintuitive forms and a lack of connection to the real-space geometries they represent, as well as to the physics embodied in those geometries.

In this work, we develop a robust family of chirality measures for arbitrary distributions, based on the distributions’ tensorial moments𝐌(k)\mathbf{M}^{(k)}.
We show that these measures take intuitive forms that are easily recognizable as ‘chiral moments’,
given by newly-defined triple tensor products of the tensorial moments,
and taking the formχn1​n2​n3=(𝐌(n1)×𝐌(n2))(n3)

∙𝐌(n3).\displaystyle\chi_{n_{1}n_{2}n_{3}}=\left(\mathbf{M}^{(n_{1})}\ignorespaces\times\ignorespaces\mathbf{M}^{(n_{2})}\right)^{(n_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{M}^{(n_{3})}.

These factorized forms are simple enough to be calculated by hand, providing a clear link to the geometries and physical processes involved.
We show these measures in action on illustrative and didactic toy-model distributions.
Finally, as a concrete illustration, inspired by recent progress in ultrafast physics and increasing demand in chiral photoelectron spectroscopy[79,112,33,42,66,124,125,126,127,70,71,51,109,89,12,55,132,59,69], we demonstrate their capabilities on the specific example of the photoelectron momentum distribution produced by resonance-enhanced multiphoton ionization of hydrogen driven by synthetic chiral light.

Our software implementation of this formalism is available as the open-source packageChimerain the Wolfram Language[105];
the specific implementation of the results presented here is available at Ref.[106].

## IIChiral moments

In one dimension, a distributionρ​(x)\rho(x)is described by its moments,M(n)=∫xn​ρ​(x)​d​xM^{(n)}=\int x^{n}\rho(x)\textrm{d}x, a sequence of scalars measuring spatial aspects of its shape.
Similarly, to characterize a three-dimensional distributionρ​(𝐫)\rho(\mathbf{r}), one can use its tensorial moments,𝐌(n)=∫𝐫⊗n​ρ​(𝐫)​d​𝐫,\displaystyle\mathbf{M}^{(n)}=\int\mathbf{r}^{\otimes n}\rho(\mathbf{r})\textrm{d}\mathbf{r},(1)

where𝐫⊗n=𝐫⊗⋯⊗𝐫\mathbf{r}^{\otimes n}=\mathbf{r}\otimes\cdots\otimes\mathbf{r}is thenn-fold tensor product of𝐫\mathbf{r}with itself, andnnis the rank of the tensorial moment.
This tensor of ranknnis the object whose components in a Cartesian frame areMi1​⋯​in(n)=∫xi1​⋯​xin​ρ​(𝐫)​d​𝐫,\displaystyle M^{(n)}_{i_{1}\cdots i_{n}}=\int x_{i_{1}}\cdots x_{i_{n}}\rho(\mathbf{r})\textrm{d}\mathbf{r},(2)

with each of thennindices,i1i_{1}throughini_{n}, ranging independently overx,y,zx,y,z.
We include, in AppendixC, a brief summary of the relevant tensor algebra.

The so-called ‘unabridged’ or ‘primitive’ tensorial moments𝐌(n)\mathbf{M}^{(n)}[111,6,143]are typically reduced to the tensorial multipolar moments[111,6]𝝁(ℓ)=Π^ℓ​𝐌(ℓ),\displaystyle\boldsymbol{\mu}^{(\ell)}=\hat{\Pi}_{\ell}\mathbf{M}^{(\ell)},(3)

using a trace-removal projectorΠ^ℓ\hat{\Pi}_{\ell},
which we motivate and define in AppendixC;
the tensorial moment of rankn=ℓn=\ellprovides the2ℓ2^{\ell}-polar moment.
The tensorial multipolar moments form irreducible representations of the rotation groupSO​(3)\mathrm{SO}(3), and they are fully determined by a minimal set of linearly-independent components,
as we explore in detail in AppendixC.4.
These components are the spherical multipolar momentsMℓ​m\displaystyle M_{\ell m}=∫Sℓ​m​(𝐫)​ρ​(𝐫)​d​𝐫,\displaystyle=\int S_{\ell m}(\mathbf{r})\rho(\mathbf{r})\textrm{d}\mathbf{r},(4)

defined as integrals against the solid harmonic polynomialSℓ​m​(𝐫)=4​π2​ℓ+1​rℓ​Yℓ​m​(θ,ϕ)S_{\ell m}(\mathbf{r})=\sqrt{\frac{4\pi}{2\ell+1}}\>r^{\ell}\>Y_{\ell m}(\theta,\phi).

As a general rule, the spherical multipolar momentsMℓ​mM_{\ell m}capture the details of the angular shape of the distributionρ​(𝐫)\rho(\mathbf{r})projected to the unit sphere.
The unabridged moment tensors𝐌(ℓ)\mathbf{M}^{(\ell)}, on the other hand, also capture this information, while including additional information about the radial structure of the distribution.
Due to their simplicity and generality, we aim to build our chiral measure directly from the latter.

The chiral measure has to be a single pseudoscalar, which we build out of the tensorial moments, as a linear combination of products of their components.
We find that the simplest such pseudoscalar requires three tensorial moments, in the shape of a tensorial triple product,
which we define for symmetric tensors as(𝐀(n1)×𝐁(n2))(n3)

∙𝐂(n3)\displaystyle\left(\mathbf{A}^{(n_{1})}\ignorespaces\times\ignorespaces\mathbf{B}^{(n_{2})}\right)^{(n_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{C}^{(n_{3})}=ϵi1​i2​i3​Ai1​𝐣𝐤​Bi2​𝐣𝐥​Ci3​𝐤𝐥,\displaystyle=\epsilon_{i_{1}i_{2}i_{3}}A_{i_{1}\mathbf{j}\mathbf{k}}B_{i_{2}\mathbf{j}\mathbf{l}}C_{i_{3}\mathbf{k}\mathbf{l}},(5)

as we detail in AppendicesAandC.
Here𝐣=(j1​⋯​jm)\mathbf{j}=(j_{1}\cdots j_{m}),𝐤=(k1​⋯​kn)\mathbf{k}=(k_{1}\cdots k_{n})and𝐥=(l1​⋯​lp)\mathbf{l}=(l_{1}\cdots l_{p})are multi-indices of lengthsm=12​(n1+n2−n3−1)m=\frac{1}{2}(n_{1}+n_{2}-n_{3}-1),n=12​(n1+n3−n2−1)n=\frac{1}{2}(n_{1}+n_{3}-n_{2}-1)andp=12​(n2+n3−n1−1)p=\frac{1}{2}(n_{2}+n_{3}-n_{1}-1).
This tensorial triple product has the form of a full contraction of the third factor,𝐂(n3)\mathbf{C}^{(n_{3})}, with a newly-defined tensorial cross product(𝐀(n1)×𝐁(n2))i3​𝐤𝐥(n3)=\trigbraces​𝒮^i3​𝐤𝐥​ϵi1​i2​i3​Ai1​𝐣𝐤​Bi2​𝐣𝐥\left(\mathbf{A}^{(n_{1})}\ignorespaces\times\ignorespaces\mathbf{B}^{(n_{2})}\right)^{(n_{3})}_{i_{3}\mathbf{k}\mathbf{l}}=\trigbraces{\hat{\mathcal{S}}}_{i_{3}\mathbf{k}\mathbf{l}}\epsilon_{i_{1}i_{2}i_{3}}A_{i_{1}\mathbf{j}\mathbf{k}}B_{i_{2}\mathbf{j}\mathbf{l}},
where\trigbraces​𝒮^i3​𝐤𝐥\trigbraces{\hat{\mathcal{S}}}_{i_{3}\mathbf{k}\mathbf{l}}denotes full symmetrisation over the indicesi3​𝐤𝐥i_{3}\mathbf{k}\mathbf{l},
which we define in detail in AppendixC.
We thus have a family of chiral measures,χn1​n2​n3=(𝐌(n1)×𝐌(n2))(n3)

∙𝐌(n3),\displaystyle\chi_{n_{1}n_{2}n_{3}}=\left(\mathbf{M}^{(n_{1})}\ignorespaces\times\ignorespaces\mathbf{M}^{(n_{2})}\right)^{(n_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{M}^{(n_{3})},(6)

coming from the different possible combinations of tensor ranksnin_{i}, and which carry the imprint of different types of chiral shapes of the distribution.

These chiral measures can be re-expressed into more straightforward forms by expanding the integral form (1) of the individual tensor factors, which gives us the equivalent expressionsχn1​n2​n3\displaystyle\chi_{n_{1}n_{2}n_{3}}=∭d​𝐫1​d​𝐫2​d​𝐫3​ρ​(𝐫1)​ρ​(𝐫2)​ρ​(𝐫3)\displaystyle=\iiint\textrm{d}\mathbf{r}_{1}\textrm{d}\mathbf{r}_{2}\textrm{d}\mathbf{r}_{3}\rho(\mathbf{r}_{1})\rho(\mathbf{r}_{2})\rho(\mathbf{r}_{3})(7a)(𝐫1⊗n1×𝐫2⊗n2)(n3)

∙𝐫3⊗n3\displaystyle\qquad\qquad\quad\left(\mathbf{r}_{1}^{\otimes n_{1}}\ignorespaces\times\ignorespaces\mathbf{r}_{2}^{\otimes n_{2}}\right)^{(n_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{r}_{3}^{\otimes n_{3}}=∭d​𝐫1​d​𝐫2​d​𝐫3​ρ​(𝐫1)​ρ​(𝐫2)​ρ​(𝐫3)\displaystyle=\iiint\textrm{d}\mathbf{r}_{1}\textrm{d}\mathbf{r}_{2}\textrm{d}\mathbf{r}_{3}\rho(\mathbf{r}_{1})\rho(\mathbf{r}_{2})\rho(\mathbf{r}_{3})(7b)[(𝐫1×𝐫2)⋅𝐫3]​(𝐫1⋅𝐫2)m​(𝐫1⋅𝐫3)n​(𝐫2⋅𝐫3)p.\displaystyle\qquad\quad\left[(\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}\right](\mathbf{r}_{1}\cdot\mathbf{r}_{2})^{m}(\mathbf{r}_{1}\cdot\mathbf{r}_{3})^{n}(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{p}.

Our chiral measures are thus revealed as
three-point correlation functions (three copies ofρ​(𝐫)\rho(\mathbf{r})evaluated at different points, integrated against a chiral correlation kernel),
and they have the general structure of a moment: a distribution integrated against a polynomial.
We therefore call our chiral measureχn1​n2​n3\chi_{n_{1}n_{2}n_{3}}a ‘chiral moment’ of the distributionρ​(𝐫)\rho(\mathbf{r}).

A similar chiral moment can be formed from the traceless version of the tensorial moments, the tensorial multipolar moments,
given naturally ashℓ1​ℓ2​ℓ3=(𝝁(ℓ1)×𝝁(ℓ2))(ℓ3)

∙𝝁(ℓ3).\displaystyle h_{\ell_{1}\ell_{2}\ell_{3}}=\left(\boldsymbol{\mu}^{(\ell_{1})}\ignorespaces\times\ignorespaces\boldsymbol{\mu}^{(\ell_{2})}\right)^{(\ell_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\boldsymbol{\mu}^{(\ell_{3})}.(8)

This traceless chiral momenthℓ1​ℓ2​ℓ3h_{\ell_{1}\ell_{2}\ell_{3}}is a pseudoscalar formed from threeSO​(3)\mathrm{SO}(3)irreducible representations.
As such, the representation theory ofSO​(3)\mathrm{SO}(3)constrains it[54]to have the formhℓ1​ℓ2​ℓ3∝∑m1​m2​m3(ℓ1ℓ2ℓ3m1m2m3)​Mℓ1​m1​Mℓ2​m2​Mℓ3​m3,h_{\ell_{1}\ell_{2}\ell_{3}}\propto\sum_{m_{1}m_{2}m_{3}}\!\!\!\begin{pmatrix}\ell_{1}&\ell_{2}&\ell_{3}\\
m_{1}&m_{2}&m_{3}\end{pmatrix}M_{\ell_{1}m_{1}}M_{\ell_{2}m_{2}}M_{\ell_{3}m_{3}},(9)

as a linear combination of the linearly-independent components, the spherical multipolar momentsMℓ​mM_{\ell m},
with linear-combination coefficients given by Wigner3​j3jsymbols.
This form is the sharpest existing expression of the formalism in the literature, and it has been used previously from molecular chirality[56,98,90,57,99,108]through to cosmological contexts[26,25].
For the traceless chiral moments, the correlation kernel takes the form(Π^ℓ1​𝐫1⊗ℓ1×Π^ℓ2​𝐫2⊗ℓ2)(ℓ3)

∙Π^ℓ3​𝐫3⊗ℓ3\left(\hat{\Pi}_{\ell_{1}}\mathbf{r}_{1}^{\otimes\ell_{1}}\ignorespaces\times\ignorespaces\hat{\Pi}_{\ell_{2}}\mathbf{r}_{2}^{\otimes\ell_{2}}\right)^{(\ell_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\hat{\Pi}_{\ell_{3}}\mathbf{r}_{3}^{\otimes\ell_{3}},
and it can be shown to equal the scalar tripolar spherical harmonic[133];
we provide explicit forms in AppendixB.

On the intuitive side, the tensorial triple product behaves similarly to the usual triple product between vectors,(𝐚×𝐛)⋅𝐜(\mathbf{a}\times\mathbf{b})\cdot\mathbf{c}.
Thus, in the same way that the cross product of a vector with itself vanishes,𝐚×𝐚=0,\mathbf{a}\times\mathbf{a}=0,the cross product of a tensor with itself also vanishes,(𝐌(n)×𝐌(n))(n′)=0,\left(\mathbf{M}^{(n)}\ignorespaces\times\ignorespaces\mathbf{M}^{(n)}\right)^{(n^{\prime})}=0,regardless of the desired rankn′n^{\prime}.
As a consequence, obtaining a nonzero tensorial triple product (and, therefore, a nonzero chiral moment) requires taking three different tensorial factors.

To satisfy this, there are two distinct options.
The first option is to assemble the chiral moment out of three different ranks of tensorial moment, in which case the first nontrivial example isχ234\chi_{234}.111The next nontrivial examples areχ245\chi_{245},χ256\chi_{256}andχ346\chi_{346}.The second option is to assemble the chiral moment using tensor factors of equal ranks, e.g. attempting to buildχ111\chi_{111},
in which case we must use tensorial moments with additional radial factors,
introducing powers ofr2r^{2}into the definition of𝐌(n)\mathbf{M}^{(n)}to yield tensor-valued moments of higher polynomial orders,𝐌(n,2​q)=∫𝐫⊗n​r2​q​ρ​(𝐫)​d​𝐫=Trq⁡(𝐌(n+2​q)),\displaystyle\mathbf{M}^{(n,2q)}=\int\mathbf{r}^{\otimes n}r^{2q}\rho(\mathbf{r})\textrm{d}\mathbf{r}=\Tr^{q}(\mathbf{M}^{(n+2q)}),(10)

which are directly given as theqq-fold trace of the higher-order tensorial moment𝐌(n+2​q)\mathbf{M}^{(n+2q)}.
By extension, these also give rise to higher-order traceless tensorial multipolar moments𝝁(ℓ,2​q)=Π^ℓ​𝐌(ℓ,2​q)\boldsymbol{\mu}^{(\ell,2q)}=\hat{\Pi}_{\ell}\mathbf{M}^{(\ell,2q)}.222As an alternative approach to achieve this, one can restrict the integration to different spherical shells for the different tensorial-moment factors inχn1​n2​n3\chi_{n_{1}n_{2}n_{3}};
this yields useful chiral moments which will be explored in future work.In what follows, we explore both options.

## IIIAnalytical examples

We now turn to specific examples of chiral distributions, to show our chiral moments in action as chiral measures.
We start with the simplest example of a chiral distribution, and we work our way up in complexity.

We construct our examples using gaussian distributions. For notational convenience, we write an arbitrary gaussian distribution asGΣ​(𝐫)=(2​π​det⁡(Σ))−3/2​e−12​𝐫​Σ−1​𝐫,\displaystyle G_{\Sigma}(\mathbf{r})={(2\pi\det(\Sigma))^{-3/2}}\ e^{-\frac{1}{2}\mathbf{r}\Sigma^{-1}\mathbf{r}},(11)

centred at the origin, whereΣi​j\Sigma_{ij}is the covariance matrix of the distribution, which determines its width and orientation, and which can be shown to equal the second-order momentsΣi​j=∫xi​xj​GΣ​(𝐫)​d​𝐫.\displaystyle\Sigma_{ij}=\int x_{i}x_{j}G_{\Sigma}(\mathbf{r})\textrm{d}\mathbf{r}.(12)

When the reference frame is aligned with the principal axes of the gaussian, this takes the formΣ=diag​(σ12,σ22,σ32)\Sigma=\mathrm{diag}(\sigma_{1}^{2},\sigma_{2}^{2},\sigma_{3}^{2}), in which case its diagonal entries, the variancesσi2\sigma_{i}^{2}, are the squares of the corresponding standard deviationsσi\sigma_{i}.

## III.1The triple-dipole case:χ111\chi_{111}

The simplest chiral distribution is a combination of three spherical gaussians of equal varianceσ2\sigma^{2}at different positions,ρ3​G​(𝐫)\displaystyle\rho_{\mathrm{3G}}(\mathbf{r})=13​∑i=13Gσ2​𝕀​(𝐫−𝐫i),\displaystyle=\frac{1}{3}\sum_{i=1}^{3}G_{\sigma^{2}\mathbb{I}}(\mathbf{r}-\mathbf{r}_{i}),(13)

as shown in Fig.1(a).
Intuitively, so long as the vectors from the origin to the three centres of the gaussians form a non-coplanar set, with a nonzero triple product,(𝐫1×𝐫2)⋅𝐫3(\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3},
the distribution itself is chiral.

It is tempting to attempt to extract this triple product of the centres through the triple tensorial product of rankn=1n=1,(𝐌(1)×𝐌(1))(1)

∙𝐌(1)(\mathbf{M}^{(1)}\times\mathbf{M}^{(1)})^{(1)}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{M}^{(1)}, but, as discussed above, this vanishes due to its symmetry.
To build a suitable chiral measure, then, we use the tensorial moments with added radial factors𝐌(n,2​q)\mathbf{M}^{(n,2q)}as defined in (10).333In nuclear physics, the moment𝐌(1,2)=∫r2​𝐫​ρ​(𝐫)​d​𝐫\mathbf{M}^{(1,2)}=\int r^{2}\>\mathbf{r}\>\rho(\mathbf{r})\textrm{d}\mathbf{r}is known as the Schiff moment[117,45].In this spirit, then, we defineχ111024=(𝐌(1)×𝐌(1,2))(1)

∙𝐌(1,4).\displaystyle\chi_{111}^{024}=\left(\mathbf{M}^{(1)}\ignorespaces\times\ignorespaces\mathbf{M}^{(1,2)}\right)^{(1)}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{M}^{(1,4)}.(14)

For our triple-gaussian example, it is a simple calculation to show thatχ111024\displaystyle\chi_{111}^{024}=127​(r12−r22)​(r22−r32)​(r32−r12)​(𝐫1×𝐫2)⋅𝐫3.\displaystyle=\frac{1}{27}(r_{1}^{2}-r_{2}^{2})(r_{2}^{2}-r_{3}^{2})(r_{3}^{2}-r_{1}^{2})(\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}.(15)

As expected, this returns a vanishing chirality if any of the radii coincide.444Moreover, the scalar factor(r12−r22)​(r22−r32)​(r32−r12)(r_{1}^{2}-r_{2}^{2})(r_{2}^{2}-r_{3}^{2})(r_{3}^{2}-r_{1}^{2})can be recognised as the Vandermonde determinantdet(111r12r22r32r14r24r34)\det\mathopen{}\begin{pmatrix}1&1&1\\
r_{1}^{2}&r_{2}^{2}&r_{3}^{2}\\
r_{1}^{4}&r_{2}^{4}&r_{3}^{4}\end{pmatrix}.Figure 1:(a) Triple-gaussian distributionρ3​G​(𝐫)\rho_{\mathrm{3G}}(\mathbf{r}), with the gaussians centred at𝐫1=𝐞^x\mathbf{r}_{1}=\hat{\mathbf{e}}_{x},𝐫2=2​𝐞^y\mathbf{r}_{2}=2\hat{\mathbf{e}}_{y}and𝐫3=3​𝐞^z\mathbf{r}_{3}=3\hat{\mathbf{e}}_{z}, and with standard deviationσ=1\sigma=1.
The central 3D figure shows contours of equal probability, with the auxiliary projections to each plane showing the corresponding marginal distribution.
(b)Vellela vellela-type distributionρv​v​(𝐫)\rho_{vv}(\mathbf{r}), with two vertically-displaced elongated gaussians, settingσ1=2\sigma_{1}=2,σ2=4\sigma_{2}=4,σsm=1/2\sigma_{\mathrm{sm}}=1/2andz0=−3/2z_{0}=-3/2, with twist angleθ=45°\theta=$45\text{\,}\mathrm{\SIUnitSymbolDegree}$.

For this triple-gaussian case, it is important to note that the chiral measureχ111024\chi_{111}^{024}only makes sense for distributions for which the origin of the variable𝐫\mathbf{r}is well defined.
This is the case e.g. for photoelectron momentum spectra, where𝐩=0\mathbf{p}=0corresponds to zero kinetic energy.
However, there are also many cases of distributions, particularly spatial ones, where translational invariance makes this measure meaningless.555A related chirality measure is available that avoids this issue.
For a chiral configuration ofN≥4N\geq 4gaussians, the origin can be set at the centre of mass, such that𝐌(1)=0\mathbf{M}^{(1)}=0.
In this case,χ111246\chi_{111}^{246}is an appropriate chirality measure and is now independent of the initial location of the origin.

As a brief note, in this case, the corresponding traceless chiral momenth111024h_{111}^{024}coincides withχ111024\chi_{111}^{024}.

## III.2The double-quadrupole case:χ221\chi_{221}

We now climb one step up in complexity, to a distribution with quadrupolar (ℓ=2\ell=2) structure.
The first nontrivial chirality measure here isχ221\chi_{221}, which, as before, contains two repeatedℓ\ell’s, i.e., two independent quadrupole moments.
The double-quadrupole chiral measure requires adding a radial factor to one of the tensorial moments:χ221020=(𝐌(2)×𝐌(2,2))(1)

∙𝐌(1).\displaystyle\chi_{221}^{020}=\left(\mathbf{M}^{(2)}\ignorespaces\times\ignorespaces\mathbf{M}^{(2,2)}\right)^{(1)}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{M}^{(1)}.(16)

To construct an explicit example of a distribution with nonzeroχ221020\chi_{221}^{020}, we take two elongated gaussians, with different lengths (to make𝐌(2)\mathbf{M}^{(2)}and𝐌(2,2)\mathbf{M}^{(2,2)}distinct), at an angleθ\thetato each other, and we displace them along the direction of the tensor cross product(𝐌(2)×𝐌(2,2))(1)\left(\mathbf{M}^{(2)}\ignorespaces\times\ignorespaces\mathbf{M}^{(2,2)}\right)^{(1)},
as shown in Figure1.
Thus, we takeρv​v​(𝐫)\displaystyle\rho_{vv}(\mathbf{r})=w1​GΣ1​(𝐫)+w2​GRz​(θ)​Σ2​Rz−1​(θ)​(𝐫−𝐫0),\displaystyle=w_{1}G_{\Sigma_{1}}(\mathbf{r})+w_{2}G_{R_{z}(\theta)\Sigma_{2}R_{z}^{-1}(\theta)}(\mathbf{r}-\mathbf{r}_{0}),(17)

where the covariance matrices of the two components are given byΣi=diag​(σi2,σsm2,σsm2)\Sigma_{i}=\mathrm{diag}(\sigma_{i}^{2},\sigma_{\mathrm{sm}}^{2},\sigma_{\mathrm{sm}}^{2}),
with a common small-axis varianceσsm2\sigma_{\mathrm{sm}}^{2},Σ2\Sigma_{2}has been rotated by an angleθ\thetaabout thezzaxis through the matrixRz(θ)R_{z}\mathopen{}(\theta)\mathclose{},
the second gaussian has been displaced by𝐫0=z0​𝐞^z\mathbf{r}_{0}=z_{0}\hat{\mathbf{e}}_{z},
and the weightswiw_{i}add tow1+w2=1w_{1}+w_{2}=1.

We encounter here our first cross product between tensors,666This cross product between rank-2 tensors has been used previously in continuum mechanics[128,19,1], introduced (to our knowledge) in Ref.[37].and, for this case, it essentially captures the cross product between the major axes of the two gaussians,
while allowing for their ambiguity in sign,
and it is given by(𝐌(2)×𝐌(2,2))(1)\displaystyle\left(\mathbf{M}^{(2)}\ignorespaces\times\ignorespaces\mathbf{M}^{(2,2)}\right)^{(1)}=C​w1​w2​sin⁡(2​θ)​𝐞^z,\displaystyle=Cw_{1}w_{2}\sin(2\theta)\hat{\mathbf{e}}_{z},(18)

whereC=12​(z02−3​σ12+3​σ22)​(σ12−σsm2)​(σ22−σsm2)C=\frac{1}{2}(z_{0}^{2}-3\sigma_{1}^{2}+3\sigma_{2}^{2})(\sigma_{1}^{2}-\sigma_{\mathrm{sm}}^{2})(\sigma_{2}^{2}-\sigma_{\mathrm{sm}}^{2}).
When contracted with the dipole moment of the distribution,𝐌(1)=w2​z0​𝐞^z\mathbf{M}^{(1)}=w_{2}z_{0}\hat{\mathbf{e}}_{z},
this gives us the chiral momentχ221020=C​w1​w22​z0​sin⁡(2​θ).\displaystyle\chi_{221}^{020}=Cw_{1}w_{2}^{2}z_{0}\sin(2\theta).(19)

The dependence onsin⁡(2​θ)\sin(2\theta)captures the fact that atθ=90°\theta=$90\text{\,}\mathrm{\SIUnitSymbolDegree}$the distribution admits mirror symmetry planes along thex​zxzandy​zyzaxes, and is therefore achiral.

We get an identical value for the traceless chiral momenth221020h_{221}^{020}, since the traceless quadrupole moments𝝁(2)\boldsymbol{\mu}^{(2)}differ from the𝐌(2)\mathbf{M}^{(2)}by a factor of the isotropic tensor𝕀\mathbb{I}, whose cross products vanish.

This type of chirality is exhibited in nature by the hydrozoanVelella velella[29,28](also known as by-the-wind sailor),
and it is also seen in man-made objects such as oblique-wing aircraft[88];
it also corresponds to molecules with two independent quadrupole tensors, such as polarizabilities at different frequencies, and a permanent dipole moment[29,28].

## III.3The helical case:χ234\chi_{234}

As our third analytical example, we now turn to the first chiral measure which is fully flexible,χ234\chi_{234}.
The flexibility comes from involving three different tensor ranks, which allows measuring the chirality of a distribution confined to a single spherical shell.
That stands in contrast to our previous examples, which required including the radial structure of the distribution (by replacing𝐌(n)\mathbf{M}^{(n)}with𝐌(n,2​q)\mathbf{M}^{(n,2q)}) and thus can only describe chirality which is spread over multiple spherical ‘shells’ of different radii.
In essence, this measure is formed from the combination of a quadrupole, octupole and hexadecapole moments – which can also be taken as traceless moments viah234h_{234}[56]– and captures their relative shape and orientation.

In geometrical terms, this chirality measure is best suited to describe helical structures, and carries the imprint of the local pitch of the helix, which can be double- or triple-stranded.
That said, given the wider variety of geometries captured by octupolar and hexadecapolar moments, this chiral moment also extends to a wider class of shapes.

To provide an explicit analytical exampleρhelix​(𝐫)\rho_{\mathrm{helix}}(\mathbf{r}), we consider the combination ofN=2,3N=2,3gaussian distributions centred at equispaced points in the(x,y)(x,y)plane at radiusr0r_{0}, with variances(σ12,σ12,σ22)(\sigma_{1}^{2},\sigma_{1}^{2},\sigma_{2}^{2}), and rotated by an angleα\alphaabout the axis that connects them to the origin.
This distribution thus has the probability densityρhelix​(𝐫)\displaystyle\rho_{\mathrm{helix}}(\mathbf{r})=1N∑j=1NGRx​(α)​Σ−1​Rx−1​(α)(Rz−1(2​π​jN)𝐫−𝐫0),\displaystyle=\frac{1}{N}\sum_{j=1}^{N}G_{R_{x}(\alpha)\Sigma^{-1}R_{x}^{-1}(\alpha)}\mathopen{}\left(R_{z}^{-1}(\tfrac{2\pi j}{N})\mathbf{r}-\mathbf{r}_{0}\right),(20)

where the covariance matrixΣ=diag​(σ12,σ12,σ22)\Sigma=\mathrm{diag}(\sigma_{1}^{2},\sigma_{1}^{2},\sigma_{2}^{2})is rotated along thexxaxis byRx(α)R_{x}\mathopen{}(\alpha)\mathclose{},
and the centroid𝐫0=r0​𝐞^x\mathbf{r}_{0}=r_{0}\hat{\mathbf{e}}_{x}is then rotated about thezzaxis byRz(2​π​jN)R_{z}\mathopen{}(\tfrac{2\pi j}{N})\mathclose{}.
We show examples in Figure2.Figure 2:Helix-gaussian distributionsρhelix​(𝐫)\rho_{\mathrm{helix}}(\mathbf{r})for (a)N=2N=2and (b)N=3N=3gaussians.
We setσ1=1/2\sigma_{1}=1/2,σ2=3/2\sigma_{2}=3/2,r0=1r_{0}=1, and use twist angleα=22.5°\alpha=$22.5\text{\,}\mathrm{\SIUnitSymbolDegree}$.

For the case ofN=2N=2gaussians, the chiral moment can be calculated analytically to beχ234\displaystyle\chi_{234}=−116r0Δ2[8r02(r02+Δ)\displaystyle=-\frac{1}{16}r_{0}\Delta^{2}\bigg[8r_{0}^{2}(r_{0}^{2}+\Delta)(21)+3Δ2(1−cos⁡(4​α))]sin⁡(4​α),\displaystyle\qquad\qquad\qquad+3\Delta^{2}(1-\cos(4\alpha))\bigg]\sin(4\alpha),

whereΔ=σ12−σ22\Delta=\sigma_{1}^{2}-\sigma_{2}^{2},
with the traceless chiral moment given byh234\displaystyle h_{234}=−1112r0Δ2[8r02(7r02+9Δ)\displaystyle=-\frac{1}{112}r_{0}\Delta^{2}\bigg[8r_{0}^{2}(7r_{0}^{2}+9\Delta)(22)+21Δ2(1−cos⁡(4​α))]sin⁡(4​α).\displaystyle\qquad\qquad\qquad+21\Delta^{2}(1-\cos(4\alpha))\bigg]\sin(4\alpha).

As in the previous case, the distribution is achiral whenα=45°\alpha=$45\text{\,}\mathrm{\SIUnitSymbolDegree}$.

Similarly, for the case ofN=3N=3gaussians, the chiral moment is given byχ234\displaystyle\chi_{234}=−3128​r0​Δ​sin⁡(2​α)​(2​r02+Δ​(1−cos⁡(2​α)))\displaystyle=-\frac{3}{128}r_{0}\Delta\sin(2\alpha)\left(2r_{0}^{2}+\Delta(1{-}\cos(2\alpha))\right)(23)×(4​r02​(r02+2​Δ)+3​Δ2​(1+3​cos⁡(2​α))​(1−cos⁡(2​α))).\displaystyle\times\left(4r_{0}^{2}(r_{0}^{2}{+}2\Delta)+3\Delta^{2}(1{+}3\cos(2\alpha))(1{-}\cos(2\alpha))\right).

In contrast to theN=2N=2case, however, for theN=3N=3geometry the traceless chiral moment coincides with the unabridged one, i.e.,h234=χ234h_{234}=\chi_{234}.

This difference in behaviour between theN=2N=2andN=3N=3geometries is remarkable and merits a closer look.
The two chiral moments involved,χ234\chi_{234}(in terms of𝐌(n)\mathbf{M}^{(n)}andh234h_{234}(in terms of𝝁(ℓ)\boldsymbol{\mu}^{(\ell)})
contain largely similar ingredients.
The key difference between them is the passage from𝐌(4)\mathbf{M}^{(4)}to𝝁(4)\boldsymbol{\mu}^{(4)}, which differ from each other by a term proportional to\trigbraces​𝒮^​(𝝁(2,2)⊗𝕀)\trigbraces{\hat{\mathcal{S}}}(\boldsymbol{\mu}^{(2,2)}\otimes\mathbb{I})(see AppendixCfor details).
This term then shows up in the difference between the two chiral moments,777Specifically,χ234−h234=(𝝁(2)×𝝁(3))(4)

∙67​\trigbraces​𝒮^​(𝝁(2,2)⊗𝕀)\chi_{234}-h_{234}=\left(\boldsymbol{\mu}^{(2)}\ignorespaces\times\ignorespaces\boldsymbol{\mu}^{(3)}\right)^{(4)}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\tfrac{6}{7}\trigbraces{\hat{\mathcal{S}}}(\boldsymbol{\mu}^{(2,2)}\otimes\mathbb{I}),
which can then be rearranged into−27​(𝝁(2)×𝝁(2,2))(3)

∙𝝁(3)-\tfrac{2}{7}\left(\boldsymbol{\mu}^{(2)}\ignorespaces\times\ignorespaces\boldsymbol{\mu}^{(2,2)}\right)^{(3)}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\boldsymbol{\mu}^{(3)}.giving rise to a lower-rank chiral moment:χ234−h234\displaystyle\chi_{234}-h_{234}=−27​h223020=−27​χ223020,\displaystyle=-\tfrac{2}{7}h_{223}^{020}=-\tfrac{2}{7}\chi_{223}^{020},(24)

independently ofNN.

This last chiral moment is an interesting and significant chiral measure in its own right, and it provides a particularly simple chiral measure forρhelix​(𝐫)\rho_{\mathrm{helix}}(\mathbf{r})in the case ofN=2N=2, where it is given byχ223020\displaystyle\chi_{223}^{020}=−12​r03​Δ3​sin⁡(4​α).\displaystyle=-\frac{1}{2}r_{0}^{3}\Delta^{3}\sin(4\alpha).(25)

This case represents the simplest instance where a rank-3-valued tensor cross product relates directly to critical physical and geometrical features,
more specifically the tensor cross product(𝐌(2)×𝐌(2,2))(3)\displaystyle\left(\mathbf{M}^{(2)}\ignorespaces\times\ignorespaces\mathbf{M}^{(2,2)}\right)^{(3)}=−2​r02​Δ2​cos⁡(2​α)​\trigbraces​𝒮^​(𝐞^x⊗𝐞^y⊗𝐞^z),\displaystyle=-2r_{0}^{2}\Delta^{2}\cos(2\alpha)\>\trigbraces{\hat{\mathcal{S}}}(\hat{\mathbf{e}}_{x}\otimes\hat{\mathbf{e}}_{y}\otimes\hat{\mathbf{e}}_{z}),(26)

valid forN=2N=2.
This is a tensor cross product between rank-2 tensors, both of which are diagonal in thex​y​zxyzreference frame, but which have different eigenvalues along those principal axes.

By contrast, for theN=3N=3geometry, the two quadrupole tensors𝐌(2)\mathbf{M}^{(2)}and𝐌(2,2)\mathbf{M}^{(2,2)}are linearly dependent,
because the three-fold symmetry ofρhelix​(𝐫)\rho_{\mathrm{helix}}(\mathbf{r})requires both tensors to be axially symmetric about thezzaxis.
Since the two are linearly dependent, their cross product vanishes, as (therefore) does the difference betweenχ234\chi_{234}andh234h_{234}.

## IVChiral photoelectron momentum distributions

Having explored the application of our chiral measures to toy-model distributions, we now turn to a concrete physical object.
Our object of choice is the photoelectron momentum distribution arising from ionization by synthetic chiral light[8,79,66,51].

Light has been a useful tool to probe chiral matter since the introduction of chirality[101,67].
Historically, light used to probe chiral matter has been circularly polarized, for which the chiral optical interaction is based on magnetic-dipole and electric-quadrupole effects, where the optical chirality is described through the spatial pitch of the circular-polarization helix.
Methods based on this interaction, including optical rotation and circular dichroism[34], are effective and form the gold standard for optically thick samples.

For optically thin samples, on the other hand, the length-scale mismatch between the wavelength-scale helical pitch and the size of typical chiral molecules makes these effects relatively weak[10].
For these cases, chiral photoelectron spectroscopy has emerged over the past two decades, allowing the use of chiral experimental configurations (such as the detection of forward-backward asymmetry in photoelectron emission[79,110,112,33,42,66,124,125,126,127,70,71,51,109,89,12,59]) to power all-electric-dipole methods that are highly enantiosensitive even at single-molecule scale, and opening access to time-resolved studies of chiral dynamics[132,10].

Within this vein, recent work has exhibited both photoelectron circular dichroism[127]as well as richly-structured three-dimensional chiral photoelectron momentum distributions, for
single-photon ionization[131,43],
resonantly-enhanced multiphoton ionization[70,33](REMPI), as well as
strong-field ionization[112,18,79,42,92].
Moreover, these methods offer additional promise when driven by synthetic chiral light[8,53,69], a three-dimensional polychromatic combination with chiral sub-cycle dynamics.
These emerging tools, and the investigation of a plethora of new processes enabled by them,
generally encode rich structural and dynamical information into the three-dimensional structure of the photoelectron momentum distribution,
thus creating the need for tools to characterize the chiral features of the latter.

In this section we illustrate how our chiral moments can be applied for this purpose.
To do this, we use the simplest example of photoionization driven by a chiral field: resonantly-enhanced two-photon ionization of atomic hydrogen driven by an elliptically-polarized fundamental, combined with a second harmonic with linear polarization orthogonal to the fundamental’s plane of ellipticity,
a configuration which has been proposed in the infrared range for giant enantiosensitive optical responses through high-order harmonic generation[8];
we show a schematic in Fig.3.
The resulting photoelectron momentum distribution is chiral due to the interference between the two ionization channels.

For this process, the final momentum-representation photoelectron wavefunction can be derived using perturbation theory, yieldingψ​(𝐩)\displaystyle\psi(\mathbf{p})=cp​(p)​𝐄2⋅𝐩+cs​(p)​𝐄1⋅𝐄1+cd​(p)​\trigbraces​Π^2​𝐄1⊗2

∙𝐩⊗2,\displaystyle=c_{\mathrm{p}}(p)\>\mathbf{E}_{2}{\cdot}\mathbf{p}+c_{\mathrm{s}}(p)\>\mathbf{E}_{1}{\cdot}\mathbf{E}_{1}+c_{\mathrm{d}}(p)\>\trigbraces{\hat{\Pi}_{2}}\mathbf{E}_{1}^{\otimes 2}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{p}^{\otimes 2},(27)

for which we defer the details to AppendixD,
where𝐄1\mathbf{E}_{1}and𝐄2\mathbf{E}_{2}are the complex amplitudes of the fundamental and second-harmonic fields,
andcs​(p)c_{\mathrm{s}}(p),cp​(p)c_{\mathrm{p}}(p)andcd​(p)c_{\mathrm{d}}(p)are complex amplitudes describing the s-, p- and d-wave ionization channels.
The photoelectron distribution is then obtained asρ​(𝐩)=|ψ​(𝐩)|2\rho(\mathbf{p})=|\psi(\mathbf{p})|^{2}and its tensorial multipolar moments, which are easy to combine into a chiral moment, for which the natural choice isχ234\chi_{234}.Figure 3:Photoionization of hydrogen by bichromatic chiral light.
(a) Level scheme and field configuration.
(b) Photoelectron momentum distribution|ψ​(𝐩)|2|\psi(\mathbf{p})|^{2}obtained via perturbation theory, as per (27), shown as a contour plot restricted to the sphere with radiusp0p_{0}(in atomic units), together with two-dimensional contour maps of the restriction of the distribution to each hemisphere.
We show|ψ​(𝐩)|2|\psi(\mathbf{p})|^{2}for the case whencs​(p)=0c_{\mathrm{s}}(p)=0,cp​(p)=cd​(p)=1c_{\mathrm{p}}(p)=c_{\mathrm{d}}(p)=1,ϵ=1/2\epsilon=1/2,φ=45°\varphi=$45\text{\,}\mathrm{\SIUnitSymbolDegree}$,E1,0=E2,0=1E_{1,0}=E_{2,0}=1.
(c) Photoelectron momentum distribution obtained by numerical simulation of the TDSE, as described in AppendixE, for the case ofϵ=0.6\epsilon=0.6.
(d) Ellipticity dependence of the different possible contributions toχ234\chi_{234}for the perturbation-theory distribution, as derived in (D.26)
(e) Ellipticity dependence ofχ234\chi_{234}for the numerical TDSE simulation.

For arbitrary polarizations of the fields,𝐄1\mathbf{E}_{1}and𝐄2\mathbf{E}_{2}, it is possible (as we argue in more detail in AppendixD) to obtainχ234\chi_{234}as a scalar polynomial in𝐄1\mathbf{E}_{1}and𝐄2\mathbf{E}_{2}, and their conjugates, of mixed degree, involving terms of ninth and eleventh order.
These polynomials are nonlinear chiral correlation functions of the field, as introduced for synthetic chiral light in[8]; in that notation, they would read ash(9)h^{(9)}andh(11)h^{(11)}.
These relatively high orders are in contrast with the lower-order correlation function (h(5)h^{(5)}) which appears for this field configuration for perturbative nonlinear optical processes[8], with the difference driven by the fact thatρ​(𝐩)\rho(\mathbf{p}), as the square of the wavefunction, is a higher-order object than the wavefunction as used in the case ofh(5)h^{(5)}.

For the specific case of an elliptically-polarized fundamental and an out-of-plane linearly-polarized second harmonic, the chiral moment simplifies to an explicit analytical dependence on the ellipticityϵ\epsilonof the fundamental and the relative phaseφ\varphibetween the two fields,
which we provide as Eq. (D.26) in the Appendices.
The ellipticity dependence is proportional to three terms given byϵ2−1(ϵ2+1)4​ϵ3\frac{\epsilon^{2}-1}{(\epsilon^{2}+1)^{4}}\epsilon^{3},ϵ​(ϵ2−1)(ϵ2+1)2\frac{\epsilon(\epsilon^{2}-1)}{(\epsilon^{2}+1)^{2}},
andϵ​(ϵ2−1)3(ϵ2+1)4\frac{\epsilon(\epsilon^{2}-1)^{3}}{(\epsilon^{2}+1)^{4}},
with relative contributions determined by the relative amplitudes of the two fields as well as their spectra and the details of the atomic structure.
We show in Figure3the shape of these ellipticity dependences.
The angular dependence of the photoelectron momentum distribution,ρ​(𝐩)\rho(\mathbf{p}), is also clearly and graphically chiral;
we show an example in Figure3.

In addition to the perturbation-theory calculation, we simulate this process through the numerical solution of the time-dependent Schrödinger equation (TDSE),
which provides a valuable test case of the application of our open-source software tools[105]for extracting the chiral moments from raw data (whether from simulations or experiment).
We detail our TDSE simulations in AppendixE.

## VDiscussion

As we have seen, for both
concrete distributions with direct links to experiment
as well as for
a variety of model distributions,
our formalism provides intuitive, flexible and robust ways of tackling one of the thornier questions in chirality – assigning a sign to the handedness of a particular distribution.
This comes as a generalization and extension of existing multipole-moment based frameworks[56,98,90,57],
with a much clearer link to the relevant shapes that embody the chirality,
as well as
an understanding of the role of the radial structure of the distribution –
a possibility which has been recognized[56,98,57], but not followed up on.
The ability to incorporate the radial features of the distribution allows
on the one hand,
more robust features, including with respect to noise as well as e.g. the precise location of the spatial origin,
and, more generally,
for a family of chiral measures with a wider scope, and thus less susceptible to the ‘blind spots’ that result from the rubber-glove theorem[136,138,46].Figure 4:(a) Apparent ‘blind spot’ distribution,ρABS​(𝐫)\rho_{\mathrm{ABS}}(\mathbf{r}), as described in AppendixF, plotted as in Fig.3.
(b) Purely octupolar ‘blind spot’ distribution,ρPOBS​(𝐫)\rho_{\mathrm{POBS}}(\mathbf{r}), as described in AppendixG.

That said, it is important to acknowledge that, even for the full generality of our chiral measuresχn1​n2​n32​q1,2​q2,2​q3\chi_{n_{1}n_{2}n_{3}}^{2q_{1},2q_{2},2q_{3}}, some ‘blind spots’ still remain – some of which can be folded into the tensor-cross-product formalism, and some of which cannot.

The simplest example of the former is a distribution of the formρ​(𝐫)=Re⁡[Y33​(𝐫)+ei​φ​Y43​(𝐫)]\rho(\mathbf{r})=\operatorname{Re}[Y_{33}(\mathbf{r})+e^{i\varphi}Y_{43}(\mathbf{r})]constrained to a sphere, as shown in Figure4(a), which we briefly explore in AppendixF.
For structures such as these,
where only two different multipolar moments (𝝁(3)\boldsymbol{\mu}^{(3)}and𝝁(4)\boldsymbol{\mu}^{(4)}) are nonzero,
a chiral measure based directly on triple tensor products will always vanish.888The general tensorial moments can be nonzero, such as e.g.𝐌(5)∝\trigbraces​𝒮^​(𝝁(3)⊗𝕀)\mathbf{M}^{(5)}\propto\trigbraces{\hat{\mathcal{S}}}(\boldsymbol{\mu}^{(3)}\otimes\mathbb{I}), but they do not provide new information in this case.Nevertheless, it is still possible to combine multiple cross products of𝝁(3)\boldsymbol{\mu}^{(3)}and𝝁(4)\boldsymbol{\mu}^{(4)}, of different ranks, into a chirally-sensitive pseudoscalar,
which takes the form of asix-point correlation function ofρ​(𝐫)\rho(\mathbf{r}),
and which we provide in AppendixF.

An example of the latter – a distribution whose chirality cannot (currently) be quantified by our tensor-cross-product formalism – can be built as a chiral superposition of purely octupolar components (Y3​m​(𝐫)Y_{3m}(\mathbf{r})) with different amplitudes for the differentmmvalues,
as shown in Figure4(b),
and which we explore briefly in AppendixG.
For such a distribution, only one tensorial multipolar moment,𝝁(3)\boldsymbol{\mu}^{(3)}, is nonzero,999As above, other general tensorial moments can be nonzero, such as𝐌(5)∝\trigbraces​𝒮^​(𝝁(3)⊗𝕀)\mathbf{M}^{(5)}\propto\trigbraces{\hat{\mathcal{S}}}(\boldsymbol{\mu}^{(3)}\otimes\mathbb{I}), but they do not provide new information.and thus no tensor triple product is directly applicable.
This example thus presents a ‘blind spot’ for our framework (or, at least, an open question), as well as for the existing chirality measures from the literature,
and, as such, appears as a distributional example of what is known in chiral measurements as ‘cryptochirality’[85]: chiral structures whose chirality is difficult to quantify or to relate to experimental observables.

It is also useful to consider expanding the range of our framework to include spatial variation of chirality, as well as its dependence on the relevant length scales.
For those purposes, one readily-applicable approach is to introduce spatial filters (e.g. gaussians) to take local values of the tensor moments, which can then produce a relevant local gaussian-filtered chiral moment.
Even more locally, the behaviour of the distributionρ​(𝐫)\rho(\mathbf{r})at a chosen point𝐫0\mathbf{r}_{0}can be understood purely in terms of its (partial) derivatives, which can then also be combined, as tensors, in the same way as the distribution’s moments.
In component notation, that would read, for example, in the formχ234(local)​(𝐫)\displaystyle\chi_{234}^{\mathrm{(local)}}(\mathbf{r})=ϵi​j​k​(∂i∂lρ)​(∂j∂m∂nρ)​(∂k∂l∂m∂nρ),\displaystyle=\epsilon_{ijk}\left(\partial_{i}\partial_{l}\rho\right)\left(\partial_{j}\partial_{m}\partial_{n}\rho\right)\left(\partial_{k}\partial_{l}\partial_{m}\partial_{n}\rho\right),(28)

using the shorthand∂i\partial_{i}for∂∂xi\frac{\partial}{\partial x_{i}}.101010Alternatively, in invariant notation this takes a form mirroring the chiral moments:χ234(local)​(𝐫)=(∇⊗2ρ×∇⊗3ρ)(4)

∙∇⊗4ρ\chi_{234}^{\mathrm{(local)}}(\mathbf{r})=\left(\nabla^{\otimes 2}\rho\times\nabla^{\otimes 3}\rho\right)^{(4)}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\nabla^{\otimes 4}\rho.

On a more general perspective, not all relevant distributions need to be of a chiral shape in their own right, and often the chirality of an experimental result comes from the relationship between the observed distribution and the surrounding experiment (for example, forwards-backwards asymmetry with respect to a preferred axis).
This is particularly important for the chiral study of light-matter interactions (such as photoelectron circular dichroism[110,126,125,127,89,70,71,109]),
where the driving light acts as a chiral reagent, providing an important spatial reference (e.g. a preferred axis) for the final observable.
For these sorts of cases, our formalism provides a natural framework, independent of the frame of reference, for incorporating these spatial features.
Thus, for example, the usual chiroptical observables will often have the form of tensor triple products, where one or more of the tensor factors is a light- or experiment-derived quantity,
such as
the propagation direction light,𝐤\mathbf{k},
a polarization tensor of either quadratic (𝐏=⟨𝐄​(t)⊗2⟩\mathbf{P}=\left\langle\mathbf{E}(t)^{\otimes 2}\right\rangle) or higher order (e.g.𝐓(3)=⟨𝐄​(t)⊗3⟩\mathbf{T}^{(3)}=\left\langle\mathbf{E}(t)^{\otimes 3}\right\rangle[107]),
or the spatial distribution of other chemical fragments obtained in a dissociative process[104,14,135].

Our formalism also extends naturally
from structural chirality, which lives in space only,
to dynamical chirality, which also includes the temporal dependence of the distribution.
For these cases, one can simply replace one or more of the tensorial-moment factors in (6) with a temporal derivative of such moments;
such a development would mirror the recent introduction of dynamical chirality in light[8,94,93].
A similar development might be to extend our formalism to deal with vector-valued[38,93,123,115](or even tensor-valued[4,58]) chiral distributions, in contrast to the scalar-valued ones we have considered so far.

A desirable broader application area for our formalism is to describe chiral optical responses in their full generality,
from circular dichroism and optical rotation[34]to chiral Raman[100]and Rayleigh[32,80]scattering and all the way up to extreme nonlinear optical processes[8,68,79,78,10,9,97,95,96,94].
Since chiral optical processes often involve tensor quantities of mixed symmetry[80,32], this would require generalizing our tensor triple product (5)
(as well as the tensor cross product (A.1))
to allow for mixed-symmetry tensor factors,
using the connection to the Wigner3​j3jsymbols (as explored in AppendixC.4) as a clear guide.

Already in its current generality, however, our work provides, as we have seen, a robust, flexible, intuitive, highly geometrical, physically-driven framework for understanding and quantifying the chirality of a wide variety of distributions.
The analytical toolset is matched by a corresponding open-source software package[105], which can deal with both symbolic computation as well as numerical simulation and experimental data.

## Acknowledgements

We are deeply grateful to the organizers and participants of the CUPUSL23 meeting in MPI-PKS, Dresden, where this work had its genesis, and particularly to Misha Ivanov and Olga Smirnova for inspiration and encouragement and to David Ayuso for stimulating discussions.

E.P. acknowledges Royal Society funding under URF\R1\211390.
N.M. acknowledges funding by the UK Research and Innovation (UKRI) under the UK government’s Horizon Europe funding guarantee [Grant No. EP/Z001390/1].
A.O. acknowledges funding from the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) 543760364.
A.L. acknowledges funding from the European Union under ERC, ULISSES, 101054696.
M.K. acknowledges Royal Society funding under URF\R1\231460.

E.P. dedicates this work to the memory of Prof. Eugenio Ley Koo.

## Appendix ADefinitions and properties

The central problem in constructing our chiral measures can be expressed as follows:
given three symmetric tensors,𝐀(n1)\mathbf{A}^{(n_{1})},𝐁(n2)\mathbf{B}^{(n_{2})}and𝐂(n3)\mathbf{C}^{(n_{3})},
with componentsAi1​⋯​in1A_{i_{1}\cdots i_{n_{1}}},Bi1​⋯​in2B_{i_{1}\cdots i_{n_{2}}}andCi1​⋯​in3C_{i_{1}\cdots i_{n_{3}}},
we would like to form a single pseudoscalar —
that is, a single scalar number, independent of the frame of reference,
and which changes sign under spatial inversion and reflections.

There is one clear way to do this, achievable via tensor contractions between the three tensor factors together with one added Levi-Civita tensor factor.
This is the tensor triple product, defined in Eq. (5), which we recall as(𝐀(n1)×𝐁(n2))(n3)

∙𝐂(n3)\displaystyle\left(\mathbf{A}^{(n_{1})}\ignorespaces\times\ignorespaces\mathbf{B}^{(n_{2})}\right)^{(n_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{C}^{(n_{3})}=ϵi1​i2​i3​Ai1​𝐣𝐤​Bi2​𝐣𝐥​Ci3​𝐤𝐥.\displaystyle=\epsilon_{i_{1}i_{2}i_{3}}A_{i_{1}\mathbf{j}\mathbf{k}}B_{i_{2}\mathbf{j}\mathbf{l}}C_{i_{3}\mathbf{k}\mathbf{l}}.

The structure is simple: the Levi-Civita factor is contracted, via each of its three indices, with one index each from𝐀(n1)\mathbf{A}^{(n_{1})},𝐁(n2)\mathbf{B}^{(n_{2})}and𝐂(n3)\mathbf{C}^{(n_{3})},
and these are then contracted with each other.
These contractions are taken through the repeated multi-indices𝐣=(j1​⋯​jm)\mathbf{j}=(j_{1}\cdots j_{m}),𝐤=(k1​⋯​kn)\mathbf{k}=(k_{1}\cdots k_{n})and𝐥=(l1​⋯​lp)\mathbf{l}=(l_{1}\cdots l_{p})that appear shared between the three pairs of factors.
Finally, the lengthsmm,nnandppof the shared multi-indices can be found by requiring that no indices remain free, which a simple calculation shows to requirem=12​(n1+n2−n3−1)m=\frac{1}{2}(n_{1}+n_{2}-n_{3}-1),n=12​(n1+n3−n2−1)n=\frac{1}{2}(n_{1}+n_{3}-n_{2}-1)andp=12​(n2+n3−n1−1)p=\frac{1}{2}(n_{2}+n_{3}-n_{1}-1).

As a quick note, the form (5) arises from the theory of isotropic tensors[3,62]as the single clear candidate for our pseudoscalar.
While other combinations are possible, they would involve internal contractions (i.e., tensor traces) between indices belonging to the same tensor factor;
as such, they would involve factors of, e.g.,Tr⁡(𝐀(n1))\Tr(\mathbf{A}^{(n_{1})}),
and can therefore be taken separately.
More concretely, the form (5) is the unique pseudoscalar with maximal connectivity between the indices of the three tensor factors.

As a quick note, our definition (5) for the tensor triple product relies on the fact that the three tensor factors are fully symmetric,
which removes any concern about which indices are contracted together.
For our purposes, this is justified, as the moment tensors𝐌(n)\mathbf{M}^{(n)}and their multipolar counterparts𝝁(ℓ)\boldsymbol{\mu}^{(\ell)}are all symmetric.
Nevertheless, the extension of this definition to tensors of mixed symmetry is an interesting (and, thus far, open) question, with clear applications to the pseudoscalars that appear in general chiroptical experiments.

Once the pseudoscalar (5) has been defined, it provides us with a clear and unique definition of the tensor cross product.
In particular, we can see that Eq. (5) defines a linear mapping𝐂(n3)↦ϵi1​i2​i3​Ai1​𝐣𝐤​Bi2​𝐣𝐥​Ci3​𝐤𝐥\mathbf{C}^{(n_{3})}\mapsto\epsilon_{i_{1}i_{2}i_{3}}A_{i_{1}\mathbf{j}\mathbf{k}}B_{i_{2}\mathbf{j}\mathbf{l}}C_{i_{3}\mathbf{k}\mathbf{l}},
which takes a symmetric complex-valued tensor and returns a scalar.
This mapping can always be interpreted as the full contraction with a separate fully-symmetric tensor, and this is what we define to be the tensor cross product:(𝐀(n1)×𝐁(n2))i3​𝐤𝐥(n3)\displaystyle\left(\mathbf{A}^{(n_{1})}\ignorespaces\times\ignorespaces\mathbf{B}^{(n_{2})}\right)^{(n_{3})}_{i_{3}\mathbf{k}\mathbf{l}}=\trigbraces​𝒮^i3​𝐤𝐥​(ϵi1​i2​i3​Ai1​𝐣𝐤​Bi2​𝐣𝐥)\displaystyle=\trigbraces{\hat{\mathcal{S}}}_{i_{3}\mathbf{k}\mathbf{l}}\bigg(\epsilon_{i_{1}i_{2}i_{3}}A_{i_{1}\mathbf{j}\mathbf{k}}B_{i_{2}\mathbf{j}\mathbf{l}}\bigg)(A.1)

where\trigbraces​𝒮^i3​𝐤𝐥\trigbraces{\hat{\mathcal{S}}}_{i_{3}\mathbf{k}\mathbf{l}}denotes full symmetrisation over the remaining free indices,i3i_{3},𝐤\mathbf{k}and𝐥\mathbf{l}.

One clear route for getting more solid intuition into the meaning, behaviour, and handling of the tensor triple product, and the tensor cross product,
is to consider the scenario when each of the factors is a simple tensor power of a chosen vector,
i.e. when𝐀(n1)=𝐚⊗n1\mathbf{A}^{(n_{1})}=\mathbf{a}^{\otimes n_{1}},𝐁(n2)=𝐛⊗n2\mathbf{B}^{(n_{2})}=\mathbf{b}^{\otimes n_{2}}and𝐂(n3)=𝐜⊗n3\mathbf{C}^{(n_{3})}=\mathbf{c}^{\otimes n_{3}},
(in component notationAi1​⋯​in1(n1)=ai1​⋯​ain1A^{(n_{1})}_{i_{1}\cdots i_{n_{1}}}=a_{i_{1}}\cdots a_{i_{n_{1}}}, and similarly for𝐁(n2)\mathbf{B}^{(n_{2})}and𝐂(n3)\mathbf{C}^{(n_{3})}).
For this case, the Levi-Civita contraction turns into a simple vector triple product,((𝐚×𝐛)⋅𝐜)\left(\left(\mathbf{a}\times\mathbf{b}\right)\cdot\mathbf{c}\right),
while the pairwise tensor contractions become simple vector dot products,
resulting in a clean expression:(𝐚⊗n1×\displaystyle\Big(\mathbf{a}^{\otimes n_{1}}\ignorespaces\times\ignorespaces𝐛⊗n2)(n3)

∙𝐜⊗n3=\displaystyle\mathbf{b}^{\otimes n_{2}}\Big)^{(n_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{c}^{\otimes n_{3}}=(A.2)((𝐚×𝐛)⋅𝐜)​(𝐚⋅𝐛)m​(𝐛⋅𝐜)n​(𝐜⋅𝐚)p.\displaystyle\left(\left(\mathbf{a}\times\mathbf{b}\right)\cdot\mathbf{c}\right)\left(\mathbf{a}\cdot\mathbf{b}\right)^{m}\left(\mathbf{b}\cdot\mathbf{c}\right)^{n}\left(\mathbf{c}\cdot\mathbf{a}\right)^{p}.

Similarly, the tensor cross product for this case is(𝐚⊗n1×𝐛⊗n2)(n3)\displaystyle\left(\mathbf{a}^{\otimes n_{1}}\ignorespaces\times\ignorespaces\mathbf{b}^{\otimes n_{2}}\right)^{(n_{3})}=\trigbraces​𝒮^​((𝐚×𝐛)​(𝐚⋅𝐛)m⊗𝐛⊗n⊗𝐚⊗p),\displaystyle=\trigbraces{\hat{\mathcal{S}}}(\left(\mathbf{a}\times\mathbf{b}\right)\left(\mathbf{a}\cdot\mathbf{b}\right)^{m}\otimes\mathbf{b}^{\otimes n}\otimes\mathbf{a}^{\otimes p}),(A.3)

i.e., a symmetrized tensor product between the cross product𝐚×𝐛\mathbf{a}\times\mathbf{b}and the tensor powers𝐛⊗n\mathbf{b}^{\otimes n}and𝐚⊗p\mathbf{a}^{\otimes p}, all multiplied by a power of their dot product,(𝐚⋅𝐛)m\left(\mathbf{a}\cdot\mathbf{b}\right)^{m}.

For simple cases, it is often fairly feasible to calculate the tensor cross product directly, at least when the tensor ranks involved are low.
For higher ranks, and for more complex cases as well as for numerical data, however, this is impractical.
For those settings, we have implemented the tensor cross product in the Wolfram Language as the open-source software packageChimeraavailable as Ref.[105].

To make this section complete, we should point out that this formalism also admits a clean extension for the case of even parity (i.e. when the tensor factors need to be combined into a single scalar, rather than a pseudoscalar), in which case we write(𝐀(n1)×𝐁(n2))(n3)

∙𝐂(n3)\displaystyle\left(\mathbf{A}^{(n_{1})}\ignorespaces\times\ignorespaces\mathbf{B}^{(n_{2})}\right)^{(n_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{C}^{(n_{3})}=A𝐣𝐤​B𝐣𝐥​C𝐤𝐥,\displaystyle=A_{\mathbf{j}\mathbf{k}}B_{\mathbf{j}\mathbf{l}}C_{\mathbf{k}\mathbf{l}},(A.4)

omitting the Levi-Civita factor.
For this case, the multi-indices are still denoted𝐣=(j1​⋯​jm)\mathbf{j}=(j_{1}\cdots j_{m}),𝐤=(k1​⋯​kn)\mathbf{k}=(k_{1}\cdots k_{n})and𝐥=(l1​⋯​lp)\mathbf{l}=(l_{1}\cdots l_{p}),
though their lengths now take the valuesm=12​(n1+n2−n3)m=\frac{1}{2}(n_{1}+n_{2}-n_{3}),n=12​(n1+n3−n2)n=\frac{1}{2}(n_{1}+n_{3}-n_{2})andp=12​(n2+n3−n1)p=\frac{1}{2}(n_{2}+n_{3}-n_{1}).
We will use this even-parity product to combine three pseudotensors in AppendixF, as a route to dealing with the apparent ‘blind spot’ mentioned in the Discussion.

## Appendix BExplicit forms for the traceless kernels

As mentioned in the main text, our chiral momentsχn1​n2​n3=(𝐌(n1)×𝐌(n2))(n3)

∙𝐌(n3)\chi_{n_{1}n_{2}n_{3}}=\left(\mathbf{M}^{(n_{1})}\ignorespaces\times\ignorespaces\mathbf{M}^{(n_{2})}\right)^{(n_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{M}^{(n_{3})}can be re-expressed as a triple integral, given by equation (7), which we recall asχn1​n2​n3\displaystyle\chi_{n_{1}n_{2}n_{3}}=∭d​𝐫1​d​𝐫2​d​𝐫3​ρ​(𝐫1)​ρ​(𝐫2)​ρ​(𝐫3)\displaystyle=\iiint\textrm{d}\mathbf{r}_{1}\textrm{d}\mathbf{r}_{2}\textrm{d}\mathbf{r}_{3}\rho(\mathbf{r}_{1})\rho(\mathbf{r}_{2})\rho(\mathbf{r}_{3})(𝐫1⊗n1×𝐫2⊗n2)(n3)

∙𝐫3⊗n3\displaystyle\qquad\qquad\quad\left(\mathbf{r}_{1}^{\otimes n_{1}}\ignorespaces\times\ignorespaces\mathbf{r}_{2}^{\otimes n_{2}}\right)^{(n_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{r}_{3}^{\otimes n_{3}}=∭d​𝐫1​d​𝐫2​d​𝐫3​ρ​(𝐫1)​ρ​(𝐫2)​ρ​(𝐫3)\displaystyle=\iiint\textrm{d}\mathbf{r}_{1}\textrm{d}\mathbf{r}_{2}\textrm{d}\mathbf{r}_{3}\rho(\mathbf{r}_{1})\rho(\mathbf{r}_{2})\rho(\mathbf{r}_{3})[(𝐫1×𝐫2)⋅𝐫3]​(𝐫1⋅𝐫2)m​(𝐫1⋅𝐫3)n​(𝐫2⋅𝐫3)p.\displaystyle\qquad\quad\left[(\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}\right](\mathbf{r}_{1}\cdot\mathbf{r}_{2})^{m}(\mathbf{r}_{1}\cdot\mathbf{r}_{3})^{n}(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{p}.

Similarly, we defined the traceless chiral moments ashℓ1​ℓ2​ℓ3=(𝝁(ℓ1)×𝝁(ℓ2))(ℓ3)

∙𝝁(ℓ3)h_{\ell_{1}\ell_{2}\ell_{3}}=\left(\boldsymbol{\mu}^{(\ell_{1})}\ignorespaces\times\ignorespaces\boldsymbol{\mu}^{(\ell_{2})}\right)^{(\ell_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\boldsymbol{\mu}^{(\ell_{3})},
in terms of the (traceless) tensorial multipolar moments𝝁(ℓ)=Π^ℓ​𝐌(ℓ)\boldsymbol{\mu}^{(\ell)}=\hat{\Pi}_{\ell}\mathbf{M}^{(\ell)},
and, for these traceless chiral moments, a similar argument applies:
the three integrals in the𝝁(ℓ)\boldsymbol{\mu}^{(\ell)}can be expanded out and brought together, giving an expression for the traceless chiral moment of the formhℓ1​ℓ2​ℓ3\displaystyle h_{\ell_{1}\ell_{2}\ell_{3}}=∭d​𝐫1​d​𝐫2​d​𝐫3​ρ​(𝐫1)​ρ​(𝐫2)​ρ​(𝐫3)\displaystyle=\iiint\textrm{d}\mathbf{r}_{1}\textrm{d}\mathbf{r}_{2}\textrm{d}\mathbf{r}_{3}\>\rho(\mathbf{r}_{1})\rho(\mathbf{r}_{2})\rho(\mathbf{r}_{3})(B.1)(Π^ℓ1​𝐫1⊗ℓ1×Π^ℓ2​𝐫2⊗ℓ2)(ℓ3)

∙Π^ℓ3​𝐫3⊗ℓ3\displaystyle\qquad\qquad\quad\left(\hat{\Pi}_{\ell_{1}}\mathbf{r}_{1}^{\otimes\ell_{1}}\ignorespaces\times\ignorespaces\hat{\Pi}_{\ell_{2}}\mathbf{r}_{2}^{\otimes\ell_{2}}\right)^{(\ell_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\hat{\Pi}_{\ell_{3}}\mathbf{r}_{3}^{\otimes\ell_{3}}=∭d​𝐫1​d​𝐫2​d​𝐫3​ρ​(𝐫1)​ρ​(𝐫2)​ρ​(𝐫3)​Hℓ1​ℓ2​ℓ3​(𝐫1,𝐫2,𝐫3).\displaystyle\!\!\!\!\!\!\!\!=\iiint\textrm{d}\mathbf{r}_{1}\textrm{d}\mathbf{r}_{2}\textrm{d}\mathbf{r}_{3}\>\rho(\mathbf{r}_{1})\rho(\mathbf{r}_{2})\rho(\mathbf{r}_{3})H_{\ell_{1}\ell_{2}\ell_{3}}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3}).

As for the ‘unabridged’ chiral moments, this takes the form of a three-point correlation function, with three copies of the densityρ​(𝐫)\rho(\mathbf{r})multiplied against a correlated kernel,Hℓ1​ℓ2​ℓ3​(𝐫1,𝐫2,𝐫3)\displaystyle H_{\ell_{1}\ell_{2}\ell_{3}}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=(Π^ℓ1​𝐫1⊗ℓ1×Π^ℓ2​𝐫2⊗ℓ2)(ℓ3)

∙Π^ℓ3​𝐫3⊗ℓ3,\displaystyle=\left(\hat{\Pi}_{\ell_{1}}\mathbf{r}_{1}^{\otimes\ell_{1}}\ignorespaces\times\ignorespaces\hat{\Pi}_{\ell_{2}}\mathbf{r}_{2}^{\otimes\ell_{2}}\right)^{(\ell_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\hat{\Pi}_{\ell_{3}}\mathbf{r}_{3}^{\otimes\ell_{3}},(B.2)

which is again a (pseudo)scalar homogeneous polynomial in the Cartesian components of𝐫1\mathbf{r}_{1},𝐫2\mathbf{r}_{2}and𝐫3\mathbf{r}_{3}, of respective ordersℓ1\ell_{1},ℓ2\ell_{2}andℓ3\ell_{3},
though now it is fully traceless, in the sense that
it is a harmonic function of each of its variables, i.e.,∇𝐫i2Hℓ1​ℓ2​ℓ3​(𝐫1,𝐫2,𝐫3)=0,\displaystyle\nabla^{2}_{\mathbf{r}_{i}}H_{\ell_{1}\ell_{2}\ell_{3}}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=0,(B.3)

fori=1,2,3i=1,2,3.111111This tracelessness also manifests as the fact that
a spherical integral ofHℓ1​ℓ2​ℓ3​(𝐫1,𝐫2,𝐫3)H_{\ell_{1}\ell_{2}\ell_{3}}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})against any spherical or solid harmonicSℓ,m​(𝐫1)S_{\ell,m}(\mathbf{r}_{1})of degreeℓ<ℓ1\ell<\ell_{1}will vanish, i.e.∫r1=1Hℓ1​ℓ2​ℓ3​(𝐫1,𝐫2,𝐫3)​Sℓ,m​(𝐫1)​d​Ω1=0\int_{r_{1}=1}H_{\ell_{1}\ell_{2}\ell_{3}}(\mathbf{r}_{1},\allowbreak{}\mathbf{r}_{2},\mathbf{r}_{3})S_{\ell,m}(\mathbf{r}_{1})\textrm{d}\Omega_{1}=0,
and similarly for integrals over𝐫2\mathbf{r}_{2}and𝐫3\mathbf{r}_{3}.

These polynomials must be constructed out of dot products and norms of the𝐫i\mathbf{r}_{i}, and, as such, they are relatively simple to construct – and, once constructed, their explicit forms are simple to verify via computer algebra.
These explicit forms read, for the first few cases, as follows:H111​(𝐫1,𝐫2,𝐫3)\displaystyle H_{111}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=(𝐫1×𝐫2)⋅𝐫3,\displaystyle=(\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3},(B.4a)H122​(𝐫1,𝐫2,𝐫3)\displaystyle H_{122}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=((𝐫1×𝐫2)⋅𝐫3)​(𝐫2⋅𝐫3),\displaystyle=\big((\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}\big)(\mathbf{r}_{2}\cdot\mathbf{r}_{3})\vphantom{\bigg]},(B.4b)H223​(𝐫1,𝐫2,𝐫3)\displaystyle H_{223}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=((𝐫1×𝐫2)⋅𝐫3)​[(𝐫1⋅𝐫3)​(𝐫2⋅𝐫3)−15​(𝐫1⋅𝐫2)​r32],\displaystyle=\big((\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}\big)\left[(\mathbf{r}_{1}\cdot\mathbf{r}_{3})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})-\tfrac{1}{5}(\mathbf{r}_{1}\cdot\mathbf{r}_{2})r_{3}^{2}\right],(B.4c)H133​(𝐫1,𝐫2,𝐫3)\displaystyle H_{133}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=((𝐫1×𝐫2)⋅𝐫3)​[(𝐫2⋅𝐫3)2−15​r22​r32],\displaystyle=\big((\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}\big)\left[(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{2}-\tfrac{1}{5}r_{2}^{2}r_{3}^{2}\right],(B.4d)H144​(𝐫1,𝐫2,𝐫3)\displaystyle H_{144}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=((𝐫1×𝐫2)⋅𝐫3)​(𝐫2⋅𝐫3)​[(𝐫2⋅𝐫3)2−37​r22​r32],\displaystyle=\big((\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}\big)(\mathbf{r}_{2}\cdot\mathbf{r}_{3})\left[(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{2}-\tfrac{3}{7}r_{2}^{2}r_{3}^{2}\right],(B.4e)H234​(𝐫1,𝐫2,𝐫3)\displaystyle H_{234}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=((𝐫1×𝐫2)⋅𝐫3)​[(𝐫1⋅𝐫3)​(𝐫2⋅𝐫3)2−27​(𝐫1⋅𝐫2)​(𝐫2⋅𝐫3)​r32−17​(𝐫1⋅𝐫3)​r22​r32],\displaystyle=\big((\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}\big)\left[(\mathbf{r}_{1}\cdot\mathbf{r}_{3})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{2}-\tfrac{2}{7}(\mathbf{r}_{1}\cdot\mathbf{r}_{2})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})r_{3}^{2}-\tfrac{1}{7}(\mathbf{r}_{1}\cdot\mathbf{r}_{3})r_{2}^{2}r_{3}^{2}\right],(B.4f)H333​(𝐫1,𝐫2,𝐫3)\displaystyle H_{333}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=((𝐫1×𝐫2)⋅𝐫3)​[(𝐫1⋅𝐫2)​(𝐫2⋅𝐫3)​(𝐫3⋅𝐫1)−15​(r12​(𝐫2⋅𝐫3)2+r22​(𝐫3⋅𝐫1)2+r32​(𝐫1⋅𝐫2)2)+225​r12​r22​r32].\displaystyle=\big((\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}\big)\left[(\mathbf{r}_{1}\cdot\mathbf{r}_{2})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})(\mathbf{r}_{3}\cdot\mathbf{r}_{1})-\tfrac{1}{5}\left(r_{1}^{2}(\mathbf{r}_{2}{\cdot}\mathbf{r}_{3})^{2}{+}r_{2}^{2}(\mathbf{r}_{3}{\cdot}\mathbf{r}_{1})^{2}{+}r_{3}^{2}(\mathbf{r}_{1}{\cdot}\mathbf{r}_{2})^{2}\right)+\tfrac{2}{25}r_{1}^{2}r_{2}^{2}r_{3}^{2}\right].(B.4g)

The specific coefficients involved (e.g.15\tfrac{1}{5},37\tfrac{3}{7},17\tfrac{1}{7}) are ultimately determined by the specific multipolar projectors\trigbraces​Π^ℓ\trigbraces{\hat{\Pi}_{\ell}}involved
(and, specifically, by the coefficientscn,ℓc_{n,\ell}andbℓ,mb_{\ell,m}we will develop in more detail in sectionC.2below).
The normalization is governed by requiring the leading term (i.e. the fully-connected contraction, leading to the combination that appears in (7)) to have unit coefficient.

In more formal terms, the polynomialsHℓ1​ℓ2​ℓ3H_{\ell_{1}\ell_{2}\ell_{3}}are known as the scalar ‘tripolar’ spherical harmonics[133, §5.16.2],
and they have seen some use in both atomic, molecular and optical physics[73,74,75,13,36,122,61,81,11,72](therein sometimes termed ‘triple product of degree zero’[40]),
as well as in nuclear spectroscopy[15]and cosmology[129,20,65,121,120,23](where they are sometimes abbreviated as ‘TripoSH’[121,120,23]),
though their detailed properties do not seem to have received much attention in the literature[15,129].
These polynomials also generalize to ‘polypolar’[121]or ‘nn-polar’[72]harmonics, which can accommodate arbitrary numbers of positions
(and, thus, correspond tonn-point correlation functions ofρ​(𝐫)\rho(\mathbf{r})[25]),
thereby embodying the higher-order combination required to deal with the apparent ‘blind spot’ as described in sectionFbelow.

Finally, for completeness, we provide here the corresponding even-parity polynomials.H112​(𝐫1,𝐫2,𝐫3)\displaystyle H_{112}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=(𝐫1⋅𝐫3)​(𝐫2⋅𝐫3)−13​(𝐫1⋅𝐫2)​r32,\displaystyle=(\mathbf{r}_{1}\cdot\mathbf{r}_{3})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})-\tfrac{1}{3}(\mathbf{r}_{1}\cdot\mathbf{r}_{2})r_{3}^{2},(B.5a)H123​(𝐫1,𝐫2,𝐫3)\displaystyle H_{123}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=(𝐫1⋅𝐫3)​(𝐫2⋅𝐫3)2−25​(𝐫1⋅𝐫2)​(𝐫2⋅𝐫3)​r32−15​(𝐫1⋅𝐫3)​r22​r32,\displaystyle=(\mathbf{r}_{1}\cdot\mathbf{r}_{3})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{2}-\tfrac{2}{5}(\mathbf{r}_{1}\cdot\mathbf{r}_{2})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})r_{3}^{2}-\tfrac{1}{5}(\mathbf{r}_{1}\cdot\mathbf{r}_{3})r_{2}^{2}r_{3}^{2},(B.5b)H222​(𝐫1,𝐫2,𝐫3)\displaystyle H_{222}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=13​(𝐫1⋅𝐫3)​(𝐫2⋅𝐫3)​(𝐫3⋅𝐫1)−19​r12​r22​r32+13​((𝐫1×𝐫2)⋅𝐫3)2,\displaystyle=\tfrac{1}{3}(\mathbf{r}_{1}\cdot\mathbf{r}_{3})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})(\mathbf{r}_{3}\cdot\mathbf{r}_{1})-\tfrac{1}{9}r_{1}^{2}r_{2}^{2}r_{3}^{2}+\tfrac{1}{3}\left((\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}\right)^{2},(B.5c)H134​(𝐫1,𝐫2,𝐫3)\displaystyle H_{134}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=(𝐫1⋅𝐫3)​(𝐫2⋅𝐫3)3−37​(𝐫1⋅𝐫3)​(𝐫2⋅𝐫3)​r22​r32−37​(𝐫1⋅𝐫2)​(𝐫2⋅𝐫3)2​r32+335​(𝐫1⋅𝐫2)​r22​r34,\displaystyle=(\mathbf{r}_{1}\cdot\mathbf{r}_{3})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{3}-\tfrac{3}{7}(\mathbf{r}_{1}\cdot\mathbf{r}_{3})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})r_{2}^{2}r_{3}^{2}-\tfrac{3}{7}(\mathbf{r}_{1}\cdot\mathbf{r}_{2})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{2}r_{3}^{2}+\tfrac{3}{35}(\mathbf{r}_{1}\cdot\mathbf{r}_{2})r_{2}^{2}r_{3}^{4},(B.5d)H224​(𝐫1,𝐫2,𝐫3)\displaystyle H_{224}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=(𝐫1⋅𝐫3)2​(𝐫2⋅𝐫3)2−47​(𝐫1⋅𝐫2)​(𝐫2⋅𝐫3)​(𝐫3⋅𝐫1)​r32+235​(𝐫1⋅𝐫2)2​r34\displaystyle=(\mathbf{r}_{1}\cdot\mathbf{r}_{3})^{2}(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{2}-\tfrac{4}{7}(\mathbf{r}_{1}\cdot\mathbf{r}_{2})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})(\mathbf{r}_{3}\cdot\mathbf{r}_{1})r_{3}^{2}+\tfrac{2}{35}(\mathbf{r}_{1}\cdot\mathbf{r}_{2})^{2}r_{3}^{4}−17​(𝐫1⋅𝐫3)2​r22​r32−17​(𝐫2⋅𝐫3)2​r12​r32+135​r12​r22​r34,\displaystyle\qquad\qquad-\tfrac{1}{7}(\mathbf{r}_{1}\cdot\mathbf{r}_{3})^{2}r_{2}^{2}r_{3}^{2}-\tfrac{1}{7}(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{2}r_{1}^{2}r_{3}^{2}+\tfrac{1}{35}r_{1}^{2}r_{2}^{2}r_{3}^{4},(B.5e)H233​(𝐫1,𝐫2,𝐫3)\displaystyle H_{233}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})=(𝐫1⋅𝐫2)​(𝐫1⋅𝐫3)​(𝐫2⋅𝐫3)2−25​(𝐫2⋅𝐫3)​((𝐫1⋅𝐫3)2​r22+(𝐫1⋅𝐫2)2​r32)+125​(𝐫1⋅𝐫2)​(𝐫1⋅𝐫3)​r22​r32\displaystyle=(\mathbf{r}_{1}\cdot\mathbf{r}_{2})(\mathbf{r}_{1}\cdot\mathbf{r}_{3})(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{2}-\tfrac{2}{5}(\mathbf{r}_{2}\cdot\mathbf{r}_{3})\left((\mathbf{r}_{1}\cdot\mathbf{r}_{3})^{2}r_{2}^{2}+(\mathbf{r}_{1}\cdot\mathbf{r}_{2})^{2}r_{3}^{2}\right)+\tfrac{1}{25}(\mathbf{r}_{1}\cdot\mathbf{r}_{2})(\mathbf{r}_{1}\cdot\mathbf{r}_{3})r_{2}^{2}r_{3}^{2}−13​(𝐫2⋅𝐫3)3​r12+725​(𝐫2⋅𝐫3)​r12​r22​r32.\displaystyle\qquad\qquad-\tfrac{1}{3}(\mathbf{r}_{2}\cdot\mathbf{r}_{3})^{3}r_{1}^{2}+\tfrac{7}{25}(\mathbf{r}_{2}\cdot\mathbf{r}_{3})r_{1}^{2}r_{2}^{2}r_{3}^{2}.(B.5f)

Here it is important to note that the scalar triple product,(𝐫1×𝐫2)⋅𝐫3(\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}, makes occasional appearances, such as inH222​(𝐫1,𝐫2,𝐫3)H_{222}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3}).
In the achiral tripolar harmonics, the scalar triple product always appears squared, in which case it can always be written as a function of the pairwise dot products,𝐫i⋅𝐫j\mathbf{r}_{i}\cdot\mathbf{r}_{j}, as the square is equal to the determinant of the Gram matrix:((𝐫1×𝐫2)⋅𝐫3)2=det[(𝐫i⋅𝐫j)i​j].\left((\mathbf{r}_{1}\times\mathbf{r}_{2})\cdot\mathbf{r}_{3}\right)^{2}=\det\mathopen{}\left[\left(\mathbf{r}_{i}\cdot\mathbf{r}_{j}\right)_{ij}\right].(B.6)

## Appendix CTensor theory

Our definition of the tensorial multipolar moment𝝁(ℓ)=Π^ℓ​𝐌(ℓ)\boldsymbol{\mu}^{(\ell)}=\hat{\Pi}_{\ell}\mathbf{M}^{(\ell)}from the ‘unabridged’ or ‘implicit’ tensorial moment𝐌(ℓ)\mathbf{M}^{(\ell)}hinges, crucially, on the trace-removal projectorΠ^ℓ\hat{\Pi}_{\ell}(also known as the ‘de-tracer’ operator[31,5,7,119]).
This Appendix summarizes its core properties, presents a general definition, and provides some useful properties.

## C.1The trace-removal projector: intuition

The core distinction between the ‘unabridged’ and the traceless moments is perhaps most familiar in the case of rankn=2n=2, where the tensorial moment components read simplyMi​j(2)=∫xi​xj​ρ​(𝐫)​d​𝐫,\displaystyle M^{(2)}_{ij}=\int x_{i}x_{j}\rho(\mathbf{r})\textrm{d}\mathbf{r},\qquad\qquad\quad(C.1)

whereas it is typically desirable to define the multipolar tensor moments having componentsμi​j(2)=∫(xi​xj−13​r2​δi​j)​ρ​(𝐫)​d​𝐫,\displaystyle\mu^{(2)}_{ij}=\int\left(x_{i}x_{j}-\frac{1}{3}r^{2}\delta_{ij}\right)\rho(\mathbf{r})\textrm{d}\mathbf{r},(C.2)

as the component-notation reading of𝝁(2)=\trigbraces​Π^2​𝐌(2)\boldsymbol{\mu}^{(2)}=\trigbraces{\hat{\Pi}_{2}}\mathbf{M}^{(2)}.
This is done because it allows us to separate the ‘shape’ information (contained inμi​j(2)\mu^{(2)}_{ij}) from the rotationally-invariant traceμ(0,2)=Tr(𝐌(2))=Mi​i(2)=∫r2ρ(𝐫)d𝐫\mu^{(0,2)}=\Tr\mathopen{}\left(\mathbf{M}^{(2)}\right)=M^{(2)}_{ii}=\int r^{2}\rho(\mathbf{r})\textrm{d}\mathbf{r},
which describes the width of the distribution.
Thus, we decompose the tensorial moment asMi​j(2)=μi​j(2)+13​μ(0,2)​δi​j,\displaystyle M^{(2)}_{ij}=\mu^{(2)}_{ij}+\tfrac{1}{3}\mu^{(0,2)}\delta_{ij},(C.3)

and (since the Kronecker deltaδi​j\delta_{ij}is invariant under rotations) each of those two terms forms an isolated subspace under arbitrary rotations
(or, in the language of group representation theory[54], an irreducible representation[63,144,76]).

For higher ranks, a similar separation holds.
Thus, for example, at rankn=3n=3, we decompose the full tensor moment asMi​j​k(3)=μi​j​k(3)+35​\trigbraces​𝒮^i​j​k​μi(1,2)​δj​k\displaystyle M^{(3)}_{ijk}=\mu^{(3)}_{ijk}+\tfrac{3}{5}\trigbraces{\hat{\mathcal{S}}}_{ijk}\mu^{(1,2)}_{i}\delta_{jk}(C.4)

to separate the octupole tensor momentμi​j​k(3)\mu^{(3)}_{ijk}fromμi(1,2)=∫xi​r2​ρ​(𝐫)​d​𝐫\mu^{(1,2)}_{i}=\int x_{i}r^{2}\rho(\mathbf{r})\textrm{d}\mathbf{r},
the dipole moment of the distributionr2​ρ​(𝐫)r^{2}\rho(\mathbf{r})(known in nuclear physics as the Schiff moment[117,45]).
That said, from rankn=4n=4onwards, there are generally multiple terms that come into play, and the decompositionMi​j​k​l(4)=μi​j​k​l(4)+35​\trigbraces​𝒮^i​j​k​l​μi​j(2,2)​δk​l+67​μ(0,4)​\trigbraces​𝒮^i​j​k​l​δi​j​δk​l,\displaystyle M^{(4)}_{ijkl}=\mu^{(4)}_{ijkl}+\tfrac{3}{5}\trigbraces{\hat{\mathcal{S}}}_{ijkl}\mu^{(2,2)}_{ij}\delta_{kl}+\tfrac{6}{7}\mu^{(0,4)}\trigbraces{\hat{\mathcal{S}}}_{ijkl}\delta_{ij}\delta_{kl},(C.5)

separates outμi​j(2,2)\mu^{(2,2)}_{ij}, the octupole moment tensor of the distributionr2​ρ​(𝐫)r^{2}\rho(\mathbf{r}),
as well asμ(0,4)\mu^{(0,4)}, the rotationally-symmetric (monopole) average of the distributionr4​ρ​(𝐫)r^{4}\rho(\mathbf{r}),
since those two contributions form isolated subspaces that do not mix under arbitrary rotations.

The description of the general idea thus far, however, ignores the role of the fractional coefficients13\tfrac{1}{3},35\tfrac{3}{5}and67\tfrac{6}{7}in Eqs. (C.3) and (C.5).
In essence, these are required to account for the various ways in which indices can be combined when e.g. recoveringμi​j(2,2)\mu^{(2,2)}_{ij}fromMi​j​k​l(4)M^{(4)}_{ijkl}by taking the trace of the latter,Mi​j​k​k(4)M^{(4)}_{ijkk}.
In the following section we will derive a general formula for these coefficients.

## C.2The trace-removal projector: properties

In more formal terms, we work in the fully-symmetric tensor space of ranknn,\trigbraces​𝒮^​(ℂd⊗n)\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes n}), in dimensiond=3d=3.121212Keepingddsymbolic will help keep the arithmetic clearer later on.We then decompose this tensor space as a direct sum of irreducibleSO​(3)\mathrm{SO}(3)representations with angular momentum numberℓ\ell,\trigbraces​𝒮^​(ℂd⊗n)=⨁ℓ=0nℳℓ(n)\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes n})=\bigoplus_{\ell=0}^{n}\mathcal{M}^{(n)}_{\ell},
withℓ\ellrestricted to the same parity asnnin all summations in this section;
we illustrate this decomposition in Figure5.
We then define\trigbraces​Π^ℓ(n)\trigbraces{\hat{\Pi}^{(n)}_{\ell}}as the orthogonal projector ontoℳℓ(n)\mathcal{M}^{(n)}_{\ell}, so that for any𝐀(n)∈\trigbraces​𝒮^​(ℂd⊗n)\mathbf{A}^{(n)}\in\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes n})we will have𝐀(n)=∑ℓ=0n\trigbraces​Π^ℓ(n)​𝐀(n).\displaystyle\mathbf{A}^{(n)}=\sum_{\ell=0}^{n}\trigbraces{\hat{\Pi}^{(n)}_{\ell}}\mathbf{A}^{(n)}.(C.6)

We now need to establish ways to connect tensor spaces of different ranks.
In the ‘downward’ direction, we already know the clear link:
it is simply the trace operator,Tr:\trigbraces​𝒮^​(ℂd⊗n)→\trigbraces​𝒮^​(ℂd⊗(n−2))\Tr:\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes n})\to\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes(n-2)}).
In the upward direction, the overall idea is as we used in Eq. (C.5):
multiply by the isotropic tensor𝕀\mathbb{I}(whose components are the Kronecker delta,δi​j\delta_{ij}),
in a symmetrized way;
in other words, we define\trigbraces​ℒ^:\trigbraces​𝒮^​(ℂd⊗n)→\trigbraces​𝒮^​(ℂd⊗(n+2))\trigbraces{\hat{\mathcal{L}}}:\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes n})\to\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes(n+2)})via\trigbraces​ℒ^​(𝐀(n))=\trigbraces​𝒮^​(𝐀(n)⊗𝕀).\displaystyle\trigbraces{\hat{\mathcal{L}}}(\mathbf{A}^{(n)})=\trigbraces{\hat{\mathcal{S}}}(\mathbf{A}^{(n)}\otimes\mathbb{I}).(C.7)

Both of these linking operations are invariant underSO​(3)\mathrm{SO}(3)rotations, which implies that they will map the irreducible representationℳℓ(n)\mathcal{M}^{(n)}_{\ell}to its ‘neighbours’,ℳℓ(n±2)\mathcal{M}^{(n\pm 2)}_{\ell},
as shown in Fig.5,
crucially, preserving the angular momentum numberℓ\ell.
Moreover, since theℳℓ(n)\mathcal{M}^{(n)}_{\ell}are irreducible representations,
Schur’s lemma[54]implies that the compositionTr∘\trigbraces​ℒ^\Tr\circ\trigbraces{\hat{\mathcal{L}}}is a multiple of the identity,
or, in other words,
that the inverse of the tensor lift\trigbraces​ℒ^\trigbraces{\hat{\mathcal{L}}}onℳℓ(n)\mathcal{M}^{(n)}_{\ell}iscn,ℓ​Trc_{n,\ell}\Tr,
as indicated in Fig.5,
for some constantcn,ℓc_{n,\ell}.
Thesecn,ℓc_{n,\ell}are the coefficients13\tfrac{1}{3},35\tfrac{3}{5}and67\tfrac{6}{7}from Eqs. (C.3) and (C.5).Figure 5:Schematic of the decomposition of\trigbraces​𝒮^​(ℂd⊗n)\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes n})as a direct sum of irreducible representationsℳℓ(n)\mathcal{M}^{(n)}_{\ell}, and the links between the different subspaces via the trace and the tensor lift operator\trigbraces​ℒ^\trigbraces{\hat{\mathcal{L}}},
for even parity (top) and odd parity (bottom).

The values of thecn,ℓc_{n,\ell}coefficients can be calculated via a recursive argument, built on the combined action of the trace and tensor lift operators.
This can be shown, for an arbitrary tensor𝐀∈\trigbraces​𝒮^​(ℂd⊗n)\mathbf{A}\in\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes n}), to be given byTr[\trigbraces𝒮^(𝐀⊗𝕀)]\displaystyle\Tr\mathopen{}\left[\trigbraces{\hat{\mathcal{S}}}(\mathbf{A}\otimes\mathbb{I})\right]=2​(2​n+d)(n+2)​(n+1)​𝐀\displaystyle=\frac{2(2n+d)}{(n+2)(n+1)}\mathbf{A}(C.8)+n​(n−1)(n+2)​(n+1)​\trigbraces​𝒮^​(Tr⁡(𝐀)⊗𝕀),\displaystyle\qquad+\frac{n(n-1)}{(n+2)(n+1)}\trigbraces{\hat{\mathcal{S}}}(\Tr(\mathbf{A})\otimes\mathbb{I}),

i.e., as a sum of
our original tensor𝐀\mathbf{A},
plus the ‘opposite’ combination of the trace and lift operators,\trigbraces​ℒ^∘Tr\trigbraces{\hat{\mathcal{L}}}\circ\Tr.
A recursive argument based on (C.8),
the proof of which we defer to sectionC.7,
then provides the desired coefficients.

The result of that calculation is the following pairs of operators and their inverses:
- •

The inverse of\trigbraces​ℒ^\trigbraces{\hat{\mathcal{L}}}onℳℓ(ℓ+2​m)\mathcal{M}^{(\ell+2m)}_{\ell}iscℓ+2​m,ℓ​Trc_{\ell+2m,\ell}\Tr, with coefficientcℓ+2​m,ℓ\displaystyle c_{\ell+2m,\ell}=(ℓ+2​m+2)​(ℓ+2​m+1)2​(m+1)​(2​ℓ+2​m+d).\displaystyle=\frac{(\ell+2m+2)(\ell+2m+1)}{2(m+1)(2\ell+2m+d)}.(C.9)
- •

The inverse of themm-fold lift\trigbraces​ℒ^m\trigbraces{\hat{\mathcal{L}}}^{m}onℳℓ(ℓ)\mathcal{M}^{(\ell)}_{\ell}isbℓ,m​Trb_{\ell,m}\Tr, with coefficientbℓ,m\displaystyle b_{\ell,m}=cℓ+2​(m−1),ℓ​⋯​cℓ,ℓ\displaystyle=c_{\ell+2(m-1),\ell}\cdots c_{\ell,\ell}=(ℓ+2​m)!2m​m!​ℓ!​(2​ℓ−2+d)!!(2​ℓ+2​(m−1)+d)!!,\displaystyle=\frac{(\ell+2m)!}{2^{m}m!\ell!}\frac{(2\ell-2+d)!!}{(2\ell+2(m-1)+d)!!},(C.10)

wheren!!=n⋅(n−2)!!n!!=n\cdot(n-2)!!is the double factorial ofnn.

Alternatively, these two operator-inverse pairs can be rephrased as follows:
- •

The inverse of\trigbraces​ℒ^\trigbraces{\hat{\mathcal{L}}}onℳℓ(n)\mathcal{M}^{(n)}_{\ell}iscn,ℓ​Trc_{n,\ell}\Tr, with coefficientcn,ℓ\displaystyle c_{n,\ell}=(n+2)​(n+1)(n+2−ℓ)​(n+ℓ+d).\displaystyle=\frac{(n+2)(n+1)}{(n+2-\ell)(n+\ell+d)}.(C.11)
- •

Starting on an arbitrary representationℳℓ(n)\mathcal{M}^{(n)}_{\ell},
them=n−ℓ2m=\frac{n-\ell}{2}-fold tracebℓ,n−ℓ2​Trn−ℓ2b_{\ell,\frac{n-\ell}{2}}\Tr^{\frac{n-\ell}{2}}will mapℳℓ(n)\mathcal{M}^{(n)}_{\ell}ontoℳℓ(ℓ)\mathcal{M}^{(\ell)}_{\ell},
with inverse\trigbraces​ℒ^n−ℓ2\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}},
and with coefficientbℓ,n−ℓ2\displaystyle b_{\ell,\frac{n-\ell}{2}}=n!2n−ℓ2​(n−ℓ2)!​ℓ!​(2​ℓ−2+d)!!(n+ℓ−2+d)!!.\displaystyle=\frac{n!}{2^{\frac{n-\ell}{2}}(\tfrac{n-\ell}{2})!\ell!}\frac{(2\ell-2+d)!!}{(n+\ell-2+d)!!}.(C.12)

## C.3The multipolar projectors\trigbraces​Π^ℓ(n)\trigbraces{\hat{\Pi}^{(n)}_{\ell}}

With this algebra in hand, it is now easy to provide an explicit definition for the trace-removal projectors\trigbraces​Π^ℓ(n)\trigbraces{\hat{\Pi}^{(n)}_{\ell}}.
This is also done recursively, starting with the lowest angular momentum numbersℓ=0\ell=0andℓ=1\ell=1, where we have\trigbraces​Π^0(n)​𝐀\displaystyle\trigbraces{\hat{\Pi}^{(n)}_{0}}\mathbf{A}=b0,n2​\trigbraces​ℒ^n2​(Trn2⁡(𝐀))\displaystyle=b_{0,\frac{n}{2}}\trigbraces{\hat{\mathcal{L}}}^{\frac{n}{2}}(\Tr^{\frac{n}{2}}(\mathbf{A}))\trigbraces​Π^1(n)​𝐀\displaystyle\trigbraces{\hat{\Pi}^{(n)}_{1}}\mathbf{A}=b1,n−12​\trigbraces​ℒ^n−12​(Trn−12⁡(𝐀)),\displaystyle=b_{1,\frac{n-1}{2}}\trigbraces{\hat{\mathcal{L}}}^{\frac{n-1}{2}}(\Tr^{\frac{n-1}{2}}(\mathbf{A})),(C.13)

since the trace operator, iterated as many times as will fit, will eliminate the contributions fromℓ>0\ell>0(resp.ℓ>1\ell>1) representations.
For arbitraryℓ\ell, the projector\trigbraces​Π^ℓ(n)\trigbraces{\hat{\Pi}^{(n)}_{\ell}}is defined as\trigbraces​Π^ℓ(n)​𝐀\displaystyle\trigbraces{\hat{\Pi}^{(n)}_{\ell}}\mathbf{A}=bℓ,n−ℓ2\trigbracesℒ^n−ℓ2(Trn−ℓ2(𝐀−∑ℓ′<ℓ\trigbracesΠ^ℓ′(n)𝐀))\displaystyle=b_{\ell,\frac{n-\ell}{2}}\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}\mathopen{}\left(\Tr^{\frac{n-\ell}{2}}\mathopen{}\left(\mathbf{A}-\sum_{\ell^{\prime}<\ell}\trigbraces{\hat{\Pi}^{(n)}_{\ell^{\prime}}}\mathbf{A}\right)\right)=bℓ,n−ℓ2\trigbracesℒ^n−ℓ2(Trn−ℓ2(𝐀)−∑ℓ′<ℓ\trigbracesΠ^ℓ′(ℓ)Trn−ℓ2(𝐀)).\displaystyle=b_{\ell,\frac{n-\ell}{2}}\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}\mathopen{}\left(\Tr^{\frac{n-\ell}{2}}\mathopen{}\left(\mathbf{A}\right)-\sum_{\ell^{\prime}<\ell}\trigbraces{\hat{\Pi}^{(\ell)}_{\ell^{\prime}}}\Tr^{\frac{n-\ell}{2}}\mathopen{}\left(\mathbf{A}\right)\right).(C.14)

i.e.,
first removing the representations withℓ′<ℓ\ell^{\prime}<\ellusing explicit projectors\trigbraces​Π^ℓ′(n)\trigbraces{\hat{\Pi}^{(n)}_{\ell^{\prime}}},
and then removing the representations withℓ′>ℓ\ell^{\prime}>\ellthrough a suitable combination of the trace and lift operators.
(This can then be simplified slightly by performing theℓ′<ℓ\ell^{\prime}<\ellremovalafterthen−ℓ2\frac{n-\ell}{2}-fold trace, as in the second line of (C.3), i.e., while the tensor is momentarily living in\trigbraces​𝒮^​(ℂd⊗ℓ)\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes\ell}), which is smaller and thus more efficient.)

Finally, we turn briefly to some useful algebraic ways to frame these relationships.
As mentioned earlier, the iterated lift
iterated lift\trigbraces​ℒ^n−ℓ2\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}is the inverse of the iterated tracebℓ,n−ℓ2​Trn−ℓ2b_{\ell,\frac{n-\ell}{2}}\Tr^{\frac{n-\ell}{2}}acting onℳℓ(n)\mathcal{M}^{(n)}_{\ell}, so we can write\trigbraces​ℒ^n−ℓ2​(bℓ,n−ℓ2​Trn−ℓ2⁡(\trigbraces​Π^ℓ(n)​𝐀))\displaystyle\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}(b_{\ell,\frac{n-\ell}{2}}\Tr^{\frac{n-\ell}{2}}(\trigbraces{\hat{\Pi}^{(n)}_{\ell}}\mathbf{A}))=\trigbraces​Π^ℓ(n)​𝐀.\displaystyle=\trigbraces{\hat{\Pi}^{(n)}_{\ell}}\mathbf{A}.(C.15)

Moreover, it is also possible to shift where the multipolar projection happens, so that we getbℓ,n−ℓ2​\trigbraces​ℒ^n−ℓ2​(\trigbraces​Π^ℓ(ℓ)​Trn−ℓ2⁡(𝐀))\displaystyle b_{\ell,\frac{n-\ell}{2}}\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}(\trigbraces{\hat{\Pi}^{(\ell)}_{\ell}}\Tr^{\frac{n-\ell}{2}}(\mathbf{A}))=\trigbraces​Π^ℓ(n)​𝐀,\displaystyle=\trigbraces{\hat{\Pi}^{(n)}_{\ell}}\mathbf{A},(C.16)

and by applying the iterated trace once again, we can rephrase this as the operator commutation relation\trigbraces​Π^ℓ(ℓ)​Trn−ℓ2⁡(𝐀)\displaystyle\trigbraces{\hat{\Pi}^{(\ell)}_{\ell}}\Tr^{\frac{n-\ell}{2}}(\mathbf{A})=Trn−ℓ2⁡(\trigbraces​Π^ℓ(n)​𝐀).\displaystyle=\Tr^{\frac{n-\ell}{2}}(\trigbraces{\hat{\Pi}^{(n)}_{\ell}}\mathbf{A}).(C.17)

Similar relationships, such as\trigbraces​Π^ℓ(n)​\trigbraces​ℒ^n−ℓ2​(𝐀)\displaystyle\trigbraces{\hat{\Pi}^{(n)}_{\ell}}\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}(\mathbf{A})=\trigbraces​ℒ^n−ℓ2​(\trigbraces​Π^ℓ(ℓ)​𝐀)\displaystyle=\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}(\trigbraces{\hat{\Pi}^{(\ell)}_{\ell}}\mathbf{A})(C.18)

for𝐀∈\trigbraces​𝒮^​(ℂd⊗ℓ)\mathbf{A}\in\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes\ell}), can be derived through equivalent formulations.

## C.4Extra tensor theory

In this section we turn to further details of the tensorial multipolar moments,
in order to provide a more fleshed-out theory,
but, most importantly, to show the key links between the tensorial version of the multipolar moments𝝁(ℓ)\boldsymbol{\mu}^{(\ell)}and the more well-known spherical multipolar momentsMℓ​mM_{\ell m}which come from the standard integration of the form∫rℓ​Yℓ​m​(θ,ϕ)​ρ​(𝐫)​d​𝐫\int r^{\ell}Y_{\ell m}(\theta,\phi)\rho(\mathbf{r})\textrm{d}\mathbf{r},
as well as to show a crucial link between our newly-defined triple tensor product and the standard Wigner3​j3jsymbols.

We begin with the (traceless) tensorial multipolar moments, defined in Eq. (3), which we recall as𝝁(ℓ)=Π^ℓ​𝐌(ℓ),\displaystyle\boldsymbol{\mu}^{(\ell)}=\hat{\Pi}_{\ell}\mathbf{M}^{(\ell)},

obtained from the tensorial moments𝐌(ℓ)\mathbf{M}^{(\ell)}using the trace-removal projectorΠ^ℓ\hat{\Pi}_{\ell},
and we examine in more depth their relation to the other objects in play.

The information contained in𝝁(ℓ)\boldsymbol{\mu}^{(\ell)}is equivalent to that contained in the (‘standard’) spherical multipolar momentsMℓ​m=∫Sℓ​m​(𝐫)​ρ​(𝐫)​d​𝐫∝∫rℓ​Yℓ​m​(θ,ϕ)​ρ​(𝐫)​d​𝐫,\displaystyle M_{\ell m}=\int S_{\ell m}(\mathbf{r})\rho(\mathbf{r})\textrm{d}\mathbf{r}\propto\int r^{\ell}Y_{\ell m}(\theta,\phi)\rho(\mathbf{r})\textrm{d}\mathbf{r},(C.19)

given by the integral ofρ​(𝐫)\rho(\mathbf{r})multiplied by the spherical harmonicYl​m​(θ,ϕ)Y_{lm}(\theta,\phi).
For our purposes, the handling is much cleaner if we phrase this in terms of the solid harmonicSℓ​m​(𝐫)=4​π2​ℓ+1​rℓ​Yℓ​m​(θ,ϕ),S_{\ell m}(\mathbf{r})=\sqrt{\frac{4\pi}{2\ell+1}}\>r^{\ell}\>Y_{\ell m}(\theta,\phi),(C.20)

as the latter is a homogeneous polynomial of degreeℓ\ellin the Cartesian components(x,y,z)(x,y,z)of𝐫\mathbf{r}.

As a homogeneous polynomial, the solid harmonic can be expressed explicitly as a sum of monomials,Sℓ​m​(𝐫)=∑i1,…,iℓ(sℓ​m)i1​⋯​iℓ​xi1​⋯​xiℓ,\displaystyle S_{\ell m}(\mathbf{r})=\sum_{i_{1},\ldots,i_{\ell}}(s_{\ell m})_{i_{1}\cdots i_{\ell}}\;x_{i_{1}}\cdots x_{i_{\ell}},(C.21)

where the individual monomial coefficients(sℓ​m)i1​⋯​iℓ(s_{\ell m})_{i_{1}\cdots i_{\ell}}can be assembled as the components of a tensor𝐬^ℓ​m=∑i1,…,iℓ(sl​m)i1​⋯​iℓ​𝐞^i1⊗⋯⊗𝐞^iℓ\displaystyle\hat{\mathbf{s}}_{\ell m}=\sum_{i_{1},\ldots,i_{\ell}}(s_{lm})_{i_{1}\cdots i_{\ell}}\hat{\mathbf{e}}_{i_{1}}\otimes\cdots\otimes\hat{\mathbf{e}}_{i_{\ell}}(C.22)

which returnsSℓ​m​(𝐫)S_{\ell m}(\mathbf{r})when contracted with𝐫⊗ℓ\mathbf{r}^{\otimes\ell}:Sℓ​m​(𝐫)\displaystyle S_{\ell m}(\mathbf{r})=𝐬^ℓ​m

∙𝐫⊗ℓ.\displaystyle=\hat{\mathbf{s}}_{\ell m}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{r}^{\otimes\ell}.(C.23)

Moreover, this tensor can be found directly from the explicit polynomial expressions forSℓ​m​(𝐫)S_{\ell m}(\mathbf{r})[133, §5.1.7, though see also §5.2.3]Sℓ​m​(𝐫)\displaystyle S_{\ell m}(\mathbf{r})=(l+m)!​(l−m)!\displaystyle=\sqrt{(l+m)!(l-m)!}×∑p,q,r1p!​q!​r!(−x+i​y2)p(x−i​y2)qzr,\displaystyle\quad\times\sum_{p,q,r}\frac{1}{p!q!r!}\left(-\frac{x+iy}{2}\right)^{p}\left(\frac{x-iy}{2}\right)^{q}z^{r},(C.24)

where the summation indices are restricted top+q+r=ℓp+q+r=\ell,p−q=mp-q=m;
from this, we can simply infer directly the expression𝐬^ℓ​m\displaystyle\hat{\mathbf{s}}_{\ell m}=(ℓ+m)!​(ℓ−m)!∑p,q,r2−p+q2p!​q!​r!\trigbraces𝒮^[𝐞^+⊗p⊗𝐞^−⊗q⊗𝐞^0⊗r].\displaystyle=\sqrt{(\ell+m)!(\ell-m)!}\sum_{p,q,r}\frac{2^{-\frac{p+q}{2}}}{p!q!r!}\trigbraces{\hat{\mathcal{S}}}\mathopen{}\left[\hat{\mathbf{e}}_{+}^{\otimes p}{\otimes}\hat{\mathbf{e}}_{-}^{\otimes q}{\otimes}\hat{\mathbf{e}}_{0}^{\otimes r}\right].(C.25)

by replacing each Cartesian componentsxix_{i}of𝐫\mathbf{r}by the corresponding basis vectors𝐞^i\hat{\mathbf{e}}_{i}, which are then tensor-multiplied together,
where the spherical unit basis vectors are defined as𝐞^±=∓12​(𝐞^x±i​𝐞^y)\hat{\mathbf{e}}_{\pm}=\mp\frac{1}{\sqrt{2}}(\hat{\mathbf{e}}_{x}\pm i\hat{\mathbf{e}}_{y})and𝐞^0=𝐞^z\hat{\mathbf{e}}_{0}=\hat{\mathbf{e}}_{z}.

That said, it is convenient to reformulate these tensors slightly, by adding a normalization constant and taking the complex conjugate.
Thus, we define𝐭^ℓ​m\displaystyle\hat{\mathbf{t}}_{\ell m}=ℓ!(2​ℓ−1)!!​𝐬^ℓ​m∗,\displaystyle=\sqrt{\frac{\ell!}{(2\ell-1)!!}}\,\hat{\mathbf{s}}_{\ell m}^{*},(C.26)

which we term the𝐭^ℓ​m\hat{\mathbf{t}}_{\ell m}the multipolar basis tensors.
These obey the following basic properties:
- •

They are, of course, purely multipolar, soΠ^ℓ​𝐭^ℓ​m=𝐭^ℓ​m.\displaystyle\hat{\Pi}_{\ell}\hat{\mathbf{t}}_{\ell m}=\hat{\mathbf{t}}_{\ell m}.(C.27a)
- •

They are symmetric under complex conjugation via𝐭^ℓ​m∗=(−1)m​𝐭^ℓ,−m.\displaystyle\hat{\mathbf{t}}_{\ell m}^{*}=(-1)^{m}\hat{\mathbf{t}}_{\ell,-m}.(C.27b)
- •

They are orthonormal,𝐭^ℓ​m∗

∙𝐭^ℓ​m′=δm,m′.\displaystyle\hat{\mathbf{t}}_{\ell m}^{*}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\hat{\mathbf{t}}_{\ell m^{\prime}}=\delta_{m,m^{\prime}}.(C.27c)
- •

They satisfy the completeness relation∑m𝐭^ℓ​m​(𝐭^ℓ​m∗

∙𝐀(ℓ))=Π^ℓ​𝐀(ℓ),\displaystyle\sum_{m}\hat{\mathbf{t}}_{\ell m}(\hat{\mathbf{t}}_{\ell m}^{*}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{A}^{(\ell)})=\hat{\Pi}_{\ell}\mathbf{A}^{(\ell)},(C.27d)

where𝐀(ℓ)\mathbf{A}^{(\ell)}is an arbitrary tensor of rankℓ\ell,
with the sum
adding up to theℓ\ell-polar projectorΠ^ℓ\hat{\Pi}_{\ell}of rankℓ\ell.

More importantly, if we integrate Eq. (C.23) againstρ​(𝐫)\rho(\mathbf{r}), we obtain a clean relation between the spherical multipolar momentMℓ​mM_{\ell m}and the tensorial moment𝐌(ℓ)\mathbf{M}^{(\ell)},Mℓ​m\displaystyle M_{\ell m}=(2​ℓ−1)!!ℓ!​𝐭^ℓ​m∗

∙𝐌(ℓ).\displaystyle=\sqrt{\frac{(2\ell-1)!!}{\ell!}}\,\hat{\mathbf{t}}_{\ell m}^{*}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{M}^{(\ell)}.(C.28)

Furthermore, using Eq. (C.27a) and the fact that the projectorΠ^ℓ\hat{\Pi}_{\ell}is orthogonal (soΠ^ℓ​𝐀

∙𝐁=𝐀

∙Π^ℓ​𝐁\hat{\Pi}_{\ell}\mathbf{A}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{B}=\mathbf{A}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\hat{\Pi}_{\ell}\mathbf{B}), we can rephrase (C.28) asMℓ​m\displaystyle M_{\ell m}=(2​ℓ−1)!!ℓ!​𝐭^ℓ​m∗

∙𝝁(ℓ).\displaystyle=\sqrt{\frac{(2\ell-1)!!}{\ell!}}\,\hat{\mathbf{t}}_{\ell m}^{*}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\boldsymbol{\mu}^{(\ell)}.(C.29)

Similarly, we can use the completeness relation (C.27d) to obtain𝝁(ℓ)=ℓ!(2​ℓ−1)!!​∑mMℓ​m​𝐭^ℓ​m\displaystyle\boldsymbol{\mu}^{(\ell)}=\sqrt{\frac{\ell!}{(2\ell-1)!!}}\sum_{m}M_{\ell m}\hat{\mathbf{t}}_{\ell m}(C.30)

which fully encapsulates the claim that the spherical multipolar momentsMℓ​mM_{\ell m}are a minimal set of linearly-independent components of the tensorial multipolar moment𝝁(ℓ)\boldsymbol{\mu}^{(\ell)}.

With this in hand, we can now examine our chirality measure, the traceless chiral moments from Eq. (8), which combine the tensorial multipolar moments into the pseudoscalarhℓ1​ℓ2​ℓ3=(𝝁(ℓ1)×𝝁(ℓ2))(ℓ3)

∙𝝁(ℓ3)h_{\ell_{1}\ell_{2}\ell_{3}}=\left(\boldsymbol{\mu}^{(\ell_{1})}\ignorespaces\times\ignorespaces\boldsymbol{\mu}^{(\ell_{2})}\right)^{(\ell_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\boldsymbol{\mu}^{(\ell_{3})}using our tensor triple product.
With the tooling we have just developed, we can use the basis expansion (C.30) to reducehℓ1​ℓ2​ℓ3h_{\ell_{1}\ell_{2}\ell_{3}}to products of the spherical multipolar momentsMℓ​mM_{\ell m}, which gives ushℓ1​ℓ2​ℓ3\displaystyle h_{\ell_{1}\ell_{2}\ell_{3}}=ℓ1!(2​ℓ1−1)!!​ℓ2!(2​ℓ2−1)!!​ℓ3!(2​ℓ3−1)!!\displaystyle=\sqrt{\frac{\ell_{1}!}{(2\ell_{1}-1)!!}\frac{\ell_{2}!}{(2\ell_{2}-1)!!}\frac{\ell_{3}!}{(2\ell_{3}-1)!!}}×∑m1,m2,m3Mℓ1​m1Mℓ2​m2Mℓ3​m3\displaystyle\qquad\times\sum_{m_{1},m_{2},m_{3}}M_{\ell_{1}m_{1}}M_{\ell_{2}m_{2}}M_{\ell_{3}m_{3}}×(𝐭^ℓ1​m1×𝐭^ℓ2​m2)(ℓ3)

∙𝐭^ℓ3​m3.\displaystyle\qquad\qquad\times\left(\hat{\mathbf{t}}_{\ell_{1}m_{1}}\ignorespaces\times\ignorespaces\hat{\mathbf{t}}_{\ell_{2}m_{2}}\right)^{(\ell_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\hat{\mathbf{t}}_{\ell_{3}m_{3}}.(C.31)

This is a crucial relationship:
it is structured as a superposition of cubic products of spherical multipolar moments,Mℓ​mM_{\ell m}, which combine to form a (pseudo)scalar;
as mentioned in the main text, this has strong consequences.

Specifically,
the relationship (C.31) is structured as a linear superposition of the components of the triple tensor productMℓ1​m1​Mℓ2​m2​Mℓ3​m3M_{\ell_{1}m_{1}}M_{\ell_{2}m_{2}}M_{\ell_{3}m_{3}},
where each of the tensor factors comes from an irreducible representation of the rotation groupSO​(3)\mathrm{SO}(3),
and where the combined sum is a scalar, i.e., is in theℓ=0\ell=0representation of the triple-tensor-product representation.
The representation theory of the rotational group[54]then enforces a uniqueness theorem, which requires the coefficients in the superposition to be multiples of the Wigner3​j3jsymbols.
In other words, Eq. (C.31) requires the identity(𝐭^ℓ1​m1×𝐭^ℓ2​m2)(ℓ3)

∙𝐭^ℓ3​m3\displaystyle\left(\hat{\mathbf{t}}_{\ell_{1}m_{1}}\ignorespaces\times\ignorespaces\hat{\mathbf{t}}_{\ell_{2}m_{2}}\right)^{(\ell_{3})}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\hat{\mathbf{t}}_{\ell_{3}m_{3}}=Nℓ1​ℓ2​ℓ3​(ℓ1ℓ2ℓ3m1m2m3),\displaystyle=N_{\ell_{1}\ell_{2}\ell_{3}}\begin{pmatrix}\ell_{1}&\ell_{2}&\ell_{3}\\
m_{1}&m_{2}&m_{3}\end{pmatrix},(C.32)

for some normalization constantNℓ1​ℓ2​ℓ3N_{\ell_{1}\ell_{2}\ell_{3}}.131313We find the result (C.32) to be remarkable as well as highly useful in forming and cementing intuition:
it illuminates the ‘true nature’ of the Wigner3​j3jsymbols, which are revealed as simply the cross product between the multipolar basis tensors;
and, separately,
it helps understand that cross product, as it is just the familiar Wigner3​j3jsymbol.
(Of course, only one of those directions is likely to be useful, depending on whether one’s intuitive understanding of the Wigner3​j3jsymbols or of the tensor cross product is stronger.)

## C.5Tensorial moments for polynomial distributions

To wrap up our summary of the properties of multipolar tensors, in this section we turn to some useful properties that apply when the distribution itself is a well-behaved polynomial.

Thus, in particular, we consider distributions of the formρ​(𝐫)\displaystyle\rho(\mathbf{r})=𝐂(k)

∙𝐫⊗k​f​(r)\displaystyle=\mathbf{C}^{(k)}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{r}^{\otimes k}f(r)=Ci1​⋯​ik(k)​xi1​⋯​xik​f​(r),\displaystyle=C^{(k)}_{i_{1}\cdots i_{k}}x_{i_{1}}\cdots x_{i_{k}}f(r),(C.33)

where the polynomial coefficients can be enclosed as a symmetric tensor𝐂(k)\mathbf{C}^{(k)}of rankkk,
and we also include a spherically-symmetric functionf​(r)f(r)(so that e.g. the distribution can be confined to a sphere, withf​(r)=δ​(r−1)f(r)=\delta(r-1),
or simply to ensure convergent integrals through, say, a gaussian filterf​(r)=e−r2/σ2f(r)=e^{-r^{2}/\sigma^{2}}).

We then ask the question:
what are the tensorial moments𝐌(n)=∫𝐫⊗n​ρ​(𝐫)​d​𝐫\mathbf{M}^{(n)}=\int\mathbf{r}^{\otimes n}\rho(\mathbf{r})\textrm{d}\mathbf{r}ofρ​(𝐫)\rho(\mathbf{r}),
and how do they relate to our initial coefficient𝐂(k)\mathbf{C}^{(k)}?
Standard intuition tells us that if𝐂(k)\mathbf{C}^{(k)}is strictlyℓ\ell-polar (and thusρ​(𝐫)\rho(\mathbf{r})is proportional to a superposition of spherical harmonics with well-definedℓ\ell), then the tensorial moment𝐌(k)\mathbf{M}^{(k)}must coincide with the𝐂(k)\mathbf{C}^{(k)}, and this is indeed the case.
But what happens when𝐂(k)\mathbf{C}^{(k)}is not strictly multipolar?

The proof is straightforward but cumbersome, and we defer it to sectionC.6.
The overall result rides on the standard intuition for fully-multipolar distributions:
first decompose𝐂(k)\mathbf{C}^{(k)}into its multipolar components, and each of these will translate transparently to the corresponding moment tensor𝐌(n)\mathbf{M}^{(n)}.

The most straightforward case is whenk=nk=n, in which case the relationship reads𝐌(n)\displaystyle\mathbf{M}^{(n)}=∑ℓ4​π​ℓ!(2​ℓ+1)!!​bℓ,n−ℓ2​\trigbraces​Π^ℓ(n)​𝐂(n)\displaystyle=\sum_{\ell}\frac{4\pi\ell!\>}{(2\ell+1)!!}b_{\ell,\frac{n-\ell}{2}}\ \trigbraces{\hat{\Pi}^{(n)}_{\ell}}\mathbf{C}^{(n)}×∫0∞r2​n+2f(r)dr,\displaystyle\quad\times\int_{0}^{\infty}r^{2n+2}f(r)\textrm{d}r,(C.34)

i.e.,𝐌(n)\mathbf{M}^{(n)}is a superposition of theℓ\ell-polar components of𝐂(k)\mathbf{C}^{(k)}, withℓ\ell-dependent coefficients,
multiplied by the radial integral∫0∞r2​n+2​f​(r)​d​r\int_{0}^{\infty}r^{2n+2}f(r)\textrm{d}r.
Of course, as promised, when𝐂(ℓ)=\trigbraces​Π^ℓ(ℓ)​𝐂(ℓ)\mathbf{C}^{(\ell)}=\trigbraces{\hat{\Pi}^{(\ell)}_{\ell}}\mathbf{C}^{(\ell)}has well-defined multipolarity, this result simplifies further, to𝐌(ℓ)\displaystyle\mathbf{M}^{(\ell)}=4​π​ℓ!(2​ℓ+1)!!​∫0∞r2​ℓ+2​f​(r)​d​r​𝐂(ℓ).\displaystyle=\frac{4\pi\ell!\>}{(2\ell+1)!!}\int_{0}^{\infty}\!\!\!\!r^{2\ell+2}f(r)\textrm{d}r\ \mathbf{C}^{(\ell)}.(C.35)

Things are more complicated in the case whenk≠nk\neq n, as then the𝐂(k)\mathbf{C}^{(k)}need to be traced down, or lifted up, to match the ranknnof the desired moment.
Thus, for the general case, as we prove in sectionC.6, we have𝐌(n)\displaystyle\mathbf{M}^{(n)}=∑ℓmin⁡(n,k)4​π​ℓ!(2​ℓ+1)!!​bℓ,n−ℓ2​bℓ,k−ℓ2​∫0∞rn+k+2​f​(r)​d​r\displaystyle=\sum_{\ell}^{\min(n,k)}\frac{4\pi\ell!}{(2\ell+1)!!}b_{\ell,\frac{n-\ell}{2}}b_{\ell,\frac{k-\ell}{2}}\int_{0}^{\infty}r^{n+k+2}f(r)\textrm{d}r×\trigbraces​ℒ^n−ℓ2​(\trigbraces​Π^ℓ(ℓ)​Trk−ℓ2⁡(𝐂(k))).\displaystyle\quad\times\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}(\trigbraces{\hat{\Pi}^{(\ell)}_{\ell}}\Tr^{\frac{k-\ell}{2}}(\mathbf{C}^{(k)})).(C.36)

The lift and the trace operators that appear here are partial inverses, but they appear to different orders.
Thus, this can simplify if we restrict it to the cases whenn>kn>k, where we have𝐌(n)\displaystyle\mathbf{M}^{(n)}=∑ℓ4​π​ℓ!(2​ℓ+1)!!​bℓ,n−ℓ2​\trigbraces​ℒ^n−k2​(\trigbraces​Π^ℓ(k)​𝐂(k))\displaystyle=\sum_{\ell}\frac{4\pi\ell!}{(2\ell+1)!!}b_{\ell,\frac{n-\ell}{2}}\>\trigbraces{\hat{\mathcal{L}}}^{\frac{n-k}{2}}(\trigbraces{\hat{\Pi}^{(k)}_{\ell}}\mathbf{C}^{(k)})×∫0∞rn+k+2f(r)dr.\displaystyle\quad\times\int_{0}^{\infty}r^{n+k+2}f(r)\textrm{d}r.(C.37)

and, similarly, forn<kn<k,𝐌(n)\displaystyle\mathbf{M}^{(n)}=∑ℓ4​π​ℓ!(2​ℓ+1)!!​bℓ,k−ℓ2​\trigbraces​Π^ℓ(n)​Trk−n2⁡(𝐂(k))\displaystyle=\sum_{\ell}\frac{4\pi\ell!}{(2\ell+1)!!}b_{\ell,\frac{k-\ell}{2}}\>\trigbraces{\hat{\Pi}^{(n)}_{\ell}}\Tr^{\frac{k-n}{2}}(\mathbf{C}^{(k)})×∫0∞rn+k+2f(r)dr.\displaystyle\quad\times\int_{0}^{\infty}r^{n+k+2}f(r)\textrm{d}r.(C.38)

## C.6Tensorial moments for polynomial distributions: rigorous proof

As in sectionC.5, in this section we onsider a distribution of the formρ​(𝐫)=𝐂(k)

∙𝐫⊗k​f​(r)\rho(\mathbf{r})=\mathbf{C}^{(k)}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{r}^{\otimes k}f(r)for some symmetric tensor𝐂(k)\mathbf{C}^{(k)}of rankkkand a spherically-symmetric functionf​(r)f(r),
and aim to calculate its rank-nntensorial moment𝐌(n)=∫𝐫⊗n​ρ​(𝐫)​d​𝐫\mathbf{M}^{(n)}=\int\mathbf{r}^{\otimes n}\rho(\mathbf{r})\textrm{d}\mathbf{r}.

To do this, we expand both𝐌(n)\mathbf{M}^{(n)}and𝐂(k)\mathbf{C}^{(k)}as superpositions of their multipolar components,
after which we can
shift the multipolar projector to a lower tensor rank using (C.16),𝐌(n)\displaystyle\mathbf{M}^{(n)}=∫𝐫⊗n​ρ​(𝐫)​d​𝐫\displaystyle=\int\mathbf{r}^{\otimes n}\rho(\mathbf{r})\textrm{d}\mathbf{r}=∑ℓ,ℓ′∫(\trigbraces​Π^ℓ(n)​𝐫⊗n)​(\trigbraces​Π^ℓ′(k)​𝐂(k))

∙𝐫⊗k​f​(r)​d​𝐫\displaystyle=\sum_{\ell,\ell^{\prime}}\int\left(\trigbraces{\hat{\Pi}^{(n)}_{\ell}}\mathbf{r}^{\otimes n}\right)\left(\trigbraces{\hat{\Pi}^{(k)}_{\ell^{\prime}}}\mathbf{C}^{(k)}\right)\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{r}^{\otimes k}f(r)\textrm{d}\mathbf{r}=∑ℓ,ℓ′∫(bℓ,n−ℓ2​\trigbraces​ℒ^n−ℓ2​(\trigbraces​Π^ℓ(ℓ)​Trn−ℓ2⁡(𝐫⊗n)))\displaystyle=\sum_{\ell,\ell^{\prime}}\int\left(b_{\ell,\frac{n-\ell}{2}}\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}(\trigbraces{\hat{\Pi}^{(\ell)}_{\ell}}\Tr^{\frac{n-\ell}{2}}(\mathbf{r}^{\otimes n}))\right)×(bℓ′,k−ℓ′2​\trigbraces​ℒ^k−ℓ′2​(\trigbraces​Π^ℓ′(ℓ′)​Trk−ℓ′2⁡(𝐂(k))))

∙𝐫⊗k​f​(r)​d​𝐫\displaystyle\quad{\times}\left(b_{\ell^{\prime},\frac{k-\ell^{\prime}}{2}}\trigbraces{\hat{\mathcal{L}}}^{\frac{k-\ell^{\prime}}{2}}(\trigbraces{\hat{\Pi}^{(\ell^{\prime})}_{\ell^{\prime}}}\Tr^{\frac{k-\ell^{\prime}}{2}}(\mathbf{C}^{(k)}))\right)\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{r}^{\otimes k}\!f(r)\textrm{d}\mathbf{r}=∑ℓ,ℓ′bℓ,n−ℓ2​bℓ′,k−ℓ′2​\trigbraces​ℒ^n−ℓ2​∫d​𝐫​f​(r)​rk−ℓ′​rn−ℓ​\trigbraces​Π^ℓ(ℓ)​𝐫⊗ℓ\displaystyle=\sum_{\ell,\ell^{\prime}}b_{\ell,\frac{n-\ell}{2}}b_{\ell^{\prime},\frac{k-\ell^{\prime}}{2}}\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}\int\!\textrm{d}\mathbf{r}\>f(r)r^{k-\ell^{\prime}}r^{n-\ell}\trigbraces{\hat{\Pi}^{(\ell)}_{\ell}}\mathbf{r}^{\otimes\ell}×(\trigbraces​Π^ℓ′(ℓ′)​Trk−ℓ′2⁡(𝐂(k)))

∙𝐫⊗k\displaystyle\quad\times\left(\trigbraces{\hat{\Pi}^{(\ell^{\prime})}_{\ell^{\prime}}}\Tr^{\frac{k-\ell^{\prime}}{2}}(\mathbf{C}^{(k)})\right)\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{r}^{\otimes k}(C.39)

and then use the completeness relation (C.27d) for the multipolar projectors:𝐌(n)\displaystyle\mathbf{M}^{(n)}=∑ℓ,ℓ′∑m,m′bℓ,n−ℓ2​bℓ′,k−ℓ′2​\trigbraces​ℒ^n−ℓ2​(𝐭^ℓ​m)\displaystyle=\sum_{\ell,\ell^{\prime}}\sum_{m,m^{\prime}}b_{\ell,\frac{n-\ell}{2}}b_{\ell^{\prime},\frac{k-\ell^{\prime}}{2}}\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}(\hat{\mathbf{t}}_{\ell m})×(𝐭^ℓ′​m′∗

∙Trk−ℓ′2⁡(𝐂(k)))\displaystyle\quad\times\left(\hat{\mathbf{t}}_{\ell^{\prime}m^{\prime}}^{*}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\Tr^{\frac{k-\ell^{\prime}}{2}}(\mathbf{C}^{(k)})\right)(C.40)×∫(𝐭^ℓ​m∗

∙𝐫⊗ℓ)(𝐭^ℓ′​m′

∙𝐫⊗k)rk−ℓ′rn−ℓf(r)d𝐫,\displaystyle\quad\times\int(\hat{\mathbf{t}}_{\ell m}^{*}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{r}^{\otimes\ell})\left(\hat{\mathbf{t}}_{\ell^{\prime}m^{\prime}}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{r}^{\otimes k}\right)r^{k-\ell^{\prime}}r^{n-\ell}f(r)\textrm{d}\mathbf{r},

which then becomes, using (C.26), (C.23) and (C.20),𝐌(n)\displaystyle\mathbf{M}^{(n)}=∑ℓ,ℓ′∑m,m′4​π​ℓ!(2​ℓ+1)!!​4​π​ℓ′!(2​ℓ′+1)!!​bℓ,n−ℓ2​bℓ′,k−ℓ′2\displaystyle=\sum_{\ell,\ell^{\prime}}\sum_{m,m^{\prime}}\sqrt{\frac{4\pi\ell!}{(2\ell+1)!!}\frac{4\pi\ell^{\prime}!}{(2\ell^{\prime}+1)!!}}b_{\ell,\frac{n-\ell}{2}}b_{\ell^{\prime},\frac{k-\ell^{\prime}}{2}}×\trigbraces​ℒ^n−ℓ2​(𝐭^ℓ​m)​(𝐭^ℓ′​m′∗

∙Trk−ℓ′2⁡(𝐂(k)))\displaystyle\quad\times\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}(\hat{\mathbf{t}}_{\ell m})\left(\hat{\mathbf{t}}_{\ell^{\prime}m^{\prime}}^{*}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\Tr^{\frac{k-\ell^{\prime}}{2}}(\mathbf{C}^{(k)})\right)(C.41)×∫Yℓ​m(𝐫)Yℓ′​m′∗(𝐫)rn+kf(r)d𝐫,\displaystyle\quad\times\int Y_{\ell m}(\mathbf{r})Y_{\ell^{\prime}m^{\prime}}^{*}(\mathbf{r})r^{n+k}f(r)\textrm{d}\mathbf{r},

and, since∫Yℓ​m​(𝐫)​Yℓ′​m′∗​(𝐫)​rn+k​f​(r)​d​𝐫\int Y_{\ell m}(\mathbf{r})Y_{\ell^{\prime}m^{\prime}}^{*}(\mathbf{r})r^{n+k}f(r)\textrm{d}\mathbf{r}is diagonal and equal toδℓ​ℓ′​δm​m′​∫0∞rn+k+2​f​(r)​d​r\delta_{\ell\ell^{\prime}}\delta_{mm^{\prime}}\int_{0}^{\infty}r^{n+k+2}f(r)\textrm{d}r,𝐌(n)\displaystyle\mathbf{M}^{(n)}=∑ℓ,m4​π​ℓ!(2​ℓ+1)!!​bℓ,n−ℓ2​bℓ,k−ℓ2​∫0∞rn+k+2​f​(r)​d​r\displaystyle=\sum_{\ell,m}\frac{4\pi\ell!}{(2\ell+1)!!}b_{\ell,\frac{n-\ell}{2}}b_{\ell,\frac{k-\ell}{2}}\int_{0}^{\infty}r^{n+k+2}f(r)\textrm{d}r×\trigbraces​ℒ^n−ℓ2​(𝐭^ℓ​m​(𝐭^ℓ​m∗

∙Trk−ℓ2⁡(𝐂(k)))),\displaystyle\quad\times\trigbraces{\hat{\mathcal{L}}}^{\frac{n-\ell}{2}}(\hat{\mathbf{t}}_{\ell m}\left(\hat{\mathbf{t}}_{\ell m}^{*}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\Tr^{\frac{k-\ell}{2}}(\mathbf{C}^{(k)})\right)),(C.42)

where the limits of theℓ,ℓ′\ell,\ell^{\prime}summations transform via∑ℓn∑ℓ′kδℓ​ℓ′=∑ℓmin⁡(n,k)\sum_{\ell}^{n}\sum_{\ell^{\prime}}^{k}\delta_{\ell\ell^{\prime}}=\sum_{\ell}^{\min(n,k)}.

Finally, we can remove themmdependence by re-applying the completeness relation (C.27d), and this gives us the full result (C.36) from the overview section.

## C.7The trace-removal projector: rigorous proofs

In this section, we provide a fuller proof of the values of the coefficientscn,ℓc_{n,\ell}andbℓ,mb_{\ell,m}, starting with the general identity (C.8).
The simplest place to start is the representation with maximal angular momentum numberℓ=n\ell=n, which is defined (within this framework) as the ‘simple’ case, whereTr⁡(𝐀)=0\Tr(\mathbf{A})=0vanishes.
For that case, the identity (C.8) is already sufficient to determine the coefficient of interest,cℓ,ℓ=(ℓ+2)​(ℓ+1)2​(2​ℓ+d),\displaystyle c_{\ell,\ell}=\frac{(\ell+2)(\ell+1)}{2(2\ell+d)},(C.43)

as the second term vanishes.

For representations with higher rank than angular momentum (i.e.n>ℓn>\ell), as indicated in Fig.5, we work recursively:
we iterate the identity (C.8) until we reach tensors of rankℓ\ell, where the trace will vanish, and use this to compute the chain of coefficients.
Thus, we rephrase Eq. (C.8) into the formTr⁡[\trigbraces​ℒ^​(𝐀)]=un​𝐀\displaystyle\Tr[\trigbraces{\hat{\mathcal{L}}}(\mathbf{A})]=u_{n}\mathbf{A}+vn​\trigbraces​ℒ^​(Tr⁡(𝐀))\displaystyle+v_{n}\trigbraces{\hat{\mathcal{L}}}(\Tr(\mathbf{A}))(C.44)withun=2​(2​n+d)(n+2)​(n+1),\displaystyle\text{with}\quad u_{n}=\frac{2(2n+d)}{(n+2)(n+1)},vn=n​(n−1)(n+2)​(n+1),\displaystyle\ v_{n}=\frac{n(n-1)}{(n+2)(n+1)},

which we can then apply recursively.
Thus, as the first step, by applying this form but replacing𝐀\mathbf{A}with\trigbraces​ℒ^​(𝐀)\trigbraces{\hat{\mathcal{L}}}(\mathbf{A}), we getTr⁡[\trigbraces​ℒ^2​(𝐀)]\displaystyle\Tr[\trigbraces{\hat{\mathcal{L}}}^{2}(\mathbf{A})]=un+2​\trigbraces​ℒ^​(𝐀)+vn+2​\trigbraces​ℒ^​(Tr⁡(\trigbraces​ℒ^​(𝐀)))\displaystyle=u_{n+2}\trigbraces{\hat{\mathcal{L}}}(\mathbf{A})+v_{n+2}\trigbraces{\hat{\mathcal{L}}}(\Tr(\trigbraces{\hat{\mathcal{L}}}(\mathbf{A})))=un+2​\trigbraces​ℒ^​(𝐀)+vn+2​\trigbraces​ℒ^​(un​𝐀+vn​\trigbraces​ℒ^​(Tr⁡(𝐀)))\displaystyle=u_{n+2}\trigbraces{\hat{\mathcal{L}}}(\mathbf{A})+v_{n+2}\trigbraces{\hat{\mathcal{L}}}(u_{n}\mathbf{A}+v_{n}\trigbraces{\hat{\mathcal{L}}}(\Tr(\mathbf{A})))=(un+2+vn+2​un)​\trigbraces​ℒ^​(𝐀)+vn+2​vn​\trigbraces​ℒ^2​(Tr⁡(𝐀)).\displaystyle=(u_{n+2}{+}v_{n+2}u_{n})\trigbraces{\hat{\mathcal{L}}}(\mathbf{A})+v_{n+2}v_{n}\trigbraces{\hat{\mathcal{L}}}^{2}(\Tr(\mathbf{A})).(C.45)

for𝐀∈\trigbraces​𝒮^​(ℂd⊗n)\mathbf{A}\in\trigbraces{\hat{\mathcal{S}}}(\mathbb{C}^{d\otimes n})of ranknn.

To apply this, we set𝐀∈ℳℓ(ℓ)\mathbf{A}\in\mathcal{M}^{(\ell)}_{\ell}, giving us a tensor\trigbraces​ℒ^​(𝐀)∈ℳℓ(ℓ+2)\trigbraces{\hat{\mathcal{L}}}(\mathbf{A})\in\mathcal{M}^{(\ell+2)}_{\ell}with the property thatTr⁡(𝐀)=0\Tr(\mathbf{A})=0,
so that we can read off the next coefficient of interest,cℓ+2,ℓ\displaystyle c_{\ell+2,\ell}=(uℓ+2+vℓ+2​uℓ)−1\displaystyle=(u_{\ell+2}+v_{\ell+2}u_{\ell})^{-1}=(ℓ+4)​(ℓ+3)22​(2​ℓ+2+d),\displaystyle=\frac{(\ell+4)(\ell+3)}{2^{2}(2\ell+2+d)},(C.46)

which determinescℓ+2,ℓ​Trc_{\ell+2,\ell}\Tras the inverse of\trigbraces​ℒ^\trigbraces{\hat{\mathcal{L}}}onℳℓ(ℓ+2)\mathcal{M}^{(\ell+2)}_{\ell}.
Moreover, we can also get the inverse of therepeatedlift operator,\trigbraces​ℒ^2\trigbraces{\hat{\mathcal{L}}}^{2}, onℳℓ(ℓ)\mathcal{M}^{(\ell)}_{\ell}, given bybℓ,2​Tr2b_{\ell,2}\Tr^{2}, with coefficientbℓ,2\displaystyle b_{\ell,2}=cℓ+2,2​cℓ,2\displaystyle=c_{\ell+2,2}c_{\ell,2}=(ℓ+4)​(ℓ+3)22​(2​ℓ+2+d)​(ℓ+2)​(ℓ+1)2​(2​ℓ+d)\displaystyle=\frac{(\ell+4)(\ell+3)}{2^{2}(2\ell+2+d)}\frac{(\ell+2)(\ell+1)}{2(2\ell+d)}=(ℓ+4)!23​ℓ!​(2​ℓ−2+d)!!(2​ℓ+2+d)!!.\displaystyle=\frac{(\ell+4)!}{2^{3}\ell!}\frac{(2\ell-2+d)!!}{(2\ell+2+d)!!}.(C.47)

A similar argument then proves the general case by induction.

## Appendix DPerturbation theory derivation

As described in SectionIV, here we consider in detail the perturbation-theory calculation for chiral photoionization.
We use the simplest example of photoionization driven by a chiral field: resonantly-enhanced two-photon ionization of atomic hydrogen driven by an elliptically-polarized fundamental, combined with a second harmonic with linear polarization orthogonal to the fundamental’s plane of ellipticity.

Thus, we consider a hydrogen atom, initially in its ground state, ionized by the bichromaticω:2​ω\omega:2\omegafield𝐄(t)=Re[𝐄1e−i​ω​t+𝐄2e−2​i​ω​t]f(t),\displaystyle\mathbf{E}(t)=\operatorname{Re}\mathopen{}\left[\mathbf{E}_{1}e^{-i\omega t}+\mathbf{E}_{2}e^{-2i\omega t}\right]f(t),(D.1)

where𝐄1\mathbf{E}_{1}and𝐄2\mathbf{E}_{2}are complex field-polarization amplitudes,
andf​(t)=exp⁡(−t2/2​T2)f(t)=\exp(-t^{2}/2T^{2})is a gaussian envelope.
We tune the fields close to the1​s1s-2​p2ptransition, with a detuningδ​ω=ω−(E2​p−E1​s)/ℏ\delta\omega=\omega-(E_{2p}-E_{1s})/\hbar.

In these conditions, the dynamics will be confined to the bound2​p2pmanifold, and to the ionized continuum including s, p and d waves (withℓ=0,1\ell=0,1and 2, respectively),
centred at energy12​me​p02=E1​s+2​ω\frac{1}{2m_{e}}p_{0}^{2}=E_{1s}+2\omega,
which we write in the form|ψ​(t)⟩\displaystyle\ket{\psi(t)}=a100​(t)​e−i​E1​s​t/ℏ​|100⟩\displaystyle=a_{100}(t)e^{-iE_{1s}t/\hbar}\ket{100}+∑ma21​m​(t)​e−i​E2​p​t/ℏ​|21​m⟩\displaystyle\qquad+\sum_{m}a_{21m}(t)e^{-iE_{2p}t/\hbar}\ket{21m}+∑ℓ,m∫0∞d​p​bℓ​m​(p,t)​e−i​p2​t2​me​ℏ​|p,ℓ​m⟩.\displaystyle\qquad+\sum_{\ell,m}\int_{0}^{\infty}\!\!\textrm{d}p\ b_{\ell m}(p,t)e^{-\frac{ip^{2}t}{2m_{e}\hbar}}\ket{p,\ell m}.(D.2)

Our observable of interest is the momentum-resolved wavefunction,ψ​(𝐩)=⟨𝐩|ψ​(t→∞)⟩\psi(\mathbf{p})=\innerproduct{\mathbf{p}}{\psi(t\to\infty)},
evaluated at the end of the pulse,
and its corresponding population density,ρ​(𝐩)=|ψ​(𝐩)|2\rho(\mathbf{p})=|\psi(\mathbf{p})|^{2}.

In the rotating-wave approximation, the hamiltonian of the system,H^=H^0+qe​𝐫^⋅𝐄​(t)\hat{H}=\hat{H}_{0}+q_{e}\hat{\mathbf{r}}\cdot\mathbf{E}(t),
induces
the bound-bound transition from1​s1sto2​p2p,
from1​s1sto thepp-wave continuum,
and from2​p2pto thess- anddd-wave continua.
Thus, the Schrödinger equation readsi​ℏ​a˙21​m​(t)\displaystyle i\hbar\,\dot{a}_{21m}(t)=12​e−i​δ​ω​t​f​(t)​⟨21​m|qe​𝐫^|100⟩⋅𝐄1​a100​(t)\displaystyle=\frac{1}{2}e^{-i\delta\omega\,t}f(t)\matrixelement{21m}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}a_{100}(t)(D.3)i​ℏ​b˙00​(p,t)\displaystyle i\hbar\,\dot{b}_{00}(p,t)=12​e−i​p2−p022​me​ℏ​t​f​(t)​∑m⟨p,00|qe​𝐫^|21​m⟩⋅𝐄1​a21​m​(t)\displaystyle=\frac{1}{2}e^{-i\frac{p^{2}-p_{0}^{2}}{2m_{e}\hbar}t}f(t)\sum_{m}\matrixelement{p,00}{q_{e}\hat{\mathbf{r}}}{21m}\cdot\mathbf{E}_{1}\,a_{21m}(t)(D.4)i​ℏ​b˙1​m​(p,t)\displaystyle i\hbar\,\dot{b}_{1m}(p,t)=12​e−i​p2−p022​me​ℏ​t​f​(t)​⟨p,1​m|qe​𝐫^|100⟩⋅𝐄2​a100​(t)\displaystyle=\frac{1}{2}e^{-i\frac{p^{2}-p_{0}^{2}}{2m_{e}\hbar}t}f(t)\matrixelement{p,1m}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{2}a_{100}(t)(D.5)i​ℏ​b˙2​m​(p,t)\displaystyle i\hbar\,\dot{b}_{2m}(p,t)=12​e−i​p2−p022​me​ℏ​t​f​(t)​∑m′⟨p,2​m|qe​𝐫^|21​m′⟩⋅𝐄1​a21​m′​(t),\displaystyle=\frac{1}{2}e^{-i\frac{p^{2}-p_{0}^{2}}{2m_{e}\hbar}t}f(t)\sum_{m^{\prime}}\matrixelement{p,2m}{q_{e}\hat{\mathbf{r}}}{21m^{\prime}}\cdot\mathbf{E}_{1}\,a_{21m^{\prime}}(t),(D.6)

We solve this system within perturbation theory, assuming thata100​(t)≡1a_{100}(t)\equiv 1, from which we can then read directly the solutionsa21​m​(t)\displaystyle a_{21m}(t)=12​i​ℏ​∫−∞td​t′​e−i​δ​ω​t′​f​(t′)​⟨21​m|qe​𝐫^|100⟩⋅𝐄1\displaystyle=\frac{1}{2i\hbar}\int_{-\infty}^{t}\!\!\textrm{d}t^{\prime}e^{-i\delta\omega\,t^{\prime}}f(t^{\prime})\matrixelement{21m}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}(D.7)b1​m​(p,t)\displaystyle b_{1m}(p,t)=12​i​ℏ​∫−∞td​t′​e−i​p2−p022​me​ℏ​t′​f​(t′)​⟨p,1​m|qe​𝐫^|100⟩⋅𝐄2\displaystyle=\frac{1}{2i\hbar}\int_{-\infty}^{t}\!\!\textrm{d}t^{\prime}e^{-i\frac{p^{2}-p_{0}^{2}}{2m_{e}\hbar}t^{\prime}}f(t^{\prime})\matrixelement{p,1m}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{2}(D.8)

for thepp-state components,
and from these we obtain thess- anddd-state components asb00​(p,t)\displaystyle b_{00}(p,t)=−14​ℏ2​∫−∞td​t′​e−i​p2−p022​me​ℏ​t′​f​(t′)​∑m⟨p,00|qe​𝐫^|21​m⟩⋅𝐄1​∫−∞t′d​t′′​e−i​δ​ω​t′′​f​(t′′)​⟨21​m|qe​𝐫^|100⟩⋅𝐄1\displaystyle=-\frac{1}{4\hbar^{2}}\int_{-\infty}^{t}\!\!\textrm{d}t^{\prime}e^{-i\frac{p^{2}-p_{0}^{2}}{2m_{e}\hbar}t^{\prime}}f(t^{\prime})\sum_{m}\matrixelement{p,00}{q_{e}\hat{\mathbf{r}}}{21m}\cdot\mathbf{E}_{1}\int_{-\infty}^{t^{\prime}}\!\!\textrm{d}t^{\prime\prime}e^{-i\delta\omega\,t^{\prime\prime}}f(t^{\prime\prime})\matrixelement{21m}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}=−14​ℏ2​(∑m⟨p,00|qe​𝐫^|21​m⟩⋅𝐄1​⟨21​m|qe​𝐫^|100⟩⋅𝐄1)​(∫−∞td​t′​e−i​p2−p022​me​ℏ​t′​f​(t′)​∫−∞t′d​t′′​e−i​δ​ω​t′′​f​(t′′))\displaystyle=-\frac{1}{4\hbar^{2}}\left(\sum_{m}\matrixelement{p,00}{q_{e}\hat{\mathbf{r}}}{21m}\cdot\mathbf{E}_{1}\matrixelement{21m}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}\right)\left(\int_{-\infty}^{t}\!\!\textrm{d}t^{\prime}e^{-i\frac{p^{2}-p_{0}^{2}}{2m_{e}\hbar}t^{\prime}}f(t^{\prime})\int_{-\infty}^{t^{\prime}}\!\!\textrm{d}t^{\prime\prime}e^{-i\delta\omega\,t^{\prime\prime}}f(t^{\prime\prime})\right)(D.9)b2​m​(p,t)\displaystyle b_{2m}(p,t)=−14​ℏ2​∫−∞td​t′​e−i​p2−p022​me​ℏ​t′​f​(t′)​∑m′⟨p,2​m|qe​𝐫^|21​m′⟩⋅𝐄1​∫−∞t′d​t′′​e−i​δ​ω​t′′​f​(t′′)​⟨21​m′|qe​𝐫^|100⟩⋅𝐄1\displaystyle=-\frac{1}{4\hbar^{2}}\int_{-\infty}^{t}\!\!\textrm{d}t^{\prime}e^{-i\frac{p^{2}-p_{0}^{2}}{2m_{e}\hbar}t^{\prime}}f(t^{\prime})\sum_{m^{\prime}}\matrixelement{p,2m}{q_{e}\hat{\mathbf{r}}}{21m^{\prime}}\cdot\mathbf{E}_{1}\int_{-\infty}^{t^{\prime}}\!\!\textrm{d}t^{\prime\prime}e^{-i\delta\omega\,t^{\prime\prime}}f(t^{\prime\prime})\matrixelement{21m^{\prime}}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}=−14​ℏ2​(∑m′⟨p,2​m|qe​𝐫^|21​m′⟩⋅𝐄1​⟨21​m′|qe​𝐫^|100⟩⋅𝐄1)​(∫−∞td​t′​e−i​p2−p022​me​ℏ​t′​f​(t′)​∫−∞t′d​t′′​e−i​δ​ω​t′′​f​(t′′)).\displaystyle=-\frac{1}{4\hbar^{2}}\left(\sum_{m^{\prime}}\matrixelement{p,2m}{q_{e}\hat{\mathbf{r}}}{21m^{\prime}}\cdot\mathbf{E}_{1}\matrixelement{21m^{\prime}}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}\right)\left(\int_{-\infty}^{t}\!\!\textrm{d}t^{\prime}e^{-i\frac{p^{2}-p_{0}^{2}}{2m_{e}\hbar}t^{\prime}}f(t^{\prime})\int_{-\infty}^{t^{\prime}}\!\!\textrm{d}t^{\prime\prime}e^{-i\delta\omega\,t^{\prime\prime}}f(t^{\prime\prime})\right).(D.10)

Both of these components are cleanly separated into two factors – one encoding the directional dependence, and the second containing the temporal and energy information.

These form a complete solution to the problem, and allow us to reconstruct the final wavefunction,
using the partial-wave expansion|𝐩⟩=∑l​mYl​m​(𝐩^)∗​|p,l​m⟩\displaystyle\ket{\mathbf{p}}=\sum_{lm}Y_{lm}(\hat{\mathbf{p}})^{*}\ket{p,lm}(D.11)

for the scattering states, givingψ​(𝐩)\displaystyle\psi(\mathbf{p})=∑ℓ,mYl​m​(𝐩^)​bℓ​m​(p,∞).\displaystyle=\sum_{\ell,m}Y_{lm}(\hat{\mathbf{p}})b_{\ell m}(p,\infty).(D.12)

The dependence on the pulse parameters is fully contained within two functions of the photoelectron momentumpp, which correspond to the temporal factors in (D.8) and (D.10),c1​(p)\displaystyle c_{1}(p)=12​i​ℏ​∫−∞∞d​t′​e−i​δ​ω​t′​f​(t′)\displaystyle=\frac{1}{2i\hbar}\int_{-\infty}^{\infty}\!\!\textrm{d}t^{\prime}e^{-i\delta\omega\,t^{\prime}}f(t^{\prime})(D.13a)c2​(p)\displaystyle c_{2}(p)=−14​ℏ2​∫−∞∞d​t′​e−i​p2−p022​me​ℏ​t′​f​(t′)​∫−∞t′d​t′′​e−i​δ​ω​t′′​f​(t′′)\displaystyle=-\frac{1}{4\hbar^{2}}\int_{-\infty}^{\infty}\!\!\textrm{d}t^{\prime}e^{-i\frac{p^{2}-p_{0}^{2}}{2m_{e}\hbar}t^{\prime}}f(t^{\prime})\int_{-\infty}^{t^{\prime}}\!\!\textrm{d}t^{\prime\prime}e^{-i\delta\omega\,t^{\prime\prime}}f(t^{\prime\prime})(D.13b)

encoding the one- and two-photon processes, respectively.
This allows us to write the final wavefunction in the formψ​(𝐩)\displaystyle\psi(\mathbf{p})=c1​(p)​∑mY1​m​(𝐩^)​⟨p,1​m|qe​𝐫^|100⟩⋅𝐄2\displaystyle=c_{1}(p)\sum_{m}Y_{1m}(\hat{\mathbf{p}})\matrixelement{p,1m}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{2}+c2​(p)​∑mY00​(𝐩^)​⟨p,00|qe​𝐫^|21​m⟩⋅𝐄1​⟨21​m|qe​𝐫^|100⟩⋅𝐄1\displaystyle\quad+c_{2}(p)\sum_{m}Y_{00}(\hat{\mathbf{p}})\matrixelement{p,00}{q_{e}\hat{\mathbf{r}}}{21m}\cdot\mathbf{E}_{1}\matrixelement{21m}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}+c2​(p)​∑m,m′Y2​m​(𝐩^)​⟨p,2​m|qe​𝐫^|21​m′⟩⋅𝐄1​⟨21​m′|qe​𝐫^|100⟩⋅𝐄1.\displaystyle\quad+c_{2}(p)\sum_{m,m^{\prime}}Y_{2m}(\hat{\mathbf{p}})\matrixelement{p,2m}{q_{e}\hat{\mathbf{r}}}{21m^{\prime}}\cdot\mathbf{E}_{1}\matrixelement{21m^{\prime}}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}.(D.14)

Our main focus here is on the angular dependence, which is encoded in the dipole transition matrix elements.
To deal with these cleanly, we use the spherical basis vectors,𝐞^±=∓12​(𝐞^x±i​𝐞^y)\hat{\mathbf{e}}_{\pm}=\mp\tfrac{1}{\sqrt{2}}(\hat{\mathbf{e}}_{x}\pm i\hat{\mathbf{e}}_{y})and𝐞^0=𝐞^z\hat{\mathbf{e}}_{0}=\hat{\mathbf{e}}_{z},
with which we can write any arbitrary vector𝐯\mathbf{v}in the form𝐯=∑q=−11vq​𝐞^q∗=4​π3​v​∑q=−11Y1​q​(𝐯^)​𝐞^q∗,\mathbf{v}=\sum_{q=-1}^{1}v_{q}\hat{\mathbf{e}}_{q}^{*}=\sqrt{\frac{4\pi}{3}}v\sum_{q=-1}^{1}Y_{1q}(\hat{\mathbf{v}})\hat{\mathbf{e}}_{q}^{*},(D.15)

and dot products between real-valued vectors as𝐮⋅𝐯=∑q=−11uq∗​vq=∑q=−11uq​vq∗\mathbf{u}\cdot\mathbf{v}=\sum_{q=-1}^{1}u_{q}^{*}v_{q}=\sum_{q=-1}^{1}u_{q}v_{q}^{*}.
This allows us to write all of the matrix elements, via the Wigner-Eckart theorem[133, §13.1.1], in the form⟨p,1​m|𝐫^|100⟩⋅𝐄2\displaystyle\matrixelement{p,1m}{\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{2}=4​π3​∑q=−11⟨p,1​m|r^​Y1​q​(𝐫^)|100⟩​𝐞^q∗⋅𝐄2=4​π3​∑q=−11(−1)1−m​⟨p,1||r^||10⟩​(110−mq0)​𝐞^q∗⋅𝐄2\displaystyle=\sqrt{\frac{4\pi}{3}}\sum_{q=-1}^{1}\matrixelement{p,1m}{\hat{r}Y_{1q}(\hat{\mathbf{r}})}{100}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{2}=\sqrt{\frac{4\pi}{3}}\sum_{q=-1}^{1}(-1)^{1-m}\matrixelement{p,1}{|\hat{r}|}{10}\begin{pmatrix}1&1&0\\
-m&q&0\end{pmatrix}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{2}(D.16)⟨21​m|𝐫^|100⟩⋅𝐄1\displaystyle\matrixelement{21m}{\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}=4​π3​∑q=−11⟨21​m|r^​Y1​q​(𝐫^)|100⟩​𝐞^q∗⋅𝐄1=4​π3​∑q=−11(−1)1−m​⟨21||r^||10⟩​(110−mq0)​𝐞^q∗⋅𝐄1\displaystyle=\sqrt{\frac{4\pi}{3}}\sum_{q=-1}^{1}\matrixelement{21m}{\hat{r}Y_{1q}(\hat{\mathbf{r}})}{100}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{1}=\sqrt{\frac{4\pi}{3}}\sum_{q=-1}^{1}(-1)^{1-m}\matrixelement{21}{|\hat{r}|}{10}\begin{pmatrix}1&1&0\\
-m&q&0\end{pmatrix}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{1}(D.17)⟨p,00|𝐫^|21​m⟩⋅𝐄1\displaystyle\matrixelement{p,00}{\hat{\mathbf{r}}}{21m}\cdot\mathbf{E}_{1}=4​π3​∑q=−11⟨p,00|r^​Y1​q​(𝐫^)|21​m⟩​𝐞^q∗⋅𝐄1=4​π3​∑q=−11⟨p,0||r^||21⟩​(0110qm)​𝐞^q∗⋅𝐄1\displaystyle=\sqrt{\frac{4\pi}{3}}\sum_{q=-1}^{1}\matrixelement{p,00}{\hat{r}Y_{1q}(\hat{\mathbf{r}})}{21m}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{1}=\sqrt{\frac{4\pi}{3}}\sum_{q=-1}^{1}\matrixelement{p,0}{|\hat{r}|}{21}\begin{pmatrix}0&1&1\\
0&q&m\end{pmatrix}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{1}(D.18)⟨p,2​m|𝐫^|21​m′⟩⋅𝐄1\displaystyle\matrixelement{p,2m}{\hat{\mathbf{r}}}{21m^{\prime}}\cdot\mathbf{E}_{1}=4​π3​∑q=−11⟨p,2​m|r^​Y1​q​(𝐫^)|21​m′⟩​𝐞^q∗⋅𝐄1=4​π3​∑q=−11(−1)m​⟨p,2||r^||21⟩​(211−mqm′)​𝐞^q∗⋅𝐄1.\displaystyle=\sqrt{\frac{4\pi}{3}}\sum_{q=-1}^{1}\matrixelement{p,2m}{\hat{r}Y_{1q}(\hat{\mathbf{r}})}{21m^{\prime}}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{1}=\sqrt{\frac{4\pi}{3}}\sum_{q=-1}^{1}(-1)^{m}\matrixelement{p,2}{|\hat{r}|}{21}\begin{pmatrix}2&1&1\\
-m&q&m^{\prime}\end{pmatrix}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{1}.(D.19)

And, finally, we can use these to write the combinations that appear in our final-state wavefunction (D.14) in the form∑mY1​m​(𝐩^)​⟨p,1​m|qe​𝐫^|100⟩⋅𝐄2\displaystyle\sum_{m}Y_{1m}(\hat{\mathbf{p}})\matrixelement{p,1m}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{2}=4​π3​⟨p,1||qe​r^||10⟩​∑m,q(−1)1−m​Y1​m​(𝐩^)​(110−mq0)​𝐞^q∗⋅𝐄2\displaystyle=\sqrt{\frac{4\pi}{3}}\matrixelement{p,1}{|q_{e}\hat{r}|}{10}\sum_{m,q}(-1)^{1-m}Y_{1m}(\hat{\mathbf{p}})\begin{pmatrix}1&1&0\\
-m&q&0\end{pmatrix}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{2}=13​p​⟨p,1||qe​r^||10⟩​𝐩⋅𝐄2\displaystyle=\frac{1}{\sqrt{3}p}\matrixelement{p,1}{|q_{e}\hat{r}|}{10}\mathbf{p}\cdot\mathbf{E}_{2}(D.20)∑mY00​(𝐩^)​⟨p,00|qe​𝐫^|21​m⟩⋅𝐄1​⟨21​m|qe​𝐫^|100⟩⋅𝐄1\displaystyle\sum_{m}Y_{00}(\hat{\mathbf{p}})\matrixelement{p,00}{q_{e}\hat{\mathbf{r}}}{21m}\cdot\mathbf{E}_{1}\matrixelement{21m}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}=4​π3​⟨p,0||qe​r^||21⟩​⟨21||qe​r^||10⟩\displaystyle=\frac{\sqrt{4\pi}}{3}\matrixelement{p,0}{|q_{e}\hat{r}|}{21}\matrixelement{21}{|q_{e}\hat{r}|}{10}×∑m,q,q′(−1)1−m(0110q′m)(110−mq0)𝐞^q′∗⋅𝐄1𝐞^q∗⋅𝐄1\displaystyle\qquad\times\sum_{m,q,q^{\prime}}(-1)^{1-m}\begin{pmatrix}0&1&1\\
0&q^{\prime}&m\end{pmatrix}\begin{pmatrix}1&1&0\\
-m&q&0\end{pmatrix}\hat{\mathbf{e}}_{q^{\prime}}^{*}\cdot\mathbf{E}_{1}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{1}=−4​π9​⟨p,0||qe​r^||21⟩​⟨21||qe​r^||10⟩​𝐄1⋅𝐄1\displaystyle=-\frac{\sqrt{4\pi}}{9}\matrixelement{p,0}{|q_{e}\hat{r}|}{21}\matrixelement{21}{|q_{e}\hat{r}|}{10}\mathbf{E}_{1}\cdot\mathbf{E}_{1}(D.21)∑m,m′Y2​m​(𝐩^)​⟨p,2​m|qe​𝐫^|21​m′⟩⋅𝐄1​⟨21​m′|qe​𝐫^|100⟩⋅𝐄1\displaystyle\sum_{m,m^{\prime}}Y_{2m}(\hat{\mathbf{p}})\matrixelement{p,2m}{q_{e}\hat{\mathbf{r}}}{21m^{\prime}}\cdot\mathbf{E}_{1}\matrixelement{21m^{\prime}}{q_{e}\hat{\mathbf{r}}}{100}\cdot\mathbf{E}_{1}=4​π3​⟨p,2||r^||21⟩​⟨21||r^||10⟩​∑m,m′,q,q′(−1)1−m′−m\displaystyle=\frac{4\pi}{3}\matrixelement{p,2}{|\hat{r}|}{21}\matrixelement{21}{|\hat{r}|}{10}\sum_{m,m^{\prime},q,q^{\prime}}(-1)^{1-m^{\prime}-m}×Y2​m​(𝐩^)​(211−mq′m′)​(110−m′q0)​𝐞^q∗⋅𝐄1​𝐞^q′∗⋅𝐄1\displaystyle\qquad\times Y_{2m}(\hat{\mathbf{p}})\begin{pmatrix}2&1&1\\
-m&q^{\prime}&m^{\prime}\end{pmatrix}\begin{pmatrix}1&1&0\\
-m^{\prime}&q&0\end{pmatrix}\hat{\mathbf{e}}_{q}^{*}\cdot\mathbf{E}_{1}\hat{\mathbf{e}}_{q^{\prime}}^{*}\cdot\mathbf{E}_{1}=20​π3​⟨p,2||qe​r^||21⟩​⟨21||qe​r^||10⟩p2​\trigbraces​Π^2​𝐩⊗2

∙𝐄1⊗2.\displaystyle=\frac{\sqrt{20\pi}}{3}\frac{\matrixelement{p,2}{|q_{e}\hat{r}|}{21}\matrixelement{21}{|q_{e}\hat{r}|}{10}}{p^{2}}\trigbraces{\hat{\Pi}_{2}}\mathbf{p}^{\otimes 2}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{E}_{1}^{\otimes 2}.(D.22)

This wraps up our calculations of the wavefunction, as these expressions can then be inserted directly into (D.14) to give usψ​(𝐩)\displaystyle\psi(\mathbf{p})=cp​(p)​𝐩⋅𝐄2+cs​(p)​𝐄1⋅𝐄1+cd​(p)​\trigbraces​Π^2​𝐩⊗2

∙𝐄1⊗2\displaystyle=c_{\mathrm{p}}(p)\>\mathbf{p}\cdot\mathbf{E}_{2}+c_{\mathrm{s}}(p)\>\mathbf{E}_{1}\cdot\mathbf{E}_{1}+c_{\mathrm{d}}(p)\>\trigbraces{\hat{\Pi}_{2}}\mathbf{p}^{\otimes 2}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{E}_{1}^{\otimes 2}(D.23)

in terms of the spherically-symmetric amplitudescp​(p)\displaystyle c_{\mathrm{p}}(p)=c1​(p)​13​p​⟨p,1||qe​r^||10⟩\displaystyle=c_{1}(p)\frac{1}{\sqrt{3}p}\matrixelement{p,1}{|q_{e}\hat{r}|}{10}(D.24a)cs​(p)\displaystyle c_{\mathrm{s}}(p)=−c2​(p)​4​π9​⟨p,0||qe​r^||21⟩​⟨21||qe​r^||10⟩\displaystyle=-c_{2}(p)\frac{\sqrt{4\pi}}{9}\matrixelement{p,0}{|q_{e}\hat{r}|}{21}\matrixelement{21}{|q_{e}\hat{r}|}{10}(D.24b)cd​(p)\displaystyle c_{\mathrm{d}}(p)=c2​(p)​20​π3​⟨p,2||qe​r^||21⟩​⟨21||qe​r^||10⟩p2.\displaystyle=c_{2}(p)\frac{\sqrt{20\pi}}{3}\frac{\matrixelement{p,2}{|q_{e}\hat{r}|}{21}\matrixelement{21}{|q_{e}\hat{r}|}{10}}{p^{2}}.(D.24c)

To relate this to experiment, we now need to calculate the experimental observable, namely, the measured photoelectron momentum distributionρ​(𝐩)=|ψ​(𝐩)|2\rho(\mathbf{p})=|\psi(\mathbf{p})|^{2},
which readsρ​(𝐩)\displaystyle\rho(\mathbf{p})=|cs(p)𝐄1⋅𝐄1|2+Re[2cs∗(p)cp(p)(𝐄1∗⋅𝐄1∗)𝐄2]⋅𝐩\displaystyle=\left|c_{\mathrm{s}}(p)\>\mathbf{E}_{1}\cdot\mathbf{E}_{1}\right|^{2}+\operatorname{Re}\mathopen{}\left[2c_{\mathrm{s}}^{*}(p)c_{\mathrm{p}}(p)(\mathbf{E}_{1}^{*}\cdot\mathbf{E}_{1}^{*})\mathbf{E}_{2}\right]\cdot\mathbf{p}+Re[2cs∗(p)cd(p)(𝐄1∗⋅𝐄1∗)\trigbracesΠ^2𝐄1⊗2+|cp(p)|2𝐄2∗⊗𝐄2]

∙𝐩⊗2\displaystyle\quad+\operatorname{Re}\mathopen{}\left[2c_{\mathrm{s}}^{*}(p)c_{\mathrm{d}}(p)(\mathbf{E}_{1}^{*}\cdot\mathbf{E}_{1}^{*})\trigbraces{\hat{\Pi}_{2}}\mathbf{E}_{1}^{\otimes 2}+|c_{\mathrm{p}}(p)|^{2}\mathbf{E}_{2}^{*}\otimes\mathbf{E}_{2}\right]\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{p}^{\otimes 2}+Re[2cp∗(p)cd(p)\trigbraces𝒮^(𝐄2∗⊗\trigbracesΠ^2𝐄1⊗2)]

∙𝐩⊗3\displaystyle\quad+\operatorname{Re}\mathopen{}\left[2c_{\mathrm{p}}^{*}(p)c_{\mathrm{d}}(p)\>\trigbraces{\hat{\mathcal{S}}}(\mathbf{E}_{2}^{*}\otimes\trigbraces{\hat{\Pi}_{2}}\mathbf{E}_{1}^{\otimes 2})\right]\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{p}^{\otimes 3}+Re[|cd(p)|2\trigbracesΠ^2𝐄1∗⁣⊗2⊗\trigbracesΠ^2𝐄1⊗2]

∙𝐩⊗4,\displaystyle\quad+\operatorname{Re}\mathopen{}\left[|c_{\mathrm{d}}(p)|^{2}\>\trigbraces{\hat{\Pi}_{2}}\mathbf{E}_{1}^{*\otimes 2}\otimes\trigbraces{\hat{\Pi}_{2}}\mathbf{E}_{1}^{\otimes 2}\right]\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\mathbf{p}^{\otimes 4},(D.25)

organized by the tensor rank of the power of𝐩\mathbf{p}involved.

For generic polarization vectors𝐄1\mathbf{E}_{1}and𝐄2\mathbf{E}_{2}, it is fully possible to extract
the unabridged tensorial moments𝐌(n)\mathbf{M}^{(n)}(as well as the traceless tensorial multipolar moments𝝁(ℓ)\boldsymbol{\mu}^{(\ell)})
for the distribution (D.25),
following the definitions given in the main text and the formalism from AppendixC.5.
From the distribution (D.25), one can read off directly that
the rank-4 moment𝐌(4)\mathbf{M}^{(4)}will be a fourth-degree polynomial in𝐄1\mathbf{E}_{1}and𝐄1∗\mathbf{E}_{1}^{*}and the rank-3 moment𝐌(3)\mathbf{M}^{(3)}will be a fourth-degree polynomial in𝐄1\mathbf{E}_{1},𝐄2\mathbf{E}_{2}, and their conjugates,
coming from the coefficients in front of𝐩⊗4\mathbf{p}^{\otimes 4}and𝐩⊗3\mathbf{p}^{\otimes 3}, respectively.
The rank-2 tensor𝐌(2)\mathbf{M}^{(2)}, coming from the𝐩⊗2\mathbf{p}^{\otimes 2}term, contains polynomials of degrees 2 and 4 in these amplitudes, depending on the ionization channel.

These nonzero moments guide directly toχ234\chi_{234}as a natural chiral measure,141414The traceless momenth234h_{234}also appears as a natural candidate, with identical considerations.which, as a product of those three moments, must therefore emerge as a polynomial of mixed rank, containing both ninth- and eleventh-degree terms – in quite a combinatoric variety.
Those polynomials, while hard to instantly visualize for the general case, are an essential result, as they show a direct connection between the photoelectron momentum distribution
and
the chiral nonlinear correlation functions of the electromagnetic field which have been proposed[8]to quantify the chirality of synthetic chiral light;
in the notation of Ref.[8]they would have the formh(9)h^{(9)}andh(11)h^{(11)}.

The field configuration we use is the same as was proposed previously for giant enantiosensitivity in high-order harmonic generation[8], where the chirality of the field is determined by thefifth-order chiral correlation function (h(5)h^{(5)}).
In our case, our results show that for ionization, in contrast, even the simplest possible configurations already involve, at least, chiral correlation functions of the ninth order and higher.
The reason is clear: in our formalism the experimental observable is the population density, which is a higher-order object, and there is no direct access to the wavefunction itself, or its coherence.


These general considerations aside, we now turn to get a concrete idea of the behaviour of our chiral measures for the final distribution (D.25).
Even for the particular field configuration at play
(𝐄1=E1​11+ϵ2​(𝐞^x+i​ϵ​𝐞^y)\mathbf{E}_{1}=E_{1}\frac{1}{\sqrt{1+\epsilon^{2}}}(\hat{\mathbf{e}}_{x}+i\epsilon\hat{\mathbf{e}}_{y})elliptically polarized in thex​yxyplane,
and𝐄2=E2​ei​φ​𝐞^z\mathbf{E}_{2}=E_{2}e^{i\varphi}\hat{\mathbf{e}}_{z}orthogonal to that plane)
the tensorial moments𝐌(n)\mathbf{M}^{(n)}are rather cumbersome, but they can be handled easily through computer algebra;
our implementation of that process is available as Ref.[106].
The end result for the chiral momentχ234\chi_{234}is, then,χ234\displaystyle\chi_{234}=213​π335​53​73ϵ​(ϵ2−1)(ϵ2+1)4E16E2p024(Δp)3|cd(p0)|2Im[{4p02E14|cd(p0)|2ϵ2−3E22|cp(p0)|2(ϵ2+1)2\displaystyle=\frac{2^{13}\pi^{3}}{3^{5}\,5^{3}\,7^{3}}\frac{\epsilon(\epsilon^{2}-1)}{(\epsilon^{2}+1)^{4}}E_{1}^{6}E_{2}p_{0}^{24}(\Delta p)^{3}\ |c_{\mathrm{d}}(p_{0})|^{2}\operatorname{Im}\mathopen{}\Big[\Big\{4p_{0}^{2}E_{1}^{4}|c_{\mathrm{d}}(p_{0})|^{2}\epsilon^{2}-3E_{2}^{2}|c_{\mathrm{p}}(p_{0})|^{2}\left(\epsilon^{2}+1\right)^{2}+6E14cs∗(p0)cd(p0)ϵ2+12iE14Im(cs∗(p)cd(p))(ϵ2−1)2}cp(p0)cd∗(p0)ei​φ],\displaystyle\qquad\qquad\qquad\qquad\qquad+6E_{1}^{4}c_{\mathrm{s}}^{*}(p_{0})c_{\mathrm{d}}(p_{0})\epsilon^{2}+12iE_{1}^{4}\operatorname{Im}(c_{\mathrm{s}}^{*}(p)c_{\mathrm{d}}(p))\left(\epsilon^{2}-1\right)^{2}\Big\}\ c_{\mathrm{p}}(p_{0})c_{\mathrm{d}}^{*}(p_{0})e^{i\varphi}\Big],(D.26)

where the radial integration has been performed assuming that the state amplitudes are sharply peaked atp0p_{0}over a small momentum intervalΔ​p\Delta p, so that they satisfy∫0∞ci∗​(p)​cj​(p)​pn+k+2​d​p=Δ​p​ci∗​(p0)​cj​(p0)​p0n+k+2\int_{0}^{\infty}c_{\mathrm{i}}^{*}(p)c_{\mathrm{j}}(p)p^{n+k+2}\textrm{d}p=\Delta p\,c_{\mathrm{i}}^{*}(p_{0})c_{\mathrm{j}}(p_{0})p_{0}^{n+k+2}.

In our final result (D.26) we see three distinct types of dependence ofχ234\chi_{234}on the ellipticity of the fundamental,
which are proportional toϵ2−1(ϵ2+1)4​ϵ3\displaystyle\frac{\epsilon^{2}-1}{(\epsilon^{2}+1)^{4}}\epsilon^{3},ϵ​(ϵ2−1)(ϵ2+1)2\displaystyle\frac{\epsilon(\epsilon^{2}-1)}{(\epsilon^{2}+1)^{2}},
andϵ​(ϵ2−1)3(ϵ2+1)4\displaystyle\frac{\epsilon(\epsilon^{2}-1)^{3}}{(\epsilon^{2}+1)^{4}},
respectively,
and which combine in different proportions depending on the specific configuration used:
the radial structure of the atom and the envelope of the driving pulses determine the state constantsci​(p)c_{\mathrm{i}}(p)(via (D.24) and (D.13)),
and the relative amplitudesE1E_{1}andE2E_{2}of the driving fields then determine which of the ellipticity dependences dominate.

## Appendix EDetails of the TDSE simulations

We perform TDSE simulations using the code from Ref.[102]. We use a radial box of size1190.34a.u.1190.34\text{\,}\mathrm{{a.u.}}with a log-uniform grid consisting of 3000 points. The first 10 points are on a uniform grid from0.036 36a.u.0.036\,36\text{\,}\mathrm{{a.u.}}up to0.3636a.u.0.3636\text{\,}\mathrm{{a.u.}}, followed by 25 points on a logarithmic grid up to3.94a.u.3.94\text{\,}\mathrm{{a.u.}}and 2965 points on a uniform grid until the box boundary.
To avoid unphysical reflections, we use a complex absorber from[77]with width32.775a.u.32.775\text{\,}\mathrm{{a.u.}}starting at1157.94a.u.1157.94\text{\,}\mathrm{{a.u.}}We use a timestep of0.0025a.u.0.0025\text{\,}\mathrm{{a.u.}}and include angular momenta up toℓmax=30\ell_{\mathrm{max}}=30and allm∈[−ℓmax,ℓmax]m\in[-\ell_{\mathrm{max}},\ell_{\mathrm{max}}]. The photoelectron angular distributions are calculated using the iSURFC method[87].
Theω\omegaand2​ω2\omegafields with fundamental frequencyω=0.375a.u.\omega=$0.375\text{\,}\mathrm{{a.u.}}$(10.20eV10.20\text{\,}\mathrm{e}\mathrm{V}) have all the same flat-top envelopes, with 4 cycleT=2​π/ω≃16.755a.u.T=2\pi/\omega\simeq$16.755\text{\,}\mathrm{{a.u.}}$(≃405as\simeq$405\text{\,}\mathrm{a}\mathrm{s}$) longsin2\sin^{2}rise and fall and88-optical-cycle-long flat-top part.
The peak electric field amplitude of theω\omegais0.005a.u.0.005\text{\,}\mathrm{{a.u.}}(8.775×1011W/cm28.775\text{\times}{10}^{11}\text{\,}\mathrm{W}\mathrm{/}\mathrm{c}\mathrm{m}^{2}) while the2​ω2\omegafield peak amplitude isF2​ω=0.0008a.u.F_{2\omega}=$0.0008\text{\,}\mathrm{{a.u.}}$(2.25×1010W/cm22.25\text{\times}{10}^{10}\text{\,}\mathrm{W}\mathrm{/}\mathrm{c}\mathrm{m}^{2}). Theω\omegafield has an elliptical polarization in thex​yxyplane and the2​ω2\omegais linearly polarized along thez{z}axis.

## Appendix FAn apparent ‘blind spot’:Y33+Y43Y_{33}+Y_{43}

Coming back to more general distributions, we now turn to an apparent ‘blind spot’ for our formalism, as mentioned briefly in the Discussion,
which is illustrative in understanding how extensions of our tensor-cross-product formalism can be used for trickier cases.
In particular, we consider a distribution of the formρABS​(𝐫)\displaystyle\rho_{\mathrm{ABS}}(\mathbf{r})=Re[Y33(𝐫)+ei​φY43(𝐫)]f(r),\displaystyle=\operatorname{Re}\mathopen{}\left[Y_{33}(\mathbf{r})+e^{i\varphi}Y_{43}(\mathbf{r})\right]f(r),(F.1)

(wheref​(r)f(r)is a rotationally-symmetric radial amplitude) consisting of a linear superposition of octupolar and hexadecapolar terms.
This distribution, shown in Figure4(a), forms a clearly chiral helical shape, reminiscent of the triple-gaussian helix from SectionIII.3, but without any quadrupolar moment.151515As an analytically-tractable alternative, (F.1) could be replaced with combinations of the formSℓ,±3​(𝐫)​e−r2S_{\ell,\pm 3}(\mathbf{r})e^{-r^{2}}.

Since we are imposing an explicitly multipolar form, only two tensorial multipolar moments are nonzero,
namely𝝁ABS(3)=C3Re[𝐭^33]and𝝁ABS(4)=C4Re[ei​φ𝐭^43],\displaystyle\boldsymbol{\mu}^{(3)}_{\mathrm{ABS}}=C_{3}\operatorname{Re}\mathopen{}\left[\hat{\mathbf{t}}_{33}\right]\ \text{and}\ \boldsymbol{\mu}^{(4)}_{\mathrm{ABS}}=C_{4}\operatorname{Re}\mathopen{}\left[e^{i\varphi}\hat{\mathbf{t}}_{43}\right],(F.2)

in terms of the multipolar basis tensors𝐭^ℓ​m\hat{\mathbf{t}}_{\ell m}as defined in (C.26),
whereC3=32​π35​∫0∞f​(r)​r5​d​rC_{3}=\sqrt{\tfrac{32\pi}{35}}\int_{0}^{\infty}f(r)r^{5}\textrm{d}randC4=128​π315​∫0∞f​(r)​r6​d​rC_{4}=\sqrt{\tfrac{128\pi}{315}}\allowbreak{}\int_{0}^{\infty}f(r)r^{6}\textrm{d}r.
The results from sectionC.5then imply that any nonzero tensorial moments𝐌ABS(n)\mathbf{M}^{(n)}_{\mathrm{ABS}}can only be obtained from the multipolar moments from (F.2) via the tensor lift operator\trigbraces​ℒ^\trigbraces{\hat{\mathcal{L}}}.
As such it is sufficient to consider𝝁ABS(3)\boldsymbol{\mu}^{(3)}_{\mathrm{ABS}}and𝝁ABS(4)\boldsymbol{\mu}^{(4)}_{\mathrm{ABS}}.

As mentioned in the Discussion, the restriction to only two nonzero multipolar moment tensors then implies that we cannot use a chiral measure based directly on a triple tensor product:
while there are three nonzero pseudotensor-valued tensor cross products,𝝅ABS(n)\displaystyle\boldsymbol{\pi}^{(n)}_{\mathrm{ABS}}=(𝝁ABS(3)×𝝁ABS(4))(n),\displaystyle=\left(\boldsymbol{\mu}^{(3)}_{\mathrm{ABS}}\times\boldsymbol{\mu}^{(4)}_{\mathrm{ABS}}\right)^{(n)},(F.3)

forn=2n=2, 4 and 6, those cannot be contracted with either of𝝁ABS(3)\boldsymbol{\mu}^{(3)}_{\mathrm{ABS}}or𝝁ABS(4)\boldsymbol{\mu}^{(4)}_{\mathrm{ABS}}to give a nonzero result.

On their own, the cross products𝝅ABS(n)\boldsymbol{\pi}^{(n)}_{\mathrm{ABS}}themselves do provide a measure of asymmetry, in that their tensor norms𝝅ABS(n)∙𝝅ABS(n)\boldsymbol{\pi}^{(n)}_{\mathrm{ABS}}\bullet\boldsymbol{\pi}^{(n)}_{\mathrm{ABS}}can only be nonzero if the distribution is chiral.
However, those norms cannot provide a sense of handedness forρABS​(𝐫)\rho_{\mathrm{ABS}}(\mathbf{r}).

Fortunately, though, itispossible to extract a sense of handedness forρABS​(𝐫)\rho_{\mathrm{ABS}}(\mathbf{r})from the cross products𝝅ABS(n)\boldsymbol{\pi}^{(n)}_{\mathrm{ABS}}, by referencing them against each other,
using theeven-parity tensor triple product from (A.4).
This yields a pseudoscalar,χ34​(246)\displaystyle\chi_{34(246)}=(𝝅ABS(2)×𝝅ABS(4))(6)

∙𝝅ABS(6),\displaystyle=\left(\boldsymbol{\pi}^{(2)}_{\mathrm{ABS}}\times\boldsymbol{\pi}^{(4)}_{\mathrm{ABS}}\right)^{(6)}\mathbin{\mathchoice{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\displaystyle\bullet$}}}\hfil}}{\hbox to5.74991pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\textstyle\bullet$}}}\hfil}}{\hbox to5.28671pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptstyle\bullet$}}}\hfil}}{\hbox to5.1909pt{\hfil\raise 0.0pt\hbox{\scalebox{0.65}{\lower 0.0pt\hbox{$\scriptscriptstyle\bullet$}}}\hfil}}}\boldsymbol{\pi}^{(6)}_{\mathrm{ABS}},(F.4)

which can be easily computed symbolically,χ34​(246)\displaystyle\chi_{34(246)}=31280​C33​C43​sin3⁡(φ),\displaystyle=\frac{3}{1280}C_{3}^{3}C_{4}^{3}\>\sin^{3}(\varphi),(F.5)

and which provides a clear sense of handedness forρABS​(𝐫)\rho_{\mathrm{ABS}}(\mathbf{r})based on the relative phaseφ\varphibetween the octupolar and hexadecapolar components.

Structurally, this new pseudoscalar can be understood using a similar manipulation to the one used in (7), substituting in the integral form of all of the𝝁ABS(ℓ)\boldsymbol{\mu}^{(\ell)}_{\mathrm{ABS}}factors.
That reveals it as asix-point correlation function, with a pseudoscalar kernel given by an isotropic 6-point function, such as described previously for cosmological applications[26,133].

## Appendix GA full ‘blind spot’: purely-octupolar chiral distributions

Finally, we turn to the ‘cryptochiral’ distribution, mentioned in SectionV:
a complete ‘blind spot’ of our formalism, and, most likely, to other existing chirality measures.
We construct this blind-spot distribution as a purely octupolar one[48,30]– that is, one sitting purely in theℓ=3\ell=3representation;
for simplicity, we deal with a spherical distribution.
Generically, such a distribution has the formρPOBS​(𝐫)\displaystyle\rho_{\mathrm{POBS}}(\mathbf{r})=∑m=03c3,m​Y3,m​(𝐫)+c.c.,\displaystyle=\sum_{m=0}^{3}c_{3,m}Y_{3,m}(\mathbf{r})+\mathrm{c.c.},(G.1)

with complex coefficientsc3,mc_{3,m}.
For the distribution shown in Figure4(b), we use the coefficients(c3,0,c3,1,c3,2,c3,3)\displaystyle(c_{3,0},c_{3,1},c_{3,2},c_{3,3})=(−1,i4,14,1),\displaystyle=\left(-1,\frac{i}{4},\frac{1}{4},1\right),(G.2)

which can be understood as follows.

The ‘bones’ of the distribution are provided by the tetrahedral symmetry which is normally associated with the functionRe⁡(Y3,2​(𝐫))\operatorname{Re}(Y_{3,2}(\mathbf{r})), which we rotate for visual clarity to align one of the main lobes with thezzaxis;
that provides the coefficients(c3,0,c3,3)=(−1,1)(c_{3,0},c_{3,3})=(-1,1).
To make this distribution chiral, we simply need to break the symmetry between the three positive lobes at the positive-zzside, and this will happen generically from most choices of the coefficientsc3,1c_{3,1}andc3,2c_{3,2}.
For definiteness and simplicity, we show an example with(c3,1,c3,2)=14​(i,1)(c_{3,1},c_{3,2})=\frac{1}{4}(i,1).

The chirality of the distribution as shown in Figure4(b) is not immediately apparent, but it can be seen explicitly from the symmetry breaking of the lobes, all of which have different values ofρPOBS​(𝐫)\rho_{\mathrm{POBS}}(\mathbf{r});
it can also be seen in the topological structure of the constant-ρPOBS​(𝐫)\rho_{\mathrm{POBS}}(\mathbf{r})contours and how they connect the various saddle points of the distribution on the sphere.

## References
- [1]H. Altenbach(2012)Kontinuumsmechanik: einführung in die materialunabhängigen und materialabhängigen gleichungen.2 edition,Springer,Berlin.Cited by:footnote 6.
- [2]S. Alvarez, P. Alemany, and D. Avnir(2005)Continuous chirality measures in transition metal chemistry.Chem. Soc. Rev.34(4),pp. 313–326.External Links:DocumentCited by:§I.
- [3]D. L. Andrews and T. Thirunamachandran(1977)On three-dimensional rotational averages.J. Chem. Phys.67(11),pp. 5026–5033.External Links:DocumentCited by:Appendix A.
- [4]D. L. Andrews(2023)Symmetry-based identification and enumeration of independent tensor properties in nonlinear and chiral optics.J. Chem. Phys.158(3),pp. 034101.External Links:DocumentCited by:§V.
- [5]J. Applequist(1989)Traceless cartesian tensor forms for spherical harmonic functions: new theorems and applications to electrostatics of dielectric media.J. Phys. A: Math. Gen.22(20),pp. 4303.External Links:DocumentCited by:Appendix C.
- [6]J. Applequist(1984)Fundamental relationships in the theory of electric multipole moments and multipole polarizabilities in static fields.Chem. Phys.85(2),pp. 279–290.External Links:DocumentCited by:§II.
- [7]J. Applequist(2002)Maxwell–Cartesian spherical harmonics in multipole potentials and atomic orbitals.Theor. Chem. Acc.107(2),pp. 103–115.External Links:DocumentCited by:Appendix C.
- [8]D. Ayuso, O. Neufeld, A. F. Ordonez, P. Decleva, G. Lerner, O. Cohen, M. Ivanov, and O. Smirnova(2019)Synthetic chiral light for efficient control of chiral light–matter interaction.Nat. Photon.13(12),pp. 866–871.External Links:DocumentCited by:Appendix D,Appendix D,§I,§IV,§IV,§IV,§IV,§V,§V.
- [9]D. Ayuso, A. F. Ordonez, M. Ivanov, and O. Smirnova(2021)Ultrafast optical rotation in chiral molecules with ultrashort and tightly focused beams.Optica8(10),pp. 1243–1246.External Links:Document,arXiv:2011.07873,https://arxiv.org/abs/2011.07873v1Cited by:§V.
- [10]D. Ayuso, A. F. Ordonez, and O. Smirnova(2022)Ultrafast chirality: the road to efficient chiral measurements.Phys. Chem. Chem. Phys.24(44),pp. 26962–26991.External Links:DocumentCited by:§IV,§V.
- [11]J. D. Barnwell, J. G. Loeser, and D. R. Herschbach(1983)Angular correlations in chemical reactions. statistical theory for four-vector correlations.J. Phys. Chem.87(15),pp. 2781–2786.External Links:DocumentCited by:Appendix B.
- [12]S. Beaulieu, A. Ferré, R. Géneaux, R. Canonge, D. Descamps, B. Fabre, N. Fedorov, F. Légaré, S. Petit, T. Ruchon, V. Blanchet, Y. Mairesse, and B. Pons(2016)Universality of photoelectron circular dichroism in the photoionization of chiral molecules.New J. Phys.18(10),pp. 102002.External Links:DocumentCited by:§I,§IV.
- [13]J. Berakdar and N. M. Kabachnik(2004)Two-electron photoemission from polarized atoms.J. Phys. B: At. Mol. Opt. Phys.38(1),pp. 23.External Links:DocumentCited by:Appendix B.
- [14]J. Berakdar, H. Klar, A. Huetz, and P. Selles(1993)Chiral electron pairs from double photoionization.J. Phys. B: At. Mol. Opt. Phys.26(8),pp. 1463.External Links:DocumentCited by:§V.
- [15]L. Biedenharn(1960)Angular correlations in nuclear spectroscopy.InNuclear Spectroscopy,E. Ajzenberg-Selove (Ed.),pp. 732–810.Note:(Part B)Cited by:Appendix B.
- [16]D. G. Blackmond(2019)The origin of biological homochirality.Cold Spring Harbor Perspect. Biol.11(3),pp. a032540.External Links:DocumentCited by:§I.
- [17]K. Y. Bliokh and F. Nori(2011)Characterizing optical chirality.Phys. Rev. A83(2),pp. 021803.External Links:DocumentCited by:§I.
- [18]E. Bloch, S. Larroque, S. Rozen, S. Beaulieu, A. Comby, S. Beauvarlet, D. Descamps, B. Fabre, S. Petit, R. Taïeb, A. J. Uzan, V. Blanchet, N. Dudovich, B. Pons, and Y. Mairesse(2021-12)Revealing the influence of molecular chirality on tunnel-ionization dynamics.Phys. Rev. X11(4),pp. 041056.External Links:DocumentCited by:§IV.
- [19]J. Bonet, A. J. Gil, and R. Ortigosa(2015)A computational framework for polyconvex large strain elasticity.Comput. Methods Appl. Mech. Eng.283,pp. 1061–1094.External Links:DocumentCited by:footnote 6.
- [20]O. Borisenko and V. Kushnir(2006)2D SU(2) principal chiral model: dual representation in the classical limit and low-temperature asymptotics of correlation functions.Ukr. J. Phys.51(1),pp. 90–99.External Links:LinkCited by:Appendix B.
- [21]A. B. Buda, T. A. d. Heyde, and K. Mislow(1992)On quantifying chirality.Angew. Chem., Int. Ed. Engl.31(8),pp. 989–1007.External Links:DocumentCited by:§I.
- [22]A. B. Buda and K. Mislow(1992)A Hausdorff chirality measure.J. Am. Chem. Soc.114(15),pp. 6006–6012.External Links:DocumentCited by:§I.
- [23]J. Byun and E. Krause(2023)Modal compression of the redshift-space galaxy bispectrum.Mon. Not. R. Astron. Soc.525(4),pp. 4854–4870.External Links:DocumentCited by:Appendix B.
- [24]R. S. Cahn, C. K. Ingold, and V. Prelog(1956)The specification of asymmetric configuration in organic chemistry.Experientia12(3),pp. 81–94.External Links:DocumentCited by:§I.
- [25]R. N. Cahn, Z. Slepian, and J. Hou(2023)Test for cosmological parity violation using the 3D distribution of galaxies.Phys. Rev. Lett.130(20),pp. 201002.External Links:Document,https://arxiv.org/abs/2110.12004,arXiv:2110.12004Cited by:Appendix B,§I,§II.
- [26]R. N. Cahn and Z. Slepian(2023)Isotropic N-point basis functions and their properties.J. Phys. A: Math. Theor.56(32),pp. 325204.External Links:Document,https://arxiv.org/abs/2010.14418,arXiv:2010.14418Cited by:Appendix F,§I,§II.
- [27]R. P. Cameron, J. B. Götte, S. M. Barnett, and A. M. Yao(2017)Chirality and the angular momentum of light.Phil. Trans. Roy. Soc. A: Math. Phys. Eng. Sci.375(2087),pp. 20150433.External Links:DocumentCited by:§I.
- [28]Cited by:§III.2.
- [29]R. P. Cameron, D. McArthur, and A. M. Yao(2023)Strong chiral optical force for small chiral molecules based on electric-dipole interactions, inspired by the asymmetrical hydrozoan velella velella.New J. Phys.25(8),pp. 083006.External Links:Document,https://arxiv.org/abs/2412.13206,arXiv:2412.13206Cited by:§III.2.
- [30]Y. Chen, L. Qi, and E. G. Virga(2017)Octupolar tensors for liquid crystals.J. Phys. A: Math. Theor.51(2),pp. 025206.External Links:DocumentCited by:Appendix G.
- [31]J. P. Coles and R. Bieri(2020)An optimizing symbolic algebra approach for generating fast multipole method operators.Comput. Phys. Commun.251,pp. 107081.External Links:DocumentCited by:Appendix C.
- [32]J. T. Collins, K. R. Rusimova, D. C. Hooper, H.-H. Jeong, L. Ohnoutek, F. Pradaux-Caggiano, T. Verbiest, D. R. Carbery, P. Fischer, and V. K. Valev(2019)First observation of optical activity in hyper-Rayleigh scattering.Phys. Rev. X9(1),pp. 011024.External Links:DocumentCited by:§V.
- [33]A. Comby, E. Bloch, C. M. M. Bond, D. Descamps, J. Miles, S. Petit, S. Rozen, J. B. Greenwood, V. Blanchet, and Y. Mairesse(2018)Real-time determination of enantiomeric and isomeric content using photoelectron elliptical dichroism.Nat. Commun.9(5212),pp. 5212.External Links:DocumentCited by:§I,§IV,§IV.
- [34]E. U. Condon(1937)Theories of optical rotatory power.Rev. Mod. Phys.9(4),pp. 432.External Links:DocumentCited by:§I,§IV,§V.
- [35]F. Crimin, N. Mackinnon, J. B. Götte, and S. M. Barnett(2019)Optical helicity and chirality: conservation and sources.Appl. Sci.9(5),pp. 828.External Links:DocumentCited by:§I.
- [36]F. Da Pieve, S. Fritzsche, G. Stefani, and N. M. Kabachnik(2007)Linear magnetic and alignment dichroism in Auger–photoelectron coincidence spectroscopy.J. Phys. B: At. Mol. Opt. Phys.40(2),pp. 329.External Links:DocumentCited by:Appendix B.
- [37]R. de Boer(1982)Vektor- und tensorrechnung für ingenieure.Springer-Verlag.Cited by:footnote 6.
- [38]C. Dryzun and D. Avnir(2011)Chirality measures for vectors, matrices, operators and functions.ChemPhysChem12(1),pp. 197–205.External Links:DocumentCited by:§I,§V.
- [39]A. C. Evans, C. Meinert, C. Giri, F. Goesmann, and U. J. Meierhenrich(2012)Chirality, photochemistry and the detection of amino acids in interstellar ice analogues and comets.Chem. Soc. Rev.41(16),pp. 5447–5458.External Links:DocumentCited by:§I.
- [40]U. Fano and G. Racah(1959)Irreducible tensorial sets.Pure and Applied Physics,Academic Press.Cited by:Appendix B.
- [41]G. H. Fecher, J. Kübler, and C. Felser(2022)Chirality in the solid state: chiral crystal structures in chiral and achiral space groups.Materials15(17),pp. 5812.External Links:DocumentCited by:§I.
- [42]Cited by:§I,§IV,§IV.
- [43]K. Fehre, N. M. Novikovskiy, S. Grundmann, G. Kastirke, S. Eckart, F. Trinter, J. Rist, A. Hartung, D. Trabert, C. Janke, G. Nalin, M. Pitzer, S. Zeller, F. Wiegandt, M. Weller, M. Kircher, M. Hofmann, L. Ph. H. Schmidt, A. Knie, A. Hans, L. B. Ltaief, A. Ehresmann, R. Berger, H. Fukuzawa, K. Ueda, H. Schmidt-Böcking, J. B. Williams, T. Jahnke, R. Dörner, M. S. Schöffler, and Ph. V. Demekhin(2021-09)Fourfold differential photoelectron circular dichroism.Phys. Rev. Lett.127,pp. 103201.External Links:Document,LinkCited by:§IV.
- [44]I. Fernandez-Corbaton, M. Fruhnert, and C. Rockstuhl(2016)Objects of maximum electromagnetic chirality.Phys. Rev. X6(3),pp. 031013.External Links:DocumentCited by:§I.
- [45]V. V. Flambaum and H. Feldmeier(2020)Enhanced nuclear Schiff moment in stable and metastable nuclei.Phys. Rev. C101(1),pp. 015502.External Links:DocumentCited by:§C.1,footnote 3.
- [46]P. W. Fowler(2005)Quantification of chirality: attempting the impossible.Symmetry: Culture and Science16(4),pp. 321–334.Cited by:§I,§I,§V.
- [47]N. Fujii and T. Saito(2004)Homochirality and life.Chem. Rec.4(5),pp. 267–278.External Links:DocumentCited by:§I.
- [48]G. Gaeta and E. G. Virga(2023)A review on octupolar tensors.J. Phys. A: Math. Theor.56(36),pp. 363001.External Links:DocumentCited by:Appendix G.
- [49]C. Gautier and T. Bürgi(2009)Chiral gold nanoparticles.ChemPhysChem10(3),pp. 483–492.External Links:DocumentCited by:§I.
- [50]P. G. D. Gennes and J. Prost(1993)The physics of liquid crystals.Oxford University Press,Oxford.Cited by:§I.
- [51]A. Geyer, J. Stindl, I. Dwojak, M. Hofmann, N. Anders, P. Roth, P. Daum, J. Kruse, S. Jacob, S. Gurevich, N. Wong, M. S. Schöffler, L. Ph. H. Schmidt, T. Jahnke, M. Kunitski, R. Dörner, and S. Eckart(2025)Chiral electron momentum distribution upon strong-field ionization of atoms.Phys. Rev. Res.7(3),pp. L032061.External Links:DocumentCited by:§I,§IV,§IV.
- [52]G. Gilat(1989)Chiral coefficient-a measure of the amount of structural chirality.J. Phys. A: Math. Gen.22(13),pp. L545.External Links:DocumentCited by:§I.
- [53]D. Habibović, K. R. Hamilton, O. Neufeld, and L. Rego(2024)Emerging tailored light sources for studying chirality and symmetry.Nat. Rev. Phys.6,pp. 663–675.External Links:DocumentCited by:§IV.
- [54]B. Hall(2004)Lie groups, lie algebras, and representations: an elementary introduction.Springer.Cited by:§C.1,§C.2,§C.4,§II.
- [55]M. Han, J. Ji, A. Blech, R. E. Goetz, C. Allison, L. Greenman, C. P. Koch, and H. J. Wörner(2025)Attosecond control and measurement of chiral photoionization dynamics.Nature645,pp. 95–100.External Links:DocumentCited by:§I.
- [56]A. B. Harris, R. D. Kamien, and T. C. Lubensky(1999)Molecular chirality and chiral parameters.Rev. Mod. Phys.71(5),pp. 1745.External Links:Document,https://arXiv.org/abs/cond-mat/9901174,cond-mat/9901174Cited by:§I,§I,§II,§III.3,§V.
- [57]J. Hattne and V. S. Lamzin(2011)A moment invariant for evaluating the chirality of three-dimensional objects.J. R. Soc. Interface8(54),pp. 144–151.External Links:DocumentCited by:§I,§II,§V.
- [58]S. Hayami, M. Yatsushiro, Y. Yanagi, and H. Kusunose(2018)Classification of atomic-scale multipoles under crystallographic point groups and application to linear response tensors.Phys. Rev. B98(16),pp. 165110.External Links:DocumentCited by:§V.
- [59]M. W. Heger and D. M. Reich(2025)Tracking chirality in photoelectron circular dichroism.Phys. Rev. Res.7(1),pp. L012047.External Links:DocumentCited by:§I,§IV.
- [60]M. Hentschel, M. Schäferling, X. Duan, H. Giessen, and N. Liu(2017)Chiral plasmonics.Sci. Adv.3(5).External Links:DocumentCited by:§I.
- [61]I. I. Ippolitov and S. V. Katyurin(1985)Coordinate representation of the McWeeny-Coulson wave function for the helium atom.Sov. Phys. J.28(8),pp. 637–641.External Links:DocumentCited by:Appendix B.
- [62]H. Jeffreys(1973)On isotropic tensors.Math. Proc. Cambridge Philos. Soc.73(1),pp. 173–176.External Links:DocumentCited by:Appendix A.
- [63]J. Jerphagnon, D. Chemla, and R. Bonneville(1978)The description of the physical properties of condensed matter using irreducible tensors.Adv. Phys.27(4),pp. 609–650.External Links:DocumentCited by:§C.1.
- [64]R. R. Jones, C. Miksch, H. Kwon, C. Pothoven, K. R. Rusimova, M. Kamp, K. Gong, L. Zhang, T. Batten, B. Smith, A. V. Silhanek, P. Fischer, D. Wolverson, and V. K. Valev(2023)Dense arrays of nanohelices: raman scattering from achiral molecules reveals the near-field enhancements at chiral metasurfaces.Adv. Mater.35(34),pp. 2209282.External Links:DocumentCited by:§I.
- [65]N. Joshi, S. Jhingan, T. Souradeep, and A. Hajian(2010)Bipolar harmonic encoding of CMB correlation patterns.Phys. Rev. D81(8),pp. 083012.External Links:DocumentCited by:Appendix B.
- [66]G. P. Katsoulis, Z. Dube, P. B. Corkum, A. Staudte, and A. Emmanouilidou(2022)Momentum scalar triple product as a measure of chirality in electron ionization dynamics of strongly driven atoms.Phys. Rev. A106(4),pp. 043109.External Links:DocumentCited by:§I,§IV,§IV.
- [67]W. T. Kelvin(1894)The molecular tactics of a crystal.Clarendon Press,Oxford.Note:ark:/13960/t7qn64054Cited by:§I,§IV.
- [68]M. Khokhlova, E. Pisanty, S. Patchkovskii, O. Smirnova, and M. Ivanov(2022)Enantiosensitive steering of free-induction decay.Sci. Adv.8(24),pp. eabq1962.External Links:DocumentCited by:§V.
- [69]Cited by:§I,§IV.
- [70]C. Lux, M. Wollenhaupt, T. Bolze, Q. Liang, J. Köhler, C. Sarpe, and T. Baumert(2012)Circular dichroism in the photoelectron angular distributions of camphor and fenchone from multiphoton ionization with femtosecond laser pulses.Angew. Chem. Int. Ed.51(20),pp. 5001–5005.External Links:DocumentCited by:§I,§IV,§IV,§V.
- [71]C. Lux, M. Wollenhaupt, C. Sarpe, and T. Baumert(2015)Photoelectron circular dichroism of bicyclic ketones from multiphoton ionization with femtosecond laser pulses.ChemPhysChem16(1),pp. 115–137.External Links:DocumentCited by:§I,§IV,§V.
- [72]A. W. Malcherek and J. S. Briggs(1997)The n-electron Coulomb continuum.J. Phys. B: At. Mol. Opt. Phys.30(20),pp. 4419.External Links:DocumentCited by:Appendix B.
- [73]N. L. Manakov, S. I. Marmo, and A. V. Meremianin(1996)A new technique in the theory of angular distributions in atomic processes: the angular distribution of photoelectrons in single and double photoionization.J. Phys. B: At. Mol. Opt. Phys.29(13),pp. 2711.External Links:DocumentCited by:Appendix B.
- [74]N. L. Manakov, A. V. Meremianin, and A. F. Starace(1998)Invariant representations of finite rotation matrices and some applications.Phys. Rev. A57(5),pp. 3233–3244.External Links:DocumentCited by:Appendix B.
- [75]N. L. Manakov, A. V. Meremianin, and A. F. Starace(2002)Multipole expansions of irreducible tensor sets and some applications.J. Phys. B: At. Mol. Opt. Phys.35(1),pp. 77.External Links:DocumentCited by:Appendix B.
- [76]S. R. Mane(2016)Irreducible Cartesian tensors of highest weight, for arbitrary order.Nucl. Instrum. Methods Phys. Res., Sect. A813,pp. 62–67.External Links:DocumentCited by:§C.1.
- [77]D. E. Manolopoulos(2002)Derivation and reflection properties of a transmission-free absorbing potential.J. Chem. Phys.117(21),pp. 9552–9559.External Links:DocumentCited by:Appendix E.
- [78]N. Mayer, D. Ayuso, P. Decleva, M. Khokhlova, E. Pisanty, M. Ivanov, and O. Smirnova(2024)Chiral topological light for detection of robust enantiosensitive observables.Nat. Photonics18,pp. 1155–1160.External Links:DocumentCited by:§V.
- [79]N. Mayer, S. Patchkovskii, F. Morales, M. Ivanov, and O. Smirnova(2022)Imprinting chirality on atoms using synthetic chiral light fields.Phys. Rev. Lett.129,pp. 243201.External Links:Document,LinkCited by:§I,§IV,§IV,§IV,§V.
- [80]D. McArthur, E. I. Alexakis, A. R. Puente, R. McGonigle, A. J. Love, P. L. Polavarapu, L. D. Barron, L. E. MacKenzie, A. S. Arnold, and R. P. Cameron(2025)Observation of Rayleigh optical activity for chiral molecules: a new chiroptical tool.J. Phys. Chem. A129(51),pp. 11884–11887.External Links:DocumentCited by:§V.
- [81]G. M. McClelland and D. R. Herschbach(1979)Symmetry properties of angular correlations for molecular collision complexes.J. Phys. Chem.83(11),pp. 1445–1454.External Links:DocumentCited by:Appendix B.
- [82]R. B. Meyer, L. Liebert, L. Strzelecki, and P. Keller(1975)Ferroelectric liquid crystals.J. Physique Lett.36(3),pp. 69–71.External Links:DocumentCited by:§I.
- [83]A. Mildner, A. Horrer, P. Weiss, S. Dickreuter, P. C. Simo, D. Gérard, D. P. Kern, and M. Fleischer(2023)Decoding polarization in a single achiral gold nanostructure from emitted far-field radiation.ACS Nano17(24),pp. 25656–25666.External Links:DocumentCited by:§I.
- [84]G. Millar, N. Weinberg, and K. Mislow(2005)On the Osipov–Pickup–Dunmur chirality index: why pseudoscalar functions are generally unsuitable to quantify chirality.Mol. Phys.103(20),pp. 2769–2772.External Links:DocumentCited by:§I.
- [85]K. Mislow and P. Bickart(1976)An epistemological note on chirality.Isr. J. Chem.15(1-2),pp. 1–6.External Links:DocumentCited by:§V.
- [86]K. Mislow and P. Poggi-Corradini(1993)Shape space of achiral simplexes.J. Math. Chem.13(1),pp. 209–211.External Links:DocumentCited by:§I.
- [87]F. Morales, T. Bredtmann, and S. Patchkovskii(2016)iSURF: a family of infinite-time surface flux methods.J Phys B: At. Mol. Opt. Phys.49(24),pp. 245001.External Links:DocumentCited by:Appendix E.
- [88]Mustard(2024)Could this change air travel forever?.Note:[Online; accessed 30 June 2025],youtu.be/C_dNt4UEVZQCited by:§III.2.
- [89]L. Nahon, G. A. Garcia, and I. Powis(2015)Valence shell one-photon photoelectron circular dichroism in chiral systems.J. Electron Spectrosc. Relat. Phenom.204,pp. 322–334.External Links:DocumentCited by:§I,§IV,§V.
- [90]M. P. Neal, M. Solymosi, M. R. Wilson, and D. J. Earl(2003)Helical twisting power and scaled chiral indices.J. Chem. Phys.119(6),pp. 3567–3573.External Links:DocumentCited by:§I,§II,§V.
- [91]O. Neufeld, M. E. Tzur, and O. Cohen(2020)Degree of chirality of electromagnetic fields and maximally chiral light.Phys. Rev. A101(5),pp. 053831.External Links:DocumentCited by:§I,§I.
- [92]Cited by:§IV.
- [93]A. F. Ordonez, D. Ayuso, P. Decleva, and O. Smirnova(2023)Geometric magnetism and anomalous enantio-sensitive observables in photoionization of chiral molecules.Commun. Phys.6(257),pp. 257.External Links:DocumentCited by:§V.
- [94]A. F. Ordonez and O. Smirnova(2018)Generalized perspective on chiral measurements without magnetic interactions.Phys. Rev. A98(6),pp. 063428.External Links:DocumentCited by:§V,§V.
- [95]A. F. Ordonez and O. Smirnova(2019)Propensity rules in photoelectron circular dichroism in chiral molecules. I. chiral hydrogen.Phys. Rev. A99(4),pp. 043416.External Links:DocumentCited by:§V.
- [96]A. F. Ordonez and O. Smirnova(2019)Propensity rules in photoelectron circular dichroism in chiral molecules. II. general picture.Phys. Rev. A99(4),pp. 043417.External Links:DocumentCited by:§V.
- [97]Cited by:§V.
- [98]M. A. Osipov, B. Pickup, and D. Dunmur(1995)A new twist to molecular chirality: intrinsic chirality indices.Mol. Phys.84(6),pp. 1193–1206.External Links:DocumentCited by:§I,§II,§V.
- [99]A. Papakostas, A. Potts, D. M. Bagnall, S. L. Prosvirnin, H. J. Coles, and N. I. Zheludev(2003)Optical manifestations of planar chirality.Phys. Rev. Lett.90(10),pp. 107404.External Links:DocumentCited by:§II.
- [100]V. Parchaňský, J. Kapitán, and P. Bouř(2014)Inspecting chiral molecules by Raman optical activity spectroscopy.RSC Adv.4(100),pp. 57125–57136.External Links:DocumentCited by:§V.
- [101]L. Pasteur(1905)Researches on the molecular asymmetry of natural organic products.Alembic Club,Edinburgh.Note:ark:/13960/t77t0rb8m. Translated fromRecherches sur la dissymétrie moléculaire des produits organiques naturels(1861)Cited by:§IV.
- [102]S. Patchkovskii and H.G. Muller(2016)Simple, accurate, and efficient implementation of 1-electron atomic time-dependent Schrödinger equation in spherical coordinates.Comput. Phys. Commun.199,pp. 153–169.External Links:Document,LinkCited by:Appendix E.
- [103]M. Petitjean(2003)Chirality and symmetry measures: a transdisciplinary review.Entropy5(3),pp. 271–312.External Links:DocumentCited by:§I.
- [104]A. Pier, K. Fehre, S. Grundmann, I. Vela-Perez, N. Strenger, M. Kircher, D. Tsitsonis, J. B. Williams, A. Senftleben, T. Baumert, M. S. Schöffler, P. V. Demekhin, F. Trinter, T. Jahnke, and R. Dörner(2020)Chiral photoelectron angular distributions from ionization of achiral atomic and molecular species.Phys. Rev. Res.2(3),pp. 033209.External Links:DocumentCited by:§V.
- [105]E. Pisanty and M. Khokhlova(2026)Chimera: chiral measures research assistant.GitHub.Note:github.com/atto-King-s/Chimera,doi:10.5281/zenodo.18684467Cited by:Appendix A,§I,§IV,§V.
- [106]E. Pisanty and M. Khokhlova(2026)Figure-making code and data for ‘Chiral moments make chiral measures’.Note:Zenodo:3692563,doi:10.1088/1751-8121/acdfc4Cited by:Appendix D,§I.
- [107]E. Pisanty, G. J. Machado, V. Vicuña-Hernández, A. Picón, A. Celi, J. P. Torres, and M. Lewenstein(2019)Knotting fractional-order knots with the polarization state of light.Nature Photon.13(8),pp. 569–574.External Links:Document,https://arxiv.org/abs/1808.05193,arXiv:1808.05193Cited by:§V.
- [108]A. Potts, D. M. Bagnall, and N. I. Zheludev(2003)A new model of geometric chirality for two-dimensional continuous media and planarmeta-materials.J. Opt. A: Pure Appl. Opt.6(2),pp. 193.External Links:DocumentCited by:§II.
- [109]I. Powis(1992)Photoelectron anisotropy: what may be learned from photoelectron—photofragment ion correlations.Chem. Phys. Lett.189(4),pp. 473–478.External Links:DocumentCited by:§I,§IV,§V.
- [110]I. Powis(2008)Photoelectron circular dichroism in chiral molecules.InAdvances in Chemical Physics,pp. 267–329.External Links:https://onlinelibrary.wiley.com/doi/pdf/10.1002/9780470259474.ch5Cited by:§IV,§V.
- [111]R. E. Raab and O. L. de Lange(2005)Multipole theory in electromagnetism: classical, quantum, and symmetry aspects, with applications.Clarendon Press,Oxford.Note:ark:/13960/s24hj1nzkpvCited by:§II.
- [112]D. Rajak, S. Beauvarlet, O. Kneller, A. Comby, R. Cireasa, D. Descamps, B. Fabre, J. D. Gorfinkiel, J. Higuet, S. Petit, S. Rozen, H. Ruf, N. Thiré, V. Blanchet, N. Dudovich, B. Pons, and Y. Mairesse(2024)Laser-induced electron diffraction in chiral molecules.Phys. Rev. X14(1),pp. 011015.External Links:DocumentCited by:§I,§IV,§IV.
- [113]A. Rassat and P. W. Fowler(2004)Is there a “most chiral tetrahedron”?.Chem. Eur. J.10(24),pp. 6575–6580.External Links:DocumentCited by:§I.
- [114]Z. X. Ren, P. W. Zhao, and J. Meng(2022)Dynamics of rotation in chiral nuclei.Phys. Rev. C105(1),pp. L011301.External Links:DocumentCited by:§I.
- [115]A. Roos, P. M. Maier, A. F. Ordonez, and O. Smirnova(2026)Geometry of chiral temporal structures. II. the formalism.Phys. Rev. A113(1),pp. 013111.External Links:DocumentCited by:§V.
- [116]E. Ruch(1972)Algebraic aspects of the chirality phenomenon in chemistry.Acc. Chem. Res.5(2),pp. 49–56.External Links:DocumentCited by:§I.
- [117]L. I. Schiff(1963)Measurability of nuclear electric dipole moments.Phys. Rev.132(5),pp. 2194–2200.External Links:DocumentCited by:§C.1,footnote 3.
- [118]S. A. Schulz, Rupert. F. Oulton, M. Kenney, A. Alù, I. Staude, A. Bashiri, Z. Fedorova, R. Kolkowski, A. F. Koenderink, X. Xiao, J. Yang, W. J. Peveler, A. W. Clark, G. Perrakis, A. C. Tasolamprou, M. Kafesaki, A. Zaleska, W. Dickson, D. Richards, A. Zayats, H. Ren, Y. Kivshar, S. Maier, X. Chen, M. A. Ansari, Y. Gan, A. Alexeev, T. F. Krauss, A. Di Falco, S. D. Gennaro, T. Santiago-Cruz, I. Brener, M. V. Chekhova, R. Ma, V. V. Vogler-Neuling, H. C. Weigand, Ü. Talts, I. Occhiodori, R. Grange, M. Rahmani, L. Xu, S. M. Kamali, E. Arababi, A. Faraon, A. C. Harwood, S. Vezzoli, R. Sapienza, P. Lalanne, A. Dmitriev, C. Rockstuhl, A. Sprafke, K. Vynck, J. Upham, M. Z. Alam, I. De Leon, R. W. Boyd, W. J. Padilla, J. M. Malof, A. Jana, Z. Yang, R. Colom, Q. Song, P. Genevet, K. Achouri, A. B. Evlyukhin, U. Lemmer, and I. Fernandez-Corbaton(2024)Roadmap on photonic metasurfaces.Appl. Phys. Lett.124(26).External Links:DocumentCited by:§I.
- [119]B. Shanker and H. Huang(2007)Accelerated Cartesian expansions – a fast method for computing of potentials of the formR−νR^{-\nu}for all realν\nu.J. Comput. Phys.226(1),pp. 732–753.External Links:DocumentCited by:Appendix C.
- [120]M. Shiraishi, T. Okumura, and K. Akitsu(2021)Minimum variance estimation of statistical anisotropy via galaxy survey.J. Cosmol. Astropart. Phys.2021(03),pp. 039.External Links:DocumentCited by:Appendix B.
- [121]M. Shiraishi, N. S. Sugiyama, and T. Okumura(2017)Polypolar spherical harmonic decomposition of galaxy correlators in redshift space: toward testing cosmic rotational symmetry.Phys. Rev. D95(6),pp. 063508.External Links:DocumentCited by:Appendix B.
- [122]D. J. Siminovitch(2008)Angular momentum coupling in NMR: a new view of rotation matrix products via Racah algebra.Mol. Phys.106(21–23),pp. 2607–2625.External Links:DocumentCited by:Appendix B.
- [123]O. Smirnova(2022)Ultrafast chiral dynamics and geometric fields in chiral molecules.InChiral Matter,pp. 175–194.External Links:DocumentCited by:§V.
- [124]C. Sparling, S. W. Crane, L. Ireland, R. Anderson, O. Ghafur, J. B. Greenwood, and D. Townsend(2023)Velocity-map imaging of photoelectron circular dichroism in non-volatile molecules using a laser-based desorption source.Phys. Chem. Chem. Phys.25(8),pp. 6009–6015.External Links:DocumentCited by:§I,§IV.
- [125]C. Sparling, D. Rajak, V. Blanchet, Y. Mairesse, and D. Townsend(2024)Fourier–hankel–abel nyquist-limited tomography: a spherical harmonic basis function approach to tomographic velocity-map image reconstruction.Rev. Sci. Instrum.95(5).External Links:DocumentCited by:§I,§IV,§V.
- [126]C. Sparling and D. Townsend(2022)Tomographic reconstruction techniques optimized for velocity-map imaging applications.J. Chem. Phys.157(11).External Links:DocumentCited by:§I,§IV,§V.
- [127]C. Sparling and D. Townsend(2025)Two decades of imaging photoelectron circular dichroism: from first principles to future perspectives.Phys. Chem. Chem. Phys.27(6),pp. 2888–2907.External Links:DocumentCited by:§I,§IV,§IV,§V.
- [128]L. Szabó(2016)A note on cross product between two symmetric second-order tensors.J. Mech. Mater. Struct.12(2),pp. 147–158.External Links:DocumentCited by:footnote 6.
- [129]I. Szapudi(2004)Wide-angle redshift distortions revisited.Astrophys. J.614(1),pp. 51.External Links:DocumentCited by:Appendix B.
- [130]Y. Tang and A. E. Cohen(2010)Optical chirality and its interaction with matter.Phys. Rev. Lett.104(16),pp. 163901.External Links:DocumentCited by:§I.
- [131]M. Tia, M. Pitzer, G. Kastirke, J. Gatzke, H. Kim, F. Trinter, J. Rist, A. Hartung, D. Trabert, J. Siebert, K. Henrichs, J. Becht, S. Zeller, H. Gassert, F. Wiegandt, R. Wallauer, A. Kuhlins, C. Schober, T. Bauer, N. Wechselberger, P. Burzynski, J. Neff, M. Weller, D. Metz, M. Kircher, M. Waitz, J. B. Williams, L. Ph. H. Schmidt, A. D. Müller, A. Knie, A. Hans, L. Ben Ltaief, A. Ehresmann, R. Berger, H. Fukuzawa, K. Ueda, H. Schmidt-Böcking, R. Dörner, T. Jahnke, P. V. Demekhin, and M. Schöffler(2017)Observation of enhanced chiral asymmetries in the inner-shell photoionization of uniaxially oriented methyloxirane enantiomers.J. Phys. Chem. Lett.8(13),pp. 2780–2786.External Links:DocumentCited by:§IV.
- [132]D. S. Tikhonov, A. Blech, M. Leibscher, L. Greenman, M. Schnell, and C. P. Koch(2022)Pump-probe spectroscopy of chiral vibrational dynamics.Sci. Adv.8(49).External Links:DocumentCited by:§I,§IV.
- [133]D.A. Varshalovich, A.N. Moskalev, and V.K. Khersonskii(1988)Quantum theory of angular momentum.World Scientific,Singapore.Note:handle:20.500.12657/50493Cited by:Appendix B,§C.4,Appendix D,Appendix F,§II.
- [134]D. Vestler, I. Shishkin, E. A. Gurvitz, M. E. Nasir, A. Ben-Moshe, A. P. Slobozhanyuk, A. V. Krasavin, T. Levi-Belenkova, A. S. Shalin, P. Ginzburg, G. Markovich, and A. V. Zayats(2018)Circular dichroism enhancement in plasmonic nanorod metamaterials.Opt. Express26(14),pp. 17841–17848.External Links:DocumentCited by:§I.
- [135]J. Viefhaus, L. Avaldi, G. Snell, M. Wiedenhöft, R. Hentges, A. Rüdel, F. Schäfers, D. Menke, U. Heinzmann, A. Engelns, J. Berakdar, H. Klar, and U. Becker(1996)Experimental evidence for circular dichroism in the double photoionization of helium.Phys. Rev. Lett.77(19),pp. 3975–3978.External Links:DocumentCited by:§V.
- [136]D. M. Walba(1991)A topological hierarchy of molecular chirality and other tidbits in topological stereochemistry.InNew Developments in Molecular Chirality,pp. 119–129.External Links:DocumentCited by:§I,§V.
- [137]N. Weinberg and K. Mislow(1993)Distance functions as generators of chirality measures.J. Math. Chem.14(1),pp. 427–450.External Links:DocumentCited by:§I.
- [138]N. Weinberg and K. Mislow(2000)On chirality measures and chirality properties.Can. J. Chem.78(1),pp. 41.External Links:DocumentCited by:§I,§V.
- [139]Y. Xie, A. V. Krasavin, D. J. Roth, and A. V. Zayats(2025)Unidirectional chiral scattering from single enantiomeric plasmonic nanoparticles.Nat. Commun.16(1125),pp. 1125.External Links:DocumentCited by:§I.
- [140]Y. Xie, A. V. Krasavin, and A. V. Zayats(2025)Meso-chiral optical properties of plasmonic nanoparticles: uncovering hidden chirality.Nanophotonics14(25),pp. 4479–4485.External Links:DocumentCited by:§I.
- [141]C. N. Yang(1958)Law of parity conservation and other symmetry laws.Science127(3298),pp. 565–569.External Links:DocumentCited by:§I.
- [142]H. Zabrodsky and D. Avnir(1995)Continuous symmetry measures. 4. chirality.J. Am. Chem. Soc.117(1),pp. 462–473.External Links:DocumentCited by:§I.
- [143]A. Zangwill(2013)Modern electrodynamics.Cambridge University Press,Cambridge.Cited by:§II.
- [144]W.-N. Zou, Q.-S. Zheng, D.-X. Du, and J. Rychlewski(2001)Orthogonal irreducible decompositions of tensors of high orders.Math. Mech. Solids6(3),pp. 249–267.External Links:DocumentCited by:§C.1.

## 


- 


Major funding support from
