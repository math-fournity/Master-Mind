# Traceable In Situ Microwave Power Measurement at the Cryogenic Device Plane in a Dilution Refrigerator

**arXiv ID**: 2607.12751v1
**Authors**: Paolo Panetta, Andrea Celotto, Alessandro Alocco, Bernardo Galvano, Luca Fasolo, Emanuele Palumbo, Luca Callegaro, Luca Oberto, Patrizia Livreri, Emanuele Enrico
**Published**: 2026-07-14
**Categories**: physics.ins-det, physics.app-ph, quant-ph
**Comments**: 7 pages, 3 figures, 4 tables
**HTML URL**: https://arxiv.org/html/2607.12751v1

## Abstract

Accurate knowledge of the microwave power delivered to a cryogenic device under test (DUT) is essential for the characterization and operation of superconducting quantum circuits. However, this information is difficult to obtain inside dilution refrigerators because of distributed attenuation, impedance mismatch, switch-path repeatability, and temperature-dependent microwave components. This paper presents an in situ measurement method for RF power at the cryogenic device plane. The method uses a custom variable temperature stage (VTS) as a cryogenic thermal-transfer element. The TVS is alternately heated by a four-wire DC heater and by microwave power dissipated in a 20 dB pass-through attenuator. By fitting the thermal transients and comparing the corresponding steady-state temperatures, the absorbed microwave power is inferred from a directly measured DC electrical power through an AC/DC substitution procedure. The finite reflection and transmission of the attenuator are then accounted for by cryogenic two-port scattering-parameter measurements based on a switch-assisted Short--Open--Load--Reciprocal calibration, so that the result is referred to the DUT reference plane. The system is demonstrated in a dilution refrigerator with powers between -43 and -58 dBm at the DUT input plane. The demonstrated relative standard uncertainty ranges from about 2% at -43.9 dBm to about 40% at -57.6 dBm. The proposed approach combines thermal RF power transfer, cryogenic S-parameter correction, and uncertainty evaluation in a measurement architecture compatible with quantum-device experiments, providing a practical route toward traceable microwave-power calibration at millikelvin stages.

## Full Text

Traceable In Situ Microwave Power Measurement at the Cryogenic Device Plane in a Dilution Refrigerator

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
- License: CC BY-NC-ND 4.0arXiv:2607.12751v1 [physics.ins-det] 14 Jul 2026

## Traceable In Situ Microwave Power Measurement at the Cryogenic Device Plane in a Dilution RefrigeratorPaolo Panetta4,
Andrea Celotto13,
Alessandro Alocco13,
Bernardo Galvano23,
Luca Fasolo3,
Emanuele Palumbo13,
Luca Callegaro3,
Luca Oberto3,
Patrizia Livreri2,
and Emanuele Enrico31Department of Applied Science and Technology, Politecnico di Torino, Torino, Italy.2Department of Engineering, University of Palermo, Palermo, Italy.3Istituto Nazionale di Ricerca Metrologica (INRiM), Torino, Italy.4Department of Physics, Università degli Studi di Pisa, Pisa, Italy.Corresponding author: Emanuele Enrico (e.enrico@inrim.it).

## Abstract

Accurate knowledge of the microwave power delivered to a cryogenic device under test (DUT) is essential for the characterization and operation of superconducting quantum circuits. However, this information is difficult to obtain inside dilution refrigerators because of distributed attenuation, impedance mismatch, switch-path repeatability, and temperature-dependent microwave components. This paper presents an in situ measurement method for RF power at the cryogenic device plane. The method uses a custom variable temperature stage (VTS) as a cryogenic thermal-transfer element. The TVS is alternately heated by a four-wire DC heater and by microwave power dissipated in a 20 dB pass-through attenuator. By fitting the thermal transients and comparing the corresponding steady-state temperatures, the absorbed microwave power is inferred from a directly measured DC electrical power through an AC/DC substitution procedure. The finite reflection and transmission of the attenuator are then accounted for by cryogenic two-port scattering-parameter measurements based on a switch-assisted Short–Open–Load–Reciprocal calibration, so that the result is referred to the DUT reference plane. The system is demonstrated in a dilution refrigerator with powers between−43-43and−58-58dBm at the DUT input plane. The demonstrated relative standard uncertainty ranges from about2%2\%at43.943.9dBm to about40%40\%at57.657.6dBm. The proposed approach combines thermal RF power transfer, cryogenic S-parameter correction, and uncertainty evaluation in a measurement architecture compatible with quantum-device experiments, providing a practical route toward traceable microwave-power calibration at millikelvin stages.

## IIntroduction

Microwave signals are central to the control, readout, and characterization of superconducting and other cryogenic quantum devices. In circuit quantum electrodynamics and related superconducting-qubit platforms, the electromagnetic field at the device reference plane determines transition rates, readout photon number, nonlinear operating points, measurement backaction, and unwanted effects such as ac Stark shifts or excess heating[9,16,1,2,7,19,6]. As these experiments are performed at millikelvin temperatures through heavily attenuated and thermally anchored coaxial lines, the power set at room temperature is non trivially related to the power delivered to the device under test (DUT). Cable losses, attenuator values, connector repeatability, switch paths, impedance mismatch, and temperature-dependent component behavior make the DUT-plane power a measurement quantity that must be calibrated rather than assumed.

Conventional RF and microwave power metrology relies extensively on thermal sensors and on DC-substitution or AC/DC transfer principles: the same thermal response is produced by an RF signal and by a measurable DC electrical power, thereby linking the RF power to voltage, current, and resistance standards[22,21,4]. Extending this concept to cryogenic environments is attractive because it eliminates the uncertainty contributions added from routing the signal back to room temperature and calibrating the gain and noise of an output amplification chain. However, the cryogenic implementation is challenging. The power sensor must operate with a very small thermal load, remain compatible with the available cooling power and wiring, and provide an uncertainty model that includes both thermal and microwave effects.

