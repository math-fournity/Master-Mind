# Fractal geometry-governed oxygen diffusion: Tumors vs. Normal Tissues

**arXiv ID**: 2604.15478v1
**Authors**: Neda Valizadeh, Robabeh Rahimi, Ramin Abolfath
**Published**: 2026-04-16
**Categories**: physics.med-ph, cond-mat.dis-nn, nlin.PS, physics.bio-ph, physics.comp-ph
**HTML URL**: https://arxiv.org/html/2604.15478v1

## Abstract

{\bf Purpose}: To develop a geometry-governed diffusion framework that explains differential tissue response under FLASH ultra-high dose rate (UHDR) irradiation by explicitly accounting for structural heterogeneity and anomalous transport in biological tissues. {\bf Methods}: We formulate a generalized diffusion--reaction model on fractal substrates to describe molecular transport in heterogeneous media. Tissue architecture is characterized by a fractal (Hausdorff) dimension \(D\), while scale-dependent transport inefficiency and memory effects are captured by a fractional parameter \(θ\). Analytical solutions for radially symmetric geometries are derived and compared with classical normal (Euclidean) diffusion and a Gaussian reference model under identical physical conditions. Transport behavior is quantified through transient probability distributions and steady-state spatial profiles. {\bf Results}: The model reveals systematic suppression of long-range transport and enhanced localization as tissue structural complexity increases. Increasing \(θ\) leads to subdiffusive dynamics, reduced effective diffusion lengths, and persistent non-Gaussian concentration profiles, even in the steady state. While increasing \(D\) alone enhances spatial accessibility, fractional dynamics dominate transport behavior when \(θ>0\), counteracting geometric connectivity. These effects produce a separation between regimes characterized by efficient inter-track overlap and rapid homogenization, and regimes marked by isolated, long-lived reactive domains.

## Full Text

Fractal geometry-governed oxygen diffusion: Tumors vs. Normal Tissues

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
- License: CC BY 4.0arXiv:2604.15478v1 [physics.med-ph] 16 Apr 2026

## Fractal geometry-governed oxygen diffusion: Tumors vs. Normal
TissuesN. Valizadehvalizadeh.neda1204@gmail.comDepartment of Physics, University of Mohaghegh Ardabili, P.O. Box 179, Ardabil, IranR. Rahimirrahimi@som.umaryland.eduUniversity of Maryland School of Medicine, MD, United States of AmericaRamin Abolfathramin1.abolfath@gmail.comDepartment of Physics and Astronomy, Howard University, Washington, DC 20059, United States of America

## Abstract

Purpose:
To develop a geometry-governed diffusion framework that explains differential tissue response under FLASH ultra-high dose rate (UHDR) irradiation by explicitly accounting for structural heterogeneity and anomalous transport in biological tissues.

Methods:
We formulate a generalized diffusion–reaction model on fractal substrates to describe molecular transport in heterogeneous media. Tissue architecture is characterized by a fractal (Hausdorff) dimensionDD, while scale-dependent transport inefficiency and memory effects are captured by a fractional parameterθ\theta. Analytical solutions for radially symmetric geometries are derived and compared with classical normal (Euclidean) diffusion and a Gaussian reference model under identical physical conditions. Transport behavior is quantified through transient probability distributions and steady-state spatial profiles.

Results:
The model reveals systematic suppression of long-range transport and enhanced localization as tissue structural complexity increases. Increasingθ\thetaleads to subdiffusive dynamics, reduced effective diffusion lengths, and persistent non-Gaussian concentration profiles, even in the steady state. While increasingDDalone enhances spatial accessibility, fractional dynamics dominate transport behavior whenθ>0\theta>0, counteracting geometric connectivity. These effects produce a separation between regimes characterized by efficient inter-track overlap and rapid homogenization, and regimes marked by isolated, long-lived reactive domains.

Conclusions:
Fractal geometry provides a unifying physical framework for understanding tissue-dependent transport and differential response under FLASH UHDR irradiation. Normal tissues, characterized by near-Euclidean geometry and weak anomalous effects, permit greater inter-track interaction and recombination, whereas tumor-like tissues with elevated structural complexity exhibit localized transport and reduced collective chemical reactivity. This proof-of-principle study establishes tissue architecture as a fundamental determinant of transport efficiency and offers a mechanistic basis for experimentally observed FLASH tissue sparing, motivating geometry-aware modeling of radiobiological response.FLASH radiotherapy, anomalous diffusion, fractal geometry, reaction–diffusion, tissue heterogeneity

## IIntroduction

Diffusion in biological systems is rarely simple or uniform. Classical Fickian diffusion, formulated for homogeneous Euclidean continua, assumes a linear growth of mean-square displacement of ions with time,⟨r2​(t)⟩∝t\langle r^{2}(t)\rangle\propto t, reflecting homogeneous diffusivity and/or ionic conductivity that relies on translational and rotational invariance of the Brownian motion in the medium. Yet, most natural and biological media are neither homogeneous nor Euclidean; rather, they are structurally complex, hierarchically organized, and dynamically heterogeneous, often exhibiting self-similar (fractal) features across spatial scales. In such environments, diffusion deviates from uniform behavior and becomesanomalous—typically subdiffusive—following power-law scaling of the form⟨r2​(t)⟩∝t22+θ,with​θ>0,\langle r^{2}(t)\rangle\propto t^{\frac{2}{2+\theta}},\quad\text{with }\theta>0,(1)

where the exponentθ\thetaencodes the degree of geometric constraint, connectivity loss, and structural disorder of the medium. These anomalous transport patterns arise when the underlying structure itself possesses fractal geometry—characterized by a non-integer Hausdorff (fractal) dimensionDDand associated spectral or walk dimensions that govern scaling of transport processes[1,2,3,4].
With a constantθ\theta(includingθ=0\theta=0), a decrease inDDfrom the Euclidean dimensionddeffectively reduces the global transport efficiency, reflecting increased geometric constraints and reduced connectivity of diffusion pathways.
In these settings, diffusion is intrinsically non-Fickian: particle spreading depends not on a constant transport coefficient but on the topology, tortuosity, and percolation properties of the medium[5,6].

Biological tissues constitute archetypal fractal media. Cellular organization, extracellular matrix (ECM), and vasculature together form anisotropic, disordered, and multiscale networks whose geometry critically shapes transport phenomena[7,8,9]. Tumor tissues, in particular, show a prominent architectural irregularity. Its microvasculature is chaotically branched and spatially heterogeneous, exhibiting fractal dimensions in the rangeD≈2.1D\approx 2.1–2.82.8, depending on the imaging modality and scale[10,11]. This irregularity compromises both perfusion and diffusion, producing patchy oxygenation patterns and persistent hypoxic niches that cannot be captured by classical continuum diffusion models[12,13]. High-resolution oxygen-tension mapping further reveals sharp spatial fluctuations inpO2\mathrm{pO_{2}}distributions, with hypoxic and normoxic regions coexisting within micrometer distances[13,14]. As tumor size increases, oxygen gradients flatten while remaining uniformly low, indicating chronic diffusion-limited hypoxia in contrast to the Krogh-type continuum transport assumptions[12]. The fractal dimension of the vascular or oxygen maps therefore provides a quantitative measure of the inefficiency of tissue space-filling and serves as a predictor of severity of hypoxia and resistance to treatment[15,8,16].

Fractal geometry likewise governs molecular transport and drug delivery within tumors. The ECM constitutes a disordered porous network that induces anomalous—often subdiffusive—propagation of therapeutic agents[17,18]. Computational and experimental studies demonstrate that densely yet chaotically vascularized tumors rapidly drain injected drugs, leading to poor intratumoral retention and spatially heterogeneous exposure[19,20]. Strategies such as transient vessel normalization effectively reduce the geometric complexity of perfusion networks, thereby improving the uniformity of drug penetration and therapeutic efficacy[21,22]. Thus, geometry governs a fundamental determinant of transport efficiency, linking multiscale structural disorder to pharmacokinetic failure.

