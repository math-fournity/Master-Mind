# Areostationary Satellite Station Keeping Via a Natural Motion Trajectory and Predictive Control

**arXiv ID**: 2603.00781v2
**Authors**: Nathan A. Gall, Robert D. Halverson, Ryan J. Caverly
**Published**: 2026-02-28
**Categories**: physics.space-ph, math.OC
**Comments**: Submitted to the Journal of Guidance, Control, and Dynamics
**HTML URL**: https://arxiv.org/html/2603.00781v2

## Abstract

Areostationary Mars orbit (AMO) satellites will play an important role in future expeditions to the Martian surface due to their strength as navigation and communication satellites. Perturbative forces experienced by an AMOR satellite will cause it to drift from its nominal orbit, necessitating station keeping. This note presents a novel approach to AMO station keeping that bridges the gap seen in prior predictive control methods between fuel-efficiency and computational-efficiency. The method proposed in this notes involves the discovery and use of a fuel-free natural motion trajectory that maintains the satellite within one degree of longitude from a areostationary orbit. Two of these natural motion trajectories exist as limit cycles about Mars' stable equilibrium longitudes. They are the resulting motion in the presence of Mars' non-homogeneous gravitational field, accounting for Keplerian and higher-order gravitational perturbations. The proposed MPC policy uses a linear time-varying (LTV) dynamic model that is derived by linearizing the satellite's dynamics relative to the appropriate natural motion trajectory. The result is a station keeping policy that minimizes the fuel consumed, maintains thrust and station-keeping constraints, and is computationally tractable for on-board implementation as a quadratic program.

## Full Text

Areostationary Satellite Station Keeping Via a Natural Motion Trajectory and Predictive Control1footnote 11footnote 1A version of this note [1] (AIAA 2025-99106) was presented at the AIAA Region V Student Conference, April 3-4, 2025 in Minneapolis, MN.

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
- License: CC BY 4.0arXiv:2603.00781v2 [physics.space-ph] 30 May 2026

## Areostationary Satellite Station Keeping Via a Natural Motion Trajectory and Predictive Control111A version of this note[1](AIAA 2025-99106) was presented at the AIAA Region V Student Conference, April 3-4, 2025 in Minneapolis, MN.Nathan A. Gall222Ph.D. Student, Department of Aerospace Engineering and Mechanics, University of Minnesota, 110 Union St. SE, Minneapolis, MN 55455, AIAA Student MemberRobert D. Halverson333Ph.D. Candidate, Department of Aerospace Engineering and Mechanics, University of Minnesota, 110 Union St. SE, Minneapolis, MN 55455, AIAA Student Memberand Ryan J. Caverly444Associate Professor, Department of Aerospace Engineering and Mechanics, University of Minnesota, 110 Union St. SE, Minneapolis, MN 55455, AIAA Member.

## 1Introduction

Achieving a sustained human presence on Mars will require satellite coverage to facilitate communication and navigation. At the Earth, geostationary satellites play a key role in terrestrial communication and navigation constellations, as they provide continuous coverage over a wide area. Satellites in areostationary Mars orbits (AMO), the Martian equivalent to a geostationary Earth orbit (GEO), have been proposed to fulfill a similar role to their Earth-orbiting counterparts[2,3,4,5,6,7]. When considering only the two-body problem, an AMO satellite will maintain its longitude without the need for any station keeping. In reality, satellites in AMO experience non-Keplerian perturbing forces that cause them to drift from their nominal orbit[8,9]. A similar effect is present in GEO, where gravitational perturbations induce a significant change in the orbit’s inclination (North-South direction) and a slow precession in the East-West direction[10]. Station keeping is performed periodically using thrusters and on-board propellant to correct for these deviations. These station-keeping maneuvers can be scheduled manually from the ground or performed autonomously on-board the satellite, using high-impulse chemical propulsion or low-thrust propulsion[11,12,13,14]. It is imperative that station-keeping maneuvers be performed in an efficient manner, as the lifetime of a satellite is dictated by its fuel remaining on board. The amount of fuel required for station keeping is computed in terms ofΔ​v\Delta v, which is defined in this note as theL1L_{1}norm of thrust normalized by the satellite’s mass.

The perturbations experienced by AMO satellites are notably different than those present in GEO. In particular, the perturbations in the orbit’s inclination (North-South direction) are an order of magnitude smaller, while the East-West and radial perturbations are much more significant[15,16]. This results in relatively quick deviations from a nominal areostationary orbit, which – along with the considerably large communication delay between Earth-based ground stations and Martian satellites – motivate the need for autonomous AMO station keeping control strategies.

Model predictive control (MPC) has been investigated for use with many spacecraft applications[17,18,19], including autonomous GEO station keeping[13]. MPC directly optimizes control actions through a finite length of time in the future, called the prediction horizon. The optimal control sequence is recomputed at each time step, resulting in a feedback policy. In order to directly optimize over the prediction horizon, a model of system dynamics is used to forecast how control actions affect the system’s trajectory. There is an inherent tradeoff between complexity in the prediction model and computational effort of the MPC policy. Developing a prediction model with linear system dynamics is desirable since it enables MPC to be solved through well-developed and efficient convex optimization strategies, which is critical when considering autonomous implementation on-board a satellite. MPC has been investigated for AMO station keeping[20,21,22,23], where it was shown that a significant tradeoff exists between fuel-efficiency and computational-efficiency. Specifically, the use of nonlinear MPC resulted in an annualΔ​v\Delta vof3.83.8m/s, while requiring computation power well-beyond the capabilities of flight computers[21,23]. An MPC policy using linear time-invariant (LTI) dynamics resulted in an annualΔ​v\Delta vof4.54.5m/s and was realistically solvable on-board a satellite as a quadratic program[20]. A linear time-varying (LTV) dynamic model was shown to yield a computationally-efficient MPC policy with an annualΔ​v\Delta vof3.73.7m/s[22], although the study in Ref.[22]noted that MPC policies with LTI or LTV dynamics exhibited performance that was very sensitive to the tuning of the MPC policy objective function and prediction horizon length.

This note presents a novel approach to MPC-based AMO station keeping that bridges the gap seen in prior work between fuel-efficiency and computational-efficiency. This is accomplished through the discovery and use of a fuel-free natural motion trajectory in the presence of the dominant radial and East-West non-Keplerian perturbing forces that maintains the satellite within one degree of longitude from a areostationary orbit. Two of these natural motion trajectories exist as limit cycles about the stable equilibrium longitudes located at17.92∘17.92^{\circ}West and167.83∘167.83^{\circ}East. They are the resulting motion in the presence of Mars’ non-homogeneous gravitational field, accounting for Keplerian and higher-order gravitational perturbations. The proposed MPC policy uses an LTV dynamic model that is derived by linearizing the satellite’s dynamics relative to the appropriate natural motion trajectory. The result is a station keeping policy that minimizes the fuel consumed, maintains thrust and station-keeping constraints, and is computationally tractable for on-board implementation as a quadratic program.

The novel contributions of this note include 1) an MPC-policy that, to the best of the knowledge of the authors’, achieves the lowestΔ​v\Delta vof any autonomous AMO station keeping policy that is formulated as a convex optimization problem and 2) a thorough assessment of the proposed MPC policy’s robustness to realistic model uncertainty, computation time requirements, and estimation errors. The robustness study presented in this note extends far beyond previous studies on MPC-based AMO station keeping[20,21,22,23], which all assumed perfect model information, instantaneous computations, and perfect state knowledge.

