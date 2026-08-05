# Solar Cruiser Disturbance Torque Estimation and Predictive Momentum Management

**arXiv ID**: 2601.00532v3
**Authors**: Ping-Yen Shen, Ryan J. Caverly
**Published**: 2026-01-02
**Categories**: physics.space-ph, math.OC
**Comments**: Submitted to Advances in Space Research
**HTML URL**: https://arxiv.org/html/2601.00532v3

## Abstract

This paper presents a novel disturbance-torque-estimation-augmented model predictive control (MPC) framework to perform momentum management on NASA's Solar Cruiser solar sail mission. Solar Cruiser represents a critical step in the advancement of large-scale solar sail technology and includes the innovative use of an active mass translator (AMT) and reflectivity control devices (RCDs) as momentum management actuators. The coupled nature of these actuators has proven challenging in the development of a robust momentum management controller. Recent literature has explored the use of MPC for solar sail momentum management with promising results, although exact knowledge of the disturbance torques acting on the solar sail was required. This paper amends this issue through the use of a Kalman filter to provide real-time estimation of unmodeled disturbance torques. Furthermore, the dynamics model used in this paper incorporates key fidelity enhancements compared to prior work, including Solar Cruiser's four-reaction-wheel assembly and the offset between its center of mass and center of pressure. More realistic operation scenarios involving the tracking of large angle slew maneuvers under attitude-dependent solar radiation force and torque are also performed to further validate the proposed method compared to prior work. Simulation results demonstrate that the proposed policy successfully manages angular momentum growth under slew maneuvers that exceed the operational envelope of the current state-of-the-art method. The inclusion of the disturbance torque estimate is shown to greatly improve the reliability and performance of the proposed MPC approach. This work establishes a new benchmark for Solar Cruiser's momentum management capabilities and paves the way for MPC-based momentum management of other solar sails making use of an AMT and/or RCDs.

## Full Text

Solar Cruiser Disturbance Torque Estimation and Predictive Momentum Management

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
- License: CC BY 4.0arXiv:2601.00532v3 [physics.space-ph] 04 Jun 2026

## Solar Cruiser Disturbance Torque Estimation and Predictive Momentum ManagementPing-Yen ShenRyan J. Caverlyrcaverly@umn.edu

## Abstract

This paper presents a novel disturbance-torque-estimation-augmented model predictive control (MPC) framework to perform momentum management on NASA’s Solar Cruiser solar sail mission.
Solar Cruiser represents a critical step in the advancement of large-scale solar sail technology and includes the innovative use of an active mass translator (AMT) and reflectivity control devices (RCDs) as momentum management actuators. The coupled nature of these actuators has proven challenging in the development of a robust momentum management controller. Recent literature has explored the use of MPC for solar sail momentum management with promising results, although exact knowledge of the disturbance torques acting on the solar sail was required.
This paper amends this issue through the use of a Kalman filter to provide real-time estimation of unmodeled disturbance torques. Furthermore, the dynamics model used in this paper incorporates key fidelity enhancements compared to prior work, including Solar Cruiser’s four-reaction-wheel assembly and the offset between its center of mass and center of pressure. More realistic operation scenarios involving the tracking of large angle slew maneuvers under attitude-dependent solar radiation force and torque are also performed to further validate the proposed method compared to prior work.
Simulation results demonstrate that the proposed policy successfully manages angular momentum growth under slew maneuvers that exceed the operational envelope of the current state-of-the-art method.
The inclusion of the disturbance torque estimate is shown to greatly improve the reliability and performance of the proposed MPC approach. This work establishes a new benchmark for Solar Cruiser’s momentum management capabilities and paves the way for MPC-based momentum management of other solar sails making use of an AMT and/or RCDs.

## keywords:Solar Sails , Momentum Management , Model Predictive Control (MPC) , Disturbance Estimation , Kalman Filtering , Solar Cruiser††journal:Advances in Space Research\affiliation

[1]organization=Department of Aerospace Engineering and Mechanics, University of Minnesota, Twin Cities,
addressline=110 Union St. SE,
city=Minneapolis, MN,
postcode=55455,
country=USA

## 1Introduction

Solar sails have the potential to remove the space exploration limits imposed by traditional propellant-based propulsion, thus unlocking a wide range of missions previously unattainable by conventional spacecraft(Macdonald and McInnes,2011; Berthet et al.,2024; Farres,2023; Miller et al.,2022; Farrés et al.,2019). Effectively leveraging the propulsion induced by solar radiation pressure (SRP) and unlocking solar sail travel requires both advancements in the design and deployment of large sail structures(Vatankhahghadim and Damaren,2021; Hibbert and Jordaan,2021; Huang et al.,2021)and the concurrent development of advanced control technology(Chen et al.,2023; Inness et al.,2024,2023).
NASA’s Solar Cruiser, which features a massive sail membrane area exceeding1,6001,600m2, is designed to pioneer next-generation space exploration capabilities and enable groundbreaking heliophysics observations(Johnson et al.,2019; Johnson and Curran,2020; Johnson et al.,2022; Pezent et al.,2021).

Generating the required propulsion from SRP necessitates precise pointing via attitude control. However, the operation of such large, flexible structures introduces significant control challenges(Boni et al.,2023; Fu and Eke,2015; Firuzi and Gong,2018). Imperfect sail shapes and structural flexibility induce persistent disturbance torques(Gauvain and Tyler,2023)that cause angular momentum accumulation within the onboard reaction wheels (RWs).
This necessitates effective momentum management to desaturate the RWs and prevent a loss of attitude control authority.
Conventional momentum management methods, such as thrusters or magnetic torquers, are unsuitable for long-term, interplanetary, deep-space missions because they either require fuel or are limited to operations near Earth’s magnetic field. Innovative actuation methodologies have been developed to adapt to solar sail missions(Wie,2004; Orphee et al.,2018; Lee et al.,2025).
On Solar Cruiser, momentum management is achieved using two specialized actuators: the active mass translator (AMT) and reflectivity control devices (RCDs)(Inness et al.,2023).

Solar Cruier’s AMT functions as an internal mechanism that shifts the spacecraft’s center of mass (CM) relative to the sail’s center of pressure (CP) in a plane parallel to the sail surface. This controllable motion produces SRP-induced torques to counteract disturbance torques in the pitch and yaw axes (torques within the plane of the sail) and unload RW angular momentum(Orphee et al.,2018).
The RCDs consist of thin-film membrane pairs, positioned near the tip of each sail boom, set at fixed opposite inclination angles(Heaton et al.,2023).
These devices generate a net roll-axis torque (torque normal to the plane of the sail) by selectively varying the reflectivity of the appropriate RCD membranes via applied voltages, resulting from an imbalance in the differential SRP forces.
A key operational constraint of RCDs is their binary actuation, as they function in an on-off manner, capable only of generating either zero torque or a fixed-magnitude torque in the positive or negative roll direction.

The current design of Solar Cruiser employs a decoupled momentum management strategy, where individual-channel threshold-activated proportional-integral-derivative (PID) controllers command the AMT’s two axes and a threshold-based strategy governs the RCDs(Tyler et al.,2023).
While this approach has been shown to manage angular momentum successfully(Inness et al.,2023), its reliance on purely reactive, threshold-based methods, as well as its neglect of coupled interactions between the AMT motion, RCD input, and the resulting effect on motion in all three axes are significant limitations.
Specifically, the inability of this state-of-the-art method to optimize the AMT and RCD inputs in a coordinated fashion and proactively prevent RW angular momentum saturation limits its performance under larger slew maneuvers.

The increasing computational capability of modern flight hardware has established model predictive control (MPC) as a viable and practical option for spacecraft attitude determination and control(Di Cairano and Kolmanovsky,2018; Eren et al.,2017; Caverly et al.,2020; Halverson et al.,2025).
MPC is a control methodology that solves an online optimization problem to determine the optimal future sequence of control actions, simultaneously enforcing constraints on both state trajectories and actuator limits, with a receding-horizon. The properties of solar sail dynamics are particularly amenable to this strategy. The low magnitude of SRP ensures slew maneuvers are inherently slow and result in smooth system dynamics.
Moreover, MPC has the potential to enforce the hard constraints associated with RW saturation and optimally allocate the limited control authority associated solar sail actuators through state and input constraints.
This combination of long time scales available for onboard processing and the need to enforce state and input constraints make MPC an ideal choice for the intricate task of solar sail momentum management.

Prior work byShen and Caverly (2026)developed MPC-based momentum management strategies tailored for solar sails equipped with an AMT and RCDs.
They developed a dynamics model that captured key features of the AMT movement, including the resultant time-varying changes in the spacecraft’s CM and moment of inertia matrix.
The MPC policy developed in the work ofShen and Caverly (2026)leveraged its optimization capabilities to handle the actuator constraints and requirements, including the enforcement of on-off RCD actuation and AMT motion rate limits, all while incorporating tuning parameters designed to adjust the trade-off between system performance and control effort.
For real-time onboard implementation, the MPC formulation was posed as a quadratic program (QP), which guarantees fast and robust convergence suitable for the short processing cycles required by the flight computer.
The work ofShen and Caverly (2025)further examined the critical balance between model fidelity and computational cost when implementing the MPC policy developed byShen and Caverly (2026)to determine feasibility for real-time implementation.
However, these MPC implementations both make unrealistic assumptions that the SRP force and torque acting on the solar sail remain constant and that exact knowledge of the disturbance torque acting on the solar sail is available for use within MPC’s prediction model.
These are significant assumptions that limit the practical implementation of the MPC policy proposed byShen and Caverly (2026). The SRP forces and torques acting on the solar sail are attitude-dependent and it is virtually impossible to accurately predict disturbance torques from analytical models due to the unpredictable shape deformation of the solar sail and temporal changes in the sail’s optical properties(Wang et al.,2025; Gauvain and Tyler,2023). The use of an inaccurate torque model within the MPC framework significantly degrades momentum management performance, negating the purported benefits of the MPC momentum management policy. Another practical limitation of the work ofShen and Caverly (2026,2025)is that their implementations assume that the solar sail is equipped with three RWs aligned with the principal axes of its body-fixed frame. Many spacecraft, including Solar Cruiser, have a 4-RW assembly for redundancy and increased performance, which precludes the use of the methods developed byShen and Caverly (2026,2025). Furthermore, the implementation in the work ofShen and Caverly (2026)assumed that the RWs remained in the same plane as the solar sail’s CP, which is not representative of Solar Cruiser’s geometry. A final limitation to note in the work ofShen and Caverly (2026)is that it is only capable of regulating the solar sail to a fixed attitude (i.e., an attitude hold). This does not meet the practical needs of a solar sail mission, which may require performing attitude slews.

To overcome the limitations of prior work, this paper presents a novel MPC-based momentum management policy that incorporates disturbance torque estimation, a 4-RW assembly tailored for the Solar Cruiser mission, an attitude-dependent SRP force and torque, and the ability to track attitude slews. A Kalman filter framework is used to estimate the unmodeled disturbance torques and system model errors in real time, thus enhancing the predictive capability of the MPC. Similar Kalman-filtering approaches have been used in the literature to estimate unknown parameters or terms within a system model(Zenere and Zorzi,2018; Woodbury and Junkins,2010; Hayes and Caverly,2025; Ahmed et al.,2024).
For example,Hayes and Caverly (2025)used a Kalman filter to estimate the unknown atmospheric density of a satellite during an orbital reentry, whileAhmed et al. (2024)estimated the unknown wind acting on a small uncrewed air vehicle.
Solar Cruiser’s 4-RW assembly is accounted for within the proposed MPC implementation through the use of the commonly-used pseudo-inverse RW allocation approach(Leve et al.,2015; Markley and Crassidis,2014). This provides the MPC prediction model with accurate knowledge of the dynamics of each individual RW, allowing for their operation to be constrained within their saturation limits.

This paper presents four key contributions relative to the state-of-the-art in solar sail momentum management, including prior work on MPC-based methods byShen and Caverly (2026,2025). The first contribution is a robust MPC momentum management formulation that uses a Kalman filter to estimate unknown disturbance torques acting on the solar sail. To the best of the knowledge of the authors, this is the first realistically-implementable momentum management policy for a solar sail equipped with an AMT and RCD that outperforms the method ofTyler et al. (2023). The second contribution is the incorporation of a 4-RW assembly within an MPC-based momentum management policy. To the best of the knowledge of the authors, this is the first MPC-based momentum management policy to consider a realistic 4-RW assembly. The third contribution is an assessment of the proposed momentum management policy in a realistic simulation of Solar Cruiser’s dynamics. Specifically, its CM is located a distance from the sail plane, non-ideal and attitude-dependent SRP forces and torques are considered, and the magnitude of the roll torque generated by the RCDs is modeled as attitude-dependent. All of these effects are meaningful when considering Solar Cruiser’s dynamics, as they result in substantial coupling between the system’s dynamics and actuation, yet they were not considered in the prior work ofShen and Caverly (2026).
The fourth contribution is the augmentation of the proposed MPC policy to track large angle slew maneuvers, which is an important operational requirement of a typical solar sail mission. This improvement expands well-beyond the attitude hold capabilities formulated and demonstrated in the prior work ofShen and Caverly (2026).

Details of the nonlinear system dynamics of Solar Cruiser,
the 4-RW control allocation algorithm, and the momentum management actuators are presented in Section2. This section also provides the linearized dynamics model used in the Kalman filter and MPC frameworks.
The Kalman filter formulation is presented in Section3, providing details of how the unmeasurable disturbance torques are estimated.
The MPC formulation is presented in Section4, detailing the implementation of estimation-prediction framework and the incorporation of the 4-RW assembly into the MPC prediction model.
Numerical simulation results are presented in Section5, validating the performance of the proposed estimation-augmented MPC with comparisons to Solar Cruiser’s state-of-the-art momentum management method(Tyler et al.,2023). Results in this section are also presented that demonstrate the effect of actuation thresholds within the proposed momentum management policy on actuation efficiency and observability of the roll-axis disturbance torque. A description of the reference slew maneuver used in this work is included in the Appendix.

## 2Attitude Dynamics and Control Actuation

NASA’s Solar Cruiser uses AMT and RCDs as its momentum management actuators(Inness et al.,2023).
The AMT changes the relative alignment of the CM and CP such that the SRP force acting on the CP results in a corresponding torque about the CM.
Moving the AMT and appropriately placing the CM/CP offset results in a controllable moment that unloads the accumulated RW angular momentum.
However, the moment of inertia matrix changes when the AMT moves and the mass distribution of the sailcraft changes.
The dynamics are thus coupled with the AMT translation.
This section presents the dynamics and control of the sailcraft, starting with important notation and proceeding with its attitude dynamics, the RW attitude control law, details regarding the momentum management control actuation, and the linearized attitude dynamics model used for the Kalman filter and MPC frameworks.

## 2.1Notation

The identity matrix of dimensionn×nn\times nis denoted as𝟏𝐧×𝐧\mbf{1}_{n\times n}, while ann×mn\times mmatrix of zeros is given by𝟎𝐧×𝐦\mbf{0}_{n\times m}.
Physical vectors are denoted asv→{\underrightarrow{{v}}}. Reference frameℱa\mathcal{F}_{a}is defined by three orthonormal, dextral physical basis vectorsa→1{\underrightarrow{{a}}}^{1},a→2{\underrightarrow{{a}}}^{2}, anda→3{\underrightarrow{{a}}}^{3}. The physical vectorv→{\underrightarrow{{v}}}resolved inℱa\mathcal{F}_{a}is denoted as𝐯𝐚=[𝐯𝐚𝟏𝐯𝐚𝟐𝐯𝐚𝟑]𝖳\mbf{v}_{a}=\begin{bmatrix}v_{a1}&v_{a2}&v_{a3}\end{bmatrix}^{\mathsf{T}}. The position of pointqqrelative to pointzzis given byr→q​z{\underrightarrow{{r}}}^{qz}, which is expressed as𝐫𝐚𝐪𝐳\mbf{r}_{a}^{qz}when resolved in reference frameℱa\mathcal{F}_{a}. The cross product operator(⋅)×(\cdot)^{\times}is used to compute the cross product of two vectors resolved in a particular reference frame. For example,u→×v→{\underrightarrow{{u}}}\times{\underrightarrow{{v}}}resolved inℱa\mathcal{F}_{a}is computed as𝐮𝐚×​𝐯𝐚\mbf{u}_{a}^{\times}\mbf{v}_{a}, where𝐮𝐚×=[𝟎−𝐮𝐚𝟑𝐮𝐚𝟐𝐮𝐚𝟑𝟎−𝐮𝐚𝟏−𝐮𝐚𝟐𝐮𝐚𝟏𝟎],\mbf{u}_{a}^{\times}=\begin{bmatrix}0&-u_{a3}&u_{a2}\\
u_{a3}&0&-u_{a1}\\
-u_{a2}&u_{a1}&0\end{bmatrix},

and𝐮𝐚=[𝐮𝐚𝟏𝐮𝐚𝟐𝐮𝐚𝟑]𝖳\mbf{u}_{a}=\begin{bmatrix}u_{a1}&u_{a2}&u_{a3}\end{bmatrix}^{\mathsf{T}}.

The direction cosine matrix (DCM)𝐂𝐛𝐚\mbf{C}_{ba}describes the attitude of reference frameℱb\mathcal{F}_{b}relative to reference frameℱa\mathcal{F}_{a}. While different attitude parameterizations can be used to describe a DCM, Euler-angle sequences are used in this work due to their ease of physical interpretation and the lack of any large-angle maneuvers that would potentially result in a kinematic singularity. The DCM can be used to express a physical vector in different reference frames. For example,𝐯𝐛=𝐂𝐛𝐚​𝐯𝐚\mbf{v}_{b}=\mbf{C}_{ba}\mbf{v}_{a}.

Within the proposed MPC policy, the subscriptj|tkj|t_{k}is used to refer to system states or inputsjjtime steps ahead of the current time steptkt_{k}.

## 2.2Solar Cruiser Attitude DynamicsFigure 1:Depictions of the Solar Cruiser model used in this paper (not drawn to scale) highlighting (a) its attitude control and momentum management actuators, including four RWs (light blue), AMT (red) and RCDs (brown and orange); and (b) the definition of key bodies and, such as the sail𝒮\mathcal{S}with CMss(also the CP of the entire sailcraft) and the bus𝒫\mathcal{P}with CMss, as well as the entire sailcraft’s CMcc.

Following the approach ofShen and Caverly (2026)and as illustrated in Fig.1, Solar Cruiser’s sail is modeled as a thin flat plate (denoted as𝒮\mathcal{S}) and a rigid rectangular bus (denoted as𝒫\mathcal{P}). The nonlinear rigid-body attitude dynamics of a solar sail incorporating the AMT translation as a control input were derived byShen and Caverly (2026), including the time-dependent moment of inertia matrix corresponding to the AMT position.
It is assumed that the each RW spin axis aligns with the position of the RW relative to the CM of the bus (pointpp). Although this assumption is not necessarily required to implement the proposed momentum management method, it removes additional coupling terms in the dynamics that can often be calibrated for upon spacecraft commissioning. As shown in Fig.1, the sailcraft body frameℱb\mathcal{F}_{b}is defined withb→3\underrightarrow{b}^{3}pointing through the normal (roll) axis of the sail, andb→2\underrightarrow{b}^{2},b→1\underrightarrow{b}^{1}pointing within the plane of the sail and representing the pitch and yaw axes, respectively.
The moment of inertia matrix relative to the sailcraft’s CM (pointcc) is defined as𝐉𝐛ℬ​𝐜​(𝐭)=𝐉𝐛𝒮​𝐬+𝐉𝐛𝒫​𝐩−𝐦𝐩𝟑+𝐦𝐬𝟑(𝐦𝐩+𝐦𝐬)𝟐​𝐫𝐛𝐩𝐬×​(𝐭)​𝐫𝐛𝐩𝐬×​(𝐭),\mbf{J}_{b}^{\mathcal{B}c}(t)=\mbf{J}^{\mathcal{S}s}_{b}+\mbf{J}^{\mathcal{P}p}_{b}-\frac{m_{p}^{3}+m_{s}^{3}}{(m_{p}+m_{s})^{2}}\mbf{r}_{b}^{{ps}^{\times}}(t)\mbf{r}_{b}^{{ps}^{\times}}(t),

wheremsm_{s}andmpm_{p}are the masses of the sail and the bus, respectively,𝐉𝐛𝒮​𝐬\mbf{J}^{\mathcal{S}s}_{b}and𝐉𝐛𝒫​𝐩\mbf{J}^{\mathcal{P}p}_{b}are the nominal moment of inertia matrices of the sail and bus relative to each of their own CMs (pointsssandpp), respectively, and the position𝐫𝐛𝐩𝐬​(𝐭)=[𝐫𝐛𝟏AMT​(𝐭)​𝐫𝐛𝟐AMT​(𝐭)​𝐫𝐛𝟑𝐩𝐬]𝖳\mbf{r}^{ps}_{b}(t)=\Big[r^{\text{AMT}}_{b1}(t)\,\,\,r^{\text{AMT}}_{b2}(t)\,\,\,{r}^{ps}_{b3}\Big]^{\mathsf{T}}contains the controllable AMT positionsrb​1AMT​(t)r^{\text{AMT}}_{b1}(t)andrb​2AMT​(t)r^{\text{AMT}}_{b2}(t). These AMT positions are actuated via the red linear actuators visualized in Fig.1.
The constant componentrb​3p​s{r}^{ps}_{b3}represents the constant offset distance in theb→3{\underrightarrow{{b}}}^{3}sail-normal direction between the CM of the sail and the CM of the bus.

Letℱa\mathcal{F}_{a}, defined by basis vectorsa→1\underrightarrow{a}^{1},a→2\underrightarrow{a}^{2},a→3\underrightarrow{a}^{3}, be an inertial reference frame. The solar sail attitude dynamics with mass translation are defined as(Shen and Caverly,2026)𝐉𝐛ℬ​𝐜​𝝎˙𝐛𝐛𝐚+𝝎𝐛𝐛𝐚×​𝐉𝐛ℬ​𝐜​𝝎𝐛𝐛𝐚+𝝎𝐛𝐛𝐚×​𝐡𝐛RW+𝐡˙𝐛RW+𝐦𝐩𝟑+𝐦𝐬𝟑(𝐦𝐩+𝐦𝐬)𝟐​(𝐫𝐛𝐩𝐬×​𝐫¨𝐛𝐩𝐬−𝟐​𝐫˙𝐛𝐩𝐬×​𝐫𝐛𝐩𝐬×​𝝎𝐛𝐛𝐚)=𝝉𝐛ℬ​𝐜,\mbf{J}_{b}^{\mathcal{B}c}\dot{{\boldsymbol{\omega}}}_{b}^{ba}+{\boldsymbol{\omega}}_{b}^{ba^{\times}}\mbf{J}_{b}^{\mathcal{B}c}{\boldsymbol{\omega}}_{b}^{ba}+{\boldsymbol{\omega}}_{b}^{ba^{\times}}\mbf{h}_{b}^{\text{RW}}+\dot{\mbf{h}}_{b}^{\text{RW}}+\frac{m_{p}^{3}+m_{s}^{3}}{(m_{p}+m_{s})^{2}}\bigg(\mbf{r}_{b}^{ps^{\times}}\ddot{\mbf{r}}_{b}^{ps}-2\dot{\mbf{r}}_{b}^{ps^{\times}}\mbf{r}_{b}^{ps^{\times}}{\boldsymbol{\omega}}_{b}^{ba}\bigg)={\boldsymbol{\tau}}_{b}^{\mathcal{B}c},(1)

where𝝎bb​a{\boldsymbol{\omega}}_{b}^{ba}is the angular velocity ofℱb\mathcal{F}_{b}relative toℱa\mathcal{F}_{a}resolved inℱb\mathcal{F}_{b},𝐡𝐛RW\mbf{h}_{b}^{\text{RW}}is the collective angular momentum of the RWs relative to the CM of the bus (pointpp) with respect to inertial reference frameℱa\mathcal{F}_{a}resolved inℱb\mathcal{F}_{b}.
The term𝝉bℬ​c=𝝉bAMT+𝝉bRCD+𝝉bdist{\boldsymbol{\tau}}_{b}^{\mathcal{B}c}={\boldsymbol{\tau}}_{b}^{\text{AMT}}+{\boldsymbol{\tau}}_{b}^{\text{RCD}}+{\boldsymbol{\tau}}_{b}^{\text{dist}}is the torque acting on the sailcraft relative to its CM, consisting of the AMT-SRP-induced torque𝝉bAMT=msmp+ms​𝐫𝐛𝐩𝐬×​𝐟𝐛SRP{\boldsymbol{\tau}}_{b}^{\text{AMT}}=\frac{m_{s}}{m_{p}+m_{s}}\mbf{r}_{b}^{ps^{\times}}\mbf{f}_{b}^{\text{SRP}}, the RCD torque𝝉bRCD{\boldsymbol{\tau}}_{b}^{\text{RCD}}, and the disturbance torque𝝉bdist{\boldsymbol{\tau}}_{b}^{\text{dist}}. The term𝐟𝐛SRP\mbf{f}_{b}^{\text{SRP}}denotes the solar radiation pressure induced force acting on the sail’s CP.
The RCD torque is generated by activating one of the set of four RCDs (either brown or orange) visualized in Fig.1. Actuating the orange RCDs generates a positive roll torque aboutb→3\underrightarrow{b}^{3}axis, while actuating the brown RCDs generates a negative torque about this same axis.
The time-dependent argument (t) for the variables𝐉𝐛ℬ​𝐜​(𝐭)\mbf{J}_{b}^{\mathcal{B}c}(t),𝐫𝐛𝐩𝐬​(𝐭)\mbf{r}^{ps}_{b}(t),𝝎bb​a​(t){\boldsymbol{\omega}}_{b}^{ba}(t),𝐡𝐛RW​(𝐭)\mbf{h}_{b}^{\text{RW}}(t),𝝉bℬ​c​(t){\boldsymbol{\tau}}_{b}^{\mathcal{B}c}(t)is omitted for brevity in Eq. (1).

