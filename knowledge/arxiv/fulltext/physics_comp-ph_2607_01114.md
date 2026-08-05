# Lanczos Method for QRPA Strength Functions in Atomic Nuclei

**arXiv ID**: 2607.01114v1
**Authors**: Dong Min Roh, Chao Yang, Jonathan Engel, Matthew L. Dai
**Published**: 2026-07-01
**Categories**: physics.comp-ph, math-ph, math.NA
**HTML URL**: https://arxiv.org/html/2607.01114v1

## Abstract

We present a symmetric Lanczos method for computing charge-changing QRPA strength functions in atomic nuclei. Starting from the finite-amplitude-method formulation of the QRPA linear-response problem, we derive equivalent spectral representations and, in the real case, a reduced eigenvalue problem involving the matrix products $MK$ and $KM$, where $M\equiv A+B$ and $K\equiv A-B$ are formed from the usual QRPA matrices $A$ and $B$. The resulting formulation enables a matrix-free Lanczos approximation of the Lorentzian-smeared strength function over a broad energy interval from a single Krylov run, in contrast to conventional frequency-by-frequency response calculations. Numerical tests for $^{112}$Sn and $^{150}$Nd first show that GMRES reproduces the converged iterative FAM strength profiles while requiring fewer iterations. Using GMRES as the frequency-by-frequency reference, we then show that the Lanczos approximation reproduces the same strength profiles with reduced overall cost. These results indicate that symmetric Lanczos projection provides an efficient and accurate approach for QRPA strength-function calculations when spectral information is required over an extended frequency range.

## Full Text

Lanczos Method for QRPA Strength Functions in Atomic Nuclei

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
- License: CC BY 4.0arXiv:2607.01114v1 [physics.comp-ph] 01 Jul 2026

## Lanczos Method for QRPA Strength Functions in Atomic NucleiDong Min RohComputational Research Division, Lawrence Berkeley National Laboratory, Berkeley, California 94720, United StatesMatthew L. DaiDepartment of Physics and Astronomy, University of North Carolina, Chapel Hill, NC 27599-3255, United StatesJonathan Engel22footnotemark:2Chao Yang11footnotemark:1(June 2026)

## Abstract

We present a symmetric Lanczos method for computing charge-changing QRPA strength functions in atomic nuclei. Starting from the finite-amplitude-method formulation of the QRPA linear-response problem, we derive equivalent spectral representations and, in the real case, a reduced eigenvalue problem involving the matrix productsM​KMKandK​MKM, whereM≡A+BM\equiv A+BandK≡A−BK\equiv A-Bare formed from the usual QRPA matricesAAandBB. The resulting formulation enables a matrix-free Lanczos approximation of the Lorentzian-smeared strength function over a broad energy interval from a single Krylov run, in contrast to conventional frequency-by-frequency response calculations. Numerical tests for112Sn and150Nd first show that GMRES reproduces the converged iterative FAM strength profiles while requiring fewer iterations. Using GMRES as the frequency-by-frequency reference, we then show that the Lanczos approximation reproduces the same strength profiles with reduced overall cost. These results indicate that symmetric Lanczos projection provides an efficient and accurate approach for QRPA strength-function calculations when spectral information is required over an extended frequency range.

## 1Introduction

Charge-changing nuclear response functions are important in nuclear-structure and weak-interaction phenomenology.
They
enter the description ofβ\betadecay and double-β\betadecay, and provide information about collective excitations and weak rates in nuclei across the chart of nuclides[16,7].
For medium-mass and heavy open-shell nuclei, especially in deformed systems, the quasiparticle random-phase approximation (QRPA) built on nuclear energy-density functionals provides a practical microscopic framework for describing such excitations and transition strengths[16,14].

In principle, QRPA strength functions can be obtained from the explicit QRPA matrix or from a full eigendecomposition of the linear-response problem.
In practice, however, the matrix dimension grows rapidly with the size of the quasiparticle space, and explicit construction becomes prohibitively expensive for heavy and deformed nuclei.
The finite amplitude method (FAM) addresses this difficulty by computing the QRPA response through induced fields, without assembling the full QRPA matrix explicitly[13,1].
The FAM has become an effective tool for self-consistent linear-response calculations, including applications to superfluid and deformed nuclei and, in particular, to charge-changing transitions in axially deformed systems[8,12,15].

Despite their usefulness, conventional FAM-based calculations still proceed one frequency at a time. For each complex frequency on the chosen contour, one must solve a new linear system.
This feature is well suited to pointwise evaluation of the response, but it can become costly when the goal is to reconstruct the strength function over a broad energy interval.
That observation motivates Krylov-based approaches that capture spectral information more globally.
These have appeared in iterative Arnoldi methods for strength functions, in spectral-density approximation techniques, and in recent polynomial and kernel-based approaches to QRPA response problems[19,10,5,3,4].

In this paper, we develop a symmetric Lanczos framework for approximating charge-changing QRPA strength functions.
Starting from the FAM linear-response equation, we derive equivalent spectral formulations and a reduced eigenvalue problem involving the matricesM​KMKandK​MKM.
These reformulations make it possible to apply a symmetric Lanczos process with respect to the appropriate inner product and to approximate the smeared strength function over a wide frequency interval from a single Krylov run, rather than from separate solves at each frequency.
Our goal is to retain the main efficiency advantages of FAM-style matrix-free calculations while exploiting the broader spectral information available through Lanczos projection.

The paper is organized as follows.
Section2develops the QRPA formulations of the strength function, including the eigendecomposition-based and reduced-eigenproblem representations.
Section3presents the frequency-by-frequency solvers and the symmetric Lanczos approximation.
Section4reports numerical results for112Sn and150Nd, together with runtime comparisons.

## Notation.

Throughout the paper, matrices and vectors may be real or complex, depending on the formulation under consideration.
For a matrixA∈ℂm×nA\in\mathbb{C}^{m\times n}, we writeA†A^{\dagger}for the Hermitian conjugate,ATA^{T}for the transpose, andA∗A^{*}for the element-wise complex conjugate.
The identity matrix is denoted byII, with its size understood from context.
When block matrices are used, their dimensions are likewise determined by the surrounding equations.
We reserveω\omegafor the physical excitation energy and writeωγ=ω+i​γ\omega_{\gamma}=\omega+i\gammawhen a finite Lorentzian smearing widthγ>0\gamma>0is introduced.
Unless stated otherwise, vectors are written as columns, and the Euclidean inner product is understood by default; when the analysis requires a different metric, such as theKK-inner product used in the Lanczos formulation, we say so explicitly.

## 2QRPA Formulation of the Strength Function

This section summarizes the QRPA equations and spectral reformulations that underlie the strength-function calculations developed later. Although the derivation passes through the linear response equation and the response function, the quantity of interest throughout is the charge-changing QRPA strength function. The iterative and Lanczos-based algorithms used to evaluate it are deferred to Section3.

## 2.1The FAM Equations and the Strength Function

The nuclear linear response, a function of frequencyω\omega, is genrated by a weak external time-dependent fieldF^​(t)\hat{F}(t)of the formF^​(t)=η​(F^​(ω)​e−i​ω​t+F^†​(ω)​ei​ω​t),\hat{F}(t)=\eta\left(\hat{F}(\omega)e^{-i\omega t}+\hat{F}^{\dagger}(\omega)e^{i\omega t}\right)\,,(1)

whereη\etais a small real parameter.
Neglecting two-quasiparticle operators that do not contribute to the QRPA, the field can be written in the quasiparticle basis asF^​(ω)=12​∑μ​ν(Fμ​ν20​(ω)​α^μ†​α^ν†+Fμ​ν02​(ω)​α^μ​α^ν),\hat{F}(\omega)=\frac{1}{2}\sum_{\mu\nu}\left(F_{\mu\nu}^{20}(\omega)\hat{\alpha}_{\mu}^{\dagger}\hat{\alpha}_{\nu}^{\dagger}+F_{\mu\nu}^{02}(\omega)\hat{\alpha}_{\mu}\hat{\alpha}_{\nu}\right),(2)

whereFμ​ν20​(ω)F_{\mu\nu}^{20}(\omega)andFμ​ν02​(ω)F_{\mu\nu}^{02}(\omega)are defined, e.g., in Ref.[16], andα^μ†\hat{\alpha}_{\mu}^{\dagger}andα^μ\hat{\alpha}_{\mu}are quasiparticle creation and annihilation operators, respectively.
For charge-changing applications of the finite-amplitude method in deformed nuclei, we refer in particular to[1,12,8].

In the QRPA, the time evolution of the quasiparticle operators under the external fieldF^​(t)\hat{F}(t)is governed by the time-dependent Hartree–Fock–Bogoliubov (TDHFB) equation:i​∂tα^μ​(t)=[H^​(t)+F^​(t),α^μ​(t)],i\partial_{t}\hat{\alpha}_{\mu}(t)=\left[\hat{H}(t)+\hat{F}(t),\hat{\alpha}_{\mu}(t)\right],(3)

