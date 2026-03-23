def __init__(self, filas, columnas):
    # Constructor de la clase Matriz
    # filas: número de filas (n)
    # columnas: número de columnas (k)
    # datos: lista 2D que almacena los elementos de la matriz
    self.n = filas
    self.k = columnas
    self.datos = [[0.0 for _ in range(columnas)] for _ in range(filas)]

def ingresar_datos(self):
    # Método para ingresar los elementos de la matriz desde consola
    # Solicita al usuario cada elemento fila por fila
    print(f"Ingrese los elementos de la matriz {self.n}x{self.k}:")
    for i in range(self.n):
        for j in range(self.k):
            while True:
                try:
                    valor = float(input(f"Elemento [{i+1},{j+1}]: "))
                    self.datos[i][j] = valor
                    break
                except ValueError:
                    print("Error: Ingrese un número real válido")

def mostrar(self, nombre="Matriz"):
    # Método para mostrar la matriz en formato legible
    print(f"{nombre} {self.n}x{self.k}:")
    for i in range(self.n):
        fila_str = " ".join([f"{self.datos[i][j]:10.6f}" for j in range(self.k)])
        print(f"[{fila_str}]")

def copiar(self):
    # Método para crear una copia profunda de la matriz
    copia = Matriz(self.n, self.k)
    for i in range(self.n):
        for j in range(self.k):
            copia.datos[i][j] = self.datos[i][j]
    return copia

def transponer(self):
    # Método para calcular la matriz transpuesta
    # Retorna una nueva matriz de dimensiones k x n
    transpuesta = Matriz(self.k, self.n)
    for i in range(self.n):
        for j in range(self.k):
            transpuesta.datos[j][i] = self.datos[i][j]
    return transpuesta

def multiplicar(self, otra_matriz):
    # Método para multiplicar esta matriz por otra matriz
    # Verifica que las dimensiones sean compatibles
    if self.k != otra_matriz.n:
        raise ValueError("Dimensiones incompatibles para multiplicación")

    resultado = Matriz(self.n, otra_matriz.k)
    for i in range(self.n):
        for j in range(otra_matriz.k):
            suma = 0.0
            for l in range(self.k):
                suma += self.datos[i][l] * otra_matriz.datos[l][j]
            resultado.datos[i][j] = suma
    return resultado

def es_cuadrada(self):
    # Método para verificar si la matriz es cuadrada
    return self.n == self.k

def es_simetrica(self):
    # Método para verificar si la matriz es simétrica
    # Solo aplicable a matrices cuadradas
    if not self.es_cuadrada():
        return False

    for i in range(self.n):
        for j in range(i+1, self.n):
            if abs(self.datos[i][j] - self.datos[j][i]) > 1e-10:
                return False
    return True

def norma_frobenius(self):
    # Método para calcular la norma de Frobenius de la matriz
    suma = 0.0
    for i in range(self.n):
        for j in range(self.k):
            suma += self.datos[i][j] ** 2
    return math.sqrt(suma)

@staticmethod
def gram_schmidt(matriz):
    # Método estático que implementa el proceso de Gram-Schmidt
    # para descomponer una matriz A en Q*R
    # A: matriz de dimensiones m x n (m >= n para tener columnas linealmente independientes)

    m = matriz.n
    n = matriz.k

    # Inicializar matrices Q y R
    Q = Matriz(m, n)
    R = Matriz(n, n)

    # Copiar columnas de A
    columnas_A = []
    for j in range(n):
        columna = [matriz.datos[i][j] for i in range(m)]
        columnas_A.append(columna)

    # Proceso de Gram-Schmidt
    for j in range(n):
        # Tomar la columna j de A
        v = columnas_A[j][:]

        # Restar las proyecciones sobre las columnas anteriores de Q
        for i in range(j):
            # Calcular producto punto entre v y columna i de Q
            producto_punto = 0.0
            for k in range(m):
                producto_punto += v[k] * Q.datos[k][i]

            # Almacenar en R
            R.datos[i][j] = producto_punto

            # Restar la proyección
            for k in range(m):
                v[k] -= producto_punto * Q.datos[k][i]

        # Calcular norma del vector residual
        norma_v = math.sqrt(sum(x*x for x in v))

        # Si la norma es casi cero, la columna es linealmente dependiente
        if norma_v < 1e-10:
            # Hacerla ortogonal arbitrariamente
            for k in range(m):
                Q.datos[k][j] = 1.0 if k == j else 0.0
            R.datos[j][j] = 0.0
        else:
            # Normalizar y almacenar en Q
            for k in range(m):
                Q.datos[k][j] = v[k] / norma_v
            R.datos[j][j] = norma_v

    return Q, R

