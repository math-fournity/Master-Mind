# Divertor topology and vacuum vessel design for stellarators

**arXiv ID**: 2607.27127v1
**Authors**: Andrew Giuliani, Raffael Wendlinger, Misha Padidar, Robert Davies, Shibabrat Naik, Calvin Lowe, Georg Harrer
**Published**: 2026-07-29
**Categories**: physics.plasm-ph, math-ph
**HTML URL**: https://arxiv.org/html/2607.27127v1

## Abstract

We present stellarator optimization algorithms for designing the edge magnetic structure in vacuum fields, together with the vacuum vessel. First, we introduce a numerical method that robustly computes periodic-orbit fixed points of any type (elliptic, hyperbolic, or parabolic), which could form the basis of a divertor. To couple divertor and vacuum vessel design, we introduce parametric families of vacuum vessels for which point-to-vessel distances, and their derivatives, can be computed efficiently. The resulting algorithms use signed distance functions to enforce coil-vessel clearance while allowing coils to be placed on or off the vessel. Using these methods, we jointly optimize modular coils and the vacuum vessel to realize a wide range of magnetic topologies for diverting exhaust, including standard X-point divertors, and single- and double-null configurations. For the first time, we show that precise snowflake divertors can be achieved in stellarators. Using this framework, we generate a number of quasi-axisymmetric stellarator designs with compatible vacuum vessels and diverse divertor architectures, which we consider to be candidates for a next-generation STAR Lite prototype.

## Full Text

Divertor topology and vacuum vessel design for stellarators

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
- License: CC BY 4.0arXiv:2607.27127v1 [physics.plasm-ph] 29 Jul 2026

## Divertor topology and vacuum vessel design for stellaratorsAndrew Giuliani1,†\orcid0000-0002-4388-2782Raffael Wendlinger2\orcid0009-0001-8080-2657Misha Padidar1\orcid0000-0002-0710-4377Robert Davies3\orcid0000-0001-5570-5882Shibabrat Naik5\orcid0000-0001-7964-2513Calvin Lowe4\orcid0009-0009-1975-7322and Georg Harrer4\orcid0000-0002-1150-39871Center for Computational Mathematics, Flatiron Institute, New York, NY 10010, USA2Institute of Applied Physics, Technische Universität Wien, Vienna, Austria3Max Planck Institute for Plasma Physics, Wendelsteinstraße 1, 17491 Greifswald, Germany4Department of Physics, Hampton University, Hampton, VA 23663, USA5Department of Mathematics, Hampton University, Hampton, VA 23663, USA†Author to whom any correspondence should be addressed.agiuliani@flatironinstitute.org

## Abstract

We present stellarator optimization algorithms for designing the edge magnetic structure in vacuum fields, together with the vacuum vessel.
First, we introduce a numerical method that robustly computes periodic-orbit fixed points of any type (elliptic, hyperbolic, or parabolic), which could form the basis of a divertor.
To couple divertor and vacuum vessel design, we introduce parametric families of vacuum vessels for which point-to-vessel distances, and their derivatives, can be computed efficiently.
The resulting algorithms use signed distance functions to enforce coil-vessel clearance while allowing coils to be placed on or off the vessel.
Using these methods, we jointly optimize modular coils and the vacuum vessel to realize a wide range of magnetic topologies for diverting exhaust, including standard X-point divertors, and single- and double-null configurations. For the first time, we show that precise snowflake divertors can be achieved in stellarators.
Using this framework, we generate a number of quasi-axisymmetric stellarator designs with compatible vacuum vessels and diverse divertor architectures, which we consider to be candidates for a next-generation STAR_Lite prototype.††articletype:Paper

## 1Introduction

The divertor is an essential mechanism in tokamaks and stellarators for safely exhausting heat and particles. By routing escaping plasma towards reinforced divertor plates, the heat load on plasma-facing components can be kept within engineering limits, and helium “ash” and other impurities (sputtered wall material, for example) can be steadily removed by nearby pumps[84,49,59,8,27,50]. In addition, tokamak experiments have emphasized that the efficiency of diversion can also have significant consequences for the plasma core, for example: proper diversion can lead to steep profile gradients, and the “high-performance mode”[2,1,77], and small resonant magnetic perturbations in the edge can mitigate potentially destructive “edge-localized modes”, in which a large fraction of plasma stored energy is rapidly expelled[17,94]. In stellarators, the Large Helical Device (LHD) has also reported a synergy between divertor and core performance, with “closed divertors” leading to an improvement in core plasma density, the establishment of an internal transport barrier and reduced impurity retention in the core[66,93].
Incorporating divertor design as early in the design cycle as possible is therefore likely to improve the commercial viability of fusion power plants.

Following the success of Wendelstein 7-X[70,39,38], the island divertor has emerged as a common choice in stellarator design, featured in numerous recent designs[91,57,42,5,33,10,78,56].
Recently, however, there have been efforts to design tokamak-style X-point divertors (i.e. diverting X-points that sit at the top and/or bottom of the device and therefore have a rotational transformι=0\iota=0), to leverage the wealth of knowledge and experience gained from 50 years of research in tokamaks[40,26]. For island, helical, orι=0\iota=0X-point divertors, the structure of the edge magnetic field (in particular, the periodic magnetic field lines, also known as “fixed points”; X-points and O-points) is central to the divertor behavior. Despite the importance of the divertor in stellarators, the vast range of divertor possibilities has been explored relatively little, and divertor-related design efforts and optimization tool development (arguably) lag progress compared to methods for optimizing the plasma core.

Controlling the geometry of the tokamak divertor is, relatively speaking, a much more mature field of research[64], and there is a taxonomy of proposed (and experimentally realized) exhaust diversion structures. The creation of either one X-point (“single-null”) or an X-point at the top and bottom of the device (“double-null”) is long established (see e.g.[85,84]) and has been incorporated into the design of the large tokamaks (for example ITER[4], JET[46], JT-60[95,14], ASDEX[47], SPARC[51,71]). More advanced tokamak divertor experiments have been performed, for example by tightly baffling the divertor (i.e. preventing the neutralized particles from re-entering the plasma via the plasma-facing component geometry)[51,71,87]. A second example is “long-legged” or “Super-X” divertors, in which the divertor leg is extended to a region of larger major radius and weaker magnetic field, thus increasing the area of PFCs wetted by the plasma[89,25,41].
Yet another promising avenue is the “snowflake” divertor, in which two X-points are “brought together” to form a second-order null in the poloidal magnetic field, resulting in a six-legged fixed point[72,74,75]. These have been shown to be efficient at spreading due to increased number of legs, increased upstream-to-target connection length and enhanced turbulent transport around the fixed point (“churning modes”)[72,74,83,82,34,73,68]. Third-order poloidal null (“cloverleaf”) tokamak configurations have also been proposed[76,52]. The novel and wide-ranging divertor options in a tokamak are useful guides, because all can (in principle) be attained in a stellarator, the latter having greater freedom via the breaking of axisymmetry.

This work introduces a method for computing fixed points of a vacuum magnetic field and controlling their positions and type within a stellarator optimization loop. The method is numerically stable when computing fixed points of any type, and admits derivatives for use in stellarator optimization. To ensure compatibility of the fixed points with a vacuum vessel, we treat the vacuum vessel geometry as degrees of freedom, in addition to the coil geometries. To efficiently compute distances from the fixed points to the vessel, we introduce families of vacuum vessel geometries for which distances from points to the vessel have closed-form expressions, or only require solving a one-dimensional root finding problem.
Through numerical experiments, we demonstrate how to optimize for nested flux surface geometry, quasisymmetry, magnetic well, and the position and even the type (elliptic, hyperbolic, parabolic) of divertor fixed point. We showcase a set of single and double null, hyperbolic and parabolic divertors, and for the first time, we show that non-axisymmetric snowflake divertors (a special subset of six-legged parabolic divertors) can be achieved in a stellarator.Figure1shows five devices designed with the methods in this paper, including single-null, double-null, and triple-null X-point divertors, a parabolic single-null divertor, and a snowflake.Figure 1:STAR_Lite class stellarators featuring various kinds of divertors, designed using the algorithms in this work.
The top row shows the magnetic surface on a field period, the six modular coils with the vacuum vessel geometry (gray).
The middle row shows Poincaré sections of the devices in theϕ=0\phi=0plane, with stable and unstable manifolds in red and blue.
The bottom row depicts the connection lengthLcL_{c}atϕ=0\phi=0of each device.
The black circle constitutes the vacuum vessel.

An indirect method of “optimizing” the edge for an island divertor is equilibrium (“stage one”) optimization, by controlling theι\iotaprofile within the confined region, since magnetic islands depend on a low-order rationalι\iotaand the magnetic shear at this location[78,33,5,42,56]. Such an approach can be used to approximately fix the location and width of the magnetic island chain, but cannot (for example) control the phase of the island chain, i.e., the poloidal location of the magnetic islands.
In addition, the island size and degree of magnetic chaos also depend upon the radial magnetic field (i.e. resonant perturbations) with respect to a set of hypothetical nested surfaces in the edge, which depends on the coils rather than the magnetic equilibrium. Another way to optimize island size is by targeting Greene’s residue for X- and O-points in the island; for example, shrinking islands in the confined region by minimizing the residue[29]. On the experimental side, the island size in W7-X is routinely adjusted using windowpane-shaped magnetic coils[3,12], and more recently exotic edge configurations (“giant islands”) have been proposed in W7-X and HSX, based on empirical simulation results[9]. Non-island divertor edge optimization includes controlling stellarator equilibria to have high-curvature on the boundary[28]or targeting fixed points directly using a𝐁×d​𝐥\mathbf{B}\times d\mathbf{l}minimization[21].

The remainder of the paper is organized as follows. Insection3we introduce a well-conditioned spectral method for computing periodic field lines and their fixed points, regardless of type (elliptic, hyperbolic, or parabolic).Section5presents a family of vacuum vessel geometries whose signed distance functions can be evaluated rapidly. Insection6we combine these ingredients into a single framework that jointly optimizes the modular coils, divertor fixed points, and vacuum vessel.Section7presents representative configurations.

## 2Periodic field lines

Periodic field lines of the magnetic field, beyond the region of nested flux surfaces, are the basis of the magnetic structures that enable diversion of ash particles to divertor plates. In this section, we review how these field lines are computed as fixed points of a Poincaré return map, and how the trace of the return map’s Jacobian classifies each fixed point as hyperbolic, elliptic, or parabolic, resulting in distinct divertor structures. The mathematics introduced here sets the stage for the numerical methods described insection3for computing fixed points.

## 2.1Field line equations and the tangent map

A closed field line, parametrized to have uniform incremental arclength, satisfies the ordinary differential equation (ODE)𝐫f​(t):=𝚪′​(t)L−𝐁​(𝚪​(t))‖𝐁​(𝚪​(t))‖=0,\displaystyle\mathbf{r}_{f}(t)=\frac{\bm{\Gamma}^{\prime}(t)}{L}-\frac{\mathbf{B}(\bm{\Gamma}(t))}{\|\mathbf{B}(\bm{\Gamma}(t))\|}=0,(1)𝚪​(0)=𝚪0\displaystyle\bm{\Gamma}(0)=\bm{\Gamma}_{0}

where𝚪​(t)=[x​(t),y​(t),z​(t)]\bm{\Gamma}(t)=[x(t),y(t),z(t)]is the Cartesian coordinates of the field line,LLis the (constant) length of the field line from its start until it closes on itself,𝚪0=[Γ0,x,Γ0,y,Γ0,z]\bm{\Gamma}_{0}=[\Gamma_{0,x},\Gamma_{0,y},\Gamma_{0,z}]is the initial field line position, andt∈[0,tp)t\in[0,t_{p})parameterizes the curve, wheretp=1/nfpt_{p}=1/n_{\text{fp}}is the period. While it is common to expresseq.1in cylindrical coordinates(R​(ϕ),ϕ,Z​(ϕ))(R(\phi),\phi,Z(\phi)), we opt for the more general Cartesian representation, which affords us more flexibility when handling strongly shaped devices and their field lines.
Computing periodic field lines can be cast as searching for roots of the displacement map,𝑫​(𝚪0,L):\displaystyle\bm{D}(\bm{\Gamma}_{0},L):=𝚪​(tp;𝚪0,L)−𝓡​(tp)​𝚪0=0,\displaystyle=\bm{\Gamma}(t_{p};\bm{\Gamma}_{0},L)-\bm{\mathcal{R}}(t_{p})\bm{\Gamma}_{0}=0,(2)Γ0,y\displaystyle\Gamma_{0,y}=0,\displaystyle=0,

where𝚪​(t)\bm{\Gamma}(t)is governed by (1),𝓡​(t)\bm{\mathcal{R}}(t)is the standard rotation matrix about theZZ-axis by the angle2​π​t2\pi t, and the field line is launched from theX​ZXZ-plane.

Differentiatingeq.1with respect to the initial position of a fixed point,𝚪​(0)\bm{\Gamma}(0), gives the forward sensitivity equation:1L​𝚽′​(t)−(𝑰−𝐁‖𝐁‖​𝐁T‖𝐁‖)​∇𝐁‖𝐁‖​𝚽​(t)\displaystyle\frac{1}{L}\bm{\Phi}^{\prime}(t)-\left(\bm{I}-\frac{\mathbf{B}}{\|\mathbf{B}\|}\frac{\mathbf{B}^{T}}{\|\mathbf{B}\|}\right)\frac{\nabla\mathbf{B}}{\|\mathbf{B}\|}\bm{\Phi}(t)=0,\displaystyle=0,(3)𝚽​(0)\displaystyle\bm{\Phi}(0)=𝑰.\displaystyle=\bm{I}.

The solution𝚽\bm{\Phi}after one period,𝚽​(tp)=∂𝚪​(tp)/∂𝚪​(0)∈ℝ3×3\bm{\Phi}(t_{p})=\partial\bm{\Gamma}(t_{p})/\partial\bm{\Gamma}(0)\in\mathbb{R}^{3\times 3}, is known as the “tangent map”.
Although𝚪​(t)\bm{\Gamma}(t)is periodic,𝚽​(t)\bm{\Phi}(t)may not be, since field lines near the fixed point are not periodic in general.
Numerically, this implies thateq.3should be solved with a Chebyshev collocation method, rather than a Fourier collocation method.
Projecting the tangent map onto the plane orthogonal to the fixed point, spanned by the normal and binormal Frenet-Serret vectors𝐧,𝐛\mathbf{n},\mathbf{b}, gives the tangent map𝑴∈ℝ2×2\bm{M}\in\mathbb{R}^{2\times 2}𝑴=[𝐧​(tp),𝐛​(tp)]T​𝚽​(tp)​[𝐧​(0),𝐛​(0)].\bm{M}=[\mathbf{n}(t_{p}),\mathbf{b}(t_{p})]^{T}\bm{\Phi}(t_{p})[\mathbf{n}(0),\mathbf{b}(0)].(4)

𝑴\bm{M}is the Jacobian of the return map, and can be used to construct an approximate Poincaré section in the plane orthogonal to𝚪′​(0)\bm{\Gamma}^{\prime}(0), in the neighborhood of the fixed point att=0t=0. The position of a field line aftertpt_{p}when launched from𝚪​(0)+[𝐧​(0),𝐛​(0)]​𝜹0\bm{\Gamma}(0)+[\mathbf{n}(0),\mathbf{b}(0)]\bm{\delta}_{0}, for small𝜹0∈ℝ2\bm{\delta}_{0}\in\mathbb{R}^{2}, is approximated by𝚪​(k​tp)+[𝐧​(k​tp),𝐛​(k​tp)]​𝜹k\bm{\Gamma}(kt_{p})+[\mathbf{n}(kt_{p}),\mathbf{b}(kt_{p})]\bm{\delta}_{k}, where𝜹k\bm{\delta}_{k}follows the linear recurrence,𝜹k+1=𝑴​𝜹k.\displaystyle\bm{\delta}_{k+1}=\bm{M}\bm{\delta}_{k}.(5)

