# Beyond the Central Limit: Universality of the Gamma Distribution from Padé-Enhanced Large Deviations

**arXiv ID**: 2603.23567v1
**Authors**: Mario Castro, José A. Cuesta
**Published**: 2026-03-24
**Categories**: physics.data-an, cond-mat.stat-mech, math.PR
**Comments**: 5 pages, uses RevTeX4.2, 3 figures (made of 12 subfigures)
**HTML URL**: https://arxiv.org/html/2603.23567v1

## Abstract

The central limit theorem provides the theoretical foundation for the universality of the normal distribution: under broad conditions, the asymptotic distribution of a sum of independent random variables approaches a Gaussian. Yet, physical systems described by positive random variable -- from earthquakes to microbial growth to epidemic spreading -- consistently exhibit gamma rather than Gaussian statistics -- what leads to field-specific mechanistic explanations that are non robust to small changes in the model details. We show that gamma distributions emerge naturally from large deviation theory when Padé approximants replace polynomial expansions of the derivative of the scaled cumulant generating function, respecting positivity constraints that the central limit theorem violates. Gamma universality thus emerges as the constrained analog of Gaussian universality, providing a mechanism-free explanation for its pervasive appearance across different disciplines.

## Full Text

Beyond the Central Limit: Universality of the Gamma Distribution from Padé-Enhanced Large Deviations

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- 
- License: arXiv.org perpetual non-exclusive licensearXiv:2603.23567v1 [physics.data-an] 24 Mar 2026\DeclareMathOperator\He

He

## Beyond the Central Limit: Universality of the Gamma Distribution from Padé-Enhanced Large DeviationsMario CastroInstitute for Research in Technology (IIT), Universidad Pontificia Comillas, Grupo Interdisciplinar de Sistemas Complejos (GISC), Madrid, SpainJosé A. CuestaUniversidad Carlos III de Madrid, Departamento de Matemáticas, Grupo Interdisciplinar de Sistemas Complejos (GISC), Leganés, SpainInstituto de Biocomputación y Física de Sistemas Complejos, Universidad de Zaragoza, Zaragoza, Spain(March 24, 2026)

## Abstract

The central limit theorem provides the theoretical foundation for the universality of the normal distribution: under broad conditions, the asymptotic distribution of a sum of independent random variables approaches a Gaussian. Yet, physical systems described by positive random variable—from earthquakes to microbial growth to epidemic spreading—consistently exhibit gamma rather than Gaussian statistics—what leads to field-specific mechanistic explanations that are non robust to small changes in the model details. We show that gamma distributions emerge naturally from large deviation theory when Padé approximants replace polynomial expansions of the derivative of the scaled cumulant generating function, respecting positivity constraints that the central limit theorem violates. Gamma universality thus emerges as the constrained analog of Gaussian universality, providing a mechanism-free explanation for its pervasive appearance across different disciplines.statistical physics, central limit theorem, gamma distribution, Markov processes, non-identical random variables

A recurring observation in physics is that complex systems often exhibit statistical regularities that are strikingly independent of microscopic details. These regularities—manifested in universal distributions—serve as guiding motifs for theory-building across disciplines. From the Maxwell-Boltzmann distribution in kinetic theory to the Tracy-Widom law in random matrix theoryTracy and Widom (1996), from the Fisher–Tippett–Gnedenko theorem in extreme value statisticsGnedenko (1943)to the ubiquity of power laws in natural and social systemsBouchaud (2001); Stumpf and Porter (2012), such patterns reflect deep structural principles that transcend specific models.

Among these, the normal distribution stands as the canonical example of universality. The central limit theorem (CLT) provides its theoretical foundation: under broad conditions, the sum of independent random variables converges to a Gaussian, enabling robust predictions in diverse contexts. Yet, this universality has limits. In systems where variables are constrained to be positive, exhibit strong heterogeneity, or are few in number, the Gaussian approximation often fails. In these regimes, usually the gamma distribution emerges—not as a statistical curiosity, but as a persistent empirical regularity.

