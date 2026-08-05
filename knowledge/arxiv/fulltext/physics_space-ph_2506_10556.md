# Lambert's problem in orbital dynamics: a self--contained introduction

**arXiv ID**: 2506.10556v2
**Authors**: Lenox Helene Baloglou, Parneet Gill, Tonatiuh Sánchez-Vizuet
**Published**: 2025-06-12
**Categories**: physics.space-ph, math-ph, math.CA, physics.class-ph
**DOI**: 10.1140/epjp/s13360-026-07368-3
**HTML URL**: https://arxiv.org/html/2506.10556v2

## Abstract

Lambert's problem is a classical boundary value problem in analytical mechanics. It arises when trying to determine the energy required to place a particle, subject to a central gravitational potential, in a "free fall" trajectory connecting two given points on a desired travel time. Due to its mathematical beauty and its relevance in aerospace engineering, it has been and remains the object of attention of countless engineers, mathematicians (pure and applied), and physicists seeking to produce efficient solution algorithms. In this expository article, didactic in nature, we present a unified and comprehensive derivation that assumes only a minimal background in physics and mathematics. We focus on the simplest unperturbed case and carefully develop the argument for elliptical trajectories. The goal is to provide a single reference that can serve as an accelerated introduction for students and researchers interested in a quick introduction to the subject.

## Full Text

Lambert’s problem in orbital dynamics: a self–contained introduction
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
- 11institutetext:Lenox Helene Baloglou22institutetext:Department of Mathematics, The University of Arizona, USA.22email:lenoxbaloglou@arizona.edu33institutetext:Parneet Gill44institutetext:Department of Mathematics, The University of Arizona, USA.44email:pgill@arizona.edu55institutetext:Tonatiuh Sánchez-Vizuet66institutetext:Department of Mathematics, The University of Arizona, USA. ORCID: https://orcid.org/0000-0002-8930-2798.66email:tonatiuh@arizona.edu

## Lambert’s problem in orbital dynamics: a self–contained introductionLenox Helene BaloglouAll authors were partially funded by the United States National Science Foundation through the grant NSF-DMS-2137305. Lenox H. Baloglou is thankful for the generous support of the University of Arizona’s RII-Sponsored Campuswide Undergraduate Student–Initiated Original Research Program.Parneet GillTonatiuh Sánchez-Vizuet

## Abstract

Lambert’s problem is a classical boundary value problem in analytical mechanics. It arises when trying to determine the energy required to place a particle, subject to a central gravitational potential, in afree falltrajectory connecting two given points on a desired travel time. Due to its mathematical beauty and its relevance in aerospace engineering, it has been and remains the object of attention of countless engineers, mathematicians (pure and applied), and physicists seeking to produce efficient solution algorithms. In this expository article, didactic in nature, we present a unified and comprehensive derivation that assumes only a minimal background in physics and mathematics. We focus on the simplest unperturbed case and carefully develop the argument for elliptical trajectories. The goal is to provide a single reference that can serve as an accelerated introduction for students and researchers interested in a quick introduction to the subject.

## 1Introduction

The goal of this expository article is didactic: we aim to provide a unified reference for readers who are comfortable with calculus, geometry and differential equations—but may not necessarily have strong background in physics—and are interested in the field of orbital dynamics in general and the Lambert problem in particular. All of the topics in this text are available in the literature—and have been available for a long while—however, a novice reader often has to spend a significant amount of time and effort jumping from one reference to another just to piece together a reasonably strong background before being able to tackle research–level questions. This was in fact the experience the two first authors—graduate students in applied mathematics interested in the use of surrogate methods for the solution of Lambert’s problemBaloglou2025;BaGiSa2025; this text grew out of their background–building efforts. Given the instructional goal and our target readership, we provide significantly more details in the calculations than what a typical research article—and even some textbooks—would do. We believe that this approach (and this reference itself) will be especially useful to students—and even researchers—in physics, astronomy, aerospace engineering and applied mathematics who find themselves in need of an accelerated introduction to the subject.

Lambert’s problem remains a very active field of research both from the purely mathematical point of view and from the practical application–oriented one. We hope that, with this accelerated minimal introduction, we can save the reader some time and provide them with the foundations that they will need to take a deeper dive into the multiple theoretical and practical complications of the field. Some of these include dealing with dragUrena2023, multiple revolutions and gravitational perturbationsArmellin2018;arora2013;Eagle;Panicucci2018;Woollands2017, uncertainty and stochasticityAdurthi2020;Schumacher2015;Teter2025;Zhang2018, and the development of robust and efficient computational algorithmsBaGiSa2025;Gueho2020;Thompson2020;Yang2022, among many others.

Part of the beauty of orbital dynamics is that it constitutes a natural connection between geometry, physics and calculus and our exposition attempts to emphasize this connection. In Section2, we start by providing a brief introduction to the Apollonian description of conic sections and their analytic geometry. This description is not often covered in elementary classes and yet it provides the most natural framework for Keplerian dynamics. We then move on to a minimal introduction to the physical concepts required. This material is part of the standard curriculum of an introductory physics class, but may not be familiar to a reader with a background in mathematics or computer science. Section3pertains to the more advanced subject of Keplerian dynamics. This subject is covered in classes of advanced mechanics (typically going by the names of theoretical or analytical mechanics) and once again we strive to synthesize just the necessary concepts to spare the reader the need for a semester–long incursion into this beautiful field. Having collected all the necessary material, Section4finally introduces Lambert’s problem and provides a careful derivation of Lagrange’s solution to it, all of which is typically found—although with a much terser exposition—in specialized texts and articles on orbital dynamics.

A few words about notation.
Throughout the text, we will use the following notational conventions:
- ∙\bullet

Scalar–valued quantities will be denoted with lightface and vector–valued quantities with boldface. Hence,rris a scalar and𝒓\bm{r}is a vector.
- ∙\bullet

Angular variables will be denoted by Greek letters.
- ∙\bullet

IfPPandQQare two points in space, the length of the straight line segment connecting them will be denoted by|P​Q||PQ|.
- ∙\bullet

IfPPis a point andLLis a line, then|P​L||PL|should be understood as the length of the line segment going through the pointPPand intersecting the lineLLat a right angle—this is the shortest distance betweenPPandLL.
- ∙\bullet

If𝑳\bm{L}is a vector, then|𝑳||\bm{L}|will denote its Euclidean magnitude.
- ∙\bullet

We will place a “hat”^\widehat{}on top of a vector whenever the Euclidean magnitude of said vector is equal to one. Therefore𝒓^\widehat{\bm{r}}implies that|𝒓|=1|\bm{r}|=1.
- ∙\bullet

The symbol:=:=denotes the fact that the quantity on the left isdefinedto be equal to the quantity on the right.
- ∙\bullet

Differentiation with respect to time will often (but not always) be denoted by a dot on top of a variable; the number of dots denotes the order of the derivative, i.e.x˙:=dd​t​x{\displaystyle\dot{x}:=\tfrac{d}{dt}x}andx¨:=d2d​t2​x{\displaystyle\ddot{x}:=\tfrac{d^{2}}{dt^{2}}x}.

## 2Preliminary background

## 2.1Conic sections

This section is a refresher—or crash course—on analytic geometry for conical sections. Since the natural coordinate system for the description of a particle moving under a central potential is a focus–centered polar system, except for a few comments, we will not delve on the Cartesian description. We start by introducing some simple notation. For two pointsP1P_{1}andP2P_{2}in the Euclidean plane we will denote by|P1​P2||P_{1}P_{2}|the length of the straight segment connecting them (i.e. their distance), while ifLLis a line andPPa point, the length of the shortest line segment passing throughPPand intersectingLLwill be denoted by|P​L||PL|.

Apollonian conics.There are several equivalent definitions of the conic sections. Perhaps the most well–known are the association between them and planar intersections of cones, and the characterization in terms of quadratic forms. However, the most useful one for our purposes will be the definition due to the Greek geometer Apollonius of PergaApollonius. The reason why we will use this definition is that it encompasses almost all of the definitions for conics in one single condition, in a way that is equivalent to thestandarddefinition in terms of quadratic forms(GlStOd2016,,  Theorem 2.1).

## Definition 1(besant1890;GlStOd2016)

Consider a pointFFin the Euclidean plane that we will callfocus, and a straight lineLLnot passing throughFFthat we will calldirectrix. For anye>0e>0, the set of points𝒞:={P∈ℝ2:|P​F|=e​|P​L|}\mathcal{C}:=\{P\in\mathbb{R}^{2}:|PF|=e|PL|\}

is called aconicwith associated focusFFand directrixLL. Moreover, we say that the conic𝒞\mathcal{C}is: an ellipse, if0<e<10<e<1, a parabola ife=1e=1, or a hyperbola ife>1e>1.

The line connectingFFwith its directrix at a right angle (depicted in solid black in Figure1) defines an axis of symmetry of the conic, known as themajororprincipalaxis. The pointVValong the segmentF​LFLand belonging to the conic is known as thevertex. As we shall now see, ellipses and hyperbolas have a second axis of symmetry and therefore a second focus and directrix, however the eccentricity (with respect to the second pair focus/directrix) remains unchanged. The following argument has been adapted from(GlStOd2016,,  Lemma 2.1.1).

Let’s consider a directrix/focus pair where the directrixLLis oriented in the vertical direction and the focusFFis located to its left at some distance|F​L||FL|. Placing a Cartesian frame of reference withxxaxis parallel to the major axis of symmetry and with itsyyaxis parallel to the directrixLL, we see that the focus has coordinates(−|F​L|,0)(-|FL|,0). Therefore, for a point with coordinates(x,y)(x,y), the condition in Definition (1) can be expressed as(x+|F​L|)2+y2=e2​x2.(x+|FL|)^{2}+y^{2}=e^{2}x^{2}.(1)

Ife=1e=1(the parabolic case) the quadratic term onxxdrops from the expression above, and it becomes clear that there will be only one point in the conic along the symmetry axis (i.e. withy=0y=0). On the other hand, assuming thate≠1e\neq 1the quadratic formula yieldsx=−|F​L|±|F​L|2−(1−e2)​(y2+|F​L|2)1−e2.x=\frac{-|FL|\pm\sqrt{|FL|^{2}-(1-e^{2})(y^{2}+|FL|^{2})}}{1-e^{2}}.(2)

Lettingy=0y=0above, we conclude that there are two distinct points along the axis of symmetry that belong to the conic. In other words, the conic will have two verticesV1V_{1}andV2V_{2}. The length of the line segment connecting them is given by|V1​V2|=2​e​|F​L||1−e2|.|V_{1}V_{2}|=\frac{2\,e|FL|}{\left|1-e^{2}\right|}.

Thesemi–major axis, familiar from the Cartesian description of conics, is defined to be half of this length, namelya:=e​|F​L||1−e2|.a:=\frac{e\,|FL|}{\left|1-e^{2}\right|}.(3)

For all values ofyyfor which Equation (2) is well defined, we see that there will be two points in the conic with the sameyycoordinate. Since the duplicity comes from the two branches of the square root, we conclude that there is second axis of symmetry—that we shall denote theminororsecondaryaxis—located along the vertical linexO=−|F​L|1−e2.x_{O}=-\frac{|FL|}{1-e^{2}}.

The point where the axes of symmetry intersect each other is known as thecenterof the conic and we shall denote it byO:=(−|F​L|1−e2,0).O:=\left(-\frac{|FL|}{1-e^{2}},\,0\right).

Settingx=xOx=x_{O}in (2) it is possible to solve foryyto obtainy=±|F​L|​e21−e2,y=\pm|FL|\sqrt{\frac{e^{2}}{1-e^{2}}},

which, in the elliptic case0<e<10<e<1, yields the value of theyycoordinate of the point in the ellipse located vertically above/below the centerOO. The length of thesemi–minoraxis is defined as the distanceb:=|F​L|​e21−e2.b:=|FL|\sqrt{\frac{e^{2}}{1-e^{2}}}.(4)

From the discussion above, it follows that the distance between the centerOOand either of the foci is given by|O​F|=||F​L|−|F​L|1−e2|=e2​|F​L||1−e2|​=⏟By(3)​e​a.|OF|=\left|\,|FL|-\frac{|FL|}{1-e^{2}}\right|=\frac{e^{2}|FL|}{\left|1-e^{2}\right|}\underbrace{=}_{\text{By }\eqref{eq:SemiMajor}}ea.(5)

From the final equality above, we can also write the distance between the focus and the directrix in terms of the length of the semi–major axis and the eccentricity as|F​L|=ae​|1−e2|.|FL|=\frac{a}{e}|1-e^{2}|.

Finally, solving for|F​L||FL|in (3) and substituting the result in (4) yieldsb=a​|1−e2|e​e21−e2=a​1−e2.b=\frac{a|1-e^{2}|}{e}\,\sqrt{\frac{e^{2}}{1-e^{2}}}=a\sqrt{1-e^{2}}.(6)Figure 1:Left: Conical sections for different values of the eccentricityee. Shades of red represent values of0<e<10<e<1resulting in ellipses; the color fades towards one. Shades of blue represent values ofe>1e>1resulting in hyperbolae with the color fading towards one. The parabola, plotted in violet, is the limiting casee=1e=1. The directrixLLis plotted as a dashed line, the focusFFis marked by an open circle. Right: Relevant geometric markers for ellipses and hyperbolae.

