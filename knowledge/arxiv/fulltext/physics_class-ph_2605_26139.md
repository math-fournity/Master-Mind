# On radiation from hyperbolic motion, behavior of electromagnetic fields, and coordinate transformations at infinity

**arXiv ID**: 2605.26139v1
**Authors**: E. T. Akhmedov, M. N. Milovanova
**Published**: 2026-05-22
**Categories**: physics.class-ph, gr-qc, hep-th
**Comments**: 6 pages, 1 figure
**HTML URL**: https://arxiv.org/html/2605.26139v1

## Abstract

We show explicitly that radiation from a uniformly accelerating charge escapes outside Rindler wedge, while within Rindler wedge there is no flux through infinity, neither in the Minkowski frame nor in the Rindler frame. This remains true despite the fact that the coordinate transformation between the Rindler and Minkowski frames is not trivial at infinity.

## Full Text

On radiation from hyperbolic motion, behavior of electromagnetic fields, and coordinate transformations at infinity

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- License: CC BY 4.0arXiv:2605.26139v1 [physics.class-ph] 22 May 2026

## On radiation from hyperbolic motion, behavior of electromagnetic fields, and coordinate transformations at infinityE. T. AkhmedovInstitutskii per, 9, Moscow Institute of Physics and Technology, 141700, Dolgoprudny, RussiaAcademician Kurchatov Square, 1, NRC ”Kurchatov Institute”, 123182, Moscow, RussiaM. N. MilovanovaInstitutskii per, 9, Moscow Institute of Physics and Technology, 141700, Dolgoprudny, Russia

## Abstract

We show explicitly that radiation from a uniformly accelerating charge escapes outside Rindler wedge, while within Rindler wedge there is no flux through infinity, neither in the Minkowski frame nor in the Rindler frame. This remains true despite the fact that the coordinate transformation between the Rindler and Minkowski frames is not trivial at infinity.

1.The problem of radiation from a uniformly accelerating charge has a long history, dating back to the early works of Max Born[1]and continuing through numerous investigations in classical and quantum field theory (see, e.g.,[2],[3],[4]and[5]). A particularly intriguing aspect of this problem is the apparent tension between descriptions of the same physical system in different coordinate frames: while in Minkowski coordinates the field of a uniformly accelerating charge possesses a radiative component, in Rindler coordinates the field appears static and does not radiate. This observation is closely related to the presence of the Rindler horizon and has been widely discussed in the literature (see, for example,[6],[7],[8]).

In our previous work[9]we revisited this problem and demonstrated explicitly that in Rindler coordinates a uniformly accelerating charge does not radiate, since this region constitutes a static zone for the source. In contrast, in Minkowski coordinates there exists a wave zone in which the same charge exhibits radiative behavior. This apparent discrepancy calls for a more detailed and quantitative comparison of the two descriptions, which we undertake in the present work.

A key geometric feature underlying this difference is that the Rindler metric cannot be globally represented as a pullback of the Minkowski metric by a smooth, non-degenerate coordinate transformation. Although locally the two metrics are related by a coordinate change, the corresponding Jacobian becomes singular at the Rindler horizon. As a consequence, the mapping between the two coordinate systems is not globally invertible, and a portion of the electromagnetic field effectively propagates beyond the Rindler horizon, remaining inaccessible to non-inertial co-accelerating observers. This feature is intimately connected with the well-known causal structure of Rindler coordinates and the role of horizons in field theory (cf.[6],[10]).

The same geometric subtlety manifests itself in the analysis of the asymptotic behavior of the fields. In particular, the asymptotics obtained directly in Minkowski coordinates may, in principle, differ from those reconstructed via Rindler coordinates using the Jacobian transformation. This is because the transformation becomes singular in the relevant limits, and therefore the operations of taking asymptotics and performing coordinate transformations do not necessarily commute. Closely related issues arise in the general theory of the asymptotic structure of fields in spacetime, as developed in the seminal works[11]and[12], where the behavior of fields at infinity is known to be sensitive to the choice of coordinates and conformal compactification.

