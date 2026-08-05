# Architecture-agnostic analysis of partially coherent light with programmable photonics

**arXiv ID**: 2607.24104v1
**Authors**: Kevin Zelaya, Matthew Markowitz, Jonathan Friedman, Mohammad-Ali Miri
**Published**: 2026-07-27
**Categories**: physics.optics, math-ph
**HTML URL**: https://arxiv.org/html/2607.24104v1

## Abstract

The precise characterization of the spatial degree of coherence of a radiation field is important for assessing its suitability for specific applications in optical communications, advanced imaging, and quantum information processing. However, measuring the full coherence matrix traditionally requires complex, phase-sensitive interferometric setups that are highly susceptible to noise and difficult to scale on integrated platforms. To address this, we propose an architecture-agnostic approach for analyzing partially coherent light that is compatible with any universal programmable photonic unitary circuit, regardless of its internal topology. Leveraging the Schur-Horn theorem, our method diagonalizes the output coherence matrix, enabling direct extraction of its eigenvalues from output power measurements alone. We numerically validate this framework across various universal topologies and demonstrate its efficacy even in under-parameterized, non-universal architectures with only minor loss in precision. Finally, our black-box optimization approach proves inherently resilient to arbitrary optical losses and component deviations, paving the way for robust, lower-depth, and programmable spatial coherence analyzers.

## Full Text

Architecture-agnostic analysis of partially coherent light with programmable photonics

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- License: CC BY-NC-ND 4.0arXiv:2607.24104v1 [physics.optics] 27 Jul 2026

## Architecture-agnostic analysis of partially coherent light with programmable photonicsKevin ZelayaDepartment of Electrical and Microelectronic Engineering, Rochester Institute of Technology, Rochester, New York 14623, USAMatthew MarkowitzDepartment of Electrical and Microelectronic Engineering, Rochester Institute of Technology, Rochester, New York 14623, USAJonathan FriedmanDepartment of Electrical and Microelectronic Engineering, Rochester Institute of Technology, Rochester, New York 14623, USAMohammad-Ali MiriDepartment of Electrical and Microelectronic Engineering, Rochester Institute of Technology, Rochester, New York 14623, USAali.miri@rit.edu

## Abstract

The precise characterization of the spatial degree of coherence of a radiation field is important for assessing its suitability for specific applications in optical communications, advanced imaging, and quantum information processing. However, measuring the full coherence matrix traditionally requires complex, phase-sensitive interferometric setups that are highly susceptible to noise and difficult to scale on integrated platforms. To address this, we propose an architecture-agnostic approach for analyzing partially coherent light that is compatible with any universal programmable photonic unitary circuit, regardless of its internal topology. Leveraging the Schur-Horn theorem, our method diagonalizes the output coherence matrix, enabling direct extraction of its eigenvalues from output power measurements alone. We numerically validate this framework across various universal topologies and demonstrate its efficacy even in under-parameterized, non-universal architectures with only minor loss in precision. Finally, our black-box optimization approach proves inherently resilient to arbitrary optical losses and component deviations, paving the way for robust, lower-depth, and programmable spatial coherence analyzers.††journal:opticajournal

Introduction– Optical coherence is a physical quantity that characterizes the phase correlation of a light wavefront. Two types of optical coherence are of interest: temporal and spatial coherence. Temporal coherence measures the stability of this phase along the direction of propagation over a specific period. In turn, spatial coherence describes the phase correlation between different points across the transverse profile of the wave, which ultimately determines the ability to form stable interference patterns. Indeed, the higher the coherence of the radiation field, the higher the contrast of interference patterns in diffraction experiments[1], such as Young’s double-slit and Michelson’s experiments. In contrast, some applications require partially coherent fields to mitigate the scattered speckle patterns[2]. Among the different mechanisms for characterizing the spatial coherence of classical radiation fields, Photonic Integrated Circuits (PICs) are a particularly useful platform, as they enable the integration of complex optical components in a small form factor. This reduces the calibration effects that typically hinder characterization in free-space optics and also enables tunability and on-chip control of light, which is useful for post-fabrication calibration if manufacturing defects are present.