The circle.The reader must have noticed that the circle is missing from the definition above. We will now see that it can be understood as a special case of an ellipse with eccentricitye=0e=0. However, if we simply lete=0e=0in Definition1, we would only recover the degenerate case of a single point: the focus. Any attempt at using Equation (1) to obtain the circle as a limiting case of the Apollonian definition will face the same shortcoming. Hence, to include the circle as a limiting case, we will have to make the additional assumption that the length of the semi–major axis,aa, is a fixed predetermined parameter independent from the eccentricity.

We will first show that the Apollonian definition implies the well–known characterization of ellipses in terms of the constant sum of distances from the foci. With that in mind, we go back to the elliptic case and observe that the existence of the second (vertical) axis of symmetry atxOx_{O}implies:
- 1.

The existence of a second focus located along the major axis of symmetry with horizontal coordinate given by|L​F2|=xO+a​e|LF_{2}|=x_{O}+aeso that the two foci are located at the pointsF1=(xO−e​a,0)andF2=(xO+e​a,0).F_{1}=(x_{O}-ea,0)\qquad\text{ and }\qquad F_{2}=(x_{O}+ea,0).
- 2.

That, for every point on the ellipse, there is a second point in the ellipse sharing the sameyycoordinate and symmetrically located horizontally with respect toxOx_{O}. Namely, ifP1=(x,y)∈𝒞thenP2=(x+2​(xO−x),y)=(2​xO−x,y)∈𝒞.P_{1}=(x,y)\in\mathcal{C}\qquad\text{ then }\qquad P_{2}=\left(x+2(x_{O}-x),y\right)=(2x_{O}-x,y)\in\mathcal{C}.

From the two points above it follows that|P1​F2|=|x−(xO+e​a)|=|xO+e​a−x|=|(2​xO−x)−(xO−e​a)|=|P2​F1|,|P_{1}F_{2}|=|x-(x_{O}+ea)|=|x_{O}+ea-x|=|(2x_{O}-x)-(x_{O}-ea)|=|P_{2}F_{1}|,

and therefore|P1​F2|+|P1​F1|=|P2​F1|+|P1​F1|=e​(|P2​L|+|P1​L|)⏟From the definition1=e​((2​xO−x)+x)=2​e​|F​L|1−e2=2​a.|P_{1}F_{2}|+|P_{1}F_{1}|=\underbrace{|P_{2}F_{1}|+|P_{1}F_{1}|=e(|P_{2}L|+|P_{1}L|)}_{\text{\scriptsize From the definition }\ref{def:Conic}}=e\left((2x_{O}-x)+x\right)=\frac{2e|FL|}{1-e^{2}}=2a.

Summarizing, if a pointPPbelongs to the ellipse𝒞\mathcal{C}, it satisfies the constant sum of distances property|P1​F2|+|P1​F1|=2​a.|P_{1}F_{2}|+|P_{1}F_{1}|=2a.(7)

On the other hand, the distance between the foci is given by|F1​F2|=2​a​e|F_{1}F_{2}|=2ae, while the distance between the foci and the center is|F1​O|=|F2​O|=a​e|F_{1}O|=|F_{2}O|=ae. Therefore, ife=0e=0it follows thatF1=F2=OF_{1}=F_{2}=O, and therefore the constant sum of distances property implies that|P​O|=a.|PO|=a.

This is, of course, the definition of a circle with radiusaa, which shows that the circle can be considered as the limiting case of ellipses with vanishing eccentricity.

Focal equation of a conic.Placing a reference frame at the focusFFwith the horizontal axis parallel to the line segmentF​LFL, it is possible to describe the position of a pointPPin terms of its distance,rr, from the focus and the angle,θ\theta, that the vector connectingFFtoPPmakes with the horizontal axis. For historical reasons, within the context of celestial mechanics, the angleθ\thetais known as thetrue anomaly.

As depicted in Figure2, using this focus–centered polar coordinate frame, the condition from Definition1can be expressed asr=e​|L​P|=e​(|F​L|−r​cos⁡θ).r=e|LP|=e\left(|FL|-r\cos\theta\right).

If we solve forrrin the expression above, we obtainr=e​|F​L|1+e​cos⁡θr=\frac{e|FL|}{1+e\cos\theta}(8a)which expresses the relationship between the radial distancerrand the polar angleθ\thetain terms of the Apollonian parameters|F​L||FL|andee(recall that the Apollonian definition of conics uses only the directrixLL, the focusFFand the eccentricity). The expression above, known as thefocal equation of a conicArnold1978, does not include the circle: lettinge=0e=0above collapses the conic into a point at the focus. This should not come as a surprise, since the Apollonian definition used to derive this expression does not include the circle.

However, just as we did before, if we assume that the semi–major axisaais an additional parameter independent ofee, we can use (3) to eliminate|F​L||FL|from the expression above and obtainr=a​|1−e2|1+e​cos⁡θ.r=\frac{a|1-e^{2}|}{1+e\cos\theta}.(8b)

In this formulation, lettinge=0e=0results in the equation of a circle of radiusaa. However, the expression above does not include the parabolic case, as fore=1e=1the expression collapses into a point. This was to be expected, as the semi–major axis is not defined for parabolas. Since we will focus on the elliptic and circular cases later on, we will prefer this last expression for the conics.

## Remark 1(On the sign ofeein the focal equation)

Our derivation of equations (8) used the geometric construction from Figure2, where the origin of the coordinate system is located at therightfocus of the ellipse: the one labeled asF1F_{1}in the top right panel of Figure1, and the directrix is the linex=|F​L|x=|FL|. However, it is possible and equally valid to place the frame of reference at theleftfocus (labeledF2F_{2}in Figure1) so that the directrix is the linex=−|F​L|x=-|FL|. In that case, if the angle is still measured from the positive horizontal axis, the equations derived by the same procedure will be analogous to (8) with the only difference being that the eccentricity in the denominator will appear with the opposite sign. Hence, depending on the references, the denominator of (8) can be equal to1+e​cos⁡θ1+e\cos\theta, as in our case, or to1−e​cos⁡θ1-e\cos\theta. Some references go as far as writing the denominator as1±e​cos⁡θ1\pm e\cos\theta. The reader should be aware of this possible discrepancy and how to resolve it.Figure 2:Polar description of a pointPPin terms of the semi–major axisaaand eccentricityee.

## 2.2Elementary concepts from mechanics

The following elements from theoretical mechanics can be found in any standard reference, such asMorin2012;Scheck2010;ThMa2014. For the benefit of the reader with no previous familiarity with physics, we collect here just the concepts that will be absolutely essential for our exposition.

Governing laws.We are ultimately interested in describing the motion of a point particle (i.e. one that can be idealized as occupying no volume) with massmmunder the action of a gravitational force𝑭\bm{F}produced by an attracting body of massMM. We will refer to the body with massMMas theattractive centerand will also consider it to be a point. We will place a reference frame at the location of the attracting center and will determine the position of the particle of massmmby the vector𝒓\bm{r}, anchored at the origin, connecting the two particles. We will denote the magnitude of the position vector byr:=|𝒓|r:=|\bm{r}|. As is customary in mechanics and dynamical systems, we will use a dot to represent time differentiation, and will denote the velocity of the particle by𝒓˙\dot{\bm{r}}. Under these circumstances, the mathematical description of the motion of the particle will be determined bym​𝒓¨=\displaystyle m\ddot{\bm{r}}=\,𝑭\displaystyle\bm{F}(Newton’s second law of motion),\displaystyle\text{(Newton's second law of motion)},𝑭=\displaystyle\bm{F}=\,−G​M​mr3​𝒓\displaystyle-\frac{GMm}{r^{3}}\bm{r}\qquad\qquad(Newton’s universal law of gravitation).\displaystyle\text{(Newton's universal law of gravitation)}.

Above, the quantityGGis a numerical constant known as thegravitational constantand the minus sign appearing in the second equation indicates that the gravitational force is attractive. Given that𝑭\bm{F}depends only on the position𝒓\bm{r}of the particle relative to the attractive center, it is referred to as acentral force. Moreover, the reader will find it easy to verify that the force can be expressed as the gradient of a scalar function in the form:𝑭​(𝒓)=−∇U​(r),whereU​(r):=−G​M​mr.\bm{F}(\bm{r})=-\nabla U(r),\qquad\text{ where }\qquad U(r):=-\frac{GMm}{r}.(9)

The scalar functionUUis referred to aspotential energy, and forces that can be expressed as the gradient of a scalar quantity are said to beconservative. From the two laws of motion above, we see that a particle under the influence of a gravitational force will be then constrained to satisfy the second order differential equation𝒓¨=−G​Mr3​𝒓.\ddot{\bm{r}}=-\frac{GM}{r^{3}}\bm{r}.(10)

A priori, the expression above is a system of three second order differential equations (one for each component of the position vector𝒓\bm{r}) that, given the appropriate initial conditions, completely determines the movement of a particle under the influence of the attractive center. Rather than setting out to integrate these equations, in what follows we will exploit the physical properties of the system to reduce it first into a two dimensional second order vector problem, and then into a first order scalar problem.

Conservation of angular momentum.For a point particle with massmm, the vector quantity𝑳:=𝒓×m​˙​𝒓\bm{L}:=\bm{r}\times m\bm{\dot{}}{\bm{r}}\,

is known as theangular momentum. The symbol “×\times” above denotes the standard vector or cross product satisfying for all𝒖,𝒗∈ℝ3\bm{u},\bm{v}\in\mathbb{R}^{3}:𝒖×𝒗=|𝒖|​|𝒗|​sin⁡ϕ​𝒏,\bm{u}\times\bm{v}=|\bm{u}||\bm{v}|\sin\phi\,\bm{n},(11)

whereϕ\phiis the angle between𝒖\bm{u}and𝒗\bm{v}, and𝒏\bm{n}is the unitary vector normal to the plane determined by𝒖\bm{u}and𝒗\bm{v}in the positive direction.

From its definition, the angular momentum is perpendicular to both the particle’s position and velocity and, at any given time it determines the instantaneous plane of motion of a particle. We will now compute the rate of change of the angular momentum for a particle under the action of a gravitational force:𝑳˙=dd​t​(𝒓×m​𝒓˙)=𝒓˙×m​𝒓˙+𝒓×m​𝒓¨​=⏟By (10)​𝒓˙×m​𝒓˙+𝒓×(−G​M​mr3​𝒓)=𝟎,\dot{\bm{L}}=\frac{d}{dt}\left(\bm{r}\times m\dot{\bm{r}}\right)=\dot{\bm{r}}\times m\dot{\bm{r}}+\bm{r}\times m\ddot{\bm{r}}\underbrace{=}_{\text{\scriptsize By \eqref{eq:SecondOrderEquation}}}\dot{\bm{r}}\times m\dot{\bm{r}}+\bm{r}\times\left(-\frac{GMm}{r^{3}}\bm{r}\right)=\bm{0},

where we used the fact that the cross product vanishes when its arguments are multiples of each other. The result above is known as theconservation of angular momentumand has long reaching consequences. The first one is that, due to𝑳\bm{L}being normal to the plane of motion,under the action of a gravitational potential, the motion of a particle is constrained to the fixed plane determined by its initial position and velocity.This fact has the effect of reducing the dimensionality of the problem from three to two dimensions, allowing us to use a polar coordinate system.

Position, velocity, and acceleration in polar coordinatesIn view of the first geometric consequence of the conservation of angular momentum, we will assume that the plane of motion coincides with the Euclideanx​yxyplane and will express the position vector𝒓\bm{r}in polar coordinates in terms of its magnituder:=|𝒓|r:=|\bm{r}|and the angleθ\thetathat it makes with respect to the positivexx–axis.

The polar basis vectors𝒓^\widehat{\bm{r}}and𝜽^\widehat{\bm{\theta}}are defined as the unit vectors pointing in the directions of purely radial,(1+Δ​r)​𝒓(1+\Delta r)\bm{r}, and purely angular,θ+Δ​θ\theta+\Delta\theta, increment respectively. We can obtain an explicit expression for𝒓^\widehat{\bm{r}}by expressing𝒓=(r​cos⁡θ,r​sin⁡θ)\bm{r}=(r\cos\theta,r\sin\theta)and inferring from the definition that𝒓^=(1+Δ​r)​𝒓|(1+Δ​r)​𝒓|=(r​cos⁡θ,r​sin⁡θ)r=(cos⁡θ,sin⁡θ).\widehat{\bm{r}}=\frac{(1+\Delta r)\bm{r}}{|(1+\Delta r)\bm{r}|}=\frac{\left(r\cos\theta,r\sin\theta\right)}{r}=\left(\cos\theta,\sin\theta\right).

From the expression above we can obtain the one for𝜽^\widehat{\bm{\theta}}by noting that, as depicted in the left panel of Figure3, the direction of angular growth is perpendicular to the unit radial vector, and therefore𝜽^=(−sin⁡θ,cos⁡θ).\widehat{\bm{\theta}}=(-\sin\theta,\cos\theta).

