# Exponential Capacity in Multilayer Hetero-Associative Neural Networks

**arXiv ID**: 2607.29554v1
**Authors**: Elena Agliari, Adriano Barra, Andrea Ladiana, Andrea Lepre
**Published**: 2026-07-31
**Categories**: cond-mat.dis-nn, stat.ML
**HTML URL**: https://arxiv.org/html/2607.29554v1

## Abstract

Exponential Hopfield networks store a number of patterns that grows exponentially with the number of neurons, and in their classical formulation they are auto-associative: they complete a corrupted copy of a memory into the memory itself. Many of the tasks one wants such a network to perform are instead hetero-associative, mapping a cue to a different target. We introduce and analyse an exponential neural network of $L$ layers of $N$ binary neurons, each layer carrying its own dataset, whose energy is an exponential of the product of the per-layer Mattis overlaps, so that it is minimised precisely when every layer retrieves the pattern of the same index; the stored association must be a surjective function of the cue, and we show why nothing else can be stored at all. A cavity/signal-to-noise analysis, made exact at leading order by a large-deviation evaluation of the noise, shows that the aligned hetero-associative state is a fixed point of the zero-temperature dynamics up to a number of stored patterns $P_c\sim e^{Nρ_L}$, exponential in the layer size, with an explicit rate $ρ_L$ that grows like $L\log 2$; enlarging the basins of attraction lowers the rate but never destroys its exponential character. Comparing the theory with structured data we find that the exponential capacity and the predicted basins survive correlated, many-to-one patterns: the network is a near-perfect content-addressable memory. The same closed forms describe, without refitting, a synthetic manifold, real T-cell-receptor/epitope triples and natural-language intent data, so the mechanism is domain-universal. Generalisation to unseen cues, though significantly above chance, stays below memorisation, and it is the geometry of the encoding, rather than the data domain, that sets how far above chance it reaches. In this family, exponential storage and strong generalisation are distinct capabilities.

## Full Text

Exponential Capacity in Multilayer Hetero-Associative Neural Networks

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
- License: CC BY 4.0arXiv:2607.29554v1 [cond-mat.dis-nn] 31 Jul 2026

## Exponential Capacity in Multilayer Hetero-Associative Neural NetworksElena AgliariAdriano BarraAndrea Ladianaandrea.ladiana@uniroma1.itAndrea Lepre

## Abstract

Exponential Hopfield networks store a number of patterns that grows
exponentially with the number of neurons, and in their classical formulation they are auto-associative: they
complete a corrupted copy of a memory into the memory itself. Many of the tasks
one wants such a network to perform are instead hetero-associative, mapping a
cue to a different target. We introduce and analyse an exponential neural
network ofLLlayers ofNNbinary neurons, each layer carrying its own
dataset, whose energy is an exponential of the product of the per-layer Mattis
overlaps, so that it is minimised precisely when every layer retrieves the
pattern of the same index; the stored association must be a surjective function
of the cue, and we show why nothing else can be stored at all. A
cavity/signal-to-noise analysis, made exact at
leading order by a large-deviation evaluation of the noise, shows that the
aligned hetero-associative state is a fixed point of the zero-temperature
dynamics up to a number of stored patternsPc∼eN​ρLP_{c}\sim e^{N\rho_{L}}, exponential in
the layer size, with an explicit rateρL\rho_{L}that grows likeL​log⁡2L\log 2;
enlarging the basins of attraction lowers the rate but never destroys its
exponential character. Comparing the theory with structured data
we
find that the exponential capacity and the predicted basins survive correlated,
many-to-one patterns: the network is a near-perfect content-addressable memory.
The same closed forms describe, without refitting, a synthetic manifold, real
T-cell-receptor/epitope triples and natural-language intent data, so the
mechanism is domain-universal. Generalisation to unseen cues, though
significantly above chance, stays below memorisation, and it is the geometry of
the encoding, rather than the data domain, that sets how far above chance it
reaches. In this family, exponential storage and strong generalisation are
distinct capabilities.

## keywords:associative memory , Hopfield networks , exponential storage capacity , hetero-association , statistical mechanics , large deviations††journal:Neural Networks\affiliation

[mat]organization=Dipartimento di Matematica, Sapienza Università di Roma, city=Rome, country=Italy\affiliation[gnfm]organization=Istituto Nazionale d’Alta Matematica, GNFM, city=Rome, country=Italy\affiliation[nanotec]organization=CNR-Nanotec, Unità di Lecce, city=Lecce, country=Italy\affiliation[sbai]organization=Dipartimento di Scienze di Base e Applicate all’Ingegneria, Sapienza Università di Roma, city=Rome, country=Italy\affiliation[infn]organization=Istituto Nazionale di Fisica Nucleare, Sezione di Roma 1, city=Rome, country=Italy

## 1Introduction

An associative memory is judged by two numbers: how many patterns it can store,
and how much of a pattern it needs to see before it recalls the rest. For four
decades the first number set the pace. Hopfield’s model[35], the
harmonic oscillator of neural computation, was shown by Amit, Gutfreund and
Sompolinsky to hold a number of memories growing only linearly in the
number of neurons,P≃0.14​NP\simeq 0.14\,N[9,10]. Reading the model
as a pairwise spin glass made the ceiling look fundamental, and made the way
past it obvious: add interactions. Baldi–Venkatesh and
Gardner[14,28,27]showed thatpp-body couplings
lift the capacity toP∼Np−1P\sim N^{\,p-1}[15], and the dense associative
memories of
Krotov and Hopfield[37,38,40,39]turned this
into a working principle for pattern recognition. Summing all the dense orders
at once is the natural endpoint of the program, and it delivers an
exponential capacityP∼ec​NP\sim e^{cN}: for binary neurons in the model of
Demircigil et al.[23], for continuous ones in the modern
Hopfield network of Ramsauer et al.[50], further developed into
energy-based transformer blocks[34], that underlies the
attention mechanism, and, analysed through the lens of glassy statistical
mechanics and Derrida’s random-energy model, in the work of Lucibello and
Mézard[43,24,25,33].

The binary case admits an especially transparent treatment. Albanese et al.[6]write the energy as a
sum of exponentials of the loss,ℋ=−N​∑μeN​(mμ−1)\mathcal{H}=-N\sum_{\mu}e^{N(m_{\mu}-1)}, and
show by a signal-to-noise argument, with no replicas and no mean-field
assumption, that each stored pattern is a fixed point of the zero-temperature
dynamics up to an exponentially large load, with basins of attraction that
shrink, but never close, as the load approaches capacity. That model is the
direct ancestor of the present one, and we lean on it throughout. It is worth
noting that this is not the only route to rigour available for this class of
models: the Guerra-interpolation programme has established, with comparable
rigour but different machinery (an interpolating free energy rather than a
cavity expansion), the free-energy and capacity of dense and Hebbian
associative networks[2,16,5]. We
use the cavity/large-deviation route throughout because it is the one that
extends most directly to the product-of-overlaps energy of
Section2, without asserting it is the only one that would work.
The same multi-layer, hetero-associative construction principle –there calledmultidirectional– has in fact been
analysed at (generalised) Hebbian order by replica methods across various architectures[19,3,7].

## The gap: association is not completion

All of the above are auto-associative. The network is handed a corrupted copy of
a stored vector and returns that vector; input and output live in the same space,
and “recall” means “clean-up”. Much of what one asks of an associative memory
is instead hetero-associative: cue and target are distinct objects, in general
in different spaces, and the task is to return the target given the cue. Pairing
the two chains of a receptor with the antigen they recognise, a sentence with its
intent, or one sensory modality with another are so many instances of this single
abstract map. An auto-associative network can only imitate it, by concatenating
cue and target into one long vector and hoping the dynamics does not tear the
halves apart. What is missing is a model in which the hetero-associative map is
the object the energy is built around, and in which the exponential capacity that
makes these networks attractive is provably retained.

Not every relation between cue and target can be stored, and it is worth saying
at once which can. The rule the network learns must be afunctionof the
cue –a cue mapped to two targets makes the two votes cancel in the field, and
the target layer relaxes to a mixture of them– and it must besurjectiveonto the target codebook, since a target no stored cue points
to is a memory with an empty basin. Injectivity, by contrast, is neither
required nor wanted: the many-to-one regime is the interesting one, and it is
the one real data supply. Remark1makes this precise and
quantifies the failure mode; every dataset below is passed through a filter that
enforces it.

## This paper

We introduce an exponential neural network ofLLlayers ofNNbinary neurons.
Each layer stores its own dataset ofPPpatterns, and the energy is an
exponential of theproductof the per-layer Mattis overlaps, so that it is
minimised precisely when every layer simultaneously retrieves the pattern of the
same index: the hetero-associative ground state. The linear-exponent
auto-associative model[6]is recovered atL=1L=1; aℤ2\mathbb{Z}_{2}-symmetric squared-overlap variant sits between them and is
analysed in an appendix.

Our contribution is twofold. On the theory side
(Sections2–6) we carry the cavity/signal-to-noise
program through for an arbitrary number of layersLL. The novelty relative to the
auto-associative case is that the per-pattern noise no longer factorises over
sites: the product structure makes its second moment a genuine large-deviation
integral, which we evaluate exactly at leading order by a saddle point on the
symmetric ray of layer magnetisations. The output is a closed-form storage
capacity, exponential in the layer sizeNN,Pc∼eN​ρL,P_{c}\;\sim\;e^{N\rho_{L}},(1)

whose rateρL\rho_{L}is fixed, for everyLL, by a single scalar saddle-point
equation: the stationarity condition of a one-dimensional variational functional,
evaluated on the symmetric ray along which all layers align coherently with the
same pattern. The rate is monotonically increasing inLLand approachesL​log⁡2L\log 2, so binding one further modality multiplies the capacity by a factor
that is itself exponential inNN. To this we add a matching analysis of the
basins under a corrupted cue, which exposes a
clean trade-off –wider networks store exponentially more but tolerate a
proportionally smaller corruption radius– together with the gap between the
annealed (moment) estimate and the typical realisation that governs finite-size
dynamics.

On the empirical side (Sections7–9) we ask the
question the theory cannot: what happens when the stored patterns are not
i.i.d. Rademacher vectors but real, structured, many-to-one data? We answer it
in three steps, moving from a generator we control to two domains that share
nothing but the surjective structure. First, on the Hidden Manifold
Model[31,29]–a controlled generator of patterns lying
near a low-dimensional manifold, with a surjective target– we show that the
exponential capacity survives, degrading gracefully as the manifold shrinks, that
the basins behave as the i.i.d. theory predicts, and that generalisation to
unseen points of the manifold is real but weak. Second, on real
T-cell-receptor/epitope triples from VDJdb[51,13], encoded
by Atchley factors[12]and a locality-sensitive
hash[20], we find the same phenomenon in sharp form: the network
is a near-perfect content-addressable memory –the two receptor chains recall
the epitope essentially without error, and its basins coincide with the i.i.d. prediction– but its ability to route an unseen receptor to the right epitope,
though several times above a label-permutation null, remains below its
memorisation. Third, on natural-language intent
data –CLINC150[42], a corpus with no biology, no geometry and no
alphabet in common with the previous two– the sameL=2L=2closed forms describe
capacity and basins without a single refitted constant, which is the sharpest
statement of universality we can make, while generalisation to unseen
utterances climbs to0.580.58against0.110.11on receptors.

Exponential storage and reliable generalisation thus emerge as distinct
capabilities of one network, and we make the separation quantitative. The
asymmetry should not be read as a defect. A memory of this family is built to
store: withNNbinary neurons there are2N2^{N}configurations and the network
occupies an exponential fraction of them with stored associations, so it is a
massive content-addressable repository rather than a low-complexity hypothesis
class, and no bound entitles one to expect strong extrapolation from an object
of that description. What is interesting is not that generalisation is bounded
but what sets the bound: it is the geometry of the encoding, not the data
domain. That data geometry, not merely data quantity, governs whether such
memories generalise is a theme of the random-features and hidden-manifold
Hopfield literature[47,36], which our results extend to the
binary exponential model.

## Outline and notation

Section2defines the model and fixes notation
(Table1); Section3derives the local field and
the update rule (Algorithm1); Sections4and5establish the exponential capacity; Section6treats the basins. The numerical narrative occupies
Sections7–9, and Section10draws
the memory-versus-classifier lesson. All heavy computations are deferred to the
appendices.

## 2The model

The system consists ofLLlayers, each composed ofNNbinary neurons,σia∈{−1,+1},a=1,…,L,i=1,…,N,\sigma_{i}^{a}\in\{-1,+1\},\qquad a=1,\dots,L,\quad i=1,\dots,N,(2)

We refer toLLas thewidthof the network and toNNas thelayer
size.
TheLLlayers are not
stacked in cascade, each transforming the output of the previous one, but
mutually coupled through a single symmetric energy and updated one neuron per
layer at a time (Section3), so a wider network here is one that
binds more modalities at once, not one that composes more transformations in
sequence. The neurons come
together withLLdatasets, one per layer, each ofPPindependent Rademacher patterns,ξiμ,a∈{−1,+1},ℙ​(ξiμ,a=±1)=12,\xi_{i}^{\mu,a}\in\{-1,+1\},\qquad\mathbb{P}\!\bigl(\xi_{i}^{\mu,a}=\pm 1\bigr)=\tfrac{1}{2},(3)

forμ=1,…,P\mu=1,\dots,P,a=1,…,La=1,\dots,Landi=1,…,Ni=1,\dots,N.
The patterns are mutually independent across(μ,a,i)(\mu,a,i).111This
layer-wise independence is the structural choice that drives the whole analysis:
it suppresses inter-layer statistical mixing at the source. Were a single pattern
replicated across layers, the fluctuations of distinct layer fields at the same
site would become entangled, and cross-pattern terms would survive every average
taken below instead of vanishing by parity. It is an idealisation: real
hetero-associative data couple the layers through a shared latent cause, and
quantifying the price of violating it is one purpose of the experiments.We
retain the inverse temperatureβ:=1/T\beta:=1/T(set toβ→∞\beta\to\inftythroughout) as a control parameter, together
with the number of stored patternsPPper layer222The appropriate intensive
measure of storage, namely the classical ratioP/NP/Nbeing here exponentially large is discussed in Section5.. The Mattis magnetisations
(equivalently, Mattis overlaps: we use the two names interchangeably)mμa:=1N​∑i=1Nξiμ,a​σia,m_{\mu}^{a}\;:=\;\frac{1}{N}\sum_{i=1}^{N}\xi_{i}^{\mu,a}\,\sigma_{i}^{a},(4)

(for eachμ=1,…,P\mu=1,\dots,Panda=1,…,La=1,\dots,L) as order parameters. Table1collects, once and for all, every
symbol used in the main text.

The cost function readsℋ​(𝝈|𝝃):=−N​∑μ=1Pexp⁡[N​∑a<b(mμa​mμb−1)].\mathcal{H}(\bm{\sigma}\,|\,\bm{\xi})\;:=\;-N\sum_{\mu=1}^{P}\exp\!\biggl[\,N\sum_{a<b}\bigl(m_{\mu}^{a}\,m_{\mu}^{b}-1\bigr)\biggr].(5)

The exponent vanishes on the perfect hetero-associative configurationmμa=1m_{\mu}^{a}=1for everyaa, normalised through the−1-1subtraction so that on
the recalled archetype∑a<b(1⋅1−1)=0\sum_{a<b}(1\cdot 1-1)=0.333A genuinelyLL-way
productexp⁡[N​∏amμa−N]\exp[N\prod_{a}m_{\mu}^{a}-N]would be
the literal AND of theLLretrieval events, and is not the choice made here.
It would collapse to0discontinuously the moment a single layer left
perfect recall, with no graceful degradation under corruption; the pairwise
sum, in contrast, stays𝒪​(1)\mathcal{O}(1)as long as even one pair of layers
remains aligned (the mechanism behind the basins of Section6),
reduces to theL=1L=1model of[6]without a separate
prescription, and is the only symmetric multilinear form admitting the
collective/orthogonal split of (7) on which every
saddle-point argument below relies.Two limits anchor
(5). The first isL=1L=1, and it is instructive that it isnota special case: with a single layer the double sum is empty, the
exponent vanishes identically andℋ≡−N​P\mathcal{H}\equiv-NPceases to depend on the
configuration. Hetero-association is intrinsically a coupling between at least
two layers, and the auto-associative exponential networks are recovered not by
settingL=1L=1in (5) but by replacing the missing partner
layer with the pattern itself,mμa​mμb↦mμm_{\mu}^{a}m_{\mu}^{b}\mapsto m_{\mu}ormμa​mμb↦mμ2m_{\mu}^{a}m_{\mu}^{b}\mapsto m_{\mu}^{2}. The first substitution returns the model
of Ref.[6], with energy−N​∑μeN​(mμ−1)-N\sum_{\mu}e^{N(m_{\mu}-1)}; the
second returns itsℤ2\mathbb{Z}_{2}-symmetric sibling, whose saddle point turns
out to coincide with theL=3L=3specialisation of the analysis below. Both are
carried out in parallel with the multilayer computation inD. The second anchor is the dense series: expanding the
exponent around perfect recall returns, order by order, multi-body couplings of
growing degree, so (5) is again a resummation of all dense
interactions, now with the interaction legs distributed across
layers.444The identification with the dense associative memories is
literal only in the single-layer case: expandingeN​(mμ−1)e^{N(m_{\mu}-1)}in powers ofmμm_{\mu}reproduces exactly thepp-body couplings of Krotov and
Hopfield[37], one per order. ForL≥2L\geq 2thekk-th order ofexp⁡[N​∑a<bmμa​mμb]\exp[N\sum_{a<b}m_{\mu}^{a}m_{\mu}^{b}]is a sum of products of2​k2kMattis
overlaps drawn from distinct layer pairs, hence a2​k2k-body spin coupling whose
legs sit in different layers: the hetero-associative analogue of the dense
series rather than the series itself.

## What can be stored

The energy (5) treats all layers alike, but a retrieval task
does not: it designates some layers as cue and one as target. Fix the
convention used throughout, layers1,…,L−11,\dots,L-1cue and layerLLtarget, and
read thePPstored indices as the graph of a relationΨ={(𝒞μ,𝝃μ,L)}μ=1P,𝒞μ:=(𝝃μ,1,…,𝝃μ,L−1),\Psi\;=\;\bigl\{\bigl(\,\mathcal{C}^{\mu},\,\bm{\xi}^{\mu,L}\,\bigr)\bigr\}_{\mu=1}^{P},\qquad\mathcal{C}^{\mu}:=\bigl(\bm{\xi}^{\mu,1},\dots,\bm{\xi}^{\mu,L-1}\bigr),(6)

between cue tuples and targets, and let𝒯={𝝃μ,L}μ≤P\mathcal{T}=\{\bm{\xi}^{\mu,L}\}_{\mu\leq P}be the target codebook, of sizeK=|𝒯|K=|\mathcal{T}|. Not every relation is storable:Ψ\Psimust be a surjectivefunctionfrom the stored cues onto𝒯\mathcal{T}. The constraint is not a
modelling preference but a property of the local field, so we state and quantify
it in Remark1of Section3, once the field
has been derived; it is the
reason every dataset in Sections7–9is passed
through a function filter before the network sees it.

## Collective and orthogonal modes

The bilinear form in the exponent admits the orthogonal decomposition∑a<bma​mb=12​[(∑ama)2−∑a(ma)2].\sum_{a<b}m^{a}\,m^{b}\;=\;\tfrac{1}{2}\Bigl[\,\bigl(\textstyle\sum_{a}m^{a}\bigr)^{2}-\textstyle\sum_{a}(m^{a})^{2}\,\Bigr].(7)

The first term,(∑ama)2\bigl(\sum_{a}m^{a}\bigr)^{2}, is the squared collective
magnetisation: it isolates the symmetric mode in which all layers align
coherently with a common archetype, the natural order parameter of
hetero-associative recall. The second term,∑a(ma)2\sum_{a}(m^{a})^{2}, weights the
residual layer-by-layer dispersion around that collective alignment. The
Hamiltonian (5) therefore rewards configurations in which
every layer simultaneously and uniformly retrieves the same pattern index, and
penalises any layer-discordant deviation. This separation between a single
collective mode andL−1L-1orthogonal fluctuation modes governs every
saddle-point analysis encountered below.SymbolMeaningNNneurons per layer (layer size)LLnumber of layers (network width)PPnumber of stored patterns per layer𝒞μ=(𝝃μ,1,…,𝝃μ,L−1)\mathcal{C}^{\mu}=(\bm{\xi}^{\mu,1},\dots,\bm{\xi}^{\mu,L-1})stored cue tuple of indexμ\muΨ:𝒞μ↦𝝃μ,L\Psi:\ \mathcal{C}^{\mu}\mapsto\bm{\xi}^{\mu,L}the stored association rule, a surjective function (Remark1)𝒯,K=|𝒯|\mathcal{T},\ K=|\mathcal{T}|target codebook and its size;P/KP/Kis the compressionσia∈{−1,+1}\sigma_{i}^{a}\in\{-1,+1\}state of neuroniiin layeraaξiμ,a∈{−1,+1}\xi_{i}^{\mu,a}\in\{-1,+1\}bitiiof patternμ\muin layeraa(Rademacher)mμa=1N​∑iξiμ,a​σiam_{\mu}^{a}=\frac{1}{N}\sum_{i}\xi_{i}^{\mu,a}\sigma_{i}^{a}Mattis overlap of layeraawith patternμ\mum^μa=1N​∑j≠iξjμ,a​σja\hat{m}_{\mu}^{a}=\frac{1}{N}\sum_{j\neq i}\xi_{j}^{\mu,a}\sigma_{j}^{a}cavity (on-site-excluded) overlapFμa=∑b≠am^μbF_{\mu}^{a}=\sum_{b\neq a}\hat{m}_{\mu}^{b}cross-layer cavity field feeding layeraaE^μ=N​∑a<bm^μa​m^μb−N​(L2)\hat{E}_{\mu}=N\sum_{a<b}\hat{m}_{\mu}^{a}\hat{m}_{\mu}^{b}-N\binom{L}{2}cavity energy of patternμ\muΦμ(\a)=exp⁡(∑c≠aξiμ,c​σic​Fμc)\Phi_{\mu}^{(\backslash a)}=\exp(\sum_{c\neq a}\xi_{i}^{\mu,c}\sigma_{i}^{c}F_{\mu}^{c})on-site off-layer factorhiah_{i}^{a}local field on neuron(i,a)(i,a), Eq. (13)Xia=ξi1,a​hiaX_{i}^{a}=\xi_{i}^{1,a}h_{i}^{a}stability variable of the recalled stateμ1,σ2\mu_{1},\ \sigma^{2}mean and variance (signal and noise) ofXiaX_{i}^{a}ρL\rho_{L}noise/storage rate, Eq. (24)α=1N​log⁡P\alpha=\tfrac{1}{N}\log Pexponential storage rate (intensive load); capacity atα=ρL\alpha=\rho_{L}γ\gammareduced load,γ→0\gamma\to 0retrieval /γ≈1\gamma\!\approx\!1transition, Eq. (34)KLK_{L}polynomial prefactor of the per-pattern noise, Eq. (25)m∗,x∗=2​(L−1)​m∗m^{\ast},\ x^{\ast}=2(L-1)m^{\ast}symmetric saddle, Eq. (23)r∈(0,1]r\in(0,1]initial overlap of a corrupted cue (d=(1−r)/2d=(1-r)/2Hamming radius)εL​(r)\varepsilon_{L}(r)storage exponent under corruption, Eq. (41)αD=D/N\alpha_{D}=D/Nmanifold aspect ratio (DDlatent dim., Section7)Table 1:Notation used throughout the main text. Cavity quantities are defined
at the site(i,a)(i,a)being updated;(L2)=L​(L−1)/2\binom{L}{2}=L(L-1)/2.

## 3Local field and dynamical update rule

The dynamics is studied in the cavity formulation: we isolate a single neuron(i,a)(i,a), express the energy as a term independent of it plus a term linear in it,
and read off the field that drives its update. Removing that one neuron from the
interaction network is what defines thecavity, and it fixes the meaning
of the whole family of names used below: the cavity overlapm^μa\hat{m}_{\mu}^{a}is
the Mattis overlap of the punctured system, the cavity fieldFμaF_{\mu}^{a}the
field the rest of the network exerts into the hole, the cavity energyE^μ\hat{E}_{\mu}and the cavity exponents of Section6the
corresponding energies and large-deviation rates evaluated there. The device
goes back to Onsager’s reaction field[48]and is standard in the
statistical mechanics of disordered
systems[44,32,18,45],
including for the Hopfield model
specifically[49,46]; we recall the names here
once, since not all of them are equally common outside that literature.
Splitting the on-site contribution
from the magnetisation,mμa=m^μa+ξiμ,a​σiaN,m^μa:=1N​∑j≠iξjμ,a​σja,m_{\mu}^{a}\;=\;\hat{m}_{\mu}^{a}+\frac{\xi_{i}^{\mu,a}\,\sigma_{i}^{a}}{N},\qquad\hat{m}_{\mu}^{a}\;:=\;\frac{1}{N}\sum_{j\neq i}\xi_{j}^{\mu,a}\,\sigma_{j}^{a},(8)

and inserting (8) in the bilinear form,N​∑a<bmμa​mμb\displaystyle N\sum_{a<b}m_{\mu}^{a}m_{\mu}^{b}=N​∑a<b(m^μa+ξiμ,a​σiaN)​(m^μb+ξiμ,b​σibN)\displaystyle\;=\;N\sum_{a<b}\Bigl(\hat{m}_{\mu}^{a}+\tfrac{\xi_{i}^{\mu,a}\sigma_{i}^{a}}{N}\Bigr)\Bigl(\hat{m}_{\mu}^{b}+\tfrac{\xi_{i}^{\mu,b}\sigma_{i}^{b}}{N}\Bigr)=N​∑a<bm^μa​m^μb+∑a<b[ξiμ,a​σia​m^μb+ξiμ,b​σib​m^μa]\displaystyle\;=\;N\sum_{a<b}\hat{m}_{\mu}^{a}\hat{m}_{\mu}^{b}+\sum_{a<b}\bigl[\xi_{i}^{\mu,a}\sigma_{i}^{a}\hat{m}_{\mu}^{b}+\xi_{i}^{\mu,b}\sigma_{i}^{b}\hat{m}_{\mu}^{a}\bigr]+𝒪​(N−1).\displaystyle\qquad+\mathcal{O}(N^{-1}).(9)

The identity∑a<b[Xa​Yb+Xb​Ya]=∑cXc​∑d≠cYd\sum_{a<b}[X_{a}Y_{b}+X_{b}Y_{a}]=\sum_{c}X_{c}\sum_{d\neq c}Y_{d}withXc=ξiμ,c​σicX_{c}=\xi_{i}^{\mu,c}\sigma_{i}^{c}andYd=m^μdY_{d}=\hat{m}_{\mu}^{d}collapses the second sum
to∑cξiμ,c​σic​Fμc\sum_{c}\xi_{i}^{\mu,c}\sigma_{i}^{c}\,F_{\mu}^{c}, whereFμc:=∑d≠cm^μdF_{\mu}^{c}:=\sum_{d\neq c}\hat{m}_{\mu}^{d}(the total cavity overlap that all
layers other thanccalready have with patternμ\mu) is the inter-layer
cavity field, defined together with the remaining cavity quantities
in (15) below. Substituting in the exponential
of (5) and usingex+𝒪​(N−1)=ex​(1+𝒪​(N−1))e^{x+\mathcal{O}(N^{-1})}=e^{x}(1+\mathcal{O}(N^{-1})),ℋ​(𝝈|𝝃)=−N​∑μ=1PeE^μ​exp⁡(∑c=1Lξiμ,c​σic​Fμc)​(1+𝒪​(N−1)).\mathcal{H}(\bm{\sigma}|\bm{\xi})\;=\;-N\sum_{\mu=1}^{P}e^{\hat{E}_{\mu}}\,\exp\!\Bigl(\sum_{c=1}^{L}\xi_{i}^{\mu,c}\sigma_{i}^{c}\,F_{\mu}^{c}\Bigr)\bigl(1+\mathcal{O}(N^{-1})\bigr).(10)

Factoring out layeraain the inner exponential and applying the binary identityex​σ=cosh⁡x+σ​sinh⁡xe^{x\sigma}=\cosh x+\sigma\sinh xwithx=ξiμ,a​Fμax=\xi_{i}^{\mu,a}F_{\mu}^{a}andσ=σia∈{−1,+1}\sigma=\sigma_{i}^{a}\in\{-1,+1\}produces the additive splitexp⁡(ξiμ,a​σia​Fμa)=cosh⁡(ξiμ,a​Fμa)+σia​sinh⁡(ξiμ,a​Fμa).\exp\!\Bigl(\xi_{i}^{\mu,a}\sigma_{i}^{a}F_{\mu}^{a}\Bigr)\;=\;\cosh\!\bigl(\xi_{i}^{\mu,a}F_{\mu}^{a}\bigr)+\sigma_{i}^{a}\sinh\!\bigl(\xi_{i}^{\mu,a}F_{\mu}^{a}\bigr).(11)

Collecting theσia\sigma_{i}^{a}-independent terms inCiaC_{i}^{a}and the linear ones
inhiah_{i}^{a}yieldsℋ​(𝝈|𝝃)=−N​[Cia+σia​hia]​(1+𝒪​(N−1)),\mathcal{H}(\bm{\sigma}|\bm{\xi})\;=\;-N\bigl[\,C_{i}^{a}+\sigma_{i}^{a}\,h_{i}^{a}\,\bigr]\bigl(1+\mathcal{O}(N^{-1})\bigr),(12)

with the local field and shift, respectively,hia\displaystyle h_{i}^{a}:=∑μ=1PeE^μ​sinh⁡(ξiμ,a​Fμa)​Φμ(\a),\displaystyle\;:=\;\sum_{\mu=1}^{P}e^{\hat{E}_{\mu}}\,\sinh\!\bigl(\xi_{i}^{\mu,a}\,F_{\mu}^{a}\bigr)\,\Phi_{\mu}^{(\backslash a)},(13)Cia\displaystyle C_{i}^{a}:=∑μ=1PeE^μ​cosh⁡(ξiμ,a​Fμa)​Φμ(\a).\displaystyle\;:=\;\sum_{\mu=1}^{P}e^{\hat{E}_{\mu}}\,\cosh\!\bigl(\xi_{i}^{\mu,a}\,F_{\mu}^{a}\bigr)\,\Phi_{\mu}^{(\backslash a)}.(14)

The cavity quantities areFμa\displaystyle F_{\mu}^{a}:=∑b≠am^μb,E^μ:=N​∑a<bm^μa​m^μb−N​(L2),\displaystyle\;=\;\sum_{b\neq a}\hat{m}_{\mu}^{b},\qquad\hat{E}_{\mu}\;=\;N\sum_{a<b}\hat{m}_{\mu}^{a}\hat{m}_{\mu}^{b}-N\binom{L}{2},(15)Φμ(\a)\displaystyle\Phi_{\mu}^{(\backslash a)}:=exp⁡(∑c≠aξiμ,c​σic​Fμc).\displaystyle\;=\;\exp\!\Bigl(\sum_{c\neq a}\xi_{i}^{\mu,c}\sigma_{i}^{c}\,F_{\mu}^{c}\Bigr).

Each of these has a plain reading. Theinter-layer cavity fieldFμaF_{\mu}^{a}is the total overlap that all layers other thanaaalready
have with patternμ\mu: it is the pressure the rest of the network exerts on
layeraato also retrieveμ\mu, and it is what makes the model
hetero-associative: a neuron in one layer is driven by the state of the
others. Thecavity energyE^μ\hat{E}_{\mu}measures how well patternμ\muis
collectively retrieved across all layer pairs; its−N​(L2)-N\binom{L}{2}floor sendseE^μ→0e^{\hat{E}_{\mu}}\to 0for any pattern that is not being retrieved, so only the
winning pattern contributes to the field. The on-site factorΦμ(\a)\Phi_{\mu}^{(\backslash a)}is the same weight restricted to the off-layer bits
at the site under update. The remainder in (12) collects the
on-site square contributions∑a<b(ξiμ,a​σia)​(ξiμ,b​σib)/N\sum_{a<b}(\xi_{i}^{\mu,a}\sigma_{i}^{a})(\xi_{i}^{\mu,b}\sigma_{i}^{b})/Ngenerated
by (8); these are bounded in absolute value by(L2)/N\binom{L}{2}/N, are invariant underξia​σia↦−ξia​σia\xi_{i}^{a}\sigma_{i}^{a}\mapsto-\xi_{i}^{a}\sigma_{i}^{a}to leading order, and do not affect the single-flip energy difference at𝒪​(1)\mathcal{O}(1). The cavity decomposition is exact at this order.

