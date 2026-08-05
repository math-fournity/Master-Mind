# Microscopic dynamics of consensus formation in multi-agent LLM Naming Games

**arXiv ID**: 2608.02178v1
**Authors**: Cristiano De Nobili, Vijayasri Iyer, Alessandro Codello, Raffaella Burioni
**Published**: 2026-08-03
**Categories**: physics.soc-ph, cond-mat.stat-mech, cs.MA, nlin.AO
**Comments**: 8 pages, 8 figures, 1 table, 1 appendix
**HTML URL**: https://arxiv.org/html/2608.02178v1

## Abstract

Decentralized populations of Large Language Model (LLM) agents can spontaneously reach consensus on shared conventions, yet the microscopic mechanisms by which their internal stochasticity shapes macroscopic ordering remain unexplored. We study a minimal LLM Naming Game in which the listener's decision is a single-token LLM call at decoding temperature $T$, replacing the inventory check of the deterministic Naming Game. Each interaction decomposes into an in-inventory and an out-inventory channel with conditional rates $π(T)\!\equiv\!P(\text{YES}\mid w\in P_j)$ and $φ(T)\!\equiv\!P(\text{YES}\mid w\notin P_j)$, whose balance controls an ordering-disordering drift. A mean-field theory of the two-rate dynamics yields an analytical ordering condition that generalizes the consensus threshold of the stochastic Naming Game to a critical line in the $(π,φ)$ plane. Across three open-weight architectures, consensus is always reached, but through three distinct listener regimes: permissive (repaint-noise dominated), near-deterministic, and conservative (missed-collapse dominated). The effective finite-size exponent $β(T)$ in $t_{\rm conv}\!\sim\!N^β$ shifts with temperature, and the temperature-sensitivity $α$ in $t_c\!\sim\!e^{αT}$ ranges from ${\approx}\,0.67$ to ${\approx}\,0$ across architectures. Decoding temperature thus emerges as an architecture-dependent control parameter for decentralized LLM populations, quantitatively characterized by the statistical-physics toolkit.

## Full Text

Microscopic dynamics of consensus formation in multi-agent LLM Naming Games

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2608.02178v1 [physics.soc-ph] 03 Aug 2026

email: ]cristiano@critiqality.ai

## Microscopic dynamics of consensus formation in multi-agent LLM Naming GamesCristiano De Nobili[Critiqality, Via Pinturicchio 21, 20133, Milan, ItalyVijayasri IyerIndependent ResearcherAlessandro CodelloDSMN, Ca’ Foscari University of Venice, Via Torino 155, 30172 Venice, ItalyIFFI, Universidad de la República, J.H.y Reissig 565, 11300 Montevideo, UruguayRaffaella BurioniDipartimento di Scienze Matematiche, Fisiche e Informatiche,
Università degli Studi di Parma, Parco Area delle Scienze, 7/A 43124 Parma, ItalyINFN, Gruppo Collegato di Parma, Parco Area delle Scienze 7/A, 43124 Parma, Italy

## Abstract

Decentralized populations of Large Language Model (LLM) agents can spontaneously reach consensus on shared conventions, yet the microscopic mechanisms by which their internal stochasticity shapes macroscopic ordering remain unexplored. We study a minimal LLM Naming Game in which the listener’s decision is a single-token LLM call at decoding temperatureTT, replacing the inventory check of the deterministic Naming Game. Each interaction decomposes into an in-inventory and an out-inventory channel with conditional ratesπ​(T)≡P​(YES∣w∈Pj)\pi(T)\!\equiv\!P(\text{YES}\mid w\in P_{j})andϕ​(T)≡P​(YES∣w∉Pj)\phi(T)\!\equiv\!P(\text{YES}\mid w\notin P_{j}), whose balance controls an ordering-disordering drift. A mean-field theory of the two-rate dynamics yields an analytical ordering condition that generalizes the consensus threshold of the stochastic Naming Game to a critical line in the(π,ϕ)(\pi,\phi)plane. Across three open-weight architectures, consensus is always reached, but through three distinct listener regimes: permissive (repaint-noise dominated), near-deterministic, and conservative (missed-collapse dominated). The effective finite-size exponentβ​(T)\beta(T)intconv∼Nβt_{\rm conv}\!\sim\!N^{\beta}shifts with temperature, and the temperature-sensitivityα\alphaintc∼eα​Tt_{c}\!\sim\!e^{\alpha T}ranges from≈0.67{\approx}\,0.67to≈0{\approx}\,0across architectures. Decoding temperature thus emerges as an architecture-dependent control parameter for decentralized LLM populations, quantitatively characterized by the statistical-physics toolkit.

## IIntroduction

Consensus formation, that is the spontaneous emergence of a shared convention
from purely local interactions, is a central problem at the intersection of
statistical physics, complex systems, and multi-agent
intelligence[6]. Classical agent-based models
such as the Voter model, Axelrod dynamics, and bounded-confidence frameworks
have shown that macroscopic order can arise from simple microscopic
stochastic rules, with the nature of the resulting phase transitions,
coarsening dynamics, and scaling laws depending sensitively on the
interaction topology and on the agents’ decision
rule[6]. Among these, the Naming Game
(NG)[26,4,19]occupies a
distinguished position: it provides a minimal, exactly solvable model of how
a population bootstraps a shared vocabulary through pairwise negotiation,
exhibiting symmetry breaking and a convergence timetconv∼N3/2t_{\rm conv}\sim N^{3/2}on fully connected
graphs[4]. ThedeterministicNG has been studied on
regular lattices[2], complex
networks[10], and generalized to include
irresolute agents with a tunable commitment parameter, revealing a
non-equilibrium phase transition from consensus to
fragmentation[3].

The rapid deployment of Large Language Models (LLMs) as autonomous,
interacting agents has opened a new arena for these questions. LLM-based
multi-agent systems are now used in negotiation, planning, and
tool-use[15,17], and populations of
such agents interact with one another and with humans at increasing
scale[18]. Whether and how decentralized
populations of LLMs can self-organize on shared conventions is therefore
not only a foundational scientific question but also a prerequisite for
the safe and reliable deployment of agentic AI. Recent empirical studies
have begun to answer it: Ashery, Aiello, and
Baronchelli[1]demonstrated that populations of LLM
agents playing a minimal coordination game, of the type used in human
experiments on convention formation[7], spontaneously reach
group-wide linguistic conventions and exhibit emergent collective biases
not present at the single-agent level. De Marzo, Castellano, and
Garcia[12]showed that LLM agents
can self-organize on arbitrary binary choices but only below a
model-dependent critical group size, and Flintet al.[14]developed a
mean-field analytical framework relating group size to the structure of
basins of attraction. Related work has investigated conformity and social influence in LLM
agents[11,5],
detailed balance in LLM-driven
dynamics[25], cultural attractors in
transmission chains[22], opinion dynamics in
networks of LLMs[8,23], agreement
protocols among reasoning agents[24],
and Ising-like collective alignment on
lattices[13]. Mean-field
methods from statistical mechanics have also proven effective in
large-population multi-agent reinforcement
learning[28], and differentiable surrogates of
agent-based models are being developed to bridge microscopic rules and
emergent collective phenomena[9].

A consistent picture is emerging: LLM populationsdoreach
consensus on shared conventions, the resulting macroscopic dynamics can
be modelled with statistical-physics tools, and the outcome depends in
non-trivial ways on the underlying architecture. What is still missing,
however, is a microscopic theory linking the stochasticity of LLM
inference to the macroscopic dynamics of consensus. In particular, the
decoding temperatureTT, the primary hyperparameter governing the
randomness of each agent’s output[16], has not been studied as an effective
control parameter in the statistical-physics sense; existing LLM-NG
studies fixTTto a single
value[1,14].
This gap is especially relevant as LLM agents move toward decentralized
deployment, where no central coordinator exists and collective outcomes
emerge bottom-up from local
interactions[18,9].

