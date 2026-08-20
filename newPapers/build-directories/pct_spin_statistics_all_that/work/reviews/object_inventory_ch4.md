# Chapter 4 object inventory audit

## Research audit record

PASS: Global numbering and object-inventory audit
INPUT SNAPSHOT: Canonical source origPapers/pct_spin_statistics_all_that.pdf, SHA-256 44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889; source JPEGs work/source-pages/pdf-146.jpg through pdf-190.jpg; native files latex/chapters/chapter04/opening.tex, sec4_1.tex through sec4_6.tex, and bibliography.tex.
FULL SCOPE READ: PDF physical pages 146-190, printed pages 134-178, all 45 page images inspected in source order. Every Chapter 4 TeX unit, displayed formula, named result, proof transition, footnote, and bibliography block was compared against the source. No Chapter 4 figures or tables occur in the source or native files.
FINDINGS: Numbering is complete and source ordered. Eq. (4-69) retains its stacked spin factor. The PDF 173 continuation of Example 3 precedes Section 4-5. The source PDF 180 reading of Eq. (4-89) is (Box_src + m^2) phi = lambda phi^3; the native mostly-plus form is (-Box + m^2) phi = lambda phi^3. The early Section 4-1 spacelike inequalities were converted from the source mostly-minus negative sector to the house mostly-plus positive sector.
EDITS MADE: sec4_1.tex spacelike inequalities and associated prose converted to the house metric; sec4_4.tex footnote marker fn-p156-parity added; sec4_5.tex Eq. (4-89) and related free-field/inhomogeneous mass operators use the notation ledger house-metric forms; sec4_1.tex footnote marker fn-p137-section-2-1 added.
CHECKS RUN: Parsed all numbered tag displays, checked uniqueness and source order, checked result/object markers, compared all 45 source JPEGs, checked bibliography labels and source order. The standalone Chapter 4 harness was compiled twice with pdflatex and produced a 39-page PDF without TeX errors. Rendered pages 24, 25, and 31 were inspected at 180 dpi for Eq. (4-69), the Example 3 to Section 4-5 boundary, Eq. (4-70), Eq. (4-89), and the Section 4-6 opening. The harness log contains five pre-existing overfull-box warnings in other paragraphs; none affects the inspected displays or source-order boundary.
UNRESOLVED: none within the Chapter 4 audit scope
STATUS: PASS

## Global inventory

- Numbered equations: 101 total, one each for (4-1) through (4-101), source order preserved. The requested late boundary is covered by (4-1) through (4-89), with (4-90) through (4-101) continuing Section 4-6.
- Theorems: 22 total, Theorem 4-1 through Theorem 4-22, each once and source ordered.
- Lemmas, propositions, definitions, claims, observations: none in the source range.
- Corollaries: 3 unnumbered objects.
- Examples: 3 objects.
- Remarks: 6 distinct objects. The continuation marker attached to Section 4-1 Remark 1 is not a seventh remark.
- Footnotes: 7.
- Proof blocks: 20 theorem proofs. Theorem 4-7 and Theorem 4-22 have no separate source proof block. Nineteen source proof endings have an explicit square; Theorem 4-14 ends in prose before its corollary.
- Bibliography: 30 entries, consisting of numeric items 1-29 and item 19a.

## Numbered-equation inventory

Each formula below is the complete native display after the authorized Dirac, adjoint, and mostly-plus metric conversions. The source marker and semantic label are retained in the Chapter 4 TeX.
### (4-1)
Source: PDF 146 / printed 134; sec4_1.tex:28; label eq:ch4-local-commutativity.

```tex
[\varphi(x),\varphi(y)]_{-}=0
```

### (4-2)
Source: PDF 147 / printed 135; sec4_1.tex:75; label eq:ch4-f1-definition.

```tex
\begin{aligned} F_1(&x_1-x_2,x_2-x_3,\ldots,x_{j-1}-x_j,x_j-x,x-y,y-y_1,\\ &y_1-y_2,\ldots,y_{k-1}-y_k) \\ &=\bra{\Omega}\varphi(x_1)\cdots\varphi(x_j)\varphi(x)\varphi(y) \varphi(y_1)\cdots\varphi(y_k)\ket{\Omega} \end{aligned}
```

### (4-3)
Source: PDF 147 / printed 135; sec4_1.tex:92; label eq:ch4-f1-extended-tube-variables.

```tex
\begin{aligned} &x_1-x_2-i\eta_1,\ldots,x_{j-1}-x_j-i\eta_{j-1}, x_j-x-i\eta,x-y-i\eta',\\ &\qquad y-y_1-i\eta'',y_1-y_2-i\rho_1,\ldots, y_{k-1}-y_k-i\rho_{k-1} . \end{aligned}
```

### (4-4)
Source: PDF 147 / printed 135; sec4_1.tex:113; label eq:ch4-permuted-tube-transformation.

```tex
\begin{aligned} &x_1-x_2-i\eta_1,\ldots,x_{j-1}-x_j-i\eta_{j-1}, (x_j-x-i\eta)+(x-y-i\eta'),\\ &\qquad -(x-y-i\eta'), (x-y-i\eta')+(y-y_1-i\eta''),\\ &\qquad y_1-y_2-i\rho_1,\ldots,y_{k-1}-y_k-i\rho_{k-1} . \end{aligned}
```

### (4-5)
Source: PDF 148 / printed 136; sec4_1.tex:148; label eq:ch4-boundary-argument.

```tex
\begin{aligned} F_1(\zeta_1,\ldots,\zeta_{j+k+1}) ={}&F_2(\zeta_1,\ldots,\zeta_{j-2},\zeta_{j-1}+\zeta_j,-\zeta_j,\\ &\qquad\zeta_j+\zeta_{j+1},\ldots,\zeta_{j+k+1}) \end{aligned}
```

### (4-6)
Source: PDF 148 / printed 136; sec4_1.tex:172; label eq:ch4-scaling-path.

```tex
\begin{aligned} &\rho(x_1-x_2),\ldots,\rho(x_{j-1}-x_j),\rho(x_j-x),\rho(x-y), \rho(y-y_1),\\ &\qquad\rho(y_1-y_2),\ldots,\rho(y_{k-1}-y_k),\quad \rho>0, \end{aligned}
```

### (4-7)
Source: PDF 148 / printed 136; sec4_1.tex:212; label eq:ch4-tempered-distribution.

```tex
\begin{aligned} f_1(&x_1-x_2,\ldots,x_{j-1}-x_j,x_j,-y_1, y_1-y_2,\ldots,y_{k-1}-y_k) \\ &=\int h(x,y)\,\mathrm{d}x\,\mathrm{d}y\, \bra{\Omega}\varphi(x_1)\cdots\varphi(x_j)\varphi(x)\varphi(y) \varphi(y_1)\cdots\varphi(y_k)\ket{\Omega} \end{aligned}
```

### (4-8)
Source: PDF 149 / printed 137; sec4_1.tex:255; label eq:ch4-locality-domain.

```tex
\braket{\Phi}{[\varphi(x),\varphi(y)]_-\Psi}=0 \quad\text{for }(x-y)^2>0,\quad \ket{\Psi},\ket{\Phi}\in D_0,
```

### (4-9)
Source: PDF 150 / printed 138; sec4_2.tex:21; label eq:ch4-9.

```tex
c+\sum_{j=1}^{N} \varphi\bigl(f_1^{(j)}\bigr)\cdots \varphi\bigl(f_j^{(j)}\bigr),
```

### (4-10)
Source: PDF 150 / printed 138; sec4_2.tex:45; label eq:ch4-10.

```tex
\sum_{j=0}^{N} \varphi\bigl(f_1^{(j)}\bigr)\cdots \varphi\bigl(f_j^{(j)}\bigr)\ket{\Omega}
```

### (4-11)
Source: PDF 151 / printed 139; sec4_2.tex:133; label eq:ch4-11.

```tex
T\ket{\Omega}=0
```

### (4-12)
Source: PDF 151 / printed 139; sec4_2.tex:153; label eq:ch4-12.

```tex
\braket{\Psi}{T^\dagger\Phi} =\braket{T\Psi}{\Phi} =\braket{TP'\Omega}{\Phi} =\braket{P'T\Omega}{\Phi}=0.
```

