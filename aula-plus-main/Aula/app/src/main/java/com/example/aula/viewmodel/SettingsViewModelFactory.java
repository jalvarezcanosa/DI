package com.example.aula.viewmodel;

import android.content.Context;

import androidx.lifecycle.ViewModel;
import androidx.lifecycle.ViewModelProvider;

import com.example.aula.data.SettingsRepository;

public class SettingsViewModelFactory implements ViewModelProvider.Factory {

    private final Context context;

    // Necesitamos el contexto para poder abrir el archivo de preferencias
    public SettingsViewModelFactory(Context context) {
        // Usamos .getApplicationContext() para evitar fugas de memoria (Memory Leaks).
        // Esto asegura que no nos quedemos atados a una Activity que pueda destruirse.
        this.context = context.getApplicationContext();
    }

    @Override
    public <T extends ViewModel> T create(Class<T> modelClass) {
        if (modelClass.isAssignableFrom(SettingsViewModel.class)) {
            // 1. Creamos el repositorio usando el contexto
            SettingsRepository repo = new SettingsRepository(context);

            // 2. Creamos el ViewModel pasándole ese repositorio
            return (T) new SettingsViewModel(repo);
        }
        throw new IllegalArgumentException("Unknown ViewModel class");
    }
}