# Electromagnetic response of two interacting topological insulator spheres in external fields

**arXiv ID**: 2606.28982v1
**Authors**: J. Cornejo Gómez, M. Ibarra-Meneses, L. Medel Onofre, A. Martín-Ruiz
**Published**: 2026-06-27
**Categories**: cond-mat.other, math-ph
**Comments**: Accepted for publication in the Annalen der Physik
**HTML URL**: https://arxiv.org/html/2606.28982v1

## Abstract

We study the static electromagnetic response of two spherical topological insulators embedded in a dielectric medium and subjected to a uniform external electric field. The gapped surface states are described by a piecewise constant axion field, which induces a topological magnetoelectric coupling localized at the spherical interfaces. {More generally, the same formalism applies to isotropic magnetoelectric media characterized by an effective scalar magnetoelectric response.} The electrostatic problem is solved at zeroth order using bispherical coordinates, allowing for an exact treatment of both parallel and perpendicular orientations of the external field relative to the center-to-center axis. The resulting mode expansions are determined by three-term recurrence relations, which are solved perturbatively for nonoverlapping spheres. The { magnetoelectric}-induced response is then computed to leading order in the fine-structure constant {(or, more generally, in the effective coupling strength)}. The induced sources are purely interfacial and generate distinct magnetostatic field configurations in the parallel and perpendicular geometries. Closed-form series representations for the induced vector potential and magnetic field are obtained in terms of the zeroth-order electrostatic coefficients. These results provide an analytically controlled description of {interaction-induced magnetostatics in coupled spherical magnetoelectric systems}.

## Full Text

Electromagnetic response of two interacting topological insulator spheres in external fields

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2606.28982v1 [cond-mat.other] 27 Jun 2026

## Electromagnetic response of two interacting topological insulator spheres in external fieldsJ. Cornejo GómezInstituto de Ciencias Nucleares, Universidad Nacional Autónoma de México, 04510 Ciudad de México, MéxicoM. Ibarra-MenesesInstituto de Ciencias Nucleares, Universidad Nacional Autónoma de México, 04510 Ciudad de México, MéxicoL. Medel OnofreInstituto de Ciencias Nucleares, Universidad Nacional Autónoma de México, 04510 Ciudad de México, MéxicoA. Martín-Ruizalberto.martin@nucleares.unam.mxInstituto de Ciencias Nucleares, Universidad Nacional Autónoma de México, 04510 Ciudad de México, México

## Abstract

We study the static electromagnetic response of two spherical topological insulators embedded in a dielectric medium and subjected to a uniform external electric field. The gapped surface states are described by a piecewise constant axion field, which induces a topological magnetoelectric coupling localized at the spherical interfaces. More generally, the same formalism applies to isotropic magnetoelectric media characterized by an effective scalar magnetoelectric response. The electrostatic problem is solved at zeroth order using bispherical coordinates, allowing for an exact treatment of both parallel and perpendicular orientations of the external field relative to the center-to-center axis. The resulting mode expansions are determined by three-term recurrence relations, which are solved perturbatively for nonoverlapping spheres. The magnetoelectric-induced response is then computed to leading order in the fine-structure constant (or, more generally, in the effective coupling strength). The induced sources are purely interfacial and generate distinct magnetostatic field configurations in the parallel and perpendicular geometries. Closed-form series representations for the induced vector potential and magnetic field are obtained in terms of the zeroth-order electrostatic coefficients. These results provide an analytically controlled description of interaction-induced magnetostatics in coupled spherical magnetoelectric systems.

## IIntroduction

Topological phases of matter have reshaped our understanding of electronic systems by revealing that global, topological properties of Bloch wave functions can determine robust and quantized physical responses[41,12,35]. In three dimensions, topological insulators represent a paradigmatic example: they exhibit an insulating bulk gap coexisting with metallic surface states protected by time-reversal symmetry and characterized by an odd number of Dirac cones[7,26,36]. Beyond bulk crystals, increasing attention has been devoted to finite and mesoscopic realizations of topological insulators, including thin films[29], nanowires[8], and nanoparticles, where geometry, confinement, and boundary conditions qualitatively modify the electronic and electromagnetic response[4].

A defining macroscopic consequence of the nontrivial topology of three-dimensional topological insulators is the topological magnetoelectric effect. At low energies, this response is described by axion electrodynamics, in which Maxwell’s theory is supplemented by a term proportional toθ​𝐄⋅𝐁\theta\,\mathbf{E}\cdot\mathbf{B}[33,6]. For strong topological insulators, the axion angle is quantized asθ=±π\theta=\pm\pi, while trivial insulators correspond toθ=0\theta=0. When time-reversal symmetry is broken at the surface, for instance by magnetic coatings or exchange coupling, this term leads to quantized surface Hall conductivities and unconventional electromagnetic phenomena such as image magnetic monopoles[34,15,22]and repulsive Casimir effect[10,11,Martín-Ruiz_2016]. Importantly, whenθ\thetais piecewise constant, the axion contribution vanishes in the bulk and manifests itself exclusively through interfacial sources, making finite geometries essential for observable effects. While our discussion is framed in the language of topological insulators and axion electrodynamics, the mathematical structure developed here applies more generally to isotropic magnetoelectric media described by a scalar magnetoelectric coupling. In this broader context, the coupling need not be quantized nor of topological origin. Materials with sufficiently high crystallographic symmetry, including certain non-collinear antiferromagnets exhibiting approximately isotropic magnetoelectric response[39,19,37], may therefore provide a more experimentally realistic platform for observing related interaction-induced electromagnetic effects.

From the standpoint of classical electrodynamics, the response of dielectric bodies to external electromagnetic fields constitutes a paradigmatic boundary-value problem with a long and well-established history[14,27]. Among the simplest nontrivial geometries, the system of two interacting spheres occupies a central role in electrostatics[9,40,17]and electromagnetic scattering theory[18,2], as it captures multiple-scattering processes, near-field coupling, and collective polarization effects that are absent in isolated-particle descriptions. Such two-body configurations arise naturally in a wide variety of mesoscopic and composite systems. In nanoparticle assemblies and colloidal suspensions, electromagnetic interactions between nearby inclusions lead to collective optical and electrostatic responses that cannot be accounted for within single-particle approximations[32,21,3,5]. At the minimal level, plasmonic and dielectric dimers provide the simplest setting in which near-field coupling, mode hybridization, and symmetry-induced selection rules can be analyzed in a controlled and analytically transparent manner[32,31,18]. More generally, ordered or disordered arrays of closely spaced particles form the building blocks of artificial metamaterials, whose effective electromagnetic properties are governed primarily by multiple-scattering effects and inter-particle interactions rather than by the response of individual constituents[30,38,20]. For these reasons, the two-sphere problem provides a paradigmatic and analytically tractable framework for exploring interaction-induced modifications of electromagnetic response in structured and topologically nontrivial media. Closely related two-body geometries have also been extensively investigated. In particular, the sphere-plane configuration has attracted sustained attention in electrostatics since it provides a realistic model for particle-surface interactions and probe-sample coupling. From a geometric standpoint, this setup can be understood as a limiting case of the two-sphere system in which the radius of one sphere tends to infinity, so that many conceptual and methodological aspects are shared between both problems[13,16,1]. When formulated in bispherical coordinates, the two-sphere problem in the presence of a field admits an exact separation of variables and allows for analytically controlled solutions[27].

Motivated by these developments, in this work we study the static electromagnetic response of two interacting topological insulator spheres embedded in a dielectric medium and subjected to a uniform external electric field. We first solve the classical electrostatic problem exactly at zeroth order using bispherical coordinates, obtaining mode expansions governed by three-term recurrence relations. These relations are solved perturbatively for nonoverlapping spheres, providing an analytically transparent description of the interaction-induced corrections. Related two-body configurations involving topological media (such as a metallic sphere near a topological insulator surface) have been previously analyzed in the context of axion electrodynamics and induced magnetoelectric effects[24], highlighting the measurable consequences of interfacial topological couplings. Building on the exact two-sphere electrostatic solution, we then compute the leading axion-induced electromagnetic response to first order in the fine-structure constant. Because the axion field is piecewise constant, the induced sources are purely interfacial and generate distinct magnetostatic field configurations in the parallel and perpendicular geometries. Our results provide an analytically controlled framework for axion-induced magnetostatics in interacting finite systems and suggest experimentally accessible signatures of topological nontriviality in multi-sphere geometries.

The remainder of this article is organized as follows. In Sec.IIwe briefly review the axion electrodynamics framework appropriate for three-dimensional topological insulators, emphasizing the form of the modified Maxwell equations and the role of piecewise constant axion fields. In Sec.IVwe introduce the general formulation of the problem, including the geometrical setup, the use of bispherical coordinates, and the perturbative expansion scheme employed to solve the axion-modified field equations. SectionVis devoted to the electrostatic problem of two dielectric spheres subjected to a uniform external electric field, which serves as the seed solution for the subsequent magnetoelectric analysis. In this section, both parallel and perpendicular orientations of the applied field are treated, and the resulting mode expansions are determined through three-term recurrence relations that are solved perturbatively for nonoverlapping spheres. In Sec.VIwe compute the leading axion-induced magnetic response generated by the topological magnetoelectric effect, again for both parallel and perpendicular configurations, and obtain explicit series representations for the induced vector potential and magnetic field. Finally, in Sec.VIIwe summarize our main results and discuss possible extensions and implications of our work.

## IIAxion electrodynamics of topological insulators

The macroscopic electromagnetic response of 3D TIs, independently of microscopic details, is described by an effective field theory that extends Maxwell electrodynamics by a topological axion term. In SI units, the corresponding action reads[33,6]S=∫d4​x​[12​(ϵ​𝐄2−1μ​𝐁2)+απ​ϵ0μ0​θ​𝐄⋅𝐁],\displaystyle S=\int d^{4}x\,\left[\frac{1}{2}\left(\epsilon\mathbf{E}^{2}-\frac{1}{\mu}\mathbf{B}^{2}\right)+\frac{\alpha}{\pi}\sqrt{\frac{\epsilon_{0}}{\mu_{0}}}\,\theta\,\mathbf{E}\cdot\mathbf{B}\right],(1)

whereα=e2/(4​π​ϵ0​ℏ​c)\alpha=e^{2}/(4\pi\epsilon_{0}\hbar c)is the fine-structure constant,ϵ\epsilonandμ\mudenote the permittivity and permeability of the material, respectively, andθ\thetais the topological magnetoelectric polarizability (axion field).

Time-reversal symmetry constrainsθ\thetato the valuesθ=0\theta=0orπ\pi(mod2​π2\pi). As a result, the axion term does not modify Maxwell’s equations in the bulk of a homogeneous TI. Its physical consequences arise only at interfaces whereθ\thetachanges discontinuously, such as between a TI and a conventional insulator. When the surface states are gapped by a TR-breaking perturbation (induced, for instance, by magnetic doping or by the application of an external static magnetic field) the system becomes a full insulator characterized by a quantized valueθ=±π\theta=\pm\pi.

Varying the action (1) yields Maxwell’s equations in matter supplemented by modified constitutive relations,𝐃\displaystyle\mathbf{D}=ϵ​𝐄+α​θπ​ϵ0μ0​𝐁,𝐇=1μ​𝐁−α​θπ​ϵ0μ0​𝐄,\displaystyle=\epsilon\mathbf{E}+\alpha\frac{\theta}{\pi}\sqrt{\frac{\epsilon_{0}}{\mu_{0}}}\,\mathbf{B},\qquad\mathbf{H}=\frac{1}{\mu}\mathbf{B}-\alpha\frac{\theta}{\pi}\sqrt{\frac{\epsilon_{0}}{\mu_{0}}}\,\mathbf{E},(2)

which encode the topological magnetoelectric effect: an electric field induces a magnetic polarization, while a magnetic field induces an electric polarization[33,6].

In the static regime relevant for this work, Maxwell’s equations reduce to∇⋅[ϵ​(𝐫)​𝐄​(𝐫)]\displaystyle\nabla\cdot\left[\epsilon(\mathbf{r})\mathbf{E}(\mathbf{r})\right]=ρ​(𝐫)−απ​ϵ0μ0​∇θ​(𝐫)⋅𝐁​(𝐫),\displaystyle=\rho(\mathbf{r})-\frac{\alpha}{\pi}\sqrt{\frac{\epsilon_{0}}{\mu_{0}}}\,\nabla\theta(\mathbf{r})\cdot\mathbf{B}(\mathbf{r}),(3)∇×[μ−1​(𝐫)​𝐁​(𝐫)]\displaystyle\nabla\times\left[\mu^{-1}(\mathbf{r})\mathbf{B}(\mathbf{r})\right]=απ​ϵ0μ0​∇θ​(𝐫)×𝐄​(𝐫),\displaystyle=\frac{\alpha}{\pi}\sqrt{\frac{\epsilon_{0}}{\mu_{0}}}\,\nabla\theta(\mathbf{r})\times\mathbf{E}(\mathbf{r}),(4)

supplemented by the homogeneous equations∇⋅𝐁=0,∇×𝐄=𝟎.\displaystyle\nabla\cdot\mathbf{B}=0,\qquad\nabla\times\mathbf{E}=\mathbf{0}.(5)

Sinceθ\thetais piecewise constant, its gradient vanishes everywhere except at material interfaces. For a TI region in contact with a conventional insulator across an interfaceΣ\Sigma, one has∇θ​(𝐫)=(θ2−θ1)​δ​(Σ)​𝐧^,\displaystyle\nabla\theta(\mathbf{r})=(\theta_{2}-\theta_{1})\,\delta(\Sigma)\,\hat{\mathbf{n}},(6)

where𝐧^\hat{\mathbf{n}}is the outward unit normal toΣ\Sigma. As a result, the axion term affects the electromagnetic response only through modified interfacial conditions, while the bulk fields obey the conventional electrostatic and magnetostatic equations. Static problems involving topological insulators can therefore be formulated as boundary-value problems closely analogous to classical dielectric systems, but augmented by topological magnetoelectric couplings localized at the material interfaces[22,23].

## IIIExact solution for an isolated topological-insulator sphere

Before addressing the interacting two-sphere geometry, it is instructive to consider the simpler case of a single isolated topological-insulator sphere in a uniform external electric field. Besides its exact solvability, this configuration provides a natural benchmark for the more general interacting problem studied below, allowing us to identify the basic magnetoelectric response induced by the axion coupling in the absence of inter-sphere interactions.

We consider a spherical topological insulator of radiusRR, characterized by constitutive parameters(ϵ1,μ1,θ)(\epsilon_{1},\mu_{1},\theta), embedded in a topologically trivial dielectric medium(ϵ2,μ2)(\epsilon_{2},\mu_{2})withθ=0\theta=0, and subjected to a static uniform electric field𝐄0=E0​𝐳^\mathbf{E}_{0}=E_{0}\hat{\mathbf{z}}. Inside the sphere, the constitutive relations take the axion-electrodynamics form𝐃1=ϵ1​𝐄1+γ​𝐁1,𝐇1=1μ1​𝐁1−γ​𝐄1,\displaystyle\mathbf{D}_{1}=\epsilon_{1}\mathbf{E}_{1}+\gamma\mathbf{B}_{1},\qquad\mathbf{H}_{1}=\frac{1}{\mu_{1}}\mathbf{B}_{1}-\gamma\mathbf{E}_{1},(7)

whereγ≡α​(θ/π)​ϵ0μ0\gamma\equiv\alpha(\theta/\pi)\sqrt{\frac{\epsilon_{0}}{\mu_{0}}}, while outside the sphere one has the conventional relations𝐃2=ϵ2​𝐄2\mathbf{D}_{2}=\epsilon_{2}\mathbf{E}_{2}and𝐇2=𝐁2/μ2\mathbf{H}_{2}=\mathbf{B}_{2}/\mu_{2}.
In the static regime, both the electric and magnetic fields may be expressed in terms of scalar potentials satisfying Laplace’s equation in each region. Owing to axial symmetry, only the dipolar (l=1l=1) sector contributes, so that the potentials take the formΦ1=−Arcosϑ,Φ2=−E0rcosϑ+P​cos⁡ϑr2,Ψ1=−Crcosϑ,,Ψ2=M​cos⁡ϑr2.\displaystyle\Phi_{1}=-Ar\cos\vartheta,\qquad\Phi_{2}=-E_{0}r\cos\vartheta+\frac{P\cos\vartheta}{r^{2}},\qquad\Psi_{1}=-Cr\cos\vartheta,,\qquad\Psi_{2}=\frac{M\cos\vartheta}{r^{2}}.(8)

Imposing the standard Maxwell boundary conditions at the spherical interface, including the axion-modified constitutive response inside the sphere, the coefficients can be determined exactly. The resulting interior fields are found to be uniform,𝐄1=3​ϵ2ϵ1+2​ϵ2+μ~​γ2​𝐄0,𝐇1=−γ​μ~2​μ2​3​ϵ2ϵ1+2​ϵ2+μ~​γ2​𝐄0,\displaystyle\mathbf{E}_{1}=\frac{3\epsilon_{2}}{\epsilon_{1}+2\epsilon_{2}+\tilde{\mu}\gamma^{2}}\,\mathbf{E}_{0},\qquad\qquad\mathbf{H}_{1}=-\frac{\gamma\tilde{\mu}}{2\mu_{2}}\frac{3\epsilon_{2}}{\epsilon_{1}+2\epsilon_{2}+\tilde{\mu}\gamma^{2}}\,\mathbf{E}_{0},(9)

