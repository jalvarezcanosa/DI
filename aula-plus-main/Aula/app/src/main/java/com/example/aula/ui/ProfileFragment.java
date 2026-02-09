package com.example.aula.ui;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.fragment.NavHostFragment;

import com.example.aula.R;
import com.example.aula.data.AuthRepository;
import com.example.aula.viewmodel.AuthViewModel;
import com.example.aula.viewmodel.AuthViewModelFactory;
import com.google.android.material.button.MaterialButton;

public class ProfileFragment extends Fragment {
    private AuthViewModel vm;

    public ProfileFragment() {
        super(R.layout.fragment_profile);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        TextView Username = view.findViewById(R.id.Username);
        MaterialButton btnLogout = view.findViewById(R.id.btnLogout);

        AuthRepository repo = new AuthRepository();
        AuthViewModelFactory factory = new AuthViewModelFactory(repo);
        // Usamos requireActivity() para compartir estado si fuera necesario, o 'this' si es local
        vm = new ViewModelProvider(this, factory).get(AuthViewModel.class);

        // Observamos el email y lo pintamos en el TextView
        vm.getCurrentUserEmail().observe(getViewLifecycleOwner(), email -> {
            if (email != null) Username.setText(email);
        });

        vm.getNavEvent().observe(getViewLifecycleOwner(), event -> {
                    if ("LOGIN".equals(event)) {
                        NavHostFragment.findNavController(this).navigate(R.id.action_profile_to_login);
                        vm.consumeNavEvent();
                    }
                }
        );

        btnLogout.setOnClickListener(v -> {
            vm.logout();
        });

        vm.loadUserProfile();

    }

}
