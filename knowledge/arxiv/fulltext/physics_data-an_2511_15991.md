# Identifying statistical indicators of temporal asymmetry using a data-driven approach

**arXiv ID**: 2511.15991v1
**Authors**: Teresa Dalle Nogare, Ben D. Fulcher
**Published**: 2025-11-20
**Categories**: physics.data-an, nlin.CD
**DOI**: 10.1103/4nb2-398s
**HTML URL**: https://arxiv.org/html/2511.15991v1

## Abstract

The dynamics of time-reversible systems are statistically indistinguishable when observed forward or backward in time. A rich literature of statistical methods to distinguish irreversible dynamics from the reversible dynamics of linear, Gaussian systems can provide insights into underlying mechanisms and aid modeling and statistical quantification of time-series data. But these existing time-reversibility metrics have been developed individually, forming a fragmented body of research that makes it challenging to identify the most effective approaches developed to date, and the most promising new directions for development. Here we address these issues by systematically evaluating over 6000 time-series summary statistics, derived from across the time-series analysis literature, on their ability to distinguish the time-irreversibility of data simulated from a diverse range of 35 systems. Our large-scale data-driven comparison highlights the effectiveness of several key families of statistics, including time-asymmetric forms of generalized autocorrelation functions, time-series symbolic sequences, and forecasting-related methods. All irreversible systems studied here could be accurately distinguished by a well-chosen time-series statistic, but no single statistic could accurately index the statistical form of irreversibility for all irreversible systems. This challenges the assumption that a given time-reversibility statistic will accurately capture time reversibility in general, and underscores the importance of tailoring statistical approaches to the time-reversal characteristics of a given system. Our results provide a unified understanding of the key algorithmic structures through which irreversibility can be effectively quantified from data, providing a foundation for connecting patterns in time series to the underlying mechanisms of the systems that generate them.

## Full Text

Identifying statistical indicators of temporal asymmetry using a data-driven approach
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- ††thanks:Contact author: teresa.dallenogare@sydney.edu.au††thanks:Contact author: ben.fulcher@sydney.edu.au

## Identifying statistical indicators of temporal asymmetry using a data-driven approachTeresa Dalle NogareBen D. FulcherSchool of Physics, The University of Sydney, Camperdown, NSW 2006, AustraliaCentre for Complex Systems, The University of Sydney, Camperdown, NSW 2006, Australia(November 20, 2025)

## Abstract

The dynamics of time-reversible systems are statistically indistinguishable when observed forward or backward in time.
A rich literature of statistical methods to distinguish irreversible dynamics from the reversible dynamics of linear, Gaussian systems can provide insights into underlying mechanisms and aid modeling and statistical quantification of time-series data.
But these existing time-reversibility metrics have been developed individually, forming a fragmented body of research that makes it challenging to identify the most effective approaches developed to date, and the most promising new directions for development.
Here we address these issues by systematically evaluating over 6000 time-series summary statistics, derived from across the time-series analysis literature, on their ability to distinguish the time-irreversibility of data simulated from a diverse range of 35 systems.
Our large-scale data-driven comparison highlights the effectiveness of several key families of statistics, including time-asymmetric forms of generalized autocorrelation functions, time-series symbolic sequences, and forecasting-related methods.
All irreversible systems studied here could be accurately distinguished by a well-chosen time-series statistic, but no single statistic could accurately index the statistical form of irreversibility for all irreversible systems.
This challenges the assumption that a given time-reversibility statistic will accurately capture time reversibility in general, and underscores the importance of tailoring statistical approaches to the time-reversal characteristics of a given system.
Our results provide a unified understanding of the key algorithmic structures through which irreversibility can be effectively quantified from data, providing a foundation for connecting patterns in time series to the underlying mechanisms of the systems that generate them.

## IIntroduction

The nature of time and the existence of a privileged direction in its flow have long fascinated both philosophers[1]and scientists, inspiring fundamental questions about the origin of time[2], the neural mechanisms of time perception[3], and the evolution of the universe[4].
The concept of time-reversibility has been studied across several disciplines, including time-series analysis[5], dynamical systems theory[6], and non-equilibrium statistical mechanics[7].
Its cross-disciplinary importance arises from the ubiquity of time-reversal asymmetric processes in the real world, motivating studies in both abstract deterministic and stochastic systems as well as in the thermodynamics of physical systems.
A deterministic dynamical system is considered reversible if its governing equations remain unchanged under time-reversal[8,6](cf. more general definitions, including for multidimensional systems[9,10]).
When studied in the context of nonequilibrium physical systems, irreversibility acquires a probabilistic interpretation, traditionally expressed in thermodynamics through the Second Law of Thermodynamics as entropy production at the macroscopic scale.
More recently, in stochastic thermodynamics—which has emerged as a theoretical framework that extends concepts from classical thermodynamics (e.g., entropy, heat, work) to smaller-scale systems where thermal fluctuations play a dominant role in the dynamics[11]—the Kullback–Leibler divergence between the probability distribution of systems trajectories evolving forward and backward in time links irreversibility (i.e. the distinguishability between the process unfolding forward versus backward in time) and entropy production, an indicator of the underlying dissipative mechanisms driving the process[12,13,14].

This study focuses on the statistical interpretation of time irreversibility (hereafter referred to as ‘irreversibility’), which refers to the ability to infer the temporal direction of a dynamical process from its observed dynamics.
That is, are the dynamics of some process statistically different from its time-reversed dynamics?
Formally, a discrete-time stationary process𝑿={Xt}t∈ℤ\bm{X}=\{X_{t}\}_{t\in\mathbb{Z}}is said to bereversibleif, for every time pointt∈ℤt\in\mathbb{Z}and everyk≥1k\geq 1, the joint distribution of the sequence𝑿t(k)≡(Xt,Xt+1,…,Xt+k)\bm{X}_{t}^{(k)}\equiv(X_{t},X_{t+1},\dots,X_{t+k})is identical to that of its time-reversed counterpart𝑿~t(k)≡(Xt+k,Xt+k−1,…,Xt)\tilde{\bm{X}}_{t}^{(k)}\equiv(X_{t+k},X_{t+k-1},...,X_{t}), that is𝑿t(k)=d𝑿~t(k),∀t∈ℤ​and​∀k≥1,\bm{X}_{t}^{(k)}\stackrel{{\scriptstyle d}}{{=}}\tilde{\bm{X}}_{t}^{(k)},\penalty 10000\ \penalty 10000\ \penalty 10000\ \forall t\in\mathbb{Z}\text{ and }\forall k\geq 1\,,(1)

where the symbol=d\stackrel{{\scriptstyle d}}{{=}}denotes that𝑿t(k)\bm{X}_{t}^{(k)}and𝑿~t(k)\tilde{\bm{X}}_{t}^{(k)}are identically distributed[15,5].
In other words, reversibility reflects the time-reversal symmetry of the probabilistic structure of a process[16], such that all of its statistical properties are invariant under time reversal[17].

In practice, we often seek to perform inference on the reversibility of a generative process from a single finite realization, i.e., a time series𝒙=(x1,x2,…,xT)\bm{x}=(x_{1},x_{2},...,x_{T}).
In this case, the time-reversed transformed time series𝒙~\tilde{\bm{x}}can be constructed by reversing the order of the data points, i.e.x~t=xT−t+1\tilde{x}_{t}=x_{T-t+1}[18,19,20,21].
Under the assumption of stationarity, the reversibility condition, Eq. (1), can then be inferred from the time-series data by estimating the joint distributions of𝒙t(k)=(xt,xt+1,…,xt+k)\bm{x}_{t}^{(k)}=(x_{t},x_{t+1},...,x_{t+k})and𝒙~t(k)=(xt+k,xt+k−1,…,xt)\tilde{\bm{x}}_{t}^{(k)}=(x_{t+k},x_{t+k-1},...,x_{t}), and quantifying their discrepancy using a suitable statistical distance or divergence measure (e.g., Kullback–Leibler divergence).
That is, the reversibility condition in Eq. (1) can be expressed as𝒙t(k)=d𝒙~t(k),∀t<T−k​and​∀k<T.\bm{x}_{t}^{(k)}\stackrel{{\scriptstyle d}}{{=}}\tilde{\bm{x}}_{t}^{(k)},\penalty 10000\ \penalty 10000\ \penalty 10000\ \forall t<T-k\text{ and }\forall k<T\,.(2)

While obtaining accurate estimates of the joint probability distributionsp​(𝒙t(k))p(\bm{x}_{t}^{(k)})andp​(𝒙~t(k))p(\tilde{\bm{x}}_{t}^{(k)})is practicable for lowkk(e.g., the typical time-delay phase space corresponding tok=1k=1), estimating high-dimensional probability distributions corresponding to largerkkquickly becomes impractical for realistic time-series lengths.
Diverse statistical methods have been developed to more tractably do inference on the time-reversibility condition on finite data (i.e., assess violation of the symmetry condition Eq. (2)) by quantifying changes in time-series properties under time reversal in terms of real-valued statistics or through test statistics that can form the basis of a statistical test for reversibility[22,17].
In this work, we focus on the inference of time reversibility based on a single real-valued summary statistic (or feature) extracted from a time series (i.e., a feature mapf:ℝT→ℝf:\mathbb{R}^{T}\to\mathbb{R}) that aims to encapsulate the deviation from the time-reversibility condition Eq. (2).

The notion of time reversibility has attracted considerable attention in the time-series analysis literature, as it serves as a valuable diagnostic tool in model development and as a means for identifying nonlinearities and non-Gaussianity in the underlying dynamical structure of a system.
A key result established in time-series analysis is that irreversibility reflects departures from linearity and Gaussianity in the underlying process[15].
This relationship has important implications for model development, since time-irreversible dynamics cannot be generated by canonical linear Gaussian time-series models, thus ruling out this ubiquitous class of dynamics[5,23].
Furthermore, reversibility statistics can act as powerful statistical summaries of the dynamical structure of time-series data that can be used for subsequent statistical learning applications like classification problems.
For example, in medicine, reversibility captures differences between healthy controls and patients with epilepsy[24,25,26,27], demonstrating its potential for clinical diagnosis.
Reversibility has also been shown to relate to brain organization and the emergence of wakefulness[21], while serving as an indicator of abnormalities[28,29,30]and nonlinearity[31]in human heartbeat dynamics and hand tremor signals[32].
In economics and finance, time series such as business cycles often exhibit asymmetric structures, typically characterized by long, gradual expansions followed by sharp contractions[33,34], making tests for time reversibility useful for classification[35].
More recently, irreversibility indicators based on autocorrelation functions[36]have revealed scale-dependent time-reversal asymmetry in fully developed turbulence[37]and identified energy transfer from large to smaller structures in turbulent flows[38].

The literature on statistical methods for inferring time-reversal asymmetry from time series is vast, spanning multiple domains and theoretical approaches, and includes a wide range of techniques designed to index time-reversibility from finite time series.
Higher-order cumulants and bi- or polyspectral statistics[39]represent some of the earliest statistical descriptors sensitive to the direction of time, along with asymmetric autocorrelation functions (i.e., forms of autocorrelation that are not invariant under time reversal)[36,40]and foundational tests based on sample bicovariances, developed both in the time[41,42]and frequency domain[43].
Other methods are based on measuring asymmetry in the distribution of consecutive temporal intervals with respect to zero, quantified by the third cumulant of the differencesxt+τ−xtx_{t+\tau}-x_{t}[22], including for processes with long-range dependencies[44], also extended across higher dimensions[45].Dikset al.[17]introduced a reversibility test based on the invariance of the distribution of delay vectors𝒚n=(xn,xn+τ,…,xn+(m−1)​τ)∈ℝm\bm{y}_{n}=(x_{n},x_{n+\tau},\dots,x_{n+(m-1)\tau})\in\mathbb{R}^{m}, built from a time series𝒙\bm{x}and across various embedding dimensionsmmand lagsτ\tau, under time reversal.
In two-dimensional embeddings(xt,xt+τ)(x_{t},x_{t+\tau}), the reversibility condition, Eq. (2), implies symmetry about the identity line, a property that is harder to visualize in higher dimensions, where it must still hold for allmmandτ\tau.
This phase-space symmetry underlies established irreversibility measures based on time-series increments[46,47,29], which consider the probabilities of rises and falls in the time series.
Following a similar rationale,Costaet al.[28]proposed a computational method based on coarse-graining time-series increments at different resolutions, thereby incorporating physical assumptions and extending the quantification of irreversibility across multiple temporal scales.
A nonlinear predictor was also used for irreversibility detection by comparing forecasting performance a fixed number of steps ahead in both the forward and backward dynamics[23].
Other approaches transform time series into alternative representations (such as symbolic sequences or network structures) which are then analyzed using tools from symbolic dynamics[48], graph theory[49,50], or information theory[51].

Here, we focus on two key limitations of the existing literature on time reversibility: its fragmentation across multiple disciplines, and the tendency for methods to be studied in isolation and evaluated on small, hand-selected sets of systems.
Addressing these limitations would yield several benefits in the literature which include clarifying conceptual relationships across results, highlighting common underlying interpretations rather than isolated outcomes, and enhancing constructive communication across diverse fields.
The breadth of algorithmic contributions to the time-reversibility literature—developed and adopted over many decades and across fields, each with its own terminology, tools, and notation—has contributed to a disjoint literature leading to a practical ambiguity in how to select an appropriate statistic from this wide array of alternatives.
Since these various methods have been proposed and tested individually, there is currently no systematic framework to guide researchers in selecting appropriate approaches from this vast interdisciplinary methodological literature on irreversibility.
In particular, since the strengths and weaknesses of different formulations of time-series statistical structure have seldom been benchmarked or compared to each other in either discrete-time or continuous-time systems[52,53], it is not well understood which types of approaches are the most powerful at capturing different types of time-reversibility from data, or what the relative strengths and limitations of each method are across systems containing different types of dynamical structure.
From the viewpoint of method development, we lack a unified context in which to assess whether new and promising methods from the broader time-series analysis field can be effectively adapted to tackle the problem of irreversibility.
Furthermore, approaches in the time-series analysis literature are often validated on a limited range of deterministic systems—most commonly the Hénon map, logistic map, and Lorenz system—despite theory on time-reversibility covering a wide range of systems that deviate in a range of different ways from linear Gaussian dynamics.
Benchmarking methods on narrow and inconsistent sets of processes can obscure their relative strengths and weaknesses in capturing the diverse ways irreversibility manifests across systems, including different types of temporal asymmetries and varying timescales.

In this work, we aim to address these issues by empirically evaluating a large library of interpretable statistics to identify those most effective for detecting irreversibility and by unifying existing time-series approaches to time-reversibility analysis.
To this end, we systematically compare and analyze the most comprehensive collection of over 6000 time-series statistics for their ability to capture the time-reversal asymmetry of over 35 diverse processes, spanning a range of formulations and dynamical behaviors (in discrete and continuous time, and encompassing varying degrees of linearity and Gaussianity).
We draw on the extensive interdisciplinary library of time-series statistics contained in the highly comparative time-series analysis package,hctsa[54,55], in which each feature is derived from interpretable time-series theory.
This connection to theory facilitates an understanding of the types of temporal structures (and ways of quantifying them) that diverse scientists have developed to date which are relevant to distinguishing reversibility.
The highly comparative, data-driven approach to methodological comparison has yielded new understanding and guided the selection of novel time-series methods for a wide range of applications—identifying features most associated with altered intrinsic brain dynamics in epileptic patients[56], discovering novel heart rate variability metrics[57], and demonstrating the utility of some established time irreversibility features in distinguishing zebra finch songs[58].
It has also facilitated the development of new theory for challenging empirical problems like tracking the proximity to criticality in near-critical systems with unknown noise levels[59].
Here we apply this approach to the problem of time reversibility for the first time to develop a unified understanding of the relative strengths and weaknesses of different types of time-series analysis methods across different types of dynamical processes, allowing us to synthesize the array of disparate prior work on this topic.

The paper is organized as follows.
In Sec.II, we introduce our highly comparative time-series analysis approach for detecting irreversibility.
We describe how we generate synthetic data from various simulated processes and outline the procedure for extracting time-series features.
The results of our analysis are presented in Sec.III.
We differentiate between features that are insensitive to the direction of time across all simulated processes (Sec.III.1) before focusing on the subset of high-performing statistical indicators of irreversibility (Sec.III.2).
We provide a detailed interpretation of the identified families of well-performing features, with particular emphasis on generalized autocorrelation functions, symbolic measures, and forecasting-based statistics.
After identifying and interpreting the top-performing features, we compare their effectiveness in distinguishing between reversible and irreversible dynamics across different processes in Sec.III.3.
Finally, in Sec.IV, we provide concluding remarks, discuss strengths and limitations of our data-driven methodology, and draw future directions for the problem of irreversibility detection from time-series data.

## IIMethods