where the quasiparticle operators acquire small-amplitude oscillations of the formα^μ​(t)\displaystyle\hat{\alpha}_{\mu}(t)=(α^μ+δ​α^μ​(t))​ei​Eμ​t,\displaystyle=\left(\hat{\alpha}_{\mu}+\delta\hat{\alpha}_{\mu}(t)\right)e^{iE_{\mu}t},(4)δ​α^μ​(t)\displaystyle\delta\hat{\alpha}_{\mu}(t)=η​∑να^ν†​(Xν​μ​(ω)​e−i​ω​t+Yν​μ∗​(ω)​ei​ω​t).\displaystyle=\eta\sum_{\nu}\hat{\alpha}_{\nu}^{\dagger}\left(X_{\nu\mu}(\omega)e^{-i\omega t}+Y_{\nu\mu}^{*}(\omega)e^{i\omega t}\right).(5)

HereEμE_{\mu}is theμth\mu^{\textrm{th}}quasiparticle energy.Xν​μ​(ω)X_{\nu\mu}(\omega)andYν​μ​(ω)Y_{\nu\mu}(\omega)are the forward and backward amplitudes, respectively.
The TDHFB HamiltonianH^​(t)\hat{H}(t)can be written asH^​(t)=H^0+δ​H^​(t),\hat{H}(t)=\hat{H}_{0}+\delta\hat{H}(t),(6)

whereH^0=∑μEμ​α^μ†​α^μ\hat{H}_{0}=\sum_{\mu}E_{\mu}\hat{\alpha}_{\mu}^{\dagger}\hat{\alpha}_{\mu}(7)

and the induced Hamiltonian isδ​H^​(t)=η​(δ​H^​(ω)​e−i​ω​t+δ​H^†​(ω)​ei​ω​t)\delta\hat{H}(t)=\eta\left(\delta\hat{H}(\omega)e^{-i\omega t}+\delta\hat{H}^{\dagger}(\omega)e^{i\omega t}\right)(8)

withδ​H^​(ω)=12​∑μ​ν(δ​Hμ​ν20​(ω)​α^μ†​α^ν†+δ​Hμ​ν02​(ω)​α^μ​α^ν)\delta\hat{H}(\omega)=\frac{1}{2}\sum_{\mu\nu}\left(\delta H_{\mu\nu}^{20}(\omega)\hat{\alpha}_{\mu}^{\dagger}\hat{\alpha}_{\nu}^{\dagger}+\delta H_{\mu\nu}^{02}(\omega)\hat{\alpha}_{\mu}\hat{\alpha}_{\nu}\right)(9)

representing a small-amplitude oscillation, and expressions forδ​Hμ​ν20​(ω)\delta H_{\mu\nu}^{20}(\omega)andδ​Hμ​ν02​(ω)\delta H_{\mu\nu}^{02}(\omega)given, e.g., in Ref.[16].
Substituting these definitions into the TDHFB equation (3) yields the FAM equations[1,12]:(Eμ+Eν−ω)​Xμ​ν​(ω)+δ​Hμ​ν20​(ω)\displaystyle\left(E_{\mu}+E_{\nu}-\omega\right)X_{\mu\nu}(\omega)+\delta H_{\mu\nu}^{20}(\omega)=−Fμ​ν20​(ω),\displaystyle=-F_{\mu\nu}^{20}(\omega),(10)(Eμ+Eν+ω)​Yμ​ν​(ω)+δ​Hμ​ν02​(ω)\displaystyle\left(E_{\mu}+E_{\nu}+\omega\right)Y_{\mu\nu}(\omega)+\delta H_{\mu\nu}^{02}(\omega)=−Fμ​ν02​(ω).\displaystyle=-F_{\mu\nu}^{02}(\omega).(11)

The quantity of interest is thestrength function, defined byd​B​(ω;F^)d​ω=−1π​Im​{S​(ω;F^)},\frac{dB(\omega;\hat{F})}{d\omega}=-\frac{1}{\pi}\text{Im}\left\{S(\omega;\hat{F})\right\},(12)

whereS​(ω;F^)=∑μ<ν(Fμ​ν20​(ω)∗​Xμ​ν​(ω)+Fμ​ν02​(ω)∗​Yμ​ν​(ω)).S(\omega;\hat{F})=\sum_{\mu<\nu}\left(F_{\mu\nu}^{20}(\omega)^{*}X_{\mu\nu}(\omega)+F_{\mu\nu}^{02}(\omega)^{*}Y_{\mu\nu}(\omega)\right).(13)

We refer toS​(ω;F^)S(\omega;\hat{F})in Eq. (13) as the QRPA response function for the external fieldF^\hat{F}; it is the auxiliary quantity from which the strength function is obtained.
In practice, we assume that the external weak field is frequency-independent, i.e.,Fμ​ν20​(ω)=Fμ​ν20F_{\mu\nu}^{20}(\omega)=F_{\mu\nu}^{20}andFμ​ν02​(ω)=Fμ​ν02F_{\mu\nu}^{02}(\omega)=F_{\mu\nu}^{02}.

## 2.2Obtaining
the Strength Function by Solving Linear Equations

The FAM equations can also be written in a compact matrix form. This reformulation is useful for two reasons. First, it isolates the frequency dependence. Second, it makes it possible to apply standard linear-algebra tools directly to the QRPA strength-function problem.
Expanding the induced Hamiltonian matrix elementsδ​Hμ​ν20​(ω)\delta H_{\mu\nu}^{20}(\omega)andδ​Hμ​ν02​(ω)\delta H_{\mu\nu}^{02}(\omega)in terms of the QRPA matricesAAandBB[16]viaδ​Hμ​ν20​(ω)\displaystyle\delta H_{\mu\nu}^{20}(\omega)=−(Eμ+Eν)​Xμ​ν​(ω)+∑μ′<ν′(Aμ​ν,μ′​ν′​Xμ′​ν′​(ω)+Bμ​ν,μ′​ν′​Yμ′​ν′​(ω)),\displaystyle=-(E_{\mu}+E_{\nu})X_{\mu\nu}(\omega)+\sum_{\mu^{\prime}<\nu^{\prime}}\left(A_{\mu\nu,\mu^{\prime}\nu^{\prime}}X_{\mu^{\prime}\nu^{\prime}}(\omega)+B_{\mu\nu,\mu^{\prime}\nu^{\prime}}Y_{\mu^{\prime}\nu^{\prime}}(\omega)\right),(14)δ​Hμ​ν02​(ω)\displaystyle\delta H_{\mu\nu}^{02}(\omega)=−(Eμ+Eν)​Yμ​ν​(ω)+∑μ′<ν′(Bμ​ν,μ′​ν′∗​Xμ′​ν′​(ω)+Aμ​ν,μ′​ν′∗​Yμ′​ν′​(ω)),\displaystyle=-(E_{\mu}+E_{\nu})Y_{\mu\nu}(\omega)+\sum_{\mu^{\prime}<\nu^{\prime}}\left(B_{\mu\nu,\mu^{\prime}\nu^{\prime}}^{*}X_{\mu^{\prime}\nu^{\prime}}(\omega)+A_{\mu\nu,\mu^{\prime}\nu^{\prime}}^{*}Y_{\mu^{\prime}\nu^{\prime}}(\omega)\right)\,,(15)

we recast the FAM equations into the linear response matrix equation:([ABB∗A∗]−ω​[I00−I])​[X​(ω)Y​(ω)]=−[F20F02],\left(\begin{bmatrix}A&B\\
B^{*}&A^{*}\end{bmatrix}-\omega\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\right)\begin{bmatrix}X(\omega)\\
Y(\omega)\end{bmatrix}=-\begin{bmatrix}F^{20}\\
F^{02}\end{bmatrix}\,,(16)

whereX​(ω),Y​(ω),F20,F02∈ℂnX(\omega),Y(\omega),F^{20},F^{02}\in\mathbb{C}^{n}are the vectorized representations of the strict upper triangular parts(μ<ν)(\mu<\nu)of the respective matrices.
One can evaluate the strength function on a frequency grid,ωi\omega_{i},i=1,2,…,nωi=1,2,\ldots,n_{\omega}, within an appropriate frequency range by solving (16) and using (12) and (13) for eachωi\omega_{i}.
Note that, whenωi\omega_{i}is near one of the eigenvalues of the matrix pencil([ABB∗A∗],[I00−I]),\left(\begin{bmatrix}A&B\\
B^{*}&A^{*}\end{bmatrix},\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\right)\,,(17)

(16) becomes ill-conditioned or singular.
To avoid these singularities in practical calculations, we replace the real frequency by the complex valueω→ωγ:=ω+i​γ\omega\to\omega_{\gamma}:=\omega+i\gammawith a smearing widthγ>0\gamma>0.
The strength function then becomes,d​B​(ω;F^)d​ω=limγ→0+−1π​Im​{S​(ωγ;F^)}=limγ→0+−1π​Im​{[F20F02]†​[X​(ωγ)Y​(ωγ)]}.\frac{dB(\omega;\hat{F})}{d\omega}=\lim_{\gamma\to 0^{+}}-\frac{1}{\pi}\text{Im}\left\{S(\omega_{\gamma};\hat{F})\right\}=\lim_{\gamma\to 0^{+}}-\frac{1}{\pi}\text{Im}\left\{\begin{bmatrix}F^{20}\\
F^{02}\end{bmatrix}^{\dagger}\begin{bmatrix}X(\omega_{\gamma})\\
Y(\omega_{\gamma})\end{bmatrix}\right\}\,.(18)

