#version 330 core

in vec3 Normal; // Normal da superfície
in vec2 TexCoord;
in vec3 lightDir;
in vec3 viewDir;

out vec4 FragColor;

uniform vec3 lightColor; // Cor da luz
uniform sampler2D ourTexture;

void main()
{
    vec4 color = texture(ourTexture, TexCoord);

    // Luz ambiente
    float ambientStrength = 0.9;
    vec3 ambient = ambientStrength * lightColor;

    // Luz difusa
    vec3 norm = normalize(Normal);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    // Luz especular (simplificada)
    vec3 reflectDir = reflect(-lightDir, norm);  
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32.0);
    vec3 specular = spec * lightColor;  

    vec3 result = (ambient + diffuse + specular) * color.rgb;
    FragColor = vec4(result, 1.0);

}
