# Performance Benchmarking: Software for the Density Matrix Renormalization Group

**arXiv ID**: 2607.28369v1
**Authors**: Per Sehlstedt, Paolo Bientinesi, Lars Karlsson
**Published**: 2026-07-30
**Categories**: physics.comp-ph, cs.CE, cs.MS, physics.chem-ph, quant-ph
**HTML URL**: https://arxiv.org/html/2607.28369v1

## Abstract

The performance of scientific software often determines the scale of problems that can be solved in practice. As multiple implementations of the same algorithm emerge, systematic evaluation is needed to compare their strengths and limitations. The density matrix renormalization group (DMRG) algorithm, widely used to study quantum systems, has over 50 software implementations. These implementations vary in multiple aspects that can strongly affect performance. However, despite the need, performance evaluations of these implementations are scarce and lack a consistent standard; many existing evaluations are either too incomplete to enable meaningful comparisons or focus on objectives other than direct performance comparisons, thereby limiting understanding of how the implementations compare. Here, we present a performance-oriented benchmarking framework to facilitate meaningful comparisons of DMRG implementations, and we apply it to quantify the performance of eight implementations, highlighting similarities and differences among them. Furthermore, we examine multiple parameter settings, optimization strategies, and implementation-specific features to demonstrate how parameter configuration can affect performance and how systematic evaluation can reveal non-obvious trade-offs. The results show significant performance differences, up to two orders of magnitude in some cases, not only between different implementations when aligning parameters, but also within the same implementation when comparing different parameter configurations. Hence, our results demonstrate the significant value and insight that can be gained from conducting rigorous performance evaluations. Using our results and framework as a starting point, more rigorous benchmarking will ultimately help users and developers make informed decisions and support future development efforts to build better, more efficient software.

## Full Text

Performance Benchmarking: Software for the Density Matrix Renormalization Group

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.28369v1 [physics.comp-ph] 30 Jul 2026

## Performance Benchmarking: Software for the Density Matrix Renormalization GroupPer SehlstedtPaolo BientinesiLars Karlsson

## Abstract

The performance of scientific software often determines the scale of problems that can be solved in practice. As multiple implementations of the same algorithm emerge, systematic evaluation is needed to compare their strengths and limitations. The density matrix renormalization group (DMRG) algorithm, widely used to study quantum systems, has over 50 software implementations. These implementations vary in multiple aspects that can strongly affect performance. However, despite the need, performance evaluations of these implementations are scarce and lack a consistent standard; many existing evaluations are either too incomplete to enable meaningful comparisons or focus on objectives other than direct performance comparisons, thereby limiting understanding of how the implementations compare. Here, we present a performance-oriented benchmarking framework to facilitate meaningful comparisons of DMRG implementations, and we apply it to quantify the performance of eight implementations, highlighting similarities and differences among them. Furthermore, we examine multiple parameter settings, optimization strategies, and implementation-specific features to demonstrate how parameter configuration can affect performance and how systematic evaluation can reveal non-obvious trade-offs. The results show significant performance differences, up to two orders of magnitude in some cases—not only between different implementations when aligning parameters, but also within the same implementation when comparing different parameter configurations. Hence, our results demonstrate the significant value and insight that can be gained from conducting rigorous performance evaluations. Using our results and framework as a starting point, more rigorous benchmarking will ultimately help users and developers make informed decisions and support future development efforts to build better, more efficient software.

Keywords—DMRG, Tensor Network, Framework

## 1Introduction

Software excellence is characterized by multiple qualities; however, for the computational scientist, performance is a central concern, as it often determines the feasible scale of computation. Yet, when attempting to identify the most effective solution, the landscape can be crowded with competing implementations whose surface characteristics offer limited insight into practical behavior. Thus, meaningful judgment requires systematic evaluation.

These considerations are particularly acute for packages that implement the density matrix renormalization group (DMRG) algorithm[84,85], as their performance is sensitive to implementation details and parameter configuration. As the DMRG field has matured, more than 50 software implementations have emerged, each offering different trade-offs in functionality, ease of use, extensibility, and supported features[69]. For new users in particular, navigating this landscape can be difficult: documentation quality varies, advertised capabilities are not always directly comparable, and practical guidance on which package to choose for a specific use case is often limited. Rigorous performance benchmarking would alleviate some of the difficulty by enabling meaningful comparisons across implementations. Additionally, it would help track progression and guide future development.

Currently, performance evaluations of DMRG implementations remain scarce and lack a consistent standard, with few cross-comparisons. Moreover, many existing evaluations are too incomplete to enable meaningful performance comparisons, as they omit critical context on the interplay between computational cost and solution quality. For instance, reporting a fast execution time in isolation provides limited value, since the speed may come at the expense of convergence or accuracy. Thus, without a clear connection between these aspects, our ability to assess how each package truly performs relative to the others is hindered.

In this paper, we pursue three aims: (i) In order to facilitate meaningful performance evaluations and comparisons of DMRG implementations, we present a performance-oriented benchmarking framework that focuses on the interplay between computational cost and solution quality; (ii) in order to highlight similarities and differences in performance across available implementations, we apply the framework and quantify the performance of eight implementations; (iii) in order to demonstrate how parameter configuration can affect performance and how systematic evaluation can reveal non-obvious trade-offs, we examine multiple parameter settings, optimization strategies, and implementation-specific features.
As such, we aim to establish a foundation for systematically evaluating tensor network methods such as DMRG, benefiting both users and developers by enabling more insightful performance assessments and better-informed decisions, and by supporting future development efforts.

The remainder of this paper is structured as follows: We outline the DMRG algorithm and many of its tunable parameters and optimization strategies inSection2; we review related work and describe our benchmarking framework inSection3, and we explain how we apply it in our experiments inSection4; we present the results of the experiments inSection5and provide the final discussions and conclusion inSection6.

## 2Theory

## 2.1The DMRG algorithm

The DMRG algorithm[84,85]is today typically framed as a variational optimization seeking to minimize the expectation valueEEof a given HamiltonianH^\widehat{H}over the set of states spanned by a variational ansatz|ψ⟩\ket{\psi}:arg⁡min|ψ⟩⁡E​(|ψ⟩)=arg⁡min|ψ⟩⁡⟨ψ|H^|ψ⟩⟨ψ|ψ⟩.\arg\min_{\ket{\psi}}E(\ket{\psi})=\arg\min_{\ket{\psi}}\frac{\expectationvalue{\widehat{H}}{\psi}}{\innerproduct{\psi}{\psi}}.(1)

The variational ansatz is usually chosen from a tensor network state family, as they have become recognized as a natural language for describing quantum states of matter[68,57].

The reason tensor network states constitute a natural choice for|ψ⟩\ket{\psi}is that they can provide efficient parameterizations by capturing the relevant entanglement properties of the systems under consideration.
Over the years, numerous tensor network families have been developed, each associated with distinct geometrical structures suited to different physical settings and classes of quantum states[12,18,58].
A viable option is provided by tree tensor networks (TTN)[71,54]; however, by far the most common choice within DMRG is the matrix product state (MPS)[68]—also known as the tensor-train decomposition[59].

A general MPS with open boundary conditions takes the form|ψMPS⟩=∑𝝈(∏k=1LMσk)​|𝝈⟩,|𝝈⟩=⨂k=1L|σk⟩,\ket{\psi_{\mathrm{MPS}}}=\sum_{\bm{\sigma}}\left(\prod^{L}_{k=1}M^{\sigma_{k}}\right)\ket{\bm{\sigma}},\qquad\ket{\bm{\sigma}}=\bigotimes^{L}_{k=1}\ket{\sigma_{k}},(2)

whereLLis the number of sites,{|σk⟩}\left\{\ket{\sigma_{k}}\right\}is the basis for the local Hilbert space at sitekkwith physical indexσk\sigma_{k}labeling the basis, and𝝈\bm{\sigma}being the multi-index of all local state indices.
Moreover,Mσk∈ℂDk×Dk+1M^{\sigma_{k}}\in\mathbb{C}^{D_{k}\times D_{k+1}}are local matrices, whereDk+1D_{k+1}denotes the bond dimension associated with the virtual link between siteskkandk+1k+1, withD1=DL+1=1D_{1}=D_{L+1}=1. The entries of these matrices constitute the variational parameters, with the bond dimension determining the amount of entanglement that can be represented[68].

Due to the matrix product structure ineq.2, the MPS is invariant under the insertion of an invertible matrix and its inverse between two adjacent sites, reflecting a gauge freedom.
This gauge freedom can be fixed by imposing left- and right-orthonormality of the matrices to the left and right of a chosen site, respectively, yielding a canonical form.
The canonical form plays a central role in DMRG, as it improves numerical stability and performance[68].

In analogy with an MPS, the Hamiltonian will typically be represented as a matrix product operator (MPO), taking the formH^=∑𝝈,𝝈′(∏k=1LWσk​σk′)​|𝝈⟩​⟨𝝈′|,\widehat{H}=\sum_{\bm{\sigma},\bm{\sigma^{\prime}}}\left(\prod^{L}_{k=1}W^{\sigma_{k}\sigma^{\prime}_{k}}\right)\ket{\bm{\sigma}}\bra{\bm{\sigma^{\prime}}},(3)