### (4-13)
Source: PDF 152 / printed 140; sec4_2.tex:201; label eq:ch4-13.

```tex
\matrixel{\Phi}{C\varphi(f)}{\Psi} =\matrixel{\varphi(f)^\dagger\Phi}{C}{\Psi},
```

### (4-14)
Source: PDF 152 / printed 140; sec4_2.tex:210; label eq:ch4-14.

```tex
CE_0=E_0C.
```

### (4-15)
Source: PDF 152 / printed 140; sec4_2.tex:220; label eq:ch4-15.

```tex
\ket{\Psi}=p\ket{\Omega},\qquad p\in\PolynomialAlgebra(\mathcal O)
```

### (4-16)
Source: PDF 152 / printed 140; sec4_2.tex:236; label eq:ch4-16.

```tex
\begin{aligned} \bra{\Phi}C\ket{\Psi} &=\bra{\Phi}Cp\ket{\Omega} =\bra{p^\dagger\Phi}C\ket{\Omega} =\bra{p^\dagger\Phi}CE_0\ket{\Omega} \\ &=\bra{p^\dagger\Phi}E_0C\ket{\Omega} =\braket{p^\dagger\Phi}{\Omega} \bra{\Omega}C\ket{\Omega}, \end{aligned}
```

### (4-17)
Source: PDF 153 / printed 141; sec4_2.tex:312; label eq:ch4-17.

```tex
\matrixel{\Phi}{C\varphi(f_1)\cdots\varphi(f_n)}{\Psi} =\matrixel{\varphi(f_n)^\dagger\cdots\varphi(f_1)^\dagger\Phi}{C}{\Psi}.
```

### (4-18)
Source: PDF 153 / printed 141; sec4_2.tex:326; label eq:ch4-18.

```tex
\begin{aligned} &\bra{\Omega}C\varphi(\{a,1\}f_1)\cdots \varphi(\{a,1\}f_n)\ket{\Omega} \\ &\quad=\bra{\varphi(\{a,1\}f_n)^\dagger\cdots \varphi(\{a,1\}f_1)^\dagger\Omega}C\ket{\Omega}. \end{aligned}
```

### (4-19)
Source: PDF 154 / printed 142; sec4_3.tex:56; label eq:ch4-19-pct-identity.

```tex
\bra{\Omega}\varphi_1(x_1)\cdots\varphi_n(x_n)\ket{\Omega} =(-1)^J\ii^F \bra{\Omega}\varphi_n(-x_n)\cdots\varphi_1(-x_1)\ket{\Omega}.
```

### (4-20)
Source: PDF 155 / printed 143; sec4_3.tex:86; label eq:ch4-20-pct-condition.

```tex
\bra{\Omega}\varphi(x_1)\cdots\varphi(x_n)\ket{\Omega} =\bra{\Omega}\varphi(-x_n)\cdots\varphi(-x_1)\ket{\Omega}
```

### (4-21)
Source: PDF 155 / printed 143; sec4_3.tex:98; label eq:ch4-21-wlc-condition.

```tex
\bra{\Omega}\varphi(x_1)\cdots\varphi(x_n)\ket{\Omega} =\bra{\Omega}\varphi(x_n)\cdots\varphi(x_1)\ket{\Omega}
```

### (4-22)
Source: PDF 155 / printed 143; sec4_3.tex:126; label eq:ch4-22-forward-boundary-value.

```tex
\begin{aligned} \lim_{\substack{\eta_1,\ldots,\eta_{n-1}\to0\\ \eta\in V_+}} W(\zeta_1,\ldots,\zeta_{n-1}) &=W(\xi_1,\ldots,\xi_{n-1}) \\ &=\bra{\Omega}\varphi(x_1)\cdots\varphi(x_n)\ket{\Omega}. \end{aligned}
```

### (4-23)
Source: PDF 155 / printed 143; sec4_3.tex:137; label eq:ch4-23-lorentz-invariance.

```tex
W(\zeta_1,\ldots,\zeta_{n-1}) =W(\Lambda\zeta_1,\ldots,\Lambda\zeta_{n-1}),
```

### (4-24)
Source: PDF 155 / printed 143; sec4_3.tex:149; label eq:ch4-24-sign-reversal.

```tex
W(\zeta_1,\ldots,\zeta_{n-1}) =W(-\zeta_1,\ldots,-\zeta_{n-1}) \quad\text{for }\zeta_1,\ldots,\zeta_{n-1}\in\mathcal{T}'_{n-1}.
```

### (4-25)
Source: PDF 156 / printed 144; sec4_3.tex:166; label eq:ch4-25-reversed-boundary-value.

```tex
\begin{aligned} \lim_{\substack{\eta_1,\ldots,\eta_{n-1}\to0\\ \eta\in V_+}} W(\zeta_{n-1},\ldots,\zeta_1) &=W(\xi_{n-1},\ldots,\xi_1) \\ &=\bra{\Omega}\varphi(-x_n)\varphi(-x_{n-1})\cdots \varphi(-x_1)\ket{\Omega}. \end{aligned}
```

### (4-26)
Source: PDF 156 / printed 144; sec4_3.tex:179; label eq:ch4-26-reversed-holomorphic.

```tex
W(\zeta_1,\ldots,\zeta_{n-1}) =W(\zeta_{n-1},\ldots,\zeta_1).
```

### (4-27)
Source: PDF 156 / printed 144; sec4_3.tex:196; label eq:ch4-27-wlc-holomorphic.

```tex
W(\zeta_1,\ldots,\zeta_{n-1}) =W(-\zeta_{n-1},\ldots,-\zeta_1).
```

### (4-28)
Source: PDF 156 / printed 144; sec4_3.tex:215; label eq:ch4-28-wlc-jost.

```tex
\begin{aligned} W(\zeta_1,\ldots,\zeta_{n-1}) &=\bra{\Omega}\varphi(x_1)\cdots\varphi(x_n)\ket{\Omega} \\ &=W(-\zeta_{n-1},\ldots,-\zeta_1) =\bra{\Omega}\varphi(x_n)\cdots\varphi(x_1)\ket{\Omega}. \end{aligned}
```

### (4-29)
Source: PDF 157 / printed 145; sec4_3.tex:255; label eq:ch4-29-general-lorentz.

```tex
\begin{aligned} \sum_{\mu'\ldots\nu'} S^{(\varphi)}_{\mu\ldots\mu'}(A,B)\cdots S^{(\psi)}_{\nu\ldots\nu'}(A,B) W_{\mu'\ldots\nu'}(\zeta_1,\ldots,\zeta_{n-1}) \\ ={}&W_{\mu\ldots\nu}\bigl(\Lambda(A,B)\zeta_1,\ldots, \Lambda(A,B)\zeta_{n-1}\bigr). \end{aligned}
```

### (4-30)
Source: PDF 157 / printed 145; sec4_3.tex:271; label eq:ch4-30-general-boundary.

```tex
\begin{aligned} \lim_{\substack{\eta_1,\ldots,\eta_{n-1}\to0\\ \eta\in V_+}} W_{\mu\ldots\nu}(\zeta_1,\ldots,\zeta_{n-1}) &=W_{\mu\ldots\nu}(\xi_1,\ldots,\xi_{n-1}) \\ &=\bra{\Omega}\varphi_\mu(x_1)\cdots \varphi_\nu(x_n)\ket{\Omega}. \end{aligned}
```

### (4-31)
Source: PDF 157 / printed 145; sec4_3.tex:287; label eq:ch4-31-general-sign.

```tex
S^{(\varphi)}_{\mu\mu'}(-1,1)\cdots S^{(\psi)}_{\nu\nu'}(-1,1) =\delta_{\mu\mu'}\cdots\delta_{\nu\nu'}(-1)^J,
```

### (4-32)
Source: PDF 157 / printed 145; sec4_3.tex:298; label eq:ch4-32-general-sign-reversal.

```tex
W_{\mu\ldots\nu}(\zeta_1,\ldots,\zeta_{n-1}) =(-1)^J W_{\mu\ldots\nu}(-\zeta_1,\ldots,-\zeta_{n-1})
```

### (4-33)
Source: PDF 157 / printed 145; sec4_3.tex:310; label eq:ch4-33-general-pct-holomorphic.

