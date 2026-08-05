# Quantum Teleportation Game -- A fun way to play and learn single qubit teleportation protocol

**arXiv ID**: 2412.12120v1
**Authors**: Himadri Barman
**Published**: 2024-12-02
**Categories**: physics.pop-ph, quant-ph
**Comments**: 10 pages, 17 figures
**HTML URL**: https://arxiv.org/html/2412.12120v1

## Abstract

We demonstrate how the quantum teleportation protocol of a single qubit can be understood by designing a simple game that can be played by three participants: Alice, Bob, and *Quantum God*.

## Full Text

Quantum Teleportation Game - A fun way to play and learn single qubit teleportation protocol
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

## Quantum Teleportation Game
- A fun way to play and learn single qubit teleportation protocolHimadri Barmanreducedpc@gmail.comDepartment of Physics, Zhejiang University, Hangzhou 310027, China

## Abstract

We demonstrate how the quantum teleportation protocol of a single qubit can be understood
by designing a simple game that can be played by three participants: Alice, Bob, andQuantum God.

## IWhat is quantum teleportation?

Teleportation refers to sending an object fast to a desired location without following a conventional trajectory-based path.
This phenomenon has been depicted in several science fiction and fantasy stories. To mention, Indian filmmaker Satyajit Ray’s
iconic film Goopy Gyne Bagha Byne (1969)’s[1]duo protagonists had the magical power to teleport themselves by a snap
of a clapping together (see  Fig.1). Also, who can forget the popular phrasebeam me up(asking someone to teleport through atransporter) in Star Trek’s episodes?
Though the above fictional examples deal with transporting real objects (even human beings),quantum teleportation(QT) in principle transfers a quantum information (defined by the quantum state) almost instantly from one place to another.
The simplest and most popular protocol for teleporting a single qubit was first proposed by Bennettet al.[2].
A few years later, their protocol was experimentally confirmed using photonic qubits[3,4]. Since then, QT has been demonstrated through various platforms, including NMR[5], coherent optical modes[6,7], trapped ions[8,9,10], combined light and matter[11], solid-sattes[12,13], superconducting circuits[14], and many other realizations[15,16]. The QT protocol has also been extended to multiqubits[17,18,19]and high-dimensional qubits[20,21,22,23,24].
Notably, successful teleportation has been achieved over a record distance of 1,400 km[25].
QT has become a cornerstone of modern quantum computation and quantum information giving rise to numerous research areas such as quantum key distribution (QKD)[26,27], quantum internet[28,29,30], measurement-based computing[31,32], and quantum repeaters[33]. Therefore an understanding of the basic protocol is is highly desirable. If this understanding can be achieved in an engaging way, such as by playing a simple rules-based game, with fun and entertainment, it may attract greater interest and awareness among students and the general public.
With this spirit in mind, we have designed a quantum teleportation game, which serves as the central focus of our paper. In the forthcoming sections, we first discuss the theory of the single-qubit QT protocol originally proposed by Benettet al.[2], then provide a detailed explanation of the game, and finally conclude with a summary.Figure 1:A scene of teleportation from the iconic film Goopy Gyne Bagha Byne (1969), directed by Academy Award-winning filmmaker Satyajit Ray. The protagonists, Goopy Gyne and Bagha Byne, successfully teleport themselves by joining hands and shouting the name of their desired destination.

## IIThe teleportation protocol

In the QT protocol, an agent named Alice is assigned to send a quantum information (represented by state|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩)
to another agent, Bob, without it being intercepted by any rival or competing agent, Eve (see Fig.2). To acheive her objective, Alice prepares an entangled state (a Bell state) shared with Bob. This presence of quantum entanglement allows Bob to generate exactly the same state in his own place after performing some quantum operations.Figure 2:A schematic of quantum teleportation: Alice sends quantum information to Bob with whom she shares
an entangled state. Meanwhile, Eve tries to intercept the information but fails as the entanglement between Alice and Bob keeps the information protected.

We briefly describe the protocol for a single qubit|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩below.

## Initialization and entanglement preparation

There are three qubits. Two of them are distributed to Alice and the third one is given to Bob.
The first qubit is in the state|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩which can be generically written in terms of single qubit bases|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩and|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩(i.e. superposition of|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩and|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩):|Q⟩=a⁢|0⟩+b⁢|1⟩ket𝑄𝑎ket0𝑏ket1\displaystyle\ket{Q}=a\ket{0}+b\ket{1}\,| start_ARG italic_Q end_ARG ⟩ = italic_a | start_ARG 0 end_ARG ⟩ + italic_b | start_ARG 1 end_ARG ⟩(1)

where|a|2+|b|2=1superscript𝑎2superscript𝑏21|a|^{2}+|b|^{2}=1| italic_a | start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT + | italic_b | start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT = 1satisfying the quantum probability conservation.
Alice’s task is to deliver the state|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩to Bob through teleportation
even though she may not have any specific knowledge about|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩.

## Convention of denoting multiqubit states:

We adopt the convention of denoting a multiqubit tensor product state by sequencing individual qubit states from right to left. In our 3-qubit situation, if the first, second, and third qubits areq0subscript𝑞0q_{0}italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT,q1subscript𝑞1q_{1}italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT, andq2subscript𝑞2q_{2}italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPTrespectively, the convention instructs us to write the 3-qubit state as|q2⟩⁢|q1⟩⁢|q0⟩=|q2⁢q1⟩⁢|q0⟩=|q2⟩⁢|q1⁢q0⟩=|q2⁢q1⁢q0⟩ketsubscript𝑞2ketsubscript𝑞1ketsubscript𝑞0ketsubscript𝑞2subscript𝑞1ketsubscript𝑞0ketsubscript𝑞2ketsubscript𝑞1subscript𝑞0ketsubscript𝑞2subscript𝑞1subscript𝑞0{\color[rgb]{0,0,1}\ket{q_{2}}\ket{q_{1}}\ket{q_{0}}=\ket{q_{2}q_{1}}\ket{q_{0%
}}=\ket{q_{2}}\ket{q_{1}q_{0}}=\ket{q_{2}q_{1}q_{0}}}| start_ARG italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG ⟩ | start_ARG italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩ | start_ARG italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_ARG ⟩ = | start_ARG italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩ | start_ARG italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_ARG ⟩ = | start_ARG italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG ⟩ | start_ARG italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_ARG ⟩ = | start_ARG italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_ARG ⟩.
Thus, the first and last qubits are denoted on the extreme right and extreme left, respectively.
Now, let as assume the other qubits of Alice and Bob are initially in states|A⟩ket𝐴\ket{A}| start_ARG italic_A end_ARG ⟩and|B⟩ket𝐵\ket{B}| start_ARG italic_B end_ARG ⟩. Then the
raw 3-qubit state is|ψ⟩0=|B⁢A⁢Q⟩subscriptket𝜓0ket𝐵𝐴𝑄\ket{\psi}_{0}=\ket{BAQ}| start_ARG italic_ψ end_ARG ⟩ start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = | start_ARG italic_B italic_A italic_Q end_ARG ⟩.
Through a set of quantum operations (will be detailed soon), an entangled state is created and shared between them.
A common such entanglement state is one of the EPR states or Bell states (conventionally denoted
by|Φ+⟩ketsuperscriptΦ\ket{\Phi^{+}}| start_ARG roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_ARG ⟩,|Ψ+⟩ketsuperscriptΨ\ket{\Psi^{+}}| start_ARG roman_Ψ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_ARG ⟩,|Φ−⟩ketsuperscriptΦ\ket{\Phi^{-}}| start_ARG roman_Φ start_POSTSUPERSCRIPT - end_POSTSUPERSCRIPT end_ARG ⟩, and|Ψ−⟩ketsuperscriptΨ\ket{\Psi^{-}}| start_ARG roman_Ψ start_POSTSUPERSCRIPT - end_POSTSUPERSCRIPT end_ARG ⟩)[34]. In our case, we choose|Φ+⟩≡(|00⟩+|11⟩)/2ketsuperscriptΦket00ket112\ket{\Phi^{+}}\equiv(\ket{00}+\ket{11})/\sqrt{2}| start_ARG roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_ARG ⟩ ≡ ( | start_ARG 00 end_ARG ⟩ + | start_ARG 11 end_ARG ⟩ ) / square-root start_ARG 2 end_ARGas the entanglement
pair. If both|A⟩ket𝐴\ket{A}| start_ARG italic_A end_ARG ⟩and|B⟩ket𝐵\ket{B}| start_ARG italic_B end_ARG ⟩are in the state|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩, then|Φ+⟩ketsuperscriptΦ\ket{\Phi^{+}}| start_ARG roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_ARG ⟩can be easily generated
by the following two-step quatum gate operations (see Fig.3for the circuit representation).
- Step 0:

Operate with a Hadamard (H𝐻Hitalic_H) gate on|A⟩=|0⟩ket𝐴ket0\ket{A}=\ket{0}| start_ARG italic_A end_ARG ⟩ = | start_ARG 0 end_ARG ⟩and create a superposition state:|A′⟩=12⁢[|0⟩+|1⟩]ketsuperscript𝐴′12delimited-[]ket0ket1\ket{A^{\prime}}=\frac{1}{\sqrt{2}}\big{[}\ket{0}+\ket{1}]| start_ARG italic_A start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_ARG ⟩ = divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 0 end_ARG ⟩ + | start_ARG 1 end_ARG ⟩ ]. This updates 2-qubit state between Alice and Bob to|ϕ1⟩=|B⁢A′⟩ketsubscriptitalic-ϕ1ket𝐵superscript𝐴′\ket{\phi_{1}}=\ket{BA^{\prime}}| start_ARG italic_ϕ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩ = | start_ARG italic_B italic_A start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_ARG ⟩and the overall 3-qubit state becomes|ψ0⟩→|ψ1⟩=|B⁢A′⟩⁢|Q⟩=|ϕ1⟩⁢|Q⟩.→ketsubscript𝜓0ketsubscript𝜓1ket𝐵superscript𝐴′ket𝑄ketsubscriptitalic-ϕ1ket𝑄\displaystyle\ket{\psi_{0}}\to\ket{\psi_{1}}=\ket{BA^{\prime}}\ket{Q}=\ket{%
\phi_{1}}\ket{Q}\,.| start_ARG italic_ψ start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_ARG ⟩ → | start_ARG italic_ψ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩ = | start_ARG italic_B italic_A start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_ARG ⟩ | start_ARG italic_Q end_ARG ⟩ = | start_ARG italic_ϕ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩ | start_ARG italic_Q end_ARG ⟩ .(2)
- Step 1:

