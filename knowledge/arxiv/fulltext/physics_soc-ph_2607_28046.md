# Inferring Coupling Strengths in Synchronized Oscillators

**arXiv ID**: 2607.28046v1
**Authors**: Gug Young Kim, Hoseok Sul, Jee Woong Choi, Seung-Woo Son
**Published**: 2026-07-30
**Categories**: physics.soc-ph, nlin.AO
**Comments**: 11 pages, 6 figures. Submitted to the Journal of the Korean Physical Society
**HTML URL**: https://arxiv.org/html/2607.28046v1

## Abstract

Accurately estimating the coupling strength in oscillator networks from macroscopic observations alone is essential for predicting synchronization transitions. We consider the inverse problem of reconstructing the unknown coupling strength $K$ in the globally coupled Kuramoto model from scalar observations of the macroscopic order parameter $R(t)$, assuming that the natural frequencies and the initial phase configuration are known. This problem is motivated by practical situations in which individual oscillator phases are inaccessible, whereas a coarse-grained collective signal can be measured continuously. Rather than relying on microscopic state observations, our method infers the coupling strength solely from the evolution of the macroscopic order parameter. We employ an extended Kalman filter with an augmented state representation that recursively estimates the coupling strength from observations of $R(t)$. By exploiting the mean-field structure of the globally coupled Kuramoto model, the covariance prediction step can be computed efficiently, substantially reducing the computational cost. Numerical simulations demonstrate that the proposed estimator accurately reconstructs the coupling strength and remains stable even when $R(t)$ is small and strongly fluctuating.

## Full Text

Inferring Coupling Strengths in Synchronized Oscillators

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.28046v1 [physics.soc-ph] 30 Jul 2026

]Received

## Inferring Coupling Strengths in Synchronized OscillatorsGug Young KimDepartment of Applied Physics, Hanyang University, Ansan, 15588, Republic of KoreaHoseok SulDepartment of Marine Science and Convergence Technology, Hanyang University, Ansan, 15588, Republic of KoreaJee Woong Choijwchoi@hanyang.ac.krSchool of Defense Intelligence and Information Convergence Engineering, Hanyang University, Ansan, 15588, Republic of KoreaSeung-Woo Sonsonswoo@hanyang.ac.krDepartment of Applied Physics, Hanyang University, Ansan, 15588, Republic of Korea([)

## Abstract

Accurately estimating the coupling strength in oscillator networks from macroscopic observations alone is essential for predicting synchronization transitions. We consider the inverse problem of reconstructing the unknown coupling strengthKKin the globally coupled Kuramoto model from scalar observations of the macroscopic order parameterR​(t)R(t), assuming that the natural frequencies and the initial phase configuration are known. This problem is motivated by practical situations in which individual oscillator phases are inaccessible, whereas a coarse-grained collective signal can be measured continuously. Rather than relying on microscopic state observations, our method infers the coupling strength solely from the evolution of the macroscopic order parameter. We employ an extended Kalman filter with an augmented state representation that recursively estimates the coupling strength from observations ofR​(t)R(t). By exploiting the mean-field structure of the globally coupled Kuramoto model, the covariance prediction step can be computed efficiently, substantially reducing the computational cost. Numerical simulations demonstrate that the proposed estimator accurately reconstructs the coupling strength and remains stable even whenR​(t)R(t)is small and strongly fluctuating.Inverse problem, extended Kalman filter, Kuramoto model, parameter estimation

## IIntroduction

Synchronization is a ubiquitous collective phenomenon observed in a wide range of natural and engineered systems, including biological rhythms, chemical oscillators, power grids, and coupled nonlinear oscillators. Since the pioneering studies of Winfree and Kuramoto, the Kuramoto model has served as a paradigmatic framework for describing how microscopic phase interactions give rise to macroscopic synchronization transitionsWinfree1967;Kuramoto1975;Strogatz2000;Acebron2005;Rodrigues2016. In the standard forward problem, the microscopic parameters of the oscillator population, such as the natural frequencies and coupling strength, are given, and the resulting macroscopic order parameter is predicted. In contrast, the inverse problem considered here asks whether an unknown microscopic interaction parameter can be inferred from limited macroscopic observations.

Estimating the coupling strength of a synchronized oscillator population is particularly important because it determines the onset and stability of collective coherence.
Moreover, in oscillator systems with effective inertia, the coupling strength can also delimit oscillatory regimes of global synchrony induced by secondary synchronized clustersKim2026CSF. Existing inference approaches using microscopic time-series data, such as the phases or signals of individual oscillators, can reconstruct phase dynamics, coupling functions, or network connectivityTimme2007;Kralemann2011;Tirabassi2015. Such approaches are powerful but require access to sufficiently resolved individual oscillator trajectories.

In many experimental or large-scale oscillator populations, individual phase trajectories are not always directly accessible after the initial preparation or calibration stage, whereas a coarse-grained collective signal can still be measured. An example is provided by populations of coupled electrochemical oscillators, where the Kuramoto order parameter has been extracted from global measurements rather than from the complete time series of all individual oscillatorsZhai2005. Similar observation constraints can arise in biological oscillator populations such as circadian systems, where the dynamics of many coupled cellular oscillators are often represented or reduced at the macroscopic levelHannay2018;Schmal2018. These examples motivate the macroscopic-observation setting considered in this study: after initialization, the microscopic phases are treated as hidden variables, and only the scalar order parameter is supplied to the estimator.

Macroscopic approaches to coupling-strength estimation often rely on the relaxation dynamics of the order parameter near a synchronized state. In such cases, the coupling strengthKKcan be inferred from the characteristic relaxation time following a perturbation. However, this strategy is intrinsically restricted to regimes where a stable synchronized state exists. For the Kuramoto model with a unimodal frequency distribution, the thermodynamic-limit order parameter vanishes below the critical coupling strengthKcK_{c}Acebron2005;Dorfler2011. Consequently, forK<KcK<K_{c}, conventional macroscopic relaxation-based methods lose the deterministic signal associated with synchronization. In finite-size systems, the order parameter does not vanish identically but exhibits sample-dependent temporal fluctuationsHong2015. These fluctuations are usually regarded as finite-size noise, yet they may still encode some information about the underlying coupling strength when combined with a dynamical model.

