import threading
import time

class AutosaveThread(threading.Thread):
    
    def __init__(self, modelo, callback_status):

        super().__init__(daemon=True)
        self.modelo = modelo
        self.callback_status = callback_status
        self._stop_event = threading.Event()
        self.interval = 10 

    def run(self):
        while not self._stop_event.is_set():
            try:
                self._stop_event.wait(self.interval)
                
                if self._stop_event.is_set():
                    break
                
                self.modelo.guardar_csv()
                
                self.callback_status(
                    "Auto-guardado completado",
                    color="green"
                )
                
            except Exception as e:
                self.callback_status(
                    f"Error en auto-guardado: {str(e)}",
                    color="red"
                )
    
    def stop(self):
        self._stop_event.set()