This paper takes a highly comparative approach to understanding types of time-series analysis approaches that are useful for inferring irreversibility from time-series data.
Our data-driven methodology is illustrated schematically in Fig.1and can be summarized in three main steps:
(i) generation of time-series data by simulating stochastic processes and dynamical systems with known time-reversal properties (depicted in Fig.1).
The set of 35 simulated processes is introduced in Sec.II.1and further elaborated in Sec.II.2, where implementation details are also provided (see AppendixA);
(ii) evaluation of a comprehensive set of time-series features to identify those most sensitive to temporal asymmetry (depicted inFigs.˜1and1).
The procedure for feature extraction and the scoring framework used to highlight the most informative features are described in Sec.II.3; and
(iii) interpretation of top-performing features to understand how they quantify different types of temporal patterns associated with irreversibility (see Sec.III).\phantomsubcaption\phantomsubcaption\phantomsubcaptionFigure 1:Schematic of our data-driven approach to identifying high-performing time-series statistics that can accurately index irreversibility from time-series data.(a) Time series generation:To include multiple and diverse sources of irreversibility, we simulated50005000-sample time series from a comprehensive library of 35 discrete-time and continuous-time processes with known reversibility properties.
Each panel shows selected illustrative time series segments from a given process class, with a [R] indicating ‘reversible’ and a [I] indicating ‘irreversible’, placed near the process label according to the reversibility specified in Table1.
We use a consistent color coding throughout the paper to identify these families of simulated processes.(b) Extraction of time-series features:For each time series𝒙\bm{x}, we constructed its time-reversed counterpart𝒙~\tilde{\bm{x}}by reversing the order of the data points, as per prior work[18,19,20,21].
To find time-series properties that are sensitive to irreversibility, we systematically computed a large set of>6000>6000interpretable time-series features implemented in thehctsalibrary[55].
In this way, each time series was summarized by a set of real numbers,f1,…,f6082f_{1},\dots,f_{6082}, that encode a broad range of its statistical properties.
As an ansatz for the ability of each time-series featurefif_{i}to index a difference in statistical properties between the original time series𝒙\bm{x}and the time-reversed time series𝒙~\tilde{\bm{x}}, we quantified the absolute difference between the feature value computed on𝒙\bm{x}and𝒙~\tilde{\bm{x}}, as|Δ​fi|=|fi−f~i||\Delta f_{i}|=|f_{i}-\tilde{f}_{i}|.(c) Assign each feature a score:To extract time-series properties that are sensitive to the reversibility of processes, each featurefif_{i}was scored based on the discriminative power of its|Δ​fi||\Delta f_{i}|in classifying time series generated by reversible [R] and irreversible [I] processes using a 1-nearest-neighbor classifier (1-NN) with leave-one-out cross-validation; the classification accuracy served as the feature’s score. We expect that an informative featurefif_{i}, associated with a high classification accuracy, displaysΔ​fi≈0\Delta f_{i}\approx 0for reversible processes and large deviations|Δ​fi|>0|\Delta f_{i}|>0for irreversible ones, yielding well-separated distributions across the dataset.

## II.1Model systems

A core component of our data-driven method is a way to meaningfully score each time-series feature on its ability to distinguish time series generated by reversible versus irreversible processes.
For such a scoring process to be useful, the set of systems we test on should be sufficiently diverse to capture as wide a range of dynamical signatures of irreversibility that are exhibited by different classes of dynamical processes.
By contrast, if our set of systems were too small or specific, features could score well by capturing idiosyncratic properties of specific processes, instead of the broader characteristic of irreversibility.
To this end, we generated a collection of univariate, stationary time series simulated from 35 reversible and irreversible systems (we simulated 100 time series from each system), yielding a dataset of 3500 time series for studying irreversibility that contains the most comprehensive coverage of processes to date (to our knowledge).
Our collection includes a broad range of both stochastic and deterministic, discrete- and continuous-time processes, subdividing processes that share similar dynamics into families, as summarized in Table1and illustrated in Fig.1, where each panel corresponds to a family of simulated processes consistently color-coded throughout the paper.
In selecting processes to incorporate in this work, we aimed to include coverage of as many diverse dynamical behaviors as possible, while generally aligning with the parameter settings used in previous studies to ensure a consistent reference for evaluating the reversibility of the simulated systems.
In labeling each system as either ‘reversible’ or ‘irreversible’, we could, in some cases, rely on prior knowledge of the process (as per the reversible i.i.d. noise processes), but in other cases relied on existing literature on irreversibility and systems that have been used to assess time-reversibility metrics to base the assessment.

Given that the dynamics of real-world systems are often modeled in the existing literature using ordinary or stochastic differential equations, we included continuous-time processes in our analysis alongside discrete-time formulations.
When treated computationally, however, numerical solutions to such systems inevitably involve approximations or truncations[60], as further discussed in Sec.II.2.
Despite the added complexity of numerically handling continuous-time systems compared to their discrete-time counterparts, including representative examples of these systems is essential to capture dynamics with varying time-scale dependencies and to evaluate the robustness of individual statistics.
Overall, we included 35 diverse systems: 15 reversible systems and 20 irreversible systems.
The motivation for including each type of dynamics, along with references to prior work used to assess their reversibility, is presented below, while details of the simulated systems are provided in AppendixA.Table 1:Summary of simulated processes grouped into six families, with a color coding that is used throughout the paper.
Each process is labeled with an abbreviation for ease of reference.
The discrete- or continuous-time nature of the simulated process is indicated by ‘D’ for discrete and ‘C’ for continuous.
The reversibility of each system is indicated by ‘R’ for reversible and ‘I’ for irreversible (assigned based on either referenced prior studies or from ground truth knowledge of the process; cf. AppendixAfor details for specific systems).Family of processesProcessLabelDiscrete/ ContinuousReversibilityNoiseGaussian noise[17]GNODRUniform noise[17]UNODRPink noise[20]PINKDRRed noise[20]REDDRViolet noise[20]VIOLETDRAutoregressive modelsAR(1) with i.i.d. Gaussian noise[15,17]AR1_GNODRStatic transformation of AR(1) with i.i.d. Gaussian noise[15,17]STARDRAR(1) with i.i.d. uniform noise[17]AR1_UNODIARMA(1,1) with i.i.d. uniform noiseARMA11_UNODIAR(3) with noise sampled from a Gamma distributionAR3_GAMMADISETAR(2;1,1,1)111Self-Exciting Threshold Autoregressive Model[61]SETAR1DISETAR(2;2,2,2)[62]SETAR2DINonlinear AR(2) with non-Gaussian noise[62]NAR2DIDeterministic chaotic mapsArnold’s Cat map[49]ARNOLDDRChirikov standard map[8]CHIRIKOVDRHénon map[17,36]HENDIQuadratic map[51]QUADDILogistic map (r=4r=4)[23,49,18]LOGISTIC_4DILogistic map (r=3.8284r=3.8284)[18]LOGISTIC_38DISum of deterministic chaotic maps/flowsSum of Hénon maps, one forward and the other reversed[17]HENR_DIVERSEDRSum of Hénon map and its reversedHENR_SAMEDRSum of a quadratic maps, one forward and the other reversed[51]QUAD_RSUMDRSum of Hénon maps[17]HEN_SUMDISum of Lorenz[36,23,62]LORENZ_SUMCISum of Rössler[62]ROSSLER_SUMCIOther deterministic modelsLinear model with logistic noise source[17]LLOGDIModulus-1 model[17]MOD1DIVan der Pol oscillator[36]VDPCIOscillatorOSCILLATORCRMackey–Glass[50]MG17CIOther stochastic processesStochastic sine mapSINE_MAPDIOrnstein–Uhlenbeck[49]OUCRBounded random walkBRWCRStochastic Van der Pol oscillatorSTOCH_VDPCISum of stochastic LorenzSTOCH_LORENZ_SUMCI

## Noise.

We included both uncorrelated (i.e., white noise) and long-range correlated (i.e., colored noise) stochastic processes under a common class labeled ‘noise’ in Table1for convenience, as a class of processes that lack any deterministic component.
We simulated time-series realizations of independent and identically distributed (i.i.d.) noise processes drawn from both a Gaussian (labeledGNO) and a uniform distribution (labeledUNO).
Time series consist of uncorrelated datapoints, drawn from a fixed distribution, leading to invariant joint distributions under time reversal, indicating that time series are statistically reversible.
Given the ground-truth knowledge of their reversible nature, these processes serve as canonical examples in empirical studies of time symmetry[17,20].
In addition, we included three colored noise processes, generated as time series with a given power spectrum: pink noise (labeledPINK), red noise (labeledRED), and violet noise (labeledVIOLET).
Since the power spectrum is insensitive to temporal irreversibility due to its inherently time-reversal symmetric construction[40], colored noise processes are reversible.

## Autoregressive processes.

We analyzed time series generated from a set of autoregressive-moving-average (ARMA) models with different linearity and Gaussianity properties, focusing on two reversible and six irreversible processes, as summarized in Table1.
The theoretical foundation of reversibility in linear stochastic processes—established in the seminal work ofWeiss [15], which established a link between Gaussianity, linearity, and time-reversibility—makes these processes canonical for studying numerical methods for indexing reversibility.
As representatives of reversible processes, we considered a first-order autoregressive process with Gaussian noise (labeledAR1_GNO) and, given that the reversibility of a linear stochastic Gaussian process is preserved under any point transformation[15], a second process obtained by applying a static nonlinear transformation to the first (labeledSTAR)[17].
Although nonlinearities or non-Gaussianities alone do not guarantee the irreversibility of linear stochastic processes[15,22], we accounted for modifications of standard linear Gaussian processes whose irreversibility has been established in prior studies[17,61,62].
We examined three irreversible autoregressive models with non-Gaussian noise distributions: a first-order autoregressive process AR(1) with uniform noise (labeledAR1_UNO)[15,17], a first-order autoregressive and moving average process ARMA(1,1) (labeledARMA11_UNO)[15]and a more complex form of linear dynamics which accounts for longer memory dependencies combined with noise from a Gamma distribution, implemented through a third-order autoregressive process, AR(3) (labeledAR3_GAMMA).
Next, we simulated three nonlinear variants of autoregressive models by introducing nonlinearities either through regime switching[63]or through equations involving squared terms and other functional forms.
Specifically, we included two variants of the Self-Exciting Threshold Autoregressive, SETAR, model previously identified as irreversible (labeledSETAR1andSETAR2)[61,62], and a nonlinear second-order autoregressive process, AR(2) (labeledNAR2)[62].

## Deterministic chaotic maps.

Motivated by prior work investigating the relationship between reversibility and chaos[8], we included various examples of chaotic dynamics[36,17,49,18,23,51](see Table1).
Despite the conceptual distinction between reversible and conservative dynamics[8], we included two representative discrete-time examples of chaotic maps that are both measure-preserving and reversible, namely the Arnold’s Cat map (labeledARNOLD)[49]the Chirikov standard map (labeledCHIRIKOV)[8], as well as four that are dissipative and irreversible: the Hénon map (labeledHEN)[17,36], the quadratic map (labeledQUAD)[51], and the logistic map in two chaotic regimes (labeledLOGISTIC_4andLOGISTIC_38, respectively)[18,23,49].

## Sum of deterministic chaotic maps/flows.

In Table1we included linear combinations of realizations of discrete-time chaotic dynamics as an interesting extension to investigate how reversibility changes between individual realizations and their linear combinations (e.g., from the irreversible nature of the Hénon map to the reversible nature of the linear combination between a realization and its time-reversed counterpart[17]).
Specifically, we generated diverse linear combinations derived from the Hénon and quadratic maps, including both: (i) combinations of forward realizations that preserve the irreversible dynamics characteristic of these processes (labeledHEN_SUM)[17]; and (ii) combinations of a forward realization with time-reversed versions, which yield reversible dynamics (labeledHENR_DIVERSEwhen the reversed series is a distinct realization, andHENR_SAMEwhen the reversed series corresponds to the same realization, andQUAD_RSUMwhere the reversal is generated from a diverse realization)[17,51].

To enrich our dataset with continuous-time processes, we included linear combinations of thexx,yy, andzzcomponents of the dynamics of two canonical examples of continuous-time chaotic flows: the Lorenz[36,23,62](labeledLORENZ_SUM) and Rössler (labeledROSSLER_SUM)[62]systems (see Table1).
We labeled these linear combinations as ‘irreversible’ as they contain components that prior work has demonstrated to be irreversible; that is any irreversible component yields a violation to the time-reversibility condition.

## Other deterministic models.

To incorporate other nonlinear and deterministic non-chaotic processes in our analysis, we implemented two models whose irreversible character has been previously studied byDikset al.[17]: a linear model with deterministic noise (labeledLLOG) and a modulus-1 process (labeledMOD1) (see Table1).

We included two kinds of continuous-time dynamic behaviors that extend beyond first-order ordinary differential equations: those described by second-order differential equations and those governed by delay differential equations.
As representative of dynamics described by second-order differential equations, we included a reversible linearized oscillator (labeledOSCILLATOR), a prototypical example often used to intuitively introduce the concept of reversibility, and an irreversible Van der Pol oscillator (labeledVDP)[36].
Physical systems characterized by time delays are particularly interesting from the perspective of reversibility, as their dynamics explicitly depend on past values; accordingly, our dataset simulated time series from the nonlinear time-delayed Mackey–Glass equations (labeledMG17)[50].

## Other stochastic processes.

Our dataset also encompasses stationary random walks, as well as chaotic and oscillatory dynamics corrupted by i.i.d. noise (see Table1).
A discrete-time process for which we analyze the irreversibility consists of a nonlinear deterministic map perturbed by additive non-Gaussian noise (labeledSINE_MAP).

In continuous-time, we included two examples of reversible random walks, namely the widely studied time-reversible Ornstein–Uhlenbeck process (labeledOU)[49]and a bounded random walk (labeledBRW).
To study the effect of stochastic fluctuations on the reversibility of dynamical systems, we examine two irreversible systems—the sum of thexx,yy, andzzcomponents of the Lorenz system (labeledSTOCH_LORENZ_SUM), and the Van der Pol oscillator (labeledSTOCH_VDP)—perturbed by noise, which we label as ‘irreversible’ based on the their underlying deterministic dynamics.

## II.2Time-series generation

To evaluate the performance of each time-series feature at distinguishing the diverse set of 15 reversible and 20 irreversible processes described above, we simulated a total of 100 time series from each process, yielding a combined dataset containing35003500simulated time series.
Continuous-time stochastic processes were simulated by numerical integration using the Euler–Maruyama method[64]with an integration time stepΔ​t=10−2\Delta t=10^{-2}s.
Continuous-time deterministic systems were simulated by numerical integration using the Runge–Kutta–Fehlberg (RKF45) method[65]with a default integration stepΔ​t=10−2\Delta t=10^{-2}s (with two exceptions:Δ​t=1\Delta t=1s for the Mackey–Glass system (MG17), which is sufficient to resolve the dynamics relative to the characteristic timescale set by the delay parameter, andΔ​t=10−3\Delta t=10^{-3}s for the bounded random walk (BRW), chosen to balance numerical accuracy and computational efficiency).
Time series were simulated using the Python language (version 3.12.4), except for colored i.i.d. noise series for which we used MATLAB 2020a.

For our main analyses, we selected a time-series length ofT=5000T=5000samples for all systems, striking a compromise between being sufficiently long (to enable complex methods to capture signatures of irreversibility), while remaining realistic for many empirical applications involving finite data.
To avoid transient effects of the initial condition, for discrete-time processes we initially simulated 10,000 samples and then discarded the first 5000 samples, resulting in theT=5000T=5000sample time series analyzed here.
For the continuous-time case, we first simulated each continuous-time process over a sufficiently long time interval (accounting for the fact that the number of samples is inversely proportional to the integration step) to discard the initial transient.
We confirmed that this transient duration exceeded the longest characteristic timescale (estimated as the first zero-crossing of the autocorrelation function) for all systems in our simulations, indicating that it is sufficient to eliminate any dynamics related to the initial condition of any given simulation, which are specified for each model in AppendixA.
To ensure that all processes were sampled on a relatively comparable timescale relative to the dynamics of the process (and avoid substantial under-sampling or over-sampling, which can bias many time-series statistics operating over relatively short temporal lags), we downsampled time series generated from continuous-time processes by reducing its sampling rate of an integer factormm, chosen as the temporal lag at which the autocorrelation function decays to1/e1/e.
While this approach of estimating a ‘correlation length’ is more naturally suited to stochastic processes, using this common processing heuristic for all continuous-time processes allowed us to effectively tackle the problem of setting a sampling rate that similarly resolves the relevant dynamical correlations for both deterministic and stochastic systems.
After downsampling, we retained the firstT=5000T=5000samples of each series.
The sensitivity of results to this time-series lengthTTis analyzed briefly for selected time-series features in AppendixB.

## II.3Feature extraction

From our diverse library of simulated time series from reversible and irreversible processes, we aimed to identify and characterize the types of time-series analysis methods that can most effectively distinguish the two types of dynamics.
To this end, we adopted a highly comparative, data-driven framework, which involved systematically evaluating>7000>7000candidate time-series features from thehctsatoolbox (version 1.09)[54,55]using MATLAB 2020a.
Each feature corresponds to a single real-valued statistical summary of aTT-sampled long time-series property,f:ℝT→ℝf:\mathbb{R}^{T}\to\mathbb{R}(T=5000T=5000here), and is typically computed after z-scoring the time series prior to feature extraction.
Examples of features implemented inhctsainclude statistics of the distribution of time-series values (including outlier measures), diverse measures of linear and nonlinear temporal correlation structure, as well as a range of complexity and dimensionality metrics[55].
The time-series feature-extraction process is illustrated in Fig.1.
In particular, for each simulated time series𝒙=(x1,…,xT)\bm{x}=(x_{1},\dots,x_{T}), we constructed its time-reversed counterpart,𝒙~=(x~1,…,x~T)\tilde{\bm{x}}=(\tilde{x}_{1},\dots,\tilde{x}_{T})by reversing the order of the data points,x~t=xT+1−t\tilde{x}_{t}=x_{T+1-t}, as per prior work[18,19,20,21].
We then extracted the same set of77967796features from both𝒙\bm{x}and𝒙~\tilde{\bm{x}}, yielding two feature vectors:𝒇={fi}i∈ℕ\bm{f}=\{f_{i}\}_{i\in\mathbb{N}}and𝒇~={f~i}i∈ℕ\tilde{\bm{f}}=\{\tilde{f}_{i}\}_{i\in\mathbb{N}}, in which each entry of each feature vector corresponds to the output of some interpretable time-series analysis algorithm.
After removing features that could not be successfully evaluated across the entire dataset (i.e., all forward and all time-reversed time series), we obtained a consistent set of60826082time-series features used throughout the remainder of this work.

Given the set of candidate features, our next goal was to identify those which are most effective for detecting reversibility.
To this end, we adopted theansatzthat the top-performing statistics can be identified via a test statistic defined for each featurefif_{i}(withi=1,….,6082i=1,....,6082) as the absolute difference between the values computed on the original and time-reversed time series:|Δ​fi|≡|fi−f~i|.|\Delta f_{i}|\equiv|f_{i}-\tilde{f}_{i}|\,.(3)