The field (13) has a transparent reading. Each stored patternμ\mucasts a vote on neuron(i,a)(i,a), weighted byeE^μe^{\hat{E}_{\mu}}(how well
the rest of the network already agrees with patternμ\muacross all layers)
and directed bysinh⁡(ξiμ,a​Fμa)\sinh(\xi_{i}^{\mu,a}F_{\mu}^{a}), the alignment that the
other layers ask of layeraa. The exponential weight is what makes the
network hetero-associative and high-capacity at once: a pattern that is being
collectively retrieved dominates the sum, while thee−N​(L2)e^{-N\binom{L}{2}}floor ofE^μ\hat{E}_{\mu}silences every pattern that is not.

The single-flip energy variation isΔ​Eia=2​N​hia​σia\Delta E_{i}^{a}=2N\,h_{i}^{a}\,\sigma_{i}^{a},
exact when all spins other than(i,a)(i,a)are held fixed, so the zero-temperature
Glauber update is steepest descent,σia​(t+1)=sign​[hia​(t)],\sigma_{i}^{a}(t+1)\;=\;\mathrm{sign}\!\bigl[\,h_{i}^{a}(t)\,\bigr],(16)

in words (Algorithm1): every neuron looks at how strongly each
stored pattern is currently being retrieved network-wide, and flips to agree with
the winner.

The schedule with which (16) is applied deserves a word, because
“parallel” is used here in a restricted sense. One elementary step selects a
single site indexiiand updates theLLneurons(i,1),…,(i,L)(i,1),\dots,(i,L)–one per
layer– simultaneously, from the fields evaluated on the current state; the
site index is then advanced along a fixed or randomly shuffled permutation of{1,…,N}\{1,\dots,N\}, and a sweep is complete once allNNsites have been visited.
The update is thusparallel across layers and sequential within each
layer: theNNspins of a given layer are never flipped at once. Keeping the
within-layer update sequential is what preserves the cavity
decomposition (12), which holds every other spin of layeraafixed while(i,a)(i,a)is updated; flipping a whole layer synchronously would
change the overlapsm^μa\hat{m}_{\mu}^{a}by𝒪​(1)\mathcal{O}(1)and invalidate the
fields on which the flips were decided.

The simultaneity across layers is a genuine, if mild, synchronicity, and it is
worth locating exactly. The cavity overlapsm^μb\hat{m}_{\mu}^{b}, hence the fieldsFμaF_{\mu}^{a}and the weightseE^μe^{\hat{E}_{\mu}}, exclude siteiiin every
layer and are therefore unaffected by theLLflips; the only dependence ofhiah_{i}^{a}on the spins updated alongside it is through the on-site factorΦμ(\a)\Phi_{\mu}^{(\backslash a)}. In the retrieval regime the sum
in (13) is dominated by the one pattern witheE^μ=𝒪​(1)e^{\hat{E}_{\mu}}=\mathcal{O}(1), and theLLsimultaneous updates then all point
at that same stored index, so the coupling is benign; away from it the rule is
simply taken as the definition of the dynamics. In either case the stability
analysis of Sections4–5is a single-site
statement,Xia>0X_{i}^{a}>0, and is insensitive to the order in which sites are
visited.Input:layer datasets{ξμ,a}\{\xi^{\mu,a}\}; initial state𝝈(0)∈{−1,+1}L​N\bm{\sigma}^{(0)}\in\{-1,+1\}^{LN}; number of sweepsNpN_{p}.Output:fixed point𝝈∗\bm{\sigma}^{\ast}.fort=1t=1toNpN_{p}doforeachsiteiiin a fixed or shuffled permutation of1,…,N1,\dots,N(sequentially)doforeachpatternμ\muand layeraadom^μa←1N​∑j≠iξjμ,a​σja\hat{m}_{\mu}^{a}\leftarrow\tfrac{1}{N}\sum_{j\neq i}\xi_{j}^{\mu,a}\sigma_{j}^{a};//how well patternμ\muis retrieved in layeraa, siteiiexcludedforeachpatternμ\mudoE^μ←N​∑a<bm^μa​m^μb−N​(L2)\hat{E}_{\mu}\leftarrow N\sum_{a<b}\hat{m}_{\mu}^{a}\hat{m}_{\mu}^{b}-N\binom{L}{2};//collective retrieval weight ofμ\muforeachlayera=1,…,La=1,\dots,L(simultaneously: one neuron per layer)dohia←∑μeE^μ​sinh⁡(ξiμ,a​Fμa)​Φμ(\a)h_{i}^{a}\leftarrow\sum_{\mu}e^{\hat{E}_{\mu}}\sinh\!\bigl(\xi_{i}^{\mu,a}F_{\mu}^{a}\bigr)\,\Phi_{\mu}^{(\backslash a)};//Eq. (13)σia←sign​(hia)\sigma_{i}^{a}\leftarrow\mathrm{sign}\!\bigl(h_{i}^{a}\bigr);Algorithm 1Zero-temperature update of the exponential hetero-associative network

The field also settles the question left open in Section2: which
association rules (6) the energy can hold.

## Remark 1(The stored rule must be a surjective function).

For (5) to operate as a hetero-associative memory,Ψ\Psimust be a function of the cue and a surjection onto the target
codebook𝒯\mathcal{T}.

(i) Single-valuedness.Supposeq≥2q\geq 2stored indices share a cue,𝒞λ=𝒞\mathcal{C}^{\lambda}=\mathcal{C}forλ∈S\lambda\in Swith|S|=q|S|=q, but carry
distinct targets. Clamping the cue at𝒞\mathcal{C}makes the cavity energyE^λ\hat{E}_{\lambda}, the inter-layer fieldFλLF_{\lambda}^{L}and the on-site factorΦλ(\L)\Phi_{\lambda}^{(\backslash L)}of (15) identical for
everyλ∈S\lambda\in S, and exponentially suppressed for every other pattern.
Sincesinh\sinhis odd, the target field (13) collapses tohiL=eE^​sinh⁡(FL)​Φ(\L)​∑λ∈Sξiλ,L​(1+o​(1)),h_{i}^{L}\;=\;e^{\hat{E}}\,\sinh\!\bigl(F^{L}\bigr)\,\Phi^{(\backslash L)}\sum_{\lambda\in S}\xi_{i}^{\lambda,L}\;\bigl(1+o(1)\bigr),(17)

so the update (16) returns the componentwise majority of theqqcontradictory targets. For independent targets the overlap of that majority with
any one of them is exactly(q−1(q−1)/2)​2−(q−1)≃2/(π​q)\binom{q-1}{(q-1)/2}2^{-(q-1)}\simeq\sqrt{2/(\pi q)}for oddqq: unity atq=1q=1, one half atq=3q=3, decaying to zero thereafter. A cue carrying two
targets is therefore not stored badly but not stored at all; what the network
returns is a mixture of them, and the failure is a property of the energy rather
than of the dynamics.

(ii) Surjectivity.Conversely, the addressable alphabet is exactly the
imageΨ​({𝒞μ})\Psi(\{\mathcal{C}^{\mu}\}). A code sitting in layerLLthat no stored
cue points to never dominates the field, its weighteE^e^{\hat{E}}ise−N​(L2)e^{-N\binom{L}{2}}-suppressed for every cue, so it carries an empty basin
while still contributing its share to the noise floor of
Section4: capacity spent on a memory that cannot be recalled.
ReadingΨ\Psias a surjection onto𝒯\mathcal{T}is what excludes this.

Injectivity, by contrast, is neither required nor desirable. The regime of
interest isP≫KP\gg K, withP/KP/Kthe mean number of cues per target: it is the
regime real data supply (many receptors per epitope, many phrasings per intent),
andP/KP/Kcontrols the depth of the target’s basin
(Section7). A bijective rule would make the reverse direction a
function as well, and the model would collapse to an auto-associative memory on
the concatenated vector: the situation the construction was meant to improve
on.

## Computational cost: time and memory

Algorithm1is exact, but not free, and the exponential
capacity of Section5carries an exponential price tag that is
worth making explicit. The first loop evaluatesP​LPLinner products of lengthNN:Θ​(N​L​P)\Theta(NLP)operations. The second costsΘ​(P​L2)\Theta(PL^{2}). The third,
read literally, costsΘ​(N​L2​P)\Theta(NL^{2}P), becauseΦμ(\a)\Phi_{\mu}^{(\backslash a)}sumsL−1L-1terms at every site; caching the full on-site sumTiμ:=∑cξiμ,c​σic​FμcT_{i}^{\mu}:=\sum_{c}\xi_{i}^{\mu,c}\sigma_{i}^{c}F_{\mu}^{c}once per(i,μ)(i,\mu)and
subtracting theaa-th term at evaluation time reduces this toΘ​(N​L​P)\Theta(NLP).
One parallel sweep of the whole network therefore costsΘ​(N​L​P)\Theta(NLP)time
wheneverN≳LN\gtrsim L(true throughout this paper), andΘ​(N​L​P)\Theta(NLP)bits is
also the memory floor, set by theLLstored datasets and dwarfing theΘ​(N​L)\Theta(NL)state and theΘ​(P​L)\Theta(PL)cavity scalars{m^μa,E^μ,Fμa}\{\hat{m}_{\mu}^{a},\hat{E}_{\mu},F_{\mu}^{a}\}. Time and memory per sweep are thus
both, to leading order, one read of the stored data, andnstepsn_{\mathrm{steps}}sweeps costΘ​(nsteps​N​L​P)\Theta(n_{\mathrm{steps}}NLP).

The cost is linear inPP, but the capacity of Section5is
exponential inNN: running the network anywhere near capacity costsΘ​(N​L​eN​ρL)\Theta(NL\,e^{N\rho_{L}})per sweep, at exactly the rateρL\rho_{L}that sets the
storage. Already atN=64N=64andL=2L=2no machine could hold the stored data, let
alone sweep them. The capacity statement is about which configurations are fixed
points of (16), not a promise that all of them can be enumerated;
this is why every experiment below usesNNof order ten and loads far belowPcP_{c}, where the degradation transition falls in an accessible window. The
arithmetic is made explicit inE.

## 4Stability of the recalled ground state

We analyse the stability of the hetero-associative configuration(𝝈1,…,𝝈L)=(𝝃1,1,…,𝝃1,L),(\bm{\sigma}^{1},\dots,\bm{\sigma}^{L})\;=\;(\bm{\xi}^{1,1},\dots,\bm{\xi}^{1,L}),(18)

in which all layers retrieve the same archetype indexμ0=1\mu_{0}=1, each from its
own dataset. By (16), stability against a single-spin flip at siteiiin layeraaamounts toXia:=ξi1,a​hia|𝝈b=𝝃1,b>0.X_{i}^{a}\;:=\;\xi_{i}^{1,a}\,h_{i}^{a}\bigl|_{\bm{\sigma}^{b}=\bm{\xi}^{1,b}}\;>\;0.(19)

The strategy is the classic signal-to-noise decomposition of attractor neural
networks[9,11,21], in the one-step, zero-temperature
form used for exponential models in
Refs.[23,6]: the field is a sum ofPPpattern votes; the vote of the recalled pattern is a deterministicsignal, the remainingP−1P-1are mean-zeronoise, and one asks when
the first dominates the fluctuations of the second. In the limit of
largeNNandPP555Throughout,N→∞N\to\inftyis taken first, at fixedμ\mu-th pattern, to obtain the exact rateρL\rho_{L}and prefactorKLK_{L}below;
the loadPPis then let grow, at fixedNN, asP=γ​eN​ρLP=\gamma\,e^{N\rho_{L}}for a
fixed load fractionγ\gamma, so that the one-step overlap collapses onto the
universal profilem1(1)=erf​(1/2​γ)m_{1}^{(1)}=\mathrm{erf}(1/\sqrt{2\gamma})of (32) (used
again inF). No double limit is taken simultaneously.the Central Limit Theorem rendersXiaX_{i}^{a}Gaussian,Xia∼𝒩​(μ1,μ2−μ12)X_{i}^{a}\sim\mathcal{N}\!\bigl(\mu_{1},\sqrt{\mu_{2}-\mu_{1}^{2}}\bigr), and stability
holds with overwhelming probability as long as the signal dominates the noise
standard deviation. (The Berry–Esseen control of this approximation, uniform inNNbecause the noise terms are i.i.d. across the independent layer datasets, is
given inA.) Everything therefore rests on two moments.

## 4.1The signal

At the trial state (18) the cavity magnetisation of the recalled
archetype is deterministic,m^1a=(N−1)/N\hat{m}_{1}^{a}=(N-1)/Nfor everyaa, while forμ≠1\mu\neq 1the layer-aaon-site factorξiμ,a\xi_{i}^{\mu,a}is independent of every
quantity in the corresponding noise term and has zero mean. The mean ofXiaX_{i}^{a}reduces to the signal alone; the computation (A)
givesμ1=𝔼​[Xia]=e−(L−1)​sinh⁡(L−1)+𝒪​(N−1).\mu_{1}\;=\;\mathbb{E}\bigl[X_{i}^{a}\bigr]\;=\;e^{-(L-1)}\sinh(L-1)+\mathcal{O}(N^{-1}).(20)

An independent check via the discrete energy difference at the trial state,Δ​Eia=N​(1−e−2​(L−1))\Delta E_{i}^{a}=N\bigl(1-e^{-2(L-1)}\bigr), is given inA. The signal is of order one and grows with the width:μ1=12​(1−e−2​(L−1))→12\mu_{1}=\tfrac{1}{2}(1-e^{-2(L-1)})\to\tfrac{1}{2}asL→∞L\to\infty.

## 4.2The noise

The second moment splits asμ2=∑μ,ν𝔼​[Xi(μ|a)​Xi(ν|a)]=μ2(diag)+μ2(off)\mu_{2}=\sum_{\mu,\nu}\mathbb{E}[X_{i}^{(\mu|a)}X_{i}^{(\nu|a)}]=\mu_{2}^{(\mathrm{diag})}+\mu_{2}^{(\mathrm{off})}.
Layer-wise dataset independence kills the off-diagonal part exactly
(A): a single uncancelled on-site Rademacher factor
carries zero mean. The diagonal part is a deterministic signal-square,𝔼​[(Xi(1|a))2]=e−2​(L−1)​sinh2⁡(L−1)+𝒪​(N−1),\mathbb{E}\bigl[(X_{i}^{(1|a)})^{2}\bigr]\;=\;e^{-2(L-1)}\sinh^{2}(L-1)+\mathcal{O}(N^{-1}),(21)

plusP−1P-1identical per-pattern noise contributions. Here the model departs from
its single-layer ancestor. Each noise term reduces, after averaging the on-site
factor, to the cavity expectation𝔼​[(Xi(μ|a))2]=𝔼​[e2​E^μ​sinh2⁡(Fμa)​∏c≠acosh⁡(2​Fμc)],μ≠1,\mathbb{E}\bigl[(X_{i}^{(\mu|a)})^{2}\bigr]\;=\;\mathbb{E}\!\Bigl[\,e^{2\hat{E}_{\mu}}\sinh^{2}(F_{\mu}^{a})\prod_{c\neq a}\cosh(2F_{\mu}^{c})\,\Bigr],\quad\mu\neq 1,(22)

where the expectation runs over the cavity magnetisations𝒎^μ∈[−1,1]L\bm{\hat{m}}_{\mu}\in[-1,1]^{L}. In the auto-associative model the exponent islinearin the Rademacher variables and this average factorises over sites
into a closed form; the product-over-layers structure of (22)
makes the exponent effectivelyquadratic, the average no longer
factorises, and a genuine large-deviation evaluation is required.

By Cramér’s theorem the empirical magnetisation of each layer obeys a large
deviation principle with the symmetric-Bernoulli rate function; independence
across layers adds the rates; and Varadhan’s
lemma[52,22]turns (22)
into a variational problem. The functional is permutation-symmetric in the
layers, and its unique non-trivial saddle sits on the symmetric raymc≡m∗m^{c}\equiv m^{\ast}, the maximally aligned direction of (7), solvingm∗=tanh⁡(2​(L−1)​m∗).m^{\ast}\;=\;\tanh\!\bigl(2(L-1)\,m^{\ast}\bigr).(23)

We stress that the full derivation is inB. Its output is two quantities. The exponential decay
rate of a single-pattern noise contribution isρL=L​[(L−1)−ϕL​(x∗)],ϕL​(x)=−x24​(L−1)+log⁡cosh⁡(x),{\;\begin{aligned} \rho_{L}&\;=\;L\bigl[(L-1)-\phi_{L}(x^{\ast})\bigr],\\
\phi_{L}(x)&\;=\;-\frac{x^{2}}{4(L-1)}+\log\cosh(x),\end{aligned}\;}(24)

withx∗=2​(L−1)​m∗x^{\ast}=2(L-1)m^{\ast}the unique positive solution oftanh⁡(x)=x/[2​(L−1)]\tanh(x)=x/[2(L-1)]. The polynomial prefactor encoding the Gaussian
fluctuations around the saddle and the on-site insertions evaluated at𝒎=m∗​𝟏\bm{m}=m^{\ast}\bm{1}isKL=(2​π)L/2detℋL∗sinh2((L−1)m∗)cosh(2(L−1)m∗)L−1,K_{L}\;=\;\frac{(2\pi)^{L/2}}{\sqrt{\det\mathcal{H}_{L}^{\ast}}}\,\sinh^{2}\!\bigl((L-1)m^{\ast}\bigr)\,\cosh\!\bigl(2(L-1)m^{\ast}\bigr)^{L-1},(25)

withℋL∗\mathcal{H}_{L}^{\ast}the Hessian of the variational functional at the
saddle (B). Hence𝔼​[(Xi(μ|a))2]=KL​e−N​ρL​(1+o​(1)).\mathbb{E}\bigl[(X_{i}^{(\mu|a)})^{2}\bigr]\;=\;K_{L}\,e^{-N\rho_{L}}\bigl(1+o(1)\bigr).(26)

Combining (21) with theP−1P-1noise contributions,μ2=e−2​(L−1)​sinh2⁡(L−1)+(P−1)​KL​e−N​ρL​(1+o​(1)),\mu_{2}\;=\;e^{-2(L-1)}\sinh^{2}(L-1)\;+\;(P-1)\,K_{L}\,e^{-N\rho_{L}}\bigl(1+o(1)\bigr),(27)σ2=μ2−μ12=(P−1)​KL​e−N​ρL​(1+o​(1)).\sigma^{2}\;=\;\mu_{2}-\mu_{1}^{2}\;=\;(P-1)\,K_{L}\,e^{-N\rho_{L}}\bigl(1+o(1)\bigr).(28)

The signal is order one; the per-pattern noise variance is exponentially small inNN. The whole storage phenomenon is the competition between these two facts,
made quantitative in the next section. Numerical values ofx∗x^{\ast},m∗m^{\ast},ϕL\phi_{L}andρL\rho_{L}for moderateLLare tabulated inB; the rate grows monotonically andρL∼L​log⁡2\rho_{L}\sim L\log 2.

## Remark 2(Annealed versus typical noise).

The wordannealedis used here in the sense familiar from the free
energy,log⁡𝔼​[Z]\log\mathbb{E}[Z]against𝔼​[log⁡Z]\mathbb{E}[\log Z], transposed from a partition function
to a moment: the quantity we evaluate is the disorder average of an exponential,𝔼​[e2​E^μ​⋯]\mathbb{E}[e^{2\hat{E}_{\mu}}\cdots], not the exponential of a disorder average. As
always, the two differ when the average is dominated by rare realisations, and
here it is. The Laplace evaluation of (22) is controlled by
the saddle𝒎^μ≡m∗​𝟏\bm{\hat{m}}_{\mu}\equiv m^{\ast}\bm{1}, an alignment of magnitude𝒪​(1)\mathcal{O}(1)between the cavity state and an unretrieved pattern; for a
genuine Rademacher pattern such an alignment is exponentially rare, the typical
cavity overlaps being𝒪​(N−1/2)\mathcal{O}(N^{-1/2}). The typical per-pattern noise is
accordingly parametrically smaller than (26), so the
variance (28) is a conservative overestimate of the noise and the
resulting capacity a conservative underestimate. Nothing is lost in rigour by
this (the bound is one-sided in the safe direction) but the gap widens
sharply withLL, and it is the reason the empirical retrieval in
Sections7–9tends to overshoot the annealed-noise
prediction atL≥3L\geq 3.

## 5Storage capacity

Within the Gaussian approximation the stability conditionXia>0X_{i}^{a}>0holds with
probabilityℙ​(Xia>0)=1−12​erfc​(μ12​σ2).\mathbb{P}\bigl(X_{i}^{a}>0\bigr)\;=\;1-\tfrac{1}{2}\,\mathrm{erfc}\!\Bigl(\tfrac{\mu_{1}}{\sqrt{2\sigma^{2}}}\Bigr).(29)

Requiring a per-spin error probability≤N−a\leq N^{-a},a>0a>0, so that the union
bound over theN​LNLpairs(i,a)(i,a)stays summable in the thermodynamic limit,
givesμ12/(2​σ2)≥a​log⁡N+𝒪​(log⁡log⁡N)\mu_{1}^{2}/(2\sigma^{2})\geq a\log N+\mathcal{O}(\log\log N).
Substituting the signal (20) and the variance (28),P≤1+e−2​(L−1)​sinh2⁡(L−1)2​a​KL​log⁡N​eN​ρL,{P\;\leq\;1+\frac{e^{-2(L-1)}\sinh^{2}(L-1)}{2\,a\,K_{L}\,\log N}\,e^{N\rho_{L}},}(30)

so that the leading exponential storage capacity isPc∼eN​ρL,ρL=L​[(L−1)−ϕL​(x∗)].P_{c}\;\sim\;e^{N\rho_{L}},\qquad\rho_{L}\;=\;L\bigl[(L-1)-\phi_{L}(x^{\ast})\bigr].(31)

Equivalently, the Mattis magnetisation after one sweep of the update
rule (16), one neuron per layer per step, simultaneously across
theLLlayers, until allNNsites have been visited once
(Algorithm1), readsm1(1)=erf​(e−(L−1)​sinh⁡(L−1)2​(P−1)​KL​e−N​ρL),{m_{1}^{(1)}\;=\;\mathrm{erf}\!\left(\frac{e^{-(L-1)}\sinh(L-1)}{\sqrt{2(P-1)\,K_{L}\,e^{-N\rho_{L}}}}\right),}(32)

which tends to unity as long as its argument diverges, i.e. as long asP​e−N​ρL→0P\,e^{-N\rho_{L}}\to 0. The capacity is therefore exponential inNN, with a rateρL\rho_{L}that increases with the widthLL,ρL∼L​log⁡2\rho_{L}\sim L\log 2asL→∞L\to\infty(B). Wider hetero-associative networks, binding more
layers at once, are exponentially more capacious.

## The intensive load

Because the capacityPc∼eN​ρLP_{c}\sim e^{N\rho_{L}}is exponential inNN, the
Amit–Gutfreund–Sompolinsky ratioP/NP/N-the intensive control parameter of
the classical theory- is itself exponentially large here and says nothing
about proximity to capacity. Two intensive quantities take its place. The first
is the exponential storage rateα:=log⁡PN,αc=ρL,\alpha\;:=\;\frac{\log P}{N},\qquad\alpha_{c}=\rho_{L},(33)

which measuresPPon its natural exponential scale and reaches capacity exactly
atα=ρL\alpha=\rho_{L}. The second, finer one is the reduced loadγ:=(P−1)​KL​e−N​ρLμ12=σ2μ12,\gamma\;:=\;\frac{(P-1)\,K_{L}\,e^{-N\rho_{L}}}{\mu_{1}^{2}}\;=\;\frac{\sigma^{2}}{\mu_{1}^{2}},(34)

namely the ratio of the noise variance (28) to the squared
signal (20), in terms of which the one-step overlap (32)
collapses onto the parameter-free profilem1(1)=erf​(1/2​γ)m_{1}^{(1)}=\mathrm{erf}(1/\sqrt{2\gamma}):γ→0\gamma\to 0is deep retrieval,γ≈1\gamma\approx 1the transition,γ≫1\gamma\gg 1failure. It isγ\gamma, notPP, that is comparable across layer sizes and widths, and
we use it as the intensive load throughout; the figures nonetheless keepPPon
the abscissa, where the exponential span of the capacity is directly visible.

Two remarks fix the meaning of this result before we test it. First, becausePcP_{c}is exponential inNN, the memory-degradation transition is visible only at
smallNN: already atN=64N=64,L=2L=2one hasPc∼e86P_{c}\sim e^{86}, out of
computational reach both in memory and in time, in a sense we make precise at
the end of Section3(Pc≈2.8×1037P_{c}\approx 2.8\times 10^{37}patterns,
whose per-sweep cost alone dwarfs any conceivable machine). Every simulation below therefore usesNNof order ten, where the transition falls in an accessible window. Second, as anticipated in
Remark2, the annealed prediction for the noise places the
transition at exponentially smallerPPthan the network actually
realises; the curves labelled “typical” below use the empirically calibrated
per-pattern variance and are the ones that track the data.

Figure1validates the exponential capacity and displays its
analytic backbone. Panel (a) compares the one-step
prediction (32) with the i.i.d. Monte-Carlo battery at widthL=2L=2and layer sizesN=8,…,12N=8,\dots,12: the recall plateaum1(1)≃1m_{1}^{(1)}\simeq 1gives way to the
disordered regimem1(1)≃0m_{1}^{(1)}\simeq 0whereP∼eN​ρ2P\sim e^{N\rho_{2}}, and the transition
marches to exponentially largerPPasNNgrows, exactly as (31)
demands. Panel (b) solves the symmetric saddle (23)
graphically, its inset showing the rateρL\rho_{L}climbing to itsL​log⁡2L\log 2asymptote.Figure 1:Exponential storage capacity.(a)One-step overlapm1(1)m_{1}^{(1)}versus the number of stored patternsPPfor the i.i.d. ensemble at widthL=2L=2and layer sizesN=8,9,10,11,12N=8,9,10,11,12: solid
lines are the closed form (32), markers Monte-Carlo
(mean±\pmstd over disorder realisations). The degradation transition
tracksPc∼eN​ρ2P_{c}\sim e^{N\rho_{2}}and shifts right withNN; because the capacity is
exponential inNN, only smallNNbrings it into an accessible window.(b)Graphical solution of the symmetric saddletanh⁡x∗=x∗/[2​(L−1)]\tanh x^{\ast}=x^{\ast}/[2(L-1)]: the non-trivial crossingx∗x^{\ast}(markers)
drifts towards2​(L−1)2(L-1)as the network widens. Inset: the noise rateρL=L​[(L−1)−ϕL​(x∗)]\rho_{L}=L[(L-1)-\phi_{L}(x^{\ast})]against the widthLL, compared toL​log⁡2L\log 2(dotted).

## 6Basins of attraction

Having established that the hetero-associative configuration (18) is a
fixed point up to an exponential load, we ask how far from it the dynamics can
start and still return. Following the protocol of the single-layer
model[6], we initialise in a corrupted archetype,σja​(0)=sja​ξj1,a,𝔼​[sja]=r∈(0,1],\sigma_{j}^{a}(0)\;=\;s_{j}^{a}\,\xi_{j}^{1,a},\qquad\mathbb{E}\bigl[s_{j}^{a}\bigr]=r\in(0,1],(35)

with maskssja∈{−1,+1}s_{j}^{a}\in\{-1,+1\}i.i.d. independently across sites and layers, so that every layer carries the same
initial overlapm1a​(0)=rm_{1}^{a}(0)=r, i.e. a Hamming distance per neurond=(1−r)/2d=(1-r)/2. The stability variable is againXia=ξi1,a​hiaX_{i}^{a}=\xi_{i}^{1,a}h_{i}^{a},
now evaluated at (35), and decomposes over patterns asXia\displaystyle X_{i}^{a}=∑μ=1PXi(μ|a),\displaystyle\;=\;\sum_{\mu=1}^{P}X_{i}^{(\mu|a)},(36)Xi(μ|a)\displaystyle X_{i}^{(\mu|a)}:=ξi1,a​eE^μ​sinh⁡(ξiμ,a​Fμa)​Φμ(\a).\displaystyle\;=\;\xi_{i}^{1,a}\,e^{\hat{E}_{\mu}}\,\sinh\!\bigl(\xi_{i}^{\mu,a}F_{\mu}^{a}\bigr)\,\Phi_{\mu}^{(\backslash a)}.

All details are inC; three facts organise the result.

First, the noise is blind to the corruption.Forμ≠1\mu\neq 1the relabelled
variablesuj(μ,c)=ξjμ,c​sjc​ξj1,cu_{j}^{(\mu,c)}=\xi_{j}^{\mu,c}s_{j}^{c}\xi_{j}^{1,c}are i.i.d. symmetric
Rademacher for everyrr, so each off-pattern contributes zero mean and
the same per-pattern varianceKL​e−N​ρLK_{L}\,e^{-N\rho_{L}}as in (28): the
noise floor does not move when the cue degrades.

Second, the signal pays a large-deviation cost.At the corrupted state the
recalled cavity overlaps concentrate atrrrather than11, and the typical
signal decays as1N​log⁡Xi(1|a)→N→∞a.s.−(L2)​(1−r2),\frac{1}{N}\log X_{i}^{(1|a)}\;\xrightarrow[N\to\infty]{\mathrm{a.s.}}\;-\binom{L}{2}\bigl(1-r^{2}\bigr),(37)

whereas the annealed signalμ1​(r)=𝔼​[Xi(1|a)]\mu_{1}(r)=\mathbb{E}[X_{i}^{(1|a)}]decays with the
strictly smaller rateΣL​(r)=\displaystyle\Sigma_{L}(r)\;={}(L2)​(1+ms2)\displaystyle\binom{L}{2}\bigl(1+m_{s}^{2}\bigr)(38)−L​[log⁡cosh⁡((L−1)​ms+ar)−log⁡cosh⁡(ar)]\displaystyle-L\Bigl[\log\cosh\bigl((L-1)m_{s}+a_{r}\bigr)-\log\cosh(a_{r})\Bigr]<(L2)​(1−r2),ar:=tanh−1⁡(r),\displaystyle\;<\;\binom{L}{2}\bigl(1-r^{2}\bigr),\qquad a_{r}=\tanh^{-1}(r),

wherems=ms​(r)m_{s}=m_{s}(r)solves therr-biased counterpart of (23),ms=tanh⁡((L−1)​ms+ar).m_{s}\;=\;\tanh\bigl((L-1)\,m_{s}+a_{r}\bigr).(39)

Third, the signal stays strictly positiveat every site: corruption only
shrinks it, so the transition remains a competition between an (exponentially
small) signal and the noise.

Writingμ1​(r):=𝔼​[Xi(1|a)]\mu_{1}(r):=\mathbb{E}\bigl[X_{i}^{(1|a)}\bigr]for the annealed signal at
corruptionrr(the same first moment as (20), now evaluated at the
corrupted initial state (35), so thatμ1​(r)=CL​(r)​e−N​ΣL​(r)\mu_{1}(r)=C_{L}(r)\,e^{-N\Sigma_{L}(r)}with the rate (38) and the
prefactorCL​(r)C_{L}(r)of Eq. (97), andμ1​(1)=μ1\mu_{1}(1)=\mu_{1}) and
repeating the signal-to-noise argument of Section5,m1(1)=erf​(μ1​(r)2​(P−1)​KL​e−N​ρL),m_{1}^{(1)}\;=\;\mathrm{erf}\!\left(\frac{\mu_{1}(r)}{\sqrt{2(P-1)\,K_{L}\,e^{-N\rho_{L}}}}\right),(40)

which tends to unity iffP​e−N​εL​(r)→0P\,e^{-N\varepsilon_{L}(r)}\to 0, with storage exponent
and capacityPc​(r)∼eN​εL​(r),εL​(r)=ρL−2​ΣL​(r),{\;P_{c}(r)\;\sim\;e^{N\varepsilon_{L}(r)},\qquad\varepsilon_{L}(r)\;=\;\rho_{L}-2\,\Sigma_{L}(r),\;}(41)

in the annealed scheme, andεLtyp​(r)=ρL−L​(L−1)​(1−r2)\varepsilon_{L}^{\mathrm{typ}}(r)=\rho_{L}-L(L-1)(1-r^{2})if the annealed signal rate is replaced by the typical one (37).
The quantitative load estimate, obtained as in (30) by requiring a
per-spin error probability≤N−a\leq N^{-a}, isP≤1+CL​(r)22​a​KL​log⁡N​eN​εL​(r),P\;\leq\;1+\frac{C_{L}(r)^{2}}{2\,a\,K_{L}\,\log N}\;e^{N\varepsilon_{L}(r)},(42)

with the prefactorCL​(r)C_{L}(r)of Eq. (97). The capacity stays
exponential at any corruption below threshold, the price of larger basins
being a smaller rate; above threshold one-step recall of the corrupted cue fails.
The thresholds,ΣL​(rc)=ρL2\displaystyle\Sigma_{L}(r_{c})=\tfrac{\rho_{L}}{2}(annealed),\displaystyle\text{(annealed)},(43)rctyp=1−ρLL​(L−1)\displaystyle r_{c}^{\mathrm{typ}}=\sqrt{1-\tfrac{\rho_{L}}{L(L-1)}}(typical),\displaystyle\text{(typical)},

