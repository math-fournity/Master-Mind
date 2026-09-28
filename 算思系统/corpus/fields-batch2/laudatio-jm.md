# **The work of James Maynard Kannan Soundararajan** 

## **Abstract** 

We give a brief account of some of the most spectacular results established by James Maynard, for which he has been awarded the Fields Medal. 

## **Mathematics Subject Classification 2020** 

Primary 11N05; Secondary 11N32, 11N35, 11J83 

## **Keywords** 

distribution of primes, sieve methods, metric Diophantine approximation 

> © 2022 International Mathematical Union Preliminary version, to appear in Proc. Int. Cong. Math. 2022, Vol. 1. DOI 10.4171/ICM2022/212 

James Maynard has established several spectacular results in analytic number theory. While the proofs of these results involve many deep ideas, their statements are remarkable for their simplicity and elegance. To illustrate, we state two such striking results of Maynard concerning prime numbers, before setting them in context. 

**Theorem 1.** _(Maynard_ **[32]** _) For each natural number 𝑚_ ≥ 2 _, there exists a positive integer 𝐶_ ( _𝑚_ ) _with the following property: There are infinitely many natural numbers 𝑛 such that the interval_ [ _𝑛, 𝑛_ + _𝐶_ ( _𝑚_ )] _contains at least 𝑚 prime numbers._ 

**Theorem 2.** _(Maynard_ **[36]** _) There are infinitely many prime numbers 𝑝 whose decimal representation does not contain the digit_ 7 _._ 

**Background.** To place these results in context, recall that the prime number theorem gives an asymptotic for _𝜋_ ( _𝑥_ ), the number of primes below _𝑥_ ; namely, 



We may think of this asymptotic as roughly saying that the “chance" of a number _𝑛_ being prime is about 1/log _𝑛_ . One overarching theme in analytic number theory may be formulated as asking in what ways does the sequence of primes resemble, or differ from, a random sequence of integers with each integer _𝑛_ ≥ 3 chosen independently to be in the random sequence with probability 1/log _𝑛_ (this is also known as the Cramér model). One obvious difference is that all primes larger than 2 must be odd, whereas a random sequence would surely contain many even numbers. But if we could account for divisibility by small primes (such as 2 in our example), would a modified random model describe accurately the behavior of prime numbers? 

There are many ways in which we could try to make this theme precise. For instance, <u>1</u> the Riemann hypothesis predicts that | _𝜋_ ( _𝑥_ ) − li( _𝑥_ )| is bounded by _𝐶_ ( _𝜖_ ) _𝑥_ 2<sup>+</sup><sup>_𝜖_</sup> for any _𝜖>_ 0 and some constant _𝐶_ ( _𝜖_ ). Fluctuations of size about<sup>~~√~~</sup> _<u>𝑥</u>_ are indeed what one would expect if we select random sets of integers with _𝑛_ ≥ 3 included in the set with probability 1/log _𝑛_ . Thus the Riemann hypothesis is, at a crude level, consistent with a random model of primes, although if we inspect the error term _𝜋_ ( _𝑥_ ) − li( _𝑥_ ) in finer detail then the influence of zeros of _𝜁_ ( _𝑠_ ) would be visible, and such features would deviate (in small but significant ways) from the random model. 

At the 1912 ICM, Landau posed four “unattackable" problems on primes: (i) the Goldbach problem that every even integer larger than 2 is the sum of two primes, (ii) the twin prime problem that there are infinitely many prime pairs _𝑛_ and _𝑛_ + 2, (iii) there is always a prime between two consecutive squares, and (iv) there are infinitely many primes of the form _𝑛_<sup>2</sup> + 1. All four problems remain open today, and all statements are exactly what one would expect for random sequences. For example, the Cramér model would suggest that the chance that _𝑛_ and _𝑛_ + 2 are both “prime" is about 1/log _𝑛_ × 1/log( _𝑛_ + 2), which would predict about _𝑥_ /(log _𝑥_ )<sup>2</sup> twin primes up to _𝑥_ . Of course some care is needed, since the same prediction could be made for _𝑛_ and _𝑛_ + 1 being prime, and we will address this soon. Similarly, we may expect that an even number _𝑁_ may have about _𝑁_ /(log _𝑁_ )<sup>2</sup> representations as a sum of two 

**2 K. Soundararajan** 

primes, making the Goldbach conjecture very plausible, and related arguments suggest the last two Landau problems as well. 

For the third Landau problem on the number of primes between _𝑛_<sup>2</sup> and ( _𝑛_ + 1)<sup>2</sup> , the random model already predicts what we believe to be the right answer — namely, there should be about (2 _𝑛_ + 1)/log( _𝑛_<sup>2</sup> ) ≈ _𝑛_ /log _𝑛_ primes in this interval. For the other three problems, some modification must be made to the Cramér model, to take into account the deterministic features of these problems with respect to divisibility by small primes. Precise conjectures for these problems were first made by Hardy and Littlewood motivated by their work on the circle method. These conjectures are widely believed to be true, and are supported by extensive heuristic and numerical evidence. For instance, Hardy and Littlewood formulated the following conjecture for the number of twin primes below _𝑥_ : 



Here ∫2 _𝑥_<sup>_𝑑𝑡_/(log</sup><sup>_𝑡_)2isasymptotically</sup><sup>_𝑥_/(log</sup><sup>_𝑥_)2,andcorrespondstothepredictionofthe</sup> Cramér model, while 𝔖({0 _,_ 2}), known as the _singular series_ , is a correction factor 



The constant 𝔖({0 _,_ 2}) has a compelling probabilistic interpretation: it is a product over all primes _𝑝_ (the first factor 2 corresponds to the prime _𝑝_ = 2), with the factor at _𝑝_ keeping track of the ratio between the chance that _𝑛_ and _𝑛_ + 2 are not divisible by _𝑝_ , and the chance that two random numbers are not divisible by _𝑝_ . Thus, for _𝑝_ = 2, the chance that _𝑛_ and _𝑛_ + 2 are both not divisible by 2 is (1 − 1/2) ( _𝑛_ must be odd), while the chance that two random numbers are both not divisible by 2 is (1 − 1/2)<sup>2</sup> = 1/4; the ratio of these chances gives the correction factor 2. For primes _𝑝_ ≥ 3, the chance that _𝑛_ and _𝑛_ + 2 are both not divisible by _𝑝_ is (1 − 2/ _𝑝_ ) whereas the chance that two random numbers are both not divisible by _𝑝_ is (1 − 1/ _𝑝_ )<sup>2</sup> , and we see the corresponding correction factor in the definition of 𝔖({0 _,_ 2}). 