```tex
W_{\mu\ldots\nu}(\zeta_1,\ldots,\zeta_{n-1}) =\ii^F(-1)^J\widehat{W}_{\nu\ldots\mu} (\zeta_{n-1},\ldots,\zeta_1),
```

### (4-34)
Source: PDF 157 / printed 145; sec4_3.tex:327; label eq:ch4-34-general-pct-boundary.

```tex
\begin{aligned} \lim_{\substack{\eta_1,\ldots,\eta_{n-1}\to0\\ \eta\in V_+}} \widehat{W}_{\nu\ldots\mu}(\zeta_{n-1},\ldots,\zeta_1) &=\widehat{W}_{\nu\ldots\mu}(\xi_{n-1},\ldots,\xi_1) \\ &=\bra{\Omega}\psi_\nu(-x_n)\cdots \varphi_\mu(-x_1)\ket{\Omega}. \end{aligned}
```

### (4-35)
Source: PDF 157 / printed 145; sec4_3.tex:338; label eq:ch4-35-general-wlc-holomorphic.

```tex
W_{\mu\ldots\nu}(\zeta_1,\ldots,\zeta_{n-1}) =\ii^F\widehat{W}_{\nu\ldots\mu} (-\zeta_{n-1},\ldots,-\zeta_1),
```

### (4-36)
Source: PDF 157 / printed 145; sec4_3.tex:349; label eq:ch4-36-general-wlc.

```tex
\bra{\Omega}\varphi_\mu(x_1)\cdots\psi_\nu(x_n)\ket{\Omega} =\ii^F\bra{\Omega}\psi_\nu(x_n)\cdots \varphi_\mu(x_1)\ket{\Omega}.
```

### (4-37)
Source: PDF 159 / printed 147; sec4_4.tex:119; label eq:ch4-37-commutation-opposite.

```tex
[\varphi(x),\psi(y)]_{\pm}=0 \qquad\text{for }(x-y)^2>0, \qquad\text{and the opposite} \qquad [\varphi(x),\psi^\dagger(y)]_{\mp}=0
```

### (4-38)
Source: PDF 159 / printed 147; sec4_4.tex:135; label eq:ch4-38-positive-norm.

```tex
\bra{\Omega}\varphi^\dagger(f)\psi^\dagger(g)\psi(g)\varphi(f)\ket{\Omega} =\bigl\lVert\psi(g)\varphi(f)\ket{\Omega}\bigr\rVert^2\geq0.
```

### (4-39)
Source: PDF 160 / printed 148; sec4_4.tex:145; label eq:ch4-39-reordered-negative.

```tex
-\bra{\Omega}\psi^\dagger(g)\psi(g)\varphi(f)\varphi^\dagger(f)\ket{\Omega}.
```

### (4-40)
Source: PDF 160 / printed 148; sec4_4.tex:180; label eq:ch4-40-no-nonzero-field-first.

```tex
[\varphi(x),\varphi(y)]_{\pm}=0
```

### (4-41)
Source: PDF 160 / printed 148; sec4_4.tex:208; label eq:ch4-41-wrong-scalar-statistics.

```tex
[\varphi(x),\varphi^\dagger(y)]_{\pm}=0 \qquad\text{for }(x-y)^2>0.
```

### (4-42)
Source: PDF 160 / printed 148; sec4_4.tex:227; label eq:ch4-42-scalar-vacuum-relation.

```tex
\bra{\Omega}\varphi(x)\varphi^\dagger(y)\ket{\Omega} +\bra{\Omega}\varphi^\dagger(y)\varphi(x)\ket{\Omega}=0.
```

### (4-43)
Source: PDF 161 / printed 149; sec4_4.tex:244; label eq:ch4-43-holomorphic-boundaries.

```tex
\begin{aligned} \bra{\Omega}\varphi(x)\varphi^\dagger(y)\ket{\Omega} &=\lim_{\substack{\eta\to0\\\eta\in V_+}} W(x-y-\ii\eta),\\ \bra{\Omega}\varphi^\dagger(y)\varphi(x)\ket{\Omega} &=\lim_{\substack{\eta\to0\\\eta\in V_+}} \widehat W(y-x-\ii\eta). \end{aligned}
```

### (4-44)
Source: PDF 161 / printed 149; sec4_4.tex:258; label eq:ch4-44-holomorphic-sum.

```tex
W(\zeta)+\widehat W(-\zeta)=0,
```

### (4-45)
Source: PDF 161 / printed 149; sec4_4.tex:269; label eq:ch4-45-hat-w-invariance.

```tex
\widehat W(\zeta)=\widehat W(-\zeta),
```

### (4-46)
Source: PDF 161 / printed 149; sec4_4.tex:278; label eq:ch4-46-holomorphic-zero.

```tex
W(\zeta)+\widehat W(\zeta)=0,
```

### (4-47)
Source: PDF 161 / printed 149; sec4_4.tex:292; label eq:ch4-47-distribution-relation.

```tex
\bra{\Omega}\varphi(x)\varphi^\dagger(y)\ket{\Omega} +\bra{\Omega}\varphi^\dagger(-y)\varphi(-x)\ket{\Omega}=0.
```

### (4-48)
Source: PDF 162 / printed 150; sec4_4.tex:358; label eq:ch4-48-general-spin-wrong-statistics.

```tex
\begin{aligned} [\varphi_\alpha(x),\varphi_\alpha^\dagger(y)]_+&=0 &&\varphi\text{ of integer spin},\\ [\varphi_\alpha(x),\varphi_\alpha^\dagger(y)]_-&=0 &&\varphi\text{ of half-odd integer spin},\\[-2pt] &\hspace{2cm}\text{for }(x-y)^2>0 \end{aligned}
```

### (4-49)
Source: PDF 162 / printed 150; sec4_4.tex:380; label eq:ch4-49-general-spin-vacuum.

```tex
\bra{\Omega}\varphi(x)\varphi^\dagger(y)\ket{\Omega} \mathbin{\pm} \bra{\Omega}\varphi^\dagger(y)\varphi(x)\ket{\Omega}=0, \qquad\text{for }(x-y)^2>0,
```

### (4-50)
Source: PDF 162 / printed 150; sec4_4.tex:391; label eq:ch4-50-general-spin-holomorphic.

```tex
W(\zeta)\mathbin{\pm}\widehat W(-\zeta)=0,
```

### (4-51)
Source: PDF 162 / printed 150; sec4_4.tex:400; label eq:ch4-51-general-spin-invariance.

```tex
\widehat W(\zeta)=(-1)^J\widehat W(-\zeta),
```

### (4-52)
Source: PDF 162 / printed 150; sec4_4.tex:415; label eq:ch4-52-general-spin-holomorphic-invariance.

```tex
\widehat W(\zeta)=\mathbin{\pm}\widehat W(-\zeta),
```

### (4-53)
Source: PDF 164 / printed 152; sec4_4.tex:560; label eq:ch4-53-example-2-normal.

```tex
[\psi_1(x),\psi_2(y)]_+=0=[\varphi(x),\psi_2(y)]_- \qquad (x-y)^2>0
```

### (4-54)
Source: PDF 164 / printed 152; sec4_4.tex:570; label eq:ch4-54-example-2-abnormal.

```tex
[\varphi(x),\psi_1(y)]_+=0, \qquad (x-y)^2>0.
```

### (4-55)
Source: PDF 165 / printed 153; sec4_4.tex:599; label eq:ch4-55-theorem-4-11-cluster.

```tex
\begin{aligned} &\bra{\Omega}M(x_1,\ldots,x_j)N(y_1+a,\ldots,y_k+a)\ket{\Omega}\\ &\quad=-\bra{\Omega}N(y_1+a,\ldots,y_k+a)M(x_1,\ldots,x_j)\ket{\Omega} \end{aligned}
```

### (4-56)
Source: PDF 165 / printed 153; sec4_4.tex:646; label eq:ch4-56-example-2-vacuum-zero.

```tex
\bra{\Omega}\varphi(y_1)\cdots\varphi(y_j) \psi_1(y_{j+1})\cdots\psi_1(y_{j+k}) \psi_2(y_{j+k+1})\cdots\psi_2(y_{j+k+\ell})\ket{\Omega}=0 \qquad k\ \text{odd},\ \ell\ \text{odd}.
```

### (4-57)
Source: PDF 167 / printed 155; sec4_4.tex:757; label eq:ch4-57-klein-general.

