package com.example.aula.ui;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.core.splashscreen.SplashScreen;

import com.example.aula.R;
import com.example.aula.data.SettingsRepository;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // 1. Instanciar el repositorio de configuración para leer las preferencias guardadas
        SettingsRepository repo = new SettingsRepository(this);

        // 2. CONFIGURACIÓN DEL MODO OSCURO
        // Es crucial hacer esto ANTES del setContentView.
        // Verificamos si el usuario guardó la preferencia de modo oscuro y forzamos el modo en la app.
        AppCompatDelegate.setDefaultNightMode(
                repo.isDarkModeEnabled()
                        ? AppCompatDelegate.MODE_NIGHT_YES // Fuerza modo noche
                        : AppCompatDelegate.MODE_NIGHT_NO  // Fuerza modo día
        );

        // 3. SPLASH SCREEN (Pantalla de carga inicial)
        // Instala la nueva API de Splash Screen de Android 12+.
        // Muestra el icono de la app mientras el sistema carga el proceso.
        SplashScreen.installSplashScreen(this);

        super.onCreate(savedInstanceState);

        // 4. CARGAR LA INTERFAZ
        // R.layout.activity_main contiene el NavHostFragment, que es el contenedor
        // donde se mostrarán el Login, Registro y Home.
        setContentView(R.layout.activity_main);
    }
}