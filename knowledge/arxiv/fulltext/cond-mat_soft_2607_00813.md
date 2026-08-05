# The Role of Compressibility in Modified Quasi-Linear Viscoelasticity: A Comparison of Simple Shear and Torsion

**arXiv ID**: 2607.00813v1
**Authors**: Valentina Balbi, Griffen Small
**Published**: 2026-07-01
**Categories**: cond-mat.soft, math-ph
**Comments**: 22 pages, 8 figures
**HTML URL**: https://arxiv.org/html/2607.00813v1

## Abstract

We investigate the role of compressibility in the modified quasi-linear viscoelastic (MQLV) constitutive framework for soft solids at finite strain, where shear and bulk responses are governed by distinct relaxation functions. Analytical and semi-analytical results are derived for simple shear and torsion, under incompressible and slightly compressible assumptions. We show that compressibility affects the response only when volume changes occur: under isochoric deformations, the bulk contribution vanishes, while even small deviations from isochoricity significantly alter the normal response. Shear stress and torque are largely insensitive to compressibility, whereas normal stress and axial force exhibit pronounced sensitivity due to the coupling between shear and bulk relaxation. We further demonstrate that volumetric effects interact with the Poynting effect: in simple shear they oppose each other, reducing relaxation, while in torsion they reinforce each other, enhancing it. These trends agree with brain tissue experiments but reveal limitations of the slightly compressible model for highly compressible materials, such as agarose gels. Overall, the results emphasise the importance of accounting for compressibility in modelling normal stress responses and motivate the development of fully compressible formulations and numerical implementations.

## Full Text

The Role of Compressibility in Modified Quasi-Linear Viscoelasticity: A Comparison of Simple Shear and Torsion

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
- License: CC BY-NC-SA 4.0arXiv:2607.00813v1 [cond-mat.soft] 01 Jul 202611footnotetext:Valentina Balbi: School of Mathematical and Statistical Sciences, University of Galway, College Road, Galway, H91 TK33, Ireland. Email: vbalbi@universityofgalway.ie22footnotetext:Griffen Small: Department of Mechanical and Manufacturing Engineering, University of Calgary, 2500 University Drive NW, Calgary, Alberta, T2N 1N4, Canada

## The Role of Compressibility in Modified Quasi-Linear Viscoelasticity: A Comparison of Simple Shear and TorsionValentina Balbi1and Griffen Small2

## Abstract

We investigate the role of compressibility in the modified quasi-linear viscoelastic (MQLV) constitutive framework for soft solids at finite strain, where shear and bulk responses are governed by distinct relaxation functions. Analytical and semi-analytical results are derived for simple shear and torsion, under incompressible and slightly compressible assumptions.
We show that compressibility affects the response only when volume changes occur: under isochoric deformations, the bulk contribution vanishes, while even small deviations from isochoricity significantly alter the normal response. Shear stress and torque are largely insensitive to compressibility, whereas normal stress and axial force exhibit pronounced sensitivity due to the coupling between shear and bulk relaxation.
We further demonstrate that volumetric effects interact with the Poynting effect: in simple shear they oppose each other, reducing relaxation, while in torsion they reinforce each other, enhancing it. These trends agree with brain tissue experiments but reveal limitations of the slightly compressible model for highly compressible materials, such as agarose gels.
Overall, the results emphasise the importance of accounting for compressibility in modelling normal stress responses and motivate the development of fully compressible formulations and numerical implementations.

## 1Introduction

The mechanical behaviour of soft solids, including biological tissues and polymeric gels, is characterised by large deformations, strong non-linearity and pronounced time-dependent effects. Capturing these features within a unified constitutive framework remains a central problem in continuum mechanics, with important implications for biomechanics and engineering applications. A wide range of constitutive approaches to non-linear viscoelasticity have been proposed, broadly classified into integral-type, differential and internal-variable models. Integral formulations, based on the theory of materials with memory, express the stress as a functional of the entire deformation history, as in the classical Pipkin–Rogers and K–BKZ models[55]. By contrast, differential models relate stress to strain and its time derivatives, but often struggle to capture long-term relaxation behaviour[9]. Internal-variable approaches, grounded in thermodynamics, introduce additional state variables to describe dissipative mechanisms and are closely related to multiplicative frameworks, in which the deformation gradient is decomposed into elastic and viscous parts[45,48,47].

Within this broad framework, quasi-linear viscoelasticity (QLV), originally introduced by Fung[24], has become one of the most widely used models in biomechanics due to its simplicity and ability to incorporate non-linear elasticity and time dependence. QLV is an integral-type model, in which the stress is expressed as the convolution of a scalar relaxation function with an instantaneous elastic response[24]. While this separable structure is computationally attractive and has been successfully applied to a wide variety of soft tissues, it also imposes significant limitations. In particular, the use of a single scalar relaxation function restricts the model to incompressible behaviour and prevents a consistent description of general three-dimensional viscoelastic responses[15].

To overcome these limitations, the modified quasi-linear viscoelastic (MQLV) framework was developed by De Pascaliset al.[15], in which the relaxation behaviour is represented by a tensorial relaxation function. This formulation enables a consistent decomposition of the stress into volumetric and deviatoric contributions, each governed by its own relaxation function, thereby ensuring that the model reduces to classical linear viscoelasticity in the small-strain limit. The MQLV model has been applied to study various deformation modes, including uniaxial tension[15], simple shear[16], torsion[50,46]and inflation[17], and has also been extended to anisotropic materials[6,5]. In particular, the MQLV approach provides a natural way to incorporate physically distinct relaxation mechanisms associated with the bulk and shear responses of a material.

Despite these advances, most applications of MQLV theory have focused on incompressible materials, reflecting the common assumption that soft solids undergo negligible volume changes. However, both experimental evidence and theoretical considerations indicate that all real materials are compressible to some extent. For example, skeletal muscle exhibits measurable deviations from isochoric behaviour due to fluid exchange and vascular effects during deformation[11]; ligaments and tendons undergo significant volume changes under tensile loading, as evidenced by strain-dependent Poisson’s ratios[53]and brain tissue displays coupled volumetric and mechanical responses arising from its highly hydrated multiphasic structure[25].

Motivated by these observations, compressible viscoelastic behaviour has been investigated within several constitutive frameworks, including internal-variable formulations at finite strain[27,28], phenomenological models for polymers[12]and hereditary formulations used in computational mechanics[13]. While these models incorporate compressibility through the volumetric response, the time-dependent behaviour is often described by a single effective relaxation function or by relaxation processes that act uniformly across the stress. For instance, internal-variable models based on short- and long-term mechanisms[1]introduce multiple time scales, but these are embedded within differential evolution equations and do not correspond to independent tensorial relaxation functions associated with distinct physical modes of deformation. Moreover, poroviscoelastic models attribute volume changes to fluid transport rather than intrinsic solid relaxation[25], leaving open the question of how multiple relaxation mechanisms interact in compressible viscoelastic solids.

In addition to these modelling considerations, experimental observations provide further evidence that multiple relaxation mechanisms may be active in soft solids. In particular, torsion experiments on ovine brain tissue[50,51]and2%2\%w/v agarose gel[7]reveal that the normalised relaxation curves of torque and axial force do not coincide, as shown in Figure1. This discrepancy is especially pronounced in agarose gels and suggests a competition between distinct relaxation processes. Such behaviour cannot be captured by classical QLV models with a single relaxation function but is naturally accommodated within the MQLV framework through the presence of multiple relaxation mechanisms.(a)(b)Figure 1:Normalised torqueτ¯\overline{\tau}and axial forceN¯z\overline{N}_{z}from torsion tests performed on (a) 10 brain tissue samples and (b) 10 agarose gel samples of radius12.5​mm12.5\,\mathrm{mm}and height∼10​mm\sim 10\,\mathrm{mm}. Data are presented as mean (solid curves) and standard deviation (surrounding colour bands). The twist rateϕ˙0=40​rad​m−1​s−1\dot{\phi}_{0}=40\,\mathrm{rad}\,\mathrm{m}^{-1}\,\mathrm{s}^{-1}was the same in both cases, but the final value of the twist differed, withϕ0=88​rad​m−1\phi_{0}=88\,\mathrm{rad}\,\mathrm{m}^{-1}for brain tissue andϕ0=25​rad​m−1\phi_{0}=25\,\mathrm{rad}\,\mathrm{m}^{-1}for agarose gel.

The aim of this paper is therefore to investigate the effect of compressibility on the modified quasi-linear viscoelastic model for soft solids. We consider two constitutive settings—slightly compressible and incompressible—and analyse their predictions for two canonical deformations: simple shear and torsion. For simple shear, we examine both isochoric and nearly-isochoric deformations, highlighting the influence of volumetric relaxation on both shear and normal stress components. For torsion, we derive analytical results in the incompressible case and develop a perturbative approach for slightly compressible solids, enabling a systematic assessment of the roles of bulk and shear relaxation in determining the torque and axial force response.

## 2Modified quasi-linear viscoelasticity

In this section, we outline the equations governing the deformation of an isotropic viscoelastic soft solid within the MQLV framework. We consider the slightly compressible and incompressible cases and, for both, formulate the corresponding model and specify the associated constitutive assumptions for the relaxation and strain energy functions. For a more detailed and comprehensive account of the isotropic MQLV theory, including derivations of the associated equations, we refer the reader to[49,6,46,15].

## 2.1Compressible form

In the large-deformation regime, the motion of a solid continuum is described by a deformation𝝌\bm{\chi}that transforms a material point with position vector𝑿\bm{X}in the undeformed configuration at timet=0t=0to a point with position vector𝒙​(t)\bm{x}(t)in the deformed configuration, such that𝒙​(t)=𝝌​(𝑿,t)\bm{x}(t)=\bm{\chi}(\bm{X},t). The associated deformation gradient tensor is defined as𝑭=∂𝒙/∂𝑿\bm{F}=\partial\bm{x}/\penalty 50\partial\bm{X}, from which various kinematic tensors can be derived, including the right Cauchy–Green deformation tensor𝑪=𝑭T​𝑭\bm{C}=\bm{F}^{\mathrm{T}}\bm{F}and the left Cauchy–Green deformation tensor𝑩=𝑭​𝑭T\bm{B}=\bm{F}\bm{F}^{\mathrm{T}}.

In the isotropic MQLV framework, the constitutive equation in its most general form can be expressed in terms of the second Piola–Kirchhoff stress tensor as follows[49,6]:𝚷(t)=J(t)𝑭(t)−1(𝔾(0):𝑻e(t))𝑭(t)−T+∫0tJ(s)𝑭(s)−1(𝔾′(t−s):𝑻e(s))𝑭(s)−Tds,\bm{\Pi}(t)=J(t)\bm{F}(t)^{-1}\left(\mathbb{G}(0)\bm{:}\bm{T}^{\mathrm{e}}(t)\right)\bm{F}(t)^{-\mathrm{T}}+\int_{0}^{t}J(s)\bm{F}(s)^{-1}\left(\mathbb{G}^{\prime}(t-s)\bm{:}\bm{T}^{\mathrm{e}}(s)\right)\bm{F}(s)^{-\mathrm{T}}\differential{s},(1)

whereJ=det​𝑭J=\mathrm{det}\,\bm{F}is the volume ratio,𝑻e\bm{T}^{\mathrm{e}}is the elastic Cauchy stress tensor and the prime denotes a derivative with respect to the argument of the function. The reduced relaxation tensor𝔾=∑i=12Gi​𝕀i\mathbb{G}=\sum_{i=1}^{2}G_{i}\mathbb{I}_{i}is a fourth-order tensor whose componentsGiG_{i}are the relaxation functions that characterise the viscoelastic behaviour of the material. By choosing an appropriate tensor basis{𝕀1,𝕀2}\{\mathbb{I}_{1},\mathbb{I}_{2}\}for𝔾\mathbb{G}, these functions can be identified with the different time-dependent mechanical moduli of the material. In particular, as shown in[49,6], by expressing the reduced relaxation tensor in terms of the basis:(𝕀1)i​j​k​l=13​δi​j​δk​land(𝕀2)i​j​k​l=12​(δi​k​δj​l+δi​l​δj​k)−13​δi​j​δk​l,\left(\mathbb{I}_{1}\right)_{ijkl}=\frac{1}{3}\delta_{ij}\delta_{kl}\qquad\text{and}\qquad\left(\mathbb{I}_{2}\right)_{ijkl}=\frac{1}{2}(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})-\frac{1}{3}\delta_{ij}\delta_{kl},(2)

withδi​j\delta_{ij}denoting the Kronecker delta, we can identify the associated components as the normalised bulk and shear moduli:G1​(t)=κ​(t)κ0andG2​(t)=μ​(t)μ0,G_{1}(t)=\frac{\kappa(t)}{\kappa_{0}}\qquad\text{and}\qquad G_{2}(t)=\frac{\mu(t)}{\mu_{0}},(3)

whereκ​(t)\kappa(t)andμ​(t)\mu(t)denote the relaxation functions for the bulk and shear moduli, respectively, whileκ​(0)=κ0\kappa(0)=\kappa_{0}andμ​(0)=μ0\mu(0)=\mu_{0}denote the corresponding instantaneous moduli.
With this same choice of basis, the double contractions between𝔾\mathbb{G}and𝑻e\bm{T}^{\mathrm{e}}in (1) naturally split the elastic response into separate hydrostatic and deviatoric parts[49,6]. Altogether, this yields a particularly tractable form of the MQLV constitutive equation, expressed in terms of two distinct and physically meaningful relaxation functions for the bulk and shear moduli[49,6]:𝚷​(t)\displaystyle\bm{\Pi}(t)=(𝚷He​(t)+1κ0​∫0tκ′​(t−s)​𝚷He​(s)​ds)\displaystyle=\left(\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}(t)+\frac{1}{\kappa_{0}}\int_{0}^{t}\kappa^{\prime}(t-s)\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}(s)\differential{s}\right)+(𝚷De​(t)+1μ0​∫0tμ′​(t−s)​𝚷De​(s)​ds),\displaystyle+\left(\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}(t)+\frac{1}{\mu_{0}}\int_{0}^{t}\mu^{\prime}(t-s)\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}(s)\differential{s}\right),(4)