```tex
\begin{aligned} \varphi'_j&=p(\alpha)\varphi_j, &&\varphi_j\in\beta,\\ \varphi'_j&=\varphi_j, &&\varphi_j\notin\beta. \end{aligned}
```

### (4-58)
Source: PDF 168 / printed 156; sec4_4.tex:840; label eq:ch4-58-sigma-definition.

```tex
\begin{aligned} \sigma_{ij}&=0 &&\text{if }\varphi_i,\varphi_j\text{ have normal commutation relations},\\ \sigma_{ij}&=1 &&\text{otherwise.} \end{aligned}
```

### (4-59)
Source: PDF 169 / printed 157; sec4_4.tex:922; label eq:ch4-59-parity-sum.

```tex
\sum_j s_j(M)t_j(\beta)= \left(\begin{smallmatrix}0\\1\end{smallmatrix}\right)\pmod 2.
```

### (4-60)
Source: PDF 169 / printed 157; sec4_4.tex:936; label eq:ch4-60-normal-monomial-pairing.

```tex
\sum_{i,j}s_i(M)\sigma_{ij}s_j(N)= \left(\begin{array}{ll} 0&\text{if $M,N$ obey the normal commutation relations},\\ 1&\text{otherwise,} \end{array}\right)\pmod 2.
```

### (4-61)
Source: PDF 169 / printed 157; sec4_4.tex:953; label eq:ch4-61-set-membership.

```tex
\text{either }t_i(\alpha)=t_j(\beta)=1 \qquad\text{or}\qquad t_i(\beta)=t_j(\alpha)=1.
```

### (4-62)
Source: PDF 169 / printed 157; sec4_4.tex:965; label eq:ch4-62-sigma-update.

```tex
\sigma_{ij}\longrightarrow\sigma_{ij} +t_i(\alpha)t_j(\beta)+t_j(\alpha)t_i(\beta)\pmod 2.
```

### (4-63)
Source: PDF 170 / printed 158; sec4_4.tex:985; label eq:ch4-63-sigma-decomposition.

```tex
\sigma_{ij}=\sum_{k=1}^{N} \bigl[t_i(\alpha_k)s_j^{(k)}+s_i^{(k)}t_j(\alpha_k)\bigr]\pmod 2,
```

### (4-64)
Source: PDF 170 / printed 158; sec4_4.tex:1030; label eq:ch4-64-even-odd-criterion.

```tex
\sum_j s_jt_j(\alpha)=0\pmod 2 \qquad\text{for all }s\in\Gamma
```

### (4-65)
Source: PDF 171 / printed 159; sec4_4.tex:1059; label eq:ch4-65-gamma-orthogonality.

```tex
\sum_{i,j}s_i(M)\sigma_{ij}s_j(N)=0 \qquad\text{if }s(M),s(N)\in\Gamma,
```

### (4-66)
Source: PDF 171 / printed 159; sec4_4.tex:1077; label eq:ch4-66-dual-basis.

```tex
\bigl(e^{(j)},d^{(k)}\bigr)=\sum_i e_i^{(j)}d_i^{(k)}=\delta_{jk}\pmod 2.
```

### (4-67)
Source: PDF 171 / printed 159; sec4_4.tex:1110; label eq:ch4-67-new-coordinate-matrix.

```tex
\sigma'_{ij}=\bigl(e^{(i)},\sigma e^{(j)}\bigr).
```

### (4-68)
Source: PDF 171 / printed 159; sec4_4.tex:1120; label eq:ch4-68-coordinate-form.

```tex
(t,\sigma s)=\sum_{i,k}(t,d^{(i)})\sigma'_{ik}(d^{(k)},s); \qquad s,t\in V.
```

### (4-69)
Source: PDF 172 / printed 160; sec4_4.tex:1190; label eq:ch4-69-pct-abnormal.

```tex
\Theta\varphi'_i(f)\Theta^{-1} =(-1)^J\left(\begin{smallmatrix}\ii\\1\end{smallmatrix}\right) \varphi_i^{\prime\dagger}(\widehat f), \qquad \Theta\ket{\Omega}=\ket{\Omega}.
```

### (4-70)
Source: PDF 173 / printed 161; sec4_5.tex:65; label eq:ch4-interaction-picture.

```tex
V(t)\varphi(x,t)V(t)^{-1}=\varphi_{\mathrm{int}}(x,t).
```

### (4-71)
Source: PDF 174 / printed 162; sec4_5.tex:121; label eq:ch4-field-transformation.

```tex
U_j(a,A)\varphi_{j\alpha}(f,t)U_j(a,A)^{-1} =\sum_\beta S_{\alpha\beta}(A^{-1}) \varphi_{j\beta}(\{a,A\}f,t).
```

### (4-72)
Source: PDF 174 / printed 162; sec4_5.tex:132; label eq:ch4-invariant-vacuum.

```tex
U_j(a,A)\ket{\Psi_{j0}}=\ket{\Psi_{j0}}\qquad j=1,2.
```

### (4-73)
Source: PDF 174 / printed 162; sec4_5.tex:143; label eq:ch4-unitary-field-equivalence.

```tex
\varphi_{2\alpha}(f,t) =V\varphi_{1\alpha}(f,t)V^{-1}.
```

### (4-74)
Source: PDF 174 / printed 162; sec4_5.tex:152; label eq:ch4-representation-equivalence.

```tex
U_2(a,A)=VU_1(a,A)V^{-1}
```

### (4-75)
Source: PDF 174 / printed 162; sec4_5.tex:161; label eq:ch4-vacuum-phase.

```tex
c\ket{\Psi_{20}}=V\ket{\Psi_{10}},
```

### (4-76)
Source: PDF 175 / printed 163; sec4_5.tex:189; label eq:ch4-equal-time-vacuum.

```tex
\bra{\Psi_{10}}\varphi_{1\alpha}(x_1,t)\cdots \varphi_{1\beta}(x_n,t)\ket{\Psi_{10}} = \bra{\Psi_{20}}\varphi_{2\alpha}(x_1,t)\cdots \varphi_{2\beta}(x_n,t)\ket{\Psi_{20}}.
```

### (4-77)
Source: PDF 175 / printed 163; sec4_5.tex:209; label eq:ch4-jost-schroer-two-point.

```tex
\bra{\Psi_0}\varphi(x)\varphi(y)\ket{\Psi_0} =\frac{1}{\ii}\Delta^+(x-y;m)
```

### (4-78)
Source: PDF 175 / printed 163; sec4_5.tex:259; label eq:ch4-positive-part-annihilates-vacuum.

```tex
\varphi_+(f)\ket{\Psi_0}=0.
```

### (4-79)
Source: PDF 176 / printed 164; sec4_5.tex:268; label eq:ch4-positive-negative-state.

```tex
\varphi_+(x)\varphi_-(y)\ket{\Psi_0}.
```

### (4-80)
Source: PDF 176 / printed 164; sec4_5.tex:292; label eq:ch4-positive-negative-action.

```tex
\varphi_+(x)\varphi_-(y)\ket{\Psi_0} =\frac{1}{\ii}\Delta^+(x-y)\ket{\Psi_0},
```

### (4-81)
Source: PDF 176 / printed 164; sec4_5.tex:302; label eq:ch4-positive-negative-commutator.

```tex
\frac{1}{\ii}\Delta^+(x-y)\ket{\Psi_0} =[\varphi_+(x),\varphi_-(y)]\ket{\Psi_0}.
```

### (4-82)
Source: PDF 176 / printed 164; sec4_5.tex:321; label eq:ch4-commutator-decomposition.

```tex
[\varphi(x),\varphi(y)]\ket{\Psi_0} =\frac{1}{\ii}\Delta(x-y)\ket{\Psi_0} +[\varphi_-(x),\varphi_-(y)]\ket{\Psi_0},
```

### (4-83)
Source: PDF 176 / printed 164; sec4_5.tex:371; label eq:ch4-commutator-vacuum-final.

```tex
[\varphi(x),\varphi(y)]\ket{\Psi_0} =\frac{1}{\ii}\Delta(x-y)\ket{\Psi_0}.
```

### (4-84)
Source: PDF 177 / printed 165; sec4_5.tex:390; label eq:ch4-free-field-equations.