## 2.3Representing
the Strength Function through Eigendecomposition

An alternative way to compute the strength function is to first perform an eigendecomposition of the QRPA matrix pencil (17), and then rewrite the strength function in terms of the QRPA eigenmodes.
This approach allows us to evaluate the strength function at any frequencyω\omegaonce the eigendecomposition of (17) is obtained. The special matrix structure of (17) yields a corresponding structure in its eigendecomposition, as described below.

If the QRPA matrices satisfyA†=A,BT=BA^{\dagger}=A,B^{T}=Band the matrix[ABB∗A∗]\begin{bmatrix}A&B\\
B^{*}&A^{*}\end{bmatrix}is positive-definite, there exists an eigendecomposition whose eigenvalues are real and come in pairs.
We refer the reader to[3, Proposition 1]and[18, Theorem 3]for a proof.

## Theorem 1

LetA,B∈ℂn×nA,B\in\mathbb{C}^{n\times n}such thatA†=A,BT=BA^{\dagger}=A,B^{T}=Band[ABB∗A∗]\begin{bmatrix}A&B\\
B^{*}&A^{*}\end{bmatrix}is positive-definite.
Then there existX,Y∈ℂn×nX,Y\in\mathbb{C}^{n\times n}and diagonalΩ∈ℝn×n\Omega\in\mathbb{R}^{n\times n}with positive diagonal elements such that:[ABB∗A∗]​[XY∗YX∗]=[I00−I]​[XY∗YX∗]​[+Ω00−Ω],\begin{bmatrix}A&B\\
B^{*}&A^{*}\end{bmatrix}\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}=\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}\begin{bmatrix}+\Omega&0\\
0&-\Omega\end{bmatrix}\,,(19)

and[XY∗YX∗]†​[I00−I]​[XY∗YX∗]=[I00−I],\displaystyle\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}^{\dagger}\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}=\begin{bmatrix}I&0\\
0&-I\end{bmatrix},(20)[XY∗YX∗]​[I00−I]​[XY∗YX∗]†=[I00−I],\displaystyle\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}^{\dagger}=\begin{bmatrix}I&0\\
0&-I\end{bmatrix},(21)[XY∗YX∗]−1=[I00−I]​[XY∗YX∗]†​[I00−I].\displaystyle\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}^{-1}=\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}^{\dagger}\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\,.(22)

By Theorem1, the matrix in (16) is invertible for anyωγ\omega_{\gamma}away from the real poles, and in particular for everyγ>0\gamma>0:([ABB∗A∗]−ωγ​[I00−I])−1=[XY∗YX∗]​[(Ω−ωγ​I)−100(−Ω−ωγ​I)−1]​[XY∗YX∗]−1​[I00−I].\begin{split}&\left(\begin{bmatrix}A&B\\
B^{*}&A^{*}\end{bmatrix}-\omega_{\gamma}\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\right)^{-1}=\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}\begin{bmatrix}(\Omega-\omega_{\gamma}I)^{-1}&0\\
0&(-\Omega-\omega_{\gamma}I)^{-1}\end{bmatrix}\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}^{-1}\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\,.\end{split}(23)

For compactness in the following derivation, we define𝒰:=[XY∗YX∗],ℱ:=[F20F02].\mathcal{U}:=\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix},\qquad\mathcal{F}:=\begin{bmatrix}F^{20}\\
F^{02}\end{bmatrix}\,.

Using the vectorized notation introduced above and substituting the inverse (23) into Eq. (13) yieldsS​(ωγ;F^)=ℱ†​[X​(ωγ)Y​(ωγ)]=−ℱ†​([ABB∗A∗]−ωγ​[I00−I])−1​ℱ=−(𝒰†​ℱ)†​[(Ω−ωγ​I)−100(−Ω−ωγ​I)−1]​(𝒰−1​[I00−I]​ℱ)=−(𝒰†​ℱ)†​[(Ω−ωγ​I)−100(Ω+ωγ​I)−1]​(𝒰†​ℱ).\begin{split}S(\omega_{\gamma};\hat{F})&=\mathcal{F}^{\dagger}\begin{bmatrix}X(\omega_{\gamma})\\
Y(\omega_{\gamma})\end{bmatrix}\\
&=-\mathcal{F}^{\dagger}\left(\begin{bmatrix}A&B\\
B^{*}&A^{*}\end{bmatrix}-\omega_{\gamma}\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\right)^{-1}\mathcal{F}\\
&=-\left(\mathcal{U}^{\dagger}\mathcal{F}\right)^{\dagger}\begin{bmatrix}(\Omega-\omega_{\gamma}I)^{-1}&0\\
0&(-\Omega-\omega_{\gamma}I)^{-1}\end{bmatrix}\left(\mathcal{U}^{-1}\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\mathcal{F}\right)\\
&=-\left(\mathcal{U}^{\dagger}\mathcal{F}\right)^{\dagger}\begin{bmatrix}(\Omega-\omega_{\gamma}I)^{-1}&0\\
0&(\Omega+\omega_{\gamma}I)^{-1}\end{bmatrix}\left(\mathcal{U}^{\dagger}\mathcal{F}\right)\,.\end{split}(24)

This implies that−1π​Im​{S​(ωγ;F^)}=([XY∗YX∗]†​[F20F02])†​[γ/π(ω−Ω)2+γ200−γ/π(ω+Ω)2+γ2]​([XY∗YX∗]†​[F20F02]),\begin{split}-\frac{1}{\pi}\text{Im}\left\{S(\omega_{\gamma};\hat{F})\right\}=\left(\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}^{\dagger}\begin{bmatrix}F^{20}\\
F^{02}\end{bmatrix}\right)^{\dagger}\begin{bmatrix}\frac{\gamma/\pi}{(\omega-\Omega)^{2}+\gamma^{2}}&0\\
0&\frac{-\gamma/\pi}{(\omega+\Omega)^{2}+\gamma^{2}}\end{bmatrix}\left(\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}^{\dagger}\begin{bmatrix}F^{20}\\
F^{02}\end{bmatrix}\right)\,,\end{split}(25)

where we have used the corresponding identity for the diagonal matrix appearing above.
It follows, after taking the limitγ→0+\gamma\to 0^{+}, that the strength function (18) can be expressed as a sum of Dirac delta functions located at the QRPA poles,d​B​(ω;F^)d​ω=∑i=1n|Ti​(F^)|2​δ​(ω−Ωi)−∑i=1n|T~i​(F^)|2​δ​(ω+Ωi),\frac{dB(\omega;\hat{F})}{d\omega}=\sum_{i=1}^{n}|T_{i}(\hat{F})|^{2}\delta(\omega-\Omega_{i})-\sum_{i=1}^{n}|\tilde{T}_{i}(\hat{F})|^{2}\delta(\omega+\Omega_{i}),(26)

whereTi​(F^)T_{i}(\hat{F})andT~i​(F^)\tilde{T}_{i}(\hat{F})are defined as[T​(F^)T~​(F^)]=[XY∗YX∗]†​[F20F02].\begin{bmatrix}T(\hat{F})\\
\tilde{T}(\hat{F})\end{bmatrix}=\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}^{\dagger}\begin{bmatrix}F^{20}\\
F^{02}\end{bmatrix}.(27)

In the eigenmode representation of Eq. (26), the projected quantitiesTi​(F^)T_{i}(\hat{F})andT~i​(F^)\tilde{T}_{i}(\hat{F})are often referred to as QRPA transition amplitudes to the positive- and negative-frequency branches, respectively.

In Figure1, we plot example QRPA transition amplitudes and the corresponding strength function.
The magnitudes ofTi​(F^)T_{i}(\hat{F})andT~i​(F^)\tilde{T}_{i}(\hat{F})do not necessarily match, so the resulting strength function is not, in general, antisymmetric about the origin.Figure 1:Illustrative example based on a five-shell QRPA calculation in6Li. The model space is small enough that the QRPA matrices can be formed and diagonalized explicitly. The example is used here only to visualize the spectral representation: left, representative transition amplitudes for the positive- and negative-frequency branches; right, the corresponding schematic strength function, shown as a sum of weighted discrete transitions.

## 2.4Reformulation as a Reduced Eigenvalue Problem

In practice, the QRPA matricesAAandBBand the external weak fieldsF20,F02F^{20},F^{02}are often real.
In that case, the dimension of the eigenvalue problem can be reduced by two, by using the productsM​KMKandK​MKM, whereM=A+BM=A+BandK=A−BK=A-B. Under the positivity assumptions inherited from Theorem1, bothMMandKKare symmetric positive-definite. Related reductions also appear in[16,5]. We summarize this construction here for completeness.

The real counterpart of the eigendecomposition (19) is[ABBA]​[XYYX]=[I00−I]​[XYYX]​[+Ω00−Ω],\begin{bmatrix}A&B\\
B&A\end{bmatrix}\begin{bmatrix}X&Y\\
Y&X\end{bmatrix}=\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\begin{bmatrix}X&Y\\
Y&X\end{bmatrix}\begin{bmatrix}+\Omega&0\\
0&-\Omega\end{bmatrix},(28)

