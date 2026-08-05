# First Observation of Dispersive Shock Waves in an Electron Beam

**arXiv ID**: 2510.19786v1
**Authors**: H. McCright, I. G. Abel, I. Haber, P. G. O'Shea, B. L. Beaudoin
**Published**: 2025-10-22
**Categories**: physics.acc-ph, nlin.PS, physics.plasm-ph
**HTML URL**: https://arxiv.org/html/2510.19786v1

## Abstract

Dispersive shock waves (DSWs) are expanding nonlinear wave trains that arise when dispersion regularizes a steepening front, a phenomenon observed in fluids, plasmas, optics, and superfluids. Here we report the first experimental observation of DSWs in an intense electron beam, using the University of Maryland Electron Ring (UMER). A localized induction-cell perturbation produced a negative density pulse that evolved into a leading soliton-like peak followed by an expanding train of oscillations. The leading peak satisfied soliton scaling laws for width^2 vs inverse amplitude and velocity vs amplitude, while the total wave-train width increased linearly with time, consistent with Korteweg--de Vries (KdV) predictions. Successive peaks showed decreasing amplitude and velocity toward the trailing edge, in agreement with dispersive shock ordering. These results demonstrate that intense charged particle beams provide a new laboratory platform for studying dispersive hydrodynamics, extending nonlinear wave physics into the high-intensity beam regime.

## Full Text

First Observation of Dispersive Shock Waves in an Electron Beam

## First Observation of Dispersive Shock Waves in an Electron BeamH. McCrightDepartment of Physics, University of Maryland, College Park, USI.G. AbelInstitute for Research in Electronics and Applied Physics, University of Maryland, College Park, USI. HaberInstitute for Research in Electronics and Applied Physics, University of Maryland, College Park, USP.G. O’SheaDepartment of Electrical and Computer Engineering, University of Maryland, College Park, USB.L. BeaudoinInstitute for Research in Electronics and Applied Physics, University of Maryland, College Park, US(October 22, 2025)

## Abstract

Dispersive shock waves (DSWs) are expanding nonlinear wave trains that arise when dispersion regularizes a steepening front, a phenomenon observed in fluids, plasmas, optics, and superfluids. Here we report the first experimental observation of DSWs in an intense electron beam, using the University of Maryland Electron Ring (UMER). A localized induction-cell perturbation produced a negative density pulse that evolved into a leading soliton-like peak followed by an expanding train of oscillations. The leading peak satisfied soliton scaling laws for(w​i​d​t​h)2(width)^{2}vs inverse amplitude and velocity vs amplitude, while the total wave-train width increased linearly with time, consistent with Korteweg–de Vries (KdV) predictions. Successive peaks showed decreasing amplitude and velocity toward the trailing edge, in agreement with dispersive shock ordering. These results demonstrate that intense charged particle beams provide a new laboratory platform for studying dispersive hydrodynamics, extending nonlinear wave physics into the high-intensity beam regime.

Dispersive shock waves (DSWs) are expanding nonlinear wave trains that regularize a steep front through the balance of dispersion and nonlinearity[1]. They appear widely in nature, from tidal bores to atmospheric “morning glory” waves[2], and have been reproduced in laboratory systems including plasmas[3,4,5,6], nonlinear optics[7,8,9,2], classical fluids[10,11], and superfluids[12,13]. Across these different media, their defining signature is consistent: a sharp leading edge followed by an oscillatory wake.

Charged particle beams provide a new platform for nonlinear dispersive dynamics. In particular, space-charge–dominated (“intense”) beams, where collective forces outweigh emittance in the transverse envelope equation[14], support collective behaviors analogous to fluids[15]. Previous work at the University of Maryland Electron Ring (UMER) demonstrated Korteweg–de Vries (KdV) solitons, which are localized, self-reinforcing waves that maintain their shape through a balance of nonlinearity and dispersion, launched by localized peaks in beam current[16,17].

Here, we report the first observation of DSWs in an intense electron beam. Unlike solitons, which remain localized, DSWs form from a steep disturbance and expand into a train of oscillations that collectively smooth the front. In UMER, these DSWs are triggered by a dip in beam current and evolve into a high-frequency train of oscillations, representing a qualitatively distinct nonlinear mechanism. Long propagation distances and highly reproducible beam conditions enable controlled studies of DSW formation with long-time evolution. By generating both peak-driven solitons and dip-driven DSWs in a reproducible setting, these experiments provide a platform for investigating nonlinear wave interactions in beams, as recent theory has highlighted the rich dynamics of DSW collisions[18]. Because beams in high-energy accelerators also start in the space-charge–dominated regime, the dynamics reported here are not confined to low-energy models: they are a general feature of intense beam physics, with implications for accelerator design and astrophysical plasmas[19,20].