where theWσk​σk′∈ℂDk×Dk+1W^{\sigma_{k}\sigma^{\prime}_{k}}\in\mathbb{C}^{D_{k}\times D_{k+1}}matrices are analogous to theMσkM^{\sigma_{k}}matrices, but carry two physical indices instead of one, corresponding to the input and output states of the local Hilbert space[68].

DMRG minimizesEEvia an iterative sweeping procedure. In this procedure, one or two adjacent local MPS tensors are optimized at a time while the others are held fixed, reducing the global optimization problem to a sequence of local optimizations. Using a canonical MPS form ensures that each local optimization remains well-conditioned throughout the procedure. At each sweep step, the effective eigenvalue problem is solved with an iterative sparse-matrix eigensolver, such as the Lanczos or Davidson methods. These projection-based solvers are preferred because they enable matrix-free implementations and efficiently target the desired extremal eigenpairs[68].

Each local optimization temporarily breaks the MPS’s canonical form, which must be restored before proceeding to maintain the algorithm’s efficiency. During this restoration, truncation is often necessary in the 2-site DMRG algorithm to control the enlarged bond dimension between sites, but the restoration can also be used to naturally allow for adaptive adjustment. Truncation is achieved by retaining the most significant states, where significance may be defined by a fixed maximum bond dimension, a threshold on the discarded weight, a combination of both, or other criteria. It is typically determined via a singular value decomposition, yielding an optimal low-rank approximation in the variational sense[68].

Symmetries in quantum systems give rise to conserved quantities, which often can be leveraged in DMRG to reduce computational effort.
IfH^\widehat{H}commutes with an operatorQ^\widehat{Q},[H^,Q^]=0,[\widehat{H},\widehat{Q}]=0,(4)

thenQ^\widehat{Q}is a conserved charged, and the eigenstates ofH^\widehat{H}can be chosen simultaneously as eigenstates ofQ^\widehat{Q}.
The eigenvaluesqqofQ^\widehat{Q}are thus good quantum numbers, and can be used to decompose the Hilbert space into independent sectors, makingH^\widehat{H}block-diagonal with respect to this decomposition.
Since the ground state lies within a definite symmetry sector, DMRG can restrict its variational search to the corresponding block, ensuring that the conserved quantity is preserved exactly throughout the calculation and avoiding unnecessary exploration of other sectors[68].

Incorporating abelian symmetries—such as aU​(1)\mathrm{U}(1)symmetry associated with total magnetization or particle number conservation—remains simple to implement due to their commutativity, and typically provides notable efficiency gains.
Leveraging non-abelian symmetries—such asSU​(2)\mathrm{SU}(2)total spin conservation—comes at a significantly higher implementation cost due to the complexity of managing non-commutative group representations, but can capture a richer internal structure and yield even greater efficiency gains[44,81].

## 2.2Tunable parameters and optimization strategies

Although the DMRG algorithm admits a compact high-level description, its practical performance depends on numerous implementation details and parameter configuration. Sensible default choices can provide robust performance in many cases, but no single set of defaults is optimal across all models and regimes. Consequently, it is important not only that users have access to these parameters but also that they are aware of different optimization strategies and which aspects of the algorithm can be tuned, so that they can make informed adjustments to adapt the method to the specific structure and numerical challenges of their problem.

Here, we go through 12 different aspects.

## Variational ansatz

The most common choice for the variational ansatz within DMRG is the MPS; however, there are other options, such as the TTN, whose hierarchical structure can be beneficial in certain situations.

## Update mode

2-site DMRG offers greater robustness by naturally allowing the bond dimension to grow dynamically, at the expense of increased computational cost. Traditional 1-site DMRG, by contrast, is computationally cheaper per step but may require additional stabilization mechanisms to avoid local minima. Because of these trade-offs, the optimal approach can vary across different stages of the optimization.

## Bond dimension

The bond dimension is one of the most influential parameters, as it determines the achievable accuracy. Beyond specifying a maximum bond dimension, users may enforce a minimum bond dimension or prescribe a gradual increase in it over time. Such strategies can improve convergence, particularly in early sweeps, and help avoid premature loss of relevant states during truncation[76].

## Eigensolver

The local eigensolver is a critical component, as its routine is typically the most time-consuming part of the algorithm.
At a high level, the choice of method—such as Lanczos, Davidson, or related variants—already influences convergence behavior and computational cost. At a more fine-grained level, solver-specific settings, including convergence tolerances, Krylov subspace dimensions, cutoffs, restart strategies, preconditioners, and orthogonalization schemes, can further affect performance.

## Truncation criterion

The choice of truncation criterion—whether based on a fixed bond dimension, a discarded weight tolerance, or related entropy-based measures—can influence the trade-off between accuracy and efficiency. As with decisions about bond dimension, different stages of the optimization can benefit from different criteria; for example, progressively decreasing the cutoff can keep early sweeps efficient while ensuring that the final MPS achieves high accuracy.

## Enhancements

Stabilization and acceleration mechanisms have been introduced since the original formulation of DMRG. These include density matrix perturbation[86], subspace expansion[30], and controlled bond expansion[22]. They are particularly important for 1-site schemes that aim to achieve lower computational costs than 2-site schemes while avoiding getting stuck in local minima when enforcing symmetry constraints.

## Symmetries

The ability for users to leverage good quantum numbers across a wide range of symmetry groups is an important implementation feature.
Although enforcing these constraints introduces some overhead and can occasionally complicate convergence, the overhead is often negligible, and symmetry-adapted DMRG typically delivers significant performance gains by reducing computational cost and improving accuracy.

## Mixed-precision

Lower floating-point precision reduces memory usage and accelerates computations at the expense of accuracy; however, because the DMRG algorithm is iterative, the loss of accuracy is often insignificant during the initial sweeps, when the MPS is still a crude approximation.
The availability of mixed-precision strategies—such as the approach introduced by Tian et al.[80]—is therefore attractive, enabling users to perform early sweeps in reduced precision to accelerate the calculation without compromising final accuracy.

Furthermore, mixed-precision techniques that emulate double-precision arithmetic have recently shown promising results on state-of-the-art hardware[6].

## Linear algebra libraries

DMRG relies heavily on tensor algebra, with frequent contractions and decompositions at its core. The efficiency of these operations depends critically on the underlying linear algebra libraries. As such, selecting libraries well optimized for the target hardware is essential for achieving maximum performance.

## Out-of-core

Large-scale DMRG calculations—e.g., high bond dimensions or many sites—can require substantial memory. In such cases, in-memory storage may become impractical, and using out-of-core strategies for storing data on disk may be necessary to complete the computation.

## Quantum chemistry

In quantum chemistry applications, additional choices—such as selecting the appropriate orbital basis and ordering to minimize long-range entanglement—can significantly improve DMRG performance by reducing the effective bond dimension and accelerating convergence[56].

## Parallelism

High-performance DMRG implementations often rely on multiple levels of parallelism to accelerate computations, including GPU acceleration where supported[94,79]. Such optimizations are essential for enabling large-scale calculations to maintain a practical time-to-solution.

## 3Performance benchmarking

## 3.1Related work

In many areas of computational science, standardized benchmark suites provide a common framework for evaluating software performance, enabling reproducible and rigorous comparisons across implementations and hardware platforms.
For example, the LINPACK benchmark has long served as the standard for assessing high-performance computing systems and underpins the TOP500 ranking of supercomputers[17].
Similar benchmark suites, such as SparseBench[15], Graph500[53], HPCG[16], and MLPerf[43], are widely used in their related fields where they facilitate the evaluation of algorithmic and software developments.
In contrast, performance benchmarking for DMRG implementations remains scarce and lacks a consistent standard.

While DMRG has been studied extensively from both algorithmic and application perspectives[68,76,8,3], relatively little attention has been paid to the systematic performance evaluation and benchmarking of its many implementations[69].
As such, existing benchmarks, which frequently appear in DMRG papers introducing new software packages or developments, typically serve purposes other than direct performance comparisons between existing implementations.

For example, many software papers introducing new packages or package versions often focus on theory, applications, and usage. Consequently, a common benchmarking practice in these papers is to measure sweep time as a function of bond dimension to validate expected time-complexity scaling—as seen in papers introducingITensor[19],Block2[95],TeNPy[27],YASTN[64],Cytnx[89],pyTTN[41], andTensorKit[13]. Another common practice in these papers is to evaluate specific aspects, such as parallel efficiency, or to demonstrate certain capabilities, such as analysis of specific systems, which we see in the introductions ofREGO[36],ALPS MPS[14],CheMPS2[87],MOLMPS[5],Kylin[74], andQCMaquis[77]. Others—such as introductions ofDMRG++[1],BAGEL[72],OSMPS[34],quimb[24],PyTeNet[50],QSpace[82], andSeeMPS[21]—focus solely on the supported methods and features, and thus do not include any benchmarks.

Likewise, papers introducing new DMRG developments typically focus on theoretical aspects and therefore often aim to quantify the potential impact in general rather than how it compares to existing implementations. Examples include the use of non-abelian symmetries[44,2,81], density matrix perturbation[86], subspace expansion[30], various parallelism strategies[94,25,55,36,73,9,88,7,75,11], mixed-precision strategies[80], controlled bond expansion[22], heterogeneous computing platforms[79,55,39,10,20,28,42], and emulated FP64 arithmetic[6].

In both cases, it is unsurprising that the benchmarks do not meet the requirements needed to enable meaningful performance comparisons between implementations and the needs of users seeking them, since the benchmarks have other main objectives and are often only applied to individual implementations.