In this work we fill this gap. We implement the minimal NG with LLM
agents, retaining the original topology and update rule of thedeterministicNG but replacing the listener’s deterministic inventory check with a
single-token LLM call at temperatureTT. We then introduce amicroscopic decompositionof each interaction into four channels,
parametrized by two conditional rates,π​(T)\pi(T)andϕ​(T)\phi(T), and show
that this pair suffices to organize the model-dependent phenomenology
into three qualitatively distinct regimes. The
setup is deliberately minimal: it isolates the effect of LLM-generated
stochasticity on a well-understood ordering dynamics, free from
prompt engineering, multi-turn memory, or strategic play. Our main
contributions are:(i)the(π,ϕ)(\pi,\phi)decomposition itself, which compresses
the stochasticity of LLM inference into two measurable conditional
rates and thereby exposes the microscopic origin of collective order;(ii)a drift analysis that links these microscopic rates to the net ordering tendency;(iii)the identification of three qualitatively distinct
listener regimes (permissive, near-deterministic, and conservative) that
emerge from the interplay of architecture and temperature, with
qualitatively different macroscopic signatures including aninverted temperature orderingfor the conservative regime;(iv)finite-size scaling and temperature-response measurements
over the accessible rangeN∈[50,150]N\!\in\![50,150]indicating that the effective
exponentβ​(T)\beta(T)intconv∼Nβt_{\rm conv}\!\sim\!N^{\beta}varies with decoding
temperature and, for the most noise-dominated architecture, reaches values
above the canonical mean-field3/23/2, and that the exponential rateα\alphagoverningtc​(T)t_{c}(T)is itself architecture-dependent, ranging from
essentially zero to≈0.7{\approx}\,0.7across the three models tested.(v)a complete-graph mean-field theory of the two-rate
dynamics whose two-word sector yields the analytical ordering condition3​π−2​ϕ−1>03\pi-2\phi-1>0, generalizing the known threshold of the stochastic NG
and rationalizing the three regimes.
Together these results promote decoding temperature to a bona-fide
effective control parameter for decentralized LLM populations, and show
that the statistical-physics toolkit of coarsening, drift analysis, and
scaling provides a natural language for characterizing and ultimately
designing the emergent behaviour of multi-agent AI systems.

## IIModelFigure 1:Schematic of the Naming Game interaction. In thedeterministicNG, the decision step is an inventory check (w∈Pjw\in P_{j}); in the LLM-NG it is replaced by the listener’s LLM call at temperatureTT.

In thedeterministic NG,NNagents are placed on a fully connected graph. Each agentiicarries an inventoryPi​(t)⊆𝒱P_{i}(t)\subseteq\mathcal{V}, where𝒱\mathcal{V}is a pool of words. All inventories start empty. At each steptt, an ordered pair(i,j)(i,j)is drawn uniformly (speakerii, listenerjj). If an agent has an empty inventory it invents by sampling from𝒱\mathcal{V}. The speaker pickswwuniformly fromPiP_{i}and transmits it. The interaction succeeds ifw∈Pjw\in P_{j}: both agents collapse to{w}\{w\}; otherwisejjappendsww(Fig.1). On the fully connected graph, thedeterministicNG exhibits a characteristic three-stage dynamics: an initial phase in which agents
accumulate distinct words in their inventories, a coarsening stage in
which pairwise agreements build up correlations between inventories,
and a final rapid collapse to a single conventional
name[4,19]. The
resulting consensus time scales astc∼N3/2t_{c}\sim N^{3/2}, a benchmark
against which we compare the LLM-driven dynamics throughout this
work.Figure 2:The two new interaction channels of the LLM-NG that do not exist in
the deterministic NG (Fig.1). Top: amissed
collapseoccurs whenw∈Pjw\!\in\!P_{j}but the LLM answers NO, at rate1−π1{-}\pi; the inventories are left unchanged. Bottom: arepaintoccurs whenw∉Pjw\!\notin\!P_{j}but the LLM answers YES,
at rateϕ\phi; the listener discards its inventory and adopts the
alien wordww. Together with Fig.1, these panels
enumerate the four channels (TP, FN, FP, TN) into which the LLM-NG
interaction decomposes (Sec.III).

In theLLM-NG, the listener receives a prompt containing its inventory and the proposed word, and returns a single YES/NO token at temperatureTT. If YES, both collapse to{w}\{w\}; if NO,jjappendsww. The prompt used throughout our simulations is:System:“You are an agent with your own language and vocabulary. You can and must reply with yes or no.”User:“Your words are:PjP_{j}. Do we addwwto the
list?”. The only control parameter varied isTT. In this work, we chose|𝒱|=104|\mathcal{V}|\!=\!10^{4}English words. This number is much larger than any explored population size, so inventory collisions during invention are negligible and𝒱\mathcal{V}is effectively unlimited, as in thedeterministicNG[4]. We track: the number of distinct wordsNd​(t)=|⋃iPi​(t)|N_{d}(t)=|\bigcup_{i}P_{i}(t)|and the success rateS​(t)S(t). Consensus is reached attct_{c}defined byNd​(tc)=1N_{d}(t_{c})=1.

A comment on the prompt. Any wording choice can induce a listener bias beyond the architecture- and temperature-dependent one under study. Alternative phrasings such as “Is the proposed word already in your list? Answer only YES or NO.” are equally legitimate and could shift the numerical values of(π,ϕ)(\pi,\phi). A parallel statistical-physics study of LLM populations on 2D lattices[13]observes that prompt rewordings can move the effective microscopic parameters quantitatively while leaving the overall collective behaviour and its physical description qualitatively similar. Given the compute budget of the present study we did not perform a systematic prompt-variation scan and defer this robustness check to future work.

## IIIMicroscopic decomposition

At each interaction, the proposed wordwwis either already present in the listener’s inventory, or absent from it. We refer to these as the in-inventory and out-inventory channels, respectively. The LLM listener can answer YES or NO in either case, producing four microscopic outcomes:
true positive (TP:w∈Pjw\in P_{j}, YES),
false negative (FN:w∈Pjw\in P_{j}, NO),
false positive (FP:w∉Pjw\notin P_{j}, YES),
and true negative (TN:w∉Pjw\notin P_{j}, NO).
We define two conditional acceptance rates (Fig.2):π​(T)\displaystyle\pi(T)≡P​(YES∣w∈Pj)=TPTP+FN,\displaystyle\equiv P(\text{YES}\mid w\in P_{j})=\frac{\text{TP}}{\text{TP}+\text{FN}}\,,(1)ϕ​(T)\displaystyle\phi(T)≡P​(YES∣w∉Pj)=FPFP+TN.\displaystyle\equiv P(\text{YES}\mid w\notin P_{j})=\frac{\text{FP}}{\text{FP}+\text{TN}}\,.(2)

ThedeterministicNG corresponds toπ=1\pi\!=\!1,ϕ=0\phi\!=\!0:π​(T)\pi(T)is the rate at which a collapse is correctly triggered,ϕ​(T)\phi(T)the
rate at which one is triggered erroneously. To weight these rates by how
often each situation occurs, we introduce thein-inventory fractionm​(t)≡P​(w∈Pj​(t)),m(t)\;\equiv\;P\bigl(w\!\in\!P_{j}(t)\bigr)\,,(3)

that is, the probability that at timettthe transmitted wordwwalready
belongs to the listener’s inventory, averaged over uniformly random
speaker–listener pairs(i,j)(i,j)and over wordswwdrawn uniformly fromPi​(t)P_{i}(t). Empirically,m​(t)m(t)is estimated from the running fraction of in-inventory interactions,m^​(t)=TP​(t)+FN​(t)TP​(t)+FN​(t)+FP​(t)+TN​(t),\hat{m}(t)\;=\;\frac{\mathrm{TP}(t)+\mathrm{FN}(t)}{\mathrm{TP}(t)+\mathrm{FN}(t)+\mathrm{FP}(t)+\mathrm{TN}(t)}\,,(4)