Similar conjectures can be made for the binary Goldbach problem, or for the number of primes of the form _𝑛_<sup>2</sup> + 1, modifying and correcting the naive predictions of the Cramér model. To illustrate, we give a generalization of the conjecture for twin primes for counting prime _𝑘_ -tuples: given distinct integers _ℎ_ 1, _ℎ_ 2, _. . ._ , _ℎ𝑘_ , for large _𝑥_ how many integers _𝑛_ ≤ _𝑥_ are there with _𝑛_ + _ℎ_ 1, _. . ._ , _𝑛_ + _ℎ𝑘_ all being prime. Here the Hardy–Littlewood conjecture predicts that 



where, with H = { _ℎ_ 1 _, . . . , ℎ𝑘_ }, 



and _𝜈_ (H _, 𝑝_ ) denotes the number of distinct residue classes occupied by the set H viewed mod _𝑝_ . Since _𝜈_ (H _, 𝑝_ ) = _𝑘_ if _𝑝_ is larger than max | _ℎ𝑖_ − _ℎ 𝑗_ |, the product defining 𝔖(H) converges absolutely to a non-negative real number, and it equals zero only if _𝜈_ (H _, 𝑝_ ) = 

**3 The work of James Maynard** 

_𝑝_ for some prime _𝑝_ . If _𝜈_ (H _, 𝑝_ ) = _𝑝_ , then for any integer _𝑛_ at least one of the numbers _𝑛_ + _ℎ_ 1 _, . . . , 𝑛_ + _ℎ𝑘_ would be a multiple of _𝑝_ , and therefore there can be only finitely many integers _𝑛_ with _𝑛_ + _ℎ_ 1, _. . ._ , _𝑛_ + _ℎ𝑘_ all being prime; for example this is what happens if we ask for _𝑛_ and _𝑛_ + 1 to be prime, or _𝑛_ , _𝑛_ + 2, _𝑛_ + 4 all to be prime. When there is no such divisibility obstruction to _𝑛_ + _ℎ_ 1, _. . ._ , _𝑛_ + _ℎ𝑘_ all being prime, the Hardy–Littlewood conjecture predicts a rich supply of such prime _𝑘_ -tuples. This is perhaps the most central question in prime number theory, and remains open in any situation where 𝔖(H) is non-zero. 

**Sieve theory.** We have described quickly some of the main motivating questions in the theory of primes. One main source of progress towards these questions is _sieve theory_ , and a large part of Maynard’s work lies broadly in this area. A typical problem in sieve theory is to bound the size of sets of integers A whose elements are constrained to omit _𝜈_ ( _𝑝_ ) given residue classes mod _𝑝_ for primes _𝑝_ . For instance the twin prime problem is of this form, as we seek to find integers _𝑛_ that are neither 0 nor −2 mod _𝑝_ for all primes _𝑝_ ≤ ~~√~~ _𝑛_ + 2 (so that _𝑛_ and _𝑛_ + 2 would both be prime). In great generality sieve methods can produce upper bounds of the conjectured order of magnitude; for example, one can show that the number of twin primes up to _𝑥_ is no more that 4 times the conjectured Hardy–Littlewood asymptotic. Producing corresponding lower bounds has proved to be a much harder problem, but sieve methods have led to striking partial results such as Chen’s theorem that there are many primes _𝑝_ for which _𝑝_ + 2 has at most two prime factors, or Iwaniec’s theorem that there are many _𝑛_ for which _𝑛_<sup>2</sup> + 1 has at most two prime factors. For a comprehensive treatment of the subject, see **[14]** . 

Chen’s theorem and Iwaniec’s theorem exhibit a limitation of traditional sieve methods, known as the _parity problem_ , which often prevents us from knowing the parity of elements left unsieved, and thus from producing prime numbers. But in some special cases, sieve methods in conjunction with other analytic input have produced prime numbers. For instance, for large _𝑥_ Baker, Harman, and Pintz **[2]** showed that the interval [ _𝑥,𝑥_ + _𝑥_<sup>_𝜃_</sup> ] contains at least _𝑐𝑥_<sup>_𝜃_</sup> /log _𝑥_ primes, where _𝑐>_ 0 is a constant and _𝜃_ = 0 _._ 525; the Landau problem of producing primes between consecutive squares corresponds to intervals with _𝜃_ =<sup><u>1</u></sup> 2<sup>. Another</sup> spectacular example is due to Friedlander and Iwaniec **[13]** who established an asymptotic formula for the number of primes up to _𝑥_ that may be written as _𝑛_<sup>2</sup> + _𝑚_<sup>4</sup> , an approximation to the Landau problem of primes of the form _𝑛_<sup>2</sup> + 1. A closely related result of Heath-Brown and Li **[25]** produces an asymptotic formula for primes of the form _𝑛_<sup>2</sup> + _𝑝_<sup>4</sup> , where _𝑝_ is prime. Yet another beautiful result due to Heath-Brown **[24]** establishes an asymptotic formula for the number of primes below _𝑥_ of the form _𝑛_<sup>3</sup> + 2 _𝑚_<sup>3</sup> with _𝑚, 𝑛_ ∈ N. Heath-Brown’s result may be viewed as an approximation to the problem of producing primes of the form _𝑛_<sup>3</sup> + 2, but before his work it was not even known if there are infinitely many primes that are the sum of three cubes of natural numbers! A crucial feature of these results is that they deal with primes represented by specializations of _norm forms_ . The Friedlander–Iwaniec result is concerned with the norm form _𝑥_<sup>2</sup> + _𝑦_<sup>2</sup> = _𝑁_ ( _𝑥_ + _𝑖𝑦_ ) associated to the field Q( _𝑖_ ), and specializing _𝑦_ to be a square; Heath-Brown’s result is concerned with the norm form _𝑁_ ( _𝑥_ + _𝑦𝛼_ + _𝑧𝛼_<sup>2</sup> ) taking the <u>1</u> norm over the field Q( _𝛼_ ) with _𝛼_ = 2 3 , and specializing _𝑧_ to be 0. The results of Friedlander– 

**4 K. Soundararajan** 

Iwaniec and Heath-Brown gave the first examples of thin sequences (in the sense that the number of integers below _𝑋_ in the sequence is ≤ _𝑋_<sup>1−</sup><sup>_𝛿_</sup> for some _𝛿>_ 0) of polynomial values in two or more variables that represent infinitely many primes; no example is known of a polynomial in 1 variable of degree more than 1 that represents infinitely many primes. 