Recent studies have also explored parameter estimation from macroscopic quantities and data-assimilation approaches for coupled oscillator systemsKato2025;SmithGottwald2025. These works demonstrate the growing interest in inferring hidden parameters of oscillator systems from limited observations. In contrast to Bayesian approaches based on macroscopic order-parameter trajectories or data-assimilation methods using partial microscopic observations, the present study develops a recursive extended Kalman filter (EKF) based estimator that uses only the scalar order parameterR​(t)R(t)after initialization.

Here we propose an EKF frameworkKalman1960;Jazwinski1970for estimating the unknown coupling strengthKKfrom the scalar macroscopic observationR​(t)R(t). We assume that the natural frequencies and the initial phase configuration are known at the initialization stage, while the true coupling strength is unknown. After initialization, the microscopic phase trajectories are not observed, only the time series of the scalar order parameter is received. By recursively propagating the microscopic state estimate and correcting it usingR​(t)R(t), the EKF extracts hidden dynamical correlations between finite-size order-parameter fluctuations and the coupling strength.

A direct EKF implementation for anNN-oscillator system is computationally expensive because the covariance prediction step involves dense matrix multiplications with cubic complexity. To overcome this limitation, we exploit the mean-field structure of the globally coupled Kuramoto model. We show that the phase-interaction block of the Jacobian can be exactly decomposed into a diagonal component and a rank-2 perturbation. This structure allows the covariance prediction to be evaluated using matrix-vector products and vector outer products, reducing the leading computational cost from𝒪​(N3)\mathcal{O}(N^{3})to𝒪​(N2)\mathcal{O}(N^{2}). Numerical simulations demonstrate that the proposed method can estimateKKusing only macroscopic observations and remains bounded even in the subcritical regime, where the order parameter is dominated by finite-size fluctuations.

In this study, we restrict our analysis to the idealized noiseless-observation setting, in which the scalar observationzkz_{k}coincides exactly with the simulated order parameterR​(t)R(t). This choice allows us to isolate and characterize the intrinsic information content of finite-size order-parameter fluctuations for coupling-strength inference, independent of measurement-noise effects. A systematic study of robustness to observation noise is left for future work.

The remainder of this paper is organized as follows. Section II defines the globally coupled Kuramoto model and the macroscopic-observation setting, and formulates the EKF state-space model using an augmented state vector. Section III exploits the mean-field structure of the model to decompose the phase-interaction block of the Jacobian exactly into a diagonal component and a rank-2 perturbation. Section IV presents numerical results, including representative estimation trajectories, ensemble-level accuracy and its relation to finite-size order-parameter fluctuations, and a computational benchmark demonstrating the efficiency of the rank-2 update. Finally, Section V summarizes the findings and discusses the limitations of the present framework together with directions for future work.

## IIProblem Setup and State-Space FormulationFigure 1:Schematic illustration of the EKF-based coupling-strength inference.
The initial phases and natural frequencies are assumed to be known, while the coupling strengthKtrueK_{\mathrm{true}}is unknown.
After initialization, only the scalar order parameterzk=R​(tk)z_{k}=R(t_{k})is observed.
The EKF internally propagates the microscopic phase estimates and recursively updates the
coupling-strength estimateK^​(t)\hat{K}(t).

We consider a population ofNNglobally coupled phase oscillators described by the Kuramoto model,θ˙i=ωi+KtrueN​∑j=1Nsin⁡(θj−θi),i=1,…,N,\dot{\theta}_{i}=\omega_{i}+\frac{K_{\mathrm{true}}}{N}\sum_{j=1}^{N}\sin(\theta_{j}-\theta_{i}),\qquad i=1,\ldots,N,(1)

whereθi​(t)\theta_{i}(t)andωi\omega_{i}denote the phase and natural frequency of theii-th oscillator, respectively. The parameterKtrueK_{\mathrm{true}}is the true coupling strength to be inferred.
The complex Kuramoto order parameter quantifies the collective synchronization state,Z​(t)=R​(t)​ei​Ψ​(t)=1N​∑j=1Nei​θj​(t),Z(t)=R(t)e^{\mathrm{i}\Psi(t)}=\frac{1}{N}\sum_{j=1}^{N}e^{\mathrm{i}\theta_{j}(t)},(2)

whereR​(t)∈[0,1]R(t)\in[0,1]measures the degree of phase coherence andΨ​(t)\Psi(t)is the mean phase. Equivalently, by definingX​(t)=1N​∑j=1Ncos⁡θj​(t),Y​(t)=1N​∑j=1Nsin⁡θj​(t),X(t)=\frac{1}{N}\sum_{j=1}^{N}\cos\theta_{j}(t),\qquad Y(t)=\frac{1}{N}\sum_{j=1}^{N}\sin\theta_{j}(t),(3)

the scalar order parameter is written asR​(t)=X2​(t)+Y2​(t)R(t)=\sqrt{X^{2}(t)+Y^{2}(t)}.

The inverse problem considered here is to estimateKtrueK_{\mathrm{true}}from the scalar macroscopic time seriesR​(t)R(t). We assume that the natural frequencies and the microscopic initial phase configuration are known at the initialization stage,θ^i,0=θi​(0)\hat{\theta}_{i,0}=\theta_{i}(0),ω^i=ωi\hat{\omega}_{i}=\omega_{i},
whereas the coupling strength is unknown and the estimator is initialized with an incorrect value,K^0=Kinit≠Ktrue\hat{K}_{0}=K_{\mathrm{init}}\neq K_{\mathrm{true}}.
After initialization, the microscopic phase trajectoriesθi​(t)\theta_{i}(t)are not observed. The only information supplied to the estimator is the scalar order parameter sampled at discrete times,zk=R​(tk)z_{k}=R(t_{k}).
Thus, the estimator must infer the hidden coupling strength by propagating the microscopic phase estimates internally and comparing the predicted macroscopic order parameter with the observed scalar signal.

