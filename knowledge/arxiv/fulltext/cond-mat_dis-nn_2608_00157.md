# An asymptotically solvable model of many-body critical phases: mobility edges, scars, and inverted scars

**arXiv ID**: 2608.00157v1
**Authors**: Yi-Ting Tu, Zi-Jian Li, Sankar Das Sarma
**Published**: 2026-07-31
**Categories**: cond-mat.dis-nn, cond-mat.stat-mech, quant-ph
**Comments**: 40 pages, 9 figures
**HTML URL**: https://arxiv.org/html/2608.00157v1

## Abstract

While the prethermal regime of random many-body localized (MBL) systems is dominated by accidental many-body resonances, another class of resonances, originating from the underlying potential structure, is expected in large-size deterministic systems. It is known that this class of resonances can lead to single-particle critical phases that are neither localized nor extended, but the consequences in interacting systems remain unclear. In this work, we construct an asymptotically solvable model of a one-dimensional nearest-neighbor interacting spin chain, whose spatial structure induces a hierarchy of mirror-like many-body resonances. We derive two phases in the thermodynamic limit, characterized by the satisfaction and violation of a version of the weak eigenstate thermalization hypothesis (ETH). While these two phases are similar to the usual MBL and ETH phases, there exist rare eigenstates that behave like the opposite phase, interpreted as many-body scars and inverted scars. Surprisingly, the two phases can be separated by a finite-temperature phase transition, corresponding to a thermodynamic many-body mobility edge, which was often believed to be impossible. Our results also suggest the existence of delocalized rare regions in an otherwise-localized interacting Aubry-André model, even if there are no low-disorder regions like those in random systems. This challenges the common belief that there is no avalanche instability in quasiperiodic MBL.

## Full Text

An asymptotically solvable model of many-body critical phases: mobility edges, scars, and inverted scars

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2608.00157v1 [cond-mat.dis-nn] 31 Jul 2026

## An asymptotically solvable model of many-body critical phases: mobility edges, scars, and inverted scarsYi-Ting TuZi-Jian LiSankar Das SarmaCondensed Matter Theory Center and Joint Quantum Institute, Department of Physics, University of Maryland, College Park, Maryland 20742, USA

## Abstract

While the prethermal regime of random many-body localized (MBL) systems is dominated by accidental many-body resonances, another class of resonances, originating from the underlying potential structure, is expected in large-size deterministic systems.
It is known that this class of resonances can lead to single-particle critical phases that are neither localized nor extended, but the consequences in interacting systems remain unclear.
In this work, we construct an asymptotically solvable model of a one-dimensional nearest-neighbor interacting spin chain, whose spatial structure induces a hierarchy of mirror-like many-body resonances.
We derive two phases in the thermodynamic limit, characterized by the satisfaction and violation of a version of the weak eigenstate thermalization hypothesis (ETH).
While these two phases are similar to the usual MBL and ETH phases, there exist rare eigenstates that behave like the opposite phase, interpreted as many-body scars and inverted scars.
Surprisingly, the two phases can be separated by a finite-temperature phase transition, corresponding to a thermodynamic many-body mobility edge, which was often believed to be impossible.
Our results also suggest the existence of delocalized rare regions in an otherwise-localized interacting Aubry-André model, even if there are no low-disorder regions like those in random systems.
This challenges the common belief that there is no avalanche instability in quasiperiodic MBL.

## IIntroduction

Statistical mechanics is based on the expectation that a generic isolated system reaches thermal equilibrium by itself, washing away all microscopic information in the initial condition.
Yet it is proposed that for quantum systems with many-body localization (MBL)[1,2,3,4], such an assumption fails, with every bit of local information in the initial condition remaining local indefinitely[5,6].
This phenomenon is most widely studied in spin chains with strong random disorder[7,8,9,10,11,12,13], but it also occurs in deterministic systems with quasiperiodic modulation[14,15,16,17,18,19].

While the stability of MBL in the thermodynamic limit remains an unsolved problem, much of the recent work has instead focused on theprethermalregime of such systems[20,21,22,23,24,25,26,27], where the dynamics are dominated by rare many-body resonances[28,29,30,31].
More specifically, a system that behaves like MBL at short timescales delocalizes slowly at longer timescales due to accidental closeness in energy levels between different localized configurations, referred to asaccidentalresonances.

For systems with a deterministic long-range structure, such as quasiperiodic MBL, while accidental resonances may still exist, another type of resonance induced by the underlying structure should be amplified compared to random systems.
In the paradigmatic Aubry-André (AA) model, a recent numerical study[27]points to the many-body resonances due to the approximately mirror-symmetric structure of the potential, which may explain the numerical observation[26]of unexpected long-range resonances in such a system.
Many-body resonances in exact mirror-symmetric MBL systems have also been recently studied in Ref.[32], where an analytical theory of isolated resonances is constructed.
The possible proliferation of this class ofstructuralmany-body resonances, as well as the thermodynamic consequences, is the motivation for this paper.

At the single-particle level, the proliferation of structural resonances often leads to single-particlecriticalphases, which are neither localized nor extended, and are characterized by thesingular continuousspectrum in the mathematical literature[33,34,35,36,37,38,39].
There are various types of models where this happens for an entire region in the parameter space: models with exact repetition structure (e.g. the Fibonacci quasicrystal[40,41,42,43,44]), models with arbitrarily weak bonds (e.g. the extended Aubry-André-Harper model[45,46,47,48,49]), and models with a parent flat band (e.g. Ref.[50]).
There are also models where this happens for a set of rare parameter values in an otherwise localized phase, such as therare initial phasesfor the Aubry-André (AA) model[51,52]above the critical point[35,39], which is due to the proliferation of mirror-like resonances calledphase resonancesin the literature.
Most of these are rigorous mathematical results in infinite-size single-particle quasiperiodic systems with no interaction whatsoever.

The consequences of particle-particle interactions in such single-particle critical phases, however, are much less studied.
Rigorously proving results on such interacting many-body systems is extremely difficult. Existing results in the literature are mostly based on mean-field and related approximations[53,54,55]and small-size numerics[56,57,58].
In particular, Refs.[53,56,57]study the interacting Fibonacci model, with inconsistent findings on whether the system becomes MBL at large potential strengths. Refs.[55,58]propose that single-particle continuous spectra may lead to a many-body phase which is neither MBL nor thermal.
However, small-size numerics are expected to be dominated by finite-size effects and do not directly probe the thermodynamic consequences of structural resonances.
Roughly speaking, the proliferation of structural resonances is expected to be hierarchical in real space, and to see the resonances ofnnlevels in the hierarchy, we need a system size at least exponential innn, leading to a Hilbert space dimension at least doubly exponential innn.
Therefore, numerically observing the thermodynamic consequences is extremely difficult, if not impossible.

In this paper, we take a different approach that neither relies on numerical data nor dives into general mathematical proofs.
Instead, we construct an asymptotically solvable model to capture the essential behaviors of structural resonances.
Our model is a one-dimensional (1D) nearest-neighbor mixed-field Ising chain with a spatial structure that we call thehierarchical mirror structure(HMS), which induces a hierarchy of mirror-like many-body resonances.
This structure can either be thought of as a simplification of the quasiperiodic structure in the single-particle study in Ref.[35]or as a generalization of the single mirror-like many-body resonance in Ref.[32].
The many-body eigenstates of our model can be written down exactly up to a controllable error bound (which can be made arbitrarily small), and the corresponding energies can be controlled in a hierarchical way.
From the rigorous solution, we derive various properties of the model in the thermodynamic limit.
In particular, we show that there are two types of many-body critical phases that generalize the single-particle phase: themany-body critically extended(MBC-E) phase and themany-body critically localized(MBC-L) phase.
As the MBC-E (MBC-L) phase satisfies (violates) a form of the weak eigenstate thermalization hypothesis (ETH)[59,60,61,62], as well as some other diagnostics,
they are similar to the usual ETH (MBL) phase in some sense.

The main distinction of MBC-E and MBC-L from the usual ETH and MBL phases is the existence of rare eigenstates that behave like those from the opposite phase.
For the MBC-E phase, while most eigenstates have local observable expectation values being thermal, there is a set of eigenstates that are dense (exists near every energy density whenever it is well-defined) but rare (a vanishing fraction in the thermodynamic limit) which are non-thermal.
This can be regarded as a form of quantum many-body scars, which are, in general, isolated non-thermal energy eigenstates in an otherwise thermal system[63,64,65,66].
For the MBC-L phase, the opposite situation occurs: the existence of rare delocalized states in an otherwise MBL spectrum.
Such phenomena, in general, are mentioned less frequently in the literature but have been termedinverted many-body scarsby some papers[67,68,69,70].
Curiously, our work involves both concepts.

Surprisingly, the MBC-E and MBC-L phases are separated by a finite-temperature phase transition in some parameter regime, implying the existence of a thermodynamic many-body mobility edge (MBME) under a closed system interpretation, which was previously claimed to be impossible in the literature[71,72].
MBMEs are, in general, points on the energy spectrum that separate (typically) localized and extended many-body eigenstates.
While thermodynamic MBMEs have been analytically argued to exist in some models containing long-range interactions[73], their existence in short-range spin chains has been controversial.
In small-size numerics on quasiperiodic spin chains whose single-particle orbitals contain a single-particle mobility edge (SPME), one does observe an MBME[74,75,76,77,78,79].
However, there are arguments that such an MBME is only a finite-size effect[71,72,22].
In Ref.[72], it was argued that the finite-size MBME due to SPME will be pushed to the edge of the spectrum in the thermodynamic limit, and in Ref.[71], it was argued that the localized phase can be destroyed by delocalized bubbles due to local energy density fluctuations.
Our model therefore shows the limitations of these arguments for short-range hierarchical systems.
In particular, it circumvents the argument of Ref.[72]as it is not based on SPME (the single-particle subspaces are all critical), and it escapes that of Ref.[71]due to the lack of a well-defined “delocalized bubble” (as a delocalized state can locally look like a localized state but globally become ETH-like).
Another interesting fact is that the localized phase appears at high temperatures in our model, which is an example of theinverse freezingphenomenon described in Ref.[80], also related to mirror symmetry.

Our results may also have implications for rare-region effects in quasiperiodic systems.
In a random strongly disordered system, as long as the system size is large enough, there must be some rare regions that accidentally have low disorder and consequently locally thermalize.
It is proposed that such a region may expand indefinitely by thermalizing nearby spins, causing anavalanchethat destroys an otherwise MBL phase[81,82,83].
In a quasiperiodic system, however, there are no rare low-disorder regions.
Although it is shown that an avalanche may occur in the AA model in the presence of a planted thermal inclusion[84], intuitively it is unlikely that such a thermal region can exist naturally in the AA model.
However, our results show that there is a different type of rare region in the AA model, characterized by the local proliferation of structural many-body resonances (which is motivated by the proof of rare initial phases of the single-particle AA model[35]).
We discuss the possibility that the interplay between structural and accidental resonances can lead to the thermalization of such regions and, therefore, lead to avalanches.

The rest of this paper is organized as follows. In Sec.II, we present the idea behind our construction, beginning with the background on single-particle critical phases and the simplification of HMS.
We then provide the intuition on the effect of interactions as well as a summary of how such effects lead to the main properties of the MBC phases.
In Sec.III, we construct the single-particle version of our solvable model, which serves both as a warmup for the reader and as a conceptual precursor for our many-body model.
In particular, we prove that our simplified real-space structure does produce a single-particle critical phase in the mathematical sense.
In Sec.IV, we construct our main many-body solvable model for MBC phases, rigorously derive the asymptotic solution, and prove its key properties.
In Sec.V, we go beyond the solvable limit and discuss the possible many-body consequences of some previously studied single-particle models: the Fibonacci quasicrystal, the EAAH model, and the rare-region effect of the AA model (with some detailed analytical constructions provided in AppendicsAandB).
We conclude in Sec.VIwith a discussion on possible extensions to higher dimensional quasicrystals.

## IIIdea behind the construction

In this section, we present the idea behind our construction of the asymptotically solvable model.
We begin with some background on single-particle critical phases, from which we extract a simplified real-space structure that we call thehierarchical mirror structure(HMS).
Then we discuss the intuition behind the effects of particle-particle interaction in such a single-particle critical phase due to HMS.
Finally, we summarize how such effects lead to the key properties of the two MBC phases that we construct rigorously later in this paper.Figure 1:Illustration of the effects of interaction on a system with hierarchical mirror structure. (a) The transport of such a system can be thought of as hierarchical oscillations between distant regions with frequenciesω1≫ω2≫ω3≫⋯\omega_{1}\gg\omega_{2}\gg\omega_{3}\gg\cdots. (b) For the lowest level of the hierarchy, if a particle is near the mirror center, it isresonantbetween two mirrored sites (aaandbb). (c) Further away from the mirror center, the particle becomesnon-resonantdue to a small asymmetry between sitesa′a^{\prime}andb′b^{\prime}(red dashed line). (d) When the particles in (b) and (c) are both present, the non-resonant particle causes the resonant particle to becomefrozendue to interaction. (e) When two mirror-symmetric non-resonant particles are both present, the resonance of the (purple) particle isprotected.

## II.1Singular continuous spectra

Consider a finite single-particle system with Hilbert spaceℋ\mathcal{H}and HamiltonianHH. To study the time evolution of a local state vector|ψ⟩∈ℋ,⟨ψ|ψ⟩=1|\psi\rangle\in\mathcal{H},\langle\psi|\psi\rangle=1, one shall decompose the Hamiltonian into the energy eigenstate basis|E⟩|E\rangle. However, the same eigenstate decomposition cannot be directly carried to an infinite system, as one cannot always find a complete set of|E⟩∈ℋ|E\rangle\in\mathcal{H}that is normalizable, i.e., the equationH​|E⟩=E​|E⟩H|E\rangle=E|E\ranglemay not have solutions. Such a problem appears when we introduce the concept of the “scattering states” (which are non-normalizable) to describe some “eigenstates” in an infinite system.
Luckily, mathematicians have solved this issue by introducing the spectral measure to “decompose” the Hamiltonian,⟨ψ|e−i​H​t|ψ⟩=∫e−i​E​t​𝑑μ​(E)\langle\psi|e^{-iHt}|\psi\rangle=\int e^{-iEt}d\mu(E)(1)

Roughly speaking, the spectral measures describe the overlap between a state vector and an energy eigenstated​μ​(E)=f​(E)​d​E∼|⟨ψ|E⟩|2​d​Ed\mu(E)=f(E)dE\sim|\langle\psi|E\rangle|^{2}dE.

As we know, the single-particle eigenstate can be classified by whether it is localized or extended; the spectral measure can also be decomposed into such parts.
However, in general, there are three parts instead of two:μ=μp​p+μa​c+μs​c\mu=\mu_{pp}+\mu_{ac}+\mu_{sc}(2)

with subscripts standing forpure point,absolutely continuous, andsingular continuous, respectively. The pure point part corresponds to localized eigenstates (or bound states), where the energy distribution functionfp​p​(E)f_{pp}(E)is a weighted sum of delta peaks,fp​p​(E)=∑iwi​δ​(E−Ei)f_{pp}(E)=\sum_{i}w_{i}\delta(E-E_{i}). The absolutely continuous part corresponds to extended states (or scattering states), wherefa​c​(E)f_{ac}(E)is a regular function. The singular continuous part, perhaps less familiar, corresponds to the state where it is neither extended nor localized, wherefs​c​(E)f_{sc}(E)is distributed on a measure-zero uncountable set (such as the Cantor set) without concentration on any particular point (which excludes the pure point case), and zero elsewhere (which excludes the absolutely continuous case). Thus, the singular continuous spectrum usually has a fractal-like structure. One famous and physically relevant example of this case is Hofstadter’s butterfly (at irrational magnetic flux ratios)[85].

We first discuss the consequence of the singular continuous spectrum on transport. Roughly speaking, the distribution offs​cf_{sc}implies that the scales of the
energy gapsδ\deltacan be arbitrarily small and discontinuous. Specifically, if we sort the scales ofδ\deltain descending order, we get a discrete sequence{δn}\{\delta_{n}\}withδn→0\delta_{n}\rightarrow 0whenn→∞n\rightarrow\infty. (We requireδn≫δn+1\delta_{n}\gg\delta_{n+1}for theoretical convenience later on.)
Thus, the transport of a local state (particle) at a certain timescalettis only governed by a series of the energy eigenstates whose gaps are aroundδn∼1/t\delta_{n}\sim 1/t.
The particle can be considered “localized” since no other eigenstates are involved in the transport at a short time interval (which should be larger than the diffusion time) related tott. However, in a longer time interval, the particle becomes “extended” as other eigenstates with a smaller gapδn+1\delta_{n+1}get involved. This phenomenon is usually referred to as anomalous diffusion or transport[86,87,88].

In interacting many-body systems, the above classification no longer works.
Nevertheless, the localized and extended spectra roughly correspond to MBL and ETH phases in many-body systems.
Therefore, it is reasonable to guess that there is a many-body counterpart of the singular continuous spectrum as well, which is the main motivation of our paper.
Note that we would not try to give a precise and rigorous definition of the many-body singular continuous spectrum, but rather study the consequences of interactions.

## II.2Hierarchical mirror structures

The transport property we discussed in the previous section motivates the construction of a class of models with a singular continuous spectrum. In particular, one can consider the situation in which each energy gapδn\delta_{n}is related to a structural resonance; thus, the hierarchy ofδn\delta_{n}implies a hierarchy of the system structure. In this manuscript, we will consider the system structure as the mirror-symmetric type in 1D lattice systems, which we call thehierarchical mirror structure(HMS).

The HMS of a system refers to the case where the underlying system parameters (potential, hopping strength, and so on) themselves have HMS.
Specifically, our model is constructed with a series of self-similar subchains. Each of them is approximately mirror-symmetric with a different length scale. The longer subchains contain the shorter ones on one side of the mirror symmetry point. A cartoon picture of an HMS system and the dynamics of a local particle in it are shown in Fig.1(a) (where lattice sites are visualized as small potential wells).
Initially, a particle is placed at siteaa. Due to the (approximate) mirror symmetry point nearby, it will first oscillate back and forth between sitesaaandbbat timet∼ω1−1t\sim\omega_{1}^{-1}. Whent∼ω2−1t\sim\omega_{2}^{-1}, the previous particle configuration (oscillating between sitesaaandbb) will oscillate between the paira,ba,band its mirror paird,cd,c, and so on.

Note that the “approximate mirror symmetry” inside HMS we mentioned above is not a rigorous definition.
Even though there have been some concrete bounds in the mathematical literature[35,36]for some special cases, it is difficult to articulate general conditions/requirements of what counts as an approximate mirror symmetry.
Even “good enough to induce resonances” cannot be easily rewritten as a rigorous definition, especially when we consider the generalization to many-body systems.
Instead, our strategy for both single-particle (Sec.III) and many-body (Sec.IV) cases will be to show rigorously that what is definitely going to happen if we assume the approximate mirror structure is good enough in some particular limit.
Then, we will discuss in Sec.Vwhat we can say about some commonly studied critical models beyond this solvable limit (part of it involves a more general but non-solvable model of the freezing/protection condition presented in AppendixA).

Note that the HMS is not the only structure that can lead to singular continuous spectra.
For example, thefrequency resonancediscussed in Ref.[38](based on Refs.[33,34]) instead has hierarchies of Bloch-wave-like resonances over a large number of regions.
In most of the well-studied models, HMS may “mix” with other types of structures.
For example, in the Fibonacci quasicrystal, there are both mirror-like and other kinds of structural resonances (see Sec.V.1).
We believe that the results of this paper can be generalized to more complicated types of resonances, although the description is expected to be much more complex.

## II.3Effects of interaction

In this subsection, we provide an intuitive explanation of the role of interaction in a many-body system with HMS, based on the cartoon picture in Fig.1(a).

Supposing the separation of the transport timescale still holds in the many-body cases (which is realized by HMS in our cases), one can study the interaction effects on the whole system by studying each level of the hierarchy separately. Let us first study the lowest level, which refers to the subchain from sitea′a^{\prime}tob′b^{\prime}in Fig.1(a). In other words, we focus on the system behavior att1∼ω1−1t_{1}\sim\omega_{1}^{-1}and ignore the long-time behavior (t≫t1t\gg t_{1}) for now. Suppose that half of this subchain is disordered enough to have a finite-size MBL description, and the coupling is local in the middle of the chain; the many-body eigenstates of the whole subchain can therefore be theoretically constructed[32]. As long as the interaction is strong enough and we are not too close to the mirror center, the effect of interaction is tosynchronizethe resonances (oscillations) of the individual particles initially sitting at different potential wells (as depicted in Fig. 1 of Ref.[32]).

It is important to emphasize that the existence of an HMS forbids the mirror symmetry point from being exact in the whole system, since an exact symmetry point should, by definition, belong to the “highest” level of the hierarchy, and we cannot find a higher one, which makes the theory self-inconsistent as we require a hierarchy of mirror centers approaching the exact limit. Thus, the symmetry point can at most be locally exact.
At the lowest level, this explicit symmetry breaking is visualized in Fig.1(b)–(e) by the red dashed line on siteb′b^{\prime}, stressing thata′a^{\prime}andb′b^{\prime}do not have exactly the same potential.
Due to the energy detuning of the potential, the (gray) particle in Fig.1(b) becomes non-resonant betweena′a^{\prime}andb′b^{\prime}(but it may still oscillate in higher levels, such as between sitesa′a^{\prime}andd′d^{\prime}).
Note that this non-resonant behavior should be generic for all symmetry-breaking terms, as the tunneling amplitude between mirror sites becomes smaller as we move further away from the mirror center.

Now, interesting things happen when the resonant (purple) and the non-resonant (gray) particles are both present and interact with each other [Fig.1(d)]: they become collectivelyfrozen, where the purple particle cannot resonate as it does in the non-interacting scenario.
There are two ways to understand this phenomenon.
One is via the synchronization picture in Ref.[32], which states that when these two particles oscillate, they must oscillate together. Thus, once the potential for these particles on the other side becomes too detuned, the oscillation stops.
Another way is to consider the interaction between two particles as an effective potential. In this case, the purple particle also senses the asymmetry of the original potential (as an effective potential) transferred by the interaction from the gray particle, and becomes non-resonant.

One may bring back the resonance of the purple particle, however, if we put an additional particle at siteb′b^{\prime}[resulting in two gray particles in Fig.1(e)].
This can be easily understood through the effective potential picture: now the gray particles on both sides provide an effective potential to the purple particle, and it is largely mirror symmetric if we assume the detuning does not cause much distortion in the orbitals.
In this case, we say that the resonance of the purple particle isprotectedby the two gray particles.
In general, mirror-symmetric configurations protect resonances, so here the resonance between sitesaaandbbis protected by either having no particles ata′a^{\prime}andb′b^{\prime}[the trivial “protection” in Fig.1(b)] or having both particles ata′a^{\prime}andb′b^{\prime}[Fig.1(e)].

Note that the above picture is highly simplified and is only for the illustration of the core idea. The general conditions for freezing and protection are much more complicated and cannot be deduced or described from single-particle dynamics alone. For example, two resonant particles may become frozen when both are present, and the configuration in Fig.1(e) does not always lead to protected resonance.
We will discuss asymptotically solvable models in Secs.IIIandIVin which a version of this simplified picture is constructed to be exact.
A more realistic (but non-solvable) model of the freezing/protection condition in the still-simplified symmetric random MBL is presented in AppendixA.

## II.4The many-body critical phases

Now we are ready to summarize the consequences of the interaction on an infinite system with HMS.
The most natural question is whether the behavior of the infinite system is similar to an MBL phase, an ETH phase, or neither.

To answer the question, we analyze the resonance structure of the particles in the system. Recall from the last subsection that, in the presence of multiple particles with interactions, whether a resonant (purple) particle can participate in the oscillation of the first level (∼ω1\sim\omega_{1}) depends on whether the particle configuration of non-resonant sites (such asa′a^{\prime}andb′b^{\prime}in Fig.1) is mirror symmetric.
The same story can also be applied to all levels of the hierarchy.
For example, whether the purple particle can oscillate between the paira,ba,band the mirror paird,cd,cmay depend on whether the configurations of the sites at the left ofa′a^{\prime}and those at the right ofd′d^{\prime}are mirror symmetric.
And even if the particle is frozen at a lower level, it may still oscillate in some higher level, depending on the same mirror-symmetric condition of the configurations.

This mirror-symmetric condition is, in fact, connected to the thermodynamic property of the system. To see this, assume that we choose a random initial product state, and ask the question: what is the probabilitypnp_{n}that thennth level has a resonating region (in which the particles can resonate from the left half to the right half of the chain)?
The answer can be provided by counting the number of mirror-symmetric configurations inside the non-resonant region.
For example, for the cases in Fig.1(d) and1(e), the probability of finding a resonating region (where the purple particle can oscillate) isp1=2/4=1/2p_{1}=2/4=1/2, which corresponds to having none or both gray particles.

