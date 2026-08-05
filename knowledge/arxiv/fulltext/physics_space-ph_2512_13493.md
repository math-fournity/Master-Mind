# Deployable Prototype Testing and Control Allocation of the CABLESSail Concept for Solar Sail Shape Control and Momentum Management

**arXiv ID**: 2512.13493v2
**Authors**: Soojeong Lee, Michael States, Keegan R. Bunker, Ryan J. Caverly
**Published**: 2025-12-15
**Categories**: physics.space-ph, math.OC
**Comments**: Submitted to Advances in Space Research
**HTML URL**: https://arxiv.org/html/2512.13493v2

## Abstract

This paper presents prototype testing and a control allocation algorithm for the Cable-Actuated Bio-inspired Lightweight Elastic Solar Sail (CABLESSail) concept aimed at performing momentum management of a solar sail. CABLESSail uses actuated cables routed along the structural booms of the solar sail to control the shape of the solar sail and changes the solar radiation pressure disturbance torques acting on it. Small-scale prototype tests of CABLESSail are presented in this paper, which demonstrate the effectiveness of cable actuation on deployable booms. A novel control allocation method is also presented in this paper that provides a computationally-efficient manner to determine the deformations required in each of the structural booms to impart the desired momentum management torque on the solar sail. Numerical simulation results with the proposed algorithm demonstrate robustness to uncertainty in the shape of the sail membrane, resulting in reliable generation of momentum management torques that exceed or meet the capabilities of state-of-the-art solar sail actuators. Both the prototype tests and control allocation methods presented in this paper represent key steps in raising the technology readiness level of the CABLESSail concept.

## Full Text

Deployable Prototype Testing and Control Allocation of the CABLESSail Concept for Solar Sail Shape Control and Momentum Management

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
- License: CC BY 4.0arXiv:2512.13493v2 [physics.space-ph] 07 Mar 2026

## Deployable Prototype Testing and Control Allocation of the CABLESSail Concept for Solar Sail Shape Control and Momentum ManagementSoojeong LeeMichael StatesKeegan R. BunkerRyan J. Caverlyrcaverly@umn.edu

## Abstract

This paper presents prototype testing and a control allocation algorithm for the Cable-Actuated Bio-inspired Lightweight Elastic Solar Sail (CABLESSail) concept aimed at performing momentum management of a solar sail. CABLESSail uses actuated cables routed along the structural booms of the solar sail to control the shape of the solar sail and changes the solar radiation pressure disturbance torques acting on it. Small-scale prototype tests of CABLESSail are presented in this paper, which demonstrate the effectiveness of cable actuation on deployable booms. A novel control allocation method is also presented in this paper that provides a computationally-efficient manner to determine the deformations required in each of the structural booms to impart the desired momentum management torque on the solar sail. Numerical simulation results with the proposed algorithm demonstrate robustness to uncertainty in the shape of the sail membrane, resulting in reliable generation of momentum management torques that exceed or meet the capabilities of state-of-the-art solar sail actuators. Both the prototype tests and control allocation methods presented in this paper represent key steps in raising the technology readiness level of the CABLESSail concept.

## keywords:Solar sails, Momentum Management, Actuation Technology, Control Allocation, Prototype Testing††journal:Advances in Space Research\affiliation

[1]organization=Department of Aerospace Engineering and Mechanics, University of Minnesota, Twin Cities,
addressline=110 Union St. SE,
city=Minneapolis, MN,
postcode=55455,
country=USA

## 1Introduction

Solar sails enable space exploration in a manner that is beyond the reach of spacecraft with traditional propulsion. Through the use of solar radiation pressure (SRP) for propulsion, solar sails are capable of performing orbital transfer and station-keeping maneuvers without any propellant. Successful development and maturation of solar sail technology will open up exciting opportunities for heliophysics, planetary science, and space exploration.

The technology needed to make solar sails a reality has advanced substantially over the past decades(Berthet et al.,2024). A number of solar sail flights have been performed with varying degrees of success, including JAXA’s IKAROS(Tsuda et al.,2013), the Planetary Society’s LightSail 2(Spencer et al.,2021), Gama Alpha(Ancona and Kezerashvili,2025), as well as NASA’s NanoSail-D(Johnson et al.,2011), NEA Scout(Lockett et al.,2020; Pezent et al.,2021a), and ACS3(Wilkie et al.,2021; Amodio et al.,2025)solar sails. These flight experiments have largely served as technology demonstration missions to advance the maturity of solar sail technology. Next-generation solar sail designs, such as NASA’s Solar Cruiser(Pezent et al.,2021b), Solar Polar Imager(Thomas et al.,2020), Space Weather Investigation Frontier (SWIFT)(Johnson et al.,2025), and HIPERSail(Wilkie et al.,2021)are notably larger than previously-flown solar sails. This will allow them to move beyond technology demonstrations and start performing impactful science.

Larger solar sails will come with a greater degree of structural flexibility(Pimienta-Penalver et al.,2019; Brownell et al.,2023; Boni et al.,2023), which leads to non-ideal sail shapes(Huang et al.,2021; Hibbert and Jordaan,2021; Wang et al.,2025). Deformation in the sail structure and its membrane can result in a significant misalignment between the solar sail’s center of mass and center of pressure, which results in large disturbance torques acting on the spacecraft(Gauvain and Tyler,2023). A typical solar sail will be equipped with a reaction-wheel-based attitude control system(Inness et al.,2023)that will saturate in the presence of large disturbance torques, necessitating momentum management(Tyler et al.,2023; Inness et al.,2023; Shen and Caverly,2025b). Momentum management is particularly challenging for solar sails, as propellant-free solutions are desired to enable long-duration missions. Less-traditional actuators have been explored for this purpose, including an active mass translator (AMT) that shifts the solar sail’s center of mass through a planar translation mechanism between portions of the solar sail’s bus(Inness et al.,2023)and reflectivity control devices (RCDs) that generate out-of-plane torques by adjusting the reflectivity properties of patches embedded into the sail membrane that are inclined at a tent angle(Heaton,2023).
As an example, NASA’s Solar Cruiser is designed to use an AMT to generate in-plane (yaw/pitch) momentum management torques and RCDs to generate out-of-plane (roll) momentum management torques(Inness et al.,2023). Other actuators and concepts have been developed for similar purposes, which can be found inGong and Macdonald (2019); Fu et al. (2016). Many of these actuators, including the AMT, face scalability challenges for solar sails larger than Solar Cruiser, as their operating principle involves the indirect cancellation of disturbance torques due to undesirable deformations in the shape of the solar sailGong and Macdonald (2019). The magnitude of these disturbance torques increases with larger solar sails, which requires larger and heavier actuators to indirectly cancel out their effect. There are also technological challenges associated with RCDs, such as embedding them within the solar sail membrane and providing them with power far from the solar sail bus. This points to the pressing need to develop new momentum management actuation technology that will enable the design and flight of the next generation of large solar sails(Spencer et al.,2019).

The Cable-Actuated Bio-inspired Lightweight Elastic Solar Sail (CABLESSail) concept was first introduced byCaverly et al. (2023)as a means to produce large, scalable momentum management torques through actuated control of the solar sail’s shape. Specifically, the CABLESSail concept leverages the fact that disturbance torques acting on the solar sail are predominantly due to unwanted boom deformations(Gauvain and Tyler,2023). By using cables routed along the length of the booms to actively control their deformation, CABLESSail can directly cancel out unwanted boom deformations, and thus cancel out these disturbance torques, or generate momentum management torques by purposefully creating boom deformations. This concept effectively transforms the flexible nature of the solar sail structure from being an undesirable property to a novel means in which to generate torques that can be used for momentum management or attitude control. Piezoelectric shape control of a solar sail’s booms has been investigated for a similar purpose(Zhang et al.,2021b,a), although the ability of these actuators to perform significant shape changes in the booms is limited by their small actuation capabilities. In contrast, CABLESSail uses cables routed along the length of the booms that are actuated by motor-driven winches in the bus of the solar sail, which is shown in Fig.1. Specifically, cables are routed along each boom to control its out-of-plane deformation in both directions, which results in a scalable and lightweight means to control the boom shape and, thus, the generation of torques. Incidentally, actuated cables have previously been proposed as a means to assist with vibration control of a solar sail’s membrane(Chen et al.,2023).Figure 1:The CABLESSail concept, which involves adjusting the tensions in cables routed along the length of the solar sail’s booms to control the boom’s bending deformation. Each boom has two actuating cables that allow for control of the boom’s out-of-plane deformation. The body frame is defined by theb1b_{1}(yaw),b2b_{2}(pitch), andb3b_{3}(roll) axes.

Although the CABLESSail concept is relatively new, substantial preliminary work towards the development of this technology is found in the literature. Following the initial formulation of the concept byCaverly et al. (2023), a modular multi-body dynamic simulation of CABLESSail was developed byBunker and Caverly (2024). A flat sail membrane model was used for the analysis performed byBunker and Caverly (2024), which was augmented to account for non-flat sail membranes byBunker and Caverly (2025). The work ofBunker and Caverly (2025)also compared the momentum management torque generation capabilities of CABLESSail to an AMT, demonstrating that reliably large torques can be generated, yet uncovered the challenge in determining appropriate boom deformations to generate a desired momentum management torque. Testing of the CABLESSail concept on a small-scale prototype was performed byBodin et al. (2025), which included both open-loop and closed-loop feedback tests with the CABLESSail actuating cables employing the controllers developed byLee and Caverly (2024,2026). Although the experiments performed byBodin et al. (2025)were promising, they only involved triangular, rollable, and collapsible (TRAC) booms made of two tape measures that were pre-deployed. Further testing on a fully deployable prototype that accommodates other boom types (e.g., lenticular booms) remains a pressing need to validate the CABLESSail concept.

This paper serves as a summary of the current state of the CABLESSail technology and includes novel results that extend upon previously published CABLESSail work(Caverly et al.,2023; Bunker and Caverly,2024; Lee and Caverly,2024; Bodin et al.,2025; Bunker and Caverly,2025; Lee et al.,2025; Lee and Caverly,2026). In particular, the novel contributions presented in this paper include 1) validation of the CABLESSail technology with a deployable22m composite lenticular boom prototype and 2) the formulation and validation of a control allocation algorithm to determine the boom deformations needed by the CABLESSail technology to generate a desired torque. These contributions fill in key needs towards elevating CABLESSail to technology readiness level (TRL) 3. Note that although a preliminary version of the proposed control allocation algorithm appeared in the work ofLee et al. (2025), this prior work did not account for the effect of clock-angle dependence, did not incorporate any constraints to ensure physically-realizable boom tip deformations, and did not assess the range of feasible torques generated by the algorithm. Additionally,Lee et al. (2025)presented preliminary results with a deployable11m composite lenticular boom that suffered from issues with boom sag due to gravity and did not feature any quantification of the CABLESSail’s actuations capabilities. Based on these significant limitations, the contributions of this paper represent a significant extension on the preliminary work ofLee et al. (2025).

