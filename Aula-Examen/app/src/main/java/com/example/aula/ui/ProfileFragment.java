package com.example.aula.ui;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.fragment.NavHostFragment;

import com.example.aula.R;
import com.example.aula.data.AuthRepository;
import com.example.aula.viewmodel.AuthViewModel;
import com.example.aula.viewmodel.AuthViewModelFactory;
import com.example.aula.viewmodel.SettingsViewModel;
import com.example.aula.viewmodel.SettingsViewModelFactory;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.materialswitch.MaterialSwitch;
import com.google.firebase.auth.FirebaseAuth;

import org.w3c.dom.Text;

public class ProfileFragment extends Fragment {

    AuthViewModel vm;

    public ProfileFragment() {
        super(R.layout.profile_fragment);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        TextView profileText = view.findViewById(R.id.ProfileText);
        TextView uidText = view.findViewById(R.id.uidText);

        MaterialSwitch switchDark = view.findViewById(R.id.switchDarkMode);
        MaterialButton btnLogout = view.findViewById(R.id.btnLogout);

        SettingsViewModelFactory settingsFactory = new SettingsViewModelFactory(requireContext());
        SettingsViewModel settingsVm = new ViewModelProvider(this, settingsFactory)
                .get(SettingsViewModel.class);

        AuthRepository repo = new AuthRepository();
        AuthViewModelFactory factory = new AuthViewModelFactory(repo);

        vm = new ViewModelProvider(this, factory).get(AuthViewModel.class);

        settingsVm.getDarkMode().observe(getViewLifecycleOwner(), enabled -> {
            if (enabled == null) return;

            if (switchDark.isChecked() != enabled) {
                switchDark.setChecked(enabled);
            }

            AppCompatDelegate.setDefaultNightMode(
                    enabled ? AppCompatDelegate.MODE_NIGHT_YES : AppCompatDelegate.MODE_NIGHT_NO
            );
        });

        switchDark.setOnCheckedChangeListener((buttonView, isChecked) -> {
            settingsVm.setDarkMode(isChecked);
        });

        vm.getNavEvent().observe(getViewLifecycleOwner(), event -> {
            if ("LOGIN".equals(event)) {
                NavHostFragment.findNavController(this).navigate(R.id.action_profile_to_authGate);
                vm.consumeNavEvent();
            }
        });

        vm.get_uid().observe(getViewLifecycleOwner(), uid -> {
            if (uid != null) {
                uidText.setText(uid);
            }
        });

        btnLogout.setOnClickListener(v -> {
            vm.logout();
        });

        vm.loadUID();

    }
}