Indeed, gamma-like distributions appear in the interevent times of earthquakesTouatiet al.(2009); Corral (2004), in the fracture dynamics of rocksDavidsenet al.(2007), in microbial growth lawsGrilli (2020); Camacho-Mateuet al.(2025), and in the scaling of phenotypic variability in bacteriaBiswas and Brenner (2024). They also arise in models of viral entryZhang and Dudko (2015), cell divisionBrenner and Shokef (2007), and stochastic exponential growthIyer-Biswaset al.(2014). In each case, mechanistic explanations are sought that are system-specific and may attribute causal explanations; however, a unifying theoretical account might clarify this ubiquity but remains elusive.

The limitations of the CLT in these contexts are well understood: convergence may be slow, higher-order corrections remain significant, and positivity constraints impose qualitative changes in behavior. Large deviation theory (LDT) offers a principled extensionTouchette (2009), but its practical application is often hindered by the difficulty of inverting the rate function to obtain explicit probability densities. Moreover, polynomial approximations of the cumulant generating function (CGF)—which underpin the CLT—can yield invalid densities when higher-order terms are includedButler (2007); Daniels (1954).

In this Letter, we propose a parsimonious and general, yet rigorous, explanation for the emergence of gamma distributions in constrained systems. By applying a Padé approximantBaker Jr (1961)to the scaled CGF within the LDT framework, we derive gamma-like distributions that outperform the normal approximation even for small system sizes and non-identical variables. This approach naturally respects the positivity constraint and captures essential features of the underlying dynamics. We demonstrate its accuracy across a range of scenarios, including sums of exponential variables with heterogeneous rates, trajectories of Markov chains, and the addition of truncated normal and other non-exponential distributions defined on the positive real axis. Furthermore, we show how the theory can be systematically extended to encompass more complex settings, including convolutions of gamma distributions and non-Markovian dynamics.

Our results suggest that the gamma distribution is not merely a convenient fit, but a universal outcome of constrained aggregation processes. This insight has implications for statistical modeling in physics, biology, and beyond, offering a new lens through which to understand the emergence of regularity in complex systems.

## Theory.—

Consider a sequence of random variables𝐗=(X1,X2,…,Xn)\mathbf{X}=(X_{1},X_{2},\dots,X_{n})with support in𝒳\mathcal{X}, and letSn​(𝐗)S_{n}(\mathbf{X})be a function of this sequence (e.g. the sum of the sequence). The probability density of this variable can be obtained as{align*}p_n(x) =∫_Xδ(S_n(X)-x)p(X) dX
=12πi
∫_a-i∞^a+i∞dξe^-ξx
⟨e^ξS_n(X)⟩,

where we have used the Laplace transform representation of Dirac’s delta functionδ​(u)=12​π​i​∫a−i​∞a+i​∞eξ​u​𝑑ξ.\delta(u)=\frac{1}{2\pi i}\int_{a-i\infty}^{a+i\infty}e^{\xi u}\,d\xi.

Let us denoteλn​(ξ)≡1n​log⁡⟨eξ​Sn​(𝐗)⟩.\lambda_{n}(\xi)\equiv\frac{1}{n}\log\left\langle e^{\xi S_{n}(\mathbf{X})}\right\rangle.(1)

Ifλn​(ξ)\lambda_{n}(\xi)has a well defined limit whenn→∞n\to\infty, thenSnS_{n}satisfies a large deviation principleTouchette (2009), and the probability density admits the asymptotic representationpn​(x)∼12​π​i​∫a−i​∞a+i​∞en​[λn​(ξ)−ξ​y]​𝑑ξ(n→∞),p_{n}(x)\sim\frac{1}{2\pi i}\int_{a-i\infty}^{a+i\infty}e^{n[\lambda_{n}(\xi)-\xi y]}\,d\xi\quad(n\to\infty),(2)

