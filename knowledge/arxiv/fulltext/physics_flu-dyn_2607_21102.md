# A One-Dimensional Integral Equation for a Porous Horizontal Disc under Water Waves

**arXiv ID**: 2607.21102v1
**Authors**: Luiz Fernando de Moraes Campos Filho, Leandro Farina, Juliana Sartori Ziebell
**Published**: 2026-07-23
**Categories**: physics.flu-dyn, math-ph
**Comments**: 16 pages, 8 figures. Accepted for publication in Ciência e Natura
**HTML URL**: https://arxiv.org/html/2607.21102v1

## Abstract

Wave scattering by a thin, porous circular plate submerged in deep water is investigated. The problem is formulated as a second-kind hypersingular Fredholm integral equation over the unit disk, solved numerically using the Boundary Element Method. The analysis focuses on calculating hydrodynamic forces, specifically added mass (real part) and damping coefficient (imaginary part). Results demonstrate the influence of the porosity parameter G: less porous plates (G real) increase added mass and hydrodynamic force, while more porous plates (G imaginary) reduce these effects but increase the damping coefficient. The proposed formulation is validated, showing excellent agreement with established literature.

## Full Text

A One-Dimensional Integral Equation for a Porous Horizontal Disc under Water Waves

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
- License: CC BY 4.0arXiv:2607.21102v1 [physics.flu-dyn] 23 Jul 2026

## A One-Dimensional Integral Equation for a Porous Horizontal Disc under Water WavesLuiz Fernando de Moraes Campos Filho1Leandro Farina2Juliana Sartori Ziebell2
1Federal Institute of Mato Grosso, MT, Brazil
2Institute of Mathematics and Statistics,
Federal University of Rio Grande do Sul, RS, Brazil
campos.filho@ifmt.edu.brfarina@mat.ufrgs.brjulianaziebell@ufrgs.br
ORCID:
Campos Filho0009-0006-4600-4914;
Farina0000-0003-2744-515X;
Ziebell0000-0001-8244-5051

## Abstract

Wave scattering by a thin, porous circular plate submerged in deep water is
investigated. The problem is formulated as a second-kind hypersingular Fredholm
integral equation over the unit disk, solved numerically using the Boundary
Element Method. The analysis focuses on calculating hydrodynamic forces,
specifically added mass (real part) and damping coefficient (imaginary part).
Results demonstrate the influence of the porosity parameterGG: less porous
plates (GGreal) increase added mass and hydrodynamic force, while more porous
plates (GGimaginary) reduce these effects but increase the damping
coefficient. The proposed formulation is validated, showing excellent agreement
with established literature.

Keywords:Porous Plate; Added Mass; Water Waves;
Damping Coefficient; Hypersingular Equation.

Resumo.O espalhamento de ondas por uma placa circular fina e porosa submersa em águas
profundas é investigado. O problema é formulado como uma equação integral
hipersingular de Fredholm do segundo tipo sobre o disco unitário, resolvida
numericamente pelo Método de Elementos de Contorno. A análise se concentra no
cálculo das forças hidrodinâmicas, expressas em termos de massa adicional
(parte real) e coeficiente de amortecimento (parte imaginária). Os resultados
demonstram a influência do parâmetro de porosidadeGG: placas menos porosas
(GGreal) aumentam a massa adicional e a força hidrodinâmica, ao passo que
placas mais porosas (GGimaginário) reduzem esses efeitos e elevam o
coeficiente de amortecimento. A formulação proposta é validada por meio de
excelente concordância com a literatura.

Palavras-chave:Disco Poroso; Massa Adicional; Ondas de Água;
Coeficiente de Amortecimento; Equação Hipersingular.

## 1INTRODUCTION

The study of wave interaction with a submerged horizontal body has been the object of great attention from researchers in the field of marine hydrodynamics and coastal engineering. A submerged horizontal platform can serve as an essential component in various coastal and offshore structures. Its application ranges from breakwaters(Yu and Chwang,1994a)and wave energy converters (WECs)(Astariz and Iglesias,2015)to coastal barriers, very large floating structures (VLFS)(Lamas-Pardoet al.,2015), and semi-submersible floating offshore wind turbines (FOWT)(Antonuttiet al.,2014; Lopez-Pavon and Souto-Iglesias,2015). The motivation for its use stems from the versatility and effectiveness of this configuration in different maritime contexts.

According toFarina (2012), the relevance of these studies is justified, as the evaluation of the hydrodynamic force acting on the floating and/or submerged body is fundamental in many problems of interest to ocean engineers and naval architects. For example, in industrial, scientific, commercial, and military activities at sea, it is important to understand the influence that waves exert on large floating or submerged structures in the water.

A range of possible cases exists in the study of wave interaction with submerged bodies, considering the possibilities of the geometry and material of the body under analysis. In this work, studies related to cases where the bodies are thin rigid plates or thin porous plates are presented.

The study of wave interaction with submerged rigid bodies/plates has been carried out by various authors. A starting point is the problem for a floating obstacle, also known as thedock problem(Garrett,1971). Such a problem can be reduced to solving a second-kind Fredholm boundary integral equation for the velocity potential.Islamet al.(2019)studied the scattering and radiation of water waves by a submerged rigid disc in a two-layer fluid, reducing the problem to a one-dimensional second-kind Fredholm integral equation, and the results were presented in terms of the hydrodynamic force.Daset al.(2022b)conducted the same study, but in a three-layer fluid. Parsons and Martin, in a series of publications (Parsons and Martin,1992;Parsons and Martin,1994;Parsons and Martin,1995;Martinet al.,1997) investigated several two-dimensional water wave problems, reducing the study to hypersingular integral equations. These investigations addressed scattering problems by submerged flat discs(Parsons and Martin,1992), curved plates and plates emerging at the surface(Parsons and Martin,1994), and water wave trapping by submerged plates(Parsons and Martin,1995). They utilized an expansion-collocation method to solve the one-dimensional equations, employing Chebyshev polynomials of the second kind for the expansion inParsons and Martin (1994).Ziebell and Farina (2012)studied the submersion of a thin, rough, circular disc in a deep-water free surface. The problem was reduced to a hypersingular equation over the body’s boundary, and the results were presented in terms of the hydrodynamic force. A study similar to that ofZiebell and Farina (2012)was presented byFarinaet al.(2017). A key methodological distinction lies in the plate geometry:Ziebell and Farina (2012)investigated thin, rough plates, whileFarinaet al.(2017)focused on thin, smooth, and nearly circular plates. Additionally, the mathematical approaches for solving the problem also differ:Ziebell and Farina (2012)employed the perturbation method to obtain the governing equation, whereasFarinaet al.(2017)utilized conformal mapping. In both works, the results were presented in terms of the hydrodynamic force.