Maynard’s work **[40]** gives a substantial generalization of Heath-Brown’s approach, and produces many further examples of thin sequences of polynomial values in many variables that represent primes. Consider an algebraic number _𝜔_ ∈ C of degree _𝑛_ , and let _𝐾_ denote the field Q( _𝜔_ ). We can associate to this the norm form _𝑁_ (<sup>�</sup> _𝑖_<sup>_𝑛_</sup> =1<sup>_𝑥𝑖𝜔𝑖_−1), which is a</sup> homogeneous polynomial of degree _𝑛_ in the variables _𝑥_ 1, _. . ._ , _𝑥𝑛_ . A thin polynomial in many variables would be obtained by specializing some of the variables in this norm form to be zero; say, we set _𝑥𝑛_ − _𝑘_ +1, _. . ._ , _𝑥𝑛_ = 0, and the number integers below _𝑥_ represented by such an incomplete norm form would be about _𝑥_<sup>1−</sup><sup>_𝑘_/</sup><sup>_𝑛_</sup> . In the range _𝑛_ ≥ 4 _𝑘_ , Maynard establishes an asymptotic formula for the number of primes represented by such an incomplete norm form, when the variables _𝑥_ 1, _. . ._ , _𝑥𝑛_ − _𝑘_ take integer values in the range [1 _, 𝑋_ ]. 

**The circle method.** Apart from sieve theory, another important source of progress towards problems on primes is the _circle method_ , which as we already mentioned formed the original motivation for Hardy and Littlewood in formulating their conjectures. To illustrate, consider the Goldbach problem of representing an even integer _𝑁_ as a sum of two primes. Using Fourier analysis, the number of such representations of _𝑁_ may be written as 



The idea in the circle method is that generating functions such as _𝑆_ ( _𝛼_ ) above tend to be large near rational numbers with small denominator (the _major arcs_ ) and small away from them (the _minor arcs_ ). 

While the circle method has not been able to tackle the binary Goldbach problem or the problem of twin primes, it has been extremely effective in problems where there is a bit more freedom. For instance, the ternary Goldbach problem asks to represent odd numbers as a sum of three primes, and there is one extra variable to play with here. Vinogradov famously used the circle method to show that all large odd numbers are the sum of three primes, and Helfgott **[26]** has extended this to show that all odd numbers larger than 5 may be so represented. Here we may mention an impressive result of Matomäki, Maynard, and Shao **[30]** which shows that large odd numbers _𝑛_ may be expressed as _𝑝_ 1 + _𝑝_ 2 + _𝑝_ 3, where all three primes _𝑝𝑖_ lie in a short interval [ _𝑛_ /3 − _𝑛_<sup>_𝜃_</sup> _, 𝑛_ /3 + _𝑛_<sup>_𝜃_</sup> ] for any _𝜃>_ 11/20. We mentioned earlier the work of Baker, Harman and Pintz **[2]** showing the existence of primes in short intervals [ _𝑥, 𝑥_ + _𝑥_<sup>0</sup><sup>_._525</sup> ], and the work of **[30]** is remarkable in solving the ternary Goldbach problem using primes in only slightly longer intervals. 

A second example of what it might mean to have an extra degree of freedom is the Green–Tao theorem that the primes contain arbitrarily long arithmetic progressions _𝑛_ , _𝑛_ + _𝑑_ , _. . ._ , _𝑛_ + ( _𝑘_ − 1) _𝑑_ . The Hardy–Littlewood conjecture would predict a stronger “one dimensional” version of such a result with specified choices for the common difference _𝑑_ ; for instance, there should be infinitely many _𝑘_ -tuples primes of the form _𝑛_ , _𝑛_ + _𝑘_ !, _𝑛_ + 2 · _𝑘_ !, 

**5 The work of James Maynard** 

_. . ._ , _𝑛_ + ( _𝑘_ − 1) · _𝑘_ !. The work of Green, Tao, and Ziegler **[19–21]** may be thought of as a farreaching generalization of the circle method, obtaining asymptotic formulae for the number of prime solutions to linear systems with at “least two degrees of freedom.” 

Maynard’s beautiful result on primes with missing digits (Theorem 2 stated above) is a rare occasion where the circle method can be used to solve a binary problem. Let M denote the set of natural numbers with no 7 in their decimal expansion (naturally one could omit any other digit instead of 7). The number of integers in M up to _𝑁_ is about _𝑁_<sup>log 9/log 10</sup> = _𝑁_<sup>1−</sup><sup>_𝛿_</sup> with _𝛿_ = 0 _._ 046 _. . ._ , so that M is a thin set making the problem of finding primes in it a challenge. Before Maynard’s work, Dartyge and Mauduit **[7,8]** had used sieve theory to show that M contains integers with at most two prime factors. To count the number of primes in M up to _𝑁_ , we use Fourier analysis writing this as 



where _𝑆_ ( _𝛼_ ) is the exponential sum over primes defined in (3), and _𝑀_ ( _𝛼_ ) =<sup>�</sup> _𝑚_ ≤ _𝑁,𝑚_ ∈M<sup>_𝑒_2</sup><sup>_𝜋𝑖𝛼_</sup> is the corresponding exponential sum over the set M. Usually such a binary problem is hopeless to attack via the circle method — the reason being that even most optimistically we may only expect “square-root cancellation” in the exponential sums _𝑆_ ( _𝛼_ ) and _𝑀_ (− _𝛼_ ) for <u>1 1</u> generic _𝛼_ , and even that would produce an integrand of size _𝑁_ 2 × _𝑁_ 2<sup>(1−</sup><sup>_𝛿_)</sup> , which is bigger than the expected main term of size about _𝑁_<sup>1−</sup><sup>_𝛿_</sup> /log _𝑁_ . A crucial feature in this problem is that the set M has a very convenient structure which results in the exponential sum _𝑀_ ( _𝛼_ ) often being unusually small. For instance, Maynard shows that its _𝐿_<sup>1</sup> -norm satisfies 



with the key point being that the exponent 0 _._ 32 is smaller even than (1 − _𝛿_ )/2, which is the optimistic square-root cancellation that we mentioned. Such estimates raise the hope of being able to attack Theorem 2, and the main idea can be seen transparently in Maynard’s expository article **[35]** , where he proves an easier version of Theorem 2 treating primes missing a digit in base _𝑏_ with _𝑏_ sufficiently large. The set of integers up to _𝑁_ missing a digit in base _𝑏_ has size about _𝑁_<sup>log(</sup><sup>_𝑏_−1)/log</sup><sup>_𝑏_</sup> , and so the problem becomes easier as the base _𝑏_ gets larger. Getting the base down to 10 turns out to be a fiendishly difficult problem, and is arguably more significant psychologically than for any mathematical reason. Maynard **[36]** tackles this brilliantly by introducing a number of new ideas, including ideas from the geometry of numbers, different aspects of sieve theory, and comparisons with a Markov process. We may expect that even in base 3 there should be infinitely many primes with a given digit missing; in base 2, the only digit that might be omitted is 0, and we find the problem of whether there are infinitely many Mersenne primes, which lies beyond reasonable mathematics. We close this discussion by pointing out two other beautiful results on the digits of prime numbers which have elements in common with Maynard’s work: namely, work of Mauduit and Rivat **[31]** which shows (in particular) that the sum of the decimal digits of primes is equally likely to be odd or even, and work of Bourgain **[6]** which allows one to specify a small proportion of the binary digits of primes. 