A simple computation shows thatdd​t​𝒓^=θ˙​𝜽^anddd​t​𝜽^=−θ˙​𝒓^.\frac{d}{dt}\widehat{\bm{r}}=\dot{\theta}\widehat{\bm{\theta}}\qquad\text{ and }\qquad\frac{d}{dt}\widehat{\bm{\theta}}=-\dot{\theta}\widehat{\bm{r}}.(12)

Unlike their Cartesian counterparts, these unit vectors are not constant, as an angleθ\thetais needed in order to determine the basis. Hence, fixing the polar coordinate system at the angleθ\theta, and using the identities in (12), we can write the position, velocity and acceleration of a particle with Cartesian coordinates(r​cos⁡θ,r​sin⁡θ)(r\cos\theta,r\sin\theta)as𝒓=\displaystyle\bm{r}=\,r​𝒓^,\displaystyle r\,\widehat{\bm{r}},(13a)𝒓˙=\displaystyle\dot{\bm{r}}=\,r˙​𝒓^+r​θ˙​𝜽^,\displaystyle\dot{r}\,\widehat{\bm{r}}+r\,\dot{\theta}\,\widehat{\bm{\theta}},(13b)𝒓¨=\displaystyle\ddot{\bm{r}}=\,(r¨−r​θ˙2)​𝒓^+(2​r˙​θ˙+r​θ¨)​𝜽^.\displaystyle(\ddot{r}-r\dot{\theta}^{2})\widehat{\bm{r}}+(2\dot{r}\dot{\theta}+r\ddot{\theta})\widehat{\bm{\theta}}.(13c)

The quantitiesr˙\dot{r}andθ˙\dot{\theta}are known respectively as the radial and angular velocities and are depicted in the right panel of Figure3.Figure 3:Left: For a fixed angleθ\thetathe polar basis vectors are orthogonal and point in the direction of growth(1+Δ)​𝒓(1+\Delta)\bm{r}(in gray) andθ+Δ​θ\theta+\Delta\theta(in red). Right: The velocity of a particle,𝒓˙\dot{\bm{r}}, can be decomposed in radial and angular components.

Conservation of energy.The kinetic energy of a particle with massmmmoving with velocity𝒓˙\dot{\bm{r}}is defined asT:=12​m​|𝒓˙|2=12​m​(r˙2+r2​θ˙2)T:=\frac{1}{2}m|\dot{\bm{r}}|^{2}=\frac{1}{2}m(\dot{r}^{2}+r^{2}\dot{\theta}^{2})\,

where we used Equation (13b) and the fact that the vectors𝒓^\widehat{\bm{r}}and𝜽^\widehat{\bm{\theta}}are perpendicular. The first term above is due to the radial component of the velocity—and is therefore known as the radial kinetic energy—while the second one is due to the angular component—and is referred to as the rotational energy.

The sum of the kinetic energy and the gravitational potential energy introduced in equation (9), constitutes the total energy of the system. We will denote it asE:=T+U=12​m​(r˙2+r2​θ˙2)−G​M​mr.E:=T+U=\frac{1}{2}m(\dot{r}^{2}+r^{2}\dot{\theta}^{2})-\frac{GMm}{r}.

Under a gravitational potential we havedd​t​E=\displaystyle\frac{d}{dt}E=\,dd​t​(12​m​(r˙2+r2​θ˙2)−G​M​mr)\displaystyle\frac{d}{dt}\left(\frac{1}{2}m(\dot{r}^{2}+r^{2}\dot{\theta}^{2})-\frac{GMm}{r}\right)=\displaystyle=\,12​m​(2​r˙​r¨+2​r​r˙​θ˙2+2​r2​θ˙​θ¨)+G​M​mr2​r˙\displaystyle\frac{1}{2}m(2\dot{r}\ddot{r}+2r\dot{r}\dot{\theta}^{2}+2r^{2}\dot{\theta}\ddot{\theta})+\frac{GMm}{r^{2}}\dot{r}=\displaystyle=\,m​(r˙​r¨+r​r˙​θ˙2+r2​θ˙​θ¨)+G​M​mr2​r˙.\displaystyle m(\dot{r}\ddot{r}+r\dot{r}\dot{\theta}^{2}+r^{2}\dot{\theta}\ddot{\theta})+\frac{GMm}{r^{2}}\dot{r}.(14)

Using the polar expressions of the position, velocity, and acceleration (13) and the fact that𝒓^⋅𝜽^=0\widehat{\bm{r}}\cdot\widehat{\bm{\theta}}=0, it is easy to verify thatm​𝒓˙⋅𝒓¨=m​(r˙​r¨+r​r˙​θ˙2+r2​θ˙​θ¨),m\dot{\bm{r}}\cdot\ddot{\bm{r}}=m(\dot{r}\ddot{r}+r\dot{r}\dot{\theta}^{2}+r^{2}\dot{\theta}\ddot{\theta}),

while from the second order equation of motion (10) and (13) we see thatm​𝒓˙⋅𝒓¨=−G​M​mr3​𝒓⋅𝒓˙=−G​M​mr2​r˙.m\dot{\bm{r}}\cdot\ddot{\bm{r}}=-\frac{GMm}{r^{3}}\bm{r}\cdot\dot{\bm{r}}=-\frac{GMm}{r^{2}}\dot{r}.

Substituting the last two results into (14) proves that, under a gravitational potential, the energyEEis constant over time.

Remark.The standard way of proving conservation of energy is to start from the kinetic term and computedd​t​(12​m​|𝒓˙|2)=m​𝒓˙⋅𝒓¨​=⏟By (10)−G​M​m|𝒓|3​𝒓⋅𝒓˙=dd​t​(G​M​m|𝒓|),\frac{d}{dt}\left(\frac{1}{2}m|\dot{\bm{r}}|^{2}\right)=m\dot{\bm{r}}\cdot\ddot{\bm{r}}\underbrace{=}_{\text{\scriptsize By \eqref{eq:SecondOrderEquation}}}-\frac{GMm}{|\bm{r}|^{3}}\bm{r}\cdot\dot{\bm{r}}=\frac{d}{dt}\left(\frac{GMm}{|\bm{r}|}\right),

from which it follows thatdd​t​(12​m​|𝒓˙|2−G​M​m|𝒓|)=dd​t​(T+U)=dd​t​E=0.\frac{d}{dt}\left(\frac{1}{2}m|\dot{\bm{r}}|^{2}-\frac{GMm}{|\bm{r}|}\right)=\frac{d}{dt}\left(T+U\right)=\frac{d}{dt}E=0.

## 3Motion under a gravitational potential

## 3.1Equations of motion

As we mentioned before, the motion of a particle under a gravitational attractive force is completely determined by the solution to the second order vector equation (10). However, conservation of momentum and energy provide the means to reduce the problem into a system of first order scalar equations, as we now demonstrate.

We start with angular momentum. Using the polar expressions for the position (13a) and velocity (13b), we can express the angular momentum as𝑳:=𝒓×m​𝒓˙=r​𝒓^×m​(r˙​𝒓^+r​θ˙​𝜽^)=m​r2​θ˙​𝒓^×𝜽^.\bm{L}:=\bm{r}\times m\dot{\bm{r}}=r\,\widehat{\bm{r}}\times m\left(\dot{r}\,\widehat{\bm{r}}+r\,\dot{\theta}\,\widehat{\bm{\theta}}\right)=mr^{2}\dot{\theta}\,\widehat{\bm{r}}\times\widehat{\bm{\theta}}.

This, together with (11) and the conservation property imply that, under a gravitational force, the magnitudeL:=|𝑳|=m​r2​θ˙L:=|\bm{L}|=mr^{2}\dot{\theta}(15)

remains constant over time. Analogously, the conservation of energy implies that the quantityE=12​m​(r˙2+r2​θ˙2)−G​M​mr.E=\frac{1}{2}m(\dot{r}^{2}+r^{2}\dot{\theta}^{2})-\frac{GMm}{r}.(16)

is constant. These two equations involve only first derivatives of the radial and angular coordinates and for that reason are sometimes referred to asfirst integrals of motion. Solving forr˙\dot{r}andθ˙\dot{\theta}in the expressions above yields the first order nonlinear system of differential equations:θ˙=\displaystyle\dot{\theta}=\,Lm​r2,\displaystyle\frac{L}{mr^{2}}\,,(17a)r˙=\displaystyle\dot{r}=\,2m​(E+G​M​mr)−(Lm​r)2.\displaystyle\sqrt{\frac{2}{m}\left(E+\frac{GMm}{r}\right)-\left(\frac{L}{mr}\right)^{2}}\,.(17b)

If initial conditionsr​(0)r(0)andθ​(0)\theta(0)are given, it is possible to integrate the system (17) to obtain the time dependence for the radial and angular parametersrrandθ\thetaof the particle for all times. We will refer to the set of points(r​(t),θ​(t))(r(t),\theta(t))that can be described by the solutions of the system (17) asorbitsortrajectories. Alternatively, the desired initial and final positions (instead of initial position and velocity) may be prescribed. In that case, determining the orbits(r​(t),θ​(t))(r(t),\theta(t))becomes something that is known as aboundary value problemin the mathematical literature. Boundary value problems require slightly different mathematical techniques than initial value problems and, even when they are solvable, often call for additional physical constraints to avoid having multiple solutions. As we will see in Section4, Lambert’s problem falls into the latter category. However, before switching our attention to it, we will spend some time studying the properties of the orbits available to objects under a gravitational potential. We will then use this geometric information to avoid having to deal with differential equations when tackling Lambert’s boundary value problem.

## 3.2Gravitational orbits

In general, under the influence of a gravitational potential the polar parametersrrandθ\thetaare not independent of each other, as their time behavior is constrained to obey the system of equations (17). Since equation (17a) couples the time evolution ofrrandθ\thetaknowledge about one of the variables will implicitly determine the other one.

The exception to this, however, is the case whenL=0L=0, as in that case (17a) is independent ofrr—note that equation (17b) depends exclusively onrr. We will study this case first. If the angular velocityθ˙\dot{\theta}vanishes at any given time, then the angular momentum would vanish as well. Therefore, by the conservation property encoded in equation (17a), this would imply thatθ˙=0\dot{\theta}=0for all times and the particle would describe a straight line at a constant angleθ0=θ​(0)\theta_{0}=\theta(0).

On the other hand, if the angular speedθ˙\dot{\theta}is not zero initially, then the conservation of angular momentum implies that it will never vanish—as the left hand side of (17a) would then be a positive constant. In that caserrandθ\thetaare functionally dependent on each other and we can assume an implicit relationship of the formr=r​(θ​(t))r=r(\theta(t)). Using the chain rule we obtain:r˙=d​rd​θ​θ˙.\dot{r}=\frac{dr}{d\theta}\dot{\theta}.

Sinceθ˙≠0\dot{\theta}\neq 0for all times, we can solve the equation above ford​r/d​θ=r˙/θ˙dr/d\theta=\dot{r}/\dot{\theta}and use the equations of motion (17) to obtain1r2​d​rd​θ=2​mL2​(E+G​M​mr)−1r2.\frac{1}{r^{2}}\frac{dr}{d\theta}=\sqrt{\frac{2m}{L^{2}}\left(E+\frac{GMm}{r}\right)-\frac{1}{r^{2}}}.

The reason why we kept the factor1/r21/r^{2}on the left hand side of the equality, is that it highlights the fact that the expression above depends onrronly through the functionu=1r.u=\frac{1}{r}.

Performing this change of variables in the equation above yields−d​ud​θ=2​mL2​(E+G​M​m​u)−u2.-\frac{du}{d\theta}=\sqrt{\frac{2m}{L^{2}}\left(E+GMmu\right)-u^{2}}.(18)

The radical in the right hand side is suggestive of a trigonometric substitution, but such a substitution requires the variableuuto appear solely as part of a “perfect square”. We therefore complete the square inside of the square root to obtaind​ud​θ=−2​mL2​(E+G​M​m​u)−u2=−2​m​EL2+(G​M​m2L2)2−(u−G​M​m2L2)2.\frac{du}{d\theta}=-\sqrt{\frac{2m}{L^{2}}\left(E+GMmu\right)-u^{2}}=-\sqrt{\frac{2mE}{L^{2}}+\left(\frac{GMm^{2}}{L^{2}}\right)^{2}-\left(u-\frac{GMm^{2}}{L^{2}}\right)^{2}}.

Finally, definingK:=2​m​EL2+(G​M​m2L2)2andy:=u−G​M​m2L2,K:=\sqrt{\frac{2mE}{L^{2}}+\left(\frac{GMm^{2}}{L^{2}}\right)^{2}}\qquad\text{ and }\qquad y:=u-\frac{GMm^{2}}{L^{2}},

and realizing thatd​ud​θ=d​yd​θ{\displaystyle\frac{du}{d\theta}=\frac{dy}{d\theta}}, the equation (18) results ind​yd​θ=−K2−y2.\frac{dy}{d\theta}=-\sqrt{K^{2}-y^{2}}.

This equation can be readily integrated by separation of variables yieldingcos−1⁡(yK)=θ−θ0.\cos^{-1}\left(\frac{y}{K}\right)=\theta-\theta_{0}.

It is customary to choose the integration constantθ0\theta_{0}so that at initial time the particle is located at the point nearest to the focus—known as theperihelionorperiapsis. Choosing this angle to beθ0=0\theta_{0}=0fixes an orientation of the system similar to the one depicted in Figure4, where the axis of symmetry is horizontal and, if there are indeed two foci, the attractive center is located at the one on the right. This is the most common choice in the literature. Following this convention the equation above implies thaty=K​cos⁡θ.y=K\cos\theta.