The interaction of waves with porous plates in two dimensions has also been the subject of investigation by various authors, and the results are presented in terms of wave reflection and transmission.Sollitt and Cross (1972)presented the first theoretical research on wave propagation in a porous medium, where reflection and transmission coefficients for a permeable breakwater of rectangular cross-section were predicted. The mathematical model is developed by expressing the normal fluid velocity through the porous plate as proportional to the jump in the velocity potential across the plate(Chwang and Wu,1994, eq 2). This relationship is based on the assumption that the flow in the porous medium is governed by Darcy’s law(Chwang,1983). Subsequently, singular integral equation methods have been applied to two-dimensional wave-porous plate problems; Gayen and Mondal used Chebyshev polynomial-based expansion-collocation methods to solve the governing hypersingular equations for a submerged porous plate(Gayen and Mondal,2014)and for two symmetric inclined permeable plates(Gayen and Mondal,2016), whileKoleyet al.(2018)considered the scattering of waves by a floating flexible porous plate using Fredholm integral equations and obtained solutions using Simpson’s quadrature formula.

According toDe Freitaset al.(2021), the investigation of the interaction of three-dimensional waves with porous plates has received less attention to date and has mainly relied on the eigenfunction expansion method.Chwang and Wu (1994)andLiuet al.(2011)addressed the phenomenon of wave scattering by a submerged horizontal porous disc. The former study discussed the non-dimensional surface elevation and the vertical wave force. The latter study presented results related to the non-dimensional wave height concerning water depth and disc radius, in addition to the vertical force exerted on the disc. On the other hand,Molin and Nielsen (2004)analyzed the axisymmetric problem of water wave propagation around a submerged porous disc, providing data on the added mass and damping coefficients as a function of the Keulegan-Carpenter number. Recently, several studies(Dokkenet al.,2017; Ouled Housseine,2019; Mackayet al.,2019)have focused on the diffraction and radiation of waves by bodies with porous components, providing data on the added mass and damping coefficients, although they did not specifically address the case of porous plates.

The study of porous plates introduces a parameter of great importance, theporous effect parameter, represented byGG. The works byYu (1995),Yu and Chwang (1994a),Yu and Chwang (1994b)introduced a boundary condition for thin porous plates, in whichGGdepends on the resistance force (ff), the inertial coefficient (SS), and the geometric properties of the porous plate. SinceGGis a complex number, it is defined asG=γ​(f−i​S)K​b¯​(f2+S2)=Gr+i​Gi,\centering G=\frac{\gamma(f-iS)}{K\bar{b}(f^{2}+S^{2})}=G_{r}+iG_{i},\@add@centering(1)

whereγ\gammais the plate porosity, defined as the ratio between the volume of the porous part and the total volume,b¯\bar{b}is the physical thickness of the porous plate, andK=ω2/gK=\omega^{2}/g, withggbeing the acceleration of gravity andω\omegathe wave angular frequency.

Daset al.(2022a)investigated the radiation and scattering of flexural gravity waves by a submerged porous disc in a deep ocean with ice cover, assuming linear theory. The problem was reduced to the solution of a hypersingular boundary integral equation that can be further reduced to a system of one-dimensional Fredholm integral equations of the second kind. The hydrodynamic force for the scattering problem, and the added mass and damping coefficients for the radiation problem, were determined and numerically computed.

In this work, the wave radiation by a submerged porous disc in a free surface fluid, but without the ice layer, will also be investigated. Although the work presented byDaset al.(2022a)is more general, this research employs a different method. Following the steps ofFarina and Martin (1997), the governing integral equation is reduced to a one-dimensional integral equation under axisymmetric motion. We employ the Boundary Element Method with robust numerical integrations to validate the integral formulation against results fromFarina and Martin (1997)andDe Freitaset al.(2021). The added mass and damping coefficients will be analyzed, with new numerical results detailing their dependence on the wavenumber for different porosity coefficientsGGand different depthsdd.

## 2METHODOLOGY

## 2.1Formulation

Consider a Cartesian coordinate system(x,y,z)(x,y,z), wherez<0z<0andz=ζ​(x,y,t)z=\zeta(x,y,t)defines the free surface elevation. Also consider that a body, with surfaceDD, is fully submerged below the free surface of a given fluid;DDis a circular, porous and closed surface, as presented in Figure1.Figure 1:Geometry of the problem studied.

Assume that the fluid motion is of small amplitude, irrotational, incompressible and inviscid to allow the introduction of a velocity potentialR​e​{ϕ​(x,y,z)​e−i​ω​t}Re\left\{\phi(x,y,z)e^{-i\omega t}\right\}, whereϕ\phisatisfies the following conditions, as presented inFarina (2012)(∂2∂x2+∂2∂y2+∂2∂z2)​ϕj=0,\left(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}\right)\phi_{j}=0,(2)∂ϕj∂z−K​ϕj=0,j=1,…,7,\frac{\partial\phi_{j}}{\partial z}-K\phi_{j}=0,\penalty 10000\ j=1,\ldots,7,(3)∂ϕj∂n=Vj+i​K​G​[ϕj],o​n​D,\frac{\partial\phi_{j}}{\partial n}=V_{j}+iKG\left[\phi_{j}\right],\penalty 10000\ on\penalty 10000\ D,(4)

whereK=ω2/gK=\omega^{2}/g,ggis the acceleration due to gravity,ω\omegais the frequency,[ϕj​(q)]=ϕj​(q+)−ϕj​(q−)\left[\phi_{j}(q)\right]=\phi_{j}(q^{+})-\phi_{j}(q^{-})is the jump inϕ\phiacross the disk, withq+q^{+}andq−q^{-}being the “positive” and “negative” sides ofDD, respectively.
Furthermore, it is required thatϕ\phisatisfies the radiation condition given byNewman (1977)limr→∞r1/2​(∂ϕj∂r−i​K​ϕj)→0,j=1,…,7,\lim_{r\rightarrow\infty}{r^{1/2}\left(\frac{\partial\phi_{j}}{\partial r}-iK\phi_{j}\right)}\rightarrow 0,\penalty 10000\ j=1,\ldots,7,(5)

wherer=(x2+y2)1/2r=(x^{2}+y^{2})^{1/2}.

Using Green’s theorem, the problem reduces to solving the hypersingular integral equation presented below.14​π​∫×D[ϕ​(q)]​∂2𝒢​(p,q)∂np​∂nq​d​Aq−i​K​G​[ϕj]​(p)=Vj,\frac{1}{4\pi}{\int{\!\!\!\!\!\!\times}}_{D}{\left[\phi(q)\right]\frac{\partial^{2}{\cal{G}}(p,q)}{\partial n_{p}\partial n_{q}}dA_{q}}-iKG\left[\phi_{j}\right](p)=V_{j},(6)