Beyond vascular and extracellular transport, experimental evidence indicates that membrane-scale heterogeneity further modulates diffusion-controlled processes in cancer. Viscosity-sensitive fluorescent probes and nanoparticle-based sensors reveal that tumor cell membranes exhibit altered lipid packing, spatially heterogeneous nanoviscosity, and markedly different viscoelastic properties relative to normal cells[23,24]. These membrane-level changes enhance lateral diffusion of lipids and reactive intermediates within the membrane plane and modify reaction–diffusion coupling at subcellular scales, directly impacting radical recombination kinetics under irradiation[25,26]. Complementary biochemical analyses further demonstrate that cancer cells actively reprogram lipid composition—enriching polyunsaturated fatty acids and altering saturation profiles—to regulate susceptibility to oxidative damage and ferroptosis[27]. Together, these are indications that membrane organization constitutes an additional fractal-like layer of transport heterogeneity. Scale-aware diffusion models that extend beyond homogeneous cytosolic or tissue-level assumptions is to be employed to explain the process.

Geometry also modulates radiobiological responses. The discovery of theFLASHradiotherapy effect—characterized by remarkable normal-tissue sparing under ultra-high dose rate (UHDR>40​Gy/s>40\,\mathrm{Gy/s}) irradiation—has challenged traditional radiochemistry-based paradigms[28,29]. While oxygen depletion and radical recombination kinetics have been proposed as principal mechanisms[30,31,32,33,34,35], emerging evidence indicates spatial topology and diffusion-channel connectivity are equally decisive.Abolfath et al. [36]employed a stochastic reaction-diffusion model to simulate radiation-induced reactive oxygen species (ROS) transport in disordered geometries, showing that tissue-like media facilitate extensive inter-track recombination, leading to oxygen depletion and reduced damage (the FLASH-sparing effect). In contrast, fractal-like tumor architectures restrict ROS percolation, isolating reactive clusters and thereby preserving oxidative injury while abolishing sparing. Recently,Guo et al. [37]developed a uniform oxygen diffusion-reaction model that accounts for the oxygen depletion as a function of dose rate, arguing transient diffusion bottlenecks may accentuate tissue-type–specific dose-rate responses. In contrast, we incorporated geometry-governed localization effects that may bridge microscopic structural organization with macroscopic radiobiological outcomes to explain differential tissue response at UHDR.

In a nutshell, intertrack recombination of reactive species (RS) emerges if the particles constituting a therapeutic beam enter tissues within short spatial and temporal intervals (<0.1​μ​m<0.1\mu m, and<1​μ​s<1\mu s). Under such conditions, the biological response of cells and tissues may exhibit sensitivity to dose rate, leading to lower reactivity rates to biomolecules such as lipids and DNA, simply because RS react with each other prior to reacting with biomolecules. This mutually inclusive condition can be broken down if the cellular blockage of the transport channels among the tracks prevents inter-track diffusion of RS. Thus, the reaction to tissue can only be described by means of an intra-track mechanisms, as the reactivity among RS and biomolecules would be dominant within independent and uncorrelated tracks. The time-lag among the tracks becomes an irrelevant parameter, and the biological response of cells and tissues shows insensitivity to radiation dose rate. Thus, the diffusibility of RS in tissues may strongly influence the differential tissue responses to radiation dose rate, i.e., FLASH-UHDR vs. conventional dose rate (CDR).

Importantly, the transition from independent to interacting radiation tracks defines a regime in which transport properties become functionally relevant. Under CDRs, temporal separation between tracks limits the coexistence of RS clouds, and inter-track interactions are therefore suppressed. In contrast, under FLASH-UHDR irradiation, the high density of tracks exposes a regime in which simultaneous multi-track transport enables overlap, and geometry-governed diffusion becomes a controlling factor in radiochemical outcomes.

Collectively, these studies demonstrate that geometry and topology are fundamental determinants of therapeutic transport, as crucial as local biochemistry or kinetic processes. The diffusion field—the tissue itself—acts as an active modulator of oxygen, drug, and ionic/radical dynamics. Nevertheless, the prevailing radiobiological and pharmacokinetic models often assume homogeneous diffusivity and continuous concentration fields, limiting their predictive precision in realistic tissues[36].

To address this limitation, we develop a generalized diffusion framework grounded in fractal geometry, in which transport coefficients are intrinsically scale-dependent and reflect the underlying tissue morphology. A central feature of this framework is the introduction of a scaling exponent,θ\theta, that quantifies the degree of geometric complexity and anisotropy within the medium. This leads to a position-dependent RS diffusivity and/or ionic (electrical) conductivityσ​(r)∝r−θ,\sigma(r)\propto r^{-\theta},(2)

governing transitions from Euclidean to fractal transport regimes. The framework recovers classical Fickian diffusion in the limitθ→0\theta\to 0where diffusivity and/or conductivity are uniformly constant (due to underlying translational symmetry), but yields anomalous (nonlinear) transport in structurally disordered domains where the RS diffusivity and/or electrical conductivity depend on the initial position of ions, with broken translational invariance.

By defining an effectivefractal conductivity, we establish a quantitative link between microstructural disorder and macroscopic transport efficiency, allowing us to compare tissue architectures in terms of their diffusive impedance. Analytical solutions for spherical and cylindrical geometries—representative of tumor nodules and localized drug depots—illustrate how fractal geometry modulates oxygen delivery, drug penetration, and radical transport.

In the following sections, we formalize the fractal diffusion equations and derive their scaling relations, analyze representative solutions under biologically relevant geometries, and discuss implications for oxygen depletion and tissue sparing inFLASHradiotherapy. This structure provides both a mechanistic foundation and a pathway toward geometry-aware predictive modeling of the therapeutic response.

## IIMethods

To investigate the role of tissue geometry and structural disorder in molecular transport, we systematically compared three distinct diffusion descriptions:
(i) generalized fractal diffusion,
(ii) classical normal (Euclidean) diffusion, and
(iii) a Gaussian reference model.

All three models are evaluated under identical physical and geometrical conditions to isolate the effects of fractal dimensionality and anomalous transport from purely kinetic or chemical influences. This comparative framework allows us to elucidate how structural complexity, encoded through the fractal dimensionDDand the scaling exponentθ\theta, modifies both transient and steady-state diffusion behavior relative to classical Fickian theory.

The formulation is intentionally minimal and geometry-driven, enabling direct interpretation of transport behavior in heterogeneous biological tissues without introducing additional phenomenological assumptions.

## II.1Generalized fractal diffusion model

Transport in heterogeneous biological tissues, embedded in Euclidean space with dimensionddis governed not only by local diffusivity but also by the geometry and connectivity of accessible pathways. In complex media such as tumors, diffusion pathways are tortuous, partially disconnected, and hierarchically organized, leading to deviations from classical Gaussian transport. To capture these effects, we model diffusion on a fractal substrate characterized by two independent indices of (1) a Hausdorff (fractal) dimensionDDand (2) a scaling exponentθ\thetathat quantifies geometric resistance and anomalous transport.

The normalized radial probability density (distribution function),P​(r,t)P(r,t), satisfies the generalized diffusion–reaction equation∂P​(r,t)∂t=1rD−1​∂∂r​[k​rD−1−θ​∂P​(r,t)∂r]−μ​P​(r,t),\frac{\partial P(r,t)}{\partial t}=\frac{1}{r^{D-1}}\frac{\partial}{\partial r}\left[k\,r^{D-1-\theta}\frac{\partial P(r,t)}{\partial r}\right]-\mu\,P(r,t),(3)

wherekkis the homogeneous microscopic transport coefficient andμ\murepresents an effective reaction or decay rate.
The factorrD−1−θr^{D-1-\theta}introduces a scale-dependent reduction of diffusive flux, reflecting tortuosity and partial disconnection of transport pathways in fractal media.

Atμ=0\mu=0, the probability density is normalized according to the fractal measure1\displaystyle 1=\displaystyle=∫𝑑Ω^​∫0∞PΩ^​(r,t)​rD−1​𝑑r\displaystyle\int d\hat{\Omega}\int_{0}^{\infty}P_{\hat{\Omega}}(r,t)\,r^{D-1}\,dr(4)=\displaystyle=∫0∞P​(r,t)​rD−1​𝑑r,\displaystyle\int_{0}^{\infty}P(r,t)\,r^{D-1}\,dr,