The dynamics of small-amplitude density perturbations in a dispersive, nonlinear medium are captured by the KdV equation[21]:∂u∂t+α​u​∂u∂z+β​∂3u∂z3=0,\frac{\partial u}{\partial t}+\alpha u\frac{\partial u}{\partial z}+\beta\frac{\partial^{3}u}{\partial z^{3}}=0,(1)

whereu​(z,t)u(z,t)is the density perturbation,α\alphais the nonlinear coefficient, andβ\betagoverns dispersion. Historically, the KdV equation admits solitary and cnoidal wave solutions. Gurevich and Pitaevskii[22]solved the nonstationary KdV Riemann problem, showing that a step-like initial perturbation evolves into a modulated wave train. Numerical studies[23]confirmed that the fastest, largest-amplitude peak leads the train, a key feature of a DSW.

For positive pulses, the nonlinear steepening is balanced by dispersion, producing solitons; this is the regime of previously observed solitons in UMER[16,17]. For negative perturbations, however, the steepening leads to a gradient catastrophe followed by dispersion-dominated regularization, resulting in an expanding oscillatory front rather than a solitary peak (Fig.1).Figure 1:Numerical KdV solution for a negative initial perturbation on a periodic domainx∈[−π,π]x\in[-\pi,\pi], computed using a pseudo-spectral spatial method and a fourth-order Runge–Kutta time stepper. Profiles are shown in100​μ​s100\ \mu\text{s}increments, increasing upward in time.

Physically, faster characteristics from larger-amplitude regions overtake slower ones, steepening the front until dispersion regularizes it into an oscillatory train[22,23]. A pseudopotential analysis[24]confirms that negative perturbations do not support localized solitons but allow oscillatory trajectories, producing peaks whose amplitude and velocity decrease toward the trailing edge.

To identify a DSW experimentally, we therefore test for the following:
- 1.

Soliton-like leading peak: The first peak should follow the linear scaling laws for solitons measured previously in UMER (velocity vs amplitude) and(w​i​d​t​h)2(width)^{2}vs1/amplitude1/\text{amplitude}.[17]
- 2.

Two distinct edge velocities: The leading and trailing edges of the DSW propagate with different speedss+s_{+}ands−s_{-}, predicted for KdV DSWs with steep initial conditions ass−=−Δ+u+,s+=23​Δ+u+,s_{-}=-\Delta+u_{+},\quad s_{+}=\frac{2}{3}\Delta+u_{+},(2)

whereΔ=u+−u−\Delta=u_{+}-u_{-}is the initial amplitude difference across the shock. The DSW therefore expands at a constant rateW​(t)=(s+−s−)​t=53​Δ​t,W(t)=(s_{+}-s_{-})t=\frac{5}{3}\Delta\,t,(3)

implying a linear growth of the DSW width with slope proportional to the initial amplitude difference across the shock[22,25].

We studied DSW formation using the 10-keV electron beam in the 11.52m circumference UMER storage ring, both experimentally and via simulations in the WARP particle-in-cell code[26]. In WARP, the beam was initialized with uniform density and transverse velocity, with a spread much smaller than the beam speed (Δ​v≪β​c\Delta v\ll\beta c,β≈vbeam/c\beta\approx v_{\mathrm{beam}}/c), using 16 million macroparticles—computational particles each representing many electrons—along with a 1 ns time step, 64 radial cells, and 2048 axial cells. The domain spanned 0.0254 m radially (conducting) and 11.52 m axially (periodic), with parameters verified for convergence and prior experimental validation[17].

In WARP, a localized, one-time longitudinal electric field introduced a narrow Gaussian velocity perturbation (10ns travel time). After a single pass, the perturbation was removed, producing two opposite-polarity current peaks that split into slow and fast waves[27,28], eventually forming dispersive shock structures (Figure 2). The simulation illustrates the qualitative evolution of a leading wave followed by smaller oscillations.Figure 2:Simulated beam current evolution using WARP for turns 5–14, stacked with 0.0075 A upward offsets. Early turns are omitted while the beam relaxes in phase space; the DSW forms once the initial negative density perturbation steepens.

Experimentally, a single 100ns rectangular bunch was injected, with current measured per turn using a wall current monitor 7.67m downstream. A controlled velocity modulation was applied via an inline induction cell, producing a negative density perturbation consistent with the simulation[29].