Intuitively,|Δ​fi||\Delta f_{i}|captures the discrepancy in a given statistical propertyfif_{i}between the original and time-reversed series, and can thereby capture a source of statistical irreversibility.
The construction in Eq. (3) is motivated by the similar form used in previous test statistics for reversibility (e.g., the ‘TR test’ statistic[42], or correlation-based measures[36]).
Note that|Δ​fi|=0|\Delta f_{i}|=0corresponds tofi=fi~f_{i}=\tilde{f_{i}}and thus time-reversal invariance, where a given time-series propertyfif_{i}is evaluated identically for both𝒙\bm{x}and𝒙~\tilde{\bm{x}}.
Since we expect|Δ​fi|≈0|\Delta f_{i}|\approx 0for reversible processes, discriminating statisticsfif_{i}for irreversibility should be able to capture deviations from the conditionΔ​fi=0\Delta f_{i}=0in the case of irreversible dynamics.
Significant deviations from zero reflect the ability of the statistic to capture the statistical change in a time series under time reversal.
Note that, since the sign ofΔ​fi\Delta f_{i}is unrelated to the goal of assessing deviations from theΔ​fi≈0\Delta f_{i}\approx 0condition, taking the absolute value as|Δ​fi||\Delta f_{i}|provides us with a desired test statistic for indexing a deviation from reversibility.

As illustrated in Fig.1, we next aimed to develop a scoring statistic to evaluate featuresfif_{i}for which|Δ​fi||\Delta f_{i}|is highly discriminative of time series generated from reversible versus irreversible processes.
To this end, we used the performance of a 1-nearest neighbor (1-NN) classifier in the space of each featurefif_{i}, evaluated using a leave-one-process-out cross-validation strategy.
For a given featurefif_{i}, this approach consists of matching each time series to that with the closestfif_{i}value (1-NN), while excluding all time series generated from the same process (leave-one-process-out).
The resulting performance score forfif_{i}is then computed as the rate at which the matches were correctly assigned to time series of the same (‘reversible’/‘irreversible’) label.
This leave-one-process-out exclusion prevented overly optimistic performance estimates that could arise from a feature simply capturing characteristic properties of a given process (rather than more general statistical structure related to irreversibility).
Note that, to avoid bias from the arbitrary ordering of systems, when multiple points had the identical distance to the query point for 1-NN, the matching neighbor was selected randomly.

As explained above, since|Δ​fi|≈0|\Delta f_{i}|\approx 0for reversible processes, in practice, high-performing features are those for which|Δ​fi||\Delta f_{i}|deviates substantially from zero for a wide range of irreversible processes, resulting in irreversible time series tending to match (via leave-one-process-out 1-NN) to other irreversible processes.
We thus found this 1-NN heuristic scoring procedure to be a suitable empirical metric with which to identify time-series features that were discriminative of irreversibility.

All code required to generate the time series and reproduce the analyses presented in this paper is openly available on GitHub at[66].
The supporting data for the simulations presented in this article are available from Zenodo[67].

## IIIResults

In this work, we aim to develop a unified understanding of the most successful types of existing time-series analysis approaches for inferring the reversibility or irreversibility of a process from a finite time series realization𝒙\bm{x}.
In this section and throughout the remainder of this work,𝒙\bm{x}refers to z-scored time series data.
As depicted in Fig.1, our data-driven approach involves comparing over 6000 time-series features on their ability to distinguish time series generated from a comprehensive range of 35 reversible and irreversible processes, using a derived statistic capturing the difference between the feature computed from the forward (ff) versus reversed (f~\tilde{f}) time series, as|Δ​f||\Delta f|, Eq. (3).
In Sec.III.1, we first characterize time-series features that are invariant to a time-reversal transformation (i.e., yieldingΔ​f≈0\Delta f\approx 0for all time series tested) and interpret them with respect to their underlying time-symmetric constructions.
Next, in Sec.III.2, we characterize the range of existing and novel time-series analysis methods that are most successful at quantifying irreversibility, and explain the algorithmic structures that underlie their strong performance.
Finally, in Sec.III.3, we demonstrate that there is no optimal summary statistic for capturing irreversibility from time-series data in general; rather, all features we tested have strengths and weaknesses that depend on how the irreversibility of a given process manifests.

## III.1Time-reversal invariant time-series features

We first aimed to characterize the type of time-series features that are invariant under the time-reversal transformation of a time series.
Such time-reversal-invariant features are interesting to characterize initially because they provide a foundation from which we can later understand features that can distinguish the direction of time.
Well-known time-reversal-invariant time-series statistics include properties of the distribution of time-series values (e.g., mean), which disregard the sequential ordering in the data (and so are insensitive to any permutation, including time reversal), and simple two-point linear autocorrelation statistics for some lagτ\tau, as⟨xt​xt+τ⟩\langle x_{t}\,x_{t+\tau}\rangle, where⟨⋅⟩\langle\cdot\rangledenotes the temporal average over the time series (and statistics of the related Fourier power spectrum, cf. the Wiener–Khinchin theorem[68])[36,5,40].
Note that the time-reversal symmetry of the two-point linear autocorrelation statistic can be determined straightforwardly by considering the equivalence of the terms in the average that makes up⟨xt​xt+τ⟩\langle x_{t}\,x_{t+\tau}\rangleor, for a time series of finite lengthTT, by explicitly analyzing a time-reversal transformation (ast↦T−t−τ+1t\mapsto T-t-\tau+1, cf. AppendixCfor details).

To generate a candidate list of time-reversal-invariant features from our set of60826082tested time-series statistics, we identified those featuresfif_{i}that gaveΔ​fi≈0\Delta f_{i}\approx 0across all tested time series, corresponding to giving identical outputs (approximately, within numerical error) when applied to each original time series𝒙\bm{x}and its time-reversed version𝒙~\tilde{\bm{x}}.
To account for numerical error, we used the heuristic criterion|Δ​f¯|<5​ε|\overline{\Delta f}|<5\varepsilon, where⋅¯\overline{\cdot}denotes the average over all time series andε=2.2×10−16\varepsilon=2.2\times 10^{-16}is the floating-point precision in Python.
This yielded a set of14141414time-reversal-insensitive time-series features (see Supplemental Material Table S1 for full list).

This set of time-reversal-insensitive features includes expected distributional properties (e.g., mean, median, standard deviation, and quantiles) and two-point linear autocorrelation statistics (and related properties of the power spectrum), as well as a range of conceptually related statistics with time-symmetric constructions.
These include symmetric generalizations of autocorrelation functions (which we refer to as generalized autocorrelations, introduced later in Sec.III.2.1), measures of symmetric patterns of time-series rises and falls (analyzed in more detail in Sec.III.2.2), some information-theoretic statistics such as auto-mutual information[69](which is time-reversal symmetric for the same reason as the two-point linear autocorrelation statistic), and some statistics of the degree distribution derived from the undirected horizontal visibility graph[70](note that subsequent developments have introduced directionality to network edges to capture irreversibility[49]).

Our results recapitulate prior literature on statistics that capture a diverse range of time-series properties but are trivially insensitive to irreversibility due to an invariance under the time-reversal transformation—either by insensitivity to temporal ordering (as distributional measures), or via a time-symmetric construction.
These time-symmetric constructions will be explored in greater detail, and contrasted with time-asymmetric constructions in Sec.III.2.

## III.2Time-series statistics of reversibility\phantomsubcaption\phantomsubcaptionFigure 2:Identifying high-performing and interpretable time-series features for detecting irreversibility through large-scale empirical testing of thousands of features on 35 reversible and irreversible processes.(a)Distribution of cross-validated classification accuracy (of distinguishing reversible from irreversible processes) across46684668features (excluding14141414that are insensitive to reversibility, cf. Sec.III.1).
Each featurefif_{i}was assessed independently on its ability to distinguish time series generated from reversible versus irreversible processes via the absolute difference between its value computed on the time series and its time-reversed counterpart, as|Δ​fi||\Delta f_{i}|(Eq. (3)).
There is a tail in the accuracy distribution, pointing to a subset of high-performing features; here we focus on the127127features with accuracies exceeding72%72\%, annotated as a dashed gray vertical line (see Supplementary Material Table S3 for a full list).(b)Distributions of|Δ​f||\Delta f|across all 3500 time series, separated between 1500 reversible (blue) and 2000 irreversible (red) time series, are shown as box plots for three selected top-performing features:i.the fourth-order cross-moment (an example of generalized autocorrelation-based feature)C1,3​(𝒙;1)=⟨xt​xt+13⟩C_{1,3}(\bm{x};1)=\langle x_{t}\,x_{t+1}^{3}\rangle;ii.the symbolic motif feature,puu​(𝒙)p_{\text{uu}}(\bm{x}), which calculates the probability of two consecutive rises in a time series, andiii.the mean absolute error (MAE) of 1-step-ahead predictions made by a second-order autoregressive (AR) model.
Next to each boxplot is a raincloud plot showing the|Δ​f||\Delta f|value for all time series and colored according to process families (defined in Table1), with random horizontal scatter to aid visualization.
Horizontal black lines indicate the zero baseline, while gray dashed lines delimit the range of values of the statistics computed from time series generated by reversible processes.
The generalized autocorrelation (i.), symbolic motif (ii.), and MAE of a 1-step-ahead AR(2) prediction (iii.) are annotated in the distribution in Fig.2.
These three features were chosen as demonstrative examples of broader families of easily interpretable time-reversal-sensitive time-series features, generalized autocorrelations (Sec.III.2.1), symbolic motif probabilities (Sec.III.2.2), and forecasting-based measures (Sec.III.2.3), which are explained in detail in the main text.
Their behavior mirrors that of all top-performing features, exhibiting|Δ​f|≈0|\Delta f|\approx 0for reversible processes but deviating substantially from zero for many irreversible processes.

Having characterized the types of features that are, by construction, invariant under time reversal, we next aim to characterize time-series statistics that are highly effective at quantifying the time-reversal asymmetry present in time series generated from irreversible processes.
Specifically, after removing the14141414time-reversal-invariant features characterized above, we aimed to understand the relative performance of the remaining46684668features (listed in Supplementary Material Table S2) and, in particular, understand the best-performing types of time-series summary statistics for indexing time reversibility.
Recall that we assessed each feature’s ability to capture irreversibility from time-series data according to its accuracy at classifying time series simulated from 35 reversible and irreversible processes (in a leave-one-process-out cross-validation design, cf. Sec.II.3).
We expected effective irreversibility statistics to quantify temporally asymmetric time-series properties that capture the non-Gaussianity and/or nonlinearity of irreversible processes.
This includes traditional measures of nonlinearity[71], statistics based on sample bicovariances (the ‘TR test’ statistic)[42]or higher-order moments[44], asymmetric autocorrelation functions[36], and statistics of symbolic strings computed via symbolization rules applied to real-valued time-series data[48].

The distribution of accuracy values across the46684668candidate time-series features is shown in Fig.2.
We see that the majority of these features are not sensitive to irreversibility, with a large peak around chance accuracy (50%).
This suggests that the majority of features in the time-series analysis literature (as represented by thehctsalibrary[55]) are mainly focused on the statistics of linear, Gaussian processes and are thus insensitive to time-reversal asymmetry.
The distribution of accuracies also exhibits a striking right-skewed tail, indicating the presence of a subset of high-scoring features.
To understand the types of algorithmic approaches that were most effective at indexing irreversibility, we focused on a subset of 127 features with an accuracy exceeding 72% (shown as a dashed vertical line in Fig.2).
This threshold was selected to encompass a sufficiently large set of features for analysis, while retaining a focus on those with the highest accuracy.
This set of high-performing features (listed in Supplementary Material Table S3) is analyzed in the remainder of this paper and encompasses a surprising range of time-series analysis algorithms, including types of statistics that have previously been used to study reversibility (e.g., estimators of higher-order moments and symbolic representations of sequential rise and fall sequences) as well as a range of novel approaches that have (to our knowledge) not previously been used to study reversibility, including the goodness of fit of a range of time-series forecasting models.

To better understand the behavior of highest-performing features, we highlight three representative features that illustrate the different manifestations of irreversibility revealed by our data-driven analysis: (i) the fourth-order cross-moment⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangle(85% accuracy, in Fig.2(i)) which is an example of what we refer to as a generalized autocorrelation feature (defined in Sec.III.2.1); (ii) the probability of two consecutive rises in the time series,puu​(𝒙)p_{\text{uu}}(\bm{x})(73% accuracy, in Fig.2(ii)); and (iii) the mean absolute error (MAE) of 1-step-ahead predictions made by a second-order autoregressive (AR) model (79% accuracy, in Fig.2(iii)).
These three plots show the distributions of absolute feature-value differences|Δ​f||\Delta f|which are, as expected, tightly centered around|Δ​f|≈0|\Delta f|\approx 0for reversible processes, reflecting the equivalence of the statistics of these processes under time-reversal.
In contrast, distributions of|Δ​f||\Delta f|display a substantial deviation|Δ​f|>0|\Delta f|>0for many of the irreversible processes (reflecting an asymmetry between the feature computed on the forward versus time-reversed time series).
Compared to reversible processes (withΔ​f≈0\Delta f\approx 0), time series generated by irreversible processes exhibit a far greater heterogeneity in|Δ​f||\Delta f|values across different types of systems, as indicated by the coloring by process in raincloud points in Fig.2.
In particular, for all high-performing features, there were some irreversible processes for which the source of irreversibility was not captured by the real-valued statistic (i.e., for which|Δ​f|≈0|\Delta f|\approx 0).
This suggests that, among the set of analyzed features, single statistical index of reversibility will be sensitive to only a subset of ways in which irreversibility can manifest in the data, a concept that will be explored in detail in Sec.III.3.

Most high-performing statistics were members of the three conceptual families of time-series analysis methods depicted in Fig.2:
generalized autocorrelation features (defined in Sec.III.2.1, like⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangle, in Fig.2(i));
statistics of rise/fall patterns (likepuu​(𝒙)p_{\text{uu}}(\bm{x}), in Fig.2(ii)); and forecasting-based measures (like the MAE of 1-step-ahead predictions made by a second-order autoregressive model, in Fig.2(iii)).
Accordingly, these three families are explored in depth in dedicated sections Sec.III.2.1, Sec.III.2.2, and Sec.III.2.3.
In addition to these three families of reversibility statistics, a range of miscellaneous time-series statistics were also contained in the high-performing set.
This includes a set of twelve ‘stick-angle’ statistics that compute measures of the angles between successive time-series points that have the same sign (afterzz-scoring).
These statistics were introduced intohctsa[54]and, although they were not designed to capture reversibility, they are highly sensitive to temporal asymmetries in irreversible processes (with accuracies as high as 89%) through their ability to quantify a directional bias in the distribution of angles computed on the positive (or negative) part of the time series generated from irreversible processes.
Another group of 27 high-performing statistics are derived from simulations of a ‘walker’ process.
Of these, 22 rely on dynamical rules based on the time series, which can index temporal asymmetry through a difference in walker dynamics when driven forward through time versus backward in time (with accuracies up to 89%).
The remaining five are based on extreme-value statistics[72], which (loosely) capture irreversibility by comparing the temporal spacing between large deviations from the mean between the forward and reversed series (up to 79%).

In summary, our data-driven evaluation of thousands of time-series features revealed the diversity of existing time-series statistics that can successfully capture temporal asymmetry in a range of irreversible processes.
Different types of time-series methods are able to index different summary statistics that capture the difference between the joint distributions (see Eq. (2)) across a wide range of tested irreversible processes, with three families of approaches—generalized autocorrelation functions, symbolic features, and forecasting-based statistics—encompassing the most powerful families of methods in our test.
We discuss these families in detail in the following sections.
Note that, although our main analyses focus on a single time-series length,T=5000T=5000samples, additional tests on a selected group of top-performing statistics show that results using this time-series length are broadly representative of those which would be obtained for shorter time series.
In particular, we found the forth-order cross-moment feature⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangle, the symbolic featurepuu​(𝒙)p_{\text{uu}}(\bm{x}), and the mean absolute error of an AR(2) predictor, a forecasting-based measure, to be quite robust to changes in the time-series length over the range of 10 to 5000 samples (see Fig.B.1).
We observe that, with around 100 samples, theΔ​f\Delta fappears to have largely converged across all three statistics and all five processes.
These preliminary results suggest that comparable outcomes can be expected with sample sizes as small as approximately 100.

## III.2.1Generalized autocorrelation features

In Sec.III.1, we noted the invariance of the two-point linear autocorrelation statistic⟨xt​xt+τ⟩\langle x_{t}\,x_{t+\tau}\rangleunder time reversal (as well as related statistics of the Fourier power spectrum) since they are defined as averages over products of time-series values separated by a time lagτ\tau, which is preserved under time reversal.
Generalized forms of autocorrelation extend the standard two-point linear autocorrelation by capturing more complex dependencies between points in a time series.
As defined here, these measures encompass a wide range of operations that, under the assumption of stationarity, capture different types of dependencies between local patterns in a time series, including temporal averages of products of data points and linear combinations of functions of those points.
Here, we focus on two classes of features within the family of autocorrelation-based statistics, constructed from different functional forms of time-averages:
(i) as products of time-series data points raised to different powers (e.g.,⟨xt​xt+τ2⟩\langle x_{t}\,x_{t+\tau}^{2}\rangle), or higher-order correlations with unequally spaced time-series points, such as three-point (or multi-point) autocorrelations (e.g.,⟨xt​xt+1​xt+3⟩\langle x_{t}\,x_{t+1}\,x_{t+3}\rangle); and
(ii) as normalized linear combinations of temporal averages of a functionffapplied to time-series points (e.g.,⟨f​(xtα​xt+τβ)⟩−⟨f​(xtα)⟩​⟨f​(xt+τβ)⟩\langle f(x_{t}^{\alpha}\,x_{t+\tau}^{\beta})\rangle-\langle f(x_{t}^{\alpha})\rangle\,\langle f(x_{t+\tau}^{\beta})\rangle).
In our experiments, 24 features derived from this family were in the top-performing set described in Sec.III.2above.

The first group of twelve high-performing features contained features of the formCα,β,γ,…​(𝒙;τ1,τ2,…)=⟨f​(xtα​xt+τ1β​xt+τ2γ​…)⟩,C_{\alpha,\beta,\gamma,...}(\bm{x};\tau_{1},\tau_{2},...)=\langle f(x_{t}^{\alpha}\,x_{t+\tau_{1}}^{\beta}\,x_{t+\tau_{2}}^{\gamma}\,...)\rangle\,,(4)