whereμ~=2​μ1​μ2/(μ1+2​μ2)\tilde{\mu}=2\mu_{1}\mu_{2}/(\mu_{1}+2\mu_{2}). Thus, the axion coupling induces a uniform magnetic response inside the topological sphere even in the absence of externally applied magnetic fields.

Outside the sphere, the electromagnetic response acquires the standard dipolar form. The electric field𝐄2\mathbf{E}_{2}consists of the superposition of the externally applied uniform field𝐄0\mathbf{E}_{0}and the field generated by an induced electric dipole moment𝐩\mathbf{p}. Similarly, the axion-induced magnetic response outside the sphere𝐇2\mathbf{H}_{2}corresponds to the field of an induced magnetic dipole𝐦\mathbf{m}. These dipolar moments are found to be𝐏=4​π​ϵ2​R3​ϵ1−ϵ2+μ~​γ2ϵ1+2​ϵ2+μ~​γ2​𝐄0,𝐌=γ​μ~2​μ2​3​ϵ2ϵ1+2​ϵ2+μ~​γ2​4​π​R3​𝐄0.\displaystyle\mathbf{P}=4\pi\epsilon_{2}R^{3}\,\frac{\epsilon_{1}-\epsilon_{2}+\tilde{\mu}\gamma^{2}}{\epsilon_{1}+2\epsilon_{2}+\tilde{\mu}\gamma^{2}}\,\mathbf{E}_{0},\qquad\qquad\mathbf{M}=\frac{\gamma\tilde{\mu}}{2\mu_{2}}\frac{3\epsilon_{2}}{\epsilon_{1}+2\epsilon_{2}+\tilde{\mu}\gamma^{2}}4\pi R^{3}\,\mathbf{E}_{0}.(10)

Therefore, the exact solution exhibits the characteristic topological magnetoelectric effect in its simplest form: an externally applied electric field generates an induced magnetic dipolar response mediated entirely by the axion coupling at the spherical interface. This isolated-sphere solution provides the natural reference configuration against which the genuinely interaction-induced modifications of the two-sphere geometry can be assessed.

## IVProblem statement

We consider the static electromagnetic response of two spherical topological insulators immersed in a homogeneous dielectric medium and subjected to an externally applied uniform electromagnetic field, as illustrated in Fig.1. Each sphere has radiusRiR_{i}(i=1,2)(i=1,2)and is characterized by a dielectric constantϵi\epsilon_{i}, magnetic permeabilityμi\mu_{i}, and a topological magnetoelectric polarizabilityθi\theta_{i}. The surrounding medium is a conventional insulator with dielectric constantϵm\epsilon_{m}and permeabilityμm\mu_{m}.

Since trivial insulators and known 3D TIs are typically nonmagnetic, we assumeμ1=μ2=μm=μ0\mu_{1}=\mu_{2}=\mu_{m}=\mu_{0}.
The spheres are identical and have the same radiusRR, and are separated by a center-to-center distancedd.
The system contains no free charges or currents, so that the electromagnetic response is entirely induced by the external fields and the material interfaces.Figure 1:Schematic configuration of the system. Two spherical TIs of radiusRR, characterized by constitutive parameters(ϵ1,μ1,θ1)(\epsilon_{1},\mu_{1},\theta_{1})and(ϵ2,μ2,θ2)(\epsilon_{2},\mu_{2},\theta_{2}), are embedded in a homogeneous external medium with parameters(ϵm,μm)(\epsilon_{m},\mu_{m})and separated by a center-to-center distancedd. The figure illustrates the two relevant orientations of the externally applied uniform fields, either electric (𝐄0\mathbf{E}_{0}) or magnetic (𝐁0\mathbf{B}_{0}): parallel to the inter-sphere axis (upper panel) and perpendicular to it (lower panel). These two geometries define the distinct configurations analyzed throughout this work.

In the specific case of three-dimensional topological insulators, a nontrivial magnetoelectric response arises when the surface states of each sphere are gapped by a time-reversal-symmetry-breaking perturbation, leading to quantized valuesθi=±π\theta_{i}=\pm\piinside the topological regions andθ=0\theta=0in the surrounding dielectric. As a result, the axion contribution is confined to the spherical interfaces, while the electromagnetic fields in the bulk obey the conventional electrostatic and magnetostatic equations. More generally, however, the present formalism is not restricted to quantized topological insulators, but applies to any isotropic magnetoelectric medium whose constitutive response can be described by an effective scalar magnetoelectric coupling. We focus on the static response of the system to an externally applied uniform electric field, which can therefore be formulated as a boundary-value problem for Maxwell’s equations with magnetoelectric interfacial couplings.

## IV.1Geometry of the problem

The presence of two interacting spherical bodies naturally suggests the use of a coordinate system adapted to spherical boundaries. We therefore employ the bispherical coordinate system, which is particularly well suited for boundary-value problems involving two spheres and has been extensively used in classical electrostatics and magnetostatics[25,28]. In this representation, the surfaces of both spheres are described by constant coordinate values, which simplifies the formulation of the problem.

The relation between the Cartesian(x,y,z)(x,y,z)and the bispherical(η,ξ,ϕ)(\eta,\xi,\phi)coordinate systems is given byx=a​sin⁡(ξ)​cos⁡(ϕ)cosh⁡(η)−cos⁡(ξ),y=a​sin⁡(ξ)​sin⁡(ϕ)cosh⁡(η)−cos⁡(ξ),z=a​sinh⁡ηcosh⁡(η)−cos⁡(ξ),\displaystyle x=\frac{a\sin{\xi}\cos{\phi}}{\cosh{\eta}-\cos{\xi}},\qquad y=\frac{a\sin{\xi}\sin{\phi}}{\cosh{\eta}-\cos{\xi}},\qquad z=\frac{a\sinh{\eta}}{\cosh{\eta}-\cos{\xi}},(11)

whereϕ\phiis the azimuthal angle around thezzaxis anda>0a>0sets the length scale of the coordinate system. The coordinate ranges are−∞≤η≤+∞,0≤ξ≤π,0≤ϕ≤2​π.\displaystyle-\infty\leq\eta\leq+\infty,\qquad 0\leq\xi\leq\pi,\qquad 0\leq\phi\leq 2\pi.(12)

In this coordinate system, surfaces of constantη\etarepresent nonintersecting spheres with centers on thezzaxis. A surfaceη=η0\eta=\eta_{0}corresponds to a sphere of radiusR=a|sinh⁡η0|,\displaystyle R=\frac{a}{|\sinh{\eta_{0}}|},(13)

whose center is located atzc=a​coth⁡(η0).\displaystyle z_{c}=a\,\coth{\eta_{0}}.(14)

Positive (negative) values ofη0\eta_{0}correspond to spheres centered on the positive (negative)zzaxis. The limiting surfaceη=0\eta=0represents a sphere of infinite radius and therefore corresponds to the planez=0z=0. Surfaces of constantξ\xiform tori intersecting thezzaxis, while surfaces of constantϕ\phiare half-planes bounded by that axis.

We consider two physical spherical topological insulators whose surfaces are described byη=η1>0\eta=\eta_{1}>0andη=η2<0\eta=\eta_{2}<0, respectively, as shown in Fig. 1. Their radii areR1=asinh⁡η1,R2=a|sinh⁡η2|,\displaystyle R_{1}=\frac{a}{\sinh{\eta_{1}}},\qquad R_{2}=\frac{a}{|\sinh{\eta_{2}}|},(15)

and the distance between their centers isd=a​(coth⁡(η1)−coth⁡(η2)),\displaystyle d=a\left(\coth{\eta_{1}}-\coth{\eta_{2}}\right),(16)

with the conditiond>R1+R2d>R_{1}+R_{2}ensuring that the spheres do not overlap.

The space is divided into three regions: the interior of sphere 1 (η>η1\eta>\eta_{1}), the interior of sphere 2 (η<η2\eta<\eta_{2}), and the exterior region (η2<η<η1\eta_{2}<\eta<\eta_{1}), which is occupied by the surrounding dielectric medium. Each region is characterized by its own electromagnetic parameters(ϵ,μ,θ)(\epsilon,\mu,\theta), with the axion fieldθ\thetachanging discontinuously across the spherical interfaces. This geometric formulation provides a convenient framework for solving the static electromagnetic boundary-value problem of two interacting topological insulator spheres in external fields.

## IV.2Electrodynamics of the problem

In the static regime considered here and in the absence of free charges and currents, the electromagnetic response of the system is governed by Maxwell’s equations supplemented by the axion-induced magnetoelectric coupling introduced in Sec.II. Since the axion fieldθ\thetais piecewise constant in the present configuration, its gradient is nonvanishing only at the spherical interfaces separating regions with different values ofθ\theta. LetΣi\Sigma_{i}(i=1,2)(i=1,2)denote the interfaces between each topological insulator sphere and the surrounding dielectric medium. Across each interface, the discontinuity of the axion field gives rise to modified electromagnetic boundary conditions. In the absence of free surface charges and currents, these conditions can be written as[𝐧^⋅(ϵ​𝐄)]Σ\displaystyle\big[\hat{\mathbf{n}}\cdot(\epsilon\mathbf{E})\big]_{\Sigma}=α~​𝐧^⋅𝐁|Σ,[𝐧^×𝐄]Σ=𝟎,\displaystyle=\tilde{\alpha}\,\hat{\mathbf{n}}\cdot\mathbf{B}\big|_{\Sigma},\qquad\big[\hat{\mathbf{n}}\times\mathbf{E}\big]_{\Sigma}=\mathbf{0},(17)[𝐧^⋅𝐁]Σ\displaystyle\big[\hat{\mathbf{n}}\cdot\mathbf{B}\big]_{\Sigma}=0,[𝐧^×(𝐁/μ)]Σ=−α~​𝐧^×𝐄|Σ,\displaystyle=0,\qquad\big[\hat{\mathbf{n}}\times(\mathbf{B}/\mu)\big]_{\Sigma}=-\tilde{\alpha}\,\hat{\mathbf{n}}\times\mathbf{E}\big|_{\Sigma},(18)

whereα~=α​(θ/π)\tilde{\alpha}=\alpha(\theta/\pi),𝐧^\hat{\mathbf{n}}is the outward unit normal to the interface, and[𝐅]Σ=𝐅​(Σ+)−𝐅​(Σ−)\big[\mathbf{F}\big]_{\Sigma}=\mathbf{F}(\Sigma^{+})-\mathbf{F}(\Sigma^{-})denotes the discontinuity of any vector field acrossΣ\Sigma. These relations provide a compact characterization of the full electromagnetic response at the interfaces.

To construct the solution, however, we adopt a perturbative approach in the axion coupling. Since the dimensionless parameterα=e2/(4​π​ϵ0​ℏ​c)\alpha=e^{2}/(4\pi\epsilon_{0}\hbar c)is small, the axion-induced effects can be treated as perturbative corrections to the conventional electrostatic and magnetostatic solutions. In this formulation, the effect of the axion term is incorporated through interfacial source terms proportional to∇θ\nabla\theta, and the modified boundary conditions need not be imposed explicitly order by order.

Accordingly, we expand the electric and magnetic fields in powers ofα\alphaas𝐄\displaystyle\mathbf{E}=𝐄(0)+𝐄(1)+𝐄(2)+⋯,\displaystyle=\mathbf{E}^{(0)}+\mathbf{E}^{(1)}+\mathbf{E}^{(2)}+\cdots,(19)𝐁\displaystyle\mathbf{B}=𝐁(0)+𝐁(1)+𝐁(2)+⋯,\displaystyle=\mathbf{B}^{(0)}+\mathbf{B}^{(1)}+\mathbf{B}^{(2)}+\cdots,(20)

where𝐄(n)\mathbf{E}^{(n)}and𝐁(n)\mathbf{B}^{(n)}denote contributions of orderαn\alpha^{n}. The zeroth-order fields correspond to the classical solution for two dielectric spheres in a static external electric field and satisfy the conventional Maxwell equations together with the standard electromagnetic boundary conditions at the spherical interfaces.

At first order inα\alpha, Gauss and Ampère’s laws yield∇⋅(ϵ​𝐄(1))=−απ​∇θ⋅𝐁(0),∇×𝐁(1)=απ​∇θ×𝐄(0),\displaystyle\nabla\cdot(\epsilon\mathbf{E}^{(1)})=-\frac{\alpha}{\pi}\,\nabla\theta\cdot\mathbf{B}^{(0)},\qquad\nabla\times\mathbf{B}^{(1)}=\frac{\alpha}{\pi}\,\nabla\theta\times\mathbf{E}^{(0)},(21)

while the remaining Maxwell equations retain their homogeneous form.

Introducing the first-order elecromagnetic potentialsϕ(1)\phi^{(1)}and𝐀(1)\mathbf{A}^{(1)}as usual, and working in the Coulomb gauge∇⋅𝐀(1)=0\nabla\cdot\mathbf{A}^{(1)}=0, Eq. (21) reduces to∇⋅(ϵ​∇ϕ(1))=απ​∇θ⋅𝐁(0),∇2𝐀(1)=−απ​∇θ×𝐄(0).\displaystyle\nabla\cdot(\epsilon\nabla\phi^{(1)})=\frac{\alpha}{\pi}\,\nabla\theta\cdot\mathbf{B}^{(0)},\quad\nabla^{2}\mathbf{A}^{(1)}=-\frac{\alpha}{\pi}\,\nabla\theta\times\mathbf{E}^{(0)}.(22)

The solution of Eq. (22) can be expressed in terms of the Green’s function asϕ(1)​(𝐫)=−απ​∫Gϵ​(𝐫,𝐫′)​∇′θ​(𝐫′)⋅𝐁(0)​(𝐫′)​d3​𝐫′,\displaystyle\phi^{(1)}(\mathbf{r})=-\frac{\alpha}{\pi}\int G_{\epsilon}(\mathbf{r},\mathbf{r}^{\prime})\,\nabla^{\prime}\theta(\mathbf{r}^{\prime})\cdot\mathbf{B}^{(0)}(\mathbf{r}^{\prime})\,\mathrm{d}^{3}\mathbf{r}^{\prime},(23)𝐀(1)​(𝐫)=απ​∫G0​(𝐫,𝐫′)​∇′θ​(𝐫′)×𝐄(0)​(𝐫′)​d3​𝐫′,\displaystyle\mathbf{A}^{(1)}(\mathbf{r})=\frac{\alpha}{\pi}\int G_{0}(\mathbf{r},\mathbf{r}^{\prime})\,\nabla^{\prime}\theta(\mathbf{r}^{\prime})\times\mathbf{E}^{(0)}(\mathbf{r}^{\prime})\,\mathrm{d}^{3}\mathbf{r}^{\prime},(24)

whereGϵ​(𝐫,𝐫′)G_{\epsilon}(\mathbf{r},\mathbf{r}^{\prime})andG0​(𝐫,𝐫′)G_{0}(\mathbf{r},\mathbf{r}^{\prime})are the Green’s functions associated with the operators−∇⋅(ϵ∇⋅)-\nabla\cdot(\epsilon\nabla\;\cdot)and−∇2⋅-\nabla^{2}\;\cdot, respectively.

In the present geometry the axion field is piecewise constant:θ=θ1\theta=\theta_{1}inside sphere 1,θ=θ2\theta=\theta_{2}inside sphere 2, andθ=θm=0\theta=\theta_{m}=0in the surrounding dielectric. Therefore,∇θ\nabla\thetavanishes everywhere in the bulk and is supported only at the spherical interfacesΣ1\Sigma_{1}andΣ2\Sigma_{2}, whereθ\thetais discontinuous. In distributional form one may write∇θ​(𝐫)=Δ​θ1​δ​(Σ1)​𝐧^1+Δ​θ2​δ​(Σ2)​𝐧^2,Δ​θi≡θm−θi,\displaystyle\nabla\theta(\mathbf{r})=\Delta\theta_{1}\,\delta(\Sigma_{1})\,\hat{\mathbf{n}}_{1}+\Delta\theta_{2}\,\delta(\Sigma_{2})\,\hat{\mathbf{n}}_{2},\quad\Delta\theta_{i}\equiv\theta_{m}-\theta_{i},(25)

where𝐧^i\hat{\mathbf{n}}_{i}is the outward unit normal toΣi\Sigma_{i}(pointing from the interior of sphereiitoward the exterior dielectric region).

In bispherical coordinates, the surfaces of the spheres are given byη=η1>0\eta=\eta_{1}>0andη=η2<0\eta=\eta_{2}<0. Using∇f=𝜼^​(1/hη)​∂ηf+⋯\nabla f=\hat{\bm{\eta}}\,(1/h_{\eta})\,\partial_{\eta}f+\cdotswith the metric factorhη=acosh⁡η−cos⁡ξ,\displaystyle h_{\eta}=\frac{a}{\cosh\eta-\cos\xi},(26)

the interfacial delta distributions becomeδ​(Σi)​𝐧^i=cosh⁡η−cos⁡ξa​𝜼^​δ​(η−ηi),(i=1,2),\displaystyle\delta(\Sigma_{i})\,\hat{\mathbf{n}}_{i}=\frac{\cosh\eta-\cos\xi}{a}\,\hat{\bm{\eta}}\,\delta(\eta-\eta_{i}),\qquad(i=1,2),(27)

