package com.example.aula.data;

import java.util.ArrayList;
import java.util.List;

public class InMemoryNoticeRepository {

    // SINGLETON: Garantiza que solo exista UNA lista de avisos en toda la app
    private static InMemoryNoticeRepository instance;
    private final List<String> database = new ArrayList<>();

    // Constructor privado: solo se puede llamar desde dentro
    public InMemoryNoticeRepository() {
        // Datos iniciales de prueba
        database.add("DI | Entrega README");
        database.add("SI | Repasar permisos Linux");
    }

    // Método para obtener la instancia única
    public static synchronized InMemoryNoticeRepository getInstance() {
        if (instance == null) instance = new InMemoryNoticeRepository();
        return instance;
    }

    // Devuelve una COPIA de la lista para evitar errores de concurrencia
    public List<String> getAll() {
        return new ArrayList<>(database);
    }

    // Añade al principio de la lista (índice 0) para que salga arriba
    public void add(String noticeText) {
        database.add(0, noticeText);
    }

    public boolean removeLast() {
        if (database.isEmpty()) return false;
        database.remove(database.size() - 1);
        return true;
    }
}