```tex
(\Box-m^2)\varphi(x)=0,\qquad [\varphi(x),\varphi(y)]=\frac{1}{\ii}\Delta(x-y),
```

### (4-85)
Source: PDF 178 / printed 166; sec4_5.tex:468; label eq:ch4-haag-two-point-equal-time.

```tex
\bra{\Psi_{20}}\varphi_2(x,t)\varphi_2(y,t)\ket{\Psi_{20}} =\frac{1}{\ii}\Delta^+(x-y,0;m).
```

### (4-86)
Source: PDF 178 / printed 166; sec4_5.tex:509; label eq:ch4-generalized-haag-covariance.

```tex
U_j(a,A)\varphi_{j\alpha}(x)U_j(a,A)^{-1} =\sum_\beta S_{\alpha\beta}(A^{-1})\varphi_{j\beta}(Ax+a).
```

### (4-87)
Source: PDF 179 / printed 167; sec4_5.tex:557; label eq:ch4-jost-criterion-two.

```tex
\abs{\xi_1\mathbin{\cdot}\xi_2} <\sqrt{\xi_1^2\xi_2^2},\qquad \xi_1^2>0,\qquad \xi_2^2>0,
```

### (4-88)
Source: PDF 179 / printed 167; sec4_5.tex:576; label eq:ch4-jost-criterion-three.

```tex
\left\{ \begin{matrix} \xi_1^2 & \xi_1\mathbin{\cdot}\xi_2 & \xi_1\mathbin{\cdot}\xi_3\\ \xi_2\mathbin{\cdot}\xi_1 & \xi_2^2 & \xi_2\mathbin{\cdot}\xi_3\\ \xi_3\mathbin{\cdot}\xi_1 & \xi_3\mathbin{\cdot}\xi_2 & \xi_3^2 \end{matrix} \right\}
```

### (4-89)
Source: PDF 180 / printed 168; sec4_5.tex:612; label eq:ch4-equation-of-motion-example.

```tex
(-\Box+m^2)\varphi(x)=\lambda\varphi(x)^3
```

### (4-90)
Source: PDF 180 / printed 168; sec4_6.tex:21; label eq:ch4-relative-locality-assumptions.

```tex
\begin{aligned} [\varphi_1(x),\varphi_2(y)]_-&=0,\\ [\varphi_1(x),\varphi_3(y)]_-&=0, \qquad \text{for }(x-y)^2>0. \end{aligned}
```

### (4-91)
Source: PDF 180 / printed 168; sec4_6.tex:32; label eq:ch4-relative-locality-conclusion.

```tex
[\varphi_2(x),\varphi_3(y)]_-=0, \qquad \text{for }(x-y)^2>0.
```

### (4-92)
Source: PDF 182 / printed 170; sec4_6.tex:140; label eq:ch4-wlc.

```tex
\bra{\Omega}\varphi(x_1)\cdots\varphi(x_n)\ket{\Omega} = \bra{\Omega}\varphi(x_n)\cdots\varphi(x_1)\ket{\Omega}
```

### (4-93)
Source: PDF 182 / printed 170; sec4_6.tex:151; label eq:ch4-wlc-pct.

```tex
\Theta\varphi(f)\Theta^{-1}=\varphi(\widehat f).
```

### (4-94)
Source: PDF 183 / printed 171; sec4_6.tex:216; label eq:ch4-wlc-interchange.

```tex
\begin{aligned} &\bra{\Omega}\varphi(x_1)\cdots\varphi(x_j)\psi(x) \varphi(x_{j+1})\cdots\varphi(x_n)\ket{\Omega}\\ &\quad = \bra{\Omega}\varphi(x_n)\cdots\varphi(x_{j+1})\psi(x) \varphi(x_j)\cdots\varphi(x_1)\ket{\Omega} \end{aligned}
```

### (4-95)
Source: PDF 183 / printed 171; sec4_6.tex:238; label eq:ch4-antiunitary-field.

```tex
\matrixel{\Theta\Phi}{\Theta\psi(x)\Theta^{-1}}{\Theta\Psi} = \matrixel{\Phi}{\psi(x)}{\Psi}^{*}.
```

### (4-96)
Source: PDF 183 / printed 171; sec4_6.tex:254; label eq:ch4-wlc-holomorphic.

```tex
\begin{aligned} &\bra{\Omega}\varphi(x_1)\cdots\varphi(x_j)\psi(x) \varphi(x_{j+1})\cdots\varphi(x_n)\ket{\Omega}\\ &\quad - \bra{\Omega}\varphi(-x_n)\cdots\varphi(-x_{j+1})\psi(-x) \varphi(-x_j)\cdots\varphi(-x_1)\ket{\Omega}=0. \end{aligned}
```

### (4-97)
Source: PDF 183 / printed 171; sec4_6.tex:262; label eq:ch4-wlc-tube.

```tex
\operatorname{Im}(x_1-x_2),\ldots,\operatorname{Im}(x_j-x), \operatorname{Im}(x-x_{j+1}),\ldots, \operatorname{Im}(x_{n-1}-x_n)\in -V_+.
```

### (4-98)
Source: PDF 183 / printed 171; sec4_6.tex:276; label eq:ch4-wlc-test-states.

```tex
\ket{\Psi} =\varphi(f_1)\cdots\varphi(f_j)\ket{\Omega}, \qquad \ket{\Phi} =\varphi(f_{j+1})\cdots\varphi(f_n)\ket{\Omega}.
```

### (4-99)
Source: PDF 185 / printed 173; sec4_6.tex:361; label eq:ch4-asymptotic-in.

```tex
\varphi_1^{\mathrm{in}}(x)=\varphi_2^{\mathrm{in}}(x)
```

### (4-100)
Source: PDF 185 / printed 173; sec4_6.tex:370; label eq:ch4-asymptotic-out.

```tex
\varphi_1^{\mathrm{out}}(x)=\varphi_2^{\mathrm{out}}(x).
```

### (4-101)
Source: PDF 186 / printed 174; sec4_6.tex:525; label eq:ch4-unique-local-solution.

```tex
(-\Box+m^2)u(x)=j(x)
```

## Theorem inventory