## 2Preliminaries

This section defines relevant vector notation, important reference frames, and the direction cosine matrix used to describe the relative orientation of the reference frames.

## 2.1Notation

Matrices are presented in boldface. Physical vectors are denoted as(⋅)→\underrightarrow{(\cdot)}. A reference frameℱc\mathcal{F}_{c}is defined by three orthonormal basis vectorsa→1{\underrightarrow{{a}}}^{1},a→2{\underrightarrow{{a}}}^{2}, anda→3{\underrightarrow{{a}}}^{3}, arranged in a right-handed fashion. The position vector describing the location of pointbbrelative to pointaaisr→b​a\underrightarrow{r}^{ba}, with its components resolved in reference frameℱc\mathcal{F}_{c}written as𝐫𝐜𝐛𝐚=[𝐫𝐜𝟏𝐛𝐚​𝐫𝐜𝟐𝐛𝐚​𝐫𝐜𝟑𝐛𝐚]𝖳\mbf{r}^{ba}_{c}=[r^{ba}_{c1}\,\,r^{ba}_{c2}\,\,r^{ba}_{c3}]^{\mathsf{T}}.

## 2.2Reference Frames

The center of Mars is defined by the unforced pointww. The reference frameℱa\mathcal{F}_{a}is defined such thata→1\underrightarrow{a}_{1}extends fromwwto0∘0^{\circ}latitude and longitude at January 1st, 2000 noon GMT (commonly referred to as the J2000 epoch). The basis vectora→3\underrightarrow{a}_{3}extends fromwwin the direction of geographical North, whilea→2\underrightarrow{a}^{2}is chosen to complete the definition of the right-handed reference frame. This frame is non-rotating and referred to as the Mars Centered Inertial (MCI) frame. A nominal areostationary orbit is described by a pointhhsuch thatr→h​w\underrightarrow{r}^{hw}is located in the equatorial plane and passes through a specified longitudeλ\lambda. Assuming Mars rotates at its mean rotation ratenncorresponding to approximately one rotation every24.624.6hours,‖r→h​w‖2\|\underrightarrow{r}^{hw}\|_{2}must be2.04277×1042.04277\times 10^{4}km to be consistent with a relative two-body orbit. This distance is defined asrnomr_{\text{nom}}; the nominal AMO semi-major axis. A second reference frame,ℱh\mathcal{F}_{h}, is defined such thath→1\underrightarrow{h}^{1}lies collinear withr→h​w\underrightarrow{r}^{hw}, andh→3\underrightarrow{h}^{3}lies collinear witha→3\underrightarrow{a}^{3}. This frame, referred to as Hill’s frame, is related to the MCI frame by the direction cosine matrix (DCM)𝐂𝐡𝐚​(𝐭)=𝐂𝟑​(𝐧​(𝐭−𝐭J2000)+λ)\mbf{C}_{ha}(t)=\mbf{C}_{3}(n(t-t_{\text{J2000}})+\lambda), where𝐂𝟑​(⋅)\mbf{C}_{3}(\cdot)is the DCM associated with a principle rotation abouta→3\underrightarrow{a}^{3}andtJ2000t_{\text{J2000}}is the time of the J2000 epoch.

## 3Dynamics of a Perturbed Areostationary Satellite

This section presents the dynamics of a satellite in a perturbed areostationary orbit, beginning with its general equations of motion, followed by a description of the relevant perturbations, a natural motion trajectory of the satellite, and a discrete-time, time-varying model describing its motion relative to the natural motion trajectory.

## 3.1Equations of Motion

Consider a spacecraft, modeled as a point with massmBm_{B}, located at point c in orbit around Mars. The state of the satellite,𝐱​(𝐭)∈ℝ𝟔\mbf{x}(t)\in\mathbb{R}^{6}, at timettis taken to be its position relative to a nominal areostationary orbit, resolved in Hill’s frame, and the rate of change of that quantity, which is defined as𝐱​(𝐭)=[𝐫𝐡𝐜𝐡𝖳​(𝐭)​𝐫˙𝐡𝐜𝐡𝖳​(𝐭)]𝖳\mbf{x}(t)=[\mbf{r}^{ch^{\mathsf{T}}}_{h}(t)\,\,\dot{\mbf{r}}^{ch^{\mathsf{T}}}_{h}(t)]^{\mathsf{T}}. The dependence of state, control, and perturbations on time are omitted throughout this note, except when necessary for clarity. It is assumed that the spacecraft is equipped with the ability to thrust in each axis. The equations of motion for this system are defined by the motion of the satellite relative to an unperturbed circular reference areostationary orbit and are given by[24]𝐱˙=𝐟​(𝐱,𝐮,𝐰​(𝐱,𝐭))=[𝐫˙𝐡𝐜𝐡𝟐​𝐧​𝐫˙𝐡𝟐𝐜𝐡+𝐧𝟐​𝐫𝐡𝟏𝐜𝐡−μ​(𝐫nom+𝐫𝐡𝟏𝐜𝐡)[(𝐫nom+𝐫𝐡𝟏𝐜𝐡)𝟐+(𝐫𝐡𝟐𝐜𝐡)𝟐+(𝐫𝐡𝟑𝐜𝐡)𝟐]𝟑/𝟐+μ𝐫nom𝟐+𝐰𝐡𝟏​(𝐱,𝐭)+𝐮𝟏𝐦𝐁−𝟐​𝐧​𝐫˙𝐡𝟏𝐜𝐡+𝐧𝟐​𝐫𝐡𝟐𝐜𝐡−μ​𝐫𝐡𝟐𝐜𝐡[(𝐫nom+𝐫𝐡𝟏𝐜𝐡)𝟐+(𝐫𝐡𝟐𝐜𝐡)𝟐+(𝐫𝐡𝟑𝐜𝐡)𝟐]𝟑/𝟐+𝐰𝐡𝟐​(𝐱,𝐭)+𝐮𝟐𝐦𝐁−μ​𝐫𝐡𝟑𝐜𝐡[(𝐫nom+𝐫𝐡𝟏𝐜𝐡)𝟐+(𝐫𝐡𝟐𝐜𝐡)𝟐+(𝐫𝐡𝟑𝐜𝐡)𝟐]𝟑/𝟐+𝐰𝐡𝟑​(𝐱,𝐭)+𝐮𝟑𝐦𝐁],\hskip-10.0pt\dot{\mbf{x}}=\mbf{f}(\mbf{x},\mbf{u},\mbf{w}(\mbf{x},t))=\left[\begin{matrix}\dot{\mbf{r}}^{ch}_{h}\vskip 5.0pt\\
2n\dot{r}^{ch}_{h2}+n^{2}r^{ch}_{h1}-\frac{\mu(r_{\text{nom}}+r^{ch}_{h1})}{\left[(r_{\text{nom}}+r^{ch}_{h1})^{2}+(r^{ch}_{h2})^{2}+(r^{ch}_{h3})^{2}\right]^{3/2}}+\frac{\mu}{r_{\text{nom}}^{2}}+w_{h1}(\mbf{x},t)+\frac{u_{1}}{m_{B}}\vskip 5.0pt\\
-2n\dot{r}^{ch}_{h1}+n^{2}r^{ch}_{h2}-\frac{\mu r^{ch}_{h2}}{\left[(r_{\text{nom}}+r^{ch}_{h1})^{2}+(r^{ch}_{h2})^{2}+(r^{ch}_{h3})^{2}\right]^{3/2}}+w_{h2}(\mbf{x},t)+\frac{u_{2}}{m_{B}}\vskip 5.0pt\\
-\frac{\mu r^{ch}_{h3}}{\left[(r_{\text{nom}}+r^{ch}_{h1})^{2}+(r^{ch}_{h2})^{2}+(r^{ch}_{h3})^{2}\right]^{3/2}}+w_{h3}(\mbf{x},t)+\frac{u_{3}}{m_{B}}\end{matrix}\right],(1)