which ensures conservation of probability within a domain of non-integer (fractional) dimensionality.Ω^\hat{\Omega}is the solid angle.
In Eq. (4),P​(r,t)P(r,t)is an angular independent PDF, hence the normalization factors stemming from the integration overΩ^\hat{\Omega}have been absorbed inP​(r,t)P(r,t).

In the limitθ=0\theta=0, Eq. (3) reduces to diffusion on a purely fractal geometry. Forθ>0\theta>0, additional geometric resistance and memory effects emerge, leading to anomalous (subdiffusive) transport.

## II.2Normal (Euclidean) diffusion

Normal diffusion refers to Fickian transport characterized by a linear growth of the mean-squared displacement with time,⟨r2​(t)⟩∝t\langle r^{2}(t)\rangle\propto t.
It is recovered in the Euclidean limit withD=dD=dandθ=0\theta=0, for which Eq. (3) reduces to∂P​(r,t)∂t=k​[1rd−1​∂∂r​(rd−1​∂P​(r,t)∂r)]−μ​P​(r,t).\frac{\partial P(r,t)}{\partial t}=k\left[\frac{1}{r^{d-1}}\frac{\partial}{\partial r}\left(r^{d-1}\frac{\partial P(r,t)}{\partial r}\right)\right]-\mu\,P(r,t).(5)

This equation describes diffusion in a homogeneous spherical or cylindrical geometry, corresponding tod=3d=3or 2, respectively. It serves as an appropriate reference model for transport in normal tissues, where extracellular spaces and intracellular environments are relatively uniform and well connected. In this regime, diffusion pathways are minimally constrained, and transport is well approximated by Fickian dynamics. The details of the numerical solution of the normal diffusion are given in AppendixA.

## II.3Gaussian reference model

For comparison, we also include a Gaussian as a reference distribution. Note that Gaussian distribution is a solution of normal diffusion for a specific boundary condition such that att=0t=0,P​(r,t)=δ​(r)P(r,t)=\delta(r)and atr=∞r=\inftyand finitett,P​(r,t)=0P(r,t)=0. DenotingPG,d​(r,t)=1𝒩d​(t)​exp⁡[−r24​k​t],P_{\mathrm{G},d}(r,t)=\frac{1}{\mathcal{N}_{d}(t)}\exp\!\left[-\frac{r^{2}}{4kt}\right],(6)

where𝒩d​(t)=2Γ​(d/2)​[14​k​t]d/2\mathcal{N}_{d}(t)=\frac{2}{\Gamma(d/2)}\left[\frac{1}{4kt}\right]^{d/2}ensures normalization. Hereddis the Euclidean dimension.Γ​(n)=(n−1)!\Gamma(n)=(n-1)!,
for integernn, andΓ​(n+12)=(n−12n)​n!​π\Gamma\left(n+\frac{1}{2}\right)=\binom{n-\frac{1}{2}}{n}n!\sqrt{\pi}.

Considering this boundary condition, forθ>0\theta>0andD≠dD\neq d, we find a non-Gaussian distribution function as a solution of Eq. (3)P​(r,t)=\displaystyle P(r,t)=2+θΓ​(D/(2+θ))​[1k​(2+θ)2​t]D/(2+θ)\displaystyle\frac{2+\theta}{\Gamma(D/(2+\theta))}\left[\frac{1}{k(2+\theta)^{2}t}\right]^{D/(2+\theta)}×\displaystyle\timesexp⁡[−r2+θk​(2+θ)2​t].\displaystyle\exp\left[-\frac{r^{2+\theta}}{k(2+\theta)^{2}t}\right].(7)

Atθ=0\theta=0the diffusion length follows the Einstein’s relation,⟨r2⟩∝t\langle r^{2}\rangle\propto t. However, forD≠dD\neq d, the normalization ofPG,D​(r,t)=exp⁡(−r2/4​k​t)/𝒩D​(t)P_{G,D}(r,t)=\exp(-r^{2}/4kt)/\mathcal{N}_{D}(t)results in𝒩D​(t)=2Γ​(D/2)​[14​k​t]D/2\mathcal{N}_{D}(t)=\frac{2}{\Gamma(D/2)}\left[\frac{1}{4kt}\right]^{D/2}whereΓ​(z)=∫0∞tz−1​e−t​𝑑t\Gamma(z)=\int_{0}^{\infty}t^{z-1}e^{-t}\,dt.
As the amplitude ofPG​(r,t)P_{G}(r,t)decreases with increasingDD, one can findPG,D<PG,dP_{G,D}<P_{G,d}forD>dD>d.
From this PDF, it is straightforward to show⟨r2​(t)⟩\displaystyle\langle r^{2}(t)\rangle=\displaystyle=∫0∞𝑑r​rD−1​r2​P​(r,t)\displaystyle\int_{0}^{\infty}drr^{D-1}r^{2}P(r,t)=\displaystyle=Γ​(D+22+θ)Γ​(D2+θ)​[k​(2+θ)2​t]2/(2+θ)∼t2/(2+θ).\displaystyle\frac{\Gamma\left(\frac{D+2}{2+\theta}\right)}{\Gamma\left(\frac{D}{2+\theta}\right)}\left[k(2+\theta)^{2}t\right]^{2/(2+\theta)}\sim t^{2/(2+\theta)}.

The exponentθ\thetaprovides a quantitative and physically transparent measure of deviation from Fickian transport and serves as a key control parameter linking tissue microstructure to macroscopic transport behavior.
To quantify transport behavior across models, we analyze the mean-square displacement (MSD), which follows the scaling as in Eq. (LABEL:eq8).
In the limit ofθ=0\theta=0, Eq.(LABEL:eq8) leads to⟨r2​(t)⟩=Γ​(D/2+1)/Γ​(D/2)​4​k​t\langle r^{2}(t)\rangle=\Gamma(D/2+1)/\Gamma(D/2)4kt, thusk→Γ​(D/2+1)/Γ​(D/2)​kk\rightarrow\Gamma(D/2+1)/\Gamma(D/2)k, globally, with normal diffusion and the growth exponent, 1/2.
Similarly, forD=dD=d, Eq.(LABEL:eq8) yields correctly2​k​t2ktfor each degree of freedom.
See Fig.1.
ForD=d=2D=d=2,⟨r2​(t)⟩=⟨x2​(t)⟩+⟨y2​(t)⟩\langle r^{2}(t)\rangle=\langle x^{2}(t)\rangle+\langle y^{2}(t)\rangle, andΓ​(D/2+1)/Γ​(D/2)=Γ​(2)/Γ​(1)=1\Gamma(D/2+1)/\Gamma(D/2)=\Gamma(2)/\Gamma(1)=1thus⟨x2​(t)⟩=⟨y2​(t)⟩=2​k​t\langle x^{2}(t)\rangle=\langle y^{2}(t)\rangle=2kt, as expected.
ForD=d=3D=d=3,Γ​(D/2+1)/Γ​(D/2)=Γ​(2+1/2)/Γ​(1+1/2)=(3​π/22)/(π/2)=3/2\Gamma(D/2+1)/\Gamma(D/2)=\Gamma(2+1/2)/\Gamma(1+1/2)=(3\sqrt{\pi}/2^{2})/(\sqrt{\pi}/2)=3/2. As⟨x2​(t)⟩=⟨y2​(t)⟩=⟨z2​(t)⟩=⟨r2​(t)⟩/3\langle x^{2}(t)\rangle=\langle y^{2}(t)\rangle=\langle z^{2}(t)\rangle=\langle r^{2}(t)\rangle/3we find⟨x2​(t)⟩=(3/2)/3×4​k​t=2​k​t\langle x^{2}(t)\rangle=(3/2)/3\times 4kt=2kt, that is the correct uniform diffusion relation for each degree of freedom.
With the decrease ofDDfromdd, as shown in Fig.1,Γ​(D/2+1)/Γ​(D/2)\Gamma(D/2+1)/\Gamma(D/2)decreases. Note thatD<dD<dcorresponds to an increase in the medium porosity, where the global diffusion in the medium decreases, due to lower accessibility of the geometrical volume for the chemical transport.
Note that this model calculation does not capture a sharp drop in the diffusion constant at the percolation threshold, as shown in Ref.[36].Figure 1:Γ​(D/2+1)/Γ​(D/2)\Gamma(D/2+1)/\Gamma(D/2)vs.DD.
Two special limits ofD=2D=2andD=3D=3correspond to cylindrical and spherical geometries.