The remainder of this paper is organized as follows. Section2presents an overview of the CABLESSail concept and a detailed summary of prior work towards the development of this technology. A description of the small-scale deployable CABLESSail prototype is provided in Section3, along with test results with the prototype. A control allocation method that determines the desired boom deformations needed to generated a specified momentum management torque is presented and tested in Section4. Section5discusses the future outlook of the CABLESSail technology, followed by concluding remarks in Section6.

## 2CABLESSail Concept: Overview and Summary of Prior Work

This section presents an overview of the CABLESSail concept, followed by a summary of previous simulation and prototyping results, as well as a discussion on the status of CABLESSail prior to the work presented in this paper.

## 2.1CABLESSail Concept Overview

The CABLESSail concept is centered around the notion that unwanted boom deformations are the main contributor to shifts in the solar sail’s center of pressure, and thus, disturbance torques acting on a solar sail(Gauvain and Tyler,2023). The goal of CABLESSail is to either counteract unwanted boom deformations to negate the disturbance torque or purposefully create boom deformations if a non-zero momentum management torque is desired.

To control the deformation of the solar sail’s booms, CABLESSail takes inspiration from the area of soft continuum robotics, where cable actuation can be used to control the deformation of a slender flexible structure. The “bio-inspired” portion of CABLESSail’s name derives from the fact that much of the soft continuum robotics literature is inspired by biological systems, such as the manner in which the trunk of an elephant or the arms of a starfish can be articulated. Given that the primary deformation of the booms of a solar sail is in the out-of-plane direction normal to the sail membrane, CABLESSail involves routing two cables along the length of each boom, as shown in Fig.1, where one cable lies above the boom’s neutral axis for bending and the other cable lies below this axis. The cables are controlled by winches mounted inside the solar sail’s bus and are connected to the end of the boom. The out-of-plane deformation of each boom can be controlled by adjusting the tension in its two actuating cables.

A significant advantage to the CABLESSail concept is the ease in which it scales to large solar sails. Very little tension is required in the actuating cable to enact large boom deformations, which means that relatively small cables can be used with minimal added mass to the system. The cables can easily be stored in a wound configuration around a winch and released during deployment of the sail membrane. Another advantage of CABLESSail is that rather than attempting to mitigate the effect of unwanted solar sail shapes like other momentum management actuators, it directly tackles the problem by controlling the boom and sail shape.

As a simple illustrative example of how CABLESSail generates momentum management torques, consider the deformation of an individual boom, as shown in Fig.2. This boom deformation will change the local Sun incidence angle (SIA) of the sail membrane quadrants attached to the deformed boom, resulting in a shift of the solar sail’s center of pressure. This local SIA change is related to the out-of-plane displacement of the membrane, which is visualized by the shading in Fig.2. As shown in Section2.2, this is an effective means to generate torques in the yaw/pitch axes (i.e., the axes aligned with the nominal plane of the sail). Deforming all booms in alternating directions, as shown in Fig.2, results in roll torques (i.e., torques in the direction normal to the nominal plane of the sail) for non-zero SIAs. Although there are many more ways in which the booms can be deformed to generate useful torques, these examples provide some intuition as to how CABLESSail can generate momentum management torques. A more systematic algorithm to determine appropriate doom deformations to create desired torques is proposed in Section4.Figure 2:CABLESSail actuation modes: (a) yaw-pitch mode involving a single boom deformation and (b) roll mode involving coordinated deformation of all booms.

## 2.2CABLESSail Simulation

A numerical simulation environment has been developed for CABLESSail that can be used to test different design options and configurations, as well as provide benchmarks to other actuation mechanisms, such as the AMT. The source code for this CABLESSail simulation is available in the Aerospace, Robotics, Dynamics, and Control (ARDC) Lab GitHub repository111https://github.com/ARDCLab/CABLESSail-Modular-NullSpace-Dynamic-Simulationand a more detailed overview of the simulation and the modeling approaches used can be found in the work ofBunker and Caverly (2024,2025).

## 2.2.1Simulation FeaturesFigure 3:Depiction of a simulated sail membrane shape.

The CABLESSail simulation models the solar sail bus as a rigid body and its structural booms as flexible bodies connected to the rigid bus. The simulation is designed to be modular to allow for streamlined testing with different solar sail geometries, various CABLESSail designs, and models with varying degrees of complexity and fidelity, as well as creating the ability to make comparisons to other actuation options.

An option within the simulation is to choose or randomly generate non-flat sail membrane shapes by specifying out-of-plane deformations at the nodes of a triangular mesh. The SRP force and torque are computed at each element of the mesh using the NEA Scout optical properties found in the work ofHeaton and Artusio-Glimpse (2015), then the results are summed across all of the elements to obtain the net SRP force and torque. An example of a non-flat sail membrane shape is shown in Fig.3. As described byBunker and Caverly (2025), the simulation can accommodate any sail membrane shape deformation,
where it is assumed that the corners of each membrane quadrant are co-located with the spacecraft bus and the tips of the neighboring booms. The results presented in this paper use a membrane shape that places the maximum deformation at the quadrant centroid, which matches the approach used byGauvain and Tyler (2023).

The numerical parameters used in the simulation results of this paper are given in Table1. The parameters are chosen to roughly match those of Solar Cruiser(Banik and Murphey,2010; Nguyen et al.,2023). The booms are approximated as Euler-Bernoulli beams with axial, transverse, and out-of-plane deformation using an assumed modes method.Table 1:Numerical values for the simulations performed in this paper.SymbolParameterValueLLBoom length29.529.5mρ\rhoLinear density0.10170.1017kg/mE​IEIFlexural Rigidity1,7001,700N⋅\cdotm2ζ\zetaDamping Ratio<1<1%hhDistance between the0.10.1mcable and the boom—Number of sail membrane3,6003,600mesh elements—Mesh element side length11m

## 2.2.2Simulation Results

To assess CABLESSail’s ability to reliably generate large momentum management torques, static simulations were performed byBunker and Caverly (2025)with intuitive boom deformation maneuvers that are within reasonable CABLESSail actuation limits. Three specific maneuvers were tested: a yaw-torque-inducing maneuver where one boom tip is deformed5050cm and a pitch-torque-inducing maneuver where one boom tip is deformed−50-50cm, (shown in Fig.2), and a roll-torque-inducing maneuver where two opposing boom tips are deformed5050cm and the other two opposing boom tips are deformed−50-50cm (shown in Fig.2). In the yaw and the pitch maneuvers, each maneuver deforms one of the two booms perpendicular to the torque axis, respectively.

Monte Carlo simulations were performed with these three maneuvers across a range of possible sail membrane shapes, where the maximum membrane deformation was sampled from a uniform distribution of−15-15cm to1515cm in each sail quadrant. Each randomly-generated membrane shape results in a different nominal disturbance torque acting on the vehicle prior to any actuation of the booms. As CABLESSail is primarily intended as a momentum management actuator, its key performance metric is its ability to cancel out unwanted disturbance torques. To assess this, the change in torque acting on the solar sail due to CABLESSail’s actuated boom deformation maneuvers was computed. The resulting change in torque histogram plots for each maneuver at a SIA of1717degrees and a clock angle of4545degrees are shown in Fig.4.Figure 4:Monte Carlo static simulations of (a) yaw, (b) pitch, and (b) roll maneuvers. Histogram of change in torque generated across all simulated sail membrane shapes.

It is observed in Figs.4and4that the yaw- and pitch-torque maneuvers generate reliably-large yaw and pitch torques across all membrane shapes.
This is a seemingly robust maneuver that produces momentum management torques that are similar in magnitude to the worst-case disturbance torques predicted for Solar Cruiser(Gauvain and Tyler,2023).
For the roll-torque maneuver in Fig.4, a reliably-large roll torque is generated for all membrane shapes. Unfortunately, significant yaw and pitch torques are also generated when performing this maneuver. Although this is an undesirable effect, the result is still notable, as roll torques are substantially more difficult to generate with existing actuator technology, such as RCDs and thrusters. This is highlighted inInness et al. (2023), where it is stated that “understanding each option for roll control is key as one single option for roll momentum management is not sufficient to completely manage the roll axis.” Moreover, this motivates the need to further optimize the boom deformations to minimize the residual yaw and pitch torques from the roll-torque maneuver and the residual roll torque from the yaw- and pitch-torque maneuvers. A novel control allocation algorithm that is developed for this purpose is presented in Section4.

## 2.3Deployed Prototype Testing

Small-scale prototype testing serves as a means to assess and develop CABLESSail’s technology in complement to the use of numerical simulations. This section outlines prior work involving two fully-deployed prototypes built using metallic tape measures to mimic a TRAC boom.

Preliminary work towards a small-scale CABLESSail prototype was presented in the work ofBodin et al. (2025), where metallic TRAC booms were fabricated by gluing two tape measures along one edge, as shown in Fig.5.
Actuating cables were run along the length of the TRAC booms with one end connected to a 3D-printed cap at the tip of the boom and the other end wrapped around a winch connected to an actuating motor at the base of the boom. The TRAC boom in Fig.5features a single cable along the web of the boom, while Fig.6has a more complete representation of CABLESSail TRAC boom, where one cable runs along the web and two cables rung along the flanges.Figure 5:Images of (a) a close-up of the TRAC boom prototype with a single actuating cable and (b) the vertical prototype testbed with a sail tension simulation device and the Vicon motion capture system in the background.Figure 6:Images of (a) the deployed tape-measure CABLESSail prototype testbed designed to use gravity to simulate thermal expansion effects on the boom, (b) a close-up of the cable attachment points at the end of the boom and the additional cables routed around pulleys to simulate sail tension, and (c) an optional pulley system attached to the boom tip to offload some of the gravitational forces and decrease the nominal tip deformation.

Two deployed prototype testbed are presented in the work ofBodin et al. (2025): a vertical testbed shown in Fig.5that minimizes the effect of gravity on the boom deformation and a horizontal testbed shown in Fig.6that purposefully uses gravity to simulate a nominal boom deformation due to thermal effects. The vertical testbed features additional cables attached to the tip of the boom and routed around pulleys with masses hanging from them to simulate the effect of sail membrane tensioning on the TRAC boom. The horizontal testbed has a similar sail membrane tensioning system shown in Fig.6, as well as a gravity offloading device shown in Fig.6that can adjust the amount of nominal deformation induced in the boom due to gravity. Further details regarding the hardware and electronics used to fabricate and operate the prototypes are found in the work ofBodin et al. (2025).