are reported in Table2. Both criteria expose the same trade-off:
as the network widens the rate grows (ρL∼L​log⁡2\rho_{L}\sim L\log 2) but the basins
shrink. In the typical criterion1−rc2=ρL/[L​(L−1)]≃log⁡2/(L−1)→01-r_{c}^{2}=\rho_{L}/[L(L-1)]\simeq\log 2/(L-1)\to 0,
so the tolerated Hamming radius vanishes asdc≃log⁡2/[4​(L−1)]d_{c}\simeq\log 2/[4(L-1)]; the
annealed criterion saturates instead at the finite limitrc→2−1≈0.4142r_{c}\to\sqrt{2}-1\approx 0.4142(C). The annealed signalμ1​(r)\mu_{1}(r)is dominated by exponentially rare corruption masks, sorcannr_{c}^{\mathrm{ann}}is the optimistic estimate andrctypr_{c}^{\mathrm{typ}}the conservative one, and the
two bracket the finite-NNrecovery threshold.

Which of the two thresholds the finite-NNdynamics realises is an empirical
question, but one for which the theory already indicates the answer, and the
argument is worth giving before the simulations confirm it. The one-step
prediction (40) is built on the annealed first momentμ1​(r)=𝔼​[Xi(1|a)]\mu_{1}(r)=\mathbb{E}[X_{i}^{(1|a)}], the prescription that fixes the corrupted-cue capacity
in the single-layer model[6]. There the exponent is linear
in the masks, the annealed average factorises site by site, and annealed and
typical coincide, so no distinction arises. The multilayer exponent is instead
quadratic in the masks, which is what opens the gaprcann<rctypr_{c}^{\mathrm{ann}}<r_{c}^{\mathrm{typ}}, and one must ask which estimate the
averaged recall follows. The signal is carried by a single stored pattern, whose
collective cavity exponentE^1\hat{E}_{1}is one random variable per disorder
realisation, fluctuating by𝒪​(N)\mathcal{O}(\sqrt{N})in the
exponent (83). The retrieval statistic reported by both
theory and experiment is an average over independent dataset re-draws, and that
average is dominated by the favourable tail ofE^1\hat{E}_{1}, precisely the
configurations the annealed meanμ1​(r)\mu_{1}(r)weights. It is therefore the annealed
mean, not the smaller typical value, that the averaged recall tracks; the typical
prescription would become operative only in a strictN→∞N\to\inftylimit taken at
fixed sub-exponential load, a regime incompatible with the exponential storage
studied here. Sections7–9confirm this directly:
Figure2(a) shows the measured transition sitting on the annealed
curve, nearrcannr_{c}^{\mathrm{ann}}and far fromrctypr_{c}^{\mathrm{typ}}. Consistently
with Remark2, the residual gap is an overshoot
toward even larger basins –the per-pattern noise being itself an annealed
overestimate– so both corrections point the same way: the network is at least as
tolerant as the annealed signal-to-noise closed form, and never as pessimistic as
the typical bound. Atr=1r=1the two coincide and Section5is
recovered,εL​(1)=εLtyp​(1)=ρL\varepsilon_{L}(1)=\varepsilon_{L}^{\mathrm{typ}}(1)=\rho_{L}.

## Remark 3(Symmetric corruption versus the clamped-cue protocol).

The closed forms above corrupt every layer by the same amount,ra≡rr^{a}\equiv r.
The hetero-associative recall protocol of Sections7–9instead clamps theL−1L-1cue layers at their exact value and lets only the
target layer evolve from an uncorrupted start: an asymmetric limit of the family
above. The tilted saddle ofCcarries one bias fieldara=tanh−1⁡(ra)a_{r^{a}}=\tanh^{-1}(r^{a})per layer, one for each of theLLcorruption
levels; clamping the cue amounts to sendingara→∞a_{r^{a}}\to\infty(i.e.ma→1m^{a}\to 1) in theL−1L-1of them that belong to the cue layers. The coupled
system then collapses to the single scalar equationmT=tanh⁡[(L−1)+arT]m_{T}=\tanh\bigl[(L-1)+a_{r_{T}}\bigr]for the target layer, in place of the
symmetric (39). We use the symmetric curve as the
reference in Figure7(b) of Section8because the two agree to the accuracy of that plot, not because they are the
same object.LLρL\rho_{L}rcr_{c}(ann.)dcd_{c}(ann.)rctypr_{c}^{\mathrm{typ}}dctypd_{c}^{\mathrm{typ}}21.34700.31950.34020.57140.214332.07840.40320.29840.80850.095842.77260.41280.29360.87690.061653.46570.41400.29300.90920.0454106.93150.41420.29290.96070.0196Table 2:Basin-of-attraction thresholds: minimal initial overlaprcr_{c}(maximal
Hamming radiusdc=(1−rc)/2d_{c}=(1-r_{c})/2) compatible with an exponential storage capacity,
under the annealed and the typical signal estimates. AsL→∞L\to\infty,rcann→2−1r_{c}^{\mathrm{ann}}\to\sqrt{2}-1whilerctyp→1r_{c}^{\mathrm{typ}}\to 1.Figure 2:Basins of attraction: larger basins cost rate.(a)Basin recovery atL=3L=3(N=30N=30,P=3.5×104P=3.5\times 10^{4}, i.i.d. ensemble): one-step overlap after the dynamics versus the cue overlaprr,
against the corrupted-cue prediction (40) built on the
annealed signalμ1​(r)\mu_{1}(r)(solid) and on the typical signal
(dashed). The measured transition sits on the annealed curve, atr≈0.47r\!\approx\!0.47next torcannr_{c}^{\mathrm{ann}}, and nowhere near the typical
thresholdrctyp=0.81r_{c}^{\mathrm{typ}}\!=\!0.81: the annealed branch is the physical
one. If anything the data overshoot the annealed curve toward larger
basins, the annealed per-pattern noise being a conservative overestimate
(Remark2). The number of stored patterns is set from
the annealed ruleP=eN​εL​(r∗)/log⁡NP=e^{N\varepsilon_{L}(r^{\ast})}/\log Natr∗=0.5r^{\ast}=0.5,
exactly as in the single-layer reference[6].(b)The thresholdsrc​(L)r_{c}(L): the annealed branch saturates at2−1\sqrt{2}-1(dotted) while the typical branch climbs towards11, so basins
shrink as the network widens.(c)Capacity exponentεL​(r)\varepsilon_{L}(r)versus initial overlaprrforL=2,3,4L=2,3,4, in the annealed (solid) and typical (dashed) schemes; the
zero-crossing is the recovery thresholdrcr_{c}. Wider networks start higher
(largerρL\rho_{L}) but cross zero at largerrr.

## 7Structured data I: the Hidden Manifold Model

The theory of Sections2–6rests on one assumption:
theLLlayer datasets are mutually independent Rademacher vectors. Real
hetero-associative data are nothing of the sort. Their layers are correlated,
because cue and target are different views of one shared cause, and their
patterns lie near a low-dimensional manifold rather than filling the hypercube.
A second feature is a modelling choice on our part rather than a property forced
by the data: we take the target to be a many-to-one (surjective) function of the
cue. Nothing requires associations to be many-to-one in general; but restricting
to that case is what supplies a single-valued, well-defined rule to store, and it
is also the structure of the two problems we go on to treat, where many distinct
cues legitimately share one target. Before touching real data we therefore ask a
controlled question, with a generator in which manifold dimension and
surjectivity are knobs we turn:

When the stored patterns are drawn near a low-dimensional manifold, with a
many-to-one target, does the exponential capacity survive — and does
memorisation buy any generalisation to unseen points of the manifold?

The generator is the Hidden Manifold Model[31,29]. Each of
thePPstored indicesμ\muowns a latent codezμ∼𝒩​(0,ID)z^{\mu}\sim\mathcal{N}(0,I_{D})in
dimensionDD; theL−1L-1cue layers push it through a fixed random feature map,
one per layer, and threshold,ξμ,a=sign​(Fa​zμ/D)\xi^{\mu,a}=\mathrm{sign}(F^{a}z^{\mu}/\sqrt{D}), so that
cue layers of a given index share the latentzμz^{\mu}–the correlation that
makes hetero-association possible. The target layer is set by a surjective
rule: the firstnbitsn_{\mathrm{bits}}latent signs select one ofK=2nbitsK=2^{n_{\mathrm{bits}}}fixed prototypesρk​(zμ)\rho_{k(z^{\mu})}, so whole regions of latent space collapse to
a common target. The two counts are distinct and both essential:PPdefines the load
(how many cues are stored),KKthe number of target prototypes, and the map is surjective precisely becauseP≫KP\gg K, withP/KP/Kthe mean number of cues per prototype. The single geometric control
parameter is the aspect ratioαD=D/N∈(0,1]\alpha_{D}=D/N\in(0,1]:
smallαD\alpha_{D}is a
tightly curved, strongly correlated manifold;αD=1\alpha_{D}=1is the near-i.i.d. edge of the same pipeline. Full construction (the region mapk​(z)k(z), the
prototypes, the symmetric-target control, and the held-out-region control) is
inF.

A convention on the numbers, valid for this section and the two that follow: all
empirical quantities stemming from the numerical experiments are reported as
means±\pmone standard deviation over independent dataset re-draws, each
re-draw itself an average over evaluation trials, with the seed counts listed inI.

## The data are a sign-image of a geometry

The first thing to verify is that the manifold is really there. The diagnostic is
the pairwise pattern overlapmμ​ν=1N​∑iξiμ,a​ξiν,am_{\mu\nu}=\frac{1}{N}\sum_{i}\xi_{i}^{\mu,a}\xi_{i}^{\nu,a},
the cosine between two stored codes in a layer. For sign patterns it concentrates
on the arcsine law𝔼​[mμ​ν]=(2/π)​arcsin⁡ρz\mathbb{E}[m_{\mu\nu}]=(2/\pi)\arcsin\rho_{z}, withρz=⟨zμ,zν⟩/(‖zμ‖​‖zν‖)\rho_{z}=\langle z^{\mu},z^{\nu}\rangle/(\|z^{\mu}\|\|z^{\nu}\|)the latent cosine
similarity: an exact, parameter-free curve (derived from Grothendieck’s identity
inF). Figure3(a) shows the measured
overlaps lying on it, turning “the data lie near a manifold” into a verified
fact rather than a hope. The same panel reads off the price of structure: the
standard deviation of the cue overlap crosses over from the i.i.d. value1/N1/\sqrt{N}atαD=1\alpha_{D}=1to the much larger(2/π)/D(2/\pi)/\sqrt{D}asαD→0\alpha_{D}\to 0. A smaller manifold makes the stored patterns more
correlated (more overlapping than Rademacher, wheneverD<(2/π)2​ND<(2/\pi)^{2}N), which is
exactly the extra noise that the clean theory does not carry, and exactly why
capacity should fall as the manifold shrinks.Figure 3:The data manifold.(a)Pattern overlapmμ​νm_{\mu\nu}against latent similarityρz\rho_{z}(density) with binned means (markers) lying on the arcsine law2π​arcsin⁡ρz\frac{2}{\pi}\arcsin\rho_{z}(black); inset, a 2D PCA embedding of the cue
patterns coloured by target region, showing the surjective clustering.(b)The cue-overlap standard deviation crosses over from the i.i.d. value1/N1/\sqrt{N}atαD=1\alpha_{D}=1to a strongly correlated regime asαD→0\alpha_{D}\to 0, tracking the manifold prediction.(c)The distinct-pattern fraction (left) collapses at smallαD\alpha_{D}while the mean overlap (right) rises: apparent stability at smallddis pattern
collision, not capacity.

## The exponential capacity survives, and fails gracefully

Figure4(a) scans the loadPPat fixed layer sizeN=10N=10. At low
load the i.i.d. ensemble retrieves perfectly and tracks the finite-NNtheory (32) to within finite-size noise (with the transition sitting
at largerPPthan the annealed estimate, as Remark2anticipates); the manifold ensembles sit
slightly below, the correlation of Figure3(b) acting as an
extra noise term on top of thee−N​ρLe^{-N\rho_{L}}floor, and the plateau drops asαD\alpha_{D}falls, the practical form of the “capacity decreases with manifold
dimension” statement. The high-load behaviour is more interesting, and at first
sight paradoxical: past capacity the i.i.d. overlap decays toward zero, while
the manifold overlap saturates on a positive floor. The floor is not
superior retrieval. It is the structural self-overlap𝔼​|mμ​ν|≈0.30\mathbb{E}|m_{\mu\nu}|\approx 0.30of the manifold: once the network can no longer
resolve individual memories it relaxes to the manifold rather than to a
random spurious state, and keeps the residual overlap that any two manifold
points share. Read against the measured floor, the manifold curve confirms rather
than contradicts the theory, and confirms that failure is graceful.

Part of the early saturation at smallαD\alpha_{D}so is not a retrieval effect at all
but a counting one, and the inset of Figure4(a) isolates
it. It tracks the collision rate(P−Punique)/P(P-P_{\mathrm{unique}})/P: the fraction of thePPdrawn latents whose sign-imagesign​(F​z)\mathrm{sign}(Fz)duplicates a pattern already in
the store. Becausez↦sign​(F​z)z\mapsto\mathrm{sign}(Fz)can realise at mostC​(N,D)=2​∑k<D(N−1k)C(N,D)=2\sum_{k<D}\binom{N-1}{k}distinct codes (Cover’s count for a central hyperplane arrangement,F),
the codebook is finite and collisions are inevitable oncePPbecomes comparable
toC​(N,D)C(N,D): atN=10N=10this count is9292,764764and10241024forαD=0.3,0.6,1.0\alpha_{D}=0.3,0.6,1.0, and the measured rate crosses one half atP≈62P\approx 62,325325and605605respectively, in the same order and of the same
magnitude. The consequence for panel (a) is a bookkeeping one that we
insist on because it is easy to misread in the opposite direction: beyond that
load the network is no longer storing new memories, only additional copies of the
few it can address, so the overlap plateau overstates rather than understates the
number of distinct memories held.
The distinct-pattern fraction
(Figure3(c)) must be read together with the stability score;
the honest “capacity falls withDD” statement is the one taken from the
matched-load transition of Figure4(a), not from raw
stability.Figure 4:Capacity, width and surjective compression.(a)One-step overlap versus loadPP(N=10N=10) for the i.i.d. ensemble
and Hidden-Manifold ensembles at severalαD\alpha_{D}: capacity falls as the
manifold shrinks, and past capacity the manifold state relaxes onto its
structural floor (dotted) rather than a spurious pattern. Inset, same abscissa
and colours: the collision rate(P−Punique)/P(P-P_{\mathrm{unique}})/P, the fraction of
drawn latents that land on a pattern already stored. It leaves zero at a load
of the order of Cover’s countC​(N,D)C(N,D), earliest for the smallestαD\alpha_{D}, and the onset of each curve’s rise coincides with the onset of
the corresponding overlap plateau.(b)Target-recall rate versusPPfor widthL=2,3,4L=2,3,4at matched layer
size; the transition shifts to largerPPwithLL(dashed: predictedPcP_{c}), so
more cue layers tolerate exponentially more memories.(c)Recall versus surjective compressionP/KP/Kat several cue-corruption
levelsrr: prototypes backed by more cue patterns have deeper basins.

## Basins, and which of the two thresholds is realised

At a matched sub-critical load the basins tell the complementary story
(Figure2(a)). We sweep the cue overlaprratL=3L=3, fixing the
load from the annealed ruleP=eN​εL​(r∗)/log⁡NP=e^{N\varepsilon_{L}(r^{\ast})}/\log Nso that the
annealed threshold lands at a chosenr∗r^{\ast}, the same operational recipe used
in the single-layer reference[6]. The measured transition
tracks the annealed one-step curve (40) and sits atr≈0.47r\approx 0.47, right next torcannr_{c}^{\mathrm{ann}}, and nowhere near the
typical valuerctyp=0.81r_{c}^{\mathrm{typ}}=0.81of Table2: the favourable
corruption masks that dominate the annealed signal are exactly the ones sampled
by the disorder average, so it is the annealed –the optimistic– branch that is
physical. This settles the question left open in Section6, in the
opposite sense to a naive “rare events do not matter” expectation: because the
signal rides on a single pattern, its rare-but-favourable fluctuations are not
averaged away. If anything the data overshoot the annealed prediction toward
still larger basins, the per-pattern noise being itself an annealed overestimate
(Remark2), so both the corrupted-cue signal and the noise
push the same way. The i.i.d. basin is the cleaner and deeper one; the manifold
basin rides the structural self-overlap floor at strong corruption, exactly as in
panel (a).

## Width helps recall

Because the rateρL\rho_{L}grows with the widthLL, more cue layers should tolerate more
stored patterns. Figure4(b) confirms it directly: at matched
layer size the target-recall curves shift to largerPPasLLgoes from22to44,
each transition sitting near its predictedPc∼eN​ρLP_{c}\sim e^{N\rho_{L}}. The case that
matters for the receptor data of Section8–two cue chains
driving a third layer,L=3L=3– is the middle curve, and having both cues rather
than one is worth an order of magnitude in tolerated load.

## The headline: memorisation without much generalisation

Beyond memorisation there is a second question, and it is the one the model was
not built to answer: whether a cue drawn from a never-stored latent is routed to
the correct target prototype. We hold two of eight latent regions out
by construction and measure four rates: memorisation (stored cues),
generalisation (fresh cues from seen regions), a novel-region control (fresh cues
from held-out regions), and chance1/nseen=0.1671/n_{\mathrm{seen}}=0.167. The three
comparisons together are what make the reading unambiguous
(Figure5). Memorisation is high. Generalisation sits
clearly above chance, so the manifold structure is being used, and climbs
with coverageP/nseenP/n_{\mathrm{seen}}, from≈0.21\approx 0.21at the sparsest sampling
toward≈0.39\approx 0.39, approaching memorisation only in the densely sampled limit,
where the stored cues tile the manifold so finely that the manifold itself acts as
the attractor. The novel-region control fixes the interpretation: its rate never
leaves chance, across the1212loads scanned it beats chance in none (Wilcoxon
signed-rank on the per-load means, two-sidedp≈4.9×10−4p\approx 4.9\times 10^{-4}), whereas
generalisation beats chance in all1212(p≈2.4×10−4p\approx 2.4\times 10^{-4}) and beats the
novel-region control at every load (sign test,p≈2.4×10−4p\approx 2.4\times 10^{-4}). The
generalisation signal is therefore real rather than an encoding artefact, and at
the same time modest: an exponential ability to memorise does not, by itself,
confer a comparable ability to classify unseen inputs, short of sampling the
manifold densely enough that classification collapses back to memory. This is the
central empirical fact of the paper, and the next section shows it survives
contact with real data.Figure 5:Memorisation without generalisation.(a)Memorisation, generalisation and novel-region recall versus load
(K=8K=8regions, two held out), with chance (dotted) and majority (dashed).(b)Excess over chance versus coverageP/nseenP/n_{\mathrm{seen}}:
generalisation grows and stays well above the novel-region control, which never
leaves chance: the signal is real but far below memorisation.(c)AsαD→1\alpha_{D}\to 1the manifold retrieval descends onto the i.i.d. theory (dashed lines); at smallαD\alpha_{D}collisions inflate the apparent
overlap above it.

## 8Structured data II: real T-cell receptors

We now replace the synthetic manifold with immunological repertoires. A T-cell
receptor recognises an antigen through the paired hypervariable loops of its two
chains, theα\alpha- andβ\beta-CDR3; the antigen is a short peptide, the
epitope. The map from receptor to epitope is exactly the object the model is
built for: a hetero-association from two cue layers to a target, and a strongly
surjective one, since many unrelated receptors converge on the same epitope. We
take the triples(α​-CDR3,β​-CDR3,epitope)(\alpha\text{-CDR3},\ \beta\text{-CDR3},\ \text{epitope})from VDJdb[51,13], assign them to the three layersa∈{1,2,3}a\in\{1,2,3\}, and run the same battery as in Section7.
Table3fixes the dictionary between the model and the biology.Model (theory)Biology / real dataLayersLLthe two receptor chains (α\alpha,β\beta) and the target epitope (L=3L=3)Independent Rademacher patternsAtchley factors passed through a SimHashSurjective many-to-one mapmany unrelated receptors converging on one epitopeTable 3:The model-to-biology dictionary for the VDJdb experiments.

## Making the problem well posed

Two things must be fixed before the network sees anything, and both are
prescribed by the theory. First, by Remark1the stored map
must be a single-valued function: a receptor mapped to two different epitopes is
not a hetero-association but a contradiction, and (17) says what
the network would return in its place. Starting from137,484137{,}484raw records we
apply a lean biological clean (human, curation score≥1\geq 1, pairedcomplex.id, valid sequences) and then afunction filterkeeping
only receptors mapped to a single epitope, which leaves1,0521{,}052clean triples
over220220epitopes, strongly surjective, up to146146receptors per epitope
with120120singletons (Figure6(a,b)): the immunological
image of the convergent recognition the model is meant to store. Second, the
sequences must become{−1,+1}N\{-1,+1\}^{N}patterns without smuggling in a learned
representation. We use Atchley factors[12], five standardised
biophysical numbers per residue placed positionally onto a fixed-length vector,
fed to a locality-sensitive SimHash[20]: a fixed, deterministic
standardise→\toPCA-whiten→\toGaussian→\tosign map, fitted per layer on the
training split, whose bits are balanced and near-orthogonal and whose Hamming
overlap obeys the same arcsine law𝔼​[mμ​ν]=1−2π​arccos⁡c\mathbb{E}[m_{\mu\nu}]=1-\tfrac{2}{\pi}\arccos cas the
manifold model, in the biophysical cosinecc(Figure6(c,d); full funnel and encoder inG). The outcome is quantitatively Rademacher-like (per-bit balance≈0.03\approx 0.03, mean absolute pattern overlap≈0.10\approx 0.10on
the receptor layers) close enough to the theory’s ideal that the i.i.d. predictions are usable as a yardstick.Figure 6:From database to binary patterns.(a)The cleaning funnel:137,484137{,}484raw records reduce to1,0521{,}052clean triples once the function filter enforces a single-valued
receptor→\toepitope map.(b)Epitope cluster sizes (rank–frequency): strongly surjective, up
to146146receptors per epitope, with120120singletons.(c)Near-Rademacher encoding: per-bit imbalance and mean pattern
overlap by layer, against the i.i.d. value1/N1/\sqrt{N}; the receptor layers are
close to ideal, the small epitope alphabet less so.(d)The SimHash law: the binned-mean pattern overlap (markers) follows
the arcsine shapemμ​ν=1−2π​arccos⁡cm_{\mu\nu}=1-\tfrac{2}{\pi}\arccos c(black) in the cosine
similarityccof the Atchley feature vectors; individual pairs (density)
scatter broadly around it, as expected for a finite hash.

## Real data behaves like the theory

The most striking result requires no fitting. We corrupt a stored receptor and
watch the dynamics recover it, sweeping the initial overlaprr(Figure7(b)). The real-data basin curve is essentially
indistinguishable from the i.i.d. one, and both sit on the finite-NNprediction (40): recovery is total forr≳0.4r\gtrsim 0.4and
collapses through a sharp transition nearr≈0.2r\approx 0.2–0.30.3. Correlated,
surjective, biologically generated patterns thus have basins of attraction that
the idealised Rademacher theory describes to within finite-size noise: the
independence assumption of Section2, violated in every literal
respect by these data, is benign for retrieval.

## Two chains recall the antigen, essentially without error

The biologically central task is(α,β)→epitope(\alpha,\beta)\to\text{epitope}: given both
receptor chains, name the antigen. Figure7(a) reports a
recall rate of0.9994±0.0010.9994\pm 0.001: perfect memory up to statistical noise. A single
chain is not enough (α→epitope\alpha\to\text{epitope}andβ→epitope\beta\to\text{epitope}recover only0.790.79and0.830.83) so the two chains are genuinely
complementary, each supplying information the other lacks, and only their
conjunction pins the epitope. The reverse, over-determined direction(β,epitope)→α(\beta,\text{epitope})\to\alpharecalls theα\alphachain perfectly
(1.001.00), as an invertible cue should. As a stored associative memory of known
receptor–epitopebindings(experimentally confirmed pairs, each one a
receptor observed to physically recognise and lock onto that particular peptide) the network is essentially flawless atL=3L=3on real data.Figure 7:Near-perfect memory, modest generalisation on real data.(a)Recall for the biological tasks: both chains name the epitope
essentially without error, each single chain only partially, and the
over-determined(β,epitope)→α(\beta,\text{epitope})\to\alphaperfectly.(b)Basins of attraction: the real-data recovery curve coincides with
the i.i.d. one and with the finite-NNtheory (black); the hetero-associative
cue(α,β)→epitope(\alpha,\beta)\to\text{epitope}needs a larger overlap to lock on.(c)Generalisation to unseen receptors versus a label-permutation null:
the true signal (≈0.10\approx 0.10) is about twice the null and well above chance,
real but modest.(d)Per-epitope generalisation versus cluster size. Each point is one
epitope: its abscissa is the number of receptors carrying it, its ordinate the
fraction of that epitope’s held-out receptors routed back to it. Epitopes backed
by more stored receptors generalise better, because a denser cluster tiles more
of the receptor manifold around the shared target. Inset: top-kkaccuracy of
retrieving the correct epitope for a new receptor.

## The headline again, sharper: memory yes, prediction barely

The database records a finite list of confirmed bindings; the biological question
is whether that list determines the rest. Does storing the known bindings let the
network predict the epitope of a receptor appearing in no stored pair, that
is, name the peptide a never-seen receptor would bind? We hold out a quarter of
the receptors of each epitope and
test recall on them. Memorisation of the training receptors is near-perfect
(0.9970.997); generalisation to held-out receptors is0.110.11–0.140.14, rising with
the number of receptors per epitope, against a chance level of0.0050.005: roughly
twenty times chance, and about twice a label-permutation null (true
generalisation≈0.10\approx 0.10versus null≈0.048\approx 0.048;
Figure7(c)), a gap that a Mann–Whitney test on the66true against the2020permuted replicates confirms is not incidental (one-sidedp≈9×10−6p\approx 9\times 10^{-6}, equivalentlyz≈3.2z\approx 3.2). The signal is therefore
real: the encoding does place receptors of the same epitope in neighbouring
regions of pattern space, and the network exploits it. But it is small. Top-1
retrieval of the correct epitope for a new receptor is0.090.09(Figure7(d)), an order of magnitude below the network’s
own memorisation. The pattern is the one of Section7, now on real
data: an exponential, near-perfect associative memory whose classification of
novel inputs is real but modest.

This is not a verdict on the model. Predicting TCR specificity from sequence
alone is a hard problem in general, and the next section shows that the same
network, storing the same way, generalises five times better on a domain whose
encoder co-locates same-target cues more tightly. What the VDJdb experiment pins
down is what an exponential hetero-associative memory does and does not deliveron this encoding.

## 9Structured data III: natural language, and the universality of the
mechanismFigure 8:The same network on natural language (L=2L=2,N=128N=128,
CLINC150).(a)PaCMAP embedding of the encoded utterances (grey: all150150intents). Four intents are highlighted: the semantically affine paircredit score/improve credit score, whose clusters coincide and
whose target codes overlap atmμ​ν=0.88m_{\mu\nu}=0.88, and two unrelated controls at|mμ​ν|≤0.06|m_{\mu\nu}|\leq 0.06from them.(b)The SimHash law: binary pattern overlap against feature cosine,
with the arcsine prediction (black); the encoding is near-Rademacher
(annotated values).(c)Capacity scan: the one-step overlap sits on the theoretical
plateau for real and i.i.d. patterns alike over the whole accessible range ofPP(the predicted capacity beinge172e^{172}), while the utterance→\tointent
routing decays under interference between cues sharing a target.(d)Basins: real and i.i.d. recovery curves coincide and follow the
finite-NNprediction (40); the transition sits belowrcannr_{c}^{\mathrm{ann}}and far fromrctypr_{c}^{\mathrm{typ}}.(e)Recall on the language tasks: the forward (surjective) direction,
the ill-posed reverse one, memorisation, generalisation to unseen utterances,
top-1 retrieval, the out-of-scope control and chance.(f)Cue content: intent recall against the number of revealed leading
tokens; half the intents are recovered from5.65.6words.

Two datasets from a biological or geometric generator leave one question open:
how much of what we have measured belongs to the network and how much to the
domain? The way to separate them is to change the domain as far as possible while
changing nothing else.

CLINC150[42]labels short user utterances with one of150150intents. It is the linguistic image of the receptor problem, a single-valued,
strongly surjective, many-to-one map, utterance→\tointent, and shares with it
nothing else: no alphabet, no metric, no generative model, no notion of distance
in common, only the structure Remark1demands. The same
function filter removes just44ambiguous utterances, leaving22,49122{,}491records over150150intents with a
compressionP/K≈150P/K\approx 150cues per target, against≈5\approx 5for VDJdb. We
takeL=2L=2(utterance, intent), which makes the closed-form numbers of
Sections5–6directly usable (ρ2=1.347\rho_{2}=1.347,
annealedrc=0.3195r_{c}=0.3195, typicalrc=0.5714r_{c}=0.5714, noLL-dependent inversion)
and binarise utterances with a word- and character-level TF–IDF map, a fixed,
learning-free representation playing the role the Atchley factors played on
receptors, passed through the same PCA-whitening-plus-SimHash binariser
(H).

## The memory side is the same theory, verbatim

Figure8collects the battery. The encoding is again
near-Rademacher: per-bit imbalance0.0290.029and mean overlap⟨|mμ​ν|⟩=0.097\langle|m_{\mu\nu}|\rangle=0.097against the i.i.d. value1/N=0.0881/\sqrt{N}=0.088atN=128N=128, with the pattern overlap following the arcsine law1−2π​arccos⁡c1-\tfrac{2}{\pi}\arccos cin the feature cosine, panel (b), exactly as in
Figure6(d). The capacity scan, panel (c), sits on the
theoretical plateau over the whole accessible range: atN=128N=128,L=2L=2the
predicted capacity isPc∼eN​ρ2=e172P_{c}\sim e^{N\rho_{2}}=e^{172}, and the one-step overlap
duly remains1.0001.000to four digits for real and i.i.d. patterns alike fromP=30P=30toP=6000P=6000. What does move is the hetero-associative routing, decaying
from1.001.00to0.750.75over the same span: interference among the growing number
of cues that share a target, not loss of memory. The basins, panel (d),
reproduce the VDJdb finding on data that have nothing to do with it: real and
i.i.d. curves lie on top of each other and on (40), with the
transition atr≈0.21r\approx 0.21–0.240.24, belowrcannr_{c}^{\mathrm{ann}}and far from
the typical threshold, once more overshooting the annealed prediction towards
larger basins in the direction Remark2anticipates.

## The geometry the encoder builds

Panel (a) makes visible what the arcsine law states. In a PaCMAP embedding of
the encoded utterances each intent is a tight cluster (median radius0.30.3,
against a median inter-centroid distance of10.310.3); the semantically affine
paircredit score/improve credit score, the most similar of the11,17511{,}175, falls on top of itself (centroids1.91.9apart, target codes
overlapping atmμ​ν=0.88m_{\mu\nu}=0.88) while two unrelated intents sit at|mμ​ν|≤0.06|m_{\mu\nu}|\leq 0.06from them and from each other. Affine targets share a
region of pattern space and unrelated ones do not; it is this co-location, not
the storage rule, that generalisation feeds on.

## What changes, and what does not

Panel (e) is the comparison the experiment was built for. The
hetero-associative task utterance→\tointent recalls at0.780±0.0220.780\pm 0.022;
memorisation of stored utterances is0.717±0.0300.717\pm 0.030; generalisation to unseen
utterances of a seen intent is0.584±0.0090.584\pm 0.009, against a chance level of1/150=0.00671/150=0.0067, an out-of-scope control at0.0140.014and a label-permutation
null of0.013±0.0020.013\pm 0.002over2020permutations (z≈3.0×102z\approx 3.0\times 10^{2}). Top-1
retrieval of the correct intent for a fresh utterance is0.527±0.0090.527\pm 0.009, rising
to0.6490.649at top-10; on receptors the corresponding numbers were0.110.11and0.090.09. Storage rule, dynamics and closed-form basins are identical in the two
cases; only the encoder differs, and generalisation differs with it by a factor
of five.

One ablation settles the attribution beyond argument. Replacing the TF–IDF
features by a text-blind random map (a deterministic hash of each utterance to
a fixed Gaussian vector, everything else unchanged, so that lexically similar
utterances receive unrelated codes) leaves memorisation at0.349±0.0230.349\pm 0.023and sends generalisation to0.008±0.0020.008\pm 0.002, exactly the chance level
(H). The network still stores; it simply has nothing to
interpolate between. Widening the representation, conversely, buys
generalisation monotonically:0.35,0.50,0.58,0.630.35,0.50,0.58,0.63atN=32,64,128,256N=32,64,128,256,
tracking the fall of the mean pattern overlap towards its i.i.d. floor1/N1/\sqrt{N}. Generalisation is a property of the map into pattern space; the
storage rule contributes the memory, and only the memory.