Substituting backKKandyy, and solving foruuwe obtainu=G​M​m2L2+cos⁡θ​2​m​EL2+(G​M​m2L2)2=G​M​m2L2​(1+cos⁡θ​2​E​L2(G​M​m)2​m+1).u=\frac{GMm^{2}}{L^{2}}+\cos\theta\sqrt{\frac{2mE}{L^{2}}+\left(\frac{GMm^{2}}{L^{2}}\right)^{2}}=\frac{GMm^{2}}{L^{2}}\left(1+\,\,\cos\theta\sqrt{\frac{2EL^{2}}{(GMm)^{2}m}+1}\right).

Finally, recalling thatu=1/ru=1/r, the expression above yieldsr=p1+e​cos⁡θ,r=\frac{p}{1+e\cos\theta},(19a)wherep:=L2G​M​m2ande:=1+2​E​L2(G​M​m)2​m.p:=\frac{L^{2}}{GMm^{2}}\qquad\text{ and }\qquad e:=\sqrt{1+\frac{2EL^{2}}{(GMm)^{2}m}}\;\;.(19b)

Equation (19a) describes all the possible trajectories for particleswith non–zero angular momentummoving under a gravitational potential111We discussed the case of zero angular momentum at the beginning of this section, which results in straight lines connecting the initial position of the particle with the attractive center.. The attentive reader will note that (19a) is exactly of the form (8) that we arrived at when studying conic sections. This allows us to state the following remarkable fact:The only possible trajectories for a particle under a central gravitational potential are conic sections.From a purely geometric point of view, the particular conic is determined by the eccentricity. Equation (19b) connects the geometry of the problem to the physical parameters by quantifying the way in which the eccentricityeedepends on the particle’s energyEEand angular momentumLL. Concretely, expressingppin terms of the angular momentum and equating (19a) with (8b), we can connect the geometric parameterseeandaawith the physical parameters, resulting inL2=a​|1−e2|​G​M​m2.L^{2}=a\left|1-e^{2}\right|GMm^{2}.(20)

We will now discuss the particular orbits and their connection with these physical parameters:

- ∙\bullet

𝑳=𝟎.Straight lines.\boxed{\bm{L=0\,.}\text{{ Straight lines.}}}If the angular momentum is zero, then (17a) implies that the angle remains constant and the particle’s orbit is a straight line.
- ∙\bullet

𝑳≠𝟎.\boxed{\bm{L\neq 0\,.}}If the angular momentum is different from zero, then the orbit’s eccentricityeeis determined by the particle’s initial energyE=12​m​(r˙02+r02​θ˙02)⏟Kinetic​−G​M​mr0⏟Potential,E=\underbrace{\frac{1}{2}m(\dot{r}_{0}^{2}+r_{0}^{2}\dot{\theta}_{0}^{2})}_{\text{\small Kinetic}}\,\,\underbrace{-\,\,\frac{GMm}{r_{0}}}_{\text{\scriptsize Potential}},

wherer0,θ0,r˙0r_{0},\theta_{0},\dot{r}_{0}andθ˙0\dot{\theta}_{0}denote respectively the initial radial and angular positions and velocities. The energy can be negative, zero or positive, which leads to three possible geometric scenarios:

- (a)

E<0.Closed orbits.\boxed{E<0\,.\,\text{{Closed orbits}}.}When the attractive potential is larger than the particle’s kinetic energy, the total energy of the system will be negative. In this case the particle won’t have enough energy to escape the attractive potential and will remain “trapped” in the sense that its distancerrto the attractive potential will be bounded for all times.

Going back to the equation (19b) for the eccentricity, we note that the only term inside the radical that is not necessarily positive is the total energyEE. Since the eccentricity must be a real number, the admissible values for the energy are limited by the condition1+2​E​L2(G​M​m)2​m≥0.1+\frac{2EL^{2}}{(GMm)^{2}m}\geq 0.

Thus, the admissible negative values for the energy lie in the range−(G​M​m)2​m2​L2≤E<0.-\frac{(GMm)^{2}m}{2L^{2}}\leq E<0.

We distinguish two cases:

- (i)

e=0.Circular orbits.\boxed{e=0\,.\,\text{{Circular orbits}}.}When substituted into Equation (19b), the minimum admissible energyE=−(G​M​m)2​m2​L2,E=-\frac{(GMm)^{2}m}{2L^{2}},

yields and eccentricitye=0e=0, which corresponds to a circular orbit. To determine the radius of the circle, we lete=0e=0in Equation (19a) and conclude that the distance between the particle and the attractive center (i.e. the radius of the orbit) isr=L2G​M​m2.r=\frac{L^{2}}{GMm^{2}}.
- (ii)

0<e<1.Elliptic orbits.\boxed{0<e<1\,.\,\text{{Elliptic orbits}}.}For values of the energy in the interval−(G​M​m)2​m2​L2<E<0-\frac{(GMm)^{2}m}{2L^{2}}<E<0

the eccentricity of the orbit remains strictly inside the interval(0,1)(0,1), which corresponds to an ellipse. The minimum and maximum distances prescribed by (19a) arermax=L2G​M​m2​(1−e)andrmin=L2G​M​m2​(1+e).r_{\text{max}}=\frac{L^{2}}{GMm^{2}(1-e)}\qquad\text{ and }\qquad r_{\text{min}}=\frac{L^{2}}{GMm^{2}(1+e)}.

From these, we can express the semi–major axis of the ellipse in terms of physical parameters asa=12​(rmax+rmin)=L2G​M​m2​(1−e2).a=\tfrac{1}{2}(r_{\text{max}}+r_{\text{min}})=\frac{L^{2}}{GMm^{2}(1-e^{2})}.(21)

The expressions for the radius of circular orbits and the semi–major axis of elliptic orbits that we just derived, confirm that a particle with no angular momentum necessarily collapses into the attractive center. They also reveal that, for a fixed initial angular momentum, more massive bodies (i.e. those for which the productM​m2Mm^{2}is larger) are bound to remain closer to the attractive center.
- (b)

E≥0.Open orbits.\boxed{E\geq 0\,.\,\text{{Open orbits}}.}When the particle’s kinetic energy is enough to exactly counteract the attractive potential or exceeds it, the particle will be able to “escape” the attraction in the sense that its distance to the attractive center will eventually grow unbounded. We infer this from the fact thate−1<1e^{-1}<1and therefore, form (19a), we have thatrmax=limθ→±cos−1⁡(−e−1)p1+e​cos⁡θ=∞.r_{\text{max}}=\lim_{\theta\to\pm\cos^{-1}(-e^{-1})}\frac{p}{1+e\cos\theta}=\infty.

The anglesθ±∞:=±cos−1⁡(−e−1)\theta_{\pm\infty}:=\pm\cos^{-1}(-e^{-1})appearing in the limit above determine oblique asymptotic lines that the particle cannot cross. As the particle drifts away, the conservation condition dictates thatE=limr→∞(12​m​(r˙2+r2​θ˙2)−G​M​mr)=limr→∞(12​m​(r˙2+r2​θ˙2))<∞.E=\lim_{r\to\infty}\left(\frac{1}{2}m(\dot{r}^{2}+r^{2}\dot{\theta}^{2})-\frac{GMm}{r}\right)=\lim_{r\to\infty}\left(\frac{1}{2}m(\dot{r}^{2}+r^{2}\dot{\theta}^{2})\right)<\infty.(22)

For this to hold, we must have thatlimr→∞θ˙=0andlimr→∞r˙=r˙∞<∞.\lim_{r\to\infty}\dot{\theta}=0\qquad\text{ and }\qquad\lim_{r\to\infty}\dot{r}=\dot{r}_{\infty}<\infty.

In fact, the condition on the angular velocity is even stronger, requiringlim1/r→0θ˙(1/r)=0.{\displaystyle\lim_{1/r\to 0}\frac{\dot{\theta}}{(1/r)}=0}.

Hence, as a particle drifts away to infinity, its angular velocity decays rapidly and indeed vanishes before the angular coordinate of the particle can reach the anglesθ±∞\theta_{\pm\infty}. Particles in this situation will describe open trajectories. We distinguish between two cases:

- (iii)

e=1.Parabolic orbits.\boxed{e=1\,.\,\text{{Parabolic orbits.}}}If the potential term equals the kinetic term, the total energy will beE=0E=0. Equation (19b) implies thate=1e=1and the particle follows a parabolic orbit. Comparing (19a) and (8a) it follows that the distance between the directrix of the parabola and the attractive center isrmin=|F​L|=p=L2G​M​m2,r_{\text{min}}=|FL|=p=\frac{L^{2}}{GMm^{2}},

while, as the angleθ\thetaapproachesπ\pior−π-\pi, equation (19a) implies thatr→∞.r\to\infty.We note that asr→∞r\to\inftythe potential energy vanishes. The limit condition (22) and the fact thatE=0E=0imply that the residual speed at infinity for a particle on a parabolic trajectory isr˙∞=0\dot{r}_{\infty}=0.
- (iv)

e>1.Hyperbolic orbits.\boxed{e>1\,.\,\text{{Hyperbolic orbits.}}}Finally, when the kinetic energy exceeds the potential energy the eccentricity of the trajectory will be greater than one, and the particle will follow a hyperbolic arc. In this case the minimum distance to the attractive center will be given byrmin=L2G​M​m2​(1+e).r_{\text{min}}=\frac{L^{2}}{GMm^{2}(1+e)}.

The excess in kinetic energy allows these particles to “reach infinity” with a non–zero radial velocity given byr˙∞=2​E/m\dot{r}_{\infty}=\sqrt{2E/m}.

In the elliptic and hyperbolic cases, the numerators from (8b) and (19a) can be equated, and the form ofeein (19b) can be used to obtain the expression for the semi–major axisaain terms of the physical parametersa=G​M​m2​|E|,a=\frac{GMm}{2|E|},(23)

which in the limiting caseE→0E\to 0is consistent with the fact that the length of the axis of symmetry of a parabola is infinite.

## 3.3Kepler’s laws of planetary motion

In their modern version, Kepler’s laws are usually stated as slight variations of the followingMorin2012;Scheck2010:
- 1.

The planets move in elliptical orbits with the Sun at one focus.
- 2.

The radius vector from the Sun to the planets sweeps out equal areas in
equal times.
- 3.

The square of the period of an orbit,𝒯\mathcal{T}, is proportional to the cube of the
semi–major axis length,aa. More precisely,𝒯2=4​π2​a3G​M,\mathcal{T}^{2}=\frac{4\pi^{2}a^{3}}{GM},

whereMMis the mass of the Sun.

We will now use the analytical tools developed in the previous section to prove Kepler’s statements.

First law.The planets move in elliptical orbits with the Sun at one focus.

The modern–day proof of this claim is, of course, the detailed analytic process leading to equation (19a), combined with the empirical observation that the distance between the planets and the Sun is bounded (which discards hyperbolas, parabolas and straight lines). It is important to remark that, in full rigor, this statement is only true for the interaction between the Sun anda singleplanet.

Second law.The radius vector from the Sun to the planets sweeps out equal areas in equal times.

This fact is a consequence of the conservation of angular momentum, as we now show. Consider a particle with position vector𝒓\bm{r}traveling along an elliptical trajectory. After experiencing an infinitesimal displacement𝒅​𝒓\bm{dr}, its position vector will sweep an infinitesimal elliptic sector as depicted in Figure4. From elementary vector algebra, the aread​AdAof the infinitesimal sector will be given byd​A=12​|𝒓×𝒅​𝒓|.dA=\tfrac{1}{2}|\bm{r\times dr}|.

A computation completely analogous to the one leading to Equation (13b), shows that𝒅​𝒓=d​r​𝒓^+r​d​θ​𝜽^.\bm{dr}=dr\,\widehat{\bm{r}}+rd\theta\,\widehat{\bm{\theta}}.

Using this and recalling that the unit vectors𝒓^\widehat{\bm{r}}and𝜽^\widehat{\bm{\theta}}are orthogonal we obtaind​A=12​|r​𝒓^×(d​r​𝒓^+r​d​θ​𝜽^)|=12​|r​𝒓^×r​d​θ​𝜽^|=12​r2​d​θ.dA=\tfrac{1}{2}|r\,\widehat{\bm{r}}\times(dr\,\widehat{\bm{r}}+rd\theta\,\widehat{\bm{\theta}})|=\tfrac{1}{2}|r\,\widehat{\bm{r}}\times rd\theta\,\widehat{\bm{\theta}}|=\tfrac{1}{2}r^{2}d\theta.

Hence, the area traversed by the particle between the timest0t_{0}andttis given byA=12​∫θ​(t0)θ​(t)r2​𝑑θ=12​∫t0tr2​θ˙​𝑑s​=⏟Conservation​12​∫t0tLm​𝑑s=L2​m​(t−t0),A=\;\tfrac{1}{2}\int_{\theta(t_{0})}^{\theta(t)}r^{2}d\theta\;=\;\tfrac{1}{2}\int_{t_{0}}^{t}r^{2}\dot{\theta}ds\underbrace{=}_{\text{\scriptsize Conservation}}\tfrac{1}{2}\int_{t_{0}}^{t}\tfrac{L}{m}\,ds\;=\;\tfrac{L}{2m}(t-t_{0}),(24)

