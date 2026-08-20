# Chapter 3 object inventory audit

Scope: source PDF pages 108--145, covering the complete Chapter 3 native
transcription and its chapter bibliography.

Source identity:

- Canonical source: origPapers/pct_spin_statistics_all_that.pdf
- Source SHA-256: 44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889
- Native files: latex/chapters/chapter03/opening.tex,
  sec3_1.tex, sec3_2.tex, sec3_3.tex, sec3_4.tex, sec3_5.tex, and
  bibliography.tex
- Source page markers: every page 108--145 occurs once in the Chapter 3
  chunks, with no marker outside that interval.

The inventory below records every source-numbered equation, theorem, proof,
footnote, and bibliography item. Formula text follows the native Dirac
notation and retains the source's mathematical content. Source page numbers
refer to the PDF, while file locations refer to the native TeX.

## Page and boundary ledger

| Source PDF pages | Native chunk | Boundary check |
| --- | --- | --- |
| 108--114 | sec3_1.tex | Section 3-1, axioms O--IV, examples, field-theory definition, cyclicity proof, and the handoff to Section 3-2 |
| 114--117 | sec3_2.tex | Section 3-2 begins on PDF 114 after the end of axiom IV and closes before Section 3-3 |
| 118--128 | sec3_3.tex | Section 3-3, equations (3-19)--(3-41), Theorems 3-1--3-6; PDF 128 ends at the word “can” |
| 129--138 | sec3_4.tex | The continuation of the linear-program paragraph begins on PDF 129, then Section 3-4 and Theorem 3-7; the proof closes before Section 3-5 |
| 138--144 | sec3_5.tex | Section 3-5, Theorems 3-8--3-9, and the chapter conclusion |
| 144--145 | bibliography.tex | Chapter bibliography, visible references [1]--[17] |

The PDF 128 to 129 sentence boundary is continuous:
sec3_3.tex ends with “once we have computed the domain of holomorphy
explicitly, we can”, and sec3_4.tex begins with “express the function in
terms of its boundary values ...”. The continuation appears before the
Section 3-4 heading. PDF 138 likewise carries the final reconstruction-proof
paragraph into the Section 3-5 heading without an object inserted between the
proof ending and the new section.

## Numbered equation inventory

The numbered sequence contains 67 unique tags. The entries below give the
complete displayed formula, source PDF page, and native location.

### Section 3-1, equations (3-1)--(3-8)

- (3-1), PDF 109, sec3_1.tex:64--68:
  \(U(a,A)\ket{\Psi_0}=\ket{\Psi_0}\).
- (3-2), PDF 110, sec3_1.tex:95--99:
  \(\ket{\Psi_0}\in D\).
- (3-3), PDF 110, sec3_1.tex:103--110:
  \(U(a,A)D\subset D,\quad \varphi_j(f)D\subset D,\quad
  \varphi_j(f)^\dagger D\subset D\).
- (3-4), PDF 111, sec3_1.tex:150--156:
  \(U(a,A)\varphi_j(f)U(a,A)^{-1}
  =\sum_k S_{jk}(A^{-1})\varphi_k(\{a,A\}f)\).
- (3-5), PDF 111, sec3_1.tex:158--163:
  \(\{a,A\}f(x)=f\bigl(A^{-1}(x-a)\bigr)\).
- (3-6), PDF 112, sec3_1.tex:232--238:
  \([\varphi_j(f),\varphi_k(g)]_{\pm}\equiv
  \varphi_j(f)\varphi_k(g)\pm\varphi_k(g)\varphi_j(f)=0\).
- (3-7), PDF 112, sec3_1.tex:288--294:
  \([\varphi_j(\mathbf{x},t),\pi_k(\mathbf{y},t)]
  =\ii\,\delta(\mathbf{x}-\mathbf{y})\delta_{jk}\).
- (3-8), PDF 113, sec3_1.tex:320--326:
  \(\bra{\Phi}B\varphi_j(f)\ket{\Psi}
  =\bra{\varphi_j(f)^\dagger\Phi}B\ket{\Psi}\).

The spin-zero, vector, and Dirac transformation displays on PDF 111 are
source-unmarked examples and are therefore starred in the native file. The
adjoint locality displays and the asymptotic-completeness display are likewise
source-unmarked.

### Section 3-2, equations (3-9)--(3-18)

- (3-9), PDF 115, sec3_2.tex:20--25:
  \(\Hilbert=\bigoplus_{n=0}^{\infty}\Hilbert^{(n)}\).
- (3-10), PDF 115, sec3_2.tex:31--36:
  \(\{\Phi^{(0)},\Phi^{(1)},\Phi^{(2)},\ldots\}\).
- (3-11), PDF 115, sec3_2.tex:41--47:
  \(\braket{\Phi}{\Psi}=\sum_{n=0}^{\infty}
  \braket{\Phi^{(n)}}{\Psi^{(n)}}\).
- (3-12), PDF 115, sec3_2.tex:52--58:
  \(\braket{\Phi}{\Phi}=\sum_{n=0}^{\infty}
  \norm{\Phi^{(n)}}^2<\infty\).
