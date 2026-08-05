# Nomic Structure and Reduction

**arXiv ID**: 2607.01289v1
**Authors**: Sean Gryb, Karim P. Y. Thébault
**Published**: 2026-07-01
**Categories**: physics.hist-ph, math-ph
**HTML URL**: https://arxiv.org/html/2607.01289v1

## Abstract

The canonical formulation of physical theories with irregular nomic structure is as constrained Hamiltonian theories within which ill-posedness of the equations of motion is connected to a pernicious form of surplus representational capacity. Such theories can be converted into theories with regular nomic structure and a well-posed initial value problem via the process of symplectic reduction. We analyse, synthesise, and contrast different approaches to the presentation and analysis of constrained Hamiltonian theories, drawing upon recent work on formalisation of nomic structure on model spaces (Gryb and Thébault 2024) and comparisons of theoretical structure and representational capacity via category theory (Bradley and Weatherall 2020; Bradley 2025b). We suggest that the case of irregular nomic structure is most naturally suited to a category theoretic presentation in which state spaces are arrows and symplectic reduction is arrow composition (Landsman 2005). Under this approach one obtains the natural results that theories with isomorphic state spaces are equivalent and theories whose reduced state spaces are isomorphic are equivalent at the level of the regular representations of their nomic structure. This analysis provides a suitable foundation for the case of quantization of theories with irregular nomic structure, which will be in a companion paper.

## Full Text

Nomic Structure and Reduction

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
- License: CC BY 4.0arXiv:2607.01289v1 [physics.hist-ph] 01 Jul 2026

## Nomic Structure and ReductionSean GrybUniversity of Groningens.b.gryb@rug.nlandKarim P. Y. ThébaultUniversity of Bristolkarim.thebault@bristol.ac.uk(Date:Draft of July 1, 2026.)

## Abstract.

The canonical formulation of physical theories withirregular nomic structureis as constrained Hamiltonian theories within which ill-posedness of the equations of motion is connected to aperniciousform of surplus representational capacity. Such theories can be converted into theories with regular nomic structure and a well-posed initial value problem via the process of symplectic reduction. We analyse, synthesise, and contrast different approaches to the presentation and analysis of constrained Hamiltonian theories, drawing upon recent work on formalisation of nomic structure on model spaces(Gryb and
Thébault2024)and comparisons of theoretical structure and representational capacity via category theory(Bradley and
Weatherall2020; Bradley2025b). We suggest that the case of irregular nomic structure is most naturally suited to a category theoretic presentation in whichstate spaces are arrowsandsymplectic reduction is arrow composition(Landsman2005). Under this approach one obtains the natural results that theories with isomorphic state spaces are equivalent and theories whose reduced state spaces are isomorphic are equivalent at the level of the regular representations of their nomic structure. This analysis provides a suitable foundation for the case of quantization of theories with irregular nomic structure, which will be in a companion paper.

## 
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

## 1.Introduction

The nomic structure of a physical theory is the structure which encodes the laws of that theory. In the context of representations of physical theories as model space we find nomic structure playing two fundamental and distinct roles. The first, and most basic, is as a partitioning function whereby the nomic structure indicates which models aremerely kinematically possibleand which models aredynamically possible. The second, equally important and yet often neglected, is a projection function whereby the nomic structure indicates which of the set of dynamically possible models can be understood as distinct and which equivalent. Significantly, the full specification of a dynamical equivalence principle will depend upon the representational context and will thus require physical as well as purely formal inputs cf.Belot (2013); Wallace (2019). However, crucially there are purely formal conditions under which we arerequiredto project out distinctions between at least some models according to some dynamical equivalence principle, else the nomic structure will not provide well-posed dynamical equations. In such cases we say that the nomic structure isirregular. In cases in which the relevant formal conditions do not obtain we say that the nomic structure isregular.

Significantly, the philosophical literature on theoretical structure, representation, and equivalence is largely confined to the regular case. In such contexts, an increasingly sophisticated account has been progressively developed in which the tools of category theory have been applied towards the diagnosis of inter-theory relations.111In what follows we will primarily follow the account provided inBradley and
Weatherall (2020). See alsoHalvorson (2012,2016); Weatherall (2019a,b); Nguyen
et al. (2020); Barrett (2022,2020); Dewar (2022); Feintzeig (2025); Bradley (2025b)and further canonical sources cited therein.The standard approach is to treat theories as categories with models as the objects and the morphisms are the isomorphisms of the theory. Conditions on functors between the theories, understood as categories, can then be applied towards the formal analysis of claims regarding, for example, theoretical equivalence or the existence of surplus structure. In a recent articleBradley (2025b)has broken new ground by extending the application of category theory as a tool to the analysis of the structure of a theory with irregular nomic structure. The particular virtues of her account are that it allows for both a clear articulation of the sense in which representation of theories with irregular nomic structure as constrained Hamiltonian theories includesurplus structureand provides tools to understand thesymplectic reductionprocess for converting irregular to regular nomic structure in terms of pair of functors between categories with models as the objects. The present article is intended as a complement to this important work both by supporting Bradley’s key conclusion regarding surplus structure via additional physical argumentation and in offering an alternative means of category theoretic presentation.

In the first regard, our particular goal is to present a number of formal and physical arguments that demonstrate the necessity of implementing dynamical equivalence principles in the context of irregular theories supporting. Our central concern will be the formal analysis of the initial value problem of classical mechanical theories and we will provide an overview of material relating to problems of ill-posedness in the context of the Euler-Lagrange equations, contained Hamiltonian theories, and first-order geometric velocity-phase space formalism. Our analysis will both provide a synthetic analysis of famous results due to Noether and Dirac, demonstrating the limitations of these approaches, and, crucially, articulate a more general and physically transparent set of diagnostic criteria that allow for the isolation of initial value constraints that indicate the existence of dynamical redundancy that generates ill-posedness.222This work builds on earlier analysis inGryb and
Thébault (2024)and is complemented by a more extensive treatment found inGryb and
Thébault (2026a).

In the second regard, our goal is to consider an alternative category theoretic presentation. In particular, we argue that the case of irregular nomic structure is most naturally suited to a category theoretic presentation in whichstate spaces are arrowsandsymplectic reduction is arrow composition(Landsman2005). Under this approach one obtains the natural results that theories with isomorphic state spaces are equivalent and theories whose reduced state spaces are isomorphic are equivalent at the level of the regular representations of their nomic structure. Furthermore, this analysis provides a suitable foundation for the case of quantization of theories with irregular nomic structure, which will be in a companion paper.

Our analysis will proceed according to the following plan. Section2is devoted to the abstract characterisation of theoretical structure and provides a constructive synthesis of a number of lines of existing work. We start by articulating the core ideas being the notions of nomic structure, dynamical distinctness, and irregularity following the account ofGryb and
Thébault (2024)and then proceed to present the core features of the standard category theory approach to theoretical structure followingBradley and
Weatherall (2020), before finally articulating an account of symmetry and structure that is implied by the intersection of these two approaches.

Section3then provides an analysis of irregular nomic structure starting from the Euler-Lagrange equations and proceeding through various articulations of the canonical analysis including the work ofBradley (2025b)and the famous results of Noether and Dirac. We provide a high-level overview of the novel results ofGryb and
Thébault (2024)andGryb and
Thébault (2026a)which resolve ambiguities in earlier work and result in a physically transparent set of diagnostic criteria for isolation of the dynamical redundancy that generates ill-posedness in terms of the existence of initial value constraints.

Finally, in Section4we consider various aspects formal and interpretative presentations framework of symplectic reduction with a focus on its role in the conversion of an irregular to regular nomic structure. We first recap the result ofBradley (2025b)under which the quotenting aspect of symplectic reduction can be rendered as a particular type of functorial relation between categories with models as objects. We then introduce the formal machinery needed to understand the alternative approach due toLandsman (2001,2005)which builds on earlier work byWeinstein (1983). In particular, we first introduce the crucial ideas of momentum maps and symplectic dual pairs. This then allows us to understand state spaces as arrows and symplectic reduction as arrow composition leading to the natural results mentioned above and, as set out in the short prospectus, a basis upon which one is able to articulate the formal tools and interpretational concepts needed to understand the quantization of theories with irregular nomic structure.

## 2.Theoretical Structure

## 2.1.Model Spaces

The notions ofconstitutive structureandnomic structureof a theory are based upon an approach in which theories are presented in terms of model spaces. Following the framework introduced byGryb and
Thébault (2024)we will apply the following definitions: Theconstitutive structureof a theory is the structure that one must assume in order to build the space,KK, ofkinematically possible models(KPM) of that theory. That is, the space which represents the basic ‘pre-nomic’ set of possibilities admitted by the theory. Each of these models can be thought of as something like a bare universe, stripped of laws and dynamics. Constitutive structures are often, although not aways, provided in terms of state space structures, used to characterize physical events, geometric or topological structures, used to characterize relations between the events, and matter structures, used to characterize particles or fields. Models with differenttokensof the sametypeof constitutive matter and geometric structure are typically constitutively distinct KPMs of the same theory. Thus, for example, two- and three- body particle models can be understood as having the distinct tokens of a common Newtonian constitutive structure.

The token-type distinction allows us to distinguish between the following two cases. First we have structure common between all KPMs which share the sametypeof structure. Such structure isconstitutively fixed. Constants of nature can typically be understood as an example of constitutively fixed structures of a theory. Second we have structure that is common between all KPMs which share the sametokenof structure but which varies between at least two distinct tokens of the same type of constitutive structure. Such structure iscontingently fixed. Constants of motion can typically be understood as an example of contingently fixed structures of a theory. This distinction allows for differentiation between the modal status of two different types of structure. That is, structure that is the same in all KPMs of the same model type, and structure that can vary between kinematically possible models that instantiate different tokens of that type. It is worth noting that with regard to KPMs, the framework we are using takes a form similar to that used to characterize the model space of a physical theory by, for example,Pooley (2017). This approach is articulated in terms of a specification of the space of KPMs together with a set of solution-independent ‘fixed’ (or ‘non-dynamical’) fields common to all KPMs, and a set of ‘non-fixed’ (or ‘dynamical’) fields not common between all KPMs. Constitutively fixed in our sense thus coincides with fixed in the sense ofPooley (2017).

Nomic structure is then the structure of a theory that represents the laws of that particular theory. Nomic structure has two important and distinct functions. The first function is topartitionthe space of KPMs: that is, to tell us which models are dynamically possible and which are not dynamically possible. We can represent this function partitioning of the space of KPMs into the proper sub-space of dynamically possible models, or DPMs,D⊂KD\subset K. The second function is to provide us with an equivalence relation between DPMs. The equivalence relation function provides a methodology for determining which DPMs are dynamically distinct and which are dynamically identical. The relevant notion of distinctness and identity is here a nomic one rather than an ontic one; that is, a distinction based upon a difference that the laws pick out between two models and not a distinction that is necessarily equivalent to a strong metaphysical notion of distinctness and identity.

We can represent the equivalence relation function of nomic structure in terms of aProjection Map,πN\pi_{N}. We will provide a more formal definition of the map later but the important point for our purposes is that the map is such that it removes distinctions between models according to some dynamical equivalence principle. We can designate the space of equivalence classesD~\tilde{D}ofDDthe space of Distinct Dynamically Possible Models (DDPMs); this allows us to consider the projection from the space of DPMs to the space of DDPMs:πN:D→D~\pi_{N}:D\to\tilde{D}. The role of the nomic structure can be given a schematic representation as per Fig.1where we have introduced the terminology of a ‘fibre’ for the equivalence class of DPMs.Figure 1.Schematic representation of the nomic structure.DDis the partition of dynamically possible models. The dotted lines are ‘fibres’ that represent dynamically equivalent models which the projection map,πN\pi_{N}, maps into single points in the space of distinct dynamically possible models,D~\tilde{D}.

Significantly, the full specification of a dynamical equivalence principle will depend upon the representational context and will thus require physical as well as purely formal inputs cf.Belot (2013); Wallace (2019). However, crucially, as discussed in(Gryb and
Thébault2024, 5.3)and elaborated below, there are purely formal conditions under which we arerequiredto project out distinctions between at least some models according to some dynamical equivalence principle, else the nomic structure will not provide well-posed dynamical equations. In such cases ofirregular nomic structurethe projection mapcannotbe treated as the identity and at least some DPMsmustbe treated as dynamically equivalent. It ismandatoryto apply a non-trivial criterion of dynamical equivalence precisely because the DPMs in question do not correspond to independently well-posed solutions of the equations of motion and implementing a non-trivial projection is asine qua nonof a non-pathological specification of nomic structure.

The contrast case is that ofregular nomic structure. In such theories the projection mapmaybe treated as the identity and we have that all DPMsmaybe treated as distinct (i.e.D=D~,πN:D→DD=\tilde{D},\pi_{N}:D\to D). Identification of dynamical equivalence requires physical or interpretative input. For example, in Newtonian particle mechanics there are good physical reasons coming from the variational principle to take DPMs related by rigid, time independent coordinate transformations to be dynamically equivalent and thus implement a non-trivial projectionπN:D→D~\pi_{N}:D\to\tilde{D}where the fibres are ISO(3) transformations(Gryb and
Thébault2024, 6.5). There is, however, nothing formally inconsistent in taking such ‘Leibniz shifted’ DPMs as dynamically distinct since they correspond to independently well-posed solutions of the equations of motion.

Crucially, the difference in the interpretation of regular and irregular theories maps onto a formal difference in both the canonical representation and the admissible quantization procedures relevant to regular and irregular classical theories of mechanics. It is thus much more than amerely philosophicaldistinction. One main aim of this paper is to explicate the structure of theories with irregular nomic structure by application of ideas from the literature of category theory and theoretical structure. We review some of these ideas in the following sub-sections. Section3is then devoted to considering the formal analysis of classical theories with irregular nomic structure represented as constrained Hamiltonian theories with a particular focus on the problem of ill-posed initial value problems.

## 2.2.Theories as Caterogies

Let us define a category𝒞\mathcal{C}as a collection ofobjectsand a collection ofmorphismsorarrows(we will use the two terms interchangeably), each with a source and target object. The morphisms or arrows in question will typically be invertible and thus isomorphisms in the applications we will consider. We denote a morphism byf:A→Bf:A\to Bwith the sourceAAand targetBB. The collection of morphisms with sourceAAand targetBBin the category𝒞\mathcal{C}is called the hom-set betweenAAandBBand is denotedHom𝒞​(A,B)\mathrm{Hom}_{\mathcal{C}}(A,B). A category comes equipped with an operation of composition for morphisms, denoted∘\circ, which is total, associative and such that for each objectAAthere is a unique identity morphism1A1_{A}whose composition with other morphisms leaves them unchanged. Thus we have a category𝒞\mathcal{C}, objects(A,B)(A,B)and morphismsf,g∈Hom𝒞​(A,B)f,g\in\mathrm{Hom}_{\mathcal{C}}(A,B)such that:f:A→B,g:B→C,f∘g=h:A→Cf:A\to B,g:B\to C,f\circ g=h:A\to C. We can then define afunctorF:𝒞→𝒟F:\mathcal{C}\to\mathcal{D}between two categories𝒞\mathcal{C}and𝒟\mathcal{D}in terms of a pair of maps: one map between the objects of𝒞\mathcal{C}and the objects of𝒟\mathcal{D}and another map between the morphisms of𝒞\mathcal{C}and the morphisms of𝒟\mathcal{D}. By definition a functor preserves sources and targets and arrow composition. We can thus consider a second category𝒟\mathcal{D}as being given by the objects(F​(A),F​(B))(F(A),F(B))and morphismsF​(f),F​(g)∈Hom𝒟​(F​(A),F​(B))F(f),F(g)\in\mathrm{Hom}_{\mathcal{D}}(F(A),F(B)). The definition of functor just given encodes the important requirement that the map between categories it induces must betotal. That is, there must be no objects or arrows in𝒞\mathcal{C}which are not mapped to at least one object or arrow in𝒟\mathcal{D}.

