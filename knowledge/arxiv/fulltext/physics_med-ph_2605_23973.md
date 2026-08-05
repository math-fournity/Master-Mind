# A digital twin for microwave liver treatment replanning

**arXiv ID**: 2605.23973v1
**Authors**: Ilias Nahmed, Francesco Dettori, Juan Verde, Michel Duprez, Pablo Alvarez, Stéphane Cotin
**Published**: 2026-05-13
**Categories**: physics.med-ph, math.NA
**DOI**: 10.1007/s11548-026-03641-z
**HTML URL**: https://arxiv.org/html/2605.23973v1

## Abstract

Purpose: MicroWave Ablation (MWA) modeling and simulation bear great potential for loco-regional treatment of liver tumors. However, accurately positioning the antenna according to a planned orientation/location is technically challenging. In cases of misplacement, maintaining the original plan may cause incomplete ablation, while repositioning the antenna may induce tumor seeding. In this work, we propose (i) a digital twin of MWA that simulates ablation outcomes, and (ii) an optimizer that suggests corrections to MWA parameters without antenna reinsertion, while ensuring complete tumor ablations. Methods: A finite element scheme was used to solve the coupled microwave propagation and heat transfer equations governing MWA, with personalized dielectric and thermal properties determined from preoperative CT and MRI images. We then proposed an optimization algorithm able to adjust power input, ablation duration, and antenna position to correct for antenna misplacement. Results: The simulator and optimizer were evaluated against in vivo swine experimental data. Three ablations were performed in liver regions with varying vascularization. The simulations accurately predicted the ablation zones despite the presence of large vessels near the antenna, achieving Dice scores of 0.82, 0.81, and 0.79. In the case of replanning scenarios, our optimizer predicted new parameter sets that led to Dice scores of 0.83, 0.83, 0.80, a corresponding improvement of 20.3%, 40.7% and 48.1% in average over the initial ablation result. Conclusion: This paper is the first to address intra-operative replanning of thermal ablation therapy. It demonstrates that optimal ablation results can be achieved without requiring antenna reinsertion by optimizing specific ablation parameters.

## Full Text

A Digital Twin for Microwave Liver Treatment Re-planning

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
- License: CC BY 4.0arXiv:2605.23973v1 [physics.med-ph] 13 May 2026

## A Digital Twin for Microwave Liver Treatment Re-planningIlias Nahmed111corresponding author : ilias.nahmed@inria.frUniversité de Strasbourg, CNRS, Inria, ICube, F-67000 Strasbourg, FranceFrancesco DettoriUniversité de Strasbourg, CNRS, Inria, ICube, F-67000 Strasbourg, FranceJuan VerdeIHU Strasbourg, Strasbourg, FranceMichel DuprezUniversité de Strasbourg, CNRS, Inria, ICube, F-67000 Strasbourg, FrancePablo AlvarezUniversité de Strasbourg, CNRS, Inria, ICube, F-67000 Strasbourg, FranceStéphane CotinUniversité de Strasbourg, CNRS, Inria, ICube, F-67000 Strasbourg, France

## Abstract

Purpose:MicroWave Ablation (MWA) modeling and simulation bear great potential for loco-regional treatment of liver tumors. However, accurately positioning the antenna according to a planned orientation/location is technically challenging. In cases of misplacement, maintaining the original plan may cause incomplete ablation, while repositioning the antenna may induce tumor seeding. In this work, we propose (i) a digital twin of MWA that simulates ablation outcomes, and (ii) an optimizer that suggests corrections to MWA parameters without antenna reinsertion, while ensuring complete tumor ablations.

Methods:A finite element scheme was used to solve the coupled microwave propagation and heat transfer equations governing MWA, with personalized dielectric and thermal properties determined from preoperative CT and MRI images. We then proposed an optimization algorithm able to adjust power input, ablation duration, and antenna position to correct for antenna misplacement.

Results:The simulator and optimizer were evaluated againstin vivoswine experimental data. Three ablations were performed in liver regions with varying vascularization. The simulations accurately predicted the ablation zones despite the presence of large vessels near the antenna, achieving Dice scores of0.820.82,0.810.81, and0.790.79. In the case of replanning scenarios, our optimizer predicted new parameter sets that led to Dice scores of 0.83, 0.83, 0.80, a corresponding improvement of 20.3%, 40.7% and 48.1% in average over the initial ablation result.

Conclusion:This paper is the first to address intra-operative replanning of thermal ablation therapy. It demonstrates that optimal ablation results can be achieved without requiring antenna reinsertion by optimizing specific ablation parameters.

## 1Introduction

Liver cancer is the third leading cause of cancer-related death in the world[18]. Although surgical resection and liver transplantation are established as effective treatment options, they remain unsuitable for more than 80% of the patients[11]. For these reasons, along with reduced costs and improved repeatability, minimally invasive locoregional treatments based on thermal ablation have gained popularity in the last decades[15]. These techniques also enforce parenchyma preservation, particularly when treating small tumors.