Recent work has started to address this gap. Nanobolometers and graphene-based thermal detectors have demonstrated the relevance of calorimetric microwave detection for circuit-QED experiments[17,18]. A nanobolometer operated at low temperature has demonstrated broadband and traceable absorbed-power measurements based on DC substitution, including calibration of a heavily attenuated input line with uncertainty down to 0.1 dB at an absorbed power of about−114-114dBm[14]. A complementary approach has shown SI-traceable RF and microwave power measurements down to 3 K using a commercial thermoelectric power sensor, for RF levels from−35-35dBm to 0 dBm over 100 kHz–10 GHz[5]. A recent experiment demonstrated AC/DC power transfer by measuring the added noise of a cryogenic on-chip attenuator through the amplification chain[8]. These results show the relevance of cryogenic RF power metrology. However, to the best of the authors’ knowledge, a comprehensive analysis, supported by detailed uncertainty budgets, is still missing.

A second, closely related requirement is to move the microwave reference plane to the DUT. VNA calibration and error-correction techniques are well established at room temperature[26,13]and, in the last decades, have been extended and adapted for cryogenic temperatures as well[25,28,27,30,29]. In this work, the microwave correction of the VTS attenuator relies on a Short–Open–Load–Reciprocal (SOLR) calibration, i.e., an unknown-thru VNA calibration derived from the use of a reciprocal transmissive standard[13]. The same cryogenic measurement architecture and its uncertainty treatment have been developed for full two-port calibrated S-parameter measurements at the millikelvin stage[23].

The contribution of this paper is an instrumentation and measurement method that combines these two ingredients—AC/DC thermal power transfer and cryogenic S-parameter calibration—in a single dilution-refrigerator to measure the incident RF power at the DUT input reference plane. A macroscopic copper variable temperature stage is weakly coupled to the refrigerator cold finger and equipped with a DC heater, a thermometer, and a microwave attenuator used as the RF absorbing element. By alternating DC and RF heating, fitting the thermal transients, and comparing the extracted steady-state temperatures, the microwave power dissipated in the attenuator is inferred from a measured DC power. The finite microwave absorption of the attenuator is then corrected using its calibrated scattering parameters, allowing to obtain the RF power at the DUT input reference plane. Following the approach of the Guite to the Expression of Uncertainty in Measurement (GUM)[15], an uncertainty budget is developed by combining contributions associated with electrical-power measurement, thermal modelling, parasitic heating fluctuations, cold-stage temperature drift, and RF calibration.

This paper is organized as follows. Section II describes the measurement system, the modified VTS, thermometry, DC power measurement, and RF line calibration. Section III introduces the thermal model used to relate the DC and RF heating experiments. Section IV reports the measurement protocol. Section V presents the extracted RF power and the uncertainty contributions. Section VI concludes the paper and discusses the remaining limitations and possible improvements.

## IIMeasurement systemFigure 1:Schematic of the experimental setup. A Variable Temperature Stage (VTS) is weakly thermally linked with the Cold Finger (CF) of a dilution refrigerator with baseplate temperature of∼80\sim 80mK. VTS can be heated both with DC and RF through, respectively, a heater (PHP_{\mathrm{H}}) and a2020dB attenuator (PAP_{\mathrm{A}}). Its temperature is measured with a resistance thermometry bridge (Th). Both Th and H are driven in DC with a 4-wire configuration. Two nominally equal RF lines are driven by Port 1 and Port 2 and read by receiversR1\mathrm{R_{1}}andR2\mathrm{R_{2}}of a Vector Network Analyzer (VNA). The input lines are attenuated at multiple stages and we callη\etathe attenuation of the line connected to Port 1. The lines go through a directional coupler and a DC before finally reaching two 6-ports RF cryogenic switches. Output lines are isolated with an isolator and amplified in two different stages. DUT, VTS and a Reciprocal (R) are connected between the two switches. Short (S), Open (O) and Load (L) standards are also connected to the remaining ports of each switch.

## II-AOverview

A schematic representation of the experimental setup is shown in Fig.1. A Variable Temperature Stage (VTS) is thermally weakly coupled to the Cold Finger (CF) of a dilution refrigerator. The VTS can be heated with both DC and RF through a heater and a2020dB attenuator, respectively.
Two 6-ports RF switches are connected at the cold ends of four RF lines. The two input lines are attenuated at multiple stages with three2020dB attenuators[20], while output lines are amplified with HEMTs inside the cryostat and LNAs at room temperature. On each switch are mounted Short (S), Open(O) and Load (L) impedance standards. The DUT, VTS and a Reciprocal (R) are connected between the two switches. The heater is driven in a 4 wire configuration, allowing the measurement of the currentIDCI_{\mathrm{{DC}}}and voltage dropVDCV_{\mathrm{DC}}across the heater resistance. The VTS temperature is measured by means of a commercial resistance thermometry bridge.

## II-BVariable Temperature Stage

The VTS is a custom object of macroscopic size (∼50​cm3\sim 50\ \mathrm{cm}^{3}) made entirely of OFHC Cu and plated in Au. It is attached to the CF through four joints of length∼10\sim 10cm. The joints are composed of external alumina washers with a stainless steel M2 screw inside, and are the dominant thermal link of the VTS to the CF, the other link being the superconducting cables used for electrical connections, as specified below. On VTS, a resistive heater H, a2020dB RF attenuator A and a RuOx thermistor Th are installed. Thermal contact between A and VTS, H and VTS, Th and VTS is a∼1​cm2\sim 1\ \mathrm{cm}^{2}interface between two Au-plated Cu planes. A power P is delivered to VTS through NbTiN superconducting cables and we name the power dissipated at heater, attenuator and thermometerPHP_{\mathrm{H}},PAP_{\mathrm{A}}andPThP_{\mathrm{Th}}, respectively.P\displaystyle P=PH+PA+PTh;\displaystyle=P_{\mathrm{H}}+P_{\mathrm{A}}+P_{\mathrm{Th}};PH\displaystyle P_{\mathrm{H}}=PDC,H+PN,H;\displaystyle=P_{\mathrm{DC,H}}+P_{\mathrm{N,H}};PA\displaystyle P_{\mathrm{A}}=PRF,A+PN,A;\displaystyle=P_{\mathrm{RF,A}}+P_{\mathrm{N,A}};PTh\displaystyle P_{\mathrm{Th}}=Pexc,Th+PN,Th,\displaystyle=P_{\mathrm{exc,Th}}+P_{\mathrm{N,Th}},