so that Eq. (25) yields∇θ=cosh⁡η−cos⁡ξa​𝜼^​[Δ​θ1​δ​(η−η1)+Δ​θ2​δ​(η−η2)].\displaystyle\nabla\theta=\frac{\cosh\eta-\cos\xi}{a}\,\hat{\bm{\eta}}\,\Big[\Delta\theta_{1}\,\delta(\eta-\eta_{1})+\Delta\theta_{2}\,\delta(\eta-\eta_{2})\Big].(28)

Equation (28) makes explicit that the axion-induced sources are localized on each spherical interface, with strengths fixed by the corresponding jumpsΔ​θi\Delta\theta_{i}. Consequently, volume integrals involving∇θ\nabla\theta(such as in Eq. (24)) reduce to surface contributions onΣ1\Sigma_{1}andΣ2\Sigma_{2}.

## VZeroth-order solution: classical two-sphere problem

We begin by constructing the electromagnetic fields at zeroth order in the axion coupling,θ=0\theta=0. In this limit, the topological magnetoelectric response is absent and the problem reduces to the classical electrostatic response of two dielectric spheres embedded in a homogeneous dielectric medium and subjected to an externally applied uniform electric field. The zeroth-order fields provide the baseline solution upon which the axion-induced corrections are built in the subsequent sections.

Since the configuration is static and free of charges and currents, the electric field can be expressed in terms of a scalar potentialϕ(0)\phi^{(0)}satisfying Laplace’s equation in each region,∇2ϕ(0)=0,\displaystyle\nabla^{2}\phi^{(0)}=0,(29)

together with the standard electromagnetic boundary conditions at the spherical interfaces. The symmetry of the problem depends on the orientation of the external field relative to the line joining the centers of the spheres. Accordingly, we consider separately the two canonical configurations: (i) an external electric field parallel to the center-to-center axis, and (ii) an external electric field perpendicular to that axis.

The general solution of Laplace’s equation in bispherical coordinates can be written as a superposition of separable modes adapted to the spherical geometry. A convenient basis of solutions is given byfn​m±,±′​(η,ξ,ϕ)=cosh⁡η−cos⁡ξ​e±(n+12)​η​Pnm​(cos⁡ξ)​e±′i​m​ϕ,\displaystyle f^{\pm,\pm^{\prime}}_{nm}(\eta,\xi,\phi)=\sqrt{\cosh\eta-\cos\xi}\;e^{\pm\left(n+\frac{1}{2}\right)\eta}\,P_{n}^{m}(\cos\xi)\,e^{\pm^{\prime}im\phi},(30)

wherePnmP_{n}^{m}are the associated Legendre polynomials of the first kind, withn∈ℤ+n\in\mathbb{Z}^{+}and−n≤m≤n-n\leq m\leq n. The prefactorcosh⁡η−cos⁡ξ\sqrt{\cosh\eta-\cos\xi}is the conformal factor associated with the bispherical coordinate system.

A second linearly independent set of solutions involving the associated Legendre functions of the second kind,Qnm​(cos⁡ξ)Q_{n}^{m}(\cos\xi), also exists. However, these functions exhibit logarithmic singularities atcos⁡ξ=±1\cos\xi=\pm 1and are therefore excluded in the present analysis. Equation (30) thus provides the most general regular solution compatible with the geometry of two nonintersecting spheres.

The expansion coefficients are fixed by imposing the boundary conditions at the spherical interfaces and by matching the far-field behavior to the externally applied uniform electric field. Further simplifications follow from the symmetry of each configuration and are discussed separately below.

## V.1Parallel external electric field

We first consider the case in which the externally applied electric field is parallel to the line joining the centers of the spheres,𝐄0=E0​𝐳^\mathbf{E}_{0}=E_{0}\hat{\mathbf{z}}. The corresponding external potential isϕ0=−E0​z\phi_{0}=-E_{0}z, which is odd under reflections with respect to thex​yxyplane. As a consequence, the electrostatic problem exhibits axial symmetry and all physical quantities are independent of the azimuthal angleϕ\phi.

The odd parity of the external potential further implies that the induced potentials inside and outside the spheres satisfyϕe​(−η,ξ)=−ϕe​(η,ξ),ϕ+​(−η,ξ)=−ϕ−​(η,ξ),\displaystyle\phi_{e}(-\eta,\xi)=-\phi_{e}(\eta,\xi),\qquad\phi_{+}(-\eta,\xi)=-\phi_{-}(\eta,\xi),(31)

so that it is sufficient to determine a single interior potential, which we choose asϕ+​(η,ξ)\phi_{+}(\eta,\xi).

At the surface of each sphere, the electrostatic boundary conditions require the continuity of the potential and of the normal component of the electric displacement field,ϕ+​(η0,ξ)\displaystyle\phi_{+}(\eta_{0},\xi)=ϕe​(η0,ξ),\displaystyle=\phi_{e}(\eta_{0},\xi),(32)ϵi​∂ηϕ+​(η0,ξ)\displaystyle\epsilon_{i}\,\partial_{\eta}\phi_{+}(\eta_{0},\xi)=ϵe​∂ηϕe​(η0,ξ),\displaystyle=\epsilon_{e}\,\partial_{\eta}\phi_{e}(\eta_{0},\xi),(33)

whereη=η0\eta=\eta_{0}defines the spherical interfaces.

Guided by the general solution of Laplace’s equation in bispherical coordinates, we expand the exterior and interior potentials asϕe​(η,ξ)\displaystyle\phi_{e}(\eta,\xi)=(cosh⁡η−cos⁡ξ)1/2​∑n=0∞[An​sinh⁡(n¯​η)−23/2​E0​a​n¯​e−n¯​η]​Pn​(cos⁡ξ),\displaystyle=(\cosh\eta-\cos\xi)^{1/2}\sum_{n=0}^{\infty}\left[A_{n}\sinh(\bar{n}\eta)-2^{3/2}E_{0}a\,\bar{n}e^{-\bar{n}\eta}\right]P_{n}(\cos\xi),(34)ϕ+​(η,ξ)\displaystyle\phi_{+}(\eta,\xi)=(cosh⁡η−cos⁡ξ)1/2​∑n=0∞Bn​e−n¯​η​Pn​(cos⁡ξ),\displaystyle=(\cosh\eta-\cos\xi)^{1/2}\sum_{n=0}^{\infty}B_{n}e^{-\bar{n}\eta}P_{n}(\cos\xi),(35)

wheren¯=n+1/2\bar{n}=n+1/2and the second term in Eq. (34) ensures the correct asymptotic behavior imposed by the external field.

Imposing continuity of the potential atη=η0\eta=\eta_{0}allows the coefficientsBnB_{n}to be expressed algebraically in terms ofAnA_{n}. The continuity of the normal component of the electric field then leads to a system of coupled three-term recurrence relations for the coefficientsAnA_{n}, which can be written compactly as𝒞n−1​An−1+𝒞n​An+𝒞n+1​An+1=𝒮n,\displaystyle\mathcal{C}_{n-1}A_{n-1}+\mathcal{C}_{n}A_{n}+\mathcal{C}_{n+1}A_{n+1}=\mathcal{S}_{n},(36)

where the coefficients𝒞n\mathcal{C}_{n}and the source term𝒮n\mathcal{S}_{n}depend on the geometric parameterη0\eta_{0}and on the dielectric contrastΔ=ϵi−ϵeϵi+ϵe.\displaystyle\Delta=\frac{\epsilon_{i}-\epsilon_{e}}{\epsilon_{i}+\epsilon_{e}}.(37)

The explicit form of Eq. (36) is derived in AppendixA.

Since|Δ|<1|\Delta|<1for physical dielectrics ande−η0<1e^{-\eta_{0}}<1for nonoverlapping spheres, the recurrence relation can be solved perturbatively in the small parameterΔ​e−2​n​η0\Delta e^{-2n\eta_{0}}. WritingAn=An(0)+An(1)+An(2)+⋯,\displaystyle A_{n}=A_{n}^{(0)}+A_{n}^{(1)}+A_{n}^{(2)}+\cdots,(38)

one obtains a hierarchy of linear equations at successive orders.

At leading order, the solution isAn(0)=2​e−η03−Δ​[n−e−2​η01−e−2​η0],\displaystyle A_{n}^{(0)}=\frac{2e^{-\eta_{0}}}{3-\Delta}\left[n-\frac{e^{-2\eta_{0}}}{1-e^{-2\eta_{0}}}\right],(39)

which corresponds to the classical electrostatic response of two dielectric spheres in a uniform external field.

The first-order correction describes the leading effect of multiple electrostatic scattering between the spheres and readsAn(1)=2​Δ​e−2​n​η03−Δ​e−2​η0​[n−1+Δ2​e−2​η0+1−Δ4​e−4​η0+𝒪​(e−6​η0)].\displaystyle A_{n}^{(1)}=\frac{2\Delta e^{-2n\eta_{0}}}{3-\Delta}e^{-2\eta_{0}}\left[n-\frac{1+\Delta}{2}e^{-2\eta_{0}}+\frac{1-\Delta}{4}e^{-4\eta_{0}}+\mathcal{O}(e^{-6\eta_{0}})\right].(40)

At second order, one findsAn(2)=Δ​e−2​n​η0​[2​e−3​η03−Δ​n−1+Δ3−Δ​e−5​η0+𝒪​(e−7​η0)],\displaystyle A_{n}^{(2)}=\Delta e^{-2n\eta_{0}}\left[\frac{2e^{-3\eta_{0}}}{3-\Delta}n-\frac{1+\Delta}{3-\Delta}e^{-5\eta_{0}}+\mathcal{O}(e^{-7\eta_{0}})\right],(41)

which accounts for higher-order multiple reflections of the induced field between the two spherical interfaces.

Together, Eqs. (39)-(41) provide an accurate representation of the electrostatic potential in the regime of moderately separated spheres. These results form the basis for the calculation of the axion-induced electromagnetic response discussed in the subsequent sections.Figure 2:Zeroth-order electrostatic configuration for two identical dielectric spheres embedded in a homogeneous dielectric medium and subjected to a uniform external electric field parallel to the center-to-center axis. The spheres are separated along the verticalzz-axis, while the horizontal axis corresponds to thexx-direction. Owing to the axial symmetry of the geometry, the system is invariant under azimuthal rotations around thezz-axis. The left panel shows the equipotential lines, whereas the right panel displays the corresponding electric field lines. Far from the spheres, the field approaches the uniform external field, while near the spherical interfaces the mutual electrostatic interaction distorts both the equipotentials and the field lines, with a pronounced enhancement in the inter-sphere region.

In Fig.2we illustrate the zeroth-order electrostatic solution for two identical dielectric spheres separated along the center-to-center axis and subjected to a uniform external electric field oriented parallel to this axis. The left panel displays the equipotential lines, while the right panel shows the corresponding electric field lines. The distortion of both the potential contours and the field trajectories clearly reflects the mutual polarization of the spheres induced by the external field. In particular, the equipotential lines are noticeably compressed in the inter-sphere region, indicating an enhanced local electric field resulting from the electrostatic interaction between the induced multipolar moments. The electric field lines remain continuous across the dielectric interfaces but exhibit pronounced bending near the spherical surfaces, consistent with the boundary conditions imposed by the dielectric mismatch.

Unlike the isolated single-sphere problem, for which the internal electrostatic field is exactly uniform and the equipotential surfaces inside the sphere are strictly planar, the interacting two-sphere geometry generally breaks the full spherical symmetry and induces higher-order multipolar contributions. As a consequence, the electric field inside each sphere is not exactly uniform, and the internal equipotential contours acquire a slight curvature, as can be appreciated in the present configuration. This departure from uniformity is a direct manifestation of the electrostatic coupling between the two spheres.

It is worth emphasizing, however, that this nonuniformity depends sensitively on the separation between the spheres. In the limit of large center-to-center distance, the mutual interaction becomes negligible, higher-order multipolar corrections are progressively suppressed, and each sphere asymptotically recovers the behavior of an isolated dielectric sphere embedded in a uniform external field, for which the internal electric field becomes exactly homogeneous. The configuration shown here corresponds to a moderate separation chosen to make the interaction-induced deviations from the isolated-sphere limit visually explicit.

Far from the spheres, the field lines recover the uniform external-field configuration, confirming the localized nature of the perturbation. This electrostatic solution provides the baseline configuration upon which the axion-induced magnetoelectric response is computed at leading order.

## V.2Perpendicular external electric field

We now consider the configuration in which the externally applied uniform electric field is perpendicular to the line joining the centers of the two spheres. Without loss of generality, we take𝐄0=E0​𝐲^\mathbf{E}_{0}=E_{0}\hat{\mathbf{y}}, so that the corresponding far-field electrostatic potential isϕ0=−E0​y\phi_{0}=-E_{0}y.

In contrast to the parallel configuration, this orientation breaks the reflection symmetry with respect to thex​yxyplane and excites angular modes with azimuthal dependence. In bispherical coordinates, the Cartesian coordinateyyis proportional tosin⁡ξ​sin⁡ϕ/(cosh⁡η−cos⁡ξ)\sin\xi\sin\phi/(\cosh\eta-\cos\xi), implying that the external field couples selectively to them=1m=1sector of the bispherical harmonics. As a consequence, the electrostatic potential must be expanded in terms of the associated Legendre functionsPn1​(cos⁡ξ)P_{n}^{1}(\cos\xi)multiplied bysin⁡ϕ\sin\phi.

Guided by the general solution of Laplace’s equation and by the required asymptotic matching to the uniform external field, we write the potential in the exterior dielectric region asϕe​(η,ξ,ϕ)=(cosh⁡η−cos⁡ξ)1/2​∑n=1∞[Cn​cosh⁡(n¯​η)−23/2​E0​a​e−n¯​η]​Pn1​(cos⁡ξ)​sin⁡ϕ,\displaystyle\phi_{e}(\eta,\xi,\phi)=(\cosh\eta-\cos\xi)^{1/2}\sum_{n=1}^{\infty}\left[C_{n}\cosh(\bar{n}\eta)-2^{3/2}E_{0}a\,e^{-\bar{n}\eta}\right]P_{n}^{1}(\cos\xi)\sin\phi,(42)

wheren¯=n+12\bar{n}=n+\tfrac{1}{2}. The second term inside the brackets represents the particular solution associated with the applied field and guarantees the correct far-field behavior, while the coefficientsCnC_{n}encode the electrostatic response of the two-sphere system.

Inside the upper sphere, regularity atη→+∞\eta\to+\inftyrestricts the solution to decaying modes, and the potential can be written asϕ+​(η,ξ,ϕ)=(cosh⁡η−cos⁡ξ)1/2​∑n=1∞Dn​e−n¯​η​Pn1​(cos⁡ξ)​sin⁡ϕ.\displaystyle\phi_{+}(\eta,\xi,\phi)=(\cosh\eta-\cos\xi)^{1/2}\sum_{n=1}^{\infty}D_{n}\,e^{-\bar{n}\eta}\,P_{n}^{1}(\cos\xi)\sin\phi.(43)

The potential inside the lower sphere follows by symmetry.

At the spherical interfaceη=η0\eta=\eta_{0}, continuity of the potential yields an algebraic relation between the interior and exterior coefficients,Dn​e−n¯​η0=Cn​cosh⁡(n¯​η0)−23/2​E0​a​e−n¯​η0,\displaystyle D_{n}e^{-\bar{n}\eta_{0}}=C_{n}\cosh(\bar{n}\eta_{0})-2^{3/2}E_{0}a\,e^{-\bar{n}\eta_{0}},(44)

which allows the coefficientsDnD_{n}to be eliminated in favor ofCnC_{n}.

The continuity of the normal component of the electric displacement field,ϵi​∂ηϕ+=ϵe​∂ηϕe\epsilon_{i}\partial_{\eta}\phi_{+}=\epsilon_{e}\partial_{\eta}\phi_{e},
then leads, after differentiation and reduction of the angular structure using standard recurrence relations of the associated Legendre functions, to a three-term difference equation for the coefficientsCnC_{n}. The explicit form of this recurrence relation and its derivation are given in AppendixB.

The resulting equation couples neighboring multipoles and depends on the geometric parameterη0\eta_{0}and on the dielectric contrastΔ=ϵi−ϵeϵi+ϵe.\displaystyle\Delta=\frac{\epsilon_{i}-\epsilon_{e}}{\epsilon_{i}+\epsilon_{e}}.(45)

For physically relevant configurations one has|Δ|<1|\Delta|<1, while the condition of nonoverlapping spheres impliese−η0<1e^{-\eta_{0}}<1. Inspection of the recurrence relation shows that the coupling between different multipole orders is suppressed by factors ofΔ​e−2​n​η0\Delta e^{-2n\eta_{0}}, which naturally suggests a perturbative solution of the formCn=Cn(0)+Cn(1)+Cn(2)+⋯.\displaystyle C_{n}=C_{n}^{(0)}+C_{n}^{(1)}+C_{n}^{(2)}+\cdots.(46)

At leading order, the recurrence relation admits a constant solution,Cn(0)=2Δ−3​e−η0,\displaystyle C_{n}^{(0)}=\frac{2}{\Delta-3}\,e^{-\eta_{0}},(47)

which corresponds to the dipolar response of each sphere in the presence of the transverse uniform field, neglecting multiple scattering effects.