Microwave ablation (MWA) constitutes, to date, one of the most effective thermal ablation modalities among the clinically available options[17]. MWA operates through a process known as dielectric hysteresis, where heat is generated from the friction and collision of water molecules (inside biological tissues) as they spin to align with the rapidly changing electromagnetic field propagating from the applicator antenna[15]. In comparison with other thermal ablation techniques, MWA requires shorter times to produce higher temperature profiles, generally leading to larger ablation zones that can be used to treat larger tumors safely. Moreover, MWA is less susceptible to the heat-sink effect, where ablations in proximity to blood vessels are less efficient due to temperature losses through advection[17,15].

Treatment through MWA can only be successful under appropriate preoperative planning. However, MWA planning in current clinical practice relies on geometrical models based on powerversusablation-duration charts provided by antenna manufacturers. Since these geometrical models completely disregard patient-specificity, they generally overestimate the ablation zones, leading potentially to incomplete ablations that could cause tumor recurrence[20]. With the emergence of computational models, it has become possible to simulate numerically the physical process of MWA in biological tissue. However, MWA involves various physical phenomena, including electromagnetics, heat transfer, and computation of tissue damage. Several methods, like Finite Elements (FE), Finite Differences, and Lattice Boltzmann, constitute suitable numerical frameworks for solving such multiphysics problems[1,16,3]. Yet, to achieve optimal ablation outcome prediction, it is essential to account for patient-specific tissue properties[14,8].

Once a plan has been established – via numerical simulation or otherwise – the antenna is inserted into the liver under CT guidance. However, because of breathing motion, changes in patient position, and insertion-induced deformation, it is practically impossible to position the antenna as planned[13,8]. This is particularly true when multiple antennas are required to treat larger tumors.
Thus, conforming to the preoperative plan often necessitates repositioning the antenna, possibly through reinsertion, which is both time-consuming and dangerous. Indeed, puncturing the tumor once, let alone several times, can lead to tumor seeding[10]. Fortunately, likely, an appropriate ablation zone can still be produced by fine-tuning ablation power and duration parameters, while avoiding both antenna reinsertion and excessive damage to healthy tissue. One can also consider slight displacements along the insertion axis, which is reasonably safer than antenna reinsertion and repositioning. As these adjustments are typically determined empirically, a re-planning tool able to quantitatively compute them could offer substantial clinical advantages.

In this paper, we present a patient-specific simulation of MWA that can be used to simulate and optimize the therapy. Sec.2.1presents the computational model, while Sec.2.2and2.3show its parametrization. The presented model is validated in Sec.2.4. In Sec.3.1we address the (re)planning solution, and present our results in Sec.3.2.

## 2Microwave ablation simulation

In this section, we describe how heat, generated by the MWA antenna, diffuses across soft tissues. Then, we explain how the model’s parameters can be tuned to characterize both the antenna and the organ, making our solution patient-specific.

## 2.1Computational model

The Pennes Bioheat equation is the most widely used model for simulating heat transfer within tissues following thermal ablation[16]. The governing equation of this model is given by:ρ​C​∂T∂t=∇⋅(κ​∇T)−ρb​Cb​ωb​(T−Tb)+Qm+Qe​x​t,\rho C\frac{\partial T}{\partial t}\ =\ \nabla\cdot(\kappa\nabla T)\ -\ \rho_{b}C_{b}\omega_{b}(T-T_{b})+Q_{m}+Q_{ext},(1)

whereρ\rho,CC,κ\kappaandTTare the tissue density (kg/m3), specific heat capacity (J/kg/K), thermal conductivity (W/m/K) and temperature (K) of the tissue, respectively;ρb\rho_{b},CbC_{b}andTbT_{b}correspond to the same physical quantities for the blood entering the tissue,ωb\omega_{b}is the blood perfusion rate (1/s) that allows modeling the heat sink effect[16],QmQ_{m}is the metabolic heat source andQe​x​tQ_{ext}is the external heat source.

A critical factor in MWA modeling is the temperature dependency of tissue parameters. Indeed, the thermal effects of MWA induce essential changes in tissue (e.g.water evaporation, coagulation, cellular denaturation), which alter both the microwave energy deposition and heat transfer phenomena. Following previous works, this work accounted for tissue coagulation in blood perfusionωb\omega_{b}[7,21], a thermal conductivityκ\kappalinearly increasing with temperature[5], as well as a water-content dependency for the heat capacityCC[4].