Experimental results with both prototypes are provided byBodin et al. (2025), including open-loop actuation tests that demonstrate the ability to deform the boom in both directions on the horizontal testbed and illustrate the effect that eyelets guiding the actuating cables along the boom have on its response using the vertical testbed. These tests provide insight into the design of the CABLESSail concept that complement the analysis performed through numerical simulations. Scaling laws based on Euler-Bernoulli beam theory are also presented in the work ofBodin et al. (2025)to better relate these small-scale prototype results to full-scale numerical values.

## 2.4Estimation & Control

The CABLESSail concept relies on precise control of the solar sail’s booms in order to generate desired torques through shape control. This necessitates the ability to estimate deformations in the booms and the design of a robust feedback controller that will ensure the booms track their desired deformation values.
CABLESSail’s estimation and control architecture is shown in Fig.7. Within this architecture, the desired torque is mapped to desired boom tip deformations through a control allocation algorithm, the estimated boom tip deformations are then subtracted from the desired deformations to generate an error that is regulated by a feedback controller that determines the actuating tension in each cable.Figure 7:Block diagram outlining the high-level estimation and control architecture. The abbreviation MM in this figure stands for momentum management.

Prior work has focused on the design and testing of the control and estimation techniques. Specifically, a feedback controller that ensures each boom tracks the desired boom tip deformation was originally developed byLee and Caverly (2024)and tested experimentally on the vertical small-scale prototype byLee and Caverly (2026); Bodin et al. (2025). The main challenge in designing this controller is ensuring robust closed-loop stability in the presence of substantial uncertainty in the structural properties and dynamics of the boom, the sail membrane, and the actuating cables. It was shown byLee and Caverly (2024,2026)that a linearized model of an Euler-Bernoulli solar sail beam actuated with a cable using the CABLESSail concept is passive from the cable tension input to the boom tip’s transverse deformation rate. This result was shown to hold for large variations in the structural properties of the boom, which motivated the use of passivity-based control. The numerical and experimental results in the work ofLee and Caverly (2024,2026)demonstrate that accurate boom tip deformation tracking can be achieved with this controller, even in the presence of notable measurement noise and with the use of low-cost prototype hardware.

Prior work on the estimation algorithm assumed that the sensors available include encoders on the winches actuating the cables and IMUs at the boom tips. Two different Kalman filters were investigated byBodin et al. (2025)to fuse together this information to obtain an accurate boom tip deformation estimate. Specifically, individual Kalman filters were implemented to estimate each boom’s tip deformation. The Kalman filters presented inBodin et al. (2025)used kinematic process models that are driven by the rate gyroscope of the boom-tip-mounted IMU and a measurement model that assumes the winch encoders can be related to the angular deflection at the boom tip. Experimental results presented in the work ofBodin et al. (2025)with the deployed prototype described in Section2.3demonstrated that the boom tip deformation can be estimated with low-cost hardware, although it highlighted some of the challenges associated with calibrating the winch encoder measurements to a corresponding boom tip deformation measurement.

Most notably, all prior work on CABLESSail’s control and estimation algorithms assumed that the desired boom tip deformations were known. In practice, a control allocation algorithm is required to determine the boom tip deformations required to achieve a desired momentum management torque. In response to this need, a novel control allocation algorithm is developed and tested in Section4.

## 2.5Status of the CABLESSail Technology

The numerical simulations and small-scale prototype testing presented in prior publications demonstrate that controlled deformations of a solar sail’s booms with the CABLESSail concept are possible and can result in the ability to reliably generate large momentum management torques. Although this is an important step in the maturation of the CABLESSail technology, there remain two critical barriers before TRL 3 can be achieved: testing on a deployable prototype and the development of a control allocation algorithm. The remainder of this paper focuses on work towards these two areas, which amounts to the novel contributions of this paper.

## 3Deployable Prototype Development

Testing on a small-scale deployable prototype is needed to assess the CABLESSail technology on a structure analogous to a solar sail boom. This section outlines the development and testing of a deployable prototype that incorporates composite lenticular booms.

## 3.1Deployable Prototype Fabrication

To better assess CABLESSail’s integration with a deployable boom, fiberglass composite lenticular booms were fabricated to match the cross-sectional dimensions of the ACS3 booms, as shown in Fig.8. Note that glass fiber reinforced polymer is used for manufacturing convenience in this work, rather than the carbon fiber reinforced polymer used for the ACS3 booms. The fabrication procedure involves laying up each half of the boom into a 3D-printed negative mold as separate parts then joining them together using epoxy. The layup schedule consists of a single0degree orientation layer of Fibre Glast plain weave22ounces per square yard (67.867.8grams per square meter) fiberglass with a matrix of West System 105 epoxy resin and 206 slow hardener, giving a post-cure thickness of0.0050.005inches (0.1270.127mm). Vacuum bagging is used during the curing process to improve the consistency and reduce the thickness of the layup by removing air bubbles, pressing the layup into the mold, and extracting excess resin. Images of the layup mold and the vacuum bag curing process are provided in Figs.8and8. The two halves are joined by applying the epoxy to the flat portions of the booms and clamping them together, as shown in Fig.8. An insert is placed between the two halves during the clamping process to ensure that the desired boom cross section is maintained during the clamping process. Once this joining process is complete, the boom flanges are trimmed to the correct height, and holes are drilled at the root for mounting to the spool. An image of a completed boom is shown in Fig.8. Booms of various lengths have been manufactured using this process. A length of 2 meters was found to be the maximum length at which the joining process can be performed without risking the insert getting stuck inside the boom.Figure 8:Images of the composite boom and manufacturing process, including (a) its cross section and dimensions in deployed and flattened configurations, (b) the layup mold, (c) the vacuum-bagged curing process, (d) the joining of two boom halves through clamping, and (e) the finished boom.

A deployment mechanism for the composite lenticular boom is designed to allow for testing. The fabricated 3D-printed mechanism integrated with a 2-meter composite boom is shown in Fig.9. The design of this mechanism is similar to that used by ACS3, where a steel ribbon is wrapped around the stored boom and used to pull the boom out for deployment. The other end of the steel ribbon is wound around a dowel connected to an actuating motor through a series of gears. The connection between the steel ribbon, the boom, and the spool that drives the boom deployment, as well as the steel ribbon’s routing to the actuated dowel is visualized in Fig.10. Although the mechanism fabricated for testing in this work includes only a single boom, the design allows for four booms to be integrated into the prototype, as shown in Fig.10.Figure 9:Images of the deployable CABLESSail prototype that features a 2-meter fiberglass composite lenticular boom.Figure 10:Depictions of the attachments between the spool of the deployable mechanism and the boom, as well as the steel ribbon that is used for deployment. Specifically, (a) a CAD model of the spool and its clamps; (b) the attachment between the spool, the boom, and the steel ribbon; and (c) an overhead view of the steel ribbon’s routing from the spool to the actuated dowel.

The motor used to drive the boom deployment is a Teknic CPM-SCSK-2310S-RLNB servo motor that has an integrated motor controller. This motor, shown at the top of the deployment mechanism in Fig.9, is much larger than what is needed to drive the boom deployment and was chosen due to its availability from a prior project. In practice, a much more compact motor can be used to drive the deployment mechanism, although this is left to be implemented in future work.

A spiral torsion spring is attached to the spool upon which the boom is stored to provide a small torque that opposes the deployment of the boom. The torsion spring is situated underneath the spool in the images of Fig.9. This torsion spring helps ensure that the boom does not expand or bloom in an undesirable fashion during deployment.

A second motor is included in the prototype to actuate the CABLESSail cable and provide a means to deform the boom in the out-of-plane direction. One end of the actuating cable is wrapped around a winch connected to the motor, while the other end is routed through a small eyelet above the boom and then is connected to the tip of the boom. A Teknic CPM-SCSK-2310S-RLNB servo motor is used for this purpose, which provides far more actuation capability than is required for this prototype. As with the boom deployment motor, a much more compact motor could be implemented in practice.

A gravity-offloading cart is used during deployment tests, as shown in Fig.9. This cart has two sets of wheels to allow for free movement of the boom during deployment. One set of wheels is located at the base of the cart and allows the cart/boom to move in the direction perpendicular to the boom deployment direction. The boom lies on the second set of wheels at the top of the cart, which allow for the boom to slide along the cart with little resistance.

## 3.2Deployable Prototype Test Results

Two experimental tests are performed with the deployable prototype to assess CABLESSail’s performance. The first test investigates its deployment and subsequent actuation capability, while the second test investigates its deformation performance in a configuration where it does not need to overcome gravity.

The first experimental test is performed where the boom is deployed, then the CABLESSail cable is used to deform the boom in the upwards direction. Still frames from a video of this test are included in Fig.11, where the entire sequence of deployment and actuation occurs over a 6-minute period. It is shown in Fig.11that the boom deploys properly from Fig.11to Fig.11without any interference from the actuating cable. The actuation of the CABLESSail cable is used in Fig.11, where a slight, yet noticeable, upwards deformation of the boom is induced. The tension in the actuation cable is then released and the boom returns to its nominal deployed configuration in Fig.11. This is a promising result, as the CABLESSail actuating cable is able to counteract and overcome the gravitational force acting on the boom when it deforms the boom above the horizontal plane.Figure 11:Still frames from a test with the deployable CABLESSail prototype. The composite lenticular boom is deployed in frames (a)-(d), then the CABLESSail actuator is used to deform the boom in the upward direction in (e), followed by the CABLESSail actuator being deactivated and the boom returning to its nominal deployed configuration in (f). Note that the gravity-offloading cart is manually moved down the length of the boom throughout the course of the deployment to avoid sagging of the boom.

A Vicon motion capture system is used to further quantify the boom tip deformation obtained when the CABLESSail actuating cable tensioned. Using the same conditions as the deployment test, the actuating cable is incrementally tensioned until the boom resists any further deformation. The results of this test are shown in Fig.12, where a maximum boom tip deformation of 18 mm is achieved within 20 seconds. The time scale, which is directly related to the motor speed, is arbitrarily chosen to demonstrate the cable actuation capability clearly. In other words, this test serves as a proof-of-concept, corresponding to a TRL 3 demonstration. For the CABLESSail concept to advance towards higher TRLs, a full-scale test must be conducted that further investigates its limitations in actuation speed and magnitude. Nonetheless, a full actuation of CABLESSail in 20 seconds is notable, as this scales to roughly 5 minutes of actuation time for a 29.5 m Solar Cruiser-scale boom. In comparison, Solar Cruiser’s AMT travels at a maximum speed of 0.5 mm/s, allowing it to travel its full 30 cm distance in about 20 minutes.

