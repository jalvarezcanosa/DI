package com.example.aula.ui;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.fragment.NavHostFragment;

import com.example.aula.R;
import com.example.aula.data.InMemoryNoticeRepository;
import com.example.aula.viewmodel.NoticeViewModel;
import com.example.aula.viewmodel.NoticeViewModelFactory;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.snackbar.Snackbar;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;
import com.google.firebase.auth.FirebaseAuth;

public class HomeFragment extends Fragment {

    private NoticeViewModel vm;

    public HomeFragment() {
        super(R.layout.fragment_home); // Infla el layout automáticamente
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // 1. Inicializar UI (usando 'view.' porque estamos en fragment)
        TextInputLayout tilTitle = view.findViewById(R.id.tilTitle);
        TextInputEditText etTitle = view.findViewById(R.id.etTitle);
        TextInputLayout tilSubject = view.findViewById(R.id.tilSubject);
        TextInputEditText etSubject = view.findViewById(R.id.etSubject);
        MaterialButton btnAdd = view.findViewById(R.id.btnAdd);
        MaterialButton btnDeleteLast = view.findViewById(R.id.btnDeleteLast);
        TextView tvList = view.findViewById(R.id.tvList);
        MaterialButton btnLogout = view.findViewById(R.id.btnLogout);

        // 2. ViewModel
        InMemoryNoticeRepository repo = new InMemoryNoticeRepository();
        NoticeViewModelFactory factory = new NoticeViewModelFactory(repo);
        // Usamos 'this' para que el VM muera con el fragment, o 'requireActivity()' si queremos compartir datos
        vm = new ViewModelProvider(this, factory).get(NoticeViewModel.class);

        // 3. Observers (IMPORTANTE: usar getViewLifecycleOwner())
        vm.getListado().observe(getViewLifecycleOwner(), texto -> {
            if (texto == null || texto.trim().isEmpty()) {
                tvList.setText("📭 No hay avisos todavía.\n\n¡Añade el primero arriba!");
            } else {
                tvList.setText(texto);
            }
        });

        vm.getError().observe(getViewLifecycleOwner(), err -> {
            tilTitle.setError(err); // Null limpia el error automáticamente
        });

        vm.getEventoToast().observe(getViewLifecycleOwner(), msg -> {
            if (msg != null) {
                // En fragment, view es la raíz segura para el Snackbar
                Snackbar.make(view, msg, Snackbar.LENGTH_SHORT)
                        .setAction("OK", v -> {})
                        .show();
                vm.consumirEventoToast();
            }
        });

        // 4. Listeners
        btnAdd.setOnClickListener(v -> {
            String title = (etTitle.getText() != null) ? etTitle.getText().toString() : "";
            String subject = (etSubject.getText() != null) ? etSubject.getText().toString() : "";

            vm.addNotice(title, subject);

            if (vm.getError().getValue() == null) {
                etTitle.setText("");
                tilTitle.setError(null);
            }
        });

        btnDeleteLast.setOnClickListener(v -> vm.deleteLast());

        etTitle.addTextChangedListener(new TextWatcher() {
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {}
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                tilTitle.setError(null);
            }
            public void afterTextChanged(Editable s) {}
        });

        btnLogout.setOnClickListener(v -> {
            FirebaseAuth.getInstance().signOut();
            NavHostFragment.findNavController(this)
                    .navigate(R.id.action_home_to_authGate);
        });
    }
}