**6 K. Soundararajan** 

**Gaps between primes.** We now turn to a discussion of Maynard’s most spectacular result — the sun amidst small stars — namely, Theorem 1 above on finding many primes in bounded intervals. To describe the recent history of this problem, let us first discuss how primes are spaced typically. The prime number theorem tells us that the _𝑛_ -th prime _𝑝𝑛_ is about _𝑛_ log _𝑛_ , so that the average spacing between two consecutive primes, _𝑝𝑛_ +1 − _𝑝𝑛_ , is about log _𝑝𝑛_ . What is the distribution of the normalized spacings ( _𝑝𝑛_ +1 − _𝑝𝑛_ )/log _𝑝𝑛_ ? The Cramér random model for primes would predict that these normalized spacings should behave like a Poisson process, and that for any fixed interval [ _𝛼, 𝛽_ ] ∈ R≥0 



Gallagher **[16]** showed that this prediction is also implied by the more refined Hardy– Littlewood conjectures, the key point being that the singular series constants 𝔖(H) (see (2)) are approximately 1 (matching the naive Cramér model) on average over _𝑘_ -element sets H . 

This conjecture on the normalized spacings between primes is wide open. Indeed if we denote by L the set of limit points of ( _𝑝𝑛_ +1 − _𝑝𝑛_ )/log _𝑝𝑛_ , then even the qualitative statement that L = [0 _,_ ∞] (which follows at once from (4)) is currently unknown. By creating long strings of composite numbers, Westzynthius established that L contains ∞, but for a long time no other limit point was known (although Erdős and Ricci had established that L has positive Lebesgue measure). Dramatic progress was made in the 2005 with the pathbreaking work of Goldston, Pintz, and Yıldırım **[17]** , who showed that for any _𝜖>_ 0 there are infinitely many _𝑛_ with _𝑝𝑛_ +1 − _𝑝𝑛_ ≤ _𝜖_ log _𝑝𝑛_ . Thus there are small gaps between primes in comparison to the average, and 0 is now known to be in L. Before the work of Goldston, Pintz, and Yıldırım,it wasonly knownthat thedifferencebetween consecutiveprimes became smaller than about 4<sup><u>1</u>of the average spacing, and their work opened the door to later advances</sup> including Maynard’s Theorem 1. 

Suppose _ℎ_ 1, _. . ._ , _ℎ𝑘_ are distinct integers with 𝔖({ _ℎ_ 1 _, . . . , ℎ𝑘_ }) _>_ 0; such tuples are called _admissible_ , and for example { _𝑘_ ! _,_ 2 · _𝑘_ ! _, . . . , 𝑘_ · _𝑘_ !} is admissible. The Hardy– Littlewood conjecture predicts that there are infinitely many _𝑛_ with _𝑛_ + _ℎ_ 1, _. . ._ , _𝑛_ + _ℎ𝑘_ all being prime. Instead of wanting all _𝑘_ of these numbers to be prime, what if we only ask for at least two of them to be prime? This would already show that infinitely often there are bounded gaps between consecutive prime numbers. Suppose we could find non-negative weights _𝑤_ ( _𝑛_ ) with the property that for large _𝑥_ and each _𝑗_ = 1, _. . ._ , _𝑘_ , 



Then summing (5) over all _𝑗_ = 1, _. . ._ , _𝑘_ we would obtain 



from which it would follow that there must be some _𝑛_ with at least 2 primes among _𝑛_ + _ℎ_ 1, _. . ._ , _𝑛_ + _ℎ𝑘_ . Thinking of the weights as giving a probability measure on _𝑥_ ≤ _𝑛_ ≤ 2 _𝑥_ , we may 

**7 The work of James Maynard** 

interpret (6) as saying that the expected number of primes among the _𝑛_ + _ℎ 𝑗_ is greater than 1, so that there must be _𝑛_ with at least 2 primes in this _𝑘_ -tuple. 

The difficult problem is to construct weights satisfying (5), and natural choices for such weights are suggested by sieve theory, in particular the theory of the Selberg sieve. The standard choice of Selberg sieve weights (which are used to give an upper bound for the number of prime _𝑘_ -tuples _𝑛_ + _ℎ_ 1, _. . ._ , _𝑛_ + _ℎ𝑘_ ) takes the shape 



Clearly _𝑤_ ( _𝑛_ ) ≥ 0 always. Expanding out the sum, the right side of (5) (the sum over all _𝑛_ ∈[ _𝑥,_ 2 _𝑥_ ]) may be evaluated asymptotically so long as _𝑅_<sup>2</sup> ≤ _𝑥_<sup>1−</sup><sup>_𝜖_</sup> . The left side of (5) is more involved, and relies on understanding the distribution of primes in arithmetic progressions with the modulus of the progression going up to _𝑅_<sup>2</sup> . The Bombieri–Vinogradov theorem permits such an understanding (at a level comparable to what the Generalized Rie- <u>1</u> mann Hypothesis would give) so long as _𝑅_<sup>2</sup> ≤ _𝑥_ 2<sup>−</sup><sup>_𝜖_</sup> , so that _𝑅_ is now constrained to be <u>1</u> ≤ _𝑥_ 4<sup>−</sup><sup>_𝜖_</sup> . For this choice of weights, the expected number of primes among the _𝑛_ + _ℎ 𝑗_ turns out to be about (2 _𝑘_ /( _𝑘_ + 1)) log _𝑅_ /log _𝑥_ , so that with _𝑅_ ≤ _𝑥_<sup>1/4−</sup><sup>_𝜖_</sup> one only expects to find<sup><u>1</u></sup> 2 a prime in the _𝑘_ -tuple. 

Although the Selberg sieve weights described above had been optimized for upper bounds in the prime _𝑘_ -tuple problem, Goldston, Pintz, and Yıldırım made the surprising discovery that there are better choices of weights for optimizing the ratio of the sums in (5). They considered weights of the form 



