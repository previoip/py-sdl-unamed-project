from sdl2 import *
from src.config_handler import ConfigType, newConfig, config_pool

APP_NAME                = b'foobar'
APP_SDL_INIT_FLAGS      = SDL_INIT_VIDEO | SDL_INIT_AUDIO | SDL_INIT_EVENTS
APP_SDL_WINDOWSIZE_W    = 640
APP_SDL_WINDOWSIZE_H    = 480
APP_SDL_WINDOWPOS_X     = SDL_WINDOWPOS_UNDEFINED
APP_SDL_WINDOWPOS_Y     = SDL_WINDOWPOS_UNDEFINED
APP_SDL_WINDOW_FLAGS    = SDL_WINDOW_RESIZABLE | SDL_WINDOW_SHOWN