The deliberately ill-posed direction says the same thing from the other end.
Cueing with the intent and asking for an utterance recalls at0.3620.362: the
reverse of a surjection is not a function, and Remark1predicts that the target layer returns the componentwise majority of theq≈20q\approx 20utterances sharing that intent atP=3000P=3000, whose overlap with any
one of them would be2/π​q≈0.18\sqrt{2/\pi q}\approx 0.18for independent codes. The
measured overlap is0.414±0.0170.414\pm 0.017, more than twice as large, because
paraphrases of one intent arenotindependent: the encoder places them
close, so their majority stays close to each. The non-invertibility is exactly
as severe as the encoder’s clustering leaves it.

## How much cue is enough

Panel (f) puts the basin question in units a reader of the data can check: we
reveal only the leading words of the utterance and re-encode, instead of
flipping random bits. Recall grows smoothly from0.1250.125at1.81.8revealed
tokens to0.7680.768at the full8.38.3, crossing one half at5.65.6: two thirds
of a sentence suffice to fall inside a basin, and the smoothness of the curve is
the linguistic image of the graceful degradation predicted under bit
corruption.

## 10Discussion

We set out to make hetero-association a first-class citizen of the exponential
associative-memory family, and to find out what such a network does on real
data. The theory answers the first question cleanly. An energy built from the
product of per-layer Mattis overlaps has the perfectly aligned
hetero-associative state as a fixed
point of its zero-temperature dynamics up to a loadPc∼eN​ρLP_{c}\sim e^{N\rho_{L}}, with a
rateρL=L​[(L−1)−ϕL​(x∗)]\rho_{L}=L[(L-1)-\phi_{L}(x^{\ast})]that we compute in closed form and that
grows likeL​log⁡2L\log 2: each further layer buys exponentially more capacity. The one structural
novelty relative to the auto-associative case -that the per-pattern noise no
longer factorises over sites- is resolved by a large-deviation saddle point on
the symmetric ray of layer magnetisations, and the same machinery, tilted, yields
the basins: enlarging them lowers the rate but never removes its exponential
character, with an explicit annealed/typical dichotomy that the simulations then
settle in favour of the conservative branch. The same field computation delimits
what such an energy can hold at all: the stored rule must be a surjective
function of the cue (Remark1), a cue withqqtargets being
answered by their componentwise majority rather than by any of them, and a
target with no cue occupying capacity it can never be addressed by.

## An excellent memory, and geometry-limited generalisation

The experiments answer the second question in two parts. First, the memory side
is unambiguous and domain-independent: on the Hidden Manifold Model, on real
VDJdb triples and on natural-language intent data alike, the network stores an
exponential number of structured, surjective associations and recalls them
robustly, with basins that match the idealised i.i.d. theory even when the
patterns are correlated and biologically generated, and the two receptor chains
name their epitope essentially without error. Second, the classifier side,
routing an unseen cue to the right target, is real but bounded, and its size
is governed by the encoding rather than by the storage rule: modest on receptor
sequences, five times larger on paraphrased text, in both cases growing as the
manifold is sampled densely enough to approach the memory itself. This is
consistent with, and sharpens, recent findings that data geometry controls
whether modern Hopfield networks generalise[47,36]: in the
binary exponential model, memorisation is exponential and essentially free,
while generalisation is bought from the geometry of the representation.

The asymmetry is worth stating as a design fact rather than as a shortcoming. A
high-capacity associative memory of this family is built first of all to
remember, that is to serve as a massive content-addressable repository, and this
one does so exceptionally well, while extending the auto-associative scenario
to the more realistic hetero-associative one, where cue and target are distinct
objects. WithNNbinary neurons per layer there are2N2^{N}configurations, and
a device that files an exponential fraction of them under their own content is
not the sort of object from which strong extrapolation should be expected. How
much it also generalises is a question about the encoder, not about the storage
rule.

## Domain universality, and where generalisation comes from

Nothing in the construction is specific to a domain: by
Remark1any single-valued, surjective, many-to-one map is a
candidate, and nothing else is. Section9pushes that claim as far
as we can: a natural-language corpus shares with a T-cell repertoire no
alphabet, no metric and no generative model, only the surjective structure, and
on it the sameL=2L=2closed forms describe capacity and basins with not one
refitted constant. The classifier side, however, does not follow the mechanism.
Generalisation to unseen utterances of a seen intent reaches0.580.58against a
memorisation of0.720.72; on receptors the corresponding figures are an order of
magnitude smaller. Paraphrases of one intent share words, so TF–IDF places them
close together and a single stored utterance already carves a basin that catches
many others; distinct receptors of one epitope share little primary sequence, so
the biophysical encoder scatters them and only dense sampling of the epitope’s
receptor cloud builds a basin. What generalises is not the memory but the
encoder’s ability to co-locate cues that share a target: a property of the
representation, not of the storage rule.

The surjective many-to-one principle travels further still: a continual,
privacy-preserving setting where clients contribute low-rank Hebbian updates
towards shared archetypes[8], and a
continuous-signal domain –multi-channel sleep polysomnography– encoded through
the same PCA-whitening-plus-SimHash pipeline ofGinto a
tri-layer hetero-associative memory[41], both point the
same way: the encoder, not the domain, is what the exponential mechanism cares
about.

## The single-layer sibling

Danalyses aℤ2\mathbb{Z}_{2}-symmetric,
squared-overlap variant atL=1L=1, whose energy penalises1−mμ21-m_{\mu}^{2}rather than1−mμ1-m_{\mu}. It restores the global spin-flip symmetry the linear model breaks,
requires the same saddle-point treatment as the multilayer noise, and has a
storage rateρ≈0.6928\rho\approx 0.6928that sits closer to the absolute ceilinglog⁡2\log 2than the linear model’sρlin≈0.6750\rho_{\mathrm{lin}}\approx 0.6750, a clean example of
how the shape of the exponent trades basin width against capacity. Its saddle
coincides with theL=3L=3specialisation of the multilayer analysis, a structural
correspondence we find suggestive.

## Limitations and outlook

The analysis is one-step and zero-temperature: it certifies fixed points and
one-update recovery, not the full multi-step relaxation or a finite-temperature
free-energy landscape, and the Gaussian signal-to-noise scheme is an
approximation whose corrections we have bounded but not resummed. The
independence of layer datasets is an idealisation; the experiments quantify its
violation but a theory of the correlated case –where a shared latent couples
the layers, as in the data– remains open, and is the natural bridge to the
random-features and hidden-manifold Hopfield
programme[31,47,36]. Two further questions we set
aside here are pursued elsewhere. First, nothing in Sections2–6rules out achimericfixed point in which distinct layers lock onto
different pattern indices; a companion architecture removes such states by
construction through a consensus mechanism over the shared
memory[4], rather than by analysing their
basin of attraction within the present energy. Second, the noise floorKL​e−N​ρLK_{L}e^{-N\rho_{L}}that limits capacity here is a property of the raw Hebbian
kernel; an off-linedreaming[26,1]step that reweights that kernel’s
eigenmodes before retrieval improves memorisation and can disentangle mixture
states in theLL-layer setting[17], suggesting that the
rateρL\rho_{L}of Section5is a property of the construction as
given, not a hard ceiling on what a hetero-associative energy of this family
can achieve. A further limitation, easily
missed because the storage rateρL\rho_{L}reads as an unqualified gain, is that
it is bought at an equal and exponential price: one parallel sweep of
Algorithm1costsΘ​(N​L​P)\Theta(NLP)in both time and memory
(Section3), so operating at any fixed fraction ofPc∼eN​ρLP_{c}\sim e^{N\rho_{L}}costsΘ​(N​L​eN​ρL)\Theta(NL\,e^{N\rho_{L}}), the identical rate that
measures capacity. Every architecture in this exponential family inherits the
same trade, a useful reminder that the capacity theorem describes the fixed
points of anN→∞N\to\inftylimit rather than any regime a real machine can
occupy;Egives the arithmetic. Finally, the bounded-generalisation
finding invites a sharper question than we have answered: is there a principled
modification of the exponent, or of the encoding, that converts some of the
exponential memorisation budget into generalisation, without collapsing to the
trivial dense-sampling limit? We believe the tools assembled here, theory and
battery together, are the right place to ask it.

## Data and code availability

The simulation engine used to generate the Monte Carlo results reported
throughout this paper is available athttps://github.com/andrea-ladiana/exponential-lam-engine/.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or
personal relationships that could have appeared to influence the work
reported in this paper.

## Acknowledgements

E.A. acknowledges Sapienza Università di Roma (RM124190CB1269EB)
A.B. acknowledges support from Sapienza University of Rome, Prot. n. RM12519999AB8CA9,Neural Networks and Learning Machines: asymptotic behaviors on structured datasets, and acknowledges support from INFN, Sezione di Roma 1.
E.A, A.B., A.Ladiana and A.Lepre are members of the GNFM group within INdAM which is acknowledged.

The authors acknowledge the use of the Lagrange Multi-GPU Server at the Department of Mathematics, Sapienza University of Rome, for computational resources supporting this work.

## Appendix AFirst and second moments at the recalled state

This appendix collects the detailed computations summarised in §4. Throughout we work at the trial state (18) and we use the relabellinguj(μ,c):=ξjμ,c​ξj1,c∈{−1,+1}u_{j}^{(\mu,c)}:=\xi_{j}^{\mu,c}\xi_{j}^{1,c}\in\{-1,+1\}forμ≠1\mu\neq 1, which is, for fixedμ≠1\mu\neq 1, an i.i.d. Rademacher family across bothj≠ij\neq iandc=1,…,Lc=1,\dots,Lby independence of the layer-specific datasets.

## Self-signal (μ=1\mu=1)

Forμ=1\mu=1at the trial state,m^1a=(N−1)/N\hat{m}_{1}^{a}=(N-1)/Nfor everyaa, soF1a\displaystyle F_{1}^{a}=∑b≠am^1b=(L−1)+𝒪​(N−1),\displaystyle\;=\;\sum_{b\neq a}\hat{m}_{1}^{b}\;=\;(L-1)+\mathcal{O}(N^{-1}),(44)E^1\displaystyle\hat{E}_{1}=N​(L2)​(N−1N)2−N​(L2)=−L​(L−1)+𝒪​(N−1).\displaystyle\;=\;N\binom{L}{2}\Bigl(\tfrac{N-1}{N}\Bigr)^{\!2}-N\binom{L}{2}\;=\;-L(L-1)+\mathcal{O}(N^{-1}).(45)

The on-site factor is deterministic, sinceξi1,c​σic=(ξi1,c)2=1\xi_{i}^{1,c}\sigma_{i}^{c}=(\xi_{i}^{1,c})^{2}=1,Φ1(\a)=exp⁡(∑c≠aF1c)=e(L−1)2​(1+𝒪​(N−1)).\Phi_{1}^{(\backslash a)}\;=\;\exp\!\Bigl(\sum_{c\neq a}F_{1}^{c}\Bigr)\;=\;e^{(L-1)^{2}}\bigl(1+\mathcal{O}(N^{-1})\bigr).(46)

Combining,Xi(1|a)=(ξi1,a)2​eE^1​sinh⁡(F1a)​Φ1(\a)=e−L​(L−1)​sinh⁡(L−1)​e(L−1)2+𝒪​(N−1).X_{i}^{(1|a)}\;=\;(\xi_{i}^{1,a})^{2}\,e^{\hat{E}_{1}}\sinh(F_{1}^{a})\,\Phi_{1}^{(\backslash a)}\;=\;e^{-L(L-1)}\sinh(L-1)\,e^{(L-1)^{2}}+\mathcal{O}(N^{-1}).(47)

Using(L−1)2−L​(L−1)=−(L−1)(L-1)^{2}-L(L-1)=-(L-1),Xi(1|a)=e−(L−1)​sinh⁡(L−1)+𝒪​(N−1).X_{i}^{(1|a)}\;=\;e^{-(L-1)}\sinh(L-1)+\mathcal{O}(N^{-1}).(48)

## Direct verification by single flip

At the trial state,E1=N​((L2)⋅1−(L2))=0E_{1}=N(\binom{L}{2}\cdot 1-\binom{L}{2})=0. Flippingσia→−ξi1,a\sigma_{i}^{a}\to-\xi_{i}^{1,a}shiftsm1a→1−2/Nm_{1}^{a}\to 1-2/Nwhile leaving every other Mattis magnetisation unchanged, so the new exponent of the recalled term isE1′=N​[(L−12)⋅1+(L−1)​(1−2N)]−N​(L2)=−2​(L−1).E_{1}^{\prime}\;=\;N\Bigl[\binom{L-1}{2}\cdot 1+(L-1)\bigl(1-\tfrac{2}{N}\bigr)\Bigr]-N\binom{L}{2}\;=\;-2(L-1).(49)

The contribution from the noise patterns is exponentially suppressed by (26), soΔ​Eia=N​(1−e−2​(L−1))\Delta E_{i}^{a}=N(1-e^{-2(L-1)}). Equating with2​N​hia​ξi1,a2N\,h_{i}^{a}\,\xi_{i}^{1,a},ξi1,a​hia=1−e−2​(L−1)2=e−(L−1)​sinh⁡(L−1),\xi_{i}^{1,a}\,h_{i}^{a}\;=\;\frac{1-e^{-2(L-1)}}{2}\;=\;e^{-(L-1)}\sinh(L-1),(50)

in agreement with (48).

## Noise contribution toμ1\mu_{1}

Forμ≠1\mu\neq 1the cavity magnetisationsm^μc=N−1​∑j≠iuj(μ,c)\hat{m}_{\mu}^{c}=N^{-1}\sum_{j\neq i}u_{j}^{(\mu,c)}are sums of(N−1)(N-1)i.i.d. Rademacher variables, som^μc=𝒪​(N−1/2),Fμc=𝒪​(N−1/2),E^μ=−N​(L2)+𝒪​(1).\hat{m}_{\mu}^{c}=\mathcal{O}(N^{-1/2}),\quad F_{\mu}^{c}=\mathcal{O}(N^{-1/2}),\quad\hat{E}_{\mu}=-N\binom{L}{2}+\mathcal{O}(1).(51)

Usingsinh⁡(ξiμ,a​Fμa)=ξiμ,a​sinh⁡(Fμa)\sinh(\xi_{i}^{\mu,a}F_{\mu}^{a})=\xi_{i}^{\mu,a}\sinh(F_{\mu}^{a}),Xi(μ|a)=ξi1,a​ξiμ,a​eE^μ​sinh⁡(Fμa)​Φμ(\a).X_{i}^{(\mu|a)}\;=\;\xi_{i}^{1,a}\,\xi_{i}^{\mu,a}\,e^{\hat{E}_{\mu}}\sinh(F_{\mu}^{a})\,\Phi_{\mu}^{(\backslash a)}.(52)

The on-site factorξi1,a\xi_{i}^{1,a}is independent of every other random object in (52): ofξiμ,a\xi_{i}^{\mu,a}by independence of layer-aapatterns at the same site; ofm^μc\hat{m}_{\mu}^{c}for anyccadμ\mu, sinceμ≠1\mu\not=1; and ofΦμ(\a)\Phi_{\mu}^{(\backslash a)}, which involvesξiμ,c\xi_{i}^{\mu,c}only forc≠ac\neq aand these are independent ofξiμ,a\xi_{i}^{\mu,a}because the datasets are independent across layers. Hence𝔼​[Xi(μ|a)]=𝔼​[ξi1,a]⋅𝔼​[⋯]=0\mathbb{E}[X_{i}^{(\mu|a)}]=\mathbb{E}[\xi_{i}^{1,a}]\cdot\mathbb{E}[\cdots]=0, exactly. Combining with (48) produces (20).

## Off-diagonal contributions toμ2\mu_{2}

## Caseμ=1\mu=1,ν≠1\nu\neq 1

Xi(1|a)X_{i}^{(1|a)}is deterministic at leading order, so𝔼​[Xi(1|a)​Xi(ν|a)]=Xi(1|a)⋅𝔼​[Xi(ν|a)]=0.\mathbb{E}\bigl[X_{i}^{(1|a)}X_{i}^{(\nu|a)}\bigr]\;=\;X_{i}^{(1|a)}\cdot\mathbb{E}[X_{i}^{(\nu|a)}]\;=\;0.(53)

## Caseμ≠ν\mu\neq\nu, both≠1\neq 1

Substituting (52) for both factors,Xi(μ|a)​Xi(ν|a)=(ξi1,a)2​ξiμ,a​ξiν,a​eE^μ+E^ν​sinh⁡(Fμa)​sinh⁡(Fνa)​Φμ(\a)​Φν(\a).X_{i}^{(\mu|a)}X_{i}^{(\nu|a)}\;=\;(\xi_{i}^{1,a})^{2}\,\xi_{i}^{\mu,a}\xi_{i}^{\nu,a}\,e^{\hat{E}_{\mu}+\hat{E}_{\nu}}\sinh(F_{\mu}^{a})\sinh(F_{\nu}^{a})\,\Phi_{\mu}^{(\backslash a)}\Phi_{\nu}^{(\backslash a)}.(54)

The on-site productξiμ,a​ξiν,a\xi_{i}^{\mu,a}\xi_{i}^{\nu,a}is independent of every other quantity in the expression, by the same independence argument as inA, and has zero expectation. Hence the off-diagonal contribution vanishes exactly.

## On-site square average𝔼​[(Φμ(\a))2]\mathbb{E}[(\Phi_{\mu}^{(\backslash a)})^{2}]

Forμ≠1\mu\neq 1,(Φμ(\a))2=exp⁡(2​∑c≠aξiμ,c​σic​Fμc).(\Phi_{\mu}^{(\backslash a)})^{2}\;=\;\exp\!\Bigl(2\sum_{c\neq a}\xi_{i}^{\mu,c}\sigma_{i}^{c}F_{\mu}^{c}\Bigr).(55)

At the trial state,σic=ξi1,c\sigma_{i}^{c}=\xi_{i}^{1,c}, soξiμ,c​σic=ξiμ,c​ξi1,c∈{−1,+1}\xi_{i}^{\mu,c}\sigma_{i}^{c}=\xi_{i}^{\mu,c}\xi_{i}^{1,c}\in\{-1,+1\}. Layer-ccon-site factors are mutually independent acrossc≠ac\neq abecause the datasets are layer-independent; averaging factor by factor and using𝔼u​[ex​u]=cosh⁡x\mathbb{E}_{u}[e^{xu}]=\cosh xforu∈{−1,+1}u\in\{-1,+1\}Rademacher,𝔼​[(Φμ(\a))2]=∏c≠acosh⁡(2​Fμc).\mathbb{E}\bigl[(\Phi_{\mu}^{(\backslash a)})^{2}\bigr]\;=\;\prod_{c\neq a}\cosh\!\bigl(2F_{\mu}^{c}\bigr).(56)

## Berry–Esseen control of the Gaussian approximation

Section4approximatesXiaX_{i}^{a}by a Gaussian via the Central
Limit Theorem applied to the sum ofP−1P-1noise contributionsXi(μ|a)X_{i}^{(\mu|a)},μ≠1\mu\neq 1, which are i.i.d. acrossμ\muat fixedNNbecause
the layer datasets are mutually independent (§2). We make the
rate of this approximation explicit.

## A deterministic bound on the noise terms

## Lemma 1.

For everyNN, every site(i,a)(i,a), everyμ≠1\mu\neq 1and every realisation of the
disorder,|Xi(μ|a)|≤ML:=sinh⁡(L−1)​e(L−1)2.\bigl|X_{i}^{(\mu|a)}\bigr|\;\leq\;M_{L}\;:=\;\sinh(L-1)\,e^{(L-1)^{2}}.(57)

## Proof.

WriteXi(μ|a)=ξi1,a​eE^μ​sinh⁡(Fμa)​Φμ(\a)X_{i}^{(\mu|a)}=\xi_{i}^{1,a}e^{\hat{E}_{\mu}}\sinh(F_{\mu}^{a})\Phi_{\mu}^{(\backslash a)}.
Every cavity magnetisation is an empirical average of±1\pm 1’s, so|m^μb|≤1|\hat{m}_{\mu}^{b}|\leq 1and|Fμc|=|∑d≠cm^μd|≤L−1|F_{\mu}^{c}|=|\sum_{d\neq c}\hat{m}_{\mu}^{d}|\leq L-1for
everycc; hence|sinh⁡(Fμa)|≤sinh⁡(L−1)|\sinh(F_{\mu}^{a})|\leq\sinh(L-1)and, sinceΦμ(\a)=exp⁡(∑c≠aui(μ,c)​Fμc)\Phi_{\mu}^{(\backslash a)}=\exp\bigl(\sum_{c\neq a}u_{i}^{(\mu,c)}F_{\mu}^{c}\bigr)withui(μ,c)=±1u_{i}^{(\mu,c)}=\pm 1,|log⁡Φμ(\a)|≤∑c≠a|Fμc|≤(L−1)2|\log\Phi_{\mu}^{(\backslash a)}|\leq\sum_{c\neq a}|F_{\mu}^{c}|\leq(L-1)^{2},
soΦμ(\a)≤e(L−1)2\Phi_{\mu}^{(\backslash a)}\leq e^{(L-1)^{2}}. FinallyE^μ=N​[Θ​(𝒎^μ)−(L2)]\hat{E}_{\mu}=N[\Theta(\hat{\bm{m}}_{\mu})-\binom{L}{2}]withΘ​(𝒎):=∑c<dmc​md\Theta(\bm{m}):=\sum_{c<d}m^{c}m^{d}affine in each coordinate separately on[−1,1]L[-1,1]^{L}; a function affine in each coordinate attains its extrema at a
vertex of the box, and among the2L2^{L}vertices𝜺∈{−1,+1}L\bm{\varepsilon}\in\{-1,+1\}^{L},Θ​(𝜺)=12​[(∑cεc)2−L]≤12​(L2−L)=(L2)\Theta(\bm{\varepsilon})=\tfrac{1}{2}\bigl[(\sum_{c}\varepsilon_{c})^{2}-L\bigr]\leq\tfrac{1}{2}(L^{2}-L)=\binom{L}{2},
with equality iff allεc\varepsilon_{c}agree in sign. HenceΘ≤(L2)\Theta\leq\binom{L}{2}everywhere on the box, soE^μ≤0\hat{E}_{\mu}\leq 0andeE^μ≤1e^{\hat{E}_{\mu}}\leq 1. Multiplying
the three bounds (with|ξi1,a|=1|\xi_{i}^{1,a}|=1) gives the claim.
∎

## Finite third moment and the Berry–Esseen bound

Since|Xi(μ|a)|3=|Xi(μ|a)|⋅(Xi(μ|a))2≤ML​(Xi(μ|a))2|X_{i}^{(\mu|a)}|^{3}=|X_{i}^{(\mu|a)}|\cdot(X_{i}^{(\mu|a)})^{2}\leq M_{L}\,(X_{i}^{(\mu|a)})^{2},
taking expectations and using (26),ρ3:=𝔼​|Xi(μ|a)|3≤ML​𝔼​[(Xi(μ|a))2]=ML​KL​e−N​ρL​(1+o​(1)).\rho_{3}\;:=\;\mathbb{E}\bigl|X_{i}^{(\mu|a)}\bigr|^{3}\;\leq\;M_{L}\,\mathbb{E}\bigl[(X_{i}^{(\mu|a)})^{2}\bigr]\;=\;M_{L}\,K_{L}\,e^{-N\rho_{L}}\bigl(1+o(1)\bigr).(58)

TheP−1P-1noise terms are i.i.d. at fixedNN, mean zero, with varianceσ12:=KL​e−N​ρL​(1+o​(1))\sigma_{1}^{2}:=K_{L}e^{-N\rho_{L}}(1+o(1))and third absolute moment bounded
by (58); the Berry–Esseen theorem (sharp constantC≤0.4748C\leq 0.4748) then givessupx|ℙ​(Xia−μ1σ≤x)−Φ​(x)|≤C​ρ3σ13​P−1≤C​MLσ1​P−1,σ2=(P−1)​σ12.\sup_{x}\Bigl|\mathbb{P}\Bigl(\tfrac{X_{i}^{a}-\mu_{1}}{\sigma}\leq x\Bigr)-\Phi(x)\Bigr|\;\leq\;C\,\frac{\rho_{3}}{\sigma_{1}^{3}\sqrt{P-1}}\;\leq\;\frac{C\,M_{L}}{\sigma_{1}\sqrt{P-1}},\qquad\sigma^{2}=(P-1)\sigma_{1}^{2}.(59)

The constantCCis universal: it depends on neitherNN,LL,PPnor the law
of the noise terms, which is the precise content of “uniform inNN”
invoked in §4.

## Remark 4(Scope of the bound).

The right-hand side of (59) is informative (→0\to 0) onceP−1≫ML2/(KL​e−N​ρL)P-1\gg M_{L}^{2}/(K_{L}e^{-N\rho_{L}}), i.e. oncePPexceeds a constant multiple
ofeN​ρLe^{N\rho_{L}}– at or beyond the critical load itself. The elementary
bound (57) is therefore silent on the sub-critical retrieval
regimeP≪PcP\ll P_{c}that the Monte Carlo battery of
Sections5–9actually probes: it certifies that
the CLT approximation is meaningful with a rate once the load is comparable
to or above capacity, not that the approximation is loose below it (the
extensive numerical agreement there is evidence of the latter, not a proof of
it). Sharpening (58) into a bound that also vanishes deep in
the sub-critical regime would require the exact third moment, rather than the
crude boundMLM_{L}, through the same large-deviation machinery asB; we leave this refinement open.

## Appendix BSaddle-point analysis: rate, prefactor, fluctuations

The diagonal noise contribution (22) requires the asymptotic evaluation, inNN, ofℐN:=𝔼​[e2​E^μ​sinh2⁡(Fμa)​∏c≠acosh⁡(2​Fμc)],μ≠1,\mathcal{I}_{N}\;:=\;\mathbb{E}\!\Bigl[\,e^{2\hat{E}_{\mu}}\sinh^{2}(F_{\mu}^{a})\prod_{c\neq a}\cosh(2F_{\mu}^{c})\,\Bigr],\qquad\mu\neq 1,(60)

the expectation running over the cavity magnetisations𝒎^μ=(m^μ1,…,m^μL)∈[−1,1]L\bm{\hat{m}}_{\mu}=(\hat{m}_{\mu}^{1},\dots,\hat{m}_{\mu}^{L})\in[-1,1]^{L}. The route taken here –cavity fields, large deviations, Gaussian fluctuations around a saddle– is standard statistical-mechanics toolkit[45,21], applied to a case (a product, rather than a sum, of per-layer overlaps in the exponent) where it does not reduce to a closed form. We carry out the analysis in three steps: large-deviation reduction to a variational problem ; identification of the symmetric saddle and proof of its uniqueness ; Gaussian fluctuation expansion and explicit evaluation of the prefactorKLK_{L}.

## Large-deviation reduction

By Cramér’s theorem, the empirical magnetisation of a single layer satisfies a large-deviation principle on[−1,1][-1,1]with rate functionIR​(m)=1+m2​log⁡(1+m)+1−m2​log⁡(1−m),I_{R}(m)\;=\;\tfrac{1+m}{2}\log(1+m)+\tfrac{1-m}{2}\log(1-m),(61)

the Cramér transform of the symmetric Bernoulli distribution. Independence across layers gives the joint rateI​(𝒎)=∑c=1LIR​(mc),𝒎∈[−1,1]L.I(\bm{m})\;=\;\sum_{c=1}^{L}I_{R}(m^{c}),\qquad\bm{m}\in[-1,1]^{L}.(62)

Substituting2​E^μ=2​N​∑c<dm^μc​m^μd−2​N​(L2)2\hat{E}_{\mu}=2N\sum_{c<d}\hat{m}_{\mu}^{c}\hat{m}_{\mu}^{d}-2N\binom{L}{2}in (60) and applying the following lemma:

## Lemma 2(Varadhan’s Lemma).

Let𝒳\mathcal{X}be a regular topological space and let(PN)N∈ℕ(P_{N})_{N\in\mathbb{N}}be a sequence of probability measures on𝒳\mathcal{X}satisfying a Large Deviation Principle with rate functionI:𝒳→[0,∞]I:\mathcal{X}\to[0,\infty].

Furthermore, letF:𝒳→ℝF:\mathcal{X}\to\mathbb{R}be a continuous function bounded from above. Then, the following limit holds:limN→∞1N​log⁡𝔼PN​[eN​F​(X)]=supx∈𝒳[F​(x)−I​(x)].\lim_{N\to\infty}\frac{1}{N}\log\mathbb{E}_{P_{N}}\left[e^{NF(X)}\right]=\sup_{x\in\mathcal{X}}\left[F(x)-I(x)\right].

The polynomial factorssinh2\sinh^{2},cosh\coshcontribute only to the sub-exponential prefactor — the leading exponential rate is1N​log⁡ℐN→N→∞−2​(L2)+sup𝒎∈[−1,1]LΨ​(𝒎),Ψ​(𝒎):=2​∑c<dmc​md−I​(𝒎).\frac{1}{N}\log\mathcal{I}_{N}\;\xrightarrow[N\to\infty]{}\;-2\binom{L}{2}+\sup_{\bm{m}\in[-1,1]^{L}}\Psi(\bm{m}),\qquad\Psi(\bm{m})\;:=\;2\sum_{c<d}m^{c}m^{d}-I(\bm{m}).(63)

## Symmetric saddle and uniqueness

The functionalΨ\Psiis invariant under permutations of the layers and even in eachmcm^{c}. Its first-order conditions read2​∑d≠cmd=tanh−1⁡(mc)2\sum_{d\neq c}m^{d}=\tanh^{-1}(m^{c})forc=1,…,Lc=1,\dots,L. Subtracting two of these equations,2​(mc′−mc)=tanh−1⁡(mc)−tanh−1⁡(mc′),2(m^{c^{\prime}}-m^{c})\;=\;\tanh^{-1}(m^{c})-\tanh^{-1}(m^{c^{\prime}}),(64)

which, combined with the strict monotonicity oftanh−1\tanh^{-1}on(−1,1)(-1,1), forcesmc=mc′m^{c}=m^{c^{\prime}}for every pair(c,c′)(c,c^{\prime}). Every interior stationary point therefore lies on the symmetric raymc≡m∗m^{c}\equiv m^{*}. On that ray,Ψ\Psireduces toΛL​(m):=2​(L2)​m2−L​IR​(m)=L​(L−1)​m2−L​IR​(m),\Lambda_{L}(m)\;:=\;2\binom{L}{2}m^{2}-L\,I_{R}(m)\;=\;L(L-1)\,m^{2}-L\,I_{R}(m),(65)

whose stationarity condition readstanh−1⁡(m∗)=2​(L−1)​m∗⟺m∗=tanh⁡(2​(L−1)​m∗).\tanh^{-1}(m^{*})\;=\;2(L-1)\,m^{*}\quad\Longleftrightarrow\quad m^{*}\;=\;\tanh\!\bigl(2(L-1)\,m^{*}\bigr).(66)

ForL≥2L\geq 2, equation (66) has the trivial rootm∗=0m^{*}=0(a local minimum ofΛL\Lambda_{L}) and two non-trivial symmetric roots±m0∗≠0\pm m^{*}_{0}\neq 0, which realise the supremum by continuity ofΛL\Lambda_{L}on[−1,1][-1,1]and byΛL​(±1)=−∞\Lambda_{L}(\pm 1)=-\infty. We pick the positive rootm∗=m0∗>0m^{*}=m^{*}_{0}>0.

With the change of variablesx=2​(L−1)​mx=2(L-1)m, equation (66) becomestanh⁡(x∗)=x∗/[2​(L−1)]\tanh(x^{*})=x^{*}/[2(L-1)], the stationarity condition ofϕL​(x):=−x24​(L−1)+log⁡cosh⁡(x).\phi_{L}(x)\;:=\;-\frac{x^{2}}{4(L-1)}+\log\cosh(x).(67)

The supremum (63) on the symmetric ray equalsL​ϕL​(x∗)L\,\phi_{L}(x^{*}). Indeed, setg​(m):=(L−1)​m2−IR​(m)g(m):=(L-1)m^{2}-I_{R}(m); withx=tanh−1⁡(m)x=\tanh^{-1}(m)one hasIR​(m)=m​x−log⁡cosh⁡(x)I_{R}(m)=mx-\log\cosh(x), whenceg​(tanh⁡(x))=(L−1)​tanh2⁡(x)−x​tanh⁡(x)+log⁡cosh⁡(x).g(\tanh(x))\;=\;(L-1)\tanh^{2}(x)-x\tanh(x)+\log\cosh(x).(68)

