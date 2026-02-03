package com.example.aula.viewmodel;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.aula.data.AuthRepository;
import com.google.firebase.auth.FirebaseAuth;

public class AuthViewModel extends ViewModel {

    private final FirebaseAuth auth;

    private final MutableLiveData<Boolean> _loading = new MutableLiveData<>(false);
    private final MutableLiveData<String> _errorMessage = new MutableLiveData<>(null);

    // Evento de navegación one-shot: "HOME", "LOGIN", etc.
    private final MutableLiveData<String> _navEvent = new MutableLiveData<>(null);

    public AuthViewModel(AuthRepository repo) {
        this.auth = repo.getAuth();
    }

    public LiveData<Boolean> getLoading() { return _loading; }
    public LiveData<String> getErrorMessage() { return _errorMessage; }
    public LiveData<String> getNavEvent() { return _navEvent; }

    public void consumeNavEvent() { _navEvent.setValue(null); }

    public void login(String email, String pass) {
        _errorMessage.setValue(null);

        _loading.setValue(true);
        auth.signInWithEmailAndPassword(email, pass)
                .addOnCompleteListener(task -> {
                    _loading.setValue(false);
                    if (task.isSuccessful()) {
                        _navEvent.setValue("HOME");
                    } else {
                        _errorMessage.setValue(parseAuthError(task.getException()));
                    }
                });
    }

    public void register(String email, String pass) {
        _errorMessage.setValue(null);

        _loading.setValue(true);
        auth.createUserWithEmailAndPassword(email, pass)
                .addOnCompleteListener(task -> {
                    _loading.setValue(false);
                    if (task.isSuccessful()) {
                        _navEvent.setValue("HOME");
                    } else {
                        _errorMessage.setValue(parseAuthError(task.getException()));
                    }
                });
    }

    private String parseAuthError(Exception e) {
        if (e == null) return "Error desconocido";
        String msg = e.getMessage();
        // Simplificación didáctica: mapeo básico por texto
        if (msg != null) {
            if (msg.contains("password") && msg.contains("invalid")) return "Credenciales inválidas";
            if (msg.contains("no user record")) return "No existe una cuenta con ese email";
            if (msg.contains("email address is already in use")) return "Ese email ya está registrado";
            if (msg.contains("network error")) return "Error de red. Revisa tu conexión";
        }
        return "No se pudo completar la operación";
    }
}