withX,Y∈ℝn×nX,Y\in\mathbb{R}^{n\times n}.
In addition, the normalization constraints (20),(21) indicate thatXT​X−YT​Y=I,XT​Y−YT​X=0,X​XT−Y​YT=I,X​YT−Y​XT=0.X^{T}X-Y^{T}Y=I,\quad X^{T}Y-Y^{T}X=0,\quad XX^{T}-YY^{T}=I,\quad XY^{T}-YX^{T}=0.(29)

These conditions imply that(X+Y)−1=(X−Y)Tand(X−Y)−1=(X+Y)T.(X+Y)^{-1}=(X-Y)^{T}\quad\text{and}\quad(X-Y)^{-1}=(X+Y)^{T}.(30)

Note that the eigendecomposition (28) is equivalent to[AB−B−A]​[XYYX]=[XYYX]​[+Ω00−Ω],\begin{bmatrix}A&B\\
-B&-A\end{bmatrix}\begin{bmatrix}X&Y\\
Y&X\end{bmatrix}=\begin{bmatrix}X&Y\\
Y&X\end{bmatrix}\begin{bmatrix}+\Omega&0\\
0&-\Omega\end{bmatrix},(31)

and the matrix[AB−B−A]\begin{bmatrix}A&B\\
-B&-A\end{bmatrix}(32)

is often referred to as the Casida matrix.

One can rewrite the eigenvalue problem for the Casida matrix,[AB−B−A]​[xiyi]=Ωi​[xiyi],\begin{bmatrix}A&B\\
-B&-A\end{bmatrix}\begin{bmatrix}x_{i}\\
y_{i}\end{bmatrix}=\Omega_{i}\begin{bmatrix}x_{i}\\
y_{i}\end{bmatrix},(33)

by employing a unitary similarity transformation,J=12​[III−I]J=\frac{1}{\sqrt{2}}\begin{bmatrix}I&I\\
I&-I\end{bmatrix}(34)

to obtain[0KM0]​[xi+yixi−yi]=Ωi​[xi+yixi−yi],\begin{bmatrix}0&K\\
M&0\end{bmatrix}\begin{bmatrix}x_{i}+y_{i}\\
x_{i}-y_{i}\end{bmatrix}=\Omega_{i}\begin{bmatrix}x_{i}+y_{i}\\
x_{i}-y_{i}\end{bmatrix},(35)

whereK:=A−BK:=A-BandM:=A+BM:=A+B.
Then we haveK​(xi−yi)=Ωi​(xi+yi),M​(xi+yi)=Ωi​(xi−yi),\begin{split}K(x_{i}-y_{i})=\Omega_{i}(x_{i}+y_{i}),\\
M(x_{i}+y_{i})=\Omega_{i}(x_{i}-y_{i}),\end{split}(36)

andM​K​(xi−yi)=Ωi2​(xi−yi),K​M​(xi+yi)=Ωi2​(xi+yi).\begin{split}MK(x_{i}-y_{i})=\Omega_{i}^{2}(x_{i}-y_{i}),\\
KM(x_{i}+y_{i})=\Omega_{i}^{2}(x_{i}+y_{i}).\end{split}(37)

In other words,M=(X−Y)​Ω​(X−Y)TandK=(X+Y)​Ω​(X+Y)T,M=(X-Y)\Omega(X-Y)^{T}\quad\text{and}\quad K=(X+Y)\Omega(X+Y)^{T},(38)

andM​K\displaystyle MK=(X−Y)​Ω2​(X−Y)−1,\displaystyle=(X-Y)\Omega^{2}(X-Y)^{-1},(39)K​M\displaystyle KM=(X+Y)​Ω2​(X+Y)−1,\displaystyle=(X+Y)\Omega^{2}(X+Y)^{-1},(40)

These identities show that the eigendecomposition (31) of dimension2​n2ncan be replaced by an eigenvalue problem of dimensionnnfor either the matrixM​KMKor the matrixK​MKM.
In addition, once we have computed an eigenvectorxi−yix_{i}-y_{i}ofM​KMK, we can recoverxi+yix_{i}+y_{i}fromxi+yi=1Ωi​K​(xi−yi),x_{i}+y_{i}=\frac{1}{\Omega_{i}}K(x_{i}-y_{i})\,,(41)

without having to find an eigendecomposition ofK​MKM.
Once the vectorsxi+yix_{i}+y_{i}andxi−yix_{i}-y_{i}are known, the original QRPA eigenvectorsxix_{i}andyiy_{i}follow immediately.

The reduced formulation also gives a direct spectral representation of the strength function. To see this, we insert the unitary similarity matrixJJ(34) into[XYYX]T​[F20F02]\begin{bmatrix}X&Y\\
Y&X\end{bmatrix}^{T}\begin{bmatrix}F^{20}\\
F^{02}\end{bmatrix}

as[XYYX]T​J​J​[F20F02].\begin{bmatrix}X&Y\\
Y&X\end{bmatrix}^{T}JJ\begin{bmatrix}F^{20}\\
F^{02}\end{bmatrix}.

This yields[R​(F^)R~​(F^)]:=12​[(X+Y)T​(F20+F02)+(X−Y)T​(F20−F02)(X+Y)T​(F20+F02)−(X−Y)T​(F20−F02)],\begin{bmatrix}R(\hat{F})\\
\tilde{R}(\hat{F})\end{bmatrix}:=\frac{1}{2}\begin{bmatrix}(X+Y)^{T}(F^{20}+F^{02})+(X-Y)^{T}(F^{20}-F^{02})\\
(X+Y)^{T}(F^{20}+F^{02})-(X-Y)^{T}(F^{20}-F^{02})\end{bmatrix},(42)

so that the strength function can be written asd​B​(ω;F^)d​ω=∑i=1n|Ri​(F^)|2​δ​(ω−Ωi)−∑i=1n|R~i​(F^)|2​δ​(ω+Ωi).\frac{dB(\omega;\hat{F})}{d\omega}=\sum_{i=1}^{n}|R_{i}(\hat{F})|^{2}\delta(\omega-\Omega_{i})-\sum_{i=1}^{n}|\tilde{R}_{i}(\hat{F})|^{2}\delta(\omega+\Omega_{i}).(43)

This representation will serve as the starting point for the Lanczos approximation developed in the next section.

The reduced formulation above is the key structural ingredient for the numerical methods developed in the next section. In particular, it provides the reduced operator on which the symmetric Lanczos approximation is built.

## 3Computational Methods for the Strength Function

This section describes the numerical strategies used to evaluate the QRPA strength function in practice. We first summarize two frequency-by-frequency approaches based on the linear response equation and then derive the symmetric Lanczos approximation based on the reduced eigenvalue problem.

## 3.1Frequency-by-Frequency Solvers

## 3.1.1Finite Amplitude Method (FAM)

A standard approach to solving Eqs. (10) and (11) is the iterative finite amplitude method (FAM)[1,12].
For each fixed frequencyω\omega, FAM treats the response equations as a fixed-point problem for the amplitudesXμ​ν​(ω)X_{\mu\nu}(\omega)andYμ​ν​(ω)Y_{\mu\nu}(\omega).
A basic iteration proceeds as follows:
- 1.

Use the current amplitudesXμ​ν​(ω)X_{\mu\nu}(\omega)andYμ​ν​(ω)Y_{\mu\nu}(\omega)to computeδ​Hμ​ν20​(ω)\delta H_{\mu\nu}^{20}(\omega)andδ​Hμ​ν02​(ω)\delta H_{\mu\nu}^{02}(\omega).
- 2.

Add the external field contributions,δ​Hμ​ν20​(ω)\displaystyle\delta H_{\mu\nu}^{20}(\omega)←δ​Hμ​ν20​(ω)+Fμ​ν20,\displaystyle\leftarrow\delta H_{\mu\nu}^{20}(\omega)+F_{\mu\nu}^{20},δ​Hμ​ν02​(ω)\displaystyle\delta H_{\mu\nu}^{02}(\omega)←δ​Hμ​ν02​(ω)+Fμ​ν02.\displaystyle\leftarrow\delta H_{\mu\nu}^{02}(\omega)+F_{\mu\nu}^{02}.
- 3.

Update the amplitudes according toXμ​ν​(ω)←−(Eμ+Eν−ω)−1​δ​Hμ​ν20​(ω),Yμ​ν​(ω)←−(Eμ+Eν+ω)−1​δ​Hμ​ν02​(ω).\begin{split}X_{\mu\nu}(\omega)&\leftarrow-\left(E_{\mu}+E_{\nu}-\omega\right)^{-1}\delta H_{\mu\nu}^{20}(\omega),\\
Y_{\mu\nu}(\omega)&\leftarrow-\left(E_{\mu}+E_{\nu}+\omega\right)^{-1}\delta H_{\mu\nu}^{02}(\omega).\end{split}(44)

The FAM is effective because it avoids constructing the full QRPA matrix explicitly.
However, the plain fixed-point iteration is not guaranteed to converge for all frequencies: as with any stationary fixed-point scheme, convergence requires the associated iteration map to be sufficiently contractive.
In practice, convergence can become slow or fail near poorly conditioned response points, especially close to QRPA poles.
For this reason, practical FAM calculations commonly use acceleration schemes such as Broyden mixing[6].
Even with such acceleration, the full iteration must be repeated at every frequency point in the target interval.