To formulate the estimation problem, we introduce the augmented state vectorxk=[θ1,k,θ2,k,…,θN,k,Kk]T.x_{k}=\left[\theta_{1,k},\theta_{2,k},\ldots,\theta_{N,k},K_{k}\right]^{T}.(4)

In the EKF prediction model, the phase dynamics are discretized using the Euler method with time stepΔ​t\Delta t,θi,k+1=θi,k+Δ​t​[ωi+Kk​(Yk​cos⁡θi,k−Xk​sin⁡θi,k)],\theta_{i,k+1}=\theta_{i,k}+\Delta t\left[\omega_{i}+K_{k}\left(Y_{k}\cos\theta_{i,k}-X_{k}\sin\theta_{i,k}\right)\right],(5)

whereXk=1N​∑j=1Ncos⁡θj,k,Yk=1N​∑j=1Nsin⁡θj,k.X_{k}=\frac{1}{N}\sum_{j=1}^{N}\cos\theta_{j,k},\qquad Y_{k}=\frac{1}{N}\sum_{j=1}^{N}\sin\theta_{j,k}.(6)

The coupling strength is treated as a static but unknown parameter and is modeled as a random walk,Kk+1=Kk+ηk,ηk∼𝒩​(0,QK).K_{k+1}=K_{k}+\eta_{k},\qquad\eta_{k}\sim\mathcal{N}(0,Q_{K}).(7)

The corresponding observation model iszk=Rk+ϵk,where​Rk=Xk2+Yk2,ϵk∼𝒩​(0,Rc).z_{k}=R_{k}+\epsilon_{k},\qquad{\rm where}~~~R_{k}=\sqrt{X_{k}^{2}+Y_{k}^{2}},~~\epsilon_{k}\sim\mathcal{N}(0,R_{c}).(8)

In the synthetic-data experiments below, the observation noise was set to zero, so thatzkz_{k}corresponds directly to the sampled order parameterR​(tk)R(t_{k}). Because the goal of this study is to determine whetherKtrueK_{\rm true}can be recovered from the intrinsic finite-size fluctuations ofR​(t)R(t)under ideal measurement conditions, we set the observation noise to zero throughout the numerical experiments (Rc=0R_{c}=0). The general noisy observation model of Eq. (8), together with the corresponding EKF update equations in Appendix A, is retained in full generality and provides a direct basis for extending the present framework to noisy measurements in future work.
In the numerical experiments, the true Kuramoto dynamics used to generateR​(tk)R(t_{k})are integrated using a fourth-order Runge–Kutta method. In contrast, the EKF uses the Euler-discretized state-space model in Eq. (5) for prediction. The detailed EKF prediction and measurement-update equations are summarized in Appendix A.

Figure1provides a schematic summary of the estimation setup described above. The initial oscillator phases and natural frequencies are assumed to be known and are supplied to the EKF at initialization, whereas the true coupling strengthKtrueK_{\rm true}remains unknown. After this initialization stage, the filter no longer has access to the individual phase trajectories; instead, it receives only the scalar order-parameter observationszk=R​(tk)z_{k}=R(t_{k})at each time step. Internally, the EKF propagates its estimate of the microscopic phase configuration forward using the state-space model and uses the mismatch between the predicted and observed order parameter to recursively correct both the phase estimates and the coupling-strength estimateK^​(t)\hat{K}(t), as illustrated by the feedback loop in the figure.

## IIILow-Rank EKF for Globally Coupled Oscillators

A direct implementation of the EKF for the augmented state𝐱k=[θ1,k,…,θN,k,Kk]T\mathbf{x}_{k}=[\theta_{1,k},\ldots,\theta_{N,k},K_{k}]^{T}requires the prediction of the covariance matrix in Appendix A,Pk|k−1=Fk−1​Pk−1|k−1​Fk−1T+Q.P_{k|k-1}=F_{k-1}P_{k-1|k-1}F_{k-1}^{T}+Q.(9)

Since the phase variables are globally coupled, the Jacobian matrixFkF_{k}is generally dense.
A naive evaluation of this covariance prediction therefore requires dense matrix-matrix multiplications, leading to a computational cost of𝒪​(N3)\mathcal{O}(N^{3}).
This cubic scaling becomes a serious bottleneck when the number of oscillators is large.

The mean-field structure of the globally coupled Kuramoto model allows this cost to be reduced.
The Jacobian matrix of the augmented state can be partitioned asFk=[Ak𝐛k𝟎T1],F_{k}=\begin{bmatrix}A_{k}&\mathbf{b}_{k}\\
\mathbf{0}^{T}&1\end{bmatrix},(10)

whereAk∈ℝN×NA_{k}\in\mathbb{R}^{N\times N}is the phase-interaction block and𝐛k∈ℝN\mathbf{b}_{k}\in\mathbb{R}^{N}is the sensitivity of the phase update with respect toKkK_{k}.
The key observation is thatAkA_{k}is not an arbitrary dense matrix.
By using the mean-field variablesXkX_{k}andYkY_{k}, it can be decomposed exactly into a diagonal component and a rank-2 perturbation,Ak=Dk+α​(𝐜𝐜T+𝐬𝐬T),α=Δ​t​KkN,A_{k}=D_{k}+\alpha\left(\mathbf{c}\mathbf{c}^{T}+\mathbf{s}\mathbf{s}^{T}\right),\qquad\alpha=\frac{\Delta tK_{k}}{N},(11)

where𝐜=(cos⁡θ1,k,…,cos⁡θN,k)T\mathbf{c}=(\cos\theta_{1,k},\ldots,\cos\theta_{N,k})^{T}and𝐬=(sin⁡θ1,k,…,sin⁡θN,k)T\mathbf{s}=(\sin\theta_{1,k},\ldots,\sin\theta_{N,k})^{T}.
The diagonal matrixDkD_{k}contains the self-derivative contribution of the phase update.