where in the third equality we used the fact that|𝑳|=L=m​r2​θ˙|\bm{L}|=L=mr^{2}\dot{\theta}is constant with respect to time. Therefore, the area swept depends only on the length of the time interval elapsed, which is equivalent to Kepler’s statement.Figure 4:The area of the parallelogram determined by the vectors𝒓\bm{r}and𝒅​𝒓\bm{dr}(shaded) is given by the norm|𝒓×𝒅​𝒓||\bm{r\times dr}|. As the position vector𝒓\bm{r}undergoes a small displacement𝒅​𝒓\bm{dr}along the elliptic arc, the area of the infinitesimal elliptic sector it traverses (dark shade) is given by12​|𝒓×𝒅​𝒓|\tfrac{1}{2}|\bm{r\times dr}|. Right: The time required to travel between𝒓𝟏\bm{r_{1}}and𝒓𝟐\bm{r_{2}}is the same as that required to travel between𝒓𝟐\bm{r_{2}}and𝒓𝟒\bm{r_{4}}.

Third law.The square of the period of an orbit is proportional to the cube of the semi–major-axis length.

Setting the time spant−t0t-t_{0}equal to one period of revolution,𝒯\mathcal{T}, in (24) and recalling that the area of an ellipse is given byπ​a​b\pi ab(whereaaandbbare the lengths of the semi–major and semi–minor axes of the ellipse), we obtainπ​a​b=L​𝒯2​m.\pi ab=\frac{L\mathcal{T}}{2m}.(25)

We can then use the last equality in (5) to expressa=e​|F​L||1−e2|a=\frac{e|FL|}{|1-e^{2}|}and substitute this into (4) yieldingb=|F​L|​e2|1−e2|=a​|1−e2|.b=|FL|\sqrt{\frac{e^{2}}{|1-e^{2}|}}=a\sqrt{|1-e^{2}|}.

From here, we use (21) to express1−e2=Lm​1G​M​a\sqrt{1-e^{2}}=\frac{L}{m}\sqrt{\frac{1}{GMa}}and obtainb=Lm​aG​Mb=\frac{L}{m}\sqrt{\frac{a}{GM}}

which, upon substitution, turns the expression (25) intoπ​Lm​a3G​M=L​𝒯2​m.\frac{\pi L}{m}\sqrt{\frac{a^{3}}{GM}}=\frac{L\mathcal{T}}{2m}.

Finally, squaring both sides and solving for𝒯\mathcal{T}leads to𝒯2=4​π2​a3G​M,\mathcal{T}^{2}=\frac{4\pi^{2}a^{3}}{GM},(26)

as desired.

## 3.4Brief historical digression

Kepler’s celebrated laws were published between 1609 and 1619 and had a tremendous impact on the astronomical community of the early17t​h17^{th}century and beyond. They are the result of decades of careful measurements of the planets’s locations made by Tycho Brahe, and then of several more years of detailed mathematical analysis of the measurements (mostly of the orbit of Mars) by Kepler himselfWilson1972. They are a testament of Brahe’s meticulous measurements (all of them madewith the naked eyeTabak2011, as the telescope would not be around until 1609) as well as of Kepler’s mathematical and computational prowess and scientific integrity. Although by Kepler’s time the Heliocentric theory of the universe was starting to show serious cracks, the notion that planets followed circular orbits was still widely accepted as true. Kepler estimated the eccentricity of Mars’s orbit to bee≈0.0926e\approx 0.0926Xavier—which is not too far from that of a circle. Due to the coarseness of most contemporary measurements, Kepler could have easily attributed the discrepancy to measurement or computational error, however he trusted Brahe’s measurements and his own computations. Years of wrestling with the data had convinced him that the circle was not the correct answer and he pushed forward hisellipticdiscovery, even if it clearly went against the widely accepted theories.

As originally stated by Kepler, his laws were purely kinematic descriptions that did not offer an underlying theory explaining the origin of the movementHockey2014;Katz2008. Due to the lack of a guiding principle leading Kepler’s analysis of empirical data, it can be argued that his conclusions were the product of serendipity: Brahe’s measurements were precise enough to show a discrepancy from a circular orbit, but not precise enough to reveal the perturbations due to the gravitational fields of other planets, which would have led Kepler astrayStillwell2010. A complete dynamic explanation of planetary orbits would have to wait until Newton’s inverse square law, while the powerful and elegant analytical treatment that we have used above would require a further refinement of Newton’s calculus. The arguments and tools that we used in the previous section to obtain the equation of the orbits can be traced back to Euler and Lagrange in the mid to late18t​h.18^{th.}centuryStillwell2010.

What we now call Kepler’s first law appeared in 1609, in his bookAstronomia novaKepler1609, where he carefully describes the lengthy thought process that led him to the conclusion that Mars’s orbit is elliptic, and states that:“. . . the orbit of the planet is not a circle, but comes in gradually on both sides and
returns again to the circle’s distance at perigee. They are all accustomed to call the shape of this sort of path ‘oval’.”Kepler1609;Linton2004Kepler in fact derived an equation that is almost identical to the center–based equation for an ellipse, but using a different angular parameter that became known as theeccentric anomaly(depicted in Figure5, where it is denoted asϕ\phi)Linton2004. After exhaustively working with the data for Mars and concluding that the ellipse was the only possible explanation, Kepler barely verified the data for other planets before generalizing the conclusion based on the conviction that “the harmony of nature demanded that allhave similar habits”Burton2010. Regarding the location of the Sun at a focus of the ellipse, LintonLinton2004points out that: “nowhere in the main body of theNew Astronomyis the word ‘focus’ mentioned, and it was only later in hisEpitome of Copernican Astronomythat Kepler emphasized this aspect of planetary orbits”. TheEpitome of Copernican Astronomy, originally entitled “Epitome Astronomiae Copernicanae”Kepler1995was intended to be a textbook in astronomy and was published in seven parts between 1618 and 1621Caspar2012;Rothman2020.

As for the second law, Kepler derived it as an approximation, in an attempt to find a proxy for the time elapsed while a planet describes an arc. His derivation uses an argument that can be considered incipient integral calculus: as described by KatzKatz2008, “Kepler then argued that the total time required to pass over a finite arc […] could be thought of as the sum of the radius vectors making up that part of the circle, or as the area swept by the radius vector”. Kepler was no stranger to “infinitesimal” arguments of that sort, which come remarkably close to integration. During his career he would use similar reasoning to approximate the area of a circle by considering the sum of infinitely many triangles with vertex on the center of the circle and sides along the circumference, as well as to calculate the surface area of a sphere by a similar argument involving infinitesimal conesBurton2010. He famously went on to extend these techniques to calculating the volume of different solids of revolution and wine barrelsKepler2018.

Going back to theequal areaslaw, Kepler discovered it sometime before 1605 and used it extensively in the calculations that would eventually lead to the first law, as he himself describes in his 1609New Astronomy. However, his thoughts on this rule evolved over time and he eventually concluded that it was not an approximation, but a true statement. He would end providing a geometric proof that is almost correct by modern standards in 1621, as part of volume V of hisEpitome of Copernican AstronomyDavis2003.

The fifth volume of the bookHarmonici mundi(harmony of the world), published in 1619Kepler1619, contains—without much fanfare—the statement that would become known as his third law. Kepler discovered this proportionality relationship around 1618 while attempting to find a connection between the movement of the planets and musical harmonies (a problem that would obsess him for his entire adult life). The discovery was also based on the analysis of empirical data, but Kepler did not consider it important enough to provide a table of the measurements in the text. Later on, in theEpitome, he would attempt—incorrectly—to explain the origin of the third law by assuming that the volumes of the planets were proportional to their distance from the Sun, and their densities decayed inversely as the square root of their distance to the SunLinton2004.

## 4Lambert’s problem

As we concluded from the argument developed in Section3.2, the only admissible trajectories for an object moving solely under the influence of a gravitational potential are conic sections. We will refer to movement along these trajectories as “free falling” since, once the particle is placed on a given orbit, conservation of angular momentum takes over and no additional energy is required to set it in motion. As is evident from equation (19b), considering that the masses of the particle and the attractive center are fixed and given, the particular conic section will be determined by the particle’s energy—or equivalently its velocity.

Lambert’s problem can be expressed as:

## Problem 1(Lambert’s Problem)

Given a particle located at the position𝒓1\bm{r}_{1}and a target position𝒓2\bm{r}_{2}, determine the energy required to place the particle on a conical orbit connecting the two points, and such that the trip’s duration isΔ​t\Delta twhile completingQQrevolutions before arriving at𝒓2\bm{r}_{2}.

From the mathematical point of view, this question becomes a two–point boundary value problem involving the equations of motion (17) (or equivalently equation (10)). Boundary value problems differ from initial value problems in the sense that, instead of knowing the initial position and velocity,𝒓\bm{r}and𝒓˙0\bm{\dot{r}}_{0},
of the particle (or alternatively its energy and angular momentum), the initial and final positions𝒓0\bm{r}_{0}and𝒓f\bm{r}_{f}are prescribed. This condition changes substantially the mathematical treatment of the problem. One key difference is that boundary value problems tend to have multiple solutions and therefore need supplemental physical information to elucidate the correct answer. Intuitively, a particle could travel along the same—closed—conic section either clockwise or counter–clockwise and complete multiple cycles before arriving at the final position. As we shall soon see, in our case the additional information will pertain to the number of revolutions that the particle can complete before arriving at the target endpoint. We will appeal to the geometric analysis of the possible trajectories that we developed in the previous section to sidestep the problem ofintegratingthe boundary value problem.

In what follows, our analysis will be focused only on particles that follow elliptical trajectories. We will consider that the ellipse has a semi–major axis of lengthaa, a semi–minor axis of lengthbb, eccentricity0≤e<10\leq e<1(understanding the circle as the limiting case of ellipses ase→0e\to 0), and the attracting center is located at the focusF1F_{1}as depicted in Figure5. Derivations following similar arguments for other conical orbits can be found inGrossman1996;Izzo2014;LaBl1969;LaBlDe1966—although the exposition in those sources is less detailed.

## 4.1Eccentric anomaly

Up to this point we have described the positionPPof a particle by its distance,rr, to the attractive center located at the focus, and the angleθ\thetasubtended by the vector connectingPPtoF1F_{1}, i.e. thetrue anomaly. However, in some cases it is convenient to characterize the position as if the particle were traversing a circle. This is achieved by inscribing the elliptical trajectory inside of an auxiliary circle of radiusaa, and projecting the pointPPvertically (in the same up/down direction as the vector connectingF1F_{1}toPP) onto the auxiliary circle as depicted in Figure5. We denote byP′P^{\prime}andCCthe points where the vertical line passing throughPPintersects the auxiliary circle and the horizontal line connecting the foci, respectively. The angleϕ\phiformed between the horizontal axis and the vector connecting the originOOand the pointP′P^{\prime}is known as theeccentric anomaly.

We first note that, as depicted in the right panel of Figure5(where both segments are highlighted in red), the horizontal coordinate of a pointPPon the ellipse can be written in terms of the eccentric anomaly asa​cos⁡ϕa\cos\phi, while its vertical component is easily expressed in terms of the true anomaly asr​sin⁡θr\sin\theta. Hence a point in the ellipse has coordinates given by(x,y)=(a​cos⁡ϕ,r​sin⁡θ).(x,y)=(a\cos\phi,r\sin\theta).(27)

Recalling that the lengths of the semi–major and semi–minor axes of the ellipse areaaandbb, respectively, and that the pointP=(a​cos⁡ϕ,r​sin⁡θ)P=(a\cos\phi,r\sin\theta)must satisfy the Cartesian equation of the ellipse1=x2a2+y2b2=a2​cos2⁡ϕa2+r2​sin2⁡θb21=\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=\frac{a^{2}\cos^{2}\phi}{a^{2}}+\frac{r^{2}\sin^{2}\theta}{b^{2}}

we obtainr​sin⁡θ=b​sin⁡ϕ.r\sin\theta=b\sin\phi.(28)

This relation, which together with (27) amounts to the familiar parametrization of an ellipse in terms of its central angle in the form(a​cos⁡ϕ,b​sin⁡ϕ)(a\cos\phi,b\sin\phi), will prove useful soon.

Our next goal is to express the positionPPin terms of the radiusrrand the eccentric anomalyϕ\phi. We start by observing that the length of the segmentC​F1CF_{1}appearing in Figure5can be expressed in two different ways. On the one hand, it is one of the legs of the right triangleC​F1​PCF_{1}P, and therefore|C​F1|=−r​cos⁡θ.|CF_{1}|=-r\cos\theta.

On the other hand, the length can be computed by subtracting the length of the segmentO​COCfrom that of the segmentO​F1OF_{1}(i.e. the focal length), which yields|C​F1|=|O​F1|−|O​C|=a​e−a​cos⁡ϕ.|CF_{1}|=|OF_{1}|-|OC|=ae-a\cos\phi.

Equating the two expressions above and solving forcos⁡θ\cos\thetaresults incos⁡θ=a​(cos⁡ϕ−e)r.\cos\theta=\frac{a(\cos\phi-e)}{r}.

