import glfw
from OpenGL.GL import *
import imgui
from imgui.integrations.glfw import GlfwRenderer
import numpy as np
import glm
import ctypes
from pywavefront import Wavefront
from PIL import Image

# Constantes (ajuste conforme necessário)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def create_texture(image):
    """ Cria uma textura OpenGL a partir de um objeto Image. """
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image.tobytes())
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glBindTexture(GL_TEXTURE_2D, 0)
    return texture

def load_image(filepath):
    """ Carrega uma imagem e retorna como um objeto Image. """
    return Image.open(filepath).convert('RGBA')

class StartScreen:
    def __init__(self):
        self.window = glfw.create_window(640, 480, "Tela Inicial", None, None)
        glfw.make_context_current(self.window)
        imgui.create_context()
        self.impl = GlfwRenderer(self.window)
        self.start_game = False

    def show(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            self.impl.process_inputs()

            imgui.new_frame()
            imgui.begin("Bem-vindo!", closable=False)
            if imgui.button("Iniciar"):
                self.start_game = True
                glfw.set_window_should_close(self.window, True)
            imgui.end()

            imgui.render()
            self.impl.render(imgui.get_draw_data())
            glfw.swap_buffers(self.window)

        self.impl.shutdown()
        glfw.destroy_window(self.window)

class OpenGLApp:
    def __init__(self):
        # Create the window
        self.window = glfw.create_window(800, 600, "OpenGL Window", None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window can't be created!")

        glfw.make_context_current(self.window)
        glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED)

        # Set background color
        glClearColor(0.1, 0.2, 0.3, 1.0)

        # Enable depth testing
        glEnable(GL_DEPTH_TEST)

        # Load the model
        self.vertices, self.indices = self.load_model("models/Stiege-a.obj")

        # Compile the shaders
        self.shader = self.create_shader_program("shaders/vertex_shader.glsl", "shaders/fragment_shader.glsl")

        # Create the VAO after loading shaders and getting uniforms
        self.vao = self.create_vao(self.vertices, self.indices)

        # Get uniform locations
        self.projection_loc = glGetUniformLocation(self.shader, "projection")
        self.view_loc = glGetUniformLocation(self.shader, "view")
        self.model_loc = glGetUniformLocation(self.shader, "model")

        # Camera settings
        self.camera_pos = glm.vec3(0.0, 0.0, 3.0)
        self.camera_front = glm.vec3(0.0, 0.0, -1.0)
        self.camera_up = glm.vec3(0.0, 1.0, 0.0)
        self.yaw = -90.0
        self.pitch = 0.0
        self.last_x = 400
        self.last_y = 300
        glfw.set_cursor_pos_callback(self.window, self.mouse_callback)

        # Timing
        self.delta_time = 0.0
        self.last_frame = 0.0
        
        # Textura
        self.texture = self.create_texture("Textures/folhas.jpg")

    def create_cube(self):
        """Cria um cubo com textura."""
        vertices = [
            -0.5, -0.5, -0.5,  0.0, 0.0,
             0.5, -0.5, -0.5,  1.0, 0.0,
             0.5,  0.5, -0.5,  1.0, 1.0,
             0.5,  0.5, -0.5,  1.0, 1.0,
            -0.5,  0.5, -0.5,  0.0, 1.0,
            -0.5, -0.5, -0.5,  0.0, 0.0,

            -0.5, -0.5,  0.5,  0.0, 0.0,
             0.5, -0.5,  0.5,  1.0, 0.0,
             0.5,  0.5,  0.5,  1.0, 1.0,
             0.5,  0.5,  0.5,  1.0, 1.0,
            -0.5,  0.5,  0.5,  0.0, 1.0,
            -0.5, -0.5,  0.5,  0.0, 0.0,

            -0.5,  0.5,  0.5,  1.0, 0.0,
            -0.5,  0.5, -0.5,  1.0, 1.0,
            -0.5, -0.5, -0.5,  0.0, 1.0,
            -0.5, -0.5, -0.5,  0.0, 1.0,
            -0.5, -0.5,  0.5,  0.0, 0.0,
            -0.5,  0.5,  0.5,  1.0, 0.0,

             0.5,  0.5,  0.5,  1.0, 0.0,
             0.5,  0.5, -0.5,  1.0, 1.0,
             0.5, -0.5, -0.5,  0.0, 1.0,
             0.5, -0.5, -0.5,  0.0, 1.0,
             0.5, -0.5,  0.5,  0.0, 0.0,
             0.5,  0.5,  0.5,  1.0, 0.0,

            -0.5, -0.5, -0.5,  0.0, 1.0,
             0.5, -0.5, -0.5,  1.0, 1.0,
             0.5, -0.5,  0.5,  1.0, 0.0,
             0.5, -0.5,  0.5,  1.0, 0.0,
            -0.5, -0.5,  0.5,  0.0, 0.0,
            -0.5, -0.5, -0.5,  0.0, 1.0,

            -0.5,  0.5, -0.5,  0.0, 1.0,
             0.5,  0.5, -0.5,  1.0, 1.0,
             0.5,  0.5,  0.5,  1.0, 0.0,
             0.5,  0.5,  0.5,  1.0, 0.0,
            -0.5,  0.5,  0.5,  0.0, 0.0,
            -0.5,  0.5, -0.5,  0.0, 1.0
        ]
        vertices = np.array(vertices, dtype=np.float32)

        vao = glGenVertexArrays(1)
        vbo = glGenBuffers(1)

        glBindVertexArray(vao)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        # Posição dos vértices
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5 * vertices.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        # Coordenadas de textura
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 5 * vertices.itemsize, ctypes.c_void_p(3 * vertices.itemsize))
        glEnableVertexAttribArray(1)

        glBindVertexArray(0)
        return vao, vbo

    def load_model(self, file_path):
        """Loads a .obj model using PyWavefront."""
        scene = Wavefront(file_path, collect_faces=True, create_materials=True)

        vertices = []
        indices = []

        for mesh in scene.meshes.values():
            for face in mesh.faces:
                for vertex_index in face:
                    vertices.append(scene.vertices[vertex_index])
                indices.append(face)

        print(f"Loaded {len(vertices)} vertices and {len(indices)} indices.")
        return np.array(vertices, dtype='f4'), np.array(indices, dtype='uint32')

    def create_vao(self, vertices, indices):
        vao = glGenVertexArrays(1)
        vbo = glGenBuffers(1)
        ebo = glGenBuffers(1)

        glBindVertexArray(vao)

        # VBO for vertices
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        # EBO for indices
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        # Vertex Position Attribute
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * vertices.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # Unbind the VAO (good practice)
        glBindVertexArray(0)

        return vao

    def create_shader_program(self, vertex_file_path, fragment_file_path):
        vertex_shader = self.compile_shader(open(vertex_file_path).read(), GL_VERTEX_SHADER)
        fragment_shader = self.compile_shader(open(fragment_file_path).read(), GL_FRAGMENT_SHADER)
        shader_program = glCreateProgram()
        glAttachShader(shader_program, vertex_shader)
        glAttachShader(shader_program, fragment_shader)
        glLinkProgram(shader_program)

        # Check for program linking errors
        if glGetProgramiv(shader_program, GL_LINK_STATUS) != GL_TRUE:
            raise Exception(f"Shader program linking failed: {glGetProgramInfoLog(shader_program).decode()}")

        # Delete individual shaders (no longer needed after linking)
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

        return shader_program

    def compile_shader(self, source, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)

        # Check for compilation errors
        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise Exception(f"Shader compilation failed: {glGetShaderInfoLog(shader).decode()}")

        return shader

    def mouse_callback(self, window, xpos, ypos):
        xoffset = xpos - self.last_x
        yoffset = self.last_y - ypos 
        self.last_x = xpos
        self.last_y = ypos

        sensitivity = 0.1 
        xoffset *= sensitivity
        yoffset *= sensitivity

        self.yaw += xoffset
        self.pitch += yoffset

        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0

        front = glm.vec3()
        front.x = glm.cos(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        front.y = glm.sin(glm.radians(self.pitch))
        front.z = glm.sin(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        self.camera_front = glm.normalize(front)

    def process_input(self, window):
        camera_speed = 2.5 * self.delta_time
        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
            self.camera_pos += camera_speed * self.camera_front
        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
            self.camera_pos -= camera_speed * self.camera_front
        if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
            self.camera_pos -= glm.normalize(glm.cross(self.camera_front, self.camera_up)) * camera_speed
        if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
            self.camera_pos += glm.normalize(glm.cross(self.camera_front, self.camera_up)) * camera_speed
        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)
        # Move a câmera para cima (tecla Espaço)
        if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
            self.camera_pos += camera_speed * self.camera_up
        # Move a câmera para baixo (tecla Shift Esquerdo)
        if glfw.get_key(window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS:
            self.camera_pos -= camera_speed * self.camera_up

    def run(self):
        
        self.cube_vao, self.cube_vbo = self.create_cube()
        
        while not glfw.window_should_close(self.window):
            current_frame = glfw.get_time()
            self.delta_time = current_frame - self.last_frame
            self.last_frame = current_frame

            self.process_input(self.window)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glUseProgram(self.shader)

            projection = glm.perspective(glm.radians(45.0), 800 / 600, 0.1, 100.0)
            view = glm.lookAt(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)
            model = glm.mat4(1.0)  # Matriz modelo identidade

            glUniformMatrix4fv(self.projection_loc, 1, GL_FALSE, glm.value_ptr(projection))
            glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, glm.value_ptr(view))
            glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, glm.value_ptr(model))
            
            # Vincular textura
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glUniform1i(glGetUniformLocation(self.shader, "ourTexture"), 0)

            glBindVertexArray(self.cube_vao)
            glDrawArrays(GL_TRIANGLES, 0, 36)  # Desenha o cubo usando índices
            glBindVertexArray(0)

            glfw.swap_buffers(self.window)
            glfw.poll_events()

        glfw.terminate()

    def create_texture(self, texture_path):
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)

        # Define parâmetros de wrapping da textura
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        # Define parâmetros de filtragem da textura
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Carrega a imagem
        image = Image.open(texture_path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, 0)
        return texture

if __name__ == "__main__":
    if not glfw.init():
        raise Exception("GLFW não pode ser inicializado!")

    start_screen = StartScreen()
    start_screen.show()

    if start_screen.start_game:
        opengl_app = OpenGLApp()
        opengl_app.run()

    glfw.terminate()