In[7,21], perfusion shutdown is modeled by a non-differentiable temperature threshold, which leads to difficulties in numerical solvers. To preserve the same physical behavior while ensuring differentiability, we replace the sharp switch by a smooth approximationωbsharp​(T)\displaystyle\omega_{b}^{\text{sharp}}(T)={ω0,T<60∘​C,0,T≥60∘​C,ωbsmooth​(T)=ω0​(12​tanh⁡(60−T)+12),\displaystyle=\qquad\omega_{b}^{\text{smooth}}(T)=\omega_{0}\left(\tfrac{1}{2}\tanh(60-T)+\tfrac{1}{2}\right),(2)

whereω0\omega_{0}denotes the blood perfusion at37∘​C37^{\circ}\mathrm{C}

The metabolic heat sourceQmQ_{m}is usually neglected in thermal ablation modeling, since it is tiny in comparison to the external heat sourceQe​x​tQ_{ext}. The latter models heating as microwaves propagate through tissue, and is defined in relation to the specific absorption rate (SAR) byQe​x​t=ρ⋅SAR=12​σ​⟨E→,E→∗⟩,Q_{ext}=\rho\cdot\mathrm{SAR}=\frac{1}{2}\sigma\langle\vec{E},\vec{E}^{*}\rangle,(3)

withE→\vec{E}the solution to the microwave propagation problem described by the frequency-domain Maxwell equation:∇×μr−1​(∇×E→)−k02​(εr−j​σω​ε0)​E→=0,\nabla\times\mu_{r}^{-1}(\nabla\times\vec{E})-k_{0}^{2}(\varepsilon_{r}-j\frac{\sigma}{\omega\varepsilon_{0}})\vec{E}=0,(4)

whereσ\sigmais the electric conductivity (S/m),μr\mu_{r}is the relative permeability,εr\varepsilon_{r}is the relative permittivity,ω=2​π​f\omega=2\pi fis the angular frequency (rad/s) forf=2450​MHzf=2450~\text{MHz},ε0=8.854×10−12​F/m\varepsilon_{0}=8.854\times 10^{-12}~\text{F/m}is the permittivity in vacuum andk0=51.35​m−1k_{0}=51.35~\text{m}^{-1}is the propagation constant in vacuum, respectively.

Similar to the thermal properties in Eq. (1), dielectric properties also vary with temperature[16]. Previous works have either neglected this dependency[14], or solved the coupled system of equations using time-discretization schemes of varying degrees of complexity and stability[3,4]. Arguably, the most critical consequence of this temperature dependency is the decay of the external heat sourceQe​x​tQ_{ext}with increasing temperature. Therefore, in the interest of saving computational time while maintaining the temperature dependency, the effective external heat source is approximated by:Qe​x​t​(T)=(1−11+exp⁡(6.583−0.0598⋅T))​σ2​⟨E→,E→∗⟩,Q_{ext}(T)=\left(1-\frac{1}{1+\exp(6.583-0.0598\cdot T)}\right)\frac{\sigma}{2}\langle\vec{E},\vec{E}^{*}\rangle,(5)

where the exponentially decaying factor is adopted from the temperature-dependent electric conductivity model in[3].

In Eq. (4), the power input from the generator is modeled by a port excitation boundary condition at the entry point of the antenna’s coaxial waveguide, the conducting materials of the antenna are idealized and modeled by Perfect Electrical Conductor boundary conditions at their surfaces, and a first-order scattering boundary condition is applied at the remaining outer domain boundaries to avoid reflection of electromagnetic waves. As for Eq. (1), all boundaries were considered thermally insulated, except for the antenna/tissue interface, where a convection boundary condition was applied to model the antenna’s cooling technology[4]. The validity of the first-order scattering boundary condition was verified by a domain-size convergence study of the electromagnetic problem, showing that boundary reflections become negligible near the ablation zone for sufficiently large domains. In particular, beyond a transverse domain width of 20 mm, the relative electric fieldL2L^{2}error remained below 0.5%, indicating that residual boundary artifacts do not affect the predicted ablation shape.

A finite element numerical scheme was implemented using the open source library FEniCSx222https://fenicsproject.org/to solve the coupled microwave propagation and heat transfer equations governing MWA. Axial symmetry was assumed for the microwave propagation problem, since low variability of the electric field solution to variations in dielectric properties has been reported in previous work[5]. Thanks to the temperature-dependent external heat sourceQe​x​tQ_{ext}introduced in Eq. (5), the microwave propagation and heat transfer problems are only weakly coupled, and a single resolution of the linear system in Eq. (4) is required.
The validity of this approximation was quantitatively verified by comparison with a strongly coupled formulation, in which the Maxwell equation is re-solved with updated dielectric properties at each thermal iteration. The resulting differences in temperature and ablation zones were found to be negligible across a wide range of blood perfusion values, with a maximal temperature RMSE below0.83∘​C0.83^{\circ}\text{C}and a maximal Arrhenius factor RMSE below1.6×10−21.6\times 10^{-2}units. In addition, comparisons between heterogeneous and homogeneous electromagnetic models, as well as between 3D and interpolated 2D electromagnetic solutions, showed that tissue heterogeneity and dimensional reduction introduce only minor errors in the temperature and damage, achieving RMSE values as small as1,07∘​C1,07^{\circ}\text{C}for the temperature, and6.6×10−26.6\times 10^{-2}units for the damage. These results justify the proposed weakly coupled, axisymmetric electromagnetic modeling, which captures the dominant heating mechanisms while significantly reducing computational cost.
An implicit time-discretization scheme was implemented to solve the nonlinear system in Eq. (1), requiring a Newton resolution per time increment (d​t=10​sdt=10\mathrm{s}).

## 2.2Antenna characterization

The geometry of the antenna strongly influences the pattern of the generated electromagnetic field, and thus the specific absorption rate, which dictates the resulting extent and shape of the ablation zone. The precise design of MWA antennas is, unfortunately, generally unknown, besides their external geometry. It is therefore essential to estimate the antenna characteristics as accurately as possible.

Since MWA antennas are designed to optimize theS11S_{11}reflection coefficient (which measures the efficiency of energy delivery), the unknown antenna geometry parameters were estimated through a constrained optimization problem. The objective was to minimize the
the reflection coefficientS11S_{11}, by varying the antenna geometry while accounting for estimates of some of its characteristics: quarter wavelength choke, 50 Ohm impedance inner/outer conductor radii, total radius. The specifics of this optimization process are out of the scope of this paper, but interested readers are referred to[6]for further details.

## 2.3Patient-specific parametrization

This work relies on a patient-specific, multi-compartment anatomical model built from preoperative medical images.
Experimental data were acquired to personalize and validate our MWA simulations. All preclinical data were obtained fromin vivoexperiments on swine models following a protocol closely aligned with the standard of care. A pre-treatment contrast-enhanced CT (CE-CT) scan was performed to identify the target ablation location and extract the swine anatomy for material property assignment.

For the microwave propagation problem, all the patient-agnostic parameters related to the antenna materials and liver tissue were obtained from publicly available databases[2].
For the heat transfer problem, the thermal properties of each tissue type were derived from the literature[19,5,2]and assigned to the corresponding anatomical compartments, as reported in Table1.
Particular attention was given to the blood perfusion parameterω0\omega_{0}, since it greatly influences the solution of the Pennes Bioheat equation. Although a constant value is typically used for the vessels, a wide range of values for the healthy liver tissue can be found in the literature[5,1,2,8], from0.015​s−10.015\text{s}^{-1}to0.071​s−10.071\text{s}^{-1}. This variability can lead to ablation volume differences as large as1818cm3.
To address this issue, a calibration of the parameterω0\omega_{0}was performed on a baseline ablation far from the large vessels using the same objective function as the one later employed in the optimization problem described in Sec.3.
A post-treatment multiphase CE-CT scan was then collected to assess this baseline ablation. The antenna was left in place during imaging, ensuring its visibility in the post-ablation scan.
This patient-specific estimated value ofω0\omega_{0}was then used in all following simulations.Table 1:Multi-compartment material properties for thermal transfer problemTissue typeκ0\kappa_{0}[W/m/K]C0C_{0}[J/kg/K]ρ\rho[kg/m3]ω0\omega_{0}[1/s]Liver Tissue0.520.5235403540108010800.0790.079(fitted value)Blood vessels0.540.5437703770106010600.20.2

## 2.4Ablation simulation results

We validated our results usingin vivoswine experiments with three ablations scenarios at the IHU of Strasbourg, with the approval of the local ethics committee.
Although limited to three ablations, thesein vivoexperiments are intended as a qualitative validation of the proposed modeling framework under realistic physiological conditions, and not as a statistical or population-level study.
The three ablations (100​W100~\text{W}during55minutes) were performed in regions with different degrees of vascularization: 1) away from any big vessels to calibrate theω0\omega_{0}parameter and to constitute a baseline (labeledB); 2) near the hepatic vein(HV)and 3) near both hepatic and portal veins(HPV). This choice was made to estimate robustness to the heat sink effect. The antenna used in this study was a 15-gaugeMedtronic Covidien Emprint™antenna with water-cooling technology, delivering up to 150W at a frequency of 2.45GHz.

