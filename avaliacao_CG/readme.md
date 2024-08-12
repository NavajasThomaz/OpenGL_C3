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
    <details open>
        <summary>

# Sumário</summary>

1. [Introdução](#Introdução)
2. [Implementação](#Implementação)
3. [Instruções](#Instruções)

    </details>
</div>
<details open>
<summary>

# Introdução</summary>

### Objetivo
O projeto visa implementar um programa em OpenGL que renderiza um cubo personalizado com a logo do C3. O cubo é renderizado com iluminação e tonalização, e é possível interagir com ele, movendo-o, rotacionando-o e escalonando-o.

### Ferramentas
<div style=display:inline-block>
<img align="center" width=100 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
Linguagem escolhida
</div>
<div>
<img align="center" width=100 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opengl/opengl-original.svg" />
Biblioteca gráfica para renderização de gráficos 3D.
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




<details open>
<summary>

# Implementação</summary>

###
Essa seção explica o passo a passo da implementação do programa em OpenGL.

1. **Bibliotecas utilizadas:** Na introdução falamos sobre as ferramentas que utilizamos e aqui mostraremos as bibliotecas utilizadas importadas no inicio do código.
```Python
import glm # utilizado para operações de vetores e matrizes
import glfw # utilizado para gerenciar janelas, eventos
import imgui # utilizado para renderização de gráficos 3D
import ctypes # Biblioteca para interação com C/C++
from OpenGL.GL import * # utilizado para renderização de gráficos 3D
import numpy as np # utilizado para operar com vetores e matrizes
from PIL import Image # utilizado para carregar imagens
from imgui.integrations.glfw import GlfwRenderer # utilizado para renderização de gráficos 3D

SCREEN_WIDTH = 1280 # Constantes para definir o tamanho da janela
SCREEN_HEIGHT = 720 #
```
2. **Configuração do ambiente:** Fizemos duas classes, uma para janela inicial e outra para a aplicação da OpenGL.

<div align="center">
<img src="https://github.com/NavajasThomaz/OpenGL_C3/blob/main/avaliacao_CG/Diagrama_das_Classes.png?raw=true"/>
</div>


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

A classe criada para essa janela é mais complexa doque a anterior, pois ela possue funções para o funcionamento da OpenGl.

#### Inicialização da janela

```Python
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
```



#### Criação do cubo

```Python
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
```


<div align='center'>
<img align="center" height=300 src="https://docs.hektorprofe.net/cdn/graficos3d/image-84.png" />
<img align="center" width=373 src="https://docs.hektorprofe.net/cdn/graficos3d/image-82.png" />
</div>


#### Criação da textura

```Python
from PIL import image
```
<div align='center'>
<img align="center"  src="https://pillow.readthedocs.io/en/stable/_static/pillow-logo.png" />

Utilizamos a biblioteca pillow para ler a imagem png da textura e converter para RGBA.
</div>


```Python
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
                    0,
                    GL_RGBA, # formato da textura
                    image.width, # largura
                    image.height, # altura
                    0,
                    GL_RGBA,
                    GL_UNSIGNED_BYTE, 
                    img_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, 0)  # Desvincula a textura
        return texture # Retorna o ID da textura
```

#### Criação e compilação dos shaders

Utlizamos 2 shaders programados em Opengl Shading Language (GLSL)

**Vertex shaders** ajustam a posição e os atributos dos vértices para definir a forma dos objetos 3D.

```glsl
#version 330 core
layout (location = 0) in vec3 position; // Posição do vértice
layout (location = 1) in vec2 texCoord; // Coordenadas de textura

out vec2 TexCoord; // Envia as coordenadas de textura para o fragment shader

uniform mat4 projection; // Matriz de projeção
uniform mat4 view; // Matriz de visualização
uniform mat4 model; // Matriz de modelo

void main() {
    gl_Position = projection * view * model * vec4(position, 1.0); // Aplica as matrizes
    TexCoord = texCoord; // Passa as coordenadas de textura para o fragment shader
}
```

 **Fragment shaders** calculam a cor e os detalhes de cada pixel, permitindo efeitos como texturização e iluminação.

```glsl
#version 330 core

in vec3 Normal; // Normal da superfície
in vec3 FragPos;  // Posição do fragmento no espaço
in vec3 ViewPos; // Posição da câmera
in vec2 TexCoord;

out vec4 FragColor;

uniform vec3 lightPos; // Posição da luz
uniform vec3 lightColor; // Cor da luz
uniform bool usePhong; // Habilitar/Desabilitar Phong
uniform sampler2D ourTexture; // shader da classe python

void main()
{
    vec4 color = texture(ourTexture, TexCoord); // Vincula o fragmento com a textura

    if (usePhong) {
        // Luz ambiente
        float ambientStrength = 0.9;
        vec3 ambient = ambientStrength * lightColor;

        // Luz difusa
        vec3 norm = normalize(Normal);
        vec3 lightDir = normalize(lightPos - FragPos);
        float diff = max(dot(norm, lightDir), 0.0);
        vec3 diffuse = diff * lightColor;

        // Luz especular (simplificada)
        float specularStrength = 0.5;
        vec3 viewDir = normalize(ViewPos - FragPos);
        vec3 reflectDir = reflect(-lightDir, norm);  
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32.0);
        vec3 specular = specularStrength * spec * lightColor;  
        vec3 result = (ambient + diffuse + specular) * color.rgb;
        FragColor = vec4(result, 1.0);
    } else {
        FragColor = color; // Cor da textura sem iluminação
    }
}
```

```Python
    def create_shader_program(self, vertex_file_path, fragment_file_path):
        """Compila e vincula um programa de shader a partir de arquivos de shader"""
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
        """ Compila um shader a partir do código fonte. """
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)

        # Check for compilation errors
        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise Exception(f"Shader compilation failed: {glGetShaderInfoLog(shader).decode()}")

        return shader
```

#### Inputs do usuário

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
```

#### Projeções

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

####

```Python
    def transladar(self, model, direcao_x, direcao_y, direcao_z):
        return glm.translate(model, glm.vec3(direcao_x, direcao_y, direcao_z))
        """ glm.translate
            Assumindo que o modelo esta como indetidade
            model=  |1 0 0 direcao_x|       |1 0 0 0|
                    |0 1 0 direcao_y|   *   |0 1 0 0|
                    |0 0 1 direcao_z|       |0 0 1 0|
                    |0 0 0 1|               |0 0 0 1|

        """
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
 <div style="display: inline_block">
    <img align="center" alt="C++" src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white">
    <a href="https://code.visualstudio.com/" target="_blank"><img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" target="_blank"></a>

 </div>



<details open>
<summary>

# Instruções</summary>
</details>