Next, we ask the question: how likely is it to findarbitrarilylong resonating regions whennngoes to infinity? Assume the resonating region at(n+1)(n+1)th level fully covers the whole region of thennth level, then it is equivalent to saying that if a particle is initially placed in a resonating region, how likely it is to be transported to an arbitrarily far distance from its origin in the thermodynamic limit, or how likely a particle can be involved in oscillations in infinitely many levels of the hierarchy.
As the answer to all these equivalent questions, the probability is (assuming the protection conditions can be treated as independent events){0,if​∑n=1∞pn​converges1,if​∑n=1∞pn​diverges\begin{cases}0,\text{ if }\sum_{n=1}^{\infty}p_{n}\text{ converges}\\
1,\text{ if }\sum_{n=1}^{\infty}p_{n}\text{ diverges}\end{cases}(3)

Such a result is almost a direct corollary, as∑n=1∞pn\sum_{n=1}^{\infty}p_{n}can be interpreted as the expectation value of the number of resonating levels. The first case, in which particles almost certainly do not participate in arbitrarily long-range resonances, is similar to the MBL case and will be considered amany-body critically localized(MBC-L) phase; the second case, in which particles almost certainly do, is similar to a many-body extended phase and will be considered amany-body critically extended(MBC-E) phase.
We will construct explicit examples of both phases in Sec.IV.

The MBC phases have significant differences from the conventional MBL and thermal phases. For a sitejjin a usual MBL chain, there is a length scaleLMBLL_{\rm MBL}determined by the primary support of the longest local integral of motion (LIOM) aroundjj.
The correlation between sitejjand another site on any given energy eigenstate must decay exponentially beyond[j−LMBL,j+LMBL][j-L_{\rm MBL},j+L_{\rm MBL}].
In MBC-L, however, for anyjjandLMBLL_{\rm MBL}, there is always a finite fraction (as a function decaying withLMBLL_{\rm MBL}) of energy eigenstates withO​(1)O(1)correlation between sitejjand some site outside[j−LMBL,j+LMBL][j-L_{\rm MBL},j+L_{\rm MBL}].
For MBC-E, although we will show that it satisfies a weak form of ETH in sectionIV(i.e., a vanishing fraction of eigenstates escape thermalization), the system behaves far from thermal. For example, there is a finite probability of having an arbitrarily long time towards thermalization. The details on the difference between the MBC and the conventional ETH/MBL phases will be discussed in Sec.IV.6.

The argument above can also be applied to the picture of energy eigenstates instead of the transport. In particular, the oscillation is replaced by the formation of (many-body) cat states, which are superpositions of the particles being in different positions.
From this point of view, we are able to extractpnp_{n}for a thermodynamic ensemble and study the finite-temperature behavior.
In Sec.IV, we will construct an explicit model that has a finite-temperature phase transition between MBC-L and MBC-E. In other words, we construct a thermodynamic many-body mobility edge (MBME).
Note that the argument of Ref.[71]against the existence of a thermodynamic MBME does not apply due to the lack of well-defined local energy densities, which can be related to the lack of the length scaleLMBLL_{\rm MBL}.

## IIIThe single-particle solvable model

In this and the next section, we construct concrete models with HMS that are asymptotically solvable and satisfy some of the intuitions introduced in Sec.IIin a mathematically rigorous manner.
We will construct the single-particle version in this section, which can be viewed as a simplification of the pictures in Fig.1(a)–(c).
By “asymptotically solvable”, we mean that every eigenstate can be labeled and written down explicitly, up to a controllable error term that can be made arbitrarily small, and that the energy spectrum has a clear hierarchical description where the hierarchical energy scales can be arbitrarily separated.

Although several models with a condition similar to HMS have been proven to be singular continuous based on the transfer matrix approach[35,36,37], a many-body generalization is extremely difficult.
As our goal is to construct a many-body generalization, we will instead use the techniques that can be easily generalized to interacting many-body systems. Specifically, we will use a strictly controlled first-order degenerate perturbation theory to allow all eigenstates to be written down explicitly with controllable errors.
We will first prove the singular continuity of the constructed single-particle model in this section and then generalize it to the many-body case in the next section.

Note that the goal of these asymptotically solvable constructions in this and the next sections is to demonstrate that our intuition, summarized in Sec.II, can indeed be rigorously true, at least in some extreme situations, and to derive their consequences.
What we need here is mathematical existence rather than numerical or experimental feasibility.
Therefore, in the construction below, we will mainly state that the conclusion works as long as some parameters are “small enough”, rather than providing concrete bounds on the scale of the parameters (which is often a much more difficult task).
“Small enough” here should be construed in the sense of mathematical abstraction, and its significance will be clearer in the details of our various proofs below.

## III.1Warmup: the all-resonant modelFigure 2:(a) Iterative construction of the single-particle all-resonant HMS model in Sec.III.1, modeling the purple particle in Fig.1(a). (b) The spectrum (black) and energy eigenstates (blue), corresponding stepwise with (a).

Before constructing the complete single-particle HMS model, we first consider the simplest case, in which a particle on every site is resonant in all levels.
This case can be thought of as modeling a subsystem of a general HMS chain and demonstrates the basic idea behind the iterative construction and singular continuity.

Let us again illustrate the idea using the cartoon picture in Fig.1(a). There is a set of sites (more accurately, localized approximate orbitals) to which the purple particle can tunnel (8 are visible in the figure, namelyaa,bb,cc,dd,ee,ff,gg,hh).
When the sites are more spatially separated (such asddandee), the weaker the tunneling amplitude is.
The ranking of the tunneling strength of the 7 “bonds” betweena,ba,b;b,cb,c;…;g,hg,his then marked as1,2,1,3,1,2,11,2,1,3,1,2,1, respectively, and so on, where thejjth term in the sequence is one plus the number of trailing zeros in the binary representation ofjj.
Focusing on the properties above, we consider a 1D chain consisting only of those sites, with the hopping parameters satisfying a similar ranking of tunneling strength.

This effective model can be constructed iteratively as shown in Fig.2(a) with the spectrum and eigenstates visualized stepwise [Fig.2(b)].
Specifically, we start with (i) a single site, (ii) make a mirrored copy to become two decoupled sites, and (iii) couple the two sites.
Now we reach the first level of the hierarchy, with eigenstates being even/odd superpositions of two sites with energy splittingΔ1\Delta_{1}.
To go to the second level, we again (iv) reflectively copy the chain and (v) couple them with a weaker bond.
Now the spectrum comprises two pairs, each with a splittingΔ2≪Δ1\Delta_{2}\ll\Delta_{1}(the figure is not to scale), and the eigenstates are approximately equal-weight superpositions of the four sites.
This procedure can be repeated again and again, and the spectrum will converge to a Cantor-like fractal which is of measure zero, and the eigenstates will still be approximately equal-weight superpositions of all sites.

To see the singular continuity of such a model, note that since the energy eigenstates are all approximately equal-weight superpositions, the energy distribution|⟨j|E⟩|2|\langle j|E\rangle|^{2}can be roughly treated as zero outside the Cantor set and constant inside.
As the weights are evenly divided, there cannot be discrete points where the weights accumulate, leading to the absence of a discrete part.
As the Cantor spectrum is of measure zero, there cannot be a continuous part in the distribution either.
This is the idea behind the proof we will present below for a more general model, which explicitly includes non-resonant sites.

The non-resonant sites will not influence the global spectrum properties until we study the many-body scenario. For completeness, in the full version of our solvable model below, we will include some non-resonant sites as well, although the conclusions remain unchanged if we ignore them in the single-particle case.

## III.2The solvable HMS HamiltonianFigure 3:Recursive construction of the solvable models, which works for both single-particle and many-body versions. At each step,Hn+1resH^{\text{res}}_{n+1}is formed by making a mirrored copy ofHnresH^{\text{res}}_{n}(theresonant region), adding a pair of new segmentsHnnr,Hnnr~H^{\text{nr}}_{n},\widetilde{H^{\text{nr}}_{n}}with small symmetry-breaking termsHnβH^{\beta}_{n}(thenon-resonant region), and finally coupling the four segments by bondsHnγ,Hnα​γ,Hnγ~H^{\gamma}_{n},H^{\alpha\gamma}_{n},\widetilde{H^{\gamma}_{n}}which are weaker and weaker asn→∞n\to\infty.

We consider a 1D tight-binding Hamiltonian on the infinite lattice with the formH∞=∑j=−∞∞tj​(|j⟩​⟨j+1|+|j+1⟩​⟨j|)+∑j=−∞∞Vj​|j⟩​⟨j|H_{\infty}=\sum_{j=-\infty}^{\infty}t_{j}(|j\rangle\langle j+1|+|j+1\rangle\langle j|)+\sum_{j=-\infty}^{\infty}V_{j}|j\rangle\langle j|(4)

where the hopping strengthtjt_{j}and on-site potentialVjV_{j}are constructed by iteratively connecting finite chains, with the steps described below.

## III.2.1Initialization of the building blocks

The chain is built by perturbing and connecting a sequence of initial subchains, which we call thebuilding blocksof the chain.
They are the resonant region of the first levelH1resH^{\text{res}}_{1}, the non-resonant regionsHnnr,n=1,2,…H^{\text{nr}}_{n},n=1,2,\ldotsfor all levels, as well as their mirror counterpartsH1res~\widetilde{H^{\text{res}}_{1}}andHnnr~\widetilde{H^{\text{nr}}_{n}}.
Their lengths are denoted byL1resL^{\text{res}}_{1}andLnnrL^{\text{nr}}_{n}, respectively, and are treated as input parameters of our construction.
For convenience, the non-tilde (tilde) ones will be used as the left (right) one in each mirror pair.

Our construction itself only requires that each of the initial building blocks has a non-degenerate energy spectrum, and that all of its eigenstates have nonzero amplitudes at the boundaries.
So almost any choice oftjt_{j}andVjV_{j}in the block would work.
However, to have a clean asymptotic solution of the model, we will make a specific choice regarding the form of the Hamiltonian.
Let each of these initial building blocksH1resH^{\text{res}}_{1}andHnnr,n=1,2,…H^{\text{nr}}_{n},n=1,2,\ldotstake the form ofH=∑j=1LVj​|j⟩​⟨j|+δ⋅∑j=1L−1tj​(|j⟩​⟨j+1|+|j+1⟩​⟨j|).H=\sum_{j=1}^{L}V_{j}|j\rangle\langle j|+\delta\cdot\sum_{j=1}^{L-1}t_{j}(|j\rangle\langle j+1|+|j+1\rangle\langle j|).(5)

whereLLis the corresponding size of the blocks.
We will construct the parametersVjV_{j}andtjt_{j}to be independent uniform random numbers in[−1,1][-1,1], andδ>0\delta>0to be a small number controlled by the error bound, which is elaborated below.
The random numbers are used to avoid accidental degeneracies and symmetries (and will be used to make the thermodynamic limit well-defined in the many-body generalization).
Note that each block is constructed with a different (independent) set of random numbers, and after this initialization step, all the parameters in the blocks are fixed, and when we later reflectively clone the block, each copy will inherit the same fixed choice of numbers.

Whileδ\deltaitself is to provide the non-zero amplitudes of the eigenstates at the boundary, its smallness is to make the eigenstates ofHHclose to the position eigenstates, which enables a clean analytical description of the final eigenstates up to a controllable error bound.
In order to bound the error from the position eigenstates, note that asδ→0\delta\to 0, the eigenstates|θj⟩|\theta_{j}\rangleofHHconverge to the position eigenstates|j⟩|j\rangle.
So for any choice of an error boundϵ0>0\epsilon_{0}>0, we can fix a small enoughδ\deltasuch that|⟨j|θj⟩|2>1−ϵ0.|\langle j|\theta_{j}\rangle|^{2}>1-\epsilon_{0}.(6)

Here we treatϵ0\epsilon_{0}as a block-independent error bound given as a parameter of our system, whileδ\deltais block-dependent and is expected to be smaller for larger blocks.

This approach of making the error bound uniform (regardless of the size of the blocks) can be treated as an idealization of localized systems so that they are strictly devoid of accidental resonances.
This is especially important when we generalize our construction to the many-body case, where controlling accidental resonances in general is still an open problem.
The rest of our construction will follow this philosophy of using artificial limits to avoid accidental resonances, so all the resonances will be of the mirror type.

The notation|θj⟩|\theta_{j}\ranglewill be used to denote the eigenstates of the initial building block that approximate|j⟩|j\rangle, which are distinguished from the eigenstates of other Hamiltonians denoted by|ψj⟩|\psi_{j}\rangle, sometimes with additional subscripts.
During the construction, those initial building blocks will be copied, mirrored, and sometimes perturbed, but every sitejjcan be traced back to exactly one of those initial building blocks, and hence the notation|θj⟩|\theta_{j}\ranglewill unambiguously denote its (possibly mirrored) eigenstate that approximates|j⟩|j\rangle.

## III.2.2The iteration step

Next, we construct the iteration step fromHnresH^{\text{res}}_{n}toHn+1resH^{\text{res}}_{n+1}(forn=1,2,…n=1,2,\ldots) as illustrated in Fig.3.
The site labels (a,b,c,da,b,c,d) and limiting parameters (α,β,γ\alpha,\beta,\gamma) will be treated as temporary variables within the iteration step. We will not put a subscriptnnfor brevity, although they are conceptually dependent on the level.

First, we make a mirror copy ofHnresH^{\text{res}}_{n}in the recursion to becomeHnres~\widetilde{H^{\text{res}}_{n}}.
Specifically,Hnres~\widetilde{H^{\text{res}}_{n}}is formed by replacing the position basis with the mirrored one|c⟩→|c~⟩|c\rangle\to|\widetilde{c}\rangle, …,|d⟩→|d~⟩|d\rangle\to|\widetilde{d}\rangleinHnresH^{\text{res}}_{n}.
The eigenstate labeling will also be mirrored.
That is, for anHnresH^{\text{res}}_{n}eigenstate|ψj⟩|\psi_{j}\rangle(the label will also be constructed recursively), the correspondingHnres~\widetilde{H^{\text{res}}_{n}}eigenstate with the same energy is denoted by|ψj~⟩|\psi_{\widetilde{j}}\rangle, wherej~=d~+d−j\widetilde{j}=\widetilde{d}+d-jis the mirrored site ofjj.

Next, we place the non-resonant building blockHnnrH^{\text{nr}}_{n}at the left ofHnresH^{\text{res}}_{n}by replacing|1⟩→|a⟩,…,|Lnnr⟩→|b⟩|1\rangle\to|a\rangle,\ldots,|L^{\text{nr}}_{n}\rangle\to|b\rangleand similarly for the eigenstate labels.
We similarly make a mirrored copy to becomeHnnr~\widetilde{H^{\text{nr}}_{n}}by|j⟩→|j~⟩|j\rangle\to|\widetilde{j}\rangle.
However, since we want it to be non-resonant, we add a symmetry-breaking perturbationHnβ=β⋅[∑j=b~a~−1tj′​(|j⟩​⟨j+1|+|j+1⟩​⟨j|)+∑j=b~a~Vj′​|j⟩​⟨j|]H^{\beta}_{n}=\beta\cdot\left[\sum_{j=\widetilde{b}}^{\widetilde{a}-1}t_{j}^{\prime}(|j\rangle\langle j+1|+|j+1\rangle\langle j|)+\sum_{j=\widetilde{b}}^{\widetilde{a}}V_{j}^{\prime}|j\rangle\langle j|\right](7)

so that the right non-resonant block becomesHnnr~+Hnβ\widetilde{H^{\text{nr}}_{n}}+H^{\beta}_{n}.
Heretj′t^{\prime}_{j}andVj′V^{\prime}_{j}are, again, independent uniform random numbers in[−1,1][-1,1], andβ>0\beta>0is a number small enough so that the eigenstates of the two blocks still look similar by mirroring (in particular, the eigenstates ofHnnr~+Hnβ\widetilde{H^{\text{nr}}_{n}}+H^{\beta}_{n}can be labeled consistently with those ofHnnrH^{\text{nr}}_{n}), but large enough so that the two blocks do not resonate after we couple all blocks together.
Note thatβ\betawill not be treated as part of the perturbation in the degenerate perturbation step below, but as a parameter generating the unperturbed eigenstates. We will discuss how to determineβ\betalater.

The four subchains are then coupled byHnγ\displaystyle H^{\gamma}_{n}=γ​(|b⟩​⟨c|+|c⟩​⟨b|),\displaystyle=\gamma\,(|b\rangle\langle c|+|c\rangle\langle b|),(8)Hnα​γ\displaystyle H^{\alpha\gamma}_{n}=α​γ​(|d⟩​⟨d~|+|d~⟩​⟨d|),\displaystyle=\alpha\gamma\,(|d\rangle\langle\widetilde{d}|+|\widetilde{d}\rangle\langle d|),Hnγ~\displaystyle\widetilde{H^{\gamma}_{n}}=γ​(|c~⟩​⟨b~|+|b~⟩​⟨c~|)\displaystyle=\gamma\,(|\widetilde{c}\rangle\langle\widetilde{b}|+|\widetilde{b}\rangle\langle\widetilde{c}|)

to form the final HamiltonianHn+1res=Hnnr+Hnγ+Hnres+Hnα​γ+Hnres~+Hnγ~+Hnnr~+Hnβ,H^{\text{res}}_{n+1}=H^{\text{nr}}_{n}+H^{\gamma}_{n}+H^{\text{res}}_{n}+H^{\alpha\gamma}_{n}+\widetilde{H^{\text{res}}_{n}}+\widetilde{H^{\gamma}_{n}}+\widetilde{H^{\text{nr}}_{n}}+H^{\beta}_{n},(9)

whereγ>0\gamma>0is a small number to make the degenerate perturbation theory as used below work within some error bound, and will be specified later.
The numberα>0\alpha>0is also intended to be small, and will be important in the many-body version of our model.
Here in the single-particle version, however, it does not play an important role, and we may just setα=1\alpha=1.

We treatγ\gammaas a perturbation whileα\alphaandβ\betaare not.
That is, the unperturbed and perturbation parts forHn+1resH^{\text{res}}_{n+1}areHn+1unp\displaystyle H^{\text{unp}}_{n+1}=Hnnr+Hnres+Hnres~+Hnnr~+Hnβ,\displaystyle=H^{\text{nr}}_{n}+H^{\text{res}}_{n}+\widetilde{H^{\text{res}}_{n}}+\widetilde{H^{\text{nr}}_{n}}+H^{\beta}_{n},(10)Hn+1pert\displaystyle H^{\text{pert}}_{n+1}=Hnγ+Hnα​γ+Hnγ~.\displaystyle=H^{\gamma}_{n}+H^{\alpha\gamma}_{n}+\widetilde{H^{\gamma}_{n}}.(11)

The unperturbed eigenstates|ψj⟩unp|\psi_{j}\rangle_{\text{unp}}ofHn+1unpH^{\text{unp}}_{n+1}are straightforwardly labeled by site indices betweenaaanda~\widetilde{a}. That is, if a sitej∈[a,b]j\in[a,b],[c,d][c,d],[d~,c~][\widetilde{d},\widetilde{c}], or[b~,a~][\widetilde{b},\widetilde{a}], then|ψj⟩unp|\psi_{j}\rangle_{\text{unp}}is the eigenstate ofHnnrH^{\text{nr}}_{n},HnresH^{\text{res}}_{n},Hnres~\widetilde{H^{\text{res}}_{n}}, orHnnr~+Hnβ\widetilde{H^{\text{nr}}_{n}}+H^{\beta}_{n}, respectively, with the corresponding label of that Hamiltonian defined above.
Now the energy levels ofHn+1unpH^{\text{unp}}_{n+1}are either nondegenerate (ifj∈[a,b]j\in[a,b]or[b~,a~][\widetilde{b},\widetilde{a}]) or twofold degenerate (ifj∈[c,c~]j\in[c,\widetilde{c}]) with subspace{|ψj⟩unp,|ψj~⟩unp}\{|\psi_{j}\rangle_{\text{unp}},|\psi_{\widetilde{j}}\rangle_{\text{unp}}\}and subspace Hamiltonian (assume without loss of generality thatj∈[c,d]j\in[c,d])γ​(0⟨ψj|d⟩unp⟨d~|ψj~⟩unp⟨ψj~|d~⟩unp⟨d|ψj⟩unp0),\gamma\,\begin{pmatrix}0&{}_{\text{unp}}\langle\psi_{j}|d\rangle\langle\widetilde{d}|\psi_{\widetilde{j}}\rangle_{\text{unp}}\\
{}_{\text{unp}}\langle\psi_{\widetilde{j}}|\widetilde{d}\rangle\langle d|\psi_{j}\rangle_{\text{unp}}&0\end{pmatrix},(12)

which leads to the new eigenstates being even/odd superpositions of them.
Note that here and below, we directly assume the normal situation with probability one. That is, the random numbers we start with do not produce accidental degeneracies and/or accidental symmetries that would make the matrix element vanish.

By makingγ\gammasmall enough, one can make first-order degenerate perturbation theory work as accurately as possible.
The perturbed eigenstates, which are also the eigenstates ofHn+1resH^{\text{res}}_{n+1}to be used for the next iteration, are then|ψj⟩n+1≈{|ψj⟩unpif​j∈[a,b]∪[b~,a~]12​(|ψj⟩unp+|ψj~⟩unp)if​j∈[c,d]12​(|ψj~⟩unp−|ψj⟩unp)if​j∈[d~,c~]|\psi_{j}\rangle_{n+1}\approx\begin{cases}|\psi_{j}\rangle_{\text{unp}}&\text{if }j\in[a,b]\cup[\widetilde{b},\widetilde{a}]\\
\frac{1}{\sqrt{2}}(|\psi_{j}\rangle_{\text{unp}}+|\psi_{\widetilde{j}}\rangle_{\text{unp}})&\text{if }j\in[c,d]\\
\frac{1}{\sqrt{2}}(|\psi_{\widetilde{j}}\rangle_{\text{unp}}-|\psi_{j}\rangle_{\text{unp}})&\text{if }j\in[\widetilde{d},\widetilde{c}]\end{cases}(13)

Here, the choice of which one is++and which one is−-is completely arbitrary, and our specific choice is solely for the convenience of labeling. We have added a subscriptn+1n+1so that we can later distinguish the eigenstates for different iteration steps.
For an example of such eigenstates and labeling, see Fig.4.Figure 4:Visualization of the eigenstates and their labeling ofHnresH^{\text{res}}_{n}withL1res=1L^{\text{res}}_{1}=1,Lnnr=nL^{\text{nr}}_{n}=n. The(i,j)(i,j)entry of the matrix is⟨j|ψi⟩n\langle j|\psi_{i}\rangle_{n}, assuming all error bounds are negligible. The figure is for illustrative purposes and not plotted from numerical data. The hierarchical structure is indicated at the bottom of the matrix, with magenta (gray) being (non-) resonance regions.

## III.2.3Error bounds

Now we are ready to determine the small numbersβ\betaandγ\gammafor the iteration step fromnnton+1n+1(note that they implicitly depend onnnas we mentioned).
From the discussion above, we have|ψj⟩lim:=limβ→0limγ→0|ψj⟩n+1={|ψj⟩nif​j∈[a,b]∪[b~,a~]12​(|ψj⟩n+|ψj~⟩n)if​j∈[c,d]12​(|ψj~⟩n−|ψj⟩n)if​j∈[d~,c~]|\psi_{j}\rangle_{\text{lim}}:=\lim_{\beta\to 0}\lim_{\gamma\to 0}|\psi_{j}\rangle_{n+1}\\
=\begin{cases}|\psi_{j}\rangle_{n}&\text{if }j\in[a,b]\cup[\widetilde{b},\widetilde{a}]\\
\frac{1}{\sqrt{2}}(|\psi_{j}\rangle_{n}+|\psi_{\widetilde{j}}\rangle_{n})&\text{if }j\in[c,d]\\
\frac{1}{\sqrt{2}}(|\psi_{\widetilde{j}}\rangle_{n}-|\psi_{j}\rangle_{n})&\text{if }j\in[\widetilde{d},\widetilde{c}]\end{cases}(14)

Here|ψj⟩n|\psi_{j}\rangle_{n}are the eigenstates of the Hamiltonian in the same limitHn+1lim:=limβ→0limγ→0Hn+1res=Hnnr+Hnres+Hnres~+Hnnr~H^{\text{lim}}_{n+1}:=\lim_{\beta\to 0}\lim_{\gamma\to 0}H^{\text{res}}_{n+1}=H^{\text{nr}}_{n}+H^{\text{res}}_{n}+\widetilde{H^{\text{res}}_{n}}+\widetilde{H^{\text{nr}}_{n}}(15)

with consistent labeling.
Note that this does not cause a notational inconsistency between|ψj⟩n|\psi_{j}\rangle_{n}and|ψj⟩n+1|\psi_{j}\rangle_{n+1}, as whenjjis in the block ofHnresH^{\text{res}}_{n}, it is indeed the|ψj⟩n|\psi_{j}\rangle_{n}from the previous iteration.
Also note that the order of limits reflects the conceptual requirements ofβ\betato be both “large enough” to suppress resonances and “small enough” to have similar eigenstates from its mirror block.

The above limits imply that as long asβ\betaandγ\gammaare chosen to be small enough, we can make|ψj⟩n+1|\psi_{j}\rangle_{n+1}as close to|ψj⟩lim|\psi_{j}\rangle_{\text{lim}}, andHn+1resH^{\text{res}}_{n+1}as close toHn+1limH^{\text{lim}}_{n+1}as we want.
For the technical requirements in all the subsequent derivations, we need an error bound parameter0<ϵn<10<\epsilon_{n}<1associated with this iteration, chosen to be smaller than half of any energy difference between subspaces inHn+1limH^{\text{lim}}_{n+1}.
Then we chooseβ\betaandγ\gammato make all of the following rigorous conditions true:2​Lnnr​|⟨θj|ψj⟩n+1|2<ϵn2L^{\text{nr}}_{n}|\langle\theta_{j}|\psi_{j}\rangle_{n+1}|^{2}<\epsilon_{n}(16)

if⟨θj|ψj⟩lim=0\langle\theta_{j}|\psi_{j}\rangle_{\text{lim}}=0, and||⟨θj|ψj⟩n+1|2−|⟨θj|ψj⟩lim|2|⟨θj|ψj⟩lim|2|<ϵn,\left|\frac{|\langle\theta_{j}|\psi_{j}\rangle_{n+1}|^{2}-|\langle\theta_{j}|\psi_{j}\rangle_{\text{lim}}|^{2}}{|\langle\theta_{j}|\psi_{j}\rangle_{\text{lim}}|^{2}}\right|<\epsilon_{n},(17)

if⟨θj|ψj⟩lim≠0\langle\theta_{j}|\psi_{j}\rangle_{\text{lim}}\neq 0, where|θj⟩≈|j⟩|\theta_{j}\rangle\approx|j\rangleis the eigenstate of (the copy of) the initial building block wherejjis in.
For energies:‖Hn+1res−Hn+1lim‖<ϵn,2​|Δ​Enmax|<ϵn\left\|H^{\text{res}}_{n+1}-H^{\text{lim}}_{n+1}\right\|<\epsilon_{n},\quad 2|\Delta E^{\text{max}}_{n}|<\epsilon_{n}(18)

where∥⋅∥\|\cdot\|denotes the operator norm,|Δ​Enmax||\Delta E^{\text{max}}_{n}|is the maximal energy shift between corresponding eigenstate indices fromHn+1limH^{\text{lim}}_{n+1}toHn+1resH^{\text{res}}_{n+1}.
Iterative applications of Eq. (14), along with the error bounds, lead to the asymptotic solution of our model: each eigenstate can be labeled and expressed exactly up to a controllable error bound (Fig.4), and the energy shifts at each level are also controlled.

To have a controllable accumulated error as we taken→∞n\to\infty, we will require2n​ϵn→02^{n}\epsilon_{n}\to 0, which implies various notions of convergence we need.
In addition, we require that the accumulated error fromnnto∞\infty, denoted byϵ≥n\epsilon_{\geq n}(which can be defined by∏n′=n∞(1+ϵn)−1\prod_{n^{\prime}=n}^{\infty}(1+\epsilon_{n})-1for what we need), satisfiesϵ≥n<2​ϵn\epsilon_{\geq n}<2\epsilon_{n}.
For physical intuition, we defineΔnmax(min)\Delta^{\text{max(min)}}_{n}for the maximum (minimum) subspace degeneracy lifting fromHn+1limH^{\text{lim}}_{n+1}toHn+1resH^{\text{res}}_{n+1}, and we will assume informally thatΔn+1max≪Δnmin\Delta^{\text{max}}_{n+1}\ll\Delta^{\text{min}}_{n}, so that we have a sequence of timescales{tn}\{t_{n}\}with1/Δnmin≪tn≪1/Δn+1max1/\Delta^{\text{min}}_{n}\ll t_{n}\ll 1/\Delta^{\text{max}}_{n+1}corresponding to the levels.
Some notion of this can be derived as a consequence of the strict error bounds, but we never use it in formal proofs.

As we already mentioned, the purpose of such error-bound requirements is only for existence proofs, and is expected to be far from optimal if we only want the same qualitative behaviors.

## III.2.4Infinite system

Having defined the initialization and the iteration step, we can now iterate to any finitenngiven the input parametersL1resL^{\text{res}}_{1},{Lnnr}\{L^{\text{nr}}_{n}\}, and the error bounds. However, defining the infinite system HamiltonianH∞H_{\infty}requires some special care.
Usually, when we think of taking a system to infinity, we are somehow “staying in the bulk of the system” and adding more and more faraway sites.
As our system is highly non-translationally invariant, for “staying in the bulk” to be well-defined, we need to see how to embedHnresH^{\text{res}}_{n}intoHn′resH^{\text{res}}_{n^{\prime}}for highern′n^{\prime}.
To do this, we note that everyHnresH^{\text{res}}_{n}appears twice insideHn+2resH^{\text{res}}_{n+2}(the left one directly, and the right one after two mirrored copying), and in general it appears2k2^{k}times inHn+k+1resH^{\text{res}}_{n+k+1}, so we have infinitly many ways to iterate to infinity while staying in the middle of the system with a consistent neighborhood.
We will treat the choice of this embedding as a random sequence and use it to defineH∞H_{\infty}, similar to how we use random numbers to initialize the potentials.

Equivalently, we may think of the ways of embedding as a slightly generalized version of the iteration step, in which, when we make a mirrored copy ofHnresH^{\text{res}}_{n}, we can either copy to the right or to the left. Now, all the ways of taking then→∞n\to\inftylimit can be described by an infinite binary sequence of “left” or “right,” corresponding to the direction of copying at thennth step.

The physical way to think about thisn→∞n\to\inftylimit is that we first prepare a finite chainHnresH^{\text{res}}_{n}and a particle concentrated near the center of the chain.
As time evolves, we can measure the particle to obtain some probability distribution, but there is a maximum timescaletnt_{n}above which finite-size effects become important.
In this case, if we want to probe longer timescales, we need to extend the boundary of the chain by embedding the originalHnresH^{\text{res}}_{n}into that of a highernn.
Thus, as long asnnis large enough, we can probe up to arbitrarily long timescalestnt_{n}with a finite system.

## III.3Progressive approximations on infinite latticeFigure 5:Progressive approximations of the solvable model on an infinite lattice, which works for both single-particle and many-body versions. The HamiltonianHn∞H^{\infty}_{n}at each step is a sum of decoupled segments. In the limit ofn→∞n\to\infty,Hn∞H^{\infty}_{n}converges to the final modelH∞H_{\infty}(in the sense of operator norm in the single-particle case, and term-wise in the many-body case).

The above construction definesH∞H_{\infty}as a limit of the sequenceHnresH^{\text{res}}_{n}, each on a finite chain with size growing innn.
However, to study the properties ofH∞H_{\infty}, it is better to make it a limit directly on the infinite lattice, so that the limit is taken within a fixed Hilbert space.
That is, we wantHn∞→H∞H^{\infty}_{n}\to H_{\infty}with eachHn∞H^{\infty}_{n}being defined already on the infinite lattice rather than in a finite system.
In this framework, we first make infinite copies of decoupled finite subchains, and then progressively couple these copies with the coupling Hamiltonians (α\alphaandγ\gammaterms at all levels), as well as the symmetry-breaking (β\beta) terms, to build thennth level.

First, we define the uncoupled HamiltonianH1∞H^{\infty}_{1}by placing all initial building blocks (H1resH^{\text{res}}_{1}andHnnrH^{\text{nr}}_{n}) in their proper positions, so that they can be progressively coupled (defined below) toH∞H_{\infty}for a fixed choice of embedding sequence.
The resulting Hamiltonian is a sum of decoupled chains, as shown in Fig.5.

Now for eachnn, going fromHn∞H^{\infty}_{n}toHn+1∞H^{\infty}_{n+1}is exactly by our original iteration step that mergesHnnrH^{\text{nr}}_{n},HnresH^{\text{res}}_{n},Hnres~\widetilde{H^{\text{res}}_{n}}, andHnnr~\widetilde{H^{\text{nr}}_{n}}intoHn+1resH^{\text{res}}_{n+1}.
But now it is happening for an infinite number of copies on the infinite lattice simultaneously.
Note that we have‖Hn+1∞−Hn∞‖<ϵn\|H^{\infty}_{n+1}-H^{\infty}_{n}\|<\epsilon_{n}by the error bound, so that we have the desired limit ofHn∞→H∞H^{\infty}_{n}\to H_{\infty}in the sense of the operator norm.

This construction also allows for a unified labeling of eigenstates for eachnn(although there are infinitely many choices of eigenbases, as the energy subspaces are highly degenerate, we will use the choice with the most local eigenstates).
Recall that we have defined the labeling of eigenstates for each segment of chains using the position index.
Now, for eachnn,Hn∞H^{\infty}_{n}is just a decoupled collection of them, so we have an unambiguous indexing system by shifting that of each block to its respective range of sites.
We denote the eigenstate ofHn∞H^{\infty}_{n}corresponding to sitejjas|ψj⟩n|\psi_{j}\rangle_{n}, which is localized and normalized as⟨ψj|ψj⟩n=1\langle\psi_{j}|\psi_{j}\rangle_{n}=1.
In particular, we have|ψj⟩1=|θj⟩|\psi_{j}\rangle_{1}=|\theta_{j}\rangle, and for alljjin the gray area in Fig.5, we have|ψj⟩n=|θj⟩|\psi_{j}\rangle_{n}=|\theta_{j}\rangleas well.
That is,|ψj⟩n|\psi_{j}\rangle_{n}only differs from|θj⟩|\theta_{j}\ranglein the purple areas forn=2n=2and above.
The energy eigenvalues corresponding to|ψj⟩n|\psi_{j}\rangle_{n}are denoted byEj,nE_{j,n}. However, unlikeHn∞H^{\infty}_{n}, the eigenstates|ψj⟩n|\psi_{j}\rangle_{n}do not converge whenn→∞n\to\inftyin the usual sense. For example, “|ψj⟩∞|\psi_{j}\rangle_{\infty}” may not be normalizable.
The quantity that corresponds to the eigenstates in a finite Hilbert space, and yet has a converging limit to infinity, is the spectral measure[89], which we will use to formulate our proof in the next subsection.

## III.4Singular continuity

Now we are ready to prove thatH∞H_{\infty}is purely singular continuous.
For some background on the rigorous treatment of spectral measure in mathematical physics, see, for example, Ref.[89].
We will fix the initial local state as|ψ⟩=|θi⟩|\psi\rangle=|\theta_{i}\ranglefor a generali∈ℤi\in\mathbb{Z}.
WhenHn∞→H∞H^{\infty}_{n}\to H_{\infty}, the spectral measureμn\mu_{n}(energy distribution) of|θi⟩|\theta_{i}\rangleforHn∞H^{\infty}_{n}weakly converges to the spectral measureμ\muforH∞H_{\infty}.
That is, for every bounded continuous functiong​(E)g(E)of energy, we havelimn→∞∫g​𝑑μn=∫g​𝑑μ\lim_{n\to\infty}\int g\,d\mu_{n}=\int g\,d\mu(19)

This allows us to discuss the singular continuity ofμ\muby limiting the properties ofμn\mu_{n}, which is much simpler to calculate.

Since the energy eigenstates ofHn∞H^{\infty}_{n}are purely discrete and labeled by the sites, the spectral measure of the local state|θi⟩|\theta_{i}\ranglecan be described by the weightswj,n=|⟨θi|ψj⟩n|2w_{j,n}=|\langle\theta_{i}|\psi_{j}\rangle_{n}|^{2}, with the corresponding energyEj,nE_{j,n}.
That is, the energy integral ofμn\mu_{n}becomes a discrete sum∫g​𝑑μn=∑jg​(Ej,n)​wj,n\int g\,d\mu_{n}=\sum_{j}g(E_{j,n})w_{j,n}(20)

Moreover, asHn∞H^{\infty}_{n}is a collection of decoupled chains, it is actually a finite sum.
Therefore, the problem of proving the spectral property ofH∞H_{\infty}reduces to the property of finite sums involvingwj,nw_{j,n}andEj,nE_{j,n}.

We proceed by first calculating how the weightswj,nw_{j,n}and energiesEj,nE_{j,n}evolve withnn, and then show the absence of atomic (pure point) and absolutely continuous parts inμ\mubased on the properties ofwj,nw_{j,n}andEj,nE_{j,n}to complete the proof.
The core idea of the evolution of the weights innnwill have a direct counterpart in the many-body setting, which leads to a weak ETH-like behavior.

## III.4.1Splitting of the weights on the orbit

Let us first calculate howwj,nw_{j,n}evolves withnnfor a fixedjj.
We will see that after somen0n_{0},wj,nw_{j,n}keeps being divided by halves.
Intuitively, as we increasenn, a particle initially at sitejjcan oscillate to more and more sites (named as theorbit) due to resonances, so the weight initially at sitejjis evenly divided among those sites in its orbit.

First note that there exists a finiten0n_{0}as an upper bound, below which|ψj⟩n=|θj⟩|\psi_{j}\rangle_{n}=|\theta_{j}\rangle, so that ifj≠ij\neq i,|ψj⟩n|\psi_{j}\rangle_{n}does not overlap with|θi⟩|\theta_{i}\rangle.
More specifically,n0n_{0}is the lowestnnsuch that sitesiiandjjappear in the sameHnresH^{\text{res}}_{n}orHnres~\widetilde{H^{\text{res}}_{n}}block inHn∞H^{\infty}_{n}.
So ifn<n0n<n_{0}, we havewj,n=δi,jw_{j,n}=\delta_{i,j}, and the value ofEj,nE_{j,n}is irrelevant forj≠ij\neq i.

Next, forn=n0n=n_{0}, due to the perturbative coupling that formsHnresH^{\text{res}}_{n},wj,nw_{j,n}first deviates fromδi,j\delta_{i,j}(again, we assume that the random numbers do not produce accidental symmetries).

Finally, forn>n0n>n_{0}, every time a pair ofHnresH^{\text{res}}_{n}andHnres~\widetilde{H^{\text{res}}_{n}}blocks are coupled, the weightwj,nw_{j,n}splits intowj,n+1w_{j,n+1}andwj~,n+1w_{\widetilde{j},n+1}evenly up to a relative error ofϵn\epsilon_{n}.
Therefore, when we go fromn0n_{0}tonn, there become2n−n02^{n-n_{0}}numbers ofj′j^{\prime}among whichwj′,nw_{j^{\prime},n}is evenly split, up to a relative error ofϵ≥n0\epsilon_{\geq n_{0}}.
Dynamically, this set ofj′j^{\prime}forms the orbit that a particle initially at thejjth eigenstate ofHn0∞H^{\infty}_{n_{0}}can oscillate to by the mirror operations of the levels fromn0n_{0}tonn.

## III.4.2Evolution of the energy tree

Next, we discuss how the energyEj,nE_{j,n}evolves corresponding to the evolution of thewj,nw_{j,n}for a fixedjj.
This evolution is basically captured in Fig.2, where the step-wise energy splitting forms a tree-like structure that we call anenergy tree, with layers corresponding tonnand branches at that layer corresponding to the energy level at thatnn.
Unlike the simple case of Fig.2, however, as we now include non-resonant sites for each level and define the Hamiltonian on an infinite lattice, there will be an infinite number of trees, which makes the description slightly more complicated.

Again, forn<n0n<n_{0}, we need to consider the cases ofi=ji=jandi≠ji\neq jseparately.
Fori≠ji\neq j, we havewj,n=0w_{j,n}=0whennnis below somen0n_{0}, so the correspondingEj,nE_{j,n}is not relevant; the energy line corresponding tojjfirst appears atn=n0n=n_{0}.
Fori=ji=j, we have instead thatwj,n=1w_{j,n}=1belown0n_{0}, so the line is relevant from the beginning. However, in this case,jjis always in the same non-resonant block for alln<n0n<n_{0}, soEj,nE_{j,n}is simply a constant there.
It first gets shifted (bounded byϵn0\epsilon_{n_{0}}) atn=n0n=n_{0}.

Now forn>n0n>n_{0}, every time a pair ofHnresH^{\text{res}}_{n}andHnres~\widetilde{H^{\text{res}}_{n}}blocks are coupled, and the weightwj,nw_{j,n}splits intowj,n+1w_{j,n+1}andwj~,n+1w_{\widetilde{j},n+1}, the energy lineEj,nE_{j,n}splits into two lines,Ej,n+1E_{j,n+1}andEj~,n+1E_{\widetilde{j},n+1}, whose differences from the original line is by the second inequality in Eq. (18)|Ej,n+1−Ej,n|,|Ej~,n+1−Ej,n|<12​ϵn|E_{j,n+1}-E_{j,n}|,|E_{\widetilde{j},n+1}-E_{j,n}|<\frac{1}{2}\epsilon_{n}(so that the splitting between them|Ej~,n+1−Ej,n+1|<ϵn|E_{\widetilde{j},n+1}-E_{j,n+1}|<\epsilon_{n}).
Note that these shifts never cause crossing between energy lines with positive weights, as all of those lines at stagennare the spectral lines inHn+1limH^{\text{lim}}_{n+1}, andϵn\epsilon_{n}is assumed to be smaller than half of any energy difference of its energy eigenspaces.

Now we can organize all of theEj,nE_{j,n}lines withwj,n≠0w_{j,n}\neq 0into a set of trees, where each branch at layernnis represented by a label(j,n)(j,n)and has child branches(j,n+1)(j,n+1)and(j~,n+1)(\widetilde{j},n+1)at the next layer (except whenj=ij=i, where it only has a single child branch(j,n+1)(j,n+1)below somen0n_{0}).
If a branch(j,n)(j,n)is not a child of another branch, we call it aroot line, so that the set of root lines is in one-to-one correspondence with the set of trees.
For a branch(j,n)(j,n), the energy rangesupEj′,n′−infEj′,n′\sup E_{j^{\prime},n^{\prime}}-\inf E_{j^{\prime},n^{\prime}}among all its children(j′,n′)(j^{\prime},n^{\prime})is called thewidthof the branch(j,n)(j,n).
The supremum of the total weightsupn′∑j′wn′,j′\sup_{n^{\prime}}\sum_{j^{\prime}}w_{n^{\prime},j^{\prime}}among its children(j′,n′)(j^{\prime},n^{\prime})is called thefinal weightof the branch(j,n)(j,n), which is bounded bywn,j​(1±ϵ≥n)w_{n,j}(1\pm\epsilon_{\geq n}).

Although there are an infinite number of trees, most of them will be irrelevant to us.
To see this, note that for a givenn1n_{1}, there is only a finite number of branches belown1n_{1}, and therefore only a finite number of root lines.
So the rest of the infinite number of trees all have root lines aboven1n_{1}.
Suppose thatn1n_{1}is large enough so thatiiis in a resonant block.
Then, for eachn>n1n>n_{1}, the root lines forming at this stage are due to the formation ofHnnrH^{\text{nr}}_{n}. Thus, the number of root lines atnnis2​Ln−1nr2L^{\text{nr}}_{n-1}.
By the error bound, we havewn,j<ϵn−1/2​Ln−1nrw_{n,j}<\epsilon_{n-1}/2L^{\text{nr}}_{n-1}for each root line(n,j)(n,j), and thus the total final weights of all of these root lines appearing atnnis bounded above byϵn−1​(1+ϵ≥n)\epsilon_{n-1}(1+\epsilon_{\geq n}).
By the convergence of accumulated errors fromn1n_{1}to infinity, we see that as long asn1n_{1}is large enough, we can make the final weights of all the root lines aboven1n_{1}arbitrarily small, and therefore we only need to consider the trees with root lines belown1n_{1}, a finite number of them.

We will see that the singular continuity ofH∞H_{\infty}is a direct consequence of the asymptotic properties of the width and final weights of the branches of these finite number of trees.

## III.4.3Absence of pure point spectrum

In this subsection, we prove thatμ\muhas no pure point part, that is, there is no delta peak in the energy distribution of|θi⟩|\theta_{i}\rangle.
The idea is that having a delta peak inμ\mumeans that the weights inμn\mu_{n}must be more and more concentrated around its final position asn→∞n\to\infty.
So if we show that a small energy window will eventually cover vanishing weight asn→∞n\to\infty, the desired result will follow.

TakegE0,δ​(E)g_{E_{0},\delta}(E)to be a family of continuous functions that is zero outside a small energy window[E0−δ,E0+δ][E_{0}-\delta,E_{0}+\delta]and has a single peak of size11atE0E_{0}. The condition thatμ\muhas no delta peak at energyE0E_{0}is equivalent to:limδ→0∫gE0,δ​𝑑μ=0\lim_{\delta\to 0}\int g_{E_{0},\delta}\,d\mu=0(21)

By approximatingμ\muusingμn\mu_{n}, it is equivalent tolimδ→0limn→∞∑jgE0,δ​(Ej,n)​wj,n=0\lim_{\delta\to 0}\lim_{n\to\infty}\sum_{j}g_{E_{0},\delta}(E_{j,n})w_{j,n}=0(22)

So, givenϵ>0\epsilon>0, we want to findδ0>0\delta_{0}>0such that0<δ≤δ00<\delta\leq\delta_{0}implieslimn→∞∑jgE0,δ​(Ej,n)​wj,n<ϵ\lim_{n\to\infty}\sum_{j}g_{E_{0},\delta}(E_{j,n})w_{j,n}<\epsilon(23)

Hence, we want to findδ0\delta_{0}such that as we evolvennto a large enough number, no matter how the new energy lines appear and split, the weights falling into the energy window[E0−δ,E0+δ][E_{0}-\delta,E_{0}+\delta]will stay belowϵ\epsilon.

To find thisδ0\delta_{0}, we will use the fact that most trees are negligible. First, choosen1n_{1}such that the total final weights of the trees with root lines beyondn1n_{1}are belowϵ/2\epsilon/2.
This way, we only need to show that a finite numbermmof trees (those with root lines belown1n_{1}) will not have a weight greater thanϵ/2\epsilon/2falling into[E0−δ,E0+δ][E_{0}-\delta,E_{0}+\delta].
This can be done by showing that each of themmtrees will contribute at mostϵ/2​m\epsilon/2mto such weight.

Now, for each tree with root line(j,n0)(j,n_{0}), asn≥n0n\geq n_{0}grows, its initial weightwj,n0w_{j,n_{0}}splits evenly into the orbit ofjjup to a relative error ofϵ≥n\epsilon_{\geq n}.
In order to avoid large weights from going into the energy window, we can pick annnsuch that each branch(j,n)(j,n)of this tree at thisnnhas a final weight<ϵ/4​m<\epsilon/4m, and requireδ0\delta_{0}to be smaller than the width of each of these(j,n)(j,n).
As different branches do not overlap with each other,[E0−δ,E0+δ][E_{0}-\delta,E_{0}+\delta]will at most overlap with two of these branches at the same time, and hence the weight falling into[E0−δ,E0+δ][E_{0}-\delta,E_{0}+\delta]due to this tree is below2⋅ϵ/4​m=ϵ/2​m2\cdot\epsilon/4m=\epsilon/2m.

With the choice ofδ0\delta_{0}that works for all of themmtrees, the total weight that can go into the energy window[E0−δ,E0+δ][E_{0}-\delta,E_{0}+\delta]is now bounded byϵ/2+m⋅ϵ/2​m=ϵ\epsilon/2+m\cdot\epsilon/2m=\epsilon, thus completing the proof thatμ\muhas no pure point part.

## III.4.4Absence of absolutely continuous spectrum

In this subsection, we prove thatμ\muhas no absolutely continuous part. That is, all the energy distribution is concentrated on a measure-zero set. Physically, this means that there is no “continuous” region on the energy distribution function.
The idea is that the energy being distributed on a measure-zero set inμ\mumeans that the weights inμn\mu_{n}must be mostly distributed in smaller and smaller regions asn→∞n\to\infty.
That is, most of the weights can be covered by a set of intervals whose total length is arbitrarily small.
As the weights are distributed in a tree-like structure, we can cover them by having one interval covering each branch.
By showing that the total width goes to zero asn→∞n\to\infty, the desired result will follow.

To write the condition thatμ\muhas no absolutely continuous part in terms of integrals, we need to construct a family of continuous functionsgδ​(E)g_{\delta}(E)that equals 1 except on a set with measureδ\delta, such thatlimδ→0∫gδ​𝑑μ=0\lim_{\delta\to 0}\int g_{\delta}\,d\mu=0(24)

Again, by approximatingμ\muusingμn\mu_{n}, it is equivalent tolimδ→0limn→∞∑jgδ​(Ej,n)​wj,n=0\lim_{\delta\to 0}\lim_{n\to\infty}\sum_{j}g_{\delta}(E_{j,n})w_{j,n}=0(25)

So we want to construct suchgδ​(E)g_{\delta}(E)so that for allϵ>0\epsilon>0, we can findδ0>0\delta_{0}>0such that0<δ≤δ00<\delta\leq\delta_{0}implieslimn→∞∑jgδ​(Ej,n)​wj,n<ϵ\lim_{n\to\infty}\sum_{j}g_{\delta}(E_{j,n})w_{j,n}<\epsilon(26)

It is enough to havegδ​(E)g_{\delta}(E)being associated with a finite set of disjoint intervals{[Ea−2​δa,Ea+2​δa]}\{[E_{a}-2\delta_{a},E_{a}+2\delta_{a}]\}indexed byaa, so thatgδ​(E)=1g_{\delta}(E)=1outside these intervals, andgδ​(E)=0g_{\delta}(E)=0inside any of[Ea−δa,Ea+δa][E_{a}-\delta_{a},E_{a}+\delta_{a}], and between 0 and 1 otherwise.
By a simple inequality argument, it is enough to show that
given anyϵ>0\epsilon>0, we can construct such{[Ea−δa,Ea+δa]}\{[E_{a}-\delta_{a},E_{a}+\delta_{a}]\}with2​∑aδa<ϵ2\sum_{a}\delta_{a}<\epsilonso that the sum of weightswj,nw_{j,n}withEj,nE_{j,n}outside any of these intervals is less thanϵ\epsilonfor all large enoughnn.

To construct such intervals, we again choosen1n_{1}such that the total final weights of the trees with root lines beyondn1n_{1}are belowϵ\epsilon.
So we only need to cover a finite numbermmof trees, those with root lines belown1n_{1}.
Our goal can be achieved by covering all branches of each tree (at largenn) using intervals with total lengths less thanϵ/m\epsilon/m.

Now, for each tree with root line(j,n0)(j,n_{0}), forn≥n0n\geq n_{0}, there are2n−n02^{n-n_{0}}branches at thisnn.
By the error bound, the width of each of the branches is bounded byϵ≥n<2​ϵn\epsilon_{\geq n}<2\epsilon_{n}.
Hence, the total width of all branches atnnis less than2n−n0+1​ϵn2^{n-n_{0}+1}\epsilon_{n}, which goes to zero asn→∞n\to\inftyby the assumption on the error bounds.
Now pick a large enoughnnso that2n−n0+1​ϵn<ϵ/m2^{n-n_{0}+1}\epsilon_{n}<\epsilon/m, and construct2n−n0+12^{n-n_{0}+1}intervals[Ea−δa,Ea+δa][E_{a}-\delta_{a},E_{a}+\delta_{a}], each covering the width of one branch.
Then we successfully cover this tree (at largenn) using a total length<ϵ/m<\epsilon/m.

Now, by merging the intervals from all of themmtrees (which may result in a smaller total length if they are not disjoint), we get the final set of intervals[Ea−δa,Ea+δa][E_{a}-\delta_{a},E_{a}+\delta_{a}]with a total length less thanm⋅ϵ/m=ϵm\cdot\epsilon/m=\epsilon.
For large enoughnn, the only source of weights that they fail to cover is from the trees with root lines beyondn1n_{1}, which is less thanϵ\epsilon, thus completing the proof.

## III.5Conclusion for the single-particle model

We have constructed the single-particle model of a 1D chain with HMS based on successive applications of first-order degenerate perturbation theory, in which all the energy eigenstates can be solved exactly up to controllable errors that can be made arbitrarily small, and the energy splittings are hierarchically separated.
From these simply expressed properties of the states and spectrum, and based on the idea of splitting weights as we evolve the indexnnof the level, we rigorously prove that the spectrum of the infinite system has neither a pure point part nor an absolutely continuous part.
That is, our single-particle model is purely singular continuous, which confirms that our solvable model is really a special case of what our physical intuition leads us to, and belongs to the broader class of models we intend to study, as explained in Sec.II.

The techniques we used in our construction and proofs have been deliberately chosen to be very general and not dependent on the particular properties of a 1D nearest-neighbor tight-binding model.
In addition to the many-body model we are going to construct, our construction above can also be generalized to single-particle models with long-range hopping and/or in higher dimensions.
On the other hand, it also comes with some drawbacks compared to more widely used techniques for 1D nearest-neighbor tight-binding models (such as the transfer matrix approach).
In particular, to avoid the issue of accidental resonance, all the controlled error bounds of the perturbation are required to be extremely small so that accidental resonance is simply impossible.
As we know, single-particle systems can withstand accidental resonances to some extent (as demonstrated by the localized nature of the Anderson and Aubry-André models), we expect our error bound to be far from optimal.
Although other techniques can avoid such issues in single-particle systems, there is no direct generalization to many-body cases.
In particular, whether many-body systems can withstand accidental resonances in general is still an open problem.
Therefore, to have a rigorous generalization of HMS to many-body systems, the only mathematical tool available to us will be this perturbative approach with controlled small error bounds.

## IVThe many-body solvable model

In this section, we will construct our many-body asymptotically solvable model with HMS, analogous to the single-particle construction in Sec.III, and derive its properties.
As we already mentioned in Sec.III, we have used the construction and proof technique that can be easily generalized to many-body systems.
Therefore, most of the construction steps will be carried over directly from those of Sec.III, as well as some of the key steps in proving its properties.
Recall that our single-particle model can be treated as a simplified model of a general chain with HMS, where we only consider a subset of localized approximate orbitals, each corresponding to one site in the modeled chain.
Intuitively, since a weak coupling between two consecutive (approximate) LIOMs can be treated as the two LIOMs being far away with all the LIOMs between them ignored, this many-body model can be similarly understood as modeling a subset of approximate LIOMs in a more general class of many-body HMS chains (see AppendixAfor a more detailed model on this).

Despite the similarities, there is a key ingredient in the many-body case that has no analogy in the single-particle case.
As we summarized in Sec.IIand visualized in Fig.1, the interaction between particles can produce non-trivial effects on the originally resonant particles, so that originally resonant particles can, in some cases, become non-resonant.
The exact condition of this freezing/protection behavior for a general HMS model turns out to be complicated (see AppendixA).
Even if we start with the already-simplified single-particle orbitals in Sec.III, it is still far from being asymptotically solvable.
Therefore, we will make a further simplification: we require that the resonant segments ([c,d][c,d]and[d~,c~][\widetilde{d},\widetilde{c}]in Fig.3) remain resonant (protected) if and only if configurations of the states in the non-resonant segments ([a,b][a,b]and[b~,a~][\widetilde{b},\widetilde{a}]) are mirror-symmetric.
We will show that this requirement can be achieved by a particular limit involving the small parametersα\alpha,β\beta, andγ\gammain the iteration step, while in the single-particle constructions we do not need to tuneα\alpha.

Another issue is what type of many-body chain we should use.
The conceptually most straightforward way is probably to add nearest-neighbor density-density interactions to the single-particle model we constructed in Sec.III.
However, the particle conservation of the resulting model leads to several technical difficulties.
First, when we couple segments of chains, the central bond can move at most one particle from one side to the other in first-order perturbation theory. Thus, to allow resonance between two halves with particle numbers differing by two or more, we need either higher-order perturbations or long-range hoppings.
While higher-order perturbations will make error bounding extremely difficult, adding long-range hopping contradicts our goal of studying a local and short-ranged spin chain.
Second, when we discuss the thermodynamic properties of the chain, particle conservation makes the eigenstate labeling and ensemble averaging much more complicated than in a system without additional conservation laws.
Although we expect that the resulting system will be qualitatively the same as what we will construct below (see AppendixAfor a non-solvable particle-conserving model), it would be unnecessarily complicated as a model to demonstrate our intuitive idea described in Sec.II.

Given the reasons above, we will use another notion of the many-body counterpart of a single-particle model, which has been used, for example, in Ref.[12], to generalize a proof of Anderson localization to MBL.
In this picture, going from a single-particle to a many-body system is simply a change in the operation of connecting two subsystems with Hilbert spaceℋA\mathcal{H}_{A}andℋB\mathcal{H}_{B}from a direct sumℋA⊕ℋB\mathcal{H}_{A}\oplus\mathcal{H}_{B}to a tensor productℋA⊗ℋB\mathcal{H}_{A}\otimes\mathcal{H}_{B}.
The many-body counterpart of a “position eigenstate” will then become a tensor product basis state of the sites, and that of “hopping” and “potential” should be treated as those on the Fock space lattice.
We will follow Ref.[12]to use the mixed-field Ising model, whose Fock space lattice is a hypercube, such that the transverse-field terms correspond to the hopping terms, and the longitudinal-field and Ising coupling terms correspond to the potential.
On the other hand, the HMS will always refer to the structure in real space, similar to how the disorder is still added in real space in Ref.[12].

We will show that this model has two thermodynamic phases: one is ETH-like and the other is MBL-like, and that they can be separated by a finite-temperature phase transition.
We will also discuss the difference between the usual ETH and MBL phases.

Note that although we will rigorously show some MBL-like behavior in our system, this has nothing to do with demonstrating the existence of a thermodynamic MBL phase in the usual sense.
Since we will artificially avoid accidental resonances by coupling finite segments of chains with weaker and weaker bonds, we are no longer in the same setting as the usual “MBL phase”, which typically requires some stability under generic local perturbations.
Indeed, if we allow tuning asymptotic weak bonds, then thermodynamic MBL certainly “exists” as an asymptotically decoupled chain without resonances, but it is not stable under generic perturbations.
One possible consequence of the interplay between the structural resonances caused by HMS and the accidental resonances when we are no longer in the rigorously error-bounded setting will be discussed in Sec.V.3.

## IV.1Construction

We will construct a mixed-field Ising model on an infinite 1D qubit lattice of the following formH∞=∑j=−∞∞Jj​σjz​σj+1z+∑j=−∞∞(hjz​σjz+hjx​σjx),H_{\infty}=\sum_{j=-\infty}^{\infty}J_{j}\sigma_{j}^{z}\sigma_{j+1}^{z}+\sum_{j=-\infty}^{\infty}\left(h_{j}^{z}\sigma_{j}^{z}+h_{j}^{x}\sigma_{j}^{x}\right),(27)

whereσjx,y,z\sigma_{j}^{x,y,z}are the Pauli matrices at sitejj.
This is the many-body counterpart of Eq. (4).
As we explained, we should viewJjJ_{j}andhjzh^{z}_{j}terms as the “potential” on the Fock space lattice, which is the counterpart of theVjV_{j}term on the real space lattice in (4).
Similarly, thehjxh^{x}_{j}term is the “hopping” on the Fock space lattice, the counterpart of thetjt_{j}term in (4).

## IV.1.1Initialization of the building blocks

As in the single-particle case of Sec.III.2.1, a set of initial building blocks is introduced for the iterative construction. They will be labeled in the exact same way (H1resH^{\text{res}}_{1},HnnrH^{\text{nr}}_{n}, etc) as in the single-particle case.
We require that each block has a non-degenerate many-body spectrum, and thatσLz\sigma^{z}_{L}of the blocks has all off-diagonal matrix elements⟨A|σLz|B⟩≠0\langle A|\sigma^{z}_{L}|B\rangle\neq 0(whereA≠BA\neq Bare energy eigenstate labels), and all diagonal matrix elements⟨A|σLz|A⟩\langle A|\sigma^{z}_{L}|A\rangleare distinct. The reason for these requirements will be illustrated in the next subsection. Again, our construction works for a general choice of Hamiltonians as the building blocks. However, for simplicity, we will make a specific choice for the Hamiltonians as in the single-particle case.
LetH=∑j=1L−1Jj​σjz​σj+1z+∑j=1L(hjz​σjz+δ⋅hjx​σjx),H=\sum_{j=1}^{L-1}J_{j}\sigma_{j}^{z}\sigma_{j+1}^{z}+\sum_{j=1}^{L}\left(h_{j}^{z}\sigma_{j}^{z}+\delta\cdot h_{j}^{x}\sigma_{j}^{x}\right),(28)

withHHstanding forH1resH^{\text{res}}_{1}orHnnr,n=1,2,…H^{\text{nr}}_{n},n=1,2,\ldots, andLLbeing the corresponding size (L1resL^{\text{res}}_{1}orLnnrL^{\text{nr}}_{n}).
The parametersJjJ_{j},hjzh^{z}_{j}, andhjxh^{x}_{j}are independent uniform random numbers in[−1,1][-1,1], andδ>0\delta>0is a small number that depends on the block (see Sec.III.2.1for the remark on randomness).

As in the single-particle case, to have a clean asymptotic solution of the energy eigenstates, we will requireδ\deltato be small enough so that the energy eigenstates of the initial blocks are close to theσz\sigma^{z}eigenstates.
First, we label the energy eigenstates of the blocks by bitstrings of lengthLL, and define the integrals of motionτ1,jz\tau^{z}_{1,j}of the blocks with eigenvalues being thejjth digit of the bitstring (with ‘0’ corresponding to eigenvalue+1+1and ‘1’ to−1-1).
Then the closeness condition can be expressed as|⟨τ1,jz⟩−⟨σjz⟩|<ϵ0\left|\langle\tau^{z}_{1,j}\rangle-\langle\sigma^{z}_{j}\rangle\right|<\epsilon_{0}(29)

for each eigenstate of the initial block, analogous to the single-particle case (6).
The correspondingσz\sigma^{z}andτ1z\tau^{z}_{1}eigenstates with bitstringAAare denoted by|A⟩0|A\rangle_{0}and|A⟩1|A\rangle_{1}, respectively.

When discussing the thermodynamic properties, we will need some additional “regularity” conditions.
We assumeLnnr→∞L^{\text{nr}}_{n}\to\inftyasn→∞n\to\infty, so that in a proper sequence of the limitδ→0\delta\rightarrow 0, the blocks for largennbecome a thermodynamic classical Ising chain, which has a well-defined entropy densitys​(e)s(e)as a function of the energy densityee, and has no long-range correlations.
We requireδ\delta(separately for each block) to be small enough that these properties still hold asn→∞n\to\infty.
When discussing approximate LIOMs, we will need an additional requirement that for any temperatureTT, the diagonal matrix element variance
ofτ1,jz\tau^{z}_{1,j}in the canonical ensemble has a uniform lower boundV​(T)>0V(T)>0, independent of the block and the site indexjj.
This can be achieved by the property of the classical Ising model with bounded field strengths. How these additional properties are used will be explained in the respective sections.

## IV.1.2The iteration step

Next, we construct the iteration step fromHnresH^{\text{res}}_{n}toHn+1resH^{\text{res}}_{n+1}, in parallel with the single-particle case in Sec.III.2.2, and again with the same method and symbols illustrated in Fig.3.

First, we make a mirror copy ofHnresH^{\text{res}}_{n}defined by the previous stage in the recursion to becomeHnres~\widetilde{H^{\text{res}}_{n}}.
Specifically,Hnres~\widetilde{H^{\text{res}}_{n}}is formed by reflecting all the site indices of each spin operator inHnresH^{\text{res}}_{n}.
Meanwhile, for each eigenstate|B⟩|B\rangleofHnresH^{\text{res}}_{n}(the labelBBis a bitstring that is constructed recursively), we label the corresponding eigenstate ofHnres~\widetilde{H^{\text{res}}_{n}}(with the same energy) as|B~⟩|\widetilde{B}\rangle, whereB~\widetilde{B}is the reversal of the bitstringBB.

Next, we place the non-resonant building blockHnnrH^{\text{nr}}_{n}(spanned over the sitesa,…,ba,\ldots,b) to the left ofHnresH^{\text{res}}_{n}.
We similarly make a mirrored copy to becomeHnnr~\widetilde{H^{\text{nr}}_{n}}.
To make it non-resonant, we add a symmetry-breaking perturbationHnβ=β⋅[∑j=b~a~−1Jj′​σjz​σj+1z+∑j=b~a~(hj′⁣z​σjz+hj′⁣x​σjx)]H^{\beta}_{n}=\beta\cdot\left[\sum_{j=\widetilde{b}}^{\widetilde{a}-1}J^{\prime}_{j}\sigma_{j}^{z}\sigma_{j+1}^{z}+\sum_{j=\widetilde{b}}^{\widetilde{a}}\left(h_{j}^{\prime z}\sigma_{j}^{z}+h_{j}^{\prime x}\sigma_{j}^{x}\right)\right](30)

with independent uniform random numbersJj′,hj′⁣x,zJ^{\prime}_{j},h^{\prime x,z}_{j}in[−1,1][-1,1]and a small numberβ>0\beta>0to be chosen below.
The eigenstates ofHnnr~+Hnβ\widetilde{H^{\text{nr}}_{n}}+H^{\beta}_{n}are labeled consistently by the reversal of the bitstrings that labelHnnrH^{\text{nr}}_{n}.

The four subchains are then coupled byHnγ=γ​σbz​σcz,Hnα​γ=α​γ​σdz​σd~z,Hnγ~=γ​σc~z​σb~zH^{\gamma}_{n}=\gamma\,\sigma^{z}_{b}\sigma^{z}_{c},\quad H^{\alpha\gamma}_{n}=\alpha\gamma\,\sigma^{z}_{d}\sigma^{z}_{\widetilde{d}},\quad\widetilde{H^{\gamma}_{n}}=\gamma\,\sigma^{z}_{\widetilde{c}}\sigma^{z}_{\widetilde{b}}(31)

to form the final HamiltonianHn+1res=Hnnr+Hnγ+Hnres+Hnα​γ+Hnres~+Hnγ~+Hnnr~+Hnβ,H^{\text{res}}_{n+1}=H^{\text{nr}}_{n}+H^{\gamma}_{n}+H^{\text{res}}_{n}+H^{\alpha\gamma}_{n}+\widetilde{H^{\text{res}}_{n}}+\widetilde{H^{\gamma}_{n}}+\widetilde{H^{\text{nr}}_{n}}+H^{\beta}_{n},(32)

with small numbersα,γ>0\alpha,\gamma>0to be chosen below.

Now, the main difference from the single-particle counterpart in Sec.III.2.2is that, in addition to controlling the non-resonances byβ\betaand the resonances byγ\gamma, we need to tune an additional parameterα\alphato allow a simple condition of freezing and protection.
By definition,α\alphacontrols the relative magnitude between two coupling HamiltoniansHnα​γH_{n}^{\alpha\gamma}andHnγH_{n}^{\gamma}.
The smallerα\alphais, the stronger the influence that the non-resonant regions have on the resonant regions.
Intuitively, by makingα\alphasmall enough, any non-symmetric configuration in the non-resonant pair will freeze the resonant pair.
But we also want to make it large enough so that when the non-resonant configuration is mirror-symmetric, the asymmetry of the interaction (between non-resonant and resonant regions in different halves) induced by theβ\betaterm is small enough to protect the resonance.
We will see that this can be achieved by choosingα≫β≫γ\alpha\gg\beta\gg\gamma.

We will again use first-order degenerate perturbation theory as in the single-particle case, with onlyγ\gammatreated as the perturbation parameter, whileα\alphaandβ\betaare fixed positive parameters during this perturbation step.
That is, the unperturbed and perturbation parts forHn+1resH^{\text{res}}_{n+1}areHn+1unp\displaystyle H^{\text{unp}}_{n+1}=Hnnr+Hnres+Hnres~+Hnnr~+Hnβ,\displaystyle=H^{\text{nr}}_{n}+H^{\text{res}}_{n}+\widetilde{H^{\text{res}}_{n}}+\widetilde{H^{\text{nr}}_{n}}+H^{\beta}_{n},(33)Hn+1pert\displaystyle H^{\text{pert}}_{n+1}=Hnγ+Hnα​γ+Hnγ~.\displaystyle=H^{\gamma}_{n}+H^{\alpha\gamma}_{n}+\widetilde{H^{\gamma}_{n}}.(34)

The unperturbed eigenstates are labeled by|A​B​C​D⟩unp|ABCD\rangle_{\text{unp}}, whereAA,BB,CC, andDDare bitstrings labeling the eigenstates ofHnnrH^{\text{nr}}_{n},HnresH^{\text{res}}_{n},Hnres~\widetilde{H^{\text{res}}_{n}}, andHnnr~+Hnβ\widetilde{H^{\text{nr}}_{n}}+H^{\beta}_{n}, respectively.
Notice that the degeneracies between|A​B​C​D⟩unp|ABCD\rangle_{\text{unp}}and|D~​B​C​A~⟩unp|\widetilde{D}BC\widetilde{A}\rangle_{\text{unp}}are split byβ\beta, and we restrictβ\betato be small enough to avoid accidental degeneracies.
Hence, the only degeneracies inHn+1unpH^{\text{unp}}_{n+1}are twofold:{|A​B​C​D⟩unp,|A​C~​B~​D⟩unp},B≠C~,\{|ABCD\rangle_{\text{unp}},|A\widetilde{C}\widetilde{B}D\rangle_{\text{unp}}\},\quad B\neq\widetilde{C},(35)

Using the perturbation theory, the diagonal term of the2×22\times 2effective Hamiltonian spanned by the unperturbed states isΔ:=⟨A​B​C​D|Hn+1pert|A​B​C​D⟩unp−⟨A​C~​B~​D|Hn+1pert|A​C~​B~​D⟩unp=γ​(⟨A|σbz|A⟩−⟨D|σb~z|D⟩)​(⟨B|σcz|B⟩−⟨C~|σcz|C~⟩)\Delta:=\langle ABCD|H^{\text{pert}}_{n+1}|ABCD\rangle_{\text{unp}}\\
-\langle A\widetilde{C}\widetilde{B}D|H^{\text{pert}}_{n+1}|A\widetilde{C}\widetilde{B}D\rangle_{\text{unp}}\\
=\gamma\big(\langle A|\sigma_{b}^{z}|A\rangle-\langle D|\sigma_{\widetilde{b}}^{z}|D\rangle\big)\big(\langle B|\sigma_{c}^{z}|B\rangle-\langle\widetilde{C}|\sigma_{c}^{z}|\widetilde{C}\rangle\big)(36)

and the off-diagonal term ist:=⟨A​B​C​D|Hn+1pert|A​C~​B~​D⟩unp=α​γ​|⟨B|σdz|C~⟩|2.t:=\langle ABCD|H^{\text{pert}}_{n+1}|A\widetilde{C}\widetilde{B}D\rangle_{\text{unp}}=\alpha\gamma\big|\langle B|\sigma_{d}^{z}|\widetilde{C}\rangle\big|^{2}.(37)

Note that the first factor inΔ\Deltahas the limit:limβ→0|⟨A|σbz|A⟩−⟨D|σb~z|D⟩|={0,if​A=D~,sA,D,if​A≠D~,\lim_{\beta\to 0}\big|\langle A|\sigma_{b}^{z}|A\rangle-\langle D|\sigma_{\widetilde{b}}^{z}|D\rangle\big|=\begin{cases}0,&\text{if }A=\widetilde{D},\\
s_{A,D},&\text{if }A\neq\widetilde{D},\end{cases}(38)

wheresA,D≠0s_{A,D}\neq 0is independent ofα\alphaandγ\gamma.
Hence, we can restrict the candidate range ofβ\betato0<β<β00<\beta<\beta_{0}(independent ofα\alphaandγ\gamma) so that whenA≠D~A\neq\widetilde{D}, any choice ofβ\betain this range will lead to,|⟨A|σbz|A⟩−⟨D|σb~z|D⟩|>12​sA,D\big|\langle A|\sigma_{b}^{z}|A\rangle-\langle D|\sigma_{\widetilde{b}}^{z}|D\rangle\big|>\frac{1}{2}s_{A,D}(39)

We also require that theβ\betain this range does not lead to additional accidental degeneracies that would invalidate the degenerate subspaces{|A​B​C​D⟩unp,|A​C~​B~​D⟩unp},B≠C~\{|ABCD\rangle_{\text{unp}},|A\widetilde{C}\widetilde{B}D\rangle_{\text{unp}}\},B\neq\widetilde{C}.
Note that this step is why we require that, in the initial building blocks, the diagonal matrix elements of the boundary term are all distinct.

Before determiningα\alpha,β\beta, andγ\gamma, we will first discuss why we will get the simple condition of freezing/protection, as long as the scales satisfy1≫α≫β≫γ1\gg\alpha\gg\beta\gg\gamma.
First, note that whenα\alphais small enough, we have (for any choice of0<β<β00<\beta<\beta_{0}andγ>0\gamma>0)|t|≪|Δ|​for all​A≠D~​and​B≠C~,|t|\ll|\Delta|\text{ for all }A\neq\widetilde{D}\text{ and }B\neq\widetilde{C},(40)

which suggests that asymmetric configurations of the non-resonant region freeze the resonant region (in first-order perturbation, which at this point may or may not be accurate).
Here we have used the property that⟨B|σcz|B⟩−⟨C~|σcz|C~⟩\langle B|\sigma_{c}^{z}|B\rangle-\langle\widetilde{C}|\sigma_{c}^{z}|\widetilde{C}\rangleis nonzero, which is expected due to the conditions on the initial building blocks as well as the random numbers in the subsequent steps.

Next, after fixing a small enoughα\alpha, we will fixβ\beta.
Due to the first line of (38), as long asβ\betais small enough, we have (for anyγ\gamma)|t|≫|Δ|​for all​A=D~​and​B≠C~,|t|\gg|\Delta|\text{ for all }A=\widetilde{D}\text{ and }B\neq\widetilde{C},(41)

which suggests that symmetric configurations of the non-resonant region protect the resonant region (again, in first-order perturbation).
Here we have used the property that⟨B|σdz|C~⟩\langle B|\sigma_{d}^{z}|\widetilde{C}\rangleis nonzero.
Again, this is due to the conditions on the initial building blocks as well as the random numbers in the subsequent steps.
In particular, this is the technical reason why we need a system without particle conservation.
If particles are conserved in the system, the resulting term⟨B|σd±|C~⟩\langle B|\sigma_{d}^{\pm}|\widetilde{C}\ranglewould only be nonzero ifBBandCChave the same number of particles (unless we add long-range hopping or go to higher-order perturbations).

Finally, after fixing a small enoughα\alphaand then a small enoughβ\betabased onα\alpha, we are ready to fixγ\gamma.
Until now,ttandΔ\Deltahave been just numbers, and we have not assumed anything about the accuracy of first-order perturbation theory; that is, whether the conditions (40) and (41) onttandΔ\Deltaactually lead to the expected freezing/protecting conditions.
However, as the degenerate perturbation theory is only controlled byγ\gamma, and the conditions (40) and (41) only depend on the ratio ofttandΔ\Delta, we can always choose a small enoughγ\gamma(after fixingα\alphaandβ\beta) to make the perturbation theory works as accurately as possible.
In particular, since we are in a finite-dimensional Hilbert space, we can always makeγ\gammasmall enough to avoid any energy level crossings that would induce accidental resonances.
The perturbed eigenstates|A​B​C​D⟩n+1|ABCD\rangle_{n+1}ofHn+1resH^{\text{res}}_{n+1}(to be used in the next iteration, along with their labels) are|A​B​C​D⟩n+1≈{|A​B​C​D⟩unp,if​A≠D~​or​B=C,|A​B​C​D⟩unp+|A​C~​B~​D⟩unp2,if​A=D~,B>C,|A​B​C​D⟩unp−|A​C~​B~​D⟩unp2,if​A=D~,B<C.|ABCD\rangle_{n+1}\\
\approx\begin{cases}|ABCD\rangle_{\text{unp}},&\text{if }A\neq\widetilde{D}\text{ or }B=C,\\
\frac{|ABCD\rangle_{\text{unp}}+|A\widetilde{C}\widetilde{B}D\rangle_{\text{unp}}}{\sqrt{2}},&\text{if }A=\widetilde{D},B>C,\\
\frac{|ABCD\rangle_{\text{unp}}-|A\widetilde{C}\widetilde{B}D\rangle_{\text{unp}}}{\sqrt{2}},&\text{if }A=\widetilde{D},B<C.\end{cases}(42)

The choice of±\pmin the eigenstates related to comparingBBandCCas binary numbers is arbitrary and is only a convenient way to label the new eigenstates as binary strings.
Note that in the case where the binary stringA​B​C​DABCDcontains only a single “1” and all other bits are “0” so that it can be labeled by a single sitejj, (42) reduces to the single-particle counterpart (13).

In the above construction, although the values ofα,β\alpha,\betaandγ\gammaare assumed to be so small that there are no many-body energy level crossings happening in the perturbation step, we expect that such a requirement is unnecessary in reality.
Specifically, if thermodynamic MBL is stable, we would expect perturbation theory to work in MBL systems even if there are energy level crossings, as the probability of energy level crossings causing accidental resonances decays exponentially.
Even if thermodynamic MBL is not stable, accidental resonances are still expected to be suppressed well before the strict scales we used (due to the very long thermalization timescale).
Our construction may also have some tolerance against accidental resonances.
However, the interplay between accidental resonances and structural (mirror) resonances is beyond the scope of this work.

## IV.1.3Error bounds

As in the single-particle case in Sec.III.2.3, the final choice of the small parametersα\alpha,β\beta, andγ\gamma(for the step fromnnton+1n+1) will be based on rigorously controlled error bounds.
From the discussion above, we have|A​B​C​D⟩lim:=limα→0limβ→0limγ→0|A​B​C​D⟩n+1={|A​B​C​D⟩n,if​A≠D~​or​B=C~,12​(|A​B​C​D⟩n+|A​C~​B~​D⟩n),if​A=D~,B>C~,12​(|A​B​C​D⟩n−|A​C~​B~​D⟩n),if​A=D~,B<C~.|ABCD\rangle_{\text{lim}}:=\lim_{\alpha\to 0}\lim_{\beta\to 0}\lim_{\gamma\to 0}|ABCD\rangle_{n+1}\\
=\begin{cases}|ABCD\rangle_{n},&\text{if }A\neq\widetilde{D}\text{ or }B=\widetilde{C},\\
\frac{1}{\sqrt{2}}\big(|ABCD\rangle_{n}+|A\widetilde{C}\widetilde{B}D\rangle_{n}\big),&\text{if }A=\widetilde{D},B>\widetilde{C},\\
\frac{1}{\sqrt{2}}\big(|ABCD\rangle_{n}-|A\widetilde{C}\widetilde{B}D\rangle_{n}\big),&\text{if }A=\widetilde{D},B<\widetilde{C}.\end{cases}(43)

Here|A​B​C​D⟩n|ABCD\rangle_{n}are the eigenstates of the Hamiltonian in the same limitHn+1lim:=limα→0limβ→0limγ→0Hn+1res=Hnnr+Hnres+Hnres~+Hnnr~H^{\text{lim}}_{n+1}:=\lim_{\alpha\to 0}\lim_{\beta\to 0}\lim_{\gamma\to 0}H^{\text{res}}_{n+1}=H^{\text{nr}}_{n}+H^{\text{res}}_{n}+\widetilde{H^{\text{res}}_{n}}+\widetilde{H^{\text{nr}}_{n}}(44)

with consistent labeling (as in the single-particle case, this does not cause a notational inconsistency with|A​B​C​D⟩n+1|ABCD\rangle_{n+1}).
For a better description of the “evolution” of the eigenstates from|A​B​C​D⟩n|ABCD\rangle_{n}to|A​B​C​D⟩n+1|ABCD\rangle_{n+1}, we define the unitariesUn​|A​B​C​D⟩n\displaystyle U_{n}|ABCD\rangle_{n}=|A​B​C​D⟩n+1,\displaystyle=|ABCD\rangle_{n+1},(45)Unlim​|A​B​C​D⟩n\displaystyle U_{n}^{\text{lim}}|ABCD\rangle_{n}=|A​B​C​D⟩lim\displaystyle=|ABCD\rangle_{\text{lim}}

so thatlimα→0limβ→0limγ→0Un=Unlim.\lim_{\alpha\to 0}\lim_{\beta\to 0}\lim_{\gamma\to 0}U_{n}=U_{n}^{\text{lim}}.(46)

Note that the order of limits in the equations above reflects the separation of scales1≫α≫β≫γ1\gg\alpha\gg\beta\gg\gamma.

For the technical requirements in all the subsequent derivations, we need an error bound parameter0<ϵn<10<\epsilon_{n}<1associated with this iteration.
We chooseα,β,γ\alpha,\beta,\gammato make all of the following rigorous conditions true:Un=Unlim+ℰn,‖ℰn‖<ϵn,U_{n}=U_{n}^{\text{lim}}+\mathcal{E}_{n},\quad\|\mathcal{E}_{n}\|<\epsilon_{n},(47)

and for energies:2​|Δ​Enmax|<ϵn2|\Delta E^{\text{max}}_{n}|<\epsilon_{n}(48)

where|Δ​Enmax||\Delta E^{\text{max}}_{n}|is the maximal energy shift between corresponding eigenstate index fromHn+1limH^{\text{lim}}_{n+1}toHn+1resH^{\text{res}}_{n+1}.
Iterative applications of Eq. (43), along with the error bounds, lead to the asymptotic solution of our model: each eigenstate can be labeled and expressed exactly up to a controllable error bound, and the energy shifts at each level are also controlled.

To have a controllable accumulated error as we taken→∞n\to\infty, we will require∑nϵn<∞\sum_{n}\epsilon_{n}<\infty. As in the single-particle case, we will assume informally that we have a sequence of timescales{tn}\{t_{n}\}with1/Δnmin≪tn≪1/Δn+1max1/\Delta^{\text{min}}_{n}\ll t_{n}\ll 1/\Delta^{\text{max}}_{n+1}corresponding to the levels.

## IV.1.4Infinite system

As in the single-particle case in Sec.III.2.4, the infinite systemH∞H_{\infty}is defined based on a sequence of embeddings ofHnresH^{\text{res}}_{n}intoHn′resH^{\text{res}}_{n^{\prime}}(n′>nn^{\prime}>n).

For the physical picture of the extension of chains according to the timescalestnt_{n}, we need to use local observables instead of local states in the single-particle case.
So the picture becomes that we are looking at Heisenberg evolution of a local observableO​(t)O(t), and that in a finite chainHnresH^{\text{res}}_{n}we can only probe its time evolution up totnt_{n}, beyond which we need to extend the chain through the embedding process.

An important consideration when taking the system to infinity in the many-body case is whether the thermodynamic limit exists. One of the conditions is that the boundary effects should be negligible compared to the bulk states.
In our system, at everynn, the bulk states in the resonant regions are always influenced by the boundary states of the non-resonant blocks.
This is contrary to the conventional thermodynamic limit where the boundary effects are ignorable, and the size of the boundaries is much smaller than the bulk.
Although this is the case, we can still characterize the properties of the bulk states using local observables; i.e., the local observables have a well-defined limit in an arbitrarily large system when sufficiently far from the boundary.
The argument is similar to that in Sec.III.2.4, where to obtain the limit of a local observable, one should always study it below a timescaletnt_{n}at eachnn, and then taken→∞n\rightarrow\infty.
Related problems of the thermodynamic limit are discussed in different models[90,91,92]

## IV.2Progressive approximations on infinite latticeFigure 6:(a) The unitary circuit that progressively approximates the eigenstates of the many-body solvable model (visualized withL1res=1,Lnnr=nL^{\text{res}}_{1}=1,L^{\text{nr}}_{n}=n). Thennth layer takes theHn∞H^{\infty}_{n}eigenstate|S⟩n|S\rangle_{n}to the correspondingHn+1∞H^{\infty}_{n+1}eigenstate|S⟩n+1|S\rangle_{n+1}. (b) The approximate action of the gates [see Eq. (49)]. A gate withnnwritten on the right denotes its mirror.

The final infinite HamiltonianH∞H_{\infty}can also be approximated by a series of infinite HamiltoniansHn∞H^{\infty}_{n}consisting of decoupled blocks, in the exact same way as described in Sec.III.3and depicted in Fig.5, with the difference that now we can no longer use operator norm to describe the limit “Hn∞→H∞H^{\infty}_{n}\to H_{\infty}” due to the divergence of the many-body operator norm.

Similar to the single-particle model, the energy eigenstates ofHn∞H^{\infty}_{n}can be described by the tensor product of the eigenstates of each block (although the energy subspaces are highly degenerate, the most “local” bases are the tensor-product ones).
As these eigenstates of each block are labeled by a bitstring, we can concatenate all of them to form a bi-infinite bitstringSS.
The eigenstates ofHn∞H^{\infty}_{n}are then denoted by|S⟩n|S\rangle_{n}.
The notation of bitstringA​B​C​DABCDwe used before to label the eigenstates now becomes a substring ofSS.
Note that an infinite tensor product of Hilbert spaces is ill-defined in general, so the notation|S⟩n|S\rangle_{n}should be regarded as a formal tensor product of the blocks, and we do not try to define its limit “|S⟩∞|S\rangle_{\infty}” that would be the eigenstates ofH∞H_{\infty}.

A convenient way to describe these eigenstates is to use a unitary circuit consisting ofUnU_{n}and its mirrorUn~\widetilde{U_{n}}on thennth layer, shown in Fig.6.
Recall that, by the definition (45) ofUnU_{n}and the error bounds (47), we haveUn​|A​B​C​D⟩n=|A​B​C​D⟩n+1={|A​B​C​D⟩n,if​A≠D~​or​B=C~,12​(|A​B​C​D⟩n+|A​C~​B~​D⟩n),if​A=D~,B>C~,12​(|A​B​C​D⟩n−|A​C~​B~​D⟩n),if​A=D~,B<C~.+ℰn,‖ℰn‖<ϵnU_{n}|ABCD\rangle_{n}=|ABCD\rangle_{n+1}\\
=\begin{cases}|ABCD\rangle_{n},&\text{if }A\neq\widetilde{D}\text{ or }B=\widetilde{C},\\
\frac{1}{\sqrt{2}}\big(|ABCD\rangle_{n}+|A\widetilde{C}\widetilde{B}D\rangle_{n}\big),&\text{if }A=\widetilde{D},B>\widetilde{C},\\
\frac{1}{\sqrt{2}}\big(|ABCD\rangle_{n}-|A\widetilde{C}\widetilde{B}D\rangle_{n}\big),&\text{if }A=\widetilde{D},B<\widetilde{C}.\end{cases}\\
+\mathcal{E}_{n},\quad\|\mathcal{E}_{n}\|<\epsilon_{n}(49)

Now defining thennth layer of the circuit [as shown in Fig.6(a)] asUn∞U^{\infty}_{n}, we then haveUn∞​|S⟩n=|S⟩n+1U^{\infty}_{n}|S\rangle_{n}=|S\rangle_{n+1}(50)

This circuit is viewed as a progressive approximation of the eigenstate ofH∞H_{\infty}.
One can viewHn∞H^{\infty}_{n}as an approximation ofH∞H_{\infty}up to a timescaletnt_{n}.
If we start with the eigenstates|S⟩1|S\rangle_{1}of the initial building blocks, evolving the circuit from layer11tonnproduces|S⟩n|S\rangle_{n}, which are approximated eigenstates ofH∞H_{\infty}up to a timescaletnt_{n}.
Thus, taking then→∞n\to\inftylimit corresponds to taking the infinite time limit.
As we will shortly see, this leads to a unique limit of local observable expectations.

Analogous to how the Pauli operators act on theσz\sigma^{z}bitstring eigenstates, we can similarly define the “progressively dressed” Pauli operatorsτn,jx,y,z\tau^{x,y,z}_{n,j}, so that they act on thejjth component of the|S⟩n|S\rangle_{n}eigenstate in the exact same way asσjx,y,z\sigma^{x,y,z}_{j}on theσz\sigma^{z}eigenstate labeled by the bitstringSS.
Note that we haveUn∞​τnx,y,z​Un∞⁣†=τn+1x,y,z.U^{\infty}_{n}\tau^{x,y,z}_{n}U^{\infty\dagger}_{n}=\tau^{x,y,z}_{n+1}.(51)

We will interpret{τn,jz}j=−∞∞\{\tau^{z}_{n,j}\}_{j=-\infty}^{\infty}as a complete set of LIOMs ofHn∞H^{\infty}_{n}, and approximate LIOMs ofH∞H_{\infty}within the timescaletnt_{n}.
In the limitn→∞n\rightarrow\infty,τn,jz\tau^{z}_{n,j}is no longer a (quasi-)local operator, analogous to a local state that may participate in an arbitrarily long resonance in the single-particle case.
However, different from the single-particle case, there remain possibilities that{τn0,jz}j=−∞∞\{\tau^{z}_{n_{0},j}\}_{j=-\infty}^{\infty}for a fixedn0n_{0}is a good set of approximate LIOMs ofH∞H_{\infty}up to an arbitrarily long timescale, which corresponds to the situation that the majority of energy eigenstates are approximately LIOM eigenstates, while only a vanishing fraction of energy eigenstates are not.
Such a case is referred to as the MBC-L phase, while the opposite scenario will be considered the MBC-E phase.
We will later see whether we have the MBC-L or MBC-E phase, which depends on the system parameters and temperature.

## IV.3Canonical ensemble

We will analyze the system in an energy (or temperature)-dependent way; thus, we need to look at some thermodynamic ensemble.
As eachHn∞H^{\infty}_{n}consists of decoupled blocks, it is natural to use the canonical ensemble, which has the property that the ensemble density matrix of a decoupled set of systems is the tensor product of the individual systems.
That is, the canonical ensemble ofHn∞H^{\infty}_{n}at a temperatureT≠0T\neq 0can be written asρn∞=⨂H:blocke−H/TTr⁡e−H/T\rho^{\infty}_{n}=\bigotimes_{H:\text{ block}}\frac{e^{-H/T}}{\Tr e^{-H/T}}(52)

whereHHruns over the blocks (HnresH^{\text{res}}_{n}andHn′nrH^{\text{nr}}_{n^{\prime}}forn′≥nn^{\prime}\geq nand their mirror counterparts) ofHn∞H^{\infty}_{n}.
We similarly denote the canonical ensemble of those blocks asρnres\rho^{\text{res}}_{n},ρnnr\rho^{\text{nr}}_{n}, etc, with a fixedTTleft implicit.

## IV.3.1Interpretation as closed systems

Although we can interpretρn∞\rho^{\infty}_{n}as the equilibrium state when we couple each block ofHn∞H^{\infty}_{n}to a thermal bath, the underlying intention is instead to study a closed system.
Indeed, many-body localization and quantum thermalization are mostly about the properties of an isolated quantum system.
Therefore, we should conceptually treat our system as being isolated. That is, in a microcanonical ensemble at some energy densityee, rather than being coupled to a bath with temperatureTT.
However, due to the boundary size issue of our system, it is not clear how to rigorously define a microcanonical ensemble, as we would need to make finite cuts of our system and take limits without being dominated by boundary effects.
(The problem we need to finesse is that a finite isolated system necessarily has a boundary, which is problematic for our purpose.)
Instead, we will just make an informal argument about why this interpretation (and using the canonical ensemble) is expected to work.

First, we fix annnand treatHn∞H^{\infty}_{n}as a set of isolated blocks (not coupled to an external bath).
From textbook statistical mechanics, we know that if we have a system consisting of a large numberNNof identical blocks, the microcanonical ensemble of the total system at energyeeis locally equivalent to the product of canonical ensembles of the blocks at temperatureTT, in theN→∞N\to\inftylimit, whereTTis determined such that the expected energy density of a block isee.
Our situation is a bit more complicated, as the blocks are not identical and the distribution of blocks withinHn∞H^{\infty}_{n}is highly non-uniform.
Moreover, whenLnnrL^{\text{nr}}_{n}grows fast enough, a finite patch of the system can be dominated by a singleHnnrH^{\text{nr}}_{n}block.
These issues make an unambiguous definition of a thermodynamic limit difficult. For example, the block number limitN→∞N\rightarrow\inftymay not be the same as the usual system size limitL→∞L\rightarrow\inftywhere the limit is taken by adding sites.
Nevertheless, we will assume some regularity requirements on the initial blocks such that the entropy density function ofHnnrH^{\text{nr}}_{n}converges to a fixed functions​(e)s(e)fast enough asn→∞n\to\infty, and thats​(e)s(e)is strictly concave (which implies a one-to-one correspondence betweeneeandTT).
In this way, we should expect some form of the central limit theorem to hold, such that with some reasonable choices of a thermodynamic limit, the microcanonical ensemble ofHn∞H^{\infty}_{n}at energy densityeewill be locally equivalent toρn∞\rho^{\infty}_{n}at temperatureT=d​e/d​sT=de/ds.

The above procedure corresponds to taking some kinds ofL→∞L\to\inftylimit first, and next, we also need to take the limit on the depth of the circuit (n→∞n\to\infty) to complete the construction.
At a givennn, local observables start to suffer from finite-size effects at a length scaleLnresL^{\text{res}}_{n}.
That is, the effective size of the bulk is aroundLnresL^{\text{res}}_{n}.
So takingL→∞L\to\inftybeforen→∞n\to\inftyimplies that the effective bulk can be much smaller than the entire system, which is the case for our system.
We expect (and assume) that the two limits can be taken together in some sense, but providing the exact procedure is beyond the scope of this paper.

Below, all the rigorous proofs will be directly based on the local properties of the canonical ensembleρn∞\rho^{\infty}_{n}withn→∞n\to\inftytaken at the end, and only their physical interpretations will be related to the closed system interpretation discussed here.
Our results are based on this reasonable assumption of the equivalence between microcanonical and canonical ensembles for the problem, but we believe that our results are valid beyond this assumption even for the microcanonical ensemble in the thermodynamic limit, although doing that is beyond the scope of the current work.

## IV.3.2Evolution innn

To analyze the properties of the system at finitennand taken→∞n\to\infty, we need to consider the relation betweenρn∞\rho^{\infty}_{n}andρn+1∞\rho^{\infty}_{n+1}.
To do this, note thatρn+1∞\rho^{\infty}_{n+1}only differs fromρn∞\rho^{\infty}_{n}by merging groups of the tensor factorsρn+1lim=ρnnr⊗ρnres⊗ρnres~⊗ρnnr~↦ρn+1res\rho^{\text{lim}}_{n+1}=\rho^{\text{nr}}_{n}\otimes\rho^{\text{res}}_{n}\otimes\widetilde{\rho^{\text{res}}_{n}}\otimes\widetilde{\rho^{\text{nr}}_{n}}\mapsto\rho^{\text{res}}_{n+1}(53)

which corresponds to four blocks being merged into one in Fig.5.
This merging consists of two changes: the eigenstate basis rotation due toUnU_{n}, and the modification of the Boltzmann weights due to energy level shifts fromHn+1limH^{\text{lim}}_{n+1}toHn+1resH^{\text{res}}_{n+1}.
To calculate the changes, first we writeρn+1lim=∑XqX​|X⟩n​⟨X|\rho^{\text{lim}}_{n+1}=\sum_{X}q_{X}|X\rangle_{n}\langle X|(54)

with Boltzmann weightsqX=e−En+1,Xlim/T∑X′e−En+1,X′lim/Tq_{X}=\frac{e^{-E^{\text{lim}}_{n+1,X}/T}}{\sum_{X^{\prime}}e^{-E^{\text{lim}}_{n+1,X^{\prime}}/T}}(55)

whereEn+1,XlimE^{\text{lim}}_{n+1,X}is the energy of the state|X⟩n|X\rangle_{n}inHn+1limH^{\text{lim}}_{n+1}(the bitstringXXwas written asA​B​C​DABCDbefore; here we use a single letter for brevity).
Now note thatUnlim​|X⟩nU^{\text{lim}}_{n}|X\rangle_{n}is an eigenstate ofHn+1limH^{\text{lim}}_{n+1}as well, with the same energyEn+1,XlimE^{\text{lim}}_{n+1,X}, asUnlimU^{\text{lim}}_{n}only rotates the eigenstates in each degenerate subspace ofHn+1limH^{\text{lim}}_{n+1}.
Thus, we haveUnlim​ρn+1lim​Unlim⁣†=ρn+1lim,U^{\text{lim}}_{n}\rho^{\text{lim}}_{n+1}U^{\text{lim}\dagger}_{n}=\rho^{\text{lim}}_{n+1},(56)

which means that the only change due to eigenstate rotation is from the error term in (47).
To bound the change, we use the trace distance for the density matrices:‖Un​ρn+1lim​Un†−ρn+1lim‖1\displaystyle\left\|U_{n}\rho^{\text{lim}}_{n+1}U^{\dagger}_{n}-\rho^{\text{lim}}_{n+1}\right\|_{1}(57)≤‖ℰn‖​‖ρn+1lim‖1​‖Un†‖+‖Unlim‖​‖ρn+1lim‖1​‖ℰn†‖\displaystyle\leq\|\mathcal{E}_{n}\|\,\|\rho^{\text{lim}}_{n+1}\|_{1}\,\|U_{n}^{\dagger}\|+\|U^{\text{lim}}_{n}\|\,\|\rho^{\text{lim}}_{n+1}\|_{1}\,\|\mathcal{E}_{n}^{\dagger}\|<2​ϵn\displaystyle<2\epsilon_{n}

where∥⋅∥1\|\cdot\|_{1}denotes the trace norm.
Next, we calculate the change due to energy level shifts.
The final ensemble isρn+1res=∑XqX′​|X⟩n+1​⟨X|\rho^{\text{res}}_{n+1}=\sum_{X}q^{\prime}_{X}|X\rangle_{n+1}\langle X|(58)

with new Boltzmann weightsqX′=e−En+1,Xres/T∑X′e−En+1,X′res/Tq^{\prime}_{X}=\frac{e^{-E^{\text{res}}_{n+1,X}/T}}{\sum_{X^{\prime}}e^{-E^{\text{res}}_{n+1,X^{\prime}}/T}}(59)

whereEn+1,XresE^{\text{res}}_{n+1,X}is the energy of the state|X⟩n+1|X\rangle_{n+1}inHn+1resH^{\text{res}}_{n+1}.
Asρn+1res\rho^{\text{res}}_{n+1}only differs fromUn​ρn+1lim​Un†U_{n}\rho^{\text{lim}}_{n+1}U^{\dagger}_{n}by a shift of Boltzmann weights fromqXq_{X}toqX′q^{\prime}_{X}, what we need to bound isqX′−qXq^{\prime}_{X}-q_{X}.
To derive the bound, first note that due to the error bound,|En+1,Xres−En+1,Xlim|<ϵn2,\left|E^{\text{res}}_{n+1,X}-E^{\text{lim}}_{n+1,X}\right|<\frac{\epsilon_{n}}{2},(60)

we havee−ϵn/2​T<rX:=e−En+1,Xres/Te−En+1,Xlim/T<eϵn/2​T.e^{-\epsilon_{n}/2T}<r_{X}:=\frac{e^{-E^{\text{res}}_{n+1,X}/T}}{e^{-E^{\text{lim}}_{n+1,X}/T}}<e^{\epsilon_{n}/2T}.(61)

The new weights can be expressed in terms of the old weights asqX′=qX​rX∑X′qX′​rX′.q^{\prime}_{X}=\frac{q_{X}r_{X}}{\sum_{X^{\prime}}q_{X^{\prime}}r_{X^{\prime}}}.(62)

Now, the numerator of (62) is bounded by (61), and the denominator is a weighted average of such bounds.
Therefore, we arrive at the ratio bounde−ϵn/T<qX′qX<eϵn/T.e^{-\epsilon_{n}/T}<\frac{q^{\prime}_{X}}{q_{X}}<e^{\epsilon_{n}/T}.(63)

To transform this bound into a trace distance bound, we bound the sum of probability differences∑X|qX′−qX|\displaystyle\sum_{X}|q^{\prime}_{X}-q_{X}|(64)=∑qX>qX′qX​(1−qX′qX)+∑qX<qX′qX​(qX′qX−1)\displaystyle=\sum_{q_{X}>q^{\prime}_{X}}q_{X}\left(1-\frac{q^{\prime}_{X}}{q_{X}}\right)+\sum_{q_{X}<q^{\prime}_{X}}q_{X}\left(\frac{q^{\prime}_{X}}{q_{X}}-1\right)<(1−x)​(1−e−ϵn/T)+x​(eϵn/T−1)\displaystyle<(1-x)(1-e^{-\epsilon_{n}/T})+x(e^{\epsilon_{n}/T}-1)=2​tanh⁡ϵn2​T\displaystyle=2\tanh\frac{\epsilon_{n}}{2T}

wherexxis the sum ofqXq_{X}thatqX<qX′q_{X}<q^{\prime}_{X}, under the most extreme condition that all the probability shifts are saturated, that is,(1−x)​e−ϵn/T+x​eϵn/T=1(1-x)e^{-\epsilon_{n}/T}+xe^{\epsilon_{n}/T}=1.
So we arrive at the bound on trace distance‖ρn+1res−Un​ρn+1lim​Un†‖1<2​tanh⁡ϵn2​T.\left\|\rho^{\text{res}}_{n+1}-U_{n}\rho^{\text{lim}}_{n+1}U^{\dagger}_{n}\right\|_{1}<2\tanh\frac{\epsilon_{n}}{2T}.(65)

Combining with (57), we finally arrive at‖ρn+1res−ρn+1lim‖1\displaystyle\left\|\rho^{\text{res}}_{n+1}-\rho^{\text{lim}}_{n+1}\right\|_{1}<2​ϵn+2​tanh⁡ϵn2​T\displaystyle<2\epsilon_{n}+2\tanh\frac{\epsilon_{n}}{2T}(66)∼2​ϵn+ϵnT.\displaystyle\sim 2\epsilon_{n}+\frac{\epsilon_{n}}{T}.

The above bound implies that for any local observableOO(a Hermitian operator supported on a finite number of sites in the infinite chain), its canonical expectation value⟨O⟩n:=Tr⁡(O​ρn∞)\langle O\rangle_{n}:=\Tr(O\rho^{\infty}_{n})(67)

has a well-defined limitlimn→∞⟨O⟩n:=⟨O⟩∞.\lim_{n\to\infty}\langle O\rangle_{n}:=\langle O\rangle_{\infty}.(68)

This is due to that, for any large enoughnn,OOis completely inside anHnresH^{\text{res}}_{n}orHnres~\widetilde{H^{\text{res}}_{n}}block.
So the bound (66) implies|⟨O⟩n+1−⟨O⟩n|\displaystyle\left|\langle O\rangle_{n+1}-\langle O\rangle_{n}\right|≤‖O‖​‖ρn+1res−ρn+1lim‖1\displaystyle\leq\|O\|\left\|\rho^{\text{res}}_{n+1}-\rho^{\text{lim}}_{n+1}\right\|_{1}(69)≲‖O‖​(2​ϵn+ϵnT).\displaystyle\lesssim\|O\|\left(2\epsilon_{n}+\frac{\epsilon_{n}}{T}\right).

By the requirements on the error bounds, the accumulated shifts converge, leading to a well-defined limit.
The limit⟨O⟩∞\langle O\rangle_{\infty}provides a well-defined notion for the thermodynamic expectation value of a local observable, even if we cannot directly define the energy eigenstates ofH∞H_{\infty}.
Also note that we only consider nonzero temperatures and that the bound converges more slowly for temperatures closer to zero.

## IV.3.3Sampling from the ensemble

As we will study the eigenstate properties of the system, especially for ETH, which is based on the properties of individual eigenstates and not just ensemble averages, we need to define how to sample an eigenstate from the ensemble.
Conceptually, what we intend to do is to sample an eigenstate from a narrow energy window around an energy densityee.
However, as we mentioned, there are difficulties in defining the microcanonical ensemble rigorously.
Instead, we will go with the counterpart in the canonical ensemble, to “choose an eigenstate at temperatureTT”.
To define this, we again use the property that the canonical ensemble ofHn∞H^{\infty}_{n}is a product ensemble of blocks, so the natural definition is to independently sample an energy eigenstate for each blockHHinHn∞H^{\infty}_{n}, such that an eigenstate|X⟩|X\rangleofHHhas a probability of the Boltzmann weightqX=e−EX/T/∑X′e−EX′/Tq_{X}=e^{-E_{X}/T}/\sum_{X^{\prime}}e^{-E_{X^{\prime}}/T}of being chosen.
If we take the formal tensor product of the sampled eigenstates from all blocks, we get an eigenstate|S⟩n|S\rangle_{n}ofHn∞H^{\infty}_{n}.
We will say that this eigenstate|S⟩n|S\rangle_{n}is being sampled fromρn∞\rho^{\infty}_{n}.
As we do not define the eigenstates ofH∞H_{\infty}, we will not define the sampling of eigenstates fromH∞H_{\infty}.
Rather, we will only study eigenstate properties at a finitenn, with the limitn→∞n\to\inftytaken in the end.

As discussed in Sec.IV.3.1, we expect a closed system interpretation ofρn∞\rho^{\infty}_{n}under a suitable regularity condition of theHnnrH^{\text{nr}}_{n}blocks and a suitableL→∞L\to\inftylimit.
Under these assumptions, we expect that the sampling fromρn∞\rho^{\infty}_{n}is also equivalent to that from a closed system.
More specifically, as long as we only look at the local properties of the sampled eigenstate, we expect that it is equivalent to randomly choosing an energy eigenstate in a narrow energy window around an energy densityee, which is determined byT=d​e/d​sT=de/dsfrom the limit entropy functions​(e)s(e)ofHnnrH^{\text{nr}}_{n}asn→∞n\to\infty.

## IV.4Fluctuations of local observable expectations

To explore the thermalization/localization properties of the many-body system, we study the fluctuations of local observable expectations for eigenstates sampled fromρn∞\rho^{\infty}_{n}.
There are two possible scenarios.
If the fluctuations for all local observables go to zero asn→∞n\to\infty, then we can say that a randomly sampled eigenstate locally looks thermal with probability 1.
Otherwise, a randomly sampled eigenstate will contain local information that distinguishes it from a thermal state.
Under the closed system interpretation ofρn∞\rho^{\infty}_{n}with a suitable way to take theL→∞L\to\inftyand then→∞n\to\inftylimits together, we expect the first scenario to be a form of the weak eigenstate thermalization hypothesis (ETH), and the second scenario to exhibit MBL-like behavior.
In this subsection, we derive the key recursion relations of the evolution of the diagonal matrix element variance
with respect to the level indexnn, which is then used in the next subsection to characterize the two MBC phases.
Then in Sec.IV.6, we will show that they can exist as finite-temperature phases in some situations.

We fix a local observableOOand consider sampling a state|S⟩n|S\rangle_{n}fromρn∞\rho^{\infty}_{n}.
The quantum expectation value,⟨S|O|S⟩nn{}_{n}\langle S|O|S\rangle_{n}, is then considered a classical random variable.
The classical expectation value of this random variable is the same as the ensemble average. That is,𝔼|S⟩n∼ρn∞[n⟨S|O|S⟩n]=⟨O⟩n,\mathbb{E}_{|S\rangle_{n}\sim\rho^{\infty}_{n}}[_{n}\langle S|O|S\rangle_{n}]=\langle O\rangle_{n},(70)

where∼\simdenotes that the eigenstate is drawn from the corresponding ensemble.
We study the variance of this classical random variable, denoted as the diagonal matrix element variance:Varn⁡[O]\displaystyle\operatorname{Var}_{n}[O]:=Var|S⟩n∼ρn∞[n⟨S|O|S⟩n]\displaystyle=\operatorname{Var}_{|S\rangle_{n}\sim\rho^{\infty}_{n}}[_{n}\langle S|O|S\rangle_{n}](71)=𝔼|S⟩n∼ρn∞[(n⟨S|O|S⟩n−⟨O⟩n)2].\displaystyle=\mathbb{E}_{|S\rangle_{n}\sim\rho^{\infty}_{n}}[(_{n}\langle S|O|S\rangle_{n}-\langle O\rangle_{n})^{2}].

We will derive a recursion relation for the diagonal matrix element variance betweennnandn+1n+1, and then characterize its behavior in then→∞n\to\inftylimit.

## IV.4.1Evolution innnfor a fixed local observable

In this subsection, we derive a recursion relation fromVarn⁡[O]\operatorname{Var}_{n}[O]toVarn+1⁡[O]\operatorname{Var}_{n+1}[O]with a fixed localOO.
As in Sec.IV.3.2, we consider the merging of four blocks into one fromnnton+1n+1, where we have two changes: the basis rotation caused byUnU_{n}and the shifts of Boltzmann weights.

We choose a large enoughnnso that the support ofOOis within anHnresH^{\text{res}}_{n}orHnres~\widetilde{H^{\text{res}}_{n}}block.
Without loss of generality, we further assume thatOOis located in anHnresH^{\text{res}}_{n}block.
The mirror ofOOin theHnres~\widetilde{H^{\text{res}}_{n}}block is referred to asO~\widetilde{O}.
Now the variance can be written asVarn[O]=Var|X⟩n∼ρn+1lim[n⟨X|O|X⟩n]\operatorname{Var}_{n}[O]=\operatorname{Var}_{|X\rangle_{n}\sim\rho^{\text{lim}}_{n+1}}[_{n}\langle X|O|X\rangle_{n}](72)

whereX=A​B​C​DX=ABCDis the bitstring labeling the eigenstates ofHn+1limH^{\text{lim}}_{n+1}. The labelA​B​C​DABCDindicates that the eigenstate is block-wise from its four decoupled blocks.

The first step is to do the change of basis from|X⟩n|X\rangle_{n}toUnlim​|X⟩n=|X⟩lim=|A​B​C​D⟩limU^{\text{lim}}_{n}|X\rangle_{n}=|X\rangle_{\text{lim}}=|ABCD\rangle_{\text{lim}}(in the notations of Sec.IV.1.3).
Although this does not change the density matrix itself [see (56)], it does affect the variance, as we are now sampling using a different basis in each degenerate subspaceHnlimH^{\text{lim}}_{n}.
By (43), we haven⟨X|UnlimOUnlim⁣†|X⟩n={⟨X|O|X⟩nn,if​A≠D~,12(n⟨X|O|X⟩n+n⟨X|O~|X⟩n),if​A=D~._{n}\langle X|U^{\text{lim}}_{n}O\,U^{\text{lim}\dagger}_{n}|X\rangle_{n}\\
=\begin{cases}{}_{n}\langle X|O|X\rangle_{n},&\text{if }A\neq\widetilde{D},\\
\frac{1}{2}(_{n}\langle X|O|X\rangle_{n}+\,_{n}\langle X|\widetilde{O}|X\rangle_{n}),&\text{if }A=\widetilde{D}.\end{cases}(73)

The bitstringsAA,BB,CC, andDDare independently sampled. And sinceOO(O~\widetilde{O}) is only supported on theHnresH^{\text{res}}_{n}(Hnres~\widetilde{H^{\text{res}}_{n}}) block,⟨X|O|X⟩nn{}_{n}\langle X|O|X\rangle_{n}(⟨X|O~|X⟩nn{}_{n}\langle X|\widetilde{O}|X\rangle_{n}) only depends onBB(CC).
Moreover, the distribution ofBBis exactly the same asC~\widetilde{C}.
Thus, we haveVar|X⟩n∼ρn+1lim[n⟨X|UnlimOUnlim⁣†|X⟩n]=(1−pn)​Varn⁡[O]+pn​Varn⁡[O]2,\operatorname{Var}_{|X\rangle_{n}\sim\rho^{\text{lim}}_{n+1}}[_{n}\langle X|U^{\text{lim}}_{n}O\,U^{\text{lim}\dagger}_{n}|X\rangle_{n}]\\
=(1-p_{n})\operatorname{Var}_{n}[O]+p_{n}\frac{\operatorname{Var}_{n}[O]}{2},(74)

wherepnp_{n}is the probability thatA=D~A=\widetilde{D}. SinceAAandD~\widetilde{D}have the same distribution, equivalently,pnp_{n}can be understood as the probability that two individual samplings fromρnnr\rho^{\text{nr}}_{n}result in the same state. Thus, we havepn=Tr(e−Hnnr/TTr⁡e−Hnnr/T)2=e−S2,nnrp_{n}=\Tr\left(\frac{e^{-H^{\text{nr}}_{n}/T}}{\Tr e^{-H^{\text{nr}}_{n}/T}}\right)^{2}=e^{-S_{2,n}^{\text{nr}}}(75)

whereS2,nnrS_{2,n}^{\text{nr}}is the thermodynamic Rényi-22entropy ofHnnrH^{\text{nr}}_{n}at temperatureTT.
Eq. (74) has a clear physical interpretation: the variance of the local observable remains the same if a resonance does not occur at thennth level, and it splits in half if a resonance occurs due to the local state being averaged with its mirror counterpart.

The rest of the derivation towardsVarn+1⁡[O]\operatorname{Var}_{n+1}[O]is to apply the error terms.
First, by the error term inUnU_{n}, and the general inequality for random variablesYYandZZ|Var⁡[Y+Z]−Var⁡[Y]|≤Var⁡[Z]+2​Var⁡[Y]​Var⁡[Z]\big|\operatorname{Var}[Y+Z]-\operatorname{Var}[Y]\big|\leq\operatorname{Var}[Z]+2\sqrt{\operatorname{Var}[Y]\operatorname{Var}[Z]}(76)

we have|Var|X⟩n∼ρn+1lim[n⟨X|UnOUn†|X⟩n]−Var|X⟩n∼ρn+1lim[n⟨X|UnlimOUnlim⁣†|X⟩n]|<4​ϵn​(1+ϵn)​‖O‖2\Big|\operatorname{Var}_{|X\rangle_{n}\sim\rho^{\text{lim}}_{n+1}}[_{n}\langle X|U_{n}O\,U^{\dagger}_{n}|X\rangle_{n}]\\
-\operatorname{Var}_{|X\rangle_{n}\sim\rho^{\text{lim}}_{n+1}}[_{n}\langle X|U^{\text{lim}}_{n}O\,U^{\text{lim}\dagger}_{n}|X\rangle_{n}]\Big|\\
<4\epsilon_{n}(1+\epsilon_{n})\|O\|^{2}(77)

Next, for the shift of the Boltzmann weight, by (64) and the general inequality for a random variableYYunder two different probability distributions{qi}\{q_{i}\}and{qi′}\{q^{\prime}_{i}\}|Varq⁡[Y]−Varq′⁡[Y]|≤(range⁡Y)22​∑i|qi′−qi|,\big|\operatorname{Var}_{q}[Y]-\operatorname{Var}_{q^{\prime}}[Y]\big|\leq\frac{(\operatorname{range}Y)^{2}}{2}\sum_{i}|q^{\prime}_{i}-q_{i}|,(78)

we have|Varn+1[O]−Var|X⟩n∼ρn+1lim[n⟨X|UnOUn†|X⟩n]|=|Var|X⟩n+1∼ρn+1res[n+1⟨X|O|X⟩n+1]−Var|X⟩n+1∼Un†​ρn+1lim​Un[n+1⟨X|O|X⟩n+1]|<4​‖O‖2​tanh⁡ϵn2​T.\Big|\operatorname{Var}_{n+1}[O]-\operatorname{Var}_{|X\rangle_{n}\sim\rho^{\text{lim}}_{n+1}}[_{n}\langle X|U_{n}O\,U^{\dagger}_{n}|X\rangle_{n}]\Big|\\
=\Big|\operatorname{Var}_{|X\rangle_{n+1}\sim\rho^{\text{res}}_{n+1}}[_{n+1}\langle X|O|X\rangle_{n+1}]\\
-\operatorname{Var}_{|X\rangle_{n+1}\sim U_{n}^{\dagger}\rho^{\text{lim}}_{n+1}U_{n}}[_{n+1}\langle X|O|X\rangle_{n+1}]\Big|\\
<4\|O\|^{2}\tanh\frac{\epsilon_{n}}{2T}.(79)

Combining (74), (77), and (79), we obtain the final recursion relation:Varn+1⁡[O]=(1−pn2)​Varn⁡[O]+δn\operatorname{Var}_{n+1}[O]=\left(1-\frac{p_{n}}{2}\right)\operatorname{Var}_{n}[O]+\delta_{n}(80)

with error term|δn|\displaystyle|\delta_{n}|<4​‖O‖2​(ϵn+tanh⁡ϵn2​T+ϵn2)\displaystyle<4\|O\|^{2}\left(\epsilon_{n}+\tanh\frac{\epsilon_{n}}{2T}+\epsilon_{n}^{2}\right)(81)∼2​‖O‖2​(2​ϵn+ϵnT).\displaystyle\sim 2\|O\|^{2}\left(2\epsilon_{n}+\frac{\epsilon_{n}}{T}\right).

This property will be used in the next subsection to characterize the two phases of MBC.

## IV.4.2Evolution innnfor approximate LIOMs

As we are going to discuss the ETH/MBL behaviors inH∞H_{\infty}, one important set of local observables is the approximate LIOM operatorsτn,jz\tau^{z}_{n,j}, defined as returning thejjth bit of theHn∞H^{\infty}_{n}eigenstate|S⟩n|S\rangle_{n}(with ‘0’ corresponding to eigenvalue+1+1and ‘1’ to−1-1).
In addition to evolving the variance ofτn0,jz\tau^{z}_{n_{0},j}for a fixedn0n_{0}innn, which is a special case of (80), we are also interested in the recursion relation fromVarn⁡[τn,jz]\operatorname{Var}_{n}[\tau^{z}_{n,j}]toVarn+1⁡[τn+1,jz]\operatorname{Var}_{n+1}[\tau^{z}_{n+1,j}](and also the drift of the expectation values).

Note that this case is actually simpler than deriving (80).
First, if thejjth LIOM is within aHn′nrH^{\text{nr}}_{n^{\prime}}orHn′nr~\widetilde{H^{\text{nr}}_{n^{\prime}}}block inHn∞H^{\infty}_{n}withn′>nn^{\prime}>n, then its evolution is trivial⟨τn+1,jz⟩n+1=⟨τn,jz⟩n,Varn+1⁡[τn+1,jz]=Varn⁡[τn,jz].\langle\tau^{z}_{n+1,j}\rangle_{n+1}=\langle\tau^{z}_{n,j}\rangle_{n},\quad\operatorname{Var}_{n+1}[\tau^{z}_{n+1,j}]=\operatorname{Var}_{n}[\tau^{z}_{n,j}].(82)

Now, if thejjth LIOM is in one of the four types of blocks inHn∞H^{\infty}_{n}that merge into anHn+1resH^{\text{res}}_{n+1}block inHn+1∞H^{\infty}_{n+1}, then we need to use a similar derivation as before.
However, the eigenstate rotation step becomes trivial, asUn​τn,jz​Un†U_{n}\tau^{z}_{n,j}U^{\dagger}_{n}is exactlyτn+1,jz\tau^{z}_{n+1,j}.
Therefore, we only need to consider the shift in Boltzmann weights, resulting in⟨τn+1,jz⟩n+1\displaystyle\langle\tau^{z}_{n+1,j}\rangle_{n+1}=⟨τn,jz⟩n+δn′\displaystyle=\langle\tau^{z}_{n,j}\rangle_{n}+\delta^{\prime}_{n}(83)Varn+1⁡[τn+1,jz]\displaystyle\operatorname{Var}_{n+1}[\tau^{z}_{n+1,j}]=Varn⁡[τn,jz]+δn′′\displaystyle=\operatorname{Var}_{n}[\tau^{z}_{n,j}]+\delta^{\prime\prime}_{n}

with error bounds|δn′|<2​tanh⁡ϵn2​T,|δn′′|<4​tanh⁡ϵn2​T.|\delta^{\prime}_{n}|<2\tanh\frac{\epsilon_{n}}{2T},\quad|\delta^{\prime\prime}_{n}|<4\tanh\frac{\epsilon_{n}}{2T}.(84)

There is no decay of variance [compared to (80)], as theτn,jz\tau^{z}_{n,j}operators themselves grow longer innnto absorb the effect of resonances, unlike a fixed local operatorOOthat stays the same during a resonance.

## IV.5Two types of MBC phases

Having derived the recursion relation (80), we can now characterize the two types of MBC phases by whetherVarn⁡[O]→0\operatorname{Var}_{n}[O]\to 0asn→∞n\to\infty, that is, whether (almost) all eigenstates sampled at temperatureTTlocally look like the canonical ensemble atTT.
Due to the convergence of accumulated errors, we can see that it is equivalent to whether the infinite product∏n(1−pn/2)\prod_{n}(1-p_{n}/2)converges to a finite value.
More specifically, pick a large enoughn0n_{0}beyond which (80) holds, and define the partial productPn=∏n′=n0n−1(1−pn′/2)P_{n}=\prod_{n^{\prime}=n_{0}}^{n-1}(1-p_{n^{\prime}}/2), then we have, forn≥n0n\geq n_{0},Varn⁡[O]=Pn​Varn0⁡[O]+∑n′=n0+1nPnPn′​δn′−1.\operatorname{Var}_{n}[O]=P_{n}\operatorname{Var}_{n_{0}}[O]+\sum_{n^{\prime}=n_{0}+1}^{n}\frac{P_{n}}{P_{n^{\prime}}}\delta_{n^{\prime}-1}.(85)

Hence, we need to distinguish between two cases depending on whetherPn→0P_{n}\to 0, or equivalently, whether∑npn\sum_{n}p_{n}diverges.
IfPn→0P_{n}\to 0, then sincePn/Pn′≤1P_{n}/P_{n^{\prime}}\leq 1and∑nδn\sum_{n}\delta_{n}converges, the limit ofVarn⁡[O]\operatorname{Var}_{n}[O]is bounded by an arbitrarily small value by choosing a largen0n_{0}.
Therefore, we haveVarn⁡[O]→0\operatorname{Var}_{n}[O]\to 0asn→∞n\to\infty.
We call this ETH-like phase themany-body critically extended(MBC-E) phase.
That is,∑npn=∞⟹MBC-E (ETH-like)\sum_{n}p_{n}=\infty\implies\text{MBC-E (ETH-like)}(86)

We will discuss the difference from the usual ETH phase in Sec.IV.6.

Conversely, ifPn→P∞>0P_{n}\to P_{\infty}>0, and suppose additionally thatVarn0⁡[O]>1P∞​∑n=n0∞|δn|.\operatorname{Var}_{n_{0}}[O]>\frac{1}{P_{\infty}}\sum_{n=n_{0}}^{\infty}|\delta_{n}|.(87)

ThenVarn⁡[O]\operatorname{Var}_{n}[O]does not go to zero asn→∞n\to\infty.
That is, the observableOOcan distinguish a randomly sampled eigenstate from the canonical ensemble.
To construct an extensive set of local observables that satisfy (87), we will use the approximate LIOMsτn,jz\tau^{z}_{n,j}.
Note that there is a lower boundVar1⁡[τ1,jz]>V\operatorname{Var}_{1}[\tau^{z}_{1,j}]>Vindependent ofjj, so by choosingn1n_{1}such thatV−∑n=n1∞δn′>V′>0V-\sum_{n=n_{1}}^{\infty}\delta_{n}^{\prime}>V^{\prime}>0, and by (83), we haveVarn⁡[τn,jz]>V′\operatorname{Var}_{n}[\tau^{z}_{n,j}]>V^{\prime}(88)

for alln>n1n>n_{1}withjjin anHn′nrH^{\text{nr}}_{n^{\prime}}block withn′>n1n^{\prime}>n_{1}.
Then we pickn0>n1n_{0}>n_{1}so that∑n=n0−1∞|δn|/P∞<V′\sum_{n=n_{0}-1}^{\infty}|\delta_{n}|/P_{\infty}<V^{\prime}.
Now, (87) is satisfied for all suchτn0,jz\tau^{z}_{n_{0},j}, giving an extensive set of local observables that violate the ETH-like property111Note that if the temperature is not too small, one can actually choosen1=1n_{1}=1and have a complete set of such observables (that is, for alljj).
But for extremely low temperatures, there remains the possibility that some initial building blocks with lownnare dominated by the ground state, giving a variance so small that it is indistinguishable from the error bound..
We call this MBL-like phase themany-body critically localized(MBC-L) phase.
In other words,∑npn<∞⟹MBC-L (MBL-like).\sum_{n}p_{n}<\infty\implies\text{MBC-L (MBL-like)}.(89)

While there are many other diagnostics that are usually applied to MBL that may also apply to MBC-L, we will not provide a rigorous derivation for each one.
For example, in the MBC-L phase, the connected correlation function between two observablesOiO_{i}andOjO_{j}supported around sitesiiandjjdecays to zero for fixediiwithj→±∞j\to\pm\infty.
This can be seen by noticing that for farawayiiandjj, the blocks they belong to will not be coupled until somen0n_{0}(which goes to infinity asj→±∞j\to\pm\infty), giving a zero correlation.
Now, wheniiandjjfirst get coupled at leveln0n_{0}, with a probability1−pn1-p_{n}, there is no resonance, and therefore the only contribution to the correlation is the error term.
The bound of the correlation is then derived by the convergence ofpnp_{n}, Eqs. (66), (77), and (79) for the shift at leveln0n_{0}, and Eqs. (69) and (80) for the bound of the shifts caused by subsequent levels.
As another example, the entanglement entropy exhibits area-law scaling with the subsystem size (for almost every energy eigenstate).
This can similarly be shown by noticing that a cut in the chain only gets anO​(1)O(1)entanglement growth when it is in a resonant block and a resonance occurs. Thus, by a similar error-bounding argument as above, one can show that the growth is limited by the convergence ofpnp_{n}.
We will discuss the difference between the MBC-L phase in our model and the usual MBL phase in Sec.IV.6.

## IV.5.1Interpretation and single-particle analogy

One can compare the above results with the single-particle case in Sec.III.4.1, where the system becomes singular continuous.
In the single-particle case, the “local observable” is just the local state projector, whose expectation value becomes the weight discussed in Sec.III.4.1.
Since the single-particle eigenstates delocalize asn→∞n\to\infty, the expectation value decays to zero in such a limit.
Hence, the weight can be considered as the single-particle analogy of the diagonal matrix element variance of local observables.

Now, the first term in Eq. (74), where a resonance is created, is analogous to the splitting of weights in Sec.III.4.1.
Thus, the mechanism that leads to the absence of a pure-point spectrum in the single-particle model is the reason for the ETH-like behavior in the many-body case.
On the other hand, we mention that the mechanism that leads to the absence of an absolutely continuous spectrum in the single-particle case is the reason for the separation between the resonance timescalestnt_{n}at differentnn.
Such a separation is expected to result in differences in the thermalization properties between MBC-E and the usual ETH phase.
For example, energy transport can be arbitrarily slow due to the fast divergence of the timescales.
Therefore, the direct analogy of the singular continuity in our many-body system is the ETH-like but non-thermal-like behavior of MBC-E.

However, the collective freezing effect has no single-particle analogy, whose consequence is that the splitting becomes conditional, depending on the probabilitypnp_{n}in Eq. (74). In the single-particle case, the weights always get split in half (up to an error term) fromnnton+1n+1(n≥n0n\geq n_{0}), and eventually, there will be an infinite number of splittings whenn→∞n\rightarrow\infty. As an analogy, in the many-body case, this corresponds topn=1p_{n}=1. While the MBC-L phase appears only when there is a finite number of splittings such that the system is MBL-like, there is no single-particle analogy for it.
Therefore, we may say that MBC-L (as well as its transition from MBC-E) is purely a many-body phenomenon.

## IV.6Mobility edges, scars, and inverted scars

In the last subsection, we showed that the many-body systems contain two phases: MBC-E (ETH-like) and MBC-L (MBL-like).
Now we will show that instead of the entire spectrum being either ETH-like or MBL-like, our model can have a much richer spectrum.
First, we will show that MBC-E and MBC-L phases can exist in the same system as a finite-TTtransition.
In other words, a many-body mobility edge exists.
Then, we will show that even within the same phase, there exist rare eigenstates that behave like those in the opposite phase.
We will interpret these rare eigenstates in the MBC-E and MBC-L phases as many-body scars and many-body inverted scars, respectively[64,67,68,69,70].

## IV.6.1Many-body mobility edges

Recall that whether our system is in MBC-E or MBC-L is determined by the convergence of∑npn=∑nexp⁡(−S2,nnr)\sum_{n}p_{n}=\sum_{n}\exp(-S_{2,n}^{\text{nr}}), whereS2,nnrS_{2,n}^{\text{nr}}is the thermodynamic Rényi-22entropy ofHnnrH^{\text{nr}}_{n}at temperatureTT.
Hence, one can have a finite-TTphase transition if its convergence depends onTT.
We will show that this happens ifLnnrL^{\text{nr}}_{n}is logarithmically divergent.

TakeLnnr=⌈p​ln⁡n⌉L^{\text{nr}}_{n}=\lceil p\ln n\rceilfor a fixedp>0p>0.
Since the classical Ising model is always in the paramagnetic phase at finiteTTwith a finite correlation length (assuming theδ\deltaterms in the initial building blocks decay to zero withnnfast enough), by the extensiveness of Rényi-22entropy we have, at largennS2,nnr​(T)=Lnnr​s2,nnr​(T)+O​(1)S_{2,n}^{\text{nr}}(T)=L^{\text{nr}}_{n}s_{2,n}^{\text{nr}}(T)+O(1)(90)

for some Rényi-22entropy density functions2,nnr​(T)s_{2,n}^{\text{nr}}(T), which goes to0asT→0T\to 0and goes toln⁡2\ln 2forT→∞T\to\infty.
The series then becomes∑ne−S2,nnr​(T)∼∑nn−p​s2,nnr​(T)\sum_{n}e^{-S_{2,n}^{\text{nr}}(T)}\sim\sum_{n}n^{-ps_{2,n}^{\text{nr}}(T)}(91)

which converges if and only ifp​s2,nnr​(T)>1ps_{2,n}^{\text{nr}}(T)>1.
That is, by tuningpp, we have a tunable critical temperatureTcT_{c}withp​s2,nnr​(Tc)=1ps_{2,n}^{\text{nr}}(T_{c})=1above (below) which the system is in MBC-L (MBC-E).
Assuming the closed-system interpretation in Sec.IV.3.1holds, this finite-TTphase transition corresponds to a thermodynamic many-body mobility edge (MBME) in the energy spectrum.
The counterintuitive phenomenon that high temperatures lead to localization can be viewed as an example of quantum inverse freezing[93].

On the other hand, ifLnnrL^{\text{nr}}_{n}grows asymptotically faster (slower) thanlog⁡n\log n, the system will be in MBC-L (MBC-E) for all nonzero temperatures (including infinity).
That is, there is no many-body mobility edge in such cases.

## IV.6.2Many-body scars

In the MBC-E phase, we have shown that for any local observableOO, the diagonal matrix element varianceVarn⁡[O]\operatorname{Var}_{n}[O]goes to zero asn→∞n\to\infty.
This guarantees that the fraction of sampled eigenstates with non-thermal expectation values goes to zero whenn→∞n\to\infty.
However, this does not mean thatalleigenstates will have thermal expectation values.
Indeed, whether there is a resonance at levelnnis controlled by the state of the non-resonant region, not inherently by the system parameters.
Therefore, one can construct states whose configurations in the non-resonant regions beyond some leveln0n_{0}are chosen to always be asymmetric.
For such a rare state, Eq. (73) always chooses the first value aboven0n_{0}, so that⟨X|O|X⟩nn{}_{n}\langle X|O|X\rangle_{n}gets fixed atn0n_{0}(up to error terms) and does not approach the thermal value.
Moreover, the conditions that produce this rare state do not asymptotically change the energy density.
To see this, one can intuitively think of a Boltzmann sampling of the blocks at leveln0n_{0}. To produce rare states, we just need that a pair of non-resonant blocks never gets symmetric states in the samples, which does not modify the temperature (a more rigorous construction is presented below).
Therefore, under the closed system interpretation, every energy window is expected to contain some rare state, so that the MBC-E phase only satisfies the weak ETH, not the strong one.
These rare states can thus be interpreted as a type of quantum many-body scars.

Now we present a construction of a scarred state|S′⟩|S^{\prime}\ranglegiven a regular energy eigenstate|S⟩|S\rangle(whereSSandS′S^{\prime}are the bitstring labels) based on swapping non-resonant blocks.
Under a suitable definition of the energy density of the infinite chain, we expect that this construction allows us to make the energy density of|S′⟩|S^{\prime}\ranglearbitrarily close to that of|S⟩|S\rangle, assuming that the latter has a well-defined energy density.
First, fix a regionRRand a large enough leveln0n_{0}so thatRRis in a resonant block, and then cut the circuit that produces|S⟩|S\rangleat layern0n_{0}to get|S⟩n0|S\rangle_{n_{0}}.
As the Hamiltonians at this stage are decoupled finite blocks, anHn0nrH^{\text{nr}}_{n_{0}}block with a given configuration almost certainly appears an infinite number of times withinSS, which means that it is possible to exchange the configuration of twoHn0nrH^{\text{nr}}_{n_{0}}blocks (by exchanging the corresponding substrings inSS) so that the configurations in theHn0nrH^{\text{nr}}_{n_{0}},Hn0nr~\widetilde{H^{\text{nr}}_{n_{0}}}pair whose corresponding resonant region containsRRare not mirror symmetric.
Similarly, this can be done for theHnnrH^{\text{nr}}_{n},Hnnr~\widetilde{H^{\text{nr}}_{n}}pair for eachn>n0n>n_{0}.
The resulting binary string after all of these block swaps becomesS′S^{\prime}, whose corresponding eigenstate|S′⟩|S^{\prime}\rangleviolates ETH due to the lack of resonance beyondn0n_{0}for a region containingRR(i.e. Eq. (73) always goes through the second branch beyondn0n_{0}).

Although an infinite shuffling of a sequence in general may lead to convergence issues or change the asymptotic energy density, there are no such issues here.
To see this, note that each swap occurs at a pair of non-resonant blocks at a differentnn, so they correspond to non-overlapping substrings inSS, makingS′S^{\prime}well-defined.
Secondly, as we assume thatLnnr→∞L^{\text{nr}}_{n}\to\inftyasn→∞n\to\infty, in order to make the configuration ofHnnrH^{\text{nr}}_{n}andHnnr~\widetilde{H^{\text{nr}}_{n}}different, we can choose the swaps so that the energy density differenceΔ​en\Delta e_{n}between theHnnrH^{\text{nr}}_{n}block before and after the swap satisfiesΔ​en→0\Delta e_{n}\to 0asn→∞n\to\infty.
Therefore, under a suitable closed system interpretation, these swaps of non-resonant blocks do not modify the energy density at leveln0n_{0}and that|S⟩n0|S\rangle_{n_{0}}and|S′⟩n0|S^{\prime}\rangle_{n_{0}}have the same energy densities222This follows from the fact that for sequencesaka_{k}andbkb_{k}related by swapping terms at disjoint indices(km,km′)(k_{m},k^{\prime}_{m})(i.e.bkm′=akmb_{k^{\prime}_{m}}=a_{k_{m}},akm′=bkma_{k^{\prime}_{m}}=b_{k_{m}}and otherwiseak=bka_{k}=b_{k}) such that|akm′−akm|→0|a_{k^{\prime}_{m}}-a_{k_{m}}|\to 0asm→∞m\to\infty, the averages∑k=1lak/l\sum_{k=1}^{l}a_{k}/land∑k=1lbk/l\sum_{k=1}^{l}b_{k}/lconverge to the same value asl→∞l\to\infty(if either converges)..

Now, by the error bounds, the energy density shifts due to the circuit from leveln0n_{0}to infinity converge, so that the energy density between|S⟩n0|S\rangle_{n_{0}}and|S⟩|S\rangle, and those between|S′⟩n0|S^{\prime}\rangle_{n_{0}}and|S′⟩|S^{\prime}\ranglecan be made arbitrarily small under a suitable closed system interpretation.
This identifies|S′⟩|S^{\prime}\rangleas the required scar state.

The existence of scar states also means that there is no uniform timescale for thermalization, since a normal state may locally look like a scar state up to a finite number of levels.
Indeed, given a local observableOOand any level indexnn, there is a finite fraction of states thatOOdoes not participate in any resonances before levelnn, so the variance ofOOdecays only after that.
That is, for anynn, there is a finite fraction of states whose thermalization timescale is longer thantnt_{n}(although the fraction goes to zero asn→∞n\to\infty).
Note that this phenomenon occurs even if the system is in MBC-E at all temperatures.

Another related property that makes MBC-E different from ETH is that, although the entanglement entropy scales as volume law (in the sense of scaling subsystem size in an infinite chain) due to the local density matrix being thermal, if we take a finite system of lengthLLand cut it in half, from the structure of the circuit in Fig.5one can see that the entanglement entropy cannot grow faster thanO​(log⁡L)O(\log L).
In other words, the volume law is only manifested when we first take the system size to infinity.
This can be interpreted as meaning that, due totnt_{n}growing too fast, a finite system is not enough to probe the full thermalization time, making the effective bulk much smaller than the system size.

## IV.6.3Many-body inverted scars

The above argument regarding many-body scars in the MBC-E phase can be carried over to the MBC-L phase as well.
That is, given a regular state|S⟩|S\ranglein MBC-L, we can construct a rare state|S′⟩|S^{\prime}\rangleby constraining an infinite number of pairs of non-resonant blocks to have symmetric configurations to make it thermal-like.
This condition similarly does not change the energy.
The more rigorous block-swapping construction of the rare states also mostly applies in this case, by swapping theHnnrH^{\text{nr}}_{n}block for an infinite number ofnnaboven0n_{0}with another block that is symmetric withHnnr~\widetilde{H^{\text{nr}}_{n}}, with the difference that when showing that the energy density does not change by the shuffling, we need to use the fact that the original energy density difference between the pair is expected to go to zero for a generic choice of|S⟩|S\rangle.
Under the closed system interpretation, this implies that there exists a set of energy levels of a vanishing fraction, which is dense in the spectrum of MBC-L and ETH-like.
In other words, the quantum expectation values for such rare states converge to the ensemble average of all nearby eigenstates (not just the rare ones).
We interpret them as many-body inverted scars.
Note that although the construction of the inverted scar state begins with a regionRR, the fact that it is thermal-like does not depend on whether the observable is related toRR, as anyR′R^{\prime}eventually becomes in the same resonant region asRRfor a large enoughnn.
In other words, being an inverted scar state (as well as a scar state) is a global property, rather than related to a particular region.

The existence of inverted scar states also implies that the MBC-L phase does not have a natural length scale as in usual MBL phases, as a generic state can locally resemble an inverted scar state.
In a usual MBL phase with a complete set of LIOMs, any given local regionRRis at most involved in resonances with a finite number of sites, as determined by the LIOM supports.
However, in the MBC-L phase, for any level indexnn, there is a finite fraction of states in whichRRis involved in the resonances within a wholeHnresH^{\text{res}}_{n}block at levelnn, meaning that there is no upper bound on the length scale over whichRRcan be involved in a resonance asn→∞n\rightarrow\infty.
This occurs even if the system is in MBC-L at all nonzero temperatures.

The difference between MBC-L and the usual MBL phases can be detected by other diagnostics as well.
In MBC-L, although the correlation functions between observablesOiO_{i}andOjO_{j}decay to zero when|i−j|→∞|i-j|\to\inftyon average, one can select rare states and observables such thatiiandjjare a pair of mirror sites for an arbitrarily largen0n_{0}with the state chosen to be resonant at that level, which then results in anO​(1)O(1)correlation.
For the entanglement entropy, there is no uniform upper bound on the area law constant for a fixed cut in MBC-L.

Another interesting property of the MBC-L phase is that, although there are approximate LIOM with non-thermal expectation values, there does not exist any true LIOM in the system in the conventional sense of commuting with the Hamiltonian, being quasilocal, and having discrete eigenvalues.
To see this, supposeOOis a LIOM that has two closest eigenvaluesλ\lambdaandλ′\lambda^{\prime}, and a primary partO1O_{1}supported in a regionRR(with‖O−O1‖≪|λ−λ′|\|O-O_{1}\|\ll|\lambda-\lambda^{\prime}|).
One can then construct an energy eigenstate with a mirror resonance that superposes the local states inRRwith eigenvaluesλ\lambdaandλ′\lambda^{\prime}; thus, the resulting expectation value⟨O⟩\langle O\rangleunder such an eigenstate is betweenλ\lambdaandλ′\lambda^{\prime}, contradicting the assumption thatOOis a LIOM.

On the other hand, theτj,nz\tau^{z}_{j,n}operators in then→∞n\to\inftylimit behave roughly like a complete set of “LIOMs” in an infinite-temperature MBC-L phase, in the sense that they are true integrals of motion but with an unconventional notion of locality.
To compare this with the usual definition of LIOMs by a Pauli expansion, we first writeUnU_{n}asUn=(1−Mn)+Rn​Mn+ℰnU_{n}=(1-M_{n})+R_{n}M_{n}+\mathcal{E}_{n}(92)

whereMnM_{n}is the orthogonal projector onto theA=D~A=\widetilde{D}subspace in the notation of Eq. (49) andRnR_{n}is a unitary operator that takes|B​C⟩n|BC\rangle_{n}to a superposition according to the rule in Eq. (49).
Now for eachjj, for a large enoughnnsuch thatτj,nz\tau^{z}_{j,n}is supported in a resonant region, by conjugating withUnU_{n}we have333Note thatMn=pn+∑Q∏j∈Qσjz​σj~zM_{n}=p_{n}+\sum_{Q}\prod_{j\in Q}\sigma^{z}_{j}\sigma^{z}_{\tilde{j}}.τj,n+1z=(1−pn)​τj,nz+pn​R†​τj,nz​R+(R†​τj,nz​R−τj,nz)​∑Q∏j∈Qσjz​σj~z+O​(ϵn)\tau^{z}_{j,n+1}=(1-p_{n})\tau^{z}_{j,n}+p_{n}R^{\dagger}\tau^{z}_{j,n}R\\
+(R^{\dagger}\tau^{z}_{j,n}R-\tau^{z}_{j,n})\sum_{Q}\prod_{j\in Q}\sigma^{z}_{j}\sigma^{z}_{\tilde{j}}+O(\epsilon_{n})(93)

wherepn=2−Lnnrp_{n}=2^{-L^{\text{nr}}_{n}}is the infinite-temperature resonance probability andQQruns over all nonempty subsets of sites in theHnresH^{\text{res}}_{n}block.
Iterating ton→∞n\to\infty, we obtain a formal Pauli expansion ofτj,∞z\tau^{z}_{j,\infty}, which is a formal integral of motion ofH∞H_{\infty}:τj,∞z=∑a≤j≤bOa,b\tau^{z}_{j,\infty}=\sum_{a\leq j\leq b}O_{a,b}(94)

where eachOa,bO_{a,b}is a weighted sum of Pauli (σ\sigma) strings, each with the convex hull of support being[a,b][a,b](i.e. acts nontrivially onaaandbband acts trivially outside[a,b][a,b]).
Note that by the first line of (93) and the convergence of∏n(1−pn)>0\prod_{n}(1-p_{n})>0in the MBC-L phase, the coefficients of such local Pauli strings converge to generally nonzero values in then→∞n\to\inftylimit, making the expansion well-defined.
However, instead of having‖Oa,b‖\|O_{a,b}\|decaying with|a−b||a-b|(which is the case for LIOMs in MBL[94,95,96,6]), in the MBC-L phase, there is always a finite fraction of states withO​(1)O(1)eigenvalues, no matter how large|a−b||a-b|is, preventing‖Oa,b‖\|O_{a,b}\|from decaying and excludingτj,∞z\tau^{z}_{j,\infty}from being LIOMs.
These rare states are exactly the ones that locally resemble an inverted scar state in[a,b][a,b](i.e. withMnM_{n}eigenvalue 1 for the largestnnin[a,b][a,b]), whose fraction goes to zero as|a−b|→∞|a-b|\to\infty.
Intuitively, instead of the nonlocal terms in the expansion (94) being smaller and smaller, they are instead more and more “inactive”. That is, they are relevant only when rarer and rarer long-range inverted scarring happens.
We interpret this as a non-conventional notion of locality (a related concept of “small-plus-large” operators is used in Ref.[97]).
It will be interesting to see how the common analytical results of MBL based on the assumption of having a complete set of LIOMs change if we modify the notion of locality in this way, but a concrete formalism is out of the scope of this paper.

## VConsequences for several studied models

In this section, we go beyond the solvable limit and discuss the possible consequences of our findings for three previously studied quasiperiodic models.
Two examples will be the many-body consequences in the single-particle critical phases: the Fibonacci quasicrystal and the extended Aubry-André-Harper (EAAH) model.
The third example will be the consequence in the localized (non-critical) phase of the interacting Aubry-André (AA) model, due to the existence of rare mirror regions.
Since these models are not in the solvable limit, the results in this section will not be rigorous, but will rather be a combination of the heuristic extension from the constructed solvable limit and some speculation on the interplay between structural and accidental resonances.

The mirror centers for a general model are often emergent from the underlying quasiperiodic structure, and these emergent mirror centers may not have a clean hierarchical structure like those in the constructed solvable model, and they may also mix with other structures (such as repetition without mirroring).
Therefore, our rigorous constructions usually cannot be directly applied to the general models.

Instead, we study a particular sitej0j_{0}or regionR0R_{0}in the chain and ask whether it is participating in (hierarchical) mirror resonances, ignoring that they may also participate in other kinds of resonances.
In other words, we regard the HMS as an effective description of some realistic quasiperiodic models.
The mirror centers of these resonances are marked asxnx_{n}(which can either be locations of sites or bonds), so thatj0j_{0}first participates in the resonance aroundx1x_{1}at a short timescale, and then the one aroundx2x_{2}at a longer timescale, and so on.
For each level indexnn, we recursively define the regionRnR_{n}to be the union ofRn−1R_{n-1}and its mirror imageRn−1~\widetilde{R_{n-1}}aroundxnx_{n}.
Then one can generalize the resonance probabilitypnp_{n}discussed in Sec.IVas the probability thatRnR_{n}is contained in a many-body mirror resonance aroundxnx_{n}, thus generalizing the MBC-E and MBC-L phases (with the caveat that the resonances at differentnnmay not be independent and that the region may involve an infinite number of non-mirror resonances as well).Figure 7:Demonstration of the single-particle HMS in (a) the Fibonacci and (b) the EAAH models. The heatmaps show the eigenstates of the models, sorted to mimic Fig.4. The sitej0j_{0}participates in the mirror resonances centered atx1x_{1}tox4x_{4}hierarchically. Brown bars in (a) mark the palindromes centered atxnx_{n}in the Fibonacci word. The lower panel in (b) shows the spatial profile of the absolute values of the hoppings|tj||t_{j}|. The parameters are (a)m=10m=10(L=89L=89),W=5W=5; (b)L=150L=150,α=5−12\alpha=\frac{\sqrt{5}-1}{2},μ=5\mu=5,V=1V=1,ϕ=3.4975648\phi=3.4975648.

## V.1Fibonacci quasicrystal

The Fibonacci quasicrystal[44]can be constructed from theFibonacci wordCmC_{m}, which is a string consisting of two lettersA\mathrm{A}andB\mathrm{B}, constructed as followsC0\displaystyle C_{0}=B\displaystyle=\mathrm{B}(95)C1\displaystyle C_{1}=A\displaystyle=\mathrm{A}Cm\displaystyle C_{m}=Cm−1​Cm−2​for​m≥2\displaystyle=C_{m-1}C_{m-2}\text{ for }m\geq 2

whereCm−1​Cm−2C_{m-1}C_{m-2}denotes concatenation. So the next few terms are:C2\displaystyle C_{2}=AB\displaystyle=\mathrm{AB}(96)C3\displaystyle C_{3}=ABA\displaystyle=\mathrm{ABA}C4\displaystyle C_{4}=ABAAB\displaystyle=\mathrm{ABAAB}C5\displaystyle C_{5}=ABAABABA\displaystyle=\mathrm{ABAABABA}

Note that the length ofCmC_{m}is themmth Fibonacci numberFmF_{m}.
The single-particle 1D Fibonacci quasicrystal with lengthFmF_{m}is then defined by the following hopping and potential, in the notation of Eq. (4) with open boundary conditions:tj=1,Vj={+Wif​(Cm)j=A−Wif​(Cm)j=Bt_{j}=1,\quad V_{j}=\begin{cases}+W&\text{if }(C_{m})_{j}=\mathrm{A}\\
-W&\text{if }(C_{m})_{j}=\mathrm{B}\end{cases}(97)

where(Cm)j(C_{m})_{j}denotes thejjth letter in the stringCmC_{m}.
The infinite Fibonacci quasicrystal is constructed from the finite ones using a procedure similar to that in Sec.III.2.4, whose spectrum has been shown to be singular continuous for allW≠0W\neq 0[40,41,42,43,44].

## V.1.1Origin of the HMS

The HMS in the single-particle Fibonacci model is demonstrated in Fig.7(a).
Such mirror resonances originate from the fact that the Fibonacci words contain longpalindromes, which are substrings that are identical to their reversal.
Indeed, one can show by an inductive argument that everyCm,m≥3C_{m},m\geq 3with the last two letters removed is a palindrome, which we will callPmP_{m}(see, e.g., Ref.[98]).
AsCmC_{m}for largemmitself contains many copies ofCm′C_{m^{\prime}}form′<mm^{\prime}<m, one can see that half of the palindrome itself contains many smaller palindromes, and so on.
Conversely, on an infinite Fibonacci chain, everyCmC_{m}itself is embedded everywhere within someCm′C_{m^{\prime}}with arbitrarily largem′>mm^{\prime}>m, thus forming an HMS to infinity.

There is some difference between the HMS of the Fibonacci model and our constructed solvable model.
Firstly, the would-be “non-resonant regions” themselves contain many mirror resonances, as demonstrated by the multiple peaks in the region to the left ofj0j_{0}in Fig.7(a), as opposed to Fig.4, in which each non-resonant particle only has one peak in the non-resonant region.
Secondly, there are non-mirror structural resonances in this model, as demonstrated by the states near the center of Fig.7(a), which have a unit of four peaks around the sitex4x_{4}and a similar unit of four additional peaks near the left edge of the chain, due to a more complicated repetitive structure of the Fibonacci words.

We remark that an alternative labeling of the sites, called theconumber, has been known to give a cleaner description of the eigenstates in the Fibonacci quasicrystal[99,100,44].
However, it is not obvious whether it can be carried over to our many-body model, as the interaction is local in real space, not in conumber space.

## V.1.2Many-body consequence

To study the many-body consequences, we need to estimate the resonance probabilitypnp_{n}.
Without a clear non-resonant region, it cannot be estimated from some entropy of “LnnrL^{\text{nr}}_{n}” as in the constructed solvable model.
Instead, we note that since this model has no weak bonds, a better approximation is to treat the many-body theory on the palindromePmP_{m}as a mirror-symmetric random MBL studied in Ref.[32], where a generalization to include the freezing/protection effects is presented in AppendixA.
We will give an intuition on how the scaling should be as follows.

Roughly speaking, a many-body resonance (or synchronized oscillation) has a level splitting (or oscillation frequency)ωsync\omega_{\text{sync}}which is exponentially small in the physical length of the resonance, that is, the size|Rn||R_{n}|of the regionRnR_{n}(in some situations it can be smaller than exponential).
For this resonance to be protected, the energy difference between the two oscillating many-body configurations must also be exponentially small.
Unlike the constructed solvable model that uses small error terms in the non-resonant region, in the Fibonacci model, since each site has a potential being either+W+Wor−W-W, any symmetry-breaking term must be of a strength2​W2W.
We will look at how this affects the protection condition around a palindromePmP_{m}.
Inside a palindromePmP_{m}, there is exactly no symmetry-breaking term; outside of it, in general,PmP_{m}can be symmetrically extended to a longer palindromePm′P^{\prime}_{m}, but the pair of sites immediately beyondPm′P^{\prime}_{m}must be different, and thus2​W2Wsymmetry-breaking.
In the analysis below, we call this pair of symmetry-breaking sitesaaanda~\widetilde{a}, the range of mirror resonance frombbtob~\widetilde{b}, and the mirror center to bexx(so that we havea<b<x<b~<a~a<b<x<\widetilde{b}<\widetilde{a}andRn={b~,…,b}R_{n}=\{\widetilde{b},\ldots,b\}).

Two conditions are required for the many-body resonance to be protected.
First, as we can think ofaaanda~\widetilde{a}as introducing a symmetry-breaking tail, in order for the tail to be small enough atbbandb~\widetilde{b}, we roughly requireb−a≳b~−bb-a\gtrsim\widetilde{b}-b.
Secondly, if there is a sitea′a^{\prime}betweenaaandbbthat has a different approximate LIOM configuration froma′~\widetilde{a^{\prime}}, it similarly introduces a symmetry-breaking tail that can affectbbandb~\widetilde{b}.
Hence, we roughly require anO​(b~−b)O(\widetilde{b}-b)number of sites within[a,b][a,b]to have symmetric configurations with their mirror images.
The first condition can always be fulfilled, asRn−1R_{n-1}must be contained near the center ofFmF_{m}with some large enoughmmon the infinite chain, and therefore near the center of a long palindromePm′P^{\prime}_{m}whose center can be chosen asxnx_{n}.
For the second condition, as it requires anO​(|Rn|)O(|R_{n}|)number of approximate LIOMs to be symmetric, it gives apnp_{n}that is exponentially small in|Rn||R_{n}|, which itself grows exponentially withnn.

The above argument strongly suggests that the interacting Fibonacci chain is deep in the MBC-L phase if the potential strength is large enough.
Moreover, it implies that a system size exponential innnis required to see the physical effect ofnnlevels in the hierarchy and that the many-body inverted scars are exponentially rare in the many-body spectrum.
This result is consistent with the small-size numerical observations in Refs.[56,57]that a strongly disordered interacting Fibonacci model behaves mostly like MBL but with rare delocalized dynamics.

Of course, there remains the possibility that accidental resonances always dominate at largenn, driving the system into the ETH phase in the thermodynamic limit.
Ruling out this possibility is at least as difficult as solving the problem of the thermodynamic stability of random MBL, and is therefore out of the scope of this paper.

## V.2Extended Aubry-André-Harper model

The single-particle extended Aubry-André-Harper (EAAH) model is defined by the following hopping and potential, in the notation of Eq. (4):tj\displaystyle t_{j}=1+μ​cos⁡[2​π​α​(j+12)+ϕ]\displaystyle=1+\mu\cos\left[2\pi\alpha\left(j+\frac{1}{2}\right)+\phi\right](98)Vj\displaystyle V_{j}=V​cos⁡(2​π​α​j+ϕ),\displaystyle=V\cos(2\pi\alpha j+\phi),

whereα\alphais an irrational number (commonly chosen to be the golden ratio) andμ,V>0\mu,V>0.
The model is shown to be in the extended phase forμ<1,V<2\mu<1,V<2, the localized phase whenV>2,2​μ<VV>2,2\mu<V, and the critical phase whenμ>1,V<2​μ\mu>1,V<2\mu[45,46,47,48,49,58].

## V.2.1Origin of the HMS

In this subsection, we will give an intuitive argument on how the HMS emerges from the EAAH model.
As we show in the constructed solvable model, the HMS gives rise to singular continuity (or critical phase) in the single-particle case.
Assume that the HMS dominates the critical phase of the EAAH model, and consider an extreme situation whereμ≫V\mu\gg Vin the critical phase; we would conclude that the HMS of the EAAH model should be dominated by the hopping, and we would ignore the effects of the potentialVjV_{j}for simplicity. The intuition is as follows.

First, due to the irrationality ofα\alpha, there will always be a set of approximate mirror-symmetric points oftjt_{j}, which is shown asxix_{i}in Fig.7(b).
The resonant block is achieved by these points.
To achieve the non-resonant blocks, note that whenμ>0\mu>0, there will be arbitrarily weak bonds|tj||t_{j}|in an infinite chain, again due to the irrationality ofα\alpha.
Combining the approximate symmetry point and the weak bonds together, we consider the tunneling of a particle in a regionRRfrom one side to the other across an approximate symmetric point.
The particles will go through several weak bonds (pairs).
Since the symmetric point is not exact, once the detuning of it is larger than the multiplication of the weak bonds (assuming that the multiplication of the bonds in between the pair of the mirror sites is much larger than the weak bond), the particle cannot successfully tunnel to the other end.
Thus,RRcan be considered a non-resonant region. The existence of the non-resonant region is shown in Fig.7(b), where the eigenstate shows mirror resonance associated with the approximate mirror centerx4x_{4}and is almost “cut off” at the weak bonds close to both ends of the chain.
For smaller levels (e.g., levels related tox1,x2x_{1},x_{2}andx3x_{3}), as the “weak bonds” are less weak, the resonant and non-resonant regions become less distinctive.
In the end, the HMS should emerge from iteratively finding the weak bonds and the approximate symmetry points.

As in the Fibonacci model, the “non-resonant regions” themselves contain mirror resonances.
On the other hand, it is more similar to our solvable model in that every level in the HMS contains at least a pair of weak bonds away from the mirror center.

## V.2.2Many-body consequence

A major difference of the EAAH model in the critical phase compared to our constructed solvable model is that
we cannot assume the “non-resonant regions” of the EAAH model to be many-body localized in the interacting case.
Instead, the EAAH model in the critical phase should be roughly viewed as a series of ergodic blocks linked by weak bonds, since the potential is not strong enough for localization compared to the hopping inside one block.
In such a case, the many-body resonance gapsωsync\omega_{\text{sync}}in the resonant regions may not be that small, and the influence of the non-resonant regions may be significantly weaker compared to systems with a background MBL phase, loosening the conditions of the protections.

However, estimating the growth rates ofωsync\omega_{\text{sync}}(and thus the protection conditions) is extremely difficult.
At small sizes, due to the lack of multiple weak bonds, the system essentially behaves like an extended phase occasionally cut off by a few isolated weak bonds.
Even theL=150L=150chain in Fig.7(b) is only barely enough to demonstrate the hierarchical cut-off strengths of the weak bonds.
Therefore, we do not attempt to estimateωsync\omega_{\text{sync}}in the interacting many-body case.

Although we cannot make a strong conclusion here, the above argument suggests that the interacting EAAH model, or possibly some variants of it, may potentially be in the MBC-E phase, or even have an MBME.
This model being in MBC-E is consistent with the small-size numerical findings in Ref.[58](in which the term “MBC” first appears in the literature), as it aligns with the small-size picture of an ETH phase being occasionally cut off by isolated weak bonds.
However, we believe that the non-thermal extended phenomenology observed in Ref.[58]may be more directly explained by the prethermal model in Ref.[22], in which it is called a non-ergodic extended (NEE) regime.
Specifically, since the interaction strength in Ref.[58]is a constant across each bond, the information spreading timescale for a small-size system is expected to be much less suppressed than the particle spreading timescale, the latter being strongly suppressed by the occasional weak hopping terms.
This separation of timescales resembles the one discussed in Ref.[22](although from a different mechanism), which is proposed to be the underlying cause of the NEE phenomenology in small-size numerics.

We remark that having arbitrarily weak bonds is not the only way to avoid the difficult conditions in the protection of many-body resonances.
Models with parent flat bands, such as Ref.[50], can achieve an effective model with arbitrarily weak bonds by having the hopping amplitude almost canceled by symmetry (across different bands).
Therefore, we propose that multi-flat-band models with quasiperiodic modulation may also lead to MBC-E phases and MBMEs.

## V.3Aubry-André model: rare region effects

The single-particle Aubry-André (AA) model is defined by the following hopping and potential, in the notation of Eq. (4):tj=12,Vj=W​cos⁡(2​π​α​j+ϕ),t_{j}=\frac{1}{2},\quad V_{j}=W\cos(2\pi\alpha j+\phi),(99)

whereα\alphais an irrational number (commonly chosen to be the golden ratio) andW>0W>0is called the disorder strength.
The model is shown to be in the localized phase forW>1W>1and the extended phase whenW<1W<1[51,52].
Although it does not have a critical phase in a wide range ofWW444Although there is a critical point atW=1W=1, it does not hold much interest in our context. As the phase boundary is shifted by the interaction, it is unclear whether we still have a stable HMS at the ETH-MBL boundary., in the localized phase, there is a set of fine-tuned points ofα\alpha, or a genericα\alphabut with a measure-zero set of fine-tunedϕ\phi, at which the spectrum becomes purely singular continuous[33,34,35,39].
For the latter case, we call such a fine-tunedϕ\phiarare initial phase, which plays a central role in this subsection.

Although a rare initial phase itself is fine-tuned, its existence implies the occurrence of delocalizedrare regionsin a generic, non-fine-tunedϕ\phiin a long enough chain.
Roughly speaking, an infinite AA chain with a fixed initial phaseϕ\phican locally look like one with any otherϕ′\phi^{\prime}, since translatingjjis equivalent to rotatingϕ\phiby an irrational angle, which can bring it arbitrarily close to any value in[0,2​π)[0,2\pi).
That is, in an infinite AA chain with any initial phase, there exist arbitrarily long regions within which all eigenstates resemble critical states.
This is similar to the existence of arbitrarily long low-disorder rare regions in the Anderson model[1].

In the Anderson case, even if such regions are extremely rare, in the presence of interactions, they lead to profound effects on the thermodynamic stability of MBL, which is called the avalanche instability[81,82,83].
Roughly speaking, the low-disorder region first thermalizes with interactions, and then it acts as a thermal bath to continue thermalizing nearby spins.
In certain situations, this process may continue indefinitely, leading to the thermalization of the entire chain and the thermodynamic instability of MBL.

The avalanche instability of the interacting AA model has been numerically studied in Ref.[84].
The result suggests that, although a small-size AA model appears MBL forW≳2.0W\gtrsim 2.0, if a local thermal seed exists in an infinite AA chain withW≲7.5W\lesssim 7.5, an avalanche will occur and destroy the MBL.
Although Ref.[84]also concludes that there are no asymptotically long thermal regions in the AA model, the result comes from a renormalization group method that does not take into account structural resonances and thus may be inaccurate for the AA model according to our current understanding.
Hence, whether a local thermal seed exists for2.0≲W≲7.52.0\lesssim W\lesssim 7.5to initiate the avalanche remains unknown.

Below, we argue that, due to the existence of rare initial phases, the interacting AA model does contain arbitrarily large delocalized rare regions at the eigenstate level, in which local expectation values are thermal.
However, as different energy eigenstates have such types of rare regions in different places, it is not clear whether they can really lead to avalanche instability.
We also discuss the possibility of rare regions that are common to all eigenstates due to the interplay between structural resonances and accidental resonances.
Although the existence of the latter types of rare regions is more speculative, their existence would very likely imply avalanche instability.
Either way, our results question the common belief that quasiperiodic MBL does not have avalanche instability due to the lack of low-disorder rare regions.

We remark that having an avalanche from a rare region in an AA chain is not the only possibility that may destroy the thermodynamic MBL of the AA model.
It may very well be the case that the ETH-MBL crossover drifts smoothly as we increase system size due to resonances from “common” regions that happen everywhere as the system size grows (as opposed to rare regions that are unlikely to appear until a very large size).

## V.3.1Rare region due to a single mirror center

Before we make the main argument about the rare region due to HMS, we first discuss whether an avalanche may be initiated by a much simpler mechanism—due to a single approximate mirror center. If so, it would be meaningless to discuss the much more complicated rare region due to HMS.

Ref.[32]shows that a single exact mirror center is enough to lead to structural many-body resonances, and an extension of the theory to the symmetric-broken case (see AppendixA) shows that an approximate one can also lead to many-body resonances with a finite probability.
Since an infinitely long AA chain contains an infinite number of arbitrarily good approximate mirror centers, this implies the existence of arbitrarily long many-body resonances around single mirror centers (with the caveat regarding accidental resonances).

However, mirror-type resonances are unlikely to induce avalanches, as information is only mixed between two parts of the system related by mirroring, rather than spreading out.
There remains the possibility that the interplay between such mirror resonances and accidental resonances may thermalize the region near the mirror center, for which we are not able to give a definite answer.
But heuristically, if we think of accidental resonances as a graph in the spin configuration space, it seems unlikely that having a set of additional two-point connections between mirrored configurations can help much with the proliferation of multiple-point connections due to accidental resonances.

A related scenario is theanti-mirror symmetryMBL studied in Ref.[101].
An anti-mirror center is similar to a mirror-symmetry one, except that the potential is flipped.
That is,Vi≈−Vx+iV_{i}\approx-V_{x+i}as opposed to a mirror symmetryVi≈Vx+iV_{i}\approx V_{x+i}.
Ref.[101]shows that in the presence ofexactanti-mirror symmetry at half filling, spin-spin correlators will show correlations between all pairs of sites, not just the mirror pairs, which they interpret as some form of delocalization.
Since approximate anti-mirror centers exist in the AA model as well, this raises the question of whether such “delocalization” may lead to thermalization.
However, we find that their result relies fundamentally on closed systems at exact half-filling.
That is, the correlation ultimately arises from the fact that if we randomly draw a spin configuration at half filling, there is anO​(1/L)O(1/L)correlation between any two sites.
Since there is no such exact-half-filling condition locally in an infinite system, their result does not apply here.

## V.3.2Rare regions due to HMS

Even if a thermal region is unlikely to emerge from a single mirror (or anti-mirror) center, having a hierarchy of mirror centers together changes the story.

The original proof of the existence of a rare initial phase in the single-particle AA model in Ref.[35]is exactly based on the construction of what we call HMS (and is, to the best of our knowledge, the first time that the idea of HMS appears in the context of critical states).
In our language, the intuition behind the construction is that given any sitej0j_{0}, one can adjust the initial phaseϕ\phistep by step so that a sequence of hierarchical mirror centersx1,x2,…x_{1},x_{2},\ldotsappears.
Specifically, at thennth step, we have an initial phaseϕn\phi_{n}that produces the mirror centersx1,…,xnx_{1},\ldots,x_{n}, with an “error tolerance”Δ​ϕn\Delta\phi_{n}such that within[ϕn−Δ​ϕn,ϕn+Δ​ϕn][\phi_{n}-\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}]those mirror centers successfully create resonances betweenj0j_{0}and its mirror pairs.
Then, since there are always arbitrarily good approximate mirror centers over the entire chain, one can choose one of them to bexn+1x_{n+1}, and slightly tune the initial phase with a new tolerance such that[ϕn+1−Δ​ϕn+1,ϕn+1+Δ​ϕn+1]⊆[ϕn−Δ​ϕn,ϕn+Δ​ϕn][\phi_{n+1}-\Delta\phi_{n+1},\phi_{n+1}+\Delta\phi_{n+1}]\subseteq[\phi_{n}-\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}]to makexn+1x_{n+1}a mirror center supporting the resonances betweenj0j_{0}and2​xn+1−j02x_{n+1}-j_{0}, so that the new resonant region covers that fromxnx_{n}, thus continuing the hierarchy.

Now, such a construction of rare initial phases relies only on the fact that (1) there are arbitrarily good single mirror centers in the chain, and (2) the length of mirror resonances can be made arbitrarily long as the mirror center becomes better and better.
Hence, there is a direct generalization to the many-body case (a detailed construction is presented in AppendixB).
However, there is a caveat regarding accidental resonances.
While we have been using arbitrarily weak bonds to avoid accidental resonance in our constructed solvable model, in the AA model, there are no weak bonds. Especially in the moderate disorder regime2.0≲W≲7.52.0\lesssim W\lesssim 7.5of the AA model susceptible to an avalanche, accidental resonances are expected to play an important role.
One way to mitigate the effect of accidental resonances is to have a large spatial separation between different levels in the hierarchy, which is, in some sense, similar to having weak bonds due to the relevant approximate LIOMs only coupled far away via their exponential tails.
In our context of constructing a rare initial phase, this corresponds to making a choice ofxn+1x_{n+1}that avoids the resonant regionRnR_{n}being too close to it, as well as being too close to the boundary of the resonant region related toxn+1x_{n+1}.

Since the interacting AA model does not have weak bonds, the rare initial phases are expected to produce an MBC-L behavior, by a similar argument as in the discussion of the Fibonacci model.
This implies the existence of arbitrarily long MBC-L-like rare regions for an arbitrary initial phase.
Although an MBC-L-like rare region behaves like MBL on average, since there are an infinite number of them, there are almost certainly an infinite number of inverted scar states.
This implies that a generic energy eigenstate of the interacting AA model, no matter how largeWWis, contains arbitrarily long rare regions within which the expectation values of local observables are thermal-like.
However, as the eigenstates inside a rare region have different energies, and since the inverted scar states are rare, it is not clear whether such types of rare regions are relevant to avalanche instability.
Note that the numerical finding in Ref.[27]can be viewed as a very-small-sized version of such a rare region.

Another type of HMS rare region comes from the rare initial phases, which are deliberately constructed to be unstable and are much more likely to lead to an avalanche (if they exist).
Recall that in the construction of a rare initial phase, we actually have some freedom in choosing the mirror centersxn+1x_{n+1}.
Therefore, we may deliberately choose them to be very close to one end ofRnR_{n}, or let the boundary of the resonant region related toxn+1x_{n+1}be close to the other end ofRnR_{n}, or both (see AppendixBfor more details), so that the HMS becomes unstable. That is, accidental resonances dominate structural resonances after some levels.
Although we cannot make a concrete conclusion, it is likely that once configurations not related by mirror symmetry start to resonate due to inadequate boundaries between different levels in the hierarchy, energy levels in the rare regions will start to randomly repel each other, leading to thermalization (of all eigenstates) within the rare region, and therefore the possibility of the onset of an avalanche for2.0≲W≲7.52.0\lesssim W\lesssim 7.5.
Note that this is different from the single-mirror-center scenario, where structural resonances are always between two configurations; here, structural resonances can involve up to2n2^{n}configurations at levelnn, making them more powerful in connecting some otherwise disconnected configuration graphs.

## VIConclusion

We have constructed asymptotically solvable models for both single-particle and many-body critical phases based on the hierarchical mirror structure, a simplification of the real-space structure commonly found in single-particle critical phases, and presented a rigorously controlled perturbation theory.
For the single-particle case, we have proved the singular continuity of the model based on the Cantor set structure of the energy splitting due to the perturbations.
For the many-body case, we have shown that the direct generalization of the singular continuity mechanism leads to the MBC-E phase, while the interaction-induced collective freezing effect leads to a new MBC-L phase that has no non-interacting counterpart.
Although the two phases resemble the familiar ETH and MBL phases, there are rare states that exhibit opposite behaviors compared to the phases in which they are embedded, interpreted as many-body scars and inverted scars, respectively.
Moreover, the two phases can be separated by a finite-TTtransition, interpreted as an MBME.
These results show that the many-body counterpart of the singular continuous spectrum, commonly found in certain types of quasiperiodic models, has different possibilities with rich behaviors due to interactions.

Based on our findings, we revisited the previous numerical results on the effects of interaction in single-particle critical phases.
In particular, we propose that the MBL-like behavior with rare dynamics in the Fibonacci quasicrystal[56,57]can be explained by it being in the MBC-L phase, and the extended-but-nonthermal behavior in the EAAH model[58]can be explained as a small-size manifestation of the MBC-E phase.
We also propose that some EAAH-type quasiperiodic models may have MBMEs similar to our solvable model.
We also revisited the problem of avalanche instability of AA-type quasiperiodic models and proposed that an avalanche may be caused by HMS-type rare regions that locally resemble MBC-L chains, possibly due to an interplay between structural and accidental resonances.
Such rare regions can be viewed as a generalization of the numerical finding in Ref.[27].

Although we only study the HMS in 1D chains, we expect direct generalizations to a more general type of approximate symmetry structure in higher-dimensional quasiperiodic systems (or quasicrystals).
Note that in the higher dimensional projection picture of quasiperiodicity[102,44], the mirror center in the quasiperiodic chains studied in Sec.Vcan be described as the 1D cut going through aC2​vC_{2v}symmetric point in the parent 2D lattice, which has a direct generalization to higher dimensional quasicrystals from a more general class of point-group symmetry of the parent lattice.
One advantage of a higher dimensional hierarchicalmm-fold rotational structure over 1D HMS is that structural resonances in a higher level no longer need to go through a virtual path that visits every bottleneck (e.g. mirror centers) caused by lower levels; hence, we expectωsync\omega_{\text{sync}}to be larger and less prone to symmetry-breaking defects.
Beyond such crystal-like symmetries, there are also structural resonances in quasiperiodic systems caused by approximate repetition without mirroring, which is also known to result in a single-particle singular continuous spectrum[33,34,39], and we also expect a generalization in interacting many-body systems.
For all of the above generalizations, we expect that there may also be two types of corresponding many-body phases: one whose many-body structural resonances are a synchronized version of the single-particle counterpart (resembling MBC-E), and another whose collective freezing effect is too strong such that the structural resonances do not reach infinity except for rare states (resembling MBC-L).

For a quasiperiodic system in general, both structural and accidental resonances exist.
Hence, when interactions are added to a single-particle critical system, there is an additional possibility that the system becomes ETH rather than MBC-L or MBC-E, as considered in this paper, similar to how an Anderson-localized system at low disorder becomes ETH upon adding interaction.
Similarly, when interactions are added to a non-critical system with rare regions, there are possibilities beyond MBL being stable or being destroyed by an avalanche.
Indeed, the numerical results in Ref.[22]suggest that there is also the possibility that a quasiperiodic system thermalizes everywhere from accidental resonances alone.
Combining the above discussion, we propose the following possibilities for the fate in the thermodynamic limit for a general quasiperiodic system with slow dynamics from many-body resonances:
(1) If structural resonances dominate and proliferate everywhere, the system becomes either MBC-L or MBC-E.
(2) If accidental resonances dominate and proliferate everywhere, the system is driven into ETH similar to the prethermal regime of random MBL.
(3) If structural resonances proliferate only in rare regions, but foster the accidental resonances to dominate and spread, the system is driven into ETH similar to the avalanche scenario in random MBL.
(4) If neither structural nor accidental resonances proliferate, the system is thermodynamically MBL.

Beyond common quasiperiodic systems, one may also be interested in realizing an MBC system directly based on our constructed solvable model.
As our construction in Sec.IVis intended to be an existence proof rather than optimizing for realizability, some care must be taken in choosing the types of coupling and the parameters to avoidωsync\omega_{\text{sync}}from being too small, either for numerical or experimental realizations.
We expect that the most promising type of system is probably the one with particle conservation and long-range coupling to move multiple particles at a time, at a low filling fraction, and that the MBC-L to MBC-E transition is probably most easily observed by tuning the chemical potential rather than the temperature.
Also, a higher-dimensional generalization, if realizable, is expected to be more stable against defects/errors from the discussion above.
For the system size issue in numerics due to the Hilbert space size being doubly exponential innn(which happens in normal quasiperiodic systems as well), we propose that some tensor-network-based method with the block structure designed to match the underlying mirror structure may be able to simulate this type of model, with enough levels in the hierarchy to demonstrate the properties.

## Acknowledgements.The authors thank David Long,DinhDuyVu, Laura Shou, Dominic Else, and Tian-Hua Yang for useful discussions.
This work is supported by the Laboratory for Physical Sciences.

## Appendix AFreezing and protection in mirror-symmetric random MBL

In this appendix, we extend the theory of mirror-type many-body resonances in Ref.[32]by including the symmetry-breaking terms, which give a more accurate description of the freezing and protection conditions than the simplified one shown in Fig.1.

We mainly follow Ref.[32]to use a 1D random-field XXZ chain that is mirror symmetric about a bond in the middle, with globally random symmetry-breaking perturbations.
But we will also discuss in the end what will change if we consider models with weak bonds, with non-uniform symmetry-breaking terms, without particle conservation, or with long-range coupling. We also discuss the applicability of this theory in the case of having multiple levels of HMS.

## A.1The model

We start from a random-field XXZ chain with a boundary at the rightH0=14​∑j<c(σjx​σj+1x+σjy​σj+1y+Δ​σjz​σj+1z)+12​∑j≤chj​σjz,H_{0}=\frac{1}{4}\sum_{j<c}\left(\sigma_{j}^{x}\sigma_{j+1}^{x}+\sigma_{j}^{y}\sigma_{j+1}^{y}+\Delta\sigma_{j}^{z}\sigma_{j+1}^{z}\right)+\frac{1}{2}\sum_{j\leq c}h_{j}\sigma_{j}^{z},\\(100)

where the site indexjjis an integer,ccis the right-most site,σjx,y,z\sigma^{x,y,z}_{j}are the Pauli operators at sitejj, andhjh_{j}are independent uniform random numbers in[−W,W][-W,W].
Note that in our context, whether there is a left boundary of the chain does not really matter, and we will keep our notation compatible with either.
We assume the interaction strengthΔ>0\Delta>0and the disorder strengthW>0W>0are enough forH0H_{0}to be MBL (either an infinite-size MBL, if it exists, or a finite-size MBL).
Then we make a mirror copy of this chain around the mirror centerc+12c+\frac{1}{2}to becomeH0~\widetilde{H_{0}}, where the tilde indicates replacing every action on sitejjwith that on the mirror sitej~=2​c−j+1\widetilde{j}=2c-j+1.
Then the two chains are coupled byHcp=14​(σcx​σc~x+σcy​σc~y+Δ​σcz​σc~z),H_{\rm cp}=\frac{1}{4}\left(\sigma_{c}^{x}\sigma_{\widetilde{c}}^{x}+\sigma_{c}^{y}\sigma_{\widetilde{c}}^{y}+\Delta\sigma_{c}^{z}\sigma_{\widetilde{c}}^{z}\right),\\(101)

to become a mirror-symmetric random XXZ chain.
Finally, we add a small symmetric-breaking term throughout the chainHϵ=ϵ2​∑jhj′​σjz,H_{\epsilon}=\frac{\epsilon}{2}\sum_{j}h^{\prime}_{j}\sigma_{j}^{z},(102)

wherehj′h^{\prime}_{j}are again independent uniform random numbers in[−W,W][-W,W].
The full Hamiltonian is thenH=H0+H0~+Hcp+Hϵ.H=H_{0}+\widetilde{H_{0}}+H_{\text{cp}}+H_{\epsilon}.(103)

To describe the mirror resonances of this system, we follow the approach of Ref.[32]to define two effective chains.
The first is theτ\tauchain consisting of the LIOMs ofH0H_{0}andH0~\widetilde{H_{0}}[94,95,96,6]:H0=∑i≤chi​τiz+∑i,j≤cJi​j​τiz​τjz+∑i,j,k≤cJi​j​k​τiz​τjz​τkz+⋯H_{0}=\sum_{i\leq c}h_{i}\tau^{z}_{i}+\sum_{i,j\leq c}J_{ij}\tau^{z}_{i}\tau^{z}_{j}+\sum_{i,j,k\leq c}J_{ijk}\tau^{z}_{i}\tau^{z}_{j}\tau^{z}_{k}+\cdots(104)

andτj~z:=τjz~\tau^{z}_{\widetilde{j}}:=\widetilde{\tau^{z}_{j}}.
The LIOMsτjz\tau^{z}_{j}have exponentially decaying tails in real space within the left/right side of the system according to the localization lengthξ\xi.
The coefficientsJi​j​k​⋯J_{ijk\cdots}also decay exponentially with the largest distance withini,j,k​…i,j,k\ldots.

The second effective chain, theη\etachain, is introduced to combine each symmetric pairτjz\tau^{z}_{j}andτj~z\tau^{z}_{\widetilde{j}}of theτ\tauchain into one site, in order to describe the Hilbert space of the possible mirror resonances of aτ\tauconfiguration.
More specifically, consider aτ\tauconfiguration|S⟩|S\ranglelabeled by theτjz\tau^{z}_{j}eigenvalues(−1)sj,sj=0,1(-1)^{s_{j}},s_{j}=0,1, all of the possible mirror resonant counterparts of the state (no matter whether the oscillations for differentjjare synchronized or not) belong to the subspace that swaps some of the pairssj,sj~s_{j},s_{\widetilde{j}}.
We say that a sitejjisactiveifsj≠sj~s_{j}\neq s_{\widetilde{j}}.
Then the set of configurations of possible mirror resonances from|S⟩|S\ranglecan be described by an effective chain in which each site corresponds to a pair of active sites in theτ\tauchain.
We define the Pauli operators of the effective chain byηjx,y,z\eta^{x,y,z}_{j}, with site labelsjjmatching the active site labels inHLH_{L}.
An eigenvalue±1\pm 1ofηjz\eta^{z}_{j}corresponds tosj=−sj~=±1s_{j}=-s_{\widetilde{j}}=\pm 1.

The task of describing the many-body mirror resonances ofHHis then reduced to finding an effective HamiltonianHeffH_{\text{eff}}in theη\etachain (from the effect of coupling and symmetry breaking), and to finding the integrals of motion in theη\etachain itself.
Given an initial configuration|S⟩|S\rangle, since the set of integrals of motion (IOMs) in theη\etachain describes the pattern of mirror oscillations as time evolves, we can deduce the form of many-body resonances in the originalσ\sigmachain.

## A.2Exact mirror symmetry

Here we briefly review the results of Ref.[32]in the exactly symmetric (ϵ=0\epsilon=0) case.
In the weakly interacting limit (Δ≪1\Delta\ll 1), the LIOMsτjz\tau^{z}_{j}are approximately the occupation numbers of single-particle localized orbitals, from which the effective Hamiltonian of theη\etachain is derived:Heff=∑⟨i​j⟩Ji​jeff​ηiz​ηjz+∑jhjeff​ηjxH_{\text{eff}}=\sum_{\langle ij\rangle}J^{\text{eff}}_{ij}\eta_{i}^{z}\eta_{j}^{z}+\sum_{j}h^{\text{eff}}_{j}\eta_{j}^{x}(105)

where the coefficients scale asJi​jeff∼Δ​e−|i−j|/ξ,hjeff∼e−2​(c−j)/ξ.J^{\text{eff}}_{ij}\sim\Delta e^{-|i-j|/\xi},\quad h^{\text{eff}}_{j}\sim e^{-2(c-j)/\xi}.(106)

This is a transverse field Ising model that is in the paramagnetic (ferromagnetic) phase near (far from) the mirror center.
That is, the IOMs in theη\etachain are approximately{ηjx}j≥j0,{ηiz​ηjz}⟨i​j⟩,j<j0,∏j<j0ηjx,\{\eta^{x}_{j}\}_{j\geq j_{0}},\quad\{\eta^{z}_{i}\eta^{z}_{j}\}_{\langle ij\rangle,j<j_{0}},\quad\prod_{j<j_{0}}\eta^{x}_{j},(107)

withj0j_{0}separating the paramagnetic and ferromagnetic phases.
Note that the IOMs are not all local, as the last one is a string of Pauli operators.
This set of IOMs indicates that the mirror oscillations betweenj0j_{0}andj0~\widetilde{j_{0}}are unsynchronized, while those outside this interval are synchronized.
Moreover, with a fixedO​(1)O(1)ratio of active sites nearj0j_{0}, the width of this unsynchronized region scales asj0~−j0∼−ξ​ln⁡Δ,\widetilde{j_{0}}-j_{0}\sim-\xi\ln\Delta,(108)

and the frequency of the synchronized oscillation scales asωsync∼1Δ|A|​∏j∈Ae−2​(c−j)/ξ\omega_{\text{sync}}\sim\frac{1}{\Delta^{|A|}}\prod_{j\in A}e^{-2(c-j)/\xi}(109)

whereAAis the set of active sites to the left ofj0j_{0}and|A||A|indicates the number of such sites.
This applies to the situation in which there is the leftmost sitebbbeyond which all sites are inactive (otherwiseωsync=0\omega_{\text{sync}}=0), and that there is no large gap of inactive sites betweenbbandb~\widetilde{b}(otherwise there can be more than one paramagnetic region).

Although these results are derived in theΔ≪1\Delta\ll 1limit, andωsync\omega_{\text{sync}}becomes state-dependent beyond that, the numerical results in Ref.[32]suggest that Eq. (109) is the smallest possible frequency among all possible initial states.
On the other hand, the largest possible frequency appears to beωsyncmax∼e−2​(c−b)/ξ,(Δ∼1)\omega^{\text{max}}_{\text{sync}}\sim e^{-2(c-b)/\xi},\quad(\Delta\sim 1)(110)

wherebbis the leftmost active site.
Also, from the synchronization pattern of the numerical results, Eq. (107) still appears to be a good set of IOMs in theΔ∼1\Delta\sim 1regime, withj0j_{0}being very close to the center.
We will assume these behaviors forΔ∼1\Delta\sim 1and that the results below will not be restricted to the weakly interacting regime.

## A.3Collective freezing

Now we consider the effect of the symmetry-breakingHϵH_{\epsilon}term.
Since it leads to an energy differenceϵ2​(hj′−hj~′)\frac{\epsilon}{2}(h^{\prime}_{j}-h^{\prime}_{\widetilde{j}})between two spin configurations related by swapping a pair of active sitesj,j~j,\widetilde{j}, the most important contribution in theη\etachain isHϵeff=∑jhj′⁣eff​ηjz,hj′⁣eff≈ϵ2​(hj′−hj~′),H^{\text{eff}}_{\epsilon}=\sum_{j}h^{\prime\,\text{eff}}_{j}\eta_{j}^{z},\quad h^{\prime\,\text{eff}}_{j}\approx\frac{\epsilon}{2}(h^{\prime}_{j}-h^{\prime}_{\widetilde{j}}),(111)

which turns theη\etachain into a mixed-field Ising model.
The longitudinal field then competes with other terms, with the tendency to turn the IOMs of theη\etachain into singleηz\eta^{z}operators.
Since anηjz\eta^{z}_{j}eigenstate does not superpose the configuration at sitejjandj~\widetilde{j}, they becomenon-resonant.

We consider the two regimes of theη\etachain separately.
In the paramagnetic (unsynchronized) regime, the original LIOMs of singleηx\eta^{x}can be rotated individually toηz\eta^{z}, with the crossover atϵ​W∼hjeff∼ωj.\epsilon W\sim h^{\text{eff}}_{j}\sim\omega_{j}.(112)

That is, the unsynchronized resonances become non-resonant one by one, starting from the one furthest from the mirror center as we increaseϵ\epsilon.
In the ferromagnetic (synchronized) regime, the situation becomes thatHϵH_{\epsilon}competes with the perturbation that lifts the two-fold degeneracy withoutHcpH_{\rm cp}.
AsHcpH_{\rm cp}contributes to the off-diagonal element∼ωsync\sim\omega_{\text{sync}}, andHϵH_{\epsilon}contributes to the diagonal difference, the transition point is estimated to beϵ​W​|A|∼ωsync,\epsilon W\sqrt{|A|}\sim\omega_{\text{sync}},(113)

where the square root comes from the assumption of independenthj′h^{\prime}_{j}.
Forϵ\epsilonlarger than this, the entire synchronized oscillation stops.
We say that the particles arecollectively frozen.
Note that this happens even when some of the sites are resonant at thisϵ\epsilonif we turn off the interaction.
This estimation agrees with the numerical result in the supplemental material of Ref.[32].

## A.4The protection layerFigure 8:Illustration of the protection layer and final LIOM structure near an approximate mirror center in a long MBL chain. (a)–(c) has the same visualization setting as Fig. 2 in Ref.[32], but now there is a third, non-resonant segment separated from the synchronized segment by theprotection layer. (d) The final LIOM structure of the coupled chain, where some of the LIOMs become locally extended.

From the results above, if we fixϵ\epsilonand the density of active sites, and movebb(the first active site) towards the left, eventually the synchronized oscillation will become frozen.
To see this, note thatωsync\omega_{\text{sync}}decays at least exponentially inc−bc-b, while|A||A|only grows linearly, so the crossover point (113) will eventually be reached by increasingc−bc-b.
Therefore, if the system size is infinite or large enough, atypicaleigenstate, which has active sites distributed everywhere in the chain, will not show arbitrarily long many-body mirror resonances around the mirror center.

On the other hand, there are eigenstates where the effective interactionJa​beffJ^{\text{eff}}_{ab}between two neighboring sites⟨a​b⟩\langle ab\ranglein theη\etachain (which can be far away in theτ\tauchain) is so weak that the bond essentially cuts theη\etachain into two independent parts.
In this way, the part to the right of it can have an effective size small enough to produce synchronized oscillations, while the part to the left of it is non-resonant.
The smallness ofJa​beffJ^{\text{eff}}_{ab}corresponds to the condition that all the sites in the interval(a,b)(a,b)in the original chain must be inactive.
We say that the synchronized resonances to the right ofbbareprotectedby the inactivity of the sites between(a,b)(a,b), and the segment(a,b)(a,b)is called theprotection layer.
This is illustrated in Fig.8(a)–(c).

The sizeLprot=b−a+1L_{\text{prot}}=b-a+1of the protection layer can be estimated by the condition thatJa​beff≪ωsyncJ^{\text{eff}}_{ab}\ll\omega_{\text{sync}}(that is, the influence from siteaaand to the left of it is not strong enough to influence the resonance in sitebband to the right of it).
SinceJa​beff∼Δ​e−Lprot/ξJ^{\text{eff}}_{ab}\sim\Delta e^{-L_{\text{prot}}/\xi}, what we need is to estimateωsync\omega_{\text{sync}}.
We can estimate the range ofωsync\omega_{\text{sync}}among all possible states in[b,b~][b,\tilde{b}], with the only condition being thatbbis an active site (this condition ensures that the sizeLres=c−b+1L_{\text{res}}=c-b+1of the resonance region is well defined).
By Eq. (109) we have, forΔ≲1\Delta\lesssim 1andLres≳−ξ2​ln⁡ΔL_{\text{res}}\gtrsim-\frac{\xi}{2}\ln\Deltaexp⁡[−Lres2ξ+ξ4​(ln⁡Δ)2]≲ωsync≲exp⁡[−2​Lresξ].\exp\left[-\frac{L_{\text{res}}^{2}}{\xi}+\frac{\xi}{4}(\ln\Delta)^{2}\right]\lesssim\omega_{\text{sync}}\lesssim\exp\left[-\frac{2L_{\text{res}}}{\xi}\right].(114)

Hence, we have the bound ofLprotL_{\text{prot}}in terms ofLresL_{\text{res}}2​Lres+ξ​ln⁡Δ≲Lprot≲Lres2−(ξ2​ln⁡Δ)2+ξ​ln⁡Δ2L_{\text{res}}+\xi\ln\Delta\lesssim L_{\text{prot}}\lesssim L_{\text{res}}^{2}-\left(\frac{\xi}{2}\ln\Delta\right)^{2}+\xi\ln\Delta(115)

Note that whenLres∼−ξ2​ln⁡ΔL_{\text{res}}\sim-\frac{\xi}{2}\ln\Delta, the upper and lower bounds coincide and become zero.
That is, when the resonance region is just the unsynchronized part, we no longer need the protection layer.

The bounds in Eq. (115) are not always achievable; however,ωsync\omega_{\text{sync}}may itself be too small and below the collective freezing bound (113).
That is,LresL_{\text{res}}itself has an upper bound depending on what type of states we choose between[b,b~][b,\widetilde{b}].
We will estimate two bounds, the “all resonant” boundLresallL^{\text{all}}_{\text{res}}, which is the maximumLresL_{\text{res}}thatallstates between[b,b~][b,\widetilde{b}]can lead to a resonance involving sitebb(as long as there is a suitable protection layer); and the “maximal resonant” boundLresmaxL^{\text{max}}_{\text{res}}, which is the maximumLresL_{\text{res}}that at leastsomestate between[b,b~][b,\widetilde{b}]can lead to a resonance involving sitebb.
To estimateLresallL^{\text{all}}_{\text{res}}, we again use the minimal possibleωsync\omega_{\text{sync}}.
Combining Eqs. (114) and (113), we haveLresall∼(ξ2​ln⁡Δ)2−ξ​ln⁡ϵ,L^{\text{all}}_{\text{res}}\sim\sqrt{\left(\frac{\xi}{2}\ln\Delta\right)^{2}-\xi\ln\epsilon},(116)

where we have dropped some subleading terms.
Similarly, to estimateLresmaxL^{\text{max}}_{\text{res}}, we use the maximal possibleωsync\omega_{\text{sync}}and combine with (113),Lresmax∼−ξ2​ln⁡ϵ.L^{\text{max}}_{\text{res}}\sim-\frac{\xi}{2}\ln\epsilon.(117)

The correspondingLprotL_{\text{prot}}is denoted byLprotmaxL^{\text{max}}_{\text{prot}}Lprotmax∼2​Lresmax+ξ​ln⁡Δ∼ξ​ln⁡Δϵ.L^{\text{max}}_{\text{prot}}\sim 2L^{\text{max}}_{\text{res}}+\xi\ln\Delta\sim\xi\ln\frac{\Delta}{\epsilon}.(118)

## A.5Integrals of motion in the coupled segments

Finally, we describe the structure of the integrals of motion of the final chain near the mirror center, depicted in Fig.8(d).
Note that if the total system size is large compared to any scales (e.g.,Lresmax+LprotmaxL^{\text{max}}_{\text{res}}+L^{\text{max}}_{\text{prot}}) that are influenced by the mirror center, then we can still call them LIOMs.
This is similar to the picture of a stable rare thermal region in a long random MBL chain.
Each integral of motion within the thermal region must be of the same size as the region, but once we go outside the region, the tail decays exponentially, as it does for other LIOMs, making it local in a length scale larger than the size of the thermal region.
We will see that the mirror center we have been considering also “stretches out” the LIOMs, making them non-local up to some scale.

We will go from the mirror center outwards, discussing the structure of each region, measured using the approximate distance from the center:
- •

Less than−ξ2​ln⁡Δ-\frac{\xi}{2}\ln\Delta
In this region, there is no synchronization, so the LIOMs are essentially the same as in the non-interacting case.
That is, they are the occupation numbers of the orbitals, which are even and odd superpositions of the original half-chain orbitals (which may be distorted near the center due to non-perturbative effects).
Each LIOM consists of two peaks here, as depicted in the center part of Fig.8(d).
- •

Between−ξ2​ln⁡Δ-\frac{\xi}{2}\ln\DeltaandLresallL^{\text{all}}_{\text{res}}
In this region, each site may or may not be involved in a resonance, depending on the sites further away from the center.
Therefore, the LIOMs must be “stretched out”.
Moreover, since every configuration can lead to synchronized resonance as long as there is a protection layer outside it, any LIOM operator must involve the entire region on both sides of the mirror centers, as depicted by extended gray regions in Fig.8(d).
- •

BetweenLresallL^{\text{all}}_{\text{res}}andLresmaxL^{\text{max}}_{\text{res}}
This region is similar to the previous case, except that it may be possible to have certain LIOMs that are only peaked on one side of the mirror.
This is due to the possibility that by observing the configuration in this region on one side of the mirror, it may be enough to imply that no resonance can occur here.
Such LIOMs must involve many sites, but the exact form depends on how to combine the original LIOMsτz\tau^{z}, and there is no general way to determine them without knowing the details betweenωsync\omega_{\text{sync}}and the configurations.
They are not depicted in Fig.8(d).
- •

BetweenLresmaxL^{\text{max}}_{\text{res}}andLresmax+LprotmaxL^{\text{max}}_{\text{res}}+L^{\text{max}}_{\text{prot}}
In this region, the LIOMsτj\tau_{j}of the original half-chain remain valid LIOMs (except for being slightly distorted by the perturbation), as they definitely do not involve a mirror resonance.
They are shown in Fig.8(d) as single-peaked LIOMs.
On the other hand, they do control whether the states withinLresmaxL^{\text{max}}_{\text{res}}can resonate, so the stretched-out LIOM does stretch to this region.
- •

BeyondLresmax+LprotmaxL^{\text{max}}_{\text{res}}+L^{\text{max}}_{\text{prot}}
In this region, again, theτj\tau_{j}remain LIOMs. Moreover, no central LIOMs are stretched to here, except for their exponential tails.
This is because the configuration here is never involved in determining whether a configuration can participate in a resonance555Note thatLresmax+LprotmaxL^{\text{max}}_{\text{res}}+L^{\text{max}}_{\text{prot}}is indeed the maximum possibleLres+LprotL_{\text{res}}+L_{\text{prot}}, as smallerLresL_{\text{res}}involving higher-order perturbation ofHcpH_{\text{cp}}will reach the freezing bound more quickly, so will not be able to makeLprotL_{\text{prot}}larger..

## A.6Extension to HMS

The results above have been for a single mirror center, that is, a single level of the HMS.
A simple way to extend to multiple levels is to assume that the LIOMs in theτ\tauchain are not entirely random, but themselves contain some stretched-out LIOMs resulting from the mirror resonances in the lower levels of the HMS.
Intuitively, instead of taking two random LIOM chains and coupling them together, as visualized in Fig.8(a), we are coupling two LIOM chains where the internal structure of each already looks like that of Fig.8(d).
To distinguish different levels, we will now add a subscriptnnto all of the symbols introduced above.

Now, although all of the asymptotic estimates above are for random LIOMs, the tails of the stretched-out LIOMs are also expected to decay exponentially at a distance ofLres,nmax+Lprot,nmaxL^{\text{max}}_{\text{res},n}+L^{\text{max}}_{\text{prot},n}away from the mirror centercnc_{n}.
Hence, we expect that if this radiusLres,nmax+Lprot,nmaxL^{\text{max}}_{\text{res},n}+L^{\text{max}}_{\text{prot},n}aroundcnc_{n}is much smaller than the distance betweencnc_{n}andcn+1c_{n+1}, it makes sense to keep using the above formalism and ask which region of the(n+1)(n+1)th level contains the stretched-out region of thennth level.
For example, if we have[cn−Lres,nmax−Lprot,nmax,cn+Lres,nmax+Lprot,nmax]⊂[cn+1−Lres,n+1all+O​(ξ),cn+1+ξ2​ln⁡Δ−O​(ξ)],\left[c_{n}-L^{\text{max}}_{\text{res},n}-L^{\text{max}}_{\text{prot},n},c_{n}+L^{\text{max}}_{\text{res},n}+L^{\text{max}}_{\text{prot},n}\right]\\
\subset\left[c_{n+1}-L^{\text{all}}_{\text{res},n+1}+O(\xi),c_{n+1}+\frac{\xi}{2}\ln\Delta-O(\xi)\right],(119)

that is, the stretched-out region of thennth level is within the all-resonance region of the(n+1)(n+1)th level (with anO​(ξ)O(\xi)padding to avoid accidental resonances), then we expect the HMS to be stable.
Moreover, since a local configuration in the all-resonant region of leveln+1n+1can participate in the mirror resonance of at least one full configuration of leveln+1n+1, and is frozen in at least one of such configurations, the resonance probabilitypn+1p_{n+1}is nontrivial (neither 0 nor 1), leading to the MBC phenomenology.
Note that as theLprot,n+1L_{\text{prot},n+1}scales at least linearly inLres,n+1L_{\text{res},n+1}, which itself scales at least exponentially innn,pnp_{n}decays at least doubly exponentially innn.
Thus, this model is always deep in the MBC-L phase (we will discuss generalization below, where it is otherwise).

On the other hand, there are many more possible scenarios beyond Eq. (119), which includes the transition from MBC-L to the single particle critical phase (if the LHS goes into the unsynchronized region), to the MBL phase (if it goes outsideLprot,n+1maxL^{\text{max}}_{\text{prot},n+1}.
A detailed study of each of them is outside the scope of this paper.
Also, if theO​(ξ)O(\xi)padding is not enough (due to a lack of general theory on accidental resonances, we cannot give an exact condition on what is “enough”), the effect of accidental resonances may interfere with the mirror resonances, or even take over the dynamics so that the system becomes ETH, a scenario that we will discuss in AppendixBin the context of avalanche instability.

## A.7Generalizations

Here, we consider the generalization beyond the random-field XXZ model symmetric around a bond with global independent symmetric breaking.
To simplify the discussion (as a first approximation), we do not distinguish between random models and the quasiperiodic model in the absence of distinctive features.
In particular, in AppendixBbelow, we will assume that the above results for the random-field XXZ model directly work for the AA model without generalizations.

## A.7.1Existence of weak bonds

The above theory assumes a constant localization lengthξ\xiacross the system, which is not true if the system contains weak bonds (e.g. the EAAH model).
One simple approximation to incorporate weak bonds is to replace the exponential tailsexp⁡(−|i−j|/ξ)\exp(-|i-j|/\xi)in all the discussion above withexp⁡(−d​(i,j))\exp(-\mathrm{d}(i,j)), whered​(i,j)\mathrm{d}(i,j)is some effective distance function that jumps a lot when a weak bond is reached.
Another way to think about it is to treat weak bonds as equivalent to a long distance, in which all “sites” are inactive (or simply have no sites between them).

Either way, the protection conditionJa​beff≪ωsyncJ^{\text{eff}}_{ab}\ll\omega_{\text{sync}}can become much easier to satisfy if there is a weak bond betweenaaandbb, as requiringJa​beffJ^{\text{eff}}_{ab}to be small no longer necessitates the condition that many (dynamical) sites within it are inactive.
Therefore, depending on the scaling of the weakness of the bonds, it becomes possible to realize MBC-E, unlike the constant-ξ\xicase, where it is always MBC-L.
This corresponds to the argument in the main text that the interacting EAAH model can be in the MBC-E phase.

## A.7.2Sharp symmetry breaking

We have assumedHϵH_{\epsilon}to be uniformly random across the entire chain.
Although this is a good model for AA-type quasiperiodic systems (as the error term when we shift the phase is itself a cosine function injj), it is not good for the Fibonacci-type quasiperiodic model, where the potential is exactly mirror symmetric within the palindrome, but becomes anO​(1)O(1)error outside it.
Instead of modeling the error as having a strengthϵ\epsilonacross all sites, it is better to model it as an exponential decay from the edge of the palindrome. That is, (111) is replaced byHϵeff=∑jhj′⁣eff​ηjz,hj′⁣eff∼e(j−je)/ξ,H^{\text{eff}}_{\epsilon}=\sum_{j}h^{\prime\,\text{eff}}_{j}\eta_{j}^{z},\quad h^{\prime\,\text{eff}}_{j}\sim e^{(j-j_{e})/\xi},(120)

withinj>jej>j_{e}, and model the chain as having no symmetry forj≤jej\leq j_{e}.
The results remain mostly the same.

## A.7.3Particle non-conserving systems and long-range hopping

Now we consider the scenario if there is no particle conservation (as in our solvable model) or if there are long-range hoppings.
These two modifications have a similar effect in the sense that nowHcpH_{\rm cp}can move more than one particle at a time.
Suppose the amplitude still follows the decay rate ofξ\xi; one can estimate thatωsync\omega_{\text{sync}}now always follows Eq. (110) (as there is no higher-order-perturbation bottleneck).
This implies thatLresmaxL^{\text{max}}_{\text{res}}andLresallL^{\text{all}}_{\text{res}}no longer have asymptotic separations.

In this case, one can see that our solvable model can be viewed as modeling a subset of LIOMs (with others assumed to be inactive).
To see this, consider a subset of sites near the boundary of the all-resonance region (which plays the role of the resonance region of our solvable model).
Suppose all other sites are inactive, and we run over all possible configurations within the subset.
Due to the lack of asymptotic separation ofLresmaxL^{\text{max}}_{\text{res}}andLresallL^{\text{all}}_{\text{res}}, we expect the corresponding protection layer to intersect with the part outsideLresmaxL^{\text{max}}_{\text{res}}and therefore be non-resonant. Now we take the interaction of all these non-resonant protection layers over the resonance configuration.
The resulting non-resonant degrees of freedom become the non-resonant region of our solvable model.
If we additionally replace those enforced-inactive sites with weak bonds, it reduces exactly to the freezing/protection conditions of our solvable model.

## Appendix BConstruction of rare initial phases in the interacting AA model

In this appendix, we present a construction of the rare initial phase in the interacting AA model mentioned in Sec.V.3.2, at which the system either becomes MBC-L or thermalizes due to accidental resonances.
The derivation is based on the theory of AppendixA, and we will use the approximation that the interacting AA model behaves like a random MBL phase in the absence of HMS.Figure 9:Construction of the rare initial phase that leads to MBC in the AA model. The gray curve is the cosine function from which the AA potentialshjh_{j}are obtained, and the red dots representhjh_{j}. (a) The spatial profile ofhjh_{j}after we have already constructed the approximate mirror pointcnc_{n}for thennth level of the hierarchy, with blue region corresponding to[ϕn−Δ​ϕn,ϕn+Δ​ϕn][\phi_{n}-\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}].
The green ribbons contain the candidates forcn+1c_{n+1}. (b) After adjusting the initial phase, the(n+1)(n+1)th level of the hierarchy is constructed withcn+1c_{n+1}being the approximate mirror point. All lengths and sizes are only for illustration and are not taken from real data.

The construction is done by iteration on the indexnnof the level in the hierarchy.
For eachnn, we construct a sitecnc_{n}and an interval[ϕn−Δ​ϕn,ϕn+Δ​ϕn][\phi_{n}-\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}]so that ifϕ\philies between them, we have a finite HMS up to levelnn, with the approximate mirror center of thennth level being the bondcn,cn+1c_{n},c_{n}+1, with the mirror center being exact ifϕ=ϕn\phi=\phi_{n}.
Additionally, we will have[ϕn+1−Δ​ϕn+1,ϕn+1+Δ​ϕn+1]⊆[ϕn−Δ​ϕn,ϕn+Δ​ϕn][\phi_{n+1}-\Delta\phi_{n+1},\phi_{n+1}+\Delta\phi_{n+1}]\subseteq[\phi_{n}-\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}]for eachnn, leading to the existence ofϕ∞\phi_{\infty}that lies in all of these intervals, producing a true HMS.
This construction is a generalization of the proof in Ref.[35]and works for all quasiperiodic models coming from an even function (such as the cosine in the AA model), not just for the AA.
However, in our case, it is not a rigorous proof due to the possible interplay with accidental rare resonances, over which we do not have full control.

Although there are four local phases of the cosine that can produce a mirror center (and also four that produce an anti-mirror center and also lead to many-body resonances), for simplicity of demonstration, we only use a particular one of them (as depicted in Fig.9).

The choice for the first level can be quite arbitrary.
Picking any sitec1c_{1}, we have aϕ1\phi_{1}at whichc1+1/2c_{1}+1/2is an exact mirror center.
Then we can pick an arbitraryΔ​ϕ1<π\Delta\phi_{1}<\pito form the first interval[ϕ1−Δ​ϕ1,ϕ1+Δ​ϕ1][\phi_{1}-\Delta\phi_{1},\phi_{1}+\Delta\phi_{1}].
Note that for anyϕ\phiin this interval, we have the corresponding length scalesLres,1allL^{\text{all}}_{\text{res},1},Lres,1maxL^{\text{max}}_{\text{res},1}, andLprot,1maxL^{\text{max}}_{\text{prot},1}as defined in Sec.A.4, which all go to infinity atϕ1\phi_{1}, so picking a phase toleranceΔ​ϕ1\Delta\phi_{1}corresponds to fixing the set of minimal length scales at which resonances can occur in the first level.

Next, we constructcn+1c_{n+1}givencnc_{n}and[ϕn−Δ​ϕn,ϕn+Δ​ϕn][\phi_{n}-\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}].
This is depicted in Fig.9, where the entire blue region in Fig.9(a) indicates the area wherehcnh_{c_{n}}andhcn+1h_{c_{n}+1}lie whenϕ∈[ϕn−Δ​ϕn,ϕn+Δ​ϕn]\phi\in[\phi_{n}-\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}].
Note that we again have the minimum length scalesLres,nallL^{\text{all}}_{\text{res},n},Lres,nmaxL^{\text{max}}_{\text{res},n}, andLprot,nmaxL^{\text{max}}_{\text{prot},n}over which resonances in thennth level can occur.
However, in order to construct the next level, we also need to fix a maximum resonance length scale; otherwise, there is no bound on where the next mirror center can be placed.
To do this, we carve out the middle half of the interval so that whenϕ∈[ϕn−Δ​ϕn,ϕn−34​Δ​ϕn]∪[ϕn+34​Δ​ϕn,ϕn+Δ​ϕn]\phi\in[\phi_{n}-\Delta\phi_{n},\phi_{n}-\frac{3}{4}\Delta\phi_{n}]\cup[\phi_{n}+\frac{3}{4}\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}], the length scaleLres,nmax+Lprot,nmaxL^{\text{max}}_{\text{res},n}+L^{\text{max}}_{\text{prot},n}has an upper boundLnboundL^{\text{bound}}_{n}.
The corresponding area wherehcnh_{c_{n}}andhcn+1h_{c_{n}+1}lie is shown in dark blue in Fig.9(a).
Now in the region ofj>cn+1+Lnboundj>c_{n}+1+L^{\text{bound}}_{n}orj<cn−Lnboundj<c_{n}-L^{\text{bound}}_{n}(we additionally need to skip over a distance ofO​(ξ)O(\xi)to avoid accidental resonances, but we do not know how to rigorously control it), we search for a candidate ofcn+1c_{n+1}.
The case forj>cn+1+Lnbound+O​(ξ)j>c_{n}+1+L^{\text{bound}}_{n}+O(\xi)is shown in Fig.9(a), where the candidate region is indicated as green ribbons aligned with the dark blue region.
The key is that there is definitely going to be a pair ofhjh_{j}andhj+1h_{j+1}lying in the interior of the green ribbons due to the irrationality of the sampled points.
By shifting the phase slightly, we can make that pair become an exact mirror center, as shown in Fig.9(b), which becomes the mirror centercn+1,cn+1+1c_{n+1},c_{n+1}+1of the next level.
Note that this also makesϕn+1∈(ϕn−Δ​ϕn,ϕn−34​Δ​ϕn)∪(ϕn+34​Δ​ϕn,ϕn+Δ​ϕn)\phi_{n+1}\in(\phi_{n}-\Delta\phi_{n},\phi_{n}-\frac{3}{4}\Delta\phi_{n})\cup(\phi_{n}+\frac{3}{4}\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}), so all of the previous bounds are satisfied.

To constructΔ​ϕn+1\Delta\phi_{n+1}, we note that there is always a closed interval containingϕn+1\phi_{n+1}in whichϕ\phiis still in(ϕn−Δ​ϕn,ϕn−34​Δ​ϕn)∪(ϕn+34​Δ​ϕn,ϕn+Δ​ϕn)(\phi_{n}-\Delta\phi_{n},\phi_{n}-\frac{3}{4}\Delta\phi_{n})\cup(\phi_{n}+\frac{3}{4}\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}).
In addition, there is also one containingϕn+1\phi_{n+1}in which Eq. (119) is satisfied.
That is, the entire region nearcnc_{n}where the LIOM structure is stretched out is within the all-resonance region nearcn+1c_{n+1}.
This means that all resonances in thennth level can participate in the(n+1)(n+1)th level as long as the configuration outside it satisfies the protection layer condition (again, we may need to add additionalO​(ξ)O(\xi)padding to avoid accidental resonances).