From the focal representation of the ellipse (8b), we can obtaincos⁡θ=1e​(a​(1−e2)r−1).\cos\theta=\frac{1}{e}\left(\frac{a(1-e^{2})}{r}-1\right).

The true anomaly,θ,\theta,can be eliminated by equating the last two expressions. Solving then forrrin the ensuing equality yields the following relationship betweenrrand the eccentric anomalyϕ\phi:r=a​(1−e​cos⁡ϕ).r=a(1-e\cos\phi).(29)

This equation is the equivalent of the polar equation of the ellipse, when the position of the point along the ellipse is identified by its distance to the focus,rr, and its eccentric anomalyϕ\phi.Figure 5:Left: The horizontal coordinate of a pointPPin the ellipse can be expressed in terms of the eccentric anomalyϕ\phi, while the vertical coordinate can be expressed in terms of the true anomalyθ\theta. The segments are marked in red in the diagram. The expressions for the two coordinates can be combined through the Cartesian equation for an ellipse to produce a relation between the two anomalies. Right: The positionPPof a point in an ellipse, centered at the origin with semi–major axisaa, can be described by its distancerrto one of the foci and the angleϕ\phisubtended by the radius joining the origin and the vertical projectionP′P^{\prime}of the pointPPonto an auxiliary circle of radiusaacentered at the origin. The angleϕ\phiis known as theeccentric anomaly.

## 4.2Kepler’s equation

Thus far, we have obtained two analytic expressions for the position of a particle on an ellipse: the focal equation of the ellipse (8b) and the eccentric equation (29), both of which relate the distance to the focusrrto a different angular parameter. Equating these two expressions results ina​(1−e2)1+e​cos⁡θ=r=a​(1−e​cos⁡ϕ).\frac{a(1-e^{2})}{1+e\cos\theta}=r=a(1-e\cos\phi).

Differentiating the expression above with respect to time yieldsa​e​(1−e2)​θ˙​sin⁡θ(1+e​cos⁡θ)2=r˙=a​e​ϕ˙​sin⁡ϕ.\frac{ae(1-e^{2})\dot{\theta}\sin\theta}{(1+e\cos\theta)^{2}}=\dot{r}=ae\dot{\phi}\sin\phi.

Solving forϕ˙\dot{\phi}and simplifying we obtainϕ˙=\displaystyle\dot{\phi}=\,(1−e2)(1+e​cos⁡θ)2⋅θ˙​sin⁡θsin⁡ϕ\displaystyle\frac{(1-e^{2})}{(1+e\cos\theta)^{2}}\cdot\frac{\dot{\theta}\sin\theta}{\sin\phi}\qquad\qquad=\displaystyle=\,r2a2​(1−e2)⋅θ˙​sin⁡θsin⁡ϕ\displaystyle\frac{r^{2}}{a^{2}(1-e^{2})}\cdot\frac{\dot{\theta}\sin\theta}{\sin\phi}(From(8b))\displaystyle(\text{From }\eqref{eq:PolarConicB})=\displaystyle=\,1a2​(1−e2)⋅Lm⋅sin⁡θsin⁡ϕ\displaystyle\frac{1}{a^{2}(1-e^{2})}\cdot\frac{L}{m}\cdot\frac{\sin\theta}{\sin\phi}(From(15))\displaystyle(\text{From }\eqref{eq:L})=\displaystyle=\,1a​1−e2⋅Lm⋅sin⁡θb​sin⁡ϕ\displaystyle\frac{1}{a\sqrt{1-e^{2}}}\cdot\frac{L}{m}\cdot\frac{\sin\theta}{b\sin\phi}(From(6))\displaystyle(\text{From }\eqref{eq:AandB})=\displaystyle=\,1a​1−e2⋅Lm⋅sin⁡θr​sin⁡θ\displaystyle\frac{1}{a\sqrt{1-e^{2}}}\cdot\frac{L}{m}\cdot\frac{\sin\theta}{r\sin\theta}(From(28))\displaystyle(\text{From }\eqref{eq:cosphi})=\displaystyle=\,(mL​G​Ma)​Lm⋅1r\displaystyle\left(\frac{m}{L}\,\sqrt{\frac{GM}{a}}\right)\frac{L}{m}\cdot\frac{1}{r}\qquad(From(20))\displaystyle(\text{From }\eqref{eq:Lae})=\displaystyle=\,ar​G​Ma3=ar⋅2​π𝒯\displaystyle\frac{a}{r}\sqrt{\frac{GM}{a^{3}}}\;=\;\frac{a}{r}\cdot\frac{2\pi}{\mathcal{T}}(From(26))\displaystyle(\text{From }\eqref{eq:K3})=\displaystyle=\,1(1−e​cos⁡ϕ)⋅2​π𝒯\displaystyle\frac{1}{(1-e\cos\phi)}\cdot\frac{2\pi}{\mathcal{T}}(From(29)).\displaystyle(\text{From }\eqref{eq:rphi}).

The ratio2​π/𝒯2\pi/\mathcal{T}is the average angular speed of the particle undergoing a full orbit over a periodTT; it is referred to as themean motionand sometimes denoted by the letternn. We have thus obtained the relation(1−e​cos⁡ϕ)​ϕ˙=2​π𝒯,(1-e\cos\phi)\dot{\phi}=\frac{2\pi}{\mathcal{T}},

which can be readily integrated with respect to time to obtainϕ−e​sin⁡ϕ=2​π𝒯​(t−t0),\phi-e\sin\phi=\frac{2\pi}{\mathcal{T}}(t-t_{0}),(30)

where the integration constant−2​π​t0/𝒯-2\pi t_{0}/\mathcal{T}follows from the convention on setting the initial position at the perihelion (or periapsis), where the angleϕ\phivanishes. This equation is known as Kepler’s equation.

The quantity2​π​(t−t0)/𝒯2\pi(t-t_{0})/\mathcal{T}appearing on the right hand side of (30) hasangularunits (recall that2​π=360∘2\pi=360^{\circ}is the angular measure of a circle in radians) and is called themean anomaly. It can be interpreted as the angular position of a fictitious body that moves with constant angular velocity2​π/𝒯2\pi/\mathcal{T}around a circular orbit of radiusaa. It is sometimes denoted byMMin the literature. To avoid confusing it with the mass of the attractive center, we will not follow this convention in the text and will write out the full quotient explicitly instead. The fact that the mean anomaly is an angular measure that varies linearly with time enables the use of time intervals as proxies for angular displacement. If theactualangular displacementϕ\phifrom the center of the ellipse is sought for, it can be obtained from the mean anomaly by solving Kepler’s equation. The angular displacement associated with the focus–centered polar coordinates(r,θ)(r,\theta)can be obtained then from the eccentric anomaly from equation (28).

## 4.3Lambert’s systemFigure 6:Left: Since the location of the attractive centerFFand the initial and final pointsP1P_{1}andP2P_{2}are known, the lengths of the position vectorsr1,r2r_{1},r_{2}and the chordc:=r2−r1c:=r_{2}-r_{1}can be computed. The goal is to determine the unknown ellipse (dashed line) connecting the points and such that the travel time equals a prescribed value. Right: The true anomaly, denoted byθ\thetaand eccentric anomaly, denoted byϕ\phi, are angular descriptors of the pointsP1P_{1}andP2P_{2}.

Let us recall that our goal is to ascertain the energy required to place a vessel on an elliptic orbit with the attractive center located at one of its foci and passes through two given pointsP1P_{1}andP2P_{2}. In geometric terms, we must find the length of the ellipse’s semi–major axisaa, the value of the eccentricityee, and the angle between the major axis and the horizontal line. Once these geometric parameters are known, the energyEEcan be recovered from Kepler’s first law using equation (23).

In this section, we will take advantage of Kepler’s equation (30), the eccentric description of the ellipse (29), and a simple geometric observation regarding the distance betweenP1P_{1}andP2P_{2}(i.e. the length of the chordc:=r2−r1c:=r_{2}-r_{1}), to obtain a system of equations that will ultimately provide us with the desired parameters. We will be making use of the following trigonometric identities, which can be easily derived from those of the sine and cosine of sums/differences of angles:cos⁡ϕ1−cos⁡ϕ2\displaystyle\cos\phi_{1}-\cos\phi_{2}=2​sin⁡(ϕ1+ϕ22)​sin⁡(ϕ2−ϕ12),\displaystyle=2\sin\left(\!\frac{\phi_{1}+\phi_{2}}{2}\!\right)\sin\left(\!\frac{\phi_{2}-\phi_{1}}{2}\!\right),(31a)sin⁡ϕ1−sin⁡ϕ2\displaystyle\sin\phi_{1}-\sin\phi_{2}=−2​cos⁡(ϕ1+ϕ22)​sin⁡(ϕ2−ϕ12),\displaystyle=-2\cos\left(\!\frac{\phi_{1}+\phi_{2}}{2}\!\right)\sin\left(\!\frac{\phi_{2}-\phi_{1}}{2}\!\right),(31b)cos⁡ϕ1+cos⁡ϕ2\displaystyle\cos\phi_{1}+\cos\phi_{2}=2​cos⁡(ϕ1+ϕ22)​cos⁡(ϕ2−ϕ12).\displaystyle=2\cos\left(\!\frac{\phi_{1}+\phi_{2}}{2}\!\right)\cos\left(\!\frac{\phi_{2}-\phi_{1}}{2}\!\right).(31c)

We start by noting that—since the locations of the attractive center and initial and final points are given—the lengths of the position vectors and the distanceccbetweenP1P_{1}andP2P_{2}(as depicted in the left panel of Figure6) are all known. Therefore, using the eccentric description of the pointsP1=(a​cos⁡ϕ1,b​sin⁡ϕ1)andP2=(a​cos⁡ϕ2,b​sin⁡ϕ2)P_{1}=(a\cos\phi_{1},b\sin\phi_{1})\qquad\text{ and }\qquad P_{2}=(a\cos\phi_{2},b\sin\phi_{2})

depicted in the right panel of Figure6, we can relateccto the lengthaaand the eccentric anomaliesϕ1\phi_{1}andϕ2\phi_{2}as follows:c2\displaystyle c^{2}=|P1−P2|2\displaystyle=|P_{1}-P_{2}|^{2}=|(a​(cos⁡ϕ1−cos⁡ϕ2),b​(sin⁡ϕ1−sin⁡ϕ2))|2\displaystyle=|(a(\cos\phi_{1}-\cos\phi_{2}),b(\sin\phi_{1}-\sin\phi_{2}))|^{2}=a2​((cos⁡ϕ1−cos⁡ϕ2)2+(1−e2)​(sin⁡ϕ1−sin⁡ϕ2)2)\displaystyle=a^{2}\left((\cos\phi_{1}-\cos\phi_{2})^{2}+(1-e^{2})(\sin\phi_{1}-\sin\phi_{2})^{2}\right)\qquad\quad(From (6))=4​a2​(1−e2​cos2⁡(ϕ1+ϕ22))​sin2⁡(ϕ2−ϕ12)\displaystyle=4a^{2}\left(1-e^{2}\cos^{2}\left(\frac{\phi_{1}+\phi_{2}}{2}\right)\right)\sin^{2}\left(\frac{\phi_{2}-\phi_{1}}{2}\right)(From (31a) and (31b)).\displaystyle\text{\small(From \eqref{eq:TrigIDsA} and \eqref{eq:TrigIDsB})}.(32a)The equation above, that uses the known magnitude of the difference|r2−r1|=c|r_{2}-r_{1}|=c, will be the first equation of our system. We now use the eccentric representation (29) to write the radial distance in terms of the eccentric anomaly for the initial and final pointsP1P_{1}andP2P_{2}asr1=a​(1−e​cos⁡ϕ1)andr2=a​(1−e​cos⁡ϕ2).r_{1}=a(1-e\cos\phi_{1})\qquad\text{ and }\qquad r_{2}=a(1-e\cos\phi_{2}).Adding these two equations and using (31c) we obtainr1+r2=2​a​(1−e​cos⁡(ϕ1+ϕ22)​cos⁡(ϕ2−ϕ12)).r_{1}+r_{2}=2a\left(1-e\cos\left(\frac{\phi_{1}+\phi_{2}}{2}\right)\cos\left(\frac{\phi_{2}-\phi_{1}}{2}\right)\right).(32b)This expression relates the value of the sumr1+r2r_{1}+r_{2}to the unknown geometric parameters, and will constitute the second equation of our system. Finally, from Kepler’s equation (30) it follows that at the timest1t_{1}andt2t_{2}when the vessel is located at the pointsP1P_{1}andP2P_{2}respectively, we haveϕ1−e​sin⁡ϕ1=2​π𝒯​(t1−t0),andϕ2−e​sin⁡ϕ2=2​π𝒯​(t2−t0).\phi_{1}-e\sin\phi_{1}=\frac{2\pi}{\mathcal{T}}(t_{1}-t_{0}),\qquad\text{ and }\qquad\phi_{2}-e\sin\phi_{2}=\frac{2\pi}{\mathcal{T}}(t_{2}-t_{0}).Subtracting the last two equations and using (31b) leads to2​π𝒯​(t2−t1)=ϕ2−ϕ1−2​e​cos⁡(ϕ1+ϕ22)​sin⁡(ϕ2−ϕ12).\frac{2\pi}{\mathcal{T}}(t_{2}-t_{1})=\phi_{2}-\phi_{1}-2e\cos\left(\!\frac{\phi_{1}+\phi_{2}}{2}\!\right)\sin\left(\!\frac{\phi_{2}-\phi_{1}}{2}\!\right).Finally, we make use of Kepler’s third law (24) to express the period𝒯\mathcal{T}in terms of the semi–major axis and rewrite the previous equation in the form:G​Ma3​(t2−t1)=ϕ2−ϕ1−2​e​cos⁡(ϕ1+ϕ22)​sin⁡(ϕ2−ϕ12).\sqrt{\frac{GM}{a^{3}}}(t_{2}-t_{1})=\phi_{2}-\phi_{1}-2e\cos\left(\!\frac{\phi_{1}+\phi_{2}}{2}\!\right)\sin\left(\!\frac{\phi_{2}-\phi_{1}}{2}\!\right).(32c)

