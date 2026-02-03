package com.example.aula.ui;

import androidx.fragment.app.Fragment;
import com.example.aula.R;
import android.os.Bundle;
import android.view.View;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.fragment.NavHostFragment;
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

    public RegisterFragment() { super(R.layout.fragment_register); }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {

        TextInputLayout tilEmail = view.findViewById(R.id.tilEmail);
        TextInputLayout tilPass = view.findViewById(R.id.tilPass);
        TextInputLayout tilPass2 = view.findViewById(R.id.tilPass2);
        TextInputEditText etEmail = view.findViewById(R.id.etEmail);
        TextInputEditText etPass = view.findViewById(R.id.etPass);
        TextInputEditText etPass2 = view.findViewById(R.id.etPass2);


        MaterialButton btnRegister = view.findViewById(R.id.btnRegister);
        CircularProgressIndicator progress = view.findViewById(R.id.progress);

        AuthRepository repo = new AuthRepository();
        AuthViewModelFactory factory = new AuthViewModelFactory(repo);
        vm = new ViewModelProvider(this, factory).get(AuthViewModel.class);

        // OBSERVAR loading
        vm.getLoading().observe(getViewLifecycleOwner(), isLoading -> {
            boolean loading = Boolean.TRUE.equals(isLoading);
            btnRegister.setEnabled(!loading);
            if (loading) {
                progress.show();
            } else {
                progress.hide();
            }
        });

        // OBSERVAR error (Snackbar)
        vm.getErrorMessage().observe(getViewLifecycleOwner(), msg -> {
            if (msg != null) {
                Snackbar.make(view, msg, Snackbar.LENGTH_LONG).show();
            }
        });

        // OBSERVAR navegación one-shot
        vm.getNavEvent().observe(getViewLifecycleOwner(), event -> {
            if (event == null) return;
            if (event.equals("HOME")) {
                NavHostFragment.findNavController(this)
                        .navigate(R.id.action_register_to_home);
            }
            vm.consumeNavEvent();
        });

        btnRegister.setOnClickListener(v -> {
            // 1) limpiar errores
            tilEmail.setError(null);
            tilPass.setError(null);

            // 2) validar local
            String email = etEmail.getText() != null ? etEmail.getText().toString().trim() : "";
            String pass = etPass.getText() != null ? etPass.getText().toString() : "";

            boolean ok = true;
            if (email.isEmpty()) { tilEmail.setError("Email obligatorio"); ok = false; }
            else if (!email.contains("@")) { tilEmail.setError("Email no válido"); ok = false; }

            if (pass.isEmpty()) { tilPass.setError("Contraseña obligatoria"); ok = false; }
            else if (pass.length() < 6) { tilPass.setError("Mínimo 6 caracteres"); ok = false; }
            else if (!pass.equals(etPass2.getText().toString())) {
                tilPass2.setError("Las contraseñas no coinciden");
            }

            if (!ok) return;

            // 3) llamar al VM
            vm.register(email, pass);
        });
    }
}