wherey≡x/ny\equiv x/n. The integral in Eq.\eqrefeq:pn_vs_lambda can be estimated via the saddle-point methodDaniels (1954), yieldingpn​(x)∼cnλn′′​(ξ∗)​en​[λn​(ξ∗)−ξ∗​y](n→∞),p_{n}(x)\sim\frac{c_{n}}{\sqrt{\lambda^{\prime\prime}_{n}(\xi^{*})}}e^{n[\lambda_{n}(\xi^{*})-\xi^{*}y]}\quad(n\to\infty),(3)

whereξ∗\xi^{*}solves the saddle-point equationn​λn′​(ξ∗)=x,n\lambda^{\prime}_{n}(\xi^{*})=x,(4)

andcnc_{n}is a normalization constant.

The classical central limit theorem (CLT) amounts to making the linear approximationn​λn′​(ξ)≈μn+σn2​ξ,n\lambda^{\prime}_{n}(\xi)\approx\mu_{n}+\sigma^{2}_{n}\xi,(5)

whereμn\mu_{n}andσn2\sigma_{n}^{2}are the mean and variance ofSnS_{n}. Within this approximation and using Eq.\eqrefeq:saddle,n​λn​(ξ)=μn​ξ+σn22​ξ2,ξ∗=x−μnσn2,n\lambda_{n}(\xi)=\mu_{n}\xi+\frac{\sigma^{2}_{n}}{2}\xi^{2},\qquad\xi^{*}=\frac{x-\mu_{n}}{\sigma_{n}^{2}},

wherebyn​λn​(ξ∗)−ξ∗​x=−(x−μn)2/2​σn2n\lambda_{n}(\xi^{*})-\xi^{*}x=-(x-\mu_{n})^{2}/2\sigma_{n}^{2}. Asλn′′​(ξ∗)\lambda_{n}^{\prime\prime}(\xi^{*})is a constant, Eq.\eqrefeq:pnasymp becomes the normal distribution.

Inspired by Baker’s work on Padé approximants in Statistical PhysicsBaker Jr (1961), we propose using rational approximations toλn′​(ξ)\lambda^{\prime}_{n}(\xi). To lowest order, the[0/1][0/1]-Padé approximant becomesn​λn′​(ξ)≈μn1−σn2​ξ/μn.n\lambda_{n}^{\prime}(\xi)\approx\frac{\mu_{n}}{1-\sigma_{n}^{2}\xi/\mu_{n}}.(6)

This approximation offers an advantage over\eqrefeq:Taylor: it is positive in the whole interval of validity of the Padé (ξ<μn/σn2\xi<\mu_{n}/\sigma_{n}^{2})—hence\eqrefeq:saddle yieldsx>0x>0. Thus, for distributions with supportx>0x>0,\eqrefeq:cgfslope provides the lowest-order rational approximation that preserves this constrained support.

Now, from\eqrefeq:cgfslope,n​λn​(ξ)=−μn2σn2​log⁡(1−σn2μn​ξ),ξ∗=μnσn2​(1−μnx),n\lambda_{n}(\xi)=-\frac{\mu_{n}^{2}}{\sigma^{2}_{n}}\log\left(1-\frac{\sigma_{n}^{2}}{\mu_{n}}\xi\right),\quad\xi^{*}=\frac{\mu_{n}}{\sigma_{n}^{2}}\left(1-\frac{\mu_{n}}{x}\right),

and thereforen​λn​(ξ∗)−ξ∗​x=μn2σn2​log⁡(xμn)−μnσn2​x+const.n\lambda_{n}(\xi^{*})-\xi^{*}x=\frac{\mu_{n}^{2}}{\sigma^{2}_{n}}\log\left(\frac{x}{\mu_{n}}\right)-\frac{\mu_{n}}{\sigma_{n}^{2}}x+\text{const.}