This rank-2 structure makes it unnecessary to form and multiply the full dense Jacobian.
Terms such asAk​Pθ​θ,k−1​AkTA_{k}P_{\theta\theta,k-1}A_{k}^{T}can be evaluated using matrix-vector products, scalar contractions, and vector outer products.
As a result, the leading computational cost of the covariance prediction is reduced from𝒪​(N3)\mathcal{O}(N^{3})to𝒪​(N2)\mathcal{O}(N^{2}).
The detailed derivation of the Jacobian elements and the rank-2 covariance prediction is provided in Appendix B.

## IVNumerical ResultsFigure 2:Representative tracking dynamics forKtrue=1K_{\mathrm{true}}=1,22, and33withN=200N=200.
Panels (a), (d), and (g) show the observed order parameterR​(t)R(t).
Panels (b), (e), and (h) show the early evolution of the coupling-strength estimateK^​(t)\hat{K}(t)during the first ten EKF update steps.
Panels (c), (f), and (i) show the absolute estimation error|K^​(t)−Ktrue||\hat{K}(t)-K_{\mathrm{true}}|on a logarithmic scale.
The horizontal dashed lines in the middle column indicate the corresponding true coupling strengthsKtrueK_{\mathrm{true}}.
The estimator remains bounded in the fluctuating regime atKtrue=1K_{\mathrm{true}}=1, while it converges more accurately for larger coupling strengths.

We numerically evaluated the proposed EKF-based estimator using synthetic data generated from the Kuramoto model.
The true Kuramoto dynamics were integrated using a fourth-order Runge–Kutta method with time stepΔ​t=0.01\Delta t=0.01.
The natural frequencies were sampled from a standard Gaussian distribution,ωi∼𝒩​(0,1)\omega_{i}\sim\mathcal{N}(0,1),
and the initial phases were sampled independently from a uniform distribution,θi​(0)∼U​[0,2​π)\theta_{i}(0)\sim U[0,2\pi).
This choice gives a disordered initial condition withR​(0)≈0R(0)\approx 0.
Unless otherwise stated, the representative tracking and ensemble-estimation experiments were performed withN=200N=200oscillators.
For the standard Gaussian distribution,g​(ω)=exp⁡(−ω2/2)/2​πg(\omega)=\exp\left(-{\omega^{2}}/{2}\right)/{\sqrt{2\pi}},
the critical coupling in the thermodynamic limit isKc=2/π​g​(0)=8/π≃1.596K_{c}={2}/{\pi g(0)}=\sqrt{{8}/{\pi}}\simeq 1.596.

In the estimation procedure, the natural frequencies and the initial phase configuration were supplied to the EKF, whereas the coupling strength was initialized with an incorrect valueKinit≠KtrueK_{\rm init}\neq K_{\rm true}.
After initialization, only the scalar order-parameter time seriesR​(tk)R(t_{k})was used for measurement updates.
The EKF prediction step used the Euler-discretized state-space model in Eq. (5). Full details of the covariance initialization, process-noise settings, and the projection bound onK^\hat{K}are given in Appendix C.
Unless otherwise stated, the simulations were performed using the no-lock version of the EKF, in whichK^\hat{K}is updated continuously throughout the entire time interval without applying a freeze or locking condition.

Figure2shows representative estimation trajectories forKtrue=1,2,K_{\mathrm{true}}=1,2,and33, corresponding respectively to subcritical, intermediate, and strongly synchronized regimes relative toKc≃1.596K_{c}\simeq 1.596.
In all cases, the EKF was initialized with the correct microscopic initial phases and natural frequencies but with an incorrect initial estimate ofKK.
After initialization, only the scalar time seriesR​(tk)R(t_{k})was supplied to the filter.

ForKtrue=1K_{\mathrm{true}}=1, the order parameter remains small and fluctuating, but the estimated coupling strength remains bounded.
For larger coupling strengths, the macroscopic signal becomes more coherent and the residual estimation error decreases more rapidly.
These results indicate that the EKF can extract information aboutKtrueK_{\mathrm{true}}not only from strongly synchronized trajectories but also from finite-size fluctuations in the weakly synchronized or subcritical regime. A representative example of the underlying microscopic phase-tracking accuracy is shown in Appendix D, where the estimated and true phase trajectories remain closely aligned even though only the scalar order parameterR​(t)R(t)is observed after initialization.”

To evaluate the statistical performance of the estimator, we performed ensemble simulations over different realizations of the initial phases and natural frequencies.
For each realization, the final estimate was defined as the temporal median ofK^​(t)\hat{K}(t)over the final observation windowWW,K^f=mediant∈W​K^​(t)\hat{K}_{\rm f}={\rm median}_{t\in W}\,\hat{K}(t).
The residual estimation error was then measured asEK=|K^f−Ktrue|E_{K}=|\hat{K}_{\rm f}-K_{\rm true}|.
The fluctuation amplitude of the order parameter was measured over the same windowWWasσR=⟨R2​(t)⟩t∈W−⟨R​(t)⟩t∈W2.\sigma_{R}=\sqrt{\left\langle R^{2}(t)\right\rangle_{t\in W}-\left\langle R(t)\right\rangle_{t\in W}^{2}}.(12)Figure 3:Finite-size macroscopic behavior of a globally coupled Kuramoto system withN=200N=200oscillators as a function of the true coupling strengthKtrueK_{\mathrm{true}}.
(a) Ensemble distribution of the time-averaged order parameter⟨R⟩t\langle R\rangle_{t}.
(b) Ensemble distribution of the fluctuation amplitudeσR\sigma_{R}evaluated over the same observation window. The inset showsσR\sigma_{R}on a logarithmic scale. The vertical dotted line marks the thermodynamic critical couplingKc≃1.596K_{c}\simeq 1.596. The order-parameter fluctuations are enhanced near the synchronization transition and remain finite in the subcritical regime, indicating that the scalar trajectoryR​(t)R(t)retains a nontrivial finite-size signal even below the synchronization threshold.Figure 4:Ensemble statistics of the coupling-strength estimation forN=200N=200.
(a) Distribution of the residual estimation error,EK=|K^f−Ktrue|E_{K}=|\hat{K}_{\rm f}-K_{\mathrm{true}}|,
as a function of the true coupling strengthKtrueK_{\mathrm{true}},
whereK^f\hat{K}_{\rm f}is defined as the temporal median ofK^​(t)\hat{K}(t)over the final observation window.
The error is shown on a logarithmic scale. Zero-error cases, if any, are excluded from the logarithmic visualization.
Each box represents the interquartile range, the red line indicates the median,
and open circles denote outliers.
The vertical dotted line marks the critical couplingKc≃1.596K_{c}\simeq 1.596.
(b) Relation between the order-parameter fluctuationσR\sigma_{R}and the residual estimation errorEKE_{K}.
Both axes are shown on logarithmic scales.
The color scale indicates the number of samples in each hexagonal bin,
and white regions correspond to bins with no samples.
Smaller fluctuations ofR​(t)R(t)are generally associated with smaller residual estimation errors,
whereas larger fluctuations lead to broader error distributions.