As a result ofeq.5, field line dynamics can be understood by analyzing the tangent map𝑴\bm{M}.
As we will discuss inSection2.2, the trace of𝑴\bm{M}is a useful classifier of different “flavors” of periodic orbits that can be used to design divertors.

## 2.2Types of diverting fixed points

The Hamiltonian nature of the field line equations guaranteesdet(𝑴)=1\det(\bm{M})=1, by the Abel-Liouville theorem. The eigenvalues of𝑴\bm{M}are thus only determined by the trace. We now describe a classification of the different types of fixed points based onTr​(𝑴)\text{Tr}(\bm{M}). Each class constitutes a different type of divertor, such as an island or an X-point.

Fixed points with|Tr​(𝑴)|>2|\text{Tr}(\bm{M})|>2are known as hyperbolic. Also known as X-points, hyperbolic fixed points are the basis of tokamak-like divertors (fig.1: columns 1-3). Particles nearby the X-point are diverted along its “legs”: eigenvectors of𝑴\bm{M}along which nearby field lines are attracted to or repelled from the fixed point. The eigenvalues of𝑴\bm{M}give the exponential rate of attraction or repulsion near the fixed point.

Island divertors route exhaust through island chains whose O-points are elliptic fixed points –|Tr​(𝑴)|<2|\text{Tr}(\bm{M})|<2. At an elliptic fixed point,𝑴\bm{M}is similar to a rotation matrix, i.e. has eigenvaluesλ±=e±i​α\lambda_{\pm}=e^{\pm i\alpha}, and repeated iterates of the mapping trace an ellipse.
As a result,𝑴\bm{M}is similar to a rotation matrix with rotation angleα\alpha,𝑴=𝑺1​(cos⁡(α)sin⁡(α)sin⁡(α)cos⁡(α))​𝑺.\bm{M}=\bm{S}^{\sm 1}\begin{pmatrix}\cos(\alpha)&\sm\sin(\alpha)\\
\sin(\alpha)&\cos(\alpha)\end{pmatrix}\bm{S}.

The rotational transform, or pitch of field lines at the fixed point, is given by the formula[35]ι=nfp2​π​α.\iota=\frac{n_{\text{fp}}}{2\pi}\alpha.(6)

Parabolic fixed points lie on the boundary between the elliptic (|Tr​(𝑴)|<2|\text{Tr}(\bm{M})|<2) and hyperbolic (|Tr​(𝑴)|>2|\text{Tr}(\bm{M})|>2) regimes, with|Tr​(𝑴)|=2|\text{Tr}(\bm{M})|=2. Parabolic fixed points may not be isolated; for example, every point on a rational-ι\iotasurface is a parabolic fixed point of the return map.
When used as part of a divertor, the fixed point is designed to be isolated.
In this work, we give special attention to fixed points withTr​(𝑴)=+2\text{Tr}(\bm{M})=+2, and further classify them by the rank of the linearized displacement map𝑴−𝑰\bm{M}-\bm{I}:rank-1 parabolic fixed pointshave𝑴≠𝑰\bm{M}\neq\bm{I}(Figure1: column 4) andrank-0 parabolic fixed pointshave𝑴=𝑰\bm{M}=\bm{I}. Rank-0 parabolic fixed points can have two or six legs protruding from the fixed point (Figure2A,Figure1: column 5).
Those with six legs are known assnowflakes, as shown inFigure2B.
Parabolic fixed points are also known as degenerate roots of the displacement map (2), since the Jacobian at the root is not full rank.
At an isolated fixed point,
the tangent map,𝑴\bm{M}, is insufficient for characterizing the manifolds of the nonlinear map in the neighborhood of the fixed point.
We will not explore reflection-hyperbolic (Tr​(𝑴)<2\text{Tr}(\bm{M})<\sm 2[13]) or negative parabolic (Tr​(𝑴)=2\text{Tr}(\bm{M})=\sm 2) fixed points in this work.

Figure 2:Stellarators exhibitingrank​(𝑴−𝑰)=0\text{rank}(\bm{M}-\bm{I})=0parabolic fixed points. Panel A shows a two-legged fixed point (horizontal diamond) with two orbiting X-points (crosses), and panel B shows a six-legged fixed point (star).

## 3A spectral method for computing fixed points

We now describe methods for numerically computing fixed points of any type: hyperbolic, elliptic, and parabolic. The computations rely on treatingeq.1as a nonlinear root-finding problem. When the fixed point is elliptic or hyperbolic, the Jacobian of the root-finding problem is well-conditioned and can be solved with Newton’s method. Systems with parabolic fixed points have a singular Jacobian; to apply Newton’s method, we introduce additional equations that stabilize the system. We begin by discussing a method for computing hyperbolic and elliptic fixed points. In both cases, the solution of the fixed point system can be differentiated with respect to system parameters using an adjoint method, making it amenable to gradient-based stellarator optimization.

## 3.1Computing hyperbolic and elliptic fixed points

In this section, we outline a numerical method for computing elliptic and hyperbolic fixed points.
This is done by solving (1) using a spectral collocation method with Newton’s method.

The fixed point curve is parameterized using theCurveXYZFourierSymmetriesrepresentation inSIMSOPT[54], originally proposed in[45]. This curve parametrization can efficiently represent stellarator symmetric andnfpn_{\text{fp}}-periodic field lines. The parametrization expresses𝚪​(t)=[x​(t),y​(t),z​(t)]\bm{\Gamma}(t)=[x(t),y(t),z(t)],t∈[0,1)t\in[0,1)as:x^​(t)\displaystyle\hat{x}(t)=x^c,0+∑m=1NFx^c,m​cos⁡(2​π​m​nfp​t)+x^s,m​sin⁡(2​π​m​nfp​t)\displaystyle=\hat{x}_{c,0}+\sum_{m=1}^{N_{F}}\hat{x}_{c,m}\cos(2\pi mn_{\text{fp}}t)+\hat{x}_{s,m}\sin(2\pi mn_{\text{fp}}t)(7)y^​(t)\displaystyle\hat{y}(t)=y^c,0+∑m=1NFy^c,m​cos⁡(2​π​m​nfp​t)+y^s,m​sin⁡(2​π​m​nfp​t)\displaystyle=\hat{y}_{c,0}+\sum_{m=1}^{N_{F}}\hat{y}_{c,m}\cos(2\pi mn_{\text{fp}}t)+\hat{y}_{s,m}\sin(2\pi mn_{\text{fp}}t)z​(t)\displaystyle z(t)=zc,0+∑m=1NFzc,m​cos⁡(2​π​m​nfp​t)+zs,m​sin⁡(2​π​m​nfp​t),\displaystyle=z_{c,0}+\sum_{m=1}^{N_{F}}z_{c,m}\cos(2\pi mn_{\text{fp}}t)+z_{s,m}\sin(2\pi mn_{\text{fp}}t),

where the coordinates forx​(t),y​(t)x(t),y(t)are:[x​(t)y​(t)]=𝓡​(t)​[x^​(t)y^​(t)].\begin{bmatrix}x(t)\\
y(t)\\
\end{bmatrix}=\bm{\mathcal{R}}(t)\begin{bmatrix}\hat{x}(t)\\
\hat{y}(t)\end{bmatrix}.(8)

For non-stellarator symmetric curves, this curve parametrization has3​(2​NF+1)3(2N_{F}+1)Fourier harmonics, also called degrees of freedom for the optimization.
For stellarator symmetric curves, the symmetry breaking harmonics are omitted from (1), i.e.,x^​(t)\hat{x}(t)only has cosine harmonics, whiley^​(t)\hat{y}(t),z​(t)z(t)only have sine harmonics, resulting in3​NF+13N_{F}+1degrees of freedom.

To apply the spectral collocation method,eq.1is discretized by evaluating the residuals at collocation points,tk=k​tp/(2​NF+1)t_{k}=k\,t_{p}/(2N_{F}+1)fork=0,1,…,2​NFk=0,1,\ldots,2N_{F},𝐫f​(tk;𝐱)=0​for​k=0,1,…,2​NF,\mathbf{r}_{f}(t_{k};\mathbf{x})=0\text{ for }k=0,1,\ldots,2N_{F},(9)

where𝐱\mathbf{x}are the Fourier harmonics in (7), (8), and the curve position,𝚪​(t)\bm{\Gamma}(t), is evaluated using the parametrization (8).

When the magnetic field is not-stellarator symmetric, the curve is not fully specified by this system of residuals, so we introduce an additional constraint on the field line:y​(0)=0y(0)=0, resulting in3​(2​NF+1)+13(2N_{F}+1)+1equations.
When the magnetic field is stellarator symmetric,y​(0)=0y(0)=0is always satisfied by the parametrization, thus this additional equation is not added to the system. In addition, theXX-component of the residual fort=0t=0is always zero:rx​(0)=0r_{x}(0)=0, regardless of the curve harmonics, because for a stellarator symmetric curve and stellarator symmetric field,Bx​(𝚪​(0))=0B_{x}(\bm{\Gamma}(0))=0impliesx′​(0)=0x^{\prime}(0)=0. Lastly, half of the remaining residual equations are redundant due to stellarator symmetry, since𝐫f​(tk)=[rf,x​(tk),rf,y​(tk),rf,z​(tk)]=[rf,x​(tk),rf,y​(tk),rf,z​(tk)]\mathbf{r}_{f}(\sm t_{k})=[r_{f,x}(\sm t_{k}),r_{f,y}(\sm t_{k}),r_{f,z}(\sm t_{k})]=[\sm r_{f,x}(t_{k}),r_{f,y}(t_{k}),r_{f,z}(t_{k})]. Removing these unnecessary equations, we are left with only3​NF+23N_{F}+2independent residuals.
ConsideringLLto be unknown in (1), the total number of unknowns is3​(2​NF+1)+13(2N_{F}+1)+1and3​NF+23N_{F}+2in the non-stellarator symmetric and stellarator symmetric cases, respectively.
In both cases, (9) along with the mentioned modifications result in a balanced system of nonlinear equations and unknowns, which we solve using Newton’s method.

## 3.2Numerically approximating parabolic fixed points

When the fixed point is parabolic, the Jacobian of the systemeq.9can be singular or poorly conditioned.
When applied to systems with singular Jacobians, Newton’s method can converge with only linear accuracy[86], and may be prone to diverging[36].
Moreover, using the fixed point solver within a stellarator optimization loop requires discretely exact derivatives of the fixed point position with respect to the design variables, which are challenging to accurately compute when the fixed point is degenerate. To address these shortcomings, we augment the system of equations with additional constraints that increase the rank of the Jacobian.

We illustrate the source of this ill-conditioning with a simple example. Consider searching for a fixed point at cylindricalϕ=0\phi=0in the(R,Z)(R,Z)plane by solving for(R0,Z0)(R_{0},Z_{0})such that𝐃​(R0,Z0)=(R​(tp,R0,Z0)−R0Z​(tp,R0,Z0)−Z0)=0,\mathbf{D}(R_{0},Z_{0})=\begin{pmatrix}R(t_{p},R_{0},Z_{0})-R_{0}\\
Z(t_{p},R_{0},Z_{0})-Z_{0}\end{pmatrix}=0,(10)

whereR​(tp,R0,Z0),Z​(tp,R0,Z0)R(t_{p},R_{0},Z_{0}),Z(t_{p},R_{0},Z_{0})denote the position of the field line launched from(R0,Z0)(R_{0},Z_{0})after one field period. Newton’s method relies on the Jacobian of (10), given by𝐉​(R0,Z0)=(∂R/∂R0∂R/∂Z0∂Z/∂R0∂Z/∂Z0)−𝑰=𝑴−𝑰.\mathbf{J}(R_{0},Z_{0})=\begin{pmatrix}\partial R/\partial R_{0}&\partial R/\partial Z_{0}\\
\partial Z/\partial R_{0}&\partial Z/\partial Z_{0}\end{pmatrix}-\bm{I}=\bm{M}-\bm{I}.(11)

The first term in the Jacobian is the tangent map𝑴\bm{M}at the solution in theR​ZRZ-plane; the𝐧,𝐛\mathbf{n},\mathbf{b}representation is given ineq.4and the two representations of𝑴\bm{M}have the same trace and determinant.
Given thatdet(𝑴)=1\det(\bm{M})=1and definingT=Tr​(𝑴)T=\text{Tr}(\bm{M}), the eigenvalues ofeq.11areT/2−1±T2−4/2T/2-1\pm\sqrt{T^{2}-4}/2, i.e., two zero eigenvalues whenT=2T=2.

Degenerate roots of nonlinear equations can still be computed with Newton’s method. To make the system well conditioned, we augment the base system of equations with additional constraints and degrees of freedom which stabilize the system[37].
We use two, more general, formulations to compute fixed points when the Jacobian of (9) is ill-conditioned or even singular in the neighborhood of parabolic fixed points. Both formulations require that some degrees of freedom, which can shape the magnetic field near the fixed point, be reserved as dependent degrees of freedom. The dependent degrees of freedom are solved for, jointly with the position of the fixed point, to ensure a fixed point of the desired type exists. In all numerical experiments, we introduce auxiliary poloidal field (PF) coils. The currents and positions of the PF coils are selected to ensure the fixed point exists.

The first formulation for stabilizing the fixed point equations is capable of computing parabolic fixed points, aside from those with𝑴=𝑰\bm{M}=\bm{I}, i.e. snowflakes. While this formulation is slightly more limited than the second, it offers simplicity. The second formulation is completely general and can be used to compute fixed points of all types. In the first formulation, the standard fixed point equations,eq.9, are augmented with the trace condition,Tr​(𝑴​(𝜼))\displaystyle\text{Tr}(\bm{M}(\bm{\eta}))=T,\displaystyle=T,(12)

whereT=2T=2when considering parabolic fixed points. The vector𝜼\bm{\eta}represents additional degrees of freedom for shaping the magnetic field and balancing the system of equations, which we will discuss momentarily. As noted earlier, the additional conditioneq.12does not stabilize the system when𝑴=𝑰\bm{M}=\bm{I}. In this case, the derivative of the trace conditioneq.12with respect to the axis position is zero; a result ofdet(𝑴)=1\det(\bm{M})=1. Due to this restriction, we introduce the more general, second formulation.
The second formulation augments the base discretization,eq.9, with four equations,Mi,j​(𝜼)\displaystyle M_{i,j}(\bm{\eta})=mi,j,i,j=1,2\displaystyle=m_{i,j},~i,j=1,2(13)

where the four valuesM1,1,M1,2,M2,1,M2,2M_{1,1},M_{1,2},M_{2,1},M_{2,2}are the entries of𝑴\bm{M}, andm1,1,m1,2m_{1,1},m_{1,2},m2,1,m2,2m_{2,1},m_{2,2}are their associated target values.
In practice, we do not need to constrain the fourth entry of𝑴\bm{M}since it is fixed bydet(𝑴)=1\det(\bm{M})=1. If the field line is stellarator symmetric, thenM1,1=M2,2M_{1,1}=M_{2,2}so we do not need to constrain one of the diagonal entries.