The purpose of the present paper is to clarify these issues in the specific context of electromagnetic fields produced by a uniformly accelerating charge. We perform a detailed comparison between two procedures for obtaining asymptotic behavior: (i) a direct analysis in Minkowski coordinates, and (ii) an indirect approach based on asymptotics in Rindler coordinates followed by a transformation using the Jacobian matrix.

2.We consider Maxwell’s equations in curvilinear coordinates,1−g​∂μ(−g​Fμ​ν)=4​π​jν,\displaystyle\frac{1}{\sqrt{-g}}\partial_{\mu}\left(\sqrt{-g}\,F^{\mu\nu}\right)=4\pi j^{\nu},(1)

wheregμ​νg_{\mu\nu}is the metric tensor,g=detgμ​νg=\det g_{\mu\nu},Fμ​ν=∂μAν−∂νAμF^{\mu\nu}=\partial^{\mu}A^{\nu}-\partial^{\nu}A^{\mu}is the electromagnetic field tensor,AμA_{\mu}is the four-potential, andjνj^{\nu}is the current density. This current is due to a uniformly accelerated charge with constant proper accelerationaa, moving along the worldlinezμ​(θ)=(1a​sinh⁡(a​θ),1a​cosh⁡(a​θ),0,0),\displaystyle z^{\mu}(\theta)=\left(\frac{1}{a}\sinh(a\theta),\frac{1}{a}\cosh(a\theta),0,0\right),(2)

whereθ\thetais the proper time.

We consider these equations in two coordinate systems covering flat spacetime: Minkowski coordinates,d​s2=d​t2−d​x2−d​y2−d​z2,\displaystyle ds^{2}=dt^{2}-dx^{2}-dy^{2}-dz^{2},(3)

and Rindler coordinates,d​s2=ρ2​d​τ2−d​ρ2−d​y2−d​z2,\displaystyle ds^{2}=\rho^{2}d\tau^{2}-d\rho^{2}-dy^{2}-dz^{2},(4)

which cover only the Rindler wedge|t|<x|t|<xof the entire flat spacetime, providedρ≥0\rho\geq 0.

The coordinate transformation between these systems,t=ρ​sinh⁡τ,x=ρ​cosh⁡τ,\displaystyle t=\rho\sinh\tau,\qquad x=\rho\cosh\tau,(5)

(withyyandzzunchanged) does not reduce to a trivial transformation at infinities (t→±∞t\to\pm\infty,x→±∞x\to\pm\infty) and, thus, is not quite a proper gauge transformation. Such a transformation can modify the asymptotic behavior of the fields and, consequently, the associated stress–energy flux at infinity. The purpose of this work is to analyze this possibility in detail and to clarify in what sense the homogeneously accelerating charge does create electromagnetic radiation, whereas in the Rindler wedge the radiation is absent[2,13,9].

To analyze this situation, one must first identify the relevant asymptotic regions. In both descriptions, the electromagnetic field is nonvanishing only at spacetime points satisfying the matching (retardation) condition, which enforces a lightlike separation between the emission and observation points. In Minkowski coordinates, this condition takes the form(t−sinh⁡(a​θ)a)2=(x−cosh⁡(a​θ)a)2+y2+z2.\displaystyle\left(t-\frac{\sinh(a\theta)}{a}\right)^{2}=\left(x-\frac{\cosh(a\theta)}{a}\right)^{2}+y^{2}+z^{2}.(6)

Hereθ\thetais the proper time of emission and(t,x,y,z)(t,x,y,z)is the observation point. We set the speed of light to one. Applying the transformation (5), one obtains the corresponding relation in Rindler coordinates:cosh⁡(τ−a​θ)=a2​ρ​(ρ2+y2+z2+a−2),\displaystyle\cosh(\tau-a\theta)=\frac{a}{2\rho}\left(\rho^{2}+y^{2}+z^{2}+a^{-2}\right),(7)