To characterize the macroscopic signal available to the estimator, we first examine the finite-size dynamics of the order parameter itself.
Figure3shows the ensemble distribution of the time-averaged order parameter⟨R⟩t\langle R\rangle_{t}and its fluctuation amplitudeσR\sigma_{R}for a finite-size Kuramoto system withN=200N=200oscillators, as functions of the true coupling strengthKtrueK_{\mathrm{true}}.
As expected,⟨R⟩t\langle R\rangle_{t}increases across the synchronization transition near the thermodynamic critical couplingKc≃1.596K_{c}\simeq 1.596.
For finiteNN, however, the order parameter does not vanish identically belowKcK_{c}but exhibits realization-dependent fluctuations.
These fluctuations become most pronounced near the transition point, where the susceptibility of the macroscopic state to finite-size effects is largest, and are strongly suppressed in the synchronized regime.
The presence of these finite-size fluctuations motivates the subsequent estimation analysis, where the EKF attempts to inferKtrueK_{\mathrm{true}}from the scalar trajectoryR​(t)R(t)even below the synchronization threshold.

Figure4summarizes the ensemble statistics.
The residual error remains bounded over the range ofKtrueK_{\rm true}, and smaller fluctuations ofR​(t)R(t)are generally associated with smaller residual estimation errors.
This relation suggests that finite-size order-parameter fluctuations, although small, still contain information about the underlying coupling strength when the initial microscopic state is known.

Finally, we tested the computational advantage of the rank-2 covariance prediction.
For the computational benchmark,NNwas varied to evaluate the scaling of the dense and rank-2 covariance prediction schemes.
Figure5compares the normalized computation time per EKF step for the dense covariance update and the proposed rank-2 update.
The normalized time is defined asT~​(N)=Tstep​(N)/Tdense​(Nref)\tilde{T}(N)={T_{\rm step}(N)}/{T_{\rm dense}(N_{\rm ref})},
whereNref=103N_{\rm ref}=10^{3}.
We also measured the speedup ratioST​(N)=Tdense​(N)/Trank​-​2​(N)S_{T}(N)={T_{\rm dense}(N)}/{T_{\rm rank\text{-}2}(N)}.
Although the absolute clock time depends on the implementation and hardware, the increasing speedup ratio in the large-NNregime provides empirical support for the theoretical reduction of the covariance prediction cost from𝒪​(N3)\mathcal{O}(N^{3})to𝒪​(N2)\mathcal{O}(N^{2}).
The nonmonotonic behavior at smallNNreflects implementation-dependent overheads.Figure 5:Computational scalability of the covariance-update step in the EKF.
(a) Normalized computation time per EKF step,T~​(N)=Tstep​(N)/Tdense​(Nref)\tilde{T}(N)=T_{\mathrm{step}}(N)/T_{\mathrm{dense}}(N_{\mathrm{ref}}),
for the dense covariance update and the proposed rank-2 update.
Here,Nref=103N_{\mathrm{ref}}=10^{3}.
(b) Computational speedup,ST​(N)=Tdense​(N)/Trank​-​2​(N)S_{T}(N)=T_{\mathrm{dense}}(N)/T_{\mathrm{rank\text{-}2}}(N).
The dashed line indicatesST=1S_{T}=1.
The nonmonotonic behavior at smallNNreflects implementation-dependent overheads,
whereas the increasing trend in the large-NNregime demonstrates the computational advantage of the rank-2 update.

## VDiscussion and Conclusion

In this study, we demonstrated that an Extended Kalman Filter (EKF) framework can efficiently estimate the coupling strength of a finite-size Kuramoto network using solely the scalar macroscopic observationR​(t)R(t), provided the initial microscopic phase configuration and natural frequencies are known. The estimator rapidly corrects an incorrect initial estimate ofKKand remains bounded even in the subcritical regime, highlighting that finite-size fluctuations of the order parameter contain decodable information about the underlying coupling interactions. Furthermore, by rigorously deriving a rank-2 block covariance prediction of the Jacobian matrix, we reduced the computational complexity from𝒪​(N3)\mathcal{O}(N^{3})to𝒪​(N2)\mathcal{O}(N^{2}). This provides a scalable foundation for tracking macroscopic-to-microscopic parameter inference in complex coupled systems.

The present framework assumes that the initial microscopic phase configuration and natural frequencies are known, which allows the filter to propagate a microscopic state estimate even though only the scalar order parameter is observed thereafter. We note that this assumption is comparatively mild for the Kuramoto model, because the coupling term drives trajectories toward the synchronized manifold onceK>KcK>K_{c}, and because the filter is corrected at every step by the aggregate signalR​(t)R(t)rather than by individual phases, small deviations in the assumed initial condition are expected to affect mainly the transient phase-tracking error rather than the long-time bias ofK^​(t)\hat{K}(t). The coupling-strength estimate is therefore expected to be comparatively insensitive to moderate initial-condition uncertainty, unlike methods that depend on tracking individual oscillator trajectories throughout.

The present study assumes noiseless macroscopic observations in order to isolate the estimability ofKtrueK_{\rm true}from finite-size fluctuations alone. Extending the estimator to noisy observations, leveraging the general EKF formulation already presented in Appendix A, together with partially known initial states and more general network topologies, remains an important direction for future work.

