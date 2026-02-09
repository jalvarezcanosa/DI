package com.example.aula.viewmodel;

import androidx.annotation.NonNull;
import androidx.lifecycle.ViewModel;
import androidx.lifecycle.ViewModelProvider;

import com.example.aula.data.InMemoryNoticeRepository;

// Implementa la interfaz Factory de Android.
// Su única misión es construir instancias de NoticeViewModel con sus dependencias.
public class NoticeViewModelFactory implements ViewModelProvider.Factory {

    private final InMemoryNoticeRepository repo;

    // Recibimos el repositorio desde fuera (Inyección de dependencias manual)
    public NoticeViewModelFactory(InMemoryNoticeRepository repo) {
        this.repo = repo;
    }

    // Este método es llamado internamente por Android cuando pides un ViewModel.
    @NonNull
    @Override
    public <T extends ViewModel> T create(@NonNull Class<T> modelClass) {
        // Verificamos si la clase que nos piden es NoticeViewModel
        if (modelClass.isAssignableFrom(NoticeViewModel.class)) {
            // Aquí ocurre la "magia": Creamos el ViewModel pasando el repo
            // y hacemos un casting genérico (T) para devolverlo.
            return (T) new NoticeViewModel(repo);
        }
        // Si nos piden un ViewModel que no sabemos fabricar, lanzamos error.
        throw new IllegalArgumentException("Unknown ViewModel class");
    }
}