@staticmethod
def algoritmo_qr(matriz, max_iter=1000, tol=1e-10):
    # Método estático que implementa el algoritmo QR para diagonalizar
    # una matriz simétrica (encontrar sus autovalores)
    # Retorna una lista de autovalores aproximados

    if not matriz.es_cuadrada():
        raise ValueError("El algoritmo QR requiere una matriz cuadrada")

    if not matriz.es_simetrica():
        print("Advertencia: La matriz no es simétrica, resultados pueden ser inexactos")

    # Crear copia de trabajo de la matriz
    A_k = matriz.copiar()

    # Historial para convergencia
    historial_diagonal = []

    for iteracion in range(max_iter):
        # Descomposición QR de A_k
        Q, R = QRDescomposicion.gram_schmidt(A_k)

        # Calcular A_{k+1} = R * Q
        A_k = R.multiplicar(Q)

        # Extraer diagonal (aproximación de autovalores)
        diagonal = [A_k.datos[i][i] for i in range(A_k.n)]
        historial_diagonal.append(diagonal)

        # Verificar convergencia (elementos fuera de la diagonal cercanos a cero)
    # The following block of code was duplicated and had an undeclared `autovalores` variable.
    # It has been removed.
    # A_k = matriz.copiar()

    # Historial para convergencia
    # historial_diagonal = []

    # for iteracion in range(max_iter):
    #     # Descomposición QR de A_k
    #     Q, R = QRDescomposicion.gram_schmidt(A_k)

    #     # Calcular A_{k+1} = R * Q
    #     A_k = R.multiplicar(Q)

    #     # Extraer diagonal (aproximación de autovalores)
    #     diagonal = [A_k.datos[i][i] for i in range(A_k.n)]
    #     historial_diagonal.append(diagonal)

    #     # Verificar convergencia (elementos fuera de la diagonal cercanos a cero)
    # autovalores.sort(reverse=True)

    # This line was also causing an error because `autovalores` was not defined.
    # It has been removed. You might need to add a return statement here if autovalores
    # is intended to be the final result of this method.
    # return autovalores

    # To ensure the algorithm works and returns something meaningful, let's assume
    # that the autovalores should be derived from the last `A_k`'s diagonal.
    autovalores = [A_k.datos[i][i] for i in range(A_k.n)]
    # Consider a convergence check and early exit if eigenvalues converge.
    # For simplicity and to fix the immediate error, we proceed with sorting.
    autovalores.sort(reverse=True) # Assuming 'autovalores' should be sorted before returning.

    # TODO: Implement a proper convergence check to break the loop earlier
    # For example:
    # if iteracion > 0:
    #     max_diff = 0.0
    #     for i in range(A_k.n):
    #         for j in range(A_k.n):
    #             if i != j:
    #                 max_diff = max(max_diff, abs(A_k.datos[i][j]))
    #     if max_diff < tol:
    #         break

    return autovalores

@staticmethod
def matriz_a_autovalores(matriz):
    # Método wrapper que aplica el algoritmo QR a una matriz
    # Retorna los autovalores ordenados
    return QRDescomposicion.algoritmo_qr(matriz)