The solution of the bioheat equation (1) is a time-dependent temperature field, which can only be measured experimentally using MR thermometry. This imaging modality is rarely available and prone to measurement errors. As an alternative, we evaluate our results against the actual ablation region. To achieve this, we simulate the ablation using the Arrhenius thermal injury model:Ω​(t)=∫0tA​exp⁡(−Δ​ER​T​(τ))​𝑑τ,\Omega(t)=\int_{0}^{t}A\exp\Big(\frac{-\Delta E}{RT(\tau)}\Big)d\tau,(6)

whereA=7.39×1039​s−1A=7.39\times 10^{39}\text{s}^{-1}is a frequency factor,Δ​E=2.577×105​J mol−1\Delta E=2.577\times 10^{5}\text{J mol}^{-1}is the activation energy,R=8.314​J mol−1​K−1R=8.314\text{J mol}^{-1}\text{K}^{-1}is the universal gas constant andT​(τ)T(\tau)is the temperature at timeτ\tau[14]. The cell death probabilityθd\theta_{d}is then computed asθd=1−e−Ω​(t)\theta_{d}=1-e^{-\Omega(t)}where the thresholdθd>0.98\theta_{d}>0.98is used for indicating cell necrosis[14].

All experimental ablations were replicated via simulation: same antenna location, power input (100 W), and ablation duration (5 min). The predicted ablation zones, as per Eq. (6), were compared with the post-treatment CE-CT segmentations to measure their accuracy.
Fig.1presents qualitative results for the HPV ablation case, with 2D and 3D comparisons of the ground truth ablation zone, against the predicted ablation zones from our model and the manufacturer’s geometrical model.
Table2summarizes the quantitative results of our validation:Table 2:Dice similar coefficient (Dsim.\text{D}_{\text{sim.}},Dman.\text{D}_{\text{man.}}), standard Hausdorff distances (dsim.Hd^{H}_{\text{sim.}},dman.Hd^{H}_{\text{man.}}), and Hausdorff distances with95th95^{\text{th}}percentile (d95,sim.Hd^{H}_{95,\text{sim.}},d95,man.Hd^{H}_{95,\text{man.}}) for the simulated and manufacturer’s ablation zones with respect toin vivoexperimental ground truth for the ablations B (baseline far from large veins), HV (near the hepatic vein) and HPV (near the hepatic and portal vein)Dsim.\text{D}_{\text{sim.}}d95,sim.Hd^{H}_{95,\text{sim.}}dsim.Hd^{H}_{\text{sim.}}Dman.\text{D}_{\text{man.}}d95,man.Hd^{H}_{95,\text{man.}}dman.Hd^{H}_{\text{man.}}B0.821.7 mm5.9 mm0.624.7 mm8.0 mmHV0.812.8 mm8.1 mm0.664.2 mm7.3 mmHPV0.792.7 mm6.4 mm0.585.5 mm8.2 mmFigure 1:Visual and quantitative comparison of ablation segmentation models for the HPV case. (a) CT slice with outlines: ground truth (blue), our prediction (red), and manufacturer’s prediction (green). (b) 3D visualization of the ground truth ablation (blue) with surrounding vasculature (red). (c) Our model’s prediction (red) vs. ground truth (blue) (Dice = 0.79). (d) Manufacturer’s model (green) vs. ground truth (blue) (Dice = 0.58)