where(τ,ρ,y,z)(\tau,\rho,y,z)is the observation point within the Rindler wedge.

3.Analysis of these relations within the Rindler wedge reveals two distinct asymptotic regimes. In Rindler coordinates, forτ→±∞\tau\to\pm\infty,
- R1.

ρ≈e±(τ−a​θ)​(1−1+a2​(y2+z2)​e±2​a​θe±2​τ),y,z≪ρ,\rho\approx e^{\pm(\tau-a\theta)}\left(1-\frac{1+a^{2}(y^{2}+z^{2})e^{\pm 2a\theta}}{e^{\pm 2\tau}}\right),\quad y,z\ll\rho,
- R2.

y2+z2≈a−1​ρ​e±(τ−a​θ)​(12±sinh⁡(a​θ)​e±a​θe±2​τ),ρ2≪y2+z2,ρ↛0.y^{2}+z^{2}\approx a^{-1}\rho e^{\pm(\tau-a\theta)}\left(\frac{1}{2}\pm\frac{\sinh(a\theta)e^{\pm a\theta}}{e^{\pm 2\tau}}\right),\quad\rho^{2}\ll y^{2}+z^{2},\quad\rho\not\to 0.

The corresponding regimes in Minkowski coordinates, fort→±∞t\to\pm\infty, are
- M1.

t≈±x∓a−1​e∓a​θt\approx\pm x\mp a^{-1}e^{\mp a\theta},y2+z2≪a−1​x,y^{2}+z^{2}\ll a^{-1}x,
- M2.

t≈±x∓a−1​e∓a​θ±y2+z2xt\approx\pm x\mp a^{-1}e^{\mp a\theta}\pm\frac{y^{2}+z^{2}}{x},y2+z2∼a−1​x.y^{2}+z^{2}\sim a^{-1}x.

These limits are in one-to-one correspondence:R1withM1, andR2withM2. Note that both sets of events(τ,ρ,y,z)(\tau,\rho,y,z)and(t,x,y,z)(t,x,y,z)lie in the same Rindler wedge.

We now illustrate the comparison using the first regime,R1andM1, which corresponds to the right future lightlike infinity𝒥+\mathcal{J}^{+}on the Penrose diagram, with small values of the transverse coordinatesyyandzz(see Fig.1). The second regime,R2andM2, corresponds instead to the asymptotic region characterized by large transverse coordinatesyyandzz.Figure 1:The Penrose diagram of Minkowski spacetime illustrating the asymptotic regions M1 and M3, together with the worldline of the charge, provides a useful geometric interpretation. The wavy lines represent tentative electromagnetic radiation propagating along the future light cone, extending into regions that lie beyond the Rindler wedge.

In Rindler coordinates, the magnetic field vanishes, while the electric field is nonzero[9],[13]:E→R=1ρ​sinh3⁡(τ−a​θ)​(a​ρ−cosh⁡(τ−a​θ)a​ya​z),B→R=0.\displaystyle\vec{E}^{R}=\frac{1}{\rho\sinh^{3}(\tau-a\theta)}\begin{pmatrix}a\rho-\cosh(\tau-a\theta)\\
ay\\
az\end{pmatrix},\quad\vec{B}^{R}=0.(8)

Here the superscriptRRmeans that the fields are defined in the Rindler corrdinates.
In the regimeR1, corresponding toρ→∞\rho\to\infty, the leading asymptotics areE→R≃±4​a​e∓3​(τ−a​θ)​(12​a​y​e∓(τ−a​θ)2​a​z​e∓(τ−a​θ)),B→R=0.\displaystyle\vec{E}^{R}\simeq\pm 4ae^{\mp 3(\tau-a\theta)}\begin{pmatrix}1\\
2aye^{\mp(\tau-a\theta)}\\
2aze^{\mp(\tau-a\theta)}\end{pmatrix},\quad\vec{B}^{R}=0.(9)