## Acknowledgements.This work was supported by Korea Research Institute for defense Technology planning and advancement (KRIT) - Grant funded by Defense Acquisition Program Administration (DAPA), South Korea (KRIT-CT-23-026, Integrated Underwater Surveillance Research Center for Adapting Future Technologies, 2023–2029).

## Appendix AEKF Prediction and Measurement Update

The true Kuramoto dynamics used to generate the observation time serieszk=R​(tk)z_{k}=R(t_{k})are integrated using a fourth-order Runge–Kutta method in the numerical simulations.
The Euler-discretized state-space model introduced in the main text
as its internal prediction model. Let the nonlinear process and observation models be𝐱k=f​(𝐱k−1)+𝐰k−1,zk=h​(𝐱k)+ϵk,\mathbf{x}_{k}=f(\mathbf{x}_{k-1})+\mathbf{w}_{k-1},\qquad z_{k}=h(\mathbf{x}_{k})+\epsilon_{k},(13)

where𝐱k=[θ1,k,…,θN,k,Kk]T\mathbf{x}_{k}=[\theta_{1,k},\ldots,\theta_{N,k},K_{k}]^{T}is the augmented state vector,𝐰k−1\mathbf{w}_{k-1}is the process noise, andϵk∼𝒩​(0,Rc)\epsilon_{k}\sim\mathcal{N}(0,R_{c})is the observation noise.
The observation function is given byh​(𝐱k)=Rk=Xk2+Yk2,h(\mathbf{x}_{k})=R_{k}=\sqrt{X_{k}^{2}+Y_{k}^{2}},(14)

whereXk=∑j=1Ncos⁡θj,k/NX_{k}=\sum_{j=1}^{N}\cos\theta_{j,k}/N,Yk=∑j=1Nsin⁡θj,k/NY_{k}=\sum_{j=1}^{N}\sin\theta_{j,k}/N.

The EKF prediction stepKalman1960;Jazwinski1970for state and convariancePkP_{k}is𝐱^k|k−1=f​(𝐱^k−1|k−1),Pk|k−1=Fk−1​Pk−1|k−1​Fk−1T+Qk,\hat{\mathbf{x}}_{k|k-1}=f(\hat{\mathbf{x}}_{k-1|k-1}),\qquad P_{k|k-1}=F_{k-1}P_{k-1|k-1}F_{k-1}^{T}+Q_{k},(15)

whereFk−1=∂f∂𝐱|𝐱^k−1|k−1F_{k-1}=\left.\frac{\partial f}{\partial\mathbf{x}}\right|_{\hat{\mathbf{x}}_{k-1|k-1}}(16)

is the Jacobian matrix of the process model (state transition model) evaluated at the posterior estimate from the previous step.QkQ_{k}relates to the process noise in EKF modelKalman1960;Jazwinski1970.

The measurement update is performed usingνk=zk−h​(𝐱^k|k−1)\nu_{k}=z_{k}-h(\hat{\mathbf{x}}_{k|k-1}).
The Kalman gain is𝒢k=Pk|k−1​HkT​(Hk​Pk|k−1​HkT+Rc)−1,\mathcal{G}_{k}=P_{k|k-1}H_{k}^{T}\left(H_{k}P_{k|k-1}H_{k}^{T}+R_{c}\right)^{-1},(17)

whereHk=∂h∂𝐱|𝐱^k|k−1H_{k}=\left.\frac{\partial h}{\partial\mathbf{x}}\right|_{\hat{\mathbf{x}}_{k|k-1}}(18)

is the observation Jacobian. Since the observation depends only on the phases and not directly onKkK_{k},Hk=[h1,kh2,k⋯hN,k0],H_{k}=\begin{bmatrix}h_{1,k}&h_{2,k}&\cdots&h_{N,k}&0\end{bmatrix},(19)

withhi,k=∂Rk∂θi,k=−Xk​sin⁡θi,k+Yk​cos⁡θi,kN​Rk.h_{i,k}=\frac{\partial R_{k}}{\partial\theta_{i,k}}=\frac{-X_{k}\sin\theta_{i,k}+Y_{k}\cos\theta_{i,k}}{NR_{k}}.(20)

In the nearly incoherent regime,RkR_{k}can become very small. Therefore, in numerical implementation, a small lower bound is imposed onRkR_{k}when evaluating Eq. (20).

The posterior state estimate is updated as𝐱^k|k=𝐱^k|k−1+𝒢k​νk\hat{\mathbf{x}}_{k|k}=\hat{\mathbf{x}}_{k|k-1}+\mathcal{G}_{k}\nu_{k}.
The covariance update can be written in the standard form,Pk|k=(I−𝒢k​Hk)​Pk|k−1.P_{k|k}=(I-\mathcal{G}_{k}H_{k})P_{k|k-1}.(21)

For numerical stability, the Joseph form may also be used:Pk|k=(I−𝒢k​Hk)​Pk|k−1​(I−𝒢k​Hk)T+𝒢k​Rc​𝒢kT.P_{k|k}=(I-\mathcal{G}_{k}H_{k})P_{k|k-1}(I-\mathcal{G}_{k}H_{k})^{T}+\mathcal{G}_{k}R_{c}\mathcal{G}_{k}^{T}.(22)

## Appendix BJacobian and Rank-2 Covariance Prediction

The Jacobian matrix of the augmented state vector is partitioned asFk=[Ak𝐛k𝟎T1],F_{k}=\begin{bmatrix}A_{k}&\mathbf{b}_{k}\\
\mathbf{0}^{T}&1\end{bmatrix},(23)

whereAk∈ℝN×NA_{k}\in\mathbb{R}^{N\times N}is the phase-interaction block and𝐛k∈ℝN\mathbf{b}_{k}\in\mathbb{R}^{N}is the sensitivity of the phase update with respect toKkK_{k}.
For the Euler-discretized prediction model,θi,k+1=θi,k+Δ​t​[ωi+Kk​(Yk​cos⁡θi,k−Xk​sin⁡θi,k)],\theta_{i,k+1}=\theta_{i,k}+\Delta t\left[\omega_{i}+K_{k}\left(Y_{k}\cos\theta_{i,k}-X_{k}\sin\theta_{i,k}\right)\right],(24)