Our simulator outperformed the manufacturer’s prediction across all ablations. It achieved substantial Dice coefficient improvements of 32% (B ablation), 22% (HV ablation), and 36% (HPV ablation), while thed95Hd^{H}_{95}distance was reduced by 2.4mm on average.
The simulator achieved lowerdHd^{H}values than the antenna manufacturer’s model on all ablations but one (HV); however, the simulator’sd95Hd^{H}_{95}being lower on this ablation suggests that this difference is likely due to an outlier. In fact,dHd^{H}is more sensitive to isolated boundary deviations thand95Hd^{H}_{95}.

Overall, the Dice coefficients were high (around 0.8), and thed95Hd^{H}_{95}values remained very low (around 2mm), indicating clinically acceptable precision. Even with the heat sink effect present in the HV and HPV ablations, the simulator’s performance was not notably reduced: both D andd95Hd^{H}_{95}values remained within the same range as the baseline ablation. These results suggest that the simulator robustly models perfusion, and the combination of high Dice scores and lowd95Hd^{H}_{95}values supports the validity of the simulation model.

## 3Intervention replanning through optimization

In this section, we propose an intraoperative strategy to adjust specific ablation parameters — namely, power, ablation duration, and electrode translation — in the event of electrode misplacement.

## 3.1Ablation replanning method

Placing the antenna at the intended position and orientation constitutes a significant technical challenge. Indeed, the liver may have deformed significantly during antenna insertion with respect to the preoperative plan, and this is due to the antenna itself, breathing, and/or patient repositioning. Consequently, it is not unrealistic to consider that, in many cases, the antenna position and orientation deviate from their intended positions after an initial insertion.

Considering this antenna misplacement context, the strategy introduced here allows the computation of a new ablation plan, while avoiding the complete withdrawal of the antenna that would otherwise introduce risks of tumor seeding. Specifically, it determines an optimal translationt→∗\vec{t}^{*}along the antenna’s shaft, together with an updated powerP∗P^{*}and ablation durationT∗T^{*}– within realistic clinical bounds –, as to achieve a complete tumor ablation while minimizing damage to healthy tissue. The general workflow for the proposed MWA replanning strategy is illustrated in Fig.2.Figure 2:Illustration of the replanning workflow. (a) The ideal initial plan (P0P_{0},T0T_{0}) achieves full tumor coverage (b) Using the same configuration when the antenna is misplaced may cause incomplete tumor coverage (c) The proposed replanning tool suggests a translationt→∗\vec{t}^{*}of the antenna along the same axis with updated powerP∗P^{*}and durationT∗T^{*}to ensure complete ablation