## 3.1.2GMRES Solver

Because Eq. (16) is a linear system, Krylov-subspace methods such as the generalized minimal residual method (GMRES)[17]provide a natural alternative to fixed-point FAM iterations. For a given complex frequencyωγ\omega_{\gamma}, GMRES seeks the approximation in the associated Krylov subspace that minimizes the residual norm. In our calculations, this typically leads to significantly fewer iterations than plain FAM updates.

To build the Krylov basis, the matricesAAandBBneed not be formed explicitly. Each GMRES iteration only requires the matrix–vector product[X​(ωγ)Y​(ωγ)]→([ABBA]−ωγ​[I00−I])​[X​(ωγ)Y​(ωγ)].\begin{bmatrix}X(\omega_{\gamma})\\
Y(\omega_{\gamma})\end{bmatrix}\to\left(\begin{bmatrix}A&B\\
B&A\end{bmatrix}-\omega_{\gamma}\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\right)\begin{bmatrix}X(\omega_{\gamma})\\
Y(\omega_{\gamma})\end{bmatrix}.(45)

Evaluating this product is equivalent to computing the left-hand side of the FAM equations (10) and (11). As with the FAM, however, a separate GMRES solve is required for every frequency value of interest. In Section4.1.2, we describe how this matvec is assembled in practice and present the preconditioner used to accelerate GMRES convergence.

## 3.2Lanczos Approximation of the Strength Function

We now use the reduced formulation to derive a Lanczos approximation for the strength function. Instead of fully diagonalizing (39) (or (40)), which can still be expensive even after reduction, we approximate the exact spectral representation (43) by means of the Lanczos method[9].
From a numerical perspective, the appeal of this approach is that one Lanczos run can capture the dominant spectral information needed over a broad frequency interval.
Closely related Krylov approaches have also been used for linear-response strength calculations in nuclear systems; see, for example,[19].

Although the matrixM​KMKis not symmetric in the Euclidean inner product, it is self-adjoint with respect to theKK-inner product, i.e.,⟨x,M​K​y⟩K=xT​K​M​K​y=(M​K​x)T​K​y=⟨M​K​x,y⟩K,\langle x,MKy\rangle_{K}=x^{T}KMKy=(MKx)^{T}Ky=\langle MKx,y\rangle_{K},(46)

for anyx,y∈ℝnx,y\in\mathbb{R}^{n}.
This observation allows us to apply a symmetric Lanczos process in theKK-inner product rather than working with a nonsymmetric algorithm in the Euclidean inner product.
Anmm-step Lanczos process generatesM​K​Qm=Qm​Tm+fm​emTMKQ_{m}=Q_{m}T_{m}+f_{m}e_{m}^{T}(47)

whereQmT​K​Qm=IandQmT​K​fm=0.Q_{m}^{T}KQ_{m}=I\quad\text{and}\quad Q_{m}^{T}Kf_{m}=0.(48)

The projected matrixTm∈ℝm×mT_{m}\in\mathbb{R}^{m\times m}is tridiagonal and has the eigendecompositionTm​Ym=Ym​Θm.T_{m}Y_{m}=Y_{m}\Theta_{m}.

The eigenvalues{θi}i=1m\{\theta_{i}\}_{i=1}^{m}of the tridiagonal matrixTmT_{m}approximate the squared excitation energies{Ωi2}i=1n\{\Omega_{i}^{2}\}_{i=1}^{n}. The corresponding excitation energies are therefore approximated asΩi≈θi.\Omega_{i}\approx\sqrt{\theta_{i}}.(49)

The eigenvectors(X−Y)∈ℝn×n(X-Y)\in\mathbb{R}^{n\times n}ofM​KMKare approximated byZm∈ℝn×mZ_{m}\in\mathbb{R}^{n\times m}, defined asZm:=Qm​Ym.Z_{m}:=Q_{m}Y_{m}.(50)

These Ritz vectors, however, are normalized through the relationZmT​K​Zm=I,Z_{m}^{T}KZ_{m}=I,(51)

which is different from the normalization(X−Y)T​K​(X−Y)=Ω(X-Y)^{T}K(X-Y)=\Omega(52)

that holds for the eigenvectorX−YX-YofM​KMKas in (38).

To relate this normalization to the exact QRPA normalization, suppose for a moment that the reduced eigenproblem were solved exactly (for example, through annn-step Lanczos process) and that we had obtainedM​K​Z=Z​ΘMKZ=Z\Theta(53)

whereZT​K​Z=IandΘ=Ω2.Z^{T}KZ=I\quad\mbox{and}\quad\Theta=\Omega^{2}.(54)

Comparing the normalization (54) with the normalization (52), we immediately obtainX−Y=Z​Ω1/2=Z​Θ1/4.X-Y=Z\Omega^{1/2}=Z\Theta^{1/4}.(55)

Moreover, sinceX+Y=K​(X−Y)​Ω−1,X+Y=K(X-Y)\Omega^{-1},

we haveX+Y=K​Z​Ω−1/2=K​Z​Θ−1/4.X+Y=KZ\Omega^{-1/2}=KZ\Theta^{-1/4}.(56)

Thus, once the Ritz pairs(Θm,Zm)(\Theta_{m},Z_{m})have been computed from anmm-step Lanczos run, the strength function is approximated byd​B​(ω;F^)d​ω≈∑i=1m|Si​(F^)|2​δ​(ω−θi)−∑i=1m|S~i​(F^)|2​δ​(ω+θi),\frac{dB(\omega;\hat{F})}{d\omega}\approx\sum_{i=1}^{m}|S_{i}(\hat{F})|^{2}\delta(\omega-\sqrt{\theta_{i}})-\sum_{i=1}^{m}|\tilde{S}_{i}(\hat{F})|^{2}\delta(\omega+\sqrt{\theta_{i}}),(57)

where the vectorsS​(F^)S(\hat{F})andS~​(F^)\tilde{S}(\hat{F})have componentsSi​(F^)S_{i}(\hat{F})andS~i​(F^)\tilde{S}_{i}(\hat{F}), respectively, and are defined as[S​(F^)S~​(F^)]=12​[(K​Zm​Θm−1/4)T​(F20+F02)+(Zm​Θm1/4)T​(F20−F02)(K​Zm​Θm−1/4)T​(F20+F02)−(Zm​Θm1/4)T​(F20−F02)].\begin{bmatrix}S(\hat{F})\\
\tilde{S}(\hat{F})\end{bmatrix}=\frac{1}{2}\begin{bmatrix}(KZ_{m}\Theta_{m}^{-1/4})^{T}(F^{20}+F^{02})+(Z_{m}\Theta_{m}^{1/4})^{T}(F^{20}-F^{02})\\
(KZ_{m}\Theta_{m}^{-1/4})^{T}(F^{20}+F^{02})-(Z_{m}\Theta_{m}^{1/4})^{T}(F^{20}-F^{02})\end{bmatrix}.(58)

One might worry that replacing the fullnn-term spectral sum by onlymmRitz contributions is too severe an approximation, or that the apparent agreement is driven primarily by replacing each Dirac delta peak by a smooth kernel such as a Lorentzian. The smoothing is certainly important for comparing strength profiles on a finite-frequency grid, but the quality of the approximation also depends on whether the projected transition amplitudesSi​(F^)S_{i}(\hat{F})andS~i​(F^)\tilde{S}_{i}(\hat{F})capture the relevant QRPA strength carried by the external field. In the numerical section of this paper, we therefore assess the smoothed strength functions through pointwise agreement, KL divergence, and runtime comparisons.

## 3.2.1Comparison with Frequency-by-Frequency Solvers

The conceptual difference between the Lanczos approach and the FAM/GMRES solvers is worth emphasizing. The Lanczos method approximates the spectral representation of the strength function, whereas the FAM and GMRES approximate the response function at one prescribed frequency.
Note that the strength function defined as in (12),d​B​(ω;F^)d​ω=−1π​Im​{S​(ω;F^)},\frac{dB(\omega;\hat{F})}{d\omega}=-\frac{1}{\pi}\text{Im}\left\{S(\omega;\hat{F})\right\},

whereS​(ω;F^)=∑μ<ν(Fμ​ν20​(ω)∗​Xμ​ν​(ω)+Fμ​ν02​(ω)∗​Yμ​ν​(ω)),S(\omega;\hat{F})=\sum_{\mu<\nu}\left(F_{\mu\nu}^{20}(\omega)^{*}X_{\mu\nu}(\omega)+F_{\mu\nu}^{02}(\omega)^{*}Y_{\mu\nu}(\omega)\right),

requires the amplitudesXμ​ν​(ω)X_{\mu\nu}(\omega)andYμ​ν​(ω)Y_{\mu\nu}(\omega)for afixedfrequencyω\omega.
Consequently, both the FAM and GMRES must be run separately for each frequency at which the strength function is requested.

On the other hand, the strength function written in terms of the eigendecomposition as in (26),d​B​(ω;F^)d​ω=∑i=1n|Ti​(F^)|2​δ​(ω−Ωi)−∑i=1n|T~i​(F^)|2​δ​(ω+Ωi),\frac{dB(\omega;\hat{F})}{d\omega}=\sum_{i=1}^{n}|T_{i}(\hat{F})|^{2}\delta(\omega-\Omega_{i})-\sum_{i=1}^{n}|\tilde{T}_{i}(\hat{F})|^{2}\delta(\omega+\Omega_{i}),