Category theory has been applied in the context of theoretical structure because it is well-suited for the analysis of formal relations between theories. In particular, if one treats theories as collections of models together with a set of structure-preserving maps between the models (i.e. the morphisms are the isomorphisms of the theory) then it is natural to identify theories with categories and inter-theory relations (so longs as they are total) as functors. The idea is then that by characterising theories as categories we gain access to precisely the formal tools needed to enact comparisons between theories in terms of various ‘levels’ of structure. Most relevant for comparison between physical theories are three cases that we will labelequivalence,surplus structure, andsurplus representational capacity.333Here we are slightly modifying the terminology ofBradley and
Weatherall (2020); Bradley (2025b)who initially, followingBaez and
Shulman (2009), talk about the third case in terms of ‘stuff’ but then later provide an interpretation in terms of ‘representational freedom’.These notions are always to be understood as relations between two categories relative to a functor from the first to the second. The three cases correspond to distinct property sets of the functor. The properties are as follows. Consider a functorF:𝒞→𝒟F:\mathcal{C}\to\mathcal{D}:
- •

FFisfaithfulif for anyf,g:A→Bf,g:A\to Bin𝒞\mathcal{C}, wheneverF​(f)=F​(g)F(f)=F(g), it is also the case thatf=gf=g; that is,FFis injective fromHom𝒞​(A,B)\mathrm{Hom}_{\mathcal{C}}(A,B)toHom𝒟​(F​(A),F​(B))\mathrm{Hom}_{\mathcal{D}}(F(A),F(B)).
- •

FFisfullif for every morphismg:F​(A)→F​(B)g:F(A)\to F(B)in𝒟\mathcal{D}, there
is some morphismf:A→Bf:A\to Bin𝒞\mathcal{C}such thatF​(f)=gF(f)=g; that is,FFis
surjective fromHom𝒞​(A,B)\mathrm{Hom}_{\mathcal{C}}(A,B)toHom𝒟​(F​(A),F​(B))\mathrm{Hom}_{\mathcal{D}}(F(A),F(B)).
- •

FFisessentially surjectiveif for every objectBBin𝒟\mathcal{D}, there is some objectAAin𝒞\mathcal{C}such thatF​AFAis isomorphic toBBin𝒟\mathcal{D}.

If a functor is full and faithful then the morphisms are in one-to-one correspondence. If a functor is essentially surjective we can match objects (up to isomorphism). Thus, the existence of a functor that is full, faithful and essentially surjective is a natural condition for us to understand to categories as equivalent.

FollowingBradley and
Weatherall (2020), in the context of physical theories characterised as categories, equivalence in this sense can be understood in terms of the relevant functor preservingbothstructure and representational capacity. We can see this as follows: First, assume, as we indicated earlier, that the morphisms are isomorphisms. It is then natural to understand the amount of structure that a theory contains as indicated by the size of the isomorphism class. Since isomorphisms are structure preserving maps the fewer isomorphisms the more structure. By definition, if two theories are related by a functor that is full then there is a surjection between the is isomorphisms of the first theory and the isomorphisms of the second. This means that the second theory must have at least as much structure as the first.

Second, consider the subclass of isomorphisms that map a model to itself. That is, the automorphisms of the objects. These can further be split into the trivial automorphisms given by the identity element and the non-trivial automorphisms given by the class of transformations identified as non-trivial symmetries of the models. A theory with non-trivial automorphisms provides us with a means to represent the same things using different models. Hence, given that we can match objects up to isomorphism, i.e. the functor is essentially surjective, the size of the non-trivial automorphism class corresponds to a theory’s representational capacity. By definition, if theories are related by a functor that is faithful we know that the non-trivial automorphisms of the first must map into non-trivial automorphisms of the second. Given that the two theories are related by the a functor that is also essentially surjective then we can understand the theories to have identical representational capacity. Thus a functor between two theories that is full, faithful, and essentially surjective will preserve both structure and representational capacity.

We can then straightforwardly distinguish the two further cases by weakening the conditions on the functor in two directions. Consider a functor that is faithful and essentially surjective but not full. This functor will preserve representational capacity but forget structure. That is, there will be some isomorphisms of the second theory that are not mapped to by any isomorphisms of first. Since a theory with more isomorphisms has less structure we can then understand the functor as forgetting structure. Then consider a functor that is full and essentially surjective but not faithful. The particular case that is important for our purposes is when we find that trivial automorphisms of the second theory that are mapped to by non-trivial automorphisms of first. This means that whereas the first theory will have the capacity to represent the same situation via at least two non-trivially related models, the second will only have a single model to represent the counterpart situation. Thus, the functor forgets representational capacity. We will consider an example of each of these types of forgetful functors in the context of symplectic reduction later following the account of following the account ofBradley (2025b).
The three cases are summarised in the Table1.Table 1.Functorial relations between theories and their interpretive significanceFaithfulFullEssentiallySurjectiveInterpretationTheories𝒞\mathcal{C}and𝒟\mathcal{D}areEquivalentrelative to functorF:𝒞→𝒟F:\mathcal{C}\to\mathcal{D}.✓\checkmark✓\checkmark✓\checkmarkIsomorphisms and objects (up to isomorphism) are in one-to-one correspondence between𝒞\mathcal{C}and𝒟\mathcal{D}.Theory𝒞\mathcal{C}hasSurplus Structurecompared with theory𝒟\mathcal{D}relative to functorF:𝒞→𝒟F:\mathcal{C}\to\mathcal{D}.✓\checkmark×\times✓\checkmarkThere are some isomorphisms of𝒟\mathcal{D}that are not mapped to by any isomorphisms of𝒞\mathcal{C}.Theory𝒞\mathcal{C}hasSurplus Representational Capacitycompared with theory𝒟\mathcal{D}relative to functorF:𝒞→𝒟F:\mathcal{C}\to\mathcal{D}×\times✓\checkmark✓\checkmarkThere are trivial automorphisms of the second theory that are mapped to by non-trivial automorphisms of the first.

## 2.3.Symmetry and Invariance

Our next goal is to provide a more formal representation of nomic structure together with a language for describing how other theoretical structures vary with respect to this structure. We can do this by introducing theNomic-AIR Formalismformalism developed in detail in(Gryb and
Thébault2024, §9). We will then relate this formalism to the category theoretic presentation of theoretical structure just given.

In our earlier largely informal discussion we set out in qualitative terms how one can understand nomic structures as providing us with apartitioning mapand aprojection map. In more formal terms, these maps can be explicitly defined as follows:

## Definition 1.

Partitioning Map,nn, is nomic structure that partitions the space,KK, of KPMs into the proper subspace,D⊂KD\subset K, of DPMs and the subspace,¬D\neg D, of non-DPMs such thatK=D∪¬DK=D\cup\neg D. In general, such structure can be represented as a non-injective map(1)n:K→D.n:K\to D\,.

The assumption that the map is non-injective is to ensure that unless the laws impose no constraints on the kinematical possibilities, there will be at least one KPM that is not a DPM.

## Definition 2.

TheProjection Map,πN\pi_{N}can be defined in four steps:
- i.

First, consider the functione:D→ℝe:D\to\mathbbm{R}such that two elementsx,y∈Dx,y\in Daredynamically equivalent,x∼yx\sim y, iffe​(x)=e​(y)e(x)=e(y), where∼\simis the dynamical equivalence relation.
- ii.

Second, use this equivalence relation to define thedynamical equivalence classes[x]={y|y∼x,∀y∈D}[x]=\{y\,|\,y\sim x,\,\forall y\in D\}.
- iii.

Third, designate the space of equivalence classesD~\tilde{D}ofDDthe space ofDistinct Dynamically Possible Models (DDPMs).
- iv.

Finally we can consider the projection from the space of DPMs to the space of DDPMs:(2)πN:D→D~.\pi_{N}:D\to\tilde{D}\,.

The projection map will necessarily be a surjective function since for every element ofD~\tilde{D}we will have thatπN​(D)\pi_{N}(D)is well-defined. When it is non-trivial it will also be non-injective since it will categorize at least two models as dynamically equivalent. An important special case is when the members of the equivalence class produced by∼\simare related by a group action. Here,eegivesDDa principal fibre bundle structure for the corresponding group, whereπN\pi_{N}is the bundle projection,[x][x]are the bundle’s fibres, andD~\tilde{D}is the base space. This is precisely the case that we will consider in the context of symplectic reduction later.

Now assume thenon-constitutivestructures (i.e. nomic, spatiotemporal or other) of a theory to be represented by a map with the domain a space,UU, and the codomain a space,VV, so that we have𝒮:U→V\mathcal{S}:U\rightarrow Vor equivalently𝒮​(u)=v\mathcal{S}(u)=vforv∈Vv\in Vandu∈Uu\in U. Let us then consider endomorphisms on the space of DPMs that is transformationsϕ:D→D\phi:D\to Dor equivalentlyd′=ϕ​(d)d^{\prime}=\phi(d)ford,d′∈Dd,d^{\prime}\in D. We can then consider thepullback of a structure by an endomorphism, that is we can define the precomposition map as followsϕd∗​𝒮\phi_{d}^{*}\mathcal{S}by transferring the action of a particular endomorphismsϕi\phi_{i}to a particular structure𝒮a\mathcal{S}_{a}by pre-applying it to the latter’s domain:ϕd∗​𝒮=𝒮∘ϕd=𝒮​(ϕ​(d))\phi_{d}^{*}\mathcal{S}=\mathcal{S}\circ\phi_{d}=\mathcal{S}(\phi(d)). Consider for a theory a theory,𝒯\mathcal{T}the space of transformations,Ψ\Psi, given by the endomorphismsψi\psi_{i}ofKK:(3)Ψ={ψi,∀i|ψi:K→K}.\Psi=\{\psi_{i},\,\forall i\,|\,\psi_{i}:K\to K\}\,.

Assume that𝒯\mathcal{T}is further equipped with nomic structureNNplaying the role of a partitioning functionn:K→Dn:K\to D. The space of transformations,Φ\Phi, is the space of all endomorphismsϕi\phi_{i}ofDD:(4)Φ={ϕi,∀i|ϕi:D→D}.\Phi=\{\phi_{i},\,\forall i\,|\,\phi_{i}:D\to D\}\,.

The spaceΦ\Phiis partitioned into three non-overlapping subspaces,Abs​(𝒮)\text{Abs}(\mathcal{S}),Rel​(𝒮)\text{Rel}(\mathcal{S}), andInc​(𝒮)\text{Inc}(\mathcal{S}), which we define as follows:

## Definition 3.

Absolute Subspace:Abs​(𝒮)\text{Abs}(\mathcal{S}): the subspace of allϕi∈Φ\phi_{i}\in\Phisuch that the pullback of the structure underϕi\phi_{i}is trivial for all tokens of the structure:ϕi∗​𝒮a=𝒮a,∀a\phi_{i}^{*}\mathcal{S}_{a}=\mathcal{S}_{a},\forall a. Such structure𝒮\mathcal{S}transformsinvariantly, and is in this sense isabsoluteunderϕi\phi_{i}.

## Definition 4.

Relative Subspace:Rel​(𝒮)\text{Rel}(\mathcal{S}): the subspace ofϕi∈Φ\phi_{i}\in\Phisuch that the pullback of the structure underϕi\phi_{i}is well-defined and non-trivial:ϕi∗​𝒮a=𝒮b\phi_{i}^{*}\mathcal{S}_{a}=\mathcal{S}_{b}, for somea≠ba\neq b. Such structure𝒮\mathcal{S}transformscovariantly, and in this sense isrelativeunderϕi\phi_{i}.

## Definition 5.

Incomplete Subspace:Inc​(𝒮)\text{Inc}(\mathcal{S}): the subspace ofϕi∈Φ\phi_{i}\in\Phisuch that the pullback of the structure underϕi\phi_{i}does not have a closed action on the tokens of the structure: there exists at least one𝒮a\mathcal{S}_{a}s.t.ϕi∗​𝒮a≠𝒮b,∀b\phi_{i}^{*}\mathcal{S}_{a}\neq\mathcal{S}_{b},\forall b. Since it is not closed under the action ofϕi\phi_{i}, such structure𝒮\mathcal{S}does not transform in an appropriately well-behaved way, and in this sense isincompleteunderϕi\phi_{i}.

We assume that the the Absolute-Incomplete-Relative (AIR) regions are non-overlapping (i.e. mutually exclusive), that the union of the three AIR regions must beΦ\Phiitself, and that the identity𝟙\mathbbm{1}is an element ofAbs​(𝒮)\text{Abs}(\mathcal{S}). It is then possible to prove that each AIR region can be defined via the complement of the other two(Gryb and
Thébault2024, Theorem 9.1). Furthermore, we can then introduce the following three further definitions:

## Definition 6.

Fixed Structure. The collection of all structures for some theory theory𝒯\mathcal{T}, for which the relative subspace ofΦ\Phiis empty:Rel​(𝒮)=∅.\text{Rel}(\mathcal{S})=\emptyset.

## Definition 7.

Abs​(πN)\text{Abs}(\pi_{N}):Symmetry transformations.The subspace of allϕi∈Φ\phi_{i}\in\Phisuch that the pullback ofπN\pi_{N}underϕi\phi_{i}is trivial:ϕi∗​πN=πN′=πN\phi_{i}^{*}\pi_{N}=\pi^{\prime}_{N}=\pi_{N}. Such transformations necessarily leave the spaceD~\tilde{D}of DDPMs invariant. These are naturally interpreted as symmetry transformations of the theory.

## Definition 8.

Rel​(πN)\text{Rel}(\pi_{N}):Dynamical transformations.The subspace of allϕi∈Φ\phi_{i}\in\Phisuch that the pullback ofπN\pi_{N}underϕi\phi_{i}is well-defined and non-trivial:ϕi∗​πN=πN′≠πN\phi_{i}^{*}\pi_{N}=\pi^{\prime}_{N}\neq\pi_{N}. The transformations in this region induce diffeomorphisms ofD~\tilde{D}that transform between DDPMs. These are naturally interpreted as the dynamical transformations of the theory.

An important special case is when the equivalence classes ofDDare identical manifoldsℱ\mathcal{F}so that the projectionπN\pi_{N}equipsDDwith a fibre bundle structure. In this case the symmetry transformationsϕv∈Abs​(πN)\phi_{v}\in\text{Abs}(\pi_{N})are the vertical directions in the bundle and the dynamical transformationsϕh∈Rel​(πN)\phi_{h}\in\text{Rel}(\pi_{N})are the horizontal directions. As already noted, fixed in our sense is a weaker requirement than that in the sense ofPooley (2017)since it places no requirement on invariance of structures across KPMs. Rather, fixed in our sense is essentially identical to idea of a ‘absolute field’ introduced in(Read2024, Def. 8).

