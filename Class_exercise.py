class Camera(object):
    def __init__(self, model, battery_model):
        self.model = model
        self.battery_model = battery_model

    def take_photo(self, thing):
        print("{} takes photos of {}".format(self.model, thing))

    def set_up(Camera, Tripod)
        print("Set up Camera {} on Tripod".format(Camera, Tripod))

class VideoCamera(Camera):
    def __init__(self, model, resolution, battery_model):
        super(VideoCamera,self).__init__(model, battery_model)
        self.resolution = resolution

    def take_video(self, thing, duration):
        print("{} record video of {} for {} seconds".format(self.model, thing, duration))

class StillCamera(Camera):
    def __init__(self, model, resolution):
        super(StillCamera,self).__init__(model, battery_model)
        self.resolution = resolution
    
    def take_video(self, thing):
        print("{} cannot record video".format(self.model))

class Lens(object):
    def __init__(self, focal_length):
        self.focal_length = focal_length

    def mount(self, Camera):
        print("Mount {} on {}".format(self.focal_length, Camera))

class MemoryCard(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def insert(self, Camera):
        print("Insert Memory Card {} in Camera {}".format(self.name, Camera))

class Battery(object):
    def __init__(self, name, model):
        self.name  = name
        self.model = model

    def charge(self):
        print("Charge battery {}".format(self.name))

class Tripod(object):
    def __init__(self, model, height):
        self.model = model
        self.height = height
    
    def prepare(self):
        print("Prepare {}".format(self.model))

class Monopod(Tripod):
    def __init__(self, model, height):
        super(Tripod,self).__init__(model, height)
        self.model = model
    

    def extend(self):
        print("Extend Monopod {}, it reaches {}".format(self.model, self.height))