evaluated in a small window aroundtt. By constructionm​(t)m(t)starts near
zero (empty or disparate inventories) and approaches unity at consensus.
The two rates then control competing tendencies: an in-inventory–YES event
(ratem​πm\,\pi) is a legitimate collapse, the ordering channel; an
out-inventory–YES event (rate(1−m)​ϕ(1{-}m)\,\phi) is arepaint, in which
the listener discards its inventory and adopts an alien word, the
disordering channel. Two clarifications on this labelling are in order. First,
“disordering” is an ensemble-averaged statement, not a property of every
event: a single repaint does commit both interacting agents to the
singleton{w}\{w\}, but becausewwis by constructionnotthe word
the listener held, repeated repaints on average redirect the population
toward random attractors rather than toward the name emerging as the
global consensus. Second, repaints are not always harmful: near
consensus, when only two or three names coexist in a metastable
configuration, a rare repaint can break the deadlock by knocking an agent
out of one attractor so that the majority absorbs it. This is how a small
residualϕ\phican accelerate late-time convergence, and why the drift
proxy introduced below predicts the sign of ordering only on average. In
what follows, “ordering” and “disordering” should be read as ensemble
labels valid at first order in a mean-field description.

We define a drift proxyΔ​(t)=m​(t)​π​(t)−λ​(1−m​(t))​ϕ​(t),\Delta(t)=m(t)\,\pi(t)-\lambda\,(1-m(t))\,\phi(t)\,,(5)

withλ=1\lambda=1. Positive drift implies net ordering; negative drift signals
that repaint noise overwhelms consolidation. The choiceλ=1\lambda\!=\!1deserves a brief comment. A
true-positive collapse consolidates two agents around a word they already
share, leaving the number ofww-holders unchanged; a false-positive
collapse instead recruits the listener into the population ofww-holders from scratch, forcing it to abandon its entire prior inventory. The consequences forNdN_{d}, for individual inventory sizes, and for the overlap distribution
therefore differ in magnitude between the two events, and a rigorous
mean-field treatment would yieldλ≠1\lambda\neq 1, possibly state-dependent.
We adoptλ=1\lambda\!=\!1as the simplest phenomenological choice: since it
is thesignofΔ\Delta, and not its magnitude, that determines the
ordering versus disordering balance and hence the three regimes of
Sec.IV.1, this suffices for the qualitative claims made here. A
mean-field derivation ofλ\lambdafrom the microscopic rates, along the
lines of Ref.[3], is a natural
extension.

The(π,ϕ)(\pi,\phi)plane
organizes several known limits: thedeterministicNG
(π=1,ϕ=0\pi\!=\!1,\phi\!=\!0)[4], lazy consolidation
(π<1,ϕ=0\pi\!<\!1,\phi\!=\!0), voter-like (π=1,ϕ=1\pi\!=\!1,\phi\!=\!1), and
maximal chaos (π=0,ϕ=1\pi\!=\!0,\phi\!=\!1). The lazy-consolidation edge is
the stochastic negotiation model of Baronchelli, Dall’Asta, Barrat, and
Loreto[3], whose hand-tuned
commitment probabilityβ\betaplays the role ofπ\pi, withϕ\phiidentically zero by construction because out-inventory interactions cannot
trigger a collapse in their update rule. The decisive difference, developed
in Sec.VIII, is that theirβ\betais imposed externally on
the update rule, whereas ourπ​(T)\pi(T)andϕ​(T)\phi(T)are emergent outputs of
the LLM listener, measured a posteriori from actual multi-agent
simulations.

## IVResults

We simulate the LLM-NG for three open-weight models served locally via
Ollama[21]:llama3.1:8b(Meta),mistral:7b(Mistral AI), andphi3:14b(Microsoft).
Unless stated otherwise,N=150N=150agents interact for up to10510^{5}steps
(1.75×1051.75\times 10^{5}forphi3:14b), withT∈{0.05,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0}T\in\{0.05,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0\}.
Each configuration is averaged over1010to1515seeds.
Throughout, consensus is defined by strict11-consensus
(Nd​(tc)=1N_{d}(t_{c})\!=\!1); central lines in all consensus-time plots show themedianacross seeds, and shaded bands span the interquartile range
(p25, p75). This robust statistic was preferred over the mean and standard
deviation because of the heavy-tailed seed distributions characteristic of
the conservative listener regime.

## IV.1Microscopic rates

Figure3summarizes the microscopic behaviour of the three
models through the conditional ratesπ​(t)\pi(t)andϕ​(t)\phi(t).

llama3.1:8b(permissive listener).The consolidation rateπ​(t)\pi(t)settles at a temperature-dependent plateau:≈1.0{\approx}\,1.0atT=0.05T\!=\!0.05, decreasing to≈0.55{\approx}\,0.55atT=2.0T\!=\!2.0(Fig.3a). The repaint rateϕ​(t)\phi(t)starts high and
decays as the system orders (Fig.3d): atT=2.0T\!=\!2.0,ϕ\phireaches≈0.50{\approx}\,0.50at early times, remaining elevated for
tens of thousands of steps. Bothπ\piandϕ\phishow clear, monotonic
temperature ordering. This places llama in arepaint-noise dominatedregime whereϕ\phiis the main lever through which temperature controls
the dynamics.

mistral:7b(near-deterministic listener).π​(t)\pi(t)saturates at≈1.0{\approx}\,1.0foralltested temperatures
(Fig.3b), andϕ​(t)\phi(t)shows only a small early-time
hump (≲0.15{\lesssim}\,0.15) that decays to zero byt≈5×103t\!\approx\!5\times 10^{3}(Fig.3e). A subtle but robustinverted temperature
orderingappears in the transient: theT=0.05T\!=\!0.05curve has the slowestπ\piapproach and thehighestearly-timeϕ\phipeak, whileT=2.0T\!=\!2.0converges fastest. At lowTT, the listener is slightly
more conservative and makes errors in both directions; higherTTincreases
overall permissiveness, paradoxically improving consistency. Sinceϕ\phiis already small, this cost is negligible and the net effect is beneficial.

phi3:14b(conservative listener).π​(t)\pi(t)settles at
dramatically lower plateaux:≈0.75{\approx}\,0.75atT=0.05T\!=\!0.05, falling
to≈0.30{\approx}\,0.30atT=2.0T\!=\!2.0(Fig.3c). AtT=2.0T\!=\!2.0, 70% of in-inventory interactions fail to trigger the collapse
they should. Meanwhileϕ​(t)\phi(t)is near zero at all temperatures
(Fig.3f), with only a faint persistent level≈0.03{\approx}\,0.03–0.050.05atT=2.0T\!=\!2.0.
This places phi3 in thelazy-consolidationlimit
(π<1\pi<1,ϕ≈0\phi\approx 0): the disordering channel is shut off, but the
ordering channel is heavily attenuated.Figure 3:Microscopic conditional rates forN=150N\!=\!150agents at selected
temperatures.Top row:consolidation rateπ​(t)=P​(YES∣w∈Pj)\pi(t)\!=\!P(\text{YES}\mid w\in P_{j})for
(a)llama3.1:8b, (b)mistral:7b, (c)phi3:14b.
Dashed line:deterministicNG (π=1\pi\!=\!1).Bottom row:repaint
rateϕ​(t)=P​(YES∣w∉Pj)\phi(t)\!=\!P(\text{YES}\mid w\notin P_{j})for
(d)llama3.1:8b, (e)mistral:7b, (f)phi3:14b.
Dashed line:deterministicNG (ϕ=0\phi\!=\!0). Shaded bands indicate
seed-to-seed variance. Note the differentyy-axis scales in the bottom
row, reflecting the order-of-magnitude difference in repaint noise across
models.Figure 4:Drift proxyΔ​(t)=m​π−λ​(1−m)​ϕ\Delta(t)=m\pi-\lambda(1{-}m)\phi(λ=1\lambda\!=\!1)
for (a)llama3.1:8b, (b)mistral:7b,
(c)phi3:14b. Positive drift implies net ordering.Figure 5:Logarithm of the number of distinct wordsln⁡Nd​(t)\ln N_{d}(t)forN=150N\!=\!150agents at all explored temperatures (colour-coded from dark=\,=\,lowTTto light=\,=\,highTT). Solid black:deterministicNG baseline.
(a)llama3.1:8b: standard ordering (highTT= slow).
(b)mistral:7b: near-deterministic, allTTbunched.
(c)phi3:14b:invertedordering (lowTT= slowest).Figure 6:Average inventory sizek¯​(t)=N−1​∑i|Pi​(t)|\bar{k}(t)=N^{-1}\sum_{i}|P_{i}(t)|forN=150N\!=\!150agents at all explored temperatures for
(a)llama3.1:8b, (b)mistral:7b,
(c)phi3:14b. Central lines are seed averages; shaded bands
are one standard error. Note the different vertical scales: the phi3
panel spans roughly an order of magnitude more than the other two.Figure 7:Finite-size scaling of the consensus timetct_{c}vs.NN(log-log) for
(a)llama3.1:8b,
(b)mistral:7b,
(c)phi3:14b.
Each colour is a different temperature. Central lines are medians
across seeds, shaded bands are the interquartile range.
Dashed black: average power-law guideN⟨β⟩N^{\langle\beta\rangle}.
Upward arrows indicate lower bounds: at least one seed did not reach
consensus within the simulation horizon, so the truetct_{c}is at least
as large as the plotted value.

