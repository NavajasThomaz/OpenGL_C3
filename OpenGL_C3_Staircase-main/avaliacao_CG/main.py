from config import *
import mesh_factory
import numpy as np
import os
from OpenGL.GL import *
import glfw

# Função auxiliar para translação
def translate(matrix, x, y, z):
    translation = np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ], dtype=np.float32)
    return np.dot(translation, matrix)

def rotate(angle, x, y, z):
    angle = np.radians(angle)
    c = np.cos(angle)
    s = np.sin(angle)
    norm = np.sqrt(x * x + y * y + z * z)
    x /= norm
    y /= norm
    z /= norm
    return np.array([
        [x * x * (1 - c) + c, x * y * (1 - c) - z * s, x * z * (1 - c) + y * s, 0],
        [y * x * (1 - c) + z * s, y * y * (1 - c) + c, y * z * (1 - c) - x * s, 0],
        [x * z * (1 - c) - y * s, y * z * (1 - c) + x * s, z * z * (1 - c) + c, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)

def scale(x, y, z):
    return np.array([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)

def perspective(fov, aspect, near, far):
    f = 1.0 / np.tan(np.radians(fov) / 2)
    return np.array([
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
        [0, 0, -1, 0]
    ], dtype=np.float32)

def orthogonal(left, right, bottom, top, near, far):
    return np.array([
        [2 / (right - left), 0, 0, -(right + left) / (right - left)],
        [0, 2 / (top - bottom), 0, -(top + bottom) / (top - bottom)],
        [0, 0, -2 / (far - near), -(far + near) / (far - near)],
        [0, 0, 0, 1]
    ], dtype=np.float32)

class App:
    def __init__(self):
        self.initialize_glfw()
        self.initialize_opengl()

        vertex_shader_path = "/Users/denisevaleriavelardemamani/Downloads/OpenGL_C3_Staircase-main/avaliacao_CG/shaders/vertex.txt"
        fragment_shader_path = "/Users/denisevaleriavelardemamani/Downloads/OpenGL_C3_Staircase-main/avaliacao_CG/shaders/fragment.txt"
        self.shader = create_shader_program(vertex_shader_path, fragment_shader_path)

        image_path = "/Users/denisevaleriavelardemamani/Downloads/OpenGL_C3_Staircase-main/Cr_Staircase.jpg"
        self.texture = create_texture(load_image(image_path))

        self.quad_vao, self.quad_vbo = mesh_factory.build_textured_quad()

        # Matriz de projeção perspectiva
        self.projection = perspective(45, SCREEN_WIDTH / SCREEN_HEIGHT, 0.1, 100)
        self.view = np.identity(4, dtype=np.float32)  # Você pode ajustar a matriz de visualização conforme necessário

    def initialize_glfw(self):
        if not glfw.init():
            raise Exception("GLFW can't be initialized")

        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_PROFILE, GLFW_CONSTANTS.GLFW_OPENGL_CORE_PROFILE)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)

        self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "OpenGL with Textures", None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window can't be created")

        glfw.make_context_current(self.window)

    def initialize_opengl(self):
        glClearColor(0.1, 0.2, 0.2, 1)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_DEPTH_TEST)

    def run(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glUseProgram(self.shader)
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glBindVertexArray(self.quad_vao)

            projection_location = glGetUniformLocation(self.shader, "projection")
            view_location = glGetUniformLocation(self.shader, "view")
            glUniformMatrix4fv(projection_location, 1, GL_FALSE, self.projection)
            glUniformMatrix4fv(view_location, 1, GL_FALSE, self.view)

            # Desenha o primeiro quadrado (transladado para trás)
            model = np.identity(4, dtype=np.float32)
            model = translate(model, 0, 0, -5)
            model_location = glGetUniformLocation(self.shader, "model")
            glUniformMatrix4fv(model_location, 1, GL_FALSE, model)
            glDrawArrays(GL_TRIANGLES, 0, 6)

            # Desenha o segundo quadrado (na posição original)
            model = np.identity(4, dtype=np.float32)
            glUniformMatrix4fv(model_location, 1, GL_FALSE, model)
            glDrawArrays(GL_TRIANGLES, 0, 6)

            glBindVertexArray(0)
            glBindTexture(GL_TEXTURE_2D, 0)
            glUseProgram(0)

            glfw.swap_buffers(self.window)

    def quit(self):
        glDeleteVertexArrays(1, [self.quad_vao])
        glDeleteBuffers(1, [self.quad_vbo])
        glDeleteTextures(1, [self.texture])
        glDeleteProgram(self.shader)
        glfw.destroy_window(self.window)
        glfw.terminate()

if __name__ == "__main__":
    my_app = App()
    my_app.run()
    my_app.quit()