whereμ\muis the Martian gravitational constant,𝐮=[𝐮𝐡𝟏​𝐮𝐡𝟐​𝐮𝐡𝟑]𝖳\mbf{u}=[u_{h1}\,\,u_{h2}\,\,u_{h3}]^{\mathsf{T}}is the thrust vector, expressed in Hill’s frame, and𝐰​(𝐱,𝐭)=[𝐰𝐡𝟏​(𝐱,𝐭)​𝐰𝐡𝟐​(𝐱,𝐭)​𝐰𝐡𝟑​(𝐱,𝐭)]𝖳\mbf{w}(\mbf{x},t)=[w_{h1}(\mbf{x},t)\,\,w_{h2}(\mbf{x},t)\,\,w_{h3}(\mbf{x},t)]^{\mathsf{T}}is the acceleration experienced by the spacecraft due to exogenous perturbations, also expressed in Hill’s frame.

## 3.2Perturbations

The exogenous forces experienced by the spacecraft that are considered in this analysis fall into three categories: third-body gravitya→3rd\underrightarrow{a}_{\text{3rd}}, solar radiation pressurea→SRP\underrightarrow{a}_{\text{SRP}}, and gravitational harmonicsa→harm\underrightarrow{a}_{\text{harm}}. The exogenous perturbation force is therefore decomposed asw→=a→3rd+a→SRP+a→harm.\underrightarrow{w}=\underrightarrow{a}_{\text{3rd}}+\underrightarrow{a}_{\text{SRP}}+\underrightarrow{a}_{\text{harm}}.(2)

Third-body gravity considers the gravitational force on the spacecraft from a body that is not Mars and takes on the forma→3rd=∑i−μi​rc​i→‖r→c​i‖3,\underrightarrow{a}_{\text{3rd}}=\sum_{i}-\frac{\mu_{i}\underrightarrow{r^{ci}}}{\left\|\underrightarrow{r}^{ci}\right\|^{3}},(3)

whereμi\mu_{i}is the gravitational parameter of theithi^{\text{th}}body, andr→c​i\underrightarrow{r}^{ci}is the position of the spacecraft relative to theithi^{\text{th}}body. For the simulations in this study, the effects of Mars’ moons Phobos and Deimos and the Sun are considered.

The effects of solar radiation pressure are small, and a discussion of their mechanics is beyond the scope of this note. A discussion of their effects on AMO station keeping is presented in Ref.[23].

The most significant perturbation experienced by areostationary satellites is caused by Mars’ nonuniform gravitational potential. The orbits of terrestrial satellites are influenced greatly by Earth’s equatorial bulge, termed the J2 perturbation. J2 refers to the term a particular series expansion describing a primary body’s gravitational potential[25]. The basis functions for this expansion are called spherical harmonics.
Mars’ gravitational potential can similarly be described using spherical harmonic expansion. The gravitational potentialUU, is given in spherical coordinatesr,λ,ϕr,\lambda,\phi: radial distance, longitude, and latitude respectively, and is described by[25]U=μr​[∑l=0∞(RMr)l​∑m=0l(Cl​m​cos⁡m​λ+Sl​m​sin⁡m​λ)​Pl​m​(sin⁡ϕ)],U=\frac{\mu}{r}\left[\sum_{l=0}^{\infty}\left(\frac{R_{M}}{r}\right)^{l}\sum_{m=0}^{l}\left(C_{lm}\cos{m\lambda}+S_{lm}\sin{m\lambda}\right)P_{lm}(\sin{\phi})\right],(4)

whereRMR_{M}is Mars’ equatorial radius,Cl​m,Sl​mC_{lm},S_{lm}are coefficients, andPl​mP_{lm}are Legendre polynomials. The perturbation due to the gravitational anomaly is given bya→harm=∇U−μ​r→c​w‖r→c​w‖3,\underrightarrow{a}_{\text{harm}}=\nabla U-\frac{\mu\underrightarrow{r}^{cw}}{\left\|\underrightarrow{r}^{cw}\right\|^{3}},(5)

where the nominal Keplerian gravitation term has been subtracted to leave only the perturbing acceleration. In this note, the coefficients from the GMM2B model presented in Ref.[26]are used up to a fifth order. This is consistent with the modeling choice used in Ref.[23], where it was shown that higher-order terms beyond fifth order result in a negligible change in the resulting gravitational acceleration.

The East-West (i.e., ‘along-track’) gravitational anomaly perturbations experienced by an areostationary satellite are heavily dependent on longitude. There exist two longitudes that are stable equilibria for East-West motion;17.92∘17.92^{\circ}West and167.83∘167.83^{\circ}East[27]. These longitudes—denoted “stable longitudes”—provide attractive targets for areostationary missions, since they not only experience small perturbations in one principle axis, but they also experience a restoring force when deviating from the nominal longitude.

## 3.3Natural Motion Trajectory

Consider a satellite in AMO at a stable longitude of17.92∘17.92^{\circ}West. The perturbations experienced by the satellite due to the gravitational anomaly modeled to a fifth order are shown in Table1. The radial perturbation is nearly three orders of magnitude greater than the perturbations in the other two directions at this longitude. The coupling between East-West and radial motion seen in Eq. (1) combined with the restorative force in the East-West perturbation induce a periodic variation in the satellite’s orbit in the form of a limit cycle. This motion is shown in Fig.1, where the orbit periodically falls ahead and behind of the nominal AMO. This manifests as a drift in longitude by about a degree in either direction with a period of approximately 127 days. Since this bounded longitudinal motion is caused by the radial and along-track spherical harmonics, a satellite following this trajectory would theoretically only have to account for the North-South (cross-track) spherical harmonic and non-spherical-harmonic perturbations to remain on this trajectory. Allowing for this drift effectively eliminates the need to cancel out the effects of the largest perturbation during station keeping. Trigonometric analysis shows that if a receiver is located on the Martian surface at17.92∘17.92^{\circ}West, a deviation in an areostationary satellite’s longitude of1∘1^{\circ}would correspond to a1.2∘1.2^{\circ}change in elevation from the horizon.Table 1:Spherical harmonic perturbations experienced by an AMO satellite at longitude17.92∘17.92^{\circ}West.AxisAcceleration (m/s2)Radial−6.7448×10−9-6.7448\times 10^{-9}East-West7.9315×10−127.9315\times 10^{-12}North-South−2.0131×10−11-2.0131\times 10^{-11}Figure 1:The natural motion trajectory caused by spherical harmonic perturbations about17.92∘17.92^{\circ}West.

A station keeping policy proposed in this note attempts to keep the satellite state close to the state trajectory defined by this limit cycle. The satellite’s state on this trajectory is given by𝐱¯​(t)\bar{\mbf{x}}(t), which evolves according to𝐱¯˙=𝐟​(𝐱¯,𝟎,𝐰¯​(𝐱¯)),\dot{\bar{\mbf{x}}}=\mbf{f}(\bar{\mbf{x}},\mbf{0},\bar{\mbf{w}}(\bar{\mbf{x}})),(6)