Higher-order corrections describe successive electrostatic reflections between the two spheres. Up to second order, these corrections can be written in the compact formCn(1)\displaystyle C_{n}^{(1)}=Δ​e−2​n​η0​(α(1)+β(1)n)+𝒪​(e−6​η0),α(1)=2​e−2​η03−Δ,\displaystyle=\Delta e^{-2n\eta_{0}}\left(\alpha^{(1)}+\frac{\beta^{(1)}}{n}\right)+\mathcal{O}(e^{-6\eta_{0}}),\quad\alpha^{(1)}=\frac{2e^{-2\eta_{0}}}{3-\Delta},(48)Cn(2)\displaystyle C_{n}^{(2)}=Δ​e−2​n​η0​(α(2)+β(2)n),α(2)=e−η0​α(1),\displaystyle=\Delta e^{-2n\eta_{0}}\left(\alpha^{(2)}+\frac{\beta^{(2)}}{n}\right),\qquad\alpha^{(2)}=e^{-\eta_{0}}\alpha^{(1)},(49)

where the coefficientsβ(1)\beta^{(1)}andβ(2)\beta^{(2)}are given explicitly in AppendixB.

The perturbative solution reveals that the perpendicular field excites a well-defined hierarchy ofm=1m=1multipolar contributions, whose amplitudes are progressively suppressed by powers ofe−η0e^{-\eta_{0}}. This structure allows the electrostatic problem to be truncated consistently at second order for the purposes of the axion-induced analysis.Figure 3:Zeroth-order electrostatic configuration for two identical dielectric spheres embedded in a homogeneous dielectric medium and subjected to a uniform external electric field perpendicular to the center-to-center axis. The spheres are separated along the verticalzz-axis, while the external field is applied along the horizontalyy-direction. The left panel shows the equipotential lines, whereas the right panel displays the corresponding electric field lines. In contrast to the parallel configuration, the electric field does not exhibit a pronounced enhancement in the inter-sphere region; instead, the field lines are predominantly deflected sideways as they flow around the spherical interfaces. Far from the spheres, the field approaches the uniform external-field configuration, confirming the localized nature of the electrostatic perturbation.

In Fig.3we show the zeroth-order electrostatic solution for two identical dielectric spheres when the external electric field is oriented perpendicular to the center-to-center axis. As in the parallel configuration, the left panel displays the equipotential lines, while the right panel shows the corresponding electric field lines. In this geometry, the external field is directed along the horizontalyy-axis, whereas the spheres are separated along the verticalzz-axis, leading to a qualitatively different distortion pattern compared to the parallel case.

The equipotential lines exhibit a lateral squeezing around each sphere, with a pronounced asymmetry between the regions facing the external field and those aligned along the inter-sphere axis. Unlike the parallel configuration, the interstitial region between the two spheres does not display a strong enhancement of the electric field. Instead, the field lines are predominantly deflected sideways, flowing around the spheres with only weak mutual focusing. This reflects the reduced electrostatic coupling between the induced multipoles in the perpendicular geometry.

The electric field lines remain continuous across the dielectric interfaces and bend smoothly around the spherical surfaces, consistent with the electrostatic boundary conditions. Unlike the isolated single-sphere problem, where the internal electric field is exactly uniform and the equipotential surfaces inside the sphere are strictly planar, the interacting two-sphere geometry generally induces a spatially nonuniform internal field due to the breaking of full spherical symmetry by the neighboring sphere. In the perpendicular configuration, however, this effect is comparatively weaker than in the parallel case, since the electrostatic interaction between the induced multipoles is less pronounced. As a result, the internal distortion remains relatively mild, although the equipotential contours still exhibit a measurable departure from exact planarity.

As in the parallel geometry, this interaction-induced nonuniformity gradually disappears as the center-to-center separation increases. In the large-distance limit, the electrostatic coupling between the spheres becomes negligible, the higher-order multipolar corrections are suppressed, and each sphere asymptotically recovers the exact isolated-sphere behavior, characterized by a homogeneous internal electric field in the presence of the external uniform field.

Far from the spheres, the field lines recover the uniform external-field configuration along theyy-direction. The absence of strong field amplification in the region between the spheres highlights the crucial role of geometry in controlling the electrostatic interaction. This perpendicular configuration therefore provides a contrasting baseline to the parallel case and serves as a complementary reference for assessing the geometry-dependent axion-induced magnetoelectric response discussed in the subsequent sections.

## V.3Mapping to the magnetostatic problem

The electrostatic analysis developed in the previous sections admits a direct and exact mapping to the corresponding magnetostatic problem of two permeable spheres in an external magnetic field. This mapping follows from the formal equivalence between electrostatics in linear dielectric media and magnetostatics in linear magnetic media in the absence of free sources.

We consider two spheres of magnetic permeabilityμi\mu_{i}embedded in a medium of permeabilityμe\mu_{e}, subjected to a uniform external magnetic field𝐇0\mathbf{H}_{0}, oriented either parallel or perpendicular to the center-to-center axis. In the static, source-free regime, the magnetic fields satisfy∇×𝐇\displaystyle\nabla\times\mathbf{H}=𝟎,\displaystyle=\mathbf{0},(50)∇⋅𝐁\displaystyle\nabla\cdot\mathbf{B}=0,\displaystyle=0,(51)

with the constitutive relation𝐁=μ​𝐇\mathbf{B}=\mu\,\mathbf{H}. Since∇×𝐇=0\nabla\times\mathbf{H}=0, the magnetic field can be expressed in terms of a scalar magnetic potential,𝐇=−∇ψ,\displaystyle\mathbf{H}=-\nabla\psi,(52)

which satisfies Laplace’s equation in each region of space,∇2ψ=0.\displaystyle\nabla^{2}\psi=0.(53)

The boundary conditions at each spherical interface are the continuity of the magnetic scalar potential and of the normal component of the magnetic induction,ψi=ψe,μi​∂nψi=μe​∂nψe,\displaystyle\psi_{i}=\psi_{e},\qquad\mu_{i}\,\partial_{n}\psi_{i}=\mu_{e}\,\partial_{n}\psi_{e},(54)

which are formally identical to the electrostatic boundary conditions for the electric potentialϕ\phiupon the replacementϵ→μ\epsilon\rightarrow\mu.

As a consequence, the complete magnetostatic solution can be obtained from the electrostatic one through the substitutionsϕ→ψ,E0→H0,ϵi→μi,ϵe→μe,\displaystyle\phi\;\rightarrow\;\psi,\qquad E_{0}\;\rightarrow\;H_{0},\qquad\epsilon_{i}\;\rightarrow\;\mu_{i},\qquad\epsilon_{e}\;\rightarrow\;\mu_{e},(55)

with no further modifications to the functional form of the solution. In particular, all bispherical mode expansions, recurrence relations, and perturbative solutions derived for the electrostatic problem remain valid under this mapping.

This correspondence allows us to treat electric and magnetic responses on the same footing, and will be exploited in the following sections when discussing the axion-induced magnetoelectric coupling of the topological insulator spheres.Figure 4:Magnetostatic field lines for two identical permeable spheres embedded in a homogeneous medium and subjected to a uniform external magnetic field. The spheres are separated along thezz-axis. The left panel corresponds to a magnetic field applied parallel to the center-to-center axis, while the right panel shows the perpendicular configuration. In the parallel case, the field lines concentrate in the inter-sphere region, whereas for the perpendicular orientation they are mainly deflected around the spheres. Far from the spheres, the magnetic field approaches the uniform external configuration.

To illustrate the magnetostatic problem we show in Fig.4the magnetic field lines for two identical permeable spheres embedded in a homogeneous medium and subjected to a uniform external magnetic field. As in the electrostatic case, the spheres are separated along thezz-axis, while the external magnetic field is applied either parallel (left panel) or perpendicular (right panel) to this axis.

In the parallel configuration (left panel), the magnetic field lines are strongly distorted in the region between the two spheres, exhibiting a clear concentration along the center-to-center axis. This behavior reflects the constructive coupling between the induced magnetic dipoles, which align with the external field and reinforce each other in the inter-sphere region. Near the spherical interfaces, the field lines bend smoothly and intersect the surfaces in a manner consistent with the magnetostatic boundary conditions imposed by the permeability contrast. Far from the spheres, the magnetic field approaches the uniform external configuration, confirming the localized nature of the induced perturbation.

In contrast, when the external magnetic field is oriented perpendicular to the center-to-center axis (right panel), the field lines are predominantly deflected sideways as they flow around the spheres. In this geometry, the mutual interaction between the induced magnetic moments is weaker, and no pronounced enhancement of the magnetic field is observed in the region between the spheres. Instead, the distortion remains localized near each sphere, highlighting the strong dependence of the magnetostatic response on the relative orientation between the external field and the sphere separation axis.

## VIAxion-induced electromagnetic response

We now turn to the electromagnetic response induced by the axion term. Using the classical electrostatic solutions obtained above as the zeroth-order input, we treat the topological magnetoelectric coupling perturbatively in the fine-structure constantα\alpha. In the present geometry the axion field is piecewise constant, so that the axion-induced sources are confined to the spherical interfaces and generate interfacial electromagnetic responses. We analyze the leading axion-induced contribution for different orientations of the externally applied electric field.

## VI.1Parallel configuration: axion-induced magnetic response

We now turn to the leading axion-induced correction in the configuration𝐄0=E0​𝐳^\mathbf{E}_{0}=E_{0}\hat{\mathbf{z}}. Since the zeroth-order electrostatic potentialϕ(0)​(η,ξ)\phi^{(0)}(\eta,\xi)is axisymmetric, all zeroth-order quantities are independent of the azimuthal angleϕ\phi. In addition, the axion fieldθ\thetais piecewise constant and its gradient is supported exclusively on the spherical interfaces, as made explicit by Eq. (28). As a result, the axion-induced source terms entering the first-order Maxwell equations are localized at the interfaces and the Green-function representation (24) reduces to a purely interfacial contribution.

Using𝐄(0)=−∇ϕ(0)\mathbf{E}^{(0)}=-\nabla\phi^{(0)}and the fact that∂ϕϕ(0)=0\partial_{\phi}\phi^{(0)}=0, the axion-induced current density entering Ampère’s law is purely azimuthal. For two identical spheres whose surfaces are located atη=±η0\eta=\pm\eta_{0}, one finds∇θ×∇ϕ(0)​(η,ξ)=−(cosh⁡η−cos⁡ξ)2a2​θ​ϕ^​[δ​(η−η0)+δ​(η+η0)]​∂ξϕ(0)​(η,ξ),\displaystyle\nabla\theta\times\nabla\phi^{(0)}(\eta,\xi)=-\frac{(\cosh\eta-\cos\xi)^{2}}{a^{2}}\,\theta\,\hat{\bm{\phi}}\,\big[\delta(\eta-\eta_{0})+\delta(\eta+\eta_{0})\big]\,\partial_{\xi}\phi^{(0)}(\eta,\xi),(56)

whereϕ^=−𝐱^​sin⁡ϕ+𝐲^​cos⁡ϕ\hat{\bm{\phi}}=-\hat{\mathbf{x}}\sin\phi+\hat{\mathbf{y}}\cos\phi. Equation (56) shows that the axion-induced surface current on each sphere circulates around the symmetry axis, which implies that the induced vector potential can be chosen to be purely azimuthal,𝐀(1)​(η,ξ,ϕ)=Aϕ(1)​(η,ξ)​ϕ^,∂ϕAϕ(1)=0.\displaystyle\mathbf{A}^{(1)}(\eta,\xi,\phi)=A^{(1)}_{\phi}(\eta,\xi)\,\hat{\bm{\phi}},\qquad\partial_{\phi}A^{(1)}_{\phi}=0.(57)

Substituting Eq. (56) into the Green-function representation (24) yields𝐀(1)​(𝐫)=−α​θπ​∫d3​𝐫′​ϕ^′​G0​(𝐫,𝐫′)​a​sin⁡ξ′cosh⁡η′−cos⁡ξ′​[δ​(η′−η0)+δ​(η′+η0)]​∂ξ′ϕ(0)​(η′,ξ′),\displaystyle\mathbf{A}^{(1)}(\mathbf{r})=-\frac{\alpha\theta}{\pi}\int d^{3}\mathbf{r}^{\prime}\;\hat{\bm{\phi}}^{\prime}\,G_{0}(\mathbf{r},\mathbf{r}^{\prime})\frac{a\sin\xi^{\prime}}{\cosh\eta^{\prime}-\cos\xi^{\prime}}\,\big[\delta(\eta^{\prime}-\eta_{0})+\delta(\eta^{\prime}+\eta_{0})\big]\,\partial_{\xi^{\prime}}\phi^{(0)}(\eta^{\prime},\xi^{\prime}),(58)

whereG0​(𝐫,𝐫′)=−(cosh⁡(η)−cos⁡(ξ))1/2​(cosh⁡(η′)−cos⁡(ξ′))1/2a​∑n,m12​n¯​e−n¯​|η−η′|​Ynm​(ξ,ϕ)​Ynm⁣∗​(ξ′,ϕ′)\displaystyle G_{0}(\mathbf{r},\mathbf{r}^{\prime})=-\frac{(\cosh{\eta}-\cos{\xi})^{1/2}(\cosh{\eta\prime}-\cos{\xi^{\prime}})^{1/2}}{a}\sum\limits_{n,m}\frac{1}{2\bar{n}}e^{-\bar{n}\absolutevalue{\eta-\eta^{\prime}}}Y_{n}^{m}\quantity(\xi,\phi)Y_{n}^{m\,\ast}\quantity(\xi^{\prime},\phi^{\prime})(59)

Performing theη′\eta^{\prime}integration collapses the volume integral into the sum of two surface integrals, one over each spherical interface. The remaining angular integrals can be evaluated by expanding the Green functionG0​(𝐫,𝐫′)G_{0}(\mathbf{r},\mathbf{r}^{\prime})in bispherical harmonics and exploiting their orthogonality properties.

Carrying out this procedure, as detailed in AppendixC, leads to a compact series representation for the azimuthal component of the vector potential,Aϕ(1)​(η,ξ)=−α​θπ​(cosh⁡η−cos⁡ξ)1/2​∑n=0∞𝒦n​(η;η0)​Pn1​(cos⁡ξ),\displaystyle A^{(1)}_{\phi}(\eta,\xi)=-\frac{\alpha\theta}{\pi}\,(\cosh\eta-\cos\xi)^{1/2}\sum_{n=0}^{\infty}\mathcal{K}_{n}(\eta;\eta_{0})\,P_{n}^{1}(\cos\xi),(60)

where the kernel𝒦n\mathcal{K}_{n}depends on the interface locations±η0\pm\eta_{0}and on the zeroth-order electrostatic coefficients through the combinationAn​sinh⁡(n¯​η0)−23/2​E0​a​n¯​e−n¯​η0A_{n}\sinh(\bar{n}\eta_{0})-2^{3/2}E_{0}a\,\bar{n}e^{-\bar{n}\eta_{0}}, withn¯=n+1/2\bar{n}=n+1/2. The explicit form of𝒦n\mathcal{K}_{n}is given in AppendixC.

Since𝐀(1)\mathbf{A}^{(1)}is purely azimuthal, the induced magnetic field𝐁(1)=∇×𝐀(1)\mathbf{B}^{(1)}=\nabla\times\mathbf{A}^{(1)}has onlyη\etaandξ\xicomponents. In bispherical coordinates it can be written as𝐁(1)=(cosh⁡η−cos⁡ξ)2a2​sin⁡ξ​[𝜼^​∂ξ−𝝃^​∂η]​(sin⁡ξcosh⁡η−cos⁡ξ​Aϕ(1)​(η,ξ)),\displaystyle\mathbf{B}^{(1)}=\frac{(\cosh\eta-\cos\xi)^{2}}{a^{2}\sin\xi}\Big[\hat{\bm{\eta}}\,\partial_{\xi}-\hat{\bm{\xi}}\,\partial_{\eta}\Big]\left(\frac{\sin\xi}{\cosh\eta-\cos\xi}\,A^{(1)}_{\phi}(\eta,\xi)\right),(61)

in agreement with the expression used in the derivation. The magnetic field lines in the meridional(η,ξ)(\eta,\xi)plane follow from the tangency conditiond​ℓ×𝐁(1)=𝟎d\bm{\ell}\times\mathbf{B}^{(1)}=\mathbf{0}, withd​ℓ=acosh⁡η−cos⁡ξ​(d​η​𝜼^+d​ξ​𝝃^)d\bm{\ell}=\frac{a}{\cosh\eta-\cos\xi}(d\eta\,\hat{\bm{\eta}}+d\xi\,\hat{\bm{\xi}}). This yields the first integralsin⁡ξcosh⁡η−cos⁡ξ​Aϕ(1)​(η,ξ)=const.,\displaystyle\frac{\sin\xi}{\cosh\eta-\cos\xi}\,A^{(1)}_{\phi}(\eta,\xi)=\text{const.},(62)

showing that the axion-induced magnetic streamlines are given by the level sets of the scalar function(sin⁡ξ/(cosh⁡η−cos⁡ξ))​Aϕ(1)​(η,ξ)(\sin\xi/(\cosh\eta-\cos\xi))A^{(1)}_{\phi}(\eta,\xi).

We now turn to the axion-induced magnetic response for the configuration in which the external electric field is applied parallel to the center-to-center axis of the two spheres. Figure5, left panel, shows the resulting magnetic field lines generated by the topological magnetoelectric effect, while the right panel displays the corresponding induced surface current density on the spheres.

The induced current is entirely localized at the spherical interfaces and corresponds to a Hall-type surface current generated by the axion term. Its spatial distribution is strongly inhomogeneous and concentrated near the polar regions of each sphere, where the normal component of the electric field is largest. The opposite orientation of the current patterns on the two spheres reflects the symmetry of the electrostatic background and the relative orientation of the induced surface Hall responses.