The Gaussian PDF does not correspond to an exact solution of the diffusion equation for any other boundary conditions, such as the ones used in this work, e.g., a uniform distribution in a cylinder with radiusRcR_{c}att=0t=0.
It has been included in our discussion to benchmark the numerical solutions and for illustrating the fastest possible spatial spreading in the absence of geometric constraints or anomalous effects. Deviations from Gaussian behavior therefore provide a direct and intuitive measure of the impact of structural disorder and anomalous transport, as in large distances (r>>Rcr>>R_{c}) and finite time, because the exact solutions of normal diffusion asymptotically approach the Gaussian.Figure 2:Radial probability distributionP​(r,t)P(r,t)as a function of distancerrfor the fractal diffusion model with fractal dimensionD=2.5D=2.5, shown for different values of the fractional parameterθ=0.0,0.5,\theta=0.0,0.5,and1.51.5.
Panels (a)–(c) correspond to timest=0.1​st=0.1\,\mathrm{s},t=1​st=1\,\mathrm{s}, andt=10​st=10\,\mathrm{s}, respectively.
For comparison, the classical normal diffusion (red dashed line) and Gaussian diffusion (blue dotted line) solutions are also displayed.
Increasingθ\thetaleads to enhanced localization and slower spreading relative to the normal and Gaussian cases, highlighting the influence of anomalous transport induced by fractal geometry.Figure 3:D=2.5D=2.5andt=0.005​st=0.005s(a)θ=0.3\theta=0.3(b)θ=0.5\theta=0.5(c)θ=0.8\theta=0.8Figure 4:Radial probability distributionP​(r,t)P(r,t)as a function of distancerrfor the fractal diffusion model with varying fractal dimensionDD.
Panels (a) and (b) correspond to the caseθ=0\theta=0at timest=1​st=1\,\mathrm{s}andt=10​st=10\,\mathrm{s}, respectively, while panels (c) and (d) show the caseθ=1.5\theta=1.5at the same times.
Results are shown for different fractal dimensionsD=2.0,2.3,2.5,D=2.0,2.3,2.5,and2.72.7.
For comparison, the classical normal diffusion solution withD=2D=2(red dashed line) and the Gaussian diffusion solution (blue dotted line) are also included.
The figure illustrates how both the fractal dimension and the fractional parameterθ\thetacontrol the spreading rate and shape of the radial probability distribution.Figure 5:θ=0\theta=0andt=0.005​st=0.005s(a)D=2D=2(b)D=2.5D=2.5(c)D=2.8D=2.8Figure 6:Steady-state radial probability distributionP​(r)P(r)as a function of distancerrfor the fractal diffusion model with different values of the fractional parameterθ=0.0,1.0,1.5,\theta=0.0,1.0,1.5,and2.02.0.
Panel (a) corresponds to the Euclidean case with fractal dimensionD=2D=2, while panel (b) shows the fractal geometry withD=2.5D=2.5.
For comparison, the steady-state solutions of normal diffusion (black dashed line) and Gaussian diffusion (magenta dotted line) are also presented.
The results demonstrate how both the fractal dimension and the parameterθ\thetamodify the stationary spatial profile, leading to deviations from classical diffusive behavior.Figure 7:Steady-state radial probability distributionP​(r)P(r)as a function of distancerrfor the fractal diffusion model with varying fractal dimensionDD.
Panel (a) corresponds to the caseθ=0\theta=0, while panel (b) shows the caseθ=1.5\theta=1.5.
Results are presented for different fractal dimensionsD=2.0,2.2,2.4,2.6,D=2.0,2.2,2.4,2.6,and2.82.8.
For comparison, the steady-state solutions of normal diffusion (black dashed line) and Gaussian diffusion
(magenta dotted line) are also included.
The figure illustrates how the combined effects of the fractional parameterθ\thetaand the fractal
dimensionDDmodify the stationary spatial distribution relative to classical diffusion models.

To quantify inter-track interactions, we introduce an overlap measure between diffusive plumes generated by spatially separated sources. This quantity serves as a proxy for the probability of inter-track coupling, and therefore for the likelihood of radical recombination between tracks. By evaluating how this overlap depends on the parametersDDandθ\theta, we directly connect geometry-governed transport properties to inter-track interaction strength.

## II.4Boundary conditions

Throughout the entire work, we consider the numerical value of the diffusion constantk=k=1 nm2/ns (10−910^{-9}m2/s). Note that for OH-radicals under thermal diffusion in water,k=4.3k=4.3nm2/ns.

All simulations shown in Figs.2–7were performed under radially symmetric boundary conditions for Eq.3. For the fractal and normal diffusion models, the computational domain was defined forr≥Rcr\geq R_{c}, whereRcR_{c}represents a microscopic cutoff length. Atr=Rcr=R_{c}, a mixed (Robin) boundary condition was imposed,−k​RcD−1−θ​∂P​(r,t)∂r|r=Rc=𝒫​[Pb​(t)−P​(Rc,t)],-k\,R_{c}^{D-1-\theta}\left.\frac{\partial P(r,t)}{\partial r}\right|_{r=R_{c}}=\mathcal{P}\,[P_{b}(t)-P(R_{c},t)],(9)

where𝒫\mathcal{P}denotes an effective permeability parameter. The boundary valuePb​(t)P_{b}(t)was assumed constant in time, corresponding toP^b​(s)=Pb/s\hat{P}_{b}(s)=P_{b}/sin Laplace space (ssis the Laplace transform variable).
At large distances, the domain was treated as unbounded withP​(r,t)→0P(r,t)\rightarrow 0asr→∞r\rightarrow\infty, enforced through decaying modified Bessel-function solutions. In contrast, the Gaussian reference distribution corresponds to the fundamental solution of the normal diffusion equation in an infinite domain with initial conditionP​(r,0)=δ​(r)P(r,0)=\delta(r)and vanishing probability density at infinity, and therefore does not involve an explicit boundary condition atr=Rcr=R_{c}. For steady-state calculations, identical spatial boundary conditions were applied with∂P/∂t=0\partial P/\partial t=0, and all distributions were normalized using the appropriate geometrical measure.


## IIIResults

Table1summarizes the fixed model parameters used in all numerical simulations, while control parameters such as the fractal exponentθ\thetaandDDare varied and reported separately in the corresponding figure captions.Table 1:Fixed model parameters used in all numerical simulations.ParameterDescriptionValuekk(orσ\sigma)Diffusion coefficient (Conductivity)4.3×10−9​m2​s−14.3\times 10^{-9}\,\mathrm{m^{2}\,s^{-1}}kk(orσ\sigma) (steady-state)Diffusion coefficient (Conductivity)17.5×10−9​m2​s−117.5\times 10^{-9}\,\mathrm{m^{2}\,s^{-1}}μ\muEffective reaction (decay) rate0.5​s−10.5\,\mathrm{s^{-1}}RcR_{c}Microscopic cutoff radius0.5×10−9​m0.5\times 10^{-9}\,\mathrm{m}𝒫\mathcal{P}Boundary permeability parameter1.5×10−6​m1.5\times 10^{-6}\,\mathrm{m}

## III.1Comparison of transient diffusion profiles

Figures2–4present the temporal evolution of the radial probability densityP​(r,t)P(r,t)for
the three diffusion models—fractal, normal, and Gaussian—under identical conditions. Across all models, the
distributions are initially localized near the origin at early times, reflecting the common initial
condition. As time progresses, however, systematic differences in both spreading rate and profile shape
emerge.

The influence of the fractional parameterθ\thetais isolated in Figure2for a fixed fractal
dimensionD=2.5D=2.5.
At early times, variations inθ\thetaprimarily modify the peak height of the distribution, while the
overall spatial extent remains comparable across cases. With increasing time, the effect ofθ\thetabecomes progressively more pronounced: larger values ofθ\thetalead to enhanced localization, steeper
decay of the distribution tail, and a marked suppression of long-distance transport. Relative to the normal
and Gaussian solutions, increasingθ\thetaproduces heavier central accumulation and shorter effective
diffusion lengths, indicating a systematic reduction in transport efficiency.
Figure 8:Three-dimensional visualization of the average overlap integralO​(t)O(t)as a function of the fractal dimensionDDand the anomalous diffusion exponentθ\theta, evaluated at a fixed timet=10​st=10\,\mathrm{s}and track separation400​nm400\,\mathrm{nm}.

