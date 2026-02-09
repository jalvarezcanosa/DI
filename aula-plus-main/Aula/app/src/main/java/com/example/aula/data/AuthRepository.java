package com.example.aula.data;

import com.google.firebase.auth.FirebaseAuth;

public class AuthRepository {

    // Interfaz para avisar al ViewModel cuando Firebase termine (ya que es asíncrono)
    public interface AuthCallback {
        void onSuccess();
        void onError(String message);
    }

    // Instancia única de Firebase (Singleton del SDK)
    private final FirebaseAuth auth = FirebaseAuth.getInstance();

    public void login(String email, String pass, AuthCallback cb) {
        // Intenta iniciar sesión en la nube
        auth.signInWithEmailAndPassword(email, pass)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        // Si todo va bien, avisamos al callback
                        cb.onSuccess();
                    } else {
                        // Si falla, traducimos el error técnico a algo legible
                        cb.onError(parseAuthError(task.getException()));
                    }
                });
    }

    public void register(String email, String pass, AuthCallback cb) {
        // Crea un usuario nuevo en Firebase
        auth.createUserWithEmailAndPassword(email, pass)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) cb.onSuccess();
                    else cb.onError(parseAuthError(task.getException()));
                });

    }

    // Verifica si ya hay un usuario logueado en caché
    public boolean isLoggedIn() {
        return auth.getCurrentUser() != null;
    }

    public void logout() {
        auth.signOut();
    }

    // Traduce errores técnicos de Firebase a español para el usuario
    private String parseAuthError(Exception e) {
        if (e == null) return "Error desconocido";
        String msg = e.getMessage();
        if (msg != null) {
            if (msg.contains("password") && msg.contains("invalid")) return "Credenciales inválidas";
            if (msg.contains("no user record")) return "No existe una cuenta con ese email";
            if (msg.contains("email address is already in use")) return "Ese email ya está registrado";
            if (msg.contains("network error")) return "Error de red. Revisa tu conexión";
        }
        return "No se pudo completar la operación";
    }

    public String getCurrentUserEmail() {
        if (auth.getCurrentUser() != null) {
            return auth.getCurrentUser().getEmail();
        }
        return "Usuario no identificado";
    }
}