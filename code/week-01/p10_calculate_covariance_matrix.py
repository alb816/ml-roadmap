"""
deep-ml #10 Calculate Covariance Matrix (Easy, Statistics)
Суть: построить матрицу ковариации.
Статус: сдана 22-09-26.
"""


import numpy as np



def cov(x: np.ndarray, y: np.ndarray) -> float:
    """Вычисляет ковариацию между двумя векторами."""
	
    # Центрируем векторы (вычитаем математическое ожидание)
    x_centered = x - np.mean(x)
    y_centered = y - np.mean(y)

    # Находим ковариацию через среднее произведение центрированных значений
    covariance = np.dot(x_centered, y_centered) / (len(x) - 1)

    return covariance


def covariance_matrix_iterative(vectors: np.ndarray) -> np.ndarray:
    """Вычисляет ковариационную матрицу с использованием циклов (покомпонентно)."""
    n_feats = len(vectors)
    cov_matrix = np.zeros((n_feats, n_feats))
                                                                                                    
    for i in range(n_feats):                                # Векторизованная реализация:
        for j in range(n_feats):                            # Xc = X - X.mean(axis=1, keepdims=True)      # (k, n) минус средние по строкам
            cov_matrix[i, j] = cov(vectors[i], vectors[j])  # cov_matrix = Xc @ Xc.T / (X.shape[1] - 1)   # произведения центрированных строк
                                             
    return cov_matrix


if __name__ == "__main__":
    # Тестовый набор данных
    A = np.array(
        [
            [1, -1, -1, -1],
            [-1, 1, 1, 1],
            [-1, 1, 1, 1],
            [-1, 1, 1, 1],
        ],
        dtype=float,
    )


    # Тест 1: Итеративный подход
    res_iterative = covariance_matrix_iterative(A)
    print("\n1. Результат итеративного метода (через циклы for):")
    print(res_iterative)

    # Тест 2: Проверка эталоном NumPy
    res_numpy = np.cov(A)
    print("\n2. Эталонный результат библиотеки NumPy (np.cov):")
    print(res_numpy)