where𝐰¯\bar{\mbf{w}}contains only the radial and along track terms of the perturbations.

## 3.4Discrete-Time Linear Time-Varying Model

This section describes a linear prediction model approximating the nonlinear dynamics in Eq. (1) in a similar to the method presented in Ref.[22]. The goal is to generate a discrete-time, linear time-varying (LTV) model that approximates the motion of the point-mass satellite relative to a reference trajectory, from each temporal node to the next. This replaces the nonlinear system of differential equations describing the dynamics with an approximate system of linear algebraic equations, which is computationally tractable to use as a prediction model in real time. In this case, the limit cycle state𝐱¯\bar{\mbf{x}}is chosen as the reference state trajectory. Since the limit cycle is a natural motion trajectory, the reference control trajectory is defined as𝐮¯=𝟎\bar{\mbf{u}}=\mbf{0}.

A continuous-time LTV system is constructed by taking a first-order Taylor’s series expansion about a reference trajectory, given by𝐱˙​(t)≈𝐀​(𝐭)​δ​𝐱​(𝐭)+𝐁​(𝐭)​δ​𝐮​(𝐭)+𝐳​(𝐭),\dot{\mbf{x}}(t)\approx\mbf{A}(t)\delta\mbf{x}(t)+\mbf{B}(t)\delta\mbf{u}(t)+\mbf{z}(t),(7)

whereδ​𝐱=𝐱−𝐱¯\delta\mbf{x}=\mbf{x}-\bar{\mbf{x}},δ​𝐮=𝐮−𝐮¯\delta\mbf{u}=\mbf{u}-\bar{\mbf{u}},𝐀​(𝐭)=∂∂𝐱​𝐟​(𝐱,𝐮,𝐰,𝐭)|𝐱¯,𝐮¯,𝐰​(𝐱¯),𝐭\mbf{A}(t)={\frac{\partial}{\partial x}}\mbf{f}(\mbf{x},\mbf{u},\mbf{w},t)\left.\right|_{\bar{\mbf{x}},\bar{\mbf{u}},\mbf{w}(\bar{\mbf{x}}),t},𝐁​(𝐭)=∂∂𝐮​𝐠​(𝐱,𝐮,𝐭)|𝐱¯,𝐮¯,𝐰​(𝐱¯),𝐭\mbf{B}(t)={\frac{\partial}{\partial u}}\mbf{g}(\mbf{x},\mbf{u},t)\left.\right|_{\bar{\mbf{x}},\bar{\mbf{u}},\mbf{w}(\bar{\mbf{x}}),t}, and𝐳​(𝐭)=𝐟​(𝐱¯,𝐮¯,𝐰​(𝐱¯),𝐭)\mbf{z}(t)=\mbf{f}(\bar{\mbf{x}},\bar{\mbf{u}},\mbf{w}(\bar{\mbf{x}}),t). In Eq. (7), the perturbations𝐰​(𝐱¯)\mbf{w}(\bar{\mbf{x}})are evaluated at the reference state, but include the terms neglected in𝐰¯\bar{\mbf{w}}, allowing the resulting prediction model to capture the cross-track terms.

For the prediction model to be used within a direct numerical optimization framework, it must express the dynamics between discrete timesteps. Applying a zeroth-order hold[28]to the inputs, the discrete-time LTV system dynamics are given by𝐱𝐤+𝟏≈𝐀𝐤​𝐱𝐤+𝐁𝐤​𝐮𝐤+𝐳𝐤,\mbf{x}_{k+1}\approx\mbf{A}_{k}\mbf{x}_{k}+\mbf{B}_{k}\mbf{u}_{k}+\mbf{z}_{k},(8)

where𝐱𝐤\mbf{x}_{k}and𝐮𝐤\mbf{u}_{k}are the state and control input attkt_{k}, respectively, and𝐀𝐤\displaystyle\mbf{A}_{k}=𝚽​(tk+1,tk),\displaystyle={\boldsymbol{\Phi}}(t_{k+1},t_{k}),(9a)𝐁𝐤\displaystyle\mbf{B}_{k}=𝐀𝐤​∫𝐭𝐤𝐭𝐤+𝟏𝚽​(τ,𝐭𝐤)−𝟏​𝐁​(τ)​dτ,\displaystyle=\mbf{A}_{k}\int_{t_{k}}^{t_{k+1}}{\boldsymbol{\Phi}}(\tau,t_{k})^{-1}\mbf{B}(\tau)\mathrm{d}\tau,(9b)𝐳𝐤\displaystyle\mbf{z}_{k}=∫tktk+1𝚽​(τ,tk)−1​𝐳​(τ)​dτ.\displaystyle=\int_{t_{k}}^{t_{k+1}}{\boldsymbol{\Phi}}(\tau,t_{k})^{-1}\mbf{z}(\tau)\mathrm{d}\tau.(9c)

The state transition matrix𝚽​(tk+1,tk){\boldsymbol{\Phi}}(t_{k+1},t_{k})is obtained by numerically integratingdd​t​𝚽​(t,t0)=𝐀​(𝐭)​𝚽​(𝐭,𝐭𝟎)\frac{\mathrm{d}}{\mathrm{d}t}{\boldsymbol{\Phi}}(t,t_{0})=\mbf{A}(t){\boldsymbol{\Phi}}(t,t_{0})subject to the initial condition𝚽​(t0,t0)=𝟏{\boldsymbol{\Phi}}(t_{0},t_{0})=\mbf{1}. As𝐀𝐤,𝐁𝐤,\mbf{A}_{k},\mbf{B}_{k},and𝐳𝐤\mbf{z}_{k}are found through integration of values of𝚽{\boldsymbol{\Phi}}between time indices, Eq. (9) and the state transition matrix can be numerically integrated simultaneously.

This formulation is quite general, and implementation must be catered to the specific AMO station-keeping application. In this system, the calculation of𝐁​(𝐭)\mbf{B}(t)is trivial and can be done analytically. The calculation of𝐀​(𝐭)\mbf{A}(t)is complicated by the spatial dependence of the disturbance terms. In Ref.[22], the nominal areostationary orbit was used as the reference trajectory where the spatial dependence of the perturbations are insignificant, thus∂𝐰∂x{\frac{\partial\mbf{w}}{\partial x}}was approximated as𝟎\mbf{0}. In this note, the limit cycle is used as a reference, where the trajectory strays hundreds of kilometers from the nominal stationary point, causing this approximation to no longer be accurate. As the partial derivatives of truncations of Eq. (4) are cumbersome to write analytically,𝐀​(𝐭)\mbf{A}(t)is calculated using a complex-step numerical differentiation scheme inspired by Refs.[29,30], which makes use of the functionatan2ComplexStep.m[31]in MATLAB.

In the implementation of control policies, it is often advantageous to define states relative to the desired reference, resulting in the perturbed dynamicsδ​𝐱𝐤+𝟏≈𝐀𝐤​δ​𝐱𝐤+𝐁𝐤​δ​𝐮𝐤+δ​𝐳𝐤,\delta\mbf{x}_{k+1}\approx\mbf{A}_{k}\delta\mbf{x}_{k}+\mbf{B}_{k}\delta\mbf{u}_{k}+\delta\mbf{z}_{k},(10)

