import colorama
import utils.config, utils.mapper, utils.continue_watching

colorama.init()

try:
    utils.config.set_up()
    utils.mapper.map()
    utils.continue_watching.continue_watching()
except KeyboardInterrupt: # If user uses Ctrl-C, don't error
    quit()