where[T​(F^)T~​(F^)]=[XY∗YX∗]†​[F20F02],\begin{bmatrix}T(\hat{F})\\
\tilde{T}(\hat{F})\end{bmatrix}=\begin{bmatrix}X&Y^{*}\\
Y&X^{*}\end{bmatrix}^{\dagger}\begin{bmatrix}F^{20}\\
F^{02}\end{bmatrix},

shows thatω\omegais decoupled from the transition-amplitude calculation. Because the Lanczos procedure approximates the eigenvaluesΩi\Omega_{i}together with the QRPA transition amplitudesT​(F^)T(\hat{F})andT~​(F^)\tilde{T}(\hat{F}), a single Lanczos run can be used to approximate the strength function over an entire frequency interval. The FAM and GMRES are therefore attractive when only a small number of frequencies are needed, whereas the Lanczos method becomes advantageous when one seeks a broad spectral scan or a full response profile.

## 3.2.2Lanczos Initialization

The symmetric Lanczos process is applied to the reduced matrixM​KMKwith theKK-inner product. We initialize the recursion with the normalized vector associated with the external field combinationf+:=F20+F02,q1=f+‖f+‖K,‖v‖K:=(vT​K​v)1/2.f_{+}:=F^{20}+F^{02},\qquad q_{1}=\frac{f_{+}}{\|f_{+}\|_{K}},\qquad\|v\|_{K}:=(v^{T}Kv)^{1/2}.(59)

This choice is natural in the reduced formulation because the combinationX+YX+Y, which is reconstructed fromK​Zm​Θm−1/4KZ_{m}\Theta_{m}^{-1/4}, couples directly tof+f_{+}in Eq. (58). It also respects the symmetry structure of the axially-deformed calculation. In our implementation, the quasiparticle basis and QRPA matrices inherit selection rules associated with the intrinsic projection quantum number, soAA,BB, and the reduced operatorM​KMKdecompose into invariant symmetry sectors. BecauseF20F^{20}andF02F^{02}are generated from an external transition operator with a specified intrinsic component,f+f_{+}already lies in the sector relevant to the desired response.

This symmetry-adapted support is important in practice. An unrestricted random starting vector generally contains components in other decoupled sectors and therefore samples spectral information unrelated to the chosen strength function. A random vector restricted to the same nonzero pattern and sign structure asf+f_{+}removes most of this mismatch and can reproduce the overall profile well, but it still lacks the physical matrix-element magnitudes of the external field. Starting fromf+f_{+}therefore both selects the correct symmetry sector and preserves the field-dependent weights needed for the detailed strength profile. We also retain the projections associated withf−:=F20−F02f_{-}:=F^{20}-F^{02}during the Lanczos calculation, since Eq. (58) shows that bothf+f_{+}andf−f_{-}enter the reconstructed transition amplitudes.

## 4Numerical Results

In this section we assess the performance of the symmetric Lanczos method for approximating QRPA strength functions.
We first discuss several practical considerations, including the regularization of the Dirac-delta distribution and the construction of matrix–vector products (matvecs) for GMRES and Lanczos.
We then present calculations for two realistic nuclei: the medium-mass nucleus112Sn and the heavier rare-earth nucleus150Nd.
The numerical discussion is organized in stages: first, we compare GMRES with the conventional iterative FAM (IFAM) to establish GMRES as an efficient frequency-by-frequency reference calculation; next, we compare the Lanczos approximation directly with this GMRES reference using strength profiles, pointwise errors, KL divergences, and runtimes.

All iterative solvers used in this section were implemented through the Python packagepynfam[15].
This package provides a workflow around the Fortran codeshfbthoandpnfamfor charge-changing HFB+QRPA calculations[11,12].
For each nucleus,hfbthois first used to obtain the HFB ground state through an axial deformation scan, after which the lowest-energy solution is taken as the reference state for the subsequentpnfamcalculation.
The latter computes the linear response for the chosen external field on the prescribed energy contour, from which the corresponding strength function is constructed.

Unless otherwise noted, we use common numerical settings across the two nuclei and vary only the nucleus-dependent inputs; both112Sn and150Nd are computed with 16 harmonic-oscillator shells.
The underlying mean field is generated with SkM∗, a standard Skyrme energy-density functional widely used in self-consistent mean-field and QRPA calculations[2].
In the pnFAM calculations we do not explicitly include theJ2J^{2}terms; that is, the spin-current contributions associated with that sector of the Skyrme functional are not turned on by hand in our setup.
Detailed discussions of the individual nuclei and their corresponding response functions are deferred to the subsections below.

## 4.1Practical Considerations

## 4.1.1Regularization

Because no conventional function possesses the properties of the Dirac-delta function, it is often defined through limits or the theory of distributions.
A common way to define the delta function is as the limit of a Gaussian functiongσ​(t)=1(2​π​σ2)1/2​e−t22​σ2,g_{\sigma}(t)=\frac{1}{(2\pi\sigma^{2})^{1/2}}e^{-\frac{t^{2}}{2\sigma^{2}}},(60)

or as the limit of a Lorentzian functionLγ​(t)=γ/πt2+γ2.L_{\gamma}(t)=\frac{\gamma/\pi}{t^{2}+\gamma^{2}}.(61)

As the width parametersσ\sigmaandγ\gammaof the Gaussian and Lorentzian, respectively, approach zero, the corresponding functions become infinitely tall and infinitely narrow, resembling the Dirac-delta function.

For density-of-states (DOS) problems, replacing the delta function with such an approximate function is known asregularizingthe spectral density, and it is shown in[10]that the width parameter controls the resolution of the DOS curves.
In this paper, we adapt this regularization strategy for our strength function calculations, replacing the delta functions with Lorentzian functions.

## 4.1.2Matvecs for GMRES and Lanczos

The equivalence between the FAM equations (10),(11) and the linear response equation (16) indicates that we can obtain the matvec[X​(ωγ)Y​(ωγ)]↦([ABBA]−ωγ​[I00−I])​[X​(ωγ)Y​(ωγ)]\begin{bmatrix}X(\omega_{\gamma})\\
Y(\omega_{\gamma})\end{bmatrix}\mapsto\left(\begin{bmatrix}A&B\\
B&A\end{bmatrix}-\omega_{\gamma}\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\right)\begin{bmatrix}X(\omega_{\gamma})\\
Y(\omega_{\gamma})\end{bmatrix}(62)

by performing the following steps for eachμ<ν\mu<\nu.
- 1.

Use the amplitudesXμ​ν​(ωγ)X_{\mu\nu}(\omega_{\gamma})andYμ​ν​(ωγ)Y_{\mu\nu}(\omega_{\gamma})to computeδ​Hμ​ν20​(ωγ)\delta H_{\mu\nu}^{20}(\omega_{\gamma})andδ​Hμ​ν02​(ωγ)\delta H_{\mu\nu}^{02}(\omega_{\gamma}).
- 2.

Addδ​Hμ​ν20​(ωγ)\delta H_{\mu\nu}^{20}(\omega_{\gamma})to(Eμ+Eν−ωγ)​Xμ​ν​(ωγ)\left(E_{\mu}+E_{\nu}-\omega_{\gamma}\right)X_{\mu\nu}(\omega_{\gamma})and addδ​Hμ​ν02​(ωγ)\delta H_{\mu\nu}^{02}(\omega_{\gamma})to(Eμ+Eν+ωγ)​Yμ​ν​(ωγ)\left(E_{\mu}+E_{\nu}+\omega_{\gamma}\right)Y_{\mu\nu}(\omega_{\gamma}).

## GMRES.

For implementing GMRES, we use the diagonal preconditionerP=[(Eμ+Eν−ωγ)−100(Eμ+Eν+ωγ)−1].P=\begin{bmatrix}\left(E_{\mu}+E_{\nu}-\omega_{\gamma}\right)^{-1}&0\\
0&\left(E_{\mu}+E_{\nu}+\omega_{\gamma}\right)^{-1}\end{bmatrix}.(63)

The corresponding preconditioned matvec is[X​(ωγ)Y​(ωγ)]↦[(Eμ+Eν−ωγ)−100(Eμ+Eν+ωγ)−1]​([ABBA]−ωγ​[I00−I])​[X​(ωγ)Y​(ωγ)],\begin{bmatrix}X(\omega_{\gamma})\\
Y(\omega_{\gamma})\end{bmatrix}\mapsto\begin{bmatrix}\left(E_{\mu}+E_{\nu}-\omega_{\gamma}\right)^{-1}&0\\
0&\left(E_{\mu}+E_{\nu}+\omega_{\gamma}\right)^{-1}\end{bmatrix}\left(\begin{bmatrix}A&B\\
B&A\end{bmatrix}-\omega_{\gamma}\begin{bmatrix}I&0\\
0&-I\end{bmatrix}\right)\begin{bmatrix}X(\omega_{\gamma})\\
Y(\omega_{\gamma})\end{bmatrix},(64)

which can be obtained by performing the following steps:
- 1.