wherePDC,HP_{\mathrm{DC,H}}andPRF,AP_{\mathrm{RF,A}}are the signal DC and RF power at heater and attenuator,Pexc,ThP_{\mathrm{exc,Th}}is the excitation power of the thermometer andPN,HP_{\mathrm{N,H}},PN,AP_{\mathrm{N,A}}andPN,ThP_{\mathrm{N,Th}}are parasitic contributions to heating. Their nature and their effects on the measurement are treated in Section V.

## II-CMeasurement of dissipated power at heater

The signal power at heaterPDC,HP_{\mathrm{DC,H}}is measured by means of a 4-wire configuration (right side of Fig.1).
This bypasses the need for a calibrated cryogenic resistor and allows to measurePDC,HP_{\mathrm{DC,H}}as the product of the measured quantitiesVDCV_{\mathrm{DC}}andIDCI_{\mathrm{DC}}.
The signal is filtered at room temperature (RT) with a cascaded RC filter and at cryostat baseplate with a cryogenic LC filter, allowing to minimizePN,HP_{\mathrm{N,H}}.

## II-DThermometry

Measurements ofTVTST_{\mathrm{VTS}}andTCFT_{\mathrm{CF}}are done with calibrated RuOx thermistors measured with a commercial multichannel resistance bridge (left side of Fig.1). For visual clarity, only the thermistor on VTS and its wiring were drawn explicitly. For the CF, the configuration is the exact same as for VTS.
As anticipated in Section I, the AC/DC transfer is performed by comparing the steady-state temperatures reached by the VTS under DC and RF heating. The thermometry chain is therefore used to extract reproducible thermal-equilibrium points rather than to measure the dissipated RF power directly.

## II-ERF lines calibration

Not all powerPRFP_{\mathrm{RF}}delivered to the VTS port of the switch is dissipated in the attenuator. The latter quantity is related to the first through the VTS attenuator scattering parametersPRF,A=PRF⋅(1−|S11|A2−|S21|A2).P_{\mathrm{RF,A}}=P_{\mathrm{RF}}\cdot(1-|S_{11}|_{\mathrm{A}}^{2}-|S_{21}|_{\mathrm{A}}^{2}).(1)

Since the quantity of interest isPRFP_{\mathrm{RF}}, a S-parameter calibration is needed to measureS11,AS_{11,\mathrm{A}}andS21,AS_{21,\mathrm{A}}and invert (1).
We implemented the SOLR calibration in the same switch-based setup described in[23], which also reports a complete uncertainty budget. Short (S), Open (O), and Load (L) impedance standards are connected to three ports of each switch, and the fourth standard is a Reciprocal (R), i.e., two cables nominally identical to the ones connecting the switches to the VTS and the DUT.
The calibration allows the full scattering matrix of any two-port device connected between the two switches, i.e., the VTS and the DUT in our case, to be de-embedded. Under the assumption, included in the calibration uncertainty budget, that the two reciprocal-path cables are identical,PRFP_{\mathrm{RF}}is equal to the power delivered at the DUT reference plane.

## IIIThermal model