A 3-2-1 Euler angle sequence is used to describe the rotation betweenℱa\mathcal{F}_{a}andℱb\mathcal{F}_{b}, so that𝐂𝐛𝐚=𝐂𝟏​(θ𝟏)​𝐂𝟐​(θ𝟐)​𝐂𝟑​(θ𝟑)\mbf{C}_{ba}=\mbf{C}_{1}(\theta_{1})\mbf{C}_{2}(\theta_{2})\mbf{C}_{3}(\theta_{3})is the DCM describing the orientation ofℱb\mathcal{F}_{b}relative toℱa\mathcal{F}_{a}, where𝐂𝐢​(⋅)\mbf{C}_{i}(\cdot)is the DCM representing a rotation about theii-th principal axis. The mapping𝝎bb​a=𝐒​(𝜽)​𝜽˙{\boldsymbol{\omega}}^{ba}_{b}=\mbf{S}({\boldsymbol{\theta}})\dot{{\boldsymbol{\theta}}}relates Euler angle rates to angular velocity, where the column matrix𝜽=[θ1​θ2​θ3]𝖳{\boldsymbol{\theta}}=\Big[\theta_{1}\,\,\,\theta_{2}\,\,\,\theta_{3}\Big]^{\mathsf{T}}is the set of Euler angles and𝐒​(𝜽)\mbf{S}({\boldsymbol{\theta}})is the mapping matrix.
It is worth noting that𝐒​(𝜽)\mbf{S}({\boldsymbol{\theta}})depends only onθ1\theta_{1}andθ2\theta_{2}due to the selected 3-2-1 Euler angle sequence. Given that a solar sail is designed to keep the Sun within its field of view and maintain a nominal spin about theb→3\underrightarrow{b}^{3}axis, this choice allows for ease of linearization about any nominal angular velocity about theb→3\underrightarrow{b}^{3}axis, and positions the kinematic singularity at180​°180\text{\textdegree}from the nominal inertial pointing attitude.

Generally, the forces and torques induced by SRP vary with the attitude of the solar sail, the shape of the sail membrane, and its optical properties. Given the slow nature of solar sail maneuvers, it is assumed that vibrations in the structure are minimal and both the sail shape and material properties remain static, which implies that𝐟𝐛SRP\mbf{f}_{b}^{\text{SRP}}and𝝉bdist{\boldsymbol{\tau}}_{b}^{\text{dist}}depend solely on the attitude of the sailcraft. The optical properties of the Solar Cruiser membrane(Heaton and Artusio-Glimpse,2015; Heaton et al.,2017)and its expected deformations(Gauvain and Tyler,2023)are incorporated into the static membrane shape model developed byBunker and Caverly (2026). This model is then employed to compute𝐟𝐛SRP\mbf{f}_{b}^{\text{SRP}}and𝝉bdist{\boldsymbol{\tau}}_{b}^{\text{dist}}based on the solar sail’s attitude𝜽{\boldsymbol{\theta}}in this work.

## 2.3Reaction Wheel Control and Allocation

The RWs onboard the sailcraft generate the vehicle’s attitude control torques through an increase or decrease in the angular momentum of the RWs. Solar Cruiser has a 4-RW assembly, which requires control allocation to determine the action to be taken by each individual RW in order to generate the required attitude control torque. Details regarding the attitude control law, the RW geometric configuration, and the RW control allocation methodology used in this work are presented in this section.

## 2.3.1Attitude Control Law

Many advanced RW attitude control methods exist that could be implemented to meet the solar sail’s attitude control requirements.
This paper employs a simple PID attitude control law to mimic the controller developed for Solar Cruiser(Inness et al.,2023).
The desired control torque to be generated by the RWs is defined through a PID control law as𝝉b,desRW=−𝐡˙b,desRW=−𝐊𝐩​(𝜽​(𝐭)−𝜽𝐝​(𝐭))−𝐊𝐝​(𝝎𝐛𝐛𝐚​(𝐭)−𝝎𝐝​(𝐭))−𝐊𝐢​∫𝐭𝟎𝐭(𝜽​(τ)−𝜽𝐝​(τ))​d​τ,{\boldsymbol{\tau}}^{\text{RW}}_{b,\text{des}}=-\dot{\mbf{h}}^{\text{RW}}_{b,\text{des}}=-\mbf{K}_{p}\bigg({\boldsymbol{\theta}}(t)-{\boldsymbol{\theta}}_{d}(t)\bigg)-\mbf{K}_{d}\bigg({\boldsymbol{\omega}}^{ba}_{b}(t)-{\boldsymbol{\omega}}_{d}(t)\bigg)-\mbf{K}_{i}\int^{t}_{t_{0}}\bigg({\boldsymbol{\theta}}(\tau)-{\boldsymbol{\theta}}_{d}(\tau)\bigg)\textrm{d}\tau,(2)

where𝜽d​(t){\boldsymbol{\theta}}_{d}(t)and𝝎d​(t)=𝐒−𝟏​(𝜽𝐝​(𝐭))​𝜽˙𝐝​(𝐭){\boldsymbol{\omega}}_{d}(t)=\mbf{S}^{-1}({\boldsymbol{\theta}}_{d}(t))\dot{{\boldsymbol{\theta}}}_{d}(t)are the desired Euler angles and angular velocity of the desired trajectory, respectively. In this work,𝜽d{\boldsymbol{\theta}}_{d}and𝜽˙d\dot{{\boldsymbol{\theta}}}_{d}are chosen to be a smooth trajectory matching a rest-to-rest maneuver with a trapezoidal Euler angle rate profile. Details of the time-dependent desired trajectory can be found in the Appendix. A different trajectory can be selected based on specific mission scenarios.

## 2.3.2Reaction Wheels Assembly Geometry

Solar Cruiser uses four RWs as its primary attitude control actuators(Inness et al.,2023).
The attitude dynamics, as established in Eq. (1) within the sailcraft’s body frame, include the three-dimensional total angular momentum of the four RWs,𝐡𝐛RW\mbf{h}_{b}^{\text{RW}}, as well as its time derivative𝐡˙bRW\dot{\mbf{h}}_{b}^{\text{RW}}. The variables𝐡𝐛RW\mbf{h}_{b}^{\text{RW}}and𝐡˙bRW\dot{\mbf{h}}_{b}^{\text{RW}}represent projections of the angular momentum of the 4-RW configuration onto the three body-frame axes. This results in the linear relationships𝐡𝐛RW=𝐌𝟑𝟒​𝐡𝟒RW,\mbf{h}_{b}^{\text{RW}}=\mbf{M}_{34}\mbf{h}^{\text{RW}}_{4},

and𝐡˙bRW=𝐌𝟑𝟒​𝐡˙𝟒RW,\dot{\mbf{h}}_{b}^{\text{RW}}=\mbf{M}_{34}\dot{\mbf{h}}^{\text{RW}}_{4},

where𝐡𝟒RW=[𝐡𝟏𝐡𝟐𝐡𝟑𝐡𝟒]𝖳\mbf{h}^{\text{RW}}_{4}=\begin{bmatrix}h_{1}&h_{2}&h_{3}&h_{4}\end{bmatrix}^{\mathsf{T}}comprises the four individual RW angular momentum values. The allocation matrix𝐌𝟑𝟒∈ℝ𝟑×𝟒\mbf{M}_{34}\in\mathbb{R}^{3\times 4}is time invariant and is determined entirely by the geometric configuration of the four RWs.
The time-derivative of the total RW angular momentum projected onto the body frame directly yields the reaction torque exerted on the spacecraft, where𝐡˙bRW=−𝝉bRW\dot{\mbf{h}}^{\text{RW}}_{b}=-{\boldsymbol{\tau}}^{\text{RW}}_{b}.

The optimal geometric configuration of a 4-RW assembly has been investigated extensively in the literature(Ismail and Varatharajoo,2010; Bellar et al.,2016; Lee et al.,2017; Leve et al.,2015; Markley and Crassidis,2014). In the absence of any direct information regarding the configuration used by Solar Cruiser, the common pyramidal configuration is used, where it is assumed that the spin axis of each RW passes through the CM of the sailcraft bus.
This choice of RW configuration only affects the definition of𝐌𝟑𝟒\mbf{M}_{34}, allowing the methods presented in this paper to be adapted to other configurations if desired.

To derive the expression for𝐌𝟑𝟒\mbf{M}_{34}, consider theii-th RW as a rigid disk rotating about its axis of symmetrywi3→{\underrightarrow{{w^{3}_{i}}}}, in its rotating frameℱwi\mathcal{F}_{w_{i}}. The reference frameℱwi\mathcal{F}_{w_{i}}is obtained fromℱb\mathcal{F}_{b}by rotatingψi\psi_{i}aboutb3→{\underrightarrow{{b^{3}}}}, then rotatingϕi\phi_{i}about the rotatedb2→{\underrightarrow{{b^{2}}}}axis. In this paperψi=60∘\psi_{i}=60^{\circ}for allii, andϕi=45∘+(i−1)⋅90∘\phi_{i}=45^{\circ}+(i-1)\cdot 90^{\circ},i=1,2,3,4i=1,2,3,4.
The DCM defining the orientation ofℱwi\mathcal{F}_{w_{i}}relative to the body frameℱb\mathcal{F}_{b}is given by𝐂𝐰𝐢​𝐛=𝐂𝐛𝐰𝐢𝖳=𝐂𝟐​(ϕ𝐢)​𝐂𝟑​(ψ𝐢)=[cos⁡ϕ𝐢​cos⁡ψ𝐢cos⁡ϕ𝐢​sin⁡ψ𝐢−sin⁡ϕ𝐢−sin⁡ψ𝐢cos⁡ψ𝐢𝟎sin⁡ϕ𝐢​cos⁡ψ𝐢sin⁡ϕ𝐢​sin⁡ψ𝐢cos⁡ϕ𝐢].\mbf{C}_{w_{i}b}=\mbf{C}_{bw_{i}}^{\mathsf{T}}=\mbf{C}_{2}(\phi_{i})\mbf{C}_{3}(\psi_{i})=\begin{bmatrix}\cos\phi_{i}\cos\psi_{i}&\cos\phi_{i}\sin\psi_{i}&-\sin\phi_{i}\\
-\sin\psi_{i}&\cos\psi_{i}&0\\
\sin\phi_{i}\cos\psi_{i}&\sin\phi_{i}\sin\psi_{i}&\cos\phi_{i}\end{bmatrix}.

The angular velocity ofℱwi\mathcal{F}_{w_{i}}relative toℱb\mathcal{F}_{b}expressed inℱb\mathcal{F}_{b}is𝝎bwi​b=𝐂𝐛𝐰𝐢​[𝟎𝟎γ˙𝐢]=[sin⁡ϕ𝐢​cos⁡ψ𝐢sin⁡ϕ𝐢​sin⁡ψ𝐢cos⁡ϕ𝐢]​γ˙𝐢,{\boldsymbol{\omega}}_{b}^{w_{i}b}=\mbf{C}_{bw_{i}}\begin{bmatrix}0\\
0\\
\dot{\gamma}_{i}\end{bmatrix}=\begin{bmatrix}\sin{\phi_{i}}\cos{\psi_{i}}\\
\sin{\phi_{i}}\sin{\psi_{i}}\\
\cos{\phi_{i}}\end{bmatrix}\dot{\gamma}_{i},

whereγ˙i\dot{\gamma}_{i}denotes the spin rate of theii-th RW.
The moment of inertia matrix of theii-th RW is given by𝐉𝐰𝐢𝒲𝐢​𝐩=diag​(𝐦𝐰​𝐫𝐰𝟐𝟒,𝐦𝐰​𝐫𝐰𝟐𝟒,𝐦𝐰​𝐫𝐰𝟐𝟐)\mbf{J}_{w_{i}}^{\mathcal{W}_{i}p}=\text{diag}(\frac{m_{w}r_{w}^{2}}{4},\frac{m_{w}r_{w}^{2}}{4},\frac{m_{w}r_{w}^{2}}{2}), wheremwm_{w}is the mass of the RW andrwr_{w}is the radius of RW.
The total angular momentum of the four RWs projected into the body frame is obtained by summing the individual contributions, which establishes the final kinematic mapping𝐡𝐛RW\displaystyle\mbf{h}^{\text{RW}}_{b}=∑i=14𝐂𝐛𝐰𝐢​𝐉𝐰𝐢𝒲𝐢​𝐩​𝐂𝐛𝐰𝐢𝖳​𝝎𝐛𝐰𝐢​𝐛\displaystyle=\sum^{4}_{i=1}\mbf{C}_{bw_{i}}\mbf{J}_{w_{i}}^{\mathcal{W}_{i}p}\mbf{C}_{bw_{i}}^{\mathsf{T}}{\boldsymbol{\omega}}_{b}^{w_{i}b}=∑i=14𝐂𝐛𝐰𝐢​[𝟏𝟐𝟎𝟎𝟎𝟏𝟐𝟎𝟎𝟎𝟏]​𝐂𝐛𝐰𝐢𝖳​[sin⁡ϕ𝐢​cos⁡ψ𝐢sin⁡ϕ𝐢​sin⁡ψ𝐢cos⁡ϕ𝐢]​𝐡𝐢\displaystyle=\sum^{4}_{i=1}\mbf{C}_{bw_{i}}\begin{bmatrix}\frac{1}{2}&0&0\\
0&\frac{1}{2}&0\\
0&0&1\end{bmatrix}\mbf{C}_{bw_{i}}^{\mathsf{T}}\begin{bmatrix}\sin{\phi_{i}}\cos{\psi_{i}}\\
\sin{\phi_{i}}\sin{\psi_{i}}\\
\cos{\phi_{i}}\end{bmatrix}h_{i}=𝐌𝟑𝟒​𝐡𝟒RW,\displaystyle=\mbf{M}_{34}\mbf{h}^{\text{RW}}_{4},

wherehi=12​mw​rw2​γ˙ih_{i}=\frac{1}{2}m_{w}r_{w}^{2}\dot{\gamma}_{i}is the angular momentum of theii-th RW resolved in frameℱwi\mathcal{F}_{w_{i}}and𝐌𝟑𝟒=[𝐂𝐛𝐰𝟏​[𝟏𝟐𝟎𝟎𝟎𝟏𝟐𝟎𝟎𝟎𝟏]​𝐂𝐛𝐰𝟏𝖳​[sin⁡ϕ𝟏​cos⁡ψ𝟏sin⁡ϕ𝟏​sin⁡ψ𝟏cos⁡ϕ𝟏]⋯𝐂𝐛𝐰𝟒​[𝟏𝟐𝟎𝟎𝟎𝟏𝟐𝟎𝟎𝟎𝟏]​𝐂𝐛𝐰𝟒𝖳​[sin⁡ϕ𝟒​cos⁡ψ𝟒sin⁡ϕ𝟒​sin⁡ψ𝟒cos⁡ϕ𝟒]].\mbf{M}_{34}=\begin{bmatrix}\mbf{C}_{bw_{1}}\begin{bmatrix}\frac{1}{2}&0&0\\
0&\frac{1}{2}&0\\
0&0&1\end{bmatrix}\mbf{C}_{bw_{1}}^{\mathsf{T}}\begin{bmatrix}\sin{\phi_{1}}\cos{\psi_{1}}\\
\sin{\phi_{1}}\sin{\psi_{1}}\\
\cos{\phi_{1}}\end{bmatrix}&\cdots&\mbf{C}_{bw_{4}}\begin{bmatrix}\frac{1}{2}&0&0\\
0&\frac{1}{2}&0\\
0&0&1\end{bmatrix}\mbf{C}_{bw_{4}}^{\mathsf{T}}\begin{bmatrix}\sin{\phi_{4}}\cos{\psi_{4}}\\
\sin{\phi_{4}}\sin{\psi_{4}}\\
\cos{\phi_{4}}\end{bmatrix}\end{bmatrix}.

Substituting in the numerical parametersψi=60∘\psi_{i}=60^{\circ}for allii, andϕi=45∘+(i−1)⋅90∘\phi_{i}=45^{\circ}+(i-1)\cdot 90^{\circ},i=1,2,3,4i=1,2,3,4results in𝐌𝟑𝟒=[0.6124−0.6124−0.61240.61240.61240.6124−0.6124−0.61240.50.50.50.5].\mbf{M}_{34}=\begin{bmatrix}0.6124&-0.6124&-0.6124&0.6124\\
0.6124&0.6124&-0.6124&-0.6124\\
0.5&0.5&0.5&0.5\end{bmatrix}.(3)

## 2.3.3Unconstrained Minimum-Norm Allocation

The PID control law in Eq. (2) determines the desired angular momentum derivative in the body-frame𝐡˙b,desRW\dot{\mbf{h}}^{\text{RW}}_{b,\text{des}}, which then needs to be allocated to the momentum of the indivitual RWs within the 4-RW assembly. Since the mapping between𝐡𝐛RW\mbf{h}_{b}^{\text{RW}}and𝐡𝟒RW\mbf{h}^{\text{RW}}_{4}is under-determined (i.e., four variables are to be determined from three equations), the allocation problem is inherently non-unique.

The selection of an optimal allocation is typically a core redundancy and safety design choice within the attitude determination and control system (ADCS).
For the purpose of developing momentum management techniques in this paper, a computationally-efficient pseudo-inverse method is employed to define this allocation uniquely, where𝐡𝟒RW\displaystyle\mbf{h}^{\text{RW}}_{4}=𝐌34†​𝐡𝐛,desRW,\displaystyle=\mathbf{M}_{34}^{\dagger}\mbf{h}_{b,\text{des}}^{\text{RW}},(4)𝐡˙4RW\displaystyle\dot{\mbf{h}}^{\text{RW}}_{4}=𝐌𝟑𝟒†​𝐡˙𝐛,desRW,\displaystyle=\mbf{M}_{34}^{\dagger}\dot{\mbf{h}}_{b,\text{des}}^{\text{RW}},(5)

and𝐌𝟑𝟒†=𝐌𝟑𝟒𝖳​(𝐌𝟑𝟒​𝐌𝟑𝟒𝖳)−𝟏\mbf{M}_{34}^{\dagger}=\mbf{M}_{34}^{\mathsf{T}}\Big(\mbf{M}_{34}\mbf{M}_{34}^{\mathsf{T}}\Big)^{-1}.
This approach yields the minimum-norm pseudo-inverse result for𝐡𝟒RW\mbf{h}^{\text{RW}}_{4}and𝐡˙4RW\dot{\mbf{h}}^{\text{RW}}_{4}, characterized by the smallest possible Euclidean norm (‖𝐡𝟒RW‖𝟐||\mbf{h}^{\text{RW}}_{4}||_{2}and‖𝐡˙4RW‖2||\dot{\mbf{h}}^{\text{RW}}_{4}||_{2}) amongst all potential combinations that yield the desired values of𝐡𝐛,desRW\mbf{h}^{\text{RW}}_{b,\text{des}}and𝐡˙b,desRW\dot{\mbf{h}}^{\text{RW}}_{b,\text{des}}. In the absence of any RW saturation, Eq. (5) is used to compute𝐡˙4RW\dot{\mbf{h}}^{\text{RW}}_{4}.

## 2.3.4Constrained Minimum-Norm Allocation via Sequential Pseudo-Inverse

The standard pseudo-inverse solution from Eq. (4) may generate wheel momentum commands that exceed the physical saturation limit of one or more RWs (i.e.,‖𝐡𝟒RW‖∞>𝐡maxRW||\mbf{h}^{\text{RW}}_{4}||_{\infty}>h^{\text{RW}}_{\text{max}}, wherehmaxRWh^{\text{RW}}_{\text{max}}is the saturation limit).
A constraint-prioritized sequential allocation scheme is applied to manage the inherent redundancy while rigorously enforcing these physical saturation constraints. This scheme is designed to find a solution to the minimization of‖𝐡𝟒RW‖𝟐||\mbf{h}^{\text{RW}}_{4}||_{2}subject to the constraint‖𝐡𝟒RW‖∞≤𝐡maxRW||\mbf{h}^{\text{RW}}_{4}||_{\infty}\leq h^{\text{RW}}_{\text{max}}in a computationally-efficient manner. Although this could be posed as a QP, the relatively short time steps associated with attitude control necessitates a more computationally-efficient strategy. To meet this need, a suboptimal solution is found through the proposed method that operates by sequentially checking the maximum individual RW angular momentum, enforcing saturation limit, and redistributing angular momentum on unsaturated RWs to satisfy the desired RW attitude control torque.
The process is as follows:
- 1.

Unconstrained Initial Solution and Saturation Check:The process commences by calculating the unconstrained minimum-norm solution using the current body-frame angular momentum𝐡𝟒RW=𝐌𝟑𝟒†​𝐡𝐛RW\mbf{h}^{\text{RW}}_{4}=\mbf{M}_{34}^{\dagger}\mbf{h}_{b}^{\text{RW}}.
The resulting unconstrained 4-RW momentum is checked against the saturation limit, where‖𝐡𝟒RW‖∞≤𝐡maxRW||\mbf{h}^{\text{RW}}_{4}||_{\infty}\leq h^{\text{RW}}_{\text{max}}must be satisfied.
If‖𝐡𝟒RW‖∞≤𝐡maxRW||\mbf{h}^{\text{RW}}_{4}||_{\infty}\leq h^{\text{RW}}_{\text{max}}is satisfied (none of the RWs saturate), the mapping of the angular momentum derivative is𝐡˙4RW=𝐌𝟑𝟒†​𝐡˙𝐛,desRW\dot{\mbf{h}}^{\text{RW}}_{4}=\mbf{M}_{34}^{\dagger}\dot{\mbf{h}}_{b,\text{des}}^{\text{RW}}, the constrained minimum-norm allocation is determined, and the remaining steps can be skipped.
If‖𝐡𝟒RW‖∞>𝐡maxRW||\mbf{h}^{\text{RW}}_{4}||_{\infty}>h^{\text{RW}}_{\text{max}}(at least one of the RWs saturate), the process continues to Steps 2 through 4.
- 2.

Saturation Implementation:The component of𝐡𝟒RW\mbf{h}^{\text{RW}}_{4}with the largest magnitude exceeding the saturation limithmaxRWh^{\text{RW}}_{\text{max}}is identified. This is labeled as theii-th component of𝐡𝟒RW\mbf{h}^{\text{RW}}_{4}(i.e.,h4RW,(i)h^{\text{RW},(i)}_{4}), where|h4RW,(i)|=‖𝐡𝟒RW‖∞|h^{\text{RW},(i)}_{4}|=||\mbf{h}^{\text{RW}}_{4}||_{\infty}and|h4RW,(i)|>hmaxRW|h^{\text{RW},(i)}_{4}|>h^{\text{RW}}_{\text{max}}. Theii-th RW is now identified as saturated for all remaining iterations.
Then, its momentum is fixed at the saturation boundaryh4,satRW,(i)=±hmaxRWh^{\text{RW},(i)}_{4,\text{sat}}=\pm h^{\text{RW}}_{\text{max}}, where the sign of the momentumh4RW,(i)h^{\text{RW},(i)}_{4}is maintained.
Crucially, when a wheel’s angular momentum is saturated and fixed, its corresponding commanded angular momentum derivativeh˙4RW,(i)\dot{h}^{\text{RW},(i)}_{4}must simultaneously be set to zero to prevent the controller from commanding further change into the limit, i.e.,h˙4,satRW,(i)=0\dot{h}^{\text{RW},(i)}_{4,\text{sat}}=0.
- 3.

Residual Calculation and Redistribution:The momentum contribution from the saturated wheel(s) is calculated and subtracted from the original demanded body-frame angular momentum. This yields the residual momentum requirement for the remaining unsaturated wheels𝐡𝐛res=𝐡𝐛,desRW−𝐌𝟑𝟒sat​𝐡𝟒,satRW,\mbf{h}_{b}^{\text{res}}=\mbf{h}_{b,\text{des}}^{\text{RW}}-\mbf{M}_{34}^{\text{sat}}\mbf{h}^{\text{RW}}_{4,\text{sat}},

where𝐌34sat\mathbf{M}_{34}^{\text{sat}}is a modified version of the allocation matrix, where the columns corresponding to the unsaturated wheels are set to zero and𝐡𝟒,satRW∈ℝ𝟒\mbf{h}^{\text{RW}}_{4,\text{sat}}\in\mathbb{R}^{4}contains±hmaxRW\pm h^{\text{RW}}_{\text{max}}in the entries associated with saturated wheels and zeros in the other entries of the matrix.

The angular momentum of thennunsaturated wheels is then recalculated as𝐡𝐧,unsatRW=(𝐌𝟑×𝐧unsat)†​𝐡𝐛res,\mbf{h}^{\text{RW}}_{n,\text{unsat}}=\Big(\mbf{M}_{3\times n}^{\text{unsat}}\Big)^{\dagger}\mbf{h}_{b}^{\text{res}},(6)