where we have defined the following terms:{𝚷He=J​𝑭−1​𝑻He​𝑭−T,𝚷De=J​𝑭−1​𝑻De​𝑭−T,𝑻He=13​(tr​𝑻e)​𝑰,𝑻De=𝑻e−13​(tr​𝑻e)​𝑰,\left\{\begin{aligned} &\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}=J\bm{F}^{-1}\bm{T}^{\mathrm{e}}_{\mathrm{H}}\bm{F}^{-\mathrm{T}},\qquad&&\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}=J\bm{F}^{-1}\bm{T}^{\mathrm{e}}_{\mathrm{D}}\bm{F}^{-\mathrm{T}},\\
&\bm{T}^{\mathrm{e}}_{\mathrm{H}}=\frac{1}{3}\left(\mathrm{tr}\,\bm{T}^{\mathrm{e}}\right)\bm{I},\qquad&&\bm{T}^{\mathrm{e}}_{\mathrm{D}}=\bm{T}^{\mathrm{e}}-\frac{1}{3}\left(\mathrm{tr}\,\bm{T}^{\mathrm{e}}\right)\bm{I},\end{aligned}\right.(5)

with𝑰\bm{I}being the identity tensor. Here,𝑻He\bm{T}^{\mathrm{e}}_{\mathrm{H}}and𝑻De\bm{T}^{\mathrm{e}}_{\mathrm{D}}denote the hydrostatic and deviatoric parts, respectively, of the elastic Cauchy stress tensor𝑻e\bm{T}^{\mathrm{e}}, while𝚷He\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}and𝚷De\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}denote the corresponding second Piola–Kirchhoff stress tensors. Applying the inverse Piola transformation𝑻=J−1​𝑭​𝚷​𝑭T\bm{T}=J^{-1}\bm{F}\bm{\Pi}\bm{F}^{\mathrm{T}}to the second Piola–Kirchhoff stress tensor (4), we obtain the corresponding MQLV constitutive equation for the (viscoelastic) Cauchy stress tensor:𝑻​(t)\displaystyle\bm{T}(t)=J​(t)−1​𝑭​(t)​(𝚷He​(t)+1κ0​∫0tκ′​(t−s)​𝚷He​(s)​ds)​𝑭​(t)T\displaystyle=J(t)^{-1}\bm{F}(t)\left(\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}(t)+\frac{1}{\kappa_{0}}\int_{0}^{t}\kappa^{\prime}(t-s)\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}(s)\differential{s}\right)\bm{F}(t)^{\mathrm{T}}+J​(t)−1​𝑭​(t)​(𝚷De​(t)+1μ0​∫0tμ′​(t−s)​𝚷De​(s)​ds)​𝑭​(t)T.\displaystyle+J(t)^{-1}\bm{F}(t)\left(\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}(t)+\frac{1}{\mu_{0}}\int_{0}^{t}\mu^{\prime}(t-s)\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}(s)\differential{s}\right)\bm{F}(t)^{\mathrm{T}}.(6)

For soft solids, the simplest choice for the time-dependent relaxation functionsκ​(t)\kappa(t)andμ​(t)\mu(t)in (6) are one-term Prony series of the form:κ​(t)=κ∞+(κ0−κ∞)​e−t/τHandμ​(t)=μ∞+(μ0−μ∞)​e−t/τD,\kappa(t)=\kappa_{\infty}+\left(\kappa_{0}-\kappa_{\infty}\right)\mathrm{e}^{-t/\penalty 50\tau_{\mathrm{H}}}\qquad\text{and}\qquad\mu(t)=\mu_{\infty}+\left(\mu_{0}-\mu_{\infty}\right)\mathrm{e}^{-t/\penalty 50\tau_{\mathrm{D}}},(7)

whereκ∞\kappa_{\infty}andμ∞\mu_{\infty}denote the long-time bulk and shear moduli, respectively, whileτH\tau_{\mathrm{H}}andτD\tau_{\mathrm{D}}denote the associated relaxation times for the bulk and shear response. In practice, however, soft solids often require multi-term Prony series to accurately fit stress relaxation data[39,50,23,33]. Nevertheless, one-term series are typically sufficient to capture the main qualitative features of the relaxation response[6,5,17,16,15]and result in a considerably simpler form of the MQLV constitutive equation than would be obtained using multi-term series.

In addition to the choice of relaxation functions, constitutive assumptions must also be specified for the instantaneous response. Non-linear elastic behaviour can be readily incorporated in (6) through the elastic Cauchy stress tensor𝑻e\bm{T}^{\mathrm{e}}by adopting a hyperelastic constitutive framework. In this setting,𝑻e\bm{T}^{\mathrm{e}}is expressed in terms of a strain energy functionWW, which, for isotropic compressible materials, depends only on the principal invariantsI1I_{1},I2I_{2}andI3I_{3}of𝑪\bm{C}, defined as:I1=tr​𝑪,I2=12​(I12−tr​𝑪2)andI3=det​𝑪=J2.I_{1}=\mathrm{tr}\,\bm{C},\qquad I_{2}=\frac{1}{2}\left(I^{2}_{1}-\mathrm{tr}\,\bm{C}^{2}\right)\quad\text{and}\quad I_{3}=\mathrm{det}\,\bm{C}=J^{2}.(8)

This form of the strain energy function leads to the following representation formula for𝑻e\bm{T}^{\mathrm{e}}[21,2,4,26,40]:𝑻e=β0​𝑰+β1​𝑩+β−1​𝑩−1,\bm{T}^{\mathrm{e}}=\beta_{0}\bm{I}+\beta_{1}\bm{B}+\beta_{-1}\bm{B}^{-1},(9)

where the response functionsβ0\beta_{0},β1\beta_{1}andβ−1\beta_{-1}are given by:{β0=2​J−1​(I2​W2+I3​W3),β1=2​J−1​W1,β−1=−2​J​W2,\left\{\begin{aligned} &\beta_{0}=2J^{-1}\left(I_{2}W_{2}+I_{3}W_{3}\right),\\
&\beta_{1}=2J^{-1}W_{1},\\
&\beta_{-1}=-2JW_{2},\end{aligned}\right.(10)

withWi=∂W/∂IiW_{i}=\partial W/\penalty 50\partial I_{i}fori=1,2,3i=1,2,3. Taking the trace of (9) and making use of the identitytr​𝑩−1=I2/I3\mathrm{tr}\,\bm{B}^{-1}=I_{2}/\penalty 50I_{3}gives:tr​𝑻e=3​β0+I1​β1+I2​β−1I3.\mathrm{tr}\,\bm{T}^{\mathrm{e}}=3\beta_{0}+I_{1}\beta_{1}+\frac{I_{2}\beta_{-1}}{I_{3}}.(11)

Using (9) and (10), together with (11), the elastic second Piola–Kirchhoff stress tensors in (5) take the form:{𝚷He=2​(23​I2​W2+13​I1​W1+I3​W3)​𝑪−1,𝚷De=2​(W1​𝑰+13​(I2​W2−I1​W1)​𝑪−1−I3​W2​𝑪−2).\left\{\begin{aligned} &\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}=2\left(\frac{2}{3}I_{2}W_{2}+\frac{1}{3}I_{1}W_{1}+I_{3}W_{3}\right)\bm{C}^{-1},\\
&\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}=2\left(W_{1}\bm{I}+\frac{1}{3}\left(I_{2}W_{2}-I_{1}W_{1}\right)\bm{C}^{-1}-I_{3}W_{2}\bm{C}^{-2}\right).\end{aligned}\right.(12)

Substituting (12) into (6) then yields the MQLV constitutive equation for an isotropic compressible viscoelastic solid with instantaneous hyperelastic response.

## 2.2Slightly compressible form

A compromise between perfect incompressibility and full compressibility is slight-compressibility. A material is classified as slightly compressible (or nearly incompressible) when its instantaneous bulk modulus is finite but several orders of magnitude larger than its instantaneous shear modulus[30]. The most common approach to modelling slight compressibility in isotropic hyperelastic solids is to assume, largely for mathematical simplicity, that the strain energy function can be additively decomposed into uncoupled isochoric and volumetric contributions as follows[2,19,31,29,26]:W=ψ​(I¯1,I¯2)+U​(J),W=\psi(\bar{I}_{1},\bar{I}_{2})+U(J),(13)

whereI¯1=tr​𝑪¯\bar{I}_{1}=\mathrm{tr}\,\overline{\bm{C}}andI¯2=tr​𝑪¯−1\bar{I}_{2}=\mathrm{tr}\,\overline{\bm{C}}^{-1}are the first and second principal invariants of the modified right Cauchy–Green deformation tensor𝑪¯=J−2/3​𝑪\overline{\bm{C}}=J^{-2/\penalty 503}\bm{C}, respectively. The first termψ\psirepresents the isochoric contribution and is obtained from the corresponding incompressible strain energy function by replacingI1I_{1}andI2I_{2}with the modified invariantsI¯1\bar{I}_{1}andI¯2\bar{I}_{2}, respectively. The second termUU, which depends only onJJ, measures volume change and thus accounts for deviations from perfect incompressibility. This implementation of slight compressibility is widely used in finite element packages, including FEBio[37], Abaqus[14]and Ansys[3].

While the slightly compressible form of the strain energy function (13) was originally conceived of for hyperelastic solids, it can be readily incorporated in the MQLV constitutive equation (6) through the elastic Cauchy stress tensor𝑻e\bm{T}^{\mathrm{e}}or, equivalently, through the elastic second Piola–Kirchhoff tensor𝚷e\bm{\Pi}^{\mathrm{e}}. By substituting (13) into (12) and applying the chain rule, we obtain:{𝚷He=J1/3​U′​(J)​𝑪¯−1,𝚷De=23​J−2/3​[3​ψ1​𝑰−(I¯1​ψ1−I¯2​ψ2)​𝑪¯−1−ψ2​𝑪¯−2],\left\{\begin{aligned} &\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}=J^{1/\penalty 503}U^{\prime}(J)\mkern 1.0mu\mkern 1.0mu\overline{\bm{C}}^{-1},\\
&\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}=\frac{2}{3}J^{-2/\penalty 503}\left[3\psi_{1}\bm{I}-\left(\bar{I}_{1}\psi_{1}-\bar{I}_{2}\psi_{2}\right)\overline{\bm{C}}^{-1}-\psi_{2}\overline{\bm{C}}^{-2}\right],\end{aligned}\right.(14)

whereψi=∂ψ/∂I¯i\psi_{i}=\partial\psi/\penalty 50\partial\bar{I}_{i}fori=1,2,3i=1,2,3. Substitution of (14) into (6) then yields the MQLV constitutive equation for an isotropic slightly compressible viscoelastic solid with instantaneous hyperelastic response.

In this work, we further specialise this MQLV formulation by specifying the following slightly compressible Mooney–Rivlin strain energy function[52,54,38]:W=c1​(I¯1−3)+c2​(I¯2−3)+12​κ0​(ln⁡J)2,W=c_{1}(\bar{I}_{1}-3)+c_{2}(\bar{I}_{2}-3)+\frac{1}{2}\kappa_{0}(\ln J)^{2},(15)

corresponding toψ=c1​(I¯1−3)+c2​(I¯2−3)\psi=c_{1}(\bar{I}_{1}-3)+c_{2}(\bar{I}_{2}-3)andU=κ0​(ln⁡J)2/2U=\kappa_{0}(\ln J)^{2}/\penalty 502in (13). We note in passing that a myriad of alternative forms for the volumetric termUUhave been proposed in the literature (see, for example,[41,2,29,22]), which differ primarily in the associated mechanical response for large and small volume dilations[2]. The stress relaxation behaviour of this slightly compressible model will be considered later.

## 2.3Incompressible limit

To conclude this section, we examine the incompressible limit, following the approach of[46]. In this limit, the volume ratio tends to unity (J​(t)→1J(t)\to 1), while the bulk modulus tends to infinity (κ​(t)→∞\kappa(t)\to\infty), and so (6) becomes:𝑻​(t)=𝑭​(t)​(𝚷De​(t)+1μ0​∫0tμ′​(t−s)​𝚷De​(s)​ds)​𝑭​(t)T−p​(t)​𝑰,\bm{T}(t)=\bm{F}(t)\left(\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}(t)+\frac{1}{\mu_{0}}\int_{0}^{t}\mu^{\prime}(t-s)\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}(s)\differential{s}\right)\bm{F}(t)^{\mathrm{T}}-p(t)\bm{I},(16)

where now, from (5), we have:𝚷De=2​[W1​𝑰+13​(I2​W2−I1​W1)​𝑪−1−W2​𝑪−2]\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}=2\left[W_{1}\bm{I}+\frac{1}{3}\left(I_{2}W_{2}-I_{1}W_{1}\right)\bm{C}^{-1}-W_{2}\bm{C}^{-2}\right](17)