Operate a controlledN⁢O⁢T𝑁𝑂𝑇NOTitalic_N italic_O italic_TorC⁢X𝐶𝑋CXitalic_C italic_Xgate where|A′⟩ketsuperscript𝐴′\ket{A^{\prime}}| start_ARG italic_A start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_ARG ⟩is the control qubit and|B⟩ket𝐵\ket{B}| start_ARG italic_B end_ARG ⟩is
the target bit. This modifies|ϕ1⟩ketsubscriptitalic-ϕ1\ket{\phi_{1}}| start_ARG italic_ϕ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩into the Bell state|Φ+⟩ketsuperscriptΦ\ket{\Phi^{+}}| start_ARG roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_ARG ⟩. The state can no longer be expressed as a product of two individual quantum states as it is already entangled.Figure 3:Generation of the Bell state|Φ+⟩ketsuperscriptΦ\ket{\Phi^{+}}| start_ARG roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_ARG ⟩from two qubits both initialized at state|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩: A Hadamard gate operates on the first qubit. A controlledN⁢O⁢T𝑁𝑂𝑇NOTitalic_N italic_O italic_T(C⁢N⁢O⁢T𝐶𝑁𝑂𝑇CNOTitalic_C italic_N italic_O italic_T) orC⁢X𝐶𝑋CXitalic_C italic_Xgate operates between first and second qubit. Image is adapted from the output generated by Python coding with IBM’sQiskitmodule.

Thus, after setting up an entanglement between Alice and Bob, the ready-to-teleport
3-qubit state is prepared as|ψ2⟩ketsubscript𝜓2\displaystyle\ket{\psi_{2}}| start_ARG italic_ψ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG ⟩=|Φ+⟩⁢|Q⟩=12⁢[|00⟩+|11⟩]⁢[a⁢|0⟩+b⁢|1⟩]absentketsuperscriptΦket𝑄12delimited-[]ket00ket11delimited-[]𝑎ket0𝑏ket1\displaystyle=\ket{\Phi^{+}}\ket{Q}=\frac{1}{\sqrt{2}}[\ket{00}+\ket{11}][a%
\ket{0}+b\ket{1}]= | start_ARG roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_ARG ⟩ | start_ARG italic_Q end_ARG ⟩ = divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 00 end_ARG ⟩ + | start_ARG 11 end_ARG ⟩ ] [ italic_a | start_ARG 0 end_ARG ⟩ + italic_b | start_ARG 1 end_ARG ⟩ ]=12⁢[a⁢|000⟩+a⁢|110⟩+b⁢|001⟩+b⁢|111⟩].absent12delimited-[]𝑎ket000𝑎ket110𝑏ket001𝑏ket111\displaystyle=\frac{1}{\sqrt{2}}\big{[}a\ket{000}+a\ket{110}+b\ket{001}+b\ket{%
111}\big{]}\,.= divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ italic_a | start_ARG 000 end_ARG ⟩ + italic_a | start_ARG 110 end_ARG ⟩ + italic_b | start_ARG 001 end_ARG ⟩ + italic_b | start_ARG 111 end_ARG ⟩ ] .(3)

## Alice’s operations

Now, Alice operates aC⁢N⁢O⁢T𝐶𝑁𝑂𝑇CNOTitalic_C italic_N italic_O italic_TorC⁢X𝐶𝑋CXitalic_C italic_Xgate (denoted by the operatorX^Csubscript^𝑋𝐶{\hat{X}}_{C}over^ start_ARG italic_X end_ARG start_POSTSUBSCRIPT italic_C end_POSTSUBSCRIPT) between the state|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩(q0subscript𝑞0q_{0}italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT) and her own qubit (q1subscript𝑞1q_{1}italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT). This updates the state|ψ2⟩ketsubscript𝜓2\ket{\psi_{2}}| start_ARG italic_ψ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG ⟩to|ψ3⟩ketsubscript𝜓3\ket{\psi_{3}}| start_ARG italic_ψ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT end_ARG ⟩:|ψ3⟩=X^C⁢(0,1)⁢|ψ2⟩ketsubscript𝜓3subscript^𝑋𝐶01ketsubscript𝜓2\displaystyle\ket{\psi_{3}}={\hat{X}}_{C}(0,1)\ket{\psi_{2}}| start_ARG italic_ψ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT end_ARG ⟩ = over^ start_ARG italic_X end_ARG start_POSTSUBSCRIPT italic_C end_POSTSUBSCRIPT ( 0 , 1 ) | start_ARG italic_ψ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG ⟩=12[a|000⟩+a|110⟩\displaystyle=\frac{1}{\sqrt{2}}\big{[}a\ket{000}+a\ket{110}= divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ italic_a | start_ARG 000 end_ARG ⟩ + italic_a | start_ARG 110 end_ARG ⟩+b|011⟩+b|101⟩].\displaystyle\qquad+b\ket{011}+b\ket{101}\big{]}\,.+ italic_b | start_ARG 011 end_ARG ⟩ + italic_b | start_ARG 101 end_ARG ⟩ ] .(4)

Note that the control and target qubits are denoted by the indices of quantum wires
in the circuit (here00and1111for wiresq0subscript𝑞0q_{0}italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPTandq1subscript𝑞1q_{1}italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT) and expressed within the parentheses following a controlled gate operator (hereX^Csubscript^𝑋𝐶{\hat{X}}_{C}over^ start_ARG italic_X end_ARG start_POSTSUBSCRIPT italic_C end_POSTSUBSCRIPT, see Sec.A).Figure 4:The single qubit quantum state (defined by|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩) teleportation circuit with all necessary gates and measurements. Image is adapted from the output generated by Python coding with IBM’sQiskitmodule.

After this, she applies a Hadamard (H𝐻Hitalic_H) gate onq0subscript𝑞0q_{0}italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT, which modifiesψ3subscript𝜓3\psi_{3}italic_ψ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPTtoψ4subscript𝜓4\psi_{4}italic_ψ start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT:|ψ4⟩ketsubscript𝜓4\displaystyle\ket{\psi_{4}}| start_ARG italic_ψ start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT end_ARG ⟩=H⁢(0)⁢|ψ3⟩absent𝐻0ketsubscript𝜓3\displaystyle=H(0)\ket{\psi_{3}}= italic_H ( 0 ) | start_ARG italic_ψ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT end_ARG ⟩=12⁢12⁢[a⁢|00⟩⁢[|0⟩+|1⟩]+a⁢|11⟩⁢[|0⟩+|1⟩]]absent1212delimited-[]𝑎ket00delimited-[]ket0ket1𝑎ket11delimited-[]ket0ket1\displaystyle=\frac{1}{\sqrt{2}}\frac{1}{\sqrt{2}}\bigg{[}a\ket{00}\big{[}\ket%
{0}+\ket{1}\big{]}+a\ket{11}\big{[}\ket{0}+\ket{1}\big{]}\bigg{]}= divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ italic_a | start_ARG 00 end_ARG ⟩ [ | start_ARG 0 end_ARG ⟩ + | start_ARG 1 end_ARG ⟩ ] + italic_a | start_ARG 11 end_ARG ⟩ [ | start_ARG 0 end_ARG ⟩ + | start_ARG 1 end_ARG ⟩ ] ]+12⁢12⁢[b⁢|01⟩⁢[|0⟩−|1⟩]+b⁢|10⟩⁢[|0⟩−|1⟩]]1212delimited-[]𝑏ket01delimited-[]ket0ket1𝑏ket10delimited-[]ket0ket1\displaystyle\quad+\frac{1}{\sqrt{2}}\frac{1}{\sqrt{2}}\bigg{[}b\ket{01}\big{[%
}\ket{0}-\ket{1}\big{]}+b\ket{10}\big{[}\ket{0}-\ket{1}\big{]}\bigg{]}+ divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ italic_b | start_ARG 01 end_ARG ⟩ [ | start_ARG 0 end_ARG ⟩ - | start_ARG 1 end_ARG ⟩ ] + italic_b | start_ARG 10 end_ARG ⟩ [ | start_ARG 0 end_ARG ⟩ - | start_ARG 1 end_ARG ⟩ ] ]=12[a|000⟩+a|001⟩+a|110⟩+a|111⟩\displaystyle=\frac{1}{2}\bigg{[}a\ket{000}+a\ket{001}+a\ket{110}+a\ket{111}= divide start_ARG 1 end_ARG start_ARG 2 end_ARG [ italic_a | start_ARG 000 end_ARG ⟩ + italic_a | start_ARG 001 end_ARG ⟩ + italic_a | start_ARG 110 end_ARG ⟩ + italic_a | start_ARG 111 end_ARG ⟩+b|010⟩−b|011⟩+b|100⟩−b|101⟩]\displaystyle\quad+b\ket{010}-b\ket{011}+b\ket{100}-b\ket{101}\bigg{]}+ italic_b | start_ARG 010 end_ARG ⟩ - italic_b | start_ARG 011 end_ARG ⟩ + italic_b | start_ARG 100 end_ARG ⟩ - italic_b | start_ARG 101 end_ARG ⟩ ]