where𝒢​(P,Q)≡𝒢​(x,y,z;ξ,η,ζ)=(R2+(z−ζ)2)−1/2+𝒢1​(R,z+ζ),{\cal{G}}(P,Q)\equiv{\cal{G}}(x,y,z;\xi,\eta,\zeta)=(R^{2}+(z-\zeta)^{2})^{-1/2}+{\cal{G}}_{1}(R,z+\zeta),(7)𝒢1​(R,z+ζ)=∫∪0∞ek​(z+ζ)​J0​(k​R)​k+Kk−K​d​k,{\cal{G}}_{1}(R,z+\zeta)={\int{\!\!\!\!\!\!\cup}}_{0}^{\infty}{e^{k(z+\zeta)}J_{0}(kR)\frac{k+K}{k-K}dk},(8)

in which𝒢1{\cal{G}}_{1}is a Green function used as the fundamental solution,R=((x−ξ)2+(y−η)2)1/2R=((x-\xi)^{2}+(y-\eta)^{2})^{1/2},J0J_{0}is a Bessel function,P=(x,y,z)P=(x,y,z)andQ=(ξ,η,ζ)Q=(\xi,\eta,\zeta), as seen inDe Freitaset al.(2021).

## 2.2Reduction to a One-Dimensional Integral Equation

Following the mathematical framework established inFarina and Martin (1997), the current objective is to introduce polar coordinates for the field pointppand source pointqq, expand the relevant physical quantities into Fourier series regarding the angular variables, and define an unknown auxiliary functionψ\psi. This procedure successfully reduces the governing formulation to a one-dimensional integral equation. The systematic sequence of simplifications is detailed as follows.

The field pointp=(x,y)p=(x,y)is expressed asp=(r​cos⁡θ,r​sin⁡θ)p=(r\cos\theta,r\sin\theta)withinΩ\Omega, and similarly, the source pointq=(ξ,η)q=(\xi,\eta)is defined asq=(ρ​cos⁡φ,ρ​sin⁡φ)q=(\rho\cos\varphi,\rho\sin\varphi)withinΩ\Omega, where the area element isd​Ω=ρ​d​ρ​d​φd\Omega=\rho d\rho d\varphi. By expanding all quantities into Fourier series in the angular variables, equation (6) is transformed into:[fn]j​(r)=[Vn]j​(r)−12​∫01wn​(ρ)​Mn​(r,ρ)​ρ​𝑑ρ+i​K​G​wn​(r),[f_{n}]_{j}(r)=[V_{n}]_{j}(r)-\frac{1}{2}\int_{0}^{1}{w_{n}(\rho)M_{n}(r,\rho)\rho d\rho}+iKGw_{n}(r),(9)

wherewnw_{n}denotes the potential jump density satisfying a one-dimensional integral equation. The interaction kernel is defined asMn​(r,ρ)=∫∪0∞e−k​b​Jn​(k​r)​Jn​(k​ρ)​k2​(k+K)k−K​d​k.\displaystyle M_{n}(r,\rho)={\int{\!\!\!\!\!\!\cup}}_{0}^{\infty}{e^{-kb}J_{n}(kr)J_{n}(k\rho)k^{2}\frac{(k+K)}{k-K}dk}.

In this context,[fn][f_{n}]represents the radial component of the auxiliary potential acting on the disk, while[Vn][V_{n}]represents the radial amplitude of the generalized body velocity for each Fourier modenn.

As established by in the literatureGuidera (1975),wnw_{n}andfnf_{n}are related via the following integral identity:wn​(r)=−4π​rn​∫r1t−2​nt2−r2​∫0tsn+1t2−s2​fn​(s)​𝑑s​𝑑t,n=0,1,2,…w_{n}(r)=-\frac{4}{\pi}r^{n}\int_{r}^{1}{\frac{t^{-2n}}{\sqrt{t^{2}-r^{2}}}}\int_{0}^{t}{\frac{s^{n+1}}{\sqrt{t^{2}-s^{2}}}f_{n}(s)dsdt},\quad n=0,1,2,\dots(10)

Substituting (9) into (10) yields:wn​(r)=wn∞​(r)+∫01wn​(ρ)​Ln​(r,ρ)​ρ​𝑑ρ−4π​i​K​G​rn​∫r11t2​n​(t2−r2)1/2​∫0tsn+1(t2−s2)1/2​wn​(s)​𝑑s​𝑑t,\begin{array}[]{cc}w_{n}(r)=\displaystyle w_{n}^{\infty}(r)+\int_{0}^{1}w_{n}(\rho)L_{n}(r,\rho)\rho d\rho\\
\displaystyle-\frac{4}{\pi}iKGr^{n}\int_{r}^{1}{\frac{1}{t^{2n}(t^{2}-r^{2})^{1/2}}}\int_{0}^{t}\frac{s^{n+1}}{(t^{2}-s^{2})^{1/2}}w_{n}(s)dsdt,\end{array}(11)

where the incident potential termwn∞w_{n}^{\infty}and the modified kernelLnL_{n}are defined as:wn∞​(r)=−4π​rn​∫r11t2​n​(t2−r2)1/2​∫0tsn+1(t2−s2)1/2​Vn​(s)​𝑑s​𝑑tw_{n}^{\infty}(r)=-\frac{4}{\pi}r^{n}\int_{r}^{1}{\frac{1}{t^{2n}(t^{2}-r^{2})^{1/2}}}\int_{0}^{t}{\frac{s^{n+1}}{(t^{2}-s^{2})^{1/2}}V_{n}(s)dsdt}(12)

andLn​(r,ρ)=2π​ρ​rn​∫r11t2​n​(t2−r2)1/2​∫0tsn+1(t2−s2)1/2​Mn​(s,ρ)​𝑑s​𝑑t.L_{n}(r,\rho)=\frac{2}{\pi}\rho r^{n}\int_{r}^{1}{\frac{1}{t^{2n}(t^{2}-r^{2})^{1/2}}}\int_{0}^{t}{\frac{s^{n+1}}{(t^{2}-s^{2})^{1/2}}M_{n}(s,\rho)dsdt}.(13)

A new unknown auxiliary functionψn\psi_{n}is introduced, related townw_{n}through the following integral transformation:wn​(r)=Dn​rn​∫r1ψn​(t)tn​(t2−r2)1/2​𝑑t,w_{n}(r)=D_{n}r^{n}\int_{r}^{1}{\frac{\psi_{n}(t)}{t^{n}(t^{2}-r^{2})^{1/2}}dt},(14)

whereDnD_{n}is an arbitrary normalization constant. Comparing this relation with (10) yields:ψn​(t)=ψn∞​(t)+2π​t−n​∫0tsn+1(t2−s2)1/2​Fn​(s)​𝑑s,\psi_{n}(t)=\psi_{n}^{\infty}(t)+\frac{2}{\pi}t^{-n}\int_{0}^{t}{\frac{s^{n+1}}{(t^{2}-s^{2})^{1/2}}F_{n}(s)ds},(15)

with the respective terms defined as:ψn∞​(t)=−4π​Dn​t−n​∫0tsn+1(t2−s2)1/2​Vn​(s)​𝑑s\psi_{n}^{\infty}(t)=-\frac{4}{\pi D_{n}}t^{-n}\int_{0}^{t}{\frac{s^{n+1}}{(t^{2}-s^{2})^{1/2}}V_{n}(s)ds}(16)