While there exist a few comprehensive performance evaluations of specific packages, such astensor-tools[38],DMRG-Budapest[48,47,45,49,46,37],Focus[90], andQuantum TEA[33], these studies have mostly been performed in isolation, using different benchmark problems and experimental setups, and are not enough to be representative of the entire landscape of implementations. As such, evaluations at large remain incomplete, with very few cross-comparisons. This article aims to contribute toward addressing that gap.

## 3.2Requirements for performance benchmarks

What requirements must a benchmark satisfy to enable meaningful performance comparisons between DMRG implementations? We argue that at least five fundamental conditions are necessary: (i) Computational cost and solution quality must be evaluated jointly, (ii) end-to-end performance metrics must be considered, (iii) a common set of model problems must be used, (iv) parameter configurations must be handled in a controlled manner, and (v) hardware and software environments must be handled in a controlled manner.

First, computational cost is only meaningful when considered alongside the solution quality obtained. For example, if implementation A is reported to be faster than implementation B but produces a lower-quality result, comparing time alone is not meaningful, since both implementations may ultimately require the same amount of time to reach a target quality.

Second, comparisons must be based primarily on end-to-end performance metrics rather than local metrics such as sweep times. For example, if implementation A performs sweeps faster than implementation B but requires more sweeps, sweep time alone provides an incomplete picture of end-to-end time cost and is thus not meaningful. Although local metrics remain valuable for understanding specific implementation characteristics, they need to be complemented by end-to-end metrics.

Third, the choice of model can greatly impact implementation performance. Thus, if implementation A is evaluated on model M and implementation B on model N, a comparison between them is not meaningful, since the observed difference may reflect the properties of the models rather than the implementations themselves. While all existing benchmarks evaluate all included implementations on the same set of model problems, different papers often use different benchmarks—with distinct sets of implementations and model problems—making meaningful comparisons across reported results difficult.

Fourth, the parameter configuration can significantly affect implementation performance. Therefore, handling parameter configurations in a controlled manner is necessary.

Finally, many implementations are continuously optimized and developed, and many performance metrics are inherently hardware-dependent and can vary significantly across different architectures. Therefore, handling hardware and software environments in a controlled manner is necessary.

## 3.3Performance metrics

Having established that performance benchmarks must jointly evaluate computational cost and solution quality to enable meaningful comparisons between implementations, we need metrics that consistently and meaningfully quantify these aspects. Several metrics can be used for this purpose, each capturing different aspects of performance. Regarding metrics for solution quality, three standard ones for DMRG are:
- •

Energy residuals:Solution quality is naturally assessed by accuracy. In DMRG, accuracy is best quantified through the computed energy and energy residuals. Because DMRG is variational and guarantees an upper bound on the ground-state energy, and because the true ground-state energy is a global minimum, lower energies indicate a better outcome of the algorithm.
- •

Energy variance:Similar to energy residuals, while not a direct indicator of accuracy, a relevant metric for solution quality is the energy varianceσH2\sigma_{H}^{2}[76,29]:σH2=⟨ψ|H^2|ψ⟩−⟨ψ|H^|ψ⟩2.\sigma_{H}^{2}=\expectationvalue{\widehat{H}^{2}}{\psi}-\expectationvalue{\widehat{H}}{\psi}^{2}.(5)

The closerσH2\sigma_{H}^{2}is to zero, the more accurately|ψ⟩\ket{\psi}represents an eigenstate of the Hamiltonian. However, low variance does not guarantee that the state is the ground state.
- •

Observables:Observables other than energy can sometimes also help assess solution quality. For example, properties associated with specific symmetries—such as magnetization—can be used to check the quantum-number distribution and ensure that the state lies in the expected sector, providing complementary insight.

Regarding metrics for computational cost, three standard ones include:
- •

Wall time:As a direct measure of time-to-solution, wall time is a practical and intuitive metric.
- •

Memory usage:High peak memory usage can limit the feasibility of large-scale or high-accuracy DMRG simulations and can therefore be an important metric.
- •

FLOPs:The number of floating-point operations (FLOPs) performed is largely hardware-independent and can therefore facilitate comparisons across different hardware systems and provide a useful basis for analyzing implementation efficiency.

Based on measurements of these primary cost metrics, several derived performance metrics can be calculated to add further depth to the analysis. Common metrics include:
- •

Floating-point throughput and efficiency:Achieved floating-point throughput (FLOP/s) is commonly used to calculate the efficiency relative to the hardware’s theoretical peak performance, and indicates how effectively the available computational resources are utilized.
- •

Speedup:Speedup quantifies relative speed improvements and is commonly used to evaluate the effectiveness of algorithmic optimizations and parallel implementations.
- •

Scalability:Scalability shows how efficiently the implementation uses available hardware as compute resources and problem sizes increase. This can include both strong and weak scaling across shared-memory threading, distributed parallelism, and accelerator-based execution such as GPUs.
- •

I/O performanceFor large-scale simulations, I/O can contribute significantly to the total runtime. Metrics such as I/O throughput can quantify this impact.

## 4Experimental setup and procedure

## 4.1Software packages

For our experiments, we test eight open source packages. Together, they span a diverse range of programming languages, maturity levels, and popularity, from well-established tools to more recent developments[69].

More specifically, the eight packages used in our experiments, together with the corresponding versions and a brief description of each, are:
- •

Block2(v0.5.3)[95,4]provides a comprehensive set of DMRG algorithms for use in electronic structure methods and other applications.
- •

ITensorMPS.jl(v0.3.28)[31]provides high-level MPS and MPO functionality, and is part of the broaderITensor[19]ecosystem, building onITensors.jl[32], which offers abstract index management.
- •

MPSKit.jl(v0.13.10)[51]provides high-level tensor network algorithms. It is part of the QuantumKitHub[62]ecosystem and builds onTensorKit.jl[13], which supports generic symmetries.
- •

PyTeNet(v1.2)[50,61]implements quantum tensor network operations and simulations structured around MPS and MPO classes. It acts as a facilitator of algorithmic experimentation.
- •

quimb(v1.12.1)[24,63]is a library for quantum information and many-body calculations, focusing primarily on tensor networks.
- •

Renormalizer(v0.0.11)[66,39,35,65,67]is a tensor network package focused on electron-phonon quantum dynamics.
- •

TeNPy(v1.1.0)[26,27,78]is a library for simulating strongly correlated quantum systems with tensor networks.
- •

YASTN(v1.6.0)[64,93]is a package for differentiable linear algebra with block-sparse tensors.

## 4.2Models

For our experiments, we focus on three standard local lattice models common to condensed matter physics settings: the transverse-field Ising model, the isotropic spin-1 Heisenberg model, and the Fermi–Hubbard model. Together, these models span a range of local Hilbert-space dimensions, entanglement structures, and symmetry properties, providing a representative and challenging testbed for assessing DMRG performance.

## 4.2.1Transverse-field Ising model

We express the transverse field Ising model with the following Hamiltonian:H^=−J​∑⟨i,j⟩σix​σjx−h​∑iσiz,\widehat{H}=-J\sum_{\left\langle i,j\right\rangle}\sigma_{i}^{x}\sigma_{j}^{x}-h\sum_{i}\sigma_{i}^{z},(6)

whereσix\sigma_{i}^{x}andσiz\sigma_{i}^{z}are Pauli operators acting on siteii,⟨i,j⟩\left\langle i,j\right\rangledenotes the set of unordered nearest-neighbor pairs,JJis the nearest-neighbor Ising exchange coupling, andhhis the transverse field strength. Important features of this Hamiltonian include aℤ2\mathbb{Z}_{2}symmetry corresponding to a global spin flip and a quantum critical point separating ordered and disordered phases ath/J=1h/J=1. The associated quantum phase transition leads to long-range correlations at criticality, providing a non-trivial setting for assessing DMRG performance.

Furthermore, for one-dimensional chains with open boundary conditions, analytical expressions for the ground-state energy are available for finite systems[60]. In particular, the ground-state energyE0E_{0}is given byE0/J=1−csc⁡(π2​(2​L+1)),E_{0}/J=1-\csc\left(\frac{\pi}{2(2L+1)}\right),(7)

which provides a useful reference for benchmarking numerical results.

## 4.2.2Spin-1 Heisenberg model

We express the isotropic spin-1 Heisenberg model with the following Hamiltonian:H^=−J​∑⟨i,j⟩S→i⋅S→j=−J​∑⟨i,j⟩(12​[Si+​Sj−+Si−​Sj+]+Siz​Sjz),\widehat{H}=-J\sum_{\left\langle i,j\right\rangle}\vec{S}_{i}\cdot\vec{S}_{j}\\
=-J\sum_{\left\langle i,j\right\rangle}\left(\frac{1}{2}\left[S_{i}^{+}S_{j}^{-}+S_{i}^{-}S_{j}^{+}\right]+S_{i}^{z}S_{j}^{z}\right),(8)

where J is the exchange coupling constant,S→i=(Siz,Siy,Siz)\vec{S}_{i}=(S_{i}^{z},S_{i}^{y},S_{i}^{z})are spin-1 operators acting on siteii, andSi±S_{i}^{\pm}are the corresponding ladder operators. It has fullSU​(2)\mathrm{SU}(2)spin-rotation symmetry corresponding to total spin conservation, with total magnetization conservation arising from itsU​(1)\mathrm{U}(1)subgroup. The model was also among the first to which DMRG was applied[85].

