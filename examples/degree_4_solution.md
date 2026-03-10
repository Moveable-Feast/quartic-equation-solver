

---
Solve:
$$
x^{4}-10x^{3}+35x^{2}-50x+24 = 0
$$
Coefficients:
$$
\begin{cases}
    a = 1 \\
    b = -10 \\
    c = 35 \\
    d = -50 \\
    e = 24
\end{cases}
$$
Parameters:
$$
\begin{cases}
    \alpha = -\dfrac{3b^2}{8a^2} + \dfrac{c}{a} = -2.5 \\
    \beta = \dfrac{b^3}{8a^3} - \dfrac{bc}{2a^2} + \dfrac{d}{a} = 0 \\
    \gamma = -\dfrac{3b^4}{256a^4} + \dfrac{b^2c}{16a^3} - \dfrac{bd}{4a^2} + \dfrac{e}{a} = 0.5625 \\
    P = -\dfrac{\alpha^2}{12} - \gamma = -1.0833 \\
    Q = -\dfrac{a^3}{108} + \dfrac{\alpha\gamma}{3} - \dfrac{\beta^2}{8} = -0.3241 \\
    R = -\dfrac{Q}{2} \pm \sqrt{\dfrac{Q^2}{4} + \dfrac{P^3}{27}} = 0.162+0.1443i \\
    U = \sqrt[3]{R} = 0.5833+0.1443i \\
    y = -\dfrac{5}{6}\alpha +
    \begin{cases}
        -\sqrt[3]{Q}, U = 0 \\
        U - \dfrac{P}{3U}, U \neq 0
    \end{cases}
    = 3.25
\end{cases}
$$
Solutions:

$$
\begin{cases}
    x_1 = -\dfrac{b}{4a} + \sqrt{\dfrac{-\alpha + \sqrt{\alpha^2 - 4\gamma}}{2}} = 4 \\
    x_2 = -\dfrac{b}{4a} + \sqrt{\dfrac{-\alpha - \sqrt{\alpha^2 - 4\gamma}}{2}} = 3 \\
    x_3 = -\dfrac{b}{4a} - \sqrt{\dfrac{-\alpha + \sqrt{\alpha^2 - 4\gamma}}{2}} = 1 \\
    x_4 = -\dfrac{b}{4a} - \sqrt{\dfrac{-\alpha - \sqrt{\alpha^2 - 4\gamma}}{2}} = 2
\end{cases}
$$



---
Solve:
$$
(1+i)x^{4}+(-10-i)x^{3}+(35+i)x^{2}+(-50-i)x+(24+i) = 0
$$
Coefficients:
$$
\begin{cases}
    a = 1+i \\
    b = -10-i \\
    c = 35+i \\
    d = -50-i \\
    e = 24+i
\end{cases}
$$
Parameters:
$$
\begin{cases}
    \alpha = -\dfrac{3b^2}{8a^2} + \dfrac{c}{a} = 14.25+1.5625i \\
    \beta = \dfrac{b^3}{8a^3} - \dfrac{bc}{2a^2} + \dfrac{d}{a} = 6.7188-23.0938i \\
    \gamma = -\dfrac{3b^4}{256a^4} + \dfrac{b^2c}{16a^3} - \dfrac{bd}{4a^2} + \dfrac{e}{a} = -8.8018-3.8359i \\
    P = -\dfrac{\alpha^2}{12} - \gamma = -7.9167+0.125i \\
    Q = -\dfrac{a^3}{108} + \dfrac{\alpha\gamma}{3} - \dfrac{\beta^2}{8} = -4.6146+7.2072i \\
    R = -\dfrac{Q}{2} \pm \sqrt{\dfrac{Q^2}{4} + \dfrac{P^3}{27}} = 3.7904-8.9163i \\
    U = \sqrt[3]{R} = 1.9721-0.8097i \\
    y = -\dfrac{5}{6}\alpha +
    \begin{cases}
        -\sqrt[3]{Q}, U = 0 \\
        U - \dfrac{P}{3U}, U \neq 0
    \end{cases}
    = -8.7504-1.6597i
\end{cases}
$$
Solutions:

$$
\begin{cases}
    x_1 = -\dfrac{b}{4a} + \dfrac{\sqrt{\alpha + 2y} + \sqrt{-(3\alpha + 2y + \dfrac{2\beta}{\sqrt{\alpha + 2y}})}}{2} = 1.6901-5.6023i \\
    x_2 = -\dfrac{b}{4a} + \dfrac{\sqrt{\alpha + 2y} - \sqrt{-(3\alpha + 2y + \dfrac{2\beta}{\sqrt{\alpha + 2y}})}}{2} = 1.5313+1.4887i \\
    x_3 = -\dfrac{b}{4a} + \dfrac{-\sqrt{\alpha + 2y} + \sqrt{-(3\alpha + 2y - \dfrac{2\beta}{\sqrt{\alpha + 2y}})}}{2} = 1.3325-0.5057i \\
    x_4 = -\dfrac{b}{4a} + \dfrac{-\sqrt{\alpha + 2y} - \sqrt{-(3\alpha + 2y - \dfrac{2\beta}{\sqrt{\alpha + 2y}})}}{2} = 0.9461+0.1193i
\end{cases}
$$


where
$$
i = \sqrt{-1}.
$$
