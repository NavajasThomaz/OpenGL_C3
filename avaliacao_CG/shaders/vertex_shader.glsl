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