There are no analytical solutions for the ground state energy of the spin-1 Heisenberg antiferromagnet, as the model is non-integrable for spin≥1\geq 1[52]. Nevertheless, numerical studies of finite periodic chains provide estimates in the thermodynamic limit, yielding a ground-state site energy of approximatelyE0=−1.401484038971​|J|E_{0}=-1.401484038971|J|[83,23].

## 4.2.3Fermi–Hubbard model

We express the Fermi–Hubbard model with the following Hamiltonian:H^=−t​∑⟨i,j⟩,σ(c^i,σ†​c^j,σ+c^j,σ†​c^i,σ)+U​∑in^i,↑​n^i,↓,n^i,σ=c^i,σ†​c^i,σ,\widehat{H}=-t\sum_{\left\langle i,j\right\rangle,\sigma}\left(\hat{c}_{i,\sigma}^{\dagger}\hat{c}_{j,\sigma}+\hat{c}_{j,\sigma}^{\dagger}\hat{c}_{i,\sigma}\right)+U\sum_{i}\hat{n}_{i,\uparrow}\hat{n}_{i,\downarrow},\quad\hat{n}_{i,\sigma}=\hat{c}_{i,\sigma}^{\dagger}\hat{c}_{i,\sigma},(9)

wherettis the hopping amplitude,UUis the coupling strength, andc^i,σ†\hat{c}_{i,\sigma}^{\dagger}andc^i,σ\hat{c}_{i,\sigma}are the fermionic creation and annihilation operators of an electron of spinσ∈{↑,↓}\sigma\in\left\{\uparrow,\downarrow\right\}at siteii, respectively. Each site can be empty, occupied by a single spin-up or spin-down electron, or doubly occupied, forming a 4-dimensional local Hilbert space. The model has a rich symmetry structure, namelyU​(2)=U​(1)×SU​(2)\mathrm{U}(2)=\mathrm{U}(1)\times\mathrm{SU}(2), reflecting total particle-number and total spin conservation. Furthermore, at half-filling on bipartite lattices, the particle-number is also a pseudo-spinSU​(2)\mathrm{SU}(2)symmetry emerging from particle-hole transformations associated withη\eta-pairing. Together with spinSU​(2)\mathrm{SU}(2), this enlarges the symmetry toSO​(4)≅SU​(2)η×SU​(2)S/ℤ2\mathrm{SO}(4)\cong\mathrm{SU}(2)_{\eta}\times\mathrm{SU}(2)_{S}/\mathbb{Z}_{2}[92,91].

In one dimension, the model can be solved exactly using the Bethe ansatz[40]. In particular, at half-filling in the thermodynamic limit, we getE0/L=−4​t​∫0∞J0​(ω)​J1​(ω)ω​[1+exp⁡(ω​U/2​t)]​𝑑ω,E_{0}/L=-4t\int_{0}^{\infty}\frac{J_{0}(\omega)J_{1}(\omega)}{\omega\left[1+\exp\left(\omega U/2t\right)\right]}\,d\omega,(10)

whereJ0J_{0}andJ1J_{1}are Bessel functions of the first kind.

## 4.2.4Model setups

For all experiments, we use one-dimensional chains of lengthL=100L=100with open boundary conditions. Regarding the model parameters, we useh/J=1h/J=1for the transverse-field Ising model,eq.6, corresponding to its quantum critical point;J=−1J=-1for the Heisenberg model,eq.8, corresponding to the antiferromagnetic case; andU/t=8U/t=8at half-filling for the Fermi–Hubbard model,eq.9, representing an intermediate-coupling regime.

To validate our experimental results later, we establish reference energies for each model. For the transverse-field Ising model, we obtain the reference energy fromeq.7, givingE0=−126.961876739681E_{0}=-126.961876739681. For the Heisenberg model, we compute the reference energy usingBlock2andMPSKitwithSU​(2)\mathrm{SU(2)}symmetry enforcement and a bond dimension of 1600, obtainingE0=−138.940086166525E_{0}=-138.940086166525. Similarly, for the Fermi–Hubbard model, using the same packages, we compute the reference energy withU​(1)×SU​(2)\mathrm{U(1)}\times\mathrm{SU(2)}symmetry enforcement and a bond dimension of 1600 to beE0=−32.545776173096E_{0}=-32.545776173096.
These computed reference energies are consistent with their corresponding thermodynamic-limit values once finite-size effects and the use of open boundary conditions are accounted for.

## 4.3DMRG setup and measurement

For our experiments, we initialize the MPS as a random state with a fixed bond dimension. To ensure that statistical fluctuations due to the randomness do not affect the results, we average over 10 independent runs.

We only measure performance for the DMRG call, so we exclude the time spent initializing the MPS and constructing the Hamiltonian. For Julia packages, we perform initial warm-up runs to trigger JIT compilation, followed by measurement runs. This ensures that timings reflect the implementation’s performance rather than one-time compilation overhead.

We assess solution quality using the relative error in energy,εr=E−E0|E0|,\varepsilon_{r}=\frac{E-E_{0}}{\left|E_{0}\right|},(11)

and computational cost using wall time. Additionally, we record these metrics at the end of every sweep to examine convergence behavior, providing a more complete picture.

The code used to generate all results presented in this work is publicly available in an online repository[70]. The repository contains the source code, input files, and instructions necessary to reproduce the calculations and figures. The specific version of the code used for this study is archived and tagged to ensure reproducibility.

All calculations were performed on a single core of an Intel Xeon Gold 6132 (Skylake-SP) compute node.

## 5Results

## 5.1Package comparisons

In this section, we present and compare the performance of the software packages, including testing the symmetries each package supports, while aiming to align the simulation parameters as closely as possible across implementations. We do not claim that these settings are optimal for any particular package, nor do we employ advanced or composite strategies. Instead, we use a set of simple, fixed parameter settings across all sweeps to obtain a baseline performance.

We show the results for the transverse-field Ising model inFigure1, the isotropic spin-1 Heisenberg model inFigure2, and the Fermi–Hubbard model inFigure3. In the Fermi–Hubbard test, not all software packages are included:quimbdoes not support the required symmetry,PyTeNetconverged to a different energy of -232.545, andRenormalizerdid not achieve better than10−210^{-2}accuracy after 18 sweeps and multiple hours of computation, with the given settings. Nevertheless, across all three models, the results provide a rich basis for comparison.Figure 1:Performance of DMRG implementations on the transverse-field Ising model using a maximum bond dimension of 100. The top and bottom panels show trivial andℤ2\mathbb{Z}_{2}symmetry enforcement, respectively. Markers mark the end of a full sweep, i.e., a forward and backward pass.Figure 2:Performance of DMRG implementations on the isotropic spin-1 Heisenberg model using a maximum bond dimension of 400. The top and bottom panels show trivial and non-trivial symmetry enforcement, respectively. Markers mark the end of a full sweep, i.e., a forward and backward pass.Figure 3:Performance of DMRG implementations on the Fermi–Hubbard model using a maximum bond dimension of 800. The top and bottom panels show the enforcement of abelian and non-abelian symmetries, respectively. Markers mark the end of a full sweep, i.e., a forward and backward pass.

We observe considerable variation in performance across the packages examined, sometimes with multiple orders of difference in elapsed time to reach a given accuracy—even when enforcing the same symmetry type. For the transverse-field Ising results inFigure1, for example, when enforcing no symmetry, we observe that the package reaching an accuracy of nearly10−1310^{-13}most quickly does so in less than 2 s, whereas the slowest takes nearly 40 s to cross that level, corresponding to nearly a 20-fold difference. Similarly, for the much larger Fermi–Hubbard system results inFigure3, when enforcing aU​(1)×U​(1)\mathrm{U(1)\times\mathrm{U(1)}}symmetry, the package crossing an accuracy of10−1110^{-11}most quickly does so in less than 700 s, whereas the slowest takes more than 3000 s, corresponding to more than a 4-fold difference.

We also observe that including symmetries clearly impacts performance. InFigure1, for example, simulations enforcingℤ2\mathbb{Z}_{2}symmetry consistently outperform those performed without symmetry enforcement. Moreover, when comparing simulations from the same package, enforcing symmetry yields a 2- to 4-fold speedup. InFigure2, the difference is even more pronounced, with the fastest simulations exploiting non-abelianSU​(2)\mathrm{SU(2)}symmetry outperforming most simulations using abelianU​(1)\mathrm{U(1)}symmetry by nearly an order of magnitude. At the same time, the latter themselves tend to be nearly an order of magnitude faster than simulations without symmetry enforcement.

Beyond symmetries, we observe the underlying physical model influencing the relative performance rankings. Different packages carry distinct levels of computational overhead, which vary in prominence depending on the model’s characteristics. Thus, testing a single model is insufficient to characterize a package’s overall performance; a broader set of models is necessary to obtain a more representative and balanced comparison.

