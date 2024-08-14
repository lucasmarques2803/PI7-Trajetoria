

    def set_thigh_pid(self, kp, ki, kd):
        value_kp = int(kp) & 0x1F
        value_ki = 2 << 5 | int(ki)
        value_kd = 4 << 5 | int(kd)
        self.RPi_Serial.write_register(globals.REG_KP, value_kp)
        self.RPi_Serial.write_register(globals.REG_KP, value_ki)
        self.RPi_Serial.write_register(globals.REG_KP, value_kd)

    def set_calf_pid(self, kp, ki, kd):
        value_kp = 1 << 5 | int(kp)
        value_ki = 3 << 5 | int(ki)
        value_kd = 5 << 5 | int(kd)
        self.RPi_Serial.write_register(globals.REG_KP, value_kp)
        self.RPi_Serial.write_register(globals.REG_KP, value_ki)
        self.RPi_Serial.write_register(globals.REG_KP, value_kd)

    def get_N(self):
        return self.N + 1

def main():
    filename="./G_trajetoria"
    coordinates=parsing(filename)
    root = ctk.CTk()
    root.title("Mechanical Leg Control Interface")