Without the effect of accidental resonances, the system at the rare initial phase is expected to be in MBC-L, as explained in AppendixA.
However, it remains possible that accidental resonances drive the system towards ETH.
In particular, in each iteration of the construction above, there is some freedom to choose how large theO​(ξ)O(\xi)distance we need to skip over when finding the next mirror center, and how large the additional padding we add in Eq. (119); inadequate padding will lead to accidental resonances between non-mirror configurations.
That is, more combinations of configurations are allowed to resonate, not just the exact mirrored one, so the effective probability of resonancepnp_{n}becomes larger, driving the system towards ETH.

Another way to think of the possibility of an avalanche is that “rare initial phases become common” due to accidental resonances.
During the construction of the rare initial phase, after we chooseϕn+1\phi_{n+1}, the possible choice ofΔ​ϕn+1\Delta\phi_{n+1}may become larger if the “all resonance” requirement also includes accidental non-mirror resonances.
Due to this effect, it may happen that the intervals[ϕn−Δ​ϕn,ϕn+Δ​ϕn][\phi_{n}-\Delta\phi_{n},\phi_{n}+\Delta\phi_{n}]do not converge to a single point asn→∞n\to\infty, but to an interval full of “rare” initial phases, which would mean that all initial phases give resonances up to infinity, thus delocalizing the entire chain.