The degrees of freedom𝜼\bm{\eta}are introduced to build a balanced system and to introduce enough flexibility in shaping the magnetic field that a fixed point can be found. In the first formulation, only one additional degree of freedom is necessary to balance the one new equation,eq.12, and in the second formulation, only two additional degrees of freedom are needed. To achieve sufficient flexibility in shaping the magnetic field, it is recommended to add even more degrees of freedom, such that the system is underdetermined. In practice, we add one or more PF coils, and let𝜼\bm{\eta}represent their current, radii, and vertical position. It may be preferable to instead use toroidal field coils, windowpane coils, or some of the modular coils as degrees of freedom.
Although the Jacobian of underdetermined systems has a null-space, one can still take a Newton step using the pseudo-inverse of the Jacobian without sacrificing performance.

With the additional equations and degrees of freedom, Newton’s method can now be applied to the joint system,eq.9with eithereq.12oreq.13. InFigure3F, we show that the condition number of the Jacobian stays finite and bounded during the solve, unlike when solvingeq.9directly.Figure4D shows an example of using the second formulation to manipulate a snowflake while maintaining a well-conditioned nonlinear solve.

## 4Examples of computing parabolic fixed points

In this section, we walk through two numerical examples to showcase the capability of the methods introduced inSection3, and to demonstrate that they are numerically stable. Starting from an initial stellarator, we perform a continuation on the trace of a fixed point through the marginal parabolic limit, pushing the fixed points through bifurcation, converting it from one type to another. Insection4.1, O-points are converted to X-points, and insection4.2a broken snowflake is healed, then converted to an elliptic fixed point. This conversion capability is useful to the STAR_Lite experiment so that various fixed points or fixed point clusters might be studied experimentally, or imperfect snowflakes might be polished by slight modifications of the PF coil currents.

## 4.1Computing rank-1 parabolic fixed points

In this section, we use formulation one, introduced insection3, to compute almost-parabolic and exactly parabolic rank-1 fixed points.
We track a fixed point over the course of a continuation, converting it from an elliptic fixed point to a parabolic, then to a hyperbolic, all by modifying the currents in auxiliary PF coils.Figure 3:Condition numbers of the Jacobian of (14a) associated to the magnetic axis (blue), of (14b) associated to the tracked fixed point (purple dashed), and of the full system (14) (purple solid) as the target traceTTof the tracked fixed point is varied.
Circle, cross, square markers correspond respectively to O, X, and parabolic fixed points.
Panel B contains the Z-coordinate of the fixed points illustrating the bifurcation.
Panel C contains a Poincaré section, showing the full, non-stellarator symmetric device for when the traceT=1.9T=1.9.
Poincaré sections of the boxed region infig.3C at the target trace value of the tracked fixed point is varied about the bifurcation point.

The example uses a stellarator with modular coils and auxiliary PF coils. The modular coil currents and geometries are fixed throughout the example and are only used to generate a suitable background magnetic field to be modified by auxiliary PF coils. The PF coil geometries are also fixed, while the PF coil currents𝐈PF\mathbf{I}_{\text{PF}}are varied to generate the desired fixed point.
At each step of the continuation, we solve𝐫f​(𝐱,𝐈PF)\displaystyle\mathbf{r}_{f}(\mathbf{x},\mathbf{I}_{\text{PF}})=0,\displaystyle=0,(14a)𝐫f​(𝐭,𝐈PF)\displaystyle\mathbf{r}_{f}(\mathbf{t},\mathbf{I}_{\text{PF}})=0,\displaystyle=0,(14b)Tr​(𝑴​(𝐱,𝐈PF))\displaystyle\text{Tr}\!\left(\bm{M}(\mathbf{x},\mathbf{I}_{\text{PF}})\right)=1.6,\displaystyle=1.6,(14c)Tr​(𝑴​(𝐭,𝐈PF))\displaystyle\text{Tr}\!\left(\bm{M}(\mathbf{t},\mathbf{I}_{\text{PF}})\right)=T,\displaystyle=T,(14d)

where𝐱\mathbf{x}and𝐭\mathbf{t}are degrees of freedom associated to the magnetic axis and the tracked fixed point, respectively.𝐱,𝐭,𝐈PF\mathbf{x},\mathbf{t},\mathbf{I}_{\text{PF}}are varied to solve the system. The continuation varies the trace of the tangent map,TT, from its originalT=1.5T=1.5to2.02.0, all the way up to2.52.5(fig.3), while maintaining the trace of the magnetic axis at1.61.6to prevent destroying the volume of nested flux surfaces.
The system,eq.14, has3​(2​NF+1)+13(2N_{F}+1)+1field line constraints and two additional trace conditions.
It also has3​(2​NF+1)+13(2N_{F}+1)+1unknowns defining the field line andNPFN_{\text{PF}}unknowns that are the PF coil currents.
In this example, there areNF=16N_{F}=16Fourier harmonics per field line andNPF=5N_{\text{PF}}=5PF coils, resulting in 202 equations and 205 unknowns. That is, the system is underdetermined by construction, leaving ample freedom to satisfy the trace requirements.

Figure3(A-E) show a sequence of Poincare sections over the course of the continuation.Figure3(A, H) captures the initial state of the tracked fixed point, the purple circle with traceT=1.9T=1.9; the fixed point is elliptic, centered between two hyperbolic X-points. As the trace of the tracked fixed point approachesT=2T=2(Figure3A-B), the island width shrinks. When the trace equals 2.0 exactly, as inFigure3(C), the bottom X-point and tracked O-point merge to become a rank-1 parabolic fixed point.Figure3(D) shows the tracked fixed point becomes hyperbolic, and a transient elliptic fixed point appears (black dot) through a transcritical bifurcation.
Finally, inFigure3(D-E) the transient elliptic fixed point annihilates with the upper X-point collapsing to a single hyperbolic fixed point through a saddle-node bifurcation.
This rich behavior illustrates the control potential of this approach, and the complexity of stellarator divertor design.

Figure3(F) shows that over the course of the continuation, the condition number (ratio of largest and smallest singular values) of the underdetermined Jacobian is well-behaved at the parabolic limit as well as in its neighborhood. In contrast, the condition number of the Jacobian associated with just the field line system,eq.14b, is not, blowing up as the system approaches the parabolic fixed point.Figure3(G) prints the Z-coordinate of the different fixed points as they evolve and interact over the course of the continuation, showing a signal of the bifurcation.

## 4.2Snowflake: a rank-0 parabolic fixed point

We now show an example of how formulation two, introduced inSection3, can be used to compute a snowflake: a rank-0 parabolic fixed point with𝑴=𝑰\bm{M}=\bm{I}. As inSection4.1, we perform a continuation on the trace of𝑴\bm{M},TT. The condition number of the Jacobian used in Newton’s method remains well conditioned as the snowflake appears,T=2T=2. Similar toSection4.1, we use fixed modular coils to produce a background magnetic field, while letting the currents in auxiliary PF coils vary to maintain existence of the fixed point.