For a new ablation plan to be admissible, the simulated ablation zone should match as closely as possible the originally planned target ablation zone.
In this work, this was achieved by maximizing the Dice similarity coefficient, denoted byDD, while simultaneously minimizing a modified Hausdorff distance[12], denoted byd95Hd^{H}_{95}, between the simulated and target ablation zones. More precisely, our replanning strategy finds a new set of optimal parametersP∗P^{*},T∗T^{*},t→∗\vec{t}^{*}via the following minimization problemarg⁡minP,T,t→⁡12​(1−D​(Asim​(P,T,t→),Atarget))+12​d95H​(Asim​(P,T,t→),Atarget),\operatorname*{\arg\min}_{P,T,\vec{t}}\frac{1}{2}\left(1-\text{D}\left(A_{\text{sim}}\left(P,T,\vec{t}\;\right),A_{\text{target}}\right)\right)+\frac{1}{2}d^{H}_{95}\left(A_{\text{sim}}\left(P,T,\vec{t}\;\right),A_{\text{target}}\right),(7)

whereAsim​(P,T,t→)A_{\text{sim}}(P,T,\vec{t}\,)denotes the simulated ablation zone corresponding to a given powerPP, ablation durationTT, antenna translation along its axist→\vec{t}; andAtargetA_{\text{target}}is the target ablation zone.

In addition, some clinically relevant constraints were imposed : a) the power input must remain within20​W20~\text{W}and150​W150~\text{W}; b) the ablation duration is limited to1515minutes; and c) the antenna translation along its axis is restricted to[−5,5]​cm[-5,5]~\text{cm}.
Because the optimization problem is highly non-linear and lacks sufficient regularity for gradient-based algorithms, genetic algorithm was employed[9]. The population size was set to 15, and the maximum number of iterations to 100, with an average optimization iteration of 55 seconds, the total computation time for the optimization algorithm ranged between 50 and 95 minutes. This computational cost reflects a proof-of-concept re-planning framework and is not intended to demonstrate real-time or intra-operative feasibility, which would require surrogate or reduced-order models beyond the scope of this work.

## 3.2Ablation replanning results

The most natural way of validating the proposed replanning strategy would be to re-plan an ablation after a failed attempt of antenna positioning in the tumor, as illustrated in Fig.2. However, reproducing such scenario in swine models (which generally do not have tumors) was not possible. As an alternative, we conducted experiments on a healthy pig, and considered the ground-truth ablated zones directly as the target ablation zonesAtargetA_{\text{target}}in (7). The optimizer was then evaluated by providing it with an antenna placement intentionally shifted from the true experimental position.

Under these considerations, a perfect optimization should find a new plan (power/time/translation) that (i) corrects the initial translation, and (ii) predicts an ablation zone identical to the target ablation zone. The Dice coefficient between these two ablation zones would then be a solid way to evaluate the replanning strategy. However, the optimization problem (7) is ill-posed, since several sets of parameters(P,T,t→)(P,T,\vec{t}\,)could yield the same simulated ablation zoneAsimA_{\text{sim}}. Although this issue has no significance in a real scenario where the objective is tailored towards the target ablation zoneAtargetA_{\text{target}}(any couple of parameters is admissible), it does introduce a bias in the evaluation of the proposed ablation replanning strategy. For this reason, the ablation durationTTwas fixed at 5 min during replanning, as in the experimental ablations, and only the power inputPPand translationt→\vec{t}were optimized.

The antenna positions from the three performed experimental ablations were artificially shifted by 5 mm along the antenna axis. Hence, the optimal “new” plan should correspond to the original power input (P=100P=100W) and the correct translation shift (t→=−5\vec{t}=-5mm). For each ablation, the optimization was run 50 times, each with a different random seed for the genetic algorithm in order to assess optimizer robustness. Average values and standard deviations of the Dice coefficient, Hausdorff distances, and relative errors (normalized by permissible ranges: 20:150W for power, -50:50mm for translation) in power and translation predictions are listed in Table3.Table 3:Dice similarity coefficientD, standard Hausdorff distancesdHd^{H}, and Hausdorff distances with95th95^{\text{th}}percentiled95Hd^{H}_{95}for the proposed ablation replanning strategy for the ablations B (baseline far from large veins), HV (near the hepatic vein), and HPV (near the hepatic and portal vein)Dinitial\text{D}_{\text{initial}}corresponds to Dice coefficient without replanning.Dd95Hd^{H}_{95}dHd^{H}Power relative errorTrans. relative errorDinitial\text{D}_{\text{initial}}B0.83±0.0020.83\pm 0.0021.671.67±0.1\pm 0.1mm5.25.2±0.5\pm 0.5mm2.3%2.3\%±0.0\pm 0.00.5%0.5\%±0.0\pm 0.00.69HV0.83±0.0030.83\pm 0.0031.631.63±0.1\pm 0.1mm5.75.7±0.5\pm 0.5mm2.3%2.3\%±0.0\pm 0.02.1%2.1\%±0.0\pm 0.00.59HPV0.80±0.0150.80\pm 0.0152.172.17±0.3\pm 0.3mm6.36.3±0.8\pm 0.8mm4.7%4.7\%±0.0\pm 0.01.1%1.1\%±0.0\pm 0.00.54

