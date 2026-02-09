package com.example.aula.viewmodel;


import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.aula.data.InMemoryNoticeRepository;

import java.util.List;

public class NoticeViewModel extends ViewModel {

    private final InMemoryNoticeRepository repo;

    // LiveData para la UI
    private final MutableLiveData<String> _listado = new MutableLiveData<>(); // El texto grande con todos los avisos
    private final MutableLiveData<String> _error = new MutableLiveData<>();   // Errores de validación (ej: título vacío)
    private final MutableLiveData<String> _eventoToast = new MutableLiveData<>(null); // Mensajes de éxito fugaces

    public NoticeViewModel(InMemoryNoticeRepository repo) {
        this.repo = repo;
        refresh(); // Cargar la lista nada más iniciarse la pantalla
    }

    public LiveData<String> getListado() { return _listado; }
    public LiveData<String> getError() { return _error; }
    public LiveData<String> getEventoToast() { return _eventoToast; }

    // Resetea el evento del Toast para que no vuelva a salir al rotar la pantalla
    public void consumirEventoToast() {
        _eventoToast.setValue(null);
    }

    // Lógica para AÑADIR un aviso
    public void addNotice(String title, String subject) {
        // 1. VALIDACIÓN (Lógica de negocio)
        if (title == null || title.trim().isEmpty()) {
            _error.setValue("El título no puede estar vacío");
            return; // Detenemos si no es válido
        }
        // Valor por defecto si la materia está vacía
        if (subject == null || subject.trim().isEmpty()) subject = "General";

        // 2. Guardar en repositorio (formato "Materia | Título")
        repo.add(subject.trim() + " | " + title.trim());

        // 3. Actualizar la UI
        refresh(); // Recargar la lista para que aparezca el nuevo
        _eventoToast.setValue("Aviso añadido"); // Feedback al usuario
    }

    // Lógica para BORRAR el último aviso
    public void deleteLast() {
        // El repositorio nos devuelve true si borró, false si estaba vacía
        boolean ok = repo.removeLast();

        if (!ok) {
            _error.setValue("No hay avisos para borrar");
            return;
        }

        refresh();
        _eventoToast.setValue("Último aviso borrado");
    }

    // Método auxiliar para transformar la LISTA de datos en TEXTO para el TextView
    private void refresh() {
        List<String> data = repo.getAll();

        // Caso lista vacía
        if (data.isEmpty()) {
            _listado.setValue("Crea un aviso para que se muestre aquí");
            return;
        }

        // Transformación de datos (Data Transformation):
        // Convertimos ["A", "B"] en "• A\n• B\n"
        StringBuilder sb = new StringBuilder();
        for (String s : data) sb.append("• ").append(s).append("\n");

        _listado.setValue(sb.toString());
    }
}