Snowflakes in tokamaks are typically defined as configurations for which both the poloidal magnetic field and its first derivative vanishes[77], i.e.𝐁pol=∇𝐁pol=0\mathbf{B}_{\text{pol}}=\nabla\mathbf{B}_{\text{pol}}=0. This is typically obtained in practice by pushing two X-points “on top of each other” (that is, the snowflake could be considered the limit of taking two nearby X-points (and zero O-points) and making their separation vanish).
For stellarators, a necessary condition to observe a snowflake is𝑴=𝑰\bm{M}=\bm{I}.
The topological index of such a fixed point is2\sm 2(i.e. the winding number calculation taken around the snowflake would be2\sm 2. From a distance, the snowflake has the same topological characteristic as two X-points, or three X-points and an O-point. As is observed infig.4, asTTincreases or decreases fromT=2T=2, the snowflake will “unfold” into these topologically equivalent states.

To observe the unfolding of a snowflake, we solve the following problem at each iteration of a continuation,𝐫f​(𝐱,𝐈PF)\displaystyle\mathbf{r}_{f}(\mathbf{x},\mathbf{I}_{\text{PF}})=0,\displaystyle=0,(15a)𝐫f​(𝐭,𝐈PF)\displaystyle\mathbf{r}_{f}(\mathbf{t},\mathbf{I}_{\text{PF}})=0,\displaystyle=0,(15b)Tr​(M​(𝐱,𝐈PF))\displaystyle\text{Tr}\!\left(M(\mathbf{x},\mathbf{I}_{\text{PF}})\right)=1.6,\displaystyle=1.6,(15c)𝑴​(𝐭,𝐈PF)\displaystyle\bm{M}(\mathbf{t},\mathbf{I}_{\text{PF}})=𝐦​(T),\displaystyle=\mathbf{m}(T),(15d)

where the target tangent map is chosen to satisfy𝐦​(T)={(T/24−T2/24−T2/2T/2)​if​T<2,(T/2+T2/4−100T/2−T2/4−1)​if​T≥2.\mathbf{m}(T)=\begin{cases}\begin{pmatrix}T/2&\sm\sqrt{4-T^{2}}/2\\
\sqrt{4-T^{2}}/2&T/2\end{pmatrix}\text{ if }T<2,\\
\\
\begin{pmatrix}T/2+\sqrt{T^{2}/4-1}&0\\
0&T/2-\sqrt{T^{2}/4-1}\end{pmatrix}\text{ if }T\geq 2.\end{cases}

WhenT=2T=2holds precisely,𝑴\bm{M}is the identity, and the fixed point corresponds to a snowflake. To make it simple to scan over values ofTT, we adopt the above parametrization of𝐦\mathbf{m}, though more general choices are possible whenT≠2T\neq 2.Figure 4:(A-C) Poincaré sections of the boxed region in (F) when the target trace value,TT, of the tracked fixed point is varied about the bifurcation point. (F) An expanded view of the Poincaré section shown in (B), where the blue dot labels the magnetic axis. (D) Condition numbers of the Jacobian ofeq.15aassociated with the magnetic axis (blue), ofeq.15bassociated with the tracked fixed point (purple dashed), and of the full systemeq.15(purple solid) as the target traceTTof the tracked fixed point is varied; the coupled system has a bounded condition number.
(E) TheR​(0)R(0)coordinates of the fixed points illustrating the bifurcation.
Circle, cross, star markers correspond respectively to O, X, and parabolic fixed points.

Figure4(A-C) shows Poincare sections over the course of the continuation. The continuation begins atT=1.95T=1.95inFigure4(A) where the elliptic fixed point is surrounded by three orbiting X-points. The snowflake appears asTTis increased toT=2T=2inFigure4(B), before splitting into two hyperbolic fixed points asTTis increased above 2.Figure4(F) shows an expanded view of the cross section with the snowflake.
InFigure4(D), we illustrate again how the standard discretization ofeq.9is ill-suited to finding parabolic fixed points. Without augmenting the system with additional degrees of freedom and constraints, the Jacobian is ill conditioned asT→2T\to 2. The Jacobian of the coupled systemeq.15, on the other hand, is well-conditioned in any regime.

## 4.3A chain of O-points

As a final exercise of these new numerical methods, we convert the bottom X-point infig.5A into an O-point, yielding a chain of O-points (fig.5B).
To convert aT>2T>2hyperbolic fixed point to aT<2T<2elliptic fixed point, the trace must pass through theT=2T=2parabolic limit. To do so, the continuation problem is augmented by enforcing a trace constraint for each periodic fixed pointfig.5A (the two elliptic points, and X-points).
Specifically, we solve𝐫f​(𝐱i,𝐈PF)\displaystyle\mathbf{r}_{f}(\mathbf{x}_{i},\mathbf{I}_{\text{PF}})=0,\displaystyle=0,(16a)𝐫f​(𝐭,𝐈PF)\displaystyle\mathbf{r}_{f}(\mathbf{t},\mathbf{I}_{\text{PF}})=0,\displaystyle=0,(16b)Tr​(𝑴​(𝐱i,𝐈PF))\displaystyle\text{Tr}\!\left(\bm{M}(\mathbf{x}_{i},\mathbf{I}_{\text{PF}})\right)=Ti,\displaystyle=T_{i},(16c)Tr​(𝑴​(𝐭,𝐈PF))\displaystyle\text{Tr}\!\left(\bm{M}(\mathbf{t},\mathbf{I}_{\text{PF}})\right)=T,\displaystyle=T,(16d)

wherei=1,2,3i=1,2,3indexes the three fixed points𝐱i\mathbf{x}_{i}whose traces are held at prescribed valuesTiT_{i}, while the bottom fixed point𝐭\mathbf{t}is continued by varying the target traceTTfrom 1.95 to 2.05, so that it transitions from hyperbolic to parabolic snowflake, then elliptic. System (16a) constrains three field line and trace conditions, resulting in 404 equations.
It also has 410 unknowns corresponding to the field line geometries andNPF=10N_{\text{PF}}=10PF coil currents.
Again, there is ample freedom in this underdetermined system to satisfy the requested traces as the tracked fixed point’s trace varies from 2.4 to 1.90.Figure 5:The tracked fixed point (purple) in panel A is converted from an X-point to an O-point in panel B, using a continuation. The traces of the tangent map for the remaining three fixed points in panel A are controlled to ensure they do not disappear. Converting the X-point into an O-point creates a divertor chain in panel B.

## 5Vacuum vessel designs with simple signed distance functions

Realistic stellarator designs have a vacuum vessel that neither intersects with the coils nor the divertor fixed points. To automate finding such a vessel, the vessel geometry can be treated as a degree of freedom during the optimization, and varied to satisfy the compatibility constraints. To efficiently compute distances from the fixed points to the vessel, we introduce a family of vacuum vessel geometries for which signed distances from points to the vessel have closed-form expressions, or only require solving a one-dimensional root finding problem. The signed distance functions (SDFs) are differentiable and can be used inside objective functions or constraints in an optimization of the design.

A signed distance function,ϱ​(𝐩;𝐯)\varrho(\mathbf{p};\mathbf{v}), is the minimum Euclidean distance from a point𝐩=(x,y,z)\mathbf{p}=(x,y,z)to the vesselΩ​(𝐯)\Omega(\mathbf{v}), signed by whether𝐩\mathbf{p}is inside or outside the volume. Explicitly,ϱ​(𝐩;𝐯)=sgn​(𝐩;Ω​(𝐯))​min𝐩∗∈Ω​(𝐯)⁡‖𝐩−𝐩∗‖,\varrho(\mathbf{p};\mathbf{v})=\text{sgn}(\mathbf{p};\Omega(\mathbf{v}))\min_{\mathbf{p}^{*}\in\Omega(\mathbf{v})}\|\mathbf{p}-\mathbf{p}^{*}\|,(17)

where𝐯=(v1,v2,…)\mathbf{v}=(v_{1},v_{2},\ldots)are degrees of freedom parameterizing the vessel.
Throughout, a semicolon separates the spatial coordinates from the vessel’s defining parameters,𝐯\mathbf{v}.
Points on the vessel are represented implicitly as the zero-level set ofϱ\varrho, i.e.{𝐩|ϱ​(𝐩;𝐯)=0}\{\mathbf{p}\,|\,\varrho(\mathbf{p};\mathbf{v})=0\}.
The vessel geometries used in this work have SDFs that are quick to compute and simple to implement. Because the SDF gives the distance to a parametrized geometry, the same machinery can also be used to parameterize ports and ensure clearance for port access[6].Figure 6:The three vacuum vessel families. Panels A and D show the pill pipe vessel, B and E the non-planar vessel, and C and F the piecewise-cylinder vessel realized as a loop of six mitred cylinders. A, B and C show the defining geometry (cross-section parameters for A, the centerline for B and C). D, E and F show the resulting three-dimensional vessels. The tube radiusrris indicated in the bottom row and the miter welds are highlighted in red in F.

A whole zoo of useful SDFs can be found in[69].
One family of surfaces that enables a quick SDF calculation is “canal surfaces”[67].
Such surfaces can be viewed as unions of spheres of radiusr​(t)r(t)swept along a three-dimensional curve𝐜​(t)\mathbf{c}(t).
By observing that the distance from𝐩\mathbf{p}to a sphere is‖𝐩−𝐜​(t)‖−r​(t)\|\mathbf{p}-\mathbf{c}(t)\|-r(t), it follows that the signed distance function at𝐩\mathbf{p}is the solution to the minimization problem:ϱcanal​(𝐩;𝐜,𝐫)=mint∈[0,1)⁡‖𝐩−𝐜​(t)‖−r​(t).\displaystyle\varrho_{\text{canal}}(\mathbf{p};\mathbf{c},\mathbf{r})=\min_{t\in[0,1)}\|\mathbf{p}-\mathbf{c}(t)\|-r(t).(18)

A few useful vessel shapes with closed form SDFs can be expressed as canal surfaces with simple choices ofc​(t),r​(t)c(t),r(t).
The first canal surface we examine is called the pill pipe.
The pill pipe is the envelope of spheres with constant radiusrrswept along a rounded rectangle of dimensions2​bx×2​by2b_{x}\times 2b_{y}and corner radiusrcr_{c}. These geometric parameters are illustrated inFigure6(A/D).
The SDF for the pill pipe has a closed-form expression that is independent oftt,ϱ​(x,y,z;r,bx,by,rc)=(∥(max⁡(ax,0),max⁡(ay,0))∥2+min⁡(max⁡(ax,ay),0)−rc)2+z2−r,\displaystyle\resizebox{390.25534pt}{}{$\displaystyle\varrho(x,y,z;r,b_{x},b_{y},r_{c})=\sqrt{\left(\big\lVert\big(\max(a_{x},0),\,\max(a_{y},0)\big)\big\rVert_{2}+\min\!\big(\max(a_{x},a_{y}),\,0\big)-r_{c}\right)^{2}+z^{2}}-r$},(19)ax=|x|−(bx−rc),ay=|y|−(by−rc).\displaystyle a_{x}=|x|-(b_{x}-r_{c}),\qquad a_{y}=|y|-(b_{y}-r_{c}).

The SDF remains valid when the side lengths of the rectangle and corner radius of the centerline are larger than the radius of the ball:bx−rc,by−rc,rc\displaystyle b_{x}-r_{c},b_{y}-r_{c},r_{c}>0,\displaystyle>0,(20)r\displaystyle r<rc.\displaystyle<r_{c}.

A special case of the pill pipe whenc​(t)c(t)is a circle of radiusRR(R=bx=by=rcR=b_{x}=b_{y}=r_{c}) is the simple toroidal vacuum vessel,ϱtorus​(x,y,z;R,r)=(x2+y2−R)2+z2−r.\displaystyle\varrho_{\text{torus}}(x,y,z;R,r)=\sqrt{(\sqrt{x^{2}+y^{2}}-R)^{2}+z^{2}}\,-r.(21)

The next canal surface defines a vessel with a non-planar centerline𝐜​(t)\mathbf{c}(t)swept by spheres with nonuniform radiir​(t)r(t), shown infig.6(B/E).
The formula for the radius is a standard Fourier series, and the centerline uses the same stellarator symmetric,nfpn_{\text{fp}}-periodic parametrization as the periodic field lineseq.7andeq.8.
The SDF takes the general form of a one-dimensional minimization problemeq.18, which can be solved robustly using a Newton’s method guarded by the bisection algorithm.
Constraints onc​(t),r​(t)c(t),r(t)are required to prevent ill-behaved geometries. First, we force that centerline to have uniform arc length, i.e.‖𝐜′​(t)‖\|\mathbf{c}^{\prime}(t)\|is constant, by requestingVart​[‖𝐜′​(t)‖]=0\mathrm{Var}_{t}\left[\|\mathbf{c}^{\prime}(t)\|\right]=0. Next, we enforce geometric conditions to prevent non-differentiable creases in the vessel: for eacht∈[0,tp)t\in[0,t_{p}), we must haver​(t)>0r(t)>0,r​(t)<(1−(r​(t)2)′′/2)/κ​(t)r(t)<(1-(r(t)^{2})^{\prime\prime}/2)/\kappa(t)and|r′​(t)|<‖𝐜′​(t)‖|r^{\prime}(t)|<\|\mathbf{c}^{\prime}(t)\|[62,92,67], whereκ​(t)\kappa(t)is the curvature of the centerline. In the case of the pill pipe vessel, these generic conditions simplify to (20). While these conditions prevent local self-intersections and creases, they do not prevent the vessel from global self-intersections, i.e. portions of the vessel that are distant in the parametertt, but close geometrically[62].

The final vessel shapes that we consider are formed by a sequence ofnsegn_{\mathrm{seg}}cylinders with radiusrrthat are glued together with the proper miter angle, shown infig.6(C/F). We call these “piecewise cylindrical” (PC) vessels. The centerline of the cylinders is defined by a periodic piecewise linear interpolant through anchor points, where the centerline inherits the field period and stellarator symmetry of the device. Due to the sharp corners at the joints of the cylinders, this vessel class is not an instance of canal surfaces.
The SDF for PC vessels requires solving a sequence of 1D minimizations, one per cylinder,ϱpc​(𝐩;𝐯)=sgn​(𝐩;𝛀​(𝐯))​min𝐩∗∈∂Ωk​(𝐯)k=1,…,nseg⁡‖𝐩−𝐩∗‖,\varrho_{\mathrm{pc}}(\mathbf{p};\mathbf{v})=\text{sgn}(\mathbf{p};\mathbf{\Omega}(\mathbf{v}))\,\min_{\begin{subarray}{c}\mathbf{p}^{*}\in\partial\Omega_{k}(\mathbf{v})\\
k=1,\ldots,n_{\text{seg}}\end{subarray}}\|\mathbf{p}-\mathbf{p}^{*}\|,(22)

where∂Ωk\partial\Omega_{k}is the boundary ofkkth cylinder, and the degrees of freedom are the vertices of the polyline and radius,𝐯=(x1,y1,z1,…,r)\mathbf{v}=(x_{1},y_{1},z_{1},\ldots,r).Figure6(C) depicts the geometric degrees of freedom and the turn anglesθk\theta_{k}.Equation22computes the distance from𝐩\mathbf{p}to thensegn_{\mathrm{seg}}mitered cylinders. This is equivalent to computing the minimum of the distance to thekkth infinite cylinder, and the two elliptic miter curves at the ends of the cylinder. Calculating the distance to an infinite cylinder has a simple closed form, but the distance to elliptical miters requires solving a nonlinear scalar equation which is described thoroughly in[16].Figure 7:Overview of the vacuum vessel geometries supported by our signed-distance-function approach, shown for real optimized devices. Columns, from left to right: torus, pill pipe, planar piecewise cylinder, non-planar, and non-planar piecewise cylinder. The top row shows configurations with the coils placed off the vessel, the bottom row with the coils on the vessel. The two simultaneously optimized unique modular coil filaments are shown in red and blue

We consider the PC vessel valid when the cylinders form a non-self-intersecting pipe. For a vessel defined by anchor points𝐱k=(xk,yk,zk)\mathbf{x}_{k}=(x_{k},y_{k},z_{k})and radiusrr, we require thatr>0r>0, the length of each cylinder be non-negative,ℓk=‖𝐱k−𝐱k+1‖>0\ell_{k}=\|\mathbf{x}_{k}-\mathbf{x}_{k+1}\|>0, each turn angleθk=arccos⁡((𝐱k−𝐱k−1)⋅(𝐱k+1−𝐱k)/(ℓk−1​ℓk))<θmax<180∘\theta_{k}=\arccos\!\Big((\mathbf{x}_{k}-\mathbf{x}_{k-1})\cdot(\mathbf{x}_{k+1}-\mathbf{x}_{k})/(\ell_{k-1}\,\ell_{k})\Big)<\theta_{\max}<180^{\circ}, and the two (elliptic) miters on each cylinder to not overlap, i.e.ℓk>r​[tan⁡(θk/2)+tan⁡(θk+1/2)]\ell_{k}>r[\tan(\theta_{k}/2)+\tan(\theta_{k+1}/2)].

In the special case of a PC vessel made up ofnseg=4n_{\mathrm{seg}}=4perpendicular cylinders with centerline that lies in the XY-plane (shown inFigure1(first column)), we can find a level-set function with a closed form expression. We use the term level-set function to highlight that the function is not an exact signed distance function; the zero-level set (ϱpc​(𝐩;𝐯)=0\varrho_{\mathrm{pc}}(\mathbf{p};\mathbf{v})=0) corresponds to the true vessel geometry, but in general, no longer provides a true distance to the vessel. In this case, the level set equation is,ϱpc​(x,y;bx,by)=max(|x|−bx,|y|−by)2+z2−r.\displaystyle\varrho_{\mathrm{pc}}(x,y;b_{x},b_{y})=\sqrt{\max\!\big(|x|-b_{x},\ |y|-b_{y}\big)^{2}+z^{2}}-r.(23)

Insection6, we show how these SDFs can be included in the optimization to design vacuum vessels that are compatible with the fixed points and coils.Figure1showcases five vessel geometries found using stellarator optimization over vessel geometries.
All the SDFs mentioned here are differentiable with respect to vessel shape parameters.
There are some instances when the nearest point on the vessel to𝐩\mathbf{p}is not unique, for example, when𝐩\mathbf{p}lies on the centerline,𝒄​(t)\bm{c}(t), of a canal vessel. When this occurs, the derivative of the SDF with respect to𝐩\mathbf{p}is not defined. While this could be problematic for a gradient-based stellarator optimization routine, it is not an issue as long as the optimizer does not query the spatial gradient through these problematic areas.
In practice, it did not prevent our algorithm from finding useful devices.
An overview of the various STAR_Lite class devices with compatible vacuum vessels are shown infig.7.

## 6Divertor and vacuum vessel direct optimization

In this section, we incorporate the differentiable methods for field line control (Section3) and vacuum vessel design (Section5) into a single framework to jointly design coils, divertor fixed points, and a vacuum vessel for a stellarator. The optimization must be initialized from a configuration where a divertor fixed point exists. Though not used here, we expect that a𝑩×d​𝒍\bm{B}\times d\bm{l}minimization[21]could be used to generate such an initialization if needed in future.

Our optimization formulation treats the vacuum vessel geometry as a degree of freedom with parameters𝐯\mathbf{v}, as well as any coil currents and geometries, specified by the vector𝐪\mathbf{q}. As discussed inSection5, we choose a vacuum vessel parameterization that admits a signed distance function,ϱ\varrho. The fixed point position𝚪divertor​(t;𝐪)\bm{\Gamma}_{\text{divertor}}(t\,;\mathbf{q})can be computed from the magnetic field using the techniques fromSection3. Additional degrees of freedom for shaping the magnetic field must be introduced in order to stabilize the computation; in all numerical experiments we introduce auxiliary PF coils with variable radii and currents.

When optimizing the divertor placement and vacuum vessel geometry, it is relevant to constrain the pairwise distances between the vessel, fixed-point, and coils. To that end, we include the following pairwise distances constraints in the joint optimization,dcoil-vessel≤ϱ​(𝚪coil​(t;𝐪);𝐯)≤Dcoil-vessel\displaystyle d_{\text{coil-vessel}}\leq\varrho\big(\bm{\Gamma}_{\text{coil}}(t\,;\,\mathbf{q});\,\mathbf{v}\big)\leq D_{\text{coil-vessel}}[coil-vessel distance](\theparentequation.1)ϱ​(𝚪divertor​(t;𝐪);𝐯)≤ddivertor-vessel\displaystyle\varrho\big(\bm{\Gamma}_{\text{divertor}}(t\,;\,\mathbf{q});\,\mathbf{v}\big)\leq d_{\text{divertor-vessel}}[divertor-vessel distance](\theparentequation.2)ϱ​(𝚪surface​(φ,θ;𝐪);𝐯)≤dsurface-vessel\displaystyle\varrho\big(\bm{\Gamma}_{\text{surface}}(\varphi,\theta\,;\,\mathbf{q})\,;\,\mathbf{v}\big)\leq d_{\text{surface-vessel}}[opt. surface-vessel distance](\theparentequation.3)Vart​[ϱ​(𝚪divertor​(t;𝐪);𝐯)]=0\displaystyle\mathrm{Var}_{t}[\varrho\big(\bm{\Gamma}_{\text{divertor}}(t\,;\,\mathbf{q})\,;\,\mathbf{v}\big)]=0[const. divertor-vessel distance](\theparentequation.4)Vart​[𝐞z⋅𝚪divertor​(t;𝐪)]=0\displaystyle\mathrm{Var}_{t}\big[\,\mathbf{e}_{z}\cdot\bm{\Gamma}_{\text{divertor}}(t\,;\,\mathbf{q})\,\big]=0[const. divertorZZ-coordinate](\theparentequation.5)

𝚪surface,𝚪coil\bm{\Gamma}_{\text{surface}},\bm{\Gamma}_{\text{coil}}are vectors representing the position of points on any flux surface, and coils, respectively.Equation\theparentequation.1constrains the pairwise distance between each coil and the vacuum vessel to be at leastdcoil-vesseld_{\text{coil-vessel}}and at mostDcoil-vesselD_{\text{coil-vessel}}. While the lower bound is used to satisfy packing constraints, the upper bound can be used to keep the coils close to the vessel, or even put the coils on the vessel, as shown inSection7.Equation\theparentequation.2ensures that the fixed point does not intersect with the vessel; sinceϱ\varrhois an SDF and the fixed point is on the interior of the vessel,ddivertor-vesseld_{\text{divertor-vessel}}is negative.Equation\theparentequation.3constrains the distance between a flux surface of the magnetic field and the vessel –dsurface-vesseld_{\text{surface-vessel}}is also negative.
The two variance constraintseqs.\theparentequation.4and\theparentequation.5additionally hold the divertor fixed point at a constant distance from the vessel and a constant vertical position as it winds toroidally. The variance is computed statistically at quadrature points on the divertor fixed point. Whileeqs.\theparentequation.4and\theparentequation.5are not strictly necessary, including them can simplify the process of designing divertor plates by keeping the divertor strikelines at fixed positions in a cross section.

When seeking a configuration with a parabolic fixed point, the optimization may be seeded with a configuration with an elliptic or hyperbolic fixed point. If the initial configuration has an elliptic or hyperbolic fixed point andTr​(𝑴)\text{Tr}(\bm{M})is far from22, then the additional degrees of freedom reserved for fixed point computation, may not have enough flexibility to convert the fixed point to parabolic. To remedy this, first we drive the configuration close to a parabolic fixed points to get an improved initial guess. Then the auxiliary degrees of freedom will have enough flexibility to ensure the parabolic fixed point can be found, so the spectral methods fromsection3can be applied using the exactTr​(𝑴)=2\text{Tr}(\bm{M})=2, or𝑴=𝑰\bm{M}=\bm{I}constraint. To find an improved initial configuration, we augment (24) with a constraint on the return map𝑴\bm{M}. We introduce the constraint,|Tr​(𝑴​(𝐜,𝐈,𝐱​(𝐜,𝐈)))−2|≤0.1|\text{Tr}(\bm{M}(\mathbf{c},\mathbf{I},\mathbf{x}(\mathbf{c},\mathbf{I})))-2|\leq 0.1(25)

when seeking rank-1 parabolic fixed points and‖𝑴​(𝐜,𝐈,𝐱​(𝐜,𝐈))−𝑰‖∞≤0.1\|\bm{M}(\mathbf{c},\mathbf{I},\mathbf{x}(\mathbf{c},\mathbf{I}))-\bm{I}\|_{\infty}\leq 0.1(26)

when seeking rank-0 parabolic fixed points.
The solutions to (24) augmented with exactly one of (25) or (26) correspond to stellarators whose divertors are close to parabolic in the desired subclass.
We use them as initial guesses in a final optimization restricted to the space of stellarators with perfectly parabolic divertors.

## 6.1Application to designing STAR_Lite-class stellarators

We now extend the optimization formulation beyond the basic pairwise distance constraints used for vacuum vessel and fixed point design,eq.24, to find STAR_Lite-class stellarators. The goal of the optimization is to find STAR_Lite scale stellarators with a quasisymmetric region of nested flux surfaces, a certain rotational transform, a magnetic well, a certain aspect ratio, a fixed point for a divertor, and a compatible vacuum vessel. Some configurations resulting from this optimization are shown insection7. To ensure the existence of a parabolic fixed point, when seeking one, one or more additional circular PF coils with variable radii, vertical position, and current are introduced.

The geometric constraints ineq.24are coupled with a standard stellarator coil design problem,min𝐪,𝐯\displaystyle\min_{\mathbf{q},\,\mathbf{v}}\quadfQA​(𝐪)\displaystyle f_{\mathrm{QA}}\big(\mathbf{q}\big)subject toι​(𝐪)=ιs∗\displaystyle\iota\big(\mathbf{q}\big)=\iota_{s}^{*}[opt. surface rotational transform](\theparentequation.1)ι​(𝐪)=ιa∗\displaystyle\iota\big(\mathbf{q}\big)=\iota_{a}^{*}[on-axis rotational transform](\theparentequation.2)A​(𝐪)=A∗\displaystyle A\big(\mathbf{q}\big)=A^{*}[aspect ratio of opt. surface](\theparentequation.3)∫01‖𝐁​(𝚪axis​(t;𝐪))‖​dt=B∗\displaystyle\int_{0}^{1}\big\|\mathbf{B}\big(\bm{\Gamma}_{\text{axis}}(t;\mathbf{q})\big)\big\|\,\mathrm{d}t=B^{*}[mean field strength](\theparentequation.4)Vart⁡[‖𝐁​(𝚪axis​(t;𝐪))‖]=0\displaystyle\operatorname{Var}_{t}\!\Big[\,\big\|\mathbf{B}\big(\bm{\Gamma}_{\text{axis}}(t\,;\,\mathbf{q})\big)\big\|\,\Big]=0[on-axis field variance](\theparentequation.5)W​(Ψ;𝐪)≤W∗\displaystyle W\big(\Psi\,;\,\mathbf{q}\big)\leq W^{*}[magnetic well](\theparentequation.6)|𝐈​(𝐪)|≤𝐈∗\displaystyle|\mathbf{I}(\mathbf{q})|\leq\mathbf{I}^{*}[coil current bound](\theparentequation.7)

The objectivefQA​(𝐪)f_{\mathrm{QA}}(\mathbf{q})measures deviation from quasisymmetry on a target optimization surface𝚪surface​(φ,θ;𝐪)\bm{\Gamma}_{\mathrm{surface}}(\varphi,\theta;\mathbf{q}), parameterized in Boozer coordinates, seeappendixB.
This flux surface is computed from the magnetic field using the “Boozer surface method”: a PDE with residual𝐫s​(𝐬,𝐪)=0\mathbf{r}_{s}(\mathbf{s},\mathbf{q})=0is solved, defining the mapping𝐬​(𝐪)\mathbf{s}(\mathbf{q})and the rotational transform on the surface. See[30,31]for a full treatment of the approach. The magnetic axis,𝚪axis​(t;𝐪)\bm{\Gamma}_{\text{axis}}(t;\mathbf{q}), is computed from the magnetic field using the spectral method fromsection3.

Equation\theparentequation.1fixes the rotational transform,ι\iota, on the target flux surface toιs∗\iota_{s}^{*}, andeq.\theparentequation.2fixesι\iotaon the magnetic axis via (6) toιa∗\iota_{a}^{*}. Together, these two constraints control the shear.Equation\theparentequation.3fixes the aspect ratio of the optimization surface to a targetA∗A^{*}.A∗A^{*}is set to that of STAR_Lite design A[40](A∗=6.66A^{*}=6.66), though the last closed flux surface might be lower aspect ratio.

The two field strength conditions,eq.\theparentequation.4andeq.\theparentequation.5, set the mean field strength on-axis to targetB∗=0.0875​TB^{*}=0.0875\mathrm{T}, and enforce on-axis quasisymmetry, respectively.Equation\theparentequation.6imposes a magnetic well, which is favorable for MHD interchange stability (seeappendixCfor details on how the well term is calculated).

Equation\theparentequation.7bounds each coil current by a coil-specific maximum collected in𝐈∗\mathbf{I}^{*}, where the absolute value and inequality act elementwise. Manufacturing constraints set the upper bound to60​kA⋅turns60~\mathrm{kA}\cdot\mathrm{turns}for the modular coils and we impose5​kA⋅turns5~\mathrm{kA}\cdot\mathrm{turns}for the PF coils when they are present.
We also impose additional geometric constraints on the vacuum vessel geometry, ensuring that it remains valid and non-self-intersecting; seesection5for these additional details.
We impose additional engineering constraints adopted by the STAR_Lite project[40]on uniform incremental arclength of the coils, coil-to-coil distance, maximum and mean-squared coil curvature, coil length, major radius. The complete problem, including these constraints and their bounds, is stated inappendixA.

Optimization is initialized from STAR_Lite design A, the baseline quasi-axisymmetric coil set of the STAR_Lite experiment[40]whose divertor is of X-point type, and solve (24) using a penalty method[65]. Sensitivities with respect to the coils and currents (𝐪\mathbf{q}) in all cases can be obtained using automatic differentiation. Note that we do not differentiate through the Newton solve. Rather, we form the adjoint system using JAX and compute discretely exact gradients using vector-Jacobian products.
The ODE and PDE constraints are imposed exactly, while a penalty method attempts to satisfy engineering and physics constraints to 0.1% accuracy when the target is nonzero, and 0.1 absolute error when the target is zero.

## 7Example configurations

In this section, we solve the optimization problem introduced insection6.1to design STAR_Lite class stellarators with novel divertor structures.
The devices differ in the divertor type, divertor location, vessel shape, and relative location of the coils: on the vessel or off the vessel, and whether there are PF coils or not.

Since a full characterization of the tool’s capabilities, as well as the physical implications of the resulting structures for a reactor, is far beyond the scope of this paper, we present only a small subset of the possible structures, along with a preliminary physical analysis.
To this end, we introduce four new configurations infig.8.
The first two are relatively simple double-null (DN) and single-null (SN) X-point divertors,fig.8(A-B). The remaining two examples showcase more exotic varieties, with panel (C) showing a parabolic single-null divertor and panel (D) a snowflake.
All four are two-field-period STAR_Lite class devices with six modular coils (blue and red in the top row offig.8), enclosed by a vacuum vessel with circular cross sections.
The parabolic and snowflake configurations additionally employ poloidal field (PF) coils, shown in orange and light blue, to shape and polish the diverting fixed point. Note that these five circular auxiliary coils are non-uniformly spaced.
While the double-null configuration retains stellarator symmetry, the single-null configurations necessarily break it: a diverting fixed point that sits only below (or only above) the plasma is incompatible with the up-down mirror symmetry that stellarator symmetry imposes on theϕ=0\phi=0cross section. As discussed below, this has consequences for how much of the device must be inspected when analyzing the scrape-off layer.Figure 8:(Top row) Four optimized stellarators with diverse diverting fixed point topologies.
The modular coils are displayed in blue and red, and the poloidal field coils are shown in orange and light blue.
The vacuum vessel is shown revealing the nested flux surfaces within.
(Bottom row) Connection lengthLcL_{c}on theϕ=0\phi=0cross section for the devices in the top row. The circular vessel cross section (solid line) also serves as the divertor target in this exercise, and the black dashed line is the cross section of the optimization surfaceΓ\Gammaon which quasisymmetry is targeted.

## 7.1Connection length and strike lines

The connection length plots (second row offig.8andfig.9) and strike-point plots (fig.10) were created using the FLARE library[23], which allows fast field line tracing and analysis. In both cases, the magnetic field is evaluated on a precomputed grid with256×256×128256\times 256\times 128points in(R,Z,ϕ)(R,Z,\phi)per field period. The connection length maps are computed by launching a field line from every node of a512×512512\times 512grid in(R,Z)(R,Z)on each cross section shown. Each field line is traced at most 50 m in both the forward and backward directions or until it hits the vessel, and the two lengths are summed to give the connection lengthLcL_{c}represented by the color bar gradient. At the major radiusR0=0.5R_{0}=0.5m, the 50 m cap corresponds to roughly 15 toroidal transits per direction, well beyond the connection lengths of the divertor legs, so it truncates only confined and near-confined field lines that never reach the wall.
The connection length maps in the second row offig.8share a common structure: a region of long connection length (Lc>100L_{c}>100m, saturated in the color bar) marks the confined core, which encloses the optimization surfaceΓ\Gammain all four configurations. Across the separatrix,LcL_{c}drops sharply, and the divertor legs are visible as narrow bands of intermediate connection length that guide the open field lines from the fixed point to the vessel wall. The distinct fixed-point topologies are clearly reflected in the leg structure: the double null exhibits the expected up-down symmetric pairs of legs, the single null and the parabolic configuration channel the exhaust into legs below the plasma, and the snowflake displays the characteristic additional legs emanating from its rank-0 parabolic fixed point.

A single toroidal cross section is, however, not sufficient to assess divertor behavior in a stellarator.Figure9therefore shows the connection length on a sequence of cross sections along the device for the single-null (top row) and double-null (bottom row) configurations. Here the broken stellarator symmetry of the single null becomes important: since cross sections atϕ\phiand−ϕ-\phiare no longer mirror images of one another, the full field periodϕ∈[0∘,−180∘]\phi\in[0^{\circ},-180^{\circ}]must be covered, whereas for the stellarator symmetric double null the half field periodϕ∈[0∘,−90∘]\phi\in[0^{\circ},-90^{\circ}]suffices, with the remaining cross sections following by symmetry. Both configurations behave well over the entire device: the core region of long connection length remains intact at every toroidal angle, the sharp gradient ofLcL_{c}across the separatrix persists, and the divertor legs sweep smoothly and continuously along the vessel wall rather than appearing or vanishing abruptly.Figure 9:Connection lengthLcL_{c}on a sequence of toroidal cross sections for the single-null (top row) and double-null (bottom row) configurations offig.8. Since the single null breaks stellarator symmetry, the cross sections span the full field periodϕ∈[0∘,−180∘]\phi\in[0^{\circ},-180^{\circ}]; for the stellarator symmetric double null the half field periodϕ∈[0∘,−90∘]\phi\in[0^{\circ},-90^{\circ}]determines the entire device. The solid line is the vessel cross section and the dashed line the optimization surfaceΓ\Gamma. In both configurations the confined core and the divertor legs persist smoothly across all toroidal angles.

The strike plots infig.10are generated using the optimized vessels as preliminary strike targets. Field lines are launched from a flux surface just outside the separatrix on a grid of180×720180\times 720points (129 600129\,600field lines) and traced in both directions for up to 100 m, with a small artificial cross-field diffusion coefficient of10−5​m2/m10^{-5}\,\mathrm{m^{2}/m}and a maximum integration step of0.01750.0175rad. Their intersections with the vessel are binned onto a240×120240\times 120grid in poloidal and toroidal angle, spanning one field period for the non-stellarator-symmetric configurations and one half period for the stellarator symmetric double null, whose remaining half follows by symmetry. The intersection count is normalized by the maximum count per cell for each configuration individually and shown as a color bar; this displays the shape of each strike pattern but not its absolute magnitude, so we additionally compare the configurations on a common scale below.

In all four configurations the strike points organize into narrow bands that are well localized in both the poloidal and toroidal angle, rather than being smeared over the vessel: the wetted area is set by the divertor topology, with the double null distributing the exhaust over four up-down symmetric bands while the single-null configurations concentrate it below the midplane (θ≈−90∘\theta\approx-90^{\circ}).
Strike line maps indicate where physical divertor targets would need to be placed on each device, and confirm that the diverted field lines strike the vessel in an ordered, topology-determined pattern rather than diffusely.

For a comparison across the configurations, we consider the smallest wall area that receives half of all field-line strikes,A50%A_{50\%}, normalized by the respective vessel surface area, since the four vessels differ substantially in size. WhileA50%A_{50\%}is not a standard figure of merit, it is a quantile-based analogue of the wetted-area measures used in tokamak heat-load studies, chosen here because it is insensitive to the histogram bin resolution and to the number of field lines traced. By this measure the snowflake spreads the bulk of its exhaust most effectively: half of its strikes are distributed over1.5%1.5\%of the vessel surface, compared to0.7%0.7\%for the double null and0.40.4–0.5%0.5\%for the single-null and parabolic configurations, a relative improvement by a factor of22–3.53.5. The snowflake divertor is effective at spreading heat, though we caution that it might not be attributed to the divertor topology alone: the snowflake is also the most chaotic of the four edge magnetic fields, which by itself broadens the strike pattern. Disentangling these contributions, and establishing whether the observed ordering holds systematically, will require a statistical analysis over many configurations, which we plan to carry out on the larger database of devices mentioned insection8.Figure 10:Strike lines for the four devices fromfig.8. Zero degrees of the poloidal angle represents the outboard midplane with the positive direction following the vessel in the counter clockwise direction.

## 7.2MHD Stability Proxy

The configurations offig.8are vacuum fields and are therefore ideal-MHD stable by construction: withp′≡0p^{\prime}\equiv 0there is no pressure drive. The relevant question is instead whether the novel edge topologies come at the price of MHD stability once a plasma is present: the strong shaping required to produce a parabolic or snowflake fixed point could, in principle, degrade the interchange stability of the core. To address this question at the operating point of the planned experiment, we evaluate two complementary ideal-MHD criteria: the Mercier interchange criterion, as computed by VMEC[43], and the ballooning growth rate, computed with COBRAVMEC[79], both evaluated on a fixed-boundary equilibrium based on the vacuum field with a low volume-averagedβ=0.01%\beta=0.01\%, matching the parameters expected for STAR_Lite design A[40]. Both are linear, ideal, local criteria that are necessary conditions for stability rather than predictions of the achievableβ\beta.
Moreover, at such lowβ\betathe pressure drive is weak, so passing these criteria confirms the configurations are stable at the operating point of the experiment; we defer analysis at reactor-relevantβ\betato the finite-β\betaextension of the framework discussed in the conclusions.

The Mercier criterion tests for local interchange instabilities, in which neighboring flux tubes swap radial positions without appreciably bending the magnetic field[32,22]. It decomposes into four terms,DMerc=DShear+DWell+DCurr+DGeodD_{\mathrm{Merc}}=D_{\mathrm{Shear}}+D_{\mathrm{Well}}+D_{\mathrm{Curr}}+D_{\mathrm{Geod}}, with the configuration Mercier-stable wherever the sum is positive: the magnetic shear termDShear≥0D_{\mathrm{Shear}}\geq 0is stabilizing, the geodesic curvature termDGeod≤0D_{\mathrm{Geod}}\leq 0is destabilizing, andDWellD_{\mathrm{Well}}is stabilizing in the presence of a magnetic well.DCurrD_{\mathrm{Curr}}reflects the contribution of the net toroidal current and can take either sign; since our configurations are current-free, this term is negligible here. SinceDWellD_{\mathrm{Well}}can be evaluated directly on the vacuum field, we are able to optimize for it explicitly, as shown through Equation (\theparentequation.6).

The ballooning criterion complements Mercier’s criterion by testing for instabilities that are localized along a field line rather than at a point, and which are driven by pressure gradients coupling to unfavorable local curvature. Unlike Mercier’s criterion, ballooning modes can grow even where the flux-surface-averaged curvature is favorable, making the two criteria complementary rather than redundant. We reportγmax\gamma_{\mathrm{max}}, the maximum over the sampled flux surfaces and field lines of the signed ballooning growth rate computed by COBRAVMEC[79], evaluated on1111flux surfaces spannings=0.05s=0.05to0.950.95with4×44\times 4initial angular positions per surface;γmax<0\gamma_{\mathrm{max}}<0indicates stability. An independent calculation of the ballooning eigenvalue with a one-dimensional finite-element solver on the same equilibria confirms stability on all analyzed surfaces.Figure 11:Ideal MHD stability analysis via the Mercier and ballooning criteria. Panel A shows the individual Mercier terms (DShearD_{\mathrm{Shear}},DWellD_{\mathrm{Well}},DCurrD_{\mathrm{Curr}},DGeodD_{\mathrm{Geod}}) and their sumDMercD_{\mathrm{Merc}}as a function of the normalized toroidal fluxs=Ψ/Ψbs=\Psi/\Psi_{b}, whereΨb\Psi_{b}is the flux at the plasma boundary, for the double-null configuration; the configuration is Mercier-stable whereverDMerc>0D_{\mathrm{Merc}}>0. Panel B comparesDMercD_{\mathrm{Merc}}(left axis, circles) and the maximum ballooning growth rateγmax\gamma_{\mathrm{max}}computed with COBRAVMEC[79](right axis, squares) across all four configurations. Note that the Mercier terms are given in arbitrary VMEC units; only their sign and relative composition are physically meaningful, not their absolute magnitude.

Figure11summarizes the analysis. Panel A shows the Mercier criterion split into its constituent termsDShearD_{\mathrm{Shear}},DWellD_{\mathrm{Well}},DCurrD_{\mathrm{Curr}}, andDGeodD_{\mathrm{Geod}}for the double-null configuration, illustrating the balance described above: away from the magnetic axis, the destabilizing geodesic contribution is overcome by the combination of shear and the optimized magnetic well. Panel B shows the ballooning growth rateγmax\gamma_{\mathrm{max}}andDMercD_{\mathrm{Merc}}for all four configurations. With respect to ballooning modes, all four devices, including the parabolic and snowflake configurations, are stable (γmax<0\gamma_{\mathrm{max}}<0) on every flux surface analyzed. The Mercier criterion is more restrictive. The double-null, single-null, and parabolic configurations are Mercier stable over the bulk of the plasma volume, with an unstable region near the magnetic axis (s≲0.1s\lesssim 0.1for the double null,s≲0.2s\lesssim 0.2for the single null and the parabolic configuration) and, for the parabolic configuration, a return to instability on the outermost surfaces. We note that the innermost flux surfaces, where all four configurations returnDMerc<0D_{\mathrm{Merc}}<0, are also where VMEC’s evaluation of the Mercier criterion is known to be least reliable, so the near-axis instability should be interpreted with caution. The snowflake configuration is Mercier stable only in the intermediate region0.3≲s≲0.50.3\lesssim s\lesssim 0.5. We conclude that the exotic divertor topologies are compatible with ballooning stability at STAR_Lite parameters, and that Mercier stability over most of the plasma volume is attainable at least up to the parabolic divertor class. For the snowflake, interchange stability is the binding constraint: notably, this configuration was optimized with the magnetic well constraint active (V′′≤−100V^{\prime\prime}\leq-100), which for this topology is evidently not sufficient to obtain Mercier stability beyond the intermediate region.
A systematic study of how Mercier stability trades against divertor topology and quasisymmetry, across the larger database of configurations mentioned in the conclusions, is left to future work.

Finally, we verify inappendixCthat the magnetic well constrainteq.\theparentequation.6indeed has the intended effect on these stability measures, by comparing two devices with identical design targets that differ only in whether the well is targeted (fig.12).

## 8Conclusions

This work presents, for the first time, a set of algorithms for the simultaneous optimization of stellarator equilibria, arbitrary divertor topology and vacuum vessel. This is achieved by the development of two new computational tools: a differentiable method for computing periodic field lines and the Jacobian of their return map, which is well-conditioned even in the degenerate limit of parabolic fixed points; and an efficient scheme for designing vessels which do not intersect the confined region, edge fixed points or coils, achieved by using signed distance functions.

The algorithms presented here are generally applicable to stellarator design, but here we demonstrate their applicability and flexibility by designing next-generation candidates for the STAR_Lite university-scale stellarator experiment at Hampton University, Virginia[40]. These stellarators are optimized for quasi-axisymmetric vacuum fields, buildable coils, geometrically simple vessels and novel divertor topologies. The examples demonstrate the versatility of the algorithms; in addition to single- and double-null-like configurations, we also show divertor structures never previously reported in stellarators; six-legged “snowflake” divertors (which are targeted as periodic field lines of the parabolic “flavor”) and an “O-point chain” which diverts plasma to the vessel wall but without (as in island divertors) encircling the confined plasma. The divertor performance of such topologies, when scaled to reactor scale, is currently unknown (and also depends on divertor plate and baffle geometry, which is not explored here), but this work presents an avenue by which divertor topology can be easily and efficiently manipulated to explore such advanced concepts. The proposed algorithms are robust enough to generate a data set of STAR_Lite class stellarators with advanced divertors, which will be analyzed in future work.

The promising results of the algorithms presented here motivate their application beyond the design of STAR_Lite configurations.
Extending the optimization to stellarators with finite plasmaβ\beta, would require the plasma-generated magnetic field to be included in the calculation of the edge fixed points.
Including the plasma-generated field could be done, for example, using a virtual casing principle such as calculated by BIEST[63]or EXTENDER[15], or by using a topology-agnostic equilibrium code such as SPEC[60,44].
Additional target functions could be included in the optimization to parametrize divertor performance. These might include flux expansion and upstream-to-target connection lengths as is used to quantify tokamak divertor performance[83,82,34,41], low-fidelity stellarator edge models such as two-point models[19,61]or reduced heat transport models[24,20,23,48], or more expansive high-fidelity models such as EMC3-EIRENE[18]or BOUT++-based tools[81,80,88,7]. Such calculations usually rely on the plasma-facing component geometry as well as the magnetic geometry, but a number of relatively straightforward algorithms for automated divertor plate/baffle construction already exist which could be used as a starting point[11,10,58,90,24].

## 9Data availability

The scripts that generate all data presented in this paper will be made publicly available in a repository on Zenodo.

## 10Acknowledgments

Supported by DOE-RENEW (DE-SC0025698, SN, GW), DOE-FAIR (DE-SC0024443, CL), the Simons Foundation (1167550, CL), and the Friedrich Schiedel Foundation for Energy Technology (RW).
This work has been carried out within the framework of the EUROfusion Consortium, partially funded by the European Union via the Euratom Research and Training Programme (Grant Agreement No 101052200 — EUROfusion). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Commission. Neither the European Union nor the European Commission can be held responsible for them. We thank the Flatiron Institute’s Scientific Computing Core.
We also thank Nikita Nikulsin for sharing his ballooning stability code.
The authors acknowledge the use of various AI systems for assistance with manuscript formulation and plotting code. All AI-assisted content was reviewed, edited, and verified by the authors, who take full responsibility for the integrity of the final work.

## Appendix AFull optimization problem

For completeness, we state here the full optimization problem (24), augmented with the engineering constraints that were omitted fromsection6for brevity. Re-using the numbering ofsection6, the problem readsmin𝐪,𝐯\displaystyle\min_{\mathbf{q},\,\mathbf{v}}\quadfQA​(𝐪,𝐬​(𝐪))\displaystyle f_{\mathrm{QA}}\big(\mathbf{q},\,\mathbf{s}(\mathbf{q})\big)subject toι​(𝐬​(𝐪))=ιs∗\displaystyle\iota\big(\mathbf{s}(\mathbf{q})\big)=\iota_{s}^{*}[opt. surface rotational transform](\theparentequation.1)ι​(𝐚​(𝐪))=ιa∗\displaystyle\iota\big(\mathbf{a}(\mathbf{q})\big)=\iota_{a}^{*}[on-axis rotational transform](\theparentequation.2)A​(𝐬​(𝐪))=A∗\displaystyle A\big(\mathbf{s}(\mathbf{q})\big)=A^{*}[aspect ratio](\theparentequation.3)∫01‖𝐁​(𝚪axis​(t;𝐚​(𝐪)))‖​dt=B∗\displaystyle\int_{0}^{1}\big\|\mathbf{B}\big(\bm{\Gamma}_{\text{axis}}(t;\mathbf{a}(\mathbf{q}))\big)\big\|\,\mathrm{d}t=B^{*}[mean field strength](\theparentequation.4)Vart⁡[‖𝐁​(𝚪axis​(t;𝐚​(𝐪)))‖]=0\displaystyle\operatorname{Var}_{t}\!\Big[\,\big\|\mathbf{B}\big(\bm{\Gamma}_{\text{axis}}(t;\mathbf{a}(\mathbf{q}))\big)\big\|\,\Big]=0[on-axis field variance](\theparentequation.5)W​(Ψ;𝐚​(𝐪),𝐬​(𝐪),𝐪)≤W∗\displaystyle W\big(\Psi;\mathbf{a}(\mathbf{q}),\,\mathbf{s}(\mathbf{q}),\,\mathbf{q}\big)\leq W^{*}[magnetic well](\theparentequation.6)|𝐈​(𝐪)|≤𝐈∗\displaystyle|\mathbf{I}(\mathbf{q})|\leq\mathbf{I}^{*}[coil current bound](\theparentequation.7)dcoil-vessel≤ϱ​(𝚪coil​(t;𝐪);𝐯)≤Dcoil-vessel\displaystyle d_{\text{coil-vessel}}\leq\varrho\big(\bm{\Gamma}_{\text{coil}}(t;\mathbf{q});\,\mathbf{v}\big)\leq D_{\text{coil-vessel}}[coil-vessel distance](\theparentequation.1)ϱ​(𝚪divertor​(t;𝐱​(𝐪));𝐯)≤ddivertor-vessel\displaystyle\varrho\big(\bm{\Gamma}_{\text{divertor}}(t;\mathbf{x}(\mathbf{q}));\,\mathbf{v}\big)\leq d_{\text{divertor-vessel}}[divertor-vessel distance](\theparentequation.2)ϱ​(𝚪surface​(φ,θ;𝐬​(𝐪));𝐯)≤dsurface-vessel\displaystyle\varrho\big(\bm{\Gamma}_{\text{surface}}(\varphi,\theta;\mathbf{s}(\mathbf{q}));\,\mathbf{v}\big)\leq d_{\text{surface-vessel}}[opt. surface-vessel distance](\theparentequation.3)Vart​[ϱ​(𝚪divertor​(t;𝐱​(𝐪));𝐯)]=0\displaystyle\mathrm{Var}_{t}[\varrho\big(\bm{\Gamma}_{\text{divertor}}(t;\mathbf{x}(\mathbf{q}));\,\mathbf{v}\big)]=0[const. divertor-vessel distance](\theparentequation.4)Vart​[𝐞z⋅𝚪divertor​(t;𝐱​(𝐪))]=0\displaystyle\mathrm{Var}_{t}\big[\,\mathbf{e}_{z}\cdot\bm{\Gamma}_{\text{divertor}}(t;\mathbf{x}(\mathbf{q}))\,\big]=0[const. divertorZZ-coordinate](\theparentequation.5)Vart⁡[‖𝚪coil,i′​(t;𝐪)‖]=0\displaystyle\operatorname{Var}_{t}\!\big[\,\|\bm{\Gamma}_{\text{coil},i}^{\prime}(t;\mathbf{q})\|\,\big]=0[uniform incremental arclength](24.13)‖𝚪coil,i​(𝐪)−𝚪coil,j​(𝐪)‖2≥dcc\displaystyle\big\|\bm{\Gamma}_{\text{coil},i}(\mathbf{q})-\bm{\Gamma}_{\text{coil},j}(\mathbf{q})\big\|_{2}\geq d_{\text{cc}}[coil-to-coil distance](24.14)Li​(𝐪)≤Lmax\displaystyle L_{i}(\mathbf{q})\leq L_{\max}[coil length](24.15)maxt⁡κi​(t;𝐪)≤κmax\displaystyle\max_{t}\,\kappa_{i}(t;\mathbf{q})\leq\kappa_{\max}[maximum curvature](24.16)1Li​(𝐪)​∫01κi​(t;𝐪)2​‖𝚪coil,i′​(t;𝐪)‖​dt≤κmsc\displaystyle\frac{1}{L_{i}(\mathbf{q})}\int_{0}^{1}\kappa_{i}(t;\mathbf{q})^{2}\,\|\bm{\Gamma}_{\text{coil},i}^{\prime}(t;\mathbf{q})\|\,\mathrm{d}t\leq\kappa_{\mathrm{msc}}[mean-squared curvature](24.17)R​(𝐬​(𝐪))=R0\displaystyle R\big(\mathbf{s}(\mathbf{q})\big)=R_{0}[major radius](24.18)

for each coiliiand each pair of distinct coilsi≠ji\neq j. Here𝚪coil,i​(t;𝐪)\bm{\Gamma}_{\text{coil},i}(t;\mathbf{q})denotes theii-th coil,κi​(t;𝐪)\kappa_{i}(t;\mathbf{q})its curvature, andLi​(𝐪)=∫01‖𝚪coil,i′​(t;𝐪)‖​dtL_{i}(\mathbf{q})=\int_{0}^{1}\|\bm{\Gamma}_{\text{coil},i}^{\prime}(t;\mathbf{q})\|\,\mathrm{d}tits length.

Constraints (\theparentequation.1)–(\theparentequation.5) are described insection6. The remaining relations are the additional engineering constraints, whose bounds follow the values used for design A of the STAR_Lite project[40].Equation24.13parameterizes each coil by uniform incremental arclength.Equation24.14keeps distinct coils at leastdcc=0.15​md_{\text{cc}}=0.15~\mathrm{m}apart.Equation24.15limits each coil to a lengthLmax=3​mL_{\max}=3~\mathrm{m}.Equations24.16and24.17bound the maximum and mean-squared curvatures byκmax=10.4​m−1\kappa_{\max}=10.4~\mathrm{m}^{-1}andκmsc=20.0​m−2\kappa_{\mathrm{msc}}=20.0~\mathrm{m}^{-2}, respectively. Finally,eq.24.18fixes the major radius of the optimization surface toR0=0.5​mR_{0}=0.5~\mathrm{m}.

Separately, the vacuum vessel geometry is constrained to remain valid and non-self-intersecting, with the constraints depending on the vessel family (section5):0<rc<bx,rc<by0<r<rc,r<rc}\displaystyle\left.\begin{aligned} &0<r_{c}<b_{x},\quad r_{c}<b_{y}\\
&0<r<r_{c},\quad r<r_{c}\end{aligned}\right\}pill pipe vessel(28a)Vart⁡[‖𝐜′​(t;𝐯)‖]=0r​(t;𝐯)>0r​(t;𝐯)<1−(r​(t;𝐯)2)′′/2κ​(t)|r′​(t;𝐯)|<‖𝐜′​(t;𝐯)‖}\displaystyle\left.\begin{aligned} &\operatorname{Var}_{t}\!\big[\,\|\mathbf{c}^{\prime}(t;\mathbf{v})\|\,\big]=0\\
&r(t;\mathbf{v})>0\\
&r(t;\mathbf{v})<\frac{1-(r(t;\mathbf{v})^{2})^{\prime\prime}/2}{\kappa(t)}\\
&|r^{\prime}(t;\mathbf{v})|<\|\mathbf{c}^{\prime}(t;\mathbf{v})\|\end{aligned}\right\}canal vessel(28b)r>0,ℓk>0,θk<θmaxℓk>r​[tan⁡(θk/2)+tan⁡(θk+1/2)]}\displaystyle\left.\begin{aligned} &r>0,\quad\ell_{k}>0,\quad\theta_{k}<\theta_{\max}\\
&\ell_{k}>r\big[\tan(\theta_{k}/2)+\tan(\theta_{k+1}/2)\big]\end{aligned}\right\}piecewise-cylinder vessel(28c)