Linear discrete unitary transformations form the basis of optical system analysis, as such transformations naturally result from light propagation in free space and dielectric media. Since general unitary matricesU​(N)U(N)can be factored into sequences of smaller-dimensionalU​(2)U(2)transforms[3,4], their implementation becomes feasible with optical components. Indeed, such a modular approach was proposed in free-space by Recket al.by using beam splitters, mirrors, and waveplates[3]. In integrated photonics, tunableU​(2)U(2)transformations can be implemented using directional couplers[5]and ring resonators[6]as passive components, combined with phase shifters as active components. Various integrated topologies based onU​(2)U(2)decompositions have been explored in the literature; notable examples include the rectangular network by Clementset al.[7]and diamond-like topologies[8,9], which enable alternative strategies for integrating universal unitary transforms. To bypass theU​(2)U(2)decomposition, other successful approaches have utilizedNN-port couplers as passive components, interlacing them with phase shifters[10,11]. These designs can be deployed through waveguide arrays[12]and multimode interferometers (MMIs)[13], enabling overparameterized unitaries and error-resilient performance[14].

In this letter, we introduce an in-situ method for analyzing the spatial optical coherence of radiation fields using PICs, regardless of the internal topology. This enables an architecture-agnostic approach that treats the PIC as a black box and operates in nonideal scenarios. We explore this by numerically demonstrating that non-universal, low-depth, and lossy architectures can achieve coherence analysis with only a minor precision penalty, paving the way for faster, programmable solutions with a reduced physical footprint.

Results– Throughout the letter, we consider a radiation field𝐄​(𝐫,t)\mathbf{E}(\mathbf{r},t)sampled at the spatial points𝐫i\mathbf{r}_{i}, fori∈{1,…,N}i\in\{1,\ldots,N\}. The sampled points are encoded into a complex-valued vector𝐱​(t)∈ℂN\mathbf{x}(t)\in\mathbb{C}^{N}, with itsii-th component containing, without loss of generality, a specific polarization component of the transverse electric field component at the point𝐫i\mathbf{r}_{i}. In this form,𝐱\mathbf{x}carries information about the spatial coherence of the original field, which is more conveniently represented through thecoherence matrix[15]defined asρ=⟨𝐱​(t)​𝐱​(t)†⟩\rho=\langle\mathbf{x}(t)\mathbf{x}(t)^{\dagger}\rangle. Here,𝐱†\mathbf{x}^{\dagger}is the conjugate transpose of𝐱\mathbf{x}, and⟨⋅⟩\langle\cdot\rangledenotes the ensemble or time average of the radiation field. Thus,ρ\rhoencodes spatial correlation between the different spatial sampling points. Mathematically, by assuming that fields are statistically stationary[1], it is straightforward to see that the coherence matrix is both Hermitian and positive semi-definite. These two properties allow factoring the coherence matrix via its eigen-decompositionρ=V​Λ​V†\rho=V\Lambda V^{\dagger}, withVVa unitary matrix (V∈𝒰​(N)V\in\mathcal{U}(N)), andΛ=diag​(λ1,…,λN)\Lambda=\textnormal{diag}(\lambda_{1},\ldots,\lambda_{N})a diagonal matrix containing the positive semi-definite eigenvalues (λn≥0\lambda_{n}\geq 0) sorted in non-increasing order (λn≥λn+1\lambda_{n}\geq\lambda_{n+1}, forn∈{1,…,N−1}n\in\{1,\ldots,N-1\}).

The coherence matrix we work with consists solely of second-order correlation components across different sampling points. These second-order correlations are fundamental because they directly quantify phase stability and mutual intensity across spatial locations, revealing the underlying spatial coherence of the field and its capacity to form stable interference patterns. Precise analysis of this spatial degree of coherence is particularly required in advanced imaging applications, such as mitigating crosstalk in optical coherence tomography[16]and speckle patterns[2].Figure 1:Algorithmic approach and numerical performance.aSchematic of the architecture-agnostic coherence matrix analyzer. A programmable unitary device (black box) is controlled by the parameter setΦ\Phi. Power detectors (PD) record the output powersPiP_{i}, which are used to compute a figure of merit,ℒ\mathcal{L}. A parameter driver iteratively updatesΦ\Phibased on these measurements untilℒ\mathcal{L}is minimized. The left dashed box depicts the magnitude and phase of randomly sampled coherence matrices of various types. The right dashed box illustrates the output after the unitary network diagonalizes the input coherence matrix.bExample of various topologies for universal unitary PICs, comprising MZI-based networks such as Reck[3]and Clemments[7], as well as multiport coupler networks[17,11,18].cNumerical simulation results showcasing the error between the original and the reconstructed eigenvalues using our architecture-agnostic approach with the universal unitary topologies shown in panelb.