|ψ4⟩ketsubscript𝜓4\ket{\psi_{4}}| start_ARG italic_ψ start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT end_ARG ⟩can be rearranged as|ψ4⟩ketsubscript𝜓4\displaystyle\ket{\psi_{4}}| start_ARG italic_ψ start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT end_ARG ⟩=12[[a|000⟩+b|100⟩]+[a|011⟩−b|111⟩]\displaystyle=\frac{1}{2}\bigg{[}\big{[}a\ket{000}+b\ket{100}\big{]}+\big{[}a%
\ket{011}-b\ket{111}\big{]}= divide start_ARG 1 end_ARG start_ARG 2 end_ARG [ [ italic_a | start_ARG 000 end_ARG ⟩ + italic_b | start_ARG 100 end_ARG ⟩ ] + [ italic_a | start_ARG 011 end_ARG ⟩ - italic_b | start_ARG 111 end_ARG ⟩ ]+[a|110⟩+b|010⟩]+[a|111⟩−b|011⟩]]\displaystyle\qquad+\big{[}a\ket{110}+b\ket{010}\big{]}+\big{[}a\ket{111}-b%
\ket{011}\big{]}\bigg{]}+ [ italic_a | start_ARG 110 end_ARG ⟩ + italic_b | start_ARG 010 end_ARG ⟩ ] + [ italic_a | start_ARG 111 end_ARG ⟩ - italic_b | start_ARG 011 end_ARG ⟩ ] ]=12[[a|0⟩+b|1⟩]|00⟩+[a|0⟩−b|1⟩]|10⟩\displaystyle=\frac{1}{2}\bigg{[}\big{[}a\ket{0}+b\ket{1}\big{]}\ket{00}+\big{%
[}a\ket{0}-b\ket{1}\big{]}\ket{10}= divide start_ARG 1 end_ARG start_ARG 2 end_ARG [ [ italic_a | start_ARG 0 end_ARG ⟩ + italic_b | start_ARG 1 end_ARG ⟩ ] | start_ARG 00 end_ARG ⟩ + [ italic_a | start_ARG 0 end_ARG ⟩ - italic_b | start_ARG 1 end_ARG ⟩ ] | start_ARG 10 end_ARG ⟩+[a|1⟩+b|0⟩]|01⟩+[a|1⟩−b|0⟩]|11⟩]\displaystyle\qquad+\big{[}a\ket{1}+b\ket{0}\big{]}\ket{01}+\big{[}a\ket{1}-b%
\ket{0}\big{]}\ket{11}\bigg{]}+ [ italic_a | start_ARG 1 end_ARG ⟩ + italic_b | start_ARG 0 end_ARG ⟩ ] | start_ARG 01 end_ARG ⟩ + [ italic_a | start_ARG 1 end_ARG ⟩ - italic_b | start_ARG 0 end_ARG ⟩ ] | start_ARG 11 end_ARG ⟩ ]=12[[1^|Q⟩]|00⟩+[X^|Q⟩]|10⟩\displaystyle=\frac{1}{2}\bigg{[}{\color[rgb]{0,0,1}\big{[}{\hat{1}}\ket{Q}%
\big{]}}\ket{00}+{\color[rgb]{0,0,1}\big{[}{\hat{X}}\ket{Q}\big{]}}\ket{10}= divide start_ARG 1 end_ARG start_ARG 2 end_ARG [ [ over^ start_ARG 1 end_ARG | start_ARG italic_Q end_ARG ⟩ ] | start_ARG 00 end_ARG ⟩ + [ over^ start_ARG italic_X end_ARG | start_ARG italic_Q end_ARG ⟩ ] | start_ARG 10 end_ARG ⟩+[Z^|Q⟩]|01⟩+[X^Z^|Q⟩]|11⟩].\displaystyle\qquad+{\color[rgb]{0,0,1}\big{[}{\hat{Z}}\ket{Q}\big{]}}\ket{01}%
+{\color[rgb]{0,0,1}\big{[}{\hat{X}}{\hat{Z}}\ket{Q}\big{]}}\ket{11}\bigg{]}\,.+ [ over^ start_ARG italic_Z end_ARG | start_ARG italic_Q end_ARG ⟩ ] | start_ARG 01 end_ARG ⟩ + [ over^ start_ARG italic_X end_ARG over^ start_ARG italic_Z end_ARG | start_ARG italic_Q end_ARG ⟩ ] | start_ARG 11 end_ARG ⟩ ] .(5)

Finally, Alice measures the first two qubits available in her lab and reports the outcome
(through telephone or texting) as two classical bits to Bob.

## II.1Bob’s action

Bob receives the classical pair of bits from Alice. There are 4 possible outcomes: (i) 00, (ii) 01, (iii) 10, and (iv) 11. Correspondingly, Bob has
states|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩,X^⁢|Q⟩^𝑋ket𝑄{\hat{X}}\ket{Q}over^ start_ARG italic_X end_ARG | start_ARG italic_Q end_ARG ⟩,Z^⁢|Q⟩^𝑍ket𝑄{\hat{Z}}\ket{Q}over^ start_ARG italic_Z end_ARG | start_ARG italic_Q end_ARG ⟩, andX^⁢Z^⁢|Q⟩^𝑋^𝑍ket𝑄{\hat{X}}{\hat{Z}}\ket{Q}over^ start_ARG italic_X end_ARG over^ start_ARG italic_Z end_ARG | start_ARG italic_Q end_ARG ⟩(see Eq. (5)). For (i), Bob already has created the
state|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩. So he does not have to do anything further or in other words, he applies an identity operatorI^^𝐼\hat{I}over^ start_ARG italic_I end_ARG(I𝐼Iitalic_Igate) on his present state.
For other outcomes, Bob needs to operate with the following gates on his existing quantum state. Bob needs to operate with
anX𝑋Xitalic_Xgate for (ii), aZ𝑍Zitalic_Zgate for (iii), and consecutivelyX𝑋Xitalic_XandZ𝑍Zitalic_Zgates for (iv)
as these operations yield the state|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩. [Note that to get|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩fromX^⁢Z^⁢|Q⟩^𝑋^𝑍ket𝑄\hat{X}\hat{Z}\ket{Q}over^ start_ARG italic_X end_ARG over^ start_ARG italic_Z end_ARG | start_ARG italic_Q end_ARG ⟩, we need to operate the latter state with(X^⁢Z^)†=Z^⁢X^superscript^𝑋^𝑍†^𝑍^𝑋(\hat{X}\hat{Z})^{\dagger}=\hat{Z}\hat{X}( over^ start_ARG italic_X end_ARG over^ start_ARG italic_Z end_ARG ) start_POSTSUPERSCRIPT † end_POSTSUPERSCRIPT = over^ start_ARG italic_Z end_ARG over^ start_ARG italic_X end_ARG, which means anX𝑋Xitalic_Xgate has to be operated on the state first and then aZ𝑍Zitalic_Zgate will be operated on that.]
This leads to a lookup table for Bob which he can blindly follow as instructions to generate the unknown state|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩in his
own lab:
{tblr}

colspec = —c—c—c—c—,
row1 = bg=TopRow, fg=black, j, row2 = bg=NormalRow, fg=black, c, row3 = bg=NormalRow, fg=black, c,
row4 = bg=NormalRow, fg=black, c,
row5 = bg=NormalRow, fg=black, cCaseAlice’s
classical bitsBob’s operators
to create
|q2⟩=|Q⟩ketsubscript𝑞2ket𝑄\ket{q_{2}}=\ket{Q}| start_ARG italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG ⟩ = | start_ARG italic_Q end_ARG ⟩Compact
formula
100I^^𝐼{\hat{I}}over^ start_ARG italic_I end_ARGZ^0⁢X^0superscript^𝑍0superscript^𝑋0{\hat{Z}}^{0}{\hat{X}}^{0}over^ start_ARG italic_Z end_ARG start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT over^ start_ARG italic_X end_ARG start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT
201Z^^𝑍{\hat{Z}}over^ start_ARG italic_Z end_ARGZ^1⁢X^0superscript^𝑍1superscript^𝑋0{\hat{Z}}^{1}{\hat{X}}^{0}over^ start_ARG italic_Z end_ARG start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT over^ start_ARG italic_X end_ARG start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT
310X^^𝑋{\hat{X}}over^ start_ARG italic_X end_ARGZ^0⁢X^1superscript^𝑍0superscript^𝑋1{\hat{Z}}^{0}{\hat{X}}^{1}over^ start_ARG italic_Z end_ARG start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT over^ start_ARG italic_X end_ARG start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT
411Z^⁢X^^𝑍^𝑋{\hat{Z}\hat{X}}over^ start_ARG italic_Z end_ARG over^ start_ARG italic_X end_ARGZ^1⁢X^1superscript^𝑍1superscript^𝑋1{\hat{Z}}^{1}{\hat{X}}^{1}over^ start_ARG italic_Z end_ARG start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT over^ start_ARG italic_X end_ARG start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT

From the table above (TableII.1), we also notice two things:X^^𝑋{\hat{X}}over^ start_ARG italic_X end_ARGgate only operates when the second qubit (q1subscript𝑞1q_{1}italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT) is
in state|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩(Case 3 and 4) whileZ^^𝑍{\hat{Z}}over^ start_ARG italic_Z end_ARGgate only operates when the first qubit (q1subscript𝑞1q_{1}italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT) is
in state|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩(Case 2 and 4). Thus, Bob merely needs to first applyC⁢N⁢O⁢T⁢(1,2)𝐶𝑁𝑂𝑇12CNOT(1,2)italic_C italic_N italic_O italic_T ( 1 , 2 )orC⁢X⁢(1,2)𝐶𝑋12CX(1,2)italic_C italic_X ( 1 , 2 )gate and thenC⁢Z⁢(0,2)𝐶𝑍02CZ(0,2)italic_C italic_Z ( 0 , 2 )gate on the existing
3-qubit state. In this way, Bob successfully generates the quantum information|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩in his place while Alice
loses it and QT happens (see Fig.4for full quantum circuit diagram). Destruction of|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩in Alice’s lab respects theNo-Cloning Theorem[35],
i.e. no quantum states can be copied without changing the original states.Table 1:A table for Bob telling him to apply the necessary gate(s) to generate|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩for his qubitq2subscript𝑞2q_{2}italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPTfor the four possible outcomes of Alice’s measurement.

## IIIThe teleportation game

## III.1Preparation

There are three players in the game, namely Alice, Bob, and Quantum God (QG). Their roles are the following.
- •

QG:QG is responsible for all quantum rules governing in the world. They also help in telling the measurement outcome.
- •

Alice:Alice has her own qubit|A⟩=|0⟩ket𝐴ket0\ket{A}=\ket{0}| start_ARG italic_A end_ARG ⟩ = | start_ARG 0 end_ARG ⟩at the beginning. But she acquires another qubit|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩from QG,
which she has been instructed to teleport to her friend Bob.
- •

Bob:Bob is supposed to receive the quantum information from Alice and generate the state|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩in his own lab by performing some quantum gate operations. He gets a default qubit|B⟩=|0⟩ket𝐵ket0\ket{B}=\ket{0}| start_ARG italic_B end_ARG ⟩ = | start_ARG 0 end_ARG ⟩.(a)(b)(c)Figure 5:Players of the Quantum Teleportation Game: (a) Alice, (b) Bob, and (c) Quantum God (representative images). Quantum God (QG) supervises all the quantum rules and updates the quantum states during the running of the game.

## III.2Acting like quantum

Since the game is only for a demonstration purpose and real quantum equipment are not available, we adopt some classical actions conducted by the players or performers in the game. We furnish below three important quantum parts that can be classically enacted in the game.

## III.2.1Updation of a quantum state

First of all, any quantum information or state is updated by the QG. QG keeps a register (can be a physical notebook or diary), where initial state is noted down by them and evolution of the state after a gate operation is updated by them on the same register. They do not share the quantum information with Alice and Bob at all (like any real quantum state is unknown to an observer).

## III.2.2Gate operations