- (3-13), PDF 115, sec3_2.tex:67--80:
  \[
  \braket{\Phi^{(n)}}{\Psi^{(n)}}=
  \int\!\cdots\!\int\dd\Omega_m(p_1)\cdots\dd\Omega_m(p_n)
  \sum_{\alpha_1\ldots\alpha_n,\beta_1\ldots\beta_n}
  \Phi^{(n)*}(p_1\alpha_1,\ldots,p_n\alpha_n)
  \prod_{j=1}^{n}
  \mathcal{D}^{(s,0)}\!\left(\frac{\widetilde p_j}{m}\right)_{\alpha_j\beta_j}
  \Psi^{(n)}(p_1\beta_1,\ldots,p_n\beta_n).
  \]
- (3-14), PDF 115, sec3_2.tex:85--98:
  \[
  \begin{aligned}
  \varphi_\alpha(f)\Psi^{(n)}(p_1\alpha_1,\ldots,p_n\alpha_n)
  ={}&\sqrt{\pi}\Biggl\{\sqrt{n+1}\int\!\dd\Omega_m(p)\,f(p)
  \Psi^{(n+1)}(p\alpha,p_1\alpha_1,\ldots,p_n\alpha_n)\\
  &+\frac{1}{\sqrt n}\sum_{j=1}^{n}(-1)^{2s(j+1)}
  \widetilde f(-p_j)\mathcal{D}^{(s,0)}(\zeta)_{\alpha\alpha_j}
  \Psi^{(n-1)}(p_1\alpha_1,\ldots,
  \widehat p_j\widehat\alpha_j,\ldots,p_n\alpha_n)\Biggr\}.
  \end{aligned}
  \]
- (3-15), PDF 116, sec3_2.tex:103--109:
  \(\widetilde f(p)=\frac{1}{(2\pi)^2}\int
  \ee^{+\ii p\cdot x}f(x)\,\dd x\).
- (3-16), PDF 116, sec3_2.tex:113--124:
  \[
  \begin{aligned}
  \bigl(U(a,A)\Psi\bigr)^{(n)}(p_1\alpha_1,\ldots,p_n\alpha_n)
  ={}&\exp\!\left[-\ii\left(\sum_{j=1}^{n}p_j\right)\!\cdot a\right]
  \sum_{(\beta)}
  \prod_{j=1}^{n}\mathcal{D}^{(s,0)}(A)_{\alpha_j\beta_j}\\
  &\quad\times\Psi^{(n)}(A^{-1}p_1\beta_1,\ldots,
  A^{-1}p_n\beta_n).
  \end{aligned}
  \]
- (3-17), PDF 116, sec3_2.tex:141--160:
  \[
  \begin{aligned}
  :\!D^\alpha\varphi(x)D^\beta\varphi(x)\!:
  ={}&\lim_{x_1,x_2\to x}\Bigl[
  D^\alpha\varphi(x_1)D^\beta\varphi(x_2)
  -\bra{\Psi_0}D^\alpha\varphi(x_1)D^\beta\varphi(x_2)\ket{\Psi_0}\Bigr]\\
  &\text{and}\\
  :\!D^\alpha\varphi(x)D^\beta\varphi(x)D^\gamma\varphi(x)\!:
  ={}&\lim_{x_1,x_2,x_3\to x}\Bigl[
  D^\alpha\varphi(x_1)D^\beta\varphi(x_2)D^\gamma\varphi(x_3)\\
  &\quad-\bra{\Psi_0}D^\alpha\varphi(x_1)D^\beta\varphi(x_2)\ket{\Psi_0}
  D^\gamma\varphi(x_3)\\
  &\quad-\bra{\Psi_0}D^\alpha\varphi(x_1)D^\gamma\varphi(x_3)\ket{\Psi_0}
  D^\beta\varphi(x_2)\\
  &\quad-\bra{\Psi_0}D^\beta\varphi(x_2)D^\gamma\varphi(x_3)\ket{\Psi_0}
  D^\alpha\varphi(x_1)\Bigr].
  \end{aligned}
  \]
- (3-18), PDF 116, sec3_2.tex:172--178:
  \(\psi(x)=\varphi(x)+:
  \frac{\partial}{\partial x_\mu}\varphi(x)
  \frac{\partial}{\partial x^\mu}\varphi(x):\).

### Section 3-3, equations (3-19)--(3-41)

- (3-19), PDF 118, sec3_3.tex:25--31:
  \(\bra{\Omega}\varphi_1(x_1)\varphi_2(x_2)\cdots
  \varphi_n(x_n)\ket{\Omega}\).
- (3-20), PDF 118, sec3_3.tex:43--49:
  \(\bra{\Omega}\varphi_1(f_1)\varphi_2(f_2)\cdots
  \varphi_n(f_n)\ket{\Omega}\).
- (3-21), PDF 118, sec3_3.tex:60--67:
  \(\mathcal{W}(x_1,x_2,\ldots,x_n)
  =\bra{\Omega}\varphi_1(x_1)\varphi_2(x_2)\cdots
  \varphi_n(x_n)\ket{\Omega}\).
- (3-22), PDF 118, sec3_3.tex:72--78:
  \(\mathcal{W}_\pi(x_1,x_2,\ldots,x_n)
  =\bra{\Omega}\varphi_{i_1}(x_{i_1})\varphi_{i_2}(x_{i_2})\cdots
  \varphi_{i_n}(x_{i_n})\ket{\Omega}\).