A substantial challenge when performing the preceding tensioning maneuvers is overcoming the gravitational pull acting on the cantilevered boom. To better assess the performance of the CABLESSail actuation without this effect, the prototype is turned sideways, as shown in Fig.13, where tensioning the actuating cable results in the boom deforming in the horizontal plane. Performing the same tensioning maneuver as in the previous tests in this new configuration results in the boom tip deformation shown in Fig.12. In this case, a 40 mm boom tip deformation is achieved, which is more than two times the deformation obtained in the vertical direction. Following the scaling laws derived byBodin et al. (2025), 40 mm of tip deformation with a 2 m boom is equivalent to 59 cm of tip deformation on Solar Cruiser’s 29.5 m long booms. Although larger-scale testing is required to verify CABLESSail’s performance on a full-scale boom, this is a promising result and provides preliminary confidence that boom tip actuation in the range of 50-75 cm for a Solar-Cruiser-class solar sail is plausible.

In addition to the fabrication challenges of full-scale booms, several challenges must be overcome if full-scale booms are used for ground testing. Gravity-offloading becomes more difficult, because longer boom increases both weight and the torque at the boom tip. Furthermore, the spiral torsion spring needs to provide larger torque to prevent the boom from expanding in an undesirable fashion during deployment. However, implementation in a space environment should not present significant challenges, as the booms and deployment mechanism used in the small-scale prototype study of this work are directly modeled after the booms and deployment mechanism used by the ACS3 mission.Figure 12:Boom tip deformation versus time for experimental tests with the deployable prototype where the deformation is performed in (a) the vertical direction and (b) the horizontal direction.Figure 13:The deployable prototype on its side to test actuation of the boom in the horizontal plane with a Vicon marker placed at the cap of the boom.

## 4Control Allocation

Although the yaw, pitch, and roll maneuvers presented in Section2.2.2are promising, a more systematic approach to determining appropriate maneuver shapes is needed. For example, the roll maneuver results in Fig.4feature substantial residual yaw and pitch torques. Moreover, it is unclear how to generate torques with components in all three axes simultaneously. To account for this, a control allocation algorithm is devised to determine the boom tip deformations needed to generate a given momentum management torque. Solving for the torque generated by a particular set of boom tip deformations can be achieved using the static simulation described in Section2.2.2. This is a simple process, as the four boom tip deformations map to a unique three-dimensional torque in the presence of no sail membrane deformation. Solving the control allocation problem requires solving the inverse problem, which is much more challenging, as the mapping from the three-dimensional torque to the four boom tip deformations is not unique. Moreover, the mapping from the boom tip deformations to the torque generated is nonlinear, which further complicates solving this inverse problem. A data-driven approach to developing a practical control allocation algorithm is proposed. Although the method outlined in this paper focuses on a single SIA, it can be extended to other SIAs by creating SIA-dependent mappings that are stored in a lookup table. This section presents the methodology of the proposed control allocation approach, followed by numerical simulation results demonstrating its performance.

## 4.1Torque Modeling Approach

To obtain a model of the torque generated by different combinations of boom tip deformations, static simulations at an SIA of1717degrees are performed using the same setup as in Section2.2.2, with an undeformed sail membrane and with a sweep through all possible combinations of boom tip deformations within the range±50\pm 50cm at all clock angles with 5 degree increments. Starting from one fixed clock angle, the torque generated by each maneuver is recorded as𝝉data,k=[τyaw,kτpitch,kτroll,k]{\boldsymbol{\tau}}_{\text{data},k}=\begin{bmatrix}\tau_{\text{yaw},k}&\tau_{\text{pitch},k}&\tau_{\text{roll},k}\end{bmatrix}and associated with the boom tip deformations𝐰data,𝐤=[𝐰𝟏,𝐤𝐰𝟐,𝐤𝐰𝟑,𝐤𝐰𝟒,𝐤]\mbf{w}_{\text{data},k}=\begin{bmatrix}w_{1,k}&w_{2,k}&w_{3,k}&w_{4,k}\end{bmatrix}, where the subscriptkkdenotes thekthk^{\mathrm{th}}data point andwi,kw_{i,k},i=1,…,4i=1,\ldots,4is the deformation of theithi^{\mathrm{th}}boom at thekthk^{\mathrm{th}}data point. Next, a set of basis functions is chosen that are used to map the boom tip deformations to the torque generated. Testing demonstrated that the yaw and pitch torques are linear combinations of the boom tip deformations, while the roll torque is a nonlinear function of boom tip deformations and clock angles. The model of torque generated by the boom tip deformations is expressed in the form𝝉=𝐟​(𝐰,ϕ),{\boldsymbol{\tau}}=\mbf{f}(\mbf{w},\phi),(1)

where𝝉=[τyawτpitchτroll],𝐟​(𝐰,ϕ)=[𝐟yaw​(𝐰,ϕ)𝐟pitch​(𝐰,ϕ)𝐟roll​(𝐰,ϕ)],{\boldsymbol{\tau}}=\begin{bmatrix}\tau_{\text{yaw}}\\
\tau_{\text{pitch}}\\
\tau_{\text{roll}}\end{bmatrix},\hskip 20.0pt\mbf{f}(\mbf{w},\phi)=\begin{bmatrix}\mbf{f}_{\text{yaw}}(\mbf{w},\phi)\\
\mbf{f}_{\text{pitch}}(\mbf{w},\phi)\\
\mbf{f}_{\text{roll}}(\mbf{w},\phi)\end{bmatrix},

while𝐟yaw​(𝐰,ϕ)\mbf{f}_{\text{yaw}}(\mbf{w},\phi)and𝐟pitch​(𝐰,ϕ)\mbf{f}_{\text{pitch}}(\mbf{w},\phi)are linear functions of𝐰\mbf{w}, and𝐟roll​(𝐰,ϕ)\mbf{f}_{\text{roll}}(\mbf{w},\phi)is a nonlinear function of𝐰\mbf{w}andϕ\phi.

The linear functions are expressed as𝐟yaw​(𝐰,ϕ)\displaystyle\mbf{f}_{\text{yaw}}(\mbf{w},\phi)=sin⁡(ϕ)​𝐀yaw​𝐰,\displaystyle=\sin(\phi)\mbf{A}_{\text{yaw}}\mbf{w},(2)𝐟pitch​(𝐰,ϕ)\displaystyle\mbf{f}_{\text{pitch}}(\mbf{w},\phi)=cos⁡(ϕ)​𝐀pitch​𝐰,\displaystyle=\cos(\phi)\mbf{A}_{\text{pitch}}\mbf{w},(3)

where𝐀yaw\mbf{A}_{\text{yaw}}and𝐀pitch\mbf{A}_{\text{pitch}}are matrices that contain linear coefficients of each boom’s deformations and constant at all clock angles, the sinusoidal functions for yaw and pitch torques are obtained by an analysis of single boom deformation.
The matrices𝐀yaw\mbf{A}_{\text{yaw}}and𝐀pitch\mbf{A}_{\text{pitch}}are obtained through a least-squares computation as[𝐀yaw𝐀pitch]=[𝝉data,yaw𝖳𝝉data,pitch𝖳]​𝐰data​(𝐰data𝖳​𝐰data)−𝟏,\begin{bmatrix}\mbf{A}_{\text{yaw}}\\
\mbf{A}_{\text{pitch}}\end{bmatrix}=\begin{bmatrix}{\boldsymbol{\tau}}_{\text{data},\text{yaw}}^{\mathsf{T}}\\
{\boldsymbol{\tau}}_{\text{data},\text{pitch}}^{\mathsf{T}}\end{bmatrix}\mbf{w}_{\text{data}}\left(\mbf{w}_{\text{data}}^{\mathsf{T}}\mbf{w}_{\text{data}}\right)^{-1},(4)

where𝐰data\displaystyle\mbf{w}_{\text{data}}=[𝐰data,𝟏⋮𝐰data,𝐧],\displaystyle=\begin{bmatrix}\mbf{w}_{\text{data},1}\\
\vdots\\
\mbf{w}_{\text{data},n}\end{bmatrix},𝝉data\displaystyle{\boldsymbol{\tau}}_{\text{data}}=[𝝉data,1⋮𝝉data,n]=[𝝉data,yaw𝝉data,pitch𝝉data,roll],\displaystyle=\begin{bmatrix}{\boldsymbol{\tau}}_{\text{data},1}\\
\vdots\\
{\boldsymbol{\tau}}_{\text{data},n}\end{bmatrix}=\begin{bmatrix}{\boldsymbol{\tau}}_{\text{data},\text{yaw}}&{\boldsymbol{\tau}}_{\text{data},\text{pitch}}&{\boldsymbol{\tau}}_{\text{data},\text{roll}}\end{bmatrix},

𝝉data,yaw=[τyaw,1⋯τyaw,n]𝖳{\boldsymbol{\tau}}_{\text{data},\text{yaw}}=\begin{bmatrix}\tau_{\text{yaw},1}&\cdots&\tau_{\text{yaw},n}\end{bmatrix}^{\mathsf{T}},𝝉data,pitch=[τpitch,1⋯τpitch,n]𝖳{\boldsymbol{\tau}}_{\text{data},\text{pitch}}=\begin{bmatrix}\tau_{\text{pitch},1}&\cdots&\tau_{\text{pitch},n}\end{bmatrix}^{\mathsf{T}},𝝉data,roll=[τroll,1⋯τroll,n]𝖳{\boldsymbol{\tau}}_{\text{data},\text{roll}}=\begin{bmatrix}\tau_{\text{roll},1}&\cdots&\tau_{\text{roll},n}\end{bmatrix}^{\mathsf{T}}, andnnis the number of data points collected.

The nonlinear function𝐟roll​(𝐰,ϕ)\mbf{f}_{\text{roll}}(\mbf{w},\phi)consists of basis functions𝐅roll​(𝐰)\mbf{F}_{\text{roll}}(\mbf{w})that applies boom tip deformations and coefficients𝐪roll​(ϕ)\mbf{q}_{\text{roll}}(\phi)related to clock angles as𝐟roll​(𝐰,ϕ)=𝐅roll​(𝐰)​𝐪roll​(ϕ).\mbf{f}_{\text{roll}}(\mbf{w},\phi)=\mbf{F}_{\text{roll}}(\mbf{w})\mbf{q}_{\text{roll}}(\phi).(5)

The polynomial basis functions span all combinations of linear to cubic terms of boom tip deformations as𝐅roll​(𝐰)=𝐅r,lin​(𝐰)+𝐅r,qua​(𝐰)+𝐅𝐫,𝐜𝐮𝐛​(𝐰),\mbf{F}_{\text{roll}}(\mbf{w})=\mbf{F}_{\text{r},\text{lin}}(\mbf{w})+\mbf{F}_{\text{r},\text{qua}}(\mbf{w})+\mbf{F}_{r,cub}(\mbf{w}),(6)

