package com.example.aula.data;

import com.google.firebase.auth.FirebaseAuth;

public class AuthRepository {
    private final FirebaseAuth auth = FirebaseAuth.getInstance();

    public FirebaseAuth getAuth() {
        return auth;
    }
}