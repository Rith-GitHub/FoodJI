package com.example.tgl10.foodji;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Ingredient extends AppCompatActivity {
    /* private EditText Ingredient;
    private EditText Quantity;
    private button Add;
    private textView Add_Ingredient; */

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ingredient);





    }

    public void openPantry(View view){
        Intent intent = new Intent(Ingredient.this, PantryActivity.class); //change pantry class to actual activity name for that
        startActivity(intent);
    }
}
