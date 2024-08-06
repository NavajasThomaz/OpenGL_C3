import glfw
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from PIL import Image
import numpy as np

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def load_image(filepath):
    """ Carrega uma imagem e retorna como um objeto Image. """
    return Image.open(filepath).convert('RGBA')


def create_texture(image):
    """ Cria uma textura OpenGL a partir de um objeto Image. """
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image.tobytes())
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glBindTexture(GL_TEXTURE_2D, 0)
    return texture


def create_shader_program(vertex_filepath: str, fragment_filepath: str) -> int:
    with open(vertex_filepath, 'r') as file:
        vertex_src = file.read()
    with open(fragment_filepath, 'r') as file:
        fragment_src = file.read()

    vertex_shader = compileShader(vertex_src, GL_VERTEX_SHADER)
    fragment_shader = compileShader(fragment_src, GL_FRAGMENT_SHADER)
    shader = compileProgram(vertex_shader, fragment_shader)
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)
    return shader