Asλn′′​(ξ∗)∝x2\lambda^{\prime\prime}_{n}(\xi^{*})\propto x^{2}, the resulting approximation is the gamma distributionpn(G)​(x)∼cn​(xμn)αn−1​e−αn​x/μn,αn≡μn2σn2.p^{(G)}_{n}(x)\sim c_{n}\left(\frac{x}{\mu_{n}}\right)^{\alpha_{n}-1}e^{-\alpha_{n}x/\mu_{n}},\quad\alpha_{n}\equiv\frac{\mu_{n}^{2}}{\sigma_{n}^{2}}.(7)

This result is exact for sums of independent and identically distributed (i.i.d.) exponential variables—in which case, the resulting gamma distribution is also known as the Erlang distribution.

The fact that\eqrefeq:gamma is a direct consequence of\eqrefeq:cgfslope reveals that gamma’s universality is the natural analog of Gaussian’s universality for distributions with domainx>0x>0.

## Numerical tests.—

To quantify the accuracy of Eq.\eqrefeq:gamma, we compute the Kullback-Leibler divergence (KLD)DKL​(pn∥pnapp)=∫−∞∞pn​(x)​log⁡(pn​(x)pnapp​(x))​𝑑xD_{\text{KL}}(p_{n}\,\|\,p^{\text{app}}_{n})=\int_{-\infty}^{\infty}p_{n}(x)\log\left(\frac{p_{n}(x)}{p_{n}^{\text{app}}(x)}\right)\,dx(8)

between the exact distributionpnp_{n}and any approximationpnappp^{\text{app}}_{n}. This divergence vanishes if, and only if, the approximation is exact.

We explore three scenarios: (i) non-identical, independent exponential distributions; (ii) truncated normal distributions; and (iii) non-identical generalized gamma distributions (such as those arising in microbiome ecologyCamacho-Mateuet al.(2025)).

## (i) Non-identical, independent exponential distributions:

LetXiX_{i},i=1​…​ni=1\ldots n, be independent random variables with exponential distributionsp​(Xi|λi)=λi​e−λi​Xi,p(X_{i}|\lambda_{i})=\lambda_{i}e^{-\lambda_{i}X_{i}},(9)

where the ratesλi\lambda_{i}are drawn from differenthyper-distributionsq​(λ)q(\lambda). We want to approximate the distribution ofSn=X1+⋯+XnS_{n}=X_{1}+\cdots+X_{n}by either a normal or a gamma distribution with the exact mean and variance.a)b)c)d)e)f)Figure 1:Empirical distributions of the sumSnS_{n}ofn=30n=30exponential variables with rates drawn from various hyper-distributionsq​(λ)q(\lambda). (a) Uniform[1,2]; (b) Log-normal(1,2); (c) power-lawq​(λ)∼λ−1q(\lambda)\sim\lambda^{-1}; (d) Uniform[0,1]; (e) One outlier rate (see text); (f) KL divergence difference between normal and gamma. The dashed straight line scales as∼1/n\sim 1/n. The gamma approximation (orange line) consistently outperforms the normal approximation (blue line). In the title, the KL divergence difference is always positive (the gamma is better). The cases in the bottom row show some discrepancies in the tails, due to the presence of some rate(s)λi≃0\lambda_{i}\simeq 0(see text).

Figure1shows the empirical distributions ofS30S_{30}for several choices ofq​(λ)q(\lambda). The gamma approximation consistently outperforms the normal. We can justify this success by using an estimate of the KLD obtained from the Edgeworth expansionJondeau and Rockinger (2001)(see section S1 of the Supplemental MaterialSMand Refs [1-3] therein). Ifpnappp_{n}^{\text{app}}is either a normal or a gamma distribution, the leading term of the expansion isDKL​(pn∥pnapp)≈112​(κ¯3−κ¯3app)2,D_{\text{KL}}(p_{n}\,\|\,p^{\text{app}}_{n})\approx\frac{1}{12}\big(\bar{\kappa}_{3}-\bar{\kappa}_{3}^{\text{app}}\big)^{2},(10)