## IV.2Drift and macroscopic convergence

The drift proxyΔ​(t)\Delta(t), Eq. (5), translates the
microscopic rates into a net ordering tendency (Fig.4).

Forllama(Fig.4a),Δ\Deltais strongly
temperature-dependent: atT=0.05T\!=\!0.05it reaches unity
(indistinguishable fromdeterministicNG), while atT=2.0T\!=\!2.0it starts
weakly negative (repaint noise overwhelms consolidation) and climbs only
slowly to≈0.55{\approx}\,0.55. The time spent at low or negative drift
maps directly onto the long plateaux inNd​(t)N_{d}(t)(Fig.5a).

Formistral(Fig.4b), all temperatures converge
toΔ=1\Delta\!=\!1within∼104{\sim}\,10^{4}steps. Surprisingly,T=0.05T\!=\!0.05shows the deepest early negative dip (≈−0.25{\approx}\,{-}0.25), reflecting
the inverted-transient physics: the conservative low-TTlistener
produces both missed collapses (lowerπ\pi) and a slightly elevatedϕ\phiin the early disordered phase.

Forphi3(Fig.4c),Δ\Deltais always positive
(no repaint noise) but never exceeds≈0.75{\approx}\,0.75. The drift mirrorsπ\pi: weak but directed ordering without disordering competition.

The macroscopic convergence (Fig.5) reveals three qualitatively
different responses ofNd​(t)N_{d}(t)to temperature:

llama(Fig.5a) showsstandardtemperature
ordering: higherTTproduces longer plateaux and slower convergence,
reflecting the monotonic growth of repaint noiseϕ​(T)\phi(T).

mistral(Fig.5b) shows all temperature curves
bunched tightly together and decayingfasterthan the deterministic
baseline during the initial phase. The mild late-time splitting is
consistent with the inverted transient: low-TTcurves have slightly longer
tails.

phi3(Fig.5c) shows astrongly invertedtemperature ordering: the lowest temperature (T=0.05T\!=\!0.05, highestπ\pi)
is theslowestto converge, withNdN_{d}plateauing at≈7{\approx}\,7distinct words through9×1049\times 10^{4}steps without
reaching consensus. Higher temperatures converge faster despite having
lowerπ\pi. The mechanism is directly visible in the average inventory sizek¯​(t)=N−1​∑i|Pi​(t)|\bar{k}(t)=N^{-1}\sum_{i}|P_{i}(t)|(Fig.6). For phi3
atT=0.05T\!=\!0.05, agents accumulate on average up to≈34{\approx}\,34words each aroundt≈7×104t\!\approx\!7\times 10^{4}and
remain at a large-inventory plateauk¯≳30\bar{k}\!\gtrsim\!30throughout the entire1.75×1051.75\times 10^{5}-step simulation window
without reaching consensus; atT=2.0T\!=\!2.0, by contrast,k¯\bar{k}peaks briefly below≈4{\approx}\,4and decays tok¯≈1\bar{k}\!\approx\!1within∼104{\sim}\,10^{4}steps. llama and
mistral peak atk¯≲5\bar{k}\!\lesssim\!5at every temperature and
collapse tok¯=1\bar{k}\!=\!1within𝒪​(104)\mathcal{O}(10^{4})steps.
This order-of-magnitude architecture-dependent difference in
per-agent inventory size is the microscopic origin of phi3’s
inverted temperature ordering: the narrowπ≈0.75\pi\!\approx\!0.75channel must consolidate a much larger accumulated vocabulary at
lowTTthan at highTT. A faint persistentϕ≈0.04\phi\!\approx\!0.04atT=2.0T\!=\!2.0may further help break
late-time deadlocks.

This inverted ordering demonstrates that the macroscopic convergence speed
is not determined byπ\pialone, but by the interplay ofπ\piwith the
inventory structure, a genuinely new feature of the LLM-NG that
emerges only when temperature is varied systematically.

## VFinite-size scaling

In thedeterministicNG on a fully connected graph,tconv∼N3/2t_{\rm conv}\sim N^{3/2}[4]. This scaling results from the interplay between the initial phase of word accumulation in the inventories of individual agents, the increase in correlations among the inventories of different agents, and the final coarsening collapse. We measuretconv​(N,T)t_{\rm conv}(N,T)forN∈{50,70,90,110,150}N\in\{50,70,90,110,150\}and fittconv∼Nβ​(T)t_{\rm conv}\sim N^{\beta(T)}(Fig.7). The explored
range spans only about half a decade inNN, so the fitted exponents
should be interpreted aseffectivequantities over this window
rather than as asymptotic critical exponents; a definitive determination
of the true asymptotic scaling would require sizes at least an order of
magnitude larger, beyond the reach of the present LLM-inference budget.

Forllama(Fig.7a), the effective exponent
varies fromβ≈1.3\beta\!\approx\!1.3at lowTTtoβ≈2.0\beta\!\approx\!2.0atT=2.0T\!=\!2.0, with a temperature-averaged value⟨β⟩=1.61±0.28\langle\beta\rangle\!=\!1.61\pm 0.28. Over the accessible size range,β​(T)\beta(T)reaches values above the canonical3/23/2at high temperatures,
consistent with persistent repaint noise slowing the ordering drift.
Whether this reflects a genuine change of universality class or a slow
crossover to the deterministic3/23/2asymptote at largerNNcannot be
decided from the current data.

Formistral(Fig.7b) we obtain⟨β⟩=1.28±0.13\langle\beta\rangle\!=\!1.28\pm 0.13, broadly consistent with an exponent
near the canonical3/23/2and tighter than for the other two architectures.
This is the expected behaviour for a near-deterministic listener whose
microscopic rates barely depend on temperature.

Forphi3(Fig.7c) we find⟨β⟩=1.59±0.47\langle\beta\rangle\!=\!1.59\pm 0.47, consistent with3/23/2within the
sizable uncertainty. The wide IQR bands and the persistent lower-bound
arrows in Fig.7c are not statistical undersampling: with1515seeds at horizon1.75×1051.75\times 10^{5}steps they reflect theintrinsicpath-dependence of the conservative listener regime,
where low-π\pidynamics make consensus trajectories strongly history
dependent. The reported value should be interpreted as a lower bound on
the true exponent, since seeds that fail to reach strict consensus within
the simulation horizon would, on average, raise it. It is worth noting
that phi3 is the empirical LLM realization of the lazy-consolidation
model of Ref.[3]: to a very good
approximation (ϕ≈0\phi\!\approx\!0at everyTT), phi3’s dynamics
coincides with theirs under the identificationβ↔π​(T)\beta\!\leftrightarrow\!\pi(T). Their analytical prediction of a
consensus–fragmentation transition atβc=1/3\beta_{c}\!=\!1/3is therefore a
direct, testable expectation for the phi3 regime (the same threshold emerges from the two-word mean field of Sec.VIIas theϕ=0\phi\!=\!0limit of the critical line): since phi3’s measuredπ\piranges from≈0.75{\approx}\,0.75atT=0.05T\!=\!0.05to≈0.30{\approx}\,0.30atT=2.0T\!=\!2.0(Sec.IV.1), the threshold is nominally crossed
inside the accessible temperature window. We nevertheless observe strict
consensus at every temperature (Sec.VIII), so testing the
prediction properly would require system sizes larger than those explored
here.

