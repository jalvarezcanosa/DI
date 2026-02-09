package com.example.aula.ui;


import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
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

public class RegisterFragment extends Fragment {

    private AuthViewModel vm;

    public RegisterFragment() {
        super(R.layout.fragment_register);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {

        // =================================================================================
        // 1. VINCULACIÓN DE VISTAS
        // Obtenemos referencias a los elementos de la interfaz.
        // =================================================================================
        TextInputLayout tilEmail = view.findViewById(R.id.tilEmail);
        TextInputLayout tilPass = view.findViewById(R.id.tilPass);
        TextInputLayout tilPass2 = view.findViewById(R.id.tilPass2); // Campo extra para confirmar pass

        TextInputEditText etEmail = view.findViewById(R.id.etEmail);
        TextInputEditText etPass = view.findViewById(R.id.etPass);
        TextInputEditText etPass2 = view.findViewById(R.id.etPass2);

        MaterialButton btnRegister = view.findViewById(R.id.btnRegister);
        MaterialButton btnGoLogin = view.findViewById(R.id.btnGoLogin);

        CircularProgressIndicator progress = view.findViewById(R.id.progress);

        // =================================================================================
        // 2. CONFIGURACIÓN DEL VIEWMODEL
        // =================================================================================
        AuthRepository repo = new AuthRepository();
        AuthViewModelFactory factory = new AuthViewModelFactory(repo);
        vm = new ViewModelProvider(requireActivity(), factory).get(AuthViewModel.class);

        // =================================================================================
        // 3. MEJORA DE UX: LIMPIEZA DE ERRORES (TextWatcher)
        // Esto sirve para que, si sale un error rojo (ej: "Pass corta"), en cuanto el usuario
        // empiece a escribir para corregirlo, el error rojo desaparezca inmediatamente.
        // =================================================================================
        TextWatcher clearErrorsWatcher = new TextWatcher() {
            @Override public void beforeTextChanged(CharSequence s, int start, int count, int after) {}

            @Override public void onTextChanged(CharSequence s, int start, int before, int count) {
                // Al escribir cualquier cosa, quitamos los mensajes de error visuales
                tilEmail.setError(null);
                tilPass.setError(null);
                tilPass2.setError(null);
            }

            @Override public void afterTextChanged(Editable s) {}
        };
        // Añadimos este "vigilante" a los tres campos de texto
        etEmail.addTextChangedListener(clearErrorsWatcher);
        etPass.addTextChangedListener(clearErrorsWatcher);
        etPass2.addTextChangedListener(clearErrorsWatcher);

        // =================================================================================
        // 4. OBSERVADORES (LiveData)
        // =================================================================================

        // Observar Carga: Bloqueamos TODOS los campos y botones mientras se registra
        vm.getLoading().observe(getViewLifecycleOwner(), isLoading -> {
            boolean loading = Boolean.TRUE.equals(isLoading);
            btnRegister.setEnabled(!loading);
            btnGoLogin.setEnabled(!loading);

            // También deshabilitamos los inputs para que no se pueda editar mientras carga
            tilEmail.setEnabled(!loading);
            tilPass.setEnabled(!loading);
            tilPass2.setEnabled(!loading);

            if (loading) progress.show();
            else progress.hide();
        });

        // Observar Errores (Snackbar)
        vm.getErrorMessage().observe(getViewLifecycleOwner(), msg -> {
            if (msg != null) {
                Snackbar.make(view, msg, Snackbar.LENGTH_LONG).show();
            }
        });

        // Observar Navegación (Éxito -> Ir al Home)
        vm.getNavEvent().observe(getViewLifecycleOwner(), event -> {
            if (event == null) return;

            if ("HOME".equals(event)) {
                NavHostFragment.findNavController(this).navigate(R.id.action_register_to_home);
            }
            vm.consumeNavEvent();
        });

        // =================================================================================
        // 5. LISTENERS DE BOTONES
        // =================================================================================

        // Botón "Ya tengo cuenta": Vuelve al login
        btnGoLogin.setOnClickListener(v ->
                NavHostFragment.findNavController(this).navigate(R.id.action_register_to_login)
        );

        // Botón "Crear Cuenta"
        btnRegister.setOnClickListener(v -> {

            // 1. Limpieza inicial de errores
            tilEmail.setError(null);
            tilPass.setError(null);
            tilPass2.setError(null);

            // 2. Obtener textos
            String email = etEmail.getText() != null ? etEmail.getText().toString().trim() : "";
            String pass = etPass.getText() != null ? etPass.getText().toString() : "";
            String pass2 = etPass2.getText() != null ? etPass2.getText().toString() : "";

            boolean ok = true;

            // 3. VALIDACIONES

            // Validar Email
            if (email.isEmpty()) {
                tilEmail.setError("Email obligatorio");
                ok = false;
            } else if (!email.contains("@")) {
                tilEmail.setError("Email no válido");
                ok = false;
            }

            // Validar Contraseña 1
            if (pass.isEmpty()) {
                tilPass.setError("Contraseña obligatoria");
                ok = false;
            } else if (pass.length() < 6) {
                tilPass.setError("Mínimo 6 caracteres");
                ok = false;
            }

            // Validar Contraseña 2 (Confirmación)
            if (pass2.isEmpty()) {
                tilPass2.setError("Repite la contraseña");
                ok = false;
            } else if (!pass2.equals(pass)) {
                // AQUÍ ES LA CLAVE: Comprobamos que ambas contraseñas sean idénticas
                tilPass2.setError("Las contraseñas no coinciden");
                ok = false;
            }

            if (!ok) return; // Si algo falló, paramos aquí.

            // 4. Llamada al ViewModel para crear usuario en Firebase
            vm.register(email, pass);
        });
    }
}