class Device:
    def turn_on(self):
        return "The device is now ON."
    def turn_off(self):
        return "The device is now OFF."
class GamingConsole(Device):
    def start_game(self, game_name):
        return f"The gaming console starts the game: {game_name}."
class SmartWatch(Device):
    def show_heart_rate(self):
        return "The smartwatch displays your heart rate: 78 BPM."
class Router(Device):
    def restart(self):
        return "The router is restarting..."
console = GamingConsole()
watch = SmartWatch()
router = Router()

print(console.turn_on())
print(console.start_game("Cyber Quest"))
print(watch.turn_on())
print(watch.show_heart_rate())
print(router.turn_on())
print(router.restart())