These ingredients are sufficient to provide a precisification of the standard notions of invariant structure and surplus structure via respective behaviour under symmetry transformations. AnInvariant Structureis absolute (and therefore invariant) under all symmetries of𝒯:Abs​(𝒮)⊇Abs​(πN)\mathcal{T}:\text{Abs}(\mathcal{S})\supseteq\text{Abs}(\pi_{N})andSurplus Structure:𝒮\mathcal{S}transforms in a well-behaved manner undersomeof the symmetries of𝒯:Rel​(𝒮)∩Abs​(πN)≠∅\mathcal{T}:\text{Rel}(\mathcal{S})\cap\text{Abs}(\pi_{N})\neq\emptyset. Correspondingly, we can also provide a precisification of the notions of a structure that is absolute or relative via respective behaviour under dynamical transformations. ADynamically Absolute Structuredoes not vary under some transformations between DDPMs and when𝒮\mathcal{S}has non-trivial relative transformations, these are always symmetry transformations. Such structurenevertransforms as one varies between DDPMs (see(Gryb and
Thébault2024, Def. 9.18)for formalisation). ADynamically Relative Structure:𝒮\mathcal{S}transforms as one varies between some DDPMs:Rel​(𝒮)∩Rel​(πN)≠∅\text{Rel}(\mathcal{S})\cap\text{Rel}(\pi_{N})\neq\emptyset. It is then straightforward to prove that invariant structures and surplus structures are mutually exclusive(Gryb and
Thébault2024, Theorem. 9.3), dynamically absolute and dynamically relative structure are mutually exclusive(Gryb and
Thébault2024, Theorem. 9.4), invariant structure that is dynamically absolute is always fixed structure(Gryb and
Thébault2024, Theorem. 9.7)and when a structure is both surplus and dynamically absolute then all relative transformations of the structure will be symmetry transformations(Gryb and
Thébault2024, Theorem. 9.8).

## 2.4.State Spaces as Objects

We can now turn the project of relating this formalism to that in terms of category theory provided earlier. The most basic ambiguity in relating the two presentations is the identification one draws between the ‘models’ that are the objects within the categories and the sets of kinematically and dynamically possible models that are picked out by the constitutive and nomic structures. Practice is not entirely consistent since in the context of spacetime theories it is standard to take both the models qua category theory objects and the models qua DPMs to correspond to spacetimes. For example, general relativity might be understood as the category defined by specifying Lorentzian manifolds (together with a suitable set of functions on them) as objects and isometries as morphisms. The nomic structure of the theory is then given by the Einstein field equations which pick out pairings of metric and stress energy tensors as the DPMs whicharethe Lorentzian manifolds in question.

By contrast, in the context of theories in initial value formulation, it is standard to take the models qua category theory objects as entire state spaces with the models qua DPMs as state space curves. For example, Hamiltonian mechanics might be understood as the category defined by specifying symplectic manifolds (together with a suitable set of functions on them) as objects and symplectomorphisms as morphisms. By contrast, the nomic structure is given by Hamilton’s equations which, for a regular theory, pick out a unique Hamilton vector field the integral curves of which are the DPMs. This dual use of the term model creates no inherent problem so long as we keep track of what we are talking about when we talk about the ‘models’ or ‘structure’ of a theory. In particular, it is natural to understand the objects in a category theoretic formulation of an initial value theory asstate spacescontaining the DPMs for specific tokens of constitutive and nomic structure. Thus in specifying tokens of the constitutive and nomic structure we are specifying the objects of the salient category.

The immediate implication is then that we can interpret the symmetry transformations as the morphisms of the category. That is, since these are precisely the maps that preserve the token of the nomic structure they will leave both the state spaces andD~\tilde{D}invariant. For the case at hand they will be invertible and thus isomorphisms. Let us indicate this identification via a compressed notation where the objects are indicated by triples⟨K,πn,𝒮⟩\langle K,\pi_{n},\mathcal{S}\rangle, understood given by tokens of the constitutive and nomic structure together with some further set of structures (e.g. matter or geometric structure) and the isomorphisms byAbs​(πN)\text{Abs}(\pi_{N})as per our definitions above. We can then consider functors between categories as corresponding to maps between: i) the same tokens of constitutive and nomic structure but different tokens of some further set of structures, e.g. solutions of a 3-body Newtonian model with different initial positions; ii) different tokens of constitutive, nomic structure, further structure, e.g. 2-body and 3-body Newtonian models, each for specific initial positions; or iii) tokens ofdifferentconstitutive and nomic structure and further structure e.g. classical and quantum mechanics Harmonic oscillators.

The intersection between these two presentations is a rich terrain that provides a powerful toolkit to disambiguate various philosophical and mathematical issues in the interpretation of physical theory. A straightforward and fruitful task is to translate the notions of equivalence, surplus structure, and surplus representational capacity defined above into the Nomic-AIR terminology. We will do this by considering their meaning in the context of a functor that maps between the categories as we have just defined them. In particular, consider a first category𝒞\mathcal{C}as given by objectsAi=⟨K1,πn1,𝒮1⟩A^{i}=\langle K^{1},\pi^{1}_{n},\mathcal{S}^{1}\rangle,B=⟨K2,πN1,𝒮1⟩B=\langle K^{2},\pi^{1}_{N},\mathcal{S}^{1}\rangleand isomorphismsAbs​(πNi)\text{Abs}(\pi^{i}_{N}), whereiiruns over all the tokens or types in question. We can then define a functorF:𝒞→𝒟F:\mathcal{C}\rightarrow\mathcal{D}to a second category𝒟\mathcal{D}with objectsF​(A)=⟨F​(K1),F​(πNi),F​(𝒮1)⟩F(A)=\langle F(K^{1}),F(\pi^{i}_{N}),F(\mathcal{S}^{1})\rangle,F​(B)=⟨F​(K2),F​(πN2),F​(𝒮2)⟩F(B)=\langle F(K^{2}),F(\pi^{2}_{N}),F(\mathcal{S}^{2})\rangleand isomorphismsAbs(F(πNi)))\text{Abs}(F(\pi^{i}_{N}))).

It is then straightforward to interpret the three functional relations. Essential surjectivity holds in all three cases and indicates that we can match objects (up to isomorphism) between the two categories. In our case the objects are families of DPMs for specific tokens of constitutive and nomic structure together with further additional structures such as matter structure. Equivalence then means that the functor is also full and faithful which means that we can match the isomorphisms as well. In our case the isomorphisms are symmetry transformations. Thus equivalence between two theories indicates that for every family of DPMs together with associated constitutive and nomic structure together with further additional structures and symmetries in𝒞\mathcal{C}, there is a corresponding family of DPMs together with associated constitutive and nomic structure together with further additional structures and symmetries in𝒟\mathcal{D}.

Surplus structure is the case in which the functor is not full and thus there are some some isomorphisms of𝒟\mathcal{D}that are not mapped to by any isomorphisms of𝒞\mathcal{C}. This means that there are symmetries of𝒟\mathcal{D}that are not symmetries of𝒞\mathcal{C}and thus the space of DDPMs in𝒟\mathcal{D}will be strictly smaller than the space of DDPMs in𝒞\mathcal{C}. The most important example of such a functor is given by specifying the structures of some theory with some symmetry class and then constructing a new theory based on the first by enlarging the symmetry class. Such enlargement may be merely by stipulation under some symmetry principle, such as all DPMs related by variational symmetries are DDPMs, without changing the nomic structure of a theory. One might also consider cases where we explicitly change the nomic structure to build in more symmetry, such as for instance in moving from Newtonian mechanics to Barbour-Bertotti theory(Barbour and
Bertotti1982). In canonical terms such a move corresponds precisely to enlarging the symmetry class by moving from a regular to an irregular representation of nomic structure, see(Gryb and
Thébault2024, p.168).

Finally, we can consider the case of surplus representational capacity. This corresponds to the functor being full and essentially surjective but not faithful. The most important case for our purposes is when there are trivial automorphisms of𝒟\mathcal{D}that are mapped to by non-trivial automorphisms𝒞\mathcal{C}. Such a functor is given by considering a theory and projecting out symmetries by moving to a reduced space of DPMs. This is removing representational capacity by redefining the space of DPMs such that distinct symmetry related DPMs in𝒞\mathcal{C}get mapped to the same DPM in𝒟\mathcal{D}. The most extreme example of such a symmetry reduction would be when the absolute subspace of the projection map of the nomic structure consists solely of the identity element(Gryb and
Thébault2024, p.155). Such a ‘categorical’ theory would havenosurplus representational capacity since there would be only one dynamically distinct model . These relationships are summarised Table2.Table 2.Functorial relations between theories in Nomic-AIR formalism.FaithfulFullEssentiallySurjectiveInterpretationTheories𝒞\mathcal{C}and𝒟\mathcal{D}areEquivalentrelative to functorF:𝒞→𝒟F:\mathcal{C}\to\mathcal{D}.✓\checkmark✓\checkmark✓\checkmarkFor every family of DPMs together with associated constitutive and nomic structure together with further additional structures and symmetries in𝒞\mathcal{C}, there is a corresponding family of DPMs together with associated constitutive and nomic structure together with further additional structures and symmetries in𝒟\mathcal{D}.Theory𝒞\mathcal{C}hasSurplus Structurecompared with theory𝒟\mathcal{D}relative to functorF:𝒞→𝒟F:\mathcal{C}\to\mathcal{D}.✓\checkmark×\times✓\checkmarkThere are symmetries of𝒟\mathcal{D}that are not symmetries of𝒞\mathcal{C}and thus the space of DDPMs in𝒟\mathcal{D}will be strictly smaller than the space of DDPMs in𝒞\mathcal{C}Theory𝒞\mathcal{C}hasSurplus Representational Capacitycompared with theory𝒟\mathcal{D}relative to functorF:𝒞→𝒟F:\mathcal{C}\to\mathcal{D}×\times✓\checkmark✓\checkmarkThere are non-trivial automorphisms in𝒞\mathcal{C}which get mapped to the identity in𝒟\mathcal{D}and thus there are distinct symmetry related DPMs in𝒞\mathcal{C}which get mapped to the same DPM in𝒟\mathcal{D}.

## 3.Irregularity and Ill-posedness

The distinction between the cases of regular and irregular nomic structure is important in the context of both classical and quantum theories. The relevant criterion is more straightforward to identify in the classical context where it can be directly connected to the well-posedness of the evolution equations. In the context of Lagrangian action principles this is a distinction which can be drawn betweenregular Lagrangiansand the class ofirregular Lagrangians with initial value constraints. This distinction in turn maps onto that between unconstrained and constrained Hamiltonian theories with the important exception of totally constrained systems, which in general haveirregular Lagrangians without initial value constraintscf.(Gryb and
Thébault2024, §11). In this section we will provide an interpretative overview of irregular nomic structure focusing on the connection between irregularity and Hamiltonian constraints, Dirac’s Theorem which connects Hamiltonian constraints to redundancy, and the geometric conditions for an irregular Lagrangian to be associated with initial value constraints via distinction between transverse and tangential orientation of the irregular variations. We will make reference to some the ideas from the previous section where relevant as the next step in our synthetic project. For further details and the explicit examples see(Gryb and
Thébault2024, §7-8).444See alsoSudarshan and
Mukunda (1974); Sundermeyer (1982); Henneaux and
Teitelboim (1992); Díaz
et al. (2014); Diaz and
Montesinos (2018); Díez et al. (2020). See alsoDirac (1958,1964). SeeSalisbury and
Sundermeyer (2017)for historical analysis highlighting the role of Léon Rosenfeld.

## 3.1.Regular and Irregular Nomic Structure

Let first review some standard but important formal material that establishes the connection between irregular Lagrangians and Hamiltonian constraints. Consider a finite dimensional system with action:(5)I=∫t1t2d​t​L​(qi,q˙i,t)I=\int_{t_{1}}^{t_{2}}\text{d}t\,L(q^{i},\dot{q}^{i},t)

where the indexi=1,…,Ni=1,...,Nruns over the degrees of freedom of the system and write the Euler–Lagrange equations in the form:(6)αi​(q,q˙,t):=∂L∂qi−∂∂t​∂L∂q˙i=Wi​j​(q,q˙)​q¨j−Ki=0\alpha_{i}(q,\dot{q},t):=\frac{\partial L}{\partial q^{i}}-\frac{\partial}{\partial t}\frac{\partial L}{\partial\dot{q}^{i}}=W_{ij}(q,\dot{q})\ddot{q}^{j}-K_{i}=0

whereαi\alpha_{i}is the Euler–Lagrange operator,Wi​jW_{ij}is the Hessian matrix:(7)Wi​j=∂2L∂q˙i​∂q˙jW_{ij}=\frac{\partial^{2}L}{\partial\dot{q}^{i}\partial\dot{q}^{j}}

and(8)Ki=∂L∂qi−∂2L∂q˙i​∂qj​q˙j.K_{i}=\frac{\partial L}{\partial q^{i}}-\frac{\partial^{2}L}{\partial\dot{q}^{i}\partial q^{j}}\dot{q}^{j}\,.

Writing the Euler–Lagrange equations in this form makes clear that the accelerationsat any particular timeare uniquely determined by the velocitiesat that timeif and only if the Hessian can be inverted. This is equivalent to the condition that the determinate of the absolute value of the Hessian is non-zero.
We define aregularLagrangian as a Lagrangian that leads to Euler–Lagrange equations that can be uniquely determined in terms of the initial configurations and velocities, and therefore satisfiesdet​|Wi​j|≠0\text{det}\lvert W_{ij}\rvert\neq 0. This implies that the Euler–Lagrange equations are autonomous, integrable and of second-order. Furthermore, if the Lagrangian is regular then we are guaranteed by the inverse function theorem that there exists a one-to-one transformation between the configuration-velocity variables(q,q˙,t)(q,\dot{q},t)and the configuration-momentum variables(q,p,t)(q,p,t). This, in turn, means that the coordinates and momenta are independent variables(Sundermeyer1982, p. 11). Systems with regular Lagrangians have regular nomic structure in the sense that the equations of motion, both the second-order Euler–Lagrange equations and the first-order Hamiltonian equations, will be well-posed for all degrees of freedom.