whereδ​𝐳𝐤=𝐀𝐤​𝐱¯𝐤+𝐁𝐤​𝐮¯𝐤+𝐳𝐤−𝐱¯𝐤+𝟏.\delta\mbf{z}_{k}=\mbf{A}_{k}\bar{\mbf{x}}_{k}+\mbf{B}_{k}\bar{\mbf{u}}_{k}+\mbf{z}_{k}-\bar{\mbf{x}}_{k+1}.(11)

The termδ​𝐳𝐤\delta\mbf{z}_{k}accounts for the difference between the reference dynamics and a truly open-loop trajectory, a consequence of the cross-track perturbation terms being absent in𝐰¯\bar{\mbf{w}}. This completes the derivation of the discrete-time LTV prediction model linearized about a natural motion trajectory.

## 4Model Predictive Control Station-Keeping Methodology

The MPC station-keeping policy proposed in this work is similar to the linear time-varying MPC policy presented in Ref.[22], with the main difference being that the dynamics are defined relative to the natural motion trajectory described in Section3.3. At each time step, the MPC policy optimizes control actions a set number of time steps in the future, called the prediction horizon. The objective of this policy is to minimize a quadratic function of state deviation and control action across the prediction horizon using a linear time-varying discrete-time model to predict how the states evolve across the horizon. The first time step of the optimal control input sequence is then applied until the next time step, when the algorithm repeats.
It should be noted that the propagation of the system to obtain the model in Eq. (8) is a fully open-loop process, and thus may be computed a priori. The key difference in this novel implementation compared to the method in Ref.[22]is that rather than using the AMO orbit as the reference trajectory, the dynamics used in the prediction model in Eq. (10) are evaluated along the limit cycle discussed in Section3. Previous policies achieved fuel savings by allowing a satellite to drift within a defined station keeping window near the desired latitude and longitude. By redefining the states relative to the limit cycle in this work, the control policy allows for similar drift relative to the longitudinal variation in the natural motion trajectory. The MPC problem is formulated asminimize𝓧t,𝓤t,𝝂\displaystyle\underset{\boldsymbol{\mathcal{X}}_{t},\boldsymbol{\mathcal{U}}_{t},{\boldsymbol{\nu}}}{\text{minimize}}𝝂𝖳​𝐒​𝝂+∑𝐤=𝟎𝐍−𝟏δ​𝐮𝐤|𝐭𝖳​𝐑​δ​𝐮𝐤|𝐭\displaystyle{\boldsymbol{\nu}}^{\mathsf{T}}\mbf{S}{\boldsymbol{\nu}}+\sum^{N-1}_{k=0}\delta\mbf{u}_{k|t}^{\mathsf{T}}\mbf{R}\delta\mbf{u}_{k|t}subject toδ​𝐱𝐤+𝟏|𝐭=𝐀𝐤|𝐭​δ​𝐱𝐤|𝐭+𝐁𝐤|𝐭​δ​𝐮𝐤|𝐭+δ​𝐳𝐤|𝐭,∀𝐤∈[𝟎⋯𝐍−𝟏],\displaystyle\delta\mbf{x}_{k+1|t}=\mbf{A}_{k|t}\delta\mbf{x}_{k|t}+\mbf{B}_{k|t}\delta\mbf{u}_{k|t}+\delta\mbf{z}_{k|t},\qquad\forall k\in\left[0\qquad\cdots\qquad N-1\right],δ​𝐱𝟎|𝐭=δ​𝐱​(𝐭),\displaystyle\delta\mbf{x}_{0|t}=\delta\mbf{x}(t),δ​𝐱min−𝝂≤δ​𝐱𝐤|𝐭≤δ​𝐱max+𝝂,∀𝐤∈[𝟎⋯𝐍],\displaystyle\delta\mbf{x}_{\text{min}}-{\boldsymbol{\nu}}\leq\delta\mbf{x}_{k|t}\leq\delta\mbf{x}_{\text{max}}+{\boldsymbol{\nu}},\qquad\forall k\in\left[0\qquad\cdots\qquad N\right],𝐟minthrust≤δ​𝐮𝐤|𝐭≤𝐟maxthrust,∀𝐤∈[𝟎⋯𝐍−𝟏],\displaystyle\mbf{f}_{\text{min}}^{\text{thrust}}\leq\delta\mbf{u}_{k|t}\leq\mbf{f}_{\text{max}}^{\text{thrust}},\qquad\forall k\in\left[0\qquad\cdots\qquad N-1\right],𝟎≤𝝂,\displaystyle\mbf{0}\leq{\boldsymbol{\nu}},

whereNNis the prediction horizon,𝓧t={δ​𝐱𝟎|𝐭,…,δ​𝐱𝐍−𝟏|𝐭}\boldsymbol{\mathcal{X}}_{t}=\{\delta\mbf{x}_{0|t},\ldots,\delta\mbf{x}_{N-1|t}\},𝓤t={δ​𝐮𝟎|𝐭,…,δ​𝐮𝐍−𝟏|𝐭}\boldsymbol{\mathcal{U}}_{t}=\{\delta\mbf{u}_{0|t},\ldots,\delta\mbf{u}_{N-1|t}\}, and𝐑=𝐑𝖳>𝟎\mbf{R}=\mbf{R}^{\mathsf{T}}>0is the constant control weighting matrix. The subscript notationk|tk|tdenotes the state or control inputkkprediction steps ahead of timett. For example,𝐱𝐤|𝐭\mbf{x}_{k|t}is the predicted statekksteps ahead of timett.
The variablesδ​𝐱min\delta\mbf{x}_{\text{min}}andδ​𝐱max\delta\mbf{x}_{\text{max}}are defined based on the prescribed station keeping window in which the spacecraft can drift from the natural motion trajectory. Specifically,δ​𝐱max=[∞​𝐫nom​tan⁡(λmax)​𝐫nom​tan⁡(ϕmax)​0  0  0]𝖳\delta\mbf{x}_{\text{max}}=[\infty\,\,r_{\text{nom}}\tan(\lambda_{\text{max}})\,\,r_{\text{nom}}\tan(\phi_{\text{max}})\,\,0\,\,0\,\,0]^{\mathsf{T}}andδ​𝐱min=−δ​𝐱max\delta\mbf{x}_{\text{min}}=-\delta\mbf{x}_{\text{max}}, whereλmax\lambda_{\text{max}}andϕmax\phi_{\text{max}}are the maximum allowable drift in longitude and latitude, respectively. The slack variable𝝂∈ℝn{\boldsymbol{\nu}}\in\mathbb{R}^{n}relaxes the station-keeping window constraint and allows for infeasible initial conditions. This is referred to as a “soft constraint." Without this, the solution to the optimization problem would not exist should the spacecraft ever leave the window. With a sufficiently large weight𝐒=𝐒𝖳>𝟎\mbf{S}=\mbf{S}^{\mathsf{T}}>0, the controller strictly enforces the window while the spacecraft is on the interior. If model inaccuracies or unforeseen environmental factors lead to the spacecraft exiting the window, the single slack variable across the prediction horizon will prevent further drift outside the window, while discouraging over-actuation to satisfy the bounds.
The maximum and minimum allowable thrust inputs expressed in Hill’s frame are defined as𝐟max\mbf{f}_{\text{max}}and𝐟min\mbf{f}_{\text{min}}, respectively, and𝐟min=−𝐟max\mbf{f}_{\text{min}}=-\mbf{f}_{\text{max}}.