## VITemperature response of the consensus time

While Fig.7examines howtct_{c}scales withNNat fixed
temperature, the complementary question is howtct_{c}depends onTTat
fixedNN. We address it in Fig.8, which displaystc​(T)t_{c}(T)forN∈{50,70,90,110,150}N\in\{50,70,90,110,150\}across the three architectures.
Becausetct_{c}varies multiplicatively withTT, we fit each curve in
log-linear form,ln⁡tc​(T)=ln⁡A+α​T,\ln t_{c}(T)\,=\,\ln A\,+\,\alpha\,T\,,(6)

so thattc​(T)=A​eα​Tt_{c}(T)\!=\!A\,e^{\alpha T}and the slopeα\alphahas units of
inverse temperature. The sign and magnitude ofα\alphaprovide a direct,
single-number summary of the temperature sensitivity of the macroscopic
consensus dynamics:α>0\alpha\!>\!0meanstct_{c}grows withTT,α≈0\alpha\!\approx\!0meansTT-independence, andα<0\alpha\!<\!0would
indicate accelerated convergence withTT. The exponential form mirrors
the power-law guide of Fig.7(a straight line on log-y)
and produces a clean dashed-line overlay on each panel of
Fig.8.Figure 8:Temperature response of the consensus timetct_{c}vs.TT(log-y, linear-x)
for (a)llama3.1:8b, (b)mistral:7b,
(c)phi3:14b. Each colour is a different agent countN∈{50,70,90,110,150}N\!\in\!\{50,70,90,110,150\}; central lines are medians across seeds and
shaded bands span the interquartile range. Dashed black: average
exponential guidetc∼e⟨α⟩​Tt_{c}\!\sim\!e^{\langle\alpha\rangle\,T}. The fitted
rates are⟨α⟩=0.67±0.14\langle\alpha\rangle\!=\!0.67\pm 0.14forllama,⟨α⟩=0.01±0.02\langle\alpha\rangle\!=\!0.01\pm 0.02formistral, and⟨α⟩=0.43±0.31\langle\alpha\rangle\!=\!0.43\pm 0.31forphi3.
Upward arrows indicate lower bounds: at least one seed did not reach
consensus within the simulation horizon.

The three measured rates differ qualitatively across architectures and map
cleanly onto the(π,ϕ)(\pi,\phi)regimes identified in
Sec.IV.1.

## llama (permissive listener,α=0.67±0.14\alpha\!=\!0.67\pm 0.14).

The exponent is clearly positive and statistically significant: across the
explored rangetct_{c}grows by a factore0.67×2.0≈4e^{0.67\times 2.0}\!\approx\!4.
This is the macroscopic fingerprint of the repaint-dominated regime: asTTrises,ϕ​(T)\phi(T)grows and the disordering channel becomes increasingly
active; the consensus time inherits this growth at an exponential rate. The
exponential, rather than linear, dependence onTTis itself informative; it
suggests thattct_{c}is sensitive to thecumulativeeffect of many
repaint events along an ordering trajectory, rather than to any single
rate-limiting step.

## mistral (near-deterministic listener,α=0.01±0.02\alpha\!=\!0.01\pm 0.02).

The exponent is indistinguishable from zero:tct_{c}is statisticallyindependentof decoding temperature across a40×40\timesrange inTT.
This is the macroscopic fingerprint of the near-deterministic regime:
withπ≈1\pi\!\approx\!1andϕ≈0\phi\!\approx\!0at everyTT(Sec.IV.1), neither microscopic rate has room to move, and the
resulting consensus dynamics is effectively decoupled from the LLM’s primary
stochasticity knob. A similar architecture-dependent insensitivity to
decoding temperature has been reported in a related statistical-physics
study of LLM populations on
lattices[13],
suggesting that this “temperature blindness” is a robust feature of
certain LLM architectures across distinct collective-dynamics settings.

## phi3 (conservative listener,α=0.43±0.31\alpha\!=\!0.43\pm 0.31).

The central value is positive and moderate, but the uncertainty band
overlaps zero. Together with the wide IQR shading in
Fig.8c, this reflects the genuine path-dependence of the
conservative regime: low-π\pidynamics is intrinsically variable from
seed to seed, and the temperature response is more subtle than for the
other two architectures. The trend is mediated by the
inventory-diversity mechanism described in Sec.IV.2rather
than by a direct change in the microscopic rates, sinceϕ\phiremains
near zero at everyTT.

The pair(β,α)(\beta,\alpha)thus provides a compact two-dimensional
fingerprint of each architecture in the multi-agent NG:β\betameasures how
the consensus time scales with system size,α\alphahow it responds to
decoding temperature. Their joint values cleanly separate the three regimes
(Table1).

## VIIMean-field theory of the two-rate dynamics