where𝐌𝟑×𝐧unsat\mbf{M}_{3\times n}^{\text{unsat}}is a modified version of the allocation matrix𝐌𝟑𝟒\mbf{M}_{34}such that the columns associated with the saturated wheels are removed, reducing its dimension to3×n3\times n.
The allocation of the unsaturated wheels angular momentum rate is computed similarly as𝐡˙n,unsatRW=(𝐌𝟑×𝐧unsat)†​𝐡˙𝐛,desRW.\dot{\mbf{h}}^{\text{RW}}_{n,\text{unsat}}=\Big(\mbf{M}_{3\times n}^{\text{unsat}}\Big)^{\dagger}\dot{\mbf{h}}_{b,\text{des}}^{\text{RW}}.(7)
- 4.

Saturation Assessment:The results of Steps 2 and 3 are compiled to obtain updated values of𝐡𝟒RW\mbf{h}^{\text{RW}}_{4}and𝐡˙4RW\dot{\mbf{h}}^{\text{RW}}_{4}. The entries of𝐡𝟒RW\mbf{h}^{\text{RW}}_{4}associated with saturated wheels are set using the appropriate entries of𝐡𝟒,satRW\mbf{h}^{\text{RW}}_{4,\text{sat}}, while the unsaturated wheel values are found using the result from Eq. (6). The entries of𝐡˙4RW\dot{\mbf{h}}^{\text{RW}}_{4}associated with saturated wheels are set to zero, while the unsaturated wheel values are chosen using Eq. (7).

If‖𝐡𝟒RW‖∞≤𝐡maxRW||\mbf{h}^{\text{RW}}_{4}||_{\infty}\leq h^{\text{RW}}_{\text{max}}, then the allocation process is completed. Else, the process returns to Step 2.

Steps 2 through 4 of this process continue recursively until all components of the final wheel momentum𝐡𝟒RW\mbf{h}^{\text{RW}}_{4}are within±hmax\pm h_{\text{max}}.
Note that the initial pseudo-inverse solved in Step 1 determines an allocation with the smallest magnitude for the under-determined systems.
When 1 RW saturates (n=3n=3), the reduced mapping becomes an one-to-one inverse mapping, leading to a unique solution in the allocation of the unsaturated wheels.
When 2 or 3 RWs are identified as saturated (n∈{1,2}n\in\{1,2\}), the mapping becomes an over-determined system, and an exact solution does not exist. In this case, the allocations performed in Eqs. (6) and (7) of Step 3 become a least-squares problems. A direct consequence of this is that the rate of change of the angular momentum in the 4 RWs,𝐡˙4RW\dot{\mbf{h}}^{\text{RW}}_{4}, will not necessarily produce the desired value of𝐡˙b,desRW\dot{\mbf{h}}_{b,\text{des}}^{\text{RW}}from the attitude control in Eq. (2), and performance of the attitude controller may suffer.
When all RWs saturate, the 4-RW system can no longer provide any torque and attitude control is no longer possible.

## 2.4Momentum Management Control Actuation

The momentum management time step is chosen based on the AMT position command update period ofΔ​t=100\Delta t=100seconds used on NEA Scout(Orphee et al.,2018), which is much longer than the attitude control (or ADCS) time step that is assumed to be one second in this work.
Specifically, the AMT and RCD control inputs generated by the momentum management controller are updated at every 100-second momentum management time step, while the numerical simulation of the sailcraft’s nonlinear dynamics runs at a one-second resolution.

The AMT actuation input𝐮AMT\mbf{u}^{\text{AMT}}corresponds to the first two components of𝐫𝐛𝐩𝐬\mbf{r}^{ps}_{b}, where𝐮AMT=[𝐫𝐛𝟏AMT𝐫𝐛𝟐AMT]𝖳\mbf{u}^{\text{AMT}}=\begin{bmatrix}r^{\text{AMT}}_{b1}&r^{\text{AMT}}_{b2}\end{bmatrix}^{\mathsf{T}}.
At any given timetkt_{k}for momentum management update, the AMT actuation dynamics are modeled based on the current position𝐮AMT​(𝐭𝐤)\mbf{u}^{\text{AMT}}(t_{k})and the incoming momentum management command𝐮𝐤AMT\mbf{u}^{\text{AMT}}_{k}. Fortk≤t≤tk+Δ​tt_{k}\leq t\leq t_{k}+\Delta t, the system drives the AMT actuator along each axis (i=1,2i=1,2) at its maximum speed|u˙max,iAMT||\dot{u}^{\text{AMT}}_{\text{max},i}|toward the target commanduk,iAMTu^{\text{AMT}}_{k,i}. Once the commanded position is reached, the actuator stops and holds its position. These resulting transient position𝐫𝐛𝐩𝐬​(𝐭)\mbf{r}^{ps}_{b}(t)and velocity𝐫˙bp​s​(t)\dot{\mbf{r}}^{ps}_{b}(t)are then used in the numerical simulation for the nonlinear system dynamics in Eq. (1).

The layout of Solar Cruiser’s RCDs allows for an approximately pure on-off roll momentum management torque to be generated in either direction(Inness et al.,2023; Tyler et al.,2023; Heaton et al.,2023). Thus, the RCD torque is modeled as𝝉bRCD=[00τb​3RCD]𝖳{\boldsymbol{\tau}}_{b}^{\text{RCD}}=\begin{bmatrix}0&0&\tau^{\text{RCD}}_{b3}\end{bmatrix}^{\mathsf{T}}, whereτb​3RCD∈{−τb​3,onRCD,0,τb​3,onRCD}\tau^{\text{RCD}}_{b3}\in\{-\tau^{\text{RCD}}_{b3,\text{on}},0,\tau^{\text{RCD}}_{b3,\text{on}}\}.
The roll torque generated when the RCDs are turned on is set to meet the Solar Cruiser’s roll torque requirement of6.525×10−56.525\times 10^{-5}N⋅\cdotm at a17∘17^{\circ}sun incidence angle (SIA), which is1.51.5times the sum of worst case roll disturbance and AMT induced roll torque at its maximum position offset(Heaton et al.,2023; Johnson et al.,2022).
The RCD torque magnitude is modeled as a quadratic cosine function of SIA to match the analysis ofHeaton et al. (2023), and is defined asτb​3,onRCD=6.525×10−5cos2⁡(17∘)​cos2⁡(SIA).\tau^{\text{RCD}}_{b3,\text{on}}=\frac{6.525\times 10^{-5}}{\cos^{2}(17^{\circ})}\cos^{2}(\text{SIA}).(8)

The torque profile ofτb​3,onRCD\tau^{\text{RCD}}_{b3,\text{on}}as a function of SIA is presented in Fig.2for a range of0∘0^{\circ}to30∘30^{\circ}. This span covers roughly double the operational range of Solar Cruiser, which is designed to remain within an SIA of0∘0^{\circ}to17∘17^{\circ}(Tyler et al.,2023; Heaton et al.,2023).Figure 2:The RCD torque profile as functions of SIA.

## 2.5Linear Dynamics for Estimation and Prediction

For practical onboard implementation, a linear model is required for disturbance estimation and predictive control.
The accuracy of the model significantly affects the performance of the controller. However, higher model fidelity comes at the cost of increased computational demand. To enable real-time onboard implementation, a trade-off must be made between prediction accuracy and computational feasibility.
Although a nonlinear dynamics model would have higher fidelity, it is not practical to consider the implementation of nonlinear MPC onboard with current technology due to their excessive computation demand.
A discrete-time linear model is thus used to supplement onboard disturbance estimation and predictive control, specifically the process model in Kalman filter and the prediction model in MPC.

The nonlinear dynamics model is linearized about the current state and AMT position at every time step, with knowledge of the attitude-dependent SRP force and estimated disturbance torque.
This yields a continuous-time linear time-varying (LTV) model, where the states include the attitude, angular velocity, reaction wheel angular momentum, and an integral state from the integral term of the attitude controller.
The state of the linear system is denoted as𝐱=[𝜽𝖳𝝎𝐛𝐛𝐚𝖳𝐡𝐛RW𝖳𝐞int𝖳]𝖳\mbf{x}=\begin{bmatrix}{\boldsymbol{\theta}}^{\mathsf{T}}&{\boldsymbol{\omega}}^{ba^{\mathsf{T}}}_{b}&\mbf{h}^{\text{RW}^{\mathsf{T}}}_{b}&\mbf{e}^{\text{int}^{\mathsf{T}}}\end{bmatrix}^{\mathsf{T}}, where𝐞int=∫𝐭𝟎𝐭(𝜽​(τ)−𝜽𝐝​(τ))​d​τ\mbf{e}^{\text{int}}=\int^{t}_{t_{0}}\big({\boldsymbol{\theta}}(\tau)-{\boldsymbol{\theta}}_{d}(\tau)\big)\textrm{d}\tauis the internal state representing the integral term of PID law.
It is assumed that the SRP force𝐟¯bSRP\bar{\mbf{f}}_{b}^{\text{SRP}}is known through an estimate from the onboard ADCS.
External disturbances are represented by𝐰=𝝉𝐛dist\mbf{w}={\boldsymbol{\tau}}^{\text{dist}}_{b}, while𝐮AMT\mbf{u}^{\text{AMT}}anduRCD{u}^{\text{RCD}}denote the AMT position and RCD torque input, respectively.
In order to perform time-varying trajectory tracking of𝜽d{\boldsymbol{\theta}}_{d}and𝝎d{\boldsymbol{\omega}}_{d}, the system is linearized about the operation point of the desired trajectory with the current angular momentum and integral state𝐱¯=[𝜽d𝖳​𝝎d𝖳​𝐡¯bRW𝖳​𝐞¯int𝖳]𝖳\bar{\mbf{x}}=\Big[{\boldsymbol{\theta}}_{d}^{\mathsf{T}}\,\,\,{\boldsymbol{\omega}}_{d}^{{\mathsf{T}}}\,\,\,\bar{\mbf{h}}^{\text{RW}^{\mathsf{T}}}_{b}\,\,\,{\bar{\mbf{e}}}^{\text{int}^{\mathsf{T}}}\Big]^{\mathsf{T}}, the current AMT position𝐫¯bp​s{\bar{\mbf{r}}}^{ps}_{b}, a nominally-off RCD torque𝝉¯bRCD=𝟎\bar{{\boldsymbol{\tau}}}^{\text{RCD}}_{b}=\mbf{0}, and the current SRP force𝐟¯bSRP\bar{\mbf{f}}_{b}^{\text{SRP}}, which are chosen as the current values when performing the linearization. Since future AMT positions are not known in advance, their rates are assumed to be zero in the linearization, i.e.,𝐫¯˙bp​s=𝟎\dot{\bar{\mbf{r}}}_{b}^{ps}=\mbf{0},𝐫¯¨bp​s=𝟎\ddot{\bar{\mbf{r}}}_{b}^{ps}=\mbf{0}.
The linearized continuous-time dynamics retaining the first-order term of Taylor series expansion is derived as𝐱˙=𝐀𝐱+𝐁𝐰​𝐰+𝐁𝐮𝟏​𝐮AMT+𝐁𝐮𝟐​𝐮RCD+𝐳,\dot{\mbf{x}}=\mbf{A}\mbf{x}+\mbf{B}_{w}\mbf{w}+\mbf{B}_{u1}\mbf{u}^{\text{AMT}}+\mbf{B}_{u2}u^{\text{RCD}}+\mbf{z},(9)

where𝐀=𝐀​(𝐱¯,𝐫¯𝐛𝐩𝐬)=[𝟎𝟑×𝟑𝟏𝟑×𝟑𝟎𝟑×𝟑𝟎𝟑×𝟑−𝐉¯𝐛ℬ​𝐜−𝟏​𝐊𝐩∂𝐟𝟐∂𝝎𝐛𝐛𝐚|𝐱¯,𝐫¯𝐛𝐩𝐬−𝐉¯𝐛ℬ​𝐜−𝟏​𝝎¯𝐛𝐛𝐚×−𝐉¯𝐛ℬ​𝐜−𝟏​𝐊𝐢𝐊𝐩𝐊𝐝𝟎𝟑×𝟑𝐊𝐢𝟏𝟑×𝟑𝟎𝟑×𝟑𝟎𝟑×𝟑𝟎𝟑×𝟑],\mbf{A}=\mbf{A}(\bar{\mbf{x}},{\bar{\mbf{r}}}^{ps}_{b})=\begin{bmatrix}\mbf{0}_{3\times 3}&\mbf{1}_{3\times 3}&\mbf{0}_{3\times 3}&\mbf{0}_{3\times 3}\\
-{\bar{\mbf{J}}}_{b}^{\mathcal{B}c^{-1}}\mbf{K}_{p}&\frac{\partial\mbf{f}_{2}}{\partial{\boldsymbol{\omega}}_{b}^{ba}}\Bigg|_{\bar{\mbf{x}},{\bar{\mbf{r}}}^{ps}_{b}}&-{\bar{\mbf{J}}}_{b}^{\mathcal{B}c^{-1}}\bar{{\boldsymbol{\omega}}}_{b}^{ba^{\times}}&-{\bar{\mbf{J}}}_{b}^{\mathcal{B}c^{-1}}\mbf{K}_{i}\\
\mbf{K}_{p}&\mbf{K}_{d}&\mbf{0}_{3\times 3}&\mbf{K}_{i}\\
\mbf{1}_{3\times 3}&\mbf{0}_{3\times 3}&\mbf{0}_{3\times 3}&\mbf{0}_{3\times 3}\end{bmatrix},𝐁𝐰=𝐁𝐰​(𝐫¯𝐛𝐩𝐬)=[𝟎𝟑×𝟑𝐉¯𝐛ℬ​𝐜−𝟏𝟎𝟑×𝟑𝟎𝟑×𝟑],𝐁𝐮𝟏=𝐁𝐮𝟏​(𝐱¯,𝐫¯𝐛𝐩𝐬,𝐟¯𝐛SRP)=[𝟎𝟑×𝟐∂𝐟𝟐∂𝐫𝐛𝐩𝐬|𝐱¯,𝐫¯𝐛𝐩𝐬,𝐟¯𝐛SRP​[𝟏𝟐×𝟐𝟎𝟏×𝟐]𝟎𝟑×𝟐𝟎𝟑×𝟐],𝐁𝐮𝟐=𝐁𝐮𝟐​(𝐫¯𝐛𝐩𝐬)=[𝟎𝟑×𝟑𝐉¯𝐛ℬ​𝐜−𝟏𝟎𝟑×𝟑𝟎𝟑×𝟑]​[𝟎𝟎𝟏],\mbf{B}_{w}=\mbf{B}_{w}({\bar{\mbf{r}}}^{ps}_{b})=\begin{bmatrix}\mbf{0}_{3\times 3}\\
{\bar{\mbf{J}}}_{b}^{\mathcal{B}c^{-1}}\\
\mbf{0}_{3\times 3}\\
\mbf{0}_{3\times 3}\end{bmatrix},\hskip 11.49994pt\mbf{B}_{u1}=\mbf{B}_{u1}(\bar{\mbf{x}},{\bar{\mbf{r}}}^{ps}_{b},{\bar{\mbf{f}}}_{b}^{\text{SRP}})=\begin{bmatrix}\mbf{0}_{3\times 2}\\
\frac{\partial\mbf{f}_{2}}{\partial\mbf{r}_{b}^{ps}}\Bigg|_{\bar{\mbf{x}},{\bar{\mbf{r}}}^{ps}_{b},{\bar{\mbf{f}}}_{b}^{\text{SRP}}}\begin{bmatrix}\mbf{1}_{2\times 2}\\
\mbf{0}_{1\times 2}\end{bmatrix}\\
\mbf{0}_{3\times 2}\\
\mbf{0}_{3\times 2}\end{bmatrix},\hskip 11.49994pt\mbf{B}_{u2}=\mbf{B}_{u2}({\bar{\mbf{r}}}^{ps}_{b})=\begin{bmatrix}\mbf{0}_{3\times 3}\\
{\bar{\mbf{J}}}_{b}^{\mathcal{B}c^{-1}}\\
\mbf{0}_{3\times 3}\\
\mbf{0}_{3\times 3}\end{bmatrix}\begin{bmatrix}0\\
0\\
1\end{bmatrix},𝐳=𝐳​(𝐱¯,𝐫¯𝐛𝐩𝐬,𝝉¯𝐛dist,𝐟¯𝐛SRP,𝝉¯𝐛dist)=𝐟​(𝐱¯,𝐫¯𝐛𝐩𝐬,𝝉¯𝐛RCD,𝐟¯𝐛SRP,𝝉¯𝐛dist)−𝐀​𝐱¯−𝐁𝐰​𝝉¯𝐛dist−𝐁𝐮𝟏​𝐫¯𝐛𝐩𝐬,\mbf{z}=\mbf{z}(\bar{\mbf{x}},{\bar{\mbf{r}}}^{ps}_{b},\bar{{\boldsymbol{\tau}}}^{\text{dist}}_{b},{\bar{\mbf{f}}}_{b}^{\text{SRP}},\bar{{\boldsymbol{\tau}}}_{b}^{\text{dist}})=\mbf{f}(\bar{\mbf{x}},{\bar{\mbf{r}}}^{ps}_{b},\bar{{\boldsymbol{\tau}}}^{\text{RCD}}_{b},{\bar{\mbf{f}}}_{b}^{\text{SRP}},\bar{{\boldsymbol{\tau}}}_{b}^{\text{dist}})-\mbf{A}\bar{\mbf{x}}-\mbf{B}_{w}\bar{{\boldsymbol{\tau}}}^{\text{dist}}_{b}-\mbf{B}_{u1}{\bar{\mbf{r}}}^{ps}_{b},

and∂𝐟𝟐∂𝝎bb​a|𝐱¯,𝐫¯bp​s=𝐉¯bℬ​c−1​((𝐉¯bℬ​c​𝝎¯bb​a)×−𝝎¯bb​a×​𝐉¯bℬ​c+𝐡¯bRW×−𝐊𝐝),\displaystyle\frac{\partial\mbf{f}_{2}}{\partial{\boldsymbol{\omega}}_{b}^{ba}}\Big|_{\bar{\mbf{x}},{\bar{\mbf{r}}}^{ps}_{b}}={\bar{\mbf{J}}}_{b}^{\mathcal{B}c^{-1}}\Big(\big({\bar{\mbf{J}}}_{b}^{\mathcal{B}c}\bar{{\boldsymbol{\omega}}}_{b}^{ba}\big)^{\times}-\bar{{\boldsymbol{\omega}}}_{b}^{ba^{\times}}{\bar{\mbf{J}}}_{b}^{\mathcal{B}c}+{\bar{\mbf{h}}}^{\text{RW}^{\times}}_{b}-\mbf{K}_{d}\Big),∂𝐟𝟐∂𝐫𝐛𝐩𝐬|𝐱¯,𝐫¯bp​s,𝐟¯bSRP,𝝉¯bdist=𝐉¯bℬ​c−1​(−mp3+ms3(mp+ms)2​𝝎¯bb​a×​(𝐫¯bp​s×​𝝎¯bb​a×+(𝐫¯bp​s×​𝝎¯bb​a)×)−mp3+ms3(mp+ms)2​(𝐫¯bp​s×​𝝎¯˙bb​a×+(𝐫¯bp​s×​𝝎¯˙bb​a)×)−msmp+ms​𝐟¯bSRP×).\displaystyle\frac{\partial\mbf{f}_{2}}{\partial\mbf{r}_{b}^{ps}}\Big|_{\bar{\mbf{x}},{\bar{\mbf{r}}}^{ps}_{b},{\bar{\mbf{f}}}_{b}^{\text{SRP}},\bar{{\boldsymbol{\tau}}}_{b}^{\text{dist}}}={\bar{\mbf{J}}}_{b}^{\mathcal{B}c^{-1}}\Big(-\frac{m_{p}^{3}+m_{s}^{3}}{(m_{p}+m_{s})^{2}}{\bar{\boldsymbol{\omega}}}_{b}^{ba^{\times}}\Big({\bar{\mbf{r}}}^{ps^{\times}}_{b}{\bar{\boldsymbol{\omega}}}_{b}^{ba^{\times}}+\big({\bar{\mbf{r}}}^{ps^{\times}}_{b}{\bar{\boldsymbol{\omega}}}_{b}^{ba}\big)^{\times}\Big)-\frac{m_{p}^{3}+m_{s}^{3}}{(m_{p}+m_{s})^{2}}\Big({\bar{\mbf{r}}}^{ps^{\times}}_{b}\dot{{\bar{\boldsymbol{\omega}}}}_{b}^{ba^{\times}}+\big({\bar{\mbf{r}}}^{ps^{\times}}_{b}\dot{{\bar{\boldsymbol{\omega}}}}_{b}^{ba}\big)^{\times}\Big)-\frac{m_{s}}{m_{p}+m_{s}}{\bar{\mbf{f}}}_{b}^{\text{SRP}^{\times}}\Big).

Note that the state-space matrices depend on𝐫¯bp​s{\bar{\mbf{r}}}^{ps}_{b}because𝐉𝐛ℬ​𝐜\mbf{J}_{b}^{\mathcal{B}c}is a function of𝐫𝐛𝐩𝐬\mbf{r}^{ps}_{b}. The nonlinear function is defined as𝐟​(𝐱¯,𝐫¯𝐛𝐩𝐬,𝝉¯𝐛RCD,𝐟¯𝐛SRP,𝝉¯𝐛dist)=[𝐒−𝟏​(𝜽𝐝)𝐟𝟐​(𝐱¯,𝐫¯𝐛𝐩𝐬,𝝉¯𝐛RCD,𝐟¯𝐛SRP,𝝉¯𝐛dist)𝐊𝐢​𝐞¯int𝟎],\mbf{f}(\bar{\mbf{x}},{\bar{\mbf{r}}}^{ps}_{b},\bar{{\boldsymbol{\tau}}}^{\text{RCD}}_{b},{\bar{\mbf{f}}}_{b}^{\text{SRP}},\bar{{\boldsymbol{\tau}}}_{b}^{\text{dist}})=\begin{bmatrix}\mbf{S}^{-1}({\boldsymbol{\theta}}_{d})\\
\mbf{f}_{2}(\bar{\mbf{x}},{\bar{\mbf{r}}}^{ps}_{b},\bar{{\boldsymbol{\tau}}}^{\text{RCD}}_{b},{\bar{\mbf{f}}}_{b}^{\text{SRP}},\bar{{\boldsymbol{\tau}}}_{b}^{\text{dist}})\\
\mbf{K}_{i}\bar{\mbf{e}}^{\text{int}}\\
\mbf{0}\end{bmatrix},

where𝐟𝟐=𝝎˙𝐛𝐛𝐚=𝐉𝐛ℬ​𝐜−𝟏(\displaystyle\mbf{f}_{2}=\dot{{\boldsymbol{\omega}}}_{b}^{ba}=\mbf{J}_{b}^{{\mathcal{B}c}^{-1}}\Bigg(−𝝎bb​a×​𝐉𝐛ℬ​𝐜​𝝎𝐛𝐛𝐚−𝝎𝐛𝐛𝐚×​𝐡𝐛RW−𝐦𝐩𝟑+𝐦𝐬𝟑(𝐦𝐩+𝐦𝐬)𝟐​(𝐫𝐛𝐩𝐬×​𝐫¨𝐛𝐩𝐬−𝟐​𝐫˙𝐛𝐩𝐬×​𝐫𝐛𝐩𝐬×​𝝎𝐛𝐛𝐚)\displaystyle-{\boldsymbol{\omega}}_{b}^{ba^{\times}}\mbf{J}_{b}^{\mathcal{B}c}{\boldsymbol{\omega}}_{b}^{ba}-{\boldsymbol{\omega}}_{b}^{ba^{\times}}\mbf{h}_{b}^{\text{RW}}-\frac{m_{p}^{3}+m_{s}^{3}}{(m_{p}+m_{s})^{2}}\bigg(\mbf{r}_{b}^{ps^{\times}}\ddot{\mbf{r}}_{b}^{ps}-2\dot{\mbf{r}}_{b}^{ps^{\times}}\mbf{r}_{b}^{ps^{\times}}{\boldsymbol{\omega}}_{b}^{ba}\bigg)+msmp+ms𝐫𝐛𝐩𝐬×𝐟𝐛SRP+𝝉𝐛RCD+𝝉𝐛dist−𝐊𝐩(𝜽−𝜽𝐝)−𝐊𝐝(𝝎𝐛𝐛𝐚−𝝎𝐝)−𝐊𝐢∫𝐭𝟎𝐭(𝜽(τ)−𝜽𝐝(τ))dτ)\displaystyle+\frac{m_{s}}{m_{p}+m_{s}}\mbf{r}_{b}^{ps^{\times}}\mbf{f}_{b}^{\text{SRP}}+{\boldsymbol{\tau}}_{b}^{\text{RCD}}+{\boldsymbol{\tau}}_{b}^{\text{dist}}-\mbf{K}_{p}({\boldsymbol{\theta}}-{\boldsymbol{\theta}}_{d})-\mbf{K}_{d}({\boldsymbol{\omega}}^{ba}_{b}-{\boldsymbol{\omega}}_{d})-\mbf{K}_{i}\int^{t}_{t_{0}}\bigg({\boldsymbol{\theta}}(\tau)-{\boldsymbol{\theta}}_{d}(\tau)\bigg)\textrm{d}\tau\Bigg)

is a combination of the attitude dynamics in Eq. (1) and the RW control law in Eq. (2) that characterize𝝎˙bb​a\dot{{\boldsymbol{\omega}}}_{b}^{ba}.

