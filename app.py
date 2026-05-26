from flask import Flask, render_template, request

app = Flask(__name__)


def doolittle_lu_with_steps(matrix):
    """
    Executes LU Decomposition using the Doolittle Method
    and records step-by-step calculations.
    """

    n = len(matrix)

    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    U = [[0.0 for j in range(n)] for i in range(n)]

    steps = []

    for i in range(n):

        # COMPUTE U MATRIX

        steps.append(f"--- Computing Row {i+1} of Upper Matrix U ---")

        for k in range(i, n):

            terms = [
                f"(L_{{{i+1}{j+1}}} \\times U_{{{j+1}{k+1}}})"
                for j in range(i)
            ]

            terms_calc = [
                L[i][j] * U[j][k]
                for j in range(i)
            ]

            total_sum = sum(terms_calc)

            U[i][k] = matrix[i][k] - total_sum

            if i == 0:

                steps.append(
                    f"\\( u_{{{i+1}{k+1}}} = "
                    f"a_{{{i+1}{k+1}}} = "
                    f"{matrix[i][k]} \\)"
                )

            else:

                formula_str = " + ".join(terms)

                calc_str = " + ".join([
                    f"({L[i][j]:.2f} \\times {U[j][k]:.2f})"
                    for j in range(i)
                ])

                steps.append(
                    f"\\( u_{{{i+1}{k+1}}} = "
                    f"a_{{{i+1}{k+1}}} - "
                    f"({formula_str}) = "
                    f"{matrix[i][k]} - "
                    f"({calc_str}) = "
                    f"{U[i][k]:.2f} \\)"
                )

        # COMPUTE L MATRIX

        if i < n - 1:
            steps.append(
                f"--- Computing Column {i+1} of Lower Matrix L ---"
            )

        for k in range(i + 1, n):

            terms = [
                f"(L_{{{k+1}{j+1}}} \\times U_{{{j+1}{i+1}}})"
                for j in range(i)
            ]

            terms_calc = [
                L[k][j] * U[j][i]
                for j in range(i)
            ]

            total_sum = sum(terms_calc)

            if U[i][i] == 0.0:
                raise ValueError(
                    "Division by zero encountered! "
                    "This matrix cannot be decomposed "
                    "using Doolittle Method."
                )

            L[k][i] = (
                (matrix[k][i] - total_sum)
                / U[i][i]
            )

            if i == 0:

                steps.append(
                    f"\\( l_{{{k+1}{i+1}}} = "
                    f"\\frac{{a_{{{k+1}{i+1}}}}}"
                    f"{{u_{{{i+1}{i+1}}}}} = "
                    f"\\frac{{{matrix[k][i]}}}"
                    f"{{{U[i][i]}}} = "
                    f"{L[k][i]:.2f} \\)"
                )

            else:

                formula_str = " + ".join(terms)

                calc_str = " + ".join([
                    f"({L[k][j]:.2f} \\times {U[j][i]:.2f})"
                    for j in range(i)
                ])

                steps.append(
                    f"\\( l_{{{k+1}{i+1}}} = "
                    f"\\frac{{a_{{{k+1}{i+1}}} - "
                    f"({formula_str})}}"
                    f"{{u_{{{i+1}{i+1}}}}} = "
                    f"\\frac{{{matrix[k][i]} - "
                    f"({calc_str})}}"
                    f"{{{U[i][i]:.2f}}} = "
                    f"{L[k][i]:.2f} \\)"
                )

    return L, U, steps


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None
    matrix_input = None
    steps = None

    if request.method == "POST":

        try:

            raw_matrix = [
                [
                    float(request.form[f'cell_{i}_{j}'])
                    for j in range(3)
                ]
                for i in range(3)
            ]

            matrix_input = raw_matrix

            L, U, calculated_steps = doolittle_lu_with_steps(raw_matrix)

            result = {
                'L': L,
                'U': U
            }

            steps = calculated_steps

        except ValueError as ve:

            error = str(ve)

        except Exception:

            error = (
                "Invalid matrix data! "
                "Please enter valid numerical values."
            )

    return render_template(
        'index.html',
        result=result,
        error=error,
        matrix_input=matrix_input,
        steps=steps
    )


if __name__ == '__main__':
    app.run(debug=True)