## References
- Anderson [1958]P. W. Anderson,Phys. Rev.109, 1492 (1958).
- Nandkishore and Huse [2015]R. Nandkishore and D. A. Huse,Annu. Rev. Condens. Matter
Phys.6, 15 (2015).
- Abaninet al.[2019]D. A. Abanin, E. Altman,
I. Bloch, and M. Serbyn,Rev. Mod. Phys.91, 021001 (2019).
- Sierantet al.[2025]P. Sierant, M. Lewenstein,
A. Scardicchio, L. Vidmar, and J. Zakrzewski,Reports
on Progress in Physics88, 026502 (2025).
- Huseet al.[2014]D. A. Huse, R. Nandkishore, and V. Oganesyan,Phys. Rev. B90, 174202 (2014).
- Imbrieet al.[2017]J. Z. Imbrie, V. Ros, and A. Scardicchio,Annalen der Physik529, 1600278 (2017).
- Baskoet al.[2006]D. M. Basko, I. L. Aleiner,
 and B. L. Altshuler,Annals of physics321, 1126 (2006).
- Oganesyan and Huse [2007]V. Oganesyan and D. A. Huse,Phys. Rev. B75, 155111 (2007).
- Žnidaričet al.[2008]M. Žnidarič, T. Prosen, and P. Prelovšek,Phys. Rev. B77, 064426 (2008).
- Pal and Huse [2010]A. Pal and D. A. Huse,Phys. Rev. B82, 174411 (2010).
- Devakul and Singh [2015]T. Devakul and R. R. P. P. Singh,Phys. Rev. Lett.115, 187201 (2015).
- Imbrie [2016a]J. Z. Imbrie,Journal of Statistical Physics163, 998 (2016a).
- Imbrie [2016b]J. Z. Imbrie,Phys. Rev. Lett.117, 027201 (2016b).
- Vidalet al.[2002]J. Vidal, D. Mouhanna, and T. Giamarchi,Phys. Rev. B - Condens. Matter Mater. Phys.65, 142011 (2002).
- Iyeret al.[2013]S. Iyer, V. Oganesyan,
G. Refael, and D. A. Huse,Phys.
Rev. B - Condens. Matter Mater. Phys.87, 134202 (2013),1212.4159.
- Mastropietro [2015]V. Mastropietro,Phys. Rev. Lett.115, 180401 (2015).
- Khemaniet al.[2017a]V. Khemani, D. N. Sheng,
 and D. A. Huse,Phys. Rev. Lett.119, 075702 (2017a).