The magnetic field lines form closed loops characteristic of localized current distributions and exhibit a clear multipolar structure. For each individual sphere, the dominant contribution is dipolar, with an effective magnetic moment aligned parallel to the external electric field. This behavior is consistent with the interpretation of the axion term as inducing a magnetization proportional to the applied electric field. In the two-sphere configuration, however, the superposition of the individual responses leads to a nontrivial field topology, with additional quadrupolar-like features arising from the interaction between the spheres.

In particular, the magnetic field lines are strongly distorted in the region between the spheres, where the induced magnetic dipoles couple constructively along the symmetry axis. This interaction enhances the magnetic field in the inter-sphere region and gives rise to a characteristic four-lobe pattern in the surrounding space. Far from the spheres, the magnetic field decays rapidly, confirming the localized nature of the axion-induced response and its interpretation in terms of effective multipolar sources confined to the interfaces.

These results provide a direct visualization of how the surface Hall currents generated by the axion term give rise to geometry-dependent magnetostatic fields, and they highlight the close connection between the electrostatic background, the induced interfacial currents, and the resulting magnetic multipole structure.Figure 5:Axion-induced magnetic response for two topological insulator spheres subjected to an external electric field parallel to the center-to-center axis. The left panel shows the magnetic field lines generated by the axion-induced surface currents, while the right panel displays the corresponding induced surface current density. The current is purely interfacial and corresponds to a Hall-type response localized on the spherical surfaces, giving rise to a magnetostatic field with a clear multipolar structure.

## VI.2Perpendicular configuration: axion-induced magnetic response

We now consider the axion-induced electromagnetic response for an externally applied electric field perpendicular to the center-to-center axis of the two spheres. In this configuration, the zeroth-order electrostatic potentialϕ(0)​(η,ξ,ϕ)\phi^{(0)}(\eta,\xi,\phi)obtained in Sec.V.2exhibits an explicit dependence on the azimuthal angleϕ\phiand is dominated bym=1m=1bispherical harmonics. As a result, the reduced axial symmetry of the problem leads to a more complex structure of the axion-induced fields than in the parallel case.

At first order in the axion coupling, the vector potential satisfies
Eq. (22),∇2𝐀(1)=−απ​∇θ×∇ϕ(0),\displaystyle\nabla^{2}\mathbf{A}^{(1)}=-\frac{\alpha}{\pi}\,\nabla\theta\times\nabla\phi^{(0)},(63)

where the gradient of the axion field∇θ\nabla\thetais localized at the spherical interfaces, as given explicitly in Eq. (28). Evaluating the cross product with the zeroth-order electric field,𝐄(0)=−∇ϕ(0)\mathbf{E}^{(0)}=-\nabla\phi^{(0)}, one finds that the axion-induced source contains both azimuthal and polar contributions, reflecting the lack of axial symmetry in the perpendicular geometry.

Substitution of Eq. (63) into the Green-function representation (24) reduces the volume integral to surface contributions on the two interfaces. Expanding the Green’s function in bispherical harmonics and projecting onto the appropriate angular modes, the first-order vector potential can be written as a superposition of Cartesian components,𝐀(1)​(η,ξ,ϕ)=Ax(1)​(η,ξ,ϕ)​𝐱^+Ay(1)​(η,ξ,ϕ)​𝐲^+Az(1)​(η,ξ)​𝐳^,\displaystyle\mathbf{A}^{(1)}(\eta,\xi,\phi)=A_{x}^{(1)}(\eta,\xi,\phi)\,\hat{\mathbf{x}}+A_{y}^{(1)}(\eta,\xi,\phi)\,\hat{\mathbf{y}}+A_{z}^{(1)}(\eta,\xi)\,\hat{\mathbf{z}},(64)

whereAx(1)A_{x}^{(1)}andAy(1)A_{y}^{(1)}involve angular harmonics withm=0,±2m=0,\pm 2, whileAz(1)A_{z}^{(1)}is associated withm=±1m=\pm 1modes.

After performing the angular integrations, the components of the vector potential can be expressed as rapidly convergent series in terms of the zeroth-order electrostatic coefficientsCnC_{n},Ai(1)​(η,ξ,ϕ)=−α​θ2​π​∑n=0∞[Cn​cosh⁡(n¯​η0)−23/2​E0​a​e−n¯​η0]​ℱi,n​(η,ξ,ϕ),i=x,y,z,\displaystyle A_{i}^{(1)}(\eta,\xi,\phi)=-\frac{\alpha\theta}{2\pi}\sum_{n=0}^{\infty}\Big[C_{n}\cosh(\bar{n}\eta_{0})-2^{3/2}E_{0}a\,e^{-\bar{n}\eta_{0}}\Big]\,\mathcal{F}_{i,n}(\eta,\xi,\phi),\qquad i=x,y,z,(65)

where the functionsℱi,n\mathcal{F}_{i,n}encode the angular dependence and the geometry of the two interfaces. Their explicit expressions are given in AppendixD.

The axion-induced magnetic field follows from𝐁(1)=∇×𝐀(1)\mathbf{B}^{(1)}=\nabla\times\mathbf{A}^{(1)}. In contrast to the parallel configuration, all components of𝐁(1)\mathbf{B}^{(1)}are generally nonzero in the perpendicular case, reflecting the reduced symmetry of the problem. Nevertheless, the magnetic response remains entirely interfacial in origin and is fully determined by the zeroth-order electrostatic solution.

For moderate separations between the spheres (e−η0≪1e^{-\eta_{0}}\ll 1), the series in Eq. (65) converges rapidly, and the leading contributions provide an accurate description of the axion-induced magnetic response in the perpendicular configuration.Figure 6:Axion-induced magnetic field and surface Hall current for the perpendicular configuration. The upper panels display the magnetic field lines generated by the axion-induced surface currents: the upper-left panel corresponds to a transverse cross section, while the upper-right panel shows the field lines in the planeϕ=π/10\phi=\pi/10. The lower panels show the corresponding transverse sections of the surface Hall current on the spheres; the color scale represents the local current magnitude. The comparison between the different cuts highlights the rotation and redistribution of both the magnetic field and the surface current, reflecting the breaking of azimuthal symmetry produced by the orientation of the external electric field.

As we know, the induced magnetic field is sourced by an interfacial Hall current on each topological-insulator sphere,𝐉H∝𝐧^×𝐄(0)\mathbf{J}_{\!H}\propto\hat{\mathbf{n}}\times\mathbf{E}^{(0)},
driven by the tangential component of the zeroth-order electric field at the surface.
Unlike the parallel case, the external field is not aligned with the center-to-center axis, and the response no longer exhibits full azimuthal symmetry aboutzz.
As a consequence, the surface current develops an intrinsically three-dimensional pattern.

Figure6displays the resulting magnetostatic configuration together with representative transverse sections of the surface current.
The upper panels show the magnetic field lines generated by the axion-induced Hall currents: the upper-left panel corresponds to a transverse cross section, while the upper-right panel shows the field structure in the planeϕ=π/10\phi=\pi/10, thereby exposing the angular dependence of the response.
The lower panels show transverse cuts of the surface current distribution, with the left panel corresponding to a cut in theyydirection and the right panel to a cut in thexxdirection; the color scale represents the local current magnitude.

Theyy-cut reveals a largely symmetric flow on each sphere: the current lines are organized in broad meridional streams on the visible cross section, with a clear up-down reversal between the upper and lower spheres, consistent with the reflection symmetry of the two-sphere arrangement with respect to the midplane between them.
In this section the current magnitude varies smoothly along the surface, indicating that the response is governed by the regular spatial variation of𝐄(0)\mathbf{E}^{(0)}.

Thexx-cut, on the other hand, displays a systematic rotation of the current pattern relative to theyy-section, reflecting the explicit breaking of azimuthal symmetry introduced by the lateral orientation of the external field.
Rather than producing a strongly irregular distribution, the current remains coherent over extended surface regions, but its direction and intensity are redistributed between the two hemispheres of each sphere according to the sign of the local tangential field.
This controlled departure from axial symmetry signals the presence of angular components withm=±1m=\pm 1, in contrast with the purely axisymmetric structure characteristic of the parallel geometry.

The magnetic field lines shown in the upper panels directly mirror this behavior.
In the transverse section, the field forms closed-loop structures characteristic of localized current sources, while theϕ=π/10\phi=\pi/10plane makes explicit the three-dimensional deformation of the field pattern.
Far from the spheres, the magnetic field decays rapidly, confirming its multipolar nature and the absence of net magnetic charge.
Together, these panels make clear that the perpendicular configuration leads to a nonaxisymmetric but smooth magnetostatic response entirely determined by the geometry of the induced surface Hall currents.

These surface Hall currents constitute the sole sources of the axion-induced magnetostatic field in the bulk.
The nonaxisymmetric but smooth character observed in the transverse cuts anticipates a magnetic response with mixed multipolar content, whose detailed field-line topology will be presented once the corresponding𝐁\mathbf{B}configuration is available.

## VIIResults and Discussion

In this work we have obtained an analytically controlled description of the static electromagnetic response of two spherical topological insulators embedded in a dielectric medium and subjected to a uniform external electric field. The problem was addressed by combining an exact zeroth-order electrostatic solution in bispherical coordinates with a perturbative treatment of the axion-induced magnetoelectric coupling. This strategy allows us to clearly disentangle classical dielectric effects from genuinely topological contributions and to identify the physical mechanisms responsible for the induced magnetostatic response.

At zeroth order in the axion coupling, the electrostatic problem reduces to the classical response of two dielectric spheres in an external field. By exploiting the separability of Laplace’s equation in bispherical coordinates, we obtained exact mode expansions for both parallel and perpendicular orientations of the applied field. In each case, the boundary conditions at the spherical interfaces lead to three-term recurrence relations for the expansion coefficients. These relations encode multiple electrostatic scattering between the spheres and admit a natural perturbative solution in the regime of nonoverlapping spheres, wheree−η0≪1e^{-\eta_{0}}\ll 1. Explicit solutions up to second order were constructed, providing a quantitatively accurate seed for the subsequent axion-induced analysis.

The axion-induced electromagnetic response arises at first order in the fine-structure constant and is entirely interfacial in origin. Because the axion field is piecewise constant, the induced sources are localized on the spherical boundaries and are fully determined by the zeroth-order electric field evaluated at the interfaces. This feature allows the axion-induced fields to be expressed in closed form in terms of the previously obtained electrostatic coefficients, without the need to impose modified boundary conditions order by order.

In the parallel configuration, the axial symmetry of the problem implies that the axion-induced surface currents circulate azimuthally around the center-to-center axis. As a result, the induced vector potential is purely azimuthal and the corresponding magnetic field lies in the meridional(η,ξ)(\eta,\xi)plane. The magnetic streamlines are governed by a single scalar invariant,sin⁡ξcosh⁡η−cos⁡ξ​Aϕ(1)​(η,ξ)=const.,\frac{\sin\xi}{\cosh\eta-\cos\xi}\,A^{(1)}_{\phi}(\eta,\xi)=\mathrm{const.},(66)

which provides a transparent geometrical interpretation of the induced magnetostatic structure. The resulting field lines resemble closed loops linking the two spheres, reflecting the circulating nature of the axion-induced surface currents.

In contrast, the perpendicular configuration exhibits a richer angular structure due to the reduced symmetry of the zeroth-order electrostatic potential. In this case, the axion-induced sources generate vector-potential components along all three Cartesian directions. The corresponding magnetic field generally possesses nonvanishingη\eta,ξ\xi, andϕ\phicomponents, leading to more intricate magnetostatic patterns. Nevertheless, the response remains fully controlled by the same perturbative framework: all axion-induced fields can be written as rapidly convergent series whose amplitudes are fixed by the electrostatic coefficientsCnC_{n}obtained at zeroth order.

An important outcome of our analysis is the rapid convergence of both the electrostatic and axion-induced series for moderate sphere separations. In practice, retaining terms up to second order in the perturbative expansion is sufficient to capture the leading interaction effects between the spheres and to construct reliable magnetostatic field profiles. This makes the present approach particularly suitable for analytical and semi-analytical studies of finite topological systems, where purely numerical treatments often obscure the underlying physical mechanisms.

From a physical perspective, our results highlight how the topological magnetoelectric effect manifests itself in interacting finite geometries. The induced magnetic response does not arise from intrinsic magnetism, but from the coupling between the externally induced electric polarization and the topological axion term at the interfaces. The dependence of the induced fields on the orientation of the external electric field provides a clear qualitative signature of the axion electrodynamics of topological insulators, which could be exploited in experimental probes of magnetoelectric nanoparticles, including topological and more general isotropic magnetoelectric materials.

Finally, while the present work focuses on static fields and nonoverlapping spheres, the framework developed here can be extended in several directions. Possible generalizations include spheres with different radii or axion parameters, configurations involving external magnetic fields, and dynamical responses at finite frequency. More broadly, our results provide a concrete analytical platform for exploring axion-induced electromagnetic phenomena in interacting mesoscopic systems, bridging the gap between idealized single-particle models and realistic multi-object geometries.

## Acknowledgements.J.C.G., M.I.-M. and L.M.O. was supported by the SECIHTI fellowships No. 1165841, No. 4065997 and No. 834773, respectively. A.M.-R. acknowledges financial support by UNAM-PAPIIT project No. IG100224, UNAM-PAPIME project No. PE109226, by SECIHTI project No. CBF-2025-I-1862 and by the Marcos Moshinsky Foundation.

## Appendix ADerivation and perturbative solution of the recurrence relations for the parallel configuration

In this appendix we present the derivation of the recurrence relations satisfied by the expansion coefficients of the electrostatic potential in the case of an external electric field parallel to the center-to-center axis, together with their perturbative solution up to second order. The purpose is to make explicit the main steps of the calculation while avoiding unnecessary algebraic repetition.

## A.1From boundary conditions to recurrence relations

The electrostatic potentials inside and outside the spheres are expanded asϕe​(η,ξ)\displaystyle\phi_{e}(\eta,\xi)=(cosh⁡η−cos⁡ξ)1/2​∑n=0∞[An​sinh⁡(n¯​η)−23/2​E0​a​n¯​e−n¯​η]​Pn​(cos⁡ξ),\displaystyle=(\cosh\eta-\cos\xi)^{1/2}\sum_{n=0}^{\infty}\left[A_{n}\sinh(\bar{n}\eta)-2^{3/2}E_{0}a\,\bar{n}e^{-\bar{n}\eta}\right]P_{n}(\cos\xi),(67)ϕ+​(η,ξ)\displaystyle\phi_{+}(\eta,\xi)=(cosh⁡η−cos⁡ξ)1/2​∑n=0∞Bn​e−n¯​η​Pn​(cos⁡ξ),\displaystyle=(\cosh\eta-\cos\xi)^{1/2}\sum_{n=0}^{\infty}B_{n}e^{-\bar{n}\eta}P_{n}(\cos\xi),(68)

withn¯=n+1/2\bar{n}=n+1/2.

Imposing continuity of the potential at the spherical surfaceη=η0\eta=\eta_{0}leads to the algebraic relationBn​e−n¯​η0=An​sinh⁡(n¯​η0)−23/2​E0​a​n¯​e−n¯​η0,\displaystyle B_{n}e^{-\bar{n}\eta_{0}}=A_{n}\sinh(\bar{n}\eta_{0})-2^{3/2}E_{0}a\,\bar{n}e^{-\bar{n}\eta_{0}},(69)

which allows the interior coefficientsBnB_{n}to be eliminated in favor of
the exterior onesAnA_{n}.

The continuity of the normal component of the electric displacement field,ϵi​∂ηϕ+=ϵe​∂ηϕe\epsilon_{i}\partial_{\eta}\phi_{+}=\epsilon_{e}\partial_{\eta}\phi_{e},
requires the computation of∂ηϕe\partial_{\eta}\phi_{e}and∂ηϕ+\partial_{\eta}\phi_{+}. After differentiation and expansion in Legendre
polynomials, terms proportional tocos⁡ξ​Pn​(cos⁡ξ)\cos\xi\,P_{n}(\cos\xi)are reduced using
the standard recurrence relationcos⁡ξ​Pn​(cos⁡ξ)=n2​n+1​Pn−1​(cos⁡ξ)+n+12​n+1​Pn+1​(cos⁡ξ).\displaystyle\cos\xi\,P_{n}(\cos\xi)=\frac{n}{2n+1}P_{n-1}(\cos\xi)+\frac{n+1}{2n+1}P_{n+1}(\cos\xi).(70)

Equating the coefficients of equal Legendre polynomials then yields a
three-term recurrence relation forAnA_{n}of the form𝒞n−1​An−1+𝒞n​An+𝒞n+1​An+1=𝒮n,\displaystyle\mathcal{C}_{n-1}A_{n-1}+\mathcal{C}_{n}A_{n}+\mathcal{C}_{n+1}A_{n+1}=\mathcal{S}_{n},(71)

where the explicit expressions of the coefficients𝒞n\mathcal{C}_{n}and the
source term𝒮n\mathcal{S}_{n}depend on the geometric parameterη0\eta_{0}and
on the dielectric contrastΔ=ϵi−ϵeϵi+ϵe.\displaystyle\Delta=\frac{\epsilon_{i}-\epsilon_{e}}{\epsilon_{i}+\epsilon_{e}}.(72)

## A.2Perturbative structure of the recurrence