and the Lagrange multiplier of incompressibility is given by:p​(t)=−limJ​(t)→1,κ​(t)→∞J​(t)−1​𝑭​(t)​(𝚷He​(t)+1κ0​∫0tκ′​(t−s)​𝚷He​(s)​ds)​𝑭​(t)T.p(t)=-\displaystyle\lim_{\begin{subarray}{c}J(t)\to 1,\\[1.0pt]
\kappa(t)\to\infty\end{subarray}}J(t)^{-1}\bm{F}(t)\left(\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}(t)+\frac{1}{\kappa_{0}}\int_{0}^{t}\kappa^{\prime}(t-s)\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}(s)\differential{s}\right)\bm{F}(t)^{\mathrm{T}}.(18)

We note that in the incompressible limit, the relaxation function for the bulk modulusκ​(t)\kappa(t)is not prescribed explicitly, as in (7). Rather, it is absorbed into the Lagrange multiplierp​(t)p(t)in (16), which itself is introduced to enforce the incompressibility constraint. Accordingly,p​(t)p(t)is determined by solving the equation of motion subject to appropriate boundary conditions. Under the common assumptions that the deformation is slow enough that inertial effects can be neglected (the quasi-static assumption) and external body forces are negligible compared to applied surface forces, the equation of motion reduces to[21,2,4,26,40]:div​𝑻=𝟎,\mathrm{div}\,\bm{T}=\bm{0},(19)

wherediv\mathrm{div}denotes the divergence operator in the deformed configuration.

In this work, we further specialise this incompressible MQLV model by specifying the following incompressible Mooney–Rivlin strain energy function[50,8,20,44]:W=c1​(I1−3)+c2​(I2−3).W=c_{1}(I_{1}-3)+c_{2}(I_{2}-3).(20)

In what follows, we use both the incompressible and slightly compressible Mooney–Rivlin MQLV models formulated in this section, with Prony series relaxation functions given by (7), to analyse their stress relaxation response under four different deformation modes: isochoric and nearly-isochoric simple shear, followed by isochoric and nearly-isochoric torsion.

## 3Simple shear of a solid cuboid

In this section, we consider both the isochoric and nearly-isochoric simple shear of a solid cuboid and derive analytical expressions for the corresponding shear and normal stresses for the incompressible, compressible and slightly compressible MQLV models formulated in Section2.

## 3.1Isochoric simple shear

In classical simple shear, a cuboid is deformed into a parallelepiped by displacing the top face relative to the fixed bottom face through the application of both shear and normal tractions, without changing the volume or dimensions of the cuboid (see Figure2(a)). This deformation, subsequently referred to as isochoric simple shear, can be written as:{x1=X1+k​(t)​X2,x2=X2,x3=X3,\left\{\begin{aligned} &x_{1}=X_{1}+k(t)X_{2},\\
&x_{2}=X_{2},\\
&x_{3}=X_{3},\end{aligned}\right.(21)

where(X1,X2,X3)(X_{1},X_{2},X_{3})and(x1,x2,x3)(x_{1},x_{2},x_{3})denote the Cartesian coordinates of a material point before and after deformation, respectively, andk​(t)k(t)is the amount of shear. By introducing the fixed Cartesian bases{𝑬1,𝑬2,𝑬3}\{\bm{E}_{1},\bm{E}_{2},\bm{E}_{3}\}and{𝒆1,𝒆2,𝒆3}\{\bm{e}_{1},\bm{e}_{2},\bm{e}_{3}\}for the undeformed and deformed configurations, respectively, we can write the deformation gradient𝑭=Fa​A​𝒆a⊗𝑬A\bm{F}=F_{aA}\,\bm{e}_{a}\otimes\bm{E}_{A}associated with the deformation (21) as follows:𝑭​(t)=(1k​(t)0010001),\bm{F}(t)=\left(\begin{array}[]{ccc}1&k(t)&0\\
0&1&0\\
0&0&1\end{array}\right),(22)

withJ=det​𝑭=1J=\mathrm{det}\,\bm{F}=1. The right Cauchy–Green deformation tensor𝑪=𝑭T​𝑭\bm{C}=\bm{F}^{\mathrm{T}}\bm{F}is then given by:𝑪​(t)=(1k​(t)0k​(t)k​(t)2+10001),\bm{C}(t)=\left(\begin{array}[]{ccc}1&k(t)&0\\[1.0pt]
k(t)&k(t)^{2}+1&0\\[1.0pt]
0&0&1\end{array}\right),(23)

from which we can easily compute the corresponding principal invariants (8):I1=k2+3,I2=k2+3andI3=1.I_{1}=k^{2}+3,\qquad I_{2}=k^{2}+3\qquad\text{and}\qquad I_{3}=1.(24)

Figure 2:Deformation of a cuboid under (a) isochoric simple shear𝝌0\bm{\chi}_{0}and (b) nearly-isochoric simple shear𝝌δ\bm{\chi}_{\delta}. In both cases, shear and normal tractions must be applied to the top face of the cuboid to maintain the deformation.

Since the deformation is homogeneous, the equation of motion (19) is automatically satisfied for both the incompressible and slightly compressible MQLV models considered in this paper. Maintaining the deformation nevertheless requires the application of both shear and normal tractions on the top face of the cuboid. In this section, we derive analytical expressions for the corresponding stresses for each model.

Before proceeding, we note in passing that, in addition to the shear and normal tractions mentioned above, surface tractions are also required on the slanted faces of the deformed cuboid. In reality, however, such tractions are never applied in simple shear experiments, causing the slanted faces to bend and the deformation to become inhomogeneous, resulting in large variations in the distribution of the stresses[18]. These undesirable effects are minimised in practice by using sufficiently thin cuboids, with the length and width equal and both at least four times greater than the height[18,20,44].

## 3.1.1Incompressible model

For the incompressible Mooney–Rivlin MQLV model, the partial derivatives of the strain energy function (20) are:W1=c1andW2=c2.W_{1}=c_{1}\qquad\text{and}\qquad W_{2}=c_{2}.(25)

Substituting these derivatives into (17), together with (23) and (24), we obtain the corresponding expression for𝚷De\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}. The MQLV constitutive equation (16) then gives the following non-zero components of the Cauchy viscoelastic stress tensor:T11​(t)\displaystyle T_{11}(t)=−p(t)+23(2c1+c2)k(t)2−2μ0k(t)DInt1(t)+23[(c1+2c2)k(t)2\displaystyle=-p(t)+\frac{2}{3}\left(2c_{1}+c_{2}\right)k(t)^{2}-2\mu_{0}k(t)\mathrm{DInt}_{1}(t)+\frac{2}{3}\Big[\left(c_{1}+2c_{2}\right)k(t)^{2}+4c1+5c2]DInt2(t)−23(c1+2c2)(2k(t)DInt3(t)−DInt4(t)),\displaystyle+4c_{1}+5c_{2}\Big]\mathrm{DInt}_{2}(t)-\frac{2}{3}\left(c_{1}+2c_{2}\right)\left(2k(t)\mathrm{DInt}_{3}(t)-\mathrm{DInt}_{4}(t)\right),(26)T12​(t)\displaystyle T_{12}(t)=μ0​(k​(t)−DInt1​(t))+23​(c1+2​c2)​(k​(t)​DInt2​(t)−DInt3​(t)),\displaystyle=\mu_{0}\left(k(t)-\mathrm{DInt}_{1}(t)\right)+\frac{2}{3}\left(c_{1}+2c_{2}\right)\left(k(t)\mathrm{DInt}_{2}(t)-\mathrm{DInt}_{3}(t)\right),(27)T22​(t)\displaystyle T_{22}(t)=−p​(t)−23​(c1+2​c2)​(k​(t)2−DInt2​(t)),\displaystyle=-p(t)-\frac{2}{3}\left(c_{1}+2c_{2}\right)(k(t)^{2}-\mathrm{DInt}_{2}(t)),(28)T33​(t)\displaystyle T_{33}(t)=−p​(t)−23​(c1−c2)​(k​(t)2−DInt2​(t)),\displaystyle=-p(t)-\frac{2}{3}\left(c_{1}-c_{2}\right)(k(t)^{2}-\mathrm{DInt}_{2}(t)),(29)

where we have introduced the compact notation in (A.1) for the integral termsDInti​(t)\mathrm{DInt}_{i}(t).

As is standard for the isochoric simple shear of an incompressible solid, we assume that the out-of-plane surface of the cuboid is traction-free throughout the deformation, so that[5,16]:T33​(t)=0.T_{33}(t)=0.(30)

By imposing this boundary condition in (29), we obtain the Lagrange multiplier of incompressibility:p​(t)=−23​(c1−c2)​(k​(t)2−DInt2​(t)),p(t)=-\frac{2}{3}\left(c_{1}-c_{2}\right)(k(t)^{2}-\mathrm{DInt}_{2}(t)),(31)

which, upon substitution into (26)–(28), yields the fully determined stress components:T11​(t)\displaystyle T_{11}(t)=2​c1​k​(t)2−2​μ0​k​(t)​DInt1​(t)+23​(c1+2​c2)​(3+k​(t)2)​DInt2​(t)\displaystyle=2c_{1}k(t)^{2}-2\mu_{0}k(t)\mathrm{DInt}_{1}(t)+\frac{2}{3}\left(c_{1}+2c_{2}\right)\left(3+k(t)^{2}\right)\mathrm{DInt}_{2}(t)(32)−23​(c1+2​c2)​(2​k​(t)​DInt3​(t)−DInt4​(t)),\displaystyle-\frac{2}{3}\left(c_{1}+2c_{2}\right)\left(2k(t)\mathrm{DInt}_{3}(t)-\mathrm{DInt}_{4}(t)\right),(33)T12​(t)\displaystyle T_{12}(t)=μ0​(k​(t)−DInt1​(t))+23​(c1+2​c2)​(k​(t)​DInt2​(t)−DInt3​(t)),\displaystyle=\mu_{0}\left(k(t)-\mathrm{DInt}_{1}(t)\right)+\frac{2}{3}\left(c_{1}+2c_{2}\right)\left(k(t)\mathrm{DInt}_{2}(t)-\mathrm{DInt}_{3}(t)\right),(34)T22​(t)\displaystyle T_{22}(t)=−2​c2​(k​(t)2−DInt2​(t)).\displaystyle=-2c_{2}(k(t)^{2}-\mathrm{DInt}_{2}(t)).(35)

## 3.1.2Slightly compressible model

For the slightly compressible Mooney–Rivlin MQLV model, the partial derivatives of the strain energy function (15) are:W1=c1,W2=c2andW3=18​κ0​J−1/2​ln⁡J.W_{1}=c_{1},\qquad W_{2}=c_{2}\qquad\text{and}\qquad W_{3}=\frac{1}{8}\kappa_{0}J^{-1/\penalty 502}\ln J.(36)

Since the deformation (21) is isochoric (i.e.J=1J=1), the modified right Cauchy–Green deformation tensor𝑪¯\overline{\bm{C}}and its associated invariantsI¯1\bar{I}_{1}andI¯2\bar{I}_{2}reduce to their unmodified counterparts given by (23) and (24), respectively. The corresponding expressions for𝚷He\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}and𝚷De\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}then follow from (14), and substitution into the MQLV constitutive equation (6) yields the following non-zero components of the Cauchy stress tensor:T11​(t)\displaystyle T_{11}(t)=23​(2​c1+c2)​k​(t)2−2​μ0​k​(t)​DInt1​(t)+23​[(c1+2​c2)​k​(t)2+4​c1+5​c2]​DInt2​(t)\displaystyle=\frac{2}{3}\left(2c_{1}+c_{2}\right)k(t)^{2}-2\mu_{0}k(t)\mathrm{DInt}_{1}(t)+\frac{2}{3}\left[\left(c_{1}+2c_{2}\right)k(t)^{2}+4c_{1}+5c_{2}\right]\mathrm{DInt}_{2}(t)−23​(c1+2​c2)​(2​k​(t)​DInt3​(t)−DInt4​(t)),\displaystyle-\frac{2}{3}\left(c_{1}+2c_{2}\right)\left(2k(t)\mathrm{DInt}_{3}(t)-\mathrm{DInt}_{4}(t)\right),(37)T12​(t)\displaystyle T_{12}(t)=μ0​(k​(t)−DInt1​(t))+23​(c1+2​c2)​(k​(t)​DInt2​(t)−DInt3​(t)),\displaystyle=\mu_{0}(k(t)-\mathrm{DInt}_{1}(t))+\frac{2}{3}\left(c_{1}+2c_{2}\right)\left(k(t)\mathrm{DInt}_{2}(t)-\mathrm{DInt}_{3}(t)\right),(38)T22​(t)\displaystyle T_{22}(t)=−23​(c1+2​c2)​(k​(t)2−DInt2​(t)),\displaystyle=-\frac{2}{3}\left(c_{1}+2c_{2}\right)(k(t)^{2}-\mathrm{DInt}_{2}(t)),(39)T33​(t)\displaystyle T_{33}(t)=−23​(c1−c2)​(k​(t)2−DInt2​(t)),\displaystyle=-\frac{2}{3}\left(c_{1}-c_{2}\right)(k(t)^{2}-\mathrm{DInt}_{2}(t)),(40)

which coincide with the stress components (26)–(29) in the absence of the Lagrange multiplier of incompressibility.

## 3.2Nearly-isochoric simple shear