At the saddle,tanh⁡(x∗)=x∗/[2​(L−1)]\tanh(x^{*})=x^{*}/[2(L-1)]gives(L−1)​tanh2⁡(x∗)=x∗2/[4​(L−1)](L-1)\tanh^{2}(x^{*})=x^{*\,2}/[4(L-1)]andx∗​tanh⁡(x∗)=x∗2/[2​(L−1)]x^{*}\tanh(x^{*})=x^{*\,2}/[2(L-1)], so thatg​(tanh⁡(x∗))=−x∗24​(L−1)+log⁡cosh⁡(x∗)=ϕL​(x∗).g(\tanh(x^{*}))\;=\;-\frac{x^{*\,2}}{4(L-1)}+\log\cosh(x^{*})\;=\;\phi_{L}(x^{*}).(69)

Combining (63) and (69),1N​log⁡ℐN→N→∞−L​(L−1)+L​ϕL​(x∗),\frac{1}{N}\log\mathcal{I}_{N}\;\xrightarrow[N\to\infty]{}\;-L(L-1)+L\,\phi_{L}(x^{*}),(70)

which defines the noise rateρL:=L​[(L−1)−ϕL​(x∗)],\rho_{L}\;:=\;L\bigl[(L-1)-\phi_{L}(x^{*})\bigr],(71)

in agreement with (24).

## Gaussian fluctuations and prefactorKLK_{L}

Having identified the saddle𝒎=m∗​𝟏\bm{m}=m^{*}\bm{1}and the exponential rateρL\rho_{L}, we now extract the polynomial prefactorKLK_{L}by performing a
systematic Gaussian expansion ofℐN\mathcal{I}_{N}around that saddle.

Since each cavity magnetisationm^μc\hat{m}_{\mu}^{c}is an empirical average ofN−1N-1i.i.d. Rademacher variables, it fluctuates on the scaleN−1/2N^{-1/2}around any deterministic value. We therefore introduce rescaled deviations
from the saddle,m^μc=m∗+ycN,yc∈ℝ,c=1,…,L,\hat{m}_{\mu}^{c}\;=\;m^{*}+\frac{y_{c}}{\sqrt{N}},\qquad y_{c}\in\mathbb{R},\quad c=1,\dots,L,(72)

and expand the actionN​Ψ​(𝒎^μ)N\Psi(\bm{\hat{m}}_{\mu})in powers ofN−1/2N^{-1/2}.
Becausem∗​𝟏m^{*}\bm{1}is a stationary point ofΨ\Psi, the linear term in𝒚\bm{y}vanishes identically, and the expansion readsN​Ψ​(𝒎^μ)=N​Ψ​(m∗​𝟏)−12​𝒚𝖳​ℋL∗​𝒚+𝒪​(N−1/2),N\,\Psi(\bm{\hat{m}}_{\mu})\;=\;N\,\Psi(m^{*}\bm{1})\;-\;\frac{1}{2}\,\bm{y}^{\mathsf{T}}\mathcal{H}_{L}^{*}\,\bm{y}\;+\;\mathcal{O}(N^{-1/2}),(73)

whereℋL∗\mathcal{H}_{L}^{*}denotes the negative of the Hessian ofΨ\Psievaluated atm∗​𝟏m^{*}\bm{1}. To compute its entries we differentiateΨ​(𝒎)=2​∑c<dmc​md−∑cIR​(mc)\Psi(\bm{m})=2\sum_{c<d}m^{c}m^{d}-\sum_{c}I_{R}(m^{c})twice: the diagonal
entries receive no contribution from the bilinear term and give−∂mc2IR​(mc)|m∗=11−m∗2-\partial_{m^{c}}^{2}I_{R}(m^{c})\big|_{m^{*}}=\frac{1}{1-m^{*\,2}}, usingIR′′​(m)=(1−m2)−1I_{R}^{\prime\prime}(m)=(1-m^{2})^{-1}; the off-diagonal entries come entirely from the
bilinear term and equal−2⋅(−1)=2⋅(−1)-2\cdot(-1)=2\cdot(-1)… more precisely, the
Hessian of−Ψ-\Psiat off-diagonal positions is−2-2, so altogether(ℋL∗)c​d=11−m∗2​δc​d−2​(1−δc​d).(\mathcal{H}_{L}^{*})_{cd}\;=\;\frac{1}{1-m^{*\,2}}\,\delta_{cd}\;-\;2\,(1-\delta_{cd}).(74)

Writing𝑱=𝟏𝟏𝖳\bm{J}=\bm{1}\bm{1}^{\mathsf{T}}for theL×LL\times Lall-ones matrix,
this is equivalentlyℋL∗=(11−m∗2+2)​IL−2​𝑱\mathcal{H}_{L}^{*}=\bigl(\frac{1}{1-m^{*\,2}}+2\bigr)I_{L}-2\bm{J},
a rank-one update of a scalar multiple of the identity whose spectrum is
immediate: the symmetric eigenvector𝟏/L\bm{1}/\sqrt{L}has eigenvalueλ∥=11−m∗2−2​(L−1)\lambda_{\parallel}=\frac{1}{1-m^{*\,2}}-2(L-1), while every vector in𝟏⟂\bm{1}^{\perp}has eigenvalueλ⟂=11−m∗2+2\lambda_{\perp}=\frac{1}{1-m^{*\,2}}+2.
The latter is manifestly positive; positivity ofλ∥\lambda_{\parallel}follows
from the geometry of the non-trivial fixed point: atm∗=tanh⁡(2​(L−1)​m∗)m^{*}=\tanh(2(L-1)m^{*})the slope oftanh\tanhsatisfies1−m∗2=sech2​(2​(L−1)​m∗)<12​(L−1)1-m^{*\,2}=\mathrm{sech}^{2}(2(L-1)m^{*})<\frac{1}{2(L-1)}, since the non-trivial crossing occurs where the curvetanh⁡(x)\tanh(x)is already less steep than the linex/[2​(L−1)]x/[2(L-1)]. HenceℋL∗\mathcal{H}_{L}^{*}is positive definite and the Gaussian integral below
converges.

We now turn to the polynomial insertions. At𝒎^μ=m∗​𝟏\bm{\hat{m}}_{\mu}=m^{*}\bm{1}the cavity field of every layer equalsFμc=(L−1)​m∗F_{\mu}^{c}=(L-1)m^{*}, sosinh2(Fμa)|m∗​𝟏=sinh2((L−1)m∗),∏c≠acosh(2Fμc)|m∗​𝟏=cosh(2(L−1)m∗)L−1.\sinh^{2}(F_{\mu}^{a})\Big|_{m^{*}\bm{1}}=\sinh^{2}\!\bigl((L-1)m^{*}\bigr),\qquad\prod_{c\neq a}\cosh\!\bigl(2F_{\mu}^{c}\bigr)\Big|_{m^{*}\bm{1}}=\cosh\!\bigl(2(L-1)m^{*}\bigr)^{L-1}.(75)

Being smooth functions of𝒎^\bm{\hat{m}}, these factors deviate from their
saddle values only at orderN−1/2N^{-1/2}, and their fluctuations do not
contribute to the leading prefactor.

Collecting all ingredients, we substitute the Taylor
expansion (73) and the frozen
insertions (75) into (60). By Cramér’s
theorem the joint density of𝒎^μ\bm{\hat{m}}_{\mu}is∝e−N​I​(𝒎^μ)+o​(N)\propto e^{-NI(\bm{\hat{m}}_{\mu})+o(N)}, and the change of variablesm^μc=m∗+yc/N\hat{m}_{\mu}^{c}=m^{*}+y_{c}/\sqrt{N}(whose JacobianN−L/2N^{-L/2}is absorbed
into the density normalisation) givesℐN\displaystyle\mathcal{I}_{N}=∫d𝒎^​eN​Ψ​(𝒎^)​sinh2⁡(Fa)​∏c≠acosh⁡(2​Fc)​(1+o​(1))\displaystyle\;=\;\int\!\mathrm{d}\bm{\hat{m}}\;e^{N\Psi(\bm{\hat{m}})}\,\sinh^{2}(F^{a})\prod_{c\neq a}\cosh(2F^{c})\;(1+o(1))=eN​Ψ​(m∗​𝟏)sinh2((L−1)m∗)cosh(2(L−1)m∗)L−1∫ℝLd𝒚e−12​𝒚𝖳​ℋL∗​𝒚(1+o(1)).\displaystyle\;=\;e^{N\Psi(m^{*}\bm{1})}\,\sinh^{2}\!\bigl((L-1)m^{*}\bigr)\,\cosh\!\bigl(2(L-1)m^{*}\bigr)^{L-1}\int_{\mathbb{R}^{L}}\!\mathrm{d}\bm{y}\;e^{-\frac{1}{2}\bm{y}^{\mathsf{T}}\mathcal{H}_{L}^{*}\bm{y}}\;(1+o(1)).(76)

The standard Gaussian integral evaluates
to(2​π)L/2/detℋL∗(2\pi)^{L/2}/\sqrt{\det\mathcal{H}_{L}^{*}}, wheredetℋL∗=λ∥​λ⟂L−1\det\mathcal{H}_{L}^{*}=\lambda_{\parallel}\,\lambda_{\perp}^{L-1}is the
product of the eigenvalues computed above. Recalling
from (70) thateN​Ψ​(m∗​𝟏)=e−N​ρL​(1+o​(1))e^{N\Psi(m^{*}\bm{1})}=e^{-N\rho_{L}}(1+o(1)),
we concludeℐN=KL​e−N​ρL​(1+o​(1)),\mathcal{I}_{N}\;=\;K_{L}\,e^{-N\rho_{L}}\,\bigl(1+o(1)\bigr),(77)

with the prefactorKL=(2​π)L/2detℋL∗sinh2((L−1)m∗)cosh(2(L−1)m∗)L−1,K_{L}\;=\;\frac{(2\pi)^{L/2}}{\sqrt{\det\mathcal{H}_{L}^{*}}}\,\sinh^{2}\!\bigl((L-1)m^{*}\bigr)\,\cosh\!\bigl(2(L-1)m^{*}\bigr)^{L-1},(78)

in agreement with (25) of the main text.

## Numerical values and asymptoticsLLx∗x^{*}m∗m^{*}ϕL​(x∗)\phi_{L}(x^{*})ρL\rho_{L}21.91500.95750.32651.347033.99730.99931.30722.078445.99990.999992.30692.772658.0000≈1\approx 13.30693.46571018.0000≈1\approx 18.30696.9315Table 4:Saddle data and noise rateρL\rho_{L}for moderateLL.

ForL→∞L\to\inftythe saddle drifts tox∗∼2​(L−1)x^{*}\sim 2(L-1)andm∗→1−m^{*}\to 1^{-}, givingϕL​(x∗)∼(L−1)−log⁡2\phi_{L}(x^{*})\sim(L-1)-\log 2and the asymptotic rateρL∼L​log⁡2,L→∞.\rho_{L}\;\sim\;L\log 2,\qquad L\to\infty.(79)

The rate is positive for everyL≥2L\geq 2, ensuring exponential suppression of the noise contribution at fixed pattern.

## Numerical validation: saddle and rate scaling

Figure9(a) plots the variational functionalϕL​(x)\phi_{L}(x)forL∈{2,3,4}L\in\{2,3,4\}, whose interior maximiser is the saddlex∗x^{*}of Table4; the equivalent graphical solution oftanh⁡(x∗)=x∗/[2​(L−1)]\tanh(x^{*})=x^{*}/[2(L-1)]appears in the main-text Figure1(a), where the rapid drift ofx∗x^{*}towards2​(L−1)2(L-1)is visible. Figure9(b) verifies the scaling (79): the rateρL\rho_{L}tracks the asymptoteL​log⁡2L\log 2from above while the Gaussian prefactorKLK_{L}grows rapidly with the widthLL. The doubling identity (80) atL=2L=2,ρ2=2​ρ1Dem\rho_{2}=2\rho_{1}^{\mathrm{Dem}}withρ1Dem=1−ϕ2​(x∗)=0.6735\rho_{1}^{\mathrm{Dem}}=1-\phi_{2}(x^{*})=0.6735, is derived at the end of this appendix and marked in the inset of Figure1(b).Figure 9:Saddle landscape, rate and prefactor.(a)The variational functionalϕL​(x)=−x2/[4​(L−1)]+log⁡cosh⁡x\phi_{L}(x)=-x^{2}/[4(L-1)]+\log\cosh xforL=2,3,4L=2,3,4; markers locate the interior maximiserx∗x^{*}of
Table4.(b)The noise rateρL\rho_{L}(left axis, linear, approachingL​log⁡2L\log 2)
and the Gaussian fluctuation prefactorKLK_{L}(right axis, logarithmic) against
widthLL. Both are smooth and monotonically increasing; the two curves are
drawn on independent scales, so where they appear to meet or separate (aroundL=4L=4) reflects only the choice of axes, not any feature ofρL\rho_{L}orKLK_{L}.

## Doubling identity forL=2L=2

ForL=2L=2the saddle equation (67) becomestanh⁡(x)=x/2\tanh(x)=x/2, withϕ2​(x)=−x2/4+log⁡cosh⁡(x)\phi_{2}(x)=-x^{2}/4+\log\cosh(x). This is exactly the saddle of the single-layer exponential Hopfield model, with rateρ1Dem=1−ϕ2​(x∗)\rho_{1}^{\mathrm{Dem}}=1-\phi_{2}(x^{\ast}). From (24),ρ2=2​[1−ϕ2​(x∗)]=2​ρ1Dem,\rho_{2}\;=\;2\bigl[1-\phi_{2}(x^{\ast})\bigr]\;=\;2\,\rho_{1}^{\mathrm{Dem}},(80)

so thatρ2/[L​(L−1)]=ρ1Dem\rho_{2}/[L(L-1)]=\rho_{1}^{\mathrm{Dem}}and the critical overlap atL=2L=2coincides with the single-layer one: a noise pattern must generate a large overlap simultaneously in two independent layers, and the two layer-overlaps being mutually independent yields the squared exponential suppression. Numericallyρ1Dem=1−ϕ2​(x∗)=0.6735\rho_{1}^{\mathrm{Dem}}=1-\phi_{2}(x^{\ast})=0.6735andρ2=1.3470=2​ρ1Dem\rho_{2}=1.3470=2\rho_{1}^{\mathrm{Dem}}, as marked in Figure9666We note a numerical caveat: forL≥10L\geq 10, the saddle magnetizationm∗m^{\ast}approaches11so rapidly that1−m∗,21-m^{\ast,2}falls below double-precision machine epsilon, leading to catastrophic cancellation in the numerical evaluation ofℋL∗\mathcal{H}_{L}^{\ast}. To computeKLK_{L}accurately at largeLL, one must substitute1/(1−m∗,2)1/(1-m^{\ast,2})with the analytically equivalent expressioncosh2⁡(x∗)\cosh^{2}(x^{\ast})derived from the saddle equation..

## Appendix CCorrupted-state cavity expansion

This appendix details the analysis summarised in §6. Throughout, the network is initialised at the corrupted state (35),σjc=sjc​ξj1,c\sigma_{j}^{c}=s_{j}^{c}\,\xi_{j}^{1,c}, with maskssjc∈{−1,+1}s_{j}^{c}\in\{-1,+1\}i.i.d. across(j,c)(j,c),𝔼​[sjc]=r∈(0,1]\mathbb{E}[s_{j}^{c}]=r\in(0,1], and all cavity quantities are evaluated at this state.

## Cavity magnetisations and local field under corruption

For the recalled archetype,m^1a=1N​∑j≠iξj1,a​σja=1N​∑j≠isja,\hat{m}_{1}^{a}\;=\;\frac{1}{N}\sum_{j\neq i}\xi_{j}^{1,a}\,\sigma_{j}^{a}\;=\;\frac{1}{N}\sum_{j\neq i}s_{j}^{a},(81)

an empirical mean of i.i.d. variables with meanrrand variance1−r21-r^{2}, independent across layers. By the Central Limit Theorem,m^1a=r+ζaN+𝒪​(N−1),ζa​∼𝑑​𝒩​(0,1−r2),\hat{m}_{1}^{a}\;=\;r+\frac{\zeta^{a}}{\sqrt{N}}+\mathcal{O}(N^{-1}),\qquad\zeta^{a}\overset{d}{\sim}\mathcal{N}\bigl(0,1-r^{2}\bigr),(82)

with{ζa}a=1L\{\zeta^{a}\}_{a=1}^{L}mutually independent. ConsequentlyF1a=(L−1)​r+𝒪​(N−1/2)F_{1}^{a}=(L-1)r+\mathcal{O}(N^{-1/2})and, substituting (82) inE^1=N​∑a<bm^1a​m^1b−N​(L2)\hat{E}_{1}=N\sum_{a<b}\hat{m}_{1}^{a}\hat{m}_{1}^{b}-N\binom{L}{2}and using∑a<b(ζa+ζb)=(L−1)​∑cζc\sum_{a<b}(\zeta^{a}+\zeta^{b})=(L-1)\sum_{c}\zeta^{c},E^1=−N​(L2)​(1−r2)+𝒵r+𝒪​(N−1/2),𝒵r:=r​(L−1)​N​∑cζc+∑a<bζa​ζb.\hat{E}_{1}\;=\;-N\binom{L}{2}\bigl(1-r^{2}\bigr)+\mathcal{Z}_{r}+\mathcal{O}(N^{-1/2}),\qquad\mathcal{Z}_{r}:=r(L-1)\sqrt{N}\sum_{c}\zeta^{c}+\sum_{a<b}\zeta^{a}\zeta^{b}.(83)

The on-site factor involves only the masks at siteii: sinceξi1,c​σic=sic\xi_{i}^{1,c}\sigma_{i}^{c}=s_{i}^{c},Φ1(\a)=exp⁡(∑c≠asic​F1c),\Phi_{1}^{(\backslash a)}\;=\;\exp\!\Bigl(\sum_{c\neq a}s_{i}^{c}\,F_{1}^{c}\Bigr),(84)

which is independent of the cavity variables (82). Using the oddness ofsinh\sinh, the signal contribution toXia=ξi1,a​hiaX_{i}^{a}=\xi_{i}^{1,a}h_{i}^{a}is thereforeXi(1|a)=eE^1​sinh⁡(F1a)​exp⁡(∑c≠asic​F1c).X_{i}^{(1|a)}\;=\;e^{\hat{E}_{1}}\,\sinh\bigl(F_{1}^{a}\bigr)\,\exp\!\Bigl(\sum_{c\neq a}s_{i}^{c}\,F_{1}^{c}\Bigr).(85)

## Noise channel under corruption

Forμ≠1\mu\neq 1definevj(μ,c):=ξjμ,c​sjc​ξj1,cv_{j}^{(\mu,c)}:=\xi_{j}^{\mu,c}\,s_{j}^{c}\,\xi_{j}^{1,c}. Sinceξjμ,c\xi_{j}^{\mu,c}is a symmetric Rademacher sign independent of(sjc,ξj1,c)(s_{j}^{c},\xi_{j}^{1,c}), the family{vj(μ,c)}\{v_{j}^{(\mu,c)}\}is i.i.d. symmetric Rademacher for everyrr, acrossjj,ccandμ≠1\mu\neq 1. The noise contributionsXi(μ|a)=ξi1,a​ξiμ,a​eE^μ​sinh⁡(Fμa)​Φμ(\a),m^μc=1N​∑j≠ivj(μ,c),Φμ(\a)=exp⁡(∑c≠avi(μ,c)​Fμc),X_{i}^{(\mu|a)}=\xi_{i}^{1,a}\xi_{i}^{\mu,a}\,e^{\hat{E}_{\mu}}\sinh(F_{\mu}^{a})\,\Phi_{\mu}^{(\backslash a)},\qquad\hat{m}_{\mu}^{c}=\frac{1}{N}\sum_{j\neq i}v_{j}^{(\mu,c)},\qquad\Phi_{\mu}^{(\backslash a)}=\exp\!\Bigl(\sum_{c\neq a}v_{i}^{(\mu,c)}F_{\mu}^{c}\Bigr),(86)

have therefore exactly the same joint law as at the uncorrupted stater=1r=1, wherevj(μ,c)=uj(μ,c)v_{j}^{(\mu,c)}=u_{j}^{(\mu,c)}ofA. In particular:𝔼​[Xi(μ|a)]=0\mathbb{E}[X_{i}^{(\mu|a)}]=0through the on-site factorξi1,a\xi_{i}^{1,a}, as inA; the off-diagonal second moments vanish as inA; the signal–noise cross terms vanish becauseξiμ,a\xi_{i}^{\mu,a}is centred and independent of the masks; and the per-pattern variance isKL​e−N​ρL​(1+o​(1))K_{L}\,e^{-N\rho_{L}}(1+o(1))as computed inB. The noise statistics are therefore insensitive to the corruption level, as anticipated in §6:σ2​(r)=(P−1)​KL​e−N​ρL​(1+o​(1))\sigma^{2}(r)=(P-1)\,K_{L}\,e^{-N\rho_{L}}(1+o(1))for everyrr, exactly as in (28).

## Annealed signal: tilted large deviations

The first moment of (85) factorises over the independent on-site and cavity randomness. Averaging the on-site masks first, conditionally on the cavity variables, with𝔼​[ex​s]=cosh⁡x+r​sinh⁡x\mathbb{E}[e^{xs}]=\cosh x+r\sinh xfors∈{−1,+1}s\in\{-1,+1\}of meanrr,μ1​(r)=𝔼​[eE^1​sinh⁡(F1a)​∏c≠a(cosh⁡F1c+r​sinh⁡F1c)],\mu_{1}(r)\;=\;\mathbb{E}\Bigl[\,e^{\hat{E}_{1}}\,\sinh(F_{1}^{a})\prod_{c\neq a}\bigl(\cosh F_{1}^{c}+r\sinh F_{1}^{c}\bigr)\Bigr],(87)

the remaining expectation running over𝒎^1∈[−1,1]L\bm{\hat{m}}_{1}\in[-1,1]^{L}. Equation (87) is in large-deviation form, exactly as (22), with two differences: the exponent carries a single power ofE^1\hat{E}_{1}, and the reference measure is biased. By Cramér’s theorem the empirical mean of the masks of one layer obeys an LDP with the tilted rate functionIr​(m)=1+m2​log⁡1+m1+r+1−m2​log⁡1−m1−r=IR​(m)−ar​m+log⁡cosh⁡(ar),ar=tanh−1⁡(r),I_{r}(m)\;=\;\frac{1+m}{2}\log\frac{1+m}{1+r}+\frac{1-m}{2}\log\frac{1-m}{1-r}\;=\;I_{R}(m)-a_{r}\,m+\log\cosh(a_{r}),\qquad a_{r}=\tanh^{-1}(r),(88)

which vanishes only atm=rm=r, and the joint rate is∑cIr​(mc)\sum_{c}I_{r}(m^{c})by independence across layers. Varadhan’s lemma then gives1N​log⁡μ1​(r)→N→∞−(L2)+sup𝒎∈[−1,1]LΨr​(𝒎),Ψr​(𝒎):=∑c<dmc​md−∑cIr​(mc),\frac{1}{N}\log\mu_{1}(r)\;\xrightarrow[N\to\infty]{}\;-\binom{L}{2}+\sup_{\bm{m}\in[-1,1]^{L}}\Psi_{r}(\bm{m}),\qquad\Psi_{r}(\bm{m})\;:=\;\sum_{c<d}m^{c}m^{d}-\sum_{c}I_{r}(m^{c}),(89)

the smooth insertions of (87) contributing only to the prefactor.

## Symmetric saddle and uniqueness

The first-order conditions read∑d≠cmd=tanh−1⁡(mc)−ar\sum_{d\neq c}m^{d}=\tanh^{-1}(m^{c})-a_{r}forc=1,…,Lc=1,\dots,L. Subtracting two of them,mc′−mc=tanh−1⁡(mc)−tanh−1⁡(mc′),m^{c^{\prime}}-m^{c}\;=\;\tanh^{-1}(m^{c})-\tanh^{-1}(m^{c^{\prime}}),(90)

and the strict monotonicity oftanh−1\tanh^{-1}forcesmc=mc′m^{c}=m^{c^{\prime}}for every pair: every interior stationary point lies on the symmetric raymc≡mm^{c}\equiv m, whereΨr\Psi_{r}reduces toΛL,r​(m)=(L2)​m2−L​Ir​(m),\Lambda_{L,r}(m)\;=\;\binom{L}{2}m^{2}-L\,I_{r}(m),(91)

with stationarity conditiontanh−1⁡(ms)=(L−1)​ms+ar⟺ms=tanh⁡((L−1)​ms+ar).\tanh^{-1}(m_{s})\;=\;(L-1)\,m_{s}+a_{r}\quad\Longleftrightarrow\quad m_{s}=\tanh\bigl((L-1)m_{s}+a_{r}\bigr).(92)

Forr>0r>0the supremum is attained at the largest rootms>rm_{s}>r; the mirror saddle near−ms-m_{s}carries the extra cost2​L​ar​ms2La_{r}m_{s}and is exponentially subdominant. It matters only atr=0r=0, where the two saddles cancel exactly in the odd integrand andμ1​(0)=0\mu_{1}(0)=0by parity, as it must for an uncorrelated input.

## Explicit rate

Settingxs:=(L−1)​ms+ar=tanh−1⁡(ms)x_{s}:=(L-1)m_{s}+a_{r}=\tanh^{-1}(m_{s})and usingIR​(ms)=ms​xs−log⁡cosh⁡(xs)I_{R}(m_{s})=m_{s}x_{s}-\log\cosh(x_{s})in (88),ΛL,r​(ms)\displaystyle\Lambda_{L,r}(m_{s})=(L2)​ms2−L​[ms​xs−log⁡cosh⁡xs−ar​ms+log⁡cosh⁡ar]\displaystyle=\;\binom{L}{2}m_{s}^{2}-L\bigl[m_{s}x_{s}-\log\cosh x_{s}-a_{r}m_{s}+\log\cosh a_{r}\bigr]=−(L2)​ms2+L​[log⁡cosh⁡xs−log⁡cosh⁡ar],\displaystyle=\;-\binom{L}{2}m_{s}^{2}+L\bigl[\log\cosh x_{s}-\log\cosh a_{r}\bigr],(93)

the second line following fromxs−ar=(L−1)​msx_{s}-a_{r}=(L-1)m_{s}. Substituting in (89) yields the signal rate quoted in (38),ΣL​(r)=(L2)−ΛL,r​(ms)=L​[L−12​(1+ms2)−log⁡cosh⁡(xs)+log⁡cosh⁡(ar)].\Sigma_{L}(r)\;=\;\binom{L}{2}-\Lambda_{L,r}(m_{s})\;=\;L\Bigl[\tfrac{L-1}{2}\bigl(1+m_{s}^{2}\bigr)-\log\cosh(x_{s})+\log\cosh(a_{r})\Bigr].(94)

Sanity checks.Atr→1r\to 1,ar→∞a_{r}\to\inftyforcesms→1m_{s}\to 1; usinglog⁡cosh⁡y=y−log⁡2+o​(1)\log\cosh y=y-\log 2+o(1)for bothxsx_{s}andara_{r}, the bracket tends to(L−1)−(xs−ar)=0(L-1)-(x_{s}-a_{r})=0, henceΣL​(1)=0\Sigma_{L}(1)=0and the𝒪​(1)\mathcal{O}(1)signal ofAis recovered. At fixedr<1r<1, comparingΛL,r\Lambda_{L,r}atmsm_{s}and atm=rm=r(whereIrI_{r}vanishes) gives0<ΣL​(r)≤(L2)​(1−r2),0\;<\;\Sigma_{L}(r)\;\leq\;\binom{L}{2}\bigl(1-r^{2}\bigr),(95)

with strict upper inequality forr<1r<1, since the saddle satisfiesms​(r)>rm_{s}(r)>r: the annealed rate is strictly smaller than the typical one, see below.

## Gaussian fluctuations and prefactor

ExpandingΨr\Psi_{r}to second order aroundms​𝟏m_{s}\bm{1}, in full analogy withB, the negative Hessian is(ℋL,r∗)c​d=11−ms2​δc​d−(1−δc​d)=(11−ms2+1)​IL−𝑱,(\mathcal{H}_{L,r}^{*})_{cd}\;=\;\frac{1}{1-m_{s}^{2}}\,\delta_{cd}-\bigl(1-\delta_{cd}\bigr)\;=\;\Bigl(\frac{1}{1-m_{s}^{2}}+1\Bigr)I_{L}-\bm{J},(96)

with eigenvaluesλ∥=11−ms2−(L−1)\lambda_{\parallel}=\frac{1}{1-m_{s}^{2}}-(L-1)on the symmetric mode andλ⟂=11−ms2+1\lambda_{\perp}=\frac{1}{1-m_{s}^{2}}+1on𝟏⟂\bm{1}^{\perp}. Positivity ofλ∥\lambda_{\parallel}follows from the saddle geometry: at the largest root the curvetanh−1⁡(m)\tanh^{-1}(m)crosses the line(L−1)​m+ar(L-1)m+a_{r}from below, i.e.11−ms2>L−1\frac{1}{1-m_{s}^{2}}>L-1. Freezing the smooth insertions of (87) at the saddle, whereF1c=(L−1)​msF_{1}^{c}=(L-1)m_{s}for everycc, and performing the Gaussian integral,CL​(r)=(2​π)L/2detℋL,r∗​sinh⁡((L−1)​ms)​[cosh⁡((L−1)​ms)+r​sinh⁡((L−1)​ms)]L−1,C_{L}(r)\;=\;\frac{(2\pi)^{L/2}}{\sqrt{\det\mathcal{H}_{L,r}^{*}}}\;\sinh\bigl((L-1)m_{s}\bigr)\,\bigl[\cosh\bigl((L-1)m_{s}\bigr)+r\sinh\bigl((L-1)m_{s}\bigr)\bigr]^{L-1},(97)

withdetℋL,r∗=λ∥​λ⟂L−1\det\mathcal{H}_{L,r}^{*}=\lambda_{\parallel}\lambda_{\perp}^{L-1}, in the same normalisation convention as (78); see Remark5for the finite-NNcorrected version.

## Annealed versus typical signal

The annealed average (87) is controlled by mask configurations withm^1c≡ms​(r)>r\hat{m}_{1}^{c}\equiv m_{s}(r)>r, which carry probabilitye−N​L​Ir​(ms)e^{-NL\,I_{r}(m_{s})}: exponentially rare. The typical behaviour is read off (82)–(83) directly. This is already visible at the level of the Gaussian fluctuation𝒵r\mathcal{Z}_{r}: writing∑a<bζa​ζb=12​[(∑cζc)2−∑c(ζc)2]\sum_{a<b}\zeta^{a}\zeta^{b}=\frac{1}{2}[(\sum_{c}\zeta^{c})^{2}-\sum_{c}(\zeta^{c})^{2}]and performing the Gaussian integral exactly,𝔼ζ​[e𝒵r]=exp⁡(L​(L−1)2​r2​(1−r2)2​[1−(L−1)​(1−r2)]​N+𝒪​(1)),if​(L−1)​(1−r2)<1,\mathbb{E}_{\zeta}\bigl[e^{\mathcal{Z}_{r}}\bigr]\;=\;\exp\!\left(\frac{L(L-1)^{2}\,r^{2}(1-r^{2})}{2\bigl[1-(L-1)(1-r^{2})\bigr]}\,N+\mathcal{O}(1)\right),\qquad\text{if }(L-1)(1-r^{2})<1,(98)

while for(L−1)​(1−r2)≥1(L-1)(1-r^{2})\geq 1the average diverges at this (CLT) level of description, the quadratic term∑a<bζa​ζb\sum_{a<b}\zeta^{a}\zeta^{b}overwhelming the Gaussian decay of theζ\zeta’s. In either case the annealed average of the fluctuation grows exponentially inNN(or worse): it is dominated by rareζ\zeta’s, not by typical ones. The exact gap between annealed and typical rates is(L2)​(1−r2)−ΣL​(r)>0\binom{L}{2}(1-r^{2})-\Sigma_{L}(r)>0, to which (98) reduces at quadratic order in the deviationm−rm-r; the divergence of (98) for(L−1)​(1−r2)≥1(L-1)(1-r^{2})\geq 1merely signals that the dominant deviations then leave the central𝒪​(N−1/2)\mathcal{O}(N^{-1/2})window, where they are correctly controlled by the tilted rate function (88) rather than by its quadratic approximation. By contrast𝒵r/N→0\mathcal{Z}_{r}/N\to 0almost surely, so1N​E^1→N→∞a.s.−(L2)​(1−r2),1N​log⁡Xi(1|a)→N→∞a.s.−(L2)​(1−r2),\frac{1}{N}\hat{E}_{1}\;\xrightarrow[N\to\infty]{\mathrm{a.s.}}\;-\binom{L}{2}\bigl(1-r^{2}\bigr),\qquad\frac{1}{N}\log X_{i}^{(1|a)}\;\xrightarrow[N\to\infty]{\mathrm{a.s.}}\;-\binom{L}{2}\bigl(1-r^{2}\bigr),(99)