LetC​(𝐱,t;𝐫i)C(\mathbf{x},t;\mathbf{r}_{i})denote the concentration field evaluated at observation point𝐱\mathbf{x}and timett, generated by a point source located at position𝐫i\mathbf{r}_{i}. We consider two identical sources placed at𝐫1\mathbf{r}_{1}and𝐫2\mathbf{r}_{2}within the same fractal medium characterized by transport parametersDDandθ\theta. The corresponding concentration profiles are thereforeC1​(𝐱,t)=C​(𝐱,t;𝐫1)C_{1}(\mathbf{x},t)=C(\mathbf{x},t;\mathbf{r}_{1})andC2​(𝐱,t)=C​(𝐱,t;𝐫2)C_{2}(\mathbf{x},t)=C(\mathbf{x},t;\mathbf{r}_{2}). Since both fields satisfy the same generalized diffusion equation under identical boundary conditions, they differ only by a spatial translation associated with the source positions. Defining the separation vectorℓ=𝐫2−𝐫1\bm{\ell}=\mathbf{r}_{2}-\mathbf{r}_{1}, translational invariance impliesC2​(𝐱,t)=C1​(𝐱−ℓ,t)C_{2}(\mathbf{x},t)=C_{1}(\mathbf{x}-\bm{\ell},t). The overlap integral is then defined asO​(t)=∫VC1​(𝐱,t)​C2​(𝐱,t)​d2​𝐱,O(t)=\int_{V}C_{1}(\mathbf{x},t)\,C_{2}(\mathbf{x},t)\,d^{2}\mathbf{x},

where𝐱\mathbf{x}is the integration (observation) coordinate over the spatial domainVV. This quantity measures the spatial coexistence of two otherwise identical diffusion profiles displaced byℓ\bm{\ell}and provides a direct macroscopic indicator of inter-source (inter-track) interaction and serves as a proxy for the probability of inter-track coupling.

Figure3shows the overlap integralO​(t)O(t)as a function of the anomalous exponentθ\theta, for a fixed fractal dimensionD=2.5D=2.5and timet=10​st=10\,\mathrm{s}. The figure focuses on the integrated overlap, which quantifies the total spatial superposition of the two diffusive plumes.

For smallθ\theta[Fig.3(a)], the overlap integral attains relatively high values, indicating extended plume interaction consistent with weakly anomalous diffusion. Asθ\thetaincreases to an intermediate value [Fig.3(b)],O​(t)O(t)decreases noticeably, reflecting enhanced confinement and reduced plume overlap. In the strongly anomalous regime [Fig.3(c)], the overlap integral drops sharply, signifying severe suppression of inter-plume coupling due to highly localized transport.

These results confirm that increasingθ\thetanot only shortens the characteristic diffusion length but also systematically reduces the overall spatial overlap between plumes. Importantly, this effect is non-perturbative: even at a fixed fractal dimension, the transport efficiency—and consequently the overlap integral—can be dramatically reduced solely through the anomalous scaling exponentθ\theta. This highlights the dominant role of fractional dynamics in controlling mass transfer in structurally complex media.

Figure4examines the combined influence of the fractal dimensionDDand the fractional parameterθ\theta. Forθ=0\theta=0[Figs.4(a,b)], increasingDDleads to progressively broader
distributions, reflecting enhanced spatial accessibility and convergence toward the classical normal
diffusion limit asD→2D\to 2. In contrast, forθ=1.5\theta=1.5[Figs.4(c,d)], this trend is
significantly attenuated: even at larger values ofDD, the distributions remain comparatively localized.
These results demonstrate that fractional dynamics can dominate over geometric connectivity in determining
transient transport behavior, giving rise to a broad range of diffusion profiles not captured by standard
diffusion models.

Figure5presents two-dimensional steady-state spatial distributions for the caseθ=0\theta=0at fixed timet=10​st=10\,\mathrm{s}while varying the fractal dimensionDD. In contrast to Figure 2, where the fractional parameter was varied at constantDD, here the influence of geometric topology alone is isolated.

For the Euclidean caseD=2D=2[Fig.5(a)], the distribution exhibits the broadest spatial spreading, consistent with classical diffusion behavior. As the fractal dimension increases toD=2.5D=2.5andD=2.8D=2.8[Figs.5(b,c)], the spatial profile progressively narrows and peak localization increases. This behavior reflects the reduction of effective accessible volume despite the nominal increase in geometric dimension, a characteristic feature of fractal substrates where connectivity and tortuosity compete with dimensional scaling.

Importantly, even in the absence of fractional effects (θ=0\theta=0), purely geometric fractality modifies the spatial organization of the probability density. This demonstrates that topology alone can alter transport characteristics, independent of anomalous temporal scaling. When combined with nonzeroθ\theta(as shown in earlier figures), these geometric effects become even more pronounced, reinforcing the complementary roles ofDDandθ\thetain controlling diffusion dynamics.

## III.2Steady-state distributions

The steady-state radial probability distributions are shown in Figure6for varying values ofθ\thetaand in Figure7for varying values ofDD. In Figure6(a), corresponding to
the Euclidean caseD=2D=2, the steady-state distribution closely follows the normal diffusion solution for
small values ofθ\theta, with noticeable deviations emerging only at largerθ\theta. Asθ\thetaincreases, the distribution exhibits reduced peak height and increasingly pronounced tails, indicating a
departure from classical equilibrium behavior.

In contrast, Figure6(b), corresponding to the fractal geometry withD=2.5D=2.5, shows that even for
moderate values ofθ\theta, the steady-state distributions differ substantially from both normal and
Gaussian solutions. The presence of broader tails and suppressed peaks indicates that fractal geometry alone
is sufficient to alter the stationary spatial organization. Comparison with the Gaussian and normal steady-
state solutions confirms that the equilibrium distributions retain a clear dependence on the underlying
transport mechanism.

Figure7further elucidates the role of the fractal dimensionDDin the stationary regime.
Forθ=0\theta=0, Figure7(a), increasingDDproduces progressively wider distributions,
consistent with increased spatial connectivity. Forθ=1.5\theta=1.5, Figure7(b), the same increase
inDDresults in significantly weaker broadening, demonstrating that fractional dynamics dominate over
geometric effects in determining the steady-state profile. Together, these results indicate thatDDandθ\thetaplay complementary but distinct roles:DDgoverns the spatial topology of the medium, whileθ\thetacontrols the effective transport efficiency across scales.


## IVDiscussion

The results presented in this study demonstrate that diffusion in structurally heterogeneous media is
fundamentally governed by geometry, and that deviations from classical Fickian behavior emerge naturally when
transport occurs on fractal substrates. While all
diffusion models considered here exhibit strong localization at early times due to identical initial
conditions, pronounced differences arise as transport evolves. The Gaussian reference model exhibits the
fastest spatial spreading, followed by classical normal diffusion, whereas the generalized fractal diffusion
model consistently shows slower radial expansion and enhanced localization. This hierarchy of spreading rates
reflects increasing geometric constraints and reduced connectivity of transport pathways.

At the mechanistic level, this behavior originates from the anomalous flux termrD−1−θ​∂rPr^{D-1-\theta}\partial_{r}P, which introduces a scale-dependent suppression of transport at larger
distances. As a result, long-range diffusion becomes increasingly inefficient, leading to subdiffusive
dynamics characterized by heavy central accumulation and truncated spatial tails. These features persist
across both transient and steady-state regimes, indicating that anomalous transport is an intrinsic
consequence of geometry rather than a transient kinetic effect[4,6].

