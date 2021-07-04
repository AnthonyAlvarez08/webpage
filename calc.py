class Polynomial:

    def __init__(self, degree : int, coefficients : list):
        self.degree = degree
        self.coeffs = coefficients
        self.eval, self.integral, self.derivative = Polynomial._polymaker(self.degree, self.coeffs)

    def area_under(self, a : float, b : float) -> float:
        return self.integral(b) - self.integral(a)

    def local_approximation(self, xo : int, x : float) -> float:
        # I do not know what I would use it for but aight
        return self.eval(xo) + (xo - x) * self.derivative(xo)

    def __str__(self) -> str:
        '''
        display a polynomial in ax^n + bx^(n-1) + ... + A1x + A0
        form
        '''
        res = ''
        for i in range(self.degree, -1, -1):
            if self.coeffs[len(self.coeffs) - i - 1] != 0:
                sign = ''
                if self.coeffs[len(self.coeffs) - i - 1] > 0:
                    sign = '+'
                else:
                    sign = '-'

                if abs(self.coeffs[len(self.coeffs) - i - 1]) == 1 and i != 0:
                    res += f'{sign}'
                else:
                    res += f'{sign}{abs(self.coeffs[len(self.coeffs) - i - 1])}'

                if i == 1:
                    res += 'x'
                elif i != 0:
                    res += f'x^{i}'

            
        res += '\n'
        return res

    @classmethod
    def _polymaker(cls, degree : int, coefficients : list):
        """
        degree: integer, degree of polynomial
        coefficients: list size degree + 1, list coefficients of polynomial
        if one wanted x^3 + 7x on would do [1, 0, 7, 0]

        returns a function evaluation of a polynomial, and its anti-derivative and derivative
        """
        coeffs = coefficients
        d = degree
        def func(x : float) -> float:
            total = 0
            exp = degree;
            for i in coeffs:
                total += x ** exp * i
                exp -= 1
            return total

        coeffs2 = coeffs
        coeffs3 = coeffs
        coeffs2.append(0)
        coeffs3.pop()

        def integral(x : float) -> float:
            total = 0
            exp = degree + 1;
            for i in coeffs2:
                try:
                    total += x ** exp * i / exp
                    exp -= 1
                except Exception:
                    total += 0
            return total

        def derivative(x : float) -> float:
            total = 0
            exp = degree - 1
            for i in coeffs3:
                if i != 0 and x != 0:
                    total += x ** exp * i * (exp + 1)
                exp -= 1
                
            return total
                
        return func, integral, derivative




# wah = Polynomial(3, [1, 0, 0, 5])
# print(wah.eval(3), wah.derivative(3), wah.integral(3))