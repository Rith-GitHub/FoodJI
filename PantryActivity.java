package com.example.tgl10.foodji;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class PantryActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pantry);
    }

    public void add(View view){
        Intent intent = new Intent(PantryActivity.this, Ingredient.class); //change pantry class to actual activity name for that
        startActivity(intent);
    }
}

