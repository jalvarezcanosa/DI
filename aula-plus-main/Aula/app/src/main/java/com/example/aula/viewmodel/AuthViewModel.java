package com.example.aula.viewmodel;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.aula.data.AuthRepository;

public class AuthViewModel extends ViewModel {

    // Repositorio: La clase que sabe hablar con Firebase
    private final AuthRepository repo;

    // ESTADOS DE LA PANTALLA (Observables)
    // _loading: Controla si se muestra el spinner de carga
    private final MutableLiveData<Boolean> _loading = new MutableLiveData<>(false);
    // _errorMessage: Guarda el mensaje de error si algo falla (para el Snackbar)
    private final MutableLiveData<String> _errorMessage = new MutableLiveData<>(null);
    // _navEvent: "Señal" para decirle a la UI que cambie de pantalla ("HOME" o "LOGIN")
    private final MutableLiveData<String> _navEvent = new MutableLiveData<>(null);

    private final MutableLiveData<String> _currentUserEmail = new MutableLiveData<>(null);

    // Inyección de dependencias: Recibimos el repositorio en el constructor
    public AuthViewModel(AuthRepository repo) {
        this.repo = repo;
    }

    // Getters públicos que devuelven LiveData inmutable
    // (La UI solo puede LEER estos datos, no modificarlos directamente)
    public LiveData<Boolean> getLoading() { return _loading; }
    public LiveData<String> getErrorMessage() { return _errorMessage; }
    public LiveData<String> getNavEvent() { return _navEvent; }

    public LiveData<String> getCurrentUserEmail() { return _currentUserEmail; }


    // Método para resetear la navegación una vez que la UI ya ha cambiado de pantalla
    public void consumeNavEvent() { _navEvent.setValue(null); }

    // Lógica de LOGIN
    public void login(String email, String pass) {
        _errorMessage.setValue(null); // Limpiar errores viejos
        _loading.setValue(true);      // Mostrar spinner

        // Llamada asíncrona al repositorio
        repo.login(email, pass, new AuthRepository.AuthCallback() {
            @Override public void onSuccess() {
                // IMPORTANTE: Usamos .postValue() porque este callback viene de
                // un hilo secundario de Firebase, y necesitamos actualizar la UI
                // en el hilo principal.
                _loading.postValue(false);
                _navEvent.postValue("HOME");
            }

            @Override public void onError(String message) {
                _loading.postValue(false);
                _errorMessage.postValue(message); // Mostrar error al usuario
            }
        });
    }

    // Lógica de REGISTRO (muy similar al login)
    public void register(String email, String pass) {
        _errorMessage.setValue(null);
        _loading.setValue(true);

        repo.register(email, pass, new AuthRepository.AuthCallback() {
            @Override public void onSuccess() {
                _loading.postValue(false);
                _navEvent.postValue("HOME"); // Si registra bien, entra directo
            }

            @Override public void onError(String message) {
                _loading.postValue(false);
                _errorMessage.postValue(message);
            }
        });
    }

    // Verifica si el usuario ya tenía sesión iniciada (para el AuthGate)
    public void checkSession() {
        // Aquí usamos .setValue() porque repo.isLoggedIn() es síncrono (instantáneo)
        _navEvent.setValue(repo.isLoggedIn() ? "HOME" : "LOGIN");
    }

    // Cerrar sesión
    public void logout() {
        repo.logout();
        _navEvent.setValue("LOGIN"); // Mandar al usuario de vuelta al login
    }

    public void loadUserProfile() {
        String email = repo.getCurrentUserEmail();
        _currentUserEmail.setValue(email);
    }
}