When Alice or Bob operates a gate, she or he picks up a cardboard where the name of the gate is written and submits it to QG (see Fig.6). QG updates the state after the gate operation as mentioned above.

## III.2.3Quantum measurement

When Alice or Bob makes a quantum measurement, a superposition quantum state gets collapsed to one of the basis state (a superposition state is a linear combination of all the states).
QG provides a paper chit which
We create a few placards or cardboards reading the names of the game. When Alice or Bob operates a gate, she or he

## III.3Equipment

Following the above discussion, the minimal required pieces of equipment are listed below.
- 1.

Cardboard pieces or cards with gate names:C⁢X𝐶𝑋CXitalic_C italic_X,H𝐻Hitalic_H,C⁢Z𝐶𝑍CZitalic_C italic_Z,X𝑋Xitalic_X.
- 2.

Nameplates or mugshot boards that can be worn by “Alice”, “Bob”, and “QG”.
- 3.

4 small pieces of papers where00000000,01010101,10101010, and11111111will be written.
- 4.

The secret diary of QG.(a)(b)(c)Figure 6:The basic equipment for the quantum teleportation game: (a) labels to be attached to the players; (b) Cardboard representing gate operators, quantum chits, and Bob’s chart; (c) QG’s secret diary.

## III.4The game

For the demonstration purpose, let us consider|Q⟩=|1⟩ket𝑄ket1\ket{Q}=\ket{1}| start_ARG italic_Q end_ARG ⟩ = | start_ARG 1 end_ARG ⟩. Alice and Bob both have state|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩. Now, the game is played by performing the following actions.
- Action 0:

QG notes down the initial 3-qubit state on their diary:|ψ0⟩=|0⟩⁢|1⟩⁢|1⟩=|001⟩ketsubscript𝜓0ket0ket1ket1ket001\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{0}}}=\ket{0}\ket{1}\ket{1}=\ket{001}| start_ARG italic_ψ start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_ARG ⟩ = | start_ARG 0 end_ARG ⟩ | start_ARG 1 end_ARG ⟩ | start_ARG 1 end_ARG ⟩ = | start_ARG 001 end_ARG ⟩(1)
- Action 1:

Alice performs anH𝐻Hitalic_H-gate operation. She submits anH𝐻Hitalic_H-gate card to QG (see Fig.7). This converts her qubit
to a superposition state12⁢[|0⟩+|1⟩]12delimited-[]ket0ket1\frac{1}{\sqrt{2}}\big{[}\ket{0}+\ket{1}\big{]}divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 0 end_ARG ⟩ + | start_ARG 1 end_ARG ⟩ ].
QG accepts the gate and updates the state in the diary:
(see Fig.7):|ψ1⟩ketsubscript𝜓1\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{1}}}| start_ARG italic_ψ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩=H^⁢(1)⁢|ψ1⟩=|0⟩⁢12⁢[|0⟩+|1⟩]⁢|1⟩absent^𝐻1ketsubscript𝜓1ket012delimited-[]ket0ket1ket1\displaystyle={\hat{H}}(1)\ket{\psi_{1}}=\ket{0}\frac{1}{\sqrt{2}}\big{[}\ket{%
0}+\ket{1}\big{]}\ket{1}= over^ start_ARG italic_H end_ARG ( 1 ) | start_ARG italic_ψ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩ = | start_ARG 0 end_ARG ⟩ divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 0 end_ARG ⟩ + | start_ARG 1 end_ARG ⟩ ] | start_ARG 1 end_ARG ⟩=12⁢[|001⟩+|011⟩].absent12delimited-[]ket001ket011\displaystyle=\frac{1}{\sqrt{2}}\big{[}\ket{001}+\ket{011}\big{]}\,.= divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 001 end_ARG ⟩ + | start_ARG 011 end_ARG ⟩ ] .(2)(a)(b)Figure 7:(a) Alice submittingH𝐻Hitalic_Hgate to QG. (b) QG accepting the gate and updating the state on their diary. Images are from the event
performed at the NIUS Physics Camp 2024, HBCSE, Mumbai, India.
- Action 2:

Now, Alice performs aC⁢N⁢O⁢T𝐶𝑁𝑂𝑇CNOTitalic_C italic_N italic_O italic_TorC⁢X𝐶𝑋CXitalic_C italic_Xoperation on (1,2) (q1subscript𝑞1q_{1}italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT: controlled bit,q2subscript𝑞2q_{2}italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPTtarget bit). She hands over aC⁢X𝐶𝑋CXitalic_C italic_Xcard to QG and mentions the qubits where the gate to be operated.
QG looks into the state and flips the qubitq2subscript𝑞2q_{2}italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPTonly when theq1subscript𝑞1q_{1}italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPTqubit in found to be|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩.
Thus, QG updates in the diary:|ψ2⟩=X^C⁢(1,2)⁢|ψ1⟩=12⁢[|001⟩+|111⟩].ketsubscript𝜓2subscript^𝑋𝐶12ketsubscript𝜓112delimited-[]ket001ket111\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{2}}}={\hat{X}}_{C}(1,2)\ket{\psi_{1%
}}=\frac{1}{\sqrt{2}}\big{[}\ket{001}+\ket{111}\big{]}\,.| start_ARG italic_ψ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG ⟩ = over^ start_ARG italic_X end_ARG start_POSTSUBSCRIPT italic_C end_POSTSUBSCRIPT ( 1 , 2 ) | start_ARG italic_ψ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩ = divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 001 end_ARG ⟩ + | start_ARG 111 end_ARG ⟩ ] .(3)

Note that this state is nothing but|Φ+⟩⁢|Q⟩ketsuperscriptΦket𝑄\ket{\Phi^{+}}\ket{Q}| start_ARG roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_ARG ⟩ | start_ARG italic_Q end_ARG ⟩and hence successfully an entanglement is established, through a Bell pair|Φ+⟩ketsuperscriptΦ\ket{\Phi^{+}}| start_ARG roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_ARG ⟩,
between Alice and Bob’s qubits.
- Action 3:

Alice submits anotherC⁢X𝐶𝑋CXitalic_C italic_Xcard to QG but now she tells that she wants to operate on (0,1). QG
flipsq1subscript𝑞1q_{1}italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT’s state only whenq0subscript𝑞0q_{0}italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPTis found to be in|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩. Hence, QG updates:|ψ3⟩=X^C⁢(0,1)⁢|ψ2⟩=12⁢[|011⟩+|101⟩].ketsubscript𝜓3subscript^𝑋𝐶01ketsubscript𝜓212delimited-[]ket011ket101\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{3}}}={\hat{X}}_{C}(0,1)\ket{\psi_{2%
}}=\frac{1}{\sqrt{2}}\big{[}\ket{011}+\ket{101}\big{]}\,.| start_ARG italic_ψ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT end_ARG ⟩ = over^ start_ARG italic_X end_ARG start_POSTSUBSCRIPT italic_C end_POSTSUBSCRIPT ( 0 , 1 ) | start_ARG italic_ψ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG ⟩ = divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 011 end_ARG ⟩ + | start_ARG 101 end_ARG ⟩ ] .(4)
- Action 4:

Alice performs anH𝐻Hitalic_H-gate operation onq0subscript𝑞0q_{0}italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT.
As soon as as she submits the gate’s card to QG, they update the state
(see Fig.7):|ψ4⟩=H^⁢(0)⁢|ψ3⟩ketsubscript𝜓4^𝐻0ketsubscript𝜓3\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{4}}}={\hat{H}}(0)\ket{\psi_{3}}| start_ARG italic_ψ start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT end_ARG ⟩ = over^ start_ARG italic_H end_ARG ( 0 ) | start_ARG italic_ψ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT end_ARG ⟩=12⁢|01⟩⁢[|0⟩−|1⟩]+12⁢|10⟩⁢[|0⟩−|1⟩]absent12ket01delimited-[]ket0ket112ket10delimited-[]ket0ket1\displaystyle=\frac{1}{2}\ket{01}\big{[}\ket{0}-\ket{1}\big{]}+\frac{1}{2}\ket%
{10}\big{[}\ket{0}-\ket{1}\big{]}= divide start_ARG 1 end_ARG start_ARG 2 end_ARG | start_ARG 01 end_ARG ⟩ [ | start_ARG 0 end_ARG ⟩ - | start_ARG 1 end_ARG ⟩ ] + divide start_ARG 1 end_ARG start_ARG 2 end_ARG | start_ARG 10 end_ARG ⟩ [ | start_ARG 0 end_ARG ⟩ - | start_ARG 1 end_ARG ⟩ ]=12⁢[|010⟩−|011⟩+|100⟩−|101⟩].absent12delimited-[]ket010ket011ket100ket101\displaystyle=\frac{1}{2}\big{[}\ket{010}-\ket{011}+\ket{100}-\ket{101}\big{]}\,.= divide start_ARG 1 end_ARG start_ARG 2 end_ARG [ | start_ARG 010 end_ARG ⟩ - | start_ARG 011 end_ARG ⟩ + | start_ARG 100 end_ARG ⟩ - | start_ARG 101 end_ARG ⟩ ] .(5)
- Action 5:

Alice makes measurements of the first and second qubits.
QG provides her with 4 chits that contain the 4 possible outcomes:
01, 11, 00, and 10.
Alice plays a lottery game – she randomly picks one out of the 4 chits. This action mimics
quantum measurement which is probabilistic. She immediately tells Bob what she got. In the game, Alice hands over her chit to Bob ((see Fig.8).
- Action 6:

Bob reads the pair of binary digits from the chit and tallies them with a chart.
We call itBob’s chart, derived from TableII.1, which simply tells
what gates he needs to operate on his present quantum state in order to convert his own
qubitq2subscript𝑞2q_{2}italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT’s state into|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩(see Fig.8(c)).
The chart reads{tblr}

colspec = —c—c—,
row1 = bg=TopRow, fg=black, j, row2 = bg=NormalRow, fg=black, c, row3 = bg=NormalRow, fg=black, c, row4 = bg=NormalRow, fg=black, c, row5 = bg=NormalRow, fg=black, c,Alice’s chitBob’s gate
00I𝐼{I}italic_I
01Z𝑍{Z}italic_Z
10X𝑋{X}italic_X
11Z⁢X𝑍𝑋{ZX}italic_Z italic_X

Table 2:Bob’s chart. The chart instructs what gate card(s) Bob needs to pick up and submit to QG
depending on what is written on the chit handed to him by Alice.(a)(b)(c)Figure 8:(a) Alice picks up a chit through a lottery. (b) All of the chits with 4 possible outcomes: ‘00’, ‘01’, ‘10’, ‘11’. (c) Bob looks into the information in the chit and applies his gate(s) accordingly.

Following the chart, Bob picks up (i) anI𝐼Iitalic_I-card (identity operation, i.e. no operation),
(ii) aZ𝑍Zitalic_Z-card, (iii) anX𝑋Xitalic_X-card or (iv) first anX𝑋Xitalic_X-card and then aZ𝑍Zitalic_Z-card when he finds00000000,01010101,10101010or11111111respectively written on Alice’s chit.
- Action 7:

Now, QG also separately creates a chart according to Alice’s measurement outcome (written on the chit). The chart contains the information of Bob’s state before he submits any gate cards to QG.{tblr}

colspec = —c—c—,
row1 = bg=TopRow, fg=black, j, row2 = bg=NormalRow, fg=black, c, row3 = bg=NormalRow, fg=black, c, row4 = bg=NormalRow, fg=black, c, row5 = bg=NormalRow, fg=black, c,Alice’s chitBob’s state
00|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩
01|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩
10−|1⟩ket1-\ket{1}- | start_ARG 1 end_ARG ⟩
11−|0⟩ket0-\ket{0}- | start_ARG 0 end_ARG ⟩
To verify if Bob’s gate operation has correctly generated|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩for his qubit, QG now reveals
the state to Bob following their chart.Action 8:Bob already knows his gate(s) and now after QG’s revelation, he knows his state before his gate operation(s). So he readily checks the final state of his qubit.
For instance, if Alice’s outcome is11111111, Bob’s chart readsZ⁢X𝑍𝑋ZXitalic_Z italic_Xand QG’s chart reads−|0⟩ket0-\ket{0}- | start_ARG 0 end_ARG ⟩. ActingZ⁢X𝑍𝑋ZXitalic_Z italic_Xon−|0⟩ket0-\ket{0}- | start_ARG 0 end_ARG ⟩, Bob obtains|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩[X𝑋Xitalic_X-gate first flips his qubit’s state and then changes the sign or phase of it]. This state is
the desired state|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩. QG confirms Bob’s final state is indeed|Q⟩ket𝑄\ket{Q}| start_ARG italic_Q end_ARG ⟩, which was originally supplied to Alice by them. Hence, the game ends.Table 3:QG’s chart for|Q⟩=|1⟩ket𝑄ket1\ket{Q}=\ket{1}| start_ARG italic_Q end_ARG ⟩ = | start_ARG 1 end_ARG ⟩.

## III.5What if|𝑸⟩=|𝟎⟩ket𝑸ket0\ket{Q}=\ket{0}bold_| start_ARG bold_italic_Q end_ARG bold_⟩ bold_= bold_| start_ARG bold_0 end_ARG bold_⟩?

Now, if QG decides to teleport the other kind of single quantum state, i.e.|Q⟩=|0⟩ket𝑄ket0\ket{Q}=\ket{0}| start_ARG italic_Q end_ARG ⟩ = | start_ARG 0 end_ARG ⟩,
the game rules and steps remain the same. However, QG updates the states
differently in their diary:|ψ0⟩ketsubscript𝜓0\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{0}}}| start_ARG italic_ψ start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_ARG ⟩=|0⟩⁢|0⟩⁢|0⟩=|000⟩.absentket0ket0ket0ket000\displaystyle=\ket{0}\ket{0}\ket{0}=\ket{000}\,.= | start_ARG 0 end_ARG ⟩ | start_ARG 0 end_ARG ⟩ | start_ARG 0 end_ARG ⟩ = | start_ARG 000 end_ARG ⟩ .(6)|ψ1⟩ketsubscript𝜓1\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{1}}}| start_ARG italic_ψ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩=H⁢(1)⁢|ψ0⟩=|0⟩⁢12⁢[|0⟩+|1⟩]⁢|0⟩absent𝐻1ketsubscript𝜓0ket012delimited-[]ket0ket1ket0\displaystyle=H(1)\ket{\psi_{0}}=\ket{0}\frac{1}{\sqrt{2}}\big{[}\ket{0}+\ket{%
1}\big{]}\ket{0}= italic_H ( 1 ) | start_ARG italic_ψ start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_ARG ⟩ = | start_ARG 0 end_ARG ⟩ divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 0 end_ARG ⟩ + | start_ARG 1 end_ARG ⟩ ] | start_ARG 0 end_ARG ⟩=12⁢[|000⟩+|010⟩]absent12delimited-[]ket000ket010\displaystyle=\frac{1}{\sqrt{2}}\big{[}\ket{000}+\ket{010}\big{]}= divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 000 end_ARG ⟩ + | start_ARG 010 end_ARG ⟩ ][after Alice submitsH⁢(1)𝐻1H(1)italic_H ( 1 )card.](7)|ψ2⟩ketsubscript𝜓2\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{2}}}| start_ARG italic_ψ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG ⟩=X^C⁢(1,2)⁢|ψ1⟩=12⁢[|000⟩+|110⟩]absentsubscript^𝑋𝐶12ketsubscript𝜓112delimited-[]ket000ket110\displaystyle=\hat{X}_{C}(1,2)\ket{\psi_{1}}=\frac{1}{\sqrt{2}}\big{[}\ket{000%
}+\ket{110}\big{]}= over^ start_ARG italic_X end_ARG start_POSTSUBSCRIPT italic_C end_POSTSUBSCRIPT ( 1 , 2 ) | start_ARG italic_ψ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG ⟩ = divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 000 end_ARG ⟩ + | start_ARG 110 end_ARG ⟩ ][after Alice submitsC⁢X⁢(1,2)𝐶𝑋12CX(1,2)italic_C italic_X ( 1 , 2 )card.](8)|ψ3⟩ketsubscript𝜓3\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{3}}}| start_ARG italic_ψ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT end_ARG ⟩=X^C⁢(0,1)⁢|ψ2⟩=12⁢[|000⟩+|110⟩]absentsubscript^𝑋𝐶01ketsubscript𝜓212delimited-[]ket000ket110\displaystyle=\hat{X}_{C}(0,1)\ket{\psi_{2}}=\frac{1}{\sqrt{2}}\big{[}\ket{000%
}+\ket{110}\big{]}= over^ start_ARG italic_X end_ARG start_POSTSUBSCRIPT italic_C end_POSTSUBSCRIPT ( 0 , 1 ) | start_ARG italic_ψ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_ARG ⟩ = divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ | start_ARG 000 end_ARG ⟩ + | start_ARG 110 end_ARG ⟩ ][unaltered, after Alice submitsC⁢X⁢(0,1)𝐶𝑋01CX(0,1)italic_C italic_X ( 0 , 1 )card.](9)|ψ4⟩ketsubscript𝜓4\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{4}}}| start_ARG italic_ψ start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT end_ARG ⟩=H^(0)|ψ3⟩=12|00⟩[|0⟩+|1⟩]+12|11⟩[(|0⟩+|1⟩]\displaystyle={\hat{H}}(0)\ket{\psi_{3}}=\frac{1}{2}\ket{00}\big{[}\ket{0}+%
\ket{1}\big{]}+\frac{1}{2}\ket{11}\big{[}(\ket{0}+\ket{1}\big{]}= over^ start_ARG italic_H end_ARG ( 0 ) | start_ARG italic_ψ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT end_ARG ⟩ = divide start_ARG 1 end_ARG start_ARG 2 end_ARG | start_ARG 00 end_ARG ⟩ [ | start_ARG 0 end_ARG ⟩ + | start_ARG 1 end_ARG ⟩ ] + divide start_ARG 1 end_ARG start_ARG 2 end_ARG | start_ARG 11 end_ARG ⟩ [ ( | start_ARG 0 end_ARG ⟩ + | start_ARG 1 end_ARG ⟩ ][after Alice submitsH⁢(0)𝐻0H(0)italic_H ( 0 )card]=12⁢[|000⟩+|001⟩+|110⟩+|111⟩].absent12delimited-[]ket000ket001ket110ket111\displaystyle=\frac{1}{2}\big{[}\ket{000}+\ket{001}+\ket{110}+\ket{111}\big{]}\,.= divide start_ARG 1 end_ARG start_ARG 2 end_ARG [ | start_ARG 000 end_ARG ⟩ + | start_ARG 001 end_ARG ⟩ + | start_ARG 110 end_ARG ⟩ + | start_ARG 111 end_ARG ⟩ ] .(10)

Just like in the previous scenario, Alice again picks one classical bit-pair out of the set {00, 01, 10, 11} and Bob follows the same chart. However, for the verification of the successful QT, QG provides a different chart to Bob:{tblr}

colspec = —c—c—,
row1 = bg=TopRow, fg=black, j, row2 = bg=NormalRow, fg=black, c, row3 = bg=NormalRow, fg=black, c, row4 = bg=NormalRow, fg=black, c, row5 = bg=NormalRow, fg=black, c,Alice’s chitBob’s state
00|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩
01|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩
10|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩
11|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩

Note that, in the above,Z𝑍Zitalic_Zgate acts like an identity operator since the operated state remain always in state|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩.Table 4:QG’s chart for|Q⟩=|0⟩ket𝑄ket0\ket{Q}=\ket{0}| start_ARG italic_Q end_ARG ⟩ = | start_ARG 0 end_ARG ⟩.

## III.6What if|𝑸⟩=𝒂⁢|𝟎⟩+𝒃⁢|𝟏⟩ket𝑸𝒂ket0𝒃ket1\ket{Q}=a\ket{0}+b\ket{1}bold_| start_ARG bold_italic_Q end_ARG bold_⟩ bold_= bold_italic_a bold_| start_ARG bold_0 end_ARG bold_⟩ bold_+ bold_italic_b bold_| start_ARG bold_1 end_ARG bold_⟩(𝒂≠𝟎𝒂0a\neq 0bold_italic_a bold_≠ bold_0,𝒃≠𝟎𝒃0b\neq 0bold_italic_b bold_≠ bold_0) ?

If QG plans to teleport a generic superposition state|Q⟩=a⁢|0⟩+b⁢|1⟩ket𝑄𝑎ket0𝑏ket1\ket{Q}=a\ket{0}+b\ket{1}| start_ARG italic_Q end_ARG ⟩ = italic_a | start_ARG 0 end_ARG ⟩ + italic_b | start_ARG 1 end_ARG ⟩, as already discussed in Sec.II, QG notes down
the states that are combinations of the updates for both|Q⟩=|0⟩ket𝑄ket0\ket{Q}=\ket{0}| start_ARG italic_Q end_ARG ⟩ = | start_ARG 0 end_ARG ⟩and|Q⟩=|1⟩ket𝑄ket1\ket{Q}=\ket{1}| start_ARG italic_Q end_ARG ⟩ = | start_ARG 1 end_ARG ⟩with appropriate coefficientsa𝑎aitalic_aandb𝑏bitalic_b. Instead of mentioning all of them, we mention
the final update:|ψ4⟩ketsubscript𝜓4\displaystyle{\color[rgb]{0,0,1}\ket{\psi_{4}}}| start_ARG italic_ψ start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT end_ARG ⟩=12[[a|0⟩+b|1⟩]|00⟩+[a|0⟩−b|1⟩]|01⟩\displaystyle=\frac{1}{2}\bigg{[}\big{[}a\ket{0}+b\ket{1}\big{]}\ket{00}+\big{%
[}a\ket{0}-b\ket{1}\big{]}\ket{01}= divide start_ARG 1 end_ARG start_ARG 2 end_ARG [ [ italic_a | start_ARG 0 end_ARG ⟩ + italic_b | start_ARG 1 end_ARG ⟩ ] | start_ARG 00 end_ARG ⟩ + [ italic_a | start_ARG 0 end_ARG ⟩ - italic_b | start_ARG 1 end_ARG ⟩ ] | start_ARG 01 end_ARG ⟩[a|1⟩+b|0⟩]|10⟩+[a|1⟩−b|0⟩]|11⟩].\displaystyle\quad\big{[}a\ket{1}+b\ket{0}\big{]}\ket{10}+\big{[}a\ket{1}-b%
\ket{0}\big{]}\ket{11}\bigg{]}\,.[ italic_a | start_ARG 1 end_ARG ⟩ + italic_b | start_ARG 0 end_ARG ⟩ ] | start_ARG 10 end_ARG ⟩ + [ italic_a | start_ARG 1 end_ARG ⟩ - italic_b | start_ARG 0 end_ARG ⟩ ] | start_ARG 11 end_ARG ⟩ ] .(11)

This state is the same as the state described in Eq. (5).
Following this, QG reveals the following chart to Bob before he applies his gates
to verify the teleported state.{tblr}

colspec = —c—c—,
row1 = bg=TopRow, fg=black, j, row2 = bg=NormalRow, fg=black, c, row3 = bg=NormalRow, fg=black, c, row4 = bg=NormalRow, fg=black, c, row5 = bg=NormalRow, fg=black, c,Alice’s chitBob’s state
00 a|0⟩+b⁢|1⟩ket0𝑏ket1\ket{0}+b\ket{1}| start_ARG 0 end_ARG ⟩ + italic_b | start_ARG 1 end_ARG ⟩
01 a|0⟩−b⁢|1⟩ket0𝑏ket1\ket{0}-b\ket{1}| start_ARG 0 end_ARG ⟩ - italic_b | start_ARG 1 end_ARG ⟩
10 a|1⟩+b⁢|0⟩ket1𝑏ket0\ket{1}+b\ket{0}| start_ARG 1 end_ARG ⟩ + italic_b | start_ARG 0 end_ARG ⟩
11 a|1⟩−b⁢|0⟩ket1𝑏ket0\ket{1}-b\ket{0}| start_ARG 1 end_ARG ⟩ - italic_b | start_ARG 0 end_ARG ⟩

Table 5:QG’s chart for|Q⟩=a⁢|0⟩+b⁢|1⟩ket𝑄𝑎ket0𝑏ket1\ket{Q}=a\ket{0}+b\ket{1}| start_ARG italic_Q end_ARG ⟩ = italic_a | start_ARG 0 end_ARG ⟩ + italic_b | start_ARG 1 end_ARG ⟩.

## IVSummary

In this paper, we discussed a simple game that involves three players to demonstrate quantum teleportation of a single qubit. Quantum teleportation is a complex concept and such demonstration can be useful to engage undergraduate students in learning the basics of it or train teachers who may find it useful in their teaching. Very recently, Nunavathet al.[36]proposed aqandies(quantum candies) model[37,38]that describes the QT protocol in terms of the candies’ classical entities (e.g. colors and tastes). In principle, instead of the ‘quantum’ chits can be replaced by qandies, that Alice picks up during her measurement through a lottery. Our kind of game can be modified and played for other entanglement based protocols such as superdense coding[39], entanglement swapping[40], and quantum key distribution[26,27].

## Acknowledgements.HB thanks Ananya Vinod (played the role of Alice), Daksh Gupta (played Bob), Arkaprava Bose (played Quantum God), and other NIUS students without whose enthusiastic participation, the game could not have been conducted successfully and this article would not have seen its final version. He also thanks Karthik Shetty and Mamatha Maddur from HBCSE, Mumbai, for providing the necessary equipment. Ananya, Karthik, and Spandan Mandal helped him by providing with some needful images. The author is also indebted to Dr Praveen Pathak, the organizer of the NIUS Physics 2024 camp at HBCSE and Dr Deepak Garg for taking part in very engaging discussions during the planning and demonstration of the game. Finally, he thanks IBM for its open-sourceQiskitSDK, which is used in generating quantum circuit diagrams discussed in the paper.

## Appendix ABasic quantum gates

We briefly discuss the gates that have been used in the QT protocol discussed in the main part of the paper.
All of these gates can be represented by2×2222\times 22 × 2unitary Hermitian matrices which act on the single qubit bases|0⟩=[10]ket0matrix10\ket{0}=\begin{bmatrix}1\\
0\end{bmatrix}| start_ARG 0 end_ARG ⟩ = [ start_ARG start_ROW start_CELL 1 end_CELL end_ROW start_ROW start_CELL 0 end_CELL end_ROW end_ARG ]and|1⟩=[01]ket1matrix01\ket{1}=\begin{bmatrix}0\\
1\end{bmatrix}| start_ARG 1 end_ARG ⟩ = [ start_ARG start_ROW start_CELL 0 end_CELL end_ROW start_ROW start_CELL 1 end_CELL end_ROW end_ARG ]during the protocol operations. Note that in this basis set, a generic2×2222\times 22 × 2matrixM^^𝑀\hat{M}over^ start_ARG italic_M end_ARGwith elementsα𝛼\alphaitalic_α,β𝛽\betaitalic_β,γ𝛾\gammaitalic_γ, andδ𝛿\deltaitalic_δcan
be expressed asM=[αβγδ]=α⁢|0⟩⁢⟨0|+β⁢|0⟩⁢⟨1|+γ⁢|1⟩⁢⟨0|+δ⁢|1⟩⁢⟨1|.𝑀matrix𝛼𝛽𝛾𝛿𝛼ket0bra0𝛽ket0bra1𝛾ket1bra0𝛿ket1bra1\displaystyle M=\begin{bmatrix}\alpha&\beta\\
\gamma&\delta\end{bmatrix}=\alpha\ket{0}\bra{0}+\beta\ket{0}\bra{1}+\gamma\ket%
{1}\bra{0}+\delta\ket{1}\bra{1}\,.italic_M = [ start_ARG start_ROW start_CELL italic_α end_CELL start_CELL italic_β end_CELL end_ROW start_ROW start_CELL italic_γ end_CELL start_CELL italic_δ end_CELL end_ROW end_ARG ] = italic_α | start_ARG 0 end_ARG ⟩ ⟨ start_ARG 0 end_ARG | + italic_β | start_ARG 0 end_ARG ⟩ ⟨ start_ARG 1 end_ARG | + italic_γ | start_ARG 1 end_ARG ⟩ ⟨ start_ARG 0 end_ARG | + italic_δ | start_ARG 1 end_ARG ⟩ ⟨ start_ARG 1 end_ARG | .(1)

If the matrix elements become individual matrices themselves (e.g.α^,β^,γ^,δ^^𝛼^𝛽^𝛾^𝛿{\hat{\alpha}},{\hat{\beta}},{\hat{\gamma}},{\hat{\delta}}over^ start_ARG italic_α end_ARG , over^ start_ARG italic_β end_ARG , over^ start_ARG italic_γ end_ARG , over^ start_ARG italic_δ end_ARG), we haveM~~𝑀\displaystyle\tilde{M}over~ start_ARG italic_M end_ARG=[α^β^γ^δ^]=α^⊗|0⟩⁢⟨0|+β^⊗|0⟩⁢⟨1|absentmatrix^𝛼^𝛽^𝛾^𝛿tensor-product^𝛼ket0bra0tensor-product^𝛽ket0bra1\displaystyle=\begin{bmatrix}{\hat{\alpha}}&{\hat{\beta}}\\
{\hat{\gamma}}&{\hat{\delta}}\end{bmatrix}={\hat{\alpha}}\otimes\ket{0}\bra{0}%
+{\hat{\beta}}\otimes\ket{0}\bra{1}= [ start_ARG start_ROW start_CELL over^ start_ARG italic_α end_ARG end_CELL start_CELL over^ start_ARG italic_β end_ARG end_CELL end_ROW start_ROW start_CELL over^ start_ARG italic_γ end_ARG end_CELL start_CELL over^ start_ARG italic_δ end_ARG end_CELL end_ROW end_ARG ] = over^ start_ARG italic_α end_ARG ⊗ | start_ARG 0 end_ARG ⟩ ⟨ start_ARG 0 end_ARG | + over^ start_ARG italic_β end_ARG ⊗ | start_ARG 0 end_ARG ⟩ ⟨ start_ARG 1 end_ARG |+γ^⊗|1⟩⁢⟨0|+δ^⊗|1⟩⁢⟨1|.tensor-product^𝛾ket1bra0tensor-product^𝛿ket1bra1\displaystyle\quad+{\hat{\gamma}}\otimes\ket{1}\bra{0}+{\hat{\delta}}\otimes%
\ket{1}\bra{1}\,.+ over^ start_ARG italic_γ end_ARG ⊗ | start_ARG 1 end_ARG ⟩ ⟨ start_ARG 0 end_ARG | + over^ start_ARG italic_δ end_ARG ⊗ | start_ARG 1 end_ARG ⟩ ⟨ start_ARG 1 end_ARG | .(2)

We follow the above two identities to express gate matrices in the discussion below.

## A.1Pauli gates

The four Pauli matrices act as gates on a single qubit and they are represented asX^^𝑋\displaystyle\hat{X}over^ start_ARG italic_X end_ARG=[0110]=|0⟩⁢⟨1|+|1⟩⁢⟨0|.absentmatrix0110ket0bra1ket1bra0\displaystyle=\begin{bmatrix}0&1\\
1&0\end{bmatrix}=\ket{0}\bra{1}+\ket{1}\bra{0}\,.= [ start_ARG start_ROW start_CELL 0 end_CELL start_CELL 1 end_CELL end_ROW start_ROW start_CELL 1 end_CELL start_CELL 0 end_CELL end_ROW end_ARG ] = | start_ARG 0 end_ARG ⟩ ⟨ start_ARG 1 end_ARG | + | start_ARG 1 end_ARG ⟩ ⟨ start_ARG 0 end_ARG | .(3)Y^^𝑌\displaystyle\hat{Y}over^ start_ARG italic_Y end_ARG=[0−ii0]=i⁢[|0⟩⁢⟨1|−|1⟩⁢⟨0|].absentmatrix0𝑖𝑖0𝑖delimited-[]ket0bra1ket1bra0\displaystyle=\begin{bmatrix}0&-i\\
i&0\end{bmatrix}=i\big{[}\ket{0}\bra{1}-\ket{1}\bra{0}]\,.= [ start_ARG start_ROW start_CELL 0 end_CELL start_CELL - italic_i end_CELL end_ROW start_ROW start_CELL italic_i end_CELL start_CELL 0 end_CELL end_ROW end_ARG ] = italic_i [ | start_ARG 0 end_ARG ⟩ ⟨ start_ARG 1 end_ARG | - | start_ARG 1 end_ARG ⟩ ⟨ start_ARG 0 end_ARG | ] .(4)Z^^𝑍\displaystyle\hat{Z}over^ start_ARG italic_Z end_ARG=[100−1]=|0⟩⁢⟨0|−|1⟩⁢⟨1|.absentmatrix1001ket0bra0ket1bra1\displaystyle=\begin{bmatrix}1&0\\
0&-1\end{bmatrix}=\ket{0}\bra{0}-\ket{1}\bra{1}\,.= [ start_ARG start_ROW start_CELL 1 end_CELL start_CELL 0 end_CELL end_ROW start_ROW start_CELL 0 end_CELL start_CELL - 1 end_CELL end_ROW end_ARG ] = | start_ARG 0 end_ARG ⟩ ⟨ start_ARG 0 end_ARG | - | start_ARG 1 end_ARG ⟩ ⟨ start_ARG 1 end_ARG | .(5)I^^𝐼\displaystyle\hat{I}over^ start_ARG italic_I end_ARG=[1001]=|0⟩⁢⟨0|+|1⟩⁢⟨1|.absentmatrix1001ket0bra0ket1bra1\displaystyle=\begin{bmatrix}1&0\\
0&1\end{bmatrix}=\ket{0}\bra{0}+\ket{1}\bra{1}\,.= [ start_ARG start_ROW start_CELL 1 end_CELL start_CELL 0 end_CELL end_ROW start_ROW start_CELL 0 end_CELL start_CELL 1 end_CELL end_ROW end_ARG ] = | start_ARG 0 end_ARG ⟩ ⟨ start_ARG 0 end_ARG | + | start_ARG 1 end_ARG ⟩ ⟨ start_ARG 1 end_ARG | .(6)

The above operators becomeX𝑋Xitalic_X,Y𝑌Yitalic_Y,Z𝑍Zitalic_Z, andI𝐼Iitalic_Igates. It is easy to see that anX𝑋Xitalic_Xgate acts as a bit-flip orNOTgate as it changes qubit|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩to|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩and vice-versa.Y𝑌Yitalic_Ygate (not part of the QT protocol), also flips the bit, however, it picks up a negative sign (ei⁢πsuperscript𝑒𝑖𝜋e^{i\pi}italic_e start_POSTSUPERSCRIPT italic_i italic_π end_POSTSUPERSCRIPTphase) when operated on|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩. Similarly, the identity Pauli matrix acts as anI𝐼Iitalic_Igate, causing no changes in the quantum states whileZ𝑍Zitalic_Zgate changes the sign of the amplitude of|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩when acted on it.

## A.2Hadamard (H𝐻Hitalic_H) gate

The Hadamard orH𝐻Hitalic_Hgate is a combination ofX𝑋Xitalic_XandZ𝑍Zitalic_Zgates with a normalization factor (1/2)1/\sqrt{2})1 / square-root start_ARG 2 end_ARG )). In operator form:H^=12⁢[X^+Z^]=12⁢[111−1].^𝐻12delimited-[]^𝑋^𝑍12matrix1111\displaystyle\hat{H}=\frac{1}{\sqrt{2}}\big{[}\hat{X}+\hat{Z}\big{]}=\frac{1}{%
\sqrt{2}}\begin{bmatrix}1&1\\
1&-1\end{bmatrix}\,.over^ start_ARG italic_H end_ARG = divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ over^ start_ARG italic_X end_ARG + over^ start_ARG italic_Z end_ARG ] = divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ start_ARG start_ROW start_CELL 1 end_CELL start_CELL 1 end_CELL end_ROW start_ROW start_CELL 1 end_CELL start_CELL - 1 end_CELL end_ROW end_ARG ] .(7)