- (3-23), PDF 118, sec3_3.tex:90--95:
  \(\ket{\Psi}=\int\dd^4x_1\cdots\dd^4x_k\,
  f(x_1,\ldots,x_k)\varphi_1(x_1)\cdots\varphi_k(x_k)\ket{\Omega}\).
- (3-24), PDF 119, sec3_3.tex:108--113:
  \(\ket{\Psi_J}=\sum_{j=1}^{J}
  \varphi_1(f_1^j)\varphi_2(f_2^j)\cdots\varphi_k(f_k^j)\ket{\Omega}\).
- (3-25), PDF 119, sec3_3.tex:183--191:
  \(U(a,A)\varphi_\alpha(x)U(a,A)^{-1}
  =\sum_{\alpha'}S^{(\varphi)}_{\alpha\alpha'}(A^{-1})
  \varphi_{\alpha'}(Ax+a)\).
- (3-26), PDF 119, sec3_3.tex:197--210:
  \[
  \begin{aligned}
  &\sum_{\alpha',\beta',\ldots,\gamma'}
  S^{(\varphi)}_{\alpha\alpha'}(A)S^{(\psi)}_{\beta\beta'}(A)\cdots
  S^{(\chi)}_{\gamma\gamma'}(A)
  \bra{\Omega}\varphi_{\alpha'}(x_1)\psi_{\beta'}(x_2)\cdots
  \chi_{\gamma'}(x_n)\ket{\Omega}\\
  &\qquad=\bra{\Omega}\varphi_\alpha(Ax_1+a)\psi_\beta(Ax_2+a)\cdots
  \chi_\gamma(Ax_n+a)\ket{\Omega}.
  \end{aligned}
  \]
- (3-27), PDF 120, sec3_3.tex:230--235:
  \(\xi_j=x_j-x_{j+1},\qquad j=1,2,\ldots,n-1\).
- (3-28), PDF 120, sec3_3.tex:239--244:
  \(\mathcal{W}(x_1,\ldots,x_n)=W(\xi_1,\xi_2,\ldots,\xi_{n-1})\).
- (3-29), PDF 120, sec3_3.tex:249--256:
  \(\widetilde{\mathcal{W}}(p_1,p_2,\ldots,p_n)
  =\int\exp\!\left(-\ii\sum_{j=1}^{n}p_j\cdot x_j\right)
  \mathcal{W}(x_1,\ldots,x_n)\,\dd^4x_1\cdots\dd^4x_n\).
- (3-30), PDF 120, sec3_3.tex:257--264:
  \(\widetilde{W}(q_1,\ldots,q_{n-1})
  =\int\exp\!\left(-\ii\sum_{j=1}^{n-1}q_j\cdot\xi_j\right)
  W(\xi_1,\xi_2,\ldots,\xi_{n-1})\,\dd^4\xi_1\cdots\dd^4\xi_{n-1}\).
- (3-31), PDF 120, sec3_3.tex:268--275:
  \(\widetilde{\mathcal{W}}(p_1,\ldots,p_n)
  =(2\pi)^4\delta^{(4)}\!\left(\sum_{j=1}^{n}p_j\right)
  \widetilde{W}(p_1,p_1+p_2,\ldots,p_1+p_2+\cdots+p_{n-1})\).
- (3-32), PDF 120, sec3_3.tex:279--283:
  \(\widetilde{W}(q_1,\ldots,q_{n-1})=0\).
- (3-33), PDF 120, sec3_3.tex:291--297:
  \(\bra{\Omega}\varphi_1(x_1)\varphi_2(x_2)\cdots\varphi_n(x_n)\ket{\Omega}
  =\overline{\bra{\Omega}\varphi_n^\dagger(x_n)\cdots
  \varphi_2^\dagger(x_2)\varphi_1^\dagger(x_1)\ket{\Omega}}\).
- (3-34), PDF 121, sec3_3.tex:302--310:
  \[
  \begin{aligned}
  \mathcal{W}(x_1,x_2,\ldots,x_{j+1},x_j,\ldots,x_n)
  &=(-1)^m\mathcal{W}(x_1,x_2,\ldots,x_j,x_{j+1},\ldots,x_n),\\
  &\qquad j=1,\ldots,n-1 .
  \end{aligned}
  \]
- (3-35), PDF 122, sec3_3.tex:408--418:
  \[
  \begin{aligned}
  \sum_{j,k=0}^{\infty}\int\cdots\int
  &\overline{f_j(x_1,\ldots,x_j)}\,
  \mathcal{W}_{jk}(x_j,x_{j-1},\ldots,x_1,y_1,\ldots,y_k)
  f_k(y_1,\ldots,y_k)\\
  &\qquad\times\dd^4x_1\cdots\dd^4x_j\,\dd^4y_1\cdots\dd^4y_k\geq0 .
  \end{aligned}
  \]
- (3-36), PDF 122, sec3_3.tex:438--446:
  \(g_0=0,\qquad g_1=g(x_1)f_0,\qquad
  g_2=g(x_1)f_1(x_2),\qquad
  g_3=g(x_1)f_2(x_2,x_3)\cdots\).
- (3-37), PDF 123, sec3_3.tex:485--494:
  \[
  \begin{aligned}
  &\mathcal{W}(x_1,\ldots,x_j,x_{j+1}+\lambda a,x_{j+2}+\lambda a,\ldots,
  x_n+\lambda a)\\
  &\longrightarrow
  \mathcal{W}(x_1,\ldots,x_j)\mathcal{W}(x_{j+1},\ldots,x_n)
  \end{aligned}
  \]
  as \(\lambda\to\infty\) in \(\Schwartz'\), for space-like \(a\).
- (3-38), PDF 125, sec3_3.tex:697--705:
  \(\bra{\Omega}\varphi_{(\alpha)(\beta)}(x_1)\cdots
  \psi_{(\mu)(\nu)}(x_n)\ket{\Omega}
  =\bra{\Omega}\varphi^*_{(\dot\alpha)(\dot\beta)}(x_1)\cdots
  \psi^*_{(\dot\mu)(\dot\nu)}(x_n)\ket{\Omega}\).
- (3-39), PDF 125, sec3_3.tex:712--723:
  \[
  \begin{aligned}
  \bra{\Omega}\varphi_{(\alpha)(\beta)}(x_1)\cdots
  \psi_{(\mu)(\nu)}(x_n)\ket{\Omega}
  & =\ii^F(-1)^J\\
  &\quad\times\overline{\bra{\Omega}\varphi^*_{(\alpha)(\beta)}(-x_1)\cdots
  \psi^*_{(\mu)(\nu)}(-x_n)\ket{\Omega}} .
  \end{aligned}
  \]
- (3-40), PDF 127, sec3_3.tex:837--842:
  \(W(\xi_1,\ldots,\xi_{n-1})
  =(-1)^J W(-\xi_1,-\xi_2,\ldots,-\xi_{n-1})\).
- (3-41), PDF 128, sec3_3.tex:944--961:
  \[
  \begin{aligned}
  &\bra{\Omega}\varphi(x_1)\varphi(x_2)\cdots\varphi(x_n)\ket{\Omega}\\
  &\quad=
  \begin{cases}
  \displaystyle\sum_{\mathrm{partitions}}
  \frac{1}{\ii}\Delta^+(x_{i_1}-x_{i_2})
  \frac{1}{\ii}\Delta^+(x_{i_3}-x_{i_4})\cdots
  \frac{1}{\ii}\Delta^+(x_{i_{n-1}}-x_{i_n}),
  &n\ \mathrm{even},\\
  0,&n\ \mathrm{odd}.
  \end{cases}
  \end{aligned}
  \]
  The following prose defines the sum over disjoint two-element partitions
  with \(i_{2k-1}<i_{2k}\), then continues across PDF 129.

### Section 3-4, equations (3-42)--(3-57)

- (3-42), PDF 129, sec3_4.tex:49--55:
  \(\mathcal{W}^{(n)}(x_1,\ldots,x_n)
  =\mathcal{W}^{(n)}(\Lambda x_1+a,\Lambda x_2+a,\ldots,\Lambda x_n+a),
  \quad\Lambda\in L_+^\uparrow\).
- (3-43), PDF 129, sec3_4.tex:60--67:
  \(\widetilde{\mathcal{W}}^{(n)}(p_1,\ldots,p_n)
  =(2\pi)^4\delta\!\left(\sum_{j=1}^{n}p_j\right)
  \widetilde{\mathcal{W}}(p_1,p_1+p_2,\ldots,p_1+p_2+\cdots+p_{n-1})\).
- (3-44), PDF 129, sec3_4.tex:70--75:
  \(\widetilde{\mathcal{W}}^{(n)}(q_1,\ldots,q_{n-1})=0
  \quad\text{if any }q_i\notin V_+\).
- (3-45), PDF 130, sec3_4.tex:80--85:
  \(\mathcal{W}^{(n)}(x_1,\ldots,x_n)
  =\overline{\mathcal{W}^{(n)}(x_n,\ldots,x_1)}\).
- (3-46), PDF 130, sec3_4.tex:90--99:
  \[
  \begin{aligned}
  \mathcal{W}^{(n)}(x_1,\ldots,x_j,x_{j+1},\ldots,x_n)
  &=\mathcal{W}^{(n)}(x_1,\ldots,x_{j+1},x_j,\ldots,x_n)\\
  &\hspace{2em}\text{if }(x_j-x_{j+1})^2<0,
  \quad j=1,2,\ldots,n-1 .
  \end{aligned}
  \]
- (3-47), PDF 130, sec3_4.tex:104--114:
  \[
  \begin{aligned}
  \sum\!\int\!\cdots\!\int
  &\dd x_1\cdots\dd x_j\,\dd y_1\cdots\dd y_k\,
  \overline{f_j(x_1,\ldots,x_j)}\\
  &\times\mathcal{W}^{(j+k)}(x_j,\ldots,x_1,y_1,\ldots,y_k)
  f_k(y_1,\ldots,y_k)\geq0 .
  \end{aligned}
  \]
- (3-48), PDF 131, sec3_4.tex:187--199:
  \[
  \begin{aligned}
  \braket{f}{g}
  &=\sum_{j,k=0}^{\infty}\int\!\cdots\!\int
  \dd x_1\cdots\dd x_j\,\dd y_1\cdots\dd y_k\,
  \overline{f_j(x_1,\ldots,x_j)}\\
  &\qquad\times\mathcal{W}^{(j+k)}(x_j,\ldots,x_1,y_1,\ldots,y_k)
  f_k(y_1,\ldots,y_k).
  \end{aligned}
  \]
- (3-49), PDF 131, sec3_4.tex:216--225:
  \[
  \begin{aligned}
  U(a,\Lambda)(f_0,f_1,f_2,\ldots)
  &=(f_0,\{a,\Lambda\}f_1,\{a,\Lambda\}f_2,\ldots),\\
  \{a,\Lambda\}f_k(x_1,\ldots,x_k)
  &=f_k\bigl(\Lambda^{-1}(x_1-a),\ldots,
  \Lambda^{-1}(x_k-a)\bigr).
  \end{aligned}
  \]
- (3-50), PDF 131, sec3_4.tex:252--257:
  \(\varphi(h)\{f_0,f_1,f_2,\ldots\}
  =(0,hf_0,h\otimes f_1,h\otimes f_2,\ldots)\).
- (3-51), PDF 131, sec3_4.tex:268--273:
  \(U(a,\Lambda)\varphi(h)U(a,\Lambda)^{-1}
  =\varphi(\{a,\Lambda\}h)\).
- (3-52), PDF 132, sec3_4.tex:295--299:
  \(\braket{\varphi(\overline h)f}{g}
  =\braket{f}{\varphi(h)g}\).
- (3-53), PDF 132, sec3_4.tex:320--324:
  \(\abs{\braket{f}{g}}\leq \lVert f\rVert\,\lVert g\rVert=0\).
- (3-54), PDF 133, sec3_4.tex:410--414:
  \(\braket{F}{G}=\lim_{n\to\infty}\braket{f_n}{g_n}\).
- (3-55), PDF 135, sec3_4.tex:580--585:
  \(\left\lVert\ket{\Psi_f}-U(a,\Lambda)\ket{\Psi_f}\right\rVert
  =\lVert f-U(a,\Lambda)f\rVert\).
- (3-56), PDF 137, sec3_4.tex:715--719:
  \((0,hg_0,h\otimes g_1,h\otimes g_2,\ldots)\).
- (3-57), PDF 137, sec3_4.tex:784--793:
  \[
  \begin{aligned}
  V\ket{\Psi_f}=\ket{\Psi_{1f}}
  &=f_0\ket{\Psi_{01}}+\varphi_1(f_1)\ket{\Psi_{01}}\\
  &\quad+\int\varphi_1(x_1)\varphi_1(x_2)f_2(x_1,x_2)
  \,\dd x_1\,\dd x_2\,\ket{\Psi_{01}}+\cdots .
  \end{aligned}
  \]

### Section 3-5, equations (3-58)--(3-67)

- (3-58), PDF 139, sec3_5.tex:32--37:
  \(U(I_s)\varphi(x)U(I_s)^{-1}
  =\varphi(x^0,-\mathbf{x})\equiv\varphi(I_sx)\).
- (3-59), PDF 139, sec3_5.tex:42--47:
  \(U(I_s)U(a,\Lambda)U(I_s)^{-1}
  =U(I_sa,I_s^{-1}\Lambda I_s)\).
- (3-60), PDF 139, sec3_5.tex:75--81:
  \(U(I_s)U(a,\Lambda)U(I_s)^{-1}U(I_sa,I_s^{-1}\Lambda I_s)^{-1}
  =\omega\mathbf{1},\quad |\omega|=1\).
- (3-61), PDF 139, sec3_5.tex:84--90:
  \(U(I_sa,I_s^{-1}\Lambda I_s)U(I_s)\ket{\Psi_0}
  =\omega^{-1}U(I_s)\ket{\Psi_0}\).
- (3-62), PDF 140, sec3_5.tex:127--132:
  \(U(I_t)U(a,\Lambda)U(I_t)^{-1}
  =U(I_ta,I_t^{-1}\Lambda I_t)\).
- (3-63), PDF 140, sec3_5.tex:134--138:
  \(U(C)U(a,\Lambda)U(C)^{-1}=U(a,\Lambda)\).
- (3-64), PDF 140, sec3_5.tex:150--156:
  \(U(I_s)\ket{\Psi_0}=\ket{\Psi_0},\quad
  U(I_t)\ket{\Psi_0}=\ket{\Psi_0},\quad
  U(C)\ket{\Psi_0}=\ket{\Psi_0}\).
- (3-65), PDF 141, sec3_5.tex:242--247:
  \(V\psi_j(x)V^{-1}=\lambda_j\psi_j(x)\).
- (3-66), PDF 143, sec3_5.tex:338--348:
  \[
  \begin{aligned}
  &\bra{\Psi_0}\varphi_{(\alpha)(\dot\beta)}(x_1)\cdots
  \psi_{(\mu)(\dot\nu)}(x_n)\ket{\Psi_0}\\
  &\quad={ }\ii^F(-1)^J
  \overline{\bra{\Psi_0}\varphi^*_{(\alpha)(\dot\beta)}(-x_1)\cdots
  \psi^*_{(\mu)(\dot\nu)}(-x_n)\ket{\Psi_0}} .
  \end{aligned}
  \]
- (3-67), PDF 143, sec3_5.tex:354--360:
  \(\Theta^{-1}\varphi_{(\alpha)(\dot\beta)}(f)\Theta
  =(-1)^j\ii^{F(\varphi)}
  \varphi^*_{(\alpha)(\dot\beta)}(\widehat{\overline f})\).

The sequence check is exact: tags (3-1) through (3-67) occur once each, in
source order. There are 67 non-starred equation or align environments and 67
tags. The 95 source-unmarked display environments in the five section files
are starred. This includes the four previously unstarred displays in
sec3_4.tex: the cluster-decomposition hypothesis and the three unnumbered
vacuum-value or equivalence displays following (3-47). No unnumbered display
consumes the equation counter.

## Numbered results and proof inventory

There are nine theorem environments, in source order Theorems 3-1 through
3-9. There are no lemmas and no corollaries in Chapter 3.

- Theorem 3-1, PDF 119, sec3_3.tex:176--211. For fields transforming in
  irreducible representations, the vacuum expectation values are tempered
  distributions and obey the relativistic transformation law (3-25)--(3-26).
  Proof: sec3_3.tex:212--217, ending with the deduction of (3-26) from
  (3-25) and vacuum invariance.
- Theorem 3-2, PDF 120--121, sec3_3.tex:220--315. With
  \(\mathcal W\) as in (3-21), the theorem gives translation dependence on
  relative coordinates and the spectral support statement (3-27)--(3-32),
  the hermiticity condition (3-33), and the local-commutativity condition
  (3-34), with the sign exponent \(m\) selected by commutation or
  anticommutation. Proof: sec3_3.tex:317--394, ending after the local
  commutativity argument.
- Theorem 3-3, PDF 122, sec3_3.tex:401--451. For a finite-support sequence of
  test functions \(f_j\in\Schwartz(\R^{4j})\), the positive-definiteness
  inequality (3-35) holds. Equality for a sequence \(f_j\) also gives zero
  for the shifted sequence \(g_0,g_1,g_2,g_3,\ldots\) in (3-36), for every
  test function \(g\). Proof: sec3_3.tex:452--469, ending with the vanishing
  of (3-35) for (3-36).
- Theorem 3-4, PDF 123, sec3_3.tex:480--510. For a space-like vector \(a\),
  the cluster limit (3-37) holds in \(\Schwartz'\). Proof:
  sec3_3.tex:511--676, ending with the spectral cutoff argument that yields
  (3-37).
- Theorem 3-5, PDF 126--127, sec3_3.tex:737--768. The distributions
  \(\mathcal W\) and \(W\) are boundary values of holomorphic functions in
  the tube, with the stated boundary limit, polynomial bound, and
  single-valued continuation to the extended tube. Proof:
  sec3_3.tex:769--827. The formal environment closes before the statement of
  Theorem 3-6.
- Theorem 3-6, PDF 127--128, sec3_3.tex:854--878. Given the permutation
  \(\pi:(1,\ldots,n)\mapsto(i_1,\ldots,i_n)\), the holomorphic functions
  \(W\) and \(W_\pi\) from Theorem 3-5 continue one another as one
  holomorphic function. Proof: sec3_3.tex:879--900, ending after the edge of
  the wedge argument.
- Theorem 3-7, PDF 129--138, sec3_4.tex:27--826. A sequence
  \(\{\mathcal W^{(n)}\}\) of tempered distributions satisfying cluster
  decomposition and properties (a)--(e), specialized to a hermitian scalar
  field, gives a separable Hilbert space, a continuous unitary
  \(\mathcal P_+^\uparrow\) representation, a unique invariant vacuum, and a
  hermitian scalar field on \(D_1\) with those vacuum expectation values.
  Every other cyclic realization with the same values is unitarily
  equivalent. The complete hypotheses are (3-42)--(3-47), and the
  construction uses the unnumbered vacuum-value display and equivalence map
  immediately following (3-47). Proof: sec3_4.tex:158--828, with the source
  continuation on PDF 138 closing the unitary-equivalence construction.
- Theorem 3-8, PDF 139, sec3_5.tex:21--51. For a hermitian scalar field,
  \(U(I_s)D=D\) and
  \(U(I_s)\varphi(x)U(I_s)^{-1}=\varphi(I_sx)\) determine \(U(I_s)\) up to
  phase, give \(U(I_s)\ket{\Psi_0}=e^{\ii\alpha}\ket{\Psi_0}\), and imply
  the group relation (3-59). Proof: sec3_5.tex:52--118, ending after the
  dense-domain extension.
- Theorem 3-9, PDF 143--144, sec3_5.tex:330--379. If the PCT identity (3-39)
  holds for all field vacuum expectation values, then a unique up to a
  factor anti-unitary \(\Theta\) exists and satisfies (3-67), with
  \(\widehat{\overline f}(x)=\overline f(-x)\), undotted index count \(j\),
  dotted index count \(k\), and \(F^{(\varphi)}=0\) for even \(j+k\) and 1
  for odd \(j+k\). Proof: sec3_5.tex:380--419, ending after the continuous
  extension to \(\Hilbert\).

The theorem list above preserves the source order of every theorem statement
and its proof. The formal proof count is 9 starts and 9 ends. Each proof has
one terminal QED square in the rendered PDF. The bounded-operator cyclicity
argument on PDF 114 is a source prose proof in parentheses, ending with
“Therefore \(\ket{\Psi}\) is cyclic.” It is not a formal proof environment and
does not affect the theorem counter.

### Formal proof-ending ledger

1. Proof of Theorem 3-1, PDF 120, sec3_3.tex:211--217: “(3-26) follows
   immediately.”
2. Proof of Theorem 3-2, PDF 121--122, sec3_3.tex:317--394: “This relation
   follows immediately from axiom III, again with the use of the extension
   from product test functions to all test functions of
   \(\Schwartz(\R^{4n})\).”
3. Proof of Theorem 3-3, PDF 122, sec3_3.tex:451--469: “Hence the expression
   (3-35) must give 0 also for the sequence (3-36).”
4. Proof of Theorem 3-4, PDF 123--125, sec3_3.tex:510--676: “so the required
   result (3-37) follows.”
5. Proof of Theorem 3-5, PDF 126--127, sec3_3.tex:769--827: “Thus
   \(W(\xi_1,\ldots,\xi_{n-1})\) is continuable into
   \(\ExtendedTube_{n-1}\).”
6. Proof of Theorem 3-6, PDF 127--128, sec3_3.tex:879--900: “Hence, by the
   edge of the wedge theorem \(W\) is holomorphic at such a point.”
7. Proof of Theorem 3-7, PDF 130--138, sec3_4.tex:158--828: “Finally, a
   simple direct calculation shows that
   \(U_1(a,\Lambda)=VU(a,\Lambda)V^{-1}\).”
8. Proof of Theorem 3-8, PDF 139, sec3_5.tex:52--118: “Thus the operator
   \(U(I_s)\) can be extended uniquely by linearity and continuity to the
   whole of \(\Hilbert\), and, so extended, continues to satisfy (3-59).”
9. Proof of Theorem 3-9, PDF 143--144, sec3_5.tex:380--419: “The extension
   to all of \(\Hilbert\) is done by continuity, and, so defined, is
   anti-unitary.”

### Unnumbered results and examples

- PDF 111: the three examples “(a) Spin Zero Field”, “(b) Vector Field”, and
  “(c) Dirac Field \(\psi\)”. Their transformation displays are unnumbered.
- PDF 113: the unnumbered “Definition” of a field theory, namely cyclicity
  of the vacuum under polynomials in the smeared field components. The
  definition is prose and has no theorem counter.
- PDF 123: the unnumbered Remark after Theorem 3-4. It states the mass-gap
  hypothesis used in the proof, the massless-particle qualification, the
  possibility of proving (3-37) without axiom III, and references 5, 7, 9,
  10, and 11.
- PDF 129: the unnumbered cluster-decomposition hypothesis inside Theorem
  3-7. It is an equation* display and has no equation number.
- PDF 130: the unnumbered vacuum expectation and unitary-equivalence displays
  inside Theorem 3-7. They are equation* displays and have no equation
  number.

## Footnote inventory

There are exactly nine footnotes in the Chapter 3 section files, in source
order. The two dagger notes in Section 3-1 use the source dagger marker. The
remaining notes use the chapter's numeric footnote sequence.

1. PDF 110, sec3_1.tex:90: “Defined in Section 2-6.” Dagger marker.
2. PDF 113, sec3_1.tex:315: “This idea was introduced in Ref. 5.” Dagger
   marker.
3. PDF 119, sec3_3.tex:208: “See Section 2-6.”
4. PDF 122, sec3_3.tex:432--434: “It is shown on p. 121 that this follows
   from (3-35) and the other axioms.”
5. PDF 126, sec3_3.tex:763: “Defined in Section 2-3.”
6. PDF 127, sec3_3.tex:881--884: “Then we say that
   \((x_1,\ldots,x_n)\) is a totally space-like point.”
7. PDF 130, sec3_4.tex:120: “Defined in Section 2-6.”
8. PDF 130, sec3_4.tex:160--163: “In this proof \(h\) will denote a test
   function in \(\mathcal S(\R^4)\) and \(f\) and \(g\) will denote elements
   of \(H\), defined below.”
9. PDF 132, sec3_4.tex:307: “Defined in Section 2-6.”

No footnote occurs in sec3_2.tex, sec3_5.tex, or bibliography.tex.

## Bibliography inventory

bibliography.tex contains one native thebibliography environment and 17
bibitem entries. Visible numbering is [1]--[17] in source order. The
intervening source prose is represented by empty-label items, so it does not
consume or alter the visible reference counter.

1. A. S. Wightman, “Les Problèmes mathématiques de la théorie quantique des
   champs,” pp. 11--19, Centre National de la Recherche Scientifique, Paris,
   1959; and also.
2. A. S. Wightman and L. Gårding, “Fields as Operator-Valued Distributions in
   Quantum Field Theory,” Ark. Fys., 28, 129 (1964).
3. R. Haag and B. Schroer, “The Postulates of Quantum Field Theory,” J. Math.
   Phys., 3, 248 (1962).
4. O. W. Greenberg, “Generalized Free Fields and Models of Local Field
   Theory,” Ann. Phys., 16, 158 (1961).
5. D. Ruelle, “On the Asymptotic Condition in Quantum Field Theory,” Helv.
   Phys. Acta, 35, 34 (1962).
6. A. S. Wightman, “Quantum Field Theory in Terms of Vacuum Expectation
   Values,” Phys. Rev., 101, 860 (1956).
7. K. Hepp, R. Jost, D. Ruelle, and O. Steinmann, “Necessary Condition on
   Wightman Functions,” Helv. Phys. Acta, 34, 542 (1961).
8. H. J. Borchers, “On the Structure of the Algebra of Field Observables,”
   Nuovo Cimento, 24, 214 (1962).
9. H. Araki, “On the Asymptotic Behavior of Vacuum Expectation Values at Large
   Spacelike Separations,” Ann. Phys., 11, 260 (1960).
10. R. Jost and K. Hepp, “Über die Matrixelemente des Translations Operators,”
    Helv. Phys. Acta, 35, 34 (1962).
11. H. Araki, K. Hepp, and D. Ruelle, “On the Asymptotic Behavior of Wightman
    Functions in Space-like Directions,” Helv. Phys. Acta, 35, 164 (1962).
12. A. O. G. Källén, “Properties of Vacuum Expectation Values of Field
    Operators,” pp. 389--447 in Dispersion Relations and Elementary
    Particles, Wiley, New York, 1960.
13. A. S. Wightman, “Quantum Field Theory and Analytic Functions of Several
    Complex Variables,” Proc. Indian Math. Soc., 24, 625 (1960).
14. W. Schmidt and K. Baumann, “Quantentheorie der Felder als
    Distributionstheorie,” Nuovo Cimento, 4, 860 (1956).
15. A. S. Wightman, “Recent Achievements of Axiomatic Field Theory,”
    Proceedings of the Summer Seminar of IAEA, Trieste, 1962, published as a
    book, Theoretical Physics, IAEA, Vienna, 1963.
16. K. Symanzik, “Green's Functions and the Quantum Theory of Fields,”
    Lectures in Theoretical Physics III, Boulder, 1960, pp. 490--531,
    Interscience, New York, 1961.
17. G. Feinberg and S. Weinberg, “On the Phase Factors in Inversions,” Nuovo
    Cimento, 14, 571 (1959).

Source page placement is preserved: references [1]--[7] begin on PDF 144, and
references [8]--[17] continue on PDF 145. The generated PDF renders [1]--[17]
with the same visible labels and content.

## Corrections applied in this audit

The source comparison established three related defects in the existing
Chapter 3 packet.

1. The top of PDF 129 continued the final sentence of the linear-program
   paragraph from PDF 128. That complete continuation was added at the start
   of sec3_4.tex before the Section 3-4 marker.
2. The source-unmarked cluster-decomposition display inside Theorem 3-7 had
   a source marker that looked like equation (3-41). Its marker is now
   p117-cluster-decomposition, and its environment is equation*.
3. The three other source-unmarked displays inside Theorem 3-7 were changed
   from numbered equation environments to equation*. Their source
   statements remain complete and their counter effect is zero.

These changes are confined to sec3_4.tex. No source-proven correction was
found in sec3_1.tex, sec3_2.tex, sec3_3.tex, sec3_5.tex, or bibliography.tex.

## Verification

- python3 scripts/audit_source.py --strict: passed. Native chunks present:
  36/36. All marked source pages remain within the canonical source.
- Equation parser: 67 tags, 67 unique identifiers, exact sequence
  3-1 through 3-67.
- Result parser: 9 theorem environments, 9 formal proofs, 9 proof endings;
  zero lemmas and zero corollaries.
- Footnote parser: 9 footnotes, matching the source-page inventory above.
- Bibliography parser: one thebibliography environment, 17 bibitem entries,
  no duplicate labels.
- Historical packet full build:
  latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex
  exited 0 and produced the packet's latex/master.pdf with 185 pages.
- Historical packet rendered artifact SHA-256: debb5e1f436ba42fd2b9a674ff500da61a9b12e71e85e7a48fb44af9a3cc9e55
- latex/master.log contains no Warning, Overfull, Underfull, undefined, or
  multiply defined diagnostics.
- Render inspection covered the PDF 128--129 continuation and Section 3-4
  boundary, the reconstruction-proof ending and Section 3-5 opening, the
  Section 3-5 theorem sequence through (3-67), and the bibliography pages.
  The continuation is visible before the Section 3-4 heading, unnumbered
  displays carry no accidental equation labels, proof endings have terminal
  black squares, and references [1]--[17] are visible in order.

Current final-candidate evidence:

The current `latex/master.pdf` is an A4, 180-page PDF with SHA-256
`4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`. The
current render and page-inspection manifests each have 180 records, and
validation passed for 180/180 visually inspected pages.

Unresolved blockers: none