Theories with regular nomic structure are thus precisely those unconstrained Hamiltonian theories which the transformation to the phase space variables is guaranteed to be unique and the coordinates and momenta will then be independent variables. Following our discussion of theoretical structure in the previous section, for unconstrained Hamiltonian theories it is natural to understand the models as being picked out by a triple⟨Γ,𝒜,ω,⟩\langle\Gamma,\mathcal{A},\omega,\rangleconsisting of the even-dimensional symplectic manifoldΓ\Gamma, the Poisson algebra𝒜\mathcal{A}of smooth, real functions onΓ\Gamma, and the symplectic two-form that equips both the manifold and algebra with the salient geometric and algebraic structures. Models defined via these structures are sufficient to determine (regular) nomic structure via Hamilton’s equations since they allow us to define for any observable quantity and Hamiltonian function,A,H∈𝒜A,H\in\mathcal{A}, time evolution automorphism via the Poisson bracket,A˙={A,H}:=ω​(XA,XH)\dot{A}=\{A,H\}:=\omega(X_{A},X_{H})whereXAX_{A}andXHX_{H}are the Hamilton vector fields induced by the symplectic structure on phase space viaιXA​ω=d​A\iota_{X_{A}}\omega=dAwhich is guaranteed to always have unique solutions sinceω\omegais non-degenerate. This is the hallmark of a Hamiltonian theory with regular nomic structure: Hamilton’s equations encode the nomic structure and pick out a unique set of internal curves on phase space as the DPMs. The isomorphisms are then given by diffemophisms whose push forward preserves both the symplectic and Poisson algebra structure. These are thesymplectomorphismϕ\phiwhich are by definition such thatϕ∗​ω′=ω\phi^{*}\omega^{\prime}=\omegaand will also be guaranteed to be such thatϕ∗​𝒜→𝒜\phi^{*}\mathcal{A}\rightarrow\mathcal{A}.

Let us then define anirregular(orsingular) Lagrangian as a Lagrangian for whichdet​|Wi​j|=0\text{det}\lvert W_{ij}\rvert=0. This implies that at least some of the components,q¨i\ddot{q}^{i}, of acceleration at a given time cannot be solved uniquely in terms of the configuration and velocity variables at that time(Sundermeyer1982, p. 39). We can represent the breakdown of integrability via the null space of the Hessian. Furthermore we can show that each dimension in the null space of the Hessian will correspond to an independent relations between canonical variables a Hamiltonian constraint. Explicitly, for anNNdimensional system, if we have that the rank of the Hessian isR<NR<N, then we can consider theN−RN-Rnull eigenvectorsλ(a)i​(q,q˙)\lambda_{(a)}^{i}(q,\dot{q}):(9)λ(a)i​(q,q˙)​Wi​j​(q,q˙)=0\lambda_{(a)}^{i}(q,\dot{q})W_{ij}(q,\dot{q})=0

fori,j=1,…,Ni,j=1,...,Nanda=1,…,N−Ra=1,...,N-R. This should be compared to the case of a regular Lagrangian system where the non-null directions are used to solve the Euler–Lagrange equations by integrating (6). We can introduce a set of explicitcanonical constraintswhich describe the relations between positions and momenta via a relation of the form:(10)φs=ps−gs​(q,pα)=0\varphi_{s}=p_{s}-g_{s}(q,p_{\alpha})=0

where the indexs=1,…,N−Rs=1,...,N-Rruns over the canonical variables which are not independent,α=1,…,R\alpha=1,...,Rruns over the remaining independent variables, and the functionsφs\varphi_{s}encode the relevant interdependencies. These relations are calledprimary constraintsfollowing the coinage ofAnderson and
Bergmann (1951). From these relations we can, at least locally, derive an explicit form of the dynamics of a constrained Hamiltonian by substituting (10) to eliminate theN−RN-Rdependent momenta, deriving the analogue of Hamilton’s equations, and then applying consistency conditions leading tosecondary constraints. Applying consistency conditions again may lead to further constraints and it is only given a termination of this procedure that a well-posed first order formalism can be established. For the most basic case the primary constraints are automatically propagated consistently and all constraints are primary constraints. In what follows we will also assume that all constraints arefirst-class, which means that they are mutually Poisson commuting on the sub-manifold that they define on phase space, that the constraint algebra is a Lie algebra, which means that their Poisson bracket relations close with at most structure constants, and that they Poisson commute with the Hamiltonian.555For more details on the explicit approach see(Sundermeyer1982, pp. 45–50)and(Gitman and
Tyutin, pp, 13–16)andHenneaux and
Teitelboim (1992)for the implicit approach, which is more general, seeSundermeyer (1982).

There are two natural methods for the category theoretic presentation of the models and isomorphisms of a constrained Hamiltonian theory: extrinsic and intrinsic. In the extrinsic, we consider the theory as formulated on the full phase space in the intrinsic we define the salient objects directly on the constraint manifold. Following the proposal ofBradley (2025b)(made in a slightly different context) we can formulate the extrinsic categoryConHamas having its objects the models as picked out by the quadruple⟨Γ,𝒜,ω,φs⟩\langle\Gamma,\mathcal{A},\omega,\varphi_{s}\rangle, where theφs\varphi_{s}are the full collection of constraints which are (by assumption) first class and primary in the terminology introduce above, and the isomorphisms as given by the subclass of symplectomorphism that also preserve the constraints.666UnconHamis the analogous to the categoryTotHaminBradley (2025b)in that it also defines a Hamiltonian theory not restricted to the final constraint surface. However, formally the two categories are quite different in that inTotHamthe relevant models are defined on the (first class) primary constraint surface of theory with secondary constraints.That is, the diffemophismsf:Γ→Γf:\Gamma\rightarrow\Gammawhich are such that their push-forward satisfiesf∗​ω′=ωf^{*}\omega^{\prime}=\omega,f∗​𝒜→𝒜f^{*}\mathcal{A}\rightarrow\mathcal{A}, andf∗​φs→φsf^{*}\varphi_{s}\rightarrow\varphi_{s}. We might then understand the dynamics to be defined simply by Hamilton’s equations as before. So we could again define expressions of the form:A,H∈𝒜A,H\in\mathcal{A},A˙={A,H}:=ω​(XA,XH)\dot{A}=\{A,H\}:=\omega(X_{A},X_{H}), andιXH​ω=d​H\iota_{X_{H}}\omega=dH.However, this nomic structure is pathological since it does fulfil the partition function. Although the Hamilton vector fieldsXHX_{H}andXAX_{A}are unique they do not lie everywhere along the constraint surface and thus supposedly dynamical trajectories in phase space may start off by obeying the constraints and then move away from the surface.

The obvious response to this pathology is to move to an intrinsic presentation where we seek to construct models explicitly within the sub-manifoldΣ\Sigmadefined by the constraints. Let us define the inclusion mapi:Σ↪Γi:\Sigma\hookrightarrow\Gammaand then push this map forward onto the symplectic structure to define a two formω~=i∗​ω\tilde{\omega}=i^{*}\omegaand onto the algebra of phase space functions to define a sub-algebra of functions that are restricted to the constraint surface,𝒜~=i∗​𝒜\tilde{\mathcal{A}}=i^{*}\mathcal{A}where the binary operation is given byω~\tilde{\omega}. Since our consistency conditions imply that{φi,H~}Σ:=ω~​(Xφi,XH~)=0\{\varphi_{i},\tilde{H}\}_{\Sigma}:=\tilde{\omega}(X_{\varphi_{i}},X_{\tilde{H}})=0,
we are guaranteed that the dynamics defined byιXH~​ω~=d​H~\iota_{X_{\tilde{H}}}\tilde{\omega}=d\tilde{H}andA˙Σ:=ω​(XA~,XH~)\dot{A}_{\Sigma}:=\omega(X_{\tilde{A}},X_{\tilde{H}})will be restricted to the constrain surface. However, crucially, the two formω~\tilde{\omega}will in general be closed but degenerate. It is a pre-symplectic two form and has a non-trivial kernel consisting of the null vector fieldsιXφi=0\iota_{X_{\varphi_{i}}}=0associated with the constraints. This means that the dynamical equations are not uniquely determined.This nomic structure is still pathological since it does fulfil the projection function. We will return to this issue shortly.

Following the proposal ofBradley (2025b)we can then formulate the intrinsic categoryPreHamas having its objects the models as picked out by the tuble⟨Σ,ω~,𝒜~⟩\langle\Sigma,\tilde{\omega},\tilde{\mathcal{A}}\rangleand consider the isomorphisms defined via the diffemophismsg:Σ→Σg:\Sigma\rightarrow\Sigmawhich are such thatg∗​ω~′=ω~g^{*}\tilde{\omega}^{\prime}=\tilde{\omega}andg∗​𝒜~′=𝒜~g^{*}\tilde{\mathcal{A}}^{\prime}=\tilde{\mathcal{A}}.777This is the category thatBradley (2025b)callsExtHamwith only notational changes.One can insightfully apply the tools for the analysis of theoretical structure via conditions on functors to our two presentations of the constrained Hamiltonian formalism. Once more followingBradley (2025b), we can define a functorF:ConHam→PreHamF:\textbf{ConHam}\rightarrow\textbf{PreHam}that takes each model⟨Γ,𝒜,ω,φs⟩\langle\Gamma,\mathcal{A},\omega,\varphi_{s}\rangleto its restriction to the points that satisfy the constraintsφs=0\varphi_{s}=0, i.e. the associated model⟨Σ,ω~,𝒜~⟩\langle\Sigma,\tilde{\omega},\tilde{\mathcal{A}}\rangle, and takes each isomorphismffto its action onΣ\Sigma. Proposition 2 ofBradley (2025b)then takes the form:

## Proposition 1.

F:ConHam→PreHamF:\textbf{ConHam}\rightarrow\textbf{PreHam}is faithful and essentially surjective but not full.

The proof is identical to that provided in(Bradley2025b, A.1-2)mutatis mutandis.888The difference between the two cases is entirely with regard to the the fact that ourConHamis defined via symplectic structure whereas Bradley’sExtHamis defined via presymplectic structure. The structure of the proof is then such that it will carry across between the two cases.Following the interpretational approach summarised in Table1, we can understand the move to the constraint surface as the elimination of surplus structure. There are isomorphisms ofConHamthat are not isomorphisms ofPreHamin particular transformations that correspond to moving along the null vector fieldsXφiX_{\varphi_{i}}.

Significantly, however, wecannotat this point move to an interpretation of these theories within the Nomic-Air formalism according to Table2since we do not have a sufficient formal basis to identify the DPMs inConHam(due to the lack of partition) or the DDPMs inPreHam(due to the lack of projection). The problem is that in both cases the nomic structure is pathological: it does not provide us with a well-posed initial value (or boundary) problem. ForConHamthe problem is obviously related to the failure to restrict to the constraint surface and that is precisely what moving toPreHamsolves. However, whilst understanding a constrained Hamiltonian theory via this category might appear to provide us with the right level of structure to pick out solutions up to isomorphism, since the salient nomic structure is itself only defined up to isomorphism it is formally ill-posed as an initial value problem precisely because it fails to project out aperniciousform of redundancy between DPMs, cf.(Bradley2025b, p.14).999This issue has been discussed a number of time in the philosophical literature on constrained Hamiltonian without its general relevance to debates on symmetry seemingly being full appreciated. SeeBelot (2003); Thébault (2011).The following two-subsections are devoted to the diagnosis of this issue following, first, the traditional Dirac approach and, second, the geometric approach ofGryb and
Thébault (2024). We will return to the problem of identifying a non-pathological presentation of the nomic structure in Section4.1in the context of the discussion ofBradley (2025b)on symplectic reduction.

## 3.2.Dirac’s Theorem

The first step is to consider explicitly the connection between the null-vector fields associated with the constraints and the ill-poedness of the initial value problem. Following a highly influential argument due toDirac (1964), it is possible to prove, in certain restricted circumstances, a direct correspondence between the directions associated with the first class of constraints within a Hamiltonian formalism. If we restrict to theories in which the constraints automatically propagate consistently (they are ‘primary constraints’) and have vanishing Poisson bracket with each other (they are ‘first class constraints’) then it is possible to prove what is often called ‘Dirac’s Theorem’ and which can be presented more formally as follows:

## Proposition 2.

Given that:
- i.

We have a constrained Hamiltonian theory with first-class primary constraintsϕa\phi_{a}, with associated totally arbitrary multipliersvav^{a}, a time dependent phase space functionF​(t):(q,p)t→ℝF(t):(q,p)_{t}\rightarrow\mathbb{R}, and external time parameter,tt.
- ii.

The physical state of the system at an initial timeStS_{t}can be specified by a full set of canonical variables(q,p)t1(q,p)_{t_{1}}; that is, although we must allow for physical states to not be uniquely determined by specified of canonical variables, we can assume that canonical variables uniquely determine physical states.StS_{t}thus supervenes on(q,p)t(q,p)_{t}.
- iii.

Whenever we make a specification of the physical state at an initial time, the equations of motion then fully determine the physical state at other times.
- iv.

Define any transformation of the canonical variables that does not change the physical state as a gauge transformation.

Then,
- D.

The first-class primary constraints,ϕa\phi_{a}, generate gauge transformations.

See(Gryb and
Thébault2024, p.117)for the proof after the original argument ofDirac (1964). The implications of Dirac’s theorem are easy to understand: we should treat as dynamically distinct only those solutions that are independent of the flows on phase space associated to the first-class primary constraints and, conversely, phase space points that lie along the orbit of a first-class primary constraint should be taken to represent physically identical states of affairs. This is precisely an interpretive justification of the geometric definition the isomorphism class inConHanabove.

There are two important restrictions to the scope of Dirac’s theorem which limit its applicability. First, in general, whilst wecanexpect most physical theories to feature constraints that are first-class and not second class, many theories, such as electromagnetism and general relativity, feature constraints that are secondary as well as primary. In his original presentation Dirac makes the ‘conjecture’ that secondary first-class constraints might also generate transformations of the physical variables that do not change physical states. There is then a large literature discussing the extent to which the conjecture can in fact be proved, and the relevance of ‘pathological’ counter-examples.101010SeeLusanna (1990,1991); Pons (2005)and the more complete lists of references therein. Recent philosophical discussion can be found inPitts (2014,2022,2024); Pooley and
Wallace (2022); Bradley (2025c,a,d).Second, as notably discussed byBarbour and
Foster (2008), the restriction to theories with an external time parameter is very limiting. In particular, any theory which is time reparametrization invariant will fall outside the scope of Dirac’s theorem. In such ‘totally constrained’ theories the Hamiltonian is itself a constraint and the association between the constraint action and gauge transformation leads to the infamous problem of time.111111SeeKuchař (1991); Isham (1993); Pons
et al. (2010); Anderson (2017); Gryb and
Thébault (2016,2024); Casadio et al. (2024)

Over and above these formal restrictions the conceptual weakness of Dirac’s approach is that it involves introducing a notion of gauge transformation both too general and too specific. It is too general since it opens up a vagueness as to what we mean by ‘does not change the physical state’. In particular, such a notion of gauge would, under some interpretations of the physical state, include rigid global transformations, like uniform spatial translations, which have nothing to do with first-class constraints nor ill-posed initial value problems. It is too specific since it restricts us to considering dynamical redundancy for instantaneous states defined relative to an external temporal background. What we would really like is a notion of gauge transformation that isdirectlyconnected to the irregularity of the Lagrangian and the fact that the accelerations depend on arbitrary functions and their derivatives(Sundermeyer1982, p. 89)and moreover makes explicit precisely when the existence of constraints derives from ill-defined initial value problems. This calls for a more geometric approach to the problem.

## 3.3.Isochronous symmetries and Initial Value Constraints