- Xuet al.[2019]S. Xu, X. Li, Y.-T. Hsu, B. Swingle, and S. Das Sarma,Phys. Rev. Research1, 032039 (2019).
- Vuet al.[2022]D. Vu, K. Huang, X. Li, and S. Das Sarma,Phys. Rev. Lett.128, 146601 (2022).
- Longet al.[2023a]D. M. Long, P. J. D. Crowley, V. Khemani, and A. Chandran,Phys. Rev. Lett.131, 106301 (2023a).
- Longet al.[2023b]D. M. Long, D. Hahn, M. Bukov, and A. Chandran,SciPost Phys.15, 251
(2023b).
- Tuet al.[2024]Y.-T. Tu, D. M. Long, and S. Das Sarma,Phys. Rev. B109, 214309 (2024).
- Colboiset al.[2024]J. Colbois, F. Alet, and N. Laflorencie,Phys. Rev. B110, 214210 (2024).
- Hahnet al.[2025]D. Hahn, D. M. Long,
M. Bukov, and A. Chandran,“Predicting
dynamics from flows of the eigenstate thermalization hypothesis,”(2025),arXiv:2504.01073 [quant-ph].
- Vanoniet al.[2026]C. Vanoni, D. M. Long, and A. Chandran,“Resonance
proliferation across localization transitions,”(2026),arXiv:2605.05445
[cond-mat.dis-nn].
- Padhanet al.[2026]A. Padhan, J. Colbois,
F. Alet, and N. Laflorencie,Phys. Rev.
Lett.136, 197101
(2026).
- Faulendet al.[2026]B. Faulend, H. Buljan, and A. Štrkalj,“Uncovering
the microscopic mechanism of slow dynamics in quasiperiodic many-body
localized systems,”(2026),arXiv:2603.28721 [cond-mat.dis-nn].
- Gopalakrishnanet al.[2015]S. Gopalakrishnan, M. Müller, V. Khemani,
M. Knap, E. Demler, and D. A. Huse,Phys.
Rev. B92, 104202
(2015).
- Khemaniet al.[2017b]V. Khemani, S. P. Lim,
D. N. Sheng, and D. A. Huse,Phys. Rev. X7, 021013 (2017b).
- Garrattet al.[2021]S. J. Garratt, S. Roy, and J. T. Chalker,Phys. Rev. B104, 184203 (2021).
- Crowley and Chandran [2022]P. Crowley and A. Chandran,SciPost Phys.12, 201 (2022).
- Liet al.[2026]Z.-J. Li, Y.-T. Tu, and S. Das Sarma,Phys. Rev. B113, L180204 (2026).
- Gordon [1976]A. Y. Gordon, Uspekhi Matematicheskikh Nauk31, 257 (1976).
- Avron and Simon [1982]J. E. Avron and B. Simon,Bulletin of the American Mathematical
Society6, 81 (1982).
- Jitomirskaya and Simon [1994]S. Jitomirskaya and B. Simon,Communications in Mathematical Physics165, 201 (1994).
- Hofet al.[1995]A. Hof, O. Knill, and B. Simon, Communications in mathematical
physics174, 149
(1995).
- Koslover [2005]D. A. Koslover,Letters in Mathematical Physics71, 123 (2005).
- Jitomirskaya [2019]S. Jitomirskaya, Current developments in mathematics2019, 1 (2019).
- Jitomirskaya and Zhang [2021]S. Jitomirskaya and S. Zhang,Journal of the European Mathematical Society24, 1723 (2021).
- Kohmotoet al.[1983]M. Kohmoto, L. P. Kadanoff, and C. Tang,Phys. Rev. Lett.50, 1870 (1983).
- Sütő [1987]A. Sütő,Communications in Mathematical Physics111, 409 (1987).
- Sütő [1989]A. Sütő, Journal of statistical physics56, 525 (1989).
- Damaniket al.[2016]D. Damanik, A. Gorodetski,
 and W. Yessen,Inventiones mathematicae206, 629 (2016).
