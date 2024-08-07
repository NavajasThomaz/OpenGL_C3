from config import *
import mesh_factory


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
    """ Retorna a matriz de rotação de 'angle' graus em torno do eixo (x, y, z). """
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
    """ Retorna a matriz de escala para os valores x, y e z. """
    return np.array([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)


class App:
    def __init__(self):
        """ Initialise the program """
        self.initialize_glfw()
        self.initialize_opengl()


    def initialize_glfw(self):
        """ Initialize all glfw related stuff. Make a window, basically. """
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
        """ Initialize any opengl related stuff. """
        glClearColor(0.1, 0.2, 0.2, 1)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_DEPTH_TEST)


        self.shader = create_shader_program("shaders/vertex.txt", "shaders/fragment.txt")
        self.texture = create_texture(load_image("Cr_Staircase.jpg"))
        self.quad_vao, self.quad_vbo = mesh_factory.build_textured_quad()

    def run(self):
        """ Run the app """
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            # Limpa o buffer de cor e o buffer de profundidade
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glUseProgram(self.shader)
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glBindVertexArray(self.quad_vao)

            # Desenha o primeiro quadrado (transladado para trás)
            model = np.identity(4, dtype=np.float32)
            model = translate(model, 0, 0, -0.5)
            glUniformMatrix4fv(glGetUniformLocation(self.shader, "model"), 1, GL_FALSE, model)
            glDrawArrays(GL_TRIANGLES, 0, 6)

            # Desenha o segundo quadrado (na posição original)
            model = np.identity(4, dtype=np.float32)
            glUniformMatrix4fv(glGetUniformLocation(self.shader, "model"), 1, GL_FALSE, model)
            glDrawArrays(GL_TRIANGLES, 0, 6)

            glBindVertexArray(0)
            glBindTexture(GL_TEXTURE_2D, 0)
            glUseProgram(0)

            glfw.swap_buffers(self.window)

    def quit(self):
        """ Cleanup the app, run exit code """
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