1. Theorem 4-1, thm:ch4-global-locality, PDF 146 / printed 134. A hermitian scalar field satisfies axioms I and II, has relation (4-1) on some spacelike-separated open sets, and has a cyclic vacuum. The conclusion is that the field is local and (4-1) holds for every spacelike-separated pair.
2. Theorem 4-2, thm:ch4-2-reeh-schlieder, PDF 150 / printed 138. For an open spacetime set O, the vacuum is cyclic for the polynomial algebra P(O) when it is cyclic for P(R4). Vectors of the form (4-10), with test-function supports in O, are dense in the Hilbert space.
3. Theorem 4-3, thm:ch4-3-separating, PDF 151 / printed 139. If O is open, O-prime is nonempty, and T belongs to P(O), then T ket Omega = 0, as in (4-11), implies T = 0.
4. Theorem 4-4, thm:ch4-4-adjoined-projection, PDF 152 / printed 140. Let E0 be the projection onto the vacuum, with the vacuum cyclic for the field. For every open O, the set {E0, P(O)} is irreducible.
5. Theorem 4-5, thm:ch4-5-smeared-fields, PDF 153 / printed 141. In any field theory, the smeared fields form an irreducible set of operators.
6. Theorem 4-6, thm:ch4-6-neutral-scalar-pct, PDF 155 / printed 143. A hermitian scalar field satisfies axioms I and II, without requiring III (LC). If PCT condition (4-20) holds for all points, WLC condition (4-21) holds at every Jost point. Conversely, WLC in a real neighborhood of a Jost point implies PCT everywhere. Since LC implies WLC, every theory of a local hermitian scalar field has PCT symmetry.
7. Theorem 4-7, thm:ch4-7-general-spin-pct, PDF 158 / printed 146. Spinor fields satisfying axioms I and II, without requiring III (LC), obey the general-spin PCT condition in the two unnumbered displays on this source page. WLC holds at Jost points. Conversely, WLC in a real neighborhood of a Jost point implies the PCT conditions everywhere. Normal commutation relations imply WLC, so a theory with normal commutation relations has PCT symmetry.
8. Theorem 4-8, thm:ch4-8, PDF 159 / printed 147. If a field theory has the two opposite spacelike commutation relations in (4-37), then either field vanishes.
9. Theorem 4-9, thm:ch4-9-scalar-spin-statistics, PDF 160 / printed 148. A scalar field obeying the wrong spin-statistics relation (4-41) has phi(x) ket Omega = 0 = phi-dagger(x) ket Omega. If phi and phi-dagger commute or anticommute with every other field, then phi = phi-dagger = 0.
10. Theorem 4-10, thm:ch4-10-general-spin-statistics, PDF 162 / printed 150. For a general irreducible spinor field, the wrong spin-statistics relation (4-48) implies phi-alpha(x) ket Omega = 0. If all fields commute or anticommute, then phi-alpha = phi-alpha-dagger = 0.
11. Theorem 4-11, thm:ch4-11, PDF 164 / printed 152. In a local field theory, if monomials M(x1,...,xj) and N(y1,...,yk) anticommute when the two point sets are spacelike separated, then either the vacuum expectation of M or the vacuum expectation of N vanishes.
12. Theorem 4-12, thm:ch4-12, PDF 166 / printed 154. In any field theory with abnormal commutation relations, an irreducible set of fields with normal commutation relations exists, obtained from the original set by a Klein transformation.
13. Theorem 4-13, thm:ch4-13, PDF 170 / printed 158. If sigma_ij is 0 for normal and 1 for abnormal commutation relations, then sigma has decomposition (4-63), where the alpha_k have even-odd rules and the s^(k) are vectors in V.
14. Theorem 4-14, thm:ch4-14-unitary-equivalence, PDF 174 / printed 162. Two irreducible sets of field operators at time t, in Hilbert spaces H1 and H2, carry continuous unitary representations of inhomogeneous SU(2), transform as (4-71), and have unique invariant states (4-72). If a unitary V relates the fields at time t as (4-73), then the representations are related by (4-74) and the invariant vacua differ by a phase as in (4-75), with c of modulus one.
15. Theorem 4-15, thm:ch4-15-jost-schroer, PDF 175 / printed 163. If phi is a hermitian scalar local field with cyclic vacuum and its two-point function is (4-77), with m > 0, then phi is a free field of mass m.
16. Theorem 4-16, thm:ch4-16-haag, PDF 177 / printed 165. Let phi_1 be a free hermitian scalar field of mass m > 0 and phi_2 a local field covariant under inhomogeneous SL(2,C). If phi_1, its time derivative, phi_2, and its time derivative satisfy Theorem 4-14, then phi_2 is a free field of mass m.
17. Theorem 4-17, thm:ch4-17-generalized-haag, PDF 178 / printed 166. Two theories satisfy Theorem 4-14 and are invariant under inhomogeneous SL(2,C). For fields transforming as (4-86), all expectation values involving four or fewer of those fields coincide in the two theories.
18. Theorem 4-18, thm:ch4-18-weak-local-relative, PDF 183 / printed 171. A weakly local phi has cyclic vacuum. A second field psi transforms under the same P-plus-up representation and has the same domain. If (4-94) holds at Jost points for every j and n, then psi is weakly local and phi and psi are weakly local with respect to each other.
19. Theorem 4-19, thm:ch4-19-transitivity, PDF 184 / printed 172. If phi_1 is weakly local with cyclic vacuum, and phi_2 and phi_3 are weakly local with respect to phi_1 with the same domain and P-plus-up representation, then phi_2 is weakly local with respect to phi_3.
20. Theorem 4-20, thm:ch4-20-asymptotic-fields, PDF 185 / printed 173. If phi_1 is weakly local with cyclic vacuum, phi_2 is weakly local with respect to phi_1, and the asymptotic in-fields agree as in (4-99), then the out-fields agree as in (4-100).
21. Theorem 4-21, thm:ch4-21-relative-locality-transitive, PDF 185 / printed 173. Three fields have the same domain and representation U of P-plus-up; phi_1 is local with cyclic vacuum; and phi_1 commutes with phi_2 and phi_3 at spacelike separation. Then phi_2 commutes with phi_3 at spacelike separation.
22. Theorem 4-22, thm:ch4-22-unique-local-solution, PDF 186 / printed 174. Given an irreducible local field j and a local solution u of (4-101) with a one-particle state of mass m, u is uniquely determined by the boundary condition displayed after (4-101).

The formula belonging to each theorem is listed at its source equation number above. Theorem 4-7 uses the two unnumbered displays in sec4_4.tex at PDF 158 / printed 146.

## Corollary inventory

- Corollary after Theorem 4-8, cor-ch4-8, PDF 160 / printed 148. No nonzero field can satisfy (4-40) together with the opposite relation for phi and phi-dagger at every spacelike separation.
- Corollary after Theorem 4-14, cor-ch4-equal-time-vacuum, PDF 175 / printed 163. In any two theories satisfying Theorem 4-14, equal-time vacuum expectation values are identical, as shown by (4-76).
- Corollary after Theorem 4-21, corollary-ch4-21, PDF 186 / printed 174. With phi_2 = phi_3, if phi_1 is local with cyclic vacuum and phi_2 is local relative to phi_1, then phi_2 is local.

## Example inventory

- Example 1, ex-ch4-1-anticommuting-scalar-spin-half, PDF 163 / printed 151 through PDF 164 / printed 152. Heading: “Anti-commuting Scalar and Spin 1/2 Field.” It defines transformed scalar and spin-half fields on the integer-spin and half-odd-integer-spin coherent subspaces, with the univalence superselection rule.
- Example 2, ex-ch4-2-scalar-two-spin-half, PDF 164 / printed 152 through PDF 166 / printed 154. Heading: “A Scalar and Two Spin 1/2 Fields.” It treats one hermitian scalar and two hermitian half-odd-integer-spin fields, their normal and abnormal relations, the resulting vacuum values, and the Klein transformation.
- Example 3, ex-ch4-3-anticommuting-hermitian-scalars, PDF 172 / printed 160 continuing on PDF 173 / printed 161 before Section 4-5. Heading: “Anti-Commuting Hermitian Scalar Fields.” It begins with two anticommuting hermitian scalar fields and continues through the even/odd Klein transformation and the abnormal PCT factor.

## Remark inventory

- Remark 1, ch4-remark-1, PDF 147 / printed 135. Covariance carries vanishing of (4-1) from a neighborhood of {x,y} to a neighborhood of {Lambda x+a, Lambda y+a}; the invariant squared separation covers an open set of the positive real axis in the house metric. Marker ch4-remark-1-continuation is the continuation of this same remark.
- Remark 2, ch4-remark-2, PDF 147 / printed 135. The asserted vanishing means that the commutator operator vanishes on its domain D.
- Section 4-2 Remark 1, remark-ch4-3-1-text, PDF 151 / printed 139. Theorem 4-3 remains valid when anticommutators replace commutators at spacelike separation; this is used in Theorem 4-8.
- Section 4-2 Remark 2, remark-ch4-3-2-text, PDF 152 / printed 140. Every bounded open set O has nonempty O-prime, so Theorem 4-3 applies.
- Section 4-2 Remark after Theorem 4-5, remark-ch4-5, PDF 153 / printed 141. The vacuum is cyclic for smeared fields, this hypothesis is essential, and the theorem justifies defining field theory by vacuum cyclicity rather than smeared-field irreducibility.
- Section 4-5 Remark after Theorem 4-17, remark-ch4-17, PDF 178 / printed 166. The generalized theorem applies when basic fields are covariant under inhomogeneous SL(2,C), while noncovariant conjugate momenta are needed for an irreducible equal-time set.

## Footnote inventory

