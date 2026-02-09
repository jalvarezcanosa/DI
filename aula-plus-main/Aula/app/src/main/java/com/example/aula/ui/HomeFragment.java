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
import com.example.aula.data.InMemoryNoticeRepository;
import com.example.aula.viewmodel.NoticeViewModel;
import com.example.aula.viewmodel.NoticeViewModelFactory;
import com.example.aula.viewmodel.SettingsViewModel;
import com.example.aula.viewmodel.SettingsViewModelFactory;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.snackbar.Snackbar;
import com.google.android.material.materialswitch.MaterialSwitch;
import com.google.android.material.textfield.TextInputLayout;
import com.google.firebase.auth.FirebaseAuth;

public class HomeFragment extends Fragment {

    public HomeFragment() {
        super(R.layout.fragment_home);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {

        TextInputLayout tilTitle = view.findViewById(R.id.tilTitle);
        TextInputLayout tilSubject = view.findViewById(R.id.tilSubject);

        MaterialButton btnAdd = view.findViewById(R.id.btnAdd);
        MaterialButton btnDeleteLast = view.findViewById(R.id.btnDeleteLast);
        MaterialButton btnLogout = view.findViewById(R.id.btnLogout);
        MaterialButton btnProfile = view.findViewById(R.id.btnProfile);

        TextView tvList = view.findViewById(R.id.tvList);

        MaterialSwitch switchDark = view.findViewById(R.id.switchDarkMode);

        // 1. CONFIGURACIÓN DEL MODO OSCURO (SettingsViewModel)
        SettingsViewModelFactory settingsFactory = new SettingsViewModelFactory(requireContext());
        SettingsViewModel settingsVm = new ViewModelProvider(this, settingsFactory)
                .get(SettingsViewModel.class);

        // Observa el cambio de modo oscuro
        settingsVm.getDarkMode().observe(getViewLifecycleOwner(), enabled -> {
            if (enabled == null) return;
            // Sincroniza el switch visual
            if (switchDark.isChecked() != enabled) {
                switchDark.setChecked(enabled);
            }
            // Aplica el tema a toda la app
            AppCompatDelegate.setDefaultNightMode(
                    enabled ? AppCompatDelegate.MODE_NIGHT_YES : AppCompatDelegate.MODE_NIGHT_NO
            );
        });

        // Listener del Switch: cuando el usuario toca, actualiza el ViewModel
        switchDark.setOnCheckedChangeListener((buttonView, isChecked) -> {
            settingsVm.setDarkMode(isChecked);
        });

        // 2. GESTIÓN DE AVISOS (NoticeViewModel)
        InMemoryNoticeRepository repo = InMemoryNoticeRepository.getInstance();
        NoticeViewModelFactory noticeFactory = new NoticeViewModelFactory(repo);
        NoticeViewModel noticeVm = new ViewModelProvider(this, noticeFactory)
                .get(NoticeViewModel.class);

        // Actualiza el TextView grande cuando cambia la lista
        noticeVm.getListado().observe(getViewLifecycleOwner(), tvList::setText);

        noticeVm.getError().observe(getViewLifecycleOwner(), err -> {
            if (err != null) Snackbar.make(view, err, Snackbar.LENGTH_LONG).show();
        });

        noticeVm.getEventoToast().observe(getViewLifecycleOwner(), msg -> {
            if (msg != null) {
                Snackbar.make(view, msg, Snackbar.LENGTH_SHORT).show();
                noticeVm.consumirEventoToast();
            }
        });

        // 3. LÓGICA DEL BOTÓN AÑADIR
        btnAdd.setOnClickListener(v -> {
            tilTitle.setError(null);

            if (tilTitle.getEditText() == null || tilSubject.getEditText() == null) {
                Snackbar.make(view, "Error en el layout: falta EditText dentro del TextInputLayout", Snackbar.LENGTH_LONG).show();
                return;
            }

            // ... validaciones de nulos ...
            String title = tilTitle.getEditText().getText().toString().trim();
            String subject = tilSubject.getEditText().getText().toString().trim();

            // Llama al ViewModel para añadir (él se encarga de la lógica de negocio)
            noticeVm.addNotice(title, subject);
            // Limpia el campo de texto
            tilTitle.getEditText().setText("");
        });

        btnDeleteLast.setOnClickListener(v -> noticeVm.deleteLast());

        btnLogout.setOnClickListener(v -> {
            FirebaseAuth.getInstance().signOut();
            NavHostFragment.findNavController(this)
                    .navigate(R.id.action_home_to_authGate);
        });

        btnProfile.setOnClickListener(v -> {
            NavHostFragment.findNavController(this).navigate(R.id.action_home_to_profile);
        });
    }
}
