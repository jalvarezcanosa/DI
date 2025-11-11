package com.example.catalogactivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.fragment.app.Fragment;

public class CatalogFragment extends Fragment {

    public CatalogFragment() {

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_catalog, container, false);

        Button navigateButton = view.findViewById(R.id.navigate_button);
        navigateButton.setOnClickListener(v -> {
            Intent intent = new Intent(getActivity(), DetailViewsActivity.class);
            startActivity(intent);
        });

        return view;
    }
}