- Jagannathan [2021]A. Jagannathan,Rev. Mod. Phys.93, 045001 (2021).
- Hatsugai and Kohmoto [1990]Y. Hatsugai and M. Kohmoto,Phys. Rev. B42, 8282 (1990).
- Hanet al.[1994]J. H. Han, D. J. Thouless,
H. Hiramoto, and M. Kohmoto,Phys. Rev. B50, 11365 (1994).
- Takadaet al.[2004]Y. Takada, K. Ino, and M. Yamanaka,Phys. Rev. E70, 066203 (2004).
- Liuet al.[2015]F. Liu, S. Ghosh, and Y. D. Chong,Phys. Rev. B91, 014108 (2015).
- Avilaet al.[2017]A. Avila, S. Jitomirskaya,
 and C. A. Marx,Inventiones mathematicae210, 283 (2017).
- Kumaret al.[2026]M. Kumar, I. M. Khaymovich, and A. Sharma,“Inapplicability of avila’s theory in the diamond chain with
quasiperiodic disorder,”(2026),arXiv:2603.12362 [cond-mat.str-el].
- Aubry and André [1980]S. Aubry and G. André, Ann. Israel Phys. Soc3, 18 (1980).
- Harper [1955]P. G. Harper,Proceedings of the Physical Society. Section
A68, 874 (1955).
- Hiramoto [1990]H. Hiramoto,Journal of the Physical Society of Japan59, 811 (1990).
- Hiramoto and Kohmoto [1992]H. Hiramoto and M. Kohmoto,International Journal of Modern Physics B6, 281 (1992).
- Settinoet al.[2020]J. Settino, N. W. Talarico, F. Cosco,
F. Plastina, S. Maniscalco, and N. Lo Gullo,Phys. Rev. B101, 144303 (2020).
- Macéet al.[2019]N. Macé, N. Laflorencie,
 and F. Alet,SciPost Phys.6, 050 (2019).
