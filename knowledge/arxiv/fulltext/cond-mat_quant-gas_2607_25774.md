# Ro-vibrational van der Waals interaction between ultracold polar molecules

**arXiv ID**: 2607.25774v2
**Authors**: Kang Feng, Hanwei Yang, Hubert J. Jóźwiak, Tijs Karman
**Published**: 2026-07-28
**Categories**: cond-mat.quant-gas, physics.atom-ph, physics.chem-ph, quant-ph
**HTML URL**: https://arxiv.org/html/2607.25774v2

## Abstract

We describe the ro-vibrational van der Waals interaction between ultracold polar molecules. This interaction is strong, leading to fast elastic collisions and orders of magnitude suppression of collisional loss. This enables evaporative cooling of Fermi mixtures of molecules in different ro-vibrational states, without active shielding by applying external fields. The scheme is compatible with microwave shielding, where it enables controlled state dependent interactions, opening up new opportunities for quantum simulation and impurity physics. The interaction can also be used to stabilize fermionic molecules in optical lattices, to control interactions in synthetic dimensions, for enhanced tweezer loading, and direct infrared shielding.

## Full Text

Ro-vibrational van der Waals interaction between ultracold polar molecules

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
- License: CC BY 4.0arXiv:2607.25774v2 [cond-mat.quant-gas] 31 Jul 2026

## Ro-vibrational van der Waals interaction between ultracold polar moleculesKang Feng, Hanwei Yang, Hubert J. Jóźwiak, Tijs KarmanInstitute for Molecules and Materials, Radboud University, Nijmegen, The Netherlands

## Abstract

We describe the ro-vibrational van der Waals interaction between ultracold polar molecules.
This interaction is strong, leading to fast elastic collisions and orders of magnitude suppression of collisional loss.
This enables evaporative cooling of Fermi mixtures of molecules in different ro-vibrational states,
without active shielding by applying external fields.
The scheme is compatible with microwave shielding,
where it enables controlled state dependent interactions,
opening up new opportunities for quantum simulation and impurity physics.
The interaction can also be used to stabilize fermionic molecules in optical lattices,
to control interactions in synthetic dimensions,
for enhanced tweezer loading, and direct infrared shielding.

## IIntroduction

Ultracold polar molecules are long considered powerful platforms for few[1]and many-body physics[2,3], quantum simulation[4,5]and computation[6,7,8,9,10], and precision measurement[11,12].
While quantum control of molecules is challenging compared to atoms,
recent progress has been rapid[13].
Molecules have anisotropic, tunable dipole–dipole interactions that are long ranged and extend over multiple sites in an optical lattice[14,15].
These interactions enable the natural realization of extended Hubbard models[16], quantum magnetism with controllable spin–spin interactions[17,4,3,18], and supersolids[19], quantum droplets[20], and other novel quantum phases[21].
In addition, molecules provide a large internal Hilbert space through their rotational, vibrational, and hyperfine degrees of freedom.
This allows quantum simulators to encode pseudo-spin and multi-orbital physics,
SU(NN) symmetric interactions[22],
and synthetic dimensions[23,24]

Shielding has recently yielded quantum gases of molecules with tunable interactions,
both Fermi degenerate gases[25,26,27,28]and Bose-Einstein condensates[29,30]of polar molecules.
Shielding is necessary for collisional stability[31]and efficient evaporative cooling,
but simultaneously offers control over molecular interactions.
Double microwave shielding offers control of the sign and strength of dipolar interactions,
and simultaneously enables tuning of the scattering length relative to the dipolar one[32].
Control of the microwave ellipticity offers further control of the anisotropy of the dipolar interactions[33,34].
Quantum gases of polar molecules with tunable interactions offer a powerful platform for quantum many-body physics and simulation[35].

In this context, additional schemes for controlling collisions and interactions can be highly valuable as a resource for interaction tuning.
We have previously developed the rotational[36]and hyperfine[37]van der Waals interactions.
These interactions can be repulsive and hence suppress adverse collisions,
and they can be controlled through the state dependence.
Unlike most collisional shielding schemes, these interactions can be effective even in the absence of external fields.

These state-dependent van der Waals interactions are qualitatively understood as follows.
The dipole-dipole interaction is the dominant long-range interaction between polar molecules,
scaling with intermolecular distance asR−3R^{-3}.
However, without external fields any eigenstate of the molecule can be assigned definite parity and has no dipole expectation value.
The dipolar interaction is still the dominant interaction,
but its effect stems from the transition dipole moment between molecular eigenstates of opposite parity.
These virtual transitions lead to a second-order interaction which varies asR−6R^{-6}and is typically called a van der Waals (vdW) interaction.
Selection rules determine which virtual excitations contribute to this interaction, i.e. which have non-zero transition dipole.
The second-order interaction is typically dominated by the allowed virtual transition with the smallest energy denominator,
and the sign of the energy denominator determines the sign of the interaction;
dominant virtual excitations (de-excitations) lead to attractive (repulsive) interactions.
Thus, the internal states of the molecules control the strength and sign of the vdW interaction[36].

For rotational states of diatomic molecules, the dipole operator has the selection ruleΔ​j=±1\Delta j=\pm 1.
Two molecules will experience resonant dipole-dipole interactions when placed in rotational statesj,j+1j,j+1, which is coupled by dipole-dipole toj+1,jj+1,j.
When molecules are placed in any other choice of rotational statesj,j′j,j^{\prime},
dipole-dipole couples this to pairs of statesj±1,j′±1j\pm 1,j^{\prime}\pm 1.
The energy denominators arej,j′j,j^{\prime}dependent, and are on the order of the rotational constant.
This results in a second-order interaction that we called the rotational van der Waals[36]to indicate that the dominant virtual excitations are purely rotational transitions,
in contrast with the conventionalelectronicvdW interaction.
The rotational vdW interaction is state dependent throughjjandj′j^{\prime},
and repulsive wheneverΔ​j≥2\Delta j\geq 2,
which results directly from thej​(j+1)j(j+1)energy spectrum of the rigid rotor that gets sparser as energy increases.
We note that this is contrary to electronic energy levels which typically become denser at higher energies and for which the vdW interaction is typically attractive.