- fn-p137-section-2-1, PDF 149 / printed 137: “See Section 2-1.”
- fn-p138-standard-arguments, PDF 150 / printed 138: “See Section 2-6.”
- fn-p142-von-neumann-algebra, PDF 154 / printed 142: “See Ref. 3 of Chapter 3.”
- fn-p156-parity, PDF 168 / printed 156: “Two numbers are said to have the same parity if they are both even, or both odd.”
- fn-p164-unsmeared-fields, PDF 176 / printed 164: “In this argument, and in several other places in the rest of the proof, we work with the unsmeared fields. This is purely a matter of convenience. The reader can easily supply the required smearing. For example, to deal with (4-79) one considers the tempered distribution T on R8 defined by <Psi|phi_+(f)phi_-(g)|Psi_0> = T(f,g) and argues that its Fourier transform is zero unless p_1^2 = -m^2, p_1^0 > 0, p_2^2 = -m^2, p_2^0 < 0. Thus, in the variables p_1+p_2, its support consists of spacelike or zero vectors. The conclusion follows as above.”
- fn-p167-jost-points, PDF 179 / printed 167: “See Theorem 2-12.”
- fn-p168-borchers-class, PDF 180 / printed 168: “We should mention at the outset that what is proved is that if a local phi_1 has the vacuum as cyclic vector, which implies that phi_1 is irreducible, then (4-90) implies (4-91). The phi_2, phi_3 need not be irreducible. In the customary mathematical definition of equivalence all elements of an equivalence class must be on the same footing, so strictly speaking it is the irreducible relatively local fields which form equivalence classes. In the following, the term equivalence class includes reducible relatively local fields along with the irreducible.”

## Proof-ending inventory

- Theorem 4-1, source PDF 149 / printed 137, native sec4_1.tex:273: manual black square after the density-domain argument.
- Theorem 4-2, source PDF 151 / printed 139, native sec4_2.tex:106: proof environment closes after orthogonality to D0.
- Theorem 4-3, source PDF 152 / printed 140, native sec4_2.tex:162: proof environment closes after the density argument.
- Theorem 4-4, source PDF 152 / printed 140, native sec4_2.tex:266: proof environment closes after C = c0.
- Theorem 4-5, source PDF 153 / printed 141, native sec4_2.tex:382: proof environment closes after irreducibility.
- Theorem 4-6, source PDF 157 / printed 145, native sec4_3.tex:233: manual black square after the Jost-point argument.
- Theorem 4-7 has no separate proof block in the source; the general-field proof immediately precedes its statement on PDF 158 / printed 146.
- Theorem 4-8, source PDF 160 / printed 148, native sec4_4.tex:169: manual black square before the corollary.
- Theorem 4-9, source PDF 162 / printed 150, native sec4_4.tex:336: manual black square after the vacuum-vanishing conclusion.
- Theorem 4-10, source PDF 162 / printed 150, native sec4_4.tex:421: manual black square after the general-spin conclusion.
- Theorem 4-11, source PDF 165 / printed 153, native sec4_4.tex:614: manual black square after the cluster limit.
- Theorem 4-12, source PDF 170 / printed 158, native sec4_4.tex:1006: manual black square after the Klein reduction.
- Theorem 4-13, source PDF 172 / printed 160, native sec4_4.tex:1169: manual black square after the even-odd rule.
- Theorem 4-14, source PDF 174-175 / printed 162-163, native sec4_5.tex:168: the source proof ends in prose, “We leave the details to the reader,” before Corollary; no printed square.
- Theorem 4-15, source PDF 177 / printed 165, native proof environment closes at sec4_5.tex:373 after (4-83), while the source logical closing square is retained at sec4_5.tex:443 after the Wightman recursion.
- Theorem 4-16, source PDF 178 / printed 166, native sec4_5.tex:485: manual black square before the environment close.
- Theorem 4-17, source PDF 179 / printed 167, native sec4_5.tex:582: manual black square before the environment close.
- Theorem 4-18, source PDF 184 / printed 172, native sec4_6.tex:314: proof environment closes after the WLC boundary-value argument.
- Theorem 4-19, source PDF 184 / printed 172, native sec4_6.tex:341: proof environment closes after the transitivity argument.
- Theorem 4-20, source PDF 185 / printed 173, native sec4_6.tex:380: proof environment closes after the asymptotic-field argument.
- Theorem 4-21, source PDF 186 / printed 174, native sec4_6.tex:449: proof environment closes after the vacuum commutator argument. Theorem 4-22 has a statement and application but no separate proof.

## Bibliography inventory

The bibliography is source ordered and contains 29 numeric entries plus 19a. The TeX entry text below is complete after line reflow.

1. Item 1; source PDF 187 / printed 175; marker bib-4-1;
```tex
\bibitem{ch4-1} A.~S.~Wightman, ``Quantum Field Theory and Analytic Functions of Several Complex Variables,'' \emph{J.~Indian Math.~Soc.}, \textbf{24}, 625 (1960).
```

