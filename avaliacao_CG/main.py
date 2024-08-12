import glfw  # Importa a biblioteca GLFW para criar janelas e gerenciar eventos
from OpenGL.GL import *  # Importa todas as funções da biblioteca OpenGL
import imgui  # Importa a biblioteca ImGui para criar interfaces gráficas
from imgui.integrations.glfw import GlfwRenderer  # Renderer de ImGui para GLFW
import numpy as np  # Biblioteca para manipulação de arrays
import glm  # Biblioteca para operações matemáticas de gráficos
import ctypes  # Biblioteca para interação com C/C++
from PIL import Image  # Biblioteca para manipulação de imagens


SCREEN_WIDTH = 1280  # Define a largura da tela
SCREEN_HEIGHT = 720  # Define a altura da tela

class StartScreen:
    def __init__(self):
        self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tela Inicial", None, None)# Cria uma janela GLFW
        glfw.make_context_current(self.window)  # Define o contexto OpenGL para a janela
        imgui.create_context()  # Cria um contexto ImGui
        self.impl = GlfwRenderer(self.window)  # Cria um renderer ImGui para GLFW
        self.start_game = False  # Flag para iniciar o jogo

    def show(self):
        """ Mostra a tela inicial e aguarda ação do usuário. """
        while not glfw.window_should_close(self.window):
            glfw.poll_events()  # Processa eventos de entrada
            self.impl.process_inputs()  # Processa entradas para ImGui

            imgui.new_frame()  # Inicia um novo frame ImGui
            imgui.begin("Bem-vindo!", closable=False)  # Cria uma janela ImGui
            if imgui.button("Iniciar"):  # Cria um botão e verifica se foi pressionado
                self.start_game = True  # Altera a flag para iniciar o jogo
                glfw.set_window_should_close(self.window, True)  # Fecha a janela
            imgui.end()  # Finaliza a janela ImGui

            imgui.render()  # Renderiza a interface ImGui
            self.impl.render(imgui.get_draw_data())  # Renderiza os dados do ImGui
            glfw.swap_buffers(self.window)  # Troca os buffers da janela

        self.impl.shutdown()  # Finaliza o renderer ImGui
        glfw.destroy_window(self.window)  # Destroi a janela GLFW