def __init__(self, matriz_A):
    # Constructor de la clase SVDQRCalculador
    # matriz_A: objeto de la clase Matriz (n x k)
    self.A = matriz_A
    self.valores_singulares = []
    self.autovalores_ATA = []

def calcular_valores_singulares_qr(self):

    # Método principal que calcula los valores singulares usando QR
    # Elige diagonalizar la matriz más pequeña entre A^T*A y A*A^T

    print("Calculando valores singulares usando algoritmo QR...")

    # Determinar qué matriz es más pequeña para mayor eficiencia
    n = self.A.n
    k = self.A.k

    if k <= n:
        # Usar A^T*A (k x k) - más pequeña
        print(f"Diagonalizando A^T*A ({k}x{k}) usando algoritmo QR...")
        A_transpuesta = self.A.transponer()
        ATA = A_transpuesta.multiplicar(self.A)

        # Verificar que ATA es simétrica
        if not ATA.es_simetrica():
            print("Advertencia: A^T*A no es exactamente simétrica por errores numéricos")

        # Aplicar algoritmo QR para encontrar autovalores de A^T*A
        # Ensure QRDescomposicion is defined in the global scope or imported if it's a class.
        # Assuming it's the class in the current scope.
        self.autovalores_ATA = QRDescomposicion.algoritmo_qr(ATA)

    else:
        # Usar A*A^T (n x n) - más pequeña
        print(f"Diagonalizando A*A^T ({n}x{n}) usando algoritmo QR...")
        A_transpuesta = self.A.transponer()
        AAT = self.A.multiplicar(A_transpuesta)

        # Aplicar algoritmo QR para encontrar autovalores de A*A^T
        # Ensure QRDescomposicion is defined in the global scope or imported if it's a class.
        autovalores_AAT = QRDescomposicion.algoritmo_qr(AAT)

        # Los autovalores no nulos de A*A^T son los mismos que los de A^T*A
        self.autovalores_ATA = autovalores_AAT
    # Calcular valores singulares como raíces cuadradas de autovalores positivos
    print("Calculando valores singulares como sqrt(λ)...")
    self.valores_singulares = []

    for autovalor in self.autovalores_ATA:
        if autovalor > 1e-10:  # Filtrar valores numéricamente no negativos
            valor_singular = math.sqrt(abs(autovalor))
            self.valores_singulares.append(valor_singular)

    # Ordenar de mayor a menor (convención SVD)
    self.valores_singulares.sort(reverse=True)

    # Mostrar información
    print(f"\nAutovalores de A^T*A encontrados: {len(self.autovalores_ATA)}")
    for i, λ in enumerate(self.autovalores_ATA):
        print(f"  λ{i+1} = {λ:.10f}")
    # The following block of code was duplicated.
    # It has been removed.
    # Calcular valores singulares como raíces cuadradas de autovalores positivos
    # print("Calculando valores singulares como sqrt(λ)...")
    # self.valores_singulares = []

    # for autovalor in self.autovalores_ATA:
    #     if autovalor > 1e-10:  # Filtrar valores numéricamente no negativos
    #         valor_singular = math.sqrt(abs(autovalor))
    #         self.valores_singulares.append(valor_singular)

    # Ordenar de mayor a menor (convención SVD)
    # self.valores_singulares.sort(reverse=True)

    # Mostrar información
    # print(f"\nAutovalores de A^T*A encontrados: {len(self.autovalores_ATA)}")
    # for i, λ in enumerate(self.autovalores_ATA):
    #     print(f"  λ{i+1} = {λ:.10f}")
    for i, sigma in enumerate(self.valores_singulares):
        print(f"  σ{i+1} = {sigma:.10f}")

    # Calcular norma de Frobenius de A y verificar propiedad
    if self.valores_singulares:
        norma_A = self.A.norma_frobenius()
        suma_sq_sigma = sum(sigma*sigma for sigma in self.valores_singulares)

        print(f"\nVerificación de propiedades:")
        print(f"  Norma de Frobenius de A: {norma_A:.10f}")
        print(f"  Suma de σ_i^2: {suma_sq_sigma:.10f}")
        print(f"  Diferencia: {abs(norma_A*norma_A - suma_sq_sigma):.2e}")
    
    # Need to return the singular values
    return self.valores_singulares