Equations (32a), (32b) and (32c), which sometimes are known collectively as Lambert’s system, relate the geometric unknownsaa,ee,ϕ1\phi_{1}, andϕ2\phi_{2}to the known quantitiesc=|r2−r1|c=|r_{2}-r_{1}|andr1+r2r_{1}+r_{2}. The time intervalt2−t1t_{2}-t_{1}appearing in the left-hand side of (32c), although not knowna priori, can be prescribed as part of the problem data. These equations will be the starting point to our determination of the transfer ellipse.

## 4.4Lagrange’s solution

A closer inspection of system (32) would seem to indicate that it contains one too many unknowns, as there are three equations and four unknown quantities:aa,ee,ϕ1\phi_{1}, andϕ2\phi_{2}. However, Lagrange observed that the anglesϕ1\phi_{1}andϕ2\phi_{2}, along with the eccentricityee, appear in the system only in two particular combinations:ϕ2−ϕ1ande​cos⁡(ϕ1+ϕ22).\phi_{2}-\phi_{1}\qquad\text{ and }\qquad e\cos\left(\frac{\phi_{1}+\phi_{2}}{2}\right).

One would then be tempted to perform a naïve change of variables and proceed to attempt a solution of the system (32) in terms of the three unknownsaa,ϕ2−ϕ1\phi_{2}-\phi_{1}ande​cos⁡(12​(ϕ1+ϕ2))e\cos\left(\tfrac{1}{2}(\phi_{1}+\phi_{2})\right). However Lagrange’s insight went one step further and he realized that by introducing two auxiliary variablesα\alphaandβ\betasuch thatcos⁡(α+β2)\displaystyle\cos\left(\!\frac{\alpha+\beta}{2}\!\right)=e​cos⁡(ϕ1+ϕ22),\displaystyle=e\cos\left(\!\frac{\phi_{1}+\phi_{2}}{2}\!\right),\qquad\qquad0≤α+β<2​π,\displaystyle 0\leq\alpha+\beta<2\pi,(33a)α−β\displaystyle\alpha-\beta=ϕ2−ϕ1−2​π​Q,\displaystyle=\phi_{2}-\phi_{1}-2\pi Q,0≤α−β<2​π,\displaystyle 0\leq\alpha-\beta<2\pi,(33b)

the system (32) takes a much simpler form. In the expression above,QQis the number of orbital cycles completed by the vessel in the given time intervalt2−t1t_{2}-t_{1}and the constraints on the sum a difference of the auxiliary variables account for the periodicity of equation(33a).

Performing the substitutions (33) in the system (32) yieldsc2​a\displaystyle\frac{c}{2a}=sin⁡(α+β2)​sin⁡(α−β2),\displaystyle=\sin\left(\!\frac{\alpha+\beta}{2}\!\right)\sin\left(\!\frac{\alpha-\beta}{2}\!\right),r1+r22​a\displaystyle\frac{r_{1}+r_{2}}{2a}=1−cos⁡(α+β2)​cos⁡(α−β2),\displaystyle=1-\cos\left(\!\frac{\alpha+\beta}{2}\!\right)\cos\left(\!\frac{\alpha-\beta}{2}\!\right),G​Ma3​(t2−t1)\displaystyle\sqrt{\frac{GM}{a^{3}}}(t_{2}-t_{1})=2​π​Q+α−β−2​cos⁡(α+β2)​sin⁡(α−β2).\displaystyle=2\pi Q+\alpha-\beta-2\cos\left(\!\frac{\alpha+\beta}{2}\!\right)\sin\left(\!\frac{\alpha-\beta}{2}\!\right).

We can now apply the trigonometric identities (31) to rewrite the system in terms of cosines and sines of a single angle (as opposed to sums and differences), obtainingca\displaystyle\frac{c}{a}=cos⁡β−cos⁡α,\displaystyle=\cos\beta-\cos\alpha,(34a)2−r1+r2a\displaystyle 2-\frac{r_{1}+r_{2}}{a}=cos⁡β+cos⁡α,\displaystyle=\cos\beta+\cos\alpha,(34b)G​Ma3​(t2−t1)\displaystyle\sqrt{\frac{GM}{a^{3}}}(t_{2}-t_{1})=2​π​Q+α−sin⁡α−(β−sin⁡β).\displaystyle=2\pi Q+\alpha-\sin\alpha-(\beta-\sin\beta).(34c)

The last equation of the system above is sometimes calledLagrange’s transfer time equation. Using the first two equations to solve forcos⁡α\cos\alphaandcos⁡β\cos\betawe obtaincos⁡α=1−r1+r2+c2​aandcos⁡β=1−r1+r2−c2​a.\cos\alpha=1-\frac{r_{1}+r_{2}+c}{2a}\qquad\text{ and }\qquad\cos\beta=1-\frac{r_{1}+r_{2}-c}{2a}\,.(35)

We will need to perform some further manipulations on the second of these equalities as followscos⁡β=1−r1+r2−c2​a=1−(r1+r2)2−c22​a​(r1+r2+c).\cos\beta=1-\frac{r_{1}+r_{2}-c}{2a}=1-\frac{(r_{1}+r_{2})^{2}-c^{2}}{2a(r_{1}+r_{2}+c)}.

Using the law of cosines, we can express the square of the length of the chord in terms of the true anomaliesθ1\theta_{1}andθ2\theta_{2}asc2=r12−2​r1​r2​cos⁡(θ2−θ1)+r22,c^{2}=r_{1}^{2}-2r_{1}r_{2}\cos(\theta_{2}-\theta_{1})+r_{2}^{2}\,,

and substitute above to obtaincos⁡β=1−r1​r2​(1+cos⁡(θ2−θ1))a​(r1+r2+c)=1−2​r1​r2​cos2⁡(12​(θ2−θ1))a​(r1+r2+c),\cos\beta=1-\frac{r_{1}r_{2}(1+\cos(\theta_{2}-\theta_{1}))}{a(r_{1}+r_{2}+c)}=1-\frac{2r_{1}r_{2}\cos^{2}\left(\tfrac{1}{2}(\theta_{2}-\theta_{1})\right)}{a(r_{1}+r_{2}+c)},(36)

where we made use of the identity1+cos⁡A=2​cos2⁡(A/2)1+\cos A=2\cos^{2}(A/2).

To connect the equality on the left of (35) and (36)(that involve only cosines) to equation (34c) (that involves only sines), we will make use of the trigonometric identitycos⁡θ=1−2​sin2⁡(θ/2){\displaystyle\cos\theta=1-2\sin^{2}(\theta/2)}which, upon substitution into said equations, yieldssin2⁡(α/2)=r1+r2+c4​aandsin2⁡(β/2)=r1​r2​cos2⁡(12​(θ2−θ1))a​(r1+r2+c).\sin^{2}(\alpha/2)=\frac{r_{1}+r_{2}+c}{4a}\qquad\text{ and }\qquad\sin^{2}(\beta/2)=\frac{r_{1}r_{2}\cos^{2}\left(\tfrac{1}{2}(\theta_{2}-\theta_{1})\right)}{a(r_{1}+r_{2}+c)}.(37)

Solving for1/a1/ain the two expressions above, equating and taking square roots leads tosin⁡(β/2)=(2​(r1​r2)1/2​cos⁡(12​(θ2−θ1))r1+r2+c)​sin⁡(α/2),\sin(\beta/2)=\left(\frac{2(r_{1}r_{2})^{1/2}\cos\left(\tfrac{1}{2}(\theta_{2}-\theta_{1})\right)}{r_{1}+r_{2}+c}\right)\sin(\alpha/2),(38)

where the positive and negative roots are determined by the differenceθ2−θ1\theta_{2}-\theta_{1}, as the cosine will yield positive and negative values depending on whetherθ2−θ1\theta_{2}-\theta_{1}belongs to the interval[0,π][0,\pi]or[π,2​π][\pi,2\pi].

We now apply the first equation in (37) toaato express the left hand side of equation (34c) asG​Ma3​(t2−t1)=(t2−t1)​G​M​(2​sin⁡(α/2)r1+r2+c)3.\sqrt{\frac{GM}{a^{3}}}(t_{2}-t_{1})=(t_{2}-t_{1})\sqrt{GM}\left(\frac{2\sin(\alpha/2)}{\sqrt{r_{1}+r_{2}+c}}\right)^{3}.

From this it follows that we can rewrite (34c) as(t2−t1)​G​M​(2​sin⁡(α/2)r1+r2+c)3=2​π​Q+α−sin⁡α−(β−sin⁡β).(t_{2}-t_{1})\sqrt{GM}\left(\frac{2\sin(\alpha/2)}{\sqrt{r_{1}+r_{2}+c}}\right)^{3}=2\pi Q+\alpha-\sin\alpha-(\beta-\sin\beta).(39)

The nonlinear system defined by equations (38) and (39) involves only the unknown auxiliary anglesα\alphaandβ\beta. Sincer1,r2,θ1,θ2r_{1},r_{2},\theta_{1},\theta_{2}, andccare all known, it suffices to prescribe the travel timet2−t1t_{2}-t_{1}to be able to attempt a solution. Note that, depending on the values of the parameters given, no solutions may exist or there may be multiple solutions. In the particular case when less than one full orbit is completed during the travel time (i.e.Q=0Q=0), any existing solution must be uniqueBattin;simo1973;Woollands2017. Once the system is solved for these two unknowns, the length of the semi–major axisaacan be recovered from the left equality in (37). This value, together with equation (23) produces the energy required to place the vessel on the elliptic transfer orbit.

## 4.5A second historical digression and some closing remarks

The polymath Johann Heinrich Lambert was born on August 26th.1728 in Mülhausen, Alsace—which was then part of the Swiss confederation and now is the city of Mulhouse, France—to a modest family. He left formal schooling at the age of 12 to assist in his father’s tailor business, but managed to find time to continue his studies independently. In 1764 he was appointed a Royal Professor in the Academy of Berlin, by the Emperor Friederich II of Prussia. He died on September 25th.1777 in Berlin from respiratory complications—pneumonia according to some sourcesVolk1980or tuberculosis according to othersDorregoLpez2023. A brief account of his life can be found atMacTutor, while a more detailed one can be found inDorregoLpez2023. Although with the passage of time his mathematical work was overshadowed by that of his illustrious contemporaries Leonhard Euler, Joseph–Louis Lagrange, and Pierre–Simon Laplace, during his lifetime he was counted among Europe’s top philosophers, astronomers, physicists and mathematicians and became known asthe Alsatian Newtonorthe Alsatian LeibnizVolk1980. He made numerous contributions to number theory, geometry, and probability, and is credited with producing the first proof of the irrationality ofπ\piWallisser.

His interest in celestial mechanics dates back at least to 1744, when he got captivated by the great comet of Klinkenberg–ChéseauxDorregoLpez2023which—by contemporary accounts—developed as many as six tails. It is unclear if the young Lambert obtained any mathematical results in the immediate aftermath of the comet’s passing, but we know that by early 1761 the idea behind Lambert’s theorem—under the assumption of a parabolic trajectory—had matured in his mind enough for him to share it with Leonhard Euler in a letter dated on February 6th.1761:“I forgot to turn problem §210 around, that the orbit may be found1∘1^{\circ}by the 3 sidesF​NFN,F​MFM,N​MNMand the timeTTrequired to traverse the arcN​MNM.2∘2^{\circ}by the ratio(F​M:F​N)(FM:FN), the angleN​F​MNFM, the timeTTand the periodic time. If the diameter of the Sun can be measured precisely enough, two observations suffice to determine the Earth’s orbit using the latter theorem.”Albouy2019;Bopp:1924;EulerArchiveVery shortly after his letter to Euler, Lambert went on to treat the elliptic and hyperbolic cases and published the results as part of his bookLambert:1761. He sent the book to Euler who, in March 24th.1761, replied in a letter:“The beautiful proof of the area of a parabolic sector, the expression for which you communicated to me gave me great pleasure; but I was even more surprised to see its application to elliptic sectors […] I easily recognize that the methods I proposed earlier may be improved considerably.”Albouy2019;Bopp:1924;EulerArchiveAs indicated by the final phrase above, in fact Euler had started working on the determination of the movement of comets at least as far back as 1742, after the passing of Halley’s comet, publishing in 1743 a geometric methodEuler1743and then in 1744 the first purely analytic method to determine a parabolic orbit based on three observations of the cometBistafa2021;Euler1744. However, Euler did not attempt to generalize his calculations to orbits other than parabolic and therefore Lambert is generally credited with the introduction of the problem that now bears his nameAlbouy2019.