The transformation of the electromagnetic tensor between the two coordinate systems is given byFμ​νM=Jμσ​Fσ​ρR​Jνρ,\displaystyle F_{\mu\nu}^{M}=J^{\sigma}_{\mu}F_{\sigma\rho}^{R}J^{\rho}_{\nu},(10)

with the Jacobian equal toJνμ=(cosh⁡(τ)ρ−sinh⁡(τ)ρ00−sinh⁡(τ)cosh⁡(τ)0000100001),\displaystyle J^{\mu}_{\nu}=\begin{pmatrix}\frac{\cosh(\tau)}{\rho}&\frac{-\sinh(\tau)}{\rho}&0&0\\
-\sinh(\tau)&\cosh(\tau)&0&0\\
0&0&1&0\\
0&0&0&1\end{pmatrix},(11)

for the two frames under consideration.

In the limitR1, the Jacobian behaves asymptotically asJνμ≃(a​e±a​θ2​(1+1+a2​(y2+z2)​e±2​a​θe±2​τ)∓a​e±a​θ2​(1+−1+a2​(y2+z2)​e±2​a​θe±2​τ)00∓(e±τ2−e∓τ)e±τ0000100001).\displaystyle J^{\mu}_{\nu}\simeq\begin{pmatrix}\frac{ae^{\pm a\theta}}{2}\left(1+\frac{1+a^{2}(y^{2}+z^{2})e^{\pm 2a\theta}}{e^{\pm 2\tau}}\right)&\mp\frac{ae^{\pm a\theta}}{2}\left(1+\frac{-1+a^{2}(y^{2}+z^{2})e^{\pm 2a\theta}}{e^{\pm 2\tau}}\right)&0&0\\
\mp\left(\frac{e^{\pm\tau}}{2}-e^{\mp\tau}\right)&e^{\pm\tau}&0&0\\
0&0&1&0\\
0&0&0&1\end{pmatrix}.(12)

Combining Eqs. (9)–(12), one findsE→M≃±4​a2​e∓4​(τ−a​θ)​(1a​y​e±a​θa​z​e±a​θ),B→M≃4​a2​e∓4​(τ−a​θ)​(0−a​z​e±a​θa​y​e±a​θ).\displaystyle\vec{E}^{M}\simeq\pm 4a^{2}e^{\mp 4(\tau-a\theta)}\begin{pmatrix}1\\
aye^{\pm a\theta}\\
aze^{\pm a\theta}\end{pmatrix},\quad\vec{B}^{M}\simeq 4a^{2}e^{\mp 4(\tau-a\theta)}\begin{pmatrix}0\\
-aze^{\pm a\theta}\\
aye^{\pm a\theta}\end{pmatrix}.(13)

Here the superscriptMMmeans that the fields are defined in the Minkowski corrdinates.

Thus, one obtains a nonvanishing magnetic field. Furthermore,
after using the matching relatione±τ≈a​ρ​e±a​θe^{\pm\tau}\approx a\rho e^{\pm a\theta}valid in this limit and subsequently expressing the result in Minkowski coordinates, one recovers the same asymptotic expressions. Indeed, the electric and magnetic fields in Minkowski coordinates are given by[9],[13]:E→M\displaystyle\vec{E}^{M}=1(t​cosh⁡(a​θ)−x​sinh⁡(a​θ))3​(a​(x2−t2)−x​cosh⁡(a​θ)+t​sinh⁡(a​θ)a​x​ya​x​z),\displaystyle=\frac{1}{(t\cosh(a\theta)-x\sinh(a\theta))^{3}}\begin{pmatrix}a(x^{2}-t^{2})-x\cosh(a\theta)+t\sinh(a\theta)\\
axy\\
axz\end{pmatrix},(14)B→M\displaystyle\vec{B}^{M}=1(t​cosh⁡(a​θ)−x​sinh⁡(a​θ))3​(0−a​t​za​t​y).\displaystyle=\frac{1}{(t\cosh(a\theta)-x\sinh(a\theta))^{3}}\begin{pmatrix}0\\
-atz\\
aty\end{pmatrix}.

