<img align="center" width=50 src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Logo_FURG_institucional.png/598px-Logo_FURG_institucional.png" />
<div align="center">
<img align="center" width=350 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opengl/opengl-original.svg" />
<img align="center" width=350 src="http://www.c3.furg.br/images/logoP.png" />
</div>

##### <div align="center">🧱Esse projeto é uma avaliação da diciplina de Sistemas Gráficos de 2024.🧱</div>

<div align="center">

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=NavajasThomaz&repo=OpenGL_C3&theme=transparent)](https://github.com/NavajasThomaz/OpenGL_C3)

</div>


### <div align="center">Autores</div>

### <div align="center">Thomaz Colalillo Navajas - 140560</div>
<div style="display: inline_block", align="center">
    <a href = "mailto:thomaznavajas@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
    <a href="www.linkedin.com/in/thomaz-navajas" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
    <a href="https://github.com/NavajasThomaz" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" target="_blank"></a>
    <a href="https://www.kaggle.com/thomaznavajas" target="_blank"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" target="_blank"></a>

</div>

### <div align="center">Denise Valéria velarde - 157670</div>
<div style="display: inline_block", align="center">
    <a href = "mailto:denise.velarde1@outlook.com"><img src="https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" target="_blank"></a>
    <a href="www.linkedin.com/in/thomaz-navajas" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
    <a href="https://github.com/DeniseValeriaVelarde" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" target="_blank"></a>

</div>
<div>



<style>
.teste{
    background-color: red;
    color: white;
    border: 2px solid black;
    padding: 10px;
    margin: 10px;
}
</style>

# Sumário
<details open>
<summary></summary>

<div class="teste">

1. [Introdução](#Introdução)
1. [Introdução](#Introdução)
2. [Implementação](#technologies)
3. [Instruções](#setup)
4. [Introdução](#Introdução)
5. [Implementação](#technologies)
6. [Instruções](#setup)

</div>

</details>

## Introdução
<details open>

<summary><h1>Introdução</h1></summary>

### Objetivo
O projeto visa implementar um programa em OpenGL que renderiza um cubo personalizado com a logo do C3. O cubo é renderizado com iluminação e tonalização, e é possível interagir com ele, movendo-o, rotacionando-o e escalonando-o.




### Ferramentas
<div>
<img align="center" width=100 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
Linguagem escolhida
</div>
<div>
<img align="center" width=100 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opengl/opengl-original.svg" />
Biblioteca gráfica para renderização de gráficos 3D.
</div>
<div>
<img align="center" width=100 src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
linguagem de programação utilizada para implementar os Shaders.
</div>
<div>
<img align="center" width=100 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original-wordmark.svg" />
Biblioteca numérica para operar com vetores e matrizes.
</div>
<div>
<img align="center" width=50 src="https://pypi.org/static/images/logo-small.8998e9d1.svg" />
Bibliotecas como GLM w GLFW para gerenciar janelas, eventos, operações de vetores e matrizes.
</div>
</details>

###
<details open>
<summary><h1>Implementação</h1></summary>

### 
1. **Bibliotecas utilizadas:** Na introdução falamos sobre as ferramentas que utilizamos e aqui mostraremos as bibliotecas utilizadas importadas no inicio do código.
```Python
import glm # utilizado para operações de vetores e matrizes
import glfw # utilizado para gerenciar janelas, eventos
import imgui # utilizado para renderização de gráficos 3D
import ctypes
from OpenGL.GL import * # utilizado para renderização de gráficos 3D
import numpy as np # utilizado para operar com vetores e matrizes
from PIL import Image # utilizado para carregar imagens
from imgui.integrations.glfw import GlfwRenderer # utilizado para renderização de gráficos 3D

SCREEN_WIDTH = 1280 # Constantes para definir o tamanho da janela
SCREEN_HEIGHT = 720 #
```
2. **Configuração do ambiente:** Fizemos duas classes, uma para janela inicial e outra para a aplicação da OpenGL.

- Janela inicial
```Python
class StartScreen:
    def __init__(self):
        self.window = glfw.create_window(                 # Instancia a janela
                                        SCREEN_WIDTH, 
                                        SCREEN_HEIGHT, 
                                        "Tela Inicial", 
                                        None, 
                                        None
                                        )
        glfw.make_context_current(self.window)            # Coloca a janela como contexto
        imgui.create_context()
        self.impl = GlfwRenderer(self.window)             # Instancia o renderer da Glfw
        self.start_game = False

    def show(self):
        while not glfw.window_should_close(self.window):  # Loop principal da janela
            glfw.poll_events()                            # Processa os eventos
            self.impl.process_inputs()                    # Processa os inputs do usuário
            imgui.new_frame()                             # Cria um novo frame
            imgui.begin("Bem-vindo!", closable=False)     # Inicia um novo frame
            if imgui.button("Iniciar"):                   # Cria um botão para iniciar a simulação
                self.start_game = True
                glfw.set_window_should_close(self.window, True)
            imgui.end()

            imgui.render()
            self.impl.render(imgui.get_draw_data())
            glfw.swap_buffers(self.window)

        self.impl.shutdown()
        glfw.destroy_window(self.window)

```

- Janela do OpenGL
```Python
class OpenGLApp:
    def __init__(self):
        # Create the window
        self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "C3_Logo", None, None)
        self.projecao = 0
        self.trans_values = [0.0, 0.0, 0.0]
        self.rot_values = [0.0, 0.0, 0.0]
        self.scale_value = 0.0
        self.usePhong = False
        self.useGouraud = False
        self.useRaster = False
        
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window can't be created!")

        glfw.make_context_current(self.window)
        glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED)

        # Set background color
        glClearColor(0.1, 0.2, 0.3, 1.0)

        # Enable depth testing
        glEnable(GL_DEPTH_TEST)

        # Compile the shaders
        self.shader = self.create_shader_program("shaders/vertex_shader.glsl", "shaders/fragment_shader.glsl")

        # Iluminação Phong
        self.usePhongLoc = glGetUniformLocation(self.shader, "usePhong")
        
        # Tonalização Gouraud
        self.useGouraudLoc = glGetUniformLocation(self.shader, "useGouraud")
        
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
        self.texture = self.create_texture("Textures/logoFurg.png")
```
```Python
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
```
```Python
    def create_vao(self, vertices, indices):
        vao = glGenVertexArrays(1)
        vbo = glGenBuffers(1)
        ebo = glGenBuffers(1)
        nbo = glGenBuffers(1)  # Novo VBO para normais
        
        glBindVertexArray(vao)

        # VBO for vertices
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        # EBO for indices
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)
        

        # Vertex Position Attributez
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * vertices.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # Unbind the VAO (good practice)
        glBindVertexArray(0)

        return vao
```
```Python
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
```
```Python
    def compile_shader(self, source, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)

        # Check for compilation errors
        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise Exception(f"Shader compilation failed: {glGetShaderInfoLog(shader).decode()}")

        return shader
```
```Python
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
```
```Python
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
```
```Python
    def perspectiva(self):
        projection = glm.perspective(glm.radians(45.0), 800 / 600, 0.1, 100.0)
        glUniformMatrix4fv(self.projection_loc, 1, GL_FALSE, glm.value_ptr(projection))
```
```Python
    def ortogonal(self):
        projection = glm.ortho(-10.0, 10.0, -10.0, 10.0, -10.0, 10.0)
        glUniformMatrix4fv(self.projection_loc, 1, GL_FALSE, glm.value_ptr(projection))
```
```Python
    def transladar(self, model, direcao_x, direcao_y, direcao_z):
        return glm.translate(model, glm.vec3(direcao_x, direcao_y, direcao_z))
```
```Python
    def rotacionar(self, model, angle_x, angle_y, angle_z):
        # Aplica a rotação em cada eixo separadamente
        model = glm.rotate(model, glm.radians(angle_x), glm.vec3(1.0, 0.0, 0.0))
        model = glm.rotate(model, glm.radians(angle_y), glm.vec3(0.0, 1.0, 0.0))
        model = glm.rotate(model, glm.radians(angle_z), glm.vec3(0.0, 0.0, 1.0))
        return model
```
```Python
    def escalonar(self, model, escala):
        return glm.scale(model, glm.vec3(escala, escala, escala))
```
```Python
    def toggle_phong(self):
        self.usePhong = not self.usePhong
        glUniform1i(self.usePhongLoc, self.usePhong)
```
```Python
    def toggle_gouraud(self):
        self.useGouraud = not self.useGouraud
```
```Python
    def toggle_raster(self):
        self.useRaster = not self.useRaster
```
```Python
    def run(self):
        
        self.cube_vao, self.cube_vbo = self.create_cube()
        model = glm.mat4(1.0)  # Matriz modelo identidade
        
        while not glfw.window_should_close(self.window):
            current_frame = glfw.get_time()
            self.delta_time = current_frame - self.last_frame
            self.last_frame = current_frame

            self.process_input(self.window)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glUseProgram(self.shader)
            
            
            if self.projecao == 0:
                self.perspectiva()
            else:
                self.ortogonal()
            if self.trans_values != [0.0, 0.0, 0.0]:
                model = self.transladar(model, self.trans_values[0], self.trans_values[1], self.trans_values[2])
                self.trans_values = [0.0, 0.0, 0.0]
            if self.rot_values != [0.0, 0.0, 0.0]:
                model = self.rotacionar(model, self.rot_values[0], self.rot_values[1], self.rot_values[2])
                self.rot_values = [0.0, 0.0, 0.0]
            if self.scale_value != 0.0:
                model = self.escalonar(model, self.scale_value)
                self.scale_value = 0.0
            
            glUniform1i(self.usePhongLoc, self.usePhong)
            
            view = glm.lookAt(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)
            
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
```
```Python
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

```

2. **Criação da escada:** Criar o modelo do cubo personalizado utilizando vértices e faces.
3. **Renderização da escada:** Renderizar a escada utilizando OpenGL.
4. **Implementação da iluminação:** Implementar a iluminação utilizando shaders.
5. **Implementação da tonalização:** Implementar a tonalização utilizando shaders.
6. **Implementação da interação:** Implementar a interação com a escada, movendo-a e escalonando-a.



### Resultados

O resultado final do projeto é um programa que renderiza uma escada 3D com iluminação e tonalização, e que permite ao usuário interagir com ela, movendo-a e escalonando-a.

### Conclusão

Este projeto demonstra a capacidade de utilizar OpenGL para renderizar gráficos 3D, implementar iluminação e tonalização, e criar interação com objetos. O projeto também demonstra a importância de utilizar bibliotecas matemáticas e de gerenciamento de janelas para facilitar o desenvolvimento de programas gráficos.

### Código

O código fonte do projeto está disponível no repositório do GitHub: [link para o repositório](https://github.com/NavajasThomaz/TumorVision).






- Movimentação
1. Translação
```Python
def transladar(self, model, direcao_x, direcao_y, direcao_z):
    return glm.translate(model, glm.vec3(direcao_x, direcao_y, direcao_z))
```
### glm.translate



2. Rotação
3. Escalonamento
- Projeção
4. Perspectiva
5. Ortogonal
- Outros
6. Iluminação (Phong)
7. Tonalização (Gouraud)
8. Rasterização (Bresenham)

<div align="center">

### Rasterização (Bresenham)

Neste projeto usamos o algoritmo de Bresenham para rasterizar linhas de forma eficiente e precisa, essa é uma tecnica amplamente utilizada para desenhar linhas entre dois pontos em uma grade de pixels.
</div>

```python
import numpy as np
from OpenGL.GL import *
```
```Python
# Função que implementa o algoritmo de Bresenham para rasterizar uma linha
def bresenham_line(x0, y0, x1, y1):
    """Implementa o algoritmo de Bresenham para rasterizar uma linha"""
    points = []  # Lista que armazenará os pontos da linha
    dx = abs(x1 - x0)  # Diferença absoluta nas coordenadas x
    dy = abs(y1 - y0)  # Diferença absoluta nas coordenadas y
    sx = 1 if x0 < x1 else -1  # Sinal do incremento x
    sy = 1 if y0 < y1 else -1  # Sinal do incremento y
    err = dx - dy  # Erro inicial

    while True:
        points.append((x0, y0))  # Adiciona o ponto atual à lista de pontos
        if x0 == x1 and y0 == y1:  # Verifica se o ponto final foi alcançado
            break
        e2 = 2 * err  # Calcula o dobro do erro
        if e2 > -dy:  # Ajusta o erro e incrementa x
            err -= dy
            x0 += sx
        if e2 < dx:  # Ajusta o erro e incrementa y
            err += dx
            y0 += sy

    return points  # Retorna a lista de pontos da linha
```
```Python
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
```
### Função de rasterização Bresenham
Inicialização:
- definimos os pontos iniciais (x0, y0) e final(x1,y1) da linha,
```Python
def bresenham_line(x0, y0, x1, y1):
    """Implementa o algoritmo de Bresenham para rasterizar uma linha"""
    points = []  # Lista que armazenará os pontos da linha
``` 
- calculamos a diferença absoluta nas coordenadas x(dx) e y(dy),
```Python
    dx = abs(x1 - x0)  # Diferença absoluta nas coordenadas x
    dy = abs(y1 - y0)  # Diferença absoluta nas coordenadas y
``` 
- Determinamos a direção da linha com os dinais incrementados x(sx) e y(sy)
```Python
    sx = 1 if x0 < x1 else -1  # Sinal do incremento x
    sy = 1 if y0 < y1 else -1  # Sinal do incremento y
```   
- inicializamos um valor de erro(err) que vai nos ajudar a decidir quando devemos incrementar as coordenadas x ou y.
```Python
err = dx - dy  # Erro inicial
```      

no looop: 
```Python
while True:
```  
- adicionamos o ponto atual a lista de pontos que compoem a linha
```Python
    points.append((x0, y0))  # Adiciona o ponto atual à lista de pontos
```  
- loop encerrado com o ponto final
```Python
    if x0 == x1 and y0 == y1:  # Verifica se o ponto final foi alcançado
        break
```  
- calcula-se e2 que é duas vezes o erro
```Python
    e2 = 2 * err  # Calcula o dobro do erro
```  
- ajustamos o erro e incrementamos x ou y dependendo do valor de e2
```Python
    if e2 > -dy:  # Ajusta o erro e incrementa x
            err -= dy
            x0 += sx
        if e2 < dx:  # Ajusta o erro e incrementa y
            err += dx
            y0 += sy
```  
### Função para configurar o VAO e VBO para a linha
```Python
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
``` 

          

```Python
```          
<img align="center" alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"
/>
Link pra pegar as imagens
https://devicon.dev/
|
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tensorflow/tensorflow-original.svg" />
TensorFlow |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/keras/keras-original.svg" />
Keras |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytorch/pytorch-original.svg" />
PyTorch |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opencv/opencv-original.svg" />
OpenCv |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg" />
NumPy |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg" />
MatPlotLib |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" />
Pandas |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg" />
FastAPI |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" />
Flask |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg" />
SciKitLearn |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/googlecloud/googlecloud-original.svg" />
Google Clouds |
<img align="center" width=20 height=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/json/json-original.svg" />
Json | and others... |


 <div style="display: inline_block">
    <img margin=10px align="center" alt="C" src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white"
    />
    <img align="center" alt="C++" src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white"
    />
    <img align="center" alt="C#" src="https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=c-sharp&logoColor=white"
    />
    <img align="center" alt="RStudio" src="https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white"
    />
    <img align="center" alt="Arduino" src="https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white"
    /><br><br>
    <img align="center" alt="Js" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"
    />
    <img align="center" alt="TypeScript" src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white"
    />
    <img align="center" alt="html5" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"
    />
    <img align="center" alt="Node.js" src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white"
    />
    <img align="center" alt="Django" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"
    />
    <a href="https://www.heroku.com/" target="_blank"><img align="center" alt="Trello" src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" target="_blank">
    </a><br>

 </div>

 ## Database Preferences

<div style="display: inline_block">   
    <a href="https://www.sqlite.org/" target="_blank"><img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" target="_blank"></a>
    <a href="https://www.mysql.com/" target="_blank"><img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white" target="_blank"></a>
    <a href="https://www.mongodb.com/" target="_blank"><img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" target="_blank"></a>
    <a href="https://www.postgresql.org/" target="_blank"><img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" target="_blank"></a>
</div><br>

# Main Projects

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=NavajasThomaz&repo=TumorVision&theme=transparent)](https://github.com/NavajasThomaz/TumorVision)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=NavajasThomaz&repo=PriceTracker&theme=transparent)](https://github.com/NavajasThomaz/PriceTracker)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=NavajasThomaz&repo=IA_KNearest_Hydrometer_Reader&theme=transparent)](https://github.com/NavajasThomaz/IA_KNearest_Hydrometer_Reader)

# Most used IDE's

<div>   
    <a href="https://www.jetbrains.com/pycharm/" target="_blank"><img src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white" target="_blank"></a>
    <a href="https://colab.research.google.com/" target="_blank"><img src="https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252" target="_blank"></a>
    <a href="https://visualstudio.microsoft.com/pt-br/downloads/" target="_blank"><img src="https://img.shields.io/badge/Visual_Studio-5C2D91?style=for-the-badge&logo=visual%20studio&logoColor=white" target="_blank"></a>
    <a href="https://code.visualstudio.com/" target="_blank"><img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" target="_blank"></a>
    <a href="https://posit.co/download/rstudio-desktop/" target="_blank"><img src="https://img.shields.io/badge/RStudio-75AADB?style=for-the-badge&logo=RStudio&logoColor=white" target="_blank"></a><br>
    <a href="https://www.gitpod.io/" target="_blank"><img src="https://img.shields.io/badge/Gitpod-000000?style=for-the-badge&logo=gitpod&logoColor=#FFAE33" target="_blank"></a>
    <a href="https://eclipseide.org/" target="_blank"><img src="https://img.shields.io/badge/Eclipse-2C2255?style=for-the-badge&logo=eclipse&logoColor=white" target="_blank"></a>
    <a href="https://www.arduino.cc/en/software" target="_blank"><img src="https://img.shields.io/badge/Arduino_IDE-00979D?style=for-the-badge&logo=arduino&logoColor=white" target="_blank"></a>
    <a href="https://notepad-plus-plus.org/downloads/" target="_blank"><img src="https://img.shields.io/badge/Notepad++-90E59A.svg?style=for-the-badge&logo=notepad%2B%2B&logoColor=black" target="_blank"></a>
    <a href="https://www.sublimetext.com/" target="_blank"><img src="https://img.shields.io/badge/sublime_text-%23575757.svg?&style=for-the-badge&logo=sublime-text&logoColor=important" target="_blank"></a>
</div><br>


# Workspace Specs 💻
 <div>
    <img align="center" alt="GPU" src="https://img.shields.io/badge/NVIDIA-RTX2070 Super-76B900?style=for-the-badge&logo=nvidia&logoColor=white"
    />
    <img align="center" alt="CPU" src="https://img.shields.io/badge/AMD-Ryzen_7_5800X-ED1C24?style=for-the-badge&logo=amd&logoColor=white"
    />
    <img align="center" alt="OS" src="https://img.shields.io/badge/Windows-10 Pro-0078D6?style=for-the-badge&logo=windows&logoColor=white"
    />
 </div><br>


# 🎮 Game Develop 👾

My journey begins in 2014 when I was just 12 years old, my parents realized that I had a great affinity with electronics and especially video games, so they decided to take advantage of this and enrolled me in the first programming school called Supergeeks.


<img class="center" alt="SuperGeeks" src="https://supergeeks.com.br/images/logo_SG_com_borda.svg?imwidth=256"
/><br>

5 years later, with a course load of 264 hours, I graduated from the course having learned in theory and practice the best tools for developing 2D, 3D, VA and VR games such as Unity and Unreal.


<div class="mycontainer center">
    <div>
        <img width=300 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/unity/unity-original-wordmark.svg" />
    </div>
    <div>
        <img width=300 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/unrealengine/unrealengine-original-wordmark.svg" />
    </div>
</div>
