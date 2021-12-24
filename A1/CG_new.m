function [x, two_norm, inf_norm] = CG_new(A, b, x_guess)
    numNodes = 19;
    % define the vectors into which you will store data
    two_norm = zeros(numNodes, 1);
    inf_norm = zeros(numNodes, 1);
    
    % set-up of initial parameters
    x = x_guess;
    r = b - A*x; % residual vector
    p = r;
    
    for i=1:numNodes 
            % alpha term
            a_n = p'*r;
            a_d = p'*A*p;
            alpha = a_n/a_d
            
            % update x
            x = x + alpha*p;
            
            % update r
            r = b - A*x;
            
            % calculate the two-norm and inf-norm
            two_norm(i) = norm(r,2);
            inf_norm(i) = norm(r, Inf);
            
            % beta term
            b_n = -1*p'*A*r;
            b_d = p'*A*p;
            beta = b_n/b_d;
            
            % update p
            p = r + beta*p;
    end
end