In the limitM1, their asymptotic form isE→M\displaystyle\vec{E}^{M}≃±e±2​a​θx2​(1a​y​e±a​θa​z​e±a​θ),B→M≃e±2​a​θx2​(0−a​z​e±a​θa​y​e±a​θ).\displaystyle\simeq\pm\frac{e^{\pm 2a\theta}}{x^{2}}\begin{pmatrix}1\\
aye^{\pm a\theta}\\
aze^{\pm a\theta}\end{pmatrix},\qquad\vec{B}^{M}\simeq\frac{e^{\pm 2a\theta}}{x^{2}}\begin{pmatrix}0\\
-aze^{\pm a\theta}\\
aye^{\pm a\theta}\end{pmatrix}.(15)

Note that these fields decay too rapidly at infinity, namely as1/x21/x^{2}. As a consequence, the flux through future lightlike infinity𝒥+\mathcal{J}^{+}within the Rindler wedge (see Fig.1), where the fields are simultaneously described in both coordinate systems, vanishes. Therefore, no radiation is produced within the Rindler wedge, neither in Rindler nor in Minkowski coordinates.

4.We now demonstrate that radiation is indeed present and is emitted into the region beyond the Rindler wedge. This becomes manifest when the problem is analyzed in Minkowski coordinates using the corresponding expressions for the electromagnetic fields. The crucial point is that the expressions (14) remain valid not only inside the Rindler wedge, but also in the complementary regions of Minkowski spacetime lying beyond it.

The asymptotic regime in Minkowski spacetime outside the Rindler wedge, corresponding to the regionx<tx<t, can be parameterized as
- M3.

t≈±x2+y2+z2+a−1​sinh⁡(a​θ)∓2​a−1​x​cosh⁡(a​θ)x2+y2+z2t\approx\pm\sqrt{x^{2}+y^{2}+z^{2}}+a^{-1}\sinh(a\theta)\mp\frac{2a^{-1}x\cosh(a\theta)}{\sqrt{x^{2}+y^{2}+z^{2}}}.

In this regime, the leading asymptotic behavior of the electromagnetic fields can likewise be obtained from Eq. (14) together with the matching condition (6) in the limitt→∞t\to\infty, now evaluated in the region beyond the Rindler wedge:E→M\displaystyle\vec{E}^{M}≃1(x2+y2+z2​cosh⁡(a​θ)−x​sinh⁡(a​θ))3​(−a​(y2+z2)+3​x​cosh⁡(a​θ)−x2+y2+z2​sinh⁡(a​θ)a​x​ya​x​z),\displaystyle\simeq\frac{1}{\left(\sqrt{x^{2}+y^{2}+z^{2}}\cosh(a\theta)-x\sinh(a\theta)\right)^{3}}\begin{pmatrix}-a(y^{2}+z^{2})+3x\cosh(a\theta)-\sqrt{x^{2}+y^{2}+z^{2}}\sinh(a\theta)\\
axy\\
axz\end{pmatrix},(16)B→M\displaystyle\vec{B}^{M}≃x2+y2+z2(x2+y2+z2​cosh⁡(a​θ)−x​sinh⁡(a​θ))3​(0−a​za​y).\displaystyle\simeq\frac{\sqrt{x^{2}+y^{2}+z^{2}}}{\left(\sqrt{x^{2}+y^{2}+z^{2}}\cosh(a\theta)-x\sinh(a\theta)\right)^{3}}\begin{pmatrix}0\\
-az\\
ay\end{pmatrix}.