The isochoric deformation (21) assumes that simple shear is accompanied by no change in volume. This assumption is routinely adopted for soft solids, which are typically modelled as incompressible. In reality, however, all materials are to some extent compressible, so experimental simple shear is invariably accompanied by an infinitesimal change in volume. Following Destradeet al.[20], we model this infinitesimal volume change with the following simple generalisation of the isochoric deformation (21):{x1=(1+δ)​X1+k​(t)​X2,x2=X2,x3=X3,\left\{\begin{aligned} &x_{1}=\left(1+\delta\right)X_{1}+k(t)X_{2},\\
&x_{2}=X_{2},\\
&x_{3}=X_{3},\end{aligned}\right.(41)

which corresponds to simple shear of amountk​(t)k(t)superposed on uniaxial extension of amountδ\deltain the shear direction (see Figure2(b)). The associated deformation gradient takes the form:𝑭​(t)=(1+δk​(t)0010001),\bm{F}(t)=\left(\begin{array}[]{ccc}1+\delta&k(t)&0\\
0&1&0\\
0&0&1\end{array}\right),(42)

withJ=1+δJ=1+\delta; hence,δ\deltacan alternatively be interpreted as the relative volume change between the undeformed and deformed configurations. The corresponding modified right Cauchy–Green deformation tensor𝑪¯=J−2/3​𝑭T​𝑭\overline{\bm{C}}=J^{-2/\penalty 503}\bm{F}^{\mathrm{T}}\bm{F}reads:𝑪¯​(t)=(1+δ)−2/3​((1+δ)2(1+δ)​k​(t)0(1+δ)​k​(t)k​(t)2+10001)\overline{\bm{C}}(t)=\left(1+\delta\right)^{-2/\penalty 503}\left(\begin{array}[]{ccc}\left(1+\delta\right)^{2}&\left(1+\delta\right)k(t)&0\\[1.0pt]
\left(1+\delta\right)k(t)&k(t)^{2}+1&0\\[1.0pt]
0&0&1\end{array}\right)(43)

and has modified principal invariantsI¯1=tr​𝑪¯\bar{I}_{1}=\mathrm{tr}\,\overline{\bm{C}}andI¯2=tr​𝑪¯−1\bar{I}_{2}=\mathrm{tr}\,\overline{\bm{C}}^{-1}given by:I¯1=(1+δ)−2/3​[k​(t)2+2+(1+δ)2]andI¯2=(1+δ)−4/3​[k​(t)2+3+2​δ2+4​δ].\bar{I}_{1}=\left(1+\delta\right)^{-2/\penalty 503}\left[k(t)^{2}+2+\left(1+\delta\right)^{2}\right]\quad\text{and}\quad\bar{I}_{2}=\left(1+\delta\right)^{-4/\penalty 503}\left[k(t)^{2}+3+2\delta^{2}+4\delta\right].(44)

We note that this modelling assumption results in a positive volume change during shearing, as demonstrated in[20]. Moreover, as the volume change associated with the deformation (41) is assumed to be small (i.e.0≤δ≪10\leq\delta\ll 1), we use the slightly compressible MQLV model to derive analytical expressions for the corresponding stresses. In this case, the partial derivatives of the strain energy function (15) are given by (36), which can be combined with (43) and (44) to obtain the corresponding expressions for𝚷He\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}and𝚷De\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}in (14). The MQLV constitutive equation (6) then gives the following non-zero components of the Cauchy stress tensor up to first-order inδ\delta:T11​(t)\displaystyle T_{11}(t)=23​(2​c1+c2)​k​(t)2−2​μ0​k​(t)​DInt1​(t)+23​[(c1+2​c2)​k​(t)2+4​c1+5​c2]​DInt2​(t)\displaystyle=\frac{2}{3}\left(2c_{1}+c_{2}\right)k(t)^{2}-2\mu_{0}k(t)\mathrm{DInt}_{1}(t)+\frac{2}{3}\left[\left(c_{1}+2c_{2}\right)k(t)^{2}+4c_{1}+5c_{2}\right]\mathrm{DInt}_{2}(t)−23(c1+2c2)(2k(t)DInt3(t)−DInt4(t))−19δ[2(10c1+7c2)k(t)2−12μ0−9κ0\displaystyle-\frac{2}{3}\left(c_{1}+2c_{2}\right)\left(2k(t)\mathrm{DInt}_{3}(t)-\mathrm{DInt}_{4}(t)\right)-\frac{1}{9}\delta\Big[2\left(10c_{1}+7c_{2}\right)k(t)^{2}-12\mu_{0}-9\kappa_{0}−6​μ0​(k​(t)2−2)​DInt0​(t)−12​(3​c1+5​c2)​k​(t)​DInt1​(t)\displaystyle-6\mu_{0}(k(t)^{2}-2)\mathrm{DInt}_{0}(t)-12\left(3c_{1}+5c_{2}\right)k(t)\mathrm{DInt}_{1}(t)+2​(14​c1+29​c2+(5​c1+14​c2)​k​(t)2)​DInt2​(t)−(5​c1+14​c2)​(4​k​(t)​DInt3​(t)−DInt4​(t))\displaystyle+2(14c_{1}+29c_{2}+\left(5c_{1}+14c_{2}\right)k(t)^{2})\mathrm{DInt}_{2}(t)-(5c_{1}+14c_{2})(4k(t)\mathrm{DInt}_{3}(t)-\mathrm{DInt}_{4}(t))+9κ0(k(t)2+1)HInt0(t)−9κ0(2k(t)HInt1(t)−HInt2(t))],\displaystyle+9\kappa_{0}(k(t)^{2}+1)\mathrm{HInt}_{0}(t)-9\kappa_{0}(2k(t)\mathrm{HInt}_{1}(t)-\mathrm{HInt}_{2}(t))\Big],(45)T12​(t)\displaystyle T_{12}(t)=μ0​(k​(t)−DInt1​(t))+23​(c1+2​c2)​(k​(t)​DInt2​(t)−DInt3​(t))\displaystyle=\mu_{0}(k(t)-\mathrm{DInt}_{1}(t))+\frac{2}{3}\left(c_{1}+2c_{2}\right)(k(t)\mathrm{DInt}_{2}(t)-\mathrm{DInt}_{3}(t))−19δ[6(5c1+7c2)−6μ0k(t)DInt0(t)−6(3c1+5c2)DInt1(t)\displaystyle-\frac{1}{9}\delta\Big[6\left(5c_{1}+7c_{2}\right)-6\mu_{0}k(t)\mathrm{DInt}_{0}(t)-6\left(3c_{1}+5c_{2}\right)\mathrm{DInt}_{1}(t)+2(5c1+14c2)(k(t)DInt2(t)−DInt3(t))+9κ0(k(t)HInt0(t)−HInt1(t))],\displaystyle+2\left(5c_{1}+14c_{2}\right)(k(t)\mathrm{DInt}_{2}(t)-\mathrm{DInt}_{3}(t))+9\kappa_{0}(k(t)\mathrm{HInt}_{0}(t)-\mathrm{HInt}_{1}(t))\Big],(46)T22​(t)\displaystyle T_{22}(t)=−23(c1+2c2)(k(t)2−DInt2(t))−19δ[6μ0−9κ0−6μ0DInt0(t)\displaystyle=-\frac{2}{3}\left(c_{1}+2c_{2}\right)(k(t)^{2}-\mathrm{DInt}_{2}(t))-\frac{1}{9}\delta\Big[6\mu_{0}-9\kappa_{0}-6\mu_{0}\mathrm{DInt}_{0}(t)−2(5c1+14c2)(k(t)2−DInt2(t))+9κ0HInt0(t)],\displaystyle-2\left(5c_{1}+14c_{2}\right)(k(t)^{2}-\mathrm{DInt}_{2}(t))+9\kappa_{0}\mathrm{HInt}_{0}(t)\Big],(47)T33​(t)\displaystyle T_{33}(t)=−23(c1−c2)(k(t)2−DInt2(t))−19δ[6μ0−9κ0−6μ0DInt0(t)\displaystyle=-\frac{2}{3}\left(c_{1}-c_{2}\right)(k(t)^{2}-\mathrm{DInt}_{2}(t))-\frac{1}{9}\delta\Big[6\mu_{0}-9\kappa_{0}-6\mu_{0}\mathrm{DInt}_{0}(t)−2(5c1−7c2)(k(t)2−DInt2(t))+9κ0HInt0(t)],\displaystyle-2\left(5c_{1}-7c_{2}\right)(k(t)^{2}-\mathrm{DInt}_{2}(t))+9\kappa_{0}\mathrm{HInt}_{0}(t)\Big],(48)

where the termsHInti​(t)\mathrm{HInt}_{i}(t)are defined in (A.2).
The corresponding stress components for the isochoric slightly compressible MQLV model, given by (37)–(40), are recovered as a special case whenδ=0\delta=0.

## 4Torsion of a solid cylinder