In his proof, Lambert made use solely of geometric tools. This made the argument hard to understand and even harder to apply for practical calculations. In fact, in the same letter mentioned above, Euler points out that:“Your theorem for expressing the area of a parabolic sector is excellent, I can see the truth of it, but by such
detours, that I could never have arrived to it had I not known it in advance; I therefore wait impatiently to see
the analysis leading to it without detours.”Albouy2019;Bopp:1924;EulerArchiveLambert did not arrive at an alternate proof using the modern methods of calculus. This would have to wait until 1780, already after his passing, when Lagrange finally arrived at an argument similar to the one presented here. Countless other proofs to the theorem have been given and rediscovered over time. In the wonderful—but heavily mathematical—articleAlbouy2019, Albouy discusses several “families” of proofs and presents a detailed timeline of early attempts and some highlights of modern ones.

In his original statement, Lambert in fact did not pose a problem in the way we did at the beginning of Section4. Instead, he made a statement about the relevant variables that determine the travel time, claiming that it depends only on the distances to the points, the length of the chord connecting them and the length of the semi–major axis of the conic (the parabolic case can be obtained by lettinga→∞a\to\infty(CoPr1993,, Problem 4.3)). In modern notation, the theorem can be stated as:

## Theorem 4.1(Lambert’s theorem)

LetP1P_{1}andP2P_{2}denote the positions of a particle moving under the influence of a gravitational potential at timest1t_{1}andt2t_{2}. Ifr1,r2r_{1},r_{2}denote the distances ofP1P_{1}andP2P_{2}from the attractive center andc:=|P2−P1|c:=|P_{2}-P_{1}|, there exists a, possibly multi–valued, function such thatt2−t1=F​(a,r1+r2,c).t_{2}-t_{1}=F(a,r_{1}+r_{2},c).

Going back to the analysis in the previous section, and recalling that the auxiliary variablesα\alphaandβ\betaare both functions ofr1+r2r_{1}+r_{2},ccand the semi–major lengthaa, it is clear that equation (39) is only one step away from the form appearing in Theorem4.1, which is why Lagrange’s argument constitutes an analytic proof of Lambert’s original statement.

Although clearly Theorem4.1is related to the orbit–determination Problem1, they are certainly not the same thing. According to AlbouyAlbouy2019, it was not until the 1960’s when the termsLambert’s theoremandLambert’s problemstarted being used interchangeably—with the second one eventually taking over. This was perhaps due to the fact that, with the advent of the space age, Lambert’s work was seen through the lens of orbital determination algorithms, many of which involved the solution of Lambert’s problem1. As it concerns practical solution methods—rather than proofs of the theorem—there have been myriads of proposed algorithms. A recent comparative study of several of the most widely used approaches can be found inMG2021.

## 5Statements and declarations

Author contribution statment.Because of the nature of mathematical research, authors are considered on equal footing and are always listed in alphabetical order. In other words,as opposed to other disciplines, in mathematics there is no “first author”. Lenox Helene Baloglou, Parneet Gill and Tonatiuh Sánchez-Vizuet all contributed in equal proportion.

Competing interests.The authors declare that they have no conflict of interest.

Funding.All authors were partially funded by the United States National Science Foundation through the grant NSF-DMS-2137305. Lenox Helene Baloglou is thankful for the generous support of the University of Arizona’s RII-Sponsored Campuswide Undergraduate Student–Initiated Original Research Program.

## References
- [1]N. Adurthi and M. Majji.Uncertain Lambert problem: A probabilistic approach.The Journal of the Astronautical Sciences, 67(2):361–386,
Mar. 2020.
- [2]A. Albouy.Lambert’s theorem: Geometry or dynamics?Celestial Mechanics and Dynamical Astronomy, 131(9), Aug. 2019.
- [3]R. Armellin, D. Gondelach, and J. F. San Juan.Multiple revolution perturbed Lambert problem solvers.Journal of Guidance, Control, and Dynamics, 41(9):2019–2032,
Sept. 2018.
- [4]V. I. Arnold.Mathematical Methods of Classical Mechanics.Springer New York, 1978.
- [5]N. Arora and R. P. Russell.A fast and robust multiple revolution Lambert algorithm using a
cosine transformation.Paper AAS, 13(728):162, 2013.
- [6]L. H. Baloglou.The Lambert problem of orbital dynamics.Honors thesis, The University of Arizona, Tucson, AZ, May 2025.
- [7]L. H. Baloglou, P. Gill, and T. Sánchez-Vizuet.A surrogate–based solver for Lambert’s problem.(In preparation), 2025.
- [8]R. H. Battin.An introduction to the mathematics and methods of
astrodynamics.AIAA Education Series. American Institute of Aeronautics &
Astronautics, Reston, VA, June 1999.
- [9]W. Besant.Conic Sections, Treated Geometrically.Cambridge school and college text books. Deighton, Bell; London,
1890.
- [10]S. R. Bistafa.Revisiting Euler’s orbital calculations for the comet of 1742.Advances in Historical Studies, 10(01):73–92, 2021.
- [11]K. Bopp.Leonhard Eulers und Johann Heinrich lamberts Briefwechsel.Abhandlungen der Preussischen Akademie der Wissenschaften,
Physikalisch-Mathematische Klasse, 2:7–37, 1924.
- [12]D. M. Burton.The history of mathematics: An introduction.McGraw-Hill Professional, New York, NY, 7 edition, Feb. 2010.
- [13]M. Caspar.Kepler.Dover Publications, 2012.
- [14]A. E. L. Davis.The mathematics of the area law: Kepler’s successful proof in
Epitome Astronomiae Copernicanae (1621).Archive for History of Exact Sciences, 57(5):355–393, July
2003.
- [15]E. Dorrego López and E. Fuentes Guillén.Johann Heinrich Lambert A Biography in Context, page
3–35.Springer International Publishing, 2023.
- [16]D. Eagle.Gravity-perturbed earth orbit lambert problem - otb/fsolve.MATLAB Central File Exchange., 2025.Retrieved June 12, 2025.
- [17]L. Euler.Determinatio orbitae cometae qui mense Martio huius anni 1742
potissimum fuit observatus.Miscellanea Berolinensia, 7:1–90, 1734.
- [18]L. Euler.Theoria motuum planetarum et cometarum.Ambrosius Haude, Berlin, 1744.
- [19]G. Glaeser, H. Stachel, and B. Odehnal.The Universe of Conics.Springer Berlin Heidelberg, 2016.
- [20]N. Grossman.The Sheer Joy of Celestial Mechanics.Birkhäuser Boston, 1996.
- [21]D. Gueho, P. Singla, R. G. Melton, and D. Schwab.A comparison of parametric and non-parametric machine learning
approaches for the uncertain Lambert problem.InAIAA Scitech 2020 Forum. American Institute of Aeronautics
and Astronautics, Jan. 2020.
- [22]T. Hockey, V. Trimble, T. R. Williams, K. Bracher, R. A. Jarrell, J. D. Marche,
J. Palmeri, and D. Green, editors.Biographical encyclopedia of astronomers.Biographical Encyclopedia of Astronomers. Springer, New York, NY, 2
edition, July 2014.
- [23]D. Izzo.Revisiting Lambert’s problem.Celestial Mechanics and Dynamical Astronomy, 121(1):1–15,
Oct. 2014.
- [24]V. J. Katz.A history of mathematics.Pearson, Upper Saddle River, NJ, 3 edition, July 2008.
- [25]J. Kepler.Epitome Astronomiae Copernicanae.Prometheus Books, Amherst, NY, Nov. 1995.English translationEpitome of Copernican astronomy and
harmonies of the world.
- [26]J. Kepler.Harmonice mindi.American Philosophical Society: Memoirs of the American Philosophical
Society. American Philosophical Society, 1997.English translationThe Harmony of the World.
- [27]J. Kepler.Astronomia Nova.Green Lion Press, 2015.Foreword by Owen Gingerich.
- [28]J. Kepler.Nova stereometria dolorium vinariorum / new solid geometry of
wine barrels.Sciences Et Savoirs. Les Belles Lettres, May 2018.Translator and editor: Eberhard Knobloch.
- [29]J. H. Lambert.Insigniores orbitae cometarum proprietates, 1761, Augsburg.
- [30]E. R. Lancaster and R. C. Blanchard.A Unified Form of Lambert’s Theorem.NASA technical note. National Aeronautics and Space Administration,
1969.
- [31]E. R. Lancaster, R. C. Blanchard, and R. A. Devaney.A note on Lambert’s theorem.Journal of Spacecraft and Rockets, 3(9):1436–1438, 1966.
- [32]C. M. Linton.From Eudoxus to Einstein.Cambridge University Press, Cambridge, England, 2004.
- [33]J. Martínez Garrido.Lambert’s problem algorithms: A critical review.Honor’s thesis, Universidad Carlos III de Madrid, Madrid, Spain,
2021.
- [34]D. Morin.Introduction to Classical Mechanics: With Problems and
Solutions.Cambridge University Press, June 2012.
- [35]J. J. O’Connor and E. F. Robertson.Johann Heinrich Lambert.MacTutor History of Mathematics, University of St Andrews,
Scotland, 2004.https://mathshistory.st-andrews.ac.uk/Biographies/Lambert/.
- [36]A. of Perga and T. Heath.Treatise on Conic Sections.Cambridge Library Collection - Mathematics. Cambridge University
Press, 2013.
- [37]P. Panicucci, V. Morand, and D. Hautesserres.Perturbed Lambert’s problem solver based on differential algebra
optimization.InAIAA Aerospace sciences meeting, Reston, Va., 2018.
- [38]J. Prussing and B. Conway.Orbital Mechanics.Oxford University Press, 1993.
- [39]A. Rothman.Kepler’sEpitome of Copernican Astronomyin context.Centaurus, 63(1):171–191, Dec. 2020.
- [40]F. Scheck.Mechanics: From Newton’s Laws to Deterministic Chaos.Springer Berlin Heidelberg, 2010.
- [41]P. W. Schumacher, C. Sabol, C. C. Higginson, and K. T. Alfriend.Uncertain Lambert problem.Journal of Guidance, Control, and Dynamics, 38(9):1573–1584,
Sept. 2015.
- [42]C. Simó.Solución del problema de Lambert mediante regularización.Collectanea Mathematica, pages 231–248, 1973.
- [43]J. Stillwell.Mathematics and Its History.Springer New York, 2010.
- [44]J. Tabak.Mathematics and the Laws of Nature: Developing the Language of
Science.History of mathematics. Facts on File, 2011.
- [45]A. M. H. Teter, I. Nodozi, and A. Halder.Probabilistic Lambert problem: Connections with optimal mass
transport, Schrödinger bridge, and reaction-diffusion PDEs.SIAM Journal on Applied Dynamical Systems, 24(1):16–43, Jan.
2025.
- [46]The Euler archive.Euler’s correspondence with Johann Heinrich Lambert, Retreived
on June 12, 2025.http://eulerarchive.maa.org/correspondence/correspondents/Lambert.html.
- [47]B. F. Thompson and L. J. Rostowfske.Practical constraints for the applied Lambert problem.Journal of Guidance, Control, and Dynamics, 43(5):967–974,
May 2020.
- [48]S. T. Thornton and J. B. Marion.Classical dynamics of particles and systems.Cengage Learning, 5 edition, 2014.
- [49]A. J. Ureña.On the Lambert problem with drag.Regular and Chaotic Dynamics, 28(4–5):668–689, Oct. 2023.
- [50]O. Volk.Johann Heinrich Lambert and the determination of orbits for
planets and comets.Celestial Mechanics, 21(2):237–250, Feb. 1980.
- [51]R. Wallisser.On Lambert’s proof of the irrationality ofπ\pi, pages
521–530.De Gruyter, Berlin, New York, 2000.Proceedings of the International Conference held in Graz, Austria,
August 30 to September 5, 1998. Editors F. Halter–Koch and Robert F. Tichy.
- [52]C. Wilson.How did Kepler discover his first two laws?Scientific American, 226(3):92–107, 1972.
- [53]R. M. Woollands, J. L. Read, A. B. Probe, and J. L. Junkins.Multiple revolution solutions for the perturbed Lambert problem
using the method of particular solutions and Picard iteration.The Journal of the Astronautical Sciences, 64(4):361–378,
July 2017.
- [54]F. Xavier.Revisiting Kepler’s measurements—lecture notes.Online, Fall 2012.Retrieved on March 13, 2025.
https://www3.nd.edu/ math/10450/lecture
- [55]B. Yang, S. Li, J. Feng, and M. Vasile.Fast solver for J2-perturbed Lambert problem using deep neural
network.Journal of Guidance, Control, and Dynamics, 45(5):875–884,
May 2022.
- [56]G. Zhang, D. Zhou, D. Mortari, and M. R. Akella.Covariance analysis of Lambert’s problem via Lagrange’s
transfer–time formulation.Aerospace Science and Technology, 77:765–773, June 2018.