the elements ofAkA_{k}areAi​j=δi​j​[1−Δ​t​Kk​(Xk​cos⁡θi,k+Yk​sin⁡θi,k)]+Δ​t​KkN​(cos⁡θi,k​cos⁡θj,k+sin⁡θi,k​sin⁡θj,k),A_{ij}=\delta_{ij}\left[1-\Delta tK_{k}\left(X_{k}\cos\theta_{i,k}+Y_{k}\sin\theta_{i,k}\right)\right]+\frac{\Delta tK_{k}}{N}\left(\cos\theta_{i,k}\cos\theta_{j,k}+\sin\theta_{i,k}\sin\theta_{j,k}\right),(25)

and the sensitivity vector isbi=∂θi,k+1∂Kk=Δ​t​(Yk​cos⁡θi,k−Xk​sin⁡θi,k).b_{i}=\frac{\partial\theta_{i,k+1}}{\partial K_{k}}=\Delta t\left(Y_{k}\cos\theta_{i,k}-X_{k}\sin\theta_{i,k}\right).(26)

By defining𝐜=[cos⁡θ1,k⋯cos⁡θN,k]T,𝐬=[sin⁡θ1,k⋯sin⁡θN,k]T,\mathbf{c}=\begin{bmatrix}\cos\theta_{1,k}&\cdots&\cos\theta_{N,k}\end{bmatrix}^{T},\qquad\mathbf{s}=\begin{bmatrix}\sin\theta_{1,k}&\cdots&\sin\theta_{N,k}\end{bmatrix}^{T},(27)

the phase-interaction block can be decomposed exactly asAk=Dk+α​(𝐜𝐜T+𝐬𝐬T),α=Δ​t​KkN,A_{k}=D_{k}+\alpha\left(\mathbf{c}\mathbf{c}^{T}+\mathbf{s}\mathbf{s}^{T}\right),\qquad\alpha=\frac{\Delta tK_{k}}{N},(28)

whereDkD_{k}is diagonal with elements(Dk)i​i=1−Δ​t​Kk​(Xk​cos⁡θi,k+Yk​sin⁡θi,k).(D_{k})_{ii}=1-\Delta tK_{k}\left(X_{k}\cos\theta_{i,k}+Y_{k}\sin\theta_{i,k}\right).(29)

Thus, the dense part ofAkA_{k}is not arbitrary but is a rank-2 perturbation of a diagonal matrix.

To exploit this structure in the covariance prediction, we partition the covariance matrix asPk=[Pθ​θ,k𝐩θ​K,k𝐩θ​K,kTPK​K,k].P_{k}=\begin{bmatrix}P_{\theta\theta,k}&\mathbf{p}_{\theta K,k}\\
\mathbf{p}_{\theta K,k}^{T}&P_{KK,k}\end{bmatrix}.(30)

The prior covariance blocks are then updated asPθ​θ,k−\displaystyle P_{\theta\theta,k}^{-}=Ak​Pθ​θ,k−1​AkT+Ak​𝐩θ​K,k−1​𝐛kT+𝐛k​𝐩θ​K,k−1T​AkT+PK​K,k−1​𝐛k​𝐛kT+Qθ​θ,\displaystyle=A_{k}P_{\theta\theta,k-1}A_{k}^{T}+A_{k}\mathbf{p}_{\theta K,k-1}\mathbf{b}_{k}^{T}+\mathbf{b}_{k}\mathbf{p}_{\theta K,k-1}^{T}A_{k}^{T}+P_{KK,k-1}\mathbf{b}_{k}\mathbf{b}_{k}^{T}+Q_{\theta\theta},(31)𝐩θ​K,k−\displaystyle\mathbf{p}_{\theta K,k}^{-}=Ak​𝐩θ​K,k−1+PK​K,k−1​𝐛k,\displaystyle=A_{k}\mathbf{p}_{\theta K,k-1}+P_{KK,k-1}\mathbf{b}_{k},(32)PK​K,k−\displaystyle P_{KK,k}^{-}=PK​K,k−1+QK.\displaystyle=P_{KK,k-1}+Q_{K}.(33)

The dominant term in Eq. (31) isAk​Pθ​θ,k−1​AkTA_{k}P_{\theta\theta,k-1}A_{k}^{T}.
LetP=Pθ​θ,k−1P=P_{\theta\theta,k-1}and omit the time index for clarity. UsingA=D+α​(𝐜𝐜T+𝐬𝐬T),A=D+\alpha(\mathbf{c}\mathbf{c}^{T}+\mathbf{s}\mathbf{s}^{T}),

we obtainA​P​AT=D​P​D+α​∑𝐮∈{𝐜,𝐬}[D​P​𝐮​𝐮T+𝐮​𝐮T​P​D]+α2​∑𝐮,𝐯∈{𝐜,𝐬}𝐮​(𝐮T​P​𝐯)​𝐯T.APA^{T}=DPD+\alpha\sum_{\mathbf{u}\in\{\mathbf{c},\mathbf{s}\}}\left[DP\mathbf{u}\,\mathbf{u}^{T}+\mathbf{u}\,\mathbf{u}^{T}PD\right]+\alpha^{2}\sum_{\mathbf{u},\mathbf{v}\in\{\mathbf{c},\mathbf{s}\}}\mathbf{u}\left(\mathbf{u}^{T}P\mathbf{v}\right)\mathbf{v}^{T}.(34)

The first termD​P​DDPDis evaluated by elementwise multiplication with the diagonal entries ofDD.
The remaining terms require only matrix-vector products such asP​𝐜P\mathbf{c}andP​𝐬P\mathbf{s},
scalar contractions such as𝐜T​P​𝐬\mathbf{c}^{T}P\mathbf{s}, and vector outer products.
Therefore, no dense matrix-matrix multiplication is required, and the covariance prediction step is evaluated with leading computational cost𝒪​(N2)\mathcal{O}(N^{2})instead of𝒪​(N3)\mathcal{O}(N^{3}).

## Appendix CEKF Numerical Implementation Details