def mostrar_resultados(self):
    # This method was missing, so I'm adding a basic implementation.
    # You might want to enhance it based on what you want to display.
    print("\n" + "=" * 70)
    print("RESULTADOS DEL CÁLCULO DE VALORES SINGULARES")
    print("=" * 70)
    print("Valores Singulares:")
    if self.valores_singulares:
        for i, sigma in enumerate(self.valores_singulares):
            print(f"  σ{i+1} = {sigma:.10f}")
    else:
        print("  No se encontraron valores singulares.")

def verificar_con_numpy(self):
    # Método para verificación con numpy (solo referencia)
    try:
        # Ensure numpy is imported
        import numpy as np
        
        A_np = self.A.to_numpy() if hasattr(self.A, 'to_numpy') else np.array(self.A.datos)
        U, S, Vt = np.linalg.svd(A_np, full_matrices=False)

        print("\n" + "=" * 70)
        print("VERIFICACIÓN CON NUMPY.LINALG.SVD")
        print("=" * 70)

        print("\nValores singulares (NumPy):")
        for i, s in enumerate(S):
            print(f"  σ{i+1} = {s:.10f}")

        return S
    except ImportError:
        print("\nNumPy no está instalado. Por favor, instálelo para usar la verificación: pip install numpy")
        return None
    except Exception as e:
        print(f"\nNo se pudo realizar verificación con NumPy: {e}")
        return None

# Main execution block (if this is intended to be run directly)
# To run this code, you'd typically define the Matriz class first
# and then proceed with this part.

# Before running the main block, ensure `Matriz` class is fully defined.
# For example, if Matriz is defined in the same cell:

# You might need to import math if not already imported
import math

# Define the Matriz class (assuming it's defined earlier in this cell)
class Matriz:
    def __init__(self, filas, columnas):
        self.n = filas
        self.k = columnas
        self.datos = [[0.0 for _ in range(columnas)] for _ in range(filas)]

    def ingresar_datos(self):
        print(f"Ingrese los elementos de la matriz {self.n}x{self.k}:")
        for i in range(self.n):
            for j in range(self.k):
                while True:
                    try:
                        valor = float(input(f"Elemento [{i+1},{j+1}]: "))
                        self.datos[i][j] = valor
                        break
                    except ValueError:
                        print("Error: Ingrese un número real válido")

    def mostrar(self, nombre="Matriz"):
        print(f"{nombre} {self.n}x{self.k}:")
        for i in range(self.n):
            fila_str = " ".join([f"{self.datos[i][j]:10.6f}" for j in range(self.k)])
            print(f"[{fila_str}]")

    def copiar(self):
        copia = Matriz(self.n, self.k)
        for i in range(self.n):
            for j in range(self.k):
                copia.datos[i][j] = self.datos[i][j]
        return copia

    def transponer(self):
        transpuesta = Matriz(self.k, self.n)
        for i in range(self.n):
            for j in range(self.k):
                transpuesta.datos[j][i] = self.datos[i][j]
        return transpuesta

    def multiplicar(self, otra_matriz):
        if self.k != otra_matriz.n:
            raise ValueError("Dimensiones incompatibles para multiplicación")
        resultado = Matriz(self.n, otra_matriz.k)
        for i in range(self.n):
            for j in range(otra_matriz.k):
                suma = 0.0
                for l in range(self.k):
                    suma += self.datos[i][l] * otra_matriz.datos[l][j]
                resultado.datos[i][j] = suma
        return resultado

    def es_cuadrada(self):
        return self.n == self.k

    def es_simetrica(self):
        if not self.es_cuadrada():
            return False
        for i in range(self.n):
            for j in range(i+1, self.n):
                if abs(self.datos[i][j] - self.datos[j][i]) > 1e-10:
                    return False
        return True

    def norma_frobenius(self):
        suma = 0.0
        for i in range(self.n):
            for j in range(self.k):
                suma += self.datos[i][j] ** 2
        return math.sqrt(suma)