## 5Numerical Results

Numerical simulation results are presented in this section to demonstrate the performance of the proposed station-keeping policy. A description of the simulation setup is first presented, followed by nominal results with the proposed station-keeping policy, comparisons to existing AMO station-keeping policies in the literature, and a robustness study of the proposed station-keeping policy.

## 5.1Simulation Setup

The spacecraft is approximated as a point mass with mass ofmB=4000m_{B}=4000kg, solar facing area of37.537.5m2, and a solar radiation constant of4.5×10−64.5\times 10^{-6}. The spacecraft is placed in a nominal AMO at a stable longitude of17.92∘17.92^{\circ}West. The spacecraft’s maximum thrust is set to𝐟max=[50  50  50]𝖳\mbf{f}_{\text{max}}=[50\,\,50\,\,50]^{\mathsf{T}}mN based on the assumption of low-thrust propulsion. The station-keeping window is defined by maximum longitude and latitude deviations ofλmax=0.2∘\lambda_{\text{max}}=0.2^{\circ}andϕmax=0.05∘\phi_{\text{max}}=0.05^{\circ}. For simulations with the proposed policy, these maximum deviations are defined relative to the natural motion trajectory, while simulations of the policies in Refs.[20,21,23,22,1]constrain these longitude and latitude deviations relative to the true AMO stable longitude of17.92∘17.92^{\circ}West and0∘0^{\circ}of latitude.

The MPC station-keeping policy uses discrete time steps of lengthΔ​t=1\Delta t=1hour and a prediction horizon of1818hours (N=18N=18) was chosen through tuning of the proposed policy to ensure satisfactory performance across all results. Values of𝐑=5.6×𝟏𝟎𝟓⋅𝟏\mbf{R}=5.6\times 10^{5}\cdot\mbf{1}, and𝐒=𝟏𝟎𝟎⋅𝟏\mbf{S}=100\cdot\mbf{1}are used within the cost function. These variables are chosen to emphasize the desire to minimize control effort, without concern as to where the spacecraft is within the station-keeping window. This MPC optimization problem is expressed as a convex quadratic problem, and solved using MATLAB’squadprog.mfunction, using theinterior-point-convexalgorithm.

All numerical simulations presented in this work begin on January 1st, Noon GMT, 2000 and involve running the appropriate station-keeping policy for570570orbits. The first215215orbits to allow the North-South station keeping bound to be reached (i.e., the system is undergoing a transient response), while the last355355orbits represent one Earth year of steady-state response. All annualΔ​v\Delta vcomputations are made over the final355355orbits to be representative of the steady-state fuel requirements. To remain consistent with the zero-order hold used in the model of the MPC policy, the control thrust is held constant between time steps. The system is propagated forward in time according to the nonlinear dynamics in Eq. (1) using MATLAB’sode45.m.

## 5.2Nominal Results with Proposed Station-Keeping Policy

The proposed MPC station-keeping policy is implemented in a simulation of the spacecraft’s nonlinear dynamics, where perfect state measurements and knowledge of all perturbations are assumed to be available. The resulting trajectory is provided in Fig.2, where the radius, latitude, and longitude of the spacecraft over the entire year is included in Fig.2(a)and zoomed in versions of these plots over the first 50 days are included in Fig.2(b). The thrust control inputs associated with this simulation are provided in Fig.3(a)and the accumulatedΔ​v\Delta vis found in Fig.3(b).(a)Full one-year simulation results.(b)First 50-day simulation results.Figure 2:Simulated year of the proposed station-keeping policy tracking the natural motion trajectory.(a)(b)Figure 3:Control inputs during a simulated year of the proposed station-keeping policy tracking the natural motion trajectory.

The total annualΔ​v\Delta vachieved by the policy is3.423.42m/s, effectively all of which is in the North-South direction (theΔ​v\Delta vexpended in the radial and East-West directions is5.8×10−65.8\times 10^{-6}m/s and1.7×10−61.7\times 10^{-6}, respectively). This highlights the efficiency of the proposed station-keeping policy at mitigating the effect of time-varying and 3rd-body disturbances in the radial and East-West directions. As observed with prior studies, a minimum amount of thrust in the North-South direction is needed to prevent secular drift in the spacecraft’s inclination. It is notable in Fig.2that the spacecraft does drift within the allowable station-keeping window relative to the natural motion trajectory, likely by taking advantage of the periodic nature of the disturbances acting on the spacecraft to avoid the need to expend fuel.

## 5.3Comparison to Prior AMO Station-Keeping Policies

To demonstrate the performance of the proposed station-keeping policy relative to methods in the literature, simulations are performed with the LTI-MPC policy from Ref[20], the LTV-MPC policy from Ref.[22], and the nonlinear MPC (nMPC) policy from Refs.[21,23]. These policies are implemented within the same simulation setup described in Section5.1and with as many of the same tuning parameters used within the proposed policy as possible. The main difference with the policies in the literature is that a static station keeping window is used (i.e., the station-keeping window is defined relative to the nominal AMO orbit at a stable longitude of17.92∘17.92^{\circ}West). It is also worth noting that to maintain consistency with Refs.[21,23], the cost function of the nMPC policy is the the 1-norm of the thrust applied, rather than the quadratic cost function used by the other policies.

The annualΔ​v\Delta vconsumed by all policies is reported in Table2, where the proposed policy has the lowest totalΔ​v\Delta vthat is roughly the same as the nonlinear MPC policy from Refs.[21,23]. The LTI-MPC and LTV-MPC policies are the only known convex-optimization-based AMO station-keeping policies in the literature and require27.327.3%22.122.1% more totalΔ​v\Delta vthan the proposed convex-optimization-based policy. This highlights the contribution of this work, where the proposed policy can be solved as a convex optimization problem, which enables real-time implementation onboard a spacecraft, while achieving similar performance to the computationally-prohibitive nonlinear MPC policy. It is important to note that the high performance and low computation properties of the proposed policy come at the expense of the spacecraft not maintaining a true AMO orbit. In contrast to the LTI-MPC, LTV-MPC, and nMPC AMO station-keeping policies that maintain the spacecraft within±0.2∘\pm 0.2^{\circ}of the stable longitude of17.92∘17.92^{\circ}West, the proposed policy maintains the spacecraft within±0.2∘\pm 0.2^{\circ}of the natural motion trajectory, resulting in roughly up to±1.2∘\pm 1.2^{\circ}of longitudinal deviation from17.92∘17.92^{\circ}West.Table 2:Comparison of the annualΔ​v\Delta vrequired with different station keeping policies.PolicyRadialΔ​v\Delta v(m/s)E-WΔ​v\Delta v(m/s)N-SΔ​v\Delta v(m/s)TotalΔ​v\Delta v(m/s)LTI-MPC[20]0.1610.9003.2904.350LTV-MPC[22]0.1950.6083.3714.175nMPC[21,23]0.0260.0883.3093.423Proposed Policy and Trajectory5.797×10−65.797\times 10^{-6}1.724×10−61.724\times 10^{-6}3.4183.4183.4183.418

## 5.4Robustness Study of Proposed AMO Station-Keeping Policy