In this work, a zeroth-order hold (ZOH) discretization on both AMT and RCD actuation is used, which has a lower computation requirement when compared to the mixed-FOH-ZOH discretization employed byShen and Caverly (2025).
Discretizing Eq. (9) using a ZOH with the momentum management timestepΔ​t\Delta tresults in𝐱𝐤=𝐀𝐤​𝐱𝐤+𝐁𝐰,𝐤​𝐰𝐤+𝐁𝐮𝟏,𝐤​𝐮𝐤AMT+𝐁𝐮𝟐,𝐤​𝐮𝐤RCD+𝐳𝐤,\mbf{x}_{k}=\mbf{A}_{k}\mbf{x}_{k}+\mbf{B}_{w,k}\mbf{w}_{k}+\mbf{B}_{u1,k}\mbf{u}^{\text{AMT}}_{k}+\mbf{B}_{u2,k}{u}^{\text{RCD}}_{k}+\mbf{z}_{k},(10)

which is used as the the Kalman filter process model and MPC prediction model.
The discrete-time LTV state-space matrices are obtained by solving𝐀𝐤=𝚽​(𝐭𝐤+𝟏,𝐭𝐤)\mbf{A}_{k}={\boldsymbol{\Phi}}(t_{k+1},t_{k}),[𝐁𝐰,𝐤𝐁𝐮𝟏,𝐤𝐁𝐮𝟐,𝐤]=𝐀𝐤​𝐁~𝐤\begin{bmatrix}\mbf{B}_{w,k}&\mbf{B}_{u1,k}&\mbf{B}_{u2,k}\end{bmatrix}=\mbf{A}_{k}\tilde{\mbf{B}}_{k}, and𝐳𝐤=𝐀𝐤​𝐳~𝐤\mbf{z}_{k}=\mbf{A}_{k}\tilde{\mbf{z}}_{k}through numerical integration of the matrix differential equations𝚽˙​(t,tk)=𝐀​𝚽​(𝐭,𝐭𝐤),\displaystyle\dot{{\boldsymbol{\Phi}}}(t,t_{k})=\mbf{A}{\boldsymbol{\Phi}}(t,t_{k}),𝐁~˙k​(t,tk)=𝚽−1​(t,tk)​[𝐁𝐰𝐁𝐮𝟏𝐁𝐮𝟐],\displaystyle\dot{\tilde{\mbf{B}}}_{k}(t,t_{k})={\boldsymbol{\Phi}}^{-1}(t,t_{k})\begin{bmatrix}\mbf{B}_{w}&\mbf{B}_{u1}&\mbf{B}_{u2}\end{bmatrix},𝐳~˙k​(t,tk)=𝚽−1​(t,tk)​𝐳,\displaystyle\dot{\tilde{\mbf{z}}}_{k}(t,t_{k})={\boldsymbol{\Phi}}^{-1}(t,t_{k})\mbf{z},

with the initial values𝚽​(tk+1,tk)=𝟏{\boldsymbol{\Phi}}(t_{k+1},t_{k})=\mbf{1},𝐁~k​(tk)=𝟎\tilde{\mbf{B}}_{k}(t_{k})=\mbf{0},𝐳~k​(tk)=𝟎\tilde{\mbf{z}}_{k}(t_{k})=\mbf{0}over the time intervalt∈[tk,tk+1]t\in[t_{k},t_{k+1}].
Note that the nonlinear dynamics in Eq. (1) are used as the system’s dynamics for all numerical simulations, while the Kalman filter and MPC use the discrete-time LTV model.
Section3presents a state and disturbance estimation framework based on a Kalman filter that is used to yield the estimates𝐱^​(tk)\hat{\mbf{x}}(t_{k})and𝐰^​(tk)\hat{\mbf{w}}(t_{k})needed to compute the LTV dynamics model used in MPC.

## 3Disturbance Estimation Using Kalman Filter

Given NASA’s efforts to develop on-orbit SRP calibration algorithms(Carzana et al.,2023), it is reasonable to assume that an accurate SRP force estimate is available within the proposed momentum management algorithm. However, the SRP disturbance torque cannot be measured directly, and needs to be estimated onboard in real time. The disturbance torque𝝉bdist{\boldsymbol{\tau}}^{\text{dist}}_{b}is an external input acting on the solar sail system that impacts its dynamics.
In the MPC policy proposed in Section4, this disturbance torque is a key parameter in the prediction model used to forecast the system dynamics and determine optimal momentum management actuation.
Due to the slow motion and relatively steady attitude operation nature of solar sails, the disturbance torque is modeled as approximately constant or slow varying.
A Kalman filter framework is developed in this section to supplement this essential parameter for MPC momentum management.

## 3.1Measurement Model

Solar Cruiser’s ADCS provides an accurate estimate of the sailcraft’s attitude, angular velocity, and angular momentum using onboard sensors such as rate gyros, inertial measurement units (IMUs), sun sensors, and star trackers.
It is thus assumed in this work that a full state measurement of𝐱𝐤=[𝜽𝐤𝖳𝝎𝐛,𝐤𝐛𝐚𝖳𝐡𝐛,𝐤RW𝖳𝐞𝐤int𝖳]𝖳\mbf{x}_{k}=\begin{bmatrix}{\boldsymbol{\theta}}^{\mathsf{T}}_{k}&{\boldsymbol{\omega}}^{ba^{\mathsf{T}}}_{b,k}&\mbf{h}^{\text{RW}^{\mathsf{T}}}_{b,k}&\mbf{e}^{\text{int}^{\mathsf{T}}}_{k}\end{bmatrix}^{\mathsf{T}}is accessible, and the measurement noise is normally distributed, resulting in the measurement model𝐲𝐤=[𝟏𝟏𝟐×𝟏𝟐𝟎𝟏𝟐×𝟑]⏟𝐇​[𝐱𝐤𝐰𝐤]+𝝂𝐤,𝝂𝐤∼𝒩​(𝟎,𝐑KF),\mbf{y}_{k}=\underbrace{\begin{bmatrix}\mbf{1}_{12\times 12}&\mbf{0}_{12\times 3}\end{bmatrix}}_{\mbf{H}}\begin{bmatrix}\mbf{x}_{k}\\
\mbf{w}_{k}\end{bmatrix}+{\boldsymbol{\nu}}_{k},\qquad{\boldsymbol{\nu}}_{k}\sim\mathcal{N}(\mbf{0},\mbf{R}^{\text{KF}}),

where𝝂k{\boldsymbol{\nu}}_{k}is the linear additive measurement noise, and the measurement error covariance matrix𝐑KF=diag​(𝐫θ,𝐫ω,𝐫𝐡,𝐫𝐞)\mbf{R}^{\text{KF}}=\text{diag}(\mbf{r}_{\theta},\mbf{r}_{\omega},\mbf{r}_{h},\mbf{r}_{e})is determined by the variance of each corresponding state measurement error (𝝈θ2,𝝈ω2,𝝈h2,𝝈e2{\boldsymbol{\sigma}}_{\theta}^{2},{\boldsymbol{\sigma}}_{\omega}^{2},{\boldsymbol{\sigma}}_{h}^{2},{\boldsymbol{\sigma}}_{e}^{2}), which is associated with the onboard ADCS state estimation accuracy.

## 3.2Process Model

Given the slow evolution of the spacecraft attitude, it is assumed that SRP force𝐟¯bSRP{\bar{\mbf{f}}}_{b}^{\text{SRP}}is a known constant updated at every time step, the error of the dynamics model is Gaussian and linearly additive, and the disturbance torque to be estimated,𝝉bdist{\boldsymbol{\tau}}_{b}^{\text{dist}}, is constant within the time update (prediction) step.
The discrete-time LTV model in Eq. (10) with the addition of linear model error is given by𝐱𝐤+𝟏KF\displaystyle\mbf{x}^{\text{KF}}_{k+1}=𝐀𝐤​𝐱𝐤KF+𝐁𝐰,𝐤​𝐰𝐤KF+𝐁𝐮𝟏,𝐤​𝐮𝐤AMT+𝐁𝐮𝟐,𝐤​𝐮𝐤RCD+𝐳𝐤+𝜼𝐤model,𝜼𝐤model∼𝒩​(𝟎,𝐐modelKF),\displaystyle=\mbf{A}_{k}\mbf{x}^{\text{KF}}_{k}+\mbf{B}_{w,k}\mbf{w}^{\text{KF}}_{k}+\mbf{B}_{u1,k}\mbf{u}^{\text{AMT}}_{k}+\mbf{B}_{u2,k}{u}^{\text{RCD}}_{k}+\mbf{z}_{k}+{\boldsymbol{\eta}}^{\text{model}}_{k},\qquad{\boldsymbol{\eta}}^{\text{model}}_{k}\sim\mathcal{N}(\mbf{0},\mbf{Q}^{\text{KF}}_{\text{model}}),𝐰𝐤+𝟏KF\displaystyle\mbf{w}^{\text{KF}}_{k+1}=𝐰𝐤KF+𝜼𝐤dist,𝜼𝐤dist∼𝒩​(𝟎,𝐐distKF),\displaystyle=\mbf{w}^{\text{KF}}_{k}+{\boldsymbol{\eta}}^{\text{dist}}_{k},\qquad{\boldsymbol{\eta}}^{\text{dist}}_{k}\sim\mathcal{N}(\mbf{0},\mbf{Q}^{\text{KF}}_{\text{dist}}),

where the linear model error𝜼kmodel{\boldsymbol{\eta}}^{\text{model}}_{k}and disturbance error𝜼kdist{\boldsymbol{\eta}}^{\text{dist}}_{k}are assumed to be linearly additive and normally distributed.
The error covariance matrices of the model uncertainty are𝐐modelKF=diag​(𝐪θ,𝐪ω,𝐪𝐡,𝐪𝐞)\mbf{Q}^{\text{KF}}_{\text{model}}=\text{diag}(\mbf{q}_{\theta},\mbf{q}_{\omega},\mbf{q}_{h},\mbf{q}_{e})and𝐐distKF\mbf{Q}^{\text{KF}}_{\text{dist}}, which are tuning parameters chosen to influence the Kalman filter’s aggressiveness in updating the estimate of the disturbance torque𝐰KF\mbf{w}^{\text{KF}}. In particular, increasing the variances within𝐐modelKF\mbf{Q}^{\text{KF}}_{\text{model}}results in a slower convergence of the disturbance torque, while increase the variances within𝐐distKF\mbf{Q}^{\text{KF}}_{\text{dist}}speeds up the convergence, while potentially making the estimates more sensitive to measurement noise.
In order to adapt to the attitude-dependent disturbance torque varying with the slew maneuver, a dynamic error covariance scaling quadratically with the desired angular velocity is added to the disturbance covariance matrix, such that𝐐distKF=diag​(𝐪τ,𝟏+ξ𝟏​ω𝐝,𝟏𝟐,𝐪τ,𝟐+ξ𝟐​ω𝐝,𝟐𝟐,𝐪τ,𝟑+ξ𝟑​ω𝐝,𝟑𝟐)\mbf{Q}^{\text{KF}}_{\text{dist}}=\text{diag}({q}_{\tau,1}+\xi_{1}\omega_{d,1}^{2},{q}_{\tau,2}+\xi_{2}\omega_{d,2}^{2},{q}_{\tau,3}+\xi_{3}\omega_{d,3}^{2}), andξi\xi_{i}is the scaling parameter associate to the dynamic covariance fori=1,2,3i=1,2,3.

The complete Kalman filter process model is reformulated as[𝐱^k+1−𝐰^k+1−]⏟𝐗^k+1−=[𝐀𝐤𝐁𝐰,𝐤𝟎𝟑×𝟏𝟐𝟏𝟑×𝟑]⏟𝐅𝐤​[𝐱^k+𝐰^k+]⏟𝐗^k++[𝐁𝐮,𝐤𝟎𝟑×𝟑]⏟𝐆𝐤​[𝐮𝐤AMTukRCD]⏟𝐔𝐤+[𝐳𝐤𝟎]⏟𝐙𝐤+[𝜼kmodel𝜼kdist]⏟𝜼k,\underbrace{\begin{bmatrix}\hat{\mbf{x}}^{-}_{k+1}\\
\hat{\mbf{w}}^{-}_{k+1}\end{bmatrix}}_{\hat{\mbf{X}}^{-}_{k+1}}=\underbrace{\begin{bmatrix}\mbf{A}_{k}&\mbf{B}_{w,k}\\
\mbf{0}_{3\times 12}&\mbf{1}_{3\times 3}\end{bmatrix}}_{\mbf{F}_{k}}\underbrace{\begin{bmatrix}\hat{\mbf{x}}^{+}_{k}\\
\hat{\mbf{w}}^{+}_{k}\end{bmatrix}}_{\hat{\mbf{X}}^{+}_{k}}+\underbrace{\begin{bmatrix}\mbf{B}_{u,k}\\
\mbf{0}_{3\times 3}\end{bmatrix}}_{\mbf{G}_{k}}\underbrace{\begin{bmatrix}\mbf{u}^{\text{AMT}}_{k}\\
{u}^{\text{RCD}}_{k}\end{bmatrix}}_{\mbf{U}_{k}}+\underbrace{\begin{bmatrix}\mbf{z}_{k}\\
\mbf{0}\end{bmatrix}}_{\mbf{Z}_{k}}+\underbrace{\begin{bmatrix}{\boldsymbol{\eta}}^{\text{model}}_{k}\\
{\boldsymbol{\eta}}^{\text{dist}}_{k}\end{bmatrix}}_{{\boldsymbol{\eta}}_{k}},

where the process noise is given by𝜼k∼𝒩​(𝟎,𝐐KF){\boldsymbol{\eta}}_{k}\sim\mathcal{N}(\mbf{0},\mbf{Q}^{\text{KF}})and𝐐KF=diag​(𝐐modelKF,𝐐distKF)\mbf{Q}^{\text{KF}}=\text{diag}(\mbf{Q}^{\text{KF}}_{\text{model}},\mbf{Q}^{\text{KF}}_{\text{dist}}).

## 3.3Summary of Kalman Filter Estimation Framework

In the time update (prediction) step, the a priori (predicted) state estimate and error covariance are given by𝐗^k−\displaystyle\hat{\mbf{X}}_{k}^{-}=𝐅𝐤−𝟏​𝐗^𝐤−𝟏++𝐆𝐤−𝟏​𝐔𝐤−𝟏+𝐙𝐤−𝟏,\displaystyle=\mbf{F}_{k-1}\hat{\mbf{X}}_{k-1}^{+}+\mbf{G}_{k-1}\mbf{U}_{k-1}+\mbf{Z}_{k-1},𝐏𝐤−\displaystyle\mbf{P}_{k}^{-}=𝐅𝐤−𝟏​𝐏𝐤−𝟏+​𝐅𝐤−𝟏𝖳+𝐐KF.\displaystyle=\mbf{F}_{k-1}\mbf{P}_{k-1}^{+}\mbf{F}_{k-1}^{\mathsf{T}}+\mbf{Q}^{\text{KF}}.

In the measurement update (correction) step, the a posteriori (updated) state estimate and error covariance are given by𝐗^k+\displaystyle\hat{\mbf{X}}_{k}^{+}=𝐗^k−+𝐊𝐤​(𝐲𝐤−𝐇​𝐗^𝐤−),\displaystyle=\hat{\mbf{X}}_{k}^{-}+\mbf{K}_{k}\left(\mbf{y}_{k}-\mbf{H}\hat{\mbf{X}}_{k}^{-}\right),𝐏𝐤+\displaystyle\mbf{P}_{k}^{+}=(𝟏−𝐊𝐤​𝐇)​𝐏𝐤−,\displaystyle=\left(\mbf{1}-\mbf{K}_{k}\mbf{H}\right)\mbf{P}_{k}^{-},

where the Kalman gain is computed as𝐊𝐤=𝐏𝐤−​𝐇𝖳​(𝐇𝐏𝐤−​𝐇𝖳+𝐑KF)−𝟏.\mbf{K}_{k}=\mbf{P}_{k}^{-}\mbf{H}^{\mathsf{T}}\left(\mbf{H}\mbf{P}_{k}^{-}\mbf{H}^{\mathsf{T}}+\mbf{R}^{\text{KF}}\right)^{-1}.The state estimate𝐗^k+=[𝐱^k+𝖳𝐰^k+𝖳]𝖳\hat{\mbf{X}}_{k}^{+}=\begin{bmatrix}\hat{\mbf{x}}^{+^{\mathsf{T}}}_{k}&\hat{\mbf{w}}^{+^{\mathsf{T}}}_{k}\end{bmatrix}^{\mathsf{T}}is used within the momentum management controller presented in the following section.

## 4Momentum Management Using MPC

Solar sail slew maneuvers are inherently slow due to the small magnitude of SRP torques and the sailcraft’s large moment of inertia. As a result, the system dynamics are relatively smooth and predictable, and external disturbances such as SRP imbalance or environmental torques evolve gradually. Moreover, the long time scales involved in solar sail maneuvers provide sufficient computational time for onboard optimization. These characteristics make MPC particularly suitable for solar sail momentum management, where coordinated use of RWs and momentum management actuators (AMT and RCDs) is required to prevent RW saturation while maintaining accurate attitude control. This section presents the MPC framework tailored for solar sail momentum management, specifically designed for Solar Cruiser’s configuration.

## 4.1Introduction to MPC

MPC is an advanced optimal control strategy that computes control actions by solving a constrained optimization problem over a finite prediction horizon at each time step. It determines a sequence of control inputs that minimize a specified objective function while satisfying the system dynamics, actuator limits, and state constraints.
At each control update, MPC uses the current system state and a predictive model to forecast future behavior over a finite horizon ofNNtime steps. It then solves for the optimal sequence of control inputs, yet only the first input is applied to the system. At the next time step, the process is repeated using updated measurements and system information. This receding-horizon strategy enables continual adaptation to disturbances and modeling inaccuracies, providing robust feedback control in the presence of uncertainty.

Real-time implementation of MPC onboard a flight computer can be realistically achieved by formulating the optimization problem as a convex QP with a quadratic objective function and affine constraints. The use of a linear dynamic prediction model within the MPC framework is required in order for it to be formulated as a QP.

## 4.2RCD Constraint Relaxation

