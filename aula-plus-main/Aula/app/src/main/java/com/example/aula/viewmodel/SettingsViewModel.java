package com.example.aula.viewmodel;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.aula.data.SettingsRepository;

public class SettingsViewModel extends ViewModel {

    private final SettingsRepository repo;
    // _darkMode: LiveData que observará la Activity/Fragment para cambiar el tema visualmente
    private final MutableLiveData<Boolean> _darkMode = new MutableLiveData<>();

    public SettingsViewModel(SettingsRepository repo) {
        this.repo = repo;
        // Al iniciar, leemos la preferencia guardada en disco para saber
        // si la app debe arrancar en modo oscuro o claro.
        _darkMode.setValue(repo.isDarkModeEnabled());
    }

    // Getter para que la UI observe los cambios
    public LiveData<Boolean> getDarkMode() {
        return _darkMode;
    }

    // Método llamado cuando el usuario toca el Switch
    public void setDarkMode(boolean enabled) {
        // 1. Guardamos el cambio en disco (Persistencia)
        repo.setDarkMode(enabled);

        // 2. Actualizamos el LiveData para que la UI reaccione y cambie los colores
        _darkMode.setValue(enabled);
    }
}