At fixed decoding temperature, the LLM listener can be approximated by
the effective two-rate ruleq​(YES∣Pj,w)={π,w∈Pj,ϕ,w∉Pj,q(\text{YES}\mid P_{j},w)\;=\;\begin{cases}\pi,&w\in P_{j},\\[2.0pt]
\phi,&w\notin P_{j},\end{cases}(7)

withπ\piandϕ\phitreated as constants, in practice the plateau
valuesπ¯​(T)\bar{\pi}(T)andϕ¯​(T)\bar{\phi}(T)of Sec.IV.1. This
defines a stochastic NG with two acceptance channels that contains the
deterministic NG (π=1\pi\!=\!1,ϕ=0\phi\!=\!0) and the stochastic
negotiation model of Ref.[3](π=β\pi\!=\!\beta,ϕ=0\phi\!=\!0) as special cases, and for which exact complete-graph mean-field equations can be written for the densities of agents carrying each possible inventory. The resulting(2m−1)(2^{m}{-}1)-dimensional hierarchy is not solvable in closed form, but it admits a natural approximate closure for the inventory-size
distribution; both are given in AppendixA. The
critical line, however, follows analytically from the two-word sector, to which we now turn.

The ordering mechanism is exposed by the two-word sector. When only two
wordsAAandBBcompete, each agent is in one of three states,AA,BB, orA​BAB, with fractionsxx,yy, andz=1−x−yz=1-x-y. On the complete
graph the mean-field equations readx˙\displaystyle\dot{x}=−(1−ϕ)​x​y+3​π−12​x​z+ϕ​y​z+π​z2,\displaystyle=-(1-\phi)\,xy+\tfrac{3\pi-1}{2}\,xz+\phi\,yz+\pi z^{2},(8)y˙\displaystyle\dot{y}=−(1−ϕ)​x​y+3​π−12​y​z+ϕ​x​z+π​z2,\displaystyle=-(1-\phi)\,xy+\tfrac{3\pi-1}{2}\,yz+\phi\,xz+\pi z^{2},(9)

reducing to the standard NG mean field forπ=1\pi\!=\!1,ϕ=0\phi\!=\!0.
Introducing the magnetization-like order parameteru=x−yu=x-yand
subtracting Eq. (9) from Eq. (8) givesu˙=z2​(3​π−2​ϕ−1)​u.\dot{u}\;=\;\frac{z}{2}\,\bigl(3\pi-2\phi-1\bigr)\,u\,.(10)

The symmetric state is unstable, and one word is amplified over the
other, whenR≡3​π−2​ϕ−1>0,i.e.π>πc​(ϕ)=1+2​ϕ3.R\;\equiv\;3\pi-2\phi-1\;>\;0,\quad\text{i.e.}\quad\pi\;>\;\pi_{c}(\phi)=\frac{1+2\phi}{3}\,.(11)

Forϕ=0\phi\!=\!0this recovers the known thresholdβc=1/3\beta_{c}\!=\!1/3of
the stochastic NG[3]; the
false-positive channel shifts the threshold upward along the critical
lineπc​(ϕ)\pi_{c}(\phi), quantifying how repaint noise obstructs ordering.
The quantityRRthus plays the role of the effective distance from the
transition, replacing the scalarβ−βc\beta-\beta_{c}, and provides an
analytical counterpart to the phenomenological drift proxy of
Eq. (5).

Evaluated on the measured plateau rates,RRrationalizes the three
regimes. Formistral,π¯≈1\bar{\pi}\!\approx\!1andϕ¯≈0\bar{\phi}\!\approx\!0giveR≈2R\!\approx\!2, the maximum possible
value: the dynamics sits deep inside the ordering region at every
temperature, which is precisely the temperature blindness of
Sec.VI. Forllama, increasingTTlowersπ\piand raisesϕ\phi; both changes decreaseRR, predicting the
observed monotonic slowdown, and the elevated early-timeϕ\phiatT=2.0T\!=\!2.0transiently drivesRRnegative, consistent with the
negative drift transient of Fig.4a. Forphi3,ϕ¯≈0\bar{\phi}\!\approx\!0reduces the condition toπ>1/3\pi>1/3: the measured
plateau falls fromπ¯≈0.75\bar{\pi}\!\approx\!0.75(R≈1.25R\!\approx\!1.25) atT=0.05T\!=\!0.05toπ¯≈0.30\bar{\pi}\!\approx\!0.30(R≈−0.1R\!\approx\!-0.1) atT=2.0T\!=\!2.0, nominally crossing the critical line inside the explored
temperature window. That strict consensus is nevertheless reached at
all temperatures (Sec.VIII) is consistent with the
mean-field transition being sharp only asN→∞N\to\inftyand with the
time dependence of the measured rates, and identifies phi3 at highTTas the natural setting in which to search for a fragmented phase at
larger system sizes. By construction, the two-word reduction does not capture the inventory-size effects that dominate phi3 at lowTT(Sec.IV.2); the inventory-size closure of
AppendixAis the natural starting point to include them.

## VIIIDiscussion and outlook

The central result of this work is that two conditional rates,π​(T)\pi(T)andϕ​(T)\phi(T), provide a compact microscopic parametrisation of the
LLM-NG that captures its leading-order macroscopic phenomenology and
cleanly organizes the observed architecture-dependent behaviour into
three qualitatively distinct regimes (Table1). The(π,ϕ)(\pi,\phi)pair is not a full microscopic theory: it averages over
inventory size, over word identity, and over per-agent heterogeneity,
and phi3 already provides an example (Sec.IV.2) in which
macroscopic convergence is co-determined byπ\piand by the inventory
structure it generates. Nevertheless, the sign of the drift proxyΔ​(t)\Delta(t)built from(π,ϕ)(\pi,\phi)tracks the qualitative
ordering / disordering balance of every architecture we tested, and
the pair suffices as a first-order diagnostic and classification tool.Table 1:Classification of the three LLM architectures by their(π,ϕ)(\pi,\phi)response, effective scaling exponent⟨β⟩\langle\beta\rangleoverN∈[50,150]N\!\in\![50,150], temperature-sensitivity⟨α⟩\langle\alpha\rangle, and
dominant slowdown mechanism. Arrows↘(T)\searrow(T)and↗(T)\nearrow(T)denote
decrease and increase with temperature.Modelπ\piϕ\phi⟨β⟩\langle\beta\rangle⟨α⟩\langle\alpha\rangleSlowdownllama3.1:8b↘(T)\searrow(T)↗(T)\nearrow(T)1.611.610.670.67repaintsmistral:7b≈1{\approx}\,1≈0{\approx}\,01.281.280.010.01(weak)phi3:14blow,↘(T)\searrow(T)≈0{\approx}\,01.591.590.430.43missed collapses

These three regimes are not imposed by hand butemergefrom the
interaction between the LLM architecture and the decoding temperature. The(π,ϕ)(\pi,\phi)decomposition acts as a bridge between the “black box” of LLM
inference and the well-understood physics of the NG.

Our work is complementary to but distinct from recent LLM-NG studies in
four specific ways. First, Ref.[1]and
Ref.[14]characterise themacroscopicoutcome (does consensus emerge, on which name, with
what bias) at a single fixed temperatureT=0.5T\!=\!0.5. We instead
decompose each microscopic interaction into the conditional rates(π,ϕ)(\pi,\phi)and trace how decoding temperature reshapes them. Second,
their analysis treats the LLM as an unresolved black box and infers
asymmetries from observed bias; we expose the underlying in-inventory and out-inventory channel structure that produces those asymmetries. Third, we
elevate decoding temperature from a fixed hyperparameter to a tunable
control parameter and quantify its effect through two complementary
scalar diagnostics,β​(T)\beta(T)andα​(N)\alpha(N). Fourth, we identify three
qualitatively distinct architecture-dependent regimes that produce
different consensus dynamics through different microscopic mechanisms.
Together, these moves convert LLM-NG from a phenomenological observation
that consensus emerges into a microscopically resolved
statistical-physics problem. Our results are also complementary to those
of Ref.[12], which established the
existence of architecture-dependent critical group sizes, and to those
of Ref.[11],
which decomposes conformity into competing effective forces; in both
cases, the(π,ϕ)(\pi,\phi)rates provide a temporally resolved diagnostic
that complements those purely macroscopic or aggregate-state
characterizations.

Two further studies complement our findings by varying different knobs of
the LLM-NG. Mehdizadeh and Hilbert[20]study a
networked Naming Game among LLM agents and show that agent memory depth
interacts with network topology in a sign-flipping way: longer memory slows
convergence in decentralized networks but accelerates the fragmented
settling of centralized ones. Their work fixes population size and varies
topology and memory, providing a natural counterpart to our
temperature-based control parameter; whether their effects persist under
finite-size scaling, and how they interact with the(π,ϕ)(\pi,\phi)decomposition, remains open. Separately, Zhanget al.[29]show that imposing lightweight schema
structure on the communication channel itself, rather than tuning a decoding
hyperparameter, can accelerate naming-game convergence by up to5.8×5.8\times. Together with our results, this points to a broader picture in
which convention formation in LLM populations can be steered through several
largely independent levers, decoding temperature, memory depth, network
topology, and communication schema, each acting on a different part of the
underlying(π,ϕ)(\pi,\phi)channel structure.

Several features are worth emphasising. First, temperature does not
universally slow consensus: formistral, increasingTTparadoxicallyimprovesconsistency by suppressing the low-TTconservative
transient; forphi3, highTTaccelerates convergence despite
loweringπ\pi, because it also reduces inventory diversity. The macroscopic
effect of decoding temperature is thusarchitecture-dependent,
mediated by the model-specific balance of the ordering and disordering
channels. This cautions against treating temperature as a universal “noise
knob” in multi-agent LLM systems.

Second, from a statistical-physics perspective, the relationship between
our(π,ϕ)(\pi,\phi)framework and the stochastic negotiation model of Baronchelliet al.[3]is more than an
analogy: their commitment probabilityβ\betais mathematically identical
to ourπ\pi, and their model corresponds exactly to theϕ=0\phi\!=\!0slice of the(π,ϕ)(\pi,\phi)plane. The essential conceptual difference is
in theoriginof the stochasticity. In their setup,β\betais
an external, hand-tuned scalar, chosen by the modeller and swept across[0,1][0,1]to trace out a phase diagram; the update rule fixesϕ=0\phi\!=\!0by construction. In ours, bothπ​(T)\pi(T)andϕ​(T)\phi(T)areemergent: they are properties of the LLM listener that we
measure a posteriori from multi-agent simulations, and their values,
theirTT-dependence, and even their qualitative shapes are set by the
architecture. This shift, from an external stochasticity parameter to
an emergent one, is what turns a mathematically clean toy model into a
diagnostic tool for real LLM populations. As a corollary, decoding
temperature moves both rates along architecture-dependent
trajectories in the two-dimensional(π,ϕ)(\pi,\phi)plane, whereas the
phase transition of Ref.[3]is
inherently a one-dimensional phenomenon along theϕ=0\phi\!=\!0edge,
of which phi3 is the empirical embodiment (Sec.V).
Notably, no fragmented phase was observed for any model at the explored
temperatures: strict11-consensus is always reached on the fully connected
graph, even for phi3 atT=2.0T\!=\!2.0, whereR≈−0.1R\!\approx\!-0.1lies nominally
below the critical line (Sec.VII). As discussed there,
this is consistent with a transition that sharpens only asN→∞N\to\infty, and with the group-size scenarios of Refs.[14,12],
where fragmentation emerges only above model-dependent population thresholds, beyond the sizes explored here.

Third, over the accessible size rangeN∈[50,150]N\!\in\![50,150]the effective
scaling exponentβ​(T)\beta(T)varies with temperature, reaching values above3/23/2forllamaat highTT. Discriminating a genuine change of
universality class from a slow crossover to the deterministic asymptote
would require substantially larger systems, a natural target for future
work.

More broadly, the(π,ϕ)(\pi,\phi)framework is not specific to the naming
game; any binary decision made by an LLM agent in the presence of a
ground-truth state can be decomposed analogously. Recent
statistical-physics analyses of LLM populations on
lattices[13]and in
conformity-driven opinion
dynamics[11]have
similarly relied on decompositions of the LLM response into competing
effective parameters (cooperative coupling vs. intrinsic bias; majority
force vs. individual preference). Asch-type conformity experiments on
multimodal LLM agents[5], where a binary
judgement with a known ground truth is flipped by social pressure,
provide a particularly close setting: the probability of yielding to
the group plays the same role as our false-positive rateϕ\phi. Our(π,ϕ)(\pi,\phi)rates fit naturally into this emerging framework as a
temporally-resolved diagnostic.

These findings carry direct implications for decentralized and
self-organizing LLM populations. As multi-agent LLM systems are
increasingly deployed without central coordination, for example in
federated learning, autonomous negotiation, distributed scientific
discovery, and collective decision making, the question of whether and
how fast they converge on shared conventions becomes operational. Our
results provide three quantitative answers. First, the(π,ϕ)(\pi,\phi)rates can be measured offline through a small set of probing prompts, so
that a system designer can determine which regime a given LLM occupies
before deploying it. Second, the rateα\alphatells the designer whether
decoding temperature is a useful design knob: formistral-like
architectures (α≈0\alpha\!\approx\!0) tuningTThas essentially no
effect on consensus speed, while forllama-like architectures
(α≈0.7\alpha\!\approx\!0.7)TTchangestct_{c}by a factor of about four
across the accessible range. Third, the temperature-dependence ofβ​(T)\beta(T)means that the effective collective dynamics of an LLM swarm
can be shaped through the joint choice of architecture and decoding
temperature, opening the door to physics-informed selection of LLMs for
specific multi-agent tasks. We view the identification of distinct
listener archetypes and their mapping onto macroscopic consensus dynamics
as a first step toward a statistical-physics taxonomy of LLM-agent
behaviour, of which the(π,ϕ,β,α)(\pi,\phi,\beta,\alpha)quadruple is a candidate
compact “datasheet” summarising an architecture’s collective properties,
much as critical exponents summarise a universality class.

Natural extensions include: heterogeneous temperatures (quenched
disorder), structured interaction topologies, multi-object naming, the
inclusion of committed
minorities[27,1], and
the exploration of model-native commitment signals (e.g. confidence
scores) as additional control parameters. The mean-field theory of Sec.VIIopens several
analytical directions: the analysis of the inventory-size hierarchy of AppendixA, which would capture the large-inventory effects that dominate the phi3 regime at lowTT; the structure of the possible fragmented states of the two-rate dynamics; the scaling of the convergence time with the distanceRRfrom the critical line; and the finite-NNrounding of the transition, which the phi3 high-TTregime is best positioned to probe.

## Appendix AMean-field equations for arbitrary vocabulary and
inventory-size closure

Let the active vocabulary containmmwords,Ωm={1,…,m}\Omega_{m}=\{1,\dots,m\}, and letnS​(t)n_{S}(t)be the fraction of agents
with inventoryS⊆ΩmS\subseteq\Omega_{m},S≠∅S\neq\emptyset, normalized as∑SnS=1\sum_{S}n_{S}=1. On the complete graph, in the limitN→∞N\to\infty,
the two-rate rule of Eq. (7) induces the exact
mean-field dynamicsn˙S=∑A,B≠∅nA​nB​1|A|​∑w∈A[qB​(w)​(2​δS,{w}−δS,A−δS,B)+(1−qB​(w))​(δS,B∪{w}−δS,B)],\dot{n}_{S}\;=\;\sum_{A,B\neq\emptyset}n_{A}n_{B}\,\frac{1}{|A|}\sum_{w\in A}\Bigl[\,q_{B}(w)\,\bigl(2\,\delta_{S,\{w\}}-\delta_{S,A}-\delta_{S,B}\bigr)\;+\;\bigl(1-q_{B}(w)\bigr)\bigl(\delta_{S,B\cup\{w\}}-\delta_{S,B}\bigr)\Bigr],(12)

whereAAandBBare the speaker and listener inventories, the
speaker choosesw∈Aw\in Auniformly,qB​(w)=πq_{B}(w)=\piifw∈Bw\in BandqB​(w)=ϕq_{B}(w)=\phiotherwise, andδS,X\delta_{S,X}is the Kronecker delta on inventories. The first bracket describes YES events, in which both agents collapse to{w}\{w\}; the second describes NO events, in which the speaker is unchanged and the listener learnswwif absent. Forϕ=0\phi=0,π=β\pi=\beta, Eq. (12) reduces to the stochastic NG of Ref.[3]; form=2m=2it closes on the three densitiesx=n{A}x=n_{\{A\}},y=n{B}y=n_{\{B\}},z=n{A,B}z=n_{\{A,B\}}and yields Eqs. (8)–(9). For generalmmthe hierarchy is(2m−1)(2^{m}{-}1)-dimensional and not solvable in closed form.

A tractable closure is obtained by assuming that all active words are
statistically equivalent, so thatnSn_{S}depends onSSonly through
its size:nS=ρk/(mk)n_{S}=\rho_{k}/\binom{m}{k}for|S|=k|S|=k, whereρk​(t)=∑|S|=knS​(t)\rho_{k}(t)=\sum_{|S|=k}n_{S}(t)is the inventory-size distribution.
This closure is the inventory analogue of the heterogeneous
(degree-based) mean-field approach to dynamical processes on complex
networks[6], with the inventory sizekkplaying the role of the node degree. Under this ansatz, a listener
with inventory sizekkcontains the transmitted word with probabilityhk=k/mh_{k}=k/m, answers YES with probabilityQk=π​hk+ϕ​(1−hk)=ϕ+(π−ϕ)​km,Q_{k}\;=\;\pi\,h_{k}+\phi\,(1-h_{k})\;=\;\phi+(\pi-\phi)\,\frac{k}{m}\,,(13)

and learns a new word (out-inventory NO event) with probabilityLk=(1−ϕ)​(1−km).L_{k}\;=\;(1-\phi)\Bigl(1-\frac{k}{m}\Bigr).(14)

WritingQ=∑kρk​Qk=ϕ+(π−ϕ)​μ/mQ=\sum_{k}\rho_{k}Q_{k}=\phi+(\pi-\phi)\,\mu/mfor the
listener-averaged YES probability, withμ=∑kk​ρk\mu=\sum_{k}k\rho_{k}the mean
inventory size, the closed equations readρ˙1\displaystyle\dot{\rho}_{1}=Q​(1−ρ1)+∑ℓ≥2ρℓ​Qℓ−ρ1​L1,\displaystyle=Q\,(1-\rho_{1})+\sum_{\ell\geq 2}\rho_{\ell}\,Q_{\ell}-\rho_{1}L_{1}\,,(15)ρ˙k\displaystyle\dot{\rho}_{k}=−ρk​(Q+Qk)+ρk−1​Lk−1−ρk​Lk,2≤k≤m.\displaystyle=-\rho_{k}\,(Q+Q_{k})+\rho_{k-1}L_{k-1}-\rho_{k}L_{k}\,,\qquad 2\leq k\leq m.(16)

In Eq. (16),−ρk​Q-\rho_{k}Qis the loss of size-kkspeakers
that collapse to singletons after a YES interaction,−ρk​Qk-\rho_{k}Q_{k}the
loss of size-kklisteners that collapse,ρk−1​Lk−1\rho_{k-1}L_{k-1}the gain
of size-kklisteners by learning one new word, and−ρk​Lk-\rho_{k}L_{k}the
corresponding loss towards sizek+1k{+}1.

At stationarity, Eq. (16) gives the recursionρk\displaystyle\rho_{k}=ρk−1​Lk−1Q+Qk+Lk,\displaystyle=\rho_{k-1}\,\frac{L_{k-1}}{Q+Q_{k}+L_{k}}\,,(17)i.e.ρk\displaystyle\text{i.e.}\quad\rho_{k}=ρ1​∏r=1k−1LrQ+Qr+1+Lr+1,\displaystyle=\rho_{1}\prod_{r=1}^{k-1}\frac{L_{r}}{Q+Q_{r+1}+L_{r+1}}\,,(18)

subject to the normalization∑kρk=1\sum_{k}\rho_{k}=1and the
self-consistency conditionQ=∑kρk​QkQ=\sum_{k}\rho_{k}Q_{k}. The
large-vocabulary mean-field problem thus reduces to a scalar
self-consistency equation forQQ, from which allρk\rho_{k}follow
recursively. This word-exchangeable ansatz describes the symmetric
active phase; the ordering instability that breaks it is governed by
the two-word sector, Eq. (10). The analysis of the
possible fragmented states of this hierarchy is left to future work.

## References
- [1]A. F. Ashery, L. M. Aiello, and A. Baronchelli(2025)Emergent social conventions and collective bias in LLM populations.Science Advances11(20),pp. eadu9368.External Links:Document,LinkCited by:§I,§I,§VIII,§VIII.
- [2]A. Baronchelli, L. Dall’Asta, A. Barrat, and V. Loreto(2006)Topology-induced coarsening in language games.Phys. Rev. E73,pp. 015102(R).Cited by:§I.
- [3]A. Baronchelli, L. Dall’Asta, A. Barrat, and V. Loreto(2007)Non-equilibrium phase transition in negotiation dynamics.Phys. Rev. E76,pp. 051102.Cited by:Appendix A,§I,§III,§III,§V,§VII,§VII,§VIII.
- [4]A. Baronchelli, M. Felici, V. Loreto, E. Caglioti, and L. Steels(2006)Sharp transition towards shared vocabularies in multi-agent systems.J. Stat. Mech.,pp. P06014.Cited by:§I,§II,§II,§III,§V.
- [5]A. Bellina, G. D. Marzo, and D. Garcia(2026)Conformity and social impact on ai agents.External Links:2601.05384,LinkCited by:§I,§VIII.
- [6]C. Castellano, S. Fortunato, and V. Loreto(2009)Statistical physics of social dynamics.Rev. Mod. Phys.81,pp. 591.Cited by:Appendix A,§I.
- [7]D. Centola and A. Baronchelli(2015-02)The spontaneous emergence of conventions: an experimental study of cultural evolution.Proceedings of the National Academy of Sciences112(7),pp. 1989–1994.External Links:ISSN 1091-6490,Link,DocumentCited by:§I.
- [8]Y.-S. Chuanget al.(2024)Simulating opinion dynamics with networks of LLM-based agents.External Links:2311.09618,LinkCited by:§I.
- [9]F. Cozzi, M. Pangallo, A. Perotti, A. Panisson, and C. Monti(2025)Learning individual behavior in agent-based models with graph diffusion networks.Note:Adv. Neural Inf. Process. Syst. (NeurIPS) 38External Links:2505.21426,LinkCited by:§I,§I.
- [10]L. Dall’Asta, A. Baronchelli, A. Barrat, and V. Loreto(2006)Nonequilibrium dynamics of language games on complex networks.Phys. Rev. E74,pp. 036105.Cited by:§I.
- [11]G. De Marzo, A. Bellina, C. Castellano, V. Priesemann, and D. Garcia(2026)Conformity generates collective misalignment in AI agents societies.External Links:2605.10721,LinkCited by:§I,§VIII,§VIII.
- [12]G. De Marzo, C. Castellano, and D. Garcia(2025)AI agents can coordinate beyond human scale.External Links:2409.02822,LinkCited by:§I,§VIII,§VIII.
- [13]C. De Nobili(2026)Collective alignment in LLM multi-agent systems: disentangling bias from cooperation via statistical physics.External Links:2605.10528,LinkCited by:§I,§II,§VI,§VIII.
- [14]A. Flint, L. M. Aiello, R. Pastor-Satorras, and A. Baronchelli(2025)Group size effects and collective misalignment in LLM multi-agent systems.External Links:2510.22422,LinkCited by:§I,§I,§VIII,§VIII.
- [15]T. Guoet al.(2024)Large language model based multi-agents: a survey of progress and challenges.External Links:2402.01680,LinkCited by:§I.
- [16]A. Holtzman, J. Buys, L. Du, M. Forbes, and Y. Choi(2020)The curious case of neural text degeneration.External Links:1904.09751,LinkCited by:§I.
- [17]S. Honget al.(2024)MetaGPT: meta programming for a multi-agent collaborative framework.External Links:2308.00352,LinkCited by:§I.
- [18]N. F. Johnson(2026)Increasing intelligence in AI agents can worsen collective outcomes.External Links:2603.12129,LinkCited by:§I,§I.
- [19]V. Loreto, A. Baronchelli, A. Mukherjee, A. Puglisi, and F. Tria(2011)Statistical physics of language dynamics.J. Stat. Mech.,pp. P04006.Cited by:§I,§II.
- [20]A. Mehdizadeh and M. Hilbert(2026)Exploring the topology and memory of consensus: how llm agents agree, fragment, or settle when forming conventions.External Links:2606.04197,LinkCited by:§VIII.
- [21]Ollama(2024)Ollama.External Links:LinkCited by:§IV.
- [22]J. Perez, G. Kovač, C. Léger, C. Colas, G. Molinaro, M. Derex, P.-Y. Oudeyer, and C. Moulin-Frier(2025)When LLMs play the telephone game: cultural attractors as conceptual tools to evaluate LLMs in multi-turn settings.Note:Proc. ICLR 2025External Links:2407.04503,LinkCited by:§I.
- [23]G. Piatti, Z. Hu, and K. Cho(2024)Cooperate or collapse: emergence of sustainable cooperation in a society of LLM agents.External Links:2404.16698,LinkCited by:§I.
- [24]C. Ruan, Y. Wang, Z. Shi, and J. Li(2025)Reaching agreement among reasoning LLM agents.External Links:2512.20184,LinkCited by:§I.
- [25]Z.-Y. Song, Q.-H. Cao, M.-X. Luo, and H. X. Zhu(2025)Detailed balance in large language model-driven agents.External Links:2512.10047,LinkCited by:§I.
- [26]L. Steels(1995)A self-organizing spatial vocabulary.Artificial Life2,pp. 319–332.External Links:ISSN 1064-5462,DocumentCited by:§I.
- [27]J. Xie, S. Sreenivasan, G. Korniss, W. Zhang, C. Lim, and B. K. Szymanski(2011-07)Social consensus through the influence of committed minorities.Phys. Rev. E84,pp. 011130.External Links:Document,LinkCited by:§VIII.
- [28]Y. Yang, R. Luo, M. Li, M. Zhou, W. Zhang, and J. Wang(2018)Mean field multi-agent reinforcement learning.InProc. ICML 2018, PMLR,Vol.80,pp. 5571.Cited by:§I.
- [29]R. Zhang and H. Woisetschläger(2025)SIGN: schema-induced games for naming.External Links:2510.21855,LinkCited by:§VIII.

## 


- 


Major funding support from