The hyperfine van der Waals interaction[37]occurs for the special case wherej′=j+1j^{\prime}=j+1.
In this case, one should nominally observe resonant dipolar interactions.
However, if one considers molecules in pairs of hyperfine states labeled by rotational and total angular momentumj,fj,f,
one can find pairs of states(j,f)+(j′,f′)(j,f)+(j^{\prime},f^{\prime})such that even thoughj→j′=j+1j\rightarrow j^{\prime}=j+1transitions are dipole allowed,f⟷/f′f\mathrel{\vtop{\halign{#\cr$\longleftrightarrow$\cr$/$\crcr}}}f^{\prime}transitions are not,
e.g. forΔ​f>1\Delta f>1orf=0⟷/f′=0f=0\mathrel{\vtop{\halign{#\cr$\longleftrightarrow$\cr$/$\crcr}}}f^{\prime}=0.
In this case, the dipolar interaction couples this pair of states of the molecules to other hyperfine states within the samej,j′j,j^{\prime}manifold.
The energy denominator for such virtual excitations is not on the order of the rotational constant as for the rotational vdW interaction,
but on the other of the hyperfine splittings.
Hence, the energy denominator is orders of magnitude smaller and the corresponding van der Waals interaction orders of magnitude stronger.
This interaction is not effective for closed-shell molecules where the hyperfine splittings are too small,
but it is very effective forΣ2{}^{2}\Sigmamolecules which includes most laser-coolable molecules[37].Figure 1:Molecular energy levels relevant for the ro-vibrational vdW interaction.The rotation-vibration coupling leads to a reduction of the rotational constant in vibrationally excited states, as indicated in gray.
This lifts the resonances of the rotational de-excitation inv=0,j=1v=0,j=1, and rotational excitation inv=1,j=0v=1,j=0,
indicated by the orange arrows.
This virtual process dominates the second-order dipolar interaction that gives rise to the ro-vibrational vdW interaction.
The purple arrows indicate that a direct resonant dipole-dipole interaction also exists,
but this involves the vibrational transition dipole moment that is at least an order of magnitude weaker than the rotational one for the molecules that we consider.

In this paper, we detail a novel ro-vibrational van der Waals interaction, which is illustrated in Fig.1.
We consider one molecule in the vibrational ground statev=0v=0and rotational statej=1j=1,
and one molecule in the first vibrationally excited statev′=1v^{\prime}=1and rotational statej′=0j^{\prime}=0.
If the rotational constant were the same in both vibrational states,
this pair(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0)would be degenerate with(0,0)+(1,1)(0,0)+(1,1).
These are related by a dipole-allowed purely rotational transition for both molecules,
and hence coupled by the dipolar interaction.
However, due to the anharmonicity of the molecular vibration, the molecular bond is slightly stretched in the vibrationally excited state,
which leads to a slight reduction of the rotational constant that makes the dipolar interaction non-resonant, see Sec.II.
The typical energy defect is in the order of 10 MHz,
resulting in a vdW interaction that is orders of magnitude stronger than the rotational counterpart.

Vibration –unlike rotation– is not currently exploited as a resource of ultracold molecules[5],
with very few exceptions including attempts to control chemical reactivity[38]and usingℓ\ell-type doubling for precision measurement[39,40,41]and shielding[42,43].
Nevertheless, ultracold molecules could readily be prepared in vibrationally excited states.
Typical ultracold molecules are bialkalis produced by associating ultracold atoms using stimulated Raman adiabatic passage (STIRAP)[44,45,46,47,48,49].
STIRAP can produce molecules in the vibrational ground state or directly in a vibrationally excited state[38].
Alternatively, the STIRAP laser and a single additional laser can drive a Raman transition into the vibrationally excited state.
For laser-coolable molecules, such as CaF[50], SrF[51], BaF[52], and YO[53], vibrationally excited states can be prepared by turning off a vibrational repump laser or a particular hyperfine component therein.
Alternatively, the main cooling laser and a vibrational repump laser can be used to drive a Raman transition.

While the ro-vibrational vdW interaction is similar in origin to the known rotational and hyperfine vdW interactions, we believe that this can be a powerful, versatile resource for controlling interactions between ultracold molecules. To demonstrate this, the manuscript is structured as follows. We begin in Sec.IIby detailing the origin of this rotation-vibration energy defect and compile these coupling constants for relevant molecules. In Sec.III, we qualitatively characterize the ro-vibrational vdW interaction, comparing its energy and length scales with its electronic, rotational, and hyperfine counterparts. In Sec.IV, we extend coupled-channel calculations to include molecular vibration, enabling the quantitative study of collision dynamics.
The results, discussed in Sec.V, confirm that
the ro-vibrational vdW interaction is stronger, leading to faster elastic collisions and better suppression of inelastic losses.
In Sec.VI, we demonstrate the universality of the ro-vibrational vdW interaction.
In Sec.VII, we consider direct evaporative cooling of fermionic mixtures without active shielding,
enabled by the favorable collisional properties.
We conclude in Sec.VIIIby discussing further applications enabled by this work,
including direct collisional shielding,
enhanced deterministic loading of molecular arrays,
and compatibility with microwave shielding, which opens up new opportunities for quantum magnetism and impurity physics.

## IIRotation-vibration coupling

The rotation-vibration energy levels of a diatomic molecule are described by the Dunham expansion[54], a power series inj​(j+1)j(j+1)andv+1/2v+1/2,E​(v,j)\displaystyle E(v,j)=Be​j​(j+1)−De​[j​(j+1)]2+…\displaystyle=B_{e}j\left(j+1\right)-D_{e}\left[j\left(j+1\right)\right]^{2}+\ldots+\displaystyle+ωe​(v+12)−ωe​xe​(v+12)2+…\displaystyle\omega_{e}\left(v+\frac{1}{2}\right)-\omega_{e}x_{e}\left(v+\frac{1}{2}\right)^{2}+\ldots−\displaystyle-αe​j​(j+1)​(v+12)+….\displaystyle\alpha_{e}j\left(j+1\right)\left(v+\frac{1}{2}\right)+\ldots.(1)

The first term describes the energy levels of a rigid rotor, whereBeB_{e}is the rotational constant.
The second term describes rotational distortion, lessening of the rotational constant upon rotational excitation, whereDeD_{e}is the rotational distortion constant.
The third term describes harmonic vibrational energy levels, andωe\omega_{e}is the harmonic oscillator frequency.
The fourth term describes the anharmonicity, quantified byωe​xe\omega_{e}x_{e}.
The fifth term describes the rotation-vibration coupling, andαe\alpha_{e}is the rotation-vibration coupling constant.
Essentially, this describes reduction of the rotational constant upon vibrational excitation,
which effectively increases the mean bond length and hence the molecule’s moment of inertia.
The sign of each term in the Dunham expansion is chosen such that the molecular constants are typically positive, but as we will discuss below this is somewhat subtle for the case of the rotation-vibration coupling constantαe.\alpha_{e}.

Pekeris derived an expression for the rotation-vibration coupling constantα\alphafor the Morse potential[55]αe\displaystyle\alpha_{e}=6​Be​(Be​xeωe−Beωe)\displaystyle=6B_{e}\left(\sqrt{\frac{B_{e}x_{e}}{\omega_{e}}}-\frac{B_{e}}{\omega_{e}}\right)(2a)=3​ωe​xe​De−6​Be2ωe\displaystyle=3\sqrt{\omega_{e}x_{e}D_{e}}-6\frac{B_{e}^{2}}{\omega_{e}}(2b)=3​Be​BeV−6​Be2ωe.\displaystyle=3B_{e}\sqrt{\frac{B_{e}}{V}}-6\frac{B_{e}^{2}}{\omega_{e}}.(2c)

The first equation here is Pekeris’ relation[55],
the second is related to it by the Kratzer relationDe=4​Be3/ωe2D_{e}=4B_{e}^{3}/\omega_{e}^{2}, which holds for many reasonable potentials,
and the third is related byV=ωe/4​xeV=\omega_{e}/4x_{e}, a relation for the potential depth that holds for the Morse potential.
In all three cases, the second term is the result for a purely harmonic potential.
In the harmonic case, the vibrational wavefunction becomes wider upon vibrational excitation,
but remains centered aroundrer_{e},
and the rotational constant related to the expectation value of1/r21/r^{2}increases.
For real anharmonic molecular potentials, the vibrational wavefunction not only becomes wider upon vibrational excitation,
but it also becomes asymmetric;
The wavefunction amplitude grows more on the largerrside and the mean interatomic distance grows,
resulting in a decrease of the rotational constant upon vibrational excitation.
Hence, the sign ofα\alphareverses from the harmonic to the anharmonic case,
such that the first term of the Pekeris relation typically dominates, but only by a factor a few.
This already indicates thatαe\alpha_{e}is quite sensitive to the precise form of the potential anharmonicity.
For example, for the Kratzer potential2​V​[(re/r)2−re/r]2V[(r_{e}/r)^{2}-r_{e}/r][56],αe=2​Be​xe\alpha_{e}=2B_{e}x_{e}which is different from the Pekeris relation by a factor3​Be/ωe​xe−3​Be/ωe​xe3\sqrt{B_{e}/\omega_{e}x_{e}}-3B_{e}/\omega_{e}x_{e}which is around 0.67 for many molecules considered by Pekeris[55].
Interestingly, this expression was more recently rederived as an approximate result for the Morse potential[57], although as we just discussed it was already known to be inaccurate compared to the exact result by Pekeris[55].

We tabulate the rotation-vibration coupling constantαe\alpha_{e}for various molecules in Table1.
For bi-alkali molecules we determine these by numerically computing ro-vibrational wavefunctions using spectroscopically accurate potential energy curves[58,59,60,61,62,63,64,65], and fitting a Dunham expansion.
We also include some laser-coolable molecules for whichαe\alpha_{e}is known directly from spectroscopy.
It can be seen that the values obtained forαe\alpha_{e}agree reasonably but only qualitatively with the Pekeris relations Eqs. (2).
Values resulting from Eqs. (2a) and (2b) agree well,
because these are related by the Kratzer relation that is widely considered to be reasonable for many realistic potential models.
Values obtained from Eq. (2c) appear to be less accurate but qualitatively meaningful (except for the case of LiK),
while this relation has the advantage that it does not require knowledge ofωe​xe\omega_{e}x_{e}.
The difference between these estimates seems to be indicative of the difference withαe\alpha_{e}from experiment, where avaiable.
We emphasize that Eq. (2c) differs from Eq. (2a) only byV=ωe/4​xeV=\omega_{e}/4x_{e}, which holds exactly for the Morse potential for which the Pekeris relation (2a) was derived in the first place.
Hence, the relatively better performance of one relation over the others is an empirical observation that does not need to hold for all molecules.
There is also substantial interest in ultrapolar molecules consisting of alkali metal and coinage metal atoms, for which spectroscopic parameters are computed in Ref.[66].
From this data available, we estimated the rotational distortion by the Kratzer relationDe=4​Be3/ωe2D_{e}=4B_{e}^{3}/\omega_{e}^{2}, the anharmonicity asωe​xe=ωe2/4​V\omega_{e}x_{e}=\omega_{e}^{2}/4V, and the rotation-vibration coupling constant by Eq. (2c).
From Eqs. (2), a strong dependence on molecular parameters is apparent,
which explains the values forαe\alpha_{e}that span orders of magnitude, and are typically between 1 MHz to 100 MHz for typicalassembledultracold molecules.Table 1:Molecular constants. For the bialkalis all molecular parameters are obtained by fitting a Dunham expansion to the ro-vibrational states calculated on the spectroscopically accurate potential energy curves, as indicated. Dipole moments and derivatives are taken from Refs.[67]and[68], as indicated. For the coinage-metal molecules, parameters are taken from Ref.[66], while the rotational distortion was estimated from these parameters by the Kratzer relationDe=4​Be3/ωe2D_{e}=4B_{e}^{3}/\omega_{e}^{2}, the anharmonicity estimated asωe​xe=ωe2/4​V\omega_{e}x_{e}=\omega_{e}^{2}/4V, andαe\alpha_{e}estimated using the third Pekeris relation, Eq. (2c).
For the laser-coolable molecules, spectroscopic parameters are taken directly from literature as indicated.Moleculeded_{e}(Debye)∂d∂r\frac{\partial d}{\partial r}(Debye/a0a_{0})BeB_{e}(GHz)DeD_{e}(kHz)ωe\omega_{e}(THz)ωe​xe\omega_{e}x_{e}(GHz)αe\alpha_{e}(MHz) Expt.Eq. (2a)Eq. (2b)Eq. (2c)14NH1.53[69]0.37[69]500.6351, 25598.42 34719  46017 81017 620[70,71]24Mg19F3.6[72]2.6[73]15.632.421.3148.1140.9142.0139.6[74]40Ca19F3.1[75]3.1[76]10.313.517.482.173.665.364.5[77,74]88Sr19F3.5[78]3.1[76]7.517.4615.166.046.344.1244.09[74]138Ba19F3.4[72]3.5[76]6.475.2514.153.736.033.632.5[74]89Y16O4.5[79]11.69.5925.886.954.054.555.2[74]LiNa0.47[68]0.049[67]11.398.27.6949.596.2108110147[62]LiK3.4[68]0.19[67]7.7247.36.3638.358.369.171.6-56.1[65]LiRb4.0[68]0.22[67]6.4832.35.8743.047.867.668.874.5[64]LiCs5.3[68]0.33[67]5.6323.65.5329.938.044.945.361.1[80]NaK2.7[68]0.10[67]2.856.803.7214.913.716.917.124.4[81]NaRb3.3[68]0.12[67]2.093.663.2313.39.012.412.815.3[60]NaCs4.7[68]0.20[67]1.742.422.969.937.098.518.5811.7[58]KRb0.63[68]0.0089[67]1.141.162.276.913.675.015.076.79[61]KCs1.9[68]0.059[67]0.910.732.055.832.733.733.765.06[63]RbCs1.2[68]0.044[67]0.490.151.784.681.261.691.711.86[59]LiAg5.211.0[66]13.876.411.773.0127[66]NaAg6.01.2[66]3.835.516.3726.022.1[66]KAg8.51.4[66]2.001.644.1212.38.1[66]RbAg9.01.6[66]1.110.5003.296.913.35[66]CsAg9.81.9[66]0.8060.2742.774.712.00[66]FrAg9.21.8[66]0.6450.1682.524.181.53[66]

## IIIRo-vibrational van der Waals interaction

We consider dipolar interactions between molecules in different ro-vibrational statesv,jv,jandv′,j′v^{\prime},j^{\prime}.
First-order dipolar interactions occur only if the transitionv,jv,jtov′,j′v^{\prime},j^{\prime}is dipole allowed,
so that the pair of states(v,j)+(v′,j′)(v,j)+(v^{\prime},j^{\prime})is coupled by the dipolar interaction to(v′,j′)+(v,j)(v^{\prime},j^{\prime})+(v,j).
Otherwise, the dominant interaction arises in second order, resulting in a van der Waals interaction∑n′≠n|⟨n′|V^dd​(R)|n⟩|2En−En′=−C6R6,\sum_{n^{\prime}\neq n}\frac{\left|\langle n^{\prime}|\hat{V}_{\mathrm{dd}}(R)|n\rangle\right|^{2}}{E_{n}-E_{n^{\prime}}}=-\frac{C_{6}}{R^{6}},(3)

wheren=(v,j)+(v′,j′)n=(v,j)+(v^{\prime},j^{\prime})is a short-hand notation for a pair of states,
with energyEnE_{n},V^dd​(R)\hat{V}_{\mathrm{dd}}(R)is the dipole-dipole interaction,
andC6C_{6}the resulting van der Waals coefficient.
Note that a strong interaction is obtained for molecules in states where there is coupling to a virtual staten′n^{\prime}that is very close in energy, minimizing the energy denominator in Eq. (3).
The sign of the interaction is determined by this denominator:
dominant virtual states that are higher (lower) in energy result in attractive (repulsive) interactions.

Pairs of virtual excitations contribute to Eq. (3) only if the transition is dipole-allowed for both molecules.
For pure rotational transitions this leads to the selection ruleΔ​j=±1\Delta j=\pm 1,Δ​v=0\Delta v=0,
and the transition dipole moment is on the order of the permanent dipole moment of the molecule around the equilibrium bond length,ded_{e}.
The selection rule for vibrational transitions isΔ​j=±1\Delta j=\pm 1andΔ​v=±1\Delta v=\pm 1,
and here the transition dipole moment is on the order of the derivative of the dipole with respect to bond length,∂d/∂r\partial d/\partial r, around equilibrium.

In this paper, we study the special case where two molecules are prepared in(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0), as illustrated in Fig.1.
This pair of molecular states is coupled by the dipole-dipole interaction to(0,0)+(1,1)(0,0)+(1,1),
which is lower in energy by2​αe2\alpha_{e}.
This leads to a second-order interaction±C6​R−6\pm C_{6}R^{-6}which is repulsive (attractive) in the upper (lower) threshold,
withC6=de4/9​αeC_{6}=d_{e}^{4}/9\alpha_{e}the isotropic vdW coefficient that determines the interaction in thess-wave channel.
This interaction can be very strong;C6=7×107C_{6}=7\times 10^{7}a.u. for NaK and101010^{10}a.u. for KAg,
which leads to corresponding length scalesR6=(m​C6/ℏ2)1/4=1700R_{6}=(mC_{6}/\hbar^{2})^{1/4}=1700and74007400a0a_{0}, respectively.
Although the molecular vibration is an essential element for this interaction mechanism,
we emphasize that this should not be considered avibrationalvdW interaction, as the virtual transitions are purely rotational.
We therefore refer to this as thero-vibrationalvdW interaction,
emphasizing that the rotation-vibration coupling is responsible for the energy denominator associated with this virtual excitation.

Typical electronic excitation energies are in the eV range,
such that typicalC6C_{6}coefficients that characterize the strength of the van der Waals interaction−C6​R−6-C_{6}R^{-6}are in the order 100–10 00010\,000atomic units,
strongly depending on the size of the constituent atoms.
The strength of this van der Waals interaction can also be conveniently characterized by a length scaleR6=(m​C6/ℏ2)1/4R_{6}=(mC_{6}/\hbar^{2})^{1/4}which is in the order of a hundred atomic units.
Note that this length scale scales relatively weakly withC6C_{6}.
Typical rotational constants are in the order of several GHz,
leading to typicalC6C_{6}coefficients in the order of hundreds of thousands of atomic units,
and typical van der Waals lengthsR6R_{6}in the order of several hundred bohr radii.
For open-shell molecules for which the hyperfine van der Waals interaction is effective,
the fine and hyperfine splittings are on the order of tens to hundreds of MHz,
leading toC6C_{6}coefficients in the millions of atomic units,
andR6R_{6}in the order of a thousand bohr radii.
Compared to these, the ro-vibrational vdW interaction discovered here is orders of magnitude stronger,
characterized byC6C_{6}coefficients in the order of tens of millions to billions of atomic units,
andR6R_{6}length scales of thousands of bohr radii.

The mechanism occurs more generally for pairs of molecules in states(v,j)+(v′,j+1)(v,j)+(v^{\prime},j+1)that are connected by purely rotational transition dipoles to(v,j+1)+(v′,j)(v,j+1)+(v^{\prime},j),
which are degenerate except for the change of rotational constant in the different vibrational states.
The energy defect is2​αe​(j+1)​Δ​v2\alpha_{e}(j+1)\Delta vand leads to repulsive (attractive) vdW interactions in the(v,j)+(v′,j+1)(v,j)+(v^{\prime},j+1)channel ifv>v′v>v^{\prime}(v<v′v<v^{\prime}).

For the molecules considered here, the transition dipole moment for vibrational transitions is at least an order of magnitude smaller than for rotational transitions.
This has two important consequences.
First, the vibrational transition dipole moment gives rise to first-order dipole-dipole interactions in the(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0)threshold, see Fig.1.
We have so far ignored this to simplify the discussion.
In reality, this dipole-dipole interaction arising from the vibrational transition dipole moment is so weak that it can be neglected, see Sec.VI.
Second, the weak vibrational transition dipole moment also means that there is no effectivevibrationalvdW interaction.
This seems obvious because the transition dipole moment is weaker than for the competing rotational vdW interaction,
and the energy denominator appears orders of magnitude larger, if it is on the order ofωe\omega_{e}.
As described in the Appendix, however, the situation is slightly more subtle because the energy denominator for virtual processes of the typev,v→v−1,v+1v,v\rightarrow v-1,v+1is determined by the anharmonicityωe​xe\omega_{e}x_{e},
which is on the order of GHz, just like the rotational constant,
so that it is possible to cancel the energy denominator to a large extent.
Due to the small vibrational transition dipole moment, we are nevertheless led to conclude that there exists no effectivevibrationalvdW interaction, see AppendixA.Figure 2:Interaction potentialsfor NaK molecules interacting by the ro-vibrational vdW interaction.
Illustrated in gray are adiabatic potential curves for different partial wavesL=0,2,4L=0,2,4,
and corresponding to different hyperfine states.
The repulsive (attractive)ss-wave interaction potentials are shown in blue (red) for the channels(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0)((0,0)+(1,1)(0,0)+(1,1)) in the hyperfine ground state.
Additional thresholds such as(v,j)+(v′,j′)=(0,0)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,0)+(1,0)and(0,1)+(1,1)(0,1)+(1,1)are shown to occur at different energies on the scale of the rotational constant, and lead to well separated potential curves.
Panel (b) provides an expanded view.

## IVCoupled-channels calculations

We describe collisions between ultracold molecules by coupled-channel calculations that include an absorbing boundary condition at short range, which models collisional loss by sticky collisions.
These calculations quantitatively describe universal collisional loss[82], and microwave shielding[83,84,28,33,85,29].
Most of the details of these calculations have been described in Ref.[32],
and we here summarize the key aspects and detail the necessary extensions to include the molecular vibration.

A single molecule is described by the HamiltonianH^(X)=H^0(X)+H^hf(X)+H^Zeeman(X)+H^ac,σ(X)+H^ac,π(X).\displaystyle\hat{H}^{(X)}=\hat{H}^{(X)}_{0}+\hat{H}^{(X)}_{\mathrm{hf}}+\hat{H}^{(X)}_{\mathrm{Zeeman}}+\hat{H}_{\mathrm{ac},\sigma}^{(X)}+\hat{H}_{\mathrm{ac},\pi}^{(X)}.(4)

where the rotation-vibrational HamiltonianH^0(X)\displaystyle\hat{H}^{(X)}_{0}=∑v,j,m|v,j,m⟩​⟨v,j,m|​E​(v,j),\displaystyle=\sum_{v,j,m}|v,j,m\rangle\langle v,j,m|\,E(v,j),(5)

is fully specified by the Dunham expansion Eq. (1).
In our previous work[32]this was limited to the termBrot​j^2B_{\mathrm{rot}}\hat{j}^{2}.
The remaining terms in the monomer Hamiltonian Eq. (4) describe the hyperfine structure,
Zeeman interaction with an external magnetic fieldBB,
and coupling to microwave electric fields, respectively, see Ref.[32].

The total Hamiltonian for the pair of colliding molecules in the center of mass frame contains, in addition to the monomer Hamiltonians discussed above,
relative kinetic energy and an intermolecular interaction potential, see Ref.[32].
We approximate the interaction by the longest range contribution, the dipole-dipole interactionV^=−304​π​ϵ0​R3​[[d^(1)​(𝒓A)⊗d^(1)​(𝒓B)](2)⊗C(2)​(R^)]0(0),\displaystyle\hat{V}=-\frac{\sqrt{30}}{4\pi\epsilon_{0}R^{3}}\left[\left[\hat{{d}}^{(1)}(\bm{r}_{A})\otimes\hat{{d}}^{(1)}(\bm{r}_{B})\right]^{(2)}\otimes C^{(2)}(\hat{R})\right]^{(0)}_{0},(6)

whereC(2)​(R^)C^{(2)}(\hat{R})is a rank-two tensor with spherical components given by Racah-normalized spherical harmonics depending on the polar coordinates ofR^\hat{R}, the intermolecular vector.
The quantity[A^(kA)⊗B^(kB)]q(k)=∑qA,qBA^qA(kA)​B^qB(kB)​⟨kA​qA​kB​qB|k​q⟩\displaystyle\left[\hat{A}^{(k_{A})}\otimes\hat{B}^{(k_{B})}\right]^{(k)}_{q}=\sum_{q_{A},q_{B}}\hat{A}^{(k_{A})}_{q_{A}}\hat{B}^{(k_{B})}_{q_{B}}\langle k_{A}q_{A}k_{B}q_{B}|kq\rangle(7)

indicates a spherical tensor product.
For themmspherical component of the dipole operator we used^m​(𝒓A)=[de+∂d∂r​ℏ2​μA​ωe​(a^+a^†)]​C1,m​(r^),\displaystyle\hat{{d}}_{m}(\bm{r}_{A})=\left[d_{e}+\frac{\partial d}{\partial r}\sqrt{\frac{\hbar}{2\mu_{A}\omega_{e}}}\left(\hat{a}+\hat{a}^{\dagger}\right)\right]C_{1,m}(\hat{r}),(8)

whereμA\mu_{A}is the reduced mass for the vibration of moleculeAA,
anda^=∑vv​|v⟩​⟨v+1|\hat{a}=\sum_{v}\sqrt{v}\ |v\rangle\langle v+1|is the annihilation operator for the molecular vibration.
We note that our previous work[32]included only the first term in Eq. (8),
whereas the second term gives the contribution of the vibrational transition dipole moment to the dipolar interaction.

We use a completely uncoupled primitive basis set.
For moleculeX=A,BX=A,Bthis consists of products of vibrational states|v⟩|v\rangle,
rotational states,|j,m⟩|j,m\rangle, with position representation⟨r^(X)|jx​mx⟩=2​jX+14​π​CjX,mX​(r^(X)),\displaystyle\langle\hat{r}^{(X)}|j_{x}m_{x}\rangle=\sqrt{\frac{2j_{X}+1}{4\pi}}C_{j_{X},m_{X}}(\hat{r}^{(X)}),(9)

and nuclear spin states|i1​m1⟩​|i2​m2⟩|i_{1}m_{1}\rangle|i_{2}m_{2}\rangle.
Where microwaves are included,
the state of the microwave fields is described in the photon number basis,|Nν⟩|N_{\nu}\rangle,
whereNν+N0,νN_{\nu}+N_{0,\nu}is the number of photons in fieldν\nurelative to a large reference numbers of photons,N0N_{0}.

Thus the basis functions describing a single moleculeXXin the presence of the two microwave fields take the form|vX⟩​|jX​mX⟩​|i1X​m1X⟩​|i2X​m2X⟩​|Nσ⟩​|Nπ⟩,\displaystyle|v^{X}\rangle|j^{X}m^{X}\rangle|i^{X}_{1}m^{X}_{1}\rangle|i^{X}_{2}m^{X}_{2}\rangle|N_{\sigma}\rangle|N_{\pi}\rangle,(10)

and the matrix elements of the Hamiltonian in this basis can be calculated as described above.
For two molecules in the presence of the two microwave fields, we set up a basis|vA⟩​|jA​mA⟩​|i1A​m1A⟩​|i2A​m2A⟩​|vB⟩​|jB​mB⟩​|i1B​m1B⟩​|i2B​m2B⟩​|ℓ​mℓ⟩​|Nσ⟩​|Nπ⟩,\displaystyle|v^{A}\rangle|j^{A}m^{A}\rangle|i^{A}_{1}m^{A}_{1}\rangle|i^{A}_{2}m^{A}_{2}\rangle|v^{B}\rangle|j^{B}m^{B}\rangle|i^{B}_{1}m^{B}_{1}\rangle|i^{B}_{2}m^{B}_{2}\rangle|\ell m_{\ell}\rangle|N_{\sigma}\rangle|N_{\pi}\rangle,(11)

which consists of the product of molecule basis sets for each moleculeX=A,BX=A,B,
a partial wave basis set|ℓ​mℓ⟩|\ell m_{\ell}\ranglethat describes the end-over-end rotation of the two molecules about one another,
and again the Hamiltonians describing both fields.
We note that in this work, we do not actually simultaneously include hyperfine and microwave fields, though we include both in different calculations.
Subsequently, the basis set is adapted to permutation symmetry of identical particles by projecting with1±P^1\pm\hat{P}, and appropriately normalizing, whereP^\hat{P}permutes moleculesAAandBB[83].
The upper (lower) sign applies for identical bosons (fermions).
The total basis is further limited by including functions only for one value of the conserved generalized angular momentum projectionℳ=mA+m1A+m2A+mB+m1B+m2B+mℓ+Nσ,\displaystyle\mathcal{M}=m^{A}+m_{1}^{A}+m_{2}^{A}+m^{B}+m_{1}^{B}+m_{2}^{B}+m_{\ell}+N_{\sigma},(12)

and parity ofℓ\ell.
Next an asymptotic basis set is determined by numerically diagonalizing the Hamiltonian excluding interaction terms for each value ofℓ\ell,mℓm_{\ell}.
Required matrices such as the asymptotic Hamiltonian, centrifugal angular momentum, and the interaction are transformed to this permutation-adapted asymptotic representation, in which all scattering calculations are performed.
The basis set is typically truncated by including functions withj≤2j\leq 2,ℓ≤5\ell\leq 5, and including no vibrational states excited further higher than the initial state under consideration.

We propagate two linearly independent sets of solutions to the coupled-channels equations using the renormalized Numerov method of Ref.[86,87].
We then impose capture boundary conditions at short distances.
At asymptotically large distances, we impose the usualSS-matrix boundary conditions corresponding to unit incoming flux in the entrance channel and outgoing flux in all energetically accessible channels.
With these boundary conditions, results are converged with a radial grid ranging from5050to50 00050\,000α0\alpha_{0}with at least3030points per local de Broglie wavelength for NaK.
For KAg, a radial grid extend from1 1391\,139to10710^{7}α0\alpha_{0}, with a minimum of3030grid points per local de Broglie wavelength is used.
From theseSS-matrix we compute elastic and inelastic cross sections, see Ref.[32]

Thermal rate coefficients are calculated by averaging these cross sections over the Maxwell-Boltzmann distribution for a given temperature, where we perform the integration using 19 logarithmically spaced collision energies between10−1010^{-10}and10−510^{-5}K.

Low-energy scattering can be characterized by thess-wave scattering length,asa_{s},
which can be extracted from theSS-matrix asas=limE→01−Si,0,0;i,0,0​(E)i​k​[1+Si,0,0;i,0,0​(E)],\displaystyle a_{s}=\lim_{E\rightarrow 0}\ \frac{1-S_{i,0,0;\ i,0,0}(E)}{ik\left[1+S_{i,0,0;\ i,0,0}\left(E\right)\ \right]},(13)

whereSi,0,0;i,0,0S_{i,0,0;\ i,0,0}is theSS-matrix diagonal element corresponding to thess-wave initial channel.
TheSS-matrix is obtained from the coupled-channels calculations described above.
We numerically confirm that the scattering length is energy independent at the lowest energies, typically in the pK to nK range.

## VCollision rates

The goal of our coupled-channel calculations is to quantitatively put these interaction mechanisms to the test. Specifically, we aim to demonstrate that the ro-vibrational vdW interaction drastically suppresses inelastic collisions,
and boost elastic collisions.
To this end, we evaluate the loss rates for collisions of two fermionic NaK molecules as a representative system.

The resulting inelastic collision rates at a temperature of 1 nK are shown in Fig,3.
One molecule is prepared inv=0v=0while the second is prepared inv′v^{\prime}as indicated by the horizontal axis.
If thev=0v=0molecule is in rotationalj=0j=0, and thev′>0v^{\prime}>0molecule is inj=1j=1,
the ro-vibrational van der Waals interaction is attractive.
This results in universal short-range loss at a rate proportional toR6∝C61/4R_{6}\propto C_{6}^{1/4},
such that the resulting rate coefficient decreases only slowly withv′v^{\prime}, which scales the energy defect.
In case thev=0v=0molecule is prepared in rotational statej=1j=1, and thev′>0v^{\prime}>0molecule is prepared inj=0j=0, the situation is reversed, and the ro-vibrational van der Waals interaction is repulsive.
This suppresses collisional loss by some seven orders of magnitude.
In both cases, ifv′=0v^{\prime}=0, the interactions are instead given by resonant dipole-dipole couplings, which are longer-ranged and lead to substantially faster collisional loss.

When repulsive ro-vibrational vdW interactions suppress collisional loss,
we find that the residual loss rate is sensitive to the hyperfine state,
shown as the markers in Fig.3.
When the molecules are prepared in an excited hyperfine state,
the loss rate coefficient is orders of magnitude higher than that obtained in the hyperfine-free calculation, shown as the solid lines.
We verify that this additional loss is entirely attributed to hyperfine relaxation, that is, inelastic transitions to lower hyperfine levels within the same(v,j)+(v′​j′)(v,j)+(v^{\prime}j^{\prime})manifold.
However, when the molecules are prepared in their hyperfine ground state,
this relaxation is energetically forbidden, and the loss rate coefficient is suppressed essentially to the hyperfine-free level.Figure 3:Rotation-vibration state dependenceof the loss rate for fermionic NaK at 1 nK and a magnetic fieldBBof 500 gauss.
At thisBBfield,
the lowest hyperfine ismINa=3/2m_{I_{\mathrm{Na}}}=3/2,mIK=−4m_{I_{\mathrm{K}}}=-4andMF=−5/2M_{F}=-5/2or−3/2-3/2forj=0j=0or11, respectively.
The excited hyperfine state shown is|mINa,mIK,mF⟩=|3/2,−3,−3/2⟩|m_{I_{\mathrm{Na}}},m_{I_{\mathrm{K}}},m_{F}\rangle=|3/2,-3,-3/2\rangleforj=0j=0,
and|3/2,−4,−7/2⟩|3/2,-4,-7/2\rangleforj=1j=1.

The results shown in Fig.3are for a magnetic fieldB=500B=500G.
The full magnetic field dependence is shown in Fig.4. At low fields, the loss rates for both the lowest and excited hyperfine states are comparable (10−14−10−1210^{-14}-10^{-12}cm3/s). As the magnetic field approachesB=20B=20G, the loss rate for the lowest hyperfine state is suppressed by two orders of magnitude, dropping to the hyperfine-free result. Above this thresholdBBvalue, the ground-state loss rate is essentially constant, demonstrating that a small magnetic field of roughly2020G is sufficient to suppress residual loss due to hyperfine relaxation. The loss rate for the excited hyperfine state does not experience this suppression and instead shows a slight increase with the field.Figure 4:Magnetic field dependence of collisional lossrate for fermionic NaK molecules in the lowest and excited hyperfine states of(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0)as a function of magnetic field at 1 nK. NearB=20B=20G, the loss rate for the lowest hyperfine state exhibits a suppression of approximately two orders of magnitude, while the excited hyperfine state shows a slight increase.

## VIUniversalityFigure 5:Universal scaling of the scattering lengthfor ro-vibrational van der Waals repulsion.
The universal relation is calculated in a minimal model that only accounts for the pair states(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0)to(0,0)+(1,1)(0,0)+(1,1), split by2​αe2\alpha_{e}, see main text.
Panels (a) and (b) shows the real and imaginary part of the scattering length, respectively.
The scattering length is expressed in dipolar length units,
and shown as a universal function of the dimensionless parameterαe/Ed\alpha_{e}/E_{d}.
Markers indicate the results of full coupled-channels calculations for NaK and KAg,
and the agreement with the minimal model verifies the universality.

Next, we consider the universality of the ro-vibrational van der Waals interaction for linear diatomic molecules.
The essence of the repulsive interaction is the dipole-dipole coupling between pairs of molecule states(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0)to(0,0)+(1,1)(0,0)+(1,1).
The dipolar interaction is characterized by a dipolar lengthRd=m​d2/8​π​ϵ0​ℏ2R_{d}=md^{2}/8\pi\epsilon_{0}\hbar^{2}and energy scaleEd=ℏ2/m​Rd2E_{d}=\hbar^{2}/mR_{d}^{2},
and the energy defect2​αe2\alpha_{e}sets an additional energy and associated length scale.
The zero-energy collision properties, characterized by the scattering length,asa_{s},
do not depend on any other length or energy scales,
whereas at finite collision energy, the collision energy itself and the associated de Broglie wavelength set an additional energy and length scale.
Hence, we expect thatas/Rda_{s}/R_{d}is a universal function of the ratioαe/Ed\alpha_{e}/E_{d},
meaning thatas/Rda_{s}/R_{d}can dependonlyon the ratioαe/Ed\alpha_{e}/E_{d}, but it cannot depend on molecular constants in any other way.
Another way of phrasing this is that different combinations of molecular parameters (mass, dipole moment, or rotation-vibration coupling constant) that lead to the same ratioαe/Ed\alpha_{e}/E_{d}, lead to the sameas/Rda_{s}/R_{d}.

This is perhaps clearest for the elastic properties,
for which we can ignore the unlikely non-adiabatic transitions that correspond to inelastic collisions,
and consider collisions on the upper repulsive adiabatic potential.
This is essentially a repulsive van der Waals potential,
for which[88]as/R6=−Γ​(−14)2​Γ​(14)≈0.676.\displaystyle{a_{s}}/{R_{6}}=-\frac{\Gamma(-\frac{1}{4})}{2\Gamma(\frac{1}{4})}\approx 0.676.(14)

UsingC6=de4/9​αeC_{6}=d_{e}^{4}/9\alpha_{e},Rd/R6=(9​αe/4​Ed)1/4R_{d}/R_{6}=(9\alpha_{e}/4E_{d})^{1/4}, this givesas/Rd≈0.552​(αeEd)−1/4.\displaystyle a_{s}/R_{d}\approx 0.552\left(\frac{\alpha_{e}}{E_{d}}\right)^{-1/4}.(15)

For the imaginary part of the scattering length, we determine the dependence onαe/Ed\alpha_{e}/E_{d}numerically by performing coupled channels calculations limited to the two essential pairs of molecule states(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0)to(0,0)+(1,1)(0,0)+(1,1).
Here, we find a scaling close to the power-law−Im​[as]/Rd∝(αe/Ed)−2-\mathrm{Im}[a_{s}]/R_{d}\propto(\alpha_{e}/E_{d})^{-2}.
The numerical results for both the real and imaginary parts of the scattering length are shown in Fig.5.

Real molecules have additional energy levels, in addition to the essential pairs of molecule states(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0)to(0,0)+(1,1)(0,0)+(1,1), considered above.
These energy levels are separated from these channels by an amount that depends not only onαe\alpha_{e},
but also on the rotational constantBeB_{e}, for example.
These additional energy scales could in principle break the universality.
Here, we verify numerically that for representative molecules, these additional energy scales play no role and the simple universality discussed above holds.
To this end we performed coupled-channels calculations that include the full ro-vibrational energy structure of NaK and KAg molecules.
The resulting scattering lengths, shown as markers in Fig.5, agree closely with the universal result.

We note that, in order to simplify the discussion above, we have ignored the existence of a second dipolar length and energy scale,Rd′R_{d}^{\prime}andEd′E_{d}^{\prime}, set by the vibrational transition dipole moment.
This leads to first-order dipolar interactions in each of the essential channels of the molecular pair(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0)and(0,0)+(1,1)(0,0)+(1,1).
The existence of this interaction energy scale –like the molecules internal energy level structure– in principle could break universality.
However, we neglected this interaction in our universal minimal model,
but included it in our full coupled-channels calculations,
such that the agreement between the two establishes that the vibrational off-diagonal dipolar interaction plays no role for representative ultracold molecules.
Finally, the hyperfine structure of real molecules sets further energy scales that are not included in the present discussion,
but we have already demonstrated in Sec.Vthat hyperfine plays no role for molecules prepared in their hyperfine ground states.

From this universality we can understand the effectiveness of the ro-vibrational vdW interaction and its dependence on molecular parameters.
Largerαe\alpha_{e}suppresses non-adiabatic transitions from the upper repulsive potential to the lower attractive one,
which in the universal two-level description is the only loss channel.
The inelastic part of the scattering length is significantly suppressed as−Im​[as]∝αe−2-\mathrm{Im}[a_{s}]\propto\alpha_{e}^{-2}.
Increasingαe\alpha_{e}also results in a weak suppression of the elastic part of the scattering lengthRe​[as]∝αe−1/4\mathrm{Re}[a_{s}]\propto\alpha_{e}^{-1/4}.
Since the imaginary part of the scattering length is suppressed much more strongly than the real part,
the ro-vibrational vdW interaction can be considered more effective for largerαe\alpha_{e}.
At fixedαe\alpha_{e}, we have the scalingRe​[as]∝Rd1/2\mathrm{Re}[a_{s}]\propto R_{d}^{1/2}whileIm​[as]∝Rd−3\mathrm{Im}[a_{s}]\propto R_{d}^{-3}.
This implies that when going to more dipolar species, at fixedαe\alpha_{e},
the elastic cross section grows while the inelastic cross section is suppressed further.
As shown in Fig.5, these effects result in ro-vibrational vdW interactions that become orders of magnitude more effective when transitioning from NaK to theultrapolarKAg.

## VIIDirect evaporation of a Fermi MixtureFigure 6:Collision rates in a Fermi mixturefor various pairs of rotational-vibrational state of (a) NaK and (b) KAg as a function of temperature.

Cooling down to a degenerate quantum gas of fermions has so far been achieved by assembly from deeply degenerate atoms[25,89],
and by evaporative cooling[26,27,90,84,28,29,30].
Efficient evaporative cooling requires a high “γ\gammaratio” of elastic to inelastic collision rates.
For molecules, this has generally required the suppression of collisional loss by shielding,
where external fields are used to engineer repulsive long-range interactions between molecules.
Here, we consider direct evaporation without active collisional shielding using external fields by using a mixture of fermionic molecules inv,j=0,1v,j=0,1andv′,j′=1,0v^{\prime},j^{\prime}=1,0states.

For a pair of molecules in the same internal state,
the dominant interaction is the rotational van der Waals interaction,
which results in universal loss[82].
For fermionic molecules, thesepp-wave collisions lead to elastic and inelastic cross sections that are suppressed at low temperature asT2T^{2}andTT, respectively.
For a pair of molecules in different internal states,
the dominant interaction is the ro-vibrational van der Waals interaction.
These collisions can proceed byss-wave,
leading toT1/2T^{1/2}andT0T^{0}scaling of the elastic and inelastic collision rates.
In absolute terms, the elastic collision rate which is proportional toR62∝C61/2R_{6}^{2}\propto C_{6}^{1/2}is enhanced by orders of magnitude for the stronger ro-vibrational interaction, when compared to the rotational one.
The inelastic rate is suppressed by orders of magnitude due to the repulsive ro-vibrational vdW interaction.

Figure6(a) shows the relevant collision rates quantitatively for NaK molecules at temperatures between 1 nK and 1μ\muK.
The rates for inelasticss-wave collisions between molecules in different internal states and for elasticpp-wave collisions between molecules in identical internal states are so far suppressed that they play essentially no role.
The elasticss-wave rate dominates over the inelasticpp-wave rate by a factor of 15 atT=1​μT=1~\muK,
and this “γ\gammaratio” of elastic-to-inelastic collisions improves substantially towards lower temperature in accordance with the Wigner threshold laws.

Figure6(b) shows the relevant collision rates for KAg molecules.
Based on the universality discussed in Sec.VI,
we expect the elasticss-wave collision rate to scale asRd​(kB​T/αe)1/2R_{d}(k_{B}T/\alpha_{e})^{1/2}for the ro-vibrational van der Waals interaction,
while thepp-wave inelastic rate scales asRd3/2​kB​T​Be−3/4R_{d}^{3/2}\ k_{B}T\ B_{e}^{-3/4}for the rotational van der Waals interaction[82].
Therefore, theγ\gammaratio at fixed temperature is expected to scale asRd−1/2R_{d}^{-1/2},
leading to a small decrease for the ultrapolar molecules.
The reduction ofαe\alpha_{e}andBeB_{e}for KAg compared to NaK lead to a small increase and decrease of theγ\gammaratio, respectively.
In general, the scaling of theγ\gammaratio with molecular parameters is not very steep.
The more qualitative difference between the two cases is the onset of threshold scaling of the collision rates,
which occurs at lower temperature for KAg due to the lower dipolar energy scale.

In general we can conclude the ro-vibrational vdW interaction can enable direct evaporation of Fermi mixtures of molecules in different vibrational states.
The scaling of theγ\gammaratio at fixed absolute temperature(Rd​αe)−1/2(R_{d}\,\alpha_{e})^{-1/2}indicates the ratio is better for smaller vibration rotation coupling constantα\alpha, which boosts the elastic cross section,
and forlessdipolar molecules, because a stronger dipolar interaction boosts the inelastic collision rate slightly more than the elastic one.
However, these scalings scalings are not steep enough to create order of magnitude performance differences between different molecules.
Theγ\gammaratio is thus expected to be roughly on the order of tens around microkelvin temperatures,
and to further improve at lower temperature, for many molecules.
Thisγ\gammaratio is not as comfortably high as what can be achieved by active collisional shielding[28,29,30],
but it could enable evaporative cooling simply by creating a mixture of different vibrational states without active external field control of the collisions.

## VIIIDiscussion

We believe that the ro-vibrational van der Waals interactions described in this work will enable new strategies for controlling collisions and interactions between ultracold molecules,
leading a multitude of powerful applications in quantum simulation and many-body physics.
In addition to enabling direct evaporation of Fermi mixtures discussed above, in Sec.VII,
we briefly discuss some opportunities here.

The ro-vibrational van der Waals interactions introduced in this work can be combined with active collisional shielding techniques, specifically double microwave shielding[29,32]. Double microwave shielding utilizesσ+\sigma^{+}andπ\pi-polarized microwave fields detuned from thej=0→1j=0\to 1rotational transition, to engineer a repulsive long-range barrier that suppresses collisional losses for molecules in their ground vibrational state.
These microwave fields can simultaneously shield molecules occupying different vibrational states such asv=0v=0andv=1v=1.
Because of the rotation-vibration coupling, thej=0→1j=0\to 1transition energy in the vibrationally excitedv=1v=1state is smaller than that of thev=0v=0ground state by2​αe2\alpha_{e},
which is on the order of MHz and therefore comparable to typical Rabi frequencies and detunings used in double microwave shielding.
Consequently, the two microwave fields dressing thev=0v=0molecules act simultaneously on thev=1v=1manifold, simply with an effective detuning shifted by+2​αe+2\alpha_{e}.
It is possible to find microwave configurations —the two Rabi frequencies,Ωσ,Ωπ\Omega_{\sigma},\Omega_{\pi}, and the two detunings,Δσ,Δπ\Delta_{\sigma},\Delta_{\pi}— that simultaneously suppress two-body loss rates for collisions involving molecules in both vibrational states.
As an example, Fig.7shows computed two-body loss rates for the NaCs molecule in a specific microwave field configuration, demonstrating the suppression of losses for all identical (v=0+v=0v=0+v=0andv=1+v=1v=1+v=1) and distinguishable (v=0+v=1v=0+v=1) collisions.Figure 7:Simultaneous double microwave shieldingof ground and excited vibrational states. Two-body loss rates,klossk_{\mathrm{loss}}, as a function of the detuning of theπ\pi-polarized microwave field,Δπ\Delta_{\pi}. Calculations performed for NaCs atΩσ=44.7×2​π​MHz,Ωπ=Δσ=22.4×2​π​MHz\Omega_{\sigma}=44.7\times 2\pi\,\mathrm{MHz},\,\Omega_{\pi}=\Delta_{\sigma}=22.4\times 2\pi\,\mathrm{MHz}.

The ability to simultaneously shield molecules in different vibrational states opens up exciting avenues for quantum simulation and spin physics. By preparing a stable mixture of vibrationally ground and excited molecules, one can encode a pseudo-spin1/21/2system where the field-dressedv=0v=0andv=1v=1states serve as the effective spin quantum numbers.
Double microwave shielding then ensures not only the collisional stability of the gas, but also provides tunability of the effective interactions between these pseudo-spin states via the induced dipolar interactions.
Specifically, this enables realization of a tunable dipolar density-density, spin-density, and Ising exchange interactions in a collisionally stable gas.
This provides a robust platform for exploring quantum simulation and many-body physics with state-dependent long-range interactions, as detailed in the accompanying work[91].

The highly-tunable state-dependent interactions are also interesting in the polaron setting,
where we envision creating impurities of molecules inv=1v=1in a bath ofv=0v=0molecules, for example.
Double microwave shielding can simultaneously stabilize the bath and impurity with respect to collisions.
It is possible to tune the microwave parameters such that the dipolar interaction betweenv=0v=0bath molecules switched off, or compensated.
Because the effective detuning forv=1v=1is different, however, dipolar interactions betweenv=1v=1impurity molecules andv=0v=0bath molecules are not compensated by the same microwave fields.
This realizes counter-intuitive “asymmetric” interactions[92];
Thev=0v=0bath molecules are effectively non-polar, but they have dipole-dipole interactions withv=1v=1impurity molecules.
That is, the dipole moment of thev=0v=0molecules appears to depend on their interaction partner.
Especially for the Fermi polaron this setting is interesting as it enables realizing a strongly interacting dipolar polaron with a non-interacting bath.
By tuning away from compensation dipolar interactions can be re-introduced in the bath,
which can lead to unconventionalppsuperfluidity,
and this new platform enables studying the competition between these various pairing mechanisms.
This setup is explored in the future work[93].

We also envision that the ro-vibrational vdW interaction may be a powerful tool to realize deterministic loading of tweezers with ultracold molecules, using schemes similar to that in Ref.[94].
The general strategy there was repeated loading of molecules into conservative trapping potentials using laser cooling.
Successfully loaded molecules are “shelved” in a rotationally excited state,
such that the shelved molecule is shielded from collisions with subsequently loaded molecules by the rotational vdW interaction.
A blockade is implemented to make sure only one molecule per tweezer can be shelved,
leading to high-probability loading of single molecules, realizing highly scalable tweezer arrays.
In this scheme, the probability of loading single molecules is limited to∼80%\sim 80~\%by residual collisional loss of molecules interacting by rotational vdW repulsion.
This limiting loading fidelity is comparable to what is possible by controlling light assisted collisions between atoms[95].
Since the ro-vibrational vdW interaction can be orders of magnitude more effective at suppressing collisional loss,
this novel interaction can substantially improve deterministic loading of molecules[96].

The ro-vibrational vdW interaction may also enable infrared shielding,
where molecules are prepared in identical internal states, e.g.v,j=1,0v,j=1,0,
and are dressed on the ro-vibrational transitionv,j=1,0⟷0,1v,j=1,0\longleftrightarrow 0,1.
As a result, a pair of molecules in states(v,j)+(v′,j′)=(1,0)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(1,0)+(1,0)is dressed with(1,0)+(0,1)(1,0)+(0,1)and(0,1)+(0,1)(0,1)+(0,1).
This dressing mixes in strongly repulsive ro-vibrational vdW interactions that could realize collisional shielding.
The difficulty is that for many molecules, the vibrational transition occurs in the terahertz regime where it is difficult to realize high power.
However, there are exceptions as for lighter molecules the vibrational transition are shifted further into the infrared.
For example, for NH molecules the vibrational transition is shifted to3​μ3~\mum[70,71].
The lifetime of vibrationally excited states is tens of miliseconds,
so that off-resonant dressing may be possible with one-body lifetimes approaching the second scale.
Whether this IR shielding can be effective is not immediately clear asαe≃19\alpha_{e}\simeq 19GHz is orders of magnitude larger than is typical for the heavier assembled molecules.
This should lead to a weaker ro-vibrational vdW repulsion, withC6ro−vib=de4/9​αe=5 000C_{6}^{\mathrm{ro-vib}}=d_{e}^{4}/9\alpha_{e}=5\,000a.u., but on the other hand the competing interactions are also weaker for this molecule.
For example, the rotational vdW interactionC6rot=de4/6​Be=280C_{6}^{\mathrm{rot}}=d_{e}^{4}/6B_{e}=280a.u. and the electronic vdW interactionC6elec=47C_{6}^{\mathrm{elec}}=47a.u.[69].
Hence, the ro-vibrational vdW interaction is still the dominant interaction and future research may reveal whether this can realize effective IR shielding of NH molecules.

More broadly, the ro-vibrational vdW interaction discovered here is a novel resource for interaction control in different internal states.
A setting in which this interaction is naturally accessed is quantum simulation with synthetic dimensions[23,24]encoded in ro-vibrational degrees of freedom.
Ro-vibrational vdW repulsion can also be a powerful tool for quantum simulation with fermionic molecules in optical lattices,
where tunneling of two molecules onto the same lattice site can otherwise lead to collisional loss.
Together with the applications of Fermi mixture evaporation, tunably interacting spin mixtures[91,93], enhanced tweezer loading[96], and direct infrared shielding, discussed above,
we conclude that the ro-vibrational vdW interaction can be a powerful resource with many potential applications for quantum science and many-body physics with ultracold molecules.

## IXAcknowledgement

We thank Edvardas Narevicius, Sebastian Will, Ian Stevenson, Eugen Dizer, Arthur Christianen and Richard Schmidt for useful discussions.
We thank Jacek Koput, Lukáš Pašteka and Anastasia Borschevsky for sharing ab initio calculations.
This work was supported by NWO VIDI (grant ID 10.61686/AKJWK33335).
The research was funded by the European Union (Project No. 101269084, HORIZON-MSCA-2025-PF, 2STICKY). The views and opinions expressed are, however, those of the authors only
and do not necessarily reflect those of the European Union or the European Research Executive Agency. Neither
the European Union nor the granting authority can be held responsible for them.

## Appendix AVibrational vdW

For many molecules, the vibrational transition dipole moment is smaller than for rotational transitions,
and the energy defect on the order ofωe\omega_{e}is orders of magnitude larger than rotational excitation energies.
This results in a vibrational vdW interaction that is orders of magnitude weaker than rotational vdW.

There is an exception to this, which is for transitions of the typev,v′→v−1,v′+1v,v^{\prime}\rightarrow v-1,v^{\prime}+1,
where the energy denominator is on the order of the anharmonicityωe​xe\omega_{e}x_{e}.
The anharmonicityωe​xe\omega_{e}x_{e}is typically only a few times larger than the rotational constant,BeB_{e},
and both are on the GHz scale for many molecules that we consider, see Table.1.
Therefore, it is even possible to find transitions for which the rotational excitation and vibrational de-excitation energies can cancel to a large extent.
For example, the transition(v,j)+(v,j)=(1,2)+(1,2)→(0,3)+(2,3)(v,j)+(v,j)=(1,2)+(1,2)\rightarrow(0,3)+(2,3)has an energy denominator that is2​ωe​xe−12​Be+18​αe2\omega_{e}x_{e}-12B_{e}+18\alpha_{e},
which for most molecules considered is only a few percent of the anharmonicity.
For KAg, for example, this energy denominator is∼40%\sim 40~\%of the rotational constant,
i.e. an order of magnitude smaller than the4​Be4B_{e}energy denominator for rotational vdW for molecules in their ground state.
What is interesting about this, apart from the small energy denominator, is that this can lead to repulsive vdW interactions between two molecules in the same internal state, herev,j=1,2v,j=1,2, such that this could be applied to a bulk gas of molecules in the same internal state.Figure 8:Vibrational vdW Interaction.Collisional loss rate for KAg molecules inv,j=1,2v,j=1,2as a function of artificial scaling of the vibrational transition dipole moment.
When the vibrational transition dipole moment is scaled by a factor∼50\sim 50, it is made comparable to the transtition dipole for purely rotational transitions.
In this case, virtual de-excitation(v,j)+(v′,j′)=(1,2)+(1,2)→(0,3)+(2,3)(v,j)+(v^{\prime},j^{\prime})=(1,2)+(1,2)\rightarrow(0,3)+(2,3)suppresses loss by a repulsive vibrational vdW interaction.
For any real molecule, however, the vibrational transition dipole moment is weaker than the rotational one by more than an order of magnitude,
and we conclude that this vibrational vdW cannot be effective.

Despite it being possible to realize order-of-magnitude smaller energy denominators when compared to purely rotational transitions,
the vibrational transition dipole moments are one to several orders of magnitude smaller than the rotational ones,
depending strongly on the molecular species.
Due to the steep scaling of theC6∝de4/Δ​EC_{6}\propto d_{e}^{4}/\Delta Ecoefficient with transition dipole moment,
this nevertheless makes the vibrational vdW interaction generally ineffective compared to the rotational one.
We demonstrate this in Fig8by showing that effective shielding by this vibrational vdW interaction for KAg molecules inv,j=1,2v,j=1,2requires artificially increasing the vibrational transition dipole moment by a factor∼50\sim 50.
Therefore we conclude there exists no effective vibrational vdW interaction between ultracold polar molecules.

## References
- Karmanet al.[2024]T. Karman, M. Tomza, and J. Pérez-Ríos,Nature Phys.20, 722 (2024).
- Cooper and Shlyapnikov [2009]N. R. Cooper and G. V. Shlyapnikov,Phys. Rev. Lett.103, 155302 (2009).
- Gorshkovet al.[2011]A. V. Gorshkov, S. R. Manmana, G. Chen,
J. Ye, E. Demler, M. D. Lukin, and A. M. Rey,Phys. Rev. Lett.107, 115301 (2011).
- Micheliet al.[2006]A. Micheli, G. K. Brennen, and P. Zoller, Nature
Physics2, 341 (2006).
- Cornishet al.[2024]S. L. Cornish, M. R. Tarbutt, and K. R. Hazzard, Nature Physics20, 730
(2024).
- DeMille [2002]D. DeMille, Phys.
Rev. Lett.88, 067901
(2002).
- Ruttleyet al.[2025]D. K. Ruttley, T. R. Hepworth, A. Guttridge, and S. L. Cornish, Nature637, 827–832
(2025).
- Picardet al.[2025]L. R. Picard, A. J. Park,
G. E. Patenotte, S. Gebretsadkan, D. Wellnitz, A. M. Rey, and K.-K. Ni, Nature637, 821 (2025).
- Hollandet al.[2023]C. M. Holland, Y. Lu, and L. W. Cheuk, Science382, 1143 (2023).
- Baoet al.[2023]Y. Bao, S. S. Yu,
L. Anderegg, E. Chae, W. Ketterle, K.-K. Ni, and J. M. Doyle, Science382, 1138 (2023).
- DeMilleet al.[2024]D. DeMille, N. R. Hutzler, A. M. Rey, and T. Zelevinsky, Nature Physics20, 741 (2024).
- Safronovaet al.[2018]M. S. Safronova, D. Budker,
D. DeMille, D. F. J. Kimball, A. Derevianko, and C. W. Clark,Rev. Mod. Phys.90, 025008 (2018).
- Langenet al.[2024]T. Langen, G. Valtolina,
D. Wang, and J. Ye, Nature Physics20, 702 (2024).
- Wall and Carr [2010]M. L. Wall and L. Carr, Phys. Rev. A82, 013611 (2010).
- Trefzgeret al.[2011]C. Trefzger, C. Menotti,
B. Capogrosso-Sansone, and M. Lewenstein, J. Phys. B.44, 193001 (2011).
- Capogrosso-Sansoneet al.[2010]B. Capogrosso-Sansone, C. Trefzger, M. Lewenstein, P. Zoller, and G. Pupillo, Phys. Rev. Lett.104, 125301 (2010).
- Barnettet al.[2006]R. Barnett, D. Petrov,
M. Lukin, and E. Demler,Phys. Rev. Lett.96, 190401 (2006).
- Carrollet al.[2025]A. N. Carroll, H. Hirzler,
C. Miller, D. Wellnitz, S. R. Muleady, J. Lin, K. P. Zamarski, R. R. Wang, J. L. Bohn, A. M. Rey,et al., Science388, 381
(2025).
- Zhanget al.[2025]W. Zhang, H. Liu, F. Deng, K. Chen, S. Yi, and T. Shi, arXiv preprint arXiv:2506.23820 (2025).
- Langenet al.[2025]T. Langen, J. Boronat,
J. Sánchez-Baena,
R. Bombín, T. Karman, and F. Mazzanti, Phys. Rev. Lett.134, 053001 (2025).
- Ciardiet al.[2025]M. Ciardi, K. R. Pedersen, T. Langen, and T. Pohl, Phys. Rev. Lett.135, 153401 (2025).
- Mukherjeeet al.[2025]B. Mukherjee, J. M. Hutson, and K. R. Hazzard, New.
J. Phys.27, 013013
(2025).
- Sundaret al.[2018]B. Sundar, B. Gadway, and K. R. Hazzard, Scientific
reports8, 3422
(2018).
- Fenget al.[2022]C. Feng, H. Manetsch,
V. G. Rousseau, K. R. Hazzard, and R. Scalettar, Phys. Rev. A105, 063320 (2022).
- De Marcoet al.[2019]L. De Marco, G. Valtolina,
K. Matsuda, W. G. Tobias, J. P. Covey, and J. Ye,Science363, 853 (2019).
- Valtolinaet al.[2020]G. Valtolina, K. Matsuda,
W. G. Tobias, J.-R. Li, L. De Marco, and J. Ye,Nature588, 239 (2020).
- Matsudaet al.[2020]K. Matsuda, L. De Marco,
J.-R. Li, W. G. Tobias, G. Valtolina, G. Quéméner, and J. Ye,Science370, 1324 (2020).
- Schindewolfet al.[2022]A. Schindewolf, R. Bause,
X.-Y. Chen, M. Duda, T. Karman, I. Bloch, and X.-Y. Luo,Nature607, 677 (2022).
- Bigagliet al.[2024]N. Bigagli, W. Yuan,
S. Zhang, B. Bulatovic, T. Karman, I. Stevenson, and S. Will,Nature631, 289 (2024).
- Shiet al.[2025]Z. Shi, Z. Huang, F. Deng, W.-J. Jin, S. Yi, T. Shi, and D. Wang,Bose-einstein
condensate of ultracold sodium-rubidium molecules with tunable dipolar
interactions(2025),arXiv:2508.20518 [cond-mat.quant-gas].
- Yuanet al.[2025]W. Yuan, S. Zhang,
N. Bigagli, H. Kwak, C. Warner, T. Karman, I. Stevenson, and S. Will, arXiv preprint arXiv:2505.08773 (2025).
- Karmanet al.[2025]T. Karman, N. Bigagli,
W. Yuan, S. Zhang, I. Stevenson, and S. Will,PRX Quantum6, 020358 (2025).
- Chenet al.[2023]X.-Y. Chen, A. Schindewolf,
S. Eppelt, R. Bause, M. Duda, S. Biswas, T. Karman, T. Hilker, I. Bloch, and X.-Y. Luo,Nature614, 59 (2023).
- Zhanget al.[2026]S. Zhang, W. Yuan,
N. Bigagli, H. Kwak, T. Karman, I. Stevenson, and S. Will,Nature651, 601–606 (2026).
- Schindewolfet al.[2025]A. Schindewolf, J. Hertkorn, I. Stevenson,
M. Ciardi, P. Gross, D. Wang, T. Karman, G. Quemener, S. Will, T. Pohl,et al., arXiv preprint arXiv:2512.14511 (2025).
- Walraven and Karman [2024]E. F. Walraven and T. Karman,Phys. Rev. A109, 043310 (2024).
- Walraven and Karman [2025]E. F. Walraven and T. Karman,Phys. Rev. A112, 032810 (2025).
- Yeet al.[2018]X. Ye, M. Guo, M. L. González-Martínez,
G. Quéméner, and D. Wang, Science advances4, eaaq0083 (2018).
- Kozyryev and Hutzler [2017]I. Kozyryev and N. R. Hutzler, Phys.
Rev. Lett.119, 133002
(2017).
- Hutzler [2020]N. R. Hutzler, Quantum Science & Technology5, 044011 (2020).
- Anderegget al.[2023]L. Anderegg, N. B. Vilas,
C. Hallas, P. Robichaud, A. Jadbabaie, J. M. Doyle, and N. R. Hutzler, Science382, 665 (2023).
- Augustovičová and Bohn [2019]L. D. Augustovičová and J. L. Bohn, New. J. Phys.21, 103022 (2019).
- Vilaset al.[2026]N. B. Vilas, P. Robichaud,
C. Hallas, J. Tao, L. Anderegg, G. K. Li, H. Lampson, L. D. Augustovičová, J. L. Bohn, and J. M. Doyle, Phys. Rev. X16, 021001 (2026).
- Niet al.[2008]K.-K. Ni, S. Ospelkaus,
M. De Miranda, A. Pe’Er, B. Neyenhuis, J. Zirbel, S. Kotochigova, P. Julienne, D. Jin, and J. Ye, Science322, 231 (2008).
- Takekoshiet al.[2014]T. Takekoshi, L. Reichsöllner, A. Schindewolf, J. M. Hutson, C. R. Le Sueur, O. Dulieu,
F. Ferlaino, R. Grimm, and H.-C. Nägerl, Phys. Rev. Lett.113, 205301 (2014).
- Molonyet al.[2014]P. K. Molony, P. D. Gregory,
Z. Ji, B. Lu, M. P. Köppinger, C. R. Le Sueur, C. L. Blackley, J. M. Hutson, and S. L. Cornish, Phys. Rev. Lett.113, 255301 (2014).
- Parket al.[2015]J. W. Park, S. A. Will, and M. W. Zwierlein, Phys. Rev. Lett.114, 205302 (2015).
- Guoet al.[2016]M. Guo, B. Zhu, B. Lu, X. Ye, F. Wang, R. Vexiau, N. Bouloufa-Maafa, G. Quéméner, O. Dulieu, and D. Wang, Phys. Rev. Lett.116, 205303 (2016).
- Stevensonet al.[2023]I. Stevenson, A. Z. Lam,
N. Bigagli, C. Warner, W. Yuan, S. Zhang, and S. Will,Phys. Rev. Lett.130, 113002 (2023).
- Zhelyazkovaet al.[2014]V. Zhelyazkova, A. Cournol, T. E. Wall,
A. Matsushima, J. J. Hudson, E. Hinds, M. Tarbutt, and B. Sauer, Phys. Rev. A89, 053416 (2014).
- Shumanet al.[2010]E. S. Shuman, J. F. Barry, and D. DeMille, Nature467, 820 (2010).
- Rockenhäuseret al.[2024]M. Rockenhäuser, F. Kogel, T. Garg,
S. A. Morales-Ramírez, and T. Langen, Phys. Rev. Res.6, 043161 (2024).
- Collopyet al.[2018]A. L. Collopy, S. Ding,
Y. Wu, I. A. Finneran, L. Anderegg, B. L. Augenbraun, J. M. Doyle, and J. Ye, Phys. Rev. Lett.121, 213201 (2018).
- Dunham [1932]J. Dunham, Phys.
Rev.41, 721 (1932).
- Pekeris [1934]C. L. Pekeris,Phys. Rev.45, 98 (1934).
- Kratzer [1920]A. Kratzer, Zeits. f. Physik3, 289
(1920).
- Burkhardt and Leventhal [2007]C. E. Burkhardt and J. J. Leventhal,Am. J. Phys.75, 686 (2007).
- Docenkoet al.[2004]O. Docenko, M. Tamanis,
R. Ferber, A. Pashov, H. Knöckel, and E. Tiemann, Eur. Phys. J. D31, 205 (2004).
- [59]O. Docenko, M. Tamanis,
R. Ferber, H. Knöckel, and E. Tiemann, Phys. Rev. A .
- Pashovet al.[2005]A. Pashov, O. Docenko, M. Tamanis, R. Ferber, H. Knöckel, and E. Tiemann,Phys. Rev. A72, 062505 (2005).
- Pashovet al.[2007]A. Pashov, O. Docenko,
M. Tamanis, R. Ferber, H. Knöckel, and E. Tiemann,Phys. Rev. A76, 022511 (2007).
- Steinkeet al.[2012]M. Steinke, H. Knöckel, and E. Tiemann,Phys. Rev. A85, 042720 (2012).
- Ferberet al.[2009]R. Ferber, I. Klincare,
O. Nikolayeva, M. Tamanis, H. Knöckel, E. Tiemann, and A. Pashov, Phys. Rev. A80, 062501 (2009).
- Ivanovaet al.[2011]M. Ivanova, A. Stein,
A. Pashov, H. Knöckel, and E. Tiemann,J. Chem. Phys.134, 024321 (2011).
- Tiemannet al.[2009]E. Tiemann, H. Knöckel, P. Kowalczyk, W. Jastrzebski, A. Pashov,
H. Salami, and A. Ross, Phys. Rev. A79, 042716 (2009).
- Śmiałkowski and Tomza [2021]M. Śmiałkowski and M. Tomza, Phys. Rev. A103, 022802 (2021).
- Aymar and Dulieu [2005]M. Aymar and O. Dulieu, J. Chem. Phys.122(2005).
- Ladjimi and Tomza [2024]H. Ladjimi and M. Tomza,Phys. Rev. A109, 052814 (2024).
- Koput [2015]J. Koput, J.
Comput. Chem.36, 1286
(2015).
- Radford and Litvak [1975]H. Radford and M. Litvak, Chem.
Phys. Lett.34, 561
(1975).
- Wayne and Radford [1976]F. Wayne and H. Radford, Mol.
Phys.32, 1407 (1976).
- Törringet al.[1984]T. Törring, W. Ernst, and S. Kindt, J. Chem. Phys.81, 4614 (1984).
- [73]Private communication from Lukáš
Pašteka and Anastasia Borshevsky, based on MRCI calculations similar to
those reported in J. Chem. Phys.,151034302 (2019), but using a
smaller basis set.
- Huber and Herzberg [1979]K. P. Huber and G. Herzberg,Molecular Spectra and Molecular Structure(Springer US, 1979).
- Childset al.[1986]W. Childs, G. Goodman, and L. Goodman,J. Mol. Spectr.115, 215 (1986).
- Haoet al.[2019]Y. Hao, L. F. Pašteka,
L. Visscher, P. Aggarwal, H. L. Bethlem, A. Boeschoten, A. Borschevsky, M. Denis, K. Esajas, S. Hoekstra, K. Jungmann, V. R. Marshall, T. B. Meijknecht, M. C. Mooij, R. G. E. Timmermans, A. Touwen, W. Ubachs, L. Willmann, Y. Yin, A. Zapara, and N. eEDM
Collaboration),J. Chem. Phys.151, 034302 (2019).
- Andersonet al.[1994]M. A. Anderson, M. D. Allen, and L. M. Ziurys,Astrophys. J.424, 503 (1994).
- Ernstet al.[1985]W. Ernst, J. Kändler,
S. Kindt, and T. Törring, Chem. Phys. Lett.113, 351 (1985).
- Suenramet al.[1990]R. D. Suenram, F. J. Lovas,
G. T. Fraser, and K. Matsumura,J. Chem. Phys.92, 4724
(1990).
- Staanumet al.[2007]P. Staanum, A. Pashov,
H. Knöckel, and E. Tiemann, Phys. Rev. A75, 042513 (2007).
- Hartmannet al.[2019]T. Hartmann, T. A. Schulze, K. K. Voges,
P. Gersema, M. W. Gempel, E. Tiemann, A. Zenesini, and S. Ospelkaus, Phys. Rev. A99, 032711 (2019).
- Idziaszek and Julienne [2010]Z. Idziaszek and P. S. Julienne, Phys. Rev. Lett.104, 113202 (2010).
- Karman and Hutson [2018]T. Karman and J. M. Hutson, Phys.
Rev. Lett.121, 163401
(2018).
- Anderegget al.[2021]L. Anderegg, S. Burchesky,
Y. Bao, S. S. Yu, T. Karman, E. Chae, K.-K. Ni, W. Ketterle, and J. M. Doyle,Science373, 779 (2021).
- Bigagliet al.[2023]N. Bigagli, C. Warner,
W. Yuan, S. Zhang, I. Stevenson, T. Karman, and S. Will,Nature Phys.19, 1579 (2023).
- Janssenet al.[2013]L. M. Janssen, A. van der
Avoird, and G. C. Groenenboom, Phys. Rev. Lett.110, 063201 (2013).
- Karman [2023]T. Karman,J. Phys. Chem. A127, 2194 (2023),arXiv:2212.03065.
- [88]K. Pérez, J. W. Desroches, K. R. A. Hazzard, and T. Karman, Hubbard models with ultracold
shielded molecules in optical lattices, in
preparation.
- Dudaet al.[2023]M. Duda, X.-Y. Chen,
A. Schindewolf, R. Bause, J. von Milczewski, R. Schmidt, I. Bloch, and X.-Y. Luo, Nature Physics19, 720 (2023).
- Liet al.[2021]J.-R. Li, W. G. Tobias,
K. Matsuda, C. Miller, G. Valtolina, L. De Marco, R. R. Wang, L. Lassablière, G. Quéméner, J. L. Bohn,et al.,Nature Phys.17, 1144 (2021).
- Jóźwiaket al.[2026]H. J. Jóźwiak, H. Yang, E. Dizer,
A. Christianen, and T. Karman,Tunable state-dependent
interactions in collisionally stable mixtures of polar molecules(2026),arXiv:2607.25777
[cond-mat.quant-gas].
- Saffman and Mølmer [2009]M. Saffman and K. Mølmer, Phys. Rev. Lett.102, 240502 (2009).
- [93]H. Yang, E. Dizer,
H. J. Jóźwiak,
R. Schmidt, A. Christianen, and T. Karman, Polarons in Microwave-Shielded Vibrational Mixtures of
Ultracold Molecules, in preparation.
- Walravenet al.[2024]E. F. Walraven, M. R. Tarbutt, and T. Karman,Phys. Rev. Lett.132, 183401 (2024).
- Kaufman and Ni [2021]A. M. Kaufman and K.-K. Ni,Nature Phys.17, 1324 (2021).
- Walravenet al.[2026]E. F. Walraven, K. Feng,
J. Rodewald, M. R. Tarbutt, and T. Karman,Deterministic loading
of molecular arrays by microwave-assisted collisions(2026),arXiv:2607.25783
[physics.atom-ph].

## 


- 


Major funding support from