These results also show that time per sweep alone is an insufficient metric for assessing performance. For instance, comparing theU​(1)×U​(1)\mathrm{U(1)}\times\mathrm{U(1)}results ofBlock2andMPSKitinFigure3reveals that whileBlock2performs sweeps faster with the given settings,MPSKitgains more accuracy faster. More specifically,Block2achieves an accuracy of nearly10−1010^{-10}in roughly 900 s by performing 18 sweeps; meanwhile,MPSKitreaches the same level of accuracy in roughly 600 s but performs only 6 sweeps. Furthermore, we observe multiple packages having shorter sweep times as they approach convergence, despite using the same settings for all sweeps; for instance, in the trivial results ofRenormalizerinFigure1, the second sweep takes roughly 6 s, whereas the third only takes roughly 3 s. Thus, we show why it is essential to consider the end-to-end interplay between computational cost and solution quality to enable meaningful comparisons across implementations.

Finally, we cannot establish a definitive performance ranking based on these results, as these tests are confined to a specific setting that does not exploit all specialized features or targeted optimizations, which can be unique to individual implementations and could significantly boost performance. Nevertheless, the substantial variation across the packages when evaluating different models and symmetries offers valuable insights for developers and users and provides a useful starting point for further investigation.

## 5.2Parameter tuning and optimization strategies

In this section, we test various settings and strategies for tunable parameters and implementation-specific features, and examine how these choices can affect performance.

## 5.2.1Krylov subspace dimension

InFigure4, we show how changing the Krylov subspace dimension can affect the interplay between computational cost and solution quality.Figure 4:Performance ofMPSKiton the transverse-field Ising model using different Krylov subspace dimensions.

We observe considerable variation in performance across the different settings. Using a larger Krylov subspace dimension can enable faster convergence, but setting it too large can make individual sweeps prohibitively expensive, reducing overall efficiency. As such, we again see that sweep time alone provides limited insight into performance: a faster sweep setting may still require substantially more sweeps to achieve the same accuracy, underscoring the importance of considering the end-to-end interplay between computational cost and solution quality.

Moreover, we observe that parameter choices are not independent. Here specifically, we see how different symmetry settings favor different Krylov settings. More broadly, different models will likely exhibit different optima; here, we study a critical point that will exhibit characteristics distinct from those of non-critical points. This difference suggests that there is no universally best parameter choice and no guarantee that a package’s defaults are always optimal, since they are typically set to fixed values.

Taken together, these results highlight the importance of choosing algorithmic parameters appropriately for the problem at hand to achieve optimal performance. While exploiting symmetries can substantially improve performance, these benefits are only fully realized when the other settings are chosen appropriately as well. In some cases, a poorly tuned configuration with symmetries may even perform worse than a well-tuned one without them. Thus, the practical performance of any package depends heavily on how effectively its parameters can be adapted to the problem at hand. A package having sufficient flexibility to tune and dynamically adjust parameters is therefore essential for achieving robust and efficient performance across a wide range of problems.

## 5.2.2Mixed-precision

InFigure5, we show how reduced floating-point precision can accelerate the early optimization stage without sacrificing final accuracy.Figure 5:Performance ofITensorMPSon the Fermi–Hubbard model using three different floating-point precision strategies: single-precision only, double-precision only, and starting with single- and switching to double-precision after four sweeps. Because the single-precision Hamiltonian yields lower energy due to numerical imprecision, the single-precision result error is calculated as an absolute difference ineq.11rather than a linear one.

When comparing the single-precision convergence with the double-precision convergence up to an accuracy of roughly10−510^{-5}, the accuracy gain per sweep is roughly the same, but, as expected, the sweep time for the single-precision calculation is faster—single-precision requiring 900 s and double-precision requiring 1350 s, roughly, to perform four sweeps. However, beyond this point, the single-precision simulation’s accuracy stagnates due to limited numerical precision, while the double-precision simulation continues to improve, reaching an accuracy below10−1110^{-11}.

This trade-off naturally suggests a mixed-precision strategy. Hence, we also show that combining the two approaches yields a clear practical advantage: By first running in single precision during the early, less sensitive stages of the optimization and then switching to double precision once higher accuracy becomes necessary, we retain the fast initial convergence while still reaching the same final accuracy as the full double-precision run. In this way, while the double-precision simulation requires nearly 2600 s to achieve an accuracy of10−1110^{-11}, the hybrid method requires only 2100 s, corresponding to nearly a 1.24× speedup.

Despite the practical advantage, few packages support mixed-precision workflows directly[69]. Although users can, in many cases, achieve similar behavior by manually restarting or switching precision during optimization, such interventions are cumbersome and are therefore often avoided in practice.

More broadly, these results illustrate the importance of remembering that the DMRG algorithm is iterative, and the optimal settings may change during different stages of an optimization. Hence, flexibility can be essential for achieving maximal performance.

## 5.2.3Update mode

InFigure6, we show how using different update modes—either 1-site or 2-site—at different stages can improve performance by leveraging their respective strengths and minimizing their drawbacks.Figure 6:Performance ofYASTNon the Fermi-Hubbard model using three update mode strategies: 1-site only, 2-site only, and alternating 1-site and 2-site.

We observe that the 1-site method performs sweeps faster for a given bond dimension because it is more computationally cost-effective than the 2-site method. Still, it becomes stuck in a suboptimal configuration, as it tends to do when symmetries are enforced, and it reaches only an accuracy of10−510^{-5}. Moreover, since the traditional 1-site method cannot dynamically increase the bond dimension, it requires starting with the target bond dimension, which can be inefficient during the early stages of the optimization when a large bond dimension is not yet necessary. In contrast, the 2-site method, while slower in sweep times, is more robust and can offset part of the overhead through its adaptability: starting with a small bond dimension and gradually increasing it allows the method to focus computational effort where it is most needed.

Building on these complementary strengths, we show that, since DMRG is iterative, we can combine the two approaches by alternating between 1-site and 2-site sweeps, starting with a small bond dimension and increasing it after every other sweep. This strategy aims to improve performance by using the efficiency of the 1-site updates while relying on the 2-site method to enhance stability and enable controlled growth of the bond dimension. As a result, the hybrid method achieves an accuracy of10−1110^{-11}in just over 1000 s, whereas the pure 2-site method takes nearly 1800 s to reach the same accuracy.

Finally, comparing theseYASTNresults to those inFigure3, where reaching an accuracy of10−1110^{-11}required around 3100 s, simply using a more gradual increase in bond dimension resulted in nearly a 2-fold speedup, and adding the alternating 1-site and 2-site sweeps on top thus yielded more than a 3-fold speedup.

Again, these results illustrate how substantially the performance can depend on the optimization strategy and parameter choices, highlighting the importance of flexibility. While many packages provide both 1-site and 2-site optimization schemes, fewer support seamless switching between them during a calculation.

## 5.2.4Subspace expansion

InFigure7, we show how subspace expansion (SSE) can be used with 1-site DMRG to speed up calculations; similar to density matrix perturbation, it can help 1-site DMRG avoid getting trapped in local minima, but it also enables controlled growth of the bond dimension.Figure 7:Performance ofTeNPyon the Fermi-Hubbard model using 2-site DMRG and 1-site DMRG with and without subspace expansion.

To start, we again observe the typical drawbacks of the traditional 1-site method, i.e., the need to start at the target bond dimension and the tendency to get stuck in local minima when enforcing symmetries, in this case, resulting in only10−210^{-2}accuracy after approximately 200 s. In contrast, the SSE approach largely avoids both issues, achieving an accuracy of nearly10−1010^{-10}in just under 140 s.

Moreover, we observe that the SSE approach offers a competitive advantage over the 2-site method at the outset, as it also allows controlled growth of the bond dimension. However, in this case, after reaching an accuracy of approximately10−810^{-8}, the SSE convergence begins to slow and eventually stagnates, reaching a final accuracy just below10−1010^{-10}, whereas the 2-site method converges to a final accuracy of around5×10−125\times 10^{-12}. Still, up to that point, SSE provides a substantial early-time speedup; for example, we see it reach an accuracy of10−610^{-6}in roughly 40 s, while the 2-site method requires about 80 s to achieve the same level, corresponding to a 2-fold speedup.

Furthermore, as with previous examples, DMRG is iterative, so the best strategy may be to combine the two approaches, using SSE in the low-to-moderate-accuracy regime and then switching to 2-site for the high-accuracy regime. Thus, by looking beyond the final error values themselves, we see that studying convergence behavior provides valuable insight into how each approach operates throughout the optimization process. In particular, we see how it can reveal regimes in which one approach reaches intermediate accuracies substantially faster than another, and in which the latter becomes more efficient near the precision limit. More broadly, this illustrates the value of doing more systematic testing, as it can reveal non-obvious performance trade-offs.

SSE workflows, similar to mixed-precision and mode-hybrid approaches, are supported by only a limited number of packages[69]. This reflects a broader issue in the software landscape, where many packages are developed largely independently, with limited modularity and interoperability. As a result, promising techniques like SSE experience slower dissemination and adoption, despite providing practical benefits.

Finally, comparing theseTeNPyresults to those inFigure3, where achieving an accuracy of10−1110^{-11}took nearly 1400 s, using the 2-site approach with a gradual increase in bond dimension does it in about 270 s, again highlighting just how sensitive these packages can be to the optimization strategies and parameter choices. More importantly, this suggests that selecting an effective optimization strategy can have a greater impact on performance than the choice of package itself, reinforcing the importance of systematic evaluation when assessing and comparing packages.

## 6Discussion and conclusion

We have examined a range of packages and parameter configurations, applying the performance-oriented benchmarking framework presented inSection3. The results showed significant performance differences, up to two orders of magnitude in some cases. Not only were the differences between packages significant when aligning parameters, but they were also significant within the same package when comparing different parameter settings and optimization strategies.