for a suitable parameter _ℓ_ , which turns out in the optimal case to be around ~~√~~ _𝑘_ . With this choice of weights, they found that the expected number of primes among _𝑛_ + _ℎ 𝑗_ is about <u>1 1</u> twice as large as previously, being (4 + _𝑂_ (1/ _𝑘_ 2 )) log _𝑅_ /log _𝑥_ . With _𝑅_ = _𝑥_ 4<sup>−</sup><sup>_𝜖_</sup> , this barely fails to give the desired relation (5), and thus barely falls short of proving bounded gaps between primes. By considering an additional possible prime value _𝑛_ + _ℎ_ for 1 ≤ _ℎ_ ≤ _𝜖_ log _𝑥_ , Goldston, Pintz, Yıldırım were able to deduce from this argument that there are infinitely many _𝑛_ with _𝑝𝑛_ +1 − _𝑝𝑛_ ≤ _𝜖_ log _𝑛_ . For a more detailed discussion of these ideas see **[47]** . 

<u>1</u> If one could take _𝑅_ to be _𝑥_ 4<sup>+</sup><sup>_𝛿_</sup> for any _𝛿>_ 0, then the argument of Goldston, Pintz, and Yıldırım would give bounded gaps between primes. To take such a value for _𝑅_ , one would need to understand the distribution of primes up to _𝑥_ in arithmetic progressions, when <u>1</u> the modulus of the progression is as large as _𝑥_ 2<sup>+2</sup><sup>_𝛿_</sup> . The Elliott–Halberstam conjectures predict that such results should hold (on average) when the modulus is as large as _𝑥_<sup>1−</sup><sup>_𝜖_</sup> . Partial progress towards such extensions of the Bombieri–Vinogradov theorem was made by Fouvry and Iwaniec **[12]** , and Bombieri, Friedlander, and Iwaniec **[5]** , but these results did not apply immediately to the problem of showing bounded gaps between primes. In April 2013, Yitang Zhang **[49]** made a spectacular breakthrough by establishing a version of the 

**8 K. Soundararajan** 

Bombieri–Vinogradov theorem in an extended range which was sufficient for the method of Goldston, Pintz, and Yıldırım. Zhang established that if _𝑘>_ 3 _._ 5 × 10<sup>6</sup> then for any admissible _𝑘_ -tuple _ℎ_ 1, _. . ._ , _ℎ𝑘_ there are infinitely many _𝑛_ with at least two of the _𝑛_ + _ℎ 𝑗_ being prime. This implied that infinitely often the gaps between consecutive primes is less than 70 million. Refinements of Zhang’s work on the equidistribution of primes in arithmetic progressions were made by the Polymath project **[46]** , and still further qualitative and quantitative refinements of such results may be found in the recent papers of Maynard **[37–39]** . 

Zhang’s work established the case _𝑚_ = 2 of Theorem 1. However, even if one could <u>1</u> take the largest possible range for _𝑅_ , namely _𝑅_ = _𝑥_ 2<sup>−</sup><sup>_𝜖_</sup> (which would be permitted by the Elliott–Halberstam conjecture), the Goldston–Pintz–Yıldırım weights would only yield that the expected number of primes in an admissible _𝑘_ -tuple is ≥ 2 − _𝜖_ . In other words, even under the Elliott–Halberstam conjecture one would fall short of establishing the existence of three primes in bounded intervals. 

The proof of Theorem 1 is based on a different choice of the weights _𝑤_ ( _𝑛_ ), discovered just months after Zhang’s work by Maynard (who announced the results in a memorable talk at Oberwolfach in October 2013) and independently by Tao (in unpublished work). The Maynard–Tao weights are a multi-dimensional extension of the weights considered earlier, and take (roughly speaking) the shape 



for suitable smooth functions _𝐹_ : [0 _,_ 1]<sup>_𝑘_</sup> → R. Astonishingly it turns out that for an appropriate choice for _𝐹_ , the expected number of primes in the tuple _𝑛_ + _ℎ_ 1, _. . ._ , _𝑛_ + _ℎ𝑘_ (recall (6) above) is ≥ _𝑐_ log _𝑘_<sup>lo</sup> log<sup><u>g</u></sup><sup>_𝑅_</sup> _𝑥_<sup>, for a positive constant</sup><sup>_𝑐_; in fact</sup><sup>_𝑐_may be taken close to 1 if</sup><sup>_𝑘_is large</sup> enough. The key point is that this expected number of primes in _𝑘_ -tuples tends to infinity with _𝑘_ , and in fact we only need _𝑅_ to grow like any power of _𝑥_ for the method to succeed, so <u>1</u> that Bombieri–Vinogradov which permits _𝑅_ = _𝑥_ 4<sup>−</sup><sup>_𝜖_</sup> is already sufficient! Thus the following more precise version of Theorem 1 holds, which may be viewed as a partial result towards the Hardy–Littlewood prime _𝑘_ -tuples conjecture. 

**Theorem 3** (Maynard **[32]** ). _Let 𝑚_ ≥ 2 _be a natural number. Let 𝑘 be sufficiently large in terms of 𝑚, and let_ H = { _ℎ_ 1 _, . . . , ℎ𝑘_ } _be any set of 𝑘 integers with_ 𝔖(H) _>_ 0 _. Then there exist infinitely many 𝑛 such that the 𝑘-tuple 𝑛_ + _ℎ_ 1 _, . . ., 𝑛_ + _ℎ𝑘 contains at least 𝑚 primes._ 

Maynard showed that _𝑘_ may be taken smaller than _𝐶𝑚_<sup>2</sup> _𝑒_<sup>4</sup><sup>_𝑚_</sup> for a suitable constant _𝐶_ , and further refinements of this (incorporating also the work of Zhang) have been made in the work of Baker and Irving **[3]** who showed that _𝑘_ may be taken as _𝐶𝑒_<sup>3</sup><sup>_._815</sup><sup>_𝑚_</sup> . Of special interest is the case _𝑚_ = 2 where the Polymath project **[45]** optimized these arguments to establish that any admissible 50-tuple contains 2 primes infinitely often. In particular, they showed that _𝑝𝑛_ +1 − _𝑝𝑛_ ≤ 246 infinitely often, and conditional on the Elliott–Halberstam conjecture that infinitely often there are at least two primes in the triple _𝑛_ , _𝑛_ + 2, _𝑛_ + 6. Let us mention one other uniform variant of these results: Maynard **[33]** shows, for instance, that there are at least 

**9 The work of James Maynard** 