Let us assume that the partially coherent field sampled at theNNpoints is fed into a general linear transformA∈G​L​(N)A\in GL(N). Following the definition of the coherence matrix, and assuming that the changes in time of the linear transformer are much larger than the statistical fluctuations of the fields, one can see that the coherence matrix produced at the output of the linear transformer becomesρout=A​ρ​A†\rho_{\textnormal{out}}=A\rho A^{\dagger}. The degree of coherence is measured by the rank of the coherence matrix; however, reconstructing the full coherence matrix is challenging and, in some experimental setups, even prohibitive. In turn, it is more convenient to reconstruct only its eigenvalues, which already encode the degree of coherence and can be used to analyze the coherence content, as proven successful in Ref.[19]. The structure of the coherence matrix can be modified in two ways:
- •

Unitary control,A∈U​(N)A\in U(N), shuffles the correlation components while preserving the degree of coherence. This is a handy resource for controlling the scattering and absorption dynamics of radiation fields before reaching the scatterer[20,21].
- •

Introducing losses into the network modifies the eigenvalues of the coherence matrix, altering the degree of coherence. Such losses break the unitary evolution and induce a general linear transformA∈G​L​(N)⊃U​(N)A\in GL(N)\supset U(N)instead. Still, the output density matrix transforms asρout=A​ρin​A†\rho_{\textnormal{out}}=A\rho_{\textnormal{in}}A^{\dagger}and satisfies the coherence matrix conditions.

The diagonal componentρn,n\rho_{n,n}is proportional to the intensities at thenn-th sampling point, forn∈{1,…,N}n\in\{1,\ldots,N\}. The total intensity is proportional to the trace ofρ\rho, which, without loss of generality, we normalize to unity (tr​ρ=1\textnormal{tr}\rho=1). We begin the analysis by focusing on parameterizedNN-dimensional unitary matrices,U​(Φ):ℝK→ℂN×NU(\Phi):\mathbb{R}^{K}\rightarrow\mathbb{C}^{N\times N}, which are not necessarily universal. Here,KKdenotes the total number of real-valued parameters inΦ={ϕk}k=1K\Phi=\{\phi_{k}\}_{k=1}^{K}controlling the transfer matrix of the unitary network, the specifics of which depend on the network design.

Fig.1aillustrates a typical experimental setup scenario involving a general linear transform, the input radiation field to be analyzed, and the power gathering and processing. The power measurements at the device output correspond to the diagonal components of the coherence matrix,(ρout)n​n(\rho_{\textnormal{out}})_{nn}. Interestingly, if the coherence matrix is already diagonal, the power measurements correspond to the singular values of the output radiation field, up to a normalization constant. From the mathematical standpoint, one can achieve such a diagonalization if the parametersΦ\Phiof the unitary processor are chosen such thatU​(Φ)=V†U(\Phi)=V^{\dagger}. This reduces the output coherence matrix toρout=Λ\rho_{\textnormal{out}}=\Lambda, from which the analysis of the coherence degree becomes immediate.

The diagonalization approach has been shown to be successful in Ref.[19]via a photonic triangular unitary network with the topology of Recket al.[3]. The latter network is suited for this task, as its topology allows layer-wise manipulation of light, maximizing output power at the ports in a descending manner. Once the power at a given output port is maximized, the network allows for independent tuning of the subsequent layer without interfering with the previous steps. Likewise, a similar approach has been implemented in Ref.[22]with a hexagonal-like photonic unit. However, complete knowledge of the network topology is not always possible, nor can its performance be ensured in non-ideal scenarios. Thus, to make the analysis of coherence matrices widely applicable across different network topologies, we propose an experimentally aware method that is independent of the unitary photonic architecture and treats the PIC as a black box.