- Varma and Žnidarič [2019]V. K. Varma and M. Žnidarič,Phys. Rev. B100, 085105 (2019).
- Wanget al.[2021]Y. Wang, C. Cheng,
X.-J. Liu, and D. Yu,Phys. Rev. Lett.126, 080602 (2021).
- Deutsch [1991]J. M. Deutsch,Phys. Rev. A43, 2046 (1991).
- Srednicki [1994]M. Srednicki,Phys. Rev. E50, 888 (1994).
- Moriet al.[2018]T. Mori, T. N. Ikeda,
E. Kaminishi, and M. Ueda,Journal
of Physics B: Atomic, Molecular and Optical Physics51, 112001 (2018).
- Deutsch [2018]J. M. Deutsch,Reports on Progress in Physics81, 082001 (2018).
- Bernienet al.[2017]H. Bernien, S. Schwartz,
A. Keesling, H. Levine, A. Omran, H. Pichler, S. Choi, A. S. Zibrov, M. Endres, M. Greiner,
V. Vuletić, and M. D. Lukin,Nature551, 579
(2017).
- Shiraishi and Mori [2017]N. Shiraishi and T. Mori,Phys. Rev. Lett.119, 030601 (2017).
- Serbynet al.[2021]M. Serbyn, D. A. Abanin,
 and Z. Papić,Nature Physics17, 675 (2021).