From Eq. (3) and Eq. (5), one can write the operator in terms of outer product formH^=12⁢[[|0⟩+|1⟩]⁢⟨0|+[|0⟩−|1⟩]⁢⟨1|].^𝐻12delimited-[]delimited-[]ket0ket1bra0delimited-[]ket0ket1bra1\displaystyle\hat{H}=\frac{1}{\sqrt{2}}\bigg{[}{\color[rgb]{0.0,0.5,0.2}\big{[%
}\ket{0}+\ket{1}\big{]}}\bra{0}+{\color[rgb]{0.0,0.5,0.2}\big{[}\ket{0}-\ket{1%
}\big{]}}\bra{1}\bigg{]}\,.over^ start_ARG italic_H end_ARG = divide start_ARG 1 end_ARG start_ARG square-root start_ARG 2 end_ARG end_ARG [ [ | start_ARG 0 end_ARG ⟩ + | start_ARG 1 end_ARG ⟩ ] ⟨ start_ARG 0 end_ARG | + [ | start_ARG 0 end_ARG ⟩ - | start_ARG 1 end_ARG ⟩ ] ⟨ start_ARG 1 end_ARG | ] .(8)

Thus,H𝐻Hitalic_Hgate creates a superposition state|0⟩±|1⟩plus-or-minusket0ket1\ket{0}\pm\ket{1}| start_ARG 0 end_ARG ⟩ ± | start_ARG 1 end_ARG ⟩, with the normalization factor1/2121/\sqrt{2}1 / square-root start_ARG 2 end_ARG, when acted on|0⟩ket0\ket{0}| start_ARG 0 end_ARG ⟩and|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩, respectively.

