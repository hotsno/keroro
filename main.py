import utils.config, utils.mapper, utils.continue_watching, colorama

colorama.init()

utils.config.set_up()
utils.mapper.map()
utils.continue_watching.continue_watching()