for some transformation functionf​(⋅)f(\cdot), being either the two-point form⟨xtα​xt+τβ⟩\langle x_{t}^{\alpha}\,x_{t+\tau}^{\beta}\ranglewith unequal exponentsα≠β\alpha\neq\beta(or with an absolute value as⟨|xtα​xt+τβ|⟩\langle|x_{t}^{\alpha}\,x_{t+\tau}^{\beta}|\rangle), or with multiple time lags, such as the three-point form⟨xtα​xt+τ1β​xt+τ2γ⟩\langle x_{t}^{\alpha}\,x_{t+\tau_{1}}^{\beta}\,x_{t+\tau_{2}}^{\gamma}\rangle.
Notably, computing the difference between statistics of this family for the original and time-reversed series effectively captures, among other measures, higher-order moments (i.e., the skewness in the first differencext+τ−xtx_{t+\tau}-x_{t}), which have been effectively employed in prior work to assess irreversibility[22].
Specific examples include⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangle(85% accuracy),⟨xt​xt+23⟩\langle x_{t}\,x_{t+2}^{3}\rangle(79%),⟨xt​xt+33⟩\langle x_{t}\,x_{t+3}^{3}\rangle(75%), and the three-point statistic⟨xt2​xt+1​xt+3⟩\langle x_{t}^{2}\,x_{t+1}\,x_{t+3}\rangle(75%).
Interestingly, features that used an absolute value (to our knowledge not studied previously) exhibited higher performance, including⟨|xt3​xt+1|⟩\langle|x_{t}^{3}\,x_{t+1}|\rangle(87% accuracy) and⟨|xt2​xt+1|⟩\langle|x_{t}^{2}\,x_{t+1}|\rangle(87%).

A second group of twelve high-performing generalized autocorrelation features were constructed according to the ‘generalized linear self-correlation function’ formulation ofDuarte Queirós and Moyano [73].
This function is given byCα,β′​(𝒙;τ)≡⟨|xt|α​|xt+τ|β⟩−⟨|xt|α⟩​⟨|xt+τ|β⟩⟨xt2​α⟩−⟨|xt|α⟩2​⟨xt+τ2​β⟩−⟨|xt+τ|β⟩2,C^{\prime}_{\alpha,\beta}(\bm{x};\tau)\equiv\frac{\langle|x_{t}|^{\alpha}\,|x_{t+\tau}|^{\beta}\rangle-\langle|x_{t}|^{\alpha}\rangle\langle|x_{t+\tau}|^{\beta}\rangle}{\sqrt{\langle x_{t}^{2\alpha}\rangle-\langle|x_{t}|^{\alpha}\rangle^{2}}\sqrt{\langle x_{t+\tau}^{2\beta}\rangle-\langle|x_{t+\tau}|^{\beta}\rangle^{2}}}\,,(5)

for various values of the exponentsα\alpha,β\beta, and the time-lagτ\tau.
This functional form was originally introduced in the study of financial markets, where it was designed to capture multiscale dependencies in traded volume[73].
To the best of our knowledge, the formulation in Eq. (5) has not previously been used to study irreversibility.
Nevertheless, our comparative analysis highlighted twelve statistics of this general form, withτ=1\tau=1and various combinations ofα\alphaandβ\beta(particularlyα=1,2\alpha=1,2andβ=2,5,10\beta=2,5,10), including the highest-performing statistic from this groupC1,2′​(𝒙;1)C^{\prime}_{1,2}(\bm{x};1)(with 88% accuracy).

Having summarized a set of generalized autocorrelation statistics, we now aim to examine why certain generalized autocorrelation measures are insensitive to time reversal (like the two-point linear autocorrelations⟨xt​xt+τ⟩\langle x_{t}\,x_{t+\tau}\rangleand others characterized in Sec.III.1above), while others rank among the highest-performing statistics in our empirical tests.
To this end, we focus on the family of statistics given in Eq. (4) and examine the distinction between generalized autocorrelations with symmetric versus asymmetric constructions.
This distinction provides a useful framework in which to interpret how these families of statistics can efficiently capture relevant differences between the joint distributions computed from the original time series𝒙\bm{x}(p​(𝒙t(k))p({\bm{x}}_{t}^{(k)})) and time-reversed counterpart𝒙~\tilde{\bm{x}}(p​(𝒙~t(k))p(\tilde{\bm{x}}_{t}^{(k)})) (see Eq. (2)) via a real-valued summary, in Eq. (3).
Illustrative examples of symmetric and asymmetric forms of generalized autocorrelation statistics are shown in Figs3and3, where we introduce a comb-like representation of the functions of patterns around a given pointtt.
This diagrammatic representation visualizes products of time-series points in the temporal average: each data point is shown as a segment, with the number of segments in a group indicating its exponent in the statistic and the horizontal separation between groups corresponding to the temporal lagτ\tau, as illustrated in the legend of the upper panels of Fig.3.
As will be elaborated through this section, the comb-like visualization emphasizes the temporal symmetry with respect to the midpoint of these functions in constructions with trivial time-reversal symmetry.

Consider a generalized expression of the simple linear two-point autocorrelation computed from aTT-sample time series𝒙\bm{x}, given byCα,β​(𝒙;τ)≡⟨xtα​xt+τβ⟩,C_{\alpha,\beta}(\bm{x};\tau)\equiv\langle x_{t}^{\alpha}\,x_{t+\tau}^{\beta}\rangle\,,(6)

for positive integer exponentsα\alphaandβ\beta, and time-lagτ\tau.
In this simple case, the construction ofCα,β​(𝒙;τ)C_{\alpha,\beta}(\bm{x};\tau)is asymmetric with respect to time-reversal ifα≠β\alpha\neq\beta, while it reduces to a symmetric form whenα=β\alpha=\beta(where symmetric forms are equivalent under time-reversal).
It is straightforward to expressCα,β​(𝒙~;τ)C_{\alpha,\beta}(\tilde{\bm{x}};\tau)in terms of the original series𝒙\bm{x}via the transformationt↦T−t−τ+1t\mapsto T-t-\tau+1(see AppendixDfor details), yielding the following expression for the absolute difference|Δ​Cα,β​(𝒙;τ)||\Delta C_{\alpha,\beta}(\bm{x};\tau)|:|Δ​Cα,β​(𝒙;τ)|\displaystyle|\Delta C_{\alpha,\beta}(\bm{x};\tau)|=|Cα,β​(𝒙;τ)−Cα,β​(𝒙~;τ)|,\displaystyle=|C_{\alpha,\beta}(\bm{x};\tau)-C_{\alpha,\beta}(\tilde{\bm{x}};\tau)|\,,(7)=|⟨xtα​xt+τβ⟩−⟨xt+τα​xtβ⟩|.\displaystyle=|\langle x_{t}^{\alpha}\,x_{t+\tau}^{\beta}\rangle-\langle x_{t+\tau}^{\alpha}\,x_{t}^{\beta}\rangle|\,.

Symmetric constructions withα=β\alpha=\beta(where the linear autocorrelation, withα=β=1\alpha=\beta=1, is a special case, see Sec.III.1) are trivial in the sense thatΔ​Cα,α=0\Delta C_{\alpha,\alpha}=0, independent of the data𝒙\bm{x}.
By contrast, assigning unequal weights to present and future points, withα≠β\alpha\neq\beta, yields a difference|Δ​Cα,β​(𝒙;τ)||\Delta C_{\alpha,\beta}(\bm{x};\tau)|which is non-zero in general.
Our experiments confirm the ability to use asymmetric constructions ofCα,βC_{\alpha,\beta}, via|Δ​Cα,β​(𝒙;τ)||\Delta C_{\alpha,\beta}(\bm{x};\tau)|, as a powerful class of statistics for distinguishing irreversible processes (for which we can have|Δ​Cα,β​(𝒙;τ)|>0|\Delta C_{\alpha,\beta}(\bm{x};\tau)|>0) from reversible processes (for which|Δ​Cα,β​(𝒙;τ)|≈0|\Delta C_{\alpha,\beta}(\bm{x};\tau)|\approx 0).

The distinction between symmetric and asymmetric forms of three-point (and, more generally, multi-point) statistics depends on both the choice of weights assigned to each data point and the temporal lags separating successive points (see AppendixEfor a general expression of the absolute difference in asymmetric three-point statistics).
This distinction can be visualized through the comb-like representations in Figs3and3, which depict a general formulation of three-point statistics and highlight the contrast between their symmetric and asymmetric constructions.
Examples of symmetric generalized autocorrelation measures are shown in Fig.3, illustrating a general symmetric construction of a three-point correlation statistic of the form⟨xtα​xt+τβ​xt+2​τα⟩\langle x_{t}^{\alpha}\,x_{t+\tau}^{\beta}\,x_{t+2\tau}^{\alpha}\ranglethat encompasses and generalizes the symmetric structure of three example statistics:⟨xt2​xt+12⟩\langle x_{t}^{2}\,x_{t+1}^{2}\rangle,⟨xt​xt+1​xt+2⟩\langle x_{t}\,x_{t+1}\,x_{t+2}\rangle,⟨xt​xt+12​xt+2⟩\langle x_{t}\,x_{t+1}^{2}\,x_{t+2}\rangle.
This general construction highlights two key characteristics: (i) the time points are equally spaced, and (ii) the exponents on the left and right match (while the middle term may be raised to any power).
In contrast, Fig.3shows examples of associated asymmetric constructions, where asymmetry arises from modifying exponents (e.g.,⟨xt​xt+12⟩\langle x_{t}\,x_{t+1}^{2}\rangle), from unequal spacing between successive pairs of data points (e.g.,⟨xt​xt+2​xt+3⟩\langle x_{t}\,x_{t+2}\,x_{t+3}\rangle), or a combination of both (e.g.,⟨xt​xt+12​xt+3⟩\langle x_{t}\,x_{t+1}^{2}\,x_{t+3}\rangle), which is expressed in a general asymmetric form of three-point correlation⟨xtα​xt+τ1β​xt+τ2γ⟩\langle x_{t}^{\alpha}\,x_{t+\tau_{1}}^{\beta}\,x_{t+\tau_{2}}^{\gamma}\rangle.
The same reasoning behind symmetric and asymmetric constructions extends to the generalized autocorrelationCα,β′​(𝒙;τ)C^{\prime}_{\alpha,\beta}(\bm{x};\tau)(Eq. (5)) through the choice of the positive integer exponentsα\alphaandβ\beta.
In particular, our results confirm that the symmetric constructions ofCα,α′​(𝒙;τ)C^{\prime}_{\alpha,\alpha}(\bm{x};\tau)are trivially insensitive to detecting irreversibility from time series, whereas asymmetric forms withβ≠α\beta\neq\alphacan reach high classification accuracies.

The best-performing features in the family of generalized autocorrelations align closely with asymmetric correlation-based statistics proposed in foundational work on time irreversibility, while extending previously studied higher-order moments that also achieve strong performance.
For instance,Pomeau [36]introduced cubic two-point correlation measures such asψ′′​(τ)=⟨xt3​xt+τ−xt​xt+τ3⟩\psi^{\prime\prime}(\tau)=\langle x_{t}^{3}\,x_{t+\tau}-x_{t}\,x_{t+\tau}^{3}\rangle\,, andRamsey and Rothman [42]proposed the well-known ‘TR test’ statistic for measuring asymmetry in business cycles,γ^2,1​(τ)=⟨xt2​xt−τ⟩−⟨xt​xt−τ2⟩\hat{\!\gamma}_{2,1}(\tau)=\langle x_{t}^{2}\,x_{t-\tau}\rangle-\langle x_{t}\,x_{t-\tau}^{2}\rangle\,.
However, in our empirical tests, the best-performing TR test reached a maximum accuracy of only 68% (withτ=2\tau=2).
By contrast, we found that extending these classical measures through additional transformations not previously studied—such as taking absolute values—led to substantial boosts in performance, e.g.,⟨|xt3​xt+1|⟩\langle|x_{t}^{3}\,x_{t+1}|\rangleand⟨|xt2​xt+1|⟩\langle|x_{t}^{2}\,x_{t+1}|\rangle, both reached 87% accuracy.
We also examined a widely used nonlinearity measure introduced bySchreiber and Schmitz [71],trev​(τ)=⟨(xt−xt−τ)3⟩t^{\mathrm{rev}}(\tau)=\langle(x_{t}-x_{t-\tau})^{3}\rangle\,, which is a commonly used statistic for time reversal (and practical proxy for nonlinearity) in the physics-based nonlinear time-series analysis literature[22].
Despite its widespread use in nonlinear dynamics, the classification accuracy of|Δ​tr​e​v||\Delta t^{rev}|remained below 71% in our tests, across five tested values of the temporal lag (τ=1,2,…​5\tau=1,2,\dots 5).
The similar overall behavior of the TR statisticγ^2,1​(τ)\hat{\!\gamma}_{2,1}(\tau)andtrev​(τ)t^{\mathrm{rev}}(\tau)can be explained by the fact that they convey nearly the same information under the assumptions of stationarity and ergodicity,tr​e​v​(τ)=−3​γ^2,1​(τ),t^{rev}(\tau)=-3\,\hat{\!\gamma}_{2,1}(\tau)\,,(8)

as it can be observed by expanding the cube in thetr​e​v​(τ)t^{rev}(\tau)statistic.Chenet al.[34]showed the same calculation using ensemble averages, thus considering that testing reversibility through𝔼​[xt2​xt−τ]=𝔼​[xt​xt−τ2]\mathbb{E}[x_{t}^{2}\,x_{t-\tau}]=\mathbb{E}[x_{t}\,x_{t-\tau}^{2}]is equivalent to testing whether the third moment of the increment seriesyt=xt−xt−τy_{t}=x_{t}-x_{t-\tau}vanishes.
This correspondence is noteworthy because it explicitly connects the TR statistic, originally defined for testing reversibility, with the symmetry of the underlying process distribution, while Eq. (8) provides a practical formulation for evaluating this relationship using empirical data.

In this section, we explained how a wide range of asymmetric constructions of generalized forms of autocorrelation are able to index time-reversal asymmetry in time-series data, including through two-point statistics with unequal exponents (e.g.,⟨xt2​xt+1⟩\langle x_{t}^{2}\,x_{t+1}\rangle), higher-order statistics through the additional freedom introduced by time lags (e.g.,⟨xt​xt+2​xt+3⟩\langle x_{t}\,x_{t+2}\,x_{t+3}\rangle), using additional operations like taking magnitudes (e.g.,⟨|xt3​xt+1|⟩\langle|x_{t}^{3}\,x_{t+1}|\rangle), and through novel functional forms involving time-averages like the financial statisticCα,β′​(𝒙;τ)C^{\prime}_{\alpha,\beta}(\bm{x};\tau)(which achieved the highest accuracy, 88%, but has not previously been used to index reversibility)[73].
This broad family of statistics were among the most successful at quantifying reversibility in our empirical tests, recapitulating existing reversibility statistics from the literature, as well as identifying new forms, such as⟨xt2​xt+1​xt+3⟩\langle x_{t}^{2}\,x_{t+1}\,x_{t+3}\rangle, which generalize earlier constructions by computing, for example, absolute values of the product of time-series data-points[36,41,71].\phantomsubcaption\phantomsubcaption\phantomsubcaption\phantomsubcaptionFigure 3:Time-series features with time-symmetric constructions are invariant to time reversal, while time-asymmetric constructions can be powerful indices of time-reversibility.We illustrate this concept with respect to two families of time-series statistics: (a), (b): generalized autocorrelation functions; and (c), (d): the frequency of patterns of consecutive rises (‘up’: u) and falls (‘down’: d) in a symbolized transformation of the time series.(a)We depict three examples of generalized autocorrelation functions with time-symmetric constructions, visualized diagrammatically using a comb-like representation introduced here.
In this representation, each vertical segment represents a time-series value at a specific timett, the spacing between groups of segments reflects the temporal lag between consecutive feature terms and the number of segments in each group represents the exponent, that is, the number of times a given time-series point contributes to the statistic.
All of these features are symmetric in time with respect to their midpoint, indicated with a vertical dashed red line.(b)Three generalized autocorrelation functions with time-asymmetric constructions are depicted, with the asymmetry arising from the use of different exponents (or non-equally spaced temporal lags).(c)Three example time-symmetric sequences of successive rises (‘up’: u) and falls (‘down’: d) are depicted diagrammatically.
The symmetry of these diagrams about their midpoint, depicted as a red dashed line, corresponds to the second half being the mirror image of the logic negation of the first half (indicated by the NOT operation, which transforms ‘u’ to ‘d’ and vice-versa).(d)Three examples of time-reversal asymmetric symbolic patterns (which are therefore candidates for indexing irreversibility) are depicted.

## III.2.2Symbolic features

The second key family of high-performing time-series statistics that we explore in detail is the group of ‘symbolic features’, which are both well-established for indexing reversibility and straightforward to analyze.
These symbolic features involve transforming a time series𝒙\bm{x}into a sequence of symbols (from a finite alphabet) using a set of coarse-graining rules[48,51,62].
Prior work has explored several symbolic approaches, including coarse-graining the time series based on value thresholds[48], encoding rules that capture relationships between successive time-series values[28], and an analysis of the distribution of all possible symbol permutations of fixed length—known as permutation patterns (or ordinal patterns)[74,75,76].
Among the set of symbolizing transformations included inhctsa, the most effective transformation for capturing irreversibility was the mapping to a two-letter alphabet based on incremental rises and falls in a time series.
This transformation maps each pair of consecutive time-series values to a binary symbol {u,d} (‘up’ and ‘down’) that encodes either a rise (xt+1−xt>0x_{t+1}-x_{t}>0) or fall (xt+1−xt<0x_{t+1}-x_{t}<0) in the time series𝒙\bm{x}, with the symbol ‘u’ (up) denoting a rise and ‘d’ (down) denoting a fall.
From the resulting symbolic sequence, simple statistics can be derived that capture different temporal structures, such as the length of the longest consecutive run of a given symbol or the probability of occurrence of a given sequence.
A simple example is the probability of the two-letter sequence ‘ud’,pud​(𝒙)p_{\text{ud}}(\bm{x}): the probability that the time series𝒙\bm{x}increases in one time step (xt+1>xtx_{t+1}>x_{t}) and then decreases in the subsequent time step (xt+2<xt+1x_{t+2}<x_{t+1}).
Although some symbolic features ranked among the top performers in our tests, their accuracies—generally below 74%—were lower than that of other features (which reached accuracies as high as 89%).
Nevertheless, the success of these simple and interpretable measures in capturing time reversibility, together with the established presence of these symbolic methods in the literature, motivated a deeper analysis to understand why they perform well.

