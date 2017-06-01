/* Oryginalny problem ze współczynnikami wektora c ustawionymi na 1
Maximize
obj:  Aq + As + Av + Bq + Bt + Cr + Cs + Cu + Dq + Dt + Dw + Er + Ew + Fr + Fu + Fv + Gs + Gw

Subject To
Aq + As + Av = 1
Bq + Bt = 1
Cr + Cs + Cu = 1
Dq + Dt + Dw = 1
Er + Ew = 1
Fr + Fu + Fv = 1
Gs + Gw = 1
Aq + Bq + Dq = 1
Cr + Er + Fr = 1
As + Cs + Gs = 1
Bt + Dt = 1
Cu + Fu = 1
Av + Fv = 1
Dw + Ew + Gw = 1

Bounds

0 <= Aq
0 <= As
0 <= Av
0 <= Bq
0 <= Bt
0 <= Cr
0 <= Cs
0 <= Cu
0 <= Dq
0 <= Dt
0 <= Dw
0 <= Er
0 <= Ew
0 <= Fr
0 <= Fu
0 <= Fv
0 <= Gs
0 <= Gw

Generals
Aq
As
Av
Bq
Bt
Cr
Cs
Cu
Dq
Dt
Dw
Er
Ew
Fr
Fu
Fv
Gs
Gw
End

*/

/*Zapisując macierz A mamy (puste pola to zera):
  Aq   As   Av   Bq   Bt   Cr   Cs   Cu   Dq   Dt   Dw   Er   Ew   Fr   Fu   Fv   Gs   Gw
A| 1    1    1                                                                            |
B|                1    1                                                                  |
C|                          1    1    1                                                   |
D|                                         1    1    1                                    |
E|                                                        1    1                          |
F|                                                                  1    1    1           |
G|                                                                                 1    1 |
q| 1              1                        1                                              |
r|                          1                             1         1                     |
s|      1                        1                                                        |
t|                     1                        1                                         |
u|                                    1                                  1                |
v|           1                                                                1           |
w|                                                   1         1                        1 |

i wstawijając do wzoru w^T * A >= c, rozwiązując problem dualny otrzymujemy:
*/
#do wklejenia do GLPK
#http://hgourvest.github.io/glpk.js/

Minimize
obj: A + B + C + D + E + F + G + q + r + s + t + u + v + w

Subject To
A + q >= 1
A + s >= 1
A + v >= 1
B + q >= 1
B + t >= 1
C + r >= 1
C + s >= 1
C + u >= 1
D + q >= 1
D + t >= 1
D + w >= 1
E + r >= 1
E + w >= 1
F + r >= 1
F + u >= 1
F + v >= 1
G + s >= 1
G + w >= 1

Bounds

Generals
A
B
C
D
E
F
G
q
r
s
t
u
v
w
End