_𝑐𝑋_ exp(− ~~√~~ log _𝑋_ ) values of _𝑥_ ∈[ _𝑋,_ 2 _𝑋_ ] such that the interval [ _𝑥, 𝑥_ + log _𝑋_ ] contains at least _𝑐_ log log _𝑋_ primes (here _𝑐_ is a positive constant). For detailed expositions on these results of Zhang, Maynard, and Tao, see **[18, 29]** . 

The Maynard–Tao weights offer a flexible new method to study many problems on primes and related sequences, and have found a number of applications. We describe two other results using these weights, both still concerned with spacings between consecutive primes. We referred earlier to the result of Westzynthius on large gaps between consecutive primes, which showed that ∞ lies in the set L of limit points of the normalized spacings ( _𝑝𝑛_ +1 − _𝑝𝑛_ )/log _𝑝𝑛_ . This was quantified in the 1930’s by Erdős and Rankin who showed that, for a positive constant _𝐶_ 



The random model would suggest that the maximal gap between primes up to _𝑋_ should be about (log _𝑋_ )<sup>2</sup> . This is known as Cramér’s conjecture, and while this is very delicate, it is widely believed that the maximal gap is no more than (log _𝑋_ )<sup>2+</sup><sup>_𝜖_</sup> , although even this is far beyond Landau’s unattackable problem of the existence of a prime between consecutive squares. Erdős drew attention to the problem of finding larger gaps between consecutive primes, offering $ 10 000 for a bound that would replace _𝐶_ in (7) with a function tending to ∞ with _𝑋_ . For more than 75 years, this problem resisted attack, with only improvements of the constant _𝐶_ being known. Then, by a remarkable coincidence, in 2014 _two_ different techniques emerged, both establishing (7) with _𝐶_ replaced by a function tending to infinity with _𝑋_ . One approach, by Ford, Green, Konyagin, and Tao **[11]** , built upon the work of Green–Tao on arithmetic progressions in the primes, while the other approach, by Maynard **[34]** , found a way to adapt the Maynard–Tao sieve weights. The second approach was better suited for quantifying the large gaps that are produced, and, joining forces, Ford, Green, Konyagin, Maynard, and Tao **[10]** established that for some constant _𝐶>_ 0 



improving the bound in (7) by a factor of log log log _𝑋_ . 

The results on small gaps and large gaps between consecutive primes show that 0 and ∞ lie in the set L of limit points of the normalized prime spacings. No other explicit numbers are known to lie in L, although we expect L to include all non-negative real numbers. Following Zhang’s breakthrough, Pintz **[42]** showed that L contains an interval [0 _, 𝑐_ ] for some _𝑐>_ 0, which however is ineffective and cannot be computed explicitly. Using the Maynard–Tao sieve weights, Banks, Freiberg, and Maynard **[4]** established the following beautiful result: If _𝛽_ 1 ≤ _𝛽_ 2 ≤ _. . ._ ≤ _𝛽_ 9 are any nine real numbers, then at least one of their differences _𝛽 𝑗_ − _𝛽𝑖_ (with _𝑖< 𝑗_ ) must be an element of L. Their result has been refined by Pintz **[43]** , and Merikoski **[41]** , and Merikoski shows that the same result holds if we start with just four real numbers _𝛽_ 1 ≤ _𝛽_ 2 ≤ _𝛽_ 3 ≤ _𝛽_ 4. Moreover, Merikoski has also shown that for any _𝑇>_ 0, the set L ∩[0 _,𝑇_ ] has measure at least _𝑇_ /3. 

**10 K. Soundararajan** 

**The Duffin–Schaeffer conjecture.** So far we have focussed entirely on Maynard’s work concerned with prime numbers. In a very different direction, Maynard in joint work with Koukoulopoulos **[28]** , resolved one of the central problems in the metric theory of Diophantine approximation, known as the Duffin–Schaeffer conjecture. 

Diophantine approximation is concerned with finding rational approximations _𝑎_ / _𝑞_ to a given irrational number _𝛼_ , with an emphasis on making | _𝛼_ − _𝑎_ / _𝑞_ | small in terms of _𝑞_ . The most basic result is Dirichlet’s theorem that for every irrational number _𝛼_ , there are infinitely many rational approximations _𝑎_ / _𝑞_ , with _𝑎_ ∈ Z, _𝑞_ ∈ N and ( _𝑎, 𝑞_ ) = 1 (so that the fraction is in reduced form) such that | _𝛼_ − _𝑎_ / _𝑞_ | ≤ 1/ _𝑞_<sup>2</sup> . For quadratic irrationals (like √2 or the golden ratio), Dirichlet’s theorem is essentially the best possible, and for every such _𝛼_ there exists a positive constant _𝐶_ ( _𝛼_ ) such that | _𝛼_ − _𝑎_ / _𝑞_ | ≥ _𝐶_ ( _𝛼_ )/ _𝑞_<sup>2</sup> for any rational approximation _𝑎_ / _𝑞_ . A celebrated result of Roth establishes that for any algebraic irrational _𝛼_ and any _𝜖>_ 0 one has | _𝛼_ − _𝑎_ / _𝑞_ | ≥ _𝐶_ ( _𝛼, 𝜖_ )/ _𝑞_<sup>2+</sup><sup>_𝜖_</sup> , for a suitable positive constant _𝐶_ ( _𝛼, 𝜖_ ). For particular interesting transcendental numbers, such as _𝜋_ , it remains an outstanding open problem to determine how well they can be approximated by rational numbers. 

Metric Diophantine approximation is concerned with such approximation problems that hold for _almost all_ irrational numbers _𝛼_ , with _almost all_ interpreted in the sense of Lebesgue measure. Since the problem of approximating _𝛼_ by rationals is identical to that of approximating _𝛼_ + 1, we may restrict attention to irrational numbers _𝛼_ ∈[0 _,_ 1). The most basic problem is the following: suppose _𝜓_ : N → R≥0 is a given function, what can be said about the measure of _𝛼_ ∈[0 _,_ 1) for which there exist infinitely many rational numbers _𝑎_ / _𝑞_ in reduced form (that is, ( _𝑎, 𝑞_ ) = 1) with | _𝛼_ − _𝑎_ / _𝑞_ | ≤ _𝜓_ ( _𝑞_ ). For instance, Dirichlet’s theorem tells us that if _𝜓_ ( _𝑞_ ) = 1/ _𝑞_<sup>2</sup> , then all irrational _𝛼_ ∈[0 _,_ 1) admit infinitely many such rational approximations. 

Let A _𝑞_ = A _𝑞_ ( _𝜓_ ) denote the set of _𝛼_ ∈[0 _,_ 1) for which there exists some reduced fraction _𝑎_ / _𝑞_ with | _𝛼_ − _𝑎_ / _𝑞_ | ≤ _𝜓_ ( _𝑞_ ), and let A denote the set of _𝛼_ ∈[0 _,_ 1) lying in infinitely many of the sets A _𝑞_ . Thus 