We identified three high-performing symbolic features that involved counting sequence probabilities in a time series:
the probability of rises in the time series,pu​(𝒙)p_{\text{u}}(\bm{x})(72% accuracy), which is a simple normalized index adopted in prior work[30]; and
the probability of two consecutive rises (or of two consecutive falls),puu​(𝒙)p_{\text{uu}}(\bm{x})(andpdd​(𝒙)p_{\text{dd}}(\bm{x})) (both have 73% accuracy).
We also identified five high-performing symbolic indices of irreversibility as the length of consecutive runs of a given symbol, including the excess occurrence of the pattern ‘uu’ (or ‘dd’) relative to a single ‘u’ (or ‘d’), i.e.,puu​(𝒙)−pu​(𝒙)p_{\text{uu}}(\bm{x})-p_{\text{u}}(\bm{x})orpdd​(𝒙)−pd​(𝒙)p_{\text{dd}}(\bm{x})-p_{\text{d}}(\bm{x})(each have 74% accuracy), as well as the mean length of consecutive rises (or falls) and the difference between the mean lengths of consecutive rises and falls (each have 73% accuracy).
Figure2(ii) plots the distribution of|Δ​puu||\Delta p_{\text{uu}}|, the best-performing symbolic feature measuring frequencies of specific symbolic motifs within the series, across all reversible and irreversible time series.
As for all the other irreversibility statistics,|Δ​puu|≈0|\Delta p_{\text{uu}}|\approx 0for reversible processes, but irreversible processes exhibit substantial deviation from zero.

Similar to the symmetric constructions of generalized autocorrelations (Fig.3), symbolic sequences that are symmetric with respect to time reversal are invariant under time reversal, i.e., they trivially yieldΔ​f=0\Delta f=0by construction (independent of data, see results in Sec.III.1).
To clarify what we mean by time-reversal symmetric constructions of symbolic sequences of local rises (u) or falls (d), we note that when a time series is reversed, rises become falls, and vice versa, i.e.,pu​(𝒙)=pd​(𝒙~)p_{\text{u}}(\bm{x})=p_{\text{d}}(\tilde{\bm{x}}).This observation can be formalized using an operator that we call the bitwise ‘logical negation’ operator that mapsu↦d\text{u}\mapsto\text{d}andd↦u\text{d}\mapsto\text{u}.
Accordingly, the sequence probabilities of the time-reversed time series𝒙~\tilde{\bm{x}}can be expressed in terms of the probability of the logically negated sequence in the original time series𝒙\bm{x}: the probability of observing a given sequence in𝒙~\tilde{\bm{x}}is equal to the probability of the corresponding bitwise-negated sequence in𝒙\bm{x}, read in reverse temporal order (i.e., from right to left).
Symmetric sequences are those for which reading the bitwise-negated sequence in reverse yields the original sequence.
Three examples of time-reversal symmetric sequences—‘ud’, ‘udud’, and ‘uudd’—are depicted diagrammatically in Fig.3with lines indicating rises or falls and the midpoint represented as a red dashed line.
For features constructed with this symmetry, the probability of occurrence in the original and reversed time series is identical, for examplepud​(𝒙)=pud​(𝒙~)p_{\text{ud}}(\bm{x})=p_{\text{ud}}(\tilde{\bm{x}}), resulting identically inΔ​pud​(𝒙)=pud​(𝒙)−pud​(𝒙~)=pud​(𝒙)−pud​(𝒙)=0\Delta p_{\text{ud}}(\bm{x})=p_{\text{ud}}(\bm{x})-p_{\text{ud}}(\tilde{\bm{x}})=p_{\text{ud}}(\bm{x})-p_{\text{ud}}(\bm{x})=0.

In contrast to these symmetric sequences, for which their time-reversal corresponds to their logical negation, sequences that do not contain this symmetry have the potential to act as a statistical indicator of time reversibility.
Three specific examples of such asymmetric constructions are illustrated in Fig.3: ‘uu’, ‘uduu’, and ‘uudu’.
For example, for the ‘uu’ motif,puu​(𝒙)p_{\text{uu}}(\bm{x})(the probability of two successive rises in a time series, 73% accuracy), we can use the time-reversal property of rises and falls described above to write:Δ​puu​(𝒙)\displaystyle\Delta p_{\text{uu}}(\bm{x})=puu​(𝒙)−puu​(𝒙~),\displaystyle=p_{\text{uu}}(\bm{x})-p_{\text{uu}}(\tilde{\bm{x}})\,,(9)=puu​(𝒙)−pdd​(𝒙).\displaystyle=p_{\text{uu}}(\bm{x})-p_{\text{dd}}(\bm{x})\,.

This provides an equivalent interpretation ofΔ​puu​(𝒙)\Delta p_{\text{uu}}(\bm{x})as a measure of the difference in frequency between two successive rises versus two successive falls in the original time series𝒙\bm{x}.
Since for a reversible process (with equivalent forward and time-reversed joint distributions, Eq. (2)),puu​(𝒙)p_{\text{uu}}(\bm{x})andpdd​(𝒙)p_{\text{dd}}(\bm{x})have equal expectation, an imbalance betweenpuu​(𝒙)p_{\text{uu}}(\bm{x})andpdd​(𝒙)p_{\text{dd}}(\bm{x})(which yieldsΔ​puu​(𝒙)≠0\Delta p_{\text{uu}}(\bm{x})\neq 0), can thus act as an statistical indicator of irreversibility.
A similar property applies to all asymmetric sequence probabilities, which are capable of capturing deviations from time-reversibility via imbalances of the frequencies of a sequence (e.g., ‘uduu’) and its logical inversion, including the two examples shown in Fig.3(d), withΔ​puduu​(𝒙)=puduu​(𝒙)−pddud​(𝒙)\Delta p_{\text{uduu}}(\bm{x})=p_{\text{uduu}}(\bm{x})-p_{\text{ddud}}(\bm{x})andΔ​puudu​(𝒙)=puudu​(𝒙)−pdudd​(𝒙)\Delta p_{\text{uudu}}(\bm{x})=p_{\text{uudu}}(\bm{x})-p_{\text{dudd}}(\bm{x}).

In summary, symbolic sequences provide a simple yet powerful framework for quantifying time-reversal asymmetries in time-series data.
Similar to generalized autocorrelations, this family of statistics embodies a common symmetry principle while capturing local patterns that may be temporally symmetric (and trivial) or asymmetric (and potentially useful as an index of time-reversal asymmetry).

## III.2.3Forecasting features

The third category of high-performing time-series features we focus on is that involving the simulation of a forecasting algorithm which attempts to predict the future of the time series from its past.
Forecasting algorithms explicitly distinguish the past and future of a time series, and are thus constructed with a directional asymmetry in time.
Despite this, forecasting-based time-series features remain relatively unexplored for this purpose, with the exception of a small number of prior studies (such as the nonlinear prediction model used to detect irreversibility byStoneet al.[23]).
The types of high-performing forecasting-based features identified in our data-driven comparison capture various goodness-of-fit metrics of a fitted forecasting model, including the mean absolute error (MAE), and the variance and Gaussianity of the residuals.
The predictive properties of a time series generated by a reversible process remain the same when observed in the forward and reversed directions of time, but there is an asymmetry in irreversible processes that can be detected by forecasting models.

The highest accuracy achieved by a forecasting-based feature was a measure of the Gaussianity of the residuals of a simple local mean forecaster (predicting the subsequent time step using the local mean of the three prior time points (81% accuracy)).
Other high-performing forecasting-based methods include the goodness of fit of autoregressive (AR) model predictions across various prediction lengths (accuracies in the range 72%–78%), with the best-performing feature (78% accuracy) capturing the goodness of fit of one-step-ahead errors using an AR(2) model.
Other statistics used a range of state-space and GARCH models, and used test statistics from a Kolmogorov–Smirnov test performed on the model residuals (yielding accuracies up to 81%); or nonlinear prediction error (using a two- or three-dimensional time-delay embedding[77], achieving accuracies up to 75%).

Figure2(iii) illustrates the effectiveness of an example feature for this family, the mean absolute error (MAE) of a one-step-ahead prediction from fitting a second-order autoregressive AR(2) model, in being able to index irreversibility.
As before, and consistent with expectation, we see values tightly concentrated around|Δ​f|≈0|\Delta f|\approx 0for reversible processes, and substantial deviations|Δ​f|>0|\Delta f|>0for irreversible processes.

While useful features show|Δ​f|>0|\Delta f|>0for some irreversible processes, we were interested to further investigate the sign of the differenceΔ​f\Delta f, which indicates whether a time series is more easily predictable forward or backward in time.
Intuitively, a time series generated by some irreversible process will be more predictable in the direction corresponding to the underlying rules of the governing dynamic process, which are formulated forward in time.
This is consistent with the claim ofStoneet al.[23]that “theoretically there may be nonlinear systems for which backward predictions might be better than forward predictions, but in practice we have found that such systems, if they exist, must be rare”.
Our results reveal an interesting subtlety to this expectation.
For a sufficiently flexible prediction model, like a nonlinear prediction model (e.g., fitted in a two-dimensional time-delay embedding space[77]), we indeed found a consistent increase in the ability to accurately forecast irreversible processes forward in time (relative to their time-reversed versions).
However, we found counterintuitive results from simpler models, including AR(2) and ARMA(3,1) models, where we found that time-reversal can lead to more accurate predictions for some irreversible processes.
This behavior could be explained by the properties of different types of asymmetries in the(xt,xt+1)(x_{t},x_{t+1})phase plots with respect to thext=xt+1x_{t}=x_{t+1}identity line (which is a hallmark of irreversible dynamics[17]).
One reason may be that the time-reversed series can have properties that better match the assumptions of a simple predictive model.
Relative to the forward-time marginal distributions,p​(xt+1|xt)p(x_{t+1}|x_{t}), time reversal can yield more Gaussian marginals,p​(xt|xt+1)p(x_{t}|x_{t+1}), which can lead to more accurate predictions by simple, strongly parametric models whose assumptions better match the statistical properties of the time-reversed data.

Our results thus highlight an underappreciated class of time-series analysis methods—well-studied algorithms for time-series forecasting—and their ability to capture time reversibility through a difference in predictability in the forward versus time-reversed directions for irreversible processes.
We also report some counterintuitive cases in which some irreversible processes can be more accurately predicted by simple models after time-reversal, due to the reversed series better matching the assumptions of the forecasting model.

## III.3Statistical signatures of irreversibility are highly process-dependent\phantomsubcaption\phantomsubcaption\phantomsubcaption\phantomsubcaptionFigure 4:All statistical time-series features have strengths and weaknesses at detecting irreversibility across different processes, demonstrating the need to tailor statistical summaries to the specific sources of irreversibility in a given process.(a)Box plot with scatter points showing the left-out accuracy of the 127 top-performing features for five representative irreversible processes: autoregressive with uniform noise distribution (AR1_UNO), logistic map (withr=4r=4) (LOGISTIC_4), linear model with logistic map noise (LLOG), noise-driven sine map (SINE_MAP), and a linear projection of the multidimensional Lorenz system (LORENZ_SUM).
Simulation details of the implemented models are in AppendixA.
The generalized autocorrelation feature⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangleis highlighted using a yellow star and the symbolic featurepuu​(𝒙)p_{\text{uu}}(\bm{x})using an orange triangle.
For each process, we computed the minimum and maximum left-out accuracies obtained by the set of top-performing features and compared these values across all irreversible processes. We then highlighted the feature with the lowest maximum accuracy across irreversible processes using a dashed line (corresponding to 99%), and similarly marked the feature with the highest minimum left-out accuracy (29%).
We plot the distribution of absolute feature differences|Δ​f||\Delta f|across: (i) all reversible time series; (ii) the autoregressive process with uniform noise (AR1_UNO); and (iii) the logistic map (withr=4r=4) (LOGISTIC_4), for two example features:(b)generalized autocorrelation⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangle; and(c)the symbolic sequence probabilitypuup_{\text{uu}}.
In both plots, the lower solid line denotes the|Δ​f|=0|\Delta f|=0baseline, while the upper dashed line delineates the maximum of the range of values observed across all time series generated from reversible processes.(d)Distribution of left-out accuracy across 2000 time series from the 20 irreversible processes for five representative features: two forms of generalized autocorrelation, namely the fourth-order statistic⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangleand the ‘generalized linear self-correlation function’C1,2′​(𝒙;1)C^{\prime}_{1,2}(\bm{x};1)[73], reported in Eq. (5), usingα=1\alpha=1,β=2\beta=2, andτ=1\tau=1; the probability of two successive increases (the ‘uu’ pattern) in a time series,puu​(𝒙)p_{\text{uu}}(\bm{x}); the mean absolute error of 1-step-ahead predictions made by a second-order AR model (labeled as ‘MAE AR(2) predictor’); and the standard deviation of the residuals from a nonlinear prediction model (labeled as ‘std dev residuals nonlinear prediction’).

Our results above highlight a range of time-series summary statistics that can index time-reversal asymmetry with high accuracy (up to 89%) across 35 diverse processes.
However, no feature exhibited perfect separation between time series generated from reversible versus irreversible processes, suggesting that there may not exist a general-purpose real-valued summary statistic that can reliably index time-reversibility.
While average accuracy provides a simple index of a feature’s performance, in this section we aimed to understand in more detail the relative strengths and weaknesses of the 127 top-performing features identified above when applied to different types of processes.
This required us to disentangle the relative performance of each feature on each process.
We computed this as the ‘left-out accuracy’, defined for each feature on each irreversible process as the proportion of the 100 time-series realizations correctly classified by the feature (during the testing phase of the 1-NN leave-one-out procedure, cf. Sec.II).

To understand the differential performance of top-performing features on different processes, we computed the distribution of left-out accuracies across the 127 top-performing features for five irreversible processes, selecting one representative process from each of the five families of processes listed in Table1: autoregressive with uniform noise distribution (AR1_UNO);
logistic map (withr=4r=4) (LOGISTIC_4);
linear model with noise being a realization of a logistic map (LLOG);
noise-driven sine map (SINE_MAP);
and a linear projection of the multidimensional Lorenz system (LORENZ_SUM).
Results are shown in Fig.4.
Different processes exhibit varying levels of difficulty.
The irreversibility of some systems is relatively straightforward to detect (e.g.,LLOGandLORENZ_SUM), where a large number of features achieve high left-out accuracies, whereas other more challenging systems (e.g.,SINE_MAP) show substantially lower accuracies.
Nevertheless, for each of the twenty irreversible processes we tested, there was at least one feature that achieved near-perfect classification accuracy (at least 99% left-out accuracy, indicated by the upper dashed line in Fig.4).
This finding demonstrates that, with access to a sufficiently diverse library of time-reversal sensitive time-series statistics, it is typically possible to formulate a real-valued summary statistic that can accurately index the form through which irreversibility manifests in a given process.
Because the target process was left out during feature selection, the good performance of the statistic result from the association of instances of the selected process with that of other irreversible ones—serving, in this sense, as a meaningful ‘index of irreversibility’.
In general, however, only a relatively small subset of the (generally high-performing) features can accurately diagnose the irreversibility, in the sense that they preferentially associate instances of a given process in theΔ​f\Delta fspace with other irreversible processes rather than reversible ones.
Indeed, multiple (of our nominally high-performing) features are unable to distinguish the irreversibility of the process (with a left-out accuracy below chance-level 50%).
Within the limitations of our comprehensive (but non-exhaustive) tests, this indicates that there exist irreversible processes for which any real-valued ‘irreversibility index’ will fail.
In other words, while there may not be an optimala prioriindex of irreversibility (as per the various no free lunch theorems[78]), our results point to the ability to accurately index irreversibility through tailoring a well-chosen statistic to a given irreversible process of interest.