A pronounced sharp peak appears in the spatial concentration field in the immediate vicinity of the track core, originating from the small-argument behavior of the modified Bessel functions entering the Green-function kernel. In particular, whenq​r→0qr\to 0(which occurs at very small radial distances or at early times), the modified Bessel function of the second kind,Kν​(q​r)K_{\nu}(qr), exhibits strong amplification that reflects the singular character of an idealized point-like source. Although this behavior is mathematically consistent with the analytical structure of the solution, it produces highly localized spikes in the numerical implementation that are not physically meaningful at the resolved scale of the model and may lead to numerical instability. To regularize this short-distance singularity, we introduced a smooth cutoff by replacing the argumentq​rqrwith(q​r)2+ε2\sqrt{(qr)^{2}+\varepsilon^{2}}. This modification prevents the kernel from probing arbitrarily small spatial scales, effectively rounding the Bessel-driven divergence while preserving the correct asymptotic behavior at larger distances. Physically, the cutoff can be interpreted as accounting for the finite core radius of the track or the limited spatial resolution of the medium, thereby removing the unphysical divergence associated with a strictly point-like source. Importantly, this regularization suppresses the artificial peak without significantly altering the large-scale spatial distribution or the integrated overlap, which remains governed by contributions from physically relevant distances.

A key outcome of this work is the clear separation of roles played by the fractal dimensionDDand the
fractional parameterθ\theta. The fractal dimension encodes the spatial topology and connectivity of the
medium, controlling the degree to which space is accessible for diffusion[7,8,9]. In contrast,θ\thetagoverns temporal transport efficiency,
capturing memory effects, transient trapping, crowding, and heterogeneous transport resistance along diffusion
pathways. The competition between these two parameters gives rise to a wide spectrum of diffusion behaviors,
ranging from near-Fickian transport to strongly localized, non-Gaussian dynamics.

This separation provides a physically transparent framework for interpreting tissue heterogeneity. Media
characterized by near-Euclidean geometry and lowθ\thetavalues support efficient transport and rapid
homogenization, leading to diffusion profiles close to classical normal or Gaussian limits. Conversely, media
with elevated fractal dimensions and nonzeroθ\thetaexhibit suppressed long-range transport, enhanced
localization, and long-lived concentration gradients. Importantly, these effects persist in the steady state,
demonstrating that equilibrium distributions retain a memory of the underlying geometric disorder, as
previously suggested in studies of tumor vasculature and porous biological networks[10,11].

When viewed in a biological context, these transport regimes naturally map onto differences between normal
and tumor tissues. Normal tissues are typically characterized by relatively homogeneous extracellular spaces,
well-connected intracellular environments, and weak geometric constraints, conditions under which transport
is often well approximated by classical or weakly anomalous diffusion[7,12]. In
contrast, tumor tissues exhibit pronounced architectural irregularity arising from abnormal cell packing,
chaotic vasculature, dense extracellular matrix remodeling, and elevated tortuosity[8,10,14]. These features reduce the accessible transport pathways and introduce
scale-dependent resistance, conditions that are naturally captured by a fractal description withD>2D>2and
nonzeroθ\theta, consistent with experimentally observed diffusion-limited hypoxia and heterogeneous drug
penetration[13,15,18].

The relevance of this framework is further reinforced by experimental observations of membrane-scale
heterogeneity in cancer cells. Fluorescence lifetime imaging and viscosity-sensitive probes have revealed
highly heterogeneous nanoviscosity landscapes within lipid bilayers, even within a single membrane[24]. Tumor cell membranes, in particular, exhibit significantly higher and more spatially
variable viscosities compared to normal cells[23]. Such nanoscale mechanical heterogeneity
introduces additional resistance to lateral diffusion and reaction–diffusion coupling, promoting non-
Gaussian transport behavior. Within the present framework, these effects are naturally captured by nonzero
values ofθ\thetaand elevated effective fractal dimensions, linking membrane-scale disorder to
macroscopic transport anomalies[27].

From a radiobiological perspective, these findings have direct implications for understanding tissue-
dependent responses to ultra-high dose rate (FLASH) irradiation. The localization of reactive species,
oxygen, and signaling molecules within fractal-like media implies reduced spatial overlap and diminished
inter-track interactions, particularly in structurally complex tumor tissues[36,37], consistent with the overlap suppression quantified in the present model. In
contrast, in more homogeneous media, enhanced connectivity promotes inter-track overlap, facilitating
recombination processes and rapid spatial homogenization, a mechanism consistent with recent stochastic
reaction–diffusion and track-structure analyses of FLASH response[33,36].

The present results indicate that geometry does not create inter-track interactions, but rather controls their extent once multiple tracks coexist within short spatial and temporal separations. In this sense, FLASH irradiation can be interpreted as a regime in which simultaneous multi-track transport makes overlap a relevant quantity, thereby exposing the role of geometry in governing reactive-species coupling. Under conventional dose-rate conditions, where such coexistence is limited, the same transport properties persist but have a reduced impact on inter-track interactions. Importantly, this framework does not replace existing biochemical or radiochemical explanations of FLASH effects, such as oxygen depletion and radical recombination kinetics[29,31,34], but rather complements them by identifying tissue geometry as an active modulator of transport and reactivity. By explicitly incorporating scale-dependent diffusivity and fractal topology, the model provides a unifying description that bridges microscopic structural disorder with macroscopic transport efficiency. This geometry-driven perspective helps reconcile disparate experimental observations, including hypoxia, delayed drug penetration, heterogeneous oxidative stress, and reduced inter-track chemical recombination in malignant tissues[30,28,35].

Overall, the generalized fractal diffusion model establishes a mechanistic link between tissue architecture
and transport behavior, demonstrating that anomalous diffusion is not merely a mathematical abstraction but a
physically necessary ingredient for describing transport in heterogeneous biological systems. By framing
diffusion as a geometry-governed process, this work provides a foundation for geometry-aware modeling of
radiobiological response and motivates future experimental efforts to quantify tissue fractality, transport
heterogeneity, and scale-dependent diffusivity in the context of FLASH radiotherapy.

## VConclusion

In this work, we developed a geometry-governed diffusion framework to describe molecular transport in
structurally heterogeneous biological tissues, with particular relevance to ultra-high dose rate (FLASH)
radiotherapy. By formulating diffusion on fractal substrates and introducing a scaling exponent that captures
geometric resistance and memory effects, we demonstrated how deviations from classical Fickian transport
arise naturally from tissue architecture itself.

The model identifies two complementary parameters that control transport behavior: the fractal dimensionDD, which encodes the spatial topology and connectivity of the medium, and the fractional parameterθ\theta, which governs scale-dependent transport efficiency and anomalous dynamics. Together, these
parameters define distinct diffusion regimes that persist across both transient and steady-state conditions.
Media characterized by near-Euclidean geometry and weak anomalous effects exhibit efficient spreading and
rapid homogenization, while fractal-like media display suppressed long-range transport, enhanced
localization, and non-Gaussian spatial profiles.

Within this framework, normal and tumor tissues naturally map onto different transport regimes. Normal
tissues are associated with lower effective fractal dimensionality and smallθ\theta, leading to diffusion
behavior close to classical or weakly anomalous limits. In contrast, tumor tissues—characterized by architectural
disorder, irregular vasculature, dense extracellular matrix remodeling, and elevated crowding—are well
described by larger effective fractal dimensions and nonzeroθ\theta, resulting in localized diffusion and
long-lived concentration gradients. These transport characteristics provide a geometric explanation for
experimentally observed phenomena such as chronic hypoxia, delayed drug penetration, and reduced spatial
overlap of reactive species in malignant tissues.

From a radiobiological perspective, the present results provide a geometry-driven framework for interpreting differential
tissue response under FLASH irradiation. By limiting inter-track overlap, as quantified by the overlap integral, and suppressing long-range transport
of radiolytic species in structurally complex media, fractal tissue geometry reduces collective chemical
reactivity, while more homogeneous tissues permit greater inter-track interaction and recombination.
Importantly, this mechanism arises from geometry-governed transport properties and does not rely on specific assumptions about
biochemical reaction rates or oxygen depletion kinetics.

Overall, this study establishes fractal geometry as a fundamental determinant of transport efficiency in
biological tissues and provides a unifying theoretical framework linking microscopic structural disorder to
macroscopic radiobiological outcomes. By framing diffusion as a geometry-controlled process, the model
complements existing chemical and kinetic descriptions of FLASH effects and motivates future experimental
efforts to quantify tissue fractality, transport heterogeneity, and scale-dependent diffusivity in both
normal and malignant tissues. Such geometry-aware modeling may ultimately contribute to more predictive and
tissue-specific approaches in radiotherapy planning and optimization.