where𝐅r,lin​(𝐰)\displaystyle\mbf{F}_{\text{r},\text{lin}}(\mbf{w})=[w1w2w3w4]​𝐪r,lin​(ϕ),\displaystyle=\begin{bmatrix}w_{1}&w_{2}&w_{3}&w_{4}\end{bmatrix}\mbf{q}_{\text{r},\text{lin}}(\phi),𝐅r,qua​(𝐰)\displaystyle\mbf{F}_{\text{r},\text{qua}}(\mbf{w})=[w12⋯w1​w2⋯]​𝐪r,qua​(ϕ),\displaystyle=\begin{bmatrix}w_{1}^{2}&\cdots&w_{1}w_{2}&\cdots\end{bmatrix}\mbf{q}_{\text{r},\text{qua}}(\phi),𝐅r,cub​(𝐰)\displaystyle\mbf{F}_{\text{r},\text{cub}}(\mbf{w})=[w13⋯w12​w2⋯w1​w2​w3⋯]​𝐪𝐫,𝐜𝐮𝐛​(ϕ),\displaystyle=\begin{bmatrix}w_{1}^{3}&\cdots&w_{1}^{2}w_{2}&\cdots&w_{1}w_{2}w_{3}&\cdots\end{bmatrix}\mbf{q}_{r,cub}(\phi),

𝐪r,lin​(ϕ)∈ℝ𝟒\mbf{q}_{\text{r},\text{lin}}(\phi)\in\mathbb{R}^{4},𝐪r,qua​(ϕ)∈ℝ𝟏𝟎\mbf{q}_{\text{r},\text{qua}}(\phi)\in\mathbb{R}^{10}, and𝐪r,cub​(ϕ)∈ℝ𝟐𝟎\mbf{q}_{\text{r},\text{cub}}(\phi)\in\mathbb{R}^{20}are trigonometric coefficients for each basis function that are expressed as𝐪roll​(ϕ)=[𝐪r,lin𝖳​(ϕ)𝐪r,qua𝖳​(ϕ)𝐪r,cub𝖳​(ϕ)]𝖳=𝐪ϕ​sin⁡(𝟐​ϕ)​[𝟏csc⁡(ϕ)sec⁡(ϕ)csc⁡(𝟐​ϕ)]𝖳,\mbf{q}_{\text{roll}}(\phi)=\begin{bmatrix}\mbf{q}_{\text{r},\text{lin}}^{\mathsf{T}}(\phi)&\mbf{q}_{\text{r},\text{qua}}^{\mathsf{T}}(\phi)&\mbf{q}_{\text{r},\text{cub}}^{\mathsf{T}}(\phi)\end{bmatrix}^{\mathsf{T}}=\mbf{q}_{\phi}\sin(2\phi)\begin{bmatrix}1&\csc(\phi)&\sec(\phi)&\csc(2\phi)\end{bmatrix}^{\mathsf{T}},

and𝐪ϕ∈ℝ𝟑𝟒×𝟒\mbf{q}_{\phi}\in\mathbb{R}^{34\times 4}is a coefficient for each trigonometric function that is determined by a linear regression using the data collected at 5 degrees intervals over the entire 360 degrees range.

## 4.2Control Allocation Methodology

Now that a fit for the nonlinear mapping from boom tip deformations to torque has been found, performing control allocation amounts to solving for the roots of the expression𝝉des−𝐟​(𝐰,ϕ){\boldsymbol{\tau}}_{\text{des}}-\mbf{f}(\mbf{w},\phi), where𝝉des{\boldsymbol{\tau}}_{\text{des}}is the desired momentum management torque to be generated. To ensure that this can be performed onboard a solar sail’s flight computer, the proposed control allocation algorithm makes use of the Levenberg-Marquardt method to solve the nonlinear weighted least-squares optimization problemmin𝐰∈ℝ𝟒\displaystyle\min_{\mbf{w}\in\mathbb{R}^{4}}\quad(𝝉des−𝐟​(𝐰,ϕ))𝖳​𝐖​(𝝉des−𝐟​(𝐰,ϕ))\displaystyle({\boldsymbol{\tau}}_{\text{des}}-\mbf{f}(\mbf{w},\phi))^{\mathsf{T}}\mbf{W}({\boldsymbol{\tau}}_{\text{des}}-\mbf{f}(\mbf{w},\phi))(7)s.t.|wi|≤wmax,i=1,2,3,4,\displaystyle|w_{i}|\leq w_{\text{max}},\,\,i=1,2,3,4,(8)

where𝐰=[𝐰𝟏𝐰𝟐𝐰𝟑𝐰𝟒]𝖳\mbf{w}=\begin{bmatrix}w_{1}&w_{2}&w_{3}&w_{4}\end{bmatrix}^{\mathsf{T}}is the design variable representing the boom tip deformations and𝐖=𝐖𝖳>𝟎\mbf{W}=\mbf{W}^{\mathsf{T}}>0is a positive definite weighting matrix that can be used to emphasize which components of𝝉des{\boldsymbol{\tau}}_{\text{des}}are more important to match. This weighting matrix can also be used to normalize the desired torque, which is useful in this application, since roll torques are typically two orders of magnitude smaller than yaw/pitch torques.
Based on the expected actuation limits of CABLESSail, a maximum feasible boom tip deformation lengthwmaxw_{\text{max}}is applied as a boundary constraint to the optimization problem.
The algorithm proceeds with the following iterative steps:
- 1.

Step 1:Initialize𝐰(𝟎)\mbf{w}^{(0)}and setj=0j=0.
- 2.

Step 2:Solve for𝐰(𝐣+𝟏)\mbf{w}^{(j+1)}with the update law𝐰(𝐣+𝟏)=𝐰(𝐣)+(𝐉𝖳​𝐖−𝟏​𝐉+η​𝐈)−𝟏​𝐉𝖳​𝐖−𝟏​(𝝉des−𝐟​(𝐰(𝐣),ϕ)),\mbf{w}^{(j+1)}=\mbf{w}^{(j)}+\left(\mbf{J}^{\mathsf{T}}\mbf{W}^{-1}\mbf{J}+\eta\mbf{I}\right)^{-1}\mbf{J}^{\mathsf{T}}\mbf{W}^{-1}({\boldsymbol{\tau}}_{\text{des}}-\mbf{f}(\mbf{w}^{(j)},\phi)),(9)

where𝐉=∂𝐟/∂𝐰|𝐰(𝐣)\mbf{J}=\partial\mbf{f}/\partial\mbf{w}|_{\mbf{w}^{(j)}}is the Jacobian of𝐟​(𝐰,ϕ)\mbf{f}(\mbf{w},\phi)evaluated at𝐰(𝐣)\mbf{w}^{(j)}andη>0\eta>0is a term used to add numerical damping to the computations. If no boom tip deformations have been constrained in previous iterations, then𝐟​(𝐰,ϕ)\mbf{f}(\mbf{w},\phi)is defined based on Eqs. (1), (2), (3), and (5), and𝐰(𝐣+𝟏)\mbf{w}^{(j+1)}is updated according to Eq. (9). If any boom tip deformations have been constrained in previous iterations, then the associated entries of𝐰(𝐣)\mbf{w}^{(j)}are fixed at their constrained values when computing𝐟​(𝐰(𝐣),ϕ)\mbf{f}(\mbf{w}^{(j)},\phi), the columns of𝐉=∂𝐟/∂𝐰|𝐰(𝐣)\mbf{J}=\partial\mbf{f}/\partial\mbf{w}|_{\mbf{w}^{(j)}}associated with these entries are removed, and the update law in Eq. (9) is only used to update the remaining unconstrained boom tip deformations.
- 3.

Step 3:Jump to Step 6 ifmax⁡(|w1(j+1)|,|w2(j+1)|,|w3(j+1)|,|w4(j+1)|)≤wmax\max\left(|w_{1}^{(j+1)}|,|w_{2}^{(j+1)}|,|w_{3}^{(j+1)}|,|w_{4}^{(j+1)}|\right)\leq w_{\text{max}}, wherewmax>0w_{\text{max}}>0is a user-defined maximum feasible boom tip deformation length. Else, go to Step 4.
- 4.

Step 4:Choose the boom tip deformation with the largest absolute value, and scale it down to the constraint boundarywmaxw_{\text{max}}while keeping its sign. For example, if|w1(j+1)|=max⁡(|w1(j+1)|,|w2(j+1)|,|w3(j+1)|,|w4(j+1)|)|w_{1}^{(j+1)}|=\max\left(|w_{1}^{(j+1)}|,|w_{2}^{(j+1)}|,|w_{3}^{(j+1)}|,|w_{4}^{(j+1)}|\right), then the solution is updated as𝐰(𝐣+𝟏)=[𝐰𝟏,max𝐰𝟐(𝐣+𝟏)𝐰𝟑(𝐣+𝟏)𝐰𝟒(𝐣+𝟏)]𝖳\mbf{w}^{(j+1)}=\begin{bmatrix}w_{1,\text{max}}&w_{2}^{(j+1)}&w_{3}^{(j+1)}&w_{4}^{(j+1)}\end{bmatrix}^{\mathsf{T}}, wherew1,max=sign​(w1(j+1))​wmax.w_{1,\text{max}}=\text{sign}(w_{1}^{(j+1)})~w_{\text{max}}.(10)
- 5.

Step 5:Setj=j+1j=j+1and return to Step 2 with the boom tip deformation constrained in Step 4 removed from the optimization problem.
- 6.

Step 6:Exit if(𝝉des−𝐟​(𝐰(𝐣+𝟏),ϕ))𝖳​𝐖​(𝝉des−𝐟​(𝐰(𝐣+𝟏),ϕ))<ϵ({\boldsymbol{\tau}}_{\text{des}}-\mbf{f}(\mbf{w}^{(j+1)},\phi))^{\mathsf{T}}\mbf{W}({\boldsymbol{\tau}}_{\text{des}}-\mbf{f}(\mbf{w}^{(j+1)},\phi))<\epsilonor the maximum number of iterations is exceeded, whereϵ>0\epsilon>0is a user-defined tolerance of convergence. Else, setj=j+1j=j+1and return to Step 2.

Note that the solution and convergence properties of this algorithm depend on the initial guess𝐰(𝟎)\mbf{w}^{(0)}. An initial guess closer to the optimal value will likely reduce the number of iterations required to meet the convergence criteria and potentially improve the quality of the solution. Results in this section are generated with𝐰(𝟎)=𝟎\mbf{w}^{(0)}=\mbf{0}to demonstrate the performance of the algorithm with a relatively poor initial guess. It is also worth noting that this algorithm transforms the nonlinear weighted least-squares into a sequence of simple computations that only involve a matrix inverse and matrix multiplications. This increases the likelihood that this algorithm could be performed onboard a solar sail flight computer.