andFn​(s)=1Dn​[(∫01wn​(ρ)​Mn​(s,ρ)​ρ​𝑑ρ)−2​i​K​G​wn​(s)].F_{n}(s)=\frac{1}{D_{n}}\left[\left(\int_{0}^{1}{w_{n}(\rho)M_{n}(s,\rho)\rho d\rho}\right)-2iKGw_{n}(s)\right].(17)

Following the approach established byFarina and Martin (1997), the governing equation for the potentialψn\psi_{n}is reformulated as:ψn​(x)=ψn∞​(x)−zn​(x)−∫01ψn​(y)​Nn​(x,y)​𝑑y,\psi_{n}(x)=\psi_{n}^{\infty}(x)-z_{n}(x)-\int_{0}^{1}\psi_{n}(y)N_{n}(x,y)dy,(18)

wherezn​(x)z_{n}(x)represents the porous contribution:zn​(x)=4π​i​K​G​x−n​∫0x∫s1s2​n+1(x2−s2)1/2​ψn​(y)yn​(y2−s2)1/2​𝑑s​𝑑yz_{n}(x)=\frac{4}{\pi}iKGx^{-n}\int_{0}^{x}\int_{s}^{1}\frac{s^{2n+1}}{(x^{2}-s^{2})^{1/2}}\frac{\psi_{n}(y)}{y^{n}(y^{2}-s^{2})^{1/2}}dsdy(19)

andNn​(x,y)N_{n}(x,y)denotes the free-surface kernel:Nn​(x,y)=2π​x​y​∫∪0∞e−k​b​jn​(k​x)​jn​(k​y)​k2​k+Kk−K​d​k.N_{n}(x,y)=\frac{2}{\pi}xy{\int{\!\!\!\!\!\!\cup}}_{0}^{\infty}{e^{-kb}j_{n}(kx)j_{n}(ky)k^{2}\frac{k+K}{k-K}dk}.(20)

This formulation is consistent with the work ofDaset al.(2022b), recovering the pure free-surface case when the ice rigidity and inertia parameters vanish.

Under the assumption of purely vertical (heave) oscillations, equation (18) reduces to the following one-dimensional governing integral equation:ψ​(x)+∫01ψ​(y)​𝒦​(x,y)​𝑑y+∫0xψ​(y)​ℐ​(x,y)​𝑑y+∫x1ψ​(y)​ℛ​(x,y)​𝑑y=x,0≤x≤1.\boxed{\begin{array}[]{c}\displaystyle\psi(x)+\int_{0}^{1}{\psi(y){\cal{K}}(x,y)dy}+\int_{0}^{x}{\psi(y){\cal{I}}(x,y)dy}+\displaystyle\int_{x}^{1}{\psi(y){\cal{R}}(x,y)dy}=x,\quad 0\leq x\leq 1.\end{array}}(21)

The kernels are defined as:𝒦​(x,y)=−N0​(x,y)+4π​i​K​G​ln⁡(|x|+|y|),{\cal{K}}(x,y)=-N_{0}(x,y)+\frac{4}{\pi}iKG\ln(|x|+|y|),(22)ℐ​(x,y)=−2π​i​K​G​ln⁡(x2−y2),{\cal{I}}(x,y)=-\frac{2}{\pi}iKG\ln(x^{2}-y^{2}),(23)ℛ​(x,y)=−2π​i​K​G​ln⁡(y2−x2),{\cal{R}}(x,y)=-\frac{2}{\pi}iKG\ln(y^{2}-x^{2}),(24)

andN0​(x,y)=bπ​(b2+X2)−1+2​Kπ​Φ0​(X,b)−bπ​(b2+T2)−1−2​Kπ​Φ0​(T,b),N_{0}(x,y)=\frac{b}{\pi}(b^{2}+X^{2})^{-1}+\frac{2K}{\pi}\Phi_{0}(X,b)-\frac{b}{\pi}(b^{2}+T^{2})^{-1}-\frac{2K}{\pi}\Phi_{0}(T,b),(25)

whereX=x−yX=x-yandT=x+yT=x+y. Here,Φ0\Phi_{0}is a two-dimensional wave potential that can be efficiently evaluated using the expansion provided byYu and Ursell (1961):Φ0​(B,C)=\displaystyle\Phi_{0}(B,C)=−e−K​C​[(ln⁡(K​S)−i​π+γ)​cos⁡(K​B)+β​sin⁡(K​B)]\displaystyle-e^{-KC}\left[(\ln(KS)-i\pi+\gamma)\cos(KB)+\beta\sin(KB)\right](26)+∑m=1∞(−K​S)mm!​(∑k=1m1k)​cos⁡(m​β).\displaystyle+\sum_{m=1}^{\infty}\frac{(-KS)^{m}}{m!}\left(\sum_{k=1}^{m}\frac{1}{k}\right)\cos(m\beta).

This model preserves the functional dependence on the wavenumberKK, the porosity parameterGG, and the submergenced=b/2d=b/2.

## 2.3The Connection with the Love-Lieb Equation

In this section, the simplifications that emerge from the problem formulation under specific conditions, notably when the wave numberKKis zero, are explored. This particular case reveals a direct connection with the classic Love equation, a fundamental problem in potential theory that describes the behavior of submerged discs in an incompressible and irrotational fluid. By examining this reduction, the consistency of the approach under analysis is not only validated, but a starting point for future investigations into the generalizations of the Love equation, particularly relevant for fluid-structure interaction, is also established.

Indeed, whenK=0K=0, the governing integral equation (21) simplifies toψ​(x)+∫01ψ​(y)​[−N0​(x,y)]​𝑑y=x,0≤x≤1.\psi(x)+\int_{0}^{1}{\psi(y)\left[-N_{0}(x,y)\right]dy}=x,\penalty 10000\ 0\leq x\leq 1.(27)

Considering the expression forN0​(x,y)N_{0}(x,y)given in (21), this equation can be explicitly rewritten asψ​(x)−bπ​∫01ψ​(y)b2+(x−y)2​𝑑y+bπ​∫01ψ​(y)b2+(x+y)2​𝑑y=x,0≤x≤1,\psi(x)-\frac{b}{\pi}\int_{0}^{1}\frac{\psi(y)}{b^{2}+(x-y)^{2}}dy+\frac{b}{\pi}\int_{0}^{1}\frac{\psi(y)}{b^{2}+(x+y)^{2}}dy=x,\penalty 10000\ 0\leq x\leq 1,(28)

whered=b2d=\frac{b}{2}.

Equation (28) shows a notable similarity with the family of integral equations known as the Love-Lieb equations. More precisely, it resembles the simplest form, (L1±L_{1}^{\pm}), presented inFarinaet al.(2022), especially when restricted to the interval0≤x≤10\leq x\leq 1. The imposition ofK=0K=0on the free surface condition of the problem under analysis is physically equivalent to the presence of a mirrored disc, which, in terms of an electrostatic problem, would correspond to the configuration of two coaxial discs separated by a distancedd(Farinaet al.,2022).