The first step in constructing a geometric formalism for the analysis of gauge symmetries in irregular Lagrangian systems is to consider a first-order Lagrangian form of the variational principle and equations of motion. This allows us to express the variational principle and symmetries in terms of geometric quantities on the tangent bundle. To adopt such an approach is follow the example of Emmy Noether rather than Paul Dirac. That is, unlike in the Dirac approach considered above, we assume an action,SS, has a particular symmetry, then investigate its consequences. As such, the structure of the approach we will follow is in the same spirit as Noether’s approach in deriving her two theorems, whilst differing on some crucial details and scope.121212See(Gryb and
Thébault2024, p. 119-121, 125-128, 181)for detailed discussion of the role and limitations of Noether’s theorem in the context of the analysis below. SeeLusanna (1991); Kosmann-Schwarzbach (2010)and(Olver1991, §4.4)for more details on Noether’s theorem and its relation to modern geometric analysis of symmetries and Lie groups.

Building on the analysis of(Gryb and
Thébault2024, §8)andGryb (2025), which is partially based onWoodhouse (1997), we can introduce the basic elements of our formalism as follows. First, consider the actionS​[γ]=∫γL​(qi,q˙i)S[\gamma]=\int_{\gamma}L(q^{i},\dot{q}^{i}), which is first order in the configuration variablesqi∈𝒞q^{i}\in\mathcal{C}, as a functional of the curveγ:ℝ→𝒞\gamma:\mathbbm{R}\to\mathcal{C}parametrized by the time variablett.131313Note that the generalisation to higher order actions is straightforward and thatiican be considered a continuous index for field theory applications.Then, define thevelocity phase space𝒱=T​𝒞\mathcal{V}=T\mathcal{C}equipped with local coordinates(qi,vi)(q^{i},v^{i})and treat the LagrangianL​(qi,vi)L(q^{i},v^{i})as a function on this space. We can write a first-order action,S1​[γ]S_{1}[\gamma], which is equivalent to but distinct from the second-order actionSS, using the one-form(11)θ=∂L∂vi​d​qi\theta=\frac{\partial L}{\partial v^{i}}\text{d}q^{i}\,

and the Hamiltonian function(12)H=vi​∂L∂qi−L.H=v^{i}\frac{\partial L}{\partial q^{i}}-L\,.

Note that, unlike on phase space proper,θ\thetaandHHare explicit functions of the LagrangianLL. Using these quantities, we have that(13)S1​[γ]=∫t1t2d​t​(ιX​θ−H)=∫γ(θ−H​d​t).S_{1}[\gamma]=\int_{t_{1}}^{t_{2}}\text{d}t\left(\iota_{X}\theta-H\right)=\int_{\gamma}\left(\theta-H\text{d}t\right)\,.

The vector field(14)X:=γ˙=q˙i​∂∂qi+v˙i​∂∂viX:=\dot{\gamma}=\dot{q}^{i}\frac{\partial}{\partial q^{i}}+\dot{v}^{i}\frac{\partial}{\partial v^{i}}\,

is the tangent to a trial curveγ\gamma, now a path in𝒱\mathcal{V}, at timett, where dots are time derivates with respect tottand fields are taken to over the extended velocity phase space𝒱t=ℝ×Γ\mathcal{V}_{t}=\mathbbm{R}\times\Gamma.

Let us now consider variations of the actionS1S_{1}with respect to a vector fieldu∈ℝ×T​𝒱u\in\mathbbm{R}\times T\mathcal{V}satisfyingιu​d​t=0\iota_{u}\text{d}t=0, whered​t\text{d}tis understood as the differential induced by the embedding ofγ\gammainto𝒱\mathcal{V}. SinceιX​d​t=1\iota_{X}\text{d}t=1, this condition implies thatuuhas no component along the tangentXXtoγ\gamma, and therefore can’t reparameteriseγ\gamma. We will call such variationsisochronoussince they preserve the time parameterization. Note that this doesnotmean thatuumust be time independent: as a function ofℝ\mathbbm{R}it can vary in time while having no component alongXXas a vector in velocity phase space. The important case where arbitrary parameterizations ofγ\gammaare allowed will be treated separately in the context of reparameterization invariant mechanics and the problem of time, see(Gryb and
Thébault2024, §12)andGryb and
Thébault (2026b).

Using this assumption, a straightforward (and well-known) calculation shows that the variational principle𝔏u​S1=0\mathfrak{L}_{u}S_{1}=0, withu​(t1)=u​(t2)=0u(t_{1})=u(t_{2})=0, leads to Hamilton’s equations(15)ιX​ω+d​H=0\iota_{X}\omega+\text{d}H=0\,

in their usual geometric form but now on velocity phase space so thatω=d​θ\omega=\text{d}\thetaandHHare taken to be functions onΓ\Gamma. Equivalence to the second-order formalism can be seen by noting that thed​vi\text{d}v^{i}leg of this equation reduces to Hamilton’s first equationq˙i=vi\dot{q}^{i}=v^{i}while thed​qi\text{d}q^{i}leg then reduces to the Euler-Lagrange equations arising fromSS.

Let us now study the consequences resulting fromS1S_{1}containing symmetries. Instead of considering, as above, arbitrary isochronous variations generated byuuand looking for conditions onXXthat satisfy𝔏u​S1=0\mathfrak{L}_{u}S_{1}=0, we considerparticularisochronousuαu_{\alpha}and take if for granted that𝔏uα​S1=0\mathfrak{L}_{u_{\alpha}}S_{1}=0forarbitraryXX(i.e., evenXXnot satisfying Hamilton’s equations). We take this to be the condition to be satisfied for the actionS1S_{1}to have symmetries.

Let us start by assuming that the symmetries of the second-order Lagrangian theory take the form(16)δϵ​qi=Tαi​ϵ​(t),\delta_{\epsilon}q^{i}=T^{i}_{\alpha}\epsilon(t)\,,

whereTαiT^{i}_{\alpha}are operators on configuration space only (i.e., they are independent of the velocitiesq˙i\dot{q}^{i}) generating the symmetries andϵ​(t)\epsilon(t)is a time-dependent gauge parameter. For a gauge groupGGwith structure constantsfα​βγf^{\gamma}_{\alpha\beta}, the generators are representation of the algebra𝔤\mathfrak{g}ofGG:(17)[𝐓α,𝐓β]=fα​βγ​𝐓γ,[\mathbf{T}_{\alpha},\mathbf{T}_{\beta}]=f^{\gamma}_{\alpha\beta}\mathbf{T}_{\gamma}\,,

in terms of the vector fields𝐓α=Tαi​∂i\mathbf{T}_{\alpha}=T^{i}_{\alpha}\partial_{i}inT​𝒞T\mathcal{C}. This is a restricted form of gauge transformations as compared to the normal Noether setup. As we will see, this restriction limits our attention to theories with only primary constraints, consistent with the assumptions of this paper. The more general case is treated inGryb and
Thébault (2026a), cf.(Gryb and
Thébault2024, §8.4).

The symmetries (16) act on velocity phase space through theprolongationvector field(18)uα=ϵ​(Tαi​∂qi+T˙αi​∂vi)+ϵ˙​(Tαi​∂vi),u_{\alpha}=\epsilon\left(T^{i}_{\alpha}\partial_{q^{i}}+\dot{T}^{i}_{\alpha}\partial_{v^{i}}\right)+\dot{\epsilon}\left(T^{i}_{\alpha}\partial_{v^{i}}\right)\,,

which can be found by differentiating (16) and reading off the terms of theqiq^{i}andviv^{i}variations. Note thatuαu_{\alpha}splits into two terms multiplying different time derivatives ofϵ\epsilon. These terms are independent at a giventt. Let us call them(19)u0,α\displaystyle u_{0,\alpha}=Tαi​∂qi+T˙αi​∂vi\displaystyle=T^{i}_{\alpha}\partial_{q^{i}}+\dot{T}^{i}_{\alpha}\partial_{v^{i}}u1,α\displaystyle u_{1,\alpha}=Tαi​∂vi.\displaystyle=T^{i}_{\alpha}\partial_{v^{i}}\,.

Imposing that the action be invariant under variations with respect touαu_{\alpha}, we get(20)𝔏uα​S1=∫γ[ιX​(ιuα​ω+d​Jα)−(ιuα​d​H)​d​t]=0,\mathfrak{L}_{u_{\alpha}}S_{1}=\int_{\gamma}\left[\iota_{X}\left(\iota_{u_{\alpha}}\omega+\text{d}J_{\alpha}\right)-\left(\iota_{u_{\alpha}}\text{d}H\right)\text{d}t\right]=0\,,

where we have defined the closed (though possibly degenerate) 2-formω=d​θ\omega=\text{d}\thetaand the quantities(21)Jα:=ιuα​θ.J_{\alpha}:=\iota_{u_{\alpha}}\theta\,.

## 3.3.1.Noether’s first theorem

We gain intuition about theJαJ_{\alpha}’s by considering the simplified case where theϵα\epsilon_{\alpha}are constants so that onlyu0,αu_{0,\alpha}contributes touαu_{\alpha}. The exterior derivativedon𝒱t\mathcal{V}_{t}reduces to the exterior derivatived𝒱\text{d}_{\mathcal{V}}on𝒱\mathcal{V}so that, for arbitraryXX, (20) leads to(22)ιu0​α​ω+d𝒱​Jα\displaystyle\iota_{u_{0\alpha}}\omega+\text{d}_{\mathcal{V}}J_{\alpha}=0\displaystyle=0(23)ιu0​α​d𝒱​H=0.\displaystyle\iota_{u_{0\alpha}}\text{d}_{\mathcal{V}}H=0\,.

The first equation, states thatJα=ιu0,α​θ=Tαi​∂L∂q˙iJ_{\alpha}=\iota_{u_{0,\alpha}}\theta=T^{i}_{\alpha}\,\frac{\partial L}{\partial\dot{q}^{i}}is the charge whose Hamilton vector fieldu0,αu_{0,\alpha}generates the global symmetry. In Section4.2, we will see that (22) is equivalent to the statement thatJαJ_{\alpha}is amomentof a strongly Hamiltonian group action cf.(Woodhouse1997, p.42). Since theTαiT^{i}_{\alpha}form represenations of the original algebra𝔤\mathfrak{g}, the fieldsu0,αu_{0,\alpha}are representations of𝔤\mathfrak{g}. Since the momentsJαJ_{\alpha}collapse elements of𝔤\mathfrak{g}to numbers, they form representation of the dual algebra𝔤∗\mathfrak{g}^{*}. The collection of moments then form themomentum mapof the groupGGabout which we will say more later.

The second equation (23) requires that the Hamiltonian flow ofJαJ_{\alpha}be zero:J˙α:={Jα,H}=0\dot{J}_{\alpha}:=\left\{J_{\alpha},H\right\}=0, where{⋅,⋅}\left\{\cdot,\cdot\right\}is the Poisson bracket associated with the (non-degenerate) symplectic 2-formω\omega. This is the symplectic version of Noether’s first theorem, implying that the momentsJαJ_{\alpha}are conservedNoether chargescf.(Ortega and
Ratiu2013, 4.5.11).

## 3.3.2.Recovering the canonical constraint formalism

We return now to the case where the gauge parameterϵ\epsiloncan be an arbitrary function of time. Inserting the prolongation (18) into the variation (20) leads to several independent constraints. First, since each derivative ofϵ\epsilonis an independent, freely specifiable function at a single time, one obtains two independent constraints: one for theϵ\epsilonterm and one for theϵ˙\dot{\epsilon}term. These terms split further into 1-form equations on𝒱\mathcal{V}and terms multiplyingd​t\text{d}t. The net result is(24)ιui,α​ω+d𝒱​Ji,α\displaystyle\iota_{u_{i,\alpha}}\omega+\text{d}_{\mathcal{V}}J_{i,\alpha}=0(i=0,1)\displaystyle=0\quad(i=0,1)ιu0,α​d𝒱​H\displaystyle\iota_{u_{0},\alpha}\text{d}_{\mathcal{V}}H=0\displaystyle=0ιu1,α​d𝒱​H\displaystyle\iota_{u_{1,\alpha}}\text{d}_{\mathcal{V}}H=J0,\displaystyle=J_{0}\,,

whereJi,α:=ιui,α​θJ_{i,\alpha}:=\iota_{u_{i,\alpha}}\thetaare the moments generating theui,αu_{i,\alpha}.

Becauseu1,αu_{1,\alpha}has nod​q\text{d}qleg,J1,α=ιu1,α​θ=0J_{1,\alpha}=\iota_{u_{1,\alpha}}\theta=0is exactly zero. Thus, thei=1i=1component of the first equation becomes(25)ιu1,α​ω=0.\iota_{u_{1,\alpha}}\omega=0\,.

This says thatu1,αu_{1,\alpha}is a degenerate direction ofω\omega. Using the explicit definitions (19) and (11) (recalling thatω=d​θ\omega=\text{d}\theta), we find that(26)Tαi​Wi​j=0,T^{i}_{\alpha}W_{ij}=0\,,

which reproduces our earlier result of (9) that the symmetry generators are in the kernel of the Hessian. Note that this is an off-shell identity, reflecting the non-invertibility of the Legendre transform. SinceWi​jW_{ij}reflects the part of the Hessian affecting thevi→piv^{i}\to p_{i}transformation, it states that the vectoru1,α=Ti​∂viu_{1,\alpha}=T^{i}\partial_{v^{i}}projects to zero under the Legendre transform.

Using the explicit expression forHHfrom (12), we find that the last equation of (24) becomes(27)J0,α=ιu1,α​d​H=Tαi​Wi​j​vj=0.J_{0,\alpha}=\iota_{u_{1,\alpha}}\text{d}H=T^{i}_{\alpha}W_{ij}v^{j}=0\,.

This leads to theprimary constraint(28)J0,α=Tαi​∂L∂vi=Ti​pi=0.J_{0,\alpha}=T^{i}_{\alpha}\frac{\partial L}{\partial v^{i}}=T^{i}p_{i}=0\,.

This off-shell identity is linked to the non-invertibility of the Legendre transform apparent from (26). Because of this, it can only be expressed in phase space and not velocity phase space. In this way, the primary constraintJ0,α=0J_{0,\alpha}=0replaces the vectoru1u_{1}on phase space, which can only be expressed on velocity phase space. So whileJ0,αJ_{0,\alpha}reduces the phase space degrees of freedom by imposing a constraint,u1u_{1}reduces the corresponding velocity phase space degrees of freedom by enlarging the kernel ofω\omega.

The primary constraintJ0,α=0J_{0,\alpha}=0can be inserted into the0-component of the first equation of (24) to imply thatu0,αu_{0,\alpha}is another null direction ofω\omegaoff-shell:(29)ιu0,α​ω=0.\iota_{u_{0,\alpha}}\omega=0\,.

On phase space, this null vector is a consequence of restrictingω\omegato the constraint surfaceJ0,α=0J_{0,\alpha}=0. This condition can be combined with the second equation of (24) and simplified using (26) to give the standardLagrangian constraint:(30)Tαi​Ki=0,T^{i}_{\alpha}K_{i}=0\,,

whereKiK_{i}is given by (8). This calculation involves eliminating theT˙αi\dot{T}^{i}_{\alpha}term appearing in both equations.

