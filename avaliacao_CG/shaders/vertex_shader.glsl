#version 330 core
layout (location = 0) in vec3 position; // Posição do vértice
layout (location = 1) in vec2 texCoord; // Coordenadas de textura
layout (location = 2) in vec3 normal; // Normal

out vec2 TexCoord; // Envia as coordenadas de textura para o fragment shader
out vec3 Normal; // Envia o vetor da normal para o fragment shader
out vec3 ViewDir; // Envia o vetor 
out vec3 LightDir; // Envia o vetor de direção da luz

uniform mat4 projection; // Matriz de projeção
uniform mat4 view; // Matriz de visualização
uniform mat4 model; // Matriz de modelo
uniform vec3 lightPos; // Vetor de posição da luz
uniform vec3 viewPos; // Posição da câmera

void main() {
    gl_Position = projection * view * model * vec4(position, 1.0); // Aplica as matrizes
    TexCoord = texCoord; // Passa as coordenadas de textura para o fragment shader
    vec3 FragPos = vec3(model * vec4(position, 1.0));
    Normal = mat3(transpose(inverse(model))) * normal;
    LightDir = normalize(lightPos - FragPos);
    ViewDir = normalize(viewPos - FragPos);
}