The observed performance sensitivity to the optimization strategy raises an important methodological consideration: whether parameter settings should be aligned across packages or each package should be evaluated under conditions that allow it to fully exploit its capabilities. While aiming to align parameters may improve comparability in some sense, it may underrepresent the strengths of packages that incorporate advanced or specialized features. This issue is particularly relevant given that many of the more recent innovations—e.g., subspace expansion or mixed-precision approaches—are implemented in only a subset of packages, and even fewer packages support multiple such innovations. Furthermore, if the comparison is expanded to include many packages, the set of features and parameter settings shared across all implementations becomes increasingly limited. As a result, comparisons based solely on harmonized settings may not fully reflect the practical performance achievable by state-of-the-art implementations, hindering our ability to assess how each package truly performs relative to the others in practice.

However, attempting to evaluate packages under conditions that reflect their full potential would introduce its own set of challenges and methodological questions. Determining the optimal configuration for your own package, let alone one developed by others, for a given problem is challenging, if not impossible, due to the level of expertise required and the endless number of possible configurations. This challenge thus underscores the value of reproducibility and transparency in benchmarking studies. Even with suboptimal configurations, by clearly documenting parameter settings, optimization strategies, and simulation procedures, researchers enable others to understand, replicate, and critically assess the reported results, thereby strengthening the reliability and interpretability of the performance assessment.

The observed influence of parameter configuration on performance also motivates broader questions regarding the role of parameter tuning itself. In particular, it remains unclear to what extent effective performance requires extensive manual tuning, or whether more general and automated tuning procedures could achieve comparable results across a range of problems and packages.

More generally, our findings raise questions about whether certain parameters have a disproportionately large impact on performance across a wide range of problems, while others play a comparatively minor role. For example, for the models we studied, we observe multiple parameter settings that can significantly impact performance. Moreover, a similar related question is the extent to which optimal parameter settings and optimization strategies depend on the specific problem under consideration; whether some require substantial adjustment across different problem classes, whereas others exhibit robust near-optimal settings that generalize well across a broad range. Identifying such influential parameters and strategies could help focus tuning efforts and simplify practical use.

The results thus also highlight the importance of understanding interactions between parameters and optimization strategies. In particular, it remains unclear whether we can further combine certain strategies to achieve additional performance gains or whether their effects would overlap and interfere negatively with one another. Addressing these questions requires that packages support all available strategies and provide sufficient flexibility to combine them seamlessly. Such flexibility will likely also be essential for achieving maximal performance across a wide range of problems.

Taken together, one thing is for certain: There is significant value and insight to be gained from conducting more rigorous performance evaluations. When they are performed, there needs to be consideration of the interplay between computational cost and solution quality to enable meaningful comparisons. Using the presented benchmarking framework and our results as a starting point, continued benchmarking will ultimately help users and developers make informed decisions and support future development efforts to build better, more efficient software.