The central result of the preceding analysis is that our system of equations resulting from the symmetries ofS1S_{1}leads to: i) an initial value constraintJ0,α=0J_{0,\alpha}=0on phase space; ii) a null directionu0,αu_{0,\alpha}ofω\omegaassociated with this constraint and; iii) a second null directionu1,αu_{1,\alpha}replacing the role ofJ0,αJ_{0,\alpha}on velocity phase space. These results can be used to derive the Lagrangian constraints and kernel of the Hessian. Together they provide a geometric framework that reproduce the standard results from constrained Hamiltonian theories in the presence of purely first class primary constraints but within a Noether rather than Dirac style analysis.

A final significant formal point runs as follows. By constructionuαu_{\alpha}is the linear combination of theui,αu_{i,\alpha}which reproduces the original Lagrangian symmetries when projected on to the configuration variablesqiq^{i}. Becauseu1,αu_{1,\alpha}has nod​q\text{d}qleg, the symmetry is generated entirely byu0,αu_{0,\alpha}. On phase space, with the Poisson bracket canonically extended off the constraint surface, the first equation of (24) says thatu0,αu_{0,\alpha}is the Hamilton vector field ofJ0,αJ_{0,\alpha}. Thus, the gauge generator is simply the primary constraintJ0,αJ_{0,\alpha}itself, reproducing Dirac’s theorem of Section3.2.

To get a well-defined evolution on phase space, one then needs to both restrict the evolution to the primary constraint surface defined byJ0,α−1​(0)={m∈Γ:J0,α​(m)=0​for all​α}J_{0,\alpha}^{-1}(0)=\{\,m\in\Gamma:J_{0,\alpha}(m)=0\ \text{ for all }\alpha\,\}then quotient by the action ofu0,αu_{0,\alpha}. To find the Lie algebra obeyed byu0,αu_{0,\alpha}, note that prolongation is a Lie algebra homomorphism as outlined in(Olver1991, Prop. 5.15). The full prolongationsuαu_{\alpha}then form representations of the original algebra𝔤\mathfrak{g}:(31)[uα,uβ]=fα​βγ​uγ.[u_{\alpha},u_{\beta}]=f^{\gamma}_{\alpha\beta}u_{\gamma}\,.

Using (18) and collecting terms with the same time derivatives ofϵ\epsilongives(32)[u0,α,u0,β]\displaystyle[u_{0,\alpha},u_{0,\beta}]=fα​βγ​u0,γ\displaystyle=f^{\gamma}_{\alpha\beta}u_{0,\gamma}[u0,α,u1,β]\displaystyle[u_{0,\alpha},u_{1,\beta}]=fα​βγ​u1,γ\displaystyle=f^{\gamma}_{\alpha\beta}u_{1,\gamma}[u1,α,u1,β]\displaystyle[u_{1,\alpha},u_{1,\beta}]=0.\displaystyle=0\,.

On phase space, whereu1,αu_{1,\alpha}is projected out, this reduces to the original algebra𝔤\mathfrak{g}of the symmetry group on configuration space. Thus, a well-defined evolution can be achieved on phase space by additionally quotienting by this group:(33)Γred=J0,α−1​(0)/G.\Gamma_{\text{red}}=J_{0,\alpha}^{-1}(0)/G\,.

On velocity phase space, however, there is no primary constraint. Instead, the kernel ofω\omegamust includeu1,αu_{1,\alpha}.141414Note that, on phase space, the symplectic structure is normally canonically extended off the primary constraint surface instead.The reduced space can be obtained by quotienting by the full graded algebra𝔤ext=T​Gext\mathfrak{g}_{\text{ext}}=TG_{\text{ext}}given in (32)(34)𝒱red=𝒱/Gext.\mathcal{V}_{\text{red}}=\mathcal{V}/G_{\text{ext}}\,.

The focus of the following final section is to consider two approaches for applying the tools of category theory to the to the construction of the reduced phase space as defined by (33). In essence, the contrast will be to understandΓred\Gamma_{\text{red}}as either an object in the codomain of a functor followingBradley (2025b)or as the composite of a special class of arrows followingLandsman (2001,2005).

## 4.Reduction and Nomic Regularity

## 4.1.Symplectic Reduction and Category Theory

Let us return to the intrinsic presentation of a classical constrained Hamiltonian theory and consider the procedure ofsymplectic reduction. We will initially follow the insightful analysis ofBradley (2025b)who proceeds in three steps. First, assume that there exists a smooth, differentiable manifold, the reduced phase space,ΓR\Gamma_{R}, defined by taking the quotient ofΣ\Sigmaby the kernel ofω~\tilde{\omega}.151515See(Ortega and
Ratiu2013, p.212)for full formal details.Next, define an open, surjective projection mapπ:Σ→ΓR\pi:\Sigma\to\Gamma_{R}such that we define the reduced two-formωR\omega_{R}viaω~=π∗​(ωR)\tilde{\omega}=\pi^{*}(\omega_{R}), which acts according toωR​(XAR,XBR)=ω~​(XA~,XB~)\omega_{R}(X_{A_{R}},X_{B_{R}})=\tilde{\omega}(X_{\tilde{A}},X_{\tilde{B}})whereXAR=π∗​(XB~)X_{A_{R}}=\pi_{*}(X_{\tilde{B}})andXBR=π∗​(XB~)X_{B_{R}}=\pi_{*}(X_{\tilde{B}}). When the mapπ\piis well-defined there can expectωR\omega_{R}to be a symplectic two form.161616See(Ortega and
Ratiu2013, p.212)for full formal details.Finally, one can then define a reduced HamiltonianHRH_{R}viaπ∗​(H~)\pi_{*}(\tilde{H})and formulate Hamilton’s equations on the reduced phase space asωR​(XHR)=d​HR\omega_{R}(X_{H_{R}})=dH_{R}. The theory formulated on reduced phase space has regular nomic structure meaning that it provides us with a well-posed initial value problem that avoids the pernicious redundancy we encountered earlier. This matches precisely the conclusion ofBradley (2025b), that removing this form of redundancy is well-motivated from the perspective of pursuing a well-posed initial value problem (p. 14).

The next step is to provide a category theoretic presentation of the reduced theory via the categoryHamRedwhich has objects(ΓR,ωR,HR)(\Gamma_{R},\omega_{R},H_{R})and arrows between
objects(ΓR1,ωR1,HR1)(\Gamma^{1}_{R},\omega^{1}_{R},H_{R}^{1})and(ΓR2,ωR2,HR2)(\Gamma^{2}_{R},\omega^{2}_{R},H_{R}^{2})given by diffeomorphismsh:ΣR1→ΣR2h:\Sigma^{1}_{R}\to\Sigma^{2}_{R}such thath∗​(ωR2)=ωR1h^{*}(\omega^{2}_{R})=\omega^{1}_{R}andh∗​HR2=HR1h^{*}H_{R}^{2}=H_{R}^{1}. The categoryHamRedhas an elegant simplicity since models are picked out by symplectic geometries and arrows by the symplectomophisms. In order to study
the relationship between the intrinsic presentation the classical constrained Hamiltonian theory and the theory of the reduced phase spaceBradley (2025b)then defines the functorGGthat takes an object(Σ,ω~,H~)(\Sigma,\tilde{\omega},\tilde{H})to(ΓR,ωR,HR)(\Gamma_{R},\omega_{R},H_{R})and that takes an arrowg:Σ→Σg:\Sigma\to\SigmatogR:ΓR→ΓRg_{R}:\Gamma_{R}\to\Gamma_{R}. Crucially, since the reduction map corresponds to a projection of equivalence classes defined by directions onΣ\Sigmadefined by the kernel ofω~\tilde{\omega}, for anyggthat acts by moving along those directions the correspondinggRg_{R}will be the identity map. This allowsBradley (2025b)to prove that the functorGGis full and essentially surjective but not faithful (see her Proposition 4). In our terminology we have that the intrinsic formulation of the theory of the constraint surface of the original phase space has surplus representational capacity compared to the theory on the reduced phase space relative to the functor defined by the reduction map. Equivalently there are distinct symmetry related DPMs in unreduced formalism that get mapped to the same DPMs in the reduced formalism.

The fact that the functor is full and essentially surjective means that symplectic reduction does not removefurthersurplus structure compared to the intrinsic presentation of the theory on the constraint surface. This means one could plausibly understand the passage from a classical constrained Hamiltonian theory formulated extrinsically on the phase space to a reduced theory in terms of a pair of functors defined via: 1) the immersion map that takes us fromConHamtoPreHamand removes (only) surplus structure by enlarging the isomorphism class; and 2) the quiotenting map that takes us fromConHamtoHamRedand removes (only) surplus representational capacity by projecting non-trivial to trivial automorphisms. Since the composition of two functors is always a functor there should then be definable a functorial relationship between the unreduced and reduced theory. This functor would be expected to be essentially surjective but neither full nor faithful.

The ‘symplectic reduction as functor’ perspective is not, however, the approach taken by mathematical physicists in formalising the symplectic reduction in terms of category theory. There are four interconnected issues that motivate an alternative formalisation of symplectic reduction to that provided byBradley (2025b). First, it would be helpful to have available a more unified formalisation of the immersion and quotient maps. Second, the reduction procedure as we defined it does not make explicit the conditions for the reduced phase space to inherent manifold structure and avoid singularities. Third, it would be more natural for the initial ‘input’ of the reduction procedure to, like the output, be given simply by a symplectic manifold and for us to have available a category theoretic analysis which encodes this. Fourth, and ultimately, most crucial, moving to an approach in which state spaces are understood as arrows and reduction as arrow composition allows for direct connection with procedures for the quantization of theories with irregular nomic structure that was Dirac’s principal motivation in constructing the constrained Hamiltonian formalism in the first place. In order to understand the structure of this alternative category theoretic presentation of symplectic reduction we must return to the idea of the momentum map associated with a symmetry which was mentioned above.

## 4.2.Poisson Manifolds and the Momentum Map

FollowingLandsman (2001,2005)cf.Butterfield (2007); Ortega and
Ratiu (2013), consider the generalisation of symplectic manifolds to the class ofPoisson manifolds,MM, which, by definition, are equipped with a Lie bracket that acts as{⋅,⋅}:C∞​(M)×C∞​(M)→C∞​(M)\{\cdot,\cdot\}:C^{\infty}(M)\times C^{\infty}(M)\rightarrow C^{\infty}(M)and is such that for eachA∈C∞​(M)A\in C^{\infty}(M)the mapB→{A,B}B\rightarrow\{A,B\}defines a derivation ofC∞​(M)C^{\infty}(M)which can be identified with a Hamilton vector fieldXfX_{f}. A smooth map between Poisson manifolds is then aPoisson mapwhen its pullback is a Lie algebra homomorphism and is aanti-Poisson mapwhen its pullback is a Lie algebra anti-homomorphism. Note that the space containing a single pointptis a Poisson manifold with trivial Lie bracket and for any Poisson manifoldMMthe mapM→ptM\rightarrow\text{pt}is trivially both Poisson and anti-Poisson.

Now, consider a Lie groupGGwith associated Lie algebra𝔤\mathfrak{g}which has astrongly Hamiltonian actiononMM. This implies that there exists a pair of Lie algebra homomorphisms: i)x∈𝔤↦XM∈Γ​(M,T​M)x\in\mathfrak{g}\mapsto X^{M}\in\Gamma(M,TM); and ii)x∈𝔤↦Jx∈C∞​(M)x\in\mathfrak{g}\mapsto J_{x}\in C^{\infty}(M)with the property thatXM=XJxX^{M}=X_{J_{x}}, whereΓ​(M,T​M)\Gamma(M,TM)indicates the space of all smooth vector fields onMMandJxJ_{x}are the special functions who generate Hamilton vector fieldXJxMX^{M}_{J_{x}}corresponding to each Lie algebra elementxx. The dual vector space to𝔤\mathfrak{g}then defines a Poisson manifold which we indicate as𝔤∗\mathfrak{g}^{*}. Finally, we can then understand the collection of the functionsJxJ_{x}to define the momentum map of𝔤\mathfrak{g}as the Poisson map:(35)J:M→𝔤∗J:M\rightarrow\mathfrak{g}^{*}

defined via the point-wise condition that for allm∈Mm\in Mandx∈𝔤x\in\mathfrak{g}we have that⟨J​(m),x⟩=Jx​(m)\langle J(m),x\rangle=J_{x}(m)and⟨⋅,⋅⟩:𝔤∗×𝔤→ℝ\langle\cdot,\cdot\rangle:\mathfrak{g}^{*}\times\mathfrak{g}\rightarrow\mathbb{R}is the duality pairing. Connection with our earlier analysis can be straightforwardly seen by considering orthonormal baseseαe^{\alpha}in the algebra𝔤\mathfrak{g}ande~α\tilde{e}^{\alpha}in the dual algebra𝔤∗\mathfrak{g}^{*}. Using these bases, we can identifyJx=J0,α​e~αJ_{x}=J_{0,\alpha}\tilde{e}^{\alpha}andXM=u0,α​eαX^{M}=u_{0,\alpha}e^{\alpha}. Then, as we saw in Section3.3, Equation24confirms thatXMX^{M}is the Hamilton vector field generated byJxJ_{x}and that these quantities are valued in the appropriate representations of𝔤\mathfrak{g}.

Physical intuition for the rather abstract momentum map formalism can be gained immediately by the recognition that the conditionXJX​(H)=0,∀x∈𝔤X_{J_{X}}(H)=0,\>\forall x\in\mathfrak{g}implies that theJxJ_{x}are the constants of the motion associated with the elements of the groupGGvia the symplectic version of Noether’s first theorem. Thus, the momentum map for translations defines the linear momentum at every point and the momentum map for rotations defines the angular momentum at every point. See(Butterfield2007, §6.3)for explicit details.

The power and elegance of the momentum map formalism is made immediately apparent by the representation of symplectic reduction that it affords. Let us consider a symplectic manifold(Γ,ω)(\Gamma,\omega)acted on by a Lie groupGGwith associated Lie algebra𝔤\mathfrak{g}that is strongly Hamiltonian action onΓ\Gamma. The associated constraint surface is then defined simply by the condition introduced above thatJ−1​(0)={m∈M:JX​(m)=0​for all​X∈𝔤}J^{-1}(0)=\{\,m\in M:J_{X}(m)=0\text{ for all }X\in\mathfrak{g}\,\}and the reduced phase space via:(36)ΓR=J−1​(0)/G\Gamma_{R}=J^{-1}(0)/G

The immersion map and the quotient map as can then be expressed as:(37)i:J−1​(0)↪Γ​π:J−1​(0)→ΓRi:J^{-1}(0)\hookrightarrow\Gamma\>\>\>\>\pi:J^{-1}(0)\rightarrow\Gamma_{R}