class QRDescomposicion:
    @staticmethod
    def gram_schmidt(matriz):
        m = matriz.n
        n = matriz.k
        Q = Matriz(m, n)
        R = Matriz(n, n)
        columnas_A = []
        for j in range(n):
            columna = [matriz.datos[i][j] for i in range(m)]
            columnas_A.append(columna)

        for j in range(n):
            v = columnas_A[j][:]
            for i in range(j):
                producto_punto = 0.0
                for k in range(m):
                    producto_punto += v[k] * Q.datos[k][i]
                R.datos[i][j] = producto_punto
                for k in range(m):
                    v[k] -= producto_punto * Q.datos[k][i]

            norma_v = math.sqrt(sum(x*x for x in v))
            if norma_v < 1e-10:
                for k in range(m):
                    Q.datos[k][j] = 1.0 if k == j else 0.0
                R.datos[j][j] = 0.0
            else:
                for k in range(m):
                    Q.datos[k][j] = v[k] / norma_v
                R.datos[j][j] = norma_v
        return Q, R

    @staticmethod
    def algoritmo_qr(matriz, max_iter=1000, tol=1e-10):
        if not matriz.es_cuadrada():
            raise ValueError("El algoritmo QR requiere una matriz cuadrada")
        if not matriz.es_simetrica():
            print("Advertencia: La matriz no es simétrica, resultados pueden ser inexactos")

        A_k = matriz.copiar()
        historial_diagonal = []

        for iteracion in range(max_iter):
            Q, R = QRDescomposicion.gram_schmidt(A_k)
            A_k = R.multiplicar(Q)
            diagonal = [A_k.datos[i][i] for i in range(A_k.n)]
            historial_diagonal.append(diagonal)

            # Simple convergence check: if off-diagonal elements are small enough
            # (You may want a more robust check)
            if iteracion > 0:
                max_off_diagonal = 0.0
                for i in range(A_k.n):
                    for j in range(A_k.n):
                        if i != j:
                            max_off_diagonal = max(max_off_diagonal, abs(A_k.datos[i][j]))
                if max_off_diagonal < tol:
                    break

        autovalores = [A_k.datos[i][i] for i in range(A_k.n)]
        autovalores.sort(reverse=True)
        return autovalores

    @staticmethod
    def matriz_a_autovalores(matriz):
        return QRDescomposicion.algoritmo_qr(matriz)