## 4.3Control Allocation Simulation Results

The proposed control allocation algorithm is validated through numerical static simulation studies. The control allocation method is first applied to improve upon the intuitive momentum management maneuvers tested in Section2.2.2with the intent of reducing unwanted residual torques. To better understand the range of desired momentum management torques that can be accurately achieved by the proposed algorithm, a second set of results is presented in this section that explores the accuracy of the torques generated across a range of desired values to determine the range of feasible torques.

## 4.3.1Comparison to Intuitive Maneuvers

The proposed control allocation algorithm is first tested by attempting to improve upon the intuitive maneuvers performed in Section2.2.2. Individual yaw, pitch, and roll maneuvers are tested. Desired torques at each clock angle in Table2are provided to the algorithm with an initial guess of𝐰(𝟎)=𝟎\mbf{w}^{(0)}=\mbf{0}, numerical dampingη=10−6\eta=10^{-6}, and a convergence tolerance ofϵ=10−5\epsilon=10^{-5}. A weighting matrix𝐖\mbf{W}used for each case is provided in Table2. Based on the discussion in Section3.2, constraints of5050cm and7575cm are chosen for the maximum allowable boom tip deformations. With those conditions, the resulting boom tip deformations computed by the proposed control allocation algorithm, with and without constraints, are shown in Table3.Table 2:Conditions for the numerical tests of the proposed control allocation algorithm for specific individual yaw, pitch, and roll maneuvers.ϕ\phi(deg)Axis𝝉des{\boldsymbol{\tau}}_{\text{des}}(N⋅\cdotm)𝐖\mbf{W}Yaw[3.7×10−400]𝖳\begin{bmatrix}3.7\times 10^{-4}&0&0\end{bmatrix}^{\mathsf{T}}diag​{1,1,102}\text{diag}\{1,1,10^{2}\}30Pitch[06.3×10−40]𝖳\begin{bmatrix}0&6.3\times 10^{-4}&0\end{bmatrix}^{\mathsf{T}}diag​{1,1,102}\text{diag}\{1,1,10^{2}\}Roll[001.8×10−5]𝖳\begin{bmatrix}0&0&1.8\times 10^{-5}\end{bmatrix}^{\mathsf{T}}diag​{1,1,103}\text{diag}\{1,1,10^{3}\}Yaw[5.2×10−400]𝖳\begin{bmatrix}5.2\times 10^{-4}&0&0\end{bmatrix}^{\mathsf{T}}diag​{1,1,102}\text{diag}\{1,1,10^{2}\}45Pitch[05.2×10−40]𝖳\begin{bmatrix}0&5.2\times 10^{-4}&0\end{bmatrix}^{\mathsf{T}}diag​{1,1,102}\text{diag}\{1,1,10^{2}\}Roll[002.1×10−5]𝖳\begin{bmatrix}0&0&2.1\times 10^{-5}\end{bmatrix}^{\mathsf{T}}diag​{1,1,103}\text{diag}\{1,1,10^{3}\}Table 3:Results of the proposed control allocation algorithm for specific individual yaw, pitch, and roll maneuvers.Optimal𝐰\mbf{w}(cm)ϕ\phi(deg)Axisw/5050cm Constraintw/7575cm ConstraintNo ConstraintYaw[41.614.5−42.936.1]𝖳\begin{bmatrix}41.6&14.5&-42.9&36.1\end{bmatrix}^{\mathsf{T}}--30Pitch[−29.024.1−20.8−23.2]𝖳\begin{bmatrix}-29.0&24.1&-20.8&-23.2\end{bmatrix}^{\mathsf{T}}--Roll[−44.2−50.050.0−39.4]𝖳\begin{bmatrix}-44.2&-50.0&50.0&-39.4\end{bmatrix}^{\mathsf{T}}[−53.2−75.075.018.1]𝖳\begin{bmatrix}-53.2&-75.0&75.0&18.1\end{bmatrix}^{\mathsf{T}}[−81.4−76.799.327.7]𝖳\begin{bmatrix}-81.4&-76.7&99.3&27.7\end{bmatrix}^{\mathsf{T}}Yaw[33.316.9−34.433.5]𝖳\begin{bmatrix}33.3&16.9&-34.4&33.5\end{bmatrix}^{\mathsf{T}}--45Pitch[−33.534.4−16.9−33.3]𝖳\begin{bmatrix}-33.5&34.4&-16.9&-33.3\end{bmatrix}^{\mathsf{T}}--Roll[−42.4−50.050.0−30.7]𝖳\begin{bmatrix}-42.4&-50.0&50.0&-30.7\end{bmatrix}^{\mathsf{T}}[−35.0−75.075.035.0]𝖳\begin{bmatrix}-35.0&-75.0&75.0&35.0\end{bmatrix}^{\mathsf{T}}[−67.2−98.798.767.2]𝖳\begin{bmatrix}-67.2&-98.7&98.7&67.2\end{bmatrix}^{\mathsf{T}}

These boom tip deformations are then used as inputs to the same Monte Carlo simulations performed in Section2.2.2that compute the change in torque generated under varying sail membrane deformations, which results in the torque distributions shown in Figs.14and15. These figures present histograms of the change in torques induced by the control allocation maneuvers, and are directly compared to the intuitive maneuvers tested in Section2.2.2. Specifically, the yaw and pitch maneuver results are shown in Fig.14, while the roll maneuver results are in Fig.15.
The histograms in Fig.14only include the5050cm constraint, as the yaw and pitch maneuvers do not violate the5050cm constraint, removing the need to test the other case.
The control allocation maneuver is shown to reliably generate torques with very similar magnitude to the intuitive maneuver in the desired axes.
Notably, in the case of the roll maneuver in Fig.15, the residual yaw and pitch torques are decreased by roughly a factor of five, which highlights a substantial improvement with the control allocation maneuver compared to the intuitive maneuver. Also, in the case of the yaw and pitch maneuver in Fig.14, the residual roll torque is decreased significantly.
The histograms in Fig.15show that the boom tip deformation constraints included in the proposed control allocation algorithm affect the residual yaw and pitch torques while reliably maintaining the roll torque generation. More strict constraints increase the residual yaw and pitch torques, but still show a significant improvement compared to the intuitive maneuver.Figure 14:Static simulations of (a, b) pure yaw and (c, d) pure pitch torque generation designed using the intuitive maneuver from Section2.2.2and the optimized Control Allocation Maneuver with a constraint. Histograms of change in torque generated across all simulated sail membrane shapes at the clock angles of (a, c)3030and (b, d)4545degrees.Figure 15:Static simulations of pure roll torque generation designed using the intuitive maneuver from Section2.2.2and the optimized Control Allocation Maneuver with and without constraints. Histograms of change in torque generated across all simulated sail membrane shapes at the clock angles of (a)3030and (b)4545degrees.

## 4.3.2Range of Feasible Torques

To find the range of feasible momentum management torques that CABLESSail can generate with the proposed control allocation algorithm, additional tests are performed with a range of commanded desired yaw, pitch, and roll torques.
Two sets of tests are performed to assess the generation of either a combined yaw and pitch torque, or a pure roll torque. In each case, the proposed control allocation algorithm is tested across a grid of desired torques, where the accuracy of the CABLESSail torque generated is assessed as a percent error relative to the desired torque and the unwanted residual torques in the other axis or axes are quantified. The resolutions of the test grids are chosen as2×10−52\times 10^{-5}and2×10−62\times 10^{-6}N⋅\cdotm for the yaw/pitch and roll torque tests, respectively. These resolutions are chosen based on the spread in torques found in Figs.14and15when testing across sail membrane shape variation, as in practice membrane shape uncertainty will limit the resolution of achievable torques. The numerical parameters for the control allocation method, such as its initial guess, numerical damping, convergence tolerance, and weighting matrix, match those used in Section4.3.1for the yaw/pitch maneuver and pure roll maneuver, respectively. A maximum boom tip deformation constraint of7575cm is used, along with a flat sail membrane shape. An SIA of1717degrees is considered for all tests and results at clock angles of55degrees,1515degrees,3030degrees,4545degrees,6060degrees, and7575degrees are included. Results at clock angles outside this range are not included, as symmetry of the sail results in a repeating pattern of results that can be extrapolated from tests within this range.

The range of feasible yaw and pitch torques across the clock angles is shown in Figs.16and17. In these figures, the dark regions depict areas of low percentage error, which correspond to the feasible torques that can be generated at the respective clock angles. For yaw torques, it is observed that as the clock angle increases from55degrees to7575degrees, the range of feasible torques gets wider. On the other hand, for pitch torques, as the clock angle increases, the range of feasible torques gets narrower. This highlights the clock-angle-dependency of the yaw/pitch torques generated with CABLESSail. This dependency is periodic, which is observed by examining the distributions of the yaw and pitch torque errors in Figs.16and17, where the yaw and pitch errors are swapped at clock angles of1515degrees and7575degrees. The same relationship is observed between Figs.16and17when comparing clock angles of3030degrees and6060degrees. The large percentage error along zero desired yaw/pitch torques is slightly misleading, as the torque errors are small in magnitude in this region, but the desired torque is also very small.
In practice, it is inadvisable to set the desired momentum management torque very close to zero due to this error. Figs.16and17also demonstrate that the residual roll torque generated with all of the desired yaw/pitch torques remains very small. Most instances have residual roll torques less than1×10−61\times 10^{-6}N⋅\cdotm.

The range of feasible roll torques at each clock angle is shown in Fig.18. Percentage roll torque error is shown on the left axis in blue, and the norm of the residual yaw/pitch torque in N⋅\cdotm is shown on the right axis in orange. At a clock angle of4545degrees, Fig.18shows that roll torques within the range of−5×10−5-5\times 10^{-5}and5×10−55\times 10^{-5}N⋅\cdotm can be generated without any visible error. This clock angle is also where the largest disturbance torques are expected(Gauvain and Tyler,2023). The norm of the residual yaw/pitch torque increases for larger roll torques.
As the clock angle moves away from4545degrees, the range of feasible roll torques gets narrower and the norm of residual yaw/pitch torques gets smaller.Figure 16:Errors of the torque generated compared to the desired torques for yaw/pitch combined maneuvers with a constraint of7575cm. Colormaps of (a, c, e) yaw and pitch torque errors in percent and (b, d, f) residual roll torques in N⋅\cdotm are included at clock angles of (a, b) 5, (c, d) 15, and (e, f) 30 degrees.Figure 17:Errors of the torque generated compared to the desired torques for yaw/pitch combined maneuvers with a constraint of7575cm. Colormaps of (a, c, e) yaw and pitch torque errors in percent and (b, d, f) residual roll torques in N⋅\cdotm are included at clock angles of (a, b) 45, (c, d) 60, and (e, f) 75 degrees.Figure 18:Errors of the torque generated compared to the desired torques for roll maneuvers with a constraint of7575cm. The left axis shows roll torque error in percent, and the right axis shows norm of residual yaw/pitch torque in N⋅\cdotm at clock angles of (a) 5, (b) 15, (c) 30, (d) 45, (e) 60, and (f) 75 degrees.