In the case that0is a regular value ofJJand theGGaction is proper and free onJ−1​(0)J^{-1}(0)we are guaranteed thatΓR\Gamma_{R}is a manifold with symplectic structure which is such thati∗​ω=π∗​ωRi^{*}\omega=\pi^{*}\omega_{R}. This defines the Marsden-Weinstein reduction under which starting from a symplectic manifold(Γ,ω)(\Gamma,\omega)equipped with a strongly Hamiltonian group actionGGwe produce a new symplectic manifold(ΓR,ωR)(\Gamma_{R},\omega_{R})in which the group action has been ‘quotiented out’.171717This process of immersion and reduction is precisely the picture that emerges from the considerations of Section3.3on phase space. Note that, onvelocityphase space, the picture is different. Rather than starting with an immersion onto the primary constraint surface and then quotienting by the gauge groupGG, you must quotient by the full actionGextG_{\text{ext}}of the extended gauge group formed by the full setui,αu_{i,\alpha}.So formulated, however, it is clear that we shouldnotunderstand the process of symplectic reduction in terms of a pair of functors that take us from the category of symplectic manifolds to itself.The immersion map is not total since it is not defined for arbitrary symplectomorphism. In fact, once defined in terms of momentum maps the natural category theoretic presentation of symplectic reduction is in terms of arrow composition. The following two sections are devoted to the explication and interpretation of this idea following the account ofLandsman (2001,2005).

## 4.3.State Spaces as Arrows

The formal basis for presenting the state space of a constrained Hamiltonian theory as an arrow within a category rather than an object comes from the notion of asymplectic dual pair. In general, a symplectic dual pair is defined by a symplectic manifold(Γ,ω)(\Gamma,\omega), a pair of Poisson manifolds,P,QP,Q, and a pair of maps given by the anti-Poisson mapΓ→P\Gamma\rightarrow Pand the Poisson mapQ←ΓQ\leftarrow\Gamma. We require that the pullback of any function onPPshould Poisson commute onΓ\Gammawith the pullback of any function onQQ. We write the symplectic dual pair itself as:(38)Q←𝑞Γ→𝑝PQ\xleftarrow{q}\Gamma\xrightarrow{p}P

and thus can write the pullback condition as{p∗​f,q∗​g}=0\{p^{*}f,q^{*}g\}=0for allf∈C∞​(P)f\in C^{\infty}(P)andg∈C∞​(Q)g\in C^{\infty}(Q).

Formally, a symplectic dual pair is an example of abimodule. Bimodules can be understood as a generalization of homomorphisms since we can construct a functor that takes us from the category that has algebras as objects and homomorphisms as arrows to a category which haskk-algebras as objects, and bimodules as arrows(Landsman2001, 2.1), cf.Feintzeig and
Steeger (2024). Bimodules always come with two compatible ‘left’ and ‘right’ actions. In the case of a bimodule over a pair of Poisson manifoldsP,QP,Qas defined by a symplectic dual pair these are precisely the anti-Poisson (left) and Poisson (right) maps from the symplectic manifold toPPandQQrespectively.

The condition for two symplectic dual pairs over two Poisson manifoldsP,QP,Qto be isomorphic is then that there exists a symplectomorphism renders the relevant Poisson and anti-Poisson maps identical. That is, for the dual pairs:(39)Q←q1Γ1→p1P\displaystyle Q\xleftarrow{q_{1}}\Gamma_{1}\xrightarrow{p_{1}}P(40)Q←q2Γ2→p2P\displaystyle Q\xleftarrow{q_{2}}\Gamma_{2}\xrightarrow{p_{2}}P

the condition for isomorphism is that we have thatφ:Γ1→Γ2\varphi:\Gamma_{1}\rightarrow\Gamma_{2}is such thatq2​φ=q1q_{2}\varphi=q_{1}andp2​φ=p1p_{2}\varphi=p_{1}. FollowingLandsman (2005), the equivalence class of isomorphic symplectic dual pairs can then be interpreted as an arrow fromQQtoPP. So defined, the arrows are well-suited to the representation of model spaces of both constrained and unconstrained Hamiltonian theories.

Consider for example, the simplest case of a theory with regular nomic structure. The phase space of such a theory can be represented simply via a symplectic manifold and we can choose as the appropriate dual pair simply the trivial Poisson manifolds and maps given by:(41)pt←(Γ,ω)→pt\textit{pt}\leftarrow(\Gamma,\omega)\rightarrow\textit{pt}

whereptindicates the one-point manifold that is trivially both Poisson and anti-Poisson. Since we define the arrows as the equivalence class of isomorphic symplectic dual pairs the condition for two model spaces as arrows to be isomorphic is identical to that which we would obtain by considering model spaces to be objects in the category of symplectic manifolds with symplectomorphisms again the salient isomorphisms. Thus if we take as a norm for physical representational practice that mathematical objects which are isomorphic under the relevant mathematical notion of isomorphism should be taken to have the same representational capacities(Weatherall2018)then we immediately get that model spaces as symplectic manifolds have the same representational capacities whether we take these to be objects in the category of symplectic manifolds(Thébault2026)or dual pairs as arrows between (trivial) Poisson manifolds.181818The generalisation of this approach to richer representations that include dynamics as encoded within non-trivial Poisson structure should then follow by considering thebifibrationsdefined respectively by the orbits of a Hamiltonian vector fieldXHX_{H}and the (connected components of the) level sets ofHH(Fasso2005).

The dual pair representation of model spaces as arrows is particularly well-suited to the representation of constrained Hamiltonian theories. As noted already, the dual to a Lie algebra,𝔤∗\mathfrak{g}^{*}, is a Poisson manifold. This means we can consider Poisson maps defined via𝔤∗←(Γ,ω)\mathfrak{g}^{*}\leftarrow(\Gamma,\omega)and anti-Poisson map(Γ,ω)→𝔤−∗(\Gamma,\omega)\rightarrow\mathfrak{g}^{*}_{-}where𝔤−∗\mathfrak{g}^{*}_{-}is the relevant Poisson manifold equipped with minus the Poisson bracket. Now consider a constrained Hamiltonian system with unconstrained phase space(Γ,ω)(\Gamma,\omega)and constraint surface defined viaJ=0J=0whereJ:Γ→𝔤∗J:\Gamma\rightarrow\mathfrak{g}^{*}is the momentum map associated to strongly Hamiltonian action of a Lie groupGGonΓ\Gamma. Following(Weinstein1983, §8), in general we have that if a Lie groupGGacts freely on a symplectic manifoldΓ\Gammawith momentum mapJJ, then the spaceΓ/G\Gamma/Gis a manifold and functions onΓ/G\Gamma/Gindicates indicates quotient for a rightGG-action and may thus be identified with the function group ofGG-invariant functions.

We thus have that the manifoldΓ/G\Gamma/Ghas Poisson structure for which the projectionρ:Γ→Γ/G\rho:\Gamma\rightarrow\Gamma/Gis a Poisson mapping. Furthermore, the structure of the mapsρ\rhoandJJis such that their pull-backs toΓ\Gammawill Poisson commute. Thus the model space of a constrained Hamiltonian theory can be defined via symplectic dual pair as(Weinstein1983; Landsman2005):(42)G\Γ←𝜌(Γ,ω)→𝐽𝔤−∗G\backslash\Gamma\xleftarrow{\rho}(\Gamma,\omega)\xrightarrow{J}\mathfrak{g}^{*}_{-}

whereG\ΓG\backslash\Gammaindicates quotient for a leftGG-action. In fact, one of the motivating examples in the construction of the more general class of mathematical object defined by dual pairs was precisely the pair above obtained by considering a strongly Hamiltonian Lie group action on a symplectic manifold with associated momentum map. It is thus not surprising that one provides a natural way to represents the other.

The proposal ofLandsman (2001,2005)is then to treat the equivalence class of isomorphic symplectic dual pairs as arrows. This then amounts to interpreting the model space of a constrained Hamiltonian theory together with the associated maps,ρ\rhoandJJ, as defining arrows between the Poisson manifoldsG\ΓG\backslash\Gammaand𝔤−∗\mathfrak{g}^{*}_{-}. Since such arrows are defined directly via the equivalence class we automatically get that symplectomorphic dual pairs correspond to model spaces with equivalent representational capacity. An attractive feature of this approach is that the extra structure defined by the left and right ‘legs’ of the dual pair allows us to encode the partition and projection that pick out the restrictions required for the models to be respectively dynamically possible and distinct. These are the immersion mapi:J−1​(0)↪Γi:J^{-1}(0)\hookrightarrow\Gammaand quotient mapπ:J−1​(0)→ΓR\pi:J^{-1}(0)\rightarrow\Gamma_{R}each of which is defined via the momentum map.

The symplectomorphisms that define the equivalence class of a dual pair are then required to be such that ifφ:Γ→Γ′\varphi:\Gamma\rightarrow\Gamma^{\prime}is the symplectomorphism thenJ′​φ=JJ^{\prime}\varphi=J. Evidently, the momentum map encodes nomic structure in terms of the partition and projection functions. Such nomic structure is automatically defined only up to isomorphism and can be specified within the same object that defines the state space up to isomorphism. Constrained Hamiltonian theories can then be understood in terms of a collection of arrows and we automatically recover the basic requirement that theories with isomorphic state spaces will be equivalent. The next step is cateorgical presentation is to specify the composition operation. The following subsection will introduce the appropriate operation and consider the representation of symplectic reduction as special class of arrow compositions under this product.

## 4.4.Symplectic Reduction as Arrow Composition

Let us consider two compatible dual pairsQ←Γ1→PQ\leftarrow\Gamma_{1}\to PandP←Γ2→RP\leftarrow\Gamma_{2}\to Rand the conditions for which we can define a tensor product that yields a new dual pairQ←Γ3→RQ\leftarrow\Gamma_{3}\to R. Let us consider a symplectic manifold(Γ,ω)(\Gamma,\omega)and letΣ\Sigmabe a closed sub-manifold. As above we define the closed two formω~=i∗​ω\tilde{\omega}=i^{*}\omegaas the restriction ofω\omegatoΣ\Sigmaviai:Σ↪Mi:\Sigma\hookrightarrow M.

Define the kernel ofω~\tilde{\omega}as thenull distributiononΣ\Sigmawhich we will write as𝒩Σ\mathcal{N}_{\Sigma}. FollowingLandsman (2001), when the rank ofω~\tilde{\omega}is constant onΣ\Sigmathe null distribution𝒩Σ\mathcal{N}_{\Sigma}is
smooth and completely integrable. Let us denote the corresponding foliationℱΣ\mathcal{F}_{\Sigma}and assume that the spaceΣ/ℱΣ\Sigma/\mathcal{F}_{\Sigma}of leaves of this foliation is a manifold in its natural topology. These assumptions suffice to restrict to cases in which symplectic reduction is non-singular and we are guaranteed that the reduced space will be a symplectic manifold.

Under these restrictions we can define the product of dual pairs as follows. LetQ←Γ1→PQ\leftarrow\Gamma_{1}\to PandP←Γ2→RP\leftarrow\Gamma_{2}\to Rbe dual pairs, with Poisson mapsJL:M1→P−J_{L}:M_{1}\to P^{-}andJR:M2→PJ_{R}:M_{2}\to P. Assume that(43)Tp​P=(Tx​JL)​(Tx​Γ1)⊕(Ty​JR)​(Ty​Γ2)T_{p}P=(T_{x}J_{L})(T_{x}\Gamma_{1})\oplus(T_{y}J_{R})(T_{y}\Gamma_{2})

for all(x,y)∈Γ1×PΓ2(x,y)\in\Gamma_{1}\times_{P}\Gamma_{2}, wherep=JL​(x)=JR​(y)p=J_{L}(x)=J_{R}(y). Define the fibre product between two manifolds byM1×Pf,gM2={(m1,m2)∈M1×M2|f​(m1)=g​(m2)}M_{1}\times^{f,g}_{P}M_{2}=\{(m_{1},m_{2})\in M_{1}\times M_{2}|f(m_{1})=g(m_{2})\}forf:m1→Pf:m_{1}\rightarrow Pandg:m2→Pg:m_{2}\rightarrow P. Then we can specify thatΓ3=Γ1×Γ2\Gamma_{3}=\Gamma_{1}\times\Gamma_{2}andΣ=Γ1×PΓ2\Sigma=\Gamma_{1}\times_{P}\Gamma_{2}and are guaranteed that𝒩Σ\mathcal{N}_{\Sigma}is
smooth and completely integrable. Given thatΣ/ℱΣ\Sigma/\mathcal{F}_{\Sigma}is a manifold in its natural topology we then have that the product operationΓ1⊚PΓ2\Gamma_{1}\circledcirc_{P}\Gamma_{2}can be defined via the symplectic manifold:(44)Γ1⊚PΓ2=(Γ1×PΓ2)/NΣ.\Gamma_{1}\circledcirc_{P}\Gamma_{2}=(\Gamma_{1}\times_{P}\Gamma_{2})/N_{\Sigma}.

and that(45)Q←Γ1⊚PΓ2→R.Q\leftarrow\Gamma_{1}\circledcirc_{P}\Gamma_{2}\to R.

defines a dual pair. So defined the composition operation is associative up to isomorphism.

If we consider the case of a connected Lie groupGGthen the product of the dual pairs defined by a constrained Hamiltonian theoryG\Γ←𝜌(Γ,ω)→𝐽𝔤−∗G\backslash\Gamma\xleftarrow{\rho}(\Gamma,\omega)\xrightarrow{J}\mathfrak{g}^{*}_{-}and the zero coadjoint orbit𝔤−∗↩0→pt\mathfrak{g}^{*}_{-}\hookleftarrow 0\to\mathrm{pt}gives:(46)G\Γ←𝜌(Γ,ω)→𝐽𝔤−∗⊚𝔤−∗𝔤−∗↩0→pt≅G\Γ←ΓR→ptG\backslash\Gamma\xleftarrow{\rho}(\Gamma,\omega)\xrightarrow{J}\mathfrak{g}^{*}_{-}\circledcirc_{\mathfrak{g}^{*}_{-}}\mathfrak{g}^{*}_{-}\hookleftarrow 0\to\mathrm{pt}\cong G\backslash\Gamma\leftarrow\Gamma_{R}\to\mathrm{pt}

whereΓR=J−1​(0)/G\Gamma_{R}=J^{-1}(0)/Gis the Marsden–Weinstein quotient. This reconstruction of the Marsden–Weinstein reduction procedure motivatesLandsman (2005)to introduce the categoryPoissonwhose objects are regular Poisson manifolds and arrows are equivalence classes of regular symplectic dual pairs. Under this restriction we get that all products exist and there are identity arrows(Landsman2001, Def. 5.10). Whilst the regularity condition is relatively mild in the case of the Poisson manifolds it is restrictive enough in the case of the dual pairs to excludept↩ΓR→𝔤−∗\mathrm{pt}\hookleftarrow\Gamma_{R}\to\mathfrak{g}^{*}_{-}. This motivates the reconstruction of symplectic reduction as the well defined composition:(47)pt←(Γ,ω)→𝐽𝔤−∗⊚𝔤−∗𝔤−∗←0→pt≅pt←ΓR→pt\mathrm{pt}\leftarrow(\Gamma,\omega)\xrightarrow{J}\mathfrak{g}^{*}_{-}\circledcirc_{\mathfrak{g}^{*}_{-}}\mathfrak{g}^{*}_{-}\leftarrow 0\to\mathrm{pt}\cong\mathrm{pt}\leftarrow\Gamma_{R}\to\mathrm{pt}

Since arrows are equivalence classes of regular symplectic dual pairs we have the arrow that is the output of the reduction procedurept←ΓR→pt\mathrm{pt}\leftarrow\Gamma_{R}\to\mathrm{pt}is defined only up to symplectomorphism.