Now the measure of A _𝑞_ is ≤ 2 _𝜙_ ( _𝑞_ ) _𝜓_ ( _𝑞_ ), since there are _𝜙_ ( _𝑞_ ) possible choices for the numerator _𝑎_ , and if _𝜓_ ( _𝑞_ ) ≤ 1/(2 _𝑞_ ) so that the intervals for different _𝑎_ do not overlap then equality holds here. If<sup>�∞</sup> _𝑞_ =1<sup>_𝜙_(</sup><sup>_𝑞_)</sup><sup>_𝜓_(</sup><sup>_𝑞_) converges, then the measure of</sup> A(<sup>�</sup> _𝑄_ ) is bounded by 2<sup>�∞</sup> _𝑞_ = _𝑄_<sup>_𝜙_(</sup><sup>_𝑞_)</sup><sup>_𝜓_(</sup><sup>_𝑞_), which is the tail of a convergent series and thus tends to 0 as</sup><sup>_𝑄_→∞. It</sup> follows that A has measure 0. This argument is identical to the easy part of the Borel–Cantelli Lemma. 

In 1941, Duffin and Schaeffer made the remarkable conjecture that in the complementary case when<sup>�∞</sup> _𝑞_ =1<sup>_𝜙_(</sup><sup>_𝑞_)</sup><sup>_𝜓_(</sup><sup>_𝑞_)diverges,themeasureofAis1.Sincethenthe</sup> Duffin–Schaeffer conjecture has remained one of the central motivating questions in the theory of metric Diophantine approximations. A number of partial results towards this conjecture were established: for example, a beautiful result of Gallagher **[15]** showed that the measure of the set A( _𝜓_ ) is always either 0 or 1, work of Erdős **[9]** and Vaaler **[48]** established 

**11 The work of James Maynard** 

the conjecture when _𝜓_ ( _𝑞_ ) is _𝑂_ (1/ _𝑞_<sup>2</sup> ) for all _𝑞_ , higher dimensional analogues of the conjecture were proved by Pollington and Vaughan **[44]** , and weaker versions of the conjecture with extra divergence conditions were established in **[1, 22, 23]** . But the full problem resisted until the recent work of Koukoulopoulos and Maynard **[28]** : 

**Theorem 4** (KoukoulopoulosandMaynard **[28]** ). _Let 𝜓_ : N → R≥0 _besuchthat_<sup>�∞</sup> _𝑞_ =1<sup>_𝜙_(</sup><sup>_𝑞_)</sup><sup>_𝜓_(</sup><sup>_𝑞_)</sup> _diverges. Then the set of 𝛼_ ∈[0 _,_ 1) _that have infinitely many rational approximations_ | _𝛼_ − _𝑎_ / _𝑞_ | ≤ _𝜓_ ( _𝑞_ ) _with_ ( _𝑎, 𝑞_ ) = 1 _has Lebesgue measure_ 1 _. In other words, the Duffin– Schaeffer conjecture holds._ 

We refer to Koukoulopoulos’s talk at this ICM **[27]** for a more detailed exposition of this result, and the ideas behind its proof. 

We have given an overview of some of Maynard’s most spectacular achievements in analytic number theory. Maynard’s work is characterized by ingenious but simple ideas, which are carried very far with his powerful technical ability. As impressive as his work so far has been, it may only mark a beginning. 

## **Funding** 

This work was partially supported by grants from the National Science Foundation, and a Simons Investigator Award from the Simons Foundation. 

## **References** 

- **[1]** C. Aistleitner, T. Lachmann, M. Munsch, N. Technau, and A. Zafeiropoulos, The Duffin-Schaeffer conjecture with extra divergence. _Adv. Math._ **356** (2019), 106808, 11 

- **[2]** R. C. Baker, G. Harman, and J. Pintz, The difference between consecutive primes. II. _Proc. London Math. Soc. (3)_ **83** (2001), no. 3, 532–562 

- **[3]** R. C. Baker and A. J. Irving, Bounded intervals containing many primes. _Math. Z._ **286** (2017), no. 3-4, 821–841 

- **[4]** W. D. Banks, T. Freiberg, and J. Maynard, On limit points of the sequence of normalized prime gaps. _Proc. Lond. Math. Soc. (3)_ **113** (2016), no. 4, 515–539 

- **[5]** E. Bombieri, J. B. Friedlander, and H. Iwaniec, Primes in arithmetic progressions to large moduli. _Acta Math._ **156** (1986), no. 3-4, 203–251 

- **[6]** J. Bourgain, Prescribing the binary digits of primes, II. _Israel J. Math._ **206** (2015), no. 1, 165–182 

- **[7]** C. Dartyge and C. Mauduit, Nombres presque premiers dont l’écriture en base _𝑟_ ne comporte pas certains chiffres. _J. Number Theory_ **81** (2000), no. 2, 270–291 

- **[8]** C. Dartyge and C. Mauduit, Ensembles de densité nulle contenant des entiers possédant au plus deux facteurs premiers. _J. Number Theory_ **91** (2001), no. 2, 230–255 

**12 K. Soundararajan** 

