'''
Concept: A smart home device can act as a light, speaker, or both.
It overrides base behavior, supports overloaded actions, and uses MRO to decide what to do.

'''


# Base class
class Device:
    def operate(self, mode="basic"):  # <-- Overloading simulated using default argument
        print(f"Device operating in {mode} mode.")

# Derived class
class Light(Device):
    def operate(self, mode="light"):  # <-- Method Overriding from Device
        print(f"Light turned ON in {mode} mode.")

# Another derived class
class Speaker(Device):
    def operate(self, mode="sound"):  # <-- Method Overriding from Device
        print(f"Speaker playing music in {mode} mode.")

# Multiple inheritance
class SmartLightSpeaker(Light, Speaker):
    def operate(self, mode="smart"):  # <-- Method Overriding from Light and Speaker
        if mode == "light":
            super(Light, self).operate(mode)  # <-- MRO: Call Speaker. Light skipped.
        elif mode == "sound":
            super().operate(mode)            # <-- MRO: Call Light
        else:
            print("Smart device operating in combined smart mode.")

# MRO shows the lookup order
print(SmartLightSpeaker.__mro__)  # <-- MRO in action

# Create object
device = SmartLightSpeaker()
device.operate("light")   # <-- Overloading (input value), MRO resolves to Speaker
device.operate("sound")   # <-- Overloading (input value), MRO resolves to Light
device.operate("smart")   # <-- Overriding in SmartLightSpeaker
