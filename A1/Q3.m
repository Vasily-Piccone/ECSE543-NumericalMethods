% Run question 3b for the CG method
% This A matrix was obtained by multiplying A*A^T, were A is the matrix
% defining the finite difference method used in this problem.
A = [18  -8   1   0   0  -8   2   0   0   0   1     0  0  0  0  0  0  0 0;
 -8  19  -8   1   0   2  -8   2   0   0   0   1   0   0   0   0   0   0 0;
 1  -8  19  -8   1   0   2  -8   2   0   0   0   1   0   0   0   0   0  0;
 0   1  -8  22 -12   0   0   2  -8   3   0   0   0   1   0   0   0   0  0;
 0   0   1 -12  18   0   0   0   3  -8   0   0   0   0   1   0   0   0  0;
 -8   2   0   0   0  19  -8   1   0   0  -8   2   0   0   0   1   0   0 0;
 2  -8   2   0   0  -8  20  -8   1   0   2  -8   2   0   0   0   1    0 0;
 0   2  -8   2   0   1  -8  20  -8   1   0   2  -8   2   0   0   0   0  0;
 0   0   2  -8   3   0   1  -8  23 -12   0   0   2  -8   3   0   0   0  0;
 0   0   0   3  -8   0   0   1 -12  19   0   0   0   3  -8   0   0   0  0;
 1   0   0   0   0  -8   2   0   0   0  19  -8   1   0   0  -8   2   1  0;
 0   1   0   0   0   2  -8   2   0   0  -8  20  -8   1   0   2  -8   0  1;
 0   0   1   0   0   0   2  -8   2   0   1  -8  19  -8   1   0   1   0  0;
 0   0   0   1   0   0   0   2  -8   3   0   1  -8  22 -12   0   0   0  0;
 0   0   0   0   1   0   0   0   3  -8   0   0   1 -12  18   0   0   0  0;
 0   0   0   0   0   1   0   0   0   0  -8   2   0   0   0  22  -8 -12  3;
 0   0   0   0   0   0   1   0   0   0   2  -8   1   0   0  -8  22   3 -12;
 0   0   0   0   0   0   0   0   0   0   1   0   0   0   0 -12   3  18 -8;
 0   0   0   0   0   0   0   0   0   0   0   1   0   0   0   3 -12  -8 18];

b = [0 0 0 0 0 0 0 -15 -15 -15 0 -30 45 15 45  -15 30  -15 45]';
x_guess = zeros(19, 1);

[sol, norm2, normInf] = CG_new(A, b, x_guess);
x1 = 1:19;

plot(x1, norm2, 'LineWidth', 2.0) 
title('2-norm and \infty-norm vs. no. iterations')
xlabel('no. iterations')
hold on 
plot(x1, normInf, 'LineWidth', 2.0)
legend('2-norm','\infty-norm ')
hold off