To determine whether the charge radiates into this asymptotic region, we compute the flux of electromagnetic energy through a sphere at infinity, denoted byΩ\Omega. Lett=Rt=R, and parametrize the observation point asx=R​cos⁡(ϕ),y=R​sin⁡(ϕ)​cos⁡(χ),z=R​sin⁡(ϕ)​sin⁡(χ)x=R\cos(\phi),y=R\sin(\phi)\cos(\chi),z=R\sin(\phi)\sin(\chi)withR→+∞R\to+\infty. The corresponding unit normal vector isn→=(cos⁡(ϕ),sin⁡(ϕ)​cos⁡(χ),sin⁡(ϕ)​sin⁡(χ))\vec{n}=(\cos(\phi),\sin(\phi)\cos(\chi),\sin(\phi)\sin(\chi)). The energy flux per unit solid angle at infinity is then given byd​Id​Ω=(S→,n→)​R2≈a2​(y2+z2)​(x2+y2+z2)2(x2+y2+z2​cosh⁡(a​θ)−x​sinh⁡(a​θ))6=a2​sin2⁡(ϕ)(cosh⁡(a​θ)−cos⁡(ϕ)​sinh⁡(a​θ))6.\displaystyle\frac{dI}{d\Omega}=\left(\vec{S},\vec{n}\right)R^{2}\approx\frac{a^{2}\left(y^{2}+z^{2}\right)\left(x^{2}+y^{2}+z^{2}\right)^{2}}{\left(\sqrt{x^{2}+y^{2}+z^{2}}\cosh(a\theta)-x\sinh(a\theta)\right)^{6}}=\frac{a^{2}\sin^{2}(\phi)}{\left(\cosh(a\theta)-\cos(\phi)\sinh(a\theta)\right)^{6}}.(17)

Integrating this expression over the angular variablesϕ\phiandχ\chi, one obtains a nonvanishing total energy flux. This demonstrates that the homogeneously accelerating charge does radiate; however, the radiation propagates into the asymptotic region lying beyond the Rindler wedge.

Acknowledgments.This work was supported by grant No. 26-12-00330 from the Russian Science Foundation (RSF).

## References
- [1]M. Born, Annalen Phys.30, 840 (1909) doi:10.1002/andp.19093351102.
- [2]W. Pauli, Theory Relativity, Pergamon Press (1958).
- [3]T. Fulton and F. Rohrlich,
Classical radiation from a uniformly accelerated charge,
Annals of Physics9, Issue 4,
499-517 (1960)
doi:10.1016/0003-4916(60)90105-6.
- [4]R. Peierls, Surprises in Theoretical Physics, Princeton University Press (1979)
doi:10.1515/9780691217888.
- [5]D. Boulware,
Annals of Physics124, Issue 1, 169 (1980).
doi:10.1016/0003-4916(80)90360-7.
- [6]W. G. Unruh,
Phys. Rev. D14, 870 (1976)
doi:10.1103/PhysRevD.14.870
- [7]R. Wald, General Relativity, Chicago Univ. Pr. (1984)
doi:10.7208/chicago/9780226870373.001.0001.
- [8]S. Weinberg, Gravitation and Cosmology, John Wiley and Sons, Inc. (1972)
ISBN 978-0-471-92567-5.
- [9]E. T. Akhmedov and M. Milovanova,
Phys. Rev. D111, no.12, 124047 (2025)
doi:10.1103/4lvr-ssjh
[arXiv:2503.00064 [physics.class-ph]].
- [10]S. Fulling,
Phys. Rev. D7, 2850 (1973)
doi:10.1103/PhysRevD.7.2850.
- [11]R. Penrose,
Phys. Rev. Lett.10, 66 (1963)
doi:10.1103/PhysRevLett.10.66.
- [12]H. Bondi, M. van der Burg, A. Metzner,
Proc. Roy. Soc. Lond. A269, 21-52 (1962)
doi:10.1098/rspa.1962.0161.
- [13]D. Kalinov,
Phys. Rev. D92, no.8, 084048 (2015)
doi:10.1103/PhysRevD.92.084048
[arXiv:1508.04281 [hep-th]].

## 


- 


Major funding support from