For nonoverlapping spheres one hase−η0<1e^{-\eta_{0}}<1, while for physical
dielectrics|Δ|<1|\Delta|<1. Inspection of Eq. (71) shows that
the coupling between neighboring coefficientsAn±1A_{n\pm 1}is suppressed by
factors ofe−2​n​η0e^{-2n\eta_{0}}, which motivates a perturbative expansion in the
small parameterΔ​e−2​n​η0\Delta e^{-2n\eta_{0}}. We therefore writeAn=An(0)+An(1)+An(2)+⋯,\displaystyle A_{n}=A_{n}^{(0)}+A_{n}^{(1)}+A_{n}^{(2)}+\cdots,(73)

whereAn(k)=𝒪​((Δ​e−2​n​η0)k)A_{n}^{(k)}=\mathcal{O}((\Delta e^{-2n\eta_{0}})^{k}).

## A.3Zeroth-order solution

At leading order the recurrence relation simplifies considerably and
reduces to a linear difference equation with polynomial coefficients innn. Guided by its structure, we seek a solution of the formAn(0)=α​n+β.\displaystyle A_{n}^{(0)}=\alpha\,n+\beta.(74)

Substitution into the zeroth-order recurrence equation and matching the
coefficients of equal powers ofnnyields a system of algebraic equations
forα\alphaandβ\beta, whose solution isAn(0)=2​e−η03−Δ​[n−e−2​η01−e−2​η0].\displaystyle A_{n}^{(0)}=\frac{2e^{-\eta_{0}}}{3-\Delta}\left[n-\frac{e^{-2\eta_{0}}}{1-e^{-2\eta_{0}}}\right].(75)

This expression corresponds to the classical electrostatic response of two
dielectric spheres in a uniform external field.

## A.4First-order correction

At first order, the recurrence relation becomes inhomogeneous, with a source
term entirely determined byAn(0)A_{n}^{(0)}. Since the inhomogeneity is
proportional toe−2​n​η0e^{-2n\eta_{0}}, we adopt the ansatzAn(1)=Δ​e−2​n​η0​(α(1)​n+β(1)).\displaystyle A_{n}^{(1)}=\Delta e^{-2n\eta_{0}}\left(\alpha^{(1)}n+\beta^{(1)}\right).(76)

Substitution into the first-order recurrence relation and comparison of the
terms proportional ton2n^{2}immediately yieldsα(1)=2​e−2​η03−Δ.\displaystyle\alpha^{(1)}=\frac{2e^{-2\eta_{0}}}{3-\Delta}.(77)

The remaining coefficientβ(1)\beta^{(1)}follows from the terms linear and
independent innn. Expanding consistently in powers ofe−η0e^{-\eta_{0}}one
obtainsβ(1)=−1+Δ3−Δ​e−4​η0+1−Δ22​(3−Δ)​e−6​η0+𝒪​(e−8​η0),\displaystyle\beta^{(1)}=-\frac{1+\Delta}{3-\Delta}e^{-4\eta_{0}}+\frac{1-\Delta^{2}}{2(3-\Delta)}e^{-6\eta_{0}}+\mathcal{O}(e^{-8\eta_{0}}),(78)

leading toAn(1)=2​Δ​e−2​n​η03−Δ​e−2​η0​[n−1+Δ2​e−2​η0+1−Δ4​e−4​η0+𝒪​(e−6​η0)].\displaystyle A_{n}^{(1)}=\frac{2\Delta e^{-2n\eta_{0}}}{3-\Delta}e^{-2\eta_{0}}\left[n-\frac{1+\Delta}{2}e^{-2\eta_{0}}+\frac{1-\Delta}{4}e^{-4\eta_{0}}+\mathcal{O}(e^{-6\eta_{0}})\right].(79)

## A.5Second-order correction

The second-order recurrence relation is driven by the first-order
coefficientsAn(1)A_{n}^{(1)}. The same structural considerations motivate the
ansatzAn(2)=Δ​e−2​n​η0​(α(2)​n+β(2)).\displaystyle A_{n}^{(2)}=\Delta e^{-2n\eta_{0}}\left(\alpha^{(2)}n+\beta^{(2)}\right).(80)

Matching the highest-order terms innnyieldsα(2)=e−η0​α(1),\displaystyle\alpha^{(2)}=e^{-\eta_{0}}\alpha^{(1)},(81)

while the remaining constantβ(2)\beta^{(2)}is obtained by collecting the
lower-order terms. Expanding in powers ofe−η0e^{-\eta_{0}}, one findsβ(2)=−1+Δ3−Δ​e−5​η0+1+3​Δ2−2​Δ2​(3−Δ)​e−7​η0+𝒪​(e−9​η0).\displaystyle\beta^{(2)}=-\frac{1+\Delta}{3-\Delta}e^{-5\eta_{0}}+\frac{1+3\Delta^{2}-2\Delta}{2(3-\Delta)}e^{-7\eta_{0}}+\mathcal{O}(e^{-9\eta_{0}}).(82)

Thus,An(2)=Δ​e−2​n​η0​[e−η0​α(1)​n−1+Δ3−Δ​e−5​η0+𝒪​(e−7​η0)].\displaystyle A_{n}^{(2)}=\Delta e^{-2n\eta_{0}}\left[e^{-\eta_{0}}\alpha^{(1)}n-\frac{1+\Delta}{3-\Delta}e^{-5\eta_{0}}+\mathcal{O}(e^{-7\eta_{0}})\right].(83)

The perturbative expansion converges rapidly for moderate separations between the spheres, wheree−η0≪1e^{-\eta_{0}}\ll 1. Higher-order corrections describe multiple electrostatic scattering between the spheres and can be obtained recursively following the same strategy. In the present work, terms up to second order provide sufficient accuracy for constructing the axion-induced electromagnetic response discussed in the main text.

## Appendix BDerivation and perturbative solution of the recurrence relations for the perpendicular configuration

In this appendix we derive the recurrence relations satisfied by the expansion coefficients of the electrostatic potential in the perpendicular configuration,𝐄0=E0​𝐲^\mathbf{E}_{0}=E_{0}\hat{\mathbf{y}}, and present their perturbative solution up to second order. The goal is to make explicit the logical structure of the calculation while keeping the algebraic details to a manageable level.

## B.1Mode selection and exterior potential

In the perpendicular configuration the far-field electrostatic potential isϕ0=−E0​y,\displaystyle\phi_{0}=-E_{0}y,(84)

which, in bispherical coordinates, exhibits an explicitsin⁡ϕ\sin\phiangular dependence. As a consequence, only bispherical harmonics with azimuthal indexm=1m=1contribute, and the angular structure is entirely captured by the combinationPn1​(cos⁡ξ)​sin⁡ϕP_{n}^{1}(\cos\xi)\sin\phi.

A convenient expansion for the exterior potential is thereforeϕe​(η,ξ,ϕ)=(cosh⁡η−cos⁡ξ)1/2​∑n=1∞Cn​cosh⁡(n¯​η)​Pn1​(cos⁡ξ)​sin⁡ϕ−E0​a​sin⁡ξ​sin⁡ϕcosh⁡η−cos⁡ξ,\displaystyle\phi_{e}(\eta,\xi,\phi)=(\cosh\eta-\cos\xi)^{1/2}\sum_{n=1}^{\infty}C_{n}\cosh(\bar{n}\eta)\,P_{n}^{1}(\cos\xi)\sin\phi-\frac{E_{0}a\sin\xi\sin\phi}{\cosh\eta-\cos\xi},(85)

withn¯=n+1/2\bar{n}=n+1/2. The second term represents the externally applied field.

Using the identityPn1​(x)=(1−x2)1/2​dPn​(x)dx,Pn1​(cos⁡ξ)=sin⁡ξ​Pn′​(cos⁡ξ),\displaystyle P_{n}^{1}(x)=(1-x^{2})^{1/2}\,\derivative{P_{n}(x)}{x},\qquad P_{n}^{1}(\cos\xi)=\sin\xi\,P_{n}^{\prime}(\cos\xi),(86)

together with the standard bispherical expansion of(cosh⁡η−cos⁡ξ)−3/2(\cosh\eta-\cos\xi)^{-3/2}, the external-field contribution can be recast in the samePn1P_{n}^{1}basis. This leads to the compact representationϕe​(η,ξ,ϕ)=(cosh⁡η−cos⁡ξ)1/2​∑n=1∞[Cn​cosh⁡(n¯​η)−23/2​E0​a​e−n¯​η]​Pn1​(cos⁡ξ)​sin⁡ϕ.\displaystyle\phi_{e}(\eta,\xi,\phi)=(\cosh\eta-\cos\xi)^{1/2}\sum_{n=1}^{\infty}\left[C_{n}\cosh(\bar{n}\eta)-2^{3/2}E_{0}a\,e^{-\bar{n}\eta}\right]P_{n}^{1}(\cos\xi)\sin\phi.(87)

## B.2Interior potential and continuity of the potential

Inside the upper sphere (η>η0\eta>\eta_{0}), regularity asη→+∞\eta\to+\inftyrequires exponentially decaying modes. The interior potential is therefore expanded asϕ+​(η,ξ,ϕ)=(cosh⁡η−cos⁡ξ)1/2​∑n=1∞Dn​e−n¯​η​Pn1​(cos⁡ξ)​sin⁡ϕ.\displaystyle\phi_{+}(\eta,\xi,\phi)=(\cosh\eta-\cos\xi)^{1/2}\sum_{n=1}^{\infty}D_{n}e^{-\bar{n}\eta}P_{n}^{1}(\cos\xi)\sin\phi.(88)

Continuity of the electrostatic potential at the spherical interfaceη=η0\eta=\eta_{0}yields the algebraic relationDn​e−n¯​η0=Cn​cosh⁡(n¯​η0)−23/2​E0​a​e−n¯​η0,\displaystyle D_{n}e^{-\bar{n}\eta_{0}}=C_{n}\cosh(\bar{n}\eta_{0})-2^{3/2}E_{0}a\,e^{-\bar{n}\eta_{0}},(89)

which allows the interior coefficientsDnD_{n}to be eliminated in favor of the exterior onesCnC_{n}.

## B.3Continuity of the normal displacement and recurrence relation

The second boundary condition enforces continuity of the normal component of the electric displacement field,ϵi​∂ηϕ+​(η0,ξ,ϕ)=ϵe​∂ηϕe​(η0,ξ,ϕ).\displaystyle\epsilon_{i}\,\partial_{\eta}\phi_{+}(\eta_{0},\xi,\phi)=\epsilon_{e}\,\partial_{\eta}\phi_{e}(\eta_{0},\xi,\phi).(90)

Upon differentiation, the resulting expressions contain terms proportional toPn1​(cos⁡ξ)​sin⁡ϕP_{n}^{1}(\cos\xi)\sin\phias well as tocos⁡ξ​Pn1​(cos⁡ξ)​sin⁡ϕ\cos\xi\,P_{n}^{1}(\cos\xi)\sin\phi. The latter are reduced to thePn±11P_{n\pm 1}^{1}basis using the standard recurrence relations for associated Legendre functions.

After eliminatingDnD_{n}using Eq. (89) and equating coefficients of identical angular harmonics, one obtains a three-term recurrence relation for the coefficientsCnC_{n}. Introducing the dielectric contrastΔ=ϵi−ϵeϵi+ϵe,\displaystyle\Delta=\frac{\epsilon_{i}-\epsilon_{e}}{\epsilon_{i}+\epsilon_{e}},(91)

the final result can be written as(n−1)​(eη0+Δ​e−2​(n−1)​η0)​Cn−1+[Δ​sinh⁡η0−(2​n+1)​cosh⁡η0−n​Δ​e−2​n​η0−(n+1)​Δ​e−2​(n+1)​η0]​Cn\displaystyle(n-1)\Big(e^{\eta_{0}}+\Delta e^{-2(n-1)\eta_{0}}\Big)C_{n-1}+\Big[\Delta\sinh\eta_{0}-(2n+1)\cosh\eta_{0}-n\Delta e^{-2n\eta_{0}}-(n+1)\Delta e^{-2(n+1)\eta_{0}}\Big]C_{n}+(n+2)​(e−η0+Δ​e−2​(n+2)​η0)​Cn+1=e−2​η0−1.\displaystyle+(n+2)\Big(e^{-\eta_{0}}+\Delta e^{-2(n+2)\eta_{0}}\Big)C_{n+1}=e^{-2\eta_{0}}-1.(92)

## B.4Perturbative structure of the recurrence

For nonoverlapping spheres one hase−η0<1e^{-\eta_{0}}<1, while for physical dielectrics|Δ|<1|\Delta|<1. Inspection of Eq. (92) shows that terms coupling different multipoles are suppressed by factors ofΔ​e−2​n​η0\Delta e^{-2n\eta_{0}}. This motivates a perturbative expansion of the formCn=Cn(0)+Cn(1)+Cn(2)+⋯,\displaystyle C_{n}=C_{n}^{(0)}+C_{n}^{(1)}+C_{n}^{(2)}+\cdots,(93)

whereCn(k)=𝒪​((Δ​e−2​n​η0)k)C_{n}^{(k)}=\mathcal{O}((\Delta e^{-2n\eta_{0}})^{k}).

## B.5Zeroth-order solution

At leading order allΔ​e−2​n​η0\Delta e^{-2n\eta_{0}}terms are neglected, and the recurrence reduces to(n−1)​eη0​Cn−1(0)+[Δ​sinh⁡η0−(2​n+1)​cosh⁡η0]​Cn(0)+(n+2)​e−η0​Cn+1(0)=e−2​η0−1.\displaystyle(n-1)e^{\eta_{0}}C_{n-1}^{(0)}+\Big[\Delta\sinh\eta_{0}-(2n+1)\cosh\eta_{0}\Big]C_{n}^{(0)}+(n+2)e^{-\eta_{0}}C_{n+1}^{(0)}=e^{-2\eta_{0}}-1.(94)

Since the right-hand side is independent ofnn, a constant solutionCn(0)=C(0)C_{n}^{(0)}=C^{(0)}is sufficient, yieldingCn(0)=2Δ−3​e−η0.\displaystyle C_{n}^{(0)}=\frac{2}{\Delta-3}\,e^{-\eta_{0}}.(95)

## B.6First-order correction

At first order the recurrence becomes inhomogeneous, with a source determined entirely byCn(0)C_{n}^{(0)}. Guided by the structure of the suppressed terms, we adopt the ansatzCn(1)=Δ​e−2​n​η0​(α(1)+β(1)n)+𝒪​(e−6​η0).\displaystyle C_{n}^{(1)}=\Delta e^{-2n\eta_{0}}\left(\alpha^{(1)}+\frac{\beta^{(1)}}{n}\right)+\mathcal{O}(e^{-6\eta_{0}}).(96)

Matching the leading contributions innnyieldsα(1)=2​e−2​η03−Δ,\displaystyle\alpha^{(1)}=\frac{2e^{-2\eta_{0}}}{3-\Delta},(97)

while the subleading terms giveβ(1)=−Δ−13−Δ​e−4​η0+𝒪​(e−6​η0).\displaystyle\beta^{(1)}=-\frac{\Delta-1}{3-\Delta}e^{-4\eta_{0}}+\mathcal{O}(e^{-6\eta_{0}}).(98)

## B.7Second-order correction

The second-order recurrence is driven by the first-order solution. Using the same structural ansatz,Cn(2)=Δ​e−2​n​η0​(α(2)+β(2)n),\displaystyle C_{n}^{(2)}=\Delta e^{-2n\eta_{0}}\left(\alpha^{(2)}+\frac{\beta^{(2)}}{n}\right),(99)

one finds from the leading-order balanceα(2)=e−η0​α(1),\displaystyle\alpha^{(2)}=e^{-\eta_{0}}\alpha^{(1)},(100)

and from the subleading termsβ(2)=1−Δ3−Δ​e−5​η0+𝒪​(e−7​η0).\displaystyle\beta^{(2)}=\frac{1-\Delta}{3-\Delta}e^{-5\eta_{0}}+\mathcal{O}(e^{-7\eta_{0}}).(101)

The perturbative expansion converges rapidly for moderate separations (e−η0≪1e^{-\eta_{0}}\ll 1), and terms up to second order are sufficient for the construction of the axion-induced electromagnetic response discussed in the main text.

## Appendix CAxion-induced vector potential in the parallel configuration

In this appendix we provide the intermediate steps leading from the Green-function representation (24) to an explicit series expression for the first-order vector potential in the parallel configuration𝐄0=E0​𝐳^\mathbf{E}_{0}=E_{0}\hat{\mathbf{z}}. Throughout we assume two identical spheres with interfaces atη=±η0\eta=\pm\eta_{0}and a uniform axion parameterθ\thetainside each sphere (withθ=0\theta=0in the exterior medium). The generalization to two different interfacesη=η1>0\eta=\eta_{1}>0andη=η2<0\eta=\eta_{2}<0follows by the replacements indicated at the end of the appendix.

## C.1Reduction of the source to the interfaces