2. Item 2; source PDF 187 / printed 175; marker bib-4-2;
```tex
\bibitem{ch4-2} R.~Haag, ``Discussion des `Axiomes' et des propri\'et\'es asymptotiques d'une th\'eorie des champs locale avec particules compos\'ees,'' in \emph{Les probl\`emes math\'ematiques de la th\'eorie quantique des champs}, CNRS, Paris, 1959.
```

3. Item 3; source PDF 187 / printed 175; marker bib-4-3;
```tex
\bibitem{ch4-3} H.~Reeh and S.~Schlieder, ``Bemerkungen zur Unit\"ar\"aquivalenz von Lorentzinvarianten Feldern,'' \emph{Nuovo Cimento}, \textbf{22}, 1051 (1961).
```

4. Item 4; source PDF 187 / printed 175; marker bib-4-4;
```tex
\bibitem{ch4-4} J.~Dixmier, \emph{Les alg\`ebres des op\'erateurs dans l'espace hilbertien (alg\`ebres de von Neumann)}, Gauthier-Villars, Paris, 1957, p.~6.
```

5. Item 5; source PDF 187 / printed 175; marker bib-4-5;
```tex
\bibitem{ch4-5} R.~Jost, ``Properties of Wightman Functions,'' in \emph{Lectures on Field Theory and the Many-Body Problem}, E.~R.~Caianiello (ed.), Academic Press, New York, 1961.
```

6. Item 6; source PDF 187 / printed 175; marker bib-4-6-7;
```tex
\bibitem{ch4-6} D.~Ruelle, ``On the Asymptotic Condition in Quantum Field Theory,'' \emph{Helv. Phys. Acta}, \textbf{35}, 147 (1962), Appendix, and also
```

7. Item 7; source PDF 187 / printed 175; marker bib-4-6-7;
```tex
\bibitem{ch4-7} H.~J.~Borchers, ``On the Structure of the Algebra of Field Operators,'' \emph{Nuovo Cimento}, \textbf{24}, 214 (1962). The idea of the proof given here is due to R.~Jost.
```

8. Item 8; source PDF 187 / printed 175; marker bib-4-8;
```tex
\bibitem{ch4-8} G.~L\"uders, ``On the Equivalence of Invariance under Time Reversal and under Particle-Anti-Particle Conjugation for Relativistic Field Theories,'' \emph{Dansk. Mat. Fys. Medd.}, \textbf{28}, 5 (1954).
```

9. Item 9; source PDF 187 / printed 175; marker bib-4-9;
```tex
\bibitem{ch4-9} W.~Pauli, ``Exclusion Principle, Lorentz Group and Reflection of Space-Time and Charge,'' p.~30 in \emph{Niels Bohr and the Development of Physics}, W.~Pauli (ed.), Pergamon Press, New York, 1955.
```

10. Item 10; source PDF 188 / printed 176; marker bib-4-10-11;
```tex
\bibitem{ch4-10} R.~Jost, ``Eine Bemerkung zum CTP Theorem,'' \emph{Helv. Phys. Acta}, \textbf{30}, 409 (1957). This paper was the starting point for many of the applications given in the present chapter. The connection between \emph{PCT} invariance and weak local commutativity introduced here is further discussed in
```

11. Item 11; source PDF 188 / printed 176; marker bib-4-10-11;
```tex
\bibitem{ch4-11} F.~J.~Dyson, ``On the Connection of Weak Local Commutativity and Regularity of Wightman Functions,'' \emph{Phys. Rev.}, \textbf{110}, 579 (1958).
```

12. Item 12; source PDF 188 / printed 176; marker bib-4-12;
```tex
\bibitem{ch4-12} J.~Schwinger, ``On the Theory of Quantized Fields I,'' \emph{Phys. Rev.}, \textbf{82}, 914 (1951). However, readers of this paper did not generally recognize that it stated or proved the \emph{PCT} theorem. In the free field case considered by Pauli no operator products occur so the ``classical'' \emph{PCT} invariance he proved for the equations is the same as the full quantum mechanical \emph{PCT} invariance.
```

13. Item 13; source PDF 188 / printed 176; marker bib-4-13-14;
```tex
\bibitem{ch4-13} M.~Fierz, ``\"Uber die relativistische Theorie kr\"aftefreier Teilchen mit beliebigem Spin,'' \emph{Helv. Phys. Acta}, \textbf{12}, 3 (1939).
```

14. Item 14; source PDF 188 / printed 176; marker bib-4-13-14;
```tex
\bibitem{ch4-14} W.~Pauli, ``On the Connection between Spin and Statistics,'' \emph{Phys. Rev.}, \textbf{58}, 716 (1940).
```

15. Item 15; source PDF 188 / printed 176; marker bib-4-15-16;
```tex
\bibitem{ch4-15} G.~L\"uders and B.~Zumino, ``Connection between Spin and Statistics,'' \emph{Phys. Rev.}, \textbf{110}, 1450 (1958); and
```

16. Item 16; source PDF 188 / printed 176; marker bib-4-15-16;
```tex
\bibitem{ch4-16} N.~Burgoyne, ``On the Connection of Spin with Statistics,'' \emph{Nuovo Cimento}, \textbf{8}, 807 (1958). Our treatment here follows the latter.
```

17. Item 17; source PDF 188 / printed 176; marker bib-4-17;
```tex
\bibitem{ch4-17} G.~F.~Dell'Antonio, ``On the Connection of Spin with Statistics,'' \emph{Ann. Phys.}, \textbf{16}, 153 (1961).
```

18. Item 18; source PDF 188 / printed 176; marker bib-4-18;
```tex
\bibitem{ch4-18} G.~L\"uders, ``Vertauschungs\-relationen zwischen verschiedenen Feldern,'' \emph{Z. Naturforsch.}, \textbf{13a}, 254 (1958). L\"uders was the first to use systematically the vector space \(V\) described in the text. The notion of Klein transformation which is used by these authors was systematically used by O.~Klein in another context:
```

19. Item 19; source PDF 189 / printed 177; marker bib-4-19;
```tex
\bibitem{ch4-19} O.~Klein, ``Quelques remarques sur le traitement approximatif du probl\`eme des \'electrons dans un r\'eseau cristallin par la m\'ecanique quantique,'' \emph{J. Phys. Radium}, \textbf{9}, 1 (1938).
```

20. Item 19a.; source PDF 189 / printed 177; marker bib-4-19a;
```tex
\item[19a.] P.~Jordan and E.~Wigner, ``\"Uber das Paulische \"Aquivalenzverbot,'' \emph{Z. Physik.}, \textbf{47}, 631 (1928).
```

21. Item 20; source PDF 189 / printed 177; marker bib-4-20;
```tex
\bibitem{ch4-20} H.~Araki, ``Connection of Spin with Commutation Relations,'' \emph{J. Math. Phys.}, \textbf{2}, 267 (1961).
```

22. Item 21; source PDF 189 / printed 177; marker bib-4-21;
```tex
\bibitem{ch4-21} R.~Haag, ``On Quantum Field Theory,'' \emph{Dan. Mat. Fys. Medd.}, \textbf{29}, 12 (1955).
```

23. Item 22; source PDF 189 / printed 177; marker bib-4-22;
```tex
\bibitem{ch4-22} D.~Hall and A.~S.~Wightman, ``A Theorem on Invariant Analytic Functions with Applications to Relativistic Quantum Field Theory,'' \emph{Mat. Fys. Medd. Dan. Vid. Selsk.}, \textbf{31}, 5 (1957).
```

24. Item 23; source PDF 189 / printed 177; marker bib-4-23;
```tex
\bibitem{ch4-23} O.~W.~Greenberg, ``Haag's Theorem and Clothed Operators,'' \emph{Phys. Rev.}, \textbf{115}, 706 (1959).
```

25. Item 24; source PDF 189 / printed 177; marker bib-4-24;
```tex
\bibitem{ch4-24} P.~G.~Federbush and K.~A.~Johnson, ``The Uniqueness of the Two-Point Function,'' \emph{Phys. Rev.}, \textbf{120}, 1926 (1960).
```

26. Item 25; source PDF 189 / printed 177; marker bib-4-25;
```tex
\bibitem{ch4-25} H.~J.~Borchers, ``\"Uber die Mannig\-faltigkeit der inter\-polierenden Felder zu einer kausalen S-Matrix,'' \emph{Nuovo Cimento}, \textbf{15}, 784 (1960).
```

27. Item 26; source PDF 189 / printed 177; marker bib-4-26;
```tex
\bibitem{ch4-26} S.~Kamefuchi, L.~O'Raifeartaigh, and Abdus Salam, ``Change of Variables and Equivalence Theorems in Quantum Field Theories,'' \emph{Nucl. Phys.}, \textbf{28}, 529 (1961).
```

28. Item 27; source PDF 189 / printed 177; marker bib-4-27;
```tex
\bibitem{ch4-27} H.~Epstein, ``On the Borchers Class of a Free Field,'' \emph{Nuovo Cimento}, \textbf{27}, 886 (1963).
```

29. Item 28; source PDF 189 / printed 177; marker bib-4-28;
```tex
\bibitem{ch4-28} O.~W.~Greenberg and A.~Messiah, ``Are There Particles in Nature Other Than Bosons or Fermions?'' \emph{Phys. Rev.}, \textbf{136}, B248 (1964).
```

30. Item 29; source PDF 190 / printed 178; marker bib-4-29;
```tex
\bibitem{ch4-29} R.~Jost, \emph{General Theory of Quantized Fields (Lectures in Applied Mathematics IV: Proceedings of the Summer Seminar, Boulder, Colorado, 1960)}, American Math. Soc., Providence, R.I., 1965.
```

The audit specifically checked the CTP wording in item 10, item 19a exact Jordan-Wigner title and 1928 citation, item 28 page B248, and item 29 parenthetical publication details.

## Boundary and correction checks

- PDF 173 / printed 161 begins with the continuation of Example 3. Section 4-5 starts after that continuation, followed by (4-70).
- PDF 172 / printed 160 Eq. (4-69) retains (-1)^J and the stacked smallmatrix spin factor. The source field star is represented by the authorized native adjoint.
- PDF 180 / printed 168 Eq. (4-89) reads (Box_src + m^2) phi(x) = lambda phi(x)^3. Since the house metric has Box_house = -Box_src, the native equation is (-Box+m^2) varphi(x)=lambda varphi(x)^3.
- Section 4-1 source formulas use (x-y)^2<0 for spacelike separation under the source metric. The native edition now uses (x-y)^2>0, with the stronger initial condition converted from (x-y)^2<-a<0 to (x-y)^2>a>0.
- No figure artwork or figure hooks belong to Chapter 4 source pages 146-190.

## Verification evidence

- Source marker coverage script: every physical page 146-190 is represented by at least one Chapter 4 marker.
- Equation parser result: 101 tags, 101 unique identifiers, exact sequence (4-1), ..., (4-101).
- Result/object parser result: one theorem object for each identifier 4-1 through 4-22; no lemma or proposition object; three corollaries; three examples; six remarks; seven footnotes; 20 proof blocks.
- Bibliography parser result: items 1-29 and 19a, 30 entries, source ordered.
- Standalone compile: `TEXINPUTS=latex: pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/private/tmp/pct-ch4-harness /private/tmp/pct-ch4-harness.tex`, run twice; output `/private/tmp/pct-ch4-harness/pct-ch4-harness.pdf`, 39 pages.
- Render inspection: `pdftoppm -f 24 -l 25 -r 180 -jpeg /private/tmp/pct-ch4-harness/pct-ch4-harness.pdf /private/tmp/pct-ch4-render/page` and `pdftoppm -f 31 -l 31 -r 180 -jpeg /private/tmp/pct-ch4-harness/pct-ch4-harness.pdf /private/tmp/pct-ch4-render/page`; inspected `page-24.jpg`, `page-25.jpg`, and `page-31.jpg`.
- Page 24 shows the stacked factor in (4-69) and the start of Example 3. Page 25 shows the continuation before Section 4-5 and (4-70). Page 31 shows (4-89), (4-90), and (4-91) with the house-metric signs.

Build command: `TEXINPUTS=latex: pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/private/tmp/pct-ch4-harness /private/tmp/pct-ch4-harness.tex` (run twice for references).

Unresolved blockers: none