## 4.4Discussion

The results of Sections4.3.1and4.3.2demonstrate CABLESSail’s ability to reliably generate large momentum management torques with the proposed control allocation method.
The tests performed in Section4.3.1highlight the robustness of the control allocation method to uncertainty in the sail membrane shape, as the control allocation algorithm assumes an undeformed membrane. Unwanted residual torques are clearly minimized in these tests when compared to the intuitive maneuvers, even with a significant constraint on the boom tip deformation of5050cm. The simulations of Section4.3.2illustrate the significant clock-angle-dependence of the feasible torque generated with CABLESSail. For example, at clock angles smaller than55degrees in magnitude, it is not feasible to generate a yaw torque with a flat sail membrane due to the solar sail’s geometry relative to the Sun. However, this coincides with clock angles where the expected disturbance torque is minimal(Gauvain and Tyler,2023), which potentially makes this effect manageable. Although the residual yaw/pitch torque can be non-negligible when generating large roll torques, its magnitude stays within the range of feasible yaw/pitch torques that can be generated at the same clock angle, as shown in Figs.16and17. This indicates the possibility of performing a yaw/pitch maneuver following a roll maneuver when the magnitude of residual yaw/pitch torque is too large and must be counteracted.

It is also worth noting that the results presented in this section highlight CABLESSail as a promising momentum management actuator when compared to state-of-the-art technology, such as an AMT and RCDs. Solar Cruiser’s RCDs were sized to produce roll torques of3×10−53\times 10^{-5}N⋅\cdotm in magnitude(Heaton et al.,2023). Fig.18demonstrates CABLESSail’s ability to accurately generate roll torques up to4×10−54\times 10^{-5}N⋅\cdotm for clock angles between3030degrees and6060degrees. Although not shown in the plots, similar results are generated for clock angles between120120degrees to150150degrees,210210degrees to240240degrees, and300300degrees to330330degrees. The range of accurate roll torque generation decreases for clock angles outside these intervals, although roll disturbance torques are also lower in these intervals(Gauvain and Tyler,2023). Solar Cruiser’s AMT is capable of generating relatively large yaw/pitch torques on the order of1.9×10−31.9\times 10^{-3}N⋅\cdotm(Inness et al.,2023; Shen and Caverly,2025a). It is shown in Figs.16and17that CABLESSail can generate yaw/pitch torques of a similar magnitude with minimal error at most clock angles. It is worth noting the difference in the residual roll torque generated when using CABLESSail in comparison to an AMT. Figs.16and17illustrate that very little residual roll torque is generated for nearly all combinations of desired yaw/pitch torques and across all clock angles, with most instances resulting in less than1×10−61\times 10^{-6}N⋅\cdotm of residual roll torque. In contrast, tangential SRP forces due to imperfect reflectivity coupled with a center of mass shift due to AMT motion can result in up to4.5×10−54.5\times 10^{-5}N⋅\cdotm of residual roll torque. This is found by multiplying the expected tangential SRP force of3×10−43\times 10^{-4}N found from NEA Scout’s optical properties(Heaton and Artusio-Glimpse,2015)and Solar Cruiser’s dimensions with the0.150.15m maximum center of mass shift enabled by Solar Cruiser’s AMT(Johnson and Curran,2020). This worst-case residual roll torque generated by the AMT is significant, as it surpasses the roll torque capability of its RCDs and of CABLESSail. CABLESSail’s ability to generate large yaw/pitch torques without inducing large residual roll torques could represent a significant advancement over the use of an AMT.

## 5Future Outlook of CABLESSail

The numerical simulations presented in this paper demonstrate that controlled deformations of a solar sail’s booms with the CABLESSail concept result in the ability to generate significant momentum management torques in the presence of sail membrane uncertainty. Small-scale prototype testing has confirmed that CABLESSail’s cable actuation is capable of reliably deforming deployable lenticular booms. These results, along with prior CABLESSail studies(Caverly et al.,2023; Bunker and Caverly,2024; Lee and Caverly,2024; Bodin et al.,2025; Bunker and Caverly,2025; Lee et al.,2025; Lee and Caverly,2026), provide the analytical and experimental proof-of-concept results to justify CABLESSail achieving TRL 3.

CABLESSail’s path towards TRLs 4 through 6 will require substantially more experimental testing with full-size prototypes to meet the TRL requirements of component and subsystem prototype demonstration in a relevant environment. These tests will ideally be performed with an engineering design unit for a potential technology demonstration flight test. To simulate a relevant environment, gravity offloading may be incorporated into the ground tests. Software-in-the-loop testing of CABLESSail’s control allocation, feedback control, and state estimation techniques will also play a role in navigating these middle TRLs.

The recent ACS3 solar sail mission demonstrated that large, undesirable boom deformations can appear upon deployment and during the course of the flight mission(Wilkie et al.,2025). Although CABLESSail was originally conceived as a momentum management actuator, it may have an even more significant benefit as a device that can provide occasional coarse corrections to undesired boom deformations. This actuation could be performed in an open-loop fashion, without the need for explicit boom tip deformation estimation. For example, it is possible that in a scenario where upon deployment the booms experience larger-than-expected deformations, CABLESSail can be used in an attempt to adjust or trim out these deformations. After some time, camera images can be used to assess whether further corrections are needed.

A broader application for the CABLESSail technology presented in this work may include actuation for a drag device that provides fine-tune control to a spacecraft’s ballistic coefficient. This could be helpful in the design of low-cost propulsion for small satellites in low-Earth orbit, where traditional propulsion options are limited. Such a device could be combined with recent advances in hardware(Murbach et al.,2010; Omar and Bevilacqua,2019)and control technology(Omar et al.,2017; Hayes and Caverly,2023,2025)to enable the precise targeted reentry of drag-modulated spacecraft.

## 6Conclusions

This paper presented critical simulation and experimental results towards increasing CABLESSail to TRL 3. Specifically, the deployable small-scale prototype fabricated and tested as part of this work provides evidence that CABLESSail is capable of achieving meaningful deformations of deployable lenticular booms without inducing buckling. Moreover, the control allocation methodology proposed in this work solves the challenge of determining the appropriate boom deformations needed to generate a particular momentum management torque. The robustness of the control allocation method to sail membrane shape uncertainty and the assessment of its range of feasible torques verified that CABLESSail is capable of providing practical momentum management capabilities to solar sails.

## Acknowledgments

This work was supported by an Early Career Faculty grant from NASA’s Space Technology Research Grants Program under award No. 80NSSC23K0075. The authors also acknowledge assistance from Austin Bodin, Niko Sexton, Chris Thacker, Michael Dallah, and Ryan Levendusky in the fabrication and testing of the CABLESSail prototype.