the on-site factor being𝒪​(1)\mathcal{O}(1): at the typical stateF1c→(L−1)​rF_{1}^{c}\to(L-1)rand the average over the on-site masks gives[cosh⁡((L−1)​r)+r​sinh⁡((L−1)​r)]L−1\bigl[\cosh((L-1)r)+r\sinh((L-1)r)\bigr]^{L-1}, although the𝒪​(N)\mathcal{O}(\sqrt{N})Gaussian fluctuation𝒵r\mathcal{Z}_{r}prevents any deterministic𝒪​(1)\mathcal{O}(1)prefactor from being attached to the typical signal. Comparing the typical rate (99) with the noise variance (28) amounts to the replacementΣL​(r)→(L2)​(1−r2)\Sigma_{L}(r)\to\binom{L}{2}(1-r^{2})in the capacity exponent of (41),εLtyp​(r)=ρL−L​(L−1)​(1−r2),\varepsilon_{L}^{\mathrm{typ}}(r)\;=\;\rho_{L}-L(L-1)\bigl(1-r^{2}\bigr),(100)

which is positive iff1−r2<ρL/[L​(L−1)]1-r^{2}<\rho_{L}/[L(L-1)]. UsingρL=L​[(L−1)−ϕL​(x∗)]\rho_{L}=L[(L-1)-\phi_{L}(x^{*})]this condition takes the closed formr>rctyp​(L)=ϕL​(x∗)L−1​∼L→∞​1−log⁡2L−1⟶1,r\;>\;r_{c}^{\mathrm{typ}}(L)\;=\;\sqrt{\frac{\phi_{L}(x^{*})}{L-1}}\;\underset{L\to\infty}{\sim}\;\sqrt{1-\frac{\log 2}{L-1}}\;\longrightarrow\;1,(101)

equivalentlyrctyp=1−ρL/[L​(L−1)]r_{c}^{\mathrm{typ}}=\sqrt{1-\rho_{L}/[L(L-1)]}, as quoted in (43). Atr=1r=1the masks are deterministic,ζa≡0\zeta^{a}\equiv 0and𝒵r≡0\mathcal{Z}_{r}\equiv 0, and annealed and typical coincide, both reducing to the exact computation ofA: the bracketcosh⁡(L−1)+sinh⁡(L−1)=eL−1\cosh(L-1)+\sinh(L-1)=e^{L-1}givese(L−1)2e^{(L-1)^{2}}, the leading rate vanishes, and the signal ise−(L−1)​sinh⁡(L−1)e^{-(L-1)}\sinh(L-1).

## Which criterion the dynamics realises

The two ratesΣL​(r)\Sigma_{L}(r)(annealed) and(L2)​(1−r2)\binom{L}{2}(1-r^{2})(typical)
bracket the finite-NNrecovery threshold, and it is legitimate to ask which one
the one-step dynamics actually obeys. The point is settled empirically in
§7, and the answer is the annealed one; here we record why
this is the theoretically consistent reading, not a coincidence. The one-step
overlap (40) is by constructionerf​(μ1​(r)/2​σ2​(r))\mathrm{erf}\!\bigl(\mu_{1}(r)/\sqrt{2\sigma^{2}(r)}\bigr)withμ1​(r)=𝔼​[Xi(1|a)]\mu_{1}(r)=\mathbb{E}[X_{i}^{(1|a)}]the annealed first moment, precisely the
prescription of the single-layer model[6]. There the
cavity exponent is linear in the masks, the annealed average factorises,μ1=e−1​sinh⁡(1)​[12​((1+r)+(1−r)​e−2)]N−1\mu_{1}=e^{-1}\sinh(1)\,[\tfrac{1}{2}((1+r)+(1-r)e^{-2})]^{N-1}, and it equals
the typical signal becauselog⁡X(1)\log X^{(1)}is a sum of i.i.d. per-site
contributions and self-averages; the annealed/typical distinction is empty and
the thresholdrc≃0.337r_{c}\simeq 0.337matches the Monte Carlo. The multilayer exponentE^1\hat{E}_{1}is quadratic in the masks (83),log⁡X(1)\log X^{(1)}no
longer self-averages, and the distinction opens. But the signal is still carried
by a single pattern:E^1\hat{E}_{1}is one random variable per disorder
realisation, and the retrieval curve is an average over independent realisations,
which samples its𝒪​(N)\mathcal{O}(\sqrt{N})upward fluctuations. AveragingX(1)=eE^1​(⋯)X^{(1)}=e^{\hat{E}_{1}}(\cdots)over the masks returnsμ1​(r)\mu_{1}(r)by definition, so
the annealed moment is the operative one and the closed form built on it is the
one the data confirm. Replacingμ1​(r)\mu_{1}(r)by its typical value would discard the
fluctuations that dominate the average at every finiteNN; the typical rate
would control the recall only in anN→∞N\to\inftylimit at fixed sub-exponential
loadPP, incompatible withP∼eN​εL​(r)P\sim e^{N\varepsilon_{L}(r)}. Finally, the same
rare-event inflation makes the annealed noise variance (28)
a conservative overestimate (Remark2), so the measured
basin is if anything slightly larger than the annealed-signal /
annealed-noise erf predicts –an overshoot toward larger basins, never toward the
typical threshold.

## Numerical thresholds and finite-NNchecks

Table2of the main text collects the thresholdsrc​(L)r_{c}(L)(fromΣL​(rc)=ρL/2\Sigma_{L}(r_{c})=\rho_{L}/2) andrctyp​(L)r_{c}^{\mathrm{typ}}(L)forL=2,…,10L=2,\dots,10; Table5resolves theL=2L=2case inrr.

## Large-LLasymptotics of the thresholds

AsL→∞L\to\inftythe two criteria behave in opposite ways. For the typical one,ϕL​(x∗)∼(L−1)−log⁡2\phi_{L}(x^{*})\sim(L-1)-\log 2in (101) gives1−rctyp​2≃log⁡2/(L−1)→01-r_{c}^{\mathrm{typ}\,2}\simeq\log 2/(L-1)\to 0, i.e. a tolerated Hamming radius shrinking asdctyp≃log⁡2/[4​(L−1)]d_{c}^{\mathrm{typ}}\simeq\log 2/[4(L-1)]. For the annealed one, the saddle freezes:ms→1m_{s}\to 1andlog⁡cosh⁡(xs)=xs−log⁡2+o​(1)\log\cosh(x_{s})=x_{s}-\log 2+o(1), so thatΣL​(r)=L​[log⁡2−ar+log⁡cosh⁡(ar)]+o​(L),\Sigma_{L}(r)\;=\;L\bigl[\log 2-a_{r}+\log\cosh(a_{r})\bigr]+o(L),(102)

and the threshold conditionΣL​(rc)=ρL/2∼(L/2)​log⁡2\Sigma_{L}(r_{c})=\rho_{L}/2\sim(L/2)\log 2reduces toar−log⁡cosh⁡(ar)=12​log⁡2⟺e−2​ar=2−1,a_{r}-\log\cosh(a_{r})\;=\;\tfrac{1}{2}\log 2\quad\Longleftrightarrow\quad e^{-2a_{r}}\;=\;\sqrt{2}-1,(103)

whose solution isrc=tanh⁡(ar)=2−1≈0.4142r_{c}=\tanh(a_{r})=\sqrt{2}-1\approx 0.4142, the finite limit quoted in §6and approached from below in Table2.rrms​(r)m_{s}(r)Σ2​(r)\Sigma_{2}(r)ε2​(r)=ρ2−2​Σ2​(r)\varepsilon_{2}(r)=\rho_{2}-2\Sigma_{2}(r)0.20.73350.8066−0.2663-0.26630.30.80600.6951−0.0433-0.04330.31950.81720.673500.40.85650.5851+0.1768+0.17680.50.89450.4781+0.3908+0.39080.57140.91640.4039+0.5391+0.53910.70.94840.2754+0.7961+0.79610.90.98540.0882+1.1706+1.1706Table 5:Tilted saddle data atL=2L=2: saddle pointms​(r)m_{s}(r), annealed signal rateΣ2​(r)\Sigma_{2}(r)and capacity exponentε2​(r)\varepsilon_{2}(r). The exponent vanishes at the annealed thresholdrc=0.3195r_{c}=0.3195; the rowr=0.5714r=0.5714marks the typical thresholdrctyp=ϕ2​(x∗)r_{c}^{\mathrm{typ}}=\sqrt{\phi_{2}(x^{*})}.

## Remark 5(Finite-NNprefactors).

As inB, the prefactor (97) is written at leading Laplace order, treating the cavity magnetisations as empirical means ofNN(rather thanN−1N-1) variables and absorbing the local-CLT normalisation. Restoring both, the corrected prefactor readsC^L​(r)=sinh⁡((L−1)​ms)​[cosh⁡((L−1)​ms)+r​sinh⁡((L−1)​ms)]L−1​(1−ms2)−L/2detℋL,r∗​eΣL​(r)−(L2)​(1+ms2).\widehat{C}_{L}(r)\;=\;\sinh\bigl((L-1)m_{s}\bigr)\bigl[\cosh\bigl((L-1)m_{s}\bigr)+r\sinh\bigl((L-1)m_{s}\bigr)\bigr]^{L-1}\frac{(1-m_{s}^{2})^{-L/2}}{\sqrt{\det\mathcal{H}_{L,r}^{*}}}\,e^{\Sigma_{L}(r)-\binom{L}{2}(1+m_{s}^{2})}.(104)

Asr→1r\to 1one findsC^L​(r)→e−(L−1)​sinh⁡(L−1)\widehat{C}_{L}(r)\to e^{-(L-1)}\sinh(L-1), matching exactly the perfect-recall signal (20). We verified (104) atL=2L=2against the exact double-binomial enumeration ofμ1​(r)\mu_{1}(r): atN=800N=800the enumerated ratioμ1​(r)​eN​Σ2​(r)\mu_{1}(r)\,e^{N\Sigma_{2}(r)}equals0.53590.5359atr=0.5r=0.5and0.48870.4887atr=0.7r=0.7, againstC^2​(0.5)=0.5368\widehat{C}_{2}(0.5)=0.5368andC^2​(0.7)=0.4896\widehat{C}_{2}(0.7)=0.4896, with residual𝒪​(N−1)\mathcal{O}(N^{-1})corrections. The same finite-NNbookkeeping applies to the noise prefactorKLK_{L}(cavity exclusion plus a factor22from the two symmetric saddles±m∗​𝟏\pm m^{*}\bm{1}of the even integrand (60)); none of it affects the ratesρL\rho_{L},ΣL​(r)\Sigma_{L}(r)or the thresholds of Table2.

## Appendix DSingle-layer squared-overlap model

We consider a single-layer (L=1L=1) variant of the exponential Hopfield model in which the exponent is built from the squared Mattis magnetisation rather than from the linear one. The cost function readsℋsq​(𝝈|𝝃)=−N​∑μ=1Pexp⁡[N​(mμ2−1)],\mathcal{H}_{\mathrm{sq}}(\bm{\sigma}\,|\,\bm{\xi})\;=\;-\,N\sum_{\mu=1}^{P}\exp\!\bigl[\,N\,(m_{\mu}^{2}-1)\,\bigr],(105)

withmμ=1N​∑iξiμ​σim_{\mu}=\frac{1}{N}\sum_{i}\xi_{i}^{\mu}\sigma_{i}the standard Mattis magnetisation.

The key structural difference with respect to the linear-exponent model[6]ℋlin​(𝝈|𝝃)=−N​∑μ=1Pexp⁡[N​(mμ−1)]\mathcal{H}_{\mathrm{lin}}(\bm{\sigma}\,|\,\bm{\xi})\;=\;-\,N\sum_{\mu=1}^{P}\exp\!\bigl[\,N\,(m_{\mu}-1)\,\bigr](106)

is the restoredℤ2\mathbb{Z}_{2}symmetry: sinceℋsq\mathcal{H}_{\mathrm{sq}}depends only onmμ2m_{\mu}^{2}, it is invariant under the global spin flip𝝈↦−𝝈\bm{\sigma}\mapsto-\bm{\sigma}, and each stored pattern is retrieved as a pair{𝝃μ,−𝝃μ}\{\bm{\xi}^{\mu},-\bm{\xi}^{\mu}\}. The linear-exponent model (106) breaks this symmetry, favouringmμ=+1m_{\mu}=+1only.

## Cavity decomposition and local field

Introducing the cavity magnetisationm^μ=1N​∑j≠iξjμ​σj\hat{m}_{\mu}=\frac{1}{N}\sum_{j\neq i}\xi_{j}^{\mu}\sigma_{j}, the squared overlap expands asN​(mμ2−1)=N​(m^μ2−1)⏟=⁣:E^μ+2​m^μ​ξiμ​σi+𝒪​(N−1),N\,(m_{\mu}^{2}-1)\;=\;\underbrace{N\,(\hat{m}_{\mu}^{2}-1)}_{=:\,\hat{E}_{\mu}}\;+\;2\,\hat{m}_{\mu}\,\xi_{i}^{\mu}\sigma_{i}\;+\;\mathcal{O}(N^{-1}),(107)

so that the Hamiltonian decomposes asℋsq=−N​[Ci+σi​hi]​(1+𝒪​(N−1))\mathcal{H}_{\mathrm{sq}}=-N[\,C_{i}+\sigma_{i}\,h_{i}\,](1+\mathcal{O}(N^{-1}))with local fieldhi=∑μ=1Pξiμ​eE^μ​sinh⁡(2​m^μ),E^μ=N​(m^μ2−1).{\;h_{i}\;=\;\sum_{\mu=1}^{P}\xi_{i}^{\mu}\,e^{\hat{E}_{\mu}}\,\sinh(2\hat{m}_{\mu}),\qquad\hat{E}_{\mu}=N\,(\hat{m}_{\mu}^{2}-1).\;}(108)

The zero-temperature Glauber update isσi​(t+1)=sign​[hi​(t)]\sigma_{i}(t+1)=\mathrm{sign}[h_{i}(t)], identical in structure to (16) for the hetero-associative network (specialised toL=1L=1with the replacementsinh⁡(Fμa)→sinh⁡(2​m^μ)\sinh(F_{\mu}^{a})\to\sinh(2\hat{m}_{\mu})).

## Signal-to-noise analysis

We test stability of the recalled ground state𝝈=𝝃1\bm{\sigma}=\bm{\xi}^{1}by computing the moments ofXi:=ξi1​hi|𝝈=𝝃1X_{i}:=\xi_{i}^{1}h_{i}\big|_{\bm{\sigma}=\bm{\xi}^{1}}.

## First moment

The self-signal (μ=1\mu=1) is deterministic at leading order,m^1=(N−1)/N\hat{m}_{1}=(N-1)/N, givingE^1=−2+𝒪​(N−1)\hat{E}_{1}=-2+\mathcal{O}(N^{-1}). The noise patterns (μ≠1\mu\neq 1) have zero mean by Rademacher independence at siteii. Henceμ1=𝔼​[Xi]=e−2​sinh⁡(2)+𝒪​(N−1).\mu_{1}\;=\;\mathbb{E}[X_{i}]\;=\;e^{-2}\sinh(2)+\mathcal{O}(N^{-1}).(109)

## Second moment

Off-diagonal contributions (μ≠ν\mu\neq\nu) vanish by the same Rademacher-independence argument as in §4. The diagonal noise contribution (μ≠1\mu\neq 1) reduces to the cavity expectation𝔼​[(Xi(μ))2]=𝔼​[e2​N​(m^μ2−1)​sinh2⁡(2​m^μ)],μ≠1.\mathbb{E}\bigl[(X_{i}^{(\mu)})^{2}\bigr]\;=\;\mathbb{E}\!\bigl[\,e^{2N(\hat{m}_{\mu}^{2}-1)}\,\sinh^{2}(2\hat{m}_{\mu})\,\bigr],\qquad\mu\neq 1.(110)

In contrast to the linear model, where the cavity exponentN​(m^μ−1)N(\hat{m}_{\mu}-1)islinearin the Rademacher variables (and the expectation factorises into a closed-form productcosh(2)N−1\cosh(2)^{N-1}), here the exponentN​(m^μ2−1)N(\hat{m}_{\mu}^{2}-1)isquadraticand the expectation no longer factorises. A genuine saddle-point treatment is required.

## Noise rate and prefactor

FollowingB, by Cramér’s theorem,m^μ\hat{m}_{\mu}satisfies a large-deviation principle with rate functionIR​(m)I_{R}(m). Varadhan’s lemma identifies the leading exponential decay of (110) as a one-dimensional variational problem. The functionalg​(m):=2​m2−IR​(m)g(m):=2m^{2}-I_{R}(m)is even inmm; its unique positive maximiserm∗m^{*}satisfiesm∗=tanh⁡(4​m∗),m^{*}=\tanh(4\,m^{*}),(111)

or equivalently, withx∗=4​m∗x^{*}=4m^{*},tanh⁡(x∗)=x∗4.\tanh(x^{*})=\frac{x^{*}}{4}.(112)

A Laplace evaluation around the saddle yields𝔼​[(Xi(μ))2]=K​e−N​ρ​(1+o​(1)),\mathbb{E}\bigl[(X_{i}^{(\mu)})^{2}\bigr]\;=\;K\,e^{-N\rho}\bigl(1+o(1)\bigr),(113)

with the noise rateρ=2−ϕ​(x∗),ϕ​(x)=−x28+log⁡cosh⁡(x),{\;\rho\;=\;2-\phi(x^{*}),\qquad\phi(x)=-\frac{x^{2}}{8}+\log\cosh(x),\;}(114)

and the polynomial prefactorK=sinh2⁡(2​m∗)1−4​(1−m∗2).K\;=\;\frac{\sinh^{2}(2m^{*})}{\sqrt{1-4(1-m^{*2})}}.(115)

Numerically, the saddle data are collected in Table6.x∗x^{*}m∗=x∗/4m^{*}=x^{*}/4ϕ​(x∗)\phi(x^{*})ρ=2−ϕ​(x∗)\rho=2-\phi(x^{*})KK3.99733.99730.999330.999331.30721.30720.69280.692813.1513.15Table 6:Saddle data, noise rate and prefactor for the squared-overlap model.

## Storage capacity

Combining the signal (109) and the varianceσ2=(P−1)​K​e−N​ρ\sigma^{2}=(P-1)\,K\,e^{-N\rho}, the Mattis magnetisation after one parallel update readsm1(1)=erf​(e−2​sinh⁡(2)2​(P−1)​K​e−N​ρ),m_{1}^{(1)}\;=\;\mathrm{erf}\!\left(\frac{e^{-2}\sinh(2)}{\sqrt{2(P-1)\,K\,e^{-N\rho}}}\right),(116)

which tends to unity as long asP​e−N​ρ→0P\,e^{-N\rho}\to 0.

The qualitative conditionP​e−N​ρ→0P\,e^{-N\rho}\to 0can be turned into a quantitative bound on the load, mirroring the derivation of (30) for the hetero-associative network. Within the Gaussian approximation, the single-spin stability conditionXi>0X_{i}>0holds with probabilityℙ​(Xi>0)=1−12​erfc​(μ12​σ2).\mathbb{P}\bigl(X_{i}>0\bigr)\;=\;1-\tfrac{1}{2}\,\mathrm{erfc}\!\Bigl(\tfrac{\mu_{1}}{\sqrt{2\sigma^{2}}}\Bigr).(117)

Requiring a per-spin error probability≤N−a\leq N^{-a},a>0a>0, so that the union bound over theNNsites remains summable in the thermodynamic limit, givesμ122​σ2≥a​log⁡N+𝒪​(log⁡log⁡N),\frac{\mu_{1}^{2}}{2\sigma^{2}}\;\geq\;a\log N+\mathcal{O}(\log\log N),(118)

and substituting the signal (109) and the varianceσ2=(P−1)​K​e−N​ρ\sigma^{2}=(P-1)\,K\,e^{-N\rho},P≤1+e−4​sinh2⁡(2)2​a​K​log⁡N​eN​ρ.{\;P\;\leq\;1+\frac{e^{-4}\sinh^{2}(2)}{2\,a\,K\,\log N}\;e^{N\rho}.\;}(119)

The leading-order storage capacity is thereforePc∼eN​ρ,ρ≈0.6928.P_{c}\;\sim\;e^{N\rho},\qquad\rho\approx 0.6928.(120)

## Consistency with the configuration-space ceiling2N2^{N}

Since the network possesses only2N2^{N}distinct configurations, any sensible storage estimate must satisfyP<2NP<2^{N}. The bound (119) does, for everyNN, for two concurrent reasons. First, the rate lies strictly belowlog⁡2\log 2: sinceϕ​(x∗)=maxx⁡ϕ​(x)≥ϕ​(4)\phi(x^{*})=\max_{x}\phi(x)\geq\phi(4)andϕ​(4)=−2+log⁡cosh⁡(4)=2−log⁡2+log⁡(1+e−8)\phi(4)=-2+\log\cosh(4)=2-\log 2+\log\bigl(1+e^{-8}\bigr),ρ=2−ϕ​(x∗)≤log⁡21+e−8<log⁡2,\rho\;=\;2-\phi(x^{*})\;\leq\;\log\frac{2}{1+e^{-8}}\;<\;\log 2,(121)

numericallyρ=0.692811<log⁡2=0.693147\rho=0.692811<\log 2=0.693147, so thateN​ρ/2N=e−N​(log⁡2−ρ)→0e^{N\rho}/2^{N}=e^{-N(\log 2-\rho)}\to 0, albeit slowly (log⁡2−ρ≃3.4×10−4\log 2-\rho\simeq 3.4\times 10^{-4}). The ceiling (121) is the squared-overlap counterpart of the linear-model rateρlin=log⁡[2/(1+e−4)]\rho_{\mathrm{lin}}=\log[2/(1+e^{-4})]: theℤ2\mathbb{Z}_{2}-symmetric exponent doubles the argument of the exponentially small correction,e−4→e−8e^{-4}\to e^{-8}, pushing the rate closer to the absolute boundlog⁡2\log 2. Second, the prefactor in (119) is itself small,e−4​sinh2⁡(2)/(2​a​K​log⁡N)≃9.2×10−3/(a​log⁡N)e^{-4}\sinh^{2}(2)/(2aK\log N)\simeq 9.2\times 10^{-3}/(a\log N). Table7reports the numerical comparison ata=1a=1: the estimate (119) stays more than two orders of magnitude below2N2^{N}over the whole range of sizes, with a gap that widens asNNgrows. The same conclusion holds a fortiori if the leading-Laplace prefactorKKis replaced by the finite-NN-corrected valueK^≈0.97\widehat{K}\approx 0.97of Remark7below, which raises the bound by roughly one decade but leaves it well under the ceiling.NNlog10⁡Pmax\log_{10}P_{\max}from (119)log10⁡2N\log_{10}2^{N}log10⁡(Pmax/2N)\log_{10}\bigl(P_{\max}/2^{N}\bigr)100.613.01−2.40-2.40203.506.02−2.52-2.525012.4115.05−2.64-2.6410027.3930.10−2.72-2.7220057.4160.21−2.79-2.79500147.61150.52−2.91-2.911000298.01301.03−3.02-3.02Table 7:Storage estimate (119) (ata=1a=1) against the configuration-space ceiling2N2^{N}for several system sizes: the bound is below2N2^{N}at everyNN, as required.

## Comparison with the linear-exponent model

The linear-exponent model (106) has a closed-form noise rateρlin=log⁡[21+e−4]≈0.6750\rho_{\mathrm{lin}}=\log\bigl[\frac{2}{1+e^{-4}}\bigr]\approx 0.6750, obtained without saddle-point analysis since the cavity exponent is linear.

Two key differences emerge:
- 1.

Analytic structure.The linear model factorises over sites (𝔼[e2​N​m^μ]=cosh(2)N−1\mathbb{E}[e^{2N\hat{m}_{\mu}}]=\cosh(2)^{N-1}); the squared model requires a genuine saddle-point integral.
- 2.

ℤ2\mathbb{Z}_{2}symmetry and capacity.The squared-overlap rate is the larger of the two,ρsq≈0.6928>ρlin≈0.6750\rho_{\mathrm{sq}}\approx 0.6928>\rho_{\mathrm{lin}}\approx 0.6750, and lies closer to the ceilinglog⁡2≈0.6931\log 2\approx 0.6931: penalising1−mμ21-m_{\mu}^{2}rather than1−mμ1-m_{\mu}rewards alignment with either sign of the pattern and thereby tightens the noise suppression.

Figure10displays the theoretical predictions (116) and the corresponding linear-model formula from[6]atN=10N=10, with Monte-Carlo markers from the zero-temperature one-step dynamics of both models . The two models are nearly indistinguishable forP≲5×102P\lesssim 5\times 10^{2}, where both achieve perfect recall (m1(1)≈1m_{1}^{(1)}\approx 1). AsPPapproaches the critical storage, the curves separate: the larger noise rate of the squared model is offset at finiteNNby its larger prefactorK≈13.15K\approx 13.15, placing the effective transition at somewhat lowerPP. In the thermodynamic limit, however, the exponential rateρsq>ρlin\rho_{\mathrm{sq}}>\rho_{\mathrm{lin}}implies that the squared model stores strictly more patterns at leading order (panel (b)).Figure 10:Squared-overlap versus linear-exponent model (L=1L=1).(a)One-step magnetisationm1(1)m_{1}^{(1)}versus loadPPatN=10N=10for
the linear-exponent modelℋlin=−N​∑μeN​(mμ−1)\mathcal{H}_{\mathrm{lin}}=-N\sum_{\mu}e^{N(m_{\mu}-1)}(solid) and the squared-overlap modelℋsq=−N​∑μeN​(mμ2−1)\mathcal{H}_{\mathrm{sq}}=-N\sum_{\mu}e^{N(m_{\mu}^{2}-1)}(dashed). The two
coincide up toP∼5×102P\!\sim\!5\times 10^{2}; at finiteNNthe squared model’s larger
prefactorK≈13.15K\approx 13.15moves its knee to slightly lowerPPdespite its
larger rate. Markers are Monte-Carlo (mean±\pmstd over seeds), from the
one-step dynamics of each model in the collision-free regimeP≪2NP\ll 2^{N}.(b)Noise rates against the absolute ceilinglog⁡2\log 2: theℤ2\mathbb{Z}_{2}-symmetric squared exponent (ρ≈0.6928\rho\approx 0.6928) sits closer to
the ceiling than the linear one (ρ≈0.6750\rho\approx 0.6750).

## Basins of attraction

Following the protocol of[6], we now quantify the basins of attraction of the stored patterns by feeding the zero-temperature dynamics with a corrupted version of the archetype. The initial configuration isσj(0)=ξ~j1:=sj​ξj1\sigma_{j}^{(0)}=\tilde{\xi}_{j}^{1}:=s_{j}\,\xi_{j}^{1}, where the corruption maskssj∈{−1,+1}s_{j}\in\{-1,+1\}are i.i.d. with𝔼​[sj]=r∈(0,1]\mathbb{E}[s_{j}]=r\in(0,1], so that the initial Mattis overlap ism1(0)=rm_{1}^{(0)}=rand the Hamming distance per neuron isd=(1−r)/2d=(1-r)/2. The quantity controlling one parallel update of spiniiis againXi=ξi1​hi|𝝈=𝝃~1X_{i}=\xi_{i}^{1}h_{i}\big|_{\bm{\sigma}=\tilde{\bm{\xi}}^{1}}, now with cavity magnetisationsm^1=1N​∑j≠isj,m^μ=1N​∑j≠iξjμ​ξ~j1(μ≠1),\hat{m}_{1}=\frac{1}{N}\sum_{j\neq i}s_{j},\qquad\hat{m}_{\mu}=\frac{1}{N}\sum_{j\neq i}\xi_{j}^{\mu}\,\tilde{\xi}_{j}^{1}\quad(\mu\neq 1),(122)

and, within the Gaussian (CLT) approximation and the large-NNreplacement of the empirical site average by an expectation, exactly as in[6], the post-update magnetisation ism1(1)=erf​[μ1​(r)/2​(μ2−μ12)]m_{1}^{(1)}=\mathrm{erf}\bigl[\mu_{1}(r)/\sqrt{2(\mu_{2}-\mu_{1}^{2})}\bigr].

## The noise channel is insensitive to the corruption

Forμ≠1\mu\neq 1the productsuj:=ξjμ​ξ~j1u_{j}:=\xi_{j}^{\mu}\tilde{\xi}_{j}^{1}are i.i.d. symmetric Rademacher variables for every value ofrr, becauseξjμ\xi_{j}^{\mu}is a symmetric sign independent ofξ~j1\tilde{\xi}_{j}^{1}. The entire noise computation leading to (113) therefore carries over verbatim: each of theP−1P-1noise patterns contributes zero mean and per-pattern varianceK​e−N​ρK\,e^{-N\rho}, withρ\rho,KKgiven by (114)–(115), the off-diagonal contributions vanish by on-site independence, andσ2=μ2−μ12≃(P−1)​K​e−N​ρ,independently of​r.\sigma^{2}\;=\;\mu_{2}-\mu_{1}^{2}\;\simeq\;(P-1)\,K\,e^{-N\rho},\qquad\text{independently of }r.(123)

(As in[6], the fluctuations of the signal term itself are dropped fromμ2−μ12\mu_{2}-\mu_{1}^{2}; see Remark6for the caveats attached to this step.)

## The corrupted signal requires a tilted saddle point

The signal term readsXi(1)=eN​(m^12−1)​sinh⁡(2​m^1),m^1=1N​∑j≠isj.X_{i}^{(1)}\;=\;e^{N(\hat{m}_{1}^{2}-1)}\,\sinh(2\hat{m}_{1}),\qquad\hat{m}_{1}=\frac{1}{N}\sum_{j\neq i}s_{j}.(124)

In the linear-exponent model the corresponding average factorises exactly over sites,𝔼​[e∑j≠isj]=(cosh⁡1+r​sinh⁡1)N−1\mathbb{E}\bigl[e^{\sum_{j\neq i}s_{j}}\bigr]=\bigl(\cosh 1+r\sinh 1\bigr)^{N-1}, which produces the closed form used in[6]. Here this step is not possible: the exponent is quadratic inm^1\hat{m}_{1}and the expectation does not factorise. The viable substitute, as for the noise evaluation (110), is a large-deviation analysis, now with a biased reference measure. By Cramér’s theorem the empirical mean of the masks satisfies an LDP with the tilted rate functionIr​(m)=1+m2​log⁡1+m1+r+1−m2​log⁡1−m1−r=IR​(m)−ar​m+log⁡cosh⁡(ar),ar:=tanh−1⁡(r),I_{r}(m)\;=\;\frac{1+m}{2}\log\frac{1+m}{1+r}+\frac{1-m}{2}\log\frac{1-m}{1-r}\;=\;I_{R}(m)-a_{r}\,m+\log\cosh(a_{r}),\qquad a_{r}:=\tanh^{-1}(r),(125)

which vanishes atm=rm=ronly, and Varadhan’s lemma gives the annealed signalμ1​(r)=𝔼​[Xi(1)]=C​(r)​e−N​Σ​(r)​(1+o​(1)),Σ​(r):=1−supm∈[−1,1][m2−Ir​(m)].\mu_{1}(r)\;=\;\mathbb{E}\bigl[X_{i}^{(1)}\bigr]\;=\;C(r)\,e^{-N\Sigma(r)}\bigl(1+o(1)\bigr),\qquad\Sigma(r)\;:=\;1-\sup_{m\in[-1,1]}\bigl[\,m^{2}-I_{r}(m)\,\bigr].(126)

The supremum is attained at the unique positive solutionms=ms​(r)m_{s}=m_{s}(r)oftanh−1⁡(ms)=2​ms+ar⟺ms=tanh⁡(2​ms+ar),\tanh^{-1}(m_{s})\;=\;2m_{s}+a_{r}\quad\Longleftrightarrow\quad m_{s}=\tanh\bigl(2m_{s}+a_{r}\bigr),(127)

which generalises the noise saddle (111) (the bias shifts the linear branch, pullingmsm_{s}towards11asr→1r\to 1), and the same algebra leading to (114) yields the explicit rateΣ​(r)=1+ms2−log⁡cosh⁡(2​ms+ar)+log⁡cosh⁡(ar).{\;\Sigma(r)\;=\;1+m_{s}^{2}-\log\cosh\bigl(2m_{s}+a_{r}\bigr)+\log\cosh(a_{r}).\;}(128)

The Laplace prefactor at leading order isC​(r)=sinh⁡(2​ms)1−2​(1−ms2),C(r)\;=\;\frac{\sinh(2m_{s})}{\sqrt{1-2\,(1-m_{s}^{2})}},(129)