Since the zeroth-order solution is axisymmetric,ϕ(0)=ϕ(0)​(η,ξ)\phi^{(0)}=\phi^{(0)}(\eta,\xi)and∂ϕϕ(0)=0\partial_{\phi}\phi^{(0)}=0. Using the bispherical expression for∇θ\nabla\thetain Eq. (28) (withη1=η0\eta_{1}=\eta_{0}andη2=−η0\eta_{2}=-\eta_{0}) one finds that the source term in Ampère’s law is purely azimuthal,∇θ×∇ϕ(0)​(η,ξ)=−(cosh⁡η−cos⁡ξ)2a2​θ​ϕ^​[δ​(η−η0)+δ​(η+η0)]​∂ξϕ(0)​(η,ξ),\displaystyle\nabla\theta\times\nabla\phi^{(0)}(\eta,\xi)=-\frac{(\cosh\eta-\cos\xi)^{2}}{a^{2}}\,\theta\,\hat{\bm{\phi}}\,\big[\delta(\eta-\eta_{0})+\delta(\eta+\eta_{0})\big]\,\partial_{\xi}\phi^{(0)}(\eta,\xi),(102)

which is equivalent to Eq. (56). Therefore the first-order vector potential may be chosen as𝐀(1)​(η,ξ,ϕ)=Aϕ(1)​(η,ξ)​ϕ^,∂ϕAϕ(1)=0,\displaystyle\mathbf{A}^{(1)}(\eta,\xi,\phi)=A^{(1)}_{\phi}(\eta,\xi)\,\hat{\bm{\phi}},\qquad\partial_{\phi}A^{(1)}_{\phi}=0,(103)

and Eq. (24) reduces to the surface-supported integral𝐀(1)​(𝐫)=−α​θπ​∫d3​𝐫′​G0​(𝐫,𝐫′)​ϕ^′​a​sin⁡ξ′cosh⁡η′−cos⁡ξ′​[δ​(η′−η0)+δ​(η′+η0)]​∂ξ′ϕ(0)​(η′,ξ′).\displaystyle\mathbf{A}^{(1)}(\mathbf{r})=-\frac{\alpha\theta}{\pi}\int d^{3}\mathbf{r}^{\prime}\;G_{0}(\mathbf{r},\mathbf{r}^{\prime})\,\hat{\bm{\phi}}^{\prime}\,\frac{a\sin\xi^{\prime}}{\cosh\eta^{\prime}-\cos\xi^{\prime}}\,\big[\delta(\eta^{\prime}-\eta_{0})+\delta(\eta^{\prime}+\eta_{0})\big]\,\partial_{\xi^{\prime}}\phi^{(0)}(\eta^{\prime},\xi^{\prime}).(104)

Performing theη′\eta^{\prime}integration collapses the volume integral into the sum of two surface integrals over the angular variables(ξ′,ϕ′)(\xi^{\prime},\phi^{\prime})evaluated atη′=η0\eta^{\prime}=\eta_{0}andη′=−η0\eta^{\prime}=-\eta_{0}.

## C.2Derivative of the zeroth-order potential at the interfaces

For the parallel configuration the exterior potential is expanded as in the main text,ϕe(0)​(η,ξ)\displaystyle\phi^{(0)}_{e}(\eta,\xi)=(cosh⁡η−cos⁡ξ)1/2​∑n=0∞[An​sinh⁡(n¯​η)−23/2​E0​a​n¯​e−n¯​η]​Pn​(cos⁡ξ),n¯=n+12.\displaystyle=(\cosh\eta-\cos\xi)^{1/2}\sum_{n=0}^{\infty}\left[A_{n}\sinh(\bar{n}\eta)-2^{3/2}E_{0}a\,\bar{n}e^{-\bar{n}\eta}\right]P_{n}(\cos\xi),\qquad\bar{n}=n+\frac{1}{2}.(105)

Since∂ξPn​(cos⁡ξ)=−sin⁡ξ​Pn′​(cos⁡ξ)\partial_{\xi}P_{n}(\cos\xi)=-\sin\xi\,P_{n}^{\prime}(\cos\xi)andPn1​(cos⁡ξ)=sin⁡ξ​Pn′​(cos⁡ξ)P_{n}^{1}(\cos\xi)=\sin\xi\,P_{n}^{\prime}(\cos\xi), we have the useful identity∂ξPn​(cos⁡ξ)=−Pn1​(cos⁡ξ).\displaystyle\partial_{\xi}P_{n}(\cos\xi)=-P_{n}^{1}(\cos\xi).(106)

Differentiating Eq. (105) with respect toξ\xigives∂ξϕe(0)​(η,ξ)\displaystyle\partial_{\xi}\phi^{(0)}_{e}(\eta,\xi)=sin⁡ξ2​(cosh⁡η−cos⁡ξ)1/2​∑n=0∞[An​sinh⁡(n¯​η)−23/2​E0​a​n¯​e−n¯​η]​Pn​(cos⁡ξ)\displaystyle=\frac{\sin\xi}{2(\cosh\eta-\cos\xi)^{1/2}}\sum_{n=0}^{\infty}\left[A_{n}\sinh(\bar{n}\eta)-2^{3/2}E_{0}a\,\bar{n}e^{-\bar{n}\eta}\right]P_{n}(\cos\xi)−(cosh⁡η−cos⁡ξ)1/2​∑n=0∞[An​sinh⁡(n¯​η)−23/2​E0​a​n¯​e−n¯​η]​Pn1​(cos⁡ξ).\displaystyle\hskip 48.36958pt-(\cosh\eta-\cos\xi)^{1/2}\sum_{n=0}^{\infty}\left[A_{n}\sinh(\bar{n}\eta)-2^{3/2}E_{0}a\,\bar{n}e^{-\bar{n}\eta}\right]P_{n}^{1}(\cos\xi).(107)

Evaluating Eq. (107) at the interfacesη=±η0\eta=\pm\eta_{0}provides the explicit angular dependence entering the surface integrals in Eq. (104).

## C.3Bispherical expansion of the Green function and angular projection

We use the standard bispherical-harmonic expansion of the free-space Green functionG0​(𝐫,𝐫′)G_{0}(\mathbf{r},\mathbf{r}^{\prime}),G0​(𝐫,𝐫′)=(cosh⁡η−cos⁡ξ)1/2​(cosh⁡η′−cos⁡ξ′)1/2​∑l=0∞∑m=−llgl​(η,η′)​Ylm​(ξ,ϕ)​Ylm​(ξ′,ϕ′)∗,\displaystyle G_{0}(\mathbf{r},\mathbf{r}^{\prime})=(\cosh\eta-\cos\xi)^{1/2}(\cosh\eta^{\prime}-\cos\xi^{\prime})^{1/2}\sum_{l=0}^{\infty}\sum_{m=-l}^{l}g_{l}(\eta,\eta^{\prime})\,Y_{l}^{m}(\xi,\phi)\,Y_{l}^{m}(\xi^{\prime},\phi^{\prime})^{*},(108)

wheregl​(η,η′)=−12​n¯​a​e−n¯​|η−η′|g_{l}(\eta,\eta^{\prime})=-\frac{1}{2\bar{n}a}e^{-\bar{n}\absolutevalue{\eta-\eta^{\prime}}}is the radial kernel (symmetric in its arguments) andYlmY_{l}^{m}are the usual spherical harmonics on the(ξ,ϕ)(\xi,\phi)sphere. Substituting Eq. (108) into Eq. (104) yields𝐀(1)​(𝐫)\displaystyle\mathbf{A}^{(1)}(\mathbf{r})=−α​θπ​(cosh⁡η−cos⁡ξ)1/2​∑l=0∞∑m=−llYlm​(ξ,ϕ)​∫𝑑Ω′​ϕ^′​Ylm​(ξ′,ϕ′)∗​sin⁡ξ′​ℐ​(η′;ξ′)​[gl​(η,η0)−gl​(η,−η0)],\displaystyle=-\frac{\alpha\theta}{\pi}(\cosh\eta-\cos\xi)^{1/2}\sum_{l=0}^{\infty}\sum_{m=-l}^{l}Y_{l}^{m}(\xi,\phi)\int d\Omega^{\prime}\;\hat{\bm{\phi}}^{\prime}\,Y_{l}^{m}(\xi^{\prime},\phi^{\prime})^{*}\,\sin\xi^{\prime}\,\mathcal{I}(\eta^{\prime};\xi^{\prime})\Big[g_{l}(\eta,\eta_{0})-g_{l}(\eta,-\eta_{0})\Big],(109)

whered​Ω′=sin⁡ξ′​d​ξ′​d​ϕ′d\Omega^{\prime}=\sin\xi^{\prime}\,d\xi^{\prime}\,d\phi^{\prime}and we defined the interface combinationℐ​(η′;ξ′)≡acosh⁡η′−cos⁡ξ′​∂ξ′ϕ(0)​(η′,ξ′)|η′=±η0.\displaystyle\mathcal{I}(\eta^{\prime};\xi^{\prime})\equiv\left.\frac{a}{\cosh\eta^{\prime}-\cos\xi^{\prime}}\,\partial_{\xi^{\prime}}\phi^{(0)}(\eta^{\prime},\xi^{\prime})\right|_{\eta^{\prime}=\pm\eta_{0}}.(110)

The differencegl​(η,η0)−gl​(η,−η0)g_{l}(\eta,\eta_{0})-g_{l}(\eta,-\eta_{0})originates from the relative sign between the twoδ\delta-supported contributions in Eq. (104) and makes the odd parity with respect toη→−η\eta\to-\etamanifest.

Becauseϕ^′\hat{\bm{\phi}}^{\prime}carries an azimuthal dependence∝e±i​ϕ′\propto e^{\pm i\phi^{\prime}}, theϕ′\phi^{\prime}integral in Eq. (109) projects only them=±1m=\pm 1harmonics. Using the standard relationssin⁡ϕ′=ei​ϕ′−e−i​ϕ′2​i,cos⁡ϕ′=ei​ϕ′+e−i​ϕ′2,\displaystyle\sin\phi^{\prime}=\frac{e^{i\phi^{\prime}}-e^{-i\phi^{\prime}}}{2i},\qquad\cos\phi^{\prime}=\frac{e^{i\phi^{\prime}}+e^{-i\phi^{\prime}}}{2},(111)

and the explicitϕ′\phi^{\prime}dependence ofYlm​(ξ′,ϕ′)∝ei​m​ϕ′Y_{l}^{m}(\xi^{\prime},\phi^{\prime})\propto e^{im\phi^{\prime}}, one finds that all contributions withm≠±1m\neq\pm 1vanish by orthogonality. As a result,𝐀(1)\mathbf{A}^{(1)}is purely azimuthal and can be written as in Eq. (103).

## C.4Final series forAϕ(1)A^{(1)}_{\phi}

Collecting the survivingm=±1m=\pm 1contributions and using the relation betweenYl±1Y_{l}^{\pm 1}andPl1​(cos⁡ξ)P_{l}^{1}(\cos\xi), the angular projection yields a compact bispherical series of the formAϕ(1)​(η,ξ)=−α​θπ​(cosh⁡η−cos⁡ξ)1/2​∑n=0∞[An​sinh⁡(n¯​η0)−23/2​E0​a​n¯​e−n¯​η0]​[gn​(η,η0)−gn​(η,−η0)]​Pn1​(cos⁡ξ),\displaystyle A^{(1)}_{\phi}(\eta,\xi)=-\frac{\alpha\theta}{\pi}(\cosh\eta-\cos\xi)^{1/2}\sum_{n=0}^{\infty}\Big[A_{n}\sinh(\bar{n}\eta_{0})-2^{3/2}E_{0}a\,\bar{n}e^{-\bar{n}\eta_{0}}\Big]\,\Big[g_{n}(\eta,\eta_{0})-g_{n}(\eta,-\eta_{0})\Big]\,P_{n}^{1}(\cos\xi),(112)

where the kernel index has been relabeledl→nl\to nfor notational
consistency with the electrostatic expansion and we used the identity (106) to express the interfacial derivative in thePn1P_{n}^{1}basis. Equation (112) is the expression quoted in the main text, with the kernelgng_{n}inherited from the Green-function expansion (108). Further refinements (e.g. rewriting thesin⁡ξ​Pn\sin\xi\,P_{n}term in Eq. (107) asn±1n\pm 1combinations) are possible using standard Legendre identities; we do not pursue them here since Eq. (112) is already suitable for numerical evaluation onceAnA_{n}is known.

## C.5Induced magnetic field and streamline invariant

GivenAϕ(1)​(η,ξ)A^{(1)}_{\phi}(\eta,\xi), the first-order magnetic field follows from𝐁(1)=∇×𝐀(1)\mathbf{B}^{(1)}=\nabla\times\mathbf{A}^{(1)}. For an axisymmetric purely azimuthal potential, the curl in bispherical coordinates reduces to𝐁(1)=(cosh⁡η−cos⁡ξ)2a2​sin⁡ξ​[𝜼^​∂ξ−𝝃^​∂η]​(sin⁡ξcosh⁡η−cos⁡ξ​Aϕ(1)​(η,ξ)),\displaystyle\mathbf{B}^{(1)}=\frac{(\cosh\eta-\cos\xi)^{2}}{a^{2}\sin\xi}\Big[\hat{\bm{\eta}}\,\partial_{\xi}-\hat{\bm{\xi}}\,\partial_{\eta}\Big]\left(\frac{\sin\xi}{\cosh\eta-\cos\xi}\,A^{(1)}_{\phi}(\eta,\xi)\right),(113)

in agreement with the expression used in the main text. The field lines in the meridional(η,ξ)(\eta,\xi)plane satisfyd​ℓ×𝐁(1)=𝟎d\bm{\ell}\times\mathbf{B}^{(1)}=\mathbf{0}withd​ℓ=acosh⁡η−cos⁡ξ​(d​η​𝜼^+d​ξ​𝝃^)d\bm{\ell}=\frac{a}{\cosh\eta-\cos\xi}(d\eta\,\hat{\bm{\eta}}+d\xi\,\hat{\bm{\xi}}), yielding the streamline invariantsin⁡ξcosh⁡η−cos⁡ξ​Aϕ(1)​(η,ξ)=const.\displaystyle\frac{\sin\xi}{\cosh\eta-\cos\xi}\,A^{(1)}_{\phi}(\eta,\xi)=\mathrm{const.}(114)

Thus, the level sets of the scalar functionsin⁡ξcosh⁡η−cos⁡ξ​Aϕ(1)\frac{\sin\xi}{\cosh\eta-\cos\xi}A^{(1)}_{\phi}provide the axion-induced magnetic field lines around the spheres.

## C.6Generalization to two distinct spheres

If the spheres are not identical, their interfaces are located atη=η1>0\eta=\eta_{1}>0andη=η2<0\eta=\eta_{2}<0, and the axion jumps areΔ​θi=θm−θi\Delta\theta_{i}=\theta_{m}-\theta_{i}. In this case, Eqs. (102) and (104) generalize by the replacementθ​[δ​(η−η0)+δ​(η+η0)]⟶Δ​θ1​δ​(η−η1)+Δ​θ2​δ​(η−η2),\displaystyle\theta\big[\delta(\eta-\eta_{0})+\delta(\eta+\eta_{0})\big]\;\longrightarrow\;\Delta\theta_{1}\,\delta(\eta-\eta_{1})+\Delta\theta_{2}\,\delta(\eta-\eta_{2}),(115)

and Eq. (112) becomes the sum of two interface contributions,Aϕ(1)​(η,ξ)=−απ​(cosh⁡η−cos⁡ξ)1/2​∑n=0∞{Δ​θ1​𝒬n​(η1)​gn​(η,η1)+Δ​θ2​𝒬n​(η2)​gn​(η,η2)}​Pn1​(cos⁡ξ),\displaystyle A^{(1)}_{\phi}(\eta,\xi)=-\frac{\alpha}{\pi}(\cosh\eta-\cos\xi)^{1/2}\sum_{n=0}^{\infty}\Big\{\Delta\theta_{1}\,\mathcal{Q}_{n}(\eta_{1})\,g_{n}(\eta,\eta_{1})+\Delta\theta_{2}\,\mathcal{Q}_{n}(\eta_{2})\,g_{n}(\eta,\eta_{2})\Big\}\,P_{n}^{1}(\cos\xi),(116)

where𝒬n​(ηi)\mathcal{Q}_{n}(\eta_{i})denotes the interfacial combination of the zeroth-order coefficients evaluated atη=ηi\eta=\eta_{i}(the obvious analogue of the bracket in Eq. (112)).

## Appendix DAxion-induced vector potential in the perpendicular configuration

Here we present the detailed derivation of the axion-induced vector potential in the perpendicular configuration,𝐄0=E0​𝐲^\mathbf{E}_{0}=E_{0}\hat{\mathbf{y}}. The purpose is to make explicit the intermediate steps leading from the Green-function representation (24) to the series expressions for the Cartesian components of𝐀(1)\mathbf{A}^{(1)}quoted in the main text.

Throughout this appendix we use the distributional expression for∇θ\nabla\thetagiven in Eq. (28), and the zeroth-order electrostatic potentialϕ(0)\phi^{(0)}obtained in Sec.VI.

## D.1Structure of the axion-induced source

At first order in the axion coupling, the vector potential satisfies∇2𝐀(1)=−απ​∇θ×∇ϕ(0).\displaystyle\nabla^{2}\mathbf{A}^{(1)}=-\frac{\alpha}{\pi}\,\nabla\theta\times\nabla\phi^{(0)}.(117)

Using the bispherical-coordinate expression for the gradient operator and the fact that∇θ\nabla\thetais purely normal to the interfaces, the source term can be written as∇θ×∇ϕ(0)=−(cosh⁡η−cos⁡ξ)2a2​[δ​(η−η0)+δ​(η+η0)]​[ϕ^​∂ξ−𝝃^​1sinh⁡η​∂ϕ]​ϕ(0),\displaystyle\nabla\theta\times\nabla\phi^{(0)}=-\frac{(\cosh\eta-\cos\xi)^{2}}{a^{2}}\Big[\delta(\eta-\eta_{0})+\delta(\eta+\eta_{0})\Big]\Big[\hat{\bm{\phi}}\partial_{\xi}-\hat{\bm{\xi}}\frac{1}{\sinh\eta}\partial_{\phi}\Big]\phi^{(0)},(118)