Figure 3shows the measured evolution of the current perturbation over successive turns 5–16. The data are background-subtracted using the beam when perturbations are not intentionally introduced to highlight the oscillatory behavior. No Fourier cutoff or other frequency filtering was applied, in order to preserve the full range of oscillations and avoid inadvertently removing or distorting features of the DSW. A fully developed DSW pattern emerges after∼10\sim 10revolutions, with a high-amplitude, fast-moving leading peak followed by a trailing oscillatory train.Figure 3:Measured current perturbation (A, background-subtracted) vs time (s) at successive revolutions in UMER, showing the formation of a dispersive shock wave from an initial negative density perturbation. The initial beam current was approximately 30 mA. Turn number increases from bottom to top. The width of the DSW at each turn was measured between the red dots, with the blue dotted lines fitted to these points to illustrate the linear expansion of the DSW.

We restricted the quantitative analysis to turns 10–16. At earlier turns, the perturbation is still evolving toward a steady DSW structure; the leading peak and subsequent oscillations are not yet well separated. At later turns, beam loss and phase-space dilution reduce signal-to-noise, systematically biasing amplitude and velocity measurements, particularly for the trailing peaks.Figure 4:Three-panel figure illustrating key features of the dispersive shock wave data:
a) Squared width of the leading peak vs inverse amplitude, showing linear scaling consistent with soliton behavior. Reducedχ2\chi^{2}= 0.51.
b) Velocity of the leading peak vs amplitude, showing linear scaling consistent with soliton behavior. Reducedχ2\chi^{2}= 1.16.
c) DSW width versus turn number, showing linear expansion. Width as measured between blue lines inFigure 3. Width of DSW expands linearly, as predicted with a reducedχ2\chi^{2}of 0.297.

The leading peak obeyed the soliton scaling laws established in prior measurements:
(i) velocity vs amplitude (Figure 4a) and
(ii)(w​i​d​t​h)2(width)^{2}vs1/amplitude1/\text{amplitude}(Figure 4b). The soliton width was defined as the full width at half maximum (FWHM) of the leading density peak.
In both cases, a linear fit produced reducedχ2\chi^{2}values of 0.51 and 1.16, respectively, suggesting that the data is well described by the linear models.

The separation between the leading and trailing edges increased linearly with turn number, as shown inFigure 4c, consistent with the KdV predictionW​(t)∝(u−−u+)​tW(t)~\propto~(u_{-}~-u_{+})t. Both linear fits yield reduced chi-squared values near unity, indicating excellent agreement with a linear model. For the data shown inFigure 3, the inferred expansion rate of the DSW width wasd​W/dt=(6.02±0.31)×10−3​s/s\mathrm{d}W/\mathrm{dt}=(6.02\pm 0.31)\times 10^{-3}~\mathrm{s/s}.

To probe the amplitude dependence ofWW, separate experiments were carried out with a smaller initial perturbation, implemented by reducing the magnitude of the applied velocity modulation from 30 mA to 20 mA. In these experiments, the inferred spreading rate wasd​W/dt=(4.04±0.33)×10−3​s/s\mathrm{d}W/\mathrm{dt}=(4.04\pm 0.33)\times 10^{-3}~\mathrm{s/s},
and the initial amplitude ratio was roughly 0.75. This is consistent with the linear scaling predicted[22,25].

Successive peaks exhibit decreasing amplitude and velocity toward the trailing edge, consistent with the expected ordering in a DSW. This is reflected inFigure 4c by the smaller slope in the DSW width between the first and second peaks compared to the slope between the first and third peaks.

We report the first observation of DSWs in a space-charge–dominated electron beam. Controlled negative density perturbations in UMER generated expanding nonlinear wave trains whose leading peak follows soliton-like scaling laws, while the total wave-train width grows linearly with time, in agreement with KdV theory. These results extend prior soliton studies into a distinct nonlinear regime, demonstrating that DSW dynamics are accessible in intense charged particle beams.

UMER’s storage-ring geometry and reproducible beam conditions enable detailed tracking of DSW formation. Beyond fundamental interest, these findings open the door to studies of soliton–DSW interactions, modulational instabilities, and combined excitations. Because high-energy accelerators also begin in a space-charge–dominated regime, the observed dynamics are scalable, establishing intense electron beams as a versatile platform for nonlinear dispersive physics with potential relevance to accelerator science, beam-driven radiation sources, and astrophysical plasma analogues.

## Acknowledgements.Thanks to Carter Hall for the opportunity to pursue this project as part of H. McCright’s Physics Undergraduate Honors Thesis at the University of Maryland, College Park, and Joseph Zennamo at Fermilab for guidance, mentorship, and feedback on drafts. Special thanks to Rollo the cat, a steadfast source of support throughout the project. This work was supported by DOE Grant No.DE-SC0022009.