whereκ¯k≡κk,n/σnk\bar{\kappa}_{k}\equiv\kappa_{k,n}/\sigma_{n}^{k}is the normalizedkkth order cumulant, and the superscript ‘app’ refers to the approximating distribution.
Using the Cauchy-Schwarz inequality, we can prove(SM,, Sec. S1)that for a sum of exponential random variables(κ¯3−κ¯3𝒢)2<κ¯32\big(\bar{\kappa}_{3}-\bar{\kappa}_{3}^{\mathcal{G}}\big)^{2}<\bar{\kappa}_{3}^{2}, so for sufficiently largenn,DKL​(pn∥ϕ𝒢)<DKL​(pn∥ϕ𝒩)D_{\text{KL}}(p_{n}\,\|\,\phi_{\mathcal{G}})<D_{\text{KL}}(p_{n}\,\|\,\phi_{\mathcal{N}}). In other words,the gamma approximation outperforms the central limit approximationprecisely in the limit where the latter is supposed to dominate.

Returning to Fig.1, we can see that, in general, the gamma approximation captures the empirical distribution over the whole range of parameters. The only discrepancies that one can spot occur at the extreme tails, only for some particular cases: those where some rates are too close to0([0,1][0,1]-uniform distribution); when they span several orders of magnitude (harmonic case, with ratesλi=i\lambda_{i}=i, fori=1,…,ni=1,\ldots,n); or when one rate is1010times lower (outlier) than the rest—which are identical.

In order to gain insight into the latter case, we can analyze the hyper-distributionq​(λ)=(1−1/n)​δ​(λ−1)+(1/n)​δ​(λ−α)q(\lambda)=(1-1/n)\delta(\lambda-1)+(1/n)\delta(\lambda-\alpha). Then, ifnnis large enough(SM,, Sec. S2),DKL​(pn∥ϕ𝒢)≈(n−1)2​α−2​(1−α−1)43​(n−1+α−2)3​(n−1+α−1)2.D_{\mathrm{KL}}\!\bigl(p_{n}\,\|\,\phi_{\mathcal{G}}\bigr)\approx\frac{(n-1)^{2}\alpha^{-2}\big(1-\alpha^{-1}\big)^{4}}{3\big(n-1+\alpha^{-2}\big)^{3}\big(n-1+\alpha^{-1}\big)^{2}}.

For largeα\alphathis scales asDKL​(pn∥ϕ𝒢)∼1/3​α2​n3D_{\mathrm{KL}}\!\bigl(p_{n}\,\|\,\phi_{\mathcal{G}}\bigr)\sim 1/3\alpha^{2}n^{3}, whereas for smallα\alphait scales as∼α2​n2/3\sim\alpha^{2}n^{2}/3. The former scaling justifies why outliers with a higher rate are well captured by the gamma approximation, whereas low-rate outliers spoil the approximation at the tails(SM,, Fig. S1).

## (ii) Truncated normal distributions:

Although the Padé expansion\eqrefeq:cgfslope does not assume that the elements ofSnS_{n}must be exponentially distributed, one may wonder whether the success of the gamma is somehow linked to the exponential decay of the empirical distribution. Our next scenarios show that the improvement gained by using Padé approximants goes beyond the sum of exponential random variables. For instance, considerXiX_{i}to be drawn from a positively truncated normal distributionp​(Xi)∝e−(Xi−μ)2/σ2​Θ​(Xi)p(X_{i})\propto e^{-(X_{i}-\mu)^{2}/\sigma^{2}}\Theta(X_{i}). In Fig.2, we show that if the left tail of the normal distribution is heavily truncated, the gamma distribution better describes again the distribution ofSnS_{n}. We quantify this by numerically computing the KLD, alongside Edgeworth approximations that qualitatively capture its shape(SM,, Sec. S3). As shown in Fig.2d), only whenμ≳σ\mu\gtrsim\sigmadoes the normal outperform the gamma.a)b)c)d)Figure 2:Empirical distribution ofS15S_{15}and the corresponding normal (blue diamonds), gamma (orange triangles), and shifted-gamma (purple circles) approximations for the sum of variables drawn from a truncated normal distribution with different values ofμ\mu. a)μ/σ=−1\mu/\sigma=-1; b)μ/σ=1\mu/\sigma=1; c)μ/σ=2\mu/\sigma=2; d) Numerical KLD (symbols) and approximation Eq.\eqrefeq:kappa3, for the normal and the gamma, and Eq.\eqrefeq:kappa4 for the shifted gamma. Note how atμ/σ∼1\mu/\sigma\sim 1(orange dashed line for the gamma, and purple dashed for the shifted gamma), both KLD cross, meaning that above that, the normal approximates better the empirical distribution, and below, the gamma is. Also note how Eqs.\eqrefeq:kappa3-\eqrefeq:kappa4 capture the transition qualitatively. In the case of the shifted gamma, the approximation extends up toμ/σ≃2\mu/\sigma\simeq 2as the third cumulant can also be matched (see Supplemental Material, Table S2).