whereϕ(0)​(η,ξ,ϕ)\phi^{(0)}(\eta,\xi,\phi)is the perpendicular zeroth-order potential expanded inPn1​(cos⁡ξ)​sin⁡ϕP_{n}^{1}(\cos\xi)\sin\phimodes.

Evaluating the derivatives atη=±η0\eta=\pm\eta_{0}yields[ϕ^​∂ξ−𝝃^​1sinh⁡η​∂ϕ]​ϕ(0)​(±η0,ξ,ϕ)\displaystyle\Big[\hat{\bm{\phi}}\partial_{\xi}-\hat{\bm{\xi}}\frac{1}{\sinh\eta}\partial_{\phi}\Big]\phi^{(0)}(\pm\eta_{0},\xi,\phi)=(cosh⁡η0−cos⁡ξ)−1/2​∑n=1∞[Cn​cosh⁡(n¯​η0)−23/2​E0​a​e−n¯​η0]\displaystyle=(\cosh\eta_{0}-\cos\xi)^{-1/2}\sum_{n=1}^{\infty}\Big[C_{n}\cosh(\bar{n}\eta_{0})-2^{3/2}E_{0}a\,e^{-\bar{n}\eta_{0}}\Big]×[ϕ^​(∂ξ+sin⁡ξ2​(cosh⁡η0−cos⁡ξ))−𝝃^​1sin⁡ξ​∂ϕ]​Pn1​(cos⁡ξ)​sin⁡ϕ.\displaystyle\quad\times\Big[\hat{\bm{\phi}}\Big(\partial_{\xi}+\frac{\sin\xi}{2(\cosh\eta_{0}-\cos\xi)}\Big)-\hat{\bm{\xi}}\frac{1}{\sin\xi}\partial_{\phi}\Big]P_{n}^{1}(\cos\xi)\sin\phi.(119)

## D.2Cartesian decomposition of the source

To facilitate the angular integrations, it is convenient to rewrite the
operator acting on the angular functions in terms of Cartesian components.
Using the explicit expressions of the bispherical basis vectors and
identifying the angular-momentum operators, one findsϕ^​∂ξ−(cos⁡ξ​cos⁡ϕ​𝐱^+cos⁡ξ​sin⁡ϕ​𝐲^)​1sin⁡ξ​∂ϕ=𝐱^​i​Lx+𝐲^​i​Ly,\displaystyle\hat{\bm{\phi}}\partial_{\xi}-(\cos\xi\cos\phi\,\hat{\mathbf{x}}+\cos\xi\sin\phi\,\hat{\mathbf{y}})\frac{1}{\sin\xi}\partial_{\phi}=\hat{\mathbf{x}}\,iL_{x}+\hat{\mathbf{y}}\,iL_{y},(120)

so that the full operator becomesϕ^​(∂ξ+sin⁡ξ2​(cosh⁡η0−cos⁡ξ))−𝝃^​1sin⁡ξ​∂ϕ=𝐱^​𝒪x+𝐲^​𝒪y+𝐳^​𝒪z,\displaystyle\hat{\bm{\phi}}\Big(\partial_{\xi}+\frac{\sin\xi}{2(\cosh\eta_{0}-\cos\xi)}\Big)-\hat{\bm{\xi}}\frac{1}{\sin\xi}\partial_{\phi}=\hat{\mathbf{x}}\mathcal{O}_{x}+\hat{\mathbf{y}}\mathcal{O}_{y}+\hat{\mathbf{z}}\mathcal{O}_{z},(121)

with explicit differential operators𝒪i\mathcal{O}_{i}acting on the angular
functions.

## D.3Green-function expansion and angular projections

Substituting Eq. (119) into the Green-function representation
(24), theη′\eta^{\prime}integration collapses onto the two spherical
interfaces. Expanding the Green’s function in spherical harmonics and usingi​Lx=i2​(L++L−),i​Ly=12​(L+−L−),L±​Ylm=(l∓m)​(l±m+1)​Ylm±1,\displaystyle iL_{x}=\frac{i}{2}(L_{+}+L_{-}),\qquad iL_{y}=\frac{1}{2}(L_{+}-L_{-}),\qquad L_{\pm}Y_{l}^{m}=\sqrt{(l\mp m)(l\pm m+1)}\,Y_{l}^{m\pm 1},(122)

together with the identitiesPn1​(cos⁡ξ)​sin⁡ϕ=−4​π​(n+1)!2​n¯​(n−1)!​i2​(Yn1+Yn−1),\displaystyle P_{n}^{1}(\cos\xi)\sin\phi=-\sqrt{\frac{4\pi(n+1)!}{2\bar{n}(n-1)!}}\frac{i}{2}\big(Y_{n}^{1}+Y_{n}^{-1}\big),(123)

the angular integrations can be performed explicitly by orthogonality of the
spherical harmonics.

As a result, the three Cartesian components of the vector potential are
obtained as convergent series,Ax(1)​(η,ξ,ϕ)\displaystyle A_{x}^{(1)}(\eta,\xi,\phi)=−α​θ2​π​∑n=0∞[Cn​cosh⁡(n¯​η0)−23/2​E0​a​e−n¯​η0]​[gn​(η,η0)+gn​(η,−η0)]​[Pn2​(cos⁡ξ)​cos⁡2​ϕ+n​(n+1)​Pn​(cos⁡ξ)]\displaystyle=-\frac{\alpha\theta}{2\pi}\sum_{n=0}^{\infty}\Big[C_{n}\cosh(\bar{n}\eta_{0})-2^{3/2}E_{0}a\,e^{-\bar{n}\eta_{0}}\Big]\Big[g_{n}(\eta,\eta_{0})+g_{n}(\eta,-\eta_{0})\Big]\Big[P_{n}^{2}(\cos\xi)\cos 2\phi+n(n+1)P_{n}(\cos\xi)\Big]+neighbor-mode contributions,\displaystyle\quad+\;\text{neighbor-mode contributions},(124)Ay(1)​(η,ξ,ϕ)\displaystyle A_{y}^{(1)}(\eta,\xi,\phi)=−α​θ2​π​∑n=0∞[Cn​cosh⁡(n¯​η0)−23/2​E0​a​e−n¯​η0]​[gn​(η,η0)+gn​(η,−η0)]​Pn2​(cos⁡ξ)​sin⁡2​ϕ\displaystyle=-\frac{\alpha\theta}{2\pi}\sum_{n=0}^{\infty}\Big[C_{n}\cosh(\bar{n}\eta_{0})-2^{3/2}E_{0}a\,e^{-\bar{n}\eta_{0}}\Big]\Big[g_{n}(\eta,\eta_{0})+g_{n}(\eta,-\eta_{0})\Big]P_{n}^{2}(\cos\xi)\sin 2\phi+neighbor-mode contributions,\displaystyle\quad+\;\text{neighbor-mode contributions},(125)Az(1)​(η,ξ)\displaystyle A_{z}^{(1)}(\eta,\xi)=−α​θ2​π​∑n=0∞4​n¯​[ϵe​sinh⁡(n¯​η0)+ϵi​cosh⁡(n¯​η0)ϵe−ϵi​Cn−23/2​E0​a​e−n¯​η0]​[gn​(η,η0)−gn​(η,−η0)]​Pn1​(cos⁡ξ).\displaystyle=-\frac{\alpha\theta}{2\pi}\sum_{n=0}^{\infty}4\bar{n}\Big[\frac{\epsilon_{e}\sinh(\bar{n}\eta_{0})+\epsilon_{i}\cosh(\bar{n}\eta_{0})}{\epsilon_{e}-\epsilon_{i}}\,C_{n}-2^{3/2}E_{0}a\,e^{-\bar{n}\eta_{0}}\Big]\Big[g_{n}(\eta,\eta_{0})-g_{n}(\eta,-\eta_{0})\Big]P_{n}^{1}(\cos\xi).(126)

Heregn​(η,η0)g_{n}(\eta,\eta_{0})denotes the radial Green-function kernel defined
in Sec.C.3.

## References
- [1]S. Banerjee, M. Levy, M. Davis, and B. Wilkerson(2017)Exact and approximate capacitance and force expressions for the electrostatic interaction between two equal-sized charged conducting spheres.IEEE Transactions on Industry Applications53(3),pp. 2455–2460.External Links:DocumentCited by:§I.
- [2]S. Batool and I. A. Qureshi(2022)Scattering of electromagnetic waves by two equal spherical particles.Optik249,pp. 168271.External Links:DocumentCited by:§I.
- [3]M. L. Brongersma, N. J. Halas, and P. Nordlander(2015)Plasmon-induced hot carrier science and technology.Nature Nanotechnology10,pp. 25–34.External Links:DocumentCited by:§I.
- [4]A. M. Cook and A. E. B. Nielsen(2023)Finite-size topology.Phys. Rev. B108,pp. 045144.External Links:DocumentCited by:§I.
- [5]I. N. Derbenev, A. V. Filippov, A. J. Stace, and E. Besley(2016-08)Electrostatic interactions between charged dielectric particles in an electrolyte solution.The Journal of Chemical Physics145(8),pp. 084103.External Links:ISSN 0021-9606,Document,LinkCited by:§I.
- [6]A. M. Essin, J. E. Moore, and D. Vanderbilt(2009)Magnetoelectric polarizability and axion electrodynamics in crystalline insulators.Phys. Rev. Lett.102,pp. 146805.External Links:DocumentCited by:§I,§II,§II.
- [7]L. Fu, C. L. Kane, and E. J. Mele(2007)Topological insulators in three dimensions.Phys. Rev. Lett.98,pp. 106803.External Links:DocumentCited by:§I.
- [8]M. Governale, B. B. Bhandari, F. Taddei, K. Imura, and U. Zülicke(2020)Finite-size effects in cylindrical topological insulators.New J. Phys.22,pp. 063055.External Links:DocumentCited by:§I.
- [9]A. Goyette and A. Navon(1976-05)Two dielectric spheres in an electric field.Phys. Rev. B13,pp. 4320–4327.External Links:Document,LinkCited by:§I.
- [10]A. G. Grushin and A. Cortijo(2011-01)Tunable Casimir repulsion with three-dimensional topological insulators.Phys. Rev. Lett.106,pp. 020403.External Links:Document,LinkCited by:§I.
- [11]A. G. Grushin, P. Rodriguez-Lopez, and A. Cortijo(2011-07)Effect of finite temperature and uniaxial anisotropy on the Casimir effect with three-dimensional topological insulators.Phys. Rev. B84,pp. 045119.External Links:Document,LinkCited by:§I.
- [12]M. Z. Hasan and C. L. Kane(2010)Colloquium: topological insulators.Rev. Mod. Phys.82,pp. 3045–3067.External Links:DocumentCited by:§I.
- [13]S. Hudlet, M. Saint Jean, C. Guthmann, and J. Berger(1998)Evaluation of the capacitive force between an atomic force microscopy tip and a metallic surface.The European Physical Journal B2(1),pp. 5–10.External Links:DocumentCited by:§I.
- [14]J. D. Jackson(1998)Classical electrodynamics.3 edition,Wiley,New York.Cited by:§I.
- [15]A. Karch(2009-10)Electric-magnetic duality and topological insulators.Phys. Rev. Lett.103,pp. 171601.External Links:Document,LinkCited by:§I.
- [16]A. Khachatourian, H. Chan, A. J. Stace, and E. Bichoutskaia(2014-02)Electrostatic force between a charged sphere and a planar surface: a general solution for dielectric materials.The Journal of Chemical Physics140(7),pp. 074107.External Links:ISSN 0021-9606,Document,LinkCited by:§I.
- [17]J. Lekner(2012-05)Electrostatics of two charged conducting spheres.Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences468(2145),pp. 2829–2848.External Links:ISSN 1364-5021,Document,LinkCited by:§I.
- [18]S. Levine and G. Olaofe(1968)Scattering of electromagnetic waves by two equal spherical particles.Journal of Colloid and Interface Science27(3),pp. 442–457.External Links:ISSN 0021-9797,Document,LinkCited by:§I.
- [19]A. Malashevich, I. Souza, S. Coh, and D. Vanderbilt(2010-05)Theory of orbital magnetoelectric response.New Journal of Physics12(5),pp. 053032.External Links:Document,LinkCited by:§I.
- [20]V. A. Markel(2016)Introduction to the Maxwell Garnett approximation: tutorial.Journal of the Optical Society of America A33,pp. 1244–1256.External Links:DocumentCited by:§I.
- [21]V.A. Markel(1993)Coupled-dipole approach to scattering of light from a one-dimensional periodic dipole structure.Journal of Modern Optics40(11),pp. 2281–2291.External Links:Document,LinkCited by:§I.
- [22]A. Martín-Ruiz, M. Cambiaso, and L. F. Urrutia(2015-12)Green’s function approach to Chern-Simons extended electrodynamics: an effective theory describing topological insulators.Phys. Rev. D92,pp. 125015.External Links:Document,LinkCited by:§I,§II.
- [23]A. Martín-Ruiz, M. Cambiaso, and L. F. Urrutia(2016-10)Electromagnetic description of three-dimensional time-reversal invariant ponderable topological insulators.Phys. Rev. D94,pp. 085019.External Links:Document,LinkCited by:§II.
- [24]A. Martín-Ruiz, O. Rodríguez-Tzompantzi, J. R. Maze, and L. F. Urrutia(2019-10)Magnetoelectric effect of a conducting sphere near a planar topological insulator.Phys. Rev. A100,pp. 042124.External Links:Document,LinkCited by:§I.
- [25]P. Moon and D. E. Spencer(1961)Field theory handbook.Springer,Berlin.External Links:ISBN 978-3-642-45858-7Cited by:§IV.1.
- [26]J. E. Moore and L. Balents(2007)Topological invariants of time-reversal-invariant band structures.Phys. Rev. B75,pp. 121306.External Links:DocumentCited by:§I.
- [27]P. M. Morse and H. Feshbach(1953)Methods of theoretical physics.McGraw-Hill,New York.Cited by:§I.
- [28]P. M. Morse and H. Feshbach(1953)Methods of theoretical physics.Vol.2,McGraw-Hill,New York.Cited by:§IV.1.
- [29]M. Okamoto, Y. Takane, and K. Imura(2014)One-dimensional topological insulator: a model for studying finite-size effects in topological insulator thin films.Phys. Rev. B89,pp. 125425.External Links:DocumentCited by:§I.
- [30]J. B. Pendry(2000)Negative refraction makes a perfect lens.Phys. Rev. Lett.85,pp. 3966–3969.External Links:DocumentCited by:§I.
- [31]E. Prodan and P. Nordlander(2004-03)Plasmon hybridization in spherical nanoparticles.The Journal of Chemical Physics120(11),pp. 5444–5454.External Links:Document,ISSN 0021-9606,LinkCited by:§I.
- [32]E. Prodan and P. Nordlander(2004)Plasmon hybridization in spherical nanoparticles.J. Chem. Phys.120,pp. 5444–5454.External Links:DocumentCited by:§I.
- [33]X.-L. Qi, T. L. Hughes, and S.-C. Zhang(2008)Topological field theory of time-reversal invariant insulators.Phys. Rev. B78,pp. 195424.External Links:DocumentCited by:§I,§II,§II.
- [34]X.-L. Qi, R. Li, J. Zang, and S.-C. Zhang(2009)Inducing a magnetic monopole with topological surface states.Science323,pp. 1184–1187.External Links:DocumentCited by:§I.
- [35]X.-L. Qi and S.-C. Zhang(2011)Topological insulators and superconductors.Rev. Mod. Phys.83,pp. 1057–1110.External Links:DocumentCited by:§I.
- [36]R. Roy(2009)Topological phases and the quantum spin Hall effect in three dimensions.Phys. Rev. B79,pp. 195322.External Links:DocumentCited by:§I.
- [37]A. Scaramucci, E. Bousquet, M. Fechner, M. Mostovoy, and N. A. Spaldin(2012-11)Linear magnetoelectric effect by orbital magnetism.Phys. Rev. Lett.109,pp. 197203.External Links:Document,LinkCited by:§I.
- [38]V. M. Shalaev(2007)Optical negative-index metamaterials.Nature Photonics1(1),pp. 41–48.External Links:Document,ISBN 1749-4893,LinkCited by:§I.
- [39]N. A. Spaldin, M. Fiebig, and M. Mostovoy(2008-10)The toroidal moment in condensed-matter physics and its relation to the magnetoelectric effect.Journal of Physics: Condensed Matter20(43),pp. 434203.External Links:Document,LinkCited by:§I.
- [40]R. D. Stoy(1989-11)Solution procedure for the Laplace equation in bispherical coordinates for two spheres in a uniform external field: perpendicular orientation.Journal of Applied Physics66(10),pp. 5093–5095.External Links:ISSN 0021-8979,Document,LinkCited by:§I.
- [41]D. J. Thouless, M. Kohmoto, M. P. Nightingale, and M. den Nijs(1982)Quantized Hall conductance in a two-dimensional periodic potential.Phys. Rev. Lett.49,pp. 405–408.External Links:DocumentCited by:§I.

## 


- 


Major funding support from