Since theNNpower measurements at the network output sample the diagonal components of the output coherence matrix, and the network performs unitary operations, the eigenvalues of the output coherence matrixρout\rho_{\textnormal{out}}are preserved. Thus, to extract the coherence matrix eigenvalues, we shall ensure that the output coherence matrix is diagonal; in that case, the power measurements correspond, up to a normalization factor, to the coherence matrix eigenvalues. Although full characterization of the coherence matrix is beyond the scope of this letter, the diagonalization condition can be assessed only by measuring the output power. This can be ensured via theSchur–Horn theorem[23]: LetX={x1≥x2≥…xN,xn∈ℝ}X=\{x_{1}\geq x_{2}\geq\ldots x_{N},x_{n}\in\mathbb{R}\}andY={y1≥y2≥…yN,yn∈ℝ}Y=\{y_{1}\geq y_{2}\geq\ldots y_{N},y_{n}\in\mathbb{R}\}be two sequences of non-increasing real numbers; then, there is a Hermitian matrixHHwith diagonal componentsYYand eigenvaluesXXif and only if∑n=1K(xn−yn)≥0\sum_{n=1}^{K}(x_{n}-y_{n})\geq 0, for allK={1,…,N}K=\{1,\ldots,N\}. Since coherence matrices satisfy this condition, normalized power measurements will never exceed the normalized coherence matrix eigenvalues. Furthermore, the equality in Schur-Horn’s theorem holds when the coherence matrix is already diagonal.

We can leverage Schur-Horn’s theorem to define an objective that converts any incident radiation field into diagonal form, without prior knowledge of the linear unitary network or the incident field. To this end, let us define the relative power vector𝐏~​(Φ)=(P~1,…,P~N−1),P~n=1−∑k=1nPk​(Φ),\widetilde{\mathbf{P}}(\Phi)=(\widetilde{P}_{1},\ldots,\widetilde{P}_{N-1}),\quad\widetilde{P}_{n}=1-\sum_{k=1}^{n}P_{k}(\Phi),(1)

wherePn​(Φ)≡(ρout)n,nP_{n}(\Phi)\equiv(\rho_{\textnormal{out}})_{n,n}are the normalized power measuresd at thenn-th output port. By following the Schur-Horn theorem, the output coherence matrixρout\rho_{\textnormal{out}}takes a diagonal form whenever thenn-th cumulative power,∑k=1nPk\sum_{k=1}^{n}P_{k}, is maximal for eachnn. This is, in turn, equivalent to the minimization problemminΦ∈𝒮​‖𝐏~​(Φ)‖2.\underset{\Phi\in\mathcal{S}}{\textnormal{min}}\|\mathbf{\widetilde{\mathbf{P}}}(\Phi)\|^{2}.(2)

It is worth stressing that the latter is independent of the unitary architecture topology, i.e., architecture agnostic. Such a feature is useful if the unitary network at hand has not been previously characterized or if the inner topology makes it difficult to estimate the light-travel paths in each section. For instance, in Ref.[19], the topology of the triangular network is leveraged to steer the incoming radiation field in a sequential process until the diagonal matrix becomes diagonal. Likewise, the hexagonal topology in Ref.[22]follows a similar reasoning.

The simple yet robust approach presented here enables an error-resilient strategy: if individual components deviate from ideal behavior due to thermal crosstalk or other unwanted effects, our approach treats the entire device as a black box and applies compensation to the active components as needed. Furthermore, for the numerical assessment of the proposed method, the exact gradients of the objective function can be readily obtained, expediting our numerical tests, especially for systems with a large number of active parameters.

To numerically validate our architecture-agnostic approach, we consider three network topologies: Reck[3], Clements[7], and interlaced multiport-coupler[17,11,18]architectures. For the interlaced structure, illustrated at the bottom of Fig.1b, we parameterize the network by the number of layers (M∈𝐙+M\in\mathbf{Z}^{+}) using the transfer matrixUint​(Φ)=F​P​(ΦM)​F​…​F​P​(Φ1)​FU_{\textnormal{int}}(\Phi)=FP(\Phi^{M})F\ldots FP(\Phi_{1})F.F∈U​(N)F\in U(N)is the unitary transfer matrix corresponding to a passive multiport coupler, which is an splits the light among its output ports without introducing gain or loss. Furthermore,P​(Φ(m))=diag​(ei​ϕ1(m),…,ei​ϕN(m))P(\Phi^{(m)})=\textnormal{diag}(e^{i\phi_{1}^{(m)}},\ldots,e^{i\phi_{N}^{(m)}})represents themm-th programmable and diagonal phase layer, whereϕn(m)\phi_{n}^{(m)}sets the controllable phase shift for thenn-th arm of themm-th layer. We denote the set of phase parameters asΦ=∪m=1MΦ(m)\Phi=\cup_{m=1}^{M}\Phi^{(m)}.