Use the amplitudesXμ​ν​(ωγ)X_{\mu\nu}(\omega_{\gamma})andYμ​ν​(ωγ)Y_{\mu\nu}(\omega_{\gamma})to computeδ​Hμ​ν20​(ωγ)\delta H_{\mu\nu}^{20}(\omega_{\gamma})andδ​Hμ​ν02​(ωγ)\delta H_{\mu\nu}^{02}(\omega_{\gamma}).
- 2.

Add(Eμ+Eν−ωγ)−1​δ​Hμ​ν20​(ωγ)\left(E_{\mu}+E_{\nu}-\omega_{\gamma}\right)^{-1}\delta H_{\mu\nu}^{20}(\omega_{\gamma})toX​(ωγ)X(\omega_{\gamma})and add(Eμ+Eν+ωγ)−1​δ​Hμ​ν02​(ωγ)\left(E_{\mu}+E_{\nu}+\omega_{\gamma}\right)^{-1}\delta H_{\mu\nu}^{02}(\omega_{\gamma})toY​(ωγ)Y(\omega_{\gamma}).

## Lanczos.

In order to perform the matvec involving the matrixM​KMK, whereM=A+BM=A+BandK=A−BK=A-B, for the symmetric Lanczos iterations on the reduced eigenvalue problem, we need to repeat the steps of (62).
The crucial distinction in the Lanczos method is that we need to setωγ=0\omega_{\gamma}=0, so that we have a matvec with the matrix[ABBA].\begin{bmatrix}A&B\\
B&A\end{bmatrix}.

Given a vectorX∈ℝnX\in\mathbb{R}^{n}, the matvec withM​KMKis computed as follows:
- 1.

Set up a vector[X0]\begin{bmatrix}X\\
0\end{bmatrix}by appendingXXwith a zero vector of sizenn.
- 2.

Apply the matvec to[X0]\begin{bmatrix}X\\
0\end{bmatrix}and obtain[A​XB​X]\begin{bmatrix}AX\\
BX\end{bmatrix}.
- 3.

ComputeZ:=A​X−B​XZ:=AX-BX.
- 4.

Apply the matvec to[Z0]\begin{bmatrix}Z\\
0\end{bmatrix}and obtain[A​ZB​Z]\begin{bmatrix}AZ\\
BZ\end{bmatrix}.
- 5.

SetM​K​X:=A​Z+B​ZMKX:=AZ+BZ.

We note that in addition to these two matvecs, we need one additional matvec to doKK-inner product orthogonalization, another matvec for reorthogonalization, and a final one for normalization with respect toKK-inner product.
Thus, the Lanczos recurrence itself incurs five matvecs per iteration.
In addition, after themm-step Lanczos iteration, we need to performmmmatvecs to computeK​Zm​Θm−1/4KZ_{m}\Theta_{m}^{-1/4}in order to derive the weightsSi​(F^)S_{i}(\hat{F})andS~i​(F^)\tilde{S}_{i}(\hat{F}).
Therefore,5​m+m=6​m5m+m=6mmatvecs are required in total.

## 4.2Medium-Mass and Heavy Nuclei

The QRPA matrix dimensions are94,48294,482for the medium-mass nucleus112Sn and101,324101,324for the heavier rare-earth nucleus150Nd.
We use converged frequency-by-frequency solvers as references for the smeared strength functions.
We compute the Gamow–Teller strength by combining the intrinsic components of theJπ=1+J^{\pi}=1^{+}spin–isospin operator.
In an axially-symmetric system, this amounts to performing separate calculations for theK=0K=0andK=1K=1components and reconstructing the total strength as the sum of theK=0K=0contribution and twice theK=1K=1contribution.
The factor of two accounts for the degeneracy of theK=±1K=\pm 1branches, which contribute equally to the total Gamow–Teller strength.

## 4.2.1GMRES as a Frequency-by-Frequency Reference

We first compare GMRES with IFAM to identify a practical reference solution for the subsequent Lanczos comparison.
Both methods solve the same linear-response problem at each prescribed frequency, but GMRES treats it directly as a Krylov linear solve rather than as a fixed-point iteration.
Thus, when both methods are converged to the same tolerance, agreement between them is expected; the main distinction is computational efficiency.
Figure2combines the comparison between GMRES and IFAM for both nuclei.
The upper panels show that the two methods produce visually indistinguishable total Gamow–Teller strength functions for112Sn and150Nd, while the lower panel quantifies this agreement through the absolute pointwise difference, which remains below10−610^{-6}over the full frequency interval.Figure 2:IFAM–GMRES comparison over0–5050MeV. Upper panels: overlaid total Gamow–Teller strengths for112Sn (left) and150Nd (right). Lower panel: absolute pointwise errors for112Sn (black) and150Nd (green).

The iteration-count comparison in Figure3reveals a clear efficiency advantage for GMRES over the iterative FAM calculation.
This improvement is consistent with the fact that GMRES typically requires fewer Krylov iterations to reach the same convergence tolerance.
For the representativeK=0K=0calculations shown in Figure3, GMRES requires23472347total iterations for112Sn compared with37813781for IFAM, and37623762for150Nd compared with53365336for IFAM over the range0–5050MeV.Figure 3:Iteration counts required for IFAM and GMRES to converge for theK=0K=0component of the Gamow–Teller operator over the interval0–5050MeV. The left panel corresponds to112Sn and the right panel to150Nd.

These results show that GMRES preserves the converged IFAM strength distribution while reducing the cost of the frequency-by-frequency calculation.
For this reason, in the remainder of this section we use the converged GMRES result as the frequency-by-frequency reference against which the Lanczos approximation is compared.

## 4.2.2Lanczos Approximation

We next compare the Lanczos approximation with the GMRES reference.
Unlike GMRES and IFAM, the Lanczos method does not solve a separate linear system at each frequency.
Instead, a single Krylov projection of the reduced eigenvalue problem provides the Ritz values and approximate transition amplitudes used to reconstruct the Lorentzian-smeared strength function over the entire interval.
This subsection is organized around three questions: how the strength profile converges as the Krylov dimension increases, how close the resulting normalized distributions are to the GMRES reference, and how the runtime compares with the frequency-by-frequency methods.

## 112Sn profile convergence.

We first consider the medium-mass nucleus112Sn.
To illustrate convergence with respect to the Krylov dimension, we compare Lanczos approximations withm=50m=50andm=100m=100iterations against the GMRES reference.
Figure4first shows the full0–5050MeV interval and then zooms in on the lower-energy windows0–1010MeV and1010–2020MeV, where the dominant peaks are located.
On the full interval, evenm=50m=50captures the broad distribution of strength.
The zoomed views, however, show thatm=50m=50can miss some peak heights and local structure, whereasm=100m=100gives visibly better agreement with the GMRES reference.
The pointwise absolute difference in the lower-right panel confirms this convergence trend: increasing the Lanczos dimension from5050to100100reduces the discrepancy throughout the plotted interval.Figure 4:Lanczos approximation of the total Gamow–Teller strength function for112Sn. From upper left to lower right, the panels compare the GMRES frequency-by-frequency reference with Lanczos approximations usingm=50m=50andm=100m=100iterations on the full0–5050MeV interval, on the zoomed intervals0–1010MeV and1010–2020MeV, and through the corresponding pointwise absolute differences from GMRES.

## 150Nd profile convergence.

For the heavy rare-earth nucleus150Nd, we compare Lanczos approximations withm=100m=100andm=200m=200iterations against the GMRES reference.
Figure5first shows the full0–5050MeV interval and then zooms in on the lower-energy windows0–1515MeV and1515–2525MeV, where the dominant peaks are located.
On the full interval,m=100m=100captures the broad distribution of strength, but the zoomed views show visible differences in local peak structure.
Them=200m=200reconstruction gives better agreement with GMRES in these zoomed regions.
Once again, the pointwise absolute difference in the lower-right panel confirms this convergence trend: increasing the Lanczos dimension from100100to200200reduces the discrepancy throughout the plotted interval.Figure 5:Lanczos approximation of the total Gamow–Teller strength function for150Nd. From upper left to lower right, the panels compare the GMRES frequency-by-frequency reference with Lanczos approximations usingm=100m=100andm=200m=200iterations on the full0–5050MeV interval, on the zoomed intervals0–1515MeV and1515–2525MeV, and through the corresponding pointwise absolute differences from GMRES.

## Distribution-level error and runtime.

As an additional distribution-level accuracy measure, we compute the Kullback–Leibler (KL) divergence between the GMRES strength distribution and each Lanczos reconstruction.
Because KL divergence is defined for probability distributions, the strength values on the sampled energy grid are first normalized separately for each nucleus aspj=SjGMRES∑ℓSℓGMRES,qj(m)=SjLanczos,m∑ℓSℓLanczos,m.p_{j}=\frac{S_{j}^{\mathrm{GMRES}}}{\sum_{\ell}S_{\ell}^{\mathrm{GMRES}}},\qquad q_{j}^{(m)}=\frac{S_{j}^{\mathrm{Lanczos},m}}{\sum_{\ell}S_{\ell}^{\mathrm{Lanczos},m}}.(65)