## VIAcknowledgment

RA was supported by the American Cancer Society Diversity in Cancer Research Institutional Development Grant (DICRIDG-21-074-01-DICRIDG) at Howard University.

## Appendix ANumerical Solution of the Diffusion Models

This Appendix provides a detailed description of the numerical procedures used to obtain the transient radial probability distributions for the three diffusion models considered in this work: generalized fractal diffusion, normal (Euclidean) diffusion, and a Gaussian reference solution. All notation and normalization conventions are fully consistent with those introduced in Secs. II and III.

## A.1Generalized Fractal Diffusion Model

The generalized diffusion equation on a fractal substrate is given by Eq. (3) of the main text,∂P​(r,t)∂t=1rD−1​∂∂r​[k​rD−1−θ​∂P​(r,t)∂r]−μ​P​(r,t),\frac{\partial P(r,t)}{\partial t}=\frac{1}{r^{D-1}}\frac{\partial}{\partial r}\left[k\,r^{D-1-\theta}\frac{\partial P(r,t)}{\partial r}\right]-\mu P(r,t),(10)

whereDDis the fractal (Hausdorff) dimension,θ\thetais the fractional transport exponent,kkis the effective transport coefficient, andμ\muis an effective decay or reaction rate.

## A.1.1Laplace-space formulation

To facilitate numerical evaluation, Eq. (10) is transformed to Laplace space,P^​(r,s)=∫0∞e−s​t​P​(r,t)​𝑑t,\hat{P}(r,s)=\int_{0}^{\infty}e^{-st}P(r,t)\,dt,(11)

which yields[d2d​r2+D−1−θr​dd​r−q2]​P^​(r,s)=−P​(r,0)k​rD−1,\left[\frac{d^{2}}{dr^{2}}+\frac{D-1-\theta}{r}\frac{d}{dr}-q^{2}\right]\hat{P}(r,s)=-\frac{P(r,0)}{k\,r^{D-1}},(12)

withq=s+μk,ν=D−2+θ2.q=\sqrt{\frac{s+\mu}{k}},\qquad\nu=\frac{D-2+\theta}{2}.(13)

The corresponding Green’s function isG​(r,r′;s)=r′⁣−D+2+θ​{Iν​(q​r)​Kν​(q​r′),r≤r′,Iν​(q​r′)​Kν​(q​r),r>r′,G(r,r^{\prime};s)=r^{\prime-D+2+\theta}\begin{cases}I_{\nu}(qr)\,K_{\nu}(qr^{\prime}),&r\leq r^{\prime},\\[4.0pt]
I_{\nu}(qr^{\prime})\,K_{\nu}(qr),&r>r^{\prime},\end{cases}(14)

whereIνI_{\nu}andKνK_{\nu}denote modified Bessel functions of the first and second kind.

## A.1.2Particular solution and boundary condition

The Laplace-space solution is written asP^​(r,s)=P^part​(r,s)+A​(s)​Kν​(q​r),\hat{P}(r,s)=\hat{P}_{\mathrm{part}}(r,s)+A(s)\,K_{\nu}(qr),(15)

with the particular solutionP^part​(r,s)=−∫Rc∞G​(r,r′;s)​P​(r′,0)k​r′⁣D−1​𝑑r′.\hat{P}_{\mathrm{part}}(r,s)=-\int_{R_{c}}^{\infty}G(r,r^{\prime};s)\frac{P(r^{\prime},0)}{k}\,r^{\prime D-1}\,dr^{\prime}.(16)

At the inner cutoff radiusr=Rcr=R_{c}, a Robin-type boundary condition is imposed,−k​RcD−1−θ​∂P^∂r|r=Rc=Λ​[P^b​(s)−P^​(Rc,s)],-k\,R_{c}^{D-1-\theta}\left.\frac{\partial\hat{P}}{\partial r}\right|_{r=R_{c}}=\Lambda\left[\hat{P}_{b}(s)-\hat{P}(R_{c},s)\right],(17)

whereΛ\Lambdais an effective permeability parameter andP^b​(s)\hat{P}_{b}(s)is the Laplace-transformed boundary value. Equation (17) uniquely determines the amplitudeA​(s)A(s).

## A.1.3Inverse Laplace transform

The time-dependent probability density is obtained via numerical inversion of the Laplace transform using the Stehfest algorithm[38],P​(r,t)=ln⁡2t​∑k=1NVk​P^​(r,sk),sk=k​ln⁡2t,P(r,t)=\frac{\ln 2}{t}\sum_{k=1}^{N}V_{k}\,\hat{P}\!\left(r,s_{k}\right),\qquad s_{k}=\frac{k\ln 2}{t},(18)

whereVkV_{k}are the Stehfest weights. Unless otherwise stated,N=10N=10is used, and convergence was verified by varyingNN.

Normalization is enforced according to the fractal measure,∫Rc∞P​(r,t)​rD−1​𝑑r=1.\int_{R_{c}}^{\infty}P(r,t)\,r^{D-1}\,dr=1.(19)

## A.2Normal (Euclidean) Diffusion

The normal diffusion model is recovered in the Euclidean limitD=2D=2andθ=0\theta=0. Equation (10) reduces to∂P​(r,t)∂t=k​[1r​∂∂r​(r​∂P∂r)]−μ​P​(r,t).\frac{\partial P(r,t)}{\partial t}=k\left[\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial P}{\partial r}\right)\right]-\mu P(r,t).(20)

In Laplace space, the Green’s function takes the formG​(r,r′;s)=I0​(q​min⁡{r,r′})​K0​(q​max⁡{r,r′}),G(r,r^{\prime};s)=I_{0}\!\left(q\min\{r,r^{\prime}\}\right)K_{0}\!\left(q\max\{r,r^{\prime}\}\right),(21)

withq=(s+μ)/kq=\sqrt{(s+\mu)/k}. The solution procedure, boundary condition, and Stehfest inversion are identical to those used for the fractal model.

Normalization is performed using the Euclidean measure,∫0∞2​π​r​P​(r,t)​𝑑r=1.\int_{0}^{\infty}2\pi r\,P(r,t)\,dr=1.(22)

## A.3Gaussian Reference Solution

For comparison, we also consider the analytical Gaussian solution describing free diffusion in two dimensions,PG​(r,t)=14​π​k​t​exp⁡(−r24​k​t),P_{\mathrm{G}}(r,t)=\frac{1}{4\pi kt}\exp\!\left(-\frac{r^{2}}{4kt}\right),(23)

which is normalized analytically. This solution represents the limiting case of homogeneous, memoryless transport and provides a reference for assessing deviations induced by fractal geometry and anomalous scaling.


All three models are evaluated using identical transport parameters and initial conditions. Radial probability distributions are compared at fixed times to isolate the effects of fractal dimensionalityDDand anomalous scalingθ\theta. Numerical quadrature is performed with adaptive integration, and normalization is verified to within numerical precision for all cases.