- Chandranet al.[2023]A. Chandran, T. Iadecola,
V. Khemani, and R. Moessner,Annual Review of Condensed Matter
Physics14, 443
(2023).
- Srivatsaet al.[2020]N. S. Srivatsa, R. Moessner,
 and A. E. B. Nielsen,Phys. Rev. Lett.125, 240401 (2020).
- Iversenet al.[2022]M. Iversen, N. S. Srivatsa, and A. E. B. Nielsen,Phys. Rev. B106, 214201 (2022).
- Chen and Zhu [2024]Q. Chen and Z. Zhu,Phys. Rev. B109, 014212 (2024).
- Srivatsaet al.[2023]N. S. Srivatsa, H. Yarloo,
R. Moessner, and A. E. B. Nielsen,Phys. Rev. B108, L100202 (2023).
- De Roecket al.[2016]W. De Roeck, F. Huveneers,
M. Müller, and M. Schiulaz,Phys. Rev. B93, 014203 (2016).
- Huanget al.[2024]K. Huang, D. Vu, S. Das Sarma, and X. Li,Phys. Rev. B109, 174214 (2024).
- Pawliket al.[2024]K. Pawlik, P. Sierant,
L. Vidmar, and J. Zakrzewski,Phys. Rev. B109, L180201 (2024).
- Liet al.[2015]X. Li, S. Ganeshan,
J. H. Pixley, and S. Das Sarma,Phys. Rev. Lett.115, 186601 (2015).
- Setiawanet al.[2017]F. Setiawan, D.-L. Deng,
 and J. H. Pixley,Phys. Rev. B96, 104205 (2017).
- Hsuet al.[2018]Y.-T. Hsu, X. Li, D.-L. Deng, and S. Das Sarma,Phys. Rev. Lett.121, 245701 (2018).
- Liet al.[2016]X. Li, J. H. Pixley,
D.-L. Deng, S. Ganeshan, and S. Das Sarma,Phys.
Rev. B93, 184204
(2016).
- Ghoshet al.[2020]S. Ghosh, J. Gidugu, and S. Mukerjee,Phys. Rev. B102, 224203 (2020).
- Tuet al.[2023a]Y.-T. Tu, D. Vu, and S. Das Sarma,Phys. Rev. B108, 064313 (2023a).
- Iadecola and Schecter [2018a]T. Iadecola and M. Schecter,Phys. Rev. B98, 144204 (2018a).
- Thieryet al.[2018]T. Thiery, F. m. c. Huveneers, M. Müller,
 and W. De Roeck,Phys. Rev. Lett.121, 140601 (2018).
- Morningstaret al.[2022]A. Morningstar, L. Colmenarez, V. Khemani,
D. J. Luitz, and D. A. Huse,Phys. Rev. B105, 174205 (2022).
- Sels [2022]D. Sels,Phys. Rev. B106, L020202 (2022).
- Tuet al.[2023b]Y.-T. Tu, D. Vu, and S. Das Sarma,Phys. Rev. B107, 014203 (2023b).
- Hofstadter [1976]D. R. Hofstadter,Phys. Rev. B14, 2239 (1976).
- Artusoet al.[1992]R. Artuso, G. Casati, and D. Shepelyansky,Phys. Rev. Lett.68, 3826 (1992).
- Piéchon [1996]F. Piéchon,Phys. Rev. Lett.76, 4372 (1996).
- Schulz-Baldes and Bellissard [1998]H. Schulz-Baldes and J. Bellissard,Reviews in Mathematical Physics10, 1 (1998).
- Reed and Simon [1980]M. Reed and B. Simon,Methods of Modern Mathematical
Physics: Functional analysis, Methods of Modern
Mathematical Physics, Vol. 1 (Academic Press, 1980).
- Eggarter [1974]T. P. Eggarter,Phys. Rev. B9, 2989 (1974).
- Griffiths and Kaufman [1982]R. B. Griffiths and M. Kaufman,Phys. Rev. B26, 5022 (1982).
- Shahet al.[2026]J. Shah, L. Shou, J. Shuler, and V. Galitski,Phys. Rev. X16, 021020 (2026).
- Iadecola and Schecter [2018b]T. Iadecola and M. Schecter,Phys. Rev. B98, 144204 (2018b).
- Serbynet al.[2013]M. Serbyn, Z. Papić, and D. A. Abanin,Phys. Rev. Lett.111, 127201 (2013).
- Roset al.[2015]V. Ros, M. Müller, and A. Scardicchio,Nuclear Physics B891, 420 (2015).
- Chandranet al.[2015]A. Chandran, I. H. Kim,
G. Vidal, and D. A. Abanin,Phys.
Rev. B91, 085425
(2015).
- Yanget al.[2026]T.-H. Yang, S. Gopalakrishnan, and D. A. Abanin,“Simple slow operators and quantum thermalization,”(2026),arXiv:2604.13172 [quant-ph].
- Fici [2015]G. Fici,“Factorizations of the fibonacci infinite word,”(2015),arXiv:1508.06754
[cs.FL].
- Ashraff and Stinchcombe [1988]J. A. Ashraff and R. B. Stinchcombe,Phys. Rev. B37, 5723 (1988).
- Macéet al.[2016]N. Macé, A. Jagannathan,
 and F. Piéchon,Phys. Rev. B93, 205153 (2016).
- Klosset al.[2023]B. Kloss, J. C. Halimeh,
A. Lazarides, and Y. Bar Lev,Nature Communications14, 3778 (2023).
- Duneau and Katz [1985]M. Duneau and A. Katz,Phys. Rev. Lett.54, 2688 (1985).

## 


- 


Major funding support from
