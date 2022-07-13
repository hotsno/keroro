import setup
import mapper
import continue_watching

if not setup.is_set_up():
    setup.set_up()
mapper.map(True)
continue_watching.continue_watching()