## References
- Maidenet al.[2016]M. D. Maiden, N. K. Lowman, D. V. Anderson, M. E. Schubert, and M. A. Hoefer, Phys. Rev. Lett.116, 174501 (2016).
- Fatomeet al.[2014]J. Fatome, C. Finot, G. Millot, A. Armaroli, and S. Trillo,Phys. Rev. X4, 021022 (2014).
- Tayloret al.[1970]R. J. Taylor, D. R. Baker, and H. Ikezi, Phys. Rev. Lett.24, 206 (1970).
- Niemannet al.[2014]C. Niemannet al., Geophys. Res. Lett.41, 7413 (2014).
- DeSilvaet al.[1971]A. W. DeSilva, W. F. Dove, I. J. Spalding, and G. C. Goldenbaum, Phys. Fluids14, 42 (1971).
- Craig [1974]A. D. Craig, J. Plasma Phys.12, 149 (1974).
- Wanet al.[2007]W. Wan, S. Jia, and J. W. Fleischer, Nat. Phys.3, 46 (2007).
- Jiaet al.[2007]S. Jia, W. Wan, and J. W. Fleischer, Phys. Rev. Lett.99, 223901 (2007).
- Ghofranihaet al.[2007]N. Ghofraniha, C. Conti, G. Ruocco, and S. Trillo, Phys. Rev. Lett.99, 043903 (2007).
- Smyth and Holloway [1988]N. F. Smyth and P. E. Holloway, J. Phys. Oceanogr.18, 947 (1988).
- Lighthill [1978]J. Lighthill,Waves in Fluids(Cambridge University Press, Cambridge, UK, 1978).
- Duttonet al.[2001]Z. Dutton, M. Budde, C. Slowe, and L. V. Hau, Science293, 663 (2001).
- Changet al.[2008]J. J. Chang, P. Engels, and M. A. Hoefer, Phys. Rev. Lett.101, 170404 (2008).
- Reiser [1994]M. Reiser,Theory and Design of Charged Particle Beams(Wiley, New York, 1994).
- Bisognanoet al.[1981]J. Bisognano, I. Haber, L. Smith, and A. Sternlieb, IEEE Trans. Nucl. Sci.28, 2513 (1981).
- Thangaraj [2009]J. C. T. Thangaraj,Study of Longitudinal Space Charge Waves in Space-Charge Dominated Beams, Ph.D. thesis, University of Maryland, College Park (2009).
- Moet al.[2013]Y. C. Mo, R. A. Kishek, D. Feldman, I. Haber, B. Beaudoin, P. G. O’Shea, and J. C. T. Thangaraj,Phys. Rev. Lett.110, 084802 (2013).
- Biondiniet al.[2025]G. Biondini, A. Bivolcic, and M. A. Hoefer, Phys. Rev. Lett.135, 067201 (2025).
- El-Tantawy [2016]S. A. El-Tantawy, Astrophys. Space Sci.361, 164 (2016).
- Shanet al.[2024]S. A. Shan, S. Arooj, and H. Saleem, Phys. Plasmas31, 122106 (2024).
- Korteweg and de Vries [1895]D. J. Korteweg and G. de Vries,Philos. Mag.39, 422 (1895).
- Gurevich and Pitaevskii [1974]A. V. Gurevich and L. P. Pitaevskii, Sov. Phys. JETP33, 291 (1974), zh. Eksp. Teor. Fiz. 60, 215 (1971).
- Fornberg and Whitham [1978]B. Fornberg and G. B. Whitham, Philos. Trans. R. Soc. A289, 373 (1978).
- Lyu [2005]C. Lyu,Nonlinear Space Plasma Physics: Solitons and Coherent Structures in Collisionless Plasmas, Ph.D. thesis, University of Maryland, College Park (2005), chapter 3: The KdV Equation and Pseudopotential Approach.
- El and Hoefer [2016]G. A. El and M. A. Hoefer, Physica D333, 11 (2016).
- Groteet al.[1996]D. P. Grote, A. Friedman, I. Haber, and S. Yu, Fusion Eng. Des.32-33, 193 (1996), proceedings of the Seventh International Symposium on Heavy Ion Inertial Fusion.
- Wanget al.[1993]J. G. Wang, D. X. Wang, and M. Reiser, Phys. Rev. Lett.71, 1836 (1993).
- Tianet al.[2010]K. Tian, R. A. Kishek, I. Haber, M. Reiser, and P. G. O’Shea, Phys. Rev. ST Accel. Beams13, 034201 (2010).
- Beaudoin [2008]B. Beaudoin,Longitudinal Space-Charge Waves Induced by Energy Modulations, Master’s thesis, University of Maryland, College Park (2008).