Since it is a bulk macroscopic object, electronic and phononic populations in VTS are assumed to be thermalized. Therefore one can describe the VTS as a thermodynamic object with a temperatureTVTST_{\mathrm{VTS}}and a thermal capacitanceCVTS=CVTS​(TVTS)C_{\mathrm{VTS}}=C_{\mathrm{VTS}}(T_{\mathrm{VTS}}). The VTS is weakly coupled to the CF, which acts as a reservoir, through a thermal conductanceG=G​(TVTS,TCF)G=G(T_{\mathrm{VTS}},T_{\mathrm{CF}}). The VTS is also coupled with three distinct objects, A, H and Th, with a temperature-dependent thermal conductance,σCu−Cu​(T)\sigma_{\mathrm{Cu-Cu}}(T), assumed to be the same for all three. PowersPHP_{\mathrm{H}},PAP_{\mathrm{A}}, andPThP_{\mathrm{Th}}are dissipated, respectively, on each object. Under the assumption thatPHP_{\mathrm{H}},PAP_{\mathrm{A}}andPThP_{\mathrm{Th}}are stationary, one can write{CA​T˙A=PA−σCu−Cu⋅(TA−TVTS)CH​T˙H=PH−σCu−Cu⋅(TH−TVTS)CTh​T˙Th=PTh−σCu−Cu⋅(TTh−TVTS)CVTST˙VTS=σCu−Cu⋅(TA+TH+TTh−−3TVTS)−G⋅(TVTS−TCF)\left\{\begin{aligned} &C_{\mathrm{A}}\dot{T}_{\mathrm{A}}=P_{\mathrm{A}}-\sigma_{\mathrm{Cu-Cu}}\cdot(T_{\mathrm{A}}-T_{\mathrm{VTS}})\\
&C_{\mathrm{H}}\dot{T}_{\mathrm{H}}=P_{\mathrm{H}}-\sigma_{\mathrm{Cu-Cu}}\cdot(T_{\mathrm{H}}-T_{\mathrm{VTS}})\\
&C_{\mathrm{Th}}\dot{T}_{\mathrm{Th}}=P_{\mathrm{Th}}-\sigma_{\mathrm{Cu-Cu}}\cdot(T_{\mathrm{Th}}-T_{\mathrm{VTS}})\\
&C_{\mathrm{VTS}}\dot{T}_{\mathrm{VTS}}=\sigma_{\mathrm{Cu-Cu}}\cdot(T_{\mathrm{A}}+T_{\mathrm{H}}+T_{\mathrm{Th}}-\\
&\quad-3T_{\mathrm{VTS}})-G\cdot(T_{\mathrm{VTS}}-T_{\mathrm{CF}})\end{aligned}\right.

Solving this system accounting for the temperature dependencies of all thermal capacitance and thermal conductance is beyond the scope of this article. We limit here to note that, at steady state, a temperature differenceΔ​TA​(H,Th)=TA​(H,Th)−TVTS\Delta T_{\mathrm{A(H,Th)}}=T_{\mathrm{A(H,Th)}}-T_{\mathrm{VTS}}establishes,Δ​TA​(H,Th)=PA​(H,Th)σCu−Cu.\Delta T_{\mathrm{A(H,Th)}}=\frac{P_{\mathrm{A(H,Th)}}}{\sigma_{\mathrm{Cu-Cu}}}.(2)

Thermal conductance of bolted Cu–Cu and Au-plated Cu–Cu interfaces at sub-kelvin and few-kelvin temperatures have been measured and reviewed in the literature[11,10,12]. Using representative conductance values>10−2​W​K−1>10^{-2}\ \mathrm{W\ K^{-1}}(Fig. 6 of[11]) in the temperature range of interest and the experimental conditionPA​(H,Th)<10−7P_{\mathrm{A(H,Th)}}<10^{-7}W givesΔ​TA​(H,Th)<0.01\Delta T_{\mathrm{A(H,Th)}}<0.01mK.
This value is well below the thermometric uncertainty reported in Section V and we can therefore assumeTA​(H,Th)T_{\mathrm{A(H,Th)}}to be equal toTVTST_{\mathrm{VTS}}and write a single thermodynamic equation for VTSCVTS​T˙VTS=P−G⋅(TVTS−TCF)==P0+PDC,H+PRF,A−G⋅(TVTS−TCF)C_{\mathrm{VTS}}\dot{T}_{\mathrm{VTS}}=P-G\cdot(T_{\mathrm{VTS}}-T_{\mathrm{CF}})=\\
=P_{0}+P_{\mathrm{DC,H}}+P_{\mathrm{RF,A}}-G\cdot(T_{\mathrm{VTS}}-T_{\mathrm{CF}})(3)

whereP0=PN,H+PN,A+PN,Th+Pexc,ThP_{0}=P_{\mathrm{N,H}}+P_{\mathrm{N,A}}+P_{\mathrm{N,Th}}+P_{\mathrm{exc,Th}}is assumed constant throughout the whole experiment. As forGG, it is the thermal conductance of the steel screws and alumina washers described in Section II-B. It is dominated by the low-temperature thermal conductivity of stainless steel, which is approximately linear in temperature over the range of this experiment[31,12]. For a rod model of lengthLLand cross-sectionAAwith fixed boundary conditionsT​(0)=TVTST(0)=T_{\mathrm{VTS}}andT​(L)=TCFT(\mathrm{L})=T_{\mathrm{CF}}, the total conductance of the rod isG=G0⋅(TVTS+TCF)/2G=G_{0}\cdot(T_{\mathrm{VTS}}+T_{\mathrm{CF}})/2withG0=σ0⋅A/LG_{0}=\sigma_{0}\cdot\mathrm{A/L}. The adequacy of this frist-order conductance model over the investigated temperature range is assessed a posteriori from the DC-heating calibration curve and its residuals (Fig.3).GGcan be plugged into (3) and analytical solutions exist forTVTS​(t)T_{\mathrm{VTS}}(t)of the formTVTS​(t)=Tfin,VTS​1−B​e−2​t/τ1+B​e−2​t/τT_{\mathrm{VTS}}(t)=T_{\mathrm{fin,VTS}}\frac{1-Be^{-2t/\tau}}{1+Be^{-2t/\tau}}(4)

hereTfin,VTST_{\mathrm{fin,VTS}}is the steady state temperature of VTS. These are easily calculated from (3) and their values areTfin,VTSDC=TCF2+2​P0G0+2​PDC,HG0T_{\mathrm{fin,VTS}}^{\mathrm{DC}}=\sqrt{T_{\mathrm{CF}}^{2}+2\frac{P_{0}}{G_{0}}+2\frac{P_{\mathrm{DC,H}}}{G_{0}}}(5)Tfin,VTSRF=TCF2+2​P0G0+2​PRF,AG0T_{\mathrm{fin,VTS}}^{\mathrm{RF}}=\sqrt{T_{\mathrm{CF}}^{2}+2\frac{P_{0}}{G_{0}}+2\frac{P_{\mathrm{RF,A}}}{G_{0}}}(6)

where superscript indicates whether thatTfin,VTST_{\mathrm{fin,VTS}}was obtained heating with DC or RF.

Equations (5) and (6) allow, under hypothesis of stationarity ofP0P_{0}over the whole experiment, to do the AC/DC power transfer by fitting (5) over an arbitrary stepped range ofPDC,HP_{\mathrm{DC,H}}and then inverting (6) to obtainPRF,A​(Tfin,VTSRF)P_{\mathrm{RF,A}}(T_{\mathrm{fin,VTS}}^{\mathrm{RF}})asPRF,A=G0​(Tfin,VTSRF)2−TCF22−P0P_{\mathrm{RF,A}}=G_{0}\frac{(T_{\mathrm{fin,VTS}}^{\mathrm{RF}})^{2}-T_{\mathrm{CF}}^{2}}{2}-P_{0}(7)

Note that here stationarity is required only forP0P_{0}over the whole experiment, andPDC,HP_{\mathrm{DC,H}}andPRF,AP_{\mathrm{RF,A}}are varied with a stepwise sweep. For the dynamic to obey (4), though,PDC,HP_{\mathrm{DC,H}}orPRF,AP_{\mathrm{RF,A}}need to remain constant over the single power step (see Fig.2(a)).
One can then correct for VTS S parameters in order to extractPRFP_{\mathrm{RF}}using equation (1).

## IVMeasurement protocol

Before cooldown, a preliminary characterization of the RF line was done to extract a rough estimate of the total attenuation from source to DUT reference planeη′≃57\eta^{\prime}\simeq 57dB. Once cooled, VTS reached a base temperature with no external heating of228228mK, measured to be stable within11mK over a five hours time span.

VTS was then heated alternately with DC and RF signal at44GHz over a 16 dB span between−43-43dBm and−58-58dBm, with a power step of44dB and a step durationΔ​t=77\Delta t=77minutes. RF source powerPRF,VNAP_{\mathrm{RF,VNA}}was increased ofη′\eta^{\prime}with respect to the desired power at DUT reference plane. When heated in DC, polarity of signal was switched every∼5\sim 5minutes (see inset of Fig.2(a)). This allows to remove, during analysis, current or voltage biases.IDCI_{\mathrm{DC}},VDCV_{\mathrm{DC}},TVTST_{\mathrm{VTS}}andTCFT_{\mathrm{CF}}were measured every1010seconds, to allow a long integration time.

Finally, the SOLR calibration procedure described in[23]was applied to measure the VTS scattering parameters at the switch-defined reference planes. These calibrated values were then used to evaluate the absorbed-power correction in (1).

All drive and measurement instruments were simultaneously operated by a dedicated software.

## VResults

## V-ASteady-state temperature extrapolation and uncertainty evaluationFigure 2:Here, the time axis is normalized forΔ​t=77\Delta t=77minutes. (a) Power vs time plots.PDC,HP_{\mathrm{DC,H}}is the measured power dissipated at H.PRF,VNAP_{\mathrm{RF,VNA}}is the power delivered at VNA source andη′\eta^{\prime}is a preliminarily estimated measure of the total attenuation between source and DUT reference plane. VTS was alternately heated with DC and RF drives with a power step of44dB. When driven in DC, polarity of signal was swapped every∼5\sim 5minutes to account for current amplifier drifts. In the inset, measuredVDCV_{\mathrm{DC}}andIDCI_{\mathrm{DC}}are plotted.
(b)TVTST_{\mathrm{VTS}}andTCFT_{\mathrm{CF}}vs time plots.TCFT_{\mathrm{CF}}was measured to slightly drift of0.090.09mK/hour. Each interval of lengthΔ\Deltat ofTVTST_{\mathrm{VTS}}was fit with (4).

Values ofTfin,VTSDCT_{\mathrm{fin,VTS}}^{\mathrm{DC}}andTfin,VTSRFT_{\mathrm{fin,VTS}}^{\mathrm{RF}}were obtained by fittingTVTS​(t)T_{\mathrm{VTS}}(t)with (4) for each time intervalΔ​t\Delta tand keepingTfin,VTST_{\mathrm{fin,VTS}},BBandτ\tauas fit parameters. The superscript DC or RF indicates whether the value ofTfin,VTST_{\mathrm{fin,VTS}}was obtained by heating with DC or RF. FittingTfin,VTST_{\mathrm{fin,VTS}}instead of simply waiting forTVTST_{\mathrm{VTS}}to stabilize allows to find its central value even ifΔ​t≫τ\Delta t\gg\taudoes not hold. Data and best fit curves are reported in Fig.2(b). For visual clarity a color code is used forTVTST_{\mathrm{VTS}}, assigning blue to DC heating and red to RF heating. Best fits are plotted in gray over the data.

The uncertainty associated withTfin,VTST_{\mathrm{fin,VTS}}includes three contributions: the uncertainty of the transient fit, the stability of the CF temperatureTCFT_{\mathrm{CF}}, and the fluctuations of the parasitic background powerP0P_{0}. The corresponding budget is summarized in TableIforTfin,VTS=229.6T_{\mathrm{fin,VTS}}=229.6mK.TABLE I:Uncertainty budget onTfin,VTS=229.6T_{\mathrm{fin,VTS}}=229.6mKUncertainty sourceUncertaintycontribution / mKFit uncertainty0.070.07TCFT_{\mathrm{CF}}stability0.230.23Fluctuations ofP0P_{0}0.580.58Total uncertainty0.63

The contribution associated with the CF drift was evaluated from the linear trend observed inTCFT_{\mathrm{CF}}during the experiment (lower curve in Fig.2(b)). An average drift of0.090.09mK/hour was measured, for a total drift of1.151.15mK over the whole experiment. Since the VTS has a large thermal capacitance and therefore averages fast temperature fluctuations, using the standard deviation of the fullTCFT_{\mathrm{CF}}time series would overestimate its effect onTfin,VTST_{\mathrm{fin,VTS}}. The drift contribution was therefore estimated from the measured drift coefficient multiplied by the experiment duration, assuming a rectangular distribution. Propagation through (5) and (6) gives a contribution between 0.03 mK and 0.05 mK, depending on the value ofTfin,VTST_{\mathrm{fin,VTS}}.

The dominant contribution arises from slow fluctuations of the parasitic background powerP0P_{0}. This term includes the thermometer drive power and residual parasitic heating mechanisms affecting the heater, attenuator, thermometer, and wiring. Possible sources include heat conduction through cable shields, radiation from warmer stages, electrical noise, parasitic currents, ground loops, and signal dissipation in cables. The thermometer drive power is expected to be stationary and well below 1 nW, while the remaining contributions are more difficult to model from frist principles.
To evaluate their effect experimentally, a five-hour measurement was performed with no applied DC or RF signal power, i.e.PDC,H=PRF,A=0P_{\mathrm{DC,H}}=P_{\mathrm{RF,A}}=0. The observed maximum excursion ofTVTST_{\mathrm{VTS}}was 1.06 mK. Since the contribution fromTCFT_{\mathrm{CF}}drift over this time scale is only a few10−210^{-2}mK, the observed variation was assigned to fluctuations ofP0P_{0}and treated as a rectangular distribution. As shown in TableI, this term dominates the uncertainty ofTfin,VTST_{\mathrm{fin,VTS}}, contributing between75.5%75.5\%and90%90\%of the total variance. The resulting standard uncertainty onTfin,VTST_{\mathrm{fin,VTS}}lies between0.610.61mK and0.660.66mK.

## V-BDC-to-thermal calibration

the DC-heating data were used to calibrate the thermal response of the VTS.
An Orthogonal Distance Regression (ODR)[3]fit was performed onTfin,VTSDC​(PDC,H)T_{\mathrm{fin,VTS}}^{\mathrm{DC}}(P_{\mathrm{DC,H}})with (5) (blue data in Fig.3). It minimizes the normalized orthogonal distance between data and best fit curve, accounting for both uncertainty onPDC,HP_{\mathrm{DC,H}}and onTfin,VTSDCT_{\mathrm{fin,VTS}}^{\mathrm{DC}}. The uncertainty onPDC,HP_{\mathrm{DC,H}}was evaluated as in TableIIfrom uncertainties on measured voltageVDC,HV_{\mathrm{DC,H}}and currentIDC,HI_{\mathrm{DC,H}}. The cold finger temperature was treated as a fixed parameter and set equal to the mean valueT¯CF\bar{T}_{\mathrm{CF}}measured over the whole experiment. The best fit parameters wereG0=(4.03±0.07)⋅10−6​W​K−2G_{0}=(4.03\pm 0.07)\cdot 10^{-6}\mathrm{\ W\ K^{-2}}

andP0=90.7±1.8​nW.P_{0}=90.7\pm 1.8\ \mathrm{nW}.

The extracted value ofP0P_{0}is in agreement with Table 2 of[20], where an heat load between1313nW and3030nW (depending on cable specifics) per line was measured on the MXC.

The extracted value ofG0G_{0}is consistent with an independent estimate based on the geometry of the four stainless-steel screws and on literature values of the low-temperature thermal conductivity of stainless steel. UsingG0,est=4​σ0​A/LG_{0,\mathrm{est}}=4\sigma_{0}\mathrm{A}/\mathrm{L}, with the factor 4 accounting for the four nominally identical screws, A =0.64​π​mm20.64\ \pi\ \mathrm{mm^{2}}, L =1010cm andσ0=(0.5÷1)⋅10−3​W​cm−1​K−2\sigma_{0}=(0.5\div 1)\cdot 10^{-3}\ \mathrm{W\ cm^{-1}K^{-2}}(Fig. 3.21 of[24]), one findsG0,est≃(4÷8)⋅10−6​WK−2G_{0,\mathrm{est}}\simeq(4\div 8)\cdot 10^{-6}\mathrm{WK^{-2}}, in agreement with the fitted value. Moreover, the residuals of the fit, shown in the lower panel of Fig.3, do not exhibit a systematic dependence on power. These two observation provide an internal consistency check of the first-order conductance model used for deriving (4).TABLE II:Uncertainty budget onPDC,H=1.2407P_{\mathrm{DC,H}}=1.2407nW (−59.06-59.06dBm)Uncertainty sourceUncertaintycontribution / fWType A uncertainty0.2Transimpedance amplifier7.2Voltage measurement6.2Current measurement0.1Total uncertainty9.5

## V-CRF power extraction at the attenuatorFigure 3:Tfin,VTST_{\mathrm{fin,VTS}}vs Power.PDC,HP_{\mathrm{DC,H}}data were fit with (5). Then (6) was inverted to obtainPRF,A​(Tfin,VTS)P_{\mathrm{RF,A}}(T_{\mathrm{fin,VTS}}). A visual representation of the inversion idea is graphed in red.Tfin,VTSRFT_{\mathrm{fin,VTS}}^{\mathrm{RF}}on the y-axis are projected onto the best fit curve and then projected again on the x-axis. Uncertainties on the best fit parameters are taken into account by the uncertainty propagation formula of (7). Below, residuals ofPDC,HP_{\mathrm{DC,H}}from the best fit curve.

The microwave powerPRF,AP_{\mathrm{RF,A}}dissipated in the VTS was then extrapolated using (7). It is the inverse of (6), obtained by solving forPRF,AP_{\mathrm{RF,A}}and using forP0P_{0}andG0G_{0}the best fit values on the DC data.
The uncertainty onPRF,AP_{\mathrm{RF,A}}was obtained by propagating the uncertainty ofTfin,VTST_{\mathrm{fin,VTS}},TCFT_{\mathrm{CF}},G0G_{0},P0P_{0}and the covariance betweenG0G_{0}andP0P_{0}. A graphic representation of the calculation is presented in Fig.3, where the values ofTfin,VTSRFT_{\mathrm{fin,VTS}}^{\mathrm{RF}}(red errorbars on the y-axis) are projected onto the best fit curve and then projected again onto the x-axis.

A correction was also applied for the RF power dissipated in the superconducting cable section connected to the VTS and heating the attenuator. The DC contribution is negligible because the relevant cables are NbTiN superconducting cables. For the RF signal, the dissipated heat can be estimated as the product of the cable attenuation coefficient with the cable length and the RF power. Using a typical attenuation coefficient of about0.30.3dB/m below44K and a cable lenght of approximately1515cm gives a dissipated fraction of about1%1\%of the transported RF power. Assuming that half of this heat flows to the VTS,PRF,AP_{\mathrm{RF,A}}would be overestimated by approximately0.5%0.5\%. This correction was applied, and its uncertainty was represented by a rectangular distribution between0%0\%and1%1\%.

## V-DCorrection to the DUT reference planeTABLE III:Uncertainty budget onPRFP_{\mathrm{RF}}forPRF=1.74​nWP_{\mathrm{RF}}=1.74\ \mathrm{nW}(−57.58-57.58dBm)Uncertainty sourceUncertaintycontribution / nWUncertaintypercentageG0G_{0},P0P_{0}, Cov(G0G_{0},P0P_{0})0.340.342424Tfin,VTSRFT_{\mathrm{fin,VTS}}^{\mathrm{RF}}0.580.586767TCFT_{\mathrm{CF}}0.210.2199RF line calibration0.0030.003<0.01<0.01Attenuation in cables0.0050.005<0.01<0.01Total uncertainty0.710.71100100TABLE IV:Uncertainty budget onPRFP_{\mathrm{RF}}forPRF=40.9​nWP_{\mathrm{RF}}=40.9\ \mathrm{nW}(−43.87-43.87dBm)Uncertainty sourceUncertaintycontribution / nWUncertaintypercentageG0G_{0},P0P_{0}, Cov(G0G_{0},P0P_{0})0.550.553737Tfin,VTSRFT_{\mathrm{fin,VTS}}^{\mathrm{RF}}0.670.675555TCFT_{\mathrm{CF}}0.210.2155VTS calibration0.080.08∼1\sim 1Attenuation in cables0.120.12∼2\sim 2Total uncertainty0.900.90100100

The quantityPRF,AP_{\mathrm{RF,A}}represents the RF power absorbed by the2020dB attenuator mounted on VTS. The target measurand, however, is the RF power available at the DUT reference plane. This is obtained by accounting for the finite reflection and transmission coefficients of the attenuator, as in (1). The scattering parameters of the attenuator were obtained from the cryogenic SOLR calibration described in Section II.E and in[23]. The uncertainty associated with this RF correction was then propagated into the final uncertainty budget.

The values ofPRFP_{\mathrm{RF}}so extracted lie between−43.87-43.87dBm and−57.58-57.58dBm with relative uncertainty going from2%2\%forPRF=−43.87P_{\mathrm{RF}}=-43.87dBm to40%40\%forPRF=−57.58P_{\mathrm{RF}}=-57.58dBm. As can be seen from TablesIIIandIV, the dominant contributions are the uncertainties onTfin,VTSRFT_{\mathrm{fin,VTS}}^{\mathrm{RF}}and on the best fit parametersG0G_{0}andP0P_{0}, while the CF temperature drift plays a minor role accounting for less than10%10\%of the total uncertainties. The uncertainties introduced by cables heating and RF lines calibration are orders of magnitude smaller than the latter and are therefore negligible.

These results can be interpreted in this way:
- •

for small signal powers theTfin,VTST_{\mathrm{fin,VTS}}variations become too small with respect to their uncertainties;
- •

the lowest signal power used for this experiment is−57.58-57.58dBm, which corresponds to1.751.75nW. This is approximately equal to uncertainty onP0P_{0}, indicating that for such low powers the signal becomes indistinguishable from the power noise.

If one considers that also the uncertainty onTfin,VTST_{\mathrm{fin,VTS}}is dominated from fluctuations ofP0P_{0}, it becomes clear that this is the first issue to be addressed in order to achieve sensitivity to lower energies.

## VIConclusions

An in situ microwave power measurement method for dilution-refrigerator experiments was presented. The method used a modified VTS as a cryogenic thermal transfer standard and realized an AC/DC comparison between microwave heating in a2020dB attenuator and directly measured DC heating in a four-wire resistor. By fitting the thermal relaxation of the weakly coupled VTS and comparing the corresponding steady-state temperatures, the RF power dissipated in the absorber was inferred from the DC electrical power. A cryogenic SOLR calibration was then used to correct for the finite reflection and transmission of the pass-through attenuator and to refer the result to the DUT reference plane.

The experiment demonstrated the feasibility of measuring RF powers in the−43-43to−58-58dBm range inside a dilution refrigerator using instrumentation that is compatible with cryogenic quantum-device measurements. The approach is complementary to on-chip cryogenic bolometers and commercial cryogenic thermoelectric sensors: it targets a higher-power, DUT-plane calibration regime while preserving a direct link to electrical quantities through the DC substitution step. The pass-through implementation also allowed the calibrated power path to remain close to the one used during device characterization.

The present uncertainty budgets identify the dominant contributions as the stability of the power backgroundP0P_{0}, the extraction of the VTS steady-state temperature and, to a minor extent, the stability of the thermal reservoirTCFT_{\mathrm{CF}}. These results indicate that further improvements should focus on reducing parasitic heating and thermal drifts, as well as improving electrical filtering and shielding of the thermometer and heater lines. A smaller VTS would reduce the response time scales, making the experiment faster and less sensitive to slow dynamics. This would also allow for an improved measurement protocol, in which a PID control system could perform the AC/DC transfer while keepingTVTST_{\mathrm{VTS}}fixed.

Future work will also compare the VTS-based result with an independent cryogenic power standard and assess the method during operation with representative quantum devices. Overall, the proposed VTS-based power meter provides a practical route toward traceable RF power calibration at the cryogenic DUT plane, addressing a measurement need that is increasingly important for scalable quantum-device characterization.

## VII*Aknowledgments

This work is supported by the European projects MiSS and MetSuperQ. MiSS is funded by the European Union through the Horizon Europe 2021-2027 Framework Programme, Grant agreement ID: 101135868. The 23FUN08 MetSuperQ project has received funding from the European Partnership on Metrology, co-financed from the European Union’s Horizon Europe Research and Innovation Programme and by the Participating States.

## References
- [1]A. Blais, S. M. Girvin, and W. D. Oliver(2020)Quantum information processing and quantum optics with circuit quantum electrodynamics.Nat. Phys.16(3),pp. 247–256.External Links:DocumentCited by:§I.
- [2]A. Blais, A. L. Grimsmo, S. M. Girvin, and A. Wallraff(2021)Circuit quantum electrodynamics.Rev. Mod. Phys.93(2),pp. 025005.External Links:DocumentCited by:§I.
- [3]P. T. Boggs and J. E. Rogers(1990)Orthogonal distance regression.InStatistical Analysis of Measurement Error Models and Applications,Contemporary Mathematics, Vol.112,pp. 183–194.Cited by:§V-B.
- [4]L. Brunetti and L. Oberto(2008)On coaxial microcalorimeter calibration.Eur. Phys. J. Appl. Phys.43(2),pp. 239–244.External Links:DocumentCited by:§I.
- [5]M. Celep, S.-H. Shin, M. Stanley, E. Breakenridge, S. Singh, and N. M. Ridler(2024)SI traceable RF and microwave power measurements at cryogenic temperatures.InProc. Conf. Precis. Electromagn. Meas. (CPEM),Denver, CO, USA,pp. 1–2.External Links:DocumentCited by:§I.
- [6]A. Celotto, A. Alocco, B. Galvano, L. Fasolo, E. Palumbo, L. Callegaro, L. Oberto, P. Livreri, and E. Enrico(2026)Device-agnostic microwave noise metrology for nonlinear cryogenic quantum devices.External Links:2605.28808,LinkCited by:§I.
- [7]A. A. Clerk, M. H. Devoret, S. M. Girvin, F. Marquardt, and R. J. Schoelkopf(2010)Introduction to quantum noise, measurement, and amplification.Rev. Mod. Phys.82(2),pp. 1155–1208.External Links:DocumentCited by:§I.
- [8]T. Descamps, L. Andersson, V. Buccheri, S. Sundelin, M. A. Aamir, and S. Gasparinetti(2026)In situ calibration of microwave attenuation and gain using a cryogenic on-chip attenuator.External Links:2602.16889,LinkCited by:§I.
- [9]M. H. Devoret and R. J. Schoelkopf(2013)Superconducting circuits for quantum information: an outlook.Science339(6124),pp. 1169–1174.External Links:DocumentCited by:§I.
- [10]R. C. Dhuley(2019)Pressed copper and gold-plated copper contacts at low temperatures—a review of thermal contact resistance.Cryogenics101,pp. 111–124.External Links:DocumentCited by:§III.
- [11]I. Didschuns, A. L. Woodcraft, D. Bintley, and P. C. Hargrave(2004)Thermal conductance measurements of bolted copper to copper joints at sub-Kelvin temperatures.Cryogenics44(5),pp. 293–299.External Links:DocumentCited by:§III.
- [12]J. W. Ekin(2006)Experimental techniques for low-temperature measurements: cryostat design, material properties and superconductor critical-current testing.Oxford Univ. Press,Oxford, U.K..External Links:DocumentCited by:§III,§III.
- [13]A. Ferrero and U. Pisani(1992)Two-port network analyzer calibration using an unknown ‘thru’.IEEE Microw. Guided Wave Lett.2(12),pp. 505–507.External Links:DocumentCited by:§I.
- [14]J.-P. Girard, R. E. Lake, W. Liu, R. Kokkoniemi, E. Visakorpi, J. Govenius, and M. Möttönen(2023)Cryogenic sensor enabling broad-band and traceable power measurements.Rev. Sci. Instrum.94(5),pp. 054710.External Links:DocumentCited by:§I.
- [15]Joint Committee for Guides in Metrology(2008)Evaluation of measurement data—guide to the expression of uncertainty in measurement.Note:JCGM 100:2008Cited by:§I.
- [16]M. Kjaergaard, M. E. Schwartz, J. Braumüller, P. Krantz, J. I.-J. Wang, S. Gustavsson, and W. D. Oliver(2020)Superconducting qubits: current state of play.Annu. Rev. Condens. Matter Phys.11(1),pp. 369–395.External Links:DocumentCited by:§I.
- [17]R. Kokkoniemi, J.-P. Girard, D. Hazra, A. Laitinen, J. Govenius, R. E. Lake, I. Sallinen, M. Partanen, V. Vesterinen, P. Hakonen, and M. Möttönen(2019)Nanobolometer with ultralow noise equivalent power.Commun. Phys.2,pp. 124.External Links:DocumentCited by:§I.
- [18]R. Kokkoniemi, J.-P. Girard, D. Hazra, A. Laitinen, J. Govenius, R. E. Lake, I. Sallinen, V. Vesterinen, M. Partanen, J. Y. Tan, K. W. Chan, K. Y. Tan, P. J. Hakonen, and M. Möttönen(2020)Bolometer operating at the threshold for circuit quantum electrodynamics.Nature586(7827),pp. 47–51.External Links:DocumentCited by:§I.
- [19]P. Krantz, M. Kjaergaard, F. Yan, T. P. Orlando, S. Gustavsson, and W. D. Oliver(2019)A quantum engineer’s guide to superconducting qubits.Appl. Phys. Rev.6(2),pp. 021318.External Links:DocumentCited by:§I.
- [20]S. Krinner, S. Storz, P. Kurpiers, P. Magnard, J. Heinsoo, R. Keller, J. Lütolf, C. Eichler, and A. Wallraff(2019-12)Engineering cryogenic setups for 100-qubit scale superconducting circuit systems.EPJ Quantum Technology6.External Links:Document,ISSN 21960763Cited by:§II-A,§V-B.
- [21]N. T. Larsen(1977)NBS type IV RF power meter operation and maintenance.Technical reportTechnical ReportNBSIR 77-866,National Bureau of Standards,Boulder, CO, USA.Cited by:§I.
- [22]A. C. Macpherson and D. M. Kerns(1955)A microwave microcalorimeter.Rev. Sci. Instrum.26(1),pp. 27–33.External Links:DocumentCited by:§I.
- [23]L. Oberto, E. Shokrolahzade, E. Enrico, L. Fasolo, A. Celotto, B. Galvano, A. Alocco, P. Terzi, F. A. Mubarak, and M. Spirito(2025)Measurement and calibration approaches for full two-port scattering parameters at mK temperatures.Note:arXiv:2505.19922External Links:2505.19922Cited by:§I,§II-E,§IV,§V-D.
- [24]Frank. Pobell(2007)Matter and methods at low temperatures.Springer.External Links:ISBN 9783540463566Cited by:§V-B.
- [25]L. M. Ranzani, L. F. Spietz, Z. Popović, and J. Aumentado(2013)Two-port microwave calibration at millikelvin temperatures.Rev. Sci. Instrum.84(3),pp. 034704.External Links:DocumentCited by:§I.
- [26]A. Rumiantsev and N. M. Ridler(2008)VNA calibration.IEEE Microw. Mag.9(3),pp. 86–99.External Links:DocumentCited by:§I.
- [27]S.-H. Shin, M. Stanley, J. Skinner, S. E. de Graaf, and N. M. Ridler(2024)Broadband coaxial S-parameter measurements for cryogenic quantum technologies.IEEE Trans. Microw. Theory Techn.72(4),pp. 2220–2228.External Links:DocumentCited by:§I.
- [28]S. Simbierowicz, V. Y. Monarkha, S. Singh, N. Messaoudi, P. Krantz, and R. E. Lake(2022)Microwave calibration of qubit drive line components at millikelvin temperatures.Appl. Phys. Lett.120(5),pp. 054004.External Links:DocumentCited by:§I.
- [29]M. Stanley, M. Celep, A. Elarabi, M. Salter, D. Singh, J. Skinner, S.-H. Shin, and N. M. Ridler(2025)A technique to improve accuracy of S-parameter measurements of coaxial connectorized devices at cryogenic temperatures.IEEE Trans. Instrum. Meas.74,pp. 1–12.Note:Art. no. 8005612External Links:DocumentCited by:§I.
- [30]M. Stanley, M. Salter, J. Urbonas, J. Skinner, S.-H. Shin, S. E. de Graaf, and N. M. Ridler(2024)Characterizing S-parameters of microwave coaxial devices with up to four ports at temperatures of 3 K and above for quantum computing applications.IEEE Trans. Instrum. Meas.73,pp. 1–6.Note:Art. no. 1500906External Links:DocumentCited by:§I.
- [31]A. L. Woodcraft and A. Gray(2009)A low temperature thermal conductivity database.InAIP Conf. Proc.,Vol.1185,pp. 681–684.External Links:DocumentCited by:§III.

## 


- 


Major funding support from