If we then define the irregular representations of a constrained Hamiltonian theories by collections of arrows of the formpt←(Γ,ω)→𝐽𝔤−∗\mathrm{pt}\leftarrow(\Gamma,\omega)\xrightarrow{J}\mathfrak{g}^{*}_{-}and reduction by composition with the zero coadjoint orbit𝔤−∗←0→pt\mathfrak{g}^{*}_{-}\leftarrow 0\to\mathrm{pt}then the collection of arrowspt←ΓR→pt\mathrm{pt}\leftarrow\Gamma_{R}\to\mathrm{pt}correspond to theregular representationsof the theory. That is, representations in which the pernicious form of surplus representational capacity has been eliminated and the corresponding initial value problem rendered well-posed. This suggests a notion of theoretical equivalence at the level of regular representations: two constrained Hamiltonian theories have equivalent regular representations when the reduced phase spaces are symplectomorphic. In essence, this means that two theories can be understood to be equivalent when stated as well-posed initial value problems on a reduced phase space but inequivalent when stated as ill-posed initial value problems as constrained Hamiltonian theories that include surplus representational capacity of the particular pernicious form. For example, we may have two theories,TTandT′T^{\prime}, with the same underlying well-posed degrees of freedom but distinct constrained Hamiltonian representations as encoded in the momentum mapsJJandJ′J^{\prime}and group actionsGGandG′G^{\prime}whenever we have that:(48)J−1​(0)/G≅J′⁣−1​(0)/G′J^{-1}(0)/G\cong J^{\prime-1}(0)/G^{\prime}

The symplectic reduction as arrow composition thus allows for a category theoretic presentation of constrained Hamiltonian theories where we automatically gain an equivalence in regular representations based upon the definition of arrows as symplectic dual pairs up to isomorphism.

## 5.Prospectus

The foregoing analysis has articulated a range formal and interpretational features particular to theories with irregular nomic structure. For an important subclass of such theories, we have demonstrated the interconnections between pernicious underdetermination problems and well-posedness of the initial value formulation making use of a first order velocity-phase space formalism. This analysis has been shown to underpin the canonical constraint analysis in both its original form due to Dirac and in geometric form as per Marsden-Weinstein symplectic reduction. Two natural lines of generalisation of the classical analysis are to consider the cases of irregular nomic structure which arises from non-isochronous symmetries and/or which involves secondary as well as primary constraints. The first generalisation would allow our analysis to include mechanical and field theories which are reparametrization invariant and would thus lead us into consideration of the problem of time. Work along these lines can be found in(Gryb and
Thébault2024, §12). The second generalisation would allow our analysis to include theories such as electromagnetism in which the primary constraints do not automatically propagate. This analysis is provided in formal terms inGryb and
Thébault (2026a). The intersection of these two generalisations, that is non-isochronous symmetries and secondary constraints, is precisely the case of general relativity. The application of the velocity-phase space analysis to this case is an outstanding mathematical problem.

A third dimension of generalisation of the foregoing analysis is the extension to quantum theories. Ultimately, the principal motivation for studying the canonical formulation of irregular systems is the challenge of quantization. This is because standard techniques for the conversion of a classical to a quantum theory are built upon (in different senses) promotion of core parts of the regular nomic structure of a classical theory to corresponding quantum structures. Thus, we find that one route to the quantization of a theory with irregular nomic structure is precisely to ‘reduce first’ and ‘quantize’ second. There is, however, a second route, to ‘quantize first and ‘reduce second’. This is the procedure of constraint quantization or Dirac quantization. Furthermore, there exists a conjecture, proved in a wide variety of cases that the quantum theories produced via the two routes are equivalent. This is the famous Guillemin–Sternberg conjecture often informally expressed in the idea that ‘reduction commutes with quantization’. In a companion paper we will deploy the formal tools and interpretational concepts introduced in the present paper towards the analysis of constrain quantization and Guillemin–Sternberg conjecture. Our goal will be to understand the relation between quantum and classical reduction procedures and evaluate the implications of the proposal that the functionality of quantization can be understood, in a certain sense, to be equivalent to the Guillemin–Sternberg conjecture.191919This is specifically intended to allow connection with the work ofFeintzeig (2024,2025)which applies the tools of category theory to quantization in the regular case.

## Acknowledgements

We are grateful to Clara Bradley, Rami Jreige, and Jer Steeger for helpful discussion.

## References
- Anderson (2017)Anderson, E. (2017).The Problem of Time.Springer.
- Anderson and
Bergmann (1951)Anderson, J. L. and P. G. Bergmann (1951).Constraints in covariant field theories.Physical Review83(5), 1018.
- Baez and
Shulman (2009)Baez, J. C. and M. Shulman (2009).Lectures on n-categories and cohomology.InTowards higher categories, pp. 1–68. Springer.
- Barbour and
Foster (2008)Barbour, J. and B. Z. Foster (2008, August).Constraints and gauge transformations: Dirac’s theorem is not always
valid.ArXiv e-prints.
- Barbour and
Bertotti (1982)Barbour, J. B. and B. Bertotti (1982).Mach’s principle and the structure of dynamical theories.Proceedings of the Royal Society of London. A. Mathematical and
Physical Sciences382(1783), 295–306.
- Barrett (2020)Barrett, T. W. (2020).Structure and equivalence.Philosophy of Science87(5), 1184–1196.
- Barrett (2022)Barrett, T. W. (2022).How to count structure.Noûs56(2), 295–322.
- Belot (2003)Belot, G. (2003).Symmetry and gauge freedom.Studies In History and Philosophy of Modern Physics34,
189–225.
- Belot (2013)Belot, G. (2013).Symmetry and equivalence.In R. Batterman (Ed.),The Oxford Handbook of Philosophy of
Physics. Oxford University Press.
- Bradley (2025a)Bradley, C. (2025a).Do first-class constraints generate gauge transformations? a
geometric resolution.The British Journal for the Philosophy of Science.Published online 12 November 2025.
- Bradley (2025b)Bradley, C. (2025b).Excess structure in the constrained hamiltonian formalism.Philosophy of Science, 1–19.
- Bradley (2025c)Bradley, C. (2025c).Excess structure in the constrained hamiltonian formalism.Philosophy of Science.Published online 24 November 2025.
- Bradley (2025d)Bradley, C. (2025d).The relationship between lagrangian and hamiltonian mechanics: The
irregular case.Philosophy of Physics.Published online 17 July 2025.
- Bradley and
Weatherall (2020)Bradley, C. and J. O. Weatherall (2020).On representational redundancy, surplus structure, and the hole
argument.Foundations of Physics50(4), 270–293.
- Butterfield (2007)Butterfield, J. (2007).On symplectic reduction in classical mechanics.In J. Butterfield and J. Earman (Eds.),Philosophy of Physics,
pp. 1–131. Elsevier.
- Casadio et al. (2024)Casadio, R., L. Chataignier, A. Y. Kamenshchik, F. G. Pedro, A. Tronconi, and
G. Venturi (2024).Relaxation of first-class constraints and the quantization of gauge
theories: From “matter without matter” to the reappearance of time in
quantum gravity.Annals of Physics470, 169783.
- Dewar (2022)Dewar, N. (2022).Structure and Equivalence.Cambridge University Press.
- Díaz
et al. (2014)Díaz, B., D. Higuita, and M. Montesinos (2014).Lagrangian approach to the physical degree of freedom count.Journal of Mathematical Physics55(12), 122901.
- Diaz and
Montesinos (2018)Diaz, B. and M. Montesinos (2018).Geometric lagrangian approach to the physical degree of freedom count
in field theory.Journal of Mathematical Physics59(5), 052901.
- Díez et al. (2020)Díez, V. E., M. Maier, J. A. Méndez-Zavaleta, and M. T. Tehrani
(2020).Lagrangian constraint analysis of first-order classical field
theories with an application to gravity.Physical Review D102(6), 065015.
- Dirac (1958)Dirac, P. A. M. (1958).Generalized hamiltonian dynamics.Proceedings of the Royal Society of London. Series A,
Mathematical and Physical Sciences246, 333–3343.
- Dirac (1964)Dirac, P. A. M. (1964).Lectures on quantum mechanics.Dover Publications.
- Fasso (2005)Fasso, F. (2005).Superintegrable hamiltonian systems: geometry and perturbations.Acta Applicandae Mathematica87(1-3), 93–121.
- Feintzeig (2025)Feintzeig, B. (2025).Quantization and the preservation of structure across theory change.Philosophy of Science92(2), 259–284.
- Feintzeig (2024)Feintzeig, B. H. (2024).Quantization as a categorical equivalence.Letters in Mathematical Physics114(1), 19.
- Feintzeig and
Steeger (2024)Feintzeig, B. H. and J. Steeger (2024).Classical limits of hilbert bimodules as symplectic dual pairs.Reviews in Mathematical Physics36(10), 2450026.
- (27)Gitman, D. and I. V. Tyutin.Quantization of fields with constraints.Springer.
- Gryb (2025)Gryb, S. (2025).Gauge symmetry and the arrow of time: How to count what counts.arXiv preprint arXiv:2509.14720.
- Gryb and
Thébault (2026a)Gryb, S. and K. P. Thébault (2026a).Initial value constraints and the dirac-noether correspondence: A
geometric account.(unpublished).
- Gryb and
Thébault (2016)Gryb, S. and K. P. Y. Thébault (2016).Schrödinger Evolution for the Universe: Reparametrization.Classical and Quantum Gravity33(6), 065004.
- Gryb and
Thébault (2024)Gryb, S. and K. P. Y. Thébault (2024).Time Regained: Volume 1: Symmetry and Evolution in Classical
Mechanics, Volume 1.Oxford University Press.
- Gryb and
Thébault (2026b)Gryb, S. B. and K. P. Thébault (2026b).Against the frozen formalism.(unpublished).
- Halvorson (2012)Halvorson, H. (2012).What scientific theories could not be.Philosophy of Science79(2), 183–206.
- Halvorson (2016)Halvorson, H. (2016).Scientific theories.In P. Humphreys (Ed.),The Oxford Handbook of Philosophy of
Science. Oxford University Press.
- Henneaux and
Teitelboim (1992)Henneaux, M. and C. Teitelboim (1992).Quantization of gauge systems.Princeton University Press.
- Isham (1993)Isham, C. J. (1993).Canonical quantum gravity and the problem of time.InIntegrable systems, quantum groups, and quantum field
theories, pp. 157–287. Springer.
- Kosmann-Schwarzbach (2010)Kosmann-Schwarzbach, Y. (2010).The Noether Theorems: Invariance and Conservation Laws in the
Twentieth Century.Springer Science & Business Media.
- Kuchař (1991)Kuchař, K. V. (1991).The problem of time in canonical quantization of relativistic
systems.In A. Ashtekar and J. Stachel (Eds.),Conceptual Problems of
Quantum Gravity, pp. 141. Boston University Press.
- Landsman (2001)Landsman, N. (2001).Quantized reduction as a tensor product.InQuantization of singular symplectic quotients, pp. 137–180. Springer.
- Landsman (2005)Landsman, N. (2005).Functorial quantization and the guillemin-sternberg conjecture.Twenty years of Bialowieza: a mathematical anthology8,
23–45.
- Lusanna (1990)Lusanna, L. (1990).An enlarged phase space for finite-dimensional constrained systems,
unifying their lagrangian, phase-and velocity-space descriptions.Physics Reports185(1), 1–54.
- Lusanna (1991)Lusanna, L. (1991).The second noether theorem as the basis of the theory of singular
lagrangians and hamiltonians constraints.La Rivista del Nuovo Cimento (1978-1999)14(3),
1–75.
- Nguyen
et al. (2020)Nguyen, J., N. J. Teh, and L. Wells (2020).Why surplus structure is not superfluous.The British Journal for the Philosophy of Science.
- Olver (1991)Olver, P. J. (1991).Applications of Lie groups to differential equations, Volume
107.Springer Science & Business Media.
- Ortega and
Ratiu (2013)Ortega, J.-P. and T. S. Ratiu (2013).Momentum maps and Hamiltonian reduction, Volume 222.Springer Science & Business Media.
- Pitts (2014)Pitts, J. B. (2014).A first class constraint generates not a gauge transformation, but a
bad physical change: The case of electromagnetism.Annals of Physics351, 382–406.
- Pitts (2022)Pitts, J. B. (2022).First-class constraints, gauge transformations, de-ockhamization, and
triviality: Replies to critics, or, how (not) to get a gauge transformation
from a second-class primary constraint.
- Pitts (2024)Pitts, J. B. (2024).Does a second-class primary constraint generate a gauge
transformation? electromagnetisms and gravities, massless and massive.Annals of Physics462, 169621.
- Pons (2005)Pons, J. (2005).On dirac’s incomplete analysis of gauge transformations.Studies In History and Philosophy of Science Part B:
…36, 491.
- Pons
et al. (2010)Pons, J., D. Salisbury, and K. A. Sundermeyer (2010).Observables in classical canonical gravity: folklore demystified.Journal of Physics A: Mathematical and General222(12018).
- Pooley (2017)Pooley, O. (2017).Background independence, diffeomorphism invariance and the meaning of
coordinates.InTowards a theory of spacetime theories, pp. 105–143.
Springer.
- Pooley and
Wallace (2022)Pooley, O. and D. Wallace (2022).First-class constraints generate gauge transformations in
electromagnetism (reply to pitts).
- Read (2024)Read, J. (2024).Background independence in classical and quantum gravity.Oxford University Press.
- Salisbury and
Sundermeyer (2017)Salisbury, D. and K. Sundermeyer (2017).Léon rosenfeld’s general theory of constrained hamiltonian
dynamics.The European Physical Journal H42(1), 23–61.
- Sudarshan and
Mukunda (1974)Sudarshan, E. C. G. and N. Mukunda (1974).Classical dynamics: a modern perspective.World Scientific.
- Sundermeyer (1982)Sundermeyer, K. (1982).Constrained dynamics with applications to Yang-Mills theory,
general relativity, classical spin, dual string model.Springer-Verlag.
- Thébault (2011)Thébault, K. P. Y. (2011, May).Symplectic reduction and the problem of time in nonrelativistic
mechanics.
- Thébault (2026)Thébault, K. P. Y. (2026).Classical and Quantum Phase Space Mechanics.Elements in the Philosophy of Physics. Cambridge: Cambridge
University Press.
- Wallace (2019)Wallace, D. (2019).Observability, redundancy and modality for dynamical symmetry
transformations.
- Weatherall (2018)Weatherall, J. O. (2018).Regarding the ‘hole argument’.The British Journal for the Philosophy of Science69(2), 329–350.
- Weatherall (2019a)Weatherall, J. O. (2019a).Theoretical equivalence in physics: Part 1.Philosophy Compass14(5), e12592.
- Weatherall (2019b)Weatherall, J. O. (2019b).Theoretical equivalence in physics: Part 2.Philosophy Compass14(5), e12591.
- Weinstein (1983)Weinstein, A. (1983).The local structure of poisson manifolds.Journal of differential geometry18(3), 523–557.
- Woodhouse (1997)Woodhouse, N. M. J. (1997).Geometric quantization.Oxford University Press.

## 


- 


Major funding support from