A demonstrative case study of the strengths and weaknesses of any given statistical indicator of reversibility is illustrated in Fig.4for two examples of features analyzed above (see Figs2(i) and2(ii)): the generalized autocorrelation⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangle(marked as an yellow star) and the probability of the ‘uu’ pattern,puu​(𝒙)p_{\text{uu}}(\bm{x})(marked as an orange triangle).
Both features accurately distinguish the irreversibility of the linear model with logistic map noise (LLOG) and the linear projection of the multidimensional Lorenz (LORENZ_SUM) systems (which are generally easier problems for our statistics), but failed for the noise-driven sine map (SINE_MAP) system (a more challenging problem for our statistics).
But the two features displayed complementary strengths and weaknesses for the autoregressive with uniform noise (AR1_UNO) process (for which⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangleis accurate butpuu​(𝒙)p_{\text{uu}}(\bm{x})fails) and the logistic map (r=4r=4) (LOGISTIC_4) process (for whichpuu​(𝒙)p_{\text{uu}}(\bm{x})is accurate but⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\ranglefails).
To elucidate this difference, we plotted the absolute difference|Δ​f||\Delta f|for both features across time-series realizations of these two processes (AR1_UNOandLOGISTIC_4) in Figs4and4.
These plots demonstrate the ability of|Δ​C1,3​(𝒙;1)||\Delta C_{1,3}(\bm{x};1)|to distinguish time series generated from theAR1_UNOprocess but not theLOGISTIC_4process (which have|Δ​C1,3​(𝒙;1)|≈0|\Delta C_{1,3}(\bm{x};1)|\approx 0, and vice-versa for|Δ​puu​(𝒙)||\Delta p_{\text{uu}}(\bm{x})|.

Having characterized the variability of feature performance across individual processes, we now focus on evaluating the relative performance of individual features across the set of simulated processes.
Figure4shows the distribution of left-out accuracies for all twenty irreversible processes across five representative top-performing features which capture temporal directionality in the data in diverse yet effective ways: two forms of autocorrelation discussed in Sec.III.2.1above, namely⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangleand the ‘generalized linear self-correlation function’[73],C1,2′​(𝒙;1)C^{\prime}_{1,2}(\bm{x};1)in Eq.5, the probability of two consecutive rises in the time seriespuu​(𝒙)p_{\text{uu}}(\bm{x}), the mean absolute error of 1-step-ahead predictions made by a second-order AR model (denoted as ‘MAE AR(2) predictor’), and the standard deviation of the residuals given a nonlinear predictor (denoted as ‘std dev prediction error’).
Consistent with their high average accuracies, all features were able to distinguish the irreversibility of the majority of processes, correctly classifying the vast majority of their realizations.
However, each feature exhibits substantial variability in left-out accuracy and, in particular, for each feature there exists at least one process for which it fails to detect irreversibility (using the conservative threshold of having a left-out accuracy below chance level of 50%).

Taken together, our results reveal a marked degree of inter-process variation in a given feature’s ability to detect irreversibility (as assessed empirically here by its ability to preferentially match time series generated from a given irreversible process to that of other irreversible processes).
Each feature encapsulates a specific form of a deviation from time-reversal symmetry (cf. Eq. (2))—e.g., of a given statistical structure and on a given timescale.
Using a single summary statistic in this way represents a data-efficient simplification of the general problem of measuring deviation in the forward versus time-reversed joint distributions directly (cf. Eq. (2)), which becomes impractical to assess (particularly on longer lags) from finite time-series data.
But this simplification comes at the cost of imposing a specific structural form of the irreversibility relative to the wide range of statistical structures through which irreversibility can manifest in general (e.g., departures from linearity and Gaussianity on different timescales).
A given feature will perform well on processes that exhibit a given type of time-reversal asymmetry, but relatively poorly on processes that exhibit a different type of asymmetry.
Our findings thus support the view of irreversibility as a multifaceted phenomenon that cannot be fully captured by any single summary statistic in general, but our results suggest a promising way forward in tailoring summary statistics to a given irreversible process.

## IVDiscussion

In this work we have presented a unified organization of statistical approaches to detecting irreversibility from time-series data by conducting the broadest comparative study of numerical methods to date, allowing us to characterize and identify connections between a wide array of promising numerical techniques.
By systematically comparing over 6000 statistics across 3500 time series, simulated from a wide range of reversible and irreversible systems, we identified methods that:
(i) recapitulate the effectiveness of established reversibility statistics, including⟨xt​xt+13⟩\langle x_{t}\,x_{t+1}^{3}\rangle[36]andpu​(𝒙)p_{\text{u}}(\bm{x})[30];
(ii) suggest useful modifications of classical measures, e.g., using absolute values in⟨|xt​xt+12|⟩\langle|x_{t}\,x_{t+1}^{2}|\ranglerelative to the original test statistic, the TR test statisticγ^2,1​(1)\hat{\gamma}_{2,1}(1)[42];
(iii) demonstrate that statistics originally developed for other purposes can act as powerful metrics of irreversibility, e.g., a formulation of generalized autocorrelation proposed byDuarte Queirós and Moyano [73], or the mean absolute error of 1-step-ahead predictions made by an AR(2) model; and
(iv) highlight novel time-series analysis methods for irreversibility detection that (to our knowledge) have not previously been studied in this context, e.g., a range of forecasting-based statistics, as well as ‘walker’ and extreme-value statistics (Sec.III.2).
We provide a deeper understanding of our findings by analyzing the algorithmic implementation of effective statistics, illustrated with a novel diagrammatic representation for generalized autocorrelation and symbolic statistics (Fig.3), showing that their asymmetric construction allows them to behave as non-trivial identifiers of irreversibility, consistent with previous studies.
Furthermore, the breadth of comparison conducted here, of both analysis methods and systems, allowed us to demonstrate that there is no general ‘best statistic’ that is effective at detecting irreversibility in all systems; but rather that each statistic captures a specific manifestation of irreversibility, expressed as an asymmetry in some underlying property.
This suggests that the summary statistic could in general be tailored to the specific statistical properties that characterize the time-reversal asymmetry of a given process.
Our results also suggest a range of recommendations.
We argue that future work should aim to benchmark the behavior of different irreversibility statistics across a broad range of systems with different irreversibility signatures (rather than focusing on a small number of hand-picked systems)
And rather than developing new statistics, future research may be more productively focus on developing methods to efficiently tailor statistical indices of irreversibility to a given system of interest.
In summary, our comparative analysis offers a broad view of irreversibility as a multifaceted concept and characterizes the myriad types of time-series analysis methods that can powerfully index it, while also providing insights to guide new directions for its analysis from time-series data.
This will be especially useful for emerging applications of time-irreversibility metrics, including in applications of non-equilibrium statistical thermodynamics, and in inferring and understanding how time-asymmetric structures in time-series data result from underlying dissipative and nonlinear mechanisms in complex physical systems.

The highly comparative data-driven method adopted here compares a large algorithmic library of time-series features derived from diverse types of time-series theory.
This empirical approach involves first simulating time-series data from a range of dynamical mechanisms with known structures (in this case diverse formulations of reversible and irreversible processes), and then systematically searching across an extensive and comprehensive set of candidate features (thehctsafeature library[55]), to identify and interpret those which are most effective at recovering the underlying time-series structure (irreversibility).
Prior highly comparative analyses following this general methodological template have identified statistical indicators of self-affine time series[54]and the distance to criticality from short noisy time series[59].
This empirical approach is complementary to a theory-driven approach, whereby new statistical methods are derived from the theory of irreversible processes (e.g.,Dikset al.[17]).
By drawing on a wide array of existing statistical theory, here we are able to provide a unified interdisciplinary perspective on the common conceptual formulations of time-series structure that are informative of time-reversibility.
We also distinguish our data-driven approach, as a wide comparison of time-series analysis methods, from other data-driven machine-learning approaches; the connection to time-series theory is essential in enabling us to connect patterns in the data to an interpretable theory for understanding and guiding future advancements.

Our analysis highlights new relationships between diverse formulations of irreversibility, bridging methods developed across different scientific fields.
We highlight important similarities between generalized autocorrelation statistics (Sec.III.2.1) and symbolic sequences derived from time-series increments (Sec.III.2.2): in both cases, symmetric structures are insensitive to reversibility, while asymmetric statistics provide sensitive real-valued indicators of irreversibility.
In the case of generalized autocorrelations, asymmetry arises through the choice of weights or temporal lags, while for symbolic features it emerges from asymmetric patterns in successive rises and falls; in both cases, trivial statistics correspond to time-symmetric local patterns, and deviations from this symmetry give rise to families of statistics with relatively high predictive performance.
This finding aligns with the observation ofSteinberg [40]for continuous signals, namely that “appropriate measures being those that depend on the direction of thetime arrow”.
The variety of constructions identified here resonates with the considerations ofPomeau [36], who emphasized the potentially infinite formulations of asymmetric autocorrelation functions as effective proxies for detecting irreversibility.
The distinction between symmetric and asymmetric constructions is illustrated in Fig.3, where we introduced a diagrammatic representation that makes the underlying temporal symmetries visually clear.
We also found connections between methodologies adopted within the same family.
For example, we identified a linear relationship between two generalized forms of autocorrelation (under ergodicity and stationarity) that originated from distinct fields: the measure ofSchreiber and Schmitz [71](thetrev​(τ)t^{\mathrm{rev}}(\tau)statistic) developed in nonlinear dynamics, and the ‘TR test’ statistic ofRamsey and Rothman [42](theγ^2,1​(τ)\hat{\!\gamma}_{2,1}(\tau)statistic) developed in finance, in Eq. (8).
Among the symbolic features, our result that the proportion of rises (or falls), as well as its extensions to rise/fall patterns (e.g., the proportion of two consecutive rises or falls), aligns with methods adopted in prior works, e.g., the percentage of positive variations (that is the percentage of rises in a time series) introduced to detect temporal asymmetries in heart rate variability series[47].
Additionally, through our broad inclusion of statistics across the time-series analysis literature we were able to identify novel time-series statistics for capturing time-reversibility that have not previously (to our knowledge) been used for this purpose.
We flag a broad range of forecasting approaches, whether linear or nonlinear, that could be adapted to this problem through differences in predictability between models applied in the forward versus backward directions.
These statistics performed strongly relative to the limited prior work on this topic, yielding time series that are generally more predictable in the forward direction when using a nonlinear predictor, consistent with the findings ofStoneet al.[23], while also highlighting counterintuitive cases in which the time-reversed series is more easily predictable when using linear models.
Complementing these findings, statistics derived from simulating dynamical processes on the time series proved to be among the most effective.
These features offer potentially novel contributions to the time-series literature, spanning from statistics of simulated ‘walkers’ to measures inspired by extreme-value theory[72].

Across the wide range of simulated processes, no individual tested time-series feature could detect irreversibility across all analyzed processes.
As discussed in Sec.I, full information on reversibility is encoded in the time-reversal symmetry of the joint distributionp​(𝒙t(τ))p({\bm{x}}_{t}^{(\tau)})which, for reasonable values of the temporal lagτ\tau, is impractical to estimate from finite data; any statistic that reduces this information to a single value thus discards information.
Consequently, each real-valued time-series summary statistic developed with the purpose of detecting time reversibility captures a specific form of temporal asymmetry (tied to a specific time-series property and typically on a predefined timescale, or set of timescales).
The limited information captured by any individual time-series statistic helps explain why previous studies, often focusing on single approaches, sometimes reached contrasting conclusions about the same processes[52].
Indeed, the breadth of our comparisons confirm that a method effective for one process may fail for another, highlighting the intrinsic limitation of any single-feature approach.
At the same time, we show that (given the leave-one-process-out nearest-neighbor matching heuristic used here) the large algorithmic library of time-series statistics contained inhctsa[55]is sufficiently comprehensive to identify an accurate statistic for capturing time irreversibility for all simulated processes.

Recognizing the strengths and weaknesses of each time-series feature lays the groundwork for future investigations into explicit hypothesis tests, facilitated by the development of an appropriate null distribution[17].
This would extend the 1-NN approach used here as a practical heuristic index, under the assumption that the set of reversible and irreversible processes is sufficiently comprehensive.
While this heuristic was adequate for our current purpose, which primarily focuses on comparative analysis, future work could aim to establish a formal testing framework that more precisely characterizes statistical deviations from reversibility.
For example, an empirical treatment could involve defining a broad set of reversible processes as the null distribution for reversibility, and then quantifying the deviation for a given time series (and test statistic) using a permutation test.
While we have briefly confirmed relatively similar behavior of key irreversibility indices as a function of time-series length (as shown in Fig.B.1), future work could more comprehensively evaluate the generalization of our results to short, noisy time series (where different features may exhibit different levels of robustness to time-series length and additive noise).
Our analysis here was also restricted to univariate time series; future work could investigate extending this approach to multivariate data, building on approaches such as cross-correlation analysis widely used in neuroscience[79], noting that a comprehensive library of pairwise statistics has recently been developed[80].
Finally, while our range of systems analyzed here is comprehensive, it is not exhaustive, and our specific quantitative and qualitative results depend on these choices.
Future work could therefore evaluate a broader range of processes, including those containing more complex timescales[53].

## Acknowledgements.T.D.N. acknowledges support from the Australian Research Council (DP240101295).
B.D.F. acknowledges support from the Australian Research Council (FT240100418).

## Appendix ASimulation details of implemented models

Here we present the simulated processes in greater detail, including the governing equations and specifying the parameter choices made in this work.
In the summary Table1we indicated with a ‘D’ the discrete-time and with a ‘C’ the continuous-time processes to emphasize that distinct simulation strategies are required for continuous-time systems which include greater attention to initial condition selection, downsampling procedures, and integration parameters, as discussed in detail in Sec.II.2.

## Noise.

Time-series realizations of independent and identically distributed (i.i.d.) noise processes were drawn from both a Gaussianxt∼𝒩​(0,1)x_{t}\sim\mathcal{N}(0,1)(labeledGNO) and a uniform distributionxt∼𝒰​(−0.5,0.5)x_{t}\sim\mathcal{U}(-0.5,0.5)(labeledUNO).
Three colored noise processes were generated using Zhivomirov’s algorithm[81], implemented in MATLAB.
As mentioned in Sec.II.1, we simulated realizations of pink noise, characterized by a power spectral density (PSD) proportional to1/f1/f(labeledPINK), whereffis frequency; red noise with a PSD proportional to1/f21/f^{2}(labeledRED); and violet noise with a PSD proportional tof2f^{2}(labeledVIOLET).

## Autoregressive models.

We simulated a first-order autoregressive process, AR(1), given byxt=a​xt−1+εt,x_{t}=a\,x_{t-1}+\varepsilon_{t}\,,(10)

wherea=0.5a=0.5andεt∼𝒩​(0,1)\varepsilon_{t}\sim\mathcal{N}(0,1)is i.i.d. Gaussian noise (labeledAR1_GNO).
Additionally, we considered the static nonlinear transformation of another AR(1) process given by Eq. (10) witha=0.6a=0.6, asyt=tanh2⁡(xt)y_{t}=\tanh^{2}(x_{t})(labeledSTAR).
We adopted the same or closely related parameter choices reported inDikset al.[17].

Next, we simulated autoregressive processes with various forms of non-Gaussianities and nonlinearities.
Linear non-Gaussian stochastic processes simulated here include:
- i.

the AR(1) in Eq. (10) with noise terms sampled from a uniform distribution,εt∼𝒰​(−0.5,0.5)\varepsilon_{t}\sim\mathcal{U}(-0.5,0.5)(labeledAR1_UNO). We decided to maintain the same parameter choice (a=0.5a=0.5) for consistency withAR1_GNO, in order to compare two processes with the same deterministic component and, therefore, isolate the noise contribution;
- ii.

an autoregressive ARMA(1,1) process:xt=0.6​xt−1+ϵt+0.4​ϵt−1,x_{t}=0.6\,x_{t-1}+\epsilon_{t}+0.4\,\epsilon_{t-1}\,,(11)

with noise sampled from a uniform distributionεt∼𝒰​(−0.5,0.5)\varepsilon_{t}\sim\mathcal{U}(-0.5,0.5)(labeledARMA11_UNO);
- iii.

an autoregressive processes with Gamma noise distribution, defined as:xt=0.3​xt−3−0.2​xt−2+0.1​xt−1+ϵt,x_{t}=0.3\,x_{t-3}-0.2\,x_{t-2}+0.1\,x_{t-1}+\epsilon_{t}\,,(12)

with manually specified parameters and noise sampled from gamma distribution,ϵt∼Γ​(1,0.3)\epsilon_{t}\sim\Gamma(1,0.3)(labeledAR3_GAMMA).
The initial condition was drawn from a uniform distribution over[0,1)[0,1).

We also considered three nonlinear autoregressive processes.
The first form of nonlinearity was introduced through Self-Exciting Threshold Autoregressive (SETAR) models, which switch betweenkkdifferent autoregressive regimes based on the pastddvalues of the time series[63].
A SETAR model is denoted SETAR(k;d,p1,…,pk)(k;d,p_{1},...,p_{k})wherekkrepresents the number of regimes,ddis the delay parameter that controls the switch between regimes andp1,…,pkp_{1},...,p_{k}are the orders of the autoregressive models within each of thekkregimes.
We simulated two variants of this process, namely the SETAR(2;1,1,1)(2;1,1,1)model defined as[61](labeledSETAR1):xt={−0.9​xt−1+ϵtif​xt−1≥1,−0.4​xt−1+ϵtif​xt−1<1,x_{t}=\begin{cases}-0.9\,x_{t-1}+\epsilon_{t}&\text{if }x_{t-1}\geq 1\,,\\
-0.4\,x_{t-1}+\epsilon_{t}&\text{if }x_{t-1}<1\,,\end{cases}(13)

and the following specific SETAR(2;2,2,2)(2;2,2,2)process introduced byMartínezet al.[62]:xt={0.62+1.25​xt−1−0.43​xt−2+0.0381​εt,if​xt−2≤3.25,2.25+1.52​xt−1−1.24​xt−2+0.0626​εt,if​xt−2>3.25,x_{t}=\begin{cases}0.62+1.25\,x_{t-1}-0.43\,x_{t-2}+0.0381\,\varepsilon_{t},\penalty 10000\ \penalty 10000\ \text{if }x_{t-2}\leq 3.25\,,\\
2.25+1.52\,x_{t-1}-1.24\,x_{t-2}+0.0626\,\varepsilon_{t},\penalty 10000\ \penalty 10000\ \text{if }x_{t-2}>3.25\,,\end{cases}(14)

whereεt∼𝒩​(0,1)\varepsilon_{t}\sim\mathcal{N}(0,1)are i.i.d. (labeledSETAR2).
For the initial conditions, the first point of theSETAR1process and the first two points of theSETAR2process were sampled from a standard normal distribution.
The second form of nonlinear process is defined by the following equation:xt+1=0.5​xt−0.3​xt−1+0.1​yt−1+0.1​xt−12+0.4​yt2+0.0025​ηt,x_{t+1}=0.5\,x_{t}-0.3\,x_{t-1}+0.1\,y_{t-1}+0.1\,x_{t-1}^{2}+0.4\,y_{t}^{2}+0.0025\,\eta_{t}\,,(15)

whereyt=sin⁡(4​π​t)+sin⁡(6​π​t)+0.0025​ξt,y_{t}=\sin(4\pi t)+\sin(6\pi t)+0.0025\,\xi_{t}\,,(16)

which is driven by both Laplacianηt∼Laplace​(0,1)\eta_{t}\sim\text{Laplace}(0,1)(sharper peak and heavier tails comped to Gaussian distribution) and bimodal Gaussianξt∼0.5​𝒩​(0.63,1)+0.5​𝒩​(−0.63,1)\xi_{t}\sim 0.5\penalty 10000\ \mathcal{N}(0.63,1)+0.5\penalty 10000\ \mathcal{N}(-0.63,1)noise (labeledNAR2).
The first two points of both thexxandyycomponents were set to zero.

## Deterministic chaotic maps.

We simulated the conservative (measure-preserving) Arnold’s Cat map[82](labeledARNOLD), defined by:xt+1\displaystyle x_{t+1}=xt+yt​mod​1,\displaystyle=x_{t}+y_{t}\,\text{mod}\penalty 100001\,,(17)yt+1\displaystyle y_{t+1}=xt+2​yt​mod​1,\displaystyle=x_{t}+2y_{t}\,\text{mod}\penalty 100001\,,

and the Chirikov standard map[8](labeledCHIRIKOV):θt+1\displaystyle\theta_{t+1}=θt+pt+K2​π​sin⁡(2​π​θt)mod​1,\displaystyle=\theta_{t}+p_{t}+\frac{K}{2\pi}\,\sin{(2\pi\theta_{t})}\penalty 10000\ \penalty 10000\ \penalty 10000\ \text{mod}\penalty 100001\,,(18)pt+1\displaystyle p_{t+1}=θt+1−θtmod​1,\displaystyle=\theta_{t+1}-\theta_{t}\penalty 10000\ \penalty 10000\ \penalty 10000\ \text{mod}\penalty 100001\,,

with parameterK=0.971635K=0.971635.
For our analysis we considered thexx-component of the Arnold’s Cat map and thepp-component of the Chirikov standard map.
As representatives of dissipative chaotic maps, we examined thexx-component of the well-studied standard Hénon map[83](a=1.4a=1.4andb=0.3b=0.3) (labeledHEN):xt+1\displaystyle x_{t+1}=1−a​xt2+yt,\displaystyle=1-a\,x_{t}^{2}+y_{t}\,,(19)yt+1\displaystyle y_{t+1}=b​xt,\displaystyle=b\,x_{t}\,,

as well as two additional one-dimensional chaotic systems.
The first one is a quadratic map[84]given by the equationxt+1=1−a​xt2x_{t+1}=1-a\,x_{t}^{2}, with choice of the parametera=1.8a=1.8(labeledQUAD).
The second, the logistic map[85], is given byxt+1=r​xt​(1−xt)x_{t+1}=r\,x_{t}\,(1-x_{t}), which we simulated both in fully chaotic regime (r=4r=4) (labeledLOGISTIC_4) and in the period-3 window (r=3.8284r=3.8284), where it exhibits intermittency (labeledLOGISTIC_38).
For all chaotic maps, initial conditions were randomly sampled from a uniform distribution over the unit interval,[0,1)[0,1).

## Sum of deterministic chaotic maps/flows.

We constructed time series by combining two independent realizations of thexx-component (one realization taken in forward time and another in reverse-time order, constructed by flipping the second in time) of two discrete-time systems: (i) the Hénon map (labeledHENR_DIVERSE); and (ii) quadratic map (labeledQUAD_RSUM).
As a special case for the Hénon map, we also simulated and included a process obtained by summing a forward-time realization with its time-reversed counterpart, generated by flipping the same time series (labeledHENR_SAME).
In addition, we summed pairs of independent forward realizations of thexx-component of the standard Hénon map (labeledHEN_SUM).

We included continuous-time processes in our analysis, considering a linear projectionx+y+zx+y+zof two multidimensional systems: the Lorenz and Rössler systems.
We simulated realizations of the Lorenz system[86]with equations (σ=10\sigma=10,ρ=28\rho=28,β=8/3\beta=8/3):d​xd​t\displaystyle\frac{dx}{dt}=σ​(y−x),\displaystyle=\sigma\,(y-x)\,,(20)d​yd​t\displaystyle\frac{dy}{dt}=x​(ρ−z)−y,\displaystyle=x\,(\rho-z)-y\,,d​zd​t\displaystyle\frac{dz}{dt}=x​y−β​z,\displaystyle=x\,y-\beta\,z\,,

with initial conditions sampled from uniform distributionsx0,y0∼𝒰​(−8,8)x_{0},y_{0}\sim\mathcal{U}(-8,8)andz0∼𝒰​(0,10)z_{0}\sim\mathcal{U}(0,10)(labeledLORENZ_SUM).
The second chaotic flow analyzed is the Rössler system[87]given by (a=0.2a=0.2,b=0.2b=0.2andc=5.7c=5.7):d​xd​t\displaystyle\frac{dx}{dt}=−y−z,\displaystyle=-y-z\,,(21)d​yd​t\displaystyle\frac{dy}{dt}=x+a​y,\displaystyle=x+a\,y\,,d​zd​t\displaystyle\frac{dz}{dt}=b+z​(x−c),\displaystyle=b+z\,(x-c)\,,

for which the initial conditions were sampled from the uniform distributionx0,y0∼𝒰​(−8,8)x_{0},y_{0}\sim\mathcal{U}(-8,8)andz0=0z_{0}=0(labeledROSSLER_SUM]).

## Other deterministic models.

We generated time series from two discrete-time deterministic models:
- i.

the linear model with deterministic noise source,xt+1=a​xt+εtx_{t+1}=a\,x_{t}+\varepsilon_{t}, wherea=0.5a=0.5andεt\varepsilon_{t}is a realization of a logistic modelεt=4​εt−1​(1−εt−1)\varepsilon_{t}=4\,\varepsilon_{t-1}\,(1-\varepsilon_{t-1})(labeledLLOG) that we refer to as ‘logistic noise’;
- ii

the processxt=a​xt−1​mod​1x_{t}=a\,x_{t-1}\penalty 10000\ \text{mod}\penalty 10000\ 1, wherea=2a=\sqrt{2}is the parameter that rules the reversible nature of the process (labeledMOD1).

Additionally, we included two continuous-time systems described by second-order differential equations:
- i.

a linearized oscillator with dynamics described by the equation:d​x2d​t2+x=0,\frac{dx^{2}}{dt^{2}}+x=0\,,(22)

with initial conditions sampled from a uniform distributionx0,y0∼𝒰​(−2,2)x_{0},y_{0}\sim\mathcal{U}(-2,2)(labeledOSCILLATOR);
- ii.

the Van der Pol oscillator[88]specified by:d2​xd​t2−μ​(1−x2)​d​xd​t+x=0,\frac{d^{2}x}{dt^{2}}-\mu\,(1-x^{2})\,\frac{dx}{dt}+x=0\,,(23)

whereμ=1\mu=1, to include effects due to non-linear damping and initial conditions sampled uniformly at random from the[−2,2)[-2,2)interval (labeledVDP).

We simulated dynamics Mackey–Glass equations, dynamics characterized by temporal delays[89].
Specifically, we analyzed the following delay differential equation:d​xd​t=β0​x​(t−τ)1+x​(t−τ)n−γ​x​(t),\frac{dx}{dt}=\frac{\beta_{0}\ x(t-\tau)}{1+x(t-\tau)^{n}}-\gamma\ x(t)\,,(24)

where we setβ0=0.2\beta_{0}=0.2,γ=0.1\gamma=0.1,n=10n=10, and the delayτ=17\tau=17(labeledMG17).
The initial condition was sampled from a uniform distribution,x0∼𝒰​(0,1.5)x_{0}\sim\mathcal{U}(0,1.5).

## Other stochastic processes.

As a discrete-time system, we simulated a noise-driven sine map:xt+1=μ​sin⁡(xt)+yt​ηt,x_{t+1}=\mu\sin{(x_{t})}+y_{t}\eta_{t}\,,(25)

whereμ=2.4\mu=2.4andyty_{t}is Bernoulli random variable that is11with probability0.010.01and0otherwise andηt∼𝒰​(−2,2)\eta_{t}\sim\mathcal{U}(-2,2)[90](labeledSINE_MAP).

In continuous time, we simulated the Ornstein–Uhlenbeck process given by:d​x=−θ​x​d​t+σ​d​W,dx=-\theta\,x\penalty 10000\ dt+\sigma\,dW\,,(26)

withθ=0.8\theta=0.8,σ=0.3\sigma=0.3,WWa Wiener process and initial conditionx0=0x_{0}=0(labeledOU).

We also included bounded random walks (BRW), which are random walks adjusted by a function that biases the random walk downward towards a neighborhood of the stationary meanτ\tauwhen the process deviates excessively from it[91].
The introduction of this adjustment function guarantees the global stationary of the generated time series, limiting the trend behavior typical of random walks.
The continuous-time version of BRW simulated here is given by:d​x=ek​(e−α1​(x−τ)−eα2​(x−τ))​d​t+eσ/2+β/2​xt2​d​W,dx=e^{k}(e^{-\alpha_{1}(x-\tau)}-e^{\alpha_{2}(x-\tau)})dt+e^{\sigma/2+\beta/2x_{t}^{2}}dW\,,(27)

with parametersk=−2k=-2,α1=α2=2\alpha_{1}=\alpha_{2}=2,σ=4\sigma=4,β=0.1\beta=0.1,x0=0x_{0}=0andWWa standard Wiener process (labeledBRW).
Finally, we included stochastic variants of the Lorenz and Van der Pol systems. The stochastic Lorenz system (labeledSTOCH_LORENZ_SUM) was obtained by adding independent Wiener processes,ηx,ηy\eta_{x},\eta_{y}andηz\eta_{z}to the deterministic dynamics pf each coordinate in Eq. (20), and the Van der Pol oscillator (labeledSTOCH_VDP) was generated by adding a standard Wiener processWWto Eq. (23).
Both systems were initialized as in the deterministic case, and the noise intensity was set by scaling the Wiener processes by a factor of1.51.5.

## Appendix BRobustness of time-series statistics for reversibility to the time-series lengthFigure B.1:Time-series features⟨xt3​xt+1⟩\langle x_{t}^{3}\,x_{t+1}\rangle,puu​(x)p_{\text{uu}}(\bm{x})and mean absolute error (MAE) of an AR(2) predictor as a function of the time-series length for a representative process from each family.We show the mean and standard deviation of the feature difference of the generalized autocorrelation⟨xt3​xt+1⟩\langle x_{t}^{3}\,x_{t+1}\rangle(light colors, solid line) and the probability of two successive risespuu​(𝒙)p_{\text{uu}}(\bm{x})(medium colors, dashed line) and MAE of an AR(2) predictor (dark colors, dotted line) for time series of lengthsTT= [10, 20, 50, 100, 200, 500, 1000, 2000, 5000] (xx-axis, logarithmic scale), computed over 100 realizations of each process.
Each panel reports a representative process per family, with colors indicating process families (see Table1).

The main analysis in this work was carried out considering 5000-sample time series.
To assess the robustness of the selected features with respect to time-series length, we computed the mean and standard deviation of the feature differencesΔ​f\Delta ffor a subset of the top-performing statistics discussed in Sec.III.2, across nine different lengths of discrete-time processes:T∈{10,20,50,100,200,500,1000,2000,5000}T\in\{10,20,50,100,200,500,1000,2000,5000\}.
Results are depicted in Fig.B.1for the generalized autocorrelation⟨xt3​xt−1⟩\langle x_{t}^{3}\,x_{t-1}\rangle(light colors, solid line), the symbolicpuu​(𝒙)p_{\text{uu}}(\bm{x})(medium colors, dashed line) statistics, and the mean absolute error (MAE) of an AR(2) predictor (dark colors, dotted line) for a representative process per family (see Table1).
Overall, we observe a larger variability in the generalized autocorrelation compared to the symbolic and the forecasting-based statistics, which exhibits a relatively flat trend forT>50T>50.
For shorter time series, errors in estimating the statistics increase, leading to higher variability in the results, particularly for the generalized autocorrelation.

## Appendix CAnalysis of the time-reversal transformation of the linear autocorrelation

As a simple demonstration of the invariance of the two-point linear autocorrelation⟨xt​xt+τ⟩\langle x_{t}\,x_{t+\tau}\rangleto time reversal when computed on a finite time series of lengthTT, we consider the temporal translation transformationt↦T−t−τ+1t\mapsto T-t-\tau+1(it reduces to the continuous reversalt↦−tt\mapsto-tin the limitT→∞T\to\infty), which preserves the number of time points in the average,t∈[1,T−τ]t\in[1,T-\tau].
Using this transformation, the two-point linear autocorrelation computed on the reversed time series𝒙~\tilde{\bm{x}}, where each term is defined asx~t=xT−t+1\tilde{x}_{t}=x_{T-t+1}, can be expressed in terms of the original time series𝒙\bm{x}⟨x~t​x~t+τ⟩=⟨xt+τ​xt⟩\langle\tilde{x}_{t}\,\tilde{x}_{t+\tau}\rangle=\langle x_{t+\tau}\,x_{t}\rangle

which is equivalent to⟨xt​xt+τ⟩\langle x_{t}\,x_{t+\tau}\rangle.
Consequently, the corresponding feature difference is identically zero, irrespective of the reversibility of the process that generated the time series.

## Appendix DAbsolute difference of asymmetric two-point generalized autocorrelation

Here we compute explicitly the absolute difference for the general formulation of a two-point generalized autocorrelation statisticCα,β​(𝒙;τ)=⟨xtα​xt+τβ⟩C_{\alpha,\beta}(\bm{x};\tau)=\langle x_{t}^{\alpha}\,x_{t+\tau}^{\beta}\rangleusing the shifted time-reversal transformationt↦T−t−τ+1≡st\mapsto T-t-\tau+1\equiv swhich preserves the number of points in the time average (t,s∈[1,T−1]t,s\in[1,T-1]).
We can express the two-point autocorrelationCα,β​(𝒙~;τ)C_{\alpha,\beta}(\tilde{\bm{x}};\tau)in terms of the original time series𝒙\bm{x}as:Cα,β​(𝒙~;τ)\displaystyle C_{\alpha,\beta}(\tilde{\bm{x}};\tau)=⟨x~tα​x~t+τβ⟩=1T−τ−1​∑t=1T−τxT−t+1α​xT−t−τ+1β,\displaystyle=\langle\tilde{x}_{t}^{\alpha}\,\tilde{x}_{t+\tau}^{\beta}\rangle=\frac{1}{T-\tau-1}\sum_{t=1}^{T-\tau}x_{T-t+1}^{\alpha}\,x_{T-t-\tau+1}^{\beta}\,,(28)=1T−τ−1​∑s=1T−τxs+τα​xsβ=⟨xt+τα​xtβ⟩.\displaystyle=\frac{1}{T-\tau-1}\sum_{s=1}^{T-\tau}x_{s+\tau}^{\alpha}\,x_{s}^{\beta}\,=\langle x_{t+\tau}^{\alpha}\,x_{t}^{\beta}\rangle\,.

Consequently, the absolute difference can be written as|Δ​Cα,β​(𝒙;τ)|\displaystyle|\Delta C_{\alpha,\beta}(\bm{x};\tau)|=|Cα,β​(𝒙;τ)−Cα,β​(𝒙~;τ)|,\displaystyle=|C_{\alpha,\beta}(\bm{x};\tau)-C_{\alpha,\beta}(\tilde{\bm{x}};\tau)|\,,(29)=|⟨xtα​xt+τβ⟩−⟨xt+τα​xtβ⟩|.\displaystyle=|\langle x_{t}^{\alpha}\,x_{t+\tau}^{\beta}\rangle-\langle x_{t+\tau}^{\alpha}\,x_{t}^{\beta}\rangle|\,.

## Appendix EAbsolute difference of asymmetric three-point generalized autocorrelation

Here we compute explicitly the absolute difference for the general case of a three-point generalized autocorrelation statistic,|Δ​Cα,β,γ​(𝒙;τ1,τ2)||\Delta C_{\alpha,\beta,\gamma}(\bm{x};\tau_{1},\tau_{2})|.
The calculation is similar to the reasoning that brought to Eq. (7) but here we emphasize the dependence on both the choice of the temporal lagsτ1,τ2\tau_{1},\tau_{2}and of the exponentsα,β,γ\alpha,\beta,\gammato build symmetric constructions.
We consider the general form of a three-point generalized autocorrelationCα,β,γ​(𝒙;τ1,τ2)=⟨xtα​xt+τ1β​xt+τ2γ⟩,C_{\alpha,\beta,\gamma}(\bm{x};\tau_{1},\tau_{2})=\langle x_{t}^{\alpha}\,x_{t+\tau_{1}}^{\beta}\,x_{t+\tau_{2}}^{\gamma}\rangle\,,(30)

for positive, integer exponentsα\alpha,β\betaandγ\gamma, and time-lagsτ1,τ2\tau_{1},\tau_{2}, such thatτ2≠2​τ1\tau_{2}\neq 2\tau_{1}ifα=γ\alpha=\gamma.
Since we have two time-lagsτ1\tau_{1}andτ2\tau_{2}, an appropriate shifting transformation ist↦T−t−τmax+1t\mapsto T-t-\tau_{\mathrm{max}}+1, whereτmax=max​(τ1,τ2)\tau_{\mathrm{max}}=\text{max}(\tau_{1},\tau_{2}).
By writingCα,β,γ​(𝒙~;τ1,τ2)C_{\alpha,\beta,\gamma}(\tilde{\bm{x}};\tau_{1},\tau_{2})in terms of𝒙\bm{x}, as for the two-point generalized autocorrelation, the absolute feature difference gets|Δ​Cα,β,γ​(𝒙;τ1,τ2)|=|Cα,β,γ​(𝒙;τ1,τ2)−Cα,β,γ​(𝒙~;τ1,τ2)|\displaystyle|\Delta C_{\alpha,\beta,\gamma}(\bm{x};\tau_{1},\tau_{2})|=|C_{\alpha,\beta,\gamma}(\bm{x};\tau_{1},\tau_{2})-C_{\alpha,\beta,\gamma}(\tilde{\bm{x}};\tau_{1},\tau_{2})|(31)=|⟨xtα​xt+τ1β​xt+τ2γ⟩−⟨xt+τmaxα​xt+(τmax−τ1)β​xt+(τmax−τ2)γ⟩|.\displaystyle=|\langle x_{t}^{\alpha}\,x_{t+\tau_{1}}^{\beta}\,x_{t+\tau_{2}}^{\gamma}\rangle-\langle x_{t+\tau_{\mathrm{max}}}^{\alpha}\,x_{t+(\tau_{\mathrm{max}}-\tau_{1})}^{\beta}\,x_{t+(\tau_{\mathrm{max}}-\tau_{2})}^{\gamma}\rangle|\,.

This formulation extends Eq. (7) and can itself be generalized to longer temporal scales in two ways: (i) by considering higher-order products, which incorporate longer histories, or (ii) by evaluating pairs or triplets of observations separated by larger temporal lags.
Therefore, the test statistic|Δ​Cα,β,γ​(𝒙;τ1,τ2)||\Delta C_{\alpha,\beta,\gamma}(\bm{x};\tau_{1},\tau_{2})|captures deviations from reversibility by quantifying the asymmetry in the data structure arising from the combined effects of unequal weights and differing temporal lags between data-points.

## References
- López and Lombardi [2024]C. López and O. Lombardi, A review of the concept of time reversal and the direction of time,Entropy26, 563 (2024).
- Rovelli [2019]C. Rovelli,The order of time, 1st ed. (Penguin Press, London, 2019).
- Buonomano [2017]D. Buonomano,Your brain is a time machine: The neuroscience and physics of time(W. W. Norton & Company, 2017).
- Hawking [2011]S. Hawking,A brief history of time: From Big Bang to black holes, 1st ed. (BANTAM UK, 2011).
- Lawrance [1991]A. J. Lawrance, Directionality and reversibility in time series,International Statistical Review / Revue Internationale de Statistique59, 67 (1991).
- Lamb and Roberts [1998]J. S. Lamb and J. A. Roberts, Time-reversal symmetry in dynamical systems: a survey,Physica D: Nonlinear Phenomena112, 1 (1998).
- Peliti and Pigolotti [1982]L. Peliti and S. Pigolotti,Stochastic thermodynamics: An introduction(Princeton University Press, 1982).
- Roberts [1992]J. Roberts, Chaos and time-reversal symmetry. Order and chaos in reversible dynamical systems,Physics Reports216, 63 (1992).
- Devaney [1976]R. L. Devaney, Reversible diffeomorphisms and flows,Transactions of the American Mathematical Society218, 89 (1976).
- Strogatz [2015]S. Strogatz,Nonlinear dynamics and chaos: With applications to physics, biology, chemistry, and engineering, second edition ed. (Westview Press, 2015).
- Seifert [2025]U. Seifert,Stochastic Thermodynamics, 1st ed. (Cambridge University Press, 2025).
- Kawaiet al.[2007]R. Kawai, J. M. R. Parrondo, and C. V. den Broeck, Dissipation: The phase-space perspective,Phys. Rev. Lett.98, 080602 (2007).
- Roldán and Parrondo [2012]E. Roldán and J. M. R. Parrondo, Entropy production and Kullback-Leibler divergence between stationary trajectories of discrete systems,Phys. Rev. E85, 031129 (2012).
- Roldán [2014]E. Roldán,Irreversibility and dissipation in microscopic systems(Springer International Publishing, 2014).
- Weiss [1975]G. Weiss, Time-reversibility of linear stochastic processes,Journal of Applied Probability12, 831 (1975).
- Giannakis and Tsatsanis [1994]G. Giannakis and M. Tsatsanis, Time-domain tests for Gaussianity and time-reversibility,IEEE Transactions on Signal Processing42, 3460 (1994).
- Dikset al.[1995]C. Diks, J. C. van Houwelingen, F. Takens, and J. DeGoede, Reversibility as a criterion for discriminating time series,Phys. Lett. A201, 221 (1995).
- Arola-Fernández and Lacasa [2023]L. Arola-Fernández and L. Lacasa, Irreversibility of symbolic time series: A cautionary tale,Phys. Rev. E108, 014201 (2023).
- Lacasa and Flanagan [2015]L. Lacasa and R. Flanagan, Time reversibility from visibility graphs of nonstationary processes,Phys. Rev. E92, 022817 (2015).
- González-Espinozaet al.[2020]A. González-Espinoza, G. Martínez-Mekler, and L. Lacasa, Arrow of time across five centuries of classical music,Phys. Rev. Research2, 033166 (2020).
- Camassaet al.[2024]A. Camassa, M. Torao-Angosto, A. Manasanch, M. L. Kringelbach, G. Deco, and M. V. Sanchez-Vives, The temporal asymmetry of cortical dynamics as a signature of brain states,Scientific Reports14, 24271 (2024).
- Cox [1981]D. R. Cox, Statistical analysis of time series: Some recent developments [with discussion and reply],Scand J Statist8, 93 (1981).
- Stoneet al.[1996]L. Stone, G. Landan, and R. M. May, Detecting time’s arrow: A method for identifying nonlinearity and deterministic chaos in time-series data,Proceedings: Biological Sciences263, 1509 (1996).
- Van Der Heydenet al.[1996]M. Van Der Heyden, C. Diks, J. Pijn, and D. Velis, Time reversibility of intracranial human EEG recordings in mesial temporal lobe epilepsy,Phys. Lett. A216, 283 (1996).
- Pijnet al.[1997]J. P. Pijn, D. N. Velis, M. J. van der Heyden, J. DeGoede, C. W. van Veelen, and F. H. Lopes da Silva, Nonlinear dynamics of epileptic seizures on basis of intracranial EEG recordings,Brain Topogr.9, 249 (1997).
- Schindleret al.[2016]K. Schindler, C. Rummel, R. G. Andrzejak, M. Goodfellow, F. Zubler, E. Abela, R. Wiest, C. Pollo, A. Steimer, and H. Gast, Ictal time-irreversible intracranial EEG signals as markers of the epileptogenic zone,Clinical Neurophysiology127, 3051 (2016).
- Zhang and Wang [2023]F. Zhang and J. Wang, Nonequilibrium indicator for the onset of epileptic seizure,Phys. Rev. E108, 044111 (2023).
- Costaet al.[2005]M. Costa, A. L. Goldberger, and C.-K. Peng, Broken asymmetry of the human heartbeat: Loss of time irreversibility in aging and disease,Phys. Rev. Lett.95, 198102 (2005).
- Guziket al.[2006]P. Guzik, J. Piskorski, T. Krauze, A. Wykretowicz, and H. Wysocki, Heart rate asymmetry by Poincaré plots of RR intervals,Biomedizinische Technik/Biomedical Engineering51, 272 (2006).
- Portaet al.[2008]A. Porta, K. R. Casali, A. G. Casali, T. Gnecchi-Ruscone, E. Tobaldini, N. Montano, S. Lange, D. Geue, D. Cysarz, and P. Van Leeuwen, Temporal asymmetries of short-term heart period variability are linked to autonomic regulation,American Journal of Physiology. Regulatory, Integrative and Comparative Physiology295, R550 (2008).
- Braunet al.[1998]C. Braun, P. Kowallik, A. Freking, D. Hadeler, K.-D. Kniffki, and M. Meesmann, Demonstration of nonlinear components in heart rate variability of healthy persons,American Journal of Physiology-Heart and Circulatory Physiology275, H1577 (1998).
- Timmeret al.[1993]J. Timmer, C. Gantert, G. Deuschl, and J. Honerkamp, Characteristics of hand tremor time series,Biological Cybernetics70, 75 (1993).
- Zumbach [2009]G. Zumbach, Time reversal invariance in finance,Quantitative Finance9, 505 (2009).
- Chenet al.[2000]Y.-T. Chen, R. Y. Chou, and C.-M. Kuan, Testing time reversibility without moment restrictions,Journal of Econometrics95, 199 (2000).
- Flanagan and Lacasa [2016]R. Flanagan and L. Lacasa, Irreversibility of financial time series: A graph-theoretical approach,Phys. Lett. A380, 1689 (2016).
- Pomeau [1982]Y. Pomeau, Symétrie des fluctuations dans le renversement du temps,Journal de Physique43, 859 (1982).
- Schmitt [2023]F. G. Schmitt, Scaling analysis of time-reversal asymmetries in fully developed turbulence,Fractal and Fractional7, 630 (2023).
- Josserandet al.[2017]C. Josserand, M. Le Berre, T. Lehner, and Y. Pomeau, Turbulence: does energy cascade exist?,Journal of Statistical Physics167, 596 (2017).
- Brillinger and Rosenblatt [1967]D. Brillinger and M. Rosenblatt, Computation and interpretation of k-th order spectra, Spectral Analysis of Time Series , 189 (1967).
- Steinberg [1986]I. Z. Steinberg, On the time reversal of noise signals,Biophysical Journal50, 171 (1986).
- Ramsey and Rothman [1988]J. B. Ramsey and P. Rothman, Characterization of the time irreversibility of economic time series: Estimators and test statistics,Working Papers (C.V. Starr Center for Applied Economics)28, 1 (1988).
- Ramsey and Rothman [1996]J. B. Ramsey and P. Rothman, Time irreversibility and business cycle asymmetry,Journal of Money, Credit and Banking28, 1 (1996).
- Hinich and Rothman [1998]M. J. Hinich and P. Rothman, Frequency-domain test of time reversibility,Macroecon. Dynam.2, 72 (1998).
- Cox [1991]D. R. Cox, Long-range dependence, non-linearity and time irreversibility,Journal of Time Series Analysis12, 329 (1991).
- Casaliet al.[2008]K. R. Casali, A. G. Casali, N. Montano, M. C. Irigoyen, F. Macagnan, S. Guzzetti, and A. Porta, Multiple testing strategy for the detection of temporal irreversibility in stationary time series,Phys. Rev. E77, 066204 (2008).
- Tsay [1992]R. S. Tsay, Model checking via parametric bootstraps in time series analysis,Journal of the Royal Statistical Society. Series C (Applied Statistics)41, 1 (1992).
- Portaet al.[2006]A. Porta, S. Guzzetti, N. Montano, T. Gnecchi-Ruscone, R. Furlan, and A. Malliani, Time reversibility in short-term heart period variability, 2006 Computers in Cardiology , 77 (2006).
- Dawet al.[2000]C. S. Daw, C. E. A. Finney, and M. B. Kennel, Symbolic approach for measuring temporal “irreversibility”,Phys. Rev. E62, 1912 (2000).
- Lacasaet al.[2012]L. Lacasa, A. Nuñez, E. Roldán, J. M. R. Parrondo, and B. Luque, Time series irreversibility: a visibility graph approach,Eur. Phys. J. B85, 217 (2012).
- Dongeset al.[2013]F. J. Donges, R. V. Donner, and J. Kurths, Testing time series irreversibility using complex network methods,EuroPhys. Lett.102, 10004 (2013).
- Kennel [2004]M. B. Kennel, Testing time symmetry in time series using data compression dictionaries,Phys. Rev. E69, 056208 (2004).
- Zanin and Papo [2021]M. Zanin and D. Papo, Algorithmic approaches for assessing irreversibility in time series: review and comparison,Entropy23, 1474 (2021).
- Zanin and Papo [2025]M. Zanin and D. Papo, Algorithmic approaches for assessing multiscale irreversibility in time series: review and comparison,Entropy27, 126 (2025).
- Fulcheret al.[2013]B. D. Fulcher, M. A. Little, and N. S. Jones, Highly comparative time-series analysis: the empirical structure of time series and their methods,Journal of The Royal Society Interface10, 20130048 (2013).
- Fulcher and Jones [2017]B. D. Fulcher and N. S. Jones,hctsa: A computational framework for automated time-series phenotyping using massive feature extraction,Cell Systems5, 527 (2017).
- Yanget al.[2024]S. Yang, Y. Zhou, C. Peng, Y. Meng, H. Chen, S. Zhang, X. Kong, R. Kong, B. T. T. Yeo, W. Liao, and Z. Zhang, Macroscale intrinsic dynamics are associated with microcircuit function in focal and generalized epilepsies,Commun Biol7, 1 (2024).
- Letzkuset al.[2023]L. Letzkus, R. Picavia, G. Lyons, J. Brandberg, J. Qiu, S. Kausch, D. Lake, and K. Fairchild, Heart rate patterns predicting cerebral palsy in preterm infants,Pediatr. Res. , 1 (2023).
- Paulet al.[2021]A. Paul, H. McLendon, V. Rally, J. T. Sakata, and S. C. Woolley, Behavioral discrimination and time-series phenotyping of birdsong performance,PLOS Computational Biology17, e1008820 (2021).
- Harriset al.[2024]B. Harris, L. L. Gollo, and B. D. Fulcher, Tracking the distance to criticality in systems with unknown noise,Phys. Rev. X14, 031021 (2024).
- Hoover [1998]W. G. Hoover, Time reversibility in nonequilibrium thermomechanics,Physica D: Nonlinear Phenomena112, 225 (1998).
- Rothman [1999]P. Rothman, Higher-order residual analysis for simple bilinear and threshold autoregressive models with the tr test, inNonlinear Time Series Analysis of Economic and Financial Data, edited by P. Rothman (Springer US, Boston, MA, 1999) pp. 357–367.
- Martínezet al.[2018]J. H. Martínez, J. L. Herrera-Diestra, and M. Chavez, Detection of time reversibility in time series by ordinal patterns analysis,Chaos: An Interdisciplinary Journal of Nonlinear Science28, 123111 (2018).
- Tong and Lim [1980]H. Tong and K. S. Lim, Threshold autoregression, limit cycles and cyclical data,Journal of the Royal Statistical Society. Series B (Methodological)42, 245 (1980).
- Kloeden and Platen [1992]P. E. Kloeden and E. Platen,Numerical solution of stochastic differential equations(Springer Berlin Heidelberg, 1992).
- Fehlberg [1969]E. Fehlberg,Low-order classical Runge-Kutta formulas with stepsize control and their application to some heat transfer problems, Tech. Rep. NASA-TR-R-315 (NASA, 1969).
- Dalle Nogare [2025a]T. Dalle Nogare,Github repository with code for the analysi(2025a).
- Dalle Nogare [2025b]T. Dalle Nogare, Dataset with processed and raw data for reproduction of the results,10.5281/zenodo.17620039(2025b).
- Cohen [1995]L. Cohen,Time-Frequency Analysis(Prentice Hall PTR, 1995).
- Kraskovet al.[2004]A. Kraskov, H. Stögbauer, and P. Grassberger, Estimating mutual information,Phys. Rev. E69, 066138 (2004).
- Luqueet al.[2009]B. Luque, L. Lacasa, F. Ballesteros, and J. Luque, Horizontal visibility graphs: Exact results for random time series,Phys. Rev. E80, 046103 (2009).
- Schreiber and Schmitz [1997]T. Schreiber and A. Schmitz, Discrimination power of measures for nonlinearity in a time series,Phys. Rev. E55, 5443 (1997).
- Altmannet al.[2006]E. G. Altmann, S. Hallerberg, and H. Kantz, Reactions to extreme events: Moving threshold model,Physica A: Statistical Mechanics and its Applications364, 435 (2006).
- Duarte Queirós and Moyano [2007]S. Duarte Queirós and L. Moyano, Yet on statistical properties of traded volume: Correlation and mutual information at different value magnitudes,Physica A: Statistical Mechanics and its Applications383, 10 (2007).
- Bandt and Pompe [2002]C. Bandt and B. Pompe, Permutation entropy: A natural complexity measure for time series,Phys. Rev. Letters88, 174102 (2002).
- Kelleret al.[2014]K. Keller, A. Unakafov, and V. Unakafova, Ordinal patterns, entropy, and EEG,Entropy16, 6212 (2014).
- Zanin and Olivares [2021]M. Zanin and F. Olivares, Ordinal patterns-based methodologies for distinguishing chaos from noise in discrete time series,Communications Physics4, 1 (2021).
- Small [2005]M. Small,Applied nonlinear time series analysis: Applications in physics, physiology and finance, Vol. 52 (World Scientific Publishing Company, 2005).
- Wolpert and Macready [1997]D. Wolpert and W. Macready, No free lunch theorems for optimization,IEEE Transactions on Evolutionary Computation1, 67 (1997).
- Decoet al.[2022]G. Deco, Y. Sanz Perl, H. Bocaccio, E. Tagliazucchi, and M. L. Kringelbach, The INSIDEOUT framework provides precise signatures of the balance of intrinsic and extrinsic dynamics in brain states,Commun Biol5, 1 (2022).
- Cliffet al.[2023]O. M. Cliff, A. G. Bryant, J. T. Lizier, N. Tsuchiya, and B. D. Fulcher, Unifying pairwise interactions in complex dynamics,Nat Comput Sci3, 883 (2023).
- Zhivomirov [2018]H. Zhivomirov, A method for colored noise generation, Romanian Journal of Acoustics and Vibration15, 14 (2018).
- Arnol‘d and Avez [1968]V. I. Arnol‘d and A. Avez,Ergodic problems of classical mechanics(New York, Benjamin, 1968).
- Hénon [1976]M. Hénon, A two-dimensional mapping with a strange attractor, Commun. math. Phys.50, 69 (1976).
- Sprott [1997]J. Sprott, Simplest dissipative chaotic flow,Phys. Lett. A228, 271 (1997).
- May [1976]R. M. May, Simple mathematical models with very complicated dynamics,Nature261, 459 (1976).
- Lorenz [1963]E. N. Lorenz, Deterministic nonperiodic flow,Journal of Atmospheric Sciences20, 130 (1963).
- Rössler [1976]O. Rössler, An equation for continuous chaos, Phys. Lett. A57,10.1016/0375-9601(76)90101-8(1976).
- van der Pol Jun. [1926]B. van der Pol Jun., LXXXVIII. On “relaxation-oscillations”,The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science2, 978 (1926).
- Mackey and Glass [1977]M. C. Mackey and L. Glass, Oscillation and chaos in physiological control systems,Science197, 287 (1977).
- Freitaset al.[2009]U. S. Freitas, C. Letellier, and L. A. Aguirre, Failure in distinguishing colored noise from chaos using the “noise titration” technique,Phys. Rev. E79, 035201 (2009).
- Nicolau [2002]J. Nicolau, Stationary processes that look like random walks: The bounded random walk process in discrete and continuous time,Econometric Theory18, 99 (2002).
