import numpy as np
from OpenGL.GL import *

# Função que implementa o algoritmo de Bresenham para rasterizar uma linha


# Função que configura o VAO e VBO para a linha
def setup_line(line_points):
    """Configura o VAO e VBO para a linha"""
    line_vertices = []  # Lista que armazenará os vértices da linha
    for x, y in line_points:
        # Convertendo coordenadas de pixels para coordenadas normalizadas OpenGL
        x_normalized = (x / 640) * 2 - 1  # Normaliza a coordenada x
        y_normalized = (y / 480) * 2 - 1  # Normaliza a coordenada y
        line_vertices.append(x_normalized)  # Adiciona a coordenada x normalizada à lista de vértices
        line_vertices.append(y_normalized)  # Adiciona a coordenada y normalizada à lista de vértices
        line_vertices.append(0.0)  # Adiciona a coordenada z (0.0) à lista de vértices (2D)

    line_vertices = np.array(line_vertices, dtype=np.float32)  # Converte a lista de vértices para um array NumPy

    vao = glGenVertexArrays(1)  # Gera um VAO 
    vbo = glGenBuffers(1)  # Gera um VBO 

    glBindVertexArray(vao)  # Liga o VAO
    glBindBuffer(GL_ARRAY_BUFFER, vbo)  # Liga o VBO
    glBufferData(GL_ARRAY_BUFFER, line_vertices.nbytes, line_vertices, GL_STATIC_DRAW)  # Envia os dados dos vértices para o buffer

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))  # Define o formato dos dados dos vértices
    glEnableVertexAttribArray(0)  # Habilita o atributo de vértice no índice 0

    glBindBuffer(GL_ARRAY_BUFFER, 0)  # Desliga o VBO
    glBindVertexArray(0)  # Desliga o VAO

    return vao, vbo  # Retorna o VAO e o VBO configurados