The proposed limit-cycle following AMO station-keeping policy is implemented in realistic off-nominal conditions to assess its robustness properties. The test cases outlined in this section include uncertainty in the magnitude of thrust provided by the thrusters, uncertainty in the mass of the spacecraft, a lack of knowledge of the time-varying perturbations acting on the spacecraft, a time-delay due to computation time, and the presence of navigation errors.

Thrust uncertainty is injected into the simulation by adding a bias to the thrust commanded by the MPC policy. This is meant to emulate a thruster with imperfect timing or thrust characterization. The station keeping policy simulated with a 15% increase and 15% decrease in unmodeled thrust results in a 1.4% increase and 1.9% increase in annualΔ​v\Delta v, respectively, compared to the nominal results.

The effect of mass uncertainty is assessed by perturbing the mass of the spacecraft’s mass to 20% less than the mass modeled in the MPC policy. This perturbed simulation results in a 2.6% increase in annualΔ​v\Delta vcompared to the nominal results.

The nominal results assume accurate knowledge of all perturbation forces acting on spacecraft. In reality the spacecraft flight computer will not be able to store ephemeris data for all gravitational bodies acting on it. To assess robustness to this lack of information, simulations are performed without the MPC policy having knowledge of the time-varying gravitational perturbations due to the Martian moons and the Sun. This results in a 3.8% increase in annualΔ​v\Delta vfrom the nominal results.

The implementation of MPC on a flight computer imposes challenges due to limited on-board computational power and memory. Prior work claimed that the long time steps associated with MPC-based station keeping policies can mitigate this issue. For example, the 1-hour time steps used in this work may provide substantial time for the relatively simple linear MPC problem to solved, even on a radiation-hardened flight computer. Although this claim may be sensible, it has not been tested in prior MPC-based station keeping policies. To better understand this effect, the proposed MPC policy is implemented such that there is a one hour (one time step) delay between the measurement of the spacecraft state and the implementation of the MPC control input. The resulting annualΔ​v\Delta vis a 3.9% increase from the nominal case.

In practice, navigation errors will lead to uncertainty in the spacecraft state used to implement the MPC policy. To assess robustness to this uncertainty, the proposed station-keeping policy is implemented with zero-mean Gaussian noise added to the spacecraft’s position and velocity. Specifically, a standard deviation of 100 m in position and 0.1 m/s in velocity is used to mimic values that are obtainable in GEO[13]. This results in a 165% increase in annualΔ​v\Delta v, with the bulk of this increase occurring due to additional thrust maneuvers in the radial and East-West directions. Although it is clear that current navigation technology is not capable of such small errors around Mars, this result demonstrates the importance of establishing Mars navigation systems to accurately perform station keeping of spacecraft orbiting Mars.

A summary of the annualΔ​v\Delta vwith all of the robustness case studies is provided in Table3. TheΔ​v\Delta vaccumulated in the radial, East-West (E-W), and North-South (N-S) directions is also provided in this table. Other than the case with navigation errors, the performance of the proposed station-keeping policy is very robust to realistic modeling errors and computational delays.Table 3:Comparison of the annualΔ​v\Delta vrequired with different cases of the proposed station keeping policy.CaseRadialΔ​v\Delta v(m/s)E-WΔ​v\Delta v(m/s)N-SΔ​v\Delta v(m/s)TotalΔ​v\Delta v(m/s)Nominal5.797×10−65.797\times 10^{-6}1.724×10−61.724\times 10^{-6}3.4183.4183.4183.41815% Increase in Thrust9.553×10−39.553\times 10^{-3}0.03040.03043.4273.4273.4673.46715% Decrease in Thrust7.364×10−37.364\times 10^{-3}0.02340.02343.4523.4523.4823.48220% Decrease in Mass0.01210.01210.03930.03933.4563.4563.5083.508No Knowledge of Time-Varying Perts.2.773×10−62.773\times 10^{-6}6.897×10−66.897\times 10^{-6}3.5493.5493.5493.5491-Hour Computation Delay5.824×10−65.824\times 10^{-6}1.739×10−51.739\times 10^{-5}3.5503.5503.5503.550Navigation Errors1.0881.0883.6503.6504.3144.3149.0459.045

## 6Conclusion

A limit cycle natural motion trajectory in the longitudinal and radial motion of AMO satellites about a stable longitude was identified. A linear discrete-time model of system dynamics near this natural motion trajectory was constructed and leveraged to enable an efficient predictive station keeping policy. This station keeping policy rivals the performance of nonlinear MPC policies and achieves the lowestΔ​v\Delta vof any convex AMO station keeping policy in the literature. Moreover, the robustness analysis performed in this work provides an important step towards practical implementation compared to prior AMO station keeping methods in the literature.

## Acknowledgments

N. A. Gall and R. J. Caverly acknowledge support from a Early Career Faculty grant from NASA’s Space Technology Research Grants Program under award No. 80NSSC23K0075, as well as the University of Minnesota’s Research & Innovation Office and the University of Minnesota’s Office of Undergraduate Research. R. D. Halverson acknowledges partial support by the Science, Mathematics, and Research for Transformation (SMART) Scholarship-for-Service Program within the Department of Defense
(DoD), USA.