## (iii) Non-identical generalized gamma distributions:

This last scenario highlights the practical implications of our work in an ongoing debate in ecology. Recent work has proposed the existence of universal macroecological laws, including the gamma distribution of abundance fluctuationsGrilli (2020). The claim is that this universality provides significant insight into the microscopic laws governing ecosystem dynamics. However, the mechanistic models proposed to justify the appearance of such a distributionGrilli (2020); Camacho-Mateuet al.(2024); George and O’Dwyer (2023)are sensitive to specific choices of certain terms. As a matter of fact, disaggregating by ecological niches, other distributions seem to fit the data as accurately, such as the generalized gammaCamacho-Mateuet al.(2025)f​(x)=λθ​k​θΓ​(k)​xθ​k−1​e−(λ​x)θ(x≥0).f(x)=\frac{\lambda^{\theta k}\theta}{\Gamma(k)}x^{\theta k-1}e^{-(\lambda x)^{\theta}}\quad(x\geq 0).(11)

Note that forθ=1\theta=1the distribution is a gamma and forθ=2\theta=2andk=1/2k=1/2a truncated normal withμ=0\mu=0.

In our final numerical experiment, we considern=6n=6different ecological subpopulations, each following a generalized gamma distribution with parametersθ\thetataken from the maximum posterior distribution of Ref.Camacho-Mateuet al.(2025). Asλ\lambdasimply sets the scale of the distribution, we fixλ=1\lambda=1. To test the generality of the approximation, we vary the shape parameterkk. As shown in Fig.3, in spite that the distribution of each random variable is poorly captured by a gamma, it nevertheless becomes accurate by aggregating justn=6n=6of them (see alsoSMfor further cases). Considering that the tails of the generalized gammas are not exponential, this result is remarkable.a)b)Figure 3:Gamma (orange) and normal (blue) approximations of the empirical histogram for a single (triangles) generalized gamma (θ=1.75\theta=1.75) and the sum (circles) of generalized gamma random variables fromn=6n=6ecological nichesCamacho-Mateuet al.(2025)with parametersλ=1\lambda=1,θ1,…,θ6=1.49,1.54,1.11,1.60,1.75,1.42\theta_{1},\ldots,\theta_{6}=1.49,1.54,1.11,1.60,1.75,1.42, respectively, and a)k=0.50k=0.50and b)k=3k=3.

## Beyond the gamma approximation.—

One advantage of using Padé approximants in\eqrefeq:cgfslope is that, whereas improving the Taylor expansion may lead to negative probabilities, Padés ensure positivity. For instance, if we chose a[1/1][1/1]-Padé,n​λn′​(ξ)≈μn+σn2​ξ1−κ3,n​ξ/2​σn2,n\lambda_{n}^{\prime}(\xi)\approx\mu_{n}+\frac{\sigma_{n}^{2}\xi}{1-\kappa_{3,n}\xi/2\sigma_{n}^{2}},(12)