## References
- Amodio et al. (2025)Amodio, A., Visser, P.,
Heiligers, J., 2025.Dynamical modelling of NASA’s ACS3 solar sail
mission.Aerospace Science and Technology
161, 110146.doi:10.1016/j.ast.2025.110146.
- Ancona and Kezerashvili (2025)Ancona, E., Kezerashvili, R.,
2025.Recent advances in space sailing missions and
technology: Review of the 6th International Symposium on Space Sailing (ISSS
2023).Aeronautics and Aerospace Open Access Journal
9, 62–73.doi:10.15406/aaoaj.2025.09.00221.
- Banik and Murphey (2010)Banik, J., Murphey, T.,
2010.Performance validation of the triangular rollable and
collapsible mast, in: 24th Annual AIAA/USU Conference on
Small Satellites, Logan, UT.
- Berthet et al. (2024)Berthet, M., Schalkwyk, J.and Çelik, O.,
Sengupta, D., Fujino, K.,
Hein, A., Tenorio, L.,
Cardoso dos Santos, J., Worden, S.,
Mauskopf, P., Miyazaki, Y.,
Funaki, I., Tsuji, S.,
Fil, P., Suzuki, K.,
2024.Space sails for achieving major space exploration
goals: Historical review and future outlook.Progress in Aerospace Sciences
150, 101047.doi:10.1016/j.paerosci.2024.101047.
- Bodin et al. (2025)Bodin, A., States, M.,
Lee, S., Raab, N.,
Caverly, R., 2025.Design, estimation, and control of a cable-driven
solar sail boom testbed prototype, in: AIAA SciTech
Forum, Orlando, FL.doi:10.2514/6.2025-2835. AIAA
2025-2835.
- Boni et al. (2023)Boni, L., Bassetto, M.,
Niccolai, L., Mengali, G.,
Quarta, A., Circi, C.,
Pellegrini, R., Cavallini, E.,
2023.Structural response of Helianthus solar sail during
attitude maneuvers.Aerospace Science and Technology
133, 108152.doi:10.1016/j.ast.2023.108152.
- Brownell et al. (2023)Brownell, M., Sinclair, A.,
Singla, P., 2023.A time-varying subspace method for shape estimation
of a flexible spacecraft membrane, in: AIAA SciTech
Forum, National Harbor, MD.doi:10.2514/6.2023-2068. AIAA
2023-2068.
- Bunker and Caverly (2024)Bunker, K., Caverly, R.,
2024.Modular dynamic modeling and simulation of a
cable-actuated flexible solar sail, in: AIAA SciTech
Forum, Orlando, FL.doi:10.2514/6.2024-2436. AIAA
2024-2436.
- Bunker and Caverly (2025)Bunker, K., Caverly, R.,
2025.Static and dynamic torque generation analysis of a
cable-actuated solar sail.arXiv preprint arXiv:2501.17336 .
- Caverly et al. (2023)Caverly, R., Bunker, K.,
Raab, N., Nguyen, V.,
Saner, G., Chen, Z.,
Douvier, T., Lyman, R.,
Sorby, O., Sorge, B.,
Teshale, E., Toriseva, B.,
2023.Solar sail attitude control using shape modulation:
The Cable-Actuated Bio-inspired Lightweight Elastic Solar Sail (CABLESSail)
concept, in: 6th International Symposium on Space
Sailing, New York, NY.
- Chen et al. (2023)Chen, T.Z., Liu, X., Cai,
G.P., You, C.L., 2023.Attitude and vibration control of a solar sail.Advances in Space Research 71,
4557–4567.doi:10.1016/j.asr.2023.01.039.
- Fu et al. (2016)Fu, B., Sperber, E., Eke,
F., 2016.Solar sail technology—a state of the art review.Progress in Aerospace Sciences
86, 1–19.doi:10.1016/j.paerosci.2016.07.001.
- Gauvain and Tyler (2023)Gauvain, B., Tyler, D.,
2023.A solar sail shape modeling approach for attitude
control design and analysis, in: 6th International
Symposium on Space Sailing, New York, NY.
- Gong and Macdonald (2019)Gong, S., Macdonald, M.,
2019.Review on solar sail technology.Astrodynamics 3,
93–125.doi:10.1007/s42064-019-0038-x.
- Hayes and Caverly (2023)Hayes, A., Caverly, R.,
2023.Model predictive tracking of spacecraft deorbit
trajectories using drag modulation.Acta Astronautica 202,
670–685.doi:10.1016/j.actaastro.2022.10.057.
- Hayes and Caverly (2025)Hayes, A., Caverly, R.,
2025.Atmospheric density-compensating model predictive
control for targeted reentry of drag-modulated spacecraft.Journal of Guidance, Control, and Dynamics
48, 2541–2556.doi:10.2514/1.G008665.
- Heaton (2023)Heaton, A., 2023.Reflectivity control device (RCD) roll momentum
management for Solar Cruiser and beyond, in: 6th
International Symposium on Space Sailing, New York, NY.
- Heaton and Artusio-Glimpse (2015)Heaton, A., Artusio-Glimpse, A.,
2015.An update to the NASA reference solar sail thrust
model, in: AIAA SPACE Conference and Exposition,
Pasadena, CA.doi:10.2514/6.2015-4506. AIAA
2015-4506.
- Heaton et al. (2023)Heaton, A., Ramazani, S.,
Tyler, D., 2023.Reflectivity control device (RCD) roll momentum
management for Solar Cruiser and beyond, in: 6th
International Symposium on Solar Sailing, New York, NY.
- Hibbert and Jordaan (2021)Hibbert, L.T., Jordaan, H.W.,
2021.Considerations in the design and deployment of
flexible booms for a solar sail.Advances in Space Research 67,
2716–2726.doi:10.1016/j.asr.2020.01.019.
- Huang et al. (2021)Huang, X., Zeng, X.,
Circi, C., Vulpetti, G.,
Qiao, D., 2021.Analysis of the solar sail deformation based on the
point cloud method.Advances in Space Research 67,
2613–2627.doi:10.1016/j.asr.2020.05.008.
- Inness et al. (2023)Inness, J., Tyler, D.,
Diedrich, B., Ramazani, S.,
Orphee, J., 2023.Momentum management strategies for Solar Cruiser
and beyond, in: 6th International Symposium on Space
Sailing, New York, NY.
- Johnson et al. (2025)Johnson, L., Akhavan-Tafti, M.,
Sood, R., Szabo, A.,
Thomas, H.D., 2025.Space weather investigation frontier (SWIFT)
mission concept: Continuous, distributed observations of heliospheric
structures from the vantage points of sun-earth L1 and sub-L1.Acta Astronautica 236,
684–691.doi:10.1016/j.actaastro.2025.07.038.
- Johnson and Curran (2020)Johnson, L., Curran, F.,
2020.Solar Cruiser Technology Maturation Plans.Technical Report 20205003681. NASA
Marshall Space Flight Center.
- Johnson et al. (2011)Johnson, L., Whorton, M.,
Heaton, A., Pinson, R.,
Laue, G., Adams, C.,
2011.NanoSail-D: A solar sail demonstration mission.Acta Astronautica 68,
571–575.doi:10.1016/j.actaastro.2010.02.008.
- Lee et al. (2025)Lee, S., Bunker, K.R.,
Caverly, R.J., 2025.CABLESSail: Solar sail momentum management using
cable-actuated shape control.7th International Symposium on Space Sailing .
- Lee and Caverly (2024)Lee, S., Caverly, R., 2024.Robust cable-actuated shape control of a flexible
solar sail boom for the CABLESSail concept, in: AAS
Guidance, Navigation and Control Conference, Breckenridge,
CO.AAS 24-071.
- Lee and Caverly (2026)Lee, S., Caverly, R., 2026.Passivity-based robust shape control of a
cable-driven solar sail boom for the CABLESSail concept.Acta Astronautica 238, Part B,
602–611.doi:10.1016/j.actaastro.2025.10.034.
- Lockett et al. (2020)Lockett, T., Castillo-Rogez, J.,
Johnson, L., Matus, J.,
Lightholder, J., Marinan, A.,
Few, A., 2020.Near-Earth Asteroid Scout flight mission.IEEE Aerospace and Electronic Systems Magazine
35, 20–29.doi:10.1109/MAES.2019.2958729.
- Murbach et al. (2010)Murbach, M., Boronowsky, K.,
Benton, J., White, B.,
Fritzler, E., 2010.Options for returning payloads from the ISS after
the termination of STS flights, in: 40th International
Conference on Environmental Systems, Barcelona, Spain. p.
6223.doi:10.2514/6.2010-6223.
- Nguyen et al. (2023)Nguyen, L., Medina, K.,
McConnel, Z., Lake, M.S.,
2023.Solar Cruiser TRAC boom development, in:
AIAA SciTech Forum, p. 1507.
- Omar and Bevilacqua (2019)Omar, S., Bevilacqua, R.,
2019.Hardware and GNC solutions for controlled
spacecraft re-entry using aerodynamic drag.Acta Astronautica 159,
49–64.doi:10.1016/j.actaastro.2019.03.051.
- Omar et al. (2017)Omar, S., Bevilacqua, R.,
Guglielmo, D., Fineberg, L.,
Treptow, J., Clark, S.,
Johnson, Y., 2017.Spacecraft deorbit point targeting using aerodynamic
drag.Journal of Guidance, Control, and Dynamics
40, 2646–2652.doi:10.2514/1.G002612.
- Pezent et al. (2021a)Pezent, J., Sood, R.,
Heaton, A., 2021a.Contingency target assessment, trajectory design, and
analysis for NASA’s NEA Scout solar sail mission.Advances in Space Research 67,
2890–2898.doi:10.1016/j.asr.2020.02.004.
- Pezent et al. (2021b)Pezent, J., Sood, R.,
Heaton, A., Miller, K.,
Johnson, L., 2021b.Preliminary trajectory design for NASA’s Solar
Cruiser: A technology demonstration mission.Acta Astronautica 183,
134–140.doi:10.1016/j.actaastro.2021.03.006.
- Pimienta-Penalver et al. (2019)Pimienta-Penalver, A., Tsai, L.W.,
Juang, J.N., Crassidis, J.,
2019.Heliogyro solar sail structural dynamics and
stability.Journal of Guidance, Control, and Dynamics
42, 1645–1657.doi:10.2514/1.G003758.
- Shen and Caverly (2025a)Shen, P.Y., Caverly, R.,
2025a.Solar Cruiser momentum management using model
predictive control, in: 7th International Symposium on
Space Sailing, Delft, The Netherlands.
- Shen and Caverly (2025b)Shen, P.Y., Caverly, R.,
2025b.Solar sail momentum management with mass translation
and reflectivity devices using predictive control.arXiv preprint arXiv:2503.12643 .
- Spencer et al. (2021)Spencer, D., Betts, B.,
Bellardo, J., Diaz, A.,
Plante, B., Mansell, J.,
2021.The LightSail 2 solar sailing technology
demonstration.Advances in Space Research 67,
2878–2889.doi:10.1016/j.asr.2020.06.029.
- Spencer et al. (2019)Spencer, D., Johnson, L.,
Long, A.C., 2019.Solar sailing technology challenges.Aerospace Science and Technology
93, 105276.doi:10.1016/j.ast.2019.07.009.
- Thomas et al. (2020)Thomas, D., Baysinger, M.,
Sutherlin, S., Bean, Q.,
Clements, K., Kobayashi, K.,
Garcia, J., Fabisinski, L.,
Capizzo, P., 2020.Solar Polar Imager concept, in:
ASCEND. Virtual Event.doi:10.2514/6.2020-4060. AIAA
2020-4060.
- Tsuda et al. (2013)Tsuda, Y., Mori, O.,
Funase, R., Sawada, H.,
Yamamoto, T., Saiki, T.,
Endo, T., Yonekura, K.,
Hoshino, H., Kawaguchi, J.,
2013.Achievement of IKAROS—Japanese deep space solar
sail demonstration mission.Acta Astronautica 82,
183–188.doi:10.1016/j.actaastro.2012.03.032.
- Tyler et al. (2023)Tyler, D., Diedrich, B.,
Gauvain, B., Inness, J.,
Heaton, A., Orphee, J.,
2023.Attitude control approach for Solar Cruiser, a
large, deep space solar sail mission, in: AAS Guidance,
Navigation and Control Conference, Breckenridge, CO.
- Wang et al. (2025)Wang, J., Cheng, Z., He,
G., Yuan, H., 2025.Uncertainty characterization of solar sail thrust
with a multiscale modeling method.Advances in Space Research 75,
5640–5655.doi:10.1016/j.asr.2025.01.026.
- Wilkie et al. (2025)Wilkie, K., Fernandez, J.,
Stohlman, O., Warren, J.,
Schneider, N., Dean, G.,
Turczynski, C., Denkins, T.,
Kang, J.H., Aquilina, R.,
Shih, P., Li, D., Perez,
M., Rhodes, A., Saravanan, P.,
Tomer, S., Hickman, T.,
2025.Adventures in solar sailing: Lessons learned from the
Advanced Solar Sail System (ACS3) mission - volume I, in:
7th International Symposium on Space Sailing,
Delft, The Netherlands.
- Wilkie et al. (2021)Wilkie, W., Fernandez, J.,
Stohlman, O., Schneider, N.,
Dean, G., Kang, J.,
Warren, J., Cook, S.,
Brown, P., Denkins, T.,
Horner, S., Tapio, E.,
Straubel, M., Richter, M.,
Heiligers, J., 2021.Overview of the NASA Advanced Composite Solar Sail
System (ACS3) technology demonstration project, in:
AIAA SciTech Forum, Virtual Event.doi:10.2514/6.2021-1260. AIAA
2021-1260.
- Zhang et al. (2021a)Zhang, F., Gong, S.,
Baoyin, H., 2021a.Three-axes attitude control of solar sail based on
shape variation of booms.Aerospace 8,
198.doi:10.3390/aerospace8080198.
- Zhang et al. (2021b)Zhang, F., Shengping, G.,
Haoran, G., Baoyin, H.,
2021b.Solar sail attitude control using shape variation of
booms.Chinese Journal of Aeronautics
35, 326–336.doi:10.1016/j.cja.2021.10.036.

## 


- 


Major funding support from