whereκ​(t;𝐯)\kappa(t;\mathbf{v})is the curvature of the non-planar centerline𝐜​(t;𝐯)\mathbf{c}(t;\mathbf{v}), and, for the piecewise-cylinder vessel,ℓk\ell_{k}andθk\theta_{k}are the length of thekk-th cylinder and the turn angle at thekk-th joint, fork=1,…,nsegk=1,\dots,n_{\text{seg}}.

## Appendix BQuasisymmetry objective

Suppose a flux surface with degrees of freedom𝐬\mathbf{s}and is parameterized by Boozer anglesθ∈[0,1]\theta\in[0,1]andφ∈[0,1/nfp]\varphi\in[0,1/n_{\text{fp}}].
The objectivefQAf_{\mathrm{QA}}measures the average violation from quasisymmetry, where the individual quasisymmetry violation isfQA​(𝐜,𝐈,𝐬)=∬S(B​(φ,θ;𝐜,𝐈,𝐬)−BQA​(θ;𝐜,𝐈,𝐬))2​𝑑S∬SBQA​(θ;𝐜,𝐈,𝐬)2​𝑑S,f_{\mathrm{QA}}(\mathbf{c},\mathbf{I},\mathbf{s})=\frac{\iint_{S}(B(\varphi,\theta;\mathbf{c},\mathbf{I},\mathbf{s})-B_{\text{QA}}(\theta;\mathbf{c},\mathbf{I},\mathbf{s}))^{2}~dS}{\iint_{S}B_{\text{QA}}(\theta;\mathbf{c},\mathbf{I},\mathbf{s})^{2}~dS},(29)

