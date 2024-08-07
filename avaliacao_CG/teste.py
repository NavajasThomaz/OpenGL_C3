# Importa as bibliotecas necessárias
import glm  # Importa a biblioteca glm para operações com matrizes
from config import *  # Importa as configurações do projeto
from OpenGL.GL import *  # Importa as funções OpenGL
from OpenGL.GL.shaders import compileProgram, compileShader  # Importa funções para compilar shaders
import mesh_factory  # Importa funções para criar meshes
# Cria a classe App que representa a aplicação
class App:
    def __init__(self):
        # Inicializa as variáveis para armazenar a posição do mouse
        self.mouse_x = 0
        self.mouse_y = 0
        # Inicializa a biblioteca GLFW
        if not glfw.init():
            return
        # Cria a janela da aplicação
        self.window = glfw.create_window(640, 480, "Hello Word", None, None)
        # Verifica se a janela foi criada com sucesso
        if not self.window:
            glfw.terminate()
            return
        # Define a janela como contexto atual
        glfw.make_context_current(self.window)
        # Define a cor de fundo da janela
        glClearColor(0.1, 0.2, 0.2, 1)
        # Habilita o blending para permitir transparência
        glEnable(GL_BLEND)
        # Define a função de blending
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        # Habilita o teste de profundidade para evitar que objetos mais distantes sejam desenhados por cima de objetos mais próximos
        glEnable(GL_DEPTH_TEST)
        # Cria o programa de shaders
        self.shader = create_shader_program("shaders/vertex.txt", "shaders/fragment.txt")
        # Carrega a textura da imagem
        self.texture = create_texture(load_image("Cr_Staircase.jpg"))
        # Cria o quad texturizado
        self.quad_vao, self.quad_vbo = mesh_factory.build_textured_quad()
    # Define a função de callback para eventos de teclado
    def key_position(self, a, b, c, d, e):
        print(a, b, c, d, e)
        # Define a função de callback para eventos de mouse
    def mouse_position(self, win, x, y):
        # Atualiza a posição do mouse
        self.mouse_x = x
        self.mouse_y = y
        # Imprime a posição do mouse no console
        print(win, x, y)
    # Define a função para multiplicar a matriz de modelo atual pela matriz fornecida
    def glMultMatrix(self, matrix_ptr):
        # Obtém a matriz de modelo atual
        current_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        # Converte o ponteiro para array NumPy
        matrix = np.frombuffer(matrix_ptr, dtype=np.float32)
        # Multiplica as matrizes usando NumPy, redimensionando antes
        result_matrix = np.dot(matrix_ptr.reshape(4, 4), current_matrix)
        # Carrega a matriz resultante no OpenGL
        glLoadMatrixf(result_matrix)
    # Define a função para executar a aplicação
    def run(self):
        # Loop principal da aplicação
        while not glfw.window_should_close(self.window):
            # Define as funções de callback para eventos de teclado e mouse
            glfw.set_cursor_pos_callback(self.window, self.mouse_position)
            glfw.set_key_callback(self.window, self.key_position)
            # Processa os eventos da janela
            glfw.poll_events()
            # Limpa o buffer de cor e o buffer de profundidade
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            # Define o programa de shaders como ativo
            glUseProgram(self.shader)
            # Define a textura como ativa
            glBindTexture(GL_TEXTURE_2D, self.texture)
            # Define o VAO como ativo
            glBindVertexArray(self.quad_vao)
            # Cria a matriz de translação com base na posição do mouse
            translation = glm.translate(glm.mat4(1.0), glm.vec3(self.mouse_x / 640, self.mouse_y / 480, 0.0))
            # Aplica a translação usando a função glMultr
            self.glMultMatrix(glm.value_ptr(translation))
            # Desenha o primeiro quadrado (transladado para trás)
            model = np.identity(4, dtype=np.float32)
            glUniformMatrix4fv(glGetUniformLocation(self.shader, "model"), 1, GL_FALSE, model)
            glDrawArrays(GL_TRIANGLES, 0, 6)
            # Desenha o segundo quadrado (na posição original)
            model = np.identity(4, dtype=np.float32)
            glUniformMatrix4fv(glGetUniformLocation(self.shader, "model"), 1, GL_FALSE, model)
            glDrawArrays(GL_TRIANGLES, 0, 6)
            # Desativa o VAO
            glBindVertexArray(0)
            # Desativa a textura
            glBindTexture(GL_TEXTURE_2D, 0)
            # Desativa o programa de shaders
            glUseProgram(0)
            # Troca os buffers
            glfw.swap_buffers(self.window)
        # Finaliza a aplicação
        glfw.terminate()
# Cria a instância da aplicação
my_app = App()
# Executa a aplicação
my_app.run()
    