## References
- Gall and Caverly [2025]Gall, N. A., and Caverly, R. J., “Predictive Station Keeping of
Areostationary Satellites Using Natural Motion Trajectories,”2025
Regional Student Conferences, 2025.10.2514/6.2025-99106, AIAA 2025-99106.
- Hastrup et al. [2003]Hastrup, R. C., Bell, D. J., Cesarone, R. J., Edwards, C. D., Ely, T. A.,
Guinn, J. R., Rosell, S. N., Srinivasan, J. M., and Townes, S. A.,
“Mars Network for Enabling Low-Cost Missions,”Acta
Astronautica, Vol. 52, No. 2–6, 2003, pp. 227–235.0.1016/S0094-5765(02)00161-3.
- Lock et al. [2016]Lock, R. E., Edwards, C. D., Nicholas, A. K., Woolley, R., and Bell, D. J.,
“Small Areostationary Telecommunications Orbiter Concepts for Mars
in the 2020s,”IEEE Aerospace Conference, 2016, pp. 1–12.10.1109/AERO.2016.7500899.
- Edwards et al. [2016]Edwards, C. D., Bell, D. J., Biswas, A., Cheung, K.-M., and Lock, R. E.,
“Proximity Link Design and Performance Options for a Mars
Areostationary Relay Satellite,”IEEE Aerospace Conference, 2016, pp.
1–10.10.1109/AERO.2016.7500680.
- Babuscia et al. [2017]Babuscia, A., Divsalar, D., and Cheung, K. M., “CDMA Communication
System for Mars Areostationary Relay Satellite,”IEEE Aerospace
Conference, 2017, pp. 1–10.10.1109/AERO.2017.7943941.
- Breidenthal et al. [2018]Breidenthal, J., Xie, H., Lau, C.-W., and MacNeal, B., “Space and Earth
Terminal Sizing for Future Mars Missions,”SpaceOps Conference, 2018.10.2514/6.2018-2426, AIAA 2018-2426.
- Pontani et al. [2022]Pontani, M., Pustorino, M., and Teofilatto, P., “Mars Constellation
Design and Low-Thrust Deployment Using Nonlinear Orbit Control,”The
Journal of the Astronautical Sciences, Vol. 69, 2022, pp. 1691–1725.10.1007/s40295-022-00352-w.
- Romero et al. [2017]Romero, P., Pablos, B., and Barderas, G., “Analysis of Orbit
Determination From Earth-Based Tracking for Relay Satellites in a Perturbed
Areostationary Orbit,”Acta Astronautica, Vol. 136, 2017, pp.
434–442.10.1016/j.actaastro.2017.04.002.
- Matthieu and Yuying [2025]Matthieu, F., and Yuying, L., “Areostationary Mars Orbit: Dynamics,
Control, and Applications,”IFAC-PapersOnLine, Vol. 59, No. 20, 2025,
pp. 488–493.10.1016/j.ifacol.2025.11.198.
- Soop [1994]Soop, E. M.,Handbook of Geostationary Orbits, Microcosm, Inc.,
Dordrecht, The Netherlands, 1994.
- De Bruijn et al. [2016]De Bruijn, F. J., Theil, S., Choukroun, D., and Gill, E.,
“Geostationary Satellite Station-Keeping Using Convex Optimization,”Journal of Guidance, Control, and Dynamics, Vol. 39, No. 3, 2016, pp.
605–616.10.2514/1.G001302.
- Gazzino et al. [2019]Gazzino, C., Arzelier, D., Louembet, C., Cerri, L., Pittet, C., and Losa, D.,
“Long-Term Electric-Propulsion Geostationary Station-Keeping via
Integer Programming,”Journal of Guidance, Control, and Dynamics,
Vol. 42, No. 5, 2019, pp. 976–991.10.2514/1.G003644.
- Caverly et al. [2020]Caverly, R. J., Di Cairano, S., and Weiss, A., “Electric Satellite
Station Keeping, Attitude Control, and Momentum Management by MPC,”IEEE Transactions on Control Systems Technology, Vol. 29, No. 4, 2020,
pp. 1475–1489.10.1109/TCST.2020.3014601.
- De Vittori et al. [2025]De Vittori, A., Pavanello, Z., Di Lizia, P., McMahon, J., and Armellin, R.,
“Combined Long-Term Collision Avoidance and Stochastic
Station-Keeping in Geostationary Earth Orbit,”Journal of Guidance,
Control, and Dynamics, Vol. 48, No. 4, 2025, pp. 840–854.10.2514/1.G008629.
- Silva and Romero [2013]Silva, J. J., and Romero, P., “Optimal Longitudes Determination for the
Station Keeping of Areostationary Satellites,”Planetary and Space
Science, Vol. 87, 2013, pp. 14–18.10.1016/j.pss.2012.11.013.
- Romero et al. [2015]Romero, P., Barderas, G., and García-Roldán, J. M.,
“Station-Keeping Maneuvers to Control the Inclination Evolution of
Areostationary Satellites,”Journal of Guidance, Control, and
Dynamics, Vol. 38, No. 11, 2015, pp. 2223–2227.10.2514/1.G001162.
- Eren et al. [2017]Eren, U., Prach, A., Koçer, B. B., Raković, S. V., Kayacan, E., and
Açıkmeşe, B., “Model Predictive Control in Aerospace
Systems: Current State and Opportunities,”Journal of Guidance,
Control, and Dynamics, Vol. 40, No. 7, 2017, pp. 1541–1566.10.2514/1.G002507.
- Di Cairano and Kolmanovsky [2018]Di Cairano, S., and Kolmanovsky, I. V., “Real-Time Optimization and
Model Predictive Control for Aerospace and Automotive Applications,”American Control Conference, 2018, pp. 2392–2409.10.23919/ACC.2018.8431585.
- Petersen et al. [2023]Petersen, C., Caverly, R. J., Phillips, S., and Weiss, A., “Safe and
Constrained Rendezvous, Proximity Operations, and Docking,”American
Control Conference, 2023, pp. 3645–3661.10.23919/ACC55779.2023.10155826.
- Halverson et al. [2021]Halverson, R., Weiss, A., and Caverly, R., “Station Keeping of
Satellites in Areostationary Mars Orbit Using Model Predictive Control,”AAS/AIAA Space Flight Mechanics Meeting, 2021.AAS 593-602.
- Halverson et al. [2023]Halverson, R. D., Weiss, A., and Caverly, R., “A Comparison of Linear
Quadratic and Nonlinear Model Predictive Control Applied to Station Keeping
of Satellites in Areostationary Mars Orbits,”AIAA SciTech Forum,
2023.10.2514/6.2023-2000, AIAA 2023-2000.
- Gall et al. [2024]Gall, N., Halverson, R., and Caverly, R., “Station Keeping of
Areostationary Mars Orbit Satellites Using Linear Time-Varying Model
Predictive Control,”AAS/AIAA Astrodynamics Specialist Conference,
2024.AAS 24-356.
- Halverson et al. [2025]Halverson, R. D., Weiss, A., Lundin, G., and Caverly, R. J.,
“Autonomous Station Keeping of Satellites in Areostationary Mars
Orbit: A Predictive Control Approach,”Acta Astronautica, Vol. 230,
2025, pp. 1–15.10.1016/j.actaastro.2025.01.064.
- Alfriend et al. [2010]Alfriend, K. T., Vadali, S. R., Gurfil, P., How, J. P., and Breger, L. S.,Spacecraft Formation Flying: Dynamics, Control, and Navigation,
1sted., Elsevier, Oxford, UK, 2010.
- Chao and Hoots [2018]Chao, C.-C. G., and Hoots, F.,Applied Orbit Perturbation and
Maintenance, 2nded., Aerospace Press, American Institute
of Aeronautics & Astronautics, Reston, VA, 2018.
- Lemoine et al. [2001]Lemoine, F. G., Smith, D. E., Rowlands, D. D., Zuber, M. T., Neumann, G. A.,
Chinn, D. S., and Pavlis, D. E., “An Improved Solution of the Gravity
Field of Mars (GMM-2B) From Mars Global Surveyor,”Journal of
Geophysical Research: Planets, Vol. 106, No. E10, 2001, pp. 23359–23376.10.1029/2000JE001426.
- Alvarellos [2009]Alvarellos, J. L., “Technical Note: Perturbations on a Stationary
Satellite by the Longitude-Dependent terms in Mars’ Gravitational Field,”The Journal of the Astronautical Sciences, Vol. 57, No. 4, 2009, pp.
701–715.10.1007/BF03321524.
- Malyuta et al. [2019]Malyuta, D., Reynolds, T., Szmuk, M., Mesbahi, M., Acikmese, B., and Carson,
J. M., “Discretization Performance and Accuracy Analysis for the
Rocket Powered Descent Guidance Problem,”AIAA SciTech Forum, 2019.10.2514/6.2019-0925, AIAA 2019-0925.
- Martins et al. [2003]Martins, J. R., Sturdza, P., and Alonso, J. J., “The Complex-Step
Derivative Approximation,”ACM Transactions on Mathematical Software,
Vol. 29, No. 3, 2003, pp. 245–262.10.1145/838250.838251.
- Cao [2025]Cao, Y., “Complex Step Jacobian,” , 2025.URLhttps://www.mathworks.com/matlabcentral/fileexchange/18176-complex-step-jacobian,
MATLAB Central File Exchange, Retrieved February 26, 2025.
- Ricciardi [2025]Ricciardi, A., “Complex-step-compatible atan2(),” , 2025.URLhttps://www.mathworks.com/matlabcentral/fileexchange/101193-complex-step-compatible-atan2,
MATLAB Central File Exchange, Retrieved February 26, 2025.

## 


- 


Major funding support from