andBQA​(θ;𝐜,𝐈,𝐬)=∫01/nfpB​(φ,θ;𝐜,𝐈,𝐬)​‖𝐧​(φ,θ;𝐬)‖​𝑑φ∫01/nfp‖𝐧​(φ,θ;𝐬)‖​𝑑φB_{\text{QA}}(\theta;\mathbf{c},\mathbf{I},\mathbf{s})=\frac{\int_{0}^{1/n_{\text{fp}}}B(\varphi,\theta;\mathbf{c},\mathbf{I},\mathbf{s})\|\mathbf{n}(\varphi,\theta;\mathbf{s})\|~d\varphi}{\int_{0}^{1/n_{\text{fp}}}\|\mathbf{n}(\varphi,\theta;\mathbf{s})\|~d\varphi}(30)

is the closest quasisymmetric field strength, in a least squares sense, to the true one generated by the coils. Here the integrals are taken over the targeted optimization surface. Note thatBQAB_{\text{QA}}depends only onθ\theta: for a quasi-axisymmetric field, the field strength on a flux surface is a function ofθ\thetaalone in Boozer coordinates, soBQA​(θ)B_{\text{QA}}(\theta)is the field strength of the closest quasi-axisymmetric field. See[31]for the full derivation.

## Appendix CControlling the magnetic well