class SVDQRCalculador:
    def __init__(self, matriz_A):
        self.A = matriz_A
        self.valores_singulares = []
        self.autovalores_ATA = []

    def calcular_valores_singulares_qr(self):
        print("Calculando valores singulares usando algoritmo QR...")
        n = self.A.n
        k = self.A.k

        if k <= n:
            print(f"Diagonalizando A^T*A ({k}x{k}) usando algoritmo QR...")
            A_transpuesta = self.A.transponer()
            ATA = A_transpuesta.multiplicar(self.A)
            if not ATA.es_simetrica():
                print("Advertencia: A^T*A no es exactamente simétrica por errores numéricos")
            self.autovalores_ATA = QRDescomposicion.algoritmo_qr(ATA)
        else:
            print(f"Diagonalizando A*A^T ({n}x{n}) usando algoritmo QR...")
            A_transpuesta = self.A.transponer()
            AAT = self.A.multiplicar(A_transpuesta)
            autovalores_AAT = QRDescomposicion.algoritmo_qr(AAT)
            self.autovalores_ATA = autovalores_AAT

        print("Calculando valores singulares como sqrt(λ)...")
        self.valores_singulares = []
        for autovalor in self.autovalores_ATA:
            if autovalor > 1e-10:
                valor_singular = math.sqrt(abs(autovalor))
                self.valores_singulares.append(valor_singular)
        self.valores_singulares.sort(reverse=True)

        print(f"\nAutovalores de A^T*A encontrados: {len(self.autovalores_ATA)}")
        for i, λ in enumerate(self.autovalores_ATA):
            print(f"  λ{i+1} = {λ:.10f}")
        for i, sigma in enumerate(self.valores_singulares):
            print(f"  σ{i+1} = {sigma:.10f}")

        if self.valores_singulares:
            norma_A = self.A.norma_frobenius()
            suma_sq_sigma = sum(sigma*sigma for sigma in self.valores_singulares)
            print(f"\nVerificación de propiedades:")
            print(f"  Norma de Frobenius de A: {norma_A:.10f}")
            print(f"  Suma de σ_i^2: {suma_sq_sigma:.10f}")
            print(f"  Diferencia: {abs(norma_A*norma_A - suma_sq_sigma):.2e}")

        return self.valores_singulares

    def mostrar_resultados(self):
        print("\n" + "=" * 70)
        print("RESULTADOS DEL CÁLCULO DE VALORES SINGULARES")
        print("=" * 70)
        print("Valores Singulares:")
        if self.valores_singulares:
            for i, sigma in enumerate(self.valores_singulares):
                print(f"  σ{i+1} = {sigma:.10f}")
        else:
            print("  No se encontraron valores singulares.")

    def verificar_con_numpy(self):
        try:
            import numpy as np
            A_np = self.A.to_numpy() if hasattr(self.A, 'to_numpy') else np.array(self.A.datos)
            U, S, Vt = np.linalg.svd(A_np, full_matrices=False)

            print("\n" + "=" * 70)
            print("VERIFICACIÓN CON NUMPY.LINALG.SVD")
            print("=" * 70)

            print("\nValores singulares (NumPy):")
            for i, s in enumerate(S):
                print(f"  σ{i+1} = {s:.10f}")
            return S
        except ImportError:
            print("\nNumPy no está instalado. Por favor, instálelo para usar la verificación: pip install numpy")
            return None
        except Exception as e:
            print(f"\nNo se pudo realizar verificación con NumPy: {e}")
            return None


print("=" * 70)
print("CÁLCULO DE VALORES SINGULARES USANDO ALGORITMO QR")
print("=" * 70)
# Solicitar dimensiones
print("\nIngrese las dimensiones de la matriz A (n x k)")
print("Requisito: n, k <= 10")

while True:
    try:
        n = int(input("Número de filas (n): "))
        k = int(input("Número de columnas (k): "))

        if n <= 0 or k <= 0:
            print("Error: Dimensiones deben ser positivas")
            continue

        if n > 10 or k > 10:
            print("Error: Dimensiones deben ser <= 10")
            continue

        break
    except ValueError:
        print("Error: Ingrese números enteros válidos")

# Crear e ingresar matriz
A = Matriz(n, k)
A.ingresar_datos()

print("\nMatriz ingresada:")
A.mostrar("A")

# Calcular valores singulares con algoritmo QR
print("\n" + "=" * 70)
print("PROCESANDO CON ALGORITMO QR...")
print("=" * 70)
try:
    # Crear calculador SVD con QR
    calculador = SVDQRCalculador(A)

    # Calcular valores singulares
    valores_singulares = calculador.calcular_valores_singulares_qr()

    # Mostrar resultados
    calculador.mostrar_resultados()

    # Opción de verificación
    print("\n" + "-" * 70)
    verificar = input("¿Desea verificar con NumPy? (s/n): ").lower()
    if verificar == 's':
        calculador.verificar_con_numpy()

except Exception as e:
    print(f"\nError durante el cálculo: {str(e)}")
    import traceback
    traceback.print_exc()
print("\n" + "=" * 70)
print("PROGRAMA FINALIZADO")
print("=" * 70)