It is important to emphasize that, to date, no closed-form analytical solution is known for the Love-Lieb equations, which consolidates them as a fundamental and challenging problem in potential theory. Equation (28), therefore, represents a natural generalization of this classical formulation. This generalization not only allows for the adaptation of the problem to different hydrodynamic contexts but can also be interpreted as an alternative form of the Love-Lieb equations, expanding their scope of application in problems involving fluid-structure interaction.

## 3NUMERICAL METHOD

Equation (21) is formulated as a Fredholm integral equation of the second kind featuring a singular kernel. The numerical treatment of these inherent singularities was addressed using the Boundary Element Method (BEM) followingFanget al.(1994)coupled with theD01GCFroutine from theNAGlibrary(The Numerical Algorithms Group,n.d), which is based on the rigorous evaluation of potential integrals(Farina,2001). This routine employs the Korobov-Conroy Number-Theoretic Method (NTM) to approximate definite integrals in up to 20 dimensions; further theoretical details regarding this method are available inFanget al.(1994).

The strategy to mitigate the singularity involved decomposing the original kernel into two distinct components, followed by partitioning the integration domain into subintervals adjacent to the singular point. Under this framework, the resulting integrals were evaluated using theD01GCFroutine. The discretization procedure partitioned the interval[0,1][0,1]intonnfinite elements, denoted asIj=[(j−1)/n,j/n]I_{j}=[(j-1)/n,j/n], adopting the midpoint as the collocation node, defined byxj=(2​j−1)/(2​n)x_{j}=(2j-1)/(2n).

Similarly, the intervals[0,x]\left[0,x\right]and[x,1]\left[x,1\right]are discretized using the same subintervals, with the indexpprunning from11tojjand the indexqqrunning fromj+1j+1tonn.
Note thatIp∪Iq=[0,1]I_{p}\cup I_{q}=\left[0,1\right]. 
The collection of all subintervals indexed byppandqqcovers the entire domain[0,1][0,1].
With this in hand, (21) is rewritten asψ​(x)+∑j=1n∫Ijψ​(y)​𝒦​(x,y)​𝑑y+∑p=1j∫Ipψ​(y)​ℐ​(x,y)​𝑑y+∑q=j+1n∫Iqψ​(y)​ℛ​(x,y)​𝑑y=x,\begin{array}[]{cc}\displaystyle\psi(x)+\sum_{j=1}^{n}{\int_{I_{j}}{\psi(y){\cal{K}}(x,y)dy}}+\sum_{p=1}^{j}\int_{I_{p}}{\psi(y){\cal{I}}(x,y)dy}\displaystyle+\sum_{q=j+1}^{n}\int_{I_{q}}{\psi(y){\cal{R}}(x,y)dy}=x,\end{array}(29)

and evaluated at each collocation pointxix_{i},i=1,2,3,…,ni=1,2,3,\ldots,n.ψ​(xi)+∑j=1n∫Ijψ​(y)​𝒦​(xi,y)​𝑑y+∑p=1j∫Ipψ​(y)​ℐ​(xi,y)​𝑑y+∑q=j+1n∫Iqψ​(y)​ℛ​(xi,y)​𝑑y=xi\psi(x_{i})+\sum_{j=1}^{n}{\int_{I_{j}}{\psi(y){\cal{K}}(x_{i},y)dy}}+\sum_{p=1}^{j}{\int_{I_{p}}{\psi(y){\cal{I}}(x_{i},y)dy}}+\sum_{q=j+1}^{n}{\int_{I_{q}}{\psi(y){\cal{R}}(x_{i},y)dy}}=x_{i}(30)