The magnetic well propertyW:=d2​Vd​Ψ2<0,W:=\frac{d^{2}V}{d\Psi^{2}}<0,

is desirable to prevent the appearance of interchange modes, whereVVis the volume of a flux surface andΨ\Psiis the toroidal flux[53]. This section shows how to compute the magnetic well from two or more surfaces parameterized in Boozer coordinates. Note that one of the surfaces can be the magnetic axis.

Given a set of flux surfaces with toroidal fluxesΨj\Psi_{j}forj=1,…,Nj=1,\ldots,N, the magnetic well can be computed by fitting an order-2​N+12N+1Hermite polynomial interpolant to the volume, and differentiating it twice with respect toΨ\Psi. The Hermite interpolant,V^\hat{V}, interpolates the volumeVjV_{j}and derivative of the volumeVj′V^{\prime}_{j}, on each flux surface,V^​(Ψj)\displaystyle\hat{V}(\Psi_{j})=Vj,j=1,…,N\displaystyle=V_{j},\quad j=1,\ldots,N(31)V^′​(Ψj)\displaystyle\hat{V}^{\prime}(\Psi_{j})=Vj′,j=1,…,N.\displaystyle=V^{\prime}_{j},\quad j=1,\ldots,N.

The volume of a surface parameterized in Boozer coordinates can be computed through a boundary integral using divergence theorem. The derivative of the volume with respect toΨ\Psican be computed by differentiating the volume integral,V​(Ψ)=∫0Ψ∫01∫01G​(ψ)+ι​I​(ψ)B​(ψ,φ,θ)2​𝑑ψ​𝑑φ​𝑑θ,V(\Psi)=\int_{0}^{\Psi}\int_{0}^{1}\int_{0}^{1}\frac{G(\psi)+\iota I(\psi)}{B(\psi,\varphi,\theta)^{2}}~d\psi~d\varphi~d\theta,(32)

which simplifies to,V′​(Ψ)=∫01∫01GB​(Ψ,φ,θ)2​𝑑φ​𝑑θ,V^{\prime}(\Psi)=\int_{0}^{1}\int_{0}^{1}\frac{G}{B(\Psi,\varphi,\theta)^{2}}~d\varphi~d\theta,(33)

when the magnetic field is a curl-free(I=0,G=const)(I=0,G=\text{const}). The right-hand-side of (33) can be evaluated directly on a Boozer surface, providing the derivative data to construct a Hermite polynomial for the volume.

In practice, the interpolation conditions are evaluated from data taken from one Boozer surface and the magnetic axis, producing a cubic hermite polynomial. Differentiating the model twice produces a linear model for the magnetic well. Note that the magnetic well is not unitless and is affected by the device’s scale and field strength.

During optimization, such as inSection6, the magnetic well can be controlled via a constraint of the form,W​(Ψ;𝐚​(𝐪),𝐬​(𝐪),𝐪)=V^′′​(Ψ)≤W∗\displaystyle W\big(\Psi;\mathbf{a}(\mathbf{q}),\,\mathbf{s}(\mathbf{q}),\,\mathbf{q}\big)=\hat{V}^{\prime\prime}(\Psi)\leq W^{*}(34)

whereW∗W^{*}is a target value of the magnetic well. The constraint can be upheld pointwise.

To confirm that the well constraint has the intended effect on the MHD stability proxies ofsection7, we compare two STAR_Lite class devices with the same design targets, except that one targets magnetic well and the other does not (fig.12). The trade-off between requesting a magnetic well and the achieved quality of quasisymmetry has already been studied in[55], where it was revealed that requesting well is typically possible, but comes at the detriment of the quasisymmetry; we echo this observation here. Note that visually, the modular coils and surface cross sections of the two configurations are quite close to one another. This hints that the magnetic well might be particularly sensitive to manufacturing errors, and a good candidate for risk neutral optimization.Figure 12:Impact of well optimization on a particular device. We compare two configurations with identical optimization goals, differing only in the well optimization: the solid lines correspond to a configuration with a well-term target ofV′′≤−100V^{\prime\prime}\leq-100, while the dotted lines correspond to a configuration in which the well term was not targeted. MHD stability changes when well optimization is utilized.

