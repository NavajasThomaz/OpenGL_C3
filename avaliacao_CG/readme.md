<div align="center">
<img align="center" width=350 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opengl/opengl-original.svg" />
<font size="10">_C3</font>
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


## Introdução
<div align="center" >
<img align="center" height=100 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
<img align="center" height=100 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original-wordmark.svg" />
<img align="center" width=100 height=200 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opengl/opengl-original.svg" />
</div>

### Objetivo
O projeto visa implementar um programa em OpenGL que renderiza um cubo personalizado com a logo do C3. O cubo é renderizado com iluminação e tonalização, e é possível interagir com ele, movendo-o, rotacionando-o e escalonando-o.

### Ferramentas

As ferramentas utilizadas nesse projeto são:

- OpenGL: biblioteca gráfica para renderização de gráficos 3D.
- C++: linguagem de programação utilizada para implementar o programa.
- GLM: biblioteca matemática para operações de vetores e matrizes.
- GLEW: biblioteca para gerenciar extensões OpenGL.
- GLFW: biblioteca para gerenciar janelas e eventos.

### Características

As principais características do projeto são:

- Renderização de uma escada 3D com iluminação e tonalização.
- Interação com a escada, movendo-a e escalonando-a.
- Utilização de shaders para implementar a iluminação e tonalização.
- Utilização de matrizes de transformação para implementar a movimentação e escalonamento.

### Implementação

A implementação do projeto é dividida em várias etapas:

1. **Configuração do ambiente:** Configurar o ambiente de desenvolvimento com as bibliotecas necessárias.
2. **Criação da escada:** Criar o modelo da escada utilizando vértices e faces.
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




## Funções
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