|**[9]**|P. Erdős, On the distribution of the convergents of almost all real numbers._J._<br>_Number Theory_**2**(1970), 425–441|
|---|---|
|**[10]**|K. Ford, B. Green, S. Konyagin, J. Maynard, and T. Tao, Long gaps between<br>primes._J. Amer. Math. Soc._**31**(2018), no. 1, 65–105|
|**[11]**|K. Ford, B. Green, S. Konyagin, and T. Tao, Large gaps between consecutive<br>prime numbers._Ann. of Math. (2)_**183**(2016), no. 3, 935–974|
|**[12]**|E. Fouvry and H. Iwaniec, On a theorem of Bombieri-Vinogradov type._Mathe-_<br>_matika_**27**(1980), no. 2, 135–152 (1981)|
|**[13]**|J. Friedlander and H. Iwaniec, The polynomial _𝑋_<sup>2 </sup>+_𝑌_<sup>4 </sup>captures its primes._Ann._<br>_of Math. (2)_**148**(1998), no. 3, 945–1040|
|**[14]**|J. Friedlander and H. Iwaniec,_Opera de cribro_. American Mathematical Society<br>Colloquium Publications 57, American Mathematical Society, Providence, RI,<br>2010|
|**[15]**|P. Gallagher, Approximation by reduced fractions._J. Math. Soc. Japan_**13**(1961),<br>342–345|
|**[16]**|P. X. Gallagher, On the distribution of primes in short intervals._Mathematika_**23**<br>(1976), no. 1, 4–9|
|**[17]**|D. A. Goldston, J. Pintz, and C. Y. Yıldı rım, Primes in tuples. I._Ann. of Math. (2)_<br>**170**(2009), no. 2, 819–862|
|**[18]**|A. Granville, Primes in intervals of bounded length._Bull. Amer. Math. Soc. (N.S.)_<br>**52**(2015), no. 2, 171–222|
|**[19]**|B. Green and T. Tao, Linear equations in primes._Ann. of Math. (2)_**171**(2010),<br>no. 3, 1753–1850|
|**[20]**|B. Green and T. Tao, The Möbius function is strongly orthogonal to nilsequences.<br>_Ann. of Math. (2)_**175**(2012), no. 2, 541–566|
|**[21]**|B. Green, T. Tao, and T. Ziegler, An inverse theorem for the Gowers_𝑈_<sup>_𝑠_+1</sup>[_𝑁_]-<br>norm._Ann. of Math. (2)_**176**(2012), no. 2, 1231–1372|
|**[22]**|G. Harman,_Metric number theory_. London Mathematical Society Monographs.<br>New Series 18, The Clarendon Press, Oxford University Press, New York, 1998|
|**[23]**|A. K. Haynes, A. D. Pollington, and S. L. Velani, The Duffin-Schaeffer conjecture<br>with extra divergence._Math. Ann._**353**(2012), no. 2, 259–273|
|**[24]**|D. R. Heath-Brown, Primes represented by_𝑥_<sup>3 </sup>+2_𝑦_<sup>3</sup>._Acta Math._**186**(2001), no. 1,<br>1–84|
|**[25]**|D. R. Heath-Brown and X. Li, Prime values of_𝑎_<sup>2 </sup>+ _𝑝_<sup>4</sup>._Invent. Math._**208**(2017),<br>no. 2, 441–499|
|**[26]**|H. A. Helfgott, The ternary Goldbach problem. In_Proceedings of the Interna-_<br>_tional Congress of Mathematicians—Seoul 2014. Vol. II_, pp. 391–418, Kyung<br>Moon Sa, Seoul, 2014|
|**[27]**|D. Koukoulopoulos, Rational approximations of irrational numbers. 2021, URL<br>https://arxiv.org/abs/2109.11003|
|**[28]**|D. Koukoulopoulos and J. Maynard, On the Duffin-Schaeffer conjecture._Ann. of_<br>_Math. (2)_**192**(2020), no. 1, 251–307|
|**13**|**The work of James Maynard**|



|**[29]**|E. Kowalski, Gaps between prime numbers and primes in arithmetic progressions|
|---|---|
||[after Y. Zhang and J. Maynard]._Astérisque_(2015), no. 367-368, Exp. No. 1084,<br>ix, 327–366|
|**[30]**|K. Matomäki, J. Maynard, and X. Shao, Vinogradov’s theorem with almost equal<br>summands._Proc. Lond. Math. Soc. (3)_**115**(2017), no. 2, 323–347|
|**[31]**|C. Mauduit and J. Rivat, Sur un problème de Gelfond: la somme des chiffres des<br>nombres premiers._Ann. of Math. (2)_**171**(2010), no. 3, 1591–1646|
|**[32]**|J. Maynard, Small gaps between primes._Ann. of Math. (2)_**181**(2015), no. 1, 383–<br>413|
|**[33]**|J. Maynard, Dense clusters of primes in subsets._Compos. Math._**152**(2016),<br>no. 7, 1517–1554|
|**[34]**|J. Maynard, Large gaps between primes._Ann. of Math. (2)_**183**(2016), no. 3, 915–<br>933|
|**[35]**|J. Maynard, Digits of primes. In_European Congress of Mathematics_, pp. 641–<br>661, Eur. Math. Soc., Zürich, 2018|
|**[36]**|J. Maynard, Primes with restricted digits._Invent. Math._**217**(2019), no. 1, 127–<br>218|
|**[37]**|J. Maynard, Primes in arithmetic progressions to large moduli I: Fixed residue<br>classes. 2020, URLhttps://arxiv.org/abs/2006.06572|
|**[38]**|J. Maynard, Primes in arithmetic progressions to large moduli II: Well-factorable<br>estimates. 2020, URLhttps://arxiv.org/abs/2006.07088|
|**[39]**|J. Maynard, Primes in arithmetic progressions to large moduli III: Uniform<br>residue classes. 2020, URLhttps://arxiv.org/abs/2006.08250|
|**[40]**|J. Maynard, Primes represented by incomplete norm forms._Forum Math. Pi_**8**<br>(2020), e3, 128|
|**[41]**|J. Merikoski, Limit points of normalized prime gaps._J. Lond. Math. Soc. (2)_**102**<br>(2020), no. 1, 99–124|
|**[42]**|J. Pintz, Polignac numbers, conjectures of Erdős on gaps between primes, arith-<br>metic progressions in primes, and the bounded gap conjecture. In_From arithmetic_<br>_to zeta-functions_, pp. 367–384, Springer, [Cham], 2016|
|**[43]**|J. Pintz, A note on the distribution of normalized prime gaps._Acta Arith._**184**<br>(2018), no. 4, 413–418|
|**[44]**|A. D. Pollington and R. C. Vaughan, The_𝑘_-dimensional Duffin and Schaeffer con-<br>jecture._Mathematika_**37**(1990), no. 2, 190–200|
|**[45]**|D. H. J. Polymath, New equidistribution estimates of Zhang type._Algebra Number_<br>_Theory_**8**(2014), no. 9, 2067–2199|
|**[46]**|D. H. J. Polymath, Variants of the Selberg sieve, and bounded intervals containing<br>many primes._Res. Math. Sci._**1**(2014), Art. 12, 83|
|**[47]**|K. Soundararajan, Small gaps between prime numbers: the work of Goldston-<br>Pintz-Yıldırım._Bull. Amer. Math. Soc. (N.S.)_**44**(2007), no. 1, 1–18|
|**[48]**|J. D. Vaaler, On the metric theory of Diophantine approximation._Pacific J. Math._<br>**76**(1978), no. 2, 527–539|



**14 K. Soundararajan** 

- **[49]** Y. Zhang, Bounded gaps between primes. _Ann. of Math. (2)_ **179** (2014), no. 3, 1121–1174 

## **Kannan Soundararajan** 

Department of Mathematics, Stanford University, Stanford CA 94305, ksound@stanford.edu 

**15 The work of James Maynard** 