## References
- [1]R. Akers, J. Ahn, G. Antar, L. Appel, D. Applegate, C. Brickley, C. Bunting,
P. Carolan, C. Challis, N. Conway, et al.Transport and confinement in the Mega Ampere Spherical Tokamak
(MAST) plasma.Plasma physics and controlled fusion, 45(12A):A175–A204, 2003.
- [2]R. Akers, J. Ahn, L. Appel, E. Arends, K. Axon, R. Buttery, C. Byrom,
P. Carolan, G. Counsell, G. Cunningham, et al.H-mode access and performance in the Mega-Amp Spherical Tokamak.Physics of Plasmas, 9(9):3919–3929, 2002.
- [3]T. Andreeva, J. Geiger, A. Dinklage, G. Wurden, H. Thomsen, K. Rahbarnia,
J. Schmitt, M. Hirsch, G. Fuchert, C. Nührenberg, et al.Magnetic configuration scans during divertor operation of
Wendelstein 7-X.Nuclear Fusion, 62(2):026032, 2022.
- [4]R. Aymar, P. Barabaschi, and Y. Shimomura.The ITER design.Plasma physics and controlled fusion, 44(5):519–565, 2002.
- [5]A. Bader, A. Ayilaran, J. Canik, A. De, W. Guttenfelder, C. Hegna, M. Knilans,
A. Malkus, T. Pedersen, P. Sinha, et al.Power and particle exhaust for the Infinity Two fusion pilot plant.Journal of Plasma Physics, 91(2):E67, 2025.
- [6]A. Baillod, E. J. Paul, T. Elder, and J. M. Halpern.Enhancing stellarator accessibility through port size optimization.Nuclear Fusion, 65(8):086040, 2025.
- [7]D. Bold and B. Shanahan.Numerical methods for stellarator simulations in bout++.arXiv preprint arXiv:2603.28221, 2026.
- [8]A. H. Boozer.Stellarator design.Journal of Plasma Physics, 81(6):515810606, 2015.
- [9]R. Davies, D. Boeyaert, A. Wolfmeister, B. Geiger, G. Harrer, and J. Geiger.Computational studies of giant edge islands and unpaired X-points
in HSX and W7-X by manipulating coil currents, 2026.
- [10]R. Davies, M. Drevlak, Y. Feng, J. Geiger, A. Goodman, C. Smiet, G. Plunk,
P. Xanthopoulos, and S. Henneberg.Stellarator divertor optimisation for a Stable Quasi-Isodynamic
Design (SQuID): magnetic topology, divertor plates and baffle design.In51st EPS Conference on Plasma Physics. European Physical
Society, 2025.
- [11]R. Davies, Y. Feng, D. Boeyaert, J. C. Schmitt, M. J. Gerard, K. A. Garcia,
O. Schmitz, B. Geiger, and S. A. Henneberg.A semi-automated algorithm for designing stellarator divertor and
limiter plates and application to HSX.Nuclear Fusion, 64(12):126044, 2024.
- [12]R. Davies, C. B. Smiet, C. Batzdorf, J. Geiger, J. Loizu, and S. A. Henneberg.Characterisation of X-and O-points in Wendelstein 7-X with
respect to coil currents.Journal of Plasma Physics, 92(2), 2026.
- [13]R. Davies, C. B. Smiet, A. Punjabi, A. H. Boozer, and S. A. Henneberg.The topology of non-resonant stellarator divertors.Nuclear Fusion, 65(7):076018, jun 2025.
- [14]E. Di Pietro, P. Barabaschi, Y. Kamada, S. Ishida, et al.Overview of engineering design, manufacturing and assembly of
JT-60SA machine.Fusion Engineering and Design, 89(9-10):2128–2135, 2014.
- [15]M. Drevlak, D. Monticello, and A. Reiman.PIES free boundary stellarator equilibria with improved initial
conditions.Nuclear fusion, 45(7):731–740, 2005.
- [16]D. Eberly.Distance from a point to an ellipse, an ellipsoid, or a
hyperellipsoid.https://geometrictools.com/Documentation/DistancePointEllipseEllipsoid.pdf,
2013.Geometric Tools. Accessed: 2026-07-18.
- [17]T. Evans.Resonant magnetic perturbations of edge-plasmas in toroidal
confinement devices.Plasma Physics and Controlled Fusion, 57(12):123001, 2015.
- [18]Y. Feng, H. Frerichs, M. Kobayashi, A. Bader, F. Effenberg, D. Harting,
H. Hoelbe, J. Huang, G. Kawamura, J. Lore, et al.Recent improvements in the EMC3-EIRENE code.Contributions to Plasma Physics, 54(4-6):426–431, 2014.
- [19]Y. Feng, M. Kobayashi, T. Lunt, and D. Reiter.Comparison between stellarator and tokamak divertor transport.Plasma physics and controlled fusion, 53(2):024009, 2011.
- [20]Y. Feng and W7-X-team.Review of magnetic islands from the divertor perspective and a
simplified heat transport model for the island divertor.Plasma Physics and Controlled Fusion, 64(12):125012, 2022.
- [21]E. Flom, W. Kalb, S. Seethalla, C. Swanson, R. Wu, M. Avida, A. Doudna Cate,
D. Dudt, T. Kruger, S. Kumar, N. Maitra, and D. Gates.Design and conceptual modeling of a tokamak-like X-point divertor
for the Helios quasi-axisymmetric stellarator.Fusion Engineering and Design, 230:115846, 2026.
- [22]D. A. Frank-Kamenetskii.Interchange or Flute Instabilities, pages 98–100.Macmillan Education UK, London, 1972.
- [23]H. Frerichs.Flare: field line analysis and reconstruction for 3d boundary plasma
modeling.Nuclear Fusion, 64(10):106034, sep 2024.
- [24]H. Frerichs, D. Boeyaert, Y. Feng, and D. Reiter.FIREFLY: heat load and particle exhaust approximations for rapid
evaluation of divertor designs.arXiv preprint arXiv:2604.11497, 2026.
- [25]A. Gallo, N. Fedorczak, S. Elmore, R. Maurizio, H. Reimerdes, C. Theiler,
C. Tsui, J. A. Boedo, M. Faitsch, H. Bufferand, et al.Impact of the plasma geometry on divertor power exhaust: experimental
evidence from tcv and simulations with soledge2d and tokam3x.Plasma Physics and Controlled Fusion, 60(1):014007, 2018.
- [26]D. Gates, S. Aslam, B. Berzin, P. Bonofiglo, A. Cote, D. Dudt, E. Flom,
D. Fort, A. Koen, T. Kruger, et al.Stellarator fusion systems enabled by arrays of planar coils.Nuclear Fusion, 65(2):026052, 2025.
- [27]D. Gates, A. Boozer, T. Brown, J. Breslau, D. Curreli, M. Landreman,
S. Lazerson, J. Lore, H. Mynick, G. Neilson, et al.Recent advances in stellarator optimization.Nuclear Fusion, 57(12):126064, 2017.
- [28]R. Gaur, D. Panici, T. Elder, M. Landreman, K. Unalmis, Y. Elmacioglu, D. Dudt,
R. Conlin, and E. Kolemen.Omnigenous umbilic stellarators.Journal of Plasma Physics, 91(6), 2026.
- [29]A. Geraldini, M. Landreman, and E. Paul.An adjoint method for determining the sensitivity of island size to
magnetic field variations.Journal of Plasma Physics, 87(3):905870302, 2021.
- [30]A. Giuliani, F. Wechsung, A. Cerfon, G. Stadler, and M. Landreman.Single-stage gradient-based stellarator coil design: optimization for
near-axis quasi-symmetry.Journal of Computational Physics, 459:111147, 2022.
- [31]A. Giuliani, F. Wechsung, G. Stadler, A. Cerfon, and M. Landreman.Direct computation of magnetic surfaces in Boozer coordinates and
coil optimization for quasisymmetry.Journal of Plasma Physics, 88(4):905880401, 2022.
- [32]R. J. Goldston and P. H. Rutherford.Introduction to Plasma Physics.Institute of Physics Publishing, Bristol and Philadelphia, 1995.
- [33]A. G. Goodman, G. G. Plunk, P. Xanthopoulos, M. Drevlak, J. Geiger, R. Davies,
H. M. Smith, C. Nührenberg, C. D. Beidler, S. A. Henneberg, and et al.A quasi-isodynamic stellarator configuration towards a fusion power
plant.Journal of Plasma Physics, 91(6):E153, 2025.
- [34]S. Gorno, C. Colandrea, O. Février, H. Reimerdes, C. Theiler, B. P. Duval,
T. Lunt, H. Raj, U. A. Sheikh, L. Simons, et al.Power exhaust and core-divertor compatibility of the baffled
snowflake divertor in TCV.Plasma Physics and Controlled Fusion, 65(3):035004, 2023.
- [35]J. M. Greene.Method for determining a stochastic transition.Technical report, Princeton Univ., NJ (USA). Plasma Physics Lab., 11
1978.
- [36]A. Griewank.Starlike domains of convergence for newton’s method at singularities.Numerische Mathematik, 35(1):95–111, 1980.
- [37]A. Griewank and G. W. Reddien.Characterization and computation of generalized turning points.SIAM Journal on Numerical Analysis, 21(1):176–185, 1984.
- [38]O. Grulke, G. Acton, J. Adamek, D. Aggelis, R.-M. Alamo-Calderon, C. Albert,
P. Aleynikov, K. Aleynikova, A. Alonso, G. Amanekwe, et al.Overview of Wendelstein 7-X high-performance operation.Nuclear Fusion, 66(11):116003, 2026.
- [39]O. Grulke, C. Albert, J. Alcuson Belloso, P. Aleynikov, K. Aleynikova,
A. Alonso, G. Anda, T. Andreeva, M. Arvanitou, E. Ascasibar, et al.Overview of the first Wendelstein 7-X long pulse campaign with
fully water-cooled plasma facing components.Nuclear Fusion, 64(11):112002, 2024.
- [40]G. F. Harrer, A. Giuliani, M. Padidar, R. Davies, S. Naik, and C. Lowe.STAR_Lite: A stellarator designed to experimentally validate
non-resonant divertors.arXiv preprint arXiv:2603.18265, 2026.
- [41]J. R. Harrison, C. Bowman, J. Clark, A. Kirk, J. Lovell, B. Patel, P. Ryan,
R. Scannell, A. Thornton, and K. Verhaegh.Benefits of the Super-X divertor configuration for scenario
integration on MAST upgrade.Plasma Physics and Controlled Fusion, 66(6):065019, 2024.
- [42]C. Hegna, D. Anderson, E. Andrew, A. Ayilaran, A. Bader, T. Bohm, K. C. Mata,
J. Canik, L. Carbajal, A. Cerfon, et al.The Infinity Two fusion pilot plant baseline plasma physics design.Journal of Plasma Physics, 91(3):E76, 2025.
- [43]S. P. Hirshman and J. C. Whitson.Steepest‐descent moment method for three‐dimensional
magnetohydrodynamic equilibria.The Physics of Fluids, 26(12):3553–3568, 12 1983.
- [44]S. Hudson, J. Loizu, C. Zhu, Z. Qu, C. Nuehrenberg, S. Lazerson, C. Smiet, and
M. Hole.Free-boundary MRxMHD equilibrium calculations using the
stepped-pressure equilibrium code.Plasma Physics and Controlled Fusion, 62(8):084002, 2020.
- [45]R. Jorge, A. Giuliani, and J. Loizu.Simplified and flexible coils for stellarators using single-stage
optimization.Physics of Plasmas, 31(11):112501, 11 2024.
- [46]M. Keilhacker, A. Gibson, C. Gormezano, and P. Rebut.The scientific success of JET.Nuclear Fusion, 41(12):1925–1966, 2001.
- [47]M. Keilhacker and A. team.The ASDEX divertor tokamak.Nuclear fusion, 25(9):1045–1054, 1985.
- [48]A. Kharwandikar.Power Exhaust Investigations in the W7-X Island Divertor.PhD thesis, University of Greifswald, 2025.
- [49]R. König, P. Grigull, K. McCormick, Y. Feng, J. Kisslinger, A. Komori,
S. Masuzaki, K. Matsuoka, T. Obiki, N. Ohyabu, et al.The divertor program in stellarators.Plasma physics and controlled fusion, 44(11):2365–2422, 2002.
- [50]K. Krieger, S. Brezinsek, J. Coenen, H. Frerichs, A. Kallenbach, A. Leonard,
T. Loarer, S. Ratynskaia, N. Vianello, N. Asakura, et al.Scrape-off layer and divertor physics: Chapter 5 of the special
issue: on the path to tokamak burning plasma operation.Nuclear Fusion, 65(4):043001, 2025.
- [51]A. Kuang, S. Ballinger, D. Brunner, J. Canik, A. Creely, T. Gray, M. Greenwald,
J. Hughes, J. Irby, B. LaBombard, et al.Divertor heat flux challenge and mitigation in SPARC.Journal of Plasma Physics, 86(5):865860505, 2020.
- [52]J. Kuang, J. Yang, Z. Ren, P. Zhang, Y. Wang, and W. Wang.Implementation of a free-boundary equilibrium solver for the
cloverleaf configuration and its implications for X-point radiators.Plasma Science and Technology, 28(4):045102, 2026.
- [53]M. Landreman and R. Jorge.Magnetic well and Mercier stability of stellarators near the
magnetic axis.Journal of Plasma Physics, 86(5):905860510, 2020.
- [54]M. Landreman, B. Medasani, F. Wechsung, A. Giuliani, R. Jorge, and C. Zhu.SIMSOPT: a flexible framework for stellarator optimization.Journal of Open Source Software, 6(65):3525, 2021.
- [55]M. Landreman and E. Paul.Magnetic fields with precise quasisymmetry for plasma confinement.Phys. Rev. Lett., 128:035001, Jan 2022.
- [56]S. A. Lazerson, A. J. Coelho, D. Douqa, A. A. Fessler, L. Hübner,
M. Moscheni, E. Hodge, R. Kembleton, J. Sissonen, K. Särkimäki,
et al.The fixed boundary plasma equilibrium basis for a one gigawatt
electric stellarator power plant.arXiv preprint arXiv:2607.09346, 2026.
- [57]J. Lion, J.-C. Anglès, L. Bonauer, A. B. Navarro, S. C. Ceron, R. Davies,
M. Drevlak, N. Foppiani, J. Geiger, A. Goodman, et al.Stellaris: A high-field quasi-isodynamic stellarator for a
prototypical fusion power plant.Fusion Engineering and Design, 214:114868, 2025.
- [58]B. Liu, G. Kawamura, S. Dai, Y. Xu, Y. Suzuki, A. Shimizu, H. Frerichs, and
Y. Feng.A universal target plate design scheme for stellarators: theoretical
basis and its application to heat load control.Nuclear Fusion, 65(1):016023, 2025.
- [59]A. Loarte.Effects of divertor geometry on tokamak plasmas.Plasma Physics and Controlled Fusion, 43(6):R183–R224, 2001.
- [60]J. Loizu, S. Hudson, and C. Nührenberg.Verification of the SPEC code in stellarator geometries.Physics of Plasmas, 23(11), 2016.
- [61]N. Maaziz, F. Reimold, V. Winters, S. Makarov, and Y. Feng.Investigating island divertor physics with an extended stellarator
two-point model.Nuclear Fusion, 2026.
- [62]T. Maekawa, N. M. Patrikalakis, T. Sakkalis, and G. Yu.Analysis and applications of pipe surfaces.Computer aided geometric design, 15(5):437–458, 1998.
- [63]D. Malhotra, A. J. Cerfon, M. O’Neil, and E. Toler.Efficient high-order singular quadrature schemes in magnetic fusion.Plasma Physics and Controlled Fusion, 62(2):024004, 2020.
- [64]C. Marsden.FORGE: Forge Optimises Reactor Geometries to improve
Exhaust, 2026.
- [65]J. Nocedal and S. J. Wright.Numerical optimization, 2006.
- [66]N. Ohyabu, T. Morisaki, S. Masuzaki, R. Sakamoto, M. Kobayashi, J. Miyazawa,
M. Shoji, A. Komori, O. Motojima, and L. E. Group).Observation of stable superdense core plasmas in the Large Helical
Device.Physical review letters, 97(5):055002, 2006.
- [67]M. Peternell and H. Pottmann.Computing rational parametrizations of canal surfaces.Journal of Symbolic Computation, 23(2-3):255–266, Feb. 1997.
- [68]D. Power, M. V. Umansky, and V. A. Soukhanovskii.Simulations of the churning mode: Toroidally symmetric plasma
convection and turbulence around the X-points in a snowflake divertor.Physics of Plasmas, 32(9), 2025.
- [69]I. Quilez.Distance functions.https://iquilezles.org/articles/distfunctions/, 2013.Accessed: 2026-07-18.
- [70]H. Renner, D. Sharma, J. Kisslinger, J. Boscary, H. Grote, and R. Schneider.Physical aspects and design of the Wendelstein 7-X divertor.Fusion science and technology, 46(2):318–326, 2004.
- [71]P. Rodriguez-Fernandez, A. Creely, M. Greenwald, D. Brunner, S. Ballinger,
C. Chrobak, D. Garnier, R. Granetz, Z. Hartwig, N. Howard, et al.Overview of the SPARC physics basis towards the exploration of
burning-plasma regimes in high-field, compact tokamaks.Nuclear Fusion, 62(4):042003, 2022.
- [72]D. Ryutov.Geometrical properties of a “snowflake” divertor.Physics of Plasmas, 14(6), 2007.
- [73]D. Ryutov, R. Cohen, W. Farmer, T. Rognlien, and M. Umansky.The ‘churning mode’of plasma convection in the tokamak divertor
region.Physica Scripta, 89(8):088002, 2014.
- [74]D. Ryutov, R. Cohen, T. Rognlien, and M. Umansky.The magnetic field structure of a snowflake divertor.Physics of Plasmas, 15(9), 2008.
- [75]D. Ryutov, R. Cohen, T. Rognlien, and M. Umansky.A snowflake divertor: a possible solution to the power exhaust
problem for tokamaks.Plasma Physics and Controlled Fusion, 54(12):124050, 2012.
- [76]D. Ryutov and M. Umansky.Divertor with a third-order null of the poloidal field.Physics of Plasmas, 20(9), 2013.
- [77]D. D. Ryutov and V. A. Soukhanovskii.The snowflake divertor.Physics of Plasmas, 22(11), 2015.ISBN: 1070-664X.
- [78]E. Sánchez, J. Velasco, I. Calvo, J. García-Regaña, C. Salcuni,
and J. Alonso.CIEMAT-QI4X: a reactor-relevant quasi-isodynamic stellarator
configuration compatible with an island divertor.Nuclear Fusion, 66(5):056008, 2026.
- [79]R. Sanchez, S. Hirshman, J. Whitson, and A. Ware.COBRA: An optimized code for fast analysis of ideal ballooning
stability of three-dimensional magnetic equilibria.Journal of Computational Physics, 161(2):576–588, 2000.
- [80]B. Shanahan, D. Bold, and B. Dudson.Global fluid turbulence simulations in the scrape-off layer of a
stellarator island divertor.Journal of Plasma Physics, 90(2):905900216, 2024.
- [81]B. Shanahan, B. Dudson, and P. Hill.Fluid simulations of plasma filaments in stellarator geometries with
bsting.Plasma Physics and Controlled Fusion, 61(2):025007, 2019.
- [82]V. Soukhanovskii, G. Cunningham, J. Harrison, F. Federici, P. Ryan, M.-U. Team,
et al.First snowflake divertor experiments in MAST-U tokamak.Nuclear Materials and Energy, 33:101278, 2022.
- [83]V. A. Soukhanovskii, S. L. Allen, M. E. Fenstermacher, C. J. Lasnier, M. A.
Makowski, A. G. McLean, W. H. Meyer, D. D. Ryutov, E. Kolemen, and R. J.
Groebner.Developing physics basis for the snowflake divertor in the DIII-D
tokamak.Nuclear Fusion, 58(3):036018, 2018.ISBN: 0029-5515.
- [84]P. Stangeby.A tutorial on some basic aspects of divertor physics.Plasma Physics and Controlled Fusion, 42(12B):B271–B291, 2000.
- [85]P. C. Stangeby and G. McCracken.Plasma boundary phenomena in tokamaks.Nuclear Fusion, 30(7):1225–1379, 1990.
- [86]E. Süli and D. F. Mayers.An introduction to numerical analysis.Cambridge university press, 2003.
- [87]G. Sun, H. Reimerdes, C. Theiler, B. Duval, M. Carpita, C. Colandrea,
O. Février, and T. Team.Performance assessment of a tightly baffled, long-legged divertor
configuration in tcv with solps-iter.Nuclear Fusion, 63(9):096011, 2023.
- [88]T. Tork, F. Reimold, D. Bold, B. Shanahan, B. Dudson, A. Stegmeir, and P. Manz.A BOUT++ transport model for island diverted stellarators including
drifts.In67th Annual Meeting of the APS Division of Plasma Physics.
APS, 2025.
- [89]P. M. Valanju, M. Kotschenreuther, S. Mahajan, and J. Canik.Super-X divertors and high power density fusion devices.Physics of Plasmas, 16(5), 2009.
- [90]A. Veksler, A. Bader, H. Frerichs, and E. Paul.Stellarator island divertor shape optimization for reduced peak heat
fluxes.arXiv preprint arXiv:2602.24049, 2026.
- [91]F. Warmer et al.European conceptual design of a HELIAS fusion power plant.Fusion Engineering and Design, 184:113293, 2022.
- [92]Z. Xu, R. Feng, and J.-g. Sun.Analytic and algebraic properties of canal surfaces.Journal of computational and applied mathematics,
195(1):220–228, 2006.
- [93]H. Yamada.Overview of results from the Large Helical Device.Nuclear Fusion, 51(9):094021, 2011.
- [94]S. Yang, J.-K. Park, Y. Jeon, N. C. Logan, J. Lee, Q. Hu, J. Lee, S. Kim,
J. Kim, H. Lee, et al.Tailoring tokamak error fields to control plasma instabilities and
transport.Nature communications, 15(1):1275, 2024.
- [95]M. Yoshikawa.An overview of the JT-60 project.Fusion engineering and design, 5(1):3–8, 1987.

## 


- 


Major funding support from