To ensure a comprehensive evaluation across these topologies, we generate three random sets ofNN-point fully coherent (FC), partially coherent (PC), and fully incoherent (FI) matrices for variousNN, where each set contains 500 random samples. The error between the eigenvalues of the original targets (λn\lambda_{n}) and the reconstructed eigenvalues (λ~n\widetilde{\lambda}_{n}) is computed through the standard distance metricd​(𝚲,𝚲~)=∑n=1N(λn−λ~n)2N.d(\mathbf{\Lambda},\widetilde{\mathbf{\Lambda}})=\sum_{n=1}^{N}\frac{(\lambda_{n}-\widetilde{\lambda}_{n})^{2}}{N}.

The statistical information of the error for each ensemble of samples is presented in the bar plots of Fig.1c. The results for the interlaced network were performed using the universal setup withM=N+1M=N+1layers[17]. These results show that no significant performance penalty is observed when transitioning across various network topologies and port sizes.

The architecture-agnostic framework of the proposed coherence analyzer proves handy when considering under-parameterized networks, since the exact diagonalization condition can be relaxed to the approximationU​(Φ)​V†≈𝕀U(\Phi)V^{\dagger}\approx\mathbb{I}. Indeed, in other scenarios, the universality is not required for optical computing tasks, and a lower-depth network suffices for tasks such as photonic state generation[24]and matrix randomization and encryption[25]. We thus consider a truncated interlaced network withM<N+1M<N+1layers, as shown in Fig.2a, and perform the coherence analysis on an ensemble of 500 random samples for each combination ofNNandMM. We separate the analysis for ensembles of random fully coherent (FC), partially coherent (PC), and fully incoherent (FI) matrices. The objective function can extract the eigenvalue with as few as three layers for PI light, with an error of around10−310^{-3}forN=8N=8and10−410^{-4}forN=20N=20.Figure 2:Performance against truncation and losses.aNon-universal interlaced network andbImpact of inherent arbitrary losses in the interlaced unitary network. The losses are randomly assigned in each layer by replacing the phaseϕn(m)→ϕn(m)−i​ln⁡γn(m)\phi_{n}^{(m)}\rightarrow\phi_{n}^{(m)}-i\ln\gamma_{n}^{(m)}, where the transmitances are randomly sampled from the intervalγn(m)∈(γmin,1)\gamma_{n}^{(m)}\in(\gamma_{\textnormal{min}},1).

In practical applications, optical networks inevitably experience losses, particularly during routing between components and around sharp bends. While typically minimal, these losses can accumulate and degrade overall performance. However, due to its overparameterization, the interlaced network demonstrates intrinsic resilience to such imperfections and moderate losses[14]. To model this, we adapt the coherence analyzer algorithm by incorporating a loss term into each phase elementϕn(m)→ϕn(m)−i​log⁡γn(m)\phi_{n}^{(m)}\rightarrow\phi_{n}^{(m)}-i\log\gamma_{n}^{(m)}, whereγn(m)∈(0,1)\gamma_{n}^{(m)}\in(0,1)denotes the transmission amplitude. To quantify the impact of these losses on the extraction of eigenvalues from the input coherence matrix, we optimize the network using parameters randomly sampled fromγn(m)∈(γmin,1)\gamma_{n}^{(m)}\in(\gamma_{\textnormal{min}},1). Varyingγmin\gamma_{\textnormal{min}}establishes a controlled upper bound on component-level loss. For eachγmin\gamma_{\textnormal{min}}, we sample 200 ensembles ofN2N^{2}random loss parameters. Although real-world losses are rarely this extreme or purely random, this stochastic approach provides a worst-case assessment. The minimum bound on the transmission in each configuration isγminM\gamma_{\textnormal{min}}^{M}, whereMMis the number of layers in the interlaced architecture. Despite the losses, the output power is normalized so that the rest of the algorithm remains unmodified. Figure2bsummarizes the numerical results forN=8N=8andN=20N=20, utilizing the input fields (partially coherent, fully incoherent, and fully coherent) previously established in Fig.1c. The data illustrate the average error distance (markers) and standard deviation (shaded area) between the reconstructed and original eigenvalues. As anticipated, the error distance increases inversely with transmittance, scaling higher as the maximum permissible loss grows.