## A.3Controlled gates

C⁢X𝐶𝑋CXitalic_C italic_XandC⁢Z𝐶𝑍CZitalic_C italic_Zgates stand forcontrolledX𝑋Xitalic_XandZ𝑍Zitalic_Zgates respectively and they are two-qubit gates.
In a two-qubit state, if the first qubit (control bit) is in state|1⟩ket1\ket{1}| start_ARG 1 end_ARG ⟩, then a controlled gate operates on the second qubit (target bit). The indices of the qubits are mentioned orderwise in the parentheses after the name of the gate. Operators representingC⁢X⁢(0,1)𝐶𝑋01CX(0,1)italic_C italic_X ( 0 , 1 )andC⁢Z⁢(0,1)𝐶𝑍01CZ(0,1)italic_C italic_Z ( 0 , 1 )gates are defined as (here00is the first/control bit,1111is the second/target bit)(a)(b)Figure 9:(a)C⁢X𝐶𝑋CXitalic_C italic_Xand (b)C⁢Z𝐶𝑍CZitalic_C italic_Zgates for input qubits|x⟩ket𝑥\ket{x}| start_ARG italic_x end_ARG ⟩and|y⟩ket𝑦\ket{y}| start_ARG italic_y end_ARG ⟩. One of the outputs remains the same as one of the inputs (control bit|x⟩ket𝑥\ket{x}| start_ARG italic_x end_ARG ⟩) in both gates. AfterC⁢X𝐶𝑋CXitalic_C italic_Xgate operation the other output for the target bit|y⟩ket𝑦\ket{y}| start_ARG italic_y end_ARG ⟩becomes the output of a classicalX⁢O⁢R𝑋𝑂𝑅XORitalic_X italic_O italic_Rgate. In case ofC⁢Z𝐶𝑍CZitalic_C italic_Zoperation, the target bit’s output conditionally changes its sign:|y⟩→−|y⟩→ket𝑦ket𝑦\ket{y}\to-\ket{y}| start_ARG italic_y end_ARG ⟩ → - | start_ARG italic_y end_ARG ⟩only when|x⟩=|1⟩ket𝑥ket1\ket{x}=\ket{1}| start_ARG italic_x end_ARG ⟩ = | start_ARG 1 end_ARG ⟩.X^C⁢(0,1)subscript^𝑋𝐶01\displaystyle\hat{X}_{C}(0,1)over^ start_ARG italic_X end_ARG start_POSTSUBSCRIPT italic_C end_POSTSUBSCRIPT ( 0 , 1 )=[I^00X^]absentmatrix^𝐼00^𝑋\displaystyle=\begin{bmatrix}{\hat{I}}&0\\
0&{\hat{X}}\end{bmatrix}= [ start_ARG start_ROW start_CELL over^ start_ARG italic_I end_ARG end_CELL start_CELL 0 end_CELL end_ROW start_ROW start_CELL 0 end_CELL start_CELL over^ start_ARG italic_X end_ARG end_CELL end_ROW end_ARG ]=I^⊗|0⟩⁢⟨0|+X^⊗|1⟩⁢⟨1|absenttensor-product^𝐼ket0bra0tensor-product^𝑋ket1bra1\displaystyle\quad={\hat{I}}\otimes\ket{0}\bra{0}+{\hat{X}}\otimes\ket{1}\bra{1}= over^ start_ARG italic_I end_ARG ⊗ | start_ARG 0 end_ARG ⟩ ⟨ start_ARG 0 end_ARG | + over^ start_ARG italic_X end_ARG ⊗ | start_ARG 1 end_ARG ⟩ ⟨ start_ARG 1 end_ARG |=|00⟩⁢⟨00|+|10⟩⁢⟨10|+|01⟩⁢⟨11|+|11⟩⁢⟨01|.absentket00bra00ket10bra10ket01bra11ket11bra01\displaystyle\quad=\ket{00}\bra{00}+\ket{10}\bra{10}+\ket{01}\bra{11}+\ket{11}%
\bra{01}\,.= | start_ARG 00 end_ARG ⟩ ⟨ start_ARG 00 end_ARG | + | start_ARG 10 end_ARG ⟩ ⟨ start_ARG 10 end_ARG | + | start_ARG 01 end_ARG ⟩ ⟨ start_ARG 11 end_ARG | + | start_ARG 11 end_ARG ⟩ ⟨ start_ARG 01 end_ARG | .(9)X^Z⁢(0,1)subscript^𝑋𝑍01\displaystyle\hat{X}_{Z}(0,1)over^ start_ARG italic_X end_ARG start_POSTSUBSCRIPT italic_Z end_POSTSUBSCRIPT ( 0 , 1 )=[I^00Z^]absentmatrix^𝐼00^𝑍\displaystyle=\begin{bmatrix}{\hat{I}}&0\\
0&{\hat{Z}}\end{bmatrix}= [ start_ARG start_ROW start_CELL over^ start_ARG italic_I end_ARG end_CELL start_CELL 0 end_CELL end_ROW start_ROW start_CELL 0 end_CELL start_CELL over^ start_ARG italic_Z end_ARG end_CELL end_ROW end_ARG ]=I^⊗|0⟩⁢⟨0|+Z^⊗|1⟩⁢⟨1|absenttensor-product^𝐼ket0bra0tensor-product^𝑍ket1bra1\displaystyle\quad={\hat{I}}\otimes\ket{0}\bra{0}+{\hat{Z}}\otimes\ket{1}\bra{1}= over^ start_ARG italic_I end_ARG ⊗ | start_ARG 0 end_ARG ⟩ ⟨ start_ARG 0 end_ARG | + over^ start_ARG italic_Z end_ARG ⊗ | start_ARG 1 end_ARG ⟩ ⟨ start_ARG 1 end_ARG |=|00⟩⁢⟨00|+|10⟩⁢⟨10|+|01⟩⁢⟨01|−|11⟩⁢⟨11|.absentket00bra00ket10bra10ket01bra01ket11bra11\displaystyle\quad=\ket{00}\bra{00}+\ket{10}\bra{10}+\ket{01}\bra{01}-\ket{11}%
\bra{11}\,.= | start_ARG 00 end_ARG ⟩ ⟨ start_ARG 00 end_ARG | + | start_ARG 10 end_ARG ⟩ ⟨ start_ARG 10 end_ARG | + | start_ARG 01 end_ARG ⟩ ⟨ start_ARG 01 end_ARG | - | start_ARG 11 end_ARG ⟩ ⟨ start_ARG 11 end_ARG | .(10)