The optimizer recovered the target translation and power input with acceptable accuracy across all three ablations. The Dice coefficients ranged from 0.80 to 0.83, improving over the ablation predictions without replanning by 36.6% in average.

For the translation parameter, the optimizer achieved high accuracy for ablation B, with a mean relative error of 0.5%. Ablations HV and HPV exhibited slightly larger errors, with relative translation errors of 2.1% and 1.1%, respectively. Despite the increased vascular complexity in these scenarios, the variability remained negligible, suggesting stable convergence toward clinically acceptable solutions.

Power estimation showed similarly stable behavior. Relative power errors were limited to approximately 2.3% for ablations B and HV, and increased to 4.7% for HPV. The higher error observed in the HPV case is consistent with the presence of multiple large vessels in close proximity to the target, which increases the sensitivity of the thermal field to power variations. Nevertheless, the high Dice coefficients and low Hausdorff distances indicate that the optimizer successfully identifies power–translation combinations that compensate for these effects and accurately reproduce the ground-truth ablation shapes.

## 4Conclusion

In this study, we introduced a patient-specific MWA simulator that accurately predicts ablation zones fromin vivoexperiments with Dice scores ranging from0.790.79to0.820.82, and Hausdorff distances of approximately2​mm2\ \text{mm}. In comparison with the ablation geometrical predictions provided by the antenna manufacturer, our simulations demonstrated consistently higher accuracy, especially in challenging situations where the ablations are targeted in the vicinity of large vessels, such as the hepatic or portal veins.
Furthermore, a replanning optimizer that could be used intra-operatively — to the best of our knowledge, the first of its kind — was presented and validated usingin vivoablations. In most clinical settings, it is almost impossible to replicate the planned antenna position exactly. The presented optimizer introduces a potential intraoperative correction for suboptimal or failed plans, which could achieve complete tumor ablation with high accuracy. This optimizer was validated using ablations on a healthy animal and achieved high accuracy and low parameter-recovery errors.

There is one limitation to the current forward simulation approach: the calibration of theωb\omega_{b}parameter requires an ablation to be performed beforehand. While this was feasible in our swine experiments, it would not be the case in a clinical setting. Fortunately, several approaches exist that estimate theω0\omega_{0}parameter directly from CT images. Such methods would personalize blood perfusion values, but they were not investigated in this work, as they fall outside the scope of this study.

The simulator presented in this paper can already serve as an effective planning tool in simple clinical settings. Its future applications are up-and-coming, as it could serve as a basis for planning more complex interventions. For instance, completely avoiding tumor seeding through no-touch techniques is a promising perspective, which would require thorough planning to account for multiple impacts and necrosis coagulation.

Regarding the replanning tool, we identified several areas for improvement. First, the current method does not account for heterogeneous tissues, in particular, the presence of a tumor. An upcoming clinical study will bring an opportunity to develop further and validate our method. Further, the computation time could be improved through the use of GPUs or surrogate deep learning models.

## Declarations
- •

Funding: This work was funded by the MEDITWIN Bpifrance i-Demo project as part of the France 2030 program.
- •

Conflict of interest: The authors have no conflict of interest to declare.
- •

Code availability: The code and data supporting this study are not publicly available at this stage of the work.

