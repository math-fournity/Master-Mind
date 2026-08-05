# Uncertainty quantification in mechanics: A unified Bayesian perspective

**arXiv ID**: 2607.18734v1
**Authors**: Sascha Ranftl, Malte Rolf, Gerhard A. Holzapfel, Ellen Kuhl
**Published**: 2026-07-21
**Categories**: physics.comp-ph, physics.data-an, stat.ME, stat.ML
**HTML URL**: https://arxiv.org/html/2607.18734v1

## Abstract

Uncertainty quantification (UQ) is essential to experimental mechanics, but has become particularly relevant in computational mechanics, manifesting in two fundamental problem types: forward and inverse problems. The former addresses how input uncertainties propagate to the quantities of interest, whereas the latter aims to infer unknown parameters from experimental observations or simulations. Since efficient propagation typically requires a prohibitive number of evaluations to compute marginal output distributions, the development of fast, data-driven surrogate models becomes necessary. Thus, we can distinguish between two inverse tasks: (i) the identification and calibration of input uncertainties, and (ii) the construction of surrogates, a methodology collectively referred to as surrogate-based UQ. Building on probabilistic reasoning and the concept of partial belief, we demonstrate that Bayesian probability theory provides a unified theoretical framework for addressing both problem types. We further show that Bayesian inference allows for the seamless incorporation of essential subproblems, including model selection for identifying the most probable model specifications and experimental design for optimizing data collection by identifying experiments or simulations that maximize expected information gain about parameters, among others such as connections to sensitivity analysis or the use of special priors like random fields. While this theoretical framework is presented for general mechanical problems, particular emphasis is placed on biomechanics, where variability and uncertainty is especially pronounced due to inherent biological heterogeneity, patient-specific variability, and noisy data.

## Full Text

Uncertainty quantification in mechanics: A unified Bayesian perspective

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
- License: CC BY 4.0arXiv:2607.18734v1 [physics.comp-ph] 21 Jul 2026

[1,2]\fnmSascha\surRanftl

1]\orgdivCourant Institute of Mathematical Sciences,\orgnameNew York University,\orgaddress\cityNew York City,\stateNY,\countryUSA

2]\orgdivDivision of Applied Mathematics,\orgnameBrown University,\orgaddress\cityProvidence,\stateRI,\countryUSA

3]\orgdivInstitute of Applied Mechanics,\orgnameFriedrich-Alexander-Universität Erlangen-Nürnberg,\orgaddress\cityErlangen,\countryGermany

4]\orgdivInstitute of Biomechanics,\orgnameGraz University of Technology,\orgaddress\cityGraz,\countryAustria

5]\orgdivDepartment of Structural Engineering,\orgnameNorwegian University of Science and Technology (NTNU),\orgaddress\cityTrondheim,\countryNorway

6]\orgdivDepartment of Mechanical Engineering,\orgnameStanford University,\orgaddress\cityStanford,\stateCA,\countryUSA

## Uncertainty quantification in mechanics:
A unified Bayesian perspectivesranftl@purdue.edu\fnmMalte\surRolf\fnmGerhard A.\surHolzapfel\fnmEllen\surKuhl[[[[[[

## Abstract

Uncertainty quantification (UQ) is essential to experimental mechanics, but has become particularly relevant in computational mechanics, manifesting in two fundamental problem types: forward and inverse problems. The former addresses how input uncertainties propagate to the quantities of interest, whereas the latter aims to infer unknown parameters from experimental observations or simulations. Since efficient propagation typically requires a prohibitive number of evaluations to compute marginal output distributions, the development of fast, data-driven surrogate models becomes necessary. Thus, we can distinguish between two inverse tasks: (i) the identification and calibration of input uncertainties, and (ii) the construction of surrogates, a methodology collectively referred to as surrogate-based UQ.
Building on probabilistic reasoning and the concept of partial belief, we demonstrate that Bayesian probability theory provides a unified theoretical framework for addressing both problem types.
We further show that Bayesian inference allows for the seamless incorporation of essential subproblems, including model selection for identifying the most probable model specifications and experimental design for optimizing data collection by identifying experiments or simulations that maximize expected information gain about parameters, among others such as connections to sensitivity analysis or the use of special priors like random fields.
While this theoretical framework is presented for general mechanical problems, particular emphasis is placed on biomechanics, where variability and uncertainty is especially pronounced due to inherent biological heterogeneity, patient-specific variability, and noisy data.

## keywords:uncertainty quantification, inverse analysis, Bayesian inference, surrogate modeling, machine learning, random fields

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

## 1Introduction

The integration of uncertainty quantification (UQ) has become indispensable to the fields of experimental and computational mechanics alike. As computational models increasingly inform engineering design and safety-critical decisions, deterministic output predictions are no longer sufficient. Instead, ensuring the reliability and robustness of simulation results requires a rigorous assessment of how input uncertainties, such as material properties, geometry, and boundary conditions, propagate through mechanical systems to affect the quantities of interest.

Biomechanical systems represent a prime example of where these uncertainties become most apparent. While physics-based mathematical models have substantially advanced our understanding of complex biomechanical systems, such as cardiovascular, respiratory, or cerebral physiology, their typically deterministic nature struggles to account for patient-specific variability, inherent biological heterogeneity, and noisy data. Collectively, these limitations remain a significant bottleneck for clinical translation.

In particular, two key challenges in the clinical application of biomechanical models persistEck et al. [2016]. First, quantifying uncertainty when adapting model inputs to patient-specific conditions is inherently difficult, as available data are often uncertain, incomplete, or noisy. Second, a persistent trade-off between model complexity and input uncertainty requires balancing errors introduced by model simplifications against those arising from uncertain parameters. Although many computational models aim to support clinical decision-making and accelerate medical device development, this potential remains only partially realized despite substantial progress over the past decade, largely due to the lack of a consistent framework.

Together, these challenges motivate a unified theoretical framework for UQ. Indeed, Bayesian probability theory has been mathematically proven as the unique, consistent approach for inference under uncertaintyCox [1946], Sivia and Skilling [2006]. By treating probability as a measure of partial belief, this theory provides a rigorous foundation to explicitly quantify all uncertainty sources, including noisy data, missing information, and uncertain models, while naturally incorporating prior knowledge. Building on these probabilistic principles, we demonstrate that Bayesian theory effectively addresses the two primary problem types: (i)forward problemsand (ii)inverse problems, with many practical cases involving a combination of both, as shown in Fig.1.Figure 1:Overview of surrogate-based uncertainty quantification by propagating uncertainty from input to output and addressing the two inverse problems involved.

Forward problems in UQ refer to quantifying how uncertainties in the model inputs affect the uncertainty in a model output or quantity of interest. For instance, one may ask:What is the uncertainty in a particular Cauchy stress component at a certain point in the aorta wall due to uncertainties in the parameters of our constitutive model?Thus, we seek topropagateuncertainty from the model inputs to the output. Indeed, it will soon become apparent that uncertainty propagation often involves solving inverse problems for two distinct practical purposes: (i) quantification of the input uncertainty and (ii) surrogate modeling.

The termquantification of the input uncertainty, whether based on experimental data or on medical data in biomechanics, may require a parameter estimation problem for the constitutive model before uncertainty propagation can commence. It is therefore often referred to asmodel calibrationand can also be reformulated as anoptimization problem. Similar to before, one may ask:What are the most likely value and associated uncertainties for the stiffness parameter of a constitutive model, given a set of, say, uniaxial tension tests?The estimated parameters, which link the measured experimental quantities to the parameters of interest, can then serve as input for computational simulations to propagate these uncertainties through the model.

The termsurrogate modelingrequires further explanation. In order to propagate uncertainty, we need a sufficient number of samples to compute themarginal probabilityof the model output. We obtain this marginal probability by integrating the joint probability with respect to the model input parameters.
In biomechanics, however, obtaining a single model output for one specific parameter set can demand hours, days, or even weeks of computational time. Unfortunately, reliable statistical estimates of model output uncertainty typically require thousands to millions of samples. This issue arises directly from the convergence behavior of numerical integration techniques used to evaluate the marginal probability (cf. Wollner et al.Wollner et al. [2025]).

Nevertheless, not all hope is lost. A common remedy is the use of a surrogate model, also known as anemulatorormeta-model, which provides a fast, data-driven approximation of the original model.

Constructing such a surrogate follows a standard three-step procedure. This involves (i) generating a manageable dataset of model outputs by solving the original model for selected input parameter samples, (ii) fitting a parameterized function to these simulations to form the surrogate, and (iii) using this surrogate in place of the original model to efficiently approximate the marginal probability or output uncertainty.
In essence, we have demonstrated that the forward UQ task frequently incorporates the inverse problem of identifying surrogate parameters. The surrogate should (i) approximate the original model as accurately and faithfully as possible so that the resulting uncertainty estimates remain meaningful and statistically significant, even with limited data, and (ii) be inexpensive and fast to evaluate, so that the computation becomes practically feasible.

In this review article, we show that Bayesian probability theory provides the unifying theoretical framework, that incorporates all these problems and concepts into a single coherent whole.
For this purpose, we begin by introducing the concepts of logic of belief and partial truth in Section2. We then propose a workflow for UQ in Section3, ranging from inverse problems, namely model calibration and parameter estimation as well as surrogate modeling, to uncertainty propagation. Building on this foundation, we review popular surrogate models and selected alternatives and discuss model selection within the Bayesian framework in Section4. Next, we introduce Bayesian experimental design and provide a brief excursion into Bayesian optimization for inverse design in Section6. This is followed by a brief exposition of the connection to sensitivity analysis in Section7. It shows that sensitivity analysis can be understood as a special case and interpretation of the foregoing Bayesian theory, including a Bayesian generalization of Sobol’ indices. We conclude with the introduction of random fields for heterogeneous materials modeling as a special statistical prior within the Bayesian theory in Section8. While many topics are accompanied by illustrative mechanical examples, detailed computational aspects and sampling methods are only briefly touched upon, as they remain beyond the scope of this review article.

## 2The logic of belief and partial truth

Here, we introduce probability theory as an extension of Aristotelianlogic. Aristotle’s logic is formalized through logical statements calledpropositions(A,B,C,…A,B,C,\ldots).

For example, letAAdenote the propositionA≡A\equiv‘Julius Caesar was left-handed.’ Its negation,¬A\neg A, would then mean¬A≡\neg{A}\equiv‘Julius Caesar was not left-handed.’ Other propositions might include:B≡B\equiv‘Julius Caesar was right-handed’ andC≡C\equiv‘Julius Caesar was ambidextrous.’ New propositions can be formed by combining existing ones with logical operations. The logical AND operation (∧\wedge) yields statements such asA∧BA\wedge B, meaningA∧B≡A\wedge B\equiv‘Julius Caesar was left-handed and right-handed.’ which is logically equivalent toA∧B≡A\wedge B\equiv‘Julius Caesar was ambidextrous≡C\equiv C.’ Likewise, the logical OR operation (∨\vee) allows combinations likeA∨BA\vee B, meaningA∨B≡A\vee B\equiv‘Caesar was left- or right-handed.’ In fact, the logical OR is already one concept more than strictly necessary, since De Morgan’s law allows it to be expressed in terms of negation and conjunction:¬(A∨B)=¬A∧¬B\neg(A\vee B)=\neg A\wedge\neg B.

Propositions can take one of two logical values:trueorfalse. For instance, consider the statementA≡A\equiv‘Julius Caesar was left-handed.’ If this proposition is true, its negation must necessarily be false. Thus,A=True⟹¬A=FalseA=\text{True}\implies\neg A=\text{False}andvice versaA=False⟹¬A=TrueA=\text{False}\implies\neg A=\text{True}. Importantly, bothAAand its negation¬A\neg Acannot be true at the same time. That is, the compound statementA∧¬A≡A\wedge\neg A\equiv‘Julius Caesar was left-handed and not left-handed’ is false regardless of which is option is actually true. In Boolean algebra, the logical valuetrueis conventionally represented by the number11, andfalseby the number0. Hence, ifA=1A=1, then its negation satisfies¬A=0\neg A=0; equivalently,A=1⟹¬A=0A=1\implies\neg A=0. The conjunction of two propositions,C≡A∧BC\equiv A\wedge B, is true only when bothAAandBBare true. In other words, the statement ‘Caesar was left- and right-handed’ can only be true if both statements — ‘Caesar was left-handed’ and ‘Caesar was right-handed’ — are true. By contrast, the proposition, or disjunction (logical OR), ‘Caesar was left- or right-handed’ is true if either (or both) of the statements is true. Formally,A=1⟹A∨B=1A=1\implies A\vee B=1, and, independently,B=1⟹A∨B=1B=1\implies A\vee B=1. The possible combinations of truth values for propositions and their logical operations can be conveniently summarized using truth tables, see Table1.Table 1:Truth table according to Boolean (Aristotelian)logic.AABBA∧BA\wedge BA∨BA\vee B1001010111110000

Propositions can also be conditioned on other propositions, denoted by the vertical bar (∣\mid). For example,A∣B=1A\mid B=1is read as ‘AAis true givenBBis true,’ ‘AAis true on the condition thatBBis true,’ or simply ‘AAis trueifBBis true.’ In our running example, this corresponds to the statement ‘Caesar was left-handed, assuming that he was right-handed.’ In essence, aconditionspecifies a prerequisite that is taken to be true before evaluating the truth of another proposition. Within the above truth table, conditioning onB=1B=1means restricting our attention to those rows whereBBis fixed at11. In other words, we consider only the second and third rows, whereBBis true, and assess the truth value ofAAunder that condition.

We will shortly see how Bayesian probability theory extends Boolean logic, in which a proposition iseithertrue (11) or false (0), to allow any real value in between. Such values can be interpreted aspartial truthsor as a degree ofbeliefin the truthfulness of a given proposition. In fact, it was mathematically proven by CoxCox [1946], and later presented in a more modern formulation inGarrett [1998], Sivia and Skilling [2006], that under certain natural assumptions111Specifically, Cox assumed that (i) degrees of belief are represented by real numbers, (ii) the system reduces to classical logic in the deterministic limit, and (iii) reasoning is internally consistent, i.e., equivalent inference paths yield identical results. Under these desiderata, the probability calculus is the unique solution., the probability calculus is, up to a constant exponent, the unique and only consistent extension of logic to partial truths. In this sense, the fundamental laws of probability arise directly from the requirements of logical consistency. They emerge naturally from Boolean algebraJaynes [2003], von Toussaint [2011], von der Linden et al. [2014].

LetP​(A)P(A)denote the probability, or degree of belief, that the propositionAAis true. Let a belief of11correspond to certainty, and a belief of0to impossibility. In principle, any other numerical representation could have been chosen forcertaintyortruth; the present choice is simply the most convenient. Logical consistency requires that eitherAAor its negation¬A\neg Amust be true, and conversely, that both cannot be true at the same time, i.e.,P​(A∨¬A)=1,P​(A∧¬A)=0,\displaystyle P(A\vee\neg A)=1\;,\quad P(A\wedge\neg A)=0\;,(1)

where these relations capture the most fundamental constraints of Boolean logic.

CoxCox [1946], building on Boole’s work, identified six basic properties of logic: (i) double negation:¬(¬A)=A\neg(\neg A)=A; (ii) commutativity:A∧⁣∨B=B∧⁣∨AA\mathbin{{\wedge}\mkern-2.0mu{\vee}}B=B\mathbin{{\wedge}\mkern-2.0mu{\vee}}A; (iii) idempotence: stating a proposition twice is equivalent to stating it once,A∧⁣∨A=AA\mathbin{{\wedge}\mkern-2.0mu{\vee}}A=A; (iv) associativity:A∧⁣∨(B∧⁣∨C)=(A∧⁣∨B)∧⁣∨CA\mathbin{{\wedge}\mkern-2.0mu{\vee}}(B\mathbin{{\wedge}\mkern-2.0mu{\vee}}C)=(A\mathbin{{\wedge}\mkern-2.0mu{\vee}}B)\mathbin{{\wedge}\mkern-2.0mu{\vee}}C; (v) De Morgan’s law:¬(A∧⁣∨B)=¬A∨⁣∧¬B\neg(A\mathbin{{\wedge}\mkern-2.0mu{\vee}}B)=\neg A\mathbin{{\vee}\mkern-2.0mu{\wedge}}\neg B; and (vi) absorption:A∧⁣∨(A∨⁣∧B)=AA\mathbin{{\wedge}\mkern-2.0mu{\vee}}(A\mathbin{{\vee}\mkern-2.0mu{\wedge}}B)=A, where∧⁣∨\mathbin{{\wedge}\mkern-2.0mu{\vee}}and∨⁣∧\mathbin{{\vee}\mkern-2.0mu{\wedge}}denotes two possible alternatives of each axiom using, consistently, either the first or second symbol each. In other words, each of the axioms: (ii) to (vi), has two equivalent variants.
Cox argued that these basic requirements of logical consistency must also hold for partial truths. For example, the law of double negation,¬(¬A)=A\neg(\neg A)=A, implies that the corresponding degree of belief satisfiesP​(¬(¬A))=P​(A)P(\neg(\neg A))=P(A), or formally,¬(¬A)=A⟹P​(¬(¬A))=P​(A)\neg(\neg A)=A\implies P(\neg(\neg A))=P(A). He further introduced theprinciple of transitivity: If we believe more strongly inAAthan inBB, and more inBBthan inCC, then we must also believe more strongly inAAthan inCC; formally,(P​(A)>P​(B))∧(P​(B)>P​(C))⟹P​(A)>P​(C)\big(P(A)>P(B)\big)\wedge\big(P(B)>P(C)\big)\implies P(A)>P(C).

Based on these logical axioms, Cox derived the so-calledsum ruleandproduct rulewithout assuming any particular functional form. This derivation relies on two key assumptions: (i) different paths of logical reasoning given the same context𝒦\mathcal{K}must lead to the same conclusions, and (ii) the probability of a statement being true is directly related to the probability of its negation. The resulting expressions are the sum rule,P​(A∧B∣𝒦)\displaystyle P(A\wedge B\mid\mathcal{K})=P​(A∣𝒦)+P​(B∣𝒦)\displaystyle=P(A\mid\mathcal{K})+P(B\mid\mathcal{K})−P​(A∨B∣𝒦),\displaystyle\hphantom{=}\,\,-P(A\vee B\mid\mathcal{K})\;,(2)

and the product rule,P​(A∧B∣𝒦)=P​(A∣B,𝒦)​P​(B∣𝒦).\displaystyle P(A\wedge B\mid\mathcal{K})=P(A\mid B,\mathcal{K})P(B\mid\mathcal{K})\;.(3)

Here,P​(A∣B,𝒦)P(A\mid B,\mathcal{K})denotes the belief thatAAis true, given that statementBBis assumed to be true and given context𝒦\mathcal{K}. For complete proofs, the interested reader is referred to related literatureCox [1946], Garrett [1998], Knuth and Skilling [2012].

These two rules (Eqs. (2) and (3)) form the mathematical foundation of Bayesian probability theory and provide a consistent framework for reasoning under uncertainty. To apply them meaningfully, however, one must always specify the context or background information𝒦\mathcal{K}on which the probabilities are conditioned.
In any given problem, including those in the broad field of mechanics, there is always some background information available, at the very least in the form of the problem definition. This context is not a mere formality. It implies that (i) there is no such thing as anunconditional probabilityand (ii) omitting relevant background knowledge often leads to inconsistent reasoning.
In our earlier discussion of Caesar’s dexterity, the background information implicitly included the assumptions that Caesar existed and that he was a human with two hands. To illustrate the importance of such context, let us now consider a different example. Suppose we analyze the preferred hand of the Hindu deity Vishnu, who is often depicted with four arms.
Counting clockwise and starting at an arbitrary arm, let us define the propositionAi≡A_{i}\equiv‘Vishnu’s preferred arm was numberii,’ wherei=1,2,3,4i=1,2,3,4. Then, by basic deductive logic, we have¬A1=A2∨A3∨A4\neg A_{1}=A_{2}\vee A_{3}\vee A_{4}, or more generally¬Ai=⋁j≠iAj\neg A_{i}=\bigvee_{j\neq i}A_{j}forj=1,2,3,4j=1,2,3,4. This leads to four equationsP​(Ai∣𝒦)+P​(¬Ai∣𝒦)=1P(A_{i}\mid\mathcal{K})+P(\neg A_{i}\mid\mathcal{K})=1, and consequently,∑iP​(Ai∣𝒦)=1\sum_{i}P(A_{i}\mid\mathcal{K})=1. We see that thecontext𝒦\mathcal{K}of either Caesar or Vishnu substantially changes the analysis. In the probability-theoretic literature, this context𝒦\mathcal{K}is often denoted in the formp​(A∣𝒦)p(A\mid\mathcal{K})with an explicit conditional complex of propositions. For the remainder of this exposition, we will omit the explicit denotation of this context, the reader however be advised that probabilities are nevertheless and always conditional on context.

As introduced above, Bayesian probability theory is formulated in terms of propositions, to which it assigns a non-negative measure of truth calledprobability. Unlike in Boolean algebra, propositions are not limited to being either true or false, but may take any value in between. In this way, Bayesian probability theory extends inductive logic to situations involving uncertainty, where probabilities represent degrees of belief rather than absolute truth values.
In contrast to frequentist statistics, this concept of probability is not an intrinsic property of a system or object that arises from the relative frequency of occurrence of a proposition in an experiment repeatedad infinitum. Instead, it expresses a subjective degree of belief in a proposition, conditioned on the available information. Different observers, having access to different information, may therefore reach different conclusions. However, consistency requires that observers who possess the same or equivalent information must arrive at the same conclusions. Together, this principle of consistency, along with the sum and product rules, forms the logical foundation of Bayesian inference and determines how beliefs should be updated as new information becomes available.

By combining the rules of logical consistency for partial truths, we arrive at the central relationships of Bayesian reasoning. Using the sum rule, we can immediately derive from Eq. (1) the intuitive resultP​(A∨¬A)=P​(A)+P​(¬A)=1P(A\vee\neg A)=P(A)+P(\neg A)=1. Another basic intuition, and one of Cox’s axioms mentioned before, suggests that our belief in the statementA∧BA\wedge Bshould yield the exact same truth value as the logically equivalent reversed statementB∧AB\wedge A. Formally:A∧B=B∧A⇒P​(A∧B)=P​(B∧A)A\wedge B=B\wedge A\Rightarrow P(A\wedge B)=P(B\wedge A). From this point forward, we adopt notation that is more common in the contemporary literature and denote the logical AND (∧\wedge) with a comma (,), so thatP​(A,B)≡P​(A∧B)P(A,B)\equiv P(A\wedge B). Applying the product rule Eq. (3), and, carelessly, omitting the context𝒦\mathcal{K}, we immediately arrive at the well-knownBayes’ theorem,P​(A,B)\displaystyle P(A,B)=P​(B,A)\displaystyle=P(B,A)=P​(A∣B)​P​(B)\displaystyle=P(A\mid B)P(B)=P​(B∣A)​P​(A).\displaystyle=P(B\mid A)P(A)\;.(4)

Bayes’ theorem expresses how our belief in a propositionAAshould be updated when new informationBBbecomes available. The termP​(A)P(A)represents theprior probability, quantifying our degree of belief inAAbefore observingBB. The termP​(B∣A)P(B\mid A)is thelikelihood, describing how compatible the new informationBBis with the assumption thatAAis true. The updated belief, orposterior probability, is given byP​(A∣B)P(A\mid B), which combines prior knowledge with new information through the normalization factorP​(B)P(B), known as theevidence. In this way, Bayes’ theorem provides a consistent and logically grounded method for learning from data.

Evaluating the normalization termP​(B)P(B)typically requires accounting for all mutually exclusive possibilities under whichBBcould occur. This is achieved through themarginalization rule, which ensures that probabilities remain consistent when integrating over unknown or unobserved variables. From the sum and product rules above, and using the law of negation (Eq. (1)), we obtain the marginalization rule in its simplest form,P​(B)\displaystyle P(B)=P​(B,A∨¬A)=P​(B,A)+P​(B,¬A)\displaystyle=P(B,A\vee\neg A)=P(B,A)+P(B,\neg A)=P​(B∣A)​P​(A)+P​(B∣¬A)​P​(¬A).\displaystyle=P(B\mid A)P(A)+P(B\mid\neg A)P(\neg A)\;.(5)

The marginalization rule generalizes naturally to a set of mutually exclusive and exhaustive propositionsBiB_{i}, whereBi∧Bj=0B_{i}\wedge B_{j}=0for alli≠ji\neq j, withi,j=1,…,Ni,j=1,\ldots,Nand⋁i=1NBi=1\bigvee_{i=1}^{N}B_{i}=1; that is, no two propositionsBjB_{j}can be true simultaneously, and the disjunction of all propositions is surely true,P​(A)=∑i=1NP​(A,Bi)=∑i=1NP​(A∣Bi)​P​(Bi).\displaystyle P(A)=\sum_{i=1}^{N}P(A,B_{i})=\sum_{i=1}^{N}P(A\mid B_{i})P(B_{i})\;.(6)

Moreover, the marginalization rule can also be extended to continuous propositionsa,b,ca,b,c, where the propositionaaexpresses ‘aahas value in[amin,amax][a_{\rm min},a_{\rm max}],’ ora∈[amin,amax]a\in[a_{\rm min},a_{\rm max}]. For continuous variables, the probability of a specific value becomes infinitesimally smallWollner et al. [2026]. In this case, the notion of probability is generalized toprobability density functions(PDF), denotedp​(a)p(a). The continuous form of the marginalization rule is thenp​(a)\displaystyle p(a)=∫p​(a∣b)​p​(b)​db.\displaystyle=\int p(a\mid b)p(b)\,\mathrm{d}b\;.(7)

Together, the marginalization rule and Bayes’ theorem provide all necessary tools for reasoning and computation with probabilities222Note the distinction between a random variable, an abstract quantity ranging over possible values, and its realization, the concrete value observed in a particular instanceWollner et al. [2026]., or what we may call thecalculus of uncertainties. Indeed, either the pair of the sum and product rules, or the pair of Bayes theorem (Eq. (2)) and the marginalization rule (Eq. (6)), are the only two rules we need to remember to do Bayesian inference.

## 3Uncertainty quantification

Bayesian probability theory provides a robust framework for quantifying information and characterizing uncertainty across diverse contexts. It enables us to perform statistical inference, make controlled approximations, and switch seamlessly between forward and inverse problems. Furthermore, it allows for the analysis of how uncertainties interact within coupled physical models, even when informed by heterogeneous and noisy datasets.
Remarkably, models for data analysis and UQ are built upon just two fundamental rules: (i) Bayes’ theorem and (ii) the marginalization rule.

To implement this framework effectively, we follow a structured workflow for UQ, as illustrated in Fig.2. The following sections adhere strictly to the notation and logic established in this process.Figure 2:Typical workflow for uncertainty quantification in mechanics.
An experiment provides input-output data pairs(𝝃,yexp)(\bm{\xi},y_{\rm exp}), which are used for model calibration and parameter estimation (inverse problem I), yielding uncertain parameters of a constitutive model𝒙\bm{x}. These uncertain parameters then serve as uncertain inputs to a computer simulation to predict uncertain outputs. Because such simulations are often computationally expensive, their sparse input–output data pairs(𝒙,y)(\bm{x},y)are often used to train the parameters of a surrogate model𝜽\bm{\theta}(inverse problem II) that replaces the computer simulation. In the final step, the uncertainties in the constitutive parameters — and, if applicable, in the surrogate model itself — are propagated from inputs to outputs using this fast surrogate approximation.
The workflow is flexible: a surrogate may be unnecessary in some cases, and it can equally accommodate related experiments or coupled simulations without changing the formalism; see, e.g.,Avril et al. [2008], where constitutive parameters are calibrated from finite element simulations of image-based extension tests, reversing the roles of experiment and simulation.

## 3.1Uncertainty propagation

In the workflow of UQ, the core objective of uncertainty propagation can be formulated as:

Quantification of how input uncertainties propagate through a computational model to yield a predictive PDF for the quantity of interest, or a summary proxy such as the variance thereof.

## 3.1.1General concept

We first introduce (surrogate-based) uncertainty propagation in a Bayesian frameworkHaylock [1997], O’Hagan et al. [1999], Kennedy and O’Hagan [2000], Oakley and O’Hagan [2002], O’Hagan [2006], Ranftl and von der Linden [2021].
LetD∈ℕD\in\mathbb{N}denote the number of uncertain parameters. Moreover, we define𝒙=(x1,…,xD)T∈𝒳\bm{x}=(x_{1},\ldots,x_{D})^{\rm T}\in\mathcal{X}as the vector of uncertain parameters or random variables within the parameter space𝒳\mathcal{X}and lety=y​(𝒙)y=y(\bm{x})333Note thatyyhere simultaneously plays the role of a random variable, a function of𝒙\bm{x}, and a realization thereof. We keep this simplified notation to avoid further overloading an already extensive formalism, and expect the intended meaning to remain clear from context., whose image𝒴\mathcal{Y}represents the set of all possible values ofyy, represent the quantity of interest.
Following the notation inJaynes [2003], von der Linden et al. [2014], the fundamental object that we are interested in, and that fully describes the uncertainty, is the probability (density) foryy, denoted asp​(y),\displaystyle p(y)\;,(8)

and the probability for𝒙\bm{x}, denoted asp​(𝒙).\displaystyle p(\bm{x})\;.(9)

Per the marginalization rule (Eq. (7)), these two quantities are related as follows,p​(y)=∫𝒙∈𝒳p​(y∣𝒙)​p​(𝒙)​d𝒙,\displaystyle p(y)=\int_{\bm{x}\in\mathcal{X}}p(y\mid{\bm{x}})p({\bm{x}})\,\mathrm{d}\bm{x}\;,(10)

whered​𝒙\mathrm{d}{\bm{x}}denotes integration with respect to the volume measure (the “infinitesimal volume element”) on𝒳\mathcal{X}.
In the forward problem, where the uncertainty is propagated from the parameters𝒙\bm{x}to the quantity of interestyy, the main task is marginalization, since it allows us to obtain the probability foryyby integrating over the uncertain inputs𝒙{\bm{x}}, i.e., averaging over all possible parameter values weighted by their probabilities. In the inverse problem, however, where we infer the probability for𝒙\bm{x}from the probability foryy, we rely on Bayes’ theorem.

Having established the most general framework, we now turn to how uncertainty is commonly represented and interpreted in practical application in the field of mechanics. While the complete description of uncertainty is provided by the probabilityp​(y)p(y), it is often more convenient to express uncertainty through simplified statistical summary measures or proxies derived from this probability. Alas, researchers often interpretuncertaintyin a narrower sense, typically associating it with thevariance. In fact, this narrow notion of uncertainty is merely derived from the underlying probability, as will become apparent after defining these quantities below.

Let us first introduce the expected value, which represents the average or mean value ofyy, weighted by its probability. The expected value is commonly denoted by⟨⋅⟩\big\langle\cdot\big\rangleor𝔼​[⋅]\mathbb{E}[\cdot]. Here, we follow the latter notation, and the expectation value ofyyis defined as𝔼​[y]=∫y∈𝒴y​p​(y)​dy.\displaystyle\mathbb{E}[y]=\int_{y\in\mathcal{Y}}yp(y)\>\mathrm{d}y\;.(11)

Next, we introduce the variance ofyy, commonly denoted asvar​[y]\mathrm{var}[y],𝔼​[(y−𝔼​[y])2]\mathbb{E}[(y-\mathbb{E}[y])^{2}], or𝕍​[y]\mathbb{V}[y], which measures the spread or dispersion of possible outcomes around the mean. Often referred to colloquially as theuncertaintyofyy, it is defined asvar​[y]=∫y∈𝒴(y−𝔼​[y])2​p​(y)​dy.\displaystyle\mathrm{var}[y]=\int_{y\in\mathcal{Y}}\big(y-\mathbb{E}[y]\big)^{2}p(y)\>\mathrm{d}y\;.(12)

These two quantities, the expectation and the variance, provide statistical metrics for describing uncertainty in a compact form. This reduction is however one-directional, as infinitely many distributions can share the same mean and variance. In mechanics, UQ is therefore often understood as the computation of the integral in Eq. (12). While the probabilityp​(y)p(y)holdsallinformation about the uncertainty by capturing all possible outcomes and their likelihoods, the variance offers a simplified statistical measure that summarizes this information into a single scalar quantity. This simplification is often pragmatic, since computing the probabilityp​(y)p(y)using the marginalization rule (Eq. (10)) can be significantly more involved than evaluating the variancevar​[y]\mathrm{var}[y]through Eq. (12), which is to be shown now.

Having defined these simple statistical measures, we now turn to the practical question of how to computevar​[y]\mathrm{var}[y]when prior knowledge about the input parameters𝒙\bm{x}is available. This knowledge about𝒙\bm{x}is described by the probabilityp​(𝒙)p(\bm{x}). However, the probabilityp​(𝒙)p(\bm{x})does not appear explicitly in Eq. (12). Furthermore, the computational model outputyyis typically defined only as a function of the inputs,y=y​(𝒙)y=y(\bm{x}). To incorporate the probabilityp​(𝒙)p(\bm{x})into Eq. (12), we apply the marginalization rule as in Eq. (10) and rearrange the terms as follows𝔼​[y]\displaystyle\mathbb{E}[y]=∫𝒙∈𝒳∫y∈𝒴y​p​(y∣𝒙)​p​(𝒙)​d𝒙​dy,\displaystyle=\int_{\bm{x}\in\mathcal{X}}\int_{y\in\mathcal{Y}}y\,p\big(y\bm{\mid}\bm{x}\big)p\big(\bm{x}\big)\>\mathrm{d}{\bm{x}}\>\mathrm{d}y\;,(13)var​[y]\displaystyle\mathrm{var}[y]=∫𝒙∈𝒳∫y∈𝒴(y−𝔼​[y])2​p​(y∣𝒙)\displaystyle=\int_{\bm{x}\in\mathcal{X}}\int_{y\in\mathcal{Y}}\Big(y-\mathbb{E}[y]\Big)^{2}p\big(y\bm{\mid}\bm{x}\big)×p​(𝒙)​d​𝒙​d​y.\displaystyle\hphantom{=}\,\,\times p\big(\bm{x}\big)\>\mathrm{d}{\bm{x}}\>\mathrm{d}y\;.(14)

In the following, we will discuss the aspects and components of Eq. (14) one by one, namely the likelihood and the prior, as already introduced in Eq. (2). Henceforth, for the sake of notational simplicity and clarity, integrals are understood to be taken over the appropriate parameter or state space, with domains omitted unless stated otherwise.

## 3.1.2The likelihood

Thelikelihood, or the conditional probability in Eq. (10),p​(y∣𝒙)p(y\mid\bm{x}), represents, in the context of experimental mechanics, themeasurement noise of the instrumentwheny​(𝒙)y(\bm{x})is obtained from a mechanical experiment such as a uniaxial tensile test. Suppose this noiseη\etais additive and Gaussian444Noise can also be non-additive and non-Gaussian, alas this model is a default choice and particularly convenient.. Then, we can writey=f​(𝒙)+η,η∼𝒩​(0,σ2),y=f(\bm{x})+\eta\;,\quad\eta\sim\mathcal{N}(0,\sigma^{2})\;,(15)

where𝒩​(μ,σ2)\mathcal{N}(\mu,\sigma^{2})denotes a normal distribution with meanμ=0\mu=0and varianceσ2\sigma^{2}. This impliesy∣𝒙∼𝒩​(f​(𝒙),σ2).y\mid\bm{x}\sim\mathcal{N}(f(\bm{x}),\sigma^{2})\;.(16)

In other words, the likelihood quantifies how closely the measured data cluster around the prediction of the forward modelf​(𝒙)f(\bm{x}).
Ify​(𝒙)y(\bm{x})instead comes from solving a computational model, we distinguish two cases: (i)deterministicmodels, where the same input always yields the same output — here, the likelihood is effectively a Dirac delta centered atf​(𝒙)f(\bm{x}); and (ii)stochasticmodels, where randomness is inherent to the simulation — thenp​(y∣𝒙)p(y\mid\bm{x})again becomes a proper probability distribution, just like in the experimental setting.

In the first case, when the computational model is deterministic, the outputyyis uniquely defined by the input parameters𝒙\bm{x}. Indeed, most models in computational mechanics fall into this category: even if the inputs contain random parameters, once a specific realization of𝒙\bm{x}is fixed, the resulting outputyyis fully determined.
In probabilistic terms, this means the likelihoodp​(y∣𝒙)p(y\mid\bm{x})simplifies and assigns all its probability to the single value predicted by the model. That is, the likelihood is zero everywhere except aty=y​(𝒙)y=y(\bm{x}), where it takes its entire probability mass. Formally,p​(y∣𝒙)={1,if​y=y​(𝒙),0,otherwise.\displaystyle p(y\mid\bm{x})=\begin{cases}1,&\text{if }y=y(\bm{x})\;,\\[4.0pt]
0,&\text{otherwise}\;.\end{cases}(17)

This simplification allows us to carry out the integration overyyin Eq. (14) analytically. The UQ equations for deterministic computer simulations then reduce to𝔼​[y]\displaystyle\mathbb{E}[y]=∫y​(𝒙)​p​(𝒙)​d𝒙,\displaystyle=\int y(\bm{x})p(\bm{x})\>\mathrm{d}\bm{x}\;,(18)var​[y]\displaystyle\mathrm{var}[y]=∫(y​(𝒙)−𝔼​[y])2​p​(𝒙)​d𝒙,\displaystyle=\int\big(y(\bm{x})-\mathbb{E}[y]\big)^{2}p(\bm{x})\>\mathrm{d}\bm{x}\;,(19)

which describe how uncertainty in the input parameters𝒙\bm{x}propagates through a deterministic model to produce uncertainty in the outputyy.

Remark.The previous assertion is a simplification. More precisely, for a deterministic model, the likelihood takes the form of a Dirac delta function,p​(y∣𝒙)=δ​(y−y​(𝒙))p(y\mid\bm{x})=\delta\big(y-y(\bm{x})\big). Carrying this delta function through the integrals is slightly more involved, but ultimately leads to the same results derived above. For simplicity, we therefore keep the more intuitive rationale. However, this simplification yields incorrect results when the mapping𝒙↦y​(𝒙)\bm{x}\mapsto y(\bm{x})is deterministic but not unique — for example, when a single input𝒙\bm{x}can lead to more than one possible outcome. This situation can arise, for instance, in polymer materials or biological tissues exhibiting hysteresis or path-dependent behavior under cyclic uniaxial tensile loading, where the same stress level may correspond to different strain states during loading and unloading. In such cases, the likelihood must be expressed more carefully[Wollner et al.,2026, Sec. 4.5].

The task of UQ for a quantity of interestyygiven uncertain input parameters𝒙\bm{x}typically involves evaluating the integral in Eq. (14), or its simplified form for deterministic models in Eq. (19). Hence, Eq. (14) can be considered as a general formulation of UQ, which is in most practical cases solved numerically. For the purposes of this introduction, we will not go further into stochastic models. Instead, we continue the exposition with the simplified UQ equation for deterministic models, see Eq. (19).

## 3.1.3The prior

Thepriorp​(𝒙)p(\bm{x}), the second term in Eq. (19), represents the probability distribution of the uncertain input parameters𝒙\bm{x}; see Eqs. (14) and (19). This distribution models variability in the input parameters; in Bayesian inference, it encodes knowledge about𝒙\bm{x}before observing new data. The specification of appropriate priors requires careful consideration of available information. In mechanics, priors are commonly constructed according to three complementary principles: data-driven, structured, and principle-based approaches.

Data-driven priors.A natural way to construct a prior is from experimental data, or, in the case of biomechanical modeling, from animal or clinical data. For instance, material parameters may be inferred from mechanical tests that provide a stress–strain relationship, population statistics, or imaging data.
Therefore, the prior in the UQ formulation (Eq. (19)) can itself be the posterior of a previous inference task. Formally, one may writep​(𝒙)≡p​(𝒙∣𝒟exp)p(\bm{x})\equiv p(\bm{x}\mid\mathcal{D}_{\rm exp}), read as the probability for𝒙\bm{x}given the experimental data𝒟exp\mathcal{D}_{\rm exp}, where𝒟exp=(𝝃(n),yexp(n))n=1N\mathcal{D}_{\rm exp}=(\bm{\xi}^{(n)},y_{\rm exp}^{(n)})_{n=1}^{N}denotes experimental input–output pairs. In data-driven settings, defining the parameter distribution thus amounts to solving an inverse problem, as discussed in the following Section3.2; see also Fig.2.

Generative models as data-driven priors.A particularly recent and emerging perspective interprets such data-driven priors through so-called generative models, often based on NNs. These typically lack a closed-form expression forp​(𝒙)p({\bm{x}}), but instead offer the ability togeneraterealizations of𝒙{\bm{x}}, i.e., draw samples fromp​(𝒙)p({\bm{x}}). As we learnedWollner et al. [2026], Bayesian inference does not necessarily require a closed-form expression, as long as samples can be drawn from the distribution.
Examples include generative adversarial networks to generate material microstructuresFokina et al. [2020], Hsu et al. [2021], Lambard et al. [2023], variational auto-encoders to generate domain shapes, e.g., blood vesselsFeldman et al. [2025], and statistical shape modelsLiang et al. [2017], Verstraeten et al. [2026], which can likewise be interpreted as generative models sampling from a ‘distribution’ of shapes.
In regards to UQ, all these neural network (NN) architectures are specific, heuristic models that allow one to generate samples; other architectures, such as diffusion modelsLyu and Ren [2024], Colmenarez et al. [2025], Vahidullah and Kuhl [2026]or normalizing flowsYang et al. [2019], may equally be used for generating microstructures or shapes, and these architectural specifics matter for UQ only insofar as they affect approximation quality. Inference based on neural generative models can be expensive, and the physical consistency of samples, though implicit in the data, is not easily guaranteed.

Structured priors: Random fields.In many mechanical systems, uncertainty is distributed spatially rather than localized in a few parameters. In such cases, the prior defines a field of random variables over the spatial domain, referred to as arandom field. Each point in the domain is associated with its own random variable, leading to spatially heterogeneous yet statistically correlated material properties. Typical examples include spatially varying mechanical properties of biological tissue, for instance due to localized pathological alterationsRanftl et al. [2022], as well as random fiber orientations in fibrous tissues.
Random fields are infinite-dimensional and therefore require finite-dimensional approximations in practice, for instance via truncated Karhunen–Loève expansions. The assumed covariance structure and correlation length directly influence the predicted variability. We return to random fields later in this review article (Section8).

Principle-based priors: Maximum entropy.When only partial information about a parameter is available — such as certain moments (e.g., mean, variance), bounds, or physical constraints — the maximum entropy principle presents a systematic and compelling framework for constructing a prior. According to this principle, one selects the distribution that maximizes entropy subject to the known constraints; this yields the least biased representation consistent with the available information.
For real-valued variables defined on the unbounded domainℝ\mathbb{R}, if only normalization, mean, and variance are prescribed, the entropy-maximizing distribution is Gaussian.
If the variable is instead defined on a bounded and periodic domain, the corresponding maximum-entropy distribution changes555As a practical example from biomechanics, consider the directional distribution of collagen-fiber anglesφ∈[0,2​π)\varphi\in[0,2\pi)in arterial tissueHolzapfel et al. [2015]. Sinceφ\varphiis a circular random variable, its first circular trigonometric moment — given by𝔼​[cos⁡φ]\mathbb{E}[\cos\varphi]and𝔼​[sin⁡φ]\mathbb{E}[\sin\varphi]— provides the appropriate constraint. Under these conditions, the entropy-maximizing distribution is the von Mises distribution,p​(φ∣a,b)∝exp⁡(a​cos⁡(φ−b)),p(\varphi\mid a,b)\propto\exp\!\big(a\cos(\varphi-b)\big),which may be interpreted as the circular analogue of the Gaussian distributionJammalamadaka and Sengupta [2001]..
For further details on the maximum entropy principle, seeJaynes [1957].

## 3.1.4Bayesian inference

Once the priorp​(𝒙)p(\bm{x})has been specified and a computational modely​(𝒙)y(\bm{x})is available, we can attempt to quantify the resulting uncertainty in the model output by solving Eq. (19). To make this concept more intuitive, we illustrate it using a simple mechanics example from linear elasticity theory, in which the model complexity is increased step by step.

Example: Linear elasticity.
We consider a linear elasticity problem with three progressively increasing levels of complexity. First, let the forward model that describes the experimental stress–strain (yy–ε\varepsilon) relationship bey=E​εy=E\varepsilon, and define the input as𝒙≔E\bm{x}\coloneqq E, whereEEis the Young’s modulus. The whole setup is conditioned on a prescribed strainε\varepsilon. We assume a deterministic model, corresponding to a delta-type likelihoodp​(y∣ε,E)=δ​(y−E​ε)p(y\mid\varepsilon,E)=\delta(y-E\varepsilon). Based on data reported in the literature, we prescribe a Gaussian prior for the Young’s modulus,E∼𝒩​(μE,σE2)E\sim\mathcal{N}(\mu_{E},\sigma^{2}_{E})with densityp​(E)=(2​π​σE2)−1/2​exp⁡(−(E−μE)2/(2​σE2))p(E)=(2\pi\sigma_{E}^{2})^{-1/2}\exp\big(-(E-\mu_{E})^{2}/(2\sigma_{E}^{2})\big), whereμE\mu_{E}denotes the prior mean andσE2\sigma_{E}^{2}the prior variance, both treated as
prescribed hyperparameters rather than inferred. Under these assumptions, the uncertainty in the stress as a function of strain follows forε≠0\varepsilon\neq 0by marginalization,p​(y∣ε)=∫δ​(y−E​ε)​p​(E)​dEp(y\mid\varepsilon)=\int\delta(y-E\varepsilon)p(E)\>\mathrm{d}E, which yieldsy∼𝒩​(μE​ε,σE2​ε2)y\sim\mathcal{N}(\mu_{E}\varepsilon,\sigma_{E}^{2}\varepsilon^{2}), so thatvar​[y∣ε]=σE2​ε2\mathrm{var}[y\mid\varepsilon]=\sigma_{E}^{2}\varepsilon^{2}grows quadratically with the applied strain.

In general, however, analytical solutions of the UQ equations are rarely available. It is important to note that the relative ease of computation in the present example arises from the linear dependence on the uncertain parameterEE, rather than from the linearity with respect to the strainε\varepsilon; nonlinear constitutive relationships would, in this context, lead to a comparable level of inference complexity. To illustrate this, in a second step, we consider a Gaussian likelihood with prescribed noise levelσy\sigma_{y},y∣ε,E∼𝒩​(E​ε,σy2)y\mid\varepsilon,E\sim\mathcal{N}(E\varepsilon,\sigma^{2}_{y}), and assign a log-uniform prior to the Young’s modulus,p​(E)∝1/Ep(E)\propto 1/Eon the truncated supportE∈[Emin,max]E\in[E_{\rm min,max}]withEmin>0E_{\min}>0.666A uniform prior on a quantity isinconsistentwith the information that this quantity is strictly positiveJeffreys [1939]. Instead, one assigns a uniform prior to the logarithm of the quantity, which directly leads to the log-uniform prior used here.. In this case, no closed-form expression for the prior predictivep​(y∣ε)p(y\mid\varepsilon)exists. Its first two moments remain analytically accessible,𝔼​[y∣ε]=ε​(Emax−Emin)/ln⁡(Emax/Emin)\mathbb{E}[y\mid\varepsilon]=\varepsilon(E_{\max}-E_{\min})/\ln(E_{\max}/E_{\min})andvar​[y∣ε]=σy2+ε2​var​[E]\mathrm{var}[y\mid\varepsilon]=\sigma_{y}^{2}+\varepsilon^{2}\mathrm{var}[E], whereas the
density itself requires numerical integration techniques, such as Monte Carlo methodsWollner et al. [2025].

Finally, in a third step, we consider the same model as in the second case, but change the quantity of interest from the stress at a single strain to the maximum absolute stress attained over a prescribed strain history,ymax=maxε∈[εmin,εmax]⁡|E​ε|y_{\rm max}=\max_{\varepsilon\in[\varepsilon_{\rm min},\varepsilon_{\rm max}]}|E\varepsilon|.
Although the constitutive model remains linear elastic, numerical methods are now typically required even to compute𝔼​[ymax]\mathbb{E}[y_{\rm max}]andvar​[ymax]\mathrm{var}[y_{\rm max}]. The computational difficulty is further amplified when dealing with large-strain settings or nonlinear material behavior, such as viscoelasticity or material anisotropy.

In addition to the above three levels, in computational mechanics, we encounter yet another, fourth practical challenge: even with advanced numerical integration methods, computing the distributionp​(y)p(y)or its proxies typically requires a very large number of simulations, i.e., evaluations ofy​(𝒙)y({\bm{x}}), often on the order of10510^{5}to10810^{8}samples. For complex mechanical models, this is computationally infeasible. As an illustration, consider a simple finite element simulation that takes only one minute to run. Performing10610^{6}such simulations would require roughly two years of continuous computation. Although vanilla Monte Carlo samplingWollner et al. [2025]is trivially parallelizable, the implied computational resources are still enormous.

A widely used strategy to address this fourth issue is the implementation ofsurrogate models. In this approach, a relatively small number of simulations is first performed, and the resulting data are used tolearna fast approximation of the model output, with predictions then available in milliseconds. In other words, we fit a parameterized function, called a surrogate, to the simulation data and use it as a substitute for the original, computationally expensive model. This allows for rapid evaluation ofy​(𝒙)y(\bm{x})millions of times, and enables numerical integration of Eq. (19).
We discuss surrogate construction and training in Section3.3, and the zoo of available surrogate models, that often share mathematical foundations with machine learning methods, in Section4.

Several methods exist for computing the posterior, and each presents distinct trade-offs between computational cost and approximation accuracy, in specific contexts
. While point estimates — such as maximum likelihood, or maximum a posteriori (MAP) and posterior mean from Bayesian inference that incorporate prior knowledge, but reduce the posterior to a single value — provide single representative values, they fail to characterize the full parameter uncertainty inherent in mechanical models.
To obtain a complete characterization, it is often necessary to sample from the full posterior using, for instance, Monte CarloWollner et al. [2026]or Markov chain Monte Carlo (MCMC) methods. Although MCMC methods are computationally expensive, they are asymptotically exact (under some conditions, as usual), and considered the most common approach. Finally, nested sampling is an evidence-focused distinct method that enables model comparison in high dimensions (cf. Section5). Importantly, these methods can yield substantially different results, particularly for complex posteriors that are multi-modal, skewed, or heavy-tailed, as illustrated in Fig.3for a representative synthetic bimodal posterior. Modelers should therefore be aware of these method-specific limitations; see related literatureKroese et al. [2011], Pensalfini et al. [2026].Figure 3:Comparison of standard methods for computing the posterior: (i) synthetic bimodal, asymmetric true posterior of a parameterx1x_{1}(black); (ii) maximum a posteriori (MAP) estimate (blue), which provides only a point estimate without uncertainty quantification; (iii) mean-field Gaussian approximation via variational inference (VI) (yellow), which captures local structure around the dominant mode but fails to represent multimodality and asymmetry and underestimates uncertainty; and (iv) reference solution (asymptotically exact) obtained with the Metropolis–Hastings (MH) algorithm (red).

## 3.2Inverse problems I: Model calibration and parameter estimation

The core objective of model calibration and parameter estimation can be stated as:

Determination of model parameters and uncertainty quantification thereof given experimental or simulation data.

## 3.2.1General concept

In mechanics, inverse problems typically arise in the following three situations: (i) experimental measurements are available, but the underlying constitutive or material parameters remain unknown; (ii) computational simulation data are available, and one aims to learn a surrogate model; or (iii) a combination of both (i) and (ii). In this section, we will mainly discuss case (i) and defer cases (ii) and (iii) to Section3.3.

Let𝒙∈𝒳⊆ℝD𝒙\bm{x}\in\mathcal{X}\subseteq\mathbb{R}^{D_{\bm{x}}}denote the vector of constitutive parameters that characterize the material behavior, whereD𝒙D_{\bm{x}}represents the number of constitutive parameters in the model. The deterministic forward modelf​(𝒙;𝝃)f(\bm{x};\bm{\xi})describes the system’s response for a given set of constitutive parameters𝒙\bm{x}and experimental control parameters𝝃∈Ξ⊆ℝD𝝃\bm{\xi}\in{\Xi}\subseteq\mathbb{R}^{D_{\bm{\xi}}}, as defined in Fig.2. These control parameters include applied loads or displacements andD𝝃D_{\bm{\xi}}is the total number of control parameters. The model output is an observable quantityyexp=f​(𝒙;𝝃)y_{\rm exp}=f(\bm{x};\bm{\xi}), such as a strain or stress component at a given location. This forward model typically represents the underlying physical laws of the system, for example through the numerical solution of partial differential equations (PDEs).
In parallel, experimental measurements provide corresponding observations of the same physical quantities under specified control conditions. The measurement can be modeled, e.g., byyexp=f​(𝒙;𝝃)+η,\displaystyle y_{\rm exp}=f(\bm{x};\bm{\xi})+\eta\;,(20)

with additive noiseη\eta.
The collected data are represented as𝒟exp=(𝝃(n),yexp(n))n=1N,\mathcal{D}_{\rm exp}=\big(\bm{\xi}^{(n)},y_{\rm exp}^{(n)}\big)_{n=1}^{N}\;,(21)

where each pair(𝝃(n),yexp(n))(\bm{\xi}^{(n)},y_{\rm exp}^{(n)})corresponds to thenn-th observation point in one experiment performed under the control parameters𝝃(n)\bm{\xi}^{(n)}, andNNdenotes the total number of observations. The goal is then to determine the parameters𝒙{\bm{x}}given the data𝒟exp\mathcal{D}_{\rm exp}and the physical modelf​(𝒙;𝝃)f(\bm{x};\bm{\xi}).

Unfortunately, inverse problems are often ill-posed, meaning that multiple parameter sets may explain the data equally well, which is often exacerbated by the presence of noise.
To address these challenges, we can reformulate the inverse problem in a Bayesian inference framework and incorporate both measurement noise and prior knowledge about the parameters in a consistent manner. Instead of seeking a singleoptimalestimate of the unknown parameters, we quantify our uncertainty about them using probability distributions. Consider, for example, the case of above assumptions with additive Gaussian noise modeled asη∼𝒩​(0,σ2)\eta\sim\mathcal{N}(0,\sigma^{2})with measurements that are independently and identically distributed (i.i.d.). Then, the joint likelihood isp(𝒟exp∣𝒙,σ)=∏n=1N1σ​2​π​exp⁡(−12​σ2​(yexp(n)−f​(𝒙;𝝃(n)))2)∝σ−N​exp⁡(−12​σ2​∑n=1N(yexp(n)−f​(𝒙;𝝃(n)))2).\begin{split}p(\mathcal{D}_{\rm exp}&\mid\bm{x},\sigma)\\
&=\prod_{n=1}^{N}\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{1}{2\sigma^{2}}\big(y_{\rm exp}^{(n)}-f(\bm{x};\bm{\xi}^{(n)})\big)^{2}\right)\\
&\propto\sigma^{-N}\exp\left(-\frac{1}{2\sigma^{2}}\sum_{n=1}^{N}\big(y_{\rm exp}^{(n)}-f(\bm{x};\bm{\xi}^{(n)})\big)^{2}\right)\;.\end{split}(22)

whereσ\sigmais the standard deviation andσ2\sigma^{2}is the variance of the measurement noise. Then, according to Bayes’ theorem, with a priorp​(𝒙,σ)p(\bm{x},\sigma), the posterior isp​(𝒙,σ∣𝒟exp)∝p​(𝒟exp∣𝒙,σ)​p​(𝒙,σ),p(\bm{x},\sigma\mid\mathcal{D}_{\rm exp})\propto p(\mathcal{D}_{\rm exp}\mid\bm{x},\sigma)p(\bm{x},\sigma)\;,(23)

which expresses our updated knowledge about the unknown parameters after observing the data. This distribution characterizes not only the expected parameter values but also their associated uncertainty or varianceWollner et al. [2026]. Note that methods for computing the posterior were outlined in Section3.1.4.

Importantly, the posterior obtained from the inverse problem (cf. Eq. (23)) often serves as the input distribution, i.e., the prior, for the subsequent uncertainty propagation analysis, as illustrated in Fig.2. In other words, once the parameters have been inferred probabilistically, their posterior defines the space of plausible parameter values that should be propagated through the model to assess the resulting uncertainty in model predictions.

In summary, inverse problems play several multi-faceted roles in mechanics, with three prominent applications:
(i) calibration or, synonymously,parameter estimation, such as fitting constitutive models to experimental data for predictive simulations;
(ii) input characterization, i.e., determining distributions of input parameters𝒙\bm{x}as a prerequisite for forward uncertainty propagation; and
(iii) surrogate model calibration — an additional inverse problem often arises, where the goal is to calibrate the hyperparameter of a surrogate model that replaces a more expensive computational model to quantify the uncertainty of the surrogate itself, as shown in Fig.2.
Note that case (iii) is a variant of case (i) with different context.
We first discuss case (iii) in the following Section3.3, before presenting an illustrative mechanical example for cases (i) and (ii) in Section3.4.

For further context, the literature provides several (bio)mechanical examples of model calibration and parameter estimation using Bayesian inference.
In biomechanics, these studies encompass UQ in blood rheology modelsRanftl et al. [2022], parameter estimation in soft biological tissues using both standard constitutive modelsMadireddy et al. [2016], Teferra and Brewick [2019], Sundnes and Rodríguez-Cantano [2022]and unsupervised discovery of constitutive modelsJoshi et al. [2022], Krijnen et al. [2025], as well as efficient inference of Windkessel parameter posteriors in three-dimensional aortic hemodynamics simulations through zero-dimensional surrogatesRichter et al. [2025], and amortized posterior estimation of boundary conditions in patient-specific cardiovascular models using conditional flow matchingChoi et al. [2026]. Another example of amortized variational inference for real-time inference with potential applications in medical diagnosis or health monitoring of engineered systems is presented inKarumuri and Bilionis [2024], which learns a NN map from data to posterior, avoiding re-solving from scratch for each new dataset.

For general mechanical problems, recent work has addressed UQ of material parameters for different experimental setups under reparametrizationWollner et al. [2025], for constitutive parameters of fiber-reinforced polymer compositesThomas et al. [2022], constitutive models including damageChakraborty and Messner [2021], phase-field fracture modelsKhodadadian et al. [2020], and coupled mechanics models based on interface deformations where only shape changes are observableWillmann et al. [2022].
Furthermore, Bayesian inference has been employed to infer hyperparameters in physics-informed NNsYang et al. [2021], with applications to COVID-19 outbreak dynamicsLinka et al. [2022]and constitutive artificial NNs for soft biological tissuesLinka et al. [2025]. Here, the NNs with hyperparameters calibrated on experimental data can be seen as the forward model directly, in contrast to surrogate modeling where simplified models approximate expensive high-fidelity simulations; a subtle but important distinction.

## 3.2.2Data fusion and data assimilation

In the context of model calibration and parameter estimation, we introduce the termsdata fusionanddata assimilation, noting that alternative definitions exist in the literature. We adopt these terms because they provide a useful distinction between inference problems involving asingleforward model (data fusion) and those that rely onmultipleforward models (data assimilation), which frequently arise in mechanics, multi-physics modeling, and multi-modal experimental setups.

Data fusionrefers to the consistent combination of information from multiple experiments, measurement modalities, or simulations within a single likelihood model, i.e., a single probabilistic model. This may include merging mechanical test data from uniaxial tensile, compression, or relaxation tests with medical imaging measurements, such as ultrasound, computed tomography, or magnetic resonance imaging. More generally, data fusion exploits complementary information and weights inconsistent evidence according to the uncertainty associated with each data source. Under the standard assumption of conditional independence, the joint likelihood factorizes and can be written asp​(yexp(1),yexp(2),…∣𝒙)=∏kp​(yexp(k)∣𝒙),\displaystyle p(y_{\rm exp}^{(1)},y_{\rm exp}^{(2)},\ldots\mid\bm{x})=\prod_{k}p(y_{\rm exp}^{(k)}\mid\bm{x})\;,(24)

where eachyexp(k)y_{\rm exp}^{(k)}denotes a distinct dataset from thekk-th experiment. Factorization greatly simplifies inference, though it requires that measurement noise and experimental errors be independent across modalities or setups. When this assumption is reasonable, each dataset contributes multiplicatively to the posterior, and usually improves parameter identifiability, as exemplarily shown for parameter identification in constitutive modeling based on multiple experimental modesWollner et al. [2025].
We may generalize this notion also to multiple physical models, see also Fig.4.Figure 4:General workflow for model calibration and parameter estimation based on multiple experimental types under the simplifying assumption of independent parameters.
The posterior is computed from the chosen prior and the likelihood, with the latter defined by the experimental data pairs𝒟exp\mathcal{D}_{\rm exp}and the computational models associated with the respective experimental typeskkand parameterized by𝒙\bm{x}. From the resulting posterior, marginalized posteriors for individual parameters or combined parameter combinations can be computed.

Building on this concept, we understanddata assimilationas the modeling of the likelihood for sequential state estimation in dynamical models. The system evolves according to𝒙t=Ft​(𝒙t−1)+ηt{\bm{x}}_{t}=F_{t}({\bm{x}}_{t-1})+\eta_{t}, and observations are collected sequentially asyt=Gt​(xt)+ηty_{t}=G_{t}(x_{t})+\eta_{t}, wherettdenotes an ordered (typically time) index, andFtF_{t}andGtG_{t}describe the state transition and observation models.
In contrast to data fusion — where all data are processed jointly without a particular order — data assimilation explicitly accounts for sequential structure, as in time-series problems. Both the likelihood and the prior follow this ordering.
Given observations up to timeTT, the posterior over the full state trajectory(𝒙0:T,y0:T)({\bm{x}}_{0:T},y_{0:T})typically factorizes asp​(𝒙0:T∣y1:T)\displaystyle p({\bm{x}}_{0:T}\mid y_{1:T})∝p​(𝒙0)​∏t=1Tp​(𝒙t∣𝒙t−1)\displaystyle\propto p({\bm{x}}_{0})\prod_{t=1}^{T}p({\bm{x}}_{t}\mid{\bm{x}}_{t-1})×p​(yt∣𝒙t),\displaystyle\hphantom{=}\,\,\times p(y_{t}\mid{\bm{x}}_{t})\;,(25)

meaning that the likelihood at each new state depends only on the previous state (Markov property), and each observation depends only on the current state.

Examples from the literature include the dynamic estimation of hyperelastic material parameters across various mechanical tests using an extended Kalman filterXie et al. [2021], Song et al. [2023], as well as dynamic soft tissue identification achieved by coupling a contact model with an iterated Kalman filterZhu et al. [2023].

## 3.2.3Accounting for model discrepancy

Even a carefully constructed computational model may not perfectly reproduce the true physical system. Simplifying assumptions, incomplete physics, and numerical approximations introduce systematic discrepancies between model predictions and experimental observations. These deviations are collectively referred to asmodel discrepancy, ormodel inadequacy; see, e.g.,Kennedy and O’Hagan [2001], Morrison et al. [2018]for Bayesian discussions.

To account for such effects in a most simple manner, the standard observation model is extended asyexp=f​(𝒙,𝝃)+δ​(𝝃)+η,y_{\rm exp}=f(\bm{x},\bm{\xi})+\delta(\bm{\xi})+\eta\;,(26)

wheref​(𝒙,𝝃)f(\bm{x},\bm{\xi})is the forward model prediction under the control parameters𝝃\bm{\xi},η\etarepresents (Gaussian) measurement noise, andδ​(𝝃)\delta(\bm{\xi})captures the systematic model discrepancy between simulations and observations.
Within the Bayesian framework, both the model parameters𝒙\bm{x}and the discrepancy functionδ​(𝝃)\delta(\bm{\xi})are treated as uncertain quantities. A flexible and widely used approach is to model the discrepancy as a Gaussian process (GP). Alternatively, it could be represented using a low-dimensional basis expansion, which is formally introduced in the following Section4.2.

Including a model discrepancy term helps prevent biased parameter estimates, as it avoids attributing structural model errors to the model parameters𝒙\bm{x}. However, it also introduces additional uncertainty and potential identifiability issues, since bothf​(𝒙,𝝃)f(\bm{x},\bm{\xi})andδ​(𝝃)\delta(\bm{\xi})may explain similar residual patterns. Careful prior specification and model validation are therefore essential to ensure meaningful inference.

Introducing a model discrepancy is recommended when the residuals — defined as the differences between observed data and model predictions — after calibration exhibit a smooth or correlated pattern with respect to the control parameters𝝃\bm{\xi}. This approach is also advisable if the forward modelf​(𝒙,𝝃)f(\bm{x},\bm{\xi})involves simplifications or neglects important physical effects, such as anisotropy, nonlinear behavior, or three-dimensionality. Additionally, model discrepancy should be considered when predictive performance deteriorates under unseen control conditions or when the residuals reveal input-dependent bias, indicating a systematic error.
Residual diagnostics, posterior predictive checks, and the model evidence or its proxies (e.g., Akaike information criterion or leave-one-out cross-validation) can be used to evaluate whether the inclusion ofδ​(𝝃)\delta(\bm{\xi})improves model adequacy.

The need to address such discrepancies is a recurring theme in recent literature. For instance, Paun et al.Paun et al. [2020]demonstrated this type of model error in one-dimensional hemodynamic simulations of the pulmonary artery, where linear and nonlinear material models yielded notably different predictions. Similarly, Römer et al.Römer et al. [2022]used a discrepancy term to account for errors in a surrogate model, while Calvetti et al.Calvetti et al. [2018]proposed an iterative loop to simultaneously update both the unknown parameters and the model error, thereby refining the posterior distribution.

## 3.2.4Hierarchical modeling

Hierarchical Bayesian modeling provides a systematic way to represent complex uncertainty structures by introducing latent variables and hyperparameters that govern lower-level model components. In contrast to a single-level Bayesian model, hierarchical formulations explicitly distinguish between different sources of uncertainty, such as parameter variability, noise levels, and higher-level structural assumptions.

To illustrate the idea, consider a forward modely(n)=f​(𝒙;𝝃(n))+η(n),η(n)∼𝒩​(0,σ2).y^{(n)}=f(\bm{x};\bm{\xi}^{(n)})+\eta^{(n)},\,\quad\eta^{(n)}\sim\mathcal{N}(0,\sigma^{2})\;.(27)

In a standard formulation, priors would be assigned directly to𝒙\bm{x}andσ\sigma. In a hierarchical setting, however, these priors themselves depend on additional hyperparametersΨ\PsiandΣ\Sigma, for examplep​(𝒙∣Ψ)p(\bm{x}\mid{\Psi})andp​(σ∣Σ)p(\sigma\mid\Sigma), together with a hyperpriorp​(Ψ,Σ)=p​(Ψ)​p​(Σ)p(\Psi,\Sigma)=p(\Psi)p(\Sigma). This additional layer allows the model to learn not only the parameters𝒙\bm{x}andσ\sigma, but also the statistical structure governing them.

The resulting joint posterior factorizes into a hierarchyp​(𝒙,σ,Ψ,Σ∣𝒟)\displaystyle p(\bm{x},\sigma,{\Psi},\Sigma\mid\mathcal{D})∝p​(𝒟∣𝒙,σ)​p​(𝒙∣Ψ)\displaystyle\propto p(\mathcal{D}\mid\bm{x},\sigma)p(\bm{x}\mid{\Psi})×p​(σ∣Σ)​p​(Ψ)​p​(Σ).\displaystyle\hphantom{=}\,\,\times p(\sigma\mid\Sigma)p({\Psi})p(\Sigma)\;.(28)

To predict the outcome for a new control parameter𝝃∗\bm{\xi}_{\ast}, we marginalize the model likelihood over the full parameter space. By using the joint posterior as a weighting function, the predictive distribution accounts for uncertainty at every level of the hierarchyp​(y∗∣𝝃∗,𝒟)\displaystyle p(y_{\ast}\mid\bm{\xi}_{\ast},\mathcal{D})=⨌p​(y∗∣𝝃∗,𝒙,σ,Ψ,Σ)\displaystyle=\iiiint p(y_{\ast}\mid\bm{\xi}_{\ast},\bm{x},\sigma,\cancel{\Psi,\Sigma})×p​(𝒙,σ,Ψ,Σ∣𝒟)​d​𝒙​d​σ​d​Ψ​d​Σ,\displaystyle\hphantom{=}\,\,\times p(\bm{x},\sigma,{\Psi},\Sigma\mid\mathcal{D})\>\mathrm{d}\bm{x}\>\mathrm{d}\sigma\>\mathrm{d}{\Psi}\>\mathrm{d}\Sigma\;,(29)

where we use the fact that the conditional of the first term contains redundant information, such thatp​(y∗∣𝝃∗,𝒙,σ,Ψ,Σ)≡p​(y∗∣𝝃∗,𝒙,σ)p(y_{\ast}\mid\bm{\xi}_{\ast},\bm{x},\sigma,{\Psi,\Sigma})\equiv p(y_{\ast}\mid\bm{\xi}_{\ast},\bm{x},\sigma). This simplification reflects that once the parameters𝒙\bm{x}andσ\sigmaare known, the additional hyperparametersΨ\PsiandΣ\Sigmaprovide no additional information for the predictiony∗y_{\ast}.
This nested marginalization highlights a key principle: uncertainty is propagated across all layers of the model, not only at the parameter level.

A practical advantage of this layered structure is flexibility. Different approximation strategies can be applied selectively at different levels. For instance, one may retain full inference for𝒙\bm{x}andσ\sigmawhile approximating the hyperparameter posterior via a Laplace or Dirac approximation. This reduces computational cost without collapsing the hierarchical structure.

Hierarchical formulations are particularly effective for modeling structured or heterogeneous systems. For instance, inter-patient variability can be represented by assuming that individual parameters follow a common distributionp​(𝒙i∣Ψ)p(\bm{x}_{i}\mid{\Psi}), whereiihere denotes the patient index andΨ\Psirepresents the shared population-level hyperparameter. This framework allows the model topoolinformation from all individuals while still respecting their unique differences. By sharing data across the entire group, the global population trends help guide the estimation for each specific case.777In practice, when characterizing biological tissue samples from multiple patient donors, experimental limitations often result in some specimens providing incomplete or noisy datasets. Instead of analyzing each specimen in isolation,poolingallows the model to learn the characteristic mechanical response from the entire population. If an individual specimen’s data is sparse, the model uses the group’s collective behavior as an informative starting point (prior) tofill in the gaps, ensuring that the identified parameters remain physically plausible and consistent with the broader patient group.This collective approach leads to much more reliable results than fitting each specimen separately, which is especially valuable when the data for a single individual are too sparse to stand on their ownPensalfini and Buganza Tepole [2023], Pensalfini et al. [2026].
Similarly, intra-patient variability or spatial heterogeneity can be addressed through random field priorsRanftl et al. [2022], which will be introduced in Section8, where the statistical properties of a field are specified rather than prescribing a deterministic function.

Many other modeling strategies can be interpreted through this hierarchical lens. For instance, model discrepancy formulations (Section3.2.3) and multi-fidelity strategies (Section4.5.3) introduce additional latent layers to account for structural model errors or varying levels of approximation. Rather than modifying the likelihoodad hoc, these approaches embed such assumptions directly into the probabilistic hierarchy by treating the model’s inadequacy as a structured uncertainty.888Notably, KoutsourelakisKoutsourelakis [2009]demonstrated that this hierarchical treatment allows for accurate uncertainty estimates even when the underlying computational models are themselves inaccurate, provided the discrepancy is modeled and propagated consistently.Even standard regression models admit such an interpretation: GP regression, for example, can be viewed as a hierarchical model where latent function values are marginalized under a conjugate prior, while hyperparameters are estimated by a higher-level distribution. This perspective will be discussed in more detail in Section4.3.

In addition, several robust or sparse modeling strategies arise naturally from hierarchical constructions. The Student-ttdistribution, for instance, can be derived by marginalizing a Gaussian likelihood with respect to an inverse-gamma prior on its variance parameter. This construction, which can be viewed as a regularized version of a non-informative Jeffreys prior results in a heavy-tailed formulation that acts as a scale mixture of Gaussians, providing inherent robustness against outliersRanftl et al. [2022,2022], as discussed in the following example (cf. Section3.4).
Similarly, the horseshoe prior employs a hierarchy of local and global scale parameters. This structure enforces strong shrinkage on negligible model parameters or surrogate hyperparameters while leaving significant physical effects virtually unaffected — a property particularly suited for high-dimensional problems where the underlying system is expected to be sparse.

From a broader perspective, UQ itself may be viewed as a hierarchical construction. Model calibration (inverse problem I) and surrogate modeling (inverse problem II) then constitute different levels within this probabilistic hierarchy, to explicitly separate distinct sources of uncertainty rather than conflating them.

## 3.3Inverse problems II: Surrogate modeling

In the Bayesian context, the core objective of surrogate modeling is:

To construct computationally efficient approximations to high-fidelity forward models in order to enable uncertainty propagation.

## 3.3.1General concept

To evaluate the integral in Eq. (19), or equivalently Eq. (14), we first need to construct a surrogate for the computational model. The surrogate is typically represented as a parameterized function,y​(𝒙)≈f^​(𝒙;𝜽),\displaystyle y(\bm{x})\approx\hat{f}(\bm{x};\bm{\theta})\;,(30)

where𝜽∈Θ\bm{\theta}\in\Thetais a vector of parameters parameterizing the surrogate. The functional form of the surrogate can vary widely; the only requirements are that it can be evaluated efficiently (fast) and that its parameters can be identified from a simulation dataset of input–output pairs𝒟=(𝒙(n),y(n))n=1N\mathcal{D}=(\bm{x}^{(n)},y^{(n)})_{n=1}^{N}. In the simplest case, the surrogate may be a constant,f^​(𝒙;𝜽)=a\hat{f}(\bm{x};\bm{\theta})=a, or a linear functionf^​(𝒙;𝜽)=b​𝒙+c\hat{f}(\bm{x};\bm{\theta})=b\bm{x}+c, fitted directly to the data𝒟\mathcal{D}. More generally, we can express the surrogate as an expansion,f^​(𝒙;𝜽)=∑p=1Pcp​ϕp​(𝒙;wp),\displaystyle\hat{f}(\bm{x};\bm{\theta})=\sum_{p=1}^{P}c_{p}\phi_{p}(\bm{x};w_{p})\;,(31)

whereϕp\phi_{p}denotes a set of basis functions parametrized bywpw_{p}andcpc_{p}are linear coefficients. The indexppenumerates the basis functions in the surrogate model, with a total ofPPterms in the expansion.

We can thus distinguish between linear surrogate parameterscpc_{p}and nonlinear surrogate parameterswpw_{p}, such that𝜽=(cp,wp)T\bm{\theta}=(c_{p},w_{p})^{\rm T}. This distinction is important, since linear parameters are often easier to determine than non-linear parameters.999For a practical example, if we consider a Gaussian likelihood and a Gaussian prior on bothcpc_{p}andwpw_{p}, then we can obtain analytic expressions for𝔼​[cp]\mathbb{E}[c_{p}], conditioned on somewpw_{p}, but not for𝔼​[wp]\mathbb{E}[w_{p}], i.e., the non-linear parameterswpw_{p}typically require numerical estimation.The basis functionsϕp\phi_{p}can be just about anything. Popular examples include polynomial and trigonometric functions, which lead to polynomial expansions or Fourier expansions, respectively. A particularly notable case is the polynomial chaos expansion (PCE), where the basis polynomialsϕp\phi_{p}are constructed to be orthogonal with respect to the input distributionp​(𝒙)p(\bm{x}).
Furthermore, the surrogate modelf^​(𝒙;𝜽)\hat{f}(\bm{x};\bm{\theta})can also be interpreted as a machine learning model. If the surrogate were implemented as a NN, the functionsϕp\phi_{p}would correspond to the outputs of the final layer. We introduce PCEs in Section4.2, while the special case of machine learning–based surrogate models is discussed in more detail later in Section4.4.

After selecting a suitable parameterization for the surrogate modelf^​(𝒙;θ)\hat{f}(\bm{x};\theta), the next step is to determine the parameters𝜽\bm{\theta}from the available data𝒟\mathcal{D}. To do so, we must define afitting criterion; that is, an optimization objective defining which surrogate parameters𝜽\bm{\theta}are considered optimal given the data𝒟\mathcal{D}. In non-probabilistic settings and particularly in machine learning, this criterion is often referred to as aloss function.

The simplest example is theL2L_{2}-loss, which leads to the familiar least-squares criterion: minimizing the sum of squared errors between predictions and observations. However, least squares is merely a special case of a more general probabilistic framework. In this setting, we seek to maximize the posterior for the surrogate parameters𝜽\bm{\theta}, given the surrogate modelf^\hat{f}and the data𝒟\mathcal{D},𝜽∗=arg⁡max𝜽⁡p​(𝜽∣𝒟,f^),\displaystyle\bm{\theta}^{\ast}=\arg\max_{\bm{\theta}}\,p(\bm{\theta}\mid\mathcal{D},\hat{f})\;,(32)

where𝜽∗\bm{\theta}^{\ast}represents theoptimalsurrogate parameters given the ansatzf^\hat{f}.
Under the assumption of a Gaussian likelihood with fixed variance and uniform prior101010Specifically, by assuming a Gaussian likelihoodp​(𝒟∣𝜽,f^)=𝒩​(f^​(𝒙;𝜽),σ2)p(\mathcal{D}\mid\bm{\theta},\hat{f})=\mathcal{N}(\hat{f}(\bm{x};\bm{\theta}),\sigma^{2})with known, constant varianceσ2\sigma^{2}, and a non-informative uniform prior overp​(𝜽)=const.p(\bm{\theta})=\text{const.}, Bayes’ theorem implies that the posterior is proportional to the likelihood,p​(𝜽∣𝒟,f^)∝𝒩​(f^​(𝒙;𝜽),σ2)p(\bm{\theta}\mid\mathcal{D},\hat{f})\propto\mathcal{N}(\hat{f}(\bm{x};\bm{\theta}),\sigma^{2})., maximizing this posterior is mathematically equivalent to minimizing theL2L_{2}-loss, or the sum of squared residuals,𝜽∗=arg⁡min𝜽​∑n=1N(y(n)−f^​(𝒙(n);𝜽))2.\displaystyle\bm{\theta}^{\ast}=\arg\min_{\bm{\theta}}\sum_{n=1}^{N}\big(y^{(n)}-\hat{f}(\bm{x}^{(n)};\bm{\theta})\big)^{2}\;.(33)

The termstrainingorlearningtypically refer to the — often iterative — process of solving Eq. (32). This optimization naturally extends to the Bayesian framework discussed in the following Section3.3.2, where the priorp​(𝜽)p({\bm{\theta}})effectively serves as aregularizerfor the objective function.

Once the optimal parameters𝜽∗\bm{\theta}^{\ast}are identified, the resulting surrogate model,f^​(𝒙;𝜽∗)≈y​(𝒙),\hat{f}(\bm{x};\bm{\theta}^{\ast})\approx y(\bm{x})\;,(34)

serves as a computationally efficient proxy for the original model. This substitution allows for the efficient approximation of the UQ solution in Eq. (19) (or equivalently Eq. (10)).

## 3.3.2Bayesian surrogate modeling

The probabilistic approach of surrogatelearningis more general than the use of simple loss functions. The approach discussed so far does not account for the uncertainty associated with the estimated optimal parameters𝜽∗\bm{\theta}^{\ast}. This simplification is valid as long as the data are sufficiently informative such that the posteriorp​(𝜽∣𝒟,f^)p(\bm{\theta}\mid\mathcal{D},\hat{f})is sharply peaked; we then have a high degree of belief about our choice of𝜽∗\bm{\theta}^{\ast}. This is typically the case when the following conditions are satisfied: (i) the dataset is large, of high quality, and informative with respect to the parameters; and (ii) the simulation and surrogate is not insensitive to certain parameters, the surrogate is not overparametrized, and no parameter-identifiability issues arise.

For truly Bayesian inference, we would need to define a suitable prior and evaluate the full parameter posteriorp​(𝜽∣𝒟,f^)p(\bm{\theta}\mid\mathcal{D},\hat{f}). To quantify the uncertainty in the parameters𝜽\bm{\theta}, one would compute the first and second posterior moments as a proxy for the full distribution, analogous to Eq. (12), as𝔼​[𝜽]\displaystyle\mathbb{E}[{\bm{\theta}}]=∫𝜽​p​(𝜽∣𝒟,f^)​d𝜽,\displaystyle=\int\bm{\theta}p(\bm{\theta}\mid\mathcal{D},\hat{f})\>\mathrm{d}\bm{\theta}\;,(35)var​[𝜽]\displaystyle\mathrm{var}[\bm{\theta}]=∫(𝜽−𝔼​[𝜽])2​p​(𝜽∣𝒟,f^)​d𝜽.\displaystyle=\int\big(\bm{\theta}-\mathbb{E}[\bm{\theta}]\big)^{2}p(\bm{\theta}\mid\mathcal{D},\hat{f})\>\mathrm{d}\bm{\theta}\;.(36)

In this light, the optimization following Eq. (32) can be viewed as a point-estimate approximation of Eq. (35). This simplification effectively represents the posterior as a Dirac delta distribution centered at the mode, i.e.,p​(𝜽∣𝒟,f^)≈δ​(𝜽−𝜽∗)p(\bm{\theta}\mid\mathcal{D},\hat{f})\approx\delta({\bm{\theta}}-{\bm{\theta}}^{\ast}). Such an approach is often preferred for its computational efficiency, particularly when epistemic uncertainty is expected to be negligible or is simply not of interest.

Estimating the uncertainty of the surrogate predictionf^​(𝒙;𝜽)\hat{f}(\bm{x};\bm{\theta})itself is more involved: one must introduce the posteriorp​(𝜽∣𝒟,f^)p(\bm{\theta}\mid\mathcal{D},\hat{f})into the UQ equation (Eqs. (19), (10), or (14)) via the marginalization rule. This results in an additional integral of the formp​(y^∣𝒙,𝒟,f^)\displaystyle p(\hat{y}\mid{\bm{x}},\mathcal{D},\hat{f})=∫p​(y^∣𝒙,𝜽)​p​(𝜽∣𝒟,f^)​d𝜽,\displaystyle=\int p(\hat{y}\mid{\bm{x}},{\bm{\theta}})\,p(\bm{\theta}\mid\mathcal{D},\hat{f})\>\mathrm{d}{\bm{\theta}}\;,(37)𝔼​[f^​(𝒙)]\displaystyle\mathbb{E}\big[\hat{f}(\bm{x})\big]=∫f^​(𝒙;𝜽)​p​(𝜽∣𝒟,f^)​d𝜽,\displaystyle=\int\hat{f}(\bm{x};\bm{\theta})p(\bm{\theta}\mid\mathcal{D},\hat{f})\>\mathrm{d}{\bm{\theta}}\;,(38)var​[f^​(𝒙)]\displaystyle\mathrm{var}\big[\hat{f}(\bm{x})\big]=∫(f^​(𝒙;𝜽)−𝔼​[f^​(𝒙)])2\displaystyle=\int\Big(\hat{f}(\bm{x};\bm{\theta})-\mathbb{E}\big[\hat{f}(\bm{x})\big]\Big)^{2}×p​(𝜽∣𝒟,f^)​d​𝜽,\displaystyle\hphantom{=}\,\,\times p(\bm{\theta}\mid\mathcal{D},\hat{f})\,\mathrm{d}{\bm{\theta}}\;,(39)

for the posterior uncertainty as a function of𝒙{\bm{x}}, or marginalized with respect to the inputs,p​(y^∣𝒟)\displaystyle p(\hat{y}\mid\mathcal{D})=∬p​(y^∣𝒙,𝜽)\displaystyle=\iint p(\hat{y}\mid{\bm{x}},{\bm{\theta}})×p​(𝒙,𝜽∣𝒟,f^)​d​𝒙​d​𝜽,\displaystyle\hphantom{=}\,\,\times p({\bm{x}},\bm{\theta}\mid\mathcal{D},\hat{f})\>\mathrm{d}{{\bm{x}}}\>\mathrm{d}{\bm{\theta}}\;,(40)𝔼​[y]≈𝔼​[f^]\displaystyle\mathbb{E}\big[y\big]\approx\mathbb{E}\big[\hat{f}\big]=∬f^​(𝒙;𝜽)\displaystyle=\iint\hat{f}(\bm{x};\bm{\theta})×p​(𝒙,𝜽∣𝒟,f^)​d​𝒙​d​𝜽,\displaystyle\hphantom{=}\,\,\times p({\bm{x}},\bm{\theta}\mid\mathcal{D},\hat{f})\>\mathrm{d}{{\bm{x}}}\>\mathrm{d}{\bm{\theta}}\;,(41)var​[y]≈var​[f^]\displaystyle\mathrm{var}\big[y\big]\approx\mathrm{var}\big[\hat{f}\big]=∬(f^​(𝒙;𝜽)−𝔼​[f^])2\displaystyle=\iint\big(\hat{f}(\bm{x};\bm{\theta})-\mathbb{E}\big[\hat{f}\big]\big)^{2}×p​(𝒙,𝜽∣𝒟,f^)​d​𝒙​d​𝜽,\displaystyle\hphantom{=}\,\,\times p({\bm{x}},\bm{\theta}\mid\mathcal{D},\hat{f})\>\mathrm{d}{{\bm{x}}}\,\mathrm{d}{\bm{\theta}}\;,(42)

where, in surrogate modeling, Bayes’ theorem implies that the joint distribution of a new input𝒙\bm{x}and the surrogate parameters𝜽\bm{\theta}, conditioned on the observed dataset𝒟\mathcal{D}and the surrogate modelf^\hat{f}, factorizes asp​(𝒙,𝜽∣𝒟,f^)=p​(𝒙)​p​(𝜽∣𝒟,𝒙,f^)p({\bm{x}},\bm{\theta}\mid\mathcal{D},\hat{f})=p({\bm{x}})\,p(\bm{\theta}\mid\mathcal{D},\cancel{{\bm{x}}},\hat{f}). This factorization shows that the posterior of the surrogate parameters𝜽\bm{\theta}is independent of a new, unseen input𝒙{\bm{x}}. It depends solely on the calibration data in𝒟\mathcal{D}, i.e., the observed input–output data pairs from simulations(𝒙(n),y(n))(\bm{x}^{(n)},y^{(n)}). A new input does not alter the uncertainty in𝜽\bm{\theta}; it only affects the model prediction at that input. The posterior changes only if additional measured data are added into𝒟\mathcal{D}.

Analogously, the posterior of the surrogate parameters can be approximated by a point mass at theiroptimalvalue𝜽∗\bm{\theta}^{\ast}, i.e.,p​(𝜽∣𝒟,f^)≈δ​(𝜽−𝜽∗).p(\bm{\theta}\mid\mathcal{D},\hat{f})\approx\delta(\bm{\theta}-\bm{\theta}^{\ast})\;.(43)

Inserting this into the marginalization over𝜽\bm{\theta}and using the
sifting property of the Dirac delta, the predictive distribution collapses to a
single evaluation of the surrogate,p​(y∣𝒙,𝒟,f^)\displaystyle p(y\mid\bm{x},\mathcal{D},\hat{f})=∫p​(y∣𝒙,𝜽,f^)​p​(𝜽∣𝒟,f^)​d𝜽\displaystyle=\int p(y\mid\bm{x},\bm{\theta},\hat{f})\,p(\bm{\theta}\mid\mathcal{D},\hat{f})\>\mathrm{d}\bm{\theta}≈p​(y∣𝒙,𝜽∗,f^).\displaystyle\approx p(y\mid\bm{x},\bm{\theta}^{\ast},\hat{f})\;.(44)

This approximation neglects the uncertainty in the surrogate parameter estimates and treats them as known exactly. As a consequence, the Bayesian formulation reduces to the standard, non-Bayesian use of the surrogate model.

The Eq. (3.3.2) strictly holds for deterministic models, where the model output is uniquely determined by the input, i.e.,p​(y∣f,𝒙)=δ​(y−f​(𝒙))p(y\mid f,\bm{x})=\delta(y-f(\bm{x}))\;.
Non-deterministic, or statistical, models would demand a prior for and to marginalize over the distribution of model valuesf^\hat{f}. In other words, the prediction requires integrating over the joint distribution of inputs𝒙\bm{x}, surrogate parameters𝜽\bm{\theta}, and model outputsf^\hat{f}conditioned on the observed data𝒟\mathcal{D}. If no surrogate is necessary and a high-fidelity model is used directly, then the dependency on𝜽{\bm{\theta}}is eliminated, but the dependency onp​(f^)p(\hat{f})remains. A simple example of such a non-deterministic model is a GP, wheref^\hat{f}is treated as a random function.

In fact, for linear surrogate parameterscpc_{p}, the integrals above can often be solved analytically — particularly for Gaussian likelihoods combined with conjugate priors, where prior and posterior share the same distributional form. The main computational challenge arises from numerically integrating over the nonlinear parameterswpw_{p}. As a result, linear methods such as PCEs are tractable (only linear parameterscpc_{p}and no non-linear parameterswpw_{p}), whereas NNs are typically intractable in a fully Bayesian treatment due to the presence of numerous nonlinear parameterswpw_{p}(cf. Ranftl et al.Ranftl and von der Linden [2021]for details).

Previously, in Section3.1, we concluded that surrogate modeling is a practical necessity for many UQ problems. Here, we have formalized surrogate modeling as an inverse problem within a Bayesian framework. Indeed, the inverse problem concerning the surrogate model is, within this framework, structurally not distinct from the inverse problem for model calibration and parameter estimation in Section3.2. We present these types of inverse problems separately merely for their distinct role they are playing in the scheme of UQ.

It is important to recognize that selecting a surrogate function in Eq. (30) constitutes a fundamental modeling choice — much like selecting a likelihood and prior for the probabilistic model or a specific constitutive model that capture physics.
Just as the combination of a constitutive model and a likelihood defines a probabilistic model for experimental data, the combination of a surrogate model and a likelihood defines a probabilistic model for simulation data. The essential distinction is that the surrogate is specifically designed to enable rapid evaluation while maintaining sufficient predictive accuracy.
While most readers are familiar with various constitutive or rheological models, we have not yet discussed specific surrogate architectures. We introduce popular classes of surrogate models along with relevant examples from the literature in Section4, and then present an illustrative mechanical example of surrogate-based UQ in Section4.8

## 3.4Example: Hierarchical inference of Young’s modulus from uniaxial tensile tests

As a first basic example, consider a uniaxial tensile test performed on five biological soft tissue samples obtained from five different patients. For clarity of exposition, we adopt a simple linear-elastic constitutive model for calibration against the experimental data. This allows us to focus entirely on the probabilistic aspects of the inference problem rather than on additional complexities of the physical model.

Patient-specific level inference. In the first hierarchical step, we aim to infer patient-specific parameters, i.e., we calibrate the constitutive model for each of the five different samples. We believe this is a natural first step because it accounts for individual variability before attempting to identify population-level trends.
Under the assumption of incompressible linear elasticity, the stress–strain relationship is governed by a single unknown material parameter: the Young’s modulusEE. In accordance with the introduced notation, we define the model parameter as𝒙=E\bm{x}=Eand the control parameter (strain) as𝝃=ε\bm{\xi}=\varepsilon, while the experimental output (stress) is denoted asyexpy_{\rm exp}. For each of the five samples, we denote the patient-specific Young’s modulus byEiE_{i},i=1,…,5i=1,\dots,5.

For experimentii, the observed data consist ofN=100N=100strain–stress pairs,𝒟exp,i=(εi(n),yexp,i(n))n=1N,\displaystyle\mathcal{D}_{{\rm exp},i}=\big(\varepsilon_{i}^{(n)},y_{{\rm exp},i}^{(n)}\big)_{n=1}^{N}\;,(45)

and the complete dataset is𝒟exp=(𝒟exp,i)i=15\mathcal{D}_{{\rm exp}}=(\mathcal{D}_{{\rm exp},i})_{i=1}^{5}.

We can now define the forward model for experimentiiand measurement pointnnwith additive Gaussian measurement noise asyexp,i(n)=f​(εi(n);Ei)+η,\displaystyle y_{{\rm exp},i}^{(n)}=f\big(\varepsilon_{i}^{(n)};E_{i}\big)+\eta\;,η∼𝒩​(0,σmeas2),\displaystyle\eta\sim\mathcal{N}(0,\sigma_{\rm meas}^{2})\;,(46)

where the model is given byf​(εi(n);Ei)=Ei​εi(n)f\big(\varepsilon_{i}^{(n)};E_{i}\big)=E_{i}\,\varepsilon_{i}^{(n)}. We assume the noise termsη\etaare statistically independent across experimentsiiand measurement pointsnn.111111In practice, each measurement is typically assumed to be normally distributed around the model prediction. While this Gaussian noise assumption is a strong simplification, it is a standard choice in the absence of detailed information regarding noise statisticsFurthermore, the varianceσmeas2\sigma_{\rm meas}^{2}is assumed to be known from device calibration and identical for all experiments, since the same experimental setup was used throughout. Repeated testing on the same specimen is not feasible in this example, as irreversible damage during the initial loading cycle — a common occurrence in biological tissues — cannot be ruled out.

Under the independence assumption, the likelihood factorizes over experiments and measurement points. Up to proportionality constants, this yieldsp​(𝒟exp∣Ei,σmeas)∝∏i=15exp⁡(−12​σmeas2​∑n=1N(yexp,i(n)−Ei​εi(n))2).p(\mathcal{D}_{{\rm exp}}\mid E_{i},\sigma_{\rm meas})\\
\propto\prod_{i=1}^{5}\exp\left(-\frac{1}{2\sigma_{\rm meas}^{2}}\sum_{n=1}^{N}\left(y_{{\rm exp},i}^{(n)}-E_{i}\varepsilon_{i}^{(n)}\right)^{2}\right)\;.(47)

We assume a flat (improper) prior on each modulus withp​(Ei)∝1p(E_{i})\propto 1, which we assume to be positive, so that the posterior is proportional to the likelihoodp​(Ei∣𝒟exp,σmeas)∝p​(𝒟exp∣Ei,σmeas).p(E_{i}\mid\mathcal{D}_{{\rm exp}},\sigma_{\rm meas})\propto p(\mathcal{D}_{{\rm exp}}\mid E_{i},\sigma_{\rm meas})\;.(48)

Taking the negative logarithm and omitting additive constants yields−log⁡p​(Ei∣𝒟exp,σmeas)=12​σmeas2​∑i=15∑n=1N(yexp,i(n)−Ei​εi(n))2.-\log p(E_{i}\mid\mathcal{D}_{{\rm exp}},\sigma_{\rm meas})\\
=\frac{1}{2\sigma_{\rm meas}^{2}}\sum_{i=1}^{5}\sum_{n=1}^{N}\left(y_{{\rm exp},i}^{(n)}-E_{i}\varepsilon_{i}^{(n)}\right)^{2}\;.(49)

which demonstrates that maximizing the posterior is equivalent to minimizing this quadratic objective function.

Since each experiment is treated independently, the prefactor1/σmeas21/\sigma_{\rm meas}^{2}merely rescales the objective function without affecting the location of its minimum. Consequently, the MAP estimate for each experimentiireduces to the classical least-squares estimatorEiMAP=arg⁡minEi>0​∑n=1N(yexp,i(n)−Ei​εi(n))2.E_{i}^{\mathrm{MAP}}=\arg\min_{E_{i}>0}\sum_{n=1}^{N}\left(y_{{\rm exp},i}^{(n)}-E_{i}\varepsilon_{i}^{(n)}\right)^{2}\;.(50)

as expected when combining a flat prior with Gaussian noise.

To quantify uncertainty, we approximate the posterior distribution. A flat prior
combined with a Gaussian likelihood admits an analytical posterior for this
problem121212Under a flat prior, the posterior is proportional to the likelihood, so its logarithm equals the log-likelihood Eq. (49) up to an additive constant. Expanding the square and completing it inEiE_{i}yields∑n=1N(yexp,i(n)−Ei​εi(n))2=∑n=1N(εi(n)​(Ei−EiMAP))2+const\sum_{n=1}^{N}\big(y_{{\rm exp},i}^{(n)}-E_{i}\varepsilon_{i}^{(n)}\big)^{2}=\sum_{n=1}^{N}\big(\varepsilon_{i}^{(n)}\big(E_{i}-E_{i}^{\rm MAP}\big)\big)^{2}+\,\text{const}, withEiMAP=∑n=1Nyexp,i(n)​εi(n)/∑n=1N(εi(n))2E_{i}^{\rm MAP}=\sum_{n=1}^{N}y_{{\rm exp},i}^{(n)}\varepsilon_{i}^{(n)}\big/\sum_{n=1}^{N}\big(\varepsilon_{i}^{(n)}\big)^{2}, where the constant collects all terms independent ofEiE_{i}and is absorbed into the normalization. Matching this quadratic exponent with that of a Gaussian density identifies the posterior as𝒩​(EiMAP,σEi2)\mathcal{N}(E_{i}^{\rm MAP},\sigma_{E_{i}}^{2})withσEi2=σmeas2/∑n=1N(εi(n))2\sigma_{E_{i}}^{2}=\sigma_{\rm meas}^{2}\big/\sum_{n=1}^{N}\big(\varepsilon_{i}^{(n)}\big)^{2}.,
but we proceed numerically and approximate it locally around the MAP estimate
through a Laplace approximation, since closed-form posteriors are unavailable in
many mechanical problems. This corresponds to a second-order Taylor expansion of
the negative log-posterior aroundEiMAPE_{i}^{\mathrm{MAP}}.
For a single experimentii, the second derivative of the negative log-posterior is given by∂2∂Ei2​[−log⁡p​(Ei∣𝒟exp,i,σmeas)]=1σmeas2​∑n=1N(∂f​(εi(n);Ei)∂Ei)2,\frac{\partial^{2}}{\partial E_{i}^{2}}\left[-\log p(E_{i}\mid\mathcal{D}_{{\rm exp},i},\sigma_{\rm meas})\right]\\
=\frac{1}{\sigma_{\rm meas}^{2}}\sum_{n=1}^{N}\left(\frac{\partial f(\varepsilon_{i}^{(n)};E_{i})}{\partial E_{i}}\right)^{2}\;,(51)

where∂f​(εi(n);Ei)/∂Ei=εi(n)\partial f(\varepsilon_{i}^{(n)};E_{i})/\partial E_{i}=\varepsilon_{i}^{(n)}.

The Laplace approximation therefore yields a Gaussian posterior,p​(Ei∣𝒟exp,i,σmeas)≈𝒩​(EiMAP,σEi2),p(E_{i}\mid\mathcal{D}_{{\rm exp},i},\sigma_{\rm meas})\approx\mathcal{N}\left(E_{i}^{\mathrm{MAP}},\sigma_{E_{i}}^{2}\right)\;,(52)

with posterior varianceσEi2≈[1σmeas2​∑n=1N(εi(n))2]−1,\sigma_{E_{i}}^{2}\approx\left[\frac{1}{\sigma_{\rm meas}^{2}}\sum_{n=1}^{N}\left(\varepsilon_{i}^{(n)}\right)^{2}\right]^{-1}\;,(53)

analogously to the analytical solution in Footnote12.

It should be noted that neither the MAP estimate nor the Laplace approximation is fully Bayesian in the strict sense: the MAP estimate reduces the full posterior to a single point, while the Laplace approximation subsequently approximates the posterior with a Gaussian distribution, rather than computing the full PDF. Nevertheless, both provide computationally tractable uncertainty estimates. The results of this first step are presented in Fig.5(a) for synthetic experimental data, yielding MAP estimates with Laplace approximations for each individual test. Note that the Laplace bands are narrow, which reflects the relatively large number of measurement points available.

Population-level inference. In the second hierarchical step, we aim to infer a population-representative Young’s modulus,EpopE_{\rm pop}, from the five patient-specific parameters{Ei}i=15\{E_{i}\}_{i=1}^{5}estimated in the first step.
We can now interpret these patient-specific parameters as independent realizations of an underlying population distribution. Specifically,Ei∼𝒩​(Epop,σpop2),E_{i}\sim\mathcal{N}(E_{\rm pop},\sigma_{\rm pop}^{2})\;,(54)

whereσpop2\sigma_{\rm pop}^{2}represents the unknown population variance. Since biological variability is assumed to dominate measurement noise in this example, we setσmeas2≈0\sigma_{\rm meas}^{2}\approx 0and treat the inferredEiE_{i}as direct observations from the underlying population distribution.

As weakly informative priors we choose, assuming independence betweenEpopE_{\rm pop}andσpop\sigma_{\rm pop},p​(Epop)∝1,p​(σpop)∝1σpop,p(E_{\rm pop})\propto 1\;,\quad p(\sigma_{\rm pop})\propto\frac{1}{\sigma_{\rm pop}}\;,(55)

where the prior onσpop>0\sigma_{\rm pop}>0is the scale-invariant Jeffreys prior. As we will see, these prior assumptions lead to a Student-ttposterior distribution forEpopE_{\rm pop}.

If we assume that the five realizations are normally distributed, the likelihood readsp​(Ei∣Epop,σpop)∝σpop−N​exp⁡(−12​σpop2​∑i=15(Ei−Epop)2).p(E_{i}\mid E_{\rm pop},\sigma_{\rm pop})\\
\propto\sigma_{\rm pop}^{-N}\exp\left(-\frac{1}{2\sigma_{\rm pop}^{2}}\sum_{i=1}^{5}(E_{i}-E_{\rm pop})^{2}\right)\;.(56)

and applying Bayes’ theorem yields the joint posteriorp​(Epop,σpop∣Ei)\displaystyle p(E_{\rm pop},\sigma_{\rm pop}\mid E_{i})∝p​(Ei∣Epop,σpop)\displaystyle\propto p(E_{i}\mid E_{\rm pop},\sigma_{\rm pop})×p​(Epop)​p​(σpop),\displaystyle\hphantom{\propto}\;\times p(E_{\rm pop})p(\sigma_{\rm pop})\;,(57)

which explicitly includes the prior of the unknown population varianceσpop2\sigma_{\rm pop}^{2}; cf. Eq. (48), where no such hyperparameter was present.

To proceed analytically, we employ the standard sum-of-squares decomposition∑i=15(Ei−Epop)2=∑i=15(Ei−E¯)2+5​(Epop−E¯)2,\sum_{i=1}^{5}(E_{i}-E_{\rm pop})^{2}=\sum_{i=1}^{5}(E_{i}-\bar{E})^{2}+5(E_{\rm pop}-\bar{E})^{2}\;,(58)

whereE¯=15​∑i=15Ei\bar{E}=\frac{1}{5}\sum_{i=1}^{5}E_{i}denotes the arithmetic mean of the realizations, andS=∑i=15(Ei−E¯)2S=\sum_{i=1}^{5}(E_{i}-\bar{E})^{2}is the centered sum of squares. The variances2=(1/(5−1))​Ss^{2}=(1/(5-1))Sserves as an unbiased estimator of the population varianceσpop2\sigma_{\rm pop}^{2}.

With the aim of eliminating the unknown population varianceσpop2\sigma_{\rm pop}^{2}, we marginalize the joint posterior by integrating outσpop\sigma_{\rm pop}p​(Epop∣Ei)∝∫0∞σpop−(N+1)×exp⁡(−12​σpop2​[S+5​(Epop−E¯)2])​d​σpop.p(E_{\rm pop}\mid E_{i})\propto\int_{0}^{\infty}\sigma_{\rm pop}^{-(N+1)}\\
\times\exp\left(-\frac{1}{2\sigma_{\rm pop}^{2}}\left[S+5(E_{\rm pop}-\bar{E})^{2}\right]\right)\>\mathrm{d}\sigma_{\rm pop}\;.(59)

Performing this integration (cf.Wollner et al. [2026]) and omitting multiplicative constants yields the normalized formp​(Epop∣Ei)∝(1+5​(Epop−E¯)2S)−5/2,p(E_{\rm pop}\mid E_{i})\propto\left(1+\frac{5(E_{\rm pop}-\bar{E})^{2}}{S}\right)^{-5/2}\;,(60)

which is recognized as a Student-ttdistribution centered at the sample arithmetic meanE¯\bar{E}with 4 degrees of freedom.
This result reveals several key properties. First, the posterior mean ofEpopE_{\rm pop}coincides with the sample mean𝔼​[E¯]=Epop,\mathbb{E}[\bar{E}]=E_{\rm pop}\;,(61)

and second, the estimator of the population variance is unbiased𝔼​[s2]=σpop2.\mathbb{E}[s^{2}]=\sigma_{\rm pop}^{2}\;.(62)

Importantly, however, the population-representative Young’s modulus is not simply the arithmetic average of the five samples. Rather, it is characterized by a full posterior that consistently accounts for both between-sample variability and limited data. The Student-ttform reflects this uncertainty: it has heavier tails than a Gaussian, appropriately reflecting the additional uncertainty arising from the small sample size.

Figure5(b) illustrates the results of this second step, showing the five MAP estimatesEiMAPE_{i}^{\text{MAP}}obtained from the first hierarchical step, the inferred population arithmetic meanE¯\bar{E}, and the corresponding 95% credible interval forEpopE_{\rm pop}. The wide interval demonstrates the considerable uncertainty in estimating the population parameter from only five samples, as expected from the Student-ttposterior with 4 degrees of freedom.Figure 5:(a) Sketch of a uniaxial tensile test, where (b) colored scatter points show the noisy experimental engineering stress–stretch data obtained from five soft biological tissue samples. Solid colored lines represent the individual maximum a posteriori (MAP) estimates of Young’s modulus for each experiment,EiMAPE_{i}^{\rm MAP}. The shaded colored bands denote the Laplace approximation of the parameter posterior (detaile view), quantifying uncertainty in the estimated modulus arising from measurement noise within each individual dataset.
(c) The black line shows the arithmetic mean,E¯\bar{E}, serving as an estimate of the population represenative Young’s modulus. The gray shaded band indicates the 95% credible interval (CI) obtained from the Student-ttposterior. This interval quantifies uncertainty in the population arithmetic mean arising from variability between experiments and the small number of realizations.

## 4Popular surrogate models

## 4.1General concept

Let us recall the general concept of surrogate modeling, introduced as an inverse problem in Section3.3, where the surrogate modelf^​(𝒙;𝜽)\hat{f}(\bm{x};\bm{\theta})is parameterized by the surrogate parameters𝜽\bm{\theta}and represented as an expansion (cf. Eq. (31)).

With this formulation in mind, we now explore different ways how the surrogate functionf^\hat{f}can be constructed.
For instance, the basis functionsϕp\phi_{p}(Eq. (31)) may be chosen as simple polynomials, in which case the surrogate function represents a polynomial expansion. When prior knowledge about the distribution of𝒙\bm{x}is available, it can be advantageous to select these polynomials accordingly, leading to the PCE described in the following Section4.2. Alternatively, the basis functionsϕp\phi_{p}can be defined through kernel representations, giving rise to GP regression, which can also be viewed as a Bayesian form of machine learning, as shown in the subsequent Section4.3. Finally, by allowing the nonlinear parameterswpw_{p}to be trainable as well, we arrive at more flexible surrogate models inspired by modern machine learning, as discussed later in Sections4.4and4.5.

## 4.2Polynomial chaos expansion

A popular choice for surrogate modeling is PCEsWiener [1938]. Consistent with the notation above, we consider a forward mapf:𝒙↦yf:\bm{x}\mapsto y, which maps input𝒙\bm{x}to outputyy. We approximate this map by a PCE surrogate, denoted asf^PCE:𝒙↦y^.\hat{f}_{\rm PCE}:\bm{x}\mapsto\hat{y}\;.(63)

The PCE surrogate is then defined as a finite expansionf^PCE​(𝒙;𝜽)=∑p=0Pcp​ϕp​(𝒙),\hat{f}_{\rm PCE}(\bm{x};\bm{\theta})=\sum_{p=0}^{P}c_{p}\phi_{p}(\bm{x})\;,(64)

whereϕp​(𝒙)\phi_{p}(\bm{x})are prescribed (multivariate) polynomial basis functions and𝜽=(c0,…,cP)T\bm{\theta}=(c_{0},\ldots,c_{P})^{\rm T}denotes the vector of unknown expansion coefficients.
This approach can be viewed as a special, linear case of the generalized model introduced in Eq. (31), in which the nonlinear parameterswpw_{p}are fixed, the basis functionsϕp\phi_{p}are specific types of polynomials, and only the linear coefficientscpc_{p}are treated as unknown variables.

A defining feature of PCEs is the choice of basis. The polynomial basis functionsϕp​(𝒙)\phi_{p}(\bm{x})are constructed to be orthonormal with respect to the probability distribution of the input parameters. This orthonormality condition is defined as∫ϕp​(𝒙)​ϕq​(𝒙)​p​(𝒙)​d𝒙=!δp,q,\displaystyle\int\phi_{p}(\bm{x})\phi_{q}(\bm{x})p(\bm{x})\>\mathrm{d}\bm{x}\stackrel{{\scriptstyle!}}{{=}}\delta_{p,q}\;,(65)

wherep​(𝒙)p(\bm{x})is the joint probability density of theDD-dimensional input random vector𝒙\bm{x}andδp,q\delta_{p,q}denotes the Kronecker delta. Here,ppandqqindex different polynomial basis functions in the expansion. This orthogonality ensures that each basis function captures a distinct, non-overlapping contribution to the variance of the surrogate modelf^PCE​(𝒙;𝜽)\hat{f}_{\rm PCE}(\bm{x};\bm{\theta}). The advantage of that will become more clear in Section7, or seeRanftl and von der Linden [2021]for details.

If all input parameters are independent, i.e., the input distribution factorizes asp​(𝒙)=∏i=1D𝒙p​(xi)p(\bm{x})=\prod_{i=1}^{D_{\bm{x}}}p(x_{i}), the multivariate basis functions admit a tensor-product form,ϕp​(𝒙)=∏k=1D𝒙ψαk​(xk),\phi_{p}(\bm{x})=\prod_{k=1}^{D_{\bm{x}}}\psi_{\alpha_{k}}(x_{k})\;,(66)

whereψαk​(xk)\psi_{\alpha_{k}}(x_{k})is a univariate polynomial of degreeαk\alpha_{k}in thekk-th input dimension. Each scalar indexppcorresponds to a unique multi-index𝜶=(α1,…,αD)\bm{\alpha}=(\alpha_{1},\ldots,\alpha_{D})and truncating the expansion amounts to restricting the admissible set of multi-indices. For standard input distributions, the resulting basis functionsϕp\phi_{p}correspond to well-known families of orthogonal polynomialsXiu and Karniadakis [2002]: Hermite polynomials for Gaussian inputs, Legendre polynomials for uniform inputs, Laguerre polynomials for Gamma-distributed inputs, etc.

Historically, PCEs were developed for discretizing stochastic differential equations in parameter space, analogously to Galerkin projectionsGhanem and Spanos [1991]. This class of methods is often referred to asintrusive UQGhanem et al. [2017], as it typically requires direct modifications of the underlying numerical solver (e.g., finite element solver).

In contrast, thenon-intrusiveapproach used here treats the solver as a black box: simulation data are generated first and the PCE is then constructed by solving a regression problem following the generalized model in Eq. (31), which is linear in the unknown coefficients.

Within the introduced Bayesian framework, this corresponds to an inverse problem in which we infer the surrogate parameters𝜽=cp\bm{\theta}=c_{p}given simulation data𝒟=(𝒙(n),y(n))n=1N\mathcal{D}=(\bm{x}^{(n)},y^{(n)})_{n=1}^{N}, subject to the orthogonality constraint in Eq. (65). Under these assumptions, the PCE coefficients can be obtained by solving the inference problem in Eq. (32), i.e., the optimization over𝜽\bm{\theta}. Furthermore, select Bayesian estimates according to Eq. (35) admit closed form expression (cf. Ranftl et al.Ranftl and von der Linden [2021]) as well.

For the PCE surrogate, maximizing the Gaussian likelihood is equivalent to a least-squares fit with fixed nonlinear parameterswpw_{p}. The optimal coefficient vector𝒄=(c0,⋯,cP)T{\bm{c}}=(c_{0},\cdots,c_{P})^{\rm T}is then given in closed form by𝒄∗=(ΦT​Φ)−1​ΦT​𝒚,\displaystyle{\bm{c}}^{\ast}=(\Phi^{\rm T}\Phi)^{-1}\Phi^{\rm T}{\bm{y}}\;,(67)

where𝒚=(y(1),⋯,y(N))T{\bm{y}}=(y^{(1)},\cdots,y^{(N)})^{\rm T}and the design matrix satisfies[Φ]n​p=ϕp​(𝒙(n))[\Phi]_{np}=\phi_{p}({\bm{x}}^{(n)})\;.
Thus, least squares arises as the maximum likelihood estimate under a Gaussian likelihood, or equivalently as a MAP estimate with a flat prior. The MAP estimate then happens to coincide also with the expected value. In other words, the familiar least-squares fit appears as a special case of Eq. (32). In contrast, introducing a non-uniform prior on𝒄{\bm{c}}(e.g., a Laplace prior, corresponding to Lasso regularization) eliminates the closed-form solution for Eq. (32) and requires numerical optimization methods.

From a Bayesian perspective on regressionO’Hagan [2013], the PCE basis functions may appear restrictive. The orthonormality condition (Eq. (65)) is simple to satisfy only when the inputs are independent and follow certain standard probability distributions, making the construction of orthonormal PCE bases for experimentally or simulation-derived input densitiesp​(𝒙∣𝒟)p(\bm{x}\mid\mathcal{D})often more involvedOladyshkin and Nowak [2012], Jakeman et al. [2019], Torre et al. [2019]. Nevertheless, the choice of basis is a modeling decision and non-orthogonal bases may be used when appropriate.

The main advantages of PCEs are interpretability and computational efficiency. When the input distributionp​(𝒙)p(\bm{x})has a standard form, such as Gaussian, Beta, or Gamma and factorizes into independent componentsXiu and Karniadakis [2005], Sudret [2008], Crestaux et al. [2009], the variance and conditional variances of the outputyyadmit simple, closed-form solutions. Once the surrogate model is learned, uncertainty propagation becomes essentially free, requiring no numerical integration. This is especially valuable for sensitivity analysis, see Section7. These advantages extend to non-standard or non-factorizing distributions, as detailed inOladyshkin and Nowak [2012], Jakeman et al. [2019], Torre et al. [2019].

The main PCE limitations are (i) poor scalability to high-dimensional inputs and (ii) restricted ability to model correlations. For (i), the number of polynomials and coefficients grows combinatorially with polynomial order and input dimension, limiting standard PCEs to about 20 variables. Various numerical techniques address this, often under additional assumptions or constraints, including hyperbolic truncationMühlpfordt et al. [2017]and sparse, adaptive, or collocation strategiesZhang et al. [2011], Foo and Karniadakis [2010], Blatman and Sudret [2011], Doostan and Owhadi [2011], Lüthen et al. [2021]. However, scalability remains limited without low effective dimension.

To address this challenge, several studies combine PCEs with NNsZhang et al. [2019], Schwab and Zech [2019], Cooper [2021], Zheng et al. [2021], Lütjens et al. [2021], Zheng et al. [2022], Oladyshkin et al. [2023], Yao et al. [2023], Bahmani et al. [2025]to leverage NN scalability. Most NN-based PCE methods achieve improved scalability but sacrifice exact analytical expressions for conditional variances, which are the key advantage of PCEs. A notable exception isDeepPCEExenberger et al. [2026], which preserves exact conditional variances while offering NN-like scalability.

PCEs have long been well-established as surrogate models in (bio)mechanics, predominantly with deterministic hyperparameters; for example, as surrogates for nonlinear constitutive modelsCampos et al. [2023], for uncertainty propagation of cardiac myofiber orientation and stiffnesses in a computational model of left ventricle deformationRodríguez-Cantano et al. [2019], or to study the sensitivity of morphological parameters affecting false lumen thrombosis following aortic dissectionJafarinia et al. [2023], to name only a few.

## 4.3Machine learning I: Gaussian process regression

In contrast to PCE, which relies on fixed orthogonal polynomial bases and assumes a specific structure in the input distributions, GP regression performs surrogate modeling by defining a probability distribution over functions. Originally established in spatial statistics and UQ under the nameKrigingKrige [1951], O’Hagan [1978], GP regression has experienced a popular revival the machine learning community as a flexible, non-parametric methodRasmussen and Williams [2006]. Here, the termnon-parametricrefers to the fact that we do not assume a specific parametric form for the function itself. Instead, we specify a parametrization of the statistics of, or equivalently thedistributionover, possible functions.

Again, we consider a general forward map,f:𝒙↦yf:\bm{x}\mapsto y, mapping an input vector𝒙\bm{x}to an outputyy, and its surrogatef^GP:𝒙↦y^.\hat{f}_{\rm GP}:\bm{x}\mapsto\hat{y}\;.(68)

Rather than expanding the target function, i.e., the forward modelffin a predefined basis, GPs define a probability distribution directly over the space of possible surrogate functionsf^GP\hat{f}_{\rm GP}. This allows the model to infer both the functional form and its associated uncertainty from the data itself, without committing to a particular functional forma priori. This does not remove prior assumptions but shifts them. Instead of a basis, one specifies a mean and a covariance (kernel) function. The kernel and its hyperparameters encode assumptions on smoothness, correlation length, and stationarity, which
implicitly define the function space in which the surrogate is inferred.

Per definition, given an input space𝒳⊂ℝD𝒙\mathcal{X}\subset\mathbb{R}^{D_{\bm{x}}}, a GP is a collection of random variables, any finite subset of which follows a joint Gaussian distribution. Colloquially, a GP can be understood as an infinite-dimensional extension of the multivariate Gaussian distribution to functions. Although this concept may appear abstract at first, the resulting equations are remarkably simple.
For a random functionf^GP:𝒳→ℝ\hat{f}_{\rm GP}:\mathcal{X}\rightarrow\mathbb{R}we writef^GP∼GP​(μ​(𝒙),k​(𝒙,𝒙′)),\hat{f}_{\rm GP}\sim\mathrm{GP}(\mu(\bm{x}),k(\bm{x},\bm{x}^{\prime}))\;,(69)

whereμ​(𝒙)=𝔼​[f^GP​(𝒙)]\mu(\bm{x})=\mathbb{E}\big[\hat{f}_{\rm GP}(\bm{x})\big]is the mean function, andk​(𝒙,𝒙′;𝜽)=cov​[f^GP​(𝒙),f^GP​(𝒙′)]k(\bm{x},\bm{x}^{\prime};\bm{\theta})=\mathrm{cov}\,[\hat{f}_{\rm GP}(\bm{x}),\hat{f}_{\rm GP}(\bm{x}^{\prime})]is the covariance function parametrized by surrogate parameters𝜽\bm{\theta}. The covariance function, often called thekernelin machine learning, encodes prior assumptions about smoothness, periodicity, or other structural properties of the unknown forward modelff. The GP framework therefore enables us to express such prior beliefs and to obtain posterior predictive distributions that quantify uncertainty in the surrogate modelf^GP\hat{f}_{\rm GP}given observed training data.

In surrogate modeling, the GP is typically employed as apriorover functions in a Bayesian setting. In GP regression, observations are assumed to be corrupted by Gaussian noise. If this likelihood is also Gaussian, then the resulting posterior is also Gaussian due to conjugacy with the Gaussian prior, ensuring analytical tractability — the posterior can be computed in closed form. For simplicity, we consider in the following zero-mean priors, i.e.,μ​(𝒙)≡0\mu(\bm{x})\equiv 0, meaning we do not assume any systematic trend or offset in the function; a rationale for this choice will be discussed later.

For the covariance function, we require only two basic properties to ensure that the GP is well-defined. First, the kernel must be symmetric, meaning it gives the same value regardless of the order of its inputs:k​(𝒙,𝒙′)=k​(𝒙′,𝒙)k(\bm{x},\bm{x}^{\prime})=k(\bm{x}^{\prime},\bm{x}). Second, it must be positive semi-definite, which guarantees that the covariance matrices constructed from the kernel are valid and correspond to a meaningful probabilistic model131313Note that this property ensures, in particular, that the resulting variances — diagonal entries of the covariance matrix — are non-negative, since a negative variance would not define a proper probability distribution. In analogy,e−x2e^{-x^{2}}is normalizable, whereasex2e^{x^{2}}is not.. Formally, for any set of points(𝒙(1),…,𝒙(n))⊂𝒳(\bm{x}^{(1)},\ldots,\bm{x}^{(n)})\subset\mathcal{X}and any real coefficientsa1,…,ana_{1},\ldots,a_{n}, it holds that∑i=1n∑j=1nai​aj​k​(𝒙(i),𝒙(j))≥0\sum_{i=1}^{n}\sum_{j=1}^{n}a_{i}a_{j}k(\bm{x}^{(i)},\bm{x}^{(j)})\geq 0.

A default choice for the kernel is the so-calledsquared-exponentialkernel, also known as the radial basis function (RBF),k​(𝒙,𝒙′;𝜽)=σf2​exp⁡(−‖𝒙−𝒙′‖22​ι2),\displaystyle k(\bm{x},\bm{x}^{\prime};{\bm{\theta}})=\sigma^{2}_{f}\exp\left(-\frac{\|\bm{x}-\bm{x}^{\prime}\|^{2}}{2\iota^{2}}\right)\;,(70)

whereσf2\sigma^{2}_{f}is the signal variance or prior variance magnitude andι\iotais the correlation length. An entire zoo of symmetric, positive semi-definite kernel functions is available in the literatureAbrahamsen [1997], Cuturi [2009], Duvenaud [2014]. In the following, we will occasionally omit to explicitly denote the dependence ofk​(𝒙,𝒙′;𝜽)k(\bm{x},\bm{x}^{\prime};{\bm{\theta}})on𝜽{\bm{\theta}}.

We now compute the posterior predictive.
Given regrouped training data𝒟=(𝒙(n),y(n))n=1N=(𝐱¯,𝒚)\mathcal{D}=(\bm{x}^{(n)},y^{(n)})_{n=1}^{N}=(\underline{\mathrm{\bm{x}}},{\bm{y}}), with𝐱¯=(𝒙(1),⋯,𝒙(N))T\underline{\mathrm{\bm{x}}}=(\bm{x}^{(1)},\cdots,\bm{x}^{(N)})^{\rm T}and𝒚=(y(1),⋯,y(N))T{\bm{y}}=(y^{(1)},\cdots,y^{(N)})^{\rm T}, we assume noisy evaluationsy(n)=f​(𝒙(n))+ηy^{(n)}=f(\bm{x}^{(n)})+\eta, whereη∼𝒩​(0,σ2)\eta\sim\mathcal{N}(0,\sigma^{2})is Gaussian i.i.d. noise. We collect the latent (noise-free) function values in the vector𝒇=(f​(𝒙(1)),…,f​(𝒙(N)))T∈ℝN\bm{f}=\big(f(\bm{x}^{(1)}),\ldots,f(\bm{x}^{(N)})\big)^{\rm T}\in\mathbb{R}^{N}. The likelihood is therefore𝒚∣𝒇,𝐱¯∼𝒩​(0,σ2​I){\bm{y}}\mid{\bm{f}},\underline{\mathrm{\bm{x}}}\sim\mathcal{N}(0,\sigma^{2}I), whereI∈ℝN×NI\in\mathbb{R}^{N\times N}is the identity matrix, and the GP prior isp​(𝒇∣𝐱¯,𝜽)=𝒩​(0,K)p({\bm{f}}\mid\underline{\mathrm{\bm{x}}},{\bm{\theta}})=\mathcal{N}(0,K). Per Bayes’ theorem,p​(𝒇∣𝒟,𝜽)=1Z​p​(𝒚∣𝒇,𝐱¯,𝜽)​p​(𝒇∣𝐱¯,𝜽)p({\bm{f}}\mid\mathcal{D},{\bm{\theta}})=\frac{1}{Z}p({\bm{y}}\mid{\bm{f}},\underline{\mathrm{\bm{x}}},\cancel{{\bm{\theta}}})p({\bm{f}}\mid\underline{\mathrm{\bm{x}}},{\bm{\theta}}), whereZZdenotes the marginal likelihood (cf. Eq. (4.3)). For a new input𝒙∗\bm{x}_{\ast}, the joint prior off∗f_{\ast}and𝒇\bm{f}is Gaussian,p​(f∗,𝒇∣𝒙∗,𝜽)=𝒩​(0,[K𝒌∗𝒌∗Tk​(𝒙∗,𝒙∗)]),p(f_{\ast},\bm{f}\mid\bm{x}_{\ast},\bm{\theta})=\mathcal{N}\big(0,\begin{bmatrix}K&{\bm{k}}_{\ast}\\
{\bm{k}}_{\ast}^{\rm T}&k({\bm{x}}_{\ast},{\bm{x}}_{\ast})\end{bmatrix}\big)\;,whereK∈ℝN×NK\in\mathbb{R}^{N\times N}is the Gram matrix with entries[K]i​j=k​(𝒙(i),𝒙(j))[K]_{ij}=k(\bm{x}^{(i)},\bm{x}^{(j)}), and𝒌∗=(k​(𝒙∗,𝒙(1)),…,k​(𝒙∗,𝒙(N)))T∈𝑹N{\bm{k}}_{*}=\big(k(\bm{x}_{*},\bm{x}^{(1)}),\dots,k(\bm{x}_{*},\bm{x}^{(N)})\big)^{\rm T}\in\bm{R}^{N}is the covariance vector between the new input and the training inputs.

The predictive distribution is obtained by conditioning this joint Gaussian on the known training values. Using the definition of conditional probability,p​(f∗∣𝒇,𝒙∗,𝜽)=p​(f∗,𝒇∣𝒙∗,𝜽)p​(𝒇∣𝒙∗,𝜽),p(f_{\ast}\mid\bm{f},\bm{x}_{\ast},\bm{\theta})=\frac{p(f_{\ast},\bm{f}\mid\bm{x}_{\ast},\bm{\theta})}{p(\bm{f}\mid\cancel{\bm{x}_{\ast}},\bm{\theta})}\;,(71)

where the denominator does not depend on𝒙∗\bm{x}_{\ast}, since the training values𝒇\bm{f}are independent of the new input. Because the joint distribution is Gaussian, this conditioning yields the familiar closed-form expressions for the predictive mean and variance.

The predictive distribution above conditions on the latent training values𝒇\bm{f}. However, these values are not known exactly; instead, they are distributed according to the posteriorp​(𝒇∣𝒟,𝜽)p(\bm{f}\mid\mathcal{D},\bm{\theta}). Therefore, to obtain the full posterior predictive distribution at a new input𝒙∗\bm{x}_{\ast}we must marginalize over the uncertainty in𝒇\bm{f}. This yieldsp​(f∗∣𝒙∗,𝒟,𝜽)\displaystyle p(f_{\ast}\mid\bm{x}_{*},\mathcal{D},\bm{\theta})=∫p​(f∗∣𝒇,𝒙∗,𝒟,𝜽)​p​(𝒇∣𝒟,𝜽)​d𝒇\displaystyle=\int p(f_{\ast}\mid\bm{f},\bm{x}_{\ast},\cancel{\mathcal{D}},\bm{\theta})p(\bm{f}\mid\mathcal{D},\bm{\theta})\>\mathrm{d}\bm{f}=𝒩​(μ​(𝒙∗),σ2​(𝒙∗)),\displaystyle=\mathcal{N}\big(\mu(\bm{x}_{*}),\sigma^{2}(\bm{x}_{*})\big)\,,(72)

which, owing to the Gaussian assumptions of the model, results again in a Gaussian distribution. The associated posterior mean and variance areμ​(𝒙∗)=𝒌∗T​(K+σ2​I)−1​𝒚,σ2​(𝒙∗)=k​(𝒙∗,𝒙∗)−𝒌∗T​(K+σ2​I)−1​𝒌∗.\displaystyle\begin{split}\mu(\bm{x}_{*})&=\bm{k}_{*}^{\rm T}(K+\sigma^{2}I)^{-1}\bm{y}\;,\\
\sigma^{2}(\bm{x}_{*})&=k(\bm{x}_{*},\bm{x}_{*})-\bm{k}_{*}^{\rm T}(K+\sigma^{2}I)^{-1}\bm{k}_{*}\;.\end{split}(73)

Since the parameter posterior for𝜽∗{\bm{\theta}}^{\ast}is usually intractable,optimalhyperparameters𝜽\bm{\theta}are often obtained by maximizing the log marginal likelihood. The marginal likelihood is defined asp​(𝒚∣𝐱¯,𝜽)=∫p​(𝒚∣𝒇,𝐱¯,𝜽)​p​(𝒇∣𝐱¯,𝜽)​d𝒇p({\bm{y}}\mid\underline{\mathrm{\bm{x}}},{\bm{\theta}})=\int p({\bm{y}}\mid{\bm{f}},\underline{\mathrm{\bm{x}}},\cancel{{\bm{\theta}}})p({\bm{f}}\mid\underline{\mathrm{\bm{x}}},{\bm{\theta}})\>\mathrm{d}{\bm{f}}, that is, by integrating out the latent function values𝒇\bm{f}. Since both the likelihood and the GP prior are Gaussian, this integral can be evaluated analytically by completing the square, resulting in a closed-form expressionlog⁡p​(𝒚∣𝐱¯,𝜽)\displaystyle\log p({\bm{y}}\mid\underline{\mathrm{\bm{x}}},{\bm{\theta}})=−12​𝒚T​(K+σ2​I)−1​𝒚\displaystyle=-\frac{1}{2}\bm{y}^{\rm T}(K+\sigma^{2}I)^{-1}\bm{y}−12​log​det(K+σ2​I)\displaystyle\hphantom{=}\,\,-\frac{1}{2}\log\det(K+\sigma^{2}I)−N2​log⁡(2​π),\displaystyle\hphantom{=}\,\,-\frac{N}{2}\log(2\pi)\;,(74)

with𝜽=(σf2,ι)T\bm{\theta}=(\sigma^{2}_{f},\iota)^{\rm T}, where the covariance matrixKKis parameterized by𝜽\bm{\theta}. In addition to the kernel parameters, the likelihood varianceσ\sigmais, in principle, also a hyperparameter. As in PCE, the likelihood parameters may likewise be treated as unknown. In GPs, however,σ\sigmais often estimated from the data or introduced as a technical parameter to stabilize the numerical matrix inversion.
While we focus on zero-mean priors, the prior mean function can also be modeled explicitly, for example by a polynomial expansion such as the PCE introduced in Section4.2. An extension of GPs to non-zero prior means with linear coefficients is presented in Ranftl et al.Ranftl and von der Linden [2021]. In machine-learning practice, however, the prior mean is typically set to zero, since the covariance function alone often provides sufficient model flexibility. This property is formalized by therepresenter theorem, which we briefly discuss next.

Representer theorem. Simply put, the essence of the representer theorem is that the solution of a regularized learning problem in a reproducing kernel Hilbert space — such as the optimization problems underlying Eq. (32) or Eq. (4.3) — admits a representation of the formf∗​(𝒙)=∑n=1Nai​k​(𝒙,𝒙(n)),f^{*}(\bm{x})=\sum_{n=1}^{N}a_{i}k(\bm{x},\bm{x}^{(n)})\;,(75)

for some coefficients𝒂=(a1,…,aN)T∈ℝN\bm{a}=(a_{1},\dots,a_{N})^{\rm T}\in\mathbb{R}^{N}. Here,f∗f^{\ast}denotes the optimal solution of the learning problem within the reproducing kernel Hilbert space defined by the kernelkk.
In the GP framework, this representation arises directly from the structure of the posterior mean given in Eq. (73), where𝒌∗=(k​(𝒙∗,𝒙(1)),…,k​(𝒙∗,𝒙(N)))T\bm{k}_{*}=\big(k(\bm{x}_{*},\bm{x}^{(1)}),\dots,k(\bm{x}_{*},\bm{x}^{(N)})\big)^{\rm T}collects the kernel evaluated at the training
inputs, so the posterior mean is a weighted sum of these kernel values. In particular, the GP posterior mean has the form of Eq. (75) with𝒂=(K+σ2​I)−1​𝒚\bm{a}=(K+\sigma^{2}I)^{-1}\bm{y}. Thus, the coefficientsaia_{i}in Eq. (75) correspond exactly to the entries of𝒂\bm{a}obtained from the GP posterior.
Consequently, it is not strictly necessary to introduce additional surrogate parameters by modeling the prior mean as a separate linear expansion of basis functions, because the representer theorem shows that the posterior mean is already a linear combination of kernel evaluations. Put differently, the GP posterior mean (not the distribution though!) constitutes a generalized linear model of the form (31), where the basis functions are given by the kernel.

Nevertheless, in practice it can be advantageous to define a non-zero prior mean function — for example as a polynomialO’Hagan [1978]or a PCE (cf. Section4.2). Conversely, such models can also be interpreted as PCEs augmented with a GP prior to capture correlations that are not explained by the polynomial trendSchobi et al. [2015].

In contrast to PCEs, GPs offer two key advantages: (i) built-in UQ and (ii) explicit modeling of covariance between variables. The first advantage can be viewed as the probabilistic counterpart of deterministic kernel methods such as support vector machinesCortes and Vapnik [1995]and kernel ridge regressionVovk [2013], following directly from the predictive variance, the right-hand side of Eq. (73). The second is achieved through the choice of kernel, which encodes correlation structure.
Importantly, GP uncertainty remains tractable even for non-factorizable input distributions — a key advantage over PCE — though uncertainty propagation may require sampling or approximationsGirard [2004], Marrel et al. [2009], Wirthl et al. [2023]. Note that this uncertainty represents epistemic uncertainty in the surrogate itself, which is distinct from the propagated aleatoric uncertainty and is not explicitly quantified in PCE.

The major limitations of GPs are: (i) unlike PCE, they do not provide exact solutions for the (conditional) variance ofyyand require numerical integration (e.g., via Monte Carlo methods) and (ii) limited scalability to high-dimensional problems, despite partial remediesHensman et al. [2013], Liu et al. [2020], Binois and Wycoff [2022].
Limitation (ii) reflects the curse of dimensionality also encountered in PCE and arises from the necessity to invert the covariance matrix during both training and inference. However, computational trade-offs exist: representing a linear expansion as in PCE in terms of kernel functions, as discussed in the representer theorem, orvice versa, can yield computational savings depending on the relative sizes of the basis and the datasetHensman et al. [2013].
Lastly, GPs inherently assume that the target variable follows a Gaussian distribution. While this can be restrictive when modeling non-Gaussian outputs, it also provides analytical tractability for Gaussian targets, and enable closed-form posterior distributions.

Similar to PCEs, GPs are a standard surrogate model especially for Bayesian optimization (cf. Section6.2), and here too the GP hyperparameters are typically assumed to be deterministic for uncertainty propagation. Examples include coupled multi-physics models of fluid–structure interaction in biofilmsWillmann et al. [2022], sensitivity analyses of output variability in a growth and remodeling model of an aortic aneurysmBrandstaeter et al. [2021]or in other biomechanical problemsWirthl et al. [2023], and the quantification of output stress uncertainty under material behavior uncertainty in a nonlinear finite element model of reconstructive surgeryLee et al. [2018]. Others used constrained GP models for parameter calibration in a reduced lung modelDinkel et al. [2024]and to represent the solution field of a PDE, enabling physics- and data-informed inference with built-in uncertainty quantification via a finite-element discretization of the weak formDalton et al. [2026]. In addition, a comparison of GP and PCE surrogates was performed for hemodynamic pulse-wave propagation modelingPaun et al. [2025].
A Bayesian treatment of the hyperparameters, by contrast, is rare; one of the few examples is found in finite element simulations of impedance cardiography of aortic dissection with multi-fidelity dataRanftl et al. [2019].

## 4.4Machine learning II: Neural networks and physics-informed learning

## 4.4.1Neural networks

Similar to PCE and GP regression, we consider a forward mapf:𝒙↦yf:\bm{x}\mapsto y, that is,y=f​(𝒙)y=f(\bm{x}), which we aim to approximate by a surrogate model. In the case of NNs, this surrogate is given by a parametric mappingf^NN:𝒙↦y^,\hat{f}_{\rm NN}:\bm{x}\mapsto\hat{y}\;,(76)

that defines a learned mappingy^=f^NN​(𝒙;𝜽)\hat{y}=\hat{f}_{\rm NN}(\bm{x};\bm{\theta}).
Thus, NNs map an input𝒙∈ℝd0\bm{x}\in\mathbb{R}^{d_{0}}to an outputy∈ℝdLy\in\mathbb{R}^{d_{L}}, withd0≡Dd_{0}\equiv DanddL≡Qd_{L}\equiv Qas used previously. They achieve this through a sequence of layers, where each layer applies a linear transformation followed by a nonlinear activation. The nonlinear transformations are known asactivation functions. By composing many such transformations, NNs can represent highly complex input–output relationships.

A feedforward network withLLlayers is defined recursively. We initialize𝐳0:=𝒙,\mathbf{z}_{0}:=\bm{x}\;,(77)

and for each hidden layerℓ=1,…,L−1\ell=1,\ldots,L-1, we compute𝐳ℓ=σℓ​(Wℓ​𝐳ℓ−1+𝐛ℓ),\mathbf{z}_{\ell}=\sigma_{\ell}(W_{\ell}\mathbf{z}_{\ell-1}+\mathbf{b}_{\ell})\;,(78)

whereWℓ∈ℝdℓ×dℓ−1W_{\ell}\in\mathbb{R}^{d_{\ell}\times d_{\ell-1}}is the weight matrix of layerℓ\ell,𝐛ℓ∈ℝdℓ\mathbf{b}_{\ell}\in\mathbb{R}^{d_{\ell}}is the bias vector, andσℓ\sigma_{\ell}is an element-wise nonlinear activation function. Each intermediate variable𝐳ℓ\mathbf{z}_{\ell}represents the output of layerℓ\ell, obtained by applying a linear transformation followed by a nonlinear actitivation to the previous layer’s output𝐳ℓ−1\mathbf{z}_{\ell-1}. The surrogate is then the output of the final layer,f^NN​(𝒙;𝜽):=𝐳L.\hat{f}_{\rm NN}(\bm{x};\bm{\theta}):=\mathbf{z}_{L}\;.(79)

with the full parameter set𝜽=(Wℓ,𝐛ℓ)ℓ=1L\bm{\theta}=(W_{\ell},\mathbf{b}_{\ell})_{\ell=1}^{L}, and usuallyσL\sigma_{L}is the identity function.
Thus, the network output is obtained by repeatedly transforming the input through all layers. Training the network consists of finding𝜽\bm{\theta}such thatf^NN​(𝒙)\hat{f}_{\rm NN}(\bm{x})closely matches the forward modelf​(𝒙)f(\bm{x})over a set of training examples. This is achieved by minimizing a loss functionℒ\mathcal{L}, typically the mean-squared error,ℒ​(𝜽)=∑n=1N(y(n)−f^NN​(𝒙(n);𝜽))2,\displaystyle\mathcal{L}(\bm{\theta})=\sum_{n=1}^{N}\big(y^{(n)}-\hat{f}_{\rm NN}(\bm{x}^{(n)};\bm{\theta})\big)^{2}\;,(80)

which measures the discrepancy between the surrogate predictions and reference outputs, i.e., the squaredL2L_{2}-norm. Note that we again seek to find optimal parameters by solving Eq. (32). Minimizing this loss function is equivalent to MAP estimation with a flat prior and the likelihoodp​(𝒟∣𝜽,f)∝exp⁡(−ℒ​(𝜽)).p(\mathcal{D}\mid\bm{\theta},f)\propto\exp(-\mathcal{L(\bm{\theta})})\;.(81)

We observe that Eq. (79), in its vectorized form, shares the same structural form as Eq. (31), the general expression for the surrogate as an expansion. Specifically, the matrix multiplication[WL​𝒛L−1]i​j=∑k[WL]i​k​[𝒛L−1]k​j≡∑k[WL]i​k​[σL−1​(𝒙;𝜽)]k​j[W_{L}{\bm{z}}_{L-1}]_{ij}=\sum_{k}[W_{L}]_{ik}[{\bm{z}}_{L-1}]_{kj}\equiv\sum_{k}[W_{L}]_{ik}[\sigma_{L-1}({\bm{x}};{\bm{\theta}})]_{kj}reveals that the activated featuresσL−1\sigma_{L-1}play an analogous role to the basis functionsϕ\phifrom previous sections. In other words, NNs can be interpreted as generalizedlinearmodels with learnable basis functions.

In this view, the final weight matrixWLW_{L}plays the role of linear coefficients, while the nonlinear basis functions arise from the compositionsσℓ​(Wℓ​𝐳ℓ−1+𝐛ℓ)\sigma_{\ell}(W_{\ell}\mathbf{z}_{\ell-1}+\mathbf{b}_{\ell}). Unlike traditional expansions such as PCEs or GPs, these basis functions depend on trainable parameters, that greatly increase the expressive power of the model. In other words, this enables NNs to represent functions that lie beyond the expressive capacity of traditional linear models — including generalized linear models.

This interpretation of NNs as a linear model with complex, trainable basis functions has inspired variants such as theextreme learning machineHuang et al. [2006]andrandom features approachesRahimi and Recht [2007], where the nonlinear transformations are fixed or randomized and only the final linear layer is optimized. When the loss function is quadratic (e.g.,L2L_{2}-norm), the resulting optimization problem for the linear parameters is convex and sometimes even admits a closed-form solution. A particular advantage of NNs is that they are scalable to high-dimensional inputsTripathy and Bilionis [2018], Zhu and Zabaras [2018].

NNs, in contrast to both GPs and PCEs, scale very well to high input dimensions. They also exhibit greater capacity for handling nonlinearities and enable new opportunities such as operator learning, which are typically challenging for PCEs or GPs to capture. Strongly nonlinear or even discontinuous functions, in particular, are often difficult to model with PCEs or GPs and NNs offer modeling capabilities that extend significantly beyond those of PCEs or GPs.

However, NNs generally lack the built-in UQ that characterizes GPs and, unlike PCEs, they do not provide analytical expressions for propagated variances or sensitivities. While Bayesian NNs and ensemble-based methods have been proposed to approximate uncertaintyLakshminarayanan et al. [2017], Wilson and Izmailov [2020], these approaches come at the cost of substantial additional computational effort and often yield less interpretable results. As such, UQ in NNs and NNs designed for UQ remain an active area of research.

Another limitation is the strong dependence of NNs on architectural and hyperparameter choices, training procedures, and regularization strategies. The mathematical guidance available for designing NN architectures is still limited, often resulting in unstable or inconsistent performance across problems and necessitating extensive heuristic trial and error. Furthermore, NNs typically require much larger amounts of data compared to GPs or PCEs, which can be detrimental in applications such as biomechanics where data are often scarce. These data requirements can be partially mitigated through physics-informed learning or careful design choices, yet they remain an inherent characteristic of most NN–based approaches.

Lastly, NNs are often regarded as black-box models, in contrast to the more interpretable structure of PCEs or the kernel-based formulation of GPs.

## 4.4.2Physics-informed neural networks

While conventional NNs learn purely from data, physics-informed machine learning enriches the learning process by integrating prior physical knowledge directly into a surrogate modelKarniadakis et al. [2021]. In computational mechanics, such prior knowledge often appears in the form of a PDE together with associated boundary and initial conditions.

LetΩ0⊂ℝD\Omega_{0}\subset\mathbb{R}^{D}denote the spatial domain representing the reference (undeformed) configuration with boundary∂Ω0\partial\Omega_{0}, where𝐗∈Ω0\mathbf{X}\in\Omega_{0}is a material point, and letT>0T>0be the final time. The forward model is governed by the PDEℱ​[u​(𝐗,t)]=q​(𝐗,t),(𝐗,t)∈Ω0×(0,T],\displaystyle\mathcal{F}[u(\mathbf{X},t)]=q(\mathbf{X},t)\;,\quad(\mathbf{X},t)\in\Omega_{0}\times(0,T]\;,(82)

whereℱ​[⋅]\mathcal{F}[\cdot]is a (possibly nonlinear) differential operator encoding the governing physics,u​(𝐗,t)u(\mathbf{X},t)is the solution field, andq​(𝐗,t)q(\mathbf{X},t)is the prescribed forcing or source term on the right-hand side of the PDE.
A simple example is the Laplacian operator,ℱ≡∇2\mathcal{F}\equiv\nabla^{2}.
Depending on the application,q​(𝐗,t)q(\mathbf{X},t)may represent body forces, distributed loads, heat generation, reaction terms, or other volumetric inputs to the system.

This PDE is supplemented by the initial and boundary conditionsu​(𝐗,0)\displaystyle u(\mathbf{X},0)=uIC​(𝐗),\displaystyle=u_{\rm IC}(\mathbf{X})\;,𝐗∈Ω0,\displaystyle\mathbf{X}\in\Omega_{0}\;,(83)u​(𝐗,t)\displaystyle u(\mathbf{X},t)=uBC​(𝐗,t),\displaystyle=u_{\rm BC}(\mathbf{X},t)\;,(𝐗,t)∈∂Ω0×(0,T],\displaystyle(\mathbf{X},t)\in\partial\Omega_{0}\times(0,T]\;,(84)

whereuurepresents the physical state (e.g., displacement or velocity). Beyond these equations, other forms of prior knowledge can also be incorporated into a learning model, such as conservation laws, symmetry or invariance properties (e.g., incompressibility), canonical variables, or empirical relations. For simplicity, we focus here on the case where the prior knowledge is represented by the PDE system (82) to (84).

A physics-informed NN (PINN) aims to learn a surrogate functionu^:Ω0×(0,T]→Y⊆ℝQ,(𝐗,t)↦u^(𝐗,t;𝜽),\hat{u}:\Omega_{0}\times(0,T]\to Y\subseteq\mathbb{R}^{Q}\;,\quad(\mathbf{X},t)\mapsto\hat{u}(\mathbf{X},t;{\bm{\theta}})\;,(85)

forQQ-dimensional spatiotemporal fields, where𝜽\bm{\theta}denotes the trainable parameters. The surrogateu^​(𝐗,t;θ)\hat{u}(\mathbf{X},t;\mathbf{\theta})approximates the true solutionu​(𝐗,t)u(\mathbf{X},t)of the forward model (Eq. (82)). The key distinction is that the NN is trained to directly satisfy the PDE constraintℱ​[u^​(𝐗,t;θ)]=q​(𝐗,t)\mathcal{F}[\hat{u}(\mathbf{X},t;\mathbf{\theta})]=q(\mathbf{X},t)at collocation points, rather than solely relying on input-output data pairs. Note that what was denoted asyypreviously is denoted asuuhere to align with standard notation in the PDE literature.

The key idea of PINNs is to trainu^\hat{u}not only to match available data but also to satisfy the PDE, boundary conditions, and initial condition. This is achieved by minimizing the composite loss functionℒ​(𝜽)\mathcal{L}(\bm{\theta})with hyperparameters𝜽\bm{\theta}that penalizes discrepancies between the surrogate solutionu^\hat{u}and the physical constraintsℒ​(𝜽)\displaystyle\mathcal{L}(\bm{\theta})=ℒdata+λPDE​ℒPDE\displaystyle=\mathcal{L}_{\rm data}+\lambda_{\rm PDE}\,\mathcal{L}_{\rm PDE}+λBC​ℒBC+λIC​ℒIC,\displaystyle\hphantom{=}\,\,+\lambda_{\rm BC}\,\mathcal{L}_{\rm BC}+\lambda_{\rm IC}\,\mathcal{L}_{\rm IC}\;,(86)

where theλ(⋅)\lambda_{(\cdot)}’s are tunable weighting parameters, and each term enforces a different constraint: (i) agreement with available data, (ii) residual of the PDE, (iii) boundary conditions, and (iv) the initial condition.
Explicitly,ℒ​(θ)=1Ndata​∑i=1Ndata|u^​(𝐗(i),t(i))−u(i)|2+λPDENPDE​∑j=1NPDE|ℱ​[u^​(𝐗(j),t(j))]−q​(𝐗(j),t(j))|2+λBCNBC​∑m=1NBC|u^​(𝐗(m),t(m))−uBC​(𝐗(m),t(m))|2+λICNIC∑n=1NIC|u^(𝐗(n),0)−uIC(𝐗(n)).|2,\displaystyle\begin{split}\mathcal{L}(\theta)&=\frac{1}{N_{\text{data}}}\sum_{i=1}^{N_{\text{data}}}\left|\hat{u}(\mathbf{X}^{(i)},t^{(i)})-u^{(i)}\right|^{2}\\
&\hphantom{=}\,\,+\frac{\lambda_{\text{PDE}}}{N_{\text{PDE}}}\sum_{j=1}^{N_{\text{PDE}}}\left|\mathcal{F}[\hat{u}(\mathbf{X}^{(j)},t^{(j)})]-q(\mathbf{X}^{(j)},t^{(j)})\right|^{2}\\
&\hphantom{=}\,\,+\frac{\lambda_{\text{BC}}}{N_{\text{BC}}}\sum_{m=1}^{N_{\text{BC}}}\left|\hat{u}(\mathbf{X}^{(m)},t^{(m)})-u_{\rm BC}(\mathbf{X}^{(m)},t^{(m)})\right|^{2}\\
&\hphantom{=}\,\,+\frac{\lambda_{\text{IC}}}{N_{\text{IC}}}\sum_{n=1}^{N_{\text{IC}}}\left|\hat{u}(\mathbf{X}^{(n)},0)-u_{\rm IC}(\mathbf{X}^{(n)}).\right|^{2}\;,\end{split}(87)

where the collocation pointsNPDEN_{\rm PDE},NBCN_{\rm BC},NICN_{\rm IC}and data pointsNdataN_{\rm data}, aresampledwithin the domain, on the boundary, and on the initial surface. Taking a NN for an ansatz foru^\hat{u}and minimizingℒ​(𝜽)\mathcal{L}(\bm{\theta})yields a surrogate whose predictions supposedly both match data and approximately satisfy the underlying physics. The most important point of PINNs is that the physics-related loss-terms in Eq. (4.4.2) effectively act as a regularizer that significantly reduces the amount of data,NdataN_{\rm data}, necessary for convergence. This approach can be taken to the extreme by training anunsupervisedPINN that omits the data-loss term in Eq. (4.4.2) entirely and relies purely on the physical equationsZhu et al. [2019].

While PINNs enforce physics pointwise at collocation points, the residuals may remain large in regions that are insufficiently sampled. Moreover, training is often sensitive to the weighting parametersλPDE\lambda_{\rm PDE},λBC\lambda_{\rm BC}, andλIC\lambda_{\rm IC}, which has motivated various adaptive weighting strategiesWang et al. [2021,2022], Basir and Senocak [2022], Wang et al. [2023].

Finally, the notion ofphysics-informed learninghere hinges on the loss function (Eq. (4.4.2)), not on the functional form ofu^\hat{u}. That is, the representationu^\hat{u}need not be a NN. Other surrogate families — such as PCEsNovák et al. [2024], kernel methods, or GPs — can also be made physics-informed by interpreting the PDE residuals and boundary and initial conditions as contributions to the likelihood or priorRaissi et al. [2017], Raissi and Karniadakis [2018], Cross et al. [2024].

## 4.4.3Neural operators

Neural operators (NOs) extend surrogate modeling beyond learning pointwise mappings. While standard NNs learn functionsf^:𝒙↦y^\hat{f}:\bm{x}\mapsto\hat{y}and PINNs learn mappings𝐗→u^\mathbf{X}\to\hat{u}, NOs learnoperators— that is, mappings between infinite-dimensional function spaces. Rather than mapping points to points, NOs map entireinput functionstooutput functions.

Formally, the true operator is denoted byℱNO:u↦v\mathcal{F}_{\rm NO}:u\mapsto v, whereuuis an input function, e.g., boundary conditions, forcing terms, or material coefficients, andvvis the corresponding output function, e.g., a PDE solution field. A neural operator then serves as a surrogateℱ^NO:u↦v^,\hat{\mathcal{F}}_{\rm NO}:u\mapsto\hat{v}\;,(88)

approximating the input–output relationship encoded byℱNO\mathcal{F}_{\rm NO}.

The most widely used neural-operator architecture is the deep operator network (DeepONet)Lu et al. [2021]. Note that while our notation here implies that𝐗\mathbf{X}is a spatial coordinate like in Section4.4.2, and often indeed it is, however it can also be a stochastic parameter𝒙{\bm{x}}.

A DeepONet consists of two subnetworks that work together to represent the operator:
- •

Branch network. The branch network encodes the input functionuu. The function is sampled at a fixed set of sensor points and passed through the branch network, which outputs a latent feature vectorb​(u)∈ℝLb(u)\in\mathbb{R}^{L}.
- •

Trunk network. In contrast, the trunk network encodes the evaluation location𝐗\mathbf{X}. For each spatial (or spatio-temporal) coordinate, the trunk network outputs a latent feature vectort​(𝐗)∈ℝLt(\mathbf{X})\in\mathbb{R}^{L}.

The surrogate operator prediction at a location𝐗\mathbf{X}is then given byv^​(𝐗;𝜽)=ℱ^NO​(u)​(𝐗)=b​(u)T​t​(𝐗),\hat{v}(\mathbf{X};{\bm{\theta}})=\hat{\mathcal{F}}_{\rm NO}(u)(\mathbf{X})=b(u)^{\rm T}t(\mathbf{X})\;,(89)

where the trainable parameters of both subnetworks are collected in𝜽\bm{\theta}, andLLis the dimension of the latent feature space. Intuitively, the branch network thus captures how the input function influences the output, while the trunk network modulates this dependence at each evaluation point𝐗\mathbf{X}. In relation to the generalized model Eq. (30) or NNs (Section4.4.1) before, the elements oft​(𝐗)t(\mathbf{X})can also be considered learnable basis functions with coefficientsb​(u)b(u).

Given a dataset of input–output function pairs(u(i),v(i))i=1Nu(u^{(i)},v^{(i)})_{i=1}^{N_{u}}, each sampled at evaluation points(𝐗(j))j=1Nx(\mathbf{X}^{(j)})_{j=1}^{N_{x}}, the surrogate operatorℱ^NO\hat{\mathcal{F}}_{\rm NO}is trained by minimizing the data misfitℒdata​(𝜽)=1Nu​Nx​∑i=1Nu∑j=1Nx|ℱ^NO​(u(i))​(𝐱j)−v(i)​(𝐱j)|2.\mathcal{L}_{\text{data}}(\bm{\theta})=\frac{1}{N_{u}N_{x}}\sum_{i=1}^{N_{u}}\sum_{j=1}^{N_{x}}\big|\hat{\mathcal{F}}_{\rm NO}(u^{(i)})(\mathbf{x}_{j})-v^{(i)}(\mathbf{x}_{j})\big|^{2}\;.(90)

Here,NuN_{u}is the number of distinct input functions,NxN_{x}denotes the number of evaluation (sensor) points per function, andv(i)​(xj)v^{(i)}(x_{j})denotes the true output function corresponding tou(i)u^{(i)}at locationxj\mathrm{x}_{j}.

In computational physics and biomechanics, the input functionuumay represent a boundary displacement, a spatially varying material parameter, a forcing profile, or any other function that parametrizes the governing PDE. The trained NOℱ^NO\hat{\mathcal{F}}_{\rm NO}can then predict the corresponding solution functionv^​(𝐱;𝜽∗)\hat{v}(\mathbf{x};{\bm{\theta}}^{\ast})approximately, e.g., instead of a PDE solver.

NOs can also be trained in a physics-informed manner analogous to PINNsWang et al. [2021], where additional loss terms enforce PDE residuals, boundary conditions, or conservation laws. However, because these constraints must be evaluated across many input functions and spatial points, the associated computational cost can be significantly higher. Efficient training schemes including separable architectures, low-rank factorizations, and adaptive collocation strategies are active research topicsYu et al. [2024], Mandl et al. [2025].

Examples of NO as a surrogate in biomechanics are diverse. They map the aortic wall microstructure to pressure-volume curves and damage progression during aortic dissection progressionYin et al. [2022], infer patient-specific mechanobiological insult profiles driving aneurysm formation from clinical maps of aortic dilatation and distensibilityGoswami et al. [2022], reconstruct full-field brain displacement fields from multimodal magnetic resonance elastography dataAgarwal et al. [2025], relate aortic flow-rate waveforms and heart rate to the corresponding pressure waveformHong et al. [2024], and denoise displacement fields in ultrasound elastographyZhu and Peng [2024]. In material modeling, NO surrogate were used to link crack configuration and loading steps to global displacement and damage fieldsGoswami et al. [2022], experimental load-displacement field measurements to a nonlocal constitutive law together with the fiber-orientation field and full-field stress predictionsJafarzadeh et al. [2025], and loading protocols to the resulting displacement fieldYou et al. [2022]. Further examples and perspectives are given inAhmadi et al. [2026], Mandl et al. [2026].

## 4.5Alternative surrogate modeling strategies

While PCEs, GPs, and PINNs represent some of the most widely used surrogate modeling techniques today, the broader literature on surrogate modeling, particularly within UQ and machine learning, is considerably more diverse. In the following sections, we will briefly introduce several additional approaches that have gained attention in recent years and discuss their respective advantages, challenges, and areas of application.

## 4.5.1Tree-based regressors and bootstrapping

Yet another important class of machine learning models applicable to regression tasks are tree-based and bootstrapping methods, including decision treesBreiman et al. [2017], random forestsBreiman [2001], and gradient boostingFriedman [2002]. These approaches aim to learn (ensembles of) nonlinear mappingsf^Tree(j):𝒙↦y^,\hat{f}_{\rm Tree}^{(j)}\colon\bm{x}\mapsto\hat{y}\;,(91)

that approximate the relationship between an input vector𝒙∈ℝD𝒙\bm{x}\in\mathbb{R}^{D_{\bm{x}}}and a scalar or vector-valued responsey∈ℝDyy\in\mathbb{R}^{D_{y}}.
Regression trees iteratively partition the input space into regions and fit simple predictive rules locally. A random forest then is an entire (random) ensemble of such treesj=1,⋯,Jj=1,\cdots,J.
The sample functions, sometimes calledweak learners, or rather the predictions thereof, are then aggregated into a single prediction — such as a mean — through different bootstrapping methodsEfron [1992], typically bagging or boosting. The latter may be guided by the gradients of the weak learners, hence the namegradient boosting.

Although these approaches have been extensively developed and analyzed within the machine learning community, and efficient open-source implementations such as XGBoostChen and Guestrin [2016]and CatBoostProkhorenkova et al. [2019]are readily available, their use for surrogate modeling and UQ in computational science remains comparatively limited, with few examples in (bio)mechanicsBraito et al. [2026].

These models can handle nonlinear, non-smooth, and even discontinuous system responses effectively; situations where smooth-function approximators such as GPs or PCEs struggle. Conversely, tree-based models often lack the smoothness desiderata of a given physical system. Moreover, ensemble methods naturally provide measures of predictive uncertainty per the nature of bootstrapping, which can be exploited for uncertainty estimation in surrogate modeling. To maintain focus, we refer the reader to a more detailed discussion of tree-based ensemble methods[Braito et al.,2026, Secs. 2.2.2 and 2.2.3].

## 4.5.2Reduced-order modeling

So far, we have primarily discussed data-driven surrogate models, which learn mappings from input to output while treating the underlying physical system as a black box.
An exception to this paradigm are the physics-informed learning approaches introduced in Section4.4, where physical constraints are explicitly incorporated into the learning process.

In contrast, we have not yet discussedreduced-order modeling(ROM) and intrusive UQ, methods that require reformulation of the governing equationsGhanem et al. [2017]. These approaches tackle the problem from the side of physics-based model reduction rather than purely data-driven approximation.
Similar to surrogate models, ROMs aim to reduce the computational complexity, dimensionality or number of degrees of freedom of the governing equations in Eq. (19) to obtain computationally efficient approximations of the true solution. Traditionally, ROMs are derived by projecting the governing equations onto a reduced basis, thereby retaining the essential physical structure of the system while substantially decreasing computational costKerschen et al. [2005], Lassila et al. [2014], Rathore et al. [2025].

More recently, data-driven ROMs have emerged by combining projection-based model reduction with machine learning techniquesKutz et al. [2016]. Such approaches have gained increasing relevance in biomechanicsChinesta et al. [2023], Siena et al. [2023], Balzotti et al. [2024], where high-fidelity simulations of complex dynamical systems are computationally demanding.
As a result, the boundary betweenphysics-informed surrogatesanddata-driven ROMshas become increasingly blurred, often depending on the degree to which physical modeling and data-driven inference are fused. We have already touched upon these hybrid approaches in Section4.4; however, a comprehensive overview would warrant its own treatment and therefore lies beyond the scope of this review article. For readers interested in UQ from the ROM perspective, we refer to the excellent literature inChen et al. [2015], Chinesta et al. [2023].

## 4.5.3Multi-fidelity modelingFigure 6:Schematic overview of multi-fidelity modeling using physical and numerical models of varying fidelity: (a) patient-specific finite element models of aortic dissection (patient model based onBäumler et al. [2025]; no permission needed) with increasing spatial resolution, ranging from coarse to fine meshes; (b) hemodynamic models of increasing dimensionality, progressing from 0D (lumped-parameter) to 1D and fully resolved 3D representations (modified fromFleeter et al. [2020]; with permission from Elsevier); and (c) constitutive models spanning from linear to nonlinear material behavior.

Multi-fidelity (MF) models combine simulations or data sources of varying accuracy and cost. The idea is to fuse high-fidelity (HF) data, which are accurate but expensive, with low-fidelity (LF) data, which are cheaper but less accurate. To place these ideas in context, we briefly sketch MF modeling here; see, e.g.,Schäfer et al. [2026]for a dedicated introduction, implementation aspects, and applications.

An illustrative example is a HF model of a boundary-value problem with a fine spatial discretization or higher-order finite elements, while the LF model could be the same boundary-value problem solved on a coarser mesh or using lower-order elementsBiehler et al. [2015], Ranftl et al. [2019], see Fig.6. Similarly, in fluid mechanics, the full three-dimensional Navier–Stokes equations may serve as the HF model, whereas corresponding LF representations could be based on the Reynolds-averaged Navier–Stokes equations, one-dimensional flow models, or even zero-dimensional lumped-parameter networksTran et al. [2017], Fleeter et al. [2020].

For vector-valued inputs and outputs, we denote the HF and LF forward models asyHF=fHF​(𝒙),yLF=fLF​(𝒙).\displaystyle y_{\rm HF}=f_{\rm HF}(\bm{x})\;,\quad y_{\rm LF}=f_{\rm LF}(\bm{x})\;.(92)

Rather than directly learning the expensive relationf^HF:𝒙↦yHF​(𝒙),\hat{f}_{\rm HF}:\bm{x}\mapsto y_{\rm HF}(\bm{x}),(93)

a MF surrogate decomposes this mapping into two stagesf^MF:𝒙↦yLF↦y^HF,\hat{f}_{\rm MF}:\bm{x}\mapsto y_{\rm LF}\mapsto\hat{y}_{\rm HF}\;,(94)

whereyLF​(𝒙)y_{\rm LF}(\bm{x})serves as an intermediate representation. The first stage provides a cheap approximation, and the second stage learns a corrective relationship fromyLF​(x)y_{\rm LF}(x)toy^HF​(𝒙)\hat{y}_{\rm HF}(\bm{x}). Thus, the composed surrogate still maps𝒙\bm{x}toy^HF​(𝒙)\hat{y}_{\rm HF}(\bm{x}), but does so more efficiently by leveraging the intermediate LF prediction.

In the Bayesian frameworkKennedy and O’Hagan [2000], the relationship between HF and LF models can be expressed through a parameterized functionyHF=f^MF​(yLF​(𝒙);𝜽),\displaystyle y_{\rm HF}=\hat{f}_{\rm MF}\big(y_{\rm LF}(\bm{x});\bm{\theta}\big)\;,(95)

wheref^MF\hat{f}_{\rm MF}denotes the MF surrogate as a function of the LF prediction, and𝜽\bm{\theta}represents model parameters.

Alternatively, one may directly model the cross-covariancecov​[yHF​(𝒙),yLF​(𝒙)∣𝜽],\displaystyle\mathrm{cov}\big[y_{\rm HF}(\bm{x}),y_{\rm LF}(\bm{x})\mid\bm{\theta}\big]\;,(96)

to directly infer the correlation structure from data. A particularly common choice is the additive modelyHF​(𝒙)≈ρLF⋅yLF​(𝒙)+δMF​(𝒙),\displaystyle y_{\rm HF}(\bm{x})\approx\rho_{\rm LF}\cdot y_{\rm LF}(\bm{x})+\delta_{\rm MF}(\bm{x})\;,(97)

whereρLF\rho_{\rm LF}is a (learnable) correlation parameter whileδMF​(𝒙)\delta_{\rm MF}(\bm{x})is the discrepancy between HF and LF. A popular Bayesian construction assumes GP priorsyLF​(𝒙)\displaystyle y_{\rm LF}(\bm{x})∼GP​(0,kLF​(𝒙,𝒙′;𝜽LF)),\displaystyle\sim\mathrm{GP}\big(0,k_{\rm LF}(\bm{x},\bm{x}^{\prime};\bm{\theta}_{\rm LF})\big)\;,(98)δMF​(𝒙)\displaystyle\quad\delta_{\rm MF}(\bm{x})∼GP​(0,kMF​(𝒙,𝒙′;𝜽MF)),\displaystyle\sim\mathrm{GP}(0,k_{\rm MF}\big(\bm{x},\bm{x}^{\prime};\bm{\theta}_{\rm MF})\big)\;,(99)

wherekLFk_{\rm LF}andkMFk_{\rm MF}are the covariance functions associated with the LF model and the discrepancy between the low- and high-fidelity models, while𝜽LF\bm{\theta}_{\rm LF}and𝜽MF\bm{\theta}_{\rm MF}are the hyperparameters of the kernels, respectively. Under this construction,yHFy_{\rm HF}is itself a GP, enabling semi-analytic posterior expressionsRanftl et al. [2019].

This formulation can be viewed as an extension of the general UQ framework (cf. Eq. (14)), where the HF model outputyHFy_{\rm HF}is substituted by the MF surrogate defined in Eqs. (95) to (97).
Consequently, the additional parameters{ρLF,𝜽LF,𝜽MF}\{\rho_{\rm LF},\bm{\theta}_{\rm LF},\bm{\theta}_{\rm MF}\}enter the inference process in Eq. (14). We marginalize over them in a fully Bayesian treatment by extending the corresponding integration.

In the literature, numerous examples demonstrate the use of multi-fidelity modeling in biomechanics to accelerate computational time, particularly for UQ. Biehler et al.Biehler et al. [2015]applied this strategy to a patient-specific abdominal aortic aneurysm model by correcting the low-fidelity structural solution with a probabilistic discrepancy term inferred from a few high-fidelity simulations based on finer finite element meshes.
Similarly, Ranftl et al.Ranftl et al. [2019]quantified uncertainty in impedance cardiography for aortic dissection using multi-resolution finite element models combined with a normal GP surrogate.
In the context of soft tissue growth and remodeling, Lee et al.Lee et al. [2020]propagated uncertainty in mechanical and biological parameters through a multi-fidelity GP surrogate trained on finite element models of tissue expansion with varying mesh refinement, enabling spatio-temporal UQ at a fraction of the high-fidelity cost.
In the vascular domain, several works compare multilevel multi-fidelity estimators across hierarchical zero-, one-, and three-dimensional hemodynamic modelsFleeter et al. [2020]or link zero-dimensional Windkessel models to patient-specific three-dimensional vascular geometries by treating model discrepancy as random noiseChoi et al. [2025], whereas in cardiac modeling, parameter-mapping strategies have been proposed to enable fast zero-dimensional approximations of high-fidelity three-dimensional simulationsMolléro et al. [2018].
For flow and coupled fluid–structure interaction problems, Nitzler et al.Nitzler et al. [2022]proposed a Bayesian multi-fidelity UQ framework that learns a nonlinear output-to-output dependency between fidelity levels via a GP, augmented by informative input features to improve accuracy in the small-data regime.
Rounding out this overview, Nitzler et al.Nitzler et al. [2026a,b]addressed high-dimensional spatial Bayesian inversion by inferring spatially varying permeability fields in poro-elastic media, combining a cheap single-physics porous flow model as low-fidelity surrogate with a Gaussian Markov random field prior and stochastic variational inference to approximate the expensive coupled high-fidelity posterior.

## 4.6Qualitative comparison of surrogate models

Each model class (type) of surrogate models presented in Section4has quantitative measures for selecting models within that class. However, choosing a particular model class in the first place requires a careful analysis of the requirements and goals of the problem, as well as the advantages and limitations of the different model classes in question, as previously discussed.

In summary, GPs and PCEs are well-established and well-understood surrogate modeling techniques for UQ, although several limitations and unresolved advanced problems remain. In contrast, NNs promise to overcome some of these limitations but are generally far less well understood and face a different set of challenges. Indeed, NNs pose a broader and potentially more impactful range of open questions regarding both methodology and fundamental theory.
The best advise is to select the surrogate model that best fits the requirements and characteristics of their specific problem. For an overview, a simplified tabular comparison of the main aspects of GPs, PCEs, and NNs in the context of surrogate modeling for UQ, presented in Table2.Table 2:Qualitative comparison of Gaussian processes (GPs), polynomial chaos expansions (PCEs), and neural networks (NNs) for surrogate modeling in uncertainty quantification (high,medium, andlow).AspectGPPCENNNonlinearity representationHighMediumHighHandling of discontinuitiesLowMediumHighComputational scalabilityLowMediumHighData efficiencyHighMediumLowUncertainty quantificationHighMediumMediumInterpretabilityMediumHighLow

## 4.7Heuristic accuracy metrics and selection criteria

The performance and accuracy of surrogate models are commonly assessed using a combination of heuristic pointwise error metrics, such as the mean squared error (MSE) and the root-mean-squared error (RMSE). Therein, one has to distinguish between metrics computed over the training dataset and those evaluated on a test or validation dataset. In particular, predictive accuracy is typically quantified via sample-based error norms computed over a validation set𝒟val=(𝒙(n),y(n))n=1Nval\mathcal{D}_{\mathrm{val}}=(\bm{x}^{(n)},y^{(n)})_{n=1}^{N_{\mathrm{val}}}.

Collecting the data into a vector𝒚=(y(1),⋯,y(N))T\bm{y}=(y^{(1)},\cdots,y^{(N)})^{\mathrm{T}}and the corresponding predictions of the surrogate at the input points for a given set of optimal hyperparameters,𝜽∗\bm{\theta}^{\ast}, into a vector𝒚^=f^​(𝒙¯;𝜽∗)≔(f^​(𝒙(1);𝜽∗),⋯,f^​(𝒙(N);𝜽∗))T\hat{\bm{y}}=\hat{f}(\underline{{\bm{x}}};{\bm{\theta}}^{\ast})\>\coloneqq\>\big(\hat{f}({\bm{x}}^{(1)};{\bm{\theta}}^{\ast}),\cdots,\hat{f}({\bm{x}}^{(N)};{\bm{\theta}}^{\ast})\big)^{\mathrm{T}}, we can define commonly used error metrics asMSE\displaystyle\mathrm{MSE}=1Nval​∑n=1Nval(y(n)−f^​(𝒙(n);𝜽∗))2,\displaystyle=\frac{1}{N_{\mathrm{val}}}\sum_{n=1}^{N_{\mathrm{val}}}\left(y^{(n)}-\hat{f}(\bm{x}^{(n)};{\bm{\theta}}^{\ast})\right)^{2}\,,(100)RMSE\displaystyle\qquad\mathrm{RMSE}=MSE,\displaystyle=\sqrt{\mathrm{MSE}}\;,(101)ϵrel=L2‖𝒚‖2=‖𝒚−𝒚^‖2‖𝒚‖2=1‖𝒚‖2​(∑n=1Nval(y(n)−f^​(𝒙(n);𝜽∗))2)1/2,\displaystyle\begin{split}\epsilon_{\mathrm{rel}}&=\frac{L_{2}}{\left\|\bm{y}\right\|_{2}}=\frac{\left\|\bm{y}-\hat{\bm{y}}\right\|_{2}}{\left\|\bm{y}\right\|_{2}}\\
&=\frac{1}{\left\|\bm{y}\right\|_{2}}\left(\sum_{n=1}^{N_{\mathrm{val}}}\left(y^{(n)}-\hat{f}(\bm{x}^{(n)};{\bm{\theta}}^{\ast})\right)^{2}\right)^{1/2}\;,\end{split}(102)

In fact, the test set is typically drawn from the same data distribution as the training set, but it contains different data points. The difference between training error and test error is called thegeneralization gap. It measures how well a model performs on unseen data and helps detect overfitting or model misspecification. In contrast,out-of-distributionevaluation measures performance on test data that doesnotoriginate from the same distribution as the training data.
The error metrics in Eq. (100) are sample-based discrete approximations of an expectation, i.e., an integral over the input space. Therefore, the error estimates are themselves random variables, and their accuracy depends on the number and selection of samples.

To obtain reliable error estimates, datasets are oftenrandomlysplit into training and test sets, according to somesplit ratio. However, in surrogate modeling data are typically scarce. For example, withN=40N=40samples, a 90/10 split leaves only 4 data points for testing — too few for meaningful error estimation. A 10/90 split improves testing but leaves too little data for training. Alternatively, a 50/50 split may mitigate either issue whilst leaving both insufficient, hence we face a challenging situation.

Resampling methods such asτ\tau-foldcross-validationaddress this problem by splitting the dataset intoτ\taudisjoint subsets. The model is trained onτ−1\tau-1subsets and tested on the remaining one. This is repeatedτ\tautimes so that each subset serves once as the test set, and the final error is the average over allτ\tauruns.
A special case isleave-one-out cross-validation, short LOOCV, whereτ=N\tau=N, i.e., the number of folds equals the total number of samples. In this setting, the model is trained onN−1N-1samples and tested on the single remaining sample, and this is repeated once for every data point. This is the standard error measure in PCE modeling. In contrast, NNs are often evaluated using anL2L_{2}error with a simple train–test split, since they typically require large datasets where additional resampling is less critical.

For probabilistic surrogates, a common metric is thenegative log predictive density(NLPD),NLPD=−1Nval​∑n=1Nvallog⁡p​(y(n)∣𝒙(n),𝒟),\displaystyle\mathrm{NLPD}=-\frac{1}{N_{\mathrm{val}}}\sum_{n=1}^{N_{\mathrm{val}}}\log p\left(y^{(n)}\mid\bm{x}^{(n)},\mathcal{D}\right)\;,(103)

which measures how well the predicted probability distribution explains the observed test data. For GPs, it is the standard test metric and corresponds to the average negative log marginal likelihood (Eq. (4.3)) evaluated on the test set.

Probabilistic surrogates also provide predictive uncertainty, for example through credible intervals. A simple consistency check is to compare the expected probability mass of an uncertainty band with the observed frequency in the test data.
For instance, under a Gaussian prediction, about 68% of the data should lie within one standard deviation of the mean, i.e.,Pr⁡(|y(n)−μ​(𝒙(n))|<σ)≈0.68\Pr\left(\lvert y^{(n)}-\mu({\bm{x}}^{(n)})\rvert<\sigma\right)\approx 0.68. Deviations from this indicate miscalibrated uncertainty.

Evaluation metrics are mainly used to assess a trained model’ performance, but they are often also used for heuristic model selection — for example, choosing the model with the lowest MSE.
However, surrogate modeling for UQ is more subtle than standard machine learning. In typical machine learning benchmarks, large datasets are available and predictive error on held-out data is the main criterion. In UQ, what matters most is accuracy in regions with highprobability mass.141414For example, consider a priorp​(𝒙)p({\bm{x}})with two sub-regions𝒳1,𝒳2⊂𝒳\mathcal{X}_{1},\mathcal{X}_{2}\subset\mathcal{X}of similar size, i.e.,∫𝒳1d𝒙≈∫𝒳2d𝒙\int_{\mathcal{X}_{1}}\mathrm{d}{\bm{x}}\approx\int_{\mathcal{X}_{2}}\mathrm{d}{\bm{x}}.
Suppose,𝒳1\mathcal{X}_{1}carries only about10−610^{-6}of the total probability mass, while𝒳2\mathcal{X}_{2}carries about10−110^{-1}.
Then, an accurate surrogate in𝒳2\mathcal{X}_{2}is far more important than in𝒳1\mathcal{X}_{1}, because UQ typically involves integrals of the form∫𝒳(y​(𝒙))ϱ​p​(𝒙)​d𝒙\int_{\mathcal{X}}\big(y({\bm{x}})\big)^{\varrho}p({\bm{x}})\mathrm{d}{\bm{x}}, whereϱ\varrhois a parameter that specifies the moment of interest (e.g.,ϱ=1\varrho=1for the mean,ϱ=2\varrho=2for the second moment). Regions with negligible probability mass contribute very little to such integrals, unlessy​(𝒙)y({\bm{x}})grows so large in those regions that it compensates for the small probability.
The same reasoning applies to sensitivity analysis, inverse problems, and related tasks.

These heuristic metrics ignore the prior and are therefore not fully suitable for performance evaluation or model selection. While surrogate accuracy in UQ was discussed in Section3.3.2, the following Section5addresses principled model selection from a Bayesian perspective.

## 4.8Example: Surrogate-based uncertainty propagation of arterial properties in a pressurized symmetric cylinder

As a second example, we aim to propagate uncertainties of a material parameter through a computational model, our forward modelff. In particular, we consider a finite element simulation of an arterial segment with initial inner radiusRinR_{\rm in}and outer radiusRoutR_{\rm out}, subjected to a constant physiological inner pressurePin=100P_{\rm in}=100mmHg. Technically,PinP_{\rm in}is a control parameter; it is held fixed and therefore suppressed in the following. For the sake of argument, the arterial wall mechanics are described by linear elasticity under an incompressibility constraint, with Young’s modulusEEas the uncertain parameter, i.e.,𝒙=E\bm{x}=E. As output, we consider the deformed outer radiusroutr_{\rm out}, i.e.,y=routy=r_{\rm out}. The input-output relationship can be written asrout=y=f​(E).r_{\rm out}=y=f(E)\;.(104)

We assume that simulation data are available in the form𝒟=(E(n),y(n))n=1N,\mathcal{D}=\big(E^{(n)},y^{(n)}\big)_{n=1}^{N}\;,(105)

wherey(n)=f​(E(n))y^{(n)}=f(E^{(n)})denotes the simulated outer radius at a given Young’s modulusE(n)E^{(n)}, for a total ofNNdata pairs.

We assume that a previous Bayesian inverse problem based on experimental mechanical tests, such as the one shown in Section3.4, has provided us with a log-normal prior for the Young’s modulus with parametersμln⁡E=4.0\mu_{\ln E}=4.0(corresponding to approximately54.654.6kPa) andσln⁡E=0.3\sigma_{\ln E}=0.3. This choice ensures physical consistency by strictly enforcingE>0E>0.

To avoid the high computational cost of repeatedly evaluating the forward model, we construct a PCE as a surrogate for the finite element simulation. BecauseEEis log-normally distributed,Hermite polynomialsϕp\phi_{p}are the appropriate orthogonal basis, as they are orthogonal with respect to the Gaussian measure in the log-transformed space. SinceEEis log-normal,ln⁡E\ln Eis Gaussian with meanμln⁡E\mu_{\ln E}and standard deviationσln⁡E\sigma_{\ln E}, so that standardizingln⁡E\ln Eyields a standard Gaussian variableE~∼𝒩​(0,1)\tilde{E}\sim\mathcal{N}(0,1)that serves as a proxy for the input,E~​(E)=ln⁡E−μln⁡Eσln⁡E.\tilde{E}(E)=\frac{\ln E-\mu_{\ln E}}{\sigma_{\ln E}}\;.(106)

The PCE approximation is then expressed asf^PCE​(E)=∑p=0Pcp​ϕp​(E~),\hat{f}_{\text{PCE}}(E)=\sum_{p=0}^{P}c_{p}\phi_{p}(\tilde{E})\;,(107)

whereϕp\phi_{p}denotes thepp-th orthogonal Hermite polynomial and the polynomial orderPPis a hyperparameter. To determine the expansion coefficients, we sampleN=50N=50training points(E(n))n=1N(E^{(n)})_{n=1}^{N}directly from the log-normal prior using Latin hypercube sampling. For each sampled value, the forward model is evaluated to obtain the corresponding outer radiusy(n)=f​(E(n))y^{(n)}=f(E^{(n)}), and the basis functions[𝚽]p​n=ϕp​(E~​(E(n)))[\bm{\Phi}]_{pn}=\phi_{p}(\tilde{E}(E^{(n)}))are used to form the design matrix𝚽\bm{\Phi}. The coefficientscpc_{p}are then determined by solving the optimization problem in Eq. (32) via least squares (cf. Section4.2), corresponding to the classical deterministic construction of PCEs. As shown in Section7, the PCE yields an analytic expression for the variance of the model responseVar​[y]≈Var​[f^PCE​(E)]=∑p=1Pcp2.\displaystyle\text{Var}[y]\approx\text{Var}[\hat{f}_{\text{PCE}}(E)]=\sum_{p=1}^{P}c_{p}^{2}\;.(108)

From a Bayesian perspective, this procedure does not constitute a fully probabilistic surrogate model and does not explicitly quantify surrogate uncertainty. A fully Bayesian treatment would instead formulate the surrogate construction itself as an inference problem, assigning probability distributions to the expansion coefficients, as exemplified in a later example (cf. Section6.3).

Together with the log-normal prior onEE, the PCE surrogate enables efficient computation of the posterior distribution of the output, the outer radius. The posterior is approximated using Monte Carlo sampling. Exemplary results based on synthetic simulation data are shown in Fig.7, illustrating how uncertainty in the Young’s modulus propagates into predictions of the outer radius under physiological loading conditions. For comparison, the results also show the posterior obtained with a uniform prior on the Young’s modulus, demonstrating the sensitivity of the inference to the choice of prior. In this case, Legendre polynomials were used as the PCE basis functions to enable a fair comparison.Figure 7:Surrogate-based uncertainty propagation through a finite element simulation of an idealized arterial wall under constant internal pressure, comparing the influence of informative (log-normal) vs. non-informative (uniform) priors on outer radius uncertainty.
(a) Sketched boundary value problem of an idealized arterial wall with inner radiusrinr_{\text{in}}, outer radiusroutr_{\text{out}}, and applied internal pressurePintP_{\rm int}.
(b) PCE surrogate models with Hermite basis (log-normal prior) and Legendre basis (uniform prior) of 5th-order, respectively, both achieve relative error<0.001%<0.001\%compared to the simulation data. The Legendre PCE is restricted to the interval[80,160][80,160]kPa as the uniform prior provides no information beyond this range. Training data are shown as markers.
(c) Log-normal (median 130 kPa, shape parameter 0.1) and uniform priors (80−16080-160kPa); overlaid is the model sensitivity|∂rout/∂E||\partial r_{\text{out}}/\partial E|, which increases at lower stiffness values.
(d) Propagated output distributions for outer radius obtained from10,00010,000Monte Carlo samples evaluated through PCE surrogates trained on5050Latin Hypercube samples. The non-informative uniform prior produces 25% larger uncertainty (standard deviation0.0150.015vs.0.0120.012mm), demonstrating how epistemic input uncertainty amplifies through the nonlinear forward model into predictive uncertainty.

## 5Bayesian model selection

Beyond qualitative comparisons, Bayesian model selection identifies the candidate model that best explains the observed data, formulated as

Identification of the most plausible model among competing hypotheses based on their posterior, thereby balancing model fit and complexity through the Bayesian evidence.

## 5.1General concept

In mechanics, we often encounter situations where several competing models may explain the same experimental data. For example, one may compare different surrogate models against a physics-based computational model or evaluate alternative constitutive laws for describing the experimental behavior of cardiac tissue, possibly using a multimodal dataset. Bayesian probability theory offers a principled mechanism for determining which model best explains the observations while accounting for uncertainty. This is the goal of Bayesianmodel selectionSivia and Skilling [2006].

To formalize this, we must make the dependence on the chosen model explicit. The probabilities must be conditioned not only on the model parameters, such as the parameters of a surrogate model, but also on the model hypothesis itself. Indeed, all probabilities until now were implicitly to be understood in the context of a given model hypothesis (cf. Section2); we had merely swept this information under the rug and not denoted this dependence explicitly.

For themm-th candidate model, we now make this dependence explicit by conditioning all probabilities on the model hypothesis. The likelihood function, which previously depended only on the parameters, is now written asp​(𝒟∣𝜽m)≡p​(𝒟∣𝜽m,ℳm),p(\mathcal{D}\mid\bm{\theta}_{m})\equiv p(\mathcal{D}\mid\bm{\theta}_{m},\mathcal{M}_{m})\;,(109)

whereℳm\mathcal{M}_{m},m=1,…,Nmm=1,\dots,N_{m}, denotes the model hypotheses and𝜽m\bm{\theta}_{m}its associated parameter vector. In the context of Section3.3, each hypothesisℳm\mathcal{M}_{m}specifies a particular surrogatef^m\hat{f}_{m}and therefore comes with its own parameterization. These parameters may represent, for example, the hyperparameters of a GP or the weights of a NN. Of course, each hypothesisℳm\mathcal{M}_{m}can also represent a physics-based forward modelfmf_{m}, where the parameters correspond to the material parameters in a constitutive law (cf. Section3.2).

While the likelihood (Eq. (109)) evaluates the data given specific parameter values and themm-th candidate, model selection requires assessing how well each model explains the data regardless of the particular parameter values chosen.
To quantify this, we perform a first marginalization over the parameters and introduce themarginal likelihood, also called themodel evidence,p​(𝒟∣ℳm)\displaystyle p(\mathcal{D}\mid\mathcal{M}_{m})=∫p​(𝒟∣𝜽m,ℳm)\displaystyle=\int p(\mathcal{D}\mid\bm{\theta}_{m},\mathcal{M}_{m})×p​(𝜽m∣ℳm)​d​𝜽m,\displaystyle\hphantom{=}\,\,\times p(\bm{\theta}_{m}\mid\mathcal{M}_{m})\>\mathrm{d}\bm{\theta}_{m}\;,(110)

which measures how well the hypothesisℳm\mathcal{M}_{m}explains the data on average, after integrating over all admissible parameter values.
This quantity, Eq. (5.1), previously appeared as a normalization constant when solving the inverse problem of parameter inference (cf. Sections3.2and3.3) and could be neglected since it does not affect the posterior distribution over parameters when the model is fixed. However, it becomes the central object for modelcomparison.

Having computed the model evidence for each candidate model in Eq. (5.1), we can now apply Bayes’ theorem to determine which model is most probable given the data. Treating the model hypothesisℳm\mathcal{M}_{m}itself as the unknown quantity, Bayes’ theorem yields the posterior of the model hypothesis,p​(ℳm∣𝒟)=p​(𝒟∣ℳm)​p​(ℳm)p​(𝒟),\displaystyle p(\mathcal{M}_{m}\mid\mathcal{D})=\frac{p(\mathcal{D}\mid\mathcal{M}_{m})p(\mathcal{M}_{m})}{p(\mathcal{D})}\;,(111)

which quantifies how plausible the modelℳm\mathcal{M}_{m}is in light of the data, irrespective of the specific parameter values. Two key factors appear: (i) the model evidencep​(𝒟∣ℳm)p(\mathcal{D}\mid\mathcal{M}_{m}), which plays the role of the likelihood and reflects how well the model explains the observations, and (ii) the prior modelp​(ℳm)p(\mathcal{M}_{m}), encoding how plausible the model was before seeing any data.

Treating the model itself as uncertain requires, according to the Bayesian paradigm, a second marginalizing, now over all model hypotheses. By the sum rule of probability,p​(𝒟)=∑m=1Nmp​(𝒟∣ℳm)​p​(ℳm).p(\mathcal{D})=\sum_{m=1}^{N_{m}}p(\mathcal{D}\mid\mathcal{M}_{m})p(\mathcal{M}_{m})\;.(112)

However, computing this summation is rarely feasible in practice.
Each term requires evaluating the model evidence via the integral in Eq. (5.1), which can be computationally prohibitive. Even when the marginal likelihood can be evaluated analytically for given hyperparameters (as in GP regression; cf. Section4.3), one often optimizes over hyperparameters rather than marginalizing over them, avoiding a second demanding integration. For this reason, model comparison often relies on approximations.

For practical comparison of two models,ℳm\mathcal{M}_{m}andℳm′\mathcal{M}_{m^{\prime}}, it is typically sufficient to consider the ratio of their posteriorsoo, defined aso=p​(ℳm∣𝒟)p​(ℳm′∣𝒟)⏟odds ratio=p​(𝒟∣ℳm)p​(𝒟∣ℳm′)⏟Bayes factor​p​(ℳm)p​(ℳm′)⏟prior odds,\displaystyle o=\underbrace{\frac{p(\mathcal{M}_{m}\mid\mathcal{D})}{p(\mathcal{M}_{m^{\prime}}\mid\mathcal{D})}}_{\text{odds ratio}}=\underbrace{\frac{p(\mathcal{D}\mid\mathcal{M}_{m})}{p(\mathcal{D}\mid\mathcal{M}_{m^{\prime}})}}_{\text{Bayes factor}}\;\underbrace{\frac{p(\mathcal{M}_{m})}{p(\mathcal{M}_{m^{\prime}})}}_{\text{prior odds}}\;,(113)

where the overall evidencep​(𝒟)p(\mathcal{D})cancels out, making pairwise comparison tractable and often sufficient for practical applications.
In fact, the three appearing terms have clear interpretations: the Bayes factor quantifies how strongly thedatasupport one model over another, while the prior odds capture anyprior preferencewe may have between the models. Together, they determine the posterior odds ratio, which represents our updated belief about which model is more probable after seeing the data151515As a special case, if two mutually exclusive and exhaustive models are considered, i.e., only one hypothesis can be true, the posteriors must satisfyp​(ℳm∣𝒟)+p​(ℳm′∣𝒟)=1.p(\mathcal{M}_{m}\mid{\mathcal{D}})+p(\mathcal{M}_{m^{\prime}}\mid{\mathcal{D}})=1.In this binary case, the odds ratiooodirectly quantifies how much more probable one model is compared to the other after observing the data..

But how should we interpret the magnitude of the odds ratiooo? Since the odds ratio can span many orders of magnitude, a logarithmic scale is commonly used. Although interpretation remain a matter of debate, Kass and RafteryKass and Raftery [1995]propose the following widely adopted classification:Hardly significant0<|\displaystyle 0<\lvertlog10(o)|<0.5,\displaystyle\log_{10}(o)\,\rvert<0.5\;,Positive evidence0.5<|\displaystyle 0.5<\lvertlog10(o)|<1,\displaystyle\log_{10}(o)\,\rvert<1\;,Strong evidence1<|\displaystyle 1<\lvertlog10(o)|<2,\displaystyle\log_{10}(o)\,\rvert<2\;,Overwhelming evidence|\displaystyle\lvertlog10(o)|>2.\displaystyle\log_{10}(o)\,\rvert>2\;.

For instance, an odds ratio of 100 (log10⁡(o)=2\log_{10}(o)=2) means that one model is 100 times more probable than the other, providing overwhelming evidence. An odds ratio of 10 (log10⁡(o)=1\log_{10}(o)=1) indicates that one model is 10 times more probable, already showing strong support. Conversely, an odds ratio of≈1\approx 1(log10⁡(o)≈0\log_{10}(o)\approx 0) suggests both models explain the data equally well, making it difficult to justify preferring one over the other.

While the Bayes factor is determined by the data and can often be computed or approximated, Bayesian reasoning also allows us to incorporate prior beliefs about the models themselves through the prior oddsp​(ℳm)p​(ℳm′),\frac{p(\mathcal{M}_{m})}{p(\mathcal{M}_{m^{\prime}})}\;,(114)

which is generally less straightforward than computing the Bayes factor.
A common assumption, particularly in surrogate modeling where no strong prior preference exists, is that all candidate models are equally likelya priori, i.e., before seeing any data. In such cases, the odds ratio reduces to the Bayes factor alone.
However, when data are limited and cannot strongly discriminate between models, the choice of prior odds becomes more influential in determining the posterior model probabilities. Further discussions and advanced techniques can be found in the specialized literatureO’Hagan [1995], Sivia and Skilling [2006], von Toussaint [2011], von der Linden et al. [2014].

While our discussion has emphasized surrogate models as competing hypotheses, model selection is equally relevant to physics-based forward models in mechanics, particularly within constitutive modeling. Bayesian model selection has been applied in discriminating among constitutive descriptions for soft biological tissuesMadireddy et al. [2015], Aggarwal et al. [2023]and various engineering materialsRitto and Nunes [2015], Mototake et al. [2020], Battalgazy et al. [2025], with comparisons to sparse regression algorithms for automated model discoveryUrrea–Quintero et al. [2026]. Similar Bayesian frameworks have been employed to evaluate competing fatigue damage progression laws in compositesChiachío et al. [2015]and to adjudicate between computational fracture modelsHamdia et al. [2019]. Furthermore, researchers have aimed to identify the optimal constitutive models for predicting pulmonary hemodynamicsPaun et al. [2020], to select among phenomenological tumor-growth modelsOden et al. [2913], or to differentiate between rheological models for yield-stress fluidsRinkens et al. [2026], to name a few.

## 5.2Example: Derivation of the Bayesian information criterion

Since the evidence integral in Eq. (5.1) is generally intractable, we next derive a closed-form approximation for practical model comparison. The following argument provides a controlled sequence of approximations, following the spirit ofvon Toussaint [2011], von der Linden et al. [2014].

Step 1: Approximating a flat prior.We assume that the priorp​(𝜽m)p(\bm{\theta}_{m})is sufficiently broad compared to the likelihood, so that within the region where the likelihood is significant, the prior is effectively constantp​(𝜽m)≈1ΛmPm​p​(𝜽¯m),p(\bm{\theta}_{m})\approx\frac{1}{\Lambda_{m}^{P_{m}}}p(\bar{\bm{\theta}}_{m})\;,(115)

whereΛm\Lambda_{m}is the characteristic prior width per dimension arising from normalization,PmP_{m}is the number of parameters in modelℳm\mathcal{M}_{m}, and𝜽¯m\bar{\bm{\theta}}_{m}is a representative prior value, here taken as the mode of the likelihood. Substituting this into the evidence integral givesp​(𝒟∣ℳm)\displaystyle p(\mathcal{D}\mid\mathcal{M}_{m})≈1ΛmPm​p​(𝜽¯m)\displaystyle\approx\frac{1}{\Lambda_{m}^{P_{m}}}p(\bar{\bm{\theta}}_{m})×∫p(𝒟∣𝜽m,ℳm)d𝜽m.\displaystyle\hphantom{=}\,\,\times\int p(\mathcal{D}\mid\bm{\theta}_{m},\mathcal{M}_{m})\>\mathrm{d}\bm{\theta}_{m}\;.(116)

Step 2: Approximating the likelihood near its maximum.Next, we assume that for large sample sizeNN, the likelihood becomes sharply peaked around the maximum likelihood estimate𝜽m∗=arg⁡max𝜽m⁡p​(𝒟∣𝜽m,ℳm).\bm{\theta}^{\ast}_{m}=\arg\max_{\bm{\theta}_{m}}p(\mathcal{D}\mid\bm{\theta}_{m},\mathcal{M}_{m})\;.(117)

To leading order, we approximate the likelihood as approximately constant within a small region of volumeΔmPm\Delta_{m}^{P_{m}}, and negligible outside. Under this approximation,∫p​(𝒟∣𝜽m,ℳm)​d𝜽m≈p​(𝒟∣𝜽m∗,ℳm)​ΔmPm.\int p(\mathcal{D}\mid\bm{\theta}_{m},\mathcal{M}_{m})\,\mathrm{d}\bm{\theta}_{m}\approx p(\mathcal{D}\mid\bm{\theta}^{\ast}_{m},\mathcal{M}_{m})\,\Delta_{m}^{P_{m}}\;.(118)

Step 3: Combining both approximations. Combining the results from Steps 1 and 2, and taking the logarithm on both sides, yieldslog⁡p​(𝒟∣ℳm)\displaystyle\log p(\mathcal{D}\mid\mathcal{M}_{m})≈log⁡p​(𝒟∣𝜽m∗,ℳm)\displaystyle\approx\log p(\mathcal{D}\mid\bm{\theta}^{\ast}_{m},\mathcal{M}_{m})−Pm​log⁡(ΛmΔm).\displaystyle\hphantom{=}\,\,-P_{m}\log\left(\frac{\Lambda_{m}}{\Delta_{m}}\right)\;.(119)

Step 4: Scaling assumptions with sample size.To make further progress, we relate the likelihood widthΔm\Delta_{m}to the number of data pointsNN. For many standard likelihoods — in particular for Gaussian likelihoods — the width of the region where the likelihood is significant shrinks proportionally to1/N1/\sqrt{N}as more data accumulatesΔm=σN,\Delta_{m}=\frac{\sigma}{\sqrt{N}}\;,(120)

for someO​(1)O(1)proportionality constantσ\sigma. If the prior information is taken to be on the same order as the information contained in one data point, i.e.,Λm≈σ\Lambda_{m}\approx\sigma, then,log⁡p​(𝒟∣ℳm)\displaystyle\log p(\mathcal{D}\mid\mathcal{M}_{m})≈log⁡p​(𝒟∣𝜽m∗,ℳm)\displaystyle\approx\log p(\mathcal{D}\mid\bm{\theta}^{\ast}_{m},\mathcal{M}_{m})−Pm2​log⁡N.\displaystyle\hphantom{=}\,\,-\frac{P_{m}}{2}\,\log N\;.(121)

This motivates the standard definition of theBayesian information criterion(BIC) asBICm=−2​log⁡p​(𝒟∣𝜽m∗,ℳm)+Pm​log⁡N,\mathrm{BIC}_{m}=-2\log p(\mathcal{D}\mid\bm{\theta}^{\ast}_{m},\mathcal{M}_{m})+P_{m}\log N\;,(122)

which provides a crude but practical approximation to the model evidence and is widely used when exact evidence computation is infeasible. Since model selection seeks to maximize the evidence or, equivalently, to minimize its negative logarithm, we choose the model with the smallest BIC value.

The key reason for the practicality of BIC is that it replaces the intractable high-dimensional evidence integral with a simple closed-form expression that depends only on the maximum likelihood value, the number of model parameters, and the size of the dataset. This is achieved through two simplifying assumptions: (i) the prior is effectively constant in the region where the likelihood is significant, and (ii) the likelihood is sharply peaked around its maximum and can be approximated by a hypercube. As a result, BIC is far easier to compute than the full evidence.

Note that the BIC valuedecreasesas the maximum likelihood increases, butincreaseswith the number of parametersPmP_{m}. This creates a natural trade-off: models with more parameters can achieve better fits to the data (lower first term), but are penalized for their increased complexity (higher second term). This automatic model complexity penalization is a manifestation ofOccam’s razor, meaning that if two models explain the data equally well (as measured by the maximum likelihood), the simpler model (with fewer parameters) is preferred because it has the smaller BIC value.

The literature offers a wide variety of related, more or less controlled approximations and model selection criteria, such as theAkaike information criterionAkaike [2003]. The interested reader is referred toStoica and Selen [2004]for a broader overview of such methods.

## 5.3Example: Kernel selection for Gaussian processes

As a first example of Bayesian model selection, we consider comparing several GP surrogate models that differ only in their choice of covariance kernel. But why does the kernel choice matter? Different kernels encode different prior assumptions about the underlying function: smoothness (squared exponential), controlled roughness (Matérn), periodicity (periodic kernels), multi-scale behavior (rational quadratic), or additive/compositional structure. Bayesian model selection provides a principled framework to let the data inform this choice. Each kernelkm​(⋅,⋅;𝜽m)k_{m}(\cdot,\cdot;\bm{\theta}_{m}), together with its hyperparameters𝜽m\bm{\theta}_{m}, defines a distinct model hypothesisℳm\mathcal{M}_{m}.

Let us first revisit the GP framework as introduced in Section4.3. For dataset𝒟=(𝐱¯,𝒚)\mathcal{D}=(\underline{\mathrm{\bm{x}}},\bm{y}), assuming a zero-mean GP prior with kernelkm​(⋅,⋅;𝜽m)k_{m}(\cdot,\cdot;\bm{\theta}_{m})and i.i.d. Gaussian observation noiseη(n)∼𝒩​(0,σ2)\eta^{(n)}\sim\mathcal{N}(0,\sigma^{2}), the likelihood for themm-th model takes the multivariate Gaussian form𝒚∣𝐱¯,𝜽m,ℳm∼𝒩​(𝟎,Km​(𝜽m)+σ2​I),\bm{y}\mid\underline{\mathrm{\bm{x}}},\bm{{\bm{\theta}}}_{m},\mathcal{M}_{m}\sim\mathcal{N}\Big(\mathbf{0},K_{m}(\bm{\theta}_{m})+\sigma^{2}I\Big)\;,(123)

whereKm​(𝜽m)K_{m}(\bm{\theta}_{m})is the Gram matrix with entries[Km]i​j=km​(𝐱(i),𝐱(j);𝜽m)[K_{m}]_{ij}=k_{m}(\mathbf{x}^{(i)},\mathbf{x}^{(j)};\bm{\theta}_{m}). Inserting this into Eq. (5.1), the model evidence becomesp​(𝒟∣ℳm)\displaystyle p(\mathcal{D}\mid\mathcal{M}_{m})=∫exp⁡(−12​𝒚T​(Km​(𝜽m)+σ2​I)−1​𝒚)(2​π)N​|Km​(𝜽m)+σ2​I|\displaystyle=\int\frac{\exp\Big(-\tfrac{1}{2}\,\bm{y}^{\rm T}(K_{m}(\bm{\theta}_{m})+\sigma^{2}I)^{-1}\bm{y}\Big)}{\sqrt{(2\pi)^{N}\big|K_{m}(\bm{\theta}_{m})+\sigma^{2}I\big|}}×p​(𝜽m)​d​𝜽m.\displaystyle\hphantom{=}\,\,\times p(\bm{\theta}_{m})\;\mathrm{d}\bm{\theta}_{m}\;.(124)

Crucially, the choice of kernelkm​(⋅,⋅;𝜽m)k_{m}(\cdot,\cdot;\bm{\theta}_{m})determines the entire GP model hypothesisℳm\mathcal{M}_{m}. Different kernels yield different Gram matricesKm​(𝜽m)K_{m}(\bm{\theta}_{m}), which in turn affect both the data-fit term𝒚T​(Km+σ2​I)−1​𝒚\bm{y}^{\rm T}(K_{m}+\sigma^{2}I)^{-1}\bm{y}, measuring how well the data conform to the GP model’s assumed covariance structure, and the complexity penalty|Km+σ2​I|\lvert K_{m}+\sigma^{2}I\rvert, which penalizes overly flexible models that can accommodate a wide range of functions.

Computing the integral in Eq. (5.3) exactly rarely admits a closed-form solution and is often intractable. A common approximation is to assume that the posterior over hyperparameters is sharply peaked at its MAP estimate, i.e.,p​(𝜽m∣𝒟,ℳm)≈δ​(𝜽m−𝜽m∗)p(\bm{\theta}_{m}\mid\mathcal{D},\mathcal{M}_{m})\approx\delta(\bm{\theta}_{m}-\bm{\theta}_{m}^{\ast}),
where𝜽m∗=arg⁡max𝜽m⁡p​(𝜽m∣𝒟,ℳm).\bm{\theta}_{m}^{\ast}=\arg\max_{\bm{\theta}_{m}}p(\bm{\theta}_{m}\mid\mathcal{D},\mathcal{M}_{m})\;.(125)

Under this approximation, the model evidence becomesp​(𝒟∣ℳm)≈exp⁡(−12​𝒚T​(Km​(𝜽m∗)+σ2​I)−1​𝒚)(2​π)N​|Km​(𝜽m∗)+σ2​I|​p​(𝜽m∗),p(\mathcal{D}\mid\mathcal{M}_{m})\approx\frac{\exp\big(-\tfrac{1}{2}\bm{y}^{\rm T}(K_{m}(\bm{\theta}_{m}^{\ast})+\sigma^{2}I)^{-1}\bm{y}\big)}{\sqrt{(2\pi)^{N}\lvert K_{m}(\bm{\theta}_{m}^{\ast})+\sigma^{2}I\rvert}}p(\bm{\theta}_{m}^{\ast})\;,(126)

Taking the logarithm and assuming a flat prior on𝜽m\bm{\theta}_{m}, we can reduce this to the log marginal likelihood in Eq. (4.3) — precisely the GP hyperparameter optimization objective from Section4.3.

This derivation explains why the log marginal likelihood serves as a legitimate criterion for GP model selection and clarifies the underlying approximation: we evaluate at the MAP hyperparameter estimate rather than integrating over all possible values. Kernel comparison thus reduces to computing Eq. (4.3) for each kernel following hyperparameter optimization and forming their ratio as the Bayes factor. In contrast, it would be unclear how to generalize ad-hoc criteria such as least squares fit or loss functions (cf. Sections4.2,3.4and4.4.1) to GP model comparison without Bayesian probability theory as a foundation.

In practice, however, the posterior over hyperparameters is oftennotsharply peaked and may even multi-modal, limiting the validity of the MAP approximation. For low-dimensional hyperparameter spaces, the integral in Eq. (5.3) can sometimes be evaluated numerically. This becomes infeasible for high-dimensional parameter spaces, as encountered in NNs. In such cases, a common approach is to approximate the evidence locally near the MAP point using a Laplace approximation or related variantsJavid et al. [2020], Wilson and Izmailov [2020].

Due to these difficulties, many heuristic or approximate model–selection criteria exist, such as cross-validationStone [1974,1977], variousinformation criteriaTrevor et al. [2009], or other approximations of the model evidence. In the following examples, we will examine one suchcontrolledapproximation in more detail.

## 5.4Example: Analytical model evidence for polynomial chaos expansions

How can a flat prior on the PCE coefficients penalize model complexity at all? For certain classes of PCEs the marginal likelihood (cf. Eq. (5.1)) admits a closed form, which makes them an ideal showcase for how Bayesian model selection trades model complexity against parsimony. We construct the evidence term by term, isolate the factors that act as an effective prior on complexity, and then demonstrate the mechanism on a nested sequence of polynomials.

As shown inRanftl and von der Linden [2021], the model evidence for a PCEℳm:ℝD→ℝ\mathcal{M}_{m}:\mathbb{R}^{D}\to\mathbb{R}— or, more generally, for a linear surrogate model as in Eq. (31) — admits a closed-form expression under three assumptions. First, the likelihood is Gaussian with known or unknown variance, equivalent to a Student-ttmarginal likelihood. Second, the prior on the expansion coefficients is flat. Third, the basis functions are fixed, and only their numberPmP_{m}changes with model indexmm.

Before stating the evidence, we introduce the notation. The design matrixMmM_{m}collects the basis functions evaluated at the data, with entries[Mm]i,q=ϕq​(𝐱(i))[M_{m}]_{i,q}=\phi_{q}(\mathbf{x}^{(i)}), andHm=MmT​MmH_{m}=M_{m}^{\mathrm{T}}M_{m}is the associated Gram matrix (cf. Section4.2). The minimal residual sum of squares isχm2=𝐲T​(I−Mm​Hm−1​MmT)​𝐲\chi_{m}^{2}=\mathbf{y}^{\mathrm{T}}(I-M_{m}H_{m}^{-1}M_{m}^{\mathrm{T}})\mathbf{y}, where the term in the brackets is the orthogonal projector onto the complement of the column space ofMmM_{m}. Thisχm2\chi_{m}^{2}coincides with the value obtained from either the posterior mean or the maximum likelihood estimate of the coefficients, andNNdenotes the number of data points.

With known variance, the matter boils down to a simple marginalization of the coefficientscpc_{p}, a Gaussian integral to be solved by completing the square. In surrogate modeling, however, the variance of the surrogate isnotknowna priori. Indeed, that seems a rather incredulous assumption!
With unknown variance, one must additionally marginalize over the unknown variance. Placing Jeffreys’ prior on the scale,p​(σ)∝1/σp(\sigma)\propto 1/\sigma, the model evidence becomesp​(𝒟∣ℳm)\displaystyle p(\mathcal{D}\mid\mathcal{M}_{m})=ΩPm​|Hm|−12​(χm2)−N−Pm2\displaystyle=\Omega_{P_{m}}\;|H_{m}|^{-\frac{1}{2}}\big(\chi_{m}^{2}\big)^{-\frac{N-P_{m}}{2}}×Γ​(Pm2)​Γ​(N−Pm2)Γ​(N2),\displaystyle\hphantom{=}\,\,\times\frac{\Gamma\left(\frac{P_{m}}{2}\right)\Gamma\left(\frac{N-P_{m}}{2}\right)}{\Gamma\left(\frac{N}{2}\right)}\;,(127)

wherePmP_{m}denotes the number of PCE basis functions in modelℳm\mathcal{M}_{m},Γ​(⋅)\Gamma(\cdot)is the Gamma function, andΩPm=2​πPm/2/Γ​(Pm/2)\Omega_{P_{m}}=2\pi^{P_{m}/2}/\Gamma(P_{m}/2)is the solid angle of the unit sphere inPmP_{m}dimensions.

The factors in Eq. (5.4) split into two groups that play different roles. Thedata-dependentfactors|Hm|−1/2|H_{m}|^{-1/2}and(χm2)−(N−Pm)/2\big(\chi_{m}^{2}\big)^{-(N-P_{m})/2}reward a model that fits the data and occupies a favorable region of parameter space. Thedata-independentfactors, namely the solid angleΩPm\Omega_{P_{m}}and the two Gamma functionsΓ​(Pm/2)\Gamma\left(P_{m}/2\right)andΓ​((N−Pm)/2)\Gamma\left((N-P_{m})/2\right), depend only on the countsNNandPmP_{m}. Keeping these two groups apart is the key to the analysis, since the data-independent group alone carries the automatic complexity penalty we isolate below.

This answers the opening question. Even with a flat prior on the coefficients, the evidence integral induces a preference for simpler models through its geometric factors, so these terms act as aneffective prioron model complexity. The effect depends on both the number of observationsNNand the model dimensionPmP_{m}, as visualized in Fig.8. Figure8(b) shows that the solid angle contribution alone biases strongly toward low-dimensional models, independently of any explicitly chosen prior.Figure 8:Illustration of the (a) effective prior structure as a function of the number of observationsNNand surrogate parametersPmP_{m}, as introduced in Eq. (5.4), showing the combined influence of solid angle and parameter prior. (b) Solid angle effect demonstrating geometric constraints from the likelihood. (c) Intrinsic prior term excluding the solid angle contribution. The boundaryN=PmN=P_{m}(black line) separates valid from invalid parameter regions. Colormap in (b) also applied to (a), y-label in (a) also applies to (b,c).

Consider a nested sequence of polynomial models in one input dimension,𝒙∈ℝ\bm{x}\in\mathbb{R}or𝒙≔x∈ℝ\bm{x}\coloneqq x\in\mathbb{R}?. Each model adds one polynomial to the previous basis,φ1={1},ϕ2={1,x},ϕ3={1,x,x2},\displaystyle\char 102\relax_{1}=\{1\}\;,\quad\phi_{2}=\{1,x\},\quad\phi_{3}=\{1,x,x^{2}\}\;,…,ϕPm={1,x,…,xPm−1},\displaystyle\dots\;,\quad\phi_{P_{m}}=\{1,x,\dots,x^{P_{m}-1}\}\;,(128)

so thatℳm⊂ℳm+1\mathcal{M}_{m}\subset\mathcal{M}_{m+1}for allmm.

To illustrate the automatic complexity penalization in Eq. (5.4), consider its data-independent factors, the solid angleΩPm\Omega_{P_{m}}and the two Gamma functionsΓ​(Pm/2)\Gamma(P_{m}/2)andΓ​((N−Pm)/2)\Gamma((N-P_{m})/2). We advance along a coarse subsequence of the nested hierarchy in steps of two,Pm+1=Pm+2P_{m+1}=P_{m}+2.161616The even step ensures that for evenNNthe half-integer arguments of the Gamma functions in Eq. (5.4) collapse to factorials, so the evidence ratio takes an elementary form. A unit step leaves half-integer Gamma functions, which remain computable but obscure the mechanism this example isolates.

Consider first the solid angle alone, isolated in Fig.8(b). For the stepPm→Pm+2P_{m}\to P_{m}+2it contributesΩPm+2ΩPm=π​Γ​(Pm2)Γ​(Pm2+1)=2​πPm,\frac{\Omega_{P_{m}+2}}{\Omega_{P_{m}}}=\pi\frac{\Gamma(\frac{P_{m}}{2})}{\Gamma(\frac{P_{m}}{2+1})}=\frac{2\pi}{P_{m}}\;,(129)

where we usedΓ​(Pm/2+1)=(Pm/2)​Γ​(Pm/2)\Gamma(P_{m}/2+1)=(P_{m}/2)\,\Gamma(P_{m}/2). Its logarithm scales as−log⁡Pm-\log P_{m}, a geometric bias toward low-dimensional models that persists even under the flat coefficient prior.

Including the Gamma functions changes this scaling. Their ratio contributesΓ​(Pm+12)​Γ​(N−Pm+12)Γ​(Pm2)​Γ​(N−Pm2)=PmN−Pm−2,\frac{\Gamma(\frac{P_{m+1}}{2})\Gamma\big(\frac{N-P_{m+1}}{2}\big)}{\Gamma(\frac{P_{m}}{2})\Gamma\big(\frac{N-P_{m}}{2}\big)}=\frac{P_{m}}{N-P_{m}-2}\;,(130)

whose factorPmP_{m}cancels the one from the solid angle. The full data-independent prefactor is thereforeΩPm+2ΩPm​PmN−Pm−2=2​πN−Pm−2.\frac{\Omega_{P_{m}+2}}{\Omega_{P_{m}}}\frac{P_{m}}{N-P_{m}-2}=\frac{2\pi}{N-P_{m}-2}\;.(131)

Reinstating the data-dependent factors from Eq. (5.4), namely|Hm|/|Hm+1|\sqrt{|H_{m}|/|H_{m+1}|}and theχ2\chi^{2}terms, gives the full evidence ratiop​(ℳm+1∣𝒟)p​(ℳm∣𝒟)\displaystyle\frac{p\big(\mathcal{M}_{m+1}\bm{\mid}\mathcal{D}\big)}{p\big(\mathcal{M}_{m}\bm{\mid}\mathcal{D}\big)}=2​πN−Pm−2​|Hm||Hm+1|\displaystyle=\frac{2\pi}{N-P_{m}-2}\sqrt{\frac{|H_{m}|}{|H_{m+1}|}}×(χm2χm+12)(N−Pm)/2​χm+12.\displaystyle\hphantom{=}\,\,\times\biggl(\frac{\chi_{m}^{2}}{\chi_{m+1}^{2}}\biggr)^{(N-P_{m})/2}\chi_{m+1}^{2}\;.(132)

Keeping only this prefactor and dropping the fit termsHHandχ2\chi^{2}, the logarithmic contribution scales aslog⁡p​(ℳm+1∣𝒟)p​(ℳm∣𝒟)∼∝−log⁡(N−Pm−2).\displaystyle\log\frac{p\big(\mathcal{M}_{m+1}\bm{\mid}\mathcal{D}\big)}{p\big(\mathcal{M}_{m}\bm{\mid}\mathcal{D}\big)}\stackrel{{\scriptstyle\propto}}{{\sim}}-\log\!\big(N-P_{m}-2\big)\;.(133)

In other words, moving to a higher polynomial order multiplies the posterior odds by the factor2​π/(N−Pm−2)2\pi/(N-P_{m}-2). So, the more complex model is penalized unless the extra parameters improve the fit at least by the same factor. This penalty grows only slowly, likelog⁡(N−Pm−2)\log(N-P_{m}-2), with the number of observationsNN, and it does not depend on how well either model fits the data. Over a whole sequence of models these factors multiply, so the penalty adds up as the models grow more complex.
This fundamental effect again illustratesOccam’s razor: If two models explain the data equally well, the simpler model is more likely to be true.

The same complexity penalty appears when we replace the exact evidence with its BIC approximation. Following the reasoning in the previous example, we obtainp​(ℳm+1∣𝒟)p​(ℳm∣𝒟)\displaystyle\frac{p(\mathcal{M}_{m+1}\mid\mathcal{D})}{p(\mathcal{M}_{m}\mid\mathcal{D})}≈p​(𝒟∣𝜽m+1∗,ℳm+1)p​(𝒟∣𝜽m∗,ℳm)⏟≥1\displaystyle\approx\underbrace{\frac{p(\mathcal{D}\mid\bm{\theta}^{\ast}_{m+1},\mathcal{M}_{m+1})}{p(\mathcal{D}\mid\bm{\theta}^{\ast}_{m},\mathcal{M}_{m})}}_{\geq 1}×(ΔmΛm)Pm​(ΛmΔm)Pm+1⏟ΛmΔm≫1.\displaystyle\hphantom{=}\,\,\times\underbrace{\left(\frac{\Delta_{m}}{\Lambda_{m}}\right)^{P_{m}}\left(\frac{\Lambda_{m}}{\Delta_{m}}\right)^{P_{m+1}}}_{\frac{\Lambda_{m}}{\Delta_{m}}\gg 1}\;.(134)

where the likelihood ratio favors the more complex model if it fits the data better, while the Occam factor penalizes the additional parameters.
Here,𝜽m∗\bm{\theta}^{\ast}_{m}and𝜽m+1∗\bm{\theta}^{\ast}_{m+1}denote the maximum likelihood estimates for modelsℳm\mathcal{M}_{m}andℳm+1\mathcal{M}_{m+1}. The quantityΔm\Delta_{m}is the typical width of the likelihood around the MLE, the region wherep​(𝒟∣𝜽,ℳ)p(\mathcal{D}\mid\bm{\theta},\mathcal{M})is non-negligible, which scales asΔm∼σ/N\Delta_{m}\sim\sigma/\sqrt{N}for Gaussian-like likelihoods. The characteristic width isΛm\Lambda_{m}, assumed independent ofNN, so the ratioΛm/Δm\Lambda_{m}/\Delta_{m}quantifies how much the data concentrates the posterior relative to the prior. SinceΛm/Δm≫1\Lambda_{m}/\Delta_{m}\gg 1for sufficiently largeNN, the Occam factor(Λm/Δm)Pm+1−Pm(\Lambda_{m}/\Delta_{m})^{P_{m+1}-P_{m}}grows exponentially with the difference in model dimensions, penalizing additional parameters unless they substantially improve the likelihood.

For nested models the likelihood ratio is≥1\geq 1, sinceℳm+1\mathcal{M}_{m+1}reproduces at least the same fit asℳm\mathcal{M}_{m}by an appropriate choice of parameters. The Occam factor(Λm/Δm)Pm+1−Pm(\Lambda_{m}/\Delta_{m})^{P_{m+1}-P_{m}}nonetheless penalizes the added complexity, and becauseΛm/Δm∼N\Lambda_{m}/\Delta_{m}\sim\sqrt{N}this penalty grows with the number of data points, making additional parameters increasingly hard to justify without a substantial improvement in fit.

Three remarks close the example. First, the result requires no orthogonality of the basis functions, so the derivation applies to any surrogate model that is linear in its parameters. Second, Eq. (5.4) is exact, whereas the BIC provides only a crude approximation. Third, for multi-output PCE withℳm:ℝD→ℝQ\mathcal{M}_{m}:\mathbb{R}^{D}\to\mathbb{R}^{Q}the evidence admits a closed-form expression of similar form when the outputs are uncorrelated, for which we refer toRanftl and von der Linden [2021].

This trade-off embodiesOccam’s razor. Simpler models are preferred unless the data support additional complexity. The posterior odds balance parsimony against explanatory power.

## 6Bayesian experimental design

We can formulate the core objective of Bayesian experimental designChaloner and Verdinelli [1995], DasGupta [1996], Lindley [1972]as:

Selection of next experimental or simulation conditions that maximize the expected information gain about uncertain model parameters or predictions, thereby enabling more efficient learning from limited data.

## 6.1General concept

Until now we assumed that the dataset is fixed and given. In many realistic settings, however, data collection is costly, and we may wish to actively select new data points in order to learn as efficiently as possible. This situation arises frequently in mechanics, where obtaining new data may involve running a computationally expensive simulation or performing a labor-intensive experiment. In such cases, we want to use all available information to decide where to sample next — that is, which experiment or simulation with a particular parameter set will be most informative.

Formally, given a dataset obtained from computer simulations — see the workflow introduced in Fig.2— we define𝒟=(𝒙(n),y(n))n=1N,\mathcal{D}=\big(\bm{x}^{(n)},y^{(n)}\big)_{n=1}^{N}\;,(135)

we seek the next optimal input parameter set𝒙(N+1)\bm{x}^{(N+1)}at which to query new observationsy(N+1)y^{(N+1)}. For notational simplicity, we sety∗≡y(N+1)y_{\ast}\equiv y^{(N+1)}and𝒙∗≡𝒙(N+1)\bm{x}_{\ast}\equiv\bm{x}^{(N+1)}, analogous to the notation for new data in GPs (cf. Section4.3).

To make a principled decision about the next query, we introduce the notion ofutility. A utility functionU​(y∗,𝒟)U(y_{\ast},\mathcal{D})quantifies the benefit of observing a new output data pointy∗y_{\ast}at design location𝒙∗\bm{x}_{\ast}, given the current dataset𝒟\mathcal{D}. The choice of utility depends on the modeling objective: it could represent the expected reduction in uncertainty, the improvement in model accuracy, or the information gained about model parameters.

In Bayesian experimental design, we select theoptimalnext query point𝒙∗\bm{x}^{\ast}— where, as in previous sections, a subscript asterisk denotes a new point and a superscript asterisk denotes the optimal point — by maximizing theexpected utility,𝒙∗\displaystyle\bm{x}^{\ast}=arg⁡max𝒙∗⁡𝔼​[U​(y∗,𝒟)],\displaystyle=\arg\max_{\bm{x}_{\ast}}\mathbb{E}\big[U(y_{\ast},\mathcal{D})\big]\;,(136)

where𝔼​[U​(y∗,𝒟)]\displaystyle\mathbb{E}\big[U(y_{\ast},\mathcal{D})\big]=∫U​(y∗,𝒟)​p​(y∗∣𝒙∗,𝒟)​dy∗\displaystyle=\int U(y_{\ast},\mathcal{D})p(y_{\ast}\mid\bm{x}_{\ast},\mathcal{D})\>\mathrm{d}y_{\ast}=∫U​(y∗,𝒟)​∫p​(y∗∣𝒙∗,𝒟,𝜽)\displaystyle=\int U(y_{\ast},\mathcal{D})\int p(y_{\ast}\mid\bm{x}_{\ast},\mathcal{D},\bm{\theta})×p​(𝜽∣𝒟)​d​𝜽​d​y∗.\displaystyle\hphantom{=}\,\,\times p(\bm{\theta}\mid\mathcal{D})\;\mathrm{d}\bm{\theta}\>\mathrm{d}y_{\ast}\;.(137)

Here,𝜽\bm{\theta}denotes the parameters of the probabilistic surrogate model. The existing dataset obtained from the computer simulation is used to train this surrogate, which provides a probabilistic approximation of the mapping𝒙↦y\bm{x}\mapsto y. Consequently,𝜽\bm{\theta}represents the surrogate model parameters, and their posterior distributionp​(𝜽∣𝒟)p(\bm{\theta}\mid\mathcal{D})quantifies the current uncertainty in that approximation.

This expression states that the expected utility is the average usefulness of observing a new data point at𝒙∗\bm{x}_{\ast}, taken over all possible outcomesy∗y_{\ast}that could occur. The inner integral marginalizes over the current uncertainty in the model parameters𝜽\bm{\theta}and the outer integral averages over all potential new observationsy∗y_{\ast}, weighted by their predictive likelihoodp​(y∗∣𝒟)p(y_{\ast}\mid\mathcal{D}). Thus, the expected utility formalizes the benefit of sampling at a proposed design point, accounting for both parameter uncertainty and observation uncertainty.

A popular choice for the utility function is theinformation gain, measured by the Kullback–Leibler (KL) divergenceMacKay [1992], Loredo [2004],U​(y∗,𝒟)\displaystyle U(y_{\ast},\mathcal{D})=∫p​(𝜽∣𝒟,y∗)\displaystyle=\int p(\bm{\theta}\mid\mathcal{D},y_{\ast})×log⁡[p​(𝜽∣𝒟,y∗)p​(𝜽∣𝒟)]​d​𝜽,\displaystyle\hphantom{=}\,\,\times\log\Bigg[\frac{p(\bm{\theta}\mid\mathcal{D},y_{\ast})}{p(\bm{\theta}\mid\mathcal{D})}\Bigg]\>\mathrm{d}\bm{\theta}\;,(138)

which quantifies how much the posterior would change after observingy∗y_{\ast}, relative to either the prior or the posterior at iterationNN. Intuitively, a larger KL divergence indicates that the potential observation is moreinformativeabout𝜽\bm{\theta}. Other utility measures exist, such as Wasserstein distancesHelin et al. [2025]or the cross-entropyLoredo [2004]; see, e.g.,Chaloner and Verdinelli [1995], DasGupta [1996], von Toussaint [2011]for an overview of utility functions.

Given the KL utility, the corresponding expected utility is𝔼​[U​(y∗,𝒟)]\displaystyle\mathbb{E}\big[U(y_{\ast},\mathcal{D})\big]=∬p​(𝜽∣𝒟,y∗)​log⁡[p​(𝜽∣𝒟,y∗)p​(𝜽∣𝒟)]\displaystyle=\iint p(\bm{\theta}\mid\mathcal{D},y_{\ast})\log\Bigg[\frac{p(\bm{\theta}\mid\mathcal{D},y_{\ast})}{p(\bm{\theta}\mid\mathcal{D})}\Bigg]×∫p(y∗∣𝒟,𝜽)\displaystyle\hphantom{=}\,\,\times\int p(y_{\ast}\mid\mathcal{D},\bm{\theta})×p​(𝜽)​d​𝜽​d​𝜽​d​y∗.\displaystyle\hphantom{=}\,\,\times p(\bm{\theta})\>\mathrm{d}\bm{\theta}\>\mathrm{d}\bm{\theta}\>\mathrm{d}y_{\ast}\;.(139)

This expression again highlights that we average the resulting information gain over all possible future outcomesy∗y_{\ast}, weighting each outcome by its predictive likelihood.

Because a future observation cannot retroactively change the prior information about the parameters, practical acquisition strategies often approximatep​(𝜽∣𝒟,y∗)≈p​(𝜽∣𝒟)p(\bm{\theta}\mid\mathcal{D},y_{\ast})\approx p(\bm{\theta}\mid\mathcal{D}).
In practice, only two ingredients are needed: (i) the current posteriorp​(𝜽∣𝒟)p(\bm{\theta}\mid\mathcal{D})and (ii) the predictive modelp​(y∗∣𝒟,𝜽)p(y_{\ast}\mid\mathcal{D},\bm{\theta}). Here, the predictive modelp​(y∗∣𝒟,𝜽)p(y_{\ast}\mid\mathcal{D},\bm{\theta})is the surrogate’s probabilistic prediction for a new output at𝒙∗\bm{x}_{\ast}, conditioned on the data and the surrogate parameters. The structure of these integrals naturally leads to nested posterior-sampling schemesvon Toussaint [2011], but these are often computationally intractable for complex models. This motivates several practical approximations, ultimately leading to what the machine learning community refers to asBayesian optimization.

In summary, when experiments involve an expensive computer simulation, the workflow proceeds as follows: (i) define a probabilistic model with a prior on the unknown parameters and a likelihood linking the design variables to the simulated data, and choose a utility function; (ii) use a surrogate model to approximate the costly simulation and efficiently evaluate the expected utility; and (iii) maximize this utility to select the next simulation point, run the corresponding simulation, update the posterior, and repeat if using a sequential design.

Among the notable earlier contributions to this field, Shannon-type expected information gain was employed to develop methodologies for optimal experimental design in algebraic nonlinear problems and combustion kinetic modelsHuan and Marzouk [2013]and further applied to assess experiment relevance under model uncertainty and to identify source locations in impedance tomographyLong et al. [2013], Beck et al. [2018].
Further contributions proposed measuring the information gain from a hypothetical experiment as the Kullback–Leibler divergence between the prior and posterior probability distributions of the quantity of interest, demonstrating the methodology on a steel wire manufacturing problemPandita et al. [2019], with follow-up work introducing sequential design strategies based on non-stationary GPs, benchmarked against uncertainty sampling and expected improvementPandita et al. [2021].
For mechanical experiments, Eberle-Blick and HyvönenEberle-Blick and Hyvönen [2024]optimize boundary pressure activations to maximize the informational value of the resulting deformations for reconstructing the material parameters, while others optimize the information content of mechanical experiments — particularly uniaxial tensile tests — for the calibration of different nonlinear constitutive modelsRicciardi et al. [2024]or history-dependent constitutive modelsBhattacharya et al. [2026].
The reader is additionally referred to the general overview of Bayesian experimental design concepts provided byRyan et al. [2015].

## 6.2Bayesian optimization and active learning

In contrast to Bayesian experimental design — which aims to gain information about uncertain model parameters — the core objective of Bayesian optimization is:

Select the next input that is expected to yield the optimal or best objective value, while simultaneously exploring uncertain regions to enhance our overall model understanding.

Thus, Bayesian optimization is fundamentally an optimization method, not a parameter-inference method.

## 6.2.1General concept

The transition from experimental design to optimization is often motivated by necessity. As previously discussed, the marginalization integrals required for full Bayesian experimental design are frequently computationally intractable. To make the problem manageable, the expected utility is often approximated using a MAP estimate.

In this context, we apply two key simplifications to the utility calculation:
- •

Parameter approximation.
Instead of integrating over the full parameter posteriorp​(𝜽∣𝒟)p(\bm{\theta}\mid\mathcal{D}), we approximate it by a delta function at its modep​(𝜽∣𝒟)\displaystyle p(\bm{\theta}\mid\mathcal{D})≈δ​(𝜽−𝜽∗),\displaystyle\approx\delta(\bm{\theta}-\bm{\theta}^{\ast})\;,𝜽∗=arg\displaystyle\bm{\theta}^{\ast}=\argmax𝜽⁡p​(𝜽∣𝒟),\displaystyle\max_{\bm{\theta}}p(\bm{\theta}\mid\mathcal{D})\;,(140)

where𝜽∗\bm{\theta}^{\ast}are the trained surrogate-model parameters.
- •

Data approximation.
Rather than integrating over all possible future outcomes, we approximate the likelihood for a new data by a delta function placed at the surrogate predictionp​(y∗∣𝒟,𝜽∗)≈δ​(y∗−f^​(𝒙;𝜽∗)),p(y_{\ast}\mid\mathcal{D},\bm{\theta}^{\ast})\approx\delta\big(y_{\ast}-\hat{f}(\bm{x};\bm{\theta}^{\ast})\big)\;,(141)

wheref^​(𝒙;𝜽)\hat{f}(\bm{x};\bm{\theta})is the surrogate model trained on the dataset𝒟\mathcal{D}.

Together, these approximations replace the full expected utility (Eq. (136)) by a point estimate𝔼​[U​(y∗,𝒟)]≈U​(f^​(𝒙;𝜽∗),𝒟).\displaystyle\mathbb{E}\big[U(y_{\ast},\mathcal{D})\big]\approx U\big(\hat{f}(\bm{x};\bm{\theta}^{\ast}),\mathcal{D}\big)\;.(142)

and the next input is chosen as𝒙∗\displaystyle\bm{x}^{\ast}=arg⁡max𝒙∗⁡U​(f^​(𝒙∗;𝜽∗),𝒟).\displaystyle=\arg\max_{\bm{x}_{\ast}}{U(\hat{f}(\bm{x}_{\ast};\bm{\theta}^{\ast}),\mathcal{D})}\;.(143)

In these MAP approximations, we no longer marginalize with respect to the surrogate parameters𝜽\bm{\theta}or the possible new observationsy∗y_{\ast}. Instead, we transform the original Bayesian experimental design inference into two simpler optimization tasks:
- •

Inner optimization. Train the surrogate model by finding the best-fitting parameter vector𝜽∗\bm{\theta}^{\ast}to learn how the expensive simulation behaves.
- •

Outer optimization. Use the trained surrogate to select the next input𝒙∗\bm{x}^{\ast}by optimizing the utility functionUU. Note that in Bayesian optimization, this utility function is typically referred to as an acquisition functionα\alpha. This step ultimately determines where the next expensive evaluation should be performed.

This separation of inference (inner optimization) and design (outer optimization) makes the problem computationally feasible, while still retaining a probabilistic interpretation through the surrogate’s predictive uncertainty. It also establishes a conceptual bridge between rigorous Bayesian experimental design and its practical approximations in engineering problems widely used in machine learning and scientific modeling. In the machine learning community, this approximate procedure is widely known as Bayesian optimizationBrochu et al. [2010], Shahriari et al. [2015], Frazier [2018]or, more broadly, active learning. In fact, after these two approximations, relatively littleBayesremains in the strict sense171717In common practice, a GP prior is typically placed onf^\hat{f}within this framework, thereby retaining a notion of uncertainty and probabilistic structure. Although not strictly necessary, GPs are particularly convenient for the inner optimization step: unlike generalized linear models, which may require adding new basis functions as new data are incorporated, a GP preserves its functional form and updates only its posterior when new data are observed..

To carry out the two-stage procedure in practice, we require a surrogate model that can both fit the available data (inner optimization) and provide predictions for evaluating the acquisition function (outer optimization). For a black-box objective functionf:𝒳→ℝf:\mathcal{X}\to\mathbb{R}, a GP surrogate is often usedf^GP∼GP​(μ​(𝒙),k​(𝒙,𝒙′)),\hat{f}_{\rm GP}\sim\mathrm{GP}(\mu(\bm{x}),k(\bm{x},\bm{x}^{\prime}))\;,(144)

as introduced in see Section4.3. Conditioning the GP surrogate model on the observed data𝒟\mathcal{D}yields the posterior mean predictionμ​(𝒙)\mu(\bm{x})and the predictive uncertainty through the posterior varianceσ2​(𝒙)\sigma^{2}(\bm{x}), which provide the data-informed prediction of the surrogate and its associated uncertainty at any new input location. Once the GP posterior mean and variance have been computed, they are plugged directly into the acquisition function.

A typically Bayesian optimization workflow consists of five steps:
- i).

Training the surrogate model on the current dataset𝒟\mathcal{D}.
- ii).

Computing the acquisition functionα​(𝒙;𝒟)\alpha(\bm{x};\mathcal{D}).
- iii).

Selecting the next query point𝒙∗=arg⁡max𝒙∈𝒳⁡α​(𝒙;𝒟)\bm{x}^{\ast}=\arg\max_{\bm{x}\in\mathcal{X}}\alpha(\bm{x};\mathcal{D}).
- iv).

Evaluating the expensive objective at𝒙∗\bm{x}^{\ast}.
- v).

Updating the dataset and repeating.

The practical application of these steps is demonstrated through an illustrative example in Section6.3.

Bayesian optimization enjoys several attractive properties. Importantly, it is known to exhibit global convergence even in non-convex problemsKawaguchi et al. [2015]. Even more importantly, it does not necessitate a fast method to evaluate the gradient of the objective function to solve the optimization problem (Eq. (143)); instead it may (or may not) utilize the gradient of the surrogate.

The literature offers a wide range of acquisition functions, each reflecting a different trade-off between exploration (sampling where uncertainty is high) and exploitation (sampling where improvement is expected). One of the simplest is the upper confidence bound (UCB) criterionUCB​(f^​(𝒙,𝜽∗),𝒟):=μ​(𝒙)+β​σ2​(𝒙),\displaystyle\mathrm{UCB}\big(\hat{f}(\bm{x},\bm{\theta}^{\ast}),\mathcal{D}\big):=\mu(\bm{x})+\beta\sqrt{\sigma^{2}(\bm{x})}\;,(145)

whereβ\betais a user-chosen tuning parameter controlling the exploration–exploitation balance: larger values ofβ\betaemphasize exploration by favoring regions with high predictive uncertainty, while smaller values focus on exploitation of areas with high predicted utility; andμ​(𝒙)\mu(\bm{x})andσ2​(𝒙)\sigma^{2}(\bm{x})denote the posterior mean and variance of the GP (cf. Section4.3).

Beyond UCB, many other acquisition functions have been proposed. The probability of improvement (PI) criterionJones et al. [1998]selects points with the highest probability of exceeding the current best observation, whereas the expected improvement (EI) criterionMočkus [1974], Jones et al. [1998]considers the expected magnitude of that improvement. Information-theoretic approaches include the maximum entropy principleLoredo [2004], which seeks points that maximally reduce global uncertainty, and more refined methods such as predictive entropy search (PES)Hernández-Lobato et al. [2014]and max-value entropy search (MES)Wang and Jegelka [2017], which explicitly target information gain about the global optimum. Recently, variance-based criteria such as the global variance approachPreuss and von Toussaint [2021]and robust Bayesian optimization formulationsHoffer et al. [2023]have gained traction for addressing noisy or stochastic environments. The choice of the acquisition function depends on the application. In mechanics, where experiments and simulations are typically costly and noisy, exploration-oriented approaches (such as UCB or PES) may be advantageous.

Generally, Bayesian optimization is particularly well suited for applications in mechanics and material design, where experiments or simulations are costly. Conveniently, many modern deep-learning frameworks — such asTensorFlow,PyTorch, andJAX— either include or interface directly with Bayesian optimization librariesBalandat et al. [2020]. Moreover, Bayesian optimization can be used to tune the relative weighting of data-loss and physics-loss terms in Eq. (87) or to optimize architectural hyperparameters such as the number of layers or neurons.

Bayesian optimization has been widely adopted across various domains. Typical examples include inverse design of material compositions via alternative acquisition functionsTian et al. [2025], Kansara et al. [2025], Raßloff et al. [2025], Chiappetta et al. [2026]or through evolutionary Monte Carlo samplingVangelatos et al. [2021]. It is also used to infer constitutive parameters for material modelsBorowska et al. [2022], Miranda-Valdez et al. [2025]and tune hyperparameters for NNsSnoek et al. [2012]and PINNsZhong et al. [2026], Zhang et al. [2026]. More recently, researchers have integrated domain-specific physics into the surrogate model itself; for instance, incorporating physics knowledge as basis functions in a semi-parametric GP has been shown to reduce required evaluations when optimizing numerical parameters in constrained muscle activation simulationsHuber et al. [2024].

## 6.3Example: Inverse design for a 3D-printed composite material based on uniaxial extension tests

We consider a 3D-printed soft material composed of a hydrogel matrix reinforced with dispersed discrete polymeric fibers. The printing process allows control of the fiber dispersion via a scalar design parameter𝝃∈Ξ\bm{\xi}\in\Xi. The objective is to determine the value of𝝃=κ\bm{\xi}=\kappasuch that the material attains a prescribed, or optimal, tensile stress valueyexp∗y_{\mathrm{exp}}^{\ast}at a specific strain.

The available experimental dataset consists ofNNinput–output pairs𝒟exp=(κi,yexp,i)i=1N,\mathcal{D}_{\rm exp}=\big(\kappa_{i},y_{\mathrm{exp},i}\big)_{i=1}^{N}\;,(146)

whereyexp,iy_{\mathrm{exp},i}denotes the measured tensile stress at a certain strain corresponding to the design parameterκi\kappa_{i}. Due to the costly manufacturing and testing procedure, onlyN=2N=2initial structures are available.
By assuming that the experimental observations are normally distributed, we can describe them as followsyexp,i=f​(κi)+η,η∼𝒩​(0,σ2),y_{\mathrm{exp},i}=f(\kappa_{i})+\eta\;,\qquad\eta\sim\mathcal{N}(0,\sigma^{2})\;,(147)

whereσ\sigmadenotes the measurement variance in this example.

Given the unknown and potentially nonlinear relationship between the design parameter and the tensile stress, a GP surrogate is employed, offering UQ in the small-data regime.
The latent stress–dispersion mapping is modeled asf​(κ)∼GP​(0,k​(κ,κ′;𝜽)),f(\kappa)\sim\mathrm{GP}\big(0,k(\kappa,\kappa^{\prime};\bm{\theta})\big)\;,(148)

wherek​(κ,κ′;𝜽)k(\kappa,\kappa^{\prime};\bm{\theta})is given in this example by a squared-exponential covariance kernel with hyperparameters𝜽=(σf2,ι,σ)T,\bm{\theta}=(\sigma^{2}_{f},\iota,\sigma)^{\rm T}\;,(149)

representing the prior variance magnitudeσf2\sigma^{2}_{f}, the correlation lengthι\iota, and the varianceσ2\sigma^{2}; see Section4.3.
Instead of estimating𝜽\bm{\theta}via marginal likelihood maximization, a fully Bayesian approach is adopted in which the hyperparameters are treated as random variables with weakly informative priors.

The prior scales are chosen based on the empirical scale of the data. The experimental stresses are standardized to zero mean and unit variance, such that the characteristic signal magnitude is of order one. Accordingly, the GP amplitude and noise parameters are assigned weakly informative priorsσf∼HalfNormal​(1)\sigma_{f}\sim\mathrm{HalfNormal}(1)andσ∼HalfNormal​(0.3)\sigma\sim\mathrm{HalfNormal}(0.3), which cover the plausible range of standardized signal and noise magnitudes while assigning vanishing mass to implausibly large values. The length-scale is modeled asι∼LogNormal​(μι,1)\iota\sim\mathrm{LogNormal}(\mu_{\iota},1), whereμι\mu_{\iota}is chosen such that the prior median corresponds to approximately half of the explored design-parameter range, reflecting smooth stress variations over physically meaningful scales; the resulting prior remains broad enough to let the data determine the precise value.

Given the experimental dataset𝒟exp\mathcal{D}_{\rm exp}, the posterior of the hyperparameters is given byp​(𝜽∣𝒟exp)∝p​(𝒟exp∣𝜽)​p​(𝜽),p(\bm{\theta}\mid\mathcal{D}_{\rm exp})\propto p(\mathcal{D}_{\rm exp}\mid\bm{\theta})p(\bm{\theta})\;,(150)

which is inferred using a MAP estimate181818In practice, hyperparameter posteriors are often multimodal with modes existing at different scales. While the ideal Bayesian approach involves using MCMC samplers to produce a collection of posterior samples, capturing all modes accurately can be difficult and computationally expensive. Consequently, a practical choice is often to use the MAP estimate or related methods such as MLE..

By approximating the hyperparameter posterior with a delta function at its mode𝜽∗\bm{\theta}^{\ast}, for any design parameter in the design spaceΞ\Xi, the predictive distribution simplifies as followsp​(y∗∣κ∗,𝒟exp)\displaystyle p(y_{\ast}\mid\kappa^{\ast},\mathcal{D}_{\rm exp})=∫p​(y∗∣𝒟exp,𝜽)\displaystyle=\int p(y_{\ast}\mid\mathcal{D}_{\rm exp},\bm{\theta})×p​(𝜽∣𝒟exp)​d​𝜽\displaystyle\hphantom{=}\,\,\times p(\bm{\theta}\mid\mathcal{D}_{\rm exp})\,\mathrm{d}\bm{\theta}≈p​(y∗∣𝒟exp,𝜽∗),\displaystyle\approx p(y_{\ast}\mid\mathcal{D}_{\rm exp},\bm{\theta}^{\ast})\;,(151)

effectively eliminating the need for marginalization over𝜽\bm{\theta}. This approximation yields the predictive meanμGP​(κ)\mu_{\rm GP}(\kappa)and predictive varianceσGP2​(κ)\sigma_{\rm GP}^{2}(\kappa)directly from the GP conditioned on the fixed hyperparameters. Consequently, the GP provides both a stress prediction and a formal uncertainty estimate for any admissible design parameter.

The inverse design problem consists of identifying the optimal designκ∗\kappa^{\ast}such thatyexp​(κ∗)≈yexp∗.y_{\mathrm{exp}}(\kappa^{\ast})\approx y_{\mathrm{exp}}^{\ast}\;.(152)

To minimize the number of additional costly experiments, a sequential Bayesian optimization strategy is employed. Bayesian optimization combines the GP surrogate with an acquisition functionα\alphathat determines where to evaluate the next experiment.

An acquisition function, derived from probabilistic considerations, is implemented using the UCB criterion (Eq. (145)). To suit the target-matching task, the criterion is adapted by defining exploitation as the minimization of the distance to a target valuey∗y^{\ast}UCBt​(κ)=−(μGP,t​(κ)−yexp∗)2+β​σGP,t2​(κ),\mathrm{UCB}_{t}(\kappa)=-\bigl(\mu_{{\rm GP},t}(\kappa)-y_{\rm exp}^{\ast}\bigr)^{2}+\beta\sqrt{\sigma_{{\rm GP},t}^{2}(\kappa)}\;,(153)

whereβ>0\beta>0controls the exploration–exploitation trade-off. The first term promotes exploitation by minimizing the squared distance to the prescribed target valuey∗y^{\ast}, while the second term encourages exploration in regions of high predictive uncertainty.
Figure 9:(a) Initial experimental synthetic stress-strain data under uniaxial tension for the virtual 3D-printed composite material. The microstructural representations of selected designs are shown alongside the optimal response predicted using Bayesian optimization. (b) Maximum Cauchy stress at the selected strain level (ε=0.3\varepsilon=0.3) as a function of the design parameter describing fiber dispersion for four Bayesian optimization iterations, illustrating progressive improvement of the Gaussian process (GP) regression models as new data are incorporated; meanwhile, (c–f) present the individual GP regression models for the initial data and iterations, demonstrating the reduction in variance and corresponding predictive uncertainty. (model parameters:β=0.8\beta=0.8,σ=0.35\sigma=0.35)

Step 1: Surrogate model.At iterationtt, the Bayesian GP surrogate is refitted using the current dataset𝒟exp,t\mathcal{D}_{{\rm exp},t}. The hyperparameters𝜽∗\bm{\theta}^{\ast}are determined via a MAP estimate, identifying the most probable model configuration. Using these fixed hyperparameters, the predictive meanμt​(κ)\mu_{t}(\kappa)and predictive varianceσt2​(κ)\sigma_{t}^{2}(\kappa)are evaluated for anyκ∈Ξ\kappa\in\Xiwithout the need for numerical marginalization.


Step 2.The acquisition function is evaluated on a dense uniform discretization of the admissible intervalΞ\Xi, obtained by subdividing the interval into fine equidistant points. For each candidate valueκ\kappaon this grid, the predictive meanμGP,t​(κ)\mu_{{\rm GP},t}(\kappa)and varianceσGP,t​(κ)\sigma_{{\rm GP},t}(\kappa)are computed and used to evaluateUCBt​(ξ)\mathrm{UCB}_{t}(\xi)191919Notably, more advanced global optimization methods can be used to find the maximum of the acquisition function more efficiently, particularly in high-dimensional spaces. Since the GP surrogate is smooth and differentiable, gradient-based optimization can be employed even when gradients of the original experiment or simulation are unavailable..


Step 3.The next candidate design parameter is selected asκt+1=arg⁡maxκ∈Ξ⁡UCBt​(κ).\kappa_{t+1}=\arg\max_{\kappa\in\Xi}\mathrm{UCB}_{t}(\kappa)\;.Accordingly, the next evaluation point is obtained purely deterministically as the maximizer of the acquisition function.


Step 4.At the selected design parameterκt+1\kappa_{t+1}, a new tension experiment is performed to obtainyexp,t+1y_{\mathrm{exp},t+1}. Alternatively, when experimental testing is impractical, a validated high-fidelity computational model capable of reproducing the tensile test may be used to provide the corresponding observation.


Step 5.The dataset is updated as𝒟exp,t+1=𝒟exp,t∪(κt+1,yexp,t+1),\mathcal{D}_{{\rm exp},t+1}=\mathcal{D}_{{\rm exp},t}\cup(\kappa_{t+1},y_{\mathrm{exp},t+1}),after which the GP surrogate is retrained using the augmented dataset, and the Bayesian optimization cycle is repeated from the surrogate update step.

The algorithm terminates once the experimentally validated mismatch becomes sufficiently small, i.e.,|yexp,t+1−yexp∗|/yexp∗≤5%,\left|y_{\mathrm{exp},t+1}-y_{\mathrm{exp}}^{\ast}\right|/y_{\mathrm{exp}}^{\ast}\leq 5\%\;,(154)

or other predefined tolerance criteria are met.

For the present example, we define the target response asyexp∗=19.00​kPay_{\mathrm{exp}}^{\ast}=19.00\,\mathrm{kPa}atε=0.3\varepsilon=0.3. As detailed in Table3and illustrated in Figure9(a), convergence was achieved after four additional Bayesian optimization iterations, resulting in an optimal parameterκ∗=0.162\kappa^{\ast}=0.162and a corresponding response ofyexp​(κ∗)=78.65​kPay_{\mathrm{exp}}(\kappa^{\ast})=78.65\,\mathrm{kPa}.
Figures9(b–d) display the experimental data alongside the evolving GP surrogate. These plots highlight the newly sampled data points and the resulting updates to the GP mean and predictive variance throughout the optimization process.Table 3:Initial experimental datasets (N=2N=2) and iterations of the Bayesian optimization.Experiment no.ξ\xiyexpy_{\mathrm{exp}}[kPa]Iterations10.060226.9820.22043.7530.30018.44140.17171.70250.16576.76360.16278.654

## 7Bayesian sensitivity analysis

A natural extension of uncertainty propagation is sensitivity analysis, for which the connection can be summarized as:

A systematic decomposition of output variance into contributions attributable to each input parameter, providing a measure of their relative influence and informing model reduction, calibration, and experimental design.

## 7.1General concept

Mathematically, (variance-based) sensitivity analysisSaltelli et al. [2008]and UQ are closely related: They share the same probabilistic formulations, but their primary objectives differ. Consider a deterministic forward modely=f​(𝒙)y=f(\bm{x})with input parameter vector𝒙\bm{x}treated as a random variable distributed according to a joint probability densityp​(𝒙)p(\bm{x}). UQ focuses on describing how uncertainty in the inputs propagates through the model to produce uncertainty in the output, as in Eqs. (14) and (19). In contrast, variance-based sensitivity analysis quantifies how much each individual inputxix_{i}contributes to the total output variance. In other words, it studies a specific family of functionals of the (conditional) output distribution — conditional variances and variances of conditional expectations — defined asvarxi​[𝔼𝒙¬i​[f​(𝒙)∣xi]],\displaystyle\mathrm{var}_{x_{i}}\left[\mathbb{E}_{\bm{x}_{\lnot i}}\left[f(\bm{x})\mid x_{i}\right]\right]\;,(155)

where𝒙¬i\bm{x}_{\lnot i}denotes the collection of all input variables exceptxix_{i}. Here, we extend the notation for𝔼​[⋅]\mathbb{E}[\cdot]andvar​[⋅]\mathrm{var}[\cdot]introduced in Section3: The subscript indicates the marginalized variables, while the vertical bar indicates the conditional variables. More precisely, the conditional expectation is𝔼𝒙¬i​[f​(𝒙)∣xi]\displaystyle\mathbb{E}_{\bm{x}_{\lnot i}}\big[f(\bm{x})\mid x_{i}\big]=∫f​(𝒙)​p​(𝒙¬i∣xi)​d𝒙¬i\displaystyle=\int f(\bm{x})p({\bm{x}}_{\lnot i}\mid x_{i})\>\mathrm{d}{\bm{x}}_{\lnot i}≕h​(xi).\displaystyle\eqcolon h(x_{i})\;.(156)

wherep​(𝒙¬i∣xi)p(\bm{x}_{\lnot i}\mid x_{i})reads as the conditional density of the remaining variables givenxix_{i}and the notationd​𝒙¬i\mathrm{d}{\bm{x}}_{\lnot i}indicates marginalization over all parameters exceptxix_{i}. That means, we keep the variablexix_{i}fixed and integrate out the influence of all remaining parameters. This operation effectively averages the model output over the uncertainty in all inputs other thanxix_{i}, producing a conditional mean responseh​(xi)h(x_{i})that depends solely on that parameter. In simple terms, this measures how much variation in the single parameterxix_{i}influences the average model output when the effects of all other parameters are averaged out.

The corresponding variance of the conditional mean response isvarxi​[h​(xi)]\displaystyle\mathrm{var}_{x_{i}}\left[h(x_{i})\right]=∫(h​(xi)−𝔼xi​[h​(xi)])2\displaystyle=\int\big(h(x_{i})-\mathbb{E}_{x_{i}}[h(x_{i})]\big)^{2}×p​(xi)​d​xi,\displaystyle\hphantom{=}\,\,\times p(x_{i})\>\mathrm{d}x_{i}\;,(157)

wherep​(xi)p(x_{i})is the marginal probability density of input variablexix_{i}. The expectation appearing in the expression is𝔼xi​[h​(xi)]=∫h​(xi)​p​(xi)​dxi.\displaystyle\mathbb{E}_{x_{i}}\big[h(x_{i})\big]=\int h(x_{i})p(x_{i})\>\mathrm{d}x_{i}\;.(158)

These variances of conditional expectations quantify how much the expected model response changes as a single parameterxix_{i}varies, after averaging out the influence of all remaining inputs. In variance-based sensitivity analysisMelito et al. [2026], this quantity plays a central role: it represents the contribution of parameterxix_{i}to the overall uncertainty in the model output. To compare this contribution across parameters, it is normalized by the total output variance, which leads directly to the definition of the first-order Sobol’ sensitivity indices.

From these variances of conditional expectations, we define the first-order Sobol’ sensitivity indicesSobol’ [1990]asSi=varxi​[𝔼𝒙¬i​[f​(𝒙)∣xi]]var​[f​(𝒙)],S_{i}=\frac{\mathrm{var}_{x_{i}}\left[\mathbb{E}_{\bm{x}_{\lnot i}}\big[f(\bm{x})\mid x_{i}\big]\right]}{\mathrm{var}\left[f(\bm{x})\right]}\;,(159)

which quantify the fraction of the total output variance that can be attributed to input parameterxix_{i}. These quantities — equivalently, the integral appearing in Eq. (155) — can be estimated either by direct Monte Carlo sampling of the simulation model or, more efficiently, by using a surrogate model (cf. Section3.3).

A key reason for the popularity of PCEs (cf. Section4.2) is that, under the assumption of independent input parameters, both the total output variance and the first-order partial variances can be written directly in terms of the PCE coefficients. In particular,var​[f​(𝒙)]=∑𝜶∈𝒜c𝜶2−c02,varxi​[h​(xi)]=∑𝜶∈𝒜ic𝜶2−c02,\displaystyle\begin{split}\mathrm{var}\left[f({\bm{x}})\right]&=\sum_{\bm{\alpha}\in\mathcal{A}}c^{2}_{\bm{\alpha}}-c_{0}^{2}\;,\\
\mathrm{var}_{x_{i}}\left[h(x_{i})\right]&=\sum_{\bm{\alpha}\in\mathcal{A}_{i}}c^{2}_{\bm{\alpha}}-c_{0}^{2}\;,\end{split}(160)

where𝒜={𝜶}\mathcal{A}=\{\bm{\alpha}\}is the set of all multi-indices associated with the polynomial basis functions in the PCE. The coefficientc0=𝔼​[f​(𝒙)]c_{0}=\mathbb{E}[f({\bm{x}})]corresponds to the constant basis function, the polynomial of order zero. The subset𝒜i={𝜶:αi=0}\mathcal{A}_{i}=\{\bm{\alpha}:\alpha_{i}=0\}contains the multi-indices of basis functions that have degree zero in the variablexix_{i}. These coefficients determine how each basis function contributes to the total variance of the model output and how much of that variance is caused by variations in the parameterxix_{i}. Importantly, that contribution is a function of not only (i) the dependency offfonxix_{i}, but also of (ii) the distribution ofxix_{i}, in particular also the domain on which it is supported, and (iii) the value of (ii) in relation to (i).

The analytical expressions above are, however, a unique advantage of PCEs. For other surrogate models, such as GPs or PINNs, evaluating Sobol’ indices generally requires additional Monte Carlo integration or numerical quadrature, making the computation significantly more expensive. This efficiency is exacerbated for higher-order Sobol’ indices, such as second-order interactions,Si​j∝varxi,xj​[𝔼𝒙¬i,¬j​[f​(𝒙)∣xi,xj]],S_{ij}\propto\mathrm{var}_{x_{i},x_{j}}\left[\mathbb{E}_{\bm{x}_{\lnot i,\lnot j}}\big[f(\bm{x})\mid x_{i},x_{j}\big]\right]\;,(161)

which quantify the joint influence of parametersxix_{i}andxjx_{j}. Since the number of Sobol’ indices grows combinatorially with the number of input parameters, brute-force Monte Carlo estimation of all the indices (Eq. (159)) quickly becomes infeasible, even more so when non-PCE surrogate models are used.

Nevertheless, the interpretability of these sensitivity indices is inherently limited, since they are based solely on the variance. The variance contains no information about (a)symmetry or the tails of the underlying probability distribution and therefore provides a complete picture only if the distribution is GaussianWollner et al. [2026].
Furthermore, the interpretation of the Sobol’ indices is more delicate for correlated input variables.
Consequently, these variance-based estimates should be interpreted with caution in practice. For a more detailed discussion of sensitivity analysis and Sobol’ indices, including total effect indices and generalizations to dependent inputs, we refer the reader to related literatureMelito et al. [2026].

From a Bayesian viewpoint, however, a fully probabilistic version of sensitivity analysis would also marginalize over the uncertainty in the surrogate model parameters. For instance, placing a GP prior on the surrogate modelOakley and O’Hagan [2004]allows one to propagate parameter uncertainty through the sensitivity indices themselves.

## 7.2Bayesian generalization

The termBayesian sensitivity analysisis not yet universally defined or established. However, Bayesian theory provides a broader framework. In Eqs. (155) to (161), no surrogate model is introduced, except in Eq. (160). The key distinction between Bayesian and vanilla sensitivity analysis lies in the incorporation of priors and the marginalization of hyperparameters. This difference becomes particularly explicit in surrogate-based sensitivity analysis.

Let the surrogate parameters be denoted by𝜽{\bm{\theta}}. In Eqs. (155) to (161), their role was left implicit. In Eq. (160), for example, we effectively assumed that the PCE coefficients𝜽=(c𝜶)T{\bm{\theta}}=(c_{\bm{\alpha}})^{\rm T}are known exactly. That is, the variance off​(𝒙)f({\bm{x}})was conditioned on fixed PCE coefficients. Consequently, the Sobol’ indices (Eqs. (159) and (161)) are likewise conditioned on fixed𝜽{\bm{\theta}}. To state this explicitly, Eqs. (7.1) and (7.1) should be written as𝔼𝒙¬i​[f​(𝒙)∣xi]\displaystyle\mathbb{E}_{\bm{x}_{\lnot i}}\big[f(\bm{x})\mid x_{i}\big]≡𝔼𝒙¬i​[f​(𝒙)∣xi,𝜽]\displaystyle\equiv\mathbb{E}_{\bm{x}_{\lnot i}}\big[f(\bm{x})\mid x_{i},{\bm{\theta}}\big]=∫f​(𝒙)​p​(𝒙¬i∣xi,𝜽)​d𝒙¬i\displaystyle=\int f(\bm{x})p({\bm{x}}_{\lnot i}\mid x_{i},{\bm{\theta}})\>\mathrm{d}{\bm{x}}_{\lnot i}=:h(xi).\displaystyle=:h(x_{i})\;.(162)

andvarxi​[h​(xi)]\displaystyle\mathrm{var}_{x_{i}}\left[h(x_{i})\right]≡varxi​[h​(xi)∣𝜽]\displaystyle\equiv\mathrm{var}_{x_{i}}\left[h(x_{i})\mid{\bm{\theta}}\right]=∫(h​(xi)−𝔼​[h​(xi)])2\displaystyle=\int\big(h(x_{i})-\mathbb{E}[h(x_{i})]\big)^{2}×p​(xi∣𝜽)​d​xi,\displaystyle\hphantom{=}\,\,\times p(x_{i}\mid{\bm{\theta}})\>\mathrm{d}x_{i}\;,(163)

where all expectations and variances are now explicitly conditioned on fixed surrogate parameters𝜽{\bm{\theta}}.

However, as shown in Sections4.2and5.4, the PCE coefficients are generally not known exactly but must be treated as uncertain random variables.
A fully Bayesian surrogate-based sensitivity analysis therefore assigns a prior to𝜽{\bm{\theta}}and marginalizes all quantities of interest with respect to it. This marginalization can be performed directly at the level of the Sobol’ indices in Eq. (159), leading to the Bayesian estimator𝔼𝜽​[Si]=∫Si​p​(𝜽)​d𝜽.\displaystyle\mathbb{E}_{{\bm{\theta}}}[S_{i}]=\int S_{i}p({\bm{\theta}})\>\mathrm{d}{\bm{\theta}}\;.(164)

The definition in Eq. (164) can be impractical due to the fraction in Eq. (159) appearing inside the integral. A more tractable approach marginalizes the surrogate parameters𝜽{\bm{\theta}}in the expectations and variances instead. From Eq. (159), this leads to the generalized Bayesian Sobol’ indexSiBayes:=∫varxi​[𝔼𝒙¬i​[f​(𝒙)∣xi]]​p​(𝜽)​d𝜽∫var​[f​(𝒙)]​p​(𝜽)​d𝜽,\displaystyle S^{\rm Bayes}_{i}:=\frac{\int\mathrm{var}_{x_{i}}\left[\mathbb{E}_{\bm{x}_{\lnot i}}\big[f(\bm{x})\mid x_{i}\big]\right]p({\bm{\theta}})\>\mathrm{d}{\bm{\theta}}}{\int\mathrm{var}\left[f(\bm{x})\right]p({\bm{\theta}})\>\mathrm{d}{\bm{\theta}}}\;,(165)

where the integrands are understood to be conditioned on𝜽{\bm{\theta}}, as in Eqs. (7.2) and (7.2).
Importantly, the definitions in Eqs. (164) and (165) are not equivalent and may yield different results in general.
Of these, the later definition is often preferred due to its favorable properties. For instance, in the case of a PCE surrogate with Gaussian likelihood and a flat prior on the coefficients, marginalization amounts to replacing fixed coefficient values in Eq. (160) by their posterior expectations, i.e.,var​[f​(𝒙)∣𝜽]=∑𝜶∈𝒜c𝜶2−c02→Bayesvar​[f​(𝒙)]=∑𝜶∈𝒜𝔼𝜽​[c𝜶2]−𝔼𝜽​[c02].\displaystyle\begin{split}\mathrm{var}\left[f({\bm{x}})\mid{\bm{\theta}}\right]&=\sum_{\bm{\alpha}\in\mathcal{A}}c^{2}_{\bm{\alpha}}-c_{0}^{2}\\
{\xrightarrow{\rm Bayes}}\quad\mathrm{var}\left[f({\bm{x}})\right]&=\sum_{\bm{\alpha}\in\mathcal{A}}\mathbb{E}_{{\bm{\theta}}}[c^{2}_{\bm{\alpha}}]-\mathbb{E}_{{\bm{\theta}}}[c_{0}^{2}]\;.\end{split}(166)

Analogous replacements apply to the variances of the conditional expectations in Eq. (160). On the left-hand side, the conditioning on𝜽{\bm{\theta}}— implicit in Eq. (160) — is made explicit; on the right-hand side, the coefficients are marginalized. For this setting, both the posterior expectations and uncertainty estimates of the PCE coefficients — and thus the Bayesian Sobol’ indices in Eq. (165) — admit closed-form expressions; seeRanftl and von der Linden [2021]for details.

The advantage of this Bayesian formulation is that meaningful sensitivity analysis can be performed even when the surrogate is notsufficientlyaccurate. In particular, uncertainty estimates for the Sobol’ indices can be derived that explicitly account for surrogate inaccuracy through the posterior of the surrogate parameters,p​(𝜽∣𝒟)p({\bm{\theta}}\mid\mathcal{D}). Rather than conditioning on a single fixed estimate of𝜽{\bm{\theta}}, the Sobol’ indices are obtained by marginalizing over this posterior. In this way, uncertainty in the surrogate parameters is systematically propagated into the sensitivity measures. As a result, the sensitivity analysis becomes quantitatively defensible, even when the surrogate’s accuracy is uncertain.

Finally, employing a GP surrogate instead of, for example, a PCE surrogate does not in itself constitute a fully Bayesian sensitivity analysis, contrary to suggestionsBecker et al. [2011], Melis et al. [2017]. A fully Bayesian treatment would also require marginalization over the GP kernel hyperparameters. In practice, however, these are typically approximated by maximum likelihood point estimates (cf. Section4.3). Moreover, GP-based sensitivity analysis generally relies on numerical integration, since the simple analytical expressions available for PCEs in Eqs. (160) and (166) do not apply.

## 8Random fields for constitutive uncertainty

The core objective of random field modeling can be formulated as:

Representation of spatially or temporally varying material or model parameters as stochastic priors that encode spatial correlation, uncertainty, and prior knowledge across the domain.

## 8.1General concept and Gaussian random fields

Random fieldsVanmarcke [2010]provide a useful framework for modeling spatially distributed uncertainties in material properties, particularly for inherently heterogeneous materials such as biological tissue. In this section, we establish that random fields, in this sense and for this purpose, can be understood as a particular and sophisticated form of prior,p​(𝒙)≡p​(𝒙∣𝐗)p(\bm{x})\equiv p(\bm{x}\mid\mathbf{X}), within the general UQ framework introduced in Eq. (14), i.e., the distribution of the parameters𝒙{\bm{x}}is now conditioned on spatial coordinates𝐗\mathbf{X}.

Colloquially, a random field generalizes the concept of a random variable to field quantities, thereby defining a random variable at every point in a spatial domain, with a prescribed correlation between every pair of points within this domain. For example, the GPs introduced in Section4.3can be regarded as a special case ofGaussianrandom fields in parameter space.

In the context of constitutive modeling, a random field assigns a random variable to each point𝐗∈Ω0\mathbf{X}\in\Omega_{0}in the reference domain. In this sense, we merely reinterpret GPs from a different perspective. In surrogate modeling and machine learning (cf. Section4.3), GPs were employed for regression — that is, to learn an unknown function from data. Here, by contrast, we use GPs for stochastic modeling and to generate samples (realizations) from the modeled probability distribution.

This perspective highlights two key differences relative to Section4.3. First, we now assign a random variable to every point in thespatial domain, whereas in surrogate modeling, a random variable was assigned to each point inparameter space. Second, our goal here is to sample from the distribution, rather than to infer or learn its parameters in the distribution.

Letggbe the variable we aim to model as a random field. A widely used prior model is the Gaussian random field, denoted asg∼GP​(μ​(𝐗),k​(𝐗,𝐗′)),g\sim\mathrm{GP}(\mu(\mathbf{X}),k(\mathbf{X},\mathbf{X}^{\prime}))\;,(167)

or, formally equally,g∣𝐗,μ,k∼𝒩​(μ​(𝐗),k​(𝐗,𝐗′)),g\mid\mathbf{X},\mu,k\sim\mathcal{N}(\mu(\mathbf{X}),k(\mathbf{X},\mathbf{X}^{\prime}))\;,(168)

with mean functionμ​(𝐗)\mu(\mathbf{X})and covariance functionk​(𝐗,𝐗′)k(\mathbf{X},\mathbf{X}^{\prime}), which defines the spatial correlation. Note thatμ\muandkkusually depend on hyperparameters just like in the regression setting in Section4.3, however we omit them in the notation here since the hyperparameters are a matter ofa priorichoice and usually fixed. Forkk, we may again choose, for example, the squared-exponential kernel introduced in Eq. (70). To generate a realization (or sample) from this prior, we evaluate the fieldg=𝒢​(𝐗¯)g=\mathcal{G}(\underline{\mathbf{X}})on a discretized spatial grid𝐗¯=(𝐗(1),…,𝐗(NX))T\underline{\mathbf{X}}=(\mathbf{X}^{(1)},\dots,\mathbf{X}^{(N_{\mathrm{X}})})^{\rm T}ofNXN_{\mathrm{X}}nodes. The resulting vectorggis jointly Gaussian distributed with covariance matrixg∼𝒩​(0,K),[K]i​j=k​(𝐗(i),𝐗(j)).g\sim\mathcal{N}(0,K)\;,\quad[K]_{ij}=k(\mathbf{X}^{(i)},\mathbf{X}^{(j)})\;.(169)

Identifyingg≔𝒙g\coloneqq{\bm{x}}, this construction defines a prior for our physical parameters𝒙{\bm{x}}at locations𝐗\mathbf{X},𝒙∣𝐗∼𝒩​(0,K){\bm{x}}\mid\mathbf{X}\sim\mathcal{N}(0,K), for uncertain input parameters in a general UQ problem, as discussed in Section3.1.
In order to evaluate the UQ formulations in Eqs. (14) and (19), we therefore must be able to sample random-field realizations fromp​(𝒙∣𝐗)p({\bm{x}}\mid\mathbf{X}). Since𝒙{\bm{x}}now is a random field, we often, but not necessarily, find thatyyis also a random field. For example, the Cauchy stress would be a random field, while its spatial average would be a simple scalar random variable.

In the following, we outline how such realizations can be generated for𝒙{\bm{x}}for Gaussian and non-Gaussian random fields. We may use these realizations then to generate samples ofyyin order to obtain Monte Carlo estimates for the UQ equations (Eq. (19)), which are then given byy​(𝒙)y({\bm{x}})ory^​(𝒙)\hat{y}({\bm{x}}), depending on whether we can evaluate the desired number of samples with the original simulationyyor need a surrogatey^\hat{y}instead.

We highlight a few representative examples in biomechanics. Gaussian random fields have been adopted, for instance by Bosnjak et al.Bošnjak et al. [2025], who perturbed patient-specific aortic geometries through displacement maps derived from Gaussian fields to quantify boundary uncertainty. Hauseux et al.Hauseux et al. [2018]modeled spatial variability in anisotropic brain tissue properties using correlated Gaussian fluctuation. Tran et al.Tran et al. [2019]represented spatial variations in the arterial stiffness of coronary artery bypass grafts via Gaussian field approximations.
In engineering fracture mechanics, Gaussian random fields have been applied to model spatial variability in phase-field simulations, including: critical energy release rate distributionsHe et al. [2025], random pore configurations in porous materialsSu et al. [2023], and spatially varying failure strength and fracture toughness in quasi-brittle materialsHai and Li [2022]. Beyond phase-field simulations, Gaussian Markov random fields have been applied to reconstruct spatially varying fields such as porosity in large-scale finite element simulations on three-dimensional domainsNitzler et al. [2026b]. Additionally, researchers have extracted Gaussian random field hyperparameters from scanning electron microscope images of fiber distributions in reinforced composite plates to perform finite element-based microscopic fracture analysis, thereby estimating local apparent strength while considering random microstructure morphologiesStefanou et al. [2022], Sakata et al. [2026]

Beyond Gaussian fields, non-Gaussian random fields have been introduced to capture more complex or bounded spatial variability, such as beta-distributed fields modeling elastic fiber degradation in the pathological aortic wallRanftl et al. [2022], spatially dependent fiber-orientation distributions required for anisotropic constitutive models of the aortic wall in patient-specific simulationsStaber and Guilleminot [2018], or heterogeneous isotropic material parameters in abdominal aortic aneurysm modelsBiehler et al. [2015]. Two such representative examples are illustrated in Fig.10.

## 8.2Sampling random field realizations

There are multitude of ways to draw samplesg(s)g^{(s)}. These realizations serve as spatially correlated uncertain model inputs, such as spatially inhomogenous parameters in a constitutive model. Here, we introduce three commonly used strategies: the Cholesky decomposition, spectral methods, and the Karhunen–Loève expansion.

## 8.2.1Cholesky decomposition

To sample a finite-dimensional realization from a GP prior, we make use of the fact that the GP marginal at a set of input points𝐗¯\underline{\mathbf{X}}follows a multivariate normal distribution. By definition of a GP, this can be written as𝒈∼𝒩​(𝝁,K),𝝁(i)=μ​(𝐗(i)),\displaystyle\bm{g}\sim\mathcal{N}(\bm{\mu},K)\;,\quad\bm{\mu}^{(i)}=\mu(\mathbf{X}^{(i)})\;,[K]i​j=k​(𝐗(i),𝐗(j)).\displaystyle\quad[K]_{ij}=k(\mathbf{X}^{(i)},\mathbf{X}^{(j)})\;.(170)

whereμ\muis the mean vector andKKis the covariance matrix describing spatial correlations between all points.

To sample from this distribution, we use the Cholesky decomposition of the covariance matrix. LetL∈ℝN×NL\in\mathbb{R}^{N\times N}denote the lower-triangular matrix obtained fromK=L​LT,K=LL^{\rm T}\;,(171)

whereKKis positive definite by construction.
The sampling procedure then consists of two simple steps
- i).

Draw a standard i.i.d. normal random vector𝜻(s){\bm{\zeta}}^{(s)}from𝜻∼𝒩​(𝟎,IN){\bm{\zeta}}\sim\mathcal{N}(\mathbf{0},I_{N}), whereINI_{N}is theN×NN\times Nidentity matrix.
- ii).

Transform this sample using𝒈(s)=𝝁+L​𝜻(s)\bm{g}^{(s)}=\bm{\mu}+L{\bm{\zeta}}^{(s)}.

This transformation produces a sample𝒈(s)\bm{g}^{(s)}from𝒩​(𝝁,K)\mathcal{N}(\bm{\mu},K)that has the desired mean and covariance. Indeed, we can easily check that𝔼​[𝒈]=𝝁+L​𝔼​[𝜻]=𝝁,\displaystyle\mathbb{E}\big[\bm{g}\big]=\bm{\mu}+L\,\mathbb{E}\big[{\bm{\zeta}}\big]=\bm{\mu}\;,(172)

andcov​[𝒈]\displaystyle\mathrm{cov}[\bm{g}]=𝔼​[(L​𝜻)​(L​𝜻)T]=L​𝔼​[𝜻​𝜻T]​LT\displaystyle=\mathbb{E}\big[(L{\bm{\zeta}})(L{\bm{\zeta}})^{\rm T}\big]=L\mathbb{E}\big[{\bm{\zeta}}{\bm{\zeta}}^{\rm T}\big]L^{\rm T}=L​IN​LT=L​LT=K.\displaystyle=LI_{N}L^{\rm T}=LL^{\rm T}=K\;.(173)

Since𝒈\bm{g}has mean𝝁\bm{\mu}and covarianceKK, and linear transformations of Gaussian variables remain Gaussian,𝒈(s)\bm{g}^{(s)}is a valid sample from the GP marginal𝒩​(𝝁,K)\mathcal{N}(\bm{\mu},K).

Note that we would arrive at the same result if we used the square root of the inverse covariance matrix,K−1/2K^{-1/2}, instead ofLL. In other words, we could also use a singular value decomposition instead of a Cholesky decomposition of the covariance for the purposes of generating samples from the distribution defined by that covariance. However, this approach has an important limitation.

The computational cost of the Cholesky factorization, and of general matrix inversions, scales as𝒪​(Nx3)\mathcal{O}(N_{x}^{3}), whereNxN_{x}is the number of collocation points, i.e., the number of spatial nodes in the finite element or finite volume discretization where the random field is evaluated. The same limitation appears in GP regression in the machine learning setting (Section4.3), where the scaling depends on the number of data points rather than the number of spatial nodes.
As a consequence, sampling random-field realizations over large or finely discretized domains becomes computationally expensive. This bottleneck is especially pronounced in biomechanics, where finely discretized spatial domains or three-dimensional patient-specific computational models often involve thousands or millions of degrees of freedom. In the next section, we introduce an alternative sampling method that achieves a more favorable computational scaling.

## 8.2.2Spectral methods (Shinozuka’s method)

Spectral methods, and in particular Shinozuka’s methodShinozuka and Deodatis [1991,1996], offer an efficient alternative for simulatingstationaryGaussian random fields without explicitly forming or factorizing the covariance matrix.

Shinozuka’s method is based on representing a stationary GP in the frequency domain, where the covariance structure can be expressed through its power spectral density. A random fieldg​(𝐗)g(\mathbf{X})is calledstationarywhen its covariance depends only on the relative distance𝒓:=𝐗−𝐗′{\bm{r}}:=\mathbf{X}-\mathbf{X}^{\prime}between two points rather than their absolute positionsk​(𝐗,𝐗′)=k​(𝐗−𝐗′)=k​(𝒓).k(\mathbf{X},\mathbf{X}^{\prime})=k(\mathbf{X}-\mathbf{X}^{\prime})=k({\bm{r}})\;.(174)

For zero-mean stationary GPg​(𝐗)g(\mathbf{X})with covariance functionk​(𝐫)=𝔼​[g​(𝐗)​g​(𝐗+𝐫)],k(\mathbf{r})=\mathbb{E}\big[g(\mathbf{X})g(\mathbf{X}+\mathbf{r})\big]\;,(175)

the corresponding power spectral densityS​(𝝎)S(\bm{\omega})is given by the Fourier transform ofkk, i.e.,S​(𝝎)=∫ℝDk​(𝐫)​e−i​𝝎⋅𝐫​d𝐫.S(\bm{\omega})=\int_{\mathbb{R}^{D}}k(\mathbf{r})e^{-i\bm{\omega}\cdot\mathbf{r}}\>\mathrm{d}\mathbf{r}\;.(176)

The power spectral density quantifies how the total variance of the random field is distributed across spatial frequencies, analogous to how an energy spectrum describes the contribution of different modes to a physical signal.

To construct a sample realization ofg​(𝐗)g(\mathbf{X})over a spatial domain, Shinozuka’s method discretizes the frequency space into a finite set of wavevectors(𝝎p)p=1P(\bm{\omega}_{p})_{p=1}^{P}. Each wavevector𝝎p\bm{\omega}_{p}defines a plane wave with a specific direction and spatial frequency: its magnitude‖𝝎p‖=2​π/λp||\bm{\omega}_{p}||=2\pi/\lambda_{p}corresponds to the wavelengthλp\lambda_{p}, and its orientation determines the direction of spatial oscillation.
For instance, in one dimension with a uniform grid, we could discretize asωp=p​Δ​ω\omega_{p}=p\Delta\omegawithΔ​ω=ωmax/P\Delta\omega=\omega_{\rm max}/P.

For each frequency component, a random phaseϑp∼Uniform​[0,2​π)\vartheta_{p}\sim\mathrm{Uniform}[0,2\pi)(177)

is independently drawn to introduce randomness while preserving the desired second-order statistics. Each component is then assigned an amplitude with volume weightsΔ​𝝎p\Delta\bm{\omega}_{p}, and the field is reconstructed as a weighted sum of cosine wavesg​(𝐗)≈∑p=1P2​S​(𝝎p)​Δ​𝝎p​cos⁡(𝝎p⋅𝐗+ϑp),g(\mathbf{X})\approx\sum_{p=1}^{P}\sqrt{2S(\bm{\omega}_{p})\Delta\bm{\omega}_{p}}\cos(\bm{\omega}_{p}\cdot\mathbf{X}+\vartheta_{p})\;,(178)

i.e., a discrete (Riemann-)approximation to the inverse Fourier transform.
This harmonic superposition, where the discretizations of the spatial and frequency domains need not necessarily coincide, produces a spatially correlated random field whose covariance matches the targetk​(𝐫)k(\mathbf{r})in the limit of fine frequency discretization, which can be shown, for example, via the central limit theorem.

Shinozuka’s spectral method offers several appealing advantages over direct covariance-based approaches. It is computationally efficient, since it bypasses the need to assemble and factorize large covariance matrices, leading to significant savings in both time and memory. The approach also scales better to higher dimensions and finely discretized domains, especially when implemented using fast Fourier transform techniques on regular grids. Furthermore, the spectral representation provides an intuitive interpretation of spatial variability in terms of underlying frequency content, enabling direct control over the correlation structure through the power spectral density.

Owing to these properties, Shinozuka’s method has become a practical choice for generating large-scale realizations of stationary random fields, where it facilitates efficient modeling of spatial heterogeneity in material properties, tissue structure, or loading conditions. Alas, Shinozuka’s method assumes stationarity. For non-stationary fields, usually more sophisticated, and often less scalable, methods are necessary, one of which we will discuss next.

## 8.2.3Karhunen-Loève expansion

The Karhunen–Loève expansionGhanem and Spanos [1991], Xiu [2010], Le Maître and Knio [2010]— a representation for random fields closely related to Shinozuka’s method — offers a mathematically elegant and physically interpretable decomposition of a random field in terms of deterministic spatial modes and random coefficients.
It provides an eigen-spectral representation of any second-order random field (i.e., one with finite variance) whose covariance function is known202020Specifying the covariance function is a major practical limitation in, for example, biomechanics. Empirical estimation of spatial correlations is often restricted by limited sample sizes and the high degree of inter-subject variability inherent in biological tissues..

Letg​(𝐗)g(\mathbf{X})be a zero-mean, square-integrable random field defined over a (spatial) domainΩ0⊂ℝD\Omega_{0}\subset\mathbb{R}^{D}, with covariance functionk​(𝐗,𝐗′)=𝔼​[g​(𝐗)​g​(𝐗′)].k(\mathbf{X},\mathbf{X}^{\prime})=\mathbb{E}\big[g(\mathbf{X})g(\mathbf{X}^{\prime})\big]\;.(179)

Under suitable regularity conditions onkk, the field can be expressedexactlyas an infinite seriesg​(𝐗)=∑p=1∞λp​ζp​ϕp​(𝐗),g(\mathbf{X})=\sum_{p=1}^{\infty}\sqrt{\lambda_{p}}\,\zeta_{p}\,\phi_{p}(\mathbf{X})\;,(180)

whereζp\zeta_{p}are i.i.d. standard normal random variables,ζp∼𝒩​(0,1)\zeta_{p}\sim\mathcal{N}(0,1), and(λp,ϕp​(𝐗))(\lambda_{p},\phi_{p}(\mathbf{X}))are the eigenvalue–eigenfunction pairs of the generalized eigenvalue problem given by the integral equation∫Ω0k​(𝐗,𝐗′)​ϕp​(𝐗′)​d𝐗′=λp​ϕp​(𝐗).\int_{\Omega_{0}}k(\mathbf{X},\mathbf{X}^{\prime})\phi_{p}(\mathbf{X}^{\prime})\>\mathrm{d}\mathbf{X}^{\prime}=\lambda_{p}\phi_{p}(\mathbf{X})\;.(181)

Each term in the Karhunen-Loève expansion represents a spatial modeϕp​(𝐗)\phi_{p}(\mathbf{X})modulated by a random coefficientλp​ξp\sqrt{\lambda_{p}}\xi_{p}. The eigenvalueλp\lambda_{p}quantify the mean contribution, or meanenergy, of each mode to the total field variance, meaning that modes associated with small eigenvalues contribute little to the overall variability. We notice that through Eq. (181), the expansion in general depends on the domainΩ0\Omega_{0}.

In practice, the series is truncated after a finite number of termsPP, yielding the approximationg​(𝐗)≈∑p=1Pλp​ξp​ϕp​(𝐗),g(\mathbf{X})\approx\sum_{p=1}^{P}\sqrt{\lambda_{p}}\xi_{p}\phi_{p}(\mathbf{X})\;,(182)

wherePPis chosen so that the cumulative energy of the retained modes captures a desired proportion of the total variance. Owing to the orthonormality of the eigenfunctions, the variance of the truncated expansion is given by the sum of the retained eigenvalues. Consequently, the relative variance represented by the firstPPmodes readsvar​[g]∝∑p=1Pλp∑p=1∞λp≈1.\mathrm{var}[g]\propto\frac{\sum_{p=1}^{P}\lambda_{p}}{\sum_{p=1}^{\infty}\lambda_{p}}\approx 1\;.(183)

This truncation provides a compact, low-dimensional representation of the stochastic field, useful for UQ.

Shinozuka’s method can be interpreted as a special case of the Karhunen–Loève expansion formulated in the Fourier domain and truncated to a finite number of Fourier modes. This enables efficient computation but restricts the method to stationary covariance functions and infinite or periodic domains. In contrast, the Karhunen–Loève expansion requires the solution of the eigenvalue problem in Eq. (181). Although computationally more demanding, it permits the modeling of more general and spatially complex random fields.

There is also a structural similarity between the Karhunen–Loève expansion and PCE (cf. Section4.2). However, their purposes differ fundamentally. In Section4.3, PCE was used to learn an approximationy^​(𝒙)\hat{y}({\bm{x}})from data, similar in spirit to GPs in machine learning. Here, in contrast, the expansion is employed togeneratesamples fromp​(𝒙∣𝐗)p({\bm{x}}\mid\mathbf{X}). Furthermore, although both approaches constitute orthogonal decompositions (typically in a Hilbert space), they differ in their objectives, underlying assumptions, and construction.

Furthermore, the Karhunen-Loève expansion is conceptually related to the representer theorem (cf. Eq. (75)) and Mercer’s theorem, shown below, which also connect positive-definite kernels to orthogonal basis functions. In fact, for GPs, the Karhunen-Loève expansion can be interpreted as decomposing the GP prior into orthogonal spatial modes, where the eigenfunctions correspond to the principal directions of variability implied by the covariance kernel.

Mercer’s theorem. In simple terms, the Mercer’s theorem, which is typically formulated in the setting of Hilbert spaces in a manner similar to the representer theorem, states that a kernel functionkkcan be represented via its non-negative eigenvalues(λp)p=1∞(\lambda_{p})_{p=1}^{\infty}and corresponding orthogonal eigenfunctions(ϕp)p=1∞(\phi_{p})_{p=1}^{\infty}as followsk​(𝐗,𝐗′)=∑p=1∞λp​ϕp​(𝐗)​ϕp​(𝐗′).k(\mathbf{X},\mathbf{X}^{\prime})=\sum_{p=1}^{\infty}\lambda_{p}\phi_{p}(\mathbf{X})\phi_{p}(\mathbf{X}^{\prime})\;.(184)

In this expression, each eigenfunctionϕp​(𝐗)\phi_{p}(\mathbf{X})represents a deterministic spatial mode, while its associated eigenvalueλp\lambda_{p}quantifies the magnitude, orenergy, of that mode in the kernel’s representation. With this knowledge, we can also understand why Eq. (182) yields samples whose covariance follows Eq. (179) by abstracting the proof for the samples obtained from Cholesky decomposition in Section8.2.1.
In the context of GPs, the kernel functionk​(𝐗,𝐗′)k(\mathbf{X},\mathbf{X}^{\prime})defines the covariance structure of the prior distribution over functions. Mercer’s theorem implies that this covariance kernel can be decomposed spectrally as above, i.e., it admits an eigenfunction decomposition, which in turn means that any sample from the GP priorg∼GP​(0,k​(𝐱,𝐱′))g\sim\mathrm{GP}(0,k(\mathbf{x},\mathbf{x}^{\prime}))can be represented (in distribution) as a above series expansion.

Thus, a GP prior can be viewed as a random series expansion over the orthonormal basis, a perspective that is closely related to the popularrandom featuresapproachRahimi and Recht [2007]. In this representation, each eigenfunctionϕp\phi_{p}contributes a spatial mode of variability, and the associated eigenvalueλp\lambda_{p}determines how strongly that mode influences the overall process. The larger the eigenvalue, the greater the contribution of that eigenfunction to the field’s variability.
This viewpoint provides a function-space interpretation of GPs. Instead of treating a GP as a distribution over random variables, it can be understood as a distribution over functions spanned by the basisϕp\phi_{p}. The smoothness, statistics, complexity, and expressiveness of the GP are therefore determined directly by the spectral properties of the kernelk​(𝐗,𝐗′)k(\mathbf{X},\mathbf{X}^{\prime}).

## 8.3Non-Gaussian random fields

Until now, we have only explicitly discussed Gaussian random fields in Section8.1and, separately, sampling methods in Section8.2. Among these methods, only the Cholesky decomposition is strictly limited to Gaussian fields, while Shinozuka’s method yields only approximately Gaussian samples in the limit of a large number of modes, due to the central limit theorem.
In contrast, the Karhunen–Loève expansion (Section8.2.3) does not rely on any assumption of Gaussianity. It merely ensures that the second-order statistics (Eq. (179)) are satisfied for a given random field, irrespective of its higher-order statistics. Only if all higher-order cumulants vanish is a Gaussian field recovered.
However, none of these methods is well suited for the explicit modeling of non-Gaussian random fields or their higher-order statistics, which we briefly introduce next.

The realization of non-Gaussian random fields is indeed an active area of researchLiu et al. [2019]. In many classical engineering and biomechanical applications, random spatial fields do not follow a purely Gaussian distribution. For instance, variables such as material properties, biological tissue microstructure, or loading conditions may exhibit asymmetric or heavy-tailed spatial distributions that cannot be accurately represented by a Gaussian model. A common strategy to construct such fields is to apply a probability transformation to an underlying Gaussian random field.

Letggdenote a Gaussian random field andgnong_{\rm non}the corresponding transformed non-Gaussian random field, with𝒞g{\mathcal{C}}_{g}and𝒞gnon−1{\mathcal{C}}_{g_{\rm non}}^{-1}denoting the cumulative distribution function ofggand the inverse cumulative distribution function (quantile function) ofgnong_{\rm non}, respectively. The transformation between the two fields can then be written asGrigoriu [1995,1998], Kim and Shields [2015]gnon​(Ω0)=𝒞gnon−1​[𝒞g​[g​(Ω0)]].g_{\rm non}(\Omega_{0})={\mathcal{C}}^{-1}_{g_{\rm non}}\Big[{\mathcal{C}}_{g}\big[g(\Omega_{0})\big]\Big]\;.(185)

In this mapping, each realization of the Gaussian field is first transformed to a uniform variable through its cumulative distribution function𝒞g{\mathcal{C}}_{g}, and then mapped to the target non-Gaussian distribution using the inverse cumulative distribution function𝒞gnon−1{\mathcal{C}}_{g_{\rm non}}^{-1}. This approach ensures that the marginal distribution of the transformed field follows the desired non-Gaussian form while inheriting the spatial correlation structure of the underlying Gaussian field in transformed form.

However, evaluating this transformation in practice can be challenging. Computing𝒞g{\mathcal{C}}_{g}may be computationally expensive, especially for large-scale correlated Gaussian fields, and closed-form expressions for the inverse𝒞gnon−1{\mathcal{C}}_{g_{\rm non}}^{-1}are often unavailable. Consequently, elaborate numerical procedures are typically required to generate approximate samples from non-Gaussian random fieldsVio et al. [2001], Trandafir and Demetriu [2005], Bocchini and Deodatis [2008], Shields et al. [2011], Kim and Shields [2015]. Despite these difficulties, such transformations remain a widely used and flexible approach for modeling complex spatial variability in engineering and biomechanical systems.

## 8.3.1Pointwise transformation methods

Non-Gaussian transformations can also be applied pointwise when specific constraints on the parameter range of a random field must be enforced. Such transformations are particularly useful when the modeled quantity must remain within physical or probabilistic bounds, as is often required in material modeling or probabilistic simulationsRanftl et al. [2022].Figure 10:Exemplary applications of (non-Gaussian) random fields in biomechanics: (a) stochastic perturbation of a patient-specific aortic surface, in which the nodes of a structured hexahedral mesh are displaced using maps derived from Gaussian random fields to model local boundary uncertainty; (b) modeling local pathological degradation of elastic fibers in aortic dissection as observed in histology, where the spatially varying degradation is represented by a beta random field.

To illustrate the concept, consider first a univariate example. Letg1\mathrm{g}_{1}andg2\mathrm{g}_{2}be two independent Gaussian random variables. The sum of their squares,g12+g22\mathrm{g}_{1}^{2}+\mathrm{g}_{2}^{2}, follows a Gamma distribution, more preciselyχ2\chi^{2}-distribution. If we defineΓ1=g12+g22\Gamma_{1}=\mathrm{g}_{1}^{2}+\mathrm{g}_{2}^{2}andΓ2=g32+g42\Gamma_{2}=\mathrm{g}_{3}^{2}+\mathrm{g}_{4}^{2}as two independent Gamma-distributed variables, then their ratioΓ1/(Γ1+Γ2)\Gamma_{1}/(\Gamma_{1}+\Gamma_{2})follows a Beta distribution, in this case, a uniform distribution, as shown inRanftl et al. [2022]. This simple example demonstrates how non-Gaussian random variables with bounded support can be generated through algebraic combinations of Gaussian random variablesHasofer et al. [1998], Vio et al. [2001,2002], Trandafir and Demetriu [2005].

We now extend this concept to spatially correlated random fields. Let{gν​(𝐗)}\{g_{\nu}(\mathbf{X})\},ν=1,…,2​R\nu=1,\dots,2R,R∈ℕR\in\mathbb{N}, be a collection of independent Gaussian random fields, and letgν​(𝐗¯)g_{\nu}(\underline{\mathbf{X}})be their corresponding discretization on a set of nodes𝐗¯\underline{\mathbf{X}}as in Section8.1. Each fieldgνg_{\nu}is assumed to have identical statistical properties but remains independent of the others. For simplicity, we omit the superscriptsssdenoting individual realizations, following the notation used in Section8.2.

A Gamma-type random field is then obtained by pointwise transformation asΓR​(𝐗)=12​∑ν=12​Rgν2​(𝐗),\Gamma_{R}(\mathbf{X})=\frac{1}{2}\sum_{\nu=1}^{2R}g_{\nu}^{2}(\mathbf{X})\;,(186)

where the squaring and summation are applied element-wise, ensuring thatΓR\Gamma_{R}andgνg_{\nu}share the same spatial support and discretization. Consequently, a sample of a Gamma field,ΓR(s)​(𝐗¯)\Gamma_{R}^{(s)}(\underline{\mathbf{X}}), can be generated from at least two independent Gaussian random field samples,g1(s)​(𝐗¯)g_{1}^{(s)}({\underline{\mathbf{X}}})andg2(s)​(𝐗¯)g_{2}^{(s)}({\underline{\mathbf{X}}}), by applying a pointwise transformation at each𝐗(n)∈𝐗¯\mathbf{X}^{(n)}\in\underline{\mathbf{X}}according to Eq. (186). Note that the Gamma distribution includes the exponential andχ\chi-distributions as special cases.

With two independent Gamma fields,ΓR​(𝐗)\Gamma_{R}(\mathbf{X})andΓR′​(𝐗)\Gamma_{R^{\prime}}(\mathbf{X}), characterized by the same covariance structure, a Beta-type random fieldβR,R′​(𝐗){\beta}_{R,{R^{\prime}}}(\mathbf{X})can be constructed asβR,R′​(𝐗)=ΓR​(𝐗)ΓR​(𝐗)+ΓR′​(𝐗),{\beta}_{R,{R^{\prime}}}(\mathbf{X})=\frac{\Gamma_{R}(\mathbf{X})}{\Gamma_{R}(\mathbf{X})+\Gamma_{R^{\prime}}(\mathbf{X})}\;,(187)

where the division and addition are likewise applied element-wise. Samples ofβR,R′(s)​(𝐗¯){\beta}_{R,{R^{\prime}}}^{(s)}(\underline{\mathbf{X}})can then be generated on this set of nodes, as before, from two independent Gamma random field samples,ΓR(s)​(𝐗¯)\Gamma_{R}^{(s)}(\underline{\mathbf{X}})andΓR′(s)​(𝐗¯)\Gamma_{R^{\prime}}^{(s)}(\underline{\mathbf{X}}), via a pointwise transformation according to Eq. (187).
The univariate marginal PDF of this field — i.e., at a fixed spatial location𝐗\mathbf{X}(cf. Eq. (187)) — follows a Beta distribution,p​(β∣𝐗)=1ℬ​(R,R′)​βR−1​(1−β)R′−1,\displaystyle p\big(\beta\bm{\mid}\mathbf{X}\big)=\frac{1}{{\cal{B}}(R,R^{\prime})}\beta^{R-1}(1-\beta)^{{R^{\prime}}-1}\;,∀𝐗∈𝐗¯,0≤β≤1.\displaystyle\quad\forall\,\mathbf{X}\in\underline{\mathbf{X}}\;,\quad 0\leq\beta\leq 1\;.(188)

We have thus constructed a random field realization whose values are either strictly positive (Eq.186) or strictly bounded between 0 and 1 (Eq.187) at every point in the domain. These constraints are crucial in mechanical problems, where negative values of Young’s modulus or unbounded order parameters such as damage variables are physically meaningless. Moreover, even a negative value at a single point in the domain can have detrimental implications for the numerical solution of the boundary value problem.

While generating Gaussian random fields on simple domains is typically straightforward, the computational effort can increase substantially for complex geometries or irregular meshes. Moreover, closed-form expressions for the correlation structure of transformed fields have been proposed inHasofer et al. [1998], Vio et al. [2001], Shields et al. [2011], yet practical applications may still face numerical challenges, especially when enforcing a prescribed correlation structureBenowitz et al. [2015].

In summary, pointwise transformation methods provide a practical means of constructing non-Gaussian random fields with bounded support, enabling the modeling of physically constrained parameters. In practice, these methods are often combined with Gaussian field generation methods such as the Shinozuka spectral approach or the Karhunen–Loève expansion, which can serve as the approximately Gaussian bases for subsequent transformations212121We note a word of caution that transformations mapping random variables from infinite to finite support can introduce numerical artifacts, causing the transformed fields to deviate from their expected statistical properties. Accordingly, practitioners should always verify the statistics of transformed fields numerically..

Finally, the random field generation methods presented here are not exhaustive. Readers interested in more sophisticated methods are referred to related excellent literatureKramer et al. [2007]. These include methods for anisotropic fieldsFuglstad et al. [2015a,b]or large computational domainsde Carvalho Paludo et al. [2019], Panunzio et al. [2018], approaches based on fast Markovian approximationsRue [2001], formulations that represent the random field as the solution of a PDE with stochastic forcing on the same spatial discretizationLindgren et al. [2011], as well as Lanczos-type methodsChow and Saad [2014]and contour-integral-based methodsAune et al. [2013].

## 9Discussion

In this review article, we introduced UQ for mechanical problems through the lens of Bayesian probability theory. Specifically, we presented it as a unifying framework for the two central challenges in mechanics: forward problems and inverse problems, backed by a significant body of literature and simple yet illustrative examples. We place a specific emphasis on biomechanical applications, where inherent variability and uncertainty necessitates such a framework, and provide illustrative examples to clarify these concepts.

The Bayesian perspective offers several conceptual and practical advantages for mechanics, specifically within the field of biomechanics. First, Bayesian inference dissolves the artificial boundaries between UQ and propagation, parameter estimation, and surrogate modeling, enabling the seamless integration of sensitivity analysis and scientific machine learning, where data-driven models complement physics-based approaches. Second, by representing uncertainties as probability distributions rather than point estimates, Bayesian inference supports engineering design and decision-making. In biomechanics, this facilitates clinical decision-making under uncertainty, acting as a key enabler for clinical translation. Third, it allows for flexible andconsistent, rigorousintegration of data and models — priors, likelihoods, and surrogates act as modular components that can be tailored to specific mechanical problems. Finally, by making modeling choices explicit and quantifiable, Bayesian methods reduce hidden assumptions and clarify the distinction betweenepistemicandaleatoricuncertainty, and the mixing thereof, an ongoing debate often clouded by ambiguityDer Kiureghian and Ditlevsen [2009], Wollner et al. [2026]. This improves interpretability, transparency, reproducibility, and predictive reliability. Furthermore, Bayesian frameworks naturally interface with computational tools like sampling, optimization, and experimental design, all of which are relevant in (bio)mechanics.

As there are still many open problems, several promising research directions emerge for advancing the Bayesian perspective in mechanics. The selection of priors, likelihoods, and surrogate models remains problem dependent and is often complicated by limited or inaccessible data. For many parameters, suitable priors are simply unavailable and substantial research is necessary to specify meaningfulanduseful input distributions from experimental or clinical information. Progress in scalable Bayesian computation through efficient sampling, variational methods, and multifidelity strategies will be essential to handle high dimensional, nonlinear, and large scale biomechanical models. Closer integration with scientific machine learning, including NOs, PINNs, and hybrid physics–data models, offers new opportunities but still requires rigorous Bayesian formulations and explicit treatment of surrogate uncertainty, which is still in its infancy. Especially surrogate modeling approaches that are explicitly tailored to and informed by mechanics remain rare. Bayesian experimental design provides an underexplored means to maximize information gain and optimize data collection. Addressing random fields and multiscale uncertainty will be crucial for modeling spatially heterogeneous and hierarchical materials and for linking macroscale variability to microscale structure. Finally, advancing clinical translation by embedding Bayesian UQ into decision support systems can enhance the credibility and impact of computational biomechanics in personalized medicine and medical device development.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Author contribution

S.R. conceived and developed the theoretical framework, and led the overall integration and writing of the manuscript.
M.R. shaped the (bio)mechanics perspective, connected the theoretical framework to and conceptualized application examples, drafted parts of the manuscript, and refined the formal presentation for didactic clarity and managed the manuscript preparation.
G.A.H., and E.K. contributed field-specific expertise, discussions, and manuscript revision.
All authors reviewed and approved the final manuscript.

## Acknowledgements

S.R. was financially supported by the Austrian Science Fund (FWF) under grand no. 10.55776/J4774.
M.R. and E.K. acknowledge support from the European Research Council (ERC) under grant no. 101141626 (DISCOVER), funded by the European Union. Views and opinions expressed are, however, those of the authors only and do not necessarily reflect those of the European Union or the European Research Council Executive Agency. Neither the European Union nor the granting authority can be held responsible for them.
The authors wish to acknowledge Maximilian P. Wollner (Institute of Biomechanics, Graz University of Technology, Graz, Austria) for his many valuable discussions, constructive feedback, and critical revisions of earlier drafts of this manuscript.

## References
- \bibcommenthead
- Eck et al. [2016]Eck, V.G.,
Donders, W.P.,
Sturdy, J.,
Feinberg, J.,
Delhaas, T.,
Hellevik, L.R.,
Huberts, W.:
A guide to uncertainty quantification and sensitivity analysis for cardiovascular applications.
International Journal for Numerical Methods in Biomedical Engineering32(8),
02755
(2016)https://doi.org/10.1002/cnm.2755
- Cox [1946]Cox, R.T.:
Probability, frequency and reasonable expectation.
American Journal of Physics14(1),
1–13
(1946)https://doi.org/10.1119/1.1990764
- Sivia and Skilling [2006]Sivia, D.,
Skilling, J.:
Data Analysis: A Bayesian Tutorial,
(2006).
Oxford University Press
- Wollner et al. [2025]Wollner, M.P.,
Rolf-Pissarczyk, M.,
Holzapfel, G.A.:
A reparameterization-invariant Bayesian framework for uncertainty estimation and calibration of simple materials.
Computational Mechanics,
1–31
(2025)https://doi.org/10.1007/s00466-024-02573-2
- Garrett [1998]Garrett, A.J.M.:
Whence the laws of probability?
In: Erickson, G.J.,
Rychert, J.T.,
Smith, C.R. (eds.)
Maximum Entropy and Bayesian Methods. Fundamental Theories of Physics,
pp. 71–86
(1998).https://doi.org/10.1007/978-94-011-5028-6_6.
Springer
- Jaynes [2003]Jaynes, E.T.:
Probability Theory,
(2003).https://doi.org/10.1017/CBO9780511790423.
Cambridge University Press
- von Toussaint [2011]von Toussaint, U.:
Bayesian inference in physics.
Reviews of Modern Physics83(3),
943–999
(2011)https://doi.org/10.1103/RevModPhys.83.943
- von der Linden et al. [2014]von der Linden, W.,
Dose, V.,
von Toussaint, U.:
Bayesian Probability Theory: Applications in the Physical Sciences,
1st edn.
(2014).https://doi.org/10.1017/CBO9781139565608.
Cambridge University Press
- Knuth and Skilling [2012]Knuth, K.H.,
Skilling, J.:
Foundations of inference.
Axioms1(1),
38–73
(2012)https://doi.org/10.3390/axioms1010038
- Wollner et al. [2026]Wollner, M.P.,
Rolf, M.,
Ranftl, S.,
Holzapfel, G.A.:
Uncertainty quantification in biomechanics: probabilistic fundamentals.
In: Holzapfel, G.A.,
Rolf, M.,
Xu, X.Y. (eds.)
Model Validation and Uncertainty Quantification in Biomechanics: Sources and Methods of Uncertainty and Variability Analysis,
(2026).
Academic Press
- Avril et al. [2008]Avril, S.,
Bonnet, M.,
Bretelle, A.-S.,
Grédiac, M.,
Hild, F.,
Ienny, P.,
Latourte, F.,
Lemosse, D.,
Pagano, S.,
Pagnacco, E.,
Pierron, F.:
Overview of identification methods of mechanical parameters based on full-field measurements.
Experimental Mechanics48,
381–402
(2008)https://doi.org/10.1007/s11340-008-9148-y
- Haylock [1997]Haylock, R.G.E.:
Bayesian Inference About Outputs of Computationally Expensive Algorithms with Uncertainty on the Inputs.
PhD thesis,
Universtity of Nottingham, UK
(1997)
- O’Hagan et al. [1999]O’Hagan, A.,
Kennedy, M.C.,
Oakley, J.E.:
Uncertainty analysis and other inference tools for complex computer codes.
In: Bernardo, J.M.,et al.(eds.)
Bayesian Staistics 6: Proceedings of the Sixth Valencia International Meeting June 6-10,
pp. 503–524
(1999).https://doi.org/10.1093/oso/9780198504856.003.0022
- Kennedy and O’Hagan [2000]Kennedy, M.C.,
O’Hagan, A.:
Predicting the output from a complex computer code when fast approximations are available.
Biometrika87(1),
1–13
(2000)https://doi.org/10.1093/biomet/87.1.1
- Oakley and O’Hagan [2002]Oakley, J.,
O’Hagan, A.:
Bayesian inference for the uncertainty distribution of computer model outputs.
Biometrika89(4),
769–784
(2002)https://doi.org/10.1093/biomet/89.4.769
- O’Hagan [2006]O’Hagan, A.:
Bayesian analysis of computer code outputs: a tutorial.
Reliability Engineering & System Safety91(10–11),
1290–1300
(2006)https://doi.org/10.1016/j.ress.2005.11.025
- Ranftl and von der Linden [2021]Ranftl, S.,
von der Linden, W.:
Bayesian surrogate analysis and uncertainty propagation.
In: Physical Sciences Forum,
vol. 3,
p. 6
(2021).https://doi.org/10.3390/psf2021003006.
MaxEnt 2021 Proceedings
- Fokina et al. [2020]Fokina, D.,
Muravleva, E.,
Ovchinnikov, G.,
Oseledets, I.:
Microstructure synthesis using style-based generative adversarial networks.
Physical Review E101(4),
043308
(2020)https://doi.org/10.1103/PhysRevE.101.043308
- Hsu et al. [2021]Hsu, T.,
Epting, W.K.,
Kim, H.,
Abernathy, H.W.,
Hackett, G.A.,
Rollett, A.D.,
Salvador, P.A.,
Holm, E.A.:
Microstructure generation via generative adversarial network for heterogeneous, topologically complex 3D materials.
JOM73(1),
90–102
(2021)https://doi.org/10.1007/s11837-020-04484-y
- Lambard et al. [2023]Lambard, G.,
Yamazaki, K.,
Demura, M.:
Generation of highly realistic microstructural images of alloys from limited data with a style-based generative adversarial network.
Scientific Reports13(1),
566
(2023)https://doi.org/10.1038/s41598-023-27574-8
- Feldman et al. [2025]Feldman, P.,
Fainstein, M.,
Siless, V.,
Delrieux, C.,
Iarussi, E.:
Recursive variational autoencoders for 3D blood vessel generative modeling.
Medical Image Analysis,
103703
(2025)https://doi.org/10.1016/j.media.2025.103703
- Liang et al. [2017]Liang, L.,
Liu, M.,
Martin, C.,
Elefteriades, J.A.,
Sun, W.:
A machine learning approach to investigate the relationship between shape features and numerically predicted risk of ascending aortic aneurysm.
Biomechanics and Modeling in Mechanobiology16(5),
1519–1533
(2017)https://doi.org/10.1007/s10237-017-0903-9
- Verstraeten et al. [2026]Verstraeten, S.,
Brüning, J.,
Goubergrits, L.,
Schievano, S.,
Capelli, C.,
Rizzo, A.,
Rolf, M.,
Holzapfel, G.A.,
Spanjaards, M.,
Huberts, W.,
SIMCor consortium:
Generation and validation of virtual patient cohorts forin silicoclinical trials: achievements from theSIMCorproject.
In: Holzapfel, G.A.,
Rolf, M.,
Xu, X.Y. (eds.)
Model Validation and Uncertainty Quantification in Biomechanics: From Biological Soft Tissue to Blood Flow,
(2026).
Academic Press
- Lyu and Ren [2024]Lyu, X.,
Ren, X.:
Microstructure reconstruction of 2D/3D random materials via diffusion-based deep generative models.
Scientific Reports14(1),
5041
(2024)https://doi.org/10.1038/s41598-024-54861-9
- Colmenarez et al. [2025]Colmenarez, J.A.,
Dong, P.,
Li, X.,
Gu, L.:
Biomechanics-trained diffusion model predicts post-PCI plaque morphology and rupture from IVOCT: towards an AI digital twin for stent planning.
Computers in Biology and Medicine198 Part B,
111216
(2025)https://doi.org/10.1016/j.compbiomed.2025.111216
- Vahidullah and Kuhl [2026]Vahidullah, T.,
Kuhl, E.:
Generative AI for material design: a mechanics perspective from burgers to matter.
Computer Methods in Applied Mechanics and Engineering461 Part A,
119171
(2026)https://doi.org/10.1016/j.cma.2026.119171
- Yang et al. [2019]Yang, G.,
Huang, X.,
Hao, Z.,
Liu, M.-Y.,
Belongie, S.,
Hariharan, B.:
Pointflow: 3D point cloud generation with continuous normalizing flows.
In: Proceedings of the IEEE/CVF International Conference on Computer Vision,
pp. 4541–4550
(2019).https://doi.org/10.1109/ICCV.2019.00464
- Ranftl et al. [2022]Ranftl, S.,
Rolf-Pissarczyk, M.,
Wolkerstorfer, G.,
Pepe, A.,
Egger, J.,
von der Linden, W.,
Holzapfel, G.A.:
Stochastic modeling of inhomogeneities in the aortic wall and uncertainty quantification using a bayesian encoder–decoder surrogate.
Computer Methods in Applied Mechanics and Engineering401,
115594
(2022)https://doi.org/10.1016/j.cma.2022.115594
- Holzapfel et al. [2015]Holzapfel, G.A.,
Niestrawska, J.A.,
Ogden, R.W.,
Reinisch, A.J.,
Schriefl, A.J.:
Modelling non-symmetric collagen fibre dispersion in arterial walls.
Journal of The Royal Society Interface12(106),
20150188
(2015)https://doi.org/10.1098/rsif.2015.0188
- Jammalamadaka and Sengupta [2001]Jammalamadaka, S.R.,
Sengupta, A.:
Topics in Circular Statistics
vol. 5,
(2001).https://doi.org/10.1142/4031.
World Scientific
- Jaynes [1957]Jaynes, E.T.:
Information theory and statistical mechanics.
The Physical Review106(4),
620–630
(1957)https://doi.org/10.1103/PhysRev.106.620
- Jeffreys [1939]Jeffreys, H.:
Theory of Probability,
(1939).
Clarendon Press
- Kroese et al. [2011]Kroese, D.P.,
Taimre, T.,
Botev, Z.I.:
Handbook of Monte Carlo Methods,
(2011).https://doi.org/10.1002/9781118014967.
John Wiley & Sons, Inc
- Pensalfini et al. [2026]Pensalfini, M.,
Böl, M.,
Buganza Tepole, A.:
Identification of model parameter distributions via multilevel Bayesian approaches.
In: Holzapfel, G.A.,
Rolf, M.,
Xu, X.Y. (eds.)
Model Validation and Uncertainty Quantification in Biomechanics: Sources and Methods of Uncertainty and Variability Analysis,
(2026).
Academic Press
- Ranftl et al. [2022]Ranftl, S.,
Müller, T.S.,
Windberger, U.,
Brenn, G.,
von der Linden, W.:
ABayesian approach to blood rheological uncertainties in aortic hemodynamics.
International Journal for Numerical Methods in Biomedical Engineering,
3576
(2022)https://doi.org/10.1002/cnm.3576
- Madireddy et al. [2016]Madireddy, S.,
Sista, B.,
Vemaganti, K.:
Bayesian calibration of hyperelastic constitutive models of soft tissue.
Journal of the Mechanical Behavior of Biomedical Materials59,
108–127
(2016)https://doi.org/10.1016/j.jmbbm.2015.10.025
- Teferra and Brewick [2019]Teferra, K.,
Brewick, P.T.:
ABayesian model calibration framework to evaluate brain tissue characterization experiments.
Computer Methods in Applied Mechanics and Engineering357,
112604
(2019)https://doi.org/10.1016/j.cma.2019.112604
- Sundnes and Rodríguez-Cantano [2022]Sundnes, J.,
Rodríguez-Cantano, R.:
A Bayesian approach to parameter estimation in cardiac mechanics.
In: Sommer, G.,
Li, K.,
Haspinger, D.C.,
Ogden, R.W. (eds.)
Solid (Bio)mechanics: Challenges of the Next Decade. Studies in Mechanobiology, Tissue Engineering and Biomaterials
vol. 24,
(2022).https://doi.org/10.1007/978-3-030-92339-6_10.
Springer Cham
- Joshi et al. [2022]Joshi, A.,
Thakolkaran, P.,
Zheng, Y.,
Escande, M.,
Flaschel, M.,
De Lorenzis, L.,
Kumar, S.:
Bayesian-EUCLID: discovering hyperelastic material laws with uncertainties.
Computer Methods in Applied Mechanics and Engineering398,
115225
(2022)https://doi.org/10.1016/j.cma.2022.115225
- Krijnen et al. [2025]Krijnen, R.P.,
Joshi, A.,
Kumar, S.,
Peirlinck, M.:
Unsupervised full-field Bayesian inference of orthotropic hyperelasticity from a single biaxial test: a myocardial case study.
arXiv
(2025)https://doi.org/10.48550/arXiv.2510.09498
- Richter et al. [2025]Richter, J.,
Nitzler, J.,
Pegolotti, L.,
Menon, K.,
Biehler, J.,
Wall, W.A.,
Schiavazzi, D.E.,
Marsden, A.L.,
Pfaller, M.R.:
Bayesian Windkessel calibration using optimized zero-dimensional surrogate models.
Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences383(2292)
(2025)https://doi.org/10.1098/rsta.2024.0223
- Choi et al. [2026]Choi, C.H.,
Marsden, A.L.,
Schiavazzi, D.E.:
FalconBC: Flow matching for Amortized inference of Latent-CONditioned physiologic Boundary Conditions.
arXiv
(2026)https://doi.org/10.48550/arXiv.2603.19331
- Karumuri and Bilionis [2024]Karumuri, S.,
Bilionis, I.:
Learning to solve Bayesian inverse problems: an amortized variational inference approach using Gaussian and flow guides.
Journal of Computational Physics511,
113117
(2024)https://doi.org/10.1016/j.jcp.2024.113117
- Thomas et al. [2022]Thomas, A.J.,
Barocio, E.,
Bilionis, I.,
Pipes, R.B.:
Bayesian inference of fiber orientation and polymer properties in short fiber-reinforced polymer composites.
Composites Science and Technology228,
109630
(2022)https://doi.org/10.1016/j.compscitech.2022.109630
- Chakraborty and Messner [2021]Chakraborty, A.,
Messner, M.C.:
Bayesian analysis for estimating statistical parameter distributions of elasto-viscoplastic material models.
Probabilistic Engineering Mechanics66,
103153
(2021)https://doi.org/10.1016/j.probengmech.2021.103153
- Khodadadian et al. [2020]Khodadadian, A.,
Noii, N.,
Parvizi, M.,
Abbaszadeh, M.,
Wick, T.,
Heitzinger, C.:
A Bayesian estimation method for variational phase-field fracture problems.
Computational Mechanics66,
827–849
(2020)https://doi.org/10.1007/s00466-020-01876-4
- Willmann et al. [2022]Willmann, H.,
Nitzler, J.,
Brandstaeter, S.,
Wall, W.A.:
Bayesian calibration of coupled computational mechanics models under uncertainty based on interface deformation.
Advanced Modeling and Simulation in Engineering Sciences9,
24
(2022)https://doi.org/10.1186/s40323-022-00237-5
- Yang et al. [2021]Yang, L.,
Meng, X.,
Karniadakis, G.E.:
B-pinns: Bayesian physics-informed neural networks for forward and inverse PDE problems with noisy data.
Journal of Computational Physics425,
109913
(2021)https://doi.org/10.1016/j.jcp.2020.109913
- Linka et al. [2022]Linka, K.,
Schäfer, A.,
Meng, X.,
Zou, Z.,
Karniadakis, G.E.,
Kuhl, E.:
Bayesian physics informed neural networks for real-world nonlinear dynamical systems.
Computer Methods in Applied Mechanics and Engineering402,
115346
(2022)https://doi.org/10.1016/j.cma.2022.115346
- Linka et al. [2025]Linka, K.,
Holzapfel, G.A.,
Kuhl, E.:
Discovering uncertainty: Bayesian constitutive artificial neural networks.
Computer Methods in Applied Mechanics and Engineering433,
117517
(2025)https://doi.org/10.1016/j.cma.2024.117517
- Xie et al. [2021]Xie, H.,
Song, J.,
Zhong, Y.,
Li, J.,
Gu, C.,
Choi, K.-S.:
Extended Kalman filter nonlinear finite element method for nonlinear soft tissue deformation.
Computer Methods and Programs in Biomedicine200,
105828
(2021)https://doi.org/10.1016/j.cmpb.2020.105828
- Song et al. [2023]Song, J.,
Xie, H.,
Zhong, Y.,
Gu, C.,
Choi, K.-S.:
Maximum likelihood-based extendedKalman filter for soft tissue modelling.
Journal of the Mechanical Behavior of Biomedical Materials137,
105553
(2023)https://doi.org/10.1016/j.jmbbm.2022.105553
- Zhu et al. [2023]Zhu, X.,
Li, J.,
Zhong, Y.,
Choi, K.-S.,
Shirinzadeh, B.,
Smith, J.,
Gu, C.:
Iterative Kalman filter for biological tissue identification.
International Journal of Robust and Nonlinear Control35,
3949–3961
(2023)https://doi.org/10.1002/rnc.6742
- Kennedy and O’Hagan [2001]Kennedy, M.C.,
O’Hagan, A.:
Bayesian calibration of computer models.
Journal of the Royal Statistical Society: Series B (Statistical Methodology)63(3),
425–464
(2001)https://doi.org/10.1111/1467-9868.00294
- Morrison et al. [2018]Morrison, R.E.,
Oliver, T.A.,
Moser, R.D.:
Representing model inadequacy: a stochastic operator approach.
SIAM/ASA Journal on Uncertainty Quantification6(2),
457–496
(2018)https://doi.org/10.1137/16M1106419
- Paun et al. [2020]Paun, L.M.,
Colebank, M.J.,
Olufsen, M.S.,
Hill, N.A.,
Husmeier, D.:
Assessing model mismatch and model selection in a Bayesian uncertainty quantification analysis of a fluid-dynamics model of pulmonary blood circulation.
Journal of the Royal Society Interface17(173),
20200886
(2020)https://doi.org/10.1098/rsif.2020.0886
- Römer et al. [2022]Römer, U.,
Liu, J.,
Böl, M.:
Surrogate-based Bayesian calibration of biomechanical models with isotropic material behavior.
International Journal for Numerical Methods in Biomedical Engineering38,
3575
(2022)https://doi.org/10.1002/cnm.3575
- Calvetti et al. [2018]Calvetti, D.,
Dunlop, M.,
Somersalo, E.,
Stuart, A.:
Iterative updating of model error for Bayesian inversion.
Inverse Problems34,
025008
(2018)https://doi.org/10.1088/1361-6420/aaa34d
- Pensalfini and Buganza Tepole [2023]Pensalfini, M.,
Buganza Tepole, A.:
Mechano-biological and bio-mechanical pathways in cutaneous wound healing.
PLoS Computational Biology19(3),
1010902
(2023)https://doi.org/10.1371/journal.pcbi.1010902
- Koutsourelakis [2009]Koutsourelakis, P.-S.:
Accurate uncertainty quantification using inaccurate computational models.
SIAM Journal on Scientific Computing31(5),
3274–3300
(2009)https://doi.org/10.1137/080733565
- Wiener [1938]Wiener, N.:
The homogeneous chaos.
American Journal of Mathematics60(4),
897–936
(1938)https://doi.org/10.2307/2371268
- Xiu and Karniadakis [2002]Xiu, D.,
Karniadakis, G.E.:
TheWiener–Askey polynomial chaos for stochastic differential equations.
SIAM Journal on Scientific Computing24(2),
619–644
(2002)https://doi.org/10.1137/S1064827501387826
- Ghanem and Spanos [1991]Ghanem, R.G.,
Spanos, P.D.:
Stochastic Finite Elements: A Spectral Approach,
(1991).https://doi.org/10.1007/978-1-4612-3094-6.
Springer New York, NY
- Ghanem et al. [2017]Ghanem, R.,
Higdon, D.,
Owhadi, H. (eds.):
Handbook of Uncertainty Quantification
vol. 6,
(2017).https://doi.org/10.1007/978-3-319-12385-1.
Springer Cham
- O’Hagan [2013]O’Hagan, A.:
Polynomial chaos: a tutorial and critique from a statistician’s perspective
(2013).http://tonyohagan.co.uk/academic/pdf/Polynomial-chaos.pdf,accessed25.06.2019
- Oladyshkin and Nowak [2012]Oladyshkin, S.,
Nowak, W.:
Data-driven uncertainty quantification using the arbitrary polynomial chaos expansion.
Reliability Engineering & System Safety106,
179–190
(2012)https://doi.org/10.1016/j.ress.2012.05.002
- Jakeman et al. [2019]Jakeman, J.D.,
Franzelin, F.,
Narayan, A.,
Eldred, M.,
Plfüger, D.:
Polynomial chaos expansions for dependent random variables.
Computer Methods in Applied Mechanics and Engineering351,
643–666
(2019)https://doi.org/10.1016/j.cma.2019.03.049
- Torre et al. [2019]Torre, E.,
Marelli, S.,
Embrechts, P.,
Sudret, B.:
A general framework for data-driven uncertainty quantification under complex input dependencies using vine copulas.
Probabilistic Engineering Mechanics55,
1–16
(2019)https://doi.org/10.1016/j.probengmech.2018.08.001
- Xiu and Karniadakis [2005]Xiu, D.,
Karniadakis, G.E.:
The Wiener-Askey polynomial chaos for stochastic differential equations.
SIAM Journal on Scientific Computing27(3),
1118–1139
(2005)
- Sudret [2008]Sudret, B.:
Global sensitivity analysis using polynomial chaos expansions.
Reliability Engineering & System Safety93(7),
964–979
(2008)https://doi.org/10.1016/j.ress.2007.04.002
- Crestaux et al. [2009]Crestaux, T.,
Le Maître, O.P.,
Martinez, J.-M.:
Polynomial chaos expansion for sensitivity analysis.
Reliability Engineering & System Safety94(7),
1161–1172
(2009)https://doi.org/10.1016/j.ress.2008.10.008
- Mühlpfordt et al. [2017]Mühlpfordt, T.,
Findeisen, R.,
Hagenmeyer, V.,
Faulwasser, T.:
Comments on truncation errors for polynomial chaos expansions.
IEEE Control Systems Letters2(1),
169–174
(2017)https://doi.org/10.1109/LCSYS.2017.2778138
- Zhang et al. [2011]Zhang, Z.,
Choi, M.,
Karniadakis, G.E.:
Anchor points matter inANOVAdecomposition.
In: Hesthaven, J.,
Rønquist, E. (eds.)
Spectral and High Order Methods for Partial Differential Equations. Lecture Notes in Computational Science and Engineering
vol. 76,
pp. 347–355
(2011).https://doi.org/10.1007/978-3-642-15337-2_32.
Springer Berlin
- Foo and Karniadakis [2010]Foo, J.,
Karniadakis, G.E.:
Multi-element probabilistic collocation method in high dimensions.
Journal of Computational Physics229(5),
1536–1557
(2010)https://doi.org/10.1016/j.jcp.2009.10.043
- Blatman and Sudret [2011]Blatman, G.,
Sudret, B.:
Adaptive sparse polynomial chaos expansion based on least angle regression.
Journal of Computational Physics230(6),
2345–2367
(2011)
- Doostan and Owhadi [2011]Doostan, A.,
Owhadi, H.:
A non-adapted sparse approximation ofPDEs with stochastic inputs.
Journal of Computational Physics230(8),
3015–3034
(2011)https://doi.org/10.1016/j.jcp.2011.01.002
- Lüthen et al. [2021]Lüthen, N.,
Marelli, S.,
Sudret, B.:
Sparse polynomial chaos expansions: literature survey and benchmark.
SIAM/ASA Journal on Uncertainty Quantification9(2),
593–649
(2021)https://doi.org/10.1137/20M1315774
- Zhang et al. [2019]Zhang, D.,
Lu, L.,
Guo, L.,
Karniadakis, G.E.:
Quantifying total uncertainty in physics-informed neural networks for solving forward and inverse stochastic problems.
Journal of Computational Physics397,
108850
(2019)https://doi.org/10.1016/j.jcp.2019.07.048
- Schwab and Zech [2019]Schwab, C.,
Zech, J.:
Deep learning in high dimension: neural network expression rates for generalized polynomial chaos expansions in UQ.
Analysis and Applications17(1)
(2019)https://doi.org/10.1142/S0219530518500203
- Cooper [2021]Cooper, R.G.:
Augmented Neural Network Surrogate Models for Polynomial Chaos Expansions and Reduced Order Modeling.
PhD thesis,
Virginia Polytechnic Institute and State University, CA, USA
(2021)
- Zheng et al. [2021]Zheng, X.,
Zhang, J.,
Wang, N.,
Tang, G.,
Yao, W.:
Mini-data-driven deep arbitrary polynomial chaos expansion for uncertainty quantification.
Reliability Engineering & System Safety229,
108813
(2021)https://doi.org/10.1016/j.ress.2022.108813
- Lütjens et al. [2021]Lütjens, B.,
Crawford, C.H.,
Veillette, M.,
Newman, D.:
PCE-PINNs: Physics-informed neural networks for uncertainty propagation in ocean modeling.
arXiv
(2021)https://doi.org/10.48550/arXiv.2105.02939
- Zheng et al. [2022]Zheng, X.,
Yao, W.,
Zhang, Y.,
Zhang, X.:
Consistency regularization-based deep polynomial chaos neural network method for reliability analysis.
Reliability Engineering & System Safety227,
108732
(2022)https://doi.org/10.1016/j.ress.2022.108732
- Oladyshkin et al. [2023]Oladyshkin, S.,
Praditia, T.,
Kroeker, I.,
Mohammadi, F.,
Nowak, W.,
Otte, S.:
The deep arbitrary polynomial chaos neural network or how deep artificial neural networks could benefit from data-driven homogeneous chaos theory.
Neural Networks166,
85–104
(2023)https://doi.org/10.1016/j.neunet.2023.06.036
- Yao et al. [2023]Yao, W.,
Zheng, X.,
Zhang, J.,
Wang, N.,
Tang, G.:
Deep adaptive arbitrary polynomial chaos expansion: a mini-data-driven semi-supervised method for uncertainty quantification.
Reliability Engineering & System Safety229,
108813
(2023)https://doi.org/10.1016/j.ress.2022.108813
- Bahmani et al. [2025]Bahmani, B.,
Kevrekidis, I.G.,
Shields, M.D.:
Neural chaos: a spectral stochastic neural operator.
Journal of Computational Physics539,
114233
(2025)https://doi.org/10.1016/j.jcp.2025.114233
- Exenberger et al. [2026]Exenberger, J.,
Ranftl, S.,
Peharz, R.:
Deep polynomial chaos expansion.
29th International Conference on Artificial Intelligence and Statistics (AISTATS)
(2026)https://doi.org/10.48550/arXiv.2507.21273
- Campos et al. [2023]Campos, J.O.,
Guedes, R.M.,
Werneck, Y.B.,
Barra, L.P.S.,
dos Santos, R.W.,
Rocha, B.M.:
Polynomial chaos expansion surrogate modeling of passive cardiac mechanics using the Holzapfel–Ogden constitutive model.
Journal of Computational Science71,
102039
(2023)https://doi.org/10.1016/j.jocs.2023.102039
- Rodríguez-Cantano et al. [2019]Rodríguez-Cantano, R.,
Sundnes, J.,
Rognes, M.E.:
Uncertainty in cardiac myofiber orientation and stiffnesses dominate the variability of left ventricle deformation response.
International Journal for Numerical Methods in Biomedical Engineering35(5),
3178
(2019)https://doi.org/10.1002/cnm.3178
- Jafarinia et al. [2023]Jafarinia, A.,
Melito, G.M.,
Müller, T.S.,
Rolf-Pissarczyk, M.,
Holzapfel, G.A.,
Brenn, G.,
Ellermann, K.,
Hochrainer, T.:
Morphological parameters affecting false lumen thrombosis following type B aortic dissection: a systematic study based on simulations of idealized models.
Biomechanics and Modeling in Mechanobiology22(3),
885–904
(2023)https://doi.org/10.1007/s10237-023-01687-5
- Krige [1951]Krige, D.G.:
A statistical approach to some basic mine valuation problems on the Witwatersrand.
Journal of the Southern African Institute of Mining and Metallurgy52(6),
119–139
(1951)https://doi.org/10.10520/AJA0038223X_4792
- O’Hagan [1978]O’Hagan, A.:
Curve fitting and optimal design for prediction.
Journal of the Royal Statistical Society. Series B (Methodological)40(1),
1–42
(1978)https://doi.org/10.2307/2984861
- Rasmussen and Williams [2006]Rasmussen, C.E.,
Williams, C.K.I.:
Gaussian Pocesses for Machine Learning,
(2006).https://doi.org/10.1142/S0129065704001899.
The MIT Press
- Abrahamsen [1997]Abrahamsen, P.:
Gaussian random fields and correlation functions.
Norwegian Computing Center, Norway
(1997)
- Cuturi [2009]Cuturi, M.:
Positive definite kernels in machine learning.
arXiv
(2009)https://doi.org/10.48550/arXiv.0911.5367
- Duvenaud [2014]Duvenaud, D.K.:
Automatic Model Construction with Gaussian Processes.
PhD thesis,
University of Cambridge, UK
(2014)
- Schobi et al. [2015]Schobi, R.,
Sudret, B.,
Wiart, J.:
Polynomial-chaos-based Kriging.
International Journal for Uncertainty Quantification5(2)
(2015)https://doi.org/10.1615/Int.J.UncertaintyQuantification.2015012467
- Cortes and Vapnik [1995]Cortes, C.,
Vapnik, V.:
Support-vector networks.
Machine Learning20(3),
273–297
(1995)https://doi.org/10.1007/BF00994018
- Vovk [2013]Vovk, V.:
Kernel ridge regression.
In: Schölkopf, B.,
Luo, Z.,
Vovk, V. (eds.)
Empirical Inference,
(2013).https://doi.org/10.1007/978-3-642-41136-6_11.
Springer Berlin, Heidelberg
- Girard [2004]Girard, A.:
Approximate Methods for Propagation of Uncertainty with Gaussian Process Models.
PhD thesis,
University of Glasgow, UK
(2004)
- Marrel et al. [2009]Marrel, A.,
Iooss, B.,
Laurent, B.,
Roustant, O.:
Calculations of Sobol indices for the Gaussian process metamodel.
Reliability Engineering & System Safety94(3),
742–751
(2009)https://doi.org/10.1016/j.ress.2008.07.008
- Wirthl et al. [2023]Wirthl, B.,
Brandstaeter, S.,
Nitzler, J.,
Schrefler, B.A.,
Wall, W.A.:
Global sensitivity analysis based on Gaussian-process metamodelling for complex biomechanical problems.
International Journal for Numerical Methods in Biomedical Engineering39(3),
3675
(2023)https://doi.org/10.1002/cnm.3675
- Hensman et al. [2013]Hensman, J.,
Fusi, N.,
Lawrence, N.D.:
Gaussian processes for big data.
arXiv
(2013)https://doi.org/10.48550/arXiv.1309.6835
- Liu et al. [2020]Liu, H.,
Ong, Y.-S.,
Shen, X.,
Cai, J.:
WhenGaussian process meets big data: a review of scalableGPs.
IEEE Transactions on Neural Networks and Learning Systems31(11),
4405–4423
(2020)https://doi.org/10.1109/TNNLS.2019.2957109
- Binois and Wycoff [2022]Binois, M.,
Wycoff, N.:
A survey on high-dimensional Gaussian process modeling with application to Bayesian optimization.
ACM Transactions on Evolutionary Learning and Optimization2(8),
1–26
(2022)https://doi.org/10.1145/354561
- Brandstaeter et al. [2021]Brandstaeter, S.,
Fuchs, S.L.,
Biehler, J.:
Global sensitivity analysis of a homogenized constrained mixture model of arterial growth and remodeling.
Journal of Elasticity145,
191–221
(2021)https://doi.org/10.1007/s10659-021-09833-9
- Wirthl et al. [2023]Wirthl, B.,
Brandstaeter, S.,
Nitzler, J.,
Schrefler, B.A.,
Wall, W.A.:
Global sensitivity analysis based on Gaussian-process metamodelling for complex biomechanical problems.
International Journal for Numerical Methods in Biomedical Engineering39(3),
3675
(2023)https://doi.org/10.1002/cnm.3675
- Lee et al. [2018]Lee, T.,
Turin, S.Y.,
Gosain, A.K.,
Bilionis, I.,
Buganza Tepole, A.:
Propagation of material behavior uncertainty in a nonlinear finite element model of reconstructive surgery.
Biomechanics and Modeling in Mechanobiology17,
1857–1873
(2018)https://doi.org/10.1007/s10237-018-1061-4
- Dinkel et al. [2024]Dinkel, M.,
Geitner, C.M.,
Robalo Rei, G.,
Nitzler, J.,
Wall, W.A.:
Solving Bayesian inverse problems with expensive likelihoods using constrained Gaussian processes and active learning.
Inverse Problems40,
095008
(2024)https://doi.org/10.1088/1361-6420/ad5eb4
- Dalton et al. [2026]Dalton, D.,
Gao, H.,
Husmeier, D.:
Finite-element Gaussian processes for the machine learning of steady-state linear partial differential equations.
Computer Methods in Applied Mechanics and Engineering451,
118580
(2026)https://doi.org/10.1016/j.cma.2025.118580
- Paun et al. [2025]Paun, L.M.,
Colebank, M.J.,
Husmeier, D.:
A comparison of Gaussian processes and polynomial chaos emulators in the context of haemodynamic pulse–wave propagation modelling.
Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences383,
20240222
(2025)https://doi.org/10.1098/rsta.2024.0222
- Ranftl et al. [2019]Ranftl, S.,
Melito, G.M.,
Badeli, V.,
Reinbacher-Köstinger, A.,
Ellermann, K.,
Linden, W.:
Bayesian uncertainty quantification with multi-fidelity data and Gaussian processes for impedance cardiography of aortic dissection.
Entropy22(1),
58
(2019)https://doi.org/10.3390/e22010058
- Huang et al. [2006]Huang, G.-B.,
Zhu, Q.-Y.,
Siew, C.-K.:
Extreme learning machine: theory and applications.
Neurocomputing70(1-3),
489–501
(2006)https://doi.org/10.1016/j.neucom.2005.12.126
- Rahimi and Recht [2007]Rahimi, A.,
Recht, B.:
Random features for large-scale kernel machines.
In: Proceedings of the 21st International Conference on Neural Information Processing System,
vol. 20
(2007)
- Tripathy and Bilionis [2018]Tripathy, R.K.,
Bilionis, I.:
Deep UQ: Learning deep neural network surrogate models for high dimensional uncertainty quantification.
Journal of Computational Physics375,
565–588
(2018)https://doi.org/10.1016/j.jcp.2018.08.036
- Zhu and Zabaras [2018]Zhu, Y.,
Zabaras, N.:
Bayesian deep convolutional encoder–decoder networks for surrogate modeling and uncertainty quantification.
Journal of Computational Physics366,
415–447
(2018)
- Lakshminarayanan et al. [2017]Lakshminarayanan, B.,
Pritzel, A.,
Blundell, C.:
Simple and scalable predictive uncertainty estimation using deep ensembles.
arXiv
(2017)https://doi.org/10.48550/arXiv.1612.01474
- Wilson and Izmailov [2020]Wilson, A.G.,
Izmailov, P.:
Bayesian deep learning and a probabilistic perspective of generalization.
Advances in neural information processing systems33,
4697–4708
(2020)
- Karniadakis et al. [2021]Karniadakis, G.E.,
Kevrekidis, I.G.,
Lu, L.,
Perdikaris, P.,
Wang, S.,
Yang, L.:
Physics-informed machine learning.
Nature Reviews Physics3(6),
422–440
(2021)https://doi.org/10.1038/s42254-021-00314-5
- Zhu et al. [2019]Zhu, Y.,
Zabaras, N.,
Koutsourelakis, P.-S.,
Perdikaris, P.:
Physics-constrained deep learning for high-dimensional surrogate modeling and uncertainty quantification without labeled data.
Journal of Computational Physics394,
56–81
(2019)https://doi.org/10.1016/j.jcp.2019.05.024
- Wang et al. [2021]Wang, S.,
Teng, Y.,
Perdikaris, P.:
Understanding and mitigating gradient flow pathologies in physics-informed neural networks.
SIAM Journal on Scientific Computing43(5),
3055–3081
(2021)https://doi.org/10.1137/20M1318043
- Wang et al. [2022]Wang, S.,
Sankaran, S.,
Perdikaris, P.:
Respecting causality is all you need for training physics-informed neural networks.
Computer Methods in Applied Mechanics and Engineering421,
116813
(2022)https://doi.org/10.1016/j.cma.2024.116813
- Basir and Senocak [2022]Basir, S.,
Senocak, I.:
Physics and equality constrained artificial neural networks: application to forward and inverse problems with multi-fidelity data fusion.
Journal of Computational Physics463,
111301
(2022)https://doi.org/10.1016/j.jcp.2022.111301
- Wang et al. [2023]Wang, S.,
Sankaran, S.,
Wang, H.,
Perdikaris, P.:
An expert’s guide to training physics-informed neural networks.
arXiv
(2023)https://doi.org/10.48550/arXiv.2308.08468
- Novák et al. [2024]Novák, L.,
Sharma, H.,
Shields, M.D.:
Physics-informed polynomial chaos expansions.
Journal of Computational Physics506,
112926
(2024)https://doi.org/10.1016/j.jcp.2024.112926
- Raissi et al. [2017]Raissi, M.,
Perdikaris, P.,
Karniadakis, G.E.:
Machine learning of linear differential equations using Gaussian processes.
Journal of Computational Physics348,
683–693
(2017)https://doi.org/10.1016/j.jcp.2017.07.050
- Raissi and Karniadakis [2018]Raissi, M.,
Karniadakis, G.E.:
Hidden physics models: machine learning of nonlinear partial differential equations.
Journal of Computational Physics357,
125–141
(2018)https://doi.org/10.1016/j.jcp.2017.11.039
- Cross et al. [2024]Cross, E.J.,
Rogers, T.J.,
Pitchforth, D.J.,
Gibson, S.J.,
Zhang, S.,
Jones, M.R.:
A spectrum of physics-informed Gaussian processes for regression in engineering.
Data-Centric Engineering5,
8
(2024)https://doi.org/10.1017/dce.2024.2
- Lu et al. [2021]Lu, L.,
Jin, P.,
Pang, G.,
Zhang, Z.,
Karniadakis, G.E.:
Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators.
Nature Machine Intelligence3(3),
218–229
(2021)https://doi.org/10.1038/s42256-021-00302-5
- Wang et al. [2021]Wang, S.,
Wang, H.,
Perdikaris, P.:
Learning the solution operator of parametric partial differential equations with physics-informed deeponets.
Science Advances7(40),
8605
(2021)https://doi.org/10.1126/sciadv.abi8605
- Yu et al. [2024]Yu, X.,
Hooten, S.,
Liu, Z.,
Zhao, Y.,
Fiorentino, M.,
Van Vaerenbergh, T.,
Zhang, Z.:
Separable operator networks.
arXiv
(2024)https://doi.org/10.48550/arXiv.2407.11253
- Mandl et al. [2025]Mandl, L.,
Goswami, S.,
Lambers, L.,
Ricken, T.:
Separable physics-informed DeepONet: breaking the curse of dimensionality in physics-informed machine learning.
Computer Methods in Applied Mechanics and Engineering434,
117586
(2025)https://doi.org/10.1016/j.cma.2024.117586
- Yin et al. [2022]Yin, M.,
Ban, E.,
Rego, B.V.,
Zhang, E.,
Cavinato, C.,
Humphrey, J.D.,
Karniadakis, G.E.:
Simulating progressive intramural damage leading to aortic dissection using DeepONet: an operator–regression neural network.
Journal of The Royal Society Interface19(187),
20210670
(2022)https://doi.org/10.1098/rsif.2021.0670
- Goswami et al. [2022]Goswami, S.,
Li, D.S.,
Rego, B.V.,
Latorre, M.,
Humphrey, J.D.,
Karniadakis, G.E.:
Neural operator learning of heterogeneous mechanobiological insults contributing to aortic aneurysms.
Journal of The Royal Society Interface19,
20220410
(2022)https://doi.org/10.1098/rsif.2022.0410
- Agarwal et al. [2025]Agarwal, A.,
Sarkar, D.R.,
Goswami, S.:
Multimodal neural operators for real-time biomechanical modelling of traumatic brain injury.
arXiv
(2025)https://doi.org/10.48550/arXiv.2510.03248
- Hong et al. [2024]Hong, J.,
Min, C.,
Lee, B.,
Persad, A.R.,
Jeong, J.-H.,
Park, Y.-H.:
Estimating aortic pressure waveform in a 1D hemodynamic model of the human arterial system using DeepONet.
46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC),
1–5
(2024)https://doi.org/10.1109/EMBC53108.2024.10781510
- Zhu and Peng [2024]Zhu, Y.,
Peng, B.:
Neural Operator-based Framework for Time Efficient Denoising of Displacement Fields in Ultrasound Elastography,
pp. 3318–3323
(2024).https://doi.org/10.1109/SMC54092.2024.10831893
- Goswami et al. [2022]Goswami, S.,
Yin, M.,
Yu, Y.,
Karniadakis, G.E.:
A physics-informed variational DeepONet for predicting crack path in quasi-brittle materials.
Computer Methods in Applied Mechanics and Engineering391,
114587
(2022)https://doi.org/10.1016/j.cma.2022.114587
- Jafarzadeh et al. [2025]Jafarzadeh, S.,
Silling, S.,
Zhang, L.,
Ross, C.,
Lee, C.H.,
Rahman, S.M.R.,
Wang, S.,
Yu, Y.:
Heterogeneous peridynamic neural operators: discover biotissue constitutive law and microstructure from digital image correlation measurements.
Foundations of Data Science7,
226–270
(2025)https://doi.org/10.3934/fods.2024041
- You et al. [2022]You, H.,
Zhang, Q.,
Ross, C.J.,
Lee, C.-H.,
Hsu, M.-C.,
Yu, Y.:
A physics-guided neural operator learning approach to model biological tissues from digital image correlation measurements.
arXiv
(2022)https://doi.org/10.48550/arXiv.2204.00205
- Ahmadi et al. [2026]Ahmadi, N.,
Cao, Q.,
Humphrey, J.D.,
Karniadakis, G.E.:
Physics-informed machine learning in biomedical science and engineering.
Annual Review of Biomedical Engineering28,
309–336
(2026)https://doi.org/10.1146/annurev-bioeng-110824-124907
- Mandl et al. [2026]Mandl, L.,
Ricken, T.,
Goswami, S.:
Physics-informed neural operators for biomechanics: advancing computational modeling with separable architectures.
In: Holzapfel, G.A.,
Rolf, M.,
Xu, Y.X. (eds.)
Model Validation and Uncertainty Quantification in Biomechanics: From Soft Biological Tissue to Blood Flow,
(2026).
Academic Press
- Breiman et al. [2017]Breiman, L.,
Friedman, J.,
Olshen, R.A.,
Stone, C.J.:
Classification and Regression Trees,
(2017).https://doi.org/10.1201/9781315139470.
Chapman and Hall/CRC
- Breiman [2001]Breiman, L.:
Random forests.
Machine Learning45,
5–32
(2001)https://doi.org/10.1023/A:1010933404324
- Friedman [2002]Friedman, J.H.:
Stochastic gradient boosting.
Computational Statistics and Data Analysis38(4),
367–378
(2002)https://doi.org/10.1016/S0167-9473(01)00065-2
- Efron [1992]Efron, B.:
Bootstrap methods: another look at the jackknife.
In: Kotz, S.,
Johnson, N.L. (eds.)
Breakthroughs in Statistics: Methodology and Distribution,
pp. 569–593
(1992).https://doi.org/10.1007/978-1-4612-4380-9_41.
Springer New York
- Chen and Guestrin [2016]Chen, T.,
Guestrin, C.:
XGBoost: A scalable tree boosting system.
In: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining,
pp. 785–794.
Association for Computing Machinery,
New York, NY
(2016).https://doi.org/10.1145/2939672.2939785
- Prokhorenkova et al. [2019]Prokhorenkova, L.,
Gusev, G.,
Vorobev, A.,
Dorogush, A.V.,
Gulin, A.:
Catboost: Unbiased boosting with categorical features.
arXiv
(2019)https://doi.org/10.48550/arXiv.1706.09516
- Braito et al. [2026]Braito, S.,
Krispel, T.,
Badeli, V.,
Tronstad, C.,
Hisdal, J.,
Kalvøy, H.,
Kern, R.,
Ranftl, S.:
Uncertainty quantification for impedance plethysmography with gradient boosting tree regression.
In: Model Validation and Uncertainty Quantification in Biomechanics: Sources and Methods of Uncertainty and Variability Analysis,
(2026).
Academic Press
- Kerschen et al. [2005]Kerschen, G.,
Golinval, J.-C.,
Vakakis, A.F.,
Bergman, L.A.:
The method of proper orthogonal decomposition for dynamical characterization and order reduction of mechanical systems: an overview.
Nonlinear dynamics41(1),
147–169
(2005)https://doi.org/10.1007/s11071-005-2803-2
- Lassila et al. [2014]Lassila, T.,
Manzoni, A.,
Quarteroni, A.,
Rozza, G.:
Model order reduction in fluid dynamics: challenges and perspectives.
In: Quarteroni, A.,
Rozza, G. (eds.)
Reduced Order Methods for Modeling and Computational Reduction,
pp. 235–273
(2014).https://doi.org/10.1007/978-3-319-02090-7_9.
Springer Cham
- Rathore et al. [2025]Rathore, S.,
Africa, P.C.,
Ballarin, F.,
Pichi, F.,
Girfoglio, M.,
Rozza, G.:
Projection-based reduced order modelling for unsteady parametrized optimal control problems in 3D cardiovascular flows.
Computer Methods and Programs in Biomedicine269,
108813
(2025)https://doi.org/10.1016/j.cmpb.2025.108813
- Kutz et al. [2016]Kutz, J.N.,
Brunton, S.L.,
Brunton, B.W.,
Proctor, J.L.:
Dynamic Mode Decomposition: Data-Driven Modeling of Complex Systems,
(2016).https://doi.org/10.1137/1.9781611974508.
SIAM
- Chinesta et al. [2023]Chinesta, F.,
Cueto, E.,
Payan, Y.,
Ohayon, J. (eds.):
Reduced Order Models for the Biomechanics of Living Organs,
(2023).https://doi.org/10.1016/C2020-0-03057-4.
Academic Press
- Siena et al. [2023]Siena, P.,
Girfoglio, M.,
Rozza, G.:
Fast and accurate numerical simulations for the study of coronary artery bypass grafts by artificial neural networks.
In: Chinesta, F.,
Cueto, E.,
Payan, Y.,
Ohayon, J. (eds.)
Reduced Order Models for the Biomechanics of Living Organs,
pp. 167–183
(2023).https://doi.org/10.1016/B978-0-32-389967-3.00012-3.
Academic Press
- Balzotti et al. [2024]Balzotti, C.,
Siena, P.,
Girfoglio, M.,
Stabile, G.,
Dueñas-Pamplona, J.,
Sierra-Pallares, J.,
Amat-Santos, I.,
Rozza, G.:
A reduced order model formulation for left atrium flow: an atrial fibrillation case.
Biomechanics and Modeling in Mechanobiology23(4),
1411–1429
(2024)https://doi.org/10.1007/s10237-024-01847-1
- Chen et al. [2015]Chen, P.,
Quarteroni, A.,
Rozza, G.:
Reduced Order Methods for Uncertainty Quantification Problems
- Bäumler et al. [2025]Bäumler, K.,
Rolf-Pissarczyk, M.,
Schussnig, R.,
Fries, T.-P.,
Mistelbauer, G.,
Marsden, A.L.,
Fleischmann, D.,
Holzapfel, G.A.:
Assessment of aortic dissection remodeling with patient-specific fluid–structure interaction models.
IEEE Transactions on Biomedical Engineering72(3),
953–964
(2025)https://doi.org/10.1109/TBME.2024.3480362
- Fleeter et al. [2020]Fleeter, C.M.,
Geraci, G.,
Schiavazzi, D.E.,
Kahn, A.M.,
Marsden, A.M.:
Multilevel and multifidelity uncertainty quantification for cardiovascular hemodynamics.
Computer Methods in Applied Mechanics and Engineering365,
113030
(2020)https://doi.org/10.1016/j.cma.2020.113030
- Schäfer et al. [2026]Schäfer, F.,
Choi, C.,
Zanoni, A.,
Menon, K.,
Gianluca, G.,
Marsden, A.L.,
Schiavazzi, D.E.:
An introduction to multi-fidelity uncertainty propagation for applications in biomechanics.
In: Holzapfel, G.A.,
Rolf, M.,
Xu, X.Y. (eds.)
Model Validation and Uncertainty Quantification in Biomechanics: Sources and Methods of Uncertainty and Variability Analysis,
(2026).
Academic Press
- Biehler et al. [2015]Biehler, J.,
Gee, M.W.,
Wall, W.A.:
Towards efficient uncertainty quantification in complex and large-scale biomechanical problems based on a Bayesian multi-fidelity scheme.
Biomechanics and Modeling in Mechanobiology14(3),
489–513
(2015)https://doi.org/10.1007/s10237-014-0618-0
- Tran et al. [2017]Tran, J.S.,
Schiavazzi, D.E.,
Ramachandra, A.B.,
Kahn, A.M.,
Marsden, A.L.:
Automated tuning for parameter identification and uncertainty quantification in multi-scale coronary simulations.
Computers and Fluids142,
128–138
(2017)https://doi.org/10.1016/j.compfluid.2016.05.015
- Fleeter et al. [2020]Fleeter, C.M.,
Geraci, G.,
Schiavazzi, D.E.,
Kahn, A.M.,
Marsden, A.L.:
Multilevel and multifidelity uncertainty quantification for cardiovascular hemodynamics.
Computer Methods in Applied Mechanics and Engineering365,
113030
(2020)https://doi.org/10.1016/j.cma.2020.113030
- Lee et al. [2020]Lee, T.,
Bilionis, I.,
Buganza Tepole, A.:
Propagation of uncertainty in the mechanical and biological response of growing tissues using multi-fidelity Gaussian process regression.
Computer Methods in Applied Mechanics and Engineering359,
112724
(2020)https://doi.org/10.1016/j.cma.2019.112724
- Choi et al. [2025]Choi, C.H.,
Zanoni, A.,
Schiavazzi, D.E.,
Marsden, A.L.:
On the performance of multi-fidelity and reduced-dimensional neural emulators for inference of physiologic boundary conditions.
arXiv
(2025)https://doi.org/10.48550/arXiv.2506.11683
- Molléro et al. [2018]Molléro, R.,
Pennec, X.,
Delingette, H.,
Garny, A.,
Ayache, N.,
Sermesant, M.:
Multifidelity-CMA: a multifidelity approach for efficient personalisation of 3D cardiac electromechanical models.
Biomechanics and Modeling in Mechanobiology17(1),
285–300
(2018)https://doi.org/10.1007/s10237-017-0960-0
- Nitzler et al. [2022]Nitzler, J.,
Biehler, J.,
Fehn, N.,
Koutsourelakis, P.-S.,
Wall, W.A.:
A generalized probabilistic learning approach for multi-fidelity uncertainty quantification in complex physical simulations.
Computer Methods in Applied Mechanics and Engineering400,
115600
(2022)https://doi.org/10.1016/j.cma.2022.115600
- Nitzler et al. [2026a]Nitzler, J.,
Temür, B.Z.,
Koutsourelakis, P.-S.,
Wall, W.A.:
Efficient Bayesian multi-fidelity inverse analysis for expensive and non-differentiable physics-based simulations in high stochastic dimensions.
Computer Methods in Applied Mechanics and Engineering448,
118442
(2026)https://doi.org/10.1016/j.cma.2025.118442
- Nitzler et al. [2026b]Nitzler, J.,
Bergbauer, M.,
Koutsourelakis, P.-S.,
Wall, W.A.:
Scalable high-dimensional Bayesian field reconstruction with finite elements: application to 3D porous media flow.
arXviv
(2026)https://doi.org/10.48550/arXiv.2605.24682
- Kass and Raftery [1995]Kass, R.E.,
Raftery, A.E.:
Bayes factors.
Journal of the American Statistical Association90(430),
773–795
(1995)
- O’Hagan [1995]O’Hagan, A.:
Fractional Bayes factors for model comparison.
Journal of the Royal Statistical Society: Series B (Methodological)57(1),
99–118
(1995)https://doi.org/10.1111/j.2517-6161.1995.tb02017.x
- Madireddy et al. [2015]Madireddy, S.,
Sista, B.,
Vemaganti, K.:
A Bayesian approach to selecting hyperelastic constitutive models of soft tissue.
Computer Methods in Applied Mechanics and Engineering291,
102–122
(2015)https://doi.org/10.1016/j.cma.2015.03.012
- Aggarwal et al. [2023]Aggarwal, A.,
Hudson, L.T.,
Laurence, D.W.,
Lee, C.-H.,
Pant, S.:
A Bayesian constitutive model selection framework for biaxial mechanical testing of planar soft tissues: application to porcine aortic valves.
Journal of the Mechanical Behavior of Biomedical Materials138,
105657
(2023)https://doi.org/10.1016/j.jmbbm.2023.105657
- Ritto and Nunes [2015]Ritto, T.G.,
Nunes, L.C.S.:
Bayesian model selection of hyperelastic models for simple and pure shear at large deformations.
Computers & Structures165,
101–109
(2015)https://doi.org/10.1016/j.compstruc.2015.04.008
- Mototake et al. [2020]Mototake, Y.I.,
Izuno, H.,
Nagata, K.,
Demura, M.,
Okada, M.:
A universal Bayesian inference framework for complicated creep constitutive equations.
Scientific Reports10(1),
10437
(2020)https://doi.org/10.1038/s41598-020-65945-7
- Battalgazy et al. [2025]Battalgazy, B.,
Khatamsaz, D.,
Ghasemi, Z.,
Mallick, D.D.,
Arroyave, R.,
Srivastava, A.:
A Bayesian-based approach for constitutive model selection and calibration using diverse material responses.
Acta Materialia287,
120796
(2025)https://doi.org/10.1016/j.actamat.2025.120796
- Urrea–Quintero et al. [2026]Urrea–Quintero, J.-H.,
Anton, D.,
De Lorenzis, L.,
Wessels, H.:
Automated constitutive model discovery by pairing sparse regression algorithms with model selection criteria.
Computer Methods in Applied Mechanics and Engineering449 Part B,
118551
(2026)https://doi.org/10.1016/j.cma.2025.118551
- Chiachío et al. [2015]Chiachío, J.,
Chiachío, M.,
Saxena, A.,
Sankararaman, S.,
Rus, G.,
Goebel, K.:
Bayesian model selection and parameter estimation for fatigue damage progression models in composites.
International Journal of Fatigue70,
361–373
(2015)https://doi.org/10.1016/j.ijfatigue.2014.08.003
- Hamdia et al. [2019]Hamdia, K.M.,
Msekh, M.A.,
Silani, M.,
Thai, T.Q.,
Budarapu, P.R.,
Rabczuk, T.:
Assessment of computational fracture models using Bayesian method.
Engineering Fracture Mechanics205,
387–398
(2019)https://doi.org/10.1016/j.engfracmech.2018.09.019
- Oden et al. [2913]Oden, J.T.,
Prudencio, E.E.,
Hawkins-Daarud, a.:
Selection and assessment of phenomenological models of tumor growth.
Mathematical Models and Methods in Applied Sciences23(7),
1309–1338
(2913)https://doi.org/10.1142/S0218202513500103
- Rinkens et al. [2026]Rinkens, A.,
Verhoosel, C.V.,
Alicke, A.,
Anderson, P.D.,
Jaensson, N.O.:
Bayesian model selection for complex flows of yield stress fluids.
arXiv
(2026)https://doi.org/10.48550/arXiv.2601.10115
- Akaike [2003]Akaike, H.:
A new look at the statistical model identification.
IEEE Transactions on Automatic Control19(6),
716–723
(2003)https://doi.org/10.1109/TAC.1974.1100705
- Stoica and Selen [2004]Stoica, P.,
Selen, Y.:
Model-order selection: a review of information criterion rules.
IEEE Signal Processing Magazine21(4),
36–47
(2004)https://doi.org/10.1109/MSP.2004.1311138
- Javid et al. [2020]Javid, K.,
Handley, W.,
Hobson, M.,
Lasenby, A.:
Compromise-free Bayesian neural networks.
arXiv
(2020)https://doi.org/10.48550/arXiv.2004.12211
- Stone [1974]Stone, M.:
Cross-validatory choice and assessment of statistical predictions.
Journal of the Royal Statistical Society: Series B (Methodological)36(2),
111–133
(1974)https://doi.org/10.1111/j.2517-6161.1974.tb00994.x
- Stone [1977]Stone, M.:
An asymptotic equivalence of choice of model by cross-validation and Akaike’s criterion.
Journal of the Royal Statistical Society: Series B (Methodological)39(1),
44–47
(1977)https://doi.org/10.1111/j.2517-6161.1977.tb01603.x
- Trevor et al. [2009]Trevor, H.,
Robert, T.,
Jerome, F.:
The Elements of Statistical Learning: Data Mining, Inference, and Prediction,
(2009).
Spinger. Chapter 9
- Chaloner and Verdinelli [1995]Chaloner, K.,
Verdinelli, I.:
Bayesian experimental design: a review.
Statistical Science10,
273–304
(1995)https://doi.org/10.1214/ss/1177009939
- DasGupta [1996]DasGupta, A.:
29. Review of optimal Bayes designs.
In: Ghosh, S.,
Rao, C.R. (eds.)
Design and Analysis of Experiments
vol. 13,
pp. 1099–1147
(1996).https://doi.org/10.1016/S0169-7161(96)13031-5
- Lindley [1972]Lindley, D.V.:
Bayesian statistics: a review.
In: Bayesian Statistics,
pp. 1–74
(1972).https://doi.org/10.1137/1.9781611970654.ch1
- MacKay [1992]MacKay, D.J.C.:
Information-based objective functions for active data selection.
Neural Computation4(4),
590–604
(1992)https://doi.org/10.1162/neco.1992.4.4.590
- Loredo [2004]Loredo, T.J.:
Bayesian adaptive exploration.
AIP Conference Proceedings707(1),
330–346
(2004)https://doi.org/10.1063/1.1751377
- Helin et al. [2025]Helin, T.,
Marzouk, Y.,
Rojo-Garcia, J.R.:
Bayesian optimal experimental design with Wasserstein information criteria.
arXiv
(2025)https://doi.org/10.48550/arXiv.2504.10092
- Huan and Marzouk [2013]Huan, X.,
Marzouk, Y.M.:
Simulation-based optimal Bayesian experimental design for nonlinear systems.
Journal of Computational Physics232,
288–317
(2013)https://doi.org/10.1016/j.jcp.2012.08.013
- Long et al. [2013]Long, Q.,
Scavino, M.,
Tempone, R.,
Wang, S.:
Fast estimation of expected information gains for Bayesian experimental designs based on Laplace approximations.
Computer Methods in Applied Mechanics and Engineering259,
24–39
(2013)https://doi.org/10.1016/j.cma.2013.02.017
- Beck et al. [2018]Beck, J.,
Dia, B.M.,
Espath, L.F.R.,
Long, Q.,
Tempone, R.:
Fast Bayesian experimental design: Laplace-based importance sampling for the expected information gain.
Computer Methods in Applied Mechanics and Engineering334,
523–553
(2018)https://doi.org/10.1016/j.cma.2018.01.053
- Pandita et al. [2019]Pandita, P.,
Bilionis, I.,
Panchal, J.:
Bayesian optimal design of experiments for inferring the statistical expectation of expensive black-box functions.
Journal of Mechanical Design141(10),
101404
(2019)https://doi.org/10.1115/1.4043930
- Pandita et al. [2021]Pandita, P.,
Tsilifis, P.,
Awalgaonkar, N.M.,
Bilionis, I.,
Panchal, J.:
Surrogate-based sequential Bayesian experimental design using non-stationary Gaussian processes.
Computer Methods in Applied Mechanics and Engineering385,
114007
(2021)https://doi.org/10.1016/j.cma.2021.114007
- Eberle-Blick and Hyvönen [2024]Eberle-Blick, S.,
Hyvönen, N.:
Bayesian experimental design for linear elasticity.
Inverse Problems and Imaging18,
1294–1319
(2024)https://doi.org/10.3934/ipi.2024015
- Ricciardi et al. [2024]Ricciardi, D.E.,
Seidl, D.T.,
Lester, B.T.,
Jones, A.R.,
Jones, E.M.C.:
Bayesian optimal experimental design for constitutive model calibration.
International Journal of Mechanical Sciences265,
108881
(2024)https://doi.org/10.1016/j.ijmecsci.2023.108881
- Bhattacharya et al. [2026]Bhattacharya, K.,
Cao, L.,
Stuart, A.:
Optimal experimental design for reliable learning of history-dependent constitutive laws.
Computer Methods in Applied Mechanics and Engineering457,
119022
(2026)https://doi.org/10.1016/j.cma.2026.119022
- Ryan et al. [2015]Ryan, E.G.,
Drovandi, C.C.,
McGree, J.M.,
Pettitt, A.N.:
A review of modern computational algorithms for Bayesian optimal design.
International Statistical Review84,
128–154
(2015)https://doi.org/10.1111/insr.12107
- Brochu et al. [2010]Brochu, E.,
Cora, V.M.,
de Freitas, N.:
A tutorial on Bayesian optimization of expensive cost functions, with application to active user modeling and hierarchical reinforcement learning.
arXiv
(2010)https://doi.org/10.48550/arXiv.1012.2599
- Shahriari et al. [2015]Shahriari, B.,
Swersky, K.,
Wang, Z.,
Adams, R.P.,
de Freitas, N.:
Taking the human out of the loop: a review of Bayesian optimization.
Proceedings of the IEEE104(1),
1–24
(2015)https://doi.org/10.1017/CBO9781107415324.004
- Frazier [2018]Frazier, P.I.:
A tutorial on Bayesian optimization.
arXiv
(2018)https://doi.org/10.48550/arXiv.1807.02811
- Kawaguchi et al. [2015]Kawaguchi, K.,
Kaelbling, L.P.,
Lozano-Pérez, T.:
Bayesian optimization with exponential convergence.
Advances in Neural Information Processing Systems28(2015)
- Jones et al. [1998]Jones, D.R.,
Schonlau, M.,
Welch, W.J.:
Efficient global optimization of expensive black-box functions.
Journal of Global Optimization13(4),
455–492
(1998)https://doi.org/10.1023/A:1008306431147
- Močkus [1974]Močkus, J.:
On Bayesian methods for seeking the extremum.
In: Močkus, J. (ed.)
Optimization Techniques IFIP Technical Conference Novosibirsk, July 1–7, 1974. Optimization Techniques 1974. Lecture Notes in Computer Science,
vol. 27,
pp. 400–404
(1974).https://doi.org/10.1007/3-540-07165-2_55.
Springer Berlin
- Hernández-Lobato et al. [2014]Hernández-Lobato, J.M.,
Hoffman, M.W.,
Ghahramani, Z.:
Predictive entropy search for efficient global optimization of black-box functions.
arXiv
(2014)https://doi.org/10.48550/arXiv.1406.2541
- Wang and Jegelka [2017]Wang, Z.,
Jegelka, S.:
Max-value entropy search for efficient Bayesian optimization.
arXiv
(2017)https://doi.org/10.48550/arXiv.1703.01968
- Preuss and von Toussaint [2021]Preuss, R.,
Toussaint, U.:
Global variance as a utility function in Bayesian optimization.
Physical Sciences Forum3(1),
3
(2021)https://doi.org/10.3390/psf2021003003
- Hoffer et al. [2023]Hoffer, J.G.,
Ranftl, S.,
Geiger, B.C.:
Robust Bayesian target value optimization.
Computers & Industrial Engineering180,
109279
(2023)
- Balandat et al. [2020]Balandat, M.,
Karrer, B.,
Jiang, D.,
Daulton, S.,
Letham, B.,
Wilson, A.G.,
Bakshy, E.:
Botorch: a framework for efficient Monte-Carlo Bayesian optimization.
arXiv
(2020)https://doi.org/10.48550/arXiv.1910.06403
- Tian et al. [2025]Tian, Y.,
Li, T.,
Pang, J.,
Zhou, Y.,
Xue, D.,
Ding, X.,
Lookmann, T.:
Materials design with target-oriented Bayesian optimization.
npj Computatational Materials11,
209
(2025)https://doi.org/10.1038/s41524-025-01704-4
- Kansara et al. [2025]Kansara, H.,
Khosroshahi, S.F.,
Guo, L.,
Bessa, M.A.,
Tan, W.:
Multi-objective Bayesian optimisation of spinodoid cellular structures for crush energy absorption.
Computer Methods in Applied Mechanics and Engineering440,
117890
(2025)https://doi.org/10.1016/j.cma.2025.117890
- Raßloff et al. [2025]Raßloff, A.,
Seibert, P.,
Kalina, K.A.,
Kästner, M.:
Inverse design of spinodoid structures using Bayesian optimization.
Computational Mechanics77,
275–296
(2025)https://doi.org/10.1007/s00466-024-02587-w
- Chiappetta et al. [2026]Chiappetta, M.,
Carraturo, M.,
Raßloff, A.,
Kästner, M.,
Auricchio, F.:
An efficient Bayesian framework for inverse problems via optimization and inversion: surrogate modeling, parameter inference, and uncertainty quantification.
arXiv
(2026)https://doi.org/10.48550/arXiv.2602.04537
- Vangelatos et al. [2021]Vangelatos, Z.,
Sheikh, H.M.,
Marcus, P.S.,
Grigoropoulos, C.P.,
Lopez, V.Z.,
Flamourakis, G.,
Farsari, M.:
Strength through defects: a novel Bayesian approach for the optimization of architected materials.
Science Advances7,
2218
(2021)https://doi.org/10.1126/sciadv.abk2218
- Borowska et al. [2022]Borowska, A.,
Gao, H.,
Lazarus, A.,
Husmeier, D.:
Bayesian optimisation for efficient parameter inference in a cardiac mechanics model of the left ventricle.
International Journal for Numerical Methods in Biomedical Engineering35(5),
3593
(2022)https://doi.org/10.1002/cnm.3593
- Miranda-Valdez et al. [2025]Miranda-Valdez, I.Y.,
Mäkinen, T.,
Koivisto, J.,
Alava, M.J.:
Bayesian optimization to infer parameters in viscoelasticity.
Journal of Rheology69(6),
1059–1066
(2025)https://doi.org/10.1122/8.0001068
- Snoek et al. [2012]Snoek, J.,
Larochelle, H.,
Adams, R.P.:
Practical Bayesian optimization of machine learning algorithms.
arXiv
(2012)https://doi.org/10.48550/arXiv.1206.2944
- Zhong et al. [2026]Zhong, Y.,
Li, Y.,
Xu, C.,
Xie, G.,
Hou, J.,
Shi, X.:
A Bayesian neural network and extended finite element method based prediction method of crack tip parameters and growth path.
Theoretical and Applied Fracture Mechanics145,
105659
(2026)https://doi.org/10.1016/j.tafmec.2026.105659
- Zhang et al. [2026]Zhang, D.,
Dai, W.,
Ding, Y.:
Bayesian optimization–based physics-informed neural network for adaptive prediction of multiaxial fatigue life in metallic materials.
Fatigue & Fracture of Engineering Materials & Structures49(1),
28–51
(2026)https://doi.org/10.1111/ffe.70101
- Huber et al. [2024]Huber, F.,
Bürkner, P.C.,
Göddeke, D.,
Schulte, M.:
Knowledge-based modeling of simulation behavior for Bayesian optimization.
Computational Mechanics74,
151–168
(2024)https://doi.org/10.1007/s00466-023-02427-3
- Saltelli et al. [2008]Saltelli, A.,
Ratto, M.,
Andres, T.,
Campolongo, F.,
Cariboni, J.,
Gatelli, D.,
Saisana, M.,
Tarantola, S.:
Global Sensitivity Analysis: The Primer,
(2008).https://doi.org/10.1002/9780470725184.
John Wiley & Sons
- Melito et al. [2026]Melito, G.M.,
Brandstaeter, S.,
Quicken, S.,
Rolf, M.,
Holzapfel, G.A.,
Ellermann, K.,
Huberts, W.:
Sensitivity analysis in biomechanics: addressing model complexity and uncertainty.
In: Holzapfel, G.A.,
Rolf, M.,
Xu, X.Y. (eds.)
Model Validation and Uncertainty Quantification in Biomechanics: Sources and Methods of Uncertainty and Variability Analysis,
(2026).
Academic Press
- Sobol’ [1990]Sobol’, I.M.H.:
On sensitivity estimation for nonlinear mathematical models.
Matematicheskoe modelirovanie2(1),
112–118
(1990)
- Oakley and O’Hagan [2004]Oakley, J.E.,
O’Hagan, A.:
Probabilistic sensitivity analysis of complex models: a Bayesian approach.
Journal of the Royal Statistical Society Series B: Statistical Methodology66(3),
751–769
(2004)https://doi.org/10.1111/j.1467-9868.2004.05304.x
- Becker et al. [2011]Becker, W.,
Rowson, J.,
Oakley, J.E.,
Yoxall, A.,
Manson, G.,
Worden, K.:
Bayesian sensitivity analysis of a model of the aortic valve.
Journal of Biomechanics44(8),
1499–1506
(2011)https://doi.org/10.1016/j.jbiomech.2011.03.008
- Melis et al. [2017]Melis, A.,
Clayton, R.H.,
Marzo, A.:
Bayesian sensitivity analysis of a 1D vascular model with Gaussian process emulators.
International Journal for Numerical Methods in Biomedical Engineering33(12),
2882
(2017)https://doi.org/10.1002/cnm.2882
- Vanmarcke [2010]Vanmarcke, E.:
Random Fields: Analysis and Synthesis,
(2010).
World Scientific
- Bošnjak et al. [2025]Bošnjak, D.,
Schussnig, R.,
Ranftl, S.,
Holzapfel, G.A.,
Fries, T.P.:
Geometric uncertainty of patient-specific blood vessels and its impact on aortic hemodynamics: A computational study.
Computers in Biology and Medicine190,
110017
(2025)https://doi.org/10.1016/j.compbiomed.2025.110017
- Hauseux et al. [2018]Hauseux, P.,
Hale, J.S.,
Cotin, S.,
Bordas, S.P.A.:
Quantifying the uncertainty in a hyperelastic soft tissue model with stochastic parameters.
Applied Mathematical Modelling62,
86–02
(2018)https://doi.org/10.1016/j.apm.2018.04.021
- Tran et al. [2019]Tran, J.S.,
Schiavazzi, D.E.,
Kahn, A.M.,
Marsden, A.L.:
Uncertainty quantification of simulated biomechanical stimuli in coronary artery bypass grafts.
Computer Methods in Applied Mechanics and Engineering345,
402–428
(2019)https://doi.org/10.1016/j.cma.2018.10.024
- He et al. [2025]He, X.,
Zhou, S.,
Xu, Y.,
Tian, J.:
Random phase field model for simulating mixed fracture modes in spatially variable rocks under impact loading.
International Journal of Impact Engineering196,
105174
(2025)https://doi.org/10.1016/j.ijimpeng.2024.105174
- Su et al. [2023]Su, Y.,
Zhu, J.,
Long, X.,
Zhao, L.,
Chen, C.,
Liu, C.:
Statistical effects of pore features on mechanical properties and fracture behaviors of heterogeneous random porous materials by phase-field modeling.
International Journal of Solids and Structures264,
112098
(2023)https://doi.org/10.1016/j.ijsolstr.2022.112098
- Hai and Li [2022]Hai, L.,
Li, J.:
Modeling tensile damage and fracture of quasi-brittle materials using stochastic phase-field model.
Theoretical and Applied Fracture Mechanics118,
103283
(2022)https://doi.org/10.1016/j.tafmec.2022.103283
- Stefanou et al. [2022]Stefanou, G.,
Savvas, D.,
Gavallas, P.,
Papaioannou, I.:
The effect of random field parameter uncertainty on the response variability of composite structures.
Composites Part C: Open Access9,
100324
(2022)https://doi.org/10.1016/j.jcomc.2022.100324
- Sakata et al. [2026]Sakata, S.,
Stefanou, G.,
Shirahama, K.,
Ono, S.:
Probabilistic strength estimation analysis of composites considering cross-correlated random fields of local strength and apparent elastic properties.
Mechanics Research Communications152,
104628
(2026)https://doi.org/10.1016/j.mechrescom.2026.104628
- Staber and Guilleminot [2018]Staber, B.,
Guilleminot, J.:
A random field model for anisotropic strain energy functions and its application for uncertainty quantification in vascular mechanics.
Computer Methods in Applied Mechanics and Engineering333,
94–113
(2018)https://doi.org/10.1016/j.cma.2018.01.001
- Shinozuka and Deodatis [1991]Shinozuka, M.,
Deodatis, G.:
Simulation of stochastic processes by spectral representation.
Appl Mech Rev44,
191–204
(1991)https://doi.org/10.1115/1.3119501
- Shinozuka and Deodatis [1996]Shinozuka, M.,
Deodatis, G.:
Simulation of multi-dimensionalGaussian stochastic fields by spectral representation.
Appl Mech Rev49,
29–53
(1996)https://doi.org/10.1115/1.3101883
- Xiu [2010]Xiu, D.:
Numerical Methods for Stochastic Computations: A Spectral Method Approach,
(2010).
Princeton University Press
- Le Maître and Knio [2010]Le Maître, O.,
Knio, O.M.:
Spectral Methods for Uncertainty Quantification: With Applications to Computational Fluid Dynamics,
(2010).https://doi.org/10.1007/978-90-481-3520-2.
Springer Dordrecht
- Liu et al. [2019]Liu, Y.,
Li, J.,
Sun, S.,
Yu, B.:
Advances inGaussian random field generation: a review.
Computers and Geosciences23(5),
1011–1047
(2019)https://doi.org/10.1007/s10596-019-09867-y
- Grigoriu [1995]Grigoriu, M.:
Applied Non-Gaussian Processes: Examples, Theory, Simulation, Linear Random Vibration, and MATLAB Solutions,
(1995).
Prentice Hall
- Grigoriu [1998]Grigoriu, M.:
Simulation of stationary non-Gaussian translation processes.
Journal of Engineering Mechanics124(2),
121–126
(1998)https://doi.org/10.1061/(ASCE)0733-9399(1998)124:2(121)
- Kim and Shields [2015]Kim, H.,
Shields, M.D.:
Simulation of strongly non-Gaussian non-stationary stochastic processes utilizingKarhunen-Loeve expansion.
In: 12th International Conference on Applications of Statistics and Probability in Civil Engineering, ICASP12
(2015)
- Vio et al. [2001]Vio, R.,
Andreani, P.,
Wamsteker, W.:
Numerical simulation of non–Gaussian random fields with prescribed correlation structure.
Publications of the Astronomical Society of the Pacific113(786),
1009–1020
(2001)https://doi.org/10.1086/322919
- Trandafir and Demetriu [2005]Trandafir, R.,
Demetriu, S.:
Numerical simulation of non–Gaussian random fields.
In: 7th Balkan Conference on Operational Research. Constanta, Romania,
pp. 231–237
(2005)
- Bocchini and Deodatis [2008]Bocchini, P.,
Deodatis, G.:
Critical review and latest developments of a class of simulation algorithms for strongly non-Gaussian random fields.
Probabilistic Engineering Mechanics23(4),
393–407
(2008)https://doi.org/10.1016/j.probengmech.2007.09.001
- Shields et al. [2011]Shields, M.D.,
Deodatis, G.,
Bocchini, P.:
A simple and efficient methodology to approximate a general non-Gaussian stationary stochastic process by a translation process.
Probabilistic Engineering Mechanics26(4),
511–519
(2011)https://doi.org/10.1016/j.probengmech.2011.04.003
- Hasofer et al. [1998]Hasofer, A.M.,
Ditlevsen, O.D.,
Tarp-Johansen, N.J.:
Positive random fields for modeling material stiffness and compliance.
In: 7th International Conference on Structural Safety and Reliability, ICOSSAR ’97,
pp. 723–730
(1998)
- Vio et al. [2002]Vio, R.,
Andreani, P.,
Tenorio, L.,
Wamsteker, W.:
Numerical simulation of non-Gaussian random fields with prescribed marginal distributions and cross-correlation structure. II. Multivariate random fields.
Publications of the Astronomical Society of the Pacific114,
1281–1289
(2002)https://doi.org/10.1086/342767
- Benowitz et al. [2015]Benowitz, B.A.,
Shields, M.D.,
Deodatis, G.:
Determining evolutionary spectra from non-stationary autocorrelation functions.
Probabilistic Engineering Mechanics41,
73–88
(2015)https://doi.org/10.1016/j.probengmech.2015.06.004
- Kramer et al. [2007]Kramer, P.R.,
Kurbanmuradov, O.,
Sabelfeld, K.:
Comparative analysis of multiscaleGaussian random field simulation algorithms.
Journal of Computational Physics226(1),
897–924
(2007)https://doi.org/10.1016/j.jcp.2007.05.002
- Fuglstad et al. [2015a]Fuglstad, G.A.,
Lindgren, F.,
Simpson, D.,
Rue, H.:
Exploring a new class of non-stationary spatialGaussian random fields with varying local anisotropy.
Statistica Sinica25(1),
115–133
(2015)https://doi.org/10.5705/ss.2013.106w
- Fuglstad et al. [2015b]Fuglstad, G.A.,
Simpson, D.,
Lindgren, F.,
Rue, H.:
Does non-stationary spatial data always require non-stationary random fields?
Spatial Statistics14,
505–531
(2015)https://doi.org/10.1016/j.spasta.2015.10.001
- de Carvalho Paludo et al. [2019]de Carvalho Paludo, L.,
Bouvier, V.,
Cottereau, R.:
Scalable parallel scheme for sampling ofGaussian random fields over very large domains.
International Journal for Numerical Methods in Engineering117(8),
845–859
(2019)https://doi.org/10.1002/nme.5981
- Panunzio et al. [2018]Panunzio, A.,
Cottereau, R.,
Puel, G.:
Large scale random fields generation using localizedKarhunen–Loève expansion.
Advanced Modeling and Simulation in Engineering Sciences5,
1–29
(2018)https://doi.org/0.1186/s40323-018-0114-7
- Rue [2001]Rue, H.:
Fast sampling ofGaussianMarkov random fields.
Journal of the Royal Statistical Society, Series B (Statistical Methodology)63(2),
325–338
(2001)https://doi.org/10.1016/j.cma.2019.02.003
- Lindgren et al. [2011]Lindgren, F.,
Rue, H.,
Lindström, J.:
An explicit link betweenGaussian fields andGaussianMarkov random fields: theSPDEapproach.
Journal of the Royal Statistical Society Series B73(4),
423–498
(2011)https://doi.org/10.1111/j.1467-9868.2011.00777.x
- Chow and Saad [2014]Chow, E.,
Saad, Y.:
PreconditionedKrylov subspace methods for sampling multivariateGaussian distributions.
SIAM Journal on Scientific Computing36(2),
588–608
(2014)https://doi.org/10.1137/130920587
- Aune et al. [2013]Aune, E.,
Eidsvik, J.,
Pokern, Y.:
Iterative numerical methods for sampling from high dimensionalGaussian distributions.
Statistics and Computing23(4),
501–521
(2013)https://doi.org/10.1007/s11222-012-9326-8
- Der Kiureghian and Ditlevsen [2009]Der Kiureghian, A.,
Ditlevsen, O.:
Aleatory or epistemic?Does it matter?
Structural Safety31(2),
105–112
(2009)https://doi.org/10.1007/s00466-024-02573-2

## 


- 


Major funding support from