It is now assumed thatψ\psiis a step function of the typeψ​(x)={ψi,x∈[i−1n,in)0,x∉[i−1n,in).\psi(x)=\left\{\begin{array}[]{cc}\psi_{i},\penalty 10000\ x\in\left[\frac{i-1}{n},\frac{i}{n}\right)\\
0,\penalty 10000\ x\notin\left[\frac{i-1}{n},\frac{i}{n}\right)\end{array}.\right.(31)

Thus, (29) can be approximated byψ​(xi)+∑j=1nψj​∫Ij𝒦​(xi,y)​𝑑y+∑p=1jψp​∫Ipℐ​(xi,y)​𝑑y+∑q=j+1nψq​∫Iqℛ​(xi,y)​𝑑y=xi\psi(x_{i})+\sum_{j=1}^{n}{\psi_{j}\int_{I_{j}}{{\cal{K}}(x_{i},y)dy}}+\sum_{p=1}^{j}{\psi_{p}\int_{I_{p}}{{\cal{I}}(x_{i},y)dy}}+\sum_{q=j+1}^{n}{\psi_{q}\int_{I_{q}}{{\cal{R}}(x_{i},y)dy}}=x_{i}(32)

Writing equation (32) in matrix form, we obtain(I+A+B+C)​ψ=x,(I+A+B+C)\psi=x,(33)

whereIIis then×nn\times nidentity matrix,ψ=[ψ1​ψ2​…​ψn]T\psi=[\psi_{1}\psi_{2}\ldots\psi_{n}]^{T}is the vector of unknown coefficients,x=[x1​x2​…​xn]Tx=[x_{1}x_{2}\ldots x_{n}]^{T}is the vector of collocation points,A=[ai,j]i,j=1nA=\left[a_{i,j}\right]_{i,j=1}^{n}is a matrix,B=[bi,j]i,j=1nB=\left[b_{i,j}\right]_{i,j=1}^{n}is a lower triangular matrix,C=[ci,j]i,j=1nC=\left[c_{i,j}\right]_{i,j=1}^{n}is an upper triangular matrix, andA=∫Ij[−N0​(x,y)+4π​i​K​G​ln⁡(|x|+|y|)]​𝑑y,A=\int_{I_{j}}{\left[-N_{0}(x,y)+\frac{4}{\pi}iKG\ln(|x|+|y|)\right]dy},B=∫Ip−2π​i​K​G​ln⁡(x2−y2)​d​y,C=∫Iq−2π​i​K​G​ln⁡(y2−x2)​d​yB=\int_{I_{p}}{-\frac{2}{\pi}iKG\ln(x^{2}-y^{2})dy},\penalty 10000\ C=\int_{I_{q}}{-\frac{2}{\pi}iKG\ln(y^{2}-x^{2})dy}N0​(xi,y)=bπ​(b2+(xi−y)2)−1+2​Kπ​Φ0​(xi−y,b)−bπ​(b2+(xi+y)2)−1−2​Kπ​Φ0​(xi+y,b).N_{0}(x_{i},y)=\frac{b}{\pi}(b^{2}+(x_{i}-y)^{2})^{-1}+\frac{2K}{\pi}\Phi_{0}(x_{i}-y,b)-\frac{b}{\pi}(b^{2}+(x_{i}+y)^{2})^{-1}-\frac{2K}{\pi}\Phi_{0}(x_{i}+y,b).

In this way, we obtain a linear system that we can solved numerically. With the obtained value ofψ\psi, the added mass and damping coefficient are calculated as indicated inFalnes (2002),𝒜​(K,b)+i​ℬ​(K,b)=8​∫01ψ​(x)​x​𝑑x,{\cal A}(K,b)+i{\cal B}(K,b)=8\int_{0}^{1}{\psi(x)x}dx,(34)

where𝒜{\cal A}is the added mass andℬ{\cal B}is the damping coefficient andd=b2d=\frac{b}{2}.

## 4RESULTS AND DISCUSSION

The linear system derived from the discretization of the governing equation was implemented in FORTRAN, with simulations conducted following the methodology proposed byDe Freitaset al.(2021)for benchmarking purposes. Model validation included a grid independence test, resulting in the selection of a quadrilateral mesh withN=80N=80. The choice of this discretization level was based on convergence analysis and is supported by the methodological precedent ofDaset al.(2022a), who employed an identical parameter in a related study. This configuration proved adequate to ensure the numerical precision required for the subsequent analyses.Table 1:Mesh independence -d=0.1d=0.1andK=0.5K=0.5.NGG𝒜{\cal{A}}ℬ{\cal{B}}GG𝒜{\cal{A}}ℬ{\cal{B}}50G=0.1G=0.1−8.6628-8.66289.80619.8061G=0.1​iG=0.1i−9.2606-9.26069.32029.320260G=0.1G=0.1−8.6640-8.66409.82639.8263G=0.1​iG=0.1i−9.2543-9.25439.33569.335670G=0.1G=0.1−8.6715-8.67159.84409.8440G=0.1​iG=0.1i−9.2495-9.24959.34809.348080G=0.1G=0.1−8.6720-8.67209.85589.8558G=0.1​iG=0.1i−9.2471-9.24719.35309.353090G=0.1G=0.1−8.6720-8.67209.85589.8558G=0.1​iG=0.1i−9.2471-9.24719.35309.3530Table 2:Mesh independence -d=0.2d=0.2andK=0.5K=0.5.NGG𝒜{\cal{A}}ℬ{\cal{B}}GG𝒜{\cal{A}}ℬ{\cal{B}}GG𝒜{\cal{A}}ℬ{\cal{B}}50G=0G=04.77454.77458.61318.6131G=1G=13.26363.26365.07595.0759G=0.7+0.3​iG=0.7+0.3i3.75383.75386.81986.819860G=0G=04.76694.76698.61208.6120G=1G=13.27513.27515.06475.0647G=0.7+0.3​iG=0.7+0.3i3.76223.76226.80626.806270G=0G=04.76314.76318.61188.6118G=1G=13.28123.28125.06285.0628G=0.7+0.3​iG=0.7+0.3i3.77523.77526.80666.806680G=0G=04.76224.76228.61118.6111G=1G=13.28313.28315.06175.0617G=0.7+0.3​iG=0.7+0.3i3.78803.78806.80976.809790G=0G=04.76224.76228.61118.6111G=1G=13.28313.28315.06175.0617G=0.7+0.3​iG=0.7+0.3i3.78803.78806.80976.8097

The results of the problem under study are presented next, detailing the Added Mass (𝒜{\cal{A}}) and Damping Coefficient (ℬ{\cal{B}}). These coefficients were calculated for a variety ofGGvalues, which will be presented later. For the analysis, the five scenarios proposed inDe Freitaset al.(2021)were considered, with the respective visual representations included for each case (Figures 4 to 8). However, to illustrate the consistency and robustness of the proposed formulation, Figures 2 and 3 present a direct comparison between the Added Mass and Damping Coefficients obtained in the current study and the corresponding results presented byDe Freitaset al.(2021). This initial visual analysis highlights the close proximity between the curves, providing a preliminary validation of the approach under analysis before the detailed discussion of the specific scenarios.Figure 2:Added mass and damping coefficients withG=0G=0andd=0.2d=0.2.Figure 3:Added mass and damping coefficients withG=1G=1andd=0.2d=0.2.

## 4.1Case 1: Variable ImaginaryGGand Fixeddd

ConsideringGGas a purely imaginary number taking 4 distinct values and the fixed depth,d=0.1d=0.1, simulations were performed and the graphs obtained, as shown in Figure4.


Figure 4:Added mass and damping coefficients as a function ofK​aKa, ford=0.1d=0.1and imaginary values ofGG.

The results obtained through the formulation under analysis demonstrate a notable agreement with those presented byDe Freitaset al.(2021), in Figures 8 and 10. This graphical similarity, observed for the specific case whereGGis purely imaginary, suggests the validity of the proposed formulation, indicating a consistent behavior with the results previously established in the literature.

## 4.2Case 2: Variable RealGGand Fixeddd

ConsideringGGas a real number taking 4 distinct values and the fixed depth,d=0.1d=0.1, simulations were performed and the graphs obtained, as shown in Figure5.Figure 5:Added mass and damping coefficients as a function ofK​aKa, ford=0.1d=0.1and real values ofGG.

It can be noted that the graphs presented by the formulation under analysis closely approach what was presented inDe Freitaset al.(2021), Figures 9 and 11, showing that the formulation found, for the case whereGGis real, presents a compatible result.

## 4.3Case 3:G=0G=0and Variabledd

ConsideringG=0G=0and the depthddtaking three distinct values, simulations were performed and the graphs obtained, as shown in Figure6.Figure 6:Added mass and damping coefficients as a function ofK​aKa, for different values ofddandG=0G=0.

It can be noted that the graphs presented by the formulation under analysis closely approach what was presented inDe Freitaset al.(2021), Figures 2 and 3, showing that the formulation found, for the case whereG=0G=0, presents a compatible result.

## 4.4Case 4:G=1G=1and Variabledd

ConsideringG=1G=1and the depthddtaking four distinct values, simulations were performed and the graphs obtained, as shown in Figure7.


Figure 7:Added mass and damping coefficients as a function ofK​aKa, for different values ofddandG=1G=1.

It can be noted that the graphs presented by the formulation under analysis closely approach what was presented inDe Freitaset al.(2021), Figures 6 and 7, validating the research under analysis for the case whereG=1G=1.

## 4.5Case 5:G=0.7+0.3​iG=0.7+0.3iand Variabledd

ConsideringG=0.7+0.3​iG=0.7+0.3iand the depthddtaking four distinct values, simulations were performed and the graphs obtained, as shown in the image below.Figure 8:Added mass and damping coefficients as a function ofK​aKa, for different values ofddandG=0.7+0.3​iG=0.7+0.3i.

It can be noted that the graphs presented by the formulation under analysis closely approach what was presented inDe Freitaset al.(2021), Figures 4 and 5, validating the research under analysis for the case whereG=0.7+0.3​iG=0.7+0.3i.

To reinforce the good agreement between the results of this research and those ofDe Freitaset al.(2021), the Mean Absolute Error (MAE) and the Root Mean Square Error (RMSE) were used to quantify the differences between the values of the studied problem and the values fromDe Freitaset al.(2021), taking one graph (values) for each of the presented cases, as shown in Tables 3 and 4 and based onCarmo and Silva (2023).Table 3:Quantifying graphical results via RMSE and MAE.G=0.1G=0.1andd=0.1d=0.1G=0.1​iG=0.1iandd=0.1d=0.1Metric𝒜{\cal{A}}ℬ{\cal{B}}𝒜{\cal{A}}ℬ{\cal{B}}RMSE0.1370.1410.300.24MAE0.1010.0630.170.11Table 4:Quantifying graphical results via RMSE and MAE.G=0G=0andd=0.2d=0.2G=1G=1andd=0.2d=0.2G=0.7+0.3​iG=0.7+0.3iandd=0.2d=0.2Metric𝒜{\cal{A}}ℬ{\cal{B}}𝒜{\cal{A}}ℬ{\cal{B}}𝒜{\cal{A}}ℬ{\cal{B}}RMSE0.09260.09510.07410.07970.08490.0658MAE0.0560.0700.05110.06920.0470.055

## 5CONCLUSION

The results obtained throughout this research demonstrate that the sequence of simplifications proposed inFarina and Martin (1997), originally aimed at deriving a one-dimensional equation for wave interaction with a rigid circular plate, was successfully adapted to the context of porous bodies. The same analytical strategy proved effective in obtaining a streamlined one-dimensional formulation for a porous circular disk while preserving the essential mathematical structure of the original model.

As discussed in Section 4 and evidenced by Figures 2 to 8, the numerical results show strong agreement with those reported inDe Freitaset al.(2021). Such compatibility reinforces the validity of the proposed integral formulation, particularly regarding added mass and damping coefficients. For future work, it is suggested to refine the approximation techniques to circumvent numerical limitations encountered during this study, noting that the current investigation focused on small submergence depths, thus excluding thed=10d=10cases.

The analysis allowed for a deeper investigation into the influence of porosity on hydrodynamic interaction by varying the complex porous parameterGG. WhenGGassumes purely real values, it physically represents a high-resistance porous structure. Under this condition, as realGGincreases, equivalent to a decrease in resistanceffin equation (1), the disk behaves increasingly like a solid plate, hindering fluid penetration and consequently reducing added mass and damping effects, as shown in Figure 5.

Conversely, whenGGis purely imaginary, the system is dominated by the inertial effect represented by the parameterSS(see equation (1)). This implies that the fluid within the pores tends to follow the disk’s motion, acting as an effective added mass coupled to the structure. This effect is particularly relevant in near-free-surface configurations, which can induce resonance in the fluid layer above the disk. The presence of inertial-dominant porosity (GGbeing purely imaginary) can amplify this resonance, leading to significantly high peaks in both added mass and damping coefficients, as presented in Figure 4.

From a physical standpoint, the system’s response as a function ofGGreflects the balance between the resistive and inertial components of the porous flow. High values of the real part ofGGindicate a more resistant medium, leading to flow blockage and concentrated hydrodynamic forces on the structure. On the other hand, high values of the imaginary part ofGGreflect a predominantly inertial response, favoring relative flow and reducing viscous resistance.

Furthermore, it was observed that forK=0K=0, equation (28) resembles the classical Love equation, originally associated with the electrostatic problem of a capacitor with coaxial circular plates. This formulation allows for a generalization to hydrodynamic contexts and can be interpreted as a variation of the Love-Lieb equations(Farinaet al.,2022), contributing to fluid-structure interaction studies across various applied mathematical modeling scenarios.

A significant limitation concerning the numerical implementation of the governing equation was identified. In contrast to the approach inFarina and Martin (1997), the direct application of the Nyström method with Gauss-Legendre quadrature proved insufficient. The singularity inherent to equation (21) hindered the use of standard methodologies, necessitating the development of an alternative numerical strategy for integral evaluation. This difficulty in treating singularities represents a path for future research in the numerical analysis of singular integral equations.

In conclusion, the research objectives were fully met. It was possible to derive an integral formulation for porous plates following the methodology inFarina and Martin (1998). The numerical consistency validates the developed approach and provides a better understanding of the physical effects introduced by porosity on the system’s hydrodynamic response.

In the small submergence regime (d=0.1d=0.1), the analysis focuses on resonance phenomena intensified by the proximity of the free surface. The nature of the porosity parameterGGsignificantly alters the hydrodynamic response: while an increase in the imaginary component (GiG_{i}) raises added mass peaks and shifts resonance frequencies to lower values, an increase in the real component (GrG_{r}) acts dissipatively, reducing peak magnitudes. Mathematically, this regime is governed by the oscillation of the thin fluid layer above the disk, where complex porosity serves as a tuning mechanism for controlling the extreme values of incident hydrodynamic forces.

## REFERENCES
- R. Antonutti, C. Peyrard, L. Johanning, A. Incecik, and D. Ingram (2014)An investigation of the effects of wind-induced inclination on floating wind turbine dynamics: heave plate excursion.Ocean Engineering91,pp. 208–217.Cited by:§1.
- S. Astariz and G. Iglesias (2015)The economics of wave energy: a review.Renewable and Sustainable Energy Reviews45,pp. 397–408.Cited by:§1.
- C. R. S. Carmo and J. R. d. M. Silva (2023)APRENDIZADO de máquina e prestação de serviços de armazenamento de dados: métricas para análise e validação de algoritmos previsores.GETEC12.Cited by:§4.5.
- A. T. Chwang and J. Wu (1994)Wave scattering by submerged porous disk.Journal of Engineering Mechanics120.Cited by:§1,§1.
- A. T. Chwang (1983)A porous-wavemaker theory.Journal of Fluid Mechanics132,pp. 395–406.Cited by:§1.
- A. Das, S. De, and B. Mandal (2022a)Radiation and scattering of flexural-gravity waves by a submerged porous disc.Meccanica57,pp. 1557–1573.External Links:DocumentCited by:§1,§1,§4.
- A. Das, S. De, and B.N. Mandal (2022b)Radiation of water waves by a heaving submerged disc in a three-layer fluid.Journal of Fluids and Structures111,pp. 103575.External Links:ISSN 0889-9746,Document,LinkCited by:§1,§2.2.
- I. M. De Freitas, L. Farina, and J. J. H. Miller (2021)The heaving motion of a porous disc submerged in deep water.Ocean Engineering219,pp. 108–290.Cited by:§1,§1,§2.1,§4.1,§4.2,§4.3,§4.4,§4.5,§4.5,§4,§4,§5.
- J. Dokken, J. Grue, and L.P. Karstensen (2017)Wave analysis of porous geometry with linear resistance law.Journal of Marine Science and Application16,pp. 480–489.Cited by:§1.
- J. Falnes (2002)Ocean waves and oscillating systems: linear interactions including wave-energy extraction.Cambridge University Press.External Links:DocumentCited by:§3.
- K. Fang, Y. Wang, and P. M. Bentler (1994)Some applications of number-theoretic methods in statistics.Statistical Science9(3),pp. 416–428.External Links:ISSN 08834237,LinkCited by:§3.
- L. Farina (2012)Ondas oceânicas de superfície.2th edition,SBMAC.Cited by:§1,§2.1.
- L. Farina, R. L. da Gama, S. Korotov, and J. S. Ziebell (2017)Radiation of water waves by a submerged nearly circular plate.Journal of Computational and Applied Mathematics310,pp. 165–173.Note:Numerical Algorithms for Scientific and Engineering ApplicationsExternal Links:ISSN 0377-0427,Document,LinkCited by:§1.
- L. Farina, G. Lang, and P. Martin (2022)Love–Lieb integral equations: applications, theory, approximations, and computations.SIAM Review64(4),pp. 831–865.Cited by:§2.3,§5.
- L. Farina and P. A. Martin (1997)Radiation of water waves by a heaving submerged horizontal disc.Journal of Fluid Mechanics337,pp. 365–379.Cited by:§1,§2.2,§2.2,§5,§5.
- L. Farina and P. A. Martin (1998)Scattering of water waves by a submerged disc using a hipersingular integral equation.Applied Ocean Research20,pp. 121–134.Cited by:§5.
- L. Farina (2001)Evaluation of single layer potentials over curved surfaces.SIAM Journal on Scientific Computing23(1),pp. 81–91.Cited by:§3.
- C. J. R. Garrett (1971)Wave forces on a circular dock.Journal of Fluid Mechanics46(1),pp. 12–139.External Links:DocumentCited by:§1.
- R. Gayen and A. Mondal (2014)A hypersingular integral equation approach to the porous plate problem.Applied Ocean Research46,pp. 70–78.Cited by:§1.
- R. Gayen and A. Mondal (2016)Water wave interaction with two symmetric inclined permeable plates.Ocean Engineering124,pp. 180–191.Cited by:§1.
- R. W. Guidera (1975)Penny-shaped cracks.Journal of Elasticity5,pp. 59–73.External Links:DocumentCited by:§2.2.
- N. Islam, S. Kundu, and R. Gayen (2019)Scattering and radiation of water waves by a submerged rigid disc in a two-layer fluid.Proceedings of The Royal Society A Mathematical Physical and Engineering Sciences475,pp. 20190331.External Links:DocumentCited by:§1.
- S. Koley, R. Mondal, and T. Sahoo (2018)Fredholm integral equation technique for hydroelastic analysis of a floating flexible porous plate.European Journal of Mechanics/B Fluids67,pp. 291–305.Cited by:§1.
- M. Lamas-Pardo, G. Iglesias, and L. Carral (2015)A review of very large floating structures (vlfs) for coastal and offshore uses.Ocean Engineering109,pp. 677–690.Cited by:§1.
- Y. Liu, H. Li, Y. Li, and S. He (2011)A new approximate analytic solution for water wave scattering by a submerged horizontal porous disk.Applied Ocean Research67,pp. 286–296.Cited by:§1.
- C. Lopez-Pavon and A. Souto-Iglesias (2015)Hydrodynamic coefficients and pressure loads on heave plates for semi-submersible floating offshore wind turbines: a comparative analysis using large scale models.Renewable Energy81,pp. 864–881.Cited by:§1.
- E.B.L. Mackay, A. Feichtner, R.E. Smith, P.R. Thies, and L. Johanning (2019)Verification of a boundary element model for wave forces on structures with porous elements.Advances in Renewable Energies Offshore - Proceedings of the 3rd International Conference on Renewable Energies Offshore,pp. 341–350.Cited by:§1.
- P. Martin, N. Parsons, and L. Farina (1997)Interaction of water waves with thin plates.International Series on Advances in Fluid Mechanics8,pp. 197–230.Cited by:§1.
- B. Molin and F.G. Nielsen (2004)Heave added mass and damping of a perforated disk below the free surface.Proceedings of the 19th International Workshop on Water Waves and Floating Bodies.Cited by:§1.
- J. N. Newman (1977)Marine hydrodynamics.Springer Briefs in Mathematics,The MIT Press.External Links:ISBN 9780262280617,DocumentCited by:§2.1.
- C. Ouled Housseine (2019)On wave diffraction-radiation by bodies with porous thin plates.Presented at 34th International Workshop on Water Waves and Floating Bodies.Cited by:§1.
- N.F. Parsons and P.A. Martin (1992)Scattering of water waves by submerged plates using hypersingular integral equations.Applied Ocean Research14(5),pp. 313–321.External Links:ISSN 0141-1187,Document,LinkCited by:§1.
- N.F. Parsons and P.A. Martin (1994)Scattering of water waves by submerged curved plates and by surface-piercing flat plates.Applied Ocean Research16(3),pp. 129–139.External Links:ISSN 0141-1187,Document,LinkCited by:§1.
- N. F. Parsons and P. A. Martin (1995)Trapping of water waves by submerged plates using hypersingular integral equations.Journal of Fluid Mechanics284,pp. 359–375.External Links:DocumentCited by:§1.
- C.K. Sollitt and R.H. Cross (1972)Wave transmission through permeable breakwaters.Coastal Engineering Proceedings1(13),pp. p.99.Cited by:§1.
- The Numerical Algorithms Group (n.d)D01GCF: one-dimensional quadrature (general-purpose integrator).The Numerical Algorithms Group.Note:NAG Library ManualExternal Links:LinkCited by:§3.
- X. Yu and A.T. Chwang (1994a)Wave-induced oscillation in harbor with porous breakwaters.Journal of Waterway, Port, Coastal, and Ocean Engineering120(2),pp. 125–144.Cited by:§1,§1.
- X. Yu (1995)Diffraction of water waves by porous breakwaters.Journal of Waterway, Port, Coastal, and Ocean Engineering121(6),pp. 275–282.Cited by:§1.
- X. Yu and A. T. Chwang (1994b)Water waves above submerged porous plate.Journal of Engineering Mechanics120(6),pp. 1270 – 1282.Note:Cited by: 116External Links:DocumentCited by:§1.
- Y. S. Yu and F. Ursell (1961)Surface waves generated by an oscillating circular cylinder on water of finite depth: theory and experiment.Journal of Fluid Mechanics11(4),pp. 529–551.External Links:DocumentCited by:§2.2.
- J. S. Ziebell and L. Farina (2012)Water wave radiation by a submerged rough disc.Wave Motion49(1),pp. 34–49.External Links:ISSN 0165-2125,Document,LinkCited by:§1.

## 


- 


Major funding support from