well defined becausems​(r)≥ms​(0)=0.9575>1/2m_{s}(r)\geq m_{s}(0)=0.9575>1/\sqrt{2}for everyr≥0r\geq 0. Sanity checks: asr→1r\to 1the rate function freezes the saddle atms→1m_{s}\to 1andΣ​(r)→0\Sigma(r)\to 0, recovering the𝒪​(1)\mathcal{O}(1)signal of the perfect-recall analysis; atr→0+r\to 0^{+}the saddle equation reduces toms=tanh⁡(2​ms)m_{s}=\tanh(2m_{s})andΣ​(0)=0.6735\Sigma(0)=0.6735, whileμ1​(0)=0\mu_{1}(0)=0identically by parity (the two saddles±ms\pm m_{s}cancel in the odd integrand), consistently with the loss of any retrieval drive for an uncorrelated input.

## One-step magnetisation and storage under corruption

Combining (123) and (126), the Mattis magnetisation after one parallel update readsm1(1)=erf​(C​(r)​e−N​Σ​(r)2​(P−1)​K​e−N​ρ)m_{1}^{(1)}\;=\;\mathrm{erf}\!\left(\frac{C(r)\,e^{-N\Sigma(r)}}{\sqrt{2(P-1)\,K\,e^{-N\rho}}}\right)(130)

(with the finite-NNprefactor corrections of Remark7, eq. (130) reduces exactly to (116) asr→1r\to 1), and it tends to unity if and only ifP​e−N​ε​(r)→0,ε​(r):=ρ−2​Σ​(r).P\,e^{-N\varepsilon(r)}\;\to\;0,\qquad\varepsilon(r)\;:=\;\rho-2\,\Sigma(r).(131)

Parametrising the load asP=γ​C​(r)2K​eN​ε​(r)P=\gamma\,\frac{C(r)^{2}}{K}\,e^{N\varepsilon(r)}, in analogy with the load parametrisation adopted in[6], eq. (130) collapses onto the universal profilem1(1)=erf​(12​γ),m_{1}^{(1)}\;=\;\mathrm{erf}\!\left(\frac{1}{\sqrt{2\gamma}}\right),(132)

and the union-bound argument leading to (119) now gives the corruption-dependent storage estimateP≤1+C​(r)22​a​K​log⁡N​eN​ε​(r),Pc​(r)∼eN​ε​(r).{\;P\;\leq\;1+\frac{C(r)^{2}}{2\,a\,K\,\log N}\;e^{N\varepsilon(r)},\qquad P_{c}(r)\;\sim\;e^{N\varepsilon(r)}.\;}(133)

The storage capacity therefore remains exponential inNNfor every corruption level such thatε​(r)>0\varepsilon(r)>0, i.e.Σ​(r)<ρ2≃0.3464⟺r>rc≃0.4032,d<dc=1−rc2≃0.2984,\Sigma(r)<\frac{\rho}{2}\simeq 0.3464\quad\Longleftrightarrow\quad r>r_{c}\simeq 0.4032,\qquad d<d_{c}=\frac{1-r_{c}}{2}\simeq 0.2984,(134)

the threshold being obtained by solvingΣ​(rc)=ρ/2\Sigma(r_{c})=\rho/2numerically along (127)–(128). Table8collects the saddle data. As in the linear model, enlarging the basins (decreasingrr) lowers the storage exponent without ever destroying its exponential character above threshold; atr=1r=1one recoversε​(1)=ρ\varepsilon(1)=\rhoand the fixed-point results of the previous subsections. For comparison, the same (annealed) criterion applied to the linear-exponent model givesrclin≃0.3374r_{c}^{\mathrm{lin}}\simeq 0.3374[6]: the squared-overlap model trades slightly narrower basins of attraction for its larger storage rateρsq>ρlin\rho_{\mathrm{sq}}>\rho_{\mathrm{lin}}, in line with the intuition that a sharper energy landscape stores more memories at the price of robustness. Note also that the threshold (134) coincides with theL=3L=3value of the hetero-associative analysis of §6(Table2): the squared-overlap saddle (127) is theL=3L=3specialisation of the tilted saddle (92), and signal and noise rates both rescale by the same factorL=3L=3, leaving the thresholdΣ​(rc)=ρ/2\Sigma(r_{c})=\rho/2invariant.rrms​(r)m_{s}(r)Σ​(r)\Sigma(r)ε​(r)=ρ−2​Σ​(r)\varepsilon(r)=\rho-2\Sigma(r)C​(r)C(r)0.00.95750.6735−0.6541-0.65413.6360.20.97320.4980−0.3033-0.30333.6280.40320.98360.346403.6250.50.98720.2814+0.1299+0.12993.6250.70.99340.1592+0.3743+0.37433.6260.90.99810.0503+0.5922+0.59223.6261.010+0.6928+0.6928–Table 8:Tilted saddle data for the corrupted-input analysis: saddle pointms​(r)m_{s}(r), signal rateΣ​(r)\Sigma(r), storage exponentε​(r)\varepsilon(r)and leading-Laplace prefactorC​(r)C(r). The capacity exponent vanishes atrc≃0.4032r_{c}\simeq 0.4032.

## Remark 6(Annealed versus typical signal).

The estimate (133) is built on the moments ofXiX_{i}, i.e. on the annealed signalμ1​(r)=𝔼​[Xi(1)]\mu_{1}(r)=\mathbb{E}[X_{i}^{(1)}], exactly as in the linear-exponent analysis of[6]. Forr<1r<1, however, this average is dominated by exponentially rare realisations of the corruption masks, those withm^1≃ms​(r)>r\hat{m}_{1}\simeq m_{s}(r)>r. The typical realisation has insteadm^1=r+ζ/N\hat{m}_{1}=r+\zeta/\sqrt{N}withζ∼𝒩​(0,1−r2)\zeta\sim\mathcal{N}(0,1-r^{2}), so thatN​(m^12−1)=−N​(1−r2)+2​r​ζ​N+ζ2,1N​log⁡Xi(1)→N→∞a.s.−(1−r2);N(\hat{m}_{1}^{2}-1)\;=\;-N(1-r^{2})+2r\zeta\sqrt{N}+\zeta^{2},\qquad\frac{1}{N}\log X_{i}^{(1)}\;\xrightarrow[N\to\infty]{\mathrm{a.s.}}\;-(1-r^{2});(135)

the𝒪​(N)\mathcal{O}(\sqrt{N})Gaussian term moreover forbids the assignment of any deterministic𝒪​(1)\mathcal{O}(1)prefactor to the typical signal. Sincems​(r)>rm_{s}(r)>rfor everyr<1r<1, comparing the supremum in (126) with the value of the variational functional atm=rm=rgivesΣ​(r)<1−r2\Sigma(r)<1-r^{2}strictly: the annealed signal overestimates the typical one at the exponential scale. Replacing the annealed rateΣ​(r)\Sigma(r)by the typical rate1−r21-r^{2}in the comparison with the noise yields the more conservative estimatesPctyp​(r)∼eN​[ρ−2​(1−r2)],rctyp=1−ρ/2≃0.8085,dctyp≃0.0958.P_{c}^{\mathrm{typ}}(r)\;\sim\;e^{N[\rho-2(1-r^{2})]},\qquad r_{c}^{\mathrm{typ}}=\sqrt{1-\rho/2}\;\simeq\;0.8085,\qquad d_{c}^{\mathrm{typ}}\simeq 0.0958.(136)

The same dichotomy is present, though not discussed, in the linear-exponent model: the factorisedμ1​(r)\mu_{1}(r)of[6]is also an annealed average, with ratelog⁡(cosh⁡1+r​sinh⁡1)−1\log(\cosh 1+r\sinh 1)-1strictly above the typical rate−(1−r)-(1-r)forr<1r<1; the typical criterion would give thererctyp,lin=1−ρlin/2≃0.6625r_{c}^{\mathrm{typ,lin}}=1-\rho_{\mathrm{lin}}/2\simeq 0.6625. Which of the two thresholds, (134) or (136), is realised by the finite-NNdynamics is best settled by MCMC simulations; the two estimates coincide atr=1r=1, where the basin analysis reduces to the fixed-point stability analysis above.

## Remark 7(Finite-NNprefactors).

Throughout this appendix the prefactors are evaluated at leading Laplace order, treating the cavity magnetisation as the empirical mean ofNN(rather thanN−1N-1) variables. Restoring thej≠ij\neq iexclusion and, for the noise, the contribution of both symmetric saddles±m∗\pm m^{*}of the even integrand (110), the corrected prefactors readC^​(r)=C​(r)​eΣ​(r)−1−ms2,K^=2​K​eρ−2​(1+m∗2)≈0.966.\widehat{C}(r)\;=\;C(r)\,e^{\Sigma(r)-1-m_{s}^{2}},\qquad\widehat{K}\;=\;2\,K\,e^{\rho-2(1+m^{*2})}\;\approx\;0.966.(137)

We verified both expressions against the exact binomial enumeration of the cavity magnetisation: atN=1600N=1600the enumerated per-pattern noise variance equals0.9646​e−N​ρ0.9646\,e^{-N\rho}and the enumerated signal atr=0.5r=0.5equals0.6663​e−N​Σ​(0.5)0.6663\,e^{-N\Sigma(0.5)}, to be compared withK^=0.9659\widehat{K}=0.9659andC^​(0.5)=0.6668\widehat{C}(0.5)=0.6668, with residual𝒪​(N−1)\mathcal{O}(N^{-1})corrections. Consistently,C^​(r)→e−2​sinh⁡(2)\widehat{C}(r)\to e^{-2}\sinh(2)asr→1r\to 1, matching the exact perfect-recall signal (109). These𝒪​(1)\mathcal{O}(1)factors affect only the prefactors of the storage estimates (119) and (133), never the ratesρ\rho,Σ​(r)\Sigma(r)nor the thresholds (134)–(136); they are however essential for quantitative comparisons at moderateNN, such as the finite-NNstorage curves of Figure10.

## Appendix EThe price of exponential capacity

Section3showed that one parallel sweep of
Algorithm1costsΘ​(N​L​P)\Theta(NLP)in both time and memory: to
leading order, a single read of theLLstored datasets. That cost is linear in
the number of stored patternsPP, and would be unremarkable werePPmoderate.
It is not. This appendix spells out what the exponential capacityPc∼eN​ρLP_{c}\sim e^{N\rho_{L}}of Section5implies for anyone who would
try to use it, and in what precise sense the capacity theorem is a
statement about a limit rather than about a machine.

## The cost inherits the storage rate

Fix a load fractionγ=P/Pc\gamma=P/P_{c}and let the network run at it. The per-sweep
cost is thenΘ​(N​L​P)=Θ​(γ​N​L​eN​ρL),\Theta(NLP)\;=\;\Theta\!\bigl(\gamma\,NL\,e^{N\rho_{L}}\bigr),(138)

exponential inNNwith exactly the rateρL\rho_{L}that measures the capacity. The
two are the same number wearing two hats: every bit of storage the network gains
by increasingNN(or, throughρL∼L​log⁡2\rho_{L}\sim L\log 2, by adding layers) is paid for,
one-to-one in the exponent, by the cost of writing the data down and sweeping it
once. Width is in this sense not a free lunch: the same factoreN​ρLe^{N\rho_{L}}that
buys exponentially more memories asLLgrows multiplies the cost of touching them
by the identical amount.

## A concrete instance

Take theN=64N=64,L=2L=2network already flagged in Section5as
out of computational reach, and follow the arithmetic. Withρ2=1.3470\rho_{2}=1.3470(Table4) the capacity isPc≈eN​ρ2=e86.2≈2.8×1037P_{c}\;\approx\;e^{N\rho_{2}}\;=\;e^{86.2}\;\approx\;2.8\times 10^{37}(139)

patterns. Merely storing the two datasets, at one byte per spin, already
requiresN​L​Pc≈64⋅2⋅2.8×1037≈3.5×1039​bytes,NLP_{c}\;\approx\;64\cdot 2\cdot 2.8\times 10^{37}\;\approx\;3.5\times 10^{39}\ \text{bytes},(140)

some6×10156\times 10^{15}times Avogadro’s number of bytes, or3.5×10153.5\times 10^{15}yottabytes: several SI prefixes past any storage medium that exists or
plausibly ever will. Running the modestnsteps=5n_{\mathrm{steps}}=5sweeps used
throughout this paper (I) at that load would takeΘ​(nsteps​N​L​Pc)≈1.8×1040\Theta(n_{\mathrm{steps}}NLP_{c})\approx 1.8\times 10^{40}elementary operations;
a hypothetical exaFLOP/s machine (101810^{18}operations per second, a rate no
single computer has yet sustained) would grind at it for≈1.8×1022\approx 1.8\times 10^{22}seconds, about4×1044\times 10^{4}times the current age of
the universe (≈4.4×1017\approx 4.4\times 10^{17}s). AndN=64N=64is small: a network wide
enough to be biologically interesting is exponentially further out of reach still.

## Why the experiments live atN∼10N\sim 10

By contrast, every experiment reported here keepsN≤128N\leq 128withPPseveral
orders of magnitude below its ownPcP_{c}(Tables13,14); at those sizesN​L​PNLPnever exceeds∼106\sim 10^{6}per
sweep: seconds of work on a laptop. This is not merely a convenient choice.
The storage transition sits atP∼eN​ρLP\sim e^{N\rho_{L}}, so it enters an observable
window only at smallNN: widen the network and the transition marches off
to loads no simulation can reach, leaving the memory in perfect-recall for everyPPone can actually store. SmallNNis where the physics is visible at all.

## A statement about a limit, not a machine

The tension is worth stating plainly, because it is generic to the whole
exponential family: Demircigil et al.’s binary model, Ramsauer et al.’s modern
Hopfield network, the present hetero-associative construction all share it. “The
network storeseN​ρLe^{N\rho_{L}}patterns” is an exact statement about the fixed
points of theN→∞N\to\inftytheory: for every finiteNNthe recalled archetype is
provably stable up to that many patterns. It is not, and structurally cannot be,
a statement about any device that simultaneously holds that many patterns in
memory, because no such device fits in the universe onceNNis more than a few
dozen. Exponential capacity is therefore best read as a statement about the
shape of the energy landscape, how many well-separated minima the
construction admits in principle, and not as a promise of a usable database.
What the finite-NNexperiments certify is the complementary, and physically
operative, half: at the sizes a machine can occupy, the landscape has exactly the
minima the theory predicts, with the basins the theory predicts, and the memory
behaves accordingly.

## Appendix FHidden Manifold Model: construction and protocols

This appendix specifies the generator of Section7and the four retrieval protocols run on it. The construction is the Hidden Manifold Model of Goldt et
al.[31]in its multilayer hetero-associative form; the
generalisation analysis follows the random-features tradition of Gerace et
al.[29]. Every reported quantity is a mean±\pmone standard
deviation overNseedsN_{\mathrm{seeds}}independent dataset re-draws, each per-seed
value being itself an average overNevalN_{\mathrm{eval}}retrieval trials.

## The two indicesPPandKK, and why both are needed

The model stores a genuinely many-to-one map, and this forces two independent
counts that the notation keeps deliberately separate.
- •

PPdefines theload: the number of pattern indicesμ=1,…,P\mu=1,\dots,Pactually stored, i.e. the number of cues the network holds, exactly as in
the Rademacher theory of Sections2–5. Each indexμ\muowns its own latent codezμz^{\mu}and hence its own set ofLLlayer
patterns{ξμ,a}a=1L\{\xi^{\mu,a}\}_{a=1}^{L}.
- •

KKis the number of distincttarget prototypes(equivalently,
target regions) available in the last layer. It is a property of the rule,
not of the sample:K=2nbitsK=2^{n_{\mathrm{bits}}}is fixed before any latent is drawn,
wherenbitsn_{\mathrm{bits}}is the number of latent coordinates read by the target
rule below.

The map is surjective precisely becauseP≫KP\gg K: many of thePPstored cues
share one of theKKtargets. The biological reading is immediate:PPcounts
receptors,KKcounts epitopes, andP/KP/Kis the mean number of receptors
converging on one epitope, the surjective compression of
Figure4(c). CollapsingPPandKKinto a single index would
forbid the very many-to-one structure the model exists to study. A third count,nseen≤Kn_{\mathrm{seen}}\leq K, enters the generalisation protocol: the number of target
regions actually populated during training.

## Latent code and cue layers

FixLLlayers,NNneurons per layer, a latent (manifold) dimensionDDwith
aspect ratioαD=D/N∈(0,1]\alpha_{D}=D/N\in(0,1](alwaysD≤ND\leq N), andK=2nbitsK=2^{n_{\mathrm{bits}}}target regions. Each indexμ=1,…,P\mu=1,\dots,Powns a latent codezμ∼𝒩​(0,ID)i.i.d. across​μ,zμ∈ℝD.z^{\mu}\;\sim\;\mathcal{N}(0,I_{D})\quad\text{i.i.d.\ across }\mu,\qquad z^{\mu}\in\mathbb{R}^{D}.(141)

Each cue layera∈{1,…,L−1}a\in\{1,\dots,L-1\}carries a fixed random feature matrixFa∈ℝN×DF^{a}\in\mathbb{R}^{N\times D}with i.i.d.𝒩​(0,1)\mathcal{N}(0,1)entries, drawn
once per dataset and shared by allPPindices, and produces the binary patternξμ,a=sign​(Fa​zμ/D)∈{−1,+1}N,a=1,…,L−1.\xi^{\mu,a}\;=\;\mathrm{sign}\!\bigl(F^{a}z^{\mu}/\sqrt{D}\bigr)\;\in\;\{-1,+1\}^{N},\qquad a=1,\dots,L-1.(142)

The1/D1/\sqrt{D}normalisation makes each pre-activation coordinate(Fa​zμ)i/D(F^{a}z^{\mu})_{i}/\sqrt{D}unit-variance, matching the standard HMM formξ=φ​(F​z/D)\xi=\varphi(Fz/\sqrt{D})withφ=sign\varphi=\mathrm{sign}. Two cue layersa≠ba\neq bat the
same indexμ\muare correlated only through the shared latentzμz^{\mu}(their feature matricesFa,FbF^{a},F^{b}are independent); this shared cause is
exactly the inter-layer correlation that the idealised theory of
Section2forbids and that makes hetero-association possible.
Distinct indices are independent given the{Fa}\{F^{a}\}.

## The surjective target and the region map

The last layera=La=Lcarries the target. Two variants are used.

Surjective target(default; the many-to-one rule the model is meant to
store). Partition latent space intoKKregions by the sign pattern of the firstnbitsn_{\mathrm{bits}}latent coordinates,k​(z)=∑j=0nbits−12j​1​[zj>0]∈{0,1,…,K−1},K=2nbits,k(z)\;=\;\sum_{j=0}^{n_{\mathrm{bits}}-1}2^{j}\,\mathbf{1}[z_{j}>0]\;\in\;\{0,1,\dots,K-1\},\qquad K=2^{n_{\mathrm{bits}}},(143)

so thatk​(z)k(z)reads the firstnbitsn_{\mathrm{bits}}signs ofzzas a binary
integer (𝟏​[⋅]\mathbf{1}[\cdot]is the indicator). FixKKprototypesρ0,…,ρK−1\rho_{0},\dots,\rho_{K-1}, each an independent Rademacher vectorρk∈{−1,+1}N\rho_{k}\in\{-1,+1\}^{N}drawn once, and set the target of indexμ\mutoξμ,L=ρk​(zμ).\xi^{\mu,L}\;=\;\rho_{k(z^{\mu})}.(144)

Every index whose latent falls in the same region (i.e. shares the firstnbitsn_{\mathrm{bits}}signs) is mapped to the same stored target: on averageP/KP/Kcues per prototype, with a per-region multiplicity that isBinomial​(P,1/K)\mathrm{Binomial}(P,1/K). The rule discards the continuous magnitudes and every
coordinatej≥nbitsj\geq n_{\mathrm{bits}}, so within a region the cueξμ,a\xi^{\mu,a}still varies continuously withzμz^{\mu}while the target is pinned toρk\rho_{k}, the geometric content of “many distinct cues, one target”.

Symmetric target(control). The last layer is instead given its own
independent feature matrix and no repetition,ξμ,L=sign​(FL​zμ/D)\xi^{\mu,L}=\mathrm{sign}(F^{L}z^{\mu}/\sqrt{D}), so each index owns a distinct target.
This is the ensemble used whenever we compare directly against the i.i.d. closed-form theory of Sections5–6, whose
assumption ofPPessentially-orthogonal targets a fixedK≪PK\ll Pwould badly
violate.

## The manifold signature: pairwise overlap and the arcsine law

The order parameter that certifies the manifold is thepairwise pattern
overlap, defined for two indicesμ≠ν\mu\neq\nuin a cue layeraaexactly as the
Mattis overlap of two stored patterns,mμ​ν:=1N​∑i=1Nξiμ,a​ξiν,a∈[−1,1],m_{\mu\nu}\;:=\;\frac{1}{N}\sum_{i=1}^{N}\xi_{i}^{\mu,a}\,\xi_{i}^{\nu,a}\;\in\;[-1,1],(145)

i.e. the normalised inner product (cosine on the hypercube) between the two
binary codes:mμ​ν=1m_{\mu\nu}=1for identical codes,0for orthogonal ones. This
is the quantity plotted in Figure3(a), and the referencemμ​νm_{\mu\nu}used throughout Section7; we now derive its law.

Writeξiμ,a=sign​(uiμ)\xi_{i}^{\mu,a}=\mathrm{sign}(u_{i}^{\mu})withuiμ=(Fa​zμ)i/D=⟨fi,zμ⟩/Du_{i}^{\mu}=(F^{a}z^{\mu})_{i}/\sqrt{D}=\langle f_{i},z^{\mu}\rangle/\sqrt{D}, wherefi∈ℝDf_{i}\in\mathbb{R}^{D}is theii-th row ofFaF^{a}, i.i.d.𝒩​(0,ID)\mathcal{N}(0,I_{D}).
For fixedzμ,zνz^{\mu},z^{\nu}and over the randomness offif_{i}, the pair(uiμ,uiν)(u_{i}^{\mu},u_{i}^{\nu})is jointly centred Gaussian withVar(uiμ)=‖zμ‖2D,Cov(uiμ,uiν)=⟨zμ,zν⟩D,corr(uiμ,uiν)=⟨zμ,zν⟩‖zμ‖​‖zν‖=:ρz.\mathrm{Var}(u_{i}^{\mu})=\frac{\|z^{\mu}\|^{2}}{D},\qquad\mathrm{Cov}(u_{i}^{\mu},u_{i}^{\nu})=\frac{\langle z^{\mu},z^{\nu}\rangle}{D},\qquad\mathrm{corr}(u_{i}^{\mu},u_{i}^{\nu})=\frac{\langle z^{\mu},z^{\nu}\rangle}{\|z^{\mu}\|\,\|z^{\nu}\|}=:\rho_{z}.(146)

By Grothendieck’s identity for the sign of correlated Gaussians (equivalently the
orthant / arcsine formula),𝔼​[sign​(X)​sign​(Y)]=2π​arcsin⁡ρ\mathbb{E}[\mathrm{sign}(X)\mathrm{sign}(Y)]=\tfrac{2}{\pi}\arcsin\rhofor
standard jointly Gaussian(X,Y)(X,Y)of correlationρ\rho; hence𝔼​[ξiμ,a​ξiν,a∣zμ,zν]=2π​arcsin⁡ρz\mathbb{E}[\xi_{i}^{\mu,a}\xi_{i}^{\nu,a}\mid z^{\mu},z^{\nu}]=\tfrac{2}{\pi}\arcsin\rho_{z}for
everyii. Averaging over theNNi.i.d. rows and using concentration,𝔼​[mμ​ν]=2π​arcsin⁡(ρz),ρz=⟨zμ,zν⟩‖zμ‖​‖zν‖,\mathbb{E}[m_{\mu\nu}]\;=\;\frac{2}{\pi}\arcsin(\rho_{z}),\qquad\rho_{z}=\frac{\langle z^{\mu},z^{\nu}\rangle}{\|z^{\mu}\|\,\|z^{\nu}\|},(147)

an exact, parameter-free curve: the “signature” verified in
Figure3(a). Fluctuations ofmμ​νm_{\mu\nu}about
(147) at fixedρz\rho_{z}are𝒪​(N−1/2)\mathcal{O}(N^{-1/2}).

The cost of curvature.For independent latentsρz\rho_{z}is itself random:⟨zμ,zν⟩∼𝒩​(0,D)\langle z^{\mu},z^{\nu}\rangle\sim\mathcal{N}(0,D)and‖z‖2≈D\|z\|^{2}\approx D, soρz\rho_{z}has zero mean and standard deviationD−1/2D^{-1/2}. Linearising
(147) for smallρz\rho_{z},mμ​ν≈2π​ρzm_{\mu\nu}\approx\tfrac{2}{\pi}\rho_{z},𝔼​[mμ​ν]≈0,Var​(mμ​ν)≈(2π)2​1D,\mathbb{E}[m_{\mu\nu}]\approx 0,\qquad\mathrm{Var}(m_{\mu\nu})\;\approx\;\Bigl(\tfrac{2}{\pi}\Bigr)^{2}\frac{1}{D},(148)

to be compared with the i.i.d. Rademacher valueVar​(mμ​ν)=1/N\mathrm{Var}(m_{\mu\nu})=1/N. The
manifold patterns are therefore more correlated than independent ones
whenever(2π)2​1D>1N⟺D<(2π)2​N≈0.405​N,\Bigl(\tfrac{2}{\pi}\Bigr)^{2}\frac{1}{D}>\frac{1}{N}\quad\Longleftrightarrow\quad D<\Bigl(\tfrac{2}{\pi}\Bigr)^{2}N\approx 0.405\,N,(149)

i.e. once the manifold is small enough. This excess correlation is precisely the
extra noise the clean theory does not carry: it adds to thee−N​ρLe^{-N\rho_{L}}floor
and lowers capacity asαD=D/N\alpha_{D}=D/Nfalls, the mechanism behind the capacity
drop in Figure4(a). AtαD=1\alpha_{D}=1the excess(2/π)2−1<0(2/\pi)^{2}-1<0vanishes with room to spare: the sign-map ensemble is then
less correlated than Rademacher and sits at the near-i.i.d. edge used as a
baseline.

## The collision subtlety

The mapz↦sign​(Fa​z)z\mapsto\mathrm{sign}(F^{a}z)is piecewise constant: it depends onzzonly
through which side of each hyperplane{fi⋅z=0}\{f_{i}\cdot z=0\}the latent falls. TheNNcentral hyperplanes cutℝD\mathbb{R}^{D}intoC​(N,D)=2​∑k=0D−1(N−1k)=𝒪​(ND−1)C(N,D)\;=\;2\sum_{k=0}^{D-1}\binom{N-1}{k}\;=\;\mathcal{O}\!\bigl(N^{D-1}\bigr)(150)

regions (Cover’s function-counting theorem for a central hyperplane
arrangement), so at mostC​(N,D)C(N,D)distinct sign codes exist in layeraa.
WhenDDis small this is far fewer than thePPlatents drawn, and many latents
collide onto identical codes. Two consequences must be handled honestly.
(i) A pattern stored inccidentical copies is reinforced as if it carried weightcc, so a naive one-step-stability score is spuriously high at smallDD,
even as the number of distinct memories, the real capacity,
collapses. We therefore always report the distinct-pattern fraction alongside
stability (Figure3(c)) and read the honest “capacity falls
withDD” statement from the matched-load transition of
Figure4(a), never from raw stability. (ii) Collisions
inflate the measured mean overlap above the arcsine prediction at smallDD(identical codes contributemμ​ν=1m_{\mu\nu}=1), the upward bias visible in
Figure5(c).

## Held-out regions and the novel-region control

The generalisation experiment tests whether the network routes a
never-stored cue to the correct target, and its whole logic rests on a
construction we now spell out. Of theKKregions, a subset of sizenseen<Kn_{\mathrm{seen}}<Kis declaredallowed(“seen”); the remainingK−nseenK-n_{\mathrm{seen}}are held out. During training thePPlatents are
drawn by rejection sampling: anyzμz^{\mu}withk​(zμ)k(z^{\mu})held-out is discarded
and redrawn, so every stored cue maps to a seen region and the held-out
prototypes{ρk:k​held out}\{\rho_{k}:k\text{ held out}\}, though they exist as vectors, are
backed by no stored cue. Four rates are measured on the same trained
network:
- •

Memorisation: fraction of thePPstored cues that recall
their own target under the clamped-cue dynamics.
- •

Generalisation: fraction of fresh latents drawn from
seen regions whose cue recalls that region’s (correctly stored) prototype.
- •

Novel-region control: the same for fresh latents drawn from
held-out regions, whose prototype was never stored.
- •

Chance:1/nseen1/n_{\mathrm{seen}}, the rate of guessing the target
uniformly among the seen prototypes (=1/6≈0.167=1/6\approx 0.167forK=8K=8, two held out).

The control is what makes the test conclusive. A held-out prototype is not stored,
so no property of the trained network can point a fresh cue at it except by
artefact (a coincidental collision in the encoder, a leak in the split, a bug). If
novel-region recall exceeded chance the “generalisation” signal would be
suspect; that it stays pinned at chance (Figure5(a,b))
while seen-region generalisation sits significantly above it certifies that the
latter is genuine exploitation of manifold geometry, not an encoding artefact.Why it works at all: a fresh cue from a seen region shares the firstnbitsn_{\mathrm{bits}}latent signs, hence a large block of sign structure, with the
stored cues of that region; those stored cues carve an energy basin around the
shared prototypeρk\rho_{k}, and a fresh cue landing inside it flows toρk\rho_{k}.
Denser sampling (larger coverageP/nseenP/n_{\mathrm{seen}}) tiles more of each
region’s cue-manifold with stored cues, so a larger fraction of fresh cues fall
into the right basin, which is why generalisation climbs with coverage toward
memorisation (the “manifold-as-attractor” limit) in
Figure5(b), while never certifying the network as a
classifier of truly novel regions.

## Retrieval protocols and the reduced load

Three protocols share one dynamics engine.Auto-associative capacity(Figure4(a)) uses one-step stability atr=1r=1: all layers
initialised at a stored pattern, unclamped dynamics.Hetero-associative
recall(Figure4(b)) clamps theL−1L-1cue layers at their
stored values and cleans the target layer from a cue-driven seed.Basins(Figure2(a)) corrupt all layers to a common initial overlaprr.
It is convenient to summarise “how close to capacity” by the reduced load of
Eq. (34),γ​(P,N,L)=(P−1)​KL​e−N​ρLμ1​(L)2,μ1​(L)=e−(L−1)​sinh⁡(L−1),\gamma(P,N,L)\;=\;\frac{(P-1)\,K_{L}\,e^{-N\rho_{L}}}{\mu_{1}(L)^{2}},\qquad\mu_{1}(L)=e^{-(L-1)}\sinh(L-1),(151)

withKL,ρLK_{L},\rho_{L}the noise prefactor and rate of Section4andμ1​(L)\mu_{1}(L)the clean one-step signal (20), for which the asymptotic
one-step overlap collapses onto the universal curvem1(1)=erf​(1/2​γ)m_{1}^{(1)}=\mathrm{erf}(1/\sqrt{2\gamma}):γ≪1\gamma\ll 1is deep retrieval,γ≈1\gamma\approx 1the transition,γ≫1\gamma\gg 1failure. We scan the number of
stored patternsPPon a logarithmic grid and read offγ\gammaas the
corresponding intensive coordinate. The two baselines are the classical i.i.d. Rademacher ensemble (iid_full, the exact closed-form regime of
Sections5–6) and theαD=1\alpha_{D}=1edge of the
samesign​(F​z)\mathrm{sign}(Fz)pipeline, so that a curve-to-curve comparison isolates the effect
of manifold dimension alone.

## Appendix GVDJdb: cleaning and encoding

This appendix documents how the raw VDJdb release[51,13]becomes the{−1,+1}N\{-1,+1\}^{N}patterns of Section8. Two principles
govern the pipeline: the stored map must be a genuine function, and the encoding
must be a fixed, deterministic map that introduces no learned representation. Both
choices are standard in the sequence-immunology and locality-sensitive-hashing
literatures, cited below.

## Cleaning into a single-valued map

We start from the fullvdjdbexport (137,484137{,}484records) and apply a
lean biological clean followed by a function filter. The receptor key isX=(Vα,Jα,CDR3α,Vβ,Jβ,CDR3β)X=(V_{\alpha},J_{\alpha},\mathrm{CDR3}_{\alpha},V_{\beta},J_{\beta},\mathrm{CDR3}_{\beta})and the target isY=epitopeY=\text{epitope}. The steps and surviving counts are in
Table9. The decisive step is the last: deduplicating triples is
not enough to makeX↦YX\mapsto Ysingle-valued, because a receptor may appear
against several epitopes; we therefore keep only receptors mapped to exactly one
epitope, dropping the5252ambiguous ones. The result is1,0521{,}052clean triples
over220220epitopes, strongly surjective (up to146146receptors per epitope,120120singletons): the “convergent recognition” the network is meant to store. A
single-valued map is the mathematical prerequisite of a well-posed
generalisation/surjectivity test.stagerecordsraw rows137,484137{,}484Homo sapiens131,574131{,}574curation score≥1\geq 110,17810{,}178drop 10x-Genomics demo9,9089{,}908pairedcomplex.id3,0323{,}032valid amino-acid sequence + length3,0313{,}031pairedα​β\alpha\betasynapses1,2271{,}227dedup(X,epitope)(X,\text{epitope})1,2271{,}227function filter (drop5252ambiguousXX)𝟏,𝟎𝟓𝟐\mathbf{1{,}052}Table 9:Cleaning funnel imposing a single-valued receptor→\toepitope map.