we would obtain shifted gamma distribution. This distribution often improves on the gamma. For instance, in the case of the sum of truncated normal variables, the shifted gamma extends the range of improvement over the normal approximation. Figure2d shows (purple line) how this approximation almost matches that of the normal up toμ∼2​σ\mu\sim 2\sigma. In this case, as the third-order cumulants are also exact, the KLD gets approximated by(SM,, Sec. S1)DKL​(f∥ϕ𝒢)=148​(κ¯4−κ¯4𝒢)2.D_{\text{KL}}(f\|\phi_{\mathcal{G}})=\frac{1}{48}\big(\bar{\kappa}_{4}-\bar{\kappa}_{4}^{\mathcal{G}}\big)^{2}.(13)

Higher-order[k/k+1][k/k+1]-Padé approximants would yield convolutions of shifted gammas (one for each pole of the denominator), leading to a hierarchy of empirical distributions that reflect only the aggregation of underlying positive random variables.

In summary, this approach not only provides an improvement on the CLT for positive random variables, as well as an explanation for the ubiquity of the gamma distribution, but it becomes a methodological tool to produce approximations for empirical distributions systematically more accurate.

This work has been supported by grants PID2022-140217NB-I00 (MC) and PID2022-141802NB-I00 (BASIC) (JAC), funded by MICIN/AEI/10.13039/501100011033 and by “ERDF/EU A way of making Europe”.

## References
- Tracy and Widom (1996)C. A. Tracy and H. Widom, Communications in
Mathematical Physics177, 727 (1996).
- Gnedenko (1943)B. Gnedenko, Annals of mathematics44, 423 (1943).
- Bouchaud (2001)J.-P. Bouchaud, Quantitative Finance1, 105 (2001).
- Stumpf and Porter (2012)M. P. Stumpf and M. A. Porter, Science335, 665
(2012).
- Touatiet al.(2009)S. Touati, M. Naylor, and I. G. Main,Physical Review Letters102, 168501 (2009).
- Corral (2004)A. Corral,Physical Review Letters92, 108501 (2004).
- Davidsenet al.(2007)J. Davidsen, S. Stanchits, and G. Dresen,Physical Review Letters98, 125502 (2007).
- Grilli (2020)J. Grilli, Nature
communications11, 4743
(2020).
- Camacho-Mateuet al.(2025)J. Camacho-Mateu, A. Lampo, M. Castro, and J. A. Cuesta, Physical Review
E111, 044404 (2025).
- Biswas and Brenner (2024)K. Biswas and N. Brenner,Physical Review Research6, L022043 (2024).
- Zhang and Dudko (2015)Y. Zhang and O. K. Dudko,Physical Review Letters114, 018104 (2015).
- Brenner and Shokef (2007)N. Brenner and Y. Shokef,Physical Review Letters99, 138102 (2007).
- Iyer-Biswaset al.(2014)S. Iyer-Biswas, G. E. Crooks, N. F. Scherer, and A. R. Dinner,Physical Review Letters113, 028101 (2014).
- Touchette (2009)H. Touchette, Physics Reports478, 1
(2009).
- Butler (2007)R. W. Butler,Saddlepoint
approximations with applications, Vol. 22 (Cambridge University Press, 2007).
- Daniels (1954)H. E. Daniels, Ann.
Math. Stat. , 631 (1954).
- Baker Jr (1961)G. A. Baker Jr, Physical Review124, 768 (1961).
- Jondeau and Rockinger (2001)E. Jondeau and M. Rockinger, Journal of Economic Dynamics and Control25, 1457 (2001).
- (19)See Supplemental Material at…
- Camacho-Mateuet al.(2024)J. Camacho-Mateu, A. Lampo, M. Sireci,
M. A. Mu ñoz, and J. A. Cuesta, Proceedings of the
National Academy of Sciences121, e2309575121 (2024).
- George and O’Dwyer (2023)A. B. George and J. O’Dwyer, Proceedings of the National Academy of Sciences120, e2215832120 (2023).

## 


- 


Major funding support from