## References
- Mandelbrot [1967]Mandelbrot, B.B. (1967). “How Long Is the Coast of Britain? Statistical Self-Similarity and Fractional Dimension.”Science,156(3775), 636–638.
- Feder [1988]Feder, J. (1988).Fractals. Springer New York, NY.
- Bunde & Havlin [1991]Bunde, A., Havlin, S. (1991).Fractals and Disordered Systems. Springer Berlin, Heidelberg.
- Metzler & Klafter [2000]Metzler, R., Klafter, J. (2000). “The random walk’s guide to anomalous diffusion: a fractional dynamics approach.”Phys. Rep.339, 1–77.
- Tarasov [2006]Tarasov, V.E. (2006). “Continuous limit of discrete systems with long-range interaction.”Journal of Physics A: Mathematical and General39, 14895.
- Zaslavsky [2002]Zaslavsky, G.M. (2002). “Chaos, fractional kinetics, and anomalous transport.”Phys. Rep.371, 461–580.
- Weibel & Gomez [1962]Weibel, E.R., Gomez, D.M. (1962). “Architecture of the human lung. Use of quantitative methods establishes fundamental relations between size and number of lung structures.”Science137(3530), 577–85.
- Baish & Jain [2000]Baish, J.W., Jain, R.K. (2000). “Fractals and cancer.”Cancer Res.60(14), 3683–8.
- Gazit et al. [1995]Gazit, Y., Berk, DA., Leunig, M., Baxter, LT., Jain, RK. (1995). “Scale-invariant behavior and vascular network formation in normal and tumor tissue.”Physical Review Letters75(12), 2428–2431.
- Gazit et al. [1997]Gazit, Y., Baish, JW., Safabakhsh, N., Leunig, M., Baxter, LT., Jain, RK., (1997). “Fractal characteristics of tumor vascular architecture during tumor growth and regression.”Microcirculation4(4), 395–402.
- Guiot et al. [2006]Guiot, C., Delsanto, P., Carpinteri, A., Pugno, N., Mansury, Y., Deisboeck, T.S. (2006). “The dynamic evolution of the power exponent in a universal growth model of tumors.”J. Theor. Biol.240(3), 459–63.
- Grimes et al. [2014]Grimes, D.R., Kannan, P., Warren, D., et al. (2014). “Estimating oxygen distribution from vasculature in three-dimensional tumour tissue.”J. R. Soc. Interface13, 20160070.
- Vaupel et al. [2021]Vaupel, P., Flood, A.B., Swartz, H.M. (2021). “Oxygenation Status of Malignant Tumors vs. Normal Tissues: Critical Evaluation and Updated Data Source Based on Direct Measurements with pO2 Microsensors.”Appl. Magn. Reson.52, 1451–1479.
- Vaupel & Harrison [2004]Vaupel, P., Harrison, L. (2004). “Tumor hypoxia: causative factors, compensatory mechanisms, and cellular response.”Oncologist9, 4–9.
- Degner et al. [1988]Degner FL., Sutherland RM. (1988). “Mathematical modelling of oxygen supply and oxygenation in tumor tissues: prognostic, therapeutic, and experimental implications.”Int J Radiat Oncol Biol Phys.15(2), 391–7.
- Lagerlöf et al. [2014]Lagerlöf JH, Kindblom J, Bernhardt P. (2014). “Oxygen distribution in tumors: a qualitative analysis and modeling study providing a novel Monte Carlo approach.”Med Phys.41(9), 094101.
- Netti et al. [1995]Netti, P.A., Baxter, L.T., Boucher, Y., Skalak, R., Jain, R.K. (1995). “Time-dependent behavior of interstitial fluid pressure in solid tumors: implications for drug delivery.”Cancer Res.55, 5451–5458.
- Stylianopoulos & Jain [2013]Stylianopoulos, T., Jain, R.K. (2013). “Combining two strategies to improve perfusion and drug delivery in solid tumors.”Proc Natl Acad Sci U S A.110(46), 18632–7.
- Mohammadi et al. [2023]Mohammadi M, Sefidgar M, Aghanajafi C, Kohandel M, Soltani M. (2023). “Computational Multi-Scale Modeling of Drug Delivery into an Anti-Angiogenic Therapy-Treated Tumor.”Cancers (Basel).15(22), 5464.
- Kashkooli et al. [2021]Kashkooli, F.M., Soltani, M., Momeni, M.M. (2021). “Computational modeling of drug delivery to solid tumors: A pilot study based on a real image.”Journal of Drug Delivery Science and Technology.62, 102347.
- Jain [2005]Jain, R.K. (2005). “Normalization of tumor vasculature: an emerging concept in antiangiogenic therapy.”Science307(5706), 58–62.
- Dewhirst & Secomb [2017]Dewhirst, M.W., Secomb, T.W. (2017). “Transport of drugs from blood vessels to tumour tissue.”Nat. Rev. Cancer17(12), 738–750.
- Li [2023]Li, Q., Zhu, W., Gong, S., Jiang, S., Feng, G. (2023). “Selective visualization of tumor cell membranes and tumors with a viscosity-sensitive plasma membrane probe.”Anal. Chem.95, 7254–7261.
- Ober [2019]Ober, K., Volz-Rakebrand, P., Stellmacher, J., Brodwolf, R., Licha, K., Haag, R., Alexiev, U. (2019). “Expanding the scope of reporting nanoparticles: Sensing of lipid phase transitions and nanoviscosities in lipid membranes.”Langmuir35, 11422–11434.
- Vozenin [2024]Vozenin, M.-C., Loo, B. W., Tantawi, S., Maxim, P. G., Spitz, D. R., Bailat, C., Limoli, C. L., (2024). “FLASH: New intersection of physics, chemistry, biology, and cancer medicine”, Rev. Mod. Phys.96, 035002.
DOI: 10.1103/RevModPhys.96.035002
- Favaudon [2025]Favaudon, V., Hotoiu, L., Labarbe, R., (2025). “Recombination of lipid free radicals in a Flash: Modeling the differential expression of oxylipins dependency on temperature, dose rate and cell status.”FRPT Conference, Prague, 2025.
- Szlasa [2020]Szlasa, W., Zendran, I., Zalesińska, A., Tarek, M., Kulbacka, J. (2020). “Expanding the scope of reporting nanoparticles: Sensing of lipid phase transitions and nanoviscosities in lipid membranes.”Lipid composition of the cancer cell membrane52, 321–342.
- Vozenin et al. [2022]Vozenin, M.C., Bourhis, J., Durante, M. (2022). “Towards clinical translation of FLASH radiotherapy.”Nat. Rev. Clin. Oncol.19(12), 791–803.
- Pratx & Kapp [2019]Pratx, G., Kapp, D.S. (2019). “A computational model of radiolytic oxygen depletion during FLASH irradiation and its effect on the oxygen enhancement ratio.”Physics in Medicine & Biology64, 185005.
- Montay-Gruel et al. [2019]Montay-Gruel, P. et al. (2019). “Long-term neurocognitive benefits of FLASH radiotherapy driven by reduced reactive oxygen species.”Proc Natl Acad Sci U S A.116(22), 10943–10951.
- Labarbe et al. [2020]Labarbe, R. Hotoiu, L., Barbier, J., Favauson, V. (2020). “A physicochemical model of reaction kinetics supports peroxyl radical recombination as the main determinant of the FLASH effect.”Radiother. Oncol.153, 303–310.
- Cao et al. [2021]Cao, X., Zhang, R., Esipova, T.V., Allu, S.R., Ashraf, R., Rahman, M. (2021). “Quantification of oxygen depletion during FLASH irradiation in vitro and in vivo.”International Journal of Radiation Oncology*Biology*Physics111(1), 240–248.
- Boscolo et al. [2021]Boscolo, D., Scifoni, E., Durante, M., Krämer, M., Fuss, M.C. (2021). “May oxygen depletion explain the FLASH effect? A chemical track structure analysis.”Radiotherapy and Oncology162, 68–75.
- Favaudon et al. [2022]Favaudon, V., Labarbe, R., Limoli, C.L. (2022). “Model studies of the role of oxygen in the FLASH effect.”Medical Physics49(3), 2068–2081.
- Espinosa-Rodríguez et al. [2022]Espinosa-Rodríguez, A., Gonzalo, R., Carabe, A. (2022). “Radical Production with Pulsed Beams: Understanding the Biochemical Basis of FLASH Radiotherapy and Future Applications.”Cancers14(21), 5227.
- Abolfath et al. [2023]Abolfath, R., Baikalov, A., Fraile, A., Bartzsch, S., Schüler, E., Mohan, R. (2023). “A stochastic reaction–diffusion modeling investigation of FLASH ultra-high dose rate response in different tissues.”Front. Phys.11, 1060910.
- Guo et al. [2024]Guo L., Medin PM., Wang KK. (2024). “A microscopic oxygen transport model for ultra-high dose rate radiotherapy in vivo: The impact of physiological conditions on FLASH effect.”Med. Phys.51(11), 8623–8637.
- [38]Stehfest, H. (1970). Algorithm 368: Numerical inversion of Laplace transforms [D5].Communications of the ACM, 13(1), 47–49.

## 


- 


Major funding support from