The control inputuRCD=τb​3RCDu^{\text{RCD}}=\tau^{\text{RCD}}_{b3}is chosen based on the momentum management strategy.
Considering the RCD on-off actuation as an explicit constraint in the MPC optimization problem leads to a mixed-integer problem, which is computationally expensive, and limits the practicality of onboard real-time MPC.
To enable the use of convex optimization solvers with the proposed MPC policy, the integer constraint is relaxed, and a PWM quantization is applied to the RCD actuation(Shen and Caverly,2026).
A continuous value ofumpcRCDu^{\text{RCD}}_{\text{mpc}}is allowed in the optimization problem, where−τb​3,onRCD≤umpcRCD≤τb​3,onRCD-\tau^{\text{RCD}}_{b3,\text{on}}\leq u^{\text{RCD}}_{\text{mpc}}\leq\tau^{\text{RCD}}_{b3,\text{on}}andτb​3,onRCD\tau^{\text{RCD}}_{b3,\text{on}}is the roll torque magnitude generated when the RCDs are turned on.
After solving the MPC optimization problem, the continuousumpcRCDu^{\text{RCD}}_{\text{mpc}}is then quantized into a discrete valueuRCD​(t)={βon​τb​3,onRCD,fortk≤t<(tk+tc),0,for(tk+tc)≤t<tk+1,u^{\text{RCD}}(t)=\begin{cases}\beta_{\text{on}}\tau^{\text{RCD}}_{b3,\text{on}},\quad\text{for}\quad t_{k}\leq t<(t_{k}+t_{c}),\\
0,\quad\text{for}\quad(t_{k}+t_{c})\leq t<t_{k+1},\end{cases}(11)

whereβon∈{−1,1}\beta_{\text{on}}\in\{-1,1\}denotes the clockwise and counterclockwise directions about the roll (b→3\underrightarrow{b}^{3}) axis,τb​3,onRCD\tau^{\text{RCD}}_{b3,\text{on}}denotes the torque magnitude when RCDs are turned on, andtc=Δ​t⋅umpcRCDτb​3,onRCDt_{c}=\Delta t\cdot\frac{u^{\text{RCD}}_{\text{mpc}}}{\tau^{\text{RCD}}_{b3,\text{on}}}is the length (cut-off time) of a single pulse PWM conversion from a continuous MPC optimal RCD input.
Details of the RCD quantization can be found in the work ofShen and Caverly (2026).

## 4.3Prediction Model

In contrast to the state𝐱\mbf{x}used in Section2.5, a modified state𝐱MPC=[𝜽𝖳𝝎𝐛𝐛𝐚𝖳𝐡𝟒RW𝖳𝐞int𝖳]𝖳\mbf{x}^{\text{MPC}}=\begin{bmatrix}{\boldsymbol{\theta}}^{\mathsf{T}}&{\boldsymbol{\omega}}^{ba^{\mathsf{T}}}_{b}&\mbf{h}^{\text{RW}^{\mathsf{T}}}_{4}&\mbf{e}^{\text{int}^{\mathsf{T}}}\end{bmatrix}^{\mathsf{T}}is employed in this MPC framework, where𝐡𝟒RW=𝐌𝟑𝟒†​𝐡𝐛RW\mbf{h}^{\text{RW}}_{4}=\mathbf{M}_{34}^{\dagger}\mbf{h}_{b}^{\text{RW}}follows the pseudo-inverse relationship discussed in Section2.3.
This modification allows for a direct constraint on the angular momentum of the individual RWs within the MPC framework.
Although a simple pseudo-inverse mapping is used in this prediction model, the proposed MPC approach is not limited to this specific optimal allocation method. More advanced RW angular momentum allocation synthesis can be used based on the design of the ADCS.

The linearized dynamics in Eq. (9) are modified to obtain a linear prediction model to be used in the MPC framework. Specifically, the linear transformation𝐱=𝐓𝐱MPC\mbf{x}=\mbf{T}\mbf{x}^{\text{MPC}}is applied, where𝐓=diag​(𝟏,𝟏,𝐌𝟑𝟒,𝟏)\mbf{T}=\text{diag}(\mbf{1},\mbf{1},\mbf{M}_{34},\mbf{1})is formed using the RW geometry matrix𝐌𝟑𝟒\mbf{M}_{34}. The inverse linear transformation𝐱MPC=𝐓†​𝐱\mbf{x}^{\text{MPC}}=\mbf{T}^{\dagger}\mbf{x}is computed using the pseudo-inverse of𝐌𝟑𝟒\mbf{M}_{34}as𝐓†=diag​(𝟏,𝟏,𝐌𝟑𝟒†,𝟏)\mbf{T}^{\dagger}=\text{diag}(\mbf{1},\mbf{1},\mbf{M}_{34}^{\dagger},\mbf{1}). Applying these transformations to Eq. (9) yields the linear dynamics𝐱˙MPC=𝐀MPC​𝐱MPC+𝐁𝐰MPC​𝐰+𝐁𝐮𝟏MPC​𝐮AMT+𝐁𝐮𝟐MPC​𝐮RCD+𝐳MPC,\dot{\mbf{x}}^{\text{MPC}}=\mbf{A}^{\text{MPC}}\mbf{x}^{\text{MPC}}+\mbf{B}_{w}^{\text{MPC}}\mbf{w}+\mbf{B}_{u1}^{\text{MPC}}\mbf{u}^{\text{AMT}}+\mbf{B}_{u2}^{\text{MPC}}u^{\text{RCD}}+\mbf{z}^{\text{MPC}},(12)

where𝐀MPC=𝐓†​𝐀𝐓\mbf{A}^{\text{MPC}}=\mbf{T}^{\dagger}\mbf{A}\mbf{T},𝐁𝐰MPC=𝐓†​𝐁𝐰\mbf{B}_{w}^{\text{MPC}}=\mbf{T}^{\dagger}\mbf{B}_{w},𝐁𝐮𝟏MPC=𝐓†​𝐁𝐮𝟏\mbf{B}_{u1}^{\text{MPC}}=\mbf{T}^{\dagger}\mbf{B}_{u1},𝐁𝐮𝟐MPC=𝐓†​𝐁𝐮𝟐\mbf{B}_{u2}^{\text{MPC}}=\mbf{T}^{\dagger}\mbf{B}_{u2}, and𝐳MPC=𝐓†​𝐳\mbf{z}^{\text{MPC}}=\mbf{T}^{\dagger}\mbf{z}. A ZOH is then applied to the inputs of Eq. (12) to yield the discrete-time linear prediction used by MPC over its prediction model, given by𝐱𝐣+𝟏|𝐭𝐤MPC=𝐀𝐣|𝐭𝐤MPC​𝐱𝐣|𝐭𝐤MPC+𝐁𝐰,𝐣|𝐭𝐤MPC​𝐰𝐣|𝐭𝐤+𝐁𝐮𝟏,𝐣|𝐭𝐤MPC​𝐮𝐣|𝐭𝐤AMT+𝐁𝐮𝟐,𝐣|𝐭𝐤MPC​𝐮𝐣|𝐭𝐤RCD+𝐳𝐣|𝐭𝐤MPC,𝐣=𝟎,𝟏,…,𝐍−𝟏,\mbf{x}^{\text{MPC}}_{j+1|t_{k}}=\mbf{A}^{\text{MPC}}_{j|t_{k}}\mbf{x}^{\text{MPC}}_{j|t_{k}}+\mbf{B}^{\text{MPC}}_{w,j|t_{k}}\mbf{w}_{j|t_{k}}+\mbf{B}^{\text{MPC}}_{u1,j|t_{k}}\mbf{u}^{\text{AMT}}_{j|t_{k}}+\mbf{B}^{\text{MPC}}_{u2,j|t_{k}}{u}^{\text{RCD}}_{j|t_{k}}+\mbf{z}^{\text{MPC}}_{j|t_{k}},\qquad j=0,1,\ldots,N-1,(13)

where the subscriptj|tkj|t_{k}refers to thejj-th discrete time step within the MPC prediction horizon at time steptkt_{k}.
The prediction model includes the state𝐱𝐣|𝐭𝐤MPC=[𝜽𝐣|𝐭𝐤𝖳𝝎𝐛,𝐣|𝐭𝐤𝐛𝐚𝖳𝐡𝟒,𝐣|𝐭𝐤RW𝖳𝐞𝐣|𝐭𝐤int𝖳]𝖳\mbf{x}^{\text{MPC}}_{j|t_{k}}=\begin{bmatrix}{\boldsymbol{\theta}}_{j|t_{k}}^{\mathsf{T}}&{\boldsymbol{\omega}}^{ba^{\mathsf{T}}}_{b,j|t_{k}}&\mbf{h}_{4,j|t_{k}}^{\text{RW}^{\mathsf{T}}}&\mbf{e}_{j|t_{k}}^{\text{int}^{\mathsf{T}}}\end{bmatrix}^{\mathsf{T}}, the AMT input𝐮𝐣|𝐭𝐤AMT\mbf{u}^{\text{AMT}}_{j|t_{k}}, and the RCD inputuj|tkRCD{u}^{\text{RCD}}_{j|t_{k}}to be designed across the prediction horizonj=0,1,…,N−1j=0,1,\ldots,N-1at timetkt_{k}. The disturbance torque is represented by𝐰𝐣|𝐭𝐤\mbf{w}_{j|t_{k}}. The MPC framework uses the state estimate from Kalman filter framework presented in Section3as its knowledge within the prediction model, where𝐱𝟎|𝐭𝐤MPC=[𝜽^𝐤𝖳𝝎^𝐛,𝐤𝐛𝐚𝖳𝐌𝟑𝟒†​𝐡^𝐛,𝐤RW𝖳𝐞^𝐤int𝖳]𝖳\mbf{x}^{\text{MPC}}_{0|t_{k}}=\begin{bmatrix}\hat{{\boldsymbol{\theta}}}_{k}^{\mathsf{T}}&\hat{{\boldsymbol{\omega}}}^{ba^{\mathsf{T}}}_{b,k}&\mathbf{M}_{34}^{\dagger}\hat{\mbf{h}}_{b,k}^{\text{RW}^{\mathsf{T}}}&\hat{\mbf{e}}_{k}^{\text{int}^{\mathsf{T}}}\end{bmatrix}^{\mathsf{T}}and𝐰𝐣|𝐭𝐤=𝐰^𝐤+\mbf{w}_{j|t_{k}}=\hat{\mbf{w}}^{+}_{k}forj=0,1,…,N−1j=0,1,\ldots,N-1.
The(⋅)^+\hat{(\cdot)}^{+}notation for a posteriori (measurement updated) state estimate is simplified as(⋅)^\hat{(\cdot)}to avoid notation clustering.
The LTV matrices of𝐀𝐣|𝐭𝐤MPC\mbf{A}^{\text{MPC}}_{j|t_{k}},𝐁𝐰,𝐣|𝐭𝐤MPC\mbf{B}^{\text{MPC}}_{w,j|t_{k}},𝐁𝐮𝟏,𝐣|𝐭𝐤MPC\mbf{B}^{\text{MPC}}_{u1,j|t_{k}},𝐁𝐮𝟐,𝐣|𝐭𝐤MPC\mbf{B}^{\text{MPC}}_{u2,j|t_{k}},𝐳𝐣|𝐭𝐤MPC\mbf{z}^{\text{MPC}}_{j|t_{k}}are linearized about the operation points (varying with the slew maneuver) across the prediction horizon, where𝐱¯j|tkMPC=[𝜽d,j|tk𝖳​𝝎d,j|tk𝖳​𝐌34†​𝐡^b,kRW𝖳​𝐞^kint𝖳]𝖳\bar{\mbf{x}}^{\text{MPC}}_{j|t_{k}}=\Big[{\boldsymbol{\theta}}_{d,j|t_{k}}^{\mathsf{T}}\,\,\,{\boldsymbol{\omega}}_{d,j|t_{k}}^{{\mathsf{T}}}\,\,\,\mathbf{M}_{34}^{\dagger}\hat{\mbf{h}}_{b,k}^{\text{RW}^{\mathsf{T}}}\,\,\,\hat{\mbf{e}}^{\text{int}^{\mathsf{T}}}_{k}\Big]^{\mathsf{T}}forj=0,1,…,N−1j=0,1,\ldots,N-1,𝐫¯bp​s=𝐫¯bp​s​(tk){\bar{\mbf{r}}}^{ps}_{b}={\bar{\mbf{r}}}^{ps}_{b}(t_{k}),𝐟¯bSRP=𝐟𝐛SRP​(𝐭𝐤)\bar{\mbf{f}}_{b}^{\text{SRP}}=\mbf{f}_{b}^{\text{SRP}}(t_{k})are updated at every momentum management timestep at timetkt_{k}, and𝐫¯˙bp​s=𝐫¯¨bp​s=𝟎\dot{\bar{\mbf{r}}}_{b}^{ps}=\ddot{\bar{\mbf{r}}}_{b}^{ps}=\mbf{0},𝝉¯bRCD=𝟎\bar{{\boldsymbol{\tau}}}^{\text{RCD}}_{b}=\mbf{0}. The time-varying parameters are the desired attitude𝜽d,j|tk{\boldsymbol{\theta}}_{d,j|t_{k}}and desired angular velocity𝝎d,j|tk{\boldsymbol{\omega}}_{d,j|t_{k}}, while the SRP force, disturbance torque, state (angular momentum and integral state), and AMT position to be linearized about are kept constant throughout the MPC prediction horizon.

## 4.4State Constraints

To ensure the practical feasibility of the controller, inequality constraints are imposed on the system states. These constraints enforce bounded deviations in sailcraft attitude, angular velocity, RW angular momentum, and integrated attitude error across the prediction horizon as𝜽d,j|tk−𝜽err≤𝜽j|tk≤𝜽d,j|tk+𝜽err{\boldsymbol{\theta}}_{d,j|t_{k}}-{\boldsymbol{\theta}}_{\text{err}}\leq{\boldsymbol{\theta}}_{j|t_{k}}\leq{\boldsymbol{\theta}}_{d,j|t_{k}}+{\boldsymbol{\theta}}_{\text{err}},𝝎d,j|tk−𝝎err≤𝝎b,j|tkb​a≤𝝎d,j|tk+𝝎err{\boldsymbol{\omega}}_{d,j|t_{k}}-{\boldsymbol{\omega}}_{\text{err}}\leq{\boldsymbol{\omega}}_{b,j|t_{k}}^{ba}\leq{\boldsymbol{\omega}}_{d,j|t_{k}}+{\boldsymbol{\omega}}_{\text{err}},𝐡𝟒,minRW≤𝐡𝟒,𝐣|𝐭𝐤RW≤𝐡𝟒,maxRW\mbf{h}^{\text{RW}}_{4,\text{min}}\leq\mbf{h}_{4,j|t_{k}}^{\text{RW}}\leq\mbf{h}^{\text{RW}}_{4,\text{max}}, and𝐞minint≤𝐞𝐣|𝐭𝐤int≤𝐞maxint\mbf{e}^{\text{int}}_{\text{min}}\leq\mbf{e}^{\text{int}}_{j|t_{k}}\leq\mbf{e}^{\text{int}}_{\text{max}}, respectively. The variables𝜽err{\boldsymbol{\theta}}_{\text{err}}and𝝎err{\boldsymbol{\omega}}_{\text{err}}are the allowable deviation from the nominal slew trajectory𝜽d,j|tk{\boldsymbol{\theta}}_{d,j|t_{k}}and𝝎d,j|tk{\boldsymbol{\omega}}_{d,j|t_{k}}across the prediction horizon. Collectively, this is written as the constraint𝐱minMPC≤𝐱𝐣|𝐭𝐤MPC≤𝐱maxMPC\mbf{x}^{\text{MPC}}_{\text{min}}\leq\mbf{x}^{\text{MPC}}_{j|t_{k}}\leq\mbf{x}^{\text{MPC}}_{\text{max}}.

To further avoid the RW angular momentum approaching the hardware physical saturation limits during sustained disturbance rejection accommodate modeling errors, soft constraints are introduced to incentivize the RW angular momentum to stay within a safe operational margin.
These soft bounds are defined as𝐡𝟒,minsoft−𝜶≤𝐡𝟒,𝐣|𝐭𝐤RW≤𝐡𝟒,maxsoft+𝜶,\mbf{h}_{4,\text{min}}^{\text{soft}}-{\boldsymbol{\alpha}}\leq\mbf{h}^{\text{RW}}_{4,j|t_{k}}\leq\mbf{h}_{4,\text{max}}^{\text{soft}}+{\boldsymbol{\alpha}},

where where𝐡𝟒,minsoft\mbf{h}_{4,\text{min}}^{\text{soft}}and𝐡𝟒,maxsoft\mbf{h}_{4,\text{max}}^{\text{soft}}represent the lower and upper bounds of the soft constraint envelope (i.e., the desired safe operation region), and the non-negative slack variable𝜶≥𝟎{\boldsymbol{\alpha}}\geq\mbf{0}is quadratically penalized in the MPC objective function, enabling graceful constraint relaxation while encouraging the system to remain within the nominal safe range.
Within the soft bounds, the slack variable remains zero and no penalty is incurred. When violated, the controller attempts to reduce the non-zero value of𝜶{\boldsymbol{\alpha}}to drive the RWs angular momentum back within the safe region, avoiding saturation.Figure 3:Illustration of the MPC soft constraint design with a prediction horizon ofN=5N=5, where no penalty is incurred for responses satisfyinghminsoft≤h≤hmaxsofth^{\text{soft}}_{\text{min}}\leq h\leq h^{\text{soft}}_{\text{max}}, while a quadratic penalty appears in the MPC objective function whenhmaxsoft≤hh^{\text{soft}}_{\text{max}}\leq horh≤hminsofth\leq h^{\text{soft}}_{\text{min}}. The response labeled “MPC design 1” indicates a design that violates the soft constraint, while “MPC design 2” does not.

Figure3illustrates the relationship between the soft constraint and the operational limits of the RWs. The original hard limitshmaxh_{\text{max}}andhminh_{\text{min}}define the absolute, physically-imposed boundaries that cannot be violated. The soft constraint boundshmaxsofth^{\text{soft}}_{\text{max}}andhminsofth^{\text{soft}}_{\text{min}}define the preferred operating limits. The light blue area defined byhminsoft≤h≤hmaxsofth^{\text{soft}}_{\text{min}}\leq h\leq h^{\text{soft}}_{\text{max}}is the region where the soft constraint is satisfied and the slack variable𝜶{\boldsymbol{\alpha}}is zero and has not effect on the MPC objective function. The light red area defined byhmaxsoft≤hh^{\text{soft}}_{\text{max}}\leq horh≤hminsofth\leq h^{\text{soft}}_{\text{min}}is the region where the soft constraint is violated. When the MPC design variable enters this region, the slack variable𝜶{\boldsymbol{\alpha}}takes on a positive value and the violation is heavily penalized in the objective function. Two examples of design variable sequence interpreting the design choices in the MPC optimization are shown in Fig.3. The red trajectory (labeled as “MPC design 1”) represents an action that violates the soft constraint in the first two steps, incurring a large penalty due to the quadratic weight on the slack variable in the MPC objective function. The blue trajectory (labeled as “MPC design 2”) represents a sequence of design that remains within the feasible region, incurring no penalty within the MPC objective function.

The soft constraint serves to improve feasibility of the MPC optimization problem by penalizing, rather than prohibiting, constraint violation. This structure strongly discourages the design variables from exceeding the soft boundshmaxsoft≤h≤hminsofth^{\text{soft}}_{\text{max}}\leq h\leq h^{\text{soft}}_{\text{min}}, but allows for excursions outside this region if the performance benefit outweighs the imposed penalty.

## 4.5Input Constraints

To ensure actuator feasibility and the satisfaction of hardware limits, constraints are imposed on both the control input magnitude and the rate of AMT motion. The actuator input𝐮𝐣|𝐭𝐤=[𝐮𝐣|𝐭𝐤AMT𝖳𝐮𝐣|𝐭𝐤RCD]𝖳\mbf{u}_{j|t_{k}}=\begin{bmatrix}\mbf{u}^{\text{AMT}^{\mathsf{T}}}_{j|t_{k}}&{u}^{\text{RCD}}_{j|t_{k}}\end{bmatrix}^{\mathsf{T}}is subject to the constraints𝐮min≤𝐮𝐣|𝐭𝐤≤𝐮max\mbf{u}_{\text{min}}\leq\mbf{u}_{j|t_{k}}\leq\mbf{u}_{\text{max}},
where the bounds𝐮min=[𝐮minAMT𝖳−τ𝐛𝟑,onRCD]𝖳\mbf{u}_{\text{min}}=\begin{bmatrix}\mbf{u}^{\text{AMT}^{\mathsf{T}}}_{\text{min}}&-\tau^{\text{RCD}}_{b3,\text{on}}\end{bmatrix}^{\mathsf{T}}and𝐮max=[𝐮maxAMT𝖳τ𝐛𝟑,onRCD]𝖳\mbf{u}_{\text{max}}=\begin{bmatrix}\mbf{u}^{\text{AMT}^{\mathsf{T}}}_{\text{max}}&\tau^{\text{RCD}}_{b3,\text{on}}\end{bmatrix}^{\mathsf{T}}reflect the physical actuation limits of the AMT position and RCD torque. It is assumed that the RCD torque magnitude is accessible from the ADCS, which can be computed based on the SIA.

In addition, the translational rate of the AMT is constrained to avoid unrealistic or dynamically infeasible actuation commands, referring to the physical speed limit of AMT. Due to the discrete-time formulation of the MPC problem, the rate constraint is implemented as a finite difference inequality𝐮˙minAMT≤𝐮𝐣|𝐭𝐤AMT−𝐮𝐣−𝟏|𝐭𝐤AMTΔ​t≤𝐮˙maxAMT,\dot{\mbf{u}}^{\text{AMT}}_{\text{min}}\leq\frac{\mbf{u}^{\text{AMT}}_{j|t_{k}}-\mbf{u}^{\text{AMT}}_{j-1|t_{k}}}{\Delta t}\leq\dot{\mbf{u}}^{\text{AMT}}_{\text{max}},

where𝐮˙minAMT\dot{\mbf{u}}^{\text{AMT}}_{\text{min}}and𝐮˙maxAMT\dot{\mbf{u}}^{\text{AMT}}_{\text{max}}define the allowable lower and upper bounds on the AMT velocity.

To ensure input continuity across successive control intervals, which is critical for the AMT input between discrete time steps, the initial AMT input at each new MPC update must match the current AMT position. This continuity constraint is enforced as𝐮−𝟏|𝐭𝐤AMT=𝐮AMT​(𝐭𝐤)\mbf{u}^{\text{AMT}}_{-1|t_{k}}=\mbf{u}^{\text{AMT}}(t_{k}), where the current AMT position becomes a design variable fixed by this equality constraint and is used to constrain the AMT rate of the first input within the MPC optimization problem.
This formulation ensures smooth AMT motion while preserving the predictive accuracy and numerical stability of the MPC framework.

## 4.6Objective Function

The objective function of the proposed MPC policy is formulated to balance state regulation, actuator efficiency, AMT motion minimization, and enforcement of soft constraints. It is defined as∑j=0N−1((𝐱𝐣|𝐭𝐤MPC−𝐱¯𝐣|𝐭𝐤MPC)𝖳𝐐(𝐱𝐣|𝐭𝐤MPC−𝐱¯𝐣|𝐭𝐤MPC)+𝐮𝐣|𝐭𝐤𝖳𝐑𝐮𝐣|𝐭𝐤+𝐮~𝐣|𝐭𝐤AMT𝖳𝐑~𝐮~𝐣|𝐭𝐤AMT)+(𝐱𝐍|𝐭𝐤MPC−𝐱¯𝐍|𝐭𝐤MPC)𝖳𝐐𝐍(𝐱𝐍|𝐭𝐤MPC−𝐱¯𝐍|𝐭𝐤MPC)+𝜶𝖳𝐂𝜶,\sum_{j=0}^{N-1}\Bigl((\mbf{x}_{j|t_{k}}^{\text{MPC}}-{\bar{\mbf{x}}}_{j|t_{k}}^{\text{MPC}})^{\mathsf{T}}\mbf{Q}(\mbf{x}^{\text{MPC}}_{j|t_{k}}-{\bar{\mbf{x}}}_{j|t_{k}}^{\text{MPC}})+\mbf{u}_{j|t_{k}}^{\mathsf{T}}\mbf{R}\mbf{u}_{j|t_{k}}+\tilde{\mbf{u}}^{\text{AMT}^{\mathsf{T}}}_{j|t_{k}}\tilde{\mbf{R}}\tilde{\mbf{u}}^{\text{AMT}}_{j|t_{k}}\Bigl)+(\mbf{x}_{N|t_{k}}^{\text{MPC}}-{\bar{\mbf{x}}}_{N|t_{k}}^{\text{MPC}})^{\mathsf{T}}\mbf{Q}_{N}(\mbf{x}^{\text{MPC}}_{N|t_{k}}-{\bar{\mbf{x}}}_{N|t_{k}}^{\text{MPC}})+{\boldsymbol{\alpha}}^{\mathsf{T}}\mbf{C}{\boldsymbol{\alpha}},

where𝐱𝐣|𝐭𝐤MPC\mbf{x}^{\text{MPC}}_{j|t_{k}}and𝐮𝐣|𝐭𝐤\mbf{u}_{j|t_{k}}denote the predicted state and control input at stagejjover the prediction horizon of lengthNN;𝐱¯j|tkMPC=[𝜽d,j|tk𝖳​𝝎d,j|tk𝖳​𝐌34†​𝐡^b,kRW𝖳​𝐞^kint𝖳]𝖳\bar{\mbf{x}}^{\text{MPC}}_{j|t_{k}}=\Big[{\boldsymbol{\theta}}_{d,j|t_{k}}^{\mathsf{T}}\,\,\,{\boldsymbol{\omega}}_{d,j|t_{k}}^{{\mathsf{T}}}\,\,\,\mathbf{M}_{34}^{\dagger}\hat{\mbf{h}}_{b,k}^{\text{RW}^{\mathsf{T}}}\,\,\,\hat{\mbf{e}}^{\text{int}^{\mathsf{T}}}_{k}\Big]^{\mathsf{T}}is the operating point at stagejjover the prediction horizon of lengthNN;𝐐=𝐐𝖳\mbf{Q}=\mbf{Q}^{\mathsf{T}}and𝐑=𝐑𝖳\mbf{R}=\mbf{R}^{\mathsf{T}}are positive semi-definite and positive definite weighting matrices, respectively, penalizing the state and control input;𝐐𝐍\mbf{Q}_{N}is the terminal weighting matrix for the final predicted state at stageNN;𝐂=𝐂𝖳\mbf{C}=\mbf{C}^{\mathsf{T}}is a positive semi-definite matrix that penalizes violation of the soft constraint via the slack variable𝜶≥𝟎{\boldsymbol{\alpha}}\geq\mbf{0};𝐑~=𝐑~𝖳{\tilde{\mbf{R}}}={\tilde{\mbf{R}}}^{\mathsf{T}}is a positive semi-definite matrix penalizing the rate of AMT translation; and𝐮~j|tkAMT=𝐮𝐣|𝐭𝐤AMT−𝐮𝐣−𝟏|𝐭𝐤AMT\tilde{\mbf{u}}^{\text{AMT}}_{j|t_{k}}=\mbf{u}^{\text{AMT}}_{j|t_{k}}-\mbf{u}^{\text{AMT}}_{j-1|t_{k}}is the difference between thejj-th AMT input and the previous input.

The term𝐮~j|tkAMT𝖳​𝐑~​𝐮~j|tkAMT\tilde{\mbf{u}}^{\text{AMT}^{\mathsf{T}}}_{j|t_{k}}\tilde{\mbf{R}}\tilde{\mbf{u}}^{\text{AMT}}_{j|t_{k}}is included to discourage unnecessary movement of the AMT, thereby promoting actuator efficiency and helping maintain the AMT in a relatively stationary configuration across time steps. This is particularly important given the discretized AMT inputs and the associated mechanical and dynamic constraints.
The slack variable penalty𝜶𝖳​𝐂​𝜶{\boldsymbol{\alpha}}^{\mathsf{T}}\mbf{C}{\boldsymbol{\alpha}}enables soft constraint enforcement on RW angular momentum, where violations are permitted when necessary, but discouraged through a quadratic penalty.

## 4.7Summary of MPC Policy and Implementation Details

The proposed MPC policy involves solving for the optimization problemminimize𝓧,𝓤,𝜶∑j=0N−1((𝐱𝐣|𝐭𝐤MPC−𝐱¯𝐣|𝐭𝐤MPC)𝖳𝐐(𝐱𝐣|𝐭𝐤MPC−𝐱¯𝐣|𝐭𝐤MPC)+𝐮𝐣|𝐭𝐤𝖳𝐑𝐮𝐣|𝐭𝐤+𝐮~𝐣|𝐭𝐤AMT𝖳𝐑~𝐮~𝐣|𝐭𝐤AMT)+(𝐱𝐍|𝐭𝐤MPC−𝐱¯𝐍|𝐭𝐤MPC)𝖳𝐐𝐍(𝐱𝐍|𝐭𝐤MPC−𝐱¯𝐍|𝐭𝐤MPC)+𝜶𝖳𝐂𝜶\displaystyle\operatorname*{minimize}_{{\boldsymbol{\mathcal{X}}},\hskip 2.0pt{\boldsymbol{\mathcal{U}}},\hskip 2.0pt{\boldsymbol{\alpha}}}\sum_{j=0}^{N-1}\Bigl((\mbf{x}_{j|t_{k}}^{\text{MPC}}-{\bar{\mbf{x}}}_{j|t_{k}}^{\text{MPC}})^{\mathsf{T}}\mbf{Q}(\mbf{x}^{\text{MPC}}_{j|t_{k}}-{\bar{\mbf{x}}}_{j|t_{k}}^{\text{MPC}})+\mbf{u}_{j|t_{k}}^{\mathsf{T}}\mbf{R}\mbf{u}_{j|t_{k}}+\tilde{\mbf{u}}^{\text{AMT}^{\mathsf{T}}}_{j|t_{k}}\tilde{\mbf{R}}\tilde{\mbf{u}}^{\text{AMT}}_{j|t_{k}}\Bigl)+(\mbf{x}_{N|t_{k}}^{\text{MPC}}-{\bar{\mbf{x}}}_{N|t_{k}}^{\text{MPC}})^{\mathsf{T}}\mbf{Q}_{N}(\mbf{x}_{N|t_{k}}^{\text{MPC}}-{\bar{\mbf{x}}}_{N|t_{k}}^{\text{MPC}})+{\boldsymbol{\alpha}}^{\mathsf{T}}\mbf{C}{\boldsymbol{\alpha}}(14)subject to𝐱𝐣+𝟏|𝐭𝐤MPC=𝐀𝐣|𝐭𝐤MPC​𝐱𝐣|𝐭𝐤MPC+𝐁𝐰,𝐣|𝐭𝐤MPC​𝐰𝐣|𝐭𝐤+𝐁𝐮𝟏,𝐣|𝐭𝐤MPC​𝐮𝐣|𝐭𝐤AMT+𝐁𝐮𝟐,𝐣|𝐭𝐤MPC​𝐮𝐣|𝐭𝐤RCD+𝐳𝐣|𝐭𝐤MPC,𝐣=𝟎,𝟏,…,𝐍−𝟏,\displaystyle\hskip 10.00002pt\mbf{x}^{\text{MPC}}_{j+1|t_{k}}=\mbf{A}^{\text{MPC}}_{j|t_{k}}\mbf{x}^{\text{MPC}}_{j|t_{k}}+\mbf{B}^{\text{MPC}}_{w,j|t_{k}}\mbf{w}_{j|t_{k}}+\mbf{B}^{\text{MPC}}_{u1,j|t_{k}}\mbf{u}^{\text{AMT}}_{j|t_{k}}+\mbf{B}^{\text{MPC}}_{u2,j|t_{k}}{u}^{\text{RCD}}_{j|t_{k}}+\mbf{z}^{\text{MPC}}_{j|t_{k}},\qquad j=0,1,\ldots,N-1,𝐱𝟎|𝐭𝐤MPC=𝐱MPC​(𝐭𝐤),\displaystyle\hskip 10.00002pt\mbf{x}^{\text{MPC}}_{0|t_{k}}=\mbf{x}^{\text{MPC}}(t_{k}),𝐮−𝟏|𝐭𝐤AMT=𝐮AMT​(𝐭𝐤),\displaystyle\hskip 10.00002pt\mbf{u}^{\text{AMT}}_{-1|t_{k}}=\mbf{u}^{\text{AMT}}(t_{k}),𝐱minMPC≤𝐱𝐣|𝐭𝐤MPC≤𝐱maxMPC,𝐣=𝟎,…,𝐍,\displaystyle\hskip 10.00002pt\mbf{x}^{\text{MPC}}_{\text{min}}\leq\mbf{x}^{\text{MPC}}_{j|t_{k}}\leq\mbf{x}^{\text{MPC}}_{\text{max}},\hskip 11.49994ptj=0,\ldots,N,𝐮min≤𝐮𝐣|𝐭𝐤≤𝐮max,𝐣=𝟎,…,𝐍−𝟏,\displaystyle\hskip 10.00002pt\mbf{u}_{\text{min}}\leq\mbf{u}_{j|t_{k}}\leq\mbf{u}_{\text{max}},\hskip 11.49994ptj=0,\ldots,N-1,𝐮˙minAMT≤𝐮𝐣|𝐭𝐤AMT−𝐮𝐣−𝟏|𝐭𝐤AMTΔ​t≤𝐮˙maxAMT,j=0,…,N−1,\displaystyle\hskip 10.00002pt\dot{\mbf{u}}^{\text{AMT}}_{\text{min}}\leq\frac{\mbf{u}^{\text{AMT}}_{j|t_{k}}-\mbf{u}^{\text{AMT}}_{j-1|t_{k}}}{\Delta t}\leq\dot{\mbf{u}}^{\text{AMT}}_{\text{max}},\hskip 10.00002ptj=0,\ldots,N-1,𝐡𝟒,minsoft−𝜶≤𝐡𝟒,𝐣|𝐭𝐤RW≤𝐡𝟒,maxsoft+𝜶,𝐣=𝟎,…,𝐍,\displaystyle\hskip 10.00002pt\mbf{h}_{4,\text{min}}^{\text{soft}}-{\boldsymbol{\alpha}}\leq\mbf{h}^{\text{RW}}_{4,j|t_{k}}\leq\mbf{h}_{4,\text{max}}^{\text{soft}}+{\boldsymbol{\alpha}},\hskip 11.49994ptj=0,\ldots,N,𝜶≥𝟎,\displaystyle\hskip 10.00002pt{\boldsymbol{\alpha}}\geq\mbf{0},

where𝜶∈ℝ4{\boldsymbol{\alpha}}\in\mathbb{R}^{4},𝓧={𝐱𝟎|𝐭𝐤MPC,𝐱𝟏|𝐭𝐤MPC,…,𝐱𝐍|𝐭𝐤MPC}{\boldsymbol{\mathcal{X}}}=\{\mbf{x}^{\text{MPC}}_{0|t_{k}},\mbf{x}^{\text{MPC}}_{1|t_{k}},\ldots,\mbf{x}^{\text{MPC}}_{N|t_{k}}\},𝓤={𝐮−𝟏|𝐭𝐤,𝐮𝟎|𝐭𝐤,𝐮𝟏|𝐭𝐤,…,𝐮𝐍−𝟏|𝐭𝐤}{\boldsymbol{\mathcal{U}}}=\{\mbf{u}_{-1|t_{k}},\mbf{u}_{0|t_{k}},\mbf{u}_{1|t_{k}},\ldots,\mbf{u}_{N-1|t_{k}}\}are the design variables,NNis the number of timesteps in the prediction horizon,𝐱MPC​(𝐭𝐤)=[𝜽^𝐤𝖳𝝎^𝐛,𝐤𝐛𝐚𝖳𝐌𝟑𝟒†​𝐡^𝐛,𝐤RW𝖳𝐞^𝐤int𝖳]𝖳\mbf{x}^{\text{MPC}}(t_{k})=\begin{bmatrix}\hat{{\boldsymbol{\theta}}}_{k}^{\mathsf{T}}&\hat{{\boldsymbol{\omega}}}^{ba^{\mathsf{T}}}_{b,k}&\mathbf{M}_{34}^{\dagger}\hat{\mbf{h}}_{b,k}^{\text{RW}^{\mathsf{T}}}&\hat{\mbf{e}}_{k}^{\text{int}^{\mathsf{T}}}\end{bmatrix}^{\mathsf{T}}is the known system state at timetkt_{k},𝐰𝐣|𝐭𝐤=𝐰^𝐤+\mbf{w}_{j|t_{k}}=\hat{\mbf{w}}^{+}_{k}is the Kalman filter disturbance estimate, and𝐮AMT​(𝐭𝐤)\mbf{u}^{\text{AMT}}(t_{k})is the AMT position at timetkt_{k}.

Due to the use of a quadratic objective function, affine equality constraints, and affine inequality constraints, this MPC policy can be solved as a QP at each time step.
The MATLAB functionquadprogwith its default settings is used to solve the QP optimization problem in the simulation results of this work.
Solving this problem yields a sequence of optimal control inputs over the prediction horizon, i.e.,𝓤∗={𝐮−𝟏|𝐭𝐤∗,𝐮𝟎|𝐭𝐤∗,𝐮𝟏|𝐭𝐤∗,…,𝐮𝐍−𝟏|𝐭𝐤∗}{\boldsymbol{\mathcal{U}}}^{*}=\{\mbf{u}_{-1|t_{k}}^{*},\mbf{u}_{0|t_{k}}^{*},\mbf{u}_{1|t_{k}}^{*},\ldots,\mbf{u}_{N-1|t_{k}}^{*}\}. Only the first input (𝐮𝟎|𝐭𝐤∗\mbf{u}_{0|t_{k}}^{*}) is applied to the system before proceeding to the next time step and again solving for the optimal sequence of control inputs.

In this work, the Kalman filter is designed to operate at the same rate (every100100seconds) as the MPC momentum management time step.
At every time steptkt_{k}, a measurement update is performed, and the Kalman filter state𝐗^k+=[𝐱^k+𝐰^k+]\hat{\mbf{X}}_{k}^{+}=\begin{bmatrix}\hat{\mbf{x}}^{+}_{k}\\
\hat{\mbf{w}}^{+}_{k}\end{bmatrix}is extracted to formulate the MPC prediction model in Eq. (13), where𝐱𝐤=𝐱^𝐤+\mbf{x}_{k}=\hat{\mbf{x}}^{+}_{k}and𝐰𝐤=𝐰^𝐤+\mbf{w}_{k}=\hat{\mbf{w}}^{+}_{k}are used for the prediction model at timetkt_{k}, and the linear transformation𝐓\mbf{T}is used to compute𝐱𝐤MPC\mbf{x}^{\text{MPC}}_{k}, where𝐱𝐤MPC=𝐓𝐱𝐤\mbf{x}^{\text{MPC}}_{k}=\mbf{T}\mbf{x}_{k}.
This transformation enables MPC to seek a minimum norm angular momentum allocation while directly constraining the angular momentum on each RW.

The recursive nature of the MPC necessitates the prediction model to be re-linearized about the current state and inputs at every time step. To improve actuation efficiency and mitigate noise, operational actuation thresholds on the AMT and RCDs are introduced as additional design tuning parameters.
These thresholds are designed to trim out minor control demands, removing small AMT movements and RCD thrusts that typically arise from minor momentum management or noisy state estimates.
Specifically, any element of the MPC-demanded AMT position change satisfying the element-wise inequality|(𝐮𝟎|𝐭𝐤AMT−𝐮−𝟏|𝐭𝐤AMT)/𝚫​𝐭|≤βthreshAMT​𝐮˙maxAMT\big|(\mbf{u}^{\text{AMT}}_{0|t_{k}}-\mbf{u}^{\text{AMT}}_{-1|t_{k}})/\Delta t\big|\leq\beta^{\text{AMT}}_{\text{thresh}}\dot{\mbf{u}}^{\text{AMT}}_{\text{max}}is set to stay at its current position (𝐮𝟎|𝐭𝐤AMT=𝐮−𝟏|𝐭𝐤AMT\mbf{u}^{\text{AMT}}_{0|t_{k}}=\mbf{u}^{\text{AMT}}_{-1|t_{k}}) for the upcoming time step. Additionally, if the MPC-demanded RCD input satisfies|u0|tkRCD|<βthreshRCD​umaxRCD\big|{u}^{\text{RCD}}_{0|t_{k}}\big|<\beta^{\text{RCD}}_{\text{thresh}}{u}^{\text{RCD}}_{\text{max}}, then it is set to zero.
In both cases, the control input is applied to the system only when the MPC demands an input exceeding the predefined magnitude thresholds.
The momentum management inputs filtered by the thresholds are then passed to perform the time update of the Kalman filter, and applied to the system.

Since the MPC demanded RCD input is a continuous value between±τb​3,onRCD\pm\tau^{\text{RCD}}_{b3,\text{on}}, it does not directly match the on-off actuation mechanism of the RCD array.
A single pulse PWM-quantization technique in Eq. (11) is used to turn the continuous RCD input value to a pulse length specified time withτb​3,onRCD\tau^{\text{RCD}}_{b3,\text{on}}value.
These thresholding filter and PWM-quantization are leveraging the MPC recursive nature. Once an input is trimmed or modified at one time step, the MPC recalculates the optimal inputs using the latest state at the next time step, compensating for the mismatched input and system dynamics.

## 5Numerical Simulation Results

Numerical simulation experiments are performed to validate the MPC momentum management policy on Solar Cruiser.
Section5.1presents the setup of the system and the controller.
Section5.2presents the state-of-the-art thresholding momentum management control developed for NASA’s Solar Cruiser byInness et al. (2023); Tyler et al. (2023), which is used as a validation of the simulation environment and a benchmark comparison to the proposed method.
Section5.3presents simulations of the proposed MPC momentum management policy under different conditions, exhibiting the importance of incorporating a disturbance estimate with the MPC policy and the effect that threshold design has on actuator efficiency.
Section5.4presents a direct comparison of the proposed MPC-based momentum management and the state-of-the-art NASA’s thresholding method.

## 5.1Simulation SetupTable 1:System parameters used in the numerical simulations.ParameterValueUnitsmpm_{p}55.555.5kgmsm_{s}55.555.5kg𝐉𝐛𝒫​𝐩\mbf{J}^{\mathcal{P}p}_{b}diag​(4.01,4.01,6.07)\textrm{diag}(4.01,4.01,6.07)kg⋅\cdotm2𝐉𝐛𝒮​𝐬\mbf{J}^{\mathcal{S}s}_{b}diag​(8049.8,8049.8,16099.6)\textrm{diag}(8049.8,8049.8,16099.6)kg⋅\cdotm2rwr_{w}0.110.11mrb​3p​s{r}^{ps}_{b3}0.470.47m

The simulation parameters are chosen to reflect NASA’s Solar Cruiser(Johnson et al.,2019; Johnson and Curran,2020; Tyler et al.,2023; Inness et al.,2023).
The total mass of the sailcraft is111111kg, where the bus and the sail each contribute half of the total mass.
The out-of-plane offset between the CM and the sail surface (also the CP) is captured byrb​3p​s{r}^{ps}_{b3}, the third component of𝐫𝐛𝐩𝐬​(𝐭)\mbf{r}^{ps}_{b}(t).
Unlike the simulations performed byShen and Caverly (2026)that assumed this offset to be zero, this distance is chosen asrb​3p​s=0.47{r}^{ps}_{b3}=0.47m in this paper to more accurately simulate Solar Cruiser’s geometry.
The rest of Solar Cruiser’s physical parameters are included in Table1.

The configuration of the 4-RW pyramid is given byψi=60∘\psi_{i}=60^{\circ}for allii,ϕi=45∘+(i−1)⋅90∘\phi_{i}=45^{\circ}+(i-1)\cdot 90^{\circ}fori=1,2,3,4i=1,2,3,4, resulting in the mapping matrix given in Eq.3.
The RWs perform attitude tracking using the PID control law in Eq. (2) with gains𝐊𝐩=0.25⋅𝟏𝟑×𝟑\mbf{K}_{p}=0.25\cdot\mbf{1}_{3\times 3}N⋅\cdotm/rad,𝐊𝐝=𝟏𝟏𝟐⋅𝟏𝟑×𝟑\mbf{K}_{d}=112\cdot\mbf{1}_{3\times 3}N⋅\cdotm⋅\cdots/rad,𝐊𝐢=𝟖×𝟏𝟎−𝟒⋅𝟏𝟑×𝟑\mbf{K}_{i}=8\times 10^{-4}\cdot\mbf{1}_{3\times 3}N⋅\cdotm/(rad⋅\cdots).
The desired maneuver trajectory (𝜽d{\boldsymbol{\theta}}_{d}and𝝎d{\boldsymbol{\omega}}_{d}) follows the sequence of attitude hold, forward slew, attitude hold, return slew, and attitude hold.
The trajectory parameters include the maximum slew rate𝜽˙slew=[0.01   0.01   0.0035]𝖳\dot{{\boldsymbol{\theta}}}_{\text{slew}}=\big[0.01\,\,\,0.01\,\,\,0.0035\big]^{\mathsf{T}}deg/s, acceleration time (required to reach maximum slew rate)taccel=500t_{\text{accel}}=500s, start time of forward slewtstart=10000t_{\text{start}}=10000s, and start time of return slewtreturn=20000t_{\text{return}}=20000s. The desired slew trajectory follows the trapezoidal Euler angle rate profile defined in the Appendix. The initial attitude𝜽0{{\boldsymbol{\theta}}}_{0}and slew goal attitude𝜽goal{\boldsymbol{\theta}}_{\text{goal}}are defined in the subsequent simulation cases.

A static membrane shape model developed inBunker and Caverly (2026)and motivated by the Solar Cruiser shape analysis performed byGauvain and Tyler (2023)is employed to compute𝐟𝐛SRP\mbf{f}_{b}^{\text{SRP}}and𝝉bdist{\boldsymbol{\tau}}_{b}^{\text{dist}}based on the solar sail’s attitude𝜽{\boldsymbol{\theta}}.
This sail shape model implements Solar Cruiser’s membrane optical properties(Heaton and Artusio-Glimpse,2015; Heaton et al.,2017), as well as its expected structural and membrane deformation(Gauvain and Tyler,2023). A non-flat sail membrane with non-ideal reflectivity properties is used in the numerical simulations, where the billowing at the centroid of each quadrant is1515cm, and a±50\pm 50cm alternating boom tip deflections to match the analysis ofBunker and Caverly (2026).
The sail membrane shape model fromBunker and Caverly (2026)includes a discretized mesh with 3,600 triangular elements, where the local SIA is computed for each planar element. The force exerted on each triangular sail mesh element by the local SRP is applied at the element’s planar centroid and modeled as a normal force,FniF_{n}^{i}, and tangential force,FtiF_{t}^{i}, given byFti\displaystyle F_{t}^{i}=P​Ai​(1−r​s)​cos⁡(αi)​sin⁡(αi),\displaystyle=PA^{i}(1-rs)\cos(\alpha^{i})\sin(\alpha^{i}),Fni\displaystyle F_{n}^{i}=−P​Ai​(1−r​s)​cos2⁡(αi)−P​Ai​Bf​(1−s)​r​cos⁡(αi)−P​Ai​(1−r)​cos⁡(αi)​(ef​Bf−eb​Bbef+eb),\displaystyle=-PA^{i}(1-rs)\cos^{2}(\alpha^{i})-PA^{i}B_{f}(1-s)r\cos(\alpha^{i})-PA^{i}(1-r)\cos(\alpha^{i})\left(\frac{e_{f}B_{f}-e_{b}B_{b}}{e_{f}+e_{b}}\right),

whereP=4.5391×10−6P=4.5391\times 10^{-6}N/m2is the solar pressure at one astronomical unit (au),AiA^{i}is the area of the i’th sail element,r=0.91r=0.91is the reflection coefficient,s=0.94s=0.94is the fraction of specular reflection coefficient,αi\alpha^{i}is the local SIA of the i’th sail element,Bb=0.67B_{b}=0.67andBf=0.79B_{f}=0.79are the back and front non-Lambertian coefficients, andeb=0.27e_{b}=0.27andef=0.025e_{f}=0.025are the back and front surface emissivity, respectively(Heaton and Artusio-Glimpse,2015). The total SRP force and disturbance torque is computed by adding up the normal and tangential forces across all sail membrane elements and accounting for the location of each element which solving for the SRP disturbance torque.
The resulting attitude-dependent SRP force and disturbance torque profiles are shown in Fig.4, where the attitude is represented by the conventional SIA and clock angle. The nominal reference attitude trajectory involving a hold-slew-hold-slew-hold maneuver sequence, starting from an initial attitude of𝜽0=𝟎{\boldsymbol{\theta}}_{0}=\mbf{0}and slewing to a target attitude of𝜽goal=[0∘​15∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,15^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}is represented by the red lines in Fig.4. The green dashed lines in Fig.4are the nominal reference attitude trajectory with𝜽goal=[0∘​10∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}. The plots are restricted to the0∘0^{\circ}to30∘30^{\circ}SIA range, which is twice the nominal operational envelope of the Solar Cruiser mission(Tyler et al.,2023; Heaton et al.,2023).
The relationship between sailcraft attitude𝜽{\boldsymbol{\theta}}, the associated SIA and clock angle, and the corresponding SRP force and disturbance torque at11au is included in Table2.
Given the slow varying nature and small magnitude of SRP force and torque,𝐟𝐛SRP\mbf{f}^{\text{SRP}}_{b}and𝝉bdist{\boldsymbol{\tau}}^{\text{dist}}_{b}are updated at every2020seconds in the simulation.
The simulation and attitude control timestep isd​t=1\textrm{d}t=1second, and the momentum management time step isΔ​t=100\Delta t=100seconds.Figure 4:The attitude-dependent SRP force and disturbance torque as functions of SIA and clock angle. The colorbars on the left plots indicate the SRP force, while the colorbars on the right plots indicate the SRP torque. Note that the colorbar scales vary across subplots to accommodate the large magnitude differences between axes. The red lines and the green dashed lines are the reference trajectories defining the operational envelopes for slew maneuvers toward𝜽goal=[0∘​15∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,15^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}and𝜽goal=[0∘​10∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}, respectively, both starting from an initial attitude of𝜽0=𝟎{\boldsymbol{\theta}}_{0}=\mbf{0}.Table 2:Attitude correspondence to SRP force and torque.Attitude𝜽{\boldsymbol{\theta}}[SIA,clock angle]𝐟𝐛SRP\mbf{f}^{\text{SRP}}_{b}𝝉bdist{\boldsymbol{\tau}}^{\text{dist}}_{b}𝟎\mbf{0}[17∘17^{\circ},10∘10^{\circ}][3.13−0.56   133.03]𝖳×10−4\big[3.13\,\,\,-0.56\,\,\,133.03\big]^{\mathsf{T}}\times 10^{-4}N[208.78−1493.80−6.91]𝖳×10−6\big[208.78\,\,\,-1493.80\,\,\,-6.91\big]^{\mathsf{T}}\times 10^{-6}N⋅\cdotm[0∘​10∘​1∘]𝖳\big[0^{\circ}\,\,\,10^{\circ}\,\,\,1^{\circ}\big]^{\mathsf{T}}[7.43∘7.43^{\circ},25.57∘25.57^{\circ}][1.33−0.64   143.46]𝖳×10−4\big[1.33\,\,\,-0.64\,\,\,143.46\big]^{\mathsf{T}}\times 10^{-4}N[238.36−628.25−3.11]𝖳×10−6\big[238.36\,\,\,-628.25\,\,\,-3.11\big]^{\mathsf{T}}\times 10^{-6}N⋅\cdotm[0∘​15∘​1∘]𝖳\big[0^{\circ}\,\,\,15^{\circ}\,\,\,1^{\circ}\big]^{\mathsf{T}}[3.62∘3.62^{\circ},61.96∘61.96^{\circ}][0.34−0.64   145.39]𝖳×10−4\big[0.34\,\,\,-0.64\,\,\,145.39\big]^{\mathsf{T}}\times 10^{-4}N[239.98−161.19−0.80]𝖳×10−6\big[239.98\,\,\,-161.19\,\,\,-0.80\big]^{\mathsf{T}}\times 10^{-6}N⋅\cdotm

The AMT and RCD actuation is as discussed in Section2.4.
The AMT has a translation limit of𝐮maxAMT=−𝐮minAMT=[0.29   0.29]𝖳\mbf{u}^{\text{AMT}}_{\text{max}}=-\mbf{u}^{\text{AMT}}_{\text{min}}=\Big[0.29\,\,\,0.29\Big]^{\mathsf{T}}m and a rate limit of𝐮˙maxAMT=−𝐮˙minAMT=[0.5   0.5]𝖳\dot{\mbf{u}}^{\text{AMT}}_{\text{max}}=-\dot{\mbf{u}}^{\text{AMT}}_{\text{min}}=\Big[0.5\,\,\,0.5\Big]^{\mathsf{T}}mm/s in theb→1\underrightarrow{b}^{1}andb→2\underrightarrow{b}^{2}axes(Johnson and Curran,2020).
The discrete-time rate constraint is defined as𝐮˙maxAMT=−𝐮˙minAMT=(𝐮𝐣+𝟏|𝐭𝐤AMT−𝐮𝐣|𝐭𝐤AMT)/𝚫​𝐭\dot{\mbf{u}}^{\text{AMT}}_{\text{max}}=-\dot{\mbf{u}}^{\text{AMT}}_{\text{min}}=(\mbf{u}^{\text{AMT}}_{j+1|t_{k}}-\mbf{u}^{\text{AMT}}_{j|t_{k}})/\Delta t, which limits the maximum AMT position change to be0.050.05m in each axis at every momentum management time step. In the simulation (d​t=1\textrm{d}t=1second), the AMT is actuated to move at its maximum rate towards the momentum management commanded position (updated everyΔ​t=100\Delta t=100seconds) in each of its axis until reaching the commanded position. The roll torque generated when the RCDs are turned on is set to meet the Solar Cruiser’s roll torque requirement as defined in Eq. (8).

The Kalman filter measurement noise covariance is chosen based on NASA Solar Cruiser’s performance requirement(Johnson and Curran,2020).
It is assumed that the onboard ADCS measurement noise standard deviation is 3 times smaller (more accurate) than the standard deviation of control requirement defined byJohnson and Curran (2020).
Based on the required pointing accuracy of<60<60arcsec in pitch/yaw and<6.8<6.8arcmin in roll (3​σ3\sigma), the standard deviation of attitude measurement noise is chosen as0.00186∘0.00186^{\circ}in pitch/yaw and0.0125∘0.0125^{\circ}in roll, i.e.,𝝈θ=diag​(0.00186∘,0.00186∘,0.0125∘){\boldsymbol{\sigma}}_{\theta}=\text{diag}(0.00186^{\circ},0.00186^{\circ},0.0125^{\circ}).
Based on the pointing jitter requirements of<10<10arcsec/sec in pitch/yaw and<1.34<1.34arcmin/sec in roll (3​σ3\sigma), the standard deviation of angular rate measurement noise is chosen as0.0003060.000306deg/sec in pitch/yaw and0.00250.0025deg/sec in roll, i.e.,𝝈ω=diag​(0.000306,0.000306,0.0025){\boldsymbol{\sigma}}_{\omega}=\text{diag}(0.000306,0.000306,0.0025)deg/sec.
It is assumed that the RW angular momentum measurement accuracy is𝝈h=10−5⋅𝟏𝟑×𝟑{\boldsymbol{\sigma}}_{h}=10^{-5}\cdot\mbf{1}_{3\times 3}N⋅\cdotm⋅\cdots, and𝝈e=10−8⋅𝟏𝟑×𝟑{\boldsymbol{\sigma}}_{e}=10^{-8}\cdot\mbf{1}_{3\times 3}rad⋅\cdots, as these parameters are not publicly available in the literature.
The collective measurement noise covariance is given by𝐑KF=diag​(𝐫θ,𝐫ω,𝐫𝐡,𝐫𝐞)=diag​(𝝈θ𝟐,𝝈ω𝟐,𝝈𝐡𝟐,𝝈𝐞𝟐)\mbf{R}^{\text{KF}}=\text{diag}(\mbf{r}_{\theta},\mbf{r}_{\omega},\mbf{r}_{h},\mbf{r}_{e})=\text{diag}({\boldsymbol{\sigma}}_{\theta}^{2},{\boldsymbol{\sigma}}_{\omega}^{2},{\boldsymbol{\sigma}}_{h}^{2},{\boldsymbol{\sigma}}_{e}^{2}).
In the simulation, zero-mean Gaussian white noise with the same measurement covariance is added to each of the measurement parameters in Kalman filter measurement update step.

The Kalman filter process noise covariance is given by𝐐KF=diag​(𝐐modelKF,𝐐distKF)\mbf{Q}^{\text{KF}}=\text{diag}(\mbf{Q}^{\text{KF}}_{\text{model}},\mbf{Q}^{\text{KF}}_{\text{dist}}), which is largely a tuning parameter of the filter.
The dynamic model error covariance𝐐modelKF=diag​(0.01𝟐⋅𝟏𝟑×𝟑,0.0001𝟐⋅𝟏𝟑×𝟑,𝟏𝟎−𝟔⋅𝟏𝟑×𝟑,𝟏𝟎−𝟏𝟔⋅𝟏𝟑×𝟑)\mbf{Q}^{\text{KF}}_{\text{model}}=\text{diag}(0.01^{2}\cdot\mbf{1}_{3\times 3},0.0001^{2}\cdot\mbf{1}_{3\times 3},10^{-6}\cdot\mbf{1}_{3\times 3},10^{-16}\cdot\mbf{1}_{3\times 3}), whose units are deg2,deg/2{}^{2}/s2,(N⋅\cdotm⋅\cdots)2, and (rad⋅\cdots)2, characterizes the combination of linearization error in the dynamics and expected deviations in the trajectory.
The disturbance model error covariance𝐐distKF=diag​(𝐪τ,𝟏+ξ𝟏​ω𝐝,𝟏𝟐,𝐪τ,𝟐+ξ𝟐​ω𝐝,𝟐𝟐,𝐪τ,𝟑+ξ𝟑​ω𝐝,𝟑𝟐)\mbf{Q}^{\text{KF}}_{\text{dist}}=\text{diag}({q}_{\tau,1}+\xi_{1}\omega_{d,1}^{2},{q}_{\tau,2}+\xi_{2}\omega_{d,2}^{2},{q}_{\tau,3}+\xi_{3}\omega_{d,3}^{2})has static covarianceqτ,1=qτ,2=5×10−6{q}_{\tau,1}={q}_{\tau,2}=5\times 10^{-6},qτ,3=5×10−9{q}_{\tau,3}=5\times 10^{-9}, and dynamic covariance scaling parametersξ1=ξ2=0.5\xi_{1}=\xi_{2}=0.5,ξ3=0.1\xi_{3}=0.1. The dynamic covariance parameters account for the fact that the attitude, and thus, the disturbance torques, are expected to deviate more quickly when performing a slew maneuver. The resulting covariance𝐐distKF=diag​(𝟓×𝟏𝟎−𝟔+12​ω𝐝,𝟏𝟐,𝟓×𝟏𝟎−𝟔+12​ω𝐝,𝟐𝟐,𝟓×𝟏𝟎−𝟗+0.1​ω𝐝,𝟑𝟐)\mbf{Q}^{\text{KF}}_{\text{dist}}=\text{diag}(5\times 10^{-6}+\mbox{$\textstyle{\frac{1}{2}}$}\omega_{d,1}^{2},5\times 10^{-6}+\mbox{$\textstyle{\frac{1}{2}}$}\omega_{d,2}^{2},5\times 10^{-9}+0.1\omega_{d,3}^{2})N⋅\cdotm2characterizes the slowly-varying nature of the disturbance estimate and the other model discrepancies captured by𝐰^\hat{\mbf{w}}.
The initial state estimate𝐗^0−=𝟎\hat{\mbf{X}}^{-}_{0}=\mbf{0}does not consider any preliminary information of the state and disturbance error.
The initial estimation error covariance is chosen as𝐏𝟎−=diag​(𝟏𝟎𝟎​𝐐modelKF,diag​(𝟏𝟎𝟑,𝟏𝟎𝟑,𝟏𝟎𝟗)​𝐐distKF)\mbf{P}_{0}^{-}=\text{diag}(100\mbf{Q}^{\text{KF}}_{\text{model}},\text{diag}(10^{3},10^{3},10^{9})\mbf{Q}^{\text{KF}}_{\text{dist}})to allow initial estimate correction.

In this work, the Kalman filter operates at the same frequency as the momentum management system, which has a time step of100100seconds.
The system undergoes an initial slew of attitude tracking, and the Kalman filter acquires its first measurement update at the first momentum management timestep, i.e.,tk=100t_{k}=100sec.
After the measurement update, the momentum management policy determines the associated AMT and RCD inputs, which are then used in the time update using the Kalman filter process model.
The momentum management input commands are passed through the AMT and RCD actuation dynamics as discussed in Section2.4, and then applied to the nonlinear dynamics as in Eq. (1) until the next momentum management timestep. The process of a measurement update, momentum management input determination, time update, and application of the input to the nonlinear system is repeated.

## 5.2NASA’s State-of-the-art Method

NASA’s state-of-the-art momentum management strategy used on Solar Cruiser is establishes as a benchmark comparison to the proposed MPC strategy.
The Solar Cruiser momentum management system utilizes three threshold-based decoupled channels to command the AMT and RCDs(Inness et al.,2023; Tyler et al.,2023).
Solar Cruiser employs on-off thresholds for both AMT and RCD activation, which are based on the RWs’ stored angular momentum in the pitch/yaw and roll axes. An upper activation threshold is set higher than a lower deactivation threshold, establishing a hysteresis.
Specifically, an actuator engages only when its corresponding RW momentum exceeds the activation threshold and remains active until the momentum drops below the deactivation threshold.

The two AMT axes (pitch and yaw) are controlled independently via PID control laws, which regulate the accumulated angular momentum stored in the corresponding RWs. The control laws for the two axes are defined asu1AMT\displaystyle u^{\text{AMT}}_{1}=KpAMT​hb​2RW+KdAMT​h˙b​2RW+KiAMT​∫t0thb​2RW​(τ)​d​τ,\displaystyle=K^{\text{AMT}}_{p}h^{\text{RW}}_{b2}+K^{\text{AMT}}_{d}\dot{h}^{\text{RW}}_{b2}+K^{\text{AMT}}_{i}\int^{t}_{t_{0}}h^{\text{RW}}_{b2}(\tau)\textrm{d}\tau,u2AMT\displaystyle u^{\text{AMT}}_{2}=−KpAMT​hb​1RW−KdAMT​h˙b​1RW−KiAMT​∫t0thb​1RW​(τ)​d​τ.\displaystyle=-K^{\text{AMT}}_{p}h^{\text{RW}}_{b1}-K^{\text{AMT}}_{d}\dot{h}^{\text{RW}}_{b1}-K^{\text{AMT}}_{i}\int^{t}_{t_{0}}h^{\text{RW}}_{b1}(\tau)\textrm{d}\tau.

The sign difference between the two PID control laws reflects the dynamics in Eq. (1), where the AMT-induced torque𝝉bAMT=msmp+ms​𝐫𝐛𝐩𝐬×​𝐟𝐛SRP{\boldsymbol{\tau}}_{b}^{\text{AMT}}=\frac{m_{s}}{m_{p}+m_{s}}\mbf{r}_{b}^{ps^{\times}}\mbf{f}_{b}^{\text{SRP}}involves a cross product with opposite signs along the body 1 and 2 axes.
This control input is updated with a time step ofΔ​t=100\Delta t=100sec using a ZOH to maintain a constant command throughout the interval.
The RCDs’ actuation follows a simple on-off logic with a fixed torque magnitude when activated. The RCD activation/deactivation switch aligns with the momentum management time stepΔ​t\Delta t.

This threshold-based control, along with the AMT PID gains, is tuned via simulation to optimize performance.
Crucially, this PID control framework does not inherently account for physical actuator constraints, such as AMT position and rate limits. These limits are enforced externally after the PID controller determines the position command. Consequently, tuning the controller to ensure effective momentum management while avoiding actuator saturation remains a key design challenge.

In the absence of any numerical values in the work ofInness et al. (2023); Tyler et al. (2023), values are chosen in this paper in an attempt to recreate the results ofInness et al. (2023); Tyler et al. (2023). To this end, the chosen thresholds for the AMT are0.250.25N⋅\cdotm⋅\cdots for activation, and0.1250.125N⋅\cdotm⋅\cdots for deactivation.
The PID gains of the AMT controller are chosen asKpAMT=0.1K^{\text{AMT}}_{p}=0.1(N⋅\cdots)-1,KdAMT=0.05K^{\text{AMT}}_{d}=0.05N-1, andKiAMT=0.0001K^{\text{AMT}}_{i}=0.0001N-1s-2.
The maximum position constraint of the AMT is enforced such that|uiAMT|=ui,maxAMT=0.29|u^{\text{AMT}}_{i}|=u^{\text{AMT}}_{i,\text{max}}=0.29m when the determined PID controller input satisfies|uiAMT|>ui,maxAMT|u^{\text{AMT}}_{i}|>u^{\text{AMT}}_{i,\text{max}}(i=1,2i=1,2).
The maximum AMT rate constraint is enforced such that|uiAMT|=Δ​t⋅u˙i,maxAMT=0.05|u^{\text{AMT}}_{i}|=\Delta t\cdot\dot{u}^{\text{AMT}}_{i,\text{max}}=0.05m when the determined PID input satisfies|uiAMT|>Δ​t⋅u˙i,maxAMT|u^{\text{AMT}}_{i}|>\Delta t\cdot\dot{u}^{\text{AMT}}_{i,\text{max}}(i=1,2i=1,2).
The chosen RCD thresholds are0.1250.125N⋅\cdotm⋅\cdots for activation, and0.3120.312N⋅\cdotm⋅\cdots for deactivation.

For practicality and for a fair comparison to the proposed method, the threshold-based momentum management uses state estimates from the Kalman filter to determine AMT and RCD inputs. Specifically, the angular momentum estimate𝐡^b,kRW+\hat{\mbf{h}}_{b,k}^{\text{RW}^{+}}is used to assess the activation/deactivation threshold and AMT proportional control, and𝐡˙^b,kRW+=𝐊𝐩​(𝜽^𝐤+−𝜽𝐝)+𝐊𝐝​(𝝎^𝐛,𝐤𝐛𝐚+−𝝎𝐝)+𝐊𝐢​𝐞^𝐤int+\hat{\dot{\mbf{h}}}_{b,k}^{\text{RW}^{+}}=\mbf{K}_{p}(\hat{{\boldsymbol{\theta}}}^{+}_{k}-{\boldsymbol{\theta}}_{d})+\mbf{K}_{d}(\hat{{\boldsymbol{\omega}}}^{{ba}^{+}}_{b,k}-{\boldsymbol{\omega}}_{d})+\mbf{K}_{i}\hat{\mbf{e}}^{\text{int}^{+}}_{k}is used for the AMT derivative control. For the AMT integral control, it is assumed that a perfect measurement of∫t0t𝐡𝐛RW​(τ)​d​τ\int^{t}_{t_{0}}\mbf{h}^{\text{RW}}_{b}(\tau)\textrm{d}\tauis accessible in the ADCS.(a)attitude(b)4 RWs angular momentum(c)body-frame RWs angular momentum(d)momentum management inputsFigure 5:Simulation results using NASA’s Solar Cruiser momentum management strategy fromInness et al. (2023); Tyler et al. (2023), featuring RW saturation under a slew of𝜽goal=[0∘​10∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}trajectory compared to a𝜽goal=[0∘​10.5∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10.5^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}trajectory. The black dashed line in (c) denotes the activation threshold (50%50\%of the soft constraint in MPC) , and the green dashed line denotes the deactivation threshold (50%50\%of the activation threshold).

Using NASA’s state-of-the-art thresholding momentum management policy, a maneuver sequence tracking initial attitude of𝜽0=𝟎{\boldsymbol{\theta}}_{0}=\mbf{0}to𝜽goal=[0∘​10∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}is performed, following the desired hold-slew-hold-slew-hold trajectory.
As shown in Fig.5with the label “NASA,” the maneuver demonstrates effective momentum management, where the steady-state performance is similar to that shown byInness et al. (2023); Tyler et al. (2023), although this is difficult to compare quantitatively due to redacted plot axes.
The momentum management method developed byInness et al. (2023); Tyler et al. (2023)is effective at keeping the angular momentum of the RWs within reasonable bounds with realistic actuation inputs.
However, with a slightly larger slew maneuver with𝜽goal=[0∘​10.5∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10.5^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}, the system suffers from RW saturation, and the solar sail loses attitude control authority, which is shown in the result of Fig.5with the label “NASA-sat.”
For reference, the black dashed lines in Fig.5(b)indicate25%25\%of the angular momentum capacity of each RW, which is also the soft constraint value chosen for the proposed MPC-based approach in the following sections.
The black dashed lines in Fig.5(c)indicate the activation thresholds, while the green dashed lines represent the deactivation thresholds.

## 5.3Proposed MPC-based Momentum Management Supported by KF Disturbance Estimate

While Solar Cruiser’s momentum management method failed to desaturate the RWs and eventually lost attitude control when performing the larger slew, the proposed MPC-based momentum management strategy has the potential to foresee the upcoming angular momentum growth and proactively take actions. This allows for more aggressive slews while maintaining RW control authority.

To highlight this improved performance, simulations of a larger slew maneuver are performed, regulating the reference trajectory of𝜽0=𝟎{\boldsymbol{\theta}}_{0}=\mbf{0}and𝜽goal=[0∘​15∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,15^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}with the RW PID control law, while the stored RW angular momentum is unloaded by the momentum management MPC policy outlined in Section4. The system parameters and Kalman filter parameters are the same as presented in Section5.1.
The MPC prediction horizon is chosen asN=10N=10timesteps, corresponding to a10001000sec forecast.
The state constraints in MPC are determined by mission requirements and RW limits, with the reference attitude tracking limit𝜽err=[5∘​5∘​5∘]𝖳{\boldsymbol{\theta}}_{\text{err}}=\Big[5^{\circ}\,\,\,5^{\circ}\,\,\,5^{\circ}\Big]^{\mathsf{T}}, the angular velocity tracking limit𝝎err=[0.1   0.1   0.1]𝖳{\boldsymbol{\omega}}_{\text{err}}=\Big[0.1\,\,\,0.1\,\,\,0.1\Big]^{\mathsf{T}}deg/s, the RW angular momentum capacity𝐡𝟒,maxRW=−𝐡𝟒,minRW=[1   1   1   1]𝖳\mbf{h}^{\text{RW}}_{4,\text{max}}=-\mbf{h}^{\text{RW}}_{4,\text{min}}=\Big[1\,\,\,1\,\,\,1\,\,\,1\Big]^{\mathsf{T}}N⋅\cdotm⋅\cdots, and a large PID integral term𝐞maxint=−𝐞minint=[𝟏𝟎𝟔​10𝟔​10𝟔]𝖳\mbf{e}^{\text{int}}_{\text{max}}=-\mbf{e}^{\text{int}}_{\text{min}}=\Big[10^{6}\,\,\,10^{6}\,\,\,10^{6}\Big]^{\mathsf{T}}rad⋅\cdots as an internal state limit.
The attitude and angular rate constraints are set to arbitrarily large limits for design completeness and flexibility, ensuring the framework can accommodate future mission requirements that may involve more aggressive maneuvers.
The soft constraint limits are chosen as25%25\%of the RWs angular momentum capacity, i.e.,𝐡𝟒,maxsoft=0.25⋅𝐡𝟒,maxRW\mbf{h}_{4,\text{max}}^{\text{soft}}=0.25\cdot\mbf{h}^{\text{RW}}_{4,\text{max}}and𝐡𝟒,minsoft=−𝐡𝟒,maxsoft\mbf{h}_{4,\text{min}}^{\text{soft}}=-\mbf{h}_{4,\text{max}}^{\text{soft}}.
The slack variable𝜶≥𝟎{\boldsymbol{\alpha}}\geq\mbf{0}is penalized heavily by the weighting matrix𝐂=𝟏𝟎𝟎𝟎𝟎⋅𝟏𝟒×𝟒\mbf{C}=10000\cdot\mbf{1}_{4\times 4}in the objective function when𝐡𝟒,𝐣|𝐭𝐤RW\mbf{h}^{\text{RW}}_{4,j|t_{k}}deviates from the soft constraint envelope.
The weights in the MPC objective function are provided in Table3, which are parameters that can be tuned to tailor the performance objective to different mission stages and scenarios.Table 3:MPC tuning parameters used in the numerical simulations.ParameterValueNN1010𝐐\mbf{Q}diag​(10⋅𝟏𝟔×𝟔,0.5⋅𝟏𝟒×𝟒,𝟎𝟑×𝟑)\text{diag}(10\cdot\mbf{1}_{6\times 6},0.5\cdot\mbf{1}_{4\times 4},\mbf{0}_{3\times 3})𝐐𝐍\mbf{Q}_{N}10⋅𝐐10\cdot\mbf{Q}𝐑\mbf{R}diag​(1,1,5×106)\text{diag}(1,1,5\times 10^{6})𝐑~\tilde{\mbf{R}}2000⋅𝟏𝟐×𝟐2000\cdot\mbf{1}_{2\times 2}𝐂\mbf{C}10000⋅𝟏𝟒×𝟒10000\cdot\mbf{1}_{4\times 4}

It is worth noting that the MPC evaluates RCD inputs as continuous values between±τb​3,onRCD\pm\tau^{\text{RCD}}_{b3,\text{on}}, but the actual applied input is quantized into the full on/off value with pulse lengthtct_{c}using PWM quantization as in Eq. (11).
The current SRP force𝐟𝐛SRP​(𝐭𝐤)\mbf{f}_{b}^{\text{SRP}}(t_{k})and RCD on torqueτb​3,onRCD​(tk)\tau^{\text{RCD}}_{b3,\text{on}}(t_{k})used in MPC are updated at every momentum management timesteptkt_{k}, while the Kalman filter provides the state and disturbance estimates. MPC’s assumption that these values are constant across the prediction horizon further shows the robustness of the proposed method.
The relaxation of the on-off RCD actuation constraints allows for the use of off-the-shelf QP solvers that can solve the optimization problem efficiently. The MATLAB functionquadprogwith its default settings is used. The mean QP solution time across600600momentum management timesteps is32.8632.86ms, and the numerical integration time for theN=10N=10LTV prediction model is39.8039.80ms, representing the average of five simulation sets of𝜽goal=[0∘​15∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,15^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}maneuver. For reference, these computations are performed on a desktop computer with a 13th Gen Intel Core i5-13400 @ 2.5 GHz with 24 GB memory and the code is run in Matlab 2024b.

To demonstrate the importance of disturbance knowledge in the MPC framework, simulation results with and without the Kalman filter disturbance estimate knowledge in MPC are shown in Fig.6, where no threshold is used (βthreshAMT=βthreshRCD=0\beta^{\text{AMT}}_{\text{thresh}}=\beta^{\text{RCD}}_{\text{thresh}}=0).
The result in blue labeled “nominalMPC” uses the nominal MPC implementation without disturbance knowledge, where the MPC prediction model uses𝐰𝐣|𝐭𝐤=𝟎\mbf{w}_{j|t_{k}}=\mbf{0}, forj=0,1,…,N−1j=0,1,\ldots,N-1. The result in red labeled “KFMPC” includes the Kalman filter estimate disturbance within the MPC prediction model, where𝐰𝐣|𝐭𝐤=𝐰^𝐤+\mbf{w}_{j|t_{k}}=\hat{\mbf{w}}^{+}_{k}, forj=0,1,…,N−1j=0,1,\ldots,N-1.
Although both of the MPC policies perform successful momentum management under an attitude hold at𝜽0=𝜽goal=[0∘​10∘​1∘]𝖳{\boldsymbol{\theta}}_{0}={{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}, the nominal MPC results in the angular momentum of two RWs stabilizing near their saturation limits.
Conversely, the MPC implementation incorporating the disturbance estimate exhibits a significant performance improvement, driving all RW angular momentum down to values safely within the specified soft constraint boundaries, thereby reserving greater control authority. An attitude hold at𝜽=𝟎{\boldsymbol{\theta}}=\mbf{0}(which has a higher disturbance torque) and other slew maneuvers have been tested without the disturbance estimate, all of which resulted in RW saturation and instability.
This further shows that the disturbance estimate is critical to the performance of MPC-based momentum management.(a)attitude(b)4 RWs angular momentum(c)body-frame RWs angular momentum(d)momentum management inputsFigure 6:Simulation results using the proposed MPC momentum management strategy under an attitude hold of𝜽0=𝜽goal=[0∘​10∘​1∘]𝖳{\boldsymbol{\theta}}_{0}={{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}with and without (nominal) the disturbance estimate knowledge in prediction model. The black dashed lines in (b) denote the25%25\%soft constraint on 4-RWs angular momentum.

The proposed MPC policy with Kalman filter estimation framework is used to perform the maneuver sequence tracking initial attitude of𝜽0=𝟎{\boldsymbol{\theta}}_{0}=\mbf{0}to𝜽goal=[0∘​15∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,15^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}, following the desired hold-slew-hold-slew-hold trajectory. An additional actuation threshold can be applied on the MPC inputs to filter out minor actuation with minimal loss in momentum management performance.
Leveraging the recursive nature of the MPC, an input activation threshold is applied to trim out minor actuation demanded by MPC, and further improve actuator efficiency and mitigate noise.
A set of results are presented in Fig.7, demonstrating the design choice of actuation thresholds.
The result in blue (labeled “MPC-thrA2R6”) uses a20%20\%AMT threshold (βthreshAMT=0.2\beta^{\text{AMT}}_{\text{thresh}}=0.2) and60%60\%RCD threshold (βthreshRCD=0.6\beta^{\text{RCD}}_{\text{thresh}}=0.6), which means that when MPC demands an AMT input less than20%20\%of the distance the AMT can move in one direction in one time step (20%20\%of0.050.05m), the AMT is held at its current position for the next time step, and the RCD input is set to zero when the MPC-demanded input is less than60%60\%of the RCD “on” torque value.
The result in red (labeled “MPC-thrA3R9”) uses a30%30\%AMT threshold (βthreshAMT=0.3\beta^{\text{AMT}}_{\text{thresh}}=0.3) and90%90\%RCD threshold (βthreshRCD=0.9\beta^{\text{RCD}}_{\text{thresh}}=0.9) on the MPC-demanded inputs.
Figures7(a)and7(b)show that the design choice of the applied thresholds do not degrade momentum management performance, which is further illustrated in the plot of the control inputs in Fig.7(c)and the zoomed in control input plot of Fig.7(d).
A comparison of actuation usage among the the three MPC policies with different actuation threshold performing the15∘15^{\circ}slew maneuver sequence over6000060000seconds is included in Table4.
The performance metric of control actuation effort is evaluated by the number of RCD on-off cycles, the total time the RCDs are turned “on”, the total AMT travel distance in each translation axis, and the sum of the total AMT travel distance across both axes. The design choice of thresholdsβthreshAMT\beta^{\text{AMT}}_{\text{thresh}}andβthreshRCD\beta^{\text{RCD}}_{\text{thresh}}can be determined by the operational characteristics and the expected lifetime of the actuators.(a)body-frame RWs angular momentum(b)4 RWs angular momentum(c)momentum management inputs(d)momentum management inputs (zoomed in)Figure 7:Threshold tuning of the proposed MPC framework under a maneuver sequence tracking initial attitude𝜽0=𝟎{\boldsymbol{\theta}}_{0}=\mbf{0}to𝜽goal=[0∘​15∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,15^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}and return, using20%20\%AMT threshold and60%60\%RCD threshold (blue), and using30%30\%AMT threshold and90%90\%RCD threshold (red). The zoomed-in plot in (d) demonstrates the control inputs between90009000to1300013000seconds of forward slew maneuver and the PWM-quantized RCD actuation pulsing at every time step.Table 4:Momentum management control actuation usage of the proposed MPC policy under different actuation threshold tuning.AMT/RCD ThresholdAMT 10% / RCD 30%AMT 20% / RCD 60%AMT 30% / RCD 90%RCD Cycle (#\#)422812RCD On Time (sec)631655544989AMT Dist 1 (cm)220.52235.25241.13AMT Dist 2 (cm)152.24147.82144.74Sum of AMT Dist (cm)372.76383.07385.87

Figure8illustrates the disturbance torque estimates generated by the Kalman filter for the three MPC test cases.
The black dashed lines are the true disturbances, accounting for the torque generated by the SRP due to the non-ideal sail shape and the solar sail’s attitude. The forward slew and return slew are initiated at1000010000and2000020000seconds respectively, which results in the change of SRP disturbance torque.
While the exact magnitude of the estimated disturbance torque does not exactly match the true disturbance torque, the estimate is reasonably accurate, and clearly assists with the MPC-based momentum management strategy, as shown in Fig.6.
It is worth noting that the disturbance torque estimate generated by the Kalman filter will account for all model inaccuracies in practice (e.g., nonlinearities, discretization approximations), which could explain the difference between the estimated and true disturbance torque. The disturbance torque in roll axis has a significantly smaller magnitude than the pitch/yaw axes and the other state estimates, making it difficult to observe and sensitive to measurement noise. However, the roll disturbance estimate still converges within the neighborhood of the true value, and allows MPC to adjust accordingly. Future work will investigate improving the observability of the roll disturbance estimate, through the use of more accurate measurements or the introduction of additional measurements.

Given the prediction model being linearized about the nominal slew trajectory, the MPC policies proactively take momentum management actuation once the slew maneuver arises in the prediction horizon (1000 seconds ahead in this case).
Within the MPC formulation, the RCD torque magnitude, SRP force, estimated disturbance torque are assumed constant, with the AMT actuation modeled as a ZOH. In contrast, the simulation incorporates the nonlinear attitude dynamics, AMT motion dynamics, and the attitude-dependent nature of the SRP force, torque, and RCD effects. Despite the simplifications in the prediction model of MPC (which improves real-time feasibility), the recursive nature allows the controller to compensate for these discrepancies at every time step, demonstrating significant robustness against model uncertainties.Figure 8:Kalman filter disturbance estimate values used in the MPC momentum management with10%10\%AMT and30%30\%RCD threshold (blue),20%20\%AMT and60%60\%RCD threshold (red), and30%30\%AMT and90%90\%RCD threshold (yellow). The black dashed line indicates the true SRP disturbance torque.

## 5.4State-of-the-Art Comparison

A maneuver sequence tracking initial attitude of𝜽0=𝟎{\boldsymbol{\theta}}_{0}=\mbf{0}to𝜽goal=[0∘​10∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}following the desired hold-slew-hold-slew-hold trajectory is executed using the MPC framework to directly compare its actuation efficiency to that of NASA’s state-of-the-art method(Inness et al.,2023; Tyler et al.,2023).
This threshold-based control policy is a recreation of the momentum management logic for Solar Cruiser based on the information provided byInness et al. (2023); Tyler et al. (2023). While it serves as a functional approximation for the purposes of this study, it is not an exact replica the proprietary controller implemented on NASA’s flight hardware.
For this simulation, MPC uses the same tuning parameters as the simulations in Fig.7with30%30\%AMT threshold and90%90\%RCD threshold.

Figure9includes the comparison of simulation results using NASA’s method(Inness et al.,2023; Tyler et al.,2023)and the proposed MPC approach with thresholds.
In Fig.9(d), the MPC proactively actuates the AMT and RCDs to avoid angular momentum growth, as shown in Figures9(b)and9(c).
A quantitative comparison of the control actuation usage is included in Table5.
The proposed MPC policy achieves a significant reduction in AMT and RCD usage during the attitude hold. In contrast, a higher actuation usage during the slew maneuver provides a significantly more effective momentum management and a broader operation region (i.e., a larger range of slew maneuvers in which momentum management can be effectively performed.
The PWM-quantization evenly distributes the input across every time step, as opposed to the longer singular “on” pulse with a long “off” period when using NASA’s benchmark method.
Although the MPC results in higher RCD on-off cycles due to this inherent PWM quantization, dividing a long activation command into multiple short pulses is not inherently detrimental, as it mitigates the risk of potentially overheating the actuator associated with excessively long RCD “on” commands. Future work could investigate the design of an actuation mechanism capable of grouping these short MPC-generated pulses into a single, longer RCD activation event according to the mission requirements and hardware limitations.(a)attitude(b)4 RWs angular momentum(c)body-frame RWs angular momentum(d)momentum management inputsFigure 9:Comparison of simulation results using the proposed MPC momentum management strategy versus NASA’s state-of-the-art method under a maneuver sequence tracking initial attitude𝜽0=𝟎{\boldsymbol{\theta}}_{0}=\mbf{0}to𝜽goal=[0∘​10∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}and return.Table 5:Control actuation usage with NASA Solar Cruiser’s state-of-the-art momentum management method and the proposed MPC method with30%30\%AMT and90%90\%RCD threshold under a maneuver sequence from𝜽0=𝟎{\boldsymbol{\theta}}_{0}=\mbf{0}to𝜽goal=[0∘​10∘​1∘]𝖳{{\boldsymbol{\theta}}}_{\text{goal}}=\Big[0^{\circ}\,\,\,10^{\circ}\,\,\,1^{\circ}\Big]^{\mathsf{T}}and return.TimeSlew Maneuver (0-30000 s)Attitude Hold (30000-60000 s)ControllerSolar CruiserMPC w/ ThresholdSolar CruiserMPC w/ ThresholdRCD Cycle (#\#)51010RCD On Time (sec)3900469517000AMT Dist 1 (cm)171.48208.7563.269.53AMT Dist 2 (cm)62.24142.2262.0512.65Sum of AMT Dist (cm)233.72350.97125.3122.18

## 6Conclusions

This paper presented a novel Kalman filter augmented MPC framework specifically designed for the challenging momentum management task of NASA’s Solar Cruiser. The integrated estimation framework proposed in this work plays a crucial role, providing real-time state and disturbance estimates that not only characterize the external disturbance torque but also capture the dynamic discrepancies between the linear prediction model and the highly nonlinear spacecraft system. This estimate closes the modeling gap needed to enable model predictive control for this momentum management application. Building upon a previously-developed MPC architecture(Shen and Caverly,2026), the policy was rigorously formulated to be computationally feasible, utilizing off-the-shelf QP solvers to ensure real-time implementation capability within the limited onboard hardware. Validation with a more realistic SRP model, while performing slew maneuver following and incorporating Solar Cruiser’s 4-RW configuration in this paper presents a key contribution towards the development of a practical implementation of the proposed MPC-based momentum management policy.

Simulation results demonstrated the proposed MPC-based momentum management policy’s superior performance and robustness. The disturbance estimate was shown to be essential in achieving reliable MPC prediction and bounded momentum management. Furthermore, the proposed MPC policy successfully managed angular momentum growth under maneuvers that exceed the capability of NASA’s state-of-the-art method designed for Solar Cruiser, establishing a larger operational slew envelope. It is shown that the MPC policy proactively unloads angular momentum in preparation for upcoming high-demand slew maneuvers. The framework also proved its efficiency by demonstrating reduced actuator usage through a lower AMT travel distance and optimized RCD usage compared to the benchmark method. This improvement has the potential to enable greater solar sail mission longevity.

Future work on this topic could be the investigation of improving roll disturbance estimates and reducing the number of RCD on-off cycles. Additional work towards the implementation of the proposed method on flight hardware and software will also be pursued to move towards its implementation on future solar sail missions.

## Acknowledgments

This material is based upon work supported by NASA under award No. 80NSSC25M7060, as well as a study grant from Chung Cheng Institute of Technology, National Defense University, Taiwan (R.O.C.). The authors would like to thank Mr. Keegan R. Bunker for the valuable discussions on sail shape modeling and providing the SRP model used in this work.

## Appendix: Reference Trajectory

For the reference maneuver in this work, the design variables include the initial attitude𝜽0{\boldsymbol{\theta}}_{0}, the predetermined goal attitude𝜽goal{\boldsymbol{\theta}}_{\text{goal}}, the maximum allowable slew rate𝜽˙slew≥𝟎\dot{{\boldsymbol{\theta}}}_{\text{slew}}\geq\mbf{0}, and the acceleration timetaccelt_{\text{accel}}required to reach the maximum slew rate. The slew maneuver is classified into acceleration, coast, and deceleration phases for both the forward maneuver start attstartt_{\text{start}}and the return maneuver initiating attreturnt_{\text{return}}.

The reference trajectory holds at its initial state𝜽d​(t)=𝜽0{\boldsymbol{\theta}}_{d}(t)={\boldsymbol{\theta}}_{0}and𝜽˙d​(t)=𝟎\dot{{\boldsymbol{\theta}}}_{d}(t)=\mbf{0}fort<tstartt<t_{\text{start}}.
The system then starts the forward maneuver, slewing toward𝜽goal{\boldsymbol{\theta}}_{\text{goal}}, attstartt_{\text{start}}.
The constant design variables𝜽˙slew\dot{{\boldsymbol{\theta}}}_{\text{slew}}andtaccelt_{\text{accel}}define a constant angular acceleration magnitude|θ¨d,i|=θ˙slew,i/taccel|\ddot{\theta}_{d,i}|=\dot{\theta}_{\text{slew},i}/t_{\text{accel}}for theii-th axis.
During the acceleration phase wheret−tstart<taccelt-t_{\text{start}}<t_{\text{accel}}, the angular rate magnitude increases linearly following|θ˙d,i|=|θ¨d,i|​(t−tstart)|\dot{\theta}_{d,i}|=|\ddot{\theta}_{d,i}|(t-t_{\text{start}}).
Concurrently, the desired attitude evolves quadratically from the initial state asθd,i=θ0,i±12​|θ¨d,i|​(t−tstart)2\theta_{d,i}=\theta_{0,i}\pm\frac{1}{2}|\ddot{\theta}_{d,i}|(t-t_{\text{start}})^{2}, where the±\pmsign depends on the slew direction defined byθ~i=θgoal,i−θ0,i\tilde{\theta}_{i}=\theta_{\text{goal},i}-\theta_{0,i}.
Once the maximum slew rate is reached, the system enters a coast phase where|θ˙d,i|=θ˙slew,i|\dot{\theta}_{d,i}|=\dot{\theta}_{\text{slew},i}is maintained.
The constant angular velocity is held fortcoast=2​θ~i/θ˙slew,i−2​taccelt_{\text{coast}}=2\tilde{\theta}_{i}/\dot{\theta}_{\text{slew},i}-2t_{\text{accel}}, until the remaining angular distance dictates the start of the deceleration phase.
During the deceleration phase, a constant negative acceleration of magnitude|θ¨d,i||\ddot{\theta}_{d,i}|is applied to smoothly bring the angular rateθ˙d,i\dot{\theta}_{d,i}back to zero exactly as the attitude reachesθgoal,i\theta_{\text{goal},i}.

The area under the angular velocity versus time plot denotes the total attitude angle change.
This integrated area matches the magnitude of slew angular displacement|θ~i||\tilde{\theta}_{i}|.
This geometric relationship establishes a strict kinematic constraint that dictates the angular velocity profile.
If the slew angle is large enough to complete the full acceleration and deceleration ramps, the standard trapezoidal profile is executed.
If the required slew angle is too small, the maximum slew rate cannot be achieved without overshooting the target. Under this condition, the reference trajectory degenerates into a triangular velocity profile. The system accelerates and shortly begins deceleration beforet=tstart+taccelt=t_{\text{start}}+t_{\text{accel}}without ever entering a constant velocity coast phase.
To satisfy the exact slew angle constraint, the acceleration duration for the degenerated triangular velocity profile is calculated astaccel​Δ=|θ~i|/|θ¨d,i|t_{\text{accel}\Delta}=\sqrt{|\tilde{\theta}_{i}|/|\ddot{\theta}_{d,i}|}. The peak angular rate of the slew is thereby reduced to|θ¨d,i|​taccel​Δ|\ddot{\theta}_{d,i}|t_{\text{accel}\Delta}.

Following the completion of the forward maneuver, the system settles and holds at the goal state𝜽d=𝜽goal{\boldsymbol{\theta}}_{d}={\boldsymbol{\theta}}_{\text{goal}},𝝎d=𝟎{\boldsymbol{\omega}}_{d}=\mbf{0}.
This reference orientation is maintained until the specified return timetreturnt_{\text{return}}triggers an identical but reversed kinematic sequence to drive the attitude from𝜽goal{\boldsymbol{\theta}}_{\text{goal}}back to the initial state𝜽0{\boldsymbol{\theta}}_{0}for the intervaltcomplete<t<treturnt_{\text{complete}}<t<t_{\text{return}}, wheretcomplete=tstart+|θ~i|/ωslew,i+taccelt_{\text{complete}}=t_{\text{start}}+|\tilde{\theta}_{i}|/\omega_{\text{slew},i}+t_{\text{accel}}when the slew angle is large enough to execute the standard trapezoidal profile, andtcomplete=tstart+2​taccel​Δt_{\text{complete}}=t_{\text{start}}+2t_{\text{accel}\Delta}when the slew angle is insufficient and the trajectory degenerates into a triangular profile. This desired slew maneuver trajectory is formulated as a function that calculates the associated reference𝜽d​(t){\boldsymbol{\theta}}_{d}(t),𝜽˙d​(t)\dot{{\boldsymbol{\theta}}}_{d}(t), and𝜽¨d​(t)\ddot{{\boldsymbol{\theta}}}_{d}(t)at any given timett. In the RW PID control law, the desired angular momentum is calculated as𝝎d​(t)=𝐒​(𝜽𝐝​(𝐭))​𝜽˙𝐝​(𝐭){\boldsymbol{\omega}}_{d}(t)=\mbf{S}({\boldsymbol{\theta}}_{d}(t))\dot{{\boldsymbol{\theta}}}_{d}(t), where the mapping matrix of a 3-2-1 Euler angle sequence is defined as𝐒​(𝜽)=[𝟏𝟎−sin⁡(θ𝟐)𝟎cos⁡(θ𝟏)sin⁡(θ𝟏)​cos⁡(θ𝟐)𝟎−sin⁡(θ𝟏)cos⁡(θ𝟏)​cos⁡(θ𝟐)].\mbf{S}({\boldsymbol{\theta}})=\begin{bmatrix}1&0&-\sin(\theta_{2})\\
0&\cos(\theta_{1})&\sin(\theta_{1})\cos(\theta_{2})\\
0&-\sin(\theta_{1})&\cos(\theta_{1})\cos(\theta_{2})\end{bmatrix}.

## References
- Ahmed et al. (2024)Ahmed, Z., Halefom, M.H.,
Woolsey, C., 2024.Tutorial review of indirect wind estimation methods
using small uncrewed air vehicles.Journal of Aerospace Information Systems
21, 667–683.doi:10.2514/1.I011345.
- Bellar et al. (2016)Bellar, A., Mohammed, M.A.S.,
Adnane, A., 2016.Minimum power consumption of the microsatellite
attitude control using pyramidal reaction wheel configuration, in:
8th International Conference on Modelling, Identification
and Control, pp. 253–257.doi:10.1109/ICMIC.2016.7804118.
- Berthet et al. (2024)Berthet, M., Schalkwyk, J.,
Çelik, O., Sengupta, D.,
Fujino, K., Hein, A.M.,
Tenorio, L., Cardoso dos Santos, J.,
Worden, S.P., Mauskopf, P.D.,
Miyazaki, Y., Funaki, I.,
Tsuji, S., Fil, P.,
Suzuki, K., 2024.Space sails for achieving major space exploration
goals: Historical review and future outlook.Progress in Aerospace Sciences
150, 101047.doi:10.1016/j.paerosci.2024.101047.
- Boni et al. (2023)Boni, L., Bassetto, M.,
Niccolai, L., Mengali, G.,
Quarta, A.A., Circi, C.,
Pellegrini, R.C., Cavallini, E.,
2023.Structural response of Helianthus solar sail during
attitude maneuvers.Aerospace Science and Technology
133, 108152.doi:10.1016/j.ast.2023.108152.
- Bunker and Caverly (2026)Bunker, K.R., Caverly, R.J.,
2026.Static and dynamic torque generation analysis of a
cable-actuated solar sail.Journal of Guidance, Control, and Dynamics ,
1–9doi:10.2514/1.G009590.
- Carzana et al. (2023)Carzana, L., Wilkie, W.K.,
Heaton, A., Diedrich, B.,
Heiligers, J., 2023.Solar-sail steering laws to calibrate the
accelerations from solar radiation pressure, planetary radiation pressure,
and aerodynamic drag, in: Proceedings of the 6th
International Symposium on Space Sailing, New York, NY.
pp. 58–65.Available athttps://www.citytech.cuny.edu/isss2023/docs/isss2023_proceedings.pdf.
- Caverly et al. (2020)Caverly, R., Di Cairano, S.,
Weiss, A., 2020.Electric satellite station keeping, attitude control,
and momentum management by MPC.IEEE Transactions on Control Systems Technology
29, 1475–1489.doi:10.1109/TCST.2020.3014601.
- Chen et al. (2023)Chen, T.Z., Liu, X., Cai,
G.P., You, C.L., 2023.Attitude and vibration control of a solar sail.Advances in Space Research 71,
4557–4567.doi:10.1016/j.asr.2023.01.039.
- Di Cairano and Kolmanovsky (2018)Di Cairano, S., Kolmanovsky, I.,
2018.Real-time optimization and model predictive control
for aerospace and automotive applications, in: American
Control Conference, pp. 2392–2409.doi:10.23919/ACC.2018.8431585.
- Eren et al. (2017)Eren, U., Prach, A.,
Koçer, B., Raković, S.,
Kayacan, E., Açıkmeşe, B.,
2017.Model predictive control in aerospace systems:
Current state and opportunities.Journal of Guidance, Control, and Dynamics
40, 1541–1566.doi:10.2514/1.G002507.
- Farres (2023)Farres, A., 2023.Propellant-less systems, in: Branz,
F., Cappelletti, C., Ricco, A.J.,
Hines, J.W. (Eds.), Next Generation
CubeSats and SmallSats. Elsevier, pp.
519–541.doi:10.1016/C2020-0-00508-6.
- Farrés et al. (2019)Farrés, A., Heiligers, J.,
Miguel, N., 2019.Road map tol4l_{4}/l5l_{5}with a solar sail.Aerospace Science and Technology
95, 105458.doi:https://doi.org/10.1016/j.ast.2019.105458.
- Firuzi and Gong (2018)Firuzi, S., Gong, S., 2018.Attitude control of a flexible solar sail in low
Earth orbit.Journal of Guidance, Control, and Dynamics
41, 1715–1730.doi:10.2514/1.G003178.
- Fu and Eke (2015)Fu, B., Eke, F.O., 2015.Attitude control methodology for large solar sails.Journal of Guidance, Control, and Dynamics
38, 662–670.doi:10.2514/1.G000048.
- Gauvain and Tyler (2023)Gauvain, B.M., Tyler, D.A.,
2023.A solar sail shape modeling approach for attitude
control design and analysis, in: Proceedings of the 6th
International Symposium on Space Sailing, New York, NY.
pp. 66–72.Available athttps://www.citytech.cuny.edu/isss2023/docs/isss2023_proceedings.pdf.
- Halverson et al. (2025)Halverson, R., Weiss, A.,
Lundin, G., Caverly, R.,
2025.Autonomous station keeping of satellites in
areostationary Mars orbit: A predictive control approach.Acta Astronautica 230,
1–15.doi:10.1016/j.actaastro.2025.01.064.
- Hayes and Caverly (2025)Hayes, A.D., Caverly, R.J.,
2025.Atmospheric-density-compensating model predictive
control for targeted reentry of drag-modulated spacecraft.Journal of Guidance, Control, and Dynamics
48, 2541–2556.doi:10.2514/1.G008665.
- Heaton et al. (2017)Heaton, A., Ahmad, N.,
Miller, K., 2017.Near Earth Asteroid Scout thrust and torque
model, in: Proceedings of the 4th International
Symposium on Solar Sailing, Kyoto, Japan.Available athttps://ntrs.nasa.gov/api/citations/20170001502/downloads/20170001502.pdf.
- Heaton and Artusio-Glimpse (2015)Heaton, A., Artusio-Glimpse, A.,
2015.An update to the NASA reference solar sail thrust
model, in: AIAA SPACE Conference and Exposition,
Pasadena, CA.doi:10.2514/6.2015-4506. AIAA
2015-4506.
- Heaton et al. (2023)Heaton, A., Ramazani, S.,
Tyler, D., 2023.Reflectivity control device (RCD) roll momentum
management for Solar Cruiser and beyond.Presentation at the 6th International Symposium on
Space Sailing, New York, NY. Available athttps://www.citytech.cuny.edu/isss2023/docs/presentations/20_June_6_Heaton.pdf.
- Hibbert and Jordaan (2021)Hibbert, L.T., Jordaan, H.W.,
2021.Considerations in the design and deployment of
flexible booms for a solar sail.Advances in Space Research 67,
2716–2726.doi:10.1016/j.asr.2020.01.019.
- Huang et al. (2021)Huang, X., Zeng, X.,
Circi, C., Vulpetti, G.,
Qiao, D., 2021.Analysis of the solar sail deformation based on the
point cloud method.Advances in Space Research 67,
2613–2627.doi:10.1016/j.asr.2020.05.008.
- Inness et al. (2024)Inness, J., Diedrich, B.,
Valdez, B., Tyler, D.,
Sanders, B., 2024.Controls modeling approach for deployment of a large
thin structures for solar sails, in: Proceedings of the
38th Annual Small Satellite Conference, Logan, UT.Paper No. SSC24-VII-06. Available athttps://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=5912&context=smallsat.
- Inness et al. (2023)Inness, J., Tyler, D.,
Diedrich, B., Ramazani, S.,
Orphee, J., 2023.Momentum management strategies for Solar Cruiser
and beyond, in: Proceedings of the 6th International
Symposium on Space Sailing, New York, NY. pp.
25–32.Available athttps://www.citytech.cuny.edu/isss2023/docs/isss2023_proceedings.pdf.
- Ismail and Varatharajoo (2010)Ismail, Z., Varatharajoo, R.,
2010.A study of reaction wheel configurations for a 3-axis
satellite attitude control.Advances in Space Research 45,
750–759.doi:10.1016/j.asr.2009.11.004.
- Johnson and Curran (2020)Johnson, L., Curran, F.,
2020.Solar Cruiser Technology Maturation Plans.Technical Report 20205003681. NASA
Marshall Space Flight Center. Huntsville, AL.Available athttps://ntrs.nasa.gov/citations/20205003681.
- Johnson et al. (2019)Johnson, L., Curran, F.,
Dissly, R., Heaton, A.,
2019.The Solar Cruiser mission: Demonstrating large
solar sails for deep space missions.Presentation at the International Astronautical
Congress, Washington, DC. Available athttps://ntrs.nasa.gov/api/citations/20190032304/downloads/20190032304.pdf.
- Johnson et al. (2022)Johnson, L., Everett, J.,
McKenzie, D., Tyler, D.,
Wallace, D., Newmark, J.,
Turse, D., Cannella, M.,
Feldman, M., 2022.The NASA Solar Cruiser mission - solar sail
propulsion enabling heliophysics missions, in:
Proceedings of the 36th Annual Small Satellite
Conference, Logan, UT.Paper No. SSC22-II-03. Available athttps://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=5303&context=smallsat.
- Lee et al. (2017)Lee, J.H., Kim, D., Kim,
J., Oh, H.S., 2017.Shorter path design and control for an underactuated
satellite.International Journal of Aerospace Engineering
2017, 8536732.doi:10.1155/2017/8536732.
- Lee et al. (2025)Lee, S., Bunker, K.R.,
Caverly, R.J., 2025.CABLESSail: Solar sail momentum management using
cable-actuated shape control, in: Proceedings of the 7th
International Symposium on Space Sailing, Delft, The
Netherlands.Abstract available athttps://filelist.tudelft.nl/LR/Subsites/ISSS%202025/ISSS2025_BookOfAbstracts_update.pdf.
- Leve et al. (2015)Leve, F.A., Hamilton, B.J.,
Peck, M.A., 2015.Spacecraft Momentum Control Systems.Space Technology Library, Springer,
Cham, Switzerland.
- Macdonald and McInnes (2011)Macdonald, M., McInnes, C.,
2011.Solar sail science mission applications and
advancement.Advances in Space Research 48,
1702–1716.doi:10.1016/j.asr.2011.03.018.
- Markley and Crassidis (2014)Markley, F.L., Crassidis, J.L.,
2014.Fundamentals of Spacecraft Attitude Determination and
Control.Space Technology Library, Springer,
New York, NY.
- Miller et al. (2022)Miller, D., Duvigneaud, F.,
Menken, W., Landau, D.,
Linares, R., 2022.High-performance solar sails for interstellar object
rendezvous.Acta Astronautica 200,
242–252.doi:10.1016/j.actaastro.2022.07.053.
- Orphee et al. (2018)Orphee, J., Diedrich, B.,
Stiltner, B., Heaton, A.,
2018.Solar torque management for the Near Earth Asteroid
Scout CubeSat using center of mass position control, in:
Proceedings of the AIAA Guidance, Navigation, and Control
Conference, Kissimmee, Florida.doi:10.2514/6.2018-1326. AIAA
2018-1326.
- Pezent et al. (2021)Pezent, J.B., Sood, R.,
Heaton, A., Miller, K.,
Johnson, L., 2021.Preliminary trajectory design for NASA’s Solar
Cruiser: A technology demonstration mission.Acta Astronautica 183,
134–140.doi:10.1016/j.actaastro.2021.03.006.
- Shen and Caverly (2025)Shen, P.Y., Caverly, R.,
2025.Solar Cruiser momentum management using model
predictive control, in: Proceedings of the 7th
International Symposium on Space Sailing, Delft, The
Netherlands.Abstract available athttps://filelist.tudelft.nl/LR/Subsites/ISSS%202025/ISSS2025_BookOfAbstracts_update.pdf.
- Shen and Caverly (2026)Shen, P.Y., Caverly, R.,
2026.Solar sail momentum management with mass translation
and reflectivity devices using predictive control.Acta Astronautica 241,
134–152.doi:10.1016/j.actaastro.2025.12.042.
- Tyler et al. (2023)Tyler, D., Diedrich, B.,
Gauvain, B., Inness, J.,
Heaton, A., Orphee, J.,
2023.Attitude control approach for Solar Cruiser, a
large, deep space solar sail mission, in: Proceedings of
the AAS Guidance, Navigation and Control Conference,
Breckenridge, CO.Available athttps://ntrs.nasa.gov/api/citations/20230001111/downloads/Attitude%20Control%20Approach%20for%20Solar%20Cruiser,%20a%20Large,%20Deep%20Space%20Solar%20Sail%20Mission%20-%20Revised.pdf.
- Vatankhahghadim and Damaren (2021)Vatankhahghadim, B., Damaren, C.J.,
2021.Solar sail deployment dynamics.Advances in Space Research 67,
2746–2756.doi:10.1016/j.asr.2020.03.029.
- Wang et al. (2025)Wang, J., Cheng, Z., He,
G., Yuan, H., 2025.Uncertainty characterization of solar sail thrust
with a multiscale modeling method.Advances in Space Research 75,
5640–5655.doi:10.1016/j.asr.2025.01.026.
- Wie (2004)Wie, B., 2004.Solar sail attitude control and dynamics, part 2.Journal of Guidance, Control, and Dynamics
27, 536–544.doi:10.2514/1.11133.
- Woodbury and Junkins (2010)Woodbury, D., Junkins, J.,
2010.On the consider Kalman filter, in:
AIAA Guidance, Navigation, and Control Conference, p.
7752.doi:10.2514/6.2010-7752.
- Zenere and Zorzi (2018)Zenere, A., Zorzi, M.,
2018.On the coupling of model predictive control and
robust Kalman filtering.IET Control Theory & Applications
12, 1873–1881.doi:10.1049/iet-cta.2017.1074.

## 


- 


Major funding support from