In this section, we derive the equations for the torsion of a solid cylinder. We consider both the incompressible and the slightly compressible cases. The deformation can be written as follows:{r=r​(R,t),θ=Θ+ϕ​(t)​Z,z=Z,\left\{\begin{aligned} &r=r(R,t),\\
&\theta=\Theta+\phi(t)Z,\\
&z=Z,\end{aligned}\right.(49)

where the twistϕ=α/H0\phi=\alpha/\penalty 50H_{0}is the angle of rotation per unit height (see Figure3). By introducing the cylindrical bases{𝑬R,𝑬Θ,𝑬Z}\{\bm{E}_{R},\bm{E}_{\Theta},\bm{E}_{Z}\}and{𝒆r,𝒆θ,𝒆z}\{\bm{e}_{r},\bm{e}_{\theta},\bm{e}_{z}\}for the undeformed and deformed configurations, respectively, we can write the deformation gradient𝑭=Fa​A​𝒆a⊗𝑬A\bm{F}=F_{aA}\,\bm{e}_{a}\otimes\bm{E}_{A}associated with the deformation (49) as follows:𝑭=(r′000r/Rr​ϕ001),\bm{F}=\begin{pmatrix}r^{\prime}&0&0\\
0&r/\penalty 50R&r\phi\\
0&0&1\end{pmatrix},(50)

wherer′=d​r/d​Rr^{\prime}=\mathrm{d}r/\penalty 50\mathrm{d}RandJ=r​r′/RJ=rr^{\prime}/\penalty 50R.
For allt≥0t\geq 0, the motion of a solid cylinder in torsion is governed by the following boundary value problem[50,46]:{Tr​r′+(Tr​r−Tθ​θ)​r′​(R)r​(R)=0,Tr​r​(R0)=0,\left\{\begin{aligned} &T_{rr}^{\prime}+(T_{rr}-T_{\theta\theta})\dfrac{r^{\prime}(R)}{r(R)}=0,\\
&T_{rr}(R_{0})=0,\end{aligned}\right.(51)

which follows from the equation of motion (19). Here, the radialTr​rT_{rr}and circumferentialTθ​θT_{\theta\theta}components of the Cauchy stress tensor are given by the corresponding constitutive equation, either in the incompressible form (16) or in the compressible form (6). In addition,r0=r​(R0)r_{0}=r(R_{0})is the outer radius of the cylinder in the deformed state, whereasR0R_{0}is the initial undeformed outer radius (see Figure3). The governing equation is complemented by the zero-traction boundary condition, requiring the radial component of the Cauchy stress tensorTr​rT_{rr}to be zero atR=R0R=R_{0}fort≥0t\geq 0. Finally, the resulting torqueτ\tauand axial forceNzN_{z}required to twist the cylinder are given by[52,42]:τ=2​π​∫0R0Tθ​z​(R)​r​(R)2​r′​(R)​dRandNz=2​π​∫0R0Tz​z​(r)​r​(R)​r′​(R)​dR.\tau=2\pi\int_{0}^{R_{0}}T_{\theta z}(R)\,r(R)^{2}\,r^{\prime}(R)\differential{R}\qquad\text{and}\qquad N_{z}=2\pi\int_{0}^{R_{0}}T_{zz}(r)\,r(R)\,r^{\prime}(R)\differential{R}.(52)

Figure 3:Deformation of a cylinder under (a) isochoric torsion𝝌0\bm{\chi}_{0}and (b) nearly-isochoric torsion𝝌ε\bm{\chi}_{\varepsilon}. In both cases, torque and axial force must be applied to the top face of the cylinder to maintain the deformation.

In the next section, these formulas will be used to compute the resultant torque and axial force predicted by the MQLV model for both incompressible and slightly compressible cylinders in torsion.

## 4.1Torsion of an incompressible cylinder

We begin by considering the incompressible case. For an incompressible material, the deformation (49) is isochoric (see Figure3(a)). Therefore, the deformation gradient satisfiesdet​𝑭=1\mathrm{det}\,\bm{F}=1, which leads tor=Rr=Rfort≥0t\geq 0. We use the Mooney–Rivlin strain energy function for an incompressible material (20).
Combining (20) with (17) and substituting into the constitutive equation (16), we obtain the non-zero components of the Cauchy stress tensor:Tr​r​(t)\displaystyle T_{rr}(t)=−p​(t)−23​(c1−c2)​r2​(ϕ​(t)2−DInt2​(t)),\displaystyle=-p(t)-\frac{2}{3}(c_{1}-c_{2})r^{2}\bigl(\phi(t)^{2}-\mathrm{DInt}_{2}(t)\bigr),(53)Tθ​θ​(t)\displaystyle T_{\theta\theta}(t)=−p​(t)+23​[(2​c1+c2)​ϕ​(t)2−3​μ0​DInt1​(t)​ϕ​(t)+(4​c1+5​c2)​DInt2​(t)]​r2\displaystyle=-p(t)+\frac{2}{3}\Bigl[(2c_{1}+c_{2})\phi(t)^{2}-3\mu_{0}\mathrm{DInt}_{1}(t)\phi(t)+(4c_{1}+5c_{2})\mathrm{DInt}_{2}(t)\Bigr]r^{2}+23​(c1+2​c2)​(DInt2​ϕ​(t)2−2​D​I​n​t3​(t)​ϕ​(t)+DInt4​(t))​r4,\displaystyle+\frac{2}{3}(c_{1}+2c_{2})\Bigl(\mathrm{DInt}_{2}\phi(t)^{2}-2\mathrm{DInt}_{3}(t)\phi(t)+\mathrm{DInt}_{4}(t)\Bigr)r^{4},(54)Tθ​z​(t)\displaystyle T_{\theta z}(t)=μ0​r​(ϕ​(t)−DInt1​(t))+23​(c1+2​c2)​r3​(DInt3​(t)−DInt2​(t)​ϕ​(t)),\displaystyle=\mu_{0}r\bigl(\phi(t)-\mathrm{DInt}_{1}(t)\bigr)+\frac{2}{3}(c_{1}+2c_{2})r^{3}\bigl(\mathrm{DInt}_{3}(t)-\mathrm{DInt}_{2}(t)\phi(t)\bigr),(55)Tz​z​(t)\displaystyle T_{zz}(t)=−p​(t)−23​(c1+2​c2)​r2​(ϕ​(t)2−DInt2​(t)),\displaystyle=-p(t)-\frac{2}{3}(c_{1}+2c_{2})r^{2}\bigl(\phi(t)^{2}-\mathrm{DInt}_{2}(t)\bigr),(56)

where, the integralsDInti​(t)\mathrm{DInt}_{i}(t)are defined in (A.1).
By using (53) and (54), we can now solve the governing problem in (51) forp​(t)p(t)to obtain:p​(t)\displaystyle p(t)=−16​[2​(5​c1−2​c2)​r2−6​c1​R02]​ϕ​(t)2+μ0​(r2−R02)​ϕ​(t)​DInt1​(t)\displaystyle=-\frac{1}{6}\Bigl[2(5c_{1}-2c_{2})r^{2}-6c_{1}R_{0}^{2}\Bigr]\phi(t)^{2}+\mu_{0}(r^{2}-R_{0}^{2})\phi(t)\mathrm{DInt}_{1}(t)−[13​(c1+8​c2)​r2−(c1+2​c2)​R02]​DInt2​(t)\displaystyle-\Bigl[\frac{1}{3}(c_{1}+8c_{2})r^{2}-(c_{1}+2c_{2})R_{0}^{2}\Bigr]\mathrm{DInt}_{2}(t)(57)−16​(c1+2​c2)​(r4−R04)​(DInt2​(t)​ϕ​(t)2−2​D​I​n​t3​(t)​ϕ​(t)+DInt4​(t)).\displaystyle-\frac{1}{6}(c_{1}+2c_{2})(r^{4}-R_{0}^{4})\Bigl(\mathrm{DInt}_{2}(t)\phi(t)^{2}-2\mathrm{DInt}_{3}(t)\phi(t)+\mathrm{DInt}_{4}(t)\Bigr).(58)

Now that all the stress components in (53)–(56) are fully determined, we can use (55) and (56) to compute the torque and axial force in (52) as follows:τ​(t)\displaystyle\tau(t)=π2​μ0​(ϕ​(t)−DInt1​(t))​R04+2​π9​(c1+2​c2)​(DInt2​(t)​ϕ​(t)−DInt3​(t))​R06,\displaystyle=\frac{\pi}{2}\mu_{0}\bigl(\phi(t)-\mathrm{DInt}_{1}(t)\bigr)R_{0}^{4}+\frac{2\pi}{9}(c_{1}+2c_{2})\bigl(\mathrm{DInt}_{2}(t)\phi(t)-\mathrm{DInt}_{3}(t)\bigr)R_{0}^{6},(59)Nz​(t)\displaystyle N_{z}(t)=−π2​[(c1+2​c2)​ϕ​(t)2−μ0​DInt1​(t)​ϕ​(t)+c1​DInt2​(t)]​R04\displaystyle=-\frac{\pi}{2}\Bigl[(c_{1}+2c_{2})\phi(t)^{2}-\mu_{0}\mathrm{DInt}_{1}(t)\phi(t)+c_{1}\mathrm{DInt}_{2}(t)\Bigr]R_{0}^{4}−π9​(c1+2​c2)​(DInt2​(t)​ϕ​(t)2−2​D​I​n​t3​(t)​ϕ​(t)+DInt4​(t))​R06.\displaystyle-\frac{\pi}{9}(c_{1}+2c_{2})\Bigl(\mathrm{DInt}_{2}(t)\phi(t)^{2}-2\mathrm{DInt}_{3}(t)\phi(t)+\mathrm{DInt}_{4}(t)\Bigr)R_{0}^{6}.(60)

In the next section, we consider the deformation of a slightly compressible solid cylinder in torsion.

## 4.2Torsion of a slightly compressible cylinder

Here, we adapt the perturbation method proposed by Levinson[36]and used by Smallet al.[52]to model the torsion of a hyperelastic cylinder. As shown in Figure3(b), we start by perturbing the isochoric deformation (49), for whichr=Rr=R, by allowing for a small volume change in the radial direction and adopting the following ansatz for the radial deformation:r=R+ε​r1​(R)+ε2​r2​(R)+O​(ε3),r=R+\varepsilon r_{1}(R)+\varepsilon^{2}r_{2}(R)+O(\varepsilon^{3}),(61)

whereε=μ0/κ0≪1\varepsilon=\mu_{0}/\penalty 50\kappa_{0}\ll 1is a small parameter that describes the degree of slight compressibility, withε=0\varepsilon=0corresponding to incompressible behaviour. Hence, the volume ratioJ=r​r′/RJ=rr^{\prime}/\penalty 50Rexpanded up to second-order inε\varepsilonreads:J=1+ε​J1​(R)+ε2​J2​(R)+O​(ε3),J=1+\varepsilon J_{1}(R)+\varepsilon^{2}J_{2}(R)+O(\varepsilon^{3}),(62)

where:{J1=r1′​(R)+r1​(R)R,J2=r2′​(R)+r2​(R)+r1​(R)​r1′​(R)R.\left\{\begin{aligned} &J_{1}=r_{1}^{\prime}(R)+\dfrac{r_{1}(R)}{R},\\
&J_{2}=r_{2}^{\prime}(R)+\frac{r_{2}(R)+r_{1}(R)r_{1}^{\prime}(R)}{R}.\end{aligned}\right.(63)

We use the slightly compressible Mooney–Rivlin strain energy function (15) and compute the tensors𝚷He\bm{\Pi}^{\mathrm{e}}_{\mathrm{H}}and𝚷De\bm{\Pi}^{\mathrm{e}}_{\mathrm{D}}in (14). We then insert these expressions into the compressible MQLV constitutive equation (6), expand the components of the Cauchy stress tensor𝑻​(t)\bm{T}(t)up to first-order inε\varepsilon. The resulting components of the Cauchy stress tensor display the following form:Ti​j​(t)=Ti​j0​(r1​(R),J1​(R),R,t)+ε​Ti​j1​(r1​(R),J1​(R),J2​(R),R,t)fori,j∈{r,θ,z}.T_{ij}(t)=T_{ij}^{0}(r_{1}(R),J_{1}(R),R,t)+\varepsilon\mkern 1.0muT_{ij}^{1}(r_{1}(R),J_{1}(R),J_{2}(R),R,t)\quad\text{for}\quad i,j\in\{r,\theta,z\}.(64)

Upon substituting them into the governing equation (51), we obtain the governing problem at order zero as follows:{r1′′​(R)+(1R−A2A0​R)​r1′​(R)−(A2A0+1R2)​r1​(R)=A1​R+A3​R3A0,r1′​(R0)+r1​(R0)R0=C0​R02,\left\{\begin{aligned} &r_{1}^{\prime\prime}(R)+\left(\dfrac{1}{R}-\dfrac{A_{2}}{A_{0}}R\right)r_{1}^{\prime}(R)-\left(\dfrac{A_{2}}{A_{0}}+\frac{1}{R^{2}}\right)r_{1}(R)=\dfrac{A_{1}R+A_{3}R^{3}}{A_{0}},\\
&r_{1}^{\prime}(R_{0})+\frac{r_{1}(R_{0})}{R_{0}}=C_{0}R_{0}^{2},\end{aligned}\right.(65)

where we have introduced the coefficientsAi​(t)A_{i}(t), which are functions ofttonly and are listed in (B.3)–(B.6), together with the constant termC0C_{0}in (B.10).
An explicit analytical solution of (65) can be found by using the Frobenius method[35]. Seeking solutions of the form:r1​(R)=Rs​∑n=0∞an​Rn,r_{1}(R)=R^{s}\sum_{n=0}^{\infty}a_{n}R^{n},(66)

we find that the indicial equation has rootss1=1s_{1}=1ands2=−1s_{2}=-1. Fors1=1s_{1}=1, the recurrence relation is:an=A2A0​an−2n+2forn≥2,a_{n}=\dfrac{A_{2}}{A_{0}}\dfrac{a_{n-2}}{n+2}\qquad\text{for}\qquad n\geq 2,(67)

which gives the first Frobenius solution:rs1​(R)=R​∑k=0∞(A22​A0)k​R2​k(k+1)!=2​A0A2​(eA2​R2/2​A0−1)R.r_{s_{1}}(R)=R\,\sum_{k=0}^{\infty}\left(\dfrac{A_{2}}{2A_{0}}\right)^{k}\dfrac{R^{2k}}{(k+1)!}=\dfrac{2A_{0}}{A_{2}}\dfrac{(\mathrm{e}^{A_{2}R^{2}/\penalty 502A_{0}}-1)}{R}.(68)

Since the two roots are separated by an integer, the second Frobenius solution can be obtained by using the reduction of order formula[35]:rs2​(R)=rs1​(R)​∫R1rs12​(u)​e−∫u[(A0−A2​x2)/A0​x]​dx​du=−12​R.r_{s_{2}}(R)=r_{s_{1}}(R)\int^{R}\dfrac{1}{r_{s_{1}}^{2}(u)}\mathrm{e}^{-\displaystyle\int^{u}\left[(A_{0}-A_{2}x^{2})/\penalty 50A_{0}x\right]\differential{x}}\differential{u}=-\dfrac{1}{2R}.(69)

The homogeneous solution of(65)1\eqref{eq:gov0}_{1}is thus:r1h​(R)=d1​rs1​(R)+d2​rs2​(R)=d1​2​A0A2​(eA2​R2/2​A0−1)R−d2​12​R,r_{1}^{\mathrm{h}}(R)=d_{1}r_{s_{1}}(R)+d_{2}r_{s_{2}}(R)=d_{1}\dfrac{2A_{0}}{A_{2}}\dfrac{(\mathrm{e}^{A_{2}R^{2}/\penalty 502A_{0}}-1)}{R}-d_{2}\dfrac{1}{2R},(70)

and the particular solution can be easily found since the inhomogeneous term of(65)1\eqref{eq:gov0}_{1}is a polynomial of degree three inRRas follows:r1p​(R)=−(4​A0​A1+2​A2​A3)4​A22​R−A14​A2​R3.r_{1}^{\mathrm{p}}(R)=-\dfrac{(4A_{0}A_{1}+2A_{2}A_{3})}{4A_{2}^{2}}R-\frac{A_{1}}{4A_{2}}R^{3}.(71)

The general solution is thus:r1​(R)=r1h​(R)+r1p​(R)=d1​2​A0A2​(eA2​R2/2​A0−1)R−d2​12​R−(4​A0​A1+2​A2​A3)4​A22​R−A14​A2​R3.r_{1}(R)=r_{1}^{\mathrm{h}}(R)+r_{1}^{\mathrm{p}}(R)=d_{1}\dfrac{2A_{0}}{A_{2}}\dfrac{(\mathrm{e}^{A_{2}R^{2}/\penalty 502A_{0}}-1)}{R}-d_{2}\dfrac{1}{2R}-\dfrac{(4A_{0}A_{1}+2A_{2}A_{3})}{4A_{2}^{2}}R-\frac{A_{1}}{4A_{2}}R^{3}.(72)

Now, imposing the regularity conditionr1​(0)=0r_{1}(0)=0enforcesd2=0d_{2}=0, while the boundary condition in(65)2\eqref{eq:gov0}_{2}gives:d1=e−A2​R2/2​A0​[2​A0​A3+A2​A1+(C0​A2+A3)​A2​R02]2​A22.d_{1}=\frac{\mathrm{e}^{-A_{2}R^{2}/\penalty 502A_{0}}\left[2A_{0}A_{3}+A_{2}A_{1}+(C_{0}A_{2}+A_{3})A_{2}R_{0}^{2}\right]}{2A_{2}^{2}}.(73)

At order one, for compactness, the governing problem can be written in terms ofJ2J_{2}as follows:{J2′​(R)−A2A0​R​J2​(R)=P​(R),J2​(R0)=C1,\left\{\begin{aligned} &J_{2}^{\prime}(R)-\dfrac{A_{2}}{A_{0}}RJ_{2}(R)=P(R),\\
&J_{2}(R_{0})=C_{1},\end{aligned}\right.(74)

where the constantC1C_{1}is given in (B.11) and the inhomogeneous term is given by:P​(R)=p0​(R)+p1​(R)​r1​(R)+p2​(R)​r1′​(R)A0−5​A22​A0​R​J1​(R)2.P(R)=\dfrac{p_{0}(R)+p_{1}(R)r_{1}(R)+p_{2}(R)r_{1}^{\prime}(R)}{A_{0}}-\frac{5A_{2}}{2A_{0}}RJ_{1}(R)^{2}.(75)

The coefficientspi​(R)p_{i}(R)are polynomial functions ofRRand are listed in (B.7)–(B.9). An analytical solution of (74) can be found by using the integrating factor method. Multiplying(74)1\eqref{eq:gov1}_{1}by the integrating factore−∫R(A2​u/A0)​du=e−A2​R2/2​A0\mathrm{e}^{-\int^{R}\left(A_{2}u/\penalty 50A_{0}\right)\differential{u}}=\mathrm{e}^{-A_{2}R^{2}/\penalty 502A_{0}}, we obtain:dd​R​(J2​(R)​e−A2​R2/2​A0)=e−A2​R2/2​A0​P​(R).\frac{\mathrm{d}}{\mathrm{d}R}\left(J_{2}(R)\mathrm{e}^{-A_{2}R^{2}/\penalty 502A_{0}}\right)=\mathrm{e}^{-A_{2}R^{2}/\penalty 502A_{0}}P(R).(76)

Integrating this equation and imposing the boundary condition(74)2\eqref{eq:gov1}_{2}yields the following solution:J2​(R)=−eA2​R2/2​A0​∫RR0e−A2​u2/2​A0​P​(u)​du+C1​eA2​(R2−R02)/2​A0.J_{2}(R)=-\mathrm{e}^{A_{2}R^{2}/\penalty 502A_{0}}\int_{R}^{R_{0}}\mathrm{e}^{-A_{2}u^{2}/\penalty 502A_{0}}P(u)\differential{u}+C_{1}\mathrm{e}^{A_{2}\left(R^{2}-R^{2}_{0}\right)/\penalty 502A_{0}}.(77)

Although the integral in (77) can be evaluated explicitly, the resulting expression is unwieldy and is therefore omitted for brevity. Finally, the expressions forr1​(R)r_{1}(R)andJ2​(R)J_{2}(R)in (72), (73) and (77) can be substituted into (64) to get the stress componentsTθ​zT_{\theta z}andTz​zT_{zz}. The resultant torque and axial force in (52) can be obtained, upon integration. Practically, we expand the solutionr1​(R)r_{1}(R)in (72)–(73) aboutR=0R=0up to order seven and similarly forJ1​(R)J_{1}(R)up to order six. We then use these expansions to calculateP​(R)P(R)in (75) and substitute into (77) to calculate the solutionJ2​(R)J_{2}(R). Once bothr1​(R)r_{1}(R)andJ2​(R)J_{2}(R)are converted into integrable functions, we can then calculate the stress componentsTθ​zT_{\theta z}andTz​zT_{zz}and finally evaluate the torque and axial force using (52).

## 5Results and discussion

The analytical expressions derived in Sections3and4for the shear and normal stresses in simple shear and for the torque and axial force in torsion are valid for arbitrary shear and twist historiesk​(t)k(t)andϕ​(t)\phi(t), respectively. We now consider a typical experimental ramp-and-hold loading scenario, for which the shear and twist histories are given by:k​(t)=k0t⋆​t−k0t⋆​(t−t⋆)​H​(t−t⋆)andϕ​(t)=ϕ0t⋆​t−ϕ0t⋆​(t−t⋆)​H​(t−t⋆),k(t)=\frac{k_{0}}{t^{\star}}t-\frac{k_{0}}{t^{\star}}(t-t^{\star})H(t-t^{\star})\qquad\text{and}\qquad\phi(t)=\frac{\phi_{0}}{t^{\star}}t-\frac{\phi_{0}}{t^{\star}}(t-t^{\star})H(t-t^{\star}),(78)

wherek0k_{0}andϕ0\phi_{0}are, respectively, the maximum values of the shear and twist,t⋆t^{\star}is the rising time of the ramp andHHis the Heaviside step function. Since ramp-phase data is often neglected in model fitting[39,50], we restrict our attention in this section to the hold phase (i.e.t≥t⋆t\geq t^{\star}) and plot the corresponding relaxation curves in simple shear and torsion to compare the predictions of the MQLV models developed previously in Sections3and4.

## 5.1Effect of compressibility

We begin by examining the effect of compressibility in the two deformation modes. Figures4(a)and4(b)show the relaxation of the shear and normal stresses for three simple shear scenarios: the incompressible and slightly compressible models under the isochoric deformation (21), and the slightly compressible model under the nearly isochoric deformation (41). The corresponding torsional responses are displayed in Figures4(c)and4(d)for different values ofε=μ0/κ0\varepsilon=\mu_{0}/\kappa_{0}.
In simple shear, the shear stress responses are identical in all three cases (Figure4(a)), as can be verified by comparing (34) and (38). This follows from the isochoric nature of deformation (21): sinceJ=1J=1, the volumetric contribution vanishes and the pull-back of the volumetric stress𝚷He\bm{\Pi}^{\text{e}}_{\text{H}}in (14) is zero.
In contrast, the normal stress exhibits a markedly different behaviour (Figure4(b)). For the isochoric case, the incompressible and slightly compressible predictions (35) and (39) differ only by a constant factor, so their normalised responses coincide (overlapping dashed and light-red curves). However, for the nearly isochoric deformation (41), even a very small volumetric change (δ=10−4\delta=10^{-4}) leads to a substantial deviation in the normal stress relaxation (red curve), demonstrating the strong sensitivity of normal stresses to volumetric effects.

In torsion, the influence of compressibility is governed byε\varepsilon. Forε=0.001\varepsilon=0.001, the slightly compressible response coincides with the incompressible one: both the torque (dashed and light-blue curves in Figure4(c)) and the axial force (dashed and magenta curves in Figure4(d)) match the incompressible predictions given by (59) and (60). Asε\varepsilonincreases to0.040.04, the torque remains unaffected by compressibility. By contrast, the axial force becomes highly sensitive: its relaxation curve departs significantly from the incompressible prediction, highlighting the key role of volumetric effects in the axial response.(a)(b)(c)(d)Figure 4:Effect of compressibility: normalised shear stressT¯12=T12​(t)/T12​(t⋆)\overline{T}_{12}=T_{12}(t)/T_{12}(t^{\star})(a) and normal stressT¯22=T22​(t)/T22​(t⋆)\overline{T}_{22}=T_{22}(t)/T_{22}(t^{\star})(b) in simple shear for the isochoric deformation (21) (incompressible and slightly compressible constitutive models) and for the nearly isochoric deformation (41)
(slightly compressible model); normalised torqueτ¯​(t)/τ¯​(t⋆)\overline{\tau}(t)/\overline{\tau}(t^{\star})(c) and axial forceN¯z​(t)/N¯z​(t⋆)\overline{N}_{z}(t)/\overline{N}_{z}(t^{\star})(c) in torsion. The following parameters are fixed:k0=0.4k_{0}=0.4,ϕ0=25​rad​m−1\phi_{0}=25\,\mathrm{rad}\,\mathrm{m}^{-1},R0=12.5​mmR_{0}=12.5\,\mathrm{mm},c1=3000​Pac_{1}=3000\,\mathrm{Pa},c2=2000​Pac_{2}=2000\,\mathrm{Pa},μ0=104​Pa\mu_{0}=10^{4}\,\mathrm{Pa},τD=5​s\tau_{\mathrm{D}}=5\,\mathrm{s},τH=2​s\tau_{\mathrm{H}}=2\,\mathrm{s},κ∞/κ0=0.4\kappa_{\infty}/\penalty 50\kappa_{0}=0.4andμ∞/μ0=0.9\mu_{\infty}/\penalty 50\mu_{0}=0.9. All curves in (a) and (b) are plotted forκ0=25​μ0\kappa_{0}=25\,\mu_{0}. For the nearly-isochoric deformation in (a) and (b), we setδ=10−4\delta=10^{-4}. In (c) and (d), we varyε=μ0/κ0∈{0.04,0.001}\varepsilon=\mu_{0}/\penalty 50\kappa_{0}\in\{0.04,0.001\}and the incompressible curves are plotted from (59) and (60).

## 5.2Strain-dependence

Next, we investigate whether compressibility amplifies the non-linear effects due to the large deformation, both in simple shear and in torsion. In light of its pronounced sensitivity to volume changes, we restrict attention to the slightly compressible model in simple shear. In Figure5, we compare the normalised shear and normal stresses for the slightly compressible model under (a) the isochoric simple shear deformation and (b) the nearly-isochoric deformation at different levels of sheark0k_{0}.(a)(b)(c)(d)Figure 5:Strain-dependence: normalised shear stressT¯12\overline{T}_{12}and normal stressT¯22\overline{T}_{22}predicted by the slightly compressible model (a) for the isochoric deformation (21) and (b) for the nearly isochoric deformation (41); normalised torqueτ¯\overline{\tau}and axial forceN¯z\overline{N}_{z}predicted by the incompressible model (c) and by the slightly compressible model (d) in torsion. The following parameters are fixed:R0=12.5​mmR_{0}=12.5\,\mathrm{mm},c1=3000​Pac_{1}=3000\,\mathrm{Pa},c2=2000​Pac_{2}=2000\,\mathrm{Pa},μ0=104​Pa\mu_{0}=10^{4}\,\mathrm{Pa},κ0=25​μ0\kappa_{0}=25\,\mu_{0},τD=5​s\tau_{\mathrm{D}}=5\,\mathrm{s},τH=2​s\tau_{\mathrm{H}}=2\,\mathrm{s},κ∞/κ0=0.4\kappa_{\infty}/\penalty 50\kappa_{0}=0.4,μ∞/μ0=0.9\mu_{\infty}/\penalty 50\mu_{0}=0.9andδ=10−4\delta=10^{-4}. In (a) and (b), we varyk0∈{0.4,0.8}k_{0}\in\{0.4,0.8\}, while in (c) and (d) we varyϕ0∈{25,100}​rad​m−1\phi_{0}\in\{25,100\}\,\mathrm{rad}\,\mathrm{m}^{-1}.

The curves show that, under the isochoric deformation, neither the shear stress nor the normal stress is affected by the magnitude of the applied shear. In contrast, for the non-isochoric deformation, the normal stress becomes sensitive to the level of shear. This behaviour arises because the bulk relaxation function is only activated when a volume change occurs. As a result, in the non-isochoric case, the bulk and shear contributions couple differently with the deformation, introducing an additional dependence of the normal stress on the applied shear.

In torsion, we compare the torque and axial force predicted by the incompressible (Figure5(c)) and slightly compressible (Figure5(d)) models for different levels of twist. We choose two levels of twist:ϕ0=25​rad​m−1\phi_{0}=25\,\mathrm{rad}\,\mathrm{m}^{-1}, which corresponds to a moderate twist, andϕ0=100​rad​m−1\phi_{0}=100\,\mathrm{rad}\,\mathrm{m}^{-1}, which corresponds to a large twist. In the incompressible case, the normalised torque and axial force curves coincide, as both depend on a single relaxation functionμ​(t)\mu(t). By contrast, in the slightly compressible model, both the torque and axial force relaxation profiles change with the level of twist, thus exhibiting strain-dependent relaxation.

The strain-dependence observed in torsion and in the normal stress response in simple shear primarily stems from the different way in which the shear and bulk relaxation functions couple with the deformation.
In simple shear, the hereditary integrals associated withμ​(t)\mu(t)andκ​(t)\kappa(t)in the shear stress combine in a factorisable manner with respect tok​(t)k(t), leading to uniform scaling that is removed upon normalisation. In contrast, the normal stress involves a non-factorisable combination of terms with different powers ofk​(t)k(t), including contributions independent ofk​(t)k(t), so that its normalised response retains a dependence on the deformation (compare (46) and (47)). Similarly, in torsion the coupling between the twistϕ​(t)\phi(t)and the relaxation functionsμ​(t)\mu(t)andκ​(t)\kappa(t)is non-factorisable, so that the relative contributions of shear and bulk relaxation depend on the level of twist, leading to strain-dependent behaviour in both torque and axial force.

## 5.3Competition between shear and bulk relaxation(a)(b)(c)(d)Figure 6:Effect of the relaxation timesτD\tau_{\mathrm{D}}andτH\tau_{\mathrm{H}}: normalised shear stressT¯12\overline{T}_{12}(a) and normal stressT¯22\overline{T}_{22}(b) predicted by the slightly compressible model for the nearly-isochoric deformation (41); normalised torqueτ¯\overline{\tau}(c) and axial forceN¯z\overline{N}_{z}(d) predicted by the slightly compressible model. The following parameters are fixed:R0=12.5​mmR_{0}=12.5\,\mathrm{mm},c1=3000​Pac_{1}=3000\,\mathrm{Pa},c2=2000​Pac_{2}=2000\,\mathrm{Pa},μ0=104​Pa\mu_{0}=10^{4}\,\mathrm{Pa},κ0=25​μ0\kappa_{0}=25\,\mu_{0},κ∞/κ0=0.4\kappa_{\infty}/\penalty 50\kappa_{0}=0.4,μ∞/μ0=0.9\mu_{\infty}/\penalty 50\mu_{0}=0.9,δ=10−4\delta=10^{-4}andk0=0.4k_{0}=0.4. We vary the following pair of parameters:τH=2​s\tau_{\mathrm{H}}=2\,\mathrm{s},τD=5​s\tau_{\mathrm{D}}=5\,\mathrm{s}(blue and red curves),τH=τD=5​s\tau_{\mathrm{H}}=\tau_{\mathrm{D}}=5\,\mathrm{s}(dashed curves),τH=5​s\tau_{\mathrm{H}}=5\,\mathrm{s},τD=2​s\tau_{\mathrm{D}}=2\,\mathrm{s}(cyan and magenta curves).

Next, in Figures6and7, we quantify the interplay between the shear and bulk relaxation functionsμ​(t)\mu(t)andκ​(t)\kappa(t)by varying the relaxation timesτD\tau_{\mathrm{D}},τH\tau_{\mathrm{H}}and the normalised long-term moduliμ∞/μ0\mu_{\infty}/\mu_{0},κ∞/κ0\kappa_{\infty}/\kappa_{0}.
In Figure6, we considerτD>τH\tau_{\mathrm{D}}>\tau_{\mathrm{H}},τD=τH\tau_{\mathrm{D}}=\tau_{\mathrm{H}}, andτD<τH\tau_{\mathrm{D}}<\tau_{\mathrm{H}}.

The relaxation times primarily affect the short-time behaviour. In simple shear, the shear stress is insensitive to changes inτH\tau_{\mathrm{H}}, as confirmed by the overlap of curves with identicalτD\tau_{\mathrm{D}}in Figure6(a). The same behaviour is observed for the torque in Figure6(c). In contrast, both normal stress and axial force (Figures6(b)and6(d)) noticeably vary withτH\tau_{\mathrm{H}}, highlighting a competition between shear and bulk relaxation mechanisms.(a)(b)(c)(d)Figure 7:Effect of normalised long-time moduliμ∞/μ0\mu_{\infty}/\penalty 50\mu_{0}andκ∞/κ0\kappa_{\infty}/\penalty 50\kappa_{0}: (a) and (b) normalised shear and normal stresses predicted by the slightly compressible model for the nearly-isochoric deformation (41) in simple shear; (c) and (d) normalised torque and axial force in torsion predicted by the slightly-compressible model. The following parameters are fixed:R0=12.5​mmR_{0}=12.5\,\mathrm{mm},c1=3000​Pac_{1}=3000\,\mathrm{Pa},c2=2000​Pac_{2}=2000\,\mathrm{Pa},μ0=104​Pa\mu_{0}=10^{4}\,\mathrm{Pa},κ0=25​μ0\kappa_{0}=25\,\mu_{0},τD=5\tau_{\mathrm{D}}=5s,τH=2\tau_{\mathrm{H}}=2s,δ=10−4\delta=10^{-4}andk0=0.4k_{0}=0.4. In (a) and (c) we set:μ∞/μ0=0.9\mu_{\infty}/\penalty 50\mu_{0}=0.9,κ∞/κ0=0.4\kappa_{\infty}/\penalty 50\kappa_{0}=0.4, while in (b) and (d) we set:μ∞/μ0=0.4\mu_{\infty}/\penalty 50\mu_{0}=0.4,κ∞/κ0=0.9\kappa_{\infty}/\penalty 50\kappa_{0}=0.9.

Figures7(a)and7(b)again confirm that the dominant contribution to the shear stress arises from the shear relaxation function, since varying the ratioμ∞/μ0\mu_{\infty}/\mu_{0}directly affects the asymptotic value of the relaxation curve. The plots also show that when the bulk relaxation effects are comparatively stronger, the relaxation behaviour of the normal stress deviates from that of the shear stress (compare Figure7(a)with7(b)). A similar behaviour is observed in torsion (Figures7(c)and7(d)).

Moreover, when the normalised long-time modulus of the shear relaxation function is greater than the bulk one, the axial force relaxes more than the torque (see Figure7(c)). However, whenμ∞/μ0<κ∞/κ0\mu_{\infty}/\mu_{0}<\kappa_{\infty}/\kappa_{0}(i.e. the relaxation associated with the shear relaxation function is greater) the torque relaxes more than the force (see Figure7(d)). This latter behaviour is consistent with the experimental data shown in Figure1(a)for torsion tests on brain tissue samples. While the slightly compressible theory that we proposed in this paper is able to capture the relaxation behaviour of brain tissue samples, the torque and axial force curves are visibly different for the agarose gel samples (see Figure1(b)). This discrepancy is possibly due to differences in the underlying material structure. Although brain tissue consists of approximately80%80\%water by volume, only2020–40%40\%of this is free flowing, with the remainder trapped inside the cells that comprise the solid matrix[10]. By contrast, agarose gels can contain upwards of90%90\%free-flowing water by volume and form a more open porous network[54]. As a result, agarose gels can undergo larger volume changes during deformation than brain tissue, which are not fully captured by the slightly compressible model proposed in this paper. For agarose gels, a fully compressible model may therefore be more appropriate. However, developing such a model for torsion is not straightforward, as torsion is not a universal deformation. From a mathematical perspective, in contrast to the incompressible case, where a deformation withr=Rr=Ris admissible for a wide class of materials, compressible elasticity generally requires additional radial deformation in order to satisfy the equation of motion. As a result, such a deformation is not compatible with all strain energy functions[34,42]and pure torsion is only recovered for special material choices. In the slightly compressible setting, this difficulty can be addressed perturbatively by introducing a small parameterε=μ0/κ0\varepsilon=\mu_{0}/\penalty 50\kappa_{0}and expanding the deformation and governing equations accordingly, leading to a tractable approximate solution obtained via a linearisation of the governing equations at successive orders[52,36]. However, in a fully compressible model, no such simplification is available and the coupled non-linear boundary value problem must be solved in full, with the resulting deformation depending explicitly on both the constitutive law and the geometry.

Finally, by comparing Figures7(a)and7(c), an opposite trend emerges: in simple shear the normal stress relaxes less than the shear stress, whereas in torsion the axial force relaxes more than the torque. This opposite behaviour can be understood by examining the interplay between volumetric effects and the Poynting effect[32,21,56,43]. In simple shear, a slightly compressible material undergoes a small volume increase (i.e.δ>0\delta>0) associated with an elongation in the shear direction and contraction in the normal direction. This induces a positive normal stress contribution arising from compressibility, which opposes the negative normal stress generated by the Poynting effect. As a result, these two mechanisms compete, reducing the overall magnitude of relaxation and leading to a higher long-time value of the normal stress compared to the shear stress. In torsion, by contrast, the deformation induces a slight volume decrease. The resulting volumetric contribution generates a negative axial force, which adds to the negative contribution associated with the Poynting effect. In this case, the two mechanisms act cooperatively, enhancing the overall relaxation and leading to a lower long-time value of the axial force compared to the torque.

## 6Conclusions

In this work, we have investigated the role of compressibility within the MQLV framework.
Our results showed that compressibility is only activated through the bulk relaxation functionκ​(t)\kappa(t)in the presence of a volume change. The bulk contribution vanishes under isochoric deformations, so that slightly compressible and incompressible models yield identical responses. Even a very small deviation from volume preservation, however, is sufficient to trigger bulk relaxation and significantly alter the stress response.

Second, the sensitivity to compressibility depends strongly on the stress measure. The shear stress in simple shear and the torque in torsion are only marginally affected by compressibility, as they are dominated by the shear relaxation functionμ​(t)\mu(t). In contrast, the normal stress in simple shear and the axial force in torsion exhibit a pronounced dependence on compressibility, reflecting the contribution of the bulk relaxation mechanism even under nearly-isochoric deformations.

Third, the slightly compressible MQLV model reveals a clear interplay between volumetric effects and the Poynting effect. In simple shear, the deformation induces a small volume increase, generating a positive volumetric contribution that opposes the negative Poynting effect; these competing mechanisms reduce the overall relaxation and increase the long-term value of the normal stress. In torsion, by contrast, the deformation leads to a volume decrease, and the resulting volumetric contribution reinforces the Poynting effect. This additive behaviour enhances the relaxation of the axial force, leading to a lower long-term value compared to the torque.

Finally, these findings have direct implications for the interpretation of experimental data. In particular, normal stress measurements such as the axial force in torsion or the normal stress in shear are significantly more sensitive to compressibility than the shear stress or torque. As a result, neglecting compressibility may lead to misinterpretation of relaxation curves and inaccurate identification of material parameters, especially when small but non-negligible volume changes are present. This highlights the importance of incorporating compressibility effects when fitting constitutive models to experimental observations involving normal stress responses.

Future work will focus on implementing the MQLV framework within finite element formulations, enabling the analysis of more general geometries, material heterogeneity and fully compressible behaviours beyond the semi-analytical approach considered here.

## Data access

The brain and agarose gel torsion data referenced in Figure1are available in the Mendeley Data repositories:https://doi.org/10.17632/m2jwdfgczs.1andhttps://doi.org/10.17632/ny3k9s7494.1, respectively.

## AI declaration

In preparing this article, the authors utilised the ChatGPT large language model as a copy editing tool to improve grammar, refine language and enhance the clarity of the original text.

## Authors contribution

Valentina Balbi: conceptualisation, methodology, formal analysis, writing original draft, writing reviewing and editing. Griffen Small: conceptualisation, methodology, formal analysis, writing original draft, writing reviewing and editing. Both authors gave final approval for publication.

## Competing Interests

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this article.

## Funding

This article has emanated from research jointly funded by the College of Science and Engineering at the University of Galway under the Millennium Fund scheme for the project “Modelling Brain Mechanics” (Valentina Balbi) and Taighde Éireann – Research Ireland under grant number GOIPG/2024/3552 (Griffen Small).

## Appendix Appendix A.Hereditary integral terms

The following compact notation for the integralsDInti​(t)\mathrm{DInt}_{i}(t)andHInti​(t)\mathrm{HInt}_{i}(t)is used throughout the manuscript:DInti​(t)=−1μ0​∫0tμ′​(t−s)​x​(s)i​dsfori=0,1,2,3,4.\mathrm{DInt}_{i}(t)=-\frac{1}{\mu_{0}}\int_{0}^{t}\mu^{\prime}(t-s)x(s)^{i}\differential{s}\qquad\text{for}\qquad i=0,1,2,3,4.(A.1)

andHInti​(t)=−1κ0​∫0tκ′​(t−s)​x​(s)i​dsfori=0,1,2.\mathrm{HInt}_{i}(t)=-\frac{1}{\kappa_{0}}\int_{0}^{t}\kappa^{\prime}(t-s)x(s)^{i}\differential{s}\qquad\text{for}\qquad i=0,1,2.(A.2)

wherex​(s)=k​(s)x(s)=k(s)in simple shear andx​(s)=ϕ​(s)x(s)=\phi(s)in torsion, according to (78).

## Appendix Appendix B.Governing equations for the slightly compressible model of torsion

The coefficientsAi​(t)A_{i}(t)appearing in the zeroth- and first-order governing equations (65) and (74), respectively, are given by the following expressions:A0=μ0​(HInt0​(t)−1),\displaystyle A_{0}=\mu_{0}(\mathrm{HInt}_{0}(t)-1),(B.3)A2=μ0​(HInt0​(t)​ϕ​(t)2−2​H​I​n​t1​(t)​ϕ​(t)+HInt2​(t)).\displaystyle A_{2}=\mu_{0}(\mathrm{HInt}_{0}(t)\phi(t)^{2}-2\mathrm{HInt}_{1}(t)\phi(t)+\mathrm{HInt}_{2}(t)).(B.4)

The coefficientsA1A_{1}andA3A_{3}of the polynomial inhomogeneous term in the zeroth-order equation are:A1=−23​(5​c1−2​c2)​ϕ​(t)2+2​μ0​ϕ​(t)​DInt1​(t)−23​(c1+8​c2)​DInt2​(t),\displaystyle A_{1}=-\dfrac{2}{3}(5c_{1}-2c_{2})\phi(t)^{2}+2\mu_{0}\phi(t)\mathrm{DInt}_{1}(t)-\dfrac{2}{3}(c_{1}+8c_{2})\mathrm{DInt}_{2}(t),(B.5)A3=−23​(c1+2​c2)​(DInt2​(t)​ϕ​(t)2−2​D​I​n​t3​(t)​ϕ​(t)+DInt4​(t)).\displaystyle A_{3}=-\dfrac{2}{3}(c_{1}+2c_{2})\Bigl(\mathrm{DInt}_{2}(t)\phi(t)^{2}-2\mathrm{DInt}_{3}(t)\phi(t)+\mathrm{DInt}_{4}(t)\Bigr).(B.6)

The coefficientsp0p_{0},p1p_{1}andp2p_{2}of the inhomogeneous term in the first-order equation are:p0\displaystyle p_{0}=−R​(A1+A3​R2)3​A0​[A0​C0​(5​c1−c2)(c1−c2)​R2+4​μ0​(DInt0​(t)−1)],\displaystyle=-\frac{R(A_{1}+A_{3}R^{2})}{3A_{0}}\left[A_{0}C_{0}\dfrac{(5c_{1}-c_{2})}{(c_{1}-c_{2})}R^{2}+4\mu_{0}(\mathrm{DInt}_{0}(t)-1)\right],(B.7)p1\displaystyle p_{1}=−R23​[A2​C0​(5​c1−c2)c1−c2−A3​(13​c1+22​c2)c1+2​c2]\displaystyle=-\dfrac{R^{2}}{3}\left[\frac{A_{2}C_{0}(5c_{1}-c_{2})}{c_{1}-c_{2}}-\frac{A_{3}(13c_{1}+22c_{2})}{c_{1}+2c_{2}}\right]+13​[A1​(7+2​c1c1+c2)+A0​C0​(−4+14​c1​c2c12−c22)−2​μ0​(DInt0​(t)−1)​(2​A2A0+ϕ​(t)2)],\displaystyle+\dfrac{1}{3}\left[A_{1}\left(7+\frac{2c_{1}}{c_{1}+c_{2}}\right)+A_{0}C_{0}\left(-4+\frac{14c_{1}c_{2}}{c_{1}^{2}-c_{2}^{2}}\right)-2\mu_{0}(\mathrm{DInt}_{0}(t)-1)\Bigl(2\dfrac{A_{2}}{A_{0}}+\phi(t)^{2}\Bigr)\right],(B.8)p2\displaystyle p_{2}=−R33​[A2​C0​(5​c1−c2)c1−c2−A3​(11−4​c1c1+2​c2)]\displaystyle=-\frac{R^{3}}{3}\left[\frac{A_{2}C_{0}(5c_{1}-c_{2})}{c_{1}-c_{2}}-A_{3}\left(11-\frac{4c_{1}}{c_{1}+2c_{2}}\right)\right]+R3​[A1​(9​c1+13​c2)c1+c2−2​A0​C0​(8−2​c1​(3​c1−4​c2)c12−c22)−2​μ0​(DInt0​(t)−1)​(2​A2A0+ϕ​(t)2)].\displaystyle+\dfrac{R}{3}\left[\frac{A_{1}(9c_{1}+13c_{2})}{c_{1}+c_{2}}-2A_{0}C_{0}\left(8-\frac{2c_{1}(3c_{1}-4c_{2})}{c_{1}^{2}-c_{2}^{2}}\right)-2\mu_{0}(\mathrm{DInt}_{0}(t)-1)\Bigl(2\dfrac{A_{2}}{A_{0}}+\phi(t)^{2}\Bigr)\right].(B.9)

The constantsC0C_{0}andC1C_{1}in the boundary conditions at the zeroth- and first-orders are:C0=23​(c1−c2)A0​(DInt2​(t)−ϕ​(t)2),\displaystyle C_{0}=\frac{2}{3}\frac{(c_{1}-c_{2})}{A_{0}}\bigl(\mathrm{DInt}_{2}(t)-\phi(t)^{2}\bigr),(B.10)C1=C0​R0​[2​c1c1−c2​r1​(R0)−(c1+7​c2)6​(c1−c2)​C0​R03]+2​μ0​(1−DInt0​(t))3​A0​R0​(2​C0​R03−3​r1​(R0)).\displaystyle C_{1}=C_{0}R_{0}\left[\frac{2c_{1}}{c_{1}-c_{2}}r_{1}(R_{0})-\frac{(c_{1}+7c_{2})}{6(c_{1}-c_{2})}C_{0}R_{0}^{3}\right]+\frac{2\mu_{0}(1-\mathrm{DInt}_{0}(t))}{3A_{0}R_{0}}\Bigl(2C_{0}R_{0}^{3}-3r_{1}(R_{0})\Bigr).(B.11)

## References
- [1]S. Ahsanizadeh and L. Li.Visco-hyperelastic constitutive modeling of soft tissues based on short and long-term internal variables.BioMedical Engineering OnLine, 14:29, 2015.
- [2]L. Anand and S. Govindjee.Continuum mechanics of solids.Oxford University Press, Oxford, UK, 2020.
- [3]Ansys Inc.Theory reference, 2026.url:https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/corp/v261/en/ans_thry/thy_mat5.html.
- [4]R. J. Atkin and N. Fox.An introduction to the theory of elasticity.Dover Publications, Mineola, NY, 2013.
- [5]V. Balbi, T. Shearer, and W. J. Parnell.A modified formulation of quasi-linear viscoelasticity for transversely isotropic materials under finite deformation.Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences, 474(2217):20180231, 2018.
- [6]V. Balbi, T. Shearer, and W. J. Parnell.Tensor decomposition for modified quasi-linear viscoelastic models: towards a fully non-linear theory.Mathematics and Mechanics of Solids, 29(6):1–25, 2023.
- [7]V. Balbi and G. Small.Ramp-and-hold relaxation test data for torsion of agarose gel, 2026.
- [8]V. Balbi, A. Trotta, M. Destrade, and A. Ní Annaidh.Poynting effect of brain matter in torsion.Soft Matter, 15(25):5147–5153, 2019.
- [9]H. Berjamin, M. Destrade, and W. J. Parnell.On the thermodynamic consistency of quasi-linear viscoelastic models for soft solids.Mechanics Research Communications, 111:103648, 2021.
- [10]S. Budday, T. C. Ovaert, G. A. Holzapfel, P. Steinmann, and E. Kuhl.Fifty shades of brain: a review on the mechanical testing and modeling of brain tissue.Archives of Computational Methods in Engineering, 27:1187–1230, 2020.
- [11]L. Causey, S. C. Cowin, and S. Weinbaum.Quantitative model for predicting lymph formation and muscle compressibility in skeletal muscle during contraction and stretch.Proceedings of the National Academy of Sciences, 109(23):9185–9190, 2012.
- [12]H. L. Cheng, J. Wang, and Z. P. Huang.A thermo-viscoelastic constitutive model for compressible amorphous polymers.Mechanics of Time-Dependent Materials, 14(3):261–275, 2010.
- [13]Dassault Systèmes.Abaqus theory guide, 2016.url:http://130.149.89.49:2080/v2016/books/stm/default.htm?startat=ch04s08ath129.html.
- [14]Dassault Systèmes.Abaqus theory guide, 2016.url:http://130.149.89.49:2080/v2016/books/stm/default.htm?startat=ch04s06ath123.html.
- [15]R. De Pascalis, D. I. Abrahams, and W. J. Parnell.On nonlinear viscoelastic deformations: a reappraisal of Fung’s quasi-linear viscoelastic model.Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences, 470(2166):20140058, 2014.
- [16]R. De Pascalis, D. I. Abrahams, and W. J. Parnell.Simple shear of a compressible quasilinear viscoelastic material.International Journal of Engineering Science, 88:64–72, 2015.
- [17]R. De Pascalis, W. J. Parnell, D. I. Abrahams, T. Shearer, D. M. Daly, and D. Grundy.The inflation of viscoelastic balloons and hollow viscera.Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences, 474(2218):20180102, 2018.
- [18]M. Destrade, Y. Du, J. Blackwell, N. Colgan, and V. Balbi.Canceling the elastic Poynting effect with geometry.Physical Review E, 107(5):L053001, 2023.
- [19]M. Destrade, M. D. Gilchrist, J. Motherway, and J. G. Murphy.Slight compressibility and sensitivity to changes in Poisson’s ratio.International Journal for Numerical Methods in Engineering, 90(4):403–411, 2011.
- [20]M. Destrade, M. D. Gilchrist, J. G. Murphy, B. Rashid, and G. Saccomandi.Extreme softness of brain matter in simple shear.International Journal of Non-Linear Mechanics, 75:54–58, 2015.
- [21]M. Destrade and G. Zurlo.Nonlinear elasticity: a concise masterclass for undergraduates.Springer, Cham, Switzerland, 2025.
- [22]S. Doll and K. Schweizerhof.On the development of volumetric strain energy functions.Journal of Applied Mechanics, 67(1):17–21, 2000.
- [23]A. Ed-Daoui and P. Snabre.Poroviscoelasticity and compression-softening of agarose hydrogels.Rheologica Acta, 60(6–7):327–351, 2021.
- [24]Y. C. Fung.Biomechanics: mechanical properties of living tissues.Springer, Berlin, Germany, 1993.
- [25]A. Greiner, N. Reiter, J. Hinrichsen, M. P. Kainz, G. Sommer, G. A. Holzapfel, P. Steinmann, E. Comellas, and S. Budday.Model-driven exploration of poro-viscoelasticity in human brain tissue: be careful with the parameters.Interface Focus, 14(6):20240026, 2024.
- [26]G. A. Holzapfel.Nonlinear solid mechanics: a continuum approach for engineering.John Wiley & Sons Ltd., Hoboken, NJ, 2000.
- [27]G. A. Holzapfel, T. C. Gasser, and M. Stadler.A structural model for the viscoelastic behavior of arterial walls: continuum formulation and finite element analysis.European Journal of Mechanics A / Solids, 21(3):441–463, 2002.
- [28]G. A. Holzapfel and J. C. Simo.A new viscoelastic constitutive model for continuous media at finite thermomechanical changes.International Journal of Solids and Structures, 33(20–22):3019–3034, 1996.
- [29]C. O. Horgan and J. G. Murphy.Constitutive models for almost incompressible isotropic elastic rubber-like materials.Journal of Elasticity, 87(2):133–146, 2007.
- [30]C. O. Horgan and J. G. Murphy.Constitutive modeling for moderate deformations of slightly compressible rubber.Journal of Rheology, 53(1):153–168, 2009.
- [31]C. O. Horgan and J. G. Murphy.Simple shearing of incompressible and slightly compressible isotropic nonlinearly elastic materials.Journal of Elasticity, 98(2):205–221, 2010.
- [32]C. O. Horgan and J. G. Murphy.Poynting effects in soft elastic materials: a review of recent results.Journal of Elasticity, 157(35):1–20, 2025.
- [33]A. Karimi, M. Haghighatnama, A. Shojaei, M. Navidbakhsh, A. Motevalli Haghi, and S. J. Adnani Sadati.Measurement of the viscoelastic mechanical properties of the skin tissue under uniaxial loading.Proceedings of the Institution of Mechanical Engineers, Part L: Journal of Materials: Design and Applications, 230(2):418–425, 2016.
- [34]E. Kirkinis and R. W. Ogden.On extension and torsion of a compressible elastic circular cylinder.Mathematics and Mechanics of Solids, 7(4):373–392, 2002.
- [35]E. Kreyszig.Advanced engineering mathematics.John Wiley & Sons Ltd., Hoboken, NJ, 2011.
- [36]M. Levinson.Finite torsion of slightly compressible rubberlike circular cylinders.International Journal of Non-Linear Mechanics, 7(4):445–463, 1972.
- [37]M. Mass, M. Herron, J. Weiss, and G. Ateshian.FEBio theory manual (version 3.4), 2022.url:https://help.febio.org/FEBioTheory/FEBio_tm_3-4-Subsection-2.4.3.html.
- [38]M. Mass, J. Weiss, and G. Ateshian.FEBio user’s manual (version 3.6), 2022.url:https://help.febio.org/docs/FEBioUser-3-6/UM36-4.1.2.9.html.
- [39]E. Matjeka, A. G. Kuchumov, H. M. Ngwangwa, T. Pandelani, and F. Nemavhola.Viscoelastic properties of porcine pericardium under biaxial tensile creep and stress relaxation: application for novel aortic valve bioprosthesis design.Bioengineering, 13(4):401, 2026.
- [40]R. W. Ogden.Non-linear elastic deformations.Dover Publications, Mineola, NY, 1997.
- [41]M. Pelliciari, S. Sirotti, and A. M. Tarantino.A strain energy function for large deformations of compressible elastomers.Journal of the Mechanics and Physics of Solids, 176:105308, 2023.
- [42]D. A. Polignone and C. O. Horgan.Pure torsion of compressible non-linearly elastic circular cylinders.Quarterly of Applied Mathematics, 49(3):591–607, 1991.
- [43]J. H. Poynting.On pressure perpendicular to the shear planes in finite pure shears, and on the lengthening of loaded wires when twisted.Proceedings of the Royal Society of London. Series A, Containing Papers of a Mathematical and Physical Character, 82(557):546–559, 1909.
- [44]B. Rashid, M. Destrade, and M. D. Gilchrist.Mechanical characterization of brain tissue in simple shear at dynamic strain rates.Journal of the Mechanical Behavior of Biomedical Materials, 28:71–85, 2013.
- [45]S. Reese and S. Govindjee.A theory of finite viscoelasticity and numerical aspects.International Journal of Solids and Structures, 35(26-27):3455–3482, 1998.
- [46]M. Righi and V. Balbi.Foundations of viscoelasticity and application to soft tissue mechanics.In J. Málek and E. Süli, editors,Modeling Biomaterials, chapter 3, pages 71–103. Springer, 2021.
- [47]F. Sidoroff.Un modèle viscoélastique non linéaire avec configuration intermédiaire.Journal de Mécanique, 13(4):679–713, 1974.
- [48]J. C. Simo.On a fully three-dimensional finite-strain viscoelastic damage model: formulation and computational aspects.Computer Methods in Applied Mechanics and Engineering, 60(2):153–173, 1987.
- [49]G. Small.Modelling the time-dependent behaviour of brain tissue in torsion.PhD thesis,, University of Galway,, Galway, Ireland, 2025.
- [50]G. Small, F. Ballatore, C. Giverso, and V. Balbi.Modelling the non-linear viscoelastic behaviour of brain tissue in torsion.Soft Matter, 21:26, 2025.
- [51]G. Small, F. Ballatore, C. Giverso, and V. Balbi.Ramp-and-hold relaxation test data for torsion of ovine brain tissue, 2025.
- [52]G. Small, H. Berjamin, and V. Balbi.Poynting effect in fluid-saturated poroelastic soft materials in torsion.International Journal of Non-Linear Mechanics, 159:104601, 2024.
- [53]A. M. Swedberg, S. P. Reese, S. A. Maas, B. J. Ellis, and J. A. Weiss.Continuum description of the Poisson’s ratio of ligament and tendon under finite deformation.Journal of Biomechanics, 47(12):3201–3209, 2014.
- [54]X. Wang, R. K. June, and D. M. Pierce.A 3-D constitutive model for finite element analyses of agarose with a range of gel concentrations.Journal of the Mechanical Behavior of Biomedical Materials, 114:104150, 2021.
- [55]A. Wineman.Nonlinear viscoelastic solids—a review.Mathematics and Mechanics of Solids, 14(3):300–366, 2009.
- [56]G. Zurlo, J. Blackwell, N. Colgan, and M. Destrade.The Poynting effect.American Journal of Physics, 88(12):1036–1140, 2020.

## 


- 


Major funding support from