The initial covariance matrix was set toPθ​θ,0=10−6​I,PK​K,0=10−2,P_{\theta\theta,0}=10^{-6}I,\qquad P_{KK,0}=10^{-2},

with zero initial cross-covariance between the phase variables andKK.
The process noise covariance was taken to be zero for all phase variables and nonzero only for the coupling-strength component,Qθ​θ=𝟎,QK=10−10.Q_{\theta\theta}=\mathbf{0},\qquad Q_{K}=10^{-10}.

This corresponds to modelingKKas a weak random-walk parameter while treating the phase evolution as deterministic within the EKF prediction model.
Unless otherwise stated, the measurement noise variance was set toRc=0R_{c}=0, so that the scalar observationzkz_{k}corresponds directly to the synthetic order parameterR​(tk)R(t_{k}).
After each measurement update, the estimated parameterK^\hat{K}was projected onto the interval[0,20][0,20].

## Appendix DMicroscopic Phase-Tracking Visualization

To visualize the microscopic phase-tracking performance, we compare the true and estimated phases of individual oscillators.
Since the oscillator phase is periodic, the phase difference is evaluated modulo2​π2\piasΔ​θi​(t)=arg​[ei​(θi​(t)−θ^i​(t))],\Delta\theta_{i}(t)=\mathrm{arg}\left[e^{i(\theta_{i}(t)-\hat{\theta}_{i}(t))}\right],(35)

wherearg​(⋅)∈(−π,π]\mathrm{arg}(\cdot)\in(-\pi,\pi].
FigureC1showsΔ​θi​(t)\Delta\theta_{i}(t)for individual oscillators in a representative case withKtrue=1K_{\mathrm{true}}=1andN=200N=200.
The dashed horizontal lines indicateΔ​θi=±0.03\Delta\theta_{i}=\pm 0.03rad.
Most phase deviations remain within this range over the simulated interval, corresponding to less than1%1\%of the full phase range2​π2\pi.Figure C1:Microscopic phase-tracking visualization of the EKF forKtrue=1K_{\mathrm{true}}=1withN=200N=200.
Each curve represents the phase differenceΔ​θi​(t)\Delta\theta_{i}(t)between the true and estimated phase of an individual oscillator.
The dashed horizontal lines indicateΔ​θi=±0.03\Delta\theta_{i}=\pm 0.03rad.
Although only the scalar order parameterR​(t)R(t)is used for correction after initialization, most phase deviations remain within|Δ​θi|≲0.03|\Delta\theta_{i}|\lesssim 0.03rad over the simulated interval, corresponding to less than1%1\%of the full phase range2​π2\pi.

## References
- (1)A. T. Winfree,
Biological rhythms and the behavior of populations of coupled oscillators,
J. Theor. Biol.16, 15–42 (1967).
- (2)Y. Kuramoto,
Self-entrainment of a population of coupled non-linear oscillators,
inInternational Symposium on Mathematical Problems in Theoretical Physics,
Lecture Notes in Physics, Vol. 39, edited by H. Araki
(Springer, Berlin, Heidelberg, 1975), pp. 420–422.
- (3)S. H. Strogatz,
From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators,
Physica D143, 1–20 (2000).
- (4)J. A. Acebrón, L. L. Bonilla, C. J. Pérez Vicente, F. Ritort, and R. Spigler,
The Kuramoto model: A simple paradigm for synchronization phenomena,
Rev. Mod. Phys.77, 137–185 (2005).
- (5)F. A. Rodrigues, T. K. D. M. Peron, P. Ji, and J. Kurths,
The Kuramoto model in complex networks,
Phys. Rep.610, 1–98 (2016).
- (6)G. Y. Kim, M. J. Lee, and S.-W. Son,
Predicting the oscillatory regimes of global synchrony induced by secondary clusters,
Chaos Solitons Fractals208, 118285 (2026).
- (7)M. Timme,
Revealing network connectivity from response dynamics,
Phys. Rev. Lett.98, 224101 (2007).
- (8)B. Kralemann, A. Pikovsky, and M. Rosenblum,
Reconstructing phase dynamics of oscillator networks,
Chaos21, 025104 (2011).
- (9)G. Tirabassi, R. Sevilla-Escoboza, J. M. Buldú, and C. Masoller,
Inferring the connectivity of coupled oscillators from time-series statistical similarity analysis,
Sci. Rep.5, 10829 (2015).
- (10)Y. Zhai, I. Z. Kiss, H. Daido, and J. L. Hudson,
Extracting order parameters from global measurements with application to coupled electrochemical oscillators,
Physica D205, 57–69 (2005).
- (11)K. M. Hannay, D. B. Forger, and V. Booth,
Macroscopic models for networks of coupled biological oscillators,
Sci. Adv.4, e1701047 (2018).
- (12)C. Schmal, E. D. Herzog, and H. Herzel,
Measuring coupling strength in circadian systems,
J. Biol. Rhythms33, 74–87 (2018).
- (13)F. Dörfler and F. Bullo,
On the critical coupling for Kuramoto oscillators,
SIAM J. Appl. Dyn. Syst.10, 1070–1099 (2011).
- (14)H. Hong, H. Chaté, L.-H. Tang, and H. Park,
Finite-size scaling, dynamic fluctuations, and hyperscaling relation in the Kuramoto model,
Phys. Rev. E92, 022122 (2015).
- (15)Y. Kato, S. Kashiwamura, E. Watanabe, M. Okada, and H. Kori,
Bayesian estimation of coupling strength and heterogeneity in a coupled oscillator model from macroscopic quantities,
Phys. Rev. E112, 034215 (2025).
- (16)L. D. Smith and G. A. Gottwald,
Data assimilation for networks of coupled oscillators: Inferring unknown model parameters from partial observations,
Proc. R. Soc. A481, 20240813 (2025).
- (17)R. E. Kalman,
A new approach to linear filtering and prediction problems,
Trans. ASME J. Basic Eng.82, 35–45 (1960).
- (18)A. H. Jazwinski,Stochastic Processes and Filtering Theory(Academic Press, New York, 1970).

## 


- 


Major funding support from
