#version 330 core

in vec3 Normal; // Normal da superfície
in vec3 FragPos;  // Posição do fragmento no espaço
in vec3 ViewPos; // Posição da câmera
in vec2 TexCoord;

out vec4 FragColor;

uniform vec3 lightPos; // Posição da luz
uniform vec3 lightColor; // Cor da luz
uniform bool usePhong; // Habilitar/Desabilitar Phong
uniform sampler2D ourTexture;

void main()
{
    vec4 color = texture(ourTexture, TexCoord);

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