We then evaluateDKL(p∥q(m))=∑jpjlog(pjqj(m)),D_{\mathrm{KL}}\left(p\middle\|q^{(m)}\right)=\sum_{j}p_{j}\log\left(\frac{p_{j}}{q_{j}^{(m)}}\right),(66)

where the GMRES distributionppis treated as the reference, or “true,” distribution for the corresponding nucleus.
The KL divergence is nonnegative and equals zero only when the two normalized distributions agree exactly; smaller values therefore indicate better agreement with the GMRES reference.
The values in Table1provide the same type of convergence evidence for both112Sn and150Nd: increasing the Lanczos dimension substantially reduces the distribution-level discrepancy.
For112Sn, the KL divergence decreases by more than an order of magnitude fromm=50m=50tom=100m=100.
For150Nd, the KL value atm=200m=200is likewise much smaller than the value atm=100m=100, consistent with improved convergence as the Krylov dimension is increased.NucleusLanczos iterationsDKL​(pGMRES∥qLanczos)D_{\mathrm{KL}}(p_{\mathrm{GMRES}}\|q_{\mathrm{Lanczos}})112Snm=50m=502.8958×10−22.8958\times 10^{-2}112Snm=100m=1002.3455×10−32.3455\times 10^{-3}150Ndm=100m=1001.6739×10−21.6739\times 10^{-2}150Ndm=200m=2008.4926×10−48.4926\times 10^{-4}Table 1:KL divergence between the normalized GMRES strength distribution and normalized Lanczos reconstructions for112Sn and150Nd. Smaller values indicate closer agreement with the GMRES reference.

Together, these comparisons isolate the convergence behavior of the Lanczos reconstruction for the two realistic test nuclei.
The runtime comparison in Figure6shows the corresponding efficiency differences among IFAM, GMRES, and Lanczos.
The improved runtime of GMRES relative to IFAM is consistent with its smaller iteration count: for the representativeK=0K=0calculations in Figure3, GMRES requires23472347total iterations for112Sn compared with37813781for IFAM, and37623762for150Nd compared with53365336for IFAM over the range0–5050MeV.
The Lanczos timings can be interpreted through the matvec-equivalent cost model in Section4.1.2.
Including the additional products needed to form the transition amplitudes, anmm-step Lanczos calculation requires6​m6mmatvecs.
Thus, the Lanczos runs used for the timing comparison cost600600matvecs for112Sn withm=100m=100and12001200matvecs for150Nd withm=200m=200.
In the same bookkeeping, IFAM and GMRES require one matvec-equivalent operation per iteration, so the corresponding GMRES costs are23472347and37623762matvecs, respectively.
These estimates explain why Lanczos remains faster than the frequency-by-frequency solvers in Figure6, even though the precise wall-clock speedups also depend on implementation overhead and post-processing costs.Figure 6:Elapsed runtime, in minutes, of IFAM, GMRES, and Lanczos for the Gamow–Teller0–5050MeV strength-function calculations in112Sn and150Nd. The Lanczos timings usem=100m=100for112Sn andm=200m=200for150Nd.

## 5Conclusion

We have presented a symmetric Lanczos framework for approximating charge-changing QRPA strength functions in a matrix-free setting. Starting from the QRPA linear-response equation and passing through eigendecomposition-based and reduced-eigenproblem formulations, we obtained a representation of the strength function that is well suited to Krylov projection. The resulting method differs conceptually from conventional frequency-by-frequency FAM calculations in that a single Lanczos run captures spectral information across an entire energy interval.

The numerical experiments show that GMRES provides an efficient frequency-by-frequency reference for the medium-mass and heavy nuclei considered here, reproducing converged IFAM strength profiles while requiring fewer iterations. Against this reference, the Lanczos approximation reproduces the same overall Gamow–Teller strength profiles for112Sn and150Nd while requiring substantially fewer matvec-equivalent operations.

Taken together, these results indicate that the symmetric Lanczos method provides a practical alternative for QRPA strength-function calculations when broad spectral information is needed. The approach is especially attractive for deformed and heavy nuclei, where explicit QRPA matrices are too large to build and repeated frequency-by-frequency solves become expensive. Natural directions for future work include extending the method to additional external fields, refining the implementation of the reduced problem, and exploring larger systematic calculations in realistic nuclear-structure applications.

## References
- [1]P. Avogadro and T. Nakatsukasa(2011)Finite amplitude method for the quasiparticle random-phase approximation.Physical Review C84(1),pp. 014314.External Links:DocumentCited by:§1,§2.1,§2.1,§3.1.1.
- [2]J. Bartel, P. Quentin, M. Brack, C. Guet, and H.-B. Håkansson(1982)Towards a better parametrisation of skyrme-like effective forces: a critical study of the skm force.Nuclear Physics A386(1),pp. 79–100.External Links:DocumentCited by:§4.
- [3]A. Bjelčić, T. Nikšić, and Z. Drmač(2022)Chebyshev kernel polynomial method for efficient calculation of the quasiparticle random phase approximation response function.Computer Physics Communications280,pp. 108477.External Links:DocumentCited by:§1,§2.3.
- [4]A. Bjelčić and N. Schunck(2025)Computing the QRPA level density with the finite amplitude method.Computer Physics Communications306,pp. 109387.External Links:DocumentCited by:§1.
- [5]J. Brabec, L. Lin, M. Shao, N. Govind, C. Yang, Y. Saad, and E. G. Ng(2015)Efficient algorithms for estimating the absorption spectrum within linear response TDDFT.Journal of Chemical Theory and Computation11(11),pp. 5197–5208.External Links:DocumentCited by:§1,§2.4.
- [6]C. G. Broyden(1965)A class of methods for solving nonlinear simultaneous equations.Mathematics of Computation19(92),pp. 577–593.External Links:DocumentCited by:§3.1.1.
- [7]J. Engel and J. Menéndez(2017)Status and future of nuclear matrix elements for neutrinoless double-beta decay: a review.Reports on Progress in Physics80(4),pp. 046301.External Links:DocumentCited by:§1.
- [8]N. Hinohara, M. Kortelainen, and W. Nazarewicz(2013)Low-energy collective modes of deformed superfluid nuclei within the finite-amplitude method.Physical Review C87(6),pp. 064309.External Links:DocumentCited by:§1,§2.1.
- [9]C. Lanczos(1950)An iteration method for the solution of the eigenvalue problem of linear differential and integral operators.Journal of Research of the National Bureau of Standards45(4),pp. 255–282.External Links:DocumentCited by:§3.2.
- [10]L. Lin, Y. Saad, and C. Yang(2016)Approximating spectral densities of large matrices.SIAM Review58(1),pp. 34–65.External Links:DocumentCited by:§1,§4.1.1.
- [11]P. Marević, N. Schunck, E. M. Ney, R. Navarro Pérez, M. Verrière, and J. O’Neal(2022)Axially-deformed solution of the skyrme-hartree–fock–bogoliubov equations using the transformed harmonic oscillator basis (iv) hfbtho (v4.0): a new version of the program.Computer Physics Communications276,pp. 108367.External Links:DocumentCited by:§4.
- [12]M.T. Mustonen, T. Shafer, Z. Zenginerler, and J. Engel(2014)Finite-amplitude method for charge-changing transitions in axially deformed nuclei.Physical Review C90(2),pp. 024308.External Links:DocumentCited by:§1,§2.1,§2.1,§3.1.1,§4.
- [13]T. Nakatsukasa, T. Inakura, and K. Yabana(2007)Finite amplitude method for the solution of the random-phase approximation.Physical Review C76(2),pp. 024318.External Links:DocumentCited by:§1.
- [14]T. Nakatsukasa, K. Matsuyanagi, M. Matsuo, and K. Yabana(2016)Time-dependent density-functional description of nuclear dynamics.Reviews of Modern Physics88(4),pp. 045004.External Links:DocumentCited by:§1.
- [15]E. M. Ney, J. Engel, T. Li, and N. Schunck(2020)Global description ofβ−\beta^{-}decay with the axially deformed skyrme finite-amplitude method: extension to odd-mass and odd-odd nuclei.Physical Review C102(3),pp. 034326.External Links:DocumentCited by:§1,§4.
- [16]P. Ring and P. Schuck(1980)The nuclear many-body problem.Theoretical and Mathematical Physics,Springer Berlin Heidelberg.External Links:DocumentCited by:§1,§2.1,§2.1,§2.2,§2.4.
- [17]Y. Saad and M. H. Schultz(1986)GMRES: a generalized minimal residual algorithm for solving nonsymmetric linear systems.SIAM Journal on Scientific and Statistical Computing7(3),pp. 856–869.External Links:DocumentCited by:§3.1.2.
- [18]M. Shao, F. H. da Jornada, C. Yang, J. Deslippe, and S. G. Louie(2016)Structure preserving parallel algorithms for solving the Bethe–Salpeter eigenvalue problem.Linear Algebra and its Applications488,pp. 148–167.External Links:DocumentCited by:§2.3.
- [19]J. Toivanen, B.G. Carlsson, J. Dobaczewski, K. Mizuyama, R.R. Rodríguez-Guzmán, P. Toivanen, and P. Veselỳ(2010)Linear response strength functions with iterative Arnoldi diagonalization.Physical Review C81(3),pp. 034312.External Links:DocumentCited by:§1,§3.2.

## 


- 


Major funding support from