Note that the first bit after theC⁢X𝐶𝑋CXitalic_C italic_Xoperation remains unchanged while
the second output becomes the classicalX⁢O⁢R𝑋𝑂𝑅XORitalic_X italic_O italic_Routput of the two input bits. This justifies theX⁢O⁢R𝑋𝑂𝑅XORitalic_X italic_O italic_Rsymbol in the control bit node of the diagrammatic representation (see Fig.9(a)). On the other hand,C⁢Z𝐶𝑍CZitalic_C italic_Zallows sign change for the second bit only when the first bit is1111, lacking a classical gate analog. One can showC⁢Z⁢(0,1)=C⁢Z⁢(1,0)𝐶𝑍01𝐶𝑍10CZ(0,1)=CZ(1,0)italic_C italic_Z ( 0 , 1 ) = italic_C italic_Z ( 1 , 0 ), i.e. the control and target bits are interchangeable and hence both bit-nodes are represented by the control-node symbol (filled circle, see Fig.9(b)).

## References
- [1]https://www.imdb.com/title/tt0063023/.
- Bennettet al.[1993]C. H. Bennett, G. Brassard,
C. Crépeau, R. Jozsa, A. Peres,  and W. K. Wootters,Phys. Rev. Lett.70, 1895 (1993).
- Bouwmeesteret al.[1997]D. Bouwmeester, J.-W. Pan, K. Mattle,
M. Eibl, H. Weinfurter,  and A. Zeilinger,Nature390, 575 (1997).
- Braunstein and Kimble [1998]S. L. Braunstein and H. J. Kimble,Phys. Rev. Lett.80, 869 (1998).
- Nielsenet al.[1998]M. A. Nielsen, E. Knill,  and R. Laflamme,Nature396, 52 (1998).
- Furusawaet al.[1998]A. Furusawa, J. L. Sørensen, S. L. Braunstein, C. A. Fuchs, H. J. Kimble,  and E. S. Polzik,Science282, 706 (1998).
- Takeiet al.[2005]N. Takei, T. Aoki,
S. Koike, K.-i. Yoshino, K. Wakui, H. Yonezawa, T. Hiraoka, J. Mizuno, M. Takeoka, M. Ban,  and A. Furusawa,Phys. Rev. A72, 042304 (2005).
- Riebeet al.[2004]M. Riebe, H. Häffner,
C. F. Roos, W. Hänsel, J. Benhelm, G. P. T. Lancaster, T. W. Körber, C. Becher, F. Schmidt-Kaler, D. F. V. James,  and R. Blatt,Nature429, 734 (2004).
- Barrettet al.[2004]M. D. Barrett, J. Chiaverini,
T. Schaetz, J. Britton, W. M. Itano, J. D. Jost, E. Knill, C. Langer, D. Leibfried, R. Ozeri,  and D. J. Wineland,Nature429, 737 (2004).
- Wanet al.[2019]Y. Wanet al.,Science364, 875 (2019).
- Shersonet al.[2006]J. F. Sherson, H. Krauter,
R. K. Olsson, B. Julsgaard, K. Hammerer, I. Cirac,  and E. S. Polzik,Nature443, 557 (2006).
- Pfaffet al.[2014]Pfaffet al.,Science345, eaau1255 (2014).
- Reindlet al.[2018]M. Reindlet al.,Science Advances4, eaau1255 (2018).
- Steffenet al.[2013]L. Steffen, Y. Salathe,
M. Oppliger, P. Kurpiers, M. Baur, C. Lang, C. Eichler, G. Puebla-Hellmann, A. Fedorov,  and A. Wallraff,Nature500, 319 (2013).
- Pirandolaet al.[2015]S. Pirandola, J. Eisert,
C. Weedbrook, A. Furusawa,  and S. L. Braunstein,Nature Photonics9, 641 (2015).
- Huet al.[2023]X.-M. Hu, Y. Guo, B.-H. Liu, C.-F. Li,  and G.-C. Guo,Nature Reviews Physics5, 339 (2023).
- Bouwmeesteret al.[1999]D. Bouwmeester, J.-W. Pan, M. Daniell,
H. Weinfurter,  and A. Zeilinger,Phys. Rev. Lett.82, 1345 (1999).
- Panet al.[2001]J.-W. Pan, M. Daniell,
S. Gasparoni, G. Weihs,  and A. Zeilinger,Phys. Rev. Lett.86, 4435 (2001).
- Zhaoet al.[2004]Z. Zhao, Y.-A. Chen,
A.-N. Zhang, T. Yang, H. J. Briegel,  and J.-W. Pan,Nature430, 54 (2004).
- Mafuet al.[2013]M. Mafu, A. Dudley,
S. Goyal, D. Giovannini, M. McLaren, M. J. Padgett, T. Konrad, F. Petruccione, N. Lütkenhaus,  and A. Forbes,Phys. Rev. A88, 032305 (2013).
- Luoet al.[2019]Y.-H. Luo, H.-S. Zhong,
M. Erhard, X.-L. Wang, L.-C. Peng, M. Krenn, X. Jiang, L. Li, N.-L. Liu, C.-Y. Lu, A. Zeilinger,  and J.-W. Pan,Phys. Rev. Lett.123, 070505 (2019).
- Zhanget al.[2019]C. Zhang, J. F. Chen,
C. Cui, J. P. Dowling, Z. Y. Ou,  and T. Byrnes,Phys. Rev. A100, 032330 (2019).
- Erhardet al.[2020]M. Erhard, M. Krenn,  and A. Zeilinger,Nature Reviews Physics2, 365 (2020).
- Huet al.[2020]X.-M. Hu, C. Zhang, B.-H. Liu, Y. Cai, X.-J. Ye, Y. Guo, W.-B. Xing, C.-X. Huang, Y.-F. Huang,
C.-F. Li,  and G.-C. Guo,Phys. Rev. Lett.125, 230501 (2020).
- Renet al.[2017]J.-G. Renet al.,Nature549, 70 (2017).
- Bennett and Brassard [2014]C. H. Bennett and G. Brassard (Elsevier BV, 2014) p. 7–11.
- Ekert [1991]A. K. Ekert,Phys. Rev. Lett.67, 661 (1991).
- Ciracet al.[1997]J. I. Cirac, P. Zoller,
H. J. Kimble,  and H. Mabuchi,Phys. Rev. Lett.78, 3221 (1997).
- Kimble [2008]H. J. Kimble,Nature453, 1023 (2008).
- Wehneret al.[2018]S. Wehner, D. Elkouss,  and R. Hanson,Science362, eaam928
(2018).
- Raussendorf and Briegel [2001]R. Raussendorf and H. J. Briegel,Phys. Rev. Lett.86, 5188 (2001).
- Briegelet al.[2009]H. J. Briegel, D. E. Browne,
W. Dür, R. Raussendorf,  and M. Van den Nest,Nature
Physics5, 19 (2009).
- Briegelet al.[1998]H.-J. Briegel, W. Dür,
J. I. Cirac,  and P. Zoller,Phys. Rev. Lett.81, 5932 (1998).
- Nielsen and Chuang [2010]M. A. Nielsen and I. L. Chuang,Quantum Computation and Quantum Information: 10th
Anniversary Edition(Cambridge University Press, Cambridge, 2010).
- Wootters and Zurek [1982]W. K. Wootters and W. H. Zurek,Nature299, 802 (1982).
- Nunavathet al.[2024]N. Nunavath, S. Mishra,  and A. Pathak,“Quantum
teleportation using quantum candies,”(2024),arXiv:2408.16016 [physics.pop-ph].
- Lin and Mor [2020]J. Lin and T. Mor, inTheory and Practice of Natural Computing(Springer International Publishing, Cham, 2020) pp. 69–81.
- Linet al.[2021]J. Lin, T. Mor,  and R. Shapira,“Quantum
information and beyond – with quantum candies,”(2021),arXiv:2110.01402
[physics.ed-ph].
- Bennett and Wiesner [1992]C. H. Bennett and S. J. Wiesner,Phys. Rev. Lett.69, 2881 (1992).
- Żukowskiet al.[1993]M. Żukowski, A. Zeilinger, M. A. Horne,  and A. K. Ekert,Phys. Rev. Lett.71, 4287 (1993).