class OpenGLApp:
    def __init__(self):
        
        # Instancia a janela do glfw
        self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "C3_Logo", None, None)
        
        
        self.projecao = 0 # Tipo de projeção atual | 0 perspectiva, 1 ortogonal
        self.trans_values = [0.0, 0.0, 0.0] # Vetor de translação
        self.rot_values = [0.0, 0.0, 0.0] # Vetor de rotação
        self.scale_value = 0.0 # Coeficiente de escala
        self.usePhong = False
        self.useGouraud = False
        self.useRaster = False
        
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window can't be created!")

        glfw.make_context_current(self.window) # Define a janela atual como contexto
        glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED) # Desabilita o cursor
        
        # Set background color
        glClearColor(0.6, 0.7, 1.0, 1.0)

        # Enable depth testing
        glEnable(GL_DEPTH_TEST)

        # Compile the shaders
        self.shader = self.create_shader_program("shaders/vertex_shader.glsl", "shaders/fragment_shader.glsl")

        # Iluminação Phong
        self.usePhongLoc = glGetUniformLocation(self.shader, "usePhong")
        
        # Tonalização Gouraud
        self.useGouraudLoc = glGetUniformLocation(self.shader, "useGouraud")
        
        # Get uniform locations
        self.projection_loc = glGetUniformLocation(self.shader, "projection") # Localização da projeção
        self.view_loc = glGetUniformLocation(self.shader, "view") # Localização da view
        self.model_loc = glGetUniformLocation(self.shader, "model") # Localização da model

        # Camera settings
        self.camera_pos = glm.vec3(0.0, 1.0, 3.0) # Poisção inicial
        self.camera_front = glm.vec3(0.0, 0.0, -1.0) # Direção inicial
        self.camera_up = glm.vec3(0.0, 1.0, 0.0) # Direção inicial
        self.yaw = -90.0 # Rotação inicial
        self.pitch = 0.0 # Rotação inicial
        self.last_x = SCREEN_WIDTH/4  # Ultima posição x do mouse
        self.last_y = SCREEN_HEIGHT/4 # Ultima posição y do mouse
        
        glfw.set_cursor_pos_callback(self.window, self.mouse_callback)

        # Timing
        self.delta_time = 0.0
        self.last_frame = 0.0
        
        # Textura
        self.texture = self.create_texture("Textures/logoFurg.png")

    def create_cube(self):
        """Cria um cubo com textura."""
        vertices = [
            # x     y     z     u    v
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

        
        vao = glGenVertexArrays(1) # Vertex Array Object
        vbo = glGenBuffers(1) # Vertex Buffer Object
        

        glBindVertexArray(vao) # Vincula o vao
        glBindBuffer(GL_ARRAY_BUFFER, vbo) # Vincula o tipo de buffer
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW) # Envia os dados dos vértices para o buffer

        # Posição dos vértices
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5 * vertices.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        """
        Aponta para os valores de coordenadas
        vertices = [ x     y     z
                   -0.5, -0.5, -0.5,  0.0, 0.0,
                    0.5, -0.5, -0.5,  1.0, 0.0,
                    0.5,  0.5, -0.5,  1.0, 1.0,
                    ...
                   ]
        """
        
        # Coordenadas de textura
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 5 * vertices.itemsize, ctypes.c_void_p(3 * vertices.itemsize))
        glEnableVertexAttribArray(1)
        """
        Aponta para os valores de texturas
        vertices = [                    u    v
                   -0.5, -0.5, -0.5,  0.0, 0.0,
                    0.5, -0.5, -0.5,  1.0, 0.0,
                    0.5,  0.5, -0.5,  1.0, 1.0,
                    ...
                   ]
        """

        glBindVertexArray(0) # Desvincula o vao
        return vao, vbo

    def create_texture(self, texture_path):
        """ Cria uma textura OpenGL a partir de um objeto Image. """
        texture = glGenTextures(1)  # Gera um ID para uma nova textura
        glBindTexture(GL_TEXTURE_2D, texture)  # Vincula a textura como uma textura 2D

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
        glTexImage2D(GL_TEXTURE_2D,  # Define os dados da imagem para a textura
                    0, # 
                    GL_RGBA, # formato da textura
                    image.width, # largura
                    image.height, # altura
                    0, # 
                    GL_RGBA, #
                    GL_UNSIGNED_BYTE, 
                    img_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, 0)  # Desvincula a textura
        return texture # Retorna o ID da textura

    def create_shader_program(self, vertex_file_path, fragment_file_path):
        """ Compila e vincula um programa de shader a partir de arquivos de shader. """
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
        """ Compila um shader a partir do código fonte. """
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
        
        # Movimentação da camera
        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
            self.camera_pos += camera_speed * self.camera_front
        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
            self.camera_pos -= camera_speed * self.camera_front
        if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
            self.camera_pos -= glm.normalize(glm.cross(self.camera_front, self.camera_up)) * camera_speed
        if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
            self.camera_pos += glm.normalize(glm.cross(self.camera_front, self.camera_up)) * camera_speed
        if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
            self.camera_pos += camera_speed * self.camera_up
        if glfw.get_key(window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS:
            self.camera_pos -= camera_speed * self.camera_up
            
        # HUD
        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)
            
        # Muda as projeções
        if glfw.get_key(window, glfw.KEY_P) == glfw.PRESS:
            self.projecao = 0
        if glfw.get_key(window, glfw.KEY_O) == glfw.PRESS:
            self.projecao = 1
            
        # Translacao
        if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
            self.trans_values = [0.0, 0.0, -0.1]
        if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
            self.trans_values = [0.0, 0.0, 0.1]
        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            self.trans_values = [-0.1, 0.0, 0.0]
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:  
            self.trans_values = [0.1, 0.0, 0.0]
        if glfw.get_key(window, glfw.KEY_PAGE_UP) == glfw.PRESS:
            self.trans_values = [0.0, 0.1, 0.0]
        if glfw.get_key(window, glfw.KEY_PAGE_DOWN) == glfw.PRESS:
            self.trans_values = [0.0, -0.1, 0.0]
            
        # Rotaçao
        if glfw.get_key(window, glfw.KEY_LEFT_ALT) == glfw.PRESS:
            self.rot_values = [0.0, 0.0, 0.5]
        if glfw.get_key(window, glfw.KEY_RIGHT_ALT) == glfw.PRESS:
            self.rot_values = [0.0, 0.0, -0.5]
        if glfw.get_key(window, glfw.KEY_LEFT_CONTROL) == glfw.PRESS:
            self.rot_values = [0.0, 0.5, 0.0]
        if glfw.get_key(window, glfw.KEY_RIGHT_CONTROL) == glfw.PRESS:
            self.rot_values = [0.0, -0.5, 0.0]
        if glfw.get_key(window, glfw.KEY_PERIOD) == glfw.PRESS:
            self.rot_values = [0.5, 0.0, 0.0]
        if glfw.get_key(window, glfw.KEY_COMMA) == glfw.PRESS:
            self.rot_values = [-0.5, 0.0, 0.0]
            
        # Escala
        if glfw.get_key(window, glfw.KEY_0) == glfw.PRESS:
            self.scale_value = 1.1
        if glfw.get_key(window, glfw.KEY_9) == glfw.PRESS:
            self.scale_value = 0.9

        # Phong
        if glfw.get_key(window, glfw.KEY_L) == glfw.PRESS:
            self.toggle_phong()
            
        # Gouraud
        if glfw.get_key(window, glfw.KEY_G) == glfw.PRESS:
            self.toggle_gouraud()
            
    def perspectiva(self):
        projection = glm.perspective(glm.radians(90.0), SCREEN_WIDTH / SCREEN_HEIGHT, 0.1, 100.0)
        # Vincula o resultado da matriz de projeção a uma uniforme no shader
        glUniformMatrix4fv(self.projection_loc, 1, GL_FALSE, glm.value_ptr(projection))
        """glm.perspective
        
        fov = Campo de visão
        aspect = proporção de aspecto da tela
        n = Distancia do plano mais proximo
        f = Distancia do plano mais distante

        Primeira Coluna: Relacionada à escala horizontal e à proporção de aspecto.

            cot(fov/2) / aspect: Escala as coordenadas X para corresponder ao campo de visão e à proporção de aspecto.

        Segunda Coluna: Relacionada à escala vertical.

            cot(fov/2): Escala as coordenadas Y para corresponder ao campo de visão.

        Terceira Coluna: Responsável pela transformação de perspectiva e mapeamento de profundidade.

            -(f + n) / (f - n): Mapeia a coordenada Z para o intervalo [-1, 1], essencial para a renderização.
            -(2 * f * n) / (f - n): Aplica a transformação de perspectiva, fazendo com que objetos mais distantes tenham valores Z menores.

        Quarta Coluna: Usada para a divisão de perspectiva.

            -1: Garante que a coordenada W seja igual a -Z após a multiplicação da matriz. A divisão por W durante a renderização cria o efeito de perspectiva.

        |cot(fov/2) / aspect   0          0                      0|
        |0                     cot(fov/2) 0                      0|
        |0                     0         -(f + n) / (f - n)    -(2 * f * n) / (f - n)|
        |0                     0         -1                      0|

        """
    
    def ortogonal(self):
        projection = glm.ortho(-10.0, 10.0, -10.0, 10.0, -10.0, 10.0)
        # Vincula o resultado da matriz de projeção a uma uniforme no shader
        glUniformMatrix4fv(self.projection_loc, 1, GL_FALSE, glm.value_ptr(projection))
        """glm.ortho
        
        |2/(right-left)    0               0               -(right+left)/(right-left)|
        |0                 2/(top-bottom)  0               -(top+bottom)/(top-bottom)|
        |0                 0               -2/(far-near)   -(far+near)/(far-near)    |
        |0                 0               0               1                         |
        """
    
    def transladar(self, model, direcao_x, direcao_y, direcao_z):
        return glm.translate(model, glm.vec3(direcao_x, direcao_y, direcao_z))
        """ glm.translate
            Assumindo que o modelo esta como indetidade
            model=  |1 0 0 direcao_x|       |1 0 0 0|
                    |0 1 0 direcao_y|   *   |0 1 0 0|
                    |0 0 1 direcao_z|       |0 0 1 0|
                    |0 0 0 1|               |0 0 0 1|

        """

    def rotacionar(self, model, angle_x, angle_y, angle_z):
        # Aplica a rotação em cada eixo separadamente
        model = glm.rotate(model, glm.radians(angle_x), glm.vec3(1.0, 0.0, 0.0))
        model = glm.rotate(model, glm.radians(angle_y), glm.vec3(0.0, 1.0, 0.0))
        model = glm.rotate(model, glm.radians(angle_z), glm.vec3(0.0, 0.0, 1.0))
        return model
        """glm.rotate
            Rx = | 1  0       0       0 |
                 | 0  cos(x) -sin(x)  0 |
                 | 0  sin(x)  cos(x)  0 |
                 | 0  0       0       1 |

            Ry = | cos(y)  0  sin(y)  0 |
                 | 0       1  0       0 |
                 | -sin(y) 0  cos(y)  0 |
                 | 0       0  0       1 |
            
            Rz = | cos(z) -sin(z)  0  0 |
                 | sin(z)  cos(z)  0  0 |
                 | 0       0       1  0 |
                 | 0       0       0  1 |
        """
    
    def escalonar(self, model, escala):
        return glm.scale(model, glm.vec3(escala, escala, escala))
        """glm.scale
            S = | escala  0       0       0 |
                | 0       escala  0       0 |
                | 0       0       escala  0 |
                | 0       0       0       1 |
        """

    def toggle_phong(self):
        self.usePhong = not self.usePhong
        glUniform1i(self.usePhongLoc, self.usePhong)
    
    def toggle_gouraud(self):
        self.useGouraud = not self.useGouraud
    
    def toggle_raster(self):
        self.useRaster = not self.useRaster
    
    def run(self):
        self.cube_vao, self.cube_vbo = self.create_cube() # cria o vao e vbo do cubo
        model = glm.mat4(1.0)   
        """Matriz modelo identidade
            |1 0 0|
            |0 1 0|
            |0 0 1|
        """
        
        while not glfw.window_should_close(self.window):
            # atualização da tela
            current_frame = glfw.get_time()
            self.delta_time = current_frame - self.last_frame
            self.last_frame = current_frame

            self.process_input(self.window) # Processa os inputs

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # limpa o buffer de cor e profundidade

            glUseProgram(self.shader) # Vincula o programa de shader
            
            # Define a projeção
            if self.projecao == 0:
                self.perspectiva()
            else:
                self.ortogonal()
            
            if self.trans_values != [0.0, 0.0, 0.0]: # Verifica se tem input
                model = self.transladar(model, self.trans_values[0], self.trans_values[1], self.trans_values[2]) # Aplica translação com os valores do input
                self.trans_values = [0.0, 0.0, 0.0] # Limpa o input
            
            if self.rot_values != [0.0, 0.0, 0.0]: # Verifica se tem input
                model = self.rotacionar(model, self.rot_values[0], self.rot_values[1], self.rot_values[2]) # Aplica rotação com os valores do input
                self.rot_values = [0.0, 0.0, 0.0] # Limpa o input
                
            if self.scale_value != 0.0: # Verifica se tem input
                model = self.escalonar(model, self.scale_value) # Aplica escala com os valores do input
                self.scale_value = 0.0
            
            glUniform1i(self.usePhongLoc, self.usePhong) # Diz ao shader se deve usar Phong
            
            view = glm.lookAt(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)
            """glm.lookAt:
            c = camera position
            t = target position
            u = camera up vector
            f = normalize(t - c) 
            r = normalize(cross(f, u)) 
            up = cross(r, f) 

            | rx  ry  rz -dot(r, c) |
            | ux  uy  uz -dot(up, c) |
            | -fx -fy -fz  dot(f, c) |
            |  0   0   0      1      |
            """
            
            glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, glm.value_ptr(view)) #glm.value_ptr: usa ponteiro
            glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, glm.value_ptr(model))
            """glUniformMatrix4fv:
                Manda uma matrix 4x4 de floats pra uma variável uniforme do shader
                Vertex Shader recebe matrix 4x4 de floats do modelo e da view
            """
            
            
            glActiveTexture(GL_TEXTURE0) # Ativa o espaço da memoria GL_TEXTURE0
            glBindTexture(GL_TEXTURE_2D, self.texture) # Vincular textura
            glUniform1i(glGetUniformLocation(self.shader, "ourTexture"), 0) # Passa para o vertex shader o sampler2d

            glBindVertexArray(self.cube_vao) # Seleciona o vao do cubo
            glDrawArrays(GL_TRIANGLES, 0, 36)  # Desenha o cubo usando triangulos como forma primitiva | 0: index inicial, (36: numero de vertices)/3 = 12 triangulos.
            glBindVertexArray(0) # Deseleciona o vao do cubo

            glfw.swap_buffers(self.window)
            glfw.poll_events()

        glfw.terminate()

if __name__ == "__main__":
    if not glfw.init():
        raise Exception("GLFW não pode ser inicializado!")

    start_screen = StartScreen()
    start_screen.show()

    if start_screen.start_game:
        opengl_app = OpenGLApp()
        opengl_app.run()

    glfw.terminate()