## References
- [1]G. Alvarez(2009-09)The density matrix renormalization group for strongly correlated electron systems: a generic implementation.Computer Physics Communications180(9),pp. 1572–1578.External Links:ISSN 0010-4655,DocumentCited by:§3.1.
- [2]G. Alvarez(2012-10)Implementation of the su(2) hamiltonian symmetry for the dmrg algorithm.Computer Physics Communications183(10),pp. 2226–2232.External Links:ISSN 0010-4655,DocumentCited by:§3.1.
- [3]A. Baiardi and M. Reiher(2020-01)The density matrix renormalization group in chemistry and molecular physics: recent developments and new challenges.The Journal of Chemical Physics152(4).External Links:ISSN 1089-7690,DocumentCited by:§3.1.
- [4](2025)Block2.GitHub.Note:External Links:LinkCited by:1st item.
- [5]J. Brabec, J. Brandejs, K. Kowalski, S. Xantheas, Ö. Legeza, and L. Veis(2020-12)Massively parallel quantum chemical density matrix renormalization group method.Journal of Computational Chemistry42(8),pp. 534–544.External Links:ISSN 1096-987X,DocumentCited by:§3.1.
- [6]C. Brower, S. Rodriguez Bernabeu, J. Hammond, J. Gunnels, S. S. Xantheas, M. Ganahl, A. Menczer, and Ö. Legeza(2026-04)Mixed-precisionAb Initiotensor network state methods adapted for nvidia blackwell technology via emulated fp64 arithmetic.Journal of Chemical Theory and Computation.External Links:ISSN 1549-9626,DocumentCited by:§2.2,§3.1.
- [7]G. K. Chan, A. Keselman, N. Nakatani, Z. Li, and S. R. White(2016-07)Matrix product operators, matrix product states, and ab initio density matrix renormalization group algorithms.The Journal of Chemical Physics145(1).External Links:ISSN 1089-7690,DocumentCited by:§3.1.
- [8]G. K. Chan and S. Sharma(2011-05)The density matrix renormalization group in quantum chemistry.Annual Review of Physical Chemistry62(1),pp. 465–481.External Links:ISSN 1545-1593,DocumentCited by:§3.1.
- [9]G. K. Chan(2004-02)An algorithm for large scale density matrix renormalization group calculations.The Journal of Chemical Physics120(7),pp. 3172–3178.External Links:ISSN 1089-7690,DocumentCited by:§3.1.
- [10]F. Chen, C. Cheng, and H. Luo(2020-08)Improved hybrid parallel strategy for density matrix renormalization group method*.Chinese Physics B29(7),pp. 070202.External Links:ISSN 1674-1056,DocumentCited by:§3.1.
- [11]F. Chen, C. Cheng, and H. Luo(2021-07)Real-space parallel density matrix renormalization group with adaptive boundaries.Chinese Physics B30(8),pp. 080202.External Links:ISSN 1674-1056,DocumentCited by:§3.1.
- [12]J. I. Cirac and F. Verstraete(2009-12)Renormalization and tensor product states in spin chains and lattices.Journal of Physics A: Mathematical and Theoretical42(50),pp. 504004.External Links:ISSN 1751-8121,DocumentCited by:§2.1.
- [13]L. Devos and J. Haegeman(2025)TensorKit.jl: a julia package for large-scale tensor computations, with a hint of category theory.arXiv.External Links:DocumentCited by:§3.1,3rd item.
- [14]M. Dolfi, B. Bauer, S. Keller, A. Kosenkov, T. Ewart, A. Kantian, T. Giamarchi, and M. Troyer(2014-12)Matrix product state applications for the alps project.Computer Physics Communications185(12),pp. 3430–3440.External Links:ISSN 0010-4655,DocumentCited by:§3.1.
- [15]J. Dongarra, V. Eijkhout, and H. v. d. Vorst(2001-01)An iterative solver benchmark.Scientific Programming9(4),pp. 223–231.External Links:ISSN 1875-919X,Link,DocumentCited by:§3.1.
- [16]J. Dongarra, M. A. Heroux, and P. Luszczek(2015-08)High-performance conjugate-gradient benchmark: a new metric for ranking high-performance computing systems.The International Journal of High Performance Computing Applications30(1),pp. 3–10.External Links:ISSN 1741-2846,Link,DocumentCited by:§3.1.
- [17]J. J. Dongarra, P. Luszczek, and A. Petitet(2003-07)The linpack benchmark: past, present and future.Concurrency and Computation: Practice and Experience15(9),pp. 803–820.External Links:ISSN 1532-0634,Link,DocumentCited by:§3.1.
- [18]G. Evenbly and G. Vidal(2011-06)Tensor network states and geometry.Journal of Statistical Physics145(4),pp. 891–918.External Links:ISSN 1572-9613,DocumentCited by:§2.1.
- [19]M. Fishman, S. White, and E. Stoudenmire(2022-08)The itensor software library for tensor network calculations.SciPost Physics Codebases.External Links:DocumentCited by:§3.1,2nd item.
- [20]M. Ganahl, J. Beall, M. Hauru, A. G.M. Lewis, T. Wojno, J. H. Yoo, Y. Zou, and G. Vidal(2023-02)Density matrix renormalization group with tensor processing units.PRX Quantum4(1).External Links:ISSN 2691-3399,DocumentCited by:§3.1.
- [21]P. García-Molina, J. J. Rodríguez-Aldavero, J. Gidi, and J. J. García-Ripoll(2026)SeeMPS: a python-based matrix product state and tensor train library.arXiv.External Links:DocumentCited by:§3.1.
- [22]A. Gleis, J. Li, and J. von Delft(2023-06)Controlled bond expansion for density matrix renormalization group ground state search at single-site costs.Physical Review Letters130(24).External Links:ISSN 1079-7114,DocumentCited by:§2.2,§3.1.
- [23]O. Golinelli, Th. Jolicoeur, and R. Lacaze(1994-08)Finite-lattice extrapolations for a haldane-gap antiferromagnet.Physical Review B50(5),pp. 3037–3044.External Links:ISSN 1095-3795,DocumentCited by:§4.2.2.
- [24]J. Gray(2018-09)Quimb: a python package for quantum information and many-body calculations.Journal of Open Source Software3(29),pp. 819.External Links:ISSN 2475-9066,DocumentCited by:§3.1,5th item.
- [25]G. Hager, E. Jeckelmann, H. Fehske, and G. Wellein(2004-03)Parallelization strategies for density matrix renormalization group algorithms on shared-memory systems.Journal of Computational Physics194(2),pp. 795–808.External Links:ISSN 0021-9991,DocumentCited by:§3.1.
- [26]J. Hauschild and F. Pollmann(2018-10)Efficient numerical simulations with tensor networks: tensor network python (tenpy).SciPost Physics Lecture Notes.External Links:DocumentCited by:7th item.
- [27]J. Hauschild, J. Unfried, S. Anand, B. Andrews, M. Bintz, U. Borla, S. Divic, M. Drescher, J. Geiger, M. Hefel, K. Hémery, W. Kadow, J. Kemp, N. Kirchner, V. S. Liu, G. Moller, D. Parker, M. Rader, A. Romen, S. Scalet, L. Schoonderwoerd, M. Schulz, T. Soejima, P. Thoma, Y. Wu, P. Zechmann, L. Zweng, R. Mong, M. Zaletel, and F. Pollmann(2024-11)Tensor network python (tenpy) version 1.SciPost Physics Codebases.External Links:ISSN 2949-804X,DocumentCited by:§3.1,7th item.
- [28]H. Hong, W. Tong, X. Liu, T. Zhang, and X. Liu(2022)High performance single-site finite dmrg on gpus.InCAIBDA 2022; 2nd International Conference on Artificial Intelligence, Big Data and Algorithms,Vol.,pp. 1–5.External Links:DocumentCited by:§3.1.
- [29]C. Hubig, J. Haegeman, and U. Schollwöck(2018-01)Error estimates for extrapolations with matrix-product states.Physical Review B97(4).External Links:ISSN 2469-9969,DocumentCited by:2nd item.
- [30]C. Hubig, I. P. McCulloch, U. Schollwöck, and F. A. Wolf(2015-04)Strictly single-site dmrg algorithm with subspace expansion.Physical Review B91(15).External Links:ISSN 1550-235X,DocumentCited by:§2.2,§3.1.
- [31](2025)ITensorMPS.jl.GitHub.Note:External Links:LinkCited by:2nd item.
- [32](2025)ITensors.jl.GitHub.Note:External Links:LinkCited by:2nd item.
- [33]D. Jaschke, M. Ballarin, N. Reinic, L. Pavesic, and S. Montangero(2026)Benchmarking quantum red tea on cpus, gpus, and tpus.InProceedings of the 10th bwHPC Symposium,pp. 45–60.External Links:ISBN 9783731514015,Link,DocumentCited by:§3.1.
- [34]D. Jaschke, M. L. Wall, and L. D. Carr(2018-04)Open source matrix product states: opening ways to simulate entangled many-body quantum systems in one dimension.Computer Physics Communications225,pp. 59–91.External Links:ISSN 0010-4655,DocumentCited by:§3.1.
- [35]T. Jiang, W. Li, J. Ren, and Z. Shuai(2020-04)Finite temperature dynamical density matrix renormalization group for spectroscopy in frequency domain.The Journal of Physical Chemistry Letters11(10),pp. 3761–3768.External Links:ISSN 1948-7185,DocumentCited by:6th item.
- [36]Y. Kurashige and T. Yanai(2009-06)High-performance ab initio density matrix renormalization group method: applicability to large-scale multireference problems for metal compounds.The Journal of Chemical Physics130(23).External Links:ISSN 1089-7690,DocumentCited by:§3.1,§3.1.
- [37]Ö. Legeza, A. Menczer, Á. Ganyecz, M. A. Werner, K. Kapás, J. Hammond, S. S. Xantheas, M. Ganahl, and F. Neese(2025-06)Orbital optimization of large active spaces via ai-accelerators.Journal of Chemical Theory and Computation21(13),pp. 6545–6558.External Links:ISSN 1549-9626,DocumentCited by:§3.1.
- [38]R. Levy, E. Solomonik, and B. K. Clark(2020-11)Distributed-memory dmrg via sparse and dense parallel tensor contractions.InSC20: International Conference for High Performance Computing, Networking, Storage and Analysis,pp. 1–14.External Links:DocumentCited by:§3.1.
- [39]W. Li, J. Ren, and Z. Shuai(2020-01)Numerical assessment for accuracy and gpu acceleration of td-dmrg time evolution schemes.The Journal of Chemical Physics152(2).External Links:ISSN 1089-7690,DocumentCited by:§3.1,6th item.
- [40]E. H. Lieb and F. Y. Wu(1968-06)Absence of mott transition in an exact solution of the short-range, one-band model in one dimension.Physical Review Letters20(25),pp. 1445–1448.External Links:ISSN 0031-9007,DocumentCited by:§4.2.3.
- [41]L. P. Lindoy, D. Rodrigo-Albert, Y. Rath, and I. Rungger(2025-11)PyTTN: an open-source toolbox for open and closed system quantum dynamics simulations using tree tensor networks.The Journal of Chemical Physics163(20).External Links:ISSN 1089-7690,DocumentCited by:§3.1.
- [42]X. Liu, H. Hong, Z. Zhang, W. Tong, J. Kossaifi, X. Wang, and A. Walid(2024-11)High-performance tensor-train primitives using gpu tensor cores.IEEE Transactions on Computers73(11),pp. 2634–2648.External Links:ISSN 2326-3814,DocumentCited by:§3.1.
- [43]P. Mattson, V. J. Reddi, C. Cheng, C. Coleman, G. Diamos, D. Kanter, P. Micikevicius, D. Patterson, G. Schmuelling, H. Tang, G. Wei, and C. Wu(2020-03)MLPerf: an industry standard benchmark suite for machine learning performance.IEEE Micro40(2),pp. 8–16.External Links:ISSN 1937-4143,Link,DocumentCited by:§3.1.
- [44]I. P. McCulloch and M. Gulácsi(2002-03)The non-abelian density matrix renormalization group algorithm.Europhysics Letters (EPL)57(6),pp. 852–858.External Links:ISSN 1286-4854,DocumentCited by:§2.1,§3.1.
- [45]A. Menczer, K. Kapás, M. A. Werner, and Ö. Legeza(2024-05)Two-dimensional quantum lattice models via mode optimized hybrid cpu-gpu density matrix renormalization group method.Physical Review B109(19).External Links:ISSN 2469-9969,DocumentCited by:§3.1.
- [46]A. Menczer and Ö. Legeza(2024)Cost optimized ab initio tensor network state methods: industrial perspectives.arXiv.External Links:DocumentCited by:§3.1.
- [47]A. Menczer and Ö. Legeza(2024-10)Tensor network state algorithms on ai accelerators.Journal of Chemical Theory and Computation20(20),pp. 8897–8910.External Links:ISSN 1549-9626,DocumentCited by:§3.1.
- [48]A. Menczer and Ö. Legeza(2025-02)Massively parallel tensor network state algorithms on hybrid cpu-gpu based architectures.Journal of Chemical Theory and Computation21(4),pp. 1572–1587.External Links:ISSN 1549-9626,DocumentCited by:§3.1.
- [49]A. Menczer, M. van Damme, A. Rask, L. Huntington, J. Hammond, S. S. Xantheas, M. Ganahl, and Ö. Legeza(2024-09)Parallel implementation of the density matrix renormalization group method achieving a quarter petaflops performance on a single dgx-h100 gpu node.Journal of Chemical Theory and Computation20(19),pp. 8397–8404.External Links:ISSN 1549-9626,DocumentCited by:§3.1.
- [50]C. Mendl(2018-10)PyTeNet: a concise python implementation of quantum tensor network algorithms.Journal of Open Source Software3(30),pp. 948.External Links:ISSN 2475-9066,DocumentCited by:§3.1,4th item.
- [51](2025)MPSKit.jl.GitHub.Note:External Links:LinkCited by:3rd item.
- [52]G. Müller, J. C. Bonner, and J. B. Parkinson(1987-04)Nonintegrability and quantum spin chains.Journal of Applied Physics61(8),pp. 3950–3952.External Links:ISSN 1089-7550,DocumentCited by:§4.2.2.
- [53]R. C. Murphy, K. B. Wheeler, B. W. Barrett, and J. A. Ang(2010)Introducing the graph 500.Cray Users Group (CUG)19(45-74),pp. 22.Cited by:§3.1.
- [54]N. Nakatani and G. K. Chan(2013-04)Efficient tree tensor network states (ttns) for quantum chemistry: generalizations of the density matrix renormalization group algorithm.The Journal of Chemical Physics138(13).External Links:ISSN 1089-7690,DocumentCited by:§2.1.
- [55]C. Nemes, G. Barcza, Z. Nagy, Ö. Legeza, and P. Szolgay(2014-06)The density matrix renormalization group algorithm on kilo-processor architectures: implementation and trade-offs.Computer Physics Communications185(6),pp. 1570–1581.External Links:ISSN 0010-4655,DocumentCited by:§3.1.
- [56]R. Olivares-Amaya, W. Hu, N. Nakatani, S. Sharma, J. Yang, and G. K. Chan(2015-01)The ab-initio density matrix renormalization group in practice.The Journal of Chemical Physics142(3).External Links:ISSN 1089-7690,DocumentCited by:§2.2.
- [57]R. Orús(2014-10)A practical introduction to tensor networks: matrix product states and projected entangled pair states.Annals of Physics349,pp. 117–158.External Links:ISSN 0003-4916,DocumentCited by:§2.1.
- [58]R. Orús(2019-08)Tensor networks for complex quantum systems.Nature Reviews Physics1(9),pp. 538–550.External Links:ISSN 2522-5820,DocumentCited by:§2.1.
- [59]I. V. Oseledets(2011-01)Tensor-train decomposition.SIAM Journal on Scientific Computing33(5),pp. 2295–2317.External Links:ISSN 1095-7197,DocumentCited by:§2.1.
- [60]P. Pfeuty(1970-03)The one-dimensional ising model with a transverse field.Annals of Physics57(1),pp. 79–90.External Links:ISSN 0003-4916,DocumentCited by:§4.2.1.
- [61](2025)PyTeNet.GitHub.Note:External Links:LinkCited by:4th item.
- [62](2025)QuantumKitHub.GitHub.External Links:LinkCited by:3rd item.
- [63](2025)quimb.GitHub.Note:External Links:LinkCited by:5th item.
- [64]M. Rams, G. Wojtowicz, A. Sinha, and J. Hasik(2025-02)YASTN: yet another symmetric tensor networks; a python library for abelian symmetric tensor network calculations.SciPost Physics Codebases.External Links:ISSN 2949-804X,DocumentCited by:§3.1,8th item.
- [65]J. Ren, W. Li, T. Jiang, Y. Wang, and Z. Shuai(2022-03)Time‐dependent density matrix renormalization group method for quantum dynamics in complex systems.WIREs Computational Molecular Science12(6).External Links:ISSN 1759-0884,DocumentCited by:6th item.
- [66]J. Ren, Z. Shuai, and G. Kin-Lic Chan(2018-08)Time-dependent density matrix renormalization group algorithms for nearly exact absorption and fluorescence spectra of molecular aggregates at both zero and finite temperature.Journal of Chemical Theory and Computation14(10),pp. 5027–5039.External Links:ISSN 1549-9626,DocumentCited by:6th item.
- [67](2025)Renormalizer.GitHub.Note:External Links:LinkCited by:6th item.
- [68]U. Schollwöck(2011-01)The density-matrix renormalization group in the age of matrix product states.Annals of Physics326(1),pp. 96–192.External Links:ISSN 0003-4916,DocumentCited by:§2.1,§2.1,§2.1,§2.1,§2.1,§2.1,§2.1,§2.1,§3.1.
- [69]P. Sehlstedt, J. Brandejs, P. Bientinesi, and L. Karlsson(2026-07)The software landscape for the density matrix renormalization group.Computer Physics Communications324,pp. 110136.External Links:ISSN 0010-4655,DocumentCited by:§1,§3.1,§4.1,§5.2.2,§5.2.4.
- [70]P. Sehlstedt(2026)DMRG-Benchmarks.GitHub.External Links:LinkCited by:§4.3.
- [71]Y.-Y. Shi, L.-M. Duan, and G. Vidal(2006-08)Classical simulation of quantum many-body systems with a tree tensor network.Physical Review A74(2).External Links:ISSN 1094-1622,DocumentCited by:§2.1.
- [72]T. Shiozaki(2017-08)BAGEL: brilliantly advanced general electronic‐structure library.WIREs Computational Molecular Science8(1).External Links:ISSN 1759-0884,DocumentCited by:§3.1.
- [73]E. Solomonik, D. Matthews, J. R. Hammond, J. F. Stanton, and J. Demmel(2014-12)A massively parallel tensor contraction framework for coupled-cluster computations.Journal of Parallel and Distributed Computing74(12),pp. 3176–3190.External Links:ISSN 0743-7315,DocumentCited by:§3.1.
- [74]Y. Song, Y. Tian, Y. Cheng, and H. Ma(2025-08)Recent implementations in kylin 1.3: improved computational efficiency ofab initiodmrg and a spin-adapted version of ec-mrci.Chinese Journal of Chemical Physics38(4),pp. 447–456.External Links:ISSN 2327-2244,DocumentCited by:§3.1.
- [75]E. M. Stoudenmire and S. R. White(2013-04)Real-space parallel density matrix renormalization group.Physical Review B87(15).External Links:ISSN 1550-235X,DocumentCited by:§3.1.
- [76]E.M. Stoudenmire and S. R. White(2012-03)Studying two-dimensional systems with the density matrix renormalization group.Annual Review of Condensed Matter Physics3(1),pp. 111–128.External Links:ISSN 1947-5462,DocumentCited by:§2.2,2nd item,§3.1.
- [77]K. Szenes, N. Glaser, M. Erakovic, V. Barandun, M. Mörchen, R. Feldmann, S. Battaglia, A. Baiardi, and M. Reiher(2025-08)QCMaquis 4.0: multipurpose electronic, vibrational, and vibronic structure and dynamics calculations with the density matrix renormalization group.The Journal of Physical Chemistry A.External Links:ISSN 1520-5215,DocumentCited by:§3.1.
- [78](2025)TeNPy.GitHub.Note:External Links:LinkCited by:7th item.
- [79]Y. Tian and H. Ma(2023-06)High-performance computing for density matrix renormalization group.Current Chinese Science3(3),pp. 178–186.External Links:ISSN 2210-2981,DocumentCited by:§2.2,§3.1.
- [80]Y. Tian, Z. Xie, Z. Luo, and H. Ma(2022-11)Mixed-precision implementation of the density matrix renormalization group.Journal of Chemical Theory and Computation18(12),pp. 7260–7271.External Links:ISSN 1549-9626,DocumentCited by:§2.2,§3.1.
- [81]A. Weichselbaum(2012-12)Non-abelian symmetries in tensor networks: a quantum symmetry space approach.Annals of Physics327(12),pp. 2972–3047.External Links:ISSN 0003-4916,DocumentCited by:§2.1,§3.1.
- [82]A. Weichselbaum(2024-11)QSpace - an open-source tensor library for abelian and non-abelian symmetries.SciPost Physics Codebases.External Links:ISSN 2949-804X,DocumentCited by:§3.1.
- [83]S. R. White and D. A. Huse(1993-08)Numerical renormalization-group study of low-lying eigenstates of the antiferromagnetics=1 heisenberg chain.Physical Review B48(6),pp. 3844–3852.External Links:ISSN 1095-3795,DocumentCited by:§4.2.2.
- [84]S. R. White(1992-11)Density matrix formulation for quantum renormalization groups.Physical Review Letters69(19),pp. 2863–2866.External Links:ISSN 0031-9007,DocumentCited by:§1,§2.1.
- [85]S. R. White(1993-10)Density-matrix algorithms for quantum renormalization groups.Physical Review B48(14),pp. 10345–10356.External Links:ISSN 1095-3795,DocumentCited by:§1,§2.1,§4.2.2.
- [86]S. R. White(2005-11)Density matrix renormalization group algorithms with a single center site.Physical Review B72(18).External Links:ISSN 1550-235X,DocumentCited by:§2.2,§3.1.
- [87]S. Wouters, W. Poelmans, P. W. Ayers, and D. Van Neck(2014-06)CheMPS2: a free open-source spin-adapted implementation of the density matrix renormalization group for ab initio quantum chemistry.Computer Physics Communications185(6),pp. 1501–1514.External Links:ISSN 0010-4655,DocumentCited by:§3.1.
- [88]S. Wouters and D. Van Neck(2014-09)The density matrix renormalization group for ab initio quantum chemistry.The European Physical Journal D68(9).External Links:ISSN 1434-6079,DocumentCited by:§3.1.
- [89]K. Wu, C. Lin, K. Hsu, H. Hung, M. Schneider, C. Chung, Y. Kao, and P. Chen(2025-03)The cytnx library for tensor networks.SciPost Physics Codebases.External Links:ISSN 2949-804X,DocumentCited by:§3.1.
- [90]C. Xiang, W. Jia, W. Fang, and Z. Li(2024-01)Distributed multi-gpu ab initio density matrix renormalization group algorithm with applications to the p-cluster of nitrogenase.Journal of Chemical Theory and Computation20(2),pp. 775–786.External Links:ISSN 1549-9626,DocumentCited by:§3.1.
- [91]C. N. Yang and S.C. Zhang(1990-06)SO4symmetry in a hubbard model.Modern Physics Letters B04(11),pp. 759–766.External Links:ISSN 1793-6640,DocumentCited by:§4.2.3.
- [92]C. N. Yang(1989-11)η\etaPairing and off-diagonal long-range order in a hubbard model.Physical Review Letters63(19),pp. 2144–2147.External Links:ISSN 0031-9007,DocumentCited by:§4.2.3.
- [93](2025)YASTN.GitHub.Note:External Links:LinkCited by:8th item.
- [94]H. Zhai and G. K. Chan(2021-06)Low communication high performance ab initio density matrix renormalization group algorithms.The Journal of Chemical Physics154(22).External Links:ISSN 1089-7690,DocumentCited by:§2.2,§3.1.
- [95]H. Zhai, H. R. Larsson, S. Lee, Z. Cui, T. Zhu, C. Sun, L. Peng, R. Peng, K. Liao, J. Tölle, J. Yang, S. Li, and G. K. Chan(2023-12)Block2: a comprehensive open source framework to develop and apply state-of-the-art dmrg algorithms in electronic structure and beyond.The Journal of Chemical Physics159(23).External Links:ISSN 1089-7690,DocumentCited by:§3.1,1st item.

## 


- 


Major funding support from