Conclusions– In this letter, we have presented an architecture-agnostic approach for the analysis of partially coherent light using programmable photonics. By relying on the Schur-Horn theorem, our method successfully extracts the eigenvalues of the coherence matrix from output power measurements alone. A significant advantage of this approach is that the device can be programmed as an identity matrix, allowing the incoming field to pass through unaffected after characterization for subsequent use.

Beyond universal networks, we demonstrated that this black-box methodology is highly adaptable, functioning effectively even in under-parameterized architectures and in the presence of arbitrary optical losses. This versatility underscores the robustness of our approach, paving the way for space-efficient, error-resilient, and programmable spatial coherence analyzers.


Funding.This project is supported by the U.S. Air Force Office of Scientific Research (AFOSR) Award# FA9550-25-1-0200.


Disclosures.The authors declare no conflicts of interest.


Data availability.Data underlying the results presented in this paper can be obtained from the authors upon reasonable request.

## References
- [1]L. Mandel, E. Wolf, and J. H. Shapiro, “Optical coherence and quantum
optics,” (1996).
- [2]S. Lee, D. Kim, S.-W. Nam,et al.,\JournalTitleScientific
reports10, 18832 (2020).
- [3]M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani,\JournalTitlePhysical review letters73, 58 (1994).
- [4]H. de Guise, O. Di Matteo, and L. L. Sánchez-Soto,\JournalTitlePhysical Review A97, 022328 (2018).
- [5]D. A. Miller,\JournalTitlePhotonics Research1, 1 (2013).
- [6]D. Yi, Y. Wang, and H. K. Tsang,\JournalTitleAPL Photonics6(2021).
- [7]W. R. Clements, P. C. Humphreys, B. J. Metcalf,et al.,\JournalTitleOptica3, 1460 (2016).
- [8]F. Shokraneh, S. Geoffroy-Gagnon, and O. Liboiron-Ladouceur,\JournalTitleOptics Express28, 23495 (2020).
- [9]K. Rahbardar Mojaver, B. Zhao, E. Leung,et al.,\JournalTitleOptics Express31, 23851 (2023).
- [10]R. Tanomura, R. Tang, T. Umezaki,et al.,\JournalTitlePhysical Review Applied17, 024071 (2022).
- [11]K. Zelaya, M. Markowitz, and M.-A. Miri,\JournalTitleScientific
Reports14, 10950 (2024).
- [12]J. Friedmanet al.,\JournalTitleScientific Reports15, 35173 (2025).
- [13]V. L. Pastor, J. Lundeen, and F. Marquardt,\JournalTitleOptics
Express29, 38441 (2021).
- [14]M. Markowitz, K. Zelaya, and M.-A. Miri,\JournalTitleOptics
Express31, 37673 (2023).
- [15]M. Born and E. Wolf,Principles of optics: electromagnetic theory of
propagation, interference and diffraction of light(Elsevier, 2013).
- [16]P. H. Tomlins and R. K. Wang,\JournalTitleJournal of Physics D:
Applied Physics38, 2519 (2005).
- [17]M. Markowitz, K. Zelaya, and M.-A. Miri,\JournalTitleOpt. Express31, 37673 (2023).
- [18]R. Tanomura, R. Tang, S. Ghosh,et al.,\JournalTitleJournal
of Lightwave Technology38, 60 (2020).
- [19]C. Roques-Carmes, S. Fan, and D. A. Miller,\JournalTitleLight:
Science & Applications13, 260 (2024).
- [20]C. Guo and S. Fan,\JournalTitlePhysical Review B110,
035430 (2024).
- [21]C. Guo and S. Fan,\JournalTitlePhysical Review B110,
035431 (2024).
- [22]A. Hashemi, A. Shiri, B. E. Saleh,et al.,\JournalTitlearXiv
preprint arXiv:2601.18797 (2026).
- [23]A. Horn,\JournalTitleAmerican Journal of Mathematics76,
620 (1954).
- [24]K. Zelaya, M. Honari-Latifpour, K. K. Mandal,et al.,\JournalTitleOptica12, 1492 (2025).
- [25]K. Zelaya, M. Honari-Latifpour, and M.-A. Miri,\JournalTitlenpj
Nanophotonics2, 6 (2025).\bibliographyfullrefs

biblio

## 


- 


Major funding support from
