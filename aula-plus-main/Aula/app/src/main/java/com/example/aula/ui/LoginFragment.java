package com.example.aula.ui;

import android.os.Bundle;
import android.view.View;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.fragment.NavHostFragment;

import com.example.aula.R;
import com.example.aula.data.AuthRepository;
import com.example.aula.viewmodel.AuthViewModel;
import com.example.aula.viewmodel.AuthViewModelFactory;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.progressindicator.CircularProgressIndicator;
import com.google.android.material.snackbar.Snackbar;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

public class LoginFragment extends Fragment {

    // Referencia al ViewModel que contendrá la lógica de negocio (comunicarse con Firebase)
    private AuthViewModel vm;

    // Constructor: Infla (carga) el layout 'fragment_login.xml' automáticamente al crear el fragmento
    public LoginFragment() { super(R.layout.fragment_login); }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {

        // =================================================================================
        // 1. VINCULACIÓN DE VISTAS (BINDING)
        // Buscamos los elementos visuales del XML por su ID para poder manipularlos.
        // =================================================================================

        // TextInputLayout: Contenedores de los campos de texto (útiles para mostrar mensajes de error)
        TextInputLayout tilEmail = view.findViewById(R.id.tilEmail);
        TextInputLayout tilPass = view.findViewById(R.id.tilPass);

        // TextInputEditText: Donde el usuario escribe realmente
        TextInputEditText etEmail = view.findViewById(R.id.etEmail);
        TextInputEditText etPass = view.findViewById(R.id.etPass);

        // Botones y Spinner de carga
        MaterialButton btnLogin = view.findViewById(R.id.btnLogin);
        MaterialButton btnGoRegister = view.findViewById(R.id.btnGoRegister);
        CircularProgressIndicator progress = view.findViewById(R.id.progress);

        // =================================================================================
        // 2. CONFIGURACIÓN DEL VIEWMODEL (MVVM)
        // Preparamos las piezas necesarias para iniciar el ViewModel
        // =================================================================================

        AuthRepository repo = new AuthRepository();            // Capa de datos
        AuthViewModelFactory factory = new AuthViewModelFactory(repo); // Fábrica para crear el VM

        // Obtenemos el ViewModel. Usamos 'requireActivity()' para que el ViewModel esté asociado
        // a la Actividad padre. Esto es útil si quisiéramos compartir datos entre Login y Register.
        vm = new ViewModelProvider(requireActivity(), factory).get(AuthViewModel.class);

        // =================================================================================
        // 3. OBSERVADORES (LiveData)
        // Aquí la UI "reacciona" a los cambios de estado del ViewModel
        // =================================================================================

        // A. Observar estado de carga (Loading)
        // Si cambia a 'true', mostramos el spinner y desactivamos botones para evitar doble clic.
        vm.getLoading().observe(getViewLifecycleOwner(), isLoading -> {
            boolean loading = Boolean.TRUE.equals(isLoading);
            btnLogin.setEnabled(!loading);
            btnGoRegister.setEnabled(!loading);

            if (loading) {
                progress.show();
            } else {
                progress.hide();
            }
        });

        // B. Observar mensajes de error
        // Si el login falla (ej: contraseña incorrecta), mostramos un Snackbar (aviso flotante inferior).
        vm.getErrorMessage().observe(getViewLifecycleOwner(), msg -> {
            if (msg != null) {
                Snackbar.make(view, msg, Snackbar.LENGTH_LONG).show();
            }
        });

        // C. Observar eventos de navegación
        // Si el ViewModel nos dice "HOME", significa que el login fue exitoso.
        vm.getNavEvent().observe(getViewLifecycleOwner(), event -> {
            if (event == null) return;

            if (event.equals("HOME")) {
                // Usamos NavController para cambiar de pantalla (del Login al Home)
                NavHostFragment.findNavController(this)
                        .navigate(R.id.action_login_to_home);
            }
            // Importante: Consumimos el evento para que no se repita si rotamos la pantalla
            vm.consumeNavEvent();
        });

        // =================================================================================
        // 4. LISTENERS DE BOTONES (Interacción del usuario)
        // =================================================================================

        // Botón "Ir a Registro": Simplemente navega a la pantalla de registro
        btnGoRegister.setOnClickListener(v ->
                NavHostFragment.findNavController(this)
                        .navigate(R.id.action_login_to_register)
        );

        // Botón "Entrar" (Login)
        btnLogin.setOnClickListener(v -> {
            // 1. Limpiamos errores visuales previos (si los hubiera)
            tilEmail.setError(null);
            tilPass.setError(null);

            // 2. Obtenemos el texto escrito (protegemos contra nulos)
            String email = etEmail.getText() != null ? etEmail.getText().toString().trim() : "";
            String pass = etPass.getText() != null ? etPass.getText().toString() : "";

            // 3. VALIDACIÓN LOCAL
            // Comprobamos reglas básicas antes de molestar al servidor (ahorra datos y tiempo)
            boolean ok = true;

            if (email.isEmpty()) {
                tilEmail.setError("Email obligatorio"); // Muestra error rojo en el input
                ok = false;
            }
            else if (!email.contains("@")) {
                tilEmail.setError("Email no válido");
                ok = false;
            }

            if (pass.isEmpty()) {
                tilPass.setError("Contraseña obligatoria");
                ok = false;
            }
            else if (pass.length() < 6) {
                tilPass.setError("Mínimo 6 caracteres");
                ok = false;
            }

            // Si alguna validación falló, detenemos la ejecución aquí
            if (!ok) return;

            // 4. Si todo está correcto, llamamos al ViewModel para iniciar sesión en Firebase
            vm.login(email, pass);
        });
    }
}