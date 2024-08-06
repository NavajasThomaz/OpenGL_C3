from config import *
import mesh_factory


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

        self.shader = create_shader_program("shaders/vertex.txt", "shaders/fragment.txt")
        self.texture = create_texture(load_image("Cr_Staircase.jpg"))
        self.quad_vao, self.quad_vbo = mesh_factory.build_textured_quad()

    def run(self):
        """ Run the app """
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT)

            glUseProgram(self.shader)
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glBindVertexArray(self.quad_vao)
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