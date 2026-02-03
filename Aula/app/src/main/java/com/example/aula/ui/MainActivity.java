package com.example.aula.ui;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import com.example.aula.R;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // La Activity ya no hace NADA más. Todo lo delega al NavHost.
    }
}