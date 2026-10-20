| № | Категория/Название | Статус | Вывод |
|---|---|---|---|
| 202 | Jacobian Matrix Calculation | сдана | приближение производных через (f_incr - f_base) / h |
| 214 | Chain Rule for Composite Functions | сдана | для реализации нужен прямой или лучше - обратный проход |
| 215, 219, 220 | сalculus | сданы | - |
| 309 | calculus | сдана | умножение многочленов происходит через свертку convolve, чтобы обеспечить сохраниение позиций коэффициентов производной |
| 221 | Newton's Method for Optimization | сдана | метод является более эффективным в сравнении с градиентным спуском, учитывая дополнительно информацию о кривизне |
| 218 | Compute the Hessian Matrix | сдана | вторые производные скалярной функции . Диагональ - 3 точки, смешанные - 4 точки. Пары j>i считаются один раз и зеркалятся по Шварцу |
|314 |Lagrange Multipliers for Constrained Quadratic Optimization | сдана |условия Qx + c = λa, a.T x = b -> линейная система 3×3; lambda = ф'(b), проверено: ф(b) = b^2/2 |
|310   |Taylor Series Approximation   | сдана  | рекуррентный член: exp — t·x/(i+1); sin — −t·x^2/((2i+2)(2i+3)); cos — −t·x^2/((2i+1)(2i+2))  |
|313   |Numerical Gradient Checking   | сдана  |  центрированная разность (f(x + eps * e_i) - f(x - eps * e_i))/(2eps) имеет точность O(eps^2) против O(eps) у односторонней  |
| 311| Classify Critical Points Using Hessian Eigenvalues | сдана |eigvalsh для симметричной матрицы; условие |lamdba| ≤ tol проверяется раньше знаков |