## Encoding, overview

Each amino-acid sequence becomes a patternξμ,a∈{−1,+1}N\xi^{\mu,a}\in\{-1,+1\}^{N}(hereN=128N=128) in two deterministic, learning-free stages: (A) a positional
Atchley-factor feature map turning the sequence into a fixed-length real vector,
and (B) a locality-sensitive (SimHash) binariser turning that vector into a
balanced, near-orthogonal sign code whose Hamming overlap tracks the cosine angle
of the features. One encoder is fitted per layer (α\alpha,β\beta,
epitope), because the three modalities differ in length and composition, and it
is fitted on the training split only: test sequences are transformed with
the frozen maps, so no held-out sequence informs the encoder.

## Stage A: positional Atchley-factor features

Atchley factors[12]summarise each amino acid by five numbers(z1,…,z5)(z_{1},\dots,z_{5}), obtained from a factor analysis of several hundred
physicochemical amino-acid indices and standardised to zero mean and unit
variance across the2020residues; the five axes are, in order, polarity /
hydrophobicity (z1z_{1}), secondary-structure propensity (z2z_{2}), molecular size /
volume (z3z_{3}), codon composition / refractivity (z4z_{4}) and electrostatic charge
(z5z_{5}). Writinga​(s)∈ℝ5a(s)\in\mathbb{R}^{5}for the factor vector of residuess, a
sequencew=(s1,…,sℓ)w=(s_{1},\dots,s_{\ell})of lengthℓ\ellis mapped to a fixedLmax×5L_{\max}\times 5array by centre padding: the N-terminal half ofwwis
written from the left, the C-terminal half from the right, and theLmax−ℓL_{\max}-\ellempty middle positions are set to zero (the mean of the
standardised factors). This keeps the conserved CDR3 anchors (the N-terminal
cysteine, the C-terminal phenylalanine–glycine) at fixed indices and lets the
padding fall in the hypervariable middle, so positional information is preserved
–a charge at position33is a different feature from a charge at position1010.
Flattening gives the real feature vectorxμ,a=(a​(s1),…)∈ℝ5​Lmax,Lmax=min⁡(⌈q99⌉,ℓmax),x^{\mu,a}\;=\;\bigl(a(s_{1}),\dots\bigr)\in\mathbb{R}^{5L_{\max}},\qquad L_{\max}=\min\!\bigl(\lceil q_{99}\rceil,\ \ell_{\max}\bigr),(152)

withLmaxL_{\max}the per-layer alignment length (the9999th percentile of the
training lengths, capped at the observed maximumℓmax\ell_{\max}). This replaces the
earlier order-destroying bag-of-kk-mers summary, retained only as the ablation
baseline below.

## Stage B: the locality-sensitive (SimHash) binariser

The feature vector is binarised by standardise→\toPCA-whiten→\toGaussian
random projection→\tosign[20]. LetΠ:ℝ5​Lmax→ℝd′\Pi:\mathbb{R}^{5L_{\max}}\to\mathbb{R}^{d^{\prime}}be the affine map that standardises each coordinate and
projects onto the topd′=min⁡(50,rank)d^{\prime}=\min(50,\text{rank})whitened PCA directions (fitted on
the training features, soΠ\Pihas unit-covariance output), and letW∈ℝN×d′W\in\mathbb{R}^{N\times d^{\prime}}be a fixed matrix with i.i.d.𝒩​(0,1)\mathcal{N}(0,1)entries. Thenξμ,a=sign​(W​Π​(xμ,a))∈{−1,+1}N,Wk​i∼𝒩​(0,1),\xi^{\mu,a}\;=\;\mathrm{sign}\!\bigl(W\,\Pi(x^{\mu,a})\bigr)\;\in\;\{-1,+1\}^{N},\qquad W_{ki}\sim\mathcal{N}(0,1),(153)

with ties (=0=0) mapped to+1+1. BecauseWWis Gaussian andΠ​(x)\Pi(x)has unit
covariance, each bit is an unbiased±1\pm 1sign, and distinct bits (distinct rows
ofWW) are near-independent: the codes are close to the Rademacher ideal the
theory assumes.

## The SimHash law connects the encoding to the manifold signature

For two feature vectors with whitened imagesvμ=Π​(xμ,a)v^{\mu}=\Pi(x^{\mu,a}),vν=Π​(xν,a)v^{\nu}=\Pi(x^{\nu,a})and angleθ=arccos⁡c\theta=\arccos c,c=⟨vμ,vν⟩/(‖vμ‖​‖vν‖)c=\langle v^{\mu},v^{\nu}\rangle/(\|v^{\mu}\|\,\|v^{\nu}\|), a single Gaussian
hyperplane separates them with probabilityθ/π\theta/\pi, so each bit agrees with
probability1−θ/π1-\theta/\piand𝔼​[mμ​ν]=1−2π​arccos⁡(c)=2π​arcsin⁡(c),\mathbb{E}[m_{\mu\nu}]\;=\;1-\frac{2}{\pi}\arccos(c)\;=\;\frac{2}{\pi}\arcsin(c),(154)

withmμ​ν=1N​∑iξiμ,a​ξiν,am_{\mu\nu}=\frac{1}{N}\sum_{i}\xi_{i}^{\mu,a}\xi_{i}^{\nu,a}the pattern overlap of
Eq. (145). This is the same Grothendieck identity as the arcsine
law (147) of the Hidden Manifold Model, now with the biophysical
cosineccin place of the latent cosineρz\rho_{z}: biochemically similar receptors
receive proximate codes, and Figure6(d) shows the measured
overlap tracking (154). Table10confirms the
Rademacher quality: per-bit balance≈0.03\approx 0.03on the receptor layers and mean
absolute pattern overlap≈0.10\approx 0.10, close to the i.i.d. value1/N≈0.0881/\sqrt{N}\approx 0.088atN=128N=128. The epitope layer, having only220220distinct
codes, is measurably less balanced (0.120.12), as expected for a small surjective
target. Alternative encodings (kk-mer, random) are retained only as ablation
baselines (Figure11): the biophysical Atchley features andkk-mers carry comparable signal, while a text-blind random projection generalises
at chance, confirming that the retrieval signal is in the features and not in the
hash.layerNNdistinct codesper-bit balanceoverlap|mμ​ν||m_{\mu\nu}|α\alpha-CDR3128128104210420.0280.0280.1040.104β\beta-CDR3128128104810480.0280.0280.1030.103epitope1281282202200.1230.1230.1200.120Table 10:Near-Rademacher quality of the Atchley++SimHash encoding (means over
seeds). “Per-bit balance” is the mean absolute per-bit magnetisation (ideal0); the receptor layers are close to Rademacher.Figure 11:Encoding ablation.(a)Generalisation to unseen receptors under the three encodings:
Atchley factors andkk-mers carry comparable biological signal (well above
chance), while a text-blind random projection collapses to chance: the signal
is in the biophysical features, not the hashing.(b)Effect of the layer sizeNN(Atchley): longer codes lower the
pairwise overlap (right axis) and slowly raise generalisation (left axis).

## Layer assignment, tasks and reproducibility

The three layers area=1a=1(α\alpha-CDR3),a=2a=2(β\beta-CDR3),a=3a=3(epitope),
soL=3L=3. Hetero-associative tasks clamp the cue layers and recall the target;
generalisation holds out a fraction of the receptors of each epitope and tests
recall on them, against both a chance level1/nepitopes1/n_{\mathrm{epitopes}}and a
label-permutation null (epitope labels shuffled before encoding), which is the
control of Figure7(c). All quantities are means±\pmone
standard deviation over independent projection seeds and train/test splits; the
dynamics engine is identical to the HMM battery, so the two are directly
comparable.

## A caveat on the held-out split

The receptors held out for generalisation are sampled uniformly at random
within each epitope cluster, after deduplication on the exact(V,J,CDR3α,V,J,CDR3β)(V,J,\mathrm{CDR3}_{\alpha},V,J,\mathrm{CDR3}_{\beta})key; the split does not
additionally enforce a minimum sequence distance between held-out and training
receptors of the same epitope. TCR repertoires are known to converge on
near-identical “public” sequences for a shared epitope[30],
so some held-out receptors may sit a few substitutions from a training one,
which would inflate the measured generalisation rate relative to a split
enforcing sequence-level separation. The label-permutation null controls for
structure in the encoding, not for this specific leakage channel; a
similarity-aware split is the natural follow-up and is not expected to remove
the signal (the two chains still recall the epitope from first principles,
Figure7(a)) but could lower its measured size.

## Appendix HThe CLINC150 protocol

This appendix gives the construction behind Section9: the
cleaning, the encoder, the retrieval protocols and the ablations. It is the
natural-language counterpart ofG, and deliberately
shares with it every step that can be shared, so that the two batteries differ
only where the data force them to. Every reported number is a mean±\pmone
standard deviation overNseeds=6N_{\mathrm{seeds}}=6dataset re-draws (projection seed
plus train/test split), each itself an average over evaluation trials, exactly as
inI.

## Data and the function filter

CLINC150[42]is a benchmark of short user utterances labelled by
one of150150intents (“set an alarm”, “what is my balance”), balanced at
about150150utterances per intent, and shipped with a set of out-of-scope (OOS)
utterances belonging to none of them. We pool the in-domain splits, normalise
and deduplicate(utterance,intent)(\text{utterance},\text{intent})pairs, and apply the same
function filter as for VDJdb (keep only utterances mapped to a single intent,
as Remark1requires) which here removes just44ambiguous utterances, leaving22,49122{,}491clean records over150150intents.
The mean compression isP/K≈150P/K\approx 150cues per target, against≈5\approx 5for
VDJdb: the same surjective structure, sampled thirty times more densely. The OOS
utterances are held aside as a novelty control.

## Encoding

The two layers area=1a=1(utterance) anda=2a=2(intent). Utterances become{−1,+1}N\{-1,+1\}^{N}patterns through a fixed, deterministic pipeline with no learned
representation: a TF–IDF vector over word(1,2)(1,2)-grams concatenated with
character(3,5)(3,5)-grams (lexical and short-phrase content on one side,
morphology and sub-word cues on the other, the linguistic analogue of the
positional Atchley map) reduced by a PCA whitening to at most5050components
fitted on the training split, then passed through the same SimHash sign
map[20]used inG. The intent layer
stores one code per intent name, so that every phrasing of an intent
shares a single target and semantically close intents receive close codes. As in
the manifold and receptor cases the pattern overlap obeys the arcsine law𝔼​[mμ​ν]=1−2π​arccos⁡c\mathbb{E}[m_{\mu\nu}]=1-\tfrac{2}{\pi}\arccos cin the feature cosinecc(Figure8(b)), with per-bit imbalance0.029±0.0020.029\pm 0.002and mean
absolute overlap0.097±0.0020.097\pm 0.002on the utterance layer atN=128N=128, against the
i.i.d. value1/N=0.0881/\sqrt{N}=0.088. ChoosingL=2L=2makes the closed forms of
Sections5–6directly usable, withρ2=1.3470\rho_{2}=1.3470,x∗=1.9150x^{\ast}=1.9150,m∗=0.9575m^{\ast}=0.9575, annealedrc=0.3195r_{c}=0.3195and
typicalrc=0.5714r_{c}=0.5714.

## Retrieval protocols

Four protocols are run, all with the engine of Algorithm1unchanged from the other two batteries.Capacity: a logarithmic gridP∈[30,6000]P\in[30,6000], one-step overlap of a stored pattern against (32),
real and i.i.d. ensembles at matchedPP.Basins: atP=2000P=2000, a sweep of
the cue overlaprron a1414-point grid, against (40).Tasks: atP=3000P=3000, the forward direction utterance→\tointent and the
reverse intent→\toutterance, plus the cue-content scan in which only the leading
fractionf∈{0.15,…,1}f\in\{0.15,\dots,1\}of the utterance’s tokens is revealed and
re-encoded with the frozen transform.Generalisation: a quarter of the
utterances of each intent held out, then memorisation (stored cues),
generalisation (held-out cues of seen intents), the OOS control and chance1/1501/150, together with top-kkretrieval and a label-permutation null over2020permutations.

## Results, and the comparison with VDJdb

Table11collects the outcome beside the receptor battery. The
memory side coincides in the two datasets and with the i.i.d. theory; the
classifier side differs by an order of magnitude. Top-kkretrieval of the
correct intent for a fresh utterance rises from0.527±0.0090.527\pm 0.009atk=1k=1to0.6000.600,0.6290.629and0.6490.649atk=3,5,10k=3,5,10: the correct intent is usually
either first or not in the shortlist at all, which is the signature of a basin
that either contains the fresh cue or does not.

Two things must be kept apart here. The OOS entry of Table11is anull control: an out-of-scope utterance, whose intent is by construction
absent from the codebook, is matched to its (unstored) target at rate0.0140.014,
i.e. at chance, which is what certifies that the generalisation signal is not
an artefact of the encoding. It is not a rejection capability, and the
distinction matters because the network does not have one: using the retrieval
confidence as an open-set score separates in-domain from out-of-scope utterances
with an AUROC of0.5130.513, that is, not at all. An exponential associative memory
recognises what it has stored; it has no built-in notion of “none of the
above”, and equipping it with one is beyond the present scope.QuantityCLINC150 (language)VDJdb (receptors)memorisation0.720.720.9970.997generalisation (unseen cue)0.580.580.110.11novelty / null control0.0140.0140.0480.048chance0.00670.00670.0050.005top-11retrieval0.530.530.090.09top-1010retrieval0.650.65–(cue)→target(\text{cue})\to\text{target}recall0.780.780.99940.9994mean cues per targetP/KP/K≈150\approx 150≈5\approx 5Table 11:The two real-data batteries side by side, atL=2L=2andL=3L=3respectively. The memory side (recall, capacity, basins) matches the i.i.d. theory in both. The classifier side differs by an order of magnitude: language
generalises far better than receptor sequences.

## Encoding ablation: where the generalisation lives

The storage rule, the dynamics and the closed-form basins are identical across
the two datasets, so the gap in generalisation cannot come from the memory.
Three scans, all at fixed load and fixed protocol, locate it in the encoder
(Table12). Replacing TF–IDF by a text-blindrandommap, a deterministic hash of the utterance to a fixed Gaussian
vector, so that similar utterances receive unrelated codes, leaves
memorisation at0.3490.349and collapses generalisation onto chance,0.0080.008against1/150=0.00671/150=0.0067: the network stores as well as ever and has nothing to
interpolate between. A plain bag-of-words map, which discards ordering and
sub-word structure but keeps lexical overlap, is if anything slightly
better than TF–IDF (0.6520.652against0.5840.584), confirming that what
matters is co-location of same-target cues rather than the sophistication of the
features. Finally, widening the code (N=32→256N=32\to 256) or the whitened
representation (d′=10→100d^{\prime}=10\to 100) buys generalisation monotonically, in step with
the fall of the mean pattern overlap towards its i.i.d. floor1/N1/\sqrt{N}: less
crowded pattern space, wider basins, more of the manifold covered by each stored
cue.scansettingmemorisationgeneralisation⟨|mμ​ν|⟩\langle|m_{\mu\nu}|\ranglefeaturesTF–IDF0.700.700.580.580.0970.097bag of words0.750.750.650.650.1040.104random (blind)0.350.350.0080.0080.1010.101layer sizeNN32320.440.440.350.350.1580.15864640.620.620.500.500.1230.1231281280.700.700.580.580.0970.0972562560.760.760.630.630.0850.085PCA capd′d^{\prime}10100.410.410.380.380.1900.19025250.540.540.440.440.1220.12250500.700.700.580.580.0970.0971001000.810.810.690.690.0850.085Table 12:Encoding ablation on CLINC150 (L=2L=2, chance=0.0067=0.0067,66seeds;
standard deviations are below0.0350.035throughout). The reference row
(TF–IDF,N=128N=128,d′=50d^{\prime}=50) differs marginally from Table11because the ablation restricts to intents with at least five utterances. The
text-blind encoder preserves memorisation and destroys generalisation, which is
the sharpest form of the claim that generalisation is a property of the
representation and not of the storage rule.

## Appendix IReproducibility: figure parameters

Every simulated point in the figures is a mean±\pmone standard deviation overNseedsN_{\mathrm{seeds}}independent re-draws of the disorder (patterns, feature
maps, train/test splits); each per-seed value is itself an average overNevalN_{\mathrm{eval}}independent retrieval trials. The dynamics is the
zero-temperature parallel Glauber update of Algorithm1, run for a
small fixed number of sweeps (nsteps=5n_{\mathrm{steps}}=5). The theory panels
(Figures1(a,b),2(a,b),9,10) are analytic: the saddlex∗x^{\ast}and the tilted
saddlems​(r)m_{s}(r)are solved numerically from the closed forms ofBandC, with no simulation.
Tables13and14list the control parameters used for each panel.Figure (panel)ProtocolParameters1(a)one-step stability,r=1r=1(i.i.d.)N∈{8,9,10,11,12}N\in\{8,9,10,11,12\},L=2L=2,PPon a log grid to∼2×107\sim\!2\!\times\!10^{7}(22 pts),Nseeds=6N_{\mathrm{seeds}}=6,Neval=200N_{\mathrm{eval}}=2002(a)corrupted-cue recoveryN=10N=10,L=2L=2,αD=0.5\alpha_{D}=0.5(d=5d=5),P=3093P=3093(γ=0.1\gamma=0.1),r∈[0,1]r\in[0,1](11 pts)3(a,b)manifold geometryN=10N=10,L=2L=2,P=800P=800,2×1042\!\times\!10^{4}pattern pairs,αD∈[0.1,1]\alpha_{D}\in[0.1,1]3(c)dimension scanN=10N=10,L=2L=2,P=3000P=3000,nbits=2n_{\mathrm{bits}}=2,αD∈[0.1,1]\alpha_{D}\in[0.1,1]4(a)capacity scanN=10N=10,L=2L=2,αD∈{0.3,0.6,1.0}\alpha_{D}\in\{0.3,0.6,1.0\}+ i.i.d.,P∈[4,5×104]P\in[4,5\!\times\!10^{4}]4(b)width scanN=10N=10,L∈{2,3,4}L\in\{2,3,4\},αD=0.5\alpha_{D}=0.5,P∈[4,2×104]P\in[4,2\!\times\!10^{4}]4(c)surjective compressionN=12N=12,L=2L=2,P=4000P=4000,K=21..6K=2^{1..6},r∈{0.6,…,1.0}r\in\{0.6,\dots,1.0\}5(a,b)generalisationN=12N=12,L=2L=2,d=6d=6,K=8K=8(66seen,22held out),P∈[16,2×104]P\in[16,2\!\times\!10^{4}],ntest=300n_{\mathrm{test}}=3005(c)theory vs empiricalN=10N=10,L=2L=2,γ=1\gamma=1(P=30920P=30920),r=0.68r=0.68,αD∈[0.1,1]\alpha_{D}\in[0.1,1]Table 13:Hidden Manifold Model figures. Rates used as theory reference:ρ2=1.347\rho_{2}=1.347,ρ3=2.078\rho_{3}=2.078,ρ4=2.773\rho_{4}=2.773;L=2L=2thresholdsrcann=0.3195r_{c}^{\mathrm{ann}}=0.3195,rctyp=0.5714r_{c}^{\mathrm{typ}}=0.5714. All runs useNseeds=6N_{\mathrm{seeds}}=6,Neval=200N_{\mathrm{eval}}=200,nsteps=5n_{\mathrm{steps}}=5.Figure (panel)ContentParameters6(a)cleaning funnelvdjdb-2025-09-25:137,484→1,052137{,}484\!\to\!1{,}052triples,220220epitopes6(b)epitope cluster sizesmax146146receptors/epitope,120120singletons6(c,d)encoding quality / SimHashAtchley + PCA(5050) + SimHash,N=128N=128;40004000sampled pairs (d)7(a)biological tasksN=128N=128,L=3L=3,P=800P=800,Nseeds=6N_{\mathrm{seeds}}=67(b)basinsN=128N=128,L=3L=3,P=600P=600,r∈[0,0.82]r\in[0,0.82]7(c)generalisation vs nullN=128N=128,P=800P=800,r=0.68r=0.68;66true vs2020label-permuted splits7(d)per-epitope / top-kkN=128N=128, test fraction0.250.25,min\mincluster size≥2\geq 211encoding ablationfeature∈{\in\{Atchley,kk-mer, random}\};N∈{32,64,128,256}N\in\{32,64,128,256\}Table 14:VDJdb figures. Layers areα\alpha-CDR3,β\beta-CDR3 and epitope
(L=3L=3); the encoder is Atchley positional features reduced by PCA and binarised
by a SimHash (G). All runs useNseeds=6N_{\mathrm{seeds}}=6,Neval=200N_{\mathrm{eval}}=200.

## References
- [1]E. Agliari, F. Alemanno, A. Barra, and A. Fachechi(2019)Dreaming neural networks: rigorous results.Journal of Statistical Mechanics: Theory and Experiment2019(8),pp. 083503.Cited by:§10.
- [2]E. Agliari, F. Alemanno, A. Barra, and A. Fachechi(2020)Generalized Guerra’s interpolation schemes for dense associative neural networks.Neural Networks128,pp. 254–267.Cited by:§1.
- [3]E. Agliari, A. Alessandrelli, A. Barra, M. S. Centonze, and F. Ricci-Tersenghi(2025)Generalized hetero-associative neural networks.Journal of Statistical Mechanics: Theory and Experiment2025(1),pp. 013302.Cited by:§1.
- [4]E. Agliari, A. Barra, A. Ladiana, and A. Lepre(2026)Thermodynamic binding: freezing chimeric states in multi-modal associative memories.InNew Frontiers in Associative Memories – Workshop at ICLR,Cited by:§10.
- [5]L. Albanese, A. Alessandrelli, A. Barra,et al.(2024)Hebbian learning from first principles.Journal of Mathematical Physics65,pp. 113302.Cited by:§1.
- [6]L. Albanese, A. Alessandrelli, A. Barra, and P. Sollich(2026)Yet another exponential Hopfield model.Neural Networks186,pp. 131223.Cited by:Appendix C,Appendix D,Appendix D,Appendix D,Appendix D,Appendix D,Appendix D,Appendix D,Appendix D,§1,§1,§2,§4,Figure 2,§6,§6,§7,Remark 6,Remark 6,footnote 3.
- [7]A. Alessandrelli, A. Barra, A. Ladiana, A. Lepre, and F. Ricci-Tersenghi(2025)Supervised and unsupervised protocols for hetero-associative neural networks.Physica A: Statistical Mechanics and its Applications,pp. 130871.Note:arXiv:2505.18796Cited by:§1.
- [8]A. Alessandrelli, F. Durante, A. Ladiana, and A. Lepre(2026)A federated many-to-one Hopfield model for associative neural networks.arXiv preprint arXiv:2603.19902.Cited by:§10.
- [9]D. J. Amit, H. Gutfreund, and H. Sompolinsky(1985)Spin-glass models of neural networks.Physical Review A32(2),pp. 1007–1018.Cited by:§1,§4.
- [10]D. J. Amit, H. Gutfreund, and H. Sompolinsky(1985)Storing infinite numbers of patterns in a spin-glass model of neural networks.Physical Review Letters55(14),pp. 1530–1533.Cited by:§1.
- [11]D. J. Amit(1989)Modeling brain function: the world of attractor neural networks.Cambridge University Press,Cambridge.Cited by:§4.
- [12]W. R. Atchley, J. Zhao, A. D. Fernandes, and T. Drüke(2005)Solving the protein sequence metric problem.Proceedings of the National Academy of Sciences102(18),pp. 6395–6400.Cited by:Appendix G,§1,§8.
- [13]D. V. Bagaev, R. M. A. Vroomans, J. Samir, U. Stervbo, C. Rius, G. Dolton, A. Greenshields-Watson, M. Attaf, E. S. Egorov, I. V. Zvyagin,et al.(2020)VDJdb in 2019: database extension, new analysis infrastructure and a T-cell receptor motif compendium.Nucleic Acids Research48(D1),pp. D1057–D1062.Cited by:Appendix G,§1,§8.
- [14]P. Baldi and S. S. Venkatesh(1987)Number of stable points for spin-glasses and neural networks of higher orders.Physical Review Letters58(9),pp. 913–916.Cited by:§1.
- [15]H. Bao, R. Zhang, and Y. Mao(2022)The capacity of the dense associative memory networks.Neurocomputing469,pp. 198–208.Cited by:§1.
- [16]A. Barra, M. Beccaria, and A. Fachechi(2018)A new mechanical approach to handle generalized Hopfield neural networks.Neural Networks106,pp. 205–222.Cited by:§1.
- [17]A. Barra, F. Durante, A. Ladiana, and M. M. Solazzo(2026)Do Hopfield networks dream of stored patterns? A statistical-mechanical theory of dreaming in multidirectional associative memories.arXiv preprint arXiv:2605.13721.Cited by:§10.
- [18]A. Barra(2006)Irreducible free energy expansion and overlaps locking in mean field spin glasses.Journal of Statistical Physics123(3),pp. 601–614.Cited by:§3.
- [19]M. S. Centonze, I. Kanter, and A. Barra(2024)Statistical mechanics of learning via reverberation in bidirectional associative memories.Physica A: Statistical Mechanics and its Applications637,pp. 129512.Cited by:§1.
- [20]M. S. Charikar(2002)Similarity estimation techniques from rounding algorithms.InProceedings of the 34th Annual ACM Symposium on Theory of Computing (STOC),pp. 380–388.Cited by:Appendix G,Appendix H,§1,§8.
- [21]A. C. C. Coolen, R. Kühn, and P. Sollich(2005)Theory of neural information processing systems.Oxford University Press.Cited by:Appendix B,§4.
- [22]A. Dembo and O. Zeitouni(1998)Large deviations techniques and applications.2nd edition,Springer,New York.Cited by:§4.2.
- [23]M. Demircigil, J. Heusel, M. Löwe, S. Upgang, and F. Vermet(2017)On a model of associative memory with huge storage capacity.Journal of Statistical Physics168(2),pp. 288–299.Cited by:§1,§4.
- [24]B. Derrida(1981)Random-energy model: an exactly solvable model of disordered systems.Physical Review B24(5),pp. 2613–2626.Cited by:§1.
- [25]E. Dohmatob(2023)A different route to exponential storage capacity.InAssociative Memory and Hopfield Networks in 2023 (NeurIPS Workshop),Cited by:§1.
- [26]A. Fachechi, E. Agliari, and A. Barra(2019)Dreaming neural networks: forgetting spurious memories and reinforcing pure ones.Neural Networks112,pp. 24–40.Cited by:§10.
- [27]E. Gardner(1985)Spin glasses with p-spin interactions.Nuclear Physics B257,pp. 747–765.Cited by:§1.
- [28]E. Gardner(1987)Multiconnected neural network models.Journal of Physics A: Mathematical and General20(11),pp. 3453.Cited by:§1.
- [29]F. Gerace, B. Loureiro, F. Krzakala, M. Mézard, and L. Zdeborová(2020)Generalisation error in learning with random features and the hidden manifold model.InInternational Conference on Machine Learning,pp. 3452–3462.Cited by:Appendix F,§1,§7.
- [30]J. Glanville, H. Huang, A. Nau, O. Hatton, L. E. Wagar, F. Rubelt, X. Ji, A. Han, S. M. Krams, C. Pettus,et al.(2017)Identifying specificity groups in the T-cell receptor repertoire.Nature547(7661),pp. 94–98.Cited by:Appendix G.
- [31]S. Goldt, M. Mézard, F. Krzakala, and L. Zdeborová(2020)Modeling the influence of data structure on learning in neural networks: the hidden manifold model.Physical Review X10(4),pp. 041044.Cited by:Appendix F,§1,§10,§7.
- [32]F. Guerra(1995)The cavity method in the mean field spin glass model. Functional representations of thermodynamic variables.InAdvances in Dynamical Systems and Quantum Physics,pp. 141–156.Cited by:§3.
- [33]C. J. Hillar and N. M. Tran(2018)Robust exponential memory in Hopfield networks.Journal of Mathematical Neuroscience8(1),pp. 1–20.Cited by:§1.
- [34]B. Hoover, Y. Liang, B. Pham, R. Panda, H. Strobelt, D. H. Chau, M. Zaki, and D. Krotov(2024)Energy transformers.InAdvances in Neural Information Processing Systems,Vol.36.Cited by:§1.
- [35]J. J. Hopfield(1982)Neural networks and physical systems with emergent collective computational abilities.Proceedings of the National Academy of Sciences79(8),pp. 2554–2558.Cited by:§1.
- [36]S. Kalaj, C. Lauditi, G. Perugini, C. Lucibello, E. M. Malatesta, and M. Negri(2024)Random features Hopfield networks generalize retrieval to previously unseen examples.arXiv preprint arXiv:2407.05658.Cited by:§1,§10,§10.
- [37]D. Krotov and J. J. Hopfield(2016)Dense associative memory for pattern recognition.InAdvances in Neural Information Processing Systems,Vol.29,pp. 1172–1180.Cited by:§1,footnote 4.
- [38]D. Krotov and J. J. Hopfield(2018)Dense associative memory is robust to adversarial inputs.Neural Computation30(12),pp. 3151–3167.Cited by:§1.
- [39]D. Krotov and J. J. Hopfield(2020)Large associative memory problem in neurobiology and machine learning.arXiv preprint arXiv:2008.06996.Cited by:§1.
- [40]D. Krotov(2023)A new frontier for Hopfield networks.Nature Reviews Physics5(7),pp. 366–367.Cited by:§1.
- [41]A. Ladiana(2026)Finite-size scaling of hetero-associative retrieval in continuous-signal-driven Ising spin systems.arXiv preprint arXiv:2605.14059.Cited by:§10.
- [42]S. Larson, A. Mahendran, J. J. Peper, C. Clarke, A. Lee, P. Hill, J. K. Kummerfeld, K. Leach, M. A. Laurenzano, L. Tang, and J. Mars(2019)An evaluation dataset for intent classification and out-of-scope prediction.InProceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP-IJCNLP),pp. 1311–1316.Cited by:Appendix H,§1,§9.
- [43]C. Lucibello and M. Mézard(2024)Exponential capacity of dense associative memories.Physical Review Letters132(7),pp. 077301.Cited by:§1.
- [44]M. Mézard, G. Parisi, and M. A. Virasoro(1986)SK model: the replica solution without replicas.Europhysics Letters1(2),pp. 77–82.Cited by:§3.
- [45]M. Mézard, G. Parisi, and M. A. Virasoro(1987)Spin glass theory and beyond.World Scientific.Cited by:Appendix B,§3.
- [46]M. Mézard(2017)Mean-field message-passing equations in the Hopfield model and its generalizations.Physical Review E95(2),pp. 022117.Cited by:§3.
- [47]M. Negri, C. Lauditi, G. Perugini, C. Lucibello, and E. Malatesta(2023)Storage and learning phase transitions in the random-features Hopfield model.Physical Review Letters131(25),pp. 257301.Cited by:§1,§10,§10.
- [48]L. Onsager(1936)Electric moments of molecules in liquids.Journal of the American Chemical Society58(8),pp. 1486–1493.Cited by:§3.
- [49]L. Pastur, M. Shcherbina, and B. Tirozzi(1999)On the replica symmetric equations for the Hopfield model.Journal of Mathematical Physics40(8),pp. 3930–3947.Cited by:§3.
- [50]H. Ramsauer, B. Schäfl, J. Lehner, P. Seidl, M. Widrich, T. Adler, L. Gruber, M. Holzleitner, M. Pavlović, G. K. Sandve, V. Greiff, D. Kreil, M. Kopp, G. Klambauer, J. Brandstetter, and S. Hochreiter(2021)Hopfield networks is all you need.InInternational Conference on Learning Representations,Cited by:§1.
- [51]M. Shugay, D. V. Bagaev, I. V. Zvyagin, R. M. A. Vroomans, J. C. Crawford, G. Dolton, E. A. Komech, A. L. Sycheva, A. E. Koneva, E. S. Egorov,et al.(2018)VDJdb: a curated database of T-cell receptor sequences of known antigen specificity.Nucleic Acids Research46(D1),pp. D419–D427.Cited by:Appendix G,§1,§8.
- [52]S. R. S. Varadhan(1966)Asymptotic probabilities and differential equations.Communications on Pure and Applied Mathematics19(3),pp. 261–286.Cited by:§4.2.

## 


- 


Major funding support from