## References
- [1]C. Audigier(2015-10)Computational modeling of radiofrequency ablation for the planning and guidance of abdominal tumor treatment.Theses,Université Nice Sophia Antipolis.External Links:LinkCited by:§1,§2.3.
- [2]C. Baumgartneret al.(2025)IT’IS Database for Thermal and Electromagnetic Parameters of Biological Tissues, Version 5.0.External Links:DocumentCited by:§2.3.
- [3]N. Bošković, M. Radmilović-Radjenović, and B. Radjenović(2023-06)Finite Element Analysis of Microwave Tumor Ablation Based on Open-Source Software Components.Mathematics11(12),pp. 2654(en).External Links:ISSN 2227-7390,Link,DocumentCited by:§1,§2.1,§2.1.
- [4]M. Cavagnaro, R. Pinto, and V. Lopresto(2015-04)Numerical models to evaluate the temperature increase induced byex vivomicrowave thermal ablation.Physics in Medicine and Biology60(8),pp. 3287–3311(en).External Links:ISSN 0031-9155, 1361-6560,Link,DocumentCited by:§2.1,§2.1,§2.1.
- [5]G. Deshazer, D. Merck, M. Hagmann, D. E. Dupuy, and P. Prakash(2016-04)Physical modeling of microwave ablation zone clinical margin variance.Medical Physics43(4),pp. 1764–1776(en).External Links:ISSN 0094-2405, 2473-4209,Link,DocumentCited by:§2.1,§2.1,§2.3.
- [6]S. Etoz and C. L. Brace(2017-12)Analysis of microwave ablation antenna optimization techniques.International Journal of RF and Microwave Computer-Aided Engineering28(3),pp. e21224.External Links:ISSN 1096-4290,DocumentCited by:§2.2.
- [7]M. Geet al.(2018-09)A multi-slot coaxial microwave antenna for liver tumor ablation.Physics in Medicine & Biology63(17) (en).External Links:ISSN 1361-6560,Link,DocumentCited by:§2.1,§2.1.
- [8]A. Heshmatet al.(2024-05)Using Patient-Specific 3D Modeling and Simulations to Optimize Microwave Ablation Therapy for Liver Cancer.Cancers16(11),pp. 2095(eng).External Links:ISSN 2072-6694,DocumentCited by:§1,§1,§2.3.
- [9]Z. Michalewicz, D. Dasgupta, R. L. Riche, and M. Schoenauer(1996)Evolutionary algorithms for constrained engineering problems.Computers & Industrial Engineering30,pp. 851–870.External Links:Link,DocumentCited by:§3.1.
- [10]P. A. Patel, L. Ingram, I. D.C. Wilson, and D. J. Breen(2013-08)No-touch Wedge Ablation Technique of Microwave Ablation for the Treatment of Subcapsular Tumors in the Liver.Journal of Vascular and Interventional Radiology24(8),pp. 1257–1262(en).External Links:ISSN 10510443,Link,DocumentCited by:§1.
- [11]L. S. Poulou(2015)Percutaneous microwave ablationvsradiofrequency ablation in the treatment of hepatocellular carcinoma.World Journal of Hepatology7(8),pp. 1054(en).External Links:ISSN 1948-5182,Link,DocumentCited by:§1.
- [12]A. Reinkeet al.(2023)Common limitations of image processing metrics: a picture story.External Links:2104.05642,DocumentCited by:§3.1.
- [13]A. Seitelet al.(2011)Computer-assisted trajectory planning for percutaneous needle insertions.Medical Physics38(6),pp. 3246–3259.External Links:DocumentCited by:§1.
- [14]F. Servinet al.(2024)Simulation of Image-Guided Microwave Ablation Therapy Using a Digital Twin Computational Model.IEEE Open Journal of Engineering in Medicine and Biology5,pp. 107–124.External Links:ISSN 2644-1276,Link,DocumentCited by:§1,§2.1,§2.4.
- [15]C. J. Simon, D. E. Dupuy, and W. W. Mayo-Smith(2005-10)Microwave Ablation: Principles and Applications.RadioGraphics25(suppl_1),pp. S69–S83(en).External Links:ISSN 0271-5333, 1527-1323,Link,DocumentCited by:§1,§1.
- [16]S. Singh and R. Melnik(2020-04)Thermal ablation of biological tissues in disease treatment: A review of computational models and future directions.Electromagnetic Biology and Medicine39(2),pp. 49–88(eng).External Links:ISSN 1536-8386,DocumentCited by:§1,§2.1,§2.1,§2.1.
- [17]K. Sugimotoet al.(2025-01)Microwave ablation vs. single-needle radiofrequency ablation for the treatment of HCC up to 4 cm: A randomized-controlled trial.JHEP Reports7(1),pp. 101269(en).External Links:ISSN 25895559,Link,DocumentCited by:§1.
- [18]J. Tu, B. Wang, X. Wang, K. Huo, W. Hu, R. Zhang, J. Li, S. Zhu, Q. Liang, and S. Han(2024-12)Current status and new directions for hepatocellular carcinoma diagnosis.Liver Research8(4),pp. 218–236(en).External Links:ISSN 25425684,Link,DocumentCited by:§1.
- [19]N. Vaidya, M. Baragona, V. Lavezzo, R. Maessen, and K. Veroy(2022-08)Tuning the Pennes Perfusion Rate to Model Large Vessel Cooling Effects in Hepatic Radiofrequency Ablation.Journal of Biomechanical Engineering144(8),pp. 084506(en).External Links:ISSN 0148-0731, 1528-8951,Link,DocumentCited by:§2.3.
- [20]R. S. Winokuret al.(2014)Characterization of in vivo ablation zones following percutaneous microwave ablation of the liver with two commercially available devices: are manufacturer published reference values useful?.Journal of Vascular and Interventional Radiology25(12),pp. 1939–1946.e1.External Links:ISSN 1051-0443,Document,LinkCited by:§1.
- [21]Q. Zhu, Y. Shen, A. Zhang, and L. X. Xu(2013-12-10)Numerical study of the influence of water evaporation on Radiofrequency ablation.BioMedical Engineering OnLine12(1),pp. 127.External Links:ISSN 1475-925X,Document,LinkCited by:§2.1,§2.1.